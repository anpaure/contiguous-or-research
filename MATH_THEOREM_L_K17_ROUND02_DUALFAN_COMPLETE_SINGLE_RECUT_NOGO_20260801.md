# `k=17`: complete zero-265-preserving single-recut no-go at the round-02 q1 dual fan

Date: 2026-08-01  
Status: exact scoped theorem.  It exhausts every one-for-one alternative
extra-cut replacement around one authenticated 7,612-piece bank, with
literal rebuilding, a complete physical-socket escape census, literal replay
of all nine central recuts, and exact q1 replay of every local escape and the
two CNF-emittable central recuts.  Independently checked DRAT proofs cover all
12 noncentral socket escapes and both emitted central formulas.  It is
not a no-go for two simultaneous replacements, an added pure-refinement cut,
another minimum base cut family, a circuit rethread, or `nu(17)=24313`.

## 1. Frozen face

The input is the CEGAR `round02` cut bank

```text
scratch/l_k17_dense_q1_cegar_20260801/round02.bank.tsv
  SHA-256 48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649
```

on the authenticated protected seven-component factor.  It selects 3,805
extra cuts, at most one in each currently split deterministic
anchor/rightmost-greedy base piece, and reconstructs 7,612 physical pieces
and 7,612 deleted rank-eight colours.

The literal necessary-residence atlas is

```text
RELAXED triples=228836 zero_colours=0 colour_degree=2:14
    zero_tail_states=0 zero_head_states=0
    zero_tail_pieces=0 zero_head_pieces=0
    match_piece_TH=7612 match_piece_TC=7612 match_piece_CH=7612
COMMON_ORIENTATION_ZERO relaxed=0
RANK10_ZERO relaxed=0
```

Thus every one of the 265 old singleton tasks remains closed and all three
physical two-shore projections are perfect.  This is still only the relaxed
two-block residence projection.

The orientation-coupled q1 formula has

\[
  892058\text{ variables},\qquad
  2417916\text{ clauses},\qquad
  228836\text{ physical seam variables}.
\]

It is UNSAT.  The independently checked proof has a 139-clause original
core, 45 core lemmas and 1,851 resolution steps.

## 2. Physical dual fan

Put

\[
 q=114930.
\]

The two forced physical sockets are

```text
s = 115442 = q + {9}, piece 3669,
t = 115186 = q + {8}, piece 3670.
```

They are the old outer sockets of base-piece children.  Their direct Johnson
seam has union `115698`, but is absent because one endpoint coordinate has
age sum

\[
                       2+1=3<4.                 \tag{2.1}
\]

In the literal atlas, orientation 0 of either piece has only colour-`q`
outgoing seams at this socket, while orientation 1 has only colour-`q`
incoming seams there.  Consequently each physical piece consumes one
colour-`q` seam in either orientation.  No colour-`q` seam joins the two
forced sockets, so the two consumptions are distinct.  The colour capacity
is one.  Hence

\[
                   |\{s,t\}|=2>|\{q\}|=1,       \tag{2.2}
\]

which is the dual-fan obstruction.

For this fixed pair, a one-replacement child can destroy the literal proof
only in one of the following ways:

1. create a resident colour-`q` seam directly joining `s` and `t`;
2. create a non-`q` seam in the forced outgoing/incoming role at `s` or `t`;
3. relocate a forced socket role.

Every replacement outside central bases 1834 and 1835 preserves the two old
outer socket identities and their roles.  Thus for a noncentral replacement
the exact test is the first two rows.  If neither occurs and the zero-265
ledger remains closed, each piece is still forced to a distinct colour-`q`
seam, so (2.2) remains a literal UNSAT certificate.  A recut inside base
1834 or 1835 can change the physical state occupying the named piece index;
those nine recuts are therefore handled separately by literal rebuild in
Section 4 and are not discharged by this persistence sentence.

## 3. Complete one-replacement census

There are exactly 16,667 alternative replacements of one currently selected
extra cut by another eligible gap in the same base piece.  Every candidate
is rebuilt literally; no prospective unary support is used.

The exact partition is:

```text
all one-replacement candidates                         16667
preserve zero lower/out/in/common-orientation/rank10   13043
create a shared colour-114930 seam                         0
create a non-114930 seam at s or t                        12
```

The 12 socket escapes are:

| base piece | old cut | new cut | socket | new directed atoms |
|---:|---:|---:|:---:|---:|
| 540 | 2838 | 2842 | `t` | 8 each direction |
| 3680 | 19815 | 19818 | `t` | 6 |
| 1284 | 6831 | 6832 | `s` | 5 |
| 3613 | 19443 | 19445 | `t` | 5 |
| 1379 | 7364 | 7380 | `t` | 4 |
| 1801 | 9773 | 9771 | `s` | 4 |
| 3254 | 17426 | 17428 | `t` | 4 |
| 1532 | 8180 | 8181 | `s` | 3 |
| 2251 | 12065 | 12067 | `t` | 2 |
| 3029 | 16232 | 16234 | `s` | 2 |
| 3344 | 17953 | 17957 | `t` | 2 |
| 2251 | 12065 | 12066 | `s` | 1 |

