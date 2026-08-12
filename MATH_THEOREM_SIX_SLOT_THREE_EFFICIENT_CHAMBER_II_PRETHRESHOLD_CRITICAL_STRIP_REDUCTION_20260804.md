# Six-slot `h=3` chamber II: exact prethreshold critical-strip reduction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It proves that every
interior minimum of the chamber-II ordered-gap train must lie on one exact
stationary Gaussian strip, and reduces the chamber to two prethreshold
boundary lattices plus that strip.  It does not sign those three residual
gates and therefore does not close the six-slot `h=3` branch.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_p(w)=\sum_{q\ge0}K(qp+w),
\tag{0.1}
\]

and

\[
 \mathcal L_3(p;a,b)=F_p(0)+F_p(a)+F_p(b).
\tag{0.2}
\]

The exact chamber-II domain is

\[
 {A\over2}\le p<A,
 \qquad
 0\le a\le {p\over3},
 \qquad
 2a\le b\le {p+a\over2},
 \qquad
 a,b<A-p.
\tag{0.3}
\]

Its cyclic gaps are ordered:

\[
                         a\le b-a\le p-b.
\tag{0.4}
\]

The canonical six-slot chamber theorem proves that the literal Bellman
functional is at least (0.2); all five availability pulses have already
been retained and signed before this reduction.

## 1. Exact two-compact-row formula

Fix `p` and put

