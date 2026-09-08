# AD audit: exact K16 H1 joint13 composed-CNF seed-1731 run

Date: 2026-07-30

## Verdict

**UNKNOWN, with exact scope and provenance frozen.**  The authenticated
469-variable / 28,233-clause composed CNF was run once with proof-retaining
Kissat 4.0.4 on H100 CPU 56.  Kissat reached its 1,790-second internal time
limit and returned exit code zero with

```text
s UNKNOWN
```

No satisfying assignment was emitted.  The 2,135,342,143-byte binary DRAT
stream is only a partial stream and is not an UNSAT certificate.  Therefore
no decoder was invoked, no length-12,873 word was materialized, and no claim
of infeasibility is made.

The exact run audit is

```text
scratch/ad_k16_h1_joint13_f03c8c3e_seed1731_h100_20260730/run.audit.json
SHA-256 4be2122366e6002c624b3d1ddcd00ba6aba252580709f83d43a18be6bfa17199
```

## Frozen model and maps

The run used exactly:

| artifact | SHA-256 |
|---|---|
| composed CNF | `f03c8c3e38caf4d4f47bb7ae4569e07526afdd7689acc2c1b32b8dfd71ab488e` |
| composed map | `f5f50ec0563adb1175500ef1426144f753dd72ed37f360f787ebb840feeb5ed8` |
| map payload | `7ff2f7a17a45b40360b7e29a004365b7f7031b169188cb58e85ddf2d1e6c8698` |
| source word | `ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a` |
| composed decoder | `cbb9e235d8e71b144caf3e69f659f40f3f3651b107366f652a342d35ef88ffe4` |
| independent model audit | `331f1d7d56c18c6c639c8abf27b9e177c692a012b9a20e6878b4397efb025c76` |
| independent-audit payload | `72be9126c4233d3d18c3008a2751774c52db46410c9ba2aa599d2a6658b774f1` |

Independent parsing gives 469 variables, 28,233 clauses, 174,662 literals,
maximum variable 469, and no empty clause.  The exact equisatisfiability
scope remains the frozen thirteen editable cells with arbitrary nonzero
reassignment and all other cells fixed.  It is not a global length-12,873
model.

## Command and resource caps

The unique remote directory is

```text
/home/amodo/or15/work/ad_h1_joint13_f03c8c3e_20260730_0602z
```

The solver binary is Kissat 4.0.4, SHA-256
`3ee4239c0bef4d237ab72827613426855b17c636d3b5843158fe5e549b175b0d`.
The executed solver command was

```bash
/usr/bin/time -v \
timeout --signal=TERM --kill-after=30s 1800s \
prlimit --as=8589934592 -- \
taskset -c 56 nice -n 15 \
/home/amodo/or15/kissat/build/kissat \
  --seed=1731 --time=1790 --flushproof=true \
  model.cnf proof.dratb
```

The audited wrapper has SHA-256
`fd32a2e366017754f7135a724890c9b776a3910241848ea1663f592a1acb8ba7`.
It ran from `2026-07-30T06:04:46+00:00` through
`2026-07-30T06:34:36+00:00`.  `/usr/bin/time` recorded:

```text
wall                     29:50.01
user seconds             1671.27
system seconds             68.46
CPU                         97%
maximum RSS              93068 KiB
swaps                         0
```

The process was the only solver launched by this lane.  A process audit
found no other solver pinned to CPU 56 before launch.  For provenance
hygiene, the retained one-second `mpstat` sample immediately before launch
did show 100% user activity from migratory background work; thus “idle core”
is not asserted.  The actual capped solve nevertheless received 97% CPU.

## Output and certificate classification

The copied transcript and resource log have hashes

```text
solve.out          fa5f8cddad0e5f4e0baaddb1f00415d17db3045cf3d93650981ab59b06417388
solve.resource.log 886dc8edafc53ace40d05425d9957dc5400f222a8563441964f70d8e13439e99
```

The retained remote partial proof has

```text
bytes    2135342143
SHA-256 8d4dbb191e0552147581ac07f6d588108656d9391f406504d4856945b00ddd91
```