The directed counts agree by socket reversal, as required by the symmetric
socket criterion.  The complete table is frozen at

```text
scratch/l_k17_dense_q1_cegar_20260801/round02.socket_escape_v2.tsv
  SHA-256 88893f08ea810662df0ef44be9d227ad53ff19485f27034d8827c6083f6b29ef
```

Of the other 13,031 zero-265-preserving replacements, 13,030 are noncentral
and retain the dual fan (2.2) verbatim.  The remaining one is the central
recut `1834:9924->9923`; its complete q1 formula is treated in Section 4.
The seven other recuts of base 1834 have one lower-colour zero.  The recut
`1835:9933->9932` has one tail-state zero, one head-state zero and one
common-orientation zero.  It therefore lies among the 3,624 replacements
which fail an earlier zero-265 row, although its q1 CNF was also emitted and
checked for the central-piece exhaustion.

## 4. Exact q1 replay of every nonpersistent case

For each of the 12 exceptional banks, the full literal relaxed atlas and the
complete orientation/tail/head/colour CNF were rebuilt.  Kissat returns
`UNSATISFIABLE` for all 12.  A fresh text proof for every formula was checked
by `drat-trim`; all 12 end in `s VERIFIED`.

The result list is

```text
scratch/l_k17_dense_q1_cegar_20260801/summary.tsv
  SHA-256 9e80b335755f7abe60a69420147717a3c1aed64b8dc8f0a4689bdb71f2023464
```

and the bank/CNF/proof/check hashes are frozen together in

```text
scratch/l_k17_dense_q1_cegar_20260801/proof_manifest.tsv
  SHA-256 95150d58c3cb0782468bd1572ca8e34c117de7e70c7c80200cc3719c8321dbff
```

The full CNFs and proofs remain under

```text
/home/amodo/or15/work/laneL_k17_dense_persistent265_20260801/cegar/dualfan
```

The nine possible recuts of the two central bases are a logically separate
case because the old socket-persistence argument does not apply to them.
Their exhaustive result is

```text
base 1834, current cut 9924:
  cut 9923                         q1 UNSATISFIABLE
  cuts 9925,9926,9927,9928,
       9929,9930,9931              fail an earlier literal local row
base 1835, current cut 9933:
  cut 9932                         fails the common-orientation row;
                                   its emitted q1 CNF is also UNSATISFIABLE
```

The `9924->9923` atlas is zero-265-clean.  Its literal seam table has only
lower mask `114930` in the forced outgoing/incoming roles of pieces 3669 and
3670 and has no seam joining the two sockets, so the same dual-fan proof
(2.2) persists independently of its checked DRAT refutation.  In contrast,
`9933->9932` has one zero tail state, one zero head state and one
common-orientation-zero piece, so it already fails item 1 of Theorem 5.1.

The two emitted CNFs have SHA-256 values
`4e04b16156110c003880d657fab34ba166420c6061e0cb7407a9860b121e1740`
and `39526bf7edc3a533494437e6fb430078e1e5a2b8b98a2ec3ab4889ccc100ffae`,
respectively.  This central table is frozen at

```text
scratch/k17_round02_dualfan_radius1_20260801/summary.tsv
  SHA-256 a5a5685ba78d6a979ea667447fba7165a61a84b589ebe6f370c6f579883332de
scratch/k17_round02_core_piece_recuts_20260801.tsv
  SHA-256 19164c31bb4a65f5cbe06a872eec9ca2e6def3655fea5ef26c30194cdb73744d
scratch/k17_round02_dualfan_radius1_20260801/core_piece_drat_summary.tsv
  SHA-256 e2ec901aa6afff7a5d64023f3400ae8c361a12798faf9f1b5b32bebf2a7740ce
```

The 12 socket-escape proof checks are independently summarized at

```text
scratch/k17_round02_dualfan_radius1_20260801/drat_summary.tsv
  SHA-256 39a4f41f4d2ecae4ad6273f86eed6de92d95dc6639e0f0355738265f3368f9c0
```

## 5. The scoped theorem

### Theorem 5.1 (complete single-recut no-go)

No bank obtained from the frozen `round02` bank by replacing exactly one of
its 3,805 selected extra cuts by another eligible cut in the same base piece
simultaneously has

1. zero relaxed lower-colour, physical endpoint and common-orientation rows;
2. zero relaxed rank-ten provider rows; and
3. an orientation-consistent q1 coloured cycle cover.

#### Proof

