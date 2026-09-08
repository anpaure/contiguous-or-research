# Audit of the exact short-cell OR-rank cut

## Verdict

**PASS.**  Let `R3` be the sum of the actual OR-ranks of every physical
singleton, internal pair, and internal triple cell in the rank-at-most-four
low component(s), and put

```text
J = E-F = sum_(r=1)^4 (r-1)*max(nr-C(11,r),0).
```

The following are sound necessary rows:

```text
Type I:
  R3 + 7*z >= 4612 + J + 4*y1.                    (I-R3)

Type II, unified:
  R3 + 7*n5 + 7*two
     >= 4615 + J + 4*y1 + 4*delta + 5*t1.         (II-R3)
```

Here `delta=n5-z`, `two` is the exact two-low-component flag, and `t1` is
the number of length-one low components.  In the corrected Type-II geometry
`t1` is a zero-one flag, is zero in either one-component branch, and is only
potentially one when `two=1`.

Equivalently, the three corrected Type-II cases are

```text
(delta,s)=(0,1): R3-J+7*n5-4*y1      >= 4615,
(delta,s)=(1,1): R3-J+7*n5-4*y1      >= 4619,
(delta,s)=(0,2): R3-J+7*n5-4*y1-5*t1 >= 4608.     (0.1)
```

These rows are exact consequences of the complete physical short-cell
ledger.  They do not assume that a sum-of-entry-ranks upper bound on `R3` is
tight.

## 1. Complete short-cell count

For low component lengths `l1,...,ls`, with total length `N`, the number of
physical short cells is

```text
C = sum_i [li + max(li-1,0) + max(li-2,0)]
  = 3*N-3*s+t1,                                   (1.1)
```

where `t1=#{i:li=1}`.  There are 561 lower targets and `q` selected
nonliteral rank-five targets.  Choose one certified short witness for each.
The witnesses are distinct physical cells: one cell has only one OR value,
whereas all selected targets are distinct.  Hence the number of unused
physical short cells is exactly

```text
G = C-(561+q).                                     (1.2)
```

The branch substitutions are

```text
Type I:
  N=464-z, q=462-z, s=1, t1=0,
  G=366-2*z.

Type II:
  N=465-n5, q=462-n5+delta,
  G=372-2*n5-3*s+t1-delta.                        (1.3)
```

## 2. The unused-rank charge

At rank `r`, at least

```text
max(nr-C(11,r),0)
```

singleton cells are unused by the chosen distinct lower-target family.
These forced-unused singletons have total rank `E` and cardinality `F`.
Every other unused cell is nonempty and therefore has rank at least one.
Consequently the baseline rank of all unused cells is at least

```text
E+(G-F) = G+J.                                     (2.1)
```

This is why the exact total-cell row contains `J=E-F`, rather than `E`.

There is one further forced charge.  A triple containing a selected
rank-five pair has OR-rank at least five.  It cannot certify a lower target.
It also cannot certify a different selected rank-five target: if its rank is
five, its OR equals the contained pair's rank-five OR; if its rank exceeds
five, it is not a rank-five witness.  Thus every such *contaminated triple*
is unused and costs four additional rank units beyond the baseline one in
(2.1).

Let `u` be the number of distinct contaminated triples.  The surplus
singletons and contaminated triples are disjoint cell families.  Both lie
among the `G` unused cells, so there is no double counting in

```text
unused OR-rank >= G+J+4*u.                         (2.2)
```

The selected cells themselves have total OR-rank exactly

```text
1936+5*q.                                          (2.3)
```

Adding (2.2) and (2.3) inside the complete total `R3` gives the master row

```text
R3 >= 1936+5*q+G+J+4*u.                           (2.4)
```

## 3. Distinct contaminated triples

In a component of length `l`, view its `l-1` pair cells as the vertices of a
path and its `l-2` triples as the edges joining consecutive pair cells.  If
`a` selected pair cells form a proper subset of all pair cells, the number of
incident triple cells is at least `a`.  If every positive pair cell is
selected, the number is `a-1`.  This follows by decomposing the selected
vertices into runs in the pair-cell path.

In every one-component branch the selected pair cells do not exhaust all
physical pairs:

