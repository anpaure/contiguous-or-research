# K15 skipped arbitrary seams: exact rank-five compiler-core obstruction

Date: 2026-07-30  
Status: exact fixed-carrier audit; no direct K16 compiler verdict

## 1. Question and correction

The retained arbitrary-seam audit contains `60` qualifying two-cycle
chronologies, but its compiler loop stopped after the first verified row.
Rows `31` through `60` were therefore never compiled.

Those skipped rows do remove the repeated immediate-lower parent target: each
has exactly

```text
rank-seven q1 holes       2
rank-seven duplicate excess 0.
```

However, their exceptional seam intersection has rank **five**, not rank six.
The full residual boundary packet has ranks

```text
6, 7, 7.
```

Thus the proposed parent-rainbow trade replaces a repeated rank-seven target
by one rank-five seam, which creates one rank-six q2 demand in addition to the
two rank-seven q1 holes.

## 2. Exact symmetry reduction

The 30 skipped chronologies form one literal symmetry orbit:

* rows `31`--`45` are the 15 coordinate rotations of row `31`;
* rows `46`--`60` are reversed coordinate rotations of the same chronology.

This was checked entry for entry on all `6,435` middle cells. Hence one
representative obstruction transports to the full family by coordinate
permutation and word reversal. The audit nevertheless compiled all 30 rows
individually.

## 3. Exact compiler result

For each row the generalized fixed-opening compiler uses the complete
length-`6,438` envelope, every literal lower target, all three boundary
residual targets, and the adjacent-omission constraints that preserve the
middle chronology under three derivatives.

Every ordinary bipartite target/position graph has Hall deficiency zero.
Nevertheless the complete adaptive model is infeasible in all 30 cases:

```text
rows decided                              30
ordinary Hall deficiency                  0 on every row
boundary residual targets                 3 on every row
variables per model                 200,122
constraints per model                50,008
exact status FIXED_OPENING_ADAPTIVE_CORE_INFEASIBLE: 30.
```

The H100 run used one low-priority CPU core, `95.94 s` wall for all 30 models,
and `366,876 KiB` maximum RSS under a `4 GiB` address-space cap. No GPU was
used.

## 4. Minimal nested representative core

For row `31` the residual targets are

```text
0x3186 = 12678, rank 6
0x318e = 12686, rank 7
0x3a86 = 14982, rank 7.
```

The first two are nested:

```text
0x3186 subset 0x318e.
```

Three exact drop-one models isolate the obstruction:

```text
omit 0x3186: all remaining 4,945 targets feasible
omit 0x318e: all remaining 4,945 targets feasible
omit 0x3a86: model remains infeasible.
```

Therefore `{0x3186,0x318e}` is a minimal two-target adaptive core relative to
the fixed carrier. Ordinary Hall can place both targets separately, but the
adjacent-omission constraints cannot place them simultaneously. The third
rank-seven boundary target is not part of this minimal core.

By the exact symmetry orbit, every skipped row carries the corresponding
rotated or reversed nested rank-six/rank-seven core.

## 5. Consequence for the parent-rainbow proposal

The skipped rows genuinely solve one problem: they have no repeated
rank-seven q1 intersection, so the known parent collision

```text
0x4279 -> child ghost 0xc279
```

is absent from this carrier family.

But the collision has not disappeared for free. It is exchanged for a
rank-five seam whose residual rank-six/rank-seven nested pair cannot be
absorbed by the current three-cell fixed-opening compiler. In the K16
first-middle inventory a hypothetical length-`12,873` word has `G=0` and only

```text
S + J + F = 3
```

units. The three residual boundary masks are not three independent spendable
units: the nested pair already conflicts inside the exact parent compiler.

Consequently these rows do **not** supply a fixed-carrier K15-to-K16 lift.
A direct K16 construction would need a new distributed ear or boundary split
that separates the nested pair before spending the three `S/J/F` units.

This is sharply scoped. It excludes the 30 retained skipped chronologies under
the existing exact length-6438 fixed-opening compiler. It does not exclude a
different parent carrier, moving the duplicate into a separately consumed
endpoint occurrence, or a direct K16 compiler with new physical cells and
constraints.

## 6. Artifacts

```text
scratch/compile_k15_rank6_arbitrary_seam_rows_20260730.py

scratch/k15_rank6_arbitrary_seam_rows_20260730/rank6_rows30.audit.json
  SHA-256 56c1c403eaa58448b5770a0c30272e90a60c19ed79e8c40a01a23bdf0c4b843f

scratch/k15_rank6_arbitrary_seam_rows_20260730/rank6_core1.audit.json
  SHA-256 d6815d3dcc411e921ae74b298a1a36852a5c2e692e47ad46a3447512fac6282a

scratch/audit_k15_rank5_arbitrary_seam_compiler_core_20260730.py

scratch/k15_rank6_arbitrary_seam_rows_20260730/audit.independent.json
  payload 7e0a46e352f35ed0e9eac87848aaf7273a23bb7a0715106f1a06f8039c7060b7
```

The independent audit reconstructs all chronologies from the authenticated
factor, verifies the 30-row symmetry orbit and seam ranks, checks every model
size/status, and authenticates the representative drop-one core.
