# Five-slot long-singleton repeated-gap gate: closure for `a<=A/8`

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves the
long-singleton pulse-free gate positive on the full small-`a` subrange
`0<a<=A/8`.  It does not close the complementary range `A/8<a<A/4` or the
short-singleton gate.

Put

\[
 A={\sqrt\pi\over2},
 \qquad F(v)=F_A(v),
 \qquad C=F(0),
 \qquad
 \varepsilon=4\sum_{m\ge1}e^{-4\pi m^2}<{1\over20000}.
\tag{0.1}
\]

The long-singleton train is

\[
 \mathcal P(p,a)=\mathcal L_3(p;a,2a)
\tag{0.2}
\]

on

\[
 0<a<{A\over4},
 \qquad
 \max\{3a,A-2a\}<p<A-a.
\tag{0.3}
\]

## 1. Frozen threshold-period estimates

The audited quarter-shift estimates give

\[
 C>{43\over1000},
 \qquad
 F(A/4)>{44739\over1000000}>{43\over1000}.
\tag{1.1}
\]

Every interior critical point of `F` on `[0,A/4]` is a strict local
maximum.  Hence the minimum on this interval is attained at an endpoint,
and therefore

\[
                         \boxed{F(w)>{43\over1000}
                         \quad(0\le w\le A/4).}
\tag{1.2}
\]

The half-period estimate gives

\[
                         \boxed{F(w)<{64\over1000}
                         \quad(0\le w\le A/2).}
\tag{1.3}
\]

## 2. Uniform positive margin

### Theorem 2.1

If (0.3) holds and

\[
                         0<a\le {A\over8},
\tag{2.1}
\]

then

\[
                         \boxed{\mathcal P(p,a)>{9\over10000}.}
\tag{2.2}
\]

### Proof

Put

\[
                         t=A-p-a.
\tag{2.3}
\]

The exact domain gives `0<t<a` and `4a+t<A`.  Composite-endpoint descent
followed by reflection at `p=A-(a+t)` and `p+a=A-t` gives the proof-safe
bound

\[
 \mathcal P(p,a)
 >C+F(a)+F(2a)-F(t)-F(a+t)-2\varepsilon.
\tag{2.4}
\]

Under (2.1), all three positive shifts `a,2a` and both adverse shifts
`t,a+t` lie in `[0,A/4]`.  Equations (1.2)--(1.3) therefore give

\[
\begin{aligned}
 \mathcal P(p,a)
 &>3{43\over1000}-2{64\over1000}-{2\over20000}\\
 &= {9\over10000}>0.
\end{aligned}
\]

This proves the theorem. \(\square\)

## 3. Scope

The remaining long-singleton domain is

\[
 {A\over8}<a<{A\over4},
 \qquad
 \max\{3a,A-2a\}<p<A-a.
\]

The compact endpoint-descent lower bound is not expected to stay positive
all the way to its large-`a` corner; near that corner one must retain more
of the original subthreshold-period train.  No claim is made about that
range, the short-singleton gate, complete five-slot positivity, or an
OR-word upper bound.
