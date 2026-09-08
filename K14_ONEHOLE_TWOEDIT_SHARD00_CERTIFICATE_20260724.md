# Certified `k=14` one-hole/two-edit shard 00 closure

Date: 2026-07-24

## Result

The first immutable shard of the one-hole/two-edit anchor-star portfolio is
certified UNSAT.  It contains 1,920 architectures: eight one-hole deletion
roots, each paired with all 240 second edit positions while suffix-root
position 3 is the common anchor.  Both replacement values range independently
over all 16,383 nonzero 14-bit masks.

Thus the certificate excludes exactly

```text
515,333,162,880
```

root/architecture/value tuples.  This is one local shard only and does not
change the certified bound `3434 <= nu(14) <= 3676`.

## Frozen formula

The exact provider formula was regenerated on Rose from the frozen inputs and
passed the independent clause-by-clause semantic auditor before solving:

```text
cases                         1,920
roots                             8
variables                    16,043
clauses                     191,871
unsafe target incidences      6,056
provider selectors           12,176
maximum unsafe/case                5
maximum providers/case            12
dead cases                         0
```

Hashes:

```text
4a2a107289feeffac3f9e2f2150896ff0f930210ba730cf606d66a6e74262790  shard00.cnf
5bfd2efba10ef63b62e93b8fc46462aba9e56d56fda4c98141ed9e5c0005691d  shard00.map
44d3904437f0a9edbbebba3d3828ab1edb07ef0f4aa3732048429070e4eeb5bb  shard00.stats
```

The remote generator binary had SHA-256
`67c0078036b58aa90b794efba2f8a4d58a5bd7e1276c487bf9f819cf232894ec`.
The generated outputs match the independent pre-launch reference hashes
exactly.

## Search and proof

A first no-proof CaDiCaL run returned exit 20 after 1.19 seconds.  This result
was treated as unchecked and had no mathematical status.  A fresh run with
seed 2400 then emitted a DRAT proof.  Independent `drat-trim` checking parsed
all 16,043 variables and 191,871 clauses and ended with

```text
s VERIFIED
```

Hashes:

```text
e85fc141a749524234d0807f1d49b8aeeecf19d81aba3736c561c5565411d2c1  shard00_seed2400.drat
717e5e5b80a0422bea568508fb39748d2b7d0af67ff58353edd27eae1cab5efb  shard00_seed2400.drat_trim.log
```

The frozen solver/checker binaries were:

```text
28ac31c3ded66d398692fd390086e5db669520bf31346a5b3780bf6ea67a1590  CaDiCaL
be9a20191731a6a6a82e509d959d5c5c9f69f1a92765bf3209685622c0384498  drat-trim
```

The complete local certificate bundle is
`scratch/k14_onehole_twoedit_shard00_certified_20260724/`.  Its manifest has
SHA-256

```text
88580a524b3289c4457c1df1f3f53ca62a353d596d7db8f54bfc77b77310500b
```

## Scope

This note records the checked proof for `shard_00.tsv`.  All other 25 shards
were subsequently DRAT-verified UNSAT as recorded in
`K14_ONEHOLE_TWOEDIT_FULL_PORTFOLIO_CERTIFICATE_20260724.md`.  The completed
portfolio still does not close arbitrary two-edit neighborhoods outside the
common-anchor family or the unrestricted 241-entry suffix problem.
