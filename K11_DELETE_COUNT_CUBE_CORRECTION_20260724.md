# Correction and audit of deletion-count cubes

## Verdict

The first eight-block cube file and every result obtained from it are
**invalid**.  They constrained the wrong internal variables and provide no
evidence about the delete-five/append-sixteen neighborhood.

A corrected, independently audited cube partition now exists.  It is exact,
but representative corrected cubes are not fast: the eight-block base and
strengthened probes both remained unknown after 300 seconds, and a
representative sixteen-block probe remained unknown after 60 seconds.
Consequently no corrected exhaustive proof run has been started.

## 1. Fatal defect in the first partition

The invalid generator inferred that consecutive exact-count rows were spaced
by six variables.  The production CNF actually allocates, for each prefix
position,

```text
6 exact-count state variables + 5 sequential-AMO auxiliaries,
```

so the row stride is eleven.  For example, the state row after prefix
boundary 58 begins at variable 1093, not variable 808.  The old cubes
therefore fixed unrelated auxiliary/internal variables.

The invalid files are quarantined by

```text
scratch/k11_length476_five_deletion_span_20260724/cubes/
    INVALID_OLD_B8_RESULTS.md
```

No old exploratory status or partial DRAT ledger may be cited.

## 2. Explicit counter-row export

The production generator now exports every counter row explicitly as

```text
counter_vars POSITION STATE_0 STATE_1 ... STATE_5
```

Regenerating with this map-only change produced a CNF byte-identical to the
audited production formula:

```text
42d64edb00f1a8cb0367b3071b2bb6a8d1cdce75e1f09f9df34d509743d6334f
```

The explicit-row map has SHA-256

```text
da94199dc580e268aede15eb2ee674abd3e838c8bbc7927ed39b847f0239722e.
```

The independent checker

```text
scratch/audit_delete_counter_map_against_cnf.py
```

reads the exported variables and verifies every counter transition clause and
the final exact-count unit directly in the production DIMACS.  Without
assuming auxiliary variable numbers or a row stride, it also recovers and
checks every row's five-link sequential at-most-one chain from the binary
clauses.  It reports

```text
PASS positions=465 deletions=5 counter_rows=465 counter_variables=2790
     transition_clauses=5571 amo_auxiliaries=2325
     cnf_clauses=2196500
```

The counter itself is exact: the compile-time initial state is count zero;
the deletion literal forces the unique same-count or next-count successor;
each next row is at-most-one; and the final state-five unit forces exactly
five deletions.

## 3. Corrected exhaustive partitions

`make_delete_count_cubes.py` now refuses to infer row allocation and consumes
the explicit rows in the map.  The independent cube auditor reparses the map,
checks all 465 rows, checks the arithmetic allocation separately, verifies
every literal list, checks all cube pairs for an opposite literal, and checks
the combinatorial weight identity.

For eight blocks it reports

```text
PASS cubes=792 pairwise_disjoint=313236
     total_weight=177301977468 expected=177301977468
     counter_stride=11
     boundary_starts=[1093,1731,2369,3007,3645,4283,4921]
     small_assignments=4293
```

Thus the 792 cubes are pairwise disjoint and cover all
`binom(465,5)=177301977468` deletion sets.  The corrected file is

```text
02850c1944c2c9907d3f64de5ab601e0862ac20d3a4cccff7f9975413cb1f215
  delete_count_b8_v2.jsonl
```

The analogous sixteen-block partition has 15,504 cubes and the same exact
weight sum:

```text
dc4b57c78276bde6f9ba61f7fe51c6299336bd5c031617fd7fb322a7646227fc
  delete_count_b16_v2.jsonl
```

## 4. Corrected solver probes

The maximum-weight eight-block cube 76 has profile

```text
[0,0,0,1,1,1,1,1]
```

and represents 667,673,264 deletion sets.  With the corrected counter
literals:

```text
base direct-span CNF                         UNKNOWN at 300.01 s
rank-Hall/chain-partition strengthened CNF  UNKNOWN at 300.01 s
```

For the sixteen-block partition, a maximum-weight five-singleton profile
still represents 21,218,430 deletion sets.  Cube 76 remained unknown at 60
seconds in both the base and strengthened formulas.

These measurements show that count-profile cubing at eight or sixteen blocks
does not currently conquer representative branches.  They are timing data,
not SAT or UNSAT evidence.

## 5. Artifact hashes

```text
3184d3b70040e6b7c509f0606df32ac5997da2aac1f90f2babb89d53f420e8cb
  scratch/delete_append_span_cnf.cpp
a765fb70841f8a7e16863261e3e165107f32b5b74b5ffbda0cc90d7e1cedb84f
  scratch/audit_delete_counter_map_against_cnf.py
a7cf23d8046f5713c325b1878d6c1b6a6eaefe0a489fe1c0929c6a29aefb8a74
  scratch/make_delete_count_cubes.py
86f383eef931b4f9b5d4271d4388c1f0b1bedc684158f8be8e395c5a64b50844
  scratch/audit_delete_count_cubes.py
```

The corrected partition is a valid basis for deeper adaptive cubing, but no
finite neighborhood exclusion has yet been obtained from it.
