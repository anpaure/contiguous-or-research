# Fixed-`z` far-socket cycle flow and the exceptional-pump criterion

**Date:** 2026-08-02  
**Lane:** A, history/topology completion of the two-bank fixed-`z` ticket  
**Status:** exact finite criterion, independently audited explicit local
closure, and a quantitative conditional ambient-corridor theorem.  The rays
export partial bi-history relations; they are not falsely treated as full
two-polarity resets.  The explicit local closure is saturated and therefore
does not itself give a spanning one-cycle host.

## 0. Verdict

For one old or new fixed-`z` terminal state, the protected packet and its
fourteen rays consist of seven directed protected paths.  Write their far
entrance sockets as `Y_i` and their far exit sockets as `X_i`, with indices
in `Z_7`.  The required exterior ear has the prescribed orientation

\[
                         X_i\leadsto Y_{i+1}.             \tag{0.1}
\]

The length-`d` monotone rays fix their near-packet histories but export
**partial** bi-history relations at their far ends.  Consequently an
exterior ear in (0.1) can be tested separately only by composing its exact
two-polarity relation with both adjacent partial sockets.  Once seven such
literal composites are accepted, no boundary state is shared by two
different ears.

The exact remaining local problem is therefore a seven-class integral path
packing with one additive group row.  It is not an ordinary marginal Hall
problem.  A single exceptional aperture or pump closes the group row
exactly when its socket-compatible residue menu contains the inverse of the
residue of the other six or seven selected ears.  An explicit private
`2d+4`-transition ear now proves that the seven local classes are nonempty
and jointly compatible with zero displacement.  The remaining use of the
criterion is a one-corridor spanning-host problem after one local ear is
opened.

## 1. The partial-socket exterior-ear catalogue

Fix one locally completed two-bank fixed-`z` packet at depth `d`.  For each
`i in Z_7`, let

* `Y_i` be the far end of the `y_i`-ray, oriented towards the packet;
* `X_i` be the far end of the `x_i`-ray, oriented away from the packet;
* `S_i^x` be the exact partial bi-history relation exported by the forward
  `x_i`-ray at `X_i`; and
* `S_i^y` be the exact partial bi-history relation exported by the reversed
  `y_i`-ray at `Y_i`.

These socket relations include the literal canonical frames, the fixed
ray-side history halves, and the triangular domains on their exterior
halves.  They are not replaced by unlabelled collar types or by fictitious
two-sided constant outputs.

Let `P_i` be the finite catalogue of all literal directed exterior ears

\[
                            P:X_i\leadsto Y_{i+1}        \tag{1.1}
\]

on the physical host face under consideration which satisfy all of the
following.

1. `P` is internally positive and negative depth-`d` resident.
2. Its exact two-polarity history relation composes with `S_i^x` and
   `S_{i+1}^y` to an accepting literal path relation.
3. It avoids the complete old/new switch-collision bank (packet rows and
   rays in both terminal states) except at its two named sockets.
4. It is co-oriented with the two rays.
5. Its occurrence-labelled physical resource set `R(P)` and its complete
   sidecar displacement `sigma(P)` in the quotient voltage group `A` are
   recorded.

Here `sigma(P)` is the **change** contributed by the physical operations
used to install the ear, relative to the retained baseline.  An ear retained
identically in the old and new fragment ledgers has `sigma(P)=0`; its
intrinsic path voltage must not be counted a second time.

The catalogue may be represented implicitly.  In the exact state-expanded
network, a vertex is

\[
   (T,H^+,H^-),                                          \tag{1.2}
\]

where `T` is a physical owner and the two histories are expressed in its
chosen frame.  A directed Johnson transition is present exactly when both
history automata accept.  A member of `P_i` is a simple directed path from
the allowed state set exported by `S_i^x` to the state set accepted by
`S_{i+1}^y`, with the physical owner/facet capacities imposed on its
projection.

### Lemma 1.1 (accepted partial sockets separate the seven ears)

