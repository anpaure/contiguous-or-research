# Lane AD: graded zero creators and the Hall-22 creator--splitter boundary

Date: 2026-07-28

Status: exact native-depth classification of all six Hall-22 zero roots;
exact local distance-one controller charts; exact maximum-matching freeness
audit; exact creator--splitter normal forms; and an exact one-braid net-creator
no-go.  No physical Hall-21 or zero-five descendant is constructed.  A
remote controller-changing macro of braid length at least two remains open.

## 0. Result and corrected boundary

Work throughout with the authoritative carrier

    scratch/k15_segment_braid_hall22_zero6.json

of SHA-256

    bb3f8b922e7e741329c4cff551363a9bc244a4c77dcc1fd70d6accc7b8c91778.

Its compiler graph has matching number (16361), Hall deficiency (22),
canonical deficient shore (1006/984), and zero set

\[
 Z=\{5801,13616,13620,17738,21641,29776\}.
\tag{0.1}
\]

The grading correction is decisive.  Here the middle rank is (r=8) and
the residence depth is (d=3), so an interior native compiler cell of depth
(e\in\{0,1,2\}) has rank

\[
 r-d+e=5+e.
\tag{0.2}
\]

Consequently a target of rank (s) can be native only at depth

\[
 e=s-(r-d)=s-5.
\tag{0.3}
\]

In particular, the proposed depth-zero change

\[
 \text{cell }5617:\quad2574\longmapsto2575
\tag{0.4}
\]

cannot occur in an interior resident controller: (2575) has rank six and
therefore requires a depth-one native cell.  The existing cell (17342),
whose native trace is the rank-seven target (2607), must remain depth two.
The only grade-compatible native split of the circuit

\[
 \{2575,2607\}/\{17342\}
\tag{0.5}
\]

uses two distinct cells: a depth-one native (2575) cell and a depth-two
native (2607) cell.

For the six actual zeros, the exact depth list is

\[
\begin{array}{c|c|c|l}
S&|S|&\text{required depth}&\text{zero-based coordinates of }S\\ \hline
5801&7&2&0,3,5,7,9,10,12\\
13616&6&1&4,5,8,10,12,13\\
13620&7&2&2,4,5,8,10,12,13\\
17738&6&1&1,3,6,8,10,14\\
21641&6&1&0,3,7,10,12,14\\
29776&6&1&4,6,10,12,13,14.
\end{array}
\tag{0.6}
\]

Thus there are four depth-one creator problems and two depth-two creator
problems.  Searching across depths is both wasteful and logically invalid:
only the row prescribed by (0.3) can produce a native target.

The strongest positive static fact is that every (S\in Z) is one Johnson
swap and one local controller-letter substitution from some current
grade-compatible native trace.  The strongest negative static fact is that,
relative to the frozen graph, the two rank-seven zeros have no currently
unmatched Hamming-distance-two depth-two address.  For (13620), none of
its 56 Hamming-distance-two addresses can even be freed by changing the
maximum matching.
These are controller-local and matching-static statements, not physical
braid certificates.

## 1. Native grading

Let (T_0,T_1,\ldots) be a rank-(r) Johnson path with residence depth
(d).  At an unclipped controller position put

\[
 P_j=\bigcap_{i=j-d}^{j}T_i.
\tag{1.1}
\]

A depth-(e) compiler cell beginning at (a) has native trace

\[
 N(a,e)=P_a\cup P_{a+1}\cup\cdots\cup P_{a+e}.
\tag{1.2}
\]

### Theorem 1.1 (native grading)

At every fully interior position and for (0\le e<d),

\[
 |P_j|=r-d,
 \qquad
 |N(j,e)|=r-d+e.
\tag{1.3}
\]

Hence an interior target of rank (s\in\{r-d,\ldots,r-1\}) is native only
at depth (s-(r-d)).

#### Proof

Write

\[
 T_{i+1}=T_i-\{a_i\}+\{b_i\}.
\tag{1.4}
\]

The (d) deletions in the window defining (P_j) are distinct.  If a
coordinate were deleted twice, it would have
to re-enter between the two deletions, producing an internal positive run
of length at most (d), contrary to depth-(d) residence.  Therefore the
intersection loses exactly (d) elements from a rank-(r) owner, proving
(|P_j|=r-d).

