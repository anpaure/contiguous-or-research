# AD audit: seed1/self 4/9/5 saturated atlas and maximal-core solver

Date: 2026-07-30  
Scope: the frozen seed1/self 4/9/5 fibre only. No builder or heavy solver was rerun.

## 1. Frozen inputs and verdict

The authoritative bundle is
`scratch/k16_triwindow_s1s1_repeatfree_frozen_atlas_20260730`.

The independent verifier
`scratch/audit_ad_k16_s1s1_frozen_atlas_and_provider_solver_20260730.py`
reconstructs the literal word and fixed layout, performs a no-cutoff provider
scan, reconstructs every same-`(target,Q)` class, checks the maximal quotient,
and validates the bounded solver report fail-closed. It reports
`PASS_STATIC_UNKNOWN`.

Authenticated principal hashes are:

| artifact | SHA-256 |
|---|---|
| `model.map.json` | `55e5a449cf64f51019dd2e1be909106eace63e652f4c3540418b04e4f0310e1c` |
| `model.cnf` | `67b074bc2ff9232af5dfa4588b9980c5e3254f14114ee7370c430eebfd384d53` |
| `model.stats.json` | `414a4d2f3acc1908a9354f97cbf206754c45b42ed0d27cd19b3b92a531b36541` |
| `host_atlas.audit.json` | `c8fda28998f9d2b5128bd9360b13e9aaa3858c00ee34af0ac5018af9c37a6bd4` |
| raw incidence | `3b65ca45625d3b2d0d16f0ef8f88b89d86d398a744f9b8c9800c1a4458b23e8a` |
| maximal incidence | `270f70383814079aa1f551b9f29883573fd3773aeddea619ca37ce960e507b79` |
| adapted solver source | `42383ef4e862763d47090712688806d47fb2bf36e846419df5776a3352985c37` |

The builder-stat payload needs one precise normalization: the builder hashed
the rank histogram while its keys were integers. JSON round-trip turns them
into strings and changes sort order. Restoring integer keys reproduces
`44edfc9edda20304b0d2a505b51153e6d7762ad0f11a6e7abac2a7b1cc8dce4b`;
the naive string-key digest is
`5eb0d5060487d6b6f81099e6d0fa0e4d9d90b4e4e6ae0e1c8d7004904af0a11c`.
The hardened atlas binds both this normalization record and the CNF hash.

## 2. Exact saturation theorem

Let `P` be the 18 free positions, split into windows of lengths `4,9,5`.
For a literal interval meeting a free window, write `Q` for its free-position
set and `F` for the OR of its fixed cells. For a residual target `T`, the row
`(T,F,Q)` is semantically admissible exactly when `F` is a subset of `T`.

**Theorem 2.1 (frozen S1 saturation).** In the frozen seed1/self layout:

1. the two fixed bodies cover exactly 65,462 nonzero masks, leaving exactly
   73 residual targets;
2. a no-cutoff literal scan finds exactly 6,128 potential intervals touching
   a free position and having fixed OR contained in their target;
3. their target-labelled semantic keys `(T,F,Q)` are exactly the 6,128 rows
   of `model.map.json`: there are no omitted or extra keys;
4. the `Q` universe is exactly all nonempty contiguous subintervals of one
   free window, hence
   `4*5/2 + 9*10/2 + 5*6/2 = 70` classes;
5. every one of the `73*70` target/`Q` classes is nonempty and has a unique
   greatest fixed OR under bitwise inclusion.

Therefore the exact same-`Q` quotient has

`73 * 70 = 5,110`

rows, and deletes `6,128 - 5,110 = 1,018` dominated rows.

*Proof.* Items 1--3 were independently replayed from the frozen parent,
layout, map, and incidence tables. For item 4, an interval cannot meet two of
the widely separated free windows while retaining fixed OR inside any
residual target; the independent scan agrees exactly with the three
contiguous-window families. Direct grouping of the 6,128 authenticated rows
then verifies item 5 and the two counts. The maximal table is an exact replay
of the resulting 5,110 greatest rows. QED.

The current 18-cell incumbent covers 65,531 masks and misses exactly
`0x43ea,0x77bc,0x83c8,0xb38c`. These four holes describe this incumbent only;
the complete provider problem contains all 73 residual rows.

## 3. Why same-Q dominance is exact

For a selected row `(T,F,Q)` and coordinate bit `b`, its effect is:

* if `b` is outside `T`, delete `Q` from the allowed support `S_b`;
* if `b` belongs to `T\F`, require at least one occurrence of `b` in `Q`.

