# Type-I canonical-prefix selector compression

## Verdict

In the standard adjacent-shadow Type-I `k=11` formula, the exact statement

```text
the suffix A[1],...,A[464] represents every nonempty mask except possibly
63, 1087, 1599, 1855, 1983, 2047
```

can be exposed using the already allocated witness selectors with

```text
0 variables / 32 clauses.
```

The current `K11_FOREST_TYPE1_PREFIX_CHAIN` implementation uses
`0 variables / 2,531 clauses`.  Two independent compressions apply:

1. its 1,974 generic-slot clauses can be replaced by six clauses because
   each generic rank-seven slot already chooses exactly one target;
2. targets which do not contain the fixed endpoint mask `63` are already
   forced out of position zero by the base exact-OR clauses.

Only 22 direct targets and four crossed rank-seven targets need the genuinely
lex-specific implication.  The replacement saves exactly 2,499 clauses.

This is a production design only.  It does not edit `k11_forest_sat.cpp`.

## 1. Precise theorem

The Type-I branch and residual coordinate quotient give

```text
A[0] = 63 = {0,1,2,3,4,5},
column(6) <=lex column(7) <=lex ... <=lex column(10).
```

Let `f_b` be the first positive position containing outside coordinate `b`.
Singleton coverage makes every `f_b` finite, and the lex order gives

```text
f_10 <= f_9 <= f_8 <= f_7 <= f_6.
```

Every interval containing position zero is a prefix.  Its OR is therefore in
the fixed chain

```text
C = {63, 1087, 1599, 1855, 1983, 2047}.             (1.1)
```

Since the full word is universal, every target outside `C` has a witness,
and no such witness can contain zero.  Consequently it has a witness wholly
inside positions `1,...,464`.

The wording "except possibly" is essential: any or all members of `C` may
also occur inside the suffix.  The theorem guarantees at least

```text
2047 - 6 = 2041
```

different nonempty suffix values; it does not assert that exactly six values
are absent.

No additional loss counter or chain circuit is needed after residual lex.
The possible loss names are already the six fixed members of (1.1).

## 2. Existing selected-witness mechanisms

The standard production portfolio has adjacent-shadow compression enabled.

* Ranks eight, nine, and ten are `DirectTarget` records.  `item.M0` is the
  exact membership vector of their selected interval.
* Each rank-seven target has a crossed alternative
  `rank_seven_shadow[column]`.  When `item.active` is true, `item.M0` is the
  membership vector of its selected crossed witness.
* Each of the six generic rank-seven `ExceptionSlot`s has one interval,
  membership vector `slot.M0`, and target selectors `slot.q[column]`.

Ranks at most five need no extra clause: a prefix contains the rank-six entry
`63` and cannot have lower rank.  For rank six, every value other than `63`
already has a selected interval avoiding zero.  Rank eleven has only the
canonical target `2047`.

## 3. Exact-one lemma for a generic slot

For every generic rank-seven slot, the base formula adds one positive clause
over all `slot.q[column]`, so at least one target is selected.  It also makes
`slot.value` have rank exactly seven and adds

```text
slot.q[column] -> every positive bit of that rank-seven target.
```

Two distinct rank-seven masks have a union of rank at least eight.  Hence two
different target selectors cannot both be true.  Thus every slot chooses
exactly one target.

Let `c` be the column of the canonical rank-seven target `1087`, let
`M=slot.M0+0`, and write `q_c=slot.q[c]`.  Under exact-one target selection,
the 329 current clauses

```text
!slot.q[column] OR !M              (column != c)      (3.1)
```

are equivalent to the single clause

```text
!M OR q_c.                                             (3.2)
```

Indeed, (3.1) says that if `M` is true, every noncanonical selector is false;
the positive target clause then forces `q_c`.  Conversely, if a
noncanonical selector is true, exact-one selection makes `q_c` false, so
(3.2) forces `M` false.

This equivalence does not use slot symmetry or any assumption about which
slot carries an exception.

## 4. Production clause schemas

### Endpoint-containment clauses already in the base formula

Suppose a fixed target `S` does not contain `63`.  Choose a low coordinate
`b in {0,...,5}` absent from `S`.  Type I fixes `A[0][b]=true`.

For a direct target, the base formula already contains

```text
-(item.M0+0) OR -A[0][b].
```

