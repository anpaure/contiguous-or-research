# Five-slot three-efficient clocks: threshold-endpoint positivity and the exact delayed-crossing frontier

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves the
threshold-saturated part of the five-slot, size-three-efficient branch
strictly positive, with all five finite pulses retained through a Bellman
lower bound.  On the only remaining (inert-endpoint) part it collapses the
five-pulse formula exactly to two delayed-crossing faces and reduces one of
them to a two-variable repeated-gap scalar.  It does not sign the two final
delayed-crossing gates and therefore does not prove the full five-slot or
all-slot Bellman inequality.

Put

\[
 A={\sqrt\pi\over2}
\]

and let

\[
 K(t)=
 \begin{cases}
 1-e^{-(A-t)^2}-e^{-(A+t)^2},&0\le t\le A,\\
 -e^{-(A+t)^2},&t>A.
 \end{cases}
\]

For `P>0`, write

\[
 F_P(v)=\sum_{q\ge0}K(qP+v),
 \qquad C(P)=F_P(0).
\tag{0.1}
\]

Consider an internally superadditive five-slot table in the
size-three-efficient regime,

\[
 (c_0,\ldots,c_5)=(0,x,y,p,p+a,p+b),
\tag{0.2}
\]

whose endpoint is the first displayed threshold crossing:

\[
 x,y,p,p+a<A\le p+b.
\tag{0.3}
\]

The inherited inequalities are

\[
 a\ge x,\qquad b\ge y,\qquad b\ge a+x,
 \qquad 0\le a\le {p\over3},\qquad
 0\le b\le {2p\over3},
\tag{0.4}
\]

as well as

\[
 y\ge2x,qquad p\ge x+y,qquad p+a\ge2y.
\tag{0.5}
\]

The exact five-pulse normal form is

\[
\begin{aligned}
 \Phi={}&\mathcal L_3(p;s_1,s_2)\\
 &+K(x)-K(s_1)
  +K(p+a)-K(p+s_1)
  +K(V_7)-K(2p+s_1)\\
 &+K(y)-K(s_2)
  +K(p+b)-K(p+s_2),
\end{aligned}
\tag{0.6}
\]

where

\[
 s_1=\max\{a,2b-p\},\qquad
 s_2=\max\{b,2a\},
\tag{0.7}
\]

and

\[
 V_7=\max\{2p+a,p+b+y\}.
\tag{0.8}
\]

## 1. Two uniform one-period train estimates

We first record the analytic estimate used at the threshold endpoint.

### Lemma 1.1

One has

\[
 \boxed{C(A)>{43\over1000}}
\tag{1.1}
\]

and

\[
 \boxed{F_A(v)<{61\over1000}
 \qquad(0\le v\le2A/5).}
\tag{1.2}
\]

Moreover `C(A)<61/1000`.

#### Proof

Normalize `v=At`, put `alpha=A^2=pi/4`, and define

\[
 \Theta(t)=\sum_{j\in\mathbb Z}e^{-\alpha(t-j)^2},
 \qquad
 \epsilon=4\sum_{m\ge1}e^{-4\pi m^2}.
\]

Poisson summation gives

\[
 \Theta(t)=2+4\sum_{m\ge1}e^{-4\pi m^2}\cos(2\pi mt),
 \qquad \epsilon<{1\over20000}.
\tag{1.3}
\]

The standard completion of the half-train is

\[
 F_A(At)=1-\Theta(t)+e^{-\alpha t^2}
             +\sum_{j\ge2}e^{-\alpha(j-t)^2}.
\tag{1.4}
\]

At `t=0`, retain the `j=2` term in (1.4):

\[
 C(A)>e^{-\pi}-{1\over20000}.
\tag{1.5}
\]

We use `333/106<pi<22/7`.  The elementary exponential bounds

\[
 e<{87\over32},
 \qquad
 e^{1/7}<1+{1\over7}
   +{{1\over98}\over1-{1\over21}}
 ={2261\over1960}
\tag{1.6}
\]

give

\[
 e^\pi<e^{22/7}
 <\left({87\over32}\right)^3{2261\over1960}
 <{20000\over861}.
\tag{1.7}
\]

The final comparison in (1.7) is the integer inequality

\[
 1488875283\cdot861
 <64225280\cdot20000.
\]

Thus `e^{-pi}>861/20000`, and (1.5) proves (1.1).  Here
`e<87/32` follows by summing through degree three and bounding the
remaining exponential tail by `(1/24)/(1-1/5)`.

