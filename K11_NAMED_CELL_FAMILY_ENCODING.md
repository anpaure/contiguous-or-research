# Exact named-cell family encoding for the `k=11` onion branches

> **Historical/superseded B/C arithmetic.**  The old named-cell width rows
> used the chain-A `y0` formula on chains B/C.  Corrected rows are frozen and
> audited in `K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md`.

## 1. Result

`k11_forest_sat.cpp` now has the optional guard

```text
K11_FOREST_NAMED_CELL_HALL=1
```

which encodes the strongest set-valued consequence of
`K11_ONION_NAMED_CELL_HALL.md`, not merely its actual-rank scalar PB
relaxation.  The guard requires exactly one of

```text
K11_FOREST_RANK_FILTRATION_TYPE1=1
K11_FOREST_RANK_FILTRATION_TYPE2=1.
```

All other prerequisites are inherited from the selected filtration guard.
The implementation reuses the existing direct lower-target witnesses,
crossed rank-three/rank-four cells, generic exception slots, rank-five chain
boundaries, and Type-II component flags.

This module proves neither SAT nor UNSAT.  It is an exact WLOG reduction of
each guarded onion branch.

## 2. Why selected-witness localization dominates the PB row

The audited theorem says every rank-at-most-four target has a witness in a
branch-specific named family.

### Type I

The unique literal six-set is `A[0]`.  Every lower target has a witness in
suffix positions `1,...,464` of physical length at most two.  For every
direct or generic rank-at-most-four witness, the implementation therefore
adds

```text
not Inside(0),
not Inside(p) or not Inside(p+2)    (0<=p<=462).
```

The `Inside` variables already define one exact nonempty interval, so the
distance-two clauses are equivalent to length at most two.

### Type II

The exact stability cases are

```text
(duplicate excess, low components) = (0,1), (1,1), (0,2).
```

The first case has slack three and retains the existing global length-three
cap.  The other two cases have no lower witness longer than two.  The plan
defines

```text
short_mode <-> two_components OR duplicate
```

and guards every direct/generic lower distance-two clause by `short_mode`.

In the two-component case every internal pair of the selected slack-one
component is already forced by `RankFiltrationTypeIIPlan` to be an exact
selected rank-five witness.  Hence an exact lower-target pair cannot lie in
that component.  A pair crossing a literal rank-five separator is equally
impossible.  A selected lower pair is therefore automatically internal to
the slack-two component, exactly as required by the named-cell theorem.

Crossed rank-three/rank-four candidates are already singleton or adjacent
physical cells, so they need no new cap.  The direct/generic witness banks
are existential, making the named choice globally WLOG.

## 3. Exact Type-II duplicate flag

Write `n5` for literal rank-five occurrences, `y0` for selected singleton
rank-five witnesses, and `s` for the number of low components.  Existing
exact boundary identities give

```text
y0 = h1 + 462 - h6,
n5 - y0 + s <= 2.
```

The implementation retains the full-width sums

```text
left  = n5+h6+s,
right = h1+464
```

and materializes the exact bitwise equality flag `tight=(left==right)`.
Under the three audited cases, `tight` is true exactly for `(1,1)` and
`(0,2)`.  Therefore

```text
duplicate <-> tight AND not two_components
```

is precisely the `(1,1)` branch.  Equality-bit and final-AND clauses are
bidirectional.  These 13 variables and 59 clauses are allocated only when
the named-cell guard is enabled, so the old Type-II guard-off inventory is
unchanged.

## 4. Selected-width consequences

The module also encodes the cheap derived comparisons

```text
Type I:                 y2 >= 96+z,
Type II duplicate:      y2 >= 96+z,
Type II two components: y2 >= 95+z.
```

Here `z=y0=h1+462-h6`.  On the three allowed rank-five maximal chains,

```text
A: y2=(h3-h2)+(h5-h4),
B: y2=h3-h2,
C: y2=h5-h4.
```

For example, chain A and offset `c` use the exact guarded comparison

```text
h2+h4+h1+(462+c) <= h3+h5+h6.
```

Chains B/C use the analogous boundary differences.  Full adders and
first-difference comparisons are bidirectional; Type-II comparisons are
guarded by the conjunction of the subcase flag and chain selector.

## 5. Exact inventories

With adjacent rank-four and rank-three shadow compression, the capped banks
contain `11+55=66` direct rank-one/rank-two targets and twelve lower generic
exception slots.

```text
branch    module variables   module clauses   location   width   mode
Type I             241            37,851       36,192   1,659      0
Type II            489            39,453       36,114   3,336      3
```

The Type-II filtration itself grows from `9,814/47,310` to
`9,827/47,369` only when the named-cell guard requests the duplicate flag.

Build-only clause-stream fingerprints with
`k11_upper546_natural_array.txt` and the audited shadow/band/local-density
prerequisites are:

```text
Type I:
  total variables = 2,951,183
  total clauses   = 14,942,372
  FNV64           = f7a34b529d06d5c2

Type II:
  total variables = 2,958,676
  total clauses   = 14,757,499
  FNV64           = acd7c39830664a7c
```

The build-only hash stub is not a SAT solver and these fingerprints are not
evidence of satisfiability or unsatisfiability.

## 6. Independent checks

```text
python3 scratch/check_k11_onion_named_cell_hall.py
python3 scratch/check_k11_named_cell_family.py
```

The second checker exhausts:

* the exact duplicate and short-mode truth tables;
* all three stability subcases;
* the equivalence between distance-two clauses and interval length at most
  two;
* the boundary-width algebra for every chain at small analogue sizes; and
* both exact module inventories.

The production source compiles cleanly with `-Wall -Wextra -Wpedantic`.
