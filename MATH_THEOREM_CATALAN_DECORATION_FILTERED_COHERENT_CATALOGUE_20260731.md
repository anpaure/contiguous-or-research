# Decoration-filtered coherent catalogues and router-resilient gluing

Date: 2026-07-31  
Status: exact conditional theorem on the prepared `H0`--`H5` all-six face;
exact `m=3,4` scope separation; no all-`m` catalogue construction

## 0. Verdict

The post-repair transparent-gluing problem has one exact quantifier order.
Choose a joint alternating decoration first, retain the coherent labels whose
six ports it marks and which genuinely merge current factor components, and
then test router resilience on that decoration-filtered multigraph.

For a decoration `D`, let `K_D` be this multigraph and, for a router deletion
set `Y`, let `(K_D)_Y` retain the labels whose occurrence sources still reach
the sink bank in `N-Y`.  Under the full prepared `H0`--`H5` hypotheses of
items 2189 and 2192, an ordered fixed-`D` transparent component-spanning list
exists exactly when some forced-port-Hall decoration `D` satisfies

\[
                \boxed{c((K_D)_Y)\le |Y|+1
                       \quad\hbox{for every }Y.}       \tag{0.1}
\]

This is the exact central catalogue theorem on the all-six coherent face.
It is not enough to find one decoration passing Hall and a different set of
edges passing router resilience.

Physical move type remains a separate literal field.  The repaired `ML(7)`
cycle has six shared-decoration transparent rows, but all six are
Hamilton-to-Hamilton rethreads.  Four are all-six coherent and two mark none
of the hexagon ports.  All 15 component-splitting toggles have zero common
componentwise decoration.  Hence this fixture calibrates transparency but
does not supply a coherent component-merge edge.  Item 2171 supplies a
separate positive `m=4` merge fixture; the two certificates must not be
identified.

Finally, coherence preserves the physical port multiplicity but not the
occurrence-labelled endpoint pairing.  The gain--Brauer transition and the
terminal one-cycle/primitive-voltage connector test remain downstream of
(0.1).

## 1. Prepared catalogue

Fix a post-router factor `F` with component set `V`, a fixed unit-capacity
linkage network `N` with sink bank `Z` after the standard vertex splitting,
and the prefix-closed, private/aligned gap and reachability hypotheses of
item 2189.  A catalogue label `t` records:

1. an alternating incidence hexagon `Z_t=(H_t;a_t,b_t,c_t)`;
2. its six named occurrence ports;
3. the three external insertion labels on the lower ports and the three
   external deletion labels on the upper ports;
4. its literal effect on the current factor-component partition;
5. one occurrence source `s_t` in `N`; and
6. the full protected gap, trace and physical boundary signature required by
   the prepared face.

Call `t` **coherent** when, in every permitted prefix context,

\[
 d_a=d_b=d_c,
 \qquad e_{ab}=e_{bc}=e_{ca}.                         \tag{1.1}
\]

On a private/disjoint prepared catalogue the external labels are unchanged,
so this reduces to one static test.  On the all-six face, (1.1) is necessary and sufficient for local
fixed-decoration palette transparency.  Boundary mark alternation is then
automatic.  Its forced owner triples are

\[
 H+d+\{ab,bc,ca\},
 \qquad (H-e)+\{a,b,c\}.                              \tag{1.2}
\]

A label is a **merge label** only when it has one fixed nonloop edge
\(\kappa_t=u_tv_t\) on the initial component set `V`.  For every
graphic-independent prefix `U`, the actual components must be exactly the
blocks of

\[
                    (V,\{\kappa_t:t\in U\}).          \tag{1.3}
\]

Thus `U+t` merges precisely the two current blocks containing `u_t,v_t`
when it remains graphic-independent.  This component-faithful Boolean
superposition is `H2`, not a consequence of a root-only move-type tag.  A
Hamilton rethread is a loop in this coordinate; a root-direction split is
outside the merge catalogue.  Coherence and move type are independent tests.

## 2. Decoration filter

Write `Dec(F)` for all joint alternating Catalan decorations of the prepared
factor, componentwise.  The following factor version makes the quantifier
over this family explicit.

### Lemma 2.1 (aggregate forced-port gap Hall)

Let `P_A,P_B` be prescribed upper- and lower-shore occurrence ports on a
middle-levels factor.  They extend to one componentwise joint decoration if
and only if all of the following hold.

