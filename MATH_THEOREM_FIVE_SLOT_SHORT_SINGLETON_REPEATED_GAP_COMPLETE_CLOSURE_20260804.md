# Five-slot short-singleton repeated gap: complete closure

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves the complete
short-singleton repeated-gap train positive on its full honest domain.  The
proof keeps the complete first two period-derivative blocks; it uses no
finite search and no false reverse-monotonicity comparison for the
threshold-period train.

Put

\[
 A={\sqrt\pi\over2},\qquad
 \mathcal R(a,\beta)
 =\mathcal L_3(a+2\beta;a,a+\beta).
\tag{0.1}
\]

## Theorem

If

\[
 0\le a\le\beta,
 \qquad 2a+2\beta<A<2a+3\beta,
\tag{0.2}
\]

then

\[
                         \boxed{\mathcal R(a,\beta)>0.}
\tag{0.3}
\]

## 1. Repeated-gap coordinates

Write

\[
 y=a+\beta,\qquad b=\beta=y-a,
 \qquad u={a\over A},\qquad p={2y-a\over A}.
\tag{1.1}
\]

For fixed `y`, put

\[
 H_y(b)=\mathcal L_3(y+b;y-b,y).
\tag{1.2}
\]

Thus `H_y(beta)=mathcal R(a,beta)`.  The four normalized inequalities in
(0.2) are exactly

\[
 u\ge0,\qquad p\ge3u,\qquad p+u<1,
 \qquad 3p+u>2.
\tag{1.3}
\]

Indeed `p+u=2y/A`, the condition `a<=beta` is `p>=3u`, and
`(3p+u)/2=(3y-a)/A`.  In particular

\[
                         {3\over5}<p<1,
 \qquad 0\le u\le\min\{p/3,1-p\}.
\tag{1.4}
\]

The lower inequality `3p+u>2` will only be needed to ensure that the
first shifted derivative already lies on the Gaussian tail.

## 2. A compact derivative gate

Put

\[
 h(x)=x e^{-\pi x^2/4},
 \qquad D(x)=h(1+x)-h(1-x).
\tag{2.1}
\]

For `0<=x<=1`,

