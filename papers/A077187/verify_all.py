#!/usr/bin/env python3
"""Fully local 3^8 smooth-order verification from generated norm and gcd tables."""
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).parent
def run(script):
    print('RUN',script,flush=True)
    subprocess.run([sys.executable,str(ROOT/script)],cwd=ROOT,check=True)
if __name__=='__main__':
    run('audit_all_b8.py')
    run('check_direct_b8.py')
    import exact_b8_fast as e
    from tower_norm import full_norm
    for gamma in (1,202,247,547,698):
        N=full_norm(e.crosscheck(gamma),6)
        for q in (2,3,5):
            while N%q==0:N//=q
        assert N==int((ROOT/f'norm_gamma_{gamma}.txt').read_text())
        print('PASS regenerated norm',gamma,flush=True)
    assert len((ROOT/'all_486_gmp.tsv').read_text().splitlines())==486
    print('PASS ALL 486 certified phase rows; theorem remains partial for general p')
