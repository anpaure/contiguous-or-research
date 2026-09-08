# Audit of the two-phase root-path switch and a same-hexagon no-go

**Date:** 2026-08-07  
**Status:** proof audit.  The balanced-union theorem and its stated
component-action boundary are correct.  A second phase cannot be obtained
by merely taking the opposite matching on the same literal paired-root
`C_6`; it needs a different auxiliary realization, an occurrence copy, or
a larger packet.

## 1. Degree audit

Let `F=M_0 dotunion M_1` be the union of edge-disjoint perfect matchings.
For a locally simple packet family, let `O` and `N` be the disjoint unions
of the old and new banks.  At every vertex `v`, packetwise balance gives

\[
 d_{F'}(v)
 =d_F(v)-d_O(v)+d_N(v)
 =2.                                                     \tag{1.1}
\]

The hypotheses `N cap F=empty`, pairwise-disjoint old edges and
pairwise-disjoint new edges make this a literal simple-edge count.  Hence
`F'=(F-O) union N` is a spanning simple two-factor.  No alternation of the
global symmetric difference is needed for this degree statement.

At an internal root of an alternating-phase root path, the two packets
remove different selected edges, one from each phase, and install two
different unoccupied cross edges.  Thus the former one-phase `00` defect
is replaced locally by

\[
                         (1_0,1_1)\longmapsto(1'_0,1'_1).              \tag{1.2}
\]

The proof of Corollary 3.1 is therefore sound under its literal packet and
privacy hypotheses.

## 2. Component action is not hidden in degree balance

A two-factor can preserve degree two while splitting, joining, or merely
rerouting its components.  The audited theorem treats the advertised
two-break reconnection and the forest condition as additional hypotheses.
It does not infer either from (1.1).  Consequently its ordered-two-SDR
statement is an exact sufficient reduction, not a proof of topology.

## 3. Same literal `C_6` cannot supply both phases

Fix one paired-root hexagon `C_e`.  Its edge set is the disjoint union of
the two alternating parity matchings

\[
                         E(C_e)=A_e\mathbin{\dot\cup}B_e.              \tag{3.1}
\]

Suppose the GK phase uses

\[
                         M_0\cap E(C_e)=A_e.                           \tag{3.2}
\]

A phase-resolved packet on this same literal hexagon has exactly one
parity as its old bank and the other parity as its new bank.  If an
edge-disjoint second perfect matching `M_1` is also to use this same
hexagon as its old packet, it cannot use `A_e`; hence it must use `B_e`.
Then

\[
                         E(C_e)\subseteq M_0\cup M_1=F.                \tag{3.3}
\]

But the phase-1 packet would need `A_e` as its new bank.  Equation (3.3)
contradicts the required condition `N^1 subset E-F`.  Operationally,
adding `A_e` would duplicate the phase-0 edges unless those edges were
simultaneously removed by a larger correlated switch.

## Proposition 3.1 (same-hexagon no-go)

The opposite alternating coloring of the original paired-root `C_6` is
not a valid second phase for the balanced-union theorem.

This does not refute a second packet for the same abstract root-rotation
edge.  Such a packet may use

1. a different auxiliary lower vertex and hence a different literal
   hexagon;
2. a genuinely distinct occurrence copy with separately priced capacity;
   or
3. a larger correlated packet in which every re-used edge of `F` also
   belongs to the global old bank.

## 4. Same standard root facets also obstruct every alternative hexagon

The obstruction is not limited to reusing the canonical auxiliary
vertex.  Let a directed depth-two root edge have standard facets

\[
                         X_U=a+\{b\},\qquad X_V=a+\{x\}.              \tag{4.1}
\]

Its common rank-one extension is

\[
                         Q=a+\{b,x\}=t_0(X_V),                       \tag{4.2}
\]

so `X_V Q` is a phase-0 matching edge.  Any incidence hexagon containing
these same two lower facets, with any third lower facet `Z=a+{z}`, has
the two alternating parity matchings on its six edges.  Exactly one
parity contains `X_V Q`.

If that parity is chosen as the phase-1 old bank, then `M_1` intersects
`M_0`.  If the other parity is chosen as the phase-1 old bank, then
`X_V Q` belongs to the phase-1 new bank and hence intersects `F`.
Therefore:

## Proposition 4.1 (same-facet phase-1 `C_6` no-go)

Under the strict packet hypotheses of the balanced-union theorem, no
phase-1 paired `C_6` for the same directed root edge can use the standard
root facets `X_U,X_V`, regardless of its auxiliary third facet.

An actual second phase must consequently use at least one of:

1. different phase-specific root facets or occurrence copies;
2. a packet larger than a single `C_6`; or
3. a correlated global switch in which every phase-0 edge re-used by a
   new bank is simultaneously included in the global old bank.

## 5. Exact remaining construction

The conditional theorem is therefore proof-safe, but an explicit second
GK phase is not supplied by recoloring the known circuit or by changing
only its auxiliary facet.  The remaining local construction must produce,
for each required phase-1 root edge, a second literal balanced packet with
different phase-specific facets/occurrences or a larger correlated edge
set.  Its old edges must lie in `M_1`, its genuinely new edges must avoid
both phases, and its component reconnection must be the advertised one.
These packets must then extend together with the MNW annulus pattern to
one ordered two-SDR.
