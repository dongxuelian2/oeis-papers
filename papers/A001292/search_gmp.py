"""Finite all-exponent test of block rotations, with exact GMP integers."""
import ctypes as C
from ctypes.util import find_library
from collections import Counter
import sys, time, json
from math import isqrt

sys.set_int_max_str_digits(200000)
G = C.CDLL(find_library('gmp'))
class Z(C.Structure):
    _fields_ = [('alloc', C.c_int), ('size', C.c_int), ('limbs', C.POINTER(C.c_ulong))]
P = C.POINTER(Z)
def bind(name, args, result=None):
    f = getattr(G, '__gmpz_' + name)
    f.argtypes, f.restype = args, result
    return f
init = bind('init', [P]); clear = bind('clear', [P])
set_z = bind('set', [P, P]); set_str = bind('set_str', [P, C.c_char_p, C.c_int], C.c_int)
mul_ui = bind('mul_ui', [P, P, C.c_ulong]); add_ui = bind('add_ui', [P, P, C.c_ulong])
submul_ui = bind('submul_ui', [P, P, C.c_ulong])
cmp_z = bind('cmp', [P, P], C.c_int)
pp = bind('perfect_power_p', [P], C.c_int)
wp, mp, rp, tp = [Z() for _ in range(4)]
w, M, R, temp = [C.byref(z) for z in (wp, mp, rp, tp)]
for z in (w, M, R, temp): init(z)

# Independent exact audit of the GMP predicate for all small inputs.
def root(n, e):
    lo, hi = 0, 1 << ((n.bit_length() + e - 1)//e)
    while lo+1 < hi:
        v=(lo+hi)//2
        if v**e <= n: lo=v
        else: hi=v
    return lo
for n in range(2, 10001):
    set_str(temp, str(n).encode(), 10)
    expected = any(root(n,e)**e == n for e in range(2,n.bit_length()))
    assert bool(pp(temp)) == expected, n
print('PASS independent all-exponent predicate audit on 2..10000', flush=True)
limit=int(sys.argv[1]) if len(sys.argv)>1 else 5000
start=time.monotonic(); counts=Counter(); D=0; found=[]
for m in range(1,limit+1):
    d=len(str(m)); B=10**d
    mul_ui(w,w,B); add_ui(w,w,m)
    mul_ui(M,M,B); add_ui(M,M,B-1)
    D+=d
    if m==1: continue
    reason=None
    if m%9 in (2,3,5,6): reason='proved_mod9'
    elif m%27==9 or (m%27==17 and d%3==0): reason='proved_mod27'
    if reason:
        counts[reason]+=m
        continue
    set_z(R,w)
    for k in range(0,m):
        if k:
            mul_ui(R,R,10**len(str(k))); submul_ui(R,M,k)
        if m<=120:
            text=''.join(str(i) for i in range(k+1,m+1))+''.join(str(i) for i in range(1,k+1))
            set_str(temp,text.encode(),10)
            assert cmp_z(R,temp)==0,(m,k)
        if pp(R):
            found.append({'m':m,'cut':k})
            print('COUNTEREXAMPLE',found[-1],flush=True)
            raise SystemExit(1)
        counts['gmp_all_exponents']+=1
    mul_ui(R,R,B);submul_ui(R,M,m)
    assert cmp_z(R,w)==0,('roundtrip',m)
    if m%500==0:
        print(json.dumps({'m':m,'digits':D,'seconds':round(time.monotonic()-start,2),'counts':dict(counts)}),flush=True)
assert sum(counts.values())==limit*(limit+1)//2-1
result={'limit':limit,'total_rotations':sum(counts.values()),'counts':dict(counts),'counterexamples':found,'seconds':round(time.monotonic()-start,3)}
print('RESULT',json.dumps(result,sort_keys=True),flush=True)
for z in (w,M,R,temp):clear(z)
