# Coordinate-filter Hall and residual pair/triple incidence cuts for `k=11,n=465`

## Verdict

The length-resolved short-cell rank vector has a compact, genuinely
distributional strengthening.  For every coordinate `b`, the physical cells
which are eligible for the already proved short witness choice must contain
enough values both containing and omitting `b`.  If `X_b` is the number of
eligible cells whose actual OR contains `b`, and `E` is the total number of
eligible cells, then

```text
386 <= X_b <= E-637,                    b=0,...,10.       (F)
```

The constants are exact:

```text
sum_(r=1)^5 C(10,r-1) = 386,
sum_(r=1)^5 C(10,r)   = 637.
```

Thus `(F)` is the containing-coordinate companion to the independently
proved omission hierarchy in
`K11_COORDINATE_OMISSION_SHORT_CELL_CUTS_20260724.md`.  It is pointwise and
is not implied by the scalar rank-vector rows, whose sum forgets which
coordinate occurs in which cell.

There is also a very small new pair/triple incidence row in the only
non-tight branch.  With `P5` the number of rank-five pair cells and `Tge5`
the number of triple cells of rank at least five,

```text
Type II (delta,s)=(0,1):
  2*Tge5+n5 >= P5+462.                               (PT5)
```

The rank-vector plan already materializes every term in `(PT5)`, so the row
costs only a few unsigned additions and one guarded comparison.

## 1. Exact eligible family

Let the low positions be the rank-at-most-four component(s) obtained after
deleting literal rank-five positions and, in Type I, the canonical rank-six
endpoint.  Define a branch-dependent physical candidate family `E`.

In Type I and either tight Type-II mode (`duplicate` or `two_components`),
`E` consists of

* every low singleton cell;
* every active low pair cell of actual OR-rank `2,3,4,5`;
* every active low triple cell of actual OR-rank five;
* every literal rank-five singleton position.

In the non-tight Type-II mode `(delta,s)=(0,1)`, also include active low
triple cells of actual OR-rank `2,3,4`.

Rank-one pair or triple cells are deliberately unnecessary: each singleton
target forces an actual literal singleton position in a zero-free word.
Cells of rank at least six are deliberately excluded because they cannot
witness a target of rank at most five.

The corrected shortening theorems give an injective choice of one cell of
`E` for every nonempty target of rank at most five:

* ranks one through four use a singleton/pair witness in Type I and tight
  Type II, and may additionally use a triple in non-tight Type II;
* a literal rank-five value uses one of its literal positions;
* every remaining rank-five value uses its selected pair/triple witness.

Different target masks use different physical cells because one physical
cell has one actual OR value.  Literal duplicates merely add unused capacity
and do not invalidate the injection.

## 2. Coordinate-filter theorem

For a coordinate `b`, let

```text
X_b = #{C in E : b in OR(C)}.
```

### Theorem 2.1

Every corrected Type-I and Type-II branch satisfies `(F)`.

### Proof

There are exactly `C(10,r-1)` rank-`r` masks containing `b`.  Summing over
`r=1,...,5` gives 386.  Restrict the injective witness choice from Section 1
to these targets.  Every selected witness has an OR containing `b`, so its
386 distinct cells lie among the cells counted by `X_b`.

Likewise, exactly `C(10,r)` rank-`r` masks omit `b`.  Their total is 637.
Every entry in a witness of a `b`-free target omits `b`, so their distinct
witnesses lie among the `E-X_b` eligible cells omitting `b`.  Hence
`E-X_b>=637`.  This proves both sides of `(F)`.  QED.

The proof uses no component orientation.  In the Type-II two-component
mode, all rank-at-most-four pair candidates automatically lie in the
slack-two component: every internal pair of the slack-one component is a
selected rank-five witness, and a pair crossing a literal rank-five
separator is inactive.

## 3. Rank-resolved form

For a physical cell family `Y`, write `Y_r(b)` for the number of its
rank-`r` cells whose OR contains `b`, and `Y_r(!b)` for the number omitting
`b`.  Let `n_r(b)` denote literal rank-`r` entries containing `b`.

