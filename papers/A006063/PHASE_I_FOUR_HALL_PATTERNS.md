# Phase I: a four-pattern near-bipartite Hall reduction

**Mixed status:** The 14-edge near-bipartiteness theorem
and the exceptional-edge charge equation are PROVED.
The existence of bipartite perfect matchings in the
four selected families below has been **verified for
all 94 lengths by an independent finite augmenting
algorithm** but is **not yet proved by a uniform
noncomputational Hall theorem**.

The range is `467<=n<=560`, with palette
`{216,343,512,729}`. Odd n has its valid fixed
point 108 deleted. All statements refer to the
fixed 14-edge deletion set D in
[SMALL_BIPARTITE_CORE.md](SMALL_BIPARTITE_CORE.md).
The residual graph `B_n=G_n-D` is bipartite.
Choose the canonical 2-coloring of the largest
bipartite graph with `chi(1)=+1`,
restricted to all n and with 108 deleted at odd n.

## 1. The complete correction dictionary

Write `Delta(n)=sum_(i in V_n) chi(i)`, with
`V_n=[1,n]` for even n and
`V_n=[1,n]\\{108}` for odd n.
The exact finite coloring arithmetic gives

```
Delta=4 at 32 lengths,
Delta=2 at 54 lengths,
Delta=0 at 8 lengths,
no other imbalance occurs.
```

All the exceptional edges below join two
**positive-color** vertices in B_n.

Define the following `Q(n) subset D`:

| condition | select these exceptional edges Q(n) |
|---|---|
| Delta(n)=4 | (70,146) and (84,132) |
| Delta(n)=2 and n!=559 | (84,132) |
| Delta(n)=2 and n=559 | (101,115) |
| Delta(n)=0 | empty |

The selected edges have no common endpoints
(since D itself is a matching), and satisfy
the exact charge equation

```
2 * sum_(e in Q(n)) chi(endpoint_of_e)
    = Delta(n).
```

Consequently the bipartite graph

```
B'_n = B_n - endpoints(Q(n))
```

has **equal-sized color classes** for every
one of the 94 lengths.

This equality is purely elementary integer
arithmetic from the shared maximal coloring.
It is **not a perfect-matching theorem**.

## 2. The sharper open Hall target

**Experimental finding (94/94 successful).** A
separate standard-library implementation
of bipartite augmenting paths finds
a perfect matching of `B'_n` for
all `467<=n<=560`. Adding the
edges of Q(n) and, for odd n, the
fixed point 108 gives a valid
four-cube involution.

This is stronger than the previous
"some four-color matching exists"
experiment: it specifies **at most
four fixed exceptional-edge patterns**
for all 94 lengths. In fact exactly
**three nonempty edge selections**
suffice, with the empty selection as
the fourth pattern.

**Conditional theorem (precise missing premise).**
If these four families of balanced
bipartite graphs `B'_n` satisfy Hall's
condition, then every `n in [467,560]`
admits a four-cube involution with
fixed point 108 precisely when n is
odd. This follows immediately by
combining Hall's theorem with the
disjoint exceptional edges Q(n).

There is no claim here that the
94 Hall inequalities have been
proved without finite computation.

The fact that a *single* two-edge
correction `{(70,146),(84,132)}`
works experimentally for **all 32
Delta=4 lengths**, and a *single*
one-edge correction `{(84,132)}`
works for **53 of the 54 Delta=2
lengths** (only n=559 uses
`{(101,115)}`), makes this a
well-defined target for an actual
one-parameter bipartite matching theorem.

## 3. Limitations

The same charge argument alone is
**not sufficient** to prove Phases
II and III. There are instances
where choosing the minimum number
of exceptional edges to balance the
two color classes still leaves a
bipartite Hall obstruction.

The purpose of this note is to
make the combinatorial target
smaller and more explicit:
instead of 94 general nonbipartite
matching searches, prove a single
family of **balanced bipartite Hall
conditions indexed by n** with a
four-line exceptional-edge selector.

[verify_phase_i_hall_patterns.py](verify_phase_i_hall_patterns.py)
is an optional **finite computational
audit**, not a replacement for the
unproved uniform Hall assertion.
