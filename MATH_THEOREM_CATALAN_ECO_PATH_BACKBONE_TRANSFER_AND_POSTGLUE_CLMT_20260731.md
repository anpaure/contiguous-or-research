# ECO path backbones have an exact monomer--dimer transfer state

Date: 2026-07-31  
Status: exact decoration-free path-backbone selection theorem; exact
state-expanded repair-first specialization; exact post-glue CLMT implication;
no all-`n` path-backbone or Decorated Middle Levels theorem

## 0. Verdict and the changed quantifier order

The path-backbone lane separates cleanly into two versions.

For the central Catalan Linear Matching Theorem, the exact minimal trace
order is now

\[
 \boxed{
 \text{any spanning middle-levels 2-factor}
 \longrightarrow \text{endpoint componentwise forest decoration}.} \tag{0.1}
\]

An arbitrary degree-preserving alternating-circuit packet may change the
starting factor; connectivity is irrelevant.  At the terminal factor the two
turn palettes must be globally bijective and the selected shores alternate
on every marked component.  Each marked component must contain an unmarked
occurrence and lie off the binary cycle face; unmarked components use either
cross phase.  A wholly marked component is forbidden because it lifts to two
rail cycles.

The collision-free strict ECO path tiling studied below is therefore an
optional stronger Hamiltonization certificate, not a central prerequisite.
Forced-port owner alignment, the gap--colour matching and the occurrence
router are absent from the minimal factor-level stage.

For a fixed component order and a fixed collision-independent strict bank,
the first arrow is exactly a monomer--dimer tiling of a line.  It has:

* an exact two-step Boolean recurrence;
* an exact unit-flow formulation and therefore an integral relaxation; and
* an exact recursive child state consisting of a two-terminal `2 by 2`
  Boolean transfer table.

If one instead insists on repair before gluing and transports one decoration
through every ECO prefix, the same theorem remains valid after deleting all
tiles which fail the literal owner or local-channel predicates.  The exact
local channel field is the ownership-indexed exported state

\[
 Q\longmapsto
 (N_{t,Q},S_t,T_{t,Q},B_{t,Q},V_t(Q),\text{unit/kill semantics}), \tag{0.2}
\]

not a scalar route rank.  Under a fixed common matching seam and pairwise
disjoint route banks these are unary tile filters, so path integrality
survives.  Without those factorization hypotheses, the child must export the
full occurrence-labelled matching transfer and pairing-resolved linkage
relation.

The path result is sufficient, not without loss of generality.  The first
branching component tree `K_(1,3)` already has a determinant-two ternary-tile
minor and a unique half-integral cover with no integral cover.

## 1. Decoration-free strict path banks

Let `F` be a spanning two-factor and let its component set be

\[
             \mathcal V=\{v_0,v_1,\ldots,v_N\}.                  \tag{1.1}
\]

The case `N=0` is the empty tiling and is accepted trivially.  Assume
`N>=1` below.

Fix the ordinary component path

\[
              A=v_0v_1\cdots v_N,
 \qquad e_i=v_{i-1}v_i\quad(1\le i\le N).             \tag{1.2}
\]

An ECO atom `t` is a **monomer offer at `i`** when its distinct old
component support is

\[
                         H_t=\{v_{i-1},v_i\}.                    \tag{1.3}
\]

It is a **dimer offer at `i`** when

\[
                    H_t=\{v_{i-1},v_i,v_{i+1}\}.                \tag{1.4}
\]

Thus the component-tree tile of a monomer is `Q_t={e_i}`, while the tile of
a dimer is `Q_t={e_i,e_(i+1)}`.

A bank `B` is called **strict and collision-independent for `A`** when:

1. every atom in `B` has one of the supports (1.3)--(1.4);
2. its literal alternating circuits have pairwise disjoint physical vertex
   supports; and
