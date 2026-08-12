# Four-slot two-efficient clocks: normalized subrange closure and the exact pulse gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves positivity
throughout the complete two-slot-efficient regime at `n=4`.  It does not
prove the other two four-slot regimes positive.

Put

\[
 A={\sqrt\pi\over2},
\]

and let `K` be the Rayleigh signed-tail kernel.  Consider a four-slot table

\[
 (c_0,c_1,c_2,c_3,c_4)=(0,x,y,z,T)
\]

in the two-slot-efficient regime.  The exact normal-form theorem gives

\[
 T=2y,\qquad r:=z-y\in[x,y/2],
\tag{0.1}
\]

and

\[
 \mathcal B_4(x,y,r)
 :=\sum_{m\ge0}K(V_m)
 =\mathcal L_2(y;r)+K(x)-K(r),
\tag{0.2}
\]

where

\[
 C(y)=\sum_{q\ge0}K(qy),\qquad
 F_y(r)=\sum_{q\ge0}K(qy+r),\qquad
 \mathcal L_2(y;r)=C(y)+F_y(r).
\tag{0.3}
\]

The source theorem already closes `y>=A`.  We treat `A/2<=y<A`.

## 1. The transient is harmless

### Lemma 1.1

For every table in the unresolved range,

\[
 K(x)-K(r)\ge0.
\tag{1.1}
\]

#### Proof

From (0.1),

\[
 0\le x\le r\le y/2<A/2.
\]

The kernel is decreasing on `[0,A/2]`.  Hence (1.1). \(\square\)

Thus no signed four-slot transient remains in this regime: it is enough to
sign `mathcal L_2(y;r)`.

## 2. The normalized triangle is already the three-slot theorem

### Theorem 2.1 (normalized-subrange closure)

If

\[
                         y+r\ge A,
\tag{2.1}
\]

then

\[
                         \boxed{\mathcal B_4(x,y,r)>0}.
\tag{2.2}
\]

#### Proof

Form the three-slot table

\[
                         (0,x,y,y+r).
\tag{2.3}
\]

It is internally superadditive: `y>=2x`, while `r>=x` gives
`y+r>=x+y`.  Its endpoint is at least `A` by (2.1).  Moreover

\[
                         2(y+r)\le3y
\]

because `r<=y/2`.  Hence (2.3) lies in regime I of the proved three-slot
Bellman theorem.  Its exact regime-I normal form is

\[
 \mathcal L_2(y;(y+r)-y)+K(x)-K((y+r)-y)
 =\mathcal B_4(x,y,r).
\]

The three-slot positivity theorem makes this quantity strictly positive.
\(\square\)

Consequently the only genuinely new part of the first four-slot regime is

\[
 \boxed{
 A/2\le y<A,\qquad
 0\le x\le r<\min\{A-y,y/2\}.
 }
\tag{2.4}
\]

This is strictly smaller than the rectangle stated in the first
four-slot normal-form note.  In particular, when `y>=2A/3`, only the thin
triangle `r<A-y` remains.

## 3. Exact compact Gaussian form

Normalize

\[
 t={y\over A},\qquad s={r\over A},\qquad a=A^2={\pi\over4}.
\tag{3.1}
\]

Then `1/2<=t<1` and `0<=s<=t/2`.  Away from the harmless equality
boundary `s+t=1`, direct expansion of the kernel gives the following two
formulas.

If `s+t<=1`, then

\[
\begin{aligned}
 \mathcal L_2(At;As)=4
 &-e^{-a(1-t)^2}-2e^{-a}
  -\sum_{q\ge1}e^{-a(1+qt)^2}\\
 &-e^{-a(1-s)^2}-e^{-a(1-t-s)^2}
  -\sum_{q\ge0}e^{-a(1+s+qt)^2}.
\end{aligned}
\tag{3.2}
\]

If `s+t>=1`, then

\[
\begin{aligned}
 \mathcal L_2(At;As)=3
 &-e^{-a(1-t)^2}-2e^{-a}
  -\sum_{q\ge1}e^{-a(1+qt)^2}\\
 &-e^{-a(1-s)^2}
  -\sum_{q\ge0}e^{-a(1+s+qt)^2}.
\end{aligned}
\tag{3.3}
\]

At `s+t=1`, the omitted compact contribution is
`1-e^{-a(1-t-s)^2}=0`, so (3.2) and (3.3) agree exactly.  Thus the
remaining Bellman problem is a two-variable compact Gaussian inequality;
there is no infinite max-plus recurrence left.

