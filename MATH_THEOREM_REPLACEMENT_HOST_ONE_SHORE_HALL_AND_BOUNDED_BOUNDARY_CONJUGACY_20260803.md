# Replacement hosts: one-shore Hall factors and bounded boundary conjugacy

**Date:** 2026-08-03
**Status:** exact conditional matching theorem and sharp resource-factorization
audit.  The theorem gives a necessary-and-sufficient ordinary Hall criterion
for two phase-local private ticket factors after one endpoint shore is fixed,
and shows how the two factors may differ throughout their bulk while sharing
only a bounded conjugate boundary.  It also gives a quantitative expansion
criterion and a bounded-rank Aharoni--Haxell fallback.  No replacement
common-basis table, owner allocation, outer matching, boundary conjugacy, or
all-dimensional family is constructed here.  The frozen `P*` instance is not
modified or reinterpreted.

## 1. Replacement-host datum

Let `D` be an abstract demand set, with `|D|=n`; the intended finite value is
`n=1748`.  A **replacement-host datum** consists of:

1. a new exact target-partition table in the required compressed-normal
   common-basis face, together with an origin-form parent and an exact outer
   materialization;
2. two perfect owner allocations `Omega^0,Omega^1` on the common root
   skeleton;
3. an injection `s:D -> S` into length-two short rows; and
4. in each phase `phi`, a complete occurrence catalogue of canonical
   tickets

   \[
        t=(s(d),p,u;q,\alpha,\beta;W),                       \tag{1.1}
   \]

   where `p,u` are rank-adjacent predecessor and successor long hosts and
   `W` contains the actual outer source pins, physical cells, addresses and
   every other declared capacity-one resource.

The local validity predicate is evaluated using `Omega^phi`; endpoint
lowers are the values actually delivered by the new outer matching.  Thus
common-basis equality does not silently choose a ticket, an endpoint lower,
or an owner occurrence.

Let `Res_phi(t)` be the complete unit-capacity footprint of `t`, after
omitting only its demand label `d`, which is private by construction.
Footprints include both physical long hosts and their outer sources.  If a
history, address, cell, cap or compiler occurrence is intended to be private,
it is also included.  A phase-local private factor is one ticket per demand
whose complete footprints are pairwise disjoint.

Everything in this definition is an existence hypothesis until explicitly
constructed.  In particular, a new common basis does not imply either a
locally positive catalogue or a private factor.

Throughout this note `phi in {0,1}` indexes only the two s7 owner
allocations.  There is no local-B5-mode axis here.  If a later replacement
host also has several local materialization modes, one must first fix that
mode (and its actual outer matching) and then apply the theorem in the owner
phase `phi`.

## 2. Bounded common boundary

Choose a set `A subseteq D` of boundary demands.  In each phase fix valid,
pairwise private boundary tickets `B_phi={b_phi(a):a in A}` and let
`partial_phi` be their full dependency closure.  This closure includes
every exterior-read endpoint, source, cell, actual address, aperture,
history/reset, residence, supplier, upper/common-cap and non-evicted compiler
row.  Additional connector/reset blocks not attached to a demand may be
adjoined to `partial_phi`; they are subject to the same capacity,
closure and serialization requirements.

Taking boundary demands `A` is only a convenient specialization.  A general
connector boundary is obtained by taking `A` empty, or smaller, and adjoining
the independently declared connector/reset blocks before taking the complete
closure.

A bijection

\[
       \theta:\partial_0\longrightarrow\partial_1             \tag{2.1}
\]

is a **complete boundary conjugacy** when it is an exterior-fixed typed
isomorphism: it preserves every equality and incidence relation, every
capacity-one identity, address, directed history and endpoint orientation,
and the exact value of every declared compositional aggregate.  Moreover the
remaining interior is sealed from the exterior in the sense of the complete
boundary factorization

\[
 {\cal F}_\phi(X,\partial_\phi,Z)
 \Longleftrightarrow
 {\cal I}_\phi(X,\partial_\phi)
 \wedge {\cal E}_\phi(\partial_\phi,Z).             \tag{2.2}
\]

For the declared exterior transport `beta`, completeness also requires

\[
 {\cal E}_0(\partial_0,Z)
 \Longleftrightarrow
 {\cal E}_1(\theta\partial_0,\beta Z).                       \tag{2.3}
\]

Here `X` is disjoint from the boundary and contains all phase-local bulk
tickets.  The boundary is **bounded** only if its complete literal
serialization has size at most an absolute constant `C`; a bounded number
of formal aggregate coordinates is insufficient without a proved bounded
literal representation and composition law.

