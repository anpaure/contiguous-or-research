# K16 H1 `x467`: cross-collar capacity exclusion

Date: 2026-07-30  
Lane: zero-branch projection  
Status: **GO, exact on the frozen joint13 support**

## 1. Scope

Fix the authenticated H1 joint13 fibre and the explicit-witness choice

```text
x467 = target H=0x2c6d, old chart 2, editable interval [1,1].
```

All thirteen editable cells may still take arbitrary nonzero values; there is
no edit-cardinality budget.  The complement is frozen.  This theorem proves
that `x467` is impossible in this fibre.  It does not force `x467`, decide the
remaining chart choices for `H`, normalize an unrestricted length-12,873 word
into joint13, or exclude edits outside joint13.

## 2. Canonical cell domain

The exact union-blocker theorem canonicalizes every editable cell to the
intersection of the selected residual target labels crossing it.  The meet
closure of the 55 residual labels, including the empty meet `0xffff`, has
exactly 216 states.  Common coordinate 6 keeps every state nonzero.

For a fixed physical tuple in one collar, a target assigned to that collar
must be compatible with at least one local interval: if the editable OR is
`U`, compatibility is exactly

```text
U subset target  and  residual_need subset U.
```

Thus the number of targets assigned to a collar is at most the number
individually compatible with one or more of its intervals.  Exhausting all
`216^w` canonical tuples is therefore a rigorous physical capacity upper
bound.  It is independent of the existential supply flags in the composed
469-variable CNF.

## 3. Exact capacities of collars 1, 2, and 3

The exhaustive census gives

| collar | width | tuples | sharp capacity | maximizing tuples |
|---:|---:|---:|---:|---:|
| 1 | 4 | 2,176,782,336 | 23 | 137 |
| 2 | 3 | 10,077,696 | 14 | 48 |
| 3 | 4 | 2,176,782,336 | 12 | 328 |

Hence the three collars together absorb at most

```text
23 + 14 + 12 = 49
```

assigned targets.  Summing the separate maxima is safe because every target
chooses exactly one chart, hence is assigned to exactly one collar.

Two structurally different width-four implementations replayed every tuple:

- the primary program specializes the four-cell prefix/suffix OR formulas;
- the independent program decodes a base-216 tuple and constructs all ten
  intervals in generic nested loops.

They agree on both maxima and the complete maximizer counts.  The primary run
used one H100 CPU core for 19.12 seconds and 9,084 KiB RSS.  The independent
run used one core for 38.88 seconds and the same RSS.  Both had explicit time
and 1-GiB address-space caps, exited zero, wrote only below
`/home/amodo/or15/work`, and did not touch `/dev/shm`.

## 4. Exact first-collar interface

Under `x467`, the authenticated physical meet quotient exhausts flat1 by

```text
0x2849, 0x2869, 0x286d, 0x2c49, 0x2c69, 0x2c6d.
```

For each fixed state `S`, exhaust all 65,535 nonzero flat0 values and test the
three first-collar charts `[0,0]`, `[0,1]`, `[1,1]` directly.  The capacities
are

| flat1 state | collar-0 capacity | forced export | Hall deficiency over 49 |
|---|---:|---:|---:|
| `0x2849` | 4 | 51 | 2 |
| `0x2869` | 5 | 50 | 1 |
| `0x286d` | 5 | 50 | 1 |
| `0x2c49` | 4 | 51 | 2 |
| `0x2c69` | 5 | 50 | 1 |
| `0x2c6d` | 3 | 52 | 3 |

This all-six census was also executed independently on one H100 CPU core
under 60-second/1-GiB caps.  It exited zero in 0.02 seconds with 4,608 KiB
RSS, wrote only to its unique `/home/amodo/or15/work` directory, and exactly
reproduced every maximum and maximizing flat0 value.

For the three formerly zero-ejection states, the exact action-availability
projection is also frozen.  Before inclusion dominance there are respectively
64, 65, and 60 profiles.  Each reduces to exactly 55 inclusion-maximal modes:

| state | maximal-mode action-count histogram |
|---|---|
| `0x286d` | 33 modes of size 3, 19 of size 4, 3 of size 5 |
| `0x2c69` | 28 modes of size 3, 24 of size 4, 3 of size 5 |
| `0x2c6d` | 37 modes of size 2, 18 of size 3 |

