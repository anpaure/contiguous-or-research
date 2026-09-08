# K17 `s=1` forced-direct theorem and residual factor gate

Date: 2026-07-31  
Verdict: **GO** for the exact 572-ear forced-direct layer and for a
capacity-respecting selection of all 8,164 remaining unique-colour edges.
The simplest
remaining scalar schedule is exactly

\[
   x_1=572,\qquad x_4=2637,\qquad x_5=430,               \tag{0.1}
\]

where `x_l` denotes the number of joining ears with `l` new edges.  Two
independently generated certificates realize all 572 direct ears with fresh
rank-eight and rank-nine colours and without sharing a base endpoint.  The
remaining 8,164 unique rank-six colours admit a simultaneous fresh-rank-eight,
base-cap-one, unused-cap-two, boundary-rank-nine-injective selection.  That
particular selection is not yet an ear packing: it has 17 illegal central
wedges and 1,764 central rank-nine collision units.  The unresolved object is
now a joint wedge-clean reselection plus a coloured 3/4-internal-vertex ear
factor carrying the 4,534 rank-five repeat decorations.

No tail, prefix, or length-24313 word is claimed.

## 1. Exactly 572 lower colours force direct ears

For the `s=1` seed, the base forest is a matching of 3,640 rank-eight-rainbow
edges on 7,280 rank-seven vertices.  Call those vertices `B`; the other
12,168 rank-seven vertices are `U`.

The greatest-supported-edge calculation gives 8,736 missing rank-six rows.
Delete every candidate provider edge whose endpoints both lie in `B`.  The
exact residual degree distribution begins with

```text
degree 0: 572 rows.
```

Thus 572 missing rank-six colours have no supported `B-U` or `U-U`
provider.  Their complete `B-B` catalogue has

```text
rows                              572
candidate incidences             3,861
fresh rank-eight colours         1,001
base endpoints                   1,573
row-degree histogram             3:42, 4:42, 5:45,
                                 6:56, 7:90, 8:297.
```

The 572 masks have a simple common normal form: coordinate 0 is present,
coordinates 1,2,3,4 are absent, and `p_0=p_1=1`.

Every actual clean ear is contained in the greatest postfixed support set.
Hence each of these 572 colours must occur on a `B-B` edge.  A base vertex
already has degree one, so it can accept at most one new edge; consequently
a `B-B` edge cannot be internal to a longer ear.  It is necessarily a
one-edge ear.  Therefore

\[
              x_1\ge 572.                                \tag{1.1}
\]

This is stronger than a scalar row count: it is an arbitrary-ear lower
bound on the immutable `s=1` seed.

## 2. The direct floor is simultaneously realizable

A deterministic minimum-remaining-values construction selects one provider
for each exceptional row while imposing all of the following simultaneously:

1. all 572 rank-six colours are distinct;
2. all 572 rank-eight edge unions are fresh and distinct;
3. all 1,144 base endpoints are distinct;
4. the two boundary rank-nine turns per direct ear are fresh and globally
   distinct, giving 1,144 turn colours;
5. the 572 edges are acyclic in the quotient on the 3,640 base components.

The quotient therefore has exactly

\[
 3640-572=3068                                             \tag{2.1}
\]

components after this layer.  A completely separate selection and replay
produces the same counts with a different certificate hash.  Thus the local
forced-direct floor (1.1) is sharp.

This does not logically prove that a *complete* solution uses only 572
direct ears: the residual global factor could force extra direct joins.  It
does prove that no rank-eight, endpoint, rank-nine, or quotient-cycle
obstruction forces such an increase at the exceptional layer itself.

## 3. The exact adjacent-length residual ledger

The final carrier tail is a path on 16,911 rank-seven vertices.  Starting
from the `s=1` matching, it needs 9,631 inserted vertices and 3,639 joining
ears.  After fixing the 572 direct ears, 3,067 ears remain.

If these residual ears use the two adjacent internal sizes three and four
(edge lengths four and five), their counts are forced by

\[
 x_4+x_5=3067,\qquad 3x_4+4x_5=9631.                    \tag{3.1}
\]

The unique solution is

\[
 x_4=2637,\qquad x_5=430.                                \tag{3.2}
\]

Every scalar row then closes exactly:

```text
all ears                     572 + 2637 + 430 = 3639
inserted U vertices          3(2637) + 4(430) = 9631
new carrier edges            572 + 4(2637) + 5(430) = 13270
new carrier turns            2(572) + 5(2637) + 6(430) = 16909
residual B-U edges           2(2637+430) = 6134
residual U-U edges           2(2637)+3(430) = 6564
free B endpoints             7280 - 2(572) = 6136
B endpoints used later       2(3067) = 6134
final path endpoints         2.
```

The 12,698 residual edges split as

\[
 12698=8164+4534,                                           \tag{3.3}
\]

where 8,164 edges carry every remaining missing rank-six colour once and
4,534 are the repeat slots that must be decorated by distinct rank-five
targets.  After removing the certified direct-ear resources, the ordinary
8,164-row lower-to-fresh-rank-eight graph still has