1. The forced upper colours are distinct, and the forced lower colours are
   distinct.
2. There is a global upper-colour transversal \(I\supseteq P_A\).  On each
   component containing `I`-marks, form the cyclic gaps between consecutive
   `I`-marks.  Every such gap contains at most one point of `P_B`.
3. A component with no `I`-mark contains no forced lower port.  After
   deleting every forced gap and its forced lower colour, the disjoint union
   of the remaining gap--lower-colour incidence graphs has a perfect
   matching.

A wholly unmarked factor component has no selected turn occurrence; one of
its two residual alternating cross-edge matching phases is merely stored.  In
particular, it contributes no fictitious gap or lower representative.

#### Proof

Necessity is componentwise alternation.  On a marked component, consecutive
selected upper occurrences delimit cyclic gaps, and exactly one selected
lower occurrence lies in each gap.  Thus forced lower occurrences occupy
different gaps, both forced palettes are injective, and the unforced lower
occurrences give the stated aggregate residual matching.  An unmarked
component contains no selected lower occurrence.

Conversely, select the forced lower occurrence in every forced gap and an
occurrence of the matched residual colour in every other gap.  Every marked
component now alternates cyclically, the two selected palettes are globally
bijective, and unmarked components are vacuous.  Storing their residual
cross-edge phase completes the factor state.  This is exactly the one-cycle
proof applied to the disjoint union of induced gaps.  \(\square\)

The existential choice of `I` is essential.  One may not check forced-port
Hall against an independently frozen upper transversal unless that
transversal is part of the construction.

For `D in Dec(F)`, define

\[
 \mathcal C_D={t:t\text{ is a coherent merge label and all six ports of }t
                  \text{ lie in }D\}.                \tag{2.1}
\]

Let `K_D` have vertex set `V` and the effective component edge \(\kappa_t\) of every
label in `C_D`.  Parallel labels remain distinct because they have different
router sources or literal resources.  For `Y subseteq V(N)`, put

\[
 \mathcal C_{D,Y}={t\in\mathcal C_D:s_t\leadsto Z\text{ in }N-Y\},
 \qquad (K_D)_Y=(V,\{\kappa_t:t\in{cal C}_{D,Y}\}). \tag{2.2}
\]

## 3. Exact catalogue theorem

### Theorem 3.1

Assume that, on every decoration-filtered ground set below, the whole
catalogue satisfies `H0`--`H5` of the ordered fixed-decoration theorem.  In
particular, it has the component-faithful fixed edges (1.3), one fixed router,
private/aligned gap superposition, and redundant reachability at every
common-independent prefix.  Then the following are equivalent.

1. There are `D in Dec(F)`, a set `S subseteq C_D`, and an ordering of `S`
   such that `{kappa_t:t in S}` is a spanning tree and `{s_t:t in S}` is
   independent in the fixed occurrence-linkage gammoid.
2. There is `D in Dec(F)`, certified by the aggregate forced-port gap--Hall
   criterion of Lemma 2.1, such that (0.1) holds for `K_D`.

#### Proof

Suppose 1 holds.  By its explicit `S subseteq C_D` hypothesis, `S` is a
spanning tree independent in the fixed linkage gammoid.  Consequently `K_D` contains
a common graphic--gammoid spanning tree.  The router-resilience theorem is
an if-and-only-if statement, so (0.1) follows.  The selected decoration gives
the upper transversal and residual Hall matching.

Conversely, forced-port Hall constructs the literal decoration `D`.
Equation (1.1) makes every label in `C_D` fixed-`D` transparent, with no
additional local palette search.  By router resilience, (0.1) supplies a
spanning tree of `K_D` independent in the occurrence-linkage gammoid.  Item
2189 makes every ordering of that tree executable on the prepared face: each
prefix joins two actual components, preserves `D`, keeps the private/aligned
gap graph leaf-peelable, restricts the common linkage, and preserves the
declared trace and reachability guards.  This is 1.  Moreover, the same
`H0`--`H5` theorem shows that **every ordering of every common spanning tree**
`S subseteq C_D` is executable.  \(\square\)

The theorem is exact only because the same `D` both filters `K_D` and is
carried through the selected tree.  Separate existential projections need
not recombine.

Equivalently, for a coherent merge-label set `U`, let `FPH_F(U)` mean that
the union of its forced ports passes Lemma 2.1, and let `RR_N(U)` mean that
its component multigraph obeys the router-resilience inequalities.  Then
the theorem says

