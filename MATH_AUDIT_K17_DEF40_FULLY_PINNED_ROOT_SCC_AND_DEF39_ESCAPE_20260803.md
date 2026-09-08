# K17: fully pinned direct-root SCC screen and an exact deficiency-39 escape

**Date:** 2026-08-03  
**Status:** exact finite audit on one authenticated fixed-def40 occurrence
packing.  This is not a chronology, residence, upper, compiler, word, or
`nu(17)=B(17)` claim.

## 1. Frozen face

The audit binds:

- strict-def84 zero-transfer parent `bf5b946f...`;
- the literal `1,748`-ticket / `7,213`-row private bank `d02e01d0...`;
- the fresh `115,086`-edge parent catalogue `57bc1ac6...`;
- the ten-mode fixed-face deficiency-40 witness `e47ceaaf...`;
- one two-phase occurrence packing for those ten modes.

The packing uses ten tickets in each phase.  Its two phasewise sets of 20
BASE_LMR rows have intersection 17 and union 23.  The compact union frozen in
this lane has SHA
`721a36e6fc1e77a33f80f0d651b6c57afb24cda33fb374ab9dc5151f8793d472`.
It is the same 23-row set as the richer authenticated occurrence export
`c92f4e30...`; the latter retains phase masks and role-side provenance.

After pinning the private bank, the ten pretransfer mode footprints, and the
23 occurrence rows, the augmented presentation has `14,502` pinned arcs and
free dummy capacity `785`.  The zero-action completion saturates exactly

```text
29256 / 29256.
```

Its compressed table is byte-identical to `bf5b946f...`; its ten-mode final
overlay is the authenticated fixed-face table `661bba80...`.

## 2. One matching and one SCC pass

Starting from that exact base presentation, orient each free presentation
edge relative to the matching:

```text
unused edge: left -> right
used edge:   right -> left.
```

The dummy bank is retained as its exact capacity node.  Pinned dummy units
are removed before the residual graph is built.  A direct low-to-root edge is
allowed precisely when it is already in the matching or its endpoints lie in
one strongly connected component.

The exact graph census is:

```text
nodes                 84,984
directed residual arcs 4,870,309
strong components      27,259
full LM/LR/MR/DM       2,450,448 / 5,980,260 / 194,480 / 19,448
```

All 27 frozen direct-root actions survive.  Across them there are `5,635`
legal direct edges, and all `5,635` are allowed.  None is present in the base
matching; all relevant endpoint pairs lie in SCC `27,256`.

This proves exact *singleton* augmented-matching feasibility on the chosen
occurrence face.  It does not allow singleton credits to be added: joint
actions still require one joint completion.

## 3. Exact materialized escape

Action 1, at physical row 146/root 1995, was selected as an independent
materialization witness.  The exact pinned augmented flow again saturates
`29,256/29,256`.  Eight compressed rows change, while every protected,
pretransfer-mode, and occurrence row remains literal.  After the ten-mode
overlay, the final table has SHA

```text
9c02bd5450209f8652208905bf78176d24e8348c18f4e8b30b92e40b1c6ea9fb.
```

The exact frozen 50-head replay gives:

```text
active heads       48
inactive heads      2
supplier neighbors  9
I + N               11
target-39 RHS       11
```

The complete supplier matcher—not merely this necessary shore—then gives

```text
16859 / 16898, deficiency 39.
```

Therefore the DRAT-certified fixed-carrier optimum 40 is not a global
root-open optimum.  One occurrence-valid direct-root recoupling breaks it by
one exact rank unit.

## 4. Stronger joint checkpoint

The subsequently frozen joint materialization in
`scratch/k17_b268_common_parent_selector_20260802/joint_scc_screen_def40_20260803`
forces all 27 named retirements at once on the richer authenticated occurrence
face.  It independently saturates `29,256/29,256`, preserves every pinned
row, and reaches complete supplier rank

```text
16876 / 16898, deficiency 22.
```

This joint max-flow witness, not the singleton SCC theorem, is what licenses
the simultaneous 27-action statement.

## 5. Exact subset descent checkpoint

The later exact root-subset descent on this same fixed occurrence face is
frozen separately in
`MATH_AUDIT_K17_FIXED10_ROOT_SUBSET_DESCENT_DEF21_20260803.md`.  It shows that
the all-27 deficiency-22 table is not locally optimal: dropping action 12,
15, or 16 gives deficiency 21 after a fresh joint completion and full
supplier replay.  The all-except-12 representative is single-toggle local
for the frozen deterministic completion protocol, and the three tied
first-level branches have no strict second-drop improvement.

## 6. Selector semantics

The current joint SAT source deliberately treats `ROOT_ACTION` bits as a
relaxation.  A bit conflicts with modes and BASE_LMR tickets at its named row,
but the SAT layer does not contain the augmented matching.  Consequently:

- UNSAT on the relaxed master is proof-safe after its cuts are independently
  authenticated;
- SAT with a root bit is never a carrier witness by itself;
- a root credit enters the 50-head inequality only after an exact completion
  is materialized and `I+N` is recomputed;
- a cut witness is not authenticated merely by storing its own SHA beside
  itself; its mathematical oracle transcript must also be independently
  frozen.

The synthetic root fixture checks only that one free action Boolean can be
selected.  It does not test augmented matching or head-state credit.  The
smallest proof-safe smoke test is exactly the protocol above: pin one actual
occurrence face, find one presentation matching, SCC-screen the 27 singleton
actions, materialize survivors (or a joint action set), and run the complete
supplier oracle.

## 7. Frozen local artifacts

Sources:

- `materialize_bf5_singleton_root_relaxed_20260803.cpp`, SHA
  `e945cf4135c1962381c341eafb6c2fb93700977abdb630407d37f81480553081`;
- `screen_bf5_singleton_root_allowed_scc_20260803.cpp`, SHA
  `8ac5fdf2d9054d30a78583004aa1d780c6b04c950cee2fde35442abbcff13cb6`.

Key outputs:

- SCC screen `367e2a6a...` and audit `fb590967...`;
- action-1 materialization audit `7b737ed6...`;
- action-1 50-head audit `8f9f52a7...`;
- action-1 complete supplier audit `f6f64ba0...`.

Both sources pass Clang C++20 `-Wall -Wextra -Wpedantic` syntax checks.  The
heavy materialization and SCC run were executed only on the H100 under
`/home/amodo/or15/work/root_k17_bf5_singleton_root_relaxed_smoke_20260803`.
