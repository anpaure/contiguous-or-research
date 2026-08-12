# Audit of the K17 singleton root-action allowed-edge/SCC theorem

Date: 2026-08-03

Audited theorem:
`MATH_THEOREM_K17_SINGLETON_ROOT_ACTION_ALLOWED_EDGE_SCC_20260803.md`,
original SHA-256
`7b782d17a83c8206c3b6f1c9304f505044b91d797a72b6ce2f5e9e3bf6c9076a`.

The theorem was corrected during this audit.  The corrected snapshot has
SHA-256
`8b0d6ce7f0834e7954e2c84c8d723751312fa8d86b9c1b2390ab401cec3b32ee`;
it now includes the matched-edge disjunct, dummy-pin order, pricing/phase-pin
scope, and pinned-relaxation qualification identified below.

Status: PASS for the corrected theorem, subject to the implementation and
noncomposition boundaries below.  It is a singleton screen on one completely
pinned presentation face.  It is not a simultaneous-action, supplier, or
global root-open theorem.

## 1. Exact matched-edge correction

For the orientation

```text
unmatched A--B edge: A -> B
matched A--B edge:   B -> A,
```

an **unmatched** edge `a--b` is allowed exactly when `a` and `b` are in the
same SCC.  A matching edge is allowed trivially, whether or not its endpoints
are in the same SCC.

Therefore the predicate in Corollary 3.2 must be

```text
exists low--rho in E_low(rho) such that
    (low--rho is in M) OR (SCC(low) == SCC(rho)).
```

As written, the corollary omits the first disjunct.  A matched bridge is a
counterexample: it belongs to the reference perfect matching, but under the
one-way matched orientation its endpoints can be distinct singleton SCCs.
The current predicate would reject it.

If the chosen edge is matched, the reference matching itself is the witness
and no toggle is needed.  If it is unmatched, the edge plus a directed return
path from `rho` to `low` gives the alternating cycle claimed in the theorem.

This correction does not affect a run that deliberately chooses the literal
parent presentation as `M` and whose candidate roots are all currently fed by
rank-seven middles.  It is nevertheless required by the theorem's stated
arbitrary-perfect-matching scope.

## 2. Dummy-capacity expansion lemma

Let the residual dummy bank have integral capacity `c`.  Replacing it by
labelled unit vertices `d_1,...,d_c`, each adjacent to the same residual set
of middle-in vertices, preserves perfect-matching feasibility:

- an integral capacitated matching lifts by assigning distinct labels to its
  `c` used dummy units; and
- forgetting labels projects every matching of the expansion to the original
  dummy-capacity flow.

The expansion is exact only under three conditions:

1. the dummy units are indistinguishable and have identical residual
   neighborhoods;
2. no socket, state, or owner constraint addresses a dummy label; and
3. all pins are processed before expansion.

The correct pin order is:

1. coalesce duplicate literal presentation pins from the two phases;
2. reject conflicting pins or a nonmatching real pin set;
3. allocate one distinct dummy unit to every pinned dummy-to-middle edge;
4. delete the corresponding middle-in endpoint; and
5. expand only the residual capacity `c-t`, where `t` dummy units were pinned.

One must not delete the single endpoint of an aggregated capacity node.  The
SCC theorem is stated on the labelled unit expansion.  No compact SCC
quotient for the single capacity node is proved here.

The current relaxed materializer has the required symmetric capacity model:
the original dummy count is 2,533, pinned dummy uses are subtracted, and the
remaining aggregate dummy node has the same legal arc set to every eligible
middle.  Thus it is existence-equivalent to the labelled expansion.  The
materializer itself is a capacitated max-flow, not an implementation of the
new SCC pass.

## 3. Phase pins are load-bearing

Let `G0` be the residual graph before phase occurrences are chosen and
`Gomega` the graph after the union of the two phases' exact presentation pins
is imposed.  Then every perfect matching of `Gomega` is a perfect matching of
the corresponding restriction of `G0`, but the converse can fail.  Pins can
delete endpoints, remove alternating cycles, and split SCCs.