\[
 \exists\text{ executable prepared list}
 \quad\Longleftrightarrow\quad
 \exists U\ \bigl(FPH_F(U)\wedge RR_N(U)\bigr),      \tag{3.1}
\]

with the **same support `U`** in both predicates.  Separate witnesses for
the two existential statements are not enough.

### Corollary 3.2 (catalogue-wide sufficient form)

Suppose the union of the six ports of every coherent merge label in a
catalogue extends to one joint decoration `D` by forced-port Hall.  If the
whole resulting component multigraph obeys (0.1), then a fixed-`D`
transparent component-spanning list exists.

Indeed, the decoded `D` itself witnesses every selected subset.  If a port
is no longer declared forced, its occurrence remains selected in `D`; in a
residual-gap description one simply treats its previously forced gap as an
ordinary matched gap.  No independent rematching or restriction argument is
needed.

This stronger form exposes the constructive three-row target:

1. supply enough coherent **merge** edges;
2. extend all prescribed ports by one residual gap--Hall matching; and
3. prove router resilience after every deletion set `Y`.

### 3.3 Exact integral master and separation rows

The theorem has a fail-closed finite encoding.  Let `alpha_p,beta_p` be the
upper and lower occurrence marks of one literal joint decoration.  Encode
the componentwise cyclic alternation directly, or, after fixing the upper
marks, use the aggregate residual gap matching of Lemma 2.1.  For every
coherent binary merge atom `t`, introduce its exact availability bit

\[
 a_t=\bigwedge_{p\in P(t)} d_p,
 \qquad d_p\in\{\alpha_p,\beta_p\},                 \tag{3.2}
\]

with the six-port linearization

\[
 a_t\le d_p\ (p\in P(t)),\qquad
 a_t\ge\sum_{p\in P(t)}d_p-5.                      \tag{3.3}
\]

For every unit-capacity router deletion set `Y` and every `p`-block
partition `Pi` of the current factor components, impose, when the right side
is positive,

\[
 \sum_{\substack{t:\ s_t\leadsto Z\text{ in }N-Y\\
                  \kappa_t\in\delta_K(\Pi)}} a_t
       \ge p-|Y|-1.                                 \tag{3.4}
\]

These rows are exact: for a fixed decoration their left side is the number
of surviving edges of `(K_D)_Y` crossing `Pi`, and the graph partition
lemma reduces all of (3.4) precisely to
`c((K_D)_Y)<=|Y|+1`.  A violated row is returned by the common
graphic--gammoid basis/min-cut separator.  The router convention includes
all unit-capacity split vertices needed to model source and sink capacities;
with nonunit capacities replace `|Y|` by their total capacity `kappa(Y)`.

No `RET` or `SPLIT` atom enters these sums.  A binary `MERGE` has component
change `-1` and contributes one nonloop graphic edge.  A rethread has change
zero; a splitter has positive component change; a move merging more than
two components lies outside this one-edge graphic theorem.

The exact catalogue score is therefore

\[
 \Delta_{\rm cat}(F)=
   \min_{D\in\operatorname{Dec}(F)}
   \max_{Y\subseteq V(N)}
      \bigl(c((K_D)_Y)-\kappa(Y)-1\bigr).            \tag{3.5}
\]

The prepared catalogue closes exactly when
`Delta_cat(F)<=0`.  This is a nested integral optimization; no interchange
of the minimum and maximum is asserted.

## 4. Why the three rows cannot be projected apart

Forced-port compatibility is collective.  Two coherent component edges may
each extend separately while their two forced lower ports lie in the same
gap of every containing upper transversal.  Then each singleton passes but
their union fails before residual matching.  Thus one cannot first select a
router-resilient tree and later combine independently chosen decorations.

Router compatibility is also collective.  On three components, a triangle
of coherent edges is connected, but if all three occurrence sources use one
unit router vertex `v`, then deleting `v` leaves three isolated components:

\[
                    c((K_D)_{\{v\}})=3>2.             \tag{4.1}
\]

This is the smallest router-resilience obstruction.

Finally, coherence alone says nothing about component progress.  A catalogue
of coherent rethreads contributes only loops to the component multigraph.
For more than one starting component, (0.1) already fails at `Y=emptyset`.

## 5. Exact `m=3,4` scope

