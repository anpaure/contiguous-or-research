# Five-slot two-efficient clocks: closure of the small-period wedge

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves positivity
of the complete size-two-efficient branch for five-slot Bellman tables.
It does not address the size-three-, size-four-, or size-five-efficient
branches, the all-slot Bellman inequality, or an OR-word upper bound.

Put

\[
 A={\sqrt\pi\over2},\qquad a=A^2={\pi\over4},
\]

and let `K` be the Rayleigh signed-tail kernel.  Write

\[
 C(y)=\sum_{q\ge0}K(qy),\qquad
 F_y(s)=\sum_{q\ge0}K(qy+s),
\]

and

\[
 \mathcal L_2(y;s)=C(y)+F_y(s).
\tag{0.1}
\]

The five-slot maximum-efficiency normal form leaves the compact scalar
wedge

\[
 {2A\over5}\le y<{A\over2},
 \qquad A-2y\le s\le {y\over2}.
\tag{0.2}
\]

The main result of this note is

\[
 \boxed{\mathcal L_2(y;s)>0\quad\text{throughout (0.2)}.}
\tag{0.3}
\]

This closes the last scalar gate in the five-slot two-efficient branch.

## 1. Exact rational certificates

Define

\[
 P_8(u)=\sum_{j=0}^{8}{u^j\over j!},
 \qquad
 Q_9(u)=\sum_{j=0}^{9}{(-u)^j\over j!}.
\tag{1.1}
\]

Taylor's theorem and the positive exponential series give, for `u>=0`,

\[
 Q_9(u)\le e^{-u}\le{1\over P_8(u)},
\tag{1.2}
\]

with strict inequalities for `u>0`.

We use the classical rational enclosure

\[
 {157\over50}<\pi<{22\over7}.
\tag{1.3}
\]

The following five checks are entirely rational.  Substituting the
polynomials (1.1), multiplying by their positive denominators, and
collecting integer terms gives

\[
\begin{aligned}
 B_L:={}&{1\over2}Q_9\!\left({11\over56}\right)
 -{3\over2P_8(1413/800)}
 -{2+200/157\over P_8(157/50)}
 >{1\over100},                                      \tag{1.4}\\
 D_L:={}&-{57\over50}Q_9\!\left({11\over14}\right)
 -{1887\over625}Q_9\!\left({352\over175}\right)
 +{468\over625P_8(157/1250)}
 +{625\over157P_8(157/50)}
 <-{1\over20},                                      \tag{1.5}\\
 {187\over1600}
 -{788\over625}Q_9\!\left({198\over175}\right)
 &<-{1\over4},                                      \tag{1.6}\\
 {131\over175}Q_9\!\left({22\over175}\right)
 -{529\over175P_8(1256/625)}
 &>{1\over5},                                       \tag{1.7}\\
 B_R:={}&{4\over5}Q_9\!\left({88\over175}\right)
 -{6\over5P_8(1413/1250)}
 +{1\over4}Q_9\!\left({11\over224}\right)\\
 &-{7\over4P_8(7693/3200)}
 -{2+250/157\over P_8(157/50)}
 >{1\over100}.                                      \tag{1.8}
\end{aligned}
\]

No floating-point estimate is used in (1.4)--(1.8).  These inequalities
are the only endpoint arithmetic needed below.

## 2. The periodized Rayleigh derivative

Normalize

\[
 y=At,\qquad s=Au.
\tag{2.1}
\]

The wedge (0.2) becomes

\[
 {2\over5}\le t\le {1\over2},
 \qquad 1-2t\le u\le {t\over2}.
\tag{2.2}
\]

Put

\[
 h(v)=ve^{-av^2}.
\tag{2.3}
\]

In (2.2), the terms with `q=0,1` in `F_(At)(Au)` lie in the compact part
of the kernel, while every term with `q>=2` lies in the Gaussian tail.
Direct differentiation therefore gives

\[
 {d\over du}F_{At}(Au)=-2A^2W_t(u),
\tag{2.4}
\]

where

\[
 W_t(u)=h(1-u)+h(1-t-u)
       -\sum_{q\ge0}h(1+u+qt).
\tag{2.5}
\]

We prove `W_t(u)>0` throughout (2.2).

## 3. A concave lower envelope

