# K11 coordinate-triple filter implementation

## Status

The independently audited coordinate-triple omission/filter theorem in
`K11_COORDINATE_TRIPLE_FILTER_NEXT_20260724.md` is implemented as a guarded,
strictly additive SAT-encoder module.

To retain the strongest already implemented branch modules, there are two
deployment sources:

```text
Type II parent (exact pair-component retained):
  scratch/k11_core_incidence/k11_forest_sat_paircomponent_triplefiltercuts.cpp

Type I parent (pair-rank-four retained):
  scratch/k11_core_incidence/k11_forest_sat_pairrank4_triplefiltercuts.cpp
```

The new gate is

```text
K11_FOREST_COORDINATE_TRIPLE_FILTER=1
```

and requires `K11_FOREST_COORDINATE_PAIR_FILTER=1`.  The existing pair-filter
gate already requires B2 and exactly one rank-filtration branch.  The new gate
is also excluded from every portal-only branch.

No source was compiled and no CNF or solver process was run locally.

## Exact circuit

For each coordinate triple `B={a,b,c}`, with `a<b<c`, the implementation uses
the canonical already-materialized pair bank `free2[a,b]` and the exact
one-coordinate bank `free1[c]`:

```text
free3[p,B] <-> free2[p,{a,b}] AND free1[p,c].
```

An exact retained-carry counter gives `Z_B`.  The arithmetic vectors are

```text
A_B = Z_B+n5,
B_B = A_B+2*Z_B       = 3*Z_B+n5,
D_B = 2*B_B+three_n5 = 6*Z_B+5*n5.
```

`CoordinatePairFilterPlan::three_n5` is now retained as a member instead of
a local variable.  This is only a C++ lifetime change: it allocates no new SAT
variable, emits no clause, and preserves its original allocation/emission
position.

The emitted exact rows are:

```text
Type I:
  82 <= Z_B,
  Z_B+n5 <= 331,
  6*Z_B+5*n5 <= 1979.

Type II:
  tight  -> 82 <= Z_B,
  !tight -> 55 <= Z_B,
  6*Z_B+5*n5 <= 1985,
  tight  -> Z_B+n5 <= 332,
  Z_B+n5 <= 351,
  !tight -> 221 <= 3*Z_B+n5.
```

All comparisons use the existing direct first-difference encoding and allocate
no auxiliary comparator variables.

## Exact incremental inventory

There are `C(11,3)=165` coordinate triples.  The Type-I bank has 464 physical
low slots; Type II has 465.

### Type I

Per triple:

```text
464 free3 gates              464 variables / 1,392 clauses
464-input exact counter      920 variables / 6,440 clauses
31 arithmetic full adders     62 variables /   434 clauses
three direct comparisons       0 variables /    12 clauses
total                       1,446 variables / 8,278 clauses
```

Across 165 triples:

```text
238,590 variables / 1,365,870 clauses.
```

### Type II

Per triple:

```text
465 free3 gates              465 variables / 1,395 clauses
465-input exact counter      922 variables / 6,454 clauses
31 arithmetic full adders     62 variables /   434 clauses
six guarded/direct rows        0 variables /    30 clauses
total                       1,449 variables / 8,313 clauses
```

Across 165 triples:

```text
239,085 variables / 1,371,645 clauses.
```

Using the already audited strongest-parent build totals, the predicted full
build-only inventories are:

```text
Type I pair-rank-four + triple filter:
  4,229,222 variables / 23,454,749 clauses.

Type II exact pair-component + triple filter:
  4,253,504 variables / 23,563,749 clauses.
```

RunPod build-only streams confirmed both totals exactly.

## Static audit

The source-only checker is

```text
scratch/check_k11_coordinate_triple_filter_implementation.py
```

It verifies:

1. the exact 464/465-input counter inventories;
2. all first-difference comparator truth tables over their complete bit widths;
3. the exact bidirectional `free3` conjunction truth table;
4. every Type-I and Type-II constant and guard;
5. marker presence for construction, clause emission, diagnostics, gate
   prerequisite, and portal exclusion;
6. exact normalization of each disabled child source back to its corresponding
   strongest parent.

The last check removes only the new guarded module/wiring and changes the
retained `three_n5` member spelling back to the old local spelling.  The result
must equal the parent byte for byte.  This certifies additive allocation and
ordered clause emission when the new gate is disabled.

