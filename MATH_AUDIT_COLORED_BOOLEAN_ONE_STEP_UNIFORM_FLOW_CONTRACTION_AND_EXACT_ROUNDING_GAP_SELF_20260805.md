# Self-audit: colored Boolean one-step flow and rounding gap

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_COLORED_BOOLEAN_ONE_STEP_UNIFORM_FLOW_CONTRACTION_AND_EXACT_ROUNDING_GAP_20260805.md`  
**Method:** exact symbolic replay and literature-scope check; no computation,
search, or solver  
**Verdict:** **GO.**  The flow and contraction theorems are unconditional.
The full spread-extension corollary is explicitly conditional on an exact
matching-concentration oracle which standard dependent rounding does not
provide.  A subsequent exact-marginal maximum-entropy argument is valid,
but the augmented graph's conditional dummy square proves that edge-
coordinate Strong Rayleigh theory cannot supply the concentration oracle.

## 1. Square-interface and fractional-load check

The augmented left shore has

\[
 C_q+(C_{q+1}-C_q)=C_{q+1}
\]

vertices, equal to the right shore.  Every old rank-`q` vertex has `n-q`
upper neighbours, and every start dummy has `C_(q+1)` neighbours.  Under
the proposed weights, a right vertex receives

\[
 {q+1\over n-q}+{C_{q+1}-C_q\over C_{q+1}}
 ={C_q\over C_{q+1}}+1-{C_q\over C_{q+1}}=1.
\]

Thus the point is exactly fractional perfect, not merely subperfect.

## 2. Future-owner expectation and contraction

For fixed `S subset U`, exactly `v-q` of the `n-q` one-element extensions
of `S` remain inside `U`.  This proves the factor `(v-q)/(n-q)`.  Also

\[
 {v-q\over n-q}
 {\binom vq\over C_q}
 ={\binom v{q+1}\over C_{q+1}},
\]

so the uniform benchmark transports exactly.  Since `v<=r` and `n=2r`,

\[
 {v-q\over n-q}\le{r-q\over2r-q}\le{1\over2}.
\]

All inherited deviations therefore form a geometric, rather than linear,
error sum over the `O(D)` interfaces.

Whole job configurations may be used as persistent colours: the colour
records every later cut and socket role, while the underlying Boolean path
continues across fragment boundaries.  Final chunk-top tests are linear
aggregates of those persistent colours.  This avoids assuming arbitrary
recolouring of a frozen named path.

## 3. Conditional concentration calculation

If each integral perfect matching preserved the fractional marginals and
had Chernoff--Bernstein tails for every nonnegative edge statistic, the
one-step exponent for a normalized top-codegree test would be

\[
 \Omega\left({\Delta_u^2d_{\min}(u)\over C_uH_u}\right).
\]

The spread theorem chooses this to be a sufficiently large multiple of
`r`, enough for all `exp(O(r))` tests across all interfaces.  The factor-
two geometric sum is absorbed by enlarging its absolute reserve constant.
Concatenated integral perfect matchings are target-disjoint Boolean paths;
cutting by the persistent configuration colours yields the abstract
interval pieces.  The conditional implication is therefore correct.

## 4. Rounding-theorem scope check

Ordinary bipartite integrality has no concentration conclusion.  The
classical exact dependent rounding for bipartite graphs supplies negative
correlation only for the restricted edge groups in its theorem, not for
arbitrary future-owner sums spread across the graph.

The Chekuri--Vondrak--Zenklusen matching/matroid-intersection theorem does
give dimension-free concentration for arbitrary linear statistics, but its
expectation is `(1-gamma)x`.  At the smallest relevant mean
`Theta(rD)=Theta(r^(3/2))`, an `exp(O(r))` union needs
`gamma=Omega(1/D)=Omega(r^(-1/2))`.  This leaves
`Theta(W/sqrt(r))` old vertices unmatched at one complete interface.  The
vanishing spread reserve is only `O(W/r^(3/4))`; it cannot absorb that loss
directly.  Repeating without regeneration can create `Theta(W)` breaks.

The source does not turn this mismatch into a nonexistence claim.  It
correctly isolates a Boolean-specific exact-concentration theorem or a
scaled-loss regeneration theorem as the remaining one-step bridge.

### 4.1 Maximum entropy and the Strong Rayleigh boundary

The strictly positive fractional point is in the relative interior of the
bipartite perfect-matching polytope.  Finite exponential-family duality
therefore gives positive edge weights whose perfect-matching Gibbs law has
exactly those marginals.

This law is not Strong Rayleigh.  Condition on all but two dummy edges of
any incumbent perfect matching.  The remaining face is `K_(2,2)`, and two
opposite edges have covariance `p(1-p)>0`.  Conditional negative
association would forbid this.  The separate theorem and audit prove this
without assuming that arbitrary preselected right endpoints are
reservable:

* `MATH_THEOREM_PERFECT_MATCHING_MAXENT_EXACT_MARGINAL_AND_STRONG_RAYLEIGH_NOGO_20260805.md`;
* `MATH_AUDIT_PERFECT_MATCHING_MAXENT_EXACT_MARGINAL_AND_STRONG_RAYLEIGH_NOGO_SELF_20260805.md`.

The conclusion is scoped correctly.  It excludes a generic Strong
Rayleigh proof, not Boolean-specific concentration of the aggregate tests.

## 5. Verdict

The unconditional mathematical gain is:

\[
 \boxed{
 \text{uniform colored flow is exact, and every inherited future-owner
 spread error contracts by at least }1/2.}
\]

The desired integral colored extension remains conditional on one clearly
stated rounding property.  Audit verdict: GO.
