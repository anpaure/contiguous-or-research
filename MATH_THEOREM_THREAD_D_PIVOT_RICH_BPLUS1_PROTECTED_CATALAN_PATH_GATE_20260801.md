# The pivot-rich `B+1` gate is a protected Catalan port Hamilton path, not a cycle completion

Date: 2026-08-01  
Lane: Thread D, protected `B+1` owner path  
Status: exact protected-seed and port-path reduction, plus unconditional
protected upper-colour/root-tail Hall extension.  Simultaneous other-head
injectivity and the spanning link tree, the nonflat source antecedent, higher
upper deck, residence outside the packets, and common compiler cap remain
unproved.

## 0. Verdict

Let `ML_m` be the incidence graph between

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal O={ [2m-1]\choose m},
\]

and write

\[
 W=|\mathcal L|=|\mathcal O|,qquad
 U={2m-1\choose m+1},qquad
 C=W-U=\operatorname {Cat}_m.                           \tag{0.1}
\]

The correct owner-layer target for `B+1` is not a two-factor followed by a
closure.  It is

\[
 \boxed{M_0\text{ perfect},\quad Q\text{ a matching of size }W-1,
 \quad \operatorname{up}_{M_0}(Q)=\mathcal U,
 \quad \lambda_{M_0}(Q)\text{ a spanning tree}.}       \tag{0.2}
\]

Then `M_0 union Q` is one alternating Hamilton path on all `2W` incidence
vertices.  Its owner projection contains every rank-`m` owner once, every
immediate-upper colour at least once, and all but one immediate-lower colour.
The missing lower colour is the forced path-boundary sidecar.

Selecting one occurrence of each upper colour decomposes (0.2) exactly as

\[
               Q=Q_0\mathbin{\dot\cup}Q_1,qquad
               |Q_0|=U,qquad |Q_1|=C-1,               \tag{0.3}
\]

where `Q_0` is an upper-exact rooted Catalan forest and the contracted links
of `Q_1` form a tree.  Since `Q_1` is a matching on the unique unused ports
of the `C` directed-path components of `Q_0`, that contracted tree is in
fact one directed Hamilton path.  There is no residual matching and no
closure edge.

For `H` resource-disjoint pivot-rich packets, the alternating second-shore
half `P_1` of their incidence lifts is always independent in the two
endpoint partitions and the rooted-link graphic matroid: its links form `H`
disjoint directed paths.  Immediate-upper colours are distinct inside each
packet, but the authoritative resource-disjointness hypothesis does not
separate upper colours between different packets.  The lossless protected
decomposition therefore chooses

\[
                         P_1=A_0\mathbin{\dot\cup}A_1,   \tag{0.4}
\]

puts an upper-independent `A_0` into `Q_0`, and forces `A_1` into the
`C-1`-connector path `Q_1`.  If the packets satisfy the additional
**upper-resource-disjoint** condition, one may take `A_0=P_1,A_1=empty`;
that clean four-matroid contraction is only a sufficient specialization.

Thus the exact protected existence gate is a jointly selected rooted
Catalan forest and directed Hamilton path in its physical port digraph.  The
local packet theorem removes the local endpoint/graphic obstruction but does
not close the global correlation.

There is one further unconditional gain.  The central shadow inequality

\[
 |\partial\mathcal X|\ge |\mathcal X|+m                 \tag{0.5}
\]

for nonempty families of rank-`m+1` sets implies that any at most `m`
prescribed distinct upper-colour/root-tail tickets extend to a complete
upper-tail injection.  Hence every upper-independent protected subbank
`A_0` passes this Hall row when `|A_0|<=m`; under the stronger
upper-resource-disjoint hypothesis all `3Hh` tickets do so whenever
`3Hh<=m`, automatically under `6Hh<=m-2`.  The open correlation is the
simultaneous injectivity of the other middle corners and the spanning
rooted-link tree containing `A_1`.