Set

\[
 v=1-t-u,\qquad x=1+t+u.
\tag{3.1}
\]

On (2.2), `x>=3/2`, and `h` is decreasing from that point onward.  The
integral test gives

\[
 \sum_{q\ge1}h(1+u+qt)
 \le h(x)+h(x+t)+{e^{-a(x+t)^2}\over2at}.
\tag{3.2}
\]

Consequently

\[
 W_t(u)\ge H_t(u),
\tag{3.3}
\]

where

\[
\begin{aligned}
 H_t(u)={}&h(1-u)-h(1+u)+h(v)\\
           &-h(x)-h(x+t)-{e^{-a(x+t)^2}\over2at}.
\end{aligned}
\tag{3.4}
\]

### Lemma 3.1 (strict concavity in the shift)

For every fixed `t` in (2.2),

\[
 H_t''(u)<0
 \qquad(1-2t\le u\le t/2).
\tag{3.5}
\]

#### Proof

One has

\[
 h''(z)=2az(2az^2-3)e^{-az^2}
\]

and

\[
 h'''(z)=2ae^{-az^2}(-4a^2z^4+12az^2-3).
\tag{3.6}
\]

On `[3/4,5/4]`, the quantity `az^2` lies in `[1/3,3/2]` after harmless
outward enlargement using (1.3).  The quadratic

\[
 -4q^2+12q-3
\]

is positive on that interval.  Hence `h''` is increasing there and

\[
 h''(1-u)-h''(1+u)\le0.
\tag{3.7}
\]

Also `1/4<=v<=1/2`, so `h''(v)<0`, whereas `x>=3/2` and `x+t>=2`, so
`h''(x),h''(x+t)>0`.  Finally

\[
 {d^2\over du^2}e^{-a(x+t)^2}>0
\]

because `x+t>=2`.  Differentiating (3.4) twice proves (3.5). \(\square\)

Thus the minimum of `H_t` on the shift interval occurs at one of its two
endpoints.

## 4. The lower wedge edge

At `u=1-2t`, formula (3.4) becomes

\[
\begin{aligned}
 L(t):={}&H_t(1-2t)\\
 ={}&h(2t)-h(2-2t)+h(t)-h(2-t)-h(2)
       -{e^{-4a}\over2at}.
\end{aligned}
\tag{4.1}
\]

Its derivative is

\[
\begin{aligned}
 L'(t)={}&2h'(2t)+2h'(2-2t)+h'(t)+h'(2-t)
          +{e^{-4a}\over2at^2}.
\end{aligned}
\tag{4.2}
\]

On `2/5<=t<=1/2`, elementary signs of `h''` give

\[
\begin{aligned}
 h'(2t)&\le0,\\
 h'(2-2t)&\le h'(1),\\
 h'(t)&\le h'(2/5),\\
 h'(2-t)&\le h'(8/5).
\end{aligned}
\tag{4.3}
\]

Also

\[
 {e^{-4a}\over2at^2}
 \le {25\over2\pi}e^{-\pi}.
\tag{4.4}
\]

Using (1.2)--(1.3) to bound the right side of (4.2)--(4.4) gives exactly
the rational expression `D_L` in (1.5).  Hence

\[
 L'(t)<-{1\over20}.
\tag{4.5}
\]

Therefore `L(t)>=L(1/2)`.  At the right endpoint,

\[
 L(1/2)
 ={1\over2}e^{-\pi/16}
 -{3\over2}e^{-9\pi/16}
 -\left(2+{4\over\pi}\right)e^{-\pi}.
\tag{4.6}
\]

The lower bound (1.4) yields

\[
 \boxed{L(t)>{1\over100}.}
\tag{4.7}
\]

## 5. The upper wedge edge

At `u=t/2`, put

\[
\begin{aligned}
 R(t):={}&H_t(t/2)\\
 ={}&D_1(t)+D_3(t)-h(1+5t/2)
       -{e^{-a(1+5t/2)^2}\over2at},
\end{aligned}
\tag{5.1}
\]

where

\[
 D_1(t)=h(1-t/2)-h(1+t/2)
\]

and

\[
 D_3(t)=h(1-3t/2)-h(1+3t/2).
\tag{5.2}
\]

The rational inequalities (1.6)--(1.7) imply

\[
 h'(3/4)+h'(6/5)<0,
 \qquad
 h'(2/5)+h'(8/5)>0.
\tag{5.3}
\]

Since `h'` decreases on `[1/4,5/4]` and increases on `[3/2,7/4]`, (5.3)
gives

\[
 D_1'(t)>0,
 \qquad D_3'(t)<0.
\tag{5.4}
\]

Therefore

\[
 D_1(t)\ge D_1(2/5),
 \qquad D_3(t)\ge D_3(1/2).
\tag{5.5}
\]

Moreover, `h` is decreasing on `[2,infinity)`, so

\[
 h(1+5t/2)\le h(2),
\]

and

\[
 {e^{-a(1+5t/2)^2}\over2at}
 \le {5\over\pi}e^{-\pi}.
\tag{5.6}
\]

Substitution of (5.5)--(5.6) into (5.1) gives the exact rational lower
bound `B_R` in (1.8).  Hence

\[
 \boxed{R(t)>{1\over100}.}
\tag{5.7}
\]

## 6. Positivity of the scalar wedge

By Lemma 3.1 and (4.7), (5.7),

\[
 H_t(u)>0
\]

throughout (2.2).  Equations (3.3) and (2.4) therefore give

\[
 W_t(u)>0,
 \qquad
 {d\over du}F_{At}(Au)<0.
\tag{6.1}
\]

Thus, for `u<=t/2`,

\[
 F_{At}(Au)\ge F_{At}(At/2).
\]

Splitting the arithmetic clock of step `At/2` into its even and odd
terms yields

\[
 C(At)+F_{At}(At/2)=C(At/2).
\tag{6.2}
\]

The all-ceiling theorem gives `C(v)>0` for every `v>0`.  Combining this
with (6.2) proves

\[
 \boxed{\mathcal L_2(At;Au)\ge C(At/2)>0,}
\tag{6.3}
\]

which is (0.3).

## 7. Complete five-slot two-efficient positivity

### Theorem 7.1

Let

\[
 (c_0,c_1,c_2,c_3,c_4,c_5)=(0,x,y,z,w,T)
\]

be nonnegative and internally superadditive, with `T>=A`, and suppose
`y/2` is a maximal generator efficiency.  Then

\[
 \boxed{\sum_{m\ge0}K(V_m)>0.}
\tag{7.1}
\]

#### Proof

If the first threshold crossing occurs at a slot at most four, the
first-crossing deletion theorem reduces to an already-proved positive
table with at most four slots.  Hence assume the first crossing is `T`.

Put

\[
 s=T-2y.
\tag{7.2}
\]

Internal superadditivity and maximal efficiency give

\[
 w=2y,qquad x\le z-y\le s\le y/2.
\tag{7.3}
\]

Since `w<A<=T`,

\[
 {2A\over5}\le y<{A\over2},
 \qquad A-2y\le s\le y/2.
\tag{7.4}
\]

The exact five-slot normal form is

\[
 \Phi
 =\mathcal L_2(y;s)
  +K(x)-K(s)
  +K(z)-K(y+s).
\tag{7.5}
\]

The kernel `K` is decreasing on `[0,3A/4]`.  Indeed, for `0<=q<=3/4`,
the sign of `-K'(Aq)` is the sign of

\[
 f(q)=\pi q-2\operatorname{arctanh}q.
\]

This function is concave, `f(0)=0`, and

\[
 f(3/4)={3\pi\over4}-\log7>0.
\]

Here `f''(q)=-4q/(1-q^2)^2<=0`, while `pi>3` and `e^2>7`
give the strict endpoint sign.  Hence `f>=0` on the interval.  Now
(7.3)--(7.4) give

\[
 0\le x\le s,
 \qquad 0\le z\le y+s\le {3y\over2}<{3A\over4}.
\]

Both corrections in (7.5) are therefore nonnegative.  The scalar wedge
theorem (6.3) makes the first term strictly positive, proving (7.1).
\(\square\)

## 8. Scope

This theorem removes the size-two-efficient branch from the five-slot
Bellman problem.  A nonpositive five-slot table, if one exists, must have a
maximally efficient generator of size three, four, or five.  No claim is
made about those branches or about arbitrary slot number.
