# Scope audit and exact invariants for four-resource cycle exchanges

Date: 2026-08-01  
Status: theorem-level model audit.  This note gives an exact normal form for
every resource-neutral exchange and an exact graphic criterion for cycle
removal.  It also records the precise, narrower scope of the frozen
Cartesian-hex Delcourt--Postle counterexample.  It does not prove that a
cycle-removing exchange always exists.

## 0. Conclusions

There are three logically distinct statements in the current frontier.

1. A displayed Cartesian ternary `C6` is an exact six-edge actuator.
2. An `N-o(N)` Delcourt--Postle matching can have one physical cycle and
   avoid every old phase in that displayed Cartesian catalogue.
3. It remains open whether an **exact outer-complete** four-resource factor
   containing a cycle must admit some larger or nonlocal neutral exchange.

The second statement does not imply the negation of the third.  It concerns
a near-perfect matching rather than an exact factor, and its conflict system
contains only the frozen Cartesian old phases.  The source theorem itself
does not classify every `3<->3` exchange, let alone exchanges of unbounded
support.

Every possible neutral exchange nevertheless has a rigid exact form.  It is
a new bijection from the old typed tails to the old typed heads whose
intersection palette and union palette are exactly the old lower and upper
palettes.  Its tail--head symmetric difference is a disjoint union of
alternating circuits.  The lower and upper imbalances of those circuits may
cancel only globally; an individual circuit need not itself be a legal
four-resource exchange.

Finally, a single directed cycle cannot absorb itself.  Any neutral exchange
whose old support lies wholly on that cycle leaves a nonempty directed cycle
cover on the same physical vertices.  Eliminating the last cycle requires an
external path endpoint bank (or a non-neutral operation).  Moreover a
nontrivial Boolean-diamond neutral exchange has at least three old and three
new atoms.

OR-word residence, deep-shadow and common-cap guards are not among the four
resources below and remain separate constraints.

## 1. Exact four-resource host and factor terminology

Let `Omega` have size `2m`, and put

\[
 \mathcal L={\Omega\choose m-1},\qquad
 \mathcal U={\Omega\choose m+1},\qquad
 \mathcal M={\Omega\choose m}.
\]

Use disjoint typed copies `mathcal T` and `mathcal H` of `mathcal M`.  For
distinct `a,b` outside `L in mathcal L`, the ordered Boolean-diamond atom is

\[
 e(L;a,b)=
 (L,\ L+a+b,\ (L+a)_{\mathcal T},\ (L+b)_{\mathcal H}).
\tag{1.1}
\]

Equivalently, for adjacent rank-`m` sets `T,H`,

\[
 e(T,H)=(T\cap H,\ T\cup H,\ T_{\mathcal T},\ H_{\mathcal H}).
\tag{1.2}
\]

A **four-resource matching** is a set of atoms with no repeated lower,
upper, typed-tail or typed-head resource.  Its physical projection is the
directed graph with arcs `T->H`.  Thus every physical vertex has outdegree
and indegree at most one.

Write

\[
 N=|\mathcal L|=|\mathcal U|={2m\choose m-1}.
\]

In this note an **exact four-resource factor** means a four-resource
matching of size `N`; equivalently it saturates both outer shores.  Its tail
and head maps remain injections into the larger set `mathcal M`.  A matching
of size `N-o(N)` is only a near-factor.  A factor whose physical graph is a
linear forest is the acyclic ordered-four-transversal object used by the
Catalan linear matching reduction.

## 2. Exact definition of a neutral alternating exchange

Let `M` be a four-resource matching.  A **resource-neutral exchange** is a
pair `(R,B)` such that

* `R subseteq M`;
* `B` is a four-resource matching disjoint from `M-R`; and
* on each typed shore `S in {L,U,T,H}`,

\[
                 V_{\mathcal S}(B)=V_{\mathcal S}(R).
\tag{2.1}
\]

Then

\[
                         M'=(M-R)\cup B
\tag{2.2}
\]

