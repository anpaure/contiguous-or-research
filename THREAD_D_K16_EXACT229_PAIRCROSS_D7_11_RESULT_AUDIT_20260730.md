# Lane D: independent audit of the exact229 distance-7 pair-cross census

Date: 2026-07-30.

## Result

The completed one-process H100 bundle is authenticated as a scoped
`NO_PASS`:

```text
scratch/threadD_k16_exact229_hall_paircross_d7_11_20260730
```

No directed old-token cycle on two through eight positions, with every two
positions at linear distance at least seven, can supply the necessary 25 new
neighbours of the frozen exact229 Hall shore.  Pair interactions at distances
7 through 11 are included exactly.  This closes the interacting extension of
the prior separation-12 class; it does not close closer, larger-support,
multi-cycle, or non-token rethreads.

## Provenance

The staged input manifest verifies byte-for-byte:

- engine source SHA-256
  `4982cee3f006575cc6efce57a906efd7913586cbb7f92a48b19a84d577c407eb`;
- helper source SHA-256
  `eba32866ef0ab432b5bd1afc57a1be6cef66ea5bf0bea6d26bdbd2caa5c96b3c`;
- exact229 chronology SHA-256
  `cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974`;
- Hall audit SHA-256
  `85471243dcdd8a8ab6dc7530fc49b6629202b4403ad90a750961153afd0b1fb0`;
- production binary SHA-256
  `777cc1358ff6f730c2167fb14f6a5ad22ba2b17357628c6203a6c90357ae7c41`;
- final result SHA-256
  `dccac35377f1891d4ea656235f575facd150d772952ba2124e28195a99fdc930`.

`run.exit=0`, `run.status=COMPLETE`, and the staged-artifact manifest verifies
all twelve recorded output hashes.  Compilation produced empty stdout and
stderr.

## Checkpoint consistency

The arc checkpoint, pair-atlas checkpoint, and final result agree exactly on
the frozen scope, shore `212/187`, all 165,701,250 tested replacements, all
165,666 local-legal arcs, the full gain histogram, 64,320 interacting position
pairs, and 11,538,425 atlas entries.

The pair checkpoint and final result also agree exactly on the correction
atlas:

```text
kappa  -2       -1          0       +1
count  12       711    11,537,585    117
```

Thus all 11,538,425 entries are accounted for, exactly 840 are nonzero, and
the observed correction range `[-2,1]` fits the audited signed-byte encoding.
The atlas stayed far below its 250,000,000-entry guard.

The 4,681 positive arcs are byte-identical to the frozen corrected wide12
catalogue: SHA-256
`8d45283cf170713af419ed2cc86d206d32e5200c5098c64353633eea73486268`.
This independently ties the new run to the already authenticated local-arc
universe.

## DFS and pruning certificate

The completed DFS reports:

```text
nodes                         37,565,341
sound-bound prunes            33,025,594
reached closures                  19,558
score-qualified closures               0
maximum reached score                  6
```

An independent parser checked every closure row for root minimality, distinct
positions, support size 2 through 8, and pairwise separation at least seven.
Its score histogram is

```text
-3:5  -2:121  -1:688  0:16268  1:966
 2:911  3:483   4:91   5:12     6:13.
```

The support-size histogram is

```text
2:544  3:3744  4:13942  5:1315  6:13.
```

The maximum 6 is the maximum among **reached closures**, not a claimed maximum
over the branches cut by the bound.  Completeness instead uses the separately
audited upper bound

```text
s + r max(0,M1) + (7-a) max(0,M2).
```

Every pruned branch has this upper bound below 25.  Since each completed cycle
has at most seven interacting position pairs, the pruning is sound.  Therefore
the combination “all reached closures below 25 + every omitted branch bounded
below 25” proves the scoped no-pass.

## Independent literal closure replay

A separate atlas-free executable applied every one of the 19,558 logged token
cycles directly to the chronology.  For each closure it recomputed the frozen
shore indicator on the complete union of affected `[p-5,p+6]` cell-start
windows, and checked every affected flat edge, exact reconstruction row, and
possibly changed erosion envelope.  It found

```text
score mismatches             0
local geometry mismatches    0
maximum literal shore gain   6
```

The literal score histogram is identical to the parser histogram above.  This
audit deliberately did not rebuild the 11.5-million-entry pair atlas.

Audit source SHA-256:
`2b9a9ce874480592835e2957dd0ccbbdbae70beaa114e17ee79f3abaf476bba3`.
Remote audit binary SHA-256:
`7d9b2c0e356911e896113dd3fb5fabcec968c5bd29702e667ea6b9739b2b7b23`.
Literal audit JSON SHA-256:
`239ca016f4623002d98d1cf1b5e5d7601e173fa33c7e54dba3f040ac5d8eda78`.

The replay used one H100 CPU, a 512 MiB address-space cap, and no GPU.  It
finished RC0 in 2.42 seconds with maximum RSS 6,268 KiB.  Its local immutable
bundle is

```text
scratch/threadD_k16_exact229_hall_paircross_d7_11_20260730/
  independent_literal_replay/
```

## Independent audit artifacts

- Solver-free parser:
  `scratch/audit_threadD_k16_exact229_paircross_d7_11_result_20260730.py`,
  SHA-256
  `37e344e348852f2b5c9a0e2ed47af343e67444ba4216e04703ff9c7fc4539a62`.
- Uniquely named parser output:
  `threadD_paircross_d7_11_solverfree_independent.audit.json`, SHA-256
  `59ff14424692c96628f030114b78652a3fed8e72f010b34993067bffc89f075d`.
- Literal replay source:
  `scratch/audit_threadD_k16_exact229_paircross_closures_literal_20260730.cpp`.
- Uniquely named literal result:
  `independent_literal_closure_replay.audit.json` in the immutable replay
  subdirectory.

## Exact surviving gate

The no-pass applies only to one directed token cycle with at most eight support
positions and minimum separation seven.  The next Hall repair must therefore
use at least one excluded mechanism: positions within distance six, support at
least nine, several interacting token cycles, or a genuinely non-token
rethread/topology change.  Nothing here proves full generalized-Hall
infeasibility for exact229 outside that quantified class.
