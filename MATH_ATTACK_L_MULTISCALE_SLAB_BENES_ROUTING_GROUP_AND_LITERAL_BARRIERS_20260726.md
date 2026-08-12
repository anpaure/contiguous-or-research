# Multiscale cross-parent slabs: abstract routing group, frame curl, and the typed Beneš gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Let \(Q_n=\mathbb F_2^n\).  A \(Q_{r+1}\)-resolution chooses one carrier
coordinate \(i\), freezes \(i\) in its two orientations, and obtains two
opposite \(Q_r\)-facets.  The certified cross-parent slab trade replaces
this \(i\)-resolution by a \(j\)-resolution of the same owner cube.

There are three different objects which might be called the resulting
"routing network."  They have different answers.

1. **Physical owners.**  A slab trade moves no owner.  It replaces the
   successor/flag structure on the same (2^{r+1}) roots.  Its action on
   owner labels is therefore the identity.  Unframed facet resolutions
   form a groupoid of partitions, not a permutation group on packet
   wires.

2. **Resolution-direction labels.**  On one carrier, the reversible
   comparisons \(i\leftrightarrow j\) generate
   
   \[
                              S_{r+1}.                 \tag{0.1}
   \]
   
   More generally, edge transpositions on an allowed direction graph
   generate the product of symmetric groups on its connected components.
   This is a group on coordinate labels, not a whole-packet routing
   theorem.

3. **Hypothetical canonically framed atomic addresses.**  Add the passive
   convention which compares old and new ordered address slots by a
   coordinate transpose.  If that address-transpose operation can then
   be selected independently in every two-face, it swaps the two middle
   vertices \(01\leftrightarrow10\) and fixes \(00,11\).  Consequently
   the exact generated group on \(Q_n\) is
   
   \[
   \boxed{
      \mathcal G_n=\prod_{k=0}^{n}
              S_{\binom nk}.}                       \tag{0.2}
   \]
   
   This is not the physical owner action of a slab: physical roots remain
   fixed.  In the hypothetical address model, the complete invariant is
   Hamming weight.  Thus even this
   maximally addressable abstract model is not rearrangeable on all
   \(2^n\) leaves.  It is fully rearrangeable inside each weight layer.

The literal factor problem stops earlier than (0.2).  A facet recoupling
is not a two-wire crossbar: every old (Q_r)-facet meets every new
(Q_r)-facet in exactly (2^{r-1}) owners.  It splits both old packets
in half.  There is no certified map sending either old packet intact to
one new packet.

There are then three exact obstructions to the naive closed,
payload-preserving hierarchy.

* **Fixed-hierarchy frame curl.**  Opposite packet facets can fuse at the
  next scale only
  when they are cubical twins.  Already in (Q_3), choosing edges parallel
  to \(x_1\) in the \(x_3=0\) slice and edges parallel to \(x_2\) in
  the \(x_3=1\) slice leaves no transverse \(Q_2\)-fusion.  In a naive
  hierarchy the first-layer switch field must be constant across every
  later twin direction.  The nominal (2^{n-2}) independent switch bits
  collapse to one.  Later re-framing or a larger associator could evade
  this schedule, so this is not a universal invariant of every slab word.

* **Scale arithmetic.**  A closed factor of \(Q_r\) into isometric
  \(C_{2r}\)'s requires \(2r\mid2^r\), hence \(r\) is a power of two.
  The certified diverse-order compiler is presently available only at
  \(r=8\cdot2^t\), and protects depth \(H\) only when
  \(H\le r/4-1\).  A closed hierarchy through
  \(r=1,2,\ldots,R\) therefore does not exist.

* **Chronology type for payload splices.**  Splicing old row pieces with
  direction words \(\pi\pi\) and \(\sigma\sigma\) at phase (t) preserves
  the doubled-permutation word exactly when their prefix direction sets
  through (t) agree.  Untyped Beneš payload switches fail at the first
  prefix-set mismatch.  A general slab trade may instead discard lineage
  and reinstall independent compilers.  A payload-preserving route must
  carry one nested flag through every protected depth and both signs.

