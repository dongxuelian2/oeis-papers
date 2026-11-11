#!/usr/bin/env python3
"""Run the submission's finite checks; standard library only, no matching solver.

AI-assisted audit tooling (2026-11-01); not journal manuscript prose.
Run from any directory. The JSON report identifies the exact checked bytes.
Infinite conclusions still require the mathematical proofs in main.tex.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
CHECKS = (
    "test_certificates.py",
    "verify_56_plus_forcing.py",
    "verify_forced_peeling.py",
    "verify_extended.py",
    "verify_eventual_involutions.py",
)
SOURCES = CHECKS + ("reproduce.py", "verify.py", "verify_57_plus_templates.py")
DATA = (
    "finite_56_cubic_order_shapes.txt", "exact_classification_below_173.json",
    "core_109.json", "base_permutations.json", "core_60_with_empty.json",
    "second_solutions.json", "third_solutions.json",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path,
                        help="write machine-readable results (including failures)")
    args = parser.parse_args()
    if not __debug__:
        parser.error("assertions must be enabled: do not use -O or PYTHONOPTIMIZE")
    paths = [HERE / name for name in SOURCES]
    paths += [HERE / "certificates" / name for name in DATA]
    paths += [HERE / "main.tex", HERE / "appendix.tex"]
    report = {
        "python": platform.python_version(),
        "scope": "finite certificates and regression tests; not independent peer review",
        "sha256": {str(p.relative_to(HERE)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in sorted(paths)},
        "checks": [],
    }
    env = os.environ.copy()
    env.pop("PYTHONOPTIMIZE", None)
    failed = False
    for name in CHECKS:
        print(f"=== {name} ===", flush=True)
        start = time.monotonic()
        result = subprocess.run([sys.executable, "-B", str(HERE / name)],
                                cwd=HERE, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(result.stdout, end="", flush=True)
        report["checks"].append({"script": name, "returncode": result.returncode,
                                 "elapsed_seconds": round(time.monotonic()-start, 3),
                                 "output": result.stdout})
        failed |= result.returncode != 0
    report["passed"] = not failed
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("FINITE CHECKS PASS" if not failed else "FINITE CHECKS FAILED")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
