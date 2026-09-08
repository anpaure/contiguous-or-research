# Spiral braids: the exact palette ledger and the missing voltage edge

Date: 2026-07-31  
Status: exact conditional connector theorem and sharp obstruction; no
all-dimension connector-existence claim

## 0. Verdict

Suppose an odd parent has (c) strict cyclic components and the even
(A/B) doubling produces (t=2c) cyclic blocks.  Then:

1. exactly (t-1=2c-1) physical seams are necessary and sufficient to
   turn chosen openings of the (t) blocks into one **linear path**;
2. preservation of both adjacent palettes is governed by one exact
   deletion--addition ledger, not by connectivity or co-orientation;
3. in a genuinely (H)-equivariant quotient, (t-1) seams form a tree
   after block contraction and therefore carry no closed voltage.  For
   (|H|>1), their lift has (|H|) components;
4. a unit-voltage connected lift using only (t-1) **new** seams is
   possible precisely when a protected old socket supplies the (t)-th
   connector (or some retained internal cycle already supplies the required
   monodromy); and
5. complement-paired period-three filters may be inserted without changing
   the voltage when they subdivide distinct sockets with the same endpoints
   and gain.  Complement pairing alone does not supply the missing socket.

This separates two constructions which should not be conflated.

* The authenticated K16 optimum uses three literal symmetry-breaking seams
  to join four already physical strict spirals into a **path**.  Its final
  wrap is not a Johnson edge, so it makes no equivariant unit-voltage-cycle
  claim.
* The authenticated (m=4) construction has a genuine quotient connector
  **cycle** of voltage (2pmod 7).  That extra closing connector is what
  makes its physical lift connected.

The strongest general connector lemma available from these data is thus a
palette-labelled, unit-voltage socket theorem.  It is stated below.

## 1. The two palettes

Let the middle vertices be the (r)-sets of a (2r)-element ground set.
For a Johnson edge (e=XY), put

\[
             \lambda(e)=X\cap Y,\qquad \mu(e)=X\cup Y .       \tag{1.1}
\]

These are respectively its lower and upper colours.  Let
(C_1,ldots,C_t) be pairwise vertex-disjoint cyclic Johnson components,
and let (L_0^-(a)), (L_0^+(b)) be the lower and upper colour loads in
their union.

Choose one oriented closure edge

\[
                  d_i=y_i x_i\in E(C_i)                       \tag{1.2}
\]

from every component.  Deleting (d_i) gives an oriented path (P_i)
from (x_i) to (y_i).  For a permutation
((i_1,ldots,i_t)), a physical seam is a Johnson edge

\[
                  s_j=y_{i_j}x_{i_{j+1}}\qquad(1\le j<t).     \tag{1.3}
\]

Write (D^pm) and (S^pm) for the colour multiplicities of the deleted
closures and inserted seams.

### Lemma 1.1 (exact physical braid and palette ledger)

The graph

\[
       \bigcup_i(C_i-d_i)\ \cup\ \{s_1,\ldots,s_{t-1}\}       \tag{1.4}
\]

is one Hamilton path on the block vertices.  Conversely, any construction
which opens every (C_i) once and joins the resulting paths without using
additional vertices needs at least (t-1) cross-block seams; equality
forces the contracted seam graph to be a tree, and a Hamilton path forces
that tree to be a path.

Its two palette loads are exactly

\[
 \boxed{
 L^-(a)=L_0^-(a)-D^-(a)+S^-(a),\qquad
 L^+(b)=L_0^+(b)-D^+(b)+S^+(b).}                       \tag{1.5}
\]

Consequently it preserves both palettes if and only if

\[
       L_0^-(a)-D^-(a)+S^-(a)\ge1\quad\hbox{for every }a,
                                                                    \tag{1.6}
\]

and the analogous inequality holds for every upper colour (b).

#### Proof

Deleting one edge from each disjoint cycle gives (t) disjoint paths.
Every cross-block edge can reduce the component count by at most one, so
(t-1) are necessary.  The seams (1.3) concatenate the paths in the
displayed order and are sufficient.  Colour loads change only on the
deleted and inserted edges, which proves (1.5) and (1.6).  \(\square\)

