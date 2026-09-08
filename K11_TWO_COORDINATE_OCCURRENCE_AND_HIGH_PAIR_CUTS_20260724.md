# Two-coordinate occurrence and high-pair incidence cuts for `k=11,n=465`

## Verdict

After the one-coordinate occurrence/filter rows, the next sound
distributional tier is the joint omission count for coordinate pairs.  For
distinct coordinates `b,c`, let

```text
Z_bc = #{low positions whose entry omits both b and c}.
```

Then

```text
Type I and tight Type II: Z_bc >=128,               (B2-tight)
Type II (delta,s)=(0,1): Z_bc >=86.                 (B2-01)
```

The rows are pointwise, survive all corrected component branches, and are
not implied by the eleven one-coordinate omission counts, the six-subcube
deficiency circuit, or the existing named pin modules.

If the one-coordinate omission gates already exist, all 55 rows add exactly
about `76k/432k` variables/clauses.  This is the recommended next structural
benchmark.

There is a still cheaper, orthogonal improvement of the non-tight
pair/triple incidence row.  Let `Pge5` count pair cells of actual OR-rank at
least five.  Then

```text
Type II (delta,s)=(0,1):
  2*Tge5+n5 >= Pge5+462.                            (PTge5)
```

It strengthens the already proved `P5` version and costs less than
`1,500/9,000` variables/clauses; the exact source-style increment is
`1,471/8,895`.

## 1. Pair-omission target count

Fix `B={b,c}`.  The number of nonempty masks of rank at most four which
omit both coordinates is

```text
sum_(r=1)^4 C(9,r) = 9+36+84+126 = 255.            (1.1)
```

In Type I and either tight Type-II mode, every such target has a selected
singleton/pair witness wholly inside the low component(s).  Every entry of
that witness omits `b,c`.  Distinct target masks use distinct physical
cells.

Mark the `Z_bc` jointly free low positions.  If their total number of runs
over all low components is `R_bc`, the total number of jointly free
singleton and internal-pair cells is exactly

```text
2*Z_bc-R_bc.                                        (1.2)
```

The chosen target cells form a subfamily of these cells.  Hence

```text
2*Z_bc-R_bc >=255.                                  (1.3)
```

If `Z_bc>0`, then `R_bc>=1`; equation `(1.3)` therefore gives
`2*Z_bc>=256`, proving `(B2-tight)`.  This argument remains valid in the
two-component mode.  Pairs in the slack-one component are not valid lower
target candidates, but counting them in `(1.2)` only enlarges the containing
family and hence remains a sound capacity upper bound.

If the existing Type-II component selectors are to be reused, the exact
two-component refinement is available.  Let `Z1_bc,Z2_bc` be the jointly
free positions in the slack-one and slack-two components, and `R2_bc` the
jointly free run count in the slack-two component.  The valid lower-target
candidate count is exactly bounded by

```text
Z1_bc+2*Z2_bc-R2_bc >=255.                          (B2-02-exact)
```

The first component contributes singleton witnesses only; the second
contributes singleton/pair witnesses.  This row is strictly stronger than
the global `Z_bc>=128` projection but requires component-resolved joint
flags and is not the recommended first tier.

In the non-tight Type-II mode, selected lower witnesses may also be triples.
A jointly free run of length `g` contains

```text
g+(g-1)+max(g-2,0)
```

short cells.  With `I_bc` the number of jointly free runs of length one, the
total is exactly

```text
3*Z_bc-3*R_bc+I_bc.                                 (1.4)
```

For `Z_bc>0`, `R_bc>=1` and `I_bc<=R_bc`, so `(1.4)` is at most
`3*Z_bc-2`.  The 255-target injection gives

```text
3*Z_bc-2 >=255,
```

and hence `Z_bc>=ceil(257/3)=86`.  This proves `(B2-01)`.

## 2. Optional rank-five augmentation

There are

```text
C(9,5)=126
```

rank-five masks omitting `b,c`, so the rank-at-most-five target total is
381.  Every nonliteral such target has a selected low pair/triple witness;
literal targets use literal rank-five positions.

If `Z_bc>=2`, all jointly free singleton/pair/triple cells over every low
component number at most `3*Z_bc-3`.  At most `n5` literal rank-five
positions omit the pair.  The case `Z_bc<=1` cannot provide 381 distinct
candidates even with all `n5<=134` literals.  Therefore every branch obeys