3. every edge-disjoint tile subfamily is a prefix-faithful strict physical
   cube: its component partition is exactly the partition of `A` obtained
   by contracting the selected tiles.

Item 3 includes the clean phase of a two-touch ECO atom.  It must not be
inferred merely from the set `H_t`.  A preselected parity side of every
fixed-rotation ECO collision path supplies Item 2, while Item 3 is the
separate physical strictness test.

No decoration is part of this definition.

## 2. Five exact forms of path selection

For an atom `t`, let

\[
 I_t=\{i:e_i\in Q_t\}.                              \tag{2.1}
\]

Thus `I_t` is an interval of length one or two.  Make a directed acyclic
multigraph `D(A,B)` on nodes `0,1,...,N` by adding

\[
 \begin{array}{ll}
 i-1\longrightarrow i&\text{for every monomer offer at }i,\\
 i-1\longrightarrow i+1&\text{for every dimer offer at }i.
 \end{array}                                         \tag{2.2}
\]

Write `m_i=1` when at least one monomer offer exists at `i`, and write
`d_i=1` when at least one dimer offer exists at `i`.

### Theorem 2.1 (exact path-backbone selector)

The following are equivalent.

1. There is a family `S subseteq B` whose tiles partition `E(A)`.
2. The component--atom incidence graph on `V(A) sqcup S` is a tree.
3. `D(A,B)` has a directed path from `0` to `N`.
4. The exact-cover system

   \[
       \sum_{t:i\in I_t}x_t=1\quad(1\le i\le N),
       \qquad x_t\ge0                                      \tag{2.3}
   \]

   is feasible.
5. The Boolean recurrence

   \[
   h_0=1,\qquad h_1=m_1,
   \qquad
   h_j=(h_{j-1}\wedge m_j)\vee
       (h_{j-2}\wedge d_{j-1})\quad(2\le j\le N)          \tag{2.4}
   \]

   ends with `h_N=1`.

Moreover every vertex of (2.3) is integral.  Hence feasibility of the
relaxation is already an exact integral selection test.

#### Proof

A tile partition is precisely an `A`-tiling.  The ordinary-tree tiling
equivalence identifies this with the incidence-tree condition, proving
`1 iff 2`.

Map an interval tile `[a,b]` to the arc `a-1 -> b`.  Successive arcs of a
directed `0`-to-`N` path partition the positions `1,...,N`, and every tile
partition gives such a path.  This proves `1 iff 3`.

For `x>=0`, put

\[
                 c_i(x)=\sum_{t:i\in I_t}x_t.                   \tag{2.5}
\]

At every internal node `i`,

\[
 c_{i+1}(x)-c_i(x)
   =\sum_{t:\min I_t=i+1}x_t-
     \sum_{t:\max I_t=i}x_t,                                  \tag{2.6}
\]

which is flow conservation.  The two endpoint equations say that the
source outflow and sink inflow are one.  Conversely, every unit flow has
load one across every prefix cut, so it satisfies (2.3).  Thus (2.3) is the
unit `0`-to-`N` flow polytope of (2.2).  The node--arc incidence matrix is
totally unimodular, so the polytope is integral.  This proves `3 iff 4` and
the final assertion.

Finally, a tiling of positions `1,...,j` ends either in a monomer at `j` or
in a dimer on `j-1,j`.  Removing that last tile gives exactly (2.4), and
adjoining either possible last tile proves the converse.  Hence `1 iff 5`.
\(\square\)

### Corollary 2.2 (decoration-free Hamiltonization)

If `B` is a strict collision-independent path bank and the equivalent
conditions of Theorem 2.1 hold, toggling the selected atoms gives one
Hamilton cycle.

#### Proof

The selected incidence graph is a tree.  Pairwise physical disjointness
makes the symmetric differences commute, and the strict component-faithful
cube identifies every prefix partition with its incidence subforest.  The
full incidence tree has one component. \(\square\)

### Exact fixed-order obstruction

