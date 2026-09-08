# Order-free two-corridor completion as a prescribed-arc Hamilton problem

**Date:** 2026-08-02  
**Lane:** root continuation of the prospective new-phase Boolean-hex reduction  
**Status:** exact graph-theoretic reduction.  Robust Hamiltonicity of the
accepted literal state graph is not claimed.

## 0. Motivation

For one fixed pair of forward total orders, the two-corridor split table has
tight suffix shores.  Therefore a theorem demanding positive Hall surplus in
every frozen order is false.  This does not obstruct the prospective
new-phase construction: the two orders are witnesses and may be chosen after
the literal history/resource filtering.

The order-free object is simply a Hamilton cycle through two prescribed arcs.

## 1. Contracted accepted state graph

Use the physical/non-equivariant notation of
`MATH_THEOREM_ROOT_PROSPECTIVE_NEW_PHASE_BOOLEAN_HEX_TWO_CORRIDOR_REDUCTION_20260802.md`.
The prescribed new Boolean-hex phase is

\[
 A_b\to F,\qquad C_{bc}\to B_{bc},\qquad E\to D_c,
\]

and the opened pump path is \(P_3:F\leadsto E\).

Contract the fixed composite path

\[
             A_b\to F\xrightarrow{P_3}E\to D_c       \tag{1.1}
\]

to one directed protected arc

\[
                         g_2:A_b\to D_c.              \tag{1.2}
\]

All internal physical fragments of `P_3` are removed from the residual vertex
bank.  The protected arc `g_2` carries the complete cumulative ledger of
`A_b->F`, every internal owner/arc of `P_3`, and `E->D_c`, including its
history boundary, private resources and integer/residue voltage.  This
prevents a later state copy from reusing any internal pump fragment or token.

Retain the other fixed new-phase arc

\[
                         g_1:C_{bc}\to B_{bc}.        \tag{1.3}
\]

Let `G_acc` be the literal directed fragment/state graph after all remaining
owner, palette, occurrence, history, upper-ticket and capacity filters have
been imposed.  Each physical residual fragment has an admissible state fibre.
A valid chronology must select exactly one state from each such fibre.
Parallel literal joins may be represented as parallel arcs or by a state
subdivision, but every shared capacity must be enforced by one genuinely
global/cumulative state expansion; independent local filtering is not enough.
No projection which forgets a capacity row is allowed.

## 2. Prescribed-arc equivalence

### Theorem 2.1

The following are equivalent.

1. The prospective new-phase construction has two vertex-disjoint residual
   corridors

   \[
     Q_1:D_c\leadsto C_{bc},\qquad
     Q_2:B_{bc}\leadsto A_b                         \tag{2.1}
   \]

   whose interiors cover every residual fragment exactly once.
2. `G_acc+{g_1,g_2}` has a directed partition-Hamilton cycle containing both
   prescribed arcs `g_1,g_2`: it selects exactly one state vertex from each
   physical-fragment fibre and visits all selected vertices once.

   On a face where one globally compatible state has already been selected
   for each physical fragment, this is an ordinary directed Hamilton cycle.

#### Proof

Given (2.1), retain the unique literal state used by each corridor fragment
and concatenate

\[
 A_b\xrightarrow{g_2}D_c
 \xrightarrow{Q_1}C_{bc}
 \xrightarrow{g_1}B_{bc}
 \xrightarrow{Q_2}A_b.                              \tag{2.2}
\]

The disjoint-cover hypothesis makes (2.2) a Hamilton cycle containing both
fixed arcs.

Conversely, delete `g_1,g_2` from a partition-Hamilton cycle containing them.
Exactly one state of every physical residual fragment was selected.  Every
remaining vertex has indegree and outdegree at most one.  The deletion makes
exactly the roots `D_c,B_bc` lose their selected incoming arcs and exactly the
sinks `C_bc,A_b` lose their selected outgoing arcs.  Hence the remainder is
the two paths in (2.1).  A crossed pairing would close a component before one
of the prescribed arcs and cannot arise from the stated Hamilton cycle.
\(\square\)

Expanding (1.1) converts the contracted Hamilton cycle back to the physical
cycle

\[
 A_b\to F\xrightarrow{P_3}E\to D_c
 \xrightarrow{Q_1}C_{bc}\to B_{bc}
 \xrightarrow{Q_2}A_b.
\]

## 3. Contraction formulation

Assume the endpoints of `g_1,g_2` are all distinct and neither prescribed arc
is a loop.  Contract each `g_i` to a marked supervertex, retaining the ordered
incoming/outgoing state at that supervertex.  Then a partition-Hamilton cycle
through both `g_i` is equivalent to a partition-Hamilton cycle of the
contracted accepted graph which uses the compatible marked states.  The two
endpoint fibres of each forced arc are replaced by its one marked contracted
fibre.

Here “contract” is directional and forced-arc aware.  For `g:u->v`, retain
at the marked supervertex only arcs entering `u` and arcs leaving `v`.
Discard arcs entering `v` or leaving `u`, since a Hamilton cycle containing
`g` has already used the unique incoming role of `v` and the unique outgoing
role of `u`.  The marked state carries the union of the two endpoint resource
ledgers with the contribution of `g` included exactly once.  With this
definition, expansion of the supervertex uniquely restores `u->v`.

This is a graph contraction, not an untyped owner contraction.  If two literal
endpoint states have different histories, private tokens, or residual
capacities, they remain different marked states after contraction.

## 4. Exact sufficient interface

Any theorem implying that the contracted accepted state graph is
partition-Hamiltonian therefore closes the topology row.  Useful sufficient
forms include:

* partition-Hamiltonicity after every admissible contraction of the two
  protected arcs;
* partition-Hamilton-connectedness with the four boundary states prescribed;
* a directed robust-expander theorem stable under the `O(d)` protected bank;
* an explicit cycle factor plus alternating-cycle mergers which never delete
  either marked supervertex state.

Once such a cycle is found, its cyclic order induces the two forward
orders used by the block-diagonal Hall certificate.  Thus the fixed-order
Hall theorem remains a fail-closed verifier, but positive Hall surplus in all
orders is not a necessary construction hypothesis.

## 5. Scope

The theorem solves no expansion row by itself.  In particular, ordinary
strong connectivity, one perfect split-table matching, and untyped Johnson
adjacency do not imply a partition-Hamilton cycle through the marked arcs.
An ordinary Hamilton cycle on a graph containing every admissible state copy
is the wrong object: it visits multiple copies of the same physical fragment.
The accepted graph must retain literal history/resource states and the
one-per-fibre constraint, and the residual integer
background-charge and downstream upper/source/compiler/regeneration rows
remain separate unless included in those states.

The gain is a sharper target:

> prove protected partition-Hamiltonicity of one accepted Boolean state graph,
> rather than robust Hall slack for every arbitrarily frozen total order.
