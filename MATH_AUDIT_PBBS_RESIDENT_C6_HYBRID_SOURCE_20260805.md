# Independent audit: the resident/common-history clean-C6 hybrid

**Date:** 2026-08-05  
**Method:** direct window indexing and occurrence-tagged cut-path replay; no
computation  
**Audited file:**
`MATH_THEOREM_PBBS_RESIDENT_C6_HYBRID_SOURCE_LOWER_TRANSPORT_AND_UPPER_MONOTONICITY_20260805.md`

## Verdict

The local/prospective theorem is proof-safe.  One literal source packet
realizes both imported structures: the common-history occurrence bijection
on every strict-lower row and the resident q-port inclusion on the complete
internal cyclic upper deck.

The occurrence tags on the three equal set-valued primed contexts are
essential.  With those tags retained, the source rethread has one component;
without them, the displayed set words alone do not record which continuation
was cut from which old port.

## 1. Derivative replay

For port `i` the source cycle is

\[
 (L_i,C_1,\ldots,C_d,R_{i+1},C'_1,\ldots,C'_d),
\]

where `L_i={c,a_i}`, `R_(i+1)={a_i,a_(i+1)}`,
`union C_j=K`, and `C'_j=C_j-x_j+y_j`.
Its consecutive windows of length `d+1`, in order, are

\[
 Q_i, P_{i,0},P_{i,1},\ldots,P_{i,d},
 Q_{i,0},Q_{i,1},\ldots,Q_{i,d-1}.
\]

The first shift replaces `L_i` by `R_(i+1)`.  The next `d` shifts replace
`C_1,...,C_d` successively by their primed copies.  The wrap shift replaces
`R_(i+1)` by `L_i`, and the final `d-1` shifts restore the unprimed copies.
This is exactly the frozen resident return rail, with no missing or duplicated
owner window.

## 2. Cut-path topology replay

Cut old port `i-1` immediately before `R_i`.  Its right path begins

\[
 (R_i,\mathcal C')
\]

and, after traversing its old continuation, reaches `L_(i-1)`.  Attach that
tagged path after `(L_i,\mathcal C)`.  The new hinge is

\[
 Q_i\longrightarrow P_{i-1}.
\]

After the return rail the continuation index is `i-1`.  Repeating therefore
acts by the 3-cycle `i -> i-1` and visits all three old port cycles in one
source cycle.  This proves the topology assertion.

The same fragments are exactly the inverse common-history rethread

\[
 (L_i,\mathcal C,R_{i+1})
   \longmapsto
 (L_i,\mathcal C,R_i),
\]

with the complete tagged right context moved together with `R_i`.  Hence the
imported strict-lower occurrence bijection applies literally, rather than to
an isomorphic but different factorization.

## 3. Consequences and scope

Composition preserves every occurrence-labelled lower compiler edge because
each packet supplies a bijection preserving address, width and value.  The
resident theorem independently gives positive-run residence and

\[
 \operatorname{Deck}_{\rm cyc}(H_2)
 \subseteq
 \operatorname{Deck}_{\rm cyc}(H_3)
\]

for intervals internal to the displayed cyclic packet.  These conclusions
therefore hold simultaneously on the same source positions.

Nothing in this audit supplies a global packet packing, protects intervals
crossing an arbitrary exterior or a final linear cut, proves zero-gap
residence, or transports extra typed common-cap routes.  Those remain global
premises and are not consequences of the local identity.