Thus "Johnson connector" and "palette-safe connector" are different
conditions.  Co-orientation does not bridge that gap.

### Corollary 1.2 (redundant-opening and exact-compensation forms)

Either of the following is sufficient for (1.6).

1. Every deleted closure colour has old load at least two on both shores.
   Then the seams may repeat arbitrary colours.
2. Every colour made deficient by the deletions occurs among the seams on
   the same shore.

The second condition is also necessary.  In particular, if
(Delta^-) and (Delta^+) are the lower and upper deficit sets after
deletion, then

\[
                  |\Delta^-|\le t-1,\qquad
                  |\Delta^+|\le t-1                              \tag{1.7}
\]

is necessary.  It is not sufficient: the same (t-1) occurrence-labelled
seams must simultaneously form the block path and cover both deficit sets.

This is the exact finite connector problem exposed by K16.

## 2. What complement pairing buys, and what it cannot buy

Let (iota(X)=\overline X).  Complementation sends a Johnson edge (e)
to a Johnson edge (iota e), and

\[
       \lambda(\iota e)=\overline{\mu(e)},\qquad
       \mu(\iota e)=\overline{\lambda(e)}.                \tag{2.1}
\]

Hence, if the closed block bank, deleted closures and inserted connectors
are all complement-paired, the upper equation in (1.6) is exactly the
complement of the lower equation.  In that special case it is enough to
check one palette.

There is, however, an unavoidable parity defect.

### Lemma 2.1 (odd-seam complement obstruction)

Assume (r>1).  Complementation has no fixed Johnson edge.  More generally,
let an odd cyclic group (H) act freely on occurrence-labelled edge
orbits and commute with complementation.  Then no (H)-edge orbit is
self-complementary.  Therefore a bank of (2c-1) seam occurrences or
clean-(H) seam orbits cannot be entirely complement-paired.

#### Proof

A fixed edge would have endpoints (X,\overline X), which are not Johnson
adjacent when (r>1).  If an (H)-orbit of an occurrence (e) were
self-complementary, then

\[
                         \iota e=g e
\]

for some (g\in H).  Since (iota) commutes with (H), applying it twice
gives (e=g^2e).  Freeness and oddness imply (g=1), hence
(iota e=e), already excluded.  Thus complement acts without fixed
points on the seam orbits, which must occur in pairs.  An odd bank cannot
be such a union.  \(\square\)

So an (A/B)-doubled linear braid necessarily contains at least one
symmetry-breaking seam.  Complement-paired period-three filters can make
the exceptional palette ledger neutral, but cannot remove this final odd
port.

## 3. Strict spirals and co-orientation

Let (R) generate a cyclic action of order (q).  A strict spiral block
has the form

\[
 \operatorname{Sp}(P,a)=P\Vert R^aP\Vert\cdots\Vert R^{(q-1)a}P,
 \qquad \gcd(a,q)=1.                                  \tag{3.1}
\]

Reversal changes (a) to (-a) without changing the undirected internal
edge set.  Consequently (t) doubled blocks can all be co-oriented by
anchored reversals whenever their voltages lie in

\[
                            \{a,-a\}                         \tag{3.2}
\]

for one unit (a).  This is exactly the K16 situation, where the natural
signs ((-4,+4,+4,-4)) become ((+4,+4,+4,+4)).

Co-orientation gives a common sheet order and reduces connector search to
phase choices and openings.  It does **not** imply any of the Johnson or
palette conditions (1.3), (1.6).  The exact restricted search object is
therefore the occurrence-labelled digraph whose vertices are oriented,
phase-shifted opened blocks and whose arcs are legal Johnson seams labelled
by their two colours and voltage.

A (2c-1)-seam physical braid is precisely a directed Hamilton path in
this digraph satisfying the two ledger inequalities (1.6).

## 4. The clean-(H) voltage obstruction

