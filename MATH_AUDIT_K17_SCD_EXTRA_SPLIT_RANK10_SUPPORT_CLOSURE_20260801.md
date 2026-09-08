# K17 SCD interior-split rank-ten support closure

Date: 2026-08-01  
Status: exact finite C++ census for the two frozen SCD segmentations stated
below.  This is a rank-ten **upper-colour support** result under the
repository's relaxed necessary one-seam residence test.  It deliberately
does not require the seam intersection to be a missing rank-eight q1 colour.
It is not a path, a complete upper deck, a compiler, or a `k=17` word.

## 1. Question

The frozen Greene--Kleitman/SCD owner forest has 24,310 rank-nine owners.
After cutting it into 6,281 resident pieces, the internal Johnson edges use
18,029 of the 19,448 rank-ten colours, leaving 1,419 rank-ten cut colours to
be restored at seams.

For a proposed oriented seam, the audit applies the same deliberately
necessary (not sufficient) residence test as the earlier integrated seam
audit: a coordinate which is all-one on either incident piece is not rejected
locally; otherwise the positive boundary runs must have combined length at
least four.

The question here is whether additional cuts inside the selected pieces can
create endpoints which remove the resulting rank-ten upper-only zero-support
colours.  This is the same projected support gate used by the all-minimum-cut
residual-19 master; lower-q1 correlation is audited separately in Section 3.

## 2. Complete single-split census

Every internal gap of every piece was enumerated.  A split replaces one piece
by its two nonempty subpieces; both orientations of both subpieces were
tested against all unchanged oriented pieces and against each other.  The
newly exposed cut colour was included among the demands.  After choosing a
set of cuts, the complete segmentation was rebuilt from scratch and every
rank-ten cut colour was re-audited.  Thus the final zero count is not inferred
from the additive coverage model.

There are exactly 18,029 candidate gaps.  Every candidate's own new rank-ten
cut colour has at least one necessary-residence provider.

### 2.1 Canonical 6,281-piece segmentation

The canonical segmentation has 322 rank-ten zero-support colours.  The
single-split activation histogram is

```text
activated old zeros : number of cuts
0 : 14490
1 :  3089
2 :   416
3 :    32
4 :     2
```

The union of all single-split endpoint states supports every one of the 322
old zeros.  Deterministic greedy cover selected 192 cuts.  Rebuilding those
cuts gives:

```text
pieces                    6473
rank-ten cut colours       1611
necessary-residence zeros     0
old zeros remaining           0
new zeros                     0
```

This proves that the canonical 322 is not an intrinsic rank-ten residence
obstruction.  It also shows that the obvious repair inside that frozen basin
is large: the displayed construction uses 192 extra cuts.  No optimality
claim is made for 192.

### 2.2 Coupled residual-19 minimum-cut segmentation

The SAT witness from the all-minimum-cut support master was independently
materialized into 6,281 physical pieces (24,310 owners).  Re-running the
same support audit recovers exactly 19 rank-ten zero-support colours.

Among its 18,029 internal cuts, 224 activate one old zero and exactly one cut
activates two; the other 17,804 activate none in the one-cut projection.  The
union superatlas supports all 19.

Deterministic greedy cover selected 18 cuts.  The complete rebuilt
segmentation gives:

```text
pieces                    6299
rank-ten cut colours       1437
necessary-residence zeros     0
old zeros remaining           0
new zeros                     0
```

The 18 chosen cuts are recorded literally in the audit output.  In
particular, this is not merely a colourwise superatlas statement: the one
common rebuilt segmentation has no rank-ten support zero under the stated
test.

## 3. Interpretation

This closes the **upper-only zero-provider** rank-ten gate inside a modestly
enlarged version of the selected minimum-cut SCD basin.  It also explains why
the canonical 322 count was misleading at that projection: cut selection and
endpoint creation are strongly correlated, and the coupled minimum-cut
witness leaves only 19 projected support defects before any extra split.

