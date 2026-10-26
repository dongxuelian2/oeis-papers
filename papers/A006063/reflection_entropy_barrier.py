#!/usr/bin/env python3
"""Independent audit of the strict-reflection entropy and depth barrier.

Mathematical facts proved in main.tex:
- consecutive reflection cubes strictly increase;
- a root sequence is an increasing subset of {2,...,K(n)};
- F(n) <= 2**(K(n)-1), where K(n)=floor((2*n)**(1/3));
- the number of lengths <= N reachable from one seed within depth <=r
  is <= sum_{j=0}^r binomial(K(N)-1,j).
Thus <=2 steps have asymptotic density zero and <=3 steps cover at
most (1/3+o(1)) of positive integer lengths.

This script does not assume the sharp A006063 threshold or use any
matching solver. It cross-checks the exact one-seed recurrence and
enumerates root sequences of depth at most three at selected N.
"""
from math import comb
from reflection_tree_counts import reflection_counts


def floor_cuberoot(x):
    low, high = 0, 1
    while high**3 <= x:
        high *= 2
    while high-low > 1:
        mid = (low+high)//2
        if mid**3 <= x:
            low = mid
        else:
            high = mid
    return low


def depth_reachability(cap, max_depth=3):
    K = floor_cuberoot(2*cap)
    states = {(7, 1)}
    reach = {7}
    by_depth = [1]
    for depth in range(1, max_depth+1):
        next_states = set()
        for old_size, last_root in states:
            for k in range(last_root+1, K+1):
                size = k**3 - old_size - 1
                if old_size < size <= cap:
                    next_states.add((size,k))
        states = next_states
        reach.update(size for size,_ in states)
        by_depth.append(len(reach))
        upper = sum(comb(K-1, j) for j in range(depth+1))
        assert len(reach) <= upper, (cap,depth,len(reach),upper)
    return K, by_depth


def check_fibonacci_majorant():
    """Verify the sharper Fibonacci ceiling and predecessor root drops."""
    F=reflection_counts(12000)
    fib=[0,1,1]
    for _ in range(3,100):
        fib.append(fib[-1]+fib[-2])
    cubs=[k**3 for k in range(2,floor_cuberoot(24000)+1)]
    for n in range(7,len(F)):
        k=floor_cuberoot(2*n)
        majorant=1 if k==2 else fib[k-2]
        assert F[n]<=majorant,(n,F[n],majorant)
        for j in range(k-1):
            root=k-j
            if root<2:break
            m=root**3-n-1
            if 7<=m<n:
                assert floor_cuberoot(2*m)<=k-2*j-1,(n,m,j)
    print("PASS: all one-seed counts n<=12000 satisfy "
          "F(n)<=Fib(K(n)-2), and every reflection predecessor "
          "drops height by at least 2*j+1.")


def main():
    f = reflection_counts(12000)
    for n in range(7,len(f)):
        K=floor_cuberoot(2*n)
        assert f[n] <= 2**(K-1), (n,f[n],K)
    print("PASS: exact reflection counts satisfy root-subset upper bound "
          "at every length 7..12000.")

    expected = {
        10000: (27, [1,20,176,895]),
        100000: (58, [1,45,875,9630]),
        1000000: (125, [1,99,4229,98749]),
    }
    for cap,(K0,counts) in expected.items():
        K,actual=depth_reachability(cap)
        assert K==K0 and actual==counts, (cap,K,actual)
        bound=sum(comb(K-1,j) for j in range(4))
        print(f"PASS N={cap}, K={K}: depth <=3 reaches "
              f"{actual[-1]} lengths ({actual[-1]/cap:.5f} of range), "
              f"rigorous counting bound={bound}.")

    print("PASS: root-order encoding and depth-3 density barrier.")


if __name__=="__main__":
    main()
