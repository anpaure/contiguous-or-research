# Ideal Beneš routing of packet flags and the literal slab obstructions

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is
used.

## 0. Outcome

There is an exact positive routing theorem on the ideal recursive packet
tree.

Let \(n=2^k\).  Suppose every wire carries one indivisible packet/flag
bundle, and every ideal \(2\times2\) switch may send its two bundles
straight or crossed.  Then the recursive Beneš network with \(2k-1\)
switching stages routes every permutation of the \(n\) bundles.  More
generally, if input and prescribed output bundles carry types and the type
multiplicities agree, choose any type-respecting bijection and route it.
All nested lower/upper flags travel intact because the network never opens
a bundle.

If every ideal switch is also declared to have two exact owner shores
partitioning the same owner union, and switches within a stage are
owner-disjoint, every routed state preserves exact middle ownership.
This remains true stage by stage.

The literal \(Q_{R+1}\) cross-parent slab does **not**, however, implement
the ideal bundle switch.  If its old packets are

\[
 P_\alpha=\{x_e=\alpha\},\qquad \alpha\in\{0,1\},
\]

and its new packets are

\[
 Q_\beta=\{x_i=\beta\},\qquad \beta\in\{0,1\},
\]

then

\[
 \boxed{|P_\alpha\cap Q_\beta|=2^{R-1}={|P_\alpha|\over2}}
                                                               \tag{0.1}
\]

for all four pairs.  The normalized owner-transfer matrix is

\[
 \boxed{
 {1\over2}
 \begin{pmatrix}1&1\\1&1\end{pmatrix},}             \tag{0.2}
\]

not either \(2\times2\) permutation matrix.  A new packet contains half of
each old packet.  The slab is an exact change of cube foliation, not a
straight/cross transport of indivisible owner-attached bundles.

Consequently:

1. **Ideal positive theorem.** Arbitrary permutations of already grouped
   legal compiler bundles are routable on an ideal Beneš packet tree.
2. **Grouping qualification.** A globally balanced ownerwise nested-flag
   table is not enough.  It must first split into complete legal compiler
   packet columns.  Beneš routing permutes atoms; it does not manufacture
   the atoms.
3. **Literal no-lift for arbitrary bundles.** A single physical slab
   generally cuts both input bundles in half.  To lift an ideal switch,
   the four half-cube restrictions must glue into two legal compiler
   columns on the new packets.
4. **Switch-availability obstruction.** A Beneš stage requires a perfect
   matching of all current packet wires.  A legal cross-parent slab exists
   only for a common active \(R\)-set, a rank-preserving nonmatching pair,
   and the audited Hamming-two status change.  No recursive factorization
   of the physical compatibility graph into the Beneš matchings is proved.
5. **Frame and orientation obstruction.** A slab replaces one active
   direction \(i\) by \(e\).  Along every routed packet path these basis
   exchanges must be legal in their actual order and must end in the
   prescribed output frame and exterior orientation.
6. **Residue obstruction.** At scale \(r\), one switch has direction
   derivative

   \[
   2qg_r(e_e-e_i),\qquad g_r={2^r\over r}.           \tag{0.3}
   \]

   Across scales, a pure flag permutation must satisfy the weighted frame
   boundary

   \[
   \sum_a g_{r(a)}(e_{e_a}-e_{i_a})=0,              \tag{0.4}
   \]

   or the prescribed output boundary.  Even when this closes, the literal
   all-depth target residue can remain nonzero in the common
   direction-kernel and can create \(L^1\) holes.
7. **Common chronology obstruction.** The new slab packets accept a fresh
   diverse-order compiler, but the slab theorem supplies no canonical
   transport of an old compiler's nested phase flags to that new compiler.
   One option must work through every depth and both signs.

Thus the ideal rearrangeability theorem is proved, as is exact owner
preservation for any stage-aligned physical sequence.  What is not proved,
and is false for arbitrary owner-attached flag bundles, is a literal
Beneš lift.  The missing theorem is a **flag-compatible physical
switching network**: a recursive bank of stage-aligned slabs whose
half-cube compiler restrictions glue, whose pathwise frames close, and
whose literal \(L^1\) residue is \(o(W)\).

