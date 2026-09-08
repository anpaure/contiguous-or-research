# Protected plateau transport in the balanced two-extension fibre

Date: 2026-07-31

Status: pure mathematics.  The protected alternating-circuit theorem and
the lower-bounded-circulation criterion below are unconditional.  The
incidence-hexagon obstruction is an explicit construction in the genuine
middle incidence graph (I(5,2)).  No claim is made that the canonical PBBS
witness section satisfies the resulting cut inequalities.

The purpose of this note is to separate three statements which are easy to
conflate.

1. Every two balanced two-extension factors are connected by alternating
   circuits.
2. The same remains true after one fixes the literal incidence support of a
   common bank of all-depth witnesses and residence corridors.
3. The analogous assertion with **incidence hexagons only** is false, even
   in the smallest nontrivial middle incidence graph beyond a hexagon.

The positive theorem gives an exact zero-shadow-defect **balanced-factor
endpoint** criterion: after one chooses the new witnesses to be installed,
a family of Hoffman cut inequalities is necessary and sufficient for one
compound protected switch.  It does not by itself give a connected order,
residence-DFA acceptance, an opening, or a common-\(Q\) compiler.  Thus the
remaining PBBS factor problem is not an unspecified topological connectivity
gate.
It is the concrete problem of selecting a witness section whose forced arcs
fit through every protected exchange cut, with the residence automaton and
the fragment ports included in the state space.

## 1. Balanced factors and literal protected supports

Put

\[
 n=2q+1,
 \qquad
 \mathcal L=\binom{[n]}q,
 \qquad
 \mathcal M=\binom{[n]}{q+1},
\]

and let (G=I(n,q)) be the bipartite inclusion graph between
(\mathcal L) and (\mathcal M).  Both shores have the same cardinality,
and (G) is ((q+1))-regular.

A **balanced factor** is a simple edge set (F\subseteq E(G)) satisfying

\[
                    \deg_F(v)=2\qquad(v\in\mathcal L\cup\mathcal M).
\tag{1.1}
\]

Contracting each (C\in\mathcal L) turns its two selected incidences into
one Johnson edge on (\mathcal M), labelled by (C).  Thus (1.1) is exactly
the balanced two-extension normal form: middle degrees are two and every
lower (q_1) colour occurs once.

An ordered carrier path

\[
 T_0,C_1,T_1,C_2,\ldots,C_s,T_s
\tag{1.2}
\]

has **incidence support**

\[
 \operatorname{supp}(1.2)
 =\{C_iT_{i-1},C_iT_i:1\le i\le s\}.
\tag{1.3}
\]

If another balanced factor contains (1.3), then (1.2), possibly as a
subpath of a longer component, occurs there in the same order or its global
reverse.  In particular every interval intersection or union certified by
(1.2) survives literally.

### Definition 1.1 (protected section)

A protected section in a factor (F) is an edge set (P\subseteq F),
usually the union of supports (1.3) for:

* one selected occurrence of each shadow target which is to be retained;
* selected residence corridors; and
* any immutable port or compiler pins.

The **protected face** is

\[
 \mathfrak F(P)=
 \{F'\subseteq E(G):\deg_{F'}\equiv2, P\subseteq F'\}.
\tag{1.4}
\]

This definition is literal.  Protecting only a target name, rather than the
incidences of one physical occurrence, is not enough.

### Definition 1.2 (hereditary residence certificate)

Fix (d\ge1).  A protected section (P) is a (d)-corridor cover if, for
every coordinate (x\in[n]) and every owner (T\in\mathcal M) containing
(x), the set (P) contains the support of a carrier path through (T)
having at least (d+1) consecutive owners, all containing (x).

This is deliberately stronger than merely naming one long run per
coordinate.

### Lemma 1.3 (what literal protection preserves)

