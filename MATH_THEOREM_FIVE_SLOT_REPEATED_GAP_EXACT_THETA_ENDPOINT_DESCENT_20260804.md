# Five-slot repeated-gap trains: exact theta endpoint-descent gates

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It strengthens the
coarse compact quadrilateral bounds by retaining the exact phase-dependent
Jacobi reflection errors.  It does not prove either remaining gate positive.

Put

\[
 A={\sqrt\pi\over2},
 \qquad F(v)=F_A(v),
 \qquad C=F(0),
\tag{0.1}
\]

and define

\[
 \Theta(t)=\sum_{j\in\mathbb Z}e^{-\pi(t-j)^2/4},
 \qquad
 \rho(w)=2-\Theta(w/A).
\tag{0.2}
\]

Poisson summation gives the exact Fourier form

\[
 \rho(w)
 =-4\sum_{m\ge1}e^{-4\pi m^2}
          \cos\left({2\pi m w\over A}\right),
 \qquad
 |\rho(w)|\le\varepsilon,
\tag{0.3}
\]

where

\[
 \varepsilon=4\sum_{m\ge1}e^{-4\pi m^2}<{1\over20000}.
\tag{0.4}
\]

## 1. Exact reflection identity

### Lemma 1.1

For every `0<=w<=A`,

\[
                         \boxed{F(w)+F(A-w)=\rho(w).}
\tag{1.1}
\]

### Proof

Write `w=At`.  The exact half-train completion is

\[
 F(At)=1-\Theta(t)+e^{-\pi t^2/4}
       +\sum_{j\ge2}e^{-\pi(j-t)^2/4}.
\]

Apply the same identity at `1-t`.  Since
`Theta(1-t)=Theta(t)`, the two displayed positive Gaussian banks together
contain exactly one copy of every term of `Theta(t)`.  Their sum is
therefore `Theta(t)`, and the two train values add to `2-Theta(t)`.
This is (1.1). \(\square\)

## 2. Exact short-singleton gate

For

\[
 \mathcal R(a,\beta)=\mathcal L_3(a+2\beta;a,a+\beta)
\]

put

\[
 y=a+\beta,
 \qquad v=A-2y,
 \qquad u=v+a.
\tag{2.1}
\]

The exact domain is

\[
 0<v<{A\over3},
 \qquad 0\le a\le{A-v\over4},
 \qquad 2a+3v<A.
\tag{2.2}
\]

Define

\[
\boxed{
 \widetilde Q_R(a,v)
 =C+F(a)+F\!\left({A-v\over2}\right)
  -F(v)-F(v+a)+\rho(v)+\rho(v+a).}
\tag{2.3}
\]

### Theorem 2.1

On (2.2),

\[
                         \boxed{\mathcal R(a,\beta)
                         \ge\widetilde Q_R(a,v).}
\tag{2.4}
\]

### Proof

The exact clock begins

\[
 0,a,y,2y-a,2y,3y-a,
\]

with the first five values below `A` and the sixth above it.  The
composite-endpoint descent lemma gives

\[
 \mathcal R(a,\beta)
 \ge C+F(a)+F(y)+F(2y-a)+F(2y).
\]

Now `2y-a=A-(v+a)` and `2y=A-v`.  Apply (1.1) to both reflected pairs and
use `y=(A-v)/2`.  This gives (2.4). \(\square\)

## 3. Exact long-singleton gate

For

\[
 \mathcal P(p,a)=\mathcal L_3(p;a,2a)
\]

put

\[
                         t=A-p-a.
\tag{3.1}
\]

The unresolved interior has

\[
 0<t<a<{A\over4},
 \qquad 4a+t<A.
\tag{3.2}
\]

Define

\[
\boxed{
 \widetilde Q_P(a,t)
 =C+F(a)+F(2a)-F(t)-F(a+t)
  +\rho(t)+\rho(a+t).}
\tag{3.3}
\]

### Theorem 3.1

On (3.2),

\[
                         \boxed{\mathcal P(p,a)
                         \ge\widetilde Q_P(a,t).}
\tag{3.4}
\]

### Proof

The exact clock begins

\[
 0,a,2a,p,p+a,p+2a,
\]

with its first five values below `A` and its sixth above it.  Endpoint
descent gives

\[
 \mathcal P(p,a)
 \ge C+F(a)+F(2a)+F(p)+F(p+a).
\]

Since `p=A-(a+t)` and `p+a=A-t`, two applications of (1.1) give
(3.4). \(\square\)

## 4. Exact threshold-period-relaxation boundary

The gates (2.3) and (3.3) retain the exact reflection phase after the
second endpoint-descent step replaces the composite period `E=V_5` by
`A`; no uniform reflection error is discarded after that replacement.
They nevertheless do not close the full domains.  At the common limiting
uniform clock

\[
 a=\beta=A/4
 \qquad\hbox{or}\qquad
 (p,a)=(3A/4,A/4),
\]

the actual train is the positive arithmetic clock `C(A/4)`.  The first
descent with its true composite period `E=5A/4` is still exact and positive,
but the subsequent threshold-period relaxation from `F_E` to `F_A` has
strictly negative Fourier coefficients.  Thus the remaining large-`a`
proof must retain either the true composite period or the original
period-three phase (for example through the `q=1,2` period derivative),
rather than replacing every train period by `A`.

The small-`a` subrange `0<a<=A/8` of `mathcal P` is separately positive by
the coarse compact estimate.  This note makes no claim about the remaining
large-`a` range, the full short-singleton gate, complete five-slot
positivity, or an OR-word upper bound.
