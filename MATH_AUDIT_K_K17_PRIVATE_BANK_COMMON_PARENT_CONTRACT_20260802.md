# K17 private-bank common-parent contract and nontransport audit

**Date:** 2026-08-02  
**Status:** independently replayed exact negative for literal transport.  This
does not rule out constructing a new private bank on another parent.

## 1. Authenticated parent contract

The protected `1,748`-ticket bank has one exact parent, not merely a set of
row IDs.  Its pre-materialization table is

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/original.res1972.tsv
SHA-256 db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185
```

The two load-bearing certificate files are

```text
selected_tickets.tsv
SHA-256 d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1

complete_outer_matching.tsv
SHA-256 179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e
```

The independent audit reconstructed every one of the `24,310` output rows
from this parent and the complete outer matching.  The result agrees
literally with

```text
private_h_outer_materialized.tsv
SHA-256 b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

Thus the common-parent contract is the four-tuple

\[
 (P_{1972},\;\mathcal T_{1748},\;\mu_{18646},\;B_{268}),
\]

not the final row footprint alone.  Here `mu` contains all `18,646` bottom
placements and marks the `3,495` movable placements forced by the tickets.
The remaining endpoint is the certified fixed-soft occurrence.

## 2. Root-preserving maps have no freedom

The two candidate target tables are

```text
warm47
  scratch/k_rots_k17_joint_1s_20260802/warm47/
    seed4015.relay_cegar.round047.table.tsv
  SHA-256 95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735

generalized_a1
  scratch/audit_k17_corrected_recoupling_common_basis_agent_20260802/
    generalized_a1_LLR.table.tsv
  SHA-256 e3956ccc091280b9091960adcc3f1d990606ed7bcf8c5b5a13078373ef16bda0
```

Every table has the `24,310` rank-eight roots exactly once.  The independent
auditor built the map by root lookup rather than assuming row IDs.  For each
target, all `24,310` roots map to the same row ID, and all `24,310` owners
agree under that map.  Consequently a row/root-preserving bijection is
uniquely forced and is the identity.  There is no hidden permutation with
which to transport the tickets.

## 3. Full occurrence replay

Under that unique map, the exact counts are:

| row | warm47 | generalized_a1 | denominator |
|---|---:|---:|---:|
| literal table rows equal to `b268` | 8,861 | 8,859 | 24,310 |
| protected unique rows equal | 734 | 734 | 7,213 |
| selected short-row states equal | 184 | 184 | 1,748 |
| host-row states equal | 550 | 550 | 3,496 |
| token-source row states equal | 568 | 568 | 3,495 |
| complete literal tickets equal | **0** | **0** | 1,748 |
| named ticket bottoms present at their hosts | 550 | 550 | 3,496 |
| complete outer receiver placements equal | 4,761 | 4,760 | 18,646 |
| forced ticket placements equal | 549 | 549 | 3,495 |

The host-bottom row includes the one fixed-soft endpoint, hence `550=549+1`.
Original hard bottoms are globally distinct, so the bottom installed at a
receiver identifies its source token.  Thus the forced-placement counts are
literal token-to-host counts, not a marginal containment screen.

These numbers also separate two notions which must not be conflated:

* owner/root preservation holds everywhere;
* the occurrence-labelled ticket and outer-placement state almost never
  survives.

## 4. One-ticket obstruction

The first selected ticket already proves impossibility.  It has

```text
ticket ordinal       0
(q,alpha,beta)       (7,0,0)
short row            14337
unique root          72498
owner                88882
```

Its protected materialized short state is

```text
[68402,72498].
```

In both warm47 and `generalized_a1`, the unique row with root `72498` is
row `14337`, but its state is

```text
[67888,68402,72498].
```

It is long, not the required short.  Root uniqueness forces this row, so no
row/root-preserving bijection transports even this ticket.  A fortiori none
transports all `1,748` tickets.  The exhaustive replay strengthens this:
there are zero fully retained literal tickets in either candidate.

## 5. Consequence for the LLR470 face

The corrected warm47 LLR transfer graph and its `470` common-positive
matching remain valid as warm47-scoped structural results.  Row-footprint
avoidance does not make that face private-safe.  In particular, the current
`470` table may not be combined with the `b268` bank merely because its
selected transfer rows avoid the `7,213` protected row IDs.

There are exactly two proof-safe continuations:

1. regenerate and independently replay a new occurrence-ticket/host/token
   bank on warm47 (or on the exact generalized table being selected), then
   reprice the `5,647` roles and supplier graph there; or
2. rebuild the complete LLR structural and phase-price catalogue on the
   authenticated `b268` table while pinning its literal bank and outer
   placements.

Until one of those common-parent constructions is supplied, the joint
LLR470/private-bank branch is rejected as a semantic input.  This is not an
unrestricted no-go for private banks, LLR transfers, or the global selector.

## 6. Independent reproducer

```text
scratch/audit_k17_private_bank_parent_transport_20260802.cpp
SHA-256 a9628cedab20c4cf4a22861fd5cff85d8db25c7c95ef8ffa5f92d0ef76d31e63

scratch/k17_phase0_retained_witness_private_basis_20260802/
  private_bank_parent_transport.audit.json
SHA-256 e694ccd249348736e739cd5f8d3fc6ef5b4937ccd48ee65f773165f54f4745c7
```

The program independently parses all tables, reconstructs `b268` from the
authenticated parent and outer matching, builds both root maps by lookup,
replays every ticket occurrence and outer placement, and emits the literal
counterexample.  It used only a lightweight local C++20/O3 replay; no search
or SAT job was run.