```text
3*Z_bc+n5 >=384.                                    (B2-r5)
```

In tight branches this is redundant after `Z_bc>=128`.  In the non-tight
branch it can strengthen `Z_bc>=86` when `n5` is small, so the natural
deployment is to guard `(B2-r5)` by `!tight`.

## 3. Exact incremental cost

Assume the one-coordinate occurrence tier has already defined exact gates

```text
free[p,b] <-> low[p] AND !A[p,b].                   (3.1)
```

For every unordered pair `b<c`, define

```text
free2[p,b,c] <-> free[p,b] AND free[p,c].           (3.2)
```

Each gate costs one variable and three clauses.  Count the fixed banks with
the source's exact Wallace/ripple counter.

Type I has 464 potentially low suffix positions.  One 464-input exact count
uses 460 full adders, hence 920 variables and 6,440 clauses.  Type II has
465 positions and uses 461 full adders, hence 922 variables and 6,454
clauses.  The exact totals for all 55 coordinate pairs, including direct
guarded comparisons, are

```text
Type I:
  joint gates       25,520 variables /  76,560 clauses
  exact counters    50,600 variables / 354,200 clauses
  comparisons                0 variables /      55 clauses
  --------------------------------------------------------
  total             76,120 variables / 430,815 clauses.

Type II:
  joint gates       25,575 variables /  76,725 clauses
  exact counters    50,710 variables / 354,970 clauses
  tight/!tight comparisons   0 variables /     275 clauses
  --------------------------------------------------------
  total             76,285 variables / 431,970 clauses.   (3.3)
```

The Type-II comparison count uses one direct clause for threshold 128 and
four for threshold 86, each guarded by the appropriate exact mode literal.

Adding `(B2-r5)` in non-tight Type II reuses each `Z_bc` counter and the
existing `n5` vector.  Fifty-five shifted additions and comparisons add less
than 2,300 variables and 16,000 clauses.

## 4. Nonredundancy

### 4.1 One-coordinate occurrence rows

The one-coordinate rows only lower-bound `Z_b` and `Z_c` separately.  Their
intersection can be as small as

```text
max(0,Z_b+Z_c-N),
```

which is far below 128 throughout the admissible low lengths.  For example,
two abstract 193-subsets of a 331-position low set can intersect in only 55
positions.  Thus all one-coordinate thresholds may hold while
`(B2-tight)` fails.

### 4.2 Six-subcube deficiency

The six-subcube module counts literal entry support inside six-coordinate
containers and their run-credit deficits.  It never materializes the joint
two-coordinate omission count.  Even the raw pointwise lower bounds are far
too weak: among the nine coordinates outside `b,c` there are 84 six-sets;
their `p_U>=28` rows give 2,352 incidences, while one rank-one jointly free
entry can contribute to 56 of those six-sets.  This incidence projection
only forces a count on the order of 42, not 128.  The global deficiency
charges constrain a different distribution and do not recover the missing
pairwise intersection.

There is a concrete abstract separation from both the six-subcube rows and
the one-coordinate occurrence rows.  In a 465-position non-tight profile,
start with six copies of every coordinate singleton.  For a fixed pair
`b,c`, add 154 rank-four entries containing `b` but not `c`, 154 containing
`c` but not `b`, and 91 containing both; distribute the remaining coordinates
of these rank-four entries nearly uniformly over the other nine coordinates.
Then

```text
Z_bc=54,
Z_b=Z_c=214,
214 <= Z_d <= 400 for every other coordinate d.
```

Every six-set contains the six copies of each of its six singleton
coordinates, so every exact support population has `p_U>=36` and both
subcube deficiency charges vanish.  The cheap one-coordinate
occurrence/filter projections with `n5=0` also hold, while `(B2-01)` fails.
This is a separation
of the exposed auxiliary projection, not a claim that the multiset is a
universal OR word.

### 4.3 Pin modules

The Type-I facet/ridge modules concern literal entries inside facets of one
fixed canonical endpoint six-set.  They do not impose 55 global pairwise
omission counts.  Type-II reverse/companion rows activate only after a named
component omits a coordinate; `(B2-tight)/(B2-01)` remain active when every
low component is coordinate-complete.  Hence neither pin package dominates
the pairwise occurrence rows.

