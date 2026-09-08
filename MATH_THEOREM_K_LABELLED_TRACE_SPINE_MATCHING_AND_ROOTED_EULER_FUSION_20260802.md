# Labelled trace spine matching and rooted Euler fusion

**Date:** 2026-08-02  
**Status:** unconditional post-rounding theorem, exact obstruction for the
tail-fixed exchange class, and a concrete sufficient fusion certificate.
This note assumes that the one-copy owner and named-target rounding has
already been obtained.  It does not prove that rounding for the triangular
pull clock.

## 0. Outcome

The corrected pull-clock theorem supplies a stationary fractional
circulation, but a successful integral rounding may still have many Euler
components.  The topology row has an exact literal structure which is more
rigid than an abstract transportation rectangle.

Write an order-`d` trace arc as

\[
        e=(A_0,A_1,\ldots,A_{d-1},A_d).
\]

Its **internal spine** is

\[
        \sigma(e)=(A_1,\ldots,A_{d-1}).
\]

Two tail-fixed arcs can exchange heads in a de Bruijn `2x2` switch if and
only if their internal spines are equal.  Once owner and named-target
payloads are included, the two exchanged terminal letters must additionally
be mutually admissible for those same labelled payloads.

This gives three exact positive results.

1. After fixing all tails, every label-preserving balanced rerouting is a
   product of bipartite perfect matchings, one for each internal spine.
   This is an integral flow face.
2. Suppose the current circulation contains complete terminal-exchange
   pools and the bipartite incidence graph between its Euler components and
   those pools is connected.  Then successive transparent `2x2` switches
   merge all components into one while preserving every owner and every
   named target occurrence.  If one protected root arc is not switched, the
   final Euler circuit starts at that root.  The sidecar cost is zero.
3. On the rigid face where every owner marks a strict chain at all `d`
   proper suffix depths, balance is exactly a directed cycle cover in an
   explicit chain-overlap graph.  Zero-sidecar serialization is exactly a
   Hamilton cycle in that graph.

There is also an exact obstruction.  If the component--pool incidence graph
has `b` connected components, pool switches can never join two of those
blocks, and they can fuse each block internally.  Thus their exact minimum
component count is `b`.  Any uncoloured sidecar then uses at least `b-1`
extra trace edges; even `b=O(1)` gives only `O(d)` overhead unless the
remaining endpoint states have total overlap deficit `O(1)`.

Accordingly, after common integral owner/target rounding, the smallest
remaining pull-clock fusion lemma is not generic connected support.  It is:

> choose the rounding so that its payload-transparent spine pools have a
> connected component-incidence graph, while retaining one prepared root.

This condition is sufficient for exact rooted Euler serialization and is
strictly stronger than fractional stationarity, state balance, or separate
owner and target exactness.

## 1. Label-perfect trace circulations

Let

\[
                    \mathcal A=2^{[k]}\setminus\{\varnothing\}
\]

and let `D_d(A)` be the order-`d` de Bruijn digraph.  Its vertices are
words in `A^d`; the trace word

\[
                    (A_0,\ldots,A_d)                 \tag{1.1}
\]

is the arc

\[
 (A_0,\ldots,A_{d-1})\longrightarrow(A_1,\ldots,A_d).
                                                               \tag{1.2}
\]

Let `Lambda` be a set of occurrence labels.  A label records at least

* one rank-`r` owner;
* every named residual lower target marked on this occurrence; and
* every protected pin or boundary role which must remain on the same
  occurrence.

It may record more data.  For `lambda in Lambda`, let `E_lambda` be the
menu of literal traces carrying exactly that payload.

A **label-perfect circulation** is a choice

\[
                    e_\lambda\in E_\lambda
                    \qquad(\lambda\in\Lambda)         \tag{1.3}
\]

such that

\[
             \sum_{\lambda\in\Lambda}\partial e_\lambda=0.    \tag{1.4}
\]

When the owner projection of `Lambda` is bijective and its marked-target
payloads partition the residual lower deck, (1.3) is exactly one trace per
owner and one occurrence per residual named target.  Parallel literal
state arcs remain occurrence-labelled.

