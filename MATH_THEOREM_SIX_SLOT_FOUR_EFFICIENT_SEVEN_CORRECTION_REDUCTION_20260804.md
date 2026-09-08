# Six-slot size-four-efficient clocks: three Apéry maxima and seven corrections

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It collapses the
twelve eventual Apéry forms in the six-slot `h=4` branch to three correlated
maxima and proves that the entire availability head has only seven possible
corrections.  It closes the threshold endpoint face, but it does not sign
the three inert endpoint faces or prove complete six-slot positivity.

Put

\[
 A={\sqrt\pi\over2}.
\]

Write a normalized six-slot `h=4` table as

\[
 (c_0,\ldots,c_6)=(0,x,y,z,P,P+u,P+v).
\tag{0.1}
\]

The canonical branch constraints include

\[
 {2A\over3}\le P<A,
 \qquad
 0\le x,y,z,
 \qquad
 0\le u<A-P\le v,
 \qquad
 x\le u,
 \qquad
 y\le v,
 \qquad
 z\le {3P\over4},
 \qquad
 u\le {P\over4},
 \qquad
 v\le {P\over2}.
\tag{0.2}
\]

Endpoint saturation is exactly

\[
 \boxed{
 v=\max\{A-P,x+u,y,2z-P\}.}
\tag{0.3}
\]

For a period `P`, write

\[
 \mathcal L_4(P;s_1,s_2,s_3)
 =\sum_{q\ge0}\sum_{r=0}^{3}K(qP+s_r),
 \qquad s_0=0.
\tag{0.4}
\]

## 1. The twelve forms collapse to three maxima

Set the reduced weights

\[
 d_1=u-{P\over4},
 \qquad
 d_2=v-{P\over2},
 \qquad
 d_3=z-{3P\over4}.
\tag{1.1}
\]

All three are nonpositive.  Moreover endpoint superadditivity gives

\[
                         d_2\ge2d_3,
\tag{1.2}
\]

because `v>=2z-P`.

The canonical four-state Apéry theorem gives four displayed linear forms
for each nonzero residue.  Under (1.1)--(1.2), their maxima simplify to

\[
 \boxed{
 s_1=\max\{u,v+z-P\},}
\tag{1.3}
\]

\[
 \boxed{
 s_2=\max\{v,2u\},}
\tag{1.4}
\]

and

