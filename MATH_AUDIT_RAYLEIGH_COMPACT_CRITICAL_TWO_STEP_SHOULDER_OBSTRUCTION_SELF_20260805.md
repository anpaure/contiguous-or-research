# Self-audit: compact-critical two-step shoulder obstruction

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_COMPACT_CRITICAL_TWO_STEP_SHOULDER_OBSTRUCTION_20260805.md`  
**Method:** independent symbolic replay; pure mathematics, no computation,
enumeration, search, or solver  
**Verdict:** **PASS SELF-AUDIT.**  The family is an exact saturated
first-minimum Bellman table, and the positive derivative prefix occurs in
its actual shoulder rather than in a free abstract deficit chain.  The
theorem correctly makes no assertion about the sign of the total shoulder.

## 1. Table audit

For `N=2H`, `L=zeta(1-2/H)`, and `lambda=L/H`, the table has four regions:
zero below `H`, value `L` at `H`, the constant value `lambda(H+1)` from
`H+1` through `2H-1`, and value `2L` at the endpoint.

If a legal sum has both inputs at least `H`, it must be `H+H=2H`.
Otherwise at most one input is nonzero, and monotonicity of the table proves
superadditivity.  The plateau lies below `zeta` because

\[
 (1-2/H)(1+1/H)=1-1/H-2/H^2<1.
\]

The endpoint is at least `zeta` for `H>=4` and is the exact value of the
proper partition `H+H`; maximum density shows no proper partition can do
better.  Thus first crossing and saturation are exact.

The ratios at `H,H+1,2H` equal `lambda`; all other positive plateau ratios
are smaller.  Consecutive critical indices give gcd one, so the formal
clock is exactly arithmetic.

## 2. Actual shoulder audit

Take residue `r=H-1` relative to the critical denomination `H`.  The
displayed value at `r` is zero, so

\[
 \Delta_r=\lambda(H-1).
\]

The next chain index is `2H-1`, whose physical displayed value is
`lambda(H+1)`.  Hence

\[
 \Delta_{2H-1}=\lambda(H-2)>0.
\]

For every layer below this second deficit, the actual active prefix has at
least two terms.  This conclusion uses only displayed-table equality
`V_m=c_m` for `m<=N`, so it has no conductor or recurrence gap.

At layer height zero the two-term derivative sum tends, as `H` tends to
infinity, to

\[
 K'(\zeta)+K'(2\zeta)=K'(2\zeta)>0.
\]

Continuity makes it positive for all sufficiently large finite `H` and on
a nonempty interval of positive layer heights.  Every later possible term
has argument beyond `zeta` and is positive.  Therefore the complete actual
prefix is positive there.

## 3. Scope

In the shoulder layer-cake, a positive derivative prefix contributes
negative local shoulder mass after the leading minus sign.  This disproves
a universal termwise-prefix or termwise-chain sign strategy in the compact
critical band.

The audit does not sum the other layers or compare the total negative
shoulder with the strict formal reserve.  It therefore supports no
counterclock, no failure of Rayleigh all-price positivity, and no OR-word
conclusion.  Its exact consequence is only that the remaining proof must
use cross-layer/residue compensation or the formal reserve.

