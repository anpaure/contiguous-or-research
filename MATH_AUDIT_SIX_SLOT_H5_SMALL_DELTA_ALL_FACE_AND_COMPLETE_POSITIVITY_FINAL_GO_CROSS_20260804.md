# Final cross-audit: six-slot `h=5` all-face small-excess closure

**Date:** 2026-08-04  
**Method:** independent symbolic replay of the all-face globalization, both
reflection branches above the half point, the compact endpoint minima, all
three theta charges, the complete `u` split, and the threshold/large-excess
gluing.  No search, solver, sampled computation, or numerical optimization
was used.

**Audited theorem:**
`MATH_THEOREM_SIX_SLOT_H5_SMALL_DELTA_ALL_FACE_AND_COMPLETE_POSITIVITY_20260804.md`,
SHA256
`59551dcca1dcd923e1d05fda17d7b491f2ff37f8a37ddd6ab8faf5dd0522854d`.

## 0. Verdict

**FINAL GO.**  The theorem closes the entire compact physical union of the
three inert endpoint faces for `0<delta<A/15`, including every pairwise and
triple face intersection.  Together with the frozen threshold and
large-excess theorems, it proves complete positivity of the canonical
six-slot least-maximum-density `h=5` branch.

The proof does not import the face-`Z` equality `A-2m=delta`.  It uses only
the universal endpoint inequality `A-2m<=delta`, which holds on faces
`X`, `Y`, and `Z` alike.

## 1. Universal third-ray bank

For every point of the compact physical polytope,

\[
                         A-2m\le\delta
\]

gives

\[
 m\ge{A-\delta\over2}>{7A\over15}
 \qquad(0<\delta<A/15).
\]

Also `0<=y<=2A/5`.  The period-uniform no-interior-minimum theorem says
that the minimum of `F` on `[0,2A/5]` is attained at an endpoint.  Since the
frozen anchor satisfies `F(2A/5)<C=F(0)`,

\[
                         F(y)\ge F(2A/5)
 >{18879\over1000000}.
\]

If `m<=A/2`, then `m>7A/15>4A/25`; strict decrease on
`[4A/25,A/2]` gives

\[
 F(m)<F(7A/15)<{7121\over1000000}.
\]

The theorem writes the first inequality weakly, which is harmless.  If
`m>A/2`, the full physical polytope has `m<=A`, so
`0<=A-m<A/2`.  Lower-half positivity and reflection give

\[
 F(m)=\Theta(m)-F(A-m)<\varepsilon
 ={50\over1000000}<{7121\over1000000}.
\]

Thus, uniformly on all endpoint faces,

\[
                         F(y)-F(m)>
 {18879-7121\over1000000}
 ={11758\over1000000}.
\]

No equality identifying the active endpoint face occurs in this argument.

## 2. Endpoint minima for `x` and `y`

The no-interior-minimum theorem on `[0,A/4]` and the strict frozen quarter
anchor `F(A/4)>C` imply

\[
                         F(x)\ge C
 \qquad(0\le x\le A/5).
\]

This justifies

\[
 C-F(u)+F(x)-F(v)
 \ge2C-F(u)-F(v).
\]

Likewise, the same endpoint-minimum principle on `[0,2A/5]` is exactly the
source of the `y` floor used in Section 1.  Neither step assumes ordinary
monotonicity near zero.

## 3. The `v>A/2` chamber

The physical rows include

\[
                         0\le v\le A.
\]

When `v>A/2`, put `w=A-v`, so `0<=w<A/2`.  Then lower-half positivity and
Jacobi reflection yield

\[
                         F(v)=\Theta(v)-F(A-v)<\varepsilon.
\]

This is stronger than each of the three prices

\[
 {49730\over1000000},\qquad
 {48000\over1000000},\qquad
 {45160\over1000000}.
\]

Hence none of the `u` cases silently assumes `v<=A/2`.  When `v<=A/2`, its
lower bounds `A/5`, `9A/40`, or `A/4` all lie beyond the monotonicity
threshold `4A/25`, so the corresponding point-anchor comparison has the
correct direction.

