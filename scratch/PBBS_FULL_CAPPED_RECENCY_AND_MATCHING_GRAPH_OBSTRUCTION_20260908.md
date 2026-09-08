# Full aperture-three PBBS recency routing: complete graph and matching obstruction

2026-09-08. One bounded exact reconstruction on h100 by
`exact_equality_structure`, followed by a bounded read-only classification
of its already exported edge metadata.

**The full D^min(h,3) state inventory admits no nontrivial cyclic
successor reassignment.** Its 4,998 additional neutral edges all point
between original components in an acyclic graph. The stronger
alternative-matching source graph also has only singleton strongly
connected components. This is a different inventory from the native
D^h inventory, which had only 17 extra edges.

This obstruction fixes every full aperture-capped letter and its
periodic recency state. It does not apply to further entrywise caps
E_i subset D_i, such as the separate unrestricted triple-preserving
cap decision. It is not an impossibility theorem for nu(17)=B(17).

## 1. The actual changed inventory

Start from the same original canonical 146 cycles of lower owners A_i
and upper owners X_i. For every cycle with original height h put

    H=min(h,3),
    D_i^H=intersection_(j=0)^H X_(i+j).                 (1.1)

The program reconstructs (1.1). It separately reconstructs D_i^h
and compares only THAT native word to the stored `source_period`.
It verifies D_i^h subset D_i^H; it does not mistakenly require the
changed word to equal the native one on cycles of height above three.

It then reconstructs the actual periodic recency states of D^H,
after one complete warm-up period, and independently replays all
coordinate last-occurrence times. Every state has first-block size
9-H followed by H singleton blocks through rank nine. Its unique
rank-eight and rank-nine prefixes are

    X_i intersect X_(i+1),  and X_i,

respectively. Both prefix maps biject the 24,310 state inventory to
their complete middle layers. The number b_9 of prefixes below
rank nine is exactly H, not the original h.

These shape and prefix identities are checked directly in the run.
Their general source proofs are in
[the capped-aperture interface](PBBS_CAPPED_APERTURE_EXACT_MIDDLE_AND_LOWER_PIN_INTERFACE_20260908.md).

## 2. Why the neutral graph is exhaustive for cyclic routing

The general prefix-count proof in
[the native-routing audit](PBBS_NATIVE_RECENCY_ROUTING_OBSTRUCTION_COMPLETE_AUDIT_20260908.md),
Sections 3–4, applies to this new inventory without change.

For a legal recency update to a different rank-nine state, b_9 cannot
increase. Hence any directed cycle has constant H. For a neutral edge
P->Q, the rank-eight prefix of P is contained in Q's rank-nine prefix.
Every rank-eight prefix appears once, so the nine eight-subsets of
Q's nine-prefix enumerate every possible neutral predecessor. The
self-loop is already one of those nine candidates.

An incoming edge to Q has just one possible letter: Q's first block.
Every candidate of the same H is tested against the complete literal
move-to-front update, not merely its two middle labels. A separate
coordinate-class implementation independently checks each computed
update. Cross-H legal edges are not exhaustively enumerated; the
proved monotonicity already excludes them from cyclic routings.

## 3. Exact graph census

The input is
[height_adaptive_canonical_cycles.json](k17_height_adaptive_20260908/height_adaptive_canonical_cycles.json),
with SHA-256

    fed20c313c639740b089428c1d2b8b572fc7138de4c11c2203be554e4acfa2a3.

The single diagnostic script is
[audit_k17_capped_recency_matching_graph_20260908.py](audit_k17_capped_recency_matching_graph_20260908.py).
It ran once on h100 (`arboghast`) under hard limits of 120 CPU seconds,
150 wall seconds, and 2 GiB address space, completing in approximately
3.71 seconds. No mathematical code ran locally and no alternative
source, cap choice, or anchor frame was tried.

| Quantity | Count |
|---|---:|
| Original components | 146 |
| Actual D^min(h,3) periodic states | 24,310 |
| All nine-subset predecessor candidates | 218,790 |
| Unequal-H candidates discarded | 22,066 |
| Complete neutral candidates tested | 196,724 |
| Rejected neutral candidates | 143,106 |
| Legal neutral edges | 53,618 |
| Native successor edges of this changed source | 24,310 |
| Physical self-loops | 24,310 |
| Extra same-component edges | 0 |
| Cross-component edges | 4,998 |

The quotient on the original 146 components has no nontrivial
strongly connected component. Every original component is therefore
its own SCC. The SCC result is checked independently of the producer
algorithm: each claimed SCC has both forward and backward reachability
from one vertex, and the condensation graph passes an acyclicity test.

As in the native inventory, a cyclic permutation cannot cross this
component DAG. Its only internal edges are the original successor
and self-loop edges. A permutation must select either the whole
original component cycle or self-loops at every vertex of that
component. Thus its minimum component count remains 146, and the
loop-free routing is unique.

## 4. The stronger source matching graph was also checked

A cycle in a component quotient alone would not certify a valid
successor permutation: the incoming and outgoing cut states of a
component need not match. The diagnostic therefore also constructs
the exact alternative-matching graph on SOURCE STATES.

