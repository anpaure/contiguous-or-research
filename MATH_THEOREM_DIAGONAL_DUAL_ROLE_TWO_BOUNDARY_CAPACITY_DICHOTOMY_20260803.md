# Diagonal dual-role turns and the two-boundary capacity dichotomy

**Date:** 2026-08-03  
**Status:** exact fixed-row occurrence/capacity theorem.  No computation is
used.  The theorem does not construct a dual-role common-cap ticket; it
identifies the extra physical resource such a ticket must supply.

Throughout the positive dual-role statements, an owner occurrence may be
the unique transit vertex of its own route and an upper-turn occurrence may
be the terminal of that route while retaining its declarative witness role.
Each is charged once in the displayed capacity ledger.  If middle-owner
reservation deletes the owner vertices rather than permitting this
dual-service interpretation, none of the positive linkages below survives
without a private owner bypass.  That issue is deliberately separate from
the two-boundary source cut proved here.

## 0. Result

Let indices lie in `Z_W`, let `2<=d<W-2`, and let nonempty source-letter
occurrences `a_i` have values `A_i`.  Assume the cyclic diagonal row is on
the flat q1-exact face: the sets

\[
 T_i=\bigcup_{j=i}^{i+d}A_j,
 \qquad
 P_i=\bigcup_{j=i+1}^{i+d}A_j
\tag{0.1a}
\]

have ranks `r` and `r-1`, respectively, and satisfy

\[
                    P_i=T_i\cap T_{i+1}.
\tag{0.1b}
\]

Put

\[
 R_i=T_i\cup T_{i+1}.
\tag{0.1c}
\]

Give the corresponding port, owner, and upper-turn intervals their literal
occurrence addresses

\[
 p_i=[i+1,i+d]_W,\qquad
 o_i=[i,i+d]_W,\qquad
 q_i=[i,i+d+1]_W.
\tag{0.1d}
\]

The abstract three-level occurrence graph has the chains

\[
 p_i-o_i-q_i,
 \qquad
 p_i-o_i-q_{i-1},
 \qquad
 p_i-o_{i+1}-q_i,
 \qquad
 p_i-o_{i+1}-q_{i+1}.
\tag{0.2}
\]

If only the occurrence vertices are priced, the paths

\[
                         p_i-o_i-q_i
\tag{0.3}
\]

are pairwise disjoint and give a perfect port-to-upper-token linkage.  This
is the abstract dual-role shortcut.

If every literal inclusion step in one of the four displayed chains must
also traverse the source-letter
occurrence which supplies the newly exposed boundary, then every path in
(0.2) uses **two distinct** source occurrences.  Consequently a unit-
capacity source-letter bank supports at most

\[
                         \left\lfloor {W\over2}\right\rfloor
\tag{0.4}
\]

pairwise capacity-disjoint dual-role paths.  In particular, the perfect
occurrence matching alone cannot be cited as a capacity-faithful terminal
router.

The factor two is exact.  Give every source occurrence capacity two.  Then
the complete family (0.3), with its literal edge labels retained, is a
capacity-feasible full linkage **on the dual-service owner/upper face**:
every source occurrence has load exactly two.  Alternatively, if each owner
has a private direct attachment to its matched upper token which does not
traverse another source capacity, the paths `p_i-o_i-q_i` use only the first
boundary occurrence and form a unit-capacity full linkage, again provided
that the owner occurrence is not separately deleted.

Thus a complete dual-role ticket must prove at least one of the following,
in the actual cap state:

1. a private/direct owner-to-upper-token attachment;
2. two units of honest capacity at every boundary source used by the
   canonical two-step lift; or
3. a different full-rank route family whose complete literal capacity
   ledger evades the two-boundary count.

Calling a required upper witness an "available terminal" without one of
these physical statements is not sufficient.

## 1. Literal labels on the four local chains

The lower extensions are

\[
 P_i\cup A_i=T_i,
 \qquad
 P_i\cup A_{i+d+1}=T_{i+1}.
\tag{1.1}
\]

The upper extensions are

