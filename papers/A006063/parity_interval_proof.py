#!/usr/bin/env python3
"""Second, algorithmically independent parity-minimal involution certificate.

Uses *integer-interval union algebra in the parity coordinate* t=(n-p)/2
rather than pointwise dynamic programming or matching search.

Under reflection through an ODD cube c=k^3 (k odd), the length maps as
  n' = c-n-1,   t' = d-t,
  d=(c-1-2*p)//2,
where p=seed%2.
The strict extension n'>n means t<d/2.
For each interval t in [a,b], cap t'<=Tcap and strictness give

  lower=max(a,d-Tcap); upper=min(b,(d-1)//2).
  If lower<=upper, append [d-upper,d-lower].

Merge integer intervals after each simultaneous round.

Both parity-specific finite base windows [70001,100001] (odd) and
[230000,302000] (even) are covered by round 12; no full permutation
is stored or solved for. The infinite odd-cube induction is separate.
"""
EXPECTED={
    7:{
        "cap":100001, "lo":70001,"hi":100001,
        "pieces":(1,23,238,1377,4453,7670,8420,7628,6054,4427,3458,3104,2997),
        "totals":(1,23,238,1437,5472,13172,22217,29816,35177,38596,40262,40861,41057),
    },
    26:{
        "cap":302000,"lo":230000,"hi":302000,
        "pieces":(1,33,467,3684,15217,25148,22123,14362,8941,7562,7216,7089,7047),
        "totals":(1,33,468,3858,19471,53458,88477,109663,118384,120695,121355,121621,121707),
    },
}


def union(intervals):
    result=[]
    for a,b in sorted(intervals):
        assert 0<=a<=b
        if result and a<=result[-1][1]+1:
            result[-1]=(result[-1][0],max(result[-1][1],b))
        else:
            result.append((a,b))
    return result


def check(seed):
    cfg=EXPECTED[seed]
    cap,lo,hi=cfg["cap"],cfg["lo"],cfg["hi"]
    parity=seed%2
    Tcap=(cap-parity)//2
    roots=[]
    for k in range(3,100,2):
        if k**3>2*cap:break
        d=(k**3-1-2*parity)//2
        roots.append((k,d))
    s=(seed-parity)//2
    intervals=[(s,s)]
    for depth in range(13):
        assert len(intervals)==cfg["pieces"][depth],(seed,depth,"pieces")
        total=sum(b-a+1 for a,b in intervals)
        assert total==cfg["totals"][depth],(seed,depth,"total")
        if depth==12:
            x=(lo-parity)//2
            y=(hi-parity)//2
            contain=[(a,b) for a,b in intervals if a<=x and y<=b]
            assert len(contain)==1,(seed,contain)
            print(f"PASS seed={seed}: {depth} interval rounds, "
                  f"{total} reachable parity lengths; "
                  f"target {lo}..{hi} lies in interval "
                  f"{(2*contain[0][0]+parity,2*contain[0][1]+parity)}.")
            break
        out=list(intervals)
        for a,b in intervals:
            for k,d in roots:
                lower=max(a,d-Tcap)
                upper=min(b,(d-1)//2)
                if lower<=upper:
                    assert lower<d-lower
                    out.append((d-upper,d-lower))
        intervals=union(out)
    assert cap%2==parity


def main():
    check(7)
    check(26)
    print("CERTIFIED: both parity-minimal fixed-point finite windows "
          "by 12 rounds of symbolic interval arithmetic.")


if __name__=="__main__":
    main()
