# RF-halo `j=3959`: exact three-anchor Hall kernel and a local service-block lift

Date: 2026-07-30

Status: **PASS solver-free local theorem and compact exact catalogue; global
embedding open**.

This note is source-relative to the authenticated geometry-valid `j=3959`
rank-eight chronology.  It proves the smallest lossless abstract repair of its
canonical Hall core, translates that repair into exact physical anchor types,
and classifies the authenticated 5,166 depth-two upper-service blocks.  It
does not prove a universal length-12,873 word and does not claim an
unrestricted K16 no-go.

## 1. Frozen Hall core

Put

```text
P = 2665,   Q = 8000,
S = {0665,066d,0675,06e5,0765,1665,8665}.
```

An independent reconstruction from the target chronology gives exactly six
neighbour cells:

| cell | source interval | allow | must | neighbours in `S` |
|---:|:---|:---|:---|:---|
| 803 | `[267,270)` | `0765` | `0465` | `0665,0765` |
| 2939 | `[979,982)` | `0675` | `0461` | `0665,0675` |
| 4349 | `[1449,1452)` | `066d` | `0464` | `0665,066d` |
| 9215 | `[3071,3074)` | `1665` | `0265` | `0665,1665` |
| 19070 | `[6356,6359)` | `06e5` | `0661` | `0665,06e5` |
| 27225 | `[10395,10397)` | `8665` | `0660` | `0665,8665` |

Both `P` and `Q` have degree zero.  Thus the induced graph is two isolates
plus a seven-left/six-right star: the core `0665` sees every old cell and each
of the other six star masks sees its private cell.  Its matching number is six
and its deficiency is three.

The reconstruction also authenticates the stored full matching: all lower
targets outside these nine are matched and the six displayed cells are owned
inside the nine-target shore.  This fact permits a direct splice only when an
abstract repair adds literal new right vertices, or when the chosen physical
cells are unused by that matching.  Newly adjacent existing cells can have
outside owners, so a physical chronology must still replay the full lower
matching.

## 2. Smallest lossless abstract augmentation

Let `Z` be a set of added right vertices, with every old incidence retained,
and define

```text
A = neighbours of P in Z,
B = neighbours of Q in Z,
C = {z in Z : z is adjacent to at least one target in S}.
```

### Theorem 1 (three-role SDR)

The nine-target shore is saturable after the lossless augmentation if and
only if the three families `A,B,C` have a system of distinct representatives.

**Proof.**  Since `P,Q` have no old neighbours, a matching must send them to
two distinct vertices of `Z`.  Seven star targets have only six old cells, so
one star target must use a third vertex of `Z`.  This proves necessity.

Conversely choose distinct representatives for `P,Q` and a star target `s`.
If `s=0665`, match all six leaves to their private old cells.  If `s` is a
leaf, match `0665` to that leaf's old cell and match the other five leaves to
their private cells.  This saturates all nine targets.  ∎

Consequently three added vertices are necessary and sufficient abstractly.
For three distinct vertices, Hall's inequalities reduce to

```text
|A|,|B|,|C| >= 1,
|A union B|, |A union C|, |B union C| >= 2.
```

The union of all three families automatically has size three because every
new vertex has a nonempty role signature.  Exhausting the seven signatures

```text
P, Q, S, PQ, PS, QS, PQS
```

gives 84 unordered three-vertex multisets: exactly 51 pass and 33 fail, in 23
orbits under permutation of the roles.  The audit JSON records all 84 rows;
the TSV is the compact exact equality catalogue.

For an arbitrary physical edit, this is a necessary projection, not a
standalone compiler proof.  If an old incidence is lost or an exterior cell
was already needed elsewhere, recompute the literal nine-row matching and
then the full lower matching.

## 3. Exact physical anchor types

For a proper-prefix source interval `J`, let `U(J)` be the OR of its maximal
source envelopes, `M(J)` its mandatory mask, and `E_p` the envelope at
position `p`.  The exact individual candidate law is

```text
M(J) subseteq T subseteq U(J),
E_p intersects T for every p in J.                         (1)
```

One interval serves every target in a family `F` exactly when

```text
M(J) subseteq intersection(F),
union(F) subseteq U(J),
E_p intersects every T in F for every p in J.              (2)
```

Important specializations are:

* `P+Q`: `M(J)=0`, `a665 subseteq U(J)`, and every position contains the top
  bit and meets `2665`.
* `P+star target T`: `M(J) subseteq 0665`,
  `2665|T subseteq U(J)`, and every position meets both masks.
* `Q+T` for a no-top star target: `M(J)=0`, `8000|T subseteq U(J)`, and every
  position contains the top bit and meets `T`.
