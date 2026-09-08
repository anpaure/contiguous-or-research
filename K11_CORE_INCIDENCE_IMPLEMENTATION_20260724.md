# Exact implementation audit for the k=11 core-cell incidence cuts

## Scope

The frozen production source remains unchanged:

```text
/root/k11_onion_20260723/k11_forest_sat_newcuts.cpp
sha256 2ab8ce03f844884c1dc6c5b4f742fe6e447680589172610fcd9649906ebdc26c
```

The opt-in variant is

```text
scratch/k11_core_incidence/k11_forest_sat_corecuts.cpp
remote: /root/k11_core_incidence_20260724/k11_forest_sat_corecuts.cpp
sha256 02d2f1cf7089b10b529a0f66afb353638ec3946988038f77bf534850f5815c5d
```

It adds `K11_FOREST_CORE_CELL_INCIDENCE=1` and implements the proved rows

```text
Type I:
  S >= 649
  3*S-5*y1 >= 1938
  6*S+5*n5 >= 4254

Type II duplicate/one-core:
  S >= 649
  3*S-5*y1 >= 1938

Type II all corrected cases:
  6*S+5*n5 >= 4254+5*tight.
```

Here `S=n1+2*n2+3*n3+4*n4`.  Type-I `n5_count` is exposed from its
existing exact counter at zero inventory cost.  Type-II duplicate exposure is
enabled by `named_cell_hall || core_cell_incidence`; this avoids the audited
literal-zero guard hazard.

## Independent arithmetic inventory

The implementation matches the independently derived inventory in
`K11_CORE_INCIDENCE_CNF_PLAN_20260724.md` exactly:

| branch | new variables | new clauses |
|---|---:|---:|
| Type I | 4,057 | 28,395 |
| Type II | 4,057 | 28,405 |

Internal sub-ledger:

```text
exact rank counters:       3688 variables / 25816 clauses
retained-carry arithmetic:  354 variables /  2478 clauses
I2 comparator:               15 variables
all comparisons:                         101 clauses Type I
                                         111 clauses Type II
```

With the option absent, the copied source reproduces the frozen inventories
exactly:

```text
Type I  3,671,659 variables / 20,175,646 clauses
Type II 3,686,611 variables / 20,247,467 clauses
```

With the option present:

```text
Type I  3,675,716 variables / 20,204,041 clauses
Type II 3,690,668 variables / 20,275,872 clauses
```

## Immutable streamed CNFs

Both formulas were generated on RunPod Rose with the clause-streaming shim.
Token-level scans verified the header variable count, maximum used variable,
header clause count, and number of zero terminators.

```text
4b4c91b7b2fb801fc6b65329c6f94396d9199d6a6ff38666b74e252f7327ac68  k11_type1_corecuts.cnf
fface46a574c29b99425fc78725caa5535bcd740adba550391d85ba414885a1f  k11_type2_corecuts.cnf
```

Remote archival paths:

```text
/root/k11_core_incidence_20260724/k11_type1_corecuts.cnf
/root/k11_core_incidence_20260724/k11_type2_corecuts.cnf
```

The streamed generator binary has SHA-256

```text
a3a905a93e3a4f60ff421b9117418b9e2a9d76eea49e99cb2142a6930de9fb11
```

## First benchmark

The 12-minute-old external baseline Type-I Kissat seed 421 was stopped only
after confirming that it had no terminal result.  It was replaced, at the
same concurrency, by strengthened Type-I seed 431 under a hard 3 GiB virtual
memory cap.  Three older integrated Type-I searches remain live, so the
baseline branch still has three independent trajectories.

No SAT/UNSAT conclusion is claimed from build inventories or silent solver
execution.  A SAT model must pass both exact OR verifiers.  An UNSAT result
must be rerun with a proof artifact and independently checked.

## Automated terminal verification

The RunPod directory also contains a lightweight watcher.  It does not infer
anything from silence or process exit.  On an external `s SATISFIABLE` marker
it decodes variables `1..5115`, verifies all 2,047 nonzero masks directly,
and then runs the independent exhaustive and suffix-state C++ verifiers.  On
any UNSAT marker it records only `NEEDS_PROOF`.

```text
scratch/decode_verify_k11_kissat.py
remote SHA-256 d2b4ea7097045e63f50baaaacca30cf3109b3fc9083d9c235886316b2a67a113

scratch/watch_k11_exact_results.sh
remote SHA-256 bf8296a82b5a8beb1dd088f508042b29058e781c1875f3d1c048c4738adc0cef
```

The decoder was tested against a live nonterminal log and correctly rejected
it without creating a candidate.  The watcher also monitors all four frozen
integrated candidate paths and records integrated UNSAT only as a trigger for
a proof-producing rerun.
