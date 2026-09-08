# Audit: the August 4 theta machinery identifies the PBBS surplus kernel, but does not yet supply the uniform cross-residue cut

**Date:** 2026-08-07  
**Status:** unconditional asymptotic interface theorem and proof-scope
audit.  The volume-normalized two-row PBBS coefficient measure converges
to the derivative of the Rayleigh signed-tail kernel, and its residue sums
converge to the periodized derivative used in the Apéry queue analysis.
The cited August 4 theorems nevertheless do not imply all-depth
transport: they control a formal periodic Apéry tail in restricted
one-defect or bounded-overlap chambers, whereas the PBBS price has a
potentially leading finite Apéry shoulder.  No all-depth FC theorem is
claimed.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 K(x)=
 \begin{cases}
 1-e^{-(A-x)^2}-e^{-(A+x)^2},&0\le x\le A,\\
 -e^{-(A+x)^2},&x>A.
 \end{cases}
\tag{0.1}
\]

The point of this note is to distinguish three statements:

1. the PBBS volume-surplus kernel has the Rayleigh local limit;
2. its residue filter is exactly the periodized derivative of the
   August 4 Gaussian train;
3. positivity of that filter on every physical finite price does **not**
   follow from the existing formal-clock theorems.

The first two statements are proved below.  The third is a precise scope
obstruction, not evidence against the desired inequality.

## 1. Terminal volume normalization

Write

\[
 C_r={2r\choose r},
 \qquad
 R_r={4^r\over C_r},
\tag{1.1}
\]

and, at depth \(D\),

\[
 V_{r,D}
 =D C_r-\sum_{j=1}^{r-1}{2r\choose j}
 =C_r v_{r,D},
\tag{1.2}
\]

where symmetry gives the exact formula

\[
 \boxed{
 v_{r,D}=D+{1\over2}-{R_r\over2}+{1\over C_r}.}
\tag{1.3}
\]

Let \(r=r_D\) be the terminal index:

\[
 V_{r,D}>0,\qquad V_{r+1,D}\le0.
\tag{1.4}
\]

Wallis asymptotics and the exact recurrence

\[
 R_r=\sqrt{\pi r}\bigl(1+O(r^{-1})\bigr),
 \qquad
 {R_r\over R_{r-1}}={2r\over2r-1},
\tag{1.5}
\]

give

\[
 {D\over\sqrt r}\longrightarrow A,
 \qquad
 \sqrt r\,v_{r,D}=O(1),
\tag{1.6}
\]

and

\[
 \boxed{
 \sqrt r\bigl(v_{r-1,D}-v_{r,D}\bigr)
 \longrightarrow {A\over2}.}
\tag{1.7}
\]

Indeed, terminality places \(R_r\) within one increment
\(R_{r+1}-R_r=O(r^{-1/2})\) of \(2D+1\).  Moreover,

\[
\begin{aligned}
 v_{r-1,D}-v_{r,D}
 &={R_r-R_{r-1}\over2}
   +{1\over C_{r-1}}-{1\over C_r}\\
 &={R_r\over4r}+o(r^{-1/2}),
\end{aligned}
\tag{1.8}
\]

which proves (1.7).  Notice that the terminal fractional phase in
\(\sqrt r\,v_{r,D}\) need not converge.  It cancels from the leading
two-row coefficient below.

## 2. The two-row coefficient converges to \(-K'\)

For \(j\ge0\), put

\[
 H_{r-j}^{(2r)}
 ={2r\choose r-j}-{2r\choose r-j-1}.
\tag{2.1}
\]

The exact ballot form is

\[
 {H_{r-j}^{(2r)}\over C_r}
 ={2j+1\over r+j+1}\,
   {{2r\choose r-j}\over {2r\choose r}}.
\tag{2.2}
\]

If \(j/\sqrt r\to z\ge0\), the uniform central local limit gives

\[
 \sqrt r\,{H_{r-j}^{(2r)}\over C_r}
 \longrightarrow 2z e^{-z^2}.
\tag{2.3}
\]

For the complete depth-\(D\) row, define

\[
 f_{r,D}(L)
 ={1\over C_r}\left(
 {\bf1}_{L\le D}H_{r-D+L}^{(2r)}
 -\widetilde H_{r-D-L}^{(2r)}
 \right).
\tag{2.4}
\]

The rank-one modification in \(\widetilde H\) is outside every fixed
Gaussian compact set and is harmless under Gaussian tail domination.
For \(L/\sqrt r\to y\ge0\), equations (1.6) and (2.3) give

\[
 \sqrt r\,f_{r,D}(L)\longrightarrow b(y),
\tag{2.5}
\]

where

