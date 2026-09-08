# Independent audit: all-period long-wrap monotone quadrature closure

**Date:** 2026-08-04  
**Verdict:** **GO.**  The residual rewrite, Euclidean geometry, monotone
right-endpoint quadrature, zero-half-mean tail sign, endpoint sign,
uniform theta margin, and all-period scope are correct.  No patch to the
source is required, and no numerical search or finite period enumeration is
used in this audit.

## 1. Exact binding

Audited source:

`MATH_THEOREM_APERY_LONG_WRAP_MONOTONE_QUADRATURE_ALL_PERIOD_CLOSURE_20260804.md`

SHA-256:

`24f440d2b516618f7798b5f4e053de0f5b3253ad1825e7685e2494bddacf8ecd`.

Its sole frozen dependency is

`MATH_THEOREM_APERY_LONG_WRAP_EUCLIDEAN_SHIFT_AND_THETA_RESIDUAL_20260804.md`

with SHA-256

`7540343eab8e110d950c7e19a6dea33aefc2e17a89f7c90b93966a4ed653b738`.

Both hashes agree with the current workspace bytes.

## 2. Residual and Fourier normalization

The dependency defines

\[
 {1\over x}=2m+\lambda,\qquad0\le\lambda<2,
 \qquad n=h-1-m,\qquad k=m-n,
\]

and proves, on the remaining narrow long-wrap chamber,

\[
 R_h(x)=\rho(Ax)+\sum_{j=k}^{m-1}\rho(A(j+\lambda)x),
\]

with `n>=1`, `k+lambda>2`, and

\[
 S_h(a)>{1\over40}+R_h(x),\qquad \Phi(W)\ge S_h(a).
\]

Writing `g(t)=rho(At)` therefore gives exactly the source's unscaled
residual

\[
 R_h(x)=g(x)+\sum_{j=k}^{m-1}g((j+\lambda)x).
\]

There is no missing factor of `A`, since every argument of `g` is the
dimensionless phase multiplying `A`.

The exact Fourier series

\[
 g(t)=-4\sum_{\ell\ge1}e^{-4\pi\ell^2}\cos(2\pi\ell t)
\]

is the Jacobi reflection error with the correct coefficient and exponent.
Absolute uniform convergence, also after one differentiation, gives

\[
 g'(t)=8\pi\sum_{\ell\ge1}\ell e^{-4\pi\ell^2}
                                   \sin(2\pi\ell t).
\]

## 3. Strict monotonicity and the endpoint sign

For `0<theta<pi`,

\[
 |\sin(\ell\theta)|\le\ell\sin\theta.
\]

Thus, with `q_ell=e^(-4 pi ell^2)`,

