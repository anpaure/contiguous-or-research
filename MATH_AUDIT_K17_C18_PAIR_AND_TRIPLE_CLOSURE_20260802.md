# Exact K17 `C18+C18` pair census and Pareto triple closure

**Date:** 2026-08-02  
**Status:** complete fixed-base pair census; independently replayed triple

## Pair census

The base is the authenticated quotient carrier with residence defect `1,581`
and cyclic upper holes `(1462,255,0)` at ranks 11--13.  Its individually
rank-10-cap-safe `C18` catalogue contains `6,860` circuits.

All

\[
\binom{6860}{2}=23{,}526{,}370
\]

disjoint-pair candidates were partitioned over 32 exact shards.  Aggregation
gave:

| gate | count |
|---|---:|
| all unordered pairs | 23,526,370 |
| shared quotient facet | 4,579,724 |
| combined cap failure | 1,242,625 |
| exact residence non-improvement | 17,703,249 |
| retained-path topology failure | 657 |
| strict-residence, one-cycle pairs | 115 |
| rank-13--16 failure among those pairs | 5 |
| exact candidates | 110 |

The complete three-object Pareto frontier `(residence,h11,h12)` consists of:

| circuit pair | residence | rank-11 holes | rank-12 holes |
|---|---:|---:|---:|
| `3559+4171` | 1,530 | 1,496 | 272 |
| `6559+6777` | 1,547 | 1,479 | 238 |
| `4171+4192` | 1,564 | 1,445 | 221 |
| `2327+4171` | 1,564 | 1,530 | 204 |

Every listed carrier has one physical owner cycle and no holes at ranks
13--17.

## Exact small triple closure

The two Pareto pairs `3559+4171` and `4171+4192` share circuit `4171`.
Literal replay of their union gives the cap-safe connected triple

\[
\{3559,4171,4192\}:
\quad
(\mathrm{res},h_{11},h_{12},h_{13})=(1530,1479,255,0).
\]

It strictly dominates the former clean pair `3559+4171`.  The bridge role of
`4171` is physical rather than cosmetic: `3559+4192` alone has the same cap
coverage but is disconnected, while adding `4171` reconnects all retained
paths into one cycle.

All other unions of Pareto pairs sharing `4171` were replayed:

- `3559+4171+2327` is connected with
  `(1530,1564,238,0)`;
- `4171+4192+2327` is disconnected;
- `3559+4171+4192+2327` is disconnected.

The promoted natural triple has exact row/middle diagnostics
`Phi=48,356`, `G2=132`, and missing target-orbit counts `87/15` at ranks
11/12.  It still fails the row/middle gate and is not a K17 construction.

## Authentication

- complete pair aggregate audit SHA:
  `d4f6bdb34c7c8196b05accce39ce44a057fe506209c66040cd8abc159bfda5eb`;
- all exact pair candidates SHA:
  `271e6527db294e337403ee3d9d4509896821cfc012f31dcdf135323f58401049`;
- exact pair Pareto table SHA:
  `dc065363e1a1a52e56a60cd68242f8142cd8eeb92e9594e8c08df32d685cb396`;
- promoted triple model/factor SHAs:
  `9efed5fa7e43989017e16306052436e8137a7f74e30be81560ad9aa5a2e3be85`,
  `b917ae257e22100459b9475ad4aa3127419685ed0ae3344f2b886127a72122b9`;
- promoted triple patch SHA:
  `d30a4f02660531d9d866cc139a828c4a8431c04151e8fbabd09474c93d46ce93`;
- promoted triple deep/orbit/Phi audit SHAs:
  `d851ff15d76a41615419190dca96df45846086cfb13960841cdfb31cff550c1d`,
  `38729a9a37e3b29d3ccfe7692e425572ec39557e4583962cb3ce76c222ec44fa`,
  `389b4f58faaf7218a836fcf7108edcae3396fb8b3d1b01f7827653c4f4f85201`;
- canonical blocker union through the triple: 709 clauses, SHA
  `8490161da10619c5e6f8273f0be5dafa981616782ebaf8b75eacf23db5a6164c`.

## Scope

The pair census is exact only for disjoint pairs from the fixed-base
individually cap-safe quotient `C18` catalogue.  The small closure census is
exact only for the explicitly listed Pareto unions.  General triples,
overlapping-facet trades, other lengths, non-equivariant moves, linear
openings, source factorization, and the lower compiler are outside scope.
No word or improved K17 upper bound follows.
