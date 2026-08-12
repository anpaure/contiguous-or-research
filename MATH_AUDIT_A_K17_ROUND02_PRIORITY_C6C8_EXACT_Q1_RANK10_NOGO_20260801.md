# K17 round02 priority C6/C8 exact-q1 and rank-ten no-go

Date: 2026-08-01  
Lane: A, independent replay of Lane L round02  
Status: exact literal atlas replay; three strengthened CNFs are DRAT-verified UNSAT

## 1. Exact outcome

The authenticated round02 cut bank has 7,612 fixed lower masks, 228,836
relaxed atoms, no common-orientation failures, no rank-ten support zeros, and
perfect TH/TC/CH projections.  Its currently priced exact-q1 core colour is
the rank-eight mask `114930`, with 80 relaxed providers.

The three requested protected incidence switches were applied to the
underlying factor and replayed against those same fixed lower masks:

| move | relaxed atoms | rank-ten ALO rows | variables | clauses | result |
|---|---:|---:|---:|---:|---|
| C6 `868` | 228,800 | 5,095 | 891,915 | 2,422,618 | UNSAT, DRAT verified |
| C6 `8242` | 228,816 | 5,096 | 891,979 | 2,422,795 | UNSAT, DRAT verified |
| C8 `6668744` | 228,848 | 5,094 | 892,107 | 2,423,143 | UNSAT, DRAT verified |

Every row retains all of the following literal gates:

- the fixed-cut residual is exactly 7,612 paths;
- every rebuilt path is internally depth-three resident;
- `B=0` and `H10=0`;
- TH, TC, and CH Hopcroft--Karp sizes are each 7,612; and
- the underlying factor has zero rank-ten holes.

The CNF is built directly from the changed path states and changed relaxed
atom atlas.  It does not replay round02 candidate-cut indices after changing
the factor.  It enforces exactly one orientation per physical path, exactly
one incoming and outgoing atom at the selected orientation, exactly one atom
for every selected lower colour, and an ALO for every rank-ten target absent
from the current internal path edges.  Thus these are strengthened exact-q1
plus rank-ten-support no-go certificates.

There is no selected-atom model to replay: all three formulas are UNSAT.  The
literal pre-CNF replay is recorded in the three audit JSON files, and each
terminal negative verdict is independently checked by `drat-trim`.

## 2. Target `114930` is unchanged

The target-provider identity audit hashes each complete oriented endpoint
state, not merely its numerical state ID.  In all three children:

```text
target                 114930
baseline degree        80
child degree           80
removed identities      0
added identities        0
identity set equal       1
```

Therefore none of the three moves acts on the priced `114930` provider
atlas.  The Lane L radius-one cut scan tested 16,667 single-cut moves, of
which 13,043 retained the zero/zero local state, and found no strict provider
degree gain for `114930`.  That is a degree-gain census only.  It is not a
necessity theorem for repairing exact q1, and it is not closure under
multi-cut or factor-rethread moves.

## 3. Compact surviving obstruction

For each child, proof trimming returns 26 original clauses and four lemmas.
The variable numbers shift slightly with the atom count, but the physical
quotient is identical.  It is an untouched two-colour bow tie on pieces
`243`, `244`, and `3262`:

| lower | directed relaxed atoms | upper |
|---:|---|---:|
| `74383` | `243_0 -> 244_0`, `244_1 -> 243_1` | `91791` |
| `67215` | `244_1 -> 3262_1`, `3262_0 -> 244_0` | `108175` |

For C6 `868` the four atom variables are respectively `22722`, `22745`,
`22752`, and `113449`; orientation variables `487,488` are the two states of
piece 243, while `489,490` are the two states of piece 244.  The two colour
ALOs, the common-orientation AMOs, and the sequential AMO chains at the
central sockets derive the empty clause.  The core uses no rank-ten coverage
clause and contains no provider of lower `114930`.

The same fan appears in the other two proofs with atom variables

```text
C6 8242:     22709, 22732, 22739, 113429
C8 6668744:  22723, 22746, 22753, 113463.
```

A separate proof extraction found another untouched dual fan, centered at
piece 6062 and using lower masks `54089` and `54092`.  Hence the priced
`114930` core is only one member of a multi-core landscape: removing or
raising its degree need not improve exact matching rank.

## 4. Frozen lineage

Inputs and executables:

```text
factor.tsv                         7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
round02.bank.tsv                   48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649
c6.tsv                             f2c948de733a5286f4d21c3ba3cd2507831e2b061ca59f7fe82ace5c11b55d67
round02 replay source              dc206294dd92181637ea2809c2feb06d4219fffdbc85c32a567e451c8eae208c
round02 O3 executable              67fe167c97013bd1bb94479598719b5455bf68021928ecfc9e1734ff06afb1d1
Kissat executable                  3ee4239c0bef4d237ab72827613426855b17c636d3b5843158fe5e549b175b0d
drat-trim executable               92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a
target identity source             f0cfd4d02bfe55eac4246f1db1cd0d1a319d374bae990e8c7079f0c4d496e309
target identity O3 executable      1632b18c110cc00731212f6db63727dcdf45106790cd8de1b19f7cb5e76b10f0
target identity output             00c74c6426c5a5448114c994c9df80a104fcb8aa4d82be3deeb116c5f17ba613
```

Formula, proof, and checker hashes:

| move | CNF | DRAT proof | checker output |
|---|---|---|---|
| C6 `868` | `b2fa835ba0d17e9fc2e5c388ed4251831dfce157661d75455562214bc6605588` | `826bdc6b82e6b1bb17a8efb7fe2ef32e939c1be177def31257a7b14b245c4340` | `807aa9c4130d5e95cd91474990d73310332d8718b8433177ec47f320857b1f65` |
| C6 `8242` | `c71e486c1c3b85ec335e6ce9a80698897ad07d28d5702b105721243623101f8b` | `a7c995c4553c387ddd02e4fe5e3e795a36871979e4ef18e0c03d8409f4995e71` | `a80eb3d27317f8d69494114ceabbbd5e566efbe8653b855de6014c83e2e73a62` |
| C8 `6668744` | `829c04d57c13acf178ff52b3d47abc264040c1d06d835d8e55c7a327a7c6cf21` | `bb5e223ef630e60f7dfd6adfdb80ca3add7e8175043657fd39eebc947263e547` | `cfc24a9f5356817d6ba0fb787551cfa55893b3ca533e19136073724a181254f3` |

The complete remote campaign is

```text
/home/amodo/or15/work/threadA_k17_round02_priority_c6c8_20260801
```

and the compact local audit bundle is

```text
scratch/threadA_k17_round02_priority_c6c8_20260801/
```

## 5. Scope

This proves a parallel higher-order no-go for exactly three named protected
factor switches on the fixed round02 cut bank.  It does not prove that
`114930` must gain a provider, that Lane L's radius-one scan is closed under
compound moves, or that all protected C6/C8 switches fail.  Internal D3 is a
path-local condition only.  Connectivity, boundary/global residence,
deeper shadows, opening, voltage, and the final compiler are not reached,
because exact q1 already fails.
