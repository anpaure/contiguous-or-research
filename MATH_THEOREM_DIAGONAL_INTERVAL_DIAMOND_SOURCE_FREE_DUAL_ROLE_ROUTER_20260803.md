# Diagonal interval diamonds give a source-free dual-role router

**Date:** 2026-08-03  
**Status:** exact occurrence-level theorem on the native interval-address
face.  No computation is used.  The theorem removes the boundary-source
capacity-two obstruction for one occurrence coordinate when an already
materialized upper-turn occurrence is allowed to retain its upper-witness
role while serving as the terminal of the same typed ticket.  It does not
prove that an arbitrary common-cap state admits that role coinstantiation,
nor does it prove two-coordinate product closure.

## 0. Result

Let indices lie in \(\mathbb Z_W\), let \(2\le d<W-2\), and let

\[
 A_0,A_1,\ldots,A_{W-1}\ne\varnothing
\]

be a cyclic literal source word.  Assume the flat q1-exact diagonal
identities

\[
 T_i=\bigcup_{h=i}^{i+d}A_h,\qquad
 P_i=\bigcup_{h=i+1}^{i+d}A_h=T_i\cap T_{i+1},
\tag{0.1}
\]

where \(|T_i|=r\), \(|P_i|=r-1\), and the two families run once through
their respective middle-level shores.  Put

\[
 R_i=T_i\cup T_{i+1}.
\tag{0.2}
\]

Give the relevant cells their literal cyclic interval addresses

\[
 p_i=[i+1,i+d]_W,\qquad
 o_i=[i,i+d]_W,\qquad
 q_i=[i,i+d+1]_W.
\tag{0.3}
\]

Then each index gives a **literal interval diamond**

\[
\begin{array}{ccccc}
 &&o_i&&\\[-2mm]
 &\nearrow&&\searrow&\\[-2mm]
 p_i&&&&q_i\\[-2mm]
 &\searrow&&\nearrow&\\[-2mm]
 &&o_{i+1}&&
\end{array}
\tag{0.4}
\]

simultaneously in physical interval addresses and in Boolean values:

\[
 p_i\subset o_i,o_{i+1}\subset q_i,
 \qquad
 P_i\subset T_i,T_{i+1}\subset R_i.
\tag{0.5}
\]

Consequently the two path families

\[
 \mathcal L^0=\{p_i-o_i-q_i:i\in\mathbb Z_W\},
 \qquad
 \mathcal L^1=\{p_i-o_{i+1}-q_i:i\in\mathbb Z_W\}
\tag{0.6}
\]

are literal pairwise vertex-disjoint full linkages from the \(W\) ports to
the \(W\) upper-turn occurrences.  Their Hasse incidences are private;
the boundary letters are occurrence labels on those incidences, not
capacity vertices.

In particular, on the native interval-address face:

1. every owner has a private, source-free attachment to a matched upper
   occurrence;
2. every port has a complete unit-capacity route to a distinct upper
   occurrence with no extra physical cell;
3. if an owner occurrence is unavailable as a transit vertex, each diamond
   contracts to the complete typed bundle \(p_i\rightsquigarrow q_i\), so
   the owner remains a named semantic witness but is not a used capacity;
4. if \(q_i\) may simultaneously certify its existing upper value \(R_i\)
   and terminate the ticket whose declared envelope is the same \(R_i\),
   the suffix gammoid on the full port bank has rank \(W\).

Thus the \(W\)-scale *additional* socket bank is unnecessary on this
dual-role face.  The existing upper-turn bank is the terminal bank.

The earlier \(\lfloor W/2\rfloor\) source cut remains correct for the
strictly stronger auxiliary model which turns every boundary-letter label
into a unit-capacity transit vertex.  It is not a cut in the native
OR-word interval-address model: different interval witnesses may overlap
in source positions, and using a long interval does not consume each of its
singleton subintervals.

## 1. Interval-address capacity, not position-disjointness

For a fixed word \(A\), a physical occurrence is an interval **address**
\([s,t]\), carrying the unique value

