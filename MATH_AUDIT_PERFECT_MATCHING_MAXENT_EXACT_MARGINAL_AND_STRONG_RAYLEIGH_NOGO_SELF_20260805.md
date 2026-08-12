# Self-audit: perfect-matching maximum entropy and Strong Rayleigh no-go

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_PERFECT_MATCHING_MAXENT_EXACT_MARGINAL_AND_STRONG_RAYLEIGH_NOGO_20260805.md`  
**Verdict:** GO, with the scope limitation in Section 6 below.

## 1. Maximum-entropy mean map

Let `Omega` be the finite set of perfect matchings and `a_M` their edge
incidence vectors.  On the quotient by affine constants, the Hessian of

\[
 \log\sum_M e^{\langle\theta,a_M\rangle}
\]

is the covariance matrix of `a_M` under a full-support Gibbs law.  It is
positive definite on the quotient.  If `x in relint conv{a_M}`, then along
every nonzero quotient ray some `a_M-x` has positive inner product and
some has negative inner product.  Hence the dual objective is coercive in
both ray directions.  The gradient equation at its minimizer gives exactly
`E[a_M]=x`.  This validates Theorem 1.1.

## 2. Relative-interior application

The bipartite perfect-matching polytope has only the degree equalities and
edge nonnegativity inequalities.  Formula (0.1) is feasible by the prior
one-step theorem and is strictly positive on every edge of `J_q`.  It is
therefore in the relative interior.  No claim of efficiently computing the
Gibbs weights is made.

## 3. Conditional square

Fixing all but two dummy edges of an incumbent perfect matching leaves:

* two unmatched universal dummies;
* their two unmatched right endpoints;
* all four dummy-to-endpoint edges;
* exactly two residual perfect matchings.

Positive Gibbs weights make both residual matchings positive.  For two
opposite edges in one residual matching, with its probability `p`, the
covariance is `p(1-p)>0`.  Thus the conditional law is not pairwise
negatively correlated.

Strong Rayleigh implies conditional negative association, so the original
law is not Strong Rayleigh.  This argument does not require that an
arbitrary preselected pair of right vertices be reservable: the two right
vertices are read from an already existing perfect matching.

## 4. Dummy count

For `n=2r` and `q<r`, the ratios satisfy

\[
 {C_{q+1}\over C_q}={2r-q\over q+1}>1.
\]

At the smallest nontrivial case `r=2,q=1`, the difference is `6-4=2`;
all other relevant cases have at least two dummies as well.  The theorem
explicitly states its assumption, so no exceptional interface is hidden.

## 5. Matching-polynomial scope

The stable vertex-variable matching polynomial marks covered vertices.
After restriction to perfect matchings, every monomial has the same vertex
support and the polynomial collapses to one vertex monomial times the
weighted perfect-matching partition function.  It cannot imply dependence
properties among edge choices.

The edge-variable perfect-matching polynomial on `K_(2,2)` produces the
two-match law audited above.  Since Strong Rayleigh implies pairwise
negative correlation, its positive covariance is already a complete
nonstability certificate; no numerical root computation is needed.

## 5.1 Stronger support-matroid replay

A Strong Rayleigh law supported on perfect matchings has a homogeneous
multi-affine stable edge generating polynomial.  The
Choe--Oxley--Sokal--Wagner support theorem therefore makes its support a
matroid base family.

Take two distinct perfect matchings `M,N` and `e=uv in M\setminus N`.
After deleting `e` from `M`, exactly `u,v` are exposed.  A one-edge basis
exchange repairs perfectness only by adding the edge `uv=e`, which is not
in `N\setminus M`.  Thus the matroid basis-exchange axiom fails.  Any
matroid base family contained in a simple graph's perfect matchings is
therefore a singleton.

This validates the stronger conclusion: no nondegenerate perfect-matching
distribution at all can be edge-Strong-Rayleigh.  The conditional square
is only the elementary full-support witness.

## 6. Scope limitation

The no-go excludes edge-coordinate Strong Rayleigh as the proof of the
required oracle for **every** exact fractional-marginal distribution.  It
does **not** exclude:

* Chernoff concentration for the particular aggregate Boolean tests;
* another exact-marginal distribution not of edge-product Gibbs form;
* a direct martingale, spectral-independence, exchange-chain, entropy, or
  discrepancy proof tailored to `J_q`;
* scaled-loss rounding plus regeneration.

In particular, a microscopic positively correlated edge pair need not
destroy concentration of macroscopic owner-count statistics.  The theorem
does not overclaim otherwise.

## 7. Source audit

The mathematical uses of the literature are limited to standard theorem
scope:

* Borcea--Branden--Liggett: Strong Rayleigh implies conditional negative
  association and is closed under conditioning;
* Choe--Oxley--Sokal--Wagner: homogeneous multi-affine stable supports are
  matroid base families;
* Leake--Ryder: vertex and edge multivariate matching polynomials are
  distinct, and stability of the former does not assert stability of the
  latter.

All application-specific conclusions are proved directly in the theorem.