is a four-resource matching of the same size and with exactly the same four
global resource sets.  In particular an exact factor remains an exact
factor.

This is the appropriate definition for a cycle-removing exchange.  It is
stronger than preserving only cardinalities and weaker than preserving any
OR-word guard.

### Theorem 2.1 (successor-permutation normal form)

Let

\[
 \mathsf T=V_{\mathcal T}(R),\qquad
 \mathsf H=V_{\mathcal H}(R),\qquad |R|=t.
\]

Resource-neutral exchanges `(R,B)` are in bijection with bijections

\[
                         \sigma:\mathsf T\longrightarrow\mathsf H
\tag{2.3}
\]

such that every `T` is Johnson-adjacent to `sigma(T)` and

\[
 \{T\cap\sigma(T):T\in\mathsf T\}=V_{\mathcal L}(R),
 \qquad
 \{T\cup\sigma(T):T\in\mathsf T\}=V_{\mathcal U}(R).
\tag{2.4}
\]

All sets in each brace in (2.4) are distinct.  The corresponding positive
phase is uniquely

\[
 B_\sigma=\{e(T,\sigma(T)):T\in\mathsf T\}.
\tag{2.5}
\]

#### Proof

The tail and head equalities in (2.1) make the atoms of `B` a bijection
between `mathsf T` and `mathsf H`; call it `sigma`.  Legality of an atom
forces Johnson adjacency, and its lower and upper resources are uniquely
`T cap sigma(T)` and `T union sigma(T)`.  The remaining two equalities in
(2.1) are therefore exactly (2.4).  Conversely (2.3)--(2.4) make (2.5) a
matching on all four shores with the same resource sets as `R`.  Disjointness
from `M-R` follows because those global resources occur only in `R`.
`square`

This normal form is the smallest exact finite model for the unrestricted
cycle question: choose a new successor bijection, but enforce both outer
palette equations.  Ordinary directed reachability or a tail--head perfect
matching alone is insufficient.

### Corollary 2.2 (alternating-circuit decomposition with two coupled debts)

Let `sigma_0` be the old tail--head bijection encoded by `R`, and let
`sigma_1` encode `B`.  The permutation

\[
                         \pi=\sigma_0^{-1}\sigma_1
\tag{2.6}
\]

decomposes the physical symmetric difference into disjoint even alternating
circuits.  Every circuit is automatically balanced on the typed tail and
head shores.  If `Gamma` is one circuit, define its outer signed debts

\[
 \delta_L(\Gamma)=\chi_L(B\cap\Gamma)-\chi_L(R\cap\Gamma),\qquad
 \delta_U(\Gamma)=\chi_U(B\cap\Gamma)-\chi_U(R\cap\Gamma).
\tag{2.7}
\]

The complete exchange is legal exactly when

\[
                 \sum_\Gamma\delta_L(\Gamma)=0,
                 \qquad
                 \sum_\Gamma\delta_U(\Gamma)=0,
\tag{2.8}
\]

and the positive atoms are pairwise resource-disjoint.  In particular,
one may not toggle the tail--head circuits independently unless each has
zero outer debt.

#### Proof

The standard symmetric difference of two bipartite perfect matchings is a
disjoint union of alternating circuits, indexed by the nontrivial cycles of
`pi`.  Equations (2.7)--(2.8) are simply the lower and upper coordinates of
(2.1), grouped by those circuits.  `square`

### Corollary 2.3 (one-point outer flux cancels on each circuit)

For every alternating circuit `Gamma` and every ground coordinate `x`,

\[
 \sum_{L}\delta_L(\Gamma;L)\,1_{x\in L}
 +\sum_{U}\delta_U(\Gamma;U)\,1_{x\in U}=0.
\tag{2.9}
\]

#### Proof

For every Boolean diamond,

\[
             \mathbf1_{T\cap H}+\mathbf1_{T\cup H}
                    =\mathbf1_T+\mathbf1_H
\tag{2.10}
\]

