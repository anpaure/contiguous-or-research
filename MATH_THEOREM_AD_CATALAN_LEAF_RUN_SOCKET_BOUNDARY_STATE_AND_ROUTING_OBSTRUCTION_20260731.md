# Leaf--run--socket gluing state: exact composition and the routing obstruction

Date: 2026-07-31  
Status: exact finite-interface composition theorem in the residual-host
normal form; exact \(d+3t\) decoration-linkage width; literal Johnson
permutation obstruction to a dimension-independent socket alphabet; no
all-dimension accepting-state theorem

## 0. Verdict

The leaf-peelable transparent-hexagon state and the strict trace state do
compose, but they do not absorb the endpoint-socket problem.

For a fixed gluing tree, the exact node record is a **correlated relation**
of five coordinates:

\[
 {\cal B}_x\subseteq
 {\cal A}_x\times{\cal G}_x\times{\cal R}_x
             \times{\cal F}_x\times{\cal S}_x.       \tag{0.1}
\]

Here:

1. \({\cal A}_x\) contains the current transparent-decoration interface
   and, when the representatives are allowed to change, the chosen
   common-core matching together with its exact augmenting-linkage
   signature.
2. \({\cal G}_x\) is the labelled connectivity state of the
   gap--colour forest.
3. \({\cal R}_x\) is the finite strict-run monoid.
4. \({\cal F}_x\) is the phase-indexed labelled physical path kernel.
5. \({\cal S}_x\) is the lower-labelled socket path-cover profile.

The word “correlated” is essential.  Independent feasible projections of
the five coordinates need not have one common witness.

There is no context-free meaning of “the smallest state”: two node records
may be identified only relative to a declared family of exterior
continuations.  In the normalized bounded-interface category below, the
gap partition is the canonical minimum for forest additions, item 2169
gives the exact linkage relation, and Section 8 gives a sharp lower bound
for routing-complete socket contexts.  The displayed encodings of the run
and physical kernels are exact finite representations, not claims of a
unique syntactic minimum.

For a Hamilton-safe alternating \(2t\)-circuit, the first coordinate has
width at most

\[
                         d+3t,                       \tag{0.2}
\]

where \(d\) is the old augmented matching deficiency.  It has width at most
\(3t\) from a decorated parent.  This is a genuine finite-state
consequence, but its augmenting paths may travel globally.

The gap coordinate is finite on a bounded interface, and the run coordinate
has a dimension-independent finite alphabet.  The socket coordinate is
different.  Without an additional locality theorem, every completed
physical path remains live because it may connect to any later path.  For
every permutation \(\pi\in S_n\), a literal Johnson path system realizes
the residual-host socket digraph of \(\pi\), with both upper and lower
connector labels valid.  All \(n!\) routings are distinguishable by exterior
routing contexts in the abstract labelled-routing algebra.  Thus an
unrestricted routing-complete socket state cannot be a dimension-independent
finite alphabet.  This does not assert that all distinguishing contexts are
simultaneously trace-realizable, transparent and leaf-peelable.

There is a positive bounded subclass: if the desired socket Hamilton cycle
is contiguous with respect to the gluing tree, every proper node carries
one socket chain, and one endpoint triple plus its used lower-colour set is
necessary and sufficient.

The smallest physical independence witness remains \(m=2\): its
leaf-peelable gap graph and strict trace both pass, but its residual socket
digraph lacks one direction.  Decoration alone does not supply sockets.

## 1. Exact scope and normalized gluing nodes

Fix \(m\ge2\), a standard middle-levels factor on \(2m-1\) old coordinates,
and a rooted tree of dynamically chosen alternating switch polygons.
A node \(x\) contains oriented retained chronology fragments.  Its parent
may touch the node only through a declared finite interface
\(\partial x\).

We impose the following normalization.

1. Every chronology edge, gap-incidence edge, or physical-lift edge which
   an ancestor may delete is exposed at the child boundary.
2. Gap vertices use stable occurrence identifiers, for example the
   preceding selected \(A\)-occurrence.  They are not identified merely by
   an endpoint pair which may change under a toggle.
3. Every physical chronology port retains enough labelled halo to determine
   a turn chord centred at the port and a residual cross edge crossing the
   port.
