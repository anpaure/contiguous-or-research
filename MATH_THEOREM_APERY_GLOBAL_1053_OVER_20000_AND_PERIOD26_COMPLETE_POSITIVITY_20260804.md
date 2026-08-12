# A `1053/20000` global compact price and complete period-twenty-six positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It sharpens the global
compact-train price from `533/10000` to `1053/20000` by a concave Jacobi
envelope centered at `1/8`.  Repricing the first three reflected pairs then
closes both authenticated period-twenty-six residual chambers, including
depths eleven and twelve.  No search, solver, sampled computation, or
numerical optimization is used.

Put

\[
A={\sqrt\pi\over2},
\qquad
f(x)=F_A(Ax),
\qquad
\varepsilon={1\over20000}.
\tag{0.1}
\]

On `0<=x<=2/13`, Jacobi completion gives

\[
f(x)=1-\Theta(x)+J(x),
\qquad
|\Theta(x)-2|<\varepsilon,
\tag{0.2}
\]

where

\[
J(x)=e^{-\pi x^2/4}
+\sum_{j\ge2}e^{-\pi(j-x)^2/4}.
\tag{0.3}
\]

## 1. Uniform strict concavity of the Jacobi positive part

For `t>=0`, write

\[
Q(t)=\left({\pi^2t^2\over4}-{\pi\over2}\right)e^{-\pi t^2/4}.
\tag{1.1}
\]

Then

\[
J''(x)=Q(x)+\sum_{j\ge2}Q(j-x).
\tag{1.2}
\]

For later finite certificates, put

\[
 P_n(z)=\sum_{r=0}^n{z^r\over r!},
 \qquad
 U_n(z)=\sum_{r=0}^{n-1}{z^r\over r!}
 +{z^n\over n!\,(1-z/(n+1))}
 \quad(0\le z<n+1).
\tag{1.2a}
\]

Positive-term comparison gives `P_n(z)<e^z<U_n(z)` for `z>0`.

### Lemma 1.1

For `0<=x<=2/13`,

\[
\boxed{J''(x)<-{1\over2}.}
\tag{1.3}
\]

#### Proof

Differentiation gives

\[
 Q'(t)={\pi^2t\over8}(6-\pi t^2)e^{-\pi t^2/4}.
\tag{1.3a}
\]

Thus `Q` is increasing on `[0,2/13]`, while it is positive and decreasing
on `[24/13,infinity)`.  Direct rational Gaussian bounds using
`pi_-=333/106<pi<355/113=pi_+` give

\[
Q(x)<-{7\over5}.
\tag{1.4}
\]

Hence the first positive term satisfies

\[
Q(2-x)\le Q(24/13)<{1\over2}.
\tag{1.5}
\]

The same monotonicity, followed by a geometric tail bound, gives

\[
\sum_{j\ge3}Q(j-x)<{1\over20}.
\tag{1.6}
\]

For a literal finite certificate, the negative endpoint follows from

\[
 {\pi_-/2-\pi_-^2/169\over U_1(\pi_+/169)}>{7\over5}.
\tag{1.6a}
\]

For the positive endpoints, direct cross multiplication gives

\[
 {\pi_+^2t^2/4-\pi_+/2\over P_n(\pi_-t^2/4)}<c
\tag{1.6b}
\]

for

\[
 (t,n,c)=
 (24/13,5,1/2),\quad
 (37/13,8,1/25),\quad
 (50/13,7,1/200).
\tag{1.6c}
\]

Finally, for `t>=50/13`,

\[
 {Q(t+1)\over Q(t)}
 ={\pi(t+1)^2/2-1\over\pi t^2/2-1}
 e^{-\pi(2t+1)/4}<{1\over2}.
\tag{1.6d}
\]

Indeed both factors decrease with `t`, the rational factor at `50/13`
is below `2` after replacing `pi` by `pi_-`, and
`P_1(pi_-(2(50/13)+1)/4)>4`.  Therefore the tail beginning at
`Q(50/13)` is below

\[
 {1/200\over1-1/2}={1\over100}.
\tag{1.6e}
\]

In particular, the endpoint comparisons are

\[
Q(2/13)<-{7\over5},
\qquad
Q(24/13)<{1\over2},
\qquad
Q(37/13)<{1\over25},
\tag{1.7}
\]