For `2<=r<=4`, the exact rows are

```text
Type I / tight Type II:
  n_r(b)+P_r(b)   >= C(10,r-1),
  n_r(!b)+P_r(!b) >= C(10,r).

Type II (delta,s)=(0,1):
  n_r(b)+P_r(b)+T_r(b)    >= C(10,r-1),
  n_r(!b)+P_r(!b)+T_r(!b) >= C(10,r).
                                                               (RF-r-b)
```

At rank one the chosen candidate family uses literal singleton positions
only, so the corresponding rows are simply

```text
n1(b)>=1,
n1(!b)>=10.                                         (RF-1-b)
```

Equivalently one may set `P1=T1=0` in the displayed hierarchy.  Rank-one
pair/triple cells were intentionally excluded from `E` because every
singleton target already forces a literal singleton occurrence.

For this exact candidate family, set `P_1=T_1=0`; equivalently, the `r=1`
rows contain `n_1` only.  Rank-one pair/triple cells were deliberately
excluded from `E` because singleton targets already force literal singleton
positions.  Including physical rank-one pair/triple cells would remain a
safe relaxation, but it would no longer be the exact rank split of `(F)`.

For rank five, in every branch,

```text
L5(b)+P5(b)+T5(b)    >= 210,
L5(!b)+P5(!b)+T5(!b) >= 252.                    (RF-5-b)
```

Here `L5` counts literal rank-five occurrences.  In the duplicate branch it
counts both occurrences of the duplicated value, which is safe but can make
one coordinate section one unit weaker than a distinct-value count.

Adding the two rows for a fixed `b` recovers the corresponding scalar
rank-vector row through Pascal's identity

```text
C(10,r-1)+C(10,r)=C(11,r).
```

Therefore the coordinate split is a lifting of, and collectively implies,
the scalar row.  The implication is strict in the exposed arithmetic
projection: a scalar total can be correct while too many abstract cells are
concentrated on one side of a coordinate cut.

Summing `(RF-r-b)` over `r` gives `(F)`.  Conversely `(F)` is cheaper but
allows capacity of one target rank to compensate for another target rank.

## 4. Cheap occurrence projections

The exact candidate counter in `(F)` can be avoided.  Put

```text
o_b   = number of low singleton positions containing b,
ell_b = number of literal rank-five positions containing b,
N     = number of low positions,
Z_b   = N-o_b.
```

A marked low position belongs to at most one singleton, two pair, and three
triple cells.  Hence all low short cells containing `b` number at most
`6*o_b`.  Since the 386 containing targets need distinct eligible cells,

```text
6*o_b+ell_b >= 386.                                  (O+)
```

For the omission side, all entries of a low cell must be among the `Z_b`
positions omitting `b`.  If `Z_b>=2`, the total number of length-one,
length-two, and length-three cells inside all zero-runs is at most

```text
3*Z_b-3.
```

This is sharp for one run of length at least two.  A run of length `g`
contributes `g+(g-1)+max(g-2,0)`, and splitting it cannot increase the
total.  The case `Z_b<=1` is impossible in a satisfying branch: it supplies
at most one low `b`-free cell plus at most `n5<=134` literal rank-five
positions, far short of the 637 required targets.  Thus

```text
3*Z_b-3+(n5-ell_b) >= 637.                           (O-)
```

Using the exact low-position counts gives the compact upper rows

```text
Type I, N=464-n5:
  3*o_b+ell_b+2*n5 <= 752.                           (O-I)

Type II, N=465-n5:
  3*o_b+ell_b+2*n5 <= 755.                           (O-II)
```

These should be conjoined with the lower-target-only occurrence rows from
the omission audit.  In particular, Type I and tight Type II already give
at least 193 low positions omitting `b`, while non-tight Type II gives at
least 130.  Dually, the 176 lower targets containing `b` give the universal
cheap rows

