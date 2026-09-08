# Rank-resolved short-cell cuts beyond the scalar `R3` row

## Verdict

The exact total short-cell OR-rank row is not locally maximal.  A strictly
stronger compact relaxation is obtained by retaining the exact OR-rank
histogram of the physical singleton, internal-pair, and internal-triple
cells in the low component(s).

Let

```text
Cr = number of physical short cells whose actual OR has rank exactly r,
Cge5 = C5+C6+...+C11,
cr = C(11,r), so (c1,c2,c3,c4)=(11,55,165,330).
```

Then every corrected Type-I/Type-II branch satisfies

```text
C1>=11, C2>=55, C3>=165, C4>=330.                 (V1)
```

The selected nonliteral rank-five witnesses also give

```text
Type I:       C5+z   >= 462,
Type II:      C5+n5  >= 462+delta.                (V2)
```

Finally, selected rank-five pair cells force distinct unused contaminated
triples.  With `two` the exact two-component flag and `t1` the exact number
of length-one low components,

```text
Type I:
  Cge5+z-y1 >= 462,

Type II, unified:
  Cge5+n5-y1+two-t1 >= 462+delta.                 (V3)
```

The three Type-II instances of `(V3)` are

```text
(delta,s)=(0,1): Cge5+n5-y1      >= 462,
(delta,s)=(1,1): Cge5+n5-y1      >= 463,
(delta,s)=(0,2): Cge5+n5-y1-t1   >= 461.          (0.1)
```

Rows `(V1)--(V3)` are exact consequences of the physical witness ledger,
need no target-assignment matrix, and jointly imply the already audited
total-`R3` cut.  They are strictly stronger than that scalar sum: high-rank
short cells can no longer compensate for a missing rank-two, rank-three, or
rank-four cell.

## 1. Physical short-cell family

Let `C` be the family consisting of every low singleton and every internal
pair and triple in the low component(s).  The audited shortening theorems
give one cell of `C` for every rank-at-most-four target in all four corrected
branches:

* Type I: every lower target has a singleton/pair witness;
* either tight Type-II mode: every lower target has a singleton/pair witness;
* Type II `(delta,s)=(0,1)`: every lower target has a witness of length at
  most three.

One physical cell has one OR value.  Witnesses selected for distinct target
masks are therefore distinct cells.

The number of short cells is

```text
|C| = 3*N-3*s+t1.                                 (1.1)
```

As before, the selected nonliteral rank-five count is

```text
Type I:  q=462-z,
Type II: q=462-n5+delta.                           (1.2)
```

## 2. Proof of the exact-rank rows

There are exactly `cr=C(11,r)` distinct rank-`r` lower masks.  Each chosen
short witness for such a mask has actual OR-rank exactly `r`.  The chosen
witness cells are distinct, so

```text
Cr>=cr, 1<=r<=4.
```

This proves `(V1)`.

Likewise, the `q` selected nonliteral rank-five masks use `q` distinct short
cells of actual OR-rank five.  Substitution of (1.2) proves `(V2)`.

## 3. Proof of the contaminated-tail row

Mark every internal pair cell selected as a rank-five witness.  A containing
triple has OR-rank at least five.  It cannot witness a lower target.  It also
cannot be the selected witness of a different rank-five target: if its rank
is five, its OR equals the contained selected pair's OR; if its rank exceeds
five, it is not a rank-five witness.  Thus every distinct contaminated
triple is unused and is disjoint from the `q` selected rank-five cells.

Let `u` be the number of distinct contaminated triples.  The audited
pair-path incidence lemma gives

```text
u>=y1                              in one component,
u>=max(y1-1+t1,0)                  in two components.   (3.1)
```

In unified notation,

```text
u>=max(y1-two+t1,0).                              (3.2)
```

The `q` selected cells and these `u` unused cells are distinct and all have
rank at least five.  Hence

```text
Cge5>=q+u.                                        (3.3)
```

The linear projection obtained by dropping the outer maximum gives `(V3)`
and all constants in (0.1).  Together, `(V2)` and `(V3)` retain the exact
piecewise statement

```text
Cge5>=q+max(y1-two+t1,0).                          (3.4)
```

There is no double counting: selected rank-five cells and contaminated
triples are disjoint physical cells, while two selected pairs incident with
one triple contribute only one cell to `u`.

