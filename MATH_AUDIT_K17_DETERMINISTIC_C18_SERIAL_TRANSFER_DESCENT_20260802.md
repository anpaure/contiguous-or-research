# Deterministic K17 quotient `C18` serial-transfer descent

**Date:** 2026-08-02  
**Status:** exact fail-closed serial phase; latest promoted Pareto carriers

## Deterministic phase rule

For a frozen connected quotient carrier, the `C18` phase is:

1. enumerate every simple quotient circuit of length nine in a modulo-root
   partition;
2. retain only exact rank-10-cap-safe circuits;
3. develop every circuit through all 17 rotations;
4. replay literal component topology and positive coordinate runs;
5. for every connected candidate, independently recount the complete cyclic
   rank-11--16 interval-union deck;
6. accept only a candidate with residence no worse, lexicographically better
   deep holes, and zero holes at ranks 13--16;
7. promote the deterministic lexicographic minimum
   `(residence,h11,h12,blocker_score,residence_deficit)`;
8. extract the current necessary residence blockers and canonically union
   them with the inherited sound bank;
9. repeat.  If there is no accepted single, test only exact unions of
   accepted complementary/blocker-delta rows; if none passes, stop and return
   control to the non-`C18` driver.

Every transfer row records exact cap current, physical component sizes,
run-2/run-3 counts, canonical removed/created blocker keys, all changed
facets/options and old/new quotient edges.  The circuit scorer independently
checks its incremental upper accounting against a full literal recount and
fails closed on disagreement.

The source is
`scratch/extract_k17_circuit_transfer_signatures_20260802.cpp`, SHA
`7a8483cf712d0fac7bab2f1a28a0e82ffdfdc7083d4af2ca0e3e097a6a9cdd6b`;
the H100 `-O3` binary has SHA
`ec51a6f8544a1179d8c14c379ae0d75c74652830295a49731944a318f39f44d7`.

## Exact descent chain

The following rows are independently literal-replayed promotions.  All have
one physical owner cycle, every rank-8/9/10 resource, all 3,944 protected
edges, and no rank-13--17 holes.

| state | residence | rank-11 holes | rank-12 holes | missing orbits 11/12 |
|---|---:|---:|---:|---:|
| non-`C18` clean base | 1,513 | 1,496 | 238 | 88/14 |
| one `C18` | 1,513 | 1,479 | 238 | 87/14 |
| second serial `C18` | 1,513 | 1,462 | 238 | 86/14 |
| non-`C18` residence base | 1,496 | 1,496 | 238 | 88/14 |
| exact complementary `C18` pair | 1,496 | 1,462 | 221 | 86/13 |
| next serial `C18` | 1,496 | 1,428 | 221 | 84/13 |
| non-`C18` residence base | 1,479 | 1,479 | 238 | 87/14 |
| exact complementary `C18` pair | 1,479 | 1,462 | 221 | 86/13 |
| next serial `C18` | 1,479 | 1,445 | 221 | 85/13 |
| joint all-three-gate `C18` | 1,462 | 1,428 | 204 | 84/12 |
| next serial `C18` | 1,462 | 1,411 | 204 | 83/12 |
| non-`C18` depth-four packet | 1,394 | 1,479 | 170 | 87/10 |
| `C18` rank-11 repair | 1,394 | 1,445 | 170 | 85/10 |

The joint step is particularly informative: one cap-safe connected circuit
removed exactly one full orbit from each of residence, rank 11 and rank 12.
Thus the three defects are not locked into mutually exclusive basins.

Several patches recur unchanged after unrelated non-`C18` promotions.  The
complementary rows also compose exactly: on the residence-1,479 base the two
accepted singles separately give `(1462,238)` and `(1479,221)`, while their
literal union gives `(1462,221)` with the same residence.  This is an
authenticated defect-transfer mechanism, not merely a score correlation.

## Current imports

The strongest current sum-defect score is:

`/home/amodo/or15/work/qa_k17_joint1394_c18_transfer_20260802_quotientaudit/promoted_c18_rank11`