Let `P_i in P_i` for every `i`, and suppose their resource sets are pairwise
compatible.  Then the union of the seven protected packet paths and the
seven exterior ears is positive and negative depth-`d` resident in both the
old and new terminal states.

#### Proof

By membership in `P_i`, the literal concatenation of the forward `x_i`-ray,
the exterior ear, and the reversed `y_(i+1)`-ray accepts in both history
polarities.  Thus every run crossing either of its far sockets is certified
inside that one composite.  Different composites have disjoint far
sockets, so no exterior history variable is shared between two ears.

Runs crossing a central packet seam are certified for every old seam
`y_i -> x_i` and every new seam `y_i -> x_(i+1)` by the two-bank collar
theorem.  All other runs are internal either to a ray or to an exterior ear.
There is consequently no untested run and no boundary state shared between
two different exterior ears. \(\square\)

## 2. Exact socket-packing theorem

Let `R_0` be that complete old/new protected switch-collision resource set
and let `c(q)` be the
remaining capacity of every occurrence-labelled physical resource `q`.
Let `sigma_0 in A` be the sum of every already fixed noncentral sidecar
displacement.  For `P in P_i`, introduce a binary variable `z_P`.

### Theorem 2.1 (necessary and sufficient fixed-order criterion)

There is a co-oriented history-safe exterior completion of the fourteen
far sockets, with one old quotient cycle, one new quotient cycle, and zero
total sidecar displacement, if and only if the following integer system is
feasible:

\[
\begin{aligned}
 \sum_{P\in P_i}z_P&=1 &&(i\in Z_7),                 \tag{2.1}\\
 \sum_{P:q\in R(P)}z_P&\le c(q)
       &&(q\notin R_0),                               \tag{2.2}\\
 \sigma_0+\sum_Pz_P\sigma(P)&=0 &&\text{in }A,       \tag{2.3}\\
 z_P&\in\{0,1\}.                                     \tag{2.4}
\end{aligned}
\]

If `A=Z_n` and integer lifts `s(P)` are fixed, (2.3) is equivalently

\[
       s_0+\sum_Pz_Ps(P)=n\ell\quad\text{for some }\ell\in Z.    \tag{2.5}
\]

#### Proof

Given a solution, choose the unique ear in each class.  Equations (2.1) and
(2.2) give seven literal, pairwise compatible prescribed-pair ears.  Lemma
1.1 proves both history polarities.  In the old state the protected path
from `Y_i` ends at `X_i`, and the selected ear goes to `Y_(i+1)`; the induced
component permutation is `i -> i+1`, one seven-cycle.  In the new state the
protected path from `Y_i` ends at `X_(i+1)`, so the induced permutation is
`i -> i+2`, again one seven-cycle.  All fragments retain their orientation.
The central fixed-`z` ledger has displacement zero, so (2.3) is precisely
the complete sidecar displacement row.  The voltage-localization theorem
now applies.

Conversely, read the seven exterior ears from any claimed completion.
Their prescribed sockets give (2.1), physical capacity gives (2.2), and
the complete directed fragment ledger gives (2.3).  Membership in `P_i`
follows from literal history acceptance and coorientation. \(\square\)

### Remark 2.2 (optional port permutation)

If the host is allowed to pair `X_i` with `Y_{pi(i)}` rather than requiring
(0.1), the exact topology row is

\[
             \pi\text{ is a 7-cycle and }\pi\circ s
             \text{ is a 7-cycle},                    \tag{2.6}
\]

where `s(i)=i+1`; the second permutation is the new terminal state viewed
from the `Y`-ports.  The strict fixed-`z` host face uses `pi=s`, so (2.6) is
automatic.  A perfect matching which ignores (2.6) can produce several
components and is not sufficient.

For completeness, let `P_ij` be the accepted ears from `X_i` to `Y_j` and
put `z_ij=sum_(P in P_ij) z_P`.  On the arbitrary-pairing face, (2.1) is
replaced by

\[
 \sum_j z_{ij}=1,\qquad \sum_i z_{ij}=1,                         \tag{2.6a}
\]