Let `R` be the nodes reachable from `0` in `D(A,B)`.  If `N` is not
reachable, then

\[
                         \delta^+_{D(A,B)}(R)=\varnothing.        \tag{2.7}
\]

Conversely such a directed cut forbids a tiling.  Thus (2.7), equivalently
the terminal condition `h_N=0` in (2.4), is the exact obstruction for a
fixed component order and a fixed bank.  An intermediate failed recurrence
value need not be terminal: a later dimer may make the recurrence true
again.  The cut is not a no-go for another component order, collision phase
or branching incidence tree.

## 3. The exact recursive interval state

The acceptance bit of a child interval is not compositional, because a
dimer selected at the parent can cover one edge at each side of a child
boundary.  The exact stateless child export has four bits.

For an edge interval `J=[a,b]`, let

\[
                    \Theta_J(\lambda,\rho)\in\{0,1\},
               \qquad \lambda,\rho\in\{0,1\},                  \tag{3.1}
\]

mean that all edges of `J` can be tiled internally except that its first
edge is reserved for a left-crossing dimer exactly when `lambda=1`, and its
last edge is reserved for a right-crossing dimer exactly when `rho=1`.
The two reservations may not reserve the same edge twice.

For the singleton interval `{i}` the transfer matrix is

\[
             \Theta_{\{i\}}=
             \begin{pmatrix}m_i&1\\[2pt]1&0\end{pmatrix}.       \tag{3.2}
\]

If `J_1=[a,c]` and `J_2=[c+1,b]`, put

\[
                  K_c=\begin{pmatrix}1&0\\0&d_c\end{pmatrix}.  \tag{3.3}
\]

All products below are over the Boolean semiring.

### Theorem 3.1 (exact interval composition)

\[
                  \boxed{\Theta_{[a,b]}
                    =\Theta_{[a,c]}K_c\Theta_{[c+1,b]}.}        \tag{3.4}
\]

Consequently a full path tiling exists if and only if

\[
                         \Theta_{[1,N]}(0,0)=1.                 \tag{3.5}
\]

The product is associative, so the `2 by 2` table is an exact child state
for any binary interval recursion.

#### Proof

Cut a tiling between positions `c` and `c+1`.  Either no tile crosses the
cut, giving boundary mode zero on both children, or the unique crossing tile
is a dimer on those two positions, giving mode one on both children and
requiring `d_c=1`.  These are exactly the two diagonal entries of `K_c`.
Restricting a global tiling proves necessity.  Conversely, compatible child
tilings and the indicated crossing dimer have disjoint covered positions
and cover the union exactly once.  This proves (3.4).  Global boundary
positions cannot be covered from outside, giving (3.5). \(\square\)

The full table really is needed.  On two positions, the systems

\[
 (m_1,m_2,d_1)=(1,0,1),\qquad (0,1,1)                         \tag{3.6}
\]

both accept with closed boundaries, but their transfer matrices are,
respectively,

\[
        \begin{pmatrix}1&1\\0&1\end{pmatrix},
        \qquad
        \begin{pmatrix}1&0\\1&1\end{pmatrix}.                 \tag{3.7}
\]

A continuation attached on the distinguished side separates them.  Thus a
single child-good bit loses exact compositional information.

## 4. Collision phases and the exact remaining path formula

In one fixed ECO rotation, every nontrivial physical collision component is
a path with two alternating parity classes.  Fix one Boolean variable
`sigma_p` for each such path `p`.  Retain its parity `sigma_p`; isolated
atoms are always retained.  This gives a pairwise physically disjoint bank.
Throughout this section, strict phase and component faithfulness are assumed
certified for every edge-disjoint subfamily of the retained bank, or are
carried explicitly in the state-expanded transitions of Section 6.  The
collision phase by itself does not certify that physical row.

For an atom `t`, let

