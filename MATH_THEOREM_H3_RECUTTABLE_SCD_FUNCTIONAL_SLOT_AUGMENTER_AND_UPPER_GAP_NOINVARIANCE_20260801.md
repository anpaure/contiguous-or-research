# Recuttable SCD packets have an exact functional-slot completion theorem,
# while the `P-2^d` upper-gap identity is false

**Date:** 2026-08-01  
**Lane:** H3 / protected nonlexical SCD host  
**Status:** exact SCD cut algebra; exact finite refutation of the proposed
upper-gap identity; exact conditional local-to-global repair and protected
connector theorems.  No all-dimensional closed-packet supply, endpoint
expansion, deep-ticket assignment, common source or compiler is proved.

## 0. Verdict

There is one genuine square identity and one accidental near-square.

* If an upper-`q1`-exact, lower-rainbow Catalan forest has `C_m` path
  components and `t` internal edges are cut, then it has

  \[
                         P=C_m+t
  \]

  pieces and exactly `P` missing lower-`q1` colours before new seams are
  inserted.  The pieces are resident only when the cut set hits the declared
  residence-defect intervals.  The count itself is structural.
* The number `H(D)` of post-cut upper holes is not determined by `P`, `t`,
  `m` or the residence depth.  For the canonical `k=17` cutting,

  \[
             P=6281,\qquad H=6273=P-8=P-2^3,
  \]

  but another authenticated minimum cutting of the same SCD bank has the
  same `P=6281` and `H=6055`, hence `P-H=226`.  Thus `P-H=2^d` already
  fails without changing `m`, `d`, the central forest or the number of
  cuts.

Moreover, the whole unchanged `1419`-cut minimum face is impossible for
ordinary endpoint-seam reassembly at rank ten: every global minimum-pattern
choice contains unsupported selected cut colours in the complete
option-conditioned one-seam relaxation.  The canonical
`322` zero-provider count is only one fixed-cut manifestation.  The live
route must therefore permit extra cuts, a local resident socket/ear, or an
interior rethread, and must select that repair together with its endpoint
state and upper tickets.

The exact positive statement is a **functional-slot theorem**.  A bounded
local recut/augmenter packet may be treated as one matching edge only when
it is closed under its new cut casualties, is boundary-state and deck
transparent, and all resource conflicts between different packets factor
through one physical site.  On that face ordinary defect Hall is necessary
and sufficient.  Singleton support alone has no bounded-defect consequence.

## 1. Structural SCD cut algebra

Put `k=2m-1` and write

\[
 \mathcal L={ [k]\choose m-1},\qquad
 \mathcal O={ [k]\choose m},\qquad
 \mathcal U={ [k]\choose m+1}.
\]

Let \(W_m=|\mathcal L|=|\mathcal O|\), \(U_m=|\mathcal U|\), and

\[
              C_m=W_m-U_m=\operatorname {Cat}_m
                  ={2W_m\over m+1}.                         \tag{1.1}
\]

Use the coherent central normal form.  Thus
\(M_0:\mathcal L\to\mathcal O\) is a perfect incidence matching and
\(\pi\) is an acyclic partial injection such that, for every
\(x\in\operatorname {dom}(\pi)\),

\[
 M_0(x)\cap M_0(\pi x)=x,
 \qquad
 x\longmapsto M_0(x)\cup M_0(\pi x)
\]

bijects \(\operatorname {dom}(\pi)\) onto \(\mathcal U\).  The resulting directed physical forest
has `U_m` edges and `C_m` path components.

Let \(D\subseteq\operatorname {dom}(\pi)\) be a set of cut edges,
\(t=|D|\), and let \(\pi_D\) be the restriction of \(\pi\) to
\(\operatorname {dom}(\pi)\setminus D\).

### Theorem 1.1 (pieces, sources, terminals and the lower square)

The cut forest has

\[
                            P=C_m+t                              \tag{1.2}
\]

