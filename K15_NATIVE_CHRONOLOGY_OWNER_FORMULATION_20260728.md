# k=15 native chronology + compact one-owner formulation

Date: 2026-07-28

This note freezes the mathematical model implemented by the native search
pipeline.  It distinguishes the genuinely hard coupled constraints from the
parts that are just bipartite matching and therefore have an exact Hall/TU
description.

## 1. Canonical five-parent directed graph

Let `V` be the 6435 middle masks of rank 8 in `[15]`.  From the five
SHA-locked parent certificates, retain every directed consecutive pair.  This
gives a directed graph

```
|V| = 6435,       |A| = 23628.
```

Each arc `a=(u,v)` carries a five-bit support mask.  Bit zero says that the arc
belongs to the Hall-29 reference path.  The reference endpoints are fixed:

```
start = 1519,     end = 1186
```

where these are indices in the sorted middle-mask catalogue.

For a radius bound `B`, the primary variables are `x_a in {0,1}` and the
constraints are

```
sum_{a enters v} x_a = 1       (v != start),
sum_{a enters start} x_a = 0,
sum_{a leaves v} x_a = 1       (v != end),
sum_{a leaves end} x_a = 0,
sum_{a not in Hall-29} x_a <= B.
```

The degree equations alone describe one start-to-end path together with any
number of directed cycles.  Connectivity is imposed without a quadratic
subtour family.  Give each vertex a 13-bit rank `p_v`, fix

```
p_start = 0,      p_end = 6434,
```

and guard `p_v = p_u + 1 (mod 8192)` by every selected arc `(u,v)`.

### Connectivity lemma

The selected arcs form exactly one Hamilton path from `start` to `end`.

Proof.  The degree equations give a start-to-end path and disjoint directed
cycles.  Along every selected arc the rank increases by one modulo 8192.  A
selected cycle would therefore have length divisible by 8192, impossible on
6435 vertices.  Hence no cycle exists.  The unique path consequently contains
all vertices.  Its endpoint rank is 6434, as fixed.  QED.

This is an exact formulation, not a relaxation.  The power-of-two modulus is
chosen only so the incrementer is a small ripple circuit.

## 2. Chronology-to-compiler state-space reduction

For path position `p` and coordinate `j`, let

```
B[p,j] = 1 iff coordinate j belongs to the middle mask at position p.
```

The depth-three erosion variables needed by the compiler are

```
Q[p,j] = B[p,j] & B[p-1,j] & B[p-2,j] & B[p-3,j]
```

with the audited clipped boundary convention.  A dense inverse-permutation
channel is unnecessary.  Anchor every physical compiler cell at its first
middle vertex rather than at its unknown numerical position.

For each vertex `v` and coordinate `j`, propagate along the uniquely selected
incoming arc the intersections of the last at most two, three, and four
middle masks.  The third layer is the erosion mask `Q(v)`.  Similarly,
propagate along the uniquely selected outgoing arc `Q` one, two, and three
steps into the future.  Store the preceding `Q` and the two predicates
``position(v)<=1`` and ``position(v)<=2``.  These are all local guarded
recurrences on selected arcs.

### Arc-propagation lemma

On the selected Hamilton path, the vertex-indexed recurrence gives exactly
the same erosion word, future masks, previous mask, and left-boundary flags as
the position-indexed definition.

Proof.  Induct from the fixed start along the unique selected successor.
At the start, all three prefix layers equal its middle mask, which is exactly
the clipped left boundary.  If the claim holds at a predecessor, intersecting
with the current fixed middle mask gives the last-two, last-three, and
last-four intersections at the current vertex.  The outgoing recurrence is
the same induction backwards from the fixed end.  At the end, the three
synthetic right-collar masks are respectively the last-three, last-two, and
last-one intersections.  The saturated start-distance recurrence gives
precisely the two exceptional left-boundary predicates.  QED.