- model SHA
  `740f74f99b429aacc204b5d17fc3753988874786a330e1f9bddf4045ed164c38`;
- factor SHA
  `0dc63730368aaffb6ee4b140378b15f03d3b8d452d9bd49456a5c362e97406d7`;
- metrics `residence=1394`, deep holes `1445/170/0`;
- missing target orbits `85/10` at ranks 11/12;
- current residence-blocker orbits `82`;
- cumulative sound bank: 731 clauses, SHA
  `7e9459a4351450213036ce708a4c9c7aa8cb0cc7c3d340361164f49a1f459d7b`.

The strongest rank-11 Pareto import is:

`/home/amodo/or15/work/qa_k17_joint1462_c18_transfer_20260802_quotientaudit/promoted_c18_rank11`

- model SHA
  `211fe774bbc53790da79908510dbe4574a58825aeedd13feb3bc8641ab72578e`;
- factor SHA
  `0a1037f2148b00bf18d273b3be80792eecd5ecb616222f4eb838f5f01a00b677`;
- metrics `residence=1462`, deep holes `1411/204/0`;
- missing target orbits `83/12` at ranks 11/12;
- current residence-blocker orbits `86`;
- cumulative sound bank: 726 clauses, SHA
  `8c4dd30dffbe7df4d13cb6cf9da8cfb2b69ffc3f2cce9f6d43c9497c4ca107ea`.

The preceding all-three joint import, used by the separate non-`C18`
residence driver, is:

`/home/amodo/or15/work/qa_k17_clean1479_c18_transfer_20260802_quotientaudit/promoted_c18_serial3_joint`

with model/factor/bank SHAs
`68a4682097bfbeb5cf4cefe30826076283aad447025e675941c006b407c97652`,
`7e8cd432f16bc700c6a940b62a7aef942cab1815aa40b561f48b7ddc02cf5028`,
and
`9240ede17b9c54dd503177ec1d36a6bae9ac085311a19e1dbcc307bd32ef2caa`.
Its metrics are `1462/1428/204/0`.

## Transfer authentication

Representative complete transfer tables/audits are:

- residence-1,513 base: TSV SHA
  `424c616ddf9055e0acf6f01b96e5618c6ed677e4ec93b60109c72bdfc54ac90c`,
  audit SHA
  `67dd423334ec300c01708e9f2eacfb98242ce78856093540d5a28c652400981e`;
- residence-1,496 base: TSV SHA
  `1d8bb8c93ea75762c869e669a93fd452f2f174c7eb990e0850185506cb235721`,
  audit SHA
  `8a1267c3e0722fb495e86c22c427efb721222f2cdf733d5bcd8373deb93be6ad`;
- residence-1,479 base: TSV SHA
  `59c1e9d6072fee82d659df2ff20d41de6eef3cf0825bbfa18202caf27cfa713d`,
  audit SHA
  `2e341240a20a9d7c378a650a23b097c06e85c273e37fbebb980ab33ad6eb7917`;
- joint `1462/1428/204` base: TSV SHA
  `66fc40ac21048f1ee0803f1d261a46789cb8aa08ad52da4925f0537f283def9a`,
  audit SHA
  `614eafd8029ab071f2d0b1fb914407e8691c03c793fbed970e928b1862e40824`.
- residence-1,394/deep-1,479/170 base: TSV SHA
  `a8e457cf5367a56a6a71d829c8471f26056d61193ab959f11d6e912ac7851f59`,
  audit SHA
  `f2c2ec2f83eb9f935ad89b2834ee8e1be9d7717c78bfe30abc8c77b0d73bd3c7`.

## Scope

This is a quotient-carrier descent theorem for the enumerated `C18` phase.
It does not prove termination at zero, cover overlapping-facet or general
higher-order packets, construct a source antecedent, solve the lower
compiler, or produce a K17 word.  Consequently it gives no new numerical
upper bound for `nu(17)` by itself.
