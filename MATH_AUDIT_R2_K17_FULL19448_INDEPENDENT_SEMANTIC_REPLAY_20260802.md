# R2 audit: independent semantic replay of the K17 full-19,448 factor

**Date:** 2026-08-02  
**Status:** PASS for one incidence-only factor: raw-map/model parsing, all
root and owner degrees, the frozen exceptional bank and protected boundary,
all frozen guards, connectivity, every ordinary rank-ten provider row, and
both licensed opened/cyclic seam palettes. This is not a residence,
rank-11-plus, source, compiler, exterior-window, regeneration, or word claim.

## 1. Frozen package

H100 audit root:

```text
/home/amodo/or15/work/r2_k17_fullq1_13_independent_20260802
```

The independently replayed model is

```text
/home/amodo/or15/work/root_k17_fullq1_ordinary_circulation_20260802/
  fullq1_13.best.model
SHA-256 e7ea3841cde04129e3b0af008da0ab2ca2deb8936f09ae22d43a9174ac888a31
```

The verifier does not include or invoke the circulation search source.

```text
source  bdd2d9f36086b7d9be8e314bd05a197fdec133aab2dc6e9fc65da252fcb32427
binary  1a27eaab2e4e06fba9577ad5210e3f13d7560f57a159aabe27b68c19cfe12774
audit   469157e326d7ac75caf742ba68373fe6ceb4e7e72051adfca93c8a658e7599de
stdout  3850f8fe3aa1c5898585dc0ce1b41e6d2896c0df84459ed264b0ccfe603bb4d5
stderr  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
manifest e1f3ba48bd6af8e8b12017e85369174ed30103b455ac7650f16777824e10a32f
```

All entries of `replay.manifest.sha256` pass `sha256sum -c`. The immutable
inputs recorded there include:

```text
incidence map 80980012d7b1449c8ce3932e77ee7e5e47f5d6eb6f18d219687358cbd024355a
global map    d90eda6666629aad49a52247b07068d24d3e8da265f587dae55e864dca223d63
guard bank    e64219c98e4191bbef8e6ba32567cec6286c777755782030fd9cca13669971fc
```

The O3 replay ran on H100 CPU 20 in 0.27 seconds with 48,640 KiB maximum
RSS. No search or solver was launched.

## 2. Independent structural replay

The verifier reconstructed the following directly from the raw maps and
incidence-only model:

```text
rank-8/rank-9 incidence rows       218,790
global incidence rows              218,790
global ordinary-pair rows          875,088
global variables                 1,093,878
selected incidence variables        48,620
selected ordinary pair variables    24,308
frozen clauses                       16,261 / 16,261 satisfied
incidence components                      1
ordinary contracted edges            24,308
ordinary contracted components             2
```

Every ordinary rank-eight root has degree two, `M` has degree one, `D` has
degree three, and every rank-nine owner has degree two. Protected variables
`M--B=10` and boundary-core variable `73` are selected. The exceptional
banks are exactly

```text
M owners  [511]
D owners  [8447,33023,65791].
```

## 3. Full ordinary immediate-upper palette

The 24,308 ordinary diamonds give the exact provider histogram

| multiplicity | rank-ten targets |
|---:|---:|
| 1 | 15,128 |
| 2 | 3,816 |
| 3 | 471 |
| 4 | 30 |
| 5 | 3 |

Thus all `19,448/19,448` rank-ten targets are covered by ordinary roots
alone, with no missing mask. This splits as all 19,412 non-`D` targets and
all 36 `D`-superset targets. The occurrence checksum is

```text
15128 + 2*3816 + 3*471 + 4*30 + 5*3 = 24308.
```

## 4. Licensed seam replay

Ordinary rethreading changed the semantic tail role even though the selected
`D` incidence bank stayed fixed. In the terminal model the unique `M`-to-`D`
tail enters through owner `8447`, not through the q1-zero checkpoint's owner
`33023`. The independently reconstructed orientations are:

| orientation | start | return | internal colour | closing colour | ordinary multiplicities |
|---:|---:|---:|---:|---:|---:|
| 0 | 33023 | 65791 | 41215 | 66047 | 1, 1 |
| 1 | 65791 | 33023 | 73983 | 33279 | 1, 1 |

Both opened palettes cover `19,448/19,448`, and both cyclic palettes cover
`19,448/19,448`. The seam occurrences are redundant providers in this
ordinary-complete model. The reconstructed tail has 5,035 bipartite vertices
and the complementary `D` cycle has 43,586, agreeing at their single `D`
vertex with the 48,620-vertex connected factor.

## 5. Fail-closed correction retained

The first audit version incorrectly fixed the q1-zero tail owner `33023`.
It failed after the map, degree, guard, connectivity, and ordinary-palette
checks with

```text
FAIL unexpected authenticated tail owner
```

No construction defect was involved: ordinary circuits can change which
fixed `D` neighbour has the tail role. The failed source, binary, stdout,
stderr, timing, and exit code remain frozen under
`replay_v0.manifest.sha256`, SHA-256
`33421eff36931708465c35a748592443aa2fbd173e38200c1102183fa21b7c10`.
The successful verifier derives the tail and seam colours from final
topology and makes no inherited-role assumption.

## 6. Exact scope

This audit independently closes full immediate rank-ten coverage inside the
specific connected guarded `h=1` factor, without exceptional-provider
recourse. It does not establish positive residence, any rank 11--17 deck,
source antecedents, a lower or terminal compiler, opening exterior windows,
regeneration, a universal word, or `nu(17)=24313`.
