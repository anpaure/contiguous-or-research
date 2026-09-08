# Independent audit: five-slot three-efficient delayed-`b` concavity

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_DELAYED_B_CONCAVITY_AND_PURE_LATTICE_GATE_20260804.md`  
**Verdict:** **PASS.**  The concavity calculation, endpoint collapse, and
the residual domain are correct.  This audit does not assert positivity of
the residual pure lattice.

## 1. Kernel differentiation

With

\[
 A={\sqrt\pi\over2},\qquad c=A^2={\pi\over4},\qquad
 h(s)=s e^{-cs^2},
\]

the normalized kernel on `0<=u<=1` is

\[
 K(Au)=1-e^{-c(1-u)^2}-e^{-c(1+u)^2}.
\]

Two differentiations give exactly

\[
 {d^2\over du^2}K(Au)
 =2c\{h'(1+u)+h'(1-u)\}=2cG(u).
\]

For `u>=1`, only the second Gaussian remains and the stated formula
`2c h'(1+u)` follows.  Thus the sign calculation uses the correct branch
and the correct positive scale factor.

## 2. Audit of Lemma 1.1

Direct differentiation verifies

\[
 h''(s)=2cs(2cs^2-3)e^{-cs^2},
\]

and

\[
 h'''(s)=2ce^{-cs^2}(-4c^2s^4+12cs^2-3).
\]

On `[3/5,7/5]`, the variable `q=cs^2` lies strictly between `7/25`
and `11/7`; the concave quadratic `-4q^2+12q-3` is positive at both
rational endpoints.  Hence `h'''` is positive there.  This proves the
claimed monotonicity of `G` on `[0,2/5]`.  On `[2/5,1/2]`, the two terms in

\[
 G'(u)=h''(1+u)-h''(1-u)
\]

have respectively positive and negative sign, so the monotonicity extends
to `[0,1/2]`.

The four-term expansion at `u=1/4,1/2` is correct.  The rational
exponential bounds used in the source imply

\[
 h'(1/2)+h'(3/4)<{1159\over1600},
\]

and

\[
 -h'(5/4)-h'(3/2)>{1167\over1600}.
\]

Therefore

\[
 G(1/4)+G(1/2)<-{1\over200}.
\]

The series estimates are directionally correct: the `e^(1/4)` tail is
bounded geometrically from degree two, and the `e^(9/5)` tail is bounded
geometrically beginning with the degree-four term.

## 3. Domain and strict concavity

Writing

\[
 \alpha=a/A,\quad t=p/A,\quad v=b/A,\quad d=1-t,
\]

the source domain gives

\[
 \alpha<d<v\le2\alpha,\qquad t\ge3\alpha.
\]

Consequently `alpha<1/4`, `v<1/2`, and

\[
 0<v-\alpha\le v/2\le1/4.
\]

The normalized second derivative of the three `b`-dependent terms is

\[
 G(v-\alpha)+G(v)+h'(1+t+v).
\]

The first two terms are at most
`G(1/4)+G(1/2)<-1/200`.  Since `t+v>1`, the last argument is greater
than two and `h'` is negative there.  Strict concavity follows.

A concave function on `[A-p,2a]` has its minimum at an endpoint.  At
`b=2a` all three pulse differences cancel exactly, leaving
`L_3(p;a,2a)`.

## 4. Threshold endpoint and residual domain

At `b=A-p`, the table

\[
 (0,d-a,d,p,p+a,A),\qquad d=A-p,
\]

is internally superadditive and size-three efficient.  The only less
immediate inequalities reduce to

\[
 p\ge2d-a,\qquad p+a\ge2d,\qquad2p\ge3d,
\]

and follow from `p>=3a` and `d<2a`.  Hence the cited threshold theorem
applies with its strict positive margin.

The existence of the open `b`-interval is equivalent to

\[
 A-2a<p<A-a,
\]

and together with `p>=3a` implies `0<a<A/4`.  This is exactly the stated
residual domain.  On `p=3a`, the three residue classes interlace to the
complete lattice `C(a)`.  The two other boundary identifications are also
correct (understood by continuity at the open boundary).

## 5. Scope

The audited theorem proves only

\[
 \mathcal H(p,a,b)\ge
 \min\{\mathcal H(p,a,A-p),\mathcal L_3(p;a,2a)\}.
\]

It does not sign the pure lattice in the interior.  No hidden positivity
claim or finite enumeration is used.

