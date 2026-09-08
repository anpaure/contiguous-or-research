# Blue-section provenance for the MW--MSW Catalan braid

## 1. Outcome

The path-dependent peak-insertion coordinates of the canonical MSW factor
do **not** create a topological proliferation.  After the MW--MSW braid is
cut at its three common edges per root, every blue section admits one of
only linearly many fixed deletion charts, and the complete collection has
only Catalan-many charted row sections.  Hence all windows meeting chart
boundaries lie in an `O(H Cat_n)` halo.

There is, however, a genuine targetwise collision which a halo count does
not see.  If `delta_i` deletes the adjacent coordinate pair `i,i+1` from a
binary target word, then

\[
 \boxed{\delta_i(u)=\delta_j(u)
 \iff u_i u_{i+1}\cdots u_{j+1}\text{ has period }2}
 \qquad(i<j).                                      \tag{1.1}
\]

Consequently the distinct one-tag parents of a target are indexed by its
maximal alternating blocks, not by all of its transition positions.  The
zero-tag and two-tag collision classes are, respectively, zero-runs and
one-runs.  This is the exact chart-holonomy/collision law.

Thus the fixed-coordinate provenance problem splits cleanly:

* **occurrence provenance is solved** at Catalan section cost;
* **target provenance remains a capacitated deletion problem**, but its
  true distinct-neighbour statistic is now explicit.

The theorem does not repair the positive-density first-shadow defect of the
unchanged canonical MSW factor.

## 2. The deletion-chart atlas

Let a parent Dyck word have length `N=2m`, and number its word gaps by
`g=0,...,N`.  Inserting a peak at gap `g` gives a child word of length
`N+2`.  Its two new coordinates occupy physical positions

\[
                         P_g=\{g+1,g+2\}.             \tag{2.1}
\]

Let

\[
 \iota_g:[N]\longrightarrow[N+2]\setminus P_g,
 \qquad
 \iota_g(t)=
 \begin{cases}
 t,&t\le g,\\
 t+2,&t>g,
 \end{cases}                                        \tag{2.2}
\]

and let `delta_g` be deletion of the two physical positions in `P_g`,
followed by the inverse order-preserving relabelling.

The peak-insertion theorem gives, for every child root `c=I_g(w)`,

\[
 \rho(c)=\iota_g(\rho(w))
 \quad\hbox{with the two labels in }P_g
 \hbox{ inserted as one adjacent block}.             \tag{2.3}
\]

Hence the entire child path uses the single fixed chart `(g,delta_g)`.
Although `g` varies between roots, there are only `N+1` chart types.

For the canonical ECO parent map one restricts to final-descent gaps, but
this only removes charts and does not change the conclusion.

### Theorem 1 (Catalan chart atlas)

In the dimension-`2n` MW--MSW comparison, cut each canonical MSW path at
its three common MW edges.  After passing from path order to tight-wreath
order and labelling every child root by its canonical ECO deletion chart,
the blue part is a union of at most

\[
                              6\operatorname{Cat}_n  \tag{2.4}
\]

charted cyclic-row intervals.  In the lift from semilength `n-1` to `n`,
these intervals use at most `2n-1` fixed coordinate charts.

For windows of at most `H+1` consecutive tight-row entries, at most

