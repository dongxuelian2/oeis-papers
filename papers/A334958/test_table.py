#!/usr/bin/env python3
"""Regression tests for complete A334958 b-file validation."""
from pathlib import Path
import tempfile
import unittest

from verify import audit_table


class TableAuditTests(unittest.TestCase):
    def setUp(self):
        self.rows = [line for line in Path(__file__).with_name('b334958.txt')
                     .read_text().splitlines() if not line.startswith('#')]

    def check_rows(self, rows):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'table.txt'
            path.write_text('\n'.join(rows) + '\n')
            audit_table(path)

    def test_valid_table_and_comments(self):
        self.check_rows(['', '  # comment', *self.rows, ' '])

    def test_incomplete_tables(self):
        for rows in ([], self.rows[:-1], self.rows[1:]):
            with self.subTest(length=len(rows)), self.assertRaises(AssertionError):
                self.check_rows(rows)

    def test_extra_row(self):
        with self.assertRaises(AssertionError):
            self.check_rows(self.rows + ['101 0'])

    def test_wrong_index_with_unchanged_value(self):
        rows = self.rows.copy()
        rows[1] = '1 1'  # Value agrees, but index 2 has been duplicated as 1.
        with self.assertRaises(AssertionError):
            self.check_rows(rows)

    def test_wrong_value(self):
        rows = self.rows.copy()
        rows[-1] = '100 0'
        with self.assertRaises(AssertionError):
            self.check_rows(rows)

    def test_extra_column(self):
        rows = self.rows.copy()
        rows[0] += ' 42'
        with self.assertRaises(AssertionError):
            self.check_rows(rows)


if __name__ == '__main__':
    unittest.main()
