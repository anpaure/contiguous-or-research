# Audit: exponential-clock regenerative macro cylinder

**Date:** 2026-08-06  
**Audited theorem:**
`MATH_THEOREM_EXPONENTIAL_CLOCK_REGENERATIVE_MACRO_ROUNDING_CE_20260806.md`  
**Method:** direct stopping-time, resource-consumption, and asymptotic replay;
no computation or search

## 1. Adaptive stopping is priced

Macros missing all prescribed root carriers may be accepted before the first
relevant macro and may cause the rate vector to be recomputed.  Lemma 3.2
conditions on the complete state immediately before the first relevant hit.
Within that state, exponential-clock competition chooses the hit category in
proportion to its current rate.  The possible pre-hit states form a mixture,
so a uniform pointwise ratio survives arbitrary recomputation.  No sum over
rounds or deterministic sum of live-root envelopes is used.

## 2. Unequal carrier loads cancel exactly

For root loads `L_i`, relative pair codegree gives

\[
 \Lambda\ge
 \left(1-(q-1)\delta/2\right)\sum_iL_i.
\]

The service rate of block `i` is at most
`theta kappa^(|A_i|-1)L_i`.  After multiplying by the common induction
bound for the other blocks and summing over `i`, the numerator is exactly
proportional to `sum_i L_i`.  Hence no lower or upper degree comparison is
needed.  The only residual requirements are relative carrier-pair and
marked-cluster ratios.

## 3. Resource-consumption cases

The theorem concerns an **exact** prescribed macro partition.

* If the first relevant macro consumes two block roots, it either merges two
  prescribed blocks or prevents one later root occurrence.  The exact event
  is impossible, so discarding that macro is a valid upper bound.
* If an earlier macro misses every chosen block root but consumes a companion
  carrier inside one block, that block can never be realized.  Again this
  only destroys the event.
* If two prescribed occurrences use one carrier owner, compatibility already
  fails and the probability is zero.
* Accepted macros are resource-disjoint by construction, so after a valid
  first service the remaining block roots are still live and distinct.

Thus choosing one root carrier per prescribed block loses no positive case.

## 4. Error scale

The multiplicative correction is

\[
 C_q=\prod_{j=1}^q(1-(j-1)\delta/2)^{-1}.
\]

For `q=O(d)` and `delta=O(d^-3)`,

\[
                         \log C_q=O(d^{-1}).
\]

The stronger fixed-factor bottom theorem also permits
`theta<=C_1 eta_*` for any absolute `C_1`.  In the absolute-load
formulation, any fixed `epsilon_0<1` merely changes this constant by
`1/(1-epsilon_0)`.

For fixed tested order `q<=K d`, even the pair ratio may deteriorate to
`delta<=gamma/d` with `K gamma<2`.  Then

\[
 C_q\le(1-K\gamma/2)^{-q},
\]

which is another fixed factor per root and is therefore permitted by the
bottom Haxell theorem.  The pristine `O(d^-3)` pair row is needed only for
the `1+o(1)` constant, not for existence.

## 5. Scope boundary

The theorem does not prove the needed integral macro factor.  Its remaining
premise is that along one state-dependent selection policy, until the
separator leave, every live required task has positive macro rate and every
reachable residual admits rates satisfying

\[
 {d_x(v,w)\over\min(d_x(v),d_x(w))}\le {\gamma\over d},
 \qquad
 {d_x(A)\over d_x(v(A))}
       \le C\eta_*\kappa^{|A|-1}.
\]

where `gamma` is a sufficiently small fixed constant for the desired order
window.  The complete orbit has much stronger pair ratios.  Arbitrary
residual deletion need not preserve the marked-cluster row:
it may trap one carrier in a small companion suborbit.  This hereditary
local-ratio statement, together with continuation to separator scale, is the
exact unresolved selector row.

## 6. Verdict

**PASS with the hereditary local-ratio premise binding.**  The theorem is a
valid dependent-rounding/cylinder result and removes both the independent
proposal Poisson barrier and the repeated-envelope `log d` loss.  It must not
be cited as an unconditional near-perfect macro matching theorem.
