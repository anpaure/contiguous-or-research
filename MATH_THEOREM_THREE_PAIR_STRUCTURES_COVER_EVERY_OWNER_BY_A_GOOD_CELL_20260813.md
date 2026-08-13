# Three pair structures cover every owner by a good long-run cell

**Date:** 2026-08-13  
**Status:** unconditional probabilistic owner-cover theorem.  In the odd middle layer,
three suitably chosen sentinel-plus-pair structures make every owner good in at least
one structure whenever the explicit inequality below holds; in particular this is
eventual for `q=Theta(sqrt R)`.  This is a cover by overlapping cell partitions, not a
partition into good cells and not yet a resident owner factor.

## 1. Pair structures and their bad fraction

Put

\[
 k=2R-1,\qquad p=R-1,\qquad W=\binom{2p+1}{p+1},
 \qquad M=q+\lceil3\log _2p\rceil.                       \tag{1.1}
\]

A pair structure consists of a distinguished sentinel and a perfect matching of the
other `2p` coordinates.  It partitions the owner layer into the pair cells of
`MATH_THEOREM_PAIR_CELL_LONG_RUN_Q_WINDOW_CLOCK_EXPLICIT_LEAVE_AND_EXACT_SPLICE_CAP_20260813.md`.
Call an owner good for that structure when its singleton-pair count is at least `M`.

For every fixed structure the number of bad owners is

\[
 L_{p,q}=\sum_{\epsilon=0}^1
         \sum_{\substack{m<M\\a,b\in\mathbb Z_{\ge0}}}
         {p!2^m\over m!a!b!},                            \tag{1.2}
\]

where `a=(R-epsilon-m)/2` and `b=p-m-a`.  If `M<=p/2`, then

\[
 \delta_{p,q}:={L_{p,q}\over W}
 \le (2p+2)2^{-p}\left({ep\over M}\right)^M.            \tag{1.3}
\]

## 2. Exact multi-structure cover

### Theorem 2.1

For every integer `t>=1`, if

\[
                         W\,\delta_{p,q}^{,t}<1,         \tag{2.1}
\]

then there exist `t` pair structures such that every rank-`R` owner is good in at
least one of them.

#### Proof

Choose the `t` structures independently and uniformly from the orbit of one pair
structure under `Sym([k])`.  This action is transitive on the owner layer.  Since every
structure has exactly `L_{p,q}` bad owners, a fixed owner is bad with probability
`delta_{p,q}`.  It is bad for all `t` independent structures with probability
`delta_{p,q}^t`.  The union bound over the `W` owners gives probability at most the
left side of (2.1) that some owner is uncovered.  If it is below one, a covering tuple
exists.  \(\square\)

### Corollary 2.2 (three structures)

Assume `M<=p/2` and

\[
 3M\log _2\!\left({ep\over M}\right)
  +3\log _2(2p+2)+2<p.                                  \tag{2.2}
\]

Then three pair structures cover every owner by a good cell.

#### Proof

Use `W<=2^(2p+1)` and (1.3):

\[
 W\delta_{p,q}^{,3}
 \le 2^{,1-p}(2p+2)^3\left({ep\over M}\right)^{3M}<1. \tag{2.3}
\]

The final inequality is implied by (2.2), with one bit of slack.  Apply Theorem 2.1.
\(\square\)

If `q=Theta(sqrt p)`, then `M=Theta(sqrt p)` and the left side of (2.2) is
`O(sqrt p log p)=o(p)`.  Hence the three-structure conclusion holds eventually in the
OR-word deadline regime.

## 3. Why this does not yet give a factor

For each of the three structures, its cells partition **all** owners, and every good
cell supports a `q`-biresident Hamilton cycle.  The theorem says that the union of the
three good-cell families covers the owner layer.  It does not select a disjoint
subfamily covering each owner once.

The naive first-good assignment generally fragments cells from the later structures;
their Hamilton cycles then cease to be available.  Equivalently, the next exact owner
gate is one of the following:

* a perfect matching in the nonuniform hypergraph whose edges are good pair cells;
* a cycle-factor selector in the union of the three good-cell Gray graphs; or
* an alternating cross-structure trade that absorbs the fragmented residual cells.

Any such selector must also retain the `q`-edge transition-collar condition.  Thus the
theorem closes the set-theoretic owner support problem with a constant number of
structures, while deliberately leaving the integral factor/chronology problem open.
