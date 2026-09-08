# K16 upper12874: exact D4 delete-plus-two-substitution no-go

Date: 2026-07-31  
Lane: D  
Status: exact scoped theorem; all 191 rows independently composed  
Global bracket: `12873 <= nu(16) <= 12874` (unchanged)

## 1. Result

Let `U=answers/k16_upper12874.word`, of length 12,874 and SHA-256

```text
631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

Exactly 191 deletions of `U` leave at most four uncovered masks.  For every
one of these deletion words, replacing any two distinct surviving cells by
arbitrary nonzero 16-bit masks fails to produce a universal word.  The
authenticated delete-plus-one-substitution theorem covers either no-op, so
the same conclusion holds for at most two substitutions.

Equivalently, the complete radius-two ball above the 191 closest deletion
basins `D4` contains no length-12,873 solution.

The scope is deliberately local.  There are 12,683 other deletions, each
with at least five holes, and they are not covered.  Neither are reorderings,
insertions, three substitutions, another parent word, or arbitrary
length-12,873 words.  Thus the exact global bracket remains a gap of one.

## 2. Complete partition

For a fixed deletion basin and two changed cells, every final witness of an
original deletion hole meets at least one changed cell.  Hence every proposed
completion belongs to the union of:

1. **all-joint:** every original hole has a final witness containing both
   changed cells;
2. **provider-first:** one changed cell, applied alone, supplies at least one
   original hole.

The frozen all-joint theorem exhausts branch 1 for all 12,874 deletions.  The
provider-first engine exhausts branch 2.  It enumerates every partial first
provider, materializes its exact ejection debts, computes the full set of
targets whose every intermediate witness crosses each prospective second
site, and tests the maximal intersection value `J` (or its coatoms when `J`
is the incumbent).  The suffix/prefix banks are built in the first-edited
word, so both-edit intervals use the literal `x OR y` cross term.

The second-site seed reduction is exact: a second value is a submask of the
intersection of all intermediate holes, so the bits of a chosen seed hole
outside that intersection must occur in its compatible context.  A first
edit can change this predicate only in the old/new compatible components
incident with that edit and their adjacent separators; these sites are added
explicitly.  The independent proof is frozen in
`THREAD_D_AUDIT_K16_PROVIDER_FIRST_SEEDED_POSITION_AND_MAXIMAL_VALUE_20260731.md`.

The seven one-, two-, or three-hole rows `D3` were already closed exactly.
The new run covers precisely the remaining 184 four-hole rows `E4`.  No D3
row was recomputed in the full E4 campaign.

## 3. Exact E4 census

A deterministic 12-row stratified pilot was terminal throughout, with mean
1.65 seconds and maximum 3.17 seconds.  The projected workload was below the
declared cap, so the remaining rows ran sequentially on one low-priority
H100 CPU.  Every one of the 184 rows returned
`PASS_EXHAUSTED_NO_COMPLETION`; no timeout, signal, resource failure, or
candidate occurred.

```text
E4 deletion rows                         184
first-provider records            21,756,304
source seed-position visits      656,144,899
affected-component additions      53,574,707
exact candidate second sites         147,575
nonzero full target cores             145,468
maximal-value tests                    119,866
coatom considerations                  120,814
literal through-chain tests                 19
positive full replays                        0
aggregate engine wall seconds          272.34028
maximum single-row wall seconds           3.16822
maximum RSS KiB                           13,312
```

`full replays=0` means no row passed the exact demanded-target through-chain
condition; it is not an unverified positive.  Had any row passed, the engine
would have materialized it and replayed all 65,535 targets before writing a
candidate.

## 4. Independent composition

The fail-closed composer:

1. authenticates the source, 191-row ledger, O3 engine, and embedded exact
   interval engine;
2. reconstructs all 191 deletions from the source and independently
   recomputes their complete interval-OR hole sets;
3. verifies that the new result IDs are exactly the 184 `E4` rows, every exit
   code is the terminal negative code, and every engine audit claims all
   12,873 first positions;
4. checks the post-run basin serialization hashes, per-row resource ledgers,
   absence of solution files, and exact expected holes;
5. authenticates the seven-row composed D3 theorem, the global all-joint
   theorem, and the all-deletion delete-plus-one theorem.

It returns

```text
PASS_EXACT_D4_DELETE_TWO_SUBSTITUTION_NO_COMPLETION
payload 199f63b9e4bf4d98f2e546021b9ed0e2f76c51e498848cd04abe15c9ea311181.
```

This proves Section 1 by the provider/all-joint dichotomy.  No SAT or
probabilistic inference is involved.

## 5. Artifacts

```text
MATH_THEOREM_K16_UPPER12874_D3_DELETE_TWO_SUBSTITUTION_NOGO_20260731.md
  SHA-256 5c66c0259bad16778c86aaf12e91c5191fcc99fd2d54d83e8ebe41d76b964dc6

THREAD_D_AUDIT_K16_UPPER12874_D4_PROVIDER_CORE_EXTENSION_AND_BENCHMARK_20260731.md
  SHA-256 5e972472d54e313c754990d6298ad9bb8f3dd5b572699a897b078c38cc0740cc

scratch/threadD_search_k16_upper12874_d4_provider_core_20260731.cpp
  SHA-256 83a65fc1df68bc7fa3cc1808f30975956b31c39d1d6adcc4e9c04f6a9dba694a

scratch/threadD_materialize_k16_upper12874_d4_basins_20260731.py
  SHA-256 c2d3d23d1c8e05592946b0688faf18620525d223484148000829e4f82c0c18e3

scratch/threadD_run_k16_upper12874_d4_provider_core_h100_20260731.sh
  SHA-256 6b4d9a5a27636e2dfa8d54f3afebf3ef8e49d0298511c8596d8363235f0ab7de

scratch/threadD_audit_k16_upper12874_d4_radius2_20260731.py
  SHA-256 6ab0b31dc5479c078d0b72d81918d13ac77e9e05a80b778b600e922a1a2dd491

scratch/threadD_k16_upper12874_d4_radius2_20260731/independent.audit.json
  SHA-256 21b13c3907d994e58ca97f3f8fce4bdd9f181d3aa90943c854de9d31eb55718e
  payload 199f63b9e4bf4d98f2e546021b9ed0e2f76c51e498848cd04abe15c9ea311181

scratch/threadD_k16_upper12874_d4_radius2_20260731/results_full/output.sha256
  SHA-256 6dcdf50c7fe1b9485fc781dc46e82cb09225f6f40544b4e28d3471e71a205a63

scratch/k16_upper12874_delete_two_sub_alljoint_global_exact_20260730.independent.audit.json
  SHA-256 e0303b3bef80d14e9bde85863347b6c78947b212eb159bac77cac005bb29bcd0

scratch/k16_upper12874_delete_sub1_all12874_20260730.audit.json
  SHA-256 37a639798cacebd7c10dee0d529ecc9535d3a936daa1b82d16884da691894d1e
```