Every (F'\in\mathfrak F(P)) retains every selected interval witness in
(P).  If (P) is a (d)-corridor cover, then every positive coordinate
run of (F') has length at least (d+1).

#### Proof

At every internal vertex of (1.2), its two path incidences already use its
full degree in (F'), so the displayed path cannot be broken or reordered.
This proves the witness assertion.

For residence, take a coordinate (x) and any (x)-owner (T).  The
protected (x)-path through (T) lies inside the maximal (x)-run of
(F') containing (T), and has at least (d+1) owners.  Hence that maximal
run has length at least (d+1).  This holds for every (x)-owner. \(\square\)

The corridor-cover hypothesis can be expensive and can freeze most of a
factor.  It is a sufficient hereditary certificate, not an assertion that
PBBS automatically supplies a sparse one.  The less restrictive endpoint
run-state formulation is treated in Section 7.

## 2. Unconditional protected plateau connectivity

### Theorem 2.1 (protected alternating-circuit connectivity)

Let (F_0,F_1\in\mathfrak F(P)).  Then
(F_0\mathbin\triangle F_1) decomposes into edge-disjoint even circuits
which alternate between (F_0\setminus F_1) and (F_1\setminus F_0).
Toggling these circuits one at a time gives

\[
          F_0=H_0,H_1,\ldots,H_t=F_1,
          \qquad H_i\in\mathfrak F(P).
\tag{2.1}
\]

All selected all-depth witnesses and protected corridors survive at every
intermediate state.  Since (I(n,q)) has no four-cycle, one may take

\[
              t\le |F_0\mathbin\triangle F_1|/6.
\tag{2.2}
\]

#### Proof

Colour (F_0\setminus F_1) red and (F_1\setminus F_0) blue.  At every
vertex the red and blue degrees agree because both full factors have degree
two.  Pair red and blue half-edges at each vertex and follow the pairings.
This partitions the symmetric difference into alternating circuits.

No edge of (P) belongs to the symmetric difference.  Toggling one circuit
therefore removes no protected edge, and removes and adds the same number
of incidences at every visited vertex.  It gives another simple degree-two
factor in (\mathfrak F(P)).  The circuits are edge-disjoint, so they may be
toggled successively.  Lemma 1.3 gives the protected-witness and corridor
claims.  The incidence graph has no (4)-cycle, so every nonempty circuit
has length at least six, proving (2.2). \(\square\)

### Corollary 2.2 (plateau-monotone transport)

Suppose (P) contains one literal witness for every shadow target covered
by (F_0).  Along (2.1), no such target is ever lost.  Consequently the
number of missing targets never exceeds its value at (F_0).  If (F_1)
is zero-defect, (2.1) is a protected plateau path to zero defect.

This is the precise unconditional monotonicity statement.  Targets gained
temporarily but not protected may later disappear, so it does not assert
setwise monotonicity of every incidental gain.

The theorem also identifies the real endpoint gate: one must find a desired
factor (F_1) sharing one suitable protected witness section with (F_0).
Once such an endpoint exists, there is no further alternating-circuit
connectivity obstruction.

## 3. Exact forced-witness insertion by a circulation

The endpoint gate has an exact cut formulation.

Fix (F\in\mathfrak F(P)), and let (Q\subseteq E(G)) be a proposed new
literal witness bank.  Edges in (Q\cap F) must not be removed, so put

\[
                    P'=P\cup(Q\cap F),
       \qquad       A=Q\setminus F.
\tag{3.1}
\]

Construct the **protected exchange digraph** (D=D(F,P')) on
(\mathcal L\cup\mathcal M) as follows:

* orient every unselected incidence (CM\notin F) as (C\to M);
* orient every removable selected incidence (CM\in F\setminus P') as
  (M\to C);
* omit the protected incidences (P').

Thus a directed circuit alternates between incidences to insert and
incidences to remove.

### Theorem 3.1 (exact protected insertion criterion)

There exists a balanced factor (F'\in\mathfrak F(P)) with
(Q\subseteq F') if and only if, for every vertex set
(S\subseteq V(D)),

\[
 \boxed{
 |A\cap\delta_D^+(S)|\le |\delta_D^-(S)|.}
\tag{3.2}
\]

Equivalently, (D) has a binary circulation which uses every arc of (A).
When (3.2) holds, (F') is obtained from (F) by one compound protected
alternating switch and can then be reached circuit by circuit as in
Theorem 2.1.

#### Proof

Give every arc of (D) upper capacity one, give arcs in (A) lower
capacity one, and all other arcs lower capacity zero.  Hoffman's circulation
criterion is

\[
 \ell(\delta^+(S))\le u(\delta^-(S))
             \qquad(S\subseteq V(D)),
\]

which is exactly (3.2).  Integral lower and upper capacities give a binary
circulation.  For completeness, the criterion follows directly by replacing
each lower bound by its forced unit imbalance and applying max-flow/min-cut;
necessity is just equality of flow entering and leaving every set (S).

Let (Z) be the support of such a circulation.  Toggle every underlying
incidence in (Z).  At a lower vertex, outgoing arcs add incidences and
incoming arcs remove incidences; circulation balance preserves degree.
The same statement, with directions reversed, holds at an upper vertex.
No protected edge is removable in (D), every edge of (A) is added, and
every edge of (Q\cap F) lies in (P').  Hence the result is a simple
balanced factor containing (P\cup Q).

Conversely, if (F') exists, orient the incidences of
(F'\setminus F) forward and those of (F\setminus F') backward.  Equal
degrees make this a binary circulation in (D), and it contains every arc
of (A).  Thus (3.2) is necessary. \(\square\)

Singleton sets in (3.2) include every local degree obstruction.  Larger
sets are the genuinely collective protected obstruction; separate
candidate feasibility does not imply their joint feasibility.

### Corollary 3.2 (literal zero-defect criterion)

Let (P) contain one selected witness for every target already covered by
(F), and for each missing target (Z) choose one proposed support (Q_Z).
Put (Q=\bigcup_ZQ_Z).  If (3.2) holds, there is a balanced factor which
retains every old selected witness and contains every (Q_Z).  Hence it has
zero shadow defect.  If (P) is also a (d)-corridor cover, the new factor
remains (d)-resident.

This is an exact zero-defect theorem, conditional only on the displayed,
checkable cut inequalities for the chosen physical witnesses.  It does not
assert connectedness of the contracted factor, a linear opening, or a
common-cap compiler.

### Corollary 3.3 (robust absorber bound)

If (D(F,P')) is (s)-arc-strong in both directions and
(|Q\setminus F|\le s), then (3.2) holds.  More generally, it is enough that

\[
 \min_{\varnothing\ne S\ne V(D)}|\delta_D^-(S)|
       \ge |Q\setminus F|.
\tag{3.3}
\]

Indeed the left side of (3.2) is at most (|Q\setminus F|).  This simple
bound is often too strong because the exchange digraph has small local
degrees; the candidate-specific inequalities (3.2) are the sharp form.

### Corollary 3.4 (duplex make-before-break transport)

Let \(P_{\rm old}\subseteq F\) be an old literal witness section and let
\(P_{\rm new}\) be a proposed replacement section certifying the same target
family.  Apply Theorem 3.1 with

\[
                     P=P_{\rm old},\qquad Q=P_{\rm new}.
\tag{3.4}
\]

If (3.2) holds, there is a balanced factor \(F^\ast\) containing
\(P_{\rm old}\cup P_{\rm new}\).  Transport from \(F\) to \(F^\ast\) while
protecting \(P_{\rm old}\); at \(F^\ast\), declare \(P_{\rm new}\) protected
and release any edges used only by \(P_{\rm old}\).  No target certified by
the two sections is absent at any time.

Thus a sequence of duplex overlaps gives a zero-defect reconfiguration even
when the initial and final protected sections are disjoint.  The exact
obstruction to one handoff is again (3.2), including its singleton degree
cuts.  In particular, “two witnesses per target” is not enough: the two
whole sections must coexist in one degree-two factor.

#### Proof

Theorem 3.1 produces the common factor.  Theorem 2.1 reaches it without
removing \(P_{\rm old}\).  After the handoff, Theorem 2.1 applied with
\(P_{\rm new}\) preserves the replacement section.  At the common state both
sections are present, so releasing the old section creates no uncovered
target. \(\square\)

## 4. A commuting incidence-hexagon absorber

Let (Z) be an (F)-alternating incidence hexagon.  Write

\[
              Z^-=Z\cap F,\qquad Z^+=Z\setminus F.
\tag{4.1}
\]

It is (P)-neutral exactly when (Z^-\cap P=\varnothing).

### Lemma 4.0 (exact local damage of one hexagon)

An alternating incidence hexagon removes exactly three selected incidences
and adds the opposite three.  In the contracted Johnson factor it changes
exactly the three edges labelled by the three lower vertices of the
hexagon, and changes no other labelled edge.  Consequently:

1. a selected interval witness is certainly retained when its incidence
   support avoids (Z^-);
2. every deleted or newly created coordinate-run boundary is incident with
   one of those three changed contracted edges; and
3. the exact residence verdict after the switch is determined by cutting at
   those three old edges and composing the endpoint run-state summaries of
   the resulting segments in their new order.

#### Proof

Each shore of an incidence hexagon has one incidence at each of its three
lower and three owner vertices.  A toggle therefore changes one endpoint of
the contracted edge belonging to each of the three lower vertices and
touches no other lower vertex.  Every other contracted adjacency is literal
and unchanged.  An interval support avoiding the removed incidences remains
selected.  Coordinate traces can change adjacency only at a changed
contracted edge, and the final assertion is exactly associativity of the
finite run-summary monoid on the segments between those edges. \(\square\)

Avoidance of (Z^-) is a clean sufficient protection test.  It need not be
necessary for a target name, because a different occurrence of the same
target may survive.

### Theorem 4.1 (conformal hexagon absorber bank)

Let (Z_1,\ldots,Z_h) be (P)-neutral, (F)-alternating incidence
hexagons whose edge supports are pairwise disjoint.  Then for every
(J\subseteq[h]),

\[
             F_J=F\mathbin\triangle\bigtriangleup_{j\in J}Z_j
\tag{4.2}
\]

is a balanced factor containing (P).  The switches commute and may be
performed in any order.

Suppose additionally that, for each required target (i), one has chosen
an index (j(i)) and a literal witness (Q_i\subseteq F_{\{j(i)\}}), and

\[
 Q_i\cap\bigcup_{j\ne j(i)}Z_j^-=\varnothing.
\tag{4.3}
\]

Then toggling every used hexagon preserves (P) and installs every (Q_i).
If (P) protects the old target section and a residence-corridor cover,
the result is a zero-defect resident factor.

#### Proof

Each hexagon separately removes and adds one incidence at each of its six
vertices.  Pairwise edge-disjointness means toggling one hexagon does not
change the selected/unselected status of an edge in another.  Summing their
balanced signed incidence vectors therefore preserves degree two and binary
edge values for every subset (J).  Their negative shores avoid (P), so
(P) survives.  Condition (4.3) says no other toggle removes the installed
witness (Q_i).  The final assertion follows from Lemma 1.3. \(\square\)

The theorem is the exact form of a local absorber cube.  Finding a
positive-density conformal bank with (4.3), or a bounded-overlap extension
whose union is still a binary circulation, would prove the desired neutral
switch theorem.  Binary generation of the ambient cycle space is not enough,
as the next section shows.

## 5. The smallest protected hexagon obstruction

The following example is entirely inside the genuine balanced middle
incidence graph (I(5,2)).

Write sets without braces.  Consider the induced eight-cycle

\[
 12-123-23-234-34-134-14-124-12.                    \tag{5.1}
\]

Define the following perfect matching of (I(5,2)):

\[
\begin{split}
\mathcal N=\{&23\!-!123, 34\!-!234,
14\!-!134, 12\!-!124,\\
&13\!-!135, 15\!-!125, 24\!-!245,
25\!-!235, 35\!-!345, 45\!-!145\}.
\end{split}                                             \tag{5.2}
\]

Every rank-two and every rank-three vertex occurs exactly once in (5.2).
Since (I(5,2)) is cubic,

\[
                         F=E(I(5,2))\setminus\mathcal N
\tag{5.3}
\]

is a balanced factor.  Its selected shore on (5.1) is

\[
 \mathcal A=\{12\!-!123, 23\!-!234,
               34\!-!134, 14\!-!124\}.             \tag{5.4}
\]

Protect

\[
                              P=F\setminus\mathcal A.  \tag{5.5}
\]

### Proposition 5.1 (protected (C_8), but no protected (C_6))

The protected face (\mathfrak F(P)) has exactly two factors.  They are
(F) and

\[
 F'=P\cup
 \{23\!-!123, 34\!-!234,
   14\!-!134, 12\!-!124\}.                         \tag{5.6}
\]

They are joined by the one alternating eight-cycle (5.1).  There is no
legal (P)-preserving incidence-hexagon move from either state.

#### Proof

Each vertex of (5.1) has one protected incidence in (P), so it has residual
degree demand one.  Every vertex outside (5.1) already has protected degree
two and is saturated.  Hence an extension of (P) can use no edge from a
cycle vertex to an outside vertex.

Among the eight displayed vertices, the only containments are the eight
edges of (5.1): for example (12) is contained only in the two displayed
triples (123,124), and the analogous assertion follows around the list.
Thus the residual graph is exactly a chordless (C_8).  It has exactly two
perfect matchings, (5.4) and the shore displayed in (5.6).  This proves the
two-state assertion.

The residual graph contains no six-cycle, so no (P)-neutral incidence
hexagon can be toggled.  Toggling the whole (C_8) exchanges its two shores
and gives (5.6). \(\square\)

Incidence graphs have no four-cycles.  Thus (C_8) is the smallest possible
support beyond a primitive (C_6), making Proposition 5.1 sharp in circuit
length.  Globally, the binary vector of (5.1) is a sum of incidence
hexagons; every such decomposition necessarily uses an incidence forbidden
by the protected face.  Therefore

\[
 \boxed{
 \text{ambient binary hexagon generation does not imply protected,
 conformal hexagon connectivity}.}
\tag{5.7}
\]

This does not refute a PBBS-specific theorem.  It proves that such a theorem
must use an additional property of the selected PBBS witness bank, rather
than cycle-space generation alone.

## 6. The exact PBBS hypothesis exposed by the theorem

Let (F_{\rm PBBS}) be the balanced PBBS factor and choose one physical
PBBS flag witness for every target to be retained.  Let (P) be the union
of their incidence supports and any protected residence/port data.  For a
chosen bank (Q) of replacement or missing-target witnesses, define

\[
 \begin{split}
 \operatorname{press}_{Q}(S)
    &=|(Q\setminus F_{\rm PBBS})\cap\delta^+(S)|,\\
 \operatorname{cap}_{P,Q}(S)
    &=|\delta^-_{D(F_{\rm PBBS},\,P\cup(Q\cap F_{\rm PBBS}))}(S)|.
 \end{split}                                           \tag{6.1}
\]

Then the exact missing PBBS lemma is

\[
 \boxed{
 \text{choose the witnesses so that }
 \operatorname{press}_{Q}(S)\le
 \operatorname{cap}_{P,Q}(S)\quad\text{for every }S.}
\tag{PBBS-PCUT}
\]

By Theorem 3.1, `(PBBS-PCUT)` is necessary and sufficient for the balanced
factor endpoint after the witness choices are fixed.  Pointwise witness
redundancy does not imply it: several candidates can put pressure on the
same protected exchange cut.  Proposition 5.1 is the extreme case in which
the residual cut structure permits one long circulation but no conformal
hexagon.

The PBBS all-depth theorem supplies the candidate witness families, but no
current theorem proves that one can select a section satisfying
`(PBBS-PCUT)` while retaining enough residence flexibility.  This is a
strictly sharper statement than “PBBS has all-depth support.”

## 7. Residence states and the fragment-braid CSP

There are two different ways to carry residence through the preceding
theorems.

1. **Literal hereditary mode.**  Put a corridor cover into (P).  Then
   Theorems 2.1 and 3.1 preserve residence automatically.  This mode may
   protect too many incidences.
2. **Endpoint-state mode.**  Cut the factor into fragments and label every
   oriented endpoint by its exact finite run-state summary.  Delete every
   seam arc whose state composition creates a forbidden short run.  Apply
   Hall, Tutte, or the circulation criterion in this lifted allowed graph,
   then replay the complete decorated component order.  For a linear word
   the replay includes both boundary collars and allows short leading or
   trailing runs only where the deadline theorem permits them; for a cyclic
   component it also includes the closing seam.

The second mode is the one relevant to the current (k=17) boundary-state
failure.  A perfect matching in the unlabelled Johnson endpoint graph says
nothing about the graph left after the `010/0110` arcs are deleted.  The
reported “pure Johnson matching SAT, run-filtered matching UNSAT” is a Hall
cut in that state-lifted graph.  It is not a global Hamiltonicity
obstruction and it is not contradicted by Theorem 2.1, because the set of
run-safe arcs is an additional state constraint, not merely a fixed subset
(P\subseteq F).

For fixed left/right endpoint states, let (H_0=(L,R;E_0)) be the currently
allowed seam graph and put

\[
                 \delta_0(X)=(|X|-|N_{H_0}(X)|)_+.
\tag{7.1}
\]

Suppose rerooting or upper-service moves create a matching (K) of new
state-safe seams.  If

\[
 |K\cap(X\times(R\setminus N_{H_0}(X)))|
                \ge\delta_0(X)\qquad(X\subseteq L),   \tag{7.2}
\]

then (H_0\cup K) has a perfect matching.

Indeed the right endpoints counted in (7.2) are distinct and new to
(N_{H_0}(X)), so

\[
 |N_{H_0\cup K}(X)|\ge |N_{H_0}(X)|+\delta_0(X)\ge|X|,
\]

and Hall applies.  Condition (7.2) is a strong, deterministic reroot
absorber condition.  It says exactly what the (\sim1739)-scale mandatory
upper-service reroot bank must do in addition to serving upper targets: its
state-safe seam effects must cross every deficient Hall cut in matching-
disjoint fashion.  Here (1739) refers to the separate full-factor
upper-service formulation; it is not the number of joins in the contracted
736-component PBBS-U macro bank.  Counting reroots or endpoint degrees alone
does not imply (7.2).

After the state matching is chosen, the fragment-braid CSP still carries
fresh lower colours, subtour/path topology, protected multi-fragment
witness spans, the absolute residence staircase, and the common-cap
compiler.  The present theorem removes only the supposed additional
balanced-fibre connectivity mystery.

## 8. Independently audited implication boundary

The following statements are proved here.

1. A fixed literal witness/corridor section (P) is preserved along a
   circuit-by-circuit path between any two balanced factors containing it.
2. The number of initially covered targets never decreases along that path.
3. For any proposed physical witness bank (Q), (3.2) is necessary and
   sufficient for a protected balanced-factor endpoint containing (Q).
4. A conformal edge-disjoint bank of alternating incidence hexagons is an
   exact commuting absorber cube.
5. Protected incidence-hexagon connectivity is false in general; the
   explicit (I(5,2)) construction needs one (C_8).
6. For a fixed endpoint-state graph, (7.2) is sufficient to repair all Hall
   deficits by reroot seams.

The following statements are not proved.

1. The canonical PBBS witness section satisfies `(PBBS-PCUT)`.
2. PBBS admits a sparse hereditary corridor cover leaving positive exchange
   connectivity.
3. The mandatory upper-service reroots can be selected to satisfy (7.2)
   together with fresh-colour and protected-span constraints.
4. A state-safe factor endpoint automatically gives one connected fragment
   braid, an admissible absolute staircase, or a common-cap compiler.
5. Exact equality (\nu(k)=B(k)) for general (k).

Thus the sharp reusable target is no longer an unrestricted “hexagons span,
therefore transport” assertion.  It is either `(PBBS-PCUT)` for a selected
physical witness bank, or the stronger state-lifted reroot condition (7.2)
when residence is imposed by endpoint states.
