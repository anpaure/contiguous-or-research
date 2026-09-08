# Perfect-matching maximum entropy gives the exact marginals, but not Strong Rayleigh concentration

**Date:** 2026-08-05  
**Method:** pure mathematics and primary-source scope audit; no finite or
computational search and no solver  
**Status:** unconditional exact-marginal Gibbs realization for the augmented
Boolean one-step flow.  Unconditional no-go for obtaining the required
Chernoff oracle from edge-coordinate Strong Rayleigh theory: no
nondegenerate probability law supported on perfect matchings of any simple
graph is edge-Strong-Rayleigh.  For positive-weight laws on the augmented
Boolean graph, a conditional `K_(2,2)` face gives an elementary positive-
correlation witness.

## 0. Question and answer

The one-step theorem in
`MATH_THEOREM_COLORED_BOOLEAN_ONE_STEP_UNIFORM_FLOW_CONTRACTION_AND_EXACT_ROUNDING_GAP_20260805.md`
constructs the fractional perfect matching

\[
 x_{S,T}={1\over 2r-q}
 \quad(S\subset T,\ |S|=q),
 \qquad
 x_{d,T}={1\over C_{q+1}}
 \quad(d\text{ a start dummy})
\tag{0.1}
\]

on the augmented Boolean interface `J_q`.  The open rounding question was
whether one can sample an integral perfect matching with these exact edge
marginals and obtain Chernoff concentration for every future-owner linear
statistic.

There is a canonical exact-marginal distribution: an edge-weighted
maximum-entropy perfect-matching law.  However, no nontrivial distribution
on perfect matchings can be Strong Rayleigh in the edge indicators.  Thus
stability/negative-association machinery does not prove the desired oracle.

## 1. Interior points have exact-marginal Gibbs laws

Let `G=(L,R;E)` be a finite bipartite graph with a perfect matching.  For a
perfect matching `M`, let `a_M in {0,1}^E` be its incidence vector, and put

\[
 P_G=\operatorname{conv}\{a_M:M\text{ is a perfect matching of }G\}.
\tag{1.1}
\]

### Theorem 1.1 (maximum-entropy realization)

For every `x in relint(P_G)`, there are strictly positive edge weights
`w_e` such that the probability law

\[
 \Pr_w(M)={\prod_{e\in M}w_e
              \over
              \sum_{M'}\prod_{e\in M'}w_e}
\tag{1.2}
\]

has

\[
                         \Pr_w(e\in M)=x_e
                         \qquad(e\in E).
\tag{1.3}
\]

#### Proof

Work in the affine span of `P_G`, modulo the vectors whose inner product is
constant on every `a_M`.  For `theta in R^E`, define

\[
 F_x(\theta)=
 \log\sum_M\exp\langle\theta,a_M\rangle
 -\langle\theta,x\rangle.
\tag{1.4}
\]

On the quotient, `F_x` is strictly convex.  Since `x` is in the relative
interior, every nonzero quotient direction has incidence vectors on both
sides of its `x`-expectation.  It follows that `F_x(theta)` tends to
infinity along every unbounded quotient ray.  Hence `F_x` has a minimizer
`theta^*`.

At that minimizer,

\[
 0=\nabla F_x(\theta^*)
  ={\sum_M a_M\exp\langle\theta^*,a_M\rangle
       \over
       \sum_M\exp\langle\theta^*,a_M\rangle}-x.
\tag{1.5}
\]

Taking `w_e=exp(theta_e^*)` gives (1.2)--(1.3). `square`

This is the finite exponential-family mean-parameter theorem.  The proof
is included to make clear that no algorithmic approximation and no
boundary limit is being used.

### Corollary 1.2 (exact Gibbs law for the Boolean flow)

The fractional point (0.1) is in `relint(P_(J_q))`.  Consequently it is the
edge-marginal vector of a positive-weight perfect-matching Gibbs law.

#### Proof

For a bipartite graph, the perfect-matching polytope is exactly

