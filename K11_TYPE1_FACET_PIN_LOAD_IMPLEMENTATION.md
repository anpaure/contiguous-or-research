# Implementation: Type-I boundary-facet pin load

## Status

The independently audited six-facet theorem is implemented in
`k11_forest_sat.cpp` behind

```text
K11_FOREST_TYPE1_FACET_PIN_LOAD=1.
```

The guard requires both

```text
K11_FOREST_RANK_FILTRATION_TYPE1=1
K11_FOREST_SUBCUBE_DEFICIENCY=1.
```

It allocates and emits nothing when absent or explicitly zero.  No remote
solver was launched.

## Wiring

`SubcubeRunCreditPlan` now retains the already allocated exact support row
for the canonical endpoint six-set `T=63` in

```text
endpoint_support[position].
```

The assignment occurs at the point where the existing support gate is
created, so retaining the reference has zero CNF cost.

For each `b=0,...,5` and suffix position `i=1,...,464`, the new plan defines

```text
y[b,i] <-> endpoint_support[i] AND !A[i,b] AND !rank5[i].
```

The exact Type-I rank cap makes this precisely the indicator that position
`i` lies in the rank-at-most-four core and its entry is contained in the
facet `63\{b}`.  Six exact 464-input Wallace/ripple counters impose

```text
sum_i y[b,i] >= 20.
```

The plan reuses `SubcubeRunCreditPlan::one` and
`LocalDensityPBPlan::rank`; it creates no duplicate constant, rank, or
six-subcube support bank.

## Exact inventory

| component | variables | clauses |
|---|---:|---:|
| `6*464` exact three-input gates | 2,784 | 11,136 |
| six 464-input exact counters | 5,520 | 38,640 |
| six comparisons to 20 | 0 | 12 |
| **total** | **8,304** | **49,788** |

Each counter uses 452 Wallace compressor full adders and eight ripple full
adders.  Every full adder has two variables and fourteen clauses and retains
the final carry.  Since `20=10100_2`, the direct first-difference comparator
uses two clauses per counter.

The complete current Type-I/rank-seven portfolio has the build-only counts

```text
guard absent:  3,640,493 variables / 19,986,627 clauses,
guard enabled: 3,648,797 variables / 20,036,415 clauses.
```

The concurrently compressed canonical-prefix guard remains exactly

```text
type1_prefix_chain_clauses=32.
```

## Build and guard checks

The source compiles cleanly with `-Wall -Wextra -Wpedantic` against the
independent CaDiCaL audit double.  The full facet-enabled build reports

```text
type1_facet_pin_load_variables=8304
type1_facet_pin_load_clauses=49788
type1_facet_pin_load_gate_variables=2784
type1_facet_pin_load_counter_variables=5520
type1_facet_pin_load_gate_clauses=11136
type1_facet_pin_load_counter_clauses=38640
type1_facet_pin_load_comparator_clauses=12
INDEPENDENT_FNV64=b33abee6ccc470f4
ADD_CALLS=88484404
DECLARED=3648797
MAXVAR=3648797.
```

The absent and explicit-zero builds have byte-identical logs:

```text
INDEPENDENT_FNV64=337b2301854ddb4b
ADD_CALLS=88268704
DECLARED=3640493
MAXVAR=3640493.
```

Invalid uses without Type I or without the subcube plan both exit with status
2 before formula allocation.

## Source-aware verification

```text
python3 scratch/check_k11_type1_boundary_facet_pin_load.py
python3 scratch/check_k11_type1_facet_pin_load_source.py
```

The second checker inspects the actual production wiring, confirms that
`support_T` is retained rather than rebuilt, verifies conditional
construction/emission, checks that the compressed 32-clause prefix schema is
still present, exhausts the support gate and full-adder truth tables,
reconstructs the 452+8 counter inventory, and exhausts all 512 nine-bit
inputs to the `>=20` comparator.

Frozen hashes at this build are

```text
0d41fbd4cfe3ac075c850b0cfe41cea740608bfa953b53d7ffc40d2a1e3bd6d5
  k11_forest_sat.cpp
4f023c02b4a48893194cafc65d98608ddba79ed41c069d6f510c606ecace1fb1
  scratch/check_k11_type1_facet_pin_load_source.py
62711ef7008dd061c019833b2050446a32ea41f4e222dd6a2bb6c453f65682d8
  scratch/check_k11_type1_boundary_facet_pin_load.py
```

This module is a satisfiability-preserving search reduction.  It proves
neither existence nor nonexistence of a 465-entry word.
