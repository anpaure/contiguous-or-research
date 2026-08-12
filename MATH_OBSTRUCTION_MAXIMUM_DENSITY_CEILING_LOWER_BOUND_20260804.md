# Obstruction: the maximum-density ceiling is not a Bellman lower bound

**Date:** 2026-08-04  
**Status:** exact symbolic counterexample.  No numerical search is used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 C(h)=\sum_{m\ge0}K(mh),                            \tag{0.1}
\]

where `K` is the Rayleigh signed-tail kernel.  A tempting strengthening of
Bellman positivity is

\[
 \Phi(c):=\sum_{m\ge0}K(V_m)\stackrel{?}{\ge}C(\lambda),
 \qquad
 \lambda=\max_j{c_j\over j}.                        \tag{0.2}
\]

This is false, even when the discrepancy from the arithmetic clock is a
single finite transient.

## 1. An exact interval on which `K` increases

For `0<u<A`, put `t=u/A`.  Direct differentiation gives

\[
 K'(u)=2\bigl((A+u)e^{-(A+u)^2}
                 -(A-u)e^{-(A-u)^2}\bigr).          \tag{1.1}
\]

Its sign is the sign of

\[
 h(t)=\log{1+t\over1-t}-\pi t.                      \tag{1.2}
\]

At `t=15/16`,

\[
 h(15/16)=\log31-{15\pi\over16}>0.                 \tag{1.3}
\]

Indeed, `e<3` gives `log31>3`, while `pi<22/7` gives

\[
 {15\pi\over16}<{165\over56}<3.
\]

Moreover

\[
 h'(t)={2\over1-t^2}-\pi>0
 \qquad(15/16\le t<1).                              \tag{1.4}
\]

Thus

\[
 \boxed{K\text{ is strictly increasing on }[15A/16,A].}
                                                               \tag{1.5}
\]

## 2. A one-transient three-slot counterexample

Consider the internally superadditive table

\[
 (c_0,c_1,c_2,c_3)
 =\left(0,{15A\over16},2A,3A\right).                \tag{2.1}
\]

Its maximum density is `lambda=A`.  The critical denominations two and
three generate every integer capacity at least two.  Since no generator
has density exceeding `A`, the exact Bellman clock is

\[
 V_0=0,\qquad V_1={15A\over16},\qquad V_m=mA
 \quad(m\ge2).                                      \tag{2.2}
\]

Therefore

\[
\begin{aligned}
 \Phi(c)-C(A)
 &=K(15A/16)-K(A)\\
 &<0                                                 \tag{2.3}
\end{aligned}
\]

by (1.5).  Hence

\[
 \boxed{\Phi(c)<C(\lambda).}                        \tag{2.4}
\]

All deviations from the maximum-density arithmetic clock are confined to
the single capacity `m=1`.  Thus the finite Apéry transient has no general
nonnegative majorization sign.

## 3. The first-crossing normalization does not rescue the bound

The first-crossing prefix of (2.1) is the two-slot table

\[
 \left(0,{15A\over16},2A\right).                    \tag{3.1}
\]

It still has maximum density `lambda=A`, and its Bellman clock is

\[
 V_{2q}=2qA,
 \qquad
 V_{2q+1}=2qA+{15A\over16}.                         \tag{3.2}
\]

Splitting the arithmetic clock of step `A` into its even and odd rows gives

\[
 \Phi(c)-C(A)
 =\sum_{q\ge0}
 \left[
 K\left(2qA+{15A\over16}\right)-K((2q+1)A)
 \right].                                           \tag{3.3}
\]

The `q=0` summand is negative by (1.5).  For every `q>=1`, both arguments
lie in `[A,infinity)`, the first is smaller, and `K` is strictly increasing
there.  Hence every summand in (3.3) is strictly negative and the series is
absolutely convergent.  Therefore (3.1) also satisfies

\[
 \boxed{\Phi(c)<C(A).}                               \tag{3.4}
\]

The proposed lower bound fails both through a single finite transient and
inside the canonical first-threshold class.  This does not threaten the
proved two-slot or three-slot positivity theorems: `C(A)>0`, and those
theorems assert only `Phi(c)>0`, not the stronger comparison (0.2).
