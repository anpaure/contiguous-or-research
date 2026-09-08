# Self-audit: Boolean assignment rounding shortcut boundaries

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_BOOLEAN_ASSIGNMENT_ROUNDING_AFK_DISCREPANCY_C6_AND_SCALED_LOSS_BOUNDARIES_20260805.md`  
**Verdict:** GO, subject to the theorem-scope qualifications below.

## 1. AFK source replay

Theorem 1.3 in the primary AFK paper explicitly says:

* the output is a matching with at least `N-o(N)` edges;
* the general signed error is
  `(1-o(1))b_k - O~(sqrt(N A_k))`;
* for nonnegative coefficients equation (7) improves the additive term to
  `O~(A_k)`.

Section 5 equation (27) uses
`delta=O(log log N/log N)`.  Equations (30)--(31) display the accumulated
additive term `O~(k A Delta)`, with `k=Theta(log N)` and
`Delta=O(log^3 N)`.  Therefore the theorem supplies neither exact
perfectness nor a mean-sensitive Bernstein error.  The audited note does
not claim an impossibility theorem for a refined AFK analysis.

## 2. Sub-isotropic rank calculation

For a connected bipartite graph, the unoriented `0,1` vertex-edge
incidence matrix has rank `|V|-1`.  On an even cycle, `|V|=|E|=f`, hence
rank `f-1`.  The perfect-matching face is one-dimensional, agreeing with
the rank calculation.

Bansal's Theorem 1.2 assumes rank at most `(1-delta)f` at every iterated
step and gives `beta=20/delta`.  Substitution yields
`delta<=1/f`, `beta>=20f` on a long-cycle face.  This limits the generic
application but does not show that a specially designed Boolean
trajectory must encounter a long cycle.  The main note states this
qualification explicitly.

The Bansal--Nagarajan matroid extension preserves one matroid polytope.
Perfect matchings are not bases of one matroid unless the supported family
is a singleton: deleting one edge from a perfect matching exposes its two
endpoints, and only that same edge can restore perfectness by a one-element
exchange.  Thus the one-matroid theorem cannot simply be relabelled as an
exact perfect-matching theorem.

## 3. `C6` count replay

For `C subset U` and exactly two active labels `a,b in U`, the only upper
hexagon vertex in the owner is `C+ab`; its provider toggles between `C+a`
and `C+b`.  Those providers form one Johnson edge.  The third active label
has exactly `n-v` choices outside `U`.  All other intersection patterns
give zero change.  This verifies (3.2).

With `A=binom(U,q)`, every Johnson edge has equal endpoint colours, so the
switch sensitivity is zero.  The mean in (3.3) is positive for `v>q`.
This rules out only old-only `C6` switch mechanisms.  It does not rule out
mixed circuits or the actual uniform matching law.

## 4. Fragmentation-tail replay

For a split `L=a+b`, the old and new tail contributions at threshold `s`
are respectively

\[
 1_{L\ge s}
 \quad\hbox{and}\quad
 1_{a\ge s}+1_{b\ge s}.
\]

The four threshold regimes give equation (4.1) exactly.  Hence chunk count
alone cannot certify socket-capacity feasibility.

## 5. Scaling replay

At critical mean `mu=Theta(rD)` and with `exp(O(r))` tests, an exponent
`Theta(gamma mu)` needs `gamma=Omega(1/D)`.  A loss fraction `gamma` at
each of `D` interfaces creates `Theta(gamma W D)=Theta(W)` breaks absent
regeneration.

The raw two-SCD theorem proves `S-P>=eta W` only in socket number and
explicitly leaves typed capacity/containment Hall open.  The spread-top
theorem proves the first adjacent-depth margin
`H_t=Theta(WD/r)=Theta(W/sqrt r)` and handles deeper reserves at the
`W/r` comparison scale.  Equation (4.1) shows why arbitrary central breaks
cannot be charged merely to the raw count reserve.

The theorem does not claim that scaled loss is impossible.  Endpoint-
localized breaks, typed linear tail reserve, or contraction of live breaks
remain valid exits.

## 6. Final scope

The companion image-set theorem supplies exact occupancy concentration.
The only claimed remaining one-step oracle is coloured assignment within
that image set.  No all-dimensional upper bound, no `k=17` construction,
and no arbitrary-colour concentration theorem is claimed here.
