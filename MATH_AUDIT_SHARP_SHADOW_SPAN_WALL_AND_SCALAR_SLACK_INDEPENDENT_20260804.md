# Independent audit: sharp shadow, coordinate span, pinned wall, and scalar slack

**Date:** 2026-08-04  
**Method:** pure mathematics and direct inspection of the cited primary
source; no finite-instance search, solver, or remote computation  
**Verdict:** **GO at the scopes stated below.**  I found no false numerical,
logical, or asymptotic implication in the four audited artifacts.  One
presentational correction was applied to the coordinate-cover outcome:
its asymptotic aperture count is a lower bound, not an equality.  The wall
result is a one-wall reproduction theorem, not an elimination or iterable
descent theorem, and the slack result is scalar only.

## 1. Audited artifacts

- `MATH_THEOREM_SHARP_OPTIONAL_THRESHOLD_SHADOW_VIA_PARTIAL_SHADOW_20260804.md`,
  SHA-256
  `90748e697d5dd10eb5b8a5cf35b849da16f73f6b188f6b3f589ec0e6e43e785b`;
- `MATH_COROLLARY_OPTIONAL_CORE_COORDINATE_SPAN_AND_LOCAL_CUBE_COVER_20260804.md`,
  SHA-256
  `2dc608be41bd7f67ca8fd0c1a368967c2aed76341470117060eb7467e16f0c40`;
- `MATH_THEOREM_CORE_PINNED_WIDE_GAP_WALL_DESCENT_FOR_OPTIONAL_CORES_20260804.md`,
  SHA-256
  `8f00f4e6025a5c5c40efb8e0f72e864d64b312b90eee3b364be8a8ac6631e822`;
- `MATH_THEOREM_SCALAR_SLACK_PARITY_GRANULARITY_AND_EQUIDISTRIBUTION_20260804.md`,
  SHA-256
  `17ba23aa2b3e91d3bf8c80ba374589316d1cb12a8a253d376f42824387627be8`.

The pinned-wall audit also checks the exact way in which the argument uses
the already frozen core-pinned reservoir, optional-DM, and near-shadow
localization theorems.  It does not reprove those dependencies from first
principles.

## 2. Direct primary-source check of the partial-shadow input

I inspected arXiv:2307.15380v3, Chao--Yu, *Tight Bound and Structural
Theorem for Joints*, specifically the source theorem labelled
`theorem:PartialShadow` and its proof:

<https://arxiv.org/abs/2307.15380v3>.

The quoted input is accurate.  In the paper's notation, if an (m)-member
family of (r)-sets has at most (s) missing facets per member and

\[
 m=\binom{x}{r-s},\qquad x\ge r-s,
\]

then every supplying family of ((r-1))-sets has size at least

\[
 \binom{x}{r-s-1}.
\]

The primary source also gives the stated equality structure: one fixed
redundant (s)-set and the two consecutive complete layers on an
(x)-set.  In an equality instance this of course forces (x) to be an
integer; the present application has (x=2D-1), so there is no hidden
integrality issue.

With

\[
 r=k+1,\qquad s=r-D,\qquad
 (\mathcal J,\mathcal F)=(\mathcal C,\mathcal A),
\]

the hypothesis “at least (D) selected facets” is exactly “at most (s)
missing facets.”  If

\[
 |\mathcal C|=\binom{x}{D},
\]

then the source theorem gives

\[
 |\mathcal A|\ge\binom{x}{D-1}.
\]

The balance chain

\[
 \binom{x}{D}=|\mathcal C|
 \ge |\mathcal A|
 \ge \binom{x}{D-1}
\]

and the exact ratio

\[
 \frac{\binom{x}{D}}{\binom{x}{D-1}}
 =\frac{x-D+1}{D}
\]

force (x\ge2D-1).  Equality in the final lower bound forces equality at
every step, hence the Chao--Yu equality classification applies.  Therefore
strict shore imbalance excludes equality and gives the integral (+1).
The optional substitution (D=d-3) is arithmetically exact:

\[
 |B^-|\ge\binom{2d-7}{d-4}+1.
\]

**Verdict for the sharp-shadow theorem: GO.**  The only external input is
the deep Chao--Yu theorem itself; this audit verifies its statement and
applicability, not its polynomial-method proof line by line.

## 3. Coordinate span and local-cube cover

