# Adversarial audit of the nonlocal-pivot BK partition

## 1. Verdict

The construction in `NONLOCAL_PIVOT_BK_PARTITION.md` is valid, subject to
the scope stated there.

Accepted claims:

* the proposed cells are literal disjoint subcubes and exhaust each critical
  orientation cube;
* the final direction has one fixed nonlocal carrier support throughout a
  cell;
* all retained supports are pairwise disjoint, including across critical
  levels;
* every nonempty critical sequence contributes exactly one retained
  nonlocal direction;
* its exact mean codimension is `2-2^(2-a)<2`;
* all but `o(W)` middle vertices lie in cells of dimension at least
  `m/8-m^(5/6)`.

Rejected inference:

* none of these facts establishes lower- or upper-shadow coverage, a
  shift-compatible SCD, or `nu(2m)=W+o(W)`.

## 2. Partition audit

The definition deliberately ignores `x_a` and records the last `1` among
`x_1,...,x_(a-1)`.  Every binary word has exactly one such record: either
`b=0`, or a unique `b in {1,...,a-1}`.  Once `b` is fixed, the conditions

\[
 x_b=1,\qquad x_{b+1}=\cdots=x_{a-1}=0
\]

do not constrain the prefix or `x_a`.  Therefore the proposed sets are
subcubes, not merely unions of subcubes.

Their sizes are

\[
 |P_0|=2,\qquad |P_b|=2^b\quad(1\le b<a),
\]

and

\[
 2+\sum_{b=1}^{a-1}2^b=2^a.
\]

This provides an independent cardinality check of exhaustion after
disjointness.  The edge case `a=1` is important: there is just one cell, the
entire one-cube, and no bit is fixed.

## 3. Carrier audit

There are two potential state-dependence failures.

### 3.1 Earlier free directions

For `r<b`, toggling the final bit could have removed the only later `DU` and
made `p_r` nonlocal.  It does not, because `x_b=1` is fixed and lies later
than every such `r`.  Thus the native-support branch of the exact carrier
formula remains true on the entire cell.

When `b=0`, there are no earlier free directions, so this argument is not
silently being applied without a barrier.

### 3.2 The final free direction

The final generator never has a later `DU`.  Its support is determined by
the most recent earlier carrier overwrite.  For `b>0`, that overwrite is
exactly the fixed block `b`: the bits after `b` and before `a` are fixed
zero, while changes in the free prefix occur earlier.  Its carrier is
therefore always `p_b+1`.

For `b=0`, every earlier bit is fixed zero, so the carrier is always the
initial stack entry `e_0`.  Toggling the final generator changes which of
the two endpoints is persistent, but the undirected Johnson support remains
the same pair.  Hence the final edge really is a cube direction rather than
only a support observed at one endpoint.

## 4. Collision audit

All possible collisions reduce to the following list.

1. Two retained native directions use distinct odd blocks, hence disjoint
   native pairs.
2. A carrier `p_b+1` is the even coordinate of a fixed barrier block.  The
   generator at that block is not retained.
3. An initial carrier `e_0` is the even coordinate of an inactive `UU`
   block, so it is not part of a retained native pair.
4. The odd endpoint `p_a` belongs to the final block and cannot be another
   generator's odd endpoint.
5. Carriers at different critical levels occupy different stack depths.
   One physical `U` coordinate cannot simultaneously occupy two persistent
   stack slots, so those even endpoints are distinct.
6. Odd endpoints cannot equal carrier endpoints by parity.

This list covers native--native, native--nonlocal, and
nonlocal--nonlocal intersections.  It also explains why it would have been
incorrect merely to cite commutativity of the tableau moves: commuting
abstract moves can have twisted physical supports, and fixed disjoint
supports need a separate proof.

## 5. Exact retained-direction count

In a sequence of length `a>=1`, the only free direction with no fixed later
`1` is the final direction `p_a`.  It is nonlocal and is retained in every
cell.  Every other free direction lies before the fixed pivot and is native.
Thus the number of retained nonlocal directions is **exactly one**, not
merely at most one, per nonempty critical sequence.