```text
Type I:                  q=N-2 < N-1,
Type II (delta,s)=(0,1): q=N-3 < N-1,
Type II (delta,s)=(1,1): q=N-2 < N-1.
```

Therefore

```text
u >= y1                                                     (one component).
                                                               (3.1)
```

In the two-component branch the audited slacks are one and two.  Every pair
in the slack-one component is selected.  The slack-two component cannot
have all of its pairs selected.  If `t1=0`, the positive pair family of the
slack-one component is the unique saturated pair component, losing exactly
one from the elementary incidence lower bound.  If `t1=1`, the length-one
component is necessarily the slack-one component and has no pair; the other
component is not saturated.  Hence

```text
u >= y1-1+t1.                                      (3.2)
```

The right side is nonnegative: when `t1=0`, the slack-one component has
length at least two and supplies at least one selected pair.

## 4. Branch arithmetic

For Type I, (1.3), (2.4), and (3.1) give

```text
R3 >= [1936+5*(462-z)] + [366-2*z] + J + 4*y1
   = 4612-7*z+J+4*y1,
```

which is `(I-R3)`.

For Type II, before using the contamination lower bound, (1.3) and (2.4)
give

```text
R3 >= 4618-7*n5+4*delta-3*s+t1+J+4*u.             (4.1)
```

Write `s=1+two`.  Equations (3.1)--(3.2) combine as

```text
u >= y1-two+t1.                                    (4.2)
```

Substitution in (4.1) and rearrangement gives `(II-R3)`, and specializing
the three exact modes gives (0.1).

The coefficient five on `t1` in the two-component projection has two
separate sources: `+t1` in the exact physical-cell count (1.1), and the
additional `+4*t1` in the contaminated-triple correction (3.2).  This is
not a repeated charge on one cell.

## 5. Compact exact CNF realization

Let `low[p]` mean that physical entry `p` has rank at most four.  Type II may
reuse the signed literal `!rank[p][5]`; Type I can define `low[p]` exactly as
the OR of the existing rank-one through rank-four flags.

The singleton contribution to `R3` is the already materialized scalar `S`.
For every coordinate `b`, introduce direct contribution bits for each
possible internal pair and triple:

```text
P[p,b] <-> low[p] & low[p+1]
                   & (A[p,b] | A[p+1,b]),

T[p,b] <-> low[p] & low[p+1] & low[p+2]
                   & (A[p,b] | A[p+1,b] | A[p+2,b]).          (5.1)
```

The pair equivalence has an exact five-clause encoding with one new
variable; the triple equivalence has an exact seven-clause encoding with one
new variable.  There are

```text
464*11 = 5104 pair bits,
463*11 = 5093 triple bits,
total   = 10197 contribution bits.                 (5.2)
```

Thus (5.1) costs exactly `10197` variables and `61171` clauses.  An exact
Wallace popcount of these bits, followed by one exact addition to `S`, uses
fewer than `10230` full adders.  With the source's audited 2-variable,
14-clause full adder, this is fewer than `20460` variables and `143220`
clauses.

Type I needs at most another `465` low flags and `2325` clauses.  An exact
`t1` flag can be obtained from the isolated-low-position flags in Type II.
The `J` term needs no saturating subtraction: exactly as in the histogram
module,

```text
J = max_(Q subseteq {2,3,4})
        sum_(r in Q) (r-1)*(nr-C(11,r)).            (5.3)
```

Enforcing all eight subset comparisons is exactly equivalent to the one
`J` row and reuses the existing rank counters.  The branch flags, `y1`,
`n5`, and `z` are already exact variables or exact counter vectors.

A conservative incremental inventory, including isolated-component flags,
the eight `J` comparisons, and final guarded arithmetic, is therefore below

```text
35,000 variables / 230,000 clauses                 (5.4)
```

in either branch.  This is compact relative to the current roughly
3.7-million-variable / 20-million-clause production formulas.  No
pair/triple target-assignment matrix is required.

## Scope

The audit establishes a necessary cut and a compact exact encoding plan.  It
does not establish satisfiability or unsatisfiability of either onion branch,
and it does not assert that `R3` reaches its sum-of-entry-ranks upper bound.
