# K16 state2 buffered facet-star three-gap identity obstruction

Date: 2026-07-30

## 1. Minimal exact three-gap class

Fix either authenticated one-blocker state2 source

| case | source SHA-256 | blocker |
|---:|---|---:|
| 0 | `762a6361c571f4e182aa03340399d3a1c07f25755c689362da173f04bd1cc407` | `0x1639` |
| 1 | `1e75cfb4c8e610a4ea2bf1095e44d3236f655aabc3efe65e8532912b7c0572a8` | `0x1879` |

Choose an unordered triple of distinct cofacet centres and remove the three
intact radius-three collars.  Preserve the residual-core order.  For each
removed closure, choose exactly one core gap from its frozen repair set.
Those sets are pairwise separated, so the chosen gaps are already physically
ordered.  Exhaust all

\[
 3!\cdot2^3=48
\]

ways to assign the three intact collars to the three gaps and orient each
collar forward or backward.

This is the smallest three-gap intact-collar subclass motivated by the
two-gap stabbing theorem: it imposes one insertion gap in each of the three
demanded repair sets.  The earlier theorem proves only that three distinct
gaps are necessary in the unchanged-row, order-preserving-core model; it
neither prescribes intact atoms nor asserts that three gaps suffice.  This
class changes no mask and moves no residual-core row.  Thus it is disjoint
from directed donor-value transfer and long-segment 3-opt.

## 2. Exact size

Each root has two depth-three centres with six repair gaps and seven
depth-two centres with four.  Its 84 unordered centre triples therefore give

\[
 \binom73 4^3
 +2\binom72(6\cdot4^2)
 +7(6^2\cdot4)
 =7280                                                     \tag{1}
\]

labelled repair-gap triples.  Hence the exact labelled
descriptor-representation count is

\[
 7280\cdot48=349{,}440
\]

per root and 698,880 across both roots.  No physical-word distinctness is
asserted at this stage; physical deduplication is reported only for the 168
survivors.

## 3. Exact local compatibility graph

For a target closure \(p\), chosen repair gap \(g\), donor collar \(q\), and
orientation sign, form the single-port transplant by deleting \(C_p\) and
inserting \(C_q\) at \(g\).  Replay every row of the inserted seven-row block
and every row whose depth-at-most-three dependency cone crosses any changed
directed seam, including the target-removal closure when the insertion does
not replace it.  The minimum repair-port separation is 56 core gaps in case
0 and 371 in case 1 (minimum compacted closure separation 59 and 374).
Hence the other selected ports only translate, and cannot alter, this local
sequence.  The two-gap flat ledger—globally unique moved rows, unequal
deletion endpoints, and repair gaps disjoint from source-flat gaps—preserves
the source flat order and fixes each target's actual phase.  Thus the three
local port tests factor independently; rows outside their disjoint
neighborhoods retain source replay.

Deduplicating over selected triples gives 720 literal local entries per
source:

\[
 \left(2\cdot6+7\cdot4\right)\cdot9\cdot2=720.              \tag{2}
\]

Write a directed arc \(q\to p\) when some gap/orientation is locally
compatible.  Every compatible entry is at the zero-offset closure gap and
uses the forward orientation.  The complete arc sets are

```text
case 0: nine self-loops, plus 10966 -> 1058;
case 1: nine self-loops, plus 6061 -> 10681 and 12768 -> 12387.
```

The extra arcs are acyclic.  A collar-to-gap assignment is a permutation of
the selected centres, and every nonidentity permutation contains a directed
cycle of length at least two.  Since the compatibility graph has no such
cycle, the only compatible permutation is the identity.  Its three
self-loops force all three zero offsets and forward orientations.  Thus every
local-carrier survivor literally restores each collar to its original place:

\[
 \text{compatible origin path}=\text{source identity path}.              \tag{3}
\]

Equivalently, among 14,560 repair-gap graphs, 14,392 have an empty target
slot—a singleton Hall obstruction.  The remaining 168 graphs have a unique
oriented perfect assignment, exactly the identity descriptor for one
`(source, unordered triple)` instance.

## 4. Materialization and full filters

The complete descriptor census is

| stage | representations | distinct words |
|---|---:|---:|
| generated | 698,880 | — |
| local carrier compatible | 168 | 2 |
| full G0/capacity/carrier | 168 | 2 |
| upper complete | 168 | 2 |
| static-lower zero-free | **0** | **0** |

All 168 carrier representations materialize byte-for-byte to the two input
sources.  Case 0 occurs through 84 triple labels and retains sole static
lower hole `0x1639`; case 1 likewise occurs 84 times and retains sole hole
`0x1879`.  The advertised three-gap topology therefore produces no new
chronology and no completion.

