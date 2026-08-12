# Complementary-pair trains and the exact scalar gate for the two inert h=4 faces

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem and exact reduction.  It
proves a uniform three-train complementary-pair lemma on the full shift
range needed by the two inert five-slot size-four-efficient faces.  It then
retains every period gain and reduces the remaining simultaneous two-pair
problem to one explicit scalar envelope.  It does **not** prove that final
envelope positive.

Put

\[
A={\sqrt\pi\over2},
\qquad
F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
\qquad
C(\tau)=F_\tau(0).
\tag{0.1}
\]

For the threshold-period train write simply `F=F_A` and `C=C(A)`.  We use
the proved rational bounds

\[
C>{57\over1400},
\qquad
F(A/4)<{293\over6000},
\tag{0.2}
\]

\[
F(w)>0\quad(0\le w\le A/2),
\tag{0.3}
\]

and the reflection estimate

\[
F(w)+F(A-w)>-\varepsilon,
\qquad
\varepsilon={1\over20000}.
\tag{0.4}
\]

Every interior critical point of `F` on `[0,A/2]` is a strict maximum,
and `F` is decreasing on `[A/4,A/2]`.  Since the two endpoint values on
`[0,A/4]` satisfy

\[
F(0)>{57\over1400},
\qquad
F(A/4)>{33\over800}>{57\over1400},
\]

the critical-point statement sharpens the usual small-shift lower bound to

