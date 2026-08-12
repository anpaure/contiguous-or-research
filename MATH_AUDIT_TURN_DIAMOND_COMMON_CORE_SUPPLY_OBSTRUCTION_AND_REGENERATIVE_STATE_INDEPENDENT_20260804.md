# Independent audit: common-history supply obstruction and regenerative state

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_TURN_DIAMOND_COMMON_CORE_SUPPLY_OBSTRUCTION_AND_REGENERATIVE_STATE_20260804.md`  
**Audited theorem SHA256:**
`e763749d0d222bb6f9207670431365102ac29f1d832aa5904569f5452fc93c03`  
**Verdict:** **GO**.  The negative supply verdict, containment/history
separation, graphic-nullity component count, exact fixed-edge factor
criterion, and stated minimal regenerative extension check.  The result is
a sharp reduction and nonimplication, not a Boolean nonexistence theorem.

No search, solver, or finite computational enumeration is used.

## 1. Scope of the turn projection

The protected factor occurrence lift records the component, turn address,
side, lower set, owner set, and singleton incidence label.  It explicitly
does not record an order-`d` source history or the cap/compiler state.

Adjoining a componentwise tag to that projection leaves every incidence,
owner, q1, phase-parity, and opening-loss statement unchanged.  Requiring
full-state equality for a completed hinge then disconnects distinct tags.
This proves Theorem 1.1 as a logical nonimplication.

The construction is intentionally a state expansion rather than a literal
Boolean counterexample.  It establishes that the forgotten state cannot be
deduced from the projection, not that no correlated literal lift exists.

## 2. Containment core versus history core

In Proposition 2.1, every literal letter has the form `Q union {a_i}` or
`Q union {b_j}`.  Hence every letter and every interval union contains `Q`.
All added coordinates are distinct, so no letter in the first history
equals a letter in the second.  A positive suffix--prefix overlap would
force at least one such equality.  Thus the overlap is zero.

At the promotion scale, `H=o(m)` and `d=O(sqrt(m))`, so
`2m-2H>=2d` eventually and the literal separation has adequate ground-set
room.

The promotion theorem itself has an even stronger semantic warning: its
retained central `2H`-words lie in `U-Q_U`.  The set `Q_U` is a common
coordinate containment core of the masks, not a common ordered de Bruijn
history.  Therefore the inequality `2H>d` cannot be used as a history-core
construction.

## 3. Component-nullity identity

For a two-factor `F`, every component is one cycle.  Deleting no `S_xi`
edge from a component retains that cycle and contributes graphic nullity
one.  Deleting at least one `S_xi` edge breaks it into paths and isolated
vertices and contributes zero.  Nullity is additive across components.

This proves

\[
 \beta(F-S_\xi)
 =\#\{\text{factor components disjoint from }S_\xi\}
\]

and the exact equivalence `eta=0` iff one guarded factor has an `S_xi` port
in every component.

## 4. Fixed-edge Ore--Ryser specialization

Assume `G=ML_m` (or an occurrence-expanded bipartite graph with the same
exact residual `b`-factor oracle).  If `eta=0`, take

\[
                         R_0=F-S_\xi.
\]

It is a forest, avoids `S_xi union Z`, and contains `D-S_xi`.  The witnessing
factor uses only edges from `R_0 union S_xi`, so it avoids

\[
 Y_{R_0}=Z\cup(E-(R_0\cup S_\xi)).
\]

Conversely, an exact extension avoiding `Y_(R_0)` uses outside-`S_xi`
edges only from the forest `R_0`.  Its outside subgraph is therefore a
forest, giving `eta=0`.

Condition `D-S_xi subset R_0` and `D cap Z=emptyset` ensure that
`Y_(R_0)` is disjoint from the forced bank `D`, as required by the exact
extension theorem.  Theorem 4.1 is correct.

The theorem correctly scopes this formula to fixed-edge guards.  A
selection-dependent common-cap or compiler restriction cannot be hidden in
`Z` without a larger state expansion.

## 5. Positive fusion implication

When `eta=0`, selecting one `S_xi` occurrence in every component is valid.
If the occurrence class is jointly all-pairs completed, one cyclic head
permutation fuses all components without adding a position.  If instead it
is a product-separable common guarded `K`-router, at most `C-1` linear joins
cost `K` each.  This gives exactly `A+(C-1)K`.

Neither implication follows from the history word alone; the theorem
explicitly includes the full guard state and joint/product semantics.

## 6. Promotion-atlas audit

The promotion inputs prove local core-safe paths and separate rankwise
integral assignments.  They do not prove:

* that one ordered history occurs across different tops;
* that separate ranks choose common nested phases;
* that selected local paths are owner-disjoint globally;
* that every rescued factor component meets one common occurrence class; or
* that the occurrences form completed hinge rectangles.

Thus the negative current-status verdict is accurate.  The scale
`H/d to infinity` only says that local paths are long enough to contain
order-`d` subwords; it supplies no equality or component transversal.

## 7. Minimal state and exact frontier

Every field of `Xi` has a cited independent failure mode:

1. without the literal core, histories can have zero overlap;
2. without orientation state, predecessor/successor roles need not agree;
3. without residence/upper state, a seam may erase a protected certificate;
4. without occurrence identity, halfports may alias one owner capacity;
5. without cap state, identical histories may lie in disconnected flag
   classes;
6. without joint completion, individually legal hinges may consume one
   common unit; and
7. without the forest-complement condition, an entire factor cycle can miss
   the exported state.

For the additive-constant problem an entire terminal compiler matching need
not be exported; a complete bounded damage signature is sufficient by
bounded eviction.  The theorem uses precisely that weaker field.

The exact remaining construction is therefore `GCCFC(K,B)`: one actual
common `d-K` history and guard state, a component-hitting occurrence bank,
joint zero/constant-cost fusion, and bounded final damage.  None of the
current inputs proves those rows simultaneously.
