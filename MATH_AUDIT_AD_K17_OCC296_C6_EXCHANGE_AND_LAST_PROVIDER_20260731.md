# Independent audit: occ296+C6 exchange catalogue and last-provider master

Date: 2026-07-31  
Status: **PASS for the exact marked-preserving factor/rank10 scope; not solved**

## 1. Scope

This note audits the superseding `occ296+C6` package without running CP-SAT.
The audit reconstructs the marked/complement split from the authenticated
physical carrier, parses every record in the custom binaries, independently
regenerates every exchange column, checks both sparse rank10 sidecars, checks
all rank10--12 baseline interval loads, checks the evaluator seed, and replays
the empty-selection literal chronology.

The exact hard stage is:

- preserve the 4,108-owner marked path and its two cross edges;
- choose one edge for every complement-internal lower colour;
- preserve degree two at every complement owner;
- preserve every boundary-correct linear rank10 target; and
- impose one-cycle connectivity by exact lazy cuts.

Ranks 11/12, residence, inverse replay, and common-cap Hall remain literal
post-connectivity gates.  No feasibility or K17-word claim is made.

## 2. Frozen package

The current source quartet supersedes the earlier concurrently written
versions.  The audited hashes are:

| artifact | SHA-256 |
|---|---|
| builder | `5062777925ea924f90e79ef6f024ab44393867a8b24d681a5d19a57cfc9ad00e` |
| wrapper | `62a057c44da61eedc45a985e6d854e2dc459fcc9f31a453446215b8b8b8a0da3` |
| generic core | `6ecf1cf02cb3791333816b058ceb1e415331274d8bc4e2dcde93ea4e87c89a1e` |
| metadata | `dc4fc767f015a5618e8c89a2c81312b01821ec99e5238ea2029915cb6cf9423c` |
| validate JSON | `df4063fe11774b662a201fd80653f2a91aa8a6b2f2a129fb47a6d9ab8d9a62a1` |
| complete catalogue binary | `f07bab5342ecf376039cc0359559e6366ad62987dc4f556668a91f2d7b387bc3` |
| absent-rank10 service index | `ec2a03c16bdacd82fcc98682efeea503506c1b9be11f80674e23533c73098d08` |
| vulnerable-last-provider index | `cac1fe10e4c2c4d49436252e6ac3e8a6d2b705ec9ec68f1e07949f130667c6a8` |
| rank10--12 guard loads | `f6250f930b9de74706c2cb14c4e8c34cd21794200fc8bf682b643ff2cf07cc59` |
| evaluator seed v2 | `cdcbb96057049e4f4906db343ac73810be9ff8ed4ab49f4f620efbcb6490e3d9` |
| empty-selection evaluation | `65655e7e2383020c6575bbfaf6cbe59fa1baeaa9af96531aae85a83f3a10a31e` |
| literal evaluator source | `037ad2f0a4ec332b7ccbfdfba05730a10f1ed1f86091905f45a3c8bef35cbc60` |
| authenticated owner cycle | `a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49` |

The metadata payload is
`d57a9737508e17f3f294d14403cfd43bdb7e0b0806de91d36e338736c037b6bc`;
the validate payload is
`207545fa16f95c65b32d0475633513f065daa04f3917c43ddca13f2aa6a4c43c`.

## 3. Physical base and fresh relative catalogue

Rotating the authenticated owner cycle by 21,331 puts the marked bank first.
Literal replay gives:

| quantity | value |
|---|---:|
| rank9 owners | 24,310 distinct |
| marked owners | 4,108 |
| complement owners | 20,202 |
| marked-internal edges | 4,107 |
| cross edges | 2 |
| complement-internal edges/colours | 20,201 |
| distinct rank8 edge colours | 24,310 |

For a complement-internal rank8 colour `c`, let `e_c={a_c,b_c}` be its
incumbent edge in this C6 carrier and let

`V_c={v outside the marked bank : c subset v}`.

Every admissible marked-preserving replacement is exactly one pair from
`binom(V_c,2)-{e_c}`.  Parsing the binary and comparing every stored endpoint
against a fresh enumeration verifies all 20,201 groups and all 545,721
off-source columns.  The fresh column stream hash is

`a0d5efb22115745fab920bd26215a8cbc8ac2b711f0a14834f6a03a189f2bed5`.

The `|V_c|` profile is unchanged as a dimension count,

| `|V_c|` | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| groups | 15 | 129 | 454 | 1,601 | 3,836 | 6,748 | 7,418 |

but the excluded incumbent pair and hence the column IDs are C6-relative.
No occurrence-only column or old source delta is reused.

