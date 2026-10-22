"""Regenerate all 486 exact integer norms; no heuristic sampling."""
from multiprocessing import Pool
from pathlib import Path
import json,sys,time
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent
def task(g):
    from exact_b8_fast import crosscheck
    from tower_norm import full_norm
    start=time.monotonic()
    N=full_norm(crosscheck(g),6)
    assert N>0
    for q in (2,3,5):
        while N%q==0:N//=q
    assert N>1
    (ROOT/f'norm_gamma_{g}.txt').write_text(str(N)+'\n')
    return g,len(str(N)),round(time.monotonic()-start,3)
if __name__=='__main__':
    phases=[g for g in range(1,729) if g%3]
    start=time.monotonic()
    with Pool(processes=4) as pool:
        results=[]
        for z in pool.imap_unordered(task,phases,chunksize=1):
            results.append(z)
            if len(results)%25==0:
                print('PROGRESS',len(results),'/486','seconds',round(time.monotonic()-start,1),flush=True)
        (ROOT/'norm_summary.json').write_text(json.dumps(sorted(results),indent=2)+'\n')
    print('COMPLETE',len(results),'seconds',round(time.monotonic()-start,1))
