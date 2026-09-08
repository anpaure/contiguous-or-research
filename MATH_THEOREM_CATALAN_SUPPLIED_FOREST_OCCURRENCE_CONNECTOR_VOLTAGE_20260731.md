# Supplied Catalan forests: exact occurrence connectors and primitive-voltage closure

Date: 2026-07-31  
Status: solver-independent necessary-and-sufficient closure theorem in the
free clean-\(H\), supplied-forest fibre; exact labelled \(m=3\) counterexample
to automatic closure by the middle-levels trace construction

## 0. Verdict

Assume that an \(H\)-invariant Catalan path forest has already been supplied,
where \(H\cong\mathbb Z_h\) acts freely on all literal vertex, edge and
endpoint-occurrence states.  Give every quotient path two formal endpoint
occurrences, including two formal ports at the same vertex for an isolated
path.  Let \(P\) pair the two ports belonging to one path traversal, and let
\({\cal S}\) be the occurrence-labelled catalogue of legal quotient Johnson
connectors, with parallel records and gains retained.

The logically weakest occurrence-level closure hypothesis is the existence of
a connector set \(M\subseteq{\cal S}\) such that

1. every endpoint occurrence is incident with exactly one member of \(M\);
2. the selected literal connector orbits are distinct, disjoint from the
   retained forest and injective after physical development;
3. the alternating port graph \(P\cup M\) is one cycle; and
4. the voltage of that cycle generates \(\mathbb Z_h\).

Equivalently, after orienting every quotient path, the connectors induce one
cyclic permutation of the oriented paths and

\[
 \gcd\!\left(h,
   \sum_i\lambda(P_i)+\sum_{s\in M}\gamma(s)\right)=1.       \tag{0.1}
\]

These four conditions are necessary and sufficient for the retained forest
plus the selected connector orbits to develop to one physical Hamilton cycle.
They do not require connector colours to be new: the already selected global
diamond matching supplies the exact lower and upper palettes, and connector
colour repetition is irrelevant to immediate coverage.  Private collars,
compiler cells, phase guards or other consumable resources still require
their own occurrence-capacity rows.

The middle-levels trace construction does **not** automatically meet this
hypothesis.  Outside its one binary cycle face it supplies the path forest,
but it supplies neither an endpoint connector matching nor an \(H\)-voltage.
More strongly, an exact labelled \(m=3\) Catalan decoration below produces a
five-path forest whose endpoint connector graph has the Hall core
\(2>1\).  It has no physical Johnson closure at all while its forest is
retained.

## 1. Rebased input and exact scope

The present theorem starts after the integral-correlation gate of
`MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md`:
the ordered four-transversal, or any other construction, has supplied a
spanning physical linear forest with exact lower and upper palettes.

For the middle-levels route there is now an earlier exact occurrence gate.
By
`MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md`,
after fixing an upper turn SDR, alternating lower representatives exist if
and only if the induced gap--lower-colour graph has a perfect matching.
Separate surjectivity of the two turn words is not sufficient.  Throughout
the trace discussion below, ``Catalan decoration'' means that this exact
gap--Hall/interlacing gate has already passed.

The global quotient perfect-matching theorem removes the old residual-Kneser
extension question.  It does not choose endpoint connectors.  Likewise,
`MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`
is used only in its stated middle-levels-resolvable class.  No assertion that
an arbitrary Catalan linear matching is middle-levels-resolvable is made.

## 2. Occurrence-port data of a supplied forest

Let the physical middle layer be the Johnson graph

\[
                         J(2m,m),                    \tag{2.1}
\]

and let \(H=\langle\rho\rangle\cong\mathbb Z_h\) act freely on every
literal state used below.  Let \(F\) be an \(H\)-invariant spanning linear
forest.  In the Catalan common-transversal application it has
\(\operatorname {Cat}_m\) physical path components, and its quotient has

\[
                  c=\operatorname {Cat}_m/h          \tag{2.2}
\]