For the upper bound, put

\[
 H(t)=e^{-\alpha t^2}+e^{-\alpha(2-t)^2}.
\]

The sign of `H'(t)` is the sign of

\[
 g(t)=\log{2-t\over t}-\pi(1-t).
\tag{1.8}
\]

The usual derivative calculation shows that `g` crosses zero once on
`(0,2/3)`, so `H` increases and then decreases.  The crossing lies in

\[
 {1\over10}<t_*<{3\over25}.
\tag{1.9}
\]

Indeed,

\[
 \log19>{20\over7}>{9\pi\over10},
\]

where `e^{20/7}<19` follows from

\[
 e^2<\left({87\over32}\right)^2,
 \qquad e^{6/7}<1+{6\over7}
 +{{18\over49}\over1-{2\over7}}={83\over35}.
\]

At the other endpoint,

\[
 {22\pi\over25}>{69\over25}>\log{47\over3}.
\]

For the last inequality, the positive Taylor series gives
`e^2>369/50` and `e^{19/25}>32/15`, whose product is larger than
`47/3`.

Consequently every value of `H` on `[0,2/5]` is bounded by the separate
coordinate maxima over the interval in (1.9):

\[
 H(t)
 <e^{-\pi/400}+e^{-2209\pi/2500}
 <{397\over400}+{1\over16}
 ={211\over200}.
\tag{1.10}
\]

For the first exponential in (1.10), use

\[
 e^{-\pi/400}<{1\over1+333/42400}
 ={42400\over42733}<{397\over400}.
\]

For the second, note

\[
 {2209\pi\over2500}>{111\over40};
\]

the degree-five positive Taylor polynomial at `111/160` is larger than
two, hence `e^{111/40}>16`.

It remains to bound the terms in (1.4) after `j=2`.  For
`0<=t<=2/5`, their first term is smaller than `1/190`, because

\[
 {169\pi\over100}>{53\over10},
 \qquad e^{53/10}=e^5e^{3/10}>148\,{13\over10}>190;
\]

the inequality `e^5>148` is already given by its degree-twelve positive
Taylor polynomial.  Successive terms have ratio smaller than `1/100`,
since

\[
 {31\pi\over20}>{93\over20},
 \qquad e^{93/20}=e^4e^{13/20}>54\,{50\over27}=100.
\]

Here the degree-ten Taylor polynomial gives `e^4>54`, while
`e^{13/20}>1+13/20+(13/20)^2/2>50/27`.  Therefore

\[
 \sum_{j\ge3}e^{-\alpha(j-t)^2}
 <{1/190\over1-1/100}<{1\over180}.
\tag{1.11}
\]

Equations (1.3), (1.4), (1.10), and (1.11) give

\[
 F_A(At)
 <{11\over200}+{1\over180}+{1\over20000}
 <{61\over1000},
\]

which proves (1.2).

Finally,

\[
 C(A)
 <1-2e^{-\pi/4}-e^{-\pi}
 <1-{10\over11}-{1\over25}
 ={14\over275}<{61\over1000}.
\]

This proves the lemma. \(\square\)

We also use the already proved critical-point fact for `F_A`: every
interior critical point on `[0,A/2]` is a strict local maximum.  Therefore

\[
 F_A(u)\ge\min\{C(A),F_A(v)\}
 \qquad(0\le u\le v\le A/2).
\tag{1.12}
\]

The same proof works for the shifted train `F_P` on any compact interval
on which the first term is compact and every positive-period term has the
displayed Gaussian-tail form; it will be replayed explicitly below.

## 2. The threshold endpoint is uniformly positive

### Theorem 2.1

If the saturated endpoint in (0.2) is exactly

\[
                         p+b=A,
\tag{2.1}
\]

then

\[
                         \boxed{\Phi>{69\over10000}>0.}
\tag{2.2}
\]

#### Proof

Equation (2.1) and `b<=2p/3` give

\[
 {3A\over5}\le p<A,
 \qquad 0<b\le{2A\over5}.
\tag{2.3}
\]

Since `p+a<A=p+b`, one has `a<b`.  Equations (0.4) give

\[
 0\le x\le b-a,
 \qquad0\le y\le b.
\tag{2.4}
\]

The endpoint-period Bellman lower bound, applied at the literal endpoint
`A`, retains every finite pulse in (0.6) and gives

\[
 \Phi\ge C(A)+F_A(x)+F_A(y)+F_A(p)+F_A(p+a).
\tag{2.5}
\]