```text
Type I / tight Type II: 3*o_b >=176,
Type II (0,1):          6*o_b >=176.                 (O-low)
```

The exact filter band `(F)` dominates all these occurrence projections.
Their advantage is cost.

## 5. Compact CNF tiers

### 5.1 Exact filter band

The existing rank-vector and `R3` plans already expose all required local
rank flags and pair/triple OR-coordinate bits.  Define one exact eligibility
flag per physical pair, and in Type II one exact branch-dependent triple
eligibility flag.  For each candidate cell `C` and coordinate `b`, define

```text
g[C,b] <-> eligible(C) AND b in OR(C).
```

Count the `g[C,b]` exactly to obtain `X_b`; obtain `E` either by one exact
candidate counter or by adding the already available rank counters.  Impose
the two comparisons in `(F)`.

The conservative fixed input counts are 1,854 candidate slots per coordinate
in Type I and 1,857 in Type II.  The Type-I count includes the rank-five
literal flag at the fixed rank-six position zero; that flag is identically
false and may be deleted, giving 1,853 potentially active slots.  A
deliberately conservative implementation which
counts `E` again, rather than reusing its constituent counters, adds less
than

```text
Type I:  66,000 variables / 380,000 clauses,
Type II: 66,000 variables / 385,000 clauses.          (5.1)
```

Reusing the exact `n_r,P_r,T_r` counters removes roughly 3,700 variables
and 26,000 clauses.  No new local OR-vector or per-target selector bank is
needed.

### 5.2 Occurrence projection

Define `low[p] AND A[p,b]` and `rank5[p] AND A[p,b]`, and exactly count the
two banks for every coordinate.  The source's 465-input Wallace/ripple
counter uses 461 full adders.  Before the small arithmetic/comparator tail,
the exact increments are about

```text
Type I:  30,481 variables / 172,491 clauses,
Type II: 30,514 variables / 172,678 clauses.          (5.2)
```

The tail is below 500 variables and 4,000 clauses.  This is the recommended
first benchmark if no coordinate-omission counter bank exists.

### 5.3 Reusing the omission-only counters

If the occurrence-only tier of
`K11_COORDINATE_OMISSION_SHORT_CELL_CUTS_20260724.md` is already present,
its exact `Z_b` counters make a much cheaper nonredundant package possible.
No new cell gate or population counter is needed.

The lower-target containing rows `(O-low)` become

```text
Type I:             Z_b+n5 <=405,
Type II tight:      Z_b+n5 <=406,
Type II non-tight:  Z_b+n5 <=435.                  (5.3)
```

The last row is redundant after the all-rank containing row below, but the
two tight rows are not: they dominate the all-rank projection once `n5` is
moderately large.

Dropping the coordinate-resolved literal term only weakens `(O+)` and
`(O-)`, because `0<=ell_b<=n5`.  This gives

```text
Type I:       6*Z_b+5*n5 <=2398,
Type II:      6*Z_b+5*n5 <=2404,
all branches: 3*Z_b+n5   >=640.                    (5.4)
```

The last row strictly strengthens the omission-only occurrence threshold
when `n5` is small, and throughout the non-tight range it raises the crude
`Z_b>=130` threshold to at least
`ceil((640-n5)/3)>=169`.  The upper rows constrain the opposite side of the
coordinate cut and therefore cannot follow from a lower bound on `Z_b`.

Using the existing exact `Z_b` and `n5` bit-vectors, all eleven copies of
`(5.3)--(5.4)` require only shifted additions and comparisons.  A direct
source-style implementation is conservatively below

```text
2,000 variables / 15,000 clauses.                  (5.5)
```

This is the cheapest coordinate-filter tier which remains nonredundant
after the omission-only module.  The standalone `(PT5)` row in Section 6 is
smaller still, but it acts only in the non-tight Type-II branch.

### 5.4 Reusing rank-resolved omission counters

If one of the exact rank-resolved omission tiers is present, the matching
containing-coordinate row is cheaper still.  For example, after the
rank-four omission counter `F4_b` has been built, impose

