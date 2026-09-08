# Fixed-`z` far-socket aperture cycle and the exact corridor-fibre gate

**Date:** 2026-08-02  
**Lane:** A, history/topology completion of the fixed-`z` two-bank atlas  
**Status:** unconditional local fourteen-socket closure, exact zero relative
displacement, and bounded-load avoidance.  A saturated local cycle is not a
spanning host.  The final two-socket ambient corridor and its downstream
upper/source/compiler rows remain separate.

## 0. Result and scope

The fourteen far sockets of the fixed-`z` two-bank packet have a uniform
literal completion.  Seven additional task-private aperture coordinates
give seven pairwise-disjoint Johnson paths

\[
                 x_{i,d}\longrightarrow y_{i+1,d}
                 \qquad(i\in\mathbb Z/7\mathbb Z),       \tag{0.1}
\]

each of length `2d+4`.  Together with the packet rows and the fourteen
monotone rays, they form one simple co-oriented old cycle.  The fixed-`z`
switch makes the new traversal advance by two packet blocks, so it is again
one cycle.  Both cycles are depth-`d` biresident, have identical lower and
immediate-upper palette multisets, and have exactly the same quotient
voltage.  In the canonical fixed-phase realization that voltage is zero.

The complete cycle has `28d+35` projected Johnson edges, hence `56d+70`
incidence edges.  It is therefore an `O(d)` protected bank.  In the
Middle-Levels specialization `k=2r-1`, when `56d+70<=r-2`, the small
protected-factor theorem embeds it in an `ML_r` two-factor.  Because every
vertex of the protected cycle is already
saturated, that embedding leaves it as a separate component.  Thus this is
an unconditional local history/topology theorem, not a global Hamilton-host
theorem.

Deleting any one of the seven new exterior paths from both phases instead
gives paired old/new protected paths with the same two exposed sockets.
Their retained connector/ray parts agree, but their central packet rows do
not.  A single ambient co-oriented corridor can then close or splice both.
The exact
corridor and voltage-fibre conditions are stated in Sections 7--8.

## 1. Input packet and aperture labels

Use the notation and hypotheses of
`MATH_THEOREM_A_FIXED_Z_TWO_BANK_DECODABLE_HISTORY_COLLAR_AND_BOUNDED_LOAD_SUBATLAS_20260802.md`.
Thus `X` has rank `r`, `a in X`, the ordered deletion banks
`D^x,D^y subset X-{a}` and marker banks `M^x,M^y subset [k]-X` are
pairwise disjoint and each has size `d`, and

\[
 H_0=abc, H_1=abp, H_2=apq, H_3=pqs,
 H_4=cps, H_5=cpt, H_6=bct.                            \tag{1.1}
\]

Write

\[
 C=X-\{a,b,c\},\qquad
 G_i=(H_{i+1}\cap H_{i+2})\cup\{z\}.                  \tag{1.2}
\]

For every `i`, the two triples `H_i,G_i` meet in exactly one coordinate.
Choose notation

\[
 H_i=\{\gamma_i,u_i,v_i\},\qquad
 G_i=\{\gamma_i,p_i,q_i\}.                             \tag{1.3}
\]

One literal table is

| `i` | `gamma_i` | `{u_i,v_i}` | `{p_i,q_i}` |
|---:|:---:|:---:|:---:|
|0|`a`|`bc`|`pz`|
|1|`p`|`ab`|`qz`|
|2|`p`|`aq`|`sz`|
|3|`p`|`qs`|`cz`|
|4|`c`|`ps`|`tz`|
|5|`c`|`pt`|`bz`|
|6|`b`|`ct`|`az`|

The order within each displayed two-set may be chosen arbitrarily and then
held fixed.

Choose pairwise-distinct aperture labels

\[
 W=(w_0,\ldots,w_6)                                    \tag{1.4}
\]

outside `X`, the two marker banks, and `{p,q,s,t,z}`.  A convenient
uniform hypothesis is

\[
                 r>=2d+3,\qquad k-r>=2d+12.             \tag{1.5}
\]

When `W` is fixed before the heptagon roles, restrict all five exterior
roles to avoid it.

If additional literal restrictions give connector `i` an allowed aperture
list `A_i`, the exact selection condition inside this template is the
ordinary bipartite Hall system

\[
             \left|\bigcup_{i\in I}A_i\right|\ge |I|
             \qquad(I\subseteq\mathbb Z/7\mathbb Z).   \tag{1.6}
\]