When the controller window advances by one place, residence gives the exact
identity

\[
 P_{j+1}=P_j-\{a_j\}+\{b_{j-d}\}.
\tag{1.5}
\]

The incoming coordinates (b_{j-d},\ldots,b_{j-d+e-1}) are distinct and
are absent from the union of the preceding controller letters, again by the
run-length condition.  Thus (P_j,P_{j+1}) are adjacent rank-((r-d))
Johnson vertices, and each of the first (e) forward steps adds one new
coordinate to the union.  Starting with (r-d) coordinates gives
(|N(j,e)|=r-d+e).  This proves (1.3).  \(\square\)

The unclipped hypothesis matters.  Boundary controller intersections use
fewer than (d+1) middle owners and must be graded separately.  Every cell
used below begins between positions 2233 and 5180 and is therefore fully
interior.

## 2. Exact local controller distance

Fix a grade-compatible depth-(e) cell (I=[a,a+e]), write

\[
 \mathbf P_I=(P_a,\ldots,P_{a+e}),
 \qquad N_I=\bigcup_{j\in I}P_j,
\tag{2.1}
\]

and let (S) have the same rank as (N_I).  Define

\[
 h_I(S)=|N_I\mathbin\triangle S|,
 \qquad
 c_I(S)=\sum_{j\in I}|P_j\setminus S|.
\tag{2.2}
\]

Here (h_I/2) is the Johnson distance between the two traces, while
(c_I) is the number of forbidden coordinate occurrences that must be
removed from the controller tuple before its union can equal (S).

### Lemma 2.1 (local substitution lower bound)

Any alteration of the letters of (mathbf P_I) into rank-((r-d)) subsets
of (S) whose union is (S) uses at least (c_I(S)) one-coordinate letter
substitutions.  If (N_I\ne S) and (|N_I|=|S|), then (h_I(S)\ge2).

#### Proof

Every occurrence of every coordinate in (P_j\setminus S) must be removed
from that particular letter, giving the first lower bound after summing over
(j\in I).  Distinct equal-cardinality sets cannot differ in one bit, so
their symmetric difference has size at least two.  \(\square\)

Because every member of (Z) has degree zero, no current compiler cell has
native trace (S\in Z): a native trace is automatically a legal target of
its own cell.  Thus Lemma 2.1 gives the universal lower bounds

\[
 h_I(S)\ge2,
 \qquad c_I(S)\ge1
\tag{2.3}
\]

for every prospective current-to-native portal.

### Theorem 2.2 (all six local lower bounds are attained)

For each zero target (S), the current controller contains a cell outside
the 984-cell canonical DM-right shore with the required depth, trace
distance (h_I(S)=2), and controller cost (c_I(S)=1).  One exact choice
for each target is displayed below.  The arrow in the last column replaces
the unique forbidden coordinate occurrence and gives a tuple of rank-five
sets with Johnson-adjacent consecutive letters and union exactly (S).

\[
\begin{array}{c|c|c|c|c|l}
S&\text{cell}&e/a&N_I&\mathbf P_I&\text{one-letter native tuple}\\ \hline
5801&17772&2/4897&6825&(2697,681,4265)&
 2697\to1673\ (11\to10)\\
13616&11240&1/4802&12720&(12464,12592)&
 12464\to13360\ (7\to10)\\
13620&17678&2/4803&14128&(12592,12848,13360)&
 12848\to12340\ (9\to2)\\
17738&10937&1/4499&20810&(20808,16714)&
 20808\to17736\ (12\to10)\\
21641&10521&1/4083&22152&(21640,21128)&
 21128\to20617\ (9\to0)\\
29776&10933&1/4495&21616&(5232,21584)&
 5232\to13392\ (5\to13).
\end{array}
\tag{2.4}
\]

The parenthetical coordinates in (2.4) are zero-based.  Direct unions give
the target in every row, and the consecutive symmetric differences remain
two.  For example,

\[
 (12592,12848,13360)
 \longmapsto
 (12592,12340,13360)
\tag{2.5}
\]

has union (13620) and both adjacent Hamming distances equal two.  Thus the
lower bounds (2.3) are exact for all six targets.  \(\square\)

These choices are the unique (c_I=1) cells closest in start position to
the existing portal start 4467.  In every row the current mandatory mask has

