# Type-II two-component B2 strengthening implementation

## Status

The new opt-in generator source is

```text
scratch/k11_core_incidence/k11_forest_sat_paircomponentcuts.cpp
```

It is an additive clone of

```text
scratch/k11_core_incidence/k11_forest_sat_pairfiltercuts.cpp
```

and adds two false-by-default, mutually exclusive gates:

```text
K11_FOREST_TYPE2_PAIR_COMPONENT_PROJECTION=1
K11_FOREST_TYPE2_PAIR_COMPONENT_EXACT=1
```

No local compilation, CNF generation, or solver run was performed while
preparing this source package.

## 1. Encoded inequalities

In the exact Type-II two-component branch, fix a coordinate pair
`B={b,c}`.  Let

```text
Z_B  = number of B-free low positions,
Z2_B = number of B-free positions in the selected slack-two component C2,
R2_B = number of nonempty B-free runs in C2.
```

The cheap gate encodes

```text
Z_B+Z2_B >= 255.                                    (1.1)
```

The exact gate instead encodes

```text
Z_B+Z2_B >= 255+R2_B.                               (1.2)
```

Both comparisons are guarded by the already exact
`two_components_flag`.  The gates are rejected if enabled together.

The source requires:

```text
K11_FOREST_COORDINATE_PAIR_OMISSION=1
K11_FOREST_RANK_FILTRATION_TYPE2=1
K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION=1.
```

No constraint from either new package is emitted when both new gates are
disabled.

## 2. Reused exact banks

`CoordinatePairOmissionPlan` now retains its already allocated and already
constrained literals

```text
free_B[p] <-> free[p,b] AND free[p,c]
```

in `pair_omission_flags`.  This is only a C++ vector copy and changes neither
the variable count nor the clause stream of B2.

The new plan also reuses

```text
TypeIITwoComponentPinPlan::slack_two_membership[p].
```

It defines

```text
z2[p] <-> free_B[p] AND slack_two_membership[p].
```

For the exact tier it additionally uses

```text
r2[0] = z2[0],
r2[p] <-> z2[p] AND !z2[p-1]  (1<=p<465).
```

The exact counters for `z2` and `r2` use the generator's full-adder
reduction.  The cheap comparison is a direct guarded first-difference
encoding of `255<=Z_B+Z2_B`.  The exact comparison constructs both ten-bit
sides and uses a guarded bidirectional equality-prefix comparator.  Every
prefix definition carries the escape literal `-two_components`, so inactive
auxiliaries impose no restriction.

## 3. Exact incremental inventories

For one coordinate pair, the cheap tier uses

| item | variables | clauses |
|---|---:|---:|
| 465 `z2` gates | 465 | 1,395 |
| exact `Z2` counter | 922 | 6,454 |
| nine-bit `Z+Z2` addition | 18 | 126 |
| guarded `255<=Z+Z2` threshold | 0 | 8 |
| **total** | **1,405** | **7,983** |

Across all 55 coordinate pairs this is exactly

```text
77,275 variables / 439,065 clauses.                  (3.1)
```

For one coordinate pair, the exact tier uses

| item | variables | clauses |
|---|---:|---:|
| 465 `z2` and 464 run-start gates | 929 | 2,787 |
| exact `Z2` and `R2` counters | 1,844 | 12,908 |
| two nine-bit additions | 36 | 252 |
| guarded ten-bit comparison | 9 | 55 |
| **total** | **2,818** | **16,002** |

Across all 55 pairs this is exactly

```text
154,990 variables / 880,110 clauses.                 (3.2)
```

These are the predicted increments in
`K11_POST_B2_STRENGTHENING_COMPARISON_20260724.md`.

## 4. Integration points

The two gates occur in:

1. environment parsing;
2. prerequisite and mutual-exclusion validation;
3. portal-branch exclusion;
4. plan construction before `variable_total`;
5. clause emission;
6. the build banner and category ledger.

The plan is Type-II-only and throws if constructed from a Type-I B2 bank.

## 5. Static audit

The companion checker is

```text
scratch/check_k11_type2_pair_component_implementation.py
```

It is designed to verify, when run in the remote build environment:

* the exact `465`-literal counter inventory;
* both per-pair and all-pair variable/clause totals;
* the direct `255<=x` comparator over all ten-bit inputs;
* the scalar identities `(1.1)` and `(1.2)` on their reachable domains;
* reuse of `pair_omission_flags` and `slack_two_membership`;
* the signed `two_components` guards;
* prerequisite and mutual-exclusion checks;
* allocation, emission, banner, and ledger markers;
* additive preservation of every parent-source line.

The source and checker were not compiled or executed locally.  They were
instead checked in the RunPod build environment.  The checker passed, an
independent source-diff audit passed, and warning-clean compilation produced

```text
k11_forest_dimacs_stream_paircomponentcuts
SHA-256 d1bcd864f3b1747584cc5711fdb0b9a966dc6f15f04d73d0da7349a1da08d693
```

Build-only streams on the complete current Type-II pair-filter formula,
including `PT5`, `PTge5`, and the retained `rank6_branch=0` units, matched
the symbolic increments exactly:

```text
projection: 3,936,704 variables / 21,751,059 clauses
exact:      4,014,419 variables / 22,192,104 clauses
```

No raw CNF was retained and no solver was launched.  The RunPod cgroup
OOM-kill counter remained 35.  These are encoding/build results only, not a
SAT or UNSAT result.

After the weaker external Type-II pair-filter run ended on its virtual-memory
cap, the exact component tier was promoted to the freed RunPod slot.  Its raw
DIMACS passed a complete token audit:

```text
declared variables = maxvar = 4,014,419
declared clauses   = clauses = 22,192,104
literals                     = 75,793,325
SHA-256 ae2bfab5e9841754cd193f45c32455d18719fb588372ecff23e892ef6c27617b
```

The old pair-filter raw file was first compressed and verified by streaming
decompression against its audited SHA-256 before removal; its `.zst` archive
is recoverable.  Kissat seed 501 then launched on CPU 20 under a 4 GiB
virtual-memory cap, with the result watcher updated before launch.  This is a
live exhaustive search, not yet a SAT or UNSAT result.