## 1. The ideal recursive packet network

An ideal wire carries one atom

\[
 \mathcal B_x=(P_x,\mathcal F_x),                   \tag{1.1}
\]

where \(P_x\) is a formal packet label and

\[
 \mathcal F_x
 =\bigl(\mathcal F_{x,q}^-,\mathcal F_{x,q}^+\bigr)_{q\le H}
                                                               \tag{1.2}
\]

is its complete nested compiler flag bundle.  The internal data in
\(\mathcal F_x\) are never separated.

An ideal \(2\times2\) switch has two states:

\[
 (A,B)\longmapsto(A,B)
 \quad\text{or}\quad
 (A,B)\longmapsto(B,A).                             \tag{1.3}
\]

Define the dyadic Beneš network \(\mathsf B_k\) recursively.

* \(\mathsf B_0\) is one wire.
* \(\mathsf B_1\) is one \(2\times2\) switch.
* For \(k\ge2\), the first stage pairs the \(2^k\) inputs, sends one wire
  of every pair into each of two copies of \(\mathsf B_{k-1}\), and the
  final stage pairs their outputs into the prescribed output pairs.

It has

\[
                         2k-1                     \tag{1.4}
\]

switching stages and

\[
 {2^k\over2}(2k-1)                                  \tag{1.5}
\]

switches.

## 2. Exact Beneš rearrangeability

### Theorem 2.1 (ideal packet-bundle rearrangeability)

For every permutation

\[
                         \pi:[2^k]\longrightarrow[2^k],         \tag{2.1}
\]

there is a setting of the switches of \(\mathsf B_k\) which sends the
bundle on input \(x\) to output \(\pi(x)\).

#### Proof

Proceed by induction on \(k\).  The cases \(k=0,1\) are immediate.

Group the input wires into pairs and the output wires into pairs.  Build a
bipartite multigraph \(G_\pi\):

* one left vertex for every input pair;
* one right vertex for every output pair;
* one edge for every input wire \(x\), joining its input-pair vertex to
  the output-pair vertex containing \(\pi(x)\).

Every vertex has degree two.  Hence every component of \(G_\pi\) is an
even cycle, including a doubled edge as a two-cycle.  Color the edges of
each component alternately red and blue.  Every input pair and every
output pair is incident with one edge of each color.

Set each first-stage switch so that its red bundle enters the upper
\(\mathsf B_{k-1}\) and its blue bundle enters the lower one.  Set each
last-stage switch so that the red and blue bundles leave for their
prescribed outputs.

The red edges define a bijection between the \(2^{k-1}\) upper input
positions and the \(2^{k-1}\) upper output positions.  The blue edges
define the analogous lower bijection.  Route these two permutations by
the induction hypothesis in the two copies of \(\mathsf B_{k-1}\).
Together with the first and last stages this routes \(\pi\). \(\square\)

### Corollary 2.2 (balanced typed bundles)

Suppose every input bundle and output demand has a type, and the input and
output multiplicities agree for every type.  Then all demands can be
met by the ideal network.

#### Proof

Choose an arbitrary bijection from input bundles to demands of the same
type, and apply Theorem 2.1. \(\square\)

A type may record an entire lower/upper nested compiler column.  Therefore
the theorem is simultaneous in every depth and sign.

### Theorem 2.3 (ideal Waksman rearrangeability for every \(n\))

For every \(n\ge1\), an unequal recursive Waksman packet network routes
every permutation of \(n\) indivisible bundles.

#### Proof

Pair all but possibly one input wire, and do the same at the output.
Given a requested permutation, form the bipartite multigraph between input
pairs and output pairs as in Theorem 2.1.  A paired vertex has degree two.
When \(n\) is odd, the unique input singleton and output singleton have
degree one.

If \(n\) is even, every component is an even cycle and its edges may be
colored alternately red and blue.

