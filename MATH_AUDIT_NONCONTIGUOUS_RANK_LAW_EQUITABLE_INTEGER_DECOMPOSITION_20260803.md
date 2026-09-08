# Self-audit: noncontiguous rank-law equitable integer decomposition

**Date:** 2026-08-03  
**Audited file:**
`MATH_THEOREM_NONCONTIGUOUS_RANK_LAW_EQUITABLE_INTEGER_DECOMPOSITION_20260803.md`  
**Method:** independent line-by-line mathematical audit of the edge-colouring
argument and its Boolean specialization.  No solver or finite search is
used.

## 0. Verdict

**GO at exactly the stated rank-pattern scope.**

The equitable edge-colouring proof is valid for bipartite multigraphs,
including parallel edges.  Applied to the path-plus-isolated-edge rank
graph, it gives exact integer rank multiplicities, the residual spacing
constraint, and optimally balanced pattern sizes.  It does not assign named
targets or choose the literal boundary chains, and the theorem says so
explicitly.

## 1. Edge-colouring audit

The multiplicity vector `n` produces a bipartite multigraph of degree

\[
                         d_{G_n}(v)=n(\delta(v))\le W.
\]

Koenig's line-colouring theorem applies to bipartite multigraphs and gives
`Delta(G_n)` colours.  Empty colours legitimately raise the number to `W`.

For two colours, properness makes every vertex incident with at most one
edge of each colour.  Their union therefore has maximum degree two and its
components are alternating paths or even cycles (with isolated edges as
one-edge paths).  A component's colour-count difference is `-1,0`, or `1`.
If the global class-size difference is at least two, a `+1` component
exists.  Swapping on it preserves properness and changes the two sizes by
`-1,+1`.  The sum of squared class sizes changes by

\[
 (a-1)^2+(b+1)^2-a^2-b^2=-2(a-b-1)<0
\]

when `a>=b+2`.  Termination and equitability follow.  Parallel two-edge
components are alternating 2-cycles with difference zero and cause no
exception.

Every colour class is a matching.  Its size is `floor(N/W)` or
`ceil(N/W)`, where `N=n(E)`.  Since `N<=dW`, the ceiling is at most `d`.
This verifies the general theorem.

## 2. Rank-graph audit

For consecutive residual path edges `e_s,e_(s+1)`, the common path-vertex
degree after multiplicity blow-up is `n_s+n_(s+1)`.  At a path endpoint it
is `n_s`, and at either endpoint of an isolated collar edge it is also
`n_s`.  Therefore (0.5) is exactly the maximum-degree row required by the
general theorem.  A colour class cannot contain adjacent path edges, while
isolated collar edges impose no cross-rank restriction.  The multiplicity
identity gives each rank exactly `n_s` occurrences across the `W` patterns.

For `n_s=binom(2r,s)-b_s`, integrality is automatic.  The audited
noncontiguous-collar theorem supplies

\[
 q_s+q_{s+1}\le1,
 \qquad \sum_s q_s\le d,
\]

so multiplication by `W` supplies the degree and total rows.  No additional
asymptotic estimate is used here.

The equitable histogram is exact.  If `N=dW`, every class has size `d`.
Otherwise the numbers of classes of sizes `floor(N/W)` and
`ceil(N/W)` are forced by their sum, giving formula (2.1).

## 3. Named-target scope audit

The construction colours copies of rank labels, not Boolean targets.  It
does not prove any of the following:

* that the `b_s` boundary targets form the required literal Ferrers chains;
* that a scheduled rank-`s` position receives a contained rank-`s` target;
* that targets scheduled at several ranks of one owner are nested;
* that all named targets are distinct; or
* that the resulting flags satisfy a sliding interval chronology.

Proposition 3.1 is an exact equivalence once both the schedule and the
boundary families are fixed.  A matching edge records one pattern, one
owner, and one owner ordering.  Disjointness enforces distinct patterns,
owners, and targets; full coverage enforces exact realization.  Conversely
every realization gives those `W` disjoint configuration edges.  There is
no hidden inference that the configuration matching exists.

Proposition 3.2 is also exact.  For `k=2r`, coordinate complementation pairs
the rank-`r` owners containing `x` with those avoiding it, so the avoiding
half has cardinality `W/2`.  Labelling all `n_s<=W/2` active patterns by
owners in that half makes every rank-`s` target containing `x` incompatible.
Their number is `binom(2r-1,s-1)`, and deleting `b_s` named boundary targets
can remove at most `b_s` of them.  The result proves only existence of a bad
owner labelling; it does not deny existence of a good correlated labelling.

The theorem therefore closes only the integer rank-inventory projection.
Its final statement correctly leaves the Boolean flag/perfect-configuration
matching open.  This is consistent with the dense-Ferrers barrier and with
the known fixed-assignment `k=5` incomparability example.

## 4. Final proof-safe boundary

The verified implication is

\[
 \boxed{
 \text{fractionally feasible integral rank vector}
 \Longrightarrow
 \text{exact equitable integral rank-pattern schedule}.}
\]

The unproved implication is

\[
 \boxed{
 \text{rank-pattern schedule}
 \Longrightarrow
 \text{integral named owner flags}.}
\]

No `o(W)`, `O(1)`, chronology, upper-deck, or universal-word conclusion is
claimed.
