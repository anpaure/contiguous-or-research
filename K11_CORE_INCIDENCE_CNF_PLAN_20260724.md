# Implementation-ready CNF plan for the k=11 core-incidence cuts

## Scope and frozen baseline

This is an independently audited patch plan against the frozen Rose source

```text
/root/k11_onion_20260723/k11_forest_sat_newcuts.cpp
sha256 2ab8ce03f844884c1dc6c5b4f742fe6e447680589172610fcd9649906ebdc26c
```

The production source is not modified.  The first implementation should be a
new opt-in copy, with the frozen file retained byte-for-byte.

The source already supplies every logical input needed by the cuts:

* `LocalDensityPBPlan::rank[p][r]` is an exact one-hot rank bank;
* `JointBandCutPlan::bits[j]` is the exact nine-bit value of `h(j+1)`;
* `RankFiltrationTypeIIPlan::n5_count` is an exact nine-bit `n5`;
* `RankFiltrationTypeIIPlan::two_components_flag` is exact;
* `RankFiltrationTypeIIPlan::duplicate_flag` is exact whenever its existing
  flag-exposure circuit is enabled.

Only the Type-I `n5` count must be exposed: change the local `n5` in
`RankFiltrationTypeIPlan::build()` into a `vector<int> n5_count` field, exactly
as Type II already does.  This changes no variables or clauses.

## Recommended option and dependencies

Add an environment option

```text
K11_FOREST_CORE_INCIDENCE = i1 | i2 | i3 | all
```

Absent means strict guard-off identity: no object, variable, or clause is
created.  The option requires exactly one of
`K11_FOREST_RANK_FILTRATION_TYPE1` and
`K11_FOREST_RANK_FILTRATION_TYPE2`.  Those options already require local
density, band cuts, and joint band cuts.  Add the new option to the list of
modules forbidden by `K11_FOREST_PORTAL_BRANCH`.

For Type II, construct `RankFiltrationTypeIIPlan` with

```cpp
enable_duplicate_flag = named_cell_hall || core_incidence_enabled;
```

This exposes the exact `duplicate_flag` even when the named-cell module is
off.  `two_components_flag` is already always exposed.  No new top-level
branch selector is needed: an instance already has exactly one filtration
type.

## Exact arithmetic

Create a standalone `CoreCellIncidencePlan` after the two rank-filtration
plans.  Reuse `local.one`; do not allocate a second constant-one variable.
Copy the existing bidirectional `full_adder`, retained-carry
`add_unsigned`, Wallace `exact_count`, guarded/un-guarded lexicographic
comparison, and direct constant-comparison primitives.  A sequential or
modular counter must not be substituted: these rows need exact ordinary
integer sums.

### Shared S bank

For each `r=1,2,3,4`, count the 465 literals

```text
local.rank[0][r],...,local.rank[464][r]
```

exactly.  The existing Wallace algorithm uses 453 compressor full adders and
eight final-ripple full adders, or 461 full adders per count.  Its returned
count has width nine.

Form

```text
S = n1 + 2*n2 + 3*n3 + 4*n4
```

as follows, retaining every generated carry:

```text
p12 = n1 + (n2 << 1)                         10 FAs, width 11
p3  = n3 + (n3 << 1)                         10 FAs, width 11
p34 = p3 + (n4 << 2)                         11 FAs, width 12
S   = p12 + p34                              12 FAs, width 13
```

The standalone shared bank therefore uses exactly

```text
1887 full adders = 3774 variables / 26418 clauses.
```

No rank-`<=4` membership gate is needed: the one-hot rank literals themselves
are the counter inputs.  In Type I the fixed rank-six endpoint contributes
zero automatically; in Type II every low component is counted automatically.

### I1

Encode

```text
S >= 649.
```

The direct first-difference comparator adds one clause for each one-bit of
`649 = 2^9+2^7+2^3+1`, hence four clauses and no variables.

* Type I: unguarded.
* Type II: prepend `-duplicate_flag` to each of the four clauses.

### I2

Use the chain-independent boundary identity, in the overflow-safe form

```text
1938 + 5*(h2+h4+h6) <= 3*S + 5*(h1+h3+h5).
```

For each of the odd and even triples, first sum the three nine-bit boundaries
(9+10=19 full adders, width 11), and only then multiply the result by five
using `x+(x<<2)` (13 full adders, width 14).  This costs 64 full adders for
both sides, versus 116 if all six `5*hi` values are materialized separately.

Then form

```text
threeS = S + (S << 1)                        14 FAs, width 15
lhs    = 5*even + 1938                       14 FAs, width 15
rhs    = threeS + 5*odd                      15 FAs, width 16
```

The 16-bit exact lexicographic comparator uses 15 prefix-equality variables
and `6*16-5=91` clauses.

* Type I: unguarded.
* Type II: every comparator and prefix-definition clause is guarded by
  `duplicate_flag`.  Arithmetic gates may remain unguarded exact definitions;
  they impose no restriction on their inputs when the final comparison is
  inactive.

### I3 / II3

Do not materialize the three A/B/C substitutions.  Reuse physical `n5`:

```text
sixS  = threeS << 1                         no FAs, width 16
fiveN = n5 + (n5 << 2)                       11 FAs, width 12
rhs3  = sixS + fiveN                         16 FAs, width 17
```

For Type I impose `rhs3>=4254` unconditionally.

