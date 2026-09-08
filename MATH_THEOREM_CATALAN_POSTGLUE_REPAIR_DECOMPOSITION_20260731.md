# Post-glue repair separates ECO topology from Catalan decoration

Date: 2026-07-31  
Status: corrected exact all-dimension implication and quantifier theorem;
exact repaired project-\(m=5\) calibration; no all-\(m\) decorated-2-factor
construction

## 0. Verdict

For the central Catalan Linear Matching Theorem, it is not necessary to
carry one fixed decoration through the component glues.

The earlier Hamilton construction remains sufficient:

\[
\boxed{
 \text{physically disjoint ECO incidence hypertree}
 \longrightarrow
 \text{one Hamilton middle-levels cycle}
 \longrightarrow
 \text{final joint-decoration repair}.}              \tag{0.1}
\]

The first arrow is purely topological.  The second may use an arbitrary
packet of degree-preserving alternating circuits; intermediate packet states
need not be decorated.  Only the final Hamilton cycle must admit a joint
alternating SDR **whose binary mark trace lies on the linear-forest side**.
The trace qualification is load-bearing: a joint alternating SDR alone
gives a perfect diamond matching of maximum degree two, but may leave one
cycle.

Thus owner alignment, residual gap Hall and occurrence-router resilience do
not constrain the ECO gluing stage on this post-glue face.  They are needed
only if a decoration must be transported through the glues, or when a
catalogue theorem is used in place of a literal disjoint hypertree.

The repaired project-\(m=5\) construction already realizes (0.1): a raw
component gluing produces a Hamilton cycle with the period-three palette
defect, and the synchronized three-\(C_{10}\) packet repairs the final cycle
to a joint decoration.  The independently audited repair-first ECO
construction proves that the two orders can also coexist at this base.

It is not minimal.  The exact weaker order is

\[
\boxed{
 \text{any spanning middle-levels 2-factor}
 \longrightarrow
 \text{terminal componentwise decorated 2-factor}.}             \tag{0.2}
\]

The terminal factor needs globally bijective upper and lower turn
representatives and componentwise alternating shore marks.  Every marked
component must contain an unmarked occurrence and lie off the ordinary
binary cycle face; wholly unmarked components use either residual cross
phase.  A wholly marked component is forbidden because it lifts to two rail
cycles.  Thus neither Hamiltonization nor component merging is part of the
minimal central trace target.

## 1. Topological stage

Let \(F\) be a spanning two-factor of the middle-levels graph, with component
set \(V\).  Let \(S\) be a family of pairwise vertex-disjoint alternating
incidence hexagons.  For \(t\in S\), let \(H_t\subseteq V\) be the set of old
factor components containing its three old matching edges.

Assume:

1. every \(t\) is a strict physical hypermerge on \(H_t\); and
2. the component--atom incidence graph
   \[
       \mathcal I(S)\quad\text{on}\quad V\sqcup S,\qquad
       v\sim t\Longleftrightarrow v\in H_t
   \]
   is a tree.

Pairwise vertex-disjointness makes the symmetric differences commute.
The strict incidence-hypertree theorem then gives

\[
                  H=F\mathbin\triangle\bigtriangleup_{t\in S}C_t
                                                               \tag{1.1}
\]

as one Hamilton cycle.  Equivalently, with \(w_t=|H_t|-1\), the exact
topology rows are

\[
 \sum_{t:H_t\subseteq A}w_t\le |A|-1
 \quad(\varnothing\ne A\subseteq V),\qquad
 \sum_tw_t=|V|-1.                                     \tag{1.2}
\]

No turn palette, gap matching or router appears in (1.1)--(1.2).

## 2. Repair stage

Let \(P=(P_1,\ldots,P_s)\) be an ordered packet of alternating even circuits
on the middle-levels graph.  Put

\[
 H_0=H,\qquad H_i=H_{i-1}\mathbin\triangle P_i.       \tag{2.1}
\]

Assume every \(H_i\), including the endpoint \(H_s\), is a spanning
two-factor.  Intermediate factors may have missing or repeated turn colours
and need not be connected.

Assume only at the endpoint that \(H_s\) has a componentwise Catalan
decoration: globally, one occurrence of every upper turn colour and one of
every lower turn colour are selected; on every marked factor component the
selected shore types alternate cyclically.  Every marked component must
contain at least one unmarked occurrence and be on the linear-forest side:
some positive zero-run has length at least four or some maximal one-run has
even length.  A wholly unmarked component uses either alternating residual
cross phase.  A wholly marked component is not accepting.

### Theorem 2.1 (post-glue repair implication)

Under the hypotheses of Sections 1--2, the Catalan Linear Matching Theorem
holds in this dimension.

#### Proof

Equation (1.1) and the incidence-hypertree theorem give one possible literal
Hamilton start, although this is surplus.  Equation (2.1) gives the terminal
spanning factor \(H_s\).  The decorated-2-factor theorem converts its global
turn representatives and componentwise residual matchings into one perfect
Boolean-diamond matching.  Partially marked components are acyclic by the
trace condition, unmarked components contribute disjoint cross edges, and
wholly marked components were excluded.  The physical lift is therefore a
spanning \(\operatorname{Cat}_m\)-path forest.  No decoration or connectivity
was used before the final endpoint. \(\square\)

### Corollary 2.2 (what disappears)

On the face of Theorem 2.1, the following are not hypotheses on the gluing
family \(S\):

* existence of a gluing family or component-merging tree at all;
* forced-port owner alignment;
* residual forced-port Hall;
* fixed-decoration transparency; or
* occurrence-router resilience.

