# Independent audit: noncontiguous collar/residual rank matching polytope

**Date:** 2026-08-03  
**Audited theorem:**
`MATH_THEOREM_NONCONTIGUOUS_COLLAR_RESIDUAL_RANK_MATCHING_POLYTOPE_20260803.md`  
**Audited theorem SHA-256:**
`b05fcb088b9513b06e499e411dad7a32a7f58d1c58e692d24d7307c32d39599b`  
**Method:** independent symbolic proof audit; no finite search or numerical
solver was used.

## 0. Verdict

**GO after three scope repairs made directly in the theorem.**  The
cardinality-capped rank-matching polytope is integral, its decomposition
gives exactly the asserted common-owner-order law, and the complete
normalized pair ledger on the retained residual band is `O(r^-2)`.

The original draft required three clarifications, all now incorporated:

1. the `O(r^-2)` claim applies to the explicitly retained band
   `I={r-b,...,r-a-1}`, with `a+1<=b=o(r)`, not to arbitrarily small
   residual ranks;
2. `K^2 rho_2=O(r^-1)` uses the optimal-depth specialization
   `d=O(sqrt(r))`, while the rank-set decomposition itself permits arbitrary
   positive integer `d`; and
3. normalized ratios are taken only over supported positive-degree target
   vertices.  A zero marginal has zero pair degree and is omitted.

These are scope corrections, not failures of the construction.  After the
repairs, every displayed conclusion follows.

## 1. Cardinality-capped matching integrality

Let `H=(L,R;E)` be the disjoint union of the residual path and the isolated
collar edges.  Consider

\[
 P_d(H)=\{x\ge0:x(\delta(v))\le1\ (v\in L\cup R),\quad
                    x(E)\le d\}.
\]

The flow representation in the theorem is exact.  Add nodes
`s_0,s,t`; use one arc `s_0->s` of capacity `d`, arcs `s->u` of capacity
one for `u in L`, the oriented middle arcs `u->v` for `uv in E`, and arcs
`v->t` of capacity one for `v in R`.  Given `x in P_d(H)`, put flow
`x(uv)` on each middle arc, flow `x(delta(u))` on `s->u`, flow
`x(delta(v))` on `v->t`, and total flow `x(E)` on `s_0->s`.  This is a
feasible flow.  Conversely, flow conservation projects every feasible flow
to a vector satisfying exactly the rows of `P_d(H)`.

All capacities are integral and the node-arc matrix is totally unimodular.
The flow polytope is therefore the convex hull of integral flows.  Coordinate
projection gives the convex hull of their integral middle-arc vectors.
Those vectors are precisely matchings of size at most `d`.  Thus adding the
cardinality cap introduces no fractional vertices.

For the chosen graph, the path vertex inequalities are exactly

\[
                         q_s+q_{s+1}\le1
\]

for consecutive residual ranks.  An isolated collar edge requires only
`q_s<=1`, which follows from `q_s<=p_s<=1`; the flow-value row is
`sum_s q_s<=d`.  Hence the hypotheses are exactly membership in `P_d(H)`,
and convex decomposition gives a law on rank sets of size at most `d` with
the desired marginals and no adjacent residual ranks.

## 2. Exact common-order degree calculation

Fix an owner `T in binom([2r],r)`.  Conditional on a sampled rank set `R`,
choose one uniform ordering of `T` and use its prefixes at all ranks in `R`.
All marked targets in the atom are therefore on one literal inclusion chain;
there is no independent collar ordering hidden in the construction.

For a fixed rank-`s` target `S`, there are
`binom(2r-s,r-s)` owners containing it.  In each such owner the probability
that rank `s` is selected and its prefix equals `S` is

\[
                         {q_s\over\binom rs}.
\]

Therefore

\[
 d_x(S)=\binom{2r-s}{r-s}{q_s\over\binom rs}
       ={q_s\over p_s},
\]

using

\[
 {\binom{2r-s}{r-s}\over\binom rs}
 ={\binom{2r}r\over\binom{2r}s}={1\over p_s}.
\]

Every owner has total atom weight one.  Since `q_s<=p_s`, every named
target has degree at most one.

## 3. Adjacent inequalities in the residual path

