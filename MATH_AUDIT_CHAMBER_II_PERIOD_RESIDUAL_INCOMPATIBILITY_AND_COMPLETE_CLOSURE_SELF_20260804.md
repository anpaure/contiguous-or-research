# Self-audit: Chamber-II period-residual incompatibility and closure

**Date:** 2026-08-04

**Audited theorem:**
`MATH_THEOREM_CHAMBER_II_PERIOD_RESIDUAL_INCOMPATIBILITY_AND_COMPLETE_CLOSURE_20260804.md`

**Audited theorem SHA-256:**
`52ec7f4ac4dbe9f0a32e5eed063cf5bf8419c535575a631b16d8c98d31e40a68`

**Method:** independent symbolic expansion of the normalized train and
period residual, followed by a separate replay of the compact derivative
bounds and global-minimum argument.  No numerical search or finite
parameter partition was used.

## 1. Verdict

**GO.**  On the residual domain

\[
 {4\over5}<\rho<{11\over12},
 \qquad0<x<{1-\rho\over2},
\]

the shift stationarity equation

\[
                         T_\rho(x)+2T_\rho(2x)=0
\]

forces the normalized period residual to be strictly positive.  It is
therefore incompatible with period stationarity.  The bounded KKT locus is
empty, the long-wrap train is positive for every admissible period, and the
frozen stationary-strip theorem closes all of Chamber II.

## 2. Normalization audit

For