and the two exact one-cycle rows are the subtour families

\[
\begin{aligned}
 \sum_{i\in S,\ j\notin S}z_{ij}&\ge1,\\
 \sum_{u\in s(S),\ j\notin S}z_{uj}&\ge1
\end{aligned}
 \qquad(\varnothing\ne S\subsetneq Z_7).                         \tag{2.6b}
\]

The first family says `pi` is one cycle.  In the new state, starting at
`Y_i` first enters `X_(s(i))` and then follows the route selected in row
`s(i)`, so the second family says `pi circ s` is one cycle.  Together with
(2.2)--(2.4), these equations are the exact arbitrary-pairing route master.

### Corollary 2.3 (exact seven-commodity flow form)

Instead of enumerating `P_i`, put one integral unit of commodity `i` through
the state-expanded network (1.2), from the state set exported at `X_i` to
the accepting set at `Y_(i+1)`.  Impose shared capacity one on every physical owner/facet or
other protected occurrence, forbid cyclic excess flow, and impose the group
row (2.3) on the selected physical sidecars.  The resulting integral
seven-commodity flow is equivalent to (2.1)--(2.4).

#### Proof

Every selected literal path gives one commodity flow.  Conversely, an
integral unit flow with no cyclic excess decomposes into one simple path;
the state coordinates give exactly the two history tests defining `P_i`.
Shared capacities give (2.2). \(\square\)

### Theorem 2.4 (fixed-fragment common-base form)

There is a useful equivalent form when the ambient host has already been
cut into a fixed table `F` of internally accepting, co-oriented fragments
and every candidate sidecar is one literal join between two fragment
sockets.  Fix one protected exceptional closing join

\[
                         e_*:r\longrightarrow s.        \tag{2.7}
\]

On the candidate-join set define:

* `M_out`, the partition matroid allowing at most one selected join with
  each tail and forbidding a tail at `r`;
* `M_in`, the partition matroid allowing at most one selected join with
  each head and forbidding a head at `s`; and
* `M_gr`, the graphic matroid obtained by forgetting join directions on
  the fragment vertex set.

For `n=|F|`, a set `Q` of joins makes `Q union {e_*}` one directed cycle
through every fragment if and only if `Q` is a common size-`n-1` base of
`M_out,M_in,M_gr`.  The completion is zero-displacement exactly when also

\[
                  \sum_{e\in Q}\sigma(e)
                    =-\sigma_0-\sigma(e_*)\quad\text{in }A.       \tag{2.8}
\]

If the seven protected fixed-`z` paths are only required to occur in their
canonical relative order rather than consecutively, this order is an
additional accepting-root constraint on the unique `s`-to-`r` path.  It is
automatic only for an already layered/ordered fragment table; it is not a
consequence of the three common-base rows.

#### Proof

A common size-`n-1` base of the two partition matroids has one outgoing join
from every fragment other than `r`, one incoming join to every fragment
other than `s`, no incoming join to `s`, and no outgoing join from `r`.
Graphic independence and size `n-1` make its undirected support a spanning
tree.  Hence the directed support is the unique Hamilton path from `s` to
`r`: every internal vertex has one incoming and one outgoing join, while
`s` and `r` are its two ends.  Adding `e_*` closes one directed Hamilton
cycle.  The converse follows by deleting `e_*` from such a cycle.  Equation
(2.8) is the complete additive ledger.

The statement about relative order is literal: a Hamilton path can meet the
seven named protected fragments in a wrong order while satisfying all three
matroids. \(\square\)

This is an exact common-base description, but it is an intersection of
**three** matroids, not the ordinary two-matroid intersection theorem.  If
two candidate joins can additionally collide through a third physical
resource, (2.2) must also be imposed; those general multi-resource rows need
not define a matroid.

### Corollary 2.5 (when a fixed pump decouples displacement)

Let `G` be the directed candidate-join graph on a connected fixed fragment
table.  Suppose there is a potential `phi:V(G)->A` such that