Let f be the original successor permutation of the changed D^H
inventory. For every legal neutral edge P->Q with P!=Q, include
the source arc

    P -> f^(-1)(Q).                                    (4.1)

Physical recency self-loops are excluded. Original successor edges
become identity arcs P->P in this new graph.

If distinct source vertices P_0,...,P_(t-1) form a nontrivial directed
cycle in (4.1), assigning

    P_i -> f(P_(i+1 modulo t))                          (4.2)

and retaining all other original successors gives an actual legal
permutation. The new destinations are exactly a permutation of the
old cut destinations. If the t cut states lie in distinct original
components, this operation merges those t cycles into one. If cuts
repeat a component, component reduction is not automatic and the
new permutation must be explicitly decomposed and checked.

There is a converse useful here. For any legal loop-free successor
permutation g, the map pi=f^(-1) composed with g is a permutation
whose arcs all belong to (4.1). If pi differs from the identity,
its cycle decomposition contains a nontrivial directed cycle in the
source matching graph. Therefore an acyclic source graph after
discarding its identity arcs proves uniqueness of the original
loop-free successor assignment.

The complete source graph has 24,310 identity arcs and 4,998 other
arcs, with exactly 24,310 singleton SCCs. Its SCC certificate is
again independently checked by mutual reachability and an acyclic
condensation. Thus there is no nontrivial source cycle to export or
reassign. No candidate permutation or fused literal word was produced.

The program would, had such a cycle existed, have replayed the new
successor permutation and the literal periodic states of each
resulting component. The latter check matters: an abstract closed
recency-state walk can retain stale coordinates never emitted on
that walk. For a genuine merger of whole original components the
full-ground letter unions exclude this issue, but arbitrary cycle
splits require an explicit replay. No unexecuted positive result
from that conditional branch is claimed.

## 5. A finite hint about the direction of the new edges

A separate metadata-only read grouped the already saved 4,998
cross-component state edges by ORIGINAL native height h, as distinct
from their common current value H=3. It found:

| Original source h | Original destination h | State edges |
|---:|---:|---:|
| 3 | 3 | 17 |
| 3 | 4 | 17 |
| 4 | 4 | 170 |
| 4 | 5 | 2,074 |
| 5 | 5 | 136 |
| 5 | 6 | 1,819 |
| 6 | 6 | 17 |
| 6 | 7 | 663 |
| 7 | 8 | 85 |

Thus original height never DECREASES along these saved cross edges.
There are 340 equal-height state edges, supported on 18 component
arcs; all other 4,658 edges raise the original height by exactly one.
The equal-height subgraph remains acyclic by the full SCC certificate.

This is an exact observation about the k17 output, not a proved
all-dimension invariant or a theorem about arbitrary capped letters.
It suggests that a finer profile ordering may explain the DAG, but
no such profile claim is assumed in the obstruction proof.

The classification reads only the graph's existing component heights
and edge multiplicities. It does not reconstruct or search the graph.
It was performed on h100 with 5 CPU seconds, 10 wall seconds, and
128 MiB address space allowed, and is saved as
[cross_edges_by_original_height.json](k17_capped_recency_matching_graph_20260908/cross_edges_by_original_height.json).

## 6. Complete saved artifacts and exact scope

Local directory:
[k17_capped_recency_matching_graph_20260908](k17_capped_recency_matching_graph_20260908/).

* [Complete certificate](k17_capped_recency_matching_graph_20260908/capped_recency_matching_certificate.json).
* [Every changed periodic state](k17_capped_recency_matching_graph_20260908/capped_periodic_states.json).
* [Every neutral candidate, accepted or rejected](k17_capped_recency_matching_graph_20260908/complete_neutral_candidates.csv).
* [Every legal neutral recency edge](k17_capped_recency_matching_graph_20260908/complete_neutral_legal_edges.csv).
* [Component quotient, all cross edges, and SCCs](k17_capped_recency_matching_graph_20260908/capped_neutral_component_quotient.json).
* [Every alternative-matching source arc](k17_capped_recency_matching_graph_20260908/complete_alternative_matching_arcs.csv).
* [Full source SCC partition and empty candidate cycle](k17_capped_recency_matching_graph_20260908/capped_alternative_matching_scc_and_cycle.json).

The legal recency-edge CSV has SHA-256

    ecbdb44113fb7a35067d3447683fc4498d21186b2ab1261b6363e9e034c1221f,

and the complete alternative-matching arc CSV has SHA-256

    779f81d655b68de17fc5be946734d18f996a9c55b9eff616c117e916f593ea5a.

The report records all primary artifact hashes and sizes. Remote
files remain in

    h100:/home/amodo/exact-b-k17-capped-recency-matching-20260908/

The conclusion fixes the recency inventory of the full source D^H.
Changing optional coordinate bits creates different recency states
and falls outside this graph. In particular this result neither
certifies nor refutes the separate
[unrestricted overlapping-cap formula](PBBS_UNRESTRICTED_TRIPLE_CAPS_COMPLETE_CNF_AND_SPARSE_RUN_CLAUSES_20260908.md).
