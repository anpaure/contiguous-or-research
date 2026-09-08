# Independent audit of `LEX_FOUR_LAYER_FACTOR.md`

## Verdict

The main four-layer theorem and its fixed-dimensional extension are
correct, but Section 2 contains a false local identity.  In particular,
(2.3) and the assertion that the two canonical half-edge labels are always
distinct are not true when both of the first two positive coordinates of
the upper target equal one.

This does **not** invalidate the theorem.  In four dimensions the exceptional
targets are charged to degree-three junctions already present in (4.4), so
the displayed `O(m^2)` repair bound remains valid without changing its
order, or even the coefficient in (4.4).  In fixed dimension every such
junction belongs to the boundary set (5.1), so the
`O_t(m^(t-2))` conclusion also remains valid.

The source should nevertheless replace the proof in Sections 2 and 4 by
the corrected case analysis below.  The schematic arrow display (6.1) is
also mislabeled: the four witness lengths are respectively one, two, three,
and four for ranks `r-2,r-1,r,r+1`.

## 1. Correct canonical-label calculation

Let `i<j` be the first two positive coordinates of
`y in L_(r+1)`, let

\[
 z_i=y-e_i,\qquad z_j=y-e_j,\qquad v=y-e_i-e_j,
\]

and, when needed, let `k` be the third positive coordinate of `y`.
The selected edges below `z_i` and `z_j` do meet at `v`, and
`z_i vee z_j=y`.  The half-edge labels at `v`, however, are as follows:

\[
\begin{array}{c|c|c}
 &\lambda_v(e_{z_i})&\lambda_v(e_{z_j})\\ \hline
 y_i\ge2,\ y_j\ge2&i&j\\
 y_i=1,\ y_j\ge2&k&j\\
 y_i\ge2,\ y_j=1&i&k\\
 y_i=y_j=1&k&k.
\end{array}
\]

For example, in the first row

\[
 b_{z_i}=v-e_i,\qquad b_{z_j}=v-e_j,
\]

not the two formulas printed in (2.3).  If `y_i=1`, deleting coordinate
`i` makes `j,k` the first two positive coordinates of `z_i`, and hence
`b_(z_i)=v-e_k`; the other cases follow identically.

There is always a third positive coordinate when one of `y_i,y_j` is one:
otherwise `|y|<=m+1`, whereas the fixed-dimensional hypothesis gives
`|y|=r+1>m+1`.

Thus the labels are distinct except in the last row.

## 2. Why the exceptional row is already a surface defect

In the four-box central case, `|y|=2m+1`.  If `y_i=y_j=1`, the two
remaining positive coordinates must sum to `2m-1`; their values are
therefore `m,m-1` in one order or the other.  Moreover `i,j` must be
coordinates 1 and 2, because fewer than two later coordinates cannot carry
the remaining sum.  Hence the only two such targets are

\[
 (1,1,m,m-1),\qquad (1,1,m-1,m).
\]

Their junctions are `(0,0,m,m-1)` and `(0,0,m-1,m)`.  Both have degree
three in the selected-cover graph.  More generally, if the labels of a
canonical pair are distinct and its junction has degree two, the
distinct-label transition rule is forced to pair them.  Therefore every
class-A failure still occurs at a degree-three vertex.

For reference, the exact degree-three count in (4.3) is correct.  The
degree formula for a vertex whose first two positive coordinates are
`p<q` is

\[
 \deg(v)=q-2+1_{v_p<m}+1_{v_q<m}.
\]

For `q=3`, summing the two possible values of `p` gives
`m^2+m-4` degree-three vertices; for `q=4` there are six.  Their total is

\[
 m^2+m+2=m(m+1)+2.
\]

A fixed junction has at most `binom(4,2)=6` canonical upper targets.
Consequently the original bound

\[
 6\bigl(m(m+1)+2\bigr)
\]

for class A remains valid, including the two equal-label targets.  What is
false is only the source's stated reason that every canonical pair has
distinct labels.

For fixed `t`, equality of the two labels again forces
`y_i=y_j=1`.  After subtracting those coordinates, all positions before
the third positive coordinate vanish.  In particular `v_1=0` or `v_2=0`,
so `v` lies in the boundary family

