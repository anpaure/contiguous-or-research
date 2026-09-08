# Independent audit: Chamber-II period-residual incompatibility

**Date:** 2026-08-04

**Audited source:**
`MATH_THEOREM_CHAMBER_II_PERIOD_RESIDUAL_INCOMPATIBILITY_AND_COMPLETE_CLOSURE_20260804.md`

**Audited source SHA-256:**
`52ec7f4ac4dbe9f0a32e5eed063cf5bf8419c535575a631b16d8c98d31e40a68`

**Method:** fresh derivation from the two branches of `K`, followed by
independent exact-rational and coefficient-ledger checks.  No floating-point
evaluation, numerical search, or parameter sampling is used.

## 1. Verdict

**GO without correction.**  The normalization, compact slope bounds,
coefficient subtraction, and strict tail signs are all exact.  On the
residual band, shift stationarity forces the period derivative to be
strictly positive, so the simultaneous KKT locus is empty.  The cited
boundary theorem then gives strict long-wrap and Chamber-II positivity.

## 2. Re-derive `kappa`, `T`, and `mathcal R` from `K`

Write `A^2=pi/4`.  On the compact branch, for `0<=u<=1`,

\[
 K(Au)=1-e^{-A^2(1-u)^2}-e^{-A^2(1+u)^2}.
\]

Direct differentiation with respect to the physical argument gives