Let `Comp(F)` be the weak components of the positive support of a
label-perfect circulation `F`.  Because every vertex is balanced, every
nontrivial weak component is Eulerian.

## 2. De Bruijn rectangle rigidity

For an arc (1.1), define its spine and terminal letter by

\[
 \sigma(e)=(A_1,\ldots,A_{d-1}),\qquad \tau(e)=A_d.   \tag{2.1}
\]

For `d=1`, the spine is the unique empty word.

Consider two selected arcs

\[
 e=(A_0,A_1,\ldots,A_{d-1},A_d),\qquad
 f=(B_0,B_1,\ldots,B_{d-1},B_d).                     \tag{2.2}
\]

Keep their tails fixed and ask whether the crossed heads are de Bruijn
arcs:

\[
\begin{aligned}
 e'&=(A_0,A_1,\ldots,A_{d-1},B_d),\\
 f'&=(B_0,B_1,\ldots,B_{d-1},A_d).
\end{aligned}                                                \tag{2.3}
\]

### Lemma 2.1 (spine equality is exact)

Both crossed arcs in (2.3) are literal de Bruijn arcs with the declared old
tails and crossed old heads if and only if

\[
                         \sigma(e)=\sigma(f).          \tag{2.4}
\]

#### Proof

The head of `f` is `(B_1,...,B_d)`.  It may follow the tail
`(A_0,...,A_(d-1))` precisely when its length-`d-1` prefix equals the
tail's length-`d-1` suffix:

\[
                  (B_1,\ldots,B_{d-1})
                    =(A_1,\ldots,A_{d-1}).            \tag{2.5}
\]

The other crossed arc gives the same equality.  This is (2.4).  For `d=1`
there is no overlap condition, as asserted.  \(\square\)

Spine equality guarantees only literal de Bruijn geometry.  The crossed
words must still lie respectively in `E_lambda` and `E_mu`.  This is the
exact owner/target correlation which an unlabelled state-flow argument
forgets.

### Corollary 2.2 (transparent rectangle)

Let `e_lambda,e_mu` be selected arcs of equal spine.  If the crossed words
in (2.3) belong respectively to `E_lambda,E_mu`, then replacing

\[
                    e_\lambda+e_\mu
                       \quad\hbox{by}\quad
                    e'_\lambda+e'_\mu                 \tag{2.6}
\]

preserves:

1. every state indegree and outdegree;
2. every owner label;
3. every marked named-target occurrence; and
4. every protected payload not explicitly excluded from the two menus.

The state assertion follows because (2.6) preserves the tail multiset and
the head multiset.  The other assertions follow because each replacement
stays in its original labelled menu.

### Lemma 2.3 (literal hinge rectangle for a nonfull chain)

Let

\[
 \varnothing=S_0\subsetneq S_1\subsetneq\cdots
   \subsetneq S_\ell\subsetneq T,
 \qquad 1\le\ell\le d-1.                               \tag{2.7}
\]

Choose `x in S_1`.  There is a family of admissible traces with a common
spine and with complete terminal pool

\[
                  \{B:\varnothing\ne B\subseteq S_1\}. \tag{2.8}
\]

Every member has owner `T`, and its suffix of length `j+1` has union `S_j`
for `1<=j<=ell`.

#### Proof

Put

\[
\begin{aligned}
 B_i&=\{x\} &&(1\le i\le d-\ell-1),\\
 B_{d-j}&=S_j\setminus S_{j-1} &&(2\le j\le\ell),\\
 B_{d-1}&=S_1,\\
 B_0&=(T\setminus S_\ell)\cup A &&(A\subseteq S_\ell),\\
 B_d&=B &&(\varnothing\ne B\subseteq S_1).
\end{aligned}                                             \tag{2.9}
\]

The middle word `(B_1,...,B_(d-1))` is independent of `A,B`.  The last
`j+1` letters have union `S_j`, because `B` is already contained in `S_1`.
The full union is `T`, because `B_1,...,B_(d-1)` cover `S_\ell` and `B_0`
contains `T\setminus S_\ell`.  Thus varying `B` gives the complete terminal pool
(2.8), with every declared payload fixed.  \(\square\)

