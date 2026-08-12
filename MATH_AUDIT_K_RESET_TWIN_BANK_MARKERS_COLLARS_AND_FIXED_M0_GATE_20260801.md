# Audit of the reset twin-bank marker ledger, clipped collars, and the fixed-`M_0` gate

**Date:** 2026-08-01  
**Lane:** K, protected reset--return host  
**Status:** exact symbolic audit.  The four-marker separation and the raw
`5d`-owner twin-bank counts are correct.  The one-sided collar statement is
a boundary-state assertion, not a completed ambient embedding: all four
path ends export nontrivial nested run requirements, and the frozen finite
audit constructs no collar.  The remaining immediate-layer obstruction is
the joint fixed-`M_0` lower/root, head-injective, and graphic correlation;
ordinary degree-only rainbow matching cannot close it.

Throughout the collar audit, `d>=2`.  This note audits
`MATH_THEOREM_RESET_RETURN_DOVERLAP_AND_UPPER_FERRERS_TWIN_BANK_20260801.md`
against the corrected scope of
`MATH_THEOREM_HEAD_INJECTIVE_COMPLETION_AND_PROTECTED_INDUCED_PATH_20260801.md`.
It does not challenge the exact `d`-overlap or the two Ferrers-triangle
coverage theorem.

## 1. Four marker signatures

Write a resource's marker signature in the order

\[
 (\eta _1,\eta _2,\eta _3,\eta _4).
\]

Every packet owner contains all of `H`.  Therefore every packet owner,
every packet lower-q1 colour, and every packet upper-q1 colour has signature
`1111`.

For the `X`-gap path, direct substitution in (4.2)--(4.5) gives

\[
\begin{array}{c|ccc}
 &\text{owners}&\text{lower q1}&\text{upper q1}\\ \hline
 L\text{-side}&0111&0111&0111\\
 R\text{-side}&1011&1011&1011\\
 \text{central edge}&-&0011&1111.
\end{array}                                                \tag{1.1}
\]

For the `U`-gap path, the owner signatures are

\[
 \begin{array}{c|ccc}
 \text{owners}&P\text{-side and }M_0&M_1,\ldots,M_d&
 M_{d+1}\text{ and }S\text{-side}\\ \hline
 \text{signature}&1110&1100&1101.
 \end{array}                                               \tag{1.2}
\]

The left outer lower colours (including `P_1 cap M_0`) have signature
`1110`; every middle-geodesic lower colour has signature `1100`; and the
right outer lower colours have signature `1101`.  The upper colours have
signature `1110` on the left outer segment and on `M_0 M_1`, signature
`1100` on the internal middle edges, and signature `1101` on
`M_d M_(d+1)` and the right outer segment.  In particular, no `U`-bank
upper colour has signature `1111`.

Consequently:

1. the two banks are pairwise disjoint on owners and on both q1 shores;
2. every bank owner and lower-q1 colour is disjoint from the packet;
3. every bank upper-q1 colour is disjoint from the opened packet palette,
   except potentially the central `X`-bank colour;
4. that central colour is
   \(V_0\cup V_1=B_X\), and the overlap identity identifies it with exactly
   the upper colour of the one omitted packet edge.

Within each row of (1.1)--(1.2), strict `X` prefixes/suffixes, strict `U`
prefixes/suffixes, or the ordered middle geodesic distinguish the resources.
Thus the exact raw ledger is

\[
 \boxed{5d\text{ owners},\qquad 5d-2\text{ lower q1 colours},\qquad
        5d-2\text{ upper q1 colours}.}                    \tag{1.3}
\]

The four-marker claim is therefore valid at precisely this raw-bank scope.

## 2. All four clipped boundary profiles

The two paths have clipped positive runs at both ends, not just at the two
ends displayed in Section 7 of the source theorem.  Reading the paths in
their displayed orders gives the complete table below.  An entry is the
number of additional consecutive owners required to reach length `d+1`.

\[
\begin{array}{c|c|c}
\text{path end}&\text{coordinate}&\text{deficiency}\\ \hline
\mathcal P_X\text{ left}&\eta _2&1\\
\mathcal P_X\text{ left}&x_s\ (1\le s\le d-1)&s+1\\
\mathcal P_X\text{ right}&\eta _1&1\\
\mathcal P_X\text{ right}&x_s\ (2\le s\le d)&d+2-s\\ \hline
\mathcal P_U\text{ left}&\eta _3&1\\
\mathcal P_U\text{ left}&u_s\ (1\le s\le d-1)&s+1\\
\mathcal P_U\text{ right}&\eta _4&1\\
\mathcal P_U\text{ right}&u_s\ (2\le s\le d)&d+2-s.
\end{array}                                                \tag{2.1}
\]

For example, `x_s` occurs in the left boundary run of `P_X` exactly
`d-s` times and in its right boundary run exactly `s-1` times.  Similarly,
`u_s` occurs at the two boundaries of `P_U` exactly `d-s` and `s-1`
times.  The marker runs have length exactly `d`.  All other nonconstant
positive runs internal to either path have length at least `d+1`, agreeing
with Lemma 7.1.

Each column of (2.1) is nested, so a one-exchange Ferrers continuation can
service one exposed side with at most `d` new roots, provided its mandatory
superlevel sets, filler labels, and endpoint edge are supplied.  What does
**not** follow from nestedness alone is that two unspecified one-sided
collars close an arbitrary embedding of both paths.  The ambient
construction must do one of the following:

* continue the two uncollared profiles through adjacent exterior roots;
* give all four ends explicit one-sided collars; or
* pair ends by explicit two-sided connector paths and verify the resulting
  run schedules.

There is no scalar-distance obstruction to the last option.  In the
displayed normal form,

\[
 d_J(R_{d-1},P_{d-1})=d+1,
 \qquad
 d_J(S_{d-1},L_{d-1})=d.                                 \tag{2.2}
\]

The first cross connector needs `d` internal roots.  Although the second
endpoint distance is only `d`, its two incident boundary profiles each
need `d` further positive owners in their sharp row, so a residence-closing
second connector also needs `d` internal roots; it must take a one-edge
detour from a shortest geodesic.  A short Johnson connector does not
automatically have the nested run order, fresh q1 palette, or rooted
orientation required here.  Those are exactly the data a global host proof
must provide.

### Proposition 2.2 (correct conditional two-collar/four-end statement)

Let `C_XU=(C_1,...,C_d)` be an internal connector from `R_(d-1)` to
`P_(d-1)`, and let `C_UX=(D_1,...,D_d)` be an internal connector from
`S_(d-1)` to `L_(d-1)`.  The four bank-end profiles are residence-closed
provided

\[
\begin{array}{ll}
x_s\in C_t &(2\le s\le d,\ 1\le t\le d+2-s),\\
u_s\in C_t &(1\le s<d,\ d-s\le t\le d),\\
u_s\in D_t &(2\le s\le d,\ 1\le t\le d+2-s),\\
x_s\in D_t &(1\le s<d,\ d-s\le t\le d),
\end{array}                                                \tag{2.3}
\]

and `C_1,C_d,D_1,D_d` contain respectively the marker obligations
`eta_1,eta_3,eta_4,eta_2`.  These containments are exactly the superlevel
sets encoded by (2.1), so they are necessary on a sharp `d`-root connector
and sufficient for the old four clipped runs.  One must additionally
require that the connectors create no new internal short run.

If both connectors are Johnson, internally vertex-disjoint, and disjoint
from the raw bank owners, their union with `P_X union P_U` is a
`7d`-owner Johnson cycle.  Deleting one chosen edge in each connector leaves
two protected paths with exactly

\[
                         7d-2                            \tag{2.4}
\]

Johnson edges.  Together with the opened packet path this gives the quoted
`11d-1` protected Johnson edges and `22d-2` containment incidences.

This is the corrected conditional interpretation of the two-collar count.
It is not yet an existence theorem: the two deleted connector edges export
new boundary states to the ambient host, and the connector owners and both
q1 palettes still have to be proved private and rooted-compatible.

The frozen audit
`scratch/audit_reset_return_upper_ferrers_twin_bank_20260801.cpp` checks
the raw owners, raw lower/upper-q1 palettes, Ferrers witnesses, and
**internal** positive runs.  It contains no collar construction.  Hence its
`d=2..40` PASS authenticates Sections 3--6 and Lemma 7.1, not a global
collared embedding.

In particular, the count after adding two one-sided collars is only the
conditional protected budget

\[
 5d+2d\le7d\text{ bank/collar owners}.                    \tag{2.5}
\]

The claimed `7d-2` q1 edges additionally presumes that each new collar
attaches as a simple extension of one existing path and that no collar q1
colour collides with either bank, the packet, or the other collar.  Marker
separation of the original `5d` owners does not itself prove those new
facts.

## 3. What a collision-safe collar must export

For each added directed Johnson edge `T -> V`, put