Finally, the physical source must be counted correctly.  The target is a
jointly designed final depth-`h` chronology with `W+1` cells: `W` owner
cells governed by (0.2) and one controlled nonowner/boundary cell.  The
pivot replaces a nonflat rank-`m+1` crossing scaffold by new rank-`m`
owners.  It is not an insertion into a pre-existing flat `W`-owner factor.

## 1. The protected pivot seed

Let one pivot-rich owner path be

\[
 V_0,V_1,\ldots,V_\ell,qquad \ell=3h,                 \tag{1.1}
\]

with

\[
 L_i=V_i\cap V_{i+1},\qquad R_i=V_i\cup V_{i+1}
                   \quad(0\le i<\ell).                \tag{1.2}
\]

The pivot-rich theorem gives pairwise-distinct `L_i` and pairwise-distinct
`R_i` within one packet.  Resource-disjoint copies make the owner and lower
banks globally distinct, but do not by themselves make the `R_i` globally
distinct.  The incidence lift is

\[
       V_0,L_0,V_1,L_1,\ldots,L_{\ell-1},V_\ell.       \tag{1.3}
\]

Properly alternate its edges into `P_0,P_1`.  For a disconnected protected
bank this colouring is existentially quantified component by component; a
fixed arbitrary set of phases need not agree with the one global Hamilton
alternation.  The phase may be selected after the eventual alternating host
is chosen.  If `M_0` is a perfect
matching containing `P_0`, define for `e=LV notin M_0`

\[
 \operatorname{up}_{M_0}(e)=M_0(L)\cup V,qquad
 \lambda_{M_0}(e)=L\longrightarrow M_0^{-1}(V).        \tag{1.4}
\]

### Theorem 1.1 (protected endpoint/graphic seed)

For `H` resource-disjoint pivot-rich paths, `P_1` has size `3Hh`, its rooted
links form `H` vertex-disjoint directed paths, and it is independent in the
lower-tail partition matroid, owner-head partition matroid, and rooted-link
graphic matroid.  Its upper map is injective on each packet.  It is globally
upper-independent exactly when no two packets use the same `R_i` colour.

#### Proof

Suppose first that `M_0(L_i)=V_i`.  Then the other protected incidence is
`L_iV_(i+1) in P_1`, and

\[
 \operatorname{up}_{M_0}(L_iV_{i+1})=R_i.              \tag{1.5}
\]

For `i<ell-1`, the next protected `M_0` edge is
`L_(i+1)V_(i+1)`, so

\[
 \lambda_{M_0}(L_iV_{i+1})=L_i\longrightarrow L_{i+1}. \tag{1.6}
\]

The last owner `V_ell` is matched by `M_0` to a lower vertex outside the
protected lower bank, extending (1.6) by one final link.  If the alternating
phase is reversed, the same path runs in the opposite direction.

For different protected paths, internal lower vertices are already occupied
by `P_0`, while perfect-matching injectivity gives distinct external terminal
preimages.  Hence the link paths are vertex-disjoint.  Equation (1.5)
identifies every upper colour; it is injective within a packet, and is
globally injective exactly under the added cross-packet condition.  Matching
and graphic independence are now immediate.  \(\square\)

Under `6Hh<=m-2`, the small protected-factor theorem can be used only as an
auxiliary consistency certificate: it supplies some two-factor containing
the incidence paths, whose alternating colouring supplies a compatible
`M_0` phase.  That auxiliary factor is discarded.  It is not the final
carrier and is not a flat source into which the pivot is inserted.

### Theorem 1.2 (protected upper-colour/root-tail extension)

Fix `M_0`.  Let `t<=m` prescribed tickets be pairs `(R,T)` with distinct
rank-`m+1` colours `R`, distinct rank-`m` rooted tails `T`, and `T subset R`.
They extend to an injection

\[
 \psi:{[2m-1]\choose m+1}\longrightarrow
                 {[2m-1]\choose m},\qquad \psi(R)\subset R.            \tag{1.7}
\]