Therefore arbitrary bundle routing is **not** proved, and the naive
multiscale Beneš lift is false.  The exact possible escape is an open,
antipodally paired, cubically twin, frame-flat, chronology-typed routing
network, with the closed compiler installed only at a sufficiently large
top scale.  No theorem currently constructs that object.

This report uses the certified slab only as an exact owner-factor trade.
It does not infer universal shadow nesting, target coverage, (LM_A), or
coefficient one.

## 1. A facet recoupling is a repartition, not a whole-wire switch

Fix distinct coordinates (i,j) of (Q_{r+1}).  Put

\[
 P_a=\{x:x_i=a\},\qquad Q_b=\{x:x_j=b\},
 \qquad a,b\in\{0,1\}.                              \tag{1.1}
\]

The (i)-resolution is ({P_0,P_1}), while the (j)-resolution is
({Q_0,Q_1}).

### Lemma 1.1 (exact intersection matrix)

For all (a,b\in\{0,1\}),

\[
                      |P_a\cap Q_b|=2^{r-1}.        \tag{1.2}
\]

Hence the normalized old/new packet-incidence matrix is

\[
                 {1\over2}
                 \begin{pmatrix}1&1\\1&1\end{pmatrix}.        \tag{1.3}
\]

#### Proof

Fixing two independent coordinates in (Q_{r+1}) leaves (r-1) free
coordinates, proving (1.2).  Each facet has (2^r) owners, giving
(1.3).  \(\square\)

A whole-wire (2\times2) switch would have intersection matrix

\[
 \begin{pmatrix}2^r&0\\0&2^r\end{pmatrix}
 \quad\hbox{or}\quad
 \begin{pmatrix}0&2^r\\2^r&0\end{pmatrix}.         \tag{1.4}
\]

Equation (1.2) rules out both.  The slab operation is a two-by-two
transpose of half-packets.  For (d) total independent resolution axes,
including the old frozen axis, the common refinement has (2^d) cells and
one original facet has split into (2^{d-1}) lineage pieces.  Equivalently,
(d) genuinely new axes in addition to the old one give (2^{d+1}) cells
and (2^d) pieces of the old facet.  Thus packet lineage is
not a Markov wire unless those pieces are promoted to the actual ports.

There is also no hidden owner permutation.  Both factors are indexed by
the same root set (Q_{r+1}); the canonical root correspondence is
(x\mapsto x).  The successor permutation changes, but the slab theorem
does not canonically match old cycles, old flags, or old packet labels to
new ones.

## 2. Exact abstract groups

### 2.1 Unframed resolutions

Without address or port labels, a state is a partition of a carrier cube
into facets.  A resolution change is a reversible arrow between two such
partitions.  Composition is defined only when the terminal partition of
one arrow is the initial partition of the next.  This is a groupoid.

A closed word can return to its initial partition while changing the
installed compiler factor or its flag chronology.  Consequently its
partition holonomy does not determine its literal target action.

### 2.2 Direction-label group

On a fixed carrier set (A), (|A|=r+1), label a resolution by its
frozen coordinate.  Comparisons along allowed pairs (ij) act as
transpositions ((i,j)).

### Proposition 2.1 (direction group)

If (Gamma) is the graph of allowed direction comparisons, then

\[
 \langle (i,j):ij\in E(\Gamma)\rangle
   =\prod_{C\in\operatorname{Comp}(\Gamma)}S_C.     \tag{2.1}
\]

In particular a star ({(e,i):i\ne e}) generates (S_A).

#### Proof

Edge transpositions of a connected graph generate the symmetric group on
its vertices: a transposition between the endpoints of a path is a word
in adjacent edge transpositions.  Different connected components do not
interact.  The star case follows also from

\[
                         (i,j)=(e,i)(e,j)(e,i). \tag{2.2}
\]

\(\square\)

This is only the group of frozen-axis labels.  It says neither that two
old packet factors travel intact nor that the required slab is present in
the current exact factor.

### 2.3 Hypothetical framed-address group

Fix an address convention in (Q_n).  In a two-face