The reflected-train identity gives, with the same `epsilon` as (1.3),

\[
 F_A(A-v)>-F_A(v)-\epsilon.
\tag{2.6}
\]

Using `p=A-b` and `p+a=A-(b-a)` in (2.5), then applying
(1.12), yields

\[
\begin{aligned}
 \Phi>{}&C(A)
 +\min\{C(A),F_A(b-a)\}
 +\min\{C(A),F_A(b)\}\\
 &-F_A(b-a)-F_A(b)-2\epsilon.
\end{aligned}
\tag{2.7}
\]

Put `U=61/1000`.  Lemma 1.1 says `C(A)<U` and
`F_A(v)<U` on the whole range in (2.7), so

\[
 \min\{C(A),F_A(v)\}-F_A(v)\ge C(A)-U.
\tag{2.8}
\]

Finally (1.1), (1.3), and (2.7)--(2.8) give

\[
 \Phi>3{43\over1000}-2{61\over1000}-{2\over20000}
 ={69\over10000}>0.
\]

No term of the five-pulse identity has been discarded; (2.5) prices the
actual Bellman clock before taking the lower bound. \(\square\)

## 3. Exact endpoint-saturation dichotomy

Let `P_5` be the best value at capacity five using only denominations
one through four.  Internal superadditivity gives the exact identity

\[
 P_5=p+v,
 \qquad v=\max\{y,a+x\}.
\tag{3.1}
\]

Indeed the only maximal two-part candidates are `2+3` and `1+4`;
every refinement is bounded by one of them using (0.5).

After endpoint saturation,

\[
                         b=\max\{A-p,v\}.
\tag{3.2}
\]

The first alternative in (3.2) is Theorem 2.1.  It remains to understand
the strict inert alternative

\[
                         b=v>A-p.
\tag{3.3}
\]

### Theorem 3.1 (all five pulses collapse on the inert face)

Under (3.3), put

\[
                         w=\max\{y,2a\}.
\tag{3.4}
\]

Then

\[
 s_1=a,qquad s_2=w,qquad V_7=2p+a,
\tag{3.5}
\]

and the exact five-pulse identity becomes

\[
\boxed{
\begin{aligned}
 \Phi={}&\mathcal L_3(p;a,w)\\
 &+K(x)-K(a)+K(y)-K(w)\\
 &+K(p+b)-K(p+w).
\end{aligned}}
\tag{3.6}
\]

Thus the inert fifth generator contributes no new Bellman value: (3.6)
is exactly the delayed-crossing four-slot, three-efficient normal form.

#### Proof

If `b=y`, then `2b-p<=a` is the inequality `2y<=p+a`.
If `b=a+x`, then

\[
 2b-p\le a
 \quad\Longleftrightarrow\quad
 a+2x\le p,
\]

which follows from `a<=p/3` and `p>=3x`.  Hence `s_1=a`.
Also `a+x<=2a`, so

\[
 \max\{b,2a\}=\max\{y,a+x,2a\}=\max\{y,2a\}=w.
\]

Finally, if `b=y`, then `b+y=2y<=p+a`; if `b=a+x`, then
`b+y=a+x+y<=a+p`.  Thus `V_7=2p+a`.

Substitution in (0.6) cancels the capacity-four and capacity-seven
pulses and gives (3.6). \(\square\)

## 4. The delayed `w=y` face reduces to one repeated-gap scalar

Assume (3.3) and `w=y`.  Since `a+x<=2a<=y`, one has

\[
                         b=y=w.
\]

Formula (3.6) reduces exactly to

\[
 \Phi=\mathcal L_3(p;a,y)+K(x)-K(a)
      \ge\mathcal L_3(p;a,y),
\tag{4.1}
\]

because `0<=x<=a<A/3` and `K` decreases there.

For fixed `p,a`, the feasible interval for `y` is

\[
 y\ge2a,\qquad y>A-p,\qquad
 y\le{p+a\over2}<{A\over2}.
\tag{4.2}
\]

These are the exact inert conditions.  Assign the overlap \(y=2a\) to the
\(w=2a\) face.  The relative interior of the remaining \(w=y\) face has

\[
 \max\{2a,A-p\}<y\le{p+a\over2}.
\tag{4.2a}
\]

All minimization below is on the closure: the boundary \(y=A-p\) is the
threshold face and \(y=2a\) is the overlap face.

Write

\[
 G_{p}(u)=\sum_{q\ge0}K(qp+u).
\]

### Lemma 4.1

