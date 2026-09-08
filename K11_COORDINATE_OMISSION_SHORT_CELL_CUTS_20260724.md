# Coordinate-omission Hall cuts for the `k=11,n=465` short-cell families

## Verdict

There is a compact pointwise strengthening of the audited short-cell
rank-vector module.  For a coordinate set `B subseteq [11]`, let a physical
cell be **`B`-free** when its actual OR omits every coordinate in `B`.
For `1<=r<=4`, write

```text
nr(B) = number of literal rank-r entries which are B-free,
Pr(B) = number of active low adjacent-pair cells of OR-rank r which are B-free,
Tr(B) = number of active low consecutive-triple cells of OR-rank r which are B-free.
```

Then every corrected onion branch satisfies the following exact necessary
rows.

```text
Type I:
  nr(B)+Pr(B) >= C(11-|B|,r).                      (I-r-B)

Type II, duplicate one-component or two-component mode:
  nr(B)+Pr(B) >= C(11-|B|,r).                      (II-tight-r-B)

Type II, no-duplicate one-component mode:
  nr(B)+Pr(B)+Tr(B) >= C(11-|B|,r).                (II-01-r-B)
```

The right side is interpreted as zero when `r>11-|B|`.  Summing over
`r=1,...,4` gives the coordinate-subcube capacity row

```text
Type I / tight Type II:
  L(B)+P(B) >= sum_(r=1)^4 C(11-|B|,r),            (H-B-tight)

Type II (delta,s)=(0,1):
  L(B)+P(B)+T(B) >= sum_(r=1)^4 C(11-|B|,r),       (H-B-01)
```

where only cells of actual OR-rank at most four are counted.  For one
omitted coordinate `B={b}`, the rank-resolved right sides are

```text
(10,45,120,210)
```

and the aggregate right side is

```text
10+45+120+210 = 385.                               (0.1)
```

For two omitted coordinates the corresponding vector is

```text
(9,36,84,126), total 255.                          (0.2)
```

These cuts require no target-to-cell assignment matrix.  They are semantic
consequences of the already audited named-cell localization, but expose its
coordinate Hall content to the SAT solver in a compressed form.

There is also a rank-five analogue.  Let `L5(B)` count literal rank-five
positions which are `B`-free and let `P5(B),T5(B)` count active low pair and
triple cells of exact OR-rank five which are `B`-free.  In every branch,

```text
L5(B)+P5(B)+T5(B) >= C(11-|B|,5).                  (R5-B)
```

For `B={b}` the right side is `C(10,5)=252`.  In the duplicate Type-II mode
this row deliberately counts both literal occurrences of the duplicated
value.  It is sound but one unit weaker in precisely those coordinate
sections omitted by the duplicated five-set.  The already encoded global
row `n5+P5+T5>=463` retains that missing aggregate unit.

## 1. Physical candidate families

Let the low positions be the rank-at-most-four components left after
deleting literal rank-five positions (and, in Type I, after deleting the
canonical rank-six endpoint).  The corrected shortening theorem gives:

* Type I: every target of rank at most four has a singleton or adjacent-pair
  witness in the unique low core;
* duplicate Type II: every such target has a singleton or adjacent-pair
  witness in the unique low component;
* two-component Type II: every such target is a singleton in the slack-one
  component or a singleton/adjacent-pair value in the slack-two component;
* Type II `(delta,s)=(0,1)`: every such target has a singleton, adjacent-pair,
  or consecutive-triple witness in the unique low component.

The global active-pair family is harmless in the two-component branch.  Every
pair in the slack-one component has OR-rank five, every pair crossing a
literal rank-five separator is inactive, and therefore an active pair of
OR-rank at most four is automatically a permitted slack-two candidate.

The exact Type-II mode guard already exists in the rank-vector plan:

```text
tight <-> duplicate OR two_components.             (1.1)
```

Thus `(II-tight-r-B)` is guarded by `tight`, while `(II-01-r-B)` is guarded
by `!tight`.  No component selector is needed.

## 2. Proof of the lower-rank hierarchy

Fix `B` and `r<=4`.  There are exactly

