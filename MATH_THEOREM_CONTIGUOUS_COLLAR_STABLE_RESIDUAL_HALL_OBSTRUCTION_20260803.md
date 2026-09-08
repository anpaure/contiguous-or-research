# Contiguous-collar/stable-residual Hall obstruction

**Date:** 2026-08-03  
**Status:** unconditional rank-level obstruction and exact
Strassen/support-function reduction.  No computation is used.

## 0. Outcome

Put

\[
 k=2r,\qquad W={2r\choose r},\qquad
 b_j={{2r\choose r-j}\over W}\quad(1\le j<r),
\]

and let

\[
 d=\left({\sqrt\pi\over2}+o(1)\right)\sqrt r.
\]

Fix a constant

\[
 c>\sqrt{\log 2},\qquad a=\lceil c\sqrt r\rceil .
\]

An exact adjacent-rank collar ending at a rank-`r` owner has a length `L`
whose distribution is forced by the collar target counts:

\[
 \Pr(L\ge j)=b_j\qquad(1\le j\le a).                 \tag{0.1}
\]

Suppose a residual rank set `R` lies below the bottom of this collar, uses
at most `d+C-L` ranks for a fixed nonnegative integer constant `C`, and contains no two adjacent
ranks.  The last condition is weaker than requiring all residual ranks in
one atom to have one parity.

Then the residual rank marginals cannot be `b_j` up to `o(1)` total error.
In fact there is an absolute constant `eta=eta(c)>0` such that every such
law has residual rank-mass deficit at least

\[
 (\eta+o(1))\sqrt r.                                  \tag{0.2}
\]

For a named-target matching this is at least

\[
 (\eta+o(1))\sqrt r\,W                               \tag{0.3}
\]

uncovered residual targets.  In particular it is not `o(W)`.

Thus the macroscopic-collar extension proposed in
`MATH_THEOREM_MACROSCOPIC_COLLAR_PARITY_DECORRELATION_20260803.md` is false
when the collar is required to be a contiguous adjacent-rank chain and the
residual atom is parity-separated.  The obstruction is already rank-level;
labels, owner ordering and target codegrees cannot remove it.  A fixed
additive increase in owner capacity does not remove it either.

The proof also gives the exact Hall/Strassen criterion for every alternative
collar--residual coupling.

## 1. Why the collar-length law is forced

Partition the collar ranks

\[
 r-a,r-a+1,\ldots,r-1
\]

into adjacent-rank inclusion chains ending at distinct rank-`r` owners.
Let `L_T` be the number of strict-lower collar vertices on the chain ending
at owner `T`.

A chain contains a rank-`r-j` vertex if and only if `L_T\ge j`.  Since every
rank-`r-j` target occurs exactly once,

\[
 \#\{T:L_T\ge j\}={2r\choose r-j}=Wb_j.               \tag{1.1}
\]

Choosing an owner uniformly gives (0.1).  This argument does not assume a
symmetric or random collar construction: (0.1) is the empirical length law
of every exact adjacent-rank collar partition.

For later use, write

\[
 \mu_0=1-b_1,\qquad
 \mu_\ell=b_\ell-b_{\ell+1}\ (1\le\ell<a),\qquad
 \mu_a=b_a.                                             \tag{1.2}
\]

Then `mu_ell=Pr(L=ell)`.

## 2. Exact Strassen/support-function reduction

Let

\[
 J=\{a+1,a+2,\ldots,r-1\}
\]

be the finite residual distance set.  Regard `J` as
the vertex set of a path, so a stable subset contains no two consecutive
distances.  For a collar length `ell`, put

\[
 \mathcal S_\ell(C)=
 \{I\subseteq J:I\text{ is stable and }|I|\le d+C-\ell\}.       \tag{2.1}
\]

The polytope of residual marginal vectors compatible with the exact collar
law is

\[
 \mathcal P_C
 =\sum_{\ell=0}^a\mu_\ell
   \operatorname{conv}\{\mathbf1_I:I\in\mathcal S_\ell(C)\}.    \tag{2.2}
\]

