# Self-audit: core-pinned uniform spread and residual host cuts

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_CORE_PINNED_UNIFORM_SPREAD_AND_EXACT_RESIDUAL_HOST_CUTS_20260804.md`  
**Method:** line-by-line probability, Hall, graphic-rank, and scope replay;
pure mathematics; no computation, search, or solver  
**Verdict:** SELF-GO at the stated asymptotic co-selection and protected-factor
scope.  Independent audit is still desirable, especially for the pinned
lower-star tail estimate.  The fixed-pull-orbit host remains open.

## 1. Pinned owner-star marginal

Fix an owner containing the pinned coordinate `q` and having external trace
size `e`.  For an external deletion `a`, the relevant trace has size
`e-1`.  Its pinned path has `e-2` immediate lower colours, and the
`K-{q}` part of the required facet has size `m-e-1`.  The ambient core has
size `m-2`, so the exact marginal is

\[
 {e-2\over {m-2\choose m-e-1}}
 ={e-2\over {m-2\choose e-1}}.
\]

Distinct external deletions use distinct independently ordered traces.
Owners of this external size number

\[
 {m\choose e}{m-2\choose e-1}.
\]

Multiplying the triple-event bound gives exactly the sum in (1.4).  The
ratio

\[
 {{m\choose e}\over {m-2\choose e-1}}
 ={m(m-1)\over e(m-e)}
\]

is correct.  Fixed `e>=4`, the middle range, and the upper
`m-e>=d+1` range all tend to zero after summation.  Thus the all-owner
random cross-trace cap two is valid.

Deleting `q` cannot hit the protected lower palette, all of whose members
contain `q`.  The same-trace deletion family contributes at most two, and
the deterministic external family at most three.  The pre-high value seven
and final value nine are therefore unchanged by pinning.

## 2. Pinned lower-star and endpoint marginals

If a lower vertex avoids `q`, at most the unique owner `x+q` from the
pinned half can lie above it.  This gives the stated unit bound.

If `q in x` and `|x cap E|=s`, a random trace meeting its star has the form
`S+z`.  The path has `s+1` owner positions and two endpoint positions, and
the required `K-{q}` part is one fixed member of a layer of size
`{m-2 choose s}`.  Hence

\[
 \mu_\ell(s)\le{(m-s)(s+1)\over {m-2\choose s}},
 \qquad
 \mu_e(s)\le{2(m-s)\over {m-2\choose s}}.
\]

There are `{m choose s}{m-2 choose s}` such lower vertices.  At the first
random level `s=2`, the sixth-moment union-bound term is `O(m^-2)`;
every fixed later level is smaller.  Central levels have exponential
denominators, and the last allowed level has denominator
`{m-2 choose d+1}=m^omega(1)`.  Therefore the complete sum is `o(1)`.

The owner-star and lower-star bad-event sums are both `o(1)`, so their union
is still below one.  This justifies one common low-path selection, rather
than two incompatible selections.

The random contribution is at most five, the own trace costs one, and the
deterministic cyclic bank costs at most four; this reproduces the spread-ten
bounds.  In the high-tail greedy step, one path raises each lower-star load
by at most one and each owner-star load by at most two.  The three critical
banks contain only `2^(m+o(m))` resources, versus
`2^(2m-o(m))` conditioned high-path supply.  They can be imposed
simultaneously.

## 3. Co-small and small cuts use the same pinned bank

The owner-star cap gives `g_U>=m-9`.  The optional-core ledger and the
sharp partial-shadow theorem then force a positive co-small core to have
size `2^(2m-o(m))`, contradicting the universal near-shadow cutoff
`O(m^2 2^m)`.  No unpinned reservoir is substituted in this step.

For the small side, the frozen co-selected small-cut theorem depends only
on:

1. singleton loss at most ten;
2. private endpoint exposure at most ten;
3. at most `2m` deterministic top endpoints; and
4. forced-facet load at most nine.

All four were established for the same pinned bank.  Its partial-shadow
and Kruskal--Katona proof is therefore reusable without changing any
occurrence geometry.  The conclusion is exactly a spanning two-factor
containing the pinned reservoir.

## 4. Exact residual Hall identity

An inclusion-minimal deficient shore contains no protected lower vertex,
because those vertices have degree two while the irreducibility theorem
allows degree at most one.  On such a shore every lower demand is two and
no protected edge enters from it.  Thus

\[
 \kappa_P(A)=\sum_U\min(2-d_P(U),a_U).
\]

Relative to the unprotected capacity, an internal owner loses
`min(2,a_U)` and an endpoint owner loses one exactly for `a_U>=2`.
This verifies `(SC)` and (2.3).  The theorem records this inequality as the
cut that was closed, not as a remaining hypothesis.

## 5. Pull-host cut and scope

Within a fixed tree-compatible pull host, accessibility and phase
consistency determine the forced label bank `J`.  A spanning tree can
contain `J` exactly when `J` is graphic-independent, equivalently

\[
 |J\cap E_H(X)|\le |X|-1
\]

for every nontrivial vertex set, with loops excluded and parallel labels
retained.  The opposite-coordinate-half tree then supplies all remaining
graphic rank without touching the pinned bank.  This proves `(PH)` at its
stated conditional scope.

The arbitrary two-factor supplied by protected Hall is not thereby placed
in this fixed pull orbit.  Also, opposite-half pulls preserve the pinned
`q`-run decomposition rather than repair it, and physical separation does
not preserve remote interval witnesses automatically.  The theorem
correctly leaves accessibility/phase consistency, endpoint residence, and
upper-host invariance open.
