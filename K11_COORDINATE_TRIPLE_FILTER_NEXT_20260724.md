# Coordinate-triple omission/filter package after B2

## Status and recommendation

This note derives the next compact redundant cut after the implemented
coordinate-pair omission, pair-filter, Type-II pair-component, and Type-I
pair-rank-four packages.  It is a theorem and source-inventory design only.
No generator was edited, no CNF was built, and no solver was run.

The recommended next package materializes the exact number `Z_B` of low
positions omitting a coordinate triple `B`, and imposes both sides of the
corresponding target cut.  Its full incremental cost, including the
rank-blind B3 occurrence rows, is

```text
Type I:  238,590 variables / 1,365,870 clauses,
Type II: 239,085 variables / 1,371,645 clauses.
```

These totals assume the already implemented pair-filter plan retains its
already constrained vector `three_n5=3*n5` as a C++ member.  That retention
has zero CNF cost.  If it is instead recomputed, add only `20 variables /
140 clauses` once to either total.

An independent theorem/inventory audit has passed.  It rederived the target
constants, all component-independent short-cell bounds, every branch
substitution, the `C<=N+3M` envelope, arithmetic widths, comparator counts,
and both total inventories.  The strictness examples below are deliberately
only separations in the exposed local arithmetic projection; they are not
claimed to extend to globally satisfying assignments of the full base CNF.

Thus the package stays below `240k` variables and `1.372M` clauses while
being strictly stronger than the earlier rank-blind B3 proposal.

## 1. Exact target constants

Fix a coordinate triple `B`.  Its complement has eight coordinates.  The
numbers of nonempty masks of ranks at most four and five which omit `B` are

```text
sum_(r=1)^4 C(8,r) = 8+28+56+70    = 162,
sum_(r=1)^5 C(8,r) = 162+C(8,5)    = 218.
```

The corresponding totals on all eleven coordinates are

```text
sum_(r=1)^4 C(11,r) = 561,
sum_(r=1)^5 C(11,r) = 1023.
```

Consequently the numbers which meet `B` are exactly

```text
561-162  = 399                 (ranks at most four),
1023-218 = 805                 (ranks at most five).       (1.1)
```

Let

```text
n5  = number of literal rank-five positions,
N   = number of low positions,
Z_B = number of low positions omitting all of B,
M_B = N-Z_B.
```

The already audited filtration gives

```text
Type I:  N=464-n5,
Type II: N=465-n5.                                    (1.2)
```

## 2. Omission-side rows

In Type I and tight Type II, every rank-at-most-four target has a singleton
or adjacent-pair witness.  The `B`-free singleton/pair cells in `Z_B` free
positions number at most `2*Z_B-1`.  The 162 distinct targets omitting `B`
therefore force

```text
Z_B >= 82.                                            (2.1)
```

In non-tight Type II, witnesses of length three are allowed.  For `Z_B>=2`,
the number of singleton/pair/triple cells in the free runs is at most
`3*Z_B-3`.  Hence

```text
Z_B >= 55.                                            (2.2)
```

The rank-five augmentation uses the 218 targets omitting `B`.  Literal
rank-five positions contribute at most `n5`, and the free low short cells
contribute at most `3*Z_B-3`.  Thus

```text
3*Z_B+n5 >= 221.                                      (2.3)
```

Row (2.3) is redundant after (2.1), and is emitted only in non-tight Type
II.

## 3. Meeting-side filter rows

Every low short cell whose OR meets `B` contains at least one of the `M_B`
low positions meeting `B`.

For singleton/pair cells, one low position is incident with at most three
cells.  Applying the injective witness choice to the 399 targets in (1.1)
gives, in Type I and tight Type II,

```text
3*M_B >= 399,
M_B >= 133.                                           (3.1)
```

For singleton/pair/triple cells, one low position is incident with at most
six cells.  Literal rank-five targets add at most `n5` further witnesses.
Applying the same injection to all 805 targets in (1.1) gives in every
branch

```text
6*M_B+n5 >= 805.                                      (3.2)
```

Substituting (1.2) into (3.1)--(3.2) gives the exact rows

```text
Type I:
  Z_B+n5       <= 331,
  6*Z_B+5*n5   <= 1979.

Type II:
  tight -> Z_B+n5 <= 332,
  6*Z_B+5*n5      <= 1985.                            (3.3)
```

There is one additional, free-arithmetic strengthening in non-tight Type
II.  If `C` is the number of singleton/pair/triple cells meeting `B`, then

```text
C <= N+3*M_B.                                         (3.4)
```

To prove (3.4), separately bound the meeting singleton, pair, and triple
counts by

```text
M_B,  min(2*M_B,N),  min(3*M_B,N).
```

If `3*M_B<=N`, their sum is at most `6*M_B<=N+3*M_B`.
If `2*M_B<=N<3*M_B`, it is at most `M_B+2*M_B+N`.
If `N<2*M_B`, it is at most `M_B+2*N<=N+3*M_B`.
This proof is valid for any number of low components.