### Anchored-cell lemma

Replacing a physical cell label `(depth,start-position)` by
`(depth,start-vertex)` preserves cell distinctness and the abstract cell
catalogue for a fixed chronology.

Proof.  A Hamilton path visits each middle vertex exactly once, so
start-position to start-vertex is a bijection.  For each fixed depth there is
exactly one physical compiler cell starting at that vertex.  The cell's fit
depends only on its local `Q` window, preceding `Q`, following `Q`, and whether
it touches the clipped left boundary; all are supplied exactly by the
arc-propagation lemma.  Thus neither cell equality nor freshly recomputed
target/cell incidence uses the absolute numerical position.  The six right-collar cells are handled
separately, and fixed endpoints make their three masks literal functions of
the selected end.  QED.

There is an important architecture convention here.  The compact Hall-29
payload was originally indexed by Hall-29 ordinal positions.  The native arc
model transports each such label to the Hall-29 start vertex and lets the cell
follow that vertex under reordering.  This **H29-anchor-transported** frozen
architecture is legitimate and its cells remain distinct, but it is not the
same restriction as keeping the frozen label at ordinal position `s` in every
new chronology.  Neither restriction obviously contains the other.  All
UNSAT statements below refer only to the anchor-transported convention.

This is the production state-space reduction.  It has
`O(Wk + |A|k)` guarded clauses and no permutation-routing symmetry.

For comparison, `scratch/k15_benes_q_cnf.cpp` implements a fully general,
proof-safe fallback: a padded 8192-wire Beneš record network carries current
mask, selected-successor mask, and end flag, then emits the dense `Q` table.
It is exact, but it emits 22.36 million extension clauses and its radius-zero
SAT regression timed out at 300 seconds.  The anchored formulation proves
that this machinery is mathematically redundant for the compiler.

## 3. Compact one-owner compiler

The audited Hall-29 Dulmage--Mendelsohn shore contains 1524 targets.  Exact
degree-one peeling gives

```
1489 frozen target/cell owner pairs,
35 residual targets,
4057 retained residual options,
3183 distinct residual-option cells,
4672 referenced cells in total.
```

The architecture is sufficient-only: SAT gives an explicit matching of the
entire 1524-target shore, while UNSAT rules out only this frozen peeled
architecture.

A cell is `(depth,start)` with depth 0, 1, or 2.  For a fixed target mask `T`,
exact fit is the conjunction of:

1. every positive coordinate of `T` occurs in the cell envelope;
2. every coordinate forced by a source occurrence and its boundary blockers
   belongs to `T`;
3. every physical `Q` position in the cell meets `T`.

The native emitter expands these statements directly into guarded clauses.
Frozen owners have no guard.  A residual option has a claim literal.  Claims
are exactly one per residual target and at most one per cell.

The key normalization established by the k=11 and k=13 certificates is that a
local definition needs at most one owner: at source `p`, its governing mask is
either the whole middle owner `P_p` or `P_p intersect X` for one chosen target
owner `X`.  This is the mathematical reason the peeled architecture is small;
it is not merely a coding heuristic.

## 4. Hall and total-unimodularity boundary

Several pieces of the problem are exact network/matching problems.

* With a fixed chronology (hence fixed `Q`), precompute which target/cell
  pairs fit.  Selecting distinct cells for all targets is ordinary bipartite
  matching.  Its incidence matrix is totally unimodular, its LP is integral,
  and Hall deficiency is the exact obstruction.
* Degree-one peeling of this graph is exact: a uniquely available cell is
  forced in every saturating matching, unless several live leaves collide on
  that cell.  Removing a noncolliding forced pair preserves feasibility and
  deficiency.
* The raw directed in/out equations for chronology are an assignment/network
  system and are integral, but they permit subtours.

