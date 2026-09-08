# `k=17` cyclic-SCD depth-three first factor: exact balance and the state-Hall gap

**Date:** 2026-08-01  
**Status:** exact finite calibration of the cyclic-quotient selector theorem.
It constructs one literal quotient chain forest, verifies complete high
target offers and exact rail balance, and then audits its representative
state graph.  The chosen factor fails statewise Hall.  This is not a no-go
for other quotient SCDs, matchings, representative alignments, or the full
common master.

## 1. Construction

For `k=17,m=8,d=3`, rotation is free on every nontrivial rank.  The quotient
rank sizes needed here are

\[
 |N_6|=728,\qquad |N_7|=1144,\qquad |N_8|=1430.
\]

The audit builds the simple quotient containment graphs and computes:

1. a matching saturating all `728` rank-six necklaces into distinct
   rank-seven necklaces;
2. a matching saturating all `1144` rank-seven necklaces into distinct
   rank-eight root necklaces;
3. coherent first literal rotations on every matched containment;
4. arbitrary least-label unmarked continuations on the `416` rank-seven
   chains without a rank-six child and the `286` root chains without a
   rank-seven child.

Translating each resulting flag through all 17 rotations gives one flag per
named rank-eight root.

## 2. Exact selector and balance replay

The replay reports

```text
orbits r6=728 r7=1144 r8=1430 match67=728 match78=1144
offers miss7=0 miss6=0 hist=1 H=1430
```

Thus every rank-seven and rank-six necklace is offered, and every coordinate
appears exactly `1430` times in both deletion positions.  Because the action
is free at ranks six and seven, marking the matched offers gives every named
target once.  This is a literal finite instance of the cyclic-SCD selector
and full depth-three rail-balance theorem.

## 3. Representative state graph

Rotate each tail flag uniquely so that its second deletion is coordinate
zero, and each head flag uniquely so that its first deletion is zero.  Build
the exact legal-turn graph `G_0` using the all-high shift law, with edges
coloured by rank-nine owner necklaces.  The result is

```text
G0 edges=3836 zeroL=246 zeroR=124 matching=1010
matched_colors=818 color_collisions=192
```

So this deterministic factor fails before owner rainbow: `246` tail flags
and `124` head flags are isolated, and maximum matching is only `1010` of
`1430`.  An arbitrary quotient chain forest and first representative
alignment therefore do not supply the remaining theorem.

The exact free choices are substantial and remain open:

* the two quotient containment matchings;
* every physical rotation realizing a quotient containment;
* the second deletion on `416` one-level chains; and
* both deletions on `286` entirely unmarked roots.

Co-designing those choices with `G_0` Hall and the owner colours is exactly
the quotient-rainbow gate.  The current common-first finite factors explore
a broader age/type family and are not refuted by this calibration.

## 4. Artifacts

* generator/auditor:
  `scratch/build_audit_k17_quotient_scd_d3_state_graph_20260801.cpp`,
  SHA-256 `aba66f7eab0d9fd1fcdb361c053a885d213f6950ef4b86545c170a350ea7b48f`;
* selected quotient flags:
  `scratch/k17_quotient_scd_d3_first_factor_20260801.tsv`,
  SHA-256 `0d468fe4613079f0dc6e5954bbafb18a2ecd5623534f2391cbe60035dce2d33d`;
* H100 O3 output:
  `scratch/k17_quotient_scd_d3_first_factor_20260801.audit.txt`,
  SHA-256 `9b65d3f7351b94faea0a04e4c169f7b2cca465a756abf0dc5859898cead5d62b`.

The run is deterministic and solver-free.  It proves only the displayed
factor's failure; no search over quotient matchings or alignments is claimed.
