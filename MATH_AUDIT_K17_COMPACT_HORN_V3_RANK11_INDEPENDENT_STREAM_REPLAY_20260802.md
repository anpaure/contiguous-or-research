# K17 compact Horn v3 + rank-11: independent stream replay

Date: 2026-08-02

## Verdict

`PASS_INDEPENDENT_K17_COMPACT_HORN_V3_RANK11_EXACT_STREAM_REPLAY`.

The combined compact-Horn-v3 plus rank-11 artifact was reconstructed by an
independent C++20 streaming auditor.  The auditor did not invoke the builder
and did not launch a SAT solver.  No builder correction surfaced.

## Frozen inputs

- combined root:
  `/home/amodo/or15/work/root_k17_compact_horn_v3_rank11_20260802`;
- combined CNF SHA-256:
  `8df50578978ad83704e14f9a7e69d7ede956bcadd41df36fda4a7f16b50bcfc8`;
- combined map SHA-256:
  `73a8f94f2a0249c29ba599bd832a3d173d5e00ed773b3e610761e610600ca5dd`;
- audited compact-Horn-v3 prefix CNF SHA-256:
  `cff3acda560916bdb846fb2f7026c0e4c514de54da4672f48d18f24ce02c103c`;
- audited compact-Horn-v3 prefix map SHA-256:
  `b623e15e60006dcf1ad4cbd817f7d595b691e9d622359a7886620e5f632ead38`.

## Exact replay

The first 1,833,776 clauses of the combined CNF agree clause-for-clause and
literal-for-literal with the independently audited compact-Horn-v3 input.  Its
last prefix clause remains the WLOG unit `204168`.  Hence the existing base,
residence-Horn, sorted blocker-bank, and WLOG rows are retained unchanged.

The independent suffix reconstruction gives:

| section | variables | clauses |
|---|---:|---:|
| exterior summary channels | 11,440 | 82,850 |
| unordered exterior pairs `Q` | 40,040 | 120,120 |
| rank-11 orbit-cover rows | — | 728 |
| appended module | 51,480 | 203,698 |
| complete artifact | 366,131 | 2,037,474 |

For each of the 1,430 rank-nine owner orbits, the auditor independently
reconstructs its eight exterior summary variables and its 28 unordered
exterior-pair variables.  The pair clauses are replayed as the exact
three-clause equivalence

`Q <=> S_x AND S_y`.

Canonicalization produces exactly 728 rank-11 target orbits.  Every target
row has exactly 55 distinct providers, and the 728 sorted rows contain 40,040
provider occurrences in total.

The map replay retains all 110,484 prefix rows exactly and reconstructs 11,440
summary rows plus 40,040 pair rows, for 161,964 rows total.

## Independent semantic controls

The auditor checks both accepting and rejecting assignments rather than only
comparing emitted text:

- every summary channel is tested with no provider and with each individual
  provider active, including the fixed-support case;
- all eight assignments to `(S_x,S_y,Q)` are tested, accepting exactly the
  four assignments satisfying `Q = S_x AND S_y`;
- every 55-provider cover row rejects the all-false assignment and accepts
  each singleton-positive assignment.

This gives 283,050 positive and 243,738 negative synthetic truth cases, all
passing.

## Artifacts

- independent H100 root:
  `/home/amodo/or15/work/qa_k17_compact_horn_v3_rank11_stream_replay_20260802_quotientaudit`;
- auditor source:
  `scratch/audit_k17_compact_horn_v3_rank11_stream_replay_20260802.cpp`;
- auditor source SHA-256:
  `7b56dffc8ed3abf127cbbe5a9aa5f4e02194192c4fdeffabe4ceeb88ef2c9416`;
- audit JSON SHA-256:
  `f058dd39973ef9fb3f222840885cb7cb852823bd9238c949149b26fb39ff39b8`.

## Scope

This is an exact construction and semantics audit of the combined CNF and map.
It makes no SAT, source-factor, compiler, universal-word, or sufficiency claim.

