# K16 facet target: sharp three-hole P/Q staircase no-go

**Date:** 2026-07-31  
**Status:** exact solver-free dynamic programme; fixed target order

## Result

Fix the facet-augmented rank-eight target order

```text
scratch/k16_facet_augmented_middle_targets_20260731.word
SHA-256 9712d02ebfb97c4a773caa90c0933eea78f30834162c462f4dd50692186b6550
```

from `MATH_THEOREM_K16_FACET_COLOUR_AUGMENTATION_20260731.md`.  It contains
every rank-eight mask exactly once and preserves the complete rank-nine
colour multiset.  Under the source three-hole P/Q staircase, its maximal
envelopes are nonempty but fail exactly six scheduled rows in the three
clusters `3287..3289`, `5189..5190`, and `6077`.

> **Theorem.** Among every monotone length-12873 P/Q staircase with arbitrary
> three start holes `X` and arbitrary three deadline holes `Y`, the maximum
> selected lower-cell area for which this fixed target order is realizable in
> its maximal envelopes is
>
> ```text
> 16876.
> ```
>
> The required lower-ideal count is `Lambda=26332`.  Even granting the three
> unselected columns their maximum possible three lower cells apiece gives
>
> ```text
> 16876 + 9 = 16885 < 26332.
> ```
>
> Hence this target order cannot be the middle chronology of a universal
> equality word, for any ghost-free waste-three P/Q rethread.

The maximizing realizable staircase is unique:

```text
start holes     X = {3290, 12871, 12872}
deadline holes  Y = {0, 6078, 6079}
```

It repairs all six scheduled-row failures and has no empty envelope, but its
span histogram is only

```text
0^2787 1^3290 2^6793,
```

so it loses far too much lower capacity.  Relative to the source staircase,
it moves one start hole from `6432` to `3290`, one from `12869` to `12872`,
and moves deadline holes `2,3` to `6078,6079`.  This is the sharpest possible
fixed-order rethread, not merely a local candidate.

## The exact P/Q model

Let `L=W+3=12873`, with fixed targets `T_0,...,T_(W-1)`.  Select starts

```text
P = [0,L) minus X
```

and deadlines

```text
Q = [0,L) minus Y,
```

where `|X|=|Y|=3`.  Pair their sorted elements monotonically.  Any universal
length-12873 word with `G=0` induces such a selected skeleton after keeping
the latest start in each middle-target deadline group.  Each selected span
is at most three.

For fixed `P,Q,T`, the maximal legal physical cell at position `j` is the
intersection of all active targets.  The schedule is realizable exactly when
these intersections are nonzero and their OR over every selected interval
recovers that interval's target.

## Sixteen-state recurrence

Scan physical positions `j=0,...,L-1`.  Before position `j`, let

```text
x = number of start holes before j,
y = number of deadline holes before j.
```

Let `ex=1[j in X]` and `ey=1[j in Y]`.  If `ex=0`, target row `j-x` starts
and a zero accumulator is appended.  The active target rows at `j` are
exactly the contiguous block

```text
T[j-y .. j-x-ex].
```

Their intersection is the maximal envelope `E_j`; reject the transition if
it is empty.  OR `E_j` into every active accumulator.  If `ey=0`, row `j-y`
ends, so its first accumulator must equal `T[j-y]`, after which it is popped.
Finally set

```text
x <- x+ex,  y <- y+ey.
```

The area increment is

```text
j(ex-ey),
```

because the final sum is the exact identity

```text
sum_i(q_i-p_i) = sum(X) - sum(Y).
```

At a fixed `j`, all future feasibility depends only on

```text
(x, y, tuple(active accumulated ORs)).
```

For identical states, a smaller accumulated area is dominated and can be
discarded.  This proves the dynamic programme exactly maximizes area rather
than sampling hole locations.  It never has more than 16 live states.  The
terminal condition is

```text
x=y=3 and the accumulator queue is empty.
```

The unique maximum is the staircase displayed above.

## Authentication against the source schedule

The source one-hole word has

```text
X_source = {6432,12869,12871}
Y_source = {0,2,3}.
```

Assigning the new target order to this staircase reproduces exactly the six
reported failures:

| row | missing bit |
|---:|---:|
| 3287 | `0008` |
| 3288 | `0008` |
| 3289 | `0010` |
| 5189 | `0010` |
| 5190 | `0010` |
| 6077 | `0200` |

There are no empty envelopes.  Thus the DP starts from the authenticated
physical gate, not merely from the carrier order.

## Scope

This is a sharp no-go for the fixed target order SHA `9712d02e...` over the
entire architecture-free three-hole P/Q family.  It does not exclude:

1. a different pair of facet-colour augmenting trails, hence a different
   rank-eight target order;
2. changing the target order after the augmentation;
3. a schedule outside the selected three-hole P/Q skeleton;
4. the separate deeper-upper defect `0x6f79` of this carrier order.

## Reproducible artifacts

- `scratch/audit_k16_facet_target_pq_threehole_dp_20260731.py`
  - SHA-256 `43b126f4cb7b755ccacb240b333c35fa6509cc614220780631ca8df5b764bf60`
- `scratch/k16_facet_target_pq_threehole_dp_20260731.audit.json`
  - SHA-256 `fc95ed0ff2eb9f61d999d76b1831f98347d2f914dc9514ce0ae01fb7dde843ed`
  - payload SHA-256 `9c84cf2e90acfda3fc8ced71127a311ecfc7e71d28a056ea6ce7ce1668f785b0`