\[
 \kappa(u)={K'(Au)\over2A},
\]

direct differentiation of the compact and tail branches gives

\[
 \kappa(u)=
 \begin{cases}
 h(1+u)-h(1-u),&0\le u\le1,\\
 h(1+u),&u\ge1.
 \end{cases}
\]

Because `0<=s<=1-rho`, the `q=0,1` terms are exactly the two compact
rows and all `q>=2` terms are tails.  Hence

\[
                         T_\rho(s)=\sum_{q\ge0}\kappa(q\rho+s).
\]

Differentiating `Q_(A rho)(A x)` with respect to `x` and `rho` gives,
up to the same positive factor `2A^2`,

\[
 G(\rho,x)=T_\rho(x)+2T_\rho(2x)
\]

and

\[
 \mathcal R(\rho,x)
 =\sum_{q\ge1}q\{
 \kappa(q\rho)+\kappa(q\rho+x)+\kappa(q\rho+2x)\}.
\]

Thus the two zero equations used in the theorem are the exact two free
first-order conditions.

## 3. Compact slope audit

On `[0,1]`,

\[
                         \kappa'(t)=h'(1+t)+h'(1-t).
\]

The reflected-curvature theorem gives

\[
                         \kappa''(t)=h''(1+t)-h''(1-t)\ge0
 \qquad(0\le t\le1/2).
\]

So `kappa'` is nondecreasing.  The corrected outer-period certificate
proved

\[
                         h'(6/5)<-{2\over5}.
\]

Moreover

\[
 h'(4/5)=e^{-4\pi/25}left(1-{8\pi\over25}\right)<0
\]

because `pi>25/8`.  Consequently

\[
 \kappa'(t)\le\kappa'(1/5)
 =h'(6/5)+h'(4/5)<-{2\over5}
\]

for every `0<=t<=1/5`.

For `4/5<u<1`,

\[
                         \kappa'(u)=h'(1+u)+h'(1-u)<1.
\]

The first summand is negative; the second is strictly below one because
`1-u>0`, its Gaussian factor is below one, and its remaining factor is at
most one.

The residual domain gives

\[
                         0<x<2x<1-\rho<1/5.
\]

Integrating the two slope bounds therefore yields

\[
 \begin{aligned}
 -\kappa(x)-2\kappa(2x)
 &>{2x\over5}+{8x\over5}=2x,\\
 \kappa(\rho+2x)-\kappa(\rho)&<2x.
 \end{aligned}
\]

Thus the compact bracket

\[
 -\kappa(x)-2\kappa(2x)+\kappa(\rho)-\kappa(\rho+2x)
\]

is strictly positive.

## 4. Coefficient-by-coefficient residual replay

Subtract `G` from `mathcal R`.  The coefficients of the three train
families are:

\[
\begin{array}{c|ccc}
 &q=0&q=1&q\ge2\\ \hline
 \kappa(q\rho)&0&1&q\\
 \kappa(q\rho+x)&-1&0&q-1\\
 \kappa(q\rho+2x)&-2&-1&q-2.
\end{array}
\]

For the final row the `q=2` coefficient is zero, so its positive tail
starts at `q=3`.  Therefore, on `G=0`,

\[
\begin{aligned}
 \mathcal R
={}&-\kappa(x)-2\kappa(2x)
       +\kappa(\rho)-\kappa(\rho+2x)\\
 &+\sum_{q\ge2}q\kappa(q\rho)
 +\sum_{q\ge2}(q-1)\kappa(q\rho+x)\\
 &+\sum_{q\ge3}(q-2)\kappa(q\rho+2x).
\end{aligned}
\]

Every argument in the three sums is greater than one.  Hence every
summand is nonnegative because `kappa(u)=h(1+u)>0` there, and the first sum
is nonempty and strictly positive.  Together with Section 3, this proves

\[
                         \mathcal R(\rho,x)>0.
\]

No curvature or Hessian assumption entered the proof.  Thus the first and
fourth KKT rows alone are inconsistent; the curvature and one-sided sign
rows are genuinely redundant for exclusion.

## 5. Global sign and boundary audit

The corrected outer-period theorem signs the period ranges through
`rho=4/5` and from `rho=11/12` onward.  The frozen long-wrap reduction signs
the remaining boundary faces `x=0` and

\[
                         x=\min\{\rho/3,(1-\rho)/2\}.
\]

If a nonpositive long-wrap value existed, continuity would give a
nonpositive minimum on the compact closure of the full admissible domain.
Every boundary is strictly positive, so the minimum would be interior in
both `rho` and `x`.  Its two free derivatives would give `G=0` and
`mathcal R=0`, contradicting Section 4.  Equality zero is excluded by the
same argument, so the conclusion is strict positivity.

The stationary-strip theorem proves that positivity of this long-wrap face
implies positivity of the complete Chamber-II polygon.  Hence the scope
claim is exact.

## 6. Dependency and scope audit

| role | file | SHA-256 |
|---|---|---|
| corrected outer-period theorem | `MATH_THEOREM_LONG_WRAP_OUTER_PERIOD_CLOSURE_AND_COMPACT_THETA_CORE_20260804.md` | `c60b69aadd89815605be134162ade2c2355008ae9f34ee39d45bb3c5cef139b3` |
| independent outer-period audit | `MATH_AUDIT_LONG_WRAP_OUTER_PERIOD_CLOSURE_AND_COMPACT_THETA_CORE_INDEPENDENT_20260804.md` | `4f230c0615122794d71e65523d4b55a8bbe9f2b6c63de66b9b6bed48c41bc4da` |
| Chamber-II stationary-strip/KKT reduction | `MATH_THEOREM_SIX_SLOT_CHAMBER_II_STATIONARY_STRIP_ELIMINATION_AND_LONG_WRAP_CURVE_20260804.md` | `f5dbde2a817c6ab23ade7de5c0f0d691d80db4d4bb23865f9643959efa79c91b` |
| independent KKT audit | `MATH_AUDIT_SIX_SLOT_CHAMBER_II_STATIONARY_STRIP_AND_LONG_WRAP_CURVE_INDEPENDENT_20260804.md` | `3900b98672355272cf866659b4a5046f60b581604e18c91282e78e29d5f53d65` |

The theorem does not address Chamber I, other six-slot efficiency branches,
all-grid Bellman positivity, or the OR-word construction programme.