Let (H\cong\mathbb Z_h) act freely on all occurrence-labelled paths,
ports and connector edges.  Suppose the construction is (H)-invariant,
so it has a genuine voltage quotient.  Gauge every quotient path
(P_i) with internal gain (r_i), and let a connector from the exit of
(P_i) to the entry of (P_j) have gain (delta_{ij}).

### Lemma 4.1 (the missing voltage edge)

If (t) quotient paths are joined by only (t-1) connector orbits into
one quotient path, its physical lift is the disjoint union of (h) paths.
In particular, for (h>1), no choice of the (t-1) connector gains can
make the lift connected.

#### Proof

The contracted quotient is a tree.  A voltage assignment on a tree is a
coboundary: choose a root and gauge each successive vertex so that every
tree-edge gain becomes zero.  The lift is therefore one identical tree in
each of the (h) sheets, with no edge between sheets.  \(\square\)

This is sharp.  Add one closing connector (e_*), so that the contracted
quotient is one directed cycle.  If the cyclic order is
(P_1,ldots,P_t), with connector gains (delta_1,ldots,delta_t), its
net voltage is

\[
                   V=\sum_{i=1}^t(r_i+\delta_i)\pmod h.       \tag{4.1}
\]

The lift has exactly (gcd(h,V)) components and is connected exactly when

\[
                              \gcd(h,V)=1.                    \tag{4.2}
\]

Thus a connected clean-(H) lift with only (t-1) **new** seams requires
a protected pre-existing closing socket (e_*), or an equivalent retained
closed walk whose voltage together with the new seams generates (H).

The qualification "clean-(H)" is essential.  K16 opens four full
physical spirals at four individual representatives and inserts three
individual connectors.  Those openings break (H)-invariance, so Lemma
4.1 does not obstruct the resulting physical Hamilton path.  It does rule
out interpreting those same three seams as an invariant unit-voltage
quotient closure.

## 5. Palette-safe unit-voltage socket theorem

The preceding identities combine into the strongest general sufficient
lemma supported by the current constructions.

### Theorem 5.1 (protected-socket spiral braid)

Let (t=2c).  Assume:

1. **Blocks.**  There are (t) pairwise vertex-disjoint opened quotient
   paths (P_i), obtained from the (A/B) doubles of (c) strict cyclic
   parent components.  Their occurrence states and ports are free under an
   odd clean cyclic group (H\cong\mathbb Z_h).  The skeleton paths cover
   every nonfilter occurrence, and together with the packet occurrences in
   Condition 6 their (H)-developments partition the full middle layer.
2. **Orientation and phase.**  Their strict voltages lie in
   ({a,-a}) for one unit (a), and reversals/phases have been selected.
3. **Topology.**  There are (t-1) new, pairwise port-disjoint Johnson
   seams
   (y_i x_{i+1}), together with one protected Johnson socket
   (e_*=y_t x_1).  These form one directed quotient cycle.
4. **Palettes.**  After accounting for every opened closure, the new seams
   and (e_*), the exact inequalities (1.6) hold on both shores.
5. **Voltage.**  The total (V) in (4.1) is a unit modulo (h).
6. **Filters.**  Every period-three exceptional filter is realized by a
   vertex-disjoint complement-paired packet.  The packet and bulk internal
   selected edges partition the two distinguished palettes.  Each packet
   is either already one of the (P_i), or replaces a distinct socket by
   a path with the same physical endpoints and the same gain; all its
   internal resources are private.

Then the quotient selected graph is one cycle, its physical (H)-lift is
one Hamilton cycle, and both adjacent palettes are complete.  If the
internal packet/bulk edges form a distinguished exact common transversal,
that transversal remains exact even when connector colours repeat.

Deleting the protected socket (e_*) leaves one physical Hamilton path
joined by exactly (2c-1) new seams.  Its palette remains complete exactly
when the ledger (1.6) remains true after that final deletion.

#### Proof