Every interior critical point of `G_p` on the interval in (4.2) is a
strict local maximum.  Consequently the minimum in `y` occurs on the
boundary of (4.2).

#### Proof

On this interval,

\[
 G_p(u)=1-e^{-(A-u)^2}
        -\sum_{q\ge0}e^{-(A+u+qp)^2}.
\tag{4.3}
\]

Put `phi(t)=t e^{-t^2}` and
`lambda(t)=phi'(t)/phi(t)=1/t-2t`.  The function `lambda` is strictly
decreasing.  At an interior critical point,

\[
 \sum_{q\ge0}\phi(A+u+qp)=\phi(A-u).
\]

Therefore

\[
 {1\over2}G_p''(u)
 \le2A\left({1\over A^2-u^2}-2\right)\phi(A-u)<0,
\tag{4.4}
\]

because `u<A/2` and
`A^2-u^2>3A^2/4=3*pi/16>1/2`. \(\square\)

The lower boundary `y=A-p`, when active, is the threshold endpoint of
Theorem 2.1.  The lower boundary `y=2a` is the overlap with the second
face below.  The only new boundary is

\[
                         2y=p+a.
\tag{4.5}
\]

Put

\[
                         \beta={p-a\over2}.
\]

Then `p=a+2*beta` and `y=a+beta`.  Hence the entire delayed `w=y` face is
reduced to the following two-variable scalar gate:

\[
\boxed{
 \mathcal R(a,\beta)
 :=\mathcal L_3(a+2\beta;a,a+\beta)>0
}
\tag{4.6}

on the closed gate domain

\[
 0\le a\le\beta,
 \qquad 2a+2\beta<A\le2a+3\beta.
\tag{4.7}
\]

The genuinely inert part has the strict right inequality
\(A<2a+3\beta\).  Equality is the already positive threshold endpoint and
is included only to close the boundary of the scalar gate.

The three cyclic gaps of (4.6) are `(a,beta,beta)`.  Thus (4.6) is a
literal repeated-gap theta train, not a residual five-pulse expression.

## 5. The delayed `w=2a` face is one explicit retained-pulse gate

Assume (3.3) and `w=2a`.  Then

\[
 a\le b\le2a,
 \qquad a<A-p<b.
\tag{5.1}
\]

Since `x<=b-a` and `y<=b`, while `K` decreases on `[0,2A/3]`, (3.6)
gives the proof-safe lower bound

\[
                         \Phi\ge\mathcal H(p,a,b),
\tag{5.2}
\]

where

\[
\boxed{
\begin{aligned}
 \mathcal H(p,a,b):={}&\mathcal L_3(p;a,2a)\\
 &+K(b-a)-K(a)+K(b)-K(2a)\\
 &+K(p+b)-K(p+2a).
\end{aligned}}
\tag{5.3}

The exact domain is

\[
 p<A,qquad p\ge3a,qquad
 a<A-p<b\le2a.
\tag{5.4}
\]

Every pulse in (5.3) is retained.  In particular, the last tail pulse is
generally negative and has not been discarded.

At the density-tie boundary `p=3a`, the gate becomes

\[
\begin{aligned}
 \mathcal H(3a,a,b)={}&C(a)
 +K(b-a)-K(a)+K(b)-K(2a)\\
 &+K(3a+b)-K(5a),
\end{aligned}
\tag{5.5}

with `A/5<a<A/4` possible on the genuinely new part.  At `b=2a`, every
pulse in (5.5) vanishes and the value is the positive ceiling `C(a)`.
At `b=A-3a`, the literal endpoint is `A` and Theorem 2.1 applies.

Thus the five-slot size-three-efficient branch is now reduced to the two
explicit analytic objects (4.6) and (5.3).  The first is a two-variable
repeated-gap train and the second is a three-variable train with exactly
three retained pulse differences.  No chamber of the original
five-pulse formula remains unclassified.

## 6. Exact scope

This note proves:

1. every threshold-saturated (`c_5=A`) size-three-efficient five-slot
   table is uniformly positive;
2. on the inert endpoint, `s_1=a` and the capacity-four and
   capacity-seven pulses vanish identically;
3. the delayed `w=y` face reduces to the repeated-gap scalar
   (4.6)--(4.7);
4. the delayed `w=2a` face reduces to the fully explicit retained-pulse
   gate (5.3)--(5.4).

It does **not** assert positivity of (4.6) or (5.3).  Those are the exact
remaining analytic gates for this maximum-efficiency branch.