If \(n\) is odd, there is one path whose endpoints are the two degree-one
vertices, while every other component is an even cycle.  The path has odd
length because its endpoints lie on opposite sides.  Color it alternately
with both endpoint edges red, and color every cycle alternately.  Every
paired vertex again sees one edge of each color.  The red class has
\(\lceil n/2\rceil\) edges and contains both singleton wires; the blue
class has \(\lfloor n/2\rfloor\).

Set the first and last switches according to this coloring.  The red and
blue classes define permutations on subnetworks of sizes
\(\lceil n/2\rceil\) and \(\lfloor n/2\rfloor\), respectively.  Recurse.
The recursion terminates at \(n=1,2\). \(\square\)

### Grouping boundary

The theorem routes whole atoms.  It does not say that a balanced table of
individual owner flags is a multiset of legal atoms.  For example, two
input bundles may be respectively all red and all blue, while the desired
two output packets are each half red and half blue.  The individual color
counts are balanced, but no permutation of the two bundles realizes the
table.

Thus an arbitrary balanced nested-flag assignment is ideal-Beneš routable
at packet scale if and only if it first admits a partition into legal
whole compiler bundles with the prescribed output multiplicities.  This
is exactly the packet grouping gate, not a switching issue.

## 3. Exact ownership on an ideal physical layout

Call a physical switch layout **stage-aligned** if, at every stage and for
every switch setting reached before that stage:

1. the two current input packets of each switch are opposite facets of one
   legal \(Q_{r+1}\) slab;
2. switches in the stage have owner-disjoint slab supports; and
3. either shore of every slab is an exact partition of the same owner
   union.

### Proposition 3.1 (ownership survives every aligned route)

Every sequence of switch settings in a stage-aligned layout preserves
every middle owner exactly once.

#### Proof

At one switch, either shore partitions the same slab owner union.  Since
the switches in one stage are owner-disjoint, replacing any subset of
their shores preserves the union and multiplicity of all owners in that
stage.  Induct over the stages. \(\square\)

This is the genuinely positive physical part of the routing proposal.
Exact ownership does not require probabilistic repair, a reserve, or a
final matching once stage alignment has been proved.

The definition is stronger than the existing isolated slab theorem.  That
theorem proves one local switch when its two facets are present.  It does
not supply one fixed recursive bank in which every later stage remains
available under every earlier switch setting.

## 4. A physical slab is a foliation switch, not a bundle switch

Let the slab have coordinates \(D\cup\{e\}\), where \(|D|=R\), and choose
\(i\in D\).  Its old \(e\)-resolution is

\[
 P_0=\{x_e=0\},\qquad P_1=\{x_e=1\},                \tag{4.1}
\]

with active directions \(D\).  Its new \(i\)-resolution is

\[
 Q_0=\{x_i=0\},\qquad Q_1=\{x_i=1\},                \tag{4.2}
\]

with active directions

\[
                         D'=(D\setminus\{i\})\cup\{e\}.          \tag{4.3}
\]

For every \(\alpha,\beta\in\{0,1\}\),

\[
 P_\alpha\cap Q_\beta
 =\{x_e=\alpha,\ x_i=\beta\}\cong Q_{R-1}.          \tag{4.4}
\]

This proves (0.1)--(0.2).

### Theorem 4.1 (indivisible-bundle obstruction)

Attach one ownerwise constant label \(A\) to \(P_0\) and a different label
\(B\) to \(P_1\).  Under the new resolution, both \(Q_0\) and \(Q_1\)
contain exactly \(2^{R-1}\) owners labelled \(A\) and \(2^{R-1}\) owners
labelled \(B\).  Hence neither new packet carries either old bundle
intact.

In particular, the new shore realizes neither the straight nor the
crossed ideal state on arbitrary owner-attached bundles.

#### Proof

Use (4.4). \(\square\)

This does not contradict exact owner preservation.  No owner is lost or
duplicated; the owner partition is changed.

## 5. The half-cube compiler gluing condition

Let \(f_\alpha\) be the owner-resolved nested flag function on old packet
\(P_\alpha\).  If flags remain attached to their owners, the prospective
flag function on \(Q_\beta\) is forced to be