and the last tail is below `1/100`.  Equations (1.6a)--(1.6e) are explicit
finite rational certificates for these statements.  Combining
(1.4)--(1.6),

\[
J''(x)<-{7\over5}+{1\over2}+{1\over20}
=-{17\over20}<-{1\over2}.
\]

This proves the lemma. \(\square\)

## 2. A certified tangent at one eighth

At `x_0=1/8`, the terms in (0.3) have exponents

\[
{\pi\over256},
\quad {225\pi\over256},
\quad {529\pi\over256},
\quad {961\pi\over256},\ldots.
\]

Finite positive Taylor lower bounds for the reciprocal exponentials give

\[
e^{-\pi/256}<{98781\over100000},
\qquad
e^{-225\pi/256}<{6324\over100000},
\tag{2.1}
\]

\[
e^{-529\pi/256}<{152\over100000},
\qquad
e^{-961\pi/256}<{1\over100000},
\tag{2.2}
\]

and the remaining tail is below `1/1000000`.  Therefore

\[
\boxed{J(1/8)<{1052581\over1000000}.}
\tag{2.3}
\]

For an explicit certificate, the four lower exponents obtained from
`pi>333/106` are

\[
{333\over27136},
\quad {74925\over27136},
\quad {176157\over27136},
\quad {320013\over27136}.
\tag{2.3a}
\]

Positive Taylor polynomials of degrees two, fourteen, twenty, and
twenty-two exceed respectively

\[
{100000\over98781},
\quad {100000\over6324},
\quad {100000\over152},
\quad 100000.
\]

The first omitted exponent is larger than `506493/27136`; a degree-eighteen
positive Taylor bound and a geometric successor ratio give the stated
`1/1000000` tail.

More explicitly,

\[
 {1\over P_{18}(506493/27136)}{1\over1-1/100}
 <{1\over1000000}.
\tag{2.3b}
\]

The successor ratio is below `1/100`; for the weighted derivative tail the
larger ratio is already certified by

\[
 {47/39\over P_3(14319/1696)}<{1\over100},
\qquad
 {39/8\over P_{18}(506493/27136)}{1\over1-1/100}
 <{1\over1000000}.
\tag{2.3c}
\]

Differentiating (0.3) gives

\[
J'(1/8)={\pi\over2}
\left[
-{1\over8}e^{-\pi/256}
+\sum_{j\ge2}\left(j-{1\over8}\right)
e^{-\pi(j-1/8)^2/4}
\right].
\tag{2.4}
\]

The same positive-denominator Taylor bounds, retaining terms through
`j=4` and bounding the remaining derivative tail geometrically, give the
strict two-sided certificate