The coupled search is not TU.  Connectivity ranks, the foreign-arc budget,
the arc-propagated chronology channel, and the Boolean cell-fit clauses couple the
assignment and matching polytopes.  Hall solves the compiler after chronology
is fixed; it does not solve chronology plus compiler simultaneously.  This is
the precise boundary between the easy flow part and the current SAT problem.

The cell family is interval-structured (only windows of length at most three),
but target masks couple all 15 coordinates.  No consecutive-ones/TU theorem
currently applies to the full dynamic fit matrix.  A useful future theorem
would show that, after the one-owner normalization, the residual 35-target
matrix remains an interval bigraph under bounded-radius segment moves.  That
would replace the residual SAT layer by Hall flow, but it is not presently
proved.

## 5. Native regressions and exact scope

The radius-zero base instance has

```
281028 variables
1304992 clauses
3640446 literal occurrences
```

Kissat on the remote CPU returned SAT in 0.24 seconds using 99 MB.  An
independent decoder verified:

```
6434 selected arcs
0 foreign arcs
6435 distinct vertices on the start-to-end path
0 position-map discrepancies
```

Thus the native chronology core reproduces Hall-29 exactly before the compiler
channel is attached.

The production arc-propagated owner composition has:

```
base variables             281028
channel variables          553408
final variables            842541
base clauses              1304992
extension clauses         3654913
final clauses             4959905
final CNF size              105 MB
native emission              0.70 s, 9.7 MB RSS
```

At radius zero, Kissat returned the expected UNSAT in 0.42 seconds using
132 MB.  This matches the independently known fact that the frozen Hall-29
peeled architecture cannot saturate its shore.

Finally, removing the foreign-arc bound entirely gives 842541 variables and
4942711 clauses.  Kissat returned UNSAT in 37.79 seconds using 491 MB.
Therefore **no Hamilton path in the complete five-parent directed union can
satisfy this particular H29-anchor-transported frozen 1489+35 peeled one-owner
architecture**.  There are no residence or upper-shadow constraints in this
CNF; the negative result already occurs at the lower compiler interface.
This is a strong and exact negative result about the architecture, not about
the original k=15 conjecture.  An ordinal-position architecture, a different
owner transport, changing a frozen owner, admitting defect-two residual
options, or enlarging the parent union all remain outside its scope.

### Independent channel and proof checks

The corrected radius-zero channel-only CNF was SAT in 0.50 seconds.  An
independent decoder checked every one of 32178 erosion/next/previous/tail mask
rows and all 19305 early-boundary bits against the literal Hall-29 word:
zero discrepancies.

This audit caught and invalidated an earlier emitter version in which the two
start-distance layers were allocated in one numeric-vertex pass.  That version
mis-set two `early0` bits and overconstrained the model.  Its results and DRAT
proof are quarantined under
`scratch/invalid_buggy_early0_arc_channel_20260728/` and must not be cited.

For the corrected unbounded CNF, Kissat emitted an ASCII DRAT proof in
38.35 seconds.  `drat-trim` independently returned `s VERIFIED` in 21.85
seconds.  The verified core contains 9259 original clauses, 5389 lemmas, and
23408 resolution steps.  The compressed proof remains retained on the H100;
the local workspace retains its SHA-256, checker log, exact command inputs,
and the independently checked source hash.

## 6. Port inventory

### Native and performance-critical

1. Five-parent successor/radius/Hamilton emission: **ported and validated** in
   `scratch/k15_native_successor_radius_cnf.cpp`.
2. Exact dynamic chronology -> erosion/cell channel plus compact fixed-mask
   owner clauses and residual matching: **ported and validated** in
   `scratch/k15_arc_owner_cnf.cpp`.
3. General dense position-indexed fallback: **ported but retired from the
   production lane** in `scratch/k15_benes_q_cnf.cpp`.

### Python models that should not be mechanically ported

* `scratch/search_k15_global_compact_owner_radius.py` built 58--76 GB Python
  CP-SAT objects before solving.  It is explicitly superseded by items 1--2
  above; do not relaunch it.
