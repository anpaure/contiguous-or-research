# Four-slot Apéry scalar gate: exact Fourier closure

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical inequality.  Combined with the
exact four-state Apéry reduction in
`MATH_THEOREM_FOUR_SLOT_APERY_EXACT_NORMAL_FORM_AND_THRESHOLD_FACE_20260804.md`,
it closes the remaining four-slot-efficient Bellman branch.  It does not
address the three-slot-efficient branch, all finite Bellman tables, or an
OR-word construction.

Put

\[
 A={\sqrt\pi\over2}
\]

and let `K` be the Rayleigh signed-tail kernel.  Write

\[
 C(a)=\sum_{m\ge0}K(ma).
\tag{0.1}
\]

The exact Apéry reduction leaves the scalar function

\[
 J(\alpha)=C(\alpha)+K(4\alpha)-K(5\alpha),
 \qquad {A\over4}\le\alpha\le {A\over3}.
\tag{0.2}
\]

## 1. A uniform small-step ceiling margin

Let

\[
 M=1-2e^{-\pi/4}.
\tag{1.1}
\]

The Fourier proof of the all-ceiling theorem gives, for every `a>0`,

\[
 \left|C(a)-{M\over2}\right|
 \le {C_0a^2\zeta(3)\over4\pi^3},
 \qquad C_0=4+8e^{-3/2}<6.
\tag{1.2}
\]

### Lemma 1.1

For `0<a<=A/3`,

\[
                         \boxed{C(a)>{1121\over30240}.}
\tag{1.3}
\]

### Proof

The rational bounds used in the ceiling theorem are

\[
 M>{3\over35},\qquad \zeta(3)<{5\over4},
 \qquad \pi^2>9.
\tag{1.4}
\]

Since `A^2=pi/4` and `a^2<=A^2/9=pi/36`, (1.2) gives

\[
 {C_0a^2\zeta(3)\over4\pi^3}
 <{6(5/4)(\pi/36)\over4\pi^3}
 ={5\over96\pi^2}<{5\over864}.
\tag{1.5}
\]

Therefore

\[
 C(a)>{3\over70}-{5\over864}
 ={1121\over30240}.
\]

This proves (1.3). \(\square\)

## 2. The adverse tail decrement is smaller

For `alpha>=A/4`, both `4alpha` and `5alpha` lie in the Gaussian tail, so

\[
 K(4\alpha)-K(5\alpha)
 =-D(\alpha),
\]

where

\[
 D(\alpha)
 =e^{-(A+4\alpha)^2}-e^{-(A+5\alpha)^2}.
\tag{2.1}
\]

### Lemma 2.1

For `A/4<=alpha<=A/3`,

\[
                         \boxed{D(\alpha)<{101\over4000}.}
\tag{2.2}
\]

### Proof

Put `t=alpha/A`, so `1/4<=t<=1/3`, and put `a_0=A^2=pi/4`.
Differentiation shows that `D'(alpha)<0` exactly when

\[
 \log {5(1+5t)\over4(1+4t)}
 <a_0t(2+9t).
\tag{2.3}
\]

On the stated interval,

\[
 {5(1+5t)\over4(1+4t)}\le {10\over7}<{3\over2},
\]

and `log(3/2)<1/2`, since the first three terms of the exponential series
give `e^(1/2)>1+1/2+1/8>3/2`.  On the other hand,

\[
 a_0t(2+9t)
 \ge {\pi\over4}{17\over16}
 >{51\over64}>{1\over2}.
\]

Thus (2.3) holds and `D` is strictly decreasing.  Its maximum is at
`alpha=A/4`, where

\[
 D(A/4)=e^{-\pi}-e^{-81\pi/64}.
\tag{2.4}
\]

The exact rational Gaussian bounds

\[
 e^{-\pi}<{7\over160},
 \qquad e^{-81\pi/64}>{37\over2000}
\tag{2.5}
\]

therefore give

\[
 D(\alpha)<{7\over160}-{37\over2000}
 ={101\over4000}.
\]

This proves (2.2). \(\square\)

## 3. Closure of the scalar gate

### Theorem 3.1

For every

\[
                         {A\over4}\le\alpha\le {A\over3},
\]

one has the uniform strict margin

\[
 \boxed{
 J(\alpha)>{1117\over94500}>0.
 }
\tag{3.1}
\]

### Proof

Lemmas 1.1 and 2.1 give

\[
 J(\alpha)
 =C(\alpha)-D(\alpha)
 >{1121\over30240}-{101\over4000}.
\]

With common denominator `756000`, the last difference is

\[
 {28025-19089\over756000}
 ={8936\over756000}
 ={1117\over94500}>0.
\]

This proves (3.1). \(\square\)

### Corollary 3.2 (complete four-slot-efficient positivity)

Every internally superadditive four-slot Bellman table whose size-four
generator has maximal efficiency has strictly positive Bellman functional.

### Proof

First apply the all-grid first-crossing deletion theorem.  If the first
displayed threshold crossing occurs before capacity four, the resulting
prefix has grid size at most three and hence has strictly positive Bellman
functional; deletion only lowered the functional, so the original table is
strictly positive as well.

It remains that the first crossing is the endpoint `T`, so `x,y,z<A`.
The exact Apéry reduction now lowers that endpoint, by tail monotonicity, to
one of three boundary faces.  The threshold face `T=A` is already positive;
the face `T=2y` is the proved two-slot-efficient branch; and the remaining
face `T=4z/3` is bounded below by `J(z/3)`, with
`A/4<=z/3<=A/3`.  Apply Theorem 3.1. \(\square\)

## 4. Scope

The scalar gate (0.2) is closed with an explicit rational margin.  Together
with the separately audited Apéry normal form, this leaves no open
four-slot-efficient case.  The three-slot-efficient branch still has two
boundary surfaces on its `w=y` face and a five-pulse `w=2u` system.  No
claim about all `n=4`, the universal Bellman inequality, or
`nu(k)<=B(k)+O(1)` is made here.
