# Independent audit: K17 219-edge both-positive LLR transfer

Date: 2026-08-02

## Verdict

**PASS for the selected single-edge socket claims and the static simultaneous
factor; PASS for the literal generalized recount, with an explicit semantic
source-independence qualification.**  Supplier/private-bank feasibility is not
credited.

An independently written parser and exact five-cell coordinate DP validated
all 219 selected transfer edges in both s7 owner phases.  The 219 receiver rows
and 219 donor rows are pairwise disjoint.  The independently materialized full
factor is byte-identical to the producer table, SHA-256
`163b8e2ccf9da60eef077bab1e4eb7f06535f20368601f57bfc855d4d1cdf92b`.

The exact simultaneous type ledger is:

| Type | Count |
|---|---:|
| `L-L-R` | 219 |
| `L-M-R` | 16,696 |
| `L-R` | 4,643 |
| `M-R` | 2,752 |

All 65,535 targets remain unique, all 24,310 per-chain root/owner pairs are
fixed, every chain is strict, and the length histogram remains
`[0,7395,16915]`.

## Individual pricing versus simultaneous pricing

The 219 edges were selected from the exact intersection of the two 1,018-row
single-edge price tables.  For every selected edge and each phase, the audit
reconstructed the edge-specific long shore, checked the stored predecessor and
successor rows and flags, and reran the exact 17-coordinate/five-cell DP.  The
result is `219/219` valid in phase 0 and `219/219` valid in phase 1.

This does **not** imply that all 219 new donor `M-R` shorts stay common-positive
after all exchanges are installed.  In the complete simultaneous table only
214 are common-positive.  Donor chain IDs

```text
221, 1130, 2636, 4746, 8129
```

are zero in both phases.  Their individual witnesses depended on a long shore
that other simultaneous transfers changed.  This is the load-bearing
distinction between marginal pricing and simultaneous repricing.

## Complete generalized recount

The phase-bound generalized DNF tables were parsed with an independent literal
parser.  Every short row, forced-role marker, bottom, root, and phase owner was
joined back to the pinned factor, P2 role ledger, and s7 owner tables.  The
complete counts are:

| Table | Phase 0 positive | Phase 1 positive | Common positive | Union zero |
|---|---:|---:|---:|---:|
| raw warm47 | 1,371 | 1,369 | 1,016 | 6,379 |
| simultaneous LLR219 | 1,582 | 1,589 | 1,240 | 6,155 |
| delta | +211 | +220 | +224 | -224 |

Among the 7,176 short rows unchanged as physical rows, common positivity moves
from 1,016 to 1,026 through 21 gains and 11 losses.  The remaining 214 common
positives are the new donor `M-R` rows, giving `1026+214=1240`.

A separate H100 O3 replay under
`/home/amodo/or15/work/audit_k17_llr219_semantic_root_20260802` regenerated both
complete 7,395-row DNF tables byte-for-byte in 30.32 seconds.  Its manifest SHA
is `2f0e2eaabe2affc7dd954f848a7fe4ab9467b9b0a765caec31f1a4198f84a29a`.
That run is execution-independent but uses the frozen generalized-pricer
source; therefore the complete zero classification is not claimed to be
source-code-independent.  The selected 219 positive claims are independently
validated by the new DP implementation in this audit.

## Provenance repair

The producer `FINAL2_MANIFEST.sha256` is not provenance-complete: it omits the
external origin factor, both s7 owner-phase tables, the P2 role ledger, and the
two parent single-edge price tables from which the 219-row intersection was
filtered.  This audit freezes those omitted inputs explicitly:

- origin `95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735`;
- phase 0 `ac52c0f1a00c91848a0f65f04745aa9a5d5a76d63169ddf3351e44c524f02207`;
- phase 1 `736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058`;
- P2 roles `8fb841ec529a42daa70ee76408cebc091cfed954a3b4885f28a35d9a6b1498dd`;
- single-edge prices `f15532db...` and `880b1bc7...`;
- selected indices/matching `882d9cee...` and `7c8653b7...`;
- raw DNF tables `44c5fcfc...` and `880f02c6...`;
- generalized DNF tables `77a4b203...` and `172bafb6...`.

The exact paths and full hashes are in `INPUTS.sha256`.

## Scope

Credited: exact selected-edge marginal socket witnesses in both phases,
pairwise physical-row disjointness, static simultaneous materialization,
target/root/owner/strictness/histogram/type preservation, literal generalized
phase recount, and the raw-to-recoupled comparison.

Not credited: supplier or private-bank feasibility, simultaneous endpoint or
ticket packing, chronology, residence, either upper opening, compiler
projection, source-cell realization, or a universal word.  A supplier/private
audit appearing in a later producer manifest is deliberately outside this
audit because it was not independently replayed here.

## Freeze

Independent H100 root:
`/home/amodo/or15/work/audit_k17_llr219_positive_agent_20260802`.

Local artifacts:
`scratch/audit_k17_llr219_positive_agent_20260802/`.  The authoritative files
are `composite.audit.json`, `selected_semantics.audit.json`,
`selected.witnesses.tsv`, `independent.llr219.table.tsv`, and
`FINAL_MANIFEST.sha256`.