\[
                         \sigma(u\to v)=\phi(v)-\phi(u)             \tag{2.9}
\]

for every admissible non-pump join.  Then every Hamilton path from `s` to
`r` has displacement `phi(r)-phi(s)`.  Thus one protected pump closes every
topologically admissible common base if and only if

\[
             \sigma_0+\sigma(e_*)+\phi(r)-\phi(s)=0.                \tag{2.10}
\]

Conversely, (2.9) exists exactly when the directed sum of `sigma` is zero on
every closed walk of the underlying candidate graph (using a reversed arc
with negated label).  If this closed-walk condition fails, topology alone
does not determine the residual displacement; a fixed pump can close only
the reachable residue fibres which contain its inverse.

#### Proof

Equation (2.9) telescopes along any `s`-to-`r` path.  This proves the first
claim and (2.10).  For the converse, fix a root and define `phi(v)` to be the
signed displacement of any root-to-`v` walk.  Vanishing closed-walk sums
makes this definition path-independent, and a one-edge extension gives
(2.9).  If a closed walk has nonzero sum, two walks between the same
endpoints obtained by inserting or deleting it have different residues, so
no endpoint potential and no topology-only pump rule exists. \(\square\)

### Corollary 2.6 (bipartite alternating-circuit test)

On an arbitrary-pairing socket graph `B subseteq L times R`, restrict to its
matching-covered edges.  The displacement sum is the same for every perfect
matching if and only if every matching-alternating circuit has signed
displacement zero.  Equivalently, on every elementary component of the
matching-covered subgraph there are functions `alpha:L->A` and `beta:R->A`
such that

\[
                          \sigma(u,v)=\alpha(u)+\beta(v).           \tag{2.11}
\]

In that case the common matching displacement is

\[
                       \sum_{u\in L}\alpha(u)+
                       \sum_{v\in R}\beta(v),                     \tag{2.12}
\]

and one pump needs only the inverse of this fixed value plus `-sigma_0`.

#### Proof

The symmetric difference of two perfect matchings is a disjoint union of
alternating circuits.  Hence the circuit condition is equivalent to equal
matching sums.  For the decomposition, fix one vertex potential on a
spanning tree of each elementary component and propagate (2.11).
The alternating circuits generate its allowed-edge cycle space, so
path-independence is exactly the displayed circuit condition.  Summing
(2.11) over a perfect matching gives (2.12). \(\square\)

## 3. Why marginal Hall and ordinary matroid intersection do not suffice

If all candidate ears have mutually disjoint interiors, and arbitrary port
pairing is allowed, forgetting (2.3) and (2.6) leaves an ordinary bipartite
perfect matching problem.  Hall is then exact for that **projection**.

For physical ears, an option can consume many owners, facets, transitions,
and history occurrences.  The family of pairwise resource-disjoint options
is a set-packing independence system, not a matroid in general.  Already
with two socket classes, let the first class have options using `{a}` and
`{b}`, while the second has one option using `{a,b}`.  Both marginal socket
classes are nonempty and the terminal pairing graph can be complete, but no
physical transversal exists.  This is the smallest resource-correlation
obstruction to a Hall-only claim.

Likewise, take two otherwise compatible complete selections with total
residues `1` and `1` in `Z_3`, and suppose no other residue is available.
Every socket, resource, and topology marginal is feasible, but the
zero-displacement face is empty.  The group row is not implied by matching
or graphic rank.

Thus (2.1)--(2.4), or its literal path-flow form, is the exact object.  A
matroid-intersection theorem is available only after a separately proved
host property makes the multi-resource supports a matroidal family (for
example, disjoint preassigned corridors or one-resource links).  The
two-bank collar theorem does not prove such a property.

## 4. Quantitative conditional spread and one exceptional pump

The next lemma gives a usable sufficient theorem once an exterior host
catalogue has been constructed.

### Theorem 4.1 (greedy seven-ear spread)

Suppose, for each `i`,

\[
               |P_i|\ge M,\qquad |R(P)|\le S,           \tag{4.1}
\]

