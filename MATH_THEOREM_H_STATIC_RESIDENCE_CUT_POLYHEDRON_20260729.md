# Static residence cuts for spanning Johnson two-factors

Date: 2026-07-29  
Lane: H  
Status: proved for integral spanning two-factors; exact polynomial separation
proved.  This is an exact integer formulation, not a claim that the displayed
linear relaxation is the convex hull.

## 0. Verdict

For the bordered-run convention used by the current full-`J(16,8)` audit,
residence at least four has a seed-independent static characterization.  Fix
a coordinate shore.  For every connected shore set `S` of one, two, or three
vertices, require

\[
  \text{selected coordinate-crossing edges incident with }S
  \ \le\ 
  \text{selected same-shore edges leaving }S.                 \tag{R}
\]

On the degree-two face this is equivalently

\[
 x(E_H(S))+x(E(S,Z))\le |S|.                                  \tag{R'}
\]

These rows are necessary and sufficient for the absence of bordered runs of
length one, two, or three.  On the exact degree-two face, their equivalent
form (R') fractionally dominates every seed-specific bordered-path no-good
currently used by the motif CEGAR.  Thus they can replace seed-generated
motifs by a global lazy separator in the two-factor model.  Eager expansion
is not attractive: there are `136,559,280` positive-shore rows at `k=16`,
and twice that number if both coordinate statuses are constrained.

The natural degree/q1/residence matrix is not totally unimodular.  Degree-only
selection retains the usual nonbipartite `f`-factor/blossom structure, and the
q1 submatrix alone has a bipartite-incidence structure, but the combined
system has neither a natural TU description nor a direct edge-matroid basis
description.  No claim is made that every possible extended matroid-parity
gadget is impossible.

There is one genuine convention mismatch in the current tree.  The full-
Johnson audit skips coordinate-constant factor cycles, whereas
`scratch/k16_even_necklace_q1_factor_20260729.py` counts a constant all-one
cycle as one finite cyclic run.  The theorem below gives exact rows for both
conventions.

## 1. Notation and the operative convention

Let

\[
 G=J(16,8),\qquad V(G)=\binom{[16]}8,
\]

and let `x` be a binary edge vector satisfying

\[
 \sum_{e\ni v}x_e=2\qquad(v\in V(G)).                          \tag{1.1}
\]

Thus `F_x` is a spanning two-factor, not necessarily connected.  Fix a
coordinate `a` and a status `sigma` in `{0,1}`, and put

\[
 U=U_{a,\sigma}:=\{X:{\bf1}_{a\in X}=\sigma\},\qquad
 Z=V(G)\setminus U,\qquad H=G[U].                              \tag{1.2}
\]

For `S subseteq U`, write:

* `E_H(S)` for shore edges having both ends in `S`;
* `delta_H(S)` for shore edges with exactly one end in `S`;
* `C_a(S)=E_G(S,Z)` for coordinate-crossing edges from `S` to the
  opposite shore.

The **bordered-run convention** regards the path components of `F_x[U]` as
the bounded `sigma`-runs.  A factor cycle contained wholly in `U` has no
entrance or exit and is therefore safe.  This is exactly the convention in
`scratch/audit_k16_full_johnson_biresident_q1_nogo_20260729.py` and
`scratch/solve_k16_pbbs_fixed_segments_q1_residence_20260729.py`, both of
which explicitly skip all-present and all-absent factor cycles.

Positive residence uses only `sigma=1`.  Zero-residence uses only `sigma=0`.
Bi-residence imposes both families.

## 2. Exact static characterization

### Theorem 2.1 (bordered residence-cut theorem)

Let `x` be a binary solution of (1.1).  For fixed `a,sigma`, the following
are equivalent.

1. Every bounded `sigma`-run of `F_x` has at least four vertices.
2. For every nonempty `H`-connected set `S subseteq U` with `|S|<=3`,

   \[
      x(C_a(S))\le x(\delta_H(S)).                             \tag{2.1}
   \]

3. For every such `S`,

   \[
      x(E_H(S))+x(C_a(S))\le |S|.                              \tag{2.2}
   \]

Disconnected sets need not be included.

#### Proof

First, summing (1.1) over `S` gives

\[
 2|S|=2x(E_H(S))+x(\delta_H(S))+x(C_a(S)).                     \tag{2.3}
\]

Consequently (2.1) and (2.2) are equivalent on the degree-two face.

Decompose `F_x[U]` into path components and cycle components.  A path
component `P` is exactly one bounded `sigma`-run.  Let `A subseteq V(P)`.
View `A` as a union of intervals along the path.  If `A` is a proper subset
of `P`, every interval containing a path endpoint contributes one selected
edge from that endpoint to `Z` and one selected path edge from `A` to
`P\A`; every internal interval contributes zero of the former and two of the
latter.  Hence

\[
 x(C_a(A)\cap E(F_x))\le
 x(\delta_P(A))\qquad(A\subsetneq V(P)).                       \tag{2.4}
\]

For `A=V(P)`, the two quantities are respectively `2` and `0`.  For a cycle
component of `F_x[U]`, there are no selected edges to `Z`, so its contribution
to the left side minus the right side of (2.1) is nonpositive for every
choice of `A`.

Suppose now that every bounded run has size at least four and `|S|<=3`.
Then `S` cannot contain an entire path component.  Applying (2.4) to the
intersection of `S` with each component of `F_x[U]` and summing proves
(2.1).

Conversely, let `P` be a bounded run with `1<=|P|<=3`, and take
`S=V(P)`.  The selected path makes `S` connected in `H`.  Its two ends use
one coordinate-crossing edge each, while no selected same-shore edge leaves
`S`.  Thus

\[
 x(C_a(S))=2>0=x(\delta_H(S)),
\]

contradicting (2.1).  This proves the equivalence.

Finally, if `S` is disconnected in `H`, both sides of (2.1) add over the
`H`-components of `S`.  A disconnected violation therefore contains a
connected violating component.  QED.

### Sharpness of the support sizes

All three sizes are necessary.  A bordered run with exactly `j` vertices
violates its size-`j` row, while every proper subset of that run satisfies
(2.1).  Thus singleton, edge, and connected-triple rows respectively detect
runs of lengths one, two, and three.

### Corollary 2.2 (the stricter literal-cyclic convention)

Suppose instead that a factor cycle contained wholly in `U` is counted as
one finite cyclic run.  Then residence at least four is equivalent to

\[
 x(\delta_H(S))\ge1                                           \tag{2.5}
\]

for every nonempty `H`-connected `S` with `|S|<=3`.

Indeed, a bordered short run and a constant short factor cycle both give a
set `S` with zero selected shore boundary.  Conversely, if the boundary of
such an `S` is zero, `F_x[U]` has a path or cycle component contained in
`S`, hence a run of size at most three.  Since `G` is simple, a constant
factor cycle of length below four can only be a triangle.  Therefore (2.1)
and (2.5) differ precisely on constant-coordinate factor triangles.

On (1.1), (2.5) can also be written

\[
 2x(E_H(S))+x(C_a(S))\le2|S|-1.                               \tag{2.6}
\]

## 3. Exact fractional separation

The separator works for an arbitrary fractional vector `x`; it separates
the original form (2.1), so it does not need to assume (1.1) numerically.
For each `v in U`, precompute

\[
 c(v)=x(E_G(\{v\},Z)),\qquad
 h(v)=x(\delta_H(\{v\})),\qquad p(v)=c(v)-h(v).                \tag{3.1}
\]

For every `S subseteq U`,

\[
 \begin{split}
 D(S)&:=x(C_a(S))-x(\delta_H(S))\\
 &=\sum_{v\in S}p(v)+2x(E_H(S)).                              \tag{3.2}
 \end{split}
\]

Hence `S` violates (2.1) exactly when `D(S)>0`.  It is enough to test:

\[
\begin{array}{ll}
\{v\}:      &p(v),\\
\{u,v\}:    &p(u)+p(v)+2x_{uv},\quad uv\in E(H),\\
\{u,v,w\}:  &p(u)+p(v)+p(w)+
               2(x_{uv}+x_{uw}+x_{vw}),
\end{array}                                                     \tag{3.3}
\]

where the last line ranges over connected triples.  Enumerating unordered
pairs of neighbors about every possible center visits every connected
triple; a triangle is evaluated using all three of its internal edges.
Deduplication is optional for correctness.

The time for one shore is

\[
 O\!\left(|E(H)|+\sum_{v\in U}\deg_H(v)^2\right),             \tag{3.4}
\]

with `O(|U|+|E(H)|)` stored data.  Thus the separator is polynomial and,
because the support bound is the fixed constant three, elementary.  At an
integral incumbent one may instead traverse the factor cycles and scan all
coordinate bit runs in `O(16|V(G)|)` time, emitting (2.1) for each bad run.

The same enumeration separates the strict rows (2.5) by evaluating
`x(delta_H(S))`.

## 4. Exact `J(16,8)` row census

Each coordinate shore induces

\[
 H\cong J(15,7)\cong J(15,8),
\]

so

\[
 |V(H)|=\binom{15}{7}=6435,\qquad
 \Delta(H)=7\cdot8=56,\qquad
 |E(H)|=180180.                                                \tag{4.1}
\]

The number of Johnson triangles is

\[
 T=\binom{15}{6}\binom93+\binom{15}{8}\binom83
  =780780.                                                     \tag{4.2}
\]

There are `|V(H)| binom(56,2)` centered wedges.  A nontriangle connected
triple is counted once and a triangle three times, so the number of distinct
connected triples is

\[
 6435\binom{56}{2}-2T=8,348,340.                              \tag{4.3}
\]

Thus one shore has

\[
 6435+180180+8,348,340=8,534,955                              \tag{4.4}
\]

rows.  All sixteen positive shores have `136,559,280`; imposing both signs
has `273,118,560`.  This is a static polynomial-size family for fixed run
threshold, but it should be separated lazily rather than instantiated.

## 5. Dominance over seed-specific motif rows

Let

\[
 P=(v_0v_1,v_1v_2,\ldots,v_\ell v_{\ell+1}),\qquad1\le\ell\le3,
\]

be a seed-generated bordered path, with the coordinate absent at `v_0` and
`v_(ell+1)` and present at the interior set
`S={v_1,...,v_ell}`.  Every edge of `P` belongs to
`E_H(S) union C_a(S)`.  Therefore (2.2) implies

\[
 x(P)\le |S|=|P|-1,                                           \tag{5.1}
\]

which is exactly the existing universal bordered-path no-good.  On the
degree-two face, the aggregate row (2.2) is seed-independent and
fractionally dominates (5.1).  This dominance statement is not asserted
outside the degree-two face, where (2.1) and (2.2) are not equivalent.

This also explains why an ordinary subtour cut is blind.  A bad run has
`x(delta_G(S))=2`, satisfying the standard subtour boundary row at equality,
but its typed boundaries are

\[
 \bigl(x(C_a(S)),x(\delta_H(S))\bigr)=(2,0).                   \tag{5.2}
\]

Residence is a coordinate-coloured small-component balance condition, not a
connectivity condition.

Consequently the exact replacement for seed-specific motif CEGAR is:

1. retain degree and q1 rows;
2. solve over the full edge catalogue;
3. separate (2.1) over all coordinates, adding any violated rows;
4. repeat until no violation remains;
5. replay the integral factor and its literal bit runs.

No seed chronology is needed to generate a valid residence row.

## 6. TU and matching-structure audit

### Proposition 6.1 (the natural matrix is not TU)

The coefficient matrix containing the residence rows is not totally
unimodular, even before q1 rows are added.

#### Proof

A shore `H=J(15,7)` contains a triangle `v_1v_2v_3`.  Restrict the three
singleton rows

\[
 x(C_a(\{v_i\}))-x(\delta_H(\{v_i\}))\le0
\]

to the three triangle-edge columns.  Up to multiplying rows by `-1` and
permuting columns, the minor is

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},                                                \tag{6.1}
\]

