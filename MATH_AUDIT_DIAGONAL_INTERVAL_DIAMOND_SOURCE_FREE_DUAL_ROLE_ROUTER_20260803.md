# Independent proof audit: diagonal interval-diamond source-free router

**Date:** 2026-08-03  
**Audited file:**
`MATH_THEOREM_DIAGONAL_INTERVAL_DIAMOND_SOURCE_FREE_DUAL_ROLE_ROUTER_20260803.md`  
**Method:** symbolic rederivation from interval addresses and Boolean ranks;
no search or solver.

## 0. Verdict

**PASS, with the scope stated in the theorem.**

The new theorem correctly distinguishes two capacity models which had
previously been conflated:

* native physical resources are interval addresses, and different
  intervals may overlap in source positions;
* the stronger boundary-node refinement additionally turns each endpoint
  letter used to certify an inclusion into a unit transit vertex.

On the native face, the q1 seam is a literal physical interval diamond and
the two displayed orientations are pairwise vertex-disjoint full
linkages.  The proof therefore supplies a genuine source-free
owner-to-upper attachment and removes the additional \(W\)-socket premise
for one occurrence coordinate when the upper witness is accepted as the
same terminal occurrence/type.

The result is not an all-dimensional construction.  In particular, it
does not infer dual-role acceptance or two-coordinate coalescence from
marginal occurrence matchings.

## 1. Address audit

For fixed \(i\), the four addresses are

\[
 p_i=[i+1,i+d],\quad
 o_i=[i,i+d],\quad
 o_{i+1}=[i+1,i+d+1],\quad
 q_i=[i,i+d+1].
\]

Hence

\[
 p_i\subset o_i\subset q_i,qquad
 p_i\subset o_{i+1}\subset q_i.
\]

Every inclusion enlarges the physical interval by one endpoint.  Under
\(d<W-2\), the four addresses are distinct and cyclic wraparound does not
collapse an interval with its complement.  Translation in \(i\) is
injective on each fixed-length address family.

Thus the physical part of the diamond is exact.

## 2. Value and rank audit

From the definitions,

\[
 P_i\cup A_i=T_i,qquad
 P_i\cup A_{i+d+1}=T_{i+1}.
\]

Also

\[
 T_i\cup A_{i+d+1}
 =T_i\cup T_{i+1}
 =R_i,
\]

and symmetrically

\[
 T_{i+1}\cup A_i=R_i.
\]

Since \(|T_i|=|T_{i+1}|=r\) and
\(|T_i\cap T_{i+1}|=|P_i|=r-1\), the owners are distinct and

\[
 |R_i|=r+r-(r-1)=r+1.
\]

Therefore all four value inclusions are strict rank-one Boolean Hasse
edges.  No inference from flatness alone is used: q1 exactness is an
explicit hypothesis.

## 3. Linkage audit

For the first phase, the finite vertex triples are

\[
 (p_i,o_i,q_i).
\]

All three coordinates are injective.  For the second phase they are

\[
 (p_i,o_{i+1},q_i),
\]

and \(i\mapsto i+1\) is a permutation.  Thus each phase contains \(W\)
pairwise vertex-disjoint paths.

Across both phases, every port and upper occurrence lies on its two diamond
paths.  Owner \(o_i\) lies on the first-phase path from \(p_i\) and the
second-phase path from \(p_{i-1}\).  Hence all finite vertex multiplicities
are exactly two, and the uniform half-flow has load one.

The directed incidence arcs are distinct ordered address pairs.  There is
no unlisted shared arc capacity.

The mixed-ledger corollary is also exact.  In its first phase the four
finite coordinates are

\[
 (p_i,a_i,o_i,q_i),
\]

all injective in \(i\).  In the second they are

\[
 (p_i,a_{i+d+1},o_{i+1},q_i),
\]

and both translations are permutations.  Thus source capacity one is
already sufficient when only the lower boundary step is source-priced and
the owner-to-upper attachment is a direct occurrence Hasse edge.  This is
strictly stronger than merely observing that all boundary labels may be
left unpriced.

## 4. Why source positions are not native capacities

An OR word assigns a value to every interval address.  Two chosen intervals
may overlap arbitrarily.  Their coexistence is automatic because both are
evaluated in the same fixed word.  The only immediate matching collision is
using one **identical interval address** for two distinct selected target
values.

Consequently, the fact that a singleton position \([h,h]\) labels two
different Hasse incidences does not make those two longer interval
occurrences collide.  Turning \([h,h]\) into a transit vertex is an
additional modelling restriction.  The earlier capacity-two theorem
correctly analyzed that restricted network; the present theorem correctly
uses the native interval-address network.

This audit does not say source positions can never be capacities.  A guard
or packet may explicitly reserve a singleton occurrence.  It says only
that containment of that position in another interval does not consume the
singleton **cell** a second time.

## 5. Owner attachment and bundle contraction

The arcs

\[
 o_i\to q_i
\]

have injective tails and heads, are physical interval Hasse incidences, and
carry no finite internal vertex.  They are therefore the private
source-free attachments requested by the previous dichotomy.

If an owner is deleted as a transit capacity, the direct bundle
\(p_i\rightsquigarrow q_i\) remains proof-safe only because its record
contains the complete conjunctive data

\[
 (P_i,T_i,T_{i+1},R_i,A_i,A_{i+d+1}).
\]

The terminal Rado theorem explicitly permits one representative to encode
one complete canonical route.  The bundle is not being split into
independently selectable atoms.  Its finite endpoints are injective, so the
contraction does not hide a capacity collision.

## 6. Dual-role audit

Upper service and terminal service may share \(q_i\) only on the stated
dual-role face.  The upper role declares

\[
 \operatorname{OR}(q_i)=R_i.
\]

The terminal route declares the same occurrence and envelope.  Thus no
second OR value is assigned to the cell.  Charging it once is exact.

If instead the terminal is required to be unused, to carry another value,
or to live in a different guard state, the coinstantiation fails.  The
theorem explicitly excludes those cases and therefore does not evade the
single-role terminal cut by relabelling it.

## 7. Two-coordinate audit

Two capacity-separated q1 banks give two independent full-rank gammoids.
With global product closure, the terminal two-Rado theorem then gives zero
common deficiency.

If both coordinates use one shared \(W\)-cell bank and require two distinct
terminal units per ticket, total demand is \(2W\) against cut capacity
\(W\).  Marginal perfect matchings are insufficient.  Conversely, exact
diagonal coalescence \((q_i,q_i)\) uses one unit per ticket and removes this
cut, but its legality is an additional paired-occurrence statement.

Thus the claimed remaining frontier—cross-coordinate allocation or
coalescence plus background/product closure—is exact.

## 8. Scope checklist

Proved:

* literal physical and Boolean diamonds;
* two full unit-capacity linkages on the native interval-address face;
* private source-free owner-to-upper attachments;
* full one-coordinate port gammoid rank;
* the distinction from the boundary-node capacity-two model; and
* the shared-bank two-coordinate cut.

Not proved:

* existence of all-dimensional q1-exact diagonal carriers;
* acceptance of upper turns as terminals in every common-cap state;
* two-coordinate coalescence or global product closure;
* transported background, arbitrary guards, or regeneration;
* an additive-constant upper bound.

No correction to the theorem is required.
