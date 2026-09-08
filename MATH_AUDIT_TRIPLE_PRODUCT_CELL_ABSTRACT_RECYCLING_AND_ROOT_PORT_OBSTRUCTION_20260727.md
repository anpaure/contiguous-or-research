# Triple product cells recycle helpers abstractly, but one matched root port kills the physical lift

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Assume first that (3\mid 2m), and put

\[
 b={2m\over3},\qquad M=m+H=b+t,\qquad t={m\over3}+H,
 \qquad N=\binom{2m}M.
\tag{0.1}
\]

Partition ([2m]) into (b) triples.  On (t) triples prescribe local
weight two and on the other (b-t) triples prescribe local weight one.
The resulting product cell has (3^b) rank-(M) tops.  It has an exact
abstract helper-recycling chronology:

* every weight-two coordinate has (3^{b-1}) disjoint three-top lines;
* toggling every line once gives (t3^{b-1}) three-top moves;
* every top participates exactly once in every weight-two coordinate,
  hence (t=\Theta(m)) times in total; and
* one formal slot remains on every top throughout.

Thus the proposed product geometry really does solve the **incidence-level**
global reuse problem.  It converts fresh companions into a closed regular
schedule with no top deficit.

There is, however, a sharp physical obstruction to lifting this chronology
with the matched-cut three-top packet from
`MATH_THEOREM_THREE_TOP_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_RECHARGE_20260727.md`.
In every source and target word of that packet, rooted position three is
occupied by a label of the packet's three-label coordinate.  Consequently:

\[
 \boxed{\text{one rooted word can realize at most one disjoint triple
 coordinate at the matched root port.}}
\tag{0.2}
\]

This is true both simultaneously and sequentially.  A coordinate-(i)
packet only swaps two labels of the (i)-th triple, so after the move the
label in position three still belongs to that same triple.  No packet from
a different coordinate can then be enabled without an additional
cross-coordinate re-rooting primitive.  Since every product-cell top must
participate in (t>1) coordinate packets, the requested one-word-per-vertex
physical lift is impossible as stated.

The product-cell idea therefore identifies the global combinatorial schedule
but does not by itself solve the global physical chronology.  The missing
operation is exactly the old gate in a sharper form: transport the unique
matched root port from one triple block to another while preserving the
whole (2H)-collar.

For completeness, this note also gives the exact packing data.  A fixed
triple partition supplies a coefficient-one family of
(\binom bt) disjoint cells, but it covers only

\[
 {\binom bt3^b\over\binom{2m}{M}}
 =\exp\left[-{2m\over3}\log{4\over3}
             -{2H^2\over m}+O\left({H^4\over m^3}+\log m\right)\right]
\tag{0.3}
\]

of the layer.  Thus the obvious fixed-partition packing is exponentially
too small.  The catalogue of all product cells is regular, but adjacent
tops have exact relative codegree

\[
 {2b\over M(2m-M)}={4+o(1)\over3m}.
\tag{0.4}
\]

A near-perfect coefficient-one packing across many triple partitions is a
separate growing-edge exact-cover problem; no such packing is proved here.
Even if it existed, (0.2) would still refute the proposed physical lift.

The case (3\nmid2m) is obtained by freezing the at most two leftover
labels.  None of the conclusions or asymptotic scales changes.

## 1. Product cells

Let

\[
 \mathcal B=(B_1,\ldots,B_b),\qquad |B_i|=3,
\tag{1.1}
\]

be a partition of ([2m]).  Fix (T\subseteq[b]), (|T|=t), and define

\[
 \mathcal P(\mathcal B,T)=
 \left\{U\in\binom{[2m]}M:
 |U\cap B_i|=
 \begin{cases}2,&i\in T,\\1,&i\notin T.
 \end{cases}\right\}.
\tag{1.2}
\]

The rank condition follows from

\[
 2t+(b-t)=b+t=M.
\tag{1.3}
\]

Every block contributes three choices, so

\[
                         |\mathcal P(\mathcal B,T)|=3^b.
\tag{1.4}
\]

Fix (i\in T), write (B_i=\{x,a,y\}), and fix all choices outside
(B_i).  If their union is (C), the three vertices on the resulting
coordinate line are