They return if the repair packet must be moved before the glues, if the
atoms overlap and need an ordered catalogue proof, or if downstream
residence/shadow/compiler state must be preserved at every intermediate
prefix.

## 3. Exact project-\(m=5\) calibration

The canonical raw factor at project \(m=5\) has three components.  Every
minimal raw ECO Hamilton endpoint misses the same three upper and three
lower period-three colours, so it is not decorated.  This is compatible
with Theorem 2.1: raw topology is the first arrow, not the final endpoint.

The synchronized three-\(C_{10}\) packet repairs a Hamilton endpoint and
exports a joint alternating SDR on the binary-trace forest side.  Separately,
transporting that repair to
the pre-glue state leaves two components and four pointwise owner-aligned
fixed-rotation ECO atoms; toggling either the isolated standard atom
\(D=101100\) or the nonstandard atom \(D=110100\) gives a decorated Hamilton
cycle.  Hence project \(m=5\) verifies both orders:

\[
\begin{array}{c}
\text{glue then repair},\\
\text{repair then glue}.
\end{array}                                           \tag{3.1}
\]

The first order uses less recursive state for the central theorem.

## 4. Exact quantifier simplification

Let \(F_0,F_*\) be any two spanning 2-factors of the middle-levels graph.
Colour

\[
 F_0\setminus F_*\quad\hbox{red},\qquad
 F_*\setminus F_0\quad\hbox{blue}.                 \tag{4.1}
\]

At every vertex the red and blue degrees agree.  Pairing unlike half-edges
at each vertex decomposes \(F_0\mathbin\triangle F_*\) into edge-disjoint
closed alternating circuits.  Toggling them successively keeps degree two
and ends at \(F_*\).  No factor in the packet need be connected.

Consequently

\[
 \boxed{
 \begin{array}{c}
 \text{a two-factor repair from }F_0\text{ to an accepting}\\
 \text{componentwise forest-decorated 2-factor exists}
 \end{array}
 \iff
 \begin{array}{c}
 \text{some accepting componentwise decorated 2-factor}\\
 \text{exists in the same middle-levels graph.}
 \end{array}}                                             \tag{4.2}
\]

Thus a raw disjoint ECO incidence hypertree is one optional way to produce
\(F_0\), but it is not a separate central existential gate.  The canonical
MMM factor, or ordinary Middle Levels Hamiltonicity, already supplies a
starting 2-factor.  The weakest missing statement in this trace route is:

> **Decorated Middle Levels 2-Factor Theorem.**  For every \(m\ge2\),
> \({\rm ML}(2m-1)\) has a spanning 2-factor with globally bijective upper
> and lower turn representatives and componentwise alternating marks, such
> that every marked component contains an unmarked occurrence and is off
> the binary cycle face.

If one insists on a canonical raw-ECO construction, an all-\(m\) disjoint
strict incidence hypertree remains an optional stronger Stage-A construction
theorem; once an accepting terminal factor exists, however, the repair packet
exists from every Stage-A factor by (4.2).  A prescribed short packet,
component merging, or a packet whose every prefix is Hamilton is a stronger
algorithmic normal form, not a new existence condition.

The decorated-2-factor theorem would prove Catalan Linear Matching in this
route.  It would not prove \(\nu(k)=B(k)\): strict residence, every deeper
shadow, protected opening/socket/voltage data and one correlated lower
common-cap compiler relation remain downstream RSB rows.

## 5. Relation to the transparent recursive route

The transparent-hexagon architecture is a stronger sufficient induction.
It starts with one componentwise joint decoration and preserves the same
selected occurrences through an ordered gluing tree.  At every hexagon the
exact local conditions are:

1. the selected local turn-colour multisets agree before and after,
   separately on the two shores; and
2. after reconnection, the retained-fragment boundary mark types alternate.

A protected trace breaker, or an exact test excluding the unique binary
cycle face, is still required for linearity.  In a multi-component factor a
wholly marked component must also be forbidden.  Carrying a leaf-peelable
decoration additionally requires the delete--contract--insert attachment
multigraph of the changed gap edges to be loopless and acyclic.

This route proves a Hamilton special case of the terminal object needed in
(4.2), but its fixed-owner,
gap-transfer and private-router data are not necessary hypotheses of the
minimal existential theorem.  Conversely, terminal existence does not
provide a transparent gluing tree or any prefix-safe downstream state.
The exact \(m=4\) census makes the distinction literal: among 31 alternating
hexagons, 16 give Hamilton outputs, 10 outputs are decorable, and only 6
admit a common forest decoration across the toggle.

Accordingly there are two live proof targets.  The minimal lane may prove
the Decorated Middle Levels 2-Factor Theorem directly, without component
merging.  The stronger recursive lane may propagate the exact relation of
joint decorations through transparent hexagons and prove that its root has
an accepting state.  Per-shore rainbows carried separately do not suffice in
either lane.

## 6. Dependencies and scope

The exact inputs are:

* MATH_THEOREM_CATALAN_ECO_COMPATIBLE_HYPERTREE_PRIVATE_COLLAR_20260731.md;
* MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md;
* MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md;
* MATH_THEOREM_CATALAN_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION_20260731.md;
* MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md;
* MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md;
* MATH_THEOREM_CATALAN_POSTGLUE_REPAIR_AND_PERIOD3_SUPPORT_GATE_20260731.md;
* MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md.

The theorem is an implication and a quantifier reduction, not an existence
proof for the decorated endpoint.  Equation (4.2) does assert an unrestricted
two-factor repair from any starting factor once such an endpoint exists; it
does not assert a short, Hamilton-safe or downstream-state-
preserving repair.  No contiguous-OR equality theorem is claimed.