If two occurrence labels use the same spine and their permitted first
targets both contain a common terminal family, Lemma 2.3 gives a physical
exchange pool.  When `\ell=d` and all `d` proper suffix ranks are marked,
the `d` strict targets use all `d` proper suffix lengths and the head word is
forced.  That rigid face is treated separately in Section 5.

## 3. Exact product-of-matchings factorization

Fix a label-perfect circulation `F`, and freeze the tail of every selected
labelled arc.  For a spine `s`, let `Lambda_s` be the labels whose frozen
tails have suffix spine `s`.  Make one separately labelled token for every
selected head of spine `s`; write this token multiset as `H_s`.  A token
`h` remembers its literal head `(s,Z_h)`, including multiplicity.

Define the bipartite graph

\[
             G_s=(\Lambda_s,H_s;\mathcal E_s)         \tag{3.1}
\]

by joining `lambda` to `h` exactly when appending the terminal letter
`Z_h` to the frozen tail of `lambda` gives a trace in `E_lambda`.

The current circulation gives a distinguished perfect matching `M_s` in
every `G_s`.

### Theorem 3.1 (tail-fixed labelled circulation factorization)

There is a bijection between

1. tail-fixed label-perfect circulations which preserve the current head
   multiset at every state, and
2. choices of one perfect matching in every graph `G_s`.

In particular, the convex hull of all such reroutings is the direct product
of bipartite perfect-matching polytopes and is integral.

#### Proof

A matching edge `lambda h` spells one literal trace with the frozen tail of
`lambda`, the common spine `s`, and terminal letter `Z_h`.  Membership in
`G_s` says exactly that the trace retains the complete payload of `lambda`.
A perfect matching uses every label once and every old head token once.
Hence it preserves the complete tail and head multisets, so its state
boundary is unchanged and remains zero.

Conversely, a tail-fixed rerouting has the same outgoing multiplicity at
every state as `F`.  To remain balanced it must have the same incoming
multiplicity, hence the same head-token multiset.  Lemma 2.1 forces every
head token to remain within its spine.  Assigning those tokens to the
labels therefore gives a perfect matching in each `G_s`.  The standard
bipartite matching theorem gives integrality.  \(\square\)

Protected labelled arcs are handled by deleting their label vertices and
their matched head tokens before applying Theorem 3.1.  Thus a rooted pin
is not averaged or reconstructed after the rerouting.

The theorem is a genuine integral-flow statement, but it does not by itself
make the selected support connected.  Connectivity couples the otherwise
independent spine matchings.

## 4. Complete exchange pools and exact component fusion

First record the sharp one-packet form.  It is often easier to plant than a
whole pool atlas.

### Theorem 4.1 (connected head-permutation packet)

Let `F` have components `C_1,...,C_c`.  Choose one unprotected selected arc

\[
                   e_i=(A_{i,0},s,Z_i)\in C_i         \tag{4.1}
\]

from every component, all with the same internal spine `s`.  Suppose there
is a cyclic permutation `pi` of `{1,...,c}` such that

\[
                 (A_{i,0},s,Z_{\pi(i)})\in E_{\lambda_i}
                    \qquad(1\le i\le c),              \tag{4.2}
\]

where `lambda_i` is the complete old payload label of `e_i`.  Then replacing
every `e_i` by the trace in (4.2) produces one rooted label-perfect Euler
circuit with zero sidecar.

#### Proof

The replacement fixes every tail and cyclically permutes the complete head
token multiset, so state balance is unchanged.  Condition (4.2) preserves
each owner, marked-target set, and pin payload separately.  Removing one arc
from each balanced component leaves that component weakly connected.  The
new arc with tail in `C_i` has head in old component `C_(pi(i))`; since `pi`
is one cycle, these crossed arcs connect all retained component blocks.
Euler's theorem and rotation to the untouched protected root finish.  \(\square\)

If `pi` has `b` cycles, the same proof leaves exactly the unions indexed by
those `b` cycles.  Thus the topology of a head-permutation packet is visible
before any physical replay.

