# The `K17` occ296+C6 signed exchange master and last-provider guards

Date: 2026-07-31  
Lane: AD, compact evaluator on the occurrence296 plus residual-C6 checkpoint  
Status: exact source-relative catalogue, sparse rank-ten master, and literal
post-connectivity oracle; no repaired carrier or compiler is claimed

## 1. Frozen source and scope

The source factor is the independently replayed occurrence296 plus C6
checkpoint

```text
scratch/k17_opt28_occ296_c6_localmin_verified_20260731.owner_cycle.word
  SHA-256 a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49
scratch/k17_opt28_occ296_c6_localmin_verified_20260731.residual.json
  SHA-256 6fcc91d45b2090b26b612020340a21088a2367c5c0bccd10d3d3614042c60fe4
scratch/k17_opt28_occ296_c6_localmin_candidate_20260731.json
  SHA-256 960ca8df23e7c4ea28c6381e6642b4ec1ab86288a57329115d72182e56be949c
```

The word contains all `24310` rank-nine owners, has all `24310` rank-eight
Johnson edge colours exactly once, and is one cycle.  The marked bank is one
literal interval of `4108` owners.  After rotating marked-first, the frozen
cross edges are

```text
83766 -> 18358, intersection 18230;
7418  -> 71930, intersection  6394 (the linear closing edge).
```

Its exact two-bank zipper baseline is

```text
strict D2 / D3 bad                       503 / 503
empty envelope / replay bad                0 / 748
replay missing bits                            776
upper holes rank 10 / 11 / 12       1585 / 824 / 116
upper holes rank 13 through 17                    0.
```

The filename `localmin` is an artifact label, not a theorem that every legal
neighbourhood has been exhausted.

## 2. Complete fresh exchange catalogue

Let `P` be the marked owner set and `Q` its complement.  For every rank-eight
colour `c` whose incumbent edge `{a_c,b_c}` lies wholly in `Q`, define

\[
 V_c=\{v\in Q:c\subset v\}.
\]

An off-source column is an unordered pair `{u,v}` in `V_c` other than
`{a_c,b_c}`.  It means delete `{a_c,b_c}` and add `{u,v}`.  Here a factor in
the stated face means a spanning simple two-factor which contains the entire
frozen marked/cross bank and whose edge-to-rank-eight-intersection map is a
bijection.  The source pair is read from the `a47aa9d...` cycle, so no
occurrence-only or OPTIMAL28 delta is reused.

### Theorem 2.1 (complete source-relative parametrization)

The catalogue contains exactly

```text
mutable lower-colour groups                     20201
off-source columns                              545721
columns including implicit keeps                565922
group-size profile
  |V_c|=3,4,5,6,7,8,9:
  15,129,454,1601,3836,6748,7418.
```

Every marked-preserving lower-rainbow factor on this fixed owner partition
and fixed marked/cross bank occurs exactly once as a choice of one implicit
keep or one off-source column in every group, subject to the owner-degree
equations.  Such a choice is one cycle iff its degree-two graph is connected.

#### Proof

The frozen marked path plus its two cross edges already gives degree two to
every marked owner: an internal marked owner has two path edges, and each
marked endpoint has one path edge and one cross edge.  Hence every remaining
edge of a factor in this face lies wholly in `Q`.  Every such Johnson edge
has one rank-eight intersection `c` and both endpoints belong to `V_c`.
Conversely every two distinct elements of `V_c` are rank-nine owners
intersecting exactly in `c`, hence form a Johnson edge.  Lower-rainbow
exactness permits exactly one edge per `c`.  The marked and cross colours are
frozen, leaving precisely the `20201` complement colours.  Thus the
per-colour choices are exhaustive and disjoint.  Requiring degree two at
every complement owner makes their union with the frozen marked/cross bank a
spanning two-factor.  A finite two-factor is a single cycle exactly when it
is connected.  Direct enumeration gives the displayed counts. ∎

The canonical column stream is

```text
SHA-256 a0d5efb22115745fab920bd26215a8cbc8ac2b711f0a14834f6a03a189f2bed5.
```

The packed complete catalogue is

```text
scratch/ad_k17_occ296_c6_localmin_marked_exchange_catalogue_20260731.bin
  SHA-256 f07bab5342ecf376039cc0359559e6366ad62987dc4f556668a91f2d7b387bc3
```

## 3. Exact signed rank-ten rows

Write the marked-first **source** order as

\[
 O_0=(P_1,\ldots,P_{4108},Q^0_1,\ldots,Q^0_{20202}).
\]

