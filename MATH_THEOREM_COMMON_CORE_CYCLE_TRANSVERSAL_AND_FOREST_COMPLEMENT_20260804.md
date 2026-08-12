# Common-core cycle transversals: the exact forest-complement reduction

**Date:** 2026-08-04  
**Status:** unconditional graph-theoretic reduction and conditional guarded
fusion theorem.  It replaces the post hoc requirement “choose one common-core
port in every factor component” by one exact graphic-independence condition.
It does not prove that the current Pascal/promotion host contains a bank with
the required literal guard and completion properties.

## 0. Setup

Let `G=(V,E)` be a finite occurrence-labelled host and let `\mathcal F` be any
nonempty family of spanning two-factors of `G` satisfying the fixed protected
owner, palette, residence, upper-witness, cap, and compiler constraints.
No exchange or polyhedral property of `\mathcal F` is assumed.

Let `S\subseteq E` be a bank of **guarded common-core ports**.  Membership in
`S` is occurrence-level: an edge in `S` carries a declared exit/entry history,
the complete boundary guard state, and any completed-hinge data needed by a
later fusion.

For `F\in\mathcal F`, write

\[
 c_S(F)=\#\{\text{cycle components }C\text{ of }F:E(C)\cap S=\varnothing\}.
\tag{0.1}
\]

For a graph `H`, put

\[
 \beta(H)=|E(H)|-|V(H)|+\kappa(H),
\tag{0.2}
\]

where isolated vertices count in `kappa(H)`.  This is the graphic nullity.

## 1. Exact cycle-transversal identity

### Theorem 1.1

For every spanning two-factor `F`,

\[
 \boxed{c_S(F)=\beta(F\setminus S).}
\tag{1.1}
\]

Consequently the following are equivalent:

1. every component of `F` contains an occurrence from `S`;
2. `F\setminus S` is a forest;
3. `\beta(F\setminus S)=0`.

#### Proof

Each component of `F` is a cycle.  If a component contains no `S`-edge, it
survives unchanged in `F\setminus S` and contributes one to the graphic
nullity.  If it contains at least one `S`-edge, deleting the `S`-edges breaks
that cycle into paths and isolated vertices, which contribute zero nullity.
Different factor components remain disjoint, so nullities add.  This proves
(1.1) and all three equivalences.  \(\square\)

Define the exact **common-core component deficiency**

\[
 \eta_{\mathcal F}(S)
   =\min_{F\in\mathcal F}\beta(F\setminus S).
\tag{1.2}
\]

Then `\eta_{\mathcal F}(S)` is precisely the smallest number of residual factor
components which fail to receive a common-core port.

### Corollary 1.2 (forest-extension form)

\[
 \boxed{\eta_{\mathcal F}(S)=0}
\tag{1.3}
\]

if and only if there are disjoint sets

\[
 R\subseteq E\setminus S,\qquad T\subseteq S
\tag{1.4}
\]

such that `R` is a forest and `R\cup T` belongs to `\mathcal F`.

#### Proof

Given a witnessing factor `F`, take `R=F\setminus S` and `T=F\cap S`.
Theorem 1.1 says that `R` is a forest exactly when `eta=0`.  Conversely,
`F=R\cup T` is a factor in `\mathcal F` and `F\setminus S=R`.  \(\square\)

Equivalently, `eta=0` is the rank-constrained guarded-factor system

\[
 F\in\mathcal F,
 \qquad
 |(F\setminus S)\cap E(U)|\le |U|-1
 \quad(\varnothing\ne U\subseteq V).
\tag{1.5}
\]

Thus the component-hitting row is neither an additional matching after the
factor nor a separate component-by-component transversal.  It is one graphic
independence constraint during factor selection.

### Corollary 1.3 (exact fixed-edge extension criterion)

Specialize to the Middle-Levels/bipartite host of the guarded Ore--Ryser
extension theorem.  Let `D` be the protected degree-at-most-two bank, let
`Z` be the fixed forbidden bank, and write