```text
C(11-|B|,r)                                         (2.1)
```

rank-`r` masks which omit every coordinate in `B`.  For each such target,
choose one witness supplied by the appropriate shortening theorem of
Section 1.

Every entry in a witness for a `B`-free target is itself `B`-free: bitwise
OR cannot remove a coordinate.  The witness cell has actual OR-rank exactly
`r`.  Consequently it belongs to the left side of the applicable row.

The chosen physical cells are distinct.  A fixed cell has one actual OR
value, and therefore cannot witness two different target masks.  Hence the
choice of one witness per target is an injection from the target family in
(2.1) into the displayed candidate family.  This proves `(I-r-B)`,
`(II-tight-r-B)`, and `(II-01-r-B)`.

Summing the four disjoint actual-rank rows proves `(H-B-tight)` and
`(H-B-01)`.  There is no double counting between ranks because one physical
cell has one OR-rank.  There is also no illicit double counting between
different coordinate rows: a cell which omits several coordinates may
legitimately serve as capacity in each of the separately necessary Hall
inequalities.

## 3. Proof of the rank-five row

The corrected maximal rank-five schedule reselects a singleton witness for
every distinct literal rank-five value.  Every remaining rank-five target
has a selected witness of physical length two or three wholly inside a low
component; all allowed rank-five schedule states have endpoint width at most
two.  Hence every rank-five target has a witness among

```text
literal rank-five singletons,
active low rank-five pairs,
active low rank-five triples.                      (3.1)
```

Apply the same injection argument to the `C(11-|B|,5)` rank-five targets
omitting `B`.  This proves `(R5-B)`.  Literal duplicates can only enlarge the
physical candidate family, so they do not threaten soundness.

## 4. Rank-blind run and occurrence corollaries

There is a cheaper consequence which does not inspect the OR-rank of a short
cell.  Fix `b`, and mark a low position when its literal entry omits `b`.
Let

```text
Zb = number of marked low positions,
Rb = number of marked runs,
Ib = number of marked runs of length one.
```

A marked run of length `g` contains `2g-1` singleton/pair cells.  It contains

```text
g+(g-1)+max(g-2,0)
```

singleton/pair/triple cells.  Summing over runs and applying the same
injection to all 385 lower targets omitting `b` gives

```text
Type I or duplicate Type II:
  2*Zb-Rb >= 385,                                  (R-run)

Type II (delta,s)=(0,1):
  3*Zb-3*Rb+Ib >= 385.                             (R-run-01)
```

In the two-component branch, write `Z1b,Z2b` for the marked positions in the
slack-one and slack-two components and `R2b` for the marked runs in the
slack-two component.  Lower targets can use only singleton cells in the
first component, so the sharper exact rank-blind row is

```text
Z1b+2*Z2b-R2b >= 385.                              (R-run-02)
```

These rows count a superset of the exact rank-at-most-four candidates and
are therefore weaker than Section 2, but they expose useful occurrence
consequences.  In particular,

```text
Type I / tight Type II: Zb>=193,
Type II (0,1):          Zb>=130.                   (R-occ)
```

For the first row, `Rb>=1` and `2*192-1<385`.  For the second, the maximum
with `Zb>=2` is one run of capacity `3*Zb-3`, and `3*129-3<385`.
The two-component refinement also gives

```text
Z1b+2*Z2b>=386,                                    (R-occ-02)
```

because the slack-one component has fewer than 385 positions, so `Z2b>0`
and consequently `R2b>=1`.

The eleven `(R-occ)` rows are an especially small first propagation tier.
Defining `low[p] & !A[p,b]`, counting it exactly, and guarding the two
Type-II thresholds costs

```text
Type I:  15,312 variables / 86,691 clauses,
Type II: 15,433 variables / 87,417 clauses.        (4.1-old)
```

Those figures use the generic prefix-equality comparator.  The implemented
source instead uses the exact no-auxiliary first-difference comparator for a
constant threshold.  Its improved plan-local inventories are

```text
Type I:  15,224 variables / 86,185 clauses,
Type II: 15,258 variables / 86,397 clauses.        (4.1)
```

