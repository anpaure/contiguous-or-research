# What equality at K16 forces, and why the deadline bound cannot prove `+1`

**Date:** 2026-07-31  
**Status:** architecture-free equality audit; no new lower bound claimed

## 1. Numerical discontinuity in the scalar bound

At `k=16`,

```text
r = 8,
W = C(16,8) = 12870,
Lambda = sum_(s=1)^7 C(16,s) = 26332.
```

For excess `e=2`, the deadline capacity is

```text
2W + C(3,2) = 25743,
```

which misses `Lambda` by `589`.  For `e=3`, it jumps to

```text
3W + C(4,2) = 38616,
```

which exceeds `Lambda` by `12284`.  Thus `d(16)=3`, but equality is very far
from equality in the cell-count inequality.  The scalar proof has no
near-tightness from which to derive a fourth unit.

## 2. First-delivery profile forced at length 12873

Assume a universal word of length `L=W+3=12873` exists.  Let `S,J,F,G` be
its first-middle stalls, jumps, same-deadline flats and different-deadline
ghosts.  The exact inventory gives

```text
S + J + F + G = 3.
```

The refined lower-cell inequality excludes a ghost:

```text
Lambda <= (3-G)(L+G),
```

whose right side is at most `25748` when `G>=1`.  Therefore

```text
G = 0,
S+J = 0,1,2,3,
F   = 3,2,1,0,
```

and the same ghost-free statement holds after reversing the word.  No one of
the four surviving profiles is excluded.  The terminal-waste lemma consumes
one unit in each orientation, but the two orientations cannot be added.

Every lower target has a witness of one, two or three letters, and every
rank-eight target has a first-delivery witness of at most four letters.
Choosing the latest left endpoint in the unique deadline group of every
rank-eight target gives `W` endpoint-essential intervals

```text
I_i=[p_i,q_i],  0 <= q_i-p_i <= 3,
```

with strictly increasing left and right endpoints and with all rank-eight
labels appearing exactly once.  Exactly three left positions `X` and three
deadlines `Y` are unused.  They satisfy

```text
|Y intersect [0,t]| >= |X intersect [0,t]|,
sum_i(q_i-p_i) = sum X - sum Y.
```

If `U_X` is the lower depth in the three unselected columns and `R_<` is the
lower repeat excess, then

```text
26332 + R_< = sum X - sum Y + U_X,
0 <= U_X <= 9.
```

Hence the three endpoint-defect pairs must have total separation at least
`26323`; in particular their height path is positive on at least `8775`
positions.  Equality cannot be repaired by a bounded local seam.

## 3. Compulsory physical lower-row counts

Let `f_p<=3` be the number of initial lower cells in column `p`, and put

```text
n_a = number of columns with f_p >= a,  a=1,2,3.
```

Then

```text
n_1+n_2+n_3 = 26332 + R_<.
```

A nested column contains at most one distinct rank-seven target and at most
two distinct targets from ranks six and seven.  Boundary lengths also give
`n_1<=L` and `n_2<=L-1`.  Consequently every equality word must satisfy

```text
n_1       >= 11440,
n_1+n_2   >= 19448,
n_2       >=  6575,
n_3       >=   587 + R_<.
```

Only three columns are absent from the selected middle core, so at least

```text
584 + R_<
```

selected middle intervals have full span three.  This improves the previous
`583` selected-core floor by using the missing final length-two row.  It is
still nowhere near a contradiction.

Every singleton target `{x}` forces an actual singleton letter `{x}`;
therefore all sixteen singleton letters occur.  No analogous parity follows
for larger lower ranks, because they may be direct letters or unions of two
or three proper submasks.

## 4. The remaining overlap and matching conditions

For selected middle labels `T_i`, define

```text
K_j = intersection of all T_i whose I_i contains j.
```

Physical realizability forces `K_j` nonempty and

```text
union_(j in I_i) K_j = T_i.
```

Conversely the maximal letters `A_j=K_j` realize the declared middle
intervals, but do not automatically cover the lower or upper layers.  Lower
universality additionally requires all `26332` masks to occur among the
length-one, -two and -three ORs.

Rank-seven coverage alone already forces at least `11434` distinct targets
to be intersections of consecutive rank-eight labels, so almost all of the
middle order is a rainbow Johnson path.  The remaining `1435` transitions
are not controlled by this count, and the analogous rank-six coupling is not
settled by a scalar moment.

There is no parity obstruction in the present ledger.  If
`N=S+J` and `F=3-N`, the middle duplicate-incidence vector only has to be a
nonnegative integral vector of total

```text
8F = 24,16,8,0.
```

The defect area and lower-repeat identity likewise permit either parity.

## 5. Exact reason the existing lower bound is blind

Two countermodels make the boundary rigorous.

First, the frozen independent-column construction has lower-depth histogram

```text
depth 3: 6884 columns
depth 2: 1124 columns
depth 1: 3432 columns
depth 0: 1430 columns.
```

Containment matchings cover every one of the `26332` lower targets exactly
once and place them under all `12870` middle targets.  Both a three-stall and
a three-flat deadline closure exist.  Thus no argument using only row
capacities, monotone deadlines, rank counts and within-column containment can
prove `L>=12874`.

Second, there is a physical countermodel much closer to the real question:

```text
scratch/k16_upper12874_best_delete.word
SHA a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

It has length `12873` and covers every nonempty mask except the rank-eight
mask `0x2c6d`.  In particular it covers all lower targets in lengths at most
three, every upper target, all sixteen singleton coordinates as literal
letters, and the exact common-envelope equations.

Its first-delivery inventory is

```text
(S,J,F,G,H)=(0,0,3,1,1).
```

There are exactly `W=12870` distinct deadline groups.  Selecting the latest
left endpoint in each group gives a genuine physical three-hole staircase:

```text
left holes      X = [6432,12869,12871],
deadline holes  Y = [0,2,3],
span histogram    = 0^1 1^2 2^6436 3^6431.
```

The group labels contain `0xc279` twice and omit `0x2c6d`.  A hypothetical
universal equality word needs the same number of deadline groups with every
rank-eight label once.  Deadline geometry sees no difference between

```text
one repeated label + one missing label
```

and

```text
the missing label replacing the repeat.
```

This is exactly the observed one-hole wrinkle.  It is not visible to the
general lower bound because that proof forgets the labels after counting
distinct deadlines.

## 6. Honest frontier

No architecture-free `+1` obstruction was found.  Any proof that
`nu(16)=12874` must use a genuinely cross-column statement coupling:

1. injectivity of all `12870` rank-eight deadline-group labels;
2. the common-envelope overlap equations of adjacent columns;
3. full lower length-three universality; and
4. preservation of all upper witnesses.

Equivalently, it must prove that the physical duplicate `0xc279` cannot be
exchanged for `0x2c6d` without destroying another required mask.  The many
negative local searches establish this only around particular words or
fibres, not for arbitrary length-`12873` words.

Machine replay:

```text
scratch/audit_k16_equality_lowerbound_blindspot_20260731.py
scratch/k16_equality_lowerbound_blindspot_20260731.audit.json
```
