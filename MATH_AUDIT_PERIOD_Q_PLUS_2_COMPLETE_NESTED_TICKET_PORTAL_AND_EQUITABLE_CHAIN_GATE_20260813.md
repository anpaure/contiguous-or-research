# Independent audit: period-`q+2` complete nested-ticket portals

**Date:** 2026-08-13  
**Verdict:** **PASS.**  
**Frozen source:** `MATH_THEOREM_PERIOD_Q_PLUS_2_COMPLETE_NESTED_TICKET_PORTAL_AND_EQUITABLE_CHAIN_GATE_20260813.md`  
**Source SHA-256:** `30d622fc1a5a8a648a8b4e25377db42f74b3079ae2f61386c5f2f05181115715`

This was a proof-level audit; no search or solver was used.

## 1. Threshold and suffix identities

With `N=q+2`, the schedule `P_a={a,a-3}` has cyclic gaps `q-1` and `3`.
For `q>=4`, both gaps are at most `q-1`, so every cyclic `(q-1)`-interval
meets it.

For `a_t=-t+1`, use representatives in `[-(q+1),0]`.  The two emissions
are `-t+1` and `-t-2`.  The suffix `J_ell=[-ell+1,0]` meets the first
exactly when `ell>=t`; when `ell<t`, both emissions lie strictly left of
the suffix.  At `t=q-1`, the second emission is `-q-1`, still outside all
listed suffixes, so the endpoint case is correct.

Choosing `y_ell in V_ell-V_(ell-1)` makes the labels distinct and gives

\[
V_\ell\cap\{y_1,\ldots,y_{q-1}\}=\{y_1,\ldots,y_\ell\}.
\]

The threshold schedule for `f in F` emits into `J_ell` exactly when
`f in V_ell`.  The toggle and core contributions therefore unite to
`V_ell` literally.  Since every core schedule meets every `(q-1)`-interval,
the immediate-lower, owner, and immediate-upper rows remain exactly those
of the repeated-core two-hole packet.

The age recurrence is also exact.  The backward distance to the latest
emission resets to zero at an emission and otherwise increments by one;
meeting every `(q-1)`-interval is equivalent to the age cap `q-1`.
For `P_a`, the two cyclic gaps give the claimed rotation of
`(1,2,...,q-1,1,2,3)`.

## 2. Partial chains and missing hypotheses

A strict chain with at most `q-1` nonempty members ending at `Q` extends
inside `Q` to one with exactly `q-1` members whenever

\[
|Q|=R-1\ge q-1,
\]

that is, whenever `R>=q`.  Refining the available rank gaps supplies the
extra members.  This hypothesis is also required by the construction's
core size `|F|=R-q`.  It should be stated in the setup.

The construction chooses three distinct toggles outside `Q`, so it also
requires an ambient ground set `[k]` satisfying

\[
k-|Q|=k-R+1\ge3.
\]

The intended odd regime `k=2R-1` satisfies this (and `R>=q` eventually),
but the local theorem as written should declare both hypotheses.

## 3. Portal count

For each increment, the distinguished toggle has exactly
`|V_ell-V_(ell-1)|` choices.  These choices are independent and phase-
recoverable.  Once fixed, the three remaining labelled phases receive an
ordered triple of distinct exterior coordinates, giving exactly

\[
\prod_{\ell=1}^{q-1}|V_\ell-V_{\ell-1}|\,(k-R+1)_3
\]

portals for the fixed endpoint convention.  A saturated chain has unit
increment product and still has the polynomial exterior bank.  Reversal
and endpoint rotation are correctly left as optional further multiplicity.

## 4. Global scope

The note correctly does not infer a packet factor from the local portal.
At different endpoints, one core coordinate's thresholds must arise from
one cyclic age word; unrelated one-endpoint portals cannot be grouped
freely.  The listed rainbow owner/root/upper/lower selection remains a
genuine joint integral problem.

The source now states the needed converse qualifier explicitly.  A
depth-`q` chronology yields the desired partition only if its selected
proper-suffix marks cover every residual lower target exactly once.  It
correctly makes no assertion for an arbitrary unmarked chronology or a
compiler using nonsuffix intervals.  The reduction to the Ferrers-profiled
equitable half-chain gate is therefore exact.

No other indexing, counting, or scope defect was found.
