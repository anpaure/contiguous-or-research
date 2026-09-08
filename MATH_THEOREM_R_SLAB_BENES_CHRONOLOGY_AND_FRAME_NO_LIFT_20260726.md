# Raw slab switches do not form a literal Beneš flag router

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Result

There is an exact abstract positive theorem and an exact physical negative
theorem.

For \(N=2^L\), an ideal network of genuine straight/cross \(2\times2\)
switches routes every permutation of \(N\) indivisible packet bundles.  It
has

\[
 2L-1\quad\hbox{stages},\qquad
 {N\over2}(2L-1)=NL-{N\over2}\quad\hbox{switches}.       \tag{0.1}
\]

Complete lower/upper nested flags may be treated as one indivisible bundle,
so the ideal theorem is automatically common in every depth and both signs.
If every switch shore partitions the same owner union and the switches in a
stage are owner-disjoint, exact middle ownership is also preserved at every
stage.

The rank-twisted cross-parent \(Q_{r+1}\) slab is not that switch.  If its old
packets are the two \(e\)-facets and its new packets are the two \(i\)-facets,
then every old packet meets every new packet in exactly half a packet:

\[
 |P_\alpha\cap Q_\beta|=2^{r-1}\qquad
 (\alpha,\beta\in\{0,1\}).                         \tag{0.2}
\]

Thus a raw slab transposes a \(2\times2\) array of \(Q_{r-1}\) subfacets.  It
does not send two whole packets straight or crossed.

There are two further exact obstructions.

1. Let \(s=2^r\), \(g_r=s/r\), and \(1\le q<r\).  For either sign, every
   nontrivial slab re-resolution changes the ownerwise literal depth-\(q\)
   flag on at least

   \[
                         2qg_r={2qs\over r}         \tag{0.3}
   \]

   of the \(2s\) slab owners, regardless of which legal isometric compiler
   is installed on the new packets.  The forced fraction is \(q/r\).  In
   particular, a raw slab can never transport a complete persistent literal
   flag table exactly, already at \(q=1\).

2. The two states of a raw switch have different active frames,

   \[
                   D^0=D,\qquad D^1=D-\{i\}+\{e\}. \tag{0.4}
   \]

   A following transverse slab requires its two inputs to have one common
   active frame.  Hence outputs of two predecessor nodes cannot be
   transversely paired in a fixed branchwise-available next layer while the
   predecessor bits remain independent.  A raw-slab network therefore does
   not have the Cartesian switch-setting structure of a Beneš network.

The frame-direction ledger itself telescopes exactly when all packets have
the same dimension.  Closing the terminal frame census removes the entire
direction-support residue, but need not remove the literal residue in the
kernel of that projection.  Consequently the abstract ideal theorem does
not prove CPCR.  A positive multiscale construction must use correlated
re-foliations and fresh common all-depth compiler choices; it cannot route a
preselected abstract nested-flow table through raw slabs.

## 1. The ideal dyadic network

An ideal wire carries one indivisible atom

\[
             \mathcal B_x=(\hbox{packet label},
             (\mathcal F_{x,q}^-,\mathcal F_{x,q}^+)_{q\le H}). \tag{1.1}
\]

An ideal switch has the two maps

\[
 (A,B)\longmapsto(A,B),\qquad
 (A,B)\longmapsto(B,A).                            \tag{1.2}
\]

Define \(\mathsf B_0\) to be one wire and \(\mathsf B_1\) to be one switch.
For \(L\ge2\), \(\mathsf B_L\) has an input switch layer, two copies of
\(\mathsf B_{L-1}\) in parallel, and an output switch layer.  Every input
pair sends one wire to each recursive copy, and every output pair receives
one wire from each recursive copy.

### Theorem 1.1 (exact ideal rearrangeability)

For every permutation \(\pi\in\operatorname{Sym}(2^L)\), a setting of
\(\mathsf B_L\) sends the atom at input \(x\) to output \(\pi(x)\).

#### Proof

Induct on \(L\).  The result is immediate for \(L=0,1\).  Pair the inputs
and pair the outputs.  Form a bipartite multigraph whose left vertices are
input pairs, whose right vertices are output pairs, and whose edge labelled
\(x\) joins the pair containing \(x\) to the pair containing \(\pi(x)\).
Every vertex has degree two.  Every component is therefore an even cycle,
with a doubled edge allowed as a two-cycle.

Color every cycle alternately red and blue.  Each input pair and each output
pair sees one edge of each color.  Set the input switches so that red edges
enter the upper recursive copy and blue edges enter the lower one.  Set the
output switches so that the same colors leave for their prescribed output
wires.  The red edges induce one permutation of \(2^{L-1}\) wires and the
blue edges another.  Route both by induction.  This routes \(\pi\). \(\square\)

