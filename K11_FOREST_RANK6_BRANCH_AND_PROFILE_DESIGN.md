# Exact k=11 rank-six branch anchor and strengthened profile design

## 1. Outcome

Assume the following already audited guards are active:

```text
K11_FOREST_CANONICAL_RANK6_ENTRY=1
K11_FOREST_RANK6_BOUNDARY_ENTRY=1
K11_FOREST_BAND_CUTS=1
K11_FOREST_JOINT_BAND_CUTS=1.
```

Let `e` be `JointBandCutPlan::e`, which is exactly the selected rank-six
singleton count `x0 in {0,1}`.

One additional 12-literal clause gives the exact anchored equivalence

```text
A[0]=63 <-> e.                                  (1.1)
```

Only the forward clause `A[0]=63 -> e` must be emitted.  The reverse
implication is already a consequence of the selected-singleton semantics and
the canonical/boundary hard clauses.

This produces an exact two-branch portfolio:

```text
branch 0: -e, equivalently no literal rank-six entry exists;
branch 1:  e, equivalently A[0]=63 is the sole literal rank-six entry.
```

The branches are disjoint and exhaustive up to the already-audited coordinate
and reversal symmetries.

The stronger audited profile inequality

```text
y2>=x1+82+14*e                                 (1.2)
```

has a compact exact implementation.  In the `e=0` branch it is already the
existing joint short-pool row.  In the `e=1` branch it becomes three
chain-specific comparisons costing exactly

```text
241 variables,
1659 clauses.
```

No solver source is edited by this design note.

## 2. The one-clause anchor

The canonical rank-six mask is

```text
C=63={0,1,2,3,4,5}.
```

Add the clause

```text
 e
 OR -A[0,0] OR -A[0,1] OR -A[0,2]
 OR -A[0,3] OR -A[0,4] OR -A[0,5]
 OR  A[0,6] OR  A[0,7] OR  A[0,8]
 OR  A[0,9] OR  A[0,10].                       (2.1)
```

The eleven array literals are precisely the mismatches from mask 63.  They
are all false exactly when `A[0]=63`, so (2.1) is

```text
A[0]=63 -> e.
```

Its exact inventory is

```text
variables: 0,
clauses: 1,
clause length: 12.
```

## 3. Why no reverse clause is needed

`JointBandCutPlan` has already proved `x0<=1` and defines `e` in both
directions as the OR of the only remaining width-zero rank-six schedule
states, `00` and `33`.  Therefore `e=1` means that the selected rank-six row
contains a singleton witness `[p,p]`.

The central interval encoding makes its exact-rank-six value equal to the
physical array entry `A[p]`.  Under the canonical-plus-boundary interaction,
every noncanonical rank-six value is forbidden globally and mask 63 is
forbidden at positions `1,...,464`.  Hence

```text
e -> p=0 and A[0]=63.                            (3.1)
```

Thus (3.1) supplies the reverse implication of (1.1) without any new clause.

The forward direction is not a logical consequence of an arbitrary auxiliary
witness choice: an array containing `A[0]=63` could initially select a longer
witness for target 63.  It is nevertheless satisfiability-preserving WLOG.
Reselect `[0,0]` as target 63's witness and select all other central witnesses
arbitrarily.  No other selected rank-six interval can contain position zero,
because an equal-rank OR containing the 6-set 63 would itself have to equal
63, whose selected witness is already fixed.  Sorting the reselected family
therefore gives a valid monotone band with `e=1`.

All enabled band, joint-band, adjacent-shadow, rank-three-shadow, and endpoint
alignment restrictions are universally valid for independently selected
central witness families; their existential auxiliary choices can be rebuilt
after reselection.  Hence clause (2.1) preserves existence.

If no rank-six literal exists, no selected rank-six singleton can exist
either, so every witness encoding automatically has `e=0` and (2.1) is
vacuous.

## 4. Exact two-branch portfolio

