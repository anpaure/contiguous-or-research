# Long-wrap Apéry clocks: monotone theta quadrature closes every period

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves the sufficient
theta gate left open in
`MATH_THEOREM_APERY_LONG_WRAP_EUCLIDEAN_SHIFT_AND_THETA_RESIDUAL_20260804.md`
for every period, and hence closes the exact-first-carry one-defect long-wrap
family.  It does not prove general Bellman positivity or an OR-word upper
bound.

Put

\[
 A={\sqrt\pi\over2},\qquad
 g(t)=\rho(At)=-4\sum_{\ell\ge1}e^{-4\pi\ell^2}
                         \cos(2\pi\ell t).
\tag{0.1}
\]

The preceding Euclidean-shift theorem reduces the open narrow long-wrap
chamber

\[
 h\ge4,\qquad {1\over2(h-1)}<x<{1\over h+1}
\tag{0.2}
\]

to the residual

\[
 R_h(x)=g(x)+\sum_{j=k}^{m-1}g((j+\lambda)x),
\tag{0.3}
\]

where

\[
 {1\over x}=2m+\lambda,\qquad 0\le\lambda<2,
 \qquad n=h-1-m,\qquad k=m-n,
\tag{0.4}
\]

and proves

\[
 S_h(a)>{1\over40}+R_h(x),\qquad \Phi(W)\ge S_h(a).
\tag{0.5}
\]

It also proves

\[
 n\ge1,qquad k+\lambda>2.
\tag{0.6}
\]

The only unresolved sufficient gate there was

\[
                         R_h(x)\ge-{1\over40}.
\tag{0.7}
\]

The theorem below gives a much stronger uniform bound.

## Theorem 1 (all-period theta residual bound)

For every parameter tuple satisfying (0.2)--(0.6),

\[
 \boxed{
 R_h(x)>\rho(0)-\rho(A/2)>-{1\over10000}.}
\tag{1.1}
\]

Consequently

\[
 \boxed{
 S_h(a)>{249\over10000}>0,
 \qquad \Phi(W)>0.}
\tag{1.2}
\]

Thus the exact-first-carry long-wrap family is positive for every `h>=4`,
including every period above the former cutoff one thousand.

## 1. First-mode dominance makes the theta error increasing

The Fourier series in (0.1), and its differentiated series, converge
absolutely and uniformly.  Hence

\[
 g'(t)=8\pi\sum_{\ell\ge1}\ell e^{-4\pi\ell^2}
                                  \sin(2\pi\ell t).
\tag{1.3}
\]

For `0<theta<pi`,

\[
                         |\sin(\ell\theta)|
                         \le \ell\sin\theta.
\tag{1.4}
\]

Writing `q_ell=e^{-4 pi ell^2}` and taking
`theta=2 pi t`, equations (1.3)--(1.4) give, for `0<t<1/2`,