### Corollary 1.2 (typed home assignments)

Suppose input atoms and output homes have types.  A type-respecting home
assignment exists and is ideal-Beneš routable if and only if the input and
output multiplicities agree for every type.

#### Proof

Necessity is immediate.  For sufficiency, choose any type-respecting
bijection and apply Theorem 1.1. \(\square\)

### Proposition 1.3 (exact counts)

The network \(\mathsf B_L\) has the counts in (0.1).  Every atom traverses
exactly \(2L-1\) switches.

#### Proof

Let \(d_L\) and \(S_L\) denote the number of stages and switches.  Parallel
recursive copies share their stage indices, so

\[
 d_L=d_{L-1}+2,qquad d_1=1.
\]

Thus \(d_L=2L-1\).  Every stage has \(N/2\) switches, giving
\(S_L=(N/2)(2L-1)\).  Equivalently,

\[
 S_L=N+2S_{L-1},\qquad S_1=1,
\]

which has the same solution. \(\square\)

If an ideal physical realization has \(N\) packets of size \(2^r\), each
stage consists of \(N/2\) owner-disjoint supports of size \(2^{r+1}\).
Therefore every stage covers the owner bank exactly once.  Replacing either
shore of any subset of those supports preserves every owner once.  This is
the exact integral ownership part which a physical stage-aligned
realization would inherit.

## 2. Exact geometry of one raw slab

Let a physical slab have orientation coordinates \(D\cup\{e\}\), where
\(|D|=r\), and fix \(i\in D\).  The old resolution and new resolution are

\[
 \begin{aligned}
 P_0&=\{x_e=0\},& P_1&=\{x_e=1\},\\
 Q_0&=\{x_i=0\},& Q_1&=\{x_i=1\}.
 \end{aligned}                                      \tag{2.1}
\]

The old active frame is \(D\).  The new active frame is

\[
                         D'=(D\setminus\{i\})\cup\{e\}.        \tag{2.2}
\]

For all \(\alpha,\beta\),

\[
 P_\alpha\cap Q_\beta
 =\{x_e=\alpha,x_i=\beta\}\cong Q_{r-1}.           \tag{2.3}
\]

This proves (0.2).  If packet-constant scalar mass is normalized by packet
size, the one-step old-to-new incidence matrix is

\[
                     {1\over2}\begin{pmatrix}1&1\\1&1\end{pmatrix}. \tag{2.4}
\]

Equation (2.4) is only a one-stage projection: the old facet bit remains as
an internal coordinate after the trade and can be exposed again by a later
re-resolution.  Therefore it must not be multiplied as a memoryless Markov
matrix through several physical stages.  What it proves exactly is that a
single raw slab is a row/column re-foliation, not an ideal straight/cross
switch on whole packets.

### Proposition 2.1 (whole owner-attached bundles do not move)

Partition an owner bank into distinct equal-size packets
\(P_1,\ldots,P_N\), and attach label \(j\) to every owner of \(P_j\).
Any sequence of exact slab re-resolutions preserves these labels owner by
owner.  If a final packet \(Q\) of the same size is monochromatic with label
\(j\), then \(Q=P_j\).

Consequently no sequence of owner-preserving re-foliations realizes a
nontrivial permutation of distinct whole owner-attached packet bundles.

#### Proof

Monochromaticity gives \(Q\subseteq P_j\).  The two sets have equal finite
cardinality, hence \(Q=P_j\). \(\square\)

This proposition does not forbid changing the compiler flags assigned to
the owners.  It says that doing so is a new selection problem, not transport
of pre-existing indivisible atoms.

## 3. A forced literal chronology change

Assume \(r\) is an admissible compiler dimension.  Put

\[
                         s=2^r,\qquad g_r={s\over r}.            \tag{3.1}
\]

Install arbitrary isometric \(C_{2r}\)-factors on \(P_0,P_1\).  On every
component the direction word is \(\pi\pi\), with every direction of \(D\)
appearing once in each lap.  Orient all components, so every owner is one
directed start.

For a start \(x\), write \(\tau_{q}^{\epsilon}(x)\) for its signed literal
target obtained from the directed \(q\)-window, \(\epsilon\in\{-,+\}\).

### Theorem 3.1 (exact (q/r) persistent-flag obstruction)

Let \(1\le q<r\).  Replace the old resolution by the new resolution and
install arbitrary isometric compiler factors on \(Q_0,Q_1\).  For each sign
\(\epsilon\),

\[
 \left|\left\{x\in P_0\dot\cup P_1:
   \tau_{q,\mathrm{new}}^{\epsilon}(x)
   \ne\tau_{q,\mathrm{old}}^{\epsilon}(x)\right\}\right|
 \ge 2qg_r.                                        \tag{3.2}
\]

