# Self-audit: period-twenty-six sharp-depth reduction

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_APERY_PERIOD26_SHARP_DEPTH_AND_TWO_RESIDUAL_THRESHOLD_CHAMBERS_20260804.md`  
**Target SHA256:**
`999d47fdcf57cb9a89edc738cf75178f61fd442cd1beb73ced5435c7c3c8bc58`  
**Verdict:** **SELF-AUDIT GO as a reduction theorem.**  This is not an
independent audit and does not claim complete period-twenty-six positivity.

## 1. Monotonicity and anchor arithmetic

At `x=2/13`, direct differentiation gives the first ratios

\[
{15\over11}e^{-2\pi/13},
\qquad
{28\over11}e^{-51\pi/52},
\]

and the first successor ratio

\[
{41\over28}e^{-69\pi/52}.
\]

The displayed rational prices imply

\[
{17\over20}+{3/25\over1-1/30}={113\over116}<1.
\]

The logarithmic derivatives are negative throughout `[2/13,1/2]`, so
the monotonicity interval is used in the correct direction.

At `2/13`, the four Gaussian lower numerators sum to

\[
56980+35140+2610+40=94770,
\]

and hence `f(2/13)<523/10000`.

At `5/26`, they sum to

\[
59905+32740+2290+33=94968,
\]

so `f(5/26)<5032/100000<63/1250`.

At `3/13`, they sum to

\[
62828+30428+2007+27=95290,
\]

giving `f(3/13)<471/10000`.  Every exponent substitution is below 25,
and an upper exponential bound gives the lower Gaussian bound in the
correct reciprocal direction.

## 2. Overlap-depth bound

The exact train identity is

\[
E(s)=C+g(\alpha)+T+\mathcal M,
\qquad
T=\sum_i(f(X_i)-f(Y_i)),
\qquad
\mathcal M\ge0.
\]

The frozen layer-cake theorem gives

\[
T\ge-H(\sup f-C).
\]

Since `sup f<G` and `C>L`, and since the theta ray has `u+1` terms,

\[
E(s)>(H+1)L-HG-(u+1)\varepsilon.
\]

Ray disjointness gives `u<=12`.  The right side is decreasing in `H` and
`u`, so for `H<=4` its worst value is

\[
5L-4G-13\varepsilon
={220120-213200-650\over1000000}
={6270\over1000000}>0.
\]

This closes the claimed generic depth range without using any new anchor.

## 3. Base and ordered inequalities

The first-five base is

\[
264144-159900-52300-50400-300=1244
\]

over denominator one million.  The shorter ledgers are positive as well.

If `X_6>=2/13`, monotonicity makes every compact difference from pair six
onward nonnegative.  Pair six alone may still pay one theta allowance;
after it, `Y_i>i/26>1/4` for `i>=7`, so the later theta terms are positive.
The remaining margin is therefore `1194/1000000`.

If `X_6<2/13`, the sixth price is

\[
L-V_6-\varepsilon
={44024-47100-50\over1000000}
=-{3126\over1000000}.
\]

Thus the first residual debt is `1244-3126=-1882`.

If also `X_7<2/13`, the strict rational comparison

\[
{7\over26}>{6\over23}
\]

gives the credit `44024-43790=234`, leaving debt `-1648`.

If also `X_8<2/13`, then

\[
{4\over13}>{2\over7},
\]

and pair eight contributes `3194`; the margin becomes `1546`.  If pair
nine remains below threshold, `9/26>1/3` gives `2009/375000`.  Charging
all three possible later pairs by the generic quarter cost is safe and
leaves

\[
3(1546)+16072-3(3408)=10486>0
\]

over denominator three million.

Therefore the ordered cases leave exactly the two chambers stated in the
theorem.

## 4. Exact slack identities

For chamber `R_6`, the baseline is

\[
7L-(3G+V_4+V_5+V_6)-7\varepsilon
=-{1882\over1000000}.
\]

Expanding `mathcal S_6` cancels every inserted price and allowance and
recovers `C+g(alpha)+sum_i P_i+mathcal M` exactly.  Its individual terms
are nonnegative because `X_i<2/13<1/4` for `i<=6`, the far prices are
valid, each theta term exceeds `-epsilon`, and all later pairs have crossed
the decreasing threshold.

For chamber `R_7`, the baseline is

\[
8L-(3G+V_4+V_5+V_6+4379/100000)-7\varepsilon
=-{1648\over1000000}.
\]

Here `g(Y_7)>0` because `Y_7>1/4`, so no eighth theta allowance is used.
The same direct expansion verifies the `mathcal S_7` identity and the
nonnegativity of every listed summand.

Thus the two remaining scalar requirements are exact for the endpoint
lower expression, rather than informal estimates.

## 5. Scope and dependencies

All six dependency hashes in the theorem match their current files.  The
result closes all `H<=4` clocks and all ordered-ray chambers outside
`R_6,R_7`; it neither proves the two residual credits nor claims complete
period-twenty-six positivity, a physical shoulder theorem, or an OR-word
construction.
