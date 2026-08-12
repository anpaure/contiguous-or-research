# Compact exact rank-3/rank-9 four-shadow encoding for `k=11`

## 1. Rank-three target geometry

Fix a rank-three target `S`.  A possible middle edge `B--C` of a
four-vertex witness has

```text
S subset B intersection C,
B intersection C = S union {x,y}.
```

The possible middle vertices are the rank-six supersets of `S`.  After
deleting `S`, their induced graph is `J(8,3)`, with

```text
56 vertices, degree 15, and 420 middle edges.
```

At endpoint `B`, there are five real Johnson edges that preserve `S` and
remove `x`, and five that preserve `S` and remove `y`.  The same holds at
`C`.  The intersection of an outer path

```text
A--B--C--D
```

is exactly `S` precisely when its two outer edges remove opposite members of
`{x,y}`.  Thus every middle edge has

```text
2 orientations * 5 * 5 = 50
```

explicit witnesses, and one rank-three target has

```text
420 * 50 = 21,000
```

explicit four-path witnesses.

## 2. Dual rank-nine geometry

Fix a rank-nine target `U`.  Its possible middle vertices are the rank-six
subsets of `U`, inducing `J(9,6)`, with

```text
84 vertices, degree 18, and 756 middle edges.
```

For an eligible middle edge,

```text
U minus (B union C) = {x,y}.
```

At either endpoint there are six edges adding `x` and six adding `y` while
remaining inside `U`.  The outer edges must add opposite missing bits.
Consequently one target has

```text
756 * 2 * 6 * 6 = 54,432
```

explicit witnesses.

## 3. Projected orientation-gate encoding

Fix an eligible middle edge `e=B--C` and one of the two assignments

```text
x to the B side, y to the C side,
y to the B side, x to the C side.
```

Let `G_B` and `G_C` be the available candidate outer edges in the two
assigned groups.  Introduce one existential orientation flag `z` and add only

```text
not z OR e,
not z OR OR(G_B),
not z OR OR(G_C).
```

For the target, add one clause containing every such orientation flag.
Orientations with an empty support group are omitted.

### Theorem 1

After existentially projecting out the orientation flags, this formula is
equivalent to the explicit clause over every supported three-edge path whose
four-vertex intersection or union is the target.

#### Proof

If a flag is true, the three clauses select its middle edge, some supported
outer edge at `B`, and some supported outer edge at `C`.  By construction the
outer changes are the two opposite excess or missing coordinates, so the
four-vertex meet or union is the target.

The outer endpoints cannot coincide.  In the lower case the `B`-side outer
vertex retains `y`, whereas the `C`-side outer vertex removes `y`.  In the
upper case the `B`-side outer vertex contains its newly added `x`, whereas the
`C`-side outer vertex, which adds `y` to a set not containing `x`, does not.
Hence the three selected edges form a simple four-vertex path.

Conversely, take any supported explicit witness `A--B--C--D`.  Its two outer
edges remove, or add, the two different coordinates in one of the two
assignments above.  Set that assignment's flag true and every other flag
false.  All clauses are satisfied.

No reverse implication for `z` is required: `z` is an existential witness,
and the target clause already forces at least one witness to be chosen.  This
is an exact projected encoding, not a relaxation.  The argument uses neither
connectivity nor path orientation.  It therefore remains exactly equivalent
to the old explicit local-path gate even in a disconnected cycle-cover
relaxation; the independent connectivity constraints retain their previous
role.  It is also exact in any sparse candidate graph because `G_B,G_C`
contain only edges actually exposed in that graph.  ∎

## 4. Exact counts

For one target:

| target | old explicit variables | old clauses | compact variables | compact clauses |
|---|---:|---:|---:|---:|
| rank 3 | 21,000 | 84,001 | 840 | 2,521 |
| rank 9 | 54,432 | 217,729 | 1,512 | 4,537 |

The old clause count uses the previous exact Tseitin gate for each explicit
three-edge conjunction: four clauses per witness, followed by one target
clause.  The compact gate uses three clauses per orientation flag and one
target clause.

Across all `C(11,3)=165` rank-three and `C(11,9)=55` rank-nine targets:

| target-specific encoding | variables | clauses |
|---|---:|---:|
| old explicit paths | 6,458,760 | 25,835,260 |
| compact orientation gates | 221,760 | 665,500 |
| saved | 6,237,000 | 25,169,760 |

The old up-front `use_quad` implementation shared one variable when the same
four-path simultaneously supplied a rank-three and a rank-nine mask, but it
also materialized paths supplying neither layer.  In the complete
`J(11,6)` graph it created

```text
5,765,760 variables and 23,063,260 clauses.
```

Replacing that whole block by all compact target gates still saves exactly

```text
5,544,000 variables and 22,397,760 clauses.
```

## 5. Implementation and independent check

Set

```text
RECOMBINE_COMPACT_FOUR_SHADOWS=1
```

in `recombine_paths_sat.cpp`.  In `quad`/`full` mode it replaces the entire
up-front explicit four-path block.  In lazy modes, a requested target at
distance three from rank six uses the same compact encoding on demand.

The independent checker

```text
scratch/verify_k11_compact_four.cpp
```

exhaustively checks all 220 targets, all 110,880 eligible target/middle-edge
incidences, and all 6,458,760 target/path incidences.  It verifies both
directions of the geometric classification, the distinctness of the outer
vertices, the abstract existential CNF truth table, and every count above.