#### Proof

Fix one old packet.  A component has length \(2r\), and direction \(i\)
occurs twice, with cyclic separation \(r\).  Since \(q<r\), the directed
\(q\)-windows containing the two occurrences are disjoint.  Exactly \(2q\)
starts on the component have a window containing \(i\).  The packet has
\(s/(2r)\) components, so exactly

\[
                         2q\,{s\over2r}=qg_r        \tag{3.3}
\]

starts in that packet use \(i\).  The two old packets therefore have exactly
\(2qg_r\) such starts.

Let the physical pair representing \(i\) have endpoints \(a_i,b_i\).
An old window which traverses \(i\) contains owners in both orientations of
this pair.  Its lower literal target, the intersection along the window,
contains neither endpoint.  Its upper literal target, the union along the
window, contains both endpoints.

In every new packet, direction \(i\) is frozen.  All owners of one new
packet contain the same one of \(a_i,b_i\) and omit the other.  Thus every
new lower target contains the selected frozen endpoint, while every new
upper target omits the opposite endpoint.  Neither target can equal the old
target for any of the starts counted in (3.3), independently of the new
compiler order.  This proves (3.2) for both signs. \(\square\)

### Corollary 3.2 (aggregate all-depth cost of persistent transport)

For \(H<r\), the sum of the ownerwise Hamming distances over both signs and
all \(q\le H\) is at least

\[
 \sum_{q=1}^{H}\sum_{\epsilon=\pm}
 d_H(\tau_{q,\mathrm{new}}^\epsilon,
     \tau_{q,\mathrm{old}}^\epsilon)
 \ge 2g_rH(H+1).                                  \tag{3.4}
\]

In particular, the ownerwise half-cube restrictions of a complete old
literal flag table never glue to a complete new literal compiler table
under a nontrivial raw slab.

The bound concerns transport of one fixed flag table.  It is not a lower
bound on the final CPCR energy: changing these flags in a correlated
compound move may be beneficial.

## 4. Frame leakage forbids a branchwise raw-slab Beneš layer

A cross-parent slab theorem applies to two packets with one common active
frame.  This gives the following elementary but decisive composition law.

### Theorem 4.1 (independent-predecessor transverse-layer obstruction)

Let \(v,w\) be two raw slab nodes.  Node \(v\) has possible output frames
\(D_v^0,D_v^1\), and node \(w\) has possible output frames
\(D_w^0,D_w^1\), where both nodes are nontrivial:

\[
                         D_v^0\ne D_v^1,\qquad D_w^0\ne D_w^1. \tag{4.1}
\]

Suppose a fixed next-stage physical slab is to pair one output packet of
\(v\) with one output packet of \(w\), and is required to remain legal for
all four independent predecessor settings.  This is impossible.

#### Proof

Legality of the next slab requires its two input packets to have the same
active frame.  Branchwise availability would therefore give

\[
                         D_v^a=D_w^b
              \qquad\hbox{for all }a,b\in\{0,1\}.  \tag{4.2}
\]

Fixing \(b=0\) in (4.2) yields \(D_v^0=D_v^1\), contradicting (4.1).
\(\square\)

Thus a fixed transverse recursive network cannot treat raw predecessor
bits as a Cartesian family of independent Beneš switch bits.  The theorem
does not rule out:

* a correlated subset of settings;
* a branch-adaptive decision tree whose later slab supports depend on the
  earlier choices; or
* a compound logical switch whose two states are restored to the same
  terminal frame before the next transverse layer.

It proves that one of these extra mechanisms is necessary.

### Corollary 4.2 (local frame restoration erases packet-home action)

Fix one physical support \(\mathcal S\cong Q_{r+1}\).  Suppose two
compound resolution states of \(\mathcal S\) both finish as two physical
\(Q_r\)-packets with the same common active frame \(E\), where
\(E\) is an \(r\)-subset of the \(r+1\) slab axes.  Then the two terminal
packet partitions are identical.

In particular, replacing a raw node by a compound node whose two logical
states have the same terminal frame cannot produce a straight/cross action
on physical packet homes inside the same slab support.  One may of course
rename the two output facets, but this changes neither their owners nor
their literal target columns.  Any nontrivial physical logical bit which
survives frame restoration must therefore be carried by different compiler
states or ordered-port holonomy on the same terminal packets.

#### Proof

There is one slab axis \(a\notin E\).  A physical \(Q_r\)-packet in
\(\mathcal S\) with active frame \(E\) is obtained by freezing \(a\) to
one of its two orientations.  Hence the only two such packets are
\(\{x_a=0\}\) and \(\{x_a=1\}\), and together they give the unique
\(E\)-parallel foliation of \(\mathcal S\).  Both terminal states must be
this foliation. \(\square\)