An **exchange pool** `P` in one `G_s` consists of equally sized sets

\[
             L(P)\subseteq\Lambda_s,\qquad
             R(P)\subseteq H_s                          \tag{4.3}
\]

such that

1. `G_s[L(P),R(P)]` is complete bipartite;
2. the current matching maps `L(P)` bijectively onto `R(P)`; and
3. none of the labels in `L(P)` is protected.

Thus the terminal heads may be permuted arbitrarily among the labels in a
pool while preserving every payload.

For a family `Pcal` of pairwise label- and head-token-disjoint exchange
pools, form the **component--pool incidence graph**

\[
                         B_F(\mathcal P).              \tag{4.4}
\]

Its left vertices are `Comp(F)`, its right vertices are the pools, and
`C-P` is an edge when component `C` contains a selected labelled arc from
`L(P)`.

### Theorem 4.2 (protected rooted pool-fusion theorem)

If `B_F(Pcal)` is connected, transparent `2x2` switches inside the pools
turn `F` into one weakly connected label-perfect circulation.  Exactly
`|Comp(F)|-1` switches suffice.  Every owner, named target, and protected
arc is retained literally.  Consequently the final support has an Euler
circuit, and that circuit may be rotated to begin with any prescribed
protected root arc.

No extra source letter or sidecar edge is used.

#### Proof

Suppose the current support has at least two components.  Connectivity of
the incidence graph implies that some pool is incident with two distinct
current component blocks.  Choose one currently selected arc from that pool
in each block.  Their heads are distinct: otherwise the two old components
would share a positive-degree state.  Completeness of the pool makes the
crossed pair legal with the same two labelled payloads.

Each selected arc in a balanced weak component lies on a directed cycle.
Removing it therefore leaves its old component weakly connected.  The two
crossed arcs join the two old components, so Corollary 2.2 merges exactly
those blocks and preserves balance and all labels.

Contract the two component vertices in (4.4).  The incidence graph remains
connected, and pool membership remains available because labels and head
tokens have only been permuted inside the same pool.  Iteration takes
exactly one switch per component merger, hence `|Comp(F)|-1` switches.

A weakly connected balanced directed multigraph has an Euler circuit.  The
protected root arc was never removed and appears in that circuit; cyclically
rotate the circuit so that this occurrence is first.  \(\square\)

The proof permits reuse of a pool in several mergers.  It does not require
a resource-disjoint switch bank beyond the disjoint definition of the pool
atlas itself.

### Corollary 4.3 (exact pool obstruction)

Let `b` be the number of connected components of `B_F(Pcal)` after deleting
isolated pool vertices.  (All circulation-component vertices, including
isolated ones, remain.)  Under switches using only `Pcal`, the minimum
possible number of circulation components is exactly `b`.

#### Proof

Theorem 4.2 fuses every connected incidence block internally.  A pool switch
uses two labels incident with the same pool, hence can only contract
component vertices already lying in the same incidence block.  No switch
can join two different blocks.  \(\square\)

This is a move-class obstruction, not a no-go for larger alternating
circuits, tail changes, or source-changing packets.

## 5. The rigid full-depth face is exactly a Hamilton problem

There is a complementary exact reduction when every selected occurrence
marks a strict chain of all `d` proper suffix depths.  Let

\[
 \varnothing=S_{i,0}\subsetneq S_{i,1}\subsetneq\cdots
   \subsetneq S_{i,d}\subsetneq T_i
       \qquad(1\le i\le W),                            \tag{5.1}
\]

and suppose all named sets `S_(i,j)` are globally distinct.  Define the
nonempty increments `A_(i,p)` by

\[
 A_{i,d-j+1}=S_{i,j}\setminus S_{i,j-1}
                \qquad(1\le j\le d),                  \tag{5.2}
\]

and put

\[
                         h_i=(A_{i,1},\ldots,A_{i,d}). \tag{5.3}
\]

The states `h_i` are distinct: equality would make all their suffix unions,
hence all the `S_(i,j)`, equal.

