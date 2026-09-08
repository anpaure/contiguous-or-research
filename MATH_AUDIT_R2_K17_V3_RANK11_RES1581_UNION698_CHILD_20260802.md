# R2 audit: residence1581 clean-block rows and union698 child

Date: 2026-08-02  
Finite root: `/home/amodo/or15/work/r2_k17_v3_rank11_res1581_union698_child_20260802`

Authenticated inputs:

- option map `7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3`;
- factor `14903257c9dd4082ef571a82aefea753a5cda958807d90958f5e43454d2c9497`;
- physical hole ledger `24b1ca524cd7322e8b8e262e3205d1330a46ebcac1938d0e93a3f0381620bd71`;
- missing-orbit ledger `ac0c6d6646e400fd166f7cb8756ba370ed574808f052ed5c9e271bbbc1034ef5`;
- raw union698 residence bank `c9bad1bd9a4a4069ebfca7edab2a8bdb890b447099c9fb4c30e75b3d7e83ad37`;
- compact-v3+rank11 parent `8df50578978ad83704e14f9a7e69d7ede956bcadd41df36fda4a7f16b50bcfc8`.

The all-phase clean-block producer and an independent semantic replay agree on 255 physical rank-12 holes forming 15 complete `Z_17` orbits, 15 distinct nonempty primary no-goods of widths 216 through 307 (total 4,221 literals), 36,142 component/persistent-hole certificate rows, and 56,100 incidence rows.  Every phase has 220 clean owners, and both optional support and component-size profile agree across all 17 phases.  The row bank SHA-256 is `0820ff83eafb30dd81ae42ed5ac0576d760a23b2f82a0155c50ad91c24d54e86`.

The raw 698 residence rows normalize to 622 logical clauses, of which exactly 562 already occur in the parent.  The 60-row delta has arity profile `2:3, 3:27, 4:30`.  The 15 clean-block rows collide with neither the parent nor the residence delta.  Global numeric lexicographic sorting and deduplication therefore give a 75-row suffix, SHA-256 `6764b2a9c73119b822493340084d95dcf2d2da5cd6dd8ffe00e5a863838299e0`.

The child has header `p cnf 366131 2037549` and SHA-256 `27e3e389e36ac4f0a2ef5115a0825cef5101b8270c0b0860d09ea42ccf9aae3d`.  Builder self-replay and a separately written audit verify the complete parent body byte prefix, complete parent clause-vector prefix, canonical suffix bytes, and exact EOF.  The corrected external-input manifest explicitly includes the parent and has SHA-256 `56b7b7a93ca1130ac216c4eb08eb0b9bbeb57da0b9a738a8220a8398a9d57a8a`; the corrected frozen package manifest has SHA-256 `9e78fcccc1a5a0ca64a6167121744405831474c56b4846a818a2af33db35b80a`.

No solver was launched.  The calibration carrier remains nonresident with 1,581 short positive runs.  There is no source, compiler, opening, exterior-window, regeneration, or word claim.