\[
 B=\{v:v_1\in\{0,m\}\text{ or }v_2\in\{0,m\}\}.
\]

There are `O_t(m^(t-2))` rank-slice vertices in `B`, and each is the
canonical junction of at most `binom(t,2)` upper targets.  This repairs the
general argument as well.

## 3. Four-window recovery and boundary charging

Once the two canonical edges are actually paired at `v`, the proof in
Section 3 is correct.  If they are consecutive trail edges `e_k,e_(k+1)`
and neither is a trail-boundary edge, the distinct-label factor identity at
their other endpoints gives

\[
 b_{e_{k-1}}\vee b_{e_k}\vee b_{e_{k+1}}=z_i,
 \qquad
 b_{e_k}\vee b_{e_{k+1}}\vee b_{e_{k+2}}=z_j.
\]

Their four-term join is therefore `z_i vee z_j=y`.  Trail orientation does
not enter this calculation.

The class-B charge is also correct.  A fixed central edge colour `z` can be
a canonical edge only for a target `z+e_h`, so it receives at most four
charges.  If `D` is the set of first and last trail edges, then
`|D|<=2T` and class B has size at most `4|D|<=8T`.

The transition-trail count remains surface order.  Off `B`, every vertex
has exactly the two incident edges obtained from `v+e_1,v+e_2`, with
labels 2 and 1, so they are paired.  Unpaired half-edges are supported on
`O(m^2)` boundary vertices.  A transition cycle meeting the boundary is
charged to one boundary transition, and a cycle avoiding it is a component
of one of at most `(m+1)^2` transverse lines.  Thus `T=O(m^2)`.

Together with the already audited three-layer repairs, these charges prove

\[
 |L_{2m}|+O(m^2)=M_m+O(m^2)
\]

for all four layers.  Appending literal repairs preserves all internal
witnesses and all appended entries are nonzero for `m>=2`.

## 4. Fixed-dimensional extension

The same corrected proof is uniform for fixed `t`.  Off the four boundary
slices in (5.1), the selected graph is a degree-two coordinate-`{1,2}`
line with distinct labels 2 and 1.  The number of boundary vertices,
transverse components, unpaired half-edges, and cycle cuts is
`O_t(m^(t-2))`.

The singleton image is exactly

\[
 \{b_z:z\in L_r^{(t)}\}
 =\{x\in L_{r-2}^{(t)}:x_1<m,\ x_2<m\}.
\]

Indeed the reverse map is `z=x+e_1+e_2`.  Its omitted boundary has
`O_t(m^(t-2))` points.  The unpaired rank-`r-1` vertices, boundary middle
edges, and the upper failures just audited have the same order.  Hence the
length `|L_r^(t)|+O_t(m^(t-2))` is valid.

The nonzero hypothesis needs the contextual assumption `m>=2`: then
`r>m` implies `r-2>=1`, so every edge-minimum entry is nonzero.  If the
extension were read independently with `m=1,r=2`, zero edge minima could
occur and would need separate treatment.

## 5. Independent finite checks

I ran the supplied verifier through `m=30`; it passed exhaustive coverage
and the stated repair charge in every case.  I separately enumerated the
canonical labels through `m=24`.  There are exactly two equal-label upper
targets for every `m`, and both junctions have degree three, exactly as the
repair above requires.

I also implemented an independent generic construction for every sampled
rank `r>m` in dimensions `t=3,4,5,6` (all `m=2,...,5` where feasible).
It rebuilt the selected edges, chose distinct-label transitions, cut every
cycle, enumerated all windows of length at most four within each trail, and
counted literal repairs.  It covered all four designated layers after
repairs; both trail counts and missing-target counts stayed bounded by a
dimension-dependent constant times `m^(t-2)`.

One limitation of the supplied checker is worth noting: after computing
the set of missing targets it appends every one literally, so final
coverage itself is automatic.  Its substantive checks are the trail
identities, exact degree-three count, boundary-edge count, and the
quadratic upper-repair charge.  Those checks passed, and the independent
case analysis above supplies the all-`m` proof that the checker alone
cannot provide.