Relative to `M_0`, (1.7) gives one incidence edge for every upper colour,
retaining every prescribed ticket and using distinct rooted tails.

#### Proof

For every nonempty family `mathcal X` of rank-`m+1` sets, the central
one-step Kruskal--Katona shadow bound is

\[
                         |\partial\mathcal X|
                              \ge|\mathcal X|+m.          \tag{1.8}
\]

Delete the `t` prescribed upper vertices and their `t` prescribed tails.
Every remaining family then has at least

\[
                  |\partial\mathcal X|-t
                     \ge|\mathcal X|+m-t\ge|\mathcal X| \tag{1.9}
\]

available tails.  Hall gives (1.7).

For a selected `(R,T)`, put `L=M_0^{-1}(T)`.  Write
`T=L+{a}` and `R=T+{b}`.  The other middle corner is `V=L+{b}`, and the
incidence `LV` has `up_(M_0)(LV)=R`.  Distinct tails give distinct `L`.
\(\square\)

The theorem deliberately stops at a semimatching.  The other corners `V`
may collide, and even a head-injective choice may branch or cycle in the
rooted-link graph.  It closes the upper/tail projection of the protected
system, not the remaining head/tree correlation.  Apply it to an
upper-independent subbank `A_0`; under added upper-resource-disjointness one
may take all `3Hh` pivot tickets.

## 2. Exact protected Catalan decomposition

Fix `M_0` containing `P_0`.  On `E(ML_m)-M_0` use the four matroids

* `mathsf M_L`: at most one edge at each lower vertex;
* `mathsf M_O`: at most one edge at each owner;
* `mathsf M_U`: at most one edge of each value `up_(M_0)`; and
* `mathsf M_G`: the cycle matroid of the labelled rooted links.

### Theorem 2.1 (protected upper-representative extension)

Let `A_0 subseteq P_1` have distinct upper colours.  There is a rooted
Catalan forest `Q_0` containing `A_0` if and only if the
four contractions

\[
 \mathsf M_L/A_0,\quad\mathsf M_O/A_0,\quad
 \mathsf M_U/A_0,\quad\mathsf M_G/A_0                  \tag{2.1}
\]

have a common independent set of size

\[
                              U-|A_0|.                  \tag{2.2}
\]

#### Proof

Theorem 1.1 makes every contraction in (2.1) legal.  A common extension of
the displayed size makes `Q_0` a matching of size `U`, uses `U` distinct
upper colours, and has forest links.  Since there are exactly `U` upper
colours, its upper map is a bijection.  Conversely, remove `A_0` from any
such rooted Catalan forest and use the definition of matroid contraction.
\(\square\)

Under upper-resource-disjointness take `A_0=P_1`; otherwise the remaining
`A_1=P_1-A_0` must be selected jointly in the connector bank below.

The forest `lambda(Q_0)` has `W` vertices and `U=W-C` edges, hence exactly
`C` components.  Because it is a directed partial permutation, each
component is a directed path with one unused tail and one unused head.

Define the **physical port digraph** `D(Q_0)` on these components.  Put an
arc `K -> K'` for every incidence edge from the unused lower-tail vertex of
`K` to the owner whose `M_0` preimage is the unused head vertex of `K'`,
after deleting all protected, cap-incompatible, residence-incompatible, or
otherwise forbidden physical incidences.  Retain parallel occurrence labels
when guards distinguish them.

### Theorem 2.2 (the `C-1` connectors are one port Hamilton path)

For a set `Q_1` of physical port incidences, optionally required to contain
the declared bank `A_1`, the following are equivalent.

1. `Q_0 union Q_1` is a matching of size `W-1` and its rooted links form a
   spanning tree.
2. The arcs of `Q_1` form a directed Hamilton path in `D(Q_0)`.

In either case `|Q_1|=C-1`.

#### Proof

