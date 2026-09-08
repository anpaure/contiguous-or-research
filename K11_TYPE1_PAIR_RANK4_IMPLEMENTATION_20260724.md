# Type-I exact rank-four pair-omission Hall row

## Scope

This note records an additive SAT-generator implementation of the exact
rank-four coordinate-pair omission row recommended in
`K11_POST_B2_STRENGTHENING_COMPARISON_20260724.md`.

The implementation is in:

```text
scratch/k11_core_incidence/k11_forest_sat_pairrank4cuts.cpp
```

It is a clone of `k11_forest_sat_pairfiltercuts.cpp`.  No local compilation,
CNF generation, or solver run was performed while preparing this module.

## Gate and prerequisites

The new independent gate is:

```text
K11_FOREST_COORDINATE_PAIR_RANK4=1
```

It is accepted only when all three prerequisites are enabled:

```text
K11_FOREST_COORDINATE_PAIR_OMISSION=1
K11_FOREST_SHORT_CELL_RANK_VECTOR=1
K11_FOREST_RANK_FILTRATION_TYPE1=1
```

The existing dependency chain therefore also requires the local-density,
core-incidence, histogram, and short-cell-R3 modules already required by the
rank-vector and Type-I filtration.

With the new gate absent or zero, no new SAT variable and no new clause is
allocated.  The B2 plan merely retains its already-created jointly-free
position literals in `pair_omission_flags`; their definitions and ordering
are unchanged.  Thus the disabled DIMACS variable/clause stream is preserved.

## Encoded theorem

Fix a coordinate pair `B={b,c}`.  There are

```text
C(9,4)=126
```

rank-four lower targets omitting `B`.  In the Type-I branch every selected
lower witness has length one or two.  Define:

- `n4(B)`: B-free physical singleton cells of exact OR-rank four;
- `P4(B)`: B-free physical adjacent-pair cells of exact OR-rank four.

Choosing one physical witness for every distinct target gives the necessary
Hall row

```text
n4(B)+P4(B) >= 126.
```

This is imposed independently for all `C(11,2)=55` coordinate pairs.

## Exact source construction

Type I has 464 physical low positions, numbered 1 through 464, and 463
adjacent pairs, beginning at positions 1 through 463.

For every `B`, the implementation creates:

```text
singleton[p] <-> free_B[p] AND rank(entry[p])==4
pair[p]      <-> pair_OR_rank4[p] AND free_B[p] AND free_B[p+1]
```

where:

- `free_B[p]` is reused from `CoordinatePairOmissionPlan`;
- `rank(entry[p])==4` is the exact one-hot rank literal in
  `LocalDensityPBPlan`;
- `pair_OR_rank4[p]` is reused from
  `ShortCellRankVectorPlan::pair_rank_flags[2]`.

The 927 flags are combined in one exact Wallace/ripple counter.  The final
carry is retained, so the counter is not modular.  A direct first-difference
constant comparator enforces `126<=count` and allocates no prefix-equality
variables.

## Exact incremental inventory

For one coordinate pair:

| item | variables | clauses |
|---|---:|---:|
| 464 two-input singleton conjunctions | 464 | 1,392 |
| 463 three-input pair conjunctions | 463 | 1,852 |
| exact 927-input counter | 1,848 | 12,936 |
| direct `126<=count` comparator | 0 | 6 |
| **total** | **2,775** | **16,186** |

Across all 55 coordinate pairs, the exact expected increment is:

```text
152,625 variables / 890,230 clauses.
```

This matches the unoptimized-from-B2 inventory in the strengthening
comparison note.  It deliberately avoids constructing one-coordinate
rank-resolved banks solely to save the smaller optimized clause difference.

## Audit artifact

The static and arithmetic checker is:

```text
scratch/check_k11_type1_pair_rank4_implementation.py
```

It checks:

1. the environment gate and all prerequisite checks;
2. reuse of the retained B2 flags and rank-vector rank-four flags;
3. exact physical offsets (464 singleton and 463 adjacent-pair cells);
4. bidirectional two- and three-input conjunction truth tables;
5. the exact Wallace/ripple variable and clause inventory;
6. the direct `126<=count` comparator on every semantic count 0 through 927;
7. clause emission and diagnostic counters for the new plan.

The checker was not run locally.  Its first remote run exposed a checker-only
width typo: it described an eleventh carry bit even though the exact
927-input counter correctly has ten output bits.  After changing that audit
width from 11 to 10, the corrected checker passed the full semantic range.
This did not change the generator or its inventory.

An independent source-diff audit passed.  Warning-clean RunPod compilation
produced

```text
k11_forest_dimacs_stream_pairrank4cuts
SHA-256 39802756cd4034fe5f31fb06701c0ba759617b950972824a7f40cd8dc1de46fe
```

The complete current Type-I pair-filter build then matched exactly:

```text
3,990,632 variables / 22,088,879 clauses.
```

No raw CNF was retained and no solver was launched.  The RunPod cgroup
OOM-kill counter remained 35.  This is an encoding/build result only.

## Expected remote diagnostics

When the new gate is enabled on the Type-I pair-filter formula, the generator
should report:

```text
coordinate_pair_rank4_variables=152625
coordinate_pair_rank4_clauses=890230
coordinate_pair_rank4_candidate_variables=50985
coordinate_pair_rank4_candidate_clauses=178420
coordinate_pair_rank4_counter_variables=101640
coordinate_pair_rank4_counter_clauses=711480
coordinate_pair_rank4_threshold_clauses=330
```

The total formula should therefore be exactly the prior Type-I pair-filter
formula plus `152625` variables and `890230` clauses, subject to no other gate
changes.