It was intentionally not passed to `drat-trim`: a proof stream produced by
an UNKNOWN run is not a certificate.  Likewise, the SAT decoder is
fail-closed on an explicit `s SATISFIABLE` marker and all 469 variables, so
it was correctly not invoked.  `answers/k16_upper12873.word` remains absent.

## Exact fallback prepared without a duplicate solve

Independently of the run, the known explicit-witness near phase was mapped
through the proxy/supply composition.  Its 120 true chart choices become
120 true compact code bits and 65 true supply flags.  The resulting total
compact phase has 185 true variables and exactly one false composed row,
base clause 8,836:

```text
(81 OR -82 OR 83 OR 84 OR 85 OR 301).
```

Conditioning on the 29 possible hole-witness codes, performing full unit
closure, densely renumbering, and tailoring polarity gives an exhaustive,
pairwise-disjoint 29-slice decomposition.  The slices have 432--453
variables and 21,278--26,914 clauses.  H-witnesses 4, 5, and 14 have one
residual phase defect; H-witness 2 exposes the three known bit-11 blocker
rows.  Clause-for-clause independent reconstruction passed.

The fallback artifacts are:

| artifact | SHA-256 |
|---|---|
| theorem/audit note | `b0dca94ca9443b73ee1dd0410a56f0fc5254d258db01b31b1f7199cb55c8cbfa` |
| 29-slice map | `8aaefe02f75f6f249d7dbf907d6a7ff9ad24f23b56b66f4be4bfc474634493e0` |
| independent audit | `987641279f1186ce3f53f14d320b1f86257facbeab8b9b9ed5e337fa95b0601f` |
| unlaunched fallback runbook | `f01c5b9d7341c38729620940133901d93e92b1b6ccd29084d8f69a5d4377f959` |

This is an exact decomposition, not a solution.  Every slice not closed by
a satisfying assignment or independently verified UNSAT proof remains
UNKNOWN; a no-go for all 29 slices would still be scoped only to the frozen
joint13 fibre.

## Coordinated four-branch observation

No duplicate branch was launched by this lane.  A separately authorized
portfolio ran four disjoint conditioned branches from an independently built
29-way package.  Read-only replay of its terminal files gave:

| branch | conditioned-CNF SHA-256 | terminal status |
|---|---|---|
| H02 | `809675ec3cff07c13d744047d29d471647c97e1ab7e683a34db67fa306851fe4` | `s UNKNOWN`, exit 0 |
| H04 | `9053597d0d970284651041998f1bb27ee204328d23f2750ac112b1e37c5ef337` | solver UNSAT; DRAT checker exit 0 and `s VERIFIED` |
| H05 | `bf6dc27dd89d3f035901617b7d6f5babea0235a290364afa527f783605c1761e` | solver UNSAT; DRAT checker exit 0 and `s VERIFIED` |
| H14 | `faac20daddcb733495015da6154640a7968a58f8b0dfdec8e2b84a8e7f815a51` | solver UNSAT; DRAT checker exit 0 and `s VERIFIED` |

The proof hashes are respectively

```text
H04 c0eaff9af15ff1bd6b95464b1e7f729866bd5009a4627071813fe41799c89223
H05 58dff95a03c110aad9d2a883c4cf7e0c6f6fa4e4310af9c373e75ec6f392da6c
H14 043c404661b4aedfe280a6788058224fe552613ff07cd9b35c410b869db33471
```

This closes those three conditioned CNFs only.  H02 remains UNKNOWN, and
the other 25 branches were not part of that portfolio.  Hence this
coordinated observation does not change the UNKNOWN status of the full CNF.

## Sharp boundary

Proved and audited:

1. the exact composed CNF, maps, source, decoder, and solver binary used in
   the run have the hashes above;
2. the single 1,790-second solver run ended UNKNOWN within the stated caps;
3. its partial proof is non-certifying and no answer word was produced; and
4. the 29-way conditioned decomposition is exhaustive and equisatisfiable
   with the original composed CNF when all branches are taken together.

Not proved:

1. SAT or UNSAT of the 469-variable CNF;
2. feasibility or infeasibility of the thirteen-cell fibre; or
3. existence or nonexistence of a universal word of length 12,873.
