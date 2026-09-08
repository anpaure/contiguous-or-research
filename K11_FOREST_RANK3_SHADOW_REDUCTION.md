# Exact rank-three shadow compression for the unrestricted `k=11,n=465` forest formula

## Status

This note proves a new globally-WLOG reduction for the exact unrestricted
forest/band SAT formulation.  It does **not** assume a fixed derivative row,
a Hamilton path, Johnson adjacency, or a prescribed set of exceptional
rank-three masks.

The reduction has not yet been added to `k11_forest_sat.cpp`.  It is designed
to compose with the already-audited option

```text
K11_FOREST_ADJACENT_SHADOWS=1
```

because that option already materializes the OR of every singleton and
adjacent-pair interval.  Under that guard, replacing the 165 generic
rank-three direct targets by the construction below is projected to save

```text
266,020 variables
194,070 clauses.
```

The exact inventory is derived in Section 5 and independently recomputed by
`scratch/verify_k11_forest_rank3_shadow.cpp`.

## 1. Endpoint crossing count

Choose one witnessing interval for each of the 165 rank-three masks and one
for each of the 462 rank-five masks in a hypothetical universal array of
length 465.  Within either rank the chosen left endpoints are distinct, and
so are the chosen right endpoints.

Let `L_3,L_5` be the two left-endpoint sets.  Then

\[
 |L_3\cap L_5|\ge 165+462-465=162.
\]

The same calculation for the right-endpoint sets gives at least 162 common
right endpoints.  A rank-three selected witness is called *crossed* if its
left endpoint and its right endpoint both occur in the selected rank-five
family.  Inclusion-exclusion inside the 165 rank-three witnesses gives

\[
 \#\{\hbox{crossed rank-three witnesses}\}
 \ge 162+162-165=159.                         \tag{1}
\]

Thus at most six selected rank-three witnesses are not crossed.  This count
holds for every independently chosen rank-three and rank-five witness family.

## 2. A crossed rank-three witness is short

Let `J=[l,r]` be a crossed selected rank-three witness.  The selected
rank-five interval with the same left endpoint has the form `[l,x]`.
Necessarily `x>r`: if `x<=r`, that rank-five interval would be contained in
`J`, forcing its rank-five OR mask to be a subset of the rank-three OR mask.
Likewise the selected rank-five interval with the same right endpoint has the
form `[y,r]` with `y<l`.

Every selected rank-five witness has physical length at most three.  Indeed,
the rank-six interval-slack theorem says that every physical interval of
length at least four contains a selected rank-six witness and therefore has
OR rank at least six.  Applied to the proper extension `[l,x]`, this yields

\[
 r<x\le l+2,
 \qquad\hbox{hence}\qquad r-l+1\le2.          \tag{2}
\]

The right extension gives the same conclusion.  Therefore at least 159 of
the 165 rank-three masks occur as the OR of a singleton or adjacent pair, and
that short interval is certified by a proper selected rank-five extension at
each endpoint.

This is an unrestricted theorem about every length-465 solution.  Notice
that it is not inferred from the fixed-row `D^3 A` ansatz.

## 3. Exact six-exception encoding

There are

\[
 465+464=929
\]

singleton and adjacent-pair physical intervals.  The adjacent-shadow guard
already materializes eleven exact OR bits for each of these intervals for its
rank-four compression.  Reuse those bits.

For every short interval `J`, add one activation `G_J` saying that its OR has
cardinality at most three.  The implication is encoded by the 330 clauses

```text
G_J -> not(all four selected OR bits)
```

over every four-subset of the eleven coordinates.

For every rank-three target `S`, introduce `Q[J,S]`.  Its clauses say:

1. `Q[J,S] -> G_J`;
2. `Q[J,S]` forces the three bits of `S` into the materialized OR of `J`;
3. some selected rank-five witness begins at the left endpoint of `J` and
   ends strictly after `J`;
4. some selected rank-five witness ends at the right endpoint of `J` and
   begins strictly before `J`.

Items 1--2 imply `OR(J)=S`: the physical OR contains all three bits of `S`
and has cardinality at most three.  Thus different target flags on the same
physical interval are automatically incompatible; no pairwise at-most-one
clauses are required.  Items 3--4 are the endpoint certificates used in the
completeness proof and expose the crossing geometry to propagation.

Add six generic exact rank-three witness slots.  Each slot selects one
interval of safe length at most three, materializes its exact OR, constrains
that OR to rank three, and chooses one of the 165 targets.  Finally, for every
target `S`, add the coverage clause

```text
OR_J Q[J,S]  OR  OR_(six slots e) Q[e,S].
```

Unused generic slots may repeat an already-covered target.  Consequently six
slots encode *at most six exceptions* without guessing which targets are
exceptional.

## 4. Exactness theorem

### Theorem

Replacing the 165 direct rank-three targets in the already-audited
adjacent-shadow forest formula by the encoding of Section 3 preserves
satisfiability exactly.

### Soundness

Every asserted short flag `Q[J,S]` fixes the physical OR of `J` to `S`.
Every generic slot is an ordinary exact physical witness.  The target
coverage clauses therefore ensure that all 165 rank-three masks occur.
All other ranks retain their existing sound encodings.

### Completeness

Take any universal length-465 array and the rank-five selected witness family
represented by its monotone-band row.  Choose one witness for every
rank-three mask.  By (1), at least 159 are crossed.  By (2), every crossed
witness is one of the 929 materialized short intervals and has both required
proper rank-five extensions, so set its corresponding short flag.  Assign
the at most six remaining target witnesses to the six generic slots.  Fill
unused slots, if any, by repeating an already-covered target.  This extends
the genuine array to all new variables and clauses.

Hence the reduction neither deletes nor invents a length-465 solution.

## 5. Exact projected inventory

The old rank-three direct encoding has 165 targets.  Its safe bound is three.
For one target it allocates

```text
3*465 threshold/inside variables
3*465 positive-bit occurrence variables
------------------------------------------
2,790 variables,
```

and emits

```text
2,788 interval-threshold clauses
8*465 = 3,720 absent-bit clauses
3*(2*465+1) = 2,793 positive-bit clauses
------------------------------------------
9,301 clauses.
```

Thus removing the direct layer removes

```text
460,350 variables
1,534,665 clauses.
```

The replacement adds:

| category | variables | clauses |
|---|---:|---:|
| six generic rank-three slots | 40,116 | 114,150 |
| 929 at-most-three gates | 929 | 306,570 |
| `929*165` short target flags | 153,285 | 919,710 |
| 165 target coverage clauses | 0 | 165 |
| **total added** | **194,330** | **1,340,595** |

The net reduction is therefore

```text
variables: 460,350 - 194,330 = 266,020
clauses:   1,534,665 - 1,340,595 = 194,070.
```

Starting from the current adjacent-shadow plus band-cut inventory, the
projected complete formula becomes

```text
variables = 3,151,328 - 266,020 = 2,885,308
clauses   = 14,554,555 - 194,070 = 14,360,485.
```

These last totals are projections until the guarded generator is implemented
and a real CaDiCaL build-only run reproduces them.

## 6. Scope

This reduction proves no SAT or UNSAT result by itself.  A future SAT model
still needs both independent OR verifiers.  A future UNSAT claim still needs
an archived generated CNF and independently checked proof.  The theorem only
states that rank three can be encoded exactly with a six-exception crossed
short strip in the unrestricted search.