\[
                         \varphi(x)=xe^{-x^2},
 \qquad
 \lambda(x)={\varphi'(x)\over\varphi(x)}={1\over x}-2x.
\tag{1.1}
\]

The function `lambda` is strictly decreasing on the positive axis.

For every

\[
                         0\le w<A-p,
\tag{1.2}
\]

the rows `q=0,1` of `F_p(w)` are compact and every later row is in the
Gaussian tail.  Hence the exact train is

\[
\boxed{
\begin{aligned}
 F_p(w)={}&2-e^{-(A-w)^2}-e^{-(A-p-w)^2}\\
          &-\sum_{q\ge0}e^{-(A+w+qp)^2}.
\end{aligned}}
\tag{1.3}
\]

Consequently

\[
 {1\over2}F_p'(w)
 =\sum_{q\ge0}\varphi(A+w+qp)
  -\varphi(A-w)-\varphi(A-p-w),
\tag{1.4}
\]

and

\[
 {1\over2}F_p''(w)
 =\sum_{q\ge0}\varphi'(A+w+qp)
  +\varphi'(A-w)+\varphi'(A-p-w).
\tag{1.5}
\]

Equations (1.3)--(1.5) retain the second compact row.  The usual
postthreshold critical-maximum lemma, which has only one compact source,
cannot be imported without this extra term.

## 2. A proof-safe critical-maximum region

### Lemma 2.1

Let `w` be an interior critical point of `F_p` in (1.2).  If

\[
                         (A+w)(A-p-w)\ge {1\over2},
\tag{2.1}
\]

then

\[
                         \boxed{F_p''(w)<0.}
\tag{2.2}
\]

Thus every interior local minimum must satisfy the strict reverse
inequality in (2.1).

#### Proof

Put

\[
 z=A+w,
 \qquad w_0=A-w,
 \qquad w_1=A-p-w.
\tag{2.3}
\]

At a critical point, (1.4) says

\[
 \sum_{q\ge0}\varphi(z+qp)
 =\varphi(w_0)+\varphi(w_1).
\tag{2.4}
\]

Since `lambda` is decreasing and `z+qp>=z`, equations (1.5) and (2.4)
give

\[
\begin{aligned}
 {1\over2}F_p''(w)
 \le{}&[\lambda(z)+\lambda(w_0)]\varphi(w_0)\\
      &+[\lambda(z)+\lambda(w_1)]\varphi(w_1).
\end{aligned}
\tag{2.5}
\]

The two coefficients are exactly

\[
 \lambda(z)+\lambda(w_0)
 =2A\left({1\over A^2-w^2}-2\right),
\tag{2.6}
\]

and

\[
 \lambda(z)+\lambda(w_1)
 =(2A-p)\left({1\over(A+w)(A-p-w)}-2\right).
\tag{2.7}
\]

Here `w<A-p<=A/2`, so

\[
 A^2-w^2>{3A^2\over4}={3\pi\over16}>{1\over2}.
\]

Thus (2.6) is strictly negative.  Under (2.1), coefficient (2.7) is
nonpositive.  Both weights in (2.5) are positive, proving (2.2).
\(\square\)

For fixed feasible `(p,a)`, compactify the `b` interval by putting

\[
                         B(p,a)=\min\left\{{p+a\over2},A-p\right\}.
\tag{2.8}
\]

Define the only possible interior-minimum fibre

\[
\boxed{
\begin{aligned}
 \mathcal C_{p,a}={}&\{b:2a<b<B(p,a),\\
 &\quad F_p'(b)=0,
 \quad (A+b)(A-p-b)<1/2\},
\end{aligned}}
\tag{2.9}
\]

Lemma 2.1 proves that no other interior point can minimize chamber II in
the `b` direction.

## 3. Exact endpoint split

The strict physical inequality `b<A-p` is recovered by taking a one-sided
limit when the second entry is active.  Continuity gives

\[
\boxed{
\begin{aligned}
 \min_{2a\le b\le B(p,a)}\mathcal L_3(p;a,b)
 =\min\biggl\{&\mathcal P_-(p,a),\ 
                         \mathcal U(p,a),\\
              &\inf_{b\in\mathcal C_{p,a}}
                   \mathcal L_3(p;a,b)\biggr\},
\end{aligned}}
\tag{3.2}
\]

where an infimum over an empty critical fibre is omitted and

\[
 \mathcal P_-(p,a)=\mathcal L_3(p;a,2a).
\tag{3.3}
\]

and

\[
 \mathcal U(p,a)=\mathcal L_3(p;a,B(p,a)).
\tag{3.3a}
\]

There are exactly two possibilities for the upper endpoint.

### 3.1 Threshold upper endpoint

If

\[
                         3p+a\ge2A,
\tag{3.4}
\]

then `B(p,a)=A-p`.  The limiting lattice

\[
                         \mathcal L_3(p;a,A-p)
\tag{3.5}
\]

is already strictly positive.  Indeed the five-slot table

\[
                         (0,a,A-p,p,p+a,A)
\tag{3.6}
\]

is internally superadditive: `A-p>=2a` is the lower chamber inequality,
`p>=a+(A-p)` follows jointly from (3.4) and `p>=3a`, while
`p+a>=2(A-p)` follows from the chamber upper wall at the limiting point.
Its first threshold is the endpoint `A`, so complete five-slot positivity
applies.

### 3.2 Repeated-gap upper endpoint

If

\[
                         3p+a\le2A,
\tag{3.7}
\]

then

\[
 B(p,a)={p+a\over2}.
\]

Writing

\[
                         \beta={p-a\over2},
\tag{3.8}
\]

gives the exact repeated-gap form

\[
\boxed{
 \mathcal R_-(p,a)=\mathcal U(p,a)
 =\mathcal L_3(a+2\beta;a,a+\beta),
 \qquad 3p+a\le2A.
}
\tag{3.9}
\]

This is the **prethreshold** side of the repeated-gap lattice: its last
compact value is

\[
 p+{p+a\over2}={3p+a\over2}\le A.
\]

The authenticated five-slot short-singleton theorem signs the opposite
side, where this value is at least `A`; it does not sign (3.9).

The lower endpoint (3.3) is likewise prethreshold on the honest chamber:

\[
                         p+2a<A.
\tag{3.10}
\]

It agrees with the arithmetic ceiling clock `C(a)>0` on `p=3a`, and its
limiting face `p+2a=A` is a positive five-slot threshold table.  Positivity
between those two faces is not inferred here.

## 4. Smallest proof-safe chamber-II gate

### Theorem 4.1

The complete chamber-II inequality follows from the following three
residual statements:

1. `mathcal P_-(p,a)>0` on its honest prethreshold domain;
2. `mathcal R_-(p,a)>0` on (3.7)--(3.9);
3. `mathcal L_3(p;a,b)>0` on every stationary fibre
   `mathcal C_{p,a}`.

The threshold upper endpoint is already closed and no interior point
outside these fibres can be a minimum in `b`.

This reduction is proof-safe but not a positivity proof.  In particular,
the postthreshold one-compact-row critical-maximum theorem cannot erase
these fibres: equation (1.3) shows the additional literal compact source
which must be paid.

## 5. Frozen dependencies and scope

| role | file | SHA-256 |
|---|---|---|
| exact six-slot three-chamber gate | `MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_EXACT_THREE_CHAMBER_GATE_20260804.md` | `a3a79b92148b1b4b415c7795473b70f50bd6d0b84f20f6899a3275f62af9b0dd` |
| canonical six-slot normal forms | `MATH_THEOREM_SIX_SLOT_CANONICAL_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md` | `3b537980a6f18aae936979335cc6756079ff10b92a80019acf3a97df8be9bede` |
| complete positivity through five slots | `MATH_THEOREM_FIVE_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md` | `69d8d73e52342a74d11a8673811e0d41d15063a2d66d1fdbc504138b4ed76bed` |
| postthreshold critical-maximum comparison (scope contrast) | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md` | `1e15d736592bce3103786fb965f62fe6f028436c0d35b763b195157a2cf3d0b6` |
| all-ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |

No claim is made about positivity of the three residual gates, the other
six-slot chambers, the full `h=3` branch, complete grid-six positivity,
the all-grid Bellman inequality, or an OR-word upper bound.