directed pieces.  Its terminal- and source-root banks are

\[
 T_D=\mathcal L\setminus\operatorname {dom}(\pi_D),
 \qquad
 S_D=\mathcal L\setminus\operatorname {im}(\pi_D),              \tag{1.3}
\]

and both have cardinality `P`.  The retained lower-`q1` colours are exactly
`dom(pi_D)`, so the raw missing lower bank has cardinality

\[
 W_m-(U_m-t)=C_m+t=P.                                            \tag{1.4}
\]

For `a in T_D` and `s in S_D`, a forward connector from the terminal owner
`M_0(a)` to the source owner `M_0(s)` has lower colour `a` exactly when

\[
                         a\subset M_0(s),\qquad a\ne s.          \tag{1.5}
\]

Thus on the coherent forward face the lower colour of a connector is
source-private: it is fixed by its outgoing terminal task.

#### Proof

Deleting one edge of a forest increases its component count by one, which
gives (1.2).  A root is terminal precisely when it has no outgoing
`pi_D` edge and is a source precisely when it has no incoming edge, proving
(1.3).  The `U_m-t` retained edges have distinct lower colours, so (1.4)
follows.

Both `M_0(a)` and `M_0(s)` have rank `m`, while `a` has rank `m-1` and is
already contained in `M_0(a)`.  Under (1.5), the two distinct owners have
intersection exactly `a`; conversely a connector of lower colour `a` forces
that containment.  \(\square\)

If the cuts stab every forbidden short-run interval, the pieces are
internally depth-`d` factorable.  This does not make their reassembly
resident: constant-one pieces can transmit a run across several seams, so
the capped boundary-age automaton must still be composed globally.

## 2. The exact upper-hole formula

For `r>=m+1`, let `Deck_r(F)` be the set of rank-`r` unions of arbitrary
contiguous owner intervals lying in one component of `F`.  Define the
pre-existing deep-hole count

\[
 A(F)=\sum_{r=m+2}^{k}
       \left|{[k]\choose r}\setminus\operatorname {Deck}_r(F)\right|,
                                                                    \tag{2.1}
\]

and the distinct deep casualties of a cut set by

\[
 B_F(D)=\sum_{r=m+2}^{k}
       \left|\operatorname {Deck}_r(F)
        \setminus\operatorname {Deck}_r(F-D)\right|.              \tag{2.2}
\]

Because every cut colour at rank `m+1` had one old provider and the old
palette was exact, cutting `t` edges creates exactly `t` immediate-upper
holes.

### Theorem 2.1 (deep collateral is the only uncancelled scalar)

The complete post-cut upper-hole count is

\[
                         H_F(D)=t+A(F)+B_F(D),                     \tag{2.3}
\]

and therefore

\[
                         P-H_F(D)=C_m-A(F)-B_F(D).                 \tag{2.4}
\]

In particular,

\[
                 H_F(D)=P-2^d
 \quad\Longleftrightarrow\quad
                 A(F)+B_F(D)=C_m-2^d.                             \tag{2.5}
\]

Equation (2.5) is an additional cut-dependent deep-shadow equality.  It is
not an Euler consequence of the SCD component count.

#### Proof

At every deep rank, the old holes and values lost by cutting are disjoint:
the first family was absent from `Deck_r(F)`, while the second was present
there and absent after cutting.  Summing those disjoint banks and adding
the `t` immediate-upper holes proves (2.3).  Substitute (1.2) to obtain
(2.4)--(2.5).  \(\square\)

This formula also explains why a count of cut positions cannot determine
the upper debt.  Different minimum transversals can destroy different
unique long-interval occurrences, so `B_F(D)` is not a function of `|D|`.

## 3. `k=17` refutes the boundary-cube identity on one fixed SCD bank

For the earliest-right minimum cutting of the authenticated `m=9,d=3`
forest,

\[
 C_9=4862,\qquad t=1419,\qquad P=6281.
\]

Its post-cut hole vector at ranks ten through fifteen is