Form a directed graph `D_C` on the owner-chain indices.  Put an arc
`j -> i` exactly when

\[
\begin{aligned}
 (A_{j,2},\ldots,A_{j,d})
     &=(A_{i,1},\ldots,A_{i,d-1}),\\
 T_i\setminus S_{i,d}
     &\subseteq A_{j,1}\subseteq T_i.                 \tag{5.4}
\end{aligned}
\]

### Theorem 5.1 (fixed-head cycle-cover equivalence)

The full-depth chains (5.1) admit a balanced one-copy literal trace
selection if and only if `D_C` has a directed cycle cover.  The selected
trace support is one rooted zero-sidecar Euler circuit if and only if the
cycle cover is one Hamilton cycle (containing the prescribed root arc, when
one is fixed).

#### Proof

Realizing all `d` strict suffix targets forces the last `d` source letters
of owner `i` to be exactly `h_i`: successive differences of the suffix
unions give (5.2).  Its first source letter `B_(i,0)` is legal precisely
when

\[
             T_i\setminus S_{i,d}
                \subseteq B_{i,0}\subseteq T_i.       \tag{5.5}
\]

Every selected edge therefore has fixed head `h_i`.  Since the `h_i` are
distinct and the selected multiset is balanced, its tail multiset must be
the same set `{h_1,...,h_W}`.  Thus there is a permutation `pi` with tail
of trace `i` equal to `h_(pi(i))`.  Literal overlap and (5.5) say exactly
that `pi(i) -> i` is an arc of `D_C`.  Hence `pi` is a directed cycle cover.

Conversely, an arc `j -> i` spells the trace

\[
             (A_{j,1},A_{i,1},\ldots,A_{i,d}),       \tag{5.6}
\]

which has owner `T_i` by (5.4), has the forced suffix chain by (5.2), and
runs from state `h_j` to state `h_i`.  A cycle cover uses every tail and
head state once, so it is balanced.  Its weak Euler components are exactly
the permutation cycles.  Therefore connectedness is equivalent to one
Hamilton cycle, and a protected arc roots that cycle by rotation.  \(\square\)

### Corollary 5.2 (exact Hall row)

The full-depth chains have a balanced one-copy trace selection if and only
if

\[
                  |N^-_{D_C}(I)|\ge |I|
                    \qquad(I\subseteq[W]),            \tag{5.7}
\]

where `N^-` denotes the possible predecessor vertices of the owner set
`I`.  If one root arc `j_0 -> i_0` is prescribed, delete its two matching
vertices and impose the same inequalities on the residual bipartite graph.

#### Proof

Split every vertex of `D_C` into a predecessor copy and an owner-head copy.
A directed cycle cover is exactly a perfect matching between these two
shores.  Equation (5.7) is Hall's theorem.  A prescribed root arc consumes
its two endpoints.  \(\square\)

### Corollary 5.3 (literal cycle-cover rectangle)

If a cycle cover contains arcs

\[
                         j\to i,\qquad \ell\to m      \tag{5.8}
\]

on two different cycles, and `j -> m, \ell -> i` are also arcs of `D_C`,
then replacing (5.8) by those two crossed arcs preserves every owner and
every chain target and merges the two cycles.

This is the fixed-head dual of Corollary 2.2.  It shows that the full-depth
post-rounding fusion problem is exactly a coloured Hamilton/cycle-exchange
problem, not a remaining rank-marginal problem.

## 6. A static fusion-tree certificate without complete pools

Complete pools are convenient but stronger than necessary.  There is an
exact static certificate using isolated transparent rectangles.

Let the initial components be `C_1,...,C_c`, and let `T` be a tree on these
components.  For every tree edge `ij`, choose one selected arc in `C_i` and
one in `C_j` which form a transparent rectangle.  Require:

1. all `2(c-1)` removed labelled arcs are distinct and unprotected;
2. every replacement arc retains its old complete payload;
3. after deleting all designated arcs, the retained support inside every
   `C_i` is weakly connected; and
4. all replacement occurrences are simultaneously admissible.

### Theorem 6.1 (protected transparent fusion tree)