\[
 T_i\cup A_{i+d+1}=R_i,
 \qquad
 T_i\cup A_{i-1}=R_{i-1}.
\tag{1.2}
\]

Therefore the four chains in (0.2) have the following ordered pairs of
source-occurrence labels:

\[
\begin{array}{c|c}
\text{chain}&\text{source occurrences used}\\
\hline
p_i-o_i-q_i&(a_i,a_{i+d+1})\\
p_i-o_i-q_{i-1}&(a_i,a_{i-1})\\
p_i-o_{i+1}-q_i&(a_{i+d+1},a_i)\\
p_i-o_{i+1}-q_{i+1}&(a_{i+d+1},a_{i+d+2}).
\end{array}
\tag{1.3}
\]

Under `2<=d<W-2`, the two entries in every row of (1.3) are distinct
physical source positions.  Equal letter values would not merge their
occurrence capacities.

## 2. Unit-capacity obstruction

### Theorem 2.1

In the literal two-boundary model of Section 1, every pairwise
capacity-disjoint family of dual-role paths has size at most `floor(W/2)`.

### Proof

Every admitted path uses two distinct members of the `W`-element physical
source bank by (1.3).  Pairwise capacity-disjointness makes the two-element
sets used by different paths disjoint.  A family of `x` paths therefore
uses `2x` distinct unit source capacities, so `2x<=W`.  This is (0.4).
`square`

This is a resource cut, not a semantic or Hall obstruction.  If boundary
letters are only edge labels and are not physical unit resources in the
chosen model, Theorem 2.1 does not apply.  Conversely, if they were priced
in the lower diagonal router, they cannot silently become free in the
owner-to-upper attachment.

## 3. Exact capacity-two realization

### Theorem 3.1

Assign capacity two to every `a_h` and unit capacity to every port, owner,
and upper-turn occurrence, with the owner and upper roles sharing those
single charged vertices as specified in Section 0.  Then the `W` paths

\[
                         p_i-o_i-q_i
\tag{3.1}
\]

form a feasible full linkage.

### Proof

The port, owner, and upper-turn coordinates in (3.1) are each injective in
`i`.  By the first row of (1.3), path `i` uses `a_i` and `a_(i+d+1)`.
For a fixed `h`, the occurrence `a_h` lies on exactly the paths indexed by

\[
                         i=h,
 \qquad                 i=h-d-1.
\tag{3.2}
\]

These indices are distinct under the stated range of `d`.  Hence every
source occurrence has load exactly two and all other finite resources have
load one.  The semantic endpoint is correct because

\[
 P_i\subset T_i\subset R_i.
\]

Thus (3.1) is a capacity-feasible full linkage. `square`

### Corollary 3.2 (private compressed attachment)

Suppose the lower step `p_i-o_i` is the literal route using `a_i`, while
`o_i-q_i` is replaced by a private attachment which consumes no source
occurrence and shares no unit capacity with another attachment.
If the owner occurrences remain available as the unique transit vertices
of their routes, then (3.1) is a unit-capacity full linkage.

The corollary states the smallest transparent positive interface.  It is
strictly stronger than the occurrence perfect matching: it certifies how
the second semantic extension is paid physically.

## 4. Relation to the terminal common-cap gate

The cyclic owner-to-upper-token graph is already a perfect matching, and a
single-role unused-socket interpretation has a linear terminal cut at fixed
additive charge.  The present theorem closes the logical gap between those
facts.

Reusing upper-turn tokens can evade the single-role cardinality cut, but
only after a complete dual-role route is materialized.  In the canonical
two-boundary lift, the raw occurrence matching has source congestion two;
with unit sources its full-linkage rank is at most `floor(W/2)`.  A valid
all-dimensional construction must therefore export the compressed/private
attachment of Corollary 3.2, honest doubled capacity, or a different
capacity-faithful route family.  It must additionally retain the owner as a
legal transit resource or supply a private bypass if owner reservation
deletes it.  Product closure between two occurrence coordinates,
transported background, guards, and regeneration remain separate
hypotheses.