Indeed, an SDR of the seven lists is precisely a choice of pairwise-distinct
`w_i`; the construction below then applies verbatim.  With no extra
restrictions all seven lists are the same pool, and (1.5) gives at least
seven choices.  This solves the local aperture matching.  It is not the
ambient spanning-corridor Hall condition of Section 7.

## 2. The explicit connector paths

Put

\[
                    C_0=C-(D^x\cup D^y).                \tag{2.1}
\]

The far endpoints are

\[
 x_{i,d}=C_0\cup D^y\cup M^x\cup H_i,
 \qquad
 y_{i+1,d}=C_0\cup D^x\cup M^y\cup G_i.                \tag{2.2}
\]

Define `Q_i` from the left endpoint to the right endpoint by the following
ordered exchanges.

1. For `j=1,...,d`, replace `d^y_j` by `m^y_j`.
2. Replace `gamma_i` by `w_i`, then `u_i` by `p_i`.
3. For `j=1,...,d`, replace `m^x_j` by `d^x_j`.
4. Replace `v_i` by `q_i`, then `w_i` by `gamma_i`.

Every line is a Johnson exchange.  After the first bank, the active triple
is `H_i`; after the first two active exchanges it is
`{w_i,p_i,v_i}`; after the second bank and the last two active exchanges it
is `G_i`.  Therefore `Q_i` has the asserted endpoints and length `2d+4`.

### Theorem 2.1 (simple seven-path bank)

The seven `Q_i` are pairwise owner- and facet-disjoint except at no points,
and each meets the packet/ray bank only at its two prescribed endpoints.

#### Proof

During the first bank exchange, the marker/deletion prefix records the
position and the active triple is `H_i`; the seven `H_i` are distinct.
After `w_i` appears, its private label records the path index.  During the
second bank exchange, the same `w_i` record and the opposite bank profile
record the position.  The last endpoint profile is the prescribed `y`-ray
profile.  These signatures also separate the connector states from the
interiors of the original `x`- and `y`-rays.

For facets internal to a bank exchange the same signature argument applies.
The two active facets containing `w_i` are private to path `i`.  The first
and last active facets have active two-sets respectively

\[
 bc,ab,aq,qs,ps,pt,ct                                  \tag{2.3}
\]

and

\[
 pz,qz,sz,cz,tz,bz,az.                                 \tag{2.4}
\]

Each list is injective; the two lists also occur on different bank cores.
Hence no unintended facet equality occurs. \(\square\)

## 3. Exact residence check

### Theorem 3.1 (all connector and junction runs are safe)

In both packet phases, every positive and negative run meeting a connector
or one of its two ray junctions has length at least `d+1`.  No internally
completed short run is created.

#### Proof

The corresponding `M^x_j` insertion and deletion, and the corresponding
`D^x_j` deletion and reinsertion, are separated by

\[
                  (d-j)+d+2+(j-1)=2d+1                 \tag{3.1}
\]

transitions.  A `D^y_j`/`M^y_j` change in the first connector bank and its
inverse change on the reverse `y`-ray are separated by at least `d+4`
transitions (the minimum occurs at `j=d`).

The aperture coordinate `w_i` is inserted before the second active
exchange, remains through all `d` exchanges of the second bank, and is
deleted only after the following active exchange.  Its positive run, and
the simultaneous zero gap of `gamma_i`, therefore span `d+2` transitions.
The labels removed before that bank stay absent through the target ray; the
labels inserted before or after it remain present through that ray.  The
four banks, active labels, and aperture labels are pairwise disjoint, so
there is no cross-identification.  Finally, Theorem 3.1 of the two-bank
note already verifies both old and new central seams. \(\square\)

## 4. Topology and palette identities

Orient the protected old block `B_i` from `y_{i,d}` backwards along its
`y`-ray, through the old row `y_i->x_i`, and forwards along the `x`-ray to
`x_{i,d}`.  Then

\[
 B_0Q_0B_1Q_1\cdots B_6Q_6                              \tag{4.1}
\]

is one simple directed cycle.  In the new phase the packet row is
`y_i->x_{i+1}`.  Following it and then the corresponding connector advances
the block index by two.  Since `gcd(7,2)=1`, the new phase is also one
cycle.

Every connector and ray is identical and co-oriented in the two phases.
The seven central old/new rows have the same facet list and, by the fixed-`z`
identity, the same cap multiset.  Thus the complete cycles have identical
lower-facet and immediate-upper-cap multisets.

Each block has `2d+1` projected edges and each connector has `2d+4`.
Consequently the complete cycle has

