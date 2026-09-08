# Independent audit: contiguous-collar/stable-residual Hall obstruction

**Date:** 2026-08-03  
**Audited theorem:**
`MATH_THEOREM_CONTIGUOUS_COLLAR_STABLE_RESIDUAL_HALL_OBSTRUCTION_20260803.md`  
**Audited theorem SHA-256:**
`be18baddafdc79d2aeec4b17b7001d44ac6d6834f6a3c3cc80e29a60161022bb`  
**Verdict:** **GO after three exact scope/proof-hygiene repairs.**

No finite search or numerical solver was used.  This audit independently
rederives the empirical collar law, the support-function criterion, the
finite Hall row, its Gaussian limit and the named-target consequence.

## 1. Exact audited scope

The result concerns only the following architecture in even dimension
`k=2r`.

1. The top ranks at distances `1,...,a` are partitioned into **contiguous
   adjacent-rank inclusion chains**, with one chain (possibly empty) rooted
   at each rank-`r` owner.
2. Conditional on a collar length `L`, the residual distance set lies in
   `J={a+1,...,r-1}`, is stable in the path on `J` (no adjacent distances),
   and has pointwise size at most `d+C-L`.
3. `C` is fixed while `r` tends to infinity.

It does not exclude a noncontiguous collar, a residual atom containing
adjacent ranks, a label-sensitive collision suppressor, or an architecture
with growing extra capacity.  It is therefore an obstruction to the stated
collar/stable-residual route, not to `B(k)+O(1)` itself.

## 2. Repairs made during audit

Three corrections were applied directly to the theorem.

* The residual distance set was written as the infinite-looking
  `{a+1,a+2,...}` despite being called finite.  It is now exactly
  `J={a+1,...,r-1}`; distance `r` is the excluded empty target.
* If `Pr(L>d+C)>0`, the conditional residual family has negative capacity
  and no law exists.  This immediate infeasible branch is now separated
  before the weighted Minkowski sum is formed.
* At `c=delta=sqrt(pi)/2`, rounding can still give `a>d+C`; that boundary
  subcase is now explicitly assigned to the same immediate capacity
  obstruction as the `c>delta` branch.

These repairs do not change any inequality, asymptotic constant or stated
conclusion.

## 3. Forced empirical collar-length law

Let `L_T` be the number of strict-lower vertices in the collar chain rooted
at owner `T`; assign `L_T=0` to an empty owner chain.  A contiguous
adjacent-rank chain contains a rank-`r-j` vertex exactly when `L_T>=j`.
Exact coverage of that rank therefore forces

\[
 \#\{T:L_T\ge j\}={2r\choose r-j}=Wb_j.
\]

Dividing by the `W` owners gives

\[
 \Pr(L\ge j)=b_j,
\]

independently of symmetry, randomness or the labels of the collar chains.
Taking successive tail differences yields

\[
 \mu_0=1-b_1,
 \quad \mu_\ell=b_\ell-b_{\ell+1}\ (1\le\ell<a),
 \quad \mu_a=b_a.
\]

Thus the collar-length law used later is forced, not selected.

## 4. Weighted Minkowski sum and support criterion

For a feasible collar length `ell`, the conditional marginal polytope is

\[
 P_\ell=operatorname{conv}{\mathbf1_I:
 I\subseteq J\text{ stable},\ |I|\le d+C-\ell\}.
\]

A joint law with the forced `L` marginal is exactly a choice of one
conditional law for every `ell`, hence its residual marginal lies in

\[
 \mathcal P_C=\sum_{\ell=0}^a\mu_\ell P_\ell.
\]

This proves both inclusions in the claimed weighted-Minkowski description.
For `w>=0`, its support function is

\[
 h_{\mathcal P_C}(w)
 =\sum_{\ell=0}^a\mu_\ell
   \max_{I\text{ stable},\ |I|\le d+C-\ell}
   \sum_{j\in I}w_j.
\]

The converse separation step is also valid.  Every `P_ell`, and therefore
`mathcal P_C`, is compact, convex and downward closed in the nonnegative
orthant.  If `q>=0` is separated by `y`, then deleting the coordinates on
which `y` is negative shows

\[
 h_{\mathcal P_C}(y)=h_{\mathcal P_C}(y_+),
 \qquad y_+\cdot q\ge y\cdot q.
\]

So a nonnegative separator exists.  This verifies the exact iff criterion
in Theorem 2.1; it is not merely a necessary Hall row.

## 5. The finite block row

Put `D_0=d+C` and

\[
 A_t=\{a+1,\ldots,a+2t\}.
\]

