# Coordinate-pair filter companion implementation

## Status

The new opt-in source is

```text
scratch/k11_core_incidence/k11_forest_sat_pairfiltercuts.cpp
SHA-256 a525f21560379b65a157cc73dc475872a2290931bb5118a4f0ffe1eb7627c139
```

It is an additive clone of

```text
scratch/k11_core_incidence/k11_forest_sat_paircuts.cpp
SHA-256 93ad0da8256f5d180c02627cadede23c00db1d58a2ccdb0c0ed25c4818924913
```

with one new gate:

```text
K11_FOREST_COORDINATE_PAIR_FILTER=1.
```

The gate requires `K11_FOREST_COORDINATE_PAIR_OMISSION=1` and exactly one
rank-filtration branch.  It is mutually exclusive with
`K11_FOREST_COORDINATE_PAIR_RANK5=1` because the new package includes and
strictly extends that non-tight row.  Every older gate remains available.

The source and checker were uploaded to RunPod.  The checker passed under
Python 3.11.  Warning-free C++2a compilation against the streaming CaDiCaL
shim produced

```text
k11_forest_dimacs_stream_pairfiltercuts
SHA-256 7ae02db8400fa8be89272177c98dff840f931cb7c93746367609f61da4e39781.
```

No raw CNF was materialized and no solver was launched.

## 1. Encoded rows

For every unordered pair `B={b,c}`, let `Z_bc` be the existing exact count
of low positions whose entries omit both coordinates, and let `n5` be the
existing exact physical rank-five count.  The new package imposes

```text
Type I:
  Z_bc+n5       <= 362,
  6*Z_bc+5*n5   <= 2142.

Type II:
  6*Z_bc+5*n5      <= 2148,
  tight  -> Z_bc+n5 <= 363,
  !tight -> 3*Z_bc+n5 >= 384.                       (1.1)
```

The exact Type-II `tight` flag is the occurrence plan's already defined

```text
tight <-> duplicate OR two_components.
```

There are 642 nonempty masks of rank at most five which meet `B`.  Every
eligible low witness cell meeting `B` contains a low position outside the
`Z_bc` jointly omitting positions, and each such position belongs to at most
six singleton/pair/triple cells.  This gives

```text
6*(N-Z_bc)+n5 >= 642.
```

Using `N=464-n5` in Type I and `N=465-n5` in Type II gives the two sixfold
rows in `(1.1)`.  In Type I and tight Type II, the 306 rank-at-most-four
targets meeting `B` use singleton/pair witnesses.  The corresponding
threefold incidence bound gives the two `Z_bc+n5` rows.  The final non-tight
row is the previously audited rank-five avoidance companion.

## 2. Shared exact arithmetic

The plan forms one shared bank

```text
three_n5 = n5+2*n5
```

and, for each of the 55 coordinate pairs, retains

```text
A_bc = Z_bc+n5,
B_bc = A_bc+2*Z_bc       = 3*Z_bc+n5,
D_bc = 2*B_bc+three_n5  = 6*Z_bc+5*n5.              (2.1)
```

All carries are retained.  `A_bc` and `B_bc` are stored as plan members for
later companions at no additional CNF cost.  Direct first-difference
constant comparisons allocate no equality-prefix variables.

The source full-adder count is

```text
10 + 55*(9+10+12) = 1715 full adders.
```

At two variables and fourteen clauses per full adder, the exact inventory is

| category | Type I variables | Type I clauses | Type II variables | Type II clauses |
|---|---:|---:|---:|---:|
| shared/per-pair arithmetic | 3,430 | 24,010 | 3,430 | 24,010 |
| direct threshold clauses | 0 | 660 | 0 | 825 |
| **pair filter total** | **3,430** | **24,670** | **3,430** | **24,835** |

The Type-I threshold count is `55*(5+7)`.  Type II uses four clauses for
`A_bc<=363`, nine for `D_bc<=2148`, and two for `384<=B_bc`, for
`55*(4+9+2)=825`.  Guards add only their escape literal.

Relative to the separate Type-II pair-rank-five package, the combined plan
adds only

```text
1,340 variables / 10,095 clauses
```

while avoiding duplicate `A_bc,B_bc` arithmetic.

## 3. Complete predicted inventories

Starting from the immediate parent's audited combinations gives

```text
Type I, rank vector + occurrence + one-coordinate companion + B2
        + pair filter:
  3,838,007 variables / 21,198,649 clauses.

Type II, rank vector + occurrence + one-coordinate companion + B2
         + pair filter:
  3,857,905 variables / 21,302,738 clauses.

Type II, preceding combination + PTge5:
  3,859,360 variables / 21,311,521 clauses.          (3.1)

Type II, preceding combination + retained old PT5 as well:
  3,859,429 variables / 21,311,994 clauses.
```

The Type-II total in the second row already includes the non-tight
`3*Z_bc+n5>=384` comparison; the separate pair-rank-five gate must not be
added again.

## 4. Integration and disabled paths

The new gate occurs in:

1. environment parsing;
2. prerequisite and mutual-exclusion validation;
3. portal-branch exclusion;
4. plan construction before `variable_total`;
5. clause emission;
6. the build banner and exact category ledger.

When the gate is absent, no `CoordinatePairFilterPlan` is constructed, no
variable is allocated, and no clause is emitted.  The static checker also
verifies that every line of the parent source remains present in the clone
in the same order, so the source transformation is additive-only.

## 5. Static verification

The checker is

```text
scratch/check_k11_coordinate_pair_filter_implementation.py
SHA-256 ad8ac067dc068fa76257e0aaae0ef6258101768f0667c14a1805bdfea93d54b8
```

It verifies the target constants, exhausts all five direct constant
comparators at their retained widths, checks every arithmetic identity and
branch substitution over `0<=Z_bc<=465`, `0<=n5<=134`, recomputes the exact
inventories, checks the signed guards and integration markers, and performs
the additive parent-source check.  Its output is

```text
PASS
Pair filter Type I: 3430 variables / 24670 clauses
Pair filter Type II: 3430 variables / 24835 clauses
Parent source is an ordered subsequence; disabled CNF paths are additive-only.
No local compilation or CNF generation was performed.
```

An independent agent audited the actual source diff and found no defect.
RunPod build-only streams to `/dev/null` then matched exactly:

```text
Type I:  3,838,007 variables / 21,198,649 clauses.
Type II with PTge5 and retained old PT5:
         3,859,429 variables / 21,311,994 clauses.
```

The cgroup OOM counter remained 35.  This is a verified encoding/build
result, not a SAT/UNSAT result.  A full raw DIMACS token audit remains
required before any future solver use.