\[
 {K'(Au)\over2A}
 =(1+u)e^{-\pi(1+u)^2/4}
  -(1-u)e^{-\pi(1-u)^2/4}.
\]

Thus, with `h(z)=z exp(-pi z^2/4)`,

\[
                         \kappa(u)=h(1+u)-h(1-u).
\]

On the tail branch `K(Au)=-exp(-A^2(1+u)^2)`, so

\[
                         \kappa(u)=h(1+u)\qquad(u\ge1).
\]

The two expressions agree at `u=1` because `h(0)=0`.

Now set `P=A rho` and `w=A s`.  On the relevant strip
`0<=s<=1-rho`, the terms with `q=0,1` lie in the compact branch and all
terms with `q>=2` lie in the tail.  Hence, directly,

\[
 {F_{A\rho}'(As)\over2A}
 =\sum_{q\ge0}\kappa(q\rho+s)=T_\rho(s).
\]

For

\[
                         \Psi(\rho,x)=Q_{A\rho}(Ax),
\]

the chain rule gives

\[
 {\partial\Psi\over\partial x}
 =2A^2\{T_\rho(x)+2T_\rho(2x)\},
\tag{2.1}
\]

and

\[
 {\partial\Psi\over\partial\rho}
 =2A^2\sum_{q\ge1}q\{
 \kappa(q\rho)+\kappa(q\rho+x)+\kappa(q\rho+2x)\}.
\tag{2.2}
\]

The missing `q=0` term in (2.2) is correct because period differentiation
multiplies every row by `q`.  Equations (2.1)--(2.2) verify both
normalizations and every factor of two in the source.

## 3. Exact rational replay of `h'(6/5)<-2/5`

The derivative is

\[
 h'(z)=e^{-\pi z^2/4}\left(1-{\pi z^2\over2}\right).
\]

At `z=6/5`,

\[
 -h'(6/5)=e^{-9\pi/25}\left({18\pi\over25}-1\right).
\tag{3.1}
\]

The classical rational bounds

\[
                         {157\over50}<\pi<{22\over7}
\]

give

\[
 {18\pi\over25}-1-{5\over4}>{27\over2500}>0
\tag{3.2}
\]

and

\[
                         {9\pi\over25}<{198\over175}.
\tag{3.3}
\]

For `t=198/175`, let

\[
 S_8(t)=\sum_{k=0}^8{t^k\over k!},
 \qquad
 E_8(t)=S_8(t)+{t^9\over9!}{1\over1-t/10}.
\]

The positive exponential series gives `e^t<E_8(t)`.  Clearing positive
denominators yields the exact identity

\[
 {25\over8}-E_8(198/175)
 ={595314738904318276567
   \over23890990472412109375000}>0.
\tag{3.4}
\]

Therefore

\[
                         e^{-9\pi/25}>{8\over25}.
\]

Combining this with (3.2) proves from scratch

\[
                         -h'(6/5)>{8\over25}{5\over4}
 ={2\over5}.
\tag{3.5}
\]

The second endpoint sign is also exact:

\[
 h'(4/5)=e^{-4\pi/25}\left(1-{8\pi\over25}\right)<0,
\]

because

\[
                         {8\over25}{157\over50}-1
 ={3\over625}>0.
\tag{3.6}
\]

No decimal Gaussian estimate enters this certificate.

## 4. Independent audit of the two derivative domains

For `0<=t<=1`, compact differentiation gives

\[
 \kappa'(t)=h'(1+t)+h'(1-t),
 \qquad
 \kappa''(t)=h''(1+t)-h''(1-t).
\]

The independently audited reflected-curvature inequality says

\[
                         h''(1+t)\ge h''(1-t)
 \qquad(0\le t\le1/2).
\]

Thus `kappa'` is nondecreasing there.  Equations (3.5)--(3.6) give

\[
 \kappa'(1/5)=h'(6/5)+h'(4/5)<-{2\over5}.
\]

Consequently

\[
                         \kappa'(t)<-{2\over5}
 \qquad(0\le t\le1/5).
\tag{4.1}
\]

For `4/5<u<1`, one has

\[
                         \kappa'(u)=h'(1+u)+h'(1-u).
\]

The first term is negative: `1+u>9/5`, and
`pi(1+u)^2/2>(157/50)(81/25)/2>1`.  In the second,
`0<1-u<1/5`; both factors in

\[
 h'(z)=e^{-\pi z^2/4}(1-\pi z^2/2)
\]

are strictly below one, and the second remains positive because
`pi(1-u)^2/2<pi/50<1`.  Therefore

\[
                         \kappa'(u)<1.
\tag{4.2}
\]

On the residual domain,

\[
 {4\over5}<\rho<{11\over12},
 \qquad0<x<{1-\rho\over2},
\]

one has

\[
                         0<x<2x<1-\rho<1/5
\]

and

\[
                         [\rho,\rho+2x]\subset(4/5,1).
\]

Thus both derivative estimates are used only inside their proved domains.
Integration gives the strict inequalities

\[
 -\kappa(x)-2\kappa(2x)>2x
\tag{4.3}
\]

and

\[
 \kappa(\rho+2x)-\kappa(\rho)<2x.
\tag{4.4}
\]

Their difference is the strictly positive compact bracket in the theorem.

## 5. Fresh coefficient subtraction

Let

\[
 G=T_\rho(x)+2T_\rho(2x).
\]

Expand `mathcal R-G` before imposing stationarity.  The coefficient of each
family is:

\[
\begin{array}{c|ccc}
 &q=0&q=1&q\ge2\\ \hline
 \kappa(q\rho)&0&1&q\\
 \kappa(q\rho+x)&-1&0&q-1\\
 \kappa(q\rho+2x)&-2&-1&q-2.
\end{array}
\tag{5.1}
\]

For the last row, the coefficient at `q=2` is zero.  Hence on `G=0`,

\[
\begin{aligned}
 \mathcal R
={}&-\kappa(x)-2\kappa(2x)
       +\kappa(\rho)-\kappa(\rho+2x)\\
 &+\sum_{q\ge2}q\kappa(q\rho)
 +\sum_{q\ge2}(q-1)\kappa(q\rho+x)\\
 &+\sum_{q\ge3}(q-2)\kappa(q\rho+2x).
\end{aligned}
\tag{5.2}
\]

This independently reproduces every coefficient and lower summation limit
in the source.

For the first sum, `q>=2` gives `q rho>8/5>1`; for the second,
`q rho+x>1`; and for the third, `q>=3` gives `q rho+2x>1`.  On all three
tails,

\[
                         \kappa(v)=h(1+v)>0.
\]

All coefficients are nonnegative, and the first sum is nonempty with
strictly positive terms.  Equations (4.3)--(4.4) make the first line of
(5.2) strictly positive as well.  Therefore

\[
                         G=0\quad\Longrightarrow\quad
 \mathcal R>0.
\]

The strictness cannot be lost at an endpoint because the residual domain
has `x>0`, `rho>4/5`, and the first Gaussian tail is always present.

## 6. Global-minimum and scope audit

The full closed long-wrap parameter set is compact after adjoining the
already-signed degenerate boundary at `P=A`.  The corrected outer-period
theorem signs the ranges through `rho=4/5` and from `rho=11/12` onward.
The frozen Chamber-II theorem signs `x=0` and the upper `x` boundary.

If a nonpositive point existed, continuity would produce a nonpositive
minimum strictly inside the residual domain.  Its two free derivatives
would be zero, giving `G=0=mathcal R`, contrary to Section 5.  Thus the
long-wrap train is strictly positive everywhere.  The stationary-strip
elimination theorem then closes the complete Chamber-II polygon.

No Hessian determinant, curvature KKT row, or one-sided derivative sign is
needed for the contradiction.  The source correctly states that those
conditions are redundant, and it makes no claim about Chamber I or the
other six-slot branches.

## 7. Final audit conclusion

The theorem is proof-safe and requires no source correction.  Its decisive
step is an exact first-derivative comparison, not a numerical theta estimate:

\[
 -\kappa(x)-2\kappa(2x)
 >\kappa(\rho+2x)-\kappa(\rho).
\]

After exact coefficient subtraction, every remaining contribution to the
period residual has a nonnegative coefficient multiplying a strictly
positive Gaussian-tail kernel.
