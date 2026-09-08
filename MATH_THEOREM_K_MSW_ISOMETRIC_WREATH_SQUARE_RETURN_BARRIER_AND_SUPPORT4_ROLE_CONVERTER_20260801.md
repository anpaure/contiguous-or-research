# MSW isometric-wreath square-return barrier and the support-four role-converter gate

**Date:** 2026-08-01  
**Lane:** K, nonlocal reset commutators / Catalan hierarchy  
**Status:** exact native no-go, exact support-four minimality on the clean
path-reversal face, exact edit-stability bound, and exact central packing and
functional-Rado criteria.  The independently audited `4d+2` complete-reversal
rail supplies one local resident/all-depth expansion.  No positive-density
planted bank or cycle-fusion bank inside one MSW factor is claimed.

## 0. Verdict

The open Johnson square is the minimum clean central role converter, but it
is **not native** to the canonical MSW/Catalan wreath hierarchy.

More precisely:

1. Every MSW wreath, for every cyclic omitted-label order, has an
   every-second Johnson cycle which is isometric.  A three-edge subpath has
   endpoints at Johnson distance three (distance two in the exceptional
   `m=2` cycle), never distance one.  Hence it cannot be the open side of
   a Johnson square.
2. Coordinate relabelling, changing the cyclic omitted-label order, and
   replacing whole wreaths by whole wreaths preserve this obstruction.
   Thus the Catalan-sized size-two exchange cube consists of factor-space
   squares, not physical three-edge Johnson-square returns.
3. If a degree-two owner graph is obtained from a wreath factor by inserting
   `J` new Johnson edges, it contains at most `3J` unoriented (at most
   `6J` oriented) three-edge square-return paths.  Consequently a
   positive-density bank of literal role converters requires a linear
   number of non-wreath interior rethreads.  Conjugation alone cannot supply
   it.
4. This is a fixed-factor obstruction, not a scarcity theorem for the
   Boolean lattice.  The full coordinate-conjugacy orbit of one clean open
   square contains a complete-footprint-disjoint subfamily of size at least
   
   \[
       {1\over48}\binom{2m+1}{m-1}
       =\left({1\over48}+o(1)\right)\binom{2m+1}{m}.
   \]

   These are abstract/planted candidates.  Their old phases do not occur as
   consecutive paths in one canonical wreath factor.  The packing must move
   the seam: any orbit fixing one physical lower or upper seam resource has
   complete-footprint matching number one.
5. For a planted square, central compatibility with the functional
   head-owner bijection is exact: the square closes the reset attachment
   path and its two predecessor paths.  Common high-target rounding follows
   from the previously proved contracted Rado inequalities only when the
   two complete reset-plus-square contractions have the same residual
   occurrence network.  Footprint disjointness alone does not imply this.
6. The local residence objection is no longer open: the complete-reversal
   return rail expands one converter to `4d+2` roots and preserves every
   internal derivative and cyclic OR deck for
   `r,k-r >= 2d+1`.  This is an `O(d)`-edge path whose complete chronology
   is non-wreath; the theorem does not assert that every individual rail
   edge was absent from a chosen baseline.  It does not plant a bank in a
   fixed MSW factor or protect exterior windows.

Thus support four is the first possible clean nonlocal role-conversion
packet after leaving the wreath category.  The exact remaining positive
theorem is a **linear non-wreath planting plus combined resource/component
matching theorem**, followed by global exterior-window, common-residual
compiler and regeneration guards.  Residence and all-depth transport
inside one complete-reversal packet are already closed by item 6.

## 1. Every wreath projects to an isometric Johnson cycle

Put

\[
 n=2m+1,\qquad W=\binom n m,\qquad
 B={W\over n}=\operatorname{Cat}_m
\]

and let

\[
                     Q=(q_0,q_1,\ldots,q_{n-1})
\]

be any cyclic ordering of the ground set.  The associated odd-graph wreath
has vertices

\[
 V_i(Q)=\{q_{i+1},q_{i+3},\ldots,q_{i+2m-1}\},
 \qquad i\in\mathbb Z_n.                                  \tag{1.1}
\]

Consecutive wreath vertices are disjoint.  Every-second vertices are
Johnson adjacent, because

\[
 V_{i+2}(Q)=V_i(Q)-q_{i+1}+q_i.                            \tag{1.2}
\]

Since `2` is invertible modulo `n`, the sequence

\[
       V_i,V_{i+2},V_{i+4},\ldots,V_{i+2(n-1)},V_i         \tag{1.3}
\]

