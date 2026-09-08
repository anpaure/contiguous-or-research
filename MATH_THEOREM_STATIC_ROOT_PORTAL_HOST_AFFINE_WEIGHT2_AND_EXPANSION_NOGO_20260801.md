# Static root-portal hosts: an affine weight-two obstruction to linear degree and expansion

Date: 2026-08-01

Status: unconditional local algebra and sharp impossibility theorems for
static connector hosts whose incident labels are realized through the unique
central turn of each raw SCD chain.  Hereditary forest compatibility forces
connectivity at most three; even the weaker demand that every complete
spanning tree be physical forces a cut of size at most four.  The result
applies to palette-neutral `C6`, `C10`, and arbitrary even incidence
circuits.  It does not obstruct the jointly selected nonlexical
`(M0,Q0,J)` construction, because that construction is deliberately
non-Cartesian and chooses one correlated matching/tree rather than exposing
every tree in a fixed host.

## 0. Outcome

The proposed nonlexical replacement for the canonical pull graph asked for
three simultaneous properties:

1. linear or superconstant ordered-portal degree at each raw SCD tail;
2. edge-connectivity `omega(d)`; and
3. static tree compatibility: every selected connector forest may be
   toggled inside one fixed factor.

These properties are incompatible when the connector labels at one raw SCD
chain all act through its unique rank-`m` root turn.

At one physical turn a two-factor chooses two incidence edges.  If every
subset of a star of connector labels is legal, all resulting local pairs
form an affine binary space consisting entirely of weight-two vectors.  Such
an affine space contains at most four pairs.  Including the base pair, there
are at most three nontrivial portal states.

Consequently a root-faithful simple connector host has

\[
                         \deg_H(C)\le3,
       \qquad            \lambda(H)\le3.              \tag{0.1}
\]

This rules out both a linear portal menu and edge-connectivity `omega(d)` as
soon as `d` grows.

The `n(n-1)` abstract incidence-hex frames through one Johnson edge are
therefore **alternative columns**, not simultaneously available Cartesian
host edges.  They must be selected jointly with the factor and port matching,
exactly as in the prospective `(M0,Q0,J)` route.

## 1. The affine weight-two lemma

Let `Omega` be a finite set and identify its subsets with vectors in
`F_2^Omega`.  Write `wt(x)` for Hamming weight.

### Lemma 1.1 (constant-weight-two affine spaces)

Let `A=b+U` be an affine subspace of `F_2^Omega` such that

\[
                         \operatorname{wt}(a)=2
                         \qquad(a\in A).               \tag{1.1}
\]

Then

\[
                          |A|\le4,
       \qquad             \dim U\le2.                 \tag{1.2}
\]

The bound is sharp.

#### Proof

On an affine binary space, every coordinate is either constant or takes the
values zero and one equally often.  Let `c` be the number of coordinates
constantly equal to one, and let `t` be the number of nonconstant
coordinates.  Summing (1.1) over `A` gives

\[
                 2|A|=c|A|+{t\over2}|A|,
       \qquad    2c+t=4.                              \tag{1.3}
\]

There are three cases.

* `c=2,t=0`: `A` has one member.
* `c=1,t=2`: every member chooses exactly one of two varying coordinates,
  so `|A|<=2`.
* `c=0,t=4`: all members are two-subsets of four coordinates.  There are
  only six such vectors, while `|A|` is a power of two, so `|A|<=4`.

This proves (1.2).  Sharpness is witnessed by

\[
                 \{12,34,13,24\},                    \tag{1.4}
\]

whose symmetric difference with `12` is a two-dimensional linear space.
\(\square\)

### Lemma 1.2 (punctured subset-sum version)

Let `b,u_1,...,u_s in F_2^Omega`.  Suppose

\[
             \operatorname {wt}\left(
               b+\sum_{i\in I}u_i\right)=2
       \qquad(\varnothing\ne I\subseteq[s]),          \tag{1.5}
\]

and suppose the `u_i` are distinct and nonzero.  Then `s<=4`.

