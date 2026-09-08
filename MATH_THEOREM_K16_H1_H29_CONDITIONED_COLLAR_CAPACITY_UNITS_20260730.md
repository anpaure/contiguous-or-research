# K16 H1 joint13: all-29 conditioned collar-capacity units

Date: 2026-07-30  
Status: **GO, exact solver-free partial classification on the frozen joint13 fibre**

## 1. Scope

Fix the authenticated length-12,873 H1 word and permit arbitrary nonzero
values only at the thirteen joint13 cells.  The complement is frozen and
there is no edit-cardinality budget.  Let

```text
H = 0x2c6d
```

be the sole source hole.  This theorem classifies every one of the 29 local
witness charts of `H` by a scalar cross-collar Hall cut.  It proves 22 chart
exclusions, of which 21 are new beyond item 1981.  Seven charts survive this
cut.  No solver result is used or duplicated.

This is not an unrestricted length-12,873 or K16 no-go, and it is not an
UNSAT certificate for the complete joint13 fibre.

## 2. Reusable capacity lemma

The 55 residual targets all contain coordinate 6.  Canonicalize every
editable cell to the intersection of the selected target labels whose charts
cross it, using `0xffff` for an empty intersection.  This preserves every
selected chart and puts each cell in the exact 216-state meet closure.

For collar `b`, canonical tuple `s`, target `T`, and local chart `j`, write

```text
V(T,j,s)  iff  U_j(s) subseteq T and N(T,j) subseteq U_j(s),
Gamma_b(s) = {T : V(T,j,s) for at least one chart j in collar b},
```

where `U_j(s)` is the OR on chart `j` and `N(T,j)` is its residual need.
For a conditioned chart `j0` of `H` in collar `b`, define

```text
K(j0)       = max |Gamma_b(s)| over tuples with V(H,j0,s),
M(c,-H)     = max |Gamma_c(s) minus {H}|.
```

If `H` selects `j0`, then `H` is assigned to collar `b` and cannot be assigned
to another collar.  The exact one-chart-per-target rows therefore imply

```text
55 <= K(j0) + sum_{c != b} M(c,-H).                 (2.1)
```

Consequently, a strict right side below 55 proves the learned unit excluding
`j0`.  Recomputing `M(c,-H)` directly is essential: subtracting one from an
all-target maximum would not be sound in general.

## 3. Exhaustive census

The four collars have widths `2,4,3,4` and chart sets

```text
J0 = 0..2,   J1 = 3..12,   J2 = 13..18,   J3 = 19..28.
```

Every `216^w` tuple was exhausted.  Both the all-target and `H`-excluded
generic capacities are

```text
[7, 23, 14, 12].
```

The conditioned capacities, in chart order, are

```text
J0:  5,  5,  5
J1: 12, 16, 20, 23, 14, 18, 21, 14, 17, 13
J2:  9, 12, 14,  9, 12,  8
J3: 10, 12, 11,  8,  9, 11,  9, 10, 11, 11.
```

Thus the other-collar terms in (2.1) are respectively `49,33,42,44`, and
the strict unit thresholds for `K(j0)` are `5,21,12,10`.

| collar | learned charts `j` with `K(j)` | charts surviving this cut |
|---:|---|---|
| 0 | `0:5, 1:5, 2:5` | none |
| 1 | `3:12, 4:16, 5:20, 7:14, 8:18, 9:21, 10:14, 11:17, 12:13` | `6:23` |
| 2 | `13:9, 14:12, 16:9, 17:12, 18:8` | `15:14` |
| 3 | `19:10, 22:8, 23:9, 25:9, 26:10` | `20:12, 21:11, 24:11, 27:11, 28:11` |

The learned-chart Hall deficiencies are, in the same grouped order,

```text
J0: 1,1,1
J1: 10,6,2,8,4,1,8,5,9
J2: 4,1,4,1,5
J3: 1,3,2,2,1.
```

Charts `6,15,20` have total capacity 56.  Charts `21,24,27,28` have total
capacity exactly 55.  These seven dispositions are **inconclusive**, not
feasibility claims.