## 5. Stronger high-pair incidence

In the non-tight one-component Type-II mode, write

```text
q=462-n5,
P=q+2  physical pair cells,
T=q+1  physical triple cells.
```

The current contaminated-triple row gives `Tge5>=q`, so
`d=T-Tge5` is zero or one.  If `d=1`, the unique low triple's two endpoint
pair cells both have rank below five: a containing triple cannot have lower
OR-rank than either endpoint pair.  Thus, with `Pge5` the number of pair
cells of rank at least five,

```text
2*d <= P-Pge5.                                      (5.1)
```

Substitution in `(5.1)` gives `(PTge5)` exactly:

```text
2*Tge5+n5 >= Pge5+462.
```

The guard is `!tight`.  In all tight modes every triple is already forced
to rank at least five, and the corresponding generic incidence row is
tautological.

The rank-vector plan currently has `P5` but not pair `rank>=6`.  During the
existing pair popcount loop, define the same exact four-clause `rank>=6`
flag already used for triples, and count the 464 Type-II flags.  The exact
increment is

```text
pair >=6 flags:                  464 / 1,856
exact 464-input counter:         920 / 6,440
Pge5=P5+Pge6 addition:            18 /   126
PT arithmetic/guard/comparator:   69 /   473
--------------------------------------------------
total:                          1,471 / 8,895.      (5.2)
```

It is strictly stronger than the `P5` row: the abstract non-tight corner

```text
Tge5=q,
P5=q,
Pge6=1
```

satisfies `2*Tge5+n5>=P5+462` at equality but violates `(PTge5)` by one.
The coordinate occurrence/filter rows contain no pair-high-rank counter and
therefore do not imply it.

## 6. Why coordinate-summed moments are not useful

Summing the one-coordinate occurrence rows collapses to scalar cuts already
present:

* `Z_b+n5<=405/406` sums to the existing `S>=649` row;
* `6*Z_b+5*n5<=2398/2404` sums to
  `6*S+11*n5>=4246`, dominated by the existing
  `6*S+5*n5>=4254` (or 4259) row;
* the summed lower omission row is weaker than the elementary entry-rank
  caps.

Likewise, summing `(B2-tight)` over all 55 pairs gives

```text
45*n1+36*n2+28*n3+21*n4 >=7040.                    (6.1)
```

But `N=n1+n2+n3+n4>=331` and `n1>=11` already give

```text
45*n1+36*n2+28*n3+21*n4
  >=21*N+24*n1
  >=21*331+24*11
  =7215.
```

Thus the summed moment is redundant even though the 55 pointwise rows are
new.  Encoding only a coordinate-summed projection would add no strength.

## 7. Exact zero-run refinements

If only the occurrence thresholds are enabled, retaining the run counts
gives the stronger exact rows

```text
Type I / tight Type II: 2*Z_b-R_b >=385,
Type II (0,1):          3*Z_b-3*R_b+I_b >=385.      (7.1)
```

In the two-component branch a sharper localized version is

```text
Z1_b+2*Z2_b-R2_b >=385.                             (7.2)
```

These are sound and nonredundant after the scalar occurrence thresholds,
but they are weaker than the full rank-resolved coordinate-filter counters,
which exclude short cells of the wrong OR-rank.  Therefore run counters are
worth adding only to an occurrence-only formulation; they should not be
stacked on top of the full filter module merely for logical strength.

## Recommendation

1. Add `(PTge5)` first if a very small branch-local refinement is desired.
2. For the next genuinely distributional benchmark, add the 55
   `(B2-tight)/(B2-01)` counters; optionally add `(B2-r5)` only in non-tight
   Type II.
3. Do not spend formula size on coordinate-summed moments.
4. Use exact run refinements only when the full rank-resolved filter module
   is absent.

These are redundant necessary cuts, not a SAT/UNSAT result.

## Verification

The lightweight checker

```text
python3 scratch/check_k11_two_coordinate_high_pair_cuts.py
```

exhausts binary run patterns through length twelve, exhausts the abstract
high-pair/high-triple path patterns through nine pair cells, constructs the
465-position one-coordinate/subcube separation, and checks every inventory
constant in `(3.3)` and `(5.2)`.  Its SHA-256 is

```text
494dc3c9dd7a8a62727f5b4c594125da42fee16ec793b24afba3a3cba32fe5e3
```