\[
                 C\cup\{x,y\},\qquad
                 C\cup\{x,a\},\qquad
                 C\cup\{a,y\}.
\tag{1.5}
\]

This is literally the top triangle used by the three-top telescope.  For a
fixed (i), the (3^{b-1}) lines (1.5) partition the cell.

## 2. Exact abstract chronology

Attach to every cell vertex (U) a formal state

\[
                         \epsilon(U)\in\{0,1\}^{T}.
\tag{2.1}
\]

The formal move on an (i)-line flips the (i)-th coordinate of each of
its three vertices and changes no other register.  It replaces one state by
one state on the same three tops.

### Theorem 2.1 (coefficient-one abstract recycling)

Starting from all-zero states, apply once every line in every coordinate
(i\in T), in an arbitrary order.  Then:

1. the line moves commute;
2. the number of moves is (t3^{b-1});
3. every top participates in exactly (t) moves;
4. every final state is the all-one vector; and
5. at every intermediate time there is exactly one formal state on each
   top.

#### Proof

For each fixed (i), its coordinate lines partition the vertex set, so
every vertex is toggled exactly once in register (i).  Moves belonging to
different coordinates act on different registers, and moves in the same
coordinate have disjoint top supports.  They therefore commute.  Counting
lines gives (t3^{b-1}), while counting incidences gives
(3t3^{b-1}=t3^b), namely (t) incidences per top.  No move adds or deletes
a top slot. \(\square\)

This theorem is the exact incidence-level content of the product-cell
proposal.  If every formal line toggle admitted one compatible physical
three-top realization on a single state assigned to each vertex, the helper
reuse would already have the required linear average.

## 3. The root-port invariant of the matched-cut packet

Recall the matched cuts in the three-top theorem.  The retained
(\omega)-path starts two letters before placeholder (A), whereas the
retained (\eta)-path starts two letters before placeholder (B).  Hence

\[
 \begin{array}{c|c|c}
 \text{top}&\text{source base}&\text{rooted position 3}\\ \hline
 C\cup\{x,y\}&\omega^+(x,y)&x\\
 C\cup\{x,a\}&\eta^+(x,a)&a\\
 C\cup\{a,y\}&\eta^+(a,y)&y.
 \end{array}
\tag{3.1}
\]

After replacing plus by minus, the same table reads (y,x,a), respectively.
In particular, position three belongs to (\{x,a,y\}) on both shores.
This statement is invariant under relabelling the three placeholders and
under reversing the orientation of the line.

### Lemma 3.1 (simultaneous context-capacity obstruction)

Let the blocks (B_i) be pairwise disjoint.  A single rooted word on a cell
vertex cannot be a source word for matched-cut packets in two different
coordinates (i\ne j\).

#### Proof

If it is a source word for coordinate (i), (3.1) gives
(p_3\in B_i).  If it is also a source word for coordinate (j), the same
argument gives (p_3\in B_j).  The blocks are disjoint. \(\square\)

Thus no one-word-per-cell-vertex assignment can realize all (t) incident
coordinate lines when (t\ge2).

### Lemma 3.2 (sequential root-block invariance)

