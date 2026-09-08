# R2 k=17 dirty-central compensated49 exact-q1 UNSAT/DRAT audit

Date: 2026-08-02

## Frozen statement

Let the source catalogue be the 49 rows of the authenticated anchored two-recut
table with central anchor `13..19` (seven compensators per anchor).  In every
row the central substitution is

```text
base 1834: cut 9924 -> cut (9912 + anchor),
```

the compensator is the row's advertised second substitution on a distinct
base, and all five source counters are zero.  For each of these 49 fixed banks:

1. literal reconstruction has exactly 3,805 base-distinct selected cuts and
   differs from the frozen round02 bank at exactly the two advertised bases;
2. the exact relaxed physical atlas has no lower-colour, tail-piece,
   head-piece, common-orientation, or rank10-provider zero row, and each of the
   three piece projections has matching size 7,612;
3. a fresh H100 `-O3` rebuild produces a CNF byte-identical to the promoted
   CNF; and
4. the CNF is UNSAT, witnessed by a retained proof accepted by `drat-trim`.

Thus the exact functional-q1 formula is infeasible for every bank in this
fixed 49-case catalogue.

## Independent replay

Unique H100 root:

```text
/home/amodo/or15/work/r2_k17_dirty_central49_proof_replay_20260802
```

The replay used four valid, prechecked-idle CPUs `20..23`.  It did not invoke
or inspect alternatives from the separate 5,054-survivor search.

The verifier independently joined the source rows to the promoted summary,
checked central provenance and unary dirtiness, reconstructed both cuts from
the complete candidate-to-base map, and then re-read the literal banks and
builder outputs.  It passed both the promoted and independently regenerated
catalogues.  Their identical local-audit payload has SHA-256
`fc9e8ae9fcd05e4758c124d7e6db15b3393ce4c43792811ff39026256392b3d9`.

Exact ranges over the 49 regenerated formulas are:

```text
relaxed atoms   228672 .. 228868
variables       891404 .. 892188
clauses         2416114 .. 2418270
```

All 49 solver exits are `20`, all 49 solver verdicts are `UNSATISFIABLE`, all
49 proof files are nonempty, all 49 checker outputs contain `s VERIFIED`, and
all 49 checker-error files are empty.  The complete 49-row result manifest is
[`summary.tsv`](scratch/r2_k17_dirty_central49_proof_replay_20260802/summary.tsv),
SHA-256
`d7956155b8bd27fada04b6e3165987fbd2a01084bda67e02d348687cc50b7fcb`.

The exact per-case bank, CNF, proof, checker-output, and checker-error hashes
are frozen in
[`proof_check_hashes.tsv`](scratch/r2_k17_dirty_central49_proof_replay_20260802/proof_check_hashes.tsv),
SHA-256
`3583a3627674452c4efcefc5c412804e189c4e30c61b369a53f4d4a68f57a646`.

The complete per-row artifact manifest has SHA-256
`8742572c6f76f4acd45a4f2f06a74c53773885134f999668aa69d696051749db`.
Its independent replay reports 637 `OK` entries; the replay log has SHA-256
`88d5b9fb03894c3227465eba4dd3778784cd6f180b9ed1d9031b863da5ae78c3`.
The 13-entry source/tool preflight also replays completely; its check log has
SHA-256
`a7ab0ca3c5f475c3e4b89c5d0ce0efa23ae59620e0ed48aa04ae856804fcc91f`.

An independently produced companion proof bundle has the same 49 CNF hashes.
Of the 49 retained proof hashes, 42 differ between the two proof-generation
runs and seven coincide; hence this replay is not merely a copy of the other
proof ledger.

## Authenticated inputs and executables

```text
factor                 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
round02 bank           48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649
candidate catalogue    fa1133f5ffc8b70bf7d1713dfa930670508fb6bb6e1255d570f00ea851d00cc6
anchored clean rows    9c4ecd1541a945bfae2be6d6534b28543a9c5c87745bdb8a47100dda274fb589
promoted summary       116418a461c110308fc105b959582c00a74338be2e45d0b804f02029c2b1b158
q1 exporter source     4e4440d87783a1cc24dfc786d4ae37c8eab46b86aba3d66629a30c31a0f0adba
exporter base source   28b2349ef9a0a7de8d5623e16ed5900b45f7852fe0b14ec5f779d94cf9778498
fresh exporter binary  76d16ba913e056a4a589a186e50f925207e13ee9edded0dafc539a530703cb60
fixed verifier source  4195cbd8d21bd4f899b1bead1787bdcd44283141f5b0282fbffc5d54bd4fd261
fixed verifier binary  dff94980e3aadbbe9b96928a425715daf01097eb11095ddec99dca26d897ef78
replay runner          8ae8e4dc3e3bf7985d81cf3aede01a46cdc9441874638dea055c4c9098b8ecd7
Kissat                  3ee4239c0bef4d237ab72827613426855b17c636d3b5843158fe5e549b175b0d
drat-trim               92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a
```

The theorem payload is
[`theorem.audit.json`](scratch/r2_k17_dirty_central49_proof_replay_20260802/theorem.audit.json),
SHA-256
`a467a96322e098c57c9e99b0b8e7c6ef27962ced34e77e28b82831bbe4c264e5`.

## Failed preflight retained but excluded

Before the certified run, an uncorrected draft used CPU indices `96..99` on a
host exposing only `0..63`.  Every attempted builder invocation failed at
`taskset` with `Invalid argument`; no CNF solve, proof, checker result, or
result row was produced.  Those files remain under `failed_cpu96_tests/` and
`failed_cpu96_results/` in the unique H100 root.  The certified runner was
patched to `20..23`; its outer stderr is empty.

## Exact scope

This is a complete no-go certificate only for the listed 49 compensated
dirty-central two-recut banks and their exact relaxed functional-q1 CNFs.  It
does not prove either unary dirty recut infeasible by itself, and it makes no
claim about any unlisted cut pair, selected rank10 coverage, ranks 11--13,
component topology, residence, exterior windows, the terminal compiler, or
the global contiguous-OR construction.

In particular, `zero_rank10=0` certifies nonempty local provider support; it is
not a selected rank10 transversal.