\[
                             12H\operatorname{Cat}_n \tag{2.5}

start positions meet a charted-section boundary.  Since
`Cat_n<4 Cat_(n-1)`, this is `O(H Cat_(n-1))` at one lift step.

### Proof

The three common edges have indices `0<a(w)<b(w)`.  Removing them leaves at
most three ordinary path intervals on every canonical root path.

Write the omitted-label cycle of a path as

\[
                         q_0,q_1,\ldots,q_{2n}.
\]

The path vertices occur in the ordinary cyclic index order, whereas the
tight-wreath order is the `+2` order on `Z_(2n+1)`.  Because `2n+1` is odd,
this order can be written

\[
              0,2,4,\ldots,2n,1,3,\ldots,2n-1.       \tag{2.6}
\]

The indicator of an ordinary cyclic interval changes value at exactly two
`+1` boundaries.  Along the `+2` order it can change only when one of those
two boundaries lies in one of the two unit steps being skipped.  It
therefore changes at most four times, and so has at most two cyclic runs.
Three blue path intervals consequently give at most six tight-row intervals
per root, proving (2.4).

Equation (2.3) assigns one deletion chart to the whole root path, hence to
each of those intervals.  A parent word of length `2n-2` has `2n-1` gaps,
which proves the chart-type assertion.

Finally, the union of `s` cyclic intervals has at most `2s` boundary
points, and a window of length at most `H+1` crosses a fixed boundary from
at most `H` starting positions.  Use `s<=6 Cat_n` to obtain (2.5).
\(\square\)

### Remark

The local two-tag positions need not be declared additional bad seams.
The exact projection table already handles windows containing zero, one,
or two tags, with the corresponding depth shift.  If one insists on a
single fixed tag-count inside each section, cutting at the two tag positions
only changes the constant in (2.4)--(2.5).

### Proposition 1.1 (the coordinate atlas is flat)

At the level of labelled coordinates, iterated peak-deletion charts have no
permutation holonomy.  A composite of elementary charts is the unique
order-preserving deletion of the union of the physical coordinate pairs
removed.  In particular, two deletion orders removing the same physical
coordinates induce the same map, and every closed coordinate-chart loop is
the identity.

### Proof

An elementary chart retains a linearly ordered subsequence and relabels its
`t`-th survivor by `t`.  Composing two such maps retains the intersection of
their survivor sets, in its inherited order.  Induction gives the first
claim.  A linearly ordered finite set has only one order-preserving
bijection to itself, proving the second.  \(\square\)

Different peak deletions of the same child may retain different physical
subsets.  They are therefore different arrows, not nontrivial monodromy of
one arrow.  Their agreement on a particular target is exactly the collision
problem in the next section.  The cyclic rotation appearing in the
step-two wreath projection changes only the choice of row origin; it does
not permute physical coordinate labels.

## 3. Exact collision of two deletion charts

Let `u=u_1...u_L` be any binary word.  For `1<=i<L`, let `delta_i(u)` be
the length-`L-2` word obtained by deleting positions `i,i+1`.

### Theorem 2 (period-two collision criterion)

For `1<=i<j<L`,

\[
 \delta_i(u)=\delta_j(u)
 \quad\Longleftrightarrow\quad
 u_t=u_{t+2}\quad(i\le t\le j-1).                    \tag{3.1}
\]

Equivalently, the factor `u_i...u_(j+1)` has period two.

### Proof

Both deleted words have the same prefix `u_1...u_(i-1)` and the same
suffix `u_(j+2)...u_L`.  Equality is therefore equivalent to equality of
their middle factors:

\[
                   u_{i+2}\cdots u_{j+1}
                   =u_i\cdots u_{j-1}.               \tag{3.2}
\]

Comparing corresponding coordinates in (3.2) gives exactly (3.1).  The
converse is the same argument reversed.  \(\square\)

### Corollary 3 (the exact one-tag neighbour count)

Put

\[
 d_t=u_t\mathbin{\mathsf{xor}}u_{t+1},
 \qquad1\le t<L.                                    \tag{3.3}
\]

The admissible one-tag charts are the positions with `d_t=1`.  Two such
charts have the same deleted parent exactly when they lie in the same run
of ones of `d`.  Therefore

\[
 \boxed{\#\{\delta_t(u):d_t=1\}
       =\#\{\text{runs of ones in }d\}.}             \tag{3.4}
\]

Equivalently, distinct one-tag parents are indexed by the maximal
alternating factors of `u` of length at least two.

For zero-tag charts (`u_tu_(t+1)=00`), equal deleted parents are precisely
the deletions lying in one maximal zero-run.  For two-tag charts they are
precisely the deletions lying in one maximal one-run.

### Proof

If `d_i=d_j=1`, the period-two condition in Theorem 2 is equivalent to
`d_i=d_(i+1)=...=d_j=1`.  This proves (3.4).  If both endpoint pairs are
`00`, period two forces the whole factor between them to be zero; the `11`
case is identical.  \(\square\)

## 4. Most targets still have linearly many distinct parents

The collision law corrects the raw transition count, but it does not create
a typical-degree obstruction.

### Corollary 4 (few distinct parents are exponentially rare)

Fix `eta<1/2`.  Among binary words of length `L=2m+O(1)`, the number having
at most `eta m` distinct one-tag parents is at most

\[
 2\sum_{s\le\eta m}{L\choose 2s}
   =2^{L H_2(\eta)+o(L)}=o(\operatorname{Cat}_m).     \tag{4.1}

Here `H_2` is binary entropy; changing `L` to `L-1` or `L+1` only changes
the lower-order term.

### Proof

The transition word `d` and the first bit of `u` determine `u`.  A binary
word of length `L-1` with exactly `s` runs of ones is specified by its `2s`
run endpoints, so there are `binom(L,2s)` possibilities.  Sum over `s` and
use the standard entropy bound.  Since `eta<1/2`, `H_2(eta)<1`, while
`Cat_m=2^{2m-o(m)}`.  \(\square\)

Thus a future capacitated-Hall argument may discard the few-low-neighbour
targets at sub-Catalan cost.  It must use the number of alternating blocks,
not the number of transitions.

## 5. What is and is not globalized

Theorems 1--2 settle the geometric part of the blue-section problem:

1. every blue row interval has a fixed coordinate-deletion chart;
2. there are only `O(Cat_m)` such intervals at one lift;
3. windows that cannot remain inside one charted interval cost only
   `O(H Cat_m)` occurrences;
4. all cross-chart identification is governed by the period-two law.

This removes a possible *holonomy of sections*: no recursive Euler pairing
is required just to keep the number of coordinate charts under control.
One simply cuts at chart changes and charges their halos.

It does **not** prove a defect recurrence.  A physical child target may be
the image of several parent targets under different charts, and the
period-two criterion describes exactly when those presentations collapse to
the same parent.  Moreover, the canonical ECO parent family uses only the
charts owned by its actual roots.  A targetwise recurrence still needs a
bounded-load assignment in this restricted deletion graph.

Finally, the unchanged canonical MSW factor already has a macroscopic
first-shadow defect in all computed dimensions.  The chart atlas cannot
change that intrinsic fact.  Its correct use is either

* inside a genuinely re-bundled antipodal factor whose first shadow has
  first been repaired; or
* as the occurrence-provenance half of a separate targetwise expansion
  theorem.