\[
 F_I\setminus S=\{\text{the displayed outgoing coordinate}\}.
\tag{2.6}
\]

Thus none is already a compiler edge to (S).  A physical route must change
the carrier/mandatory ledger as well as the native trace.  Moreover, if only
the displayed controller letter is changed and its two exterior neighbours
are frozen, the left/right exterior XOR weights are respectively

\[
 (4,2),(2,2),(2,2),(4,2),(2,4),(4,2)
\tag{2.7}
\]

in the row order of (2.4).  Only the (13616) and (13620) substitutions
remain Johnson-adjacent on both exterior sides without moving neighbouring
controller letters.

This theorem is deliberately local.  It does **not** assert that the changed
tuple extends to a maximal erosion controller.  Its two exterior Johnson
edges, the middle-owner deck, depth-three residence, upper shadows, lower
support, and retained matching must all be restored by an actual carrier
move.

## 3. Three distinct meanings of “free”

The free-cell proposal is ambiguous unless a matching is fixed.

1. A cell is **DM-atlas-free** if it is outside the 984-cell canonical
   DM-right shore.  Every cell in (2.4) is DM-atlas-free.  This says nothing
   about exterior matching service.
2. Given the deterministic maximum matching (M_0) returned by the exact
   auditor, a cell is **(M_0)-unmatched** if no edge of (M_0) uses it.
3. A cell is **maximum-matching-freeable** if some maximum matching of the
   current graph leaves it unmatched.

The third notion is invariant under the initial choice of maximum matching.

### Lemma 3.1 (alternating criterion for freeability)

Let (c) be a right vertex of a bipartite graph and (M) a maximum
matching.  If (c) is (M)-matched, then some maximum matching leaves (c)
unmatched if and only if an (M)-alternating path starts at (c) with its
matched edge and ends at an (M)-unmatched right vertex.

#### Proof