\[
 \boxed{
 s_3=\max\{z,u+s_2\}.}
\tag{1.5}

#### Proof

For residue one, the four reduced forms are

\[
 d_1,\quad d_2+d_3,\quad d_1+2d_2,\quad3d_3.
\]

The third is at most `d_1`, while (1.2) makes the fourth at most the
second.  Adding `P/4` gives (1.3).

For residue two, the forms are

\[
 d_2,\quad2d_1,\quad2d_3,\quad d_1+d_2+d_3.
\]

Equation (1.2) makes `2d_3<=d_2`, and nonpositivity gives
`d_1+d_2+d_3<=d_2`.  Adding `P/2` gives (1.4).

For residue three, the forms are

\[
 d_3,\quad d_1+d_2,\quad3d_1,\quad2d_2+d_3.
\]

The last is at most `d_3`.  Adding `3P/4` leaves

\[
 z,\qquad u+v,\qquad3u,
\]

whose last two have maximum `u+s_2`.  This proves (1.5). \(\square\)

## 2. Exact seven-correction head

Define

\[
 g=\max\{z,u+y,v+x\},
 \qquad
 h=\max\{z,u+v\}.
\tag{2.1}
\]

### Theorem 2.1

The exact Bellman functional is

\[
\boxed{
\begin{aligned}
 \Phi={}&\mathcal L_4(P;s_1,s_2,s_3)\\
 &+K(x)-K(s_1)
  +K(y)-K(s_2)
  +K(z)-K(s_3)\\
 &+K(P+u)-K(P+s_1)
  +K(P+v)-K(P+s_2)\\
 &+K(P+g)-K(P+s_3)\\
 &+K(2P+h)-K(2P+s_3).
\end{aligned}}
\tag{2.2}
\]

There are no other availability corrections.

#### Proof

The formal four-coset clock has values `qP+s_r`.  At capacities one, two,
and three the actual values are `x,y,z`.  Capacity four is `P`.  At
capacities five and six the actual values are `P+u,P+v`.  At capacity
seven, the maximal decompositions give

\[
 V_7=P+\max\{z,u+y,v+x\}=P+g.
\]

Capacities eight, nine, and ten already realize the stabilized values:

* at eight, two period generators give `2P`;
* at nine, either `P+(P+u)` realizes `2P+u`, or `(P+v)+z`
  realizes `P+v+z`; these are exactly the two forms in (1.3);
* at ten, `P+(P+v)` and `2(P+u)` realize exactly (1.4).

At capacity eleven, the representatives available for residue three give

\[
                         V_{11}=2P+\max\{z,u+v\}=2P+h.
\]

The possible third stable form `3u` first becomes available from three
size-five generators at capacity fifteen.  From capacity twelve onward,
the residue-zero value is `3P`; capacities thirteen and fourteen realize
all forms in (1.3)--(1.4), and capacity fifteen realizes all forms in
(1.5).  Padding by size-four period generators proves equality thereafter.
Subtracting the formal values at the seven exceptional capacities gives
(2.2). \(\square\)

## 3. Three early corrections are favorable

One has

\[
                         x\le s_1,
 \qquad y\le s_2,
 \qquad z\le s_3.
\tag{3.1}
\]

Indeed `x<=u<=s_1`, endpoint saturation gives `y<=v<=s_2`, and (1.5)
contains `z`.  All six arguments in the first correction row of (2.2) lie
in `[0,3A/4]`: each `s_r<=rP/4` because its reduced Apéry weight is
nonpositive, and `P<A`.  Since `K` decreases on this compact interval,

\[
 K(x)-K(s_1)\ge0,
 \qquad
 K(y)-K(s_2)\ge0,
 \qquad
 K(z)-K(s_3)\ge0.
\tag{3.2}
\]

Thus only the final four corrections in (2.2) can be adverse.

## 4. Endpoint faces

Equation (0.3) gives exactly four endpoint faces:

\[
\begin{array}{ll}
\mathrm T:&v=A-P,\\
\mathrm X:&v=x+u,\\
\mathrm Y:&v=y,\\
\mathrm Z:&v=2z-P.
\end{array}
\tag{4.1}
\]

On the threshold face `T`, one has `c_6=A`.  The literal endpoint-period
comparison and the audited subcomplementary-pair theorem give

\[
                         \boxed{\Phi>{163\over70000}>0.}
\tag{4.2}
\]

This conclusion does not require size six to be the maximum-density
denomination; its proof uses only `c_6=A`, internal superadditivity, and the
literal period-six comparison.

The inert faces `X,Y,Z` retain the four later corrections

\[
\begin{aligned}
 &K(P+u)-K(P+s_1),
 &&K(P+v)-K(P+s_2),\\
 &K(P+g)-K(P+s_3),
 &&K(2P+h)-K(2P+s_3).
\end{aligned}
\tag{4.3}
\]

Their correlated sign is the exact remaining `h=4` analytic gate.

## 5. Scope and frozen dependencies

This theorem reduces the complete normalized `h=4` branch to three inert
endpoint faces with four explicitly priced late corrections.  It does not
claim those faces positive.

| role | file | SHA-256 |
|---|---|---|
| canonical six-slot normal forms | `MATH_THEOREM_SIX_SLOT_CANONICAL_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md` | `3b537980a6f18aae936979335cc6756079ff10b92a80019acf3a97df8be9bede` |
| canonical-form audit | `MATH_AUDIT_SIX_SLOT_CANONICAL_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_INDEPENDENT_20260804.md` | `fae9fe02688d666e956619abe40698791a4146004a59a483893d0634ebbe3006` |
| compact kernel monotonicity | `MATH_THEOREM_FIVE_SLOT_TWO_EFFICIENT_SMALL_PERIOD_WEDGE_CLOSURE_20260804.md` | `a678fc5a33c6457d9d640aa963d902fdb8c7ed932ade6a14fd320caf8d285e43` |
| endpoint subcomplementary-pair closure | `MATH_THEOREM_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_20260804.md` | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |
| independent endpoint audit | `MATH_AUDIT_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_INDEPENDENT_20260804.md` | `1045aba0ab3a372f0e822f9e61702e600240c73eee61faa1916676a4790c7f8b` |