\[
\boxed{-{1\over1000}<J'(1/8)<0.}
\tag{2.5}
\]

Concretely, the needed Gaussian brackets are

\[
{98780\over100000}<e^{-\pi/256}<{98781\over100000},
\]

\[
{6321\over100000}<e^{-225\pi/256}<{6324\over100000},
\]

\[
{151\over100000}<e^{-529\pi/256}<{152\over100000},
\qquad
{7\over1000000}<e^{-961\pi/256}<{10\over1000000},
\tag{2.5a}
\]

and the weighted derivative tail after `j=4` is below `1/1000000`.
The four lower Gaussian bounds follow, with no decimal approximation, from

\[
\begin{aligned}
U_1((1/256)\pi_+)&<{100000\over98780},&
U_8((225/256)\pi_+)&<{100000\over6321},\\
U_{12}((529/256)\pi_+)&<{100000\over151},&
U_{15}((961/256)\pi_+)&<{1000000\over7}.
\end{aligned}
\tag{2.5b}
\]

Substitution in the square bracket `B` in (2.4) gives the exact rational
enclosure

\[
 -{4713\over8000000}<B<-{1961\over4000000}<0.
\tag{2.5c}
\]

Since `333/212<pi/2<355/226`,

\[
 J'(1/8)>{355\over226}\left(-{4713\over8000000}\right)
 =-{334623\over361600000}>-{1\over1000},
\]

while the upper enclosure in (2.5c) gives `J'(1/8)<0`.  This proves
(2.5) by direct cross multiplication.

All estimates in this section are literal rational cross multiplications;
no location of the maximizer is assumed.

## 3. The improved global price

Lemma 1.1 implies, for every `x` in `[0,2/13]`,

\[
J(x)\le J(1/8)+J'(1/8)(x-1/8)-{1\over4}(x-1/8)^2.
\tag{3.1}
\]

The maximum of the last two terms over the whole real line is
`J'(1/8)^2`.  Equations (2.3) and (2.5) therefore give

\[
J(x)<{1052582\over1000000}.
\tag{3.2}
\]

Using (0.2),

\[
f(x)<J(x)-1+\varepsilon
<{52632\over1000000}
<{1053\over20000}
\qquad(0\le x\le2/13).
\tag{3.3}
\]

The last comparison has the exact fail-closed margin

\[
 {1053\over20000}-{52632\over1000000}
 ={18\over1000000}>0.
\tag{3.3a}
\]

On `[2/13,1/2]`, the authenticated period-twenty-six monotonicity and
anchor give

\[
f(x)\le f(2/13)<{523\over10000}<{1053\over20000}.
\tag{3.4}
\]

Thus

\[
\boxed{
f(x)<G_*:={1053\over20000}
\qquad(0\le x\le1/2).}
\tag{3.5}
\]

## 4. Repricing the two residual chambers

The authenticated period-twenty-six residual proof used the old global
price

\[
G={533\over10000}={1066\over20000}
\]

on exactly the first three far endpoints.  Replacing it by `G_*` gains

\[
3(G-G_*)
=3\,{13\over20000}
={1950\over1000000}.
\tag{4.1}
\]

On chamber `R_6`, replace the first three nonnegative price slacks
`G-f(Y_i)` by `G_*-f(Y_i)`.  The exact residual identity becomes

\[
\boxed{
E(s)={68\over1000000}+\mathcal S_6^*,
\qquad \mathcal S_6^*\ge0.}
\tag{4.2}
\]

Indeed `-1882+1950=68`.

Formally, `mathcal S_6^*` is the slack functional `mathcal S_6` of the
authenticated residual theorem with only `R_1,R_2,R_3` changed from `G`
to `G_*`; all other rows are identical.  Each changed summand is

\[
 f(X_i)-L+G_*-f(Y_i)\ge0
\]

by the compact floor and the global price (strictness is not needed here).

Likewise chamber `R_7` becomes

\[
\boxed{
E(s)={302\over1000000}+\mathcal S_7^*,
\qquad \mathcal S_7^*\ge0,}
\tag{4.3}
\]

because `-1648+1950=302`.  No middle-train, overlap-depth, or theta credit
is spent in either closure.

Likewise `mathcal S_7^*` changes only `R_1,R_2,R_3`; its fourth through
seventh price rows and every theta, middle-train, and later-pair summand
are untouched.  Thus (4.2)--(4.3) are literal repricings of the frozen
identities, not new lower-bound ledgers.

## 5. Complete period-twenty-six theorem

### Theorem 5.1

Every honest exact-first-carry period-twenty-six cyclic Apéry clock
satisfies

\[
\boxed{\Phi(W)>0.}
\tag{5.1}
\]

#### Proof

The authenticated period-twenty-six reduction closes every chamber outside
`R_6` and `R_7`.  Equations (4.2)--(4.3) close those two residual chambers
with strict positive margins.  Finally `Phi(W)>=E(s)`. \(\square\)

## 6. Scope and frozen dependencies

This theorem concerns only honest exact-first-carry formal cyclic Apéry
clocks of period twenty-six.  It does not address overshoot, later first
crossing, finite physical shoulders, arbitrary periods, or an OR-word
construction.

| role | file | SHA-256 |
|---|---|---|
| authenticated period-26 chamber reduction and `2/13` monotonicity | `MATH_THEOREM_APERY_PERIOD26_SHARP_DEPTH_AND_TWO_RESIDUAL_THRESHOLD_CHAMBERS_20260804.md` | `15777eb5978671af4ce685f9760fc1c2a1cef25e424cafe7deda8bc004cdee2f` |
| Jacobi completion and theta bound | `MATH_THEOREM_APERY_PERIOD25_SHARP_GLOBAL_PRICE_AND_THRESHOLD_RAY_COMPLETE_POSITIVITY_20260804.md` | `61265fdf0e355aae0c6c786f9725ee639a427a1efb866fa21191ccb7b575653a` |
