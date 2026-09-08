# Symmetric random pure-rail shells satisfy the named-order fractional checkpoint uniformly

**Date:** 2026-08-13  
**Input:** `MATH_THEOREM_OVERLAPPING_CORE_POSITIVE_ROLE_FLOW_AND_ORDERING_GATE_20260813.md`  
**Method:** exact orbit counting and Bernstein concentration  
**Status:** unconditional quantitative fractional theorem.  It constructs a
deterministic multiset of actual core-disjoint rail shells for which uniform
random cyclic orders give load \(1+e^{-\Omega(q)}\) at every named owner and
weighted pair-codegree \(O(k^{-2})\).  It does **not** make the ground-point
role equations exact and it does not round the cyclic orders integrally.

## 1. The multiple-choice ordering hypergraph

Put

\[
 q=d+1,\qquad c=R-q,\qquad M=k-c,
 \qquad W={k\choose R}.
\tag{1.1}
\]

For a period (N\ge 2q+2), a **shell** is a pair

\[
 (C,T),\qquad |C|=c,\quad |T|=N,\quad C\cap T=\varnothing.
\tag{1.2}
\]

Let \(\Omega(T)\) be the cyclic orders of \(T\), modulo rotation.  A choice
\(\sigma\in\Omega(T)\) gives the closed pure-rail owner deck

\[
 \mathcal D(C,T,\sigma)
 =\{C\cup I_i^q(\sigma):i\in\mathbb Z_N\}.
\tag{1.3}
\]

Given labelled shell tokens \(j\in\mathcal J\), form the multiple-choice
hypergraph \(\mathcal G\) with vertex set

\[
 \mathcal J\ \dot\cup\ { [k]\choose R}
\tag{1.4}
\]

and one edge

\[
 E(j,\sigma)=\{j\}\cup\mathcal D(C_j,T_j,\sigma)
\tag{1.5}
\]

for every cyclic order of shell \(j\).  A perfect matching of
\(\mathcal G\) is exactly a choice of one order for every shell whose owner
decks partition the named owner layer.  These edges have one token plus
the \(N\) owners; this token augmentation is separate from the owner-only
orbit hypergraph in Section 5.

Give every order of a fixed token equal weight:

\[
 z_{j,\sigma}=\frac1{|\Omega(T_j)|}.
\tag{1.6}
\]

Every token then has fractional load one.  A named owner \(A\) has load

\[
 L_A=\sum_j
 \frac{N_j}{{N_j\choose q}}
 \mathbf 1\{C_j\subset A,\ A\setminus C_j\subseteq T_j\}.
\tag{1.7}
\]

Thus \(L_A=1\) is precisely equation (6.5) of the input note.

## 2. One symmetric shell is exactly unbiased

Choose a shell of period \(N\) uniformly: first choose \(C\) uniformly
from \({[k]\choose c}\), then choose \(T\) uniformly from
\({[k]\setminus C\choose N}\).

### Lemma 2.1 (named-owner eligibility)

For every named owner (A\in{[k]\choose R}),

\[
 \boxed{
 \Pr(C\subset A,\ A\setminus C\subseteq T)
 ={N\choose q}\frac1W.}
\tag{2.1}
\]

Consequently the expected contribution of this shell to (1.7) is

\[
 \boxed{\mathbb E X_{N,A}=\frac NW,}
 \qquad
 X_{N,A}:=\frac N{{N\choose q}}
 \mathbf1\{C\subset A,\ A\setminus C\subseteq T\}.
\tag{2.2}
\]

#### Proof

Every shell contains exactly \({N\choose q}\) eligible owners, namely

\[
 \{C\cup Q:Q\in{T\choose q}\}.
\]

The shell distribution is invariant under the transitive action of
\(S_k\) on the \(W\) named owners.  Hence every owner has eligibility
probability \({N\choose q}/W\).  Multiplication by the uniform-order
window probability (N/{N\choose q}) gives (2.2). \(\square\)

In particular, for arbitrary prescribed periods (N_j), independent
symmetric shells satisfy

\[
 \mathbb E L_A=\frac1W\sum_jN_j.
\tag{2.3}
\]

Thus the sole scalar equation

\[
                         \sum_jN_j=W
\tag{2.4}
\]

