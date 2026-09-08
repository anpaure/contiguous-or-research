# Compact exact rank-4/rank-8 pair-shadow encoding for `k=11`

## 1. Rank-eight target geometry

Fix a rank-eight target `U`.  Its possible central vertices are the 28
rank-six subsets of `U`; their induced graph is

\[
 J(8,6)\cong J(8,2).
\]

At a center `T`, write `U minus T={a,b}`.  Its twelve induced neighbours split
into two disjoint groups:

```text
A_T: six edges whose other endpoint adds a,
B_T: six edges whose other endpoint adds b.
```

### Lemma 1

Three consecutive central vertices with middle vertex `T` have union `U` if
and only if the two selected real edges at `T` consist of one member of `A_T`
and one member of `B_T`.

#### Proof

Each Johnson neighbour of `T` adds exactly one element outside `T`.  The union
of the three vertices is `T` plus the elements added by the two incident
edges.  It equals `U=T union {a,b}` exactly when those additions are distinct,
one `a` and one `b`.  The selected graph has real degree at most two, so the
two selected group edges are precisely the consecutive path edges through
`T`.  ∎

Thus target `958` has exactly

```text
28 centers * 6 * 6 cross-group pairs = 1008
```

ordinary pair witnesses.

## 2. Symmetric rank-four geometry

For a rank-four target `S`, a possible center has

```text
T = S union {a,b}.
```

The ten support-preserving incident edges split into two groups of five,
according to whether they remove `a` or remove `b`.  A triple intersection is
exactly `S` if and only if one selected edge belongs to each group.  There are

```text
21 centers * 5 * 5 = 525
```

witness pairs per rank-four target.

## 3. Hierarchical exact encoding

For each target and possible center introduce

```text
p_T <-> OR(selected edges in first group),
q_T <-> OR(selected edges in second group),
z_T <-> p_T AND q_T.
```

Then add

```text
OR_T z_T.
```

By Lemma 1 and its intersection dual, this is logically equivalent to the
old clause over every explicit cross-product pair witness.  It is not a
relaxation and does not assume a particular orientation.

For one rank-eight target this uses only

```text
28 * 3 = 84 variables
28 * 17 + 1 = 477 clauses,
```

instead of

```text
1008 variables
1008 * 3 + 1 = 3025 clauses.
```

For all rank-four and rank-eight targets together:

| encoding | variables | clauses |
|---|---:|---:|
|old all-incident-pairs block|200,970|603,405|
|compact grouped block|34,650|182,985|
|saved|166,320|420,420|

The old block materialized all `C(30,2)=435` incident pairs at every one of
462 centers, including pairs useful to neither required layer.  The compact
block creates only three variables for an eligible target-center flag.

## 4. Implementation

Set

```text
RECOMBINE_COMPACT_PAIR_SHADOWS=1.
```

In a pair/hybrid mode, this replaces the old rank-4/rank-8 pair block by the
equivalent grouped formulation.  In a lazy mode, any requested target at
distance two from the central rank—especially initial target `958`—uses the
same compact gate on demand.

The construction is valid in sparse candidate graphs as well: empty group
supports simply remove that center, and the equivalence is relative to the
candidate selected edges actually available.
