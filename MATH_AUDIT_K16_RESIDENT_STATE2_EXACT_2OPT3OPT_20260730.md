# Exact tail-fixed 2-opt/3-opt census from the K16 state-2 chronology

**Date:** 2026-07-30  
**Status:** two new upper-complete exact carriers; complete scoped no-go after
the static lower-candidate gate; no K16 word claimed

## 1. Input and scope

The authenticated input is

```text
scratch/k16_resident_state2_upper2_targets.txt
SHA256 77dd098d7e066cd81ed68846d554c5e5a7247e90ec764033394287f312c28464
```

It has length 12,873, contains every rank-eight mask, has precisely the three
adjacent duplicate pairs starting at `6432,12869,12871`, has the forced
three-flat scalar capacity 32,175, reconstructs exactly from its nonzero
maximal envelopes, and misses only the two upper masks

```text
0x4e79, 0xc679.
```

The census fixes the terminal flat pairs at starts 12,869 and 12,871.  It
then exhausts:

1. every standard linear 2-opt segment reversal; and
2. every genuinely three-cut standard 3-opt reconnection.

The four 3-opt patterns are the arrangements of the two internal segments
which are not merely 2-opt with an irrelevant third cut.  Arbitrary block
relocations, four-or-more cuts, movement of the terminal flat pairs, and
changes of target values are outside the theorem.

## 2. Complete candidate reduction

Both old upper holes have rank nine.  If a rethreaded chronology first
creates a missing rank-nine mask across a new join, then both rank-eight
endpoints of that join are subsets of the missing mask.  This remains true
when the immediate join is a flat: every interval newly crossing the join
still has those two boundary targets as subsets of the final rank-nine union.

Thus a successful 2-opt must assign its two new joins to the two holes.  A
successful genuine 3-opt must assign at least two of its three joins.  Each
hole has only its nine rank-eight submasks, so the join assignments pin all
three cuts.  Enumerating these constraints is complete and avoids an
`O(12873^3)` loop.

The optimized C++ replay found:

| gate | 2-opt | genuine 3-opt |
|---|---:|---:|
| candidate keys | 1 | 299 |
| exact three-flat profile | 1 | 278 |
| scalar capacity at least 26,332 | 1 | 267 |
| exact nonzero maximal-envelope carrier | 0 | 4 |
| upper complete | 0 | 2 |

The full run used 5 MiB and 1.54 seconds wall time on one low-priority H100
CPU core.

## 3. The four exact carriers

For cuts after `a<b<c`, pattern 4 is

```text
A + C(forward) + B(forward) + D,
```

i.e. the two internal blocks are transposed without reversal.  Pattern 3 is
`A + reverse(B) + reverse(C) + D`.

| pattern/cuts | capacity | upper holes | exact static zero-candidate lower masks |
|---|---:|---|---|
| p3 `(5627,6433,12826)` | 31,371 | `ce71,cef7` | `4671,4879,8000` |
| p4 `(3278,6388,12826)` | 29,065 | none | **`4c71`** |
| p4 `(4172,6388,12826)` | 29,959 | `2e79,2e7d` | `0e71,4879` |
| p4 `(5725,6388,12826)` | 31,512 | none | **`4879,4c39`** |

The two upper-complete artifacts are frozen as:

```text
u0 target   scratch/k16_resident_state2_2opt3opt_20260730/best_targets.txt.u0
            SHA256 9a96c2c5a1ea6f14eb208a1a800f36853c4765b08c3a56b16c6889f0cca3f14b
u0 envelope scratch/k16_resident_state2_2opt3opt_20260730/best_envelope.word.u0
            SHA256 57669ee5934872f766cdd1666f5a418d6710040f1edafe2c59f2d8ddf146b54a

u1 target   scratch/k16_resident_state2_2opt3opt_20260730/best_targets.txt.u1
            SHA256 6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0
u1 envelope scratch/k16_resident_state2_2opt3opt_20260730/best_envelope.word.u1
            SHA256 20aed0f12f33d49a6abd0565da85fcc7ba5ae6ba580c8097dc1d4012bea8a6b3
```

The second rethread explains how `0x4c71` can be restored.  It has the exact
candidate lower cell

```text
start 3279, length 3, joined envelope 0x4c71, mandatory core 0x4830.
```

However, that same block transposition removes every candidate for `0x4879`
and `0x4c39`.  It trades one static obstruction for two.

## 4. Exact static lower-candidate gate

Let `d_i` be the forced deadline offset, dropping from three to zero at the
three adjacent flat pairs, and let `P_j` be the maximal source envelope.
A strict lower target can only occur in a cell

```text
[i,i+ell-1],  1 <= ell <= d_i.
```

For such a cell define `E` as the union of its envelopes.  For each carrier
bit, if all its possible source positions lie inside the cell, that bit is
mandatory in the cell; let `M` be the union of those mandatory bits.  Any
exact occurrence of a lower target `S` necessarily satisfies

```text
M subseteq S subseteq E,
P_j intersects S for every physical position j in the cell.
```

The independent audit enumerates every mask satisfying these conditions in
every lower cell.  It obtains exactly one zero-candidate target for `u0` and
exactly two for `u1`, as displayed above.  A zero candidate is an exact
fixed-chronology no-go before any simultaneous Hall/COMP3 issue.

Therefore neither of the two upper-complete chronologies compiles to a word.
This does **not** rule out a nearby nonstandard rethread.

## 5. What was gained

The upper side is no longer the difficult part of the state-2 construction.
A three-cut block transposition solves it while retaining nonzero exact
maximal-envelope reconstruction and thousands of units of scalar capacity.
The remaining defect has been localized to one rank-seven mask in the better
candidate:

```text
0x4c71.
```

The next search should start from `u0` and create a lower cell for `0x4c71`
without losing upper coverage.  The `u1` witness shows one concrete geometry
that creates that host, and also identifies the two colours which must be
protected while importing it.  This is a much smaller specification than
the previous four-upper-hole chronology problem.

## 6. Reproducibility

```text
scratch/search_k16_resident_state2_exact_2opt3opt_20260730.cpp
scratch/audit_k16_resident_state2_2opt3opt_20260730.py
scratch/k16_resident_state2_2opt3opt_20260730/summary.json
scratch/k16_resident_state2_2opt3opt_20260730/independent.audit.json
```

The independent audit status is

```text
PASS_TWO_UPPER_COMPLETE_EXACT_CARRIERS_LOWER_COMPILER_OPEN
```

with payload SHA

```text
150573b156c0e509ea55c9e4a3620f2729d4a009b7cf58563c1a966fbc4f50dc.
```