\[
                       7(4d+5)=28d+35                  \tag{4.2}
\]

projected edges and `56d+70` incidence edges.

## 5. Exact displacement

The connector paths and all collar rays are retained with the same
orientation.  They therefore cancel from the old/new fragment ledger.  The
old and new fixed-`z` central seam sums agree by cyclic reindexing.  Hence

\[
                   V_{new}-V_{old}=0.                  \tag{5.1}
\]

No voltage pump is required for this local completion.  In the canonical
single-frame construction both cycle voltages are zero.  A separately
protected child-native coprime-voltage pump is still required if the global
developed factor must be connected; (5.1) says that subsequent uses of this
repair do not change that pump's voltage.

## 6. Atlas size, load, and unconditional avoidance

Fix the banks and the seven aperture labels.  The number of role-labelled
packets avoiding them is exactly

\[
 N_{d,W}=(r-1-2d)_2\cdot(k-r-2d-7)_4\cdot(k-r-2d-11)
          =Theta(k^7)                                  \tag{6.1}
\]

in the central regime with `d=o(k)`.

There is one additional private high-load prefix.  On `Q_0`, the first
bank and the exchange `a->w_0` are independent of all seven heptagon roles.
Add the complete occurrence closure of that `O(d)` prefix to the private
root bank.  Outside this enlarged private bank, the marker/bank/aperture
signature determines a connector index and stage, and equality with a fixed
owner, facet, cap, incidence, or history occurrence determines at least one
of the seven role values.  The finite-pattern argument from the central
load theorem therefore gives an absolute `K_1` such that every nonprivate
resource occurs in at most

\[
                              K_1k^6                    \tag{6.2}
\]

completed local cycles.

### Corollary 6.1 (proof-safe forbidden-bank avoidance)

For every forbidden bank `Q` of nonprivate occurrence-labelled socket,
owner, facet, cap, incidence, or history resources,

\[
 |\{T:T\cap Q\ne\varnothing\}|\le K_1|Q|k^6.           \tag{6.3}
\]

In particular `|Q|=o(k)` leaves `Omega(k^7)` completed local tickets.
This is an unconditional local avoidance theorem.  It says nothing about a
prescribed ambient corridor whose resources are not part of these local
tickets.

For every fixed nonprivate socket position `ell` and every ticket subfamily
`A`, the same fibre bound gives the genuine endpoint-spread estimate

\[
       |\{\text{socket profile at }\ell:T\in A\}|
                 \ge {|A|\over K_1k^6}.                \tag{6.4}
\]

In particular the full atlas exposes `Omega(k)` distinct literal profiles
at each nonprivate position.  Equation (6.4) is useful avoidance/expansion,
but it is still a one-position statement and must not be substituted for
the joint ordered-Hall condition below.

## 7. One omitted connector and the exact ambient gate

Delete one `Q_j` from both phase cycles.  Because both full phase graphs are
cycles and contain `Q_j` with the same orientation, each becomes one simple
path with the same two exposed far endpoints.  They are paired old/new
paths, not one identical path, because their central packet rows differ.
All other twelve far sockets are now accepted internally.  The remaining
global interface is therefore one ordered socket pair, not fourteen
independent socket choices.

Let `Gamma_T` be the directed state graph of an ambient residual host after
contracting this protected path to one ported root vertex `star`.  An arc
out of `star` uses the outgoing exposed socket, and an arc into `star` uses
the incoming exposed socket.  All arcs must include literal Johnson
adjacency, owner/facet capacity, and the two-polarity boundary-history test.
Fix a candidate closing arc `a_*:z->star` and a total order `prec` with
`star` first and `z` last.  Split every vertex into a tail and a head copy
and retain only forward arcs other than `a_*`.  Remove the tail copy of `z`
and the head copy of `star`; call the resulting balanced bipartite graph
`B^0_(T,a_*,prec)`.

The following Hall reduction assumes that this state expansion is
**capacity-faithful**: every matching in `B^0` uses each capacity-one owner,
facet, and history occurrence at most once.  This holds, for example, when
the candidate arc catalogue is globally resource-injective, or when every
shared physical resource has been replaced by an exact exclusive state
gadget whose matching projection is bijective.  Per-arc legality alone does
not imply capacity-faithfulness.

### Theorem 7.1 (exact ordered-Hall corridor criterion)

The protected path extends, using the fixed closing arc and order, through
every residual state to one co-oriented spanning cycle iff, under the
capacity-faithful hypothesis,