\[
                  (1419,2454,1655,608,122,15),                    \tag{3.1}
\]

so `H=6273` and `P-H=8=2^3`.  In the notation of Theorem 2.1,

\[
 A(F)=911+608+135+8=1662,\qquad
 B_F(D)=1543+1047+473+114+15=3192,                               \tag{3.2}
\]

and `4862-1662-3192=8`.

The equality is not stable even inside the all-minimum-cut atlas.  A second
authenticated endpoint-degree minimum segmentation has the same
`m,d,t,P`, but its hole vector is

\[
                  (1419,2398,1576,549,102,11).                    \tag{3.3}
\]

Hence

\[
                  H=6055,\qquad P-H=226.                         \tag{3.4}
\]

The deep casualty term has changed by `218` while every scalar in (1.2) is
unchanged.  Two further resident refinement fixtures point in the opposite
direction:

\[
\begin{array}{c|c|c|c}
\text{fixture}&P&\text{rank-10--15 holes}&P-H\\ \hline
\text{ten-facet isolation}&6475&(1613,2595,1728,640,133,18)&-252\\
\text{eight-facet isolation}&6433&(1571,2556,1708,630,128,16)&-176.
\end{array}                                                       \tag{3.5}
\]

Thus neither `P-H=2^d` nor even `H<=P` is a residence-segmentation
invariant.

The frozen `m=4,...,8` phase-detachment fixtures certify only the central
owner/lower/immediate-upper forests.  Their authenticated notes explicitly
do not certify residence segmentation or arbitrary-width upper decks, so
they provide no legitimate lower-dimensional values of `B_F(D)` with which
to test (2.5).  The required numerical equalities would be

\[
\begin{array}{c|ccccc}
m&4&5&6&7&8\\ \hline
d&2&2&3&3&3\\
C_m-2^d&10&38&124&421&1422,
\end{array}                                                       \tag{3.6}
\]

but none of these five deep-casualty totals is a proved fixture datum.

There is also a non-scalar obstruction.  The canonical fixed segmentation
has `322` cut rank-ten colours with no extendable ordinary seam provider.
More strongly, after ranging over all `8894` componentwise minimum patterns,
every global `1419`-cut choice still contains at least fourteen unsupported
selected colours in the complete option-conditioned one-seam relaxation.
Therefore no ordinary endpoint-seam braid of unchanged minimum fragments can
be upper-`q1` complete, regardless of the favourable count in (3.1).  This
does not cover an interior rethread or a compound resident seam module.

## 4. Closed recut/augmenter packets

Let \(Z\) be a bank of currently unsupported target colours and let
\(\mathcal S\) be a bank of physical repair sites in the original SCD
chains.
A **closed depth-`d` repair packet** `gamma(z,s)` consists of a completely
specified local replacement at site `s` for target `z`, with the following
literal certificate.

1. **Bounded recut.**  It uses a declared bounded number of extra cuts
   (two in a two-cut packet) and a bounded owner/edge support.
2. **One-copy algebra.**  Every old owner is retained exactly once; `z` is
   newly supplied; every deleted lower and immediate-upper colour is either
   restored inside the packet or named as a child demand.  A *closed*
   packet recursively services all such children within the same site.
3. **Residence transition.**  Its internal word is valid and its exact
   capped input/output age transition is declared.  If it is advertised as
   boundary-neutral, that transition equals the transition of the block it
   replaces on every legal incoming state.
4. **Deck transparency.**  Its internal, prefix, suffix and total OR decks
   contain the corresponding old decks needed by every exterior context,
   or every exception is an explicit occurrence-labelled child ticket
   closed inside the packet.
5. **Root and topology.**  Its `M_0` roots, endpoint owners and direction are
   literal.  It either has the same external endpoints as the replaced block
   or carries the exact quotient edge and potential certificate used by the
   global forest.
