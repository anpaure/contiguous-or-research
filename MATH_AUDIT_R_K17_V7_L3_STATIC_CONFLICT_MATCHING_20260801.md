# Audit of the k=17 v7 fixed-L3 static conflict matching

Date: 2026-08-01  
Lane: R / independent finite resource audit  
Status: exact lower-bound certificate for the published one-L3-column-per-
target catalogue.  It is not a complete conflict graph and says nothing
against newly generated options.

## 1. Frozen scope

The vertices are the one hundred `L=3` rows of
`scratch/k17_socket_v7_extendable_zero100_compact_sockets_20260801.tsv`.
Guard intervals use the half-open component intervals in
`scratch/k17_min_cut_alternative_provider_atlas_20260801/segments.tsv`.

Two rows are declared adjacent when at least one literal static obstruction
holds:

1. they use a common facet owner;
2. two guard intervals overlap on one component;
3. one guard contains the other row's facet position;
4. one row's required extra cut lies strictly inside the other guard; or
5. after intersecting each row's explicit selected-component option with
   the option domains of its two guards, their allowed sets on a common
   component have empty intersection.

Every listed relation is a necessary incompatibility under the bank
replayer semantics.  Endpoint degree, lower collisions, joint child
providers, graphic cycles, and common-cap rows are omitted, so the audited
graph is only a certified subgraph of the full physical nogood graph.

The resulting scoped graph has `100` edges, maximum degree `8`, and `23`
isolated vertices.  The overlapping category counts are facet `10`, guard
overlap `35`, guard--facet `38`, guard--cut `21`, and incompatible component
state `81`.  The following thirty-seven edges are pairwise
vertex-disjoint:

```text
4059-78911       7667-69110       8060-69612
8170-73434       9726-75738       14190-24366
15996-77434      16058-87290      17663-48910
18414-84939      20403-82931      21751-22206
23499-25565      24467-32023      30193-73586
31418-40874      31831-80370      32141-105893
32391-88719      33775-66558      67439-67451
68589-77485      69246-69342      69355-69363
69533-81081      70650-73688      70847-77103
71327-84879      72677-81797      73395-73635
73529-83833      73652-77748      75230-83422
75737-75749      78558-87751      79722-86507
85790-85957
```

### Theorem 1.1 (fixed-L3 replacement floor)

Every pairwise compatible subfamily of the one hundred frozen L3 columns has
size at most `63`.  Hence any all-one-hundred L3 solution must replace at
least `37` of those specific columns.

#### Proof

The displayed edges form a matching: their seventy-four endpoint labels are
distinct.  An independent set contains at most one endpoint of every
matching edge and at most all twenty-six unmatched vertices, hence has size
at most `37+26=63`. \(\square\)

This proves only a replacement floor.  It does not prove that thirty-seven
new columns suffice.

The independent solver-free reproducer is
`scratch/audit_r_k17_v7_l3_static_conflict_matching_independent_20260801.py`,
with frozen payload
`scratch/r_k17_v7_l3_static_conflict_matching_independent_20260801.audit.json`.
It reads
the frozen atlas plus the exact state/segment tables, reconstructs all five
conflict predicates, checks every displayed matching edge, and asserts the
edge/category/degree counts above.  It does not search or solve a selector.

## 2. Parent-child collision

The frozen `75749/L3` row uses facets

\[
                         74725,67557,10213
\]

and requires component states `557:0,1209:1`.  The same-source integrated
round-one `14309/L3` row uses facets

\[
                         14308,13285,10213
\]

and requires `293:0,557:0`.  They share literal owner `10213`, so these two
individually clean rows do not form a physical regenerative packet.

The disjoint-looking generation-three `14309/L3` row was generated
separately and was not jointly authenticated with the v7 `75749` row.  Its
individual PASS therefore does not certify composition.

## 3. Cut-sharing scope

The one hundred fixed L3 rows use `213` extra-boundary occurrences on `207`
distinct boundary literals.  The six doubles are exactly

```text
684:4    16058/31418   child 80570
1587:6   20403/82931   child 83891
1356:1   32141/81797   child 97669
1182:4   68589/72677   child 101349
3439:1   69355/69363   child 73443
1072:3   73434/73688   child 89816
```

Five paired rows are adjacent in the audited conflict graph;
`32141/81797` is only the one pair not excluded by this static audit.
Therefore any independent subfamily can contain at most one repeated
boundary occurrence, proving

\[
 \left|\bigcup_{p\in S}D^{\rm ext}_p\right|
       \ge\sum_{p\in S}|D^{\rm ext}_p|-1.
\]

The raw sum `213` remains an individual-world diagnostic, not a feasible
joint upper bound.