\[
 \operatorname{OR}_A[s,t]=\bigcup_{h=s}^t A_h.
\tag{1.1}
\]

Distinct target assignments need distinct interval addresses.  They do
not need disjoint sets of source positions.  Indeed, all interval ORs are
simultaneously defined by the same fixed word, and arbitrary selected
intervals may overlap.

In particular, the singleton interval \([h,h]\) and a longer interval
containing position \(h\) are different physical cells.  Assigning the
singleton cell to one literal target does not prevent the longer interval
from witnessing another target.  Equivalently, when a containment
incidence is recorded as

\[
 [s,t]\xrightarrow{A_{s-1}}[s-1,t]
 \quad\hbox{or}\quad
 [s,t]\xrightarrow{A_{t+1}}[s,t+1],
\tag{1.2}
\]

the displayed letter is the exact semantic label of the incidence.  It is
not automatically an additional finite-capacity vertex.

This distinction is forced by the definition of a universal OR word.  A
model which node-prices the label in (1.2) is a valid stronger sufficient
model, but position-disjointness in that model is not necessary for
simultaneous interval witnesses.

## 2. The physical Boolean diamond

The four address containments in (0.5) are immediate from (0.3):

\[
\begin{aligned}
 [i+1,i+d]_W&\subset[i,i+d]_W\subset[i,i+d+1]_W,\\
 [i+1,i+d]_W&\subset[i+1,i+d+1]_W\subset[i,i+d+1]_W.
\end{aligned}
\tag{2.1}
\]

The literal value identities are

\[
\begin{aligned}
 P_i\cup A_i&=T_i,
 &P_i\cup A_{i+d+1}&=T_{i+1},\\
 T_i\cup A_{i+d+1}&=R_i,
 &T_{i+1}\cup A_i&=R_i.
\end{aligned}
\tag{2.2}
\]

Because \(P_i=T_i\cap T_{i+1}\) has rank \(r-1\), the two owners are
distinct rank-\(r\) sets and their union has rank \(r+1\).  Therefore every
inclusion in (2.2) is a Boolean Hasse incidence.  At the same time, every
address inclusion in (2.1) changes the interval length by one.  Hence (0.4)
is not merely an abstract containment square: it is an occurrence-labelled
diamond in the physical interval poset.

The two ordered edge-label pairs are

\[
 \begin{array}{c|c}
 p_i-o_i-q_i&(A_i,A_{i+d+1})\\
 p_i-o_{i+1}-q_i&(A_{i+d+1},A_i).
 \end{array}
\tag{2.3}
\]

The labels certify the two literal unions.  Section 1 explains why they
need not be inserted as internal capacity vertices.

## 3. Two explicit full linkages

### Theorem 3.1

In the node-split occurrence network whose finite vertices are the port,
owner, and upper-turn interval addresses, and whose directed arcs are the
four private Hasse incidences in (0.4), each family in (0.6) is a
unit-capacity full linkage.

### Proof

In \(\mathcal L^0\), path \(i\) uses the triple

\[
 (p_i,o_i,q_i).
\tag{3.1}
\]

Each coordinate is injective in \(i\).  Hence the paths are pairwise
vertex-disjoint.  In \(\mathcal L^1\), path \(i\) uses

\[
 (p_i,o_{i+1},q_i),
\tag{3.2}
\]

and translation \(i\mapsto i+1\) is a permutation of \(\mathbb Z_W\), so
these paths are again pairwise vertex-disjoint.  The arcs are distinct
ordered occurrence incidences, and (2.2) proves their literal semantics.
\(\square\)

### Corollary 3.2 (zero overload of the complete diamond catalogue)

Retain both paths at every port.  Every port, owner, and upper-turn
occurrence has raw multiplicity exactly two, while every directed Hasse
incidence has multiplicity one.  Uniform path weight \(1/2\) is therefore
a feasible balanced flow of value \(W\).

### Proof

