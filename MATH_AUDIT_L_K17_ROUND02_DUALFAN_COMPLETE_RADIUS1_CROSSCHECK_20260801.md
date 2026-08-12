# Independent audit: `k=17` round-02 dual-fan complete single-recut closure

Date: 2026-08-01  
Status: **PASS**, with the conjunctive scope stated below.  This audit checks
the enumeration partition, the exceptional central recuts, the physical
dual-fan persistence argument, and both DRAT-verification bundles for

```text
MATH_THEOREM_L_K17_ROUND02_DUALFAN_COMPLETE_SINGLE_RECUT_NOGO_20260801.md
  SHA-256 a2c4a8dbf45b57b01517071c8fed6d679b97eef9120fe2a3bbc6fe039d883fcd
```

## 1. Exact scope

The audited conclusion is

> No bank obtained from the frozen `round02` bank by replacing exactly one
> selected extra cut by another eligible cut in the same base piece both
> preserves every zero-265 row and admits the exact orientation-coupled q1
> coloured cycle cover.

The socket scanner evaluates the physical fan only after the candidate has
passed the zero-265 score.  Therefore this is not an unconditional statement
that q1 alone is UNSAT for every recut after dropping the lower, endpoint,
common-orientation, or rank-ten guards.  It also does not cover an added cut,
a cut deletion plus a cut elsewhere, two simultaneous replacements,
alternative base cuts, or a non-cut circuit.

## 2. Exhaustive partition

The scanner loops over every currently selected split base and every other
eligible gap in that same base exactly once.  Its literal reconstruction and
score give

```text
all same-base one-recut candidates       16667
zero-265 failures                         3624
zero-265-clean candidates                13043
```

The clean set has the disjoint partition

```text
noncentral, dual fan unchanged           13030
noncentral physical socket escapes          12
central 1834:9924->9923, fan unchanged       1
                                           -----
                                           13043
```

The nine central alternatives split as follows:

* `1834:9924->9923` is the sole zero-265-clean recut;
* `1834:9924->9925,...,9931` each have a zero lower colour;
* `1835:9933->9932` has one zero tail state, one zero head state and one
  common-orientation-zero piece (rank-ten zero remains zero).

These identities are frozen in

```text
scratch/k17_round02_dualfan_radius1_20260801/independent_partition.audit.tsv
  SHA-256 b92561c3d9317becd4ffc3d2e9216fbb715c4771dc376c85d005c530c617d107
scratch/k17_round02_core_piece_recuts_20260801.tsv
  SHA-256 19164c31bb4a65f5cbe06a872eec9ca2e6def3655fea5ef26c30194cdb73744d
scratch/k17_round02_dualfan_radius1_20260801/summary.tsv
  SHA-256 a5a5685ba78d6a979ea667447fba7165a61a84b589ebe6f370c6f579883332de
```

## 3. Physical socket completeness

For a noncentral recut the physical states at pieces 3669 and 3670 are
unchanged.  The scanner reconstructs all occurrence-labelled states, all
selected lower colours, every Johnson-neighbour head/tail occurrence, and
the literal relaxed residence predicate.  It separately counts

1. a colour-`114930` seam shared by the two forced sockets; and
2. a non-`114930` outgoing or incoming arm at either socket.

Among all zero-265-clean recuts it finds no shared core seam and exactly 12
noncentral arm escapes.  Every one of the other 13,030 clean noncentral
recuts therefore leaves the two-socket/one-colour inequality

\[
             |\{L(3669),L(3670)\}|=2>|\{114930\}|=1
\]

literally unchanged.

The only clean central recut, `9924->9923`, was checked separately from its
emitted seam table.  Both forced outgoing/incoming role sets contain only
lower mask `114930`, and there is no shared seam between the two pieces.
Thus the same combinatorial dual-fan proof persists; its solver proof is
redundant confirmation.

The 12 escape rows are frozen at

```text
scratch/k17_round02_dualfan_radius1_20260801/socket_escape.tsv
  SHA-256 706405a8331cb6ec21e56de4d8c4be728a0a72a3acb685d57195dee39979c27d
```

Their first three columns agree exactly with the independently generated
Lane-L table of SHA-256
`88893f08ea810662df0ef44be9d227ad53ff19485f27034d8827c6083f6b29ef`.

## 4. Exact q1 proof checks

All 12 noncentral escape CNFs are UNSAT.  The verifier requires Kissat exit
20 and `UNSATISFIABLE`, checks the emitted proof with `drat-trim`, requires
the literal line `s VERIFIED`, and records the CNF/proof hashes.  The frozen
summary is

```text
scratch/k17_round02_dualfan_radius1_20260801/drat_summary.tsv
  SHA-256 39a4f41f4d2ecae4ad6273f86eed6de92d95dc6639e0f0355738265f3368f9c0
```

Both emitted central formulas were independently rechecked on H100 CPU by

```text
scratch/verify_k17_round02_core_piece_q1_unsat_20260801.sh
  SHA-256 221fd9b41197e81a35af67a9b064ccaa691dca16c59cc9c92eae7149ee41973d
```

The resulting manifest is byte-identical to the pre-existing one:

```text
scratch/k17_round02_dualfan_radius1_20260801/core_piece_drat_summary.tsv
  SHA-256 e2ec901aa6afff7a5d64023f3400ae8c361a12798faf9f1b5b32bebf2a7740ce
```

It records:

```text
9924->9923: CNF 4e04b161... proof f351fe1a... VERIFIED
9933->9932: CNF 39526bf7... proof b69c393b... VERIFIED
```

The latter formula is stronger than needed for the theorem because that
recut already fails the common-orientation row.

## 5. Reproducer audit

The noncentral runner and verifier have SHA-256 values

```text
scratch/run_k17_round02_socket_escape_exact_q1_20260801.sh
  22a411450f7126f8840fd12dfefd7d612aadc891eec2223e4f04b0ccf1443ef5
scratch/verify_k17_round02_socket_escape_q1_unsat_20260801.sh
  e931444cbf101bb065fea32292de879a6f2abcf4c56da387dd3520656f4c6691
```

The runner identifies the replaced row by its old cut value rather than by
the base id.  This is sound for the frozen input because every selected old
cut in `round02.bank.tsv` occurs exactly once.  It is not a generic-safe
interface without that uniqueness precondition.

## 6. Consequence

Within the frozen one-split-per-base, fixed-cardinality face, cut-choice
Hamming distance at least two is necessary.  The smallest live extension is
a coupled two-replacement move (in particular, an `s` arm and a `t` arm
whose new colours/outside sockets are compatible, or a two-change direct
seam activation), followed by the complete q1 formula.  The audit does not
claim that two replacements suffice.

A subsequent exact pair audit closes all 65 compatible unordered pairs of
the 12 visible one-arm escapes.  Consequently the useful Hamming-two master
must not be restricted to their Cartesian product.  It must retain at least
one of the genuinely joint branches: a central-base role recut, dirty-single
compensation, or a seam whose geometry is exposed by one recut while its
lower colour is introduced by the other.  This is the minimal non-single-cut
handoff; feasibility is still open.

Ranks 11--17, exact product residence, component joining, selected rank-ten
provider packing, and the terminal compiler remain downstream even after a
q1-feasible bank is found.