Conditions 1 and 3 give a connected degree-two quotient graph.  Condition
5 and the cyclic voltage-cover theorem give one physical component, hence
one Hamilton cycle.  The load identity (1.5) and Condition 4 give both
palette covers.  A filter socket replacement preserves topology because
it subdivides one cycle edge by a disjoint path, and preserves voltage
because its endpoint gain equals the removed socket gain.  Its private,
complement-paired internal transversal supplies precisely the reserved
lower and upper colours, while the bulk supplies the rest.  Simultaneous
replacement at distinct sockets therefore preserves all conclusions.
Deleting (e_*) opens the cycle into a path; applying (1.5) once more gives
the final assertion.  \(\square\)

### Corollary 5.2 (neutral Hall form)

Gauge the protected cycle so that (e_*) carries the unit voltage and all
other skeleton sockets have gain zero.  Form the compatibility graph
between complement-paired filter packets and occurrence-labelled zero-gain
sockets.  Join a packet to a socket when some orientation and phase gives a
literal endpoint-preserving, palette-private path.

If this graph has a matching saturating the filter packets, then Condition
6 of Theorem 5.1 holds automatically and the total voltage stays that of
(e_*).  This is the period-three neutral-connector theorem in the
(2c)-block spiral language.

Hall's condition here does not produce the initial (2c)-block skeleton,
nor does it prove the palette ledger for the nonfilter seams.

## 6. Exact calibrations

### 6.1 K16

The authenticated K15 parent has (c=2) strict cycles.  Its (A/B)
double gives four strict (mathbb Z_{15})-spirals of base lengths

\[
                         426,426,3,3,
\]

all co-oriented to voltage (+4).  Three Johnson seams join them into one
linear rank-eight path, and direct replay verifies (1.6) on both shores.
The fourth wrap has symmetric difference six, not two.  Therefore K16 is
an exact instance of Lemma 1.1, but **not** of the unit-voltage cycle in
Theorem 5.1.  Its four selected openings/connectors are literal symmetry
defects, as Lemma 2.1 predicts.

### 6.2 The physical (m=4) lift

The (m=4), (mathbb Z_7)-equivariant common-transversal forest has two
quotient paths.  Its connector quotient is a two-cycle with gains
((3,6)) or ((5,4)), in either case total voltage

\[
                              2\pmod7.
\]

The lift is therefore connected.  The internal forest already uses every
lower and upper colour exactly once, so connector-colour repetitions are
harmless.  This is the protected-socket/unit-voltage side of Theorem 5.1,
not the three-seam K16 side.

### 6.3 Period-three filters

At the maximal clean subgroup (H), the canonical complement-paired
period-three packets are vertex-disjoint, internally voltage-zero and exact
on the exceptional palettes.  They meet Condition 6 once a complementary
bulk forest and a saturating neutral socket matching exist.  The packets
do not themselves prove either of those two global objects.

## 7. Sharp remaining gate

Within the strict (A/B)-doubled architecture, the remaining theorem is
now exactly the following finite statement.

> After choosing one opening, orientation and phase for each of the
> (2c) strict blocks, the occurrence-labelled connector digraph contains
> a directed Hamilton path whose (2c-1) labels satisfy both palette
> ledgers.  For a clean-(H) connected lift, this path must extend through
> a protected socket to a directed cycle of unit total voltage.  Every
> period-three packet must have a private neutral socket assignment.

Nothing in strictness, co-orientation, complement pairing or the scalar
component count proves this statement.  The odd-seam obstruction and the
tree-voltage obstruction show that some symmetry breaking or one protected
unit-voltage socket is genuinely unavoidable.

## 8. Inputs used

The finite and general ingredients reconciled here are:

* `MATH_THEOREM_K16_THREE_PRIMARY_SPIRAL_BRAID_ANATOMY_20260731.md`;
* `MATH_THEOREM_CATALAN_M4_Z7_PHYSICAL_LIFT_AND_CONNECTOR_VOLTAGE_20260731.md`;
* `MATH_THEOREM_CATALAN_PERIOD3_FILTER_PACKET_AND_NEUTRAL_CONNECTOR_20260731.md`;
* `MATH_AUDIT_CATALAN_PERIOD3_FILTER_SECTIONS_AND_PORT_VOLTAGE_20260731.md`.
