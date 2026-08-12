# K16 all-deletion target-block automaton

Date: 2026-07-31  
Status: exact structural reduction; all 116,073 hole incidences replayed  
Global bracket: `12873 <= nu(16) <= 12874` (unchanged)

## 1. Purpose

The survivor-bit theorem removes the literal first-value explosion once the
deletion word's holes, vulnerable targets, and service intervals are known.
Rebuilding those objects independently for all 12,874 deletions would waste
the main common structure.

This note gives one shared automaton on the original length-12874 source.  It
is target-first rather than deletion-first.  Deleting a cell changes only one
local state of the automaton for each target.  Physical positions are retained
as interval/bitset records, so this is not the unsound transition quotient
which identifies different first sites or values.

## 2. Compatible blocks

Fix a word `X=(x_0,...,x_(N-1))` and a nonzero target `t`.  Call position `i`
`t`-compatible when

```text
x_i subseteq t.
```

The compatible positions split into maximal consecutive blocks.  For a block
`B`, store

```text
s(B)       = OR_{i in B} x_i,
first_B(a) = first position of coordinate a in B,
last_B(a)  = last position of coordinate a in B,
count_B(a) = number of cells of B containing a.
```

Call `B` full when `s(B)=t`.

### Lemma 2.1 (coverage)

An interval has OR `t` iff it lies in one `t`-compatible block and contains
at least one occurrence of every coordinate of `t`.  Hence `t` is covered iff
there is a full block.

This is immediate: an interval with OR `t` contains no cell outside `t`, and
the whole compatible block has OR at most `t`; conversely a full block itself
is a witness.

### Lemma 2.2 (witness core)

If there are two full blocks, the intersection of all `t`-witness intervals
is empty.  If `B` is the unique full block, put

```text
left_core(B,t)  = min_{a in t} last_B(a),
right_core(B,t) = max_{a in t} first_B(a).             (2.1)
```

The exact witness core is

```text
K_X(t) = [left_core,right_core]
```

when `left_core <= right_core`, and is empty otherwise.

Indeed every witnessing interval starts no later than the earliest last
occurrence in (2.1), and ends no earlier than the latest first occurrence.
Both extremal endpoints are attained by extending to the opposite end of the
full block.

Thus a covered target is vulnerable to editing physical site `p` exactly when
`p in K_X(t)`.

## 3. Service intervals from the same blocks

Replace the cell at site `p` by `u`.  Let `C_t(p)` be the OR of the maximal
`t`-compatible suffix immediately before `p` and prefix immediately after
`p`.  The edit supplies or preserves `t` exactly for

```text
t minus C_t(p) subseteq u subseteq t.                 (3.1)
```

The block automaton gives `C_t(p)` without enumerating intervals:

1. If `p` lies in compatible block `B`, then

   ```text
   C_t(p) = OR_{i in B, i != p} x_i.                   (3.2)
   ```

2. If `p` lies in an incompatible gap, the left block contributes `s(B_L)`
   exactly when `p` is the first position of the gap, and the right block
   contributes `s(B_R)` exactly when `p` is the last position.  A singleton
   gap receives both; an interior point of a longer gap receives neither.

For a vulnerable `p` in the unique full block, (3.2) simplifies further:

```text
t minus C_t(p)
  = {a in t : p is the unique occurrence of a in B}.  (3.3)
```

So the vulnerable-target part of the survivor-bit index consists of one core
interval plus at most `|t|` exceptional physical sites, not a general
position-by-value table.

## 4. Exact deletion transition

Delete source position `d`.

* If `d` is compatible and belongs to block `B`, only that block changes: it
  becomes `B minus {d}` after index contraction.  Its OR, first/last
  occurrences, unique coordinates, full status, core, and service records are
  updated from the stored per-coordinate counts.
* If `d` is incompatible and is a singleton gap, its two neighboring
  compatible blocks merge, with payload the OR of their payloads.  No other
  block changes.
* If `d` lies in a longer incompatible gap, no compatible blocks merge.
  Only the one or two gap-endpoint service records exposed by shortening the
  gap change.

This is the promised bounded OR halo.  A deletion never requires rebuilding a
target's interval family.

There is also a sharp critical-site bound.  Inside a compatible block, a
deletion can change

* full status only at a cell uniquely carrying some coordinate;
* the witness core only at a first or last occurrence; and
* another site's service lower bound only at a cell participating in a
  coordinate of block multiplicity at most two.

The union has at most `4|t|` physical positions per block.  Every other
compatible deletion has the baseline automaton state, modulo the contracted
index.  Wide changes from incompatible deletions occur only at singleton gaps;
longer gaps have only constant-size endpoint corrections.

