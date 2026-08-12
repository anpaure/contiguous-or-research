# Fresh-path permutohedra, sharp mark orientation, and the compound square-router gate

**Date:** 2026-08-06  
**Method:** exact fresh-event algebra, bipartite (b)-matching, and
alternating-route bookkeeping; no computation or search  
**Status:** proof-safe reduction.  The fresh-path fibre is a product of two
permutohedra, not merely the diagonal permutohedron obtained by commuting
paired swap events.  This gives an exact sharp-cap mark selector once the
insertion-event loads are at most ((d-1)L), and it gives a still smaller
two-port orientation problem after the unmarked level-two owners have been
chosen.  Neither statement by itself is a physical macro rounding: changing
the mark changes one lower portal and the level-one owner portals, and those
portals need a simultaneous alternating router.  A literal two-path example
shows that the abstract capacity selector and even the two-port orientation
criterion do not imply such a router.

## 1. The full fixed-endpoint fibre

Put

\[
                         m=d-1\ge2.                         \tag{1.1}
\]

Fix a rank-(t) set (S), an (m)-set (A\subseteq S), and an
(m)-set (B\subseteq[k]\setminus S).  Choose independent orders

\[
 \alpha=(a_1,\ldots,a_m)\in\operatorname{Ord}(A),\qquad
 \beta=(b_1,\ldots,b_m)\in\operatorname{Ord}(B),             \tag{1.2}
\]

and put

\[
 S_j(\alpha,\beta)
   =S\setminus\{a_1,\ldots,a_j\}
       \cup\{b_1,\ldots,b_j\},\qquad 0\le j\le m.           \tag{1.3}
\]

This is a fresh (d)-vertex Johnson path.  Conversely, after its two
endpoint event sets (A,B) are fixed, every fresh path has the form (1.3).
Thus the fibre has

\[
                              (m!)^2                         \tag{1.4}
\]

members.  The paired events

\[
                         e_i=(-a_i,+b_i)                     \tag{1.5}
\]

and their common permutations describe a valid diagonal subfibre, but they
do not describe all the freedom: deletion and insertion orders may be
permuted independently.  This is exactly the synchronized Boolean-chain
freedom in
`MATH_THEOREM_FRESH_FIFO_BLOCK_CHAIN_KERNEL_AND_PAYLOAD_ATLAS_GATE_20260805.md`.

### Theorem 1.1 (product-permutohedron square calculus)

Let (\tau_q=(q,q+1)), where (1\le q<m).

1. Replacing (alpha) by (alpha\tau_q) changes exactly the lower
   vertex in role (q).  If (C=S_{q-1}(\alpha,\beta)), the old and new
   vertices are
   
   \[
           C-a_q+b_q,\qquad C-a_{q+1}+b_q.                \tag{1.6}
   \]
   
   They are Johnson adjacent.
2. Replacing (\beta) by (\beta\tau_q) also changes exactly role (q),
   from
   
   \[
           C-a_q+b_q\quad\hbox{to}\quad C-a_q+b_{q+1}.    \tag{1.7}
   \]
   
   These two vertices are Johnson adjacent.
3. Performing both transpositions changes role (q) to
   
   \[
                              C-a_{q+1}+b_{q+1}.            \tag{1.8}
   \]
   
   The four choices form one literal Johnson square.  The original and
   diagonal choices are its opposite corners.

Consequently the order graph of a fixed endpoint fibre is

\[
                  \operatorname{Perm}(A)\mathbin\square
                  \operatorname{Perm}(B).                 \tag{1.9}
\]

#### Proof

Every prefix strictly before (q) contains neither of the transposed
events, while every prefix at or after (q+1) contains both.  Hence only
the (q)-th state changes.  Formulae (1.6)--(1.8) follow directly from
(1.3).  In (1.6) the two states exchange (a_q,a_{q+1}); in (1.7) they
exchange (b_q,b_{q+1}).  Those are Johnson edges.  Applying the two
independent exchanges gives the four-cycle and (1.9). \(\square\)

