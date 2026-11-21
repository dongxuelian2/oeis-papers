#!/usr/bin/env python3
"""AI-assisted regression tests for certificate rejection and interval closure."""
import copy
import unittest
from unittest.mock import patch

import verify
import verify_56_plus_forcing as shapes
import verify_57_plus_templates as templates
import verify_eventual_involutions as involutions
import verify_extended as extended


class CertificateTests(unittest.TestCase):
    def test_invalid_permutations_rejected(self):
        for p in ([7]*7, [True]+list(range(2,8)), list(range(1,8))):
            with self.assertRaises(AssertionError):
                verify.check(7, p)

    def test_invalid_shape_size_rejected(self):
        n, (roots, order) = next(iter(shapes.read_shapes().items()))
        with self.assertRaises(AssertionError):
            shapes.verify_shape(n+1, roots, order)

    def test_duplicate_classification_rejected(self):
        original = extended.read("exact_classification_below_173.json")
        broken = copy.deepcopy(original)
        broken["positive"].append(broken["positive"][0])
        with patch.object(extended, "read", return_value=broken):
            with self.assertRaises(AssertionError):
                extended.check_small()

    def test_hall_witness_corruption_rejected(self):
        broken = copy.deepcopy(extended.read("exact_classification_below_173.json"))
        broken["negative"][0]["S"] = []
        with patch.object(extended, "read", return_value=broken):
            with self.assertRaises(AssertionError):
                extended.check_small()

    def test_invalid_cycles_rejected(self):
        p = [8-i for i in range(1,8)]
        for cycle in ([], [1], [1,1], [0,1], [1,2]):
            with self.assertRaises(AssertionError):
                extended.check_cycle(p, cycle)

    def test_compact_certificate_keys(self):
        original_read = extended.read
        original = original_read("core_109.json")
        for key in ("0173", "+173", " 173", "not-an-index", "365"):
            broken = copy.deepcopy(original)
            broken[key] = ["invalid witness"]
            with self.subTest(key=key):
                with patch.object(extended, "read", side_effect=lambda name:
                                  broken if name == "core_109.json" else original_read(name)):
                    with self.assertRaises(AssertionError):
                        extended.check_compact()

        replaced = copy.deepcopy(original)
        replaced["0173"] = replaced.pop("173")
        with patch.object(extended, "read", return_value=replaced):
            with self.assertRaises(AssertionError):
                extended.check_compact()

        missing = copy.deepcopy(original)
        del missing["173"]
        with patch.object(extended, "read", return_value=missing):
            with self.assertRaises(AssertionError):
                extended.check_compact()

    def test_compact_certificates(self):
        constructed, archive = extended.check_compact()
        self.assertEqual(set(constructed), set(range(173, 365)))
        self.assertEqual(len(archive), 192)

    def test_template_witnesses(self):
        for n, blocks in templates.parametric_rows().items():
            p, start = [], 0
            for end, root in blocks:
                p.extend(root**3-i for i in range(start+1, end+1))
                start = end
            verify.check(n, p)

    def test_interval_union_against_explicit_sets(self):
        # Independent direct finite reflection enumeration, not interval algebra.
        for seed, cap in ((7, 301), (26, 500)):
            known = {seed}
            for depth in range(6):
                parity = seed & 1
                intervals = involutions.closure(seed, cap, depth)
                expanded = {2*t+parity for a,b in intervals for t in range(a,b+1)}
                self.assertEqual(expanded, known)
                additional = set(known)
                for m in known:
                    for root in range(3, 11, 2):
                        n = root**3-m-1
                        if m < n <= cap:
                            additional.add(n)
                known = additional


if __name__ == "__main__":
    unittest.main(verbosity=2)