If some `ell>d+C` has `mu_ell>0`, the pointwise capacity condition is
already impossible, so from now through this section assume that every
`ell` in the support of `mu` is at most `d+C`.  Here the sum is a weighted
Minkowski sum.  Formula (2.2) is exact: its
convex coefficients are precisely the conditional laws of `R` given
`L=ell`.

For a nonnegative weight vector `w=(w_j)_{j\in J}`, define

\[
 \alpha_h(w)=
 \max\left\{\sum_{j\in I}w_j:
 I\subseteq J\text{ stable},\ |I|\le h\right\}.         \tag{2.3}
\]

### Theorem 2.1 (exact stable-residual criterion)

A nonnegative residual marginal vector `q` belongs to `mathcal P_C` if and
only if

\[
 \sum_{j\in J}w_jq_j
 \le
 \sum_{\ell=0}^a\mu_\ell\alpha_{d+C-\ell}(w)            \tag{2.4}
\]

for every `w\ge0`.

### Proof

The support function of a Minkowski sum is the sum of the support functions,
which gives necessity.  Conversely, `mathcal P_C` is compact, convex and
downward closed in the nonnegative orthant.  If `q>=0` is outside it, choose
a separating functional `y`, and put `w=y_+`.  Downward closure gives

\[
 h_{\mathcal P_C}(y)=h_{\mathcal P_C}(y_+),
\]

because every coordinate carrying a negative coefficient can be set to zero
without leaving `mathcal P_C`; while `w\cdot q\ge y\cdot q`.  Hence the
nonnegative functional `w` still strictly separates `q` from
`mathcal P_C`, and violates (2.4).  This proves sufficiency. `square`

This is the exact finite Hall/Strassen min--max reduction.  The dynamic
program for `alpha_h` is irrelevant to the proof; no algorithmic assertion
is needed.

If the no-adjacent condition is deleted, (2.3) is the sum of the `h` largest
positive weights.  The criterion reduces to the expected-uniform-matroid
polymatroid inequalities

\[
 \sum_{j\in A}q_j
 \le \mathbb E\min(d+C-L,|A|)\qquad(A\subseteq J).       \tag{2.5}
\]

For decreasing `q_j`, it is enough to check initial residual segments.

If every atom must use one parity, replace (2.3) by the maximum of the two
cardinality-capped parity sums.  That is a still smaller polytope.  The
obstruction below applies already to the larger stable-set polytope.

## 3. One finite Hall row

Put

\[
 D_0=d+C,
\]

and choose an integer `t` such that

\[
 D_0-a<t<D_0,
 \qquad a+2t<r.                                         \tag{3.1}
\]

Consider the block of `2t` consecutive residual distances

\[
 A_t=\{a+1,a+2,\ldots,a+2t\}.                           \tag{3.2}
\]

Every stable subset of `A_t` has size at most `t`.  Pointwise,

\[
 |R\cap A_t|\le\min(t,D_0-L).                            \tag{3.3}
\]

Taking expectations and using (0.1),

\[
 \begin{aligned}
 \sum_{j=a+1}^{a+2t}q_j
 &\le \mathbb E\min(t,D_0-L)\\
 &=t-\mathbb E(L-(D_0-t))_+\\
 &=t-\sum_{j=D_0-t+1}^{a}b_j.                           \tag{3.4}
 \end{aligned}
\]

Consequently

\[
 \sum_{j=a+1}^{a+2t}(b_j-q_j)
 \ge
 \sum_{j=D_0-t+1}^{a+2t}b_j-t.                         \tag{3.5}
\]

This is one instance of (2.4), obtained by taking `w` to be the indicator
of `A_t`.  It is also valid for any single-parity residual law, since such a
rank set is stable.

## 4. The Hall row has macroscopic positive deficit

Set

\[
 \delta={\sqrt\pi\over2},\qquad
 t=\left\lfloor{d+C\over2}\right\rfloor.               \tag{4.1}
\]

Because `c>sqrt(log 2)>delta/2`, conditions (3.1) hold for all sufficiently
large `r` whenever `c\le delta`, unless `a>d+C`, in which case the
pointwise capacity is already impossible.  (This alternative can occur at
the boundary value `c=delta`; it is already a complete obstruction.)  Also