## 4. Exact pulse representation

Let `sigma` be socket measure minus job measure:

\[
 d\sigma(u)=
 \begin{cases}
  2(A-u)e^{-(A-u)^2}\,du
  -2(A+u)e^{-(A+u)^2}\,du,&0<u<A,\\
  -2(A+u)e^{-(A+u)^2}\,du,&u>A.
 \end{cases}
\tag{4.1}
\]

Then, for every `v>=0`,

\[
                         K(v)=\sigma([v,\infty)).
\tag{4.2}
\]

For `0<=r<=y/2`, define the periodic half-cell pulse

\[
 P_{y,r}=\bigcup_{q\ge0}[qy+r,qy+y/2).
\tag{4.3}
\]

### Theorem 4.1 (pulse identity)

One has the exact identity

\[
 \boxed{
 \mathcal L_2(y;r)
 =C(y/2)+\sigma(P_{y,r}).
 }
\tag{4.4}
\]

#### Proof

Splitting the arithmetic clock of step `y/2` into its even and odd terms
gives

\[
 C(y/2)=C(y)+F_y(y/2).
\tag{4.5}
\]

Therefore

\[
 \mathcal L_2(y;r)-C(y/2)
 =\sum_{q\ge0}\bigl(K(qy+r)-K(qy+y/2)\bigr).
\tag{4.6}
\]

Using (4.2), each summand is `sigma([qy+r,qy+y/2))` (endpoint choices
are immaterial because `sigma` is absolutely continuous).  The intervals
are disjoint, and Gaussian integrability justifies summation.  This is
(4.4). \(\square\)

Since the all-ceiling theorem gives `C(y/2)>0`, the exact residual scalar
gate is

\[
 \boxed{
 C(y/2)+\sigma(P_{y,r})>0
 }
\tag{4.7}
\]

on the compact domain (2.4).  The stronger pulse inequality

\[
                         \sigma(P_{y,r})\ge0
\tag{4.8}
\]

would close the entire two-slot-efficient four-slot regime by itself, but
(4.8) is neither asserted nor needed in the later critical-point proof.

Two boundary checks are automatic:

* at `r=y/2`, the pulse is empty and
  `mathcal L_2(y;y/2)=C(y/2)>0`;
* at `r=0`, `mathcal L_2(y;0)=2C(y)>0`.

## 5. The whole low-period rectangle is positive

The pulse need not be estimated globally in the range

\[
                         {A\over2}\le y\le {2A\over3}.
\]

On this range the shifted train itself decreases to the balanced residue.

Put

\[
 h(u)=ue^{-au^2},\qquad a={\pi\over4}.
\]

### Lemma 5.1 (positive periodized Rayleigh derivative)

For

\[
 {1\over2}\le t\le {2\over3},qquad0\le s\le {t\over2},
\]

one has

\[
\begin{aligned}
 W_t(s):={}&h(1-s)+h(1-t-s)\\
 &-\sum_{q\ge0}h(1+s+qt)>0.
\end{aligned}
\tag{5.1}
\]

#### Proof

Write

\[
 v=1-t-s,\qquad x=1+t+s.
\]

The function `h` is decreasing on `[3/2,infinity)`.  Hence the integral
test gives

\[
 \sum_{q\ge1}h(1+s+qt)
 \le h(x)+h(x+t)+{e^{-a(x+t)^2}\over2at}.
\tag{5.2}
\]

It is therefore enough to prove positivity of

\[
\begin{aligned}
 H_t(s):={}&h(1-s)-h(1+s)+h(v)\\
 &-h(x)-h(x+t)-{e^{-a(x+t)^2}\over2at}.
\end{aligned}
\tag{5.3}
\]

For later use, note

\[
 h''(u)=2au(2au^2-3)e^{-au^2}
\]

and