The exposed source pairs are `(O_0)_i(O_0)_(i+1)` for
`1<=i<24310`.  The cycle closes through `Q_20202 P_1`, but that edge
occurrence is not an exposed linear pair.

For source group `c`, let `y_c` indicate that its source edge is deleted and
let `x_{c,uv}` select its replacement.  The exact group equation is

\[
       \sum_{uv}x_{c,uv}=y_c.                    \tag{3.1}
\]

For every complement owner `w`, exact degree preservation is

\[
 \sum_{c,uv}x_{c,uv}{\bf1}_{w\in\{u,v\}}
 -\sum_c y_c{\bf1}_{w\in\{a_c,b_c\}}=0.         \tag{3.2}
\]

Let `L_0(S)` be the number of source owner edges of union `S`, omitting the
closing edge `Q_20202 P_1`.  Then every rank-ten target has the exact row

\[
 L_0(S)+\sum_{c,uv:u\cup v=S}x_{c,uv}
       -\sum_{c:a_c\cup b_c=S}y_c\ge1.          \tag{3.3}
\]

### Lemma 3.1 (linear zipper identity)

For every connected factor `F` on this fixed marked/cross face, orient its
unique cycle through the frozen marked path and write

\[
 O_F=(P_1,\ldots,P_{4108},Q^F_1,\ldots,Q^F_{20202}).
\]

A rank-ten target occurs as an interval OR in the literal zipper of `F` iff
it is the union of an exposed pair `(O_F)_i(O_F)_(i+1)`,
`1<=i<24310`.

#### Proof

Let `M=4108`, `R=20202`, and put

\[
 g_0=P_M\cap Q^F_1,\quad
 g_i=Q^F_i\cap Q^F_{i+1}\ (1\le i<R),\quad
 g_R=Q^F_R\cap P_1.
\]

The lower-rainbow property makes the two incident facets of each `Q^F_i`
distinct rank-eight subsets of that rank-nine owner, hence
`g_(i-1) union g_i=Q^F_i`.  The exposed pairs have canonical witnesses

```text
P_i P_(i+1):       [P_i,P_(i+1)],
P_M Q^F_1:         [P_M,g_0,g_1],
Q^F_i Q^F_(i+1):  [g_(i-1),g_i,g_(i+1)].
```

Conversely, a rank-ten interval containing at least two marked tokens
contains a consecutive marked pair.  If it contains exactly one marked token
and any facets, that token must be `P_M`; rank ten requires the interval to
reach `g_1`, so it contains the boundary witness.  If it contains no marked
token, two consecutive facets union to only a rank-nine owner, so a rank-ten
interval contains three consecutive facets and hence a complement witness.
In every case the witness union is a rank-ten subset of the interval union
and therefore equals it.  The final-to-first edge occurrence has no
contiguous linear suffix/prefix witness and is the unique omitted occurrence.
Its *target* need not be omitted, because another exposed edge may have the
same union. ∎

No general multiplicity equality is asserted by this proof.  For the frozen
source, a complete exact census separately proves that the targets of exposed
load one are exactly the literal interval-load-one targets; both sets have
size `12196`.  This check is necessary at the marked/facet boundary: the
interval `[P_4107,P_4108]` can be extended by the inert first facet without
changing its union `0x14776`, but that target already has the second exposed
provider `P_4106 P_4107`.  Similarly, the closing union `0x11cfa` has two
cyclic edge occurrences but exposed load one and literal interval load one.
Only the closing edge occurrence, not its target, is omitted from `L_0`.

For every group/degree selection, (3.3) is the exact algebraic exposed-edge
load row.  After the selection is connected, Lemma 3.1 makes that same row
exact for literal rank-ten interval coverage.  Thus all losses and gains are
included; no fixed-window approximation is used.

There are `1585` currently absent rank-ten targets, with `54307` fresh
restoring references and support `10..45`.  As one selected column has only
one new union label,

\[
                         \sum_c y_c\ge1585.       \tag{3.4}
\]

The gain-bank index is

```text
scratch/ad_k17_occ296_c6_localmin_marked_exchange_rank10holes_20260731.bin
  SHA-256 ec2a03c16bdacd82fcc98682efeea503506c1b9be11f80674e23533c73098d08
```

## 4. Protected last providers

The exposed-owner-edge source load `L_0` has profile

```text
load        1      2    3   4  5
targets 12196   4948  662  54  3.
```

Of the `12196` singleton targets, `2826` have their provider in the frozen
marked/cross bank.  The other `9370` have a unique incumbent complement
group `g(S)`.  Their exact sparse survival row is

\[
   \sum_{j:\,\operatorname{newunion}(j)=S}x_j-y_{g(S)}\ge0. \tag{4.1}
\]