\[
 {g'(t)\over8\pi}
 \ge \sin(2\pi t)
       \left(q_1-\sum_{\ell\ge2}\ell^2q_\ell\right).
\tag{1.5}
\]

The bracket is strictly positive.  Indeed `pi>3`,
`ell^2-1>=3(ell-1)`, and `ell^2<=4^(ell-1)` for `ell>=2`, so

\[
 {1\over q_1}\sum_{\ell\ge2}\ell^2q_\ell
 <\sum_{r\ge1}4^r e^{-36r}<1.
\tag{1.6}
\]

Therefore

\[
                    \boxed{g'(t)>0\quad(0<t<1/2).}
\tag{1.7}
\]

Every cosine mode in (0.1) has zero integral on the half interval:

\[
 \int_0^{1/2}\cos(2\pi\ell t)\,dt=0.
\]

Absolute convergence permits termwise integration, giving

\[
                         \int_0^{1/2}g(t)\,dt=0.
\tag{1.8}
\]

In particular strict increase and (1.8) imply

\[
                         g(0)<0<g(1/2).
\tag{1.9}
\]

## 2. A zero-mean monotone tail lemma

### Lemma 2.1

Let `u` be increasing on `[0,b]` and satisfy
`integral_0^b u=0`.  Then

\[
                         I(s):=\int_s^b u(t)\,dt\ge0
                         \qquad(0\le s\le b).
\tag{2.1}
\]

#### Proof

If `u(s)>=0`, then `u(t)>=0` for `t>=s`, so `I(s)>=0`.  If
`u(s)<0`, then `u(t)<=u(s)<0` for `t<=s`; hence

\[
 I(s)=-\int_0^s u(t)\,dt>0.
\]

This proves (2.1). \(\square\)

The following right-endpoint quadrature consequence is the whole
large-period argument.  If

\[
                         0<d,\qquad d\le y,
 \qquad z=y+(N-1)d\le b,
\tag{2.2}
\]

then monotonicity gives

\[
 d\sum_{r=0}^{N-1}u(y+rd)
 \ge \int_{y-d}^{z}u(t)\,dt.
\tag{2.3}
\]

Using (2.1),

\[
 \int_{y-d}^{z}u
 =I(y-d)-I(z)
 \ge-I(z)
 \ge-(b-z)u(b).
\tag{2.4}
\]

The final inequality follows from `u(t)<=u(b)` on `[z,b]`.

## 3. Apply the quadrature to the Euclidean block

Set

\[
 y=(k+\lambda)x,
 \qquad
 z=(m-1+\lambda)x.
\tag{3.1}
\]

The sum in (0.3) is exactly the `n`-point block

\[
 \sum_{j=k}^{m-1}g((j+\lambda)x)
 =\sum_{r=0}^{n-1}g(y+rx).
\tag{3.2}
\]

All hypotheses of (2.2) hold with `u=g`, `b=1/2`, `d=x`, and
`N=n`.  Indeed, (0.6) gives

\[
                         y-x=(k+\lambda-1)x>0,
\tag{3.3}
\]

while (0.4) gives the exact terminal gap

\[
 {1\over2}-z
 =\left(m+{\lambda\over2}\right)x
  -(m-1+\lambda)x
 =\left(1-{\lambda\over2}\right)x.
\tag{3.4}
\]

Since `0<=lambda<2`,

\[
                         0<{1\over2}-z\le x.
\tag{3.5}
\]

Equations (2.3)--(2.4), (3.2), and (3.5) now give

\[
 x\sum_{j=k}^{m-1}g((j+\lambda)x)
 \ge-\left({1\over2}-z\right)g(1/2)
 \ge-xg(1/2),
\tag{3.6}
\]

where the last step uses `g(1/2)>0`.  Dividing by `x>0`,

\[
 \sum_{j=k}^{m-1}g((j+\lambda)x)\ge-g(1/2).
\tag{3.7}
\]

Thus

\[
 R_h(x)\ge g(x)-g(1/2)>g(0)-g(1/2),
\tag{3.8}
\]

the last inequality being strict because `x>0` and `g` is strictly
increasing.

The authenticated theta estimate used in the Euclidean-shift theorem is

\[
                         |\rho(w)|<{1\over20000}
                         \qquad(0\le w\le A).
\tag{3.9}
\]

Therefore

\[
 g(0)-g(1/2)>-{2\over20000}=-{1\over10000}.
\tag{3.10}
\]

This proves (1.1).  Finally (0.5) and (3.10) give

\[
 S_h(a)>{1\over40}-{1\over10000}
 ={249\over10000}>0.
\]

Since `Phi(W)>=S_h(a)`, equation (1.2) follows. \(\square\)

## 4. What was and was not used

The proof does not estimate a growing Dirichlet kernel term by term.
First-mode dominance is used once, to prove monotonicity of the complete
theta error `g`.  Zero mean on `[0,1/2]` then converts the entire shifted
block into a right-endpoint quadrature of a nonnegative tail integral.

No period enumeration, solver, numerical search, or computer-assisted
inequality is used.  The result closes only the exact-first-carry
one-defect long-wrap branch supplied by the cited Euclidean reduction.  It
does not close multi-defect Apéry clocks, finite shoulders in the original
Bellman history, integral Boolean chainization, upper-shadow construction,
residence, or common-cap routing.

## 5. Frozen dependency

| role | file | SHA-256 |
|---|---|---|
| Euclidean shifted-block reduction, compact margin, and theta estimate | `MATH_THEOREM_APERY_LONG_WRAP_EUCLIDEAN_SHIFT_AND_THETA_RESIDUAL_20260804.md` | `7540343eab8e110d950c7e19a6dea33aefc2e17a89f7c90b93966a4ed653b738` |

The monotonicity and zero-mean argument is reproduced in full above; it
does not rely on an unaudited auxiliary lemma.
