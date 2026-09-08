# Stabilizer-stratified defect collapse

**Date:** 2026-08-03  
**Status:** unconditional finite-group theorem and conditional
application to the OR-word construction.  The quarantine implication is
conditioned on the target-bypass interface of Definition 7.0.  No finite
computation is used.

## 0. Outcome

Let the cyclic coordinate rotation group `C_k` act on target masks,
addressed cells, ports, sinks, and every finite physical capacity used by a
fixed residual child.  The free-orbit rigidity theorem says that a matching
defect or suffix-flow corank is a multiple of the orbit order when the
action is free on the complete addressed object.

In a composite dimension the action is not free globally.  The exact
repair is to stratify by **exact orbit order**.  On the order-`q` stratum,
the common stabilizer is the unique subgroup of `C_k` of order `k/q`, so
the residual action is a free action of `C_q`.

Consequently, if a capacity-faithful matching or flow gate is realized
inside its own order-`q` stratum, its defect is a nonnegative multiple of
`q`.  A uniform estimate

\[
                         0\le \delta_q\le C             \tag{0.1}
\]

therefore forces `delta_q=0` for every `q>C`.  There are at most `C`
remaining orbit orders, and in the Boolean target space all masks of orbit
order at most `C` form a bank of size less than `2^{C+1}`, independently of
`k`.

For target-indexed residual gates, or after every non-target residual task
has been placed in a separately certified bounded sidecar, this gives two
useful exact conclusions.

1. A uniform **per-stabilizer** defect bound for a fixed number of such gates
   is already an additive-constant theorem; the defects need not first be
   summed over the divisors of `k`.
2. More sharply, all target masks of orbit order at most `C` may be
   quarantined and appended literally.  Every remaining stabilizer-pure
   **target-bypass** gate with defect at most `C` then saturates exactly.

The quantization theorem applies simultaneously to the exact addressed
compiler graph, the fixed-signature lower-pin graph, the two cross-ray
graphs, the router incidence graph, and the node-split suffix flow.  It does
**not** construct the required stabilizer-pure physical strata.
Cross-stratum shared capacity, nonflat packing transport, a fixed seam, or
a noninvariant compensation linkage destroys the conclusion unless isolated
into the bounded sidecar.  Literal target quarantine additionally requires an
equivariant map from every residual left claim to the target whose literal
appendage waives that claim; it does not quarantine an unrelated router,
topology, or compensation task.  Separate gates may be combined only after
their physical capacities are disjointly reserved or they have been encoded
as one joint capacity-faithful gate.

## 1. Exact-period strata of a cyclic action

Let `G=C_k=<rho>` act on a finite set `X`.  For every divisor `q|k`, put

\[
 X_q=\{x\in X:|Gx|=q\}.                              \tag{1.1}
\]

Because a cyclic group has a unique subgroup of every order dividing
`k`, every point of `X_q` has the same stabilizer

\[
 H_q=\langle\rho^q\rangle,
 \qquad |H_q|=k/q.                                   \tag{1.2}
\]

Hence `H_q` acts trivially on `X_q`, the `G`-action factors through

\[
                         G/H_q\cong C_q,              \tag{1.3}
\]

and this quotient action is free on `X_q`.

### Lemma 1.1 (period-stratum freeness)

For every `q|k`, the residual action of `C_q` on `X_q` is free.

### Proof

If a coset `gH_q` fixes `x in X_q`, then `g` lies in the stabilizer of
`x`, which is exactly `H_q`.  Thus `gH_q` is the identity coset. \(\square\)

## 2. Stabilizer-pure occurrence matchings

Let `A` and `B` be finite `C_k`-sets, and let `H` be an invariant
bipartite graph on them.  Call a subgraph `H^pure` **stabilizer-pure** when

\[
 E(H^{\rm pure})\subseteq
 \bigcup_{q\mid k} A_q\times B_q.                    \tag{2.1}
\]

Write

\[
 M_q=H^{\rm pure}[A_q,B_q],
 \qquad
 \delta_q=|A_q|-\nu(M_q).                            \tag{2.2}
\]

The shores are occurrence-labelled.  Equal target values at different
addresses are different vertices, and aliases of one physical cell have
already been coalesced through one capacity-one vertex before the graph is
formed.

### Theorem 2.1 (periodwise matching quantization)

For every `q|k`,

\[
                         \delta_q\in q\mathbb Z_{\ge0}. \tag{2.3}
\]

In particular, if `delta_q<q`, then `M_q` has a matching saturating `A_q`.

### Proof