## 4. Exhaustive `u` split and exact margins

The physical interval is `0<=u<A/6`.  The three closed/half-open cases

\[
 [0,A/32],\qquad[A/32,A/16],\qquad[A/16,A/6)
\]

cover it completely; overlaps at `A/32` and `A/16` are harmless because
both adjacent estimates apply.

### Case I

For `0<=u<=A/32`, use

\[
 F(u)<49000/10^6,qquad v\ge A/5,qquad
 F(v)<49730/10^6.
\]

With `C>44024/10^6`,

\[
 2C-F(u)-F(v)>{88048-49000-49730\over10^6}
 =-{10682\over10^6}.
\]

### Case II

For `A/32<=u<=A/16`,

\[
 v\ge{A+4(A/32)\over5}={9A\over40},
\]

so

\[
 2C-F(u)-F(v)>{88048-51000-48000\over10^6}
 =-{10952\over10^6}.
\]

### Case III

For `A/16<=u<A/6`,

\[
 v\ge{A+4(A/16)\over5}={A\over4},
\]

and therefore

\[
 2C-F(u)-F(v)>{88048-53300-45160\over10^6}
 =-{10412\over10^6}.
\]

Every subtraction is exact and uses a strict source inequality.

## 5. Period gains and theta charge

The exact reflected decomposition is

\[
 \mathscr E_5=T_5+\sum_{j=1}^6D_j
 +\Theta(u)+\Theta(v)+\Theta(m).
\]

All six period gains are nonnegative.  On the all-face polytope no theta
term has a uniformly positive sign: unlike face `Z`, `m` may exceed `A/2`.
The proof therefore correctly charges all three terms by

\[
                         3\varepsilon={150\over10^6}.
\]

Adding the universal third-ray bank gives the three exact margins

\[
 {11758-10682-150\over10^6}={926\over10^6},
\]

\[
 {11758-10952-150\over10^6}={656\over10^6},
\]

and

\[
 {11758-10412-150\over10^6}={1196\over10^6}.
\]

Thus `656/10^6` is the correct uniform minimum.  Since the literal
endpoint-period theorem gives `Phi>=mathscr E_5`, every physical table in
the interval has `Phi>656/10^6`.

## 6. Complete branch gluing

The canonical `h=5` normalization has exactly the ranges

\[
 \delta=0,qquad 0<\delta<A/15,qquad
 A/15\le\delta<A/5.
\]

The threshold predecessor gives `Phi>163/70000`; the present theorem gives
`Phi>656/10^6`; and the large-excess predecessor gives
`Phi>59573/132500000`.  The shared endpoint `delta=A/15` belongs to the
large-excess result, while the formal endpoint `delta=A/5` is excluded from
the physical inert stratum.  The three ranges are exhaustive and disjoint as
used.

Therefore no canonical inert `h=5` region remains open.  This closes only
the least-maximum-density branch `h=5`; the theorem correctly does not claim
complete six-slot positivity without separate closure of the other
least-density branches.

## 7. Frozen dependency verification

All six direct dependencies exist at exactly their declared SHA256 values:

| role | SHA256 |
|---|---|
| reflected physical polytope and decomposition | `2f26836e6c46974153136e45247ae10c3f5ff44a8bd9f55d60e511b98d091aef` |
| large-excess closure and two-fifths anchor | `34dfb968b14876fdd190183eef29723475ca2c6c537faac8b807c641dd4fba1a` |
| face-`Z` compact bounds and point anchors | `5b9fc5880b0b8717036b744c2639928cfd84d27f57d0b4d5aca125afec0243d5` |
| exact threshold theorem | `4a751598067165d88cd1e01e0406c3dce09c941cbba7fa0dd95487d0ff3e4b59` |
| no-interior-minimum theorem | `f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3` |
| quarter anchor | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |

The audited theorem remains unchanged at SHA256
`59551dcca1dcd923e1d05fda17d7b491f2ff37f8a37ddd6ab8faf5dd0522854d`.