The independent deletion permutohedron is important.  It changes no FIFO
owner set in the synchronized normal form, although it changes the ordered
queue exported to the next block.  Thus it is owner-invisible locally but
not automatically chronology-closed.

## 2. Exact effect on the marked level-two owner

The second insertion mark is

\[
                              c(P)=b_2.                     \tag{2.1}
\]

For the punctured duplicate lift, write

\[
 R(P)=S\cup B,\qquad K_2(P)=S\cup\{b_1,b_2\}.             \tag{2.2}
\]

A level-two tail (Y\subseteq[k]\setminus R(P)) gives the unmarked owner

\[
                              T_2=K_2(P)\cup Y.             \tag{2.3}
\]

Equivalently, in one literal FIFO copy with incoming queue
(X=(x_1,\ldots,x_D)), the first two owners have the form

\[
 \begin{aligned}
 T_1&=S\cup\{x_2,\ldots,x_D\}\cup\{b_1\},\\
 T_2&=S\cup\{x_3,\ldots,x_D\}\cup\{b_1,b_2\}.
 \end{aligned}                                             \tag{2.4}
\]

### Theorem 2.1 (three kinds of adjacent insertion switch)

For an adjacent insertion transposition (\tau_q):

1. if (q=1), the unmarked level-two owner (T_2) is unchanged and the
   mark changes from (b_2) to (b_1); the lower vertex (S_1) and the
   level-one owner (T_1) change;
2. if (q=2), the mark changes from (b_2) to (b_3) and every
   level-two owner changes by
   
   \[
                              T_2-b_2+b_3;                  \tag{2.5}
   \]
3. if (q\ge3), both (T_2) and its mark are unchanged.

Every deletion-order transposition leaves all owner sets and the mark
unchanged inside the current block.

For an (h)-fold macro, item 1 preserves all (h) unmarked level-two
owners simultaneously, but changes the (h) level-one owners
simultaneously.

#### Proof

Deletion labels do not occur in (2.2)--(2.4).  Swapping (b_1,b_2)
preserves their unordered pair and hence (2.3), while the second ordered
label changes from (b_2) to (b_1).  Formula (2.4) shows the changed
level-one owner explicitly.  Swapping positions 2 and 3 replaces the
unordered first-two set by
({b_1,b_3}), proving (2.5).  A transposition after position 2 changes
neither the first-two set nor its second entry. \(\square\)

This corrects a tempting overstatement: the (q=1) switch is
**level-two-owner neutral**, not all-owner neutral.  Any integral use of it
must route the changed lower and level-one portals.

The theorem gives a useful fibre decomposition.  Before the mark is
oriented, one first chooses an unordered first-insertion pair
({u,v}\subseteq B), which determines the level-two kernel.  The two
orientations

\[
                         (b_1,b_2)=(u,v),(v,u)             \tag{2.6}
\]

use the same unmarked level-two owner and choose (v,u), respectively,
as the mark.

## 3. An exact sharp-cap Hall selector before physical routing

Let (mathcal P) be any family of fresh endpoint fibres.  For
(P\in\mathcal P), let (B(P)) be its (m)-element insertion-event
set.  We ask only for a mark

\[
                         c(P)\in B(P)                      \tag{3.1}
\]

with capacity (L) at each coordinate.  Put

\[
 R_s=|\{P\in\mathcal P:s\in B(P)\}|.                     \tag{3.2}
\]

### Theorem 3.1 (capacitated event-list selector)

The following Hall condition is necessary and sufficient for (3.1):

\[
 |\mathcal X|\le L\,\bigl|\bigcup_{P\in\mathcal X}B(P)\bigr|
 \qquad(\mathcal X\subseteq\mathcal P).                  \tag{3.3}
\]

In particular, the pointwise event-load bound

\[
                              R_s\le mL\quad(s\in[k])      \tag{3.4}
\]

implies a sharp-cap assignment.

Under (3.4), there is in fact a distribution on integral assignments for
which

\[
                    \Pr(c(P)=s)={1\over m}
                    \qquad(s\in B(P)).                    \tag{3.5}
\]

No higher-order cylinder is asserted.

