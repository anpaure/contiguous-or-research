# Independent audit V1: near-full owner-gammoid protected-wedge bypass

**Date:** 2026-08-04  
**Verdict:** **GO** at the explicit occurrence-faithful fixed-state scope.
No computation, search, or solver output is used.

Audited theorem:
`MATH_THEOREM_NEAR_FULL_OWNER_GAMMOID_PROTECTED_WEDGE_BYPASS_20260804.md`,
SHA-256
`4962e57f888848a40bc9b1f6cb8cb871d95bc2f1d777858a609ef9aebe93aadd`.

Author audit:
`MATH_AUDIT_NEAR_FULL_OWNER_GAMMOID_PROTECTED_WEDGE_BYPASS_20260804.md`,
SHA-256
`03933c744336fafd30358a8f5dd1abf8572149d41218f66ac46caaeef8ba0d68`.

The earlier draft's `p=m` endpoint gap is repaired by the frozen hypothesis
`1<=p<=m-1`.

## 1. Basis hitting and supported menus

Each required lower turn has exactly `m` owner neighbours.  If `B` is a
basis of `Gamma|P_0`, then

\[
 |P_0\setminus B|=K,
\]

so every owner star satisfies

\[
 |B\cap N_i|\ge m-K\ge p.
\]

No symmetry or base distribution is required.  The same proof works under
the weaker direct premise that one independent set hits each star at least
`p` times.

If `s_i=|B cap N_i|`, the unsupported wedges are exactly the pairs chosen
from the `m-s_i` owners outside `B`.  Thus

\[
 |W_i(B)|={m\choose2}-{m-s_i\choose2}=B_{s_i}(m).
\]

Because `s_i>=p` and `p<=m-1`,

\[
 B_p(m)-B_{p-1}(m)=m-p>0.
\]

Hence every supported menu strictly exceeds the sharp `B_(p-1)` deletion
threshold.  The exact menu-packing theorem applies and gives pairwise
distinct wedge owners and q1 terminal values.

## 2. Routing and factor completion

Every selected wedge has at least one owner in `B`.  Since all selected
owner values are distinct, choosing one basis owner from each wedge gives a
`p`-element subset of `B`.  Gammoid independence is hereditary, so these
ports have simultaneous vertex-disjoint typed suffixes to distinct sinks.

The fixed-state hypotheses give distinct source occurrences, distinct owner
ports, empty prefix interiors, and separation from the suffix network except
at the intended port.  Prepending the prefixes therefore preserves
disjointness and the compensation linkage.

The wedge q1 terminal is correctly retained only as part of the protected
factor structure; it is not silently identified with the typed gammoid sink.

The selected incidence bank has `2p` edges, lower degree two, and owner
degree one.  Under degree compatibility and

\[
 2p+|P_*|\le m-2,
\]

the small protected-factor theorem applies.  Completion-stability of the
physical port and suffix identity is an explicit and necessary premise.

## 3. Exact fixed-bank Rado row

For a fixed wedge bank, claim `i` has the two-port menu `A_i(D)`.  Rado's
theorem gives maximum service size

\[
 \min_{X\subseteq[p]}
 \left(p-|X|+r_\Gamma\!\left(\bigcup_{i\in X}A_i(D)\right)\right).
\]

Therefore the deficiency is exactly

\[
 \max_{X\subseteq[p]}
 \left(|X|-r_\Gamma\!\left(\bigcup_{i\in X}A_i(D)\right)\right).
\]

The all-subset rank inequalities are necessary and sufficient for this
fixed-bank architecture, and weakening each by `C` leaves at most `C`
claims.

## 4. Sharp scalar-corank boundary

At corank `K=m-p+1`, make `m-p+1` ports in one required star loops and all
other ports free.  This is a strict gammoid and every basis meets that star
in only `p-1` ports.  Its supported wedge menu has exactly
`B_(p-1)(m)` elements.  The attained prefix-conflict construction can cover
exactly those `p-1` coordinate stars, so the sequential cardinality-only
argument has no remaining candidate.  The theorem correctly claims
sharpness only for this scalar implication, not necessity of the corank row.

## 5. Frozen deletion transfer

Fix a raw full linkage `mathcal R` of all ports in `P_0`.  Its paths are
pairwise vertex-disjoint and use distinct terminal slots.  Consequently one
deleted capacity vertex or slot meets at most one displayed path.  If

\[
 h_F(\mathcal R)
 =|\{R\in\mathcal R:\operatorname{cap}(R)\cap F\ne\varnothing\}|,
\]

then deleting those paths leaves a residual linkage on at least
`|P_0|-h_F` ports.  Hence

\[
 K=|P_0|-r_\Gamma(P_0)
 \le h_F(\mathcal R)
 \le |F|.
\]

Thus `h_F<=m-p`, or more coarsely `|F|<=m-p`, implies the main theorem.
The count is correctly in physical unit capacities and sink slots; bounded
logical claim count alone would not suffice.

## 6. Adaptive contraction

For an independent background set `C` of size `b`,

\[
 r_{(M/C)|P_0}(P_0)
 =r_M(C\cup P_0)-r_M(C)
 =r_M(C\cup P_0)-b.
\]

Therefore

\[
 K=b+|P_0|-r_M(C\cup P_0),
\]

and the displayed joint-rank floor is exactly equivalent to
`K<=m-p`.  No individual survival premise is inserted into this identity.

## 7. Full-set cut sufficiency

The construction before wedge selection uses only the scalar full-set rank

\[
 r_\Gamma(P_0)\ge|P_0|-(m-p).
\]

In the node-split typed suffix network, max-flow/Menger identifies
`r_Gamma(P_0)` with the minimum capacity of a `P_0`-to-typed-sink cut.
Thus the rank floor is equivalent to requiring that same floor for every
full-set cut.  Rank inequalities for all subsets are unnecessary at this
stage because a basis with global complement size at most `m-p` already
hits every `m`-owner star at least `p` times.

The frozen and adaptive common-cap formulas are the same cut statement
after, respectively, deleting the fixed background capacities or contracting
an independent background set.  The theorem correctly leaves the
occurrence-faithful owner-port lift and the cut floor as premises.

## 8. Post-factor paired-port deletion

Suppose the `2p` distinct owner ports of a fixed wedge bank have one raw
pairwise-disjoint suffix linkage.  If `h` displayed paths meet the deleted
side-capacity bank, a claim loses both alternatives only if two of those
`h` paths belong to its disjoint owner pair.  Hence at most

\[
 \left\lfloor h/2\right\rfloor
\]

claims lose both paths.  Every other claim selects a surviving path from
the original disjoint linkage, proving the stated Rado-deficiency bound.

If `c` deleted common sources or guards independently kill both alternatives
of `c` claims, and `h` counts only the remaining side-specific path losses,
the bound becomes

\[
 c+\left\lfloor h/2\right\rfloor.
\]

This is an upper bound on terminal deficiency, not an assertion that the
casualties can always be repaired exactly.

## 9. Scope and verdict

The theorem does not construct the owner occurrences, prove their suffix
rank, identify the q1 terminal with the typed sink, or close topology,
residence, decoration, and regeneration.  It gives exact sufficient and
fixed-bank criteria once those physical premises are supplied.

The independent V1 verdict is **GO** at the corrected hashes above.