\[
              x+\langle e_i,e_j\rangle,
              \qquad x_i=x_j=0,                    \tag{2.3}
\]

add the convention that the change from the (i)-first to the (j)-first
address order is represented by

\[
 x+e_i\longleftrightarrow x+e_j,                   \tag{2.4}
\]

with (x) and (x+e_i+e_j) fixed.  This is one edge transposition in the
Johnson graph on a constant-weight layer.  It is an address comparison,
not a physical owner map supplied by the slab theorem.

### Theorem 2.2 (fully addressable hypothetical leaf group)

Assume that the switch (2.4) is independently available in every
two-face of (Q_n).  Then its generated permutation group is exactly

\[
 \boxed{
   \prod_{k=0}^{n}\operatorname{Sym}
       \{x\in Q_n:|x|=k\}.}                         \tag{2.5}
\]

#### Proof

Every generator (2.4) preserves Hamming weight, giving containment in
the right side.

For fixed (k), the vertices of weight (k) form the Johnson graph
(J(n,k)); two vertices are adjacent precisely when they differ by
deleting one (1) and inserting one (1), equivalently when their
Hamming distance is two.  This graph is connected: repeatedly exchange
an element of (X\setminus Y) with one of (Y\setminus X) to move (X)
to (Y).  Equation (2.4) supplies the transposition on every such edge.
Edge transpositions of a connected graph generate its full symmetric
group.  This proves equality independently in every weight layer.
\(\square\)

Thus Hamming weight is the first and complete invariant in this idealized
model.  Higher-scale coordinate transpositions add no group elements once
all local two-face switches are present: a coordinate transposition on a
larger subcube is the product of its disjoint two-face transpositions.

If only uniform global coordinate switches are allowed, the group is
merely the natural (S_n)-action.  If uniform endpoint flips are added as
separate operations, it becomes the cube automorphism group

\[
                             C_2^n\rtimes S_n.       \tag{2.6}
\]

Conditional, context-dependent one-bit flips would destroy the weight
invariant and enlarge the group, but they are not supplied by a
facet-resolution trade.

### 2.4 Sequential routing capacity

Theorem 2.2 is a generation theorem, not a logarithmic-depth routing
theorem.  It nevertheless gives an explicit word-length bound.

The diameter of (J(n,k)) is (min(k,n-k)).  A transposition of two
vertices at graph distance (d) is a word of length (2d-1\le n-1) in
edge transpositions along a shortest path.  Every permutation of a set of
size (v) is a product of at most (v-1) arbitrary transpositions.
Therefore every element of (2.5) has a word of length at most

\[
                (n-1)\bigl(2^n-(n+1)\bigr).        \tag{2.7}
\]

No claim of a disjoint, rearrangeably nonblocking schedule follows from
(2.7).

For comparison, if one postulates (M) genuine binary whole-wire
switches arranged in disjoint layers, one layer has at most (M/2)
independent bits.  A network realizing all (M!) permutations must have

\[
 2^{LM/2}\ge M!,
 \qquad
 L\ge2\log_2M-O(1).                               \tag{2.8}
\]

The ordinary Beneš depth (2\lceil\log_2M\rceil-1) meets this
information scale.  Lemma 1.1 shows that a slab resolution is not the
whole-wire switch assumed by (2.8).

## 3. The first fixed-hierarchy compatibility obstruction: cubical twins

A physical orientation packet can be written

\[
                    \mathcal Q(F,E;D),              \tag{3.1}
\]

where (D) is a matching of active physical swap pairs, (F) records
fixed-present coordinates, and (E) records fixed-absent coordinates.
Equivalently, on every active pair (uv\in D) its owners satisfy

\[
                             x_u\oplus x_v=1,        \tag{3.2}
\]

in addition to the fixed pins.

### Lemma 3.1 (twin-facet criterion)

Two physical (Q_r)-packets are opposite facets of one physical
(Q_{r+1}) if and only if, after one common relabelling,

1. they have the same active matching (D);
2. all exterior pins agree; and
3. there is one further physical pair (e={u,v}), disjoint from (D),
   on which the first packet pins (u=1,v=0) and the second pins
   (u=0,v=1).

