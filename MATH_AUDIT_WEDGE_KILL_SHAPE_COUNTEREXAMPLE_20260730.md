# Audit: the unrestricted wedge kill-shape lemma is false

The wedge identity itself is correct: if coordinate `x` is absent at a
Johnson-cycle vertex `C[v]` and present at both neighbours, then the two
flanking adjacent unions are both `C[v] union {x}`.  In particular those
two edge occurrences have a repeated rank-`r+1` colour.

The stronger claim that every fragile target whose kernel contains a wedge
edge has rank exactly `r+2` is false for an unrestricted Johnson cycle even
at the required odd middle rank `r=(k+1)/2`.  Consider the following cycle
in `J(9,5)`, in one-based set notation:

```
12389, 12489, 13489, 13589, 15689, 15789, 12789.
```

At vertex `12489`, coordinate `3` is absent and is present at both neighbours
`12389` and `13489`.  Thus this is a wedge, and both flanking unions equal
`123489`.

Let `Y=12345689`, which has rank `8=r+3`.  The only cyclic vertex intervals
whose OR equals `Y` are

```
12389,12489,13489,13589,15689
12489,13489,13589,15689.
```

Their internal edge spans are respectively `{0,1,2,3}` and `{1,2,3}`.
Consequently `kernel(Y)={1,2,3}`, which contains the wedge's right edge.
So a rank-`r+3` fragile target can kill a wedge edge.

The exact reproducer is
[audit_wedge_kill_shape_counterexample_20260730.py](scratch/audit_wedge_kill_shape_counterexample_20260730.py).

This does **not** refute a narrower theorem for the protected all-depth
factors used by the odd-dimensional construction.  It shows that such a
theorem needs an explicit extra hypothesis and proof; the observed absence
of rank-`r+3` wedge killers at `k=13,15` is not a consequence of the local
wedge algebra alone.  The safe-cut strategy may still use either:

1. an independently imposed/checkable safe-wedge condition in `(E1)`; or
2. a global dispersion/counting lemma specific to protected factors.

Until one of those is proved, the wedge census is strong finite evidence but
does not close `(SPILL)` for general `k`.
