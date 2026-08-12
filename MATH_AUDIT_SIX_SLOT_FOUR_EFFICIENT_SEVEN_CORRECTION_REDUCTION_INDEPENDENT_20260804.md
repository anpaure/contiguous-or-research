# Independent audit: six-slot `h=4` three-maxima, seven-correction reduction

**Date:** 2026-08-04  
**Method:** pure Apéry-path and Bellman-capacity algebra only; no numerical
search or enumeration.  
**Audited source:**
`MATH_THEOREM_SIX_SLOT_FOUR_EFFICIENT_SEVEN_CORRECTION_REDUCTION_20260804.md`  
**Audited source SHA-256:**
`fa362d05e586749467f9d5acb5f20883825d82505da71fba97fec678b4c213f9`

## Verdict

**PASS as an exact reduction after a presentation-only source patch.**
The source was amended to list three inherited canonical inequalities
that its sign argument already used (`x<=u`, `y<=v`, and
`z<=3P/4`), to state `x,y,z>=0`, and to repair malformed TeX spacing.
Those facts follow respectively from internal superadditivity and the
size-four maximum-density condition; the mathematical statement was not
strengthened.  The three inert endpoint faces remain unsigned.

## 1. Apéry maxima

For

\[
 d_1=u-P/4,\qquad d_2=v-P/2,\qquad d_3=z-3P/4,
\]

all three weights are nonpositive and `d_2>=2d_3` is exactly
`v>=2z-P`.

Applying these inequalities to the twelve canonical simple-path forms
leaves:

\[
 \beta_1=\max\{d_1,d_2+d_3\},
 \qquad
 \beta_2=\max\{d_2,2d_1\},
\]

and

\[
 \beta_3=\max\{d_3,d_1+d_2,3d_1\}.
\]

Adding the residue baselines gives exactly

\[
 s_1=\max\{u,v+z-P\},
 \quad
 s_2=\max\{v,2u\},
 \quad
 s_3=\max\{z,u+s_2\}.
\]

Every domination used here has the stated direction; in particular,
`3d_3<=d_2+d_3` and `2d_3<=d_2` both follow from the same endpoint
inequality.

## 2. Exact availability head

The formal four-coset clock and the literal Bellman clock differ exactly
at capacities

\[
 1,2,3,5,6,7,11.
\]

The literal values there are respectively

\[
 x, y, z, P+u, P+v, P+g, 2P+h,
\]

where

\[
 g=\max\{z,u+y,v+x\},
 \qquad
 h=\max\{z,u+v\}.
\]

This follows directly by listing the complementary decompositions at
capacity seven.  The asserted capacity-eleven maximum also survives all
shorter representatives: the Bellman recurrence gives

\[
\begin{aligned}
 x+V_{10}&\le2P+\max\{z,u+v\},\\
 y+V_9&\le2P+\max\{z,u+v\},\\
 P+V_7&\le2P+\max\{z,u+v\},
\end{aligned}
\]

using `x<=u`, `y<=v`, `v>=u+x`, `v+y<=P`, and
`g<=max{z,u+v}`.  The remaining recurrence terms are exactly
`2P+z` or `2P+u+v`.  Hence no lower-capacity surrogate for the formal
`3u` term creates an eighth correction.

Capacities eight, nine, and ten realize

\[
 2P,
 \quad2P+s_1,
 \quad2P+s_2,
\]

respectively.  Direct recurrence checks use
`x+z<=P`, `v>=u+x`, `v+y<=P`, and `2z<=P+v` to dominate every other
partition.  At capacity fifteen, three size-five generators make the
last `3u` form available, so capacities twelve through fifteen realize
all four stabilized residues.  Padding by size-four generators proves
equality thereafter.  Subtracting the seven unavailable formal values
therefore gives exactly equation (2.2), with no hidden eighth correction.

## 3. Sign and endpoint checks

Internal superadditivity gives `x<=u` and `y<=v`, while the Apéry formulas
give `u<=s_1`, `v<=s_2`, and `z<=s_3`.  Maximum efficiency gives

\[
 s_1\le P/4,
 \quad s_2\le P/2,
 \quad s_3\le3P/4.
\]

Thus all arguments in the first three corrections lie in
`[0,3A/4]`, where `K` is decreasing, and those corrections are indeed
nonnegative.  No sign is inferred for the four late corrections.

Endpoint saturation is precisely

\[
 v=\max\{A-P,x+u,y,2z-P\},
\]

so the four named faces exhaust the endpoint.  On `v=A-P`, the literal
endpoint is `c_6=A`.  The proof of the audited subcomplementary-pair
bound uses only this equality, internal superadditivity, and the literal
period-six comparison; it does not require size six to be the selected
maximum-density denomination.  Hence the strict margin `163/70000`
applies exactly as stated.

## 4. Scope check

The source closes only the threshold face.  It reduces the union of the
other three faces to four correlated late corrections and does not sign
them.  It therefore does not close `h=4`, grid six, or any all-grid
Bellman inequality.