Every mode records a representative flat0 value and the exact five-bit guard
of each available 469-model action.  A six-bit 55-code selector, invalid-code
rows, and action-to-compatible-mode clauses give an exact compact interface.
For `0x286d`, 48 modes expose one removed-bit omitter and 7 expose two; for
`0x2c69`, the counts are 43 and 12.  State `0x2c6d` removes no bit from `H`.

## 5. Hall contradiction and derived clauses

In every one of the six exhaustive flat1 states, collar 0 forces at least 50
targets into collars 1--3.  Those collars jointly absorb at most 49.  Hence no
canonical assignment selecting `x467` exists.

Equivalently, with `A[T,j]` denoting the original chart indicator (and a
contracted chart fixed to zero in the 469-variable model), the authenticated
cuts are

```text
sum A[T,j], j=3..12  <= 23,
sum A[T,j], j=13..18 <= 14,
sum A[T,j], j=19..28 <= 12,
x467 => sum A[T,j], j=0..2 <= 5.
```

The one-chart-per-target rows give `sum A[T,j]=55`; summing the four cuts
under `x467` gives `55 <= 54`, a contradiction.  The state-specific cuts
strengthen the right side to `53,54,54,53,54,52`.

In the explicit-witness CNF the exact derived clause is therefore

```text
(-467).
```

In the composed 469-variable model, target `H` uses code variables

```text
[81,82,83,84,85]
```

in least-significant-bit order.  Old chart 2 is code pattern `01000` in that
order, so its exact exclusion row is

```text
(81 OR -82 OR 83 OR 84 OR 85).
```

This is a solver-independent strengthening row for the frozen fibre.

## 6. Frozen lineage

Primary sources and results:

```text
scratch/audit_k16_h1_joint13_per_collar_physical_capacity_20260730.cpp
SHA-256 cd55a5d1662a431ec7c674a5fe79bdc491b5d152fe92b81b62bf3ee040170edb

scratch/k16_h1_joint13_per_collar_physical_capacity_20260730/result.json
SHA-256 effeceba208052b798eb93356ce9a6bca36ec47c5bef588545404947123b014c

scratch/k16_h1_joint13_per_collar_physical_capacity_20260730/resource.log
SHA-256 fa1002035e3f39003ac0522618431777ab78f8e891aab8204ed4b28b7258a67f
```

Independent generic replay:

```text
scratch/replay_k16_h1_joint13_per_collar_capacity_generic_20260730.cpp
SHA-256 fd325f3e057de67c867adce1d940aea83ec9256c5306d7f23043a6308fc31c59

scratch/k16_h1_joint13_per_collar_physical_capacity_20260730/replay.json
SHA-256 ebdc76127c3f6206463b376ce1b2a072c288da080475cf78a81669d89a3448f9

scratch/k16_h1_joint13_per_collar_physical_capacity_20260730/replay.resource.log
SHA-256 8ab0cd2d54f448e72c1de949a87392d92d612dbf8f93a72aad0e63d3e624e612
```

Action-mode and Hall audits:

```text
scratch/k16_h1_y467_zero_meet_collar0_capacity_v3_20260730.audit.json
SHA-256 d3faedd4dc1b247b3dc608cf53c7016c758641923a3e26b9c38c45f19d5fa0e0

scratch/k16_h1_y467_zero_states_cross_collar_hall_20260730.audit.json
SHA-256 a50992c88efe63d6981f639e1208cf6f9c31676821def50a80e61330b1063c44

scratch/audit_k16_h1_y467_allsix_collar0_capacity_20260730.cpp
SHA-256 aca3bbaab760c682ef13601c3db2950ca3766060049e349d02a341f924e3a7b5

scratch/k16_h1_y467_allsix_collar0_capacity_20260730/result.json
SHA-256 78c47a496dcc7e6d6c863906335a8aca7dd48bcd4a731ad0d700ac6f721a2193

scratch/k16_h1_y467_allsix_collar0_capacity_20260730/resource.log
SHA-256 e534ff86626e27281e2d2b91df58eecf65d8926022efe3f1c095b6f00194d987

scratch/k16_h1_y467_allsix_cross_collar_hall_v2_20260730.audit.json
SHA-256 1a1a7ea66519277abb2ec74fb7ddb06268016abff1c738b00d7472251ebcbbd6
```

The authenticated witness map is SHA-256
`146f81f628148b2fd904bb5e030236135b00cd502aa2d58051ebb32d6e82638a`;
the six-state meet audit is SHA-256
`e8a4e58cea9fafb93a4fd97e28a5e665b4f698cc486ab52d2687cbba2a934be3`.

The global bracket remains

```text
12873 <= nu(16) <= 12874.
```