\[
 f_\beta^{\rm glue}
 =f_0|_{P_0\cap Q_\beta}
   \ \cup\
  f_1|_{P_1\cap Q_\beta}.                           \tag{5.1}
\]

Let \(\mathscr C(Q_\beta)\) be the finite catalogue of owner-resolved
nested flag functions supplied by legal diverse-order compiler conjugates
on \(Q_\beta\).

### Proposition 5.1 (exact local flag-lift criterion)

The physical slab transports the two old owner-attached flag tables to
legal new compiler packets if and only if

\[
                         f_\beta^{\rm glue}\in\mathscr C(Q_\beta)
 \qquad(\beta=0,1).                                  \tag{5.2}
\]

#### Proof

Equation (5.1) is forced owner by owner.  Membership in
\(\mathscr C(Q_\beta)\) is exactly the assertion that one legal compiler
state realizes that forced table on the entire new packet. \(\square\)

Nothing in the isolated slab theorem proves (5.2).  It says that an
arbitrary fresh compiler may be installed on each new packet, not that it
agrees with the old flags on the four half-cubes.

For arbitrary balanced nested-flag tables, (5.2) is false generically.
The old tables may use unrelated compiler conjugates, while a new packet
must be described by one conjugate on both of its halves.

If flags are allowed to be discarded and freshly chosen after every
re-resolution, (5.2) is unnecessary.  But then the construction is not
routing prescribed flag bundles; it is selecting a new packet atlas and
solving the target problem afterward.

## 6. Physical switch availability

The cross-parent slab theorem imposes the following local conditions.

1. The two old packets have one common active \(R\)-set \(D\).
2. Their special coordinates form a rank-preserving cross-half pair
   \(e=\{u,v\}\) which is not a current matching edge.
3. The two parent status labels differ in exactly the Hamming-two pattern
   \((1,0)\leftrightarrow(0,1)\).
4. The new shore freezes one actually active direction \(i\in D\).

Let \(\mathcal G_{\rm slab}\) be the graph whose vertices are current
packet slots and whose edges are compatible physical slabs.  A Beneš
stage requires a perfect matching of all current wires in
\(\mathcal G_{\rm slab}\), and successive stages require transverse
matchings after the preceding re-resolutions.

### Gate 6.1 (recursive switch-bank availability)

Prove that the physical packet family contains a stage-aligned recursive
subnetwork isomorphic to \(\mathsf B_k\), with \(k\to\infty\), while
leaving only \(o(W)\) owners outside it.

The isolated Hamming-two reachability theorem proves that
\(\mathcal G_{\rm slab}\) has some cross-parent edges.  It proves neither
a perfect matching nor the transverse recursive factorization in Gate
6.1.

Moreover, switches in different stages reuse owners.  Their settings need
not form a Cartesian cube: the next physical slab may cease to exist
after an earlier frame exchange.  A literal Beneš bank needs branchwise
availability under every setting used by the routing algorithm.

## 7. Frame, orientation, and pathwise monodromy

For a switch \(a\) at packet dimension \(r(a)\), orient the frame exchange
from the removed active direction \(i_a\) to the activated direction
\(e_a\).  At signed depth \(q\), its direction residue is

\[
 z_{a,q}^\epsilon
 =2qg_{r(a)}(e_{e_a}-e_{i_a}),
 \qquad g_r={2^r\over r}.                           \tag{7.1}
\]

Hence every compound route satisfies

\[
 {1\over q}z_q^-={1\over q}z_q^+
 =2\sum_ag_{r(a)}(e_{e_a}-e_{i_a}),                 \tag{7.2}
\]

independently of \(q\).

For a pure permutation of a fixed multiset of input flag bundles into
output slots with the same aggregate frame census, the right side must
vanish.  If output slots have prescribed different frames, it must equal
their frame boundary.  These are necessary aggregate conditions.

They are not sufficient.  Along each routed packet path:

* \(i_a\) must be active when it is removed;
* \(e_a\) must be inactive when it is activated;
* the ordered sequence of exchanges must end at that path's prescribed
  active \(R\)-set; and