and every nonprivate resource occurs in at most `L` members of any other
one class.  If

\[
                              M>6SL,                    \tag{4.2}
\]

then (2.1)--(2.2) has a solution.

#### Proof

Choose the seven classes successively.  Before the last choice, at most six
previous ears have exposed at most `6S` forbidden resources.  Each removes
at most `L` options from the current class.  Inequality (4.2) leaves an
option. \(\square\)

This lemma does not solve (2.3).  For that row, reserve the last socket
class as an exceptional aperture/pump family.  Write

\[
                 P_6(g)=\{P\in P_6:\sigma(P)=g\}.       \tag{4.3}
\]

### Theorem 4.2 (residue-complete exceptional pump)

Assume the first six socket classes can be selected with pairwise compatible
resources.  Suppose every residue class in the pump family satisfies

\[
              |P_6(g)|>6S L_*\quad(g\in A),             \tag{4.4}
\]

where every resource occurs in at most `L_*` members of each `P_6(g)` and
each of the first six ears has support at most `S`.  Then the seventh ear
can be chosen so that all resources remain compatible and (2.3) holds.

More generally, if the pump offers only a residue set `B subseteq A`, a
completion exists exactly when

\[
 -\sigma_0-\sum_{i=0}^5\sigma(P_i)\in B               \tag{4.5}
\]

for some compatible first-six selection, with a compatible pump option in
that residue fibre.

#### Proof

For fixed first-six ears, let `g` be the inverse residue required by (2.3).
Their union exposes at most `6S` forbidden resources, which delete at most
`6SL_*` members of `P_6(g)`.  By (4.4) one compatible member remains.
Equation (4.5) is the same argument without residue completeness and is
both necessary and sufficient. \(\square\)

The theorem also applies to a separate constant exceptional closing aperture
after all seven ears: replace `P_6(g)` by its socket-compatible aperture
menu and replace `6S` by `7S`.

## 5. Explicit zero-displacement local closure

The abstract nonemptiness issue in Section 4 is now closed for a saturated
local ticket.  Put

\[
 G_i=(H_{i+1}\cap H_{i+2})\cup\{z\},\qquad
 H_i=\{\gamma_i,u_i,v_i\},\qquad
 G_i=\{\gamma_i,p_i,q_i\}.                              \tag{5.1}
\]

The seven pairs `H_i,G_i` meet in exactly the one displayed `gamma_i`.
Choose seven pairwise-distinct private aperture labels `w_i`, disjoint from
all packet roles and collar banks.  Starting at `x_(i,d)`, take the literal
ear `Q_i` whose exchanges are

\[
 D^y\longrightarrow M^y,quad
 \gamma_i\longrightarrow w_i,quad
 u_i\longrightarrow p_i,quad
 M^x\longrightarrow D^x,quad
 v_i\longrightarrow q_i,quad
 w_i\longrightarrow\gamma_i,                           \tag{5.2}
\]

where each bank arrow denotes its `d` ordered one-coordinate exchanges.
It has `2d+4` transitions and ends at `y_(i+1,d)`.

### Theorem 5.1 (literal fourteen-socket closure)

The seven `Q_i` are pairwise owner/facet-disjoint and meet the packet/ray
bank only at their prescribed endpoints.  Each belongs to the exact
partial-socket catalogue `P_i`.  Selecting all seven solves
(2.1)--(2.4) with total displacement zero.  The resulting old and new
graphs are simple co-oriented cycles, both depth-`d` biresident.  They use

\[
                   28d+35\text{ Johnson edges}
          =56d+70\text{ incidence edges}.              \tag{5.3}
\]

#### Proof

After the first bank arrow, (5.2) changes the active triple `H_i` into
`{w_i,p_i,v_i}`; after the second bank and last two exchanges it is `G_i`.
This proves the endpoint identity and rank preservation.  Before `w_i`
appears, the ordered bank profile together with the distinct `H_i` records
the connector and stage; while it is present, the private `w_i` records the
connector; after it disappears, the terminal profile and distinct `G_i`
do so.  The analogous two-coordinate signatures separate all facets and
also separate the connector interiors from the original rays.