\[
                         F(w)>{57\over1400}
                         \qquad(0\le w\le A/4).
\tag{0.5}

## 1. A uniform complementary/subcomplementary pair lemma

### Theorem 1.1

Let

\[
A\le\tau\le{5A\over4},
\qquad
0\le y\le{A\over2},
\qquad
0\le z\le{3A\over4},
\qquad
y+z\le\tau.
\tag{1.1}
\]

Then

\[
                         \boxed{
C(\tau)+F_\tau(y)+F_\tau(z)>0.}
\tag{1.2}
\]

Thus one ceiling train pays for every complementary or subcomplementary
pair in the exact h=4 `y,z` range.

### Proof

For every fixed `w<A`, increasing the period only removes negative Gaussian
tail mass, so

\[
F_\tau(w)\ge F(w),
\qquad C(\tau)\ge C.
\tag{1.3}
\]

If `z<=A/2`, all three terms on the left of (1.2) are positive by
(0.2)--(0.3).  Hence take `z>A/2` and put

\[
                         v=A-z.
\tag{1.4}
\]

The upper bound on `z` gives

\[
                         A/4\le v<A/2.
\tag{1.5}
\]

Reflection and (1.3) give

\[
C(\tau)+F_\tau(y)+F_\tau(z)
>C(\tau)+F(y)-F(v)-\varepsilon.
\tag{1.6}

Suppose first that `y<=v`.  If `y>=A/4`, monotone decrease on
`[A/4,A/2]` gives `F(y)>=F(v)`, so (1.6) is larger than
`C-epsilon>0`.  If `y<A/4`, equations (0.2), (0.5), and monotone decrease
give

\[
\begin{aligned}
C(\tau)+F_\tau(y)+F_\tau(z)
&>2{57\over1400}-{293\over6000}-{1\over20000}\\
&={13669\over420000}>0.
\end{aligned}
\tag{1.7}

It remains to take `y>v` and write

\[
                         s=y-v.
\tag{1.8}

Since `y+z=A+s<=tau`, period monotonicity gives
`C(tau)>=C(A+s)`.  Also `0<s<=A/4` by (1.1) and (1.5).  Therefore (1.6)
improves to

\[
C(\tau)+F_\tau(y)+F_\tau(z)
>C(A+s)+F(v+s)-F(v)-\varepsilon.
\tag{1.9}

#### Short displacement: `0<s<=A/24`

On `[A/4,A/2]`, differentiation of the train gives

\[
-F'(t)
<2(A-t)e^{-(A-t)^2}.
\tag{1.10}

Here `A-t` lies in `[A/2,3A/4]`, on which
`w exp(-w^2)` is increasing; indeed `3A/4<1/sqrt(2)` follows from
`pi<22/7<32/9`.  Hence

\[
F(v)-F(v+s)
<{\pi\over64}e^{-9\pi/64}<{1\over30}.
\tag{1.11}

For the last rational bound, use `pi<22/7` and
`exp(9pi/64)>3/2`; the latter follows already from
`pi>3` and the quadratic Taylor polynomial for the exponential.  Equations
(0.2), (1.9), and (1.11) give

\[
C(\tau)+F_\tau(y)+F_\tau(z)
>{57\over1400}-{1\over30}-{1\over20000}
={3079\over420000}>0.
\tag{1.12}

#### Long displacement: `A/24<=s<=A/4`

The ceiling train is increasing in its period, and

\[
                         C(25A/24)>{49\over1000}.
\tag{1.13}

Here is an exact certificate.  Write

\[
M=1-2e^{-\pi/4},
\qquad
R(\tau)=\sum_{q\ge1}e^{-(A+q\tau)^2},
\qquad
C(\tau)=M-R(\tau).
\]

The degree-six positive Taylor sum at `333/424<pi/4` proves

\[
e^{\pi/4}>{125\over57},
\qquad M>{11\over125}.
\tag{1.14}

At `tau=25A/24`, the first exponent is larger than

\[
{2401\over2304}{333\over106}={88837\over27136},
\]

and its degree-eight positive Taylor sum is larger than `64000/2457`.
Successive exponents differ by more than

\[
{3075\over576}{333\over424}={113775\over27136},
\]

whose degree-eight positive Taylor sum exceeds `64`.  Thus

\[
R(25A/24)
<{2457\over64000}\,{1\over1-1/64}
={39\over1000}.
\tag{1.15}

Equations (1.14)--(1.15) prove (1.13).  Since `F(v+s)>0` and
`F(v)<293/6000`, equation (1.9) now gives

\[
C(\tau)+F_\tau(y)+F_\tau(z)
>{49\over1000}-{293\over6000}-{1\over20000}
={7\over60000}>0.
\tag{1.16}

All cases are exhausted. \(\square\)

## 2. Exact two-pair coordinates on the inert faces

Take a size-four-efficient boundary table

\[
                         (0,x,y,z,P,\tau)
\tag{2.1}

on either inert face

\[
\tau=P+x\ge\max(A,y+z)
\quad\hbox{or}\quad
\tau=y+z\ge\max(A,P+x).
\tag{2.2}

Put

\[
u=A-P,
\qquad v=A-z,
\qquad\delta=\tau-A.
\tag{2.3}

Then

\[
0\le u\le A/5,
\qquad
0\le\delta\le A/4-{5u\over4},
\tag{2.4}

and

\[
x-u\le\delta,
\qquad
y-v\le\delta,
\qquad
\max\{x-u,y-v\}=\delta.
\tag{2.5}

The last equality simply says that one of the two complementary sums is
the active endpoint.  The remaining literal constraints imply

\[
\begin{gathered}
0\le x\le(A-u)/4,
\qquad2x\le y\le(A-u)/2,\\
v\ge x+u,
\qquad
v\ge A/4+3u/4,
\qquad
v\le A-x-y.
\end{gathered}
\tag{2.6}

For `delta>=0`, define the exact period gain

\[
D_\delta(w)
=F_{A+\delta}(w)-F_A(w)
=\sum_{q\ge1}
\left(
e^{-(A+qA+w)^2}
-e^{-(A+q(A+\delta)+w)^2}
\right)
\ge0,
\tag{2.7}

and the exact reflected-pair loss

\[
G_\delta(a,b)
=F_A(a)-F_A(b)+D_\delta(a)+D_\delta(A-b).
\tag{2.8}

Finally put

\[
\Theta(b)=F_A(b)+F_A(A-b),
\qquad |\Theta(b)|<\varepsilon.
\tag{2.9}

### Theorem 2.1 (exact two-pair identity)

The five-residue endpoint train on either inert face is exactly

\[
\boxed{
\begin{aligned}
\mathscr B_{A+\delta}(x,y,z,P)
={}&C(A)+D_\delta(0)\\
&+G_\delta(x,u)+G_\delta(y,v)\\
&+\Theta(u)+\Theta(v).
\end{aligned}}
\tag{2.10}

#### Proof

For any pair `a,A-b`, equations (2.7)--(2.9) give the literal identity

\[
F_{A+\delta}(a)+F_{A+\delta}(A-b)
=G_\delta(a,b)+\Theta(b).
\]

Apply this first to `(a,b)=(x,u)`, for which `A-u=P`, and then to
`(a,b)=(y,v)`, for which `A-v=z`.  Also
`C(A+delta)=C(A)+D_delta(0)`. \(\square\)

## 3. The weakest uniform pair gate left by the reduction

Let `D_delta` be the compact polytope defined by (2.4)--(2.6) together
with (2.5), and define the joint pair envelope

\[
\Gamma(\delta)
=\inf_{(u,x,y,v)\in\mathcal D_\delta}
\bigl(G_\delta(x,u)+G_\delta(y,v)\bigr).
\tag{3.1}

### Corollary 3.1 (sharp scalar boundary)

Both inert h=4 faces are positive if

\[
\boxed{
C(A)+D_\delta(0)+\Gamma(\delta)>2\varepsilon
\qquad(0\le\delta\le A/4).
}
\tag{3.2}

Conversely, any inert-face table whose endpoint-period lower bound is
nonpositive must violate (3.2) at its own value of `delta`, with the exact
theta terms in (2.10).  Thus (3.2) is the weakest uniform two-pair
inequality after replacing the two exponentially tiny theta terms only by
their common absolute bound; no period gain is discarded.  The train itself
is the literal endpoint-period Bellman lower bound, so no adverse finite-head
sign is being assumed away.

Theorem 1.1 shows that the `y,z` pair by itself is never the obstruction
once it is assigned one ceiling train.  What remains is precisely the
simultaneous allocation of that same ceiling margin against the other
`x,P` pair, encoded without relaxation by `Gamma(delta)`.

## 4. Scope

The uniform pair theorem is proved.  The final scalar gate (3.2) is not
signed here, so this note does not close the two inert h=4 faces, the
five-slot Bellman inequality, or any OR-word upper bound.
