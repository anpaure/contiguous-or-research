# Audit of the K16 upper-complete singleton-capped P/Q dynamic programme

**Date:** 2026-07-31  
**Status:** exact correction; the proposed `21878+9` capacity no-go is false

## 1. Frozen carrier and question

Fix

```text
scratch/k16_facet_augmented_uppercomplete_capacity27597_targets_20260731.word
SHA-256 63aababe9d5cbaeec4ce68a1ec32edc02d249caf3750bb20f6bc87c1ca1eac43.
```

It is squarefree on all `C(16,8)=12870` middle targets, has the complete
rank-nine adjacent palette, and its target chronology covers every upper
mask at every rank.  A hypothetical equality word has length `12873`, hence
its monotone middle skeleton has three omitted starts and three omitted
deadlines.

The proposed stronger audit required one exact physical interval for the
lower singleton `0x8000` and reported maximum selected area `21878`, hence
capacity `21878+9=21887<26332`.  That numerical claim is invalid.

## 2. Exact bug

The pin automaton used the documented states

```text
-1 = not started,
 3,2,1 = active cells remaining,
 0 = completed.
```

After processing a cell, however, the first version applied

```python
if current_pin == -1:
    next_pin = -1
elif current_pin == 1:
    next_pin = 0
else:
    next_pin = current_pin - 1
```

to `current_pin=0`.  Thus a completed pin changed from `0` back to `-1` on
the next physical cell.  Since the terminal state demanded `pin=0`, the
programme silently required the chosen pin to end at physical position
`12872`.  It did not enumerate singleton pins at arbitrary positions.

The correction is the absorbing transition

```python
if current_pin in (-1,0):
    next_pin = current_pin.
```

## 3. Literal counterexample to the stale bound

Take

```text
start holes    X = {5718,10950,10951},
deadline holes Y = {10,12,13}.
```

Pair the retained starts and deadlines monotonically.  Their selected area
is exactly

```text
sum X - sum Y = 27584.
```

Let `E_p` be the intersection of all prescribed middle targets active at
physical position `p`.  At `p=5717`,

```text
active rows         = {5714,5715,5716,5717},
E_5717              = 0xa045,
E_5717 & 0x8000     = 0x8000.
```

Set the physical letter at `5717` to `0x8000` and every other letter to its
maximal envelope `E_p`.  Direct row-by-row replay gives

```text
middle failures = 0,
maximum span    = 3,
singleton OR    = 0x8000.
```

Therefore this is a literal member of the claimed singleton-pinned P/Q
family with selected area `27584>21878`.

## 4. Corrected exact DP theorem

### Theorem 4.1

For the frozen target order above, among all three-start-hole,
three-deadline-hole monotone P/Q schedules whose maximal-envelope replay
survives one exact `0x8000` interval of length one, two, or three, the maximum
selected area is

```text
27584.
```

One maximizing witness is the schedule in Section 3, with a length-one pin
at `5717`.  Granting the three omitted starts their full boundary credit
gives

```text
27584+9 = 27593 = 26332+1261.
```

Hence the forced singleton consumes only four units relative to the
unconstrained maximum `27588`; it does **not** yield a capacity obstruction.

### Proof

At position `j`, let `x,y` count the start and deadline holes already used,
and let the queue record, for each active middle row, the OR accumulated so
far.  The active rows are the contiguous block determined by `j,x,y`.  An
unpinned cell may be enlarged to their common envelope.  During the pin,
every nonzero letter is forced to `0x8000`, because a union equals a
singleton iff every participating nonzero set is that singleton.  The pin
state records whether it has not started, has one to three cells remaining,
or is completed.

Thus all future legality is determined by

```text
(j,x,y,active accumulated ORs,pin state).
```

For an identical state, retaining only the largest partial value of
`sum X-sum Y` is exact: every future transition and future area increment is
identical.  The corrected completed state is absorbing, so every possible
pin start and length is represented.  Exhausting the finite recurrence gives
`27584`.  The independent literal replay in Section 3 verifies the emitted
witness.  QED.

An exact singleton interval of any positive length automatically contains a
length-one singleton occurrence.  Thus checking lengths at most three does
not omit a longer singleton witness.

## 5. What remains true about the compiler gate

The unconstrained area-maximizing schedule

```text
X={5722,10950,10951}, Y={10,12,13}
```

is still impossible: `0x8000` has no individually legal prefix host there,
and its relaxed lower Hall graph is deficient.  This is a theorem only about
that schedule.

The corrected singleton-compatible schedule is not thereby a compiler.  An
exact individual-prefix audit has `27593` slots, gives `0x8000` exactly one
host, but leaves `1477` other lower targets with no individual host
(`27` of rank six and `1450` of rank seven).  Hence that displayed schedule
also fails.  What is **not** closed is the schedule-wide question: another
P/Q schedule could trade area for hosts of different compulsory targets.
A simultaneous lower Hall/common-cap argument, or a DP carrying a genuinely
decisive family of target pins, is still required.

The upper gate is not involved here: the frozen target chronology is already
complete at every upper rank.

## 6. Reproducible artifacts

- corrected exhaustive DP:
  `scratch/audit_r_k16_facet_uppercomplete_singleton_capacity_dp_20260731.py`,
  SHA-256 `7cca0e185f4830b51468f99ebf4a0afedd36d0fdb461d04c269e950c8589a14b`;
- corrected DP audit:
  `scratch/k16_facet_uppercomplete_singleton_capacity_dp_20260731.audit.json`,
  SHA-256 `91f112e0505d5f4339e0029c028be78feacbbae112119d9f34c0d5d1984e552e`,
  payload SHA-256 `39ec4de6f815317d5e96140eb5dd7e2e167e850992b5179ae52e339981ae9aa1`;
- independent literal replay:
  `scratch/audit_r_k16_uppercomplete_singleton_counterexample_20260731.py`,
  SHA-256 `e039ff25316e2ffbfc2dda526ac277b3f64755d63431fcddf3fb850d947d512d`;
- replay payload:
  `scratch/r_k16_uppercomplete_singleton_counterexample_20260731.audit.json`,
  SHA-256 `e992e830b0087e5d415bfe3a80801fc6172964bd97a100bebe515d8e2b96e79d`,
  payload SHA-256 `7b37a59b066656ec4828e59a29f0544514c32fca3ffeae23181ac2b63cc8df85`.

The literal replay is deliberately independent of the DP implementation: it
constructs the monotone schedule and every maximal envelope from scratch and
checks all `12870` middle rows directly.
