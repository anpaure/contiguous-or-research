# Core-cell incidence cuts for the corrected `k=11,n=465` onion branches

## Status

This note proves new necessary conditions for the corrected Type-I branch and
for the one-core subbranches of Type II.  It does **not** change the proved
value of `nu(11)`, and it does not edit the production solver.

The main Type-I conclusions are

```text
S >= 649,                                             (I1)
3*S - 5*y1 >= 1938,                                  (I2)
6*S + 5*z >= 4254.                                   (I3)
```

Here

```text
z  = y0 = number of selected literal rank-five singleton witnesses,
y1 = number of selected rank-five witnesses of width one,
y2 = number of selected rank-five witnesses of width two,
S  = n1 + 2*n2 + 3*n3 + 4*n4.
```

Width is `right-left`, so widths one and two mean physical lengths two and
three.  In Type I, `z=n5` and `y0+y1+y2=462`, so (I2) is equivalently

```text
3*S + 5*z + 5*y2 >= 4248.                            (I2')
```

The same two short-core rows (I1)--(I2) hold in the corrected Type-II
duplicate/one-core case `(delta5,s)=(1,1)`.  In that case `z=n5-1`.
The three-cell argument also covers the Type-II two-component case with a
stronger boundary correction.  All three corrected Type-II cases have the
single physical form

```text
6*S+5*n5 >= 4254+5*tight,                            (II3)
```

where `tight` is the exact corrected stability-tight flag.  It is one in the
`(delta5,s)=(1,1)` and `(0,2)` cases and zero in the `(0,1)` case.

The proof is a weighted refinement of the named-cell Hall argument.  It
counts not just how many physical singleton/pair/triple cells exist, but the
total target-coordinate incidence those cells must carry.

## 1. Correct branch hypotheses

### 1.1 Type I

Normalize the unique literal rank-six entry to the first position.  Deleting
it leaves an exact rank-five equality word of length

```text
464 = C(11,5)+2.
```

Let `z` be the number of literal rank-five entries.  Exact rank-filtration
stability gives:

* the `z` literal rank-five values are distinct and occupy the two boundary
  blocks;
* all rank-at-most-four entries form one nonempty contiguous core `C`;
* `|C|=464-z`;
* the other `q=462-z` rank-five masks have selected witnesses in `C`;
* the inner slack is exactly

  ```text
  |C|-q=2.
  ```

Order those `q` incomparable selected rank-five witnesses by their left
endpoints.  The interval-slack normal form puts the `i`-th witness inside
`[i,i+2]`.  Consequently every core interval of length at least three
contains a selected rank-five witness.  In particular, every target of rank
at most four has a witness in `C` of physical length at most two.

Independently, the rank-six slack-three row implies that every physical
interval of length at least four contains a selected rank-six witness.
Therefore every selected rank-five witness has physical length at most
three.  The `q` nonliteral rank-five witnesses in `C` consequently split as

```text
y1 pairs and y2 triples,
y1+y2=q=462-z.
```

These statements are valid for all three corrected maximal rank-five state
chains A, B, and C.  No A-only assumption is used below.

### 1.2 Type-II duplicate/one-core branch

Write

```text
z      = number of distinct literal rank-five values,
delta5 = n5-z,
s      = number of rank-at-most-four components.
```

The corrected stability alternatives are

```text
(delta5,s) in {(0,1),(1,1),(0,2)}.
```

In the duplicate/one-core case `(delta5,s)=(1,1)`, deleting the one duplicate
literal occurrence gives the same rank-five equality geometry as in Type I:

```text
|C|=464-z=(462-z)+2.
```

Thus every lower target has a singleton/pair witness in `C`, and the
selected nonliteral rank-five witnesses are `y1` pairs and `y2` triples.
The literal selected singleton count is `y0=z`, while the physical literal
rank-five occurrence count is `n5=z+1`.

In the no-duplicate one-core case `(delta5,s)=(0,1)`, the low core has one
more unit of slack.  The singleton/pair conclusions need not hold, but every
rank-at-most-five target still has a witness of physical length at most three
by the global rank-six containment cap.  This is enough for the three-cell
row in Section 5.

