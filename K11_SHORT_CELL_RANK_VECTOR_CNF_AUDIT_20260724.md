# Independent audit of the length-resolved short-cell rank-vector CNF

## Verdict

The theorem in `K11_SHORT_CELL_RANK_VECTOR_CUTS_20260724.md` and its opt-in
implementation in

```text
scratch/k11_core_incidence/k11_forest_sat_rankvectorcuts.cpp
SHA-256 15eb618401de15257621f6a1ef695110ad3d8ac84a45af4f539f839fa713b1a3
```

are sound as written.  This audit found no branch, range, polarity,
popcount, rank-flag, counter, schedule, or contaminated-triple error.

The exact predicted rank-vector-only increments are

```text
Type I:  31,137 variables / 209,120 clauses,
Type II: 31,378 variables / 210,756 clauses.
```

No production source was changed and no local CNF generation or solver was
run during this audit.

## 1. Physical length-resolved theorem

Let `P_r` and `T_r` be the numbers of active low pair and triple cells whose
actual OR rank is exactly `r`.  Let `T_ge_5` count active low triple cells
of rank at least five.

### Lower targets

In Type I and the two tight Type-II modes, every rank-at-most-four target
has a singleton/pair witness.  Distinct masks require distinct physical
cells, so

```text
n_r+P_r >= C(11,r),  r=1,2,3,4.
```

In the non-tight Type-II one-component mode the shortening radius is three,
giving

```text
n_r+P_r+T_r >= C(11,r),  r=1,2,3,4.
```

The `r=1` rows need not be encoded because the existing exact histogram
already imposes `n1>=11`.  In the two tight modes, the pair row implies the
weaker pair/triple row because the triple counter is an exact nonnegative
integer.

The implementation therefore correctly uses:

* Type I: pair rows unguarded;
* Type II: pair rows under `tight=duplicate OR two`;
* Type II: pair/triple rows under `!tight`.

The `tight` gate is bidirectional.  `duplicate` and `two` are exact and
mutually exclusive under the existing rank-filtration alternatives.

### Selected rank-five cells

The selected maximal rank-five schedule contains `y1` pair witnesses and
`y2` triple witnesses.  Therefore

```text
P5>=y1,
T5>=y2.
```

With `y1=even-odd` and

```text
Type I:  y2=462-n5-even+odd,
Type II: y2=462-n5+duplicate-even+odd,
```

the implementation's unsigned forms are exactly

```text
even <= P5+odd,

Type I:
  462+odd <= T5+n5+even,

Type II:
  462+duplicate+odd <= T5+n5+even.
```

No signed subtraction is encoded.

### Contaminated triples and the max corner

Each selected rank-five pair contaminates its incident triple cells.  A
contaminated triple is disjoint from the selected rank-five triple family:
if its rank is five, its OR equals that of the contained selected pair; if
its rank is larger, it cannot witness a rank-five target.

The exact distinct-triple incidence bound is

```text
u>=y1                         in one low component,
u>=max(y1-1+t1,0)             in two low components.
```

Hence

```text
T_ge_5 >= y2+max(y1-two+t1,0).
```

The source implements this without a max wire.  `T5>=y2` supplies the first
arm and the additional tail comparison supplies the second:

```text
Type I:
  T_ge_5+n5 >= 462,

Type II:
  T_ge_5+n5+two >= 462+duplicate+t1.
```

Their conjunction is exact at the important two-component corner
`y1=t1=0`: although the second row alone gives away one triple, `T5>=y2=q`
retains the baseline `T_ge_5>=q`.

No contaminated triple is counted twice when it is incident with two
selected pairs; `T_ge_5` counts physical triples, while the incidence lemma
already lower-bounds the number of distinct contaminated triples.

## 2. Pair/triple ranges and local OR vectors

The rank-vector module reuses the bidirectional coordinate-contribution
wires from the audited `R3` module.

| branch | pair cells | triple cells | reason |
|---|---:|---:|---|
| Type I | 463 | 462 | starts `1..463` and `1..462`; cells crossing rank-six `A[0]` are omitted |
| Type II | 464 | 463 | all physical starts |

Every cell is stored as one consecutive block of eleven contribution
literals.  An inactive cell contains a rank-five separator, so its eleven
contribution bits are all false.  Active blocks are exactly their physical
OR vectors.

The source checks divisibility by eleven before interpreting the flat banks;
there is no Type-I offset mismatch.

## 3. Exact local ranks

The existing Wallace/ripple routine uses ten full adders to count eleven
bits.  Its output is exactly four bits because a cell rank lies in
`0,...,11`.  The source's `resize(4)` therefore does not truncate an active
carry.

For each pair and triple cell, four flags are defined exactly:

```text
rank==2, rank==3, rank==4, rank==5.
```

For a fixed four-bit constant, the four forward implications plus one
reverse clause form an exact five-clause equality gate.

For triples, the high-rank flag is defined by

```text
rank>=6 <-> b3 OR (b2 AND b1).
```

This identity is valid for every four-bit unsigned value, not only the
reachable range `0,...,11`.  The four clauses in `define_at_least_six`
encode both directions:

```text
b3 -> high,
b2 & b1 -> high,
high -> b3 | b2,
high -> b3 | b1.
```

Thus `T_ge_5=T5+T_ge_6` is an exact addition of disjoint flag families.

## 4. Exact counters and arithmetic

The exact counter costs are:

```text
462 inputs -> 456 full adders -> 912 variables / 6,384 clauses,
463 inputs -> 460 full adders -> 920 variables / 6,440 clauses,
464 inputs -> 460 full adders -> 920 variables / 6,440 clauses.
```

There are four pair counters and five triple counters.  Consequently:

```text
Type I counters:  8,240 variables / 57,680 clauses,
Type II counters: 8,280 variables / 57,960 clauses.
```

All additions retain their final carry, and every variable comparison uses
the exact bidirectional prefix-equality comparator.  With a signed guard
`-tight`, prepending `-guard` correctly prepends the positive literal
`tight`, so the comparison is active exactly when `tight` is false.

## 5. Exact predicted source inventory

The operation-by-operation source mirror gives:

| category | Type-I variables | Type-I clauses | Type-II variables | Type-II clauses |
|---|---:|---:|---:|---:|
| per-cell 11-bit popcounts | 18,500 | 129,500 | 18,540 | 129,780 |
| exact rank flags, including triple `>=6` | 4,162 | 20,348 | 4,171 | 20,392 |
| pair/triple counters | 8,240 | 57,680 | 8,280 | 57,960 |
| exact `tight` branch gate | 0 | 0 | 1 | 3 |
| unsigned arithmetic | 176 | 1,232 | 296 | 2,072 |
| exact comparators | 59 | 360 | 90 | 549 |
| **rank-vector-only total** | **31,137** | **209,120** | **31,378** | **210,756** |

The flag counts use the optimized four-clause high-rank gate; this improves
on the conservative sixteen-row estimate in the theorem note.

Added to the audited histogram plus `R3` formulas, the expected complete
inventories are

```text
Type I:  3,742,531 variables / 20,651,922 clauses,
Type II: 3,762,230 variables / 20,754,457 clauses.
```

These totals remain predictions until checked by the RunPod build report
and an independent DIMACS token audit.

## 6. Deployment checklist

1. Keep `K11_FOREST_SHORT_CELL_RANK_VECTOR` separately opt-in and require
   `K11_FOREST_SHORT_CELL_R3`.
2. Expose the `R3` pair/triple contribution banks and exact `t1` vector by
   reference only; disabled inventories must remain unchanged.
3. Preserve the Type-I suffix-only and Type-II all-start cell ranges.
4. Require every local rank equality and `>=6` flag in both directions.
5. Retain all final counter and arithmetic carries.
6. Define `tight <-> duplicate OR two` exactly.
7. Use the pair lower rows in Type I and under `tight` in Type II; use the
   pair/triple rows under `!tight` in Type II.
8. Enforce both selected-schedule rows `P5>=y1` and `T5>=y2`.
9. Enforce the contaminated-triple tail row in addition to `T5>=y2`; neither
   alone handles every max branch.
10. Confirm category counters against the exact table above.
11. On RunPod, compare the full DIMACS inventory, maximum literal, and
    declared variable count before starting any solver.
12. Do not replace existing exhaustive branch coverage merely because the
    stronger formula is available.

## 7. RunPod confirmation and first immutable branch

The frozen source was copied byte-for-byte to RunPod Rose and compiled there
with `-O3 -std=c++2a -Wall -Wextra -Wpedantic`.  Compilation produced zero
warning bytes.

```text
source SHA-256:
15eb618401de15257621f6a1ef695110ad3d8ac84a45af4f539f839fa713b1a3

RunPod streaming binary SHA-256:
30e200941dc619457a1a501bebe6e45f7ea013be1dab8ff4ed1b193fcb4de813
```

Build-only streams to `/dev/null` reported exactly the two predicted complete
inventories:

```text
Type I:  3,742,531 variables / 20,651,922 clauses,
Type II: 3,762,230 variables / 20,754,457 clauses.
```

Every internal category counter also matched Section 5 exactly.  Both
branches were then materialized and independently scanned token by token:

```text
Type I:
p cnf 0003742531 000020651922
maxvar=3742531 clauses=20651922
SHA-256 c888989126ede379322b613a77c29eeeb835cf9f32ac91effbdb8fbbf11c9ec3

Type II:
p cnf 0003762230 000020754457
maxvar=3762230 clauses=20754457
SHA-256 93b3ece194b2119d0a962cc7c548fa12d5dd0a2d21283a8504a5c59c02842343
```

All generation and scanning ran on RunPod.  The cgroup OOM-kill counter
remained 35.  After confirming that external Type-II histogram seed 451 had
no terminal marker or candidate, it was replaced at unchanged concurrency by
rank-vector seed 461 under the same 4 GiB cap.  The older integrated Type-II
baseline remains live.  The corresponding Type-I histogram run likewise had
no terminal marker or candidate and was replaced by rank-vector seed 471
under the same 3 GiB cap, while all three older integrated Type-I baselines
remained live.  Thus exhaustive branch coverage was not removed in either
branch.