* `Q+8665`: `M(J) subseteq 8000`, `8665 subseteq U(J)`, and every position
  contains the top bit.

The frozen geometry has no zero-mandatory cell.  More sharply, no incumbent
cell even has an allowed union containing `2665`; 12,864 cells have the top
bit in their allowed union, but every one has a mandatory bit outside
`8000`.  Hence the baseline has no `P` or `Q` anchor and no multi-signature
anchor of the displayed types.  The nonempty one-predicate frontiers
(`P`: 34, `Q`: 1,428, external star: 207) show why these local predicates do
not by themselves prove a wider chronology no-go.

## 4. The 5,166 upper-service blocks

The authenticated block census contains 34,560 raw blocks and exactly 5,166
which are internally depth-two resident.  Each block is

```text
B = (V0,V1,V2,4a79,4e39,4d39)
```

and supplies the encoded upper services

```text
ca79 < ea79 < eb79,     4e79,
```

while retaining the final `4e39--4d39` lower-provider edge.  Boundary
residence and global embedding are not part of that source census.

### Theorem 2 (exact local `Q+S` lift)

At constant compiler depth two, every one of the 5,166 blocks admits:

1. a length-one internal candidate for `Q=8000`; and
2. a distinct right-straddling candidate for star leaf `0765`.

Only the `P=2665` role is forced outside this six-row collar.

**Internal `Q` cell.**  Let `L1,L2` be the immediately preceding two target
rows.  Exact replay of the block forces `L1` to contain every prefix bit whose
initial run has length one or two, and forces `L2` to contain every prefix bit
whose initial run has length one.  Put

```text
K = (prefix-run<=2 mask) OR ((V0&V1&V2)&7fff).
```

For every block, `K` has rank seven.  There are 56 distinct `K` values, with
intersection `2100`, union `6b79`, and multiplicity histogram

```text
20*81 + 30*96 + 6*111 = 5166.
```

Choosing `L1` as any rank-eight completion of `K` other than `V0` gives eight
nonflat choices.  Then the internal envelope at relative source position two
contains the top bit, while all its low bits also occur at the preceding
source position; no forbidden low bit is mandatory.  Equation (1) therefore
gives an exact `8000` cell.  `L2` must additionally contain the prefix-run-one
mask.  The unchanged predecessor `fb40` contains none of the 56 required
cores, so the unmodified left boundary realizes zero blocks.

**Universal right star cell.**  Exact replay at the fixed block suffix
requires the first two right rows to contain `0500` and `0100`, respectively.
For every block choose

```text
R0 = 0767,     R1 = 076d,     R2 = 027f.
```

These are distinct rank-eight rows, `R0` contains `0500`, and `R1` contains
`0100`.  The two envelopes of the right straddler are then

```text
4d39 & R0 & R1 = 0521,
R0 & R1 & R2   = 0265.
```

Both are nonzero and their OR is exactly `0765`.  Any mandatory bit of this
cell lies in that same allowed union, so (1) proves an exact `0765` candidate.
The independent replay verifies the six block rows and these two cells for
all 5,166 blocks.

No length-one/two cell wholly controlled by the collar can serve any of the
seven star masks or `2665`.  A left straddler can serve `0765` for 1,086
blocks, but none serves `2665`; on the right, the final `4d39`-only suffix
makes bit `0100` mandatory, which also excludes `2665`.  Thus `P` genuinely
requires a third, distinct exterior anchor.

Combining Theorems 1 and 2 yields an explicit local equality lift: match
`8000` to the internal cell, match `0765` to the right straddler, and seek one
exterior `2665` cell.  The old `0765` private cell can then take core `0665`,
and the other five leaves use their old private cells.

## 5. Exact scope and next gate

The service-only relocation which moves `4a79,4e39,4d39` behind the intact
tail retains all six old star/private cells locally (starts
`267,979,1449,3071,6356->6353,10395->10392`).  Its unbuffered chronology still
has 26 structural seam errors.  Likewise, the displayed `R0,R1,R2` rows have
only been replayed far enough to prove the six block rows and local Hall cell;
their own outer-row embedding remains open.

The proof-safe construction cascade is therefore:

1. choose a block, one of its eight nonflat `L1` completions, a compatible
   `L2`, and the universal right boundary;
2. embed those rows with exact envelope/middle replay and preserve the six old
   star cells;
3. create a distinct exterior `2665` anchor;
4. replay the nine-target matching and then the full lower matching;
5. only then replay the two upper chains and all 65,535 masks.

The upper identities encoded by the block were used only to define the
5,166-member domain.  No upper-complete chronology is claimed.