* the frozen endpoint orientations must match the output slot.

Thus aggregate circulation can hide nontrivial pathwise frame monodromy.
The exact path state is an ordered basis together with its frozen
orientation word, not merely a vertex of the direction-count lattice.

At the literal target level, even zero aggregate direction residue leaves
a possible all-depth derivative

\[
 R_{\rm lit}
 \in\bigoplus_{q\le H,\epsilon=\pm}\ker\Pi_q^\epsilon.           \tag{7.3}
\]

For the authoritative \(L^1\) objective, this residue is harmless only if
its zero-to-positive and positive-to-zero threshold crossings have
aggregate \(o(W)\).  Direction closure alone does not imply this.

## 8. Nested chronology and orientation cylinders

One compiler option fixes a complete owner-resolved nested flag tower.
At one owner, the depth-\(q\) support is the prefix of one diverse order;
the lower and upper targets are coupled and use the same active
directions.

When a slab replaces \(i\) by \(e\):

* the old packets keep \(e\) frozen and visible in every literal target;
* the new packets keep \(i\) frozen and visible;
* \(e\) becomes a varied direction, hence is empty on the lower trace and
  full on the upper trace when it occurs in a window; and
* an old prefix containing \(i\) cannot be transported unchanged to a
  new active frame which omits \(i\).

Therefore an abstract route of support labels does not determine a route
of literal lower/upper flags.  The half-cube gluing condition (5.2) must
hold for the same compiler state at every depth and both signs.

This is stronger than separate depthwise support balance.  It is also
stronger than the aggregate residue closure (7.2).

## 9. Conditional literal lifting theorem

The ideal Beneš route lifts to a literal owner-exact nested-flag route if
the following four conditions hold.

1. **Grouping.** The desired assignment is a permutation of complete legal
   compiler packet bundles.
2. **Physical network.** There is a stage-aligned recursive slab bank
   realizing the ideal switch graph for every branch used.
3. **Local gluing.** At every active switch, the forced half-cube tables
   satisfy (5.2), with the requested straight/cross bundle action.
4. **Closure.** Every routed path ends in its prescribed frame and
   orientation, and the aggregate literal residue has \(o(W)\) harmful
   threshold crossings.

### Theorem 9.1 (conditional physical rearrangeability)

Under Conditions 1--4, every balanced prescribed output assignment of the
grouped bundles has a legal switch setting which preserves every middle
owner exactly once and realizes the prescribed common all-depth flags,
up to the declared \(o(W)\) literal residue.

#### Proof

Choose the type-respecting bundle permutation and route it by Theorem 2.1.
Condition 2 realizes every ideal switch as a physical stage while
Proposition 3.1 preserves exact ownership.  Condition 3 identifies the
ideal transported bundle at every physical output packet.  Induction over
the stages therefore transports the complete nested flags, not merely
their separate marginals.  Condition 4 gives the prescribed final slots
and the \(o(W)\) literal \(L^1\) error. \(\square\)

## 10. Exact boundary

Proved:

* exact Beneš rearrangeability for \(2^k\) ideal packet bundles;
* exact simultaneous routing of whole nested lower/upper flag atoms;
* exact middle-owner preservation for every stage-aligned physical
  resolution sequence;
* the rank-one half-and-half owner-transfer law (0.2);
* the exact half-cube compiler gluing criterion;
* the aggregate and pathwise frame/residue necessities; and
* a conditional literal lifting theorem.

Not proved:

* grouping an arbitrary balanced ownerwise flag assignment into legal
  compiler packet atoms;
* a positive-density recursive physical Beneš subnetwork;
* branchwise independence of overlapping slab settings;
* half-cube gluing for the actual diverse-order compiler catalogue;
* pathwise orientation/frame closure; or
* \(o(W)\) harmful literal residue for the final \(L^1\) target.

The ideal routing problem is closed.  The physical problem is not a local
descent problem and not a generic switching-network corollary.  It is a
flag-compatible recursive slab-bank theorem.
