# Full-prefix pointwise square candidates

The proof in `LATE_PREFIX_POINTWISE_ENUMERATION.md` reduces every fixed cut k>=10, in the exact region R_(m,k)<H_k^2, to at most eight explicit least modular roots. Each root's squared decimal length either rejects it or determines one endpoint for an exact equality test. It gives complete effective enumeration, not an infinite nonexistence theorem.

A simple guaranteed region is

    k<m, D(m)<=2D(k)-2digits(k).

For same-width cuts beyond the theorem's explicit midpoint threshold, this includes every later endpoint in the width. Earlier-width and cross-boundary endpoint positions require no separate exception within the displayed region.

## Files

- `LATE_PREFIX_POINTWISE_ENUMERATION.md`: theorem, proof, scope, and exact endpoint characterization.
- `verify_late_prefix_candidates.py`: standard-library exact enumeration and certificate generator.
- `late-prefix-1000-certificate.json` and `late-prefix-1000-verification.txt`: completed smaller audit.
- `late-prefix-10000-certificate.json`: completed full cutwise audit.
- `late-prefix-10000-summary.json`: compact summary and source/certificate hashes, generated from the full certificate.
- `summarize_certificate.py`: reproduce the compact summary.
- `LATE_PREFIX_INDEPENDENT_AUDIT.md`: independent mathematical and computational review, with its own explicitly stated scope.
- `verify_late_prefix_independent.py` and `verify_late_prefix_coverage_10000.py`: independent verifier programs, with companion result files. The added exact-endpoint check is recorded in `late-prefix-independent-exact-endpoint-results.json`.

Run the main audit and summarize it:

    python verify_late_prefix_candidates.py --max-cut 10000 --output late-prefix-10000-certificate.json
    python summarize_certificate.py

Pair coverage counts refer to the guaranteed finite digit-count region. Most cuts are already excluded by the 2/5 local tests; the summary reports coverage at locally surviving cuts separately. No claim is made that all covered pairs are newly excluded by this method or that observed absence extends beyond the verified finite domain.