By Lemma 1.1, `C_q` acts freely on every addressed vertex orbit of both
shores of `M_q`.  The graph is invariant.  Apply the free cyclic
matching-deficiency divisibility theorem to `M_q`. \(\square\)

### Corollary 2.2 (uniform local defect gives global constant defect)

Let `C` be a nonnegative integer.  If

\[
                         \delta_q\le C                \tag{2.4}
\]

for every divisor `q|k`, then `delta_q=0` for `q>C`, and

\[
 \sum_{q\mid k}\delta_q
   =\sum_{\substack{q\mid k\\q\le C}}\delta_q
   \le C^2.                                           \tag{2.5}
\]

The bound is independent of the number of divisors of `k`.

The same statement holds for any fixed number `g` of stabilizer-pure
matching gates: their total deficiency is at most `gC^2`.

## 3. Stabilizer-pure suffix networks

Fix one materialized post-compensation child.  Let `D` be its addressed,
node-split, directed suffix network, including source arcs from physical
ports, terminal arcs to physical sinks, and every finite capacity arc.

A family of subnetworks `(D_q)_{q|k}` is **capacity-faithfully
stabilizer-pure** when:

1. the active ports, sinks, internal vertices, and finite-capacity arcs of
   `D_q` all have exact `C_k`-orbit order `q`;
2. `D_q` is invariant and the action factors through `C_q`;
3. different `D_q` share no finite physical capacity, port, or sink; and
4. every port-to-sink path used for an order-`q` claim lies entirely in
   `D_q` and has the required terminal type.

The bookkeeping supersource and supersink may be fixed by the action; they
carry no physical capacity.  Their incident source and terminal **arc**
orbits are part of item 1 and must have exact order `q`.  Likewise every
node-split unit-capacity arc is included in item 1.

Let `P_q` be the order-`q` port bank and let

\[
 \gamma_q=|P_q|-r_{\Gamma_q}(P_q)                    \tag{3.1}
\]

be its suffix-gammoid corank.

### Theorem 3.1 (periodwise suffix-corank quantization)

For every `q|k`,

\[
                         \gamma_q\in q\mathbb Z_{\ge0}. \tag{3.2}
\]

Consequently, `gamma_q<=C` for every stratum implies

\[
                         \sum_{q\mid k}\gamma_q\le C^2. \tag{3.3}
\]

### Proof

Every finite physical vertex and capacity-bearing arc orbit in `D_q` has
size `q`.  The free cyclic suffix-corank divisibility theorem applied to
the residual `C_q`-action gives (3.2).  Equation (3.3) follows exactly as
in Corollary 2.2. \(\square\)

### Corollary 3.2 (regular factor plus stratified router)

Suppose that, in every stratum, a claim-to-port graph is left
`h`-regular and right-degree at most `h`, all incidence prefixes are
edge-private, and the suffix corank is `gamma_q`.  Then all but at most
`gamma_q` order-`q` claims are serviceable.  If `gamma_q<=C`, every
stratum with `q>C` is serviced completely and at most `C^2` claims are
missed over all strata.

This conclusion uses the private literal factor-router theorem after the
suffix rank is computed.  An abstract Middle-Levels factor alone does not
produce the literal prefixes or the networks `D_q`.

## 4. Short-period Boolean masks form a constant bank

Let `C_k` act on subsets of `[k]` by cyclic coordinate rotation.  A mask
has orbit order `q` if and only if its binary incidence word has least
period `q`; necessarily `q|k`.

### Lemma 4.1 (short-period mask count)

For a nonnegative integer `C`, the number of Boolean masks whose orbit order
is at most `C` is less than

\[
                         2^{C+1}.                     \tag{4.1}
\]

### Proof

For each `q|k`, an order-`q` mask is determined by its first `q` bits.
Ignoring primitivity gives at most `2^q` masks.  Therefore

\[
 \#\{S:|C_kS|\le C\}
 \le\sum_{q=1}^{C}2^q
 =2^{C+1}-2.                                          \tag{4.2}
\]

Restricting to nonempty masks or to any rank range can only decrease this
number. \(\square\)

### Corollary 4.2 (literal quarantine)

All target masks of orbit order at most `C` may be removed from the
equivariant compiler and appended literally at terminal cost less than
`2^{C+1}`.  If every remaining exact-period compiler stratum has
deficiency at most `C`, it is in fact exact by Theorem 2.1.

Thus a uniform per-period estimate suffices even in highly composite
dimensions.  There is no divisor-count loss.

## 5. Exact interface with simultaneous lower pins

Fix a resident cyclic carrier and an equivariant protected occurrence
system `Z=(Z_x)`.  Its cell signature is

