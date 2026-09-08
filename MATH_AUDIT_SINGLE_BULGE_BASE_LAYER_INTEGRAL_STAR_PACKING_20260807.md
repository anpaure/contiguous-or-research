# Audit of the single-bulge base-layer integral star packing

**Date:** 2026-08-07  
**Object audited:** `MATH_THEOREM_SINGLE_BULGE_BASE_LAYER_INTEGRAL_STAR_PACKING_20260807.md`  
**Verdict:** **PASS in its stated triangular/asymptotic regime**, with one
necessary explicit hypothesis correction: the theorem must assume `d>=2`
(and hence `R=3(d-1)>0`) and a nonempty base layer `s>=1`.  Without this,
the displayed ratios divide by `R` at `d=1`.

## 1. Literal lift

In the length-`3d` schedule `L^(d-1) H` repeated three times, the number of
low phases is

\[
 R=3(d-1).
\]

With `P=C_0-H`, one has

\[
 |P|=(m-d-1)-d=m-2d-1=s-1.
\]

At a low singleton phase the rank-`s` suffix target is exactly `P+x`.
Distinct low private labels therefore give exactly the `R`-petal star

\[
 \{P+x:x\in L\}.
\]

Conversely, outside an `(s-1)`-set `P` there are

\[
 v=n-s+1
\]

labels.  After reserving `R=3d-3` low labels, choosing a `d`-set `H` and
three high private labels requires `d+3` more.  The condition is exactly

\[
 v-(3d-3)\ge d+3
 \quad\Longleftrightarrow\quad v\ge4d.
\]

Thus (1.3) is both the correct elementary supply condition and sufficient
for the cited literal hinge realization.  Auxiliary banks may overlap
between rings because this theorem claims disjointness only of the named
base targets.

## 2. Greedy incidence bound

The inclusion graph is `(v,s)`-biregular, so `Cv=Vs`.  Let

\[
 w=v-R+1.
\]

At termination, every unselected centre is incident with at least `w` used
targets.  Hence the number of incidences from unselected centres to used
targets is at least `(C-M)w`.  There are `U=MR` used targets and each has
only `s` centres, so it is at most `MRs`.  Therefore

\[
 (C-M)w\le MRs,
 \qquad
 M\ge {Cw\over Rs+w}.
\]

Using `Cv=Vs` and multiplying by `R/V` gives exactly

\[
 {U\over V}\ge {Rsw\over v(Rs+w)}.
\]

In the triangular regime, `R=Theta(d)`, `s,v=Theta(n)`, and `n=Theta(d^2)`.
The two multiplicative losses are

\[
 1-{w\over v}=O(R/v)=O(1/d),
 \qquad
 1-{Rs\over Rs+w}=O(v/(Rs))=O(1/d).
\]

Thus (2.5) is correct.

## 3. Capacity statement and scope

For `s=m-2d` and the optimal triangular scale, the local central-binomial
ratio is

\[
 {\binom{2m+1}{m-2d}\over\binom{2m+1}{m}}
 \longrightarrow e^{-\pi}.
\]

Consequently the packing supplies `(e^(-pi)-o(1))W` pairwise distinct
rank-`s` endpoints.  Since

\[
 e^{-\pi}\approx0.04321,
 \qquad
 \theta=4\sum_{a\ge1}e^{-4\pi a^2}\approx1.395\cdot10^{-5},
\]

the advertised factor above the theta demand is indeed over `10^3`.

The conclusion is correctly scoped to the base row.  The greedy proof does
not control collisions among higher marked targets, bridge targets, owners,
upper colours, or auxiliary banks.  It therefore gives a large integral
candidate reservoir, not an integral hinge factor.

## 4. Required textual correction

Add near the start:

> Assume `d>=2`, `s>=1`, and `n-s+1>=4d`.

The supply condition already appears later as (1.3); moving it into the
theorem's ambient hypotheses would make the quantifier exact.  No other
formula requires correction.

