# Audit of the induced rank-eight flag moment

## 1. Exact identity

Fix a rank-eight target `U` and let `S_U` be its 28 rank-six subsets.  In the
selected graph define

```text
i_U = selected real edges with both endpoints in S_U,
c_U = selected real edges with exactly one endpoint in S_U,
e_U = selected dummy endpoint edges incident with S_U.
```

Summing the degree-two equations over all 28 vertices gives

\[
 2i_U+c_U+e_U=56.                         \tag{1}
\]

The support counts in the complete `J(11,6)` graph are:

* `J(8,6)` has `28*12/2=168` internal edges;
* each of the 28 vertices has `30-12=18` external neighbours, giving
  `28*18=504` cut edges; and
* there are 28 possible dummy endpoint edges.

Thus a literal-multiset encoding of (1) has

```text
2*168 + 504 + 28 = 868 occurrences.
```

These correct the tempting but erroneous cut count 252: internal degree is
12, not 21, and every external edge is counted once from its unique endpoint
inside `S_U`.

## 2. Why it was not added

With the source's audited exact unary counters, exact equality 56 on 868
occurrences would introduce:

```text
at_most(56): 48,608 variables and 97,972 clauses
at_least(56): 47,068 variables and 187,349 clauses
total:         95,676 variables and 285,321 clauses.
```

For comparison, the new exact compact target-`958` witness gate uses only

```text
84 variables and 477 clauses.
```

More importantly, (1) is literally the sum of 28 degree equations already in
the base CNF.  It contains no target-coverage information: it holds whether
or not `U` is the union of a consecutive triple.  A binary-adder encoding
could reduce its size, but would still duplicate an already explicit degree
consequence.

Therefore the induced flag moment is mathematically exact but currently a
poor propagation-cost trade.  It is documented and deliberately not exposed
as an environment option.

## 3. Other cheap consequences

The rank-seven coverage clauses imply `i_U>=8`, because all eight rank-seven
subsets of `U` must occur as upper edge colours and each corresponding edge is
internal to `S_U`.  This still does not force a triple-union witness: eight
internal selected edges can form a matching.  The exact missing condition is
local adjacency with different addition flags, precisely what the compact
two-group center gate enforces.

Hence no scalar edge-count or degree moment replaces the pair gate.  The
two-group formulation in `K11_COMPACT_PAIR_SHADOWS.md` is the exact local
formulation, only substantially compressed.