The sequence `p_s=binom(2r,s)/binom(2r,r)` is increasing for `s<r`.
Thus the largest adjacent sum inside
`J={1,...,r-a-1}` is

\[
                         p_{r-a-2}+p_{r-a-1}.
\]

For `a=(c+o(1))sqrt(r)`, the local central-binomial estimate gives

\[
 p_{r-a-2}+p_{r-a-1}=2e^{-c^2+o(1)}.
\]

This is strictly below one for fixed `c>sqrt(log 2)`.  Hence every
`q_s<=p_s` satisfies all adjacent path inequalities for sufficiently large
`r`.  Together with `sum q_s<=d`, this verifies the asserted specialization
to the optimal triangular residual vector.

## 4. Exhaustive normalized pair ledger

Write `eta_(s,t)=Pr(s,t in R)`.  The only nonzero target-target pair degrees
occur for nested targets `S subset U`; targets of equal rank or incomparable
targets cannot be two prefixes of one order.  If `|S|=s<t=|U|`, then

\[
 d_x(S,U)
 =\binom{2r-t}{r-t}
   {\eta_{s,t}\over\binom rt\binom ts}.
\]

Dividing first by the degree of `U` and then by the degree of `S` gives the
two exact identities

\[
 {d_x(S,U)\over d_x(U)}
 ={\eta_{s,t}\over q_t\binom ts},
 \qquad
 {d_x(S,U)\over d_x(S)}
 ={\eta_{s,t}\over q_s\binom{2r-s}{t-s}}.
\]

For positive marginals, `eta_(s,t)<=min(q_s,q_t)`.  The residual matching
law also forces `t-s>=2`.  On
`I={r-b,...,r-a-1}`, with `b=o(r)`, we have
`2<=t-s<=b`; for sufficiently large `r` this lies below half of each upper
binomial argument.  Consequently both binomial denominators are at least a
constant multiple of `r^2`.  Both endpoint-normalized ratios are therefore
`O(r^-2)`, uniformly even when one positive `q_s` is arbitrarily small.
If a marginal is zero, the associated pair degree is zero instead.

For an owner-target pair with `S subset T`,

\[
 d_x(o_T,S)={q_s\over\binom rs},\qquad
 {d_x(o_T,S)\over d_x(S)}
 ={p_s\over\binom rs}
 ={1\over\binom{2r-s}{r-s}}.
\]

Here `a+1<=r-s<=b=o(r)`, so the denominator is at least
`binom(r,2)` for all sufficiently large `r`.  Since the target degree is at
most one and the owner degree equals one, this is normalization by the
smaller incident degree; it also bounds normalization by the owner degree.
Two owner vertices never share an atom.

This exhausts all pair types involving owners and retained residual
targets.  Hence

\[
                         \rho_2^{residual}=O(r^{-2}).
\]

Every atom has one owner plus at most `d` targets, so `K<=d+1`.  In the
optimal-depth regime `d=O(sqrt(r))`, and therefore

\[
                         K^2\rho_2^{residual}=O(r^{-1}).
\]

Pairs involving a collar target, cross collar/residual pairs, and pairs
through residual ranks below `r-b` are intentionally outside this estimate.
They may remain at the critical `Theta(1/r)` scale.

## 5. Scope relative to the contiguous-collar obstruction

The contiguous-collar theorem assumes that the collar ranks assigned to an
owner form one adjacent-rank initial segment.  Exact collar counts then
force

\[
                         Pr(L\ge j)=p_{r-j},
\]

and the residual set has the random pointwise capacity `d+C-L`.  The present
law imposes neither property: collar ranks are isolated edges in the rank
graph, may be selected noncontiguously, and share only the global bound
`|R|<=d` with the residual ranks.  Thus it legitimately escapes the stated
Hall row and does not contradict it.

The theorem remains fractional.  It does not provide an integral named-
target matching, a literal Ferrers chronology, an all-rank subcritical
hypergraph, upper coverage, topology, common-cap routing, or regeneration.
The next lower-side problem is exactly the scoped one stated by the theorem:
round the noncontiguous collar/residual atom law with a Boolean-specific
absorber while controlling the still-critical collar incidences.