#### Proof

The three conditions plainly construct the two (e)-facets of
(mathcal Q(F,E;D\cup\{e\})).

Conversely, opposite facets of a coordinate-disjoint (Q_{r+1}) share
the other (r) active axes and every exterior status.  They differ only
in the two orientations of the frozen remaining axis.  This is exactly
the displayed condition.  \(\square\)

An abstract packet pairing by cardinality is therefore insufficient.
The matching and pins are physical port types.

### Proposition 3.2 (minimal (Q_3) frame curl)

In the slice (x_3=0) of (Q_3), resolve the
((x_1,x_2))-square into its two (x_1)-edges.  In the slice (x_3=1),
resolve it into its two (x_2)-edges.  These four edges partition all
owners of (Q_3), and both slice resolutions are legal owner
repartitions.  No lower edge and upper edge are cubical twins for a
transverse next-stage (Q_2)-fusion.

#### Proof

A lower edge has active direction (x_1), while every upper edge has
active direction (x_2).  Lemma 3.1 requires the active matchings to
agree.  Equivalently, their four-vertex union varies all three
coordinates and is not an affine two-cube.  \(\square\)

If both slices choose the same edge direction, corresponding edges do
fuse across \(x_3\).  This gives the exact zero-curl law.

### Corollary 3.3 (switch-field collapse)

Fix coordinates \(a,b\) of \(Q_n\).  For every
\(z\in Q_{n-2}\), resolve the \((a,b)\)-square above \(z\) into either its
\(a\)-edges or its \(b\)-edges; write the choice as
\(\varepsilon(z)\in\{a,b\}\).  If these edges are to fuse successively
along every remaining coordinate while retaining a common active frame,
then \(\varepsilon\) is constant.

#### Proof

Fusion across a remaining coordinate \(j\) pairs the squares above
\(z\) and \(z+e_j\).  Lemma 3.1 forces
\(\varepsilon(z)=\varepsilon(z+e_j)\).  The graph \(Q_{n-2}\) is
connected, so all values agree.  \(\square\)

The naive first layer had \(2^{n-2}\) nominal switch bits.  Literal
next-scale cubicality in this prescribed fusion schedule retains only
one.  This is the first exact compatibility obstruction for the naive
fixed hierarchy, before target collisions or energy enter.  It does not
exclude a later re-framing, a different fusion schedule, or a larger
associator.

## 4. Scale and divisibility barriers

### Proposition 4.1 (closed-scale arithmetic)

If (Q_r) is factored into cycles of length (2r), then

\[
                              2r\mid2^r.             \tag{4.1}
\]

Consequently (r) is a power of two.

#### Proof

The number of cycles would be (2^r/(2r)), proving divisibility.  Since
(r\mid2^{r-1}), (r) has no odd prime factor.  \(\square\)

The separate dyadic doubled-permutation construction supplies the
owner-side factor when \(r\) is a power of two; this sufficiency is not a
consequence of Proposition 4.1 alone.  The current diverse-order literal
compiler is more restrictive: its certified dimensions are

\[
                              r=8\cdot2^t,           \tag{4.2}
\]

and its protected range is

\[
                              H\le r/4-1.            \tag{4.3}
\]

At (r=1), the arithmetic orbit has length two, but it is a degenerate
back-and-forth traversal of the unique (K_2) edge, not the certified
simple-cycle compiler needed for positive-depth flags.

Thus Theorem 2.2's decisive local (Q_2) address switches are not
available as closed compiler-safe factors through a positive protected
depth.  A multiscale literal network would have to leave its small scales
open and ported, carry their state upward, and close only after reaching a
dimension satisfying (4.2)-(4.3).

There is presently no theorem that performs this open-to-closed lift.

### 4.2 A parity consequence in the hypothetical address model