Under these four conditions, performing all tree rectangles simultaneously
produces one rooted label-perfect Euler circuit with no sidecar.

#### Proof

Every rectangle preserves the complete tail and head multisets, hence their
sum preserves state balance and every labelled row.  Condition 3 leaves one
connected retained block for each tree vertex.  The two added crossed arcs
for tree edge `ij` join the retained blocks of `C_i,C_j`.  Since `T` is
connected, the final support is weakly connected.  The protected root
survives, and Euler's theorem finishes as in Theorem 4.1.  \(\square\)

Condition 3 is necessary in a simultaneous certificate: although deleting
one arc from an Euler component never disconnects it, deleting several
designated arcs can.

## 7. Exact sidecar ledger after maximal pool fusion

Let the pool theorem leave directed Euler components

\[
                         Q_1,\ldots,Q_b.
\]

Choose an exit state `v_i` on `Q_i` and an entry state `u_i` on `Q_i`.
For an ordering `pi`, the trace-Euler serialization theorem gives the
uncoloured overhead

\[
 \sum_{j=1}^{b-1}
   \left(d-\operatorname{ov}
       (v_{\pi(j)},u_{\pi(j+1)})\right),               \tag{7.1}
\]

where `ov` is exact suffix--prefix overlap of order-`d` states.

Two consequences must be kept separate.

* Every sidecar has at least `b-1` edges, because one edge merges at most
  two weak components.
* The statement `b=O(1)` gives only `O(d)` overhead in general.  Additive
  `O(1)` requires an ordering and endpoints for which (7.1) is `O(1)`, or
  a further transparent fusion packet.

Thus a bounded number of circulation components is not itself the desired
bounded-sidecar theorem.

## 8. Rebase on the corrected pull clock

The proved stationary pull-clock circulation closes the real fractional
trace row.  Suppose a separate theorem rounds it to a label-perfect
circulation `F` with

1. one trace per rank-`r` owner;
2. one occurrence of every residual named lower target; and
3. one protected root trace.

Theorem 3.1 then gives the exact tail-fixed integral fibre of `F`.  Theorem
4.2 proves rooted zero-sidecar serialization from a connected transparent
spine-pool incidence graph.  Equivalently, Theorem 6.1 permits a static
protected transparent fusion tree.  On the rigid full-depth face, Theorem
5.1 replaces both by the exact Hamilton-cycle condition in `D_C`.

The minimal remaining post-rounding assertion is therefore:

> **Pull-clock spine-interlacing lemma.**  One can choose the common
> owner/target-exact rounding and its root so that the tail-fixed
> admissibility graphs contain either a connected exchange-pool atlas or a
> protected transparent fusion tree; on every rigid full-depth block, the
> corresponding graph `D_C` has a compatible cycle-exchange route to one
> Hamilton cycle.

For a bounded-sidecar version it suffices instead that the pool incidence
has `O(1)` blocks and that their exact overlap tour (7.1) is `O(1)`.

Neither statement follows from the stationary rank marginals.  The
fractional theorem averages over owners, core choices, private orders,
block placements, and marked-target thinning; none of those averages
forces two integral traces to share a literal spine, much less to accept
each other's terminal letters with the same named payload.

## 9. Sharp scope

The note proves, after an integral label-perfect selection:

* exact de Bruijn geometry of every tail-fixed `2x2` switch;
* a product-of-bipartite-matchings description of the tail-fixed fibre;
* an explicit connected-pool theorem yielding one rooted Euler circuit;
* an exact full-depth cycle-cover/Hamilton reduction;
* a static protected fusion-tree theorem; and
* the exact component and overlap sidecar ledgers for this move class.

It does not prove:

* the common integral owner/target rounding;
* the pull-clock spine-interlacing lemma;
* residence or upper interval-union coverage after source changes;
* a common-cap compiler; or
* a full upper bound for `nu(k)`.

The theorem is compatible with arbitrary extra guarded rows only when those
rows are included literally in each label menu `E_lambda`.  Setwise or
rankwise equality after the switch is not a substitute for occurrence-level
payload transparency.