makes every named-owner fractional equation exact **in expectation**.
No ground-point or orbit averaging is being substituted for named owners
here.

## 3. Uniform concentration over every named owner

Let

\[
 b_*:=\max_j\frac{N_j}{{N_j\choose q}}.
\tag{3.1}
\]

### Theorem 3.1 (robust named-owner fractional checkpoint)

Assume (2.4), and choose all shells independently and symmetrically as
above.  If

\[
 \eta:=4\sqrt{b_*\log(4W)}\le1,
\tag{3.2}
\]

then with positive probability

\[
 \boxed{|L_A-1|\le\eta
 \quad\text{for every }A\in{[k]\choose R}.}
\tag{3.3}
\]

Hence there is a deterministic multiset of actual shells satisfying
(3.3).

#### Proof

For fixed \(A\), the variables \(X_{N_j,A}\) in (2.2) are independent,
take values in \([0,b_*]\), and have total mean one.  Moreover

\[
 \sum_j\operatorname {Var}X_{N_j,A}
 \le \sum_j b_*\mathbb EX_{N_j,A}=b_*.
\tag{3.4}
\]

Bernstein's inequality, using \(0<\eta\le1\), gives

\[
 \Pr(|L_A-1|>\eta)
 \le2\exp\left(-\frac{\eta^2}
 {2(b_*+b_*\eta/3)}\right)
 \le2\exp\left(-\frac{3\eta^2}{8b_*}\right).
\tag{3.5}
\]

With (3.2), the last expression is at most
\(2(4W)^{-6}\).  A union bound over the \(W\) owners is strictly less
than one. \(\square\)

For the two shortest legal periods

\[
 n=2q+2,\qquad n+1=2q+3,
\tag{3.6}
\]

one has

\[
 b_*=O(q^2 4^{-q}).
\tag{3.7}
\]

Indeed, \({N\choose q}\) is within a factor two of a largest binomial
coefficient of order \(N\), and a largest coefficient is at least
\(2^N/(N+1)\).  Since \(\log W\le k\log2\), (3.2) becomes

\[
 \boxed{\eta=O(q\sqrt{k}\,2^{-q}).}
\tag{3.8}
\]

In the central regime \(q=\Theta(\sqrt k)\), this is

\[
                         \eta=e^{-\Omega(q)}.
\tag{3.9}
\]

## 4. Owner-pair loads retain the exact orbit scale

For two distinct owners (A,B), let

\[
 L_{A,B}=\sum_j
 \Pr_{\sigma\in\Omega(T_j)}
 \bigl(A,B\in\mathcal D(C_j,T_j,\sigma)\bigr).
\tag{4.1}
\]

This is their weighted codegree under (1.6).  Put

\[
 \rho_*:=\max_{N\in\{N_j:j\in\mathcal J\}}
 \max_{A\ne B}\rho_N(A,B),
\tag{4.2}
\]

where the exact fixed-period orbit ratio is

\[
 \rho_N(A,B)=
 \begin{cases}
 \displaystyle
 \frac2{{R\choose\delta}{k-R\choose\delta}},
 &|A\cap B|=R-\delta,\quad1\le\delta<q,\\[3mm]
 \displaystyle
 \frac{N-2q+1}{{R\choose q}{k-R\choose q}},
 &|A\cap B|=c,\\[3mm]
 0,&\text{otherwise.}
 \end{cases}
\tag{4.3}
\]

These are the exact ratios from the carousel-orbit codegree theorem.

### Theorem 4.1 (simultaneous pair sparsity)

Under the hypotheses of Theorem 3.1, there is a deterministic shell
multiset for which (3.3) holds and, simultaneously,

\[
 \boxed{L_{A,B}\le\rho_*+\zeta
 \quad(A\ne B),}
\tag{4.4}
\]

where

\[
 \zeta=
 4\sqrt{b_*\rho_*\log(4W^2)}
 +4b_*\log(4W^2).
\tag{4.5}
\]

#### Proof

For a fixed pair, let (Y_j) be the (j)-th summand in (4.1).  A
uniform symmetric shell followed by a uniform cyclic order is the uniform
parameterized orbit of one period-\(N_j\) rail.  Therefore