Under the address-transpose convention of Section 2.3, a coordinate
transposition on a framed (Q_{r+1}) exchanges the
(2^{r-1}) pairs of vertices whose two selected bits differ.  If
(r\ge2), this is an even permutation of atomic addresses.  Therefore a
hierarchy using only (r\ge2) resolution transpositions lies in the
alternating group on the full address set.  This gives a second elementary
obstruction to arbitrary abstract address routing once the nondegenerate
(r=1) stage is removed.  Physically every slab word fixes owner roots, so
this is not an additional physical owner-permutation invariant.

It is weaker than frame curl for the literal hierarchy, but unlike frame
curl it is a group invariant of the canonical address model.

## 5. Chronology is a port type for payload-preserving splices

Let an isometric \(C_{2r}\) row have direction word

\[
                    \pi\pi,
 \qquad \pi=(\pi_0,\ldots,\pi_{r-1})               \tag{5.1}
\]

with \(\pi\) a permutation of the active directions.  Define its prefix
set

\[
                    P_t(\pi)=\{\pi_0,\ldots,\pi_{t-1}\}.        \tag{5.2}
\]

### Lemma 5.1 (exact prefix-set splice test)

Take rows \(\pi\pi\) and \(\sigma\sigma\).  Cross-splice their first-half
tails at phase \(t\), producing first-half words

\[
 \pi_{[0,t)}\sigma_{[t,r)},
 \qquad
 \sigma_{[0,t)}\pi_{[t,r)}.                       \tag{5.3}
\]

Both hybrids are permutations of the \(r\) directions if and only if

\[
                              P_t(\pi)=P_t(\sigma). \tag{5.4}
\]

#### Proof

The first word in (5.3) is a permutation precisely when its prefix
(P_t(\pi)) is the complement of the suffix direction set
({\sigma_t,\ldots,\sigma_{r-1}}), namely when it equals
(P_t(\sigma)).  The same condition handles the second word.
\(\square\)

If (5.4) fails, a hybrid repeats one direction and omits another.  It is
not isometric and its protected trace need not be geodesic.

Lemma 5.1 certifies only the doubled-permutation direction words.  Even
when (5.4) holds, a physical owner-preserving splice still requires
matching phase owners, legal successor edges, disjoint resource use, and
the appropriate port/collar ledger.  Prefix equality is not by itself a
literal associator.

The switch must also be repeated at the antipodal phase \(t+r\) with the
same decision; otherwise the second half is no longer a copy of the first
and the word is not \(\rho\rho\).  Thus the actual port type includes at
least

\[
   (\text{active frame},\ \text{phase},\ P_t(\pi),\
          \text{antipodal mate}).                  \tag{5.5}
\]

For all-depth literal traces it includes the nested prefix flag

\[
                 P_1(\pi)\subset P_2(\pi)\subset\cdots
                    \subset P_H(\pi).              \tag{5.6}
\]

Routing the depth-(q) support profiles separately does not produce one
route satisfying (5.6).  Likewise the lower and upper signs are the empty
and full images of the same active face and cannot be switched
independently.

For a literal port this list is still incomplete: one also needs the
phase owner/root orientation, all exterior pins, and the ordered cyclic
\(H\)-neighborhood on both sides of the splice.  The nested sets in
(5.6) remember direction support but not translated basepoints.

These conditions constrain a network which transports old row pieces.
They are not necessary for a general certified slab replacement which
throws away old cycle lineage and installs independent certified factors
on the new facets.

## 6. Exact invariant ledger

The following invariants and constraints survive every certified literal
slab word in their stated scopes.

### 6.1 Root ownership

Every trade preserves the complete middle-owner multiset.  In a rooted
path-column formulation its signed difference \(\delta\) satisfies

\[
                               A\delta=0             \tag{6.1}
\]

in every root fibre.  Therefore an owner-rooted flag is replaced at its
own root; it is not transported as an indivisible token to another root.

### 6.2 Macroblock rank

Every certified axis joins the two halves of one macroblock.  Toggling it
preserves the number of selected coordinates in that macroblock.  Hence
the local-rank vector

\[
        (|X\cap B_1|,\ldots,|X\cap B_b|)             \tag{6.2}
\]

is constant along every factor row and all routing remains block diagonal
by this vector.  The finer parent status label is not invariant; the
cross-parent slab was constructed precisely to break it.