There are `289011` restoring references.  Exactly one row has no restorer:

```text
S = 0x1c0df = 114911,
g(S) = 17165,
old lower colour = 0x180d7,
old edge = {0x180df,0x1c0d7}.
```

Thus (4.1) forces `y_17165=0` in this exchange fibre.  This is not a global
obstruction: a move changing the marked/cross bank lies outside the theorem.

The protected bank is deliberately distinct from the hole bank:

```text
scratch/ad_k17_occ296_c6_localmin_marked_exchange_rank10_protected_last_20260731.bin
  SHA-256 cac1fe10e4c2c4d49436252e6ac3e8a6d2b705ec9ec68f1e07949f130667c6a8
```

Its layout is header `<8s4I>`, then target masks, incumbent group IDs, CSR
offsets, and restoring column IDs.  No one-gain cardinality floor applies to
these already-covered targets.  In the full master, (4.1) is already the
`L_0(S)=1` instance of (3.3); the sidecar exposes it directly to D/R.

## 5. Ranks eleven/twelve and residence

Ranks eleven and twelve are chronology-dependent.  A single exchange column
usually violates degree and has no literal path order, so assigning it an
independent rank-eleven/twelve or residence delta is not sound.  The exact
workflow is:

1. solve (3.1)--(3.3) and the degree rows;
2. add ordinary component cuts until the chosen factor is one cycle;
3. traverse that cycle from the frozen marked orientation;
4. materialize its literal facet zipper; and
5. rescan every rank-10/11/12 interval, strict D2/D3 run, maximal envelope,
   replay row, and compiler pre-guard.

The compact baseline target-load sidecar contains every rank-10/11/12 target
and its exact interval load:

```text
scratch/ad_k17_occ296_c6_localmin_marked_exchange_upper_guard_loads_20260731.bin
  SHA-256 f6250f930b9de74706c2cb14c4e8c34cd21794200fc8bf682b643ff2cf07cc59
```

Its singleton counts are

```text
rank 10 / 11 / 12: 12196 / 4448 / 772.
```

The binary layout is header `<8s4I>`, followed for each rank by `<4I>` and a
complete `(target,load)` table.  It is a separation/index artifact, not an
assertion that deep rows are affine in isolated columns.

The exact literal oracle is

```text
scratch/evaluate_ad_k17_opt28_marked_exchange_20260731.cpp
  SHA-256 037ad2f0a4ec332b7ccbfdfba05730a10f1ed1f86091905f45a3c8bef35cbc60
scratch/ad_k17_occ296_c6_localmin_marked_exchange_seed_20260731.bin
  SHA-256 cdcbb96057049e4f4906db343ac73810be9ff8ed4ab49f4f620efbcb6490e3d9
```

For every connected compound selection it reports exact gained and lost
target masks at each of ranks 10, 11, and 12, hence exact last-provider
losses, together with residence and compiler guards.  The empty-selection
regression has SHA
`65655e7e2383020c6575bbfaf6cbe59fa1baeaa9af96531aae85a83f3a10a31e`
and reproduces `503/503`, `748/776`, and `1585/824/116` exactly.

A nonempty exact regression reverses the last authenticated C6 circuit.  Its
three fresh source-relative column IDs are `7408,7613,106479`.  The selection
remains degree two, connected and lower-rainbow, and the signed rank-ten delta
passes.  Literal replay gives

```text
                         base     reverse-C6
rank-10 holes             1585       1584   (gain 1, loss 0)
rank-11 holes              824        822   (gain 2, loss 0)
rank-12 holes              116        117   (gain 0, loss 1)
strict D2 / replay bad 503 / 748  503 / 749.
```

Thus even a legal compound that improves ranks ten and eleven can destroy a
rank-twelve last provider.  The selection/evaluation SHAs are
`c2b2c49064013cde8070b8ecb4cbaff07ca119ddca190d649ed870b4b787305b`
and
`b1b0c5ab3ab24a12b75fcfeebf7475384e7a162f455db959c8bb5850c585bc33`.
The solver-free mapping/evaluator-consistency audit is
`scratch/audit_ad_k17_occ296_c6_reverse_last_regression_20260731.py`
(SHA `cde6ae516663b9d9002f5c7215ac1bbe851ed2616689ecd3fad0cbe11e6d9bba`),
with JSON SHA
`2ea390bee5ff3171c3d6aaeeb7adafb2f722180a7ce22c0014ca530a724ef791`.

## 6. Sparse master delivered to D/R

The executable wrapper is

