# Audit: acceptance-aware isolated macro nibble and `(CE)`

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_ACCEPTANCE_AWARE_ISOLATED_MACRO_NIBBLE_PRESERVES_COMPANION_CE_20260805.md`  
**Method:** symbolic conflict-mass and cylinder audit; no computation

## 1. Survival exponent

One macro has `R=Theta(d)` resources.  The proposal scale is `Theta(1/d)`
times a fractional matching of vertex load one.  Thus its first-order
conflict mass is `Theta(1)`.  Correcting the sum over its resources to a
union costs at most

\[
 {R\choose2}O(d^{-1})O(d^{-3})=O(d^{-2}).
\]

The type-dependent exponent is therefore uniform within each complete
`h`-orbit up to `O(d^-2)`.

## 2. Shared competitors

For two disjoint desired macros there are `O(d^2)` ordered resource pairs.
The proposal mass of macros through one pair is

\[
                         O(d^{-1})O(d^{-3})=O(d^{-4}),
\]

so their shared-competitor mass is `O(d^-2)`.  For `g<=Cd` desired macros,
the total inclusion--exclusion correction is `O(g^2/d^2)`, which is at
most `O(g/d)` and hence costs `1+O(1/d)` per root macro.

## 3. Exact acceptance formula

Pairwise disjoint desired macros are all accepted exactly when they are all
proposed and every other proposal meeting their union is absent.  Therefore

\[
 \Pr(F_1,\ldots,F_g\text{ accepted})
 =\prod_iq_{F_i}\prod_{E:E\cap(\cup_iF_i)\ne\varnothing}(1-q_E).
\]

Using `1-q<=e^-q` and the two-term union lower bound gives precisely the
product `prod_i q_i e^{-L(F_i)}` times the shared-competitor correction.
No unpriced positive correlation remains.

## 4. Partition summation

After the fixed-macro bound, summing over one serving macro for each block
of a prescribed partition factorizes upon dropping disjointness.  The
local cluster ledger contributes `kappa^(|A|-1)` for block `A`, and summing
over round assignments replaces `zeta_i` by `sum_i zeta_i`.  Thus the
full order-`O(d)` cylinder follows from only local cluster sizes two and
three.

## 5. Binding hypotheses

The theorem is conditional in two material ways.

1. A residual fractional factor must have normalized resource-pair
   codegree `O(d^-3)`.
2. It must retain the much sharper marked same-macro codegrees
   `xi kappa^(b-1)` for `b=2,3`.

The first does not imply the second: `O(d^-3)` is polynomial, whereas
`kappa=exp[-Theta(d log d)]`.  Both are proved for the complete orbit, but
neither is currently regenerated jointly on every lower/owner residual.

The scalar accepted-envelope condition
`sum_i zeta_i<=(1+o(1))eta_*` is not enough to iterate the theorem.  Shared
early competitors can positively correlate the survival and first-hit
times of distinct roots.  The multi-round conclusion therefore correctly
requires the stopped multi-root estimate (5.2); that estimate is presently
open.

## 6. Verdict

**PASS for the one-round theorem.**  It genuinely prices the isolation
survival factor and the within-round shared-competitor correction.  The
multi-round section is a proof-safe reduction to the explicitly unproved
stopped multi-root estimate, not a theorem derived from one-point hazard.
Thus the file does not prove the regenerative fresh-macro nibble or the
near-perfect integral selector.