#### Proof

Make (L) private copies of every coordinate and match each path to one
copy of one member of its insertion bank.  Ordinary bipartite Hall is
exactly (3.3).

For the sufficient condition, count the path--coordinate incidences from
a subfamily (mathcal X):

\[
 m|\mathcal X|
   \le\sum_{s\in N(\mathcal X)}R_s
   \le mL|N(\mathcal X)|.                                 \tag{3.6}
\]

Cancel (m) to obtain (3.3).

For (3.5), in the path--slot graph give every edge weight (1/(mL)).
Every path has (mL) incident edges, so its load is one.  A slot over
coordinate (s) has load (R_s/(mL)\le1).  The bipartite matching
polytope is integral, so this fractional point is a convex combination of
integral matchings saturating every path.  Summing the (L) slot
marginals over one coordinate gives (3.5). \(\square\)

At the optimal scale

\[
                              L=\left\lceil{M\over kd}\right\rceil,
                                                                  \tag{3.7}
\]

condition (3.4) asks for insertion-event loads of order

\[
                              mL\sim {M\over k}.            \tag{3.8}
\]

Thus the factor-(d) colour gap disappears *at the assignment stage*: a
coarse (M/k)-scale bound on the whole insertion bank would imply the
sharp (M/(kd))-scale mark cap.  What is not proved is an integral
near-factor satisfying (3.4), still less one with the owner cylinder.
Average event load alone does not imply (3.4).

## 4. After level-two owners are fixed: a two-port orientation theorem

Suppose each selected macro has already chosen its unordered pair

\[
                              e_P=\{u_P,v_P\}.             \tag{4.1}
\]

The pair determines the unmarked level-two owner fibre.  Orienting the edge
toward (v_P) means

\[
                         (b_1,b_2)=(u_P,v_P),              \tag{4.2}
\]

so its head is the mark.  Let (G) be the resulting coordinate
multigraph.

### Theorem 4.1 (exact port-orientation criterion)

The port edges can be oriented with mark indegree at most (L) if and
only if

\[
                              |E(G[X])|\le L|X|
                              \qquad(X\subseteq[k]).       \tag{4.3}
\]

In particular,

\[
                              \Delta(G)\le2L               \tag{4.4}
\]

is sufficient.  Under (4.4), the orientations may be distributed so that
each endpoint of every port edge is its mark with probability (1/2).

#### Proof

Match each port edge to one of (L) private slots at one of its two
endpoints.  Hall for this incidence graph reduces to (4.3): for an edge
subfamily (F), all its possible slots lie over (V(F)), and the worst
subfamily on a fixed vertex set (X) is (E(G[X])).  This proves the
criterion.

If (4.4) holds, then

\[
                         2|E(G[X])|\le\sum_{x\in X}\deg_G(x)
                                      \le2L|X|,             \tag{4.5}
\]

which gives (4.3).  Finally, assigning weight (1/(2L)) to each
edge--endpoint-slot incidence gives load one at every port edge and load
(deg_G(x)/(2L)\le1) at every slot over (x).  Integrality and convex
decomposition give the stated symmetric distribution. \(\square\)

This is the exact pseudoarboricity form of the sharp colour gate.  Since a
factor has about (M/d) macros, the average port degree is about (2L).
Thus (4.4) is a near-regularity assertion, not a consequence of a
constant-factor maximum-degree estimate.

## 5. How much physical flexibility remains after a mark is fixed

The full product fibre gives a stronger local spread estimate than the
diagonal paired-event fibre.

Fix a desired mark (z\in B).  There are

\[
                              m!(m-1)!                     \tag{5.1}
\]

paths in the endpoint fibre with (b_2=z).  Let (V) be an internal
lower vertex.  If (V) occurs in role (q), put

\[
 D(V)=S\setminus V\subseteq A,\qquad
 I(V)=V\setminus S\subseteq B,\qquad |D(V)|=|I(V)|=q.     \tag{5.2}
\]

### Theorem 5.1 (fixed-mark internal-vertex aperture)

