# Audit of fixed sharp-shield factor extension

**Date:** 2026-08-05  
**Method:** independent protected-Ore, exposure, near-shadow, optional-core,
and Kruskal--Katona replay; no computation or search  
**Audited theorem:**
`MATH_THEOREM_FIXED_SHARP_SHIELD_BANK_EXTENDS_TO_MIDDLE_LEVELS_TWO_FACTOR_20260805.md`

## 0. Verdict

**PASS after simplifying the all-cut proof.**  For every fixed `q`, a bank
of `q` pairwise resource-disjoint sharp shields extends to a spanning
Middle-Levels two-factor for all sufficiently large `m`.

The first draft imported the older reservoir's exponential cutoff and
described the Kruskal--Katona estimate as uniform over arbitrary polynomial
sizes.  Neither is needed.  Here `|E(P)|=O_q(m)`, so the general near-shadow
theorem gives an `O_q(m^2)` small/co-small cutoff.  The theorem has been
patched to use that exact cutoff.

## 1. Orbit and exposure replay

A shield has `m` rank-`m` owners, `m-1` rank-`m-1` transition facets, and
`m-1` rank-`m+1` edge unions.  Under a uniform coordinate permutation each
fixed vertex is uniform in its rank layer.  After a fixed number of previous
shields, each forbidden layer has `O_q(m)` vertices, while every relevant
layer is exponential.  The expected collision count tends to zero, proving
the fixed-bank selection.

For owners `T_i,T_j` of one geodesic,

\[
                         |T_i\cap T_j|=m-|i-j|.
\]

A rank-`m-1` lower vertex can therefore lie below at most two path owners.
Similarly

\[
                         |I_i\cup I_j|=m-1+|i-j|
\]

shows that one rank-`m` owner contains at most two path transition facets.
Thus

\[
 \ell_P(x)\le2q,
 \qquad z_U\le2q.
\]

All `2q` path endpoints are legitimately placed in the deterministic top
endpoint bank, leaving private endpoint exposure zero.  The protected bank
has exactly `2q(m-1)` incidence edges.

## 2. Near-shadow and co-small replay

The general protected-Ore near-shadow theorem applies to every maximum-
degree-two protected bank.  With `e=2q(m-1)`, any failed shore satisfies

\[
 \min\{|A|,W-|A|\}
 <{m(m-1)\over2m-1}e=O_q(m^2).
\]

For a co-small failure, the exact optional-complement identity gives a
positive minimal optional core `B^-` and an owner family `Q` with
`|Q|>|B^-|`.  Since every owner contains at most `2q` forced transition
facets and has residual capacity at most two, every member of `Q` contains
at least

\[
                         D=m-2q-1
\]

members of `B^-`.  The sharp one-sided partial-shadow theorem yields

\[
 |B^-|\ge{2D-1\choose D-1}+1=2^{2m-o(m)},
\]

contradicting the `O_q(m^2)` co-small cutoff.  This verifies that the
generic forced-facet corollary is applicable; none of the old reservoir's
random-trace structure is being imported.

## 3. Small-shore replay

For a small shore `A`, the exact path-forest loss identity gives

\[
 \lambda_P(A)
 \le2q|A|+\min\left\{2q,{|A|\choose2}\right\}.
\]

The endpoint term is exact: a counted deterministic endpoint contains a
pair of selected facets, and two distinct rank-`m-1` facets have at most one
common rank-`m` owner.

The near-shadow cutoff is `O_q(m^2)`, hence eventually smaller than
`binom(m+3,3)`.  Writing `|A|=binom(x,m)` gives `x<m+3`; Kruskal--Katona and
the exact shadow-slack inequality therefore give

\[
 \sigma(A)>
 { (m-2)(m-4)\over4(m-1)}|A|.
\]

For fixed `q`, this dominates the protected loss for all sufficiently large
`m`.  Singletons pass separately because
`lambda_P({x})<=2q<m-2=sigma({x})`.

## 4. Scope

The result is an unrooted owner/lower-q1 factor-extension theorem.  It does
not place the paths at prescribed directed positions in PBBS components,
connect the completed factor, construct source antecedents, or preserve the
upper deck and terminal common cap.

## 5. Independent cut-form replay

There is also a direct exact form of the residual criterion.  Let `G` be an
`m`-regular balanced bipartite graph on shores `L,R`, let `F` have maximum
degree two, put `H=G-F`, and set `b(v)=2-d_F(v)`.  The bipartite `b`-factor
criterion is

\[
 e_H(A,R\setminus B)\ge b(A)-b(B)
 \qquad(A\subseteq L,\ B\subseteq R).
\]

With `X=L\setminus A` and

\[
 q=|B|-|A|=|X|+|B|-|L|,
\]

direct degree algebra gives

\[
 e_H(A,R\setminus B)-b(A)+b(B)
 =(m-2)(|A|-|B|)+e_H(X,B).
\]

Thus cuts with `q<=0` are automatic, while cuts with `q>0` are equivalent
to

\[
 e_H(X,B)\ge(m-2)q.
\]

Using regular edge balance, this is also equivalent to

\[
 e_F(X,B)\le2q+e_G(A,R\setminus B).
\]

This confirms the cut algebra used to motivate the shield extension.  The
proof in the theorem closes these cuts through near-shadow and forced-facet
structure rather than assuming the final inequality.
