# Audit of the second `w=y` boundary closure

**Date:** 2026-08-04  
**Verdict:** **PASS.**  The repeating-gap parameterization, compact-to-tail
slope comparison, Poisson coefficient and sign, train derivative, and
reduction to the uniform ceiling clock are all exact.  The theorem proves

\[
 \mathcal L_3(2y-u;u,y)>0
\]

throughout the stated surface.

No search, H100 computation, solver, or floating-point sign decision was
used.  The few large rational power comparisons were replayed by exact
cross-multiplication.

## 1. Frozen source and inherited inputs

| role | file | SHA-256 |
|---|---|---|
| audited theorem | `MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_WY_SECOND_BOUNDARY_CLOSURE_20260804.md` | `6a44b458c013e3c553be3925f9439960b139262175aaf79bbb9fb50054f6c7d7` |
| parent period reduction | `MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_PULSE_NORMAL_FORMS_20260804.md` | `0b46d0b2e073cc9eab4171198e2b4686ce08ef055887fd3f72cd0a506cdfef35` |
| first `w=y` boundary | `MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_THRESHOLD_SURFACE_CLOSURE_20260804.md` | `7e1a12d5cce9a16b6fd9a1b65d7d9d625d114c5b8810fa7f2d6baf95bfed722b` |

The audit-note hash is reported outside this self-referential note.

## 2. Parameter domain

On the surface `P+u=2y`, put `b=y-u`.  The inequalities

\[
 2y-A\le u\le y/2
\]

are equivalent to

\[
 y/2\le b\le A-y.
\]

Moreover

\[
 u=y-b,
 \qquad P=2y-u=y+b.
\]

Thus one period has ordered gaps `(u,b,b)`.  Since
`A/2<=y<=2A/3`, the interval is nonempty, `0<=u<=A/3`, and

\[
 3A/4\le P\le A,
 \qquad P+u=2y\ge A.
\]

Every compact/tail branch used later is therefore correctly identified.

## 3. Increase of the normalized compact slope

For

\[
 h(t)=t e^{-\pi t^2/4},
 \qquad D(t)=h(1+t)-h(1-t),
\]

one has `K'(At)=2A D(t)` on the compact branch.  Differentiation gives

\[
 D'(t)=h'(1+t)+h'(1-t),
 \quad
 h'(s)=e^{-\pi s^2/4}(1-\pi s^2/2).
\]

For `2/3<=t<=1`, the small argument `r=1-t` satisfies

\[
 h'(r)>{9\over10}{52\over63}={26\over35}.
\]

The large argument `s=1+t` satisfies

\[
 h'(s)>-{37\over7}{1\over8}=-{37\over56}.
\]

The exponential bounds used here are sign-safe:

* `e^{11/126}<263/241<10/9` follows from the geometric majorant of
  the positive exponential series;
* the degree-seven positive Taylor sum at `25/12` is
  `289664104889/36118462464>8`.

Hence

\[
 D'(t)>{23\over280}>0.
\]

Lemma 2.1 is valid on the closed interval, including `t=1` by one-sided
continuity.

## 4. Reflected-slope theta identity

Let

\[
 S(a)=\sum_{n\in\mathbb Z}(n+a)e^{-\pi(n+a)^2/4}.
\]

The four terms with indices `0,-1,1,-2` sum to

\[
 -\bigl(D(1-a)-D(a)\bigr).
\]

Pairing all remaining positive and negative indices gives

\[
 S(a)=-R(a)+T(a),
\]

where

\[
 R(a)=D(1-a)-D(a),
 \quad
 T(a)=\sum_{k\ge2}\bigl(h(k+a)-h(k+1-a)\bigr).
\]

For `0<=a<=1/3`, `h` decreases on every argument in the last sum and
`k+a<=k+1-a`; all its summands are nonnegative.  The first gives

\[
 T(a)\ge h(7/3)-h(8/3)>{1\over80}.
\]

The two strict rational comparisons were checked exactly:

\[
 e^{49\pi/36}<e^{30/7}
 <(11/4)^4(7/5)={102487\over1280}<{280\over3},
\]

and, using `pi>333/106`,

\[
 e^{16\pi/9}>e^{296/53}
 >\sum_{j=0}^8{(296/53)^j\over j!}
 ={4633837100358140947\over19611802479578715}
 >{640\over3}.
\]

These are exactly equivalent to `h(7/3)>1/40` and
`h(8/3)<1/80`.

Poisson summation at parameter `1/4` gives

\[
 \sum_{n\in\mathbb Z}e^{-\pi(n+a)^2/4}
 =2+4\sum_{m\ge1}e^{-4\pi m^2}\cos(2\pi ma).
\]

Differentiating both sides and comparing with
`theta'(a)=-(pi/2)S(a)` gives the exact coefficient

\[
 S(a)=16\sum_{m\ge1}m e^{-4\pi m^2}\sin(2\pi ma).
\]

There is no missing factor or sign.  Since `pi>3` and `e^3>20`,

\[
 |S(a)|
 <{16e^{-12}\over1-2e^{-36}}
 <{1\over5000}.
\]

Consequently

\[
 R(a)=T(a)-S(a)
 >{1\over80}-{1\over5000}
 ={123\over10000}>0.
\]

Thus `D(1-a)>D(a)` is proved uniformly, not inferred numerically.

## 5. Physical slope order

In the theorem's domain, set `a=u/A` and `p=P/A`.  Then

\[
 0\le a\le1/3,
 \qquad1-a\le p\le1.
\]

Since `D` increases on `[2/3,1]`,

\[
 D(p)\ge D(1-a)>D(a),
\]

and hence

\[
                         K'(P)>K'(u).
\]

This is the key compact-to-tail comparison and has the correct direction.

## 6. Derivative of the repeating-gap train

For fixed `y`, define

\[
 H_y(b)=\mathcal L_3(y+b;y-b,y).
\]

Termwise differentiation is justified by uniform Gaussian convergence.
The exact result is

\[
\begin{aligned}
H_y'(b)={}&-K'(u)+K'(P)+K'(P+y)\\
&+\sum_{q\ge2}\left(
qK'(qP)+(q-1)K'(qP+u)+qK'(qP+y)
\right).
\end{aligned}
\]

The coefficient of `K'(P+u)=K'(2y)` is zero, which is why that term does
not appear.  The first two terms have strictly positive sum by the preceding
section.  Every other displayed argument is strictly above `A`, while all
its coefficients are nonnegative; `K'>0` there.  Therefore

\[
                         H_y'(b)>0.
\]

There is no hidden finite transient in this derivative.

## 7. Uniform endpoint and final sign

The least allowed repeated gap is `b=y/2`.  At this endpoint

\[
 u={y\over2}=:s,
 \qquad P={3y\over2}=3s,
\]

and the three residue classes are the complete arithmetic lattice:

\[
 H_y(y/2)
 =\sum_{n\ge0}K(ns)
 =C(s)>0
\]

by the proved all-ceiling theorem.  Strict increase in `b` therefore gives

\[
 \mathcal L_3(2y-u;u,y)=H_y(y-u)\ge C(y/2)>0.
\]

This proves the theorem throughout the closed domain, including
`y=A/2`, `u=0`, and the singleton limiting face
`y=2A/3`, `u=A/3`.

## 8. Scope

The theorem closes only the second period boundary of the `w=y` face.
Together with the separately proved first boundary and period monotonicity,
it closes that face's subcritical effective-clock term.  The parent theorem
prices its remaining compact transient separately.

This audit makes no claim about the `w=2u` five-pulse system, the remaining
large-residue tail scope, the all-slot Bellman inequality, or an OR-word
upper bound.