At the two far junctions the bank pairs are disjoint.  Inside `Q_i`, the
matched `M^x/D^x` events have `2d+1` intervening transitions; the inverse
`D^y/M^y` events across the reversed `y`-ray have at least `d+4`; and the
`w_i` run and `gamma_i` zero gap have `d+2` intervening transitions.  Every
other active event persists into the adjacent length-`d` ray.  Thus the
two literal partial sockets accept in both polarities.  The two-bank theorem
handles the central seams.

Old traversal advances packet index by one and new traversal by two, so
both are cycles on `Z_7`.  All connectors and rays are retained co-oriented
in both phases and therefore cancel in the fragment ledger; the fixed-`z`
central seam difference is zero.  Finally, each protected packet block has
`2d+1` Johnson edges and each `Q_i` has `2d+4`, yielding (5.3). \(\square\)

This is a local closure, not a spanning-host theorem.  Every vertex of the
local cycle is saturated.  Even when `k=2r-1` and `56d+70<=r-2` let the
small protected-factor theorem extend it to a spanning two-factor, the
local cycle remains a separate component.  Deleting one `Q_j` in both
phases instead leaves paired old/new protected paths with the same two far
sockets; their central rows differ.  The remaining global topology/history
gate is then one resource-faithful ambient corridor between that socket
pair, with its displacement in the same ledger.

The fully audited construction and its corridor formulation are in
`MATH_THEOREM_A_FIXED_Z_FAR_SOCKET_APERTURE_CYCLE_AND_CORRIDOR_FIBRE_GATE_20260802.md`.

## 6. What the two-bank atlas supplies, and what it does not

The two-bank theorem supplies three exact inputs to the criterion above.

1. **Exact partial sockets.**  The length-`d` rays export the relations used
   in Lemma 1.1; they are not full two-polarity resets.
2. **Local support.**  The selected terminal bank has `14+28d` incidence
   edges, hence `O(d)` local support before exterior ears and sidecars.
3. **Local spread.**  Every nonprivate ray/history resource decodes to at
   most two central endpoint resources, and therefore has `O(k^6)` load in
   the `Theta(k^7)` restricted central atlas.

The explicit `Q_i` prove that all seven local `P_i` are jointly nonempty
with zero displacement.  They do **not** prove that the one remaining
socket pair after opening a `Q_i` admits a spanning ambient corridor, that
the ambient corridor catalogue satisfies (4.1)--(4.2), or that one
socket-compatible pump realizes every group residue.  Those are properties
of the residual host and aperture catalogue.

Accordingly, the strongest current positive statement is conditional:
the local closure is unconditional.  For a spanning host, a resource-faithful
residual corridor satisfying the ordered/common-base rows of Section 2,
together with either direct zero-sum feasibility or the residue-compatible
exceptional menu (4.4), splices the opened local path into one ambient
cycle.  This condition is exact enough to be audited by path packing plus a
finite group layer; it makes no marginal matching claim.

## 7. Downstream rows still separate

Solving (2.1)--(2.4) closes only the following rows:

* the fourteen far positive/negative history sockets;
* co-oriented one-cycle topology in both heptagon terminal states; and
* zero total displacement of the sidecars explicitly included in the
  ledger.

It does not imply:

1. preservation or regeneration of upper interval-OR targets beyond the
   immediate cap row;
2. a maximal source/erosion antecedent or full exterior deck transport;
3. the common lower compiler/common-`Q` matching;
4. an aperture discharge unless that aperture was literally the pump in
   Theorem 4.2;
5. a child-native coprime-voltage seed after a modulus change; or
6. compatibility of later cap providers and other sidecars whose resources
   and displacements were not included in `R(P)` and `sigma(P)`.

Every later sidecar must either be incorporated into (2.2)--(2.3) or proved
neutral by a separate literal ledger.