For (1\le q\le m-1), the proportion of the paths in (5.1) which contain
(V) is

\[
 p_z(V)=
 \begin{cases}
 \displaystyle {1\over m(m-1)},
    &q=1,\ z\notin I(V),\\[2mm]
 \displaystyle {1\over {m\choose q}{m-1\choose q-1}},
    &2\le q\le m-1,\ z\in I(V),\\[2mm]
 0,&\text{otherwise}.
 \end{cases}                                               \tag{5.3}
\]

In particular,

\[
                              p_z(V)\le {1\over m(m-1)}.   \tag{5.4}
\]

If the first insertion (w\ne z) is fixed as well, then among the
(m!(m-2)!) compatible paths a fixed internal lower vertex has proportion
at most (1/m).

#### Proof

A deletion order contains the prescribed (q)-set (D(V)) as its first
(q) entries with probability (1/{m\choose q}).

For (q=1), the first inserted label must be the unique member of (I(V))
and cannot equal the mark fixed in position 2.  Its insertion probability
is (1/(m-1)).  For (q\ge2), the prefix (I(V)) must contain (z); with
(z) fixed in position 2, its probability is
(1/{m-1\choose q-1}).  This proves (5.3).  The largest nonzero value is
attained at (q=1) or (q=m-1), giving (5.4).

If the ordered first pair is ((w,z)), the insertion prefix is forced at
rank 1, and at rank (q\ge2) its remaining (q-2) labels have probability
(1/{m-2\choose q-2}).  Multiplication by
(1/{m\choose q}) gives a maximum of (1/m). \(\square\)

Thus averaging over the first companion gives a genuine extra factor
(m\asymp d) of lower-portal spread.  Fixing an unmarked level-two owner
pins the unordered first pair and loses that factor.  This is the local
form of the fixed-fibre two-mark rigidity theorem: the broad (m)-element
mark list is available before the level-two owner is fixed; afterwards the
unmarked owner has only the two orientations in (2.6).

For reference, if fixed marks (z_P) are assigned and path orders are then
chosen independently and uniformly, a sufficient lower-only collision
criterion is

\[
 \sum_P\sum_{v\in F}p_{P,z_P}(v)
 +\sum_{P<Q}\sum_v p_{P,z_P}(v)p_{Q,z_Q}(v)<1,             \tag{5.5}
\]

where (F) is a fixed forbidden lower bank.  Indeed the left side bounds
the expected number of forbidden hits and pair collisions.  No estimate in
the current macro factor proves (5.5); it is recorded only as an exact
quantitative target.  Here (p_(P,z_P)(v)) is extended to equal one at either
fixed endpoint of the fibre and zero at an incompatible vertex; in an
application the other selected endpoints should normally be included in
(F).

## 6. The compound square-router is the physical gate

Fix a selected owner-disjoint macro family and one orientation of every
port edge.  For a macro (P), let (Z_P^0) be the typed bundle consisting
of

* its current rank-(t) lower vertex (S_1); and
* its (h\in\{2,3\}) current level-one owner occurrences.

Let (Z_P^1) be the corresponding bundle after the (q=1) insertion
switch.  Every resource outside these bundles is unchanged by Theorem 1.1
and Theorem 2.1.  Let (F) be the invariant occupied resource bank.

### Theorem 6.1 (exact simultaneous-toggle criterion)

A set (mathcal X) of macros can have all its port edges reversed
simultaneously if and only if

\[
 \begin{aligned}
 &Z_P^1\cap F=\varnothing &&(P\in\mathcal X),\\
 &Z_P^1\cap Z_Q^0=\varnothing &&(P\in\mathcal X,
                                  Q\notin\mathcal X),\\
 &Z_P^1\cap Z_R^1=\varnothing &&(P,R\in\mathcal X, P\ne R).
 \end{aligned}                                             \tag{6.1}
\]

Every such move is reversible.  It preserves every unmarked level-two
owner and changes the mark load by

\[
            \sum_{P\in\mathcal X}
                 (\mathbf e_{b_1(P)}-\mathbf e_{b_2(P)}).  \tag{6.2}
\]