Port \(p_i\) and terminal \(q_i\) lie on the two paths of diamond \(i\).
Owner \(o_i\) lies on \(p_i-o_i-q_i\) and on
\(p_{i-1}-o_i-q_{i-1}\).  The four directed incidence types in (0.4) are
indexed uniquely by their diamond.  Dividing the vertex multiplicities by
two gives load one. \(\square\)

### Corollary 3.3 (mixed ledger: lower source priced, upper source free)

Even in the stronger model which node-prices the boundary source used by
the lower port-to-owner step, either phase is a unit-capacity full linkage
provided the owner-to-upper Hasse attachment is kept source-free.

For the first phase, use the finite-resource records

\[
 (p_i,a_i,o_i,q_i),
 \qquad a_i=[i,i].
\tag{3.3}
\]

For the second phase, use

\[
 (p_i,a_{i+d+1},o_{i+1},q_i).
\tag{3.4}
\]

Every coordinate in either row is injective in \(i\).  Hence both are
pairwise capacity-disjoint full linkages with unit source capacities.

This is the precise realization of the source-free alternative in the
two-boundary dichotomy.  One need not remove all source pricing: it is
enough not to charge a second source unit for the attachment between two
already materialized nested interval occurrences.

## 4. Private source-free attachment and reserved-owner bypass

The upper half of the first phase consists of the occurrence-labelled
Hasse edges

\[
 \eta_i:o_i\longrightarrow q_i.
\tag{4.1}
\]

Their tails and heads are separately injective.  Thus \(\{\eta_i\}\) is
the private source-free owner-to-upper attachment required by the earlier
two-boundary dichotomy.  Likewise

\[
 \eta'_i:o_{i+1}\longrightarrow q_i
\tag{4.2}
\]

is a second such attachment.

Here "source-free" has a precise meaning: the arc record retains the
literal label \(A_{i+d+1}\) in (4.1), or \(A_i\) in (4.2), but it has no
finite internal capacity.  Both endpoint intervals already exist in the
fixed word.  The attachment certifies their literal containment; it does
not construct the upper interval by consuming the boundary singleton as a
new cell.

If owner reservation removes \(o_i\) from the residual transit network,
use a **complete diamond bundle**

\[
 \beta_i=(p_i,q_i;P_i,T_i,T_{i+1},R_i,
              A_i,A_{i+d+1}).
\tag{4.3}
\]

The finite occurrence coordinates of \(\beta_i\) are only \(p_i\) and
\(q_i\).  Its record contains both internal owners and all four identities
in (2.2), so it is a complete canonical route rather than an untyped
shortcut.  The representatives \(\beta_i\) are mutually capacity-disjoint
because their port and terminal coordinates are injective.  This is exactly
the complete-route representation permitted in a terminal Rado menu: one
representative records the whole conjunctive block, not one atom of it.

Thus deleting native owners as residual **capacity vertices** does not
destroy the bundled diagonal route.  It destroys only the stricter network
which insists that an owner be a transit capacity.

## 5. Dual-role coinstantiation

The upper obligation at seam \(i\) is the fact

\[
 \operatorname{OR}_A(q_i)=R_i.
\tag{5.1}
\]

The diagonal terminal ticket supplied by \(\beta_i\) has endpoint \(q_i\)
and retains the same declared envelope \(R_i\), together with the contained
owner alternatives \(T_i,T_{i+1}\).  When the terminal specification
accepts this exact occurrence/type, (5.1) and the terminal obligation are
not two different assignments of values to one cell.  They are two roles
of the same occurrence fact.  Charging \(q_i\) once is therefore exact.

Let \(Q=\{q_i:i\in\mathbb Z_W\}\) be the unit terminal bank and let
\(\Gamma_\diamond\) be the strict gammoid generated by the direct bundle
arcs \(p_i\rightsquigarrow q_i\).  Then

\[
 r_{\Gamma_\diamond}(X)=|X|
 \qquad(X\subseteq\{p_i\}),
\tag{5.2}
\]

and in particular

\[
 r_{\Gamma_\diamond}(\{p_i\})=W.
\tag{5.3}
\]

