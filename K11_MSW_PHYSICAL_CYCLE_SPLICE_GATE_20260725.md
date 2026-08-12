# The exact physical cycle-splice gate for the canonical (K=11) wreath factor

> **Dependency warning (2026-07-25).**  Sections 8--12 use the separate
> cyclic-four support classification.  That classification is currently
> under repair after a direct A--E row contradiction was found (the class-E
> row (4217\mid6538) supports the purported hole
> \(\{1,2,7,10\}\)).  The local physical splice lemmas in Sections 2--7
> and 10 remain independent of that list; the numerical claims (298),
> (32), (224), and the resulting support thresholds are suspended until
> the support ledger is recomputed.

Date: 2026-07-25

## 1. Outcome

Let an exact wreath factor on eleven coordinates be expanded into its forty-two
vertex-disjoint alternating middle-level cycles.  Each cycle contains eleven
rank-five vertices and eleven rank-six vertices and is physical in either
orientation.

This note proves three facts.

1. A one-cut splice of two such cycles has exactly five new no-lazy tests.
   Allowing both orientations, every off-factor middle-level incidence has a
   unique tail orientation which passes the two backward tests.  The two head
   orientations both fail exactly in four explicit ordered-position patterns.
2. The existence of thirty-six legal splices is equivalent to a transversal
   directed linear forest of size thirty-six in an explicit port graph with
   twenty-two vertices over each wreath cycle.  This equivalence preserves
   every rank-five and rank-six vertex exactly and isolates acyclicity as the
   only global condition after the ports have been selected.
3. The lower and upper shadow changes have an exact replacement ledger.  Each
   selected cycle loses one old turn and every splice adds one new turn.  In
   particular, an individual append splice can lose at most one supported
   colour on either side, and a full six-path fusion removes forty-two old
   turns and adds thirty-six new turns.

The standard middle-levels flippable-pair connectivity theorem does **not**
by itself supply this forest.  Its auxiliary graph remembers the cross
incidence but not the two symbols immediately before it or the two deletion
symbols immediately after it.  Precisely half of the raw off-cycle facets at
each oriented canonical tail already fail the backward physical test.  Thus a
published flippable-pair schedule must be lifted chart by chart to the port
graph below; ordinary cycle-joining connectivity is not such a lift.

No computation or enumeration is used.

## 2. Canonical cycles and oriented cuts

Write one cyclic coordinate order as

\[
 z_0,z_1,\ldots,z_{10}
\]

with indices modulo eleven, and put

\[
 S_i=\{z_{i-5},z_{i-4},z_{i-3},z_{i-2},z_{i-1}\},
\]

\[
 U_i=\{z_{i-5},z_{i-4},z_{i-3},z_{i-2},z_{i-1},z_i\}.
\]

The canonical alternating cycle contains

\[
 S_i-U_i-S_{i+1}.
\]

Its port word is

\[
 a_i=z_i,\qquad b_i=z_{i-5}.
\tag{2.1}
\]

An **oriented cut port** is an edge of the alternating cycle together with
the orientation of the remaining path from its rank-five endpoint to its
rank-six endpoint.  Every cycle has twenty-two such ports.  For a port (p),
write

\[
 H(p)=\text{its rank-five head},\qquad
 T(p)=\text{its rank-six tail}.
\]

The other rank-five neighbour of (T(p)), which is the last source on the
oriented cut path, is denoted (L(p)).

Deleting the cut edge gives an alternating path beginning at (H(p)) and
ending

\[
 L(p)-T(p).
\]

Reversing one wreath cycle changes neither its rank-five/rank-six vertex set
nor either cyclic shadow support.  It only exchanges its two possible ports
at a chosen source or target.  Thus both orientations are genuinely
available in the fusion problem.

## 3. The exact five seam tests

Consider an oriented cut path ending at state (i), and another beginning at
state (h).  Let