This tier does not require the short-cell rank-vector module.  It is weaker
than the exact physical-cell rows but about half their size.  A bare Type-II
filtration which has not already exposed the exact duplicate flag pays a
separate `40/187` upstream increment; current core/rank-vector builds already
contain that flag.

## 5. Relation to the scalar rank-vector rows

For fixed `r` and `t=|B|`, summing `(I-r-B)` or its Type-II counterpart over
all `t`-sets `B` gives

```text
C(11-r,t) * Cr >= C(11,t)*C(11-t,r),               (4.1)
```

because a rank-`r` cell omits exactly `11-r` coordinates.  The binomial
identity

```text
C(11,t)*C(11-t,r) = C(11,r)*C(11-r,t)              (4.2)
```

reduces (4.1) to the existing scalar row

```text
Cr>=C(11,r).                                        (4.3)
```

Thus the coordinate hierarchy refines, and collectively implies, the
rank-vector lower rows.  The implication is strict in the rank/support
projection: scalar `(4.3)` permits all `C(11,r)` abstract cells to contain a
fixed coordinate, while the `B={b}` row requires at least `C(10,r)` cells to
omit it.  This is an arithmetic separation only; the complete target-level
OR formula of course already forbids the concentrated assignment.

Similarly, summing `(R5-{b})` over all eleven coordinates gives

```text
6*(n5+P5+T5) >= 11*C(10,5)=2772,
n5+P5+T5 >= 462.                                   (4.4)
```

This is the no-duplicate arm of the existing rank-five vector row.  In the
duplicate mode the existing aggregate threshold `463` is independent and
must be retained.

## 6. Relation to pin-load and subcube modules

The recommended `|B|=1` rows are not replacements for the existing
coordinate pin modules.

* The Type-I facet theorem counts at least twenty **literal core entries**
  supported inside each of the six named facets of the canonical six-set.
  The omission rows count all eligible singleton/pair cells in a ten-coordinate
  section.  Either abstract summary can hold while the other fails, so the
  modules are incomparable.
* Type-II localization and reverse-pin rows concern targets **meeting** a
  missing coordinate and force literals or occurrence load in a named
  component.  The present theorem concerns targets **omitting** coordinates
  and needs no coordinate-complete-component orientation.  Again neither
  family subsumes the other.
* The six-subcube module counts literal entry support and run credit under
  six-set containers.  It does not resolve the actual OR support of all
  short pair/triple cells.  Conversely, the omission rows do not imply any
  fixed-six-set run structure.  They are incomparable.

At higher codimension the full hierarchy does meet the facet theorem.  If
`R` is a five-set and `B=[11]\R`, then the Type-I aggregate row says that at
least thirty qualifying singleton/pair cells are supported inside `R`.
Combining that row with the independently proved rank-five support-run
restriction recovers the lower bound of twenty literal core entries inside
`R`.  Thus the all-`B` theorem contains the candidate-capacity premise of the
facet argument.  The compact `|B|=1` tier does not, and encoding all 462
five-set sections would defeat the purpose of the present small module.

The named-cell target bank plus the base OR semantics already implies the
new Hall rows.  Their purpose is propagation: a few exact counters expose a
large family of target consequences without waiting for 385 separate
witness constraints to interact.

## 7. Compact `|B|=1` CNF tiers

The audited `ShortCellRankVectorPlan` already supplies:

* every active pair/triple OR bit in `pair_contribution` and
  `triple_contribution`;
* exact pair/triple rank flags `2,3,4,5`;
* the exact Type-II `tight` flag;
* exact singleton ranks in `local.rank[p][r]`.

For a singleton, define

```text
sfree[p,b,r] <-> local.rank[p][r] & !A[p,b].        (6.1)
```

For a pair or triple cell `c`, define

```text
pfree[c,b,r] <-> pair_rank_eq[c,r] & !pair_OR[c,b],
tfree[c,b,r] <-> triple_rank_eq[c,r] & !triple_OR[c,b].  (6.2)
```

Each definition in (6.1)--(6.2) is one variable and three clauses.  Exact
Wallace/ripple counters and guarded unsigned comparisons then implement the
rows.