#### Proof

Fix `i_0`.  Every vector in

\[
       b+u_{i_0}+operatorname {span}
              \{u_i:i\ne i_0\}                      \tag{1.6}
\]

is indexed by a subset containing `i_0`, so (1.5) makes the whole affine
space weight two.  Lemma 1.1 bounds it by four.  It contains the `s`
distinct vectors

\[
       b+u_{i_0},
       \qquad b+u_{i_0}+u_i\quad(i\ne i_0),           \tag{1.7}
\]

so `s<=4`. \(\square\)

## 2. Static circuit hosts

Let `G` be a bipartite incidence graph and let `F` be a spanning two-factor.
For every vertex `v`, write

\[
                         B_v=F\cap\delta_G(v),
       \qquad            |B_v|=2.                    \tag{2.1}
\]

Let `H` be a simple labelled connector graph.  A label `e in E(H)` carries
an even incidence circuit `Z_e`; individually,

\[
                         F_e=F\mathbin\triangle Z_e   \tag{2.2}
\]

is again a two-factor.  This includes ordinary factor-alternating `C6` and
`C10` switches and palette-neutral composites.

Call the circuit family **Cartesian tree-compatible** when, for every
graphic forest `J subseteq E(H)`,

\[
             F_J=F\mathbin\triangle
                    \mathop\triangle_{e\in J}Z_e      \tag{2.3}
\]

is a two-factor and has the component contraction prescribed by `J`.

Suppose a raw SCD component `C` has a distinguished central occurrence
`v_C`.  For an incident connector label `e`, its local state is

\[
                         P_e(C)=F_e\cap\delta(v_C).    \tag{2.4}
\]

Call the host **root-faithful** at `C` when every incident connector has
`P_e(C) != B_C` and different neighbours of `C` give different local pairs
`P_e(C)`.  An ordered Johnson portal is root-faithful: its head is read from
the new incidence pair at the unique rank-`m` root, so a genuine portal is
nonbase and different heads give different pairs.

Call the circuit family **root-local** at `C` when a connector label not
incident with `C` in `H` has empty incidence with the distinguished physical
turn:

\[
             Z_e\cap\delta_G(v_C)=\varnothing
             \qquad(e\notin\delta_H(C)).             \tag{2.5a}
\]

Thus the local state at `v_C` depends exactly on the connector labels chosen
from the host star of `C`.  This is the literal static-root model; without
root locality, a remote label is importing an additional socket at `C` and
belongs to the multi-socket escape discussed below.

### Theorem 2.1 (root degree at most three)

If the circuit family is Cartesian tree-compatible and root-faithful at
`C`, then

\[
                              \deg_H(C)\le3.           \tag{2.5}
\]

#### Proof

Every subset of the star `delta_H(C)` is a graph forest.  Tree compatibility
therefore says that for every `S subseteq delta_H(C)`, the local state

\[
 B_C\mathbin\triangle
       \mathop\triangle_{e\in S}
       \bigl(B_C\mathbin\triangle P_e(C)\bigr)        \tag{2.6}
\]

has size two.  The collection of all states in (2.6) is the affine space

\[
 B_C+operatorname {span}_{\mathbb F_2}
       \{B_C\mathbin\triangle P_e(C):e\in\delta_H(C)\}.
                                                        \tag{2.7}
\]

Lemma 1.1 says that (2.7) contains at most four distinct pairs.  One is the
base pair `B_C`.  Root faithfulness makes the `deg_H(C)` singleton states
distinct nonbase pairs, proving (2.5). \(\square\)

### Corollary 2.2 (no static root expander)

If every vertex of a simple connector host is root-faithful, then

\[
                    \Delta(H)\le3,
       \qquad       \lambda(H)\le\delta(H)\le3.       \tag{2.8}
\]

Thus no such family has superconstant ordered-portal degree or
edge-connectivity `omega(d)`.

