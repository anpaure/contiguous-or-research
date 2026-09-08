# R2 audit: compact-v3 + rank11 + C18 rank12 + union694 child

Date: 2026-08-02  
Finite root: `/home/amodo/or15/work/r2_k17_v3_rank11_c18_union694_child_20260802`

Authenticated inputs are the compact-v3+rank11 parent CNF SHA-256 `8df50578978ad83704e14f9a7e69d7ede956bcadd41df36fda4a7f16b50bcfc8`, raw residence bank SHA-256 `d718f3536cce182209782ea2ac3daa312ad26b6357bb8df1969bed746716c542`, and the 14-row C18 rank-12 clean-block bank SHA-256 `b1dbd3e5d7bd278fe6b5a2e3fcccb670b3a93bfad0ffcfc9a2e144393c638c09`.

The raw 694 residence rows normalize to 618 distinct logical clauses; 76 reordered duplicates disappear.  Exactly 562 normalized clauses are already present in the parent.  The exact 56-row delta has arity profile `2:3, 3:24, 4:29`.  None of the 14 clean-block clauses occurs in the parent or residence delta.  Numeric normalization, global lexicographic sorting, and deduplication therefore produce an exact 70-row tail.

The child header is `p cnf 366131 2037544`.  The builder self-replay and a separately written replay both verify:

- the complete parent CNF body is an exact byte prefix;
- all 2,037,474 parent clause token-vectors form an exact prefix;
- the suffix is exactly the canonical 70-row export;
- the child ends after clause 2,037,544.

Hashes:

- child CNF `7d7ed776c2141f492187cebfff01653a430af5ca574afa84cdaa9994f4b418dd`;
- canonical tail `9296d4b1dc8192cf7d66add1f8a118a357b4a3c41f55f3ddde9859712ad597d2`;
- residence delta `9a9c9de84b51d3217f0ef534f8e05c670c2c142f8267bb878c166250ff3bdf4b`;
- canonical C18 rank-12 rows `b6c8e92b8cfd43f7cf43e79d3954bb4885fc7c41b45b89db53b7de2ea8f609a9`;
- builder audit `01fef550fb4c86606ddfb4f4b576b911e4ff133abb1ce5d3c755574c8ba8900d`;
- independent audit `197ebb39f806331453a7ea50a5b70b1b1e790c51d75cb0668a1bd2567b3e2e62`;
- frozen manifest `3aac1d881d8b00d034c413136294f3a47819e5dd6130b982e152e622173860fb`.

No solver was launched.  This child adds necessary residence and carrier-derived rank-12 propagation only.  The calibration carrier remains nonresident, and there is no source, compiler, opening, exterior-window, regeneration, or word claim.
