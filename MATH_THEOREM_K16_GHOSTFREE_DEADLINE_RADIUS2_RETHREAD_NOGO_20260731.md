# K16 ghost-free schedule: exact one/two-deadline rethread no-go

**Date:** 2026-07-31  
**Status:** solver-free finite theorem; fixed target order and row labels only

## Result

Consider the length-12873 generalized schedule in
`MATH_CONSTRUCTION_K16_GHOSTFREE_GENERALIZED_SCHEDULE_20260730.md`.  Keep
every row start and rank-eight row label fixed, and change the right endpoint
of at most two physical schedule rows.  Require nondecreasing deadlines,
`G=0`, and nonzero maximal envelopes which still realize every scheduled
row.

> **Theorem.** No such one- or two-row deadline rethread makes even one of
> the four forced upper targets
>
> ```text
> c679 ca79 ea79 eb79
> ```
>
> feasible under the exact generalized envelopes.

There are exactly twelve admissible endpoint assignments in the relaxed
maximal-envelope model, and all twelve fail the four targets separately.
Consequently a successful schedule-level repair of this fixed target order
must change at least three physical row deadlines, or must change a row
label/order or introduce a stall/jump.

## Why the radius-two search collapses to twelve cases

Equal deadlines of delivery rows force equal rank-eight labels: the two
interval unions are nested sets of the same rank.  Conversely `G=0` forces
all repeated occurrences of one label to share one deadline.  Collapse the
schedule into its consecutive same-label groups.  It has

```text
12870 groups: 12867 singletons and 3 groups of multiplicity 2.
```

A singleton group costs one changed physical row; a double group costs two.
The group deadlines use every integer in `[0,12872]` except

```text
0, 2, 3.
```

More explicitly, group zero has deadline `1`, and every group `g>=1` has
deadline `g+3`.  Thus all deadlines after the initial three-hole prefix are
packed consecutively.

The support of a changed deadline assignment splits into consecutive group
blocks.  Between two unchanged neighbouring groups, a block must inject its
deadlines into the open integer interval between the two fixed deadlines.
Every block beginning at group `2` or later has exactly as many available
integers as groups, so its original assignment is forced.  A nonadjacent
pair of changed groups acts independently and gives no additional cases.
At physical cost at most two, the only movable supports are therefore

```text
{0}, {1}, {0,1}, {1,2}.
```

The complete list of nontrivial endpoint assignments is:

```text
q0:       1 -> 0, 2, or 3
q1:       4 -> 2 or 3
(q0,q1):  (1,4) -> (0,1), (0,2), (0,3), or (2,3)
(q1,q2):  (4,5) -> (2,3), (2,4), or (3,4)
```

All twelve have nonzero maximal envelopes and retain every fixed scheduled
row.  Their only envelope changes occur at physical positions `1..5`.

## Exact upper-target test

For a candidate schedule with maximal envelopes `P_i` and an upper target
`U`, any witness interval `[s,e]` must lie in one maximal run on which
`P_i & U` is nonzero.  For a fixed start `s`, take the earliest `e` for which

```text
OR_{i=s}^e (P_i & U) = U.
```

Inside this interval every physical cell is restricted to `P_i & U`; outside
it the cell retains its full envelope `P_i`.  The interval is compatible
with the schedule exactly when every scheduled row still has its full target
in the OR of these allowed envelopes.  If the earliest endpoint suppresses
the last host of a required outside-`U` bit, a longer endpoint only suppresses
more hosts, so it cannot repair the row.  Testing the earliest endpoint is
therefore exact.

For every one of the twelve rethreads the audit returns:

| target | compatible starts | schedule-feasible starts |
|---:|---:|---:|
| `c679` | 6446 | **0** |
| `ca79` | 6447 | **0** |
| `ea79` | 6447 | **0** |
| `eb79` | 8780 | **0** |

The counts and dominant blockers are unchanged from the original schedule.
For the first three targets the largest primary blocker remains scheduled row
`12544..12546`, target `96a6`, required bit `0002`; for `eb79` it remains
row `6144..6147`, target `6c74`, required bit `0004`.  These blockers are far
outside the only mutable envelope positions `1..5`.

## Scope

This closes exactly the radius-two **deadline-only** rethread with fixed row
starts, target order, and row labels.  It does not close:

1. three or more changed physical deadlines;
2. a target-order rethread or row relabelling;
3. replacing a delivery row by a stall or jump while retaining total waste
   three;
4. a nonlocal schedule construction followed by a new compiler.

The result explains why the four-hole common core cannot be repaired by a
small deadline perturbation: the only three unused deadlines are all at the
left boundary, while the exact upper blockers live deep in the schedule.

## Reproducible artifacts

- `scratch/audit_k16_ghostfree_deadline_radius2_rethread_20260731.py`
  - SHA-256 `838ae80be3ed4ce074e7bf60a24d01dcb4efe0d486c7a758e1fb593acce847d5`
- `scratch/k16_ghostfree_deadline_radius2_rethread_20260731.audit.json`
  - SHA-256 `d00f7853d13097ac3148758ce7a50099f2f5b9cbea9e77567b1f6e2bc1e7917a`
  - payload SHA-256 `67092c0d7600f8b5f0280ba776c0b586359059dc8368215068a0e5158615d014`