An independent actual-diff audit separately checked the relative placement:
construction precedes `variable_total`, emission is in the intended module
order, diagnostics follow the build banner, and portal exclusion is in the
active branch guard.  Both sources passed that audit.

Static-check output:

```text
PASS
Type I increment: 238590 variables / 1365870 clauses
Type II increment: 239085 variables / 1371645 clauses
Both strongest branch-specific parents retain their existing modules.
Disabled source normalizes exactly to each parent; no old CNF path moved.
No local compilation, CNF generation, or solver run was performed.
```

The same checker passed under RunPod Python 3.11.  An independent actual-diff
audit also passed both sources, including bank alignment, all arithmetic
widths and guards, strongest-parent retention, placement, diagnostics, portal
exclusion, and disabled normalization.

## Source hashes before remote build

```text
67f1cf72a1e81a43591a2f7975baa980596b780935691aa1aaa40cc625ea3252
  scratch/k11_core_incidence/k11_forest_sat_paircomponent_triplefiltercuts.cpp

35b34b1cbdb362023a9f5b0c433c1225e1e20fff263bd6a690303795cb8334e7
  scratch/k11_core_incidence/k11_forest_sat_pairrank4_triplefiltercuts.cpp

d56ebdfcb2a33f1426128886f2cf29211f126cd9a497de21b277b11121f8ff98
  scratch/check_k11_coordinate_triple_filter_implementation.py
```

The parent hashes are:

```text
8defd7d2e9f34fe446f259b57ecb56bbcb82a74943118091cd45482c95aafd84
  scratch/k11_core_incidence/k11_forest_sat_paircomponentcuts.cpp

9cb42b2cf3c212e7eacd9257c12dd43beff2c0aa1a18a487c6de82d55edd1151
  scratch/k11_core_incidence/k11_forest_sat_pairrank4cuts.cpp
```

Warning-clean RunPod compilation produced:

```text
558d6c324fb3689e30e41ab7b8df9b644eee8a4e27dfbd8ed39787eddad6db95
  k11_forest_dimacs_stream_paircomponent_triplefiltercuts

77757c75f3253892c725f8701e433f2b1257f3ae5a83eaece9980eaf0c5a24fd
  k11_forest_dimacs_stream_pairrank4_triplefiltercuts
```

The strongest build-only streams were exactly:

```text
Type II exact pair-component + triple filter:
  4,253,504 variables / 23,563,749 clauses.

Type I pair-rank-four + triple filter:
  4,229,222 variables / 23,454,749 clauses.
```

No raw CNF was retained and no solver was launched for this module.  The
RunPod cgroup OOM-kill counter remained 35.

The former external Type-I pair-filter search later ended on its tightened
virtual-memory cap with no mathematical terminal marker.  Its raw CNF was
compressed, verified by streaming decompression against SHA-256
`e9e4fdbf...9ab115f0`, and only then removed.  The stronger Type-I
pair-rank-four plus triple-filter raw formula passed a full token audit:

```text
declared variables = maxvar = 4,229,222
declared clauses   = clauses = 23,454,749
literals                     = 79,993,676
SHA-256 4ebb66ae319c8dded33901890c83f7e6e261bcc76ae2e9141991262d43b5f972
```

Kissat seed 511 then launched on CPU 22 under a 4 GiB virtual-memory cap,
with the result watcher updated first.  This is a live exhaustive search and
does not yet change a bound.

## Recommended remote deployment flags

Type II should retain the exact pair-component module:

```text
K11_FOREST_COORDINATE_PAIR_FILTER=1
K11_FOREST_TYPE2_PAIR_COMPONENT_EXACT=1
K11_FOREST_COORDINATE_TRIPLE_FILTER=1
```

along with all prerequisites already required by the exact pair-component
source.

Type I should retain the pair-rank-four module:

```text
K11_FOREST_COORDINATE_PAIR_FILTER=1
K11_FOREST_COORDINATE_PAIR_RANK4=1
K11_FOREST_COORDINATE_TRIPLE_FILTER=1
```

along with the Type-I rank-vector prerequisites.

Before any solve, both sources still require remote compilation, build-only
inventory confirmation, disabled-DIMACS comparison, and raw-token audit.
