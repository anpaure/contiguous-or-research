# Exact local coalescence certificate for the integral quaternary cover

Date: 2026-09-07. This is a scoped negative computation, not a lower bound
on the unrestricted integral optimum.

Input: `q4int_final1280_witness_20260906_f7a91.json`, SHA-256
`bbe7dfcd84b4dffebbae82142ed90f90ddda20d8ee4b137a0b62170a14945f36`.
Its 80 explicit chain-pair rectangles cover all 4096 points of `[4]^6`
with principal charge 1280. The original file is unchanged.

## 1. Complete criterion for a containing-product merge

For any finite point family `S subset [q]^d`, put an edge between distinct
coordinate axes `i,j` when some `x,y in S` satisfy

\[
x_i<y_i,\qquad x_j>y_j,
\]

or the reversed inequalities. A coordinate split makes both projections of
`S` strict chains if and only if it is a proper two-coloring of this
conflict graph. Indeed two projected points are incomparable precisely
when a pair of coordinates in the same shore witnesses these inequalities.
Absence of incomparable projected pairs makes that projection a chain.

For a chosen split, the product of the two projections is the smallest
chain-pair rectangle that could contain `S`. Thus testing every split of
the union of two old supports is exhaustive for their possible coalescence
into a single containing chain-pair rectangle. Extra points, new splits,
and nonsaturated chains are all allowed by this criterion.

## 2. Result

All `binom(80,2)=3160` pairs and all 31 unordered nonempty complementary
coordinate splits were tested, for a total of **97,960 exact tests**.
There is **no legal containing-product coalescence at all**, regardless of
charge. Hence no extra cells or subsequent trimming can arise from this
particular two-to-one move on the saved cover.

There is also a short structural certificate for the exhaustive result.
Every coordinate varies in every row's corresponding shore chain. Its
conflict graph is therefore exactly the complete bipartite graph `K_(3,3)`
on its original split: independent choices of the two chain members give
every cross-shore inversion, while chain monotonicity excludes within-shore
inversions. Any containing rectangle must retain that split, up to exchange
of shores.

- 2560 pairs use different original splits. The union of their conflict
  graphs has a triangle, so no split works.
- 600 pairs share a split. Their projected unions fail to be chains on
  both shores in 360 cases, on only the first shore in 120 cases, and on
  only the second shore in 120 cases. Each failed shore supplies an
  internal inversion edge, which forms a triangle with the old `K_(3,3)`.

The companion checker verifies the full cover, coordinate variation,
every pair/split test, and this count breakdown using integer comparisons:

`python3 -B scripts/check_q4_pair_coalescence_20260907.py`

## 3. Private targets also rule out redundancy-financed single-product trades

The test was strengthened to retain only targets that become uncovered
after deleting the chosen rows. Let `mult(x)` be the original global
coverage count and let

\[
P_i=\{x\in R_i:\operatorname{mult}(x)=1\}.
\]

For deletion of one row, the critical set is `P_i`. For deletion of two
rows, it is exactly

\[
P_i\cup P_j\cup
\{x\in R_i\cap R_j:\operatorname{mult}(x)=2\}.
\]

All 80 one-row cases and 3160 two-row cases were tested against all 31
splits, for **100,440 additional exact tests**. There are exactly 80 legal
one-row replacements, each reconstructing its original rectangle at its
original charge. There are no legal two-to-one replacements. No critical
set is empty, so deletion alone does not work either.

The checker certifies a stronger reason: for every row, its private target
set `P_i` already has conflict graph `K_(3,3)` on the original split, and
its projections onto those shores are the **entire** original chains.
Therefore any one chain-pair rectangle containing `P_i` must retain the
original split and contain the whole original rectangle `R_i`.

Consequently, if any nonempty subset of rows is removed and replaced by
one chain-pair rectangle, all their globally private targets must be
restored by that new rectangle. The private-core property forces it to
contain all the removed original rectangles. Section 2 rules this out
when two or more rows were removed, and when only one was removed its
charge cannot decrease. Thus **no many-to-one improving replacement is
possible in this saved cover**, even after ignoring all redundant old
incidences.

This remains a local structural certificate. It does not exclude
two-to-two or larger trades with several new rectangles sharing the old
private targets, altered cover banks, or a completely different integral
construction. No new upper bound is claimed.
