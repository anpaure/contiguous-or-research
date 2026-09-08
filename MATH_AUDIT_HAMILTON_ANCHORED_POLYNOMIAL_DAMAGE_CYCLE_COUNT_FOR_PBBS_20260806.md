# Self-audit: Hamilton-anchored polynomial-damage PBBS completion

**Date:** 2026-08-06  
**Verdict:** proof-safe graph theorem, subject to the explicitly stated
all-occurrence (or prefix-safe) exposure hypothesis.  No computation, finite
search, or solver output is used.

Audited theorem:
`MATH_THEOREM_HAMILTON_ANCHORED_POLYNOMIAL_DAMAGE_CYCLE_COUNT_FOR_PBBS_20260806.md`.

## 1. Inputs actually used

The proof uses four mathematical inputs and does not infer any one from the
others.

1. The middle-level incidence graph has a Hamilton cycle, whose alternating
   edge classes are the base matchings `H_0,H_1`.
2. The Johnson spectral-surplus inequality localizes any family with shadow
   surplus at most polynomial to a polynomial small side.
3. The balanced sharp partial-shadow theorem forces a balanced adjacent-rank
   pair of minimum one-sided degree greater than `r/2` to have exponential
   size.
4. The polynomial partial-matching extension theorem applies after adding
   one residual edge because both exposures increase by at most one.

The separable-tag and typed-gammoid results occur only in the consequence and
scope sections.  They are not used to prove the matching or component bound.

## 2. Why the hatted exposure is necessary

For a completed partial matching the old `alpha` parameter maximizes only
over lower vertices not already used by that matching.  In a sequential
insertion, however, the lower endpoint of a later protected edge is still
unmatched at an earlier prefix.  The final residual-domain `alpha` therefore
does not bound every prefix.

The theorem uses

\[
 \widehat\alpha(F)=\max_{x\in\mathcal L}|N(x)\cap Y|,
 \qquad
 \widehat\beta(F)=\max_{U\in\mathcal U}|N(U)\cap Z|.
\]

Both are monotone under taking prefixes.  An explicitly verified
prefix-safe ordering is equally sufficient.  The advertised PBBS exposure
must be checked on one of these two domains before the theorem is cited.

## 3. Residual connectedness audit

For a component `(A,C)` of the residual graph, a residual perfect matching
gives `|A|=|C|`.  Choosing a smallest component gives `|A|<W/2`.  All old
neighbours of `A` lie in `C union Y_j`, so its old shadow surplus is at most
`j`.  The spectral inequality then gives `|A|<2rj`.

Every member of `A` nevertheless retains at least
`D_*=r-\widehat\alpha(F)>(1/2+epsilon)r` neighbours in `C`.  Complementing
turns these neighbours into facets, with the two complemented families still
equal in size.  The balanced partial-shadow threshold gives

\[
 |A|\ge{2D_*-1\choose D_*}
      =2^{(1+2\epsilon)r-O(\log r)},
\]

contradicting `|A|<2r^(C+1)`.  No assertion about expansion *inside* an
arbitrary component is hidden here; the argument rules out more than one
component.

## 4. Allowed-edge and strong-connectivity audit

For a residual edge `e`, the protected matching `F_j+e` has polynomial size
and exposures at most the hatted caps plus one.  The matching-extension
theorem therefore produces a residual perfect matching containing `e`.
Thus every residual edge is allowed.

Relative to any residual perfect matching `N`, every allowed edge lies on an
`N`-alternating cycle.  Hence every arc of the contracted exchange digraph
lies on a directed cycle.  Since the underlying contraction is connected,
its strong-component condensation cannot contain an edge and has only one
vertex.  This proves strong connectivity; bare Hall existence would not.

## 5. Diameter audit

For a lower set `S` in the contracted digraph,

\[
 |\Gamma^+(S)|=|N_G(S)-Y_j|.
\]

Up to size `W/2`, spectral surplus gives

\[
 |\Gamma^+(S)|-|S|\ge |S|/(2r)-j.
\]

Strong connectivity supplies integral growth by at least one below size
`4rj`; above that threshold the growth factor is at least `1+1/(4r)`.
The complement isomorphism supplies the same estimate for backward balls,
charging the `j` deleted lower vertices.  Forward and backward balls larger
than `W/2` intersect.  This proves directed diameter

\[
 8rj+16r\log W+4\le8rj+32r^2+4.
\]

The use of `W/2`, rather than half the residual shore, is safe because the
residual shore has `W-j` vertices and `j` is polynomial while `W` is
exponential.

## 6. Repair and component-count audit

At insertion step `j`, the new protected edge is one exchange arc.  A short
return path closes it to a directed cycle.  Switching that alternating cycle
preserves all earlier protected endpoints and inserts the next literal
incidence.  Summing twice the directed-cycle lengths gives

\[
 |M\triangle H|\le8rf^2+64r^2f+10f.
\]

Apply this separately to the two alternating halves of one Hamilton cycle.
Any component of the resulting coloured two-matching cover which uses no
new coloured edge would be a cycle subgraph of the base Hamilton cycle; the
only such cycle is the entire Hamilton cycle.  Otherwise every component
contains a distinct new coloured edge.  The component count is therefore at
most one plus half the total matching symmetric difference.

A physical edge common to the two completed matchings is new relative to at
least one of the two edge-disjoint Hamilton halves.  Thus the common-edge
debt is polynomial as claimed.  The theorem does not assert that this debt is
zero.

## 7. Random-matching warning audit

The middle-level incidence graph is edge-transitive.  Under the uniform
perfect-matching law every edge has marginal `1/r`.  A fixed matching has
`W` edges, so the expected number of common edges is `W/r`.  Each common edge
is an isolated coloured two-cycle.  Hence unweighted random extension has
exponentially large expected component count and cannot itself justify the
desired conclusion.

This is only a warning about that measure.  It is not a no-go theorem for all
weighted matching laws.

## 8. Exact PBBS scope

The theorem retains the protected stretched role-zero, immediate-palette,
and arbitrary-upper backup incidences if they are included in the two
protected matchings and the prefix-safe cap holds.  It proves a polynomial
component census and a polynomial set meeting all components.

It does not prove:

1. a simultaneous root-to-coded-port arm packing;
2. a simple factor after eliminating common completed edges;
3. biresidence or one literal common-history antecedent; or
4. the typed suffix rank or common two-coordinate Rado inequalities.

The polynomial separable-code theorem now has enough signatures for all
components, but only after the first item supplies actual coded ports.  The
typed deficiency remains

\[
 |P_{\rm conn}|-r_{\Gamma_{\rm suf}^{\rm type}}(P_{\rm conn}),
\]

with the common Rado/Edmonds all-subset condition required in the
two-coordinate model.