It does **not** close the integrated lower-q1/rank-ten gate.  Requiring each
seam intersection to be one of the missing rank-eight q1 colours gives the
following independent replay on the residual-19 segmentation and on its
18-split rebuild:

| quantity | residual-19 pieces | 18-split rebuild |
|---|---:|---:|
| pieces | 6,281 | 6,299 |
| missing rank-eight colours | 6,281 | 6,299 |
| raw rank-ten upper zeros | 0 | 0 |
| relaxed-resident rank-ten upper zeros | 605 | 581 |
| relaxed-resident piece-to-piece matching | 5,868 | 5,898 |
| relaxed-resident piece-to-lower matching | 4,615 | 4,649 |

Thus the selected splits improve the correlated projection only modestly;
581 rank-ten colours still have no seam that simultaneously carries a
missing lower-q1 colour and passes the relaxed residence predicate.

The result does not charge these 18 splits as word positions.  Cuts are
piece boundaries in the proposed carrier assembly.  They increase the number
of pieces/seams that must be joined and therefore make the subsequent degree,
connectivity, and all-width chronology constraints harder; they do not by
themselves change the 24,310-owner count.

## 4. Scope exclusions

The audit does **not** establish any of the following:

* simultaneous lower-q1 and rank-ten support (581 rank-ten zeros remain);
* a simultaneous in/out-degree-one assignment for all 6,299 pieces;
* one Hamilton path through the pieces;
* preservation of ranks 11--17 under one chronology;
* exact coordinate residence across the entire final path (the seam test is
  only a necessary local relaxation);
* a depth-three antecedent or strict-lower compiler;
* `nu(17)=24313` or any improved certified upper bound for `nu(17)`.

The next exact gate is an integrated endpoint-degree/path selector on the
6,299-piece segmentation, followed by all-width upper CEGAR and literal
compiler replay.

## 5. Reproducible artifacts

All enumeration and compilation ran on the H100 host's CPU using
`g++ -std=c++20 -O3 -DNDEBUG`.

* audit source:
  `scratch/audit_k17_scd_322_extra_split_cover_20260801.cpp`, SHA-256
  `6bb71cfd6fc71c135cf5cdc2d7e0946abb4a4af359c7fbc418a215dad85f956d`;
* canonical output:
  `scratch/audit_k17_scd_322_extra_split_cover_20260801.out`, SHA-256
  `499316e9f3e371bef25e3e945db3b9cfc26b6de9cb30bbfa0f0fb3404bd794f7`;
* minimum-cut model materializer:
  `scratch/materialize_k17_allmin_model_pieces_20260801.cpp`, SHA-256
  `a42603f7af20d446030bfec7ca91b506bd2422200380afc706c6da2e61aa01f1`;
* materialized residual-19 pieces:
  `scratch/k17_selected_b19_pieces_20260801.json`, SHA-256
  `8164f88fcd02cf56a9ccc8af7c7c156bf1dcf8fd3a9ec12df5ed4b23aaad5aa1`;
* residual-19 split audit:
  `scratch/k17_selected_b19_extra_split_audit_20260801.out`, SHA-256
  `77833a34b00ee0cf3afb0f9d8940eafceaa83cb41f7b2471a5103e925d5a3dfe`.
* literal 18-split rebuild:
  `scratch/k17_selected_b19_split18_pieces_20260801.json`, SHA-256
  `77d6d98aea4ccfaf5de6c90169ae7ca87543edbd8d0beea544a686dac06859f2`;
* generalized integrated seam audit source:
  `scratch/audit_k17_scd_6281_oriented_seam_hall_20260801.cpp`, SHA-256
  `01afbb1db152949d8cbd78320f8cfb4033af8f6592e8d874024c1ae8fadfb82b`;
* integrated 18-split output:
  `scratch/k17_selected_b19_split18_integrated_20260801.out`, SHA-256
  `8b83a60df4cfe69eec19a3788f7d57b95c43f21b78e2b2e6b9574619a4ce52f7`.
