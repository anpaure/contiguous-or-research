# K16 u0 blocker: the exact host-restoring segment order and the fixed3+1 4-opt no-go

**Date:** 2026-07-30  
**Status:** solver-free local theorem plus authenticated scoped exhaustive census

## 1. Verdict

The upper-complete G0 chronology `u0` has one static lower obstruction:
rank-seven target `0x4c71` has no proper-prefix host.  The smallest change in
its fixed pattern-4 segment-order family which creates such a host is to move
one target row, `0x4c79`, from after the long rotated block to before it.  The
new cell

```text
start 3279, length 3
position envelopes 0x0c61,0x0431,0x4411
allowed OR 0x4c71
mandatory 0x4871
```

is an exact host.  This one-row repair is not upper-complete: it loses
`0x4e79` and `0x6c79`.

Keeping both the blocker host and all upper targets in the same fixed
pattern-4 family uniquely forces the alternate chronology `u1`.  Relative to
`u0`, its shorter adjacent-block transposition moves original rows
`3279..5725`, a block of 2,447 targets, across the 6,438-row rotated block.
Its unique `0x4c71` host is again `[3279,3282)`, now with

```text
position envelopes 0x0c61,0x0471,0x4461
allowed OR 0x4c71
mandatory 0x4830.
```

But `u1` is not statically lower-feasible: the complete ranks-1-through-7
atlas has two zero-degree targets, `0x4879` and `0x4c39`.

Finally, the complete standard fixed-three-plus-one 4-opt fibre around `u1`
has no static pass.  Its sole named-host-plus-upper survivor is `u0`, which
returns to the original zero-degree target `0x4c71`.

All conclusions are source-relative.  They do not exclude a movable original
cut, terminal-flat cuts, nonstandard row duplication, a five-cut rethread, or
an unrestricted length-12,873 K16 word.

## 2. The fixed pattern-4 family

Let `Q` be the authenticated state2 target order and fix

\[
 b=6388,\qquad c=12826.
\]

For a first cut `a`, consider

\[
 q(a)=Q[0..a]\;Q[b+1..c]\;Q[a+1..b]\;Q[c+1..].       \tag{2.1}
\]

The two authenticated upper-complete rows are

```text
u0 = q(3278), SHA-256 9a96c2c5a1ea6f14eb208a1a800f36853c4765b08c3a56b16c6889f0cca3f14b
u1 = q(5725), SHA-256 6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0.
```

In `u0`, the local target run beginning `0x4c79,0x6479,0x7469,...`
lies after the first flat, where the remaining depth is only two.  Thus its
three-cell `0x4c71` prefix is not available.  Advancing the first cut from
3278 to 3279 moves the single row `0x4c79` before the rotated block, while
the remaining depth is still three.  Direct envelope reconstruction gives
the first host displayed above.  A nonidentity relocation cannot move fewer
than one row, so this is sharp within (2.1).

## 3. The upper seam forces seven first-cut candidates

The state2 source is missing upper target `0x4e79`.  In (2.1), the first new
join contains `Q[6389]=0x6639`, which is not a subset of `0x4e79`, and the
last join is fixed with union `0xc679`.  Therefore `0x4e79` must be supplied
at the return join

\[
 Q[12826]\cup Q[a+1]=0x4a79\cup Q[a+1]=0x4e79.       \tag{3.1}
\]

Exact enumeration of (3.1) gives only

\[
 a\in\{281,3278,4172,5626,5725,6333,6387\}.
\]

Each receives the forced G0 depth, scalar-capacity, maximal-envelope middle,
blocker-host, and unrestricted upper audits:

