# Independent audit of the quartet integral face resolver

## 0. Verdict

The main theorem of `QUARTET_INTEGRAL_FACE_RESOLVER.md` is correct and
strictly stronger than the proposed catalog-resolution statement:

* every deterministic quartet wreath partition already contains every
  lower and upper target as an abstract cube face;
* choosing one complete catalog member gives a disjoint integral middle
  partition with zero face deficit; and
* arbitrary switching by whole rank-vector sectors preserves this result.

The theorem does **not** produce consecutive cycle windows.  The source
note correctly isolates a severe face-to-window thinning and cites the
zero-pivot fixed-matching capacity obstruction as an explicit separation.

## 1. Audit of the local lemmas

Fix one matching of a quartet.

For a local lower target of rank `s<=2`, at least `2-s` matching edges are
empty: `s` selected coordinates can meet at most `s` of the two edges.
Consequently any `r<=2-s` empty edges can be promoted to free edges.  The
intersection over those `r` directions removes both endpoints of each and
restores the target exactly.

For an upper target of rank `s>=2`, at least `s-2` matching edges are full.
This is the pigeonhole dual of the preceding statement.  Demoting any
`r<=s-2` full edges to free edges produces a face whose union is the target.

Both arguments hold for all three local frames.  The pair block in odd
dimension has the identical statements around baseline rank one.  No
compatibility between sector frames is used.

## 2. Audit of the global deficit allocation

Let `b_j` be two for a quartet and one for the optional leftover pair.
For a lower target with local ranks `s_j`,

\[
 \sum_j(b_j-s_j)=q.                                  \tag{2.1}
\]

Even if some summands are negative, the sum of their positive parts is at
least `q`.  Hence integers `r_j` can be selected with

\[
 0\le r_j\le(b_j-s_j)_+,
 \qquad\sum_jr_j=q.                                  \tag{2.2}
\]

The rank vector `t_j=s_j+r_j` sums to `m`.  In every changed block it lies
between the target rank and the local baseline, exactly the range covered by
the local lower lemma.

The apparent circularity--the frame depends on `t`--is harmless.  The rank
vector is selected using only the local ranks and capacities; after that,
whichever frame the wreath function assigned to `t` satisfies the
frame-independent local lemma.

Replacing positive deficits by positive surpluses proves the upper side.
The Cartesian product of the local faces has dimension `sum r_j=q` and is
contained in one actual product cell.  This verifies all endpoint cases,
including the empty and full targets at `q=m`.

## 3. Integral-selection quantifiers

A complete wreath member is already a partition of the entire middle
layer.  Selecting all cells of one member assigns every source exactly once
and creates no overlap.  The face theorem is universal over the frame
function, so that same selected member covers every target.

Thus the assumptions

* `R=Theta(m2^H)`, and
* every nested source--target pair occurs somewhere in the catalog

are unnecessary for targetwise face coverage.  They may still matter as a
reservoir for ordered windows, but not for the integral face resolver.

The theorem covers each target somewhere.  It does not claim that every
prescribed nested pair survives after selecting one member; the latter is a
strictly stronger and generally false demand.

## 4. Audit of the face-to-window count

In a physical `d`-cube, choose `q` varying directions and orient the other
`d-q` directions.  This gives exactly

\[
 \binom dq2^{d-q}                                    \tag{4.1}
\]

lower faces, and the same number of upper faces.

A cycle factor using each cell vertex once has only `2^d` cyclic starts.
A window whose intersection drops rank by exactly `q` must delete `q`
different selected coordinates without restoring them, hence must use a
geodesic sequence of distinct effective directions.  Each start therefore
exposes at most one lower and one upper target.  The ratio

\[
 \min(1,2^q/\binom dq)                               \tag{4.2}
\]

is valid.  The elementary bound `binom(d,q)>=(d/q)^q` gives the displayed
`(2q/d)^q` estimate.

This is only a local trace bound because the same Boolean target may occur
in several cells.  The source note does not incorrectly turn it into a
global omission count.

## 5. Audit of the fixed-frame separation

A constant sector frame reconstructs the ordinary cube partition of one
global coordinate matching.  The face theorem gives exact abstract
coverage there.

For any geodesic window using only those native matching directions, the
number of full native pairs is unchanged between its middle source and its
lower intersection.  The source and target full-pair distributions separate
by `Theta(q)` at `q=c sqrt(m)`.  The fixed-type capacity argument recorded
in `PIVOT_SHADOW_CAPACITY.md` then gives a positive-proportion target band
with too few eligible source windows.  Its zero-pivot specialization yields
`Omega(W)` omissions, after the standard large-cell and seam hypotheses.

Thus abstract integral face coverage can coexist with macroscopic
consecutive-window failure.  The sector-dependent construction is outside
the fixed-matching hypothesis, so this example is a separation, not a
general no-go theorem for all wreaths.

## 6. Audit of cell-mixing rigidity

For two partitions, each vertex lies in a unique cell on either side.  An
exact selection of whole cells imposes `x_C+y_D=1` whenever `C intersect D`
is nonempty.  Propagation along the bipartite overlap graph forces every
connected component to take all cells from one side.  Thus independent
per-source choices are invalid.

Rank-vector sectors are a legitimate exception because they are disjoint
before any cell choice is made.  Three or more overlapping systems produce
a higher exact-cover problem not solved by pairwise face incidence.

## 7. Machine audit

`scratch/check_quartet_integral_face_resolver.py` verifies:

* every possible frame function through `m=4`--including all `59,049`
  functions at `m=4`;
* random frame functions through `m=7`;
* both lower and upper coverage at every depth; and
* the exact local face/window counting formula through dimension 20.

All checks pass.  The computation validates the finite face theorem and its
boundary cases; it does not simulate or certify a deep-shadow cycle factor.