## 4. Exact learned rows

The explicit-witness variables of the 29 `H` charts are `x465,...,x493`,
with chart `j` represented by `x(465+j)`.  The 22 solver-free units are

```text
-x465, -x466, -x467, -x468, -x469, -x470,
-x472, -x473, -x474, -x475, -x476, -x477,
-x478, -x479, -x481, -x482, -x483, -x484,
-x487, -x488, -x490, -x491.
```

The exact-one row for target `H` consequently reduces to

```text
x471 OR x480 OR x485 OR x486 OR x489 OR x492 OR x493.
```

In the 469-variable proxy/supply-code composition, the `H` code variables
are `[81,82,83,84,85]` in least-significant-bit order, and the numeric code
is exactly the old chart index `j`.  No `H` chart was contracted.  For every
learned chart `j`, its exact compact exclusion row is

```text
OR over bit i=0..4 of
    variable[81+i]   if bit_i(j)=0,
   -variable[81+i]   if bit_i(j)=1.
```

After these 22 no-goods and the pre-existing invalid-code rows, the compact
`H` domain is exactly

```text
{6, 15, 20, 21, 24, 27, 28}.
```

## 5. Independent authentication

The primary optimized enumerator updates all conditioned charts during one
pass per collar.  On one H100 CPU core it exhausted

```text
216^2, 216^4, 216^3, 216^4
```

tuples in 57.53 seconds using 9,088 KiB maximum RSS.  It ran under a
240-second/1-GiB cap in a unique `/home/amodo/or15/work` directory and wrote
nothing to `/dev/shm`.

A structurally independent replay first exports and audits the complete
55-by-29 need ledger from JSON, then decodes every tuple as a base-216 number
and constructs all intervals with generic nested loops.  It independently
checks the explicit `H` exactly-one/mutex rows, compact LSB code mapping,
invalid codes 29--31, all physical chart intervals, and absence of any
contracted `H` action.  Its one-core H100 run took 304.58 seconds and 8,924
KiB RSS under 600-second/1-GiB/CPU-590 caps.  It reproduced every generic and
conditioned capacity, every total, and the exact 22-chart learned set.

Frozen primary lineage:

```text
scratch/enumerate_k16_h1_h29_conditioned_collar_capacity_20260730.cpp
  SHA-256 b2a4a333ea0eea53d617319ef74a7cfee685cf368fc1e84195e52115059d3a8d

scratch/k16_h1_h29_conditioned_collar_capacity_20260730/result.json
  SHA-256 1cf38f49743dce287d3151f60b88831e9bc8cbf8d8c74802a33edb4ad5a46e54

scratch/k16_h1_h29_conditioned_collar_capacity_20260730/manifest.audit.json
  SHA-256 2fe6209611b86d44dd5c31492090bab9e0ae65b4a6cbbda6aca3385a1f741ffe
```

Independent replay and audit:

```text
scratch/replay_k16_h1_joint13_all_h_conditioned_capacity_generic_20260730.cpp
  SHA-256 0eab5f17fb7f0c571376a9408f39d72c2c7081471a63fba16f3429f126e6e5f8

scratch/k16_h1_joint13_all_h_conditioned_capacity_generic_replay_20260730/result.json
  SHA-256 935fda6ca7d0ef5a19f87bcb6f98c851257a83fd4a918230900a13366ebe9df3

scratch/k16_h1_joint13_all_h_conditioned_capacity_generic_replay_20260730/resource.log
  SHA-256 84a5974f2f8250c2d1ffc60e91d4d94d4a7509c17b3b8c84d30b442e0f7d7903

scratch/k16_h1_joint13_all_h_conditioned_capacity_independent_20260730.audit.json
  SHA-256 ed1215e3f908c22384b0402f021b0e4421274cc401f0054d20cc0b5f7f29d62e
```

The witness map remains SHA-256
`146f81f628148b2fd904bb5e030236135b00cd502aa2d58051ebb32d6e82638a`.

The exact bracket is unchanged:

```text
12873 <= nu(16) <= 12874.
```
