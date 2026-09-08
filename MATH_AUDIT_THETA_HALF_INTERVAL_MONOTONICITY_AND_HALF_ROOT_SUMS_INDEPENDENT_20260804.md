# Independent audit: theta half-interval monotonicity and half-root sums

**Date:** 2026-08-04  
**Verdict:** **GO.**  The Fourier normalization, strict derivative bound,
sign at the quarter point, root-of-unity identities, odd and even
half-root sums, elementary exponential comparisons, and their exact
long-wrap boundary interpretation are all correct.  No numerical sampling,
finite census, or computational search is used in this audit.

## 1. Exact binding

The audited source is

`MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md`

with SHA-256

`f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3`.

The two scope dependencies used to check normalization and the final
geometric interpretation are:

| role | file | SHA-256 |
|---|---|---|
| exact Jacobi reflection formula | `MATH_THEOREM_FIVE_SLOT_REPEATED_GAP_EXACT_THETA_ENDPOINT_DESCENT_20260804.md` | `0bed69bf36b52abb5eab3022f2a06f3eabe7f05cdd299d232d9fd0a7b90094ff` |
| Euclidean long-wrap coordinates and residual block | `MATH_THEOREM_APERY_LONG_WRAP_EUCLIDEAN_SHIFT_AND_THETA_RESIDUAL_20260804.md` | `7540343eab8e110d950c7e19a6dea33aefc2e17a89f7c90b93966a4ed653b738` |

All three hashes agree with the current workspace bytes.

## 2. Fourier normalization

The Jacobi bank in the reflection theorem is

\[
 \Theta(t)=\sum_{j\in\mathbb Z}e^{-\pi(t-j)^2/4}.
\]

Poisson summation with Gaussian parameter `1/4` gives

\[
 \Theta(t)=2\sum_{\ell\in\mathbb Z}
                 e^{-4\pi\ell^2}e^{2\pi i\ell t}
 =2+4\sum_{\ell\ge1}e^{-4\pi\ell^2}
                         \cos(2\pi\ell t).
\]

Since the exact reflection error is `2-Theta(t)`, this reproduces

\[
 \rho(At)=-4\sum_{\ell\ge1}q_\ell\cos(2\pi\ell t),
 \qquad q_\ell=e^{-4\pi\ell^2}.
\]

Thus both the coefficient `-4` and exponent `-4 pi ell^2` in the source
are exact.  The derivative series is uniformly absolutely convergent,
because `sum ell*q_ell` converges, and termwise differentiation gives

\[
 {d\over dt}\rho(At)
 =8\pi\sum_{\ell\ge1}\ell q_\ell\sin(2\pi\ell t).
\]

There is no missing factor of `A`: the differentiation variable is the
dimensionless coordinate `t`, exactly as stated.

## 3. Strict half-interval monotonicity

For `0<theta<pi`, the identity

\[
 \sin(\ell\theta)=\sin\theta\,U_{\ell-1}(\cos\theta)
\]

and the standard bound `|U_(ell-1)(x)|<=ell` on `[-1,1]` prove

\[
                         |\sin(\ell\theta)|
                         \le\ell\sin\theta.
\]

Keeping the positive `ell=1` term and bounding every later term in the
adverse direction therefore gives precisely

\[
 {\rho'(At)\over8\pi}
 \ge\sin\theta\left(q_1-\sum_{\ell\ge2}\ell^2q_\ell\right),
 \qquad\theta=2\pi t.
\]

For `ell>=2`,

\[
 \ell^2-1\ge3(\ell-1),\qquad
 \ell^2\le4^{\ell-1}.
\]

Using `pi>3` and putting `j=ell-1` gives the strict estimate

\[
 {1\over q_1}\sum_{\ell\ge2}\ell^2q_\ell
 <\sum_{j\ge1}(4e^{-36})^j
 ={4e^{-36}\over1-4e^{-36}}<1.
\]

The last inequality needs only `e>2`: it gives
`4e^(-36)<4/2^36<1/2`.  Since `sin(theta)>0` on the open half interval,
the derivative is strictly positive there.

## 4. Quarter-point sign

At `t=1/4`, odd Fourier modes vanish and

\[
 \cos(\pi(2j)/2)=\cos(\pi j)=(-1)^j.
\]

Hence

\[
 \rho(A/4)=4\sum_{j\ge1}(-1)^{j+1}q_{2j}.
\]

The positive numbers `q_(2j)` decrease strictly to zero.  The alternating
series is therefore strictly positive.  Combined with strict
monotonicity, this proves `rho(At)>0` for every `1/4<=t<=1/2`, including
both endpoints claimed by the source.

## 5. Root-of-unity identity

For every positive integer `ell`,

\[
 \sum_{i=0}^{N-1}\cos(2\pi\ell i/N)
 =\begin{cases}N,&N\mid\ell,\\0,&N\nmid\ell.
 \end{cases}
\]

Absolute convergence permits interchanging this finite root sum with the
Fourier series.  It follows exactly that

\[
 \sum_{i=0}^{N-1}\rho(Ai/N)
 =-4N\sum_{j\ge1}q_{jN}=-4NQ_N.
\]

Also `rho(A(1-t))=rho(At)` and `rho(0)=-4Q`.

### Odd case

For `N=2m+1`, all nonzero roots pair under `i <-> N-i`, so

\[
 -4Q+2\sum_{i=1}^{m}\rho(Ai/N)=-4NQ_N.
\]

Thus

\[
 \sum_{i=1}^{m}\rho(Ai/N)=2Q-2NQ_N.
\]

### Even case

For `N=2m`, the second fixed point is `i=m`.  Since

\[
 \rho(A/2)=-4\sum_{\ell\ge1}(-1)^\ell q_\ell,
\]

one has

\[
 \rho(0)+\rho(A/2)=-8\sum_{j\ge1}q_{2j}.
\]

Pairing the other roots in the root-of-unity identity gives

\[
 \sum_{i=1}^{m-1}\rho(Ai/N)
 =4\sum_{j\ge1}q_{2j}-2NQ_N.
\]

Both displayed identities in the source are therefore exact.

## 6. Elementary positivity estimates

For every `N>=3`,

\[
 Q_N=\sum_{j\ge1}e^{-4\pi j^2N^2}
 \le\sum_{j\ge1}q_N^j={q_N\over1-q_N},
\]

because `j^2>=j`.  Also `q_N<1/2`.  In the odd range,

\[
 {Nq_N\over q_1}
 =N e^{-4\pi(N^2-1)}
 <N e^{-12(N^2-1)}<{1\over2}.
\]

For the final elementary inequality, `e>2` gives

\[
 e^{12(N^2-1)}>2^{12(N^2-1)}>2N
 \qquad(N\ge3).
\]

Consequently

\[
 NQ_N<{Nq_N\over1-q_N}<2Nq_N<q_1\le Q,
\]

which proves strict positivity in the odd identity.

For even `N>=4`, similarly

\[
 {Nq_N\over q_2}
 =N e^{-4\pi(N^2-4)}
 <N e^{-12(N^2-4)}<1.
\]

Again this follows from `e>2`, since
`2^(12(N^2-4))>N`.  Therefore

\[
 NQ_N<2Nq_N<2q_2
 \le2\sum_{j\ge1}q_{2j},
\]

and the even half-root sum is strictly positive.  These calculations
supply the omitted details behind the source's phrase “the same
elementary exponential comparison”; no stronger analytic estimate is
being assumed.

## 7. Exact long-wrap boundary interpretation

The Euclidean long-wrap theorem uses

\[
 {1\over x}=2m+\lambda,qquad
 n=h-1-m,qquad k=m-n,qquad0\le\lambda<2,
\]

and its theta residual is

\[
 R_h(x)=\rho(Ax)+\sum_{j=k}^{m-1}\rho(A(j+\lambda)x).
\]

The equality wall is `k+lambda=2`.  Since `k` is integral, its two
geometries are exactly `(k,lambda)=(1,1)` and `(2,0)`.

If `(k,lambda)=(1,1)`, then `x=1/(2m+1)` and

\[
 R_h(x)=\rho\left({A\over2m+1}\right)
       +\sum_{j=1}^{m-1}\rho\left({A(j+1)\over2m+1}\right)
 =\sum_{i=1}^{m}\rho\left({Ai\over2m+1}\right)>0.
\]

Here `h=2m` and the odd root grid has `N=h+1=2m+1`.

If `(k,lambda)=(2,0)`, then `x=1/(2m)` and

\[
 R_h(x)=\rho\left({A\over2m}\right)
       +\sum_{j=2}^{m-1}\rho\left({Aj\over2m}\right)
 =\sum_{i=1}^{m-1}\rho\left({Ai\over2m}\right)>0.
\]

Here `h=2m-1` and the even root grid has `N=h+1=2m`.  Thus the two sums in
the source are literally the complete residual blocks on the two
long-wrap equality faces, with no omitted endpoint, duplicate root, or
index shift.

## 8. Scope verdict

**GO:** the lemma proves strict monotonicity of the Jacobi reflection
error on the open half interval, positivity from the quarter point onward,
and exact positive theta residuals on the two Euclidean equality faces.

It does **not** prove positivity of an arbitrary fractional translate of
the Dirichlet block, the sufficient inequality `R_h(x)>=-1/40` in the
interior long-wrap chamber, the full long-wrap Bellman clock, any general
Bellman inequality, or an integral OR-word construction.