## 2. Two path-capacity lemmas

Let

```text
C=(A1,...,AN),
ri=|Ai|,
S=sum_i ri.
```

All entries are nonempty.

### Lemma 2.1: rank capacity of singleton/pair cells

The total OR-rank of all singleton and adjacent-pair cells satisfies

```text
sum_i |Ai| + sum_(i=1)^(N-1) |Ai union A(i+1)|
    <= 3*S-r1-rN
    <= 3*S-2.                                        (2.1)
```

#### Proof

Use

```text
|Ai union A(i+1)| <= ri+r(i+1).
```

After summing, each internal `ri` occurs once as a singleton and twice in
adjacent pairs, while each endpoint rank occurs only once in a pair.  This
gives the first inequality.  Zero-freeness gives `r1,rN>=1`.  QED.

### Lemma 2.2: rank capacity through triples

For `N>=4`, the total OR-rank of every core interval of lengths one, two, or
three satisfies

```text
sum_(J subset C, 1<=|J|<=3) |U(J)|
 <= 6*S-3*r1-r2-r(N-1)-3*rN
 <= 6*S-8.                                          (2.2)
```

#### Proof

For every such interval,

```text
|U(J)| <= sum_(i in J) ri.
```

In the sum over all intervals of lengths at most three, the coefficient of
`ri` is

```text
3,5,6,...,6,5,3.
```

This proves the first inequality.  The four displayed boundary ranks are
positive, giving a total deficit of at least eight from `6*S`.  QED.

### Lemma 2.3: cells touched by one named coordinate

Fix a coordinate `b`, and let

```text
ob=#{i:b in Ai}.
```

The number of singleton and adjacent-pair cells meeting at least one marked
position is at most

```text
G2(N,ob)=ob+min(N-1,2*ob)=min(3*ob,N+ob-1).          (2.3)
```

Indeed there are `ob` marked singletons, every marked position is incident
with at most two path edges, and the path has only `N-1` edges.  Both bounds
are simultaneously sharp for an unconstrained marked path.

## 3. The Type-I named-coordinate cut

For a fixed coordinate `b`, the number of nonempty masks of ranks at most
four which contain `b` is

```text
sum_(t=1)^4 C(10,t-1)=1+10+45+120=176.              (3.1)
```

Every one of these 176 masks has a singleton/pair witness in `C`.  Witnesses
of distinct target masks are distinct physical cells, because one physical
cell has only one OR value.  Each of the 176 cells meets a core position
containing `b`.  Lemma 2.3 therefore gives

```text
G2(|C|,ob)>=176,
3*ob>=176,
ob>=59.                                             (3.2)
```

This holds for every one of the eleven coordinates.  Since each core entry
contributes once to `ob` for each coordinate it contains,

```text
sum_b ob = sum_(i in C)|Ai| = S.
```

Summing (3.2) proves

```text
boxed: S>=11*59=649.                                (I1)
```

The pointwise statement `ob>=59` is stronger than its aggregate.  The
aggregate is attractive computationally because it needs no named-coordinate
occurrence bank.

## 4. The Type-I weighted pair-cell cut

The total target-coordinate incidence of all nonempty masks of ranks one
through four is

```text
sum_(t=1)^4 t*C(11,t)
 =11*(C(10,0)+C(10,1)+C(10,2)+C(10,3))
 =11*176
 =1936.                                             (4.1)
```

Choose one singleton/pair witness in `C` for each of those 561 lower masks.
In addition, the selected rank-five row has exactly `y1` pair witnesses in
`C`.  These `561+y1` cells are all distinct:

* lower targets have different OR values from one another;
* selected rank-five targets have different OR values from one another;
* a rank-five target cannot share a cell with a lower target.

The required cells therefore have total OR-rank

```text
1936+5*y1.                                          (4.2)
```

They are a subfamily of all singleton/pair cells of `C`.  Lemma 2.1 gives

```text
1936+5*y1 <= 3*S-2.
```

Hence

```text
boxed: 3*S-5*y1>=1938.                              (I2)
```