```text
249,477 incidences, zero zero-rows, matching rank 8,164/8,164.
```

This last statement is only a palette Hall check.  It does not impose the
rank-seven capacities or compatible turn wedges.

There is one useful exact type row.  Among the 8,164 unique-colour demands,
3,640 have only `U-U` providers, 1,001 have only `B-U` providers, and 3,523
have both types.  If `b` unique colours are ultimately put on `B-U` edges,
then the repeat slots must split as

\[
 \operatorname{rep}_{BU}=6134-b,\qquad
 \operatorname{rep}_{UU}=b-1600.                         \tag{3.4}
\]

Thus the exact scalar interval is

\[
                  1600\le b\le4524.                     \tag{3.5}
\]

It has ample room, but it should be imposed explicitly in a residual master.

### 3.1 The residual capacity row is feasible

An exact CP-SAT selection, followed by a dependency-free replay, chooses all
8,164 unique-colour edges with:

```text
fresh rank-eight colours                 8,164
B-U / U-U edges                       3,065 / 5,099
remaining base endpoint degrees       0:3,071, 1:3,065
unused rank-seven degrees              0:4,416, 1:2,241, 2:5,511
boundary rank-nine colours,
including the direct layer               4,209, all distinct.
```

The exact repeat filler required around this state is therefore

```text
additional previously unused U vertices    1,879
repeat B-U edges                            3,069
repeat U-U edges                            1,465
repeat edges total                          4,534.
```

So the rank-eight and vertex-capacity correlation is not an obstruction.
However, inspecting the already degree-two unused vertices finds 17
incompatible wedges, 1,503 repeated central rank-nine units, and 261 central
rank-nine values colliding with the boundary bank.  These 1,764 collision
units are immutable if the selected unique-edge set is frozen.  The next
master must therefore reselect unique providers while imposing central-wedge
legality and global central rank-nine injectivity; adding repeat edges after
the fact cannot repair those saturated vertices.

## 4. Exact residual factor formulation

Let `C_1,...,C_3068` be the path components after the direct layer.  Let
`B_free` be their 6,136 free endpoints and let `U` be the 12,168 unused
rank-seven vertices.  Form the candidate Johnson graph on `B_free union U`,
retaining only `B-U` and `U-U` edges that pass the fresh rank-eight and local
endpoint-turn tests.

The carrier part of the remaining theorem is to select a subgraph `H` with:

* degree one at exactly 6,134 vertices of `B_free`, leaving two final
  endpoints;
* degree two at exactly 9,631 vertices of `U`, and degree zero at the other
  2,537;
* 6,134 selected `B-U` edges and 6,564 selected `U-U` edges;
* 2,637 components with three internal `U` vertices and 430 with four;
* every selected edge-union colour distinct and outside the used bank;
* every selected degree-two turn colour distinct and outside the used bank;
* all 8,164 remaining missing rank-six edge-intersection colours present
  exactly once;
* after contracting each old component and each new ear, an acyclic connected
  quotient.  With 3,068 vertices and 3,067 ears this is a tree; the physical
  degree bound then makes the full object one path.

This is a coloured `b`-factor plus a short-path decomposition and one graphic
matroid condition.  The scalar constraints are no longer open.

There is a particularly compact contraction once a wedge-clean unique-edge
selection is also acyclic.  Base, direct and unique edges then number

\[
 3640+572+8164=12376,                                     \tag{4.1}
\]

on `7280+(2241+5511)=15032` currently used vertices, so the partial linear
forest has exactly

\[
 15032-12376=2656                                         \tag{4.2}
\]

components and 5,312 ports.  Activating the required 1,879 zero-degree
unused vertices gives 4,535 contracted nodes.  The 4,534 repeat edges must
use 5,310 of the old ports, leave two final endpoints, and give every new
vertex degree two.  Therefore any connected acyclic repeat completion is
automatically one Hamilton path.  This reframes the filler as a port-Hamilton
path on 2,656 existing components plus 1,879 singleton vertices.

The fixed `(x4,x5)` face is a clean sufficient short-ear schedule, not a
logical necessity for this contracted global completion; variable ear
lengths are allowed if the port-Hamilton path and the colour/deletion-label
conditions close.

## 5. The 4,534-repeat decoration is a local cap problem

For a selected carrier edge `e=vw`, write

\[
 C_e=v\cap w,\qquad |C_e|=6.                               \tag{5.1}
\]

If `e` carries a unique rank-six target, its source letter is fixed to
`A_e=C_e`.  If `e` is one of the 4,534 repeat slots, choose a deletion
`g_e in C_e` and put

\[
 A_e=C_e-\{g_e\},\qquad |A_e|=5.                           \tag{5.2}
\]

The chosen rank-five sets in (5.2) must be distinct.  Together with the two
outer source letters, they supply the 4,536 rank-five tail targets.

At every carrier vertex `v` with incident carrier edges `e,f`, exact
factorization is the single local equation

\[
                    A_e\cup A_f=v.                        \tag{5.3}
\]