## 4. Boundary-correct rank10 reduction

For a connected factor, orient its unique cycle through the frozen marked
path and write its nonflat row as marked rank9 owners followed by the rank8
facet rail.  Exactly as in the general zipper lemma, its rank10 interval set
is the set of owner-edge unions after omitting the closing cross edge.

If `p(S)` is the number of exposed owner edges with union `S` and `i(S)` is
the number of literal rank10 intervals with union `S`, the canonical-witness
argument proves `p(S)>0` iff `i(S)>0`.  It does **not** prove multiplicity
equality: at the marked/facet boundary an interval can acquire an inert facet
without acquiring another adjacent canonical witness.

The independent frozen-source census separately verifies exact singleton-set
equality, `p(S)=1` iff `i(S)=1`.  The boundary exception is harmless here:
`[P_4107,P_4108]` extends through the first facet with unchanged union
`0x14776`, but that target already has exposed provider `P_4106P_4107`.
Also, the closing union `0x11cfa` has two cyclic edge occurrences but exactly
one exposed provider and one literal interval provider; only the closing edge
occurrence is omitted.  The canonical exposed load profile is

| load | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|
| targets | 12,196 | 4,948 | 662 | 54 | 3 |

The guard binary's rank10 interval loads may be larger than canonical loads,
but its 12,196 singleton targets are exactly the same targets.  This is the
required last-provider identity.

## 5. Exact signed equations

Let `x_(c,f)` select replacement edge `f` for lower colour `c`, and let `y_c`
mean that incumbent `e_c` is deleted.  The frozen generic core uses exactly

`sum_f x_(c,f) = y_c`,

the complement-owner degree equations, and for every rank10 target `S`,

`p_0(S) + sum_(c,f: union(f)=S) x_(c,f)
        - sum_(c: union(e_c)=S) y_c >= 1`.                            (R_S)

Every one of the 545,721 exchange variables occurs positively in exactly one
row, every one of the 20,201 changed-colour variables occurs negatively in
the row of its old union, and all 19,448 base loads were independently
recomputed.  A canonical independent serialization of these row semantics
has SHA-256

`f11a927a07ea1aeda37cfceea36a3142beb6fa188dafb794cbebf7c5f5d7ce52`.

Equation `(R_S)` is exact, including last-provider losses; it does not merely
ask that every initially absent target gain a provider.

## 6. Absent-target service sidecar

The C6 base has 1,585 absent rank10 targets.  Parsing the complete service
binary verifies:

- all 1,585 target masks in sorted numeric order;
- all 54,307 provider references;
- every referenced column's literal new union;
- completeness against all 545,721 columns; and
- support range 10 through 45.

Because one selected edge has only one rank10 union, every completion selects
at least 1,585 columns.  This is only a gain floor; owner balance,
connectivity, and losses of old targets still matter.

## 7. Vulnerable-last-provider sidecar

Among the 12,196 singleton rank10 targets:

- 2,826 have their sole provider on the frozen marked/cross bank and cannot be
  lost in this face;
- 9,370 have their sole provider on a mutable complement source edge.

For each vulnerable target `S`, the protected sidecar stores its unique
source group `g(S)` and every restoring column.  All 9,370 source IDs and all
289,011 restoring references were checked against the full catalogue.  The
exact sparse row is

`sum_(f: union(f)=S) x_f - y_(g(S)) >= 0`.                           (P_S)

This is precisely `(R_S)` with base load one.  It has no unconditional gain
floor: if the source is retained, no restoring column is needed.

The restoring-support range is 0 through 44.  Exactly one target has no
restoring column:

`S = 0x1c0df = 114911`.

For this target `(P_S)` becomes `-y_(g(S))>=0`; hence its incumbent source
edge is rigorously forced kept in every rank10-complete solution.  This is a
theorem of the stated marked-preserving exchange face, not a search
observation.

The protected sidecar is a compact projection of the already complete
19,448-row master.  Pinning it in the wrapper does not introduce a stronger
feasible-set restriction.

## 8. Full rank10--12 guard-load binary

The guard binary explicitly stores a load, including zero, for every target:

`C(17,10)+C(17,11)+C(17,12)=19,448+12,376+6,188=38,012` rows.

All rows were replayed from 134,403 monotone interval extensions.  Exact
headline counts are:

| rank | covered | holes | singleton intervals |
|---:|---:|---:|---:|
| 10 | 17,863 | 1,585 | 12,196 |
| 11 | 11,552 | 824 | 4,448 |
| 12 | 6,072 | 116 | 772 |

