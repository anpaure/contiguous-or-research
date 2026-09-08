# Independent audit: K17 M17_s3, socket-weighted tables, and private H-short bank

Date: 2026-08-02

## Verdict

The `M17_s3` carrier and its two union-supplier projections pass independent replay at `(R,H,Phi)=(1916,1678,5510)` with robust projection `(59,45)`. The socket-weighted table counts also replay exactly, but the object advertised as the c1 weighted table is not C1 owner-phase-labelled: it uses the canonical `original.res1972` owner map. The correct current authenticated phase-0 placement-labelled weighted parent is therefore s7 phase 0, SHA-256 `713f582264427147a126ac16e7fb040484fa84377ae709ad299d8c298b955271`. `M17_s3` itself has no regenerated typed-socket census and is not yet a socket-labelled parent.

The subsequently frozen private phase-0 H-short bank also passes in its declared positive scope: all 1,748 tickets are literal enumerator members, use 3,496 distinct endpoint hosts, have injective movable bottom tokens apart from one explicitly fixed soft-long endpoint, are disjoint from the selected short hosts, and extend to a complete 18,646-token outer matching. It does not certify residual long socket/state completion.

## 1. M17_s3 checkpoint

The authenticated checkpoint is

`/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/checkpoint_compiler_joint_res1916_deep1678_def59_zero45_s3/`.

Its manifest is `ac0aa113ba257aaaa8b656bb7698672918b25226fb2e4c0bcc7f3a57d95ce3ae` and its model is `d9ec3d9b5f06670292edaa5da7e0f2e925215266ca941c6a7e5870fd217c98d6`. The exact parent is M17 `1917/1679`, manifest `92395665370c176f9e7853b16ad814c737473adf1c04fa9efade7c9b963cb696`, model `c00386f2a3b0b06afab08b727261391f581beb89e27bfcfba2b2109ff5cb3286`.

Independent replay verifies the immutable 16,261-row guard, exact degrees and boundary, one connected unicyclic factor, both owner phases, both 19,448-target openings, residence histogram `[1214,702]`, and upper vector `[0,1446,230,2,0,0,0,0]`. The one octahedral C8 has zero old-target losses and one gain in each opening and reconstructs the checkpoint model byte-for-byte.

The two freshly rebuilt round47 transports are:

| phase | table SHA-256 | supplier edges | matching | defect | zero heads | graph FNV64 |
|---:|---|---:|---:|---:|---:|---|
| 0 | `42439f604b3758c881e79615b74c228067c28f9361f7363ff9f6d5aa54d98344` | 72,064 | 16,842/16,898 | 56 | 42 | `67615aed653041de` |
| 1 | `6d8f7d47e4ea6750b73940ab8236fa2f57916540e3a89f866fd69d417369bf37` | 72,130 | 16,839/16,898 | 59 | 45 | `d9363cb106034277` |

Both target tables, Hall shores, zero lists, and incidence differences are byte-identical to the checkpoint copies.

One provenance defect is real: nested projection manifest `7821e7a117e149a1b6d999041b794a1faae78dda0849e312b4baa6bfd770e2c2` contains 27 absolute paths into deleted staging directory `.M17_s3.stage.evsm6B`. Its entries are not directly path-replayable. The promoted files survive and independently rebuild byte-for-byte, so this is a stale-path defect, not a content or numerical failure.

## 2. Independent socket-weighted table replay

Three supplied weighted tables were parsed independently from their raw rows and placement selections. Every table has 24,310 rows, owner/root incidence bijections, strict chains, histogram `(0,7395,16915)`, all 65,535 lower targets exactly once, 18,646 distinct selected real placements, and 1,748 selected H-short hosts. Socket summaries and tuple files were replayed occurrence by occurrence.

| supplied table | SHA-256 | actual owner binding | defect / zero heads | sockets / zero roles |
|---|---|---|---:|---:|
| advertised c1 weighted | `3886de626d55d4393d3f71f51fa9799488608f26eb977a8ff60e7be39cfac7cd` | canonical `original.res1972` | 29 / 22 | 2,407 / 5,949 |
| s7 weighted phase 0 | `713f582264427147a126ac16e7fb040484fa84377ae709ad299d8c298b955271` | s7 phase 0 | 121 / 108 | 3,615 / 5,493 |
| s7 weighted phase 1 | `42e56cb4dfb97740edc89e8e04239969f558c953cc224bb00e616b01d41b1346` | s7 phase 1 | 131 / 121 | 3,653 / 5,497 |