\[
 {K'(Ax)\over2A}=D(x),
\tag{2.2}
\]

whereas for `x>1`,

\[
 {K'(Ax)\over2A}=h(1+x)>0.
\tag{2.3}
\]

Termwise differentiation of (1.2) gives

\[
\begin{aligned}
 H_y'(b)={}&-K'(y-b)+K'(y+b)+K'(2y+b)\\
 &+\sum_{q\ge2}\bigl(
 qK'(q(y+b))+(q-1)K'(q(y+b)+y-b)\\
 &\hspace{42mm}+qK'(q(y+b)+y)\bigr).
\end{aligned}
\tag{2.4}
\]

Since `y/A=(p+u)/2`, retaining the complete `q=1,2` blocks and dropping
only positive `q>=3` tails yields

\[
 {H_y'(b)\over2A}>D(p)-D(u)+T(p,u),
\tag{2.5}
\]

where

\[
\begin{aligned}
T(p,u)={}&h\left(1+{3p+u\over2}\right)
 +2h(1+2p)+h(1+2p+u)\\
 &+2h\left(1+{5p+u\over2}\right).
\end{aligned}
\tag{2.6}
\]

The kernel is decreasing on `[0,2A/3]`.  Since `u<=1/4`, this gives
`D(u)<=0`.  It is therefore enough to prove

\[
                         J(p,u):=D(p)+T(p,u)>0.
\tag{2.7}
\]

All four arguments in (2.6) lie to the right of the maximum of `h`.
Consequently `J(p,u)` is decreasing in `u`.  Its smallest allowed value
at fixed `p` is attained at

\[
 u_*(p)=
 \begin{cases}
 p/3,&3/5\le p\le3/4,\\
 1-p,&3/4\le p\le1.
 \end{cases}
\tag{2.8}
\]

Define

\[
\begin{aligned}
 J_-(p)={}&D(p)+h(1+5p/3)+2h(1+2p)\\
          &+h(1+7p/3)+2h(1+8p/3),
                   &&3/5\le p\le3/4,\\
 J_+(p)={}&D(p)+h(3/2+p)+2h(1+2p)\\
          &+h(2+p)+2h(3/2+2p),
                   &&3/4\le p\le1.
\end{aligned}
\tag{2.9}
\]

Then `J(p,u)>=J_-(p)` on the first strip and
`J(p,u)>=J_+(p)` on the second.

## 3. Both strips have the same unique worst corner

We use

\[
 h''(x)={\pi\over2}x\left({\pi x^2\over2}-3\right)e^{-\pi x^2/4}.
\tag{3.1}
\]

On either interval in (2.9), `h''(1+p)>0` and
`h''(1-p)<=0`; hence

\[
                         D''(p)=h''(1+p)-h''(1-p)>0.
\tag{3.2}
\]

Every other argument in (2.9) is at least two, where `h''` is positive.
Thus

\[
                         J_-''(p)>0,
 \qquad J_+''(p)>0.
\tag{3.3}
\]

It remains to orient the two convex functions at their common endpoint.
Put

\[
 \rho=e^{-\pi/64},
 \qquad r_-={119\over125},
 \qquad r_+={497\over522}.
\tag{3.4}
\]

The elementary Taylor bounds already used for the four-slot period gate
give

\[
                         r_-<\rho<r_+.
\tag{3.5}
\]

For reference, if `x=q/4`, then

\[
 h'(q/4)=\rho^{q^2}\left(1-{\pi q^2\over32}\right).
\tag{3.6}
\]

The following three inequalities are exact rational certificates; after
multiplication by their positive denominators they are integer
inequalities:

\[
\begin{aligned}
 {497\over522}{29\over32}
<&{115\over32}r_-^{49}
 +{5\over3}{211\over32}r_-^{81}
 +4{67\over8}r_-^{100}\\
 &+{7\over3}{331\over32}r_-^{121}
 +{16\over3}{25\over2}r_-^{144},
\end{aligned}
\tag{3.7}
\]

\[
\begin{aligned}
 r_-{101\over112}
>&{427\over112}r_+^{49}
 +{779\over112}r_+^{81}
 +4{247\over28}r_+^{100}\\
 &+{1219\over112}r_+^{121}
 +4{92\over7}r_+^{144},
\end{aligned}
\tag{3.8}
\]

and

\[
 7r_-^{48}+9r_-^{80}+20r_-^{99}+11r_-^{120}>1.
\tag{3.9}
\]

Using `3<pi<22/7`, equations (3.5)--(3.7) in the literal derivative

\[
\begin{aligned}
 J_-'(3/4)={}&h'(1/4)+h'(7/4)
 +{5\over3}h'(9/4)+4h'(5/2)\\
 &+{7\over3}h'(11/4)+{16\over3}h'(3)
\end{aligned}
\tag{3.10}
\]

give

\[
                         J_-'(3/4)<0.
\tag{3.11}
\]

Similarly, (3.5), (3.6), and (3.8), applied to

\[
\begin{aligned}
 J_+'(3/4)={}&h'(1/4)+h'(7/4)+h'(9/4)
 +4h'(5/2)\\
 &+h'(11/4)+4h'(3),
\end{aligned}
\tag{3.12}
\]

give

\[
                         J_+'(3/4)>0.
\tag{3.13}
\]

Convexity now shows that `J_-` is decreasing up to `3/4`, while `J_+`
is increasing from `3/4`.  Their common minimum is

\[
\begin{aligned}
 J_-(3/4)=J_+(3/4)
 ={}&h(7/4)-h(1/4)+h(9/4)+2h(5/2)\\
 &+h(11/4)+2h(3).
\end{aligned}
\tag{3.14}
\]

Multiplying (3.14) by `4/rho`, inequality (3.9) gives, even after the
last positive term is discarded,

\[
 {4J_-(3/4)\over\rho}
 =-1+7\rho^{48}+9\rho^{80}+20\rho^{99}
       +11\rho^{120}+24\rho^{143}>0.
\tag{3.15}
\]

Therefore `J(p,u)>0` on the whole quadrilateral (1.3).  Equations
(2.5)--(2.7) prove

\[
                         \boxed{H_y'(b)>0.}
\tag{3.16}
\]

## 4. The two lower boundaries

The original domain in repeated-gap coordinates is

\[
 {A\over3}<y<{A\over2},
 \qquad b\ge y/2,\qquad b>A-2y,\qquad b\le y,
\tag{4.1}
\]

with equality permitted at `b=y/2` whenever `y>2A/5`.

### 4.1 The uniform boundary

If `y>=2A/5`, the lower boundary is `b=y/2`.  Put `s=y/2`.  Then

\[
\begin{aligned}
 H_y(y/2)
 &=\sum_{q\ge0}\{K(3qs)+K((3q+1)s)+K((3q+2)s)\}\\
 &=C(s)>0
\end{aligned}
\tag{4.2}
\]

by the all-ceiling theorem.

### 4.2 The threshold boundary

Let `A/3<y<=2A/5` and approach the lower boundary

\[
                         b=A-2y.
\tag{4.3}
\]

Set

\[
 v=A-2y,
 \qquad a=3y-A.
\tag{4.4}
\]

Then

\[
 0\le a\le v\le A/3,
 \qquad 2a+3v=A.
\tag{4.5}
\]

The exact compact quadrilateral reduction, followed by continuity at the
boundary, gives

\[
 H_y(A-2y)
 \ge C(A)+F_A(a)-F_A(v)-2\varepsilon,
\tag{4.6}
\]

where

\[
 \varepsilon=4\sum_{m\ge1}e^{-4\pi m^2}<{1\over20000}.
\tag{4.7}
\]

Every interior critical point of `F_A` on `[0,A/2]` is a strict local
maximum.  The valid endpoint consequence, since `0<=a<=v`, is

\[
                         F_A(a)\ge\min\{C(A),F_A(v)\}.
\tag{4.8}
\]

Also

\[
 C(A)>{43\over1000},
 \qquad F_A(v)<{61\over1000}\quad(0\le v\le2A/5).
\tag{4.9}
\]

If `F_A(v)<=C(A)`, (4.6) is at least
`C(A)-2epsilon`, which is strictly positive by (4.7) and (4.9).  If
`F_A(v)>C(A)`, it is greater than

\[
 2C(A)-F_A(v)-2\varepsilon
 >{86\over1000}-{61\over1000}-{1\over10000}
 ={249\over10000}>0.
\tag{4.10}
\]

Thus the threshold boundary is strictly positive as well.

## 5. Conclusion and scope

For each fixed `y`, (3.16) makes the train strictly increasing in its
repeated gap `b`.  Sections 4.1--4.2 prove its lower boundary positive.
Therefore (0.3) follows on the entire domain (0.2).

This closes only the short-singleton repeated-gap scalar `mathcal R`.
It does not assert positivity of the long-singleton scalar `mathcal P`,
the retained-pulse gate depending on `mathcal P`, arbitrary five-slot
tables, or the all-grid Bellman inequality.