\[
 \{z\in\mathbb R_{\ge0}^E:
   z(\delta(v))=1\text{ for every }v\in L\cup R\}.
\tag{1.6}
\]

Theorem 1.1 of the one-step note proves that (0.1) satisfies all degree
equalities, and every coordinate in (0.1) is strictly positive.  Hence it
lies in the relative interior of (1.6).  Apply Theorem 1.1. `square`

Thus exact marginal existence is not the missing theorem.

## 2. A two-matching face is positively correlated

Consider `K_(2,2)` with left vertices `a,b`, right vertices `u,v`, and
strictly positive edge weights.  It has two perfect matchings

\[
 M_0=\{au,bv\},
 \qquad
 M_1=\{av,bu\}.
\tag{2.1}
\]

Put `p=Pr(M_0)`, so `0<p<1`.  Then

\[
 \Pr(au\in M)=\Pr(bv\in M)=p,
 \qquad
 \Pr(au,bv\in M)=p.
\tag{2.2}
\]

Therefore

\[
 \operatorname{Cov}(1_{au\in M},1_{bv\in M})
 =p-p^2=p(1-p)>0.
\tag{2.3}
\]

So this edge-indicator law is not negatively associated and hence is not
Strong Rayleigh.

## 3. The no-go occurs inside every augmented Boolean interface

### Theorem 3.1 (conditional-square obstruction)

Assume `J_q` has at least two start dummies.  Every perfect-matching Gibbs
law on `J_q` with strictly positive edge weights fails the Strong Rayleigh
property in its edge coordinates.

#### Proof

Choose any perfect matching `M` of `J_q`, two distinct start dummies
`d_1,d_2`, and let `T_1,T_2` be the right vertices matched to them in `M`.
Condition on every edge of

\[
 M\setminus\{d_1T_1,d_2T_2\}
\tag{3.1}
\]

being selected.  Matching constraints then remove all other vertices and
leave exactly `d_1,d_2` and `T_1,T_2`.  Since every start dummy is adjacent
to every right vertex, the residual graph is `K_(2,2)`.  Strict positivity
of the original edge weights gives positive weight to both residual
perfect matchings.

Strong Rayleigh measures are closed under coordinate conditioning and are
negatively associated after every such conditioning.  But the conditional
law violates pairwise negative correlation by (2.3).  The original law
therefore cannot be Strong Rayleigh. `square`

For `n=2r`, `q<r`, and `r>=2`,

\[
 H_{q+1}=C_{q+1}-C_q\ge2,
\tag{3.2}
\]

so the obstruction applies throughout the nontrivial Boolean interfaces
used in the construction.

### Corollary 3.2

The exact-marginal Gibbs law from Corollary 1.2 is not Strong Rayleigh.
In particular, the desired arbitrary-linear-statistic Chernoff oracle does
not follow from:

* Strong Rayleigh concentration for its edge indicators;
* negative association of all disjoint edge families; or
* conditioning an edge-variable monomer--dimer Strong Rayleigh law to
  perfect cardinality.

The last bullet is not merely a failure of proof technique: the resulting
perfect-matching edge law has the explicit conditional positive
correlation above.

## 4. Stronger support obstruction: no nondegenerate perfect-matching law is Strong Rayleigh

The preceding conditional-square proof uses positive weights and the
universal dummies.  The actual obstruction is completely general.

### Lemma 4.1 (perfect matchings cannot be two matroid bases)

Let `G` be a simple graph.  A family of perfect matchings of `G` which is
the set of bases of a matroid contains at most one matching.

#### Proof

Suppose it contains distinct perfect matchings `M,N`.  Choose
`e=uv in M\setminus N`.  The matroid basis-exchange axiom would give an
edge `f in N\setminus M` such that

\[
                         M-e+f
\tag{4.1}
\]

is another base, hence another perfect matching of `G`.

After deleting `e`, precisely `u` and `v` are unmatched.  Adding one edge
repairs the matching only if that edge joins `u` and `v`.  Since `G` is
simple, the unique such edge is `e`, but `e` is not in `N\setminus M`.
Contradiction. `square`