\[
       \max_{A\subseteq L(B^0_{T,a_*,prec})}
          (|A|-|N(A)|)=0.                              \tag{7.1}
\]

Equivalently, the exact obstruction is a Hall set with
`|N(A)|<=|A|-1`.  Minimizing the left side over all admissible closing arcs
and orders gives the exact unrestricted rooted-corridor criterion.

#### Proof

A perfect matching of the reduced shores has `n-1` edges in the full
forward graph and leaves exactly `z` without an outgoing edge and `star`
without an incoming edge.  Forwardness makes it acyclic, so it is the one
spanning directed path from `star` to `z`; adding `a_*` gives the cycle.
Conversely, deleting `a_*` from such a cycle gives precisely that perfect
matching.  Hall's theorem gives (7.1). \(\square\)

This is a joint history/topology condition.  Separate matchings of the two
endpoint histories, or a separate graphic-rank calculation, do not imply
(7.1).

Without a capacity-faithful expansion, (7.1) is only necessary.  The exact
fixed-order model must retain, in addition to the tail/head degree rows,

\[
              \sum_{e:\,q\in\operatorname{supp}(e)}x_e\le1
              \qquad\text{for every capacity-one resource }q. \tag{7.2}
\]

This is a matching with shared-resource packing rows, not ordinary
bipartite matching; no Hall sufficiency is claimed for that general face.

## 8. Corridor displacement fibres and a constant pump

For a task `t`, let `C_t(sigma)` be the occurrence-labelled ambient
corridors satisfying Theorem 7.1 and having total added-seam displacement
`sigma in Z_m`.  For a literal corridor `C`, let `P_t(C)` be the displacement
set of pump choices which are simultaneously resource-, history-, and
topology-compatible with `C`.  Exact zero displacement is possible iff

\[
 \left|\{C:\ C\in C_t(\sigma)\text{ for some }\sigma,
                    \ -\sigma\in P_t(C)\}\right|>0.    \tag{8.1}
\]

A single fixed pump displacement covers only one fibre.  A constant-support
phase-tunable pump closes every fibre only when, for every candidate
corridor, its compatible literal menu realizes all of `Z_m`; an abstract
surjective pump menu before corridor/resource conditioning is insufficient.
When the ambient corridor is retained identically in both phases, its
relative displacement is already zero and no pump is needed.

Here is the exact conditional spread statement.  Suppose the left side of
(8.1) is at least `c k^7` for every live task, every completed
corridor--pump choice uses at most `S_d=O(d)` nonprivate resources, and every
such resource occurs in at most `Ck^6` choices of any other task.  Then one
choice excludes at most `CS_dk^6` choices elsewhere, so greedy selection
serves `H` tasks whenever

\[
                     c k^7>(H-1)CS_dk^6.               \tag{8.2}
\]

Thus fixed `H` succeeds for `d=o(k)`.  The local atlas proves (6.3), but it
does not prove the ambient hypotheses in (8.1)--(8.2).

## 9. Why marginal socket spread is insufficient

The distinction in the preceding sentence is necessary.  Take arbitrarily
many tickets with pairwise-spread terminal labels, but let every admissible
continuation of every socket pass through one common exterior resource
`q_*`.  Every socket has a nonempty, even arbitrarily large, marginal menu,
while no ticket admits seven resource-disjoint continuations.  Equivalently,
after contracting the local path one may arrange a forward Hall set `A`
with `|N(A)|=|A|-2`; all individual endpoint degrees can remain positive.

Likewise, put every accepting corridor in displacement fibre `1` and give
the sole pump displacement `0`.  Topology and history can then be feasible
while (8.1) fails.  Hence neither the `Theta(k^7)/O(k^6)` local spread nor
separate history, topology, and voltage marginals imply a completed ambient
ticket.

## 10. Rows still downstream

The theorem closes, locally and literally:

1. all fourteen fixed-`z` far histories;
2. one old and one new co-oriented quotient cycle;
3. lower-facet and immediate-upper packet-palette transport;
4. depth-`d` positive and negative residence; and
5. zero relative sidecar displacement.

After the one-connector opening, the remaining history/topology row is the
single rooted corridor condition (7.1), possibly with the fibre condition
(8.1).  Still downstream are global immediate-upper completeness, deeper
upper witnesses, source/envelope binding, aperture discharge outside the
seven private labels, the terminal common compiler, Pascal regeneration,
and a child-native nonzero-voltage seed.  No universal word or
`B(k)+O(1)` conclusion is asserted.
