# Six-slot full affine setup-cost family: closure by reflected-slope monotonicity

**Date:** 2026-08-04
**Status:** unconditional pure-mathematical theorem.  It proves every member
of the six-slot affine setup-cost no-descent family strictly positive, not
only its balanced member.  It makes no claim for the full six-slot `h=5`
branch or for the analogous affine family in arbitrary grid size.

Put

\[
                         A={\sqrt\pi\over2},
\]

and let `K` be the Rayleigh signed-tail kernel.  For `0<beta<A/4`, the
six-slot affine setup-cost table is

\[
 c_j=\alpha j-\beta\quad(1\le j<6),\qquad c_6=A,
 \qquad \alpha={A+2\beta\over6}.
\tag{0.1}
\]

Its exact Bellman clock is

\[
 V_m=\alpha m-\beta\left\lceil{m\over5}\right\rceil.
\tag{0.2}
\]

## Theorem

Every table (0.1) has

\[
                         \boxed{\sum_{m\ge0}K(V_m)>0.}
\tag{0.3}
\]

More precisely, after parametrizing the family by `t=c_1/A`, its
functional is strictly decreasing on `0<t<=1/6`, and its minimum on the
closed interval is the strictly positive arithmetic ceiling clock

\[
                         C(A/6)=\sum_{m\ge0}K(mA/6)>0.
\tag{0.4}
\]

## 1. Gap coordinates and the complete clock

Put

\[
 x=c_1=\alpha-\beta,
 \qquad t={x\over A}.
\tag{1.1}
\]

Solving `A=6alpha-2beta` and `x=alpha-beta` gives

\[
 \alpha={A-2x\over4},\qquad
 \beta={A-6x\over4}.
\tag{1.2}
\]

Thus

\[
 0<\beta<{A\over4}
 \quad\Longleftrightarrow\quad
 0<t<{1\over6}.
\tag{1.3}
\]

Adjoin the harmless endpoint `t=1/6`, corresponding to `beta=0`.  Define

\[
 a={\alpha\over A}={1-2t\over4},
 \qquad p={c_5\over A}=1-t.
\tag{1.4}
\]

For `m=5q+r`, `0<=r<5`, formula (0.2) becomes

\[
 {V_{5q+r}\over A}=qp+s_r,
\tag{1.5}
\]

where

\[
 (s_0,s_1,s_2,s_3,s_4)
 =\left(0,t,{1\over4}+{t\over2},{1\over2},
                {3\over4}-{t\over2}\right).
\tag{1.6}
\]

Equivalently, the cyclic gaps are

\[
                         (t,a,a,a,a).
\tag{1.7}
\]

Write

\[
 \Phi(t)=\sum_{q\ge0}\sum_{r=0}^{4}K\bigl(A(qp+s_r)\bigr).
\tag{1.8}
\]

## 2. Exact slope table

Differentiating the five normalized arguments in (1.5) gives

\[
\begin{array}{c|ccccc}
r&0&1&2&3&4\\ \hline
{d\over dt}(qp+s_r)&-q&1-q&{1\over2}-q&-q&-{1\over2}-q.
\end{array}
\tag{2.1}
\]

Termwise differentiation of (1.8) is valid uniformly on
`0<=t<=1/6`: after finitely many compact terms, the derivative summands
are bounded by a constant times
`(q+1)^2 exp(-c(q+1)^2)` for an absolute `c>0`.

We partition every term of the derivative as follows.

### 2.1 The first reflected pair

The terms `(q,r)=(0,1)` and `(1,0)` have arguments `t` and `1-t`, and
slopes `1` and `-1`.  Their total derivative is

\[
 A\{K'(At)-K'(A(1-t))\}<0.
\tag{2.2}
\]

Indeed `0<=t<=1/6<=1/3`, and the authenticated reflected compact-slope
lemma gives

\[
                         K'(A(1-t))>K'(At).
\tag{2.3}
\]

### 2.2 The second reflected pair

Put

\[
                         u={1\over4}+{t\over2}.
\tag{2.4}
\]

Then `1/4<=u<=1/3`, while `s_4=1-u`.  The terms `(0,2)` and `(0,4)`
have opposite slopes `1/2` and `-1/2`; hence their derivative is

\[
 {A\over2}\{K'(Au)-K'(A(1-u))\}<0
\tag{2.5}
\]

by the same reflected compact-slope lemma.

### 2.3 The stationary terms

Exactly three terms in the compact/first-period portion are stationary:

\[
 (q,r)=(0,0),\qquad(0,3),\qquad(1,1).
\tag{2.6}
\]

Their normalized arguments are respectively `0`, `1/2`, and
`p+t=1`, and their contribution to `Phi'(t)` is zero.

### 2.4 Every remaining term is a favorable tail term

For `q=1` and `r=2,3,4`, the smallest remaining argument is

\[
 p+s_2=1+{1-2t\over4}>1,
\tag{2.7}
\]

and the corresponding slopes are `-1/2,-1,-3/2`.

For `q>=2`, every argument is larger than one because

\[
 qp+s_r\ge2p\ge{5\over3}>1,
\tag{2.8}
\]

and all five slopes in (2.1) are strictly negative.  On the Gaussian
tail,

\[
 K'(y)=2(A+y)e^{-(A+y)^2}>0\qquad(y>A).
\tag{2.9}
\]

Thus every remaining derivative summand is strictly negative.

The partition (2.2), (2.5), (2.6), and (2.7)--(2.9) is exhaustive.
Consequently

\[
                         \boxed{\Phi'(t)<0
                         \quad(0<t\le1/6).}
\tag{2.10}
\]

## 3. The uniform endpoint

At `t=1/6`, equation (1.4) gives `a=1/6`, and (1.6) becomes

\[
                         s_r={r\over6}\qquad(0\le r<5),
 \qquad p={5\over6}.
\tag{3.1}
\]

Therefore the arguments in (1.8) are

\[
 A(qp+s_r)={A(5q+r)\over6}.
\]

As `(q,r)` ranges over `q>=0`, `0<=r<5`, the integer `5q+r` ranges
over every nonnegative integer exactly once.  Hence

\[
                         \Phi(1/6)=C(A/6)>0
\tag{3.2}
\]

by the strict reciprocal-ceiling theorem.

Since `Phi` is strictly decreasing,

\[
                         \Phi(t)>\Phi(1/6)>0
 \qquad(0<t<1/6).
\tag{3.3}
\]

This proves (0.3). \(\square\)

## 4. Scope

The theorem closes the complete one-parameter affine setup-cost family at
grid six.  In particular it strictly contains the previously closed
balanced point `beta=A/10`.

It does **not** close every six-slot `h=5` table: a general member of that
branch need not have four equal long gaps or an empty availability head.
It also does not claim the same monotonicity in arbitrary grid size.  The
reflected compact-slope theorem used here is authenticated only when the
smaller reflected argument is at most `1/3`; the additional reflected
pairs in larger grids can approach `1/2`.

## 5. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| affine setup-cost clock and exact Apéry form | `MATH_THEOREM_AFFINE_SETUP_COST_FIRST_CROSSING_AND_APERY_NO_DESCENT_20260804.md` | `408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce` |
| reflected compact-slope inequality | `MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_WY_SECOND_BOUNDARY_CLOSURE_20260804.md` | `6a44b458c013e3c553be3925f9439960b139262175aaf79bbb9fb50054f6c7d7` |
| strict reciprocal-ceiling margin | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |
