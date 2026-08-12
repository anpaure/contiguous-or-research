# Independent audit: K17 compiler-aware carrier 1918 / 1681 / robust 59/49

Date: 2026-08-02

## Verdict

The frozen checkpoint
`/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/checkpoint_compiler_joint_res1918_deep1681_def59_zero49_s7/`
passes independent carrier and compiler-projection replay.

Checkpoint manifest SHA-256 is `b99333b131b5ddbf0ab36909ee91dfbdb4dcaeee8686c353f186c5290126eba9`; model SHA-256 is `37a160f2b3f02839fcd9621dccb42cce43a0297016cdf050ded742baa6f84748`.

The exact parent is the compiler checkpoint `res1919/deep1682/def63/zero49/M128`, with manifest SHA-256 `ced569c95bb13162c57209af8a678104b521739ac3f6a73f71c2f2a80a1a8673` and model SHA-256 `ce0d12ff44ae40dc9d12e7e207d1fe935c433e8424ec351914d6d8f518e7e2bd`. It is not the plain 1921/1694 carrier.

The result certifies a carrier and exact two-phase projection score. Both phase projections remain Hall-deficient, so this is not a completed compiler, source chronology, common-cap construction, or universal word.

## Carrier replay

Using the checkpoint’s immutable 16,261-row guard copy at SHA-256 `e64219c98e4191bbef8e6ba32567cec6286c777755782030fd9cca13669971fc`, fresh parsing verifies:

- 48,620 selected incidence edges;
- exact ordinary/M/D root degrees and owner degree two;
- normalized boundary and all guards;
- one connected augmented component;
- 19,412/19,412 ordinary non-D q1 colours;
- 19,448/19,448 targets in both openings;
- both short histograms `[1213,705]`, residence 1,918;
- both upper missing vectors `[0,1449,230,2,0,0,0,0]`, total 1,681;
- provider histogram `[0,15108,3788,482,33,1]`.

The single selected batch row is independently inferred as one octahedral C8 circuit with core `114977`, cyclic labels `6,9,7,12`, and roots `115553,115617,119137,119201`. It is physical at the parent, preserves all hard rows, reconstructs the terminal model byte-for-byte, and has zero old upper losses plus one gain in each opening.

Thus `Phi=2R+H` improves from the exact parent’s `5520` to `5517`. The primary model extends to all 1,093,878 variables and satisfies all 7,164,257 round-5 clauses and 22,659,207 literals.

## Path-independent compiler projection

The reconstruction starts from the authenticated raw round047 payload table, SHA-256 `95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735`. Its original short-reset projection was independently recomputed as perfect `16898/16898`, zero deficiency and zero zero-heads, reproducing audit SHA-256 `2b79c35507d07be6c1fbb1503ceff0701ebf11184230b030bc3bfec8f761361a`.

A fresh phase adapter decoded the carrier’s two perfect owner phases and regenerated both 24,310-row transported tables. Both tables independently retain all 65,535 lower targets exactly once, histogram `(0,7395,16915)`, 48,620 selected carrier edges, one component and exact selected owner-phase matching.

The rebuilt phase-table and incidence-diff hashes are byte-identical to the checkpoint:

- phase 0 table: `ac52c0f1a00c91848a0f65f04745aa9a5d5a76d63169ddf3351e44c524f02207`;
- phase 1 table: `736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058`;
- incidence diff: `d4f6948641980adf57a226c9acdd880982a85b33555d0eb27b72f042580ba0a2`.

Fresh exhaustive projection gives:

| phase | matching | deficiency | zero heads | Hall shore | graph FNV64 |
|---:|:---:|---:|---:|:---:|:---|
| 0 | 16841/16898 | 57 | 46 | 72/15 | `6861944c4c5706df` |
| 1 | 16839/16898 | 59 | 49 | 72/13 | `7224bd188cb7487e` |

Every audit report, Hall list and zero-head list is byte-identical to the frozen checkpoint. Taking the componentwise worst over both phases gives robust projection `(59,49)`.

These two `NO_SHORTRESET_HARD_HEAD_PROJECTION_HALL` results are exact obstructions. The word “compiler-aware” means the carrier was selected using this projection score; it does not mean a compiler exists.

## Evidence and scope

The root bundle is `scratch/audit_k17_compiler_res1918_deep1681_def59_zero49_20260802/root/`; the persistent H100 root is `/home/amodo/or15/work/audit_k17_compiler_joint_res1918_deep1681_root_20260802/`.

A separately frozen implementation is at `scratch/audit_k17_compiler_res1918_deep1681_def59_zero49_20260802/defect_agent/`, with 45-entry manifest SHA-256 `5d276f200e97cc0bd2d8ef67c388a481eb668f61ed3f0bf3c3c69c7574a80499`.

A third clean-room carrier adapter is frozen at `scratch/ad_k17_s7_carrier_adapter_20260802/`, with 53-entry manifest SHA-256 `172a155cbcc247c58532d8cf48aa01cbba965933b7ae5bd09a62dc9042e6ea56`; its persistent mirror is `/home/amodo/or15/work/audit_k17_s7_carrier_adapter_joint_packet_20260802/`. It independently obtains the same two owner phases, exact target partition, byte-identical phase tables and robust projection `(59,49)`.

Excluded: occurrence-labelled source consistency, same-role state/flag balance, a literal depth-three chronology, DM/common-cap compilation, residence or upper completion, and a length-24,313 word.