The frozen repaired `ML(7)` cycle has 31 alternating incidence hexagons.  Of
the 16 Hamilton outputs, six have a nonempty common-decoration fibre.  All
six are rethreads: component count remains one.  Four mark all six ports and
have coherent label pairs

\[
                 (d,e)=(5,1),(6,5),(2,1),(3,6).       \tag{5.1}
\]

The other two mark zero hexagon ports for their common decorations.  They are
transparent but do not belong to the all-six coherent catalogue of Theorem
3.1.

The same source cycle has 15 component-splitting toggles.  Exhaustive replay
over all 1,728 source decorations finds zero common componentwise decoration
for every one; failure is already at the two palette bijections.  This does
not rule out redecorating the split output or a different source factor.

At `m=3`, all five splitting hexagons have exactly 12 common componentwise
decorations.  Separately, item 2171's standard `m=4` factor begins with
component lengths 28 and 42.  Its literal toggle has ports
`[19,21,23,25,27,29]`, common external labels `(d,e)=(6,0)`, and produces
one component of length 70.  Thus it is a coherent binary `MERGE` on its own
prepared factor.  It is not a logical consequence of the six repaired-cycle
rethreads.

## 6. Gain--Brauer sockets and voltage remain downstream

All-six fixed-decoration transparency preserves the physical degree and port
multiset at the six touched vertices.  It does not fix the pairing of named
ports through path fragments.  If `P_i` is the gain-labelled path involution
after step `i`, then on one named boundary and in one gauge the exact
transition is

\[
 T_i=P_iP_{i-1}^{-1},\qquad
 T_r\cdots T_1=P_rP_0^{-1}.                          \tag{6.1}
\]

When the named boundary changes, compose instead by gain--Brauer stacking.
Carry the sealed-cycle ledger throughout and reject every proper nonroot
sealed cycle.  At the root, the selected connector orbits must be literal,
distinct, disjoint from the forest, injectively developed, use every formal
port once, make `MP_final` one occurrence cycle, respect the connector
capacities, and have closed voltage `V` with `gcd(h,V)=1`.  Only the voltage
row is vacuous when `h=1`.

Therefore (0.1) closes component selection and ordering, not physical socket
closure.  A coherent rethread may change `P_i` without changing component
count; a merge may reduce factor components without providing a terminal
connector cycle.  Neither certificate may be substituted for the other.

## 7. Scope and remaining supply theorem

The exact all-`m` target on this face is now:

> construct a repaired entrance and a Hall-feasible decoration whose
> coherent **merge-edge** catalogue is router-resilient, then carry the
> resulting gain--Brauer, residence, deep-shadow and compiler state through
> the ordered transparent list.

This note does not construct such a catalogue.  It proves no all-`m`
decoration, residence redistribution, socket/voltage closure, compiler or
coefficient-one theorem.  Its purpose is to fix the central quantifiers and
prevent rethread witnesses from being promoted as merge edges.

## 8. Exact audit and dependencies

The lightweight audit
`scratch/threadD_audit_item2192_catalogue_jointness_20260731.py` replays the
item-2171 merge `(28,42)->70`, derives `(d,e)=(6,0)` from its literal
external neighbours, and verifies a three-edge reduced-row counterexample in
which router resilience and forced-port Hall each have a spanning-tree
witness but no common spanning-tree witness.  Its frozen JSON is
`scratch/threadD_item2192_catalogue_jointness_20260731.audit.json`; semantic
replay is exact.  The counterexample is deliberately abstract and is not a
physical middle-levels no-go.

The proof depends on the following frozen exact inputs:

* `MATH_THEOREM_CATALAN_TRANSPARENT_ROUTER_RESILIENCE_CRITERION_20260731.md`;
* `MATH_THEOREM_CATALAN_COHERENT_ALLSIX_TRANSPARENT_HEX_20260731.md`;
* `MATH_THEOREM_CATALAN_FORCED_PORT_GAP_HALL_20260731.md`;
* `MATH_THEOREM_CATALAN_ORDERED_FIXED_D_TRANSPARENT_GLUING_AFTER_ROUTER_20260731.md`;
* `scratch/audit_catalan_ml7_component_toggle_scope_20260731.py`.

The prepared assumptions are load-bearing.  The resilience formula uses a
fixed unit-capacity router and named sources; coherence is only the all-six
local face; and executable ordering additionally needs the private/aligned
gap, component-faithful, trace, and redundant-reachability hypotheses of the
ordered fixed-decoration theorem.
