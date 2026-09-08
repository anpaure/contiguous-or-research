# Five-slot three-efficient pure lattice: the `q=1,2` convex one-dimensional gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It rewrites the
period derivative of the sole residual pure lattice in exact compact
coordinates, retains the complete `q=1,2` derivative blocks, proves that
their possible adverse part is strictly convex in one coordinate, and
reduces a sufficient proof of strict period monotonicity to one explicit
one-variable inequality.  It does not sign that final inequality.

Put

\[
 A={\sqrt\pi\over2},\qquad c={\pi\over4},\qquad
 h(x)=x e^{-cx^2}.
\]

The remaining pure lattice is

\[
 \mathcal P(p,a)=\mathcal L_3(p;a,2a)
 =\sum_{q\ge0}\{K(qp)+K(qp+a)+K(qp+2a)\}
\tag{0.1}
\]

on

\[
 0<a<{A\over4},\qquad
 \max(3a,A-2a)<p<A-a.
\tag{0.2}
\]

## 1. Exact compact coordinates

Write

\[
 t={p\over A},\qquad \alpha={a\over A},\qquad
 r=1-t,qquad s=r-\alpha.
\tag{1.1}
\]

Then (0.2) is equivalent to

\[
 0<r<{2\over5},\qquad 0<s<{r\over2},\qquad
 s\ge {4r-1\over3}.
\tag{1.2}
\]

The weak lower inequality is allowed when the original face includes
`p=3a`; using the closed interval makes no difference to the limiting
argument.

Indeed, `p+a<A` gives `s>0`, while `p+2a>A` gives `s<r/2`.  Finally,
`p>=3a` is exactly `s>=(4r-1)/3`.  Feasibility of the last two
inequalities forces `r<2/5`.

For `0<=u<=1`, direct differentiation gives

\[
 {K'(Au)\over2A}=h(1+u)-h(1-u),
\tag{1.3}
\]

whereas for `u>1`,

\[
 {K'(Au)\over2A}=h(1+u)>0.
\tag{1.4}
\]

## 2. The complete first two derivative blocks

Define

\[
\begin{aligned}
 B(r,s)={}&h(2-r)-h(r)+h(2-s)-h(s)+h(2+r-2s)\\
 &+2h(3-2r)+2h(3-r-s)+2h(3-2s).
\end{aligned}
\tag{2.1}
\]

### Proposition 2.1

On (1.2),

\[
 {1\over2A}{\partial\over\partial p}\mathcal P(p,a)
 >B(r,s).
\tag{2.2}
\]

#### Proof

Termwise differentiation of the Gaussian tails gives

\[
 {\partial\over\partial p}\mathcal P(p,a)
 =\sum_{q\ge1}q\{K'(qp)+K'(qp+a)+K'(qp+2a)\}.
\tag{2.3}
\]

The three normalized `q=1` arguments are

\[
 1-r,\qquad1-s,\qquad1+r-2s.
\]

The first two lie below one and the last lies above one.  Applying
(1.3)--(1.4) gives the first line of (2.1).

The three normalized `q=2` arguments are

\[
 2-2r,\qquad2-r-s,\qquad2-2s,
\]

all greater than one.  Their coefficient two gives the second line of
(2.1).  Every argument with `q>=3` is greater than one, so every omitted
term is strictly positive.  This proves (2.2).  \(\square\)

Thus `B(r,s)>=0` on (1.2) would prove strict period monotonicity and close
the residual pure lattice by its already-positive lower-period boundary.

## 3. Strict convexity in the residual coordinate

### Proposition 3.1

For each fixed `r` in `(0,2/5)`, the function

\[
 s\longmapsto B(r,s)
\]

is strictly convex on the interval in (1.2).

#### Proof

Differentiating twice gives

\[
\begin{aligned}
 B_{ss}(r,s)={}&h''(2-s)-h''(s)
 +4h''(2+r-2s)\\
 &+2h''(3-r-s)+8h''(3-2s).
\end{aligned}
\tag{3.1}
\]

Here

\[
 h''(x)=2cx(2cx^2-3)e^{-cx^2}.
\tag{3.2}
\]

On (1.2), one has `0<s<1/5`, so `h''(s)<0`.  All four other
arguments in (3.1) are greater than `9/5`, hence greater than
`sqrt(6/pi)`; therefore their second derivatives are positive.  Every
term in (3.1) is strictly positive.  \(\square\)

The literal first derivative used to locate the unique minimum is

\[
\begin{aligned}
 B_s(r,s)={}&-h'(2-s)-h'(s)-2h'(2+r-2s)\\
 &-2h'(3-r-s)-4h'(3-2s).
\end{aligned}
\tag{3.3}
\]

## 4. Exact one-dimensional residual gate

Put

\[
 \ell(r)=\max\left(0,{4r-1\over3}\right),
 \qquad I_r=[\ell(r),r/2].
\tag{4.1}
\]

By Proposition 3.1 there is a unique clipped minimizer
`sigma(r) in I_r`, characterized without any optimization ambiguity by

\[
 \sigma(r)=
 \begin{cases}
  \ell(r),&B_s(r,\ell(r))\ge0,\\
  r/2,&B_s(r,r/2)\le0,\\
  \text{the unique }s\in(\ell(r),r/2)\text{ with }B_s(r,s)=0,
       &\text{otherwise}.
 \end{cases}
\tag{4.2}
\]

Define the one-variable lower envelope

\[
                         \Psi(r)=B(r,\sigma(r)).
\tag{4.3}
\]

### Corollary 4.1

The exact analytic inequality

\[
 \boxed{\Psi(r)\ge0\qquad(0<r<2/5)}
\tag{4.4}
\]

is sufficient to prove

\[
 {\partial\over\partial p}\mathcal P(p,a)>0
\]

throughout the residual domain (0.2).  Consequently (4.4), together with
the already-proved boundary value at `p=max(3a,A-2a)`, would prove
`mathcal P(p,a)>0` everywhere on that domain.

## 5. Scope

This reduction uses no finite enumeration and no discarded adverse
`q=1` term.  It retains the whole `q=1,2` derivative contribution and
drops only strictly positive `q>=3` tails.  The remaining issue is the
one-dimensional inequality (4.4); neither (4.4) nor full five-slot
positivity is claimed here.
