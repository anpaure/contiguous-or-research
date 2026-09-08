# Independent audit: six-slot full affine setup-cost monotonicity closure

**Date:** 2026-08-04  
**Verdict:** **GO.**  The audited theorem correctly proves strict positivity
for the complete six-slot affine setup-cost family.  The argument is
specific to grid six; it does not establish the analogous all-grid claim.

## 1. Frozen inputs

| role | file | SHA-256 |
|---|---|---|
| audited theorem | `MATH_THEOREM_SIX_SLOT_FULL_AFFINE_SETUP_COST_MONOTONICITY_CLOSURE_20260804.md` | `46dbd0b0fc9a6125a3143de0379ab6211e2c3e803d33f76e9245fa72cdc2192b` |
| affine clock theorem | `MATH_THEOREM_AFFINE_SETUP_COST_FIRST_CROSSING_AND_APERY_NO_DESCENT_20260804.md` | `408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce` |
| reflected compact-slope theorem | `MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_WY_SECOND_BOUNDARY_CLOSURE_20260804.md` | `6a44b458c013e3c553be3925f9439960b139262175aaf79bbb9fb50054f6c7d7` |
| reciprocal-ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |

All hashes were recomputed from the current local bytes.

## 2. Parameter conversion and full interval

For grid six, the affine family has

\[
 A=6\alpha-2\beta,\qquad x=c_1=\alpha-\beta.
\]

Solving gives

\[
 \alpha={A-2x\over4},\qquad
 \beta={A-6x\over4}.
\]

Consequently

\[
 0<\beta<{A\over4}
 \quad\Longleftrightarrow\quad
 0<x<{A\over6}
 \quad\Longleftrightarrow\quad
 0<t:={x\over A}<{1\over6}.
\]

Thus the theorem covers the entire admissible affine parameter interval,
not merely the balanced value.  The added endpoint `t=1/6` is exactly the
limit `beta=0` and is used only to anchor the monotonicity argument.

## 3. Exact residue clock

Put `p=1-t`.  Direct substitution into `c_r=r alpha-beta` gives

\[
 (s_0,s_1,s_2,s_3,s_4)
 =\left(0,t,{1\over4}+{t\over2},{1\over2},
                    {3\over4}-{t\over2}\right).
\]

The affine clock theorem says

\[
 V_m=\alpha m-\beta\left\lceil {m\over5}\right\rceil.
\]

Writing `m=5q+r`, with `0<=r<5`, gives exactly

\[
 {V_{5q+r}\over A}=qp+s_r.
\]

Differentiation therefore gives the complete slope row

\[
 (-q,\ 1-q,\ 1/2-q,\ -q,\ -1/2-q),
\]

as stated.  Uniform termwise differentiation is legitimate because
`p>=5/6`; the differentiated Gaussian tail is dominated by
`O((q+1)^2 exp(-c(q+1)^2))` uniformly in `t`.

## 4. Exhaustive derivative partition

### First reflected pair

The cells `(0,1)` and `(1,0)` contribute

\[
 A\bigl(K'(At)-K'(A(1-t))\bigr).
\]

Here `0<=t<=1/6<=1/3`.  Corollary 2.3 of the reflected-slope theorem,
with its high argument chosen as `1-t`, gives

\[
 K'(A(1-t))>K'(At),
\]

so this pair is strictly negative.

### Second reflected pair

Let `u=1/4+t/2`.  Then `1/4<=u<=1/3`, `s_4=1-u`, and the cells `(0,2)`
and `(0,4)` contribute

\[
 {A\over2}\bigl(K'(Au)-K'(A(1-u))\bigr)<0
\]

by the same authenticated corollary.  The upper endpoint `u=1/3` remains
inside its proved closed range.

### Stationary and tail cells

The only zero-slope cells before the generic tail are

\[
 (0,0),\qquad(0,3),\qquad(1,1).
\]

For `q=1`, the remaining residues `r=2,3,4` have respective slopes
`-1/2,-1,-3/2`, and their smallest normalized argument is

\[
 p+s_2=1+{1-2t\over4}>1.
\]

For `q>=2`, all five slopes are strictly negative and

\[
 qp+s_r\ge2p\ge{5\over3}>1.
\]

On the physical tail `y>A`,

\[
 K'(y)=2(A+y)e^{-(A+y)^2}>0.
\]

Every such slope-times-derivative contribution is therefore strictly
negative.  These two reflected pairs, the three stationary cells, the
three `q=1` tail cells, and all `q>=2` cells partition the derivative
without omission or overlap.  Hence

\[
                         \Phi'(t)<0.
\]

## 5. Endpoint identification

At `t=1/6`,

\[
 p={5\over6},\qquad s_r={r\over6}\quad(0\le r<5).
\]

Thus the arguments are

\[
 {A(5q+r)\over6}.
\]

Euclidean division by five shows that `(q,r)` runs through every
nonnegative integer exactly once.  Therefore

\[
 \Phi(1/6)=\sum_{m\ge0}K(mA/6)=C(A/6)>0,
\]

where the last inequality is precisely the fixed reciprocal-ceiling
positivity theorem with reciprocal parameter six.  Strict decrease now
gives

\[
 \Phi(t)>\Phi(1/6)>0\qquad(0<t<1/6).
\]

## 6. Scope boundary

The proof uses only two reflected pairs, whose smaller normalized
arguments are at most `1/3`.  For larger affine grids additional pairs
approach `1/2`, outside the cited reflected-slope theorem.  Accordingly,
the audited result closes the full affine family at grid six only.  It
does not close the whole six-slot `h=5` branch, arbitrary grid size,
complete Bellman positivity, or an OR-word upper bound.