so unit propagation gives `-(item.M0+0)`.

For a crossed rank-seven target, the base formula already contains

```text
-item.active OR -(item.M0+0) OR -A[0][b],
```

so unit propagation gives the desired
`-item.active OR -(item.M0+0)`.

Consequently the prefix-chain module need only mention targets which contain
`63` but are not the canonical member of their rank.  Those are precisely the
targets excluded by residual lex rather than by endpoint containment alone.

### Direct ranks eight through ten

For each noncanonical direct target **containing `63`** add

```text
-(item.M0 + 0).
```

There are `C(5,r-6)` rank-`r` supersets of `63`, and the canonical exemption
is respectively `1599`, `1855`, or `1983`.  The count is

```text
(C(5,2)-1) + (C(5,3)-1) + (C(5,4)-1)
= 9 + 9 + 4 = 22.                                     (4.1)
```

### Crossed rank-seven alternatives

For each of the four noncanonical rank-seven supersets of `63`, add

```text
-item.active OR -(item.M0 + 0).
```

This contributes `C(5,1)-1=4` clauses.                 (4.2)

### Generic rank-seven slots

For each of the six slots add only

```text
-(slot.M0 + 0) OR slot.q[canonical_rank7_column].       (4.3)
```

This contributes six clauses, replacing `6*329=1,974` clauses.

The exact nonredundant incremental inventory in the adjacent-shadow
production formula is

| component | variables | clauses |
|---|---:|---:|
| direct ranks 8--10 | 0 | 22 |
| crossed rank 7 | 0 | 4 |
| six generic rank-7 slots | 0 | 6 |
| **total** | **0** | **32** |

The corresponding solver-add inventory is

```text
22*(one literal + terminator)
+4*(two literals + terminator)
+6*(two literals + terminator)
=44+12+18=74 add calls.
```

Relative to the current `0/2,531` implementation this saves

```text
2,531 - 32 = 2,499 clauses.                             (4.4)
```

For comparison, retaining explicit propagation closure for all fixed direct
and crossed targets while compressing only the generic slots gives
`0/563`.  The other 531 clauses are exact duplicates of the endpoint-
containment propagation displayed above.

The current full Type-I v6 inventory is

```text
3,640,493 variables / 19,989,126 clauses.
```

Replacing only the slot schema gives the predicted full inventory

```text
3,640,493 variables / 19,986,627 clauses.               (4.5)
```

If adjacent shadows are disabled, rank seven remains direct and the analogous
nonredundant fallback costs `4+22=26` unit clauses.  The 32-clause count is
the one relevant to the standard compressed production portfolio.

## 5. Prerequisites and scope

The mathematical guard requires

```text
K11_FOREST_RANK_FILTRATION_TYPE1=1
K11_FOREST_RESIDUAL_COORD_LEX=1.
```

The 32-clause implementation additionally uses

```text
K11_FOREST_ADJACENT_SHADOWS=1
```

and the existing exact generic-slot rank/target encoding.  Type I already
brings the branch-one prerequisites which fix `A[0]=63`.

No containment-cap, subcube-deficiency, named-cell, pin-localization, or
rank-seven-width guard is needed.  This cut is incompatible with Type II and
with portal formulas that allocate a different target portfolio.

All clauses are logical consequences of the normalized exact OR formula.
Thus the theorem changes propagation, not the represented solution set.  A
SAT candidate still requires exhaustive interval-OR verification, and an
UNSAT result still requires an independently checked proof trace.

## 6. Source-level blueprint

The existing emission block can retain its current guard and canonical array.
In pseudocode, replace its target loops by

```text
for direct target S of rank 7..10:
    if 63 subseteq S and S != canonical_by_rank[rank(S)]:
        add(-Inside_S(0))

if adjacent shadows:
    c = column of target 1087
    for crossed rank-seven target S:
        if 63 subseteq S and S != 1087:
            add(-active_S, -Inside_S(0))
    for generic rank-seven slot g:
        add(-Inside_g(0), q_g[c])
```

The first loop automatically gives 26 unit clauses in a non-adjacent
fallback (`4` at rank seven and `22` at ranks eight through ten).  In the
standard adjacent build, rank seven is absent from `direct`, giving the
`22+4+6=32` inventory above.

The canonical rank-seven column should be found by mask value and checked for
existence rather than relying on a hard-coded column number.
