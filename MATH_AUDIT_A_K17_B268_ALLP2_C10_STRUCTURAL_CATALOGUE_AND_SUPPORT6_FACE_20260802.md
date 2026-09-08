# K17 b268 all-P2 C10 catalogue and the four-anchor support-six face

**Date:** 2026-08-02  
**Status:** proof-complete structural catalogue on the authenticated `b268`
private-bank parent.  Socket, supplier, cyclic-cell, endpoint-state and
compiler pricing of the 580 surviving C10s is deliberately **UNKNOWN** while
the H100 receiver campaign is held for the active q1 run.

## 1. Literal parent and row bank

All assertions below use the materialized private-bank parent

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  private_h_outer_materialized.tsv
SHA-256 b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

and the authenticated original-P2 row list

```text
scratch/k17_fixed_p2_role_moving_escape_20260802/
  phase0.p2_global_union.metrics.tsv
SHA-256 b45713072b1d54d315c9d6de3512741aaa8c143966316bece76b80d0ec5ae137
```

The list has exactly 3,899 distinct row IDs.  Every one of these rows is
still literally length two on `b268`; write it as `(A_v,R_v)`, where `A_v`
is its bottom target and `R_v` its rank-eight root.  The twelve residual
anchors are

```text
23021 23042 23046 23070 23336 23340
23471 23850 23955 23987 24051 24055.
```

A direct rowwise comparison with the frozen round-47 phase-zero table gives
zero differences in `(root,length,target-string)` on these 3,899 rows.
There are, however, 1,863 owner differences.  Consequently the old C4/C6/C8
**containment** catalogues transport literally to `b268`, while their old
owner-dependent socket prices do not.  No socket verdict is imported across
that parent change.

This common-parent binding is essential.  Avoiding the 7,213 row addresses
of the old private-bank footprint on a different warm47-derived table is not
literal ticket preservation.

## 2. Exact primitive-cycle characterization

Form the directed containment graph `G` on the 3,899 rows by

\[
             v\longrightarrow w\quad\Longleftrightarrow\quad
             A_v\subsetneq R_w.                         \tag{2.1}
\]

An exact target/root/row-length-preserving reassignment is a permutation of
the bottoms among the fixed roots.  Its nonidentity part decomposes uniquely
into directed cycles of `G`.  In particular, a primitive five-row receiver
circuit is exactly a simple directed five-cycle

\[
 v_0\to v_1\to v_2\to v_3\to v_4\to v_0,              \tag{2.2}
\]

and its alternating matching circuit is a C10.  Cyclic rotation of the
five row IDs describes the same labelled circuit; reversal is a different
circuit unless its five reverse arcs also exist.

The frozen enumerator starts at each of the twelve anchors, exhausts the
four successive out-neighbour lists, enforces five distinct rows and the
closing arc, and canonicalizes by the five directed rotations only.  Hence
its set output is complete and duplicate-free for (2.2) meeting the anchor
set.  This is a code-transparent completeness proof, not a random census.

## 3. Exact b268 catalogue

The complete catalogue contains 580 C10s.  Their anchor incidence is:

| anchor | C10s |
|---:|---:|
| 23021 | 57 |
| 23042 | 127 |
| 23046 | 0 |
| 23070 | 50 |
| 23336 | 2 |
| 23340 | 173 |
| 23471 | 24 |
| 23850 | 76 |
| 23955 | 71 |
| 23987 | 0 |
| 24051 | 0 |
| 24055 | 0 |

The counts sum to 580.  Since every enumerated cycle meets at least one
anchor, every catalogue row therefore meets exactly one anchor.

## 4. Sharp scoped consequence

For each of

```text
23046 23987 24051 24055
```

there is no primitive all-P2 C10 at all.  Moreover, the earlier complete
all-P2 containment audits give no C4, C6 **or C8** through any of these four
anchors.  These structural catalogues apply to `b268` by the exact
bottom/root comparison in Section 1.  A permutation on five moved rows has
cycle type `5` or `3+2` after fixed points are removed.  The first type is
absent by this catalogue; the second would require an anchor-containing C4
or C6 component, also absent for these four anchors.  Therefore

\[
 \boxed{
  \text{any exact all-original-P2 target/root/length-preserving receiver
  packet moving one of these four anchors has support}
  \ge 6. }
                                                               \tag{4.1}
\]

This is a support floor inside the literal `b268`, original-P2,
target/root/row-length-preserving architecture.  It does not exclude a
mixed-F C8, a changed long row, a regenerated socket grammar, or a compound
packet which changes the parent ticket bank.

For the other eight anchors, the 580 C10s are structural candidates only.
No socket-positive, private-safe or composable packet is claimed until each
candidate is replayed on one common-parent tuple containing both transported
phases, the literal 1,748-ticket bank, outer matching, selected-parent
supplier, cyclic-cell and endpoint-state ledgers.

## 5. Frozen evidence

```text
scratch/a_five_role_joint_packet_20260802/
  enumerate_b268_original_p2_receiver_c10.cpp
    874550363e81e0435e1a75cd3d67528d38b0a2bae624eb074393b544d609c8d2
  b268_original_p2_receiver_c10.tsv
    ecfde0119eb1987f4359f35fab2be3d82a6e9e50534b5300138dbcc7aaac7c4a
  b268_original_p2_receiver_c10.audit.json
    37fbe0402f0412ce643d2f3b8e2e0b1570b0a9be44c5c1a2505fa93de6896038
  verify_b268_original_p2_receiver_c10.cpp
    c1400eaf90bd13bfce948740220bfa5a5f08b512cb56457a26dab4c29a306bc8
  b268_original_p2_receiver_c10.independent.audit.json
    25ca88d00f6f3363aa5a01614fb5d0ef0347ca83083af6d2e607894074000491
  audit_b268_original_p2_receiver_c10_light.cpp
    a0c1546e95bfae6e2e107cd26cab7ccd22d1238afdfbf7e171a3670714473bd6
  b268_original_p2_receiver_c10.light.audit.json
    fccbb0020d471ae8d44ddeeca707922f04b899196df2e02ccbd14954851ae667
  MANIFEST.b268.original_p2.enum.sha256
```

The first independent verifier recursively regenerates the entire 580-cycle
set and compares it literally with the producer ledger.  The second is a
small certificate replay which additionally proves zero round47-to-`b268`
root/chain drift and exactly 1,863 owner changes on the 3,899-row bank.  The
manifest also binds the O3 binary, the two exact inputs and the empty stderr.
Structural enumeration ran in the persistent H100 campaign root; no new
heavy job was launched for this audit.

Scope exclusions: mixed-F support four, common two-phase occurrence
selection, private-ticket replay after an edit, selected-parent supplier
matching, bottom pins, cyclic cells, endpoint histories, owner chronology,
residence, upper shadows, source/common-cap/compiler closure, topology and a
word.
