# Protected safe-switch trees: exact cycle-factor fusion and the LKK separation

**Date:** 2026-08-02  
**Lane:** K, prospective direct-new-phase residual topology  
**Status:** exact composition theorem.  It gives a sufficient and, on the
maximum-merge face, necessary auxiliary-tree condition.  It does not prove
that the residual Boolean factor has the required safe-switch supply.

## 0. Outcome

There are two different graphic objects behind the proposed cycle-factor
route.

* A certified two-component pull is a rank-two edge.  Compatible pulls on
  an ordinary spanning tree merge a cycle factor to one cycle.
* A certified ternary Boolean hex whose three deleted adjacencies lie on
  three distinct current cycles is a rank-three hyperedge.  Compatible
  hexes merge to one cycle exactly on a spanning **incidence tree** (a loose
  or Berge hypertree), not merely on a connected 2-section.

The common statement is this.  If `T` is a family of compatible local
switches with original-component footprints `e`, then

\[
       \sum_{e\in T}(|e|-1)=|V|-1                         \tag{0.1}
\]

and

\[
       \sum_{e\in A}(|e|-1)\le |\mathop{\rm union}A|-1
       \qquad(\varnothing\ne A\subseteq T)                \tag{0.2}
\]

are the exact incidence-tree equations.  Under the literal compatibility
hypotheses below, a spanning family satisfying (0.1)--(0.2) produces one
cycle, preserves the marked direct-new-phase arcs, and transports every
resource included in the switch state by its declared additive increment.
It preserves that resource exactly when the total increment is zero (in
particular, when every local increment is zero).

The opposite Lovasz--Kruskal--Katona branches used in the residual
Ore--Ryser theorem prove only existence of a degree-two owner/lower factor.
They do not imply a crossing safe pull for a component cut, let alone a
compatible spanning tree or hypertree.  Thus the cycle-factor route is a
valid replacement for a robust-Hamilton theorem only after one adds an
independent protected switch-supply row.

## 1. Literal switch state

Let `F_0` be a directed spanning two-factor on physical fragments, already
selecting exactly one accepted state in every physical fibre.  Let `P` be
the protected occurrence bank, including the two marked contractions in the
direct-new-phase reduction.

A local switch `z` consists of a deleted arc set `O_z`, an added arc set
`N_z`, and an extended occurrence support `K_z`.  The latter contains the
arcs, every history collar whose value may change, and every occurrence of
a shared resource used to certify the switch.  Its original-component
footprint `e_z` is the set of cycles of `F_0` meeting `O_z`.

Call a family `T` **statically protected-compatible** if:

1. `O_z` is selected and `N_z` is absent in `F_0` for every `z`;
2. `K_z` is disjoint from `P`, and the sets `K_z` are pairwise disjoint;
3. `O_z` and `N_z` use the same physical-fibre multiset and have the same
   degree vector, so every subfamily still selects exactly one state per
   physical fibre and is a two-factor;
4. on the full exported state, the replacement `O_z -> N_z` is either the
   identity or a declared additive increment `gamma_z`; and
5. every `z` is a certified **maximum merger**: whenever the members of
   `e_z` are distinct current cycles, the replacement joins those
   `|e_z|` cycles to one and changes no other component.

For the application, the exported state may include lower and upper
palettes, occurrence-labelled histories, private sockets, integer charge,
finite quotient voltage, and compiler guards.  Equality of unnamed set
inventories is not a substitute for equality of this state.

Pairwise disjoint extended supports are a convenient static sufficient
condition, not a necessary one.  The exact weaker condition is
**hereditary applicability**: for every acyclic subfamily `S` and every
`z notin S` which extends it acyclically, `z` remains a literal accepted
maximum merger in `F_0 triangle S`, with the declared state increment.
Every theorem below remains true under this weaker condition.

### Lemma 1.1 (commutation and protection)

For a statically protected-compatible family, every subfamily may be
applied in any order.  The final selected factor is

\[
 F_T=\left(F_0-\mathop{\dot\bigcup}_{z\in T}O_z\right)
       \mathbin{\dot\cup}
       \mathop{\dot\bigcup}_{z\in T}N_z,              \tag{1.1}
\]