When both edges carry distinct rank-six colours, (5.3) is automatic: their
two facet intersections are distinct facets of `v`.  If one or both edges
are repeat slots, (5.3) becomes an explicit constraint on the deletion
labels `g_e,g_f`.  For example, if

\[
 C_e=v-\{x\},\quad C_f=v-\{y\},\quad x\ne y,              \tag{5.4}
\]

and only `e` is shrunk, (5.3) says `g_e != y`.  If both are shrunk, it says

\[
 g_e\ne y,\qquad g_f\ne x,\qquad g_e\ne g_f.             \tag{5.5}
\]

Thus the Boolean-diamond compiler does not disappear completely; on a fixed
ear factor it reduces to a six-valued edge-label CSP with an SDR condition
on the resulting rank-five sets.  This is the precise meaning of the
"4,534-repeat factor" gate.

The contracted ledger splits this CSP canonically.  Every one of the 1,879
newly activated unused vertices has degree two and both incident edges are
repeat edges.  Hence these vertices account for

\[
 2(1879)=3758                                             \tag{5.6}
\]

repeat edges, leaving only

\[
 4534-3758=776                                            \tag{5.7}
\]

single repeat connectors between existing component ports.

At a new unused centre `u`, write its two incident facets as

\[
 C=u-\{x\},\qquad D=u-\{y\},\qquad x\ne y.               \tag{5.8}
\]

Choosing the two rank-five source letters means deleting `g` from `C` and
`h` from `D`.  Equation (5.3) on the two sides is exactly

\[
 g\ne y,\qquad h\ne x,\qquad g\ne h.                     \tag{5.9}
\]

There are therefore exactly `5*4=20` ordered deletion pairs at every such
centre--the literal Boolean-diamond multiplicity.  A single repeat connector
flanked by two unique facets has at most two forbidden deletions and hence at
least four choices.  After the repeat topology is fixed, the lower compiler
is consequently a grouped SDR with 1,879 twenty-pair domains and 776
single-label domains, not an unrestricted common-cap problem.

The next solver/theorem should therefore select the `b`-factor, its
3/4-vertex ear decomposition, and the deletion labels jointly.  Solving only
the 8,164-row ordinary Hall graph is insufficient.

## 6. Certificates

Independent construction A:

```text
scratch/solve_independent_k17_gk_shift1_forced_direct_20260731.py
  SHA-256 1b29031d85ffa35467d694eaff520d79bf8e8f90e913f61124b8357c5f83c028
scratch/k17_gk_shift1_forced_direct_matching_20260731.tsv
  SHA-256 8afb0d8f6e754ab31aa6d2f8f2dbe161cdcddce8c81883239195000d9f4afb71
scratch/independent_k17_gk_shift1_forced_direct_matching_20260731.audit.json
  SHA-256 a5a353617df6bcb777f133390dc922c3ae9be94bba3d9121e55e734bfbe5031c
  canonical payload acefe5847940e921880b5e1013709d73c477671346604ec227252f7b971acb34
```

Independent construction B:

```text
scratch/independent_k17_gk_shift1_exceptional_bb_20260731.tsv
  SHA-256 7abcbd84c926a4b6fb7154b2b2554d07282508eae10e7b411e2b9a2217231b8d
scratch/audit_independent_k17_gk_shift1_exceptional_bb_20260731.py
  SHA-256 30df7876d88407ded9e5f1cb8c4f4bb1db3ae76ff08fbe5292bca83d614f76bf
scratch/independent_k17_gk_shift1_exceptional_bb_replay_20260731.audit.json
  SHA-256 e04f92672500e40116e3d5fb9c2efe22d977246121b3820f6a72be7983d33761
  canonical payload f921ebf67b84435c31e3ae67e844bd3fdf72dbd52cecf2e1c7de9f7796fe8843
```

Residual capacity selection and independent replay:

```text
scratch/independent_k17_gk_shift1_residual_cap_20260731.tsv
  SHA-256 7e5706b65996e6d303108114c69f41c381a8743799da048c928eb9b2e50a47ff
scratch/solve_independent_k17_gk_shift1_residual_cap_20260731.py
  SHA-256 5f73de6ceaccf7d3165ccb51112bfe57e273a34a30d7b9508f25dfce65dacfce
scratch/audit_independent_k17_gk_shift1_residual_cap_20260731.py
  SHA-256 e32dddfdf5ff14a80ce24e52c80e9e6a220b3c02fdcf49423bbd42f04d6f0b7b
scratch/independent_k17_gk_shift1_residual_cap_replay_20260731.audit.json
  SHA-256 6b9f5389e59d086cadda4be9e7bd146991c050fa1231513097bed7f30b6157cc
  canonical payload 952b19f4df8b8a920107448a9b66bc4e1c4d2ee6b5760538933222d23c538ff5
```

Scope exclusion: these certificates do not produce a wedge-clean unique-edge
selection, select the 3,067 residual ears, assign the 4,534 rank-five deletion
labels, or construct the prefix or upper continuation.
