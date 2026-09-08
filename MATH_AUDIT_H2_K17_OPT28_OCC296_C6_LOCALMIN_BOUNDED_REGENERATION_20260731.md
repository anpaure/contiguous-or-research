# Independent audit of the K17 occurrence296 + C6 local minimum

Date: 2026-07-31  
Lane: H2, independent physical replay and bounded-regeneration vector  
Status: **PASS in the exact source-relative scope below; upstream compiler gates remain open**

## 1. Frozen subject and verdict

The audited checkpoint is the composition of

1. the authenticated `occurrence_greedy296` macro forest and connected
   residual flow; and
2. the 1,160-step residual old-`U` C6 history in
   `scratch/k17_opt28_occ296_c6_localmin_candidate_20260731.json`.

The candidate and canonical residual have SHA-256 values

```text
960ca8df23e7c4ea28c6381e6642b4ec1ab86288a57329115d72182e56be949c  candidate
6fcc91d45b2090b26b612020340a21088a2367c5c0bccd10d3d3614042c60fe4  residual
```

The residual payload is

```text
c92b72db852a8362a2f99c8091dec072ef42af831e1ef83af5381375d6d2a6e4.
```

The independent verdict is

> **PASS_H2_INDEPENDENT_OCCURRENCE296_C6_LOCALMIN_FULL_REPLAY.**

This is not a compiler certificate and not a `K17` word.

## 2. Independent reconstruction

The audit imports no root materializer.  It authenticates the frozen H2
occurrence-reconstruction code by raw hash, then rebuilds the 1,430 macros
from the two `K15` parent cycles and one selected physical occurrence of each
of the 5,005 q2 colours.  It independently checks the 5,005 macro-forest
components, the 106 marked components, 28 optional components, 133 fixed
packet `U` owners, and the literal 4,108-owner marked path.

For each advertised C6 row with rank-seven kernel `K` and outside triple
`a<b<c`, the audit recomputes

```text
ta=K+a, tb=K+b, tc=K+c,
owners=(ta+b, tb+c, tc+a),
old ports=(ta,tb,tc), new ports=(tb,tc,ta),
```

with the two orientations interchanged when requested.  At every one of the
1,160 steps it verifies the removed incidence is live, the added incidence
is new and physically contained in its owner, every rank-eight port retains
degree two, and all 6,435 objects form one cycle.  The final incidence map is
literal-equal to all 4,872 rows of the canonical residual.  The 9,744
residual incidences exactly fill the conditioned demand; owner and port
resources do not repeat.

The macro and packet objects never change under these C6 moves.  Hence their
component interiors, including the independently recomputed 296-packet
component-interior floor (weighted floor 478), are invariant.  Port circuits
can improve seams and global chronology, but cannot repair those interior
packets without an occurrence/split-column actuator.

## 3. Literal materialization

The final factor expands to one Johnson cycle with

```text
objects                                  6,435
distinct rank-nine owners               24,310 / 24,310
distinct lower-q1 colours               24,310 / 24,310
cyclic lower holes q1..q9        0,1441,770,147,2,0,0,0,0
marked/complement owners                 4,108 / 20,202
marked D2/D3 packets                     0 / 0
complement D2/D3 packets                 230 / 94
```

The nonflat row has 4,108 rank-nine marked tokens and 20,203 distinct
rank-eight facet tokens.  Its exact audit is

```text
strict D2 packets                         503
strict D3 packets                         503
maximal-envelope empty cells                0
literal replay mismatching rows           748
missing row-bit host obligations           776
upper holes rank 10/11/12        1585 / 824 / 116
upper holes rank 13/14/15/16/17   0 / 0 / 0 / 0 / 0
```

The owner-cycle and nonflat-row artefacts have SHA-256 values

```text
d34e30f2801b09f4769a41c53f412d6ba472a270b36e99d840972571b57fe13f  independent owner cycle
45b6769ba4f92c386181340a9483a0f8b2f682ca9697d51972a2d352c8b060a9  independent Z row
```

## 4. Exact bounded-regeneration vector

Here “upper literal weight” means one unit for each distinct missing literal
target mask in ranks 10, 11, and 12.  The audit additionally records rank-bit
mass and q-depth-weighted mass, so this convention is not ambiguous.

| state | central | strict D2 | replay rows | missing row bits | upper q1–q3 literal weight | common-cap Hall |
|---|---:|---:|---:|---:|---:|---|
| pure residual-`U` C6 escape-8 | 0 | 1,029 | 1,571 | 1,651 | 2,467 | undefined |
| occurrence_greedy296 | 0 | 1,875 | 2,769 | 2,901 | 2,986 | undefined |
| occurrence296 + C6 local minimum | 0 | **503** | **748** | **776** | 2,525 | undefined |

Consequently:

- central ownership and lower-q1 matching remain exact, so the central
  coordinate is zero in all three states; equality at zero is not a strict
  contraction;
- strict residence, replay-row count, and unpacketized hard-host row-bit
  weight all contract strictly relative to both parents;
- upper q1–q3 literal weight improves by 461 against occurrence296 but
  worsens by 58 against pure-C6 escape-8, so it is **not** a two-parent
  contraction; and
- the child does close all q4-and-deeper upper holes, whereas the pure parent
  retains three rank-13 holes and occurrence296 retains two.

Thus the checkpoint is a genuine two-parent contraction in its residence
coordinates, but not a componentwise Pareto contraction of the complete
bounded-regeneration vector.

## 5. Why common-cap remains undefined

The exact common-cap defect

```text
V_*(Z)=min_Q (|T|-nu(H_Q))
```

is defined only after literal replay, residence, protected upper rows,
sockets, and prepins pass.  The child still has 748 replay failures, 503
strict residence packets, and 2,525 rank-10--12 upper holes.  Therefore its
common-cap Hall coordinate is fail-closed as undefined (logically
`+infinity`).  No marginal provider-support count is renamed as `V_*`.

## 6. Audit artefacts

```text
04e0148f4005f96c64df3f88d80628ffc8172e3c7fce67bf8f60e3c3fb1a1b29  scratch/h2_independent_audit_k17_opt28_occ296_c6_localmin_20260731.py
fc6716d285f774c246e22b7cbfd9a29f69391ace9f7d8089061d2fed57f38be7  scratch/h2_k17_opt28_occ296_c6_localmin_independent_20260731.audit.json
caef94767d76ef5fab84aa1bba454740c6fcca4e98914ac74ed0615d777a278d  audit JSON payload
```

The JSON contains exact packet, row-bit, cyclic lower q1--q9, and upper-hole
set digests, all input raw and canonical payload hashes, residual resource
ledgers, and both parent comparisons.  The scope is source-relative to the frozen OPTIMAL28 and
occurrence296 artefacts.  It proves no unrestricted `K17` obstruction and no
compiler or equality result.
