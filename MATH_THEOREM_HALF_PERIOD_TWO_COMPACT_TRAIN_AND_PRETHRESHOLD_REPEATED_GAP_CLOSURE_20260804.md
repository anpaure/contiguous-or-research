# The half-period two-compact train decreases: closure of the prethreshold repeated-gap gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves the final
one-variable half-period function from the prethreshold repeated-gap
reduction strictly positive.  Consequently it closes the shared
prethreshold repeated-gap obstruction in six-slot `h=3` chambers II and
III.  It does not sign the two other chamber-II residuals, chamber I, the
complete six-slot problem, or any all-grid statement.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 h(x)=xe^{-\pi x^2/4},
\tag{0.1}
\]

and

\[
 F_P(w)=\sum_{q\ge0}K(qP+w).
\tag{0.2}
\]

The preceding exact reduction leaves only

\[
 \mathcal B(u)
 =\mathcal L_3\!\left({A\over2};Au,
 A\left({1\over4}+{u\over2}\right)\right),
 \qquad0\le u\le{1\over6}.
\tag{0.3}
\]

We prove a stronger monotonicity statement for the individual train
`F_(A/2)`.

## 1. The exact derivative

### Theorem 1.1 (half-period two-compact monotonicity)

For every

\[
                         0\le w\le {A\over3},
\]

one has

