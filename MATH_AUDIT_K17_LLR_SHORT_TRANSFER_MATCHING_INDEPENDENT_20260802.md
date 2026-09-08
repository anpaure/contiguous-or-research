# Independent audit: K17 static LMR+LR to MR+LLR short transfer on warm47

Date: 2026-08-02

## Decision

**PASS, with static-only scope.**  An independent C++20/O3 replay from the
literal warm47 factor table and literal P2 role ledger reconstructs the claimed
short-transfer graph:

- 1,018 union-zero low-rank P2 `L-R` receiver roles;
- 34,757 strict-containment edges into the 16,915 `L-M-R` donor rows;
- receiver degree minimum/maximum/exact average
  `4 / 56 / (34757/1018) = 34.142436149312...`;
- independent maximum flow `1018/1018` to distinct donors.

The producer's literal selected matching was then parsed separately and its
entire simultaneous exchange was materialized.  Both the producer matching and
the independently selected matching yield strict complete factors with the
same target, root, owner, and chain-length universes as warm47.

This is **not a socket cure**.  Every exchange changes

```text
(low < middle < donor_root) + (upper_low < receiver_root)
    ->
(middle < donor_root) + (low < upper_low < receiver_root).
```

Thus the 1,018 old low-rank `L-R` shorts become `L-L-R` longs, but shortness is
transferred to 1,018 new rank-7 `M-R` rows.  Those new `M-R` shorts have not been
priced by the old P2 role ledger and must pass a fresh socket/common-phase
oracle before any socket improvement can be credited.

## Frozen inputs

The replay used these exact artifacts:

| Artifact | SHA-256 |
|---|---|
| `scratch/k_rots_k17_joint_1s_20260802/warm47/seed4015.relay_cegar.round047.table.tsv` | `95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735` |
| `scratch/k17_fixed_p2_role_moving_escape_20260802/p2_structural_rethread_roles.tsv` | `8fb841ec529a42daa70ee76408cebc091cfed954a3b4885f28a35d9a6b1498dd` |
| producer `llr_short_transfer.matching.tsv` | `f6fa956c3ad00f7d5accf87a771d1784907ba5a34b71dd98093a1d87b4ed6a94` |
| producer frozen manifest | `c5238fc2324538df856973cf8d0d1263767151d479197c954b522a26f8d87c0e` |
| producer frozen source inside its remote root | `76ce409a564538c690b75ac7bcd13d6a1be734bd456a520452202fa90f3b021d` |

The producer root was
`/home/amodo/or15/work/root_k17_llr_short_transfer_matching_20260802`.
Its frozen manifest, rather than the mutable working-tree source path, defines
the producer source compared here.

The independent audit used the persistent H100 root
`/home/amodo/or15/work/audit_k17_llr_short_transfer_agent_20260802`.
Its verifier source SHA-256 is
`ee027c49fbfc3ee97bfb4ec7b8cfa2997e1e17f4dc89f07c21389e21e292f311`.
It does not include or call the producer implementation: it uses a strict new
parser, an independently written Dinic network, and a complete post-exchange
factor verifier.

## Input authentication

The independent parser checks all of the following before constructing the
transfer graph:

1. The factor has 24,310 canonical rows, 65,535 pairwise distinct targets,
   24,310 distinct rank-8 roots, and 24,310 distinct rank-9 owners.
2. Every root is a strict subset of its fixed owner; every target chain is
   strict; the target ranks 1 through 8 have census
   `[17,136,680,2380,6188,12376,19448,24310]`.
3. The input length histogram is `[0,7395,16915]` for lengths 1, 2, and 3.
4. The warm47 structural types are exactly
   `LMR=16915, LLR=0, LR=4862, MR=2533`, so the input is on the
   compressed-normal face.
5. The P2 ledger has 3,899 canonical, distinct short-row references.  Every
   ledger bottom/root/rank agrees with its literal factor row; every union flag
   is the Boolean union of its two phase flags; all 3,899 structural degrees
   and off-diagonal degrees are recomputed from mask containment.  The full P2
   structural edge count is 67,280.

The union-zero ledger census is 1,641, split by bottom rank as
`rank4=17, rank5=277, rank6=724, rank7=623`.  Exactly the first three groups,
`17+277+724=1018`, are the low-rank `L-R` receiver rows in this theorem.

## Independent graph and matching

For each of the 1,018 receivers with old bottom `u`, the audit independently
enumerates every warm47 `L-M-R` donor with old low target `l` and adds an edge
iff `l` is a proper subset of `u`.  This gives exactly 34,757 edges.  The full
degree histogram is frozen as `degree_histogram.tsv`; its extrema are 4 and 56.

An independently implemented unit-capacity Dinic network has maximum flow
1,018.  Extraction checks that every receiver is matched once, every donor is
used at most once, and every selected pair is a literal graph edge.

The independent matching is not merely the producer table read back: it shares
970 exact receiver/donor pairs with the producer and uses 1,004 of the same
donor rows.  The remaining 48 pair choices differ while both matchings cover
the identical 1,018-row receiver set.

## Full simultaneous exchange replay

The audit independently materializes two complete 24,310-row tables:

- one using the new Dinic matching;
- one using the producer's exact 1,018-row matching.

For each table it verifies, after writing and rereading the literal file:

- receiver rows and donor rows are disjoint;
- exactly 2,036 physical rows change, each exactly once;
- every unselected row is byte-for-byte unchanged at the parsed field level;
- each chain retains its original root and owner;
- all 65,535 targets occur exactly once, with the original target-rank census;
- all roots and owners retain their original complete universes;
- every resulting chain incidence is strict;
- the length histogram remains `[0,7395,16915]`.

The exact structural type ledger is:

| Type | Before | After | Delta |
|---|---:|---:|---:|
| `L-M-R` | 16,915 | 15,897 | -1,018 |
| `L-L-R` | 0 | 1,018 | +1,018 |
| `L-R` | 4,862 | 3,844 | -1,018 |
| `M-R` | 2,533 | 3,551 | +1,018 |

The producer-materialized factor SHA-256 is
`0883ed410412313f4536fa6f60e0ca4602ec4ce311c2ba7726167d10c9069362`.
The independently matched materialized factor SHA-256 is
`ef9eb3e791755fa282f64e834eecf6108cf33b2d44018c927123dd665844415b`.

## Scope boundary

This audit proves an exact **static factor recoupling** statement from the
literal table and ledger.  It proves target partition, fixed per-chain
root/owner incidence, strict containment, disjoint simultaneous support, and
length/type census claims.

It does not prove occurrence-level socket compatibility for the new rows,
source-cell or supplier/private-bank realizability beyond the fixed owner/root
factor incidence, phase chronology, residence, either upper opening, compiler
projection, or a realized universal word.  In particular, the 623 union-zero
rank-7 P2 roles are not receivers in this low-rank transfer graph, and the 1,018
new `M-R` shorts require independent repricing.

## Frozen outputs

The independent audit artifacts are under
`scratch/audit_k17_llr_short_transfer_agent_20260802/`.  The authoritative
result is `independent.audit.json`; `FINAL_MANIFEST.sha256` freezes the inputs,
source, note, replay logs, degree histogram, independent matching, and both
materialized full-factor tables.
