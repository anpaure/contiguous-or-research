# The authenticated `b268` all-P2 C10 structural gate

**Date:** 2026-08-02  
**Status:** exact structural catalogue and independently replayed scoped
obstruction.  Socket, common-state, supplier, chronology, topology, upper,
source, and compiler gates remain open.

## 1. Exact parent and row class

The parent is the authenticated private-bank materialization

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  private_h_outer_materialized.tsv
SHA-256 b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

Let `P` be the 3,899 row IDs in

```text
scratch/k17_fixed_p2_role_moving_escape_20260802/
  phase0.p2_global_union.metrics.tsv
SHA-256 b45713072b1d54d315c9d6de3512741aaa8c143966316bece76b80d0ec5ae137
```

These are the authenticated *original-P2* rows.  Every row in `P` is still
literal length two in `b268`, and both of its target masks agree with the
metric record.  This restriction matters: `b268` has 7,395 length-two rows
in total, but the other 3,496 are shortened F/H roles.  A broad enumeration
over all 7,395 rows is therefore a mixed-role superset, not an all-P2
catalogue.

For `i in P`, write its literal target chain as

\[
                 (a_i,r_i),\qquad a_i\subsetneq r_i.
\]

Define the directed receiver graph

\[
       i\longrightarrow j \quad\Longleftrightarrow\quad
       a_i\subsetneq r_j.                                      \tag{1.1}
\]

The twelve named residual anchors are

\[
\begin{split}
\mathcal A=\{&23021,23042,23046,23070,23336,23340,\\
             &23471,23850,23955,23987,24051,24055\}.
\end{split}                                                     \tag{1.2}
\]

All twelve belong to `P`.

## 2. Exact C10 correspondence

### Proposition 2.1 (directed-cycle normal form)

Let `i_0,...,i_4` be distinct rows in `P`.  Reassign each row `i_{t+1}`
the predecessor bottom `a_{i_t}`, with indices modulo five.  The five rebuilt
rows are valid strict two-target chains if and only if

\[
 i_0\to i_1\to i_2\to i_3\to i_4\to i_0                 \tag{2.1}
\]

is a directed simple 5-cycle in (1.1).

The reassignment preserves the target multiset exactly: the five roots stay
fixed and the five bottoms are merely permuted.  Owners and roots stay at
their original rows.

#### Proof

The rebuilt row `i_{t+1}` is legal precisely when
`a_{i_t} subsetneq r_{i_{t+1}}`, which is exactly its edge in (2.1).
Distinctness makes the support five.  The target-multiset assertion is the
identity

\[
 \{a_{i_0},\ldots,a_{i_4}\}_{\rm multiset}
 =
 \{a_{i_4},a_{i_0},\ldots,a_{i_3}\}_{\rm multiset}.
\]

No state or source realization is used. ∎

Thus an all-P2 five-row cyclic target packet is neither more nor less than a
directed simple 5-cycle of (1.1).  Reversal is not identified: it need not be
a directed cycle.  The catalogue identifies only the five cyclic rotations,
using their lexicographically least row tuple.

## 3. Complete catalogue

The exact result is

| anchor | number of canonical C10s containing it |
|---:|---:|
| 23021 | 57 |
| 23042 | 127 |
| **23046** | **0** |
| 23070 | 50 |
| 23336 | 2 |
| 23340 | 173 |
| 23471 | 24 |
| 23850 | 76 |
| 23955 | 71 |
| **23987** | **0** |
| **24051** | **0** |
| **24055** | **0** |

There are exactly **580 distinct canonical cycles** meeting at least one
anchor.  A cycle meeting multiple anchors contributes to each corresponding
row of the table but appears only once in the 580-row file.

The producer used explicit nested directed walks.  The independent verifier
used a separate recursive enumeration: from every anchor it generated every
simple directed walk of four edges, tested the fifth closing edge, reduced by
the least cyclic rotation, and compared the resulting set literally with the
producer output.  It also checks strict tuple order, payload masks, all five
edges, simplicity, anchor incidence, and the exact per-anchor counts.