is a Hamilton cycle on the `n` roots of this wreath's Johnson trace.

### Theorem 1.1 (exact wreath metric)

For every \(t\in\mathbb Z_n\),

\[
 \boxed{
 d_J\bigl(V_i(Q),V_{i+2t}(Q)\bigr)=\min\{t,n-t\},
 }
                                                               \tag{1.4}
\]

where `t` is represented in \(\{0,\ldots,n-1\}\).  Hence (1.3) is an
isometric `n`-cycle in \(J(n,m)\).

#### Proof

Read the coordinates in the step-two cyclic order

\[
                         r_j=q_{i+1+2j}.
\]

Then

\[
 V_i=\{r_0,\ldots,r_{m-1}\},\qquad
 V_{i+2t}=\{r_t,\ldots,r_{t+m-1}\},                       \tag{1.5}
\]

with subscripts modulo `2m+1`.  These are two cyclic intervals of length
`m` in a cycle of length `2m+1`.  If
\(s=\min\{t,n-t\}\le m\), their intersection has size `m-s`.
Since \(d_J(A,B)=m-|A\cap B|\) on rank-`m` sets, (1.4) follows.
\(\square\)

### Corollary 1.2 (no native open square)

For \(m\ge3\), every three-edge subpath of (1.3) has endpoints at Johnson
distance three.  For `m=2`, its endpoints have distance two.  In no
dimension does a simple three-edge wreath subpath have adjacent endpoints.
Therefore no MSW wreath contains the retained three-edge path of an open
Johnson \(C_4\).

This conclusion holds for every omitted-label order `Q`, not merely the
canonical order.  It is consequently invariant under every coordinate
conjugation and under every operation which replaces complete wreaths by
complete wreaths.

The scope of the last sentence matters.  A genuinely non-wreath
edge-level splice is outside the conclusion; that is precisely the live
escape.

## 2. Factor-space squares are not owner-path squares

Let \(\mathfrak W_m\) denote the class of exact factors which are disjoint
unions of complete wreaths.  The canonical MSW factor and every factor
obtained from it by the standard whole-wreath Catalan component choices
belong to \(\mathfrak W_m\).

### Theorem 2.1 (hierarchy closure obstruction)

No member of \(\mathfrak W_m\) contains a native open support-four Johnson
square return in its every-second owner chronology.

In particular, the \(\operatorname{Cat}_{m-2}\) independent size-two
transposition components of the canonical MSW exchange cube do not supply
\(\operatorname{Cat}_{m-2}\) open square role converters.  Their square
structure lives in the **factor exchange/shadow lattice**: a component
choice replaces whole wreaths.  On either shore, every individual physical
row still obeys Theorem 1.1.

#### Proof

Every connected row of a factor in \(\mathfrak W_m\) is (1.3) for some
cyclic order `Q`.  Corollary 1.2 excludes the required path in each row.
Rows are vertex-disjoint, so a connected three-edge path cannot use edges
from two rows.  The statement about the exchange cube follows because its
size-two moves replace two complete old wreaths by two complete new
wreaths. \(\square\)

Thus a Petr--Turek/Pluecker square in a lower-shadow action table must not
be identified with a literal square in the owner chronology.  The former
can be present while the latter is forbidden by (1.4).

Likewise, the statement that a canonical incidence pull *contracts* to a
square-normal-form rail is only an algebraic/socket statement.  Contraction
forgets the intermediate owner chronology.  A literal expansion to the
three-edge return must introduce at least one non-wreath owner edge by
Theorem 4.1 below; it is not supplied by the contracted pull itself.

Theorem 2.1 does not refute a closed support-four `C8`/`q=4` matching
switch which takes old edges from several different wreaths.  Such a
packet is not a three-edge path in one wreath and has a different projection
signature.  The present obstruction is specifically to using an open
square path reversal as the reset role converter.

## 3. Support four is the exact clean minimum

Let adjacent rank-`m` seam roots be

\[
                         E=L+x,\qquad F=L+y,                 \tag{3.1}
\]

where \(|L|=m-1\).  A clean orientation-flip return is a simple Johnson
path from `E` to `F` whose edge intersections and unions are separately
injective and whose two orientations are used in different phases.

### Lemma 3.1 (common-neighbour dichotomy)

Every common Johnson neighbour \(C\notin\{E,F\}\) is of exactly one of the
forms