whose determinant is `-2`.  Hence the matrix is not TU.  Independently, the
three degree rows restricted to any Johnson triangle give the same minor, so
adding or deleting q1 rows cannot restore TU.  QED.

The q1 rows by themselves have a useful remnant: each Johnson edge has one
rank-seven intersection colour and one rank-nine union colour.  After
signing one colour shore, their coefficient matrix is the node-edge
incidence matrix of a bipartite colour multigraph and is TU.  This property
does not survive adjoining the middle-vertex degree rows, as (6.1) shows.

Degree-only spanning two-factor selection is a nonbipartite `f`-factor
problem and is polynomial by matching/blossom methods.  It is not made TU by
that algorithmic fact.

There is also no direct single-matroid basis description on the Johnson-edge
ground set for a nontrivial family of spanning two-factors.  If `F_1` and
`F_2` are distinct such factors and `e=uv in F_1\F_2`, deleting `e` lowers
the degrees of `u,v`; adding one different simple edge cannot restore degree
two at both vertices.  Thus the basis-exchange axiom fails between `F_1`
and `F_2`.

Likewise, q1 coverage and the no-short-run property are not hereditary under
edge deletion, so they are not themselves matroid independence systems on
this ground set.  These observations rule out the natural TU and direct
edge-matroid routes.  They do **not** rule out a larger auxiliary-graph or
matroid-parity encoding; no such encoding is presently proved or disproved.

## 7. Precise implementation boundary

The theorem supplies an exact static/lazy residence layer for the
full-Johnson feasibility model.  It does not prove feasibility or
infeasibility after degree and q1 rows are added, and it does not make the
relaxation integral.  Its concrete gain is that residence no longer depends
on the short motifs of one incumbent or seed factor.

Before using the word **cyclic** in a final certificate, the project should
choose one of the two constant-cycle conventions.  For the model currently
described by the full-Johnson audit, (2.1) is the exact row.  If the literal
`cyclic_runs` checker is authoritative, use (2.5) instead.