\[
 V_Z(c)=\{x:I_c\cap Z_x\ne\varnothing\}.             \tag{5.1}
\]

Retain the exact addressed signature graph

\[
 {\cal E}_Z=
 \{(S,c):K_c\subseteq S\subseteq E_c, S=V_Z(c)\}.   \tag{5.2}
\]

Every matching in this graph is simultaneously realizable by the one
factor `A_h={x:h in Z_x}`; hence no further interval-cover condition remains
after `Z` is fixed.

Suppose there is a stabilizer-pure invariant subgraph

\[
 {\cal E}_Z^{\rm pure}
   =\mathbin{\dot\bigcup}_{q\mid k}{\cal E}_{Z,q}     \tag{5.3}
\]

whose left shore consists of the strict-lower targets not quarantined in
Section 4, and whose right shore uses distinct physical cells with the same
exact orbit order as their assigned targets.

### Theorem 5.1 (bounded per-period signature defect closes the lower side)

If every `E_{Z,q}` has matching deficiency at most `C`, then all strata
with `q>C` match exactly.  After appending all short-period masks, the
literal lower-compiler defect is zero and the added length is less than
`2^{C+1}`.

Alternatively, without quarantining, the total matching defect is at most
`C^2`.

### Proof

The fixed-signature matching theorem makes every selected edge compatible
with the same literal factor.  Theorem 2.1 gives exactness for `q>C`.
Lemma 4.1 bounds the quarantined target bank.  The non-quarantine statement
is Corollary 2.2. \(\square\)

This theorem is stronger than a rank-only fractional clock and weaker than
the original all-dimensional objective.  The missing construction is an
equivariant protected occurrence system whose **actual addressed signature
graph**, not its rank projection, has the stated stabilizer-pure bounded
defect.

## 6. Flatness and the legality of the strata

The preceding quotient arguments require literal actions on one fixed
physical object.  Suppose schedule or packing states are transported along
an occurrence graph by edge bijections.  The flat-continuation theorem says
that these transports define one globally coherent gauge exactly when all
closed-walk holonomies are trivial; on a simply connected presentation it
is enough to check the translated face relations.

For the stabilizer decomposition, the required consequence is:

\[
 \boxed{
 \text{every rotation carries complete capacity-faithful packings to
 complete packings, and the induced transport is pure gauge.}}          \tag{6.1}
\]

Under (6.1), exact orbit order is well defined for addressed ports, cells,
sinks, and packing labels.  Without it, a value may have period `q` while
its physical realization acquires nontrivial holonomy or a larger address
orbit; Theorems 2.1 and 3.1 then cannot be applied to the projected value
stratum.

Linear seams, pivot collars, openings, compensation paths, deadline flags,
and odd topology actuators normally break the action.  They must be placed
in a bounded exceptional bank or repeated equivariantly.  A single shared
unit capacity between two period strata also invalidates the direct-sum
argument; the same is true for two separately solved gates unless the shared
capacity is priced in one joint gate.

## 7. Stabilizer-stratified bounded-reset theorem

The preceding rows combine into the following construction theorem.

### Definition 7.0 (equivariant target-bypass interface)

For each residual matching gate, let `A^(j)` denote its addressed left
demand shore.  For each residual suffix-flow gate, first couple the suffix
network to a stabilizer-pure regular claim-to-port router as in Corollary
3.2, and let `A^(j)` denote that router's addressed gain claims--not its
ports or internal flow vertices.

A family of these gates has an **equivariant target-bypass interface** when
there are `C_k`-equivariant maps

\[
                         \pi_j:A^{(j)}\longrightarrow\mathcal T,    \tag{7.1}
\]

where \(\mathcal T\) is the set of appendable nonempty target masks, with the
following semantics: appending a mask `S` waives every residual obligation
in every fibre `pi_j^{-1}(S)`.  Every residual obligation without such a
map belongs to a separately certified bounded exceptional bank.

If a claim `a` has orbit order `q` and `pi_j(a)` has orbit order `r`, then

\[
                              r\mid q.                \tag{7.2}
\]

Indeed equivariance gives
`Stab(a) subseteq Stab(pi_j(a))`, so the orbit of the image is a quotient of
the orbit of `a`.  In particular, every claim of orbit order at most `C`
maps to a target mask of orbit order at most `C`.

This interface is automatic for a compiler whose left vertices are the
target masks themselves.  It is an additional theorem for router, topology,
compensation, or continuation tasks; a suffix port or a unit separator is
not a target merely because its loss contributes one unit to a potential.

