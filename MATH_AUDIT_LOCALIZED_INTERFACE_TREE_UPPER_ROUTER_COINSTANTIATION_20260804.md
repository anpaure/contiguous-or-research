# Audit of localized interface-tree upper/router co-instantiation

**Date:** 2026-08-04  
**Verdict:** PASS after two scope clarifications incorporated into the
theorem: the unicyclic reduction is stated for a chordless module cycle,
and the router separator is not allowed to prescribe an integral route
which the fractional-flow proof is supposed to choose.

## 1. Claim audited

The audited theorem is

MATH_THEOREM_LOCALIZED_INTERFACE_TREE_UPPER_ROUTER_COINSTANTIATION_20260804.md

with SHA-256

0e2f6a05a3e16e3d81bb63d2a857c986db49242d892d36b2bce0fba81fce1412.

It proves only a conditional localized host theorem. It does not prove that
the current Boolean carrier has a bounded total seam footprint, a uniform
separator certificate, a small exceptional occurrence bank, or private
physical lifts. It therefore proves no new bound on \(\nu(k)\).

## 2. Product-profile count

For fixed \(P\cap U=S\), there are

\[
 {p-|U|\choose h-|S|}
\]

choices for \(P\). The independent \(B\)-shore count is

\[
 {q-|V|\choose\ell-|T|}.
\]

Their product is (0.2). The fibres are disjoint, so profile-wise lower
bounds may be summed even when the physical exception banks overlap.
Injectivity of the colour-to-seam map implies that \(E_\lambda\) removes at
most \(|E_\lambda|\) members of one fibre. Thus the positive-part sum
(0.3) is correct.

This refines, but does not contradict, the global hybrid bound in the
product-Johnson source theorem. The new information is useful only when the
module certificate is uniform on each chosen profile.

## 3. Join-tree amalgamation

The union of module join trees has

\[
 \sum_M(|V(T_M)|-1)+(|V(G)|-1)
\]

edges on \(\sum_M|V(T_M)|\) vertices, hence is a tree. For a shared
variable, internal running intersection plus connectedness of the modules
containing it and attachment containment gives one connected global
subtree. Lemma 2.1 is therefore exact.

Lemma 2.2 correctly requires **simultaneous** local support of all incident
separator assignments. Equality of the individual separator projections
would be insufficient at a degree-at-least-two module.

The uniform separator certificate is a genuine additional hypothesis. It
is not inferred from separate lower, upper, or router feasibility.

## 4. Upper and router substitutions

The upper substitution uses precisely the audited order of quantifiers:

1. pin the common interface state;
2. solve the dual witness-choice join;
3. require a nonempty semijoin core on its running-intersection tree; and
4. use immutable reserve Hall outside the full restricted menu envelope.

The reserve construction can then delete one edge per old component without
touching the selected rainbow witness bank.

For the router, weight every chain \(g-p-s\) by \(1/(h_0q_0)\). The loads
are:

\[
 1\quad\text{at each claim},\qquad
 {1\over h_0}\quad\text{on a prefix},\qquad
 {\deg_{B_0}(p)\over h_0}\le1\quad\text{at a port},
\]

\[
 {\deg_{B_0}(p)\over h_0q_0}\le {1\over q_0}
 \quad\text{on a suffix},
\]

and the sink load is at most one by (0.4). With private interiors this is a
valid unit-capacity fractional flow. Integral max flow chooses the literal
routes.

Accordingly, a separator may pin the residual state and factor records but
cannot pin an arbitrary integral route. This clarification is explicit in
the frozen theorem.

## 5. Unicyclic reduction

After attached trees are eliminated, a chordless module cycle has complete
adjacent separator relations \(K_i\). A global tuple is exactly a closed
walk through these relations, which is exactly a diagonal element of their
composition. The fixed-point criterion (0.6) is therefore necessary and
sufficient.

The chordless qualifier is needed. If nonadjacent cycle modules share a
variable, the displayed cycle is missing a separator chord and the simple
two-boundary transfer description need not encode the complete natural
join. The theorem now states the qualifier.

The equality/equality/disequality triangle has no fixed point. One or two
nonempty relation scopes always admit a join tree, so three is the minimum
number of relations in such a hidden cyclic correlation.

## 6. Physical scope

Natural-join consistency does not itself prove capacity feasibility. The
literal corollary separately assumes private interiors and complete priced
interfaces in one cap/phase/occurrence/type state. This matches the private
pushout scope of the source theorem.

The following remain theorem inputs:

* the lower all-subset assignment;
* Boolean realizability and uniform profile support of the upper menus;
* physical occurrence lifts of both router factors;
* compensation privacy and cross-coordinate capacity closure; and
* an exhaustive target ledger.

No finite search, solver, random experiment, or computational candidate was
used.

## 7. Source ledger

    8b41c84ce5d39fb8c16aff7a285a5644c66f2a5dabb71935bf71f65f0b76858a  MATH_THEOREM_PRODUCT_JOHNSON_SEAM_LOCAL_EXTENSION_AND_RARE_DEFECT_CONTAINERS_20260804.md
    9e329db1beeb6614a7ea43e5e18b72fea9619c2c57882b010d977376b49677b9  MATH_THEOREM_BPLUS1_OCCURRENCE_SECTION_DUAL_JOIN_TREE_RESERVE_HALL_AND_BLOCKER_LLL_20260804.md
    2d64e2cb36b65706133ae1e68c6bdda80d433ccd428259860382a301538096d0  MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md
    575a89720b723b6d5f3c42c147d4c808aae667bc9856b037e9a9db5eeba33e01  MATH_THEOREM_TOKEN_SPHERE_LAMINAR_PRIVATE_PIVOT_HOST_COINSTANTIATION_20260804.md