coordinatewise.  One tail--head alternating circuit uses the same typed
tail set and the same typed head set in its old and new phases.  Subtracting
(2.10) over its two phases gives (2.9).  `square`

Thus lower and upper debts are already opposite at the one-point marginal
level.  This is only a necessary flux identity: it does not imply equality
of the actual lower and upper set palettes in (2.4).

## 3. Exact graphic accounting

Let `G=partial M` and `G'=partial M'` be the directed physical graphs, and
forget orientation only while taking graphic rank.  Put

\[
                         G_0=G-\partial R.
\tag{3.1}
\]

Contract every connected component of `G_0`.  Let `Q_R` and `Q_B` be the
resulting quotient multigraphs formed from the old and new physical edges.
Loops are retained as graphic loops.

### Theorem 3.1 (cycle-rank identity)

Let `c(X)` denote the number of directed cycle components of a physical
partial-permutation graph `X`.  Then

\[
 c(G)-c(G')
   =r_{\rm gr}(G_0+\partial B)-r_{\rm gr}(G_0+\partial R)
   =r_{\rm gr}(Q_B)-r_{\rm gr}(Q_R).
\tag{3.2}
\]

Hence an exchange removes exactly `q` physical cycles if and only if its
new quotient phase has graphic-rank gain `q` over its old quotient phase.

#### Proof

Equation (2.1) preserves at every physical middle vertex its outdegree
indicator and its indegree indicator.  Consequently the sets of directed
path sources, directed path sinks and isolated vertices are pointwise
unchanged.  The number of directed path components is therefore unchanged.
For a maximum-in/outdegree-one graph,

\[
                 \kappa(X)=p(X)+c(X)+i(X),
\]

so `c(G)-c(G')=kappa(G)-kappa(G')`.  Graphic rank is
`|V|-kappa`, giving the first equality in (3.2).  Contracting a common base
preserves rank differences, giving the second.  `square`

This is the exact replacement for an informal statement that an alternating
cycle ought to break a physical cycle.  The relevant condition is a strict
graphic-rank gain after the common remainder is contracted.

### Theorem 3.2 (a directed cycle cannot absorb itself)

Let `C` be one directed cycle component of `G`.  If `R subseteq E(C)`, then
every resource-neutral replacement `B` leaves the graph induced on `V(C)`
a nonempty directed cycle cover.  In particular

\[
                              c(G')\ge c(G)
\tag{3.3}
\]

when `C` is the only component touched, so the cycle is not removed.

More generally, an exchange supported only on a union of directed cycle
components can merge several cycles, but it cannot eliminate the last one
from that union.

#### Proof

Every old tail and old head in `R` belongs to `V(C)`, hence Theorem 2.1
forces every new edge to have both ends in `V(C)`.  On that vertex set the
untouched old edges together with `B` still give indegree and outdegree one
at every vertex.  A finite nonempty directed graph with that degree profile
is a disjoint union of directed cycles.  The multi-cycle statement is the
same argument on the union.  `square`

Thus a neutral absorber for the last cycle must touch at least one path
component.  If the factor has only cycles and isolated vertices, neutral
four-resource exchanges can merge its cycles but can never produce a
linear forest.  A gain/loss operation or an endpoint-changing sidecar is
then necessary.

### Corollary 3.3 (minimum support)

A nontrivial Boolean-diamond resource-neutral exchange has

\[
                             |R|=|B|\ge3.
\tag{3.4}
\]

Consequently eliminating a single cycle requires at least one old atom
outside that cycle and at least three old atoms in total.

#### Proof

Support one is uniquely determined by its four resources.  Theorem 4.2 of
`MATH_THEOREM_BOOLEAN_HEX_TERNARY_FOUR_RESOURCE_ABSORBER_20260801.md`
proves that a nonidentity `2<->2` Boolean-diamond exchange is impossible.
Theorem 3.2 supplies the exterior-support assertion.  `square`

The familiar ternary hex (`3<->3`) meets the lower bound, but its use of one
cycle edge and two distinct path components is a sufficient graphic pattern,
not a proved classification of all minimum exchanges.

## 4. Exact scope of the frozen Cartesian-C6 refutation

Let `X_m` be the three-uniform configuration hypergraph whose members are
the old phases of the **displayed Cartesian fan** in
`MATH_THEOREM_BOOLEAN_HEX_TERNARY_FOUR_RESOURCE_ABSORBER_20260801.md`.
The frozen calculations are

\[
 d_{X_m}(e)=(m-1)^2,\qquad \Delta_2(X_m)\le1.
\tag{4.1}
\]

The theorem
`MATH_THEOREM_BOOLEAN_HEX_DP_HEX_FREE_CYCLE_OBSTRUCTION_20260801.md`
adds `X_m` to the Delcourt--Postle conflict system and proves, for all large
`m`, the existence of a four-resource matching of size `N-o(N)` whose
physical graph is one prescribed directed four-cycle plus a linear forest
and which contains no member of `X_m`.

Therefore the following implication is rigorously false:

\[
 \text{DP near-perfectness + one cycle}
 \quad\Longrightarrow\quad
 \text{an applicable displayed Cartesian ternary hex}.
\tag{4.2}
\]

It does **not** prove any of the following stronger statements.

1. An exact outer-complete four-resource factor with a cycle can avoid all
   neutral exchanges.
2. The protected near-factor avoids every possible `3<->3` exchange.  The
   source absorber theorem explicitly does not classify all hexagons
   through a target.
3. It avoids an `O(|C|)` cycle-following exchange or any unbounded-support
   exchange.
4. Every fixed finite exchange catalogue is avoidable merely because it is
   finite.

For a new bounded catalogue `mathcal C_m`, the same conflict-free strategy
is valid only after its old-phase configuration hypergraph, its intersections
with the protected cycle, and all mixed codegrees with physical short-cycle
conflicts satisfy the Delcourt--Postle hypotheses.  The calculation (4.1)
does this for `X_m`; it is not automatic for an arbitrary catalogue.

## 5. Exact target for a cycle-following theorem

The weakest correct positive statement now has the following form.

> Given an exact four-resource factor `M` and a directed cycle component
> `C`, find a finite old set `R subseteq M` meeting `C` and at least one path
> component, together with a successor bijection `sigma` satisfying
> (2.4), such that the contracted graphic-rank gain in (3.2) is positive.

For bounded support this is a finite four-resource circuit catalogue.  For
`O(|C|)` support it is a cycle-following successor-permutation problem with
two globally cancelling outer-palette debts.  Either version must also
specify whether it works for exact factors only or already for the
`N-o(N)` Delcourt--Postle near-factor.

Only after this central exchange has been found may one impose the separate
literal guards:

* owner chronology and endpoint sockets;
* residence;
* deeper lower and upper shadows;
* the common nonzero compiler-cap state; and
* star-hidden fan/crossing trace compatibility if the exchange is lifted by
  a one-cell seam.

No implication to a literal OR word is asserted here.

## 6. Provenance and audit boundary

The model and the Cartesian-C6 scope were checked against:

* `MATH_AUDIT_JMS_ORDERED_DIAMOND_DEFINITIVE_AND_DP_FALLBACK_20260801.md`;
* `MATH_THEOREM_BOOLEAN_HEX_TERNARY_FOUR_RESOURCE_ABSORBER_20260801.md`;
* `MATH_THEOREM_BOOLEAN_HEX_PLANTED_DP_FIXED_BANK_20260801.md`;
* `MATH_THEOREM_BOOLEAN_HEX_DP_HEX_FREE_CYCLE_OBSTRUCTION_20260801.md`;
* `MATH_THEOREM_BOOLEAN_HEX_COMPONENT_PRIVATE_CONTRACTION_20260801.md`; and
* `scratch/boolean_hex_dp_hex_free_cycle_20260801.audit.json`.

The new content of this note is Theorems 2.1, 3.1 and 3.2 and their exact
scope consequences.  No finite search is used.
