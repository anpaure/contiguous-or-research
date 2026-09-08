# Independent audit of the compact four-shadow encoding

## Result

The compact rank-three/rank-nine encoding is **sound, complete, and an exact
existential projection** of the old explicit four-vertex-path encoding.
I found no mathematical or implementation defect.

The conclusion applies to:

* the complete `J(11,6)` candidate graph;
* an arbitrary sparse candidate subgraph;
* a disconnected selected cycle cover during lazy connectivity refinement;
* up-front `quad`/`full` construction; and
* on-demand rank-three/rank-nine target construction.

For a disconnected selected graph, the statement is deliberately only local:
the compact target gate is exactly equivalent to the old local path gate.
Neither gate by itself turns a disconnected cycle cover into a linear
Hamilton path.  The pre-existing connectivity constraints/cuts remain
necessary and are unchanged.

Audited revisions:

```text
7045de28ed2b52230b5e530018275bd33f49b677f28df69ec77c1851b0d24e89  K11_COMPACT_FOUR_SHADOWS.md
c5ebeee20ebd9a3904f02fc3c140b61077d62b3ac7758b5c00cdf299136b0c77  recombine_paths_sat.cpp
0601337348bf1e9637e1999b0edeefe98ebb63f66b119b4488f0fc622b183f11  scratch/verify_k11_compact_four.cpp
```

## 1. Geometry audit

Let `B--C` be the middle edge of a simple four-vertex Johnson path
`A--B--C--D`.  Since `B,C` are adjacent rank-six sets,

```text
|B intersection C| = 5,     |B union C| = 7.
```

### Rank three

If the fourfold intersection is a rank-three set `S`, then

```text
B intersection C = S union {x,y}
```

for two distinct coordinates `x,y`.  A single outer Johnson edge can remove
at most one coordinate from this middle intersection.  Therefore the two
outer edges must remove `x` and `y`, one on each side.  Conversely, if both
outer vertices contain `S` and the two outer edges remove opposite members of
`{x,y}`, their fourfold intersection is exactly `S`.

For fixed `S`, eligible middle vertices correspond to the three-subsets of
the eight coordinates outside `S`.  Their induced graph is `J(8,3)`, so it
has

```text
C(8,3) = 56 vertices,
degree 3*(8-3) = 15,
56*15/2 = 420 edges.
```

For one eligible middle edge and one assigned removal at one endpoint, any
of the five coordinates outside that endpoint can be inserted.  Hence both
support groups have size five.  There are

```text
2 * 5 * 5 = 50
```

explicit paths per middle edge and `420*50 = 21,000` per rank-three target.

### Rank nine

Dually, if the fourfold union is a rank-nine set `U`, then

```text
U minus (B union C) = {x,y}.
```

The two outer edges must add `x` and `y` on opposite sides and may introduce
no coordinate outside `U`.  Conversely these conditions force union `U`.

The middle vertices are the rank-six subsets of `U`, inducing `J(9,6)`:

```text
C(9,6) = 84 vertices,
degree 6*(9-6) = 18,
84*18/2 = 756 edges.
```

For a prescribed added coordinate, any of the six coordinates of the
endpoint may be removed.  Both groups therefore have size six.  This gives

```text
2 * 6 * 6 = 72
```

paths per middle edge and `756*72 = 54,432` per rank-nine target.

### Four distinct vertices

The middle edge itself can never enter an outer support group.  In the lower
case its opposite endpoint still contains both `x,y`; in the upper case it
contains neither missing coordinate.  Thus each outer endpoint differs from
both middle endpoints in the required way.

The two outer endpoints are also distinct.  For the assignment "remove `x`
at `B`, remove `y` at `C`", the `B`-side endpoint retains `y` while the
`C`-side endpoint omits it.  In the upper case, the `B`-side endpoint contains
newly added `x`, while the `C`-side endpoint adds `y` to a set that does not
contain `x`.  Therefore every grouped choice is a simple four-vertex path;
there is no hidden triangle or repeated endpoint.

## 2. Exact existential projection in an arbitrary graph

Fix a target and let `O` be the set of supported assignments.  An assignment
`o` consists of a candidate middle edge `m_o` and two nonempty sets of
candidate outer edges `L_o,R_o`.  The compact clauses are

```text
OR(o in O) z_o,
z_o -> m_o,
z_o -> OR(L_o),
z_o -> OR(R_o).
```

After existentially eliminating the `z_o`, these clauses are true exactly
when

```text
OR(o in O, l in L_o, r in R_o) (m_o AND l AND r)
```

is true.  This is precisely the projection of the old formulation, which
introduced one equivalence variable for every explicit triple of selected
edges and then ORed those variables.  If `O` is empty, both formulations add
an empty target clause.

This proof treats the available edge sets as arbitrary.  Deleting candidate
edges merely shrinks `L_o`, `R_o`, or removes an unsupported assignment.  It
therefore proves exactness in every sparse candidate graph, including one
whose candidate or selected graph is disconnected.  Connectivity and path
orientation play no role in the local equivalence.

Sharing an old explicit-path variable between a rank-three and rank-nine
target does not change this conclusion.  Its reverse Tseitin implication
only determines an auxiliary variable from the edge variables; it places no
additional restriction on the projected edge assignment.  Replacing it by
separate target-specific existential flags preserves the conjunction of all
target-existence requirements.