### 6.3 Owner-overlap components and state availability

After an \(i\to j\) switch, the sequential inverse \(j\to i\) is
immediately legal on that same owner carrier.  By contrast, a
**simultaneous signed formal combination** using both orientations needs
distinct owner-disjoint carriers already present on the corresponding
shores; a signed coefficient does not create the reverse copy.
Simultaneous switches require disjoint owner slabs.  Sequentially, the
next proposed transverse slab must satisfy the twin criterion in the
factor produced by the preceding stage.

Consequently the physical move graph is state dependent.  Components of
the universal closure hypergraph containing every slab that can occur in
any reachable state are stable routing blocks; no slab word crosses
between them.  Components of the slabs visible in one current state need
not be invariant, because a recoupling can expose new later slabs.

### 6.4 Component count

At one fixed scale (r), each resolution contains two (Q_r) packet
factors and hence exactly

\[
                     2\,{2^r\over2r}={2^r\over r}    \tag{6.3}
\]

compiler cycles.  A one-scale slab replacement preserves this count.
Across different scales no common component count is invariant, and a
legal two-break may merge or split successor cycles.

### 6.5 Checkerboard parity

Every nontrivial cube and every opposite-facet resolution contains equal
numbers of the two cube checkerboard classes.  A slab recoupling preserves
those totals.  They are already saturated in an unprescribed complete
owner factor, so this parity gives no routing obstruction unless the
ports themselves prescribe checkerboard classes.  It must not be confused
with the stronger framed-address weight invariant in Theorem 2.2.

### 6.6 Antipodal and sign constraints

Every closed packet row has word \(\pi\pi\).  Its depth-(q) faces occur
in antipodal pairs, every fixed-support multiplicity is even, and the
lower and upper images are the empty/full versions of the same face.
These statements are packetwise; moving frames do not define one global
target antipode.

For a geodesic owner window (X_0,\ldots,X_q),

\[
 \mathbf1_{L_q}+\mathbf1_{U_q}
       =\mathbf1_{X_0}+\mathbf1_{X_q}.              \tag{6.4}
\]

Thus every owner-preserving compound residue satisfies the genuine
frame-independent point identity

\[
                     M_q^-R_q^-+M_q^+R_q^+=0.        \tag{6.5}
\]

Here \(M_q^-\) and \(M_q^+\) are the point-versus-target incidence
maps on ranks \(m-q\) and \(m+q\), while \(R_q^\pm\) are the signed
target-load residues of the trade.  They are unrelated to the notation
for a missing-target count.

### 6.7 Common flag chronology

For every participating row which is geodesic through depth \(H\), all
signed depths are projections of one owner-rooted flag incidence.  For a
trade there is one signed flag vector \(\eta\) such that

\[
                           R_q^\pm=P_q^\pm\eta,
             \qquad 1\le q\le H.                   \tag{6.6}
\]

The lower/upper margins at fixed (q) also come from one crossing-grid
matching supported on (L\subset U), (|U\setminus L|=2q).

This assertion is not automatic for the presently hypothetical open
stages \(r\le4H\).  Such stages need a separate open-flag transport
theorem before (6.6) may be assigned to them.

### 6.8 Weighted multiscale direction closure

Assume that a closed isometric compiled primitive is installed at every
scale under discussion, that \(q<r\) at every such scale, and that all
carrier directions are embedded in one common physical direction
universe.  At scale (r), one (i\to j) resolution change has
occurrence-refined
direction derivative

\[
              2qg_r(e_j-e_i),
              \qquad g_r={2^r\over r}.              \tag{6.7}
\]

Therefore a mixed-scale word which is closed in the direction incidence
at one, hence every, positive depth must satisfy

\[
 \boxed{
       \sum_t g_{r_t}(e_{j_t}-e_{i_t})=0.}           \tag{6.8}
\]

Unweighted abstract closure is insufficient.

For dyadic scales (r=2^a\ge2),

\[
                       v_2(g_r)=r-a.                \tag{6.9}
\]