* `scratch/search_k15_global_a29_bounded_exact*.py` reached about 102 GB and
  returned UNKNOWN.  Its monolithic all-cell channel is superseded, not a
  candidate for a line-for-line C++ port.
* The large global branches in
  `scratch/search_k15_directed_parent_union_cpsat_v2.py` are the historical
  prototype.  They and the Python arc-propagation prototype are retained as
  semantic reference tests only, not as production search builders.

### Python that should remain Python

* deterministic JSON/flat serialization and SHA provenance;
* Hall/DM audits, leaf peeling, defect atlases, and clause-count reports;
* SAT-model decoding and final certificate verification;
* small k=11/k=13 fixed-carrier calibration.

These scripts are linear or sparse orchestration/audit code.  Porting them
would not improve the search bottleneck and would make proof provenance harder
to inspect.

## 7. Frozen artifacts and hashes

```
scratch/export_k15_native_union_flat.py
  d13a3e3c15d5d57dd5866dc6110afc831b7d9cb058b73d56db1494b7f965a138
scratch/k15_native_successor_radius_cnf.cpp
  075665ef48358428b79ff342d3fd8ec2eae1eacd6cafb2b6b035bf05f2db5e6f
scratch/k15_arc_owner_cnf.cpp
  81dc4436386b060b2844b777b79baee9ebd6e94744e54943dd5fc0b54fa74a0a
scratch/k15_benes_q_cnf.cpp
  1f7e6f91780de20233bcb6175bc1b4c07e1b0df541e73e99f5d4a1dd5723cab8
scratch/k15_h29_one_owner.flat
  9a9edd9c8d55b9a551b03cc1437476cc29dd4fb6cff8bbc8fee52e7a5f6d2dc6
scratch/k15_h29_one_owner_cia_audit.json
  721a67896e5f992945cb0adabcb47fff94cdfe1c2d993b347270b03a1b7f35f4
scratch/k15_native_union.flat
  2b4fbfdbe1a6c606c4edf7ceba6b9b3a3224906911f5c92855ecdfe30367904f
scratch/k15_radius0_base.cnf
  2dd3e7d8b7cea4af61e649d978a6b887d4541e6b7791ac80dbe34faf05a7211c
scratch/k15_radius0_pos.map
  6d8d30a710e8da8c89087b9c78ad07f8160420810670df5d0f84eec05615a609
scratch/k15_radius0_arc.map
  6fcc9579a45500a68ff42d9000a775e21bda4f42868592e59b391f717e45ac99
scratch/audit_k15_arc_channel_model.py
  24020721c482455113ffadc8323e696a98ea5db5207c3a76bce40e77e31ee879
scratch/k15_radius0_arc_channel_fixed.audit.json
  c31092f169233c95f4f78f574e78d7fdbd602b800586e3385e479989035e70db
corrected unbounded CNF (remote)
  e688f2123df6e89cbb14a33d1d09811d6b33c7f0001b8036d51d5ff98440be03
corrected ASCII DRAT proof (remote, before compression)
  7727fc221331c1a18192d1332551167fe093446e2af8993abf3209ad6a7369f6
corrected compressed DRAT proof (remote)
  e5d8d6534811a4c55a265d7dcb444b73a3d9b2ed44ae6e9683527c38721c63a9
scratch/k15_unbounded_arc_owner_fixed.proof.solve
  bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162
scratch/k15_unbounded_arc_owner_fixed.drat_check.log
  4a69aefc6757ab38f73368cac6e1fecb560ed747b7300d5b07dfdd28a69b1046
scratch/k15_unbounded_arc_owner_fixed.drat_check.time
  61fe4decde1f398232d47cd1fcea103534634b5368eef05b682e4a8d226821c6
```

The five canonical parent SHA-256 values are embedded in the serializer and
must all match before it emits a union payload.