\[
 C=L+z\quad(z\notin L+x+y),                              \tag{3.2}
\]

or

\[
 C=L-p+x+y\quad(p\in L).                                \tag{3.3}
\]

In case (3.2), the two detour edges `EC,CF` have the same lower colour
`L`.  In case (3.3), they have the same upper colour `L+x+y`.

#### Proof

A common neighbour differs from both adjacent sets `L+x,L+y` in one
deletion and one insertion.  Either it retains all of `L`, forcing
(3.2), or it contains both `x,y`, forcing (3.3).  The displayed
intersection/union repetitions are immediate. \(\square\)

### Theorem 3.2 (clean role-converter minimum)

A clean open path-reversal role converter on one adjacent seam has support
at least four roots.  Equality is attained by choosing \(p\in L\) and
\(z\notin L+x+y\) and taking

\[
 E=L+x,\quad E'=L-p+x+z,\quad
 F'=L-p+y+z,\quad F=L+y.                               \tag{3.4}
\]

The three-edge path `E,E',F',F`, with the seam `EF` omitted in both
phases, has three distinct lower colours and three distinct upper colours.
Its two orientations have exactly one head-owner alternating return and two
predecessor-parity returns.

#### Proof

Support two is the pair of opposite seam orientations, the forbidden
owner-repeating closed doubleton.  Support three is a two-edge detour and
fails one palette by Lemma 3.1.  Direct calculation in (3.4) gives the
three lower colours

\[
 L-p+x,quad L-p+z,quad L-p+y
\]

and the three upper colours

\[
 L+x+z,quad L-p+x+y+z,quad L+y+z,
\]

all distinct.  The projection calculation is the open-\(C_4\)
three-return identity. \(\square\)

There is a second, independent support-three barrier in the canonical
Catalan menu.  Matching-closed Boolean-hex toggles have even attachment
and even predecessor sign, whereas the closed reset phase difference has
sign `(-1,+1)`.  Therefore the ternary hex can fuse three selected cycles
but cannot serve as the closed reset role converter.  Theorem 3.2 is not a
classification of every imaginable support-three non-Cartesian open macro;
it is exact for clean path reversal, while the parity statement closes the
matching-closed hex face.

## 4. A sharp edge-rethreading barrier

Let \(G_0\) be the every-second owner graph of a wreath factor, regarded as
an undirected two-factor.  Let `G` be any graph of maximum degree at most
two on the same roots, and put

\[
                         J=|E(G)\setminus E(G_0)|.           \tag{4.1}
\]

Let \({\cal R}_3(G)\) be the set of unoriented simple three-edge paths of
`G` whose endpoints are Johnson adjacent.  Clean open squares form a
subset of \({\cal R}_3(G)\).

### Theorem 4.1 (three-window charging)

\[
                         |{\cal R}_3(G)|\le3J.              \tag{4.2}
\]

There are at most `6J` oriented occurrences.  In particular, a
resource-disjoint bank of `h` open support-four returns requires

\[
                         J\ge h/3.                           \tag{4.3}
\]

#### Proof

If all three edges of a member of \({\cal R}_3(G)\) belonged to \(G_0\),
they would be three consecutive edges of one wreath cycle.  Corollary 1.2
would make its endpoints nonadjacent.  Thus every return path contains a
new edge from (4.1).

In a maximum-degree-two graph, a fixed edge lies in at most three
unoriented three-edge paths: once as the middle edge and once in each end
position.  Charge every return path to one of its new edges.  This proves
(4.2); orientation doubles the bound. \(\square\)

Consequently `o(W)` new owner edges cannot create a positive-density
\(\Theta(W)\) square bank.  More generally, \(\Theta(B)\) converters, where
\(B=\operatorname{Cat}_m=W/(2m+1)\), already require \(\Omega(B)\) genuine
new edges relative to the chosen native baseline.  The stronger Section 2
statement says that replacing whole wreaths still creates **zero** returns,
even when its ordinary edge distance from that baseline is large: the
useful edits must leave the wreath category in the final graph.

The theorem is indifferent to how the new edges were generated.  It
therefore applies to serial conjugations, bounded commutators and
row-preserving hierarchy switches after their final owner graph is
reconstructed.  It does not rule
out a deliberately linear-scale nonlocal braid.

The audited complete-reversal return rail is consistent with this bound.
It does not locate the forbidden three-edge path inside a wreath; it
replaces the seam by an explicit `O(d)`-edge non-wreath return and makes the
two complete phases opposite orientations of the resulting `4d+2`-cycle.
Theorem 4.1 therefore diagnoses why that collar must be planted rather than
recovered post hoc from a native wreath.