Matching compatibility permits at most one selected outgoing and one
selected incoming arc at each contracted component.  Thus selected arcs
form a directed partial permutation.  Their union with the old forest is
connected and acyclic exactly when the contracted arcs form a connected
acyclic graph.  A connected acyclic partial permutation is a directed path
through all `C` vertices, and it has `C-1` arcs.  The converse is immediate.
\(\square\)

### Corollary 2.3 (exact protected `B+1` owner certificate)

The protected Hamilton path exists if and only if one can choose `M_0`, a
partition `P_1=A_0 dotcup A_1` with `A_0` upper-independent, a common
extension `Q_0 superseteq A_0` from Theorem 2.1, and a directed Hamilton
port path `Q_1 superseteq A_1` from Theorem 2.2.  Put
`Q=Q_0 dotcup Q_1`.  Then

\[
 |Q|=U+C-1=W-1,qquad
 \operatorname{up}_{M_0}(Q)=\mathcal U,                 \tag{2.3}
\]

and `M_0 union Q` is one alternating Hamilton path containing every
protected pivot path.

Conversely, from any protected path certificate select one edge of `Q` for
every upper colour.  For a colour carried by one or more protected edges,
select at most one such protected occurrence.  Put
`A_0=P_1 cap Q_0` and `A_1=P_1-Q_0`; the remaining `C-1` edges are `Q_1`.
Hence this partitioned reduction loses no protected solution.  If protected
upper colours are globally distinct, choose every protected occurrence and
recover the sufficient specialization `A_0=P_1`.

There is no residual Hall problem and no closure edge in this theorem.

Equivalently, on the physical incidence-edge ground outside `M_0`, the
union `Q` obeys the common-rank system

\[
 \begin{aligned}
 |Q|&=W-1,\\
 r_{\rm tail}(Q)=r_{\rm head}(Q)&=W-1,\\
 r_{\rm gr}(\lambda(Q))&=W-1,\\
 r_{\rm up}(Q)&=U,\\
 P_1&\subseteq Q,
 \end{aligned}                                         \tag{2.4}
\]

for some compatible componentwise alternating colouring of `P`.  The upper
row is a rank condition, not upper-partition independence of all `Q`, since
the `C-1` connector edges may repeat colours already represented by `Q_0`.

Let `h_*` be the unique unused incoming/head port of the directed link path
and `t_*` its unique unused outgoing/tail port.  The owner order starts at
`M_0(h_*)` and ends at `M_0(t_*)`; the unique missing lower colour is
`t_*`.  Prescribing the two physical endpoint types is therefore part of
the port-Hamilton problem, not a later residual closure.

### Theorem 2.4 (a distinguished packet is a prefix iff its first head is free)

Distinguish one pivot packet and orient it as

\[
 M_0(L_i)=V_i,qquad L_iV_{i+1}\in P_1
                    \quad(0\le i<\ell=3h).             \tag{2.5}
\]

Put `L_out=M_0^{-1}(V_ell)`.  For any protected certificate `Q` containing
these edges, the following are equivalent.

1. The owner Hamilton order begins
   \[
                         V_0,V_1,\ldots,V_\ell.         \tag{2.6}
   \]
2. `V_0` is the unique owner not used as a `Q`-head.
3. `L_0` is the unique indegree-zero vertex of the directed link path
   `lambda_(M_0)(Q)`.

When these conditions hold, the first continuation after the packet is the
unique `Q`-edge with tail `L_out`.  Requiring that edge to belong to a
declared exported-state menu is the complete right-interface guard.

#### Proof

The protected links forced by (2.5) are

\[
 L_0\longrightarrow L_1\longrightarrow\cdots
 \longrightarrow L_{\ell-1}\longrightarrow L_{out}.   \tag{2.7}
\]