6. **Complete footprint.**  Every lower, owner-slot, head, tail, guard,
   compiler and protected resource used by the replacement or its child
   closure is listed in one physical footprint.

For the functional-slot interface below, `z` is the packet's one **primary**
target in `Z`.  Any other member of `Z` supplied incidentally is not credited
to this packet.  If one wants to credit a packet for several primary targets,
the task side becomes a set-cover hyperedge and Theorem 5.1 is no longer the
exact formulation.

The tight one-to-two Boolean-diamond augmenter and the resident facet socket
are examples of local algebra from which such packets may be built.  Their
local theorems alone do not imply Items 3--6 after placement in an SCD host.

Call a packet atlas **functional by site** when the following factorization
is part of its certificate.

* The target labels and the physical sites are both capacity-one resources.
* After the fixed protected bank is contracted and the target label `z` is
  removed from the footprint of `gamma(z,s)`, all remaining capacity
  resources of that packet lie in a site block `R_s`; the blocks `R_s` are
  pairwise disjoint.
* For every partial injection from targets to sites, the corresponding
  boundary transitions, deck maps, fixed-`M_0` roots and quotient edges
  commute and are jointly valid.  In particular, their quotient support is
  already certified to be a linear forest (for example by endpoint
  neutrality, by direct graphic independence, or by a fixed common potential
  together with quotient indegree at most one and physical maximum degree
  at most two).  A common potential plus the physical degree bound alone is
  not enough: an acyclic orientation of a triangle has both properties while
  its undirected support is cyclic.

The second bullet is deliberately stated after deleting the target label:
two alternative packets for the same target necessarily share that target
resource.  The definition only asserts disjointness for the site-controlled
resources of packets that can occur together.

These hypotheses are deliberately stronger than pairwise endpoint legality.
They are the exact conditions that collapse the physical repair problem to
ordinary matching.

## 5. Exact bounded-defect local-to-global theorem

Form the bipartite graph

\[
                 G_{\rm cl}=(Z,\mathcal S;E),\qquad
 z\sim s\Longleftrightarrow
 \text{a closed functional packet }\gamma(z,s)\text{ exists}.    \tag{5.1}
\]

### Theorem 5.1 (functional-slot repair and exact defect)