This strictly increases along successive dyadic scales from (r=2)
onward.  If (r_0) is the smallest scale in a closed word, reduction of
(6.8) modulo
(g_{r_1}/g_{r_0}), where (r_1) is the next scale, imposes a genuine
power-of-two divisibility condition on the (r_0)-boundary.  In
particular a single (0,\pm1) small-scale imbalance cannot generally be
cancelled by larger scales.

The statistic (6.7) is occurrence/frame refined.  In a moving-frame atlas
there is no global map from an unlabelled physical target to its local
swap support, so (6.8) must not be advertised as a literal-target
invariant.  Nor is (6.7) presently proved for the proposed small open
stages; those require their own open-direction ledger.

## 7. Quantitative routing and exposure bounds

### 7.1 Entropy of a true packet network

Let one packet have (s=2^r) owners and let

\[
                              M={G\over s}           \tag{7.1}
\]

be the number of packet ports in an owner mass (G).  A layer of genuine
disjoint binary whole-port switches would contain at most (M/2) bits.
The information lower bound (2.8) therefore applies.  A slab layer has
the same number of paired owner regions but, by Lemma 1.1, does not
supply those whole-port bits.

At the central scale \(G=(1-o(1))\binom{2m}{m}\) with \(r=o(m)\),
\[
 \log_2M
 =2m-r-\frac12\log_2(\pi m)+o(1).                 \tag{7.1a}
\]
Thus even an ideal true-switch network which globally rearranges all
packet ports needs \(\Theta(m)\) binary layers by (2.8).  This entropy
bound concerns arbitrary global permutations; a targeted shadow repair
may need a much smaller routing family.

### 7.2 Flag exposure under one split

In an isometric (Q_r) packet factor, a fixed active direction belongs to
exactly

\[
                              q{2^r\over r}          \tag{7.2}
\]

depth-(q) windows per sign.  These are precisely the windows which
cannot remain wholly inside either facet when that direction is removed
from the active frame.  Summing both signs and all protected depths gives

\[
 2\sum_{q=1}^{H}q{2^r\over r}
       ={2^rH(H+1)\over r}                         \tag{7.3}
\]

typed flag occurrences exposed by one packet split.

A complete \(Q_{r+1}\) slab resolution has two \(Q_r\) packets, so its
corresponding exposure is twice (7.3).

This is an occurrence count, not automatically a literal loss: a
successful typed port network could transport these flags.  It proves
that a facet-only packet lineage, with no boundary channel, is
insufficient.

### 7.3 Minimum number of frame-changing layers

This paragraph concerns a hierarchy of fixed-scale \(Q_r\) packet
layers, so that the packet count \(M=G/2^r\) is constant.  Fix a baseline
direction frame.  If a final \(Q_r\)-packet has \(a(P)\)
active directions outside that frame, then at depth (q) at most

\[
                         a(P)q{2^r\over r}           \tag{7.4}
\]

of its starts use at least one such direction, by the union bound and
(7.2).  Hence producing \(\delta G\) occurrences which genuinely use a
nonbaseline direction requires

\[
                  \sum_Pa(P)\ge
                     \delta\,{G\over2^r}{r\over q}. \tag{7.5}
\]

One two-packet slab switch changes the sum on the left by at most two.  A
full owner-disjoint layer has at most (M/2) switches and changes it by at
most (M).  Therefore any such state-feasible hierarchy needs at least

\[
                              \delta\,{r\over q}     \tag{7.6}
\]

full layers.  This is conditional on the premise that the repaired
occurrences must use nonbaseline directions.  It is a routing-capacity
bound, not a universal lower bound on every target-cover construction.

## 8. What a genuine Beneš lift would require

If arbitrary independent whole-port (2\times2) switches were supplied
and \(M\) were a power of two,
the standard Beneš induction would route every permutation.  Pair the
inputs and outputs, form the 2-regular bipartite multigraph whose edges are
the demanded connections, alternately two-colour every cycle, send the
two colours through the two recursive subnetworks, and set the first and
last switches accordingly.  This proves rearrangeability in
\(2\log_2M-1\) stages.  For arbitrary \(M\), pad to the next power of
two; the resulting depth is \(2\lceil\log_2M\rceil-1\).