4. If an unmarked fragment is not bounded by its two selected marks inside
   the node, both possible residual-matching boundary phases are retained.

Condition 1 is the **no hidden reopening** convention.  If a later toggle
may delete a hidden interior edge, a boundary connectivity partition alone
is not sufficient; either that edge must be exposed or the full
deletion-aware forest response must be carried.

The target at the root is the conjunction of:

1. a fixed or newly selected alternating decoration whose gap--colour graph
   is a balanced forest;
2. the strict cyclic trace condition
   \[
     \text{every zero-run has length at least four, and every one-run has
     even length};                                   \tag{1.1}
   \]
3. the residual-host normal form of item 2162: every physical path has one
   terminal residual host \(q_C\), and the endpoint-labelled socket graph
   has a uniformly outgoing directed Hamilton cycle;
4. when the intermediate lower floor is requested, the connector lower
   colours are pairwise distinct.

Primitive quotient voltage, deeper shadows, residence and the common-cap
compiler are outside this theorem.

## 2. Decoration state and the \(d+3t\) linkage bound

### 2.1 Fixed-decoration transparent mode

Suppose the same selected turn occurrences are carried through a polygon
toggle.  For every retained fragment record

\[
  \alpha(P)=
  \begin{cases}
    \varnothing,&P\text{ contains no selected occurrence},\\
    (\operatorname{firsttype}(P),\operatorname{lasttype}(P)),
      &\text{otherwise}.
  \end{cases}                                        \tag{2.1}
\]

Also record, separately on the two shores, the selected local turn-colour
multisets at every active polygon vertex.

The toggle is transparent exactly when:

1. both local selected colour multisets are unchanged; and
2. after empty selected subsequences are discarded, consecutive nonempty
   fragment subsequences have opposite last/first shore types in every new
   factor cycle.

This is the exact transparent-polygon state from item 2158.

### 2.2 Representative-changing mode