For

\[
 D_0-a<t<D_0,\qquad a+2t<r,
\]

the maximum stable-set size of `A_t` is exactly `t`.  Hence every residual
atom obeys

\[
 |R\cap A_t|\le\min(t,D_0-L).
\]

The infeasible event `L>D_0` has already been excluded.  For integral
`u=D_0-t`, the tail-sum identity gives

\[
 \mathbb E(L-u)_+
 =\sum_{j=u+1}^a\Pr(L\ge j)
 =\sum_{j=D_0-t+1}^a b_j.
\]

Therefore

\[
 \sum_{j=a+1}^{a+2t}q_j
 \le t-\sum_{j=D_0-t+1}^a b_j,
\]

and subtraction from the desired block mass gives exactly

\[
 \sum_{j=a+1}^{a+2t}(b_j-q_j)
 \ge \sum_{j=D_0-t+1}^{a+2t}b_j-t.
\]

This is the indicator-weight instance of the full support criterion.

## 6. Fixed `C`, Gaussian limit and positivity

Take

\[
 \delta={\sqrt\pi\over2},
 \qquad t=\left\lfloor{d+C\over2}\right\rfloor.
\]

Because fixed `C` disappears after division by `sqrt(r)`, while
`d/sqrt(r)->delta`, the lower and upper endpoints of the sum in the last
display converge respectively to `delta/2` and `c+delta`.  The conditions
on `t` hold whenever `c>delta/2` and the pointwise capacity is feasible;
`a+2t<r` is automatic because its left side is `O(sqrt(r))`.

The exact product

\[
 b_j=\prod_{i=0}^{j-1}{r-i\over r+i+1}
\]

has, uniformly for `j=O(sqrt(r))`,

\[
 \log b_j=-{j^2\over r}+O(r^{-1/2}),
\]

so the sum is a Riemann sum and

\[
 {1\over\sqrt r}
 \left(\sum_{j=D_0-t+1}^{a+2t}b_j-t\right)
 \longrightarrow
 \eta(c):=
 \int_{\delta/2}^{c+\delta}e^{-x^2}\,dx-{\delta\over2}.
\]

The positivity proof is rigorous.  At `c_0=sqrt(log 2)`, using
`delta=int_0^infty e^{-x^2}dx`,

\[
 \eta(c_0)
 =\int_0^{\delta/2}(1-e^{-x^2})\,dx
  -\int_{c_0+\delta}^{\infty}e^{-x^2}\,dx.
\]

The bounds

\[
 1-e^{-x^2}\ge x^2-{x^4\over2},
 \qquad
 \int_A^\infty e^{-x^2}dx\le{e^{-A^2}\over2A}
\]

give the positive lower bound

\[
 {\delta^3\over24}-{\delta^5\over320}
 -{e^{-(c_0+\delta)^2}\over2(c_0+\delta)}>0.
\]

The certified coarse estimates in the theorem leave a margin greater than
`0.010`; since `eta(c)` is increasing, positivity follows for every
`c>=sqrt(log 2)`.

If `c>delta`, then `a>d+C` eventually, while
`Pr(L=a)=b_a=e^{-c^2+o(1)}` is bounded away from zero, so the pointwise
capacity itself is impossible.  The same conclusion handles a rounded
`c=delta` instance with `a>d+C`.  Otherwise the Hall-row limit applies.

## 7. Named-target leave

The residual marginal `q_j` is per owner, so across `W` owners the selected
occurrence mass at distance `j` is `Wq_j`.  There are exactly `Wb_j` named
targets at that rank.  If named-target degree is at most one, the omitted
mass in `A_t` is therefore

\[
 W\sum_{j\in A_t}(b_j-q_j).
\]

The Hall row gives

\[
 (\eta(c)+o(1))\sqrt r\,W.
\]

This is a literal named-target deficit, not merely a failure of a symmetric
rank law.  It is `Omega(sqrt(r)W)`, hence in particular cannot be `o(W)`.
The same summation applies to fractional named-target degrees bounded by
one.

## 8. Final assessment

All requested rows survive audit:

* the empirical collar-length law is forced exactly;
* the weighted Minkowski/support-function criterion is an iff statement;
* one finite stable-block Hall row yields the claimed deficit;
* fixed additive `C` vanishes in the Gaussian scaling;
* `eta(c)` is strictly positive throughout the stated range;
* the `c>delta` case is even more strongly pointwise infeasible;
* rank-mass deficit converts exactly to named-target leave under the stated
  degree-at-most-one hypothesis.

The theorem is therefore safe to cite with its stated restricted scope.
