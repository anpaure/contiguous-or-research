# Independent audit: K16 reorganized-H1 joint13 occupancy projection

Date: 2026-07-30

## Verdict

**GO, with a precise scope.**  The two compact occupancy CNFs are the same
Boolean formula up to the ordering of literals inside clauses.  Each is
equisatisfiable with the authenticated raw unbounded-substitution CNF on the
frozen 13-cell support.  Neither is an unsafe strengthening for that
existential, unbounded-cardinality question.

The projection is not a bijection on physical mask assignments and is not
change-count preserving.  Its exactness therefore does **not** automatically
extend to a constraint such as “exactly (b) changed cells”, to edits outside
the 13 listed positions, or to unrestricted length-12873 words.

No SAT solver was run in this audit.  Both formulae remain solver-status
`UNKNOWN` unless a separately authenticated run supplies a verdict.

## Frozen scope and lineage

The source is
`scratch/k16_h2_to_h1_p0.h1.word`, length 12873, SHA-256
`ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a`.
Literal contiguous-OR replay gives the sole hole
(H=11373=\mathtt{0x2c6d}).

The zero-based editable support is

```text
0, 1,
4486, 4487, 4488, 4489,
6438, 6439, 6440,
12869, 12870, 12871, 12872.
```

Equivalently, the four half-open blocks are
`[0,2)`, `[4486,4490)`, `[6438,6441)`, and `[12869,12873)`.
The complement is frozen.  The intervening fixed-gap ORs are respectively
`0x7fff`, `0xffff`, and `0xffff`; hence none of the 55 residual targets can
have a relevant witness crossing between these four blocks.  Fixed-only
intervals already cover 65,480 targets.

The original support file has SHA-256
`2113ceb9471adb07407e57898ea0f451b7f38d926f3e034ac6cd2d3c2261e153`.
The independently commented copy has SHA-256
`e4e42646f8f5ca50a721e1cdccbd3c2013248d5eed307374cb1a5f5b07bb5c34`;
after comments are removed, the two position lists are identical.

The provider-atlas lineages are:

- `scratch/k16_reorganized_h1_exact_provider_atlas.audit.json`, SHA-256
  `59cbc69665c5f21c8f9575e997765da478e947322d926669172cb71a04ddbbb7`;
- `scratch/k16_reorganized_h1_exact_provider_atlas_v2.audit.json`, SHA-256
  `b216a9da50abe571969049cc5c60b4dff534c6eebba286de1612ef9c124d3c68`.

The second adds the complete 153-row minimum-debt detail.  Both have the same
one-edit debt histogram.  The four minimum-debt portal families are

| portal position | values | exact two-target debt |
|---:|---:|---|
| 0 | 128 | 18553, 26745 |
| 4489 | 8 | 9833, 11881 |
| 6440 | 16 | 32877, 43117 |
| 12872 | 1 | 52833, 52835 |

Their source-witness hull union is exactly the 13-cell support above.  The
separate solver-free geometry audit is
`scratch/ad_k16_h1_four_portal_geometry_20260730.audit.json`, SHA-256
`3263ab64f540e5552f810f2dbf919d6b18da89310162ff8746c0f099e9b4a9d0`.
This atlas/geometry information motivates the fibre; it does not make the
fibre exhaustive for edits outside the support.

## Authenticated raw formula

The parent unbounded-support CNF is
`scratch/k16_reorganized_h1_fourportal_joint13_20260730/model.cnf`, SHA-256
`0fc8ab9880a5016cbc404810f74f1b04c54e93903f6b2b7e1ff47e7dc12f8cb7`.
It has 1,816 variables, 35,208 clauses, and 81,990 literals.  Its map and
statistics hashes are respectively
`cefb607c2b16278aeafedc865fd74ec86f77bf5dc35b83a2a3fd347c8cdc47e9`
and
`390efe8ac875a660fb34fa530be844011c12f7378262e92978790c39e0415318`.
It contains no change-cardinality constraint.

The emitter source is
`scratch/k16_dynamic_unbounded_substitution_cnf_20260730.cpp`, SHA-256
`5d40fc37e1b1caea5992049887204a8224589b48f91ab7b5c6d7531efdc503a1`;
the included frozen core has SHA-256
`c660cae1f5915f23a783fc371177cbe90f0206830d2fb83be92bd0c17a964cb8`.
The compiled emitter in the model directory has SHA-256
`2d67050e3f2a5eb7604b7b4c742b8477d30578d32be2bc7f78649364d2ce51b7`.

The existing independent raw-formula audit,
`scratch/k16_reorganized_h1_fourportal_joint13_cnf_20260730.audit.json`,
has SHA-256
`8b4e73c42771f7c3ce35fba4121db1274fd38f3711864380e3c71c000da9d3ad`.
It independently rederived all 55 repair targets, 341 affected-interval
bases, and 1,595 dominance-minimal witness terms.

## The two compact formulae

The first formula is
`scratch/k16_reorganized_h1_fourportal_joint13_20260730/model.occupancy.cnf`:

- CNF SHA-256:
  `504677bee9bdf8a9eed475f284bcae489a2cf78db6dbc2a2b696c9bc7a632887`;
- map SHA-256:
  `486b5a2f3fa3fd05432190e62bba5fdf7594739b9cd71b058212e8e60a346330`;
- builder SHA-256:
  `1998ae4a1dd83e3309f88d809eb920c4d2affcba085ebdfa9771a23aa72d41eb`;
- map payload SHA-256:
  `7aa37cc02cff2f93fe38b2bfa284feb9af8becb00c248adcabfba970b7cb999d`.

The independently generated second formula is
`scratch/ad_k16_h1_fourportal_joint13_occupancy_20260730/model.cnf`:

- CNF SHA-256:
  `251229383ec319a744fea37bd2f3f89bdf59e638727677166f0eaa7751ecd9bb`;
- map SHA-256:
  `f624e5684fe58c122d43371c16fbd4e1c8db9b9ae8a84930d3b9cf59a4758f31`;
- builder SHA-256:
  `c3f7946a6fffd919c17fa0b7a059d651e0cd2a8102417cb1a0e0ab4aa4d2f2a9`;
- map payload SHA-256:
  `4f163a37546364532807ef1767b33e3706e921587099d841954d262fe9974e08`.

Each has exactly 1,130 variables, 17,558 clauses, and 67,482 literals.
After sorting literals within every clause, the two ordered clause lists are
term-for-term identical; there are 17,558 distinct normalized clauses and
the set differences in both directions are empty.  Occupancy, block-control,
availability, and all 1,595 chart records also use the same variable numbers
and have identical semantic ledgers.  Both builders reproduced their checked
in CNF and map byte-for-byte in a fresh temporary directory.

The byte-level CNF hash difference is solely literal ordering.  It has no
semantic content.

## Why the projection is exact

For each residual target (t), let (y_{t,p}) say that editable cell (p)
lies in one selected witness chart for (t).  The clauses enforce:

1. every target selects a nonempty support;
2. that support lies in one of the four blocks and is one contiguous run;
3. a tracked bit is available at a cell exactly when no selected target
   using that cell omits the bit;
4. every bit required by the selected chart occurs in at least one cell of
   the run.

All 55 residual targets contain coordinate 6 (`0x0040`), and their common
coordinate set is exactly `{6}`.  That bit is implicit and installed in every
canonical cell.  The other 15 coordinates use explicit availability
variables.  Thus a cell used by targets (T_p) is decoded as

\[
v'_p=\bigcap_{t\in T_p}t,
\]

with the empty intersection decoded as `0xffff`.  Every decoded cell is
nonzero.

**Compact to raw.**  A satisfying occupancy assignment decodes to these
canonical masks.  On a selected chart for (t), every cell is a submask of
(t), and the durable clauses supply the exact residual need from the raw
affected-interval ledger.  Hence that chart is a literal witness for (t).
All other targets retain a fixed-only witness.  The decoded physical word is
therefore a raw-fibre solution.

**Raw to compact.**  Given any raw-fibre solution, choose one true raw witness
term for every residual target and mark its editable run with (y).  Each
original cell on that run is a submask of every target marking the cell, so
replacing it by the intersection of those targets can only add bits while
remaining a submask of each marked target.  Every selected witness's required
bits survive, and an unmarked cell may safely become `0xffff`.  Consequently
the canonicalized word satisfies all compact clauses.  This proves
equisatisfiability.

The changed mask values—and even the number of positions differing from the
source—may change under this canonicalization.  This is the only material
caveat; it is harmless because the authenticated parent formula has budget
`-1` (unbounded).

## SAT decoding and replay

Both encodings have a fail-closed SAT decoder.  Each requires an explicit SAT
status and a complete assignment of variables 1 through 1130, checks every
CNF clause, reconstructs a length-12873 physical word, and independently
replays all contiguous ORs to require coverage of all 65,535 nonzero masks.

- First decoder:
  `scratch/decode_verify_ad_k16_reorganized_h1_fourportal_occupancy_20260730.py`,
  SHA-256
  `06e04a156473d76690809924182d3c2e1bec3c1e4379fac77fd66a28dc60e4e7`.
- Second decoder:
  `scratch/decode_verify_ad_k16_h1_fourportal_joint13_occupancy_20260730.py`,
  SHA-256
  `bd7a59635c6b37cec867619ed3c501d74428714da5b91feae8f58eef1b7bfc5c`.

The generic raw decoder
`scratch/decode_verify_k16_dynamic_unbounded_substitution_20260730.py`
(SHA-256
`37bbd13953c1f2f43531d7588925b30d1845f6cf849fdbf00c17690231908c85`)
applies to the 1,816-variable parent, not directly to either compact variable
numbering.

## Claim boundary

A verified `UNSAT` proof for either compact CNF would prove only that no
universal word exists in this frozen-complement 13-cell fibre.  A decoded SAT
assignment would give a valid universal length-12873 word and therefore close
the global gap constructively.  Neither direction licenses an unrestricted
K16 no-go absent an independent theorem reducing all length-12873 words to
this support.