Flipping such an even alternating path preserves cardinality, matches its
formerly unmatched right endpoint, and frees (c).  Conversely, if (M')
is maximum and frees (c), the component of (M\mathbin\triangle M'))
containing (c) is an even alternating path whose other endpoint is a right
vertex unmatched by (M).  \(\square\)

### Theorem 3.2 (exact minimum-controller-cost freeness census)

Restrict first to the cells attaining both local minima

\[
 h_I(S)=2,
 \qquad c_I(S)=1.
\tag{3.1}
\]

Their exact counts are

\[
\begin{array}{c|c|c|c}
S&\text{minimum-cost cells}&M_0\text{-unmatched}&
 \text{maximum-matching-freeable}\\ \hline
5801&19&0&0\\
13616&40&12&23\\
13620&24&0&0\\
17738&38&9&22\\
21641&42&14&27\\
29776&48&17&36.
\end{array}
\tag{3.2}
\]

All six cells in (2.4) are outside the canonical DM-right shore.  Only cell
11240 is (M_0)-unmatched, but all four displayed rank-six cells are
maximum-matching-freeable.  For the other three, one-edge native rematches
are

\[
 20810:10937\to12097,
 \qquad22152:10521\to12378,
 \qquad21616:10933\to12577.
\tag{3.3}
\]

Both displayed rank-seven cells are forced in every maximum matching:
deleting either lowers the matching rank from 16361 to 16360.

If the controller-cost-one restriction is dropped while Hamming distance
two is retained, each rank-seven zero has 56 grade-compatible cells, and
neither has an (M_0)-unmatched one.  For (5801), the unique freeable
distance-two cell is

\[
 \begin{array}{c|c|c|c}
 \text{cell}&\text{start}&N_I&\mathbf P_I\\ \hline
 15108&2233&9897&(8865,8872,9384).
 \end{array}
\tag{3.4}
\]

It can be freed by the exact alternating right-cell chain

\[
15108\;\xleftrightarrow{9897}\;12875
 \;\xleftrightarrow{9773}\;15355,
\tag{3.5}
\]

where cell 15355 is (M_0)-unmatched.  Replacing coordinate 13 by coordinate
12 in all three letters of (3.4) gives

\[
 (4769,4776,5288)
\tag{3.6}
\]

with union (5801); its local controller cost is three, not one.

For (13620), every one of its 56 distance-two cells is matched in every
maximum matching of the current graph.  The (M_0)-unmatched native
depth-two cells are exactly

\[
\begin{array}{c|c|c}
\text{cell}&\text{start}&N_I\\ \hline
15355&2480&9773\\
17460&4585&12685\\
17963&5088&3868\\
19187&6312&17140.
\end{array}
\tag{3.7}
\]

The nearest already-unmatched portal to (5801) is cell 15355, at Hamming
distance four and exact local controller cost three.  One internally legal
target tuple is

\[
 (8741,8745,1577)\longmapsto(4769,4649,1577).
\tag{3.8}
\]

The nearest already-unmatched portal to (13620) is cell 17963, at Hamming
distance six and exact local controller cost five.  One internally legal
target tuple is

\[
 (3604,3348,3352)\longmapsto(13332,9492,9520).
\tag{3.9}
\]

The census is obtained from the full exact current compiler graph, and
freeability is then certified by Lemma 3.1.  It is static: changing the
controller changes the incidence graph itself.  In particular, the
nonfreeability of the 56 current addresses for (13620) does not rule out a
remote braid which creates a new edge while simultaneously rerouting other
service.

## 4. Exact creator--splitter normal forms

Let (G=(L,R;E)) have maximum matching (M), and suppose (z\in L) is
exposed.

### Theorem 4.1 (clean native ear)

Suppose a final physical controller has an unused cell (c\in R) of the
grade prescribed by (0.3), with native trace (z), and every edge of (M)
remains a valid, cell-disjoint literal pin in that same final word.  Then

\[
 M\cup\{zc\}
\tag{4.1}
\]

is a matching of size (|M|+1).  If a retained shore has gap one less than
the old deficiency, the new deficiency is exactly one less.

#### Proof

Nativeness makes (zc) a literal compiler edge.  The target (z) and cell
(c) are unused by (M), so adjoining it gives (4.1).  The retained shore
gives the reverse Hall inequality.  \(\square\)

### Theorem 4.2 (root transfer followed by a splitter)

Suppose a new edge (zc) appears but (c) is matched by (M) to (y).
Replacing (yc) by (zc) preserves matching size and transfers the exposed
root from (z) to (y).  A later distinct unused cell (c') adjacent to
(y), with all other pins retained, increases the matching size by one.

#### Proof

The first exchange is a length-two alternating flip.  It leaves exactly
(y) exposed in place of (z).  Since (c') is distinct and unused,
adjoining (yc') then augments the matching.  \(\square\)

This is the precise creator--then--splitter normal form.  A creator alone may
remove one old zero while creating a replacement zero; only the second cell
produces net Hall gain.

### Theorem 4.3 (forced-cell deletion tests)

Let the old maximum size be \(N\), and let \(G'\) be a proposed final
compiler graph.

1. A forced clean ear \(zc\) belongs to a matching of size \(N+1\) if and
   only if

   \[
   \nu\bigl(G'-\{\text{target }z,\text{ cell }c\}\bigr)\ge N.
   \tag{4.2}
   \]

2. For distinct targets \(z,y\) and distinct forced cells \(c_z,c_y\), the
   two forced pins belong to a matching of size \(N+1\) if and only if they
   form an SDR and

   \[
   \nu\bigl(G'-\{\text{targets }z,y,\text{ cells }c_z,c_y\}\bigr)
   \ge N-1.
   \tag{4.3}
   \]

#### Proof

For (4.2), delete the forced edge from a size-\((N+1)\) matching to obtain
the residual size-\(N\) matching; conversely adjoin the forced edge to such a
residual matching.  The proof of (4.3) is identical after deleting or
adjoining the two forced edges.  \(\square\)

For the current \(\{2575,2607\}/\{17342\}\) circuit, deleting the two targets
and cell 17342 leaves exact residual matching rank \(16360\).  Thus a final
graded split needs a depth-one \(2575\) cell, a distinct depth-two \(2607\)
cell, and residual rank at least \(16360\); those data give rank \(16362\)
and Hall deficiency at most 21.  A retained gap-21 shore would make the
deficiency exactly 21.

### Corollary 4.4 (graded two-cell rule)

Two distinct targets of different ranks cannot be served by one literal
interval, and their native cells have different forced depths.  In
particular:

* the circuit ({2575,2607}) requires a depth-one native (2575) interval
  and a distinct depth-two native (2607) interval;
* the nested zero pair
  (13616\subset13620=13616\cup\{2\}) requires a depth-one native (13616)
  interval and a distinct depth-two native (13620) interval for a
  simultaneous native discharge.

Necessity follows because one interval has one OR value and from Theorem
1.1.  The two unused native intervals are sufficient if the exterior literal
matching is retained, by applying Theorem 4.1 twice.

An exceptional pin of a depth-two (13620) envelope down to (13616) may
create a root transfer, but it cannot serve both targets simultaneously.  It
therefore does not evade the two-cell rule.

## 5. Literal common-controller conditions

“Native” is useful only after one final controller has been fixed.  If the
final controller contains distinct unused intervals of native traces
(S_1,\ldots,S_t), those intervals simultaneously realize their targets.
However, a controller-changing braid can alter every old pin which crosses a
changed collar.  A clean-ear application therefore needs all of the
following in one final state:

1. the middle-owner deck and Johnson chronology;
2. depth-three residence;
3. all protected lower and upper supports;
4. target- and cell-disjoint new intervals of the forced depths;
5. a retained exterior matching, or an explicit alternating reroute; and
6. one common physical word realizing every retained pin and new native
   interval.

For an exceptional pin of an interval (I) with envelope (E) down to
(K\subset E), the coordinate-survival ledger is exact:

\[
 Q'_x=Q_x\setminus I\quad(x\in E\setminus K),
 \qquad Q'_x=Q_x\quad(x\notin E\setminus K).
\tag{5.1}
\]

Every retained interval requiring a deleted coordinate must still meet its
new (Q'_x).  For the certified exceptional rebase of cell 17342 from 2607
to 2575, only zero-based coordinate 5 is deleted on positions
([4467,4469]).  It serves 2575 but displaces 2607, leaving 984 critical-
shore pins and Hall deficiency 22.  Thus ordinary reachability and static
matching freeness are not common-(Q) certificates.

## 6. Exact finite no-go and shortest-route consequences

The complete resident, all-upper-safe one-braid catalogue from the six-zero
carrier has the exact filter counts

\[
 551095\longrightarrow11927\longrightarrow9073.
\tag{6.1}
\]

Every surviving `FF`, `RF`, `FR`, or `RR` endpoint has

\[
 h\ge22,
 \qquad z\ge6.
\tag{6.2}
\]

Its exact zero marginal is

\[
 7274u^6+320u^7+1203u^8+243u^9+31u^{10}+2u^{11}.
\tag{6.3}
\]

The scanner and log hashes are respectively

    889379685f55e1938f24fceffd889951332966fe547021874b5482b1c2fa7d29
    041e7a718e15ff8e95e614ea561492c4e8ac6526cf79f9d7eb886194a20f0a51.

### Theorem 6.1 (one-braid net-creator obstruction)

No safe one-braid endpoint has Hall deficiency 21 or five zeros.  More
sharply, if (A) is the set of old zeros which gain incidence and (B) the
set of new zero targets, then

\[
 |B|\ge |A|.
\tag{6.4}
\]

#### Proof

Equation (6.2) is the full exact catalogue statement.  Since the initial
zero set has size six, the endpoint has

\[
 z'=6-|A|+|B|.
\tag{6.5}
\]

The inequality (z'\ge6) is equivalent to (6.4).  \(\square\)

Thus a one-braid raw creator is not excluded, but it must steal at least as
much zero service as it creates.  Likewise, a clean unused ear retaining the
old size-16361 matching is impossible in this catalogue, since Theorem 4.1
would give matching size 16362.

The first shell contains 684 nonidentity braids preserving both
((h,z)=(22,6)).  None changes the projected ({2575,2607}) circuit and
none creates a candidate for any target in (0.1).  Exactly two relocate the
shared circuit cell; all 18194 eligible second braids from those states fail
to reach Hall 21 or zero five.  Seven audited near-creator corridors add
63783 second moves with the same negative conclusion.  This closes the
direct/near-creator radius-two class only, not all possible remote two-braid
routes.

### Theorem 6.2 (the physically graded portal has fixed collateral)

The complete neutral-first second-neighbour census has 682 distinct
nontrivial protected-neutral first states and

    375,282,842 Johnson-valid second braids
      8,164,534 residence-valid second braids
      6,224,656 all-upper-safe second braids
             10 grade-compatible {2575,2607} portals.

Every portal has, up to reversal, the controller motif

\[
(2567,2574,2604),
\tag{6.6}
\]

so that

\[
2567\cup2574=2575,\qquad
2567\cup2574\cup2604=2607.
\tag{6.7}
\]

Thus the required depth-one/depth-two split is physically real.  But all ten
states have Hall deficiency 25, eight zeros, and lower-hole vector

\[
(6,20,6,1,0,0,0).
\tag{6.8}
\]

Relative to the Hall-22 base, each loses exactly

\[
\begin{array}{c|c}
q=1&719,2667\\
q=2&591,2603,2665
\end{array}
\tag{6.9}
\]

and gains \(q=2\) target 2575, while preserving every upper support.  The
old deficient shore improves to gap 21, but a remote gap-25 shore appears.
Hence native grading and the desired local split do not preserve exterior
service.

Across the ten portal states, the recorded third-neighbour census has
5,484,833 Johnson-valid moves, 119,994 resident moves, and 91,293
all-upper-safe moves.  There is no Hall-21 output.  The ten
Hall-22/zero-six outputs are inverse repairs which destroy the portal; the
22 nonidentity portal-preserving outputs have best score Hall 25/zero 9 and
restore none of the five losses in (6.9).  This closes the audited
neutral-router--graded-portal--one-repair architecture for the
\(\{2575,2607\}\) circuit.  It does not cover remote creator macros for the
six zeros.

### Corollary 6.3 (shortest possible architectures)

Any safe route from the canonical carrier to Hall 21 or to five zeros has
length at least two.  A shortest two-braid route must have one of the forms

\[
 \text{router}\to\text{combined clean creator/splitter},
\tag{6.10}
\]

or

\[
 \text{compensated raw creator/zero transfer}
 \to\text{splitter plus repair}.
\tag{6.11}
\]

If creator and splitter are required to be genuinely separate states and
the first step is a protected-neutral router, at least three braids are
necessary:

\[
 \text{neutral legality router}
 \to\text{graded creator}
 \to\text{graded splitter}.
\tag{6.12}
\]

The catalogue proves the first-step lower bound and the direct radius-two
negative class.  It does not prove that every remote two-braid route is
impossible, nor that a three-braid route exists.

## 7. Sharp remaining obstruction

The native grading correction completely removes cell 5617 from the
creator search.  It also gives an exact reduced search space:

\[
\begin{array}{c|c}
\text{target}&\text{only admissible native first-cell row}\\ \hline
5801,13620&\text{depth two}\\
13616,17738,21641,29776&\text{depth one}.
\end{array}
\tag{7.1}
\]

The local controller gate is already open: Theorem 2.2 attains the minimum
\((h,c)=(2,1)\) for every zero.  The static free-cell gate is open, after
maximum-matching rerouting, for all four displayed rank-six portals, but
closed at controller cost one for both rank-seven zeros.  It is invariantly
closed at Hamming distance two for \(13620\) under every maximum matching of
the current graph.

The remaining gate is therefore not rankwise incidence or ordinary
matching reachability.  It is a physical chronology theorem which transports
one of the graded local substitutions through the middle-owner path while
simultaneously retaining residence, protected shadows, exterior matching
capacity, and the common-(Q) word.  Any future search should reject a
candidate before Hall evaluation unless its prospective native cell has
depth exactly (|S|-5).

No constant-one asymptotic conclusion and no exact (k=15) optimum follows
from this note.

## 8. Audit boundary

The decisive logical separations are:

* Theorem 1.1 is an integral controller theorem; no fractional realization
  is used.
* Theorem 2.2 proves only an internally Johnson-legal local tuple.  It does
  not silently extend that tuple to neighbouring controller positions.
* Theorem 3.2 concerns the current incidence graph.  A controller move may
  both create and destroy edges, so static freeability is only a search
  filter.
* Theorems 4.1 and 4.2 require literal retention of the old pins in the same
  final word.  Mere equality of Hall scores is insufficient.
* Theorem 6.1 is exhaustive only for the stated four three-cut braid types.
  The radius-two conclusion has the explicitly stated direct/near-creator
  scope.

These qualifications are necessary: dropping any one of them would turn the
proved graded atlas into an unproved physical creator claim.