| `a` | return row | capacity | preflight geometry | `0x4c71` host | upper holes |
|---:|:---:|---:|:---:|:---:|:---|
| 281 | `0x4e78` | 26068 | no: below lower capacity | no | — |
| 3278 | `0x4c79` | 29065 | yes | no | none |
| 4172 | `0x0e79` | 29959 | yes | yes | `0x2e79,0x2e7d` |
| 5626 | `0x4e59` | 31413 | no: middle replay | no | — |
| 5725 | `0x4e39` | 31512 | yes | yes | none |
| 6333 | `0x4e69` | 32120 | no: middle replay | no | — |
| 6387 | `0x4679` | 32174 | no: middle replay | no | — |

Hence `a=5725` is the unique host-plus-upper survivor in this family.

Write the original blocks as

```text
A = rows 0..3278
D = rows 3279..5725, length 2447
E = rows 5726..6388
C = rows 6389..12826, length 6438
Z = the suffix.
```

Then

\[
 u0=A\,C\,D\,E\,Z,
 \qquad
 u1=A\,D\,C\,E\,Z.
\]

Transposing these adjacent blocks can be implemented by relocating either
`D` or `C`; the shorter choice is the 2,447-row block `D`.  This proves the
claimed minimum only for this exact adjacent-block representation.

## 4. Host-aware preflight and the u1 blockers

The independent preflight checker processes candidates in the following
fail-closed order:

1. complete rank-eight multiset and exactly three adjacent flat excesses;
2. forced depths, endpoint validity, and scalar capacity;
3. nonzero maximal envelopes and exact replay of every middle row;
4. arbitrary-width upper replay;
5. named proper-prefix blocker hosts;
6. the complete ranks-1-through-7 candidate atlas.

It does not call a solver.  Only a zero-free final atlas authorizes CP.

On `u0`, it stops at stage 5: `0x4c71` has no host.  On `u1`, the named host
passes and the complete atlas gives

```text
proper-prefix cells: 31,512
candidate incidences: 350,892
zero-degree targets: 0x4879,0x4c39.
```

Thus moving the blocker does not remove lower debt; it transfers one static
obstruction into two.

## 5. Complete fixed3+1 standard 4-opt scope

The authenticated census freezes source cuts

\[
 5725,6388,12826,
\]

adds one extra cut in `0..12868` excluding those three, and tests every
permutation and orientation of the resulting three internal segments.  The
quantified representation count is exactly

\[
 (12869-3)\cdot 3!\cdot2^3=617568.
\]

Its staged ledger is

```text
quantified representations       617,568
upper-join prefilter passes        25,867
exact carrier/capacity passes      12,876
named 0x4879/0x4c39 host passes         1
upper-complete passes                   1
complete lower-atlas audits             1
zero-free static passes                  0.
```

The unique retained row has

```text
extra cut 3278
sorted cuts 3278,5725,6388,12826
segment order 2,0,1
reverse bits 0.
```

Direct reconstruction identifies it byte-for-byte with `u0`.  Independent
survivor replay gives exactly one host each for `0x4879` and `0x4c39`, no
host for `0x4c71`, 361,816 total lower candidate incidences, and sole
zero-degree target `0x4c71`.

The independent audit authenticates the enumerator source and verifies every
count partition, but deliberately does not duplicate the 617,568-case loop.
The exhaustive claim therefore retains the authenticated enumerator as its
enumeration component and adds an independent exact survivor replay.

## 6. Artifacts

```text
scratch/audit_k16_variable_depth_comp3_host_preflight_20260730.py
scratch/audit_k16_u0_4c71_host_segment_order_20260730.py
scratch/k16_state2_tailfixed_3opt_uppercomplete_20260730/
  u0.host_preflight.audit.json
  u1/host_preflight.audit.json
  u0_4c71_host_segment_order.audit.json

scratch/threadD_k16_state2_fixed3plus1_4opt_lower_host_census_20260730.cpp
scratch/threadD_k16_state2_fixed3plus1_4opt_20260730/result.json
scratch/audit_k16_state2_fixed3plus1_4opt_result_20260730.py
scratch/threadD_k16_state2_fixed3plus1_4opt_20260730/independent_survivor.audit.json
```

No handoff or research-index entry is made by this lane.