\[
 {d+C\over\sqrt r}\longrightarrow\delta,
 \qquad {a\over\sqrt r}\longrightarrow c.             \tag{4.2}
\]

The local central-binomial estimate, uniformly for `j=O(sqrt r)`, is

\[
 b_j=\exp(-j^2/r+o(1)).                                  \tag{4.3}
\]

Hence the right side of (3.5), divided by `sqrt r`, tends to

\[
 \eta(c)
 :=\int_{\delta/2}^{c+\delta}e^{-x^2}\,dx-\frac\delta2. \tag{4.4}
\]

### Lemma 4.1

For every `c\ge sqrt(log 2)`,

\[
 \eta(c)>0.                                              \tag{4.5}
\]

### Proof

The function is increasing in `c`, so it is enough to take
`c_0=sqrt(log 2)`.  Since `delta=int_0^infty e^{-x^2}dx`,

\[
 \eta(c_0)
 =\int_0^{\delta/2}(1-e^{-x^2})\,dx
  -\int_{c_0+\delta}^{\infty}e^{-x^2}\,dx.              \tag{4.6}
\]

The elementary inequalities

\[
 1-e^{-x^2}\ge x^2-{x^4\over2},
 \qquad
 \int_A^\infty e^{-x^2}dx\le {e^{-A^2}\over2A}         \tag{4.7}
\]

give

\[
 \eta(c_0)
 \ge {\delta^3\over24}-{\delta^5\over320}
      -{e^{-(c_0+\delta)^2}\over2(c_0+\delta)}>0.       \tag{4.8}
\]

For completeness, the last strict inequality follows already from the
standard certified bounds

\[
 0.88<\delta<0.887,qquad c_0>0.83,qquad
 e^{-2.924}<0.054:
\]

the first two terms in (4.8) exceed `0.0266`, while the final term is less
than `0.0158`. `square`

Combining (3.5)--(4.5),

\[
 \sum_{j=a+1}^{a+2t}(b_j-q_j)
 \ge (\eta(c)+o(1))\sqrt r.                             \tag{4.9}
\]

If `c>delta`, then `a>d+C` for all sufficiently large `r`,
while a positive fraction `b_a` of collar chains have length `a`.  The
pointwise capacity `L+|R|\le d+C` already fails.  Thus (4.9), together with
this trivial long-collar obstruction (including the possible `c=delta`
boundary subcase just noted), covers every fixed
`c>sqrt(log 2)`.

## 5. Translation to named-target leave

Suppose residual targets are used in a matching, so no named target occurs
more than once.  At distance `j`, there are `Wb_j` named targets and `Wq_j`
selected occurrences.  Therefore the number omitted in the block `A_t` is

\[
 W\sum_{j\in A_t}(b_j-q_j).
\]

Equation (4.9) proves the lower bound (0.3).  In particular, the leave is
not merely larger than `o(W)`; it is a positive fraction of the entire
`Theta(sqrt r W)` strict-lower mass.

The same conclusion holds for a weighted law whose named target degrees are
at most one, by summing the degree deficits rank by rank.

## 6. What the obstruction does and does not say

The obstruction uses exactly three properties:

1. the top collar is one contiguous adjacent-rank chain, forcing (0.1);
2. residual atoms have no adjacent selected ranks;
3. the total collar-plus-residual rank capacity is `d+O(1)` pointwise.

It does not use labels, literal intervals, upper coverage or topology.

There are therefore three possible escapes.

* **Decorrelate without a stable rank set.**  Adjacent residual ranks may
  occur, but their named-target realization must suppress codegrees by a
  different Boolean mechanism.
* **Abandon a contiguous collar.**  A fractional rank-matching construction
  may select an arbitrary collar subset with the correct individual
  marginals; this avoids the forced random capacity `d-L`, but it is not an
  adjacent-rank collar path.
* **Use growing, not bounded, extra capacity.**  A fixed additive constant
  does not alter the limit (4.4).  Any repair inside this exact architecture
  must change capacity or stability on a `Theta(sqrt r)` scale.

Thus the correct next Boolean-specific target is not the proposed
contiguous-collar plus parity-residual superposition.  It is a joint atom law
whose collision suppression is label-sensitive rather than enforced by
deleting every adjacent pair of residual ranks.
