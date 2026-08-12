# Six-slot prethreshold repeated gaps reduce to one half-period function

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It proves strict
monotonicity in the repeated gap on the complete prethreshold domain and
reduces that two-variable domain to one explicit half-period function.
Both endpoints of the remaining one-variable interval are strictly
positive.  This note does **not** sign the interior of that interval and
therefore does not by itself close the six-slot `h=3` branch.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_P(w)=\sum_{q\ge0}K(qP+w),
\tag{0.1}
\]

and

\[
 \mathcal L_3(P;u,v)=F_P(0)+F_P(u)+F_P(v).
\tag{0.2}
\]

The common residual left by chambers II and III is

\[
 \boxed{
 \mathcal R_-(P,a)
 =\mathcal L_3\!\left(P;a,{P+a\over2}\right)}
\tag{0.3}
\]

on

\[
 {A\over2}\le P<{2A\over3},
 \qquad
 0\le a\le {P\over3},
 \qquad
 3P+a\le2A.
\tag{0.4}
\]

The equality face in the last condition is understood by continuity.  In
the literal chamber-II interior it is strict.

The already-closed short-singleton theorem does not apply to (0.4).  If

\[
 \beta={P-a\over2},
\]

then (0.3) has cyclic gaps `(a,beta,beta)`, but (0.4) is exactly

\[
                         2a+3\beta\le A,
\]

whereas the short-singleton theorem assumes the opposite strict
inequality `A<2a+3beta`.

## 1. Fixed-sum repeated-gap coordinates

Write

\[
 y={P+a\over2},
 \qquad
 b={P-a\over2}.
\tag{1.1}
\]

Thus `a=y-b`, `P=y+b`, and

\[
 H_y(b):=\mathcal L_3(y+b;y-b,y)
\tag{1.2}
\]

satisfies

\[
                         \mathcal R_-(P,a)=H_y(b).
\tag{1.3}
\]

The complete domain (0.4) becomes

\[
 {A\over4}\le y\le {2A\over5},
 \qquad
 \max\left\{{y\over2},{A\over2}-y\right\}
 \le b\le
 \min\{y,A-2y\}.
\tag{1.4}
\]

Indeed `a<=b`, `P>=A/2`, and `P+y<=A` give respectively the three
nontrivial bounds in (1.4), and the implications reverse.

The point of these coordinates is that the old proof of the
postthreshold short-singleton theorem has an exact derivative identity
which remains valid before threshold.  Normalize

\[
 p={y+b\over A},
 \qquad
 u={y-b\over A},
 \qquad
 r={3p+u\over2}.
\tag{1.5}
\]

On (1.4),

\[
 {1\over2}\le p\le {2\over3},
 \qquad
 0\le u\le {p\over3},
 \qquad
 3p+u\le2.
\tag{1.6}
\]

In particular

\[
                         0\le u\le {1\over5}.
\tag{1.7}
\]

## 2. A retained two-period derivative

Put

\[
 h(x)=xe^{-\pi x^2/4},
 \qquad
 D(x)=h(1+x)-h(1-x).
\tag{2.1}
\]

For compact arguments,