\[
                         \boxed{F_{A/2}'(w)<0.}
\tag{1.1}
\]

#### Proof

Write `w=Ax`.  Since `0<=x<=1/3`, the rows `q=0,1` are compact and all
later rows are Gaussian tails.  The exact two-compact derivative formula
is

\[
 {F_{A/2}'(Ax)\over2A}=T(x),
\tag{1.2}
\]

where

\[
 \boxed{
 T(x)=\sum_{q\ge0}h\left(1+x+{q\over2}\right)
       -h(1-x)-h\left({1\over2}-x\right).}
\tag{1.3}
\]

Termwise differentiation is justified uniformly by a Gaussian summable
majorant.

We first prove that `T` is strictly convex.  Direct differentiation gives

\[
 h''(z)={\pi\over2}z
 \left({\pi z^2\over2}-3\right)e^{-\pi z^2/4}
\tag{1.4}
\]

and

\[
 h'''(z)={\pi\over2}e^{-\pi z^2/4}
 \left(-4\eta^2+12\eta-3\right),
 \qquad \eta={\pi z^2\over4}.
\tag{1.5}
\]

The two roots of the quadratic in (1.5) are

\[
                         {3-\sqrt6\over2},
 \qquad {3+\sqrt6\over2}.
\]

For `2/3<=z<=4/3`, the classical bounds `3<pi<22/7` give

\[
 {3-\sqrt6\over2}< {1\over3}
 <\eta<{88\over63}< {3+\sqrt6\over2}.
\]

Thus `h'''(z)>0` throughout `[2/3,4/3]`, and hence

\[
                         h''(1+x)-h''(1-x)\ge0
 \qquad(0\le x\le1/3).
\tag{1.6}
\]

Every summand `h''(1+x+q/2)` with `q>=1` is positive, because its
argument is at least `3/2` and `pi(3/2)^2/2>3`.  Also

\[
 h''(1/2-x)<0
 \qquad(0\le x\le1/3).
\]

Therefore

\[
\begin{aligned}
 T''(x)={}&h''(1+x)-h''(1-x)\\
 &+\sum_{q\ge1}h''\left(1+x+{q\over2}\right)
 -h''\left({1\over2}-x\right)>0.
\end{aligned}
\tag{1.7}
\]

It remains to sign the two endpoints.  At zero,

\[
 T(0)=\sum_{n\ge0}h\left({3\over2}+{n\over2}\right)-h(1/2).
\tag{1.8}
\]

For `z>=2`, successive terms spaced by `1/2` have ratio

\[
 {h(z+1/2)\over h(z)}
 =\left(1+{1\over2z}\right)
 e^{-(\pi/4)(z+1/4)}
 \le {5\over4}e^{-9\pi/16}<{1\over4}.
\tag{1.9}
\]

For the last inequality, `pi>3` and the positive exponential series give
`e^(27/16)>5`.  Hence

\[
 T(0)<h(3/2)+{4\over3}h(2)-h(1/2).
\tag{1.10}
\]

After division by `h(1/2)>0`, the right side is negative precisely when

\[
                         3e^{-\pi/2}
 +{16\over3}e^{-15\pi/16}<1.
\tag{1.11}
\]

The positive Taylor series at `157/100` gives

\[
                         e^{\pi/2}>{9\over2},
\]

and the elementary estimates

\[
 e^2>{331\over45},
 \qquad
 e^{13/16}>{54853\over24576}
\]

give `e^(15pi/16)>e^(45/16)>16`.  The two terms in (1.11) are therefore
strictly less than `2/3` and `1/3`, respectively.  Thus

\[
                         T(0)<0.
\tag{1.12}
\]

At the other endpoint,

\[
 T(1/3)=\sum_{q\ge0}h\left({4\over3}+{q\over2}\right)
          -h(2/3)-h(1/6).
\tag{1.13}
\]

For `z>=7/3`, the analogous successive ratio obeys

\[
 {h(z+1/2)\over h(z)}
 \le {17\over14}e^{-31\pi/48}<{1\over5}.
\tag{1.14}
\]

Indeed `pi>3`, `e>8/3`, and `e^(15/16)>12/5` give

\[
 e^{31\pi/48}>e^{31/16}
 >{32\over5}>{85\over14}.
\]

Consequently

\[
 \sum_{q\ge0}h\left({4\over3}+{q\over2}\right)
 <h(4/3)+h(11/6)+{5\over4}h(7/3).
\tag{1.15}
\]

The middle term is smaller than `h(1/6)`, because

\[
 {h(11/6)\over h(1/6)}=11e^{-5\pi/6}<1.
\tag{1.16}
\]

For example, `pi>3`, `e^2>331/45`, and `e^(1/2)>3/2` give
`e^(5pi/6)>e^(5/2)>11`.

The first and last terms in (1.15) are together smaller than `h(2/3)`.
Indeed, after division by `h(2/3)`, it is enough that

\[
 2e^{-\pi/3}+{35\over8}e^{-5\pi/4}<1.
\tag{1.17}
\]

Here `e^(pi/3)>e>8/3`, so the first term is less than `3/4`; and
`e^(5pi/4)>e^(15/4)>20>35/2`, so the second is less than `1/4`.
Equations (1.15)--(1.17) prove

\[
                         T(1/3)<0.
\tag{1.18}
\]

A convex function lies below the chord joining its endpoint values.
Equations (1.7), (1.12), and (1.18) therefore give

\[
                         T(x)<0
 \qquad(0\le x\le1/3).
\]

Together with (1.2), this proves (1.1).  \(\square\)

## 2. Positivity of the final one-variable function

### Theorem 2.1

For every `0<=u<=1/6`,

\[
                         \boxed{\mathcal B(u)>0.}
\tag{2.1}
\]

#### Proof

From (0.3),

\[
 \mathcal B(u)=F_{A/2}(0)+F_{A/2}(Au)
 +F_{A/2}\!\left(A\left({1\over4}+{u\over2}\right)\right).
\tag{2.2}
\]

Both moving arguments lie in `[0,A/3]`.  Theorem 1.1 gives

\[
\begin{aligned}
 \mathcal B'(u)={}&A F_{A/2}'(Au)\\
 &+{A\over2}F_{A/2}'\!\left(
 A\left({1\over4}+{u\over2}\right)\right)<0.
\end{aligned}
\tag{2.3}
\]

Thus `mathcal B` is strictly decreasing.  At its right endpoint, its
three residue classes modulo `A/2` form the complete arithmetic `A/6`
lattice, so

\[
                         \mathcal B(1/6)=C(A/6)>0
\tag{2.4}
\]

by strict arithmetic-ceiling positivity.  Hence

\[
                         \mathcal B(u)\ge\mathcal B(1/6)>0.
\]

This proves (2.1).  \(\square\)

## 3. Closure of the shared six-slot gate

Combining Theorem 2.1 with the exact half-period reduction gives the
following.

### Corollary 3.1 (prethreshold repeated-gap closure)

For

\[
 {A\over2}\le P<{2A\over3},
 \qquad
 0\le a\le {P\over3},
 \qquad
 3P+a\le2A,
\]

one has

\[
 \boxed{
 \mathcal L_3\!\left(P;a,{P+a\over2}\right)>0.}
\tag{3.1}
\]

This is exactly the repeated-gap upper endpoint in chamber II.  Under
the chamber-III coordinates

\[
 P=c+2\beta,
 \qquad a=c,
 \qquad {P+a\over2}=c+\beta,
\]

it is also exactly the pulse-free residual

\[
                         \mathcal L_3(c+2\beta;c,c+\beta).
\]

Thus the common prethreshold scalar obstruction in both chambers is
closed.

## 4. Exact scope

This theorem does not close the complete chamber-II gate: its lower
endpoint `mathcal P_-(p,a)` and its stationary two-compact strip remain
separate residuals.  It also does not address chamber I, arbitrary
six-slot tables, larger grids, the configuration-dual inequality, or an
OR-word upper bound.

## 5. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| exact two-variable to half-period reduction | `MATH_THEOREM_SIX_SLOT_PRETHRESHOLD_REPEATED_GAP_HALF_PERIOD_REDUCTION_20260804.md` | `c7479855908547c4d18ccc139d0df6880bb73905f93b7b9ba26683a841636286` |
| arithmetic ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |

