# `k=15`: residence-safe segment-splice reduction

Date: 2026-07-27

## 1. Audited input

The selected quotient factor

`scratch/k15_dual_descent_a4_step19.json`

has 17 physical cycles, covers every lower and upper shadow at every depth,
and has 45 forward depth-three residence violations.  Its 17-cycle status is
obtained from the canonical 73-cycle PBBS factor by exact zero-boundary
arity-three and arity-four trades.  Every intermediate factor remains
shadow-hole-free.

The 45 residence violations occur on only two physical cycles:

* a length-135 cycle, with 30 violations, hit optimally by 15 cut edges;
* a length-45 cycle, with 15 violations, hit optimally by 8 cut edges.

The cut indices below use the raw orientation returned by
`k15_pbbs_trade_lns.lift_cycles`; an index `c` means the directed edge
`cycle[c] -> cycle[(c+1) mod length]`.

```text
length 135: 6,15,24,33,42,51,60,69,78,87,96,105,114,123,132
length  45: 1,4,10,16,22,28,34,40
```

Optimality follows from exact branch-and-bound set cover on the violation
arcs.  A violation caused by an insertion at transition `i` and deletion
`t<=3` transitions later is removed exactly when a cut hits one of the
transitions `i,...,i+t`.

Cutting each of the other 15 physical cycles once yields exactly 38 linear
segments.  Thus a solution needs 37 new seams.

## 2. Why the count is exact

The original cyclic factor has 6,435 Johnson edges and uses every rank-seven
intersection colour exactly once.  Removing 38 edges and adding 37 seams
produces a Hamilton path with 6,434 edges.  Consequently exactly one
rank-seven colour must be absent.  This is the forced one-boundary flag in an
optimal odd-dimensional word; it is not a loss of efficiency.

For the 23 mandatory residence cuts alone, direct exhaustive counting gives

| depth | lower holes | upper holes |
|---:|---:|---:|
| 1 | 23 | 0 |
| 2 | 16 | 0 |
| 3--7 | 0 | 0 |

Thus the residence repair damages only the two lowest intersection shadows.
The new seams have exactly the right local support to restore them.

## 3. Exact finite target

For each chosen cut, orient the resulting segment as inherited from its
cycle.  Find a linear ordering of all 38 segments such that:

1. each of the 37 new endpoint pairs is a Johnson edge;
2. all but one of the 38 deleted rank-seven intersection colours are supplied
   by the new seams, with no collision against an internal colour;
3. the length-three windows crossing seams restore every deleted depth-two
   lower shadow;
4. every coordinate inserted at or immediately before a seam survives at
   least three transitions;
5. the upper shadows and all deeper lower shadows remain covered.

These conditions are local to at most four vertices around each seam, except
for the all-different use of segments and missing colours.  Therefore the
target is a finite exact-cover/Hamilton-path instance on 38 segments, not a
new 429-variable factor search.

If this path exists, the linear depth-three OR--Pascal compiler is the final
check.  The independent static-anchor certificate already proves that there
is no scalar or static Hall obstruction at `k=15`; only the global countdown
realization can still fail.

## 4. Scope

This reduction does not yet prove `nu(15)=6438`.  It replaces the previous
two simultaneous requirements—merge 17 cycles into one factor and remove 45
residence violations—by one smaller splice problem in which cutting is
allowed to perform both jobs at once.  It also avoids the unnecessary demand
that the intermediate object remain a cyclic factor: the final OR word needs
a path.
