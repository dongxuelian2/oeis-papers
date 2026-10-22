"""Independently compute decimal full-digit-layer states, no group-ring code."""
from exact_b8_fast import coefficients,D
from scalar_reference import polyforms
def order_is_exact(p,r):
    assert pow(10,r,p)==1
    for q in (2,3,5):
        if r%q==0:assert pow(10,r//q,p)!=1
def layer_states(p,r):
    C=Y=0;ten_power=1;initial=None
    for e in range(1,2*r+1):
        L=ten_power;ten_power=ten_power*10%p
        q=ten_power;N=9*L%p
        alpha=pow(q,9*pow(10,e-1,r)%r,p)
        if q==1:
            sum0=N;sum1=N*(N-1)*pow(2,-1,p)%p
        else:
            iv=pow(q-1,-1,p)
            sum0=(alpha-1)*iv%p
            sum1=(q-N*alpha+(N-1)*q*alpha)*iv*iv%p
        A=(L*sum0+sum1)%p
        B=((q-1)*sum0-sum1)%p
        C=(alpha*C+B)%p
        Y=(Y+A)*pow(alpha,-1,p)%p
        if e==r:initial=(C,Y)
    return initial,(C,Y)
if __name__=='__main__':
    for p,r in ((52489,26244),(328051,328050),(839809,52488)):
        order_is_exact(p,r)
        s=r//6561;g=pow(s,-1,729);m=r//729;z=pow(10,m,p)
        UU,VV=coefficients(g)
        def ev(a):return sum(c*pow(z,i,p) for i,c in enumerate(a))%p
        predicted=tuple(sum(ev(f)*pow(m,i,p) for i,f in enumerate(parts))*pow(D,-1,p)%p for parts in (UU,VV))
        state1,state2=layer_states(p,r)
        measured=tuple((state2[i]-state1[i])%p for i in range(2))
        assert predicted==measured and measured!=(0,0)
        print('PASS prime',p,'order',r,'phase',g,'drift',measured)