No additional terminal socket is used.

This is the exact point at which the theorem stops.  If the terminal role
demands a different value, a different cap state, or an occurrence which
must be unused in the single-role sense, then (5.1) does not coinstantiate
it and the theorem supplies no sink.

## 6. Relation to the boundary-source capacity cut

Refine every diamond route into a path which node-prices both displayed
labels in (2.3).  Every route then uses two distinct source occurrences.
The total unit source capacity is \(W\), so at most \(\lfloor W/2\rfloor\)
routes coexist.  Giving every source capacity two makes either complete
phase feasible with exact load two.

There is no contradiction.  The two networks answer different questions:

\[
\begin{array}{c|c}
\text{native interval occurrence network}
 &\text{overlap of constituent positions is free; full rank }W,\\
\text{boundary-node refinement}
 &\text{each edge label is a unit transit resource; rank at most }W/2.
\end{array}
\tag{6.1}
\]

The second row is a stronger sufficient implementation.  It becomes
necessary only when some external guard or compiler rule genuinely consumes
the boundary singleton occurrence as a unit route resource.  Such a rule
must be stated explicitly; it is not implied by ordinary OR-word interval
semantics.

This also gives the sharp local no-go.  If complete routes are required to
move through rank-by-rank interval Hasse steps **and** every added endpoint
position is node-priced, no unit-capacity local router can exceed
\(\lfloor W/2\rfloor\).  The minimal escapes are precisely:

1. use the native edge-labelled interval diamonds of this theorem;
2. provide honest capacity two at the endpoint source nodes; or
3. leave the local interval-Hasse face and export another terminal bank.

## 7. Two occurrence coordinates

The theorem closes one occurrence coordinate.  It yields an exact
zero-defect two-coordinate terminal compiler under either of the following
additional, explicit conditions.

1. The two systems have capacity-separated copies of their diagonal
   upper-turn banks and their cap state has global product closure.  Apply
   (5.2) in each system and then the terminal two-Rado theorem.
2. Both coordinate roles of each logical ticket may coalesce on one
   physical \(q_i\), and the legal paired-occurrence relation contains a
   deterministic diagonal bundle \((q_i,q_i)\) after one common relabelling.
   Then every ticket consumes one, not two, terminal capacities.

Conversely, if two coordinate roles must use distinct physical terminal
units and both are restricted to the same \(W\)-element q1 bank, the
terminal cut has capacity \(W\) against demand \(2W\).  No pair of
marginal perfect matchings can overcome that shared-capacity cut.

Therefore the remaining common-cap issue is no longer a one-coordinate
socket shortage.  It is exactly cross-coordinate capacity allocation or
coalescence, plus transported background and cap-state product closure.

## 8. Linear opening and exact scope

The cyclic theorem uses the wrap diamond.  A literal linear opening retains
all interior diamonds; any missing wrap ticket is one named boundary
obligation, not a \(W\)-scale bank.  Recovering it requires either one
priced boundary bundle or accepting one unit of terminal deficiency.

The theorem proves:

* a literal physical interval diamond at every cyclic q1 seam;
* two explicit full unit-capacity port-to-upper linkages;
* a private source-free owner-to-upper attachment;
* a complete owner-bypassing bundle representation;
* full one-coordinate suffix rank using the already present q1 upper bank;
  and
* the exact shared-bank dichotomy for two occurrence coordinates.

It does not prove:

* existence of a q1-exact diagonal carrier in every dimension;
* that an arbitrary terminal ticket accepts the upper-turn type;
* that two physical occurrence coordinates coalesce;
* transported phase 1, common-cap product closure, residence, deeper upper
  witnesses, or regeneration; or
* \(\nu(k)\le B(k)+O(1)\).

The new proof-safe interface is

\[
\boxed{
 \text{q1-exact literal diagonal}
 +\text{dual-role acceptance of its existing }q_i
 \Longrightarrow
 \text{full source-free one-coordinate terminal router}.}
\]