## 4. Exact dominance over the total-`R3` row

For `r=1,...,4`, let

```text
fr=max(nr-cr,0),
J=sum_(r=1)^4 (r-1)*fr.
```

Every rank-`r` singleton entry is itself a rank-`r` short cell.  Therefore
`Cr>=nr` structurally.  Together with `(V1)`,

```text
Cr>=max(cr,nr)=cr+fr.                              (4.1)
```

Consequently

```text
sum_(r=2)^4 (r-1)*Cr >= 1375+J,                   (4.2)
```

because

```text
1*C(11,2)+2*C(11,3)+3*C(11,4)=55+330+990=1375.
```

Also, the conjunction of `(V2)` and `(V3)` gives (3.4), and the physical
incidence proof permits `u=max(y1-two+t1,0)` in the lower bound.  Hence

```text
sum_(r=5)^11 (r-1)*Cr >= 4*q+4*u.                 (4.3)
```

Let `G=|C|-(561+q)` be the exact number of unused short cells in a chosen
complete witness family.  Since

```text
R3=sum_r r*Cr=|C|+sum_(r=2)^11 (r-1)*Cr,
```

(4.2)--(4.3) yield

```text
R3 >= (561+q+G)+(1375+J)+(4*q+4*u)
   = 1936+5*q+G+J+4*u.                            (4.4)
```

This is exactly the master inequality used to derive

```text
Type I:
  R3+7*z >= 4612+J+4*y1,

Type II:
  R3+7*n5+7*two
     >= 4615+J+4*y1+4*delta+5*t1.
```

Thus `(V1)--(V3)` imply the audited `R3` rows.

The implication is strict already in the nonnegative rank-histogram
projection.  For example, in Type I with `z=y1=J=0`, take

```text
(C1,C2,C3,C4,C5,C6,...,C11)=(11,55,165,329,829,0,...,0).
```

The total number of cells is `1389`, and

```text
R3=11+2*55+3*165+4*329+5*829=6077>=4612,
```

so the scalar `R3` row holds with large slack.  But `C4>=330` fails.  This
is an arithmetic separation, not a claim that the displayed histogram is a
physical OR word.

## 5. A useful single weighted projection

The four exact-rank rows also imply the branch-independent capacity row

```text
sum_(r=1)^4 r*Cr >= 1936+E,                        (W4)
```

where

```text
E=sum_(r=1)^4 r*max(nr-C(11,r),0).
```

Indeed, (4.1) can be multiplied by `r` and summed.  `(W4)` is weaker than
the four separate rows but is a cheap useful propagation cut.  Unlike the
total `R3` inequality, neither `(W4)` nor `(V1)` allows a rank-five or
higher cell to supply rank capacity for a lower target.

## 6. Compact exact CNF realization

Reuse the `10197` exact pair/triple coordinate-contribution bits proposed
for the `R3` module.  Inactive pair/triple cells have the all-zero vector.
For each of the `464+463=927` possible pair/triple cells:

1. exact-popcount its eleven contribution bits into four binary bits;
2. define exact equality flags for ranks `2,...,5`;
3. define one exact flag for rank at least six.

The rank-one row needs no new flag or counter: every rank-one singleton is
a short cell and the existing exact histogram already has `n1>=11`.

With the source's audited two-variable/fourteen-clause full adder, the
existing Wallace routine uses exactly ten full adders on eleven inputs.
Thus the 927 per-cell popcounts cost

```text
18,540 variables / 129,780 clauses.                (6.1)
```

An equality to one fixed four-bit constant costs one output and five clauses
(four forward implications and one reverse clause).  Defining the four
rank flags costs

```text
3,708 variables / 18,540 clauses.                  (6.2)
```

An exact `rank>=6` flag can conservatively be defined by the sixteen-row
truth table of the four count bits, costing

```text
927 variables / 14,832 clauses.                    (6.3)
```

For 927 input flags the audited Wallace-plus-ripple counter uses 924 full
adders.  Five counters (four exact ranks and the high-rank tail) therefore
cost

```text
9,240 variables / 64,680 clauses.                  (6.4)
```

Adding the already existing singleton counters `nr`, forming `Cge5`, and
emitting the guarded comparisons costs fewer than