\[
 {g'(t)\over8\pi}
 \ge\sin(2\pi t)
 \left(q_1-\sum_{\ell\ge2}\ell^2q_\ell\right).
\]

For `ell>=2`, the exact estimates

\[
 \ell^2-1\ge3(\ell-1),\qquad
 \ell^2\le4^{\ell-1},\qquad \pi>3
\]

give

\[
 {1\over q_1}\sum_{\ell\ge2}\ell^2q_\ell
 <\sum_{r\ge1}(4e^{-36})^r<1.
\]

Hence `g'(t)>0` on `0<t<1/2`.

Termwise integration is justified by absolute convergence, and every
Fourier mode has zero half-period integral:

\[
 \int_0^{1/2}\cos(2\pi\ell t)\,dt=0.
\]

Therefore

\[
                         \int_0^{1/2}g(t)\,dt=0.
\]

A strictly increasing continuous function with zero integral cannot have
`g(1/2)<=0`, since it would then be strictly negative before the endpoint.
Likewise it cannot have `g(0)>=0`.  Thus

\[
                         g(0)<0<g(1/2),
\]

exactly as required for the terminal quadrature estimate.

## 4. Zero-mean terminal-integral lemma

Let `u` be increasing on `[0,b]` with zero integral and define

\[
 I(s)=\int_s^b u(t)\,dt.
\]

If `u(s)>=0`, monotonicity makes the integrand nonnegative on `[s,b]`.
If `u(s)<0`, then `u(t)<=u(s)<0` for `t<=s`, and zero total mean gives

\[
 I(s)=-\int_0^s u(t)\,dt>0.
\]

Hence `I(s)>=0` for every `s`.

For a right-endpoint grid

\[
 y,y+d,\ldots,z=y+(N-1)d,
 \qquad0<d\le y,\qquad z\le b,
\]

monotonicity on each interval
`[y+(r-1)d,y+rd]` gives

\[
 d\sum_{r=0}^{N-1}u(y+rd)
 \ge\int_{y-d}^{z}u(t)\,dt.
\]

The right side equals `I(y-d)-I(z)`, so

\[
 \int_{y-d}^{z}u\ge-I(z).
\]

Finally `u(t)<=u(b)` on `[z,b]`, giving

\[
 I(z)\le(b-z)u(b).
\]

Every inequality direction in the source's quadrature lemma is therefore
correct.

## 5. Euclidean block geometry

Set

\[
 y=(k+\lambda)x,
 \qquad z=(m-1+\lambda)x.
\]

The index range `j=k,...,m-1` has exactly

\[
 m-k=m-(m-n)=n
\]

terms, and hence

\[
 \sum_{j=k}^{m-1}g((j+\lambda)x)
 =\sum_{r=0}^{n-1}g(y+rx).
\]

The left quadrature endpoint is legal because

\[
 y-x=(k+\lambda-1)x>0
\]

by `k+lambda>2`.  From `1/x=2m+lambda`,

\[
\begin{aligned}
 {1\over2}-z
 &=\left(m+{\lambda\over2}\right)x
   -(m-1+\lambda)x\\
 &=\left(1-{\lambda\over2}\right)x.
\end{aligned}
\]

Since `0<=lambda<2`, this terminal gap is strictly positive and at most
one mesh:

\[
                         0<{1\over2}-z\le x.
\]

Thus all hypotheses of the quadrature lemma hold with
`u=g`, `b=1/2`, `d=x`, and `N=n`.

## 6. Uniform residual bound

The quadrature lemma and the terminal-gap identity give

\[
 x\sum_{j=k}^{m-1}g((j+\lambda)x)
 \ge-\left({1\over2}-z\right)g(1/2).
\]

Because `g(1/2)>0` and the terminal gap is at most `x`,

\[
 \sum_{j=k}^{m-1}g((j+\lambda)x)\ge-g(1/2).
\]

Therefore

\[
 R_h(x)\ge g(x)-g(1/2)>g(0)-g(1/2),
\]

where the final inequality is strict because `x>0` and `g` is strictly
increasing.

The dependency supplies the strict uniform theta estimate

\[
                         |\rho(w)|<{1\over20000}
                         \qquad(0\le w\le A).
\]

Since `g(0)=rho(0)` and `g(1/2)=rho(A/2)`, it follows that

\[
 g(0)-g(1/2)>-{2\over20000}=-{1\over10000}.
\]

Combining this with the frozen compact margin gives the exact arithmetic

\[
 S_h(a)>{1\over40}-{1\over10000}
 ={250-1\over10000}={249\over10000}>0.
\]

Since `Phi(W)>=S_h(a)`, the literal long-wrap functional is strictly
positive.

## 7. All-period scope

The source closes the complete **narrow exact-first-carry one-defect
long-wrap chamber** (the only part passed into the Euclidean residual) for
every `h>=4`, with no former cutoff at one thousand.  Together with the
already-proved broad subrange, this closes every exact-first-carry
one-defect long-wrap clock.

It does not address multi-defect Apéry words, a finite shoulder separating
an original Bellman clock from its formal periodic clock, threshold
overshoot, later first crossing, arbitrary Bellman positivity, or any
integral carrier/common-cap construction.

## 8. Verdict

**GO:** every identity and inequality in the all-period monotone
quadrature closure is correctly directed and exactly scoped.