For a common-rank family (B\subseteq[C,U]) with
(h=|U\setminus C|), the deletion map (S\mapsto S\setminus C) places
the family in one rank of an (h)-cube.  Hence

\[
 |B|\le\binom{h}{t}
 \le\binom{h}{\lfloor h/2\rfloor}.
\]

The central binomial coefficient is strictly increasing with (h).
Consequently

\[
 |B|>\binom{2D-1}{D-1}
 \quad\Longrightarrow\quad h\ge2D.
\]

Applying the same bound separately to every interval in a cover and then
using the union bound gives the displayed cover-number lower bound.  For
fixed (C), with (h=D+C), the ratio of the two central coefficients is

\[
 \frac{\binom{2D-1}{D-1}}
      {\binom{D+C}{\lfloor(D+C)/2\rfloor}}
 =2^{D-C+O(1)}.
\]

After (D=d-3), writing this as (2^{d-C+O(1)}) merely absorbs an
absolute factor in the (O(1)) exponent.

**Verdict for the span/cover corollary: GO after one presentation fix.**
Equation (0.6) now reads `t >= 2^(d-C+O(1))`; the earlier bare asymptotic
expression could be misread as an equality, for which no matching upper
cover is proved.  The result is a necessary localization obstruction only.
It supplies no theorem that the actual damage family has such a bounded
interval cover.

## 4. Core-pinned wall theorem

### 4.1 Coinstantiated forbidden bank

For an owner with (h\) core coordinates there are

\[
 \binom{m-1}{h}\binom mh
\]

choices, and each has (m) facets.  Summing through (h=d), with
(d=O(\sqrt m)), gives (2^{o(m)}), as claimed.

The low-path separation has a strict one-unit gap: a low protected colour
has external trace at most (m-d-2), whereas a facet below an owner with
(h<d+1) has external trace at least (m-d-1).  Adding the new bank to
the high-tail greedy exclusions changes a (2^{m+o(m)})-scale forbidden
bank by only (2^{o(m)}), against the already proved
(2^{2m-o(m)})-scale resource denominators.  Thus the inherited union
bound remains (2^{-m+o(m)}).

### 4.2 Wall gap

If (h(U)<d+1), every facet of (U) lies in the enlarged forbidden bank,
so only the deterministic top palette can be protected.  Simplicity gives
at most one protected same-external-trace facet, and the cyclic
one-point-completion lemma gives at most two external deletions.  There are
(m-1) wall facets, hence

\[
 g_U^{(1)}\ge m-4\ge d-2
\]

asymptotically.

If (h(U)\ge d+1), at most (e=m-h(U)) protected wall facets arise by
external deletion and at most two by core deletion.  Deleting the pinned
coordinate is off the wall and is unprotected because all protected
physical colours contain that coordinate.  Thus

\[
 g_U^{(1)}\ge(m-1)-(e+2)=h(U)-3\ge d-2.
\]

### 4.3 Shore balance and reproduction

For an off-wall owner, all protected degrees vanish, so
(g_U=m,c_U=2).  Positive optional capacity forces at least (m-1)
members of (B_0) below every member of (Q_0).  If
(|Q_0|\ge|B_0|>0), the sharp threshold-shadow theorem with (D=m-1)
would give

\[
 |B_0|\ge\binom{2m-3}{m-2}=2^{2m-o(m)},
\]

contradicting the inherited near-shadow localization
(|B^-|=O(m^2 2^m)).  Empty-side cases are also handled correctly, so
(|Q_0|\le|B_0|), and strict total imbalance gives
(|Q_1|>|B_1|).

For (U\in Q_1), the unique off-wall facet is the one deleting the pinned
coordinate.  The capacity inequality and the wall gap leave at least
(d-3) selected wall facets.  Removing the common pinned coordinate from
both shores produces adjacent ranks satisfying the sharp-shadow theorem,
and therefore reproduces the full bound and the (2d-6) coordinate span
inside the wall.

**Verdict for the pinned-wall theorem: GO relative to its named frozen
dependencies.**  Its exact conclusion is reproduction on one protected
side.  It neither eliminates the reproduced core nor proves that a second
wall may be imposed while preserving all hypotheses.  “Descent” must not
be read as an already established iteration.

## 5. Scalar slack

### 5.1 Exact parity formulas and quotient law

For (C_m=\binom{2m}{m}) and (A_m=4^m/(2C_m)), direct symmetry gives