Assume the packet atlas is functional by site.  A target family
\(Z'\subseteq Z\) is simultaneously repairable by assigning one closed
packet to each of its primary targets if and only if it is matchable into
\(\mathcal S\) in \(G_{\rm cl}\).  Consequently the minimum number of
unrepaired primary targets in this construction class is exactly

\[
 \boxed{
   \delta(G_{\rm cl})=
     \max_{X\subseteq Z}\bigl(|X|-|N(X)|\bigr). }                 \tag{5.2}
\]

In particular, all but at most `b` targets are repairable if and only if

\[
                         |N(X)|\ge |X|-b
                         \qquad(X\subseteq Z).                    \tag{5.3}
\]

#### Proof

A matching chooses at most one packet per site.  Functional-site
disjointness and commuting closure make the corresponding local
replacements simultaneous, proving sufficiency.  Conversely, any repair in
this construction class assigns distinct physical sites to its target
packets and hence records a matching.  The defect form of Hall's theorem
gives (5.2)--(5.3).  \(\square\)

### Corollary 5.2 (a checkable degree/load sufficient condition)

Suppose an exceptional target bank `E_0` has size at most `b`.  If for some
integer `L>=1`

\[
 \deg(z)\ge L\quad(z\in Z\setminus E_0),
 \qquad
 \deg(s)\le L\quad(s\in\mathcal S),                              \tag{5.4}
\]

then all targets outside `E_0` have simultaneous closed repairs; hence the
global defect is at most `b`.

If a protected bank deletes at most `p` sites, it is enough before deletion
to replace the first bound in (5.4) by `deg(z)>=L+p`.

#### Proof

For every \(X\subseteq Z\setminus E_0\), double counting incidences gives

\[
                  L|X|\le e(X,N(X))\le L|N(X)|.
\]

Thus Hall holds on `Z-E_0`.  Removing `p` sites lowers every target degree
by at most `p`, giving the robust version.  \(\square\)

### Proposition 5.3 (singleton support has no bounded-defect consequence)

For every `n`, there is a functional-site incidence graph in which all `n`
targets have a local packet but every simultaneous repair covers at most
one target.

#### Proof

Take one site adjacent to all `n` targets.  Every target has singleton
support, while (5.2) gives defect `n-1`.  \(\square\)

### Theorem 5.4 (exact two-cut packet defect with a graphic oracle)

Let `F` be the current physical SCD forest and let `\mathcal S_2` be a bank
of physical SCD windows.  A packet at a site
in `\mathcal S_2` makes at most the two declared boundary cuts and is closed
in the one-copy, residence, deck, root and protected-resource senses of
Section 4.  Assume packets chosen at different sites have disjoint complete
non-topological footprints, but do **not** assume that their physical edge
switches are jointly acyclic.

Let `\widetilde G_2` be the bipartite packet multigraph with one labelled
edge `\gamma(z,s)` for every such closed packet; parallel target--site edges
are retained because their physical switches may differ.  A packet matching
uses at most one edge at each target and each site.

For a packet `\gamma`, let `D_\gamma` be its deleted physical edge bank and
`N_\gamma` its new physical edge bank.  For a packet matching `M` in
`\widetilde G_2`, put

\[
 F_M=\left(F-\bigcup_{\gamma\in M}D_\gamma\right)
                  \cup\bigcup_{\gamma\in M}N_\gamma.             \tag{5.5}
\]

Then the packets of `M` are simultaneously valid and have a physical linear
forest exactly when

\[
 \deg_{F_M}(v)\le2\quad(v\in\mathcal O),
 \qquad
 |E_{F_M}(Y)|\le |Y|-1
       \quad(\varnothing\ne Y\subseteq\mathcal O).               \tag{5.6}
\]

Consequently the exact two-cut defect in this atlas is

\[
 |Z|-\max\{|M|:M\text{ is a packet matching satisfying }(5.6)\}.
                                                                    \tag{5.7}
\]

Every matching of size `q` in (5.7) uses at most `2q` new cuts.  If, after
deleting all site edge banks and contracting the retained background, every
choice of at most one packet per site is degree-safe and graphic-independent,
then (5.6) is automatic and (5.7) reduces exactly to the defect-Hall formula
(5.2).  A checkable stronger sufficient condition is that every target
filling at a fixed site has one fixed quotient-edge signature and the union
of those signatures over the whole site bank is degree-safe and a forest.

#### Proof

Matching is exactly the primary-target and site-capacity row.  Closure and
disjoint non-topological footprints make all other declared local resources
simultaneous.  The remaining physical support is literally (5.5).  A graph
is a linear forest exactly when it has maximum degree at most two and its
edge set is graphic-independent, equivalently the subset inequalities in
(5.6).  Maximizing the number of selected primary targets proves (5.7).
The final assertion makes the graphic test true for every site matching, so
Theorem 5.1 applies. \(\square\)

The degree-plus-graphic row in (5.6) is not itself a matroid.  On vertices
`1,...,5`, both

\[
 A=\{12,23,34\},\qquad B=\{25,12,13,34\}
\]

are linear forests and `|A|<|B|`, but adding `25` to `A` gives degree three
at vertex `2`, while adding `13` gives a triangle.  Thus no member of `B-A`
augments `A`.  This exchange failure already occurs before lower, owner-slot,
ticket and residence resources are added.

This star is the sharp reason that the requested theorem needs a load,
expansion or defect-Hall hypothesis.  Polynomial raw augmenter supply is
irrelevant unless the candidates are active in the current forest and their
complete footprints satisfy the functional-site condition.

### Theorem 5.5 (bounded-radius alternating packet repair)

Let `M` be any matching of `G_cl`.  A closed alternating repair of radius
`q` is a simple path

\[
 z_0,s_0,z_1,s_1,\ldots,z_q,s_q                         \tag{5.8}
\]

such that `z_0` is unmatched by `M`, every `z_i s_i` is an edge of
`G_cl`,

\[
                         M(s_i)=z_{i+1}\qquad(0\le i<q), \tag{5.9}
\]

and `s_q` is unmatched.  Toggling the alternating path replaces `q` old
packets by `q+1` new packets, preserves every already repaired target, and
decreases the defect by one.

Fix integers `b,r>=0`.  Suppose that every matching `M` with more than `b`
unmatched targets has a closed alternating repair (5.8) with `q<=r`.
Then, from any initial functional packet family, repeated local toggles
produce a simultaneous repair with defect at most `b`.  Every toggle changes
at most `2r+1` packet columns.  Hence, if one packet column has support at
most `sigma` and names at most `c` cut positions, one toggle has changed
support at most `(2r+1)sigma` and a changed-cut ledger of size at most
`(2r+1)c`.

Equivalently, let `U_M` be the unmatched target bank and define its
alternating closure by

\[
 X_0=U_M,\qquad
 X_{i+1}=U_M\mathbin\cup M(N(X_i)).                       \tag{5.10}
\]

Here `M(N(X_i))` is the set of target partners of the matched sites in
`N(X_i)`.  The radius-`r` hypothesis is exactly

\[
 N(X_r)\cap(\mathcal S\setminus V(M))\ne\varnothing
 \quad\hbox{whenever }|U_M|>b.                            \tag{5.11}
\]

#### Proof

The symmetric difference of `M` with (5.8) is a matching of size
`|M|+1`.  Functional-site factorization turns that matching into a jointly
valid packet family; its altered columns are the `q` deleted and `q+1`
inserted edges.  Repeating terminates after at most `|Z|` toggles with at
most `b` unmatched targets.  The support bounds follow by taking the union
of the altered packet ledgers.  Finally, breadth-first alternating search
from `U_M` has target layers (5.10); it reaches a free site by depth `r`
exactly when (5.11) holds.  \(\square\)

For a closed two-cut atlas, take `c=2`: each bounded-radius toggle changes
at most `4r+2` named cut positions and at most `(2r+1)sigma` packet-support
units.  This is a per-toggle bound; the union of all sites visited during a
long repair sequence may be much larger.

Without a uniform radius, Theorem 5.1 is recovered from the ordinary
augmenting-path lemma: defect Hall at most `b` says that any matching with
larger defect is nonmaximum and therefore has some alternating repair.  A
bounded radius is an additional expansion assertion, not a consequence of
Hall or of two-cut locality.

### Proposition 5.6 (two-cut locality does not bound exchange radius)

For every `n`, there is a functional packet graph with a perfect matching
and a matching of defect one whose unique augmenting path changes `2n-1`
packet columns.

#### Proof

Take targets `z_1,...,z_n`, sites `s_1,...,s_n`, and edges

\[
 z_i s_i\ (1\le i\le n),\qquad
 z_{i+1}s_i\ (1\le i<n).                               \tag{5.12}
\]

The diagonal edges form a perfect matching.  From
`M={z_(i+1)s_i:1<=i<n}`, however, `z_1` and `s_n` are the only free
vertices and the unique augmenting path is

\[
 z_1,s_1,z_2,s_2,\ldots,z_n,s_n.                       \tag{5.13}
\]

Thus even if every edge of (5.12) is represented by a closed two-cut packet,
one local edge per target and global matchability do not give an
`O(1)`-support repair sequence.  \(\square\)

If footprints at distinct sites still cross in owner, lower, head, guard or
graphic resources, (5.1) is not the right graph.  The object is then a
coloured hypermatching plus a graphic row.  It must be stated that way; it
cannot be replaced by a generic matroid claim.

## 6. Protected sidecar connector theorem

The favourable scalar `P-H=b` has one exact possible interpretation, but
only on a stronger ticket-functional face.  Suppose `b` pieces form a
prescribed protected directed path using `b-1` certified internal arcs.
After contracting it, there are `P-b+1` components and hence exactly `P-b`
remaining connector tasks in a Hamilton completion.

Assume the pre-sidecar pieces are lower-clean, so their raw missing-lower
bank has size `P`, and the sidecar arcs use `b-1` distinct members of this
bank.  The exact residual bank then has size `P-b+1`; assign its members
bijectively as source-private tokens `a_K` to the contracted components
`K`.  Fix one physical orientation and one exported boundary-state sheet
for every contracted component before forming any connector menu.

Let \(\mathcal H_D^S\) be the complete upper-hole bank remaining after the
sidecar is installed.  If

\[
                         |\mathcal H_D^S|\le P-b,                  \tag{6.1}
\]

assign its members injectively to the `P-b` connector tasks and pad unused
tasks by dummy tickets.  Declare one contracted component \(K_\dagger\) to
be the global terminal and one component \(K_*\) to be the global root,
distinct when there is more than one component.  For each
\(K\ne K_\dagger\), let
\(\mathcal A_K\) be the menu of **sealed connector columns** which:

1. add exactly one Johnson seam from the terminal owner of `K`, use exactly
   its source-private lower token `a_K`, and consume no extra owner or
   missing-lower token;
2. enter a component different from `K_*` and use its fixed incoming owner
   and orientation sheet;
3. realize the upper ticket assigned to `K` by a literal interval occurrence
   lying inside the fixed column word; a longer occurrence is allowed only
   when its whole ordered segment was contracted as one compound column;
4. carry an accepting boundary-age transition and every named guard; and
5. strictly increase one common component potential.

Assume all non-head resources in different columns are private by task, so
the only shared capacity is the chosen incoming component.  The outgoing
task bank \(K\ne K_\dagger\) and admissible incoming bank \(J\ne K_*\)
both have size \(P-b\).
Write \(N(K)\) for the set of incoming components represented in
\(\mathcal A_K\).

### Theorem 6.1 (ticket-aligned protected Hamilton completion)

Under the preceding assumptions, a resident, lower-q1-injective,
upper-complete Hamilton owner path containing the prescribed `b`-piece
sidecar exists within the declared sealed-column class if and only if

\[
                  \left|\bigcup_{K\in X}N(K)\right|\ge |X|
                  \qquad\text{for every connector-task family }X. \tag{6.2}
\]

It uses every missing lower colour except the declared global terminal.

#### Proof

Hall selects distinct incoming component slots, one for every nonterminal
outgoing task.  The fixed sheets make the incoming and outgoing uses of a
component physically consistent.  The lower colours are distinct because
they are the tasks' source-private tokens.  Every selected arc increases
the common potential, so the indegree/outdegree-one component graph has no
directed cycle.  With `P-b+1` contracted vertices and `P-b` arcs it is one
Hamilton path from \(K_*\) to \(K_\dagger\).  The sealed columns give residence
and every assigned upper ticket; the protected path supplies its contracted
internal arcs.  Its `b-1` joins and the `P-b` Hall joins use `P-1` distinct
members of the raw missing-lower bank, leaving exactly \(a_{K_\dagger}\) for
the terminal compiler.  Conversely, any completion in this class assigns
different incoming components to all outgoing tasks and therefore records
a matching saturating the task bank; Hall necessity gives (6.2).
\(\square\)

For the canonical raw `k=17` segmentation, before any hypothetical sidecar
is installed, `b=8` makes

\[
                         H=P-b=6273.                            \tag{6.3}
\]

Thus the arithmetic is exactly square for Theorem 6.1: after an eight-piece
sidecar is contracted, there is one upper ticket per remaining connector
task.  This does **not** instantiate the theorem.  The actual protected
packet/banks are not proved to occupy eight resident SCD pieces, the 6,273
arbitrary-width targets are not sealed one per connector column, and the
canonical bank already has 322 rank-ten zero providers.  The alternate
minimum cutting (3.3) also shows that the square depends on the cut choice.

## 7. Asymptotic target

Suppose a protected SCD selector supplies a central coherent forest and a
recut/repair system with:

\[
 t=O(C_md),\qquad |\mathcal H_D|=O(C_md),\qquad
 bL_m=o(W_m),                                             \tag{7.1}
\]

where \(L_m\) bounds the owner support of one sidecar piece.  Suppose
Theorem 5.1 reduces the local zero-provider bank to that sidecar while
Theorem 6.1 joins the final pieces.  If every selected repair uses `O(1)`
amortized new protected support, the complete reserved support is

\[
                         O(C_md)+O(bL_m)+O(d),                  \tag{7.2}
\]

and therefore

\[
 {O(C_md)\over W_m}=O\!\left({d\over m}\right)=o(1)
                         \qquad(d=o(m)).                         \tag{7.3}
\]

At the intended `d=Theta(sqrt(m))`, the first term is
`O(W_m/sqrt(m))`.  For the formal specialization \(b=2^d\), a polynomial
\(L_m\) still gives \(bL_m=o(W_m)\); this is only a capacity statement and
does not construct the sidecar.

The scalar lower compiler still requires

\[
                         P\le\Delta_{2m-1},                       \tag{7.4}
\]

where `Delta` is the exact omission allowance of the lower-bound ledger.
Neither (7.1) nor (7.3) implies (7.4) in every dimension.  More importantly,
the common source/cap compiler, fixed-`M_0` head correlation, arbitrary
exterior witnesses and hereditary regeneration remain separate from the
functional-slot theorems above.

## 8. Relation to frozen notes

The coherent central normal form and conditional braid are from
`MATH_THEOREM_AD_REGENERATIVE_SCD_CATALAN_BRAID_STATE_AND_SHADOW_CAP_GATES_20260801.md`.
The canonical `6281`-piece boundary monoid and `6273`-hole ledger are in
`MATH_AUDIT_A_K17_SCD_6281_PIECE_BOUNDARY_AND_POSTCUT_UPPER_LEDGER_20260801.md`
and
`MATH_AUDIT_THREAD_A_K17_SCD_RESIDENT_PIECES_ALLINTERVAL_UPPER_GATE_20260801.md`.
The alternate-minimum and compact-socket upper ledgers are in
`MATH_THEOREM_K17_SCD_COMPACT_SOCKET_BANK_AND_UPPER_CASUALTY_LEDGER_20260801.md`.
The complete minimum-face rank-ten obstruction and the two refinement rows
in (3.5) are in
`MATH_AUDIT_A_K17_M9_MINCUT_FACET_RAIL_AND_COMPOUND_FRAGMENTATION_GATE_20260801.md`.
The exact flexible-cut transition system is
`MATH_AUDIT_A_K17_M9_CUTFLEX_PATTERNED_SEAM_FLOW_20260801.md`.
The tight local augmenter algebra and its true simultaneous resource/graphic
conditions are
`MATH_THEOREM_ODD_DIAMOND_TIGHT_ONE_TO_TWO_AUGMENTER_20260801.md` and
`MATH_AUDIT_K_ODD_DIAMOND_ONE_TO_TWO_AUGMENTER_AND_RESOLUTION_GATE_20260801.md`.
The SCD-specific paired-ear grammar and its square-SDR gate are
`MATH_THEOREM_SCD_SHORT_TRIANGLE_AUGMENTER_EAR_GRAMMAR_20260801.md` and
`MATH_THEOREM_THREAD_D_SCD_SHORT_BOUNDARY_CAPACITY_TWO_AND_PAIRED_EAR_GATE_20260801.md`.

No compiler/lower-cap, arbitrary-exterior, recursive-ear or all-`m`
conclusion beyond the displayed conditional statements is intended.