### Corollary 3.1 (scoped support-five obstruction)

No all-original-P2 single-C10 target reassignment on the authenticated
`b268` parent can change any of rows

\[
                 23046,\quad23987,\quad24051,\quad24055.       \tag{3.1}
\]

Consequently a receiver-root-bank repair of any one of these four anchors
must leave this move class: it needs a mixed F/H role, a non-C10 compound
permutation, or larger support.  This is not an unrestricted support-six
lower bound.

#### Proof

By Proposition 2.1 every packet in the stated class is one of the enumerated
directed simple 5-cycles.  The four incidence counts in (3.1) are zero. ∎

## 4. Exact private-ledger nonintersection—and its boundary

The independent verifier also parses the authenticated files

```text
selected_tickets.tsv
SHA-256 d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1

complete_outer_matching.tsv
SHA-256 179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e
```

and proves:

1. none of the 3,899 original-P2 rows is a short, host, or token row of any
   of the 1,748 selected tickets;
2. none is a token or H-receiver row of the 18,646 outer placements; and
3. no original-P2 bottom mask is an outer token bottom.

Therefore any catalogue C10 has zero literal row/bottom footprint on that
private ledger.  This does **not** prove simultaneous common-state or source
realizability.  In particular, the private certificate is a phase-0 object;
there is no authenticated transported two-phase ticket/state contract for a
C10 merely from footprint disjointness.

## 5. Selected `LLR470` comparison

On the distinct selected structural table
`llr_fullprivate470.table.tsv`, only 3,429 original-P2 rows remain length two.
The same exact directed-cycle construction gives 291 cycles and counts

```text
23021:39  23042:0  23046:0  23070:31  23336:0  23340:123
23471:0   23850:55 23955:43 23987:0 24051:0 24055:0.
```

This comparison is structural only.  The `LLR470` table is not the parent of
the `b268` private bank, so its 7,213-row avoidance label cannot be promoted
to ticket preservation.  The exact parent mismatch is already documented in
`MATH_AUDIT_K_K17_PRIVATE_BANK_COMMON_PARENT_CONTRACT_20260802.md`.

## 6. Frozen artifacts

```text
scratch/a_five_role_joint_packet_20260802/
  enumerate_b268_original_p2_receiver_c10.cpp
    874550363e81e0435e1a75cd3d67528d38b0a2bae624eb074393b544d609c8d2

  enumerate_b268_original_p2_receiver_c10
    b66d7f8cd38cba7232d784a6137f804fde2e58d5bd69d9e7b3255eac627e76e3

  b268_original_p2_receiver_c10.tsv
    ecfde0119eb1987f4359f35fab2be3d82a6e9e50534b5300138dbcc7aaac7c4a

  b268_original_p2_receiver_c10.audit.json
    37fbe0402f0412ce643d2f3b8e2e0b1570b0a9be44c5c1a2505fa93de6896038

  verify_b268_original_p2_receiver_c10.cpp
    c1400eaf90bd13bfce948740220bfa5a5f08b512cb56457a26dab4c29a306bc8

  b268_original_p2_receiver_c10.independent.audit.json
    25ca88d00f6f3363aa5a01614fb5d0ef0347ca83083af6d2e607894074000491

  current_allp2_receiver_c10.tsv
    3a0206361119288856773395716818aefd2d20a9d742203f4033df12c999af18

  current_allp2_receiver_c10.audit.json
    08669e89d5d07e71907ca6f0d4b33fe564e3dc892b7db7f2c69467876f5c488d

  c10_socket_pricing.resource_hold.status.txt
    d4179f3546536485b264c453f0a2066ff7d471c5c8c82fea17abfebf9ebbafc0
```

The H100 socket pricers were stopped under the shared resource hold.  Their
partial files are preserved remotely under
`/home/amodo/or15/work/a_k17_allp2_c10_20260802`; no partial shard is used as
a verdict.  Both selected-parent and `b268` marginal two-phase socket pricing
are therefore **UNKNOWN/QUEUED**.