\[
 W_m^-=C_m/2,\quad \Lambda_m^-=2^{2m-2}-1,
\]

and

\[
 W_m^+=C_m,\quad
 \Lambda_m^+=2^{2m-1}-C_m/2-1.
\]

Thus (Lambda=W(A_m-\eta)-1), with
(eta=0,1/2), exactly.  Writing
(Lambda=qW+\rho), only (q) and (q+1) can be the minimal depth once
(T_{q+1}<W), which holds asymptotically because (q=O(\sqrt m)) while
(W) is exponential.  The two cases and (0\le\sigma<W+d) follow.

### 5.2 Dyadic congruence and fixed-slack equations

Kummer gives

\[
 v_2(C_m)=s_2(m).
\]

After reducing the odd phase denominator to (u_m) and the even phase
denominator to (2u_m), both parities have granularity
(g_m=2^{s_2(m)-1}).  Hence

\[
 \sigma\equiv\binom{d+1}{2}+1\pmod {g_m}.
\]

The two displayed Diophantine identities follow by substitution and
multiplication by two.  For fixed ((d,s)) with positive correction,
(R_m=4^m/C_m) increases strictly while the correction divided by (C_m)
decreases strictly, so there is at most one solution.  The remaining
nonpositive-correction depths form a finite set for fixed (s).  This
justifies the (O_S(\sqrt K)) near-zero count.

Here (d) in the “equivalence” statement is the already defined minimal
depth.  The bare exponential equation, if presented with an unconstrained
new variable (d), should be regarded only as a necessary candidate
equation until minimality is checked.  The subsequent uniqueness argument
uses it in the safe direction, so this wording point does not affect any
conclusion.

### 5.3 Equidistribution and square-root-scale liminf

Stirling gives

\[
 A_m=\frac{\sqrt{\pi m}}2+O(m^{-1/2}).
\]

The sequence (alpha\sqrt m+\beta) is uniformly distributed modulo one
for every nonzero (alpha); the stated second-derivative estimate on
dyadic blocks is sufficient.  A perturbation tending to zero preserves
uniform distribution.  Outside a density-zero set where
(\{\Lambda/W\}\le T_q/W), the exact quotient law gives

\[
 \frac\sigma W=1-\{\Lambda/W\}+O(m/W).
\]

This proves the paritywise uniform limiting law.  Fixed-interval uniform
distribution also suffices for the shrinking-endpoint density-one claim:
eventually every bad set lies in any prescribed fixed endpoint
neighbourhood, after which the neighbourhood width may tend to zero.

For the stronger liminf, the squared expansion

\[
 A_m^2=\frac\pi4\left(m+\frac14+
              \frac1{32m}+O(m^{-2})\right)
\]

is correct.  The polynomial

\[
 u_n=\frac{4(n+\eta)^2}{\pi}-\frac14
\]

is uniformly distributed modulo one because its quadratic coefficient is
irrational.  For each prescribed shrinking interval one may first fix its
width and then choose an arbitrarily large (n) in it; this allows both
(1/m=o(\varepsilon)) and the Stirling remainder to be absorbed.  With
(m=\lfloor u_n\rfloor), (A_m-\eta-1/W) lies immediately below the
integer (n) by (O(\varepsilon/\sqrt m)).  It is therefore in the
second quotient case, and

\[
 \liminf\sqrt m\,\frac\sigma W=0
\]

on both parities.  Replacing (sqrt m) by (sqrt k) changes only a
constant factor.

**Verdict for the scalar-slack theorem: GO.**  It proves neither a uniform
polynomial lower bound nor finiteness of zero slack.  It also cannot round
the lower deck: its correct constructive target remains the excess
(D-\sigma), not the total duplicate count (D).

## 6. Combined scope verdict

The four artifacts are mutually consistent:

1. Chao--Yu forces every optional core to have
   (4^{d+O(1)}/\sqrt d) size.
2. Such a core spans at least (2d-6) free coordinates and requires
   exponentially many deadline-sized interval pieces.
3. One pinned wall reproduces, rather than destroys, this core on its
   protected side.
4. Scalar slack is often large but has arbitrarily small
   (o(W/\sqrt k)) subsequences, so it cannot replace the missing
   occurrence-labelled structural theorem.

None of these statements proves (B(k)+O(1)) or exact equality for all
dimensions.  Apart from the corrected comparison sign in the cover
corollary, no source correction is required by this audit.