The owner `V_0=M_0(L_0)` is a `Q`-head exactly when some rooted link enters
`L_0`.  Thus items 2 and 3 are equivalent.  A spanning directed link path
whose initial vertex is `L_0` must begin with the already forced chain
(2.7), because every internal in/out port on that chain is occupied.
Expanding the `M_0` edges gives (2.6).  Conversely (2.6) makes `V_0` the
owner-shore endpoint of the alternating incidence path, so no `Q` edge has
that head.  At `L_out` the incoming protected link is occupied and the
unique unused outgoing port gives the asserted continuation.  \(\square\)

In the two-stage decomposition, select every upper occurrence of the
distinguished packet into `Q_0`; its upper colours are distinct internally,
and conflicting occurrences from other packets may instead enter `A_1`.
Then (2.7) lies in one rooted-Catalan component.  The prefix condition says
that this component has unused head `L_0` and that the contracted port
Hamilton path starts there.  Thus prefixing adds a prescribed root and one
right-continuation guard, not another residual matching or closure.

## 3. Flow-checkable sufficient form and sharp obstruction

If `D_f subseteq D(Q_0)` is acyclic, split its vertices into tail and head
copies and let `B_f` be its bipartite arc graph.  Then

\[
                           \nu(B_f)\ge C-1               \tag{3.1}
\]

is sufficient for a protected port Hamilton path: a matching of size
`C-1` selects a partial permutation with one path component, and acyclicity
excludes directed cycles.  Equivalently its Hall deficiency is at most one.

Neither ordinary connectivity nor a size-`C-1` matching in the unrestricted
port graph is sufficient.  A bidirected star is strongly connected but has
path-cover number linear in `C`; and a partial permutation with `C-1` arcs
may consist of one directed path together with directed cycles.  The
acyclicity/tree row is indispensable.

There are also literal incidence obstructions.  The authenticated `m=4`
upper-exact rooted Catalan forest has `C=14` but residual port matching rank
only `11`, below the required `C-1=13`.  A protected finite fixture can force
two different tails to the same head (`50->54` and `52->54`).  Therefore
upper exactness, local palette transparency, and protected edge
disjointness do not imply Theorem 2.2.

Theorem 2.1 is a four-matroid common extension, not ordinary matroid
intersection.  The local determinant-two minor in the ordered-four-
transversal system rules out a raw total-unimodularity shortcut.  These are
scoped obstructions to automatic completion, not an all-dimensional no-go.

## 4. Correct `W+1` depth-row ledger

The pivot has a temporal direction.  Before inserting its source letter
`X`, the `h` crossing length-`h+1` source windows are

\[
                             U_j=M_j\cup M_{j+1},        \tag{4.1}
\]

of rank `m+1`.  After insertion they are replaced by the `h+1` rank-`m`
owners `M_0,...,M_h`.  Thus a flat rank-`m` depth row cannot be preserved
through the insertion.

The direct final `B+1` source target must instead be designed jointly.  The
scalar count gives `W+1` depth cells: `W` selected owner occurrences plus
one surplus occurrence.  In the proposed split-core architecture one adds
the stronger physical requirement that the row is

* `W` rank-`m` owner cells, ordered by the Hamilton path
  `M_0 union Q`; and
* one controlled **boundary** nonowner cell, invisible to the incidence
  path certificate and priced by the single additive source position.

Theorem 2.4 allows the distinguished `3h+1`-owner packet segment to be the
prefix of that owner block.  Placing its source block at the beginning then
turns the left clipped residence flags into true global boundary flags.
Only the `L_out` right-exported state must be continued through the rest of
the Hamilton owner block.

The pre-insertion state is a nonflat scaffold in which (4.1), not the future
owners, occupies the pivot crossing bank.  Therefore none of the following
is legitimate:

1. start with a flat `W`-owner factor and insert `X` while freezing all old
   depth-`h` rows;
2. count the extra depth cell as a repeated owner without checking its
   actual rank and boundary role; or
3. use a residual closure edge to pay that cell.