## 5. The complete Boolean orbit has linear collision-free supply

The absence in Section 2 is not caused by unavoidable set-resource
collisions.  Continue with `n=2m+1`.  Let \({\cal S}_m\) be the full
coordinate-conjugacy orbit of the oriented square (3.4), parametrized by

\[
 |L|=m-1,quad p\in L,quad x,y,z\notin L
 \text{ pairwise distinct}.                              \tag{5.1}
\]

Give a square its **central complete footprint** consisting of

* its four rank-`m` roots;
* its three retained lower colours and the omitted seam lower colour (L);
* its three retained upper colours and the omitted seam upper colour
  `L+x+y`.

Thus every footprint has four resources in each of the three rank layers.

### Proposition 5.0 (fixed-seam collision)

Any complete-footprint-disjoint family whose members all use the same
lower seam `L` has size at most one.  The same holds if they all use the
same upper seam, and a fortiori if they have the same endpoint pair
`E,F`.

Thus a fixed-base/stabilizer orbit cannot give a bank merely by varying
`p,z` or the active orientation.  A positive-density construction must
move the physical seam resources as well as the active labels.  This is
why the next theorem uses the full coordinate orbit, not one fixed-core
menu.

### Theorem 5.1 (linear abstract square packing)

The footprint hypergraph of \({\cal S}_m\) has a matching of size at least

\[
 \boxed{
 {1\over48}\binom{2m+1}{m-1}
 }
 =\left({1\over48}+o(1)\right)\binom{2m+1}{m}.            \tag{5.2}
\]

Hence all root, lower, upper and omitted-seam set resources can be made
pairwise disjoint on a positive-density abstract bank.

#### Proof

Let \(P=|{\cal S}_m|\).  By transitivity, a fixed resource in ranks
`m-1,m,m+1` lies respectively in

\[
 {4P\over\binom n{m-1}},\qquad
 {4P\over\binom n m},\qquad
 {4P\over\binom n{m+1}}                                \tag{5.3}
\]

footprints.  Since

\[
 \binom n{m+1}=\binom n m,qquad
 \binom n{m-1}={m\over m+2}\binom n m,                  \tag{5.4}
\]

the maximum resource degree is

\[
                         \Delta={4P\over\binom n{m-1}}.  \tag{5.5}
\]

A greedy choice of one footprint deletes at most \(12\Delta\) candidates.
It therefore chooses at least \(P/(12\Delta)\), which is (5.2).
\(\square\)

Theorem 5.1 is deliberately central.  It does not choose occurrence flags,
place the old path edges in one selected factor, preserve residence or
deep shadows, or provide compiler sinks.  Its role is to locate the exact
obstruction: raw Boolean conjugates are plentiful and can avoid fixed
set-resource collisions, but they are spread across conjugate factors.
Conjugating `(F,Q)` gives `(gF,gQ)`; it does not install `gQ` in the
original `F`.

## 6. Exact topology and functional-selection interface

Let `M` be a selected occurrence-labelled factor/table state.  A
**guarded square candidate** records:

1. one clean square (3.4), with both phase paths literal in the respective
   occurrence atlases;
2. the opened reset segment to which its endpoints are attached;
3. its complete physical resource, flag, witness, residence and compiler
   footprint; and
4. the current directed components touched by all old atoms.

Make the combined conflict hypergraph \({\cal H}_{\square}(M)\) whose
vertices are the complete physical resources and current component slots,
and whose hyperedges are guarded square candidates.  Component slots are
included with the multiplicity required by the desired cut-and-join mode.

### Proposition 6.1 (exact simultaneous-fusion criterion)

A family of guarded squares is simultaneously collision-free and
component-disjoint exactly when its hyperedges form a matching in
\({\cal H}_{\square}(M)\).  If a closed `q=4` packet is used and its four
old edges lie on four distinct directed cycles, its toggle fuses those four
cycles into one.  For the opened-reset use, the topology is instead the
literal cut-and-join determined by the recorded reset segment; no cycle
gain follows from the square palette alone.

This is a finite necessary-and-sufficient formulation, not an expansion
theorem.  The matching in Theorem 5.1 is only the projection of
\({\cal H}_{\square}(M)\) onto its central set resources.

