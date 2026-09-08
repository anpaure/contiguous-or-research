# K=16: compression frontier below the verified 12874 word

The verified universal word

`answers/k16_upper12874.word`

has length 12874 and SHA-256

`631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e`.

Consequently

\[
12873\le \nu(16)\le12874.
\]

## Exact single-cell compression census

All 12,874 deletions were audited exactly.  The unique best deletion is
position 1, whose value is `0x2800`; the resulting length-12873 word has the
single hole

\[
0x2c6d=11373.
\]

The only deletion roots with at most two holes are:

| deleted position | holes |
|---:|---|
| 0 | `{18553,26745}` |
| 1 | `{11373}` |
| 3 | `{5229,21613}` |
| 12873 | `{52833,52835}` |

All 12,873 adjacent OR-fusions were also audited exactly.  The minimum is two
holes, attained only by

| fused positions | holes |
|---:|---|
| 0,1 | `{11373,18553}` |
| 2,3 | `{5229,21613}` |

The fusion audit is `scratch/k16_upper12874_fusion.audit.json`.

## Exact repair radius

For the unique one-hole deletion, all arbitrary one-cell substitutions and all
arbitrary two-cell substitutions are negative.

For each of the three two-hole deletion roots and both minimum two-hole fusion
roots, all arbitrary two-cell substitutions are also negative.  The proof is a
complete partition:

1. if one edit individually installs at least one input hole, the generalized
   provider audit enumerates that edit and every common-provider second edit;
2. otherwise every new input-hole witness contains both edits, which is the
   generalized joint audit.

Thus none of the best deletion/fusion roots can be compressed to a universal
length-12873 word with at most two subsequent substitutions.

The relevant implementations are:

- `scratch/search_k16_exact_two_edit_multihole_20260730.cpp`
- `scratch/search_k16_exact_joint_two_edit_multihole_20260730.cpp`
- `scratch/audit_k16_upper12874_adjacent_fusion_20260730.py`
- `scratch/audit_k16_common_provider_one_edit_20260730.py`

The finite negative result does not imply `nu(16)=12874`: more global
rethreading at fixed length 12873 remains open.  Blocker-aware and multibasin
replica-exchange searches are running on that fixed length.
