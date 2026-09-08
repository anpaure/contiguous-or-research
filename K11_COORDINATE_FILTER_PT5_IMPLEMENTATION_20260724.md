# Coordinate-filter companion and PT5 implementation

## Status

The next opt-in source is

```text
scratch/k11_core_incidence/k11_forest_sat_filtercuts.cpp
SHA-256 f08430662d2b3af8bf16c30748e78c5fa324423e18bed6977c48ea69338124fe
```

It is a byte-for-byte clone of the occurrence-cut source followed by two
separately gated additions:

```text
K11_FOREST_COORDINATE_FILTER_COMPANION=1
K11_FOREST_PT5_INCIDENCE=1.
```

The first gate requires
`K11_FOREST_COORDINATE_OMISSION_OCCURRENCE=1`.  The second is Type-II-only
and requires the audited short-cell rank-vector module.  Frozen sources were
not edited.  No local compilation, CNF generation, or SAT solving was run.

## 1. Coordinate-filter companion

Let `Z_b` be the exact low-position omission count already exposed by the
occurrence plan and let `n5` be the exact literal rank-five count.  The new
plan imposes

```text
Type I:
  Z_b+n5       <= 405,
  6*Z_b+5*n5   <= 2398,
  3*Z_b+n5     >= 640.

Type II:
  tight -> Z_b+n5 <= 406,
  6*Z_b+5*n5      <= 2404,
  3*Z_b+n5        >= 640.                           (1.1)
```

The redundant non-tight row `Z_b+n5<=435` is deliberately absent.

Arithmetic is shared exactly.  Once per branch, form

```text
three_n5 = n5+2*n5.
```

For each coordinate form

```text
A_b = Z_b+n5,
B_b = A_b+2*Z_b       = 3*Z_b+n5,
D_b = 2*B_b+three_n5  = 6*Z_b+5*n5.                (1.2)
```

All carries are retained.  The direct constant comparisons are exact and
need no equality-prefix variables.  The Type-II `A_b<=406` row reuses the
exact

```text
tight <-> duplicate OR two_components
```

flag from the occurrence plan.

## 2. Standalone PT5 row

The independent Type-II-only gate imposes, under `!tight`,

```text
P5+462 <= 2*Tge5+n5.                                (2.1)
```

It reuses

```text
P5   = exact number of active low pair cells of OR-rank five,
T5   = exact number of active low triple cells of OR-rank five,
Tge6 = exact number of active low triple cells of OR-rank at least six,
Tge5 = T5+Tge6.
```

The comparator's guard is the signed literal `-tight`; every order and
prefix-equality clause contains its escape literal `tight`.  Thus (2.1) is
active exactly in the no-duplicate one-component mode and imposes nothing
in either tight mode.

## 3. Exact incremental inventory

The companion arithmetic uses

```text
10 + 11*(9+10+12) = 351 full adders.
```

With two variables and fourteen clauses per full adder, its exact inventory
is:

| category | Type I variables | Type I clauses | Type II variables | Type II clauses |
|---|---:|---:|---:|---:|
| shared/coordinate arithmetic | 702 | 4,914 | 702 | 4,914 |
| direct threshold clauses | 0 | 143 | 0 | 165 |
| **coordinate companion** | **702** | **5,057** | **702** | **5,079** |

PT5 uses 29 full adders and one twelve-bit guarded comparator:

| category | variables | clauses |
|---|---:|---:|
| arithmetic | 58 | 406 |
| guarded comparator | 11 | 67 |
| **PT5 total** | **69** | **473** |

With the audited rank-vector and occurrence modules also enabled, the
predicted full inventories are therefore

```text
Type I, occurrence+companion:
  3,758,457 variables / 20,743,164 clauses.

Type II, occurrence+companion+PT5:
  3,778,259 variables / 20,846,406 clauses.          (3.1)
```

Useful partial combinations are

```text
Type II, rank-vector+PT5 only:
  3,762,299 variables / 20,754,930 clauses.

Type II, occurrence+companion without PT5:
  3,778,190 variables / 20,845,933 clauses.          (3.2)
```

The Type-II duplicate flag is already present in the audited rank-vector
formula, so no additional upstream exposure charge appears in these totals.

## 4. Integration audit

Both gates are included in:

1. environment parsing;
2. their exact prerequisite checks;
3. portal-branch incompatibility;
4. plan construction before `variable_total`;
5. clause emission;
6. the build summary and exact category ledgers.

The coordinate companion cannot be constructed without a nonnull occurrence
plan.  PT5 cannot be constructed outside Type II or without the exact
rank-vector counters.  With both gates absent, neither plan allocates a
variable or emits a clause.

The static checker is

```text
scratch/check_k11_coordinate_filter_implementation.py
SHA-256 dd1d020d894f78fffbb48bde5d3d357b9431fd330dcde26f34d957a5d8bd67f1
```

It exhausts every direct constant comparator, every reachable `Z_b,n5`
arithmetic identity, and every integer PT5 premise; independently recomputes
both exact inventories; and checks all source integration markers.  It also
asserts that constant `435` does not occur in the companion class.

Its output is

```text
PASS
Coordinate companion Type I: 702 variables / 5057 clauses
Coordinate companion Type II: 702 variables / 5079 clauses
PT5 incidence Type II: 69 variables / 473 clauses
No local compilation or CNF generation was performed.
```

## 5. RunPod confirmation

The frozen source and audit artifacts were copied byte-for-byte to Rose.
Their remote hashes matched the values above, and the checker passed under
Python 3.11.  Compilation with
`-O3 -std=c++2a -Wall -Wextra -Wpedantic` and the DIMACS streaming shim
emitted zero warning bytes.  The streaming binary has SHA-256

```text
1bcb40027d404639cdac54bd79a92ac08eeebacb3dceff3ca4e0247e2098582e
```

Build-only `/dev/null` streams exactly matched the predictions:

```text
Type I occurrence+companion:
  3,758,457 variables / 20,743,164 clauses
  companion delta: 702 / 5,057

Type II occurrence+companion+PT5:
  3,778,259 variables / 20,846,406 clauses
  companion delta: 702 / 5,079
  PT5 delta:        69 /   473
```

No raw CNF was retained and no live solver was added or replaced.

## Scope

This is a static implementation audit, not a SAT/UNSAT result.  RunPod
compilation and build-only streaming are complete; a materialized DIMACS
would still require token auditing before use in an exhaustive solver slot.
No live solver was changed.