### 7.1 Recommended first benchmark: rank four only

The largest coordinate section is the rank-four row

```text
Type I / tight Type II: n4(!b)+P4(!b) >= 210,
Type II (0,1):          n4(!b)+P4(!b)+T4(!b) >= 210. (6.3)
```

Using the source's exact two-variable/fourteen-clause full adder, the exact
increment beyond the existing rank-vector module is:

| category | Type I vars | Type I clauses | Type II vars | Type II clauses |
|---|---:|---:|---:|---:|
| omission flags | 10,197 | 30,591 | 15,312 | 45,936 |
| exact counters/additions | 20,328 | 142,296 | 30,690 | 214,830 |
| guarded comparators | 99 | 605 | 209 | 1,276 |
| **total** | **30,624** | **173,492** | **46,211** | **262,042** |

The Type-I counts use `464` suffix singleton cells and `463` pair cells.
Type II uses `465` singletons, `464` pairs, and `463` triples.  For each
coordinate the Type-II circuit counts singleton-plus-pair capacity once,
counts triples once, and adds the two counters; it does not duplicate the
singleton/pair Wallace bank.

### 7.2 All rank-resolved rows `r=2,3,4`

Rank one need not be re-encoded: every singleton target in a zero-free word
forces a literal singleton entry, and the base target clauses already expose
that fact.  Adding the coordinate rows for ranks two, three, and four costs
exactly:

```text
Type I:  91,872 variables / 520,476 clauses,
Type II: 138,633 variables / 786,126 clauses.       (6.4)
```

This is the strongest one-coordinate lower-target tier.

### 7.3 Aggregate `385` tier

If a smaller rank-agnostic tier is desired, add exact rank-one flags to the
already retained local pair/triple popcounts and define one
`rank-in-{1,2,3,4} and bit-b-absent` flag per cell.  The exact increments are

```text
Type I:  31,087 variables / 191,086 clauses,
Type II: 47,138 variables / 297,268 clauses.        (6.5)
```

This directly encodes the two `385` rows.  It is slightly larger than the
rank-four-only tier and weaker than all rank-resolved rows, but it tests the
full lower ideal in one comparator per coordinate.

### 7.4 Rank-five coordinate tier

Using the existing exact rank-five flags, `(R5-{b})` costs

```text
Type I:  45,815 variables / 259,490 clauses,
Type II: 45,936 variables / 260,205 clauses.        (6.6)
```

The literal rank-five occurrence flags are included in these totals.

All inventories above retain every carry and use bidirectional equality,
conjunction, and comparator gates.  They are incremental to the audited
rank-vector CNF; no new local OR-vector bank or per-target matrix is needed.

## 8. Two-coordinate tier

After the `B={b}` rank-four flags exist, define

```text
free[c,{b1,b2}] <-> free[c,b1] & free[c,b2]         (7.1)
```

and count them.  The `55` rank-four rows with right side `126` then add

```text
Type I:  153,120 variables /   867,460 clauses,
Type II: 231,055 variables / 1,310,210 clauses.     (7.2)
```

beyond the one-coordinate rank-four tier.  These rows are a genuine further
refinement: eleven one-coordinate capacities do not control the overlap of
their omission families.  The cost is still moderate but materially larger,
so the natural deployment order is rank-four `|B|=1`, then all ranks at
`|B|=1`, and only then `|B|=2` if solver telemetry justifies it.

## Scope

The final checker was copied without modification to the Rose RunPod and
executed there with `/usr/bin/python3.11`; it printed `PASS`.  The remote
SHA-256 values were

```text
3c8d7d2f8ec24397264fad25e4721e3aad19e0de1fc26d703e5b586821c41f6b  pre-annotation theorem note
7477cd005e9a3244110c62b8f7745e22489056f945fe426f017a58208a1acf23  checker
```

This note proves necessary redundant cuts and exact compact inventories.  It
does not prove satisfiability or unsatisfiability of either onion branch, and
it does not change the certified bound on `nu(11)`.  No production source or
live solver is changed by this note.