In the direct certificate this cell is required to attach at the `t_*` end
and literally realize the missing lower colour in the same common-cap
state.  Placement and counting alone do not prove that service.  Placing it in the interior would replace or
bypass one `Q` transition; that is a different certificate and needs two
new mixed-transition rows.  It cannot preserve literal consecutiveness of
the neighboring owners.

The owner path theorem controls only the `W` owner cells.  It neither proves
from counting that the surplus is a nonowner nor supplies its target value.
A physical
`B+1` theorem must additionally produce the nonflat antecedent, the one
nonowner cell, the literal pivot source letters and caps, and the forced
boundary lower target.

## 5. Immediate and arbitrary-width upper scope

The certificate has zero immediate-upper holes because `Q_0` itself uses
one occurrence of every rank-`m+1` colour.  It is already a path, so there
is no cycle opening and no opening damage.  The one missing transition is
on the immediate-lower side.

The local pivot insertion preserves every old contiguous-union occurrence
at every width.  This guarantees zero packet-local arbitrary-upper damage
inside a jointly constructed source.  It does not prove that the ambient
nonflat scaffold initially covers every upper target, nor that the final
source antecedent and common cap exist.  Those are global source rows, not
consequences of (2.3).

## 6. Exact remaining theorem

The weakest owner-layer statement still missing is:

> **Protected Catalan port-Hamilton theorem.**  For every fixed bank of
> resource-disjoint pivot-rich paths in sufficiently large dimension, choose
> a compatible `M_0` and a partition `P_1=A_0 dotcup A_1`; start from the
> guaranteed upper-tail semimatching extending `A_0`, reselect it so the
> other heads are injective and its links form an upper-exact rooted Catalan
> forest `Q_0`; and find a physical directed Hamilton path through the `C`
> component ports which contains `A_1` and has the prescribed `(h_*,t_*)`
> boundary types.

For the split-core placement, strengthen this only by choosing one
distinguished packet with `h_*=L_0`, forcing its rooted component to be the
first component of the port Hamilton path, and restricting the first
post-packet edge at `L_out` to the exported-state menu.  Theorem 2.4 proves
that these conditions are necessary and sufficient for the packet owner
segment to be the literal Hamilton-path prefix.  They do not prove that the
rooted global connector exists.

This would solve owner completeness, lower-`q1` up to the one forced
boundary colour, immediate-upper completeness, topology, and containment of
all protected packets.  It is strictly weaker than the earlier
upper-surjective bounded-component two-factor theorem because it has no
residual matching and no closure.

It still would not by itself prove `B(k)+1`.  The source-level theorem must
simultaneously construct:

1. the `W+1`-cell nonflat depth chronology with exactly one controlled
   nonowner cell;
2. residence on the ambient portions and at the packet interfaces;
3. all arbitrary-width upper witnesses; and
4. one literal common lower-compiler cap, including the boundary colour.

The pivot-rich packet is now fully compatible with this interface.  The
unproved part is global integral correlation plus the nonflat source
antecedent, not another local packet lemma.

For `H>=1`, the clipped residence flags leave between `2H-2` and `2H` packet ends needing
ambient continuation.  The lower bound is attained only when both
global path endpoints are chosen to be packet collar ends; endpoint type is
therefore coupled to the port-Hamilton selection.

## 7. Dependency scope

The proof uses:

* the local path and zero-damage statements in
  `MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`;
* the auxiliary small protected-factor theorem only to certify an admissible
  alternating `M_0` phase under `6Hh<=m-2`; and
* the unprotected path equivalence in
  `MATH_THEOREM_BPLUS1_CATALAN_HAMILTON_PATH_CERTIFICATE_20260801.md`.

The protected upper-tail Hall step is reproved in Theorem 1.2 and agrees
with `MATH_THEOREM_PROTECTED_UPPER_EXACT_HAMILTON_PATH_AND_ROOTED_TAIL_EXTENSION_20260801.md`.

It imports no residual closure, Hamilton-cycle extension, arbitrary-width
upper completion, residence extension, or common-cap theorem.
