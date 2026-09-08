# Exact K17 mixed `C6+C18` strict-clean escape

**Date:** 2026-08-02  
**Status:** complete fixed-base disjoint mixed-pair census; independently
replayed positive witness

## Result

The authenticated quotient carrier with residence defect `1,581` and deep
holes `(1462,255,0)` has exactly:

- `73` individually rank-10-cap-safe quotient `C6` circuits;
- `6,860` individually rank-10-cap-safe quotient `C18` circuits.

All

\[
73\cdot 6860=500{,}780
\]

mixed pairs were partitioned over eight shards and replayed.  The exact
census is:

| gate | count |
|---|---:|
| all mixed pairs | 500,780 |
| shared quotient facet | 24,105 |
| combined cap failure | 5,103 |
| exact residence non-improvement | 471,403 |
| retained-path topology failure after strict improvement | 136 |
| strict-residence, one-cycle pairs | 33 |
| rank-13--16 failure among those pairs | 0 |

Every one of the 33 survivors received an independent literal one-cycle
replay, exact positive-run recount, and complete cyclic rank-11--16
interval-union recount.

The best strict-clean carrier has:

\[
\text{residence}=1547,
\qquad
(h_{11},h_{12},h_{13})=(1513,272,0).
\]

It retains all rank-8 owners/facets, all rank-10 caps, all 3,944 protected
edges, one physical owner cycle, and complete ranks 13--17.  Its exact
row/middle diagnostics are `Phi=48,380`, `G2=120`; this gate still fails.

A second Pareto carrier has residence `1,564` and deep holes
`(1462,238,0)`.  It is useful because it improves rank 12 while preserving
the former rank-11 floor.

## Authentication

- complete mixed audit SHA:
  `634fcfff7b5bf229dd74a55b30882e1adc77af6925552d5ec74d2a14c3392cd5`;
- clean-1547 model SHA:
  `fb1c96c33964006ad3eec1f71550a7d033724c3508dbec54c7f3dc8bb9961ef5`;
- clean-1547 factor SHA:
  `165664c5e27cf1c3e67c387fa8e08e2576bd64ea06c13340c18a16db8de9eee0`;
- balanced-1564 model/factor SHAs:
  `35b8f9dd4287c336584ab54b8341e7a3cd1e394086fb0848cb405d6089827c9d`,
  `a56ea34a57c05f2993c6999ad2b1f9fde79089dfd8bd94b08e0e4b784329ad7a`;
- canonical blocker union through both Pareto models: 706 clauses, SHA
  `549c9aed6dc3306a580129800251f3b47316e29c4a6d777c60d086628d06c14a`.

The catalogue, pair scorer, and shard aggregator are respectively:

- `scratch/catalogue_k17_c18_cap_safe_paths_20260802.cpp`, SHA
  `f3ab5947873173b1f0095b13fa5c93bc5ed909206c48b2285a1c5df3468f621c`;
- `scratch/search_k17_c18_pair_strict_clean_20260802.cpp`, SHA
  `aded34497cfb29826ab4ae7d9337c4037f5855a3208d14fa9d6702592a1c83c5`;
- `scratch/aggregate_k17_c18_pair_strict_clean_shards_20260802.cpp`, SHA
  `4c79aa0cf1237242942af5f0d86cd044dfcef83c4daa8f61c25fe76dbeac6eeb`.

## Scope

This is exact only for disjoint `C6+C18` pairs on the fixed residence-1,581
quotient carrier.  Pairs sharing a quotient facet, triples, other mixed
lengths, non-equivariant physical moves, linear openings, source
factorization, and the lower compiler are not covered.  No K17 word or new
upper bound follows yet.

