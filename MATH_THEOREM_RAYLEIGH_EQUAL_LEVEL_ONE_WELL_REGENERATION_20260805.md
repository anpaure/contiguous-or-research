# Rayleigh equal-level subtraction regenerates the one-well kernel

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional theorem.  For the first equal-level subtraction
of the Rayleigh residual pair, the transformed signed-tail kernel is again
strictly decreasing up to the end of its socket support and strictly
increasing afterward.  Hence it has one zero and one minimum and admits a
second canonical equal-level subtraction.  This theorem does **not** prove
that all later transforms obey the same curvature bounds or that the
iteration terminates.

## 0. Setup

Put

\[
 A={\sqrt\pi\over2}
\]

and

\[
 K(t)=
 \begin{cases}
  1-e^{-(A-t)^2}-e^{-(A+t)^2},&0\le t\le A,\\
  -e^{-(A+t)^2},&t>A.
 \end{cases}                                      \tag{0.1}
\]

Let `b` be its unique zero and `c` its unique minimum, so

\[
 0<b<c<A.
\]

Write `m=K(c)`.  For `m<u<0`, let

\[
 \ell(u)\in(b,c),\qquad r(u)\in(c,\infty)
\]

be the two inverse branches of `K`, and put

\[
 z(u)=r(u)-\ell(u).
\]

The equal-level subtraction theorem proves that `z` is a strictly
increasing bijection from `(m,0)` to `(0,infinity)`.  Write

\[
 u(t)=z^{-1}(t).
\]

Its transformed signed-tail kernel is

\[
 \widetilde K(t)=
 \begin{cases}
   K(t)+u(t),&0\le t<b,\\
   u(t),&t\ge b.
 \end{cases}                                      \tag{0.2}
\]

At an equal-level pair set

\[
 a=K'(r(u))>0,
 \qquad q=-K'(\ell(u))>0.
\]

Then

\[
 u'(t)={a q\over a+q}.                              \tag{0.3}
\]

The open row in the preceding reduction was the pointwise inequality

\[
 -K'(t)\ge u'(t)\qquad(0<t<b).                     \tag{0.4}
\]

We prove it strictly.

## 1. Two global differential bounds

Let

\[
 Q(x)=2x e^{-x^2},
 \qquad Q'(x)=2(1-2x^2)e^{-x^2}.
\]

### Lemma 1.1 (global curvature ceiling)

For every `x>=0`,

\[
 \boxed{K''(x)<{8\over5}.}                         \tag{1.1}
\]

### Proof

For `0<=x<=A`, put `v=A-x` and `w=A+x`.  Then

\[
 K''(x)=Q'(v)+Q'(w),
 \qquad 0\le v\le A\le w.                         \tag{1.2}
\]

Since `A>1/sqrt(2)`, one has `Q'(w)<0`.

If `v>=3/10`, then `Q'` is decreasing on `[0,A]` until well past
`3/10`, and

\[
 Q'(v)\le Q'(3/10)
 ={41\over25}e^{-9/100}<{8\over5}.                 \tag{1.3}
\]

The last inequality follows from
`e^(9/100)>1+9/100`, hence
`e^(-9/100)<100/109<40/41`.

Suppose instead that `v<3/10`.  Since `sqrt(pi)>17/10`,

\[
 w=\sqrt\pi-v>{7\over5}.                           \tag{1.4}
\]

The function `Q'` is increasing on
`[7/5,infinity)`.  Also `w<=sqrt(pi)`, so

\[
 Q'(w)\le Q'(\sqrt\pi)
 =-2(2\pi-1)e^{-\pi}<-{2\over5}.                  \tag{1.5}
\]

For the last strict inequality, the function
`(2x-1)e^(-x)` decreases for `x>3/2`.  Thus

\[
 (2\pi-1)e^{-\pi}
 >(37/7)e^{-22/7}>{1\over5}.                       \tag{1.6}
\]

Indeed, `22/7<16/5`, while the elementary bounds
`e<11/4` and `e^(1/5)<5/4` give

\[
 e^{22/7}<e^{16/5}
 <(11/4)^3(5/4)={6655\over256}<{185\over7}.
\]

Since always `Q'(v)<=2`, equations (1.5)--(1.6) give
`Q'(v)+Q'(w)<8/5` in the second case as well.

For `x>A`,

\[
 K''(x)=Q'(A+x)<0,
\]

so (1.1) is automatic.  This proves the lemma. `square`

### Lemma 1.2 (left-slope floor)

The zero satisfies

\[
 b<{1\over2},                                      \tag{1.7}
\]

and, for every `0<t<=1/2`,

\[
 \boxed{-K'(t)>{2\over5}t.}                       \tag{1.8}
\]

### Proof

First,

\[
 e^{(\pi+1)/4}<e^{29/28}
 =e\,e^{1/28}
 <{87\over32}{28\over27}={203\over72}.            \tag{1.9}
\]

Here `pi<22/7`; the standard exponential series gives
`e<87/32`, and `e^x<1/(1-x)` for `0<x<1` gives
`e^(1/28)<28/27`.

Also, with `A^2=pi/4>157/200`,

\[
 \cosh A>1+{A^2\over2}+{A^4\over24}>{203\over144}.
\]

Consequently

\[
 e^{-(A-1/2)^2}+e^{-(A+1/2)^2}
 =2e^{-(\pi+1)/4}\cosh A>1.
\]

Thus `K(1/2)<0`, and uniqueness of the zero gives (1.7).

For the slope estimate, put `x=2At` and write

\[
 {-K'(t)\over t}
 =4e^{-(A^2+t^2)}H(x),
 \qquad
 H(x)=2A^2{\sinh x\over x}-\cosh x.                \tag{1.10}
\]

Its power series is

\[
 H(x)=\sum_{n\ge0}
 {2A^2-(2n+1)\over(2n+1)!}x^{2n}.                 \tag{1.11}
\]

The constant coefficient is positive, while every coefficient with
`n>=1` is negative.  Hence `H` is strictly decreasing for `x>0`.

We next check that it remains positive through `x=A`.  Since
`pi<256/81`, one has `A<8/9`.  For `0<=x<=8/9`, the bound

\[
 (2n)!\ge2\,12^{n-1}\qquad(n\ge1)
\]

gives

\[
 \cosh x
 \le1+{x^2/2\over1-x^2/12}
 \le {323\over227}<{10\over7}.                    \tag{1.12}
\]

Therefore

\[
 A\sinh A-{1\over2}\cosh A
 >A^2+{A^4\over6}-{5\over7}>{3\over20},           \tag{1.13}
\]

where the final rational inequality follows from
`A^2>157/200`.  In particular `H(A)>3/10>0`.

Both factors on the right side of (1.10) are now positive and strictly
decreasing on `0<t<=1/2`.  Hence `(-K'(t))/t` is decreasing there.
At the right endpoint, equations (1.9) and (1.13) give

\[
 -K'(1/2)
 =4e^{-(\pi+1)/4}
 \left(A\sinh A-{1\over2}\cosh A\right)
 >{288\over203}{3\over20}>{1\over5}.              \tag{1.14}
\]

It follows that

\[
 {-K'(t)\over t}
 \ge {-K'(1/2)\over1/2}>{2\over5},
\]

which is (1.8). `square`

## 2. Harmonic endpoint slopes

### Theorem 2.1 (regenerative pointwise inequality)

For every `0<t<b`,

\[
 \boxed{-K'(t)>u'(t).}                              \tag{2.1}
\]

### Proof

Fix `t` and let

\[
 \ell=\ell(u(t)),\qquad r=r(u(t)),
 \qquad d_-=c-\ell,qquad d_+=r-c.
\]

Then `d_-+d_+=t`.  Lemma 1.1 and `K'(c)=0` give

\[
 q=-K'(\ell)=\int_\ell^cK''(x)dx
 <{8\over5}d_-,
\]

and

\[
 a=K'(r)=\int_c^rK''(x)dx
 <{8\over5}d_+.
\]

The harmonic-mean map `(a,q)->aq/(a+q)` is increasing in each
positive variable.  Therefore

\[
 u'(t)={aq\over a+q}
 <{8\over5}{d_-d_+\over d_-+d_+}
 \le {8\over5}{t\over4}={2\over5}t.               \tag{2.2}
\]

Since `t<b<1/2`, Lemma 1.2 gives

\[
 -K'(t)>{2\over5}t>u'(t).
\]

This proves (2.1). `square`

## 3. One-well regeneration

### Corollary 3.1

The transformed kernel in (0.2) is strictly decreasing on `(0,b)` and
strictly increasing on `(b,infinity)`.  It has a unique zero

\[
 \widetilde b\in(0,b)
\]

and its unique minimum is attained at `b`.

### Proof

On `(0,b)`, equations (0.2) and (2.1) give

\[
 \widetilde K'(t)=K'(t)+u'(t)<0.
\]

On `(b,infinity)`,

\[
 \widetilde K'(t)=u'(t)>0.
\]

The preceding equal-level theorem gives

\[
 \widetilde K(0)=K(0)+m>0,
 \qquad
 \widetilde K(b)=u(b)<0,
 \qquad
 \lim_{t\to\infty}\widetilde K(t)=0.
\]

Strict monotonicity proves every assertion. `square`

### Corollary 3.2 (a second canonical subtraction exists)

After cancelling the common one-piece density of the transformed socket
and job measures, their residual densities are

\[
 -\widetilde K'(y)\mathbf1_{(0,b)}(y)dy,
 \qquad
 \widetilde K'(x)\mathbf1_{(b,\infty)}(x)dx.
\]

For every level between `widetilde K(b)` and zero there are exactly two
inverse branches, one on each side of `b`.  Pairing those branches gives a
second exact state-dependent equal-level socket subtraction, by the same
change-of-variables argument as in the primary theorem.

This is a structural regeneration theorem for **one further step**.  The
new kernel after that second subtraction is not asserted to satisfy the
Rayleigh-specific bounds (1.1) and (1.8).  Therefore no infinite
iteration, termination, or complete coagulation is claimed.

## 4. Exact remaining scalar

The first adaptive subtraction no longer ends at an arbitrary transformed
pair: it ends at another one-zero/one-minimum signed-tail pair, and hence
the same canonical move is available once more.

To turn this into a full coagulation proof it is enough to prove one of the
following genuinely new statements.

1. **Invariant curvature/slope cone.**  Every iterated kernel `K_n`
   satisfies a scale-covariant version of

   \[
   \sup K_n''\le4\inf_{0<t<b_n}{-K_n'(t)\over t}.
   \]

   Then the harmonic-slope proof above repeats indefinitely.
2. **Terminal contraction.**  Some monotone size functional of the unused
   socket support or transformed job work contracts under each equal-level
   subtraction, while the total expected number of appended sockets stays
   finite.

Neither statement is proved here.  What is proved is the complete first
regeneration step and the exact differential inequality that made it
possible.

## 5. Frozen dependency

`MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_PRIMARY_SUBTRACTION_20260805.md`,
current SHA-256 at the time of this proof:

`b63058f76b1ebb4904b4b939b10f981332d7de36bba90a39d8b1a35424787ac6`.