The independent supplier graph fingerprints for the s7 tables are `c9f1ec131936d1a2` and `ad5591f099abe767`. Their independently rebuilt socket tuple files are byte-identical to the producer outputs.

The c1 label fails closed. Its owner/root map has zero differences from the canonical origin, but 11,930 owner differences from C1 phase 0 and 12,287 from C1 phase 1. Its numerical metrics are correct for the literal table, but it cannot be guarded as `C1_PHASE0` or promoted as a C1 placement-labelled parent.

The selected placements are genuinely different, not merely dummy relabellings. Canonical-versus-s7 phase-0 real-placement/H-short overlaps are `549/623`; canonical-versus-s7 phase 1 are `539/573`; s7 phase-0 versus phase-1 overlaps are `15965/1133`.

## 3. Pareto parent decision

Under the three-coordinate order “minimize supplier defect, minimize zero socket roles, maximize exact socket tuples,” the literal numerical tables are nondominated: the canonical-owner table owns the defect frontier, s7 phase 0 owns the zero-role frontier, and s7 phase 1 has the largest raw tuple count. Provenance is load-bearing, however. The canonical-owner row cannot parent a C1-labelled master.

For a phase-0 carrier-labelled placement Benders branch, the current correct weighted parent is s7 phase 0 `713f5822...`. It is phase-authenticated and improves s7 phase 1 in supplier defect, zero hard heads, and zero socket roles. S7 phase 1 remains a separate guarded row only if raw tuple count is itself retained as a Pareto coordinate.

The M17_s3 tables differ from the corresponding s7 owner phases on 2,567 roots. Therefore neither s7 socket census may be relabelled as M17. M17_s3 remains the authoritative carrier/projection root, but a separate M17-weighted materialization and typed census are required before it can replace the s7 weighted parent.

## 4. Private phase-0 H-short bank

The producer package is

`/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/phase0_retained_witness_private_basis_20260802/`.

Its selected tickets have SHA-256 `d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1`; the complete outer matching has SHA-256 `179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e`; and the complete retained-witness enumerator output `slot_witness.tsv` has SHA-256 `1d78ed8411612c99cb7d9d92dfe4c0dfa84c7f71dc1a8f3afb58e31eb5d7dbfb`.

Independent replay reruns all 209,817,496 candidate pairs of the original enumerator, reproduces its 33,261-record retained-witness summary, and checks every selected row by literal membership and a separate 17-coordinate five-cell feasibility test. The selected bank has:

- exactly 1,748 eligible H shorts and no fixed/free shorts;
- 1,748 predecessor and 1,748 successor hosts, all 3,496 hosts mutually distinct;
- 3,495 distinct movable real bottom tokens plus one declared fixed soft-long endpoint;
- no overlap between a selected short host and any endpoint long host;
- direct bottom-containment checks on every forced movable edge.

The outer certificate uses all 18,646 real bottom tokens once, covers all 1,748 free receivers and exactly 16,898 hard receivers complementary to the short bank, and contains every one of the 3,495 forced movable endpoint edges. The other 15,151 edges are residual outer bottom-matching completion only.

Thus this is a positive private-ticket/outer-extension seed under its original phase-0 enumerator guard. It does not certify fixed/free shorts, residual long socket choices, shared state, reset balance, chronology, residence, upper coverage, common cap, compiler completion, or a word.

## 5. Frozen evidence

The independent checkpoint package is `scratch/audit_m17_s3_checkpoint_agent_20260802/`. The independent weighted/private package is `scratch/audit_m17_s3_s7_table_agent_20260802/`. A third structural replay and supplier reconstruction are in `scratch/audit_k17_m17_s3_weighted_tables_20260802/root/`.

Persistent compute roots are:

- `/home/amodo/or15/work/audit_m17_s3_checkpoint_agent_20260802/`;
- `/home/amodo/or15/work/audit_m17_s3_s7_table_agent_20260802/`;
- `/home/amodo/or15/work/audit_k17_m17_s3_weighted_tables_root_20260802/`.
