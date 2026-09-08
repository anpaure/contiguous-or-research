# An exact even-to-odd common-colour Pascal lift

Date: 2026-07-29

Status: exact conditional construction and complete finite audit on the saved
`k=14` carrier family.  No `k=15` word is claimed.

## 1. The construction

Let `k=2r`, let

```text
T_0,T_1,...,T_{W-1},       W=C(2r,r),
```

be a Hamilton path in `J(2r,r)`, and colour transition `i` by

```text
X_i=T_i intersection T_{i+1},
U_i=T_i union T_{i+1}.
```

Both colour layers have cardinality

```text
N=C(2r,r-1)=C(2r,r+1).
```

Form the bipartite occurrence multigraph `H_T` with one edge
`X_i--U_i` for every transition.  Suppose `H_T` has a matching of size `N`
which saturates both colour layers.  Equivalently, there is a set `K` of
`N` transition indices on which the lower colours and upper colours are both
rainbows.

Deleting the other transitions cuts `T` into

```text
W-N=Cat(r)
```

vertex paths.  For a component `T_a,...,T_b`, introduce a new coordinate
`z` and define

```text
zT_a,zT_{a+1},...,zT_b,U_{b-1},U_{b-2},...,U_a.       (1.1)
```

If `a<b`, (1.1) is a Johnson cycle on rank `r+1` of `[2r+1]`.

### Theorem 1.1

If no deleted-transition component is a singleton, the cycles (1.1)

1. enumerate every rank-`r+1` subset of `[2r+1]` exactly once; and
2. their consecutive intersections enumerate every rank-`r` subset exactly
   once.

#### Proof

The `z`-sector contains `z+T` and therefore gives all middle sets containing
`z`.  The other sector consists of `U_i`, `i in K`; common-rainbow
surjectivity gives every rank-`r+1` set not containing `z` exactly once.

Inside the `z`-sector, consecutive intersections are `z+X_i`, `i in K`,
and therefore give every rank-`r` set containing `z` once.  At the two cross
edges of a component the intersections are `T_a,T_b`.  Consecutive reversed
`U` vertices intersect in the intervening `T_i`; distinctness of the selected
`U_i` makes the intersection have rank exactly `r`.  Hence every `T_i` in
the component appears exactly once as a no-`z` lower colour.  Summing over
components proves the assertion.  QED.

The run of the new coordinate in (1.1) has length `b-a+1`.  Thus a minimum
component length `d+1` supplies the new-coordinate part of depth-`d`
residence.  Residence of the old coordinates and all deeper shadows remain
separate gates.

## 2. Exact matching reformulation

The common-rainbow condition is just a bipartite perfect matching in `H_T`.
It is therefore decidable in polynomial time, with no SAT and no heuristic.
The solver-free implementation is

```text
scratch/audit_even_to_odd_common_colour_lift.py.
```

This is the path-ordered version of the central-diamond/SCD construction:
each matched pair `X subset U`, `|U-X|=2`, owns the Johnson edge between the
two intermediate rank-`r` sets.

## 3. The actual k=14 data

For the verified optimal carrier

```text
scratch/k14_intersection_sixpiece_hallpass_004a.json
```

both transition-colour families already cover all 3,003 targets, but the
maximum common rainbow has size only

```text
2,578 / 3,003.
```

Thus the obvious reverse lift of that certificate is impossible by an exact
deficiency of 425.

An exhaustive solver-free census of all 135 distinct saved `k=14` Johnson
paths with complete middle deck found a best common rainbow of

```text
2,739 / 3,003,
```

attained by `scratch/k14_central_2opt_descent.certificate.json`.  The
remaining exact deficiency is 264.  No saved carrier satisfies Theorem 1.1.

Starting from those saved paths, the exact dynamic C++ neighborhood

```text
scratch/search_k14_common_colour_2opt.cpp
```

preserves the complete middle deck and both q1 supports while recomputing the
affected bipartite matching components exactly.  Steepest 2-opt followed by
steepest connected 3-opt improves the best matching to

```text
2,918 / 3,003,
```

so the current constructive deficiency in this lane is 85.  The result was
independently recomputed from
`scratch/k14_common_colour_3opt_best_20260729.json`; its audit is
`scratch/k14_common_colour_3opt_best_20260729.audit.json`.  It is a strict
local optimum for both implemented neighborhoods, not a global lower bound.
The matching objective does not preserve residence: this best path has 228
old-coordinate runs of length below three (82 of length one and 146 of
length two).  Consequently it is not itself a decorated lift seed.  Any
successful continuation must optimize the common rainbow jointly with run
constraints, rather than treating the remaining 85 as the only gate.

This explains why merely possessing a perfect lower shadow and a perfect
upper shadow at `k=14` does not automatically lift to `k=15`: the two
rainbows must use the **same transition occurrences**.  It also gives a
small, exact new search objective—raise the common matching from 2,918 to
3,003—whose success would produce an exact middle/q1 `k=15` cycle factor
before the residence, deeper-shadow, and compiler gates are checked.