it retains `P`, and its exported state is the initial state plus
`sum_z gamma_z`.

#### Proof

Disjoint extended supports imply that one switch changes neither the old
arcs, new arcs, collar context nor resource witnesses of another.  The
degree/fibre equality makes (1.1) a partition two-factor after every
subfamily.  Protection and the state formula are then literal.  The same
argument is exactly the definition of hereditary applicability.  \(\square\)

The support qualification is load-bearing.  Two switches can have disjoint
deleted edges but share a born edge, history collar, unique upper witness,
or capacity token.  Individual safety in `F_0` does not make such a pair
safe.

## 2. The mixed-rank incidence forest theorem

For a switch family `T`, form its incidence bipartite graph `I(T)`.  One
shore is the original cycle set `V(T)`, the other is `T`, and `v-z` is an
incidence exactly when `v in e_z`.

### Lemma 2.1 (incidence-tree arithmetic)

The following are equivalent.

1. `I(T)` is a tree.
2. `V(T)=union_{z in T} e_z`, (0.1) holds, and (0.2) holds for every
   nonempty `A subseteq T`.
3. The switches admit a rooted order in which the first switch uses only
   new original components and every later `z` meets the union of its
   predecessors in exactly one already merged component and introduces
   `|e_z|-1` new original components.

#### Proof

The incidence graph induced by a nonempty subfamily `A` has
`|union A|+|A|` vertices and `sum_{e in A}|e|` edges.  It is acyclic exactly
when

\[
 \sum_{e\in A}|e|\le |\mathop{\rm union}A|+|A|-1,
\]

which is (0.2).  Equality for the full spanning family is (0.1), and turns
the forest into a tree.  Leaf deletion in the incidence tree, followed by
reversal, gives the rooted order; that order directly reconstructs the
tree.  \(\square\)

### Theorem 2.2 (protected mixed-rank fusion)

Let `T` be a protected-compatible family of certified maximum mergers.  If
`I(T)` is a tree, then applying `T` in a rooted order replaces all cycles in
`V(T)` by one cycle.  Every other cycle is unchanged, and

\[
       c(F_T)=c(F_0)-\sum_{z\in T}(|e_z|-1).          \tag{2.1}
\]

If `V(T)` is the full cycle set of `F_0`, then `F_T` is one marked
partition-Hamilton cycle.  It retains `P` and its exact exported state is
the state in Lemma 1.1.  Hence any exported coordinate is preserved when
`sum_{z in T} gamma_z=0`; otherwise the displayed sum is the exact final
acceptance ledger and must itself be tested.

Conversely, suppose every selected switch is applied once and at its turn
is a maximum merger of the `|e_z|` distinct current components it meets.  If
the switches turn precisely the original cycles in `V` into one cycle, then
their incidence graph is a tree.  Thus (0.1)--(0.2) are necessary on this
maximum-merge face.

#### Proof

Use the rooted order in Lemma 2.1.  At the first step, maximum-merger
semantics joins its footprint to one cycle.  At every later step, exactly
one footprint member belongs to the accumulated cycle and all other members
are new cycles.  Hence the switch still sees `|e_z|` distinct current cycles
and joins them to one.  This proves (2.1) and the forward assertions.

Conversely, maximum mergers lower component count by
`sum_z(|e_z|-1)=|V|-1`.  Every original component must occur, so the
incidence graph is connected.  It has `|V|+|T|` vertices and

\[
 \sum_z|e_z|=\sum_z(|e_z|-1)+|T|=|V|+|T|-1
\]

edges.  A connected graph with one fewer edge than vertices is a tree.
\(\square\)

## 3. Graph pulls versus ternary hexes

For binary maximum-merger pulls, every footprint has size two.  Then
(0.2) is ordinary graphic acyclicity, and Theorem 2.2 says:

> a protected-compatible labelled spanning tree in the auxiliary pull
> multigraph is necessary and sufficient on the maximum-merger face.

In particular, connectivity of the labelled auxiliary graph is enough only
when one may choose a spanning tree whose literal packet representatives are
mutually compatible.  Connectivity after forgetting packet conflicts is
not enough.

For ternary Boolean hexes, every footprint has size three.  Equations
(0.1)--(0.2) become