\[
 \mathbb EY_j=\frac{N_j}{W}\rho_{N_j}(A,B).
\tag{4.6}
\]

By (2.4),

\[
 \sum_j\mathbb EY_j\le\rho_*.
\tag{4.7}
\]

Also \(0\le Y_j\le N_j/{N_j\choose q}\le b_*\), because occurrence of
both owners implies occurrence of either one.  Hence

\[
 \sum_j\operatorname {Var}Y_j
 \le b_*\sum_j\mathbb EY_j
 \le b_*\rho_*.
\tag{4.8}
\]

The standard one-sided Bernstein bound

\[
 \Pr\left(\sum_j(Y_j-\mathbb EY_j)>t\right)
 \le\exp\left(-\frac{t^2}
 {2(b_*\rho_*+b_*t/3)}\right)
\tag{4.9}
\]

with \(t=\zeta\) is at most \((4W^2)^{-2}\).  Union-bound this over fewer
than (W^2) ordered owner pairs, together with the owner events in
Theorem 3.1. \(\square\)

For central \(R\sim k/2\) and \(q=o(R)\), the maximum in (4.3) is the
distance-one value, so

\[
 \rho_*=\frac2{R(k-R)}=\Theta(k^{-2}).
\tag{4.10}
\]

Equations (3.7), (4.5), and \(\log W=O(k)\) give

\[
 \zeta=e^{-\Omega(q)}.
\tag{4.11}
\]

Thus the sampled multiple-choice ordering hypergraph has

\[
 \boxed{
 \begin{aligned}
  &\text{token load}=1,\\
  &\text{named-owner load}=1\pm e^{-\Omega(q)},\\
  &\text{owner--owner weighted codegree}=O(k^{-2}),\\
  &\text{token--owner weighted codegree}
    \le b_*=e^{-\Omega(q)},\\
  &\text{token--token weighted codegree}=0.
 \end{aligned}}
\tag{4.12}
\]

## 5. Relation to the complete-orbit owner hypergraph

If the shells are not frozen first, take as hyperedges all period-\(N\)
pure-rail owner decks on \({[k]\choose R}\), retaining parameterized
copies.  The carousel-orbit theorem gives an exactly regular
\(N\)-uniform hypergraph.  Weighting every incident edge by the reciprocal
degree is an **exact** named-owner fractional perfect matching, and

\[
 \frac{\Delta_2}{D}=\frac2{R(k-R)}=\Theta(k^{-2}).
\tag{5.1}
\]

For the shortest period \(N=2q+2=\Theta(\sqrt k)\), the elementary
growing-rank collision parameter is

\[
 \boxed{N^2\frac{\Delta_2}{D}=\Theta(k^{-1}).}
\tag{5.2}
\]

Equation (5.2) is favorable nibble geometry, but it is not by itself an
invocation of the classical Pippenger--Spencer theorem: its standard
quantifiers fix the uniformity before the degree/codegree limit.  A
diagonal quantitative nibble or a direct orbit-specific argument is still
needed here.

## 6. Exact boundary

The theorem proves that the named-order gate has no fractional or pairwise
pseudorandomness defect:

\[
 \boxed{
 \text{symmetric actual shells}
 \Longrightarrow
 \text{uniform named loads }1+e^{-\Omega(q)}
 \text{ and pair load }O(k^{-2}).}
\tag{6.1}
\]

It does not combine this with the exact ground-point equations

\[
 \sum_{j:x\in C_j}N_j+q|\{j:x\in T_j\}|=D.
\tag{6.2}
\]

The role-flow theorem proves (6.2), while the present independent-shell
argument proves (6.1).  A simultaneous construction must either preserve
the concentration estimates while conditioning/rounding the support
flow, or work directly in the complete orbit.

Nor does a near-perfect fractional point imply an integral one.  The
remaining positive semigroup gate is now precisely:

1. prove a growing-uniformity matching theorem applicable to the exact
   orbit in (5.1), preferably with a pseudorandom reserve; and
2. build a protected overlapping-core absorber which eliminates the
   resulting named-owner leave and the already-isolated insertion
   puncture.

This note proves no owner-disjoint integral factor, no bounded leave, and
no literal lower/upper/socket/common-cap compatibility.