```text
Type I / tight Type II:
  F4_b+120 <= n4+P4,

Type II (0,1):
  F4_b+120 <= n4+P4+T4.                            (5.6)
```

The right sides are already exact rank-vector counters and the left
omission count already exists.  Equation `(5.6)` is exactly the rank-four
containing row because total rank-four capacity minus `F4_b` is the number
of candidate cells containing `b`.  No new physical flag or population
counter is required.  The same construction applies at ranks two, three,
and five with constants `10,45,210` as appropriate.

Thus, after a rank-resolved omission tier, all containing companions cost
only additions and guarded comparisons (well below 2,000 variables and
15,000 clauses even for every one-coordinate row).  They remain
nonredundant whenever the physical rank has surplus capacity: a lower bound
on the omitted side does not upper-bound that omission count, and therefore
does not force enough candidates on the containing side.

## 6. Residual pair/triple incidence

The selected contaminated-triple row forces every physical triple to have
rank at least five in Type I and in both tight Type-II modes.  Therefore the
generic nesting inequality between pair and triple cells is redundant in
those branches.

The non-tight Type-II one-component mode has

```text
q      = 462-n5 selected nonliteral rank-five targets,
P      = q+2 physical pair cells,
T      = q+1 physical triple cells,
Tge5  >= q.
```

Let `d=T-Tge5`, so `d` is zero or one.  If `d=1`, the unique triple cell of
rank below five has two distinct endpoint pair cells, and neither endpoint
pair can have rank five (indeed neither can have rank at least five).
Therefore

```text
2*d <= P-P5.
```

Substituting `P=q+2`, `T=q+1`, and `q=462-n5` gives exactly `(PT5)`:

```text
2*Tge5+n5 >= P5+462.
```

This is strictly stronger than the current rank-vector tail.  The abstract
corner

```text
Tge5=q, P5=q+1
```

satisfies `Tge5>=q` and can satisfy `P5>=y1,T5>=y2`, but violates `(PT5)`
by one.

The row should be guarded by `!tight`.  Since `P5`, `Tge5`, `n5`, and
`tight` already exist, its implementation needs fewer than 100 variables
and 700 clauses.  A stronger optional version replaces `P5` by `Pge5`.
Defining the exact pair `rank>=6` flags and one counter raises the increment
to less than 1,500 variables and 9,000 clauses.

## 7. Relation to existing modules

* The rank-vector rows are the coordinate sums/projections of the new Hall
  hierarchy; they cannot enforce its pointwise distribution.
* Type-I facet/ridge pin loads concern literal entries inside named facets
  of the fixed endpoint six-set.  `(F)` concerns all eligible short cells
  across every coordinate cut.  The modules are incomparable.
* Type-II reverse/companion pin loads activate only when a named component
  omits a coordinate.  `(F)` remains active when both components are
  coordinate-complete, so it covers the presently unguarded orientation.
* The six-subcube module counts literal entry supports and their run credit;
  it does not count the exact rank/coordinate support of the pair/triple
  candidate family.  Conversely `(F)` does not imply six-set run structure.
* The all-subcube form is valid: for any `U subseteq[11]`, eligible cells
  with OR contained in `U` are at least the number of rank-at-most-five
  targets contained in `U` after literal capacity is included.  Summing
  those rows over all `U` collapses to the existing rank-vector moments.
  Pointwise rows are the new information; the summed scalar is redundant.

These are necessary redundant propagation cuts.  They do not establish SAT
or UNSAT and do not change the certified bound on `nu(11)`.

## 8. Finite arithmetic check

Run

```text
python3 scratch/check_k11_coordinate_filter_pair_incidence.py
```

It verifies the two target constants, exhausts every binary path through
length twelve for the `3*Z-3` zero-run envelope, and exhausts all abstract
pair/triple high-rank patterns through nine pair cells for `(PT5)`.  The
checked script SHA-256 is

```text
a07674e09684b512c8cf079990dbc9031ce300cdfe9f66f5a3ef10ed0cd472d4
```