```text
500 variables / 4,000 clauses.                     (6.5)
```

Hence the rank-vector strengthening costs, beyond the exact `R3`
coordinate-contribution wires,

```text
fewer than 33,000 variables / 235,000 clauses.     (6.6)
```

If retained together with the audited total-`R3` popcount, the combined
increment remains below approximately

```text
68,000 variables / 465,000 clauses,
```

well under three percent of the current roughly twenty-million-clause
formula.  No per-target occurrence or assignment bank is needed.

### 6.1 Minimal deployment tier

The single row

```text
C4>=330
```

already separates the scalar `R3` relaxation in the example of Section 4.
It needs the same 927 local popcounts, but only one equality flag and one
counter.  The corresponding conservative increment beyond the contribution
wires is below

```text
22,000 variables / 150,000 clauses.
```

This is the natural first benchmark.  The other four exact-rank banks and
the high-tail counter can then be added without changing the local
popcounts.

## 7. Stronger pair/triple-resolved form

The same local popcounts support a strictly stronger and slightly cheaper
package.  Split the histogram into

```text
Pr = number of internal pair cells of actual OR-rank r,
Tr = number of internal triple cells of actual OR-rank r,
Tge5=T5+T6+...+T11.
```

In Type I and either tight Type-II mode, every lower target has a
singleton/pair witness.  Therefore

```text
nr+Pr >= C(11,r),  r=1,2,3,4.                     (L-pair)
```

The `r=1` instance is already implied by `n1>=11`.  In the non-tight
Type-II `(delta,s)=(0,1)` mode, the exact shortening radius is three, giving

```text
nr+Pr+Tr >= C(11,r),  r=1,2,3,4.                  (L-triple)
```

The selected rank-five schedule itself gives, in every branch,

```text
P5>=y1,
T5>=y2.                                           (S5)
```

Finally, the `y2` selected rank-five triples and the `u` contaminated
triples are disjoint.  Hence

```text
Tge5>=y2+max(y1-two+t1,0).                         (TC-exact)
```

A max-free implementation uses the conjunction

```text
Tge5>=y2,
Tge5>=y1+y2-two+t1.                               (TC-linear)
```

The first row is already implied by `T5>=y2`.  Thus no max wire is needed.
Rows `(L-pair)/(L-triple)`, `(S5)`, and `(TC-linear)` imply `(V1)--(V3)`:
the pair/triple lower rows imply the corresponding total `Cr` rows;
`P5+T5>=y1+y2=q` implies `(V2)`; and adding `P5>=y1` to `(TC-exact)` gives
the required overall rank-at-least-five tail.  The implication is strict
because, in a short-mode branch, triple cells of rank at most four cannot
compensate for a deficient singleton/pair pool.

This length-resolved package is the recommended physical cut.  It does not
double-count a triple incident with two selected pairs: `Tge5` counts the
physical triple once, and the incidence lemma supplies the number of
*distinct* contaminated triples.

### 7.1 Length-resolved CNF cost

The 927 per-cell popcounts still cost (6.1).  Exact rank flags `2,...,5`
are needed for the 464 pairs and 463 triples, while `rank>=6` is needed only
for triples.  This costs

```text
4,171 variables / 25,948 clauses.
```

Each exact counter on 464 or 463 inputs uses 460 full adders.  Four pair
counters and five triple counters therefore cost

```text
8,280 variables / 57,960 clauses.
```

With fewer than 500 variables / 4,000 clauses for additions, guards, and
comparisons, the stronger length-resolved package costs, beyond the exact
coordinate-contribution wires,

```text
fewer than 31,500 variables / 218,000 clauses.     (7.1)
```

It is both stronger and slightly smaller than the unsplit rank-vector
package, because no high-rank pair counter is required.

Strictness over the unsplit vector is immediate in the arithmetic
projection: in a tight branch, for example,

```text
n4=233, P4=96, T4=1
```

gives `C4=n4+P4+T4=330`, so the unsplit rank-four row is tight, but the
valid singleton/pair row has `n4+P4=329<330`.

## Scope

These are necessary redundant cuts, not a SAT/UNSAT result.  They are
strictly stronger than the scalar total-rank projection, but the full exact
OR formula may impose additional value- and position-sensitive constraints
not represented by the rank vector.