Let \({\cal A}\) and \({\cal A}'\) be the old and new augmented trace
graphs.  Their perfect matchings are exactly the old and new alternating
decorations.  Suppose an alternating \(2t\)-circuit changes the factor.
Put

\[
 H={\cal A}\cap{\cal A}',\qquad
 N=|\text{one shore}|,\qquad
 d=N-\nu({\cal A}),\qquad
 r=N-\nu(H).                                         \tag{2.2}
\]

### Lemma 2.1 (exact bounded common-core width)

\[
                              r\le d+3t.              \tag{2.3}
\]

For any maximum matching \(M\) of \(H\), the new factor is decorable if and
only if \({\cal A}'\) contains \(r\) pairwise vertex-disjoint
\(M\)-augmenting paths covering all \(2r\) vertices exposed by \(M\).

#### Proof

The circuit removes at most \(t\) old physical-incidence edges, at most
\(t\) old upper-turn augmented edges, and at most \(t\) old lower-turn
augmented edges.  Restrict an old maximum matching of size \(N-d\) to
\(H\).  At most \(3t\) of its edges disappear, so

\[
 \nu(H)\ge N-d-3t,
\]

which is (2.3).  The symmetric difference of \(M\) with a perfect matching
of \({\cal A}'\) contains exactly \(r\) vertex-disjoint augmenting paths
covering the exposed vertices.  Conversely, toggling a complete such
linkage increases \(|M|\) by \(r\) and gives a perfect matching.
\(\square\)

Thus a decorated parent has linkage width at most \(3t\).  The exact node
state is not the scalar \(r\), but the chosen common-core maximum matching
\(M\) and the realized terminal-linkage relation:
which oriented collections of vertex-disjoint path fragments connect which
exposed terminals.  If the adhesion has \(b\) named vertices, put
\[
                         p=b+2r.
\]
A safe crude bound on the oriented endpoint patterns is
\[
                         4^p p!=2^{O(p\log p)}.       \tag{2.4}
\]
In particular \(p\le b+6t\) from a decorated parent.

The paths may pass through the whole retained augmented graph.  Bound
(2.3) proves bounded width, not bounded length, locality, or existence.

For a fixed transparent decoration, this linkage coordinate is the
diagonal state and may be omitted.  If representatives change, the linkage
produces a new perfect matching, after which its current palette/fragment
decoration interface must still be carried for later toggles.  Every
linkage choice remains correlated in (0.1) with that interface, its induced
gap graph, trace and physical socket data.

## 3. The leaf-peelable gap coordinate

Fix one carried decoration.  Let \(\Gamma\) be its gap--lower-colour graph,
and assume \(\Gamma\) is a balanced forest.  The selected lower occurrences
already display a perfect matching of \(\Gamma\); hence that matching is
unique.

At one toggle write

\[
 D=E(\Gamma)\setminus E(\Gamma'),\qquad
 S=E(\Gamma')\setminus E(\Gamma).                    \tag{3.1}
\]

Let \(B\) be the stable labelled gap/colour vertices incident with \(S\).
After deleting \(D\), define

\[
 \Pi_\Gamma(D)
   =\text{the partition of }B\text{ into components of }\Gamma-D.
                                                               \tag{3.2}
\]

### Theorem 3.1 (minimal completed-factor gap state)

For a fixed transparent decoration, \(\Gamma'\) is a balanced forest if and
only if the multigraph induced by \(S\) on the blocks of
\(\Pi_\Gamma(D)\) is loopless and acyclic.

No matching-exposure mask is needed in this completed-factor mode.

#### Proof

Transparency already transports the displayed perfect matching to
\(\Gamma'\).  The graph \(\Gamma-D\) is a forest.  Adding \(S\) preserves
acyclicity exactly when no new edge lies inside one old component and the
component-level attachment multigraph is acyclic.  A forest with a perfect
matching has a unique, leaf-peelable matching. \(\square\)

The partition in (3.2) is Myhill-minimal for addition after the declared
deletions.  If two states give different partitions, choose named
\(u,v\in B\) connected in one and not the other.  Add one fresh matched
pair \(z,w\), one vertex on each shore.  If \(u,v\) are on opposite shores,
join them by the new length-three path \(u-w-z-v\), with \(zw\) the new
matching edge.  If they lie on the same shore, take \(w\) on the opposite
shore, make \(z\) a leaf at \(w\), and add \(uw,vw,zw\).  In either case
the old matching plus \(zw\) remains perfect, while a cycle is created
exactly in the first state.  Thus the distinction is witnessed inside the
balanced bipartite leaf-peelable category.

Hence an interface of size \(b\) has up to \(\operatorname{Bell}(b)\)
connectivity states, plus rejection.  A single hexagon is finite, but a
node exposing unboundedly many gap incidences does not have a constant
alphabet.

### 3.2 Open bottom-up nodes

If a bottom-up node has open gap vertices and its matching is not yet
closed, its exact state is

\[
                    (B,\Pi_\Gamma,\mu),              \tag{3.3}
\]

where \(\mu(v)=1\) records that the boundary vertex \(v\) is already matched
inside the node.  Every interior vertex which will never reappear must
already be matched, and no closed interior component may be deficient.
At a glue, quotient the child connectivity blocks, add the local incidence
edges, require the quotient to be loopless and acyclic, and update the
matching exposure mask.

For a search over representatives, the state is the feasible relation of
possible masks, not one independently chosen mask.

If a future operation may delete a hidden interior edge, (3.3) is not
complete.  One must retain the corresponding deletion-response table, or
the relevant boundary forest itself.  This is precisely why the
normalization in Section 1 is required.

## 4. A finite exact strict-run monoid

The decoration coordinate already proves that consecutive selected marks
have opposite shore types.  Therefore every completed zero-run is even.
The strict run test need not store that parity a second time.

For \(n\ge1\), define the boundary descriptors

\[
 z(n)=\min(n,4)\in\{1,2,3,4\},\qquad
 o(n)=n\bmod2\in\{0,1\}.                             \tag{4.1}
\]

For every nonempty linear trace fragment \(w\), record:

1. its first and last bits;
2. the descriptor \(z(n)\) for a boundary zero-run and \(o(n)\) for a
   boundary one-run;
3. whether all of \(w\) is one run; and
4. whether every completed internal zero-run has length at least four and
   every completed internal one-run is even.

Add one empty state and one absorbing failure state.  This gives at most
44 states per oriented fragment after the decoration coordinate is imposed.

### Theorem 4.1 (exact strict-run composition)

Reversal swaps the prefix and suffix descriptors.  On concatenation,
equal boundary bits merge, with capped addition for \(z\) and parity
addition for \(o\); unequal bits complete both boundary runs and test them.
At the root apply the same rule to the cyclic suffix/prefix pair.

The root accepts exactly condition (1.1).

#### Proof

All runs strictly inside a child are summarized by its internal-good bit.
Only the two runs meeting a new seam can change.  If their bits agree they
form one run, and (4.1) retains exactly the information relevant to a later
test.  If the bits differ, both become complete and can be tested
immediately.  The homogeneous flag prevents treating the same run as two
different boundary runs.  The final cyclic merge is identical.

Alternation from Section 2 already supplies evenness of complete zero-runs,
so the zero threshold is the only remaining zero condition. \(\square\)

This 44-state representation is a convenient exact upper bound, not a claim
of global Myhill minimality after it is producted with the decoration
coordinate.  For example, that coordinate may already distinguish an
all-zero fragment from a fragment containing a completed selected block,
allowing further quotienting.  The threshold \(1,2,3,4+\), one-run parity,
homogeneous flag and absorbing failure nevertheless give a direct
deterministic transfer without referring back to the full word.

A protected \(0^4\) block is a convenient sufficient invariant for the
weaker forest condition, but it is not the exact strict-run state (1.1).

## 5. Phase-indexed physical path state

The run monoid does not determine the literal physical forest.  A retained
fragment containing no selected mark may lie inside a longer zero-run.
The forced residual matching on that fragment has two boundary phases:
the first exposed zero may match rightward inside the fragment or leftward
across its boundary.  Even an even-length subfragment has two phases unless
both bounding marks are already present and protected.

Define \({\cal F}_x\) to be a labelled cut-open path skeleton retaining:

1. every labelled physical middle vertex exposed to an ancestor, with its
   current degree deficit;
2. the reduced path graph on the exposed vertices and retained hosts,
   including their incidence and order along each path piece;
3. the exact two-phase boundary relation of every open unmarked fragment;
4. every unsuppressed residual edge \(q\), its upper label \(U(q)\), and
   whether it is terminal in its current path piece; and
5. a failure flag for any closed physical cycle which contains no exposed
   edge available to a declared future deletion.

Internal degree-two vertices which are neither future chronology ports nor
residual hosts may be suppressed.  The local halo retained at a chronology
port determines every turn chord

\[
                    v_{r-1}v_{r+1}
\]

and every residual cross edge affected by a parent reconnection.

### Lemma 5.1 (sufficient exact physical-kernel update)

Under the no-hidden-reopening normalization, the state \({\cal F}_x\) is
enough to update the literal physical lift through a parent polygon toggle,
and the restriction of every final witness induces such a state.

When a component becomes permanently closed inside the processed node,
it is admissible in the residual-host normal form exactly when it contains
one residual edge \(q_C\), that edge is terminal, and the path has the
literal record

\[
                         (t_C,h_C,U_C),               \tag{5.1}
\]

where \(t_C\) is the terminal endpoint of \(q_C\), \(h_C\) is the opposite
path endpoint and \(U_C=u(q_C)\).  If \(C=q_C\) is isolated, retain its two
orientation choices.

After emitting (5.1) into the socket coordinate, remove that finalized path
from the active physical skeleton; do not retain a duplicate copy.

#### Proof

Every changed physical edge is incident with an exposed chronology halo,
so the local edge formula from item 2162 computes the update.  The reduced
labelled path graph retains the order and incidence of every host and every
future port, while suppressing only inert internal subdivision.  The phase
relation is exactly the missing datum for residual pairs crossing an
unmarked boundary.  A permanently closed cycle cannot be broken by any
allowed continuation and is rejected.  Suppressing a nonhost internal
degree-two vertex changes neither future degrees, endpoints nor host
records.  The final record statement is item 2162's one-terminal-host
theorem.  No minimality of this concrete encoding is asserted. \(\square\)

## 6. Exact socket path-cover profile

Let \({\cal C}\) be a set of finalized path components with records (5.1).
For isolated hosts, expand the two orientation choices.  A legal directed
socket arc is

\[
 C\longrightarrow C'
 \quad\Longleftrightarrow\quad
 h_C\cup t_{C'}=U_{C'}.                              \tag{6.1}
\]

Its lower label is

\[
                         \lambda(C,C')
                              =h_C\cap t_{C'}.         \tag{6.2}
\]

A directed socket chain \(C_1,\ldots,C_s\) has signature

\[
 \theta(C_1,\ldots,C_s)
  =\bigl((t_{C_1},U_{C_1}),\,h_{C_s},\,\Lambda\bigr), \tag{6.3}
\]

where its internal lower labels are required to be pairwise distinct and
\(\Lambda\) is their set.  Equivalently, admissible chain signatures are
generated from singleton chains by the partial product below; an internal
label repetition is never collapsed into a set.

For two vertex-disjoint chains define

\[
 ((t,U),h,\Lambda)\star((t',U'),h',\Lambda')
   =((t,U),h',\Lambda\cup\Lambda'\cup\{h\cap t'\})   \tag{6.4}
\]

exactly when

\[
 \begin{split}
 h\cup t'&=U',\\
 \Lambda\cap\Lambda'&=\varnothing,\\
 h\cap t'&\notin\Lambda\cup\Lambda'.
 \end{split}                                         \tag{6.5}
\]

If lower-floor injectivity is not required, delete \(\Lambda\) and the last
two conditions.

### Theorem 6.1 (socket-profile equivalence)

Prune socket-empty branches, or designate as the socket root the first
gluing node containing every finalized component.  Thus every proper socket
node below it represents a strict subset of the final component set.

For an unrestricted socket order, the exact state of such a proper node is the
set of all covers of its finalized component records by any number of
vertex-disjoint directed chains, represented by the multiset of signatures
(6.3) and their pairwise-disjoint used lower-label sets.  A proper internal
directed cycle is rejected.

At the root, a state accepts exactly when it contains one chain
\(((t,U),h,\Lambda)\) satisfying

\[
             h\cup t=U,\qquad h\cap t\notin\Lambda.   \tag{6.6}
\]

This is equivalent to a uniformly outgoing residual-host Hamilton closure
with pairwise-distinct connector lower colours.

#### Proof

Restrict any final directed Hamilton cycle to the component vertices below
a proper gluing node.  Since a proper subset cannot contain a closed cycle
of the final Hamilton cycle, the restriction is a disjoint union of
directed chains.  Every internal arc satisfies (6.1), and lower
injectivity gives disjoint \(\Lambda\)'s.  Hence it yields one recorded
profile.

Conversely, disjoint child chains may be joined exactly by (6.4)--(6.5).
Associativity follows because the first entrance, last exit and union of
used labels are independent of parenthesization.  Induction over the
gluing tree reconstructs the represented chain cover.  At the root,
(6.6) adds the last legal fresh-colour arc and makes one directed Hamilton
cycle.  Item 2162 then gives the literal uniformly outgoing closure.
\(\square\)

### Corollary 6.2 (tree-contiguous positive subclass)

Call a socket Hamilton cycle \(T\)-contiguous when, for every proper
gluing-tree node, the components finalized below that node occupy one cyclic
interval of the socket cycle.

In this subclass every proper node carries one chain.  Therefore its exact
socket state is just the feasible set of triples (6.3), with product
(6.4).  This one-chain state is necessary and sufficient for
\(T\)-contiguous closure.

It is not without loss of generality for an unrestricted closure.  A global
Hamilton cycle may enter and leave one subtree arbitrarily many times, so
its restriction can have arbitrarily many chains.

## 7. Exact joint composition theorem

At a search node, let \({\cal B}_x\) be the set of jointly realizable tuples
in (0.1); do not replace it by the Cartesian product of its projections.

### Theorem 7.1 (leaf--run--socket gluing composition)

Assume:

1. the gluing tree satisfies the normalized finite-interface convention of
   Section 1;
2. every fixed-decoration toggle is tested dynamically by Section 2.1;
3. every representative-changing \(2t\)-toggle carries the complete
   common-core linkage relation of Section 2.2;
4. all node operations use the same literal occurrence and coordinate
   labels across the five state coordinates.

Then the following are equivalent.

1. Choices below the root give a leaf-peelable alternating decoration, the
   strict trace condition (1.1), and a uniformly outgoing residual-host
   socket Hamilton closure; if requested, all connector lower colours are
   distinct.
2. Bottom-up propagation of the correlated state relation (0.1) has an
   accepting root tuple, where:
   * the decoration/linkage coordinate is perfect;
   * the gap coordinate has no exposed matching deficit and its labelled
     attachment graph is a forest;
   * the cyclic run monoid accepts;
   * the physical kernel has no open chronology port and emits exactly one
     terminal-host record per path; and
   * the socket profile satisfies (6.6).

#### Proof

For necessity, restrict a final witness to every subtree.  The decoration
restricts to the local palette/boundary state, or to the common-core
augmenting paths when representatives change.  Deleting the parent-changed
gap edges gives the partition (3.2).  Cutting the trace gives its run
summary and residual phase relation.  Cutting the physical forest gives
its path kernel.  Finally, restricting the socket Hamilton cycle gives the
chain cover in Theorem 6.1.  All five restrictions come from the same
witness, so they form one tuple in the correlated relation.

For sufficiency, induct from the leaves.  The transparent or linkage test
gives one alternating decoration.  The quotient-forest update preserves a
balanced gap forest and hence its unique matching.  The run monoid proves
(1.1).  The physical kernel reconstructs the literal forest and its
terminal-host records.  The socket products reconstruct one lower-injective
directed Hamilton cycle.  These operations use the same tuple labels, so no
incompatible marginal choices are combined. \(\square\)

Theorem 7.1 is a decision/composition theorem.  It does not assert that the
root relation is nonempty for every \(m\).

## 8. Why the socket coordinate is not a fixed finite alphabet

### Theorem 8.1 (literal permutation realization)

For every \(n\ge2\) and every permutation \(\pi\in S_n\), there is a
literal Johnson path system of \(n\) vertex-disjoint four-edge paths with:

1. one designated terminal host per path;
2. pairwise-distinct host upper labels;
3. a residual socket digraph with arc permutation \(\pi^{-1}\); and
4. pairwise-distinct lower labels on the selected permutation arcs.

Consequently the full upper-and-lower socket gate accepts exactly when
\(\pi\) is one cycle.

#### Construction and proof

Put \(m=3n-1\).  Partition a \(2m\)-set as

\[
 C\ \dot\cup\ P\ \dot\cup\ Q\ \dot\cup\ Y\
       \dot\cup\{d\},                                 \tag{8.1}
\]

where

\[
 |C|=m-2,\qquad
 P=\{p_i\}_{i=1}^n,\quad
 Q=\{q_i\}_{i=1}^n,\quad
 Y=\{y_i\}_{i=1}^n.                                  \tag{8.2}
\]

The count is

\[
 (m-2)+n+n+n+1=2m.
\]

For \(j=\pi(i)\), define

\[
 \begin{split}
 h_i&=C+p_i+q_i,\\
 t_i&=C+q_j+y_i,\\
 s_i&=C+p_j+y_i,
 \end{split}                                         \tag{8.3}
\]

and designate \(t_is_i\) as the terminal host.  Its upper label is

\[
                  U_i=C+p_j+q_j+y_i.                 \tag{8.4}
\]

Complete the path

\[
                    t_i-s_i-r_i-w_i-h_i              \tag{8.5}
\]

by

\[
 (r_i,w_i)=
 \begin{cases}
  (C+p_i+y_i,\ C+p_i+d),&j\ne i,\\
  (C+d+y_i,\ C+q_i+d),&j=i.
 \end{cases}                                         \tag{8.6}
\]

Every set in (8.3)--(8.6) has size \(m\).  Consecutive sets differ by one
deletion and one insertion, so every displayed edge is Johnson.  The
\(Y\)-tags separate all \(t_i,s_i,r_i\); the \(P,Q,d\) labels separate the
\(w_i,h_i\).  Different path types have different numbers or kinds of
outside-\(C\) labels.  Thus all displayed vertices are distinct.

For a possible predecessor \(h_a\),

\[
 h_a\cup t_i=U_i
 \quad\Longleftrightarrow\quad
 a=j=\pi(i).                                         \tag{8.7}
\]

Indeed, equality holds for \(a=j\).  If \(a\ne j\), the union contains
\(p_a\) or \(q_a\), which is absent from \(U_i\).
Therefore the only socket arc into component \(i\) comes from component
\(\pi(i)\), so the directed permutation is \(\pi^{-1}\) and has the same
cycle type as \(\pi\).

The selected connector lower label is

\[
 h_{\pi(i)}\cap t_i=C+q_{\pi(i)},                    \tag{8.8}
\]

and these labels are pairwise distinct.  Equations (8.7)--(8.8) prove all
claims. \(\square\)

For \(n=2\), this uniform construction already works at \(m=5\): the
transposition closes and the identity does not, although all paths have the
same unlabelled length, degree and terminal-host profile.

### Proposition 8.2 (smallest four-edge calibration)

There is already an identity/transposition pair in \(J(6,3)\).  Write a
three-set as its concatenated digits.  The identity system is

\[
\begin{split}
 P_1&:012-013-014-024-023,\\
 P_2&:015-025-035-135-125.
\end{split}                                          \tag{8.9}
\]

The first edge of each path is the terminal host.  Thus

\[
 (t_1,h_1,U_1)=(012,023,0123),\qquad
 (t_2,h_2,U_2)=(015,125,0125).                       \tag{8.10}
\]

Its only socket arcs are the two loops, with lower labels \(02,15\).

The transposition system is

\[
\begin{split}
 Q_1&:012-013-014-015-025,\\
 Q_2&:023-035-034-134-123,
\end{split}                                          \tag{8.11}
\]

with

\[
 (t_1,h_1,U_1)=(012,025,0123),\qquad
 (t_2,h_2,U_2)=(023,123,0235).                       \tag{8.12}
\]

Its only socket arcs are \(Q_1\to Q_2\) and \(Q_2\to Q_1\), with lower
labels \(02,12\).  Hence the second system closes and the first does not.
Both systems consist of two vertex-disjoint four-edge Johnson paths on ten
distinct vertices, and both have distinct host upper labels and distinct
selected lower connector labels.

This is minimal under the two-path/four-edge specification: two
vertex-disjoint four-edge paths require ten distinct middle vertices, while
\(J(4,2)\) has only six. \(\square\)

### Theorem 8.3 (routing-state lower bound)

In the abstract labelled endpoint-routing composition algebra, the
\(n!\) permutation states of Theorem 8.1 are pairwise
completion-distinguishable.  Any exact routing-complete compositional state
therefore needs at least

\[
                         n!\text{ states}
\]

and at least

\[
                         \log_2(n!)=\Omega(n\log n)
\]

bits.

#### Proof

Let \(\pi\ne\pi'\), put \(\delta=\pi^{-1}\pi'\), and choose \(a\) moved by
\(\delta\).  Choose an \(n\)-cycle \(c\) with

\[
                         c(\delta(a))=a.
\]

For the exterior routing

\[
                         \rho=c\pi^{-1},
\]

we have

\[
 \rho\pi=c,
\]

which is Hamiltonian, whereas

\[
 \rho\pi'=c\delta
\]

fixes \(a\) and is not Hamiltonian.  Thus an exterior context distinguishes
every pair. \(\square\)

For odd \(n\), the same argument may be restricted to the even permutation
algebra, giving \(n!/2\) classes; a three-fragment reconnection is
topologically a 3-cycle.  Item 2158 does **not** prove that every such
routing context is simultaneously palette-transparent and leaf-peelable.
Hence Theorem 8.3 is an exact lower bound for the abstract labelled socket
category, not an unconditional lower bound for trace-realizable Catalan
states.

Its rigorous consequence for the present recursion is:

\[
 \boxed{\text{carry the occurrence-labelled socket path-cover profile,
 or prove a new locality theorem for transparent Catalan socket graphs}.}
\]

## 9. Strict separation and calibrated witnesses

Each successive implication among the three central gates is strict.

1. **Decoration does not imply a gap forest.**  Item 2158 has a transparent
   \(m=4\) toggle for which the new gap graph contains the literal
   \(K_{2,2}\) on gap vertices
   \(\{67,100\},\{67,76\}\) and lower colours \(65,68\).
   Palettes, alternation and physical linearity survive, but
   leaf-peelability fails.  The \(K_{2,2}\) is the smallest possible
   bipartite cycle; no claim of dimension-minimality is made.
2. **A leaf decoration does not imply the strict run condition.**  On the
   \(m=2\) middle-levels cycle, \(I=\{0\},J=\{1\}\) has trace
   \[
                              100100.
   \]
   Its gap graph is \(K_{1,1}\), but both zero-runs have length two and both
   one-runs are odd.  It is the unique physical cycle face.
3. **Leaf decoration plus strict runs do not imply sockets.**  The
   \(I=J=\{0\}\) trace
   \[
                              110000
   \]
   has the same leaf-peelable \(K_{1,1}\) gap graph and satisfies (1.1),
   but item 2162's residual socket digraph contains only
   \(C_1\to C_2\), not \(C_2\to C_1\).

The last example is the smallest nontrivial trace-derived counterexample to
omitting the socket coordinate.  A separately audited \(n=2,m=3\)
permutation pair in Proposition 8.2 is the smallest
same-length-four-path Johnson counterexample to replacing occurrence labels
by unlabelled component profiles.

### 9.1 The standard private-triple recursion fails before this state can accept

Item 2172 supplies a complementary global obstruction at \(m=5\).  In the
complete unmodified standard Merino--Mička--Mütze family there are exactly
two Hamilton outputs.  Each realizes only \(81\) of the \(84\) turn colours
on each shore and misses the lower orbit

\[
               \{73,146,292\}
       =\{001001001,010010010,100100100\}.            \tag{9.1}
\]

One of those two gluing trees is locally all-six palette-transparent at both
glues and has disjoint lower private triples

\[
                       \{82,84,88\},\qquad
                       \{50,52,56\}.                 \tag{9.2}
\]

Thus the local private attachment geometry can pass while the global
decoration palette already fails.  In the state language of this note, the
root is rejected in the decoration coordinate before the gap, run or socket
coordinates can repair it.  Consequently the exact composition theorem is
not an induction theorem for the unmodified standard family.  Any such
recursion must first add a palette-repair/nonstandard switch, change the
representatives or gluing family, or start from a different factor.  Item
2172 does not rule out a decorable \(ML(9)\) cycle or a nonstandard
private-triple construction.

## 10. Exact remaining boundary

Proved:

1. the exact correlated product state (0.1) and the root acceptance theorem;
2. the \(d+3t\) decoration-linkage width, with the warning that linkage may
   be global;
3. the Myhill-minimal gap connectivity partition on a declared bounded
   interface;
4. the finite strict-run monoid;
5. the phase-indexed physical path kernel;
6. the exact unrestricted socket chain-cover profile and the
   \(T\)-contiguous one-chain specialization;
7. the literal permutation realization and abstract routing lower bound;
8. the three strict-separation witnesses above, with only the minimalities
   stated individually in Section 9.

Not proved:

1. that every \(m\) admits an accepting correlated root state;
2. that a published Middle Levels gluing tree has bounded relevant
   interface after all required global augmenting paths are exposed;
3. that every transparent Catalan socket graph has bounded routing width or
   a \(T\)-contiguous Hamilton cycle;
4. a palette-repair mechanism which escapes the standard \(m=5\)
   private-triple obstruction of Section 9.1;
5. primitive quotient voltage, residence, deeper shadows or compiler
   compatibility.

Thus item 2169 bounds the **decoration repair width** of a bounded polygon.
It does not collapse the later endpoint socket Hamilton problem.

## 11. Sources and audit scope

The proof uses only the exact statements in:

* MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md;
* MATH_THEOREM_AD_CATALAN_TRACE_RESIDUAL_SOCKET_GATE_AND_M2_COUNTEREXAMPLE_20260731.md;
* MATH_THEOREM_CATALAN_BOUNDARY_LINKAGE_GAMMOID_STATE_20260731.md;
* MATH_THEOREM_CATALAN_TRACE_LONG_SWITCH_AUGMENTING_LINKAGE_20260731.md;
* MATH_THEOREM_CATALAN_SUPPLIED_FOREST_OCCURRENCE_CONNECTOR_VOLTAGE_20260731.md;
* MATH_THEOREM_CATALAN_PRIVATE_TRIPLE_STANDARD_M5_REFUTATION_20260731.md.

Three independent audits checked the gap state, the strict-run monoid, the
phase requirement, the socket chain product, and the permutation
construction.  A separate audit note freezes the decisive line-by-line
checks and all source hashes.

No new finite search is used in the composition proofs.  Section 9.1
imports the separately frozen exhaustive \(m=5\) census of item 2172.  No
SAT solve or web result is used.