For a full product cell this number is the orbit invariant

\[
 c=\#\{\text{nonempty critical levels}\}
   \le\lfloor d/2\rfloor.
\]

It does not depend on which pivot cells contain the vertex.  Empty critical
levels contribute neither a direction nor a defect.

## 6. Probability and codimension audit

Under uniform orientations, the number of strings in `P_b` gives

\[
 \Pr(P_0)=2^{1-a},\qquad \Pr(P_b)=2^{b-a}.
\]

The exact mean is therefore

\[
 (a-1)2^{1-a}+\sum_{b=1}^{a-1}(a-b)2^{b-a}
 =2-2^{2-a}.
\]

Checks at the smallest lengths are:

\[
\begin{array}{c|ccc}
a&1&2&3\\ \hline
\mathbb E\Delta_a&0&1&3/2.
\end{array}
\]

The orbit measure weights a cell by its number of vertices.  This is exactly
the distribution above.  Averaging cells without size weights would be the
wrong measure and is not used.

Summing over at most `floor(d/2)` critical levels gives expectation less
than `d`.  Markov is then applied separately in each orbit and summed with
orbit-size weights.  This proves a statement about the number of middle
**vertices**, not about the number of large cells.

## 7. Tail audit

The large-cell conclusion imports two previously audited estimates from
`BK_SUPPORT_FORMULA.md`:

* small-active orbits contain only `o(W)` vertices;
* radius greater than `ceil(m^(2/3))` contains only `o(W)` vertices.

On the complement,

\[
 \Pr(\Delta>m^{5/6})\le
 {m^{2/3}+1\over m^{5/6}}=O(m^{-1/6}).
\]

Thus the additional exception is also `o(W)`.  The argument does not claim
that a uniformly chosen *cell* is large, which would require a different
unweighted orbit calculation.

## 8. Independent machine audit

`scratch/verify_nonlocal_pivot_bk_partition.py` does not use the support
formula to generate predicted edge supports.  It:

1. enumerates every balanced word;
2. computes its recording path by ordinary binary RSK;
3. obtains each physical support by comparing the two actual inverse words;
4. canonicalizes odd-BK orbits and their pivot cells;
5. enumerates every vertex and every retained-direction edge once per cell;
6. verifies that cells are disjoint and cover all tableaux;
7. verifies fixed supports and global pairwise disjointness;
8. separately checks the explicit carrier `p_b+1` or the initial carrier;
9. checks exactly one nonlocal direction per critical sequence;
10. checks the exact rational mean-codimension identity orbit by orbit.

The exhaustive run through `m=9` reports:

```
m=1 tableaux=2     cells=2    cell_edges=0      carriers=0:    PASS
m=2 tableaux=6     cells=5    cell_edges=2      carriers=0:    PASS
m=3 tableaux=20    cells=13   cell_edges=16     carriers=1:    PASS
m=4 tableaux=70    cells=36   cell_edges=86     carriers=5:    PASS
m=5 tableaux=252   cells=101  cell_edges=420    carriers=21:   PASS
m=6 tableaux=924   cells=289  cell_edges=1948   carriers=78:   PASS
m=7 tableaux=3432  cells=834  cell_edges=8764   carriers=276:  PASS
m=8 tableaux=12870 cells=2427 cell_edges=38638  carriers=943:  PASS
m=9 tableaux=48620 cells=7101 cell_edges=167908 carriers=3155: PASS
```

The finite audit supports every local and partition assertion but is not a
substitute for the general carrier proof.

## 9. Residual mathematical boundary

The new partition changes the support catalog in a real but quantitatively
limited way: a cell gains only `c<=d/2` nonlocal pairs.  It has not been
shown that these pairs distribute target shadow types evenly, that cube
cycle factors can be coordinated across cells, or that their total defect
is `o(W)` through a growing depth.  Any such inference would require a new
typed matching or shift-compatibility theorem.

The accepted conclusion is therefore a stronger exact middle-layer cube
partition, not a solution of the universal-OR problem.