\[
\boxed{
 b(y)=
 2(A-y)e^{-(A-y)^2}{\bf1}_{y\le A}
 -2(A+y)e^{-(A+y)^2}
 =-K'(y).}
\tag{2.6}
\]

The value at \(y=A\) is interpreted by continuity.

The scaled two-row coefficient is

\[
 \widehat\mu_L
 =V_{r-1,D}\nu_{2r,D}(L)
  -V_{r,D}\nu_{2r-2,D}(L),
\tag{2.7}
\]

so, after dividing both births by their central rows,

\[
 {\widehat\mu_L\over C_rC_{r-1}}
 =v_{r-1,D}f_{r,D}(L)
  -v_{r,D}f_{r-1,D}(L).
\tag{2.8}
\]

Both normalized birth rows in (2.8) have the same limit (2.5).
Using (1.6)--(1.7),

\[
\boxed{
 {r\,\widehat\mu_L\over C_rC_{r-1}}
 \longrightarrow {A\over2}b(y)
 =-{A\over2}K'(y).}
\tag{2.9}
\]

The term containing
\(v_{r,D}(f_{r,D}-f_{r-1,D})\) is \(o(r^{-1})\);
the whole leading term is
\((v_{r-1,D}-v_{r,D})f_{r,D}\).
Thus (2.9) is independent of the fluctuating terminal volume phase.

Standard off-central binomial bounds give, uniformly in the terminal
sequence,

\[
 \sqrt r\,|f_{r,D}(L)|
 \le C(1+L/\sqrt r)e^{-c(L/\sqrt r)^2}.
\tag{2.10}
\]

Consequently (2.9) may be summed on arithmetic progressions and used in
Riemann sums.  This is the required domination; pointwise local CLT alone
would not justify the residue passage.

## 3. Exact limiting residue filter

Let \(h=h_D\) satisfy

\[
 {h\over\sqrt r}\longrightarrow P>0,
\qquad
 {a\over\sqrt r}\longrightarrow x\in[0,P],
\tag{3.1}
\]

and put

\[
 S_{h,a}=\sum_{j\ge0}\widehat\mu_{a+jh}.
\tag{3.2}
\]

Equations (2.9)--(2.10) and dominated convergence give

\[
\boxed{
 {2r\over A C_rC_{r-1}}S_{h,a}
 \longrightarrow
 Q_P(x):=\sum_{j\ge0}-K'(x+jP).}
\tag{3.3}
\]

At the critical terminal denomination \(h=D\), one has \(P=A\).
If

\[
 F(w)=\sum_{j\ge0}K(jA+w),
\tag{3.4}
\]

then the limiting PBBS surplus profile is exactly

\[
 \boxed{Q_A(w)=-F'(w).}
\tag{3.5}
\]

Thus the August 4 theta machinery has found the correct limiting
analytic object; no new Gaussian kernel has to be invented.

There is also an exact diagnostic from the Jacobi reflection identity

\[
 F(w)+F(A-w)=\rho(w).
\tag{3.6}
\]

Differentiation gives

\[
\boxed{
 Q_A(A-w)-Q_A(w)=\rho'(w)>0
 \qquad(0<w<A/2).}
\tag{3.7}
\]

The monotone zero-mean theta theorem therefore controls the small
reflected **antisymmetric** part of the PBBS residue filter.  It does not
by itself sign the full pairing against an arbitrary price defect; the
dominant symmetric part remains.

## 4. The exact Apéry-tail/shoulder split on the price side

Fix a minimum-density denomination \(h\) for a closed min-plus price and
write

\[
 m={p_h\over h},
 \qquad
 \delta(L)=\psi(L)-mL.
\tag{4.1}
\]

Then

\[
 \delta(L)\ge0,\qquad
 \delta(L+h)\le\delta(L),\qquad
 \delta(jh)=0.
\tag{4.2}
\]

For \(1\le a<h\), define the stabilized residue distance and its finite
shoulder by

\[
 d_a=\lim_{j\to\infty}\delta(a+jh),
 \qquad
 \eta_{a,j}=\delta(a+jh)-d_a.
\tag{4.3}
\]

The limits exist by (4.2), and

\[
 \eta_{a,j}\ge0,\qquad
 \eta_{a,j+1}\le\eta_{a,j},\qquad
 \eta_{a,j}\longrightarrow0.
\tag{4.4}
\]

Subadditivity of \(\delta\), followed by passage to far enough
representatives, gives the honest cyclic Apéry inequality

\[
\boxed{
 d_{(a+b)\bmod h}\le d_a+d_b.}
\tag{4.5}
\]

In contrast, the first representatives

\[
 e_a=\delta(a)
\tag{4.6}
\]

need not obey the carry version of (4.5).  A cheap partition of
\(h+a\) only proves that \(\delta(h+a)\) is cheap; it need not make
\(\delta(a)\) cheap.  This is precisely why the finite configuration LP
in the depth-eight theorem has genuine shared capacities rather than an
automatic cyclic-metric certificate.

For every finite signed coefficient measure, the exact decomposition is

\[
\boxed{
 \sum_L\widehat\mu_L\delta(L)
 =
 \sum_{a=1}^{h-1}S_{h,a}d_a
 +\sum_{a=1}^{h-1}\sum_{j\ge0}
       \widehat\mu_{a+jh}\eta_{a,j}.}
\tag{4.7}
\]

The first term is the formal periodic Apéry part.  The second is the
finite availability shoulder.

This distinction survives local CLT normalization.  In the hard regime
\(h\asymp D\asymp\sqrt r\), the Gaussian coefficient window
\(L=\Theta(\sqrt r)\) contains only \(O(1)\) translates of each residue.
There is no uniform reason for those first translates to have reached
their stabilized values.  The available all-slot conductor bound is
\(O(D^2)=O(h^2)\) in this regime, much larger than the active
\(O(h)\) window.  Hence the
shoulder term in (4.7) can be of the same leading order as the formal
term.

## 5. What the August 4 theorems actually certify

The match is useful but incomplete.

1. The cyclic prefix-minimum theorem applies to the stabilized profile
   \(d\), not automatically to the first-representative vector \(e\).
2. The all-period monotone-quadrature theorem closes the exact-first-carry
   **one-defect** long-wrap formal clock.  It does not state positivity of
   (4.7) for an arbitrary multidefect profile.
3. The multidefect reflected-ray theorem closes bounded overlap
   (\(H\le2\) under its terminal-coverage condition) and reduces the
   rest to a high-overlap scalar.  It explicitly leaves \(H\ge3\) and
   finite shoulders open.
4. The finite-shoulder Pareto theorem gives an exact min-plus recursion
   for every active shoulder prefix and an exact derivative-train
   decomposition, but explicitly leaves the sign of its final shoulder
   scalar open.  Thus it supplies the right state variables, not the
   missing inequality.
5. The later inverse-circle variance theorem closes the complete formal
   Rayleigh phase after first-minimum normalization in its stated period
   range.  It too keeps the finite shoulder as a separate queue.
6. The later physical-inverse half-line theorem proves that the shoulder
   breaks cyclic subadditivity exactly at wrapped sums and gives a
   saturated Bellman family for which the naive finite cyclic-variance
   extension is false.  Thus an unsigned prefix-moment argument cannot
   supply the missing cut; the location-sensitive signed shoulder term
   must be retained.

Accordingly, none of these theorems supplies the Farkas inequalities for
the uncompressed PBBS configuration LP, nor the shared-capacity
inequalities for its compressed multi-defect transport LP.

The right-endpoint quadrature argument remains valuable: through (3.7)
it gives the exact uniform control of the theta antisymmetry.  What is
missing is a theorem controlling the symmetric residue surplus jointly
with the shoulder in (4.7).

## 6. The exact next uniform target

A proof by this route needs two additional statements.

First, one needs a formal cross-residue cut, in a normalization matching
the admissible cyclic profile, of the schematic form

\[
 \int_0^P Q_P(x)d(x)\,dx\ge0
\tag{6.1}
\]

or its exact discrete analogue.  At \(P=A\), the theta theorem controls
the reflected error in \(Q_A\), but (6.1) still needs the multidefect
symmetric component.

Second, one needs a shoulder theorem showing that the second term in
(4.7) cannot erase the formal margin.  Equivalently, one may prove the
finite binomial transport LP directly.  Any asymptotic version must be
quantitative enough to dominate the uniform local-CLT and terminal
rounding errors; a merely pointwise \(o(1)\) limit is insufficient near
the linear-price null ray.

Thus the August 4 work provides the correct kernel, reflection identity,
and formal-tail geometry.  It does **not** currently certify asymptotic
binomial surplus transport for every min-plus price.  The remaining
obstruction is not another theta calculation: it is the uniform
multidefect-plus-shoulder cut in (4.7).

## 7. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| one-defect all-period theta quadrature | MATH_THEOREM_APERY_LONG_WRAP_MONOTONE_QUADRATURE_ALL_PERIOD_CLOSURE_20260804.md | 24f440d2b516618f7798b5f4e053de0f5b3253ad1825e7685e2494bddacf8ecd |
| cyclic prefix minima and multidefect overlap reduction | MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md | 28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e |
| exact finite-shoulder Pareto recursion and unsigned scalar gate | MATH_THEOREM_APERY_FINITE_SHOULDER_PARETO_FRONTIER_AND_ONE_DEFECT_COCYCLE_20260804.md | a15aff104c48a7e2fb095a06d00131489e2d9e5f0ea0940fc49d6127ab4b3def |
| complete formal cyclic variance closure | MATH_THEOREM_CYCLIC_APERY_INVERSE_CIRCLE_VARIANCE_CLOSURE_20260805.md | 173ff71dc06656cd7aeef62a209da76267581438bea64f7992dfe0485312b6a3 |
| exact physical inverse and sharp finite-wrap shoulder obstruction | MATH_THEOREM_RAYLEIGH_PHYSICAL_INVERSE_HALF_LINE_SUMSETS_AND_SHARP_SHOULDER_WRAP_BARRIER_20260805.md | e75ab25ed4854fbfde566797c02181af5eb1144e4207088b93d76255e18f9634 |
| finite cyclic PBBS transport LP | MATH_THEOREM_PBBS_VOLUME_SEED_ALL_PRICES_DEPTH8_AND_CYCLIC_APERY_TRANSPORT_LP_20260807.md | 33aad4dae1db10dea9d8c3df0aff0e445cc045bf778b27e88a15e90a4aa7892a |
