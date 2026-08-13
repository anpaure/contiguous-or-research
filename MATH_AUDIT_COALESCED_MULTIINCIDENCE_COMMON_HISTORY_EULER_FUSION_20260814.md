# Hostile audit of coalesced multi-incidence common-history Euler fusion

**Date:** 2026-08-14

**Audited source:**
`MATH_THEOREM_COALESCED_MULTIINCIDENCE_COMMON_HISTORY_EULER_FUSION_20260814.md`

**Verdict:** PASS after clarifying “same successor swap” to mean a swap of
the reused incoming occurrence's current successor. Multiple incidences may
reuse one identical local antecedent alteration, one history vertex, and
even one incoming occurrence as a sequential splice handle. They may not
identify or multiply occurrence-labelled de Bruijn edges.

## 1. Coalescing local antecedent alterations

At a component, incidences in one equivalence class have the same start
and the same literal length-d history. They therefore impose identical
values on identical source positions. Applying that assignment once
satisfies every incidence in the class; applying it several times is
literally idempotent.

The simultaneous freedom theorem must be applied to the union of source
positions changed by the distinct classes, not to an incidence multiset.
By hypothesis, those distinct class blocks are disjoint and cyclically
separated by at least one unaltered position. Consequently every connected
component of the changed-position set has length at most d, exactly as in
Section 1 and Section 3 of
`MATH_AUDIT_SEPARATED_MULTI_PORT_COMMON_HISTORY_EULER_FUSION_INDEPENDENT_20260813.md`.
Repeated incidences in one class neither lengthen a changed block nor
remove another forced endpoint. Thus the local antecedent proof remains
valid without a degree bound inside a class.

This conclusion would fail if two incidences shared a start but requested
different literal histories. The theorem explicitly places those
incidences in distinct classes, so their identical physical blocks could
not satisfy the disjoint/separated-class hypothesis. That conflict is
correctly excluded.

## 2. Reusing a de Bruijn history vertex

After local realization, each component source word is a closed walk in
the occurrence-labelled order-d de Bruijn multigraph. Every physical
source position supplies a distinct labelled edge occurrence, even if two
occurrences have the same literal transition.

Literal equality on every component-graph edge means the incident walks
share a de Bruijn vertex. Reusing the same vertex for many incidences is
unproblematic: the disjoint union of all labelled edge occurrences is
still balanced, and connectedness of the component graph makes its union
weakly connected on nonisolated vertices. The standard balanced-connected
criterion therefore already gives an Euler circuit. This proof neither
chooses nor consumes a unique port occurrence for each component-graph
incidence.

## 3. Sequential reuse of one incoming occurrence

The explicit successor-permutation proof is also sound. Let p be one
incoming occurrence ending at a shared history H in the accumulated cycle,
and let q_i be an incoming occurrence ending at H in the next child cycle.
At step i, transpose the two successor values assigned to p and q_i.

Before the swap, p and q_i lie in distinct cycles of the current successor
permutation. A transposition of successor values at two points in distinct
cycles merges those cycles. Both successor edges leave H, so the swapped
successor assignment remains a legal de Bruijn transition assignment.

After the swap, p remains the same single labelled incoming occurrence,
now with the successor formerly assigned to q_i. At the next step, p lies
in the accumulated cycle and has one current successor. Swapping that
current successor with the successor at q_(i+1) again merges two distinct
cycles. Nothing requires restoring p's original successor between steps.

In permutation notation, the handle reuse applies the transpositions

    (p,q_1), (p,q_2), ..., (p,q_t)

to successor values. At every stage the successor map remains a
permutation on the unchanged set of labelled edge occurrences. Hence no
occurrence is duplicated, identified, omitted, or consumed by being used
as a splice handle.

The phrase “reuse the same incoming occurrence” must be read in precisely
this handle sense. It would be false if it meant traversing its labelled
edge multiple times in the final Euler circuit. The theorem does not make
that claim: the final circuit uses every labelled occurrence once.

## 4. Occurrence ledger and short decks

Successor swaps change only which legal outgoing occurrence follows an
incoming occurrence at a shared history vertex. They do not alter any
labelled de Bruijn edge's own literal (d+1)-letter context. An Euler circuit
of the final successor permutation therefore contains exactly the original
occurrence-labelled width-(d+1) deck.

For each shorter width ell<=d, attach an occurrence to its terminal
labelled de Bruijn edge and read the literal suffix of length ell from that
edge's context. This gives the same label-preserving bijection used in the
prior separated-port audit. The complete owner occurrence ledger and every
strict-lower compiler cell whose validity uses only a word of width at most
d consequently transport exactly.

As before, this does not preserve the tuple of constituent physical
source-position identities across a new seam, nor any interval longer than
d+1. It also does not preserve a compiler resource depending on the new
adjacency of two occurrence labels rather than on the literal terminal-edge
context.

## 5. Exact MSW formulation

For a fixed oriented MSW row, a start determines its forced-history
signature. Thus all incidences using the same start and using that forced
signature form one coalesced class. Only the distinct used starts need be
cyclically separated by at least d+1.

This is an exact weakening of distinct-port-per-incidence packing. It does
not show that a global assignment of parent options, component
orientations, and coalesced starts exists. That assignment remains the
finite/global gate isolated by the highest-valley theorem.

## 6. Scope and verdict

The theorem is unconditional under its explicit class-separation and
literal-equality hypotheses. It proves source fusion and occurrence-ledger
preservation through width d+1. It does not prove:

1. existence of a coalesced incidence assignment for all MSW components;
2. any proper-upper or longer source interval;
3. preservation of seam-sensitive occurrence-label adjacency;
4. a final opening cap; or
5. permission to identify two parallel occurrence-labelled edges.

No computation was needed for this audit. The proof is a finite
permutation-cycle argument and agrees with Section 3 of the prior
independent separated-port audit.

The final bytes copied to H100 have SHA-256 digests:

| artifact | SHA-256 |
|---|---|
| coalesced theorem | `be510b37ee380b584706a8ae8e2fbc2d73cec56c4a38d398cfd68749fbcd8789` |
| this audit before adding the present self-hash table | `5165b3bdd77925422b9ed9eeedc9c7ab1a3c59363dbba905ee0ca52f1674fa3a` |
