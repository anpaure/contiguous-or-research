# Carrier3's K15 Pascal tower is transported by two exact reflections

Date: 2026-07-30

Status: exact finite theorem for the authenticated old and repeat-free K15
parents; constructive diagnostic, not a K16 completion.

## Statement

Let `A5,A6,A7` be the 19, 94, and 293 no-top layers of carrier3's
authenticated Hall shore.  Thus there are 406 labelled K15 Pascal targets.
Every one occurs exactly once as a literal interval in each of

```text
answers/k15.word
scratch/k16_carrier3_hall22_checkpoint_20260730/K15_REPEATFREE_SEED.word.
```

If a target has rank `s` and its unique interval starts at `p` in the old
word and at `p'` in the repeat-free word, then

```text
p + p' + (s-5) is exactly 3881 or 10271.
```

There are no exceptions.  The exact domain census is

| rank | `C=3881` | `C=10271` |
|---:|---:|---:|
| 5 | 0 | 19 |
| 6 | 66 | 28 |
| 7 | 173 | 120 |
| total | 239 | 167 |

The canonical widths are one, two, and three at ranks five, six, and seven.
The only boundary exception is `0x4879`, which is a singleton in the old word
and a width-three interval in the repeat-free word; its start still obeys the
same rank-normalized reflection law.

## Carrier explanation

Taking the third adjacent-OR derivative of each word gives two Hamilton paths
through the 6,435 rank-eight masks.  If `pi[i]` is the repeat-free position of
the old carrier's `i`-th mask, then `pi` consists of exactly four reversed
blocks:

```text
old 0..3833       -> repeat-free 3878..45
old 3834..6389    -> repeat-free 6434..3879
old 6390..6416    -> repeat-free 26..0
old 6417..6434    -> repeat-free 44..27.
```

The first two blocks are the two arcs of the 6,390-vertex component and the
last two are the arcs of the 45-vertex component.  The two carriers share
6,431 of their 6,434 path edges and differ only at their openings/junctions.
The constants `3881` and `10271` are precisely the first two carrier
reflection constants shifted by the derivative depth three.

Consequently, replacing the old parent wholesale by the repeat-free parent
does not destroy the Pascal Hall tower: it transports the tower exactly.
Any useful mixed-parent repair must cross the two large reflection domains or
alter one of the unique provider intervals.

## The missing K16 edges are two intact K15 motifs

The three K16 carrier edges whose absence accounts for the 22 private
provider motifs are

```text
287d--2c6d, 287d--6879, 4d39--4e39.
```

All three occur in every one of the six authenticated K15 carriers.  In the
old carrier they form the two subpaths

```text
6879--287d--2c6d at positions 0,1,2;
4d39--4e39       at positions 5727,5728.
```

In the repeat-free carrier the same motifs are reversed at positions
`3878,3877,3876` and `4541,4540`.  Carrier3 split their vertices across the
even-lift braid.  Thus the Hall-22 defect is exactly the loss of two parent
subpaths, not an unfamiliar K16-only obstruction.

## Authentication

```text
scratch/audit_k16_carrier3_k15_pascal_reflections_20260730.py
SHA 114839c9fb185b7cd1223efe71fdae02a1f0c9c22a01bb133438965092825872

scratch/k16_carrier3_hall22_checkpoint_20260730/
  k15_pascal_reflections.audit.json
SHA fe331619cfe3cc307a20367fe77344326f5e57011dc8f68d8586967dfe196542
payload 73a5a2fd2234b8367060ecdc90062ae2cf4026a091a2e8179d851acd113e76b4
```

Input word hashes:

```text
old        f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b
repeatfree 4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6
```

## Search disposition

Preserve the two displayed K15 motifs as indivisible blocks during the even
rethread.  A whole-parent replacement is provably neutral on the 406-target
tower, while a cross-domain braid can change its placement.  Hard-gate every
candidate by the three-flat `G=0` profile, exact maximal-envelope replay, and
all upper masks; then score the 22 private provider motifs before invoking
the full Hall compiler.