path occurrences.  The closure theorem itself only needs the supplied
quotient path count \(c\).

For each quotient path occurrence \(P_i\), create two formal ports
\(p_i^-\) and \(p_i^+\).  If \(P_i\) is isolated, these are different
occurrences at the same quotient vertex.  Let

\[
 P=\{p_i^-p_i^+:1\le i\le c\}                       \tag{2.3}
\]

be the fixed path-pairing involution on ports.  Orienting the traversal
\(p_i^-\to p_i^+\) gives it a gain \(\lambda(P_i)\in\mathbb Z_h\).
Reversing the path negates this gain.  For an isolated path use the two
formal ports at the same chosen quotient representative and set
\(\lambda(P_i)=0\).

A legal connector record is

\[
 s=(p_i^\epsilon,p_j^\eta;e_s,\gamma(s)),            \tag{2.4}
\]

where \(e_s\) is one literal quotient Johnson-edge orbit joining the two
endpoint vertices and \(\gamma(s)\in\mathbb Z_h\) is its gain in the
displayed direction.  Records are occurrence-labelled: parallel quotient
edges, two ports on an isolated vertex and distinct physical edge orbits are
not collapsed.  The catalogue is assumed to have already removed a connector
orbit if it intersects the retained forest or fails a prescribed literal
guard.  Selected records must still be distinct and jointly develop to
distinct physical edges.

The freeness and injective-development hypotheses are indispensable.  A
stabilized port orbit, a coarsened repeated occurrence, or two quotient
records developing to the same physical edge is not described by the simple
cyclic voltage count below.

## 3. Exact component formula

Let \(M\) be a perfect matching of the formal port occurrences by legal
connector records.  Then

\[
                             P\cup M                  \tag{3.1}
\]

is a two-regular occurrence multigraph, hence a disjoint union of alternating
cycles \(C_1,\ldots,C_t\).  Orient each \(C_r\).  Add the signed gains of
its alternating path traversals and connectors and write

\[
 V_r=\sum_{P_i\subset C_r}\!\pm\lambda(P_i)
      +\sum_{s\subset C_r}\!\pm\gamma(s)
      \pmod h.                                       \tag{3.2}
\]

Changing representatives of quotient vertices adds a coboundary to the edge
gains and therefore does not change \(V_r\).  Because every path is a tree,
one may alternatively gauge every path edge to gain zero and charge the
whole value to the connector records.  The connector gains must be
recomputed in that gauge; the original numerical \(\gamma(s)\)'s are not
held fixed while the path gauges change.

### Theorem 3.1 (supplied-forest occurrence closure)

The developed physical graph \(F\cup\widetilde M\) has exactly

\[
                         \sum_{r=1}^t\gcd(h,V_r)      \tag{3.3}
\]

cycle components, with \(\gcd(h,0)=h\).  In particular,

\[
 F\cup\widetilde M\text{ is one physical Hamilton cycle}
 \quad\Longleftrightarrow\quad
 t=1\quad\hbox{and}\quad\gcd(h,V_1)=1.              \tag{3.4}
\]

#### Proof

Contract every retained physical path to its two formal port occurrences.
This changes neither the component count nor any cycle voltage.  Starting in
phase \(g\in\mathbb Z_h\) above a port of \(C_r\), one traversal of the
alternating quotient cycle returns to that port in phase \(g+V_r\).  The
lifted cycles over \(C_r\) are therefore the orbits of the translation
\(g\mapsto g+V_r\).  Their number is \(\gcd(h,V_r)\).  Summing over the
quotient occurrence cycles gives (3.3), and (3.4) follows.  Since the forest
is spanning and every formal port is used once, the unique connected
two-regular lift in (3.4) is Hamiltonian. \(\square\)

### Corollary 3.2 (weakest invariant-fibre hypothesis)

Within the free \(H\)-invariant fibre in which every edge of \(F\) is
retained, conditions 1--4 in Section 0 are both sufficient and necessary.