Palette neutrality was not used.  Allowing `C10`, longer alternating
circuits, or exact immediate-colour cancellation does not evade the local
degree-two obstruction.

### Corollary 2.3 (bounded multi-socket interface)

Suppose a host component exposes `s` distinguished physical factor turns,
and different neighbouring components require different nonbase **combined**
states on those turns.  Then

\[
                           \deg_H(C)\le4^s-1.          \tag{2.9}
\]

Indeed, Lemma 1.1 gives at most four states at each turn, so the combined
signature has at most `4^s` values.

In the middle two levels, contracting one raw SCD chain contracts its unique
central 0-lexical incidence edge and exposes its two physical endpoints.
Even if a connector is permitted to program both shores, `s=2` gives

\[
                           \deg_H(C)\le15,
       \qquad              \lambda(H)\le15.           \tag{2.10}
\]

Thus using both ends of every raw central SCD edge still cannot produce
edge-connectivity `omega(d)`.  To evade (2.9), a purported host must import
an unbounded auxiliary socket bank not belonging to the raw SCD component,
or abandon Cartesian subset compatibility.

### Theorem 2.4 (spanning-tree compatibility still has a four-edge cut)

The growing-connectivity obstruction does not require every forest subset
to be valid.  Suppose only that:

1. `H` is a connected simple host;
2. for **every spanning tree** `T` of `H`, the simultaneous circuit toggle
   gives a valid two-factor with the declared component merges; and
3. at a chosen host vertex `C`, incident labels are root-local and
   root-faithful as above.

Then

\[
                              \lambda(H)\le4.          \tag{2.11}
\]

If `H-C` is connected, then also `deg_H(C)<=4`.

#### Proof

Let `K` be one component of `H-C`, and let `E_K` be the host edges from `C`
to `K`.  For every nonempty subset `S subseteq E_K`, and after fixing one
edge from `C` into every other component of `H-C`, there is a spanning tree
whose complete set of edges at `C` inside `K` is exactly `S`.

To see this, take the distinct endpoints in `K` of the edges in `S` as
roots.  Every connected graph has a spanning forest with exactly one
specified root in each component: adjoin a new vertex adjacent to all roots,
extend that star forest to a spanning tree, and delete the new vertex.  Add
the edges in `S`.  Do the same independently in the other components of
`H-C`.

Freeze the toggles chosen in those other components.  At the root turn of
`C`, varying `S` gives local vectors

\[
                         b+\sum_{e\in S}u_e.           \tag{2.12}
\]

Every nonempty `S` occurs in a compatible spanning tree, so every vector in
(2.12) has weight two.  Root faithfulness makes the `u_e`, `e in E_K`,
distinct and nonzero.  Lemma 1.2 gives

\[
                              |E_K|\le4.               \tag{2.13}
\]

But `E_K` is an edge cut, proving (2.11).  If `H-C` is connected, this cut
is the entire star of `C`, proving the degree bound. \(\square\)

Thus even the weaker requirement “every global merge tree works” is
incompatible with edge-connectivity `omega(d)`.  A positive construction
must choose one specially correlated tree/matching; it cannot expose a
highly connected host all of whose spanning trees are physical.

## 3. Why duplicate local states do not give a root connector

One might try to attach many labels at `C` which have the same local state
but travel to different remote components.  This does not implement the
declared ordinary connector star through one root socket.

Suppose `e=CX` and `f=CY` have the same nonbase root toggle.  Since
`{e,f}` is a forest, both must be selectable.  Their identical local
toggles cancel in (2.6), returning the base state at the unique socket of
`C`.  If that socket is the only interface of the circuits with `C`, the
combined switch has no surviving attachment there and cannot contract the
three components according to the tree `X-C-Y`.

Hence a **single-socket** tree-compatible realization forces local-state
injectivity, rather than merely head injectivity.  Parallel labels between
the same component pair do not help either: they form a labelled two-cycle
and a spanning tree can use at most one.  Artificial parallel multiplicity
can inflate multigraph cut size, but supplies neither distinct portal heads
nor additional simultaneous connector capacity.