For Type II impose

```text
rhs3 >= 4254                                      unconditionally
duplicate_flag      -> rhs3 >= 4259
two_components_flag -> rhs3 >= 4259.
```

This exactly covers `(delta5,s)=(0,1),(1,1),(0,2)`.  It avoids exposing a new
public `stability_tight` field.  The constants have respectively six and five
one-bits, so Type I uses six direct clauses and Type II uses
`6+5+5=16` direct clauses.  The two conditional copies are intentional and
cost no new OR-guard variable.

## Audited inventories

Every full adder is exactly two variables and fourteen clauses.  Raw ripple
outputs are retained; no semantic-width trimming is assumed.

| rows | branch | variables | clauses |
|---|---:|---:|---:|
| I1 only | I or II | 3774 | 26422 |
| I2 only | I or II | 4003 | 28007 |
| I3 only | I | 3856 | 26998 |
| I3 only | II | 3856 | 27008 |
| I1+I2+I3 | I | **4057** | **28395** |
| I1+I2+I3 | II | **4057** | **28405** |

For all three rows, the ledger is:

```text
four exact counts                             1844 FAs
weighted S                                      43 FAs
two boundary triple sums and two x5 values      64 FAs
3*S                                             14 FAs
I2 side additions                               29 FAs
5*n5 and final I3 addition                      27 FAs
                                                -------
total arithmetic                              2021 FAs
```

Thus arithmetic contributes 4042 variables and 28294 clauses; I2 contributes
15 comparator variables and 91 clauses.  Constant comparisons contribute ten
clauses in Type I and twenty in Type II.

If Type II previously had neither named-cell Hall nor another consumer of the
duplicate flag, enabling exact duplicate exposure adds a separate
**40 variables / 187 clauses** inside `RankFiltrationTypeIIPlan`: equality
widths 11,12,12 cost 38 variables/178 clauses, the selected tight flag costs
1/6, and `duplicate_flag` costs 1/3.  This cost is already present when
`K11_FOREST_NAMED_CELL_HALL` is enabled.  Accordingly the total incremental
cost over a Type-II build with no prior flag consumer is 4097 variables and
28592 clauses; over the current named-cell build it is exactly 4057/28405.

### Optional Type-I n1/n2 reuse

As a second-stage optimization only, expose `n1_count`, `n2_count`, and
`profile_count=n1+2*n2` from `TypeIGlobalPairProfilePlan`, and instantiate it
before the incidence plan.  This changes that plan's inventory by zero.  The
new S bank then needs only the n3/n4 counters and 33 further adders:

```text
1910 variables / 13370 clauses.
```

With all rows, the incremental incidence inventory above an already-enabled
global-pair plan becomes

```text
2193 variables / 15347 clauses.
```

The first benchmark should nevertheless use the standalone 4057-variable
version, because it is a smaller source refactor and gives a clean inventory
delta.

## Minimal source integration points

Against the frozen source:

1. Near `RankFiltrationTypeIPlan` (currently around lines 2330--2522), expose
   `n5_count` as a field; do not recompute it.
2. Near `RankFiltrationTypeIIPlan` (around lines 1147--1503), retain the
   existing exact duplicate circuit and enable it when either named-cell Hall
   or the new option is active.
3. Add `CoreCellIncidencePlan` after the filtration-plan definitions.
4. Parse and validate the new row option near the other environment flags
   (around lines 3754--3995).
5. Instantiate it immediately after both filtration objects (around line
   4176), then emit its clauses beside those plans (around line 4280).
6. Add module and sub-ledger inventories to the final diagnostic line.
7. Add the new option to portal-branch incompatibility checks.

Recommended diagnostics are `counter_variables`, `counter_clauses`,
`arithmetic_variables`, `arithmetic_clauses`, `comparator_variables`, and
`comparator_clauses`, plus the selected row mask.

## Required validation before solving

1. Compile only a copied opt-in variant; preserve the frozen source and hash.
2. Run build-only inventories for `i1`, `i2`, `i3`, and `all` in both Type I
   and Type II.  Exact differences must match the table above, including the
   conditional 40/187 Type-II flag bank.
3. Stream each new CNF and audit header variables, header clauses, maximum
   literal, and zero terminators.
4. On small randomized assignments to rank and boundary inputs, exhaustively
   compare the circuit output with ordinary integer evaluation of I1--I3.
5. Only after those checks, benchmark propagation and solving.  A silent
   solver exit or OOM remains no evidence of UNSAT.

## Hazards

* The old A-only singleton formula is unsound on chains B and C.  I2 must use
  the universal `y1` identity; I3 should use physical `n5` as above.
* In Type II, `z` is `n5-1` in the duplicate branch.  Substituting `z=n5`
  there weakens the required threshold by five and is incorrect.
* I1 and I2 are not valid in the no-duplicate one-component or two-component
  branches; their Type-II guard must be the exact `duplicate_flag`, not
  `stability_tight` and not `!two_components`.
* I3 needs the stronger threshold in both the duplicate and two-component
  branches.  Guarding it only by `duplicate_flag` misses `(0,2)`.
* All carries must be retained.  Modular addition can admit false profiles.
* Guarding only the first comparator clause is insufficient.  Every
  prefix-equality definition in a guarded comparator must carry the guard.
* Do not count incidental OR values from literal atom words in the certified
  ledger; the cuts concern exact physical rank/count variables.

