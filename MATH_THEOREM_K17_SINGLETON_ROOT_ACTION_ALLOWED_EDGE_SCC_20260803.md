# K17 singleton root actions as allowed presentation edges

**Date:** 2026-08-03  
**Status:** exact bipartite-matching reduction.  This is a screening and
materialization theorem for one pinned root action.  It is not a supplier,
occurrence, chronology, compiler, word, or `nu(17)=B(17)` claim.

## 1. Pinned presentation graph

Fix one authenticated parent, a row-disjoint set of selected transfer modes,
all protected presentation edges, and every phase-occurrence presentation
edge that is required to remain literal.  First coalesce the phase pins and
reject any literal collision.  Reserve one distinct dummy unit for every
pinned dummy-to-middle presentation edge.  Delete all pinned real and dummy
endpoints, and expand the remaining dummy capacity into distinct unit copies
with identical residual middle neighborhoods.  The unpinned common-basis
completion is then an ordinary balanced bipartite graph

```text
G = (A,B;E)
```

with at least one perfect matching `M`.  The right shore contains the
remaining rank-eight root vertices.  A direct-root action at a root `rho`
requires `rho` to be matched from a low left vertex rather than a rank-seven
middle left vertex.

Let

```text
E_low(rho) = { low--rho in E }.
```

The action is legal only when `rho` and every edge needed by the action are
unpinned.  That prerequisite is separate from the theorem below.

## 2. Exact singleton criterion

### Theorem 2.1 (allowed-edge criterion)

A singleton direct-root action at `rho` extends to a perfect presentation
matching if and only if some edge of `E_low(rho)` belongs to a perfect
matching of `G`.

#### Proof

If a completed presentation satisfies the action, its edge incident with
`rho` is a low-to-root edge and belongs to that perfect matching.

Conversely, if a low-to-root edge `e` belongs to a perfect matching `M'`,
then `M'` is a complete presentation in which `rho` is matched directly from
a low vertex.  Hence it satisfies the singleton action.  No other root-action
condition remains.  QED.

This is stronger than testing one arbitrarily selected direct-low child:
the action is feasible when **any** one of its legal low children is an
allowed edge.

## 3. One SCC pass decides all singleton actions

Orient the edges relative to `M` as follows:

```text
unmatched edge: A -> B
matched edge:   B -> A.
```

Call the resulting directed graph `D_M`.

### Theorem 3.1 (alternating-SCC test)

For an unmatched edge `a--b`, the following are equivalent:

1. `a--b` belongs to some perfect matching of `G`;
2. `a--b` lies on an `M`-alternating cycle;
3. `a` and `b` lie in the same strongly connected component of `D_M`.

Every edge of `M` is allowed trivially.

#### Proof

If a second perfect matching contains `a--b`, the symmetric difference of
the two matchings is a disjoint union of alternating cycles, one containing
that edge.  Conversely, toggling an alternating cycle preserves perfectness
and installs each formerly unmatched edge on the cycle.  Under the stated
orientation an alternating cycle is a directed cycle, so an unmatched edge
lies on one exactly when its endpoints are in the same strongly connected
component.  QED.

### Corollary 3.2

After one exact perfect matching and one SCC decomposition, every candidate
singleton root action is decided by

```text
exists low--rho in E_low(rho)
    with ((low--rho) in M or SCC(low) == SCC(rho)).
```

When an unmatched edge passes, an SCC path from `rho` back to `low`, together
with the edge `low->rho`, gives an explicit alternating cycle.  Toggling that
cycle materializes a witness completion without a second max-flow solve.  If
the direct-low edge is already in `M`, the incumbent matching itself is the
witness and no cycle is required.  The explicit matched-edge disjunct is
essential: a matched bridge is allowed even though its endpoints need not lie
in one SCC under the `B -> A` orientation.

## 4. Fail-closed use in the K17 joint selector

Positive allowedness must be recomputed on the **actual pinned face**.  In
particular, it is invalid to run a positive test on the bare
`bf5b946f...` parent and then reuse the witness after selecting modes or phase
occurrences: those choices delete left and right endpoints and can split
alternating SCCs.  A bare-face negative is safe in the one-way sense that
deleting edges/endpoints cannot make an edge occur in a perfect matching if
it occurred in none before, provided the later face is genuinely a subgraph
of the same presentation instance.  It still does not certify feasibility of
the later pinned face as a whole.

The proof-safe singleton smoke protocol is therefore:

1. SHA-bind the `bf5b946f...` parent, its exact bundle manifest, the fresh
   `115086`-mode catalogue, selected structural modes, both fully priced
   phase-occurrence choices, protected rows, and the 27 named candidate
   roots.  A request emitted before pricing completion is not an authenticated
   SCC instance.
2. Pin every literal presentation edge implied by those choices.
3. Find one exact perfect matching of the residual expanded presentation
   graph.  If none exists, reject the candidate state before pricing roots.
4. Build `D_M` and its SCCs once.
5. Apply Corollary 3.2 to all 27 roots.
6. For each survivor, toggle an explicit alternating cycle, rematerialize the
   complete table, and recompute the exact 50-head supplier cut.  Count a
   Hall credit only when the rematerialized row states actually provide it.

The present free `ROOT_ACTION` Boolean relaxation implements none of Steps
2--6 and therefore cannot authenticate a SAT witness.  It remains useful as
a proof-safe relaxation for an UNSAT result only when the parent, bundle,
root-action catalogue, request, and every cut are independently SHA-bound and
the relaxation direction is preserved.

## 5. Scope boundary

Singleton allowedness is not compositional.  Two individually allowed
low-to-root edges can require the same low endpoint or incompatible
alternating cycles.  Therefore this theorem does not justify adding singleton
credits or selecting several actions independently.  Multi-action feasibility
must be checked by one joint matching/flow oracle (or by a separately proved
exchange system).  The theorem's exact gain is that the first 27-way screen
needs one matching and one SCC computation, while retaining literal witness
cycles for every survivor.