The matching theorems below construct `X` for a fixed boundary.  They do not
prove (2.1)--(2.3).

## 3. Fix one host shore

Put `D^o=D-A`.  In phase `phi`, fix an injective predecessor assignment

\[
              \pi_\phi:D^o\longrightarrow P_\phi.    \tag{3.1}
\]

Every `pi_phi(d)` is required to be rank-adjacent to `s(d)`, compatible
with the chosen owner allocation, and disjoint from the boundary.  Let
`Q_phi` be a successor-host pool disjoint from
`pi_phi(D^o)` and from all boundary endpoint hosts.

### Definition 3.1 (right-private atlas)

A right-private atlas consists of one completed valid ticket

\[
                      t_\phi(d,u)                         \tag{3.2}
\]

for selected pairs `(d,u) in D^o times Q_phi`, using predecessor
`pi_phi(d)` and successor `u`, such that:

1. every footprint in (3.2) avoids `partial_phi`; and
2. whenever `d != d'` and `u != u'`,

   \[
    \operatorname {Res}_\phi(t_\phi(d,u))
       \cap
    \operatorname {Res}_\phi(t_\phi(d',u'))
       =\varnothing.                                      \tag{3.3}
   \]

Tickets with the same successor conflict through that physical host.  Thus
inside the atlas the only residual conflict between distinct demands is
equality of the successor state.

Condition (3.3) is a statement about the **complete** footprint, not only
the two endpoint rows.  It follows, for example, if every residual resource
is either demand-private or a function of the successor host and resources
belonging to distinct successors are disjoint.  Outer-source privacy then
follows from injectivity of the fixed outer matching.  Any shared address,
cell, flag or history relation between different successor states violates
(3.3).

### Lemma 3.2 (identity-core inverse decoupling)

Suppose, as an additional replacement-host hypothesis, that the exact outer
matching decomposes as

\[
                   \mu=\operatorname{id}_H\mathbin{\dot\cup}\mu_{\rm red},
                                                               \tag{3.4}
\]

where the source and receiver rows of `mu_red` are disjoint from the
identity-hard core `H`.  Suppose every long endpoint used by the boundary
and the two atlases lies in `H`, while every movable short/free inverse
choice belongs to `mu_red`.

Then distinct physical endpoint hosts automatically have distinct outer
sources, every selected endpoint source pin is the identity edge `h -> h`,
and changing either phase-local ticket factor leaves `mu_red` and its
reduced inverse-matching Hall rows unchanged.

#### Proof

For `h in H`, (3.4) gives `mu^{-1}(h)=h`; injectivity of the identity map
proves source privacy from host privacy.  The two summands in (3.4) have
disjoint source and receiver shores, so selecting or changing endpoint
occurrences in `H` neither deletes nor redirects an edge of `mu_red`.
\(\square\)

Without the certified decomposition (3.4), outer sources remain explicit
members of every footprint in (3.3); distinct receiver hosts alone are not
used as a surrogate for inverse-parent compatibility.  In an identity-core
`LR--S` construction, `mu_red` is exactly the reduced `LR--S` inverse
matching, so Lemma 3.2 says that endpoint selection does not erode that
matching or consume any of its Hall capacity.

Let `G_phi` be the bipartite graph on `D^o` and `Q_phi` with edge
`du` precisely when the atlas contains (3.2).

## 4. Exact two-phase Hall theorem

### Theorem 4.1 (one-shore branch, two phase-local flows)

Fix a replacement-host datum, boundary tickets and predecessor assignments
as above, and suppose each phase has a right-private atlas.  Then the
following are equivalent.

1. In each phase there is a private ticket factor on all demands, using its
   boundary tickets and tickets from its declared right-private atlas, and
   extending its fixed predecessor assignment.
2. For each `phi in {0,1}` and every `X subseteq D^o`,

   \[
                   |N_{G_\phi}(X)|\ge |X|.              \tag{4.1}
   \]

If, in addition, (2.1)--(2.3) hold, the two bulk factors may be chosen
independently and erased after use; their only common carried object is the
boundary transported by `theta`.

#### Proof

Suppose a factor exists in phase `phi`.  Its successors are distinct,
so its demand--successor pairs form a matching of `G_phi` saturating
`D^o`.  Hall's theorem gives (4.1).

