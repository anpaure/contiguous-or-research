# Noncontiguous collar/residual rank matching polytope

**Date:** 2026-08-03  
**Status:** unconditional fractional joint-flag theorem.  No computation is
used.  The theorem deliberately abandons a contiguous adjacent-rank collar;
it does not produce an integral named-target matching or a literal Ferrers
chronology.

## 0. Result

Put

\[
 k=2r,\qquad W={2r\choose r},\qquad
 p_s={{2r\choose s}\over W}\quad(1\le s<r).
\tag{0.1}
\]

Let `d` be a positive integer and fix an integer collar width
`1<=a<=r-2`.  Split the ranks
into

\[
 J=\{1,\ldots,r-a-1\},\qquad
 C=\{r-a,\ldots,r-1\}.
\tag{0.2}
\]

Let `q=(q_1,...,q_(r-1))` satisfy

\[
 0\le q_s\le p_s,\qquad
 \sum_{s<r}q_s\le d,\qquad
 q_s+q_{s+1}\le1\quad(s,s+1\in J).
\tag{0.3}
\]

Then there is a probability distribution on rank sets `R subseteq [r-1]`
such that

\[
 |R|\le d,\qquad
 \Pr(s\in R)=q_s,
\tag{0.4}
\]

and no two selected residual ranks in `J` are adjacent.  Collar ranks may be
selected in an arbitrary, noncontiguous pattern.

For every rank-`r` owner `T`, choose `R` from this distribution and choose a
uniform ordering of `T`.  Mark the initial set of that ordering at every
rank in `R`.  This gives one compatible owner-plus-flag atom: all selected
collar and residual targets lie on the same inclusion chain and their total
number is at most `d`.  Its exact named-target degree is

\[
 d_x(S)={q_s\over p_s}\qquad(|S|=s),
\tag{0.5}
\]

while every owner has degree one.

If `a=(c+o(1))sqrt(r)` for fixed `c>sqrt(log 2)` and `q_s<=p_s`, then the
adjacent inequalities in (0.3) hold for all sufficiently large `r`.
Consequently the optimal triangular residual vector, whose total mass is at
most the optimal depth `d=d(2r)=O(sqrt(r))`, has a **single fractional
common-order realization** with no adjacent residual ranks.  More precisely,
fix any `b=b(r)` with `a+1<=b=o(r)` and retain the central residual band

\[
                  \mathcal I=\{r-b,\ldots,r-a-1\}.
\tag{0.6a}
\]

Over the owner vertices and supported positive-degree residual targets in
`mathcal I`, define `rho_2^residual` as maximum pair degree divided by the
smaller incident degree.  Then

\[
 \rho_2^{\rm residual}=O(r^{-2}),\qquad
 K^2\rho_2^{\rm residual}=O(r^{-1}),
\tag{0.6}
\]

where `K<=d+1=O(sqrt(r))` includes the owner vertex.  The general rank-set
decomposition above remains valid for arbitrary positive integer `d`; only
this final asymptotic `K^2 rho_2` specialization uses `d=O(sqrt(r))`.

This closes the fractional collar--residual compatibility problem after
noncontiguous collar patterns are allowed.  It does **not** contradict the
contiguous-collar Hall obstruction: that obstruction fixes the empirical
initial-segment length law `Pr(L>=j)=p_(r-j)`, whereas the present
decomposition is free to distribute collar ranks noncontiguously among
owners.

## 1. A bipartite rank graph

Construct a bipartite graph `H` having one distinguished edge `e_s` for
each rank `s<r`.

* For the residual ranks in `J`, make

  \[
                         e_1,e_2,\ldots,e_{r-a-1}
  \]

  the consecutive edges of one path.  Thus `e_s,e_t` meet exactly when
  `|s-t|=1`.
* For every collar rank `s in C`, make `e_s` an isolated edge in a separate
  component.

A matching of `H` is therefore exactly a rank set whose residual part has
no adjacent members.  The collar part is unrestricted.

Consider the polytope

\[
 \mathcal P_d(H)=
 \left\{x\in\mathbb R_{\ge0}^{E(H)}:
 x(\delta(v))\le1\ (v\in V(H)),\quad x(E(H))\le d\right\}.
\tag{1.1}
\]

### Lemma 1.1 (cardinality-capped bipartite matching integrality)

`mathcal P_d(H)` is integral.  Its vertices are incidence vectors of
matchings of size at most `d`.

### Proof

Orient every edge from the left shore to the right shore.  Add a source
joined to every left vertex by a capacity-one arc and join every right
vertex to a sink by a capacity-one arc.  Precede the source by one arc of
capacity `d`.  A feasible source--sink flow is determined on the middle
arcs by a vector in (1.1), and every vector in (1.1) extends to such a flow
by putting the corresponding incident sums on the outer arcs.

The network-flow polytope has an integral constraint matrix and integral
capacities.  Its projection to the middle arcs is therefore the convex hull
of integral middle-arc vectors, which are precisely matchings of size at
most `d`.  This proves the lemma. `square`

## 2. Rank-set decomposition

Put `x_(e_s)=q_s`.  At an internal path vertex, feasibility in (1.1) is
exactly

\[
                         q_s+q_{s+1}\le1.
\]

At every isolated collar edge it is `q_s<=1`, and the source-capacity row is
`sum_s q_s<=d`.  Thus (0.3) says precisely that `x in mathcal P_d(H)`.
By Lemma 1.1,

