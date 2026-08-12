# K17 OPTIMAL28 occurrence-greedy296: independent connected full replay

Date: 2026-07-31  
Status: **PASS, exact source-relative audit**

## Scope

This note authenticates the `occurrence_greedy296` OPTIMAL28 checkpoint from
primitive data.  The audit does not import or call either root materializer.
It reconstructs the nonflat macro forest from the K15 parent and the selected
physical q2 occurrences, replays the frozen marked packet and corrected
residual b-flow, expands the literal owner cycle, and independently computes
the two-bank Z row, maximal envelope, residence defects, and shadow ledgers.

It does **not** construct a common-cap assignment, lower compiler, K17 word, or
claim about `nu(17)`.

## Authenticated checkpoint

- occurrence flow: `scratch/k17_opt28_occurrence_greedy296_verified_20260731.flow.json`
  - file SHA-256 `079f5cd96f713ef2d72dd43acff10f84416acdb670aeff96f61a3cb97f29c25f`
  - payload `fed50b14fda074d87f5fc610b9c529550a9e2a85f550bc6a298bc8b4fd561cb4`
- corrected residual: `scratch/k17_opt28_occurrence_greedy296_connected_bflow_v2_20260731.json`
  - file SHA-256 `63b49db80ad983bcd440aba3ac4b449888e30dea2d3c83e140e15b07082f69d0`
  - payload `dcb06a14d12db49bca53b95e9317786c8c7d751323a4104956ed053140976660`
  - residual-row payload `327d60f1f1d072b3bcb60e84404e52f346e25a98499fcf688fde842cddf67a8c`

The earlier residual file has SHA
`c32349f7f962d69b23191e26b0f86aea1afab1d14fdfaf9ceb5ac25b626050e7`
and pins a pre-finalization flow SHA `55f8af1f...`.  The v2 sidecar corrects
that pin to `079f5cd...`; its 4,872 assignment rows and their payload are
exactly identical to the earlier file.  The independent audit also checks
every residual row directly against the finalized forest.

## Reconstruction

From the authenticated K15 parent, the audit recomputes all 5,005 rank-six
q2 colours and their occurrence profile

`1^3630 2^1320 3^55`.

The selected occurrence transversal retains 5,005 distinct physical edges
and deletes 1,430.  The induced three-shore graph decomposes into exactly
1,430 X-to-Y macro paths with 19,305 distinct tagged rank-nine owners.  Their
old-rank-eight port graph is an acyclic 5,005-component forest.  Every macro
node path, endpoint, owner word, component macro set, component word, marked
flag, and stored D2/D3 count agrees with the frozen flow.

The 106 marked components plus 28 optional components are byte-literally
unchanged from the OPTIMAL28 packet face.  Replaying its 105 candidates gives
133 distinct packet U owners and the same 4,108-owner marked path, with no
strict D2 or D3 defect.

The corrected residual supplies 4,872 remaining old-U owners and 9,744
incidences.  Its load equals the recomputed port demand exactly:

`demand 0^615 1^1896 2^3924`.

Together, 1,430 macros and 5,005 U objects give degree two at every one of the
6,435 old-rank-eight ports and one object cycle.  Literal expansion has 24,310
distinct rank-nine owners and 24,310 distinct rank-eight Johnson
intersections, hence both palettes are exact.

## Exact ledgers

| ledger | independently replayed value |
|---|---:|
| occurrence changes from fixed skeleton | 196 |
| component-interior short-run tax | 724 -> 296 |
| components carrying that tax | 257 -> 157 |
| weighted replay floor | 478 |
| marked / complement owners | 4,108 / 20,202 |
| marked-bank D2 / D3 | 0 / 0 |
| complement-bank D2 / D3 | 848 / 561 |
| Z-row strict D2 / D3 | 1,875 / 1,874 |
| maximal envelope cells / empty | 24,313 / 0 |
| literal envelope replay mismatches | 2,769 |
| Z upper holes r10..r17 | 1908, 929, 149, 2, 0, 0, 0, 0 |
| arbitrary residual-U rank-ten zero support | 177 |

The two rank-thirteen holes are `0x0fefc` and `0x173f7`.

The owner cycle itself has exact lower-q1 coverage.  Its fixed-width lower
hole counts for q1..q9 are

`0, 1626, 980, 242, 16, 0, 0, 0, 0`.

The owner-cycle all-width upper ledger agrees with the Z ledger except at
rank eleven: it has 928 holes, whereas facet substitution leaves 929.  This
distinction is explicitly recorded; no owner-cycle statistic is silently
substituted for the physical Z-row statistic.

Relative to the authoritative fixed skeleton, 850 old rank-ten holes are
filled and 858 new ones are created, changing 1,900 holes to 1,908.  Of the
218 rank-ten targets having zero support in the pure-U fixed-skeleton
relaxation, this occurrence change serves 32 and leaves 186 as holes.

Recomputing the stronger arbitrary residual-U relaxation on the **new**
occurrence skeleton gives 19,271 possibly supported rank-ten targets and 177
with zero support.  The zero-support payload is
`b383958488c70ea67ecf5678f84677c68e666cbf5eb4a1f98b7ecd48bee3f778`;
its tag profile is 90 X-only and 87 Y-only.  All 177 remain holes in the
materialized cycle.  Against the old 218-target set, the intersection is 137,
with 40 new-only and 81 old-only targets.

## Fail-closed separation

The connected b-flow proves that the selected occurrence forest has a legal
port completion; it does not repair component interiors.  As long as these
macro components are kept intact, any residual pure-U port pairing,
component permutation, reversal, or port cut retains the 296 internally
zero-bracketed short-run signatures in 157 components.  This is an exact
component-interior floor for the frozen occurrence choice, not a global K17
no-go.  Independently, even an arbitrary locally admissible residual-U
pairing has zero support for the 177 targets above; this is the exact port-side
floor for the same frozen occurrence skeleton.  Conversely, the 32 formerly
unsupported rank-ten targets now served show that occurrence/split-column
changes genuinely escape the old fixed-skeleton 218-target obstruction.  Port
circuits and occurrence columns therefore act on different gates and must not
be conflated.

## Independent artifacts

- script: `scratch/h2_independent_audit_k17_opt28_occurrence_greedy296_connected_20260731.py`
  - SHA-256 `d60b4d376b6347df641c65dd3b400c0bfbf911609d502074ddd171bc3935038e`
- audit JSON: `scratch/h2_k17_opt28_occurrence_greedy296_connected_20260731.audit.json`
  - SHA-256 `047bb2999a8ad22ad421740cd675bae49af64d52b9c80f2578a2d4db7366d433`
  - payload `7416eee10f36706d11c0d31b8bb0eae721686a23915e47236475daa735920692`
- independently serialized owner cycle:
  `scratch/h2_k17_opt28_occurrence_greedy296_connected_owner_cycle_20260731.word`
  - SHA-256 `5af336c0cc122a703238243f25aebba61a8c12ec492aa7c5f4fc80256f62743e`
  - integer order exactly equals the root materialization with SHA
    `801896cd15cc6b0b202db75421b93c1dc0e13a33b67fbc902ce283e242c381a6`
- independently serialized Z row:
  `scratch/h2_k17_opt28_occurrence_greedy296_connected_20260731.zrow`
  - SHA-256 `d84599d11987bfbc82398f968b9deef7e26113b49ac245ba024e7d2cea26c66b`
