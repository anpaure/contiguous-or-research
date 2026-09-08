# Repeated Rayleigh equal-level subtraction fails the second prefix-Hall row

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional no-go for one specific adaptive policy.  The first
equal-level subtraction regenerates a one-zero/one-minimum signed-tail
kernel, so a second equal-level subtraction is algebraically defined.
However, the pair left after that second subtraction violates the necessary
first-piece prefix Hall inequality at the origin.  Therefore the
equal-level rule cannot be iterated twice as a complete construction.
This does **not** rule out completing the first transformed pair with a
different second-socket coupling.

## 0. Input from the first transform

Let `K` be the Rayleigh signed-tail kernel, let `b` be its zero, and let
`u(t)` be the inverse remainder-level function from the first equal-level
subtraction.  The first transformed kernel is

\[
 \widetilde K(t)=
 \begin{cases}
  K(t)+u(t),&0\le t<b,\\
  u(t),&t\ge b.
 \end{cases}                                      \tag{0.1}
\]

The one-well regeneration theorem proves

\[
 \widetilde K'(t)<0\quad(0<t<b),
 \qquad
 \widetilde K'(t)>0\quad(t>b),                    \tag{0.2}
\]

and gives a unique zero

\[
 0<\widetilde b<b.
\]

The minimum is at `b`.  Put

\[
 \widetilde m=\widetilde K(b)=u(b)<0.
\]

The minimum is a genuine corner.  Its one-sided slopes are

\[
 L_-:=\widetilde K'(b-)=K'(b)+u'(b)<0,
 \qquad
 L_+:=\widetilde K'(b+)=u'(b)>0.                  \tag{0.3}
\]

The strict sign on the left is precisely the proved pointwise inequality
`-K'(b)>u'(b)` (or its limit from below).

## 1. Density created by a second equal-level subtraction

For `v in (widetilde m,0)`, let

\[
 \widetilde\ell(v)\in(\widetilde b,b),
 \qquad
 \widetilde r(v)\in(b,\infty)
\]

be the two inverse branches of `widetilde K`, and set

\[
 \widetilde z(v)=\widetilde r(v)-\widetilde\ell(v).
\]

The second equal-level rule pairs the residual job
`widetilde r(v)` with the residual socket `widetilde ell(v)` and leaves
the new job `widetilde z(v)`.

### Lemma 1.1 (positive new-job density at zero)

The new-job measure

\[
 \widehat\mu=\widetilde z_\#(dv|_{(\widetilde m,0)})
\]

has a strictly positive right density at zero:

\[
 \boxed{
 {d\widehat\mu\over dt}(0+)
 ={(-L_-)L_+\over -L_-+L_+}>0.}                   \tag{1.1}
\]

### Proof

The one-sided inverse-function theorem at the corner gives, as
`v downarrow widetilde m`,

\[
 \widetilde\ell(v)
 =b+{v-\widetilde m\over L_-}+o(v-\widetilde m),
\]

and

\[
 \widetilde r(v)
 =b+{v-\widetilde m\over L_+}+o(v-\widetilde m).
\]

Consequently

\[
 \widetilde z(v)
 =(v-\widetilde m)
 \left({1\over L_+}-{1\over L_-}\right)
 +o(v-\widetilde m).
\]

Inverting this linear asymptotic yields (1.1). `square`

## 2. The remaining socket bank is quadratically thin

The second equal-level rule uses exactly the residual sockets on
`(widetilde b,b)`.  Its unused socket bank is therefore

\[
 \widehat\nu(dy)
 =-\widetilde K'(y)\mathbf1_{(0,\widetilde b)}(y)dy. \tag{2.1}
\]

### Lemma 2.1

One has

\[
 \boxed{{d\widehat\nu\over dy}(0+)=0.}             \tag{2.2}
\]

Hence

\[
 \widehat\nu(0,t]=o(t)\qquad(t\downarrow0).      \tag{2.3}
\]

### Proof

The original kernel has `K'(0)=0`.  At first-transform separation
`t downarrow0`, both equal-level endpoints tend to the smooth minimum `c`,
so both endpoint slopes tend to zero.  Their parallel sum

\[
 u'(t)={K'(r(u))[-K'(\ell(u))]
        \over K'(r(u))-K'(\ell(u))}
\]

therefore tends to zero.  Equation (0.1) gives

\[
 \widetilde K'(0+)=K'(0)+u'(0+)=0.
\]

This proves (2.2), and integration gives (2.3). `square`

## 3. Prefix-Hall contradiction

### Theorem 3.1 (second equal-level remainder is not coagulable)

The pair `(widehat mu,widehat nu)` left by two consecutive equal-level
subtractions admits no finite coagulation.

### Proof

For any finite coagulation, let `kappa` be the first-piece marginal.
Every job of size at most `t` has its first positive piece at most `t`.
Therefore the necessary prefix-Hall inequality is

\[
 \widehat\nu(0,t]\ge\kappa(0,t]
 \ge\widehat\mu(0,t]                               \tag{3.1}
\]

for every `t>0`.

Lemma 1.1 gives, with a constant `h_0>0`,

\[
 \widehat\mu(0,t]=h_0t+o(t).
\]

Lemma 2.1 gives

\[
 \widehat\nu(0,t]=o(t).
\]

These contradict (3.1) for all sufficiently small positive `t`.
`square`

## 4. Exact consequence

The first equal-level subtraction remains a correct exact reduction, and
the first transformed pair may still admit a coagulation.  What is ruled
out is the policy

\[
 \boxed{
 \text{cancel common density, pair equal levels, and repeat unchanged}.}
\]

After the first subtraction, any successful continuation must deliberately
use a non-equal-level coupling near the transformed origin.  It must assign
enough small unused sockets to the positive-density family of small
remainders; otherwise the first-piece prefix Hall row fails exactly as
above.

The obstruction is local and policy-specific.  It is not a separator for
the original Rayleigh configuration cone, not a no-go for every adaptive
interval flow, and not a statement about the discrete or literal OR-word
problem.

## 5. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_PRIMARY_SUBTRACTION_20260805.md`,
   SHA at use:
   `b63058f76b1ebb4904b4b939b10f981332d7de36bba90a39d8b1a35424787ac6`.
2. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`,
   SHA at use:
   `910adbabec163e81d7896e155255561ec00463ca8fb67b9c7bf69aebd9588e20`.
