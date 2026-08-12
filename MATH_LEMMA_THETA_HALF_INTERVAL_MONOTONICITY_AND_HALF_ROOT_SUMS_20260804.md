# Jacobi reflection error: half-interval monotonicity and positive half-root sums

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical lemma.  It supplies two exact
Fourier facts useful for the large-period long-wrap gate.  It does not by
itself sign an arbitrary shifted Dirichlet block or a Bellman clock.

Put

\[
 q_\ell=e^{-4\pi\ell^2},
 \qquad
 \rho(At)=-4\sum_{\ell\ge1}q_\ell\cos(2\pi\ell t),
 \qquad A={\sqrt\pi\over2}.
\tag{0.1}
\]

Thus `rho` is the exact Jacobi reflection error

\[
                         F_A(w)+F_A(A-w)=\rho(w).
\]

## 1. Strict monotonicity on the half interval

### Theorem 1.1

The function

\[
                         t\longmapsto\rho(At)
\]

is strictly increasing on `0<t<1/2`.

Moreover,

\[
                         \rho(At)>0
                         \qquad(1/4\le t\le1/2).
\tag{1.0}
\]

### Proof

Termwise differentiation is justified by absolute uniform convergence and
gives

\[
 {d\over dt}\rho(At)
 =8\pi\sum_{\ell\ge1}\ell q_\ell\sin(2\pi\ell t).
\tag{1.1}
\]

For `0<theta<pi`, the elementary Chebyshev bound

\[
                         |\sin(\ell\theta)|
                         \le\ell\sin\theta
\tag{1.2}
\]

holds for every positive integer `ell`.  Hence, with `theta=2 pi t`,

\[
 {1\over8\pi}{d\over dt}\rho(At)
 \ge \sin\theta\left(q_1-
               \sum_{\ell\ge2}\ell^2q_\ell\right).
\tag{1.3}
\]

The bracket is positive.  Indeed `pi>3`,
`ell^2-1>=3(ell-1)` for `ell>=2`, and
`ell^2<=4^(ell-1)` give

\[
 {1\over q_1}\sum_{\ell\ge2}\ell^2q_\ell
 <\sum_{j\ge1}4^j e^{-36j}
 ={4e^{-36}\over1-4e^{-36}}<1.
\tag{1.4}
\]

The last inequality follows already from `e>2`.  Since `sin theta>0`,
(1.3)--(1.4) prove the strict derivative sign.

For the additional sign, direct substitution gives

\[
 \rho(A/4)
 =4\sum_{j\ge1}(-1)^{j+1}q_{2j}>0,
\tag{1.5}
\]

because the terms `q_(2j)` decrease strictly.  Monotonicity proves (1.0).
\(\square\)

## 2. Exact half-root sums

For an integer `N>=3`, put

\[
                         Q_N=\sum_{j\ge1}q_{jN},
 \qquad                  Q=\sum_{\ell\ge1}q_\ell.
\tag{2.1}
\]

The root-of-unity identity gives

\[
 \sum_{i=0}^{N-1}\rho\left({Ai\over N}\right)
 =-4NQ_N.
\tag{2.2}
\]

### Theorem 2.1 (odd half-root sum)

If `N=2m+1>=3`, then

\[
 \boxed{
 \sum_{i=1}^{m}\rho\left({Ai\over N}\right)
 =2Q-2NQ_N>0.}
\tag{2.3}
\]

### Proof

The symmetry `rho(A(1-t))=rho(At)` and `rho(0)=-4Q` turn (2.2) into

\[
 -4Q+2\sum_{i=1}^{m}\rho(Ai/N)=-4NQ_N,
\]

which is the identity in (2.3).

For positivity, `Q>=q_1`, while

\[
 Q_N\le{q_N\over1-q_N}
\tag{2.4}
\]

because `(jN)^2>=jN^2`.  For `N>=3`, `pi>3` and `e>2` give

\[
 {Nq_N\over q_1}< {1\over2},
 \qquad q_N<{1\over2}.
\]

Together with (2.4), these strict estimates give `NQ_N<Q`.  Hence the
right side of (2.3) is positive.  \(\square\)

### Theorem 2.2 (even half-root sum)

If `N=2m>=4`, then

\[
 \boxed{
 \sum_{i=1}^{m-1}\rho\left({Ai\over N}\right)
 =4\sum_{j\ge1}q_{2j}-2NQ_N>0.}
\tag{2.5}
\]

### Proof

At the second fixed point,

\[
 \rho(A/2)=-4\sum_{\ell\ge1}(-1)^\ell q_\ell.
\]

Therefore

\[
 \rho(0)+\rho(A/2)
 =-8\sum_{j\ge1}q_{2j}.
\]

Using symmetry in (2.2) proves the identity (2.5).

Now `sum_(j>=1)q_(2j)>=q_2`, and (2.4) remains valid.  For `N>=4`, the
same elementary exponential comparison gives

\[
                         NQ_N<2q_2.
\]

Substitution in (2.5) proves strict positivity.  \(\square\)

## 3. Long-wrap boundary interpretation

The two equality geometries adjacent to the Euclidean long-wrap chamber
are exactly these half-root sums:

* `(k,lambda)=(1,1)` gives the odd grid

  \[
  \sum_{i=1}^{m}\rho\left({Ai\over2m+1}\right)>0;
  \]

* `(k,lambda)=(2,0)` gives the even grid

  \[
  \sum_{i=1}^{m-1}\rho\left({Ai\over2m}\right)>0.
  \]

Thus the degeneration of the first Fourier-mode margin at either boundary
is not an adverse case: the complete theta block is strictly positive
there.  Extending this positivity through every fractional translate is a
separate Dirichlet-block theorem and is not asserted here.

## 4. Scope

The lemma is exact and all-period.  It replaces neither the full shifted
block inequality `R_h(x)>=-1/40` nor the literal integral construction.  Its
role is to provide strict monotonicity of the reflection error and exact
positive anchors for the two Euclidean root-grid faces.