\[
 r_t(\sigma)=
 \begin{cases}
  1,&t\text{ is isolated},\\
  [\sigma_{p(t)}=\epsilon(t)],&t\text{ has parity }\epsilon(t)
      \text{ on collision path }p(t).
 \end{cases}                                                     \tag{4.1}
\]

After any desired unary filter `g(t)`, define the tile-offer formulae

\[
 \begin{aligned}
 M_i(\sigma)&=\bigvee_{t\text{ monomer at }i}
                     (g(t)\wedge r_t(\sigma)),\\
 D_i(\sigma)&=\bigvee_{t\text{ dimer at }i}
                     (g(t)\wedge r_t(\sigma)).                  \tag{4.2}
 \end{aligned}
\]

Replace `m_i,d_i` in (2.4) by the Boolean formulae (4.2), without
simplifying after each step, and call the final formula `Phi_A(sigma)`.

### Theorem 4.1 (exact parity-bank criterion)

There is a collision-parity choice whose retained unary-good atoms contain
a strict monomer--dimer tiling of `A` if and only if

\[
                              \Phi_A(\sigma)                     \tag{4.3}
\]

is satisfiable.

#### Proof

For a fixed assignment `sigma`, (4.2) is exactly the availability bit of
each interval tile.  Theorem 2.1 says that the resulting bank tiles `A` if
and only if the evaluation of (2.4) is true.  Existentially quantifying the
phase assignment proves (4.3). \(\square\)

For a fixed phase, the selection polytope remains a unit-flow polytope.  The
joint phase-and-flow linearization is not asserted to be totally unimodular:
the same phase variable can constrain offers at distant component-path
positions.

This observation identifies a useful exact frontier-width parameter.  At a component cut,
call a phase variable **active** when it has a surviving tile offer on each
side of the cut.  If at most `w` phase variables are active at every cut,
then (4.3) has an exact left-to-right dynamic program with at most

\[
                             2^{w+1}                              \tag{4.4}
\]

occupancy/phase states per cut: one monomer--dimer boundary bit and the
assignment of every active phase.  Variables are introduced at their first
offer and forgotten after their last offer.  In the worst case an active
phase cannot be forgotten when its two parities enable distinguishable
future offers; this does not assert that `w` is the minimum state width of
every particular instance.  Local collision degree at most two does not
bound `w`, because collision-path order and component-path order are
different.

Thus an all-`n` path proof may proceed in either of two exact ways:

1. choose a collision phase first and prove (2.4); or
2. construct component orders with bounded active-phase width and propagate
   the state (4.4).

## 5. Owner alignment and rank-balanced channels as unary filters

This section records the stronger repair-first specialization.  Fix one
prepared endpoint, one upper transversal `I`, and one occurrence-labelled
gap-forest matching `M`, all preserved on the declared strict cube.

For an atom `t`, let `P_A(t)` be its three selected upper-port occurrences
and let `F_t` be its three literal forced gap--lower-colour occurrence
edges.  On the leaf-peelable face define

\[
       \operatorname {Own}(t)
       =[P_A(t)\subseteq I]\wedge[F_t\subseteq M].               \tag{5.1}
\]

The second conjunct is literal pointwise owner alignment.  Off the forest
face it must be replaced by the vertex-disjoint alternating-cycle packing
criterion; colour-set equality is not a substitute.

Let `E_sh(t)` be the at-most-two genealogy-shared old edges, and put

\[
                            w_t=|H_t|-1\in\{1,2\}.                \tag{5.2}
\]

For every ownership state `Q subseteq E_sh(t)`, export the tuple (0.2).
After vertex splitting define

\[
 \operatorname {Link}(t,Q)=
 \left[
 \operatorname {maxflow}
 (N_{t,Q}-B_{t,Q}-V_t(Q);S_t,T_{t,Q})=w_t
 \right].                                                       \tag{5.3}
\]