The certified slab does not satisfy the induction's whole-port axiom.
For a literal replacement, all of the following new theorems are needed.

1. **Open payload switch.**  A two-input/two-output operation which sends
   each entire owner/flag payload straight or crossed.  Equality of total
   owner unions is not enough.
2. **Twin-coherent scheduling.**  Every pair presented to a stage must
   satisfy Lemma 3.1 after all earlier choices.  Equivalently, the frame
   connection must be flat around every routing square.
3. **State-feasible reverses.**  Every reverse edge used by a formal
   routing cycle must occur on a physical slab currently in that shore.
4. **Owner-disjoint stages.**  Simultaneous switches must have disjoint
   owner carriers; overlapping stages require a proved associator, not
   commutativity on labels.
5. **Typed ports.**  Ports must record pins, active frame, local-rank
   vector, phase owner, ordered cyclic \(H\)-neighborhood, prefix flag
   (5.6), and antipodal mate.
6. **Small-scale transport.**  Stages below the compiler threshold must be
   open and must transport every exposed flag in (7.3) without charging it
   as leave.
7. **Top-scale closure.**  The final packets must admit one certified
   compiler conjugate, with all rows geodesic and with the same chronology
   used at every depth and both signs.
8. **Weighted multiscale balance.**  A closed direction route must satisfy
   (6.8), including its dyadic congruences.
9. **Literal target control.**  The final route must prove (o(W))
   aggregate holes or the required floor ledger.  Abstract owner
   rearrangeability and direction closure do not imply this.

The first missing theorem is already item 1 together with item 2: the
certified facet trade is a split-and-merge repartition, and arbitrary
local settings violate cubical twin coherence on (Q_3).  Chronology and
target control are later, independent gates.

## 9. Constant-one implication boundary

The multiscale idea has one genuine positive abstract feature: if local
(Q_2) address transpositions were independently available, every
permutation inside each orientation-weight layer could be routed.  Thus
there is no further group-theoretic obstruction inside a layer.

But the literal exact-factor construction lacks those fine switches and
does not possess a Beneš packet network.  In particular:

* the full leaf group is not (S_{2^n});
* the actual physical owner action is pointwise trivial;
* packet lineages split at every facet recoupling;
* the first arbitrary setting pattern fails cubicality in (Q_3);
* closed compiler-safe factors do not exist at all intermediate scales;
  and
* untyped payload paths can fail the prefix-set splice test.

Therefore multiscale slabs do not presently prove a shadow-dispersing
factor, (LM_A), MWB, or the coefficient-one theorem.  The precise next
object is the typed open Beneš network described in Section 8.  A proof
of that object would still have to be followed by the literal target
coverage theorem; a counterexample to it would close this routing lane
without affecting other possible exact-factor constructions.

## 10. Independent audit of the decisive steps

The following points were rederived independently.

* The intersection matrix (1.2) makes whole-packet routing impossible at
  one slab unless a new payload map is added.
* The group (2.5) follows exactly from connectedness of every Johnson
  layer, and Hamming weight is both necessary and sufficient as an
  abstract orbit invariant.
* Lemma 3.1 is a necessary-and-sufficient physical fusion test, not merely
  a dimension count.
* Proposition 3.2 is the first nontrivial frame-holonomy obstruction; it
  appears before compiler choices.
* Divisibility (4.1) is necessary, while the sparse scale and depth
  restrictions (4.2)-(4.3) are properties of the currently certified
  compiler and must not be weakened to all dyadic scales.
* The prefix-set condition (5.4) is necessary and sufficient for the two
  formal hybrid first halves to remain permutations; it is not a physical
  owner-splice theorem.
* The multiscale closure coefficient is (g_r=2^r/r); replacing it by an
  unweighted boundary loses a genuine power-of-two congruence.
* The flag-exposure count (7.3) is exact as an occurrence incidence, but
  it is not by itself a lower bound on literal word length.

These audits leave no claimed positive literal routing theorem.  They do
isolate the first fixed-hierarchy compatibility obstruction and the exact
escape data.
