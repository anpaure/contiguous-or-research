# Exact `K17` occurrence-radius-two frontier no-go

Date: 2026-07-31  
Status: solver-free exhaustive theorem for the frozen six-swap parent face;
no global `K17` obstruction, socket-packet obstruction, or all-dimension
claim is made

## 0. Result

The complete occurrence-radius-two continuation of the twelve
three-component radius-one states has been enumerated exactly.  No state has
a connected residence-clean direct-connector graph.  In particular, no state
can have a labelled Hamilton path, regardless of connector-label collisions.

The exact census is

```text
raw second-swap transitions                         17160
same-coordinate returns already in radius 0/1          13
unique genuine two-coordinate states                17081
states preserving every forced module               17081
strict D2/D3 residence-clean states                  16855
connected clean connector graphs                         0
connected graphs with at most two forced leaves          0
```

Thus one more occurrence exchange after the six-swap state does not close
the direct one-`U` marked-path gate.  The next occurrence-only search radius
is at least three.  Non-occurrence Steiner sockets, facet rethreads, and the
existing three-path fallback are outside this theorem and remain live.

## 1. Exact universe

Let `tau0` be the frozen six-swap residence-clean occurrence transversal.
Its complete one-coordinate neighbourhood has twelve states whose clean
connector projection has three weak components; the radius-one theorem proves
that every other state has at least four components.

For each of these twelve roots, change any one occurrence coordinate to any
other member of its fibre.  There are `1430` choices per root, hence `17160`
raw transitions.  Thirteen transitions alter the already-changed coordinate;
their endpoints lie back in the frozen radius-zero/radius-one universe.
After removing these and identifying the same two-coordinate state reached
in the two possible orders, exactly `17081` states remain.

The independent audit reconstructs the occurrence fibres directly from the
parent trace, reproduces the fibre histogram

```text
fibre size       1       2      3
number        3630    1320     55,
```

and proves exact equality between its independently generated set of `17081`
choice signatures and the producer TSV.  Thus no beam, objective cutoff, or
solver presolve defines the universe.

## 2. Literal evaluator

Every state is rebuilt from the parent exactly as in the radius-one census:

1. retain its chosen occurrence of every lower colour;
2. rebuild all `1430` `A/X/Y` macro paths;
3. reject a state if one of the `165` protected three-owner patterns splits;
4. take the complete macro-forest closure of the required macros;
5. materialize the literal owner word of every marked component;
6. count strict internal `D2<3` and `D3<4` runs; and
7. for every oriented component pair, test the literal five-token connector
   collar and construct the clean undirected projection.

All `17081` states preserve the protected modules.  Exactly `16855` also
have zero strict internal D2/D3 debt.

## 3. Exact graph-delta lemma

For a marked component `C`, define its literal profile to be

```text
(ordered port path of C, complete ordered owner word of C).
```

The clean directed connector relation between `C` and `C'` is a function
only of their two literal profiles: it uses their oriented endpoint ports and
the first/last five owner tokens.  Consequently, if both profiles survive an
occurrence exchange unchanged, every directed connector between them is
unchanged.  Only pairs incident to a changed profile need replay.

The producer matches profiles byte-for-byte, copies unchanged pair results,
and literally replays every other pair.  It evaluates `2,047,205` pairs
instead of the full `94,444,155`, a fraction

```text
0.021676354666945775.
```

This is an exact identity, not a heuristic locality assumption.  As a
separate boundary check, every one of the `583` states reported with only two
weak components is recomputed from all component pairs with the delta cache
disabled; every metric agrees.

The six-swap state and all twelve radius-one roots are also rebuilt before
the enumeration, and their stored component, closure, arc, and leaf counts
are asserted exactly.

## 4. Census and sharp boundary

Among the `16855` clean states, the weak-component histogram is

```text
components       2       3      4     5    6   7   8
states          583   14623   1503   124   20   1   1.
```

The forced-leaf histogram is

```text
leaves       17   18   19    20    21    22    23   24  25  26
states        6   59  355  1276  3601  6139  4168  989 235  27.
```

The two lexicographically best topology/leaf states are

```text
22802:(0,4321)->(0,4983), 1817:(0,447)->(0,3475)
    marked 107, closure 155, graph 105+2, leaves 17, clean arcs 328;

5150:(0,107)->(0,859), 1817:(0,447)->(0,3475)
    marked 108, closure 156, graph 106+2, leaves 17, clean arcs 328.
```

Both states remain disconnected.  More generally the minimum leaf count is
`17`, so any
fixed radius-two state still needs at least

\[
       \left\lceil {17-2\over2}\right\rceil=8
\]

outside-catalogue adjacency units before a spanning path is possible.  This
is an adjacency-unit bound, not an eight-swap bound.

## 5. Consequence and scope

The exact direct-connector progression is now

```text
six-swap state:         5 components, 23 leaves, one isolate;
best radius-one state:  3 components, 21 leaves;
best radius-two state:  2 components, 17 leaves;
```

Occurrence changes genuinely improve the obstruction, but they do not
finish it at radius two.  Any successful continuation must use at least one
of:

1. occurrence radius at least three;
2. a non-direct Steiner/socket packet;
3. a facet or complementary-bank rethread; or
4. the already certified multi-path/non-port fallback.

The theorem is confined to the fixed `K15` parent, six-swap source, protected
pattern list, and pure-old-`U` direct connector definition.  It proves no
`K17` lower bound and does not exclude another carrier or another two-bank
architecture.

## 6. Artifacts

```text
scratch/build_k17_radius2_occurrence_frontier_input_20260731.py
scratch/k17_radius2_occurrence_frontier_20260731.input.txt
scratch/census_k17_radius2_occurrence_frontier_20260731.cpp
scratch/k17_radius2_occurrence_frontier_20260731.census.tsv
scratch/k17_radius2_occurrence_frontier_20260731.stdout
scratch/k17_radius2_occurrence_frontier_20260731.stderr
scratch/audit_k17_radius2_occurrence_frontier_20260731.py
scratch/k17_radius2_occurrence_frontier_20260731.audit.json
```

The independent audit status is

```text
PASS_INDEPENDENT_K17_RADIUS2_OCCURRENCE_FRONTIER_NOGO
payload SHA-256 d1df707690411fac0d6a6ee25128077eb39f2ac313ac66d8ac6b7f810ce05d55.
```