Let `F` be the currently guarded formula plus anchor clause (2.1).  Run the
two cases

```text
F0 = F AND -e,
F1 = F AND  e.
```

By (1.1):

* every model of `F0` has no literal rank-six array entry;
* every model of `F1` has exactly one such entry, namely `A[0]=63`.

The cases cannot overlap and

```text
F = F0 OR F1
```

at the level of satisfiability.  Conversely, every original solution can be
put in one of these branches:

1. the array-level theorem permits at most one distinct rank-six mask and at
   most one literal occurrence overall;
2. coordinate symmetry relabels its mask as 63;
3. reversal moves the occurrence, if present, to position zero; and
4. witness reselection makes `e=1`; when no occurrence exists, `e=0`.

Each branch adds one unit clause.  Relative to the existing guarded formula,
the common anchored base costs one clause and zero variables; each portfolio
member then costs one further clause.

For proof production, two independent UNSAT-under-unit logs are an exhaustive
mathematical case split, but they are not automatically one DRAT/LRAT proof of
`F`.  A final certificate must either use a checked case-split wrapper, derive
the opposite unit from each assumption proof and combine them, or rerun the
unbranched anchored formula proof-producing.  Search completeness does not
depend on this certificate packaging detail.

## 5. Boundary identities for the stronger profile row

Use the production plan's one-based shorthand

```text
g_j = rank_six_plan.boundary[j-1],
h_j = joint_plan.boundary[j-1].
```

The rank-six chain is

```text
00,01,02,03,13,23,33.
```

Therefore

```text
x0 = g1 + 462-g6 = e,
x1 = (g2-g1)+(g6-g5),
x0+x1 = g2+462-g5,
x1 = g2+462-g5-e.                               (5.1)
```

Substituting (5.1) into (1.2) gives the common exact form

```text
g2+544+13*e <= y2+g5.                           (5.2)
```

For `e=0`, this is exactly the already encoded joint-pool inequality
`y2>=x0+x1+82`.  No new arithmetic is needed in branch zero.

For `e=1`, equation (5.2) is

```text
g2+557 <= y2+g5.                                (5.3)
```

## 6. The three exact rank-five transformations

The selected rank-five schedule lies on exactly one of the following chains.
The `h_j` values count the slots through the first `j` states.

### Chain A

```text
00,01,02,12,13,23,33.
```

Its width-two count is

```text
y2=(h3-h2)+(h5-h4).
```

Equation (5.3) becomes

```text
g2+557+h2+h4 <= h3+h5+g5.                       (6.1)
```

### Chain B

```text
00,01,02,12,22,23,33.
```

Here

```text
y2=h3-h2,
```

so

```text
g2+557+h2 <= h3+g5.                             (6.2)
```

### Chain C

```text
00,01,11,12,13,23,33.
```

Here

```text
y2=h5-h4,
```

so

```text
g2+557+h4 <= h5+g5.                             (6.3)
```

Each row is active only for its corresponding chain and for `e=1`.

## 7. Implementation-safe guard choices

There are two equivalent implementation modes.

### Branch-specialized mode — recommended for the portfolio

In the `e=1` binary, the unit clause `e` is already present.  Reuse the
existing `add_leq_guarded` method with only the corresponding chain selector
as guard.  Emit (6.1)--(6.3).  In the `e=0` binary, emit none of these rows;
the prior joint-pool circuit already implies the desired specialization.

### One-formula mode

Add an `add_leq_double_guarded(x,y,e,chain)` helper.  It is identical to
`add_leq_guarded`, except that **every** order clause and every prefix-equality
definition clause is prefixed by both

```text
-e, -chain.
```

The arithmetic adders may remain unguarded: they define fresh output bits
exactly and are extendable for every input.  Guarding only the final order
circuit is safe, provided all its auxiliary prefix-equality clauses receive
both guards.  No conjunction variable is needed.