The sources are distinct, the sinks have unit capacity, and the semantic
map identifies the `w_t` channels with the `w_t` component-path edges of
the tile.  For prescribed source--sink pairs, (5.3) is replaced by the full
pairing-resolved linkage relation.

For fixed execution, (5.3) plus its semantic map is the exact local linkage
row.  For adversarial router deletion, a ternary all-or-none atom needs one
additional field: either its two unit edges survive independently, or its
grouped atomic kill table satisfies

\[
 \min\{|Y|:Y\text{ disables the atom in state }Q\}\ge w_t.       \tag{5.4}
\]

Two required paths whose loss of either disables the whole ternary atom do
not imply (5.4).

For a prescribed family \(\mathcal Q=(\mathcal Q_t)_t\) of ownership-state
requirements, define

\[
 \operatorname {Good}_{\mathcal Q}(t)=\operatorname {Own}(t)\wedge
       \bigwedge_{Q\in\mathcal Q_t}
       \bigl(\operatorname {Link}(t,Q)\wedge
             \operatorname {Sem}(t,Q)\bigr),                    \tag{5.5}
\]

including (5.4) when deletion resilience is required.  For one frozen
ownership orientation take \(\mathcal Q_t=\{Q_t^\star\}\).  For the robust
export which must survive either assignment at every shared edge, take
\(\mathcal Q_t=2^{E_{\rm sh}(t)}\), of size at most four.

### Theorem 5.1 (exact filtered path-collar selector)

Assume:

1. the fixed matching seam and physical cube are preserved by every tile;
2. every tile has the literal directed realization asserted by its exported
   local channel state;
3. across selected tiles, the route banks are pairwise disjoint, or one
   declared laminar/global certificate proves both simultaneous directed
   realization and the additive damage bound with the exported unit/grouped
   semantics; and
4. all interactions between tiles are exhausted by those fixed interfaces.

Then a repair-first owner-aligned, rank-balanced private ECO path collar
with ownership-state requirement \(\mathcal Q\) exists if and only if
Theorem 2.1 accepts after setting `g(t)=Good_Q(t)`.

#### Proof

Under Items 1--4, owner and channel feasibility are unary properties of a
tile.  Delete every failing tile.  Any tiling of the residual bank is an
incidence tree, every forced edge belongs to the same unique matching, and
the disjoint or global certificate simultaneously realizes the routes and
adds damage one per monomer and two per dimer with the correct unit/grouped
semantics.  The private-collar composition theorems therefore execute it.

Conversely, any collar in the declared factorized bank consists only of
tiles satisfying (5.5), and its component supports partition `E(A)`.
Theorem 2.1 therefore accepts. \(\square\)

The converse is deliberately relative to the declared bank.  A construction
using off-forest matching exchange, nonlocal shared routing, a different
component order or a branching hypertree can exist when this filtered path
system fails.

## 6. The full exported child state

When the hypotheses of Theorem 5.1 are not frozen globally, a four-bit
monomer--dimer table alone is insufficient.  At every path separator use a
finite interface set `Sigma_i` and export the relation

\[
 \widehat\Theta_J\subseteq
   (\{0,1\}\times\Sigma_{a-1})
   \times(\{0,1\}\times\Sigma_b).                  \tag{6.1}
\]

The seam kernel records either no crossing dimer or one named crossing
dimer together with compatible interface states.  Relational composition
is the state-expanded form of (3.4).  Equivalently, make a layered directed
graph whose nodes are `(position,state)` and whose arcs are complete tile
realizations.  Feasible global collars are exactly source--sink paths in
this graph, so its realization-variable unit-flow polytope is again
integral.

For the repair-first ECO application, a proof-sufficient `Sigma_i` contains:

1. **physical frontier:** the occurrence identities, old/new matching phase,
   component root and strict-cube boundary effect;
2. **matching seam:** the fixed upper-transversal key and the full
   occurrence-labelled boundary gap--colour matching transfer, including
   exact mates and root coverage;