\[
 \delta_\star(P,Z')=0
 \iff
 P\text{ extends to a spanning two-factor avoiding }Z'.
\tag{1.6}
\]

Then a protected completion `F` with `F\setminus S` a forest exists if and
only if there is a graphic forest

\[
 R_0\subseteq E\setminus(S\cup Z),
 \qquad D\setminus S\subseteq R_0,
\tag{1.7}
\]

such that

\[
 \boxed{
 \delta_\star\!\left(
   D,
   Z\cup\bigl(E\setminus(R_0\cup S)\bigr)
 \right)=0.}
\tag{1.8}
\]

#### Proof

If `F` is a witnessing factor, take `R_0=F\setminus S`.  It is a forest,
contains `D\setminus S`, and lies outside `S\cup Z`.  The factor `F` avoids
every edge outside `R_0\cup S`, so it witnesses (1.8).

Conversely, let `R_0` satisfy (1.7)--(1.8), and take a factor `F` supplied by
the extension criterion.  It contains `D`, avoids `Z`, and every edge of
`F\setminus S` lies in `R_0`.  Hence `F\setminus S` is a subgraph of a
forest and is itself a forest.  Theorem 1.1 gives
`\eta_{\mathcal F}(S)=0`.  \(\square\)

This is an exact all-cut formulation.  It does not assert that the family of
admissible forests `R_0` is a matroid.

## 2. Zero-cost completed-hinge consequence

Assume now that every `e in S` is an occurrence-labelled completed hinge.
Call `S` **jointly all-pairs completed** when the following holds.

For any factor `F\in\mathcal F`, any distinct components
`C_1,...,C_c`, and any selected `e_i\in E(C_i)\cap S`, the hinge head of
`e_j` is legal at the tail role of `e_i` for every `i\ne j`; moreover every
supported permutation of the selected heads is jointly legal under the full
shared owner, palette, residence, witness, cap, and compiler ledger.

### Theorem 2.1 (forest complement implies zero-cost fusion)

If `\eta_{\mathcal F}(S)=0` and `S` is jointly all-pairs completed, then some
factor in `\mathcal F` can be fused into one spanning cycle without adding a
physical position.

#### Proof

Choose `F\in\mathcal F` with `F\setminus S` a forest.  By Theorem 1.1 every
component of `F` contains an `S`-hinge.  Select one such hinge in each
component.  If there is one component, nothing remains to prove.  Otherwise
the all-pairs completion hypothesis makes every cyclic permutation of the
selected heads legal.  Reassign the heads according to one cyclic ordering
of the components.  The completed-hinge permutation theorem says that the
new number of components is the number of cycles of that permutation, namely
one, and that no physical position is added.  \(\square\)

The all-pairs hypothesis can be weakened verbatim: it suffices that every
witnessing selection induces a compatibility digraph with a directed
Hamilton cycle.

## 3. Constant-cost overlap consequence

Suppose instead that every port in `S` carries the same complete guarded
history core of length `d-K`: every selected exit ends in that core, every
selected entry begins with it, and the declared connector of at most `K`
letters preserves the full boundary state.  Assume the connector atlas is
product-separable.

### Theorem 3.1

If `\eta_{\mathcal F}(S)=0` and a witnessing factor has at most `C` components,
then its components can be joined into one protected path with added charge
at most

\[
 \boxed{A+(C-1)K,}
\tag{3.1}
\]

where `A` is the total charge of the selected openings.  In particular this
is `O(1)` for absolute `A,C,K`.

#### Proof

Choose one `S`-port in every component, possible by Theorem 1.1.  The common
core gives a guarded connector of charge at most `K` between every ordered
pair of selected ports.  Apply the exact guarded overlap-tour theorem to any
linear ordering of the at most `C` components.  \(\square\)

## 4. Exact obstruction and quantifier boundary

The incidence, owner, and immediate-palette data alone do not imply
`\eta_{\mathcal F}(S)=0`.  Indeed, attach independent formal order-`d` history
tags to the components of any admissible factor and let `S` contain only
ports with one distinguished tag.  All incidence and q1 statements are
unchanged, while every differently tagged factor component is disjoint from
`S`.  Equivalently, `F\setminus S` retains those cycles and has positive
nullity.

Therefore the present promotion and turn-diamond theorems imply an additive
constant only after proving both of the following in one occurrence-labelled
child:

1. **common-core supply:** a bank `S` with one common full guarded core and
   either completed-hinge or constant-cost connector semantics;
2. **cycle-transversal factorization:** `\eta_{\mathcal F}(S)=0`, equivalently a
   guarded factor whose complement of `S` is a forest.

The second row is the exact **Common-Core Component Transversal**.  It can be
attacked with the same joint graphic-factor machinery as the adaptive-rank
theorem; no post hoc component assignment remains.

## 5. Scope

This theorem proves an exact reduction, not the missing supply statement.
The existing promotion atlas has a `2H` **coordinate-containment** core in
each top and top-dependent ordered tail words.  Although `2H>d`
asymptotically, that scalar inequality does not furnish one common ordered
`d`-letter de Bruijn history across different tops or factor components.
What remains unproved is precisely the correlated occurrence-level assertion
that one actual common ordered history and full guard signature form a bank
`S` satisfying (1.3) while retaining the lower compiler and upper witness
system.
