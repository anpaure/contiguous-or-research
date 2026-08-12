# Self-audit: all-period long-wrap monotone quadrature closure

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_APERY_LONG_WRAP_MONOTONE_QUADRATURE_ALL_PERIOD_CLOSURE_20260804.md`  
**Target SHA-256:**
`24f440d2b516618f7798b5f4e053de0f5b3253ad1825e7685e2494bddacf8ecd`  
**Verdict:** **PASS / GO in the stated exact-first-carry long-wrap scope.**

This is a proof audit, not an independent authorship audit.  No enumeration,
solver, numerical search, Python, or H100 computation was used.

## 1. Imported reduction and parameter domain

The dependency hash in the theorem agrees byte-for-byte with the audited
Euclidean-shift source:

`MATH_THEOREM_APERY_LONG_WRAP_EUCLIDEAN_SHIFT_AND_THETA_RESIDUAL_20260804.md`,
SHA-256
`7540343eab8e110d950c7e19a6dea33aefc2e17a89f7c90b93966a4ed653b738`.

That source proves, on the open narrow chamber,

\[
 R_h(x)=g(x)+\sum_{j=k}^{m-1}g((j+\lambda)x),
 \quad
 {1\over x}=2m+\lambda,quad0\le\lambda<2,
\]

\[
 n=m-k\ge1,qquad k+\lambda>2,
\]

and

\[
 S_h(a)>{1\over40}+R_h(x),qquad \Phi(W)\ge S_h(a).
\]

Thus the new proof is entitled to work only with the displayed theta block.
It does not silently replace a necessary condition by a sufficient one.

## 2. Monotonicity audit

Uniform absolute convergence of

\[
 -4\sum_{\ell\ge1}e^{-4\pi\ell^2}\cos(2\pi\ell t)
\]

and its differentiated series follows immediately from Gaussian decay.
For `0<t<1/2`, put `theta=2 pi t`.  The standard inequality

\[
 |\sin(\ell\theta)|\le\ell\sin\theta
 \qquad(0<\theta<\pi)
\]

gives

\[
 {g'(t)\over8\pi}
 \ge\sin\theta\left(q_1-\sum_{\ell\ge2}\ell^2q_\ell\right).
\]

The elementary tail estimate is correctly directed:

\[
 {\ell^2q_\ell\over q_1}
 =\ell^2e^{-4\pi(\ell^2-1)}
 <4^{\ell-1}e^{-36(\ell-1)}.
\]

Its geometric sum is less than one, so the derivative is strictly positive.

Each Fourier mode integrates to zero on `[0,1/2]`; therefore

\[
 \int_0^{1/2}g=0.
\]

A strictly increasing continuous zero-mean function must have
`g(0)<0<g(1/2)`.  The theorem uses no stronger sign assertion.

## 3. Monotone-tail lemma audit

For an increasing zero-mean function `u` on `[0,b]`,

\[
 I(s)=\int_s^b u=-\int_0^s u\ge0.
\]

If `u(s)<0`, the right expression is positive; if `u(s)>=0`, the original
tail integral is nonnegative.  Thus the proof covers both possible locations
of the unique zero.

For grid points `y,y+d,...,z`, the intervals

\[
 [y-d,y],[y,y+d],\ldots,[z-d,z]
\]

partition `[y-d,z]`.  Since the sample is at each interval's right endpoint,
monotonicity gives

\[
 d\sum u(y+rd)\ge\int_{y-d}^{z}u.
\]

The tail decomposition

\[
 \int_{y-d}^{z}u=I(y-d)-I(z)
 \ge-I(z)\ge-(b-z)u(b)
\]

has the correct inequality directions.  The last step uses
`u(t)<=u(b)`.

## 4. Euclidean endpoint algebra audit

With

\[
 y=(k+\lambda)x,qquad z=(m-1+\lambda)x,
\]

the block contains exactly `n=m-k` points.  Its left integration endpoint
is legal because

\[
 y-x=(k+\lambda-1)x>0.
\]

The terminal gap is exactly

\[
 {1\over2}-z
 =\left(1-{\lambda\over2}\right)x.
\]

Since `0<=lambda<2`, this lies in `(0,x]`.  Hence the complete block obeys

\[
 \sum_{j=k}^{m-1}g((j+\lambda)x)\ge-g(1/2).
\]

There is no hidden factor `n`, `x`, or endpoint cell: the factor `x` from
the Riemann sum cancels after the terminal gap is bounded by `x`.

Adding the singleton theta term gives

\[
 R_h(x)\ge g(x)-g(1/2)>g(0)-g(1/2).
\]

The authenticated bound `|rho(w)|<1/20000` at both `w=0` and `w=A/2`
then yields

\[
 R_h(x)>-{1\over10000}.
\]

Finally

\[
 {1\over40}-{1\over10000}
 ={250-1\over10000}={249\over10000}>0.
\]

All strict and weak inequalities are sufficient for strict positivity.

## 5. Scope audit

The theorem closes every period in the open narrow exact-first-carry
long-wrap chamber.  The complementary endpoint and broad subrange were
already handled by the dependency chain.  It does not close:

* multi-defect Apéry clocks;
* a negative finite shoulder between an original history and its formal clock;
* arbitrary Bellman rows;
* integral chainization or Euler fusion;
* upper shadows, residence, or the literal common-cap router.

Subject to that scope, the proof is complete.