Conversely, (4.1) gives a matching `m_phi` saturating `D^o`.  Select
`t_phi(d,m_phi(d))`.  Fixed predecessors are injective and disjoint
from the successor pool.  Distinct matched successors and (3.3) make the
complete selected footprints pairwise disjoint; they also avoid the fixed
boundary.  Adding the boundary tickets therefore gives a private factor.
Apply this argument separately in the two phases.

Finally, (2.2) existentially erases each phase-local interior, while
(2.1) and (2.3) identify the complete exterior traces.  No equality of bulk
ticket identities is used.  \(\square\)

The theorem is exact within the certified atlases.  If an atlas contains
every valid completion under the fixed predecessor assignment, (4.1) is an
exact criterion for that whole one-shore face.  If it is only a selected
subatlas, (4.1) is an exact criterion for the subatlas and a sufficient
condition for the full catalogue.

The symmetric theorem fixes successors and matches predecessors.

### Corollary 4.2 (bounded-defect common deletion)

Before promoting any additional demands to the boundary, let

\[
 h_\phi
   =|D^o|-\nu(G_\phi)
   =\max_{X\subseteq D^o}\bigl(|X|-|N_{G_\phi}(X)|\bigr). \tag{4.2}
\]

There is a common set `A^+ subseteq D^o` with

\[
                         |A^+|\le h_0+h_1                    \tag{4.3}
\]

such that each phase graph has a matching saturating `D^o-A^+`.  The bound
is sharp from the two deficiency numbers alone.

If the demands of `A^+` have separately certified phase-valid boundary
tickets whose complete closures are conjugate and disjoint from the two
restricted factors, they may be promoted to the boundary.  Consequently
uniformly bounded phase deficiencies reduce the matching layer to a bounded
common boundary; they do not by themselves construct that boundary.

#### Proof

Take a maximum matching in each phase and let `U_phi` be its unmatched
left shore.  Then `|U_phi|=h_phi`; the equality in (4.2) is the
standard bipartite deficiency formula.  Put `A^+=U_0 union U_1`.  Restricting
either matching to `D^o-A^+` still saturates every remaining demand, which
proves (4.3).

For sharpness, take disjoint sets `U_0,U_1` of sizes `h_0,h_1`, isolate
`U_phi` only in phase `phi`, and give every other demand a private
successor in both phases.  Any common deletion leaving both graphs
saturable contains `U_0 union U_1`.  The final assertion follows by adding
the hypothesized disjoint boundary tickets and applying Theorem 4.1.
\(\square\)

### Rado extension

After deleting the boundary and fixing the chosen endpoint shore, suppose
instead that the residual completed ticket objects are the ground set of a
matroid `K_phi`, and a demand is adjacent to its compatible objects.
Then a phase factor exists exactly when

\[
       r_{K_\phi}(N(X))\ge |X|\qquad(X\subseteq D^o).  \tag{4.4}
\]

This is Rado's theorem.  The right-private case is the partition-matroid
specialization, where the rank is the number of distinct successor states
and (4.4) is (4.1).  Crossing predecessor, successor, cell and address
capacities do not constitute one matroid merely because each separate row
is a partition constraint.

## 5. Quantitative Hall expansion

The exact Hall family (4.1) can be discharged by a simple load estimate.
For one phase put

\[
 \delta=\min_{d\in D^o}\deg_{G}(d),\qquad
 \Delta=\max_{u\in Q}\deg_G(u).                            \tag{5.1}
\]

### Lemma 5.1 (minimum-menu versus successor-load criterion)

If `D^o` is nonempty and

\[
                         \delta>0\quad\hbox{and}\quad
                         \delta\ge\Delta,                    \tag{5.2}
\]

then `G` has a matching saturating `D^o`.

#### Proof

For nonempty `X subseteq D^o`, count edges between `X` and `N(X)`:

\[
       \delta |X|\le e(X,N(X))\le\Delta |N(X)|.
\]

Equation (5.2) gives `|N(X)|>=|X|`; apply Hall.  \(\square\)

This scalar threshold is sharp using only `(delta,Delta)`: if
`delta<Delta`, take `Delta` left vertices all adjacent to the same `delta`
right vertices.  The minimum left degree is `delta`, the maximum right load
is `Delta`, and Hall fails.

For a boundary-aware version, let the unpinned atlas have minimum left
degree `delta_0`.  Suppose each pinned boundary block, including any
connector/reset block and its full dependency closure, deletes at most
`lambda` distinct successor neighbours from the menu of any one residual
demand.  If there are `b` such blocks and the postdeletion maximum successor
load is `Delta`, then