#### Proof

After the switches, the occupied exclusive bank is exactly

\[
       \bigcup_{P\notin\mathcal X}Z_P^0
       \ \cup\!
       \bigcup_{P\in\mathcal X}Z_P^1.                     \tag{6.3}
\]

The old bundles are pairwise disjoint and avoid (F).  Therefore (6.3)
is a legal resource set exactly under the three displayed conditions.
The same adjacent transposition reverses the switch, proving
reversibility.  The level-two and mark assertions are Theorem 2.1.
\(\square\)

There is a useful lower-only special case.  Regard the current corner
(S_1(P)) as the tail of an arc and the alternate corner as its head.  If
heads never hit the invariant bank and have multiplicity at most one, a
feasible toggle family is exactly a disjoint union of

* directed cycles on occupied corners; and
* directed paths whose final head is a free lower vertex.

Along a path, the free lower vertex moves to the initial tail; along a
cycle, occupancy rotates.  This is the literal alternating-hole router
suggested by the permutohedron.  For compound (h=2,3) portals, one
alternative bundle may hit several old bundles and two alternative bundles
may intersect.  Then (6.1), rather than ordinary directed paths, is the
correct condition.

### Theorem 6.2 (aligned compound routes transport one mark exactly)

Assume a portal bank is **atomic**: any two compound bundles occurring as
current or alternative states are either equal or disjoint, and every such
bundle avoids the invariant bank (F).  Regard the two states of a macro
(P) as the directed arc

\[
                  (Z_P^0,b_2(P))\longrightarrow
                  (Z_P^1,b_1(P)).                         \tag{6.4}
\]

An aligned route is a sequence (P_1,...,P_l) such that

\[
 Z_{P_i}^1=Z_{P_{i+1}}^0,
 \qquad b_1(P_i)=b_2(P_{i+1})qquad(1\le i<\ell),         \tag{6.5}
\]

and the final bundle (Z_(P_l)^1) is currently free.  Toggling every macro
on the route is legal and changes the colour-load vector by exactly

\[
                  -\mathbf e_{b_2(P_1)}
                  +\mathbf e_{b_1(P_\ell)}.               \tag{6.6}
\]

The route reverses after use, and the free compound bundle moves from
(Z_(P_l)^1) to (Z_(P_1)^0).

More generally, build the ordinary directed portal graph whose arcs are
(6.4), retaining an arc concatenation only when both equalities in (6.5)
hold.  Give every compound-bundle state unit vertex capacity.  For every
colour (s), add a source node (sigma_s), join the super-source to it with
capacity

\[
                              o_s=(n_s-L)_+,               \tag{6.7}
\]

and join (sigma_s) to the tail state of every macro with old colour (s).
For every colour (t), add a sink node (gamma_t), join every free terminal
state of colour (t) to (gamma_t), and give the edge from (gamma_t) to the
super-sink capacity

\[
                              g_t=(L-n_t)_+.               \tag{6.8}
\]

If this network has flow value (sum_s o_s), then an integral flow gives
pairwise resource-disjoint aligned routes whose simultaneous toggle makes
every colour load at most (L).

#### Proof

At an internal route state, the alternative bundle claimed by (P_i) is
exactly the current bundle vacated by (P_(i+1)).  Atomicity and
vertex-disjointness give all three conditions in (6.1).  The colour change
on one arc is

\[
                              -\mathbf e_{b_2(P_i)}
                              +\mathbf e_{b_1(P_i)}.        \tag{6.9}
\]

The second equality in (6.5) makes all internal terms telescope, proving
(6.6).  Applying the same involutions in reverse order restores the old
state; the only unfilled old bundle is the first one, proving the free-hole
statement.

Unit-capacity directed max flow is integral.  Its path decomposition gives
vertex-disjoint aligned routes.  A route beginning at colour (s) removes
one of its (o_s) excess units, and a route ending at colour (t) consumes one
of its (g_t) free slots.  Equations (6.7)--(6.8) therefore imply the final
cap. \(\square\)

