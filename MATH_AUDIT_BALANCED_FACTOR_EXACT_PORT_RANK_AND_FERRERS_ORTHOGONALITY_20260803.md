# Independent audit: balanced-factor port rank and Ferrers orthogonality

**Date:** 2026-08-03  
**Verdict:** **GO after three proof-safety clarifications.**  
**Audited theorem:**
`MATH_THEOREM_BALANCED_FACTOR_EXACT_PORT_RANK_AND_FERRERS_ORTHOGONALITY_20260803.md`  
**Audited theorem SHA-256:**
`2ab0b8f8ce21425e4699ed9562bd53e9e6ec22fc7fc22d67042283a67d4b2232`

No finite search or H100 computation was used.  This is a direct
mathematical audit of the rank-transfer proof, the cut normalization, and
the uniform-gammoid counterexample.

## 1. Exact rank transfer

Let (I\subseteq P) be a maximum suffix-linkable port set.  For every
(Y\subseteq I), right (h)-regularity and left degree (h) give

\[
 h|Y|=e_B(Y,N_B(Y))\le h|N_B(Y)|.
\]

For (h\ge1), Hall therefore matches all of (I) to distinct gains.
Concatenating the matched private prefixes with a suffix linkage of (I)
services (|I|=r_\Gamma(P)) gains.  Conversely, every serviceable family
uses distinct unit ports whose suffixes form a linkage, so its size is at
most (r_\Gamma(P)).  Hence

\[
 \nu_{\rm claim}=r_\Gamma(P)
\]

is exact, not merely a lower bound.

The proof needs (h\ge1).  With (h=0), the displayed Hall cancellation is
invalid and there need be no factor-generated route at all.  The theorem
and its equal-shore corollary were patched to state (h\ge1).

The concatenation argument also needs endpoint-safe prefix privacy, not
only disjoint open interiors.  The interface was patched to exclude claim
starts and physical ports from all prefix interiors and to list the only
allowed prefix endpoint intersections.  It was further clarified that any
typed identity is already encoded in the occurrence-state port, so suffix
feasibility is a property of the port and hence defines one strict
gammoid.  Under these explicit hypotheses, the proof is complete.

## 2. Normalized cut identity

Attach a unit supersource arc to each port and unit terminal arcs to the
supersink.  For a finite cut with suffix source side (W), the cut capacity
is exactly

\[
 n-|P(W)|+c(W).
\]

Max-flow/min-cut therefore gives

\[
 r_\Gamma(P)=\min_W\{n-|P(W)|+c(W)\},
\]

and consequently

\[
 n-r_\Gamma(P)=\max_W\{|P(W)|-c(W)\}.
\]

Thus corank at most (C) is equivalent to every normalized cut satisfying
(c(W)\ge |P(W)|-C).  The theorem was patched only to remove a terminology
ambiguity: (W) may contain terminal vertices, whose unit terminal arcs
then contribute to (c(W)); it excludes the supersink.  This is the exact
cut family represented by the formula.

## 3. Uniform-gammoid construction

For (1\le c\le n), insert (c) unit bottlenecks between all (n) ports
and all (n) terminal vertices.  Any (X\subseteq P) with (|X|\le c)
links by assigning its ports distinct bottlenecks and distinct terminals.
The (c) bottlenecks separate every larger set.  Therefore

\[
 r_\Gamma(X)=\min\{|X|,c\},
\]

so the induced strict gammoid is exactly (U_{c,n}).  The extension is
strictly downstream of the declared ports and leaves the carrier, Ferrers
holes, named target allocation, factor, and private prefixes unchanged.

This proves the stated logical orthogonality: those upstream data alone do
not imply any nontrivial lower bound on suffix rank.  The construction is
not claimed to be an actual OR-word child, and it does not show that the
parent-derived suffix router is deficient.

## 4. Scope-safe conclusion

On the fixed balanced, equal-shore, edge-private, port-complete,
occurrence-typed interface, full service is equivalent to full suffix-port
rank, and bounded claim loss is equivalent to bounded suffix corank.  Dense
or punctured Ferrers data do not establish that rank without an additional
literal suffix-capacity expansion theorem.

The result must not be cited outside this fixed-network interface, for a
router with bypass paths, for claim-dependent suffix legality not encoded
in ports, or as a negative theorem about the actual all-dimensional OR
construction.
