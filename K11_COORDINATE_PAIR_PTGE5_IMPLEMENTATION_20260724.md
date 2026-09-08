# Coordinate-pair omission and PTge5 implementation

## Status

The new opt-in source is

```text
scratch/k11_core_incidence/k11_forest_sat_paircuts.cpp
```

It is a mechanical clone of `k11_forest_sat_filtercuts.cpp` followed by
three separately gated additions:

```text
K11_FOREST_COORDINATE_PAIR_OMISSION=1
K11_FOREST_COORDINATE_PAIR_RANK5=1
K11_FOREST_PTGE5_INCIDENCE=1
```

Every previous gate remains available.  With all three new gates absent, the
new members merely retain already constructed vectors and allocate no SAT
variable or clause; the prior formula streams are unchanged.

The source and checker were uploaded to RunPod.  The checker passed under
Python 3.11, and warning-free C++2a compilation against the streaming
CaDiCaL shim produced

```text
k11_forest_dimacs_stream_paircuts
SHA-256 9bc92c38e838f4bbfa2b9afbc0a45a7cbda7e8e7166d5d23f79275c40f83092e.
```

Build-only streams to `/dev/null` exactly matched every predicted complete
inventory below.  No raw CNF was materialized and no solver was launched.

## 1. Coordinate-pair omission module

The occurrence plan now retains, at zero CNF cost, its exact flags

```text
free[p,b] <-> low[p] AND !A[p,b].
```

For every unordered coordinate pair `b<c`, the new plan defines

```text
free2[p,b,c] <-> free[p,b] AND free[p,c]
```

and exactly counts these flags as `Z_bc`.  It imposes

```text
Type I:                 Z_bc >= 128,
Type II tight:          Z_bc >= 128,
Type II non-tight:      Z_bc >= 86.
```

The Type-II comparisons reuse the occurrence plan's exact

```text
tight <-> duplicate OR two_components
```

flag.  Threshold comparisons are direct first-difference clauses, with one
clause for 128 and four clauses for 86.  The plan requires
`K11_FOREST_COORDINATE_OMISSION_OCCURRENCE`.

Exact incremental inventory:

| category | Type I variables | Type I clauses | Type II variables | Type II clauses |
|---|---:|---:|---:|---:|
| joint omission gates | 25,520 | 76,560 | 25,575 | 76,725 |
| exact counters | 50,600 | 354,200 | 50,710 | 354,970 |
| threshold clauses | 0 | 55 | 0 | 275 |
| **total** | **76,120** | **430,815** | **76,285** | **431,970** |

The 464 Type-I indices are positions 1--464; the 465 Type-II indices are
positions 0--464.  Alignment is inherited directly from the stored
one-coordinate banks.

## 2. Optional pair rank-five boundary

`K11_FOREST_COORDINATE_PAIR_RANK5` is Type-II-only and requires the B2 gate.
For every pair it reuses `Z_bc`, the existing exact `n5`, and the occurrence
tight flag to impose

```text
!tight -> 3*Z_bc+n5 >= 384.
```

Arithmetic is

```text
A=Z_bc+n5,
B=A+2*Z_bc.
```

This uses 19 full adders and two guarded threshold clauses per pair:

```text
2,090 variables / 14,740 clauses.
```

The positive `tight` escape literal is present in every comparison clause.

## 3. Stronger PTge5 module

`K11_FOREST_PTGE5_INCIDENCE` is independent of the coordinate modules.  It
requires Type II and `K11_FOREST_SHORT_CELL_RANK_VECTOR`.

When enabled, the rank-vector plan reuses each pair cell's existing exact
four-bit popcount to define and count pair rank at least six.  No popcount is
rebuilt.  It then exposes

```text
Pge5=P5+Pge6.
```

The exact triple sum

```text
Tge5=T5+Tge6
```

was already constructed by the rank-vector tail and is now retained for
reuse.  The new guarded row is

```text
!tight -> 2*Tge5+n5 >= Pge5+462.
```

The pair flag/count expansion costs

```text
1,384 variables / 8,296 clauses.
```

The standalone arithmetic and twelve-bit comparator retain the harmless
provably-zero high carry of `Pge5` and cost

```text
71 variables / 487 clauses.
```

Hence the exact total PTge5 increment is

```text
1,455 variables / 8,783 clauses.
```

This is sixteen variables and 112 clauses below the earlier 1,471/8,895
estimate because the implementation reuses the already existing `Tge5`
adder.  It does not rely on truncating either exact sum.

The older `K11_FOREST_PT5_INCIDENCE` gate is preserved.  PTge5 logically
dominates it, but enabling both deliberately emits both rows and adds the old
69-variable/473-clause module as well.

## 4. Predicted complete inventories

Starting from the audited parent totals, the main combinations are:

```text
Type I, rank vector + occurrence + companion + B2:
  3,834,577 variables / 21,173,979 clauses.

Type II, rank vector + occurrence + companion + B2:
  3,854,475 variables / 21,277,903 clauses.

Type II, preceding combination + B2-r5:
  3,856,565 variables / 21,292,643 clauses.

Type II, preceding combination + PTge5:
  3,858,020 variables / 21,301,426 clauses.

Type II, every preceding gate plus the older PT5 gate:
  3,858,089 variables / 21,301,899 clauses.
```

PTge5 alone on top of the audited Type-II rank-vector formula gives

```text
3,763,685 variables / 20,763,240 clauses.
```

## 5. Integration audit

All gates occur in:

1. environment parsing;
2. prerequisite validation;
3. portal-branch exclusion;
4. construction before `variable_total`;
5. clause emission;
6. the build banner and category ledgers.

The pair-rank-five plan cannot be constructed in Type I or without B2.
PTge5 cannot be constructed without Type II and the exact rank vector.  Pair
rank at least six is defined directly from the exact popcount, not as the
complement of ranks two through five.

The static checker is

```text
scratch/check_k11_coordinate_pair_implementation.py
```

It exhausts the direct comparator truth tables, the integer PTge5 implication,
the B2-r5 arithmetic, all exact counter widths and inventories, the predicted
complete totals, and the source integration markers.  Its output is

```text
PASS
B2 Type I: 76120 variables / 430815 clauses
B2 Type II: 76285 variables / 431970 clauses
B2-r5 Type II: 2090 variables / 14740 clauses
PTge5 total delta: 1455 variables / 8783 clauses
No local compilation or CNF generation was performed.
```

Two independent agents audited the actual source diff.  RunPod then supplied
the compilation and build-only checks:

```text
Type I, B2 strongest displayed combination:
  3,834,577 variables / 21,173,979 clauses.

Type II, B2 + B2-r5 + PTge5 + retained PT5:
  3,858,089 variables / 21,301,899 clauses.
```

The cgroup OOM counter remained unchanged at 35.  This is a verified
encoding/build result, not a SAT/UNSAT result.  A full raw token audit is
still required before any future solver launch.
