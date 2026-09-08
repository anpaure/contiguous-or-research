# `k=17`: standard MMM gluing-tree long-run search

**Date:** 2026-08-02  
**Status:** authenticated scoped negative search result.  The search does not
prove UNSAT for the full family.  It shows that extensive local and distant
sampling of the standard Merino--Micka--Mutze pull/gluing-tree family is far
inferior to the current nonstandard larger-circuit carrier.  The audit covers
only central ownership, rank-eight q1, one-component topology, positive
depth-three residence, and rank-ten q1.  It makes no deeper-upper, source, or
compiler claim.

## 1. Family exposed

For `n=8`, the standard Middle Levels factor has `1430` Dyck-word orbits and
`95` plane-tree components.  The complete standard pull auxiliary multigraph
has

```text
plane-tree vertices                              95
labelled standard pull edges                    427
underlying component pairs                      288
pair multiplicities                    157 x 1, 127 x 2, 4 x 4
edges in one gluing spanning tree                 94
```

The new C++ materialization reconstructs every standard pull hexagon from the
Dyck-word formulas, toggles the selected circuits against the base factor,
and rejects a candidate unless all quotient degrees are two, the quotient is
one cycle, and its voltage is coprime to `17`.  Every accepted lift is then
replayed literally on all `24310` physical rank-nine owners in both shore
orientations.

The primary sources are

```text
scratch/search_k17_mmm_gluing_longrun_lns_20260802.cpp
scratch/search_k17_mmm_full_gluing_tree_lns_20260802.cpp
scratch/search_k17_mmm_random_gluing_trees_20260802.cpp
```

The H100 full-tree campaign used the fresh root

```text
/home/amodo/or15/work/root_k17_mmm_full_gluing_tree_lns_20260802
```

and eight independent `900`-second single-core lanes.  All eight exited zero.
Their raw best tree had

```text
positive depth-three short runs                 6851
rank-ten q1 holes                               2431
```

## 2. Distant random-tree census

To test whether tree-exchange annealing had merely remained near the
canonical spanning tree, four additional `900`-second lanes sampled random
Kruskal spanning trees in the full `427`-label auxiliary multigraph.  They
ran under

```text
/home/amodo/or15/work/root_k17_mmm_random_gluing_trees_20260802.
```

The exact final census is

```text
sampled labelled trees                     73,136,596
valid one-cycle physical lifts                259,554
best positive short runs                        7,259
best rank-ten q1 holes                           2,431
```

All four independent lanes reached exactly `7259/2431`.  This does not prove
a global lower bound, but it shows that distant random standard gluing trees
are worse than the locally optimized basin rather than revealing a hidden
low-defect region.

## 3. Exact parallel-incidence completion

A fixed unlabelled quotient factor can contain parallel incidence labels with
different voltages.  This is a small exact residual question, not another
heuristic search.  The new enumerator

```text
scratch/enumerate_k17_mmm_parallel_voltage_labels_20260802.cpp
```

constructs all `12870` quotient incidence labels, groups them by their two
quotient endpoints, exhausts every parallel-label assignment of each saved
incumbent, and literally re-lifts and scores every coprime-voltage assignment.

For the residence-best raw tree there are five binary pairs.  Of its `32`
assignments, `30` give a single physical cycle.  The exact optimum is

```text
positive depth-three short runs                 6817
rank-ten q1 coverage                     17017 / 19448
rank-ten q1 holes                               2431
```

An independent factor-only verifier checks all `24310` owners, all `24310`
rank-eight intersection colours, one physical component, every positive run,
all `24310` linear cuts, and the complete rank-ten load table.  The best cut
absorbs only two short runs, leaving `6815` internal defects.

The rank-ten Pareto incumbent comes from another raw tree.  Exact enumeration
of its five binary pairs gives

```text
positive depth-three short runs                 6868
rank-ten q1 coverage                     17051 / 19448
rank-ten q1 holes                               2397
best-cut internal short runs                    6866
```

Thus the parallel voltage labels do not conceal a rescue of the standard
tree family.

## 4. Comparison with the nonstandard carrier

The current marker58 larger-circuit carrier has

```text
positive depth-three short runs                 3672
rank-ten q1 holes                                  0
```

The standard-family lex incumbent is therefore worse by

```text
6817 - 3672 = 3145
```

positive defects and also misses `2431` immediate-upper targets.  It is not
retained as a `k=17` seed.

This is the important structural conclusion.  Classical pull hexagons are
enough to join the plane-tree factor cycles, but choosing a different gluing
tree does not provide the freedom needed for long positive coordinate runs
or an exact upper decoration.  The successful branch must use larger
palette-preserving alternating circuits outside the standard pull-tree
parameterization.

## 5. Next construction theorem

The strongest next target suggested by the comparison is the following.

> **Upper-decorated long-run circuit theorem.**  There is a family of larger
> alternating circuits which rethreads an exact owner/rank-eight/rank-ten
> Hamilton factor while preserving both q1 palettes and one-component
> topology, and whose generated safe component contains a chronology in
> which every insertion-to-next-deletion flip gap is at least `2d+1`.
> Moreover, the move family has bounded negative return or a regenerative
> state, so serial repairs do not accumulate residence debt.

The finite marker58 descent is direct evidence for this theorem: it has
already reached `3672` positive defects while retaining rank-ten q1 exactly,
whereas the standard gluing-tree family remains at `6817/2431`.  Deeper upper
shadows, the source factor, and the terminal compiler remain separate gates.

## 6. Frozen artifacts and hashes

The summary audit is

```text
scratch/k17_mmm_standard_gluing_tree_search_20260802.audit.json
SHA-256 4f62790f4a4d0ff5aa8ed3b165455bcacfedaacec221d05d6d3e4de5e7dc494e
```

The residence-best exact completion is frozen at

```text
scratch/k17_mmm_full_gluing_tree_longrun_20260802/lane_333/parallel_best.*
```

with hashes

```text
factor TSV
  ca6cf32b732245f00271913ea16880f9ae05d5a96a629ddbced446f14a372fee
parallel-label audit
  2241f81177e2990fc16fa266ae06f5ebe903c96d063c54936d83cc5ec1b26f85
independent physical audit
  85917314c4decf22864b6fea3c2e076be7d55f8ed81604f7213f7412cd03ee14
```

The independent verifier is

```text
scratch/audit_k17_mmm_gluing_candidate_20260802.cpp
SHA-256 c96630312b8a46f5dd04852082fee76427a8fdd9ec77424c7b6b4ef376ca1884
```

The authoritative status is

```text
PASS_K17_MMM_STANDARD_GLUING_TREE_SEARCH_SCOPED_NEGATIVE.
```

It is deliberately not an UNSAT statement for all standard gluing trees, all
Middle Levels Hamilton cycles, or all equivariant factors.
