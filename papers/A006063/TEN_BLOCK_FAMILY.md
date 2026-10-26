# A ten-block nested degeneration for three high-end lengths

This sixth symbolic family covers **345, 357, 351** with one
ten-block rearrangement, without separately using their 5-, 6-,
and 10-segment numeric endpoint certificates.

Let `alpha,beta` be binary parameters satisfying `beta<=alpha`.
Define the ten nonnegative input-block lengths

```
(7,
 12*alpha,
 159-24*alpha-99*beta,
 14*beta,
 28*beta,
 63*beta,
 10+24*alpha-6*beta,
 8*beta,
 159-24*alpha-107*beta,
 10+24*alpha+93*beta)
```

and arrange their output blocks in the order

```
(1,2,8,5,6,9,4,10,3,7).
```

All zero-length blocks are removed from both orders.
As usual `C_j=1+A_j+B_j+ell_j` is the reflected sum
on block `j`. Direct expansion gives the ten nominal sums:

```
(8, 8+19*alpha, 343,
 167-12*alpha+61*beta,
 167-12*alpha-30*beta,
 167-12*alpha+61*beta,
 512, 177+12*alpha+27*beta,
 343, 512).
```

For the only allowed pairs `(alpha,beta)=(0,0),(1,0),(1,1)`,
every nonempty block has a cube sum:

- Blocks 1,3,7,9,10 are always present and their sums are
  `8,343,512,343,512`.
- Block 2 is present only at `alpha=1`, giving sum `27`.
- Blocks 4,5,6,8 are present only at `beta=1` (hence
  `alpha=1`), giving `216,125,216,216`.

The permutation length is

```
n = 345 + 12*alpha - 6*beta.
```

Consequently:

| alpha | beta | n | nonempty blocks |
|---:|---:|---:|---:|
| 0 | 0 | 345 | 5 |
| 1 | 0 | 357 | 6 |
| 1 | 1 | 351 | 10 |

This is a straightforward symbolic block-rearrangement proof;
no matching algorithm or case-specific boundary multiset test
is a logical premise.

Combined with the previous five algebraic families, this
makes **25 parametrically generated seed lengths**, leaving
**57 exceptional finite integer identities** from the former 82
independent seed lengths. The new exceptional atlas therefore
contains **795** reflected blocks and the expanded full atlas
still contains **1,009** blocks.

The complete proof still relies on those 57 numerical
identities, so this note does not claim a uniform, case-free
construction. It is an additional structural compression of
the finite certificate.