Indeed, sufficiency is Theorem 3.1.  Conversely, the complement of \(F\) in
an \(H\)-invariant Hamilton cycle containing \(F\) edgewise uses every
endpoint occurrence once.  Its
quotient is connected and two-regular, hence one alternating occurrence
cycle, and connectedness of its physical development forces primitive total
voltage by (3.3).

Each clause is individually essential.  Port matching without occurrence
connectivity leaves several quotient cycles; one quotient cycle with
nonprimitive voltage leaves several physical phase cycles; and a repeated or
noninjectively developed literal seam does not give a simple Hamilton cycle.
Thus ordinary Hall or Tutte feasibility for the port matching alone is not a
closure theorem.

For \(h=1\), the voltage condition is vacuous and (3.4) reduces to the one
alternating-cycle condition.

The occurrence-multigraph convention includes the small cases.  When
\(c=1\), the closing connector joins the two ports of the sole path and is a
loop only after that path is contracted; together with the path traversal it
is an alternating two-edge cycle on the two formal ports.  When \(c=2\), the
two distinct connectors may become parallel edges after component
contraction.  Neither case may be simplified by identifying the two formal
ports or the two literal connector records.

## 4. Directed cyclic-order form

The same condition can be written without the port involution.  Choose an
orientation of each path and call its entry and exit ports
\(p_i^-\) and \(p_i^+\).  The selected connectors must be

\[
       s_i:p_i^+\longrightarrow p_{\pi(i)}^-          \tag{4.1}
\]

for a permutation \(\pi\) of the \(c\) path occurrences.  Then (3.4) is
equivalent to

\[
 \pi\text{ is one }c\text{-cycle},qquad
 \gcd\!\left(h,
   \sum_i\lambda(P_i)+\sum_i\gamma(s_i)\right)=1.    \tag{4.2}
\]

Thus a ``uniform outgoing orientation'' is not an extra topological axiom:
after orienting the unique alternating occurrence cycle, every retained path
automatically has one entering and one leaving connector.  It becomes a real
restriction only when a pre-oriented connector catalogue forbids one of the
two path orientations.  Literal seam distinctness follows from the edge-orbit
records, not from connector-colour injectivity.

An exact selector formulation may impose one connector at every formal port,
the usual two-edge cut across every proper nonempty set of contracted path
occurrences, literal edge-orbit capacity one, and a primitive residue row for
the oriented total gain.  Any private socket, collar or compiler resource is
an additional capacity row; it is not implied by (4.2).

## 5. What the trace theorem supplies

On a middle-levels Hamilton cycle, a Catalan decoration supplies:

* an upper turn SDR together with a perfect gap--lower-colour matching,
  hence both turn-colour bijections in alternating cyclic order;
* the resulting unique residual cross-edge matching after the turn
  occurrences have been chosen;
* the exact common lower/upper diamond matching; and
* a degree-two physical lift.

For a cyclic trace

\[
                  1^{a_1}0^{b_1}\cdots1^{a_s}0^{b_s},            \tag{5.1}
\]

the alternating SDR forces every \(b_t\) to be positive and even.  The lift
contains one cycle exactly on the exceptional binary face

\[
                     b_t=2\text{ for all }t,qquad
                     a_t\text{ odd for all }t.        \tag{5.2}
\]

Outside (5.2), it is a spanning \(\operatorname {Cat}_m\)-path forest and is
therefore a valid input to Theorem 3.1.  But the trace axioms contain no
endpoint connector selection, no private-socket condition, no clean-group
equivariance and no gain ledger.  None of conditions 1--4 in Section 0 follows
formally even after the exact gap--Hall decoration has been supplied.  A
fortiori, separate two-sided turn surjectivity does not imply them.

The following labelled example shows that this is a real physical failure,
not merely absent bookkeeping.

## 6. Exact \(m=3\) decorated-trace Hall obstruction