Using all 805 targets again, (3.4) gives

```text
N+3*M_B+n5 >= 805.
```

In Type II this is

```text
1860-3*(Z_B+n5) >= 805,
Z_B+n5 <= 351.                                       (3.5)
```

The tight row in (3.3) dominates (3.5), so (3.5) matters only in the
non-tight branch.

## 4. Recommended combined theorem

For every one of the `C(11,3)=165` coordinate triples, impose

```text
Type I:
  Z_B >= 82,
  Z_B+n5 <= 331,
  6*Z_B+5*n5 <= 1979.

Type II:
  tight  -> Z_B >= 82,
  !tight -> Z_B >= 55,
  6*Z_B+5*n5 <= 1985,
  tight  -> Z_B+n5 <= 332,
  Z_B+n5 <= 351,
  !tight -> 3*Z_B+n5 >= 221.                         (4.1)
```

The unconditional Type-II `<=351` row may instead be guarded by `!tight`;
the clause count is unchanged.  Every row is a semantic consequence of the
base OR formula and the audited short-witness theorem.

The new information is not supplied by the 55 pair rows.  For example, a
tight abstract position profile may use 27 positions omitting all three
coordinates and 101 positions of each pair-only omission type.  Every
constituent pair then has omission count 128, while `Z_B=27<82`.  In loose
Type II, `Z_B=55,n5=0` satisfies the rank-blind B3 occurrence threshold but
violates `3*Z_B+n5>=221`, while constituent pair counts can all be 128.  The
profile `Z_B=219,n5=134` satisfies

```text
6*Z_B+5*n5=1984<=1985,
3*Z_B+n5>=221,
```

but violates the overlap row `Z_B+n5<=351`.  These examples are separations
in the exposed arithmetic projection; they are not claimed SAT witnesses.

## 5. Source-style encoding

For `B={a,b,c}` with `a<b<c`, choose the canonical contained pair `{a,b}`.
For every physical low-position slot define

```text
free3[p,B] <-> free2[p,{a,b}] AND free1[p,c].         (5.1)
```

Both inputs in (5.1) are exact banks already present after B2.  Exactly
count the `free3` flags to obtain `Z_B`.

Reuse `n5` and the pair-filter vector `three_n5=3*n5`, and form

```text
A_B = Z_B+n5,
B_B = A_B+2*Z_B       = 3*Z_B+n5,
D_B = 2*B_B+three_n5 = 6*Z_B+5*n5.                  (5.2)
```

All carries are retained.  The direct first-difference comparators already
used by the pair-filter plan allocate no auxiliary variables.

For one triple, (5.2) uses

```text
9+10+12 = 31 full adders
          = 62 variables / 434 clauses.              (5.3)
```

The relevant comparator clause counts are the numbers of set or zero bits
of the zero-extended constants:

```text
82<=Z:       3 clauses,       55<=Z:       5 clauses,
A<=331:      5 clauses,       A<=332:      6 clauses,
A<=351:      3 clauses,       221<=B:      6 clauses,
D<=1979:     4 clauses,       D<=1985:     7 clauses. (5.4)
```

## 6. Exact incremental inventory

Type I has 464 physical low-position slots.  Per coordinate triple:

```text
464 free3 gates                   464 vars / 1,392 clauses
exact 464-input counter           920 vars / 6,440 clauses
31 arithmetic full adders          62 vars /   434 clauses
three thresholds                    0 vars /    12 clauses
total                            1,446 vars / 8,278 clauses.
```

Across 165 triples:

```text
238,590 variables / 1,365,870 clauses.               (6.1)
```

Type II has 465 slots.  Per coordinate triple:

```text
465 free3 gates                   465 vars / 1,395 clauses
exact 465-input counter           922 vars / 6,454 clauses
31 arithmetic full adders          62 vars /   434 clauses
six branch/filter thresholds        0 vars /    30 clauses
total                            1,449 vars / 8,313 clauses.
```

Across 165 triples:

```text
239,085 variables / 1,371,645 clauses.               (6.2)
```

The Type-II threshold count in (6.2) includes both the `Z>=82/Z>=55`
branch rows and all four filter comparisons in (4.1).  These inventories
include the earlier B3 occurrence tier; they are not to be added on top of
the `228,360/1,292,775` or `228,855/1,296,405` B3 totals.

## 7. Deployment order

This package is the natural next independent probe after the currently
implemented pair tiers:

```text
Type I:  pair rank-four -> triple filter,
Type II: exact pair-component -> triple filter.
```

It is rank-blind, so it should not replace the Type-I pair-rank-four row.
Its advantage is that it tests a genuinely new third-order coordinate
intersection while simultaneously constraining the complementary side of
that intersection.  A future source must receive the usual additive-diff,
truth-table, inventory, remote build-only, and raw-token audits before any
solver launch.