This corrects the overly strong intermediate phrase “no three-gap carrier”:
trivial remove-and-restore representations are carriers.  The exact result
is **no nonidentity carrier and no zero-free completion**.

## 5. Audits

The primary exact audit

`scratch/k16_state2_buffered_star_three_gap_20260730/audit_k16_state2_buffered_star_three_gap_20260730.py`

has SHA-256
`077de92c0a318f73ecc6dda076eecc8c947e16eb76bb796cb02a19289b4d6079`.
It enumerates all 698,880 descriptors through cached exact local ports,
materializes every survivor, then independently replays the full flat
profile, capacity, maximal envelope, target reconstruction, arbitrary-width
upper coverage, and complete static lower atlas.

Its artifacts are

- `scratch/k16_state2_buffered_star_three_gap_20260730/three_gap.audit.json`,
  SHA-256 `2deca3770b78a6fb9a448590db3f4216a808d9522607ee78432abbc1336ccd68`,
  payload SHA-256
  `4a5fbc3ed623493a4a01bbb5e295702407649d31b10f2e383d6b0ac68f2f63f0`;
- `scratch/k16_state2_buffered_star_three_gap_20260730/local_compatibility.tsv`,
  SHA-256 `37259b6702ed72e052d85412e20c1e6e112f944a2ff65d59f7313cadcd46533f`;
- `scratch/k16_state2_buffered_star_three_gap_20260730/carrier_survivors.tsv`,
  SHA-256 `b99501038bb98e096e7e439d07a22c500e40cb64f1b2f05e22438a3072075861`;
- `scratch/k16_state2_buffered_star_three_gap_20260730/carrier_case0.targets`,
  SHA-256 `762a6361c571f4e182aa03340399d3a1c07f25755c689362da173f04bd1cc407`;
- `scratch/k16_state2_buffered_star_three_gap_20260730/carrier_case1.targets`,
  SHA-256 `1e75cfb4c8e610a4ea2bf1095e44d3236f655aabc3efe65e8532912b7c0572a8`.

A structurally separate six-port implementation independently derives the
720-entry tables, the three extra arcs, all 168 identity survivors, and the
two retained blockers:

- `scratch/k16_state2_buffered_star_graph_independent_20260730/audit_three_gap_intact_prefilter.py`,
  SHA-256 `4016347cfe5ae6b8f60c49c0a5a8302795298a6c7d708648fe2b6184d623e63e`;
- `scratch/k16_state2_buffered_star_graph_independent_20260730/three_gap_intact_prefilter.audit.json`,
  SHA-256 `3d8ceb887a9b4697c49b026e36baea4970f1177c6854d547cee444bbb27c0bfc`,
  payload SHA-256
  `bc66daf9a6486c8eef2dacc32be57a545ed4522cb44f65db79c1ca99295bc8de`;
- `scratch/k16_state2_buffered_star_graph_independent_20260730/THREE_GAP_INTACT_PREFILTER_AUDIT.md`,
  SHA-256 `950d3ad4ce3a1fa1ef211f62d21e7eccbb6936918c4ab398ad3b32127b9331a5`.

A third, warning-free C++ production enumerator freezes the same complete
descriptor class and all full-filter/replay logic.  Its independently coded
preflight reconstructs the exact 698,880-row domain and all 168 literal
identity descriptors:

- `scratch/k16_state2_three_gap_intact_collar_master_20260730/search_k16_state2_three_gap_intact_collar_master_20260730.cpp`,
  SHA-256 `e7501217248e4f4cd52e9e16263f68c68462bc481518520cf98bf5025ba05987`;
- `scratch/k16_state2_three_gap_intact_collar_master_20260730/audit_k16_state2_three_gap_intact_collar_master_20260730.py`,
  SHA-256 `72003941c52343af7e933fd81ad92d1f7623a484b9f3d5580868468e7476bd33`;
- `scratch/k16_state2_three_gap_intact_collar_master_20260730/preflight.audit.json`,
  SHA-256 `0a3a3bad3eeec5a5e70a12b289fa857a721734540ef66e4dad1866e93adacca6`,
  payload SHA-256
  `b9ae88c1363b4bd8c344237076314e90272e55e30eea0052c762ad091c41bf4d`.

The production executable itself was not launched: the two exact local-port
audits already reduce the full class to two authenticated source words, and
no H100 CPU was safely free at the resource audit.  No remote process was
launched.

## 6. Exact boundary

This theorem covers only three intact, forward/reverse, unchanged
radius-three collars, one gap from each frozen repair set, and an
order-preserving residual core.  It does not cover splitting or interleaving
a collar across gaps, changed values, directed donor transfer, wider atoms,
core-segment moves, other sources, or unrestricted K16.  The bracket remains

\[
 12873\le\nu(16)\le12874.
\]
