# Independent audit: the second `w=y` boundary closure

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_WY_SECOND_BOUNDARY_CLOSURE_20260804.md`  
**Audited theorem SHA-256:**
`6a44b458c013e3c553be3925f9439960b139262175aaf79bbb9fb50054f6c7d7`  
**Verdict:** **PASS.**  The reflected-slope identity, all derivative signs,
the closed parameter domain, and the reduction to the uniform arithmetic
clock are correct.  No search, H100 computation, solver, or floating-point
sign decision was used.

## 1. Domain replay

On the boundary `P+u=2y`, set

\[
                         b=y-u.
\]

Then

\[
 u=y-b,qquad P=y+b.
\]

The inherited bounds

\[
 A/2\le y\le2A/3,qquad2y-A\le u\le y/2
\]

are exactly equivalent to

\[
                         y/2\le b\le A-y.
\]

Thus

\[
 0\le u\le A/3,qquad3A/4\le P\le A,qquad
 P+u=2y\ge A.
\]

At `y=A/2`, the endpoint `u=0` is legitimate.  At `y=2A/3`, the interval
collapses to `u=b=A/3`.  No endpoint is lost.

## 2. Monotonicity of the compact slope

With

\[
 h(t)=t e^{-\pi t^2/4},qquad D(t)=h(1+t)-h(1-t),
\]

direct differentiation gives

\[
 K'(At)=2A D(t),qquad
 D'(t)=h'(1+t)+h'(1-t).
\]

For `2/3<=t<=1`, put `r=1-t` and `s=1+t`.  The two exact estimates in
the theorem are

\[
 h'(r)>{9\over10}{52\over63}={26\over35},
 \qquad
 h'(s)>-{37\over7}{1\over8}=-{37\over56}.
\]

The first uses `r<=1/3`; the second uses `5/3<=s<=2`.  Their difference is

\[
                         D'(t)>{23\over280}>0.
\]

The directions remain valid at both closed endpoints by one-sided
continuity.  Hence `D` is strictly increasing on `[2/3,1]`.

## 3. Reflected-slope Poisson identity

Define

\[
 S(a)=\sum_{n\in\mathbb Z}(n+a)e^{-\pi(n+a)^2/4}.
\]

The four terms indexed by `0,-1,1,-2` sum to

\[
 -\bigl(D(1-a)-D(a)\bigr).
\]

Pairing the remaining indices `k` and `-(k+1)`, `k>=2`, gives exactly

\[
 S(a)=-R(a)+T(a),
\]

where

\[
 R(a)=D(1-a)-D(a),qquad
 T(a)=\sum_{k\ge2}\bigl(h(k+a)-h(k+1-a)\bigr).
\]

For `0<=a<=1/3`, both arguments in every summand of `T` are at least two,
`h` is decreasing there, and `k+a<=k+1-a`.  Hence every summand is
nonnegative.  The first one satisfies

\[
 T(a)\ge h(2+a)-h(3-a)
       \ge h(7/3)-h(8/3)>{1\over80}.
\]

The two rational exponential estimates proving the last inequality have
the correct directions:

\[
 e^{49\pi/36}<280/3,qquad e^{16\pi/9}>640/3.
\]

Poisson summation gives

\[
 \Theta(a):=\sum_{n\in\mathbb Z}e^{-\pi(n+a)^2/4}
 =2+4\sum_{m\ge1}e^{-4\pi m^2}\cos(2\pi ma).
\]

Since

\[
 \Theta'(a)=-{\pi\over2}S(a),
\]

differentiating the Fourier side gives the exact coefficient and sign

\[
                         S(a)=16\sum_{m\ge1}
 m e^{-4\pi m^2}\sin(2\pi ma).
\]

There is no missing factor two.  The ratio of consecutive absolute tail
terms is at most `2e^{-36}`, so

\[
 |S(a)|<{16e^{-12}\over1-2e^{-36}}<{1\over5000}.
\]

Consequently

\[
 R(a)=T(a)-S(a)>{1\over80}-{1\over5000}
 ={123\over10000}>0.
\]

This proves `D(1-a)>D(a)` with a strict uniform margin.

## 4. Corollary direction

If

\[
 0\le a\le1/3,qquad1-a\le p\le1,
\]

then `1-a,p` both lie in `[2/3,1]`.  Since `D` is increasing there,

\[
 D(p)\ge D(1-a)>D(a).
\]

Using `K'(At)=2AD(t)` gives, in the required direction,

\[
                         K'(Ap)>K'(Aa).
\]

This compares a possibly compact slope at `u=Aa` with the period slope at
`P=Ap`; it is not an illicit appeal to monotonicity of `K'` across the
turning point.

## 5. Exact train derivative

For fixed `y`, write

\[
 H_y(b)=\mathcal L_3(y+b;y-b,y),qquad
 u=y-b,quad P=y+b.
\]

Termwise differentiation is justified by Gaussian domination.  For each
period index,

\[
 {d\over db}(qP)=q,quad
 {d\over db}(qP+u)=q-1,quad
 {d\over db}(qP+y)=q.
\]

Therefore

\[
\begin{aligned}
 H_y'(b)={}&-K'(u)+K'(P)+K'(P+y)\\
 &+\sum_{q\ge2}\left(
 qK'(qP)+(q-1)K'(qP+u)+qK'(qP+y)
 \right).
\end{aligned}
\]

In particular, the coefficient of `K'(P+u)=K'(2y)` at `q=1` is exactly
zero, explaining its absence.

Set `a=u/A` and `p=P/A`.  The domain gives

\[
 0\le a\le1/3,qquad p+a=2y/A\ge1,qquad p\le1.
\]

Thus the preceding slope comparison makes

\[
                         K'(P)-K'(u)>0.
\]

Every remaining displayed argument is at least `A`, every coefficient is
nonnegative, and `K'>0` in the Gaussian tail.  Hence

\[
                         H_y'(b)>0
\]

throughout the full closed parameter interval.

## 6. Uniform-lattice endpoint

The minimum allowed repeated gap is `b=y/2`.  At this point

\[
                         u=y/2=:s,qquad P=3s.
\]

The three residue classes are exactly

\[
 3qs,qquad(3q+1)s,qquad(3q+2)s,qquad q\ge0,
\]

so, with neither omission nor multiplicity,

\[
                         H_y(y/2)=C(s)>0
\]

by the all-ceiling theorem.  Since `H_y` is strictly increasing,

\[
 \mathcal L_3(2y-u;u,y)=H_y(y-u)\ge C(y/2)>0.
\]

This includes both domain endpoints and proves the theorem.

## 7. Consequence for all four-slot tables

This theorem closes the second boundary `P+u=2y`.  The first boundary
`P+u=A` was already audited, and strict period monotonicity reduces the
entire subcritical `w=y` face to those two boundaries.  The large-period
case is removed by first-crossing deletion.  The independently audited
`w=2u` theorem closes the other three-efficient face.

Together with the previously proved two-efficient and four-efficient
branches, these cases exhaust which of

\[
                         y/2,qquad z/3,qquad T/4
\]

has maximal efficiency.  Therefore every internally superadditive
four-slot Bellman table has strictly positive functional.  Equivalently,
any finite Bellman counterexample must have at least five active slots.

This does not prove the all-slot Bellman inequality or
`nu(k)<=B(k)+O(1)`.

**Final independent verdict: PASS.**
