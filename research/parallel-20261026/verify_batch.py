#!/usr/bin/env python3
"""Run the complete parallel OEIS batch from any working directory."""
import argparse
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
PAPERS = (
    'A048702', 'A079495', 'A084043', 'A085124', 'A195608',
    'A214972-A152009', 'A236383', 'A248520-A248521', 'A340138', 'A393833',
    'A005046', 'A092635', 'A136050', 'A237930', 'A260056',
    'A308090', 'A308620', 'A334595', 'A334958', 'A357127',
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--compile-papers', action='store_true',
                        help='compile all sources twice and reject LaTeX warnings')
    args = parser.parse_args()
    for name in PAPERS:
        folder = ROOT/'papers'/name
        print(f'Checking {name}', flush=True)
        if args.compile_papers:
            with tempfile.TemporaryDirectory(prefix='oeis-latex-') as output:
                command = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                           f'-output-directory={output}', 'main.tex']
                for _ in range(2):
                    result = subprocess.run(command, cwd=folder, stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT, text=True)
                    if result.returncode:
                        raise SystemExit(result.stdout)
                log = (Path(output)/'main.log').read_text()
                issues = [line for line in log.splitlines() if any(marker in line for marker in
                          ('Warning', 'Overfull', 'Underfull', 'undefined', 'Missing character'))]
                if issues:
                    raise SystemExit(f'{name}: {issues}')
                print(f'PASS {name}: two LaTeX passes, no layout/reference warnings', flush=True)
        else:
            subprocess.run([sys.executable, str(folder/'verify.py')], cwd=ROOT, check=True)
    if not args.compile_papers:
        subprocess.run([sys.executable, str(ROOT/'research/parallel-20261026/greedy/a085061_counterexamples.py')],
                       cwd=ROOT, check=True)
    print(f'PASS complete {len(PAPERS)}-paper batch', flush=True)


if __name__ == '__main__':
    main()