### Theorem 4.2 (universal edge-Strong-Rayleigh no-go)

Every Strong Rayleigh probability measure supported on the perfect
matchings of a simple graph is concentrated on one perfect matching.

#### Proof

Its edge generating polynomial is multi-affine and homogeneous because
all perfect matchings have the same cardinality.  The support theorem of
Choe--Oxley--Sokal--Wagner says that the support of a homogeneous
multi-affine stable polynomial is the set of bases of a matroid.  Lemma
4.1 says that a matroid base family contained in the perfect matchings is a
singleton. `square`

### Corollary 4.3

No probability distribution with the strictly fractional edge marginals
(0.1) can be Strong Rayleigh in edge coordinates, regardless of whether it
is Gibbs, maximum entropy, full support, or sparse support.

This is stronger than Theorem 3.1.  The conditional square remains useful
as a self-contained elementary certificate for the natural full-support
Gibbs law.

## 5. Why the Heilmann--Lieb theorem does not contradict this

The stable multivariate matching polynomial used in the
Heilmann--Lieb/Borcea--Branden theory is a **vertex-variable** polynomial.
It records which vertices are covered, with the matching edge weights as
coefficients.  On perfect matchings every vertex is covered, so its top
perfect-cardinality part is a constant multiple of the single monomial

\[
                         \prod_{v\in V(G)}z_v.
\tag{5.1}
\]

That stability statement contains no information about which edges were
chosen.

The edge-variable matching generating polynomial is a different object.
Already its perfect-cardinality part on `K_(2,2)` is

\[
 w_{au}w_{bv}z_{au}z_{bv}
 +w_{av}w_{bu}z_{av}z_{bu},
\tag{5.2}
\]

whose probability measure has the positive covariance (2.3).  It is not
real stable.  Thus one cannot transfer the vertex-variable matching
polynomial theorem to edge-indicator concentration.

Primary scope references:

* J. Borcea, P. Branden and T. Liggett, *Negative dependence and the
  geometry of polynomials*, JAMS 22 (2009), arXiv:0707.2340: Strong
  Rayleigh measures are stable edge/subset generating measures and enjoy
  conditional negative association.
* Y.-B. Choe, J. Oxley, A. Sokal and D. Wagner, *Homogeneous multivariate
  polynomials with the half-plane property*, Advances in Applied
  Mathematics 32 (2004), arXiv:math/0202034: the support of a homogeneous
  multi-affine stable polynomial is the set of bases of a matroid.
* J. Leake and N. Ryder, *Generalizations of the Matching Polynomial to
  the Multivariate Independence Polynomial*, Algebraic Combinatorics 2
  (2019), arXiv:1610.00805: distinguishes the stable vertex matching
  polynomial from the edge matching generating polynomial.

## 6. Exact surviving frontier

The maximum-entropy calculation closes one row:

\[
 \boxed{\text{there is a positive perfect-matching law with exactly (0.1)}}.
\tag{6.1}
\]

The support theorem closes one proposed route negatively:

\[
 \boxed{\text{no nondegenerate perfect-matching law is edge-Strong-Rayleigh}}.
\tag{6.2}
\]

This does **not** disprove the one-step Chernoff oracle.  Strong Rayleigh is
much stronger than concentration of the particular aggregate
future-owner statistics used in the Boolean construction.  The exact next
question is therefore Boolean-specific:

> Does the exact-marginal maximum-entropy law, or another exact-marginal
> distribution on perfect matchings of `J_q`, concentrate the prescribed
> colour-by-future-owner sums despite its unavoidable local positive edge
> correlations?

The `K_(2,2)` obstruction is microscopic and does not by itself rule out
that aggregate concentration.  Any proof must exploit the high-dimensional
Boolean inclusion geometry, exchange entropy, or direct martingale/
spectral control; generic Strong Rayleigh theory cannot supply it.