### Theorem 7.1

Fix nonnegative integer constants `C`, `b`, and a fixed number `g` of
residual matching/flow gates.  Suppose that for every sufficiently large
`k` there is a physical word skeleton of length `B(k)+b_skel` and a
certified exceptional terminal-repair bank of cost `b_term`, where

\[
                         b_{\rm skel}+b_{\rm term}\le b,              \tag{7.3}
\]

with:

1. exact central ownership, residence, complete upper interval-OR coverage,
   and legal path topology, apart from the certified exceptional bank;
2. one fixed post-compensation residual state carrying a cyclic action;
3. flat, capacity-faithful packing transport as in (6.1);
4. a bounded exceptional physical bank containing every noninvariant seam,
   pivot, opening, compensation, deadline, and odd-actuator resource, and
   every residual obligation lacking a target-bypass map; its certified
   terminal repair cost is included in `b_term`;
5. for every exact orbit order `q`, stabilizer-pure addressed graphs or
   subnetworks for each of the `g` residual gates, with every suffix-flow
   gate coupled to the stabilizer-pure regular router required by Corollary
   3.2, and with distinct gates either pairwise disjoint in finite physical
   capacity or already combined into one joint capacity-faithful gate whose
   displayed deficiency is the joint deficiency;
6. deficiency or corank at most `C` in every one of those period-`q` gates;
   and
7. an equivariant target-bypass interface as in Definition 7.0 for every
   nonexceptional left demand or gain claim.

Then

\[
                         \nu(k)\le B(k)+O_{C,b,g}(1). \tag{7.4}
\]

More explicitly, without short-period quarantine,

\[
                         \nu(k)\le B(k)+b+gC^2.       \tag{7.5}
\]

With quarantine, all nonexceptional period strata saturate exactly and

\[
                         \nu(k)\le B(k)+b+2^{C+1}-2. \tag{7.6}
\]

### Proof

For each matching gate apply Corollary 2.2.  For each suffix-flow gate apply
Theorem 3.1 and then Corollary 3.2 to its coupled regular router.  This gives
at most `gC^2` unmatched nonexceptional left demands or gain claims.  Map
them through the target-bypass interface and append the distinct image
masks; their number is at most the number of unmatched claims.  Adding the
skeleton excess and certified exceptional repair costs at most `b` by
(7.3), proving (7.5).

For the sharper formulation, quarantine all target masks of order at most
`C`.  Lemma 4.1 bounds this bank by `2^(C+1)-2`.  If a nonexceptional claim
remains, its image target has orbit order `r>C`; divisibility (7.2) forces
the claim orbit order `q` to satisfy `q>=r>C`.  Conversely every claim with
`q<=C` was waived by the quarantine.  Thus every surviving matching stratum
has deficiency at most `C<q` and is exact by Theorem 2.1.  Every surviving
suffix stratum has corank at most `C<q`, hence corank zero by Theorem 3.1;
Corollary 3.2 then services all of its remaining router claims.  Flatness and
capacity separation ensure these literal conclusions coexist in the one
materialized child.  Adding the skeleton/exception budget (7.3) proves
(7.6). \(\square\)

## 8. What this removes, and the exact remaining theorem

The theorem removes a real composite-dimension obstruction.  It is not
necessary to find one globally free `C_k`-action, nor to pay once for every
divisor of `k`.  It is enough to have:

\[
 \boxed{
 \text{a stabilizer-pure physical realization with a uniform bounded
 quotient defect on each exact-period stratum, together with an
 equivariant target-bypass interface and joint capacity separation.}}   \tag{8.1}
\]

Large-period strata then close exactly by arithmetic rigidity, and the
entire short-period target bank is constant-size.

What remains unproved is the existence of one word skeleton satisfying the
seven hypotheses of Theorem 7.1.  In current terminology, the smallest
missing object is an upper-complete one-copy equivariant carrier with:

* one flat complete-packing gauge;
* a protected occurrence signature whose same-period target-cell graphs
  have uniformly bounded defect;
* private literal claim-to-port prefixes and same-period suffix networks
  with uniformly bounded corank and a target-bypass map on their gain
  claims;
* one bounded noninvariant seam/odd-actuator bank; and
* a regenerative same-parity transition preserving these data.

The abstract Middle-Levels two-factor supplies neither the literal port
map nor the suffix networks.  The fractional rotor supplies neither the
one-copy owner chronology nor the protected signature.  The forward
Catalan atlas supplies neither the color-tail-head matching nor the odd
actuator.  Those are construction gates, not defects in the
stabilizer-collapse theorem.