\[
 \beta=T(p)\setminus H(p')
\]

be the coordinate removed by a proposed cross edge

\[
 T(p)-H(p').
\]

Equivalently, in the complemented notation of the endpoint reduction,

\[
 H(p')\cap D_i=\varnothing.
\]

### Lemma 3.1 (five-test seam lemma)

The cross edge is physical if and only if

\[
 \boxed{
 \begin{aligned}
 \beta&\ne a_{i-2},a_{i-1},\\
 b'_h&\ne a_{i-1},a_i,\\
 b'_{h+1}&\ne a_i.
 \end{aligned}}
\tag{3.1}
\]

#### Proof

Around the new seam the deletion/insertion word is

\[
 \ldots,a_{i-2},b_{i-2},a_{i-1},b_{i-1},a_i,
 \beta,a'_h,b'_h,a'_{h+1},b'_{h+1},\ldots.
\]

Physicality says that an inserted coordinate may not be deleted in either of
the next two transitions.  Only the tests involving

\[
 a_{i-2},a_{i-1},a_i
\]

change.  Their unchanged old deletion tests may be discarded, leaving
exactly (3.1).  The inequalities (a_i\ne\beta) and
(a'_h\ne\beta) are automatic because the cross source and cross target are
different from the old source and target.  All later tests are inherited
from the second cut path.  (square)

This is the exact local condition; no run theorem or sufficient
pairwise-disjointness condition is being substituted for it.

## 4. Every off incidence has one backward-compatible tail orientation

Fix a rank-six vertex (U) of one canonical cycle.  List its elements in
the local cyclic order as

\[
 U=\{u_0,u_1,u_2,u_3,u_4,u_5\}.
\tag{4.1}
\]

Its two rank-five neighbours in its own cycle are

\[
 U-u_0,\qquad U-u_5.
\]

The other four facets (U-u_k), (1\le k\le4), belong to other wreath
cycles.  They belong to four distinct cycles: if another wreath contained
two facets of (U), those two five-windows would be consecutive and their
intermediate six-window would be (U), contradicting the unique ownership
of (U).

Orient the cut path so that its last source is (U-u_5).  The two recent
protected coordinates are

\[
 (a_{i-1},a_i)=(u_4,u_5),
\]

and the backward-compatible off facets are exactly

\[
 U-u_1,\qquad U-u_2.
\tag{4.2}
\]

Under the reverse orientation the last source is (U-u_0), the protected
pair is

\[
 (a_{i-1},a_i)=(u_1,u_0),
\]

and the compatible off facets are exactly

\[
 U-u_3,\qquad U-u_4.
\tag{4.3}
\]

### Theorem 4.1 (unique backward orientation)

For every off-factor incidence

\[
 S=U-u_k\subset U,qquad 1\le k\le4,
\]

exactly one of the two orientations of the cycle containing (U) satisfies
the first line of (3.1).

In particular, for a fixed oriented tail, two of its four geometrically
valid off-cycle facets pass the backward physical test and two fail it.

#### Proof

Equations (4.2)--(4.3) partition the four off facets.  They are obtained by
substituting the two reversed canonical port words in the first line of
(3.1).  (square)

This already proves that unlabelled middle-level adjacency loses essential
information: at every oriented tail it overcounts physical outgoing facets
by a factor two before the head is inspected.

## 5. The exact two-orientation test at the head

Let the proposed head source have its internal cyclic-window order

\[
 S=\{w_0,w_1,w_2,w_3,w_4\}.
\tag{5.1}
\]

Let

\[
 r=a_{i-1},\qquad t=a_i
\]

be the two protected tail coordinates.  The backward condition ensures
(r,t\in S).

If the head cycle is traversed forward, its first two deletion ports are

\[
 w_0,w_1.
\]

If it is traversed backward, they are

\[
 w_4,w_3.
\]

Consequently the forward orientation is legal exactly when

\[
 w_0\notin\{r,t\},\qquad w_1\ne t,
\tag{5.2}
\]

and the reverse orientation is legal exactly when

\[
 w_4\notin\{r,t\},\qquad w_3\ne t.
\tag{5.3}
\]

### Theorem 5.1 (double-block classification)

Write (operatorname{pos}(x)) for the position of (x) in (5.1).  Both
head orientations fail if and only if

\[
 \boxed{
 (\operatorname{pos}(r),\operatorname{pos}(t))
 \in\{(4,0),(4,1),(0,3),(0,4)\}.}
\tag{5.4}
\]

#### Proof

The forward direction fails precisely when

\[
 \operatorname{pos}(r)=0
 \quad\text{or}\quad
 \operatorname{pos}(t)\in\{0,1\},
\]

and the reverse direction fails precisely when

\[
 \operatorname{pos}(r)=4
 \quad\text{or}\quad
 \operatorname{pos}(t)\in\{3,4\}.
\]

Intersecting the two conditions, with (r\ne t), gives exactly the four
ordered pairs in (5.4).  (square)

Thus an off-factor incidence has a unique backward-compatible tail
orientation and at least one compatible head orientation unless its two
protected coordinates form one of four explicit double-block patterns.
Nothing in ordinary middle-level incidence excludes those four patterns.

### Corollary 5.2 (a missing lower colour has only two blocking patterns)

For a cross incidence, the new lower colour is

\[
 B^*=S\setminus\{t\}.
\]

If (B^*) is absent from the original canonical cyclic-four-window
support, then

\[
 \operatorname{pos}(t)\notin\{0,4\}.
\]

Consequently a support-repairing incidence is double-blocked only in the
two cases

\[
 \boxed{(\operatorname{pos}(r),\operatorname{pos}(t))
        \in\{(4,1),(0,3)\}.}
\tag{5.5}
\]

#### Proof

Deleting (w_0) or (w_4) from the five-window
(S=(w_0,w_1,w_2,w_3,w_4)) leaves respectively the old cyclic windows
({w_1,w_2,w_3,w_4}) or ({w_0,w_1,w_2,w_3}).  Such a colour is already
in the canonical support.  Therefore a missing (B^*) has (t) in an
internal position.  Intersect this with the four cases in (5.4). □

## 6. The physical port graph and exact fusion equivalence

Let (mathcal C) be the set of forty-two wreath cycles.  Define a directed
graph (mathfrak P(F)) as follows.

* Its vertices are the (42\cdot22=924) oriented cut ports.
* Ports are partitioned into forty-two groups, one group over each wreath.
* There is an arc (p\to p') precisely when
  (H(p')\subset T(p)), the two ports lie over different wreaths, and the
  five tests (3.1) hold.

### Theorem 6.1 (transversal linear-forest equivalence)

The forty-two physical wreath cycles can be fused by one-cut splices into
six physical alternating paths if and only if there are

1. a transversal (P\subset V(\mathfrak P(F))) containing one port over
   each wreath cycle; and
2. thirty-six arcs of the induced graph (mathfrak P(F)[P])

whose indegrees and outdegrees are at most one and which contain no directed
cycle.

#### Proof

Cut every wreath at its selected port.  An arc (p\to p') joins the upper
tail of the first cut path to the lower head of the second.  The indegree and
outdegree bounds use each endpoint at most once.  Acyclicity makes the result
a path forest.  Since it has forty-two vertices and thirty-six arcs, it has
six components.

Every original rank-five and rank-six vertex remains present exactly once.
At an internal port, its missing head edge and missing tail edge are filled
by the incoming and outgoing cross edges.  A directed source retains one
rank-five endpoint and a sink retains one rank-six endpoint.  Therefore every
component is an alternating path from rank five to rank six.  Lemma 3.1
proves physicality at every seam.  The two seams bordering an internal
eleven-cycle segment are separated by ten old quotient transitions, so their
radius-two tests do not interact.

Conversely, a one-cut fusion records one oriented cut port per original
wreath and one port-graph arc per cross edge.  Its six path components give
the degree and acyclicity conditions, and the edge count is thirty-six.
(square)

After the local arc filter has been imposed, **acyclicity is the only
remaining nonlocal path condition**.  In particular, ignoring acyclicity
first gives a partition-constrained bipartite matching problem; subtour
elimination is a separate final step.

## 7. Audit of the standard flippable-pair route

The ordinary middle-level cycle-joining constructions use an auxiliary
graph or hypergraph whose edges certify alternating middle-level incidences.
That datum sees

\[
 H(p')\subset T(p),
\]

but it does not record

\[
 a_{i-2},a_{i-1},a_i,b'_h,b'_{h+1}.
\]

Theorems 4.1 and 5.1 give an exact lift audit.

* At every oriented canonical tail, two of the four raw off-cycle facets
  are invalid because the cross deletion equals one of the two protected
  recent insertions.
* For either surviving facet, both choices of head orientation can still be
  invalid, precisely in the four patterns (5.4).

Therefore a connected standard flippability graph, a spanning tree in the
MNW support hypergraph, or the existence of an unrestricted middle-level
Hamilton cycle does not imply the transversal forest of Theorem 6.1.
Every new seam in a proposed standard switch must first lift to an arc of
(mathfrak P(F)).  The published connectivity statement contains no such
port assertion.

This is not a proof that all standard MSW switches fail.  It is the precise
reason they cannot be imported as a black box.  A successful lift must prove
that thirty-six dynamically compatible charts avoid both the backward half
of the raw facets and the four head double-block patterns, with a common
choice of one port per wreath.

## 8. Exact lower/upper support ledger

For a selected port (p), let

\[
 B_0(p),\qquad Y_0(p)
\]

be the lower rank-four and complementary-upper rank-four turn colours on
the deleted old edge.  For an arc (e=p\to p'), let

\[
 B^*(e)=L(p)\cap H(p'),
\]

and, writing (D(p)=[11]\setminus T(p)) and (D_1(p')) for the first
target complement after the head,

\[
 Y^*(e)=D(p)\cap D_1(p').
\]

In the canonical notation of Section 2 these are

\[
 B^*(e)=U_i\setminus\{z_i,\beta\},
\qquad
 Y^*(e)=D_i\setminus\{a'_h\}.
\tag{8.1}
\]

Here the \(z\)-indices are taken in the selected orientation of the tail
port.  If one instead keeps one fixed forward \(z\)-order while selecting
the reverse tail orientation at \(D_i\), the first formula reads

\[
 B^*(e)=U_i\setminus\{z_{i-5},\beta\}.
\tag{8.1a}
\]

Let (m_Z(C)) be the initial multiplicity of colour (C) in ledger
(Z\in\{B,Y\}).  If (r_Z(C)) selected cuts have old colour (C), and
(s_Z(C)) selected arcs create (C), then the final multiplicity is

\[
 \boxed{m_Z^{\rm fin}(C)=m_Z(C)-r_Z(C)+s_Z(C).}
\tag{8.2}
\]

Consequently, if the initial support is (sigma_Z), then

\[
 \boxed{
 \sigma_Z^{\rm fin}
 =\sigma_Z-L_Z+G_Z,}
\tag{8.3}
\]

where

\[
 L_Z=#\{C:m_Z(C)>0, r_Z(C)=m_Z(C), s_Z(C)=0\},
\tag{8.4}
\]

\[
 G_Z=#\{C:m_Z(C)=0, s_Z(C)>0\}.
\tag{8.5}
\]

This is an exact support identity, not a union bound.

There are forty-two deleted old turns and thirty-six new seam turns.  In a
sequential append realization, each splice cuts one new cycle turn and adds
one seam turn; hence one append splice can decrease either support by at
most one.  The six final path sinks account for the six cut turns which have
no outgoing replacement.  The crude universal bound is therefore

\[
 \sigma_Z^{\rm fin}\ge\sigma_Z-42.
\tag{8.6}
\]

The useful criterion is the exact one:

\[
 \boxed{L_B-G_B\le\sigma_B-319,
 \qquad L_Y-G_Y\le\sigma_Y-319.}
\tag{8.7}
\]

For example, if an initial cyclic ledger has full support (330), at most
eleven net colour extinctions are allowed on either side.  Equivalently, at
least thirty-one of the forty-two selected cut turns on each side must be
redundant or restored by seam colours, after coincidences between cut
colours are counted correctly.

For the canonical support \(\sigma_B=\sigma_Y=298\), (8.7) is equivalent to

\[
 G_B-L_B\ge21,\qquad G_Y-L_Y\ge21.
\tag{8.8}
\]

Since there are only thirty-two initially missing colours, \(G_Z\le32\);
hence every valid fusion necessarily satisfies

\[
 \boxed{L_B\le11,\qquad L_Y\le11.}
\tag{8.9}
\]

There are only thirty-six seam arcs.  A seam contributes at most one new
colour to each ledger.  Therefore at least

\[
 \boxed{6+L_B+L_Y}
\tag{8.10}
\]

of the selected seams must simultaneously create an initially missing
lower colour and an initially missing complementary-upper colour.  At such
a seam the two four-sets are disjoint, because

\[
 \Omega=B^*\sqcup Y^*\sqcup
 \{\text{the three seam letters}\}.
\tag{8.11}
\]

Thus the explicit disjointness graph on the thirty-two canonical holes is
an unavoidable coupled resource; separate lower and upper Hall matchings
cannot prove the fusion theorem.

## 9. Exact remaining finite theorem

For the canonical MSW factor at (m=5), the cycle-fusion line has now been
reduced to the following object.

> **Physical rainbow port-forest theorem.**  In the \(924\)-vertex grouped
> port graph \(\mathfrak P(F_{\rm MSW})\), choose one vertex from each of the
> forty-two groups and thirty-six induced arcs forming a directed linear
> forest, so that the two exact ledgers (8.2) both have support at least
> (319).

The local seam rule, exact middle ownership, and support accounting are all
closed.  What remains is a coupled representative/matching/subtour problem.
Ordinary MNW flippability connectivity is only the unfiltered projection of
this problem and does not settle it.

## 10. Exact audit of the universal four-letter MSW (C_8)

There is one standard MSW chart whose ports can be checked completely.  It
both exhibits the failure of the inherited switch orientation and supplies a
repaired physical splice.

Let

\[
 T=(t_0,t_1,t_2,t_3,t_4,t_5,t_6)
\]

be an ordering of seven labels, disjoint from the four labels
\(\alpha,\beta,\gamma,\delta\), and put

\[
 \begin{aligned}
 C&=(\delta,\beta,\gamma,\alpha,T),\\
 D&=(\beta,\alpha,\delta,\gamma,T).
 \end{aligned}
\tag{10.1}
\]

For a cyclic omitted-label word (Q=(q_0,\ldots,q_{10})), write

\[
 V_j(Q)=\{q_{j+1},q_{j+3},q_{j+5},q_{j+7},q_{j+9}\}.
\tag{10.2}
\]

Denote (V_j(C)) by (c_j) and (V_j(D)) by (d_j).  The universal MSW
(C_8) contains the new odd-graph edge

\[
 c_1-d_4.
\tag{10.3}
\]

Indeed,

\[
 c_1=\{\gamma,t_0,t_2,t_4,t_6\},
\]

\[
 d_4=\{\beta,\delta,t_1,t_3,t_5\},
\]

so these sets are disjoint and their unique omitted coordinate is
(alpha).

### Proposition 10.1 (the inherited (C_8) seam is backward-lazy)

Use the old (C_8) cut (c_0c_1) on the (C)-wreath and orient its
remaining path so that its last source before target complement (c_1) is
(c_2).  Then the current and preceding insertion labels are

\[
 a_i=\beta,\qquad a_{i-1}=\alpha.
\]

The cross edge (10.3) has cross deletion (alpha).  Hence

\[
 \beta^*=a_{i-1},
\]

and the first line of (3.1) fails.

Thus the ordinary inherited-path orientation of the standard (C_8) is
not a legal one-seam splice.  This does not say that the complete (C_8)
factor trade is nonphysical: that trade creates two new canonical wreaths
and reverses one short inherited path.  It says precisely that its usual
cycle-joining provenance cannot be copied as one unchanged-history seam.

#### Proof

The odd edge (c_1c_2) omits the symbol (q_1(C)=\beta), while the
preceding odd edge (c_2c_3), in the inherited orientation, places
(q_3(C)=\alpha) in the protected slot.  Equation (10.3) omits the only
coordinate outside (c_1\cup d_4), namely (alpha).  Lemma 3.1 applies.
(square)

### Theorem 10.2 (one-edge-shifted physical (C_8) splice)

Instead cut the (C)-wreath at (c_1c_2), with head (c_2), last source
(c_0), and target complement (c_1).  Cut the (D)-wreath at
(d_3d_4), with head (d_4), and add the cross edge (c_1d_4).

The resulting one-cut concatenation is physical.  Its five seam symbols are

\[
 \boxed{
 (a_{i-2},a_{i-1};\beta^*;
   b'_h,b'_{h+1};a_i)
 =(t_3,t_5;\alpha;t_1,t_3;\delta).}
\tag{10.4}
\]

All five inequalities in (3.1) follow from the distinctness of the eleven
labels.

The new lower and complementary-upper colors are

\[
 \boxed{B^*=\{\beta,t_1,t_3,t_5\},}
\tag{10.5}
\]

\[
 \boxed{Y^*=\{\gamma,t_2,t_4,t_6\}.}
\tag{10.6}
\]

Moreover the deleted (C)-turn colors are

\[
 B_C=\{\alpha,t_1,t_3,t_5\},
\qquad
 Y_C=\{t_0,t_2,t_4,t_6\},
\tag{10.7}
\]

while the deleted lower color at the (D)-head cut is

\[
 B_D=\{\beta,t_1,t_3,t_5\}=B^*.
\tag{10.8}
\]

Thus this seam automatically restores the lower cut color of its head
wreath.

#### Proof

With the shifted (C)-cut, the last matching edge is (c_0c_1), whose
omitted label is (delta).  Reading the source states backward by two
positions gives the preceding protected labels (t_5,t_3).  The cross edge
omits (alpha).

Starting the (D)-path at (d_4) in the indicated orientation, its first
two deletion edges omit (t_1,t_3).  This proves (10.4) and hence
physicality.

Directly from (10.2),

\[
 c_0=\{\alpha,\beta,t_1,t_3,t_5\},
\]

and (10.5) is (c_0\cap d_4).  The first target complement after (d_4)
is

\[
 d_5=\{\alpha,\gamma,t_2,t_4,t_6\},
\]

so (c_1\cap d_5) gives (10.6).  Finally

\[
 c_2=\{\alpha,\delta,t_1,t_3,t_5\},
\qquad
 c_3=\{\beta,t_0,t_2,t_4,t_6\},
\]

and

\[
 d_2=\{\beta,\gamma,t_1,t_3,t_5\}.
\]

The intersections (c_0\cap c_2), (c_1\cap c_3), and
(d_2\cap d_4) are exactly (10.7)--(10.8).  (square)

Theorem 10.2 is a genuine exact splice lemma extracted from a standard MSW
chart.  The canonical MSW atlas contains only a Catalan-sized sparse family
of these four-letter charts (fourteen chart occurrences at (m=5) when all
Dyck concatenation positions are included), so this lemma alone does not
provide the thirty-six edges required by Theorem 6.1.  Its significance is
sharper: standard switch geometry is usable, but only after a port-sensitive
cut shift which is invisible in the ordinary flippability graph.

## 11. Seven backward-safe witnesses for every missing lower colour

The orientation freedom has a useful support consequence which does not
require the explicit list of thirty-two holes.

### Theorem 11.1 (seven distinct tail-wreath witnesses)

Let \(C\in\binom{\Omega}{4}\) be absent from the canonical cyclic
four-window support.  For every

\[
 \beta\in\Omega\setminus C
\]

there is a backward-safe off-factor splice whose new lower colour is \(C\).
The seven resulting tail five-sets \(C\cup\{\beta\}\) lie in seven distinct
wreath cycles.

Equivalently, in the bipartite graph joining a missing four-colour to a
wreath cycle when that cycle has a backward-safe port creating the colour,
every missing colour has degree exactly seven.  For the canonical
\(m=5\) factor this graph has \(32\cdot7=224\) incidences.

#### Proof

Fix \(\beta\notin C\), and let

\[
 W=C\cup\{\beta\}
\]

be its unique owner five-window.  Write the cyclic order around \(W\) as

\[
 \ldots,w_{-1},w_0,w_1,w_2,w_3,w_4,w_5,\ldots,
 \qquad W=\{w_0,w_1,w_2,w_3,w_4\}.
\]

The symbol \(\beta\) cannot be \(w_0\) or \(w_4\), because deleting either
endpoint leaves one of the owner's old cyclic four-windows, whereas \(C\)
is missing.  Hence

\[
 \beta\in\{w_1,w_2,w_3\}.
\tag{11.1}
\]

If \(\beta=w_1\) or \(w_2\), take

\[
 U^+=W\cup\{w_5\}
\]

and use the forward tail orientation whose last source is \(W=U^+-w_5\).
Theorem 4.1 says that precisely the facets \(U^+-w_1\) and \(U^+-w_2\)
are backward-safe.  Choose the one omitting \(\beta\).  Its cross head is

\[
 H^+=U^+-\beta,
\]

and its lower turn is

\[
 W\cap H^+=W-\beta=C.
\tag{11.2}
\]

If \(\beta=w_2\) or \(w_3\), instead take

\[
 U^-=W\cup\{w_{-1}\}
\]

and use the reverse tail orientation whose last source is
\(W=U^--w_{-1}\).  In the notation of Theorem 4.1, \(\beta\) is one of
the two reverse-safe internal omissions.  Again the cross head
\(H^-=U^--\beta\) satisfies

\[
 W\cap H^-=C.
\tag{11.3}
\]

Thus (11.1) always supplies at least one backward-safe splice.  Its head
belongs to another wreath: it is an off-factor facet of \(U^\pm\).

It remains to prove distinctness of the seven tail cycles.  Suppose
\(C+\beta\) and \(C+\gamma\), with \(\beta\ne\gamma\), belonged to one
wreath.  They are two cyclic five-windows with intersection of size four.
Two such windows in an eleven-cycle must be consecutive, and their
intersection \(C\) is then a cyclic four-window of that wreath.  This
contradicts the choice of \(C\).  Hence the seven values of \(\beta\) give
seven distinct tail wreaths. \(\square\)

The theorem concerns only the two backward seam tests.  A witness may still
be deleted by the two-orientation head obstruction (5.4), and one selected
port must serve both the incoming and outgoing arc of an internal path
component.  Thus the \(224\)-incidence graph is a genuine Hall resource, not
yet a proof of the \(21\) distinct support repairs required by (8.7).

## 12. A sharp degree-to-twenty-one matching reduction

The number (224=32\cdot7) sits just four incidences above the
degree-eleven obstruction.  This gives a useful exact reduction which does
not require checking all Hall subsets separately.

### Proposition 12.1 (the (224/11) matching threshold)

Let \(\mathcal H\) be the bipartite graph of Theorem 11.1, with the
thirty-two missing colours on the left and the forty-two tail wreaths on
the right.  If every tail wreath is incident with at most eleven missing
colours, then \(\mathcal H\) has a matching of size at least twenty-one.

More generally, let \(\mathcal H'\) be any subgraph of \(\mathcal H\)
(for example, after imposing the head tests).  If

\[
 |E(\mathcal H')|\ge221
 \quad\hbox{and}\quad
 \Delta(\mathcal H')\le11,
\tag{12.1}
\]

then \(\mathcal H'\) has a matching of size at least twenty-one.

#### Proof

By Koenig's theorem, the maximum matching size equals the minimum vertex
cover size.  A vertex cover of size at most twenty can meet at most
\(20\cdot11=220\) edges when the maximum degree is at most eleven.  Such a
cover therefore cannot cover the (224) edges of \(\mathcal H\), or the
at least (221) edges of \(\mathcal H'\).  Hence every vertex cover, and
therefore every maximum matching, has size at least twenty-one. \(\square\)

The degree-eleven premise is deliberately isolated: it is a finite
statement about how many of the thirty-three internal four-facets of the
eleven middle windows in one canonical wreath belong to the explicit
missing family (3.1)--(4.1).  If it holds, the backward half of the lower
support target already has twenty-one distinct colours on twenty-one
distinct tail cycles.  What it still does not supply is the compatible
choice of head cycles, the upper colour gains, the cut-loss ledger, or the
extension to a thirty-six-arc directed linear forest.