\[
                         q=\sum_\omega\lambda_\omega
                              \mathbf1_{R_\omega},
\qquad
 \lambda_\omega\ge0,\quad\sum_\omega\lambda_\omega=1,
\tag{2.1}
\]

where every `R_omega` has size at most `d` and has no adjacent residual
ranks.  An empty matching may be added to make the coefficients sum to one.
Sampling `R_omega` with probability `lambda_omega` proves (0.4).

For the asymptotic specialization, the largest two residual marginals have
ranks `r-a-1,r-a-2`.  The central-binomial estimate gives

\[
 p_{r-a-1}+p_{r-a-2}
 =2e^{-c^2+o(1)}<1
\tag{2.2}
\]

for fixed `c>sqrt(log 2)`.  Since `p_s` is increasing in `s<r` and
`q_s<=p_s`, every residual adjacent inequality follows.  The optimal
triangular vector has `sum_s q_s<=d`, so it belongs to (1.1).

## 3. One common owner ordering

Fix an owner `T`.  Conditional on `R_omega`, take a uniform permutation of
the `r` coordinates of `T`, and for every `s in R_omega` take its first `s`
coordinates.  These sets are nested in increasing rank, irrespective of
whether the collar ranks in `R_omega` are consecutive.  Their number is at
most `d`.

For a fixed target `S` of rank `s`, an owner containing `S` realizes it as
the first `s` elements with probability `1/binom(r,s)`.  There are
`binom(2r-s,r-s)` such owners.  Therefore

\[
 d_x(S)
 ={ {2r-s\choose r-s}q_s\over {r\choose s}}
 ={q_s\over p_s},
\tag{3.1}
\]

using

\[
 { {2r-s\choose r-s}\over {r\choose s}}
 ={W\over {2r\choose s}}={1\over p_s}.
\]

This proves (0.5).  More importantly, collar and residual targets in one
atom are prefixes of the **same** ordering.  Hence every residual target is
contained in every later selected collar target, and pointwise capacity is
already enforced by `|R_omega|<=d`.  No separate random collar length or
post hoc owner compatibility is used.

## 4. Residual pair codegrees

Work in the asymptotic specialization of Section 0, and restrict attention
to supported positive-degree residual targets in
`mathcal I={r-b,...,r-a-1}`, where `a+1<=b=o(r)`.  If a residual marginal
`q_s` is zero, every atom containing rank `s` has zero weight, so all pairs
through such a target have degree zero and may simply be omitted from the
normalized maximum.  If two distinct supported residual targets have
nonzero codegree, they form a flag `S subset U` of ranks `s<t`; by the
matching construction, `t-s>=2`.  Write

\[
                         \eta_{s,t}=\Pr(s,t\in R).
\]

Always

\[
                         \eta_{s,t}\le\min(q_s,q_t).
\tag{4.1}
\]

The uniform-order flag formula gives

\[
 {d_x(S,U)\over d_x(U)}
 ={\eta_{s,t}\over q_t{t\choose s}}
 \le {1\over {t\choose s}},
\tag{4.2}
\]

and

\[
 {d_x(S,U)\over d_x(S)}
 ={\eta_{s,t}\over q_s{2r-s\choose t-s}}
 \le {1\over {2r-s\choose t-s}}.
\tag{4.3}
\]

On the stated band, `2<=t-s<=b=o(r)`, so both denominators are
`Omega(r^2)`.
For an owner-target pair,

\[
 {d_x(o_T,S)\over d_x(S)}
 ={p_s\over {r\choose s}}
 ={1\over {2r-s\choose r-s}}=O(r^{-2}),
\tag{4.4}
\]

since every retained residual target has owner codimension between `a+1`
and `b`, and hence between `2` and `o(r)`.  The target degree is at most one
by `q_s<=p_s`, whereas every owner has degree one, so (4.4) is exactly the
normalization by the smaller incident degree; it also bounds the raw pair
degree divided by the owner degree.  Distinct owners have codegree zero.
Equations (4.2)--(4.4) prove the first part of (0.6); `K<=d+1=O(sqrt(r))`
in the optimal-depth specialization proves the second.

Pairs involving a collar target are deliberately excluded from (0.6).
The arbitrary collar subset may contain adjacent ranks, so those pairs can
remain on the critical `Theta(1/r)` scale.  This is why the theorem is a
fractional compatibility result, not a black-box integral rounding theorem.

## 5. Exact scope after the contiguous-collar no-go

The theorem proves:

1. the optimal rank marginals, total owner capacity, collar targets, and a
   no-adjacent residual support coexist in one fractional common-order flag
   law;
2. every pair collision internal to the retained central residual band is
   subcritical at order `r^-2`; and
3. the forced `Omega(sqrt(r)W)` Hall deficit of a contiguous collar is
   avoided at rank level.

It does not prove:

1. an integral matching of the named owner-plus-flag atoms;
2. exact prechainization of the collar inside the support of one residual
   matching;
3. the sliding Ferrers cocycle or literal interval closure; or
4. upper coverage, common-cap routing, topology, or regeneration.

The next lower-side target is therefore a **noncontiguous-collar Boolean
absorber**: round the combined atom law while using switches on the critical
collar coordinates and preserving the already subcritical residual bank.