3. **ownership state:** the unresolved shared-edge bits `Q` and their
   literal deleted-port map;
4. **linkage state:** named sources, remaining unit sink bank, child
   exclusions and the full pairing-resolved directed boundary-linkage
   relation; and
5. **rank semantics:** the map to component-path units and, for an
   indivisible atom, its grouped kill relation.

These fields cannot in general be replaced by counts.

* The two-gap owner-drift exchange has the same matching cardinality at both
  endpoints but changes the mate of a later forced port.
* At paper `n=3`, the same binary atom and terminals have rank one before
  ownership in both the private and public routers, but only the private
  router survives the assigned-away shared edge.
* At paper `n=5`, two sources are individually routable in both the private
  and bottleneck routers, while their joint linkage ranks are two and one.
* Two abstract paths do not certify two independently surviving component
  units for an all-or-none ternary toggle.
* The two possible doubled-side phases of a two-touch ECO atom can merge or
  split with identical component support.

Thus (6.1), with these literal fields or an equivalent continuation
signature, is the exact child export.  In the decoration-free post-glue
Stage A, Items 2--5 disappear.  If a common strict collision-independent
bank has already been fixed, Item 1 also collapses and (6.1) reduces to the
`2 by 2` table of Section 3.

## 7. Post-glue CLMT implication

### Theorem 7.1 (path topology followed by endpoint repair)

Assume the following in one dimension.

1. A component order and a strict collision-independent ECO bank satisfy
   any of the equivalent conditions of Theorem 2.1.  Let `S` be the
   selected tiling and let

   \[
                     H=F\mathbin\triangle
                       \bigtriangleup_{t\in S}C_t.               \tag{7.1}
   \]

2. Starting from `H`, an ordered packet of alternating even circuits gives

   \[
       H_0=H,\qquad H_j=H_{j-1}\mathbin\triangle P_j,            \tag{7.2}
   \]

   where every `H_j` is a spanning two-factor and the final `H_s` is a
   Hamilton cycle.
3. The final cycle `H_s` has a **CLMT-accepting forest decoration**: it has
   one joint alternating SDR (equivalently, for some upper occurrence
   transversal its cyclic gap--lower-colour graph has a perfect matching),
   and its induced binary mark trace lies off the unique cycle face.  In the
   exact trace normal form, either some positive unmarked run has length at
   least four or some maximal marked run has even length.

Then the Catalan Linear Matching Theorem holds in this dimension.

#### Proof

Corollary 2.2 makes `H` a literal Hamilton middle-levels cycle.  The packet
(7.2) gives the final Hamilton cycle `H_s`.  The joint SDR gives the
Boolean-diamond matching, and the exact binary-trace criterion says that
the added forest-side condition makes its physical Johnson lift acyclic.
The lift has the required two colour bijections and exactly `Cat_m` path
components.  This is the Catalan Linear Matching conclusion. \(\square\)

### Theorem 7.2 (factor-level endpoint is the minimal trace implication)

Let `F_0` be any spanning middle-levels 2-factor, with no path-backbone or
component-connectivity hypothesis.  Suppose an alternating-circuit packet
through spanning 2-factors ends at `F_s` with:

1. globally bijective upper and lower turn representatives;
2. componentwise alternating selected shores;
3. at least one unmarked occurrence on every marked component; and
4. every partially marked component off the ordinary binary cycle face.

Give every wholly unmarked component either residual cross-matching phase.
Then `F_s` induces a perfect diamond matching whose physical lift is a
spanning `Cat_m`-path forest.

#### Proof

Apply the decorated-2-factor theorem componentwise.  The global turn
bijections and residual matchings give a perfect diamond matching.  Partially
marked components are acyclic by Item 4, unmarked components contribute
disjoint cross edges, and Item 3 excludes the two rail cycles of a wholly
marked component.  The fixed global edge count then gives `Cat_m` paths.
\(\square\)

