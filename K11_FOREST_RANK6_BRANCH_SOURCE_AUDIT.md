# Independent source audit: exact `k=11` rank-six portfolio branch

## Verdict

**PASS.**  The current source

```text
k11_forest_sat.cpp
SHA-256 c1eff19c73fa6610bd603194a43c89ffb5a54092cb35947fda64c6ed61876f0b
```

correctly implements the audited `K11_FOREST_RANK6_BRANCH=0|1` design.

* Both branches emit the exact 12-literal anchor and one branch unit.
* Branch zero allocates and emits no profile circuit.
* Branch one allocates exactly 241 variables and emits exactly 1,659 profile
  clauses.
* The anchor plus the existing canonical/boundary clauses gives
  `A[0]=63 <-> e`.
* Units `-e` and `e` therefore form the exact no-rank-six/sole-`A[0]=63`
  partition.
* All three chain-specific profile inequalities, guards, constants, term
  orders, and formula totals are correct.

No solver source or main handoff was modified by this audit.

## 1. Exact previous-source reconstruction and diff

The implementation was recorded as five source patches.  I reversed them in
reverse order and obtained

```text
scratch/k11_forest_sat_before_branch_reconstructed.cpp
SHA-256 1172c55d5ab21f829af8263cb5cc13e65dec0179c5a50159ed3c1b064ba21c81
```

which exactly matches the requested pre-edit snapshot.

The direct old/new source diff has SHA-256

```text
93ba862fa6927ca4c9f23ef513203d2712363962fccacf54c18b0c18680867a0
```

and contains only:

1. `RankSixBranchProfilePlan`;
2. strict environment parsing and dependency validation;
3. conditional profile-plan allocation;
4. conditional profile-clause insertion;
5. the anchor and branch unit;
6. diagnostics.

No pre-existing hard clause or variable allocation was altered.  When the
environment variable is absent, the plan is null, `next` is unchanged, and
neither anchor nor unit is emitted.

Both source snapshots compile warning-free at
`-O3 -std=c++20 -Wall -Wextra -Wpedantic` against the deterministic build-only
CaDiCaL test double.

## 2. Guard parsing and dependencies

The source initializes

```text
rank_six_branch=-1
```

and changes it only when the environment variable is present with exact
string value `"0"` or `"1"`.  Absence disables the feature.  Empty string,
`00`, `2`, `true`, and every other string exit with status 2 and

```text
K11_FOREST_RANK6_BRANCH must be absent or exactly 0 or 1
```

For either valid branch, all four required guards are checked before reading
the seed or allocating plans:

```text
K11_FOREST_CANONICAL_RANK6_ENTRY
K11_FOREST_RANK6_BOUNDARY_ENTRY
K11_FOREST_BAND_CUTS
K11_FOREST_JOINT_BAND_CUTS.
```

Omitting canonical, boundary, or joint while keeping the other prerequisites
exits with status 2 and the complete dependency diagnostic.  Omitting both
band and joint does likewise.  If joint is independently requested without
band, the earlier joint-band dependency check safely exits before any null
dereference.

The dependency set is neither too weak nor unnecessarily broad:

* band and joint allocate the reused boundary bits, chain selectors, true
  constant, and exact `e=x0`;
* canonical and boundary provide the hard reverse implication
  `e -> A[0]=63` and its literal-entry semantics;
* adjacent shadows, rank-three shadows, endpoint alignment, and the
  singleton-pool guard are optional.

## 3. Allocation and clause-insertion order

`BandCutPlan` and `JointBandCutPlan` are allocated first.  The source then
allocates `RankSixBranchProfilePlan` if and only if

```text
rank_six_branch==1.
```

This occurs before `variable_total` is frozen and before
`declare_more_variables`, so all 241 branch-one auxiliaries are declared.
Branch zero and disabled mode do not construct the plan and do not advance
`next`.

Profile clauses are transferred to the solver when the plan exists.  The
anchor and unit are then emitted for either selected branch.  Canonical and
boundary literal gates are emitted later, but CNF clause order has no logical
effect; all reverse-implication clauses are present in the same final formula.
Proof tracing and DIMACS writing see the complete variable and clause set.

## 4. Exact source anchor and branch units

The source constructs

```text
anchor = {e}
```

and appends, for bits zero through ten,

```text
-A[0,b] for b=0,...,5,
 A[0,b] for b=6,...,10.
```

This is exactly the 12-literal clause

```text
A[0]=63 -> e.
```

The canonical-plus-boundary hard clauses already allow a literal rank-six
entry only as `A[0]=63`.  Since `e=1` is exactly the existence of a selected
rank-six singleton and the central singleton's value equals its array entry,
the existing formula supplies

```text
e -> A[0]=63.
```

Thus the implemented anchor gives the audited equivalence.  The source then
emits exactly one unit using

```text
rank_six_branch==1 ? e : -e.
```

The polarity is correct:

```text
branch 0: -e
branch 1:  e.
```

Both diagnostic counters are incremented at these actual addition sites and
report one in either branch and zero when disabled.

## 5. Exact branch partition

In branch zero, `e=0` and the anchor force `A[0]!=63`.  The canonical and
oriented-boundary gates already forbid every other literal rank-six
value/position pair.  Therefore no literal rank-six entry exists.

In branch one, `e=1`; the existing reverse implication forces `A[0]=63`, and
the canonical/boundary gates make it the sole literal rank-six occurrence.