Rows with the same `(T,Q)` have identical support deletions. If
`F'` contains `F`, then `T\F'` is contained in `T\F`, so `(T,F',Q)` has only
weaker occurrence demands. Its authenticated representative is a literal
interval. Replacing `(T,F,Q)` by `(T,F',Q)` therefore preserves every free-cell
assignment that realized the former row, and cannot introduce a new
forbidden bit. Conversely the greatest row is already one of the original
physical rows. Thus retaining the unique greatest `F` is an exact existential
quotient, not a relaxation.

## 4. Maximal-core criterion

For one retained row per target, define

`S_b = P \ union{Q : b notin T}`

and let `A_b` be the inclusion-minimal family among the selected `Q` for which
`b` belongs to `T\F`.

**Theorem 4.1 (exact fixed-choice criterion).** The selected literal rows can
be realized by 18 nonzero free cells if and only if

1. `union_b S_b = P`; and
2. `S_b intersect Q` is nonempty for every bit `b` and every `Q` in `A_b`.

*Proof.* Necessity follows from nonzero cells and each required occurrence.
For sufficiency, assign to position `p` the maximal cell
`{b : p in S_b}`. Condition 1 makes every cell nonempty. The definition of
`S_b` enforces every forbidden-bit condition. Condition 2 places every needed
bit in every inclusion-minimal demand; every discarded nonminimal demand
contains a retained one and is therefore also met. Hence every chosen
representative interval has OR exactly its target. QED.

This proves that the adapted C++ search is exact for its frozen 5,110-option
catalogue. It is not merely a necessary-condition solver.

## 5. Complete hardcode audit

The following seed5-specific quantities had to change:

| location/meaning | seed5 | seed1/self |
|---|---:|---:|
| target count / `MAX_TARGETS` | 70 | 73 |
| raw semantic rows | 6,081 | 6,128 |
| removed same-Q rows | 1,181 | 1,018 |
| reduced rows | 4,900 | 5,110 |
| fixed-body coverage | 65,465 | 65,462 |
| full incumbent coverage | 65,532 | 65,531 |
| parent/collar/word names | seed5, score3 | seed1, score4 |
| atlas, report, proof schemas | RF495 v2 | S1S1 v1 |
| proof scope text | seed5/70 | seed1/73 |
| assigned-state serialization | 9 bytes | **10 bytes** |

The last row is a decisive verifier issue: 73 target bits occupy ten bytes.
The old nine-byte serialization overflows once target index 72 is assigned.
The new verifier uses ten bytes for `assigned`, while correctly retaining nine
bytes for each 70-bit `Q`-demand family.

The following constants remain exact and must not be changed:

* 18 free positions, so `ALL_POS=(1<<18)-1` and support serialization uses
  three bytes;
* 16 coordinate bits;
* 70 `Q` classes, so the two-word `Bits70`, six high root-domain bits
  (`hi=0x3f`), and nine-byte demand serialization remain correct;
* the free positions, body slices `[4,6434)` and `[6443,12868)`, and total
  length 12,873.

The solver itself computes raw/removed counts dynamically and its
`assigned_lo/assigned_hi`, `all_assigned`, hashing, domains, and choices are
valid for 73 targets after changing `MAX_TARGETS`. No width selector,
privileged-hole root, or seed4 restriction remains.

The freezer-specific hardcodes are the bundle path, seed1/score4 filenames,
the four incumbent holes, and the S1S1 atlas schema. Its `70` checks remain
correct because they refer to `Q`, not target count. The independent verifier
also updates all input hashes, coverage/count tuples, loop bounds over targets,
report/proof schemas, and proof-scope text. It additionally checks every
manifest output hash and the normalized builder payload.

## 6. Solver status and fail-closed boundary

The node-one smoke report is authenticated against the new atlas hash. It is
`UNKNOWN`, with one branch, 5,111 transitions, and no mathematical verdict.
The count is consistent with filtering all 5,110 root choices and entering one
child before the node limit.

The C++ solver accepts source hashes from its command line and echoes them; it
does not compute them. Therefore a future result is authenticated only through
the independent verifier:

* `SAT` requires replay of all 73 selected rows, reconstruction of all 18
  maximal-core cells, and literal coverage of all 65,535 nonzero masks;
* `UNSAT` requires exhaustive replay of the complete branch/leaf/reference
  tree, including exact 73-target state identity and report node counts;
* `UNKNOWN` remains `UNKNOWN`.

No heavy solve was launched in this audit, and no K16 bound changes.