Since `y1=462-z-y2`, this is equivalently

```text
boxed: 3*S+5*z+5*y2>=4248.                          (I2')
```

This row is a weighted strengthening of the existing unweighted named-cell
Hall row `y2>=96+z`.

By Section 1.2, the proofs of Sections 3 and 4 apply verbatim under the exact
corrected Type-II guard `(delta5,s)=(1,1)`.  The `z` in those proofs is the
number of distinct literal values, so `z=n5-1` in that branch.

## 5. The three-cell incidence cut

Now include every selected nonliteral rank-five witness, not only the pair
witnesses.  There are `462-z` of them, and every one has physical length at
most three.  Together with all lower targets, the required distinct cells
have total OR-rank

```text
1936+5*(462-z)=4246-5*z.                             (5.1)
```

They form a subfamily of all intervals in `C` of lengths at most three.
Lemma 2.2 yields

```text
4246-5*z <= 6*S-8.
```

Therefore

```text
boxed: 6*S+5*z>=4254.                               (I3)
```

Unlike (I1)--(I2), this argument needs only a single low component and the
global length-at-most-three cap.  It consequently applies to:

* Type I, with `z=n5`;
* Type II `(delta5,s)=(0,1)`, with `z=n5`;
* Type II `(delta5,s)=(1,1)`, with `z=n5-1`.

In physical `n5` notation, the duplicate Type-II version is

```text
6*S+5*n5>=4259.                                     (5.2)
```

### 5.1 The Type-II two-component correction

In the remaining corrected case `(delta5,s)=(0,2)`, write the two low
components as `C1,C2`, with lengths `N1,N2`, rank sums `S1,S2`, and assigned
nonliteral rank-five witness counts `q1,q2`.

A lower-target witness is internal to one low component: crossing a literal
rank-five separator would make its OR-rank at least five.  A selected
nonliteral rank-five witness is also internal.  If it contained a literal
rank-five entry `A` while its target were `B`, then

```text
A subset B and |A|=|B|=5,
```

so `A=B`, contrary to `B` being nonliteral.

The local slacks are one and two.  Hence the slack-one component has length
at least one and the slack-two component has length at least two.  For a
nonempty component of length one, the difference between `6*Sj` and the
rank capacity of all its length-at-most-three cells is at least five.  For
every component of length at least two, that difference is at least eight:

```text
length 1 coefficient:       1,       defect at least 5;
length 2 coefficients:      2,2,     defect at least 8;
length 3 coefficients:      3,4,3,   defect at least 8;
length >=4 coefficients:    3,5,6,...,6,5,3, defect at least 8.
```

The two components therefore have total boundary defect at least `5+8=13`.
All 561 lower targets and all `462-z` selected nonliteral rank-five targets
still require distinct internal cells of lengths at most three.  Consequently

```text
4246-5*z <= 6*S-13,
```

and

```text
boxed: 6*S+5*z>=4259                for (delta5,s)=(0,2).  (5.3)
```

Here `n5=z`.  Combining (I3), (5.2), and (5.3) gives the promised unified
Type-II row

```text
boxed: 6*S+5*n5>=4254+5*tight.                       (II3)
```

## 6. Exact A/B/C boundary formulas

Let

```text
0<=h1<=h2<=h3<=h4<=h5<=h6<=462
```

be the six transition positions of the selected corrected rank-five state
chain.  The exact `y0,y2` formulas are:

| chain | states | `y0=z` | `y2` |
|---|---|---:|---:|
| A | `00 01 02 12 13 23 33` | `462+h1-h6` | `h3+h5-h2-h4` |
| B | `00 01 02 12 22 23 33` | `462+h1+h5-h4-h6` | `h3-h2` |
| C | `00 01 11 12 13 23 33` | `462+h1+h3-h2-h6` | `h5-h4` |

In all three cases, subtraction from `y0+y1+y2=462` gives the same formula

```text
y1=h2+h4+h6-h1-h3-h5.                              (6.1)
```

Thus (I2) has one chain-independent unsigned form:

```text
3*S+5*(h1+h3+h5) >= 1938+5*(h2+h4+h6).             (6.2)
```

The three guarded forms of (I3) are:

```text
A: 6*S+5*h1       >= 1944+5*h6,
B: 6*S+5*h1+5*h5  >= 1944+5*h4+5*h6,
C: 6*S+5*h1+5*h3  >= 1944+5*h2+5*h6.               (6.3)
```

These formulas explicitly retain the internal `22` block on B and the
internal `11` block on C.  They must not be attached to the old unsound
A-only singleton equation.

## 7. Relation to existing cuts

### 7.1 Logical source

The existing named-cell Hall theorem uses the same core geometry only at the
level of cell cardinality.  It proves that all 561 lower masks occur among
the `|C|` singletons and `|C|-1` pairs and derives

```text
y2>=96+z.
```

Rows (I1)--(I3) retain target rank, equivalently target-coordinate
incidence, and compare it with the rank capacity of those physical cells.
The unweighted count does not contain this information.

The existing global pair-profile row

```text
n1+2*n2>=110
```

uses only rank-one and rank-two target structure.  It neither controls all
eleven named coordinate occurrence counts nor accounts for the 165 rank-three
and 330 rank-four targets.

The facet and ridge pin-load rows are localized to fixed faces of the
normalized endpoint six-set.  In contrast, `ob>=59` holds for every one of
the eleven coordinates, including all five coordinates outside that endpoint.

### 7.2 Exact redundancy regions among the new rows

The three rows are not mutually redundant.

* (I2) implies (I1) when `y1>=2`; (I1) is needed only at `y1=0,1` after
  (I2) is present.
* (I3) implies (I1) when `z<=73`; (I1) implies (I3) when `z>=72`.
  At `z=72,73` the two integer lower bounds overlap.
* Doubling (I2) implies (I3) whenever

  ```text
  2*y1+z>=76.
  ```

  Thus (I3) is most relevant in the low-`z`, low-`y1`, triple-heavy corner.

### 7.3 Arithmetic separation examples

The following are integer endpoint/rank profiles, not claimed OR words.
Their purpose is to show that the new rows are not algebraic rewrites of the
current scalar count, fan, moment, named-cell, and pair-profile rows.

1. **(I1) is independent of (I2)--(I3).**  Take chain A with

   ```text
   (h1,...,h6)=(0,0,181,181,362,362),
   (z,y1,y2)=(100,0,362),
   (n1,n2,n3,n4)=(81,283,0,0).
   ```

   Then `|C|=364`, `S=647`, (I2) and (I3) hold, but (I1) fails.

2. **(I2) is independent of (I1),(I3).**  Take the valid chain-B boundary
   profile already used in the singleton-boundary repair audit,

   ```text
   (h1,...,h6)=(20,70,270,320,321,383),
   (z,y1,y2)=(100,162,200),
   (n1,n2,n3,n4)=(11,353,0,0).
   ```

   Here `S=717`; (I1) and (I3) hold, while

   ```text
   3*S-5*y1=1341<1938.
   ```

3. **(I3) is independent of (I1)--(I2).**  Take chain A with

   ```text
   (h1,...,h6)=(0,0,231,231,462,462),
   (z,y1,y2)=(0,0,462),
   (n1,n2,n3,n4)=(279,185,0,0).
   ```

   Then `|C|=464`, `S=649`; (I1)--(I2) hold, while

   ```text
   6*S+5*z=3894<4254.
   ```

All three examples satisfy `n1+2*n2>=110`, the Type-I low-entry count, the
`n5<=133` cap, the six-set support-moment scalar row, and the applicable
unweighted named-cell/fan inequalities.  This is an arithmetic separation
from the published scalar comparators, not a claim of satisfiability under
the full OR clauses.

## 8. Compact CNF design

The aggregate rows are much cheaper than encoding the eleven named counts
`ob` separately.

### 8.1 Shared exact `S` bank

Reuse the exact one-hot literal-rank flags

```text
rank[p][1],...,rank[p][4]
```

from `LocalDensityPBPlan`.  Count `n1,...,n4` exactly and form