The two units are contradictory, so the branches are disjoint.  Since every
Boolean model of the common anchored formula has either `e=0` or `e=1`, they
are exhaustive.  The previously audited symmetry/reselection theorem makes
the common anchored formula equisatisfiable with the normalized unrestricted
existence problem.

## 6. Branch-one profile source

The plan reuses exactly:

```text
rank_six_plan.bits[1] = g2
rank_six_plan.bits[4] = g5
joint_plan.bits[1]    = h2
joint_plan.bits[2]    = h3
joint_plan.bits[3]    = h4
joint_plan.bits[4]    = h5
joint_plan.chain_selector[0..2]
joint_plan.one.
```

`constant_bits(557)` has ten bits and allocates no variable.  The three source
calls are exactly:

```text
A: g2+557+h2+h4 <= h3+h5+g5
B: g2+557+h2    <= h3+g5
C: g2+557+h4    <= h5+g5.
```

Their guards are the corresponding exact-one rank-five chain selectors.
Because this plan exists only in branch one and the same formula contains the
unit `e`, no second `e` guard is needed.  Every comparator clause, including
all five prefix-equality clauses per higher bit, contains the chain guard.

The source orders all nine-bit boundary terms before the ten-bit constant,
matching the audited minimum-width term order.  Its ripple adders retain the
final carry and use the same exact `2w/14w` circuit as the already audited
joint plan.  Unguarded adders are total definitions and impose no extra input
restriction for inactive chain rows.

## 7. Algebra of the implemented rows

The exact rank-six identities are

```text
x1=g2+462-g5-e.
```

The strengthened theorem is

```text
y2>=x1+82+14e.
```

Under the branch-one unit this becomes

```text
g2+557<=y2+g5.
```

For the three selected rank-five chains,

```text
A: y2=(h3-h2)+(h5-h4)
B: y2=h3-h2
C: y2=h5-h4,
```

which yield exactly the three source comparisons in Section 6.  Every sign
and constant is correct.

Branch zero constructs no profile plan.  Its specialization
`y2>=x1+82` is already implied by the existing joint-band circuit (indeed the
existing fan and cumulative rows imply `y2>=x1+84` when `e=0`).  Hence no
branch-zero profile clauses are missing.

## 8. Exact profile inventory

Independent width-by-width reconstruction gives:

| row | adder variables/clauses | comparator variables/clauses | total |
|---|---:|---:|---:|
| A | `98 / 686` | `11 / 67` | `109 / 753` |
| B | `56 / 392` | `10 / 61` | `66 / 453` |
| C | `56 / 392` | `10 / 61` | `66 / 453` |
| **total** | `210 / 1,470` | `31 / 189` | **`241 / 1,659`** |

The actual allocated plan reports exactly these totals.  Thus the deltas from
the common unbranched prerequisite formula are:

```text
branch 0:   0 variables,    2 clauses  (anchor + unit)
branch 1: 241 variables, 1661 clauses  (profile + anchor + unit).
```

Equivalently, branch one differs from branch zero by precisely

```text
241 variables / 1,659 clauses.
```

## 9. Guard-off identity and all formula totals

Build-only generation with the exact old and new sources gives:

| configuration | variables | clauses |
|---|---:|---:|
| all guards off, old | 4,892,622 | 15,524,818 |
| all guards off, current/branch absent | 4,892,622 | 15,524,818 |
| four prerequisites, old | 4,899,664 | 15,777,974 |
| four prerequisites, current/branch absent | 4,899,664 | 15,777,974 |
| all previous structural guards, old | 2,924,697 | 14,732,378 |
| all previous structural guards, current/branch absent | 2,924,697 | 14,732,378 |
| four prerequisites + branch 0 | 4,899,664 | 15,777,976 |
| four prerequisites + branch 1 | 4,899,905 | 15,779,635 |
| all structural guards + branch 0 | 2,924,697 | 14,732,380 |
| all structural guards + branch 1 | 2,924,938 | 14,734,039 |

These reproduce every total in
`K11_FOREST_RANK6_BRANCH_IMPLEMENTATION.md`.  The branch-one minus branch-zero
difference is `241/1,659` in both the minimal-prerequisite and fully guarded
profiles.

## 10. Checker evidence and hashes

The implementation checker is

```text
scratch/verify_k11_rank6_branch_implementation.cpp
SHA-256 55ff98228a78fee35ff65175afd757e115a16d226eaf9748b2c2a68ccea3565c
```

It compiles warning-free and reports:

```text
anchor_equivalence=PASS
branch_partition=PASS
branch0_profile_variables=0 clauses=0
branch1_profile_variables=241 clauses=1659
anchor_variables=0 clauses=1 unit_clauses=1
```

The independent design-audit checker is

```text
scratch/audit_k11_rank6_branch_profile_design_independent.cpp
SHA-256 289e40fa1a52c8fbb8041720e27a376b671cff83d237f41ba333d28f1541ac39
```

and independently exhausts the anchor, genuine chain-count algebra, guard
semantics, inventories, and Boolean partition.  The source diff plus the
deterministic old/new builds establish that the checked design is the one
actually integrated into the current source.

## 11. Scope

This audit certifies the source implementation and exact formula generation;
it does not claim either branch SAT or UNSAT.  A branch SAT model still needs
independent OR verification.  Two branch UNSAT results require checked proof
artifacts plus a validated case-split/cube wrapper, assumption discharge, or
an additional proof-producing run of the unbranched anchored formula.