\[
 J=T\cap V,\qquad R=T\cup V.                              \tag{3.1}
\]

A literal protected collar needs all of the following, not just (2.1):

1. its owners `T,V` are new and its lower colours `J` and immediate upper
   colours `R` avoid the protected packet/bank palettes;
2. the selected predecessor tails are distinct;
3. the adjacent exterior owner continues every exported boundary run;
4. every source interval crossing the collar/host join either retains its
   old witness or has a named duplicate;
5. its directed incidences extend the same predecessor matching used by
   the ambient Catalan construction.

Items 1--2 can plausibly be enforced using marker signatures and private
fillers, but neither follows from the raw four-marker table once filler
coordinates are exchanged.  Items 3--4 are inherently properties of the
chosen ambient chronology.  Maximal erosion converts owner intervals to
literal source intervals only after this whole chronology has passed the
residence test; it cannot certify the join in advance.

## 4. The exact fixed-`M_0` equation

Let

\[
 M_0:{[2m-1]\choose m-1}\longrightarrow{[2m-1]\choose m}
\]

be the predecessor incidence matching.  If an upper colour `R` is assigned
tail owner `T=psi(R)`, then `J=M_0^{-1}(T)` is already fixed.  The only legal
other corner is

\[
 V_{M_0}(R,T)=J\cup(R-T).                                 \tag{4.1}
\]

Equivalently, a proposed second facet `phi(R)` is rooted-compatible iff

\[
 \boxed{M_0\bigl(\psi(R)\cap\phi(R)\bigr)=\psi(R).}        \tag{4.2}
\]

The protected packet and each explicitly oriented bank path can prescribe
(4.2) on their own distinct lower colours.  The global problem is to extend
those prescriptions while making `phi` injective and the directed owner
graph graphic-independent (or giving the required controlled component
topology).  An arbitrary disjoint second-facet matching does not do this:
two distinct `(R,T,phi(R))` triples can have the same intersection
`T intersect phi(R)`, and even distinct intersections need not extend to one
perfect `M_0`.

Thus the surviving immediate-layer gate is the simultaneous choice

\[
 \boxed{
 \begin{gathered}
 M_0\text{ extends every protected packet/bank/collar tail};\\
 \phi(R)=V_{M_0}(R,\psi(R))\text{ is injective for every upper colour};\\
 \{\psi(R)\to\phi(R)\}\text{ has the required graphic topology}.
 \end{gathered}}                                           \tag{4.3}
\]

Global reversal removes the need to solve (4.3) simultaneously in two
opposite phase-address systems: one may build one oriented complete host
and reflect its whole certificate.  It does not weaken (4.3) within that
one host.

## 5. Why generic rainbow matching cannot close (4.3)

For a fixed `M_0`, each immediate-upper colour has `m+1` candidate
occurrences, while the relevant occurrence graph has maximum degree
`Delta=m-1`.  The generic Aharoni--Berger--Meshulam bound for a graph
requires colour classes of size at least `2 Delta`.  Here

\[
 m+1<2(m-1)\qquad(m\ge4),                                \tag{5.1}
\]

with the first case `m=4` equal to `2 Delta-1`.  Wdowinski's sharp abstract
examples at `r Delta-1` show that no argument using only uniformity,
maximum degree, and class size can replace this by the false
`|colour|>Delta` shortcut.

This is not a Boolean impossibility theorem: those sharp examples live in
the general multihypergraph setting.  It proves that a positive result must
use the Boolean incidence equation (4.2), a correlated construction of
`M_0`, or comparably strong structure.

## 6. Audited conclusion

The exact local conclusion is

\[
 \boxed{
 \begin{array}{l}
 \text{the }d\text{-overlap has only the two stated upper Ferrers leaves};\\
 \text{the raw twin bank repays them with }5d\text{ collision-free owners};\\
 \text{its }5d-2\text{ lower and }5d-2\text{ upper q1 colours are simple};\\
 \text{all internal positive runs are residence-safe.}
 \end{array}}                                             \tag{6.1}
\]

The exact surviving obstruction is not another local Ferrers deficit.  It
is a **one-oriented protected host theorem**: realize collision-safe
boundary continuations for all four profiles in (2.1), satisfy the joint
fixed-`M_0` relation (4.3), join/open the protected paths without losing
exterior all-width witnesses, and retain the terminal compiler and a
reversal-closed regenerative interface.  None of these rows follows from
the raw marker ledger or from degree-only rainbow matching.