The only escape inside a static host is to give one SCD component an
unbounded bank of physically distinct auxiliary sockets.  The two native
ends of its central SCD edge are insufficient by Corollary 2.3.  Such an
imported bank is not the ordered-root portal model; its packet size, port
bookkeeping, and residence/upper interfaces must be charged explicitly.

## 4. Edge-disjoint `C6/C10` families are even smaller

The canonical proof obtains tree compatibility from pairwise edge-disjoint
alternating circuits.  The same observation applies to a nonlexical base.

At the distinguished turn `v_C`, every circuit which passes through the
root uses one of the two old factor edges in `B_C`.  Pairwise edge
disjointness therefore permits at most two such circuit labels.  Thus an
edge-disjoint root-local family satisfies the stronger bound

\[
                           \deg_H(C)\le2.              \tag{4.1}
\]

Decorated rails may also use `v_C` as an unchanged external endpoint; this
raises the safe endpoint-neighbour bound to the constant eight proved in
the canonical audit, but it remains independent of `m`.

So replacing lexical incidences by a nonlexical factor does not by itself
create a linear static portal menu.  The obstruction comes from one fixed
degree-two factor state, not from the parenthesis form of the canonical
source.

## 5. Reconciliation with the `n(n-1)` abstract frames

For a Johnson edge `p=I+e`, `q=I+b`, every choice

\[
       a\in I,
       \qquad c\notin p\cup q,
       \qquad H=(I-a)+e                              \tag{5.1}
\]

gives one common-delete incidence-hex frame, for exactly `n(n-1)` frames.
These frames choose different cores, active labels, external stubs, and
usually different surrounding factor incidences.

Theorem 2.1 says they cannot all be columns of one Cartesian static host at
the same root.  Doing so would require all subsets of a large star of local
states to remain degree two, contradicting Lemma 1.1.

The correct interpretation is

\[
 \boxed{
 \text{quadratic prospective alternatives}
 \quad\ne\quad
 \text{quadratic simultaneous static degree}.}       \tag{5.2}
\]

One frame may be chosen while the factor and its other shore are selected;
the unchosen frames disappear.  This is exactly the useful supply regime
for an LLL, matching, or common-basis selector, but not for a fixed expander
of hereditary circuit toggles.

## 6. Why the H3 `(M0,Q0,J)` route survives

There is an exact positive linear reservoir in the H3 quantifier order.

Let

\[
 \mathcal L={ [2m-1]\choose m-1},
 \qquad
 \mathcal M={ [2m-1]\choose m},                     \tag{6.1}
\]

and fix any perfect containment matching

\[
                         M_0:\mathcal L\longrightarrow\mathcal M.
                                                        \tag{6.2}
\]

Create an outgoing and incoming copy of every `L in \mathcal L`.  Put an arc

\[
                         L_{\rm out}\longrightarrow K_{\rm in}
                                                        \tag{6.3}
\]

when

\[
                         L\subset M_0(K),
       \qquad            L\ne K.                     \tag{6.4}
\]

Call this bipartite graph `P(M0)`.

### Theorem 6.1 (exact linear free-port reservoir)

For every perfect `M0`, the graph `P(M0)` is `(m-1)`-regular on both
shores.  Matchings in `P(M0)` are in bijection with incidence matchings

\[
                         Q\subseteq ML_m-M_0.          \tag{6.5}
\]

Under the bijection, the arc `L -> K` is the rooted link obtained from the
incidence edge `L M_0(K)`.

#### Proof

Fix an incoming vertex `K`.  The `m` rank-`(m-1)` subsets of `M_0(K)` are
its possible tails.  One is `K` itself, leaving exactly `m-1` neighbours in
(6.4).

Fix an outgoing vertex `L`.  It has exactly `m` rank-`m` supersets.  Since
`M_0` is bijective, their inverse images under `M_0` are `m` distinct
incoming roots.  The superset `M_0(L)` gives the excluded loop `K=L`,
leaving exactly `m-1` neighbours.