\[
       \delta_0-b\lambda>0\quad\hbox{and}\quad
       \delta_0-b\lambda\ge\Delta                            \tag{5.3}
\]

implies (4.1).  For `n=1748`, (5.3) is a concrete sufficient expansion
target.  Neither common-basis normality nor nonempty individual menus implies
(5.2) or (5.3).

## 6. Bounded-rank set-packing fallback

When (3.3) fails, ordinary Hall is generally unavailable.  Remove every
candidate meeting the fixed boundary.  For each residual demand `d` and
phase `phi`, let `H_(phi,d)` be the hypergraph whose edges are the
complete residual footprints of its valid ticket candidates.  Assume every
edge has size at most an absolute constant `r>=2`.

### Theorem 6.1 (Aharoni--Haxell sufficient expansion)

If, for every nonempty `I subseteq D^o`,

\[
 \nu\!\left(\bigcup_{d\in I}{\cal H}_{\phi,d}\right)
          >(2r-3)(|I|-1),                                  \tag{6.1}
\]

then phase `phi` has a private ticket factor extending its boundary.
If (6.1) holds in both phases and (2.1)--(2.3) hold, the two factors have the
same bounded-boundary conclusion as Theorem 4.1.

#### Proof

Pad smaller footprints by candidate-private dummy vertices to obtain rank
`r` without changing disjointness.  Equation (6.1) is the
Aharoni--Haxell rainbow-matching hypothesis, so one pairwise disjoint
footprint can be selected from every demand family.  These footprints are
exact completed tickets and avoid the boundary.  The boundary and erasure
conclusions follow as in Theorem 4.1.  \(\square\)

Condition (6.1) is sufficient, not necessary.  Its rank must count every
literal capacity-one resource in a ticket footprint.  Hiding a growing
address/history list in one formal label invalidates the claimed constant
`r`.

## 7. Why ordinary Hall can be false

### Proposition 7.1 (minimal uncaptured-resource obstruction)

There are two demands with distinct fixed predecessors and a successor
graph having a perfect matching, but no private ticket factor.

#### Proof

Give demand one the sole ticket `(d_1,p_1,u_1)` and demand two the sole
ticket `(d_2,p_2,u_2)`, with `u_1 != u_2`.  The successor graph consists of
two disjoint edges and passes Hall.  Let both completed tickets use one
additional capacity-one cell `z`.  They cannot be selected together.
\(\square\)

Thus (3.3), a valid matroidal replacement, or the full hypergraph condition
is load-bearing.  Endpoint-host Hall alone cannot authenticate physical
cells, addresses or histories.

There is an analogous boundary obstruction.  If the reduced dependency
graph contains `m` vertex-disjoint bulk--exterior edges and none is removed
by a proved aggregate or reset, every literal separator has size at least
`m`.  A bounded boundary therefore does not follow from the existence of
the two private factors; it is the separate hypothesis (2.1)--(2.3).

## 8. Exact construction target

The replacement-host route is reduced to the following explicit clauses.

1. **Static host -- UNPROVED.** Construct the new exact common-basis table,
   origin parent and outer matching.
2. **Owner allocation -- UNPROVED.** Construct both owner factors with the
   required rank-adjacent ticket catalogues.
3. **Boundary -- UNPROVED.** Exhibit a complete boundary conjugacy of
   uniformly bounded literal size, including aperture, address, histories,
   reset, residence, supplier, upper/common-cap and compiler dependencies.
4. **One-shore route -- UNPROVED EXISTENCE, EXACT TEST.** Find injective
   predecessor assignments and right-private atlases satisfying (4.1), or
   the quantitative sufficient row (5.3), in both phases.  For a bounded-
   sidecar theorem it is enough to prove uniformly bounded deficiencies
   `h_0,h_1` and supply the paired boundary completions required after the
   common deletion of Corollary 4.2.
5. **General route -- UNPROVED EXISTENCE, SUFFICIENT TEST.** If no
   right-private atlas exists, prove the bounded-rank footprint and
   Aharoni--Haxell expansion (6.1).
6. **Serialization -- UNPROVED.** Integrate the phase factors and boundary
   with one integral chronology and the already-scoped pivot, birail,
   pull-clock and bounded-eviction theorems.

The new content is that clause 4 is an ordinary bipartite problem only
after the exact resource factorization (3.3).  Under that condition, the
two phasewise Hall families and the bounded boundary conjugacy are sufficient;
no phase-common matching of the other `n-|A|` bulk ticket identities is
required.

No unconditional statement about `nu(k)` follows.
