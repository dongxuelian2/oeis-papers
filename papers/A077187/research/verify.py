#!/usr/bin/env python3
from sympy import primerange
from defect_transfer import transfer_state
from independent_digit_layers import state_at_e,mountain_window
count=0
for p in primerange(7,350):
    (C,Y),early,(r,u,v,T,E)=transfer_state(p)
    X=(81*C+10)%p;Z=(81*Y+1)%p
    if p*T<=150000 or p==233:
        assert (C,Y)==state_at_e(p,p*T,r),(p,'state')
        count+=1
        for j in sorted({0,1,2,min(r-1,11),r-1}):
            z=pow(10,j,p)
            assert mountain_window(p,p*T,C,Y,j)==(10*X*z*z-20*z+Z)*pow(81*z,-1,p)%p,(p,j)
    if 20%u==0:
        j=(9*pow(10,T,r)-10)%r;z=pow(10,j,p)
        assert (10*X*z*z-20*z+Z)%p==0,(p,'u-divides-20')
    if p==113:
        assert (r,u,v,T,E,C,Y,X,Z)==(112,16,7,336,5,86,0,83,1)
        assert mountain_window(p,p*T,C,Y,32)==0
    if p==233:
        assert (r,u,v,T,E,X,Z)==(232,8,29,1624,4,119,174)
        assert mountain_window(p,p*T,C,Y,33)==0
    if p==313:
        assert not any((10*X*pow(10,j,p)**2-20*pow(10,j,p)+Z)%p==0 for j in range(r))
print("PASS forward-layer vs inverse-transfer on",count,"primes; square/witness tests and negative control")