## 5. Target-first deletion-hole theorem

### Theorem 5.1

For a universal source word, deleting `d` makes target `t` a hole iff

1. `t` has exactly one full compatible block `B`;
2. `d in B`; and
3. `d` uniquely carries at least one coordinate of `t` within `B`.

**Proof.** If `d` is incompatible, every old full block persists and deletion
can only merge compatible blocks, so coverage cannot be lost.  If `d` is
compatible, every block other than its own persists.  Coverage is therefore
lost exactly when its block was the unique full block and removing `d` makes
its OR a proper submask of `t`, which is condition 3.  QED.

Distinct hole-producing cells in one block own distinct coordinates.
Consequently

```text
number of deletions making t a hole <= rank(t),
sum_t number of hole incidences <= K * 2^(K-1).        (5.1)
```

At `K=16`, (5.1) gives the unconditional ceiling `524,288`, independent of
word length.  The frozen source has only `116,073` incidences.

## 6. Exact shared provider index

The complete all-deletion provider-first engine can now be built without
materializing 12,874 deletion words.

1. Build every target's compatible-block automaton once.
2. Emit deletion holes target-first by Theorem 5.1.
3. For a deletion `d`, apply only the local transition of Section 4 to targets
   whose touched block/gap state changes.
4. Recompute vulnerable contributions from the updated unique-full block and
   (2.1).  For survivor bit `b`, a vulnerable target contributes only when
   `b notin t`; its interval is `[E_B(p),t]`, with `E_B(p)` given by (3.3).
5. Accumulate upper restrictions as range counters on the core interval and
   lower restrictions as at most `|t|` point counters.  Local deletion events
   subtract the old range/points and add the new ones.
6. For each deletion hole, group all physical provider sites by the exact
   context in (3.2) and the gap rule.  Keep each group as a position bitset or
   interval list.  Values remain Boolean intervals and physical positions
   remain distinct for the exact second sweep.

For a target with blocks `B_1,...,B_s`, the provider-site context partition
has one generic class per block, at most `K` essential-site exceptions per
block, two endpoint classes per incompatible gap, and one common interior-gap
class.  Multiple essential deletions of the same hole target reuse this one
partition; only the unique full block receives a point correction.

This replaces the `12,873 * 116,073 = 1,494,207,729` raw canonical
position/hole incidences by a reusable target-block catalogue.  It is a data
structure reduction, not a claim that the remaining exact second-stage work
is constant.

If `R` is the total number of compatible blocks over the targets retained in
the catalogue, its explicit record size is

```text
O(KR + K*2^K + N*2^K)                                (6.1)
```

with only range/point updates per deletion.  Compatibility bitsets for all
targets can alternatively be built by subset-zeta OR in

```text
O(K * 2^K * ceil(N / word_size))                      (6.2)
```

machine-word operations.  Neither (6.1) nor (6.2) has the extra factor `N`
caused by rebuilding every deletion basin.

## 7. Complete K16 hole audit

The target-first implementation was checked against every row of the frozen
all-deletion table.  It scans only the 51,154 distinct targets which occur as
deletion holes, reconstructs their full compatible blocks, and emits their
essential cells.

```text
distinct hole targets                 51,154
recorded deletion-hole incidences    116,073
reconstructed incidences             116,073
targets with one full block           51,154 / 51,154
maximum deletions for one target            5
all compatible blocks             14,393,749
compatible cell visits            17,725,217
```

The exact deletion multiplicity histogram is

```text
1: 8,080
2: 24,731
3: 15,001
4: 3,182
5: 160.
```

The remote solver-free replay used 6 MiB RSS and under one wall second.  The
runtime is calibration only; the theorem is the block identity above.

Artifacts:

```text
scratch/audit_k16_all_deletion_hole_block_automaton_20260731.cpp
  SHA-256 aa06d2b1094b356c17d1747c1a46d0054fdbfb51e2ae04e2ec0f32a21885218e

scratch/k16_all_deletion_hole_block_automaton_20260731.audit.json
  SHA-256 2bf3e36091c522c50aa6c25635f65a5ae65e3b9e84d13b3873341c367ddf3359
```

## 8. What remains

The automaton removes repeated basin construction and gives an exact shared
first-provider index.  It does not itself close all deletions.  The remaining
implementation step is to connect each retained physical first-site bitset to
the already-proved maximal-second-value/target-core sweep while keeping exact
site identities.  A negative D5/all-deletion result still requires complete
shard accounting and independent replay.

No claim about `nu(16)` changes here.