\[
                         {K'(Ax)\over2A}=D(x),
\]

and for tail arguments the normalized derivative is `h(1+x)`.

Termwise differentiation of (1.2), justified by a Gaussian summable
majorant, gives

\[
\begin{aligned}
 H_y'(b)={}&-K'(y-b)+K'(y+b)+K'(2y+b)\\
 &+\sum_{q\ge2}\bigl(
 qK'(q(y+b))+(q-1)K'(q(y+b)+y-b)\\
 &\hspace{40mm}+qK'(q(y+b)+y)\bigr).
\end{aligned}
\tag{2.2}
\]

All terms in the sum with `q>=3` are strictly favorable tail terms.
Keeping the complete `q=2` row gives

\[
 {H_y'(b)\over2A}>J(p,u),
\tag{2.3}
\]

where

\[
\begin{aligned}
 J(p,u)={}&-D(u)+D(p)+D(r)+2h(1+2p)\\
 &+h(1+2p+u)
 +2h\left(1+{5p+u\over2}\right).
\end{aligned}
\tag{2.4}
\]

### Lemma 2.1

On (1.6),

\[
                         -D(u)\ge0.
\tag{2.5}
\]

Moreover, `D` is strictly increasing on `[3/4,1]`.

#### Proof

For `0<u<=1/5`,

\[
 {h(1+u)\over h(1-u)}
 ={1+u\over1-u}e^{-\pi u}<1.
\]

Indeed

\[
 \log{1+u\over1-u}
 \le {2u\over1-u^2}
 \le {25u\over12}<3u<\pi u.
\]

This proves (2.5), including equality at `u=0`.

Next

\[
                         D'(x)=h'(1+x)+h'(1-x).
\]

For `3/4<=x<=1`, the second summand is positive and the first is
negative.  Put `s=1-x<=1/4` and `t=1+x>=7/4`.  From
`3/4<pi/4<11/14`,

\[
 h'(s)
 =e^{-\pi s^2/4}(1-\pi s^2/2)
 >\left(1-{11\over224}\right)
   \left(1-{11\over112}\right)>{4\over5}.
\]

On `[7/4,2]`, `h''>0`, so `-h'(t)<=-h'(7/4)`.  The coarse bounds
`pi>3`, `pi<22/7`, and `e^2>7` give

\[
 -h'(t)< {37\over7}e^{-147/64}<{37\over49}<{4\over5}.
\]

Thus `D'(x)>0`.  \(\square\)

Since `r>=(3/2)p`, Lemma 2.1 gives

\[
                         D(r)\ge D(3p/2).
\tag{2.6}
\]

Every displayed tail `h` in (2.4) is decreasing in its argument.  The
largest admissible `u` is

\[
 u_*(p)=
 \begin{cases}
 p/3,&1/2\le p\le3/5,\\
 2-3p,&3/5\le p\le2/3.
 \end{cases}
\tag{2.7}
\]

Consequently

\[
 J(p,u)\ge
 \begin{cases}
 G_-(p),&1/2\le p\le3/5,\\
 G_+(p),&3/5\le p\le2/3,
 \end{cases}
\tag{2.8}
\]

where

\[
\begin{aligned}
G_-(p)={}&D(p)+D(3p/2)+2h(1+2p)\\
 &+h(1+7p/3)+2h(1+8p/3),
\end{aligned}
\tag{2.9}
\]

and

\[
\begin{aligned}
G_+(p)={}&D(p)+D(3p/2)+2h(1+2p)\\
 &+h(3-p)+2h(2+p).
\end{aligned}
\tag{2.10}
\]

## 3. Exact positivity of the two derivative strips

The identity

\[
 h''(x)={\pi\over2}x
 \left({\pi x^2\over2}-3\right)e^{-\pi x^2/4}
\tag{3.1}
\]

shows that

\[
 D''(x)=h''(1+x)-h''(1-x)>0
 \qquad(1/2\le x\le1).
\tag{3.2}
\]

Every other `h` argument in (2.9)--(2.10) is at least two, where
`h''>0`.  Therefore

\[
                         G_-''>0,
 \qquad G_+''>0
\tag{3.3}
\]

on their respective intervals.

Only two small rational Gaussian certificates are needed.  They are
included explicitly to keep the proof independent of numerical search.
For a rational `x`, bound `pi` by

\[
                         {157\over50}<\pi<{22\over7}
\]

and bound `e^{-z}` by its odd and even Taylor polynomials through degree
41.  Since the Lagrange remainder has the next alternating sign,

\[
 \sum_{j=0}^{41}{(-z)^j\over j!}<e^{-z}
 <\sum_{j=0}^{40}{(-z)^j\over j!}.
\tag{3.4}
\]

Substitution in `h(x)` and
`h'(x)=e^{-\pi x^2/4}(1-\pi x^2/2)` gives the following rational
intervals.  Each entry is a direct fraction comparison after positive
denominators are cleared.

At `p_0=23/40`:

\[
\begin{array}{c|c|c}
x&h(x)&h'(x)\\ \hline
63/40&(28/125,9/40)&(-83/200,-411/1000)\\
17/40&(46/125,37/100)&(31/50,623/1000)\\
149/80&(61/500,123/1000)&(-293/1000,-29/100)\\
11/80&(27/200,17/125)&(191/200,957/1000)\\
43/20&(7/125,29/500)&(-21/125,-41/250)\\
281/120&(31/1000,4/125)&(-13/125,-101/1000)\\
38/15&(2/125,17/1000)&(-3/50,-57/1000).
\end{array}
\tag{3.5}
\]

The value column gives

\[
\begin{aligned}
G_-(23/40)
&>{28\over125}+{61\over500}
 +2{7\over125}+{31\over1000}+2{2\over125}\\
&\quad-{37\over100}-{17\over125}
={15\over1000}>{1\over100}.
\end{aligned}
\tag{3.6}
\]

The derivative column, with coefficients
`1,1,3/2,3/2,4,7/3,16/3`, gives

\[
                         |G_-'(23/40)|<{1\over20}.
\tag{3.7}
\]

By convexity, the tangent at `23/40` is a global lower bound.  Since

\[
 \left|p-{23\over40}\right|\le{3\over40}
 \qquad(1/2\le p\le3/5),
\]

equations (3.6)--(3.7) prove

\[
                         \boxed{G_-(p)>{1\over160}>0.}
\tag{3.8}
\]

At `p=3/5`, the same Taylor certificate gives

\[
\begin{array}{c|c|c}
x&h(x)&h'(x)\\ \hline
8/5&(213/1000,43/200)&(-407/1000,-403/1000)\\
2/5&(44/125,177/500)&(329/500,331/500)\\
19/10&(111/1000,14/125)&(-69/250,-34/125)\\
1/10&(99/1000,1/10)&(39/40,489/500)\\
11/5&(49/1000,1/20)&(-149/1000,-73/500)\\
12/5&(1/40,27/1000)&(-89/1000,-17/200)\\
13/5&(3/250,7/500)&(-49/1000,-23/500).
\end{array}
\tag{3.9}
\]

It follows that

\[
                         G_+(3/5)>{17\over1000}>{1\over100}
\tag{3.10}
\]

and

\[
                         G_+'(3/5)>{1\over2}.
\tag{3.11}
\]

Since `G_+` is convex, (3.11) makes it strictly increasing on
`[3/5,2/3]`; hence

\[
                         \boxed{G_+(p)>{1\over100}>0.}
\tag{3.12}
\]

Equations (2.3), (2.8), (3.8), and (3.12) prove the main monotonicity
statement

\[
                         \boxed{H_y'(b)>0}
\tag{3.13}

on the entire prethreshold domain (1.4).

## 4. Collapse to one half-period function

The lower endpoint in (1.4) changes at `y=A/3`.

If

\[
                         {A\over3}\le y\le{2A\over5},
\]

then `b=y/2`.  Put `s=y/2`.  The three cosets become all residue
classes modulo `3s`, and therefore

\[
                         H_y(y/2)=C(s)>0.
\tag{4.1}
\]

If

\[
                         {A\over4}\le y\le{A\over3},
\]

then `b=A/2-y`, so `P=y+b=A/2`.  Put

\[
                         u={2y\over A}-{1\over2}
                         \in[0,1/6].
\tag{4.2}
\]

The remaining boundary is the single function

\[
\boxed{
 \mathcal B(u)
 =\mathcal L_3\!\left({A\over2};Au,
 A\left({1\over4}+{u\over2}\right)\right),
 \qquad0\le u\le{1\over6}.}
\tag{4.3}
\]

### Theorem 4.1 (exact one-variable reduction)

Every nonpositive value of the two-variable gate (0.3)--(0.4) forces a
nonpositive value of `mathcal B` on `[0,1/6]`.  Conversely, positivity of
`mathcal B` on that interval proves

\[
                         \mathcal R_-(P,a)>0
\]

on the complete domain (0.4).

#### Proof

For each fixed `y`, (3.13) puts the minimum at the lower endpoint of
(1.4).  The endpoint is (4.1) for `y>=A/3` and (4.3) for `y<=A/3`.
The arithmetic endpoint (4.1) is strictly positive, leaving exactly
(4.3).  \(\square\)

Both endpoints of the remaining interval are already positive.  At
`u=0`, splitting the arithmetic `A/4` lattice into even and odd residue
classes gives

\[
\begin{aligned}
 \mathcal B(0)
 &=2C(A/2)+\{C(A/4)-C(A/2)\}\\
 &=C(A/4)+C(A/2)>0.
\end{aligned}
\tag{4.4}
\]

At `u=1/6`, the three residue classes modulo `A/2` form the complete
`A/6` arithmetic lattice, so

\[
                         \mathcal B(1/6)=C(A/6)>0.
\tag{4.5}
\]

There is also an exact threshold-period expression for the interior.
Write

\[
 f(w)=F_A(w),
 \qquad
 \rho(w)=2-\sum_{j\in\mathbb Z}
                e^{-\pi(w/A-j)^2/4}.
\tag{4.6}
\]

The Jacobi reflection identity is

\[
                         f(w)+f(A-w)=\rho(w).
\tag{4.7}
\]

Since `F_{A/2}(w)=f(w)+f(A/2+w)`, formula (4.3) becomes

\[
\boxed{
\begin{aligned}
 \mathcal B(u)={}&f(0)+f(A/2)
 +f(Au)-f(A(1/2-u))\\
 &+f(A(1/4+u/2))-f(A(1/4-u/2))\\
 &+\rho(A(1/2-u))+\rho(A(1/4-u/2)).
\end{aligned}}
\tag{4.8}
\]

Thus the former two-dimensional prethreshold obstruction is now one
explicit compact theta inequality, with positive endpoints.  No
critical fibre, hidden availability pulse, or second free parameter
remains.

## 5. Consequence and exact scope

The chamber-III coupled-pulse theorem already reduces chamber III to
(0.3).  The repeated-gap upper endpoint of chamber II is the same gate.
Therefore positivity of the single function (4.3), together with the
other two chamber-II residuals, closes this shared obstruction in both
chambers.

This note proves only the reduction and strict repeated-gap monotonicity.
It does not assert that `mathcal B(u)>0` for every interior
`0<u<1/6`; it does not sign the chamber-II lower endpoint or stationary
strip; and it does not prove complete grid-six positivity, the all-grid
Bellman inequality, or an OR-word upper bound.

## 6. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| chamber-II prethreshold reduction | `MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_CHAMBER_II_PRETHRESHOLD_CRITICAL_STRIP_REDUCTION_20260804.md` | `8101f952bdfc4900f2fdd9d4b6396642c694c850cb420c7ef8dc03e24f19c1f3` |
| chamber-III pulse cancellation | `MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_CHAMBER_III_COUPLED_PULSE_CANCELLATION_20260804.md` | `4e53e83f9912b3e8ec42eacf9dff1065d71d649be5cc8f4400f0223cbba8b811` |
| reflected compact-slope theorem | `MATH_THEOREM_REFLECTED_COMPACT_SLOPE_FULL_HALF_INTERVAL_AND_ALL_GRID_AFFINE_CLOSURE_20260804.md` | `2c37dfcd8d05231cd3cd60e4babe3cf1c22b54e869f716665c08511d3fcf4c2f` |
| opposite-side short-singleton closure | `MATH_THEOREM_FIVE_SLOT_SHORT_SINGLETON_REPEATED_GAP_COMPLETE_CLOSURE_20260804.md` | `8f7e7caecfbf873d7992e34349e3d3c3cc7968ae8e8691615d193d4afa8ef992` |
| arithmetic ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |

