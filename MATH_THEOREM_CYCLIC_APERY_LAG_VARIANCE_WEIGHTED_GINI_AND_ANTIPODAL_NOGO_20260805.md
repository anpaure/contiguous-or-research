# Cyclic Apéry lag variance, weighted Gini, and the antipodal-product no-go

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional sharp reduction and exact counterexample.  Every
cyclic subadditive profile satisfies a lag-wise weighted-Gini variance
bound which is an equality for the unit sawtooth.  Replacing the lag Gini
factor by its worst possible value gives an attractive antipodal-product
bound, but the resulting proposed closure inequality is false already for
capped sawteeth.  The weighted-Gini inequality remains a valid possible
route to the all-period Apéry variance theorem.

## 1. Cyclic subadditive profiles as maximal-window walks

Let

\[
 e:\mathbb Z/g\mathbb Z\longrightarrow[0,\infty),
 \qquad e(0)=0,
\tag{1.1}
\]

be subadditive, and normalize `e(1)=1`.  Use representatives
`0,...,g-1`, put `e(g)=e(0)`, and define cyclic increments

\[
 \Delta_i=e(i)-e(i-1),\qquad1\le i\le g.
\tag{1.2}
\]

### Lemma 1.1 (simultaneous maximal-window characterization)

Subadditivity is equivalent to

\[
 \boxed{
  \sum_{t=i+1}^{i+j}\Delta_t
       \le \sum_{t=1}^{j}\Delta_t=e(j)
  \qquad(i,j\in\mathbb Z/g\mathbb Z),}
\tag{1.3}
\]

with cyclic index intervals.  Thus, for every length `j`, the increment
window starting at the distinguished origin has maximum sum among all
cyclic `j`-windows.  In addition,

\[
 \Delta_i\le1,qquad \sum_{i=1}^g\Delta_i=0.
\tag{1.4}
\]

#### Proof

The left side of (1.3) telescopes to `e(i+j)-e(i)`.  Hence (1.3) is
exactly `e(i+j)<=e(i)+e(j)`.  Taking `j=1` gives `Delta_(i+1)<=e(1)=1`,
and the cyclic telescoping sum is zero. \(\square\)

The condition is much stronger than the one-sided Lipschitz bound: one
common origin maximizes every cyclic window length simultaneously.

## 2. A sharp lag-wise variance bound

Write

\[
 \mu={1\over g}\sum_i e(i),
 \qquad
 G_j={1\over g}\sum_i|e(i+j)-e(i)|,
\tag{2.1}
\]

and

\[
 s_j=e(j)+e(-j).
\tag{2.2}
\]

### Theorem 2.1 (weighted cyclic Gini bound)

Every profile (1.1) satisfies

\[
 \boxed{
  \operatorname {Var}(e)
  \le {1\over4g}\sum_{j\in\mathbb Z/g\mathbb Z}s_jG_j.}
\tag{2.3}
\]

#### Proof

Fix `j` and let `I` be uniform on the cyclic group.  Put

\[
 X_j=e(I+j)-e(I).
\tag{2.4}
\]

Translation invariance gives `E X_j=0`.  Subadditivity in the two
directions gives

\[
 -e(-j)\le X_j\le e(j).
\tag{2.5}
\]

For any mean-zero random variable `X` in `[-a,b]`, write
`t=E X_+=E X_-`.  Then

\[
 E X^2
 \le bE X_+ + aE X_-
 =(a+b)t={a+b\over2}E|X|.
\tag{2.6}
\]

Apply (2.6) with `a=e(-j)`, `b=e(j)`.  It gives

\[
 {1\over g}\sum_i(e(i+j)-e(i))^2
 \le {s_jG_j\over2}.
\tag{2.7}
\]

Finally average over uniform `j`.  The pair `(I,I+j)` is uniform on two
independent group elements, so

\[
 {1\over g^2}\sum_{i,j}(e(i+j)-e(i))^2
 =2\operatorname {Var}(e).
\tag{2.8}
\]

Equations (2.7)--(2.8) give (2.3). \(\square\)

### Corollary 2.2 (antipodal product bound)

The weaker inequality

\[
 \boxed{
 2\operatorname {Var}(e)
 \le {1\over g}\sum_j e(j)e(-j)}
\tag{2.9}
\]

also holds.

#### Proof

The elementary interval bound `(X+a)(b-X)>=0`, averaged for a mean-zero
`X in[-a,b]`, gives `E X^2<=ab`.  Apply it to (2.4)--(2.5) and then use
(2.8). \(square\)

For the unit sawtooth `e(j)=j`, `0<=j<g`, every lag difference takes only
the two endpoint values `j` and `j-g`.  Therefore equality holds in both
(2.3) and (2.9), and

\[
 \operatorname {Var}(e)={g^2-1\over12}
 ={\mu(\mu+1)\over3}.
\tag{2.10}
\]

Thus (2.3) retains the conjectured extremizer exactly.

## 3. The antipodal closure is false

It would be sufficient, but is not valid, to try to prove

\[
 {1\over g}\sum_j e(j)e(-j)
 \le {2\over3}\mu(\mu+1).
\tag{3.1}
\]

### Theorem 3.1 (capped-sawtooth counterexample)

Let `M>=3`, `g>=2M`, and define

\[
 e_M(j)=\min\{j,M\},\qquad0\le j<g.
\tag{3.2}
\]

Then `e_M` is nonnegative, has true zero only at the origin, satisfies
`e_M(1)=1`, and is subadditive on `Z/gZ`.  Moreover

\[
 \mu_M=M-{M(M+1)\over2g},
\tag{3.3}
\]

and

\[
 {1\over g}\sum_j e_M(j)e_M(-j)
 =M^2\left(1-{M\over g}\right).
\tag{3.4}
\]

For every fixed `M>=3`, equation (3.1) fails for all sufficiently large
`g`.

#### Proof

If representatives `a,b` satisfy `a+b<g`, ordinary subadditivity of
`min(x,M)` on the nonnegative integers applies.  If `a+b>=g`, then
`c=a+b-g` obeys `c<=a,b`, so

\[
 e_M(c)\le e_M(a)\le e_M(a)+e_M(b).
\]

This proves cyclic subadditivity.

Summing the values `0,1,...,M-1` and the remaining `g-M` copies of `M`
gives (3.3).  For `1<=j<M`, the antipodal product is `jM`; the same terms
occur at the other end.  For `M<=j<=g-M`, the product is `M^2`.  Hence

\[
 \begin{aligned}
 \sum_j e_M(j)e_M(-j)
 &=2M\sum_{j=1}^{M-1}j+(g-2M+1)M^2\\
 &=gM^2-M^3,
 \end{aligned}
\]

which is (3.4).  As `g to infinity`, the two sides of (3.1) tend to
`M^2` and `(2/3)M(M+1)`.  The first is larger exactly when `M>2`.
\(\square\)

The failure is informative: (2.9) ignores how rarely a capped profile's
lag differences attain the extreme interval endpoints.  The factor `G_j`
in (2.3) prices that rarity and therefore cannot simply be discarded.

## 4. Sharpened all-period target

The cyclic Apéry variance conjecture would follow from the single weighted
Gini inequality

\[
 \boxed{
  \sum_j s_jG_j
  \le {4g\over3}\mu(\mu+1).}
\tag{4.1}
\]

Unlike the false antipodal closure, (4.1) is exact on the sawtooth and
automatically discounts long flat caps through their small lag Gini terms.
It is not proved here.

Equations (1.3) and (4.1) give a new formulation of the composite-period
frontier: prove a weighted cyclic-Gini inequality for a closed walk whose
distinguished prefix simultaneously maximizes every cyclic window sum.
This formulation contains no explicit Kneser stabilizer, although a proof
may still need the same subgroup structure.

This note does not prove the cyclic Apéry variance conjecture or formal
Rayleigh positivity.

## 5. Dependencies

1. elementary subadditivity on a finite cyclic group;
2. the phase-moment reduction in
   `MATH_THEOREM_RAYLEIGH_GENERAL_APERY_PHASE_MOMENTS_AND_VARIANCE_GATE_20260805.md`.