The double guard changes literal counts but not variable or clause counts.
It permits one common CNF, while branch-specialized generation avoids carrying
the inactive arithmetic through the `e=0` search.

For a clean isolated circuit, do not guard only the leading comparison clauses
while leaving the prefix-equality definitions singly guarded.  Those exact
definitions are existentially extendable and so would not by themselves
restrict the boundary inputs, but keeping them active obscures the intended
inactive-branch semantics and complicates clause audits.  Do not activate the
actual constant-557 order rows in the `e=0` branch.

## 8. Exact circuit inventory

The existing `add_unsigned` implementation, for operand width `w`, creates

```text
2*w variables,
14*w clauses
```

and returns width `w+1`.  A guarded unsigned comparison at final width `w`
creates

```text
w-1 prefix-equality variables,
w+5*(w-1)=6*w-5 clauses.
```

Constant 557 has ten bits and is represented with signed literals of the
existing constant-one variable, so it allocates nothing.

Term order matters because each ripple addition widens the accumulator.  Use
the following variable-minimizing orders:

```text
A left:  sum_all({g2,h2,h4,c557})   widths 9,9,9,10
A right: sum_all({h3,h5,g5})        widths 9,9,9

B left:  sum_all({g2,h2,c557})      widths 9,9,10
B right: sum_all({h3,g5})           widths 9,9

C left:  sum_all({g2,h4,c557})      widths 9,9,10
C right: sum_all({h5,g5})           widths 9,9.
```

The exact costs are:

| row | adder variables | comparator variables | total variables | adder clauses | comparator clauses | total clauses |
|---|---:|---:|---:|---:|---:|---:|
| A | 98 | 11 | 109 | 686 | 67 | 753 |
| B | 56 | 10 | 66  | 392 | 61 | 453 |
| C | 56 | 10 | 66  | 392 | 61 | 453 |
| total | 210 | 31 | **241** | 1,470 | 189 | **1,659** |

Thus:

```text
anchor only:                    0 variables,    1 clause;
profile circuit:              241 variables, 1659 clauses;
anchor + profile common CNF:  241 variables, 1660 clauses;
either branched common CNF:   241 variables, 1661 clauses after its unit.
```

With branch-specialized generation, the lean inventories are instead:

```text
e=0 branch: anchor + unit                 = 0 variables, 2 clauses;
e=1 branch: anchor + unit + profile rows  = 241 variables, 1661 clauses.
```

The anchor is redundant after the `e=1` unit but should remain in a common
base for exact branch semantics.

## 9. Independent checker

The independent design checker is

```text
scratch/verify_k11_rank6_branch_profile_design.cpp.
```

It:

1. exhausts small monotone boundary tuples for all three chains and verifies
   the common and transformed inequalities against the direct `x1,y2`
   definitions;
2. checks the exact real equality on the explicit surviving singleton
   profile `x=(1,0,366,95), y=(0,366,96)`;
3. independently derives every ripple-adder and comparator inventory using
   the production circuit rules; and
4. asserts the one-clause anchor inventory.

It compiles cleanly with

```text
g++ -O3 -std=c++20 -Wall -Wextra -pedantic \
    scratch/verify_k11_rank6_branch_profile_design.cpp \
    -o verify_k11_rank6_branch_profile_design
```

and prints

```text
branch_profile_algebra=PASS
chain_A_variables=109 clauses=753
chain_B_variables=66 clauses=453
chain_C_variables=66 clauses=453
profile_total_variables=241 clauses=1659
anchor_variables=0 clauses=1 length=12
```

## 10. Recommendation

Add the 12-literal anchor behind a guard requiring canonical, boundary, band,
and joint plans.  Launch two exact portfolio branches with units `-e` and
`e`.  Generate the 1,659-clause profile circuit only in the `e=1` branch, or
use a correctly double-guarded common circuit if maintaining one binary is
operationally preferable.

This branch is mathematical, not heuristic: after the anchor, the two cases
partition all satisfying arrays exactly.
