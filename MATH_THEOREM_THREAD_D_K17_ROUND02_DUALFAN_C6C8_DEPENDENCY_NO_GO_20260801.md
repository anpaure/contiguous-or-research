# The round02 `114930` dual fan: corrected dependency cone and the complete protected C6/C8 verdict

Date: 2026-08-01  
Status: proved for the fixed round02 bank and the stated protected incidence-C6/C8 catalogues

## 1. Correct physical indexing

The two q1 core sockets are the rank-nine owners

\[
        s=115442,\qquad t=115186.
\]

The labels `L3669,L3670` in the quotient-core report are not the literal
piece indices of the dense replay.  Resolving the owners in the rebuilt
round02 bank gives

\[
 (p_s,p_t)=(3670,3671),qquad
 (\tau_s,\tau_t)=(7340,7342),qquad
 (\eta_s,\eta_t)=(7341,7343),                 \tag{1.1}
\]

where `tau` is the outgoing state and `eta` the incoming state.  All finite
claims below use the owner masks in (1.1), not imported piece numbers.

## 2. Exact dependency-cone lemma

Let `M` be a protected incidence-C6 or incidence-C8 switch, and let `A(M)`
be the set of old fixed-cut pieces whose internal factor incidences it
changes.  Define `K` to contain the two socket pieces and every current piece
containing a rank-nine owner `h` for which

\[
        |h\cap s|=8\quad\hbox{or}\quad |h\cap t|=8,        \tag{2.1}
\]

and the intersection in (2.1) is one of the 7,612 selected lower colours.

**Lemma 2.1.** If `A(M) cap K` is empty, the `114930` dual-fan certificate is
unchanged.

**Proof.** Neither central socket piece is rebuilt.  Every changed relaxed
atom has at least one endpoint state in a rebuilt piece.  If a new atom were
incident with `tau_s,eta_s,tau_t`, or `eta_t`, its opposite endpoint owner
would satisfy (2.1), and its old containing piece would belong to `K`, a
contradiction.  The same argument applies to removal of an old incident atom.
Thus the central roles and all atoms at the two sockets are unchanged, so the
two-socket/one-colour dual fan remains a subformula.  QED.

For the frozen bank this cone has exactly 17 neighbour owners in 16 physical
pieces.

## 3. Complete finite census

The executable
`scratch/threadD_k17_round02_dualfan_c6c8_20260801.cpp` exhausts:

* all 46,818 protected legal incidence-C6 moves; 373 meet the cone;
* all 24,504,480 oriented incidence-C8 keys; 54,463 are factor-aligned and
  protected-safe, and 500 meet the cone.

Every retained move is replayed by rebuilding its literal fixed-cut paths and
all incident relaxed atoms.  A local-gate survivor must retain:

* exactly 7,612 paths and internal depth-three residence;
* zero lower, tail, head, common-orientation, and rank-ten singleton rows;
* the original factor rank-ten q1 palette;
* exact `TH`, `TC`, and `CH` matching ranks 7,612.

There are 138 structural breaker rows.  Exactly two pass every local gate,
both C6; no C8 does:

| C6 id | core | ordered labels | phase | new noncore socket atoms | degree of `114930` |
|---:|---:|:---:|---:|---:|---:|
| 26029 | 57944 | 2,5,16 | 0 | 34 | 80 |
| 44796 | 115376 | 0,1,6 | 1 | 10 | 64 |

Both rethread the physical `s` piece.  Their literal three-incidence ledgers
are frozen in `c6_26029.move.tsv` and `c6_44796.move.tsv`.

## 4. Exact full-q1 verdict on the two survivors

For each survivor the exact orientation/seam/colour model was rebuilt, with
one exact lower-colour row for every selected colour and an ALO row for every
rank-ten target absent from the current internal factor edges.

| id | atoms | variables | clauses | rank-ten rows | result |
|---:|---:|---:|---:|---:|:---|
| 26029 | 228,834 | 892,052 | 2,422,991 | 5,095 | UNSAT |
| 44796 | 228,822 | 892,005 | 2,422,860 | 5,095 | UNSAT |

Kissat returns UNSAT before branching in both cases.  `drat-trim` independently
verifies both proofs; each backward core has 26 original clauses, four lemmas,
and 32 resolution steps.

Hence no single protected incidence-C6 or incidence-C8 in the exact socket
dependency cone both preserves the full local ledger and completes the exact
q1+rank-ten model.

This is **not** a no-go for arbitrary two-cut substitutions, compound
circuits, larger q-gons, residence/deeper shadows, or the terminal compiler.

## 5. Frozen artifacts and hashes

Inputs:

* factor SHA-256 `7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df`;
* round02 bank SHA-256 `48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649`;
* C6 catalogue SHA-256 `f2c948de733a5286f4d21c3ba3cd2507831e2b061ca59f7fe82ace5c11b55d67`.

Code and census:

* source SHA-256 `1f0e3a9aa9e4389aa4ad689bd67c78b0c10e96066511000773abf0f5b9fd3e5a`;
* `census.tsv` SHA-256 `85a092ce915623ff0dc7e1ee789f3fab7d1f72b52980bf42c300f7e4ba9ce59b`;
* `census.audit.json` SHA-256 `3645537503ccd4319dcf95a9887dc5d27896de0819525595945fae243b3f79dc`.

Proof bundles under `scratch/threadD_k17_mask114930_c6c8_20260801/`:

* id 26029: compressed CNF SHA-256
  `30fd69a266ad7758135bbbcc0213a3fce44414b748510c4066cab053f892c171`,
  DRAT SHA-256
  `fa3e0cb2a7b1d000decba9dc0c53d1025d883e6d9d379b3349d3cacd4f16e8f0`,
  verifier output SHA-256
  `09868a56165cec791b2137f1a4785e0efffb57d36e8d7777d474cc3f0bfb3772`;
* id 44796: compressed CNF SHA-256
  `125c17102bf65f0fc1f83add63ca7195caef947f9253af960cf86f32305f6400`,
  DRAT SHA-256
  `ba2f6de454e435334dec670ec9daf287c0428a34f747e478400665894502c859`,
  verifier output SHA-256
  `dcadffcb55e0c5d14a280521346b3c0abcc013f393dc3b76966263ad03a6fbe4`.