For completeness, an independent depth-three projection of the same block
values is also frozen.  Only 2,250 of 5,166 pass the necessary internally
known depth-three middle reconstruction; 2,916 are already impossible in a
depth-three placement.  This does not affect the depth-two lift above.

## 6. Frozen artifacts

Hall kernel and equality catalogue:

```text
scratch/audit_j3959_local_hall_augmentation_independent_20260730.py
  SHA 4d728d0814f22a8d6ca0204fba39964b391321e6749fbfba257a29e0c2c2872a
scratch/k16_j3959_hall_core_augmentation_20260730.audit.json
  SHA 611f19912f9acfcd8d21fa71b0d92010d0c23d45dac658d11506bb45694df9d4
  payload 45afc9b92d90e9b470eefd98c3b0e7e9557d646f94df408ee81fdb0e42cd406a
scratch/k16_j3959_hall_core_three_anchor_catalogue_20260730.tsv
  SHA 0afa5e0ae40b687d58a53ddb39e08d729cab3f2f9c66a07576f554361fb4c659
```

Independent physical-anchor audit:

```text
MATH_AUDIT_K16_RF_HALO_J3959_HALL_ANCHOR_TYPES_20260730.md
  SHA f61ec8e6fe68a37a87de2a304bfb3214b8c21f68ba7b5b94796dca517fcf00d3
scratch/k16_rf_halo_j3959_hall_anchor_types_20260730/hall_anchor_types.audit.json
  SHA 4cecacbf2291fd857f2b624dcd768a2d2abafb6fc8cf37c088fa44a9e99c2b24
  payload 4314e3f685318c751bd3887dddbfda3ae76368a3c58499e46f895ef5bd192219
scratch/k16_rf_halo_j3959_hall_anchor_types_20260730/independent_replay.audit.json
  SHA aeb91e3f1dfeb3b8b1a9357dd2017146b2e942d561dc106ed5643e1096e6fff0
  payload d4cf92d906eb76bf70989246538754c04070219e22f88e51b473d5cc2721b7c9
```

Depth-two service-block lift:

```text
scratch/audit_k16_j3959_alternative_upper_service_blocks_20260730.py
  SHA b355269642f50a45fecfb9a52a00bca3b7ef78c9ee44ec8378bd1da9c685244b
scratch/k16_j3959_alternative_upper_service_blocks_20260730.audit.json
  SHA 2f1b37317f7ad99271a459647aea58fdd41d863efa23f8f315336c08ffefb101
  payload a736c39b447d4fd9bbcaf77d7a8058ae3157bf6fad7f75107db159796378d4f3
scratch/audit_k16_j3959_upper_service_block_hall_types_20260730.py
  SHA 122e820433027cc1e84acc65d61e5491875d0f33ca502855829d71668e26e1ed
scratch/k16_j3959_upper_service_block_hall_types_20260730.audit.json
  SHA 981ffbba35fbe3afdbc8d14241e6b78518dcac7d132326886c3827ce03944b0d
  payload 5f5bbffa95cca885573604bbd84c3b3290b25fee5aebc8291794bc91b883ec9b
scratch/k16_j3959_upper_service_block_q_boundary_catalogue_20260730.tsv
  SHA b6bbbfdc2535356032fd70c86b341cf8c8bb31f76874a467d851afcd8e7b88d4
scratch/independent_replay_k16_j3959_upper_service_block_local_lift_20260730.py
  SHA bfb7e320f51ed44cc1d4846b640fc61f29f542e024816d60eec65ec7db6ccb6f
scratch/k16_j3959_upper_service_block_local_lift_independent_20260730.audit.json
  SHA 8e20283a099d5ceb89cdde93e966a9d0f1620fbc0c106f9bb4589438048d0720
  payload 34088842368c9034852636d9240ed99361ea6905aed9308026754503f89b101b
```

Depth-three necessary projection:

```text
scratch/audit_k16_j3959_upper_service_block_hall_boundaries_20260730.py
  SHA f09a2c612d061354605ac017d8bee9a1b0334ab8bfdc4947fe2e32baad1eeb3e
scratch/k16_j3959_upper_service_block_hall_boundaries_20260730.audit.json
  SHA 9c70494779b86358f4b2d09c5c7dfa852471c2fee0fec4b6918cd47f0e7a7a3b
  payload 89ec306e235ce58762de551ac229df1572e2dd8b4353681fed25a221b58a2856
scratch/k16_j3959_upper_service_block_hall_boundary_types_20260730.tsv
  SHA a788558730234390a9486a65040d98bd3a1610b4cb366b000ee1f82f62b25320
```

Frozen chronology:

```text
scratch/k16_rf_halo_j_family_20260730/rank1_j3959.targets
  SHA edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee
```