```text
scratch/solve_ad_k17_occ296_c6_localmin_signed_rank10_master_20260731.py
  SHA-256 62a057c44da61eedc45a985e6d854e2dc459fcc9f31a453446215b8b8b8a0da3
```

It fail-closes on old split/occurrence deltas and authenticates the current
cycle, residual, catalogue stream, metadata, protected bank, guard bank,
seed, and evaluator.  The gain-bank binary is an independently audited
sidecar recorded by the metadata; the wrapper does not open it.  Its exact
initial model has

```text
off-source x variables                          545721
changed-group y variables                        20201
total Boolean variables                         565922
group rows                                       20201
owner-degree rows                                20202
rank-ten signed rows                             19448
initial hard rows                                59851.
```

The H100 CPU-only build used one process, one pinned CPU, a `12 GiB` address
cap, `387224 KiB` maximum RSS, and `4.19 s` wall time.  The frozen proto is

```text
/home/amodo/or15/work/ad_k17_occ296_c6_master_a0d5_20260731/rank10_master.bin
  SHA-256 6e91df2f2767a43fb5f24a6eaa9909807f4b25ce216aef4435d4a72af36aa3fc
```

The authenticated build-result SHA is
`5225020b2b22d45bf31b86abda3409b39e7d6ecfb89761c54d24437a0a94b2d6`
with payload
`1840f53bb9a0603b68002e399d9492cbada0f3015049afdb34c8a5b7d2f5e938`.
The byte-identical local build manifest is
`scratch/ad_k17_occ296_c6_localmin_signed_rank10_master_20260731.build.json`.
The model was built, not solved.

Reproduction commands are

```sh
python3 scratch/solve_ad_k17_occ296_c6_localmin_signed_rank10_master_20260731.py \
  --validate-only --output /tmp/c6.validate.json

python3 scratch/solve_ad_k17_occ296_c6_localmin_signed_rank10_master_20260731.py \
  --build-only --model-output /tmp/c6.rank10.bin --output /tmp/c6.build.json

clang++ -std=c++20 -O2 scratch/evaluate_ad_k17_opt28_marked_exchange_20260731.cpp \
  -o /tmp/c6_eval
/tmp/c6_eval \
  scratch/k17_opt28_occ296_c6_localmin_verified_20260731.owner_cycle.word \
  scratch/ad_k17_occ296_c6_localmin_marked_exchange_seed_20260731.bin \
  SELECTION.txt OUTPUT.json
```

## 7. Exact boundary

Proved and delivered:

* a complete fresh `545721`-column exchange bank relative to the C6 source;
* exact group, owner-degree, lower-q1, connectivity, and all rank-ten rows;
* separate gain and protected-loss banks, including one forced keep;
* exact baseline load tables at ranks 10--12; and
* exact post-connectivity scoring of rank10--12 losses, residence, envelopes,
  replay, and scalar compiler pre-guards.

Not proved:

* feasibility of the signed degree/rank-ten master;
* existence of a connected compound selection improving the literal score;
* common-cap matching (the current scalar margin `3293-(1585+824+116)=768`
  is only diagnostic);
* an exact compiler; or
* a `K17` equality word.

Every future compound packet must be decoded to literal removed/added edges
relative to cycle SHA `a47aa9d...` before composition.  Old fixed-base deltas
remain inadmissible.

## 8. Independent audits

The complete binary catalogue, both signed sidecars, all `38012` guard rows,
the seed, empty replay, wrapper pins, and signed-row semantics were rebuilt
independently in

```text
MATH_AUDIT_AD_K17_OCC296_C6_EXCHANGE_AND_LAST_PROVIDER_20260731.md
  SHA-256 36b0af8ac990b4ab429d0a4120f453936aeba7f8a4f7bc8fa59157c4ebee49e8
scratch/audit_ad_k17_occ296_c6_localmin_exchange_master_20260731.py
  SHA-256 ceecc941f8486280bf30799fc86bdd72918959ab7dfcd0c5b28701489c18104d
scratch/ad_k17_occ296_c6_localmin_exchange_master_20260731.independent.audit.json
  SHA-256 edb8dcabd9e637974959edd140d4cb5781aa86d3bcd4dddabd5c479c187ed771
  payload 4fe0c70268e1b611f0aa88050993d1c68f648da2bd6f3069cf4d2421e26cb3c2
```

The distinct format/quantifier audit proving why holes and protected losses
must not share one gain-floor bank is

```text
MATH_AUDIT_H3_AD_K17_OCC296_C6_LOCALMIN_INVENTORY_AND_V3_LAST_PROVIDER_GATE_20260731.md
  SHA-256 a4ceb409ebad16f81e57bb0704dcc4069d2389d54912792fd084ed426ab1c797
```