Now fix a high-target flag table and a functional head-owner bijection
\(\theta\).  On one planted square, the head-owner symmetric difference is
one alternating path and the predecessor symmetric difference is two
alternating paths.  Joined to the opened reset, all three become alternating
cycles.  Therefore the central attachment and predecessor matchings remain
bijections; for a footprint-disjoint bank these cycle toggles commute.
The lower palette is unchanged as a set, but a host which freezes the
occurrence-labelled lower--tail assignment must also carry the square's
additional lower--tail alternating path in the guarded footprint.

Let the two complete phase contractions, including reset and square, have
residual occurrence networks \(G^\rightarrow_{\rm res}\) and
\(G^\leftarrow_{\rm res}\).  If they are literally equal to one network
\(G_{\rm res}\), the exact common functional-table gate is the contracted
Rado family

\[
 r_{G_{\rm res}}
 \left(\bigcup_{c\in I}{\cal L}_c\right)\ge |I|
 \qquad\text{for every target set }I.                       \tag{6.1}
\]

Equivalently, in the purely bipartite face, every target subset has at
least its cardinality of reachable residual owners.  Under (6.1), one
common residual basis extends both phase packets; failure of (6.1) gives
the exact Hall/Rado cut obstruction.

The equality of residual networks is essential.  Central palette equality,
pairwise footprint disjointness, or phasewise Hall separately do not imply
it.  This is also why the opposite-seam one-Cartesian-ear pair fails even
though each ear separately has the right marginal gain.

For the complete-reversal `4d+2` collar, the two **internal** occurrence
systems are literal reversals of the same cycle, so the immediate palettes,
all derivative inventories and cyclic OR decks already agree.  In (6.1)
its remaining equality premise is therefore exterior: the planted cut
occurrences, high-target lists, guards and compiler cells must induce the
same contracted residual network.  The local collar theorem does not prove
that exterior equality or provide a large family of compatible cuts.

## 7. Exact surviving construction target

The q-gon and open-square theorems now separate four layers cleanly.

1. **Permutation algebra:** the reflected reverse and forward q-gons have
   the reset signature, but same-port composition is a closed doubleton.
2. **Minimal role conversion:** the open support-four Johnson square removes
   that central doubleton and provides the exact three returns.
3. **Canonical-host obstruction:** every native MSW wreath is isometric, so
   the square does not occur; `h` planted candidates cost at least `h/3`
   new owner edges.
4. **Global selection:** after a non-wreath braid creates candidates, one
   must find a large matching in \({\cal H}_{\square}(M)\), verify the
   intended component cut-and-join, and pass the common residual Rado cut
   (6.1), exterior-window and compiler rows.  The local `4d+2`
   complete-reversal rail may be used to discharge intrinsic residence and
   all-depth packet chronology, but it does not discharge these global
   rows.

Thus support-four path reversal is the exact minimum **after** leaving the
canonical wreath category.  Its full coordinate orbit has positive-density
collision-free central supply, but its conjugates do not generate native
**open-square role-converter** fusion in the canonical MSW/Catalan
hierarchy.  This does not exclude the already separate closed `C8`/`q=4`
fusion trades.  Positive-density fusion through the open-square converter
requires a linear-scale non-wreath rethreading theorem plus the combined
matching condition above.

## 8. Dependencies and scope

This note uses the literal wreath formula and the exact results in:

* `MATH_THEOREM_QGON_PROJECTION_COMPOSITION_AND_CLOSED_DOUBLETONGATE_20260801.md`;
* `MATH_THEOREM_L_OPEN_JOHNSON_C4_RESET_THREE_RETURN_LIFT_AND_ALLDEPTH_GATE_20260801.md`;
* `MATH_THEOREM_K_RAMSEY_HEX_FUNCTIONAL_HOST_AND_RESET_PARITY_GATE_20260801.md`;
* `MATH_THEOREM_K_RESET_CONTRACTED_DUAL_FUNCTIONAL_FLOW_AND_RADO_PHASE_ROUTER_20260801.md`;
* `MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`;
* `MATH_AUDIT_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`;
* `MATH_ATTACK_B_FACTOR_EXCHANGE_EXPANSION_20260725.md`.

No claim is made that an arbitrary MSW component switch is row-preserving,
that the bare central square is automatically resident (its consecutive
private-coordinate run has length two), that the complete-reversal collar
has an exterior-safe positive-density planting, that the complete Boolean
packing is simultaneously applicable to one factor, or that cycle fusion
alone proves the lower compiler or \(\nu(k)=B(k)\).
