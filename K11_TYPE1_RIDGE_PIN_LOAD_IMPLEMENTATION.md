# Implementation: Type-I boundary-ridge pin load

## Status

The independently audited ridge theorem is implemented in
`k11_forest_sat.cpp` behind

```text
K11_FOREST_TYPE1_RIDGE_PIN_LOAD=1.
```

The guard requires the already exact facet module
`K11_FOREST_TYPE1_FACET_PIN_LOAD=1`, and therefore inherits its Type-I and
subcube prerequisites.  It allocates and emits nothing when absent or zero.

## Wiring

`TypeIFacetPinLoadPlan` now retains its existing exact literals

```text
facet_support[b][i]
  <-> [i in C4 and A[i] subseteq 63\{b}].
```

Retaining these variable references changes no variable or clause count.
For every `0<=b<c<6` and suffix position `1<=i<465`, the ridge plan defines

```text
z[b,c,i]
  <-> facet_support[b][i] AND !A[i,c] AND !rank4[i].
```

This is exactly the indicator that `i` lies in `C4` and its entry is a
proper subset of `63\{b,c}`.  Fifteen exact 464-input counters impose

```text
sum_i z[b,c,i] >= 10.
```

## Exact inventory

| component | variables | clauses |
|---|---:|---:|
| `15*464` exact three-input gates | 6,960 | 27,840 |
| fifteen exact 464-input counters | 13,800 | 96,600 |
| fifteen comparisons to 10 | 0 | 30 |
| **total** | **20,760** | **124,470** |

Every counter has 452 Wallace compressor adders and eight ripple adders.
Each full adder uses two variables and fourteen clauses and retains its final
carry.  Since `10=1010_2`, each first-difference comparison uses two clauses.

The current full Type-I build changes from

```text
3,648,797 variables / 20,036,415 clauses
```

to

```text
3,669,557 variables / 20,160,885 clauses.
```

The build-only audit reports exactly

```text
type1_ridge_pin_load_variables=20760
type1_ridge_pin_load_clauses=124470
type1_ridge_pin_load_gate_variables=6960
type1_ridge_pin_load_counter_variables=13800
type1_ridge_pin_load_gate_clauses=27840
type1_ridge_pin_load_counter_clauses=96600
type1_ridge_pin_load_comparator_clauses=30
INDEPENDENT_FNV64=3948591229824f06
ADD_CALLS=89023684
DECLARED=3669557
MAXVAR=3669557.
```

Absent and explicit-zero ridge guards have identical full clause-stream
fingerprints:

```text
INDEPENDENT_FNV64=b33abee6ccc470f4
ADD_CALLS=88484404
DECLARED=3648797
MAXVAR=3648797.
```

An attempted ridge guard without the facet guard exits with status two before
formula construction.

## Verification

The theorem, independent theorem audit, and source-aware checks are

```text
K11_TYPE1_BOUNDARY_RIDGE_PIN_LOAD.md
K11_TYPE1_BOUNDARY_RIDGE_PIN_LOAD_AUDIT.md
scratch/check_k11_type1_boundary_ridge_pin_load.py
scratch/check_k11_type1_ridge_pin_load_source.py
```

Both checkers pass.  The source compiles cleanly apart from the pre-existing
unused `BITS` warning under `-Wall -Wextra -Wpedantic` against the independent
CaDiCaL hash double.

Frozen local SHA-256 values are

```text
bb42caaee3c5adfc511ed8171a80944889020a4b0a3869069baeb90141034cc3
  k11_forest_sat.cpp
f0516ba8004b8b16b6d11520162bfb9711dd6c6e512b057c6168b721dc01877f
  scratch/check_k11_type1_ridge_pin_load_source.py
```

This is a satisfiability-preserving search reduction.  It proves neither
existence nor nonexistence of a 465-entry word.