Any two spanning 2-factors are connected by alternating circuits, so a
packet from `F_0` exists exactly when some accepting terminal factor exists.
The monomer--dimer selector of Theorem 2.1 disappears entirely from this
minimal existential statement.

The packet in Theorem 7.1 Item 2 need not commute with the ECO atoms, avoid
their ports, or preserve a decoration at intermediate states.  It is applied
later in literal order.  The exact quantifiers of that stronger path route
are

\[
 \exists(A,B,S)\ \operatorname {Topo}(F;A,B,S)
 \quad\wedge\quad
 \exists(P,\mathscr D_s)\
 \operatorname {EndpointForestDecor}(H(S);P,\mathscr D_s).       \tag{7.3}
\]

There is no universal quantifier over all topological outputs: one selected
path tiling and one endpoint packet suffice.  The minimal factor route drops
the first conjunct entirely:

\[
 \exists(F_s,\mathscr D_s)\quad
 \operatorname{ComponentwiseFactorAccept}(F_s,\mathscr D_s).    \tag{7.4}
\]

## 8. Comparison with repair-first private collars

The repair-first theorem has a different and stronger quantifier pattern.
In schematic form it requires

\[
 \exists(P_0,\mathscr D_0,S)\quad
 \forall U\subseteq S:\quad
 \begin{cases}
   \text{the physical prefix }U\text{ has its incidence partition},\\
   \mathscr D_0\text{ transports with the same matching seam},\\
   \text{every pending forced port stays owner-aligned},\\
   \text{the routed backbone satisfies its damage bound}.
 \end{cases}                                                     \tag{8.1}
\]

By contrast, (7.3) asks for no decoration or route during optional ECO
Hamiltonization and decorates only the final packet endpoint; (7.4) does not
ask for Hamiltonization at all.

Therefore:

* terminal decorated-factor repair is the weakest trace architecture here;
* repair-first private collars remain useful when an ordered catalogue
  replaces a literal disjoint cube, or when residence, shadows, sockets,
  voltage and compiler state must survive every prefix;
* terminal factor success does not imply the prefix state (8.1); and
* repair-first success does not supply a uniform final repair packet for an
  unrelated factor output.

At project `m=5`, both orders are independently positive: the raw ECO
Hamilton endpoint is repaired by the synchronized three-`C10` packet, and
the transported repair endpoint also has owner-aligned fixed-rotation ECO
Hamilton merges.  This finite coexistence does not prove either all-`n`
supply statement.

## 9. The first branching obstruction

Let `A=K_(1,3)` have arm edges `e_1,e_2,e_3`, and admit only the three
ternary pair-of-arm tiles

\[
       Q_{12}=\{e_1,e_2\},\quad
       Q_{13}=\{e_1,e_3\},\quad
       Q_{23}=\{e_2,e_3\}.                           \tag{9.1}
\]

Their edge--tile matrix is

\[
       \begin{pmatrix}
       1&1&0\\
       1&0&1\\
       0&1&1
       \end{pmatrix},
       \qquad \det=-2.                               \tag{9.2}
\]

The exact-cover equations have the unique fractional solution

\[
                       x_{12}=x_{13}=x_{23}=\tfrac12,             \tag{9.3}
\]

and no integral solution.  One tile misses one arm; two tiles double-cover
one arm.  This is the smallest determinant obstruction because every tree
with fewer than three edges is a path and every zero-one matrix of order at
most two has determinant in `{-1,0,1}`.

The obstruction has two consequences.

1. Consecutive-ones/TU integrality is a genuine path theorem and cannot be
   quoted for a branching component tree.
2. Restricting Stage A to a path is not without loss of generality.  For
   example, three binary atoms on the arms of a star form a valid incidence
   tree, but their unique ordinary-tree expansion is the star, not a path.

State expansion can solve a supplied bounded-width branching instance, but
it does not make the native subtree exact-cover matrix totally unimodular.