Thus the three escapes listed after Theorem 4.1 are not equivalent.
Correlation or branch adaptation can retain a genuine re-foliation.
Local frame restoration on a fixed slab can retain only compiler
holonomy; it cannot turn the slab into an owner-home permutation switch.

## 5. Repeated-axis law and exact direction telescoping

Along the packet containing a fixed owner, every traded node changes the
active frame by

\[
                D_{t+1}=D_t\setminus\{i_t\}\cup\{e_t\},
                \qquad i_t\in D_t, e_t\notin D_t.              \tag{5.1}
\]

A straight node leaves \(D_t\) unchanged.  For a physical axis \(a\), let
\(A_a(t)\) and \(R_a(t)\) count its activations and removals through time
\(t\).  Then

\[
 A_a(t)-R_a(t)
  =\mathbf1_{\{a\in D_t\}}-\mathbf1_{\{a\in D_0\}}.            \tag{5.2}
\]

In particular, changes of one axis must alternate between activation and
removal, and a route returning to its initial frame activates and removes
every axis equally often.  Equation (5.2), not a free word in exchange
generators, is the exact repeated-axis constraint.

There is also a global version.  At stage \(t\), let

\[
                   C_t=\sum_{P\text{ current}}\mathbf1_{D(P)}  \tag{5.3}
\]

be the active-frame census of the packet factor.  One slab trade changes
\(C_t\) by

\[
                              2(e_e-e_i).           \tag{5.4}
\]

At signed depth \(q<r\), one packet contributes \(qg_r\) windows containing
each active direction.  Hence its global direction-support incidence vector
is

\[
                              Z_q(t)=qg_rC_t,        \tag{5.5}
\]

and every fixed-dimension sequence satisfies the exact telescope

\[
 Z_q(T)-Z_q(0)
   =qg_r(C_T-C_0)
   =2qg_r\sum_{\text{traded slabs }a}(e_{e_a}-e_{i_a}).         \tag{5.6}
\]

Thus equal initial and terminal frame census kills the complete
direction-support residue at every protected depth and both signs.  It does
not imply equality of literal targets.  The residual literal derivative may
lie in the common kernel of all direction-support projections, exactly the
floor-covariance difficulty retained by CPCR.

## 6. Alignment with CPCR

The preceding results separate two statements which must not be conflated.

1. **Persistent transport.** Start with one prescribed ownerwise nested-flow
   table and attempt to carry it through a routing network unchanged.  Raw
   slabs fail this statement by Theorem 3.1.  They also fail the fixed
   independent-switch topology by Theorem 4.1.
2. **Resolution selection.** Use a correlated sequence of slabs to choose a
   final exact packet atlas, then install legal compiler states whose common
   all-depth load vector satisfies the integer floor covariance target.
   This is CPCR.  Theorem 3.1 does not refute it, because CPCR is allowed to
   change ownerwise targets; Theorem 5.1 of the local-minimum analysis also
   shows why such changes may have to be compound rather than individually
   downhill.

The ideal Beneš theorem would become relevant only after construction of a
logical two-state gadget satisfying all of the following:

* both states have the same terminal packet frames and exterior orientations;
* its two states act as a genuine permutation on a declared family of legal
  complete compiler bundles, rather than as the half/half re-foliation
  (2.3);
* transverse copies remain branchwise available; and
* the compound literal derivatives obey the common all-depth CPCR quota.

No such gadget is supplied by one \(Q_{r+1}\) slab.

## 7. Exact boundary

Proved:

* exact ideal Beneš permutation universality for \(N=2^L\), with the stage
  and switch counts (0.1);
* exact typed-home universality for already grouped indivisible atoms;
* exact integral owner preservation in any stage-aligned physical bank;
* the half/half intersection law (0.2);
* impossibility of nontrivially permuting whole owner-attached packet bundles;
* the exact \(q/r\) lower bound (3.2) for transport of persistent literal
  flags;
* the branchwise transverse-layer obstruction of Theorem 4.1; and
* collapse of every fixed-support frame-restored logical node to one
  terminal packet foliation;
* the repeated-axis and direction-census telescoping identities
  (5.2)--(5.6).

Not proved:

* a frame-restored compound logical switch;
* a correlated raw-slab family large enough to realize every required CPCR
  resolution state;
* a branch-adaptive physical decision tree of near-spanning owner density;
* cancellation of the literal kernel residue; or
* CPCR and coefficient one.

The multiscale raw-slab Beneš proposal therefore fails as a literal router
of a preassigned balanced nested flow.  Its surviving use is as a correlated
re-foliation mechanism inside the unresolved CPCR selection problem.