The complete load profiles and singleton-set hashes agree byte-for-byte with
the metadata.  In particular:

- rank10 singleton payload:
  `1dd9809b449821eefe6158dfc70ed7e9f581906b3da96aa86dd3acd2764bf540`;
- rank11 singleton payload:
  `c8cf059ab075abd9cc52a5b45e360743c37251038f451aaea935e7ff3bb3a029`;
- rank12 singleton payload:
  `b965ca90c57dde9a3b7fba479899599ae88bf77080189803130fdd47a7d7ab0c`.

### Scope correction

For rank10, the owner-edge reduction makes provider gain/loss additive and
the protected rows exact.  For ranks 11 and 12, the guard binary is an exact
**baseline multiplicity ledger only**.  It does not record a context-free
delta for a single exchange and it does not identify an exchange-independent
survivor.  Multi-edge rethreading changes the final order, so last-provider
survival at those ranks must be checked on the literal connected chronology.
Treating load greater than one as automatic safety under arbitrary compound
selection would be unsound.

## 9. Seed and empty-selection evaluator

The version-2 seed was independently parsed and verifies:

- carrier SHA `a47aa9d7...`;
- rotation 21,331;
- dimensions 24,310 / 4,108 / 20,201 / 545,721;
- the exact 1,585 rank10 target IDs;
- service census 54,307 with support 10--45;
- D2/D3 counts 503/503;
- zero empty envelope, 748 replay mismatches; and
- upper holes 1,585/824/116.

Its payload SHA is
`7353f5f9389fe1493a901e832b3912b1d202bc83543cdcfb5168f41bec2bc6fa`.

The empty-selection evaluator output independently replays one cycle, exact
lower-q1, and the same literal chronology:

| metric | value |
|---|---:|
| D2 short runs | 503 = 230 length1 + 273 length2 |
| D3 short runs | 503 = 230 length2 + 273 length3 |
| inverse mismatching rows / missing bits | 748 / 776 |
| empty envelopes | 0 |
| host redundancy | 252,803 |
| envelope volume / minimum size | 150,224 / 6 |
| rank10/11/12 holes | 1,585 / 824 / 116 |

Its owner-order LE32 hash is
`901944ed239ce95ae2ea849a882382ffb83fc813532f506fd754fa48211fa652`,
and its Z-row LE32 hash is
`5fc594d3f04f30c730633d3f587360cf36101bff07eb63fe7a2e3118c44624f2`.

Common-cap matching is explicitly `UNSOLVED`; the evaluator reports only the
scalar slack pre-guard.

## 10. Wrapper validation

The validate JSON has status

`PASS_INPUTS_AND_LITERAL_SPLIT_BASES_VALIDATED_NOT_MODEL_BUILT`.

This exact label is appropriate.  Validation authenticates the C6 base and
regenerates the 545,721-column stream.  It supplies no split columns, builds
no CP model, and proves no feasibility statement.  The wrapper hashes the
new protected sidecar, guard ledger, seed, evaluator, C6 residual, and owner
cycle before delegating to the frozen generic core.

The hard rank10 equations are the full equations `(R_S)`; the service and
protected binaries are compact external indexes and are not silently used as
weaker substitutes.

## 11. Exact remaining boundary

Proved and complete in this face:

1. all 545,721 C6-relative marked-preserving lower-colour exchanges;
2. exact lower palette and owner-degree equations;
3. all 19,448 signed rank10 equations, including losses;
4. all 54,307 absent-target provider references;
5. all 9,370 vulnerable singleton rows and the forced keep at `0x1c0df`;
6. exact lazy one-cycle cuts; and
7. exact literal post-materialization evaluation.

Still unsolved:

1. an integral degree-balanced, connected rank10 completion;
2. simultaneous rank11/rank12 survival and service;
3. zero D2/D3 and exact inverse replay; and
4. common-cap Hall and the final compiler.

## 12. Independent artifacts

- verifier:
  `scratch/audit_ad_k17_occ296_c6_localmin_exchange_master_20260731.py`,  
  SHA-256 `ceecc941f8486280bf30799fc86bdd72918959ab7dfcd0c5b28701489c18104d`;
- audit JSON:
  `scratch/ad_k17_occ296_c6_localmin_exchange_master_20260731.independent.audit.json`,  
  SHA-256 `edb8dcabd9e637974959edd140d4cb5781aa86d3bcd4dddabd5c479c187ed771`;
- audit JSON payload:
  `4fe0c70268e1b611f0aa88050993d1c68f648da2bd6f3069cf4d2421e26cb3c2`.