## 10. Exact all-`n` target and proved/open boundary

For the canonical factor, the exact path-backbone Stage A target is

\[
 \boxed{
 \exists\text{ component order }A,
 \ \exists\text{ collision-independent strict ECO bank }B:
 \Theta^{A,B}_{[1,N]}(0,0)=1.}                                  \tag{10.1}
\]

On the collision-parity face, replace (10.1) by

\[
                  \exists A,\sigma:\ \Phi_A(\sigma)=1.          \tag{10.2}
\]

Equations (10.1)--(10.2) are necessary and sufficient for their declared
path architectures.  Coherent two-section connectivity does not imply
them, because it supplies neither a component Hamilton order nor a
compatible interval tiling.  A failed transfer for one `A,B` is only the
cut (2.7), not an obstruction to another order or to a branching
hypertree.

For the **ECO path construction route**, Theorem 7.1 asks for two displayed
certificates: prove (10.1), (10.2), or a nonpath pairwise-disjoint strict
incidence hypertree, and exhibit a terminal forest-decorated Hamilton
endpoint.  This is an optional stronger construction, not the minimal
central gate.  The symmetric difference of any two spanning two-factors
decomposes into closed alternating circuits.  Hence from any starting factor
a terminal circuit packet exists if and only if some CLMT-accepting
componentwise decorated factor exists at all.

Consequently the weakest exact missing statement in the
middle-levels trace route is the **Decorated Middle Levels 2-Factor
Theorem**:

> for every `m`, `ML(2m-1)` has a spanning 2-factor with globally bijective
> upper and lower turn representatives and componentwise alternating marks,
> such that every marked component contains an unmarked occurrence and is
> off the binary cycle face.

The canonical MMM factor already supplies a starting 2-factor.  Stage A is
therefore an ECO-specific sufficient Hamiltonization certificate, not an
additional necessary existential gate for central CLMT.

The repaired project-`m=5` singleton passes the stronger owner/channel base,
but it is not a recursive proof of Item 1.  The ownership-resolved max-flow
oracle is an exact input to the repair-first version, not evidence that raw
ECO genealogy constructs the required channels uniformly.

Downstream RSB still requires residence, deeper-shadow, socket/voltage and
compiler preservation.  The post-glue central implication deliberately
makes no claim about those coordinates.

## 11. Dependencies and audit

This note uses:

* `MATH_THEOREM_AD_ECO_OWNER_ROUTED_HYPERTREE_GATE_20260731.md`;
* `MATH_THEOREM_CATALAN_ECO_LOCAL_CHANNEL_EXPORTED_STATE_AND_FIRST_OBSTRUCTIONS_20260731.md`;
* `MATH_THEOREM_CATALAN_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION_20260731.md`;
* `MATH_THEOREM_CATALAN_POSTGLUE_REPAIR_DECOMPOSITION_20260731.md`;
* `MATH_THEOREM_AD_TERMINAL_ECO_HAMILTONIZATION_AND_POSTGLUE_DECORATION_REPAIR_20260731.md`;
* `MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`;
* `MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`;
* `MATH_THEOREM_CATALAN_LEAF_FOREST_FORCED_PORT_OWNER_ALIGNMENT_20260731.md`;
* `MATH_THEOREM_CATALAN_PRIVATE_TREE_AUTOMATIC_HALL_AND_ROUTER_20260731.md`; and
* `MATH_THEOREM_CATALAN_BOUNDARY_LINKAGE_GAMMOID_STATE_20260731.md`.

The companion lightweight audit exhausts all monomer/dimer availability
patterns through eight path edges, compares brute force, recurrence,
reachability and the transfer product, and checks the determinant-two star.
It does not audit the family-level strictness hypothesis, phase-width bound,
owner/channel composition, LP vertex set or post-glue CLMT implication; and
it does not search the canonical all-`n` ECO catalogue or construct a final
repair packet.
