# Independent audit: complementary-pair train and h=4 inert scalar reduction

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md`  
**Method:** exact analytic replay; no search, sampling, or numerical
optimization.

## Verdict

**PASS.**  The uniform three-train pair lemma is proved on the entire h=4
shift domain, the inert-face coordinate conversion is exact, and the final
joint pair envelope is a proof-safe scalar boundary.  The scalar boundary
itself remains unsigned, exactly as stated.

## 1. Small-shift and reflection inputs

The frozen train proofs give

\[
C(A)>57/1400,
\qquad
F_A(A/4)>33/800,
\qquad
F_A(A/4)<293/6000.
\]

Since every interior critical point on `[0,A/4]` is a strict maximum, its
minimum occurs at an endpoint.  Both endpoints exceed `57/1400`, so the
strengthened lower bound used in (0.5) is valid.  Monotone decrease on
`[A/4,A/2]`, positivity through `A/2`, and the theta-reflection error
`1/20000` are also exactly the previously proved inputs.

## 2. Complementary-pair case split

If `z>A/2`, putting `v=A-z` converts `z<=3A/4` into
`A/4<=v<A/2`.  Reflection gives

\[
F_\tau(z)>-F_A(v)-1/20000,
\]

because period enlargement only raises each fixed shifted train.

When `y<=v`, monotone decrease handles `y>=A/4`; the strengthened
small-shift bound handles `y<A/4`.  The displayed margin

\[
2(57/1400)-293/6000-1/20000=13669/420000
\]

is exact.

When `y>v`, write `s=y-v`.  The subcomplementary condition gives
`A+s=y+z<=tau`, so `C(tau)>=C(A+s)`.  Also `0<s<=A/4`.

For `s<=A/24`, differentiation gives

\[
-F_A'(t)<2(A-t)e^{-(A-t)^2}.
\]

On the relevant interval the right side is maximized at `A-t=3A/4`.
Integration gives

\[
F_A(v)-F_A(v+s)
<(\pi/64)e^{-9\pi/64}<1/30.
\]

The elementary estimates in the theorem imply the last strict rational
bound.  Hence the short-displacement margin `3079/420000` is correct.

## 3. Long-displacement ceiling certificate

The exact ceiling identity is

\[
C(\tau)=1-2e^{-\pi/4}
-\sum_{q\ge1}e^{-(A+q\tau)^2}.
\]

The three Taylor comparisons used in the theorem are exact:

\[
\sum_{j=0}^{6}{(333/424)^j\over j!}>{125\over57},
\]

\[
\sum_{j=0}^{8}{(88837/27136)^j\over j!}
>{64000\over2457},
\]

and

\[
\sum_{j=0}^{8}{(113775/27136)^j\over j!}>64.
\]

All follow by positive-term truncation and integer cross multiplication.
They give

\[
M>11/125,
\qquad
R(25A/24)<39/1000,
\]

and therefore `C(25A/24)>49/1000`.  The resulting long-displacement
margin

\[
49/1000-293/6000-1/20000=7/60000
\]

is exact.  This completes an independent replay of Theorem 1.1.

## 4. Inert-face coordinate audit

With `u=A-P`, `v=A-z`, and `delta=tau-A`, the two active maxima give

\[
x-u\le\delta,
\qquad y-v\le\delta,
\qquad\max(x-u,y-v)=\delta.
\]

The efficiency inequality `tau<=5P/4` gives

\[
0\le\delta\le A/4-5u/4.
\]

The remaining translations are direct:

\[
P\ge x+z\iff v\ge x+u,
\]

\[
z\le3P/4\iff v\ge A/4+3u/4,
\]

and

\[
z\ge x+y\iff v\le A-x-y.
\]

Thus the compact domain in Section 3 contains exactly the two normalized
inert faces, including their overlap.

## 5. Exact train decomposition and scalar logic

For fixed `w<A`, subtracting the two period trains term by term gives the
nonnegative exact gain `D_delta(w)`.  Reflection then gives, identically,

\[
F_{A+\delta}(a)+F_{A+\delta}(A-b)
=G_\delta(a,b)+\Theta(b).
\]

Applying this to `(x,u)` and `(y,v)`, and using
`C(A+delta)=C(A)+D_delta(0)`, proves (2.10) with no dropped term.

Since each theta term exceeds `-epsilon`, condition (3.2) forces every
literal endpoint-period lower bound positive.  Conversely, a nonpositive
train at a particular `delta` makes its actual pair sum an admissible value
in the infimum defining `Gamma(delta)` and therefore forces failure of the
strict scalar condition.  Both logical directions are correct.

## 6. Scope

The theorem signs one ceiling-plus-pair subsystem uniformly.  It does not
show that the same single ceiling margin simultaneously pays the second
pair; that unresolved correlation is exactly `Gamma(delta)`.  No complete
h=4, five-slot, all-slot, or OR-word theorem follows yet.