\[
 h'''(u)=2ae^{-au^2}
 \left(-4a^2u^4+12au^2-3\right).
\tag{5.4}
\]

On `[2/3,4/3]`, put `q=au^2`.  The elementary bounds

\[
 {157\over200}<a<{11\over14}
\tag{5.5}
\]

give `1/3<q<3/2`.  The polynomial

\[
 -4q^2+12q-3
\]

is increasing and positive on this interval.  Thus `h''` is increasing
on `[2/3,4/3]`, and

\[
 h''(1-s)-h''(1+s)\le0.
\]

Also `h''(v)<=0` because `0<=v<=1/2`, whereas
`h''(x),h''(x+t)>=0` because `x>=3/2`.  Finally the second derivative in
`s` of

\[
 {e^{-a(x+t)^2}\over2at}
\]

is positive.  Therefore

\[
                         H_t''(s)<0.
\tag{5.6}
\]

So the minimum of `H_t` on `[0,t/2]` is attained at one of its endpoints.
It remains to verify those endpoints uniformly in `t`.  The following
short rational certificate records that verification.

Define

\[
 P_8(u)=\sum_{k=0}^8{u^k\over k!},\qquad
 Q_5(u)=\sum_{k=0}^5{(-u)^k\over k!}.
\tag{5.7}
\]

For `u>=0`, (5.5) and the Taylor remainder give

\[
 Q_5\!\left({11u^2\over14}\right)
 \le e^{-au^2}
 \le {1\over P_8(157u^2/200)}.
\tag{5.8}
\]

Put

\[
 h_-(u)=uQ_5(11u^2/14),\qquad
 h_+(u)={u\over P_8(157u^2/200)},
\tag{5.9}
\]

and split `[1/2,2/3]` into the eight rational intervals

\[
 I_i=[\ell_i,u_i],\qquad
 \ell_i={24+i\over48},\quad u_i={25+i\over48}
 \quad(0\le i<8).
\tag{5.10}
\]

Monotonicity of `h` on the argument intervals occurring in (5.3), and
monotonicity of the final Gaussian tail, give for `t in I_i`

\[
\begin{aligned}
 H_t(0)\ge B_i^{(0)}:={}&
 h_-(1-u_i)-h_+(1+\ell_i)-h_+(1+2\ell_i)\\
 &-{1\over
  2(157/200)\ell_iP_8((157/200)(1+2\ell_i)^2)},
\end{aligned}
\tag{5.11}
\]

and

\[
\begin{aligned}
 H_t(t/2)\ge B_i^{(1)}:={}&
 h_-(1-u_i/2)-h_+(1+\ell_i/2)\\
 &+h_-(1-3u_i/2)-h_+(1+3\ell_i/2)\\
 &-h_+(1+5\ell_i/2)\\
 &-{1\over
  2(157/200)\ell_iP_8((157/200)(1+5\ell_i/2)^2)}.
\end{aligned}
\tag{5.12}
\]

Every quantity in (5.11)--(5.12) is rational.  Expanding `P_8,Q_5` and
cross-multiplying gives the exact certificate

\[
\begin{array}{c|cccccccc}
 i&0&1&2&3&4&5&6&7\\ \hline
 B_i^{(0)}>1/1000&\checkmark&\checkmark&\checkmark&\checkmark&
 \checkmark&\checkmark&\checkmark&\checkmark\\
 B_i^{(1)}>1/50&\checkmark&\checkmark&\checkmark&\checkmark&
 \checkmark&\checkmark&\checkmark&\checkmark
\end{array}
\tag{5.13}
\]

This is only integer arithmetic; no numerical approximation to `pi` or
an exponential is used.  Equations (5.6) and (5.13) prove `H_t(s)>0`, and
(5.2) proves (5.1). \(\square\)

### Theorem 5.2 (low-period closure)

If

\[
                         {A\over2}\le y\le {2A\over3},
\]

then every two-slot-efficient four-slot table has strictly positive
Bellman sum.

#### Proof

For the normalized variables `t=y/A`, `s=r/A`, direct differentiation of
the shifted train gives

\[
 {d\over ds}F_{At}(As)=-2A^2W_t(s)<0
\tag{5.14}
\]

by Lemma 5.1.  Hence

\[
 F_y(r)\ge F_y(y/2).
\]

Using the even/odd identity (4.5),

\[
 \mathcal L_2(y;r)
 \ge C(y)+F_y(y/2)=C(y/2)>0.
\]

The transient (1.1) is nonnegative, so the full Bellman sum is strictly
positive. \(\square\)

## 6. The residual thin triangle is positive

It remains to take

\[
 {2\over3}\le t<1,\qquad0\le s\le1-t.
\tag{6.1}
\]

The interval is closed at its endpoints during minimization; the strict
source domain is recovered afterward.

### Lemma 6.1 (monotonicity up to `t=4/5`)

For

\[
 {2\over3}\le t\le {4\over5},\qquad0\le s\le1-t,
\]

one has `W_t(s)>0`.

#### Proof

The tail bound (5.2) and the lower function `H_t` in (5.3) remain valid.
The same sign calculation as in Lemma 5.1 gives `H_t''(s)<0` on the new
domain: `1-s,1+s` still lie in `[2/3,4/3]`, the small argument lies in
`[0,1/3]`, and both tail arguments exceed `3/2`.  Hence it again suffices
to check the endpoints `s=0,1-t`.

Use `Q_5` from (5.7), and put

\[
 P_{10}(u)=\sum_{k=0}^{10}{u^k\over k!},
 \qquad
 \widetilde h_+(u)={u\over P_{10}(157u^2/200)}.
\tag{6.2}
\]

Split `[2/3,4/5]` into

\[
 J_i=[\ell_i,u_i],\qquad
 \ell_i={40+i\over60},\quad u_i={41+i\over60}
 \quad(0\le i<8).
\tag{6.3}
\]

The same Taylor inequalities as (5.8) give, for `t in J_i`,

\[
\begin{aligned}
 H_t(0)\ge D_i^{(0)}:={}&h_-(1-u_i)
 -\widetilde h_+(1+\ell_i)-\widetilde h_+(1+2\ell_i)\\
 &-{1\over
 2(157/200)\ell_iP_{10}((157/200)(1+2\ell_i)^2)},
\end{aligned}
\tag{6.4}
\]

and

\[
\begin{aligned}
 H_t(1-t)\ge D_i^{(1)}:={}&
 \min\{h_-(\ell_i),h_-(u_i)\}
 -\widetilde h_+(2-u_i)-\widetilde h_+(2)\\
 &-\widetilde h_+(2+\ell_i)
 -{1\over
 2(157/200)\ell_iP_{10}((157/200)(2+\ell_i)^2)}.
\end{aligned}
\tag{6.5}
\]

The minimum in (6.5) is valid because `h` is unimodal.  Exact rational
expansion and cross-multiplication give

\[
\begin{array}{c|cccccccc}
 i&0&1&2&3&4&5&6&7\\ \hline
 D_i^{(0)}>1/40&\checkmark&\checkmark&\checkmark&\checkmark&
 \checkmark&\checkmark&\checkmark&\checkmark\\
 D_i^{(1)}>1/2000&\checkmark&\checkmark&\checkmark&\checkmark&
 \checkmark&\checkmark&\checkmark&\checkmark.
\end{array}
\tag{6.6}
\]

Thus both endpoints are positive; concavity proves `H_t(s)>0`, and the
tail comparison proves `W_t(s)>0`. \(\square\)

It follows that for `t<=4/5`, `F_{At}(As)` decreases in `s`.  Its minimum
on (6.1) is at `s=1-t`, where `y+r=A`; Theorem 2.1 makes the Bellman sum
strictly positive.

For `t>=4/5`, monotonicity is unnecessary.  We instead price every
possible interior critical point.

### Lemma 6.2 (critical-point Gaussian collapse)

Suppose

\[
 {4\over5}\le t<1,\qquad0<s<1-t,\qquad W_t(s)=0.
\]

Then

\[
                         F_{At}(As)>0.
\tag{6.7}
\]

#### Proof

Put

\[
 u=1-s,\qquad v=1-t-s,\qquad w=1+s,\qquad d=w+t.
\]

At a critical point, (5.1) says

\[
 h(u)+h(v)=\sum_{q\ge0}h(w+qt).
\tag{6.8}
\]

For `q>=1`, `w+qt>=d`; hence

\[
 \sum_{q\ge1}e^{-a(w+qt)^2}
 \le {h(u)+h(v)-h(w)\over d}.
\tag{6.9}
\]

Using the two-compact formula for the shifted train,

\[
 F_{At}(As)\ge
 2-e^{-au^2}-e^{-av^2}-e^{-aw^2}
 -{h(u)+h(v)-h(w)\over d}=:\Phi(t,s).
\tag{6.10}
\]

Multiplication by `d` collapses this expression to three Gaussians:

\[
 d\Phi=
 2d-(2+t)e^{-au^2}-2e^{-av^2}-t e^{-aw^2}.
\tag{6.11}
\]

Set `q=1-t`, `p=s`.  Then `0<=p<=q<=1/5`, and (6.11) is

\[
 G(q,p)=2(2+p-q)
 -(3-q)e^{-a(1-p)^2}
 -2e^{-a(q-p)^2}
 -(1-q)e^{-a(1+p)^2}.
\tag{6.12}
\]

For fixed `p`,

\[
 {\partial G\over\partial q}
 =-2+e^{-a(1-p)^2}+e^{-a(1+p)^2}
 +4a(q-p)e^{-a(q-p)^2}<0.
\tag{6.13}
\]

Indeed, the three positive terms are respectively smaller than `2/3`,
`1/2`, and `22/35`; their sum is smaller than two.  Therefore the minimum
is at `q=1/5`.

On that boundary define

\[
\begin{aligned}
 G_*(p):=G(1/5,p)
 ={}&{18\over5}+2p-{14\over5}e^{-a(1-p)^2}\\
 &-2e^{-a(1/5-p)^2}-{4\over5}e^{-a(1+p)^2}.
\end{aligned}
\tag{6.14}
\]

We record three rational estimates.  First,

\[
                         G_*''(p)>1.
\tag{6.15}
\]

Write `E(x)=e^{-ax^2}`.  On `[4/5,6/5]`, `E''` is increasing.  Rational
Taylor bounds give

\[
 E''(1)<{5\over12},\qquad E''(6/5)<{13\over20}.
\tag{6.16}
\]

For `0<=x<=1/5`,

\[
 -2E''(x)=4a(1-2ax^2)E(x)
 >4{157\over200}{164\over175}{339\over350}
 ={2182143\over765625}>{27\over10}.
\tag{6.17}
\]

Thus

\[
 G_*''(p)>{27\over10}-{14\over5}{5\over12}
 -{4\over5}{13\over20}={76\over75}>1.
\]

For completeness, (6.16) follows by putting `a<11/14` into `E''`, using
that `q(2q-1)e^{-q}` increases on the relevant `q` interval, and using
`e^{-q}<1/P_8(q)`.

Second, the same rational bounds give

\[
                         G_*(0)>{3\over200}.
\tag{6.18}
\]

Indeed,

\[
 G_*(0)={18\over5}(1-e^{-a})-2e^{-a/25},
\]

and replacing both exponentials by their `P_8` upper bounds at
`a>157/200` proves (6.18) by integer cross-multiplication.

Finally,

\[
                         G_*'(0)>-{1\over20}.
\tag{6.19}
\]

Here

\[
 G_*'(0)=2-4ae^{-a}-{4a\over5}e^{-a/25}.
\]

The functions `ae^{-a}` and `ae^{-a/25}` increase on the present range;
putting `a<11/14` and using the `P_8` upper bounds proves (6.19) by rational
cross-multiplication.

Strong convexity now gives, for `p>=0`,

\[
 G_*(p)>{3\over200}-{1\over800}={11\over800}>0.
\tag{6.20}
\]

Equations (6.13) and (6.20) give `G(q,p)>0`, so (6.11) gives
`Phi(t,s)>0`.  Equation (6.10) proves (6.7). \(\square\)

### Theorem 6.3 (complete two-efficient positivity)

Every two-slot-efficient four-slot Bellman table has strictly positive
Bellman sum.

#### Proof

The source theorem closes `y>=A`.  Theorem 5.2 and Lemma 6.1 close all
subcritical periods through `y=4A/5` by monotonicity.  Now take
`4A/5<=y<A`.  On the compact `s` interval, a minimum of
`mathcal L_2(y;r)` is either:

* at `r=0`, where it equals `2C(y)>0`;
* at `r=A-y`, where Theorem 2.1 (with `x=r`) makes it positive; or
* at an interior critical point, where Lemma 6.2 gives `F_y(r)>0`, while
  `C(y)>0` by the all-ceiling theorem.

Thus `mathcal L_2(y;r)>0` throughout.  The transient (1.1) is
nonnegative. \(\square\)

## 7. Exact scope

This note proves the complete first efficiency regime at `n=4`.  The
remaining four-slot work consists only of the three-slot-efficient
transient and the four-state Apéry regime.  The note does not prove either
of those regimes, the universal Bellman inequality, or any OR-word bound.

<!-- Superseded scope retained only as hidden lineage:
generator is most efficient and any of the following holds:

\[
 y\ge A,
 \qquad y+r\ge A,
 \qquad {A\over2}\le y\le {2A\over3}.
\]

The only part of this efficiency regime not closed here is therefore

\[
 \boxed{
 {2A\over3}<y<A,qquad 0\le x\le r<A-y.
 }
\tag{6.1}
\]

It is governed by (3.2), equivalently by the pulse inequality (4.7).  The
note does not sign this last thin triangle, the three-slot-efficient
transient, the four-state Apéry regime, the universal Bellman inequality,
or any OR-word bound.
-->