Consider a chronology using only matched-cut product-cell packets.  If a
coordinate-(i) packet touches a word (p), then it is enabled only when
(p_3\in B_i), and its target word (p') still satisfies
(p'_3\in B_i).  Consequently a word touched once in coordinate (i)
cannot later be touched in a different coordinate (j\ne i).

#### Proof

The enabling assertion is (3.1).  The packet changes the placeholder roles
by interchanging the two selected labels from (B_i), while keeping the
rooted port fixed.  The target entry in position three is therefore the
other displayed label of (B_i).  Induction proves the final assertion.
\(\square\)

### Corollary 3.3 (the proposed physical product chronology does not lift)

For (t>1), the abstract chronology of Theorem 2.1 has no physical lift
whose only primitives are the matched-cut three-top packets and which keeps
one rooted retained word on every cell vertex.

The obstruction is not middle incidence, collar cancellation, or helper
count.  It is a one-port context-capacity invariant.  To escape it one needs
at least one of the following genuinely new inputs:

1. a collar-neutral primitive which transports the matched root port from
   one triple block to another;
2. several simultaneously live root ports on one physical path, together
   with compatible middle rectangles; or
3. a larger packet whose single move changes more than one product
   coordinate.

The existing three-top packet supplies none of these.

## 4. The largest immediate coefficient-one packing

For one fixed partition (\mathcal B), the cells

\[
          \{\mathcal P(\mathcal B,T):T\in\tbinom{[b]}t\}
\tag{4.1}
\]

are pairwise disjoint: their local rank vectors differ.  Their union is the
set of rank-(M) tops meeting every triple in one or two points.  Therefore
its exact size and density are

\[
 |\mathcal A_{\mathcal B}|=\binom bt3^b,
 \qquad
 f_m={\binom bt3^b\over\binom{3b}{b+t}}.
\tag{4.2}
\]

For (H=O(\sqrt{m\log m})), the entropy expansion
(h(1/2+z)=\log2-2z^2+O(z^4)) gives

\[
 \log f_m
 =-{2m\over3}\log{4\over3}-{2H^2\over m}
   +O\left({H^4\over m^3}+\log m\right).
\tag{4.3}
\]

In particular (f_m=e^{-\Theta(m)}).  A fixed partition gives a perfectly
coefficient-one packing, but not a positive-density one.

## 5. The all-partitions cell hypergraph

Let (\mathscr P_{m,H}) have the rank-(M) tops as vertices and all product
cells (1.2), over all triple partitions and all (T\in\binom{[b]}t), as
edges.  It is regular.  A fixed top (U) belongs to

\[
 D={M!(2m-M)!\over2^b t!(b-t)!}
\tag{5.1}
\]

cells.

Indeed, partition the (M) labels of (U) into (t) pairs and (b-t)
singletons, do the complementary partition on the other shore, and match
the pair classes to the singleton classes.  The factorials simplify to
(5.1).

Let (U,V) be Johnson-adjacent, say
(U\setminus V=\{x\}), (V\setminus U=\{y\}).  A cell containing both must
put (x,y) in the same triple, and that condition is sufficient.  In a
uniform cell through (U), (x) lies in a weight-two block with probability
(2t/M), when the unique complementary label is uniform, and in a
weight-one block with probability ((b-t)/M), when the two complementary
labels are uniform.  Hence

\[
 {\deg(U,V)\over D}
 ={2t\over M}{1\over2m-M}
  +{b-t\over M}{2\over2m-M}
 ={2b\over M(2m-M)}.
\tag{5.2}
\]

This equals ((4+o(1))/(3m)) in the calibrated regime.  The edge size is

\[
                         K=3^b=\exp(\Theta(m)).
\tag{5.3}
\]

Thus the catalogue has a uniform fractional perfect matching, but its
uniformity grows exponentially and its maximum relative codegree is at
least order (1/m).  Fixed-uniformity nibble theorems do not supply the
near-factor claimed in the proposal.  Establishing such a near-factor
would be a new theorem.  It is logically prior to global coefficient-one
installation, but the root-port obstruction of Section 3 shows that proving
it alone would not rescue the proposed physical lift.

## 6. Leftover labels

If (2m=3b+\ell), (\ell\in\{1,2\}), freeze a subset of the leftover
labels in every cell and choose (t) so that the active triple contribution
is (b+t=M-s), where (s) is the number of frozen included labels.  The
coordinate-line chronology and the root-port obstruction are unchanged.
The edge size remains (3^b=\exp(\Theta(m))), and all density and codegree
estimates change only by bounded factors.

## 7. Exact implication boundary

Proved:

1. the exact (3^b)-vertex product cell and its tight three-top lines;
2. an exact commuting coefficient-one abstract chronology with
   (\Theta(m)) uses per top;
3. a coefficient-one disjoint packing for one fixed triple partition and
   its exponentially small density;
4. the exact degree and adjacent-pair codegree of the all-partitions
   catalogue; and
5. a statewise root-port invariant refuting both the simultaneous and the
   sequential one-word physical lifts by the existing matched-cut packet.

Not proved:

1. a near-perfect packing of product cells over many triple partitions;
2. a multi-port or cross-block collar-neutral physical primitive;
3. compatibility with a preassigned PBBS/MSW owner table; or
4. any global constant-one factor theorem.

The main conclusion is therefore a clean split.  Product cells solve global
helper accounting at the formal incidence level, but the existing physical
packet has only one matched root port.  The proposed construction collapses
exactly at that interface.

## 8. The corrected incidence object: the root-port flag hypergraph

The obstruction above also identifies the right replacement for disjoint
product coordinates.  A legitimate sequence must remember the label at the
matched root port, not just the top containing the word.

Let

\[
 \mathfrak F=\{(U,x):U\in\tbinom{[2m]}M,\ x\in U\}
\tag{8.1}
\]

be the set of root-port flags, and use two copies
\(\mathfrak F^+,\mathfrak F^-\) for outgoing and incoming flags.  Put

\[
                         L_0=2m-M=m-H.
\tag{8.2}
\]

For an \((M-2)\)-set (C) and distinct (x,y,a\notin C), the oriented
three-top packet has the flag action

\[
\begin{array}{rcl}
 (C+xy,x)&\longmapsto&(C+xy,y),\\
 (C+ya,y)&\longmapsto&(C+ya,a),\\
 (C+ax,a)&\longmapsto&(C+ax,x).
\end{array}
\tag{8.3}
\]

This is a directed triangle circulation.  It is exactly the position-three
transition in (3.1), including its orientation.

Define the six-uniform hypergraph \(\mathcal H_{\rm flag}\) on
\(\mathfrak F^+\sqcup\mathfrak F^-\) by taking one edge for every packet
(8.3), containing its three outgoing and three incoming flag resources.

### Lemma 8.1 (exact degrees and codegrees)

The hypergraph \(\mathcal H_{\rm flag}\) is regular of degree

\[
                         D_0=(M-1)L_0.
\tag{8.4}
\]

Its maximum pair codegree is

\[
                         \Delta_2=L_0,
 \qquad {\Delta_2\over D_0}={1\over M-1}=O(m^{-1}).
\tag{8.5}
\]

#### Proof

For an outgoing flag \((U,x)^+\), choose its head
(y\in U\setminus\{x\}) and then the third triangle label
(a\notin U\).  This gives every containing packet uniquely, proving
(8.4).  The incoming count is the same by reversal.

One packet has only one outgoing and one incoming flag on each of its three
tops.  A same-top pair can therefore occur only as
\((U,x)^+,(U,y)^-\) with (x\ne y).  Its arc is fixed, while the third
label has (L_0) choices, so its codegree is (L_0).  If the two resources
belong to different tops, those tops must be two edges of one label
triangle with a common \((M-2)\)-core.  The two tops and the signed port
labels then determine the third label and the orientation, giving codegree
at most one.  This proves (8.5). \(\square\)

### Corollary 8.2 (near-perfect incidence-level port circulation)

The classical fixed-uniformity Pippenger--Spencer matching theorem applies
to \(\mathcal H_{\rm flag}\).  Hence there is a collection of pairwise
flag-disjoint three-top packets covering

\[
                         (1-o(1))|\mathfrak F|
\tag{8.6}
\]

outgoing flags and the same number of incoming flags.

The selected packet arcs give, on all but (o(MN)) top-label flags, one
incoming and one outgoing transition.  Therefore for all but (o(N)) tops,
the induced directed graph on its (M) labels is a union of directed paths
and cycles covering (M-o(M)) labels.

Equivalently, the matching contains ((1-o(1))MN/3) three-top packets and
therefore supplies ((1-o(1))MN=\Theta(W)) top-event incidences.  Its
average formal reuse is ((1-o(1))M=\Theta(m)) per top, exactly the dense
recycling scale which the fresh-helper construction lacked.

This is a genuine growing-throughput theorem at the **flag-incidence**
level, obtained from a fixed six-uniform hypergraph.  It avoids the
exponentially uniform cell-packing problem of Section 5 and respects the
root-port invariant which killed the disjoint-triple product.

It still does not finish the physical lift.  Two further facts are needed:

1. the path/cycle components on almost every top must be joined so that one
   rooted word can follow a path of length \(\Theta(m)\); and
2. the \(\omega/\eta\) context words supplied to adjacent packet events
   must agree with the state left by the preceding event.

Thus the corrected successor to the product-cell proposal is a
**flag-circulation coalescence and context-lift theorem**, not a packing of
disjoint ternary coordinates.