\[
       |V|=2|T|+1,
       \qquad 2|A|\le |\mathop{\rm union}A|-1.        \tag{3.1}
\]

This is precisely a loose/Berge hypertree.  It also exposes the parity
restriction: pure ternary contraction can span only an odd number of old
cycles.

### Proposition 3.1 (connected 2-section is insufficient)

Let

\[
 e_1=\{1,2,3\},\qquad e_2=\{1,2,4\},\qquad
 e_3=\{1,2,5\}.                                      \tag{3.2}
\]

The 2-section and the incidence hypergraph are connected, but there is no
spanning ternary incidence tree.  Every pair of hyperedges already violates
`2|A| <= |union A|-1`.  After one three-cycle fusion, each remaining
hyperedge meets only two current components, so its certified three-cycle
fusion rule no longer applies.

This is the exact reason one must not replace the loose-hypertree row by
ordinary auxiliary connectivity.

## 4. A finite labelled-supply criterion

It is sometimes easier to prove an abstract tree first and then choose a
literal switch for every tree edge.  Let `R_e` be the list of literal packet
realisations of an edge/hyperedge `e` in a fixed incidence tree `T`.  Suppose
the protected bank deletes at most `lambda |P|` members of every list, and
every surviving packet conflicts with at most `Delta` members of any other
one list.  If

\[
       \min_{e\in T}|R_e|>
       \lambda|P|+(|T|-1)\Delta,                     \tag{4.1}
\]

then `T` has protected-compatible literal representatives.

#### Proof

Process the tree edges in any order.  At step `i`, protection has removed at
most `lambda|P|` choices and the previously selected `i-1` packets exclude
at most `(i-1)Delta`.  Inequality (4.1) leaves a choice.  \(\square\)

This deliberately elementary criterion is not asserted for the current
Boolean host.  It records the exact list/load statement which would turn
abstract component connectivity into literal safe-switch connectivity.

## 5. Why residual LKK expansion does not supply the tree

The residual Ore theorem proves every capacity-two shore inequality in the
rank-`(m-1)`/rank-`m` containment graph after the protected bank.  Its two
opposite LKK branches concern only the projected incidence degrees.  They
do not mention:

* which projected incidences lie in the selected two-factor;
* whether a crossing alternating `C6/C8` is present;
* whether a switch has maximum-merger stub pairing;
* occurrence-labelled history or upper/common-cap transparency; or
* conflicts between switch collars.

Consequently those inequalities cannot imply a spanning switch tree.  A
literal separation is obtained by refining every selected factor component
with its component label and accepting only state transitions preserving
that label.  This changes no projected incidence, degree, codegree, protected
demand or LKK calculation, but every cross-component safe-switch list is
empty.  Equivalently, the known hex-free-factor constructions show that even
strong projected marginal hypotheses need not leave one applicable short
Boolean hex.

The weakest extra topology hypothesis is therefore:

> **Protected safe-switch basis.**  The chosen residual partition
> two-factor admits either (i) an exchange-independent labelled spanning
> tree of certified binary mergers, or (ii) an exchange-independent
> spanning incidence hypertree of certified ternary mergers, with the
> direct-new-phase marked arcs included in the protected state.

Under this hypothesis, Theorem 2.2 closes topology.  LKK supplies marginal
factor existence only.  It gives no positive lower bound on any switch cut,
so the safe-switch basis remains an independent correlation row.

## 6. Scope

The theorem composes whatever state is literally included in the extended
supports and local equality tests.  It does not infer residence, deeper
upper coverage, integer background charge, quotient voltage or compiler
safety from owner/lower exactness.  In particular:

* the exact corrected `C6` stub formula allows component deltas
  `-2,-1,0,+1,+2`; a catalogue entry is a ternary hyperedge here only after
  the `-2` maximum-merger condition is proved;
* an individually upper-safe switch family may lose a unique upper witness
  in combination unless occurrence supports or the final multiset ledger
  are controlled;
* disjoint arc supports do not imply disjoint history collars; and
* finite quotient voltage and regenerative integer charge are different
  exported coordinates.

Thus the cycle-factor alternative is exact, but its new live theorem is a
protected, occurrence-labelled switch-basis supply theorem, not another
Ore--Ryser shore inequality.
