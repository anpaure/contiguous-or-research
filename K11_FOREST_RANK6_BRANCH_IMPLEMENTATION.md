# Implementation of the exact k=11 rank-six portfolio branch

## 1. Verdict

**PASS.**  The audited branch anchor and branch-one profile circuit were added
to `k11_forest_sat.cpp` behind

```text
K11_FOREST_RANK6_BRANCH=0
```

or

```text
K11_FOREST_RANK6_BRANCH=1.
```

The variable must be absent or have exactly one of those two string values.
The edit started from source SHA-256

```text
1172c55d5ab21f829af8263cb5cc13e65dec0179c5a50159ed3c1b064ba21c81
```

and produced

```text
c1eff19c73fa6610bd603194a43c89ffb5a54092cb35947fda64c6ed61876f0b.
```

Both branches add the one exact anchor clause and one unit clause.  Branch zero
allocates no profile circuit.  Branch one allocates exactly 241 variables and
emits exactly 1,659 profile clauses.

No live search was started.

## 2. Guard validation

When `K11_FOREST_RANK6_BRANCH` is present, all four audited prerequisite
guards must be active:

```text
K11_FOREST_CANONICAL_RANK6_ENTRY=1
K11_FOREST_RANK6_BOUNDARY_ENTRY=1
K11_FOREST_BAND_CUTS=1
K11_FOREST_JOINT_BAND_CUTS=1.
```

An absent variable leaves the feature disabled.  The strings `0` and `1` are
accepted.  Empty strings, `00`, `2`, and all other values are rejected.  An
invalid value exits with status 2 and prints

```text
K11_FOREST_RANK6_BRANCH must be absent or exactly 0 or 1
```

Missing prerequisite guards also exit with status 2 and print their complete
list.

## 3. Exact anchor and units

Let `e=JointBandCutPlan::e`.  The implementation emits

```text
e OR (A[0]!=63),
```

expanded as one 12-literal clause with the audited mismatch polarity.  The
canonical and oriented-boundary clauses already imply `e -> A[0]=63`, so the
new clause gives the anchored equivalence

```text
e iff A[0]=63.
```

It then emits exactly one unit:

```text
branch 0: -e,
branch 1:  e.
```

Thus branch zero contains no literal rank-six array entry and branch one has
the sole such entry `A[0]=63`.  The common costs are

```text
anchor: 0 variables, 1 clause of length 12,
unit:   0 variables, 1 unit clause.
```

Both clauses are added only after all plan clauses have been transferred to
the solver.

## 4. Branch-one profile plan

`RankSixBranchProfilePlan` is allocated before `variable_total` is frozen,
but only when the selected branch equals one.  It reuses:

```text
BandCutPlan::bits,
JointBandCutPlan::bits,
JointBandCutPlan::chain_selector,
JointBandCutPlan::one.
```

No boundary counter, chain selector, or constant-one variable is duplicated.

Under the branch unit `e=1`, the audited profile inequality is

```text
g2+557<=y2+g5.
```

The three selected-chain forms emitted by the plan are exactly

```text
A: g2+557+h2+h4 <= h3+h5+g5,
B: g2+557+h2    <= h3+g5,
C: g2+557+h4    <= h5+g5.
```

Each comparison is guarded only by its corresponding exact-one chain
selector; the branch unit already supplies `e=1`.  Term order puts all
nine-bit boundaries before the ten-bit constant 557, attaining the audited
minimum inventory:

| chain | variables | clauses |
|---|---:|---:|
| A | 109 | 753 |
| B | 66 | 453 |
| C | 66 | 453 |
| total | **241** | **1,659** |

Branch zero does not construct `RankSixBranchProfilePlan`, so it allocates
and emits exactly zero profile variables and clauses.  Its specialization of
the strengthened inequality is already implied by the existing joint-pool
row.

## 5. Diagnostics

The build summary prints

```text
rank6_branch=none|0|1
rank6_branch_anchor_clauses=0|1
rank6_branch_unit_clauses=0|1
```

and, only in branch one,

```text
rank6_branch_profile_variables=241
rank6_branch_profile_clauses=1659.
```

The anchor and unit counters are incremented at their actual solver-addition
sites.  The profile diagnostics come directly from the allocated plan.

## 6. Guard-off identity

With `K11_FOREST_RANK6_BRANCH` absent and all optional guards off, the edited
source reports exactly the frozen pre-edit inventory

```text
variables=4892622 clauses=15524818
rank6_branch=none
rank6_branch_anchor_clauses=0
rank6_branch_unit_clauses=0.
```

No branch-plan variables are allocated.

## 7. Exact branch inventories

With only the four required structural guards plus branch zero:

```text
variables=4899664 clauses=15777976
anchor clauses=1 unit clauses=1
profile variables/clauses=0/0.
```

With the same prerequisites plus branch one:

```text
variables=4899905 clauses=15779635
anchor clauses=1 unit clauses=1
profile variables/clauses=241/1659.
```

Thus branch one differs from branch zero by exactly the audited profile-plan
inventory.

With every existing optional structural guard, the canonical and boundary
gates, and the singleton-pool cut, the frozen exact portfolio inventories are:

```text
branch 0:
  variables=2924697
  clauses=14732380

branch 1:
  variables=2924938
  clauses=14734039.
```

The corresponding fully guarded unbranched inventory was

```text
variables=2924697 clauses=14732378,
```

so branch zero adds exactly the anchor and unit, while branch one additionally
adds 241 variables and 1,659 clauses.

## 8. Independent checkers

The implementation-specific checker is

```text
scratch/verify_k11_rank6_branch_implementation.cpp
SHA-256 55ff98228a78fee35ff65175afd757e115a16d226eaf9748b2c2a68ccea3565c.
```

It independently:

1. exhausts all 2,048 possible values of `A[0]` and both values of `e`,
   verifying the anchor polarity and exact equivalence under the already-hard
   reverse implication;
2. verifies that the two units partition the anchored models;
3. recomputes the exact ripple-adder and comparator inventories; and
4. checks the branch-one transformed integer inequality over every pair of
   feasible rank-six boundary values.

It prints

```text
anchor_equivalence=PASS
branch_partition=PASS
branch0_profile_variables=0 clauses=0
branch1_profile_variables=241 clauses=1659
anchor_variables=0 clauses=1 unit_clauses=1
```

The earlier algebra checker

```text
scratch/verify_k11_rank6_branch_profile_design.cpp
```

independently exhausts the three rank-five chain transformations and reports
the same per-chain costs.

Both compile cleanly with `-O3 -std=c++20 -Wall -Wextra -pedantic`.

## 9. Production compilation

The frozen source compiles cleanly against the real remote CaDiCaL library,
without generating a formula or starting a search.  The production executable
has SHA-256

```text
39c0e58fafd844fe25af1ef5695142c3dc7b0f8b8222fec80a6101c8cb9b352d.
```

No SAT or UNSAT result is claimed here.