An incidence `LV` outside `M_0` has the unique head
`K=M_0^{-1}(V)` and gives (6.3).  Distinct tails and distinct heads are
exactly distinct lower and middle endpoints of the incidence edges, i.e. the
matching condition in (6.5). \(\square\)

Thus linear per-port supply is unconditional **after** `M0` has been chosen.
Kőnig's theorem even decomposes `P(M0)` into `m-1` perfect matchings.
What is not automatic is connectivity/acyclicity of a chosen matching after
the rooted Catalan forest is contracted, nor survival after prescribed free
ports are deleted.

There is nevertheless a proof-safe bounded-deletion statement.  If `A` is
deleted from the outgoing shore and `B` from the incoming shore, restrict
any perfect matching of `P(M0)`.  Among the surviving outgoing vertices, at
most `|B|` lose their partners; dually at most `|A|` surviving incoming
vertices are unmatched.  Hence

\[
 \begin{aligned}
 \operatorname {def}_{\rm out}(P(M_0)-A-B)&\le |B|,\\
 \operatorname {def}_{\rm in}(P(M_0)-A-B)&\le |A|.
 \end{aligned}                                      \tag{6.6}
\]

Thus a bounded protected port bank creates only bounded ordinary matching
deficiency at this stage.  This does not control the later graphic/path
condition after `Q0` has consumed almost all ports.

Most importantly, the `m-1` incident arcs are alternatives in a matching.
They are not circuit toggles that may be selected in arbitrary subsets.
Theorem 2.1 therefore does not apply to this reservoir, and there is no
contradiction between its linear degree and the static-host no-go.

The prospective nonlexical construction uses different quantifiers.

1. `M0` chooses one predecessor incidence at every lower root.
2. `Q0` jointly chooses distinct tails, distinct heads, one literal
   occurrence of every immediate-upper colour, and a rooted Catalan forest.
3. After contracting that forest, `J` is a **free-port matching**: at most
   one outgoing and one incoming connector is selected at every component,
   with acyclicity and rooted Hall producing one directed component path.

Alternative frames are not asserted to be simultaneously toggleable.  The
matching consumes one alternative at a port and discards the rest.  Hence
the star of all alternatives is never a legal selected forest, and the
hypothesis of Theorem 2.1 deliberately fails.

This is not a weakness of H3; the affine obstruction proves that such
non-Cartesian selection is necessary for superconstant menus.

Accordingly, the static-expander target should be replaced by the exact
prospective target already isolated there:

\[
 \boxed{
 \begin{array}{c}
 \text{joint protected }(M_0,Q_0)\text{ rooted Catalan forest},\\
 \text{then an acyclic free-port reservoir satisfying all rooted Hall cuts}.
 \end{array}}                                        \tag{6.7}
\]

The appropriate robustness parameter is not edge-connectivity of a static
raw-chain host.  It is the minimum Hall surplus of the residual free-port
bipartite graph after the protected tickets are fixed.

## 7. Exact surviving alternatives

The impossibility theorem leaves three routes.

1. **Joint nonlexical selection.**  Use the quadratic frame lists as
   alternative columns in `(M0,Q0,J)`, never as one Cartesian host.
2. **Multi-socket packets.**  Give each SCD component many distinct physical
   sockets.  Then Theorem 2.1 applies separately at each socket, but packet
   size, upper witnesses, and residence state grow and must be controlled.
3. **Non-Cartesian circuit calculus.**  Permit only colored/partitioned
   subsets of an overlapping circuit family, with an explicit theorem that
   the selected family realizes a free-port path.  Ordinary graphic
   spanning-tree extension no longer applies by itself.

What is ruled out is the hoped-for shortcut

\[
 \text{one fixed nonlexical factor}
 +\text{one root-local C6/C10 expander}
 +\text{arbitrary forest toggles}.                   \tag{7.1}
\]

It cannot simultaneously have linear tail degree and growing edge
connectivity.