The literal census partitions all 16,667 replacements.  A candidate outside
the 13,043-row preserving set fails item 1 or 2.  Within the preserving set,
13,030 noncentral candidates create neither a direct shared colour-`q` seam
nor a non-`q` arm at either forced socket; their central states are unchanged,
so the dual-fan proof (2.2) persists and item 3 fails.  The 12 noncentral
exceptions are exactly the socket-escape table in Section 3, and their
complete q1 formulas are all DRAT-verified UNSAT.  The only remaining
preserving case is the central recut `9924->9923`, whose complete q1 formula
is also UNSAT.  The other eight central recuts fail the zero-265 ledger;
seven have a lower-colour zero, while `9933->9932` has a
common-orientation zero (and is separately q1-UNSAT).  These cases are
exhaustive.  \(\square\)

## 6. Minimal next face

Within the fixed 7,612-piece, one-split-per-base replacement face, any
successful continuation has Hamming distance at least two from `round02`.
The smallest literal next master is therefore a **coupled two-replacement**
model.  Its local priority rows are:

* a geometry-mover recut paired with a different recut which selects the
  new seam's lower colour, even when neither singleton has that seam;
* one visible socket escape plus a neutral global blocker rerouter;
* a central-role change or a pair which jointly repairs a singleton local
  zero; and
* followed by the complete q1 formula, not merely the local rank-two test.

This lower bound does not say that two replacements suffice.  A single
*added* pure-refinement cut also leaves the theorem's fixed-cardinality face
and remains live, as do a selected-cut deletion plus a compensating cut in a
previously unsplit base, alternative minimum base cuts, and non-cut circuit
rethreads.

A subsequent exact audit closes one natural depth-two subface.  Of the 66
formal unordered pairs of the twelve visible socket-escape moves, one pair
uses two alternative cuts in base 2251 and is incompatible.  All 65
compatible pairs remain zero-265-clean, yet every complete q1 formula is
UNSAT and all 65 proofs are DRAT-verified.  This rejects only pairs selected
entirely from the visible one-cut escape menu.  It does not test two recuts
which are individually invisible but jointly activate a new seam, a visible
escape plus an arbitrary neutral rerouter, or a pair which repairs an
individual local-zero failure.  In particular it does not promote the
Hamming lower bound from two to three.

Even q1 feasibility would still leave component joining, exact product
residence, ranks 11--17, rank-ten provider packing in the selected cover, and
the terminal compiler.

## 7. Reproducers

```text
scratch/search_l_k17_round02_dualfan_socket_escape_20260801.cpp
  SHA-256 76421ec6df9450bb962859c29f060778ad66caa616bdc3b210e1c8d3f2eaabac
scratch/run_l_k17_round02_dualfan_candidates_h100_20260801.sh
  SHA-256 e82c5fd4d6a5ee3f9d2fa88076787db6b31bf209cef94516a2ac497771ef3bb2
scratch/verify_l_k17_round02_dualfan_candidates_h100_20260801.sh
  SHA-256 d3b03d3c66c163c936cbb31d3f4c4b45261c3e13557dde5c2fdb097880ac9823
scratch/run_k17_round02_socket_escape_exact_q1_20260801.sh
  SHA-256 22a411450f7126f8840fd12dfefd7d612aadc891eec2223e4f04b0ccf1443ef5
scratch/verify_k17_round02_socket_escape_q1_unsat_20260801.sh
  SHA-256 e931444cbf101bb065fea32292de879a6f2abcf4c56da387dd3520656f4c6691
scratch/verify_k17_round02_core_piece_q1_unsat_20260801.sh
  SHA-256 221fd9b41197e81a35af67a9b064ccaa691dca16c59cc9c92eae7149ee41973d
scratch/k17_round02_dualfan_radius1_20260801/independent_partition.audit.tsv
  SHA-256 b92561c3d9317becd4ffc3d2e9216fbb715c4771dc376c85d005c530c617d107
scratch/l_k17_dense_q1_cegar_20260801/round02.core.cnf
  SHA-256 354e3aef1fa6512c29409656a7ab93c1049759f33b9bd2852830cb77ce54f56f
scratch/l_k17_dense_q1_cegar_20260801/round02.core.lemmas
  SHA-256 fb14a4ec64c4b49d5f4d87ea90fe40486455f2a4004e0defa522e1c4598b1a67
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.tsv
  SHA-256 7b2edd1557f4fe94e6c88acdc362ffb18b88cd21f8bf6e03eb3699f5c89556b7
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.audit.json
  SHA-256 fe5fb127e9d405574f9e1b7da7f2cc7fcdb98794ce0a881e6497819099123b70
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.q1_summary.tsv
  SHA-256 b2cdcece539162e9a0eee4ad4ebcdfc0597cc075e0b8732674511753add8a39b
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.drat_summary.tsv
  SHA-256 006c2c09177248228cf40a20d78472ee28abcc581c95308050546f3db6a1f3f3
```