Use decimal bitmasks on old coordinates \(0,\ldots,4\), and use bit \(5\)
for \(\infty\).  The following ten pairs give a Hamilton cycle of
\({\rm ML}(5)\), written as \((A_i,B_i)\):

\[
\begin{array}{c|rrrrrrrrrr}
i&0&1&2&3&4&5&6&7&8&9\\ \hline
A_i&3&5&9&10&24&17&20&12&6&18\\
B_i&7&13&11&26&25&21&28&14&22&19.
\end{array}                                           \tag{6.1}
\]

Indeed \(A_i\subset B_i\supset A_{i+1}\), cyclically.  Select

\[
                    I=\{0,1,3,5,7\},\qquad
                    J=\{0,2,4,6,8\}.                 \tag{6.2}
\]

The five cyclic \(I\)-gaps are

\[
 [0,1),[1,3),[3,5),[5,7),[7,0),                    \tag{6.3}
\]

and the selected lower positions \(0,2,4,6,8\) lie one in each gap, with
respective colours \(1,8,16,4,2\).  Thus this fixture passes the exact
gap--Hall criterion, not merely the two separate turn-surjectivity tests.

The ten upper-turn values are

\[
 23,15,15,27,27,29,29,30,30,23,                     \tag{6.4}
\]

and \(I\) selects \(23,15,27,29,30\), all five rank-four masks on
five coordinates.  The ten lower-turn values are

\[
 1,1,8,8,16,16,4,4,2,2,                              \tag{6.5}
\]

and \(J\) selects all five singleton masks.  The cyclic mark trace is

```text
11100110011001100100
```

so marks alternate by rail and all zero-runs are even.  It is outside
(5.2), hence gives a path forest.  Direct literal construction gives the
fifteen physical Johnson edges

\[
\begin{split}
 &(7,13),(7,19),(11,26),(13,41),(14,28),\\
 &(14,38),(19,50),(21,25),(21,52),(26,56),\\
 &(35,37),(38,50),(41,42),(44,52),(49,56).
\end{split}                                           \tag{6.6}
\]

On all twenty vertices of \(J(6,3)\), its five path components may be
oriented as

\[
\begin{split}
 &(28,14,38,50,19,7,13,41,42),\\
 &(11,26,56,49),\\
 &(35,37),\\
 &(44,52,21,25),\\
 &(22).
\end{split}                                           \tag{6.7}
\]

The isolated vertex \(22\) has two formal endpoint occurrences.  Among
the other path endpoints

\[
                 \{28,42,11,49,35,37,44,25\},        \tag{6.8}
\]

it is Johnson-adjacent only to \(28\).  Therefore the two ports at \(22\)
have the single available neighbour port at \(28\).  This is the exact
port-Hall obstruction

\[
                   |\{22^-,22^+\}|=2
                   >|N(\{22^-,22^+\})|=1.            \tag{6.9}
\]

No connector perfect matching exists, even when every unused edge of
\(J(6,3)\) is allowed.  Consequently no Hamilton cycle can contain all
edges of this supplied trace forest.  A switch that deletes forest edges may
escape, but that is outside the supplied-forest closure fibre.

This example satisfies both turn-surjections and an exact gap--Hall
alternating decoration, so the trace construction itself does not
automatically meet even the first occurrence-level connector gate.  Since
the example fails already at \(h=1\), primitive voltage is a fortiori not
automatic.  More generally the trace data contain no \(H\)-action or gains
from which a unit-voltage claim could be inferred.

## 7. Remaining constructive gate

After a Catalan path forest is supplied, the exact remaining problem is now
fully localized:

1. build the occurrence-labelled endpoint connector catalogue, including
   every literal parallel edge orbit and private-resource row;
2. choose one connector at every port so that \(P\cup M\) is connected; and
3. choose the connected closure in a primitive voltage class.

The trace normal form can still be useful as a forest generator, but a
recursive construction must additionally prove this endpoint Hall/circuit/
voltage statement or deliberately alter the forest.  Global quotient colour
matching alone does not imply it.