Consequently:

- a negative singleton result on the unpinned face is a safe one-way screen:
  later pins cannot create a perfect matching containing an edge that no
  perfect matching of the larger face contained;
- a positive result is not reusable after any mode, state-group, occurrence,
  or protected-presentation pin changes; and
- exact acceptance requires rebuilding the residual dummy capacity and graph,
  finding one perfect matching, and recomputing SCCs after the fully priced
  phase-0/phase-1 occurrence assignment is fixed.

Repeated identical phase pins must be coalesced.  Conflicting phase pins make
the candidate infeasible before the singleton screen.

## 4. No multi-action composition

Individual allowedness does not compose.  Two allowed low-to-root edges may
share the same low endpoint; alternatively, their witness alternating cycles
may compete for a matched edge.  Summing singleton `rho` credits is therefore
invalid.

For a proposed set `T` of direct-low root actions, the exact test remains
polynomial but is joint: remove every middle-out-to-root edge incident with a
root in `T` (and impose all current pins), then ask for one perfect matching.
Because every root has matching degree one in a completion, a perfect
matching of this restricted graph exists if and only if every root in `T` is
fed by a low vertex simultaneously.  A failed solve returns the joint Hall
shore.  Singleton SCCs are domain filters and witness harvesters, not a
replacement for this joint oracle.

## 5. Relation to the emitted joint selector

The current V1 master does not contain common-basis/presentation matching
variables.  A `ROOT_ACTION` bit currently:

- conflicts with a selected transfer incident with its named row; and
- conflicts with an occurrence that pins the row in its `BASE_LMR` state.

It does not force a low-to-root presentation edge or jointly compose several
actions.  This is correctly a branch--Benders intent variable.  A SAT model
must go to the external root/common-basis oracle; a singleton survivor is not
an accepted materialization.

Nor is supplier gain a function of `rho` alone.  Different allowed low
children, alternating return paths, or residual matching completions can
materialize different head/supplier incidences.  A positive supplier replay
authenticates one literal completion column.  A zero-gain replay does not
eliminate the root action, and a negative Benders cut must still be proved
over every residual completion represented by its master assignment.

The candidate singleton-screen request needs two fail-closed conditions:

1. it must not be executed while any active role/phase menu is incomplete,
   because missing occurrence endpoints are missing pins; and
2. it must bind the semantic bundle/parent, protected rows, phase catalogues,
   root-action catalogue, complete assignment, selected modes, selected
   occurrences, and selected root-action file.

Emitting a request before active-set pricing is finished is safe only if it is
marked `WAIT_FOR_PRICING` and never used to certify a survivor.  The SCC pass
must be regenerated after pricing because the phase pins may change.

Finally, any UNSAT result from the free-`ROOT_ACTION` master remains scoped to
the authenticated pinned-parent/catalogue relaxation and its universally
verified cuts.  It is not a global root-open UNSAT result.  The current V1
source correctly rejects a manifest attempt to self-declare exhaustive root
columns; an exhaustive future schema needs a parsed, hash-bound, independently
replayed column-exhaustion certificate.

## 6. Proof-safe singleton protocol

The corrected protocol is:

1. finish active-set pricing and fix the common declared state plus one
   occurrence in each phase;
2. authenticate and coalesce all parent, protected, mode, and phase pins;
3. reserve pinned dummy units, expand the residual indistinguishable capacity,
   and reject any pin conflict;
4. find one residual perfect matching;
5. for every candidate low-to-root edge, accept it when it is matched or its
   endpoints share an SCC;
6. materialize the matching directly in the matched case, or toggle the
   explicit alternating cycle in the unmatched case;
7. replay the table and exact 50-head/supplier graph; and
8. for more than one selected action, discard singleton composition and run
   the joint restricted matching oracle.

Only the rematerialized supplier incidence may be counted as a Hall credit.