## 3. Counts

The independently recomputed complete-graph counts are:

| quantity | rank 3 | rank 9 |
|---|---:|---:|
| targets | 165 | 55 |
| eligible middle edges per target | 420 | 756 |
| orientation flags per target | 840 | 1,512 |
| explicit paths per target | 21,000 | 54,432 |

Thus:

```text
eligible target/middle-edge incidences = 165*420 + 55*756 = 110,880
target/path incidences = 165*21,000 + 55*54,432 = 6,458,760
compact variables = 165*840 + 55*1,512 = 221,760
compact clauses = 3*221,760 + 220 = 665,500
```

An edge of `J(11,6)` has 29 non-middle choices at either endpoint.  Of the
`29^2=841` pairs, nine have a repeated outer endpoint, leaving 832 simple
unoriented four-paths with that middle edge.  Therefore the old up-front
implementation made

```text
6,930*832 = 5,765,760 variables
4*5,765,760 + 220 = 23,063,260 clauses.
```

The claimed up-front savings are consequently exactly

```text
5,544,000 variables and 22,397,760 clauses.
```

All arithmetic in the source note is correct.

## 4. Implementation audit

The implementation at `recombine_paths_sat.cpp:955` follows the proved
projection literally:

1. it scans only real candidate middle edges;
2. it checks the exact target containment and two-coordinate difference;
3. it constructs both assignments of those coordinates to the two sides;
4. each support group contains only real candidate edges actually present in
   `incident[center]`;
5. it omits an assignment if either group is empty;
6. it adds exactly the three implications for one fresh flag; and
7. it adds one final OR of all flags.

No converse implication for a flag is needed.  The `desired` computation and
`solver.phase` call in lines `1000--1014` affect only a heuristic polarity;
the phase call adds no clause and cannot change satisfiability.

The dispatch is also correct:

* in `quad` and `full` modes, lines `1077--1094` replace the complete old
  up-front four-path block and mark every rank-three/rank-nine target in
  `target_constrained`;
* otherwise, lines `1179--1198` dispatch a missing or explicitly requested
  target of distance three to the same compact routine;
* `target_constrained` prevents duplicate target clauses when an initial or
  lazy target was already installed;
* rank-three/rank-nine targets are disjoint from the compact pair-shadow
  ranks, so enabling both compact encodings creates no ownership conflict;
* the run, distance, orbit, endpoint, degree, orientation, and connectivity
  encodings are generated independently of the compact flags and remain
  unchanged; and
* the lazy coverage loop requests exactly the rank-three/rank-nine targets
  handled by this routine, while longer missing upper targets continue to
  block the whole candidate path as before.

The diagnostic `eligible_centers` counter is geometric: in a sparse graph it
may count a middle edge even when neither orientation has two nonempty support
groups.  `orientation_gates` is the supported count actually encoded.  This
is only a naming/detail issue in diagnostics and has no logical effect.

## 5. Independent executions

The supplied checker was compiled with

```text
g++ -O3 -std=c++20 scratch/verify_k11_compact_four.cpp
```

and produced:

```text
vertices=462 Johnson_edges=6930
rank3_targets=165 centers_each=420 gates_each=840 explicit_each=21000
rank9_targets=55 centers_each=756 gates_each=1512 explicit_each=54432
target_path_incidences=6458760
target_middle_edge_incidences=110880
old_upfront_path_variables=5765760 old_upfront_path_clauses=23063260
compact_variables=221760 compact_clauses=665500
saved_upfront_variables=5544000 saved_upfront_clauses=22397760
PASS
```

The checker genuinely verifies both directions of the geometric
classification.  For every grouped outer-edge pair it checks distinct outer
vertices and the exact aggregate.  It then brute-enumerates every simple
outer-edge pair at every eligible middle edge and verifies that any exact
target path removes/adds the two different classified coordinates.  Its
five-bit truth table independently checks existential projection of the two
orientation flags.

The checker assumes the complete graph, so its executable alone does not
certify sparse/disconnected behavior; that part is supplied by the arbitrary-
support projection proof in Section 2.  This is a scope distinction, not a
gap in the result.

The modified main source also passed a C++20 syntax build against a minimal
no-op CaDiCaL interface.  Formula initialization on the complete graph
reported

```text
compact_four_shadows=1 centers=110880 orientation_gates=221760
variables=221760 group_edge_occurrences=2383920
```

For on-demand targets `37` (rank three) and `2044` (rank nine), it reported

```text
constrain=37   compact_centers=420 orientation_gates=840
               compact_variables=840 group_edge_occurrences=8400
constrain=2044 compact_centers=756 orientation_gates=1512
               compact_variables=1512 group_edge_occurrences=18144
```

Using only the 461 candidate edges of the supplied score-549 path gave two
compact flags versus two explicit witnesses for target `37`, and six compact
flags versus six explicit witnesses for target `2044`.  This is an additional
sparse-dispatch consistency check; no SAT search was run locally.

## Conclusion

`RECOMBINE_COMPACT_FOUR_SHADOWS=1` is safe to use.  It changes only the
auxiliary representation of rank-three/rank-nine target existence and has
the exact same projected feasible edge assignments as the previous explicit
encoding, with the documented complete-graph reduction in variables and
clauses.