This theorem is a genuine regenerative mechanism: a used route remains
present with the reverse orientation and carries the free compound bundle
back to its initial state.  Its missing premise is structural.  The current
macro orbit does not yet provide an atomic portal bank or the all-cut rank
needed for the flow value in (6.7).

### Proposition 6.3 (capacity feasibility does not imply physical routing)

There are two disjoint fresh three-vertex paths with distinct requested
new marks whose two required (q=1) switches collide in the same lower
vertex.

#### Proof

On the ground set ([7]), take

\[
 \begin{array}{c|c|c}
 &\text{deletion order}&\text{insertion order}\\ \hline
 P:&(4,2)&(5,3),\\
 Q:&(6,1)&(7,3),
 \end{array}                                               \tag{6.10}
\]

with initial states (124) and (126), respectively.  Their current
paths are

\[
                         P:124,125,135,
 \qquad                  Q:126,127,237.                    \tag{6.11}
\]

The six displayed vertices are distinct.  Reversing the first two
insertions changes the two marks from the common overloaded coordinate
(3) to (5) and (7), which are distinct, but
changes both first internal vertices to

\[
                              123.                          \tag{6.12}
\]

Hence both abstract mark choices obey capacity one while the simultaneous
physical rethread is impossible.  The two port edges are ({3,5}) and
({3,7}); their multigraph has maximum degree two and therefore satisfies
Theorem 4.1 with (L=1). \(\square\)

The example already fails on the lower shore; adding owner portals cannot
repair it.  It proves that Theorem 3.1 or Theorem 4.1 cannot be substituted
for the macro-capacity rounding theorem.

## 7. What this changes in the factor-(d) problem

The event-order idea gives two exact reductions.

1. **Before owner selection:** if a near-factor can be chosen with
   insertion-event loads (R_s\le mL), then Theorem 3.1 assigns the sharp
   marks.  The mark assignment itself is no longer a growing-rank
   hypergraph problem.
2. **After unmarked level-two owner selection:** it is enough that the
   first-pair port multigraph satisfy (4.3), followed by one feasible
   compound square routing from the initial orientation to a cap-feasible
   orientation.

The first route still needs event-bank rounding at relative error
(O(1/d)).  The second route still needs near-average port pseudoarboricity
and the literal lower/level-one router.  Neither follows from the current
(O(M/k)) bound on the already chosen (b_2) loads.

A proof-safe sufficient theorem replacing the open capacity part of the
August 6 macro gate is therefore:

> **Regenerative compound square-router theorem.**  The joint fractional
> (2/3) macro factor can be rounded to an owner-disjoint near-factor with
> (O(M/d)) lower leave so that its unmarked level-two port graph satisfies
> (4.3), a cap-feasible orientation is reachable through compound toggles
> satisfying (6.1), and after every stopped separator exposure the same
> statement holds in the residual instance with the required marked
> cylinder through order (O(d)).

This theorem would close the colour part without proving

\[
                         \chi'(\mathcal A)
                         =(1+O(1/d))\Delta(\mathcal A)     \tag{7.1}
\]

for the whole growing-rank augmented hypergraph.  It is genuinely weaker
in colour algebra, but it is not presently proved: the complete bundles in
(6.1), their hereditary routing, and the higher marked cylinder remain the
integral content.

## 8. Proof-status summary

The following statements are unconditional in this note:

* the full product-permutohedron calculus;
* the exact effect of each adjacent switch on the lower row and marked
  level-two owner;
* the sharp capacitated event-list Hall selector and its one-point-uniform
  convex decomposition;
* the exact two-port pseudoarboricity criterion;
* the (O(d^{-2})) fixed-mark lower-vertex aperture before the first
  companion is fixed;
* the exact simultaneous compound-toggle criterion; and
* the explicit collision obstruction.

The note does **not** prove an integral macro near-factor, a hereditary
marked cylinder, or (B(k)+O(1)).  Its main conclusion is that the missing
factor (d) is not intrinsic to choosing one mark from a (d)-element
event bank.  It is concentrated in producing and regenerating a physical
compound square router while the owner and marked-cylinder resources are
kept integral.
