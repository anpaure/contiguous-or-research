# Minimal-component portfolios in `k11_forest_sat.cpp`

## Status

The environment variable

```text
K11_FOREST_MIN_COMPONENT=e0c1
```

or

```text
K11_FOREST_MIN_COMPONENT=e1c2
```

enables one exact, independently proved component branch.  If the variable is
absent, no clause and no variable is added, so all pre-existing formulas are
unchanged.  The mode is rejected unless `K11_FOREST_RANK6_BRANCH` is respectively
`0` or `1`; that branch already requires the canonical-entry, boundary-entry,
band-cut, and joint-band-cut modules.

This is a completeness statement **within the named component branch**, not a
claim that either branch covers every possible optimum.

## Common notation

Let `P_i` be the selected rank-five interval in position `i` of the monotone
witness order and `Q_i` the analogous rank-six interval.  A state `(a,b)` at
row index `i` denotes the physical interval `[i+a,i+b]`.  The base formula
already enforces one state per row, monotonicity, the exact interval OR, exact
rank, and a permutation of every mask in each central layer.

For Boolean coordinate variables, the added three-clause encodings are exact:

```text
z <-> (x OR y):   (-x z), (-y z), (-z x y)
z <-> (x AND y):  (-z x), (-z y), (z -x -y).
```

## Mode `e1c2`

The component theorem says the sole literal rank-six witness is the isolated
component `Q_0=[0,0]`, while the other component is

```text
P_0,Q_1,P_1,Q_2,...,Q_461,P_461.
```

The existing branch symmetries make `mask(Q_0)=63`.  The implementation adds
the corresponding state and eleven coordinate units explicitly.

For `0<=i<=460`, the theorem gives

```text
Q_(i+1) = [ left(P_i), right(P_(i+1)) ].
```

Writing the three states as `(a,b)`, `(a',b')`, `(c,d)`, equality of physical
endpoints is exactly

```text
c=a-1, d=b'.
```

Because each row already chooses exactly one state, one implication from each
`P_i` state to all `Q_(i+1)` states with `c=a-1`, and one from each `P_(i+1)`
state to those with `d=b'`, is necessary and sufficient.  An empty support is
the correct unit prohibition.

The two rank-five intervals are distinct proper subsets of the rank-six
interval, so coordinatewise

```text
mask(Q_(i+1)) = mask(P_i) OR mask(P_(i+1)).
```

For `1<=i<=460`, the two distinct rank-six neighbors contain `P_i`; two
distinct six-sets containing the same five-set intersect in that five-set:

```text
mask(P_i) = mask(Q_i) AND mask(Q_(i+1)).
```

These are identities (5.4)--(5.8), not heuristic Johnson constraints.  They
contribute exactly 39,625 schedule clauses and no variables.

Deleting the boundary literal leaves a 464-position word with central slack
two.  Therefore every rank-at-most-four target has a witness of physical
length at most two.  The implementation adds `not Inside(p) OR not Inside(p+2)`
for direct and generic lower witnesses.  The same theorem leaves at most four
uncrossed rank-three and rank-four target names.  Existing six generic slots
are retained, but slots 4 and 5 are forced to select the same target names as
slots 0 and 1.  Their interval variables remain independent.  This is
complete: select the at most four genuine exceptions in the first four slots
and fill unused names by duplicating any already selected target/witness.

## Mode `e0c1`

There is no anchored literal entry, so reversing the whole array is a genuine
symmetry of this branch and of every optional prerequisite.  It exchanges the
endpoint colors.  We may therefore choose the left color as the perfect
matching.  The other matching is the unique order-preserving unit shift:

```text
Q_i=[left(P_i),right(P_(i+1))], 0<=i<=460,
Q_461 is a proper same-left extension of P_461.
```

For the first relation, state coordinates obey `c=a,d=b'+1`.  The final
relation obeys `c=a,d>b`.  As in `e1c2`, exact-one row states make the support
implications necessary and sufficient.  The mask identities are

```text
Q_i = P_i OR P_(i+1),             0<=i<=460,
P_i = Q_(i-1) AND Q_i,            1<=i<=461.
```

They contribute exactly 39,656 clauses and no variables.  No reversal is used
in `e1c2`, where reversing would move the anchored literal away from position
zero.

## Independent finite checker

`scratch/check_k11_mincomp_schedule.cpp` independently enumerates all 1,000
state triples.  It verifies that both encoded projection relations are exactly
the corresponding physical endpoint equalities, checks the final-extension
relation, and recomputes the two fixed schedule-clause counts.

```text
g++ -O3 -std=c++20 -Wall -Wextra -Wpedantic \
  scratch/check_k11_mincomp_schedule.cpp -o /tmp/check_k11_mincomp
/tmp/check_k11_mincomp
```

Expected output begins with `PASS` and includes
`e1_schedule_clauses=39625 e0_schedule_clauses=39656`.