```text
S=n1+2*n2+3*n3+4*n4
```

with retained-carry unsigned ripple addition.

Using the current Wallace/ripple primitives:

* an exact count of 465 literals uses 461 full adders, hence 922 variables
  and 6,454 clauses;
* four standalone counts use 3,688 variables and 25,816 clauses;
* the weighted sum uses 43 further full adders, hence 86 variables and 602
  clauses.

Thus a standalone exact `S` bank costs

```text
3,774 variables / 26,418 clauses.                   (8.1)
```

If the existing Type-I global-pair-profile module is refactored to expose its
exact `n1,n2` and `n1+2*n2` wires, only the `n3,n4` counters and 33 additional
full adders are needed:

```text
1,910 variables / 13,370 clauses.                   (8.2)
```

This refactor is optional and must preserve guard-off identity.

The direct comparison `S>=649` has four first-difference clauses because

```text
649=2^9+2^7+2^3+1.
```

### 8.2 Boundary arithmetic for (I2)--(I3)

Use the already extracted nine-bit `h1,...,h6` wires.  Materialize

```text
Mi=5*hi=hi+(hi<<2),
T =3*S =S+(S<<1).
```

Then compare (6.2) once and the three rows in (6.3) under their exact chain
selectors.  A straightforward shared circuit uses:

* 293 full adders: 586 variables and 4,102 clauses;
* one 16-bit and three 17-bit lexicographic comparators: 63 variables and
  382 clauses;
* four direct constant-comparison clauses for `S>=649`.

One reproducible 293-adder breakdown is

```text
six Mi=5*hi values                         66
T=3*S                                     14
the two three-term odd/even h sums        50
the two sides of (6.2)                    29
the A, B, C sides of (6.3)          28+53+53
                                           ---
                                           293.
```

The aggregate-row circuit beyond the `S` bank is therefore

```text
649 variables / 4,488 clauses.                      (8.3)
```

Up to constant-size branch-guard glue, all three rows together cost

```text
standalone: 4,423 variables / 30,906 clauses,
with n1,n2 reuse: 2,559 variables / 17,858 clauses.  (8.4)
```

All carries must be retained.  The comparisons should be guarded as follows:

* (I1)--(I2): Type I, or the exact corrected Type-II duplicate/one-core flag;
* the A/B/C forms of (I3): Type I;
* Type II: use the unified physical row (II3) in all three corrected cases;
* each formula in (6.3): additionally by its exact A/B/C selector.

No clause should be emitted when the corresponding top-level option is off.
The module must depend on the corrected rank-five singleton-count repair;
using the old A-only `y0` proxy would be unsound.

If the Type-II plan already exposes its exact `n5` count and corrected
`tight` flag, (II3) is cheaper than substituting `z` chain by chain.  Reuse
`6*S`, form `5*n5` with eleven full adders, and add it to `6*S` with sixteen
more.  Two guarded direct constant comparisons enforce `>=4254` when
`!tight` and `>=4259` when `tight`.  This adds only

```text
54 variables / 389 clauses                         (8.5)
```

beyond a shared `S,6*S` bank.

### 8.3 Optional pointwise bank

For stronger propagation one may encode `ob>=59` separately for all eleven
coordinates.  If exact low-position flags already exist, define

```text
occ[p,b] <-> low[p] AND A[p][b].
```

Using 465 inputs per coordinate, eleven AND banks, eleven exact counters, and
the direct `>=59` comparators costs

```text
15,257 variables / 86,394 clauses.                  (8.6)
```

This is still moderate relative to the full exact CNF, but the aggregate
`S>=649` row should be benchmarked first.

## 9. Recommended next step

1. Independently audit Sections 2--6, especially the corrected Type-II
   guards and the A/B/C substitutions.
2. Implement only the aggregate `S` bank and rows behind a new opt-in guard.
3. Run build-only inventory and clause-stream audits before any solve.
4. Benchmark the rows separately and jointly on corrected Type I and all
   three corrected Type-II cases.

These are necessary propagation cuts, not a proof of infeasibility at
length 465.
