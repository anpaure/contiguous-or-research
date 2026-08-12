# The nonsaturated `k=11` core has one lower-ideal defect cell

## 1. Verdict

Assume that a zero-free universal word of length `465` exists in the
principal nonsaturated branch

```text
no literal rank-six entry,
no repeated literal rank-five value,
one rank-at-most-four component.
```

In the corrected filtration notation this is the Type-II mode

```text
(delta_5,s)=(0,1).
```

Let `n5` be the number of literal rank-five entries, let `C` be the unique
rank-at-most-four component, and let `y1,y2` count the selected nonliteral
rank-five pair and triple witnesses.  Then

```text
N:=|C|=465-n5,
q:=462-n5=N-3,
y1+y2=q.
```

The new structural conclusion is:

> Among all `N-2=q+1` triples internal to `C`, at most one can have OR-rank
> below five.  Consequently all but at most one of the 561 masks of ranks
> one through four have a singleton or adjacent-pair witness in `C`.

The single possible exception is not an unspecified triple.  The complete
rank-five endpoint schedule is necessarily the outer chain

```text
A: 00,01,02,12,13,23,33.
```

If the `12` block is nonempty, there is no exceptional triple.  If that
block is empty, there is exactly one triple not already selected at rank
five or contaminated by a selected rank-five pair.  With the usual chain-A
boundaries it is

```text
H=[h3,h3+2].
```

It is the only cell which can carry the one lower-ideal exception.

This gives the new necessary rows

```text
y2 >= 93+n5+Delta_lit,                          (H0-01+)
3*S-E-5*y1 >= 1934,                             (H1-01)
```

where

```text
Delta_lit = total repetition excess of literal values of ranks 1,...,4,
F=sum_(r=1)^4 max(nr-C(11,r),0),
E=sum_(r=1)^4 r*max(nr-C(11,r),0),
S=n1+2*n2+3*n3+4*n4.
```

Always `Delta_lit>=F`, so `(H0-01+)` strictly strengthens the histogram row
proved below whenever literal values repeat before a rank count exceeds the
size of its layer.

The first row is sharpened by one whenever no genuine carrier is needed
(in particular when `H` is absent or has rank at least five).  Every
coordinate occurs in at least 59 core positions and is omitted
in at least 193 core positions.  Thus the occurrence thresholds previously
available only in the tight short-core modes extend to the hardest
nonsaturated mode.

These statements do not refute length `465`.  They give a lossless exact
template and new global lower-capacity cuts inside its hardest branch.

The zero-margin subbranch is considerably more rigid.  A genuinely needed
carrier has rank three or four.  The slice `n5=134` has no zero-margin
word.  At `n5=133`, zero margin forces an exact nested word

```text
P4 || D3 || Q4
```

in which every pair outside `D3` is selected at rank five, all but two
consecutive pairs inside `D3` are selected at rank four, the two exceptional
pairs are the only nonliteral masks below rank four, every other internal
triple is selected at rank five, and every internal four-window is a
distinct rank-six witness.  Equations (6.2)--(6.6) give the exact counts, seam
types, and coordinate-run identities.

## 2. Inputs re-audited

The initial one-defect path reduction uses the following established
equality facts.

1. Rank-six equality and absence of a literal six-set imply that every word
   entry has rank at most five.
2. In mode `(delta_5,s)=(0,1)`, deleting the `n5` literal five-set positions
   leaves one contiguous component `C` of length `N=465-n5`.
3. Every literal five-set value is distinct.  Reselect its literal occurrence
   as its rank-five witness.  The other `q=462-n5` five-sets have witnesses
   wholly inside `C`.
4. Every rank-five witness has physical length at most three.  This follows
   directly from the rank-six antichain at slack three: every physical
   interval of length four contains a selected rank-six witness.

For item 3, a witness for a nonliteral five-set cannot contain a literal
five-set entry.  If it contained literal value `R` and had OR `T`, then
`R subseteq T` and `|R|=|T|=5`, forcing `R=T`, contrary to `T` being
nonliteral.  Hence the `q` selected nonliteral witnesses really are internal
to `C`.

The selected internal witnesses are pairwise interval-incomparable.  If one
contained another, their two OR values would be comparable five-sets and
therefore equal, while the selected targets are distinct.  No fixed middle
row, Johnson path, or natural grading is assumed.

The later nested rank-four and coordinate sections additionally invoke the
previously proved named-cell shortening, rank-four surplus-component,
boundary--core rigidity, and coordinate-transversal theorems. Their use is
flagged where it occurs; the four-item list above is not meant to replace
those later inputs.

## 3. General one-defect path lemma

### Lemma 3.1

Let a segment of length `N=q+3` contain selected incomparable witnesses for
`q` distinct rank-`r` targets.  Suppose every selected witness has length two
or three and every lower-rank target represented in the segment has a
witness of length at most three.

Then at most one physical triple can have OR-rank below `r`.  Equivalently,
all but at most one lower-rank target have a singleton or adjacent-pair
witness.

### Proof

View the `N-1` adjacent-pair cells as the vertices of a path; its `N-2`
edges are the physical triples, each incident with its two contained pair
cells.  Let `a` selected rank-`r` witnesses be pairs and `b` be triples, so

```text
a+b=q.
```

The selected pair vertices form a proper subset of the pair path: indeed

```text
a<=q=N-3<(N-1).
```

In fact at least two pair vertices are unselected.  Decompose the selected
vertices into runs.  An internal run of length `ell` is incident with
`ell+1` path edges, while a run touching one endpoint is incident with
`ell` edges.  Since the complement has at least two vertices, summing over
the runs shows that at least `a` distinct physical triples contain a
selected pair.

None of the `b` selected triple witnesses contains a selected pair witness.
Such containment would make the corresponding distinct rank-`r` OR values
comparable, which is impossible.  Thus at least

```text
a+b=q
```

of the `N-2=q+1` triples are either selected rank-`r` witnesses or contain a
selected rank-`r` pair.  At most one triple remains.

A lower-rank triple witness is neither selected at rank `r` nor allowed to
contain a selected rank-`r` pair.  It must be the one remaining triple.
One physical cell has one OR value, so it can account for at most one lower
target.  QED.

### Application to `k=11`

The named-cell shortening lemma gives every rank-at-most-four target a
witness of length at most three in `C`.  Apply Lemma 3.1 with `r=5` and
`q=N-3`.  This proves the verdict without using a state-chain formula.

The inequality `T_ge5>=q` in the earlier residual pair/triple incidence
note is the rank-tail projection of the same path argument.  The advance
here is to identify its simultaneous lower-ideal consequence, its unique
carrier cell, and the resulting Hall and incidence rows.

## 4. Exact chain-A template and the carrier cell

Choose one witness for each of the 462 five-sets, including every distinct
literal occurrence as its singleton witness, and order the intervals by
left endpoint:

```text
I_j=[ell_j,r_j],  0<=j<462.
```

Their right endpoints are also strictly increasing.  Put

```text
alpha_j=ell_j-j,
beta_j =r_j-j.
```

There are 462 distinct left and right endpoints in 465 positions, so

```text
0<=alpha_j<=beta_j<=3.
```

Strict endpoint increase makes both sequences nondecreasing.  The
length-three cap gives `beta_j-alpha_j<=2`.

Because `delta_5=0`, every literal rank-five position is one of the selected
singleton cells.  Since the low positions form one component, those literal
positions are precisely two boundary blocks.  Therefore no selected
singleton can have an internal diagonal state `11` or `22`.  The remaining
non-diagonal states are totally ordered:

```text
01 < 02 < 12 < 13 < 23.
```

Together with the two boundary diagonal states, the schedule is necessarily
chain A.  For boundaries

```text
0<=h1<=h2<=h3<=h4<=h5<=h6<=462,
```

the exact selected intervals are

```text
00: I_j=[j,j]       for 0 <=j<h1,
01: I_j=[j,j+1]     for h1<=j<h2,
02: I_j=[j,j+2]     for h2<=j<h3,
12: I_j=[j+1,j+2]   for h3<=j<h4,
13: I_j=[j+1,j+3]   for h4<=j<h5,
23: I_j=[j+2,j+3]   for h5<=j<h6,
33: I_j=[j+3,j+3]   for h6<=j<462.
```

Hence

```text
C=[h1,h6+2],
n5=462+h1-h6,
y1=(h2-h1)+(h4-h3)+(h6-h5),
y2=(h3-h2)+(h5-h4).
```

The selected pair starts are

```text
[h1,h2-1], [h3+1,h4], [h5+2,h6+1],
```

and the selected triple starts are

```text
[h2,h3-1], [h4+1,h5].
```

If `h3<h4`, every core triple is selected or contains a selected pair.  If
`h3=h4`, the sole exception is exactly

```text
H=[h3,h3+2].                                      (4.1)
```

Indeed the triples before `H` are covered successively by the first pair
block and the `02` block, while the triples after `H` are covered by the
`13` block and the last pair block.  This also audits all zero-length block
cases.

Write

```text
e=1 if h3=h4 and |OR(H)|<=4, and e=0 otherwise,
rho=|OR(H)| when e=1, and rho=0 when e=0.
```

Then every lower target other than possibly `OR(H)` has a singleton/pair
witness, and the possible exception has rank `rho`.

## 5. Quantitative consequences

### 5.1 Unweighted Hall row

There are `N` singleton cells and `N-1-y1` pair cells not already selected
as rank-five pair witnesses.  At most the one carrier `H` can be added.
Distinct lower targets require distinct cells, so

```text
561 <= N+(N-1-y1)+e.                              (5.1)
```

Using `N=465-n5` and `y1+y2=N-3` gives the exact guarded form

```text
y2 >= 94+n5-e.                                    (5.2)
```

In particular `e<=1` proves

```text
y2 >= 93+n5.                                      (5.3)
```

Now let `nr` be the number of rank-`r` singleton entries in `C`.  At most
`C(11,r)` of those positions can serve distinct rank-`r` singleton targets.
Thus at most `N-F` singleton cells are useful, where

```text
F=sum_(r=1)^4 max(nr-C(11,r),0).
```

Replacing `N` by `N-F` in (5.1) proves

```text
y2 >= 94+n5+F-e >= 93+n5+F.                       (H0-01)
```

In the exact chain-A boundary variables this is the unsigned row

```text
h3+h5+h6 >= h1+h2+h4+555+F,                       (5.3a)
```

with `555` replaced by `556-e` in the carrier-resolved version.

This is the nonsaturated analogue of the existing tight-core histogram Hall
rows.  It cuts, for example, the previously recorded scalar-feasible profile
`(n5,y1,y2)=(134,107,221)`, because it requires `y2>=227` even when `F=0`.
That arithmetic separation is not a claim that the old profile was an OR
word.

### 5.1a Injective collision map across ranks two through five

The histogram correction `F` can be replaced by the full literal-value
repetition excess.  For `1<=r<=4`, let `zr` be the number of distinct
literal rank-`r` values occurring in `C`, and put

```text
Delta_lit=N-(z1+z2+z3+z4).
```

Universality forces `z1=11`.  Since `zr<=min(nr,C(11,r))`,

```text
Delta_lit>=F.                                     (5.3b)
```

Exactly

```text
561-(z1+z2+z3+z4)=96+n5+Delta_lit                (5.3c)
```

lower masks are not literal values.  Let `v` be one precisely when a
nonliteral lower target has no singleton/pair witness and must use the
carrier `H`, and zero otherwise.  Thus `v<=1`; a low `H` which merely
repeats a literal value, or whose value has another pair witness, has
`v=0`.  Every one of the other nonliteral lower targets must use an
adjacent pair.

In fact a genuine carrier has rank three or four.  Rank one is necessarily
literal.  If three nonempty entries `X,Y,Z` have two-set union `T` and
neither adjacent pair has union `T`, then both `X union Y` and
`Y union Z` are nonempty proper subsets of `T`, hence singletons.  They
both contain `Y`, so they are the same singleton, contradicting
`X union Y union Z=T`.  Thus every rank-two triple target already has an
adjacent-pair witness.  Consequently

```text
v=1 implies rho in {3,4}.                          (5.3c')
```

Map those `96+n5+Delta_lit-v` targets to their chosen pair cells, and map
the `y1` selected rank-five pair targets to their pair cells.  This is an
injection: within each rank the target values are distinct, and one cell
cannot have two OR-ranks.  There are only `N-1=464-n5` physical pairs in
the core.  Hence

```text
y1+2*n5+Delta_lit <=368+v.                        (5.3d)
```

Using `y1+y2=462-n5` gives the carrier-resolved form

```text
y2>=94+n5+Delta_lit-v,                            (5.3e)
```

and therefore the unconditional strengthening

```text
y2>=93+n5+Delta_lit.                              (H0-01+)
```

This is the requested collision map: rank-two, rank-three, rank-four, and
rank-five pair witnesses compete injectively for the same physical path
edges.  It is strictly stronger than merely counting surplus singleton
positions.

### 5.2 One rank-resolved defect

Let `Pr` be the number of internal pair cells whose actual OR-rank is `r`.
For `1<=r<=4`, choose lower witnesses as above and let `epsilon_r` record
whether the unique carrier is used at rank `r`.  Then

```text
nr+Pr >= C(11,r)-epsilon_r,
sum_r epsilon_r <=1.
```

The two-set argument in Section 5.1a sharpens this to

```text
epsilon_1=epsilon_2=0,
n1+P1>=11,
n2+P2>=55;                                       (5.3f)
```

only the rank-three and rank-four rows can spend the common defect.

Consequently

```text
nr+Pr >= C(11,r)-1,                               (5.4)
sum_(r=1)^4 max(C(11,r)-nr-Pr,0) <=1.             (5.5)
```

The stronger exact form has `epsilon_r=1` only when `v=1`,
`r=rho`, and `rho in {3,4}`.  Thus the triple allowance cannot be spent
independently in four rank rows; every possible shortage is carried by one
named mask.

For any coordinate set `B`, the same argument gives

```text
nr(B)+Pr(B)
  >= C(11-|B|,r)-1_{v=1,r=rho,OR(H) intersect B=empty}.   (5.6)
```

This is a single-carrier strengthening of the previous non-tight
singleton/pair/triple omission hierarchy.

### 5.3 Weighted rank-incidence row

The total rank incidence of the lower ideal is

```text
sum_(r=1)^4 r*C(11,r)=1936.
```

Put `rho_c=v*rho`, so `rho_c` is zero unless the carrier is genuinely
needed and otherwise belongs to `{3,4}`.  The targets assigned to
singleton/pair cells have total rank `1936-rho_c`.  Useful singleton
witnesses have total rank at most `S-E`.  The sum of the OR-ranks of all
internal pair cells is at most

```text
2*S-r_first-r_last <=2*S-2.
```

The `y1` selected rank-five pair witnesses consume exactly `5*y1` of that
pair capacity.  Therefore

```text
1936-rho_c+5*y1 <=3*S-E-2,
3*S-E-5*y1 >=1938-rho_c.                          (5.7)
```

Since `rho_c<=4`, the unconditional row is

```text
3*S-E-5*y1 >=1934.                                (H1-01)
```

If no genuine carrier is needed, the tight-core constant `1938` holds
even though the component slack is three.

### 5.4 Coordinate occurrence and omission

Fix a coordinate `b`, and let

```text
ob=#{i in C:b in A_i},
Zb=N-ob.
```

There are 176 lower masks containing `b`.  At most one can use `H`, so at
least 175 have singleton/pair witnesses.  The number of singleton/pair cells
meeting the `ob` marked positions is at most `3*ob`.  Hence

```text
3*ob>=175,
ob>=59.                                           (5.8)
```

There are 385 lower masks omitting `b`.  At least 384 have singleton/pair
witnesses.  If the `Zb` unmarked positions have `Rb` nonempty runs, their
singleton/pair cells number exactly `2*Zb-Rb`.  Thus

```text
2*Zb-Rb>=384.
```

Here `Rb>=1`, so

```text
Zb>=193.                                          (5.9)
```

The exact effective-carrier refinement is

```text
b in OR(H):     at least 175 containing and all 385 omitting targets
                use singleton/pair cells;
b notin OR(H):  all 176 containing and at least 384 omitting targets
                use singleton/pair cells.
```

These two exceptional counts apply only when `v=1`; if `v=0`, both full
counts `176,385` apply.  In particular the old
nonsaturated omission threshold `Zb>=130`, obtained by crediting every
triple independently, can be raised to `193` without assuming tightness.
Summing (5.8) over all coordinates also gives

```text
S>=649                                             (5.10)
```

in the nonsaturated mode.  Summing (5.9) gives the complementary upper
incidence row

```text
11*N-S>=2123,
S<=2992-11*n5.                                    (5.11)
```

### 5.5 Endpoint-pair exclusion in every coordinate section

The occurrence bounds above still credited selected rank-five pair cells as
if they could carry lower targets.  Removing those cells gives an exact
stronger coordinate ledger.

For a coordinate `b`, let

```text
ab = number of selected rank-five pair witnesses whose value omits b,
cb = y1-ab = number whose value contains b.
```

Every selected pair value has rank five, so

```text
sum_b ab=6*y1,
sum_b cb=5*y1.                                    (5.12)
```

When `v=1`, put

```text
db=1 if b notin OR(H), and 0 otherwise,
fb=1 if b     in OR(H), and 0 otherwise.
```

When `v=0`, put `db=fb=0`.  Thus `db` records that `H` can supply one of
the 385 lower masks omitting `b`, while `fb` records that it can supply one
of the 176 lower masks containing `b`.

The `b`-free singleton/pair cells in the core number exactly

```text
2*Zb-Rb.
```

The `ab` selected rank-five pairs among them are unavailable to the lower
ideal.  Therefore

```text
2*Zb-Rb-ab >=385-db.                              (5.13)
```

The total singleton/pair family has `2*N-1` cells.  Its cells containing
`b` number

```text
(2*N-1)-(2*Zb-Rb)=2*ob+Rb-1.
```

After the `cb` selected rank-five pairs are removed, the containing targets
give

```text
2*ob+Rb-1-cb >=176-fb.                            (5.14)
```

Adding (5.13)--(5.14) recovers the carrier-resolved Hall row (5.1), so no
cell has been charged twice.

Since `Rb>=1`, (5.13) implies the pointwise integer bound

```text
Zb >=193+ceil((ab-db)/2).                         (5.15)
```

Since a binary word with `ob` marked positions has at most `ob+1` zero
runs, (5.14) implies

```text
ob >=ceil((176-fb+cb)/3).                         (5.16)
```

These contain (5.8)--(5.9) as their `ab=cb=0` projections.

The exact aggregate rounding is useful.  Set

```text
Komit=max(0,ceil((6*y1-v*(11-rho))/2)),
Khit =max(0,ceil((5*y1-11-v*rho)/3)).              (5.17)
```

For omission, each of the `v*(11-rho)` coordinates omitted by `H` can
absorb the first unit of `ab` without increasing the baseline 193; every
two remaining units cost another omitted position.  For occurrence, the
baseline `ob=59` absorbs one unit of `cb` in every coordinate and a second
unit in each of the `v*rho` coordinates contained in `H`; every three
remaining units cost another occurrence.  Hence

```text
649+Khit <= S <= 11*N-2123-Komit.                 (5.18)
```

Because a genuine carrier has rank three or four, (5.18) has the following
unconditional projection, with no carrier flag:

```text
649+max(0,ceil((5*y1-15)/3))
 <=S
 <=11*N-2123-max(0,ceil((6*y1-8)/2)).              (5.18a)
```

In particular, if there is no genuine carrier (`v=0`),

```text
S >=649+max(0,ceil((5*y1-11)/3)),
S+3*y1 <=11*N-2123.                               (5.19)
```

These are endpoint-chain incidence cuts: they use not only that the lower
ideal is short, but that the `y1` occupied pair cells carry five-sets and
therefore remove six omission slots and five occurrence slots apiece.

### 5.6 All-codimension omission hierarchy

The pair-exclusion argument is not restricted to one coordinate.  Fix
`B subseteq [11]`, put `t=|B|`, and let

```text
ZB = #{i in C:A_i intersect B=empty},
RB = number of B-free runs in C,
aB = # selected rank-five pair values disjoint from B,
dB = 1 if v=1 and OR(H) intersect B=empty, else 0.
```

There are

```text
L(t)=sum_(r=1)^4 C(11-t,r)                        (5.20)
```

lower targets disjoint from `B`.  At most `OR(H)` can avoid the
singleton/pair family.  The `B`-free singleton/pair cells number
`2*ZB-RB`, and the `aB` selected rank-five pair cells are unavailable.
Therefore the exact pointwise row is

```text
2*ZB-RB-aB >= L(t)-dB.                            (5.21)
```

For `t<=10`, universality of the singleton outside `B` implies `ZB>0`,
and hence `RB>=1`.  Summing (5.21) over every `t`-set `B` gives the
rank-histogram moment

```text
2*sum_(i in C) C(11-|A_i|,t)
  >= C(11,t)*(L(t)+1)+C(6,t)*y1
       -v*C(11-rho,t).                            (5.22)
```

Here each entry is disjoint from `C(11-|A_i|,t)` choices of `B`, each
selected five-set pair value is disjoint from `C(6,t)` choices, and the
carrier is disjoint from `C(11-rho,t)` choices.  Equation (5.22) is a new
global lower-bound hierarchy coupling literal ranks to the endpoint chain.
The `t=1` member is the non-rounded aggregate behind (5.18); the pointwise
rows retain the stronger coordinatewise rounding.

For illustration, `t=6` gives

```text
2*(210*n1+84*n2+28*n3+7*n4)
  >=14322+y1-v*C(11-rho,6).                       (5.23)
```

No target assignment variables occur in this derivation.  The hierarchy is
valid simultaneously for all `B`; the one possible deficit is always the
same carrier mask `OR(H)`, rather than an independently spendable unit in
each section.

### 5.7 Nested rank-four stability when `n5` is near 134

The nonsaturated core itself covers every mask through rank four and has

```text
|C|=465-n5=331+e4,
e4=134-n5.                                        (5.24)
```

For rank four,

```text
M4=C(11,4)=330,
d4=1,
L4=C(11,1)+C(11,2)+C(11,3)=231.
```

Delete the literal rank-four entries of `C`.  Let `x4` be their repetition
excess and `s3` the number of nonempty rank-at-most-three components.  The
surplus-component proof, applied anew inside the physical core, gives

```text
0<=x4<=e4,
s3<=1+e4-x4.                                      (5.25)
```

The total selected rank-four slack across those components is exactly
`1+e4-x4`.  Whenever `s3<4`, the coordinate-transversal theorem
also forces at least one of the rank-at-most-three components to have total
OR `[11]`.

There is a rank-four/rank-five pair-packing law valid throughout this
nonsaturated mode.  Put

```text
z4=n4-x4
```

for the number of distinct literal rank-four values, and select those values
as singleton witnesses.  Let `v4` count selected nonliteral rank-four triple
witnesses.  Every such cell has OR-rank four, so the outer one-defect theorem
gives

```text
v4<=1.                                            (5.25a)
```

The other `330-z4-v4` nonliteral rank-four targets occupy adjacent pairs.
They are disjoint from the `y1` selected rank-five pair cells.  Since `C`
has `N-1=464-n5` physical pairs,

```text
y1 <=134-n5+z4+v4
    =134-n5+n4-x4+v4.                             (5.25b)
```

If `v4=1`, that triple is necessarily the same physical carrier `H`, has
`rho=4`, and forces `h3=h4` in the outer chain-A schedule.  This couples two
successive rank filtrations through actual cells rather than through their
separate width marginals.

The endpoint cases are especially rigid.

* If `n5=134`, then `e4=0`.  Exact rank-four boundary--core rigidity gives

  ```text
  C=P4 || D3 || Q4,
  ```

  where the literal rank-four entries in `P4,Q4` are distinct, `D3` is one
  rank-at-most-three component covering every mask through rank three, and

  ```text
  |P4|+|Q4|=n4<=100,
  |D3|>=231.                                      (5.26)
  ```

  The constant is independently recomputed from
  `sigma_4=330+1-231=100`.

  There is a further exact consequence.  The component `D3` has

  ```text
  |D3|=(330-n4)+1.
  ```

  Its selected nonliteral rank-four family therefore has slack one.  Every
  adjacent pair of `D3` is a selected distinct rank-four witness, and every
  mask of ranks one through three occurs literally as an entry of `D3`.
  Consequently

  ```text
  F=|D3|-231=100-n4,                               (5.27)
  y1<=n4<=100.                                     (5.28)
  ```

  The second row follows either by cell disjointness--the `330-n4` inner
  rank-four pairs and the `y1` outer rank-five pairs are disjoint among the
  330 physical pairs of `C`--or by substituting (5.27) into the sharpened
  no-carrier Hall row.

  In fact every one of the 561 outer lower targets now has a singleton/pair
  witness, so the carrier allowance can be set to zero even if the physical
  seam triple happens to have low rank.  If `H` lies wholly in `D3`, its two
  contained adjacent pairs have distinct rank-four OR values; their common
  containing triple must have rank at least five.  If a low `H` meets `P4`
  or `Q4`, its OR equals a literal rank-four value and is redundant.
  Therefore the correct top-slice rows use

  ```text
  y2>=228+F=328-n4,
  e_effective=0.                                   (5.29)
  ```

* If `n5=133`, then `e4=1`.  A repeated literal rank-four occurrence
  (`x4=1`) forces one rank-at-most-three component; with no repetition there
  are at most two.  In the latter case at least one is coordinate-complete.

  The complete three-way refinement is:

  1. `x4=1,s3=1`: the low component has slack one.  All its adjacent pairs
     are distinct rank-four witnesses and all rank-at-most-three targets are
     literal.  Writing `n4` for the physical rank-four count,

     ```text
     F=101-n4,
     y1<=n4.                                       (5.30)
     ```

     The extra rank-four occurrence is the one duplicate; it does not create
     another selected singleton value.

  2. `x4=0,s3=2`: both low components have slack one.  Every internal pair
     in either component is selected at rank four, every rank-at-most-three
     target is literal, and

     ```text
     F=101-n4,
     y1<=n4+1.                                     (5.31)
     ```

     At least one of the two low components is coordinate-complete.

  3. `x4=0,s3=1`: the unique low component has slack two.  Let `v4` be the
     number of its selected rank-four triple witnesses.  The outer
     one-defect theorem forces

     ```text
     v4<=1.                                        (5.32)
     ```

     No rank-at-most-three target can use the outer seam triple in this
     subcase.  Indeed, if `v4=0`, the component has `m-2` selected
     rank-four pair witnesses among its `m-1` physical pairs, leaving only
     one pair unselected at rank four.  A rank-at-most-three triple wholly
     inside the component contains two pairs, neither of which can be a
     selected rank-four pair, and so would require two such free pairs.  A
     triple meeting a deleted literal rank-four position has rank at least
     four.  Thus a low seam is impossible when `v4=0`; when `v4=1`, the
     seam is already the rank-four witness.  In either case all
     rank-at-most-three targets use singleton/pair cells.

     All other nonliteral rank-four targets use adjacent pairs, whence

     ```text
     n4<=102+v4,
     y1<=n4+1+v4.                                  (5.33)
     ```

     If `v4=1`, that one rank-four triple is the outer carrier `H`; if
     `v4=0`, all 561 outer lower targets have singleton/pair witnesses.  The
     slack-two component is coordinate-complete.

* If `n5=132`, there are at most three rank-at-most-three components, and
  again at least one is coordinate-complete.

The bounds in (5.30)--(5.33) are physical cell counts, not scalar schedule
guesses.  In a slack-one inner component every pair is already occupied by a
rank-four target.  In the slack-two mode, all but `v4` of the `330-n4`
nonliteral rank-four targets occupy pairs; subtracting those cells from the
331 physical pairs of the outer core gives (5.33).  The first inequality in
(5.33) is the lower-target capacity

```text
(332-n4)+1+v4 >=231.
```

### 5.8 Hand elimination of the `t=1,...,6` averages at `n5=134`

The all-codimension hierarchy was checked symbolically against the exact
top slice; it does not by itself yield a contradiction.  This audit is
useful because it identifies precisely where averaging loses the endpoint
geometry.

Write `F=100-n4`.  Since every rank-one, rank-two, and rank-three target is
literal in `D3`, the smallest possible binomial moment in (5.22), at fixed
`F`, is obtained by putting all `F` surplus entries at rank three:

```text
(n1,n2,n3,n4)=(11,55,165+F,100-F).                (5.34)
```

Any surplus moved to rank one or two only increases every moment for
`1<=t<=6`.  Also `y1<=n4=100-F`, and the carrier allowance is unnecessary.
Substitution into (5.22) gives the following exact residual margins:

| `t` | `2 M_t - [C(11,t)(L(t)+1)+C(6,t)y1]` is at least |
|---:|---:|
| 1 | `404+8F` |
| 2 | `2810+29F` |
| 3 | `8465+62F` |
| 4 | `14410+85F` |
| 5 | `15150+76F` |
| 6 | `10078+43F` |

For example, at `t=1` the two sides before the `y1` substitution are

```text
2*M1=5250+2F,
11*(385+1)+6*y1=4246+6*y1,
```

and `y1<=100-F` gives the first margin.  The other five rows follow by the
same binomial expansion, with no optimization oracle.

Thus every nonnegative averaging or convex combination of the six scalar
moments remains feasible in the exact top slice.  The nonredundant content
is the pointwise rounding, the shared carrier identity, and especially the
physical pair disjointness `y1<=n4` (or `y1<=n4-1` in chain B), all of which
are erased by summing over `B`.

### 5.9 Finite recursive classification for every `n5<=132`

For the remaining nonsaturated slices the rank-four filtration can be
parameterized without losing any word.  This gives a finite structural
classification even though it does not collapse to one onion.

Retain

```text
e4=134-n5,
x4=rank-four literal repetition excess,
z4=n4-x4,
s3=# rank-at-most-three components.
```

For component `j`, let `mj` be its length, `qj` the number of selected
nonliteral rank-four witnesses assigned to it, and

```text
tj=mj-qj.
```

Then every hypothetical word determines integers satisfying

```text
0<=x4<=e4,
1<=s3<=1+e4-x4,
tj>=1,
sum_j tj=1+e4-x4,
sum_j qj=330-z4.                                  (5.35)
```

Every selected rank-four witness has length two or three by the global
rank-six cap.  There is one shared low-triple token:

```text
v4 = # selected nonliteral rank-four triple witnesses,
w3 = # rank-three targets with no singleton/pair witness,
v4+w3<=1.                                         (5.36)
```

If `v4=1`, its cell is `H`, its value has rank four, and `w3=0`.  If
`w3=1`, `H` has rank exactly three and every nonliteral rank-four target
uses a pair.  The rank-two lemma of Section 5.1a rules out a genuinely
needed lower triple.  All remaining rank-at-most-three targets use singleton/pair cells
inside the `s3` components.

Let

```text
Delta3=(total rank-at-most-three positions)
       -(number of distinct literal values of ranks one through three).
```

Thus `Delta3` is the literal repetition excess inside the lower components
and dominates the rank-histogram surplus `F3`.  The distinct literal values,
internal pair cells, selected rank-four pairs, and optional lower carrier
give the exact global collision row

```text
Delta3+n4 <=369-2*n5-s3-x4+v4+w3.                (5.37)
```

Indeed the number of nonliteral rank-at-most-three targets which still need
pairs is

```text
231-[(N-n4)-Delta3]-w3.
```

Adding the `330-z4-v4` pair-witnessed rank-four targets and injecting both
families into the `N-n4-s3` physical pairs derives (5.37), with every
subtraction term visible.

The cross-rank collision map is injective: map each of the
`330-z4-v4` pair-witnessed rank-four targets and each of the `y1`
pair-witnessed rank-five targets to its physical pair cell.  The target
families have different ranks and the chosen cells within each family are
distinct, so their images are disjoint.  This is exactly the pair-packing
law

```text
y1<=134-n5+z4+v4.                                 (5.38)
```

There is also a pointwise recursive omission law.  For a coordinate set
`B`, let `ZB3,RB3` count `B`-free positions and runs over the rank-at-most-
three components, let `aB4` count selected rank-four pair values disjoint
from `B`, and let `dB3=1` precisely when `w3=1` and the lower carrier is
disjoint from `B`.  Put

```text
L3(t)=sum_(r=1)^3 C(11-t,r),  t=|B|.
```

Then

```text
2*ZB3-RB3-aB4 >=L3(t)-dB3.                       (5.39)
```

For `0<=t<=10`, summing over every `t`-set `B` gives

```text
2*sum_(rank<=3 positions i) C(11-|A_i|,t)
 >= C(11,t)*(L3(t)+1)
      +C(7,t)*(330-z4-v4)
      -w3*C(11-rho,t),                            (5.40)
```

where `rho=3` when the last term is present.  The restriction `t<=10` is
needed for the extra run term; the pointwise row (5.39) itself remains valid
also for `B=[11]`.  The factor `C(7,t)` is exact: each selected rank-four
pair value omits seven coordinates.  Equations
(5.35)--(5.40), together with the outer chain-A template, classify every
`n5<=132` word through rank four.  If `s3<4`, at least one listed component
is coordinate-complete; for larger `s3` the full transversal condition,
not an unjustified complete-component claim, must be retained.

Here and below, “classify” means a lossless necessary word-to-template map.
It does not assert that every integer tuple satisfying the displayed rows
lifts to a compatible bit assignment or OR word.

## 6. Equality skeleton

Put

```text
D=y2-(93+n5+Delta_lit)>=0.
```

When `D=0`, the collision injection in Section 5.1a forces all of the
following:

1. `v=1`, so `h3=h4` and `H` carries a nonliteral mask of rank three or four;
2. every distinct literal lower value and every pair not selected at rank
   five is needed;
3. their OR values, together with `OR(H)`, are exactly the 561 distinct lower
   masks.

Thus the zero-margin nonsaturated branch is an exact labelled path template:

* rank-five singleton labels occupy the two physical ends;
* rank-five pair labels occupy the first and last pair blocks;
* rank-five triple labels occupy the two triple blocks;
* the unique seam triple `H` supplies the one lower label not supplied by a
  singleton or pair.

The carrier rank is in fact only three or four.  It cannot be one because
every singleton target is literal.  It cannot be two because the two
middle pair colors whose union is `OR(H)` are distinct, have ranks at
least two, and are not `OR(H)`; two such subsets cannot fit inside a
two-set.  More explicitly, put `v2=0`; for `r=3,4` let `vr` indicate
that `H` supplies one nonliteral rank-`r` target.  Then
`v3+v4=1`, and for `r=2,3,4` put

```text
pr=C(11,r)-zr-vr.
```

The `p2,p3,p4,y1` chosen pair families are disjoint subsets of the same
physical edge set.  At `D=0` their sizes sum to `N-1`, so they partition
every adjacent pair of `C`; the OR values in the four color classes are
respectively all nonliteral rank-two, rank-three, rank-four, and selected
rank-five pair targets.  Together with the literal vertices and `H`, this is
a complete rank-colored path skeleton through rank five.

The triple cells are simultaneously exact.  Since `h3=h4`, the selected
rank-five pair cells form only the two boundary-touching runs.  They
contaminate exactly `y1` distinct triples; the `y2` selected rank-five
triple cells are disjoint from those, and

```text
y1+y2+1=q+1=N-2.
```

Thus every physical triple is exactly one of: a selected rank-five triple,
a triple containing a selected rank-five pair, or the unique lower carrier
`H`.  No unnamed short cell remains in the zero-margin template.

Equivalently, the physical pair cells have three consecutive zones:

```text
rank-five pair prefix || lower pair core || rank-five pair suffix.  (6.1a)
```

The middle zone has

```text
p=96+n5+Delta_lit-1
```

edges, whose distinct OR values are exactly the nonliteral lower targets not
assigned to `H`.  Its `p-1` consecutive edge pairs correspond to physical
triples: one is the lower seam `H`, while the other

```text
p-2=93+n5+Delta_lit=y2
```

have distinct rank-five unions.  Thus zero margin is precisely a rainbow
path on the nonliteral lower masks, with one low seam and all other edge
unions in the rank-five layer.  If `B_i` denotes the lower OR color of the
`i`th middle pair, its internal physical vertex satisfies

```text
empty != A_(i+1) subseteq B_i intersect B_(i+1),
B_i union B_(i+1) has rank five except at the seam.        (6.1b)
```

The rank-six layer on this middle segment is automatically saturated.
Choose one interval for each rank-six target.  These 462 intervals are
pairwise incomparable, so after ordering their distinct left endpoints,
their distinct right endpoints occur in the same order.  With only three
unused positions on either endpoint side, the `j`th interval has left
endpoint at least `j` and right endpoint at most `j+3`; hence every selected
rank-six interval has length at most four.
Let `L=p+1` be its number of physical vertices.  At most `465-L` of
the 462 selected rank-six intervals fail to lie wholly in the segment, by
charging them to distinct left endpoints before it or distinct right
endpoints after it.  Thus at least `L-3` lie inside.  Every cell there of
length at most three has rank at most five by (6.1b), so the contained
rank-six witnesses must be four-windows.  There are exactly `L-3` of
those.  Hence

> every one of the `L-3=p-2=y2` middle four-windows is a selected witness
> for a distinct rank-six target.                         (6.1b6)

This also gives a general zero-run fingerprint.  Let `U_l` be the sum of
the ranks of the length-`l` middle windows, and let `R^(l)` be the total
number, over all coordinates, of zero runs of length at least `l` in the
binary traces restricted to this middle segment.  Runs truncated at a
segment endpoint are counted, and an all-zero trace is one full-length run.
Put
`Rpair=U2`.  Since the `L-2` triples consist of `L-3` rank-five
targets and the rank-`rho` seam,

```text
U2=Rpair,
U3=5*(L-3)+rho,
U4=6*(L-3).
```

The coordinate identity `U_(l+1)-U_l=R^(l)-11` now yields

```text
R^(2)=5*L-4+rho-Rpair,
R^(3)=L+8-rho,
# zero runs of length exactly two
   =4*L-12+2*rho-Rpair.                            (6.1b7)
```

Every five-window contains two distinct rank-six four-window ORs, so it has
rank at least seven.  Therefore `R^(4)>=L+1`: at most `7-rho` zero runs
have length exactly three (at most four for a rank-three seam and three for
a rank-four seam).

This immediately gives two further exact, solver-free constraints.  Let
`pr` be the number of middle-edge colors of rank `r`, as above.  Away
from the seam, two consecutive ranks `r,s` satisfy

```text
r+s>=6,                                            (6.1c)
```

because their union has rank five and their intersection contains the
nonempty shared word entry.  Hence a rank-two color can be adjacent only to
a rank-four color after the seam transition is deleted.  The deletion
leaves at most two paths, and on each path the rank-two vertices are
separated by rank-four vertices.  Therefore

```text
p2<=p4+2.                                         (6.1d)
```

The seam type is also exact.  If `rho=3`, its two colors both have rank
two.  If `rho=4`, their ranks are `(2,3)`, `(3,2)`, or `(3,3)`.
Consequently (6.1d) sharpens to `p2<=p4+1` in the first two rank-four
seam types and to `p2<=p4` in the `(3,3)` type.

There is also an incidence ceiling which retains the rank of every literal
value.  Put

```text
Rpair=2*p2+3*p3+4*p4,
Llit =z1+2*z2+3*z3+4*z4.
```

If `V_0,...,V_p` are the `p+1` physical vertices under the middle edge
colors, then

```text
V_i subseteq B_i intersect B_(i+1)   (1<=i<p).
```

At each ordinary transition that intersection has size
`|B_i|+|B_(i+1)|-5`; at the seam it has size
`|B_i|+|B_(i+1)|-rho`.  The two end vertices have ranks at most
`|B_1|` and `|B_p|`.  Summing these pointwise bounds yields

```text
sum_(i=0)^p |V_i| <=2*Rpair-5*p+10-rho.            (6.1e)
```

Exactly `y1` core vertices lie outside this middle vertex segment, and
each has rank at most four.  Moreover
`Rpair=1936-Llit-rho`.  Thus every zero-margin word obeys

```text
S <=4*y1+2*Rpair-5*p+10-rho
  =3882+4*y1-5*p-2*Llit-3*rho.                    (6.1f)
```

Combining this ceiling with the weighted lower row (5.7) eliminates `S`
and gives the purely discrete seam inequality

```text
15*p+6*Llit+E+8*rho <=9708+7*y1,
```

or, after using the zero-margin identities for `p` and `y1`,

```text
29*n5+22*Delta_lit+6*Llit+E+8*rho <=10866.        (6.1g)
```

Unlike a scalar Hall row, (6.1d)--(6.1g) see the order of the rank-colored
pair path and the unique seam.  They do not by themselves contradict the
remaining parameter ranges, but they are necessary consequences of exact
zero margin.

Zero margin also aligns the whole rank-four filtration with the three pair
zones.  No vertex of the middle lower-pair segment can have rank four.  If
such a vertex had literal value `R`, either incident middle edge would
have lower OR `B` with `R subseteq B`; since both have rank at most four,
this would force `B=R`, contradicting that every middle edge color is a
nonliteral target.  Thus the `p+1` middle vertices lie in one physical
rank-at-most-three component.  Every nonliteral rank-four or lower pair
target occurs on this central segment, while every pair outside the segment
is selected at rank five.

In the recursive notation of Section 5.9, zero margin therefore gives the
exact identities

```text
Delta_lit=x4+Delta3,
v4+w3=1,
g:=y1-(n4+s3-1)
  =370-2*n5-s3-x4-Delta3-n4 >=0.                  (6.1h)
```

Here `n4+s3-1` is exactly the number of physical pairs not internal to a
rank-at-most-three component, and `g` counts the selected rank-five pairs
which nevertheless lie inside those components.  Equivalently, (5.37)
becomes an equality with explicit slack

```text
Delta3+n4+g
 =369-2*n5-s3-x4+v4+w3.                           (6.1i)
```

This identifies what the recursive collision slack means geometrically:
it is not an anonymous capacity surplus, but the number of rank-five pair
cells embedded in the next lower components.

Let `tstar` be the rank-four slack of the component containing the middle
segment.  The two pairs under `H` are not selected at rank four.  If
`rho=4`, one of the component's rank-four witnesses is the triple `H`,
so exactly `tstar` component pairs are not selected at rank four.  If
`rho=3`, every rank-four witness is a pair, so that number is
`tstar-1`.  The two seam pairs therefore force

```text
rho=4  implies tstar>=2,
rho=3  implies tstar>=3.                          (6.1j)
```

Since the total rank-four component slack is `135-n5-x4`, (6.1j) is a
small but sharp recursive carrier budget.  It reproves immediately that
zero margin is impossible at `n5=134`, and that `n5=133` forces
`x4=0,rho=4,tstar=2,s3=1`.

The rest of the recursive geometry is also exact.  Put

```text
T=135-n5-x4=sum_j tj.
```

Every nonliteral rank-four witness lies in the central component: its pair
witness is on the middle segment, or it is the seam `H` itself.  Hence all
other rank-at-most-three components have `qj=0`; their total length is
`T-tstar`, and all of their internal pairs are selected at rank five.
They contribute

```text
g_sat=T-tstar-(s3-1)
```

of the embedded rank-five pairs.  Put `g_c=g-g_sat` for the number in the
two central tails outside the middle segment.  If `k` is the number of
nonliteral masks of ranks at most three, then in either carrier rank

```text
k=tstar-g_c=T-s3+1-g,
z1+z2+z3=231-k.                                   (6.1k)
```

For `rho=4`, the `k` targets are exactly the central pairs not selected
at ranks four or five.  For `rho=3`, there are `k-1` such pair colors
plus `H` itself.  Thus `k>=2` in the former case and `k>=3` in the
latter.  The normal form also retains the feasibility conditions

```text
T-tstar>=s3-1,
g_sat>=0,
g>=g_sat,
g_c>=0.
```

The central component is obtained from the `(p+1)`-vertex middle
segment by attaching exactly `g_c` low vertices at its two ends through
rank-five pair edges; the remaining `s3-1` components are rank-five-pair
paths of total length `T-tstar`.  Equations (6.1h)--(6.1k), together with
the rainbow four-window saturation (6.1b6), are a finite exact normal form
for every zero-margin slice, not only the top three enumerated below.

This is the remaining construction gate in the zero-margin subbranch; it is
an exact target, not a heuristic middle-level row.

This is a viable exact combinatorial skeleton, not an asserted bit assignment.
For example, the endpoint schedule itself is nonempty: with `n5=0`, take
`h1=h2=0`, `h3=h4=231`, and `h5=h6=462`.  It selects 231 rank-five triples
on either side of the unique seam `H`.  Global OR compatibility, coordinate
pins, and upper-rank coverage remain to be solved.

The nested rank-four audit sharply localizes this equality skeleton near the
top of the `n5` range.

* At `n5=134`, `D=0` is impossible: Section 5.7 supplies every lower target
  by a singleton/pair and raises the exact Hall constant by one.
* At `n5=133`, `D=0` forces the inner mode

  ```text
  x4=0, s3=1, v4=1, rho=4.                        (6.1)
  ```

  The other two inner modes have no genuine carrier.  In (6.1),

  ```text
  Delta_lit=103-n4,
  y1=n4,
  y2=329-n4,
  n4<=103.                                        (6.2)
  ```

  Here is the exact reason the inequalities collapse.  Write

  ```text
  C=P4 || D3 || Q4,
  |P4|+|Q4|=n4,
  |D3|=332-n4.
  ```

  The entries in `P4,Q4` are distinct literal rank-four masks, and `D3`
  is the unique coordinate-complete rank-at-most-three component.  Of its
  `331-n4` physical pairs, `329-n4` are the selected nonliteral
  rank-four witnesses.  The two pairs contained in `H` cannot be among
  them: their ORs are proper subsets of the rank-four mask `OR(H)`.
  Hence those are exactly the two remaining pairs of `D3`.  At outer zero
  margin both carry distinct nonliteral rank-at-most-three targets.
  Conversely, a pair outside `D3` contains a literal rank-four entry and
  therefore cannot have a nonliteral OR of rank at most four.
  Consequently there are exactly two, not merely at most two, nonliteral
  targets below rank four.  This proves
  `Delta_lit+n4-101=2`, which is (6.2).

  The entire double filtration is therefore fixed at the cell-family level:

  * every pair outside `D3` is one of the `n4=y1` selected rank-five
    pair witnesses;
  * every pair inside `D3` except the two consecutive pairs under `H`
    is one of the `329-n4` selected rank-four pair witnesses;
  * the two seam-pair ORs are precisely the two missing literal masks below
    rank four;
  * every triple internal to `D3` except `H` is one of the
    `329-n4=y2` selected rank-five triple witnesses;
  * `H` is the final nonliteral rank-four target.

  If the seam ranks are `(2,3)` or `(3,2)`, then
  `(z1,z2,z3)=(11,54,164)`; if they are `(3,3)`, then
  `(z1,z2,z3)=(11,55,163)`.  Thus exactly 229 masks below rank four occur
  literally in `D3`, with `103-n4` repeated positions.  This is a
  lossless exact template, although it is still not a bit assignment or a
  contradiction.

  The rank-six layer is then forced as well.  Put `m=|D3|=332-n4`.
  The 462 selected rank-six intervals are pairwise incomparable.  Ordered
  by left endpoint, their right endpoints have the same strict order; with
  only three unused endpoint positions this gives length at most four.  At
  most `465-m` of them fail to lie inside `D3`: charge such an interval
  either to its left endpoint before `D3` or to its right endpoint after
  `D3`.  Therefore at least

  ```text
  462-(465-m)=m-3
  ```

  selected rank-six intervals lie inside `D3`.  Every subinterval of
  `D3` of length at most three has rank at most five by the preceding
  template.  The contained rank-six intervals must consequently be
  four-windows.  There are only `m-3` such windows, so equality holds:

  > every four-window of `D3` is a selected witness for a distinct
  > rank-six target.                                      (6.3)

  This has a compact run-length fingerprint.  Let `U_l` be the sum of the
  OR-ranks of all length-`l` windows of `D3`, and let `R^(l)` be the
  total, over the eleven coordinates, of zero runs having length at least
  `l`.  Coordinatewise window counting gives

  ```text
  U_(l+1)-U_l=R^(l)-11.                            (6.4)
  ```

  If `s0` is the sum of the two seam-pair ranks, then `s0=5` in the
  `(2,3)` case and `s0=6` in the `(3,3)` case.  The exact template and
  (6.3) give

  ```text
  U2=4*(m-3)+s0,
  U3=5*(m-3)+4=5*m-11,
  U4=6*(m-3).
  ```

  Hence

  ```text
  R^(2)=m+12-s0,
  R^(3)=m+4,
  # zero runs of length exactly two =8-s0.          (6.5)
  ```

  In particular there are exactly three length-two zero runs across all
  coordinates in the `(2,3)` seam case and exactly two in the `(3,3)`
  case.  Every five-window contains two distinct six-set four-window ORs,
  so it has rank at least seven.  Applying (6.4) once more gives
  `R^(4)>=m+1`; consequently at most three zero runs have length exactly
  three.  These identities are another lossless test of the surviving
  double-filtration template.

  Finally, the three entries under `H` themselves have only a few forms.
  In the `(2,3)` seam case, write

  ```text
  OR(H)={x,y,c,d},
  B2={x,y},
  B3={y,c,d}.
  ```

  Since `B2,B3` are precisely the two nonliteral lower masks, the actual
  three-entry segment is forced to be

  ```text
  {x}, {y}, {c,d}
  ```

  or its reversal.  In the `(3,3)` case, write the seam colors as
  `I union {a}` and `I union {b}`, where `|I|=2`.  Their shared middle
  entry is a nonempty subset `Y subseteq I`.  If `|Y|=1`, the two outer
  entries are forced to be `(I minus Y) union {a}` and
  `(I minus Y) union {b}`.  If `Y=I`, each outer entry is `{a}` or
  `{a,i}` for one `i in I`, and analogously on the `b` side.  This
  exhausts the local seam because an entry equal to either three-set would
  make that missing target literal.                              (6.6)

* At `n5=132`, the carrier budget (6.1j) leaves exactly the following five
  modes.  Here `g` has the meaning in (6.1h).

  | mode | `(x4,s3,rho,tstar,g)` | `Delta_lit` | `y1` | `y2` |
  |---|---:|---:|---:|---:|
  | A | `(1,1,4,2,0)` | `105-n4` | `n4` | `330-n4` |
  | B | `(0,2,4,2,0)` | `104-n4` | `n4+1` | `329-n4` |
  | C0 | `(0,1,4,3,0)` | `105-n4` | `n4` | `330-n4` |
  | C1 | `(0,1,4,3,1)` | `104-n4` | `n4+1` | `329-n4` |
  | D | `(0,1,3,3,0)` | `105-n4` | `n4` | `330-n4` |

  The coarse ledger also gives the necessary ranges

  ```text
  A:  2<=n4<=104,
  B:  1<=n4<=104,
  C1: 0<=n4<=104,
  C0,D: 0<=n4<=105.
  ```

  The upper bounds are `Delta3>=0`; the lower bounds in A and B come,
  respectively, from one repeated literal rank-four occurrence and from
  the literal rank-four separator between two lower components.

  To verify completeness, the total inner slack is `3-x4`.  A rank-four
  carrier needs central slack at least two, while a rank-three carrier
  needs at least three.  Thus `x4=2` is impossible.  If `x4=1`, only
  mode A remains.  If `x4=0,rho=3`, only mode D remains.  If
  `x4=0,rho=4`, the slack-three budget is either all central, giving C0
  or C1, or splits as `2+1`, giving B.  In the latter case the second
  component has no nonliteral rank-four witness and is a single literal
  lower entry.  In the central-slack-three case, the two seam pairs leave
  only one further pair not selected at rank four; it is a lower pair in
  C0 and the unique embedded rank-five pair in C1.  This proves
  `g in {0,1}` and all table entries.

  These five rows are again exact cell templates.  Let `M3` be the middle
  lower-pair vertex segment.  In A, C0, and D it is the entire
  rank-at-most-three component and has length `333-n4`.  In B it is the
  central component of length `332-n4`, with one isolated literal lower
  component outside.  In C1 its length is `332-n4`, with one further low
  vertex attached at an end by the unique embedded rank-five pair.
  Every triple internal to `M3` except `H` is a distinct selected
  rank-five witness, and endpoint saturation makes every four-window of
  `M3` a distinct selected rank-six witness.

  Modes A, B, and C1 have exactly two nonliteral masks below rank four,
  namely the seam pair colors.  Mode C0 has those two plus its one
  additional lower pair color.  Mode D has two missing rank-two masks and
  the rank-three carrier, so
  `(z1,z2,z3)=(11,53,164)`; its seam entries are three distinct
  singletons.  The rank-four carrier modes have the local seam forms in
  (6.6).

Thus the first three `n5` slices are completely classified at zero Hall
margin.  They still leave coherent nested templates rather than a
contradiction.

## 7. Broader chain/component coupling

The same endpoint audit gives an exact lossless reduction for the
duplicate-free Type-II modes.

* If `(delta_5,s)=(0,1)`, internal diagonal states `11,22` are empty and the
  schedule is chain A.
* If `(delta_5,s)=(0,2)`, exactly one internal diagonal block is nonempty.
  Reversal exchanges `11` and `22`, so one may orient the schedule as chain B
  with a positive `22` block.  The low component to its left has slack two
  and the component to its right has slack one.  All selected nonliteral
  witnesses in the right component are its adjacent pairs.

To see the second statement directly, a chain-B `22` block on slots
`[h4,h5)` occupies literal positions `[h4+2,h5+1]`.  The left low component
has length `h4-h1+2` and contains `h4-h1` selected nonliteral witnesses; the
right has length `h6-h5+1` and contains `h6-h5` witnesses.  Their slacks are
therefore two and one.  Chain C is the reversed orientation.

More explicitly, the oriented chain-B word has the exact physical form

```text
P5 || C2 || R5 || C1 || Q5,                       (7.1)
```

where `P5,R5,Q5` are distinct literal rank-five blocks, `C2` is the
slack-two component, and `C1` is the slack-one component.  The selected
rank-five schedule is

```text
00: literal singletons in P5,
01: adjacent pairs in C2,
02: triples in C2,
12: adjacent pairs in C2,
22: literal singletons in R5 (a nonempty block),
23: every adjacent pair in C1,
33: literal singletons in Q5.                      (7.2)
```

Thus every lower target represented in `C1` is a literal entry, while every
lower target represented in `C2` has a singleton/pair witness.  This proves
the component/slack alignment directly from physical endpoints; it is not a
scalar consequence of `delta_5+s=2`.

The coordinate endpoint-pair ledger also has an exact two-component form.
Let `N=465-n5`, let `S` be the total entry-rank sum over `C1 union C2`, and
retain

```text
ab=# selected rank-five pair values omitting b,
cb=y1-ab.
```

Let `Zb,ob` count omission/occurrence positions across both components and
let `Rb` count zero runs separately inside them.  The two components have
`2*N-2` singleton/pair cells, so every one of the 385 omitting and 176
containing lower targets gives

```text
2*Zb-Rb-ab       >=385,
2*ob+Rb-2-cb     >=176.                            (7.3)
```

Again `sum ab=6*y1` and `sum cb=5*y1`.  Since `Rb>=1` and
`Rb<=ob+2`,

```text
Zb >=193+ceil(ab/2),
ob >=ceil((176+cb)/3).                             (7.4)
```

Summing the exact integer costs yields

```text
649+max(0,ceil((5*y1-11)/3))
  <= S
  <= 11*N-2123-3*y1.                              (7.5)
```

Inside the slack-one component `C1`, if its length and entry-rank sum are
`m,S1` and `R1` is the sum, over all coordinates, of their zero-run counts,
then all `m-1` adjacent pairs have OR-rank exactly five.  The identity

```text
sum_(pairs in C1) |OR(pair)| = S1+R1-11
```

therefore specializes to

```text
S1+R1=5*m+6.                                      (7.6)
```

Equation (7.6) is an exact coordinate-run fingerprint of the rigid
slack-one path.  It can be combined with the already proved fact that one of
`C1,C2` is coordinate-complete; no claim is made here as to which component
must be complete.

If `C1` is the coordinate-complete component, then necessarily `m>=4`.
Indeed `m<=1` has total OR-rank at most four, `m=2` has total OR equal to one
five-set, and for `m=3` the two adjacent five-sets share the nonempty middle
entry, so their union has size at most nine.

There is also an exact lower-ideal margin.  Put

```text
D2=y2-(95+n5+Delta_lit).
```

Here `Delta_lit` is the repetition excess among literal values of ranks one
through four across both low components.  Every nonliteral lower target uses
a physical pair, and there is no carrier.  The same collision injection now
has only `N-2` physical pair cells, so

```text
y1+2*n5+Delta_lit <=367,
y2>=95+n5+Delta_lit.                              (7.6a)
```

Thus `D2>=0`; if `D2=0`, every distinct literal lower value and every pair
cell not selected at rank five is used exactly once, and their OR values are
the complete 561-mask lower ideal.  This is the two-component analogue of
the equality skeleton in Section 6, with no triple carrier.  Since
`Delta_lit>=F`, it also strengthens the earlier histogram row
`y2>=95+n5+F`.

The equality skeleton can again be made exact.  The non-rank-five pairs form
one contiguous segment inside the slack-two component `C2`.  It has

```text
p=96+n5+Delta_lit
```

edges, whose colors are all nonliteral lower masks, and `L=p+1` vertices.
Every one of its `p-1=y2` edge transitions is a distinct selected
rank-five triple.  In particular consecutive color ranks sum to at least
six, and rank-two colors are separated by rank-four colors:

```text
p2<=p4+1.                                         (7.6b)
```

Endpoint saturation gives at least `L-3` selected rank-six intervals
inside this segment.  All shorter cells have rank at most five, so every
one of its `L-3=y2-1` four-windows is a distinct selected rank-six
witness.                                          (7.6c)

With `Rpair`, `U_l`, and `R^(l)` as in Section 6, the carrier-free
window sums are

```text
U2=Rpair,
U3=5*(L-2),
U4=6*(L-3),
R^(2)=5*L+1-Rpair,
R^(3)=L+3,
# zero runs of length exactly two =4*L-2-Rpair.    (7.6d)
```

Every five-window has rank at least seven, so `R^(4)>=L+1` and at most
two zero runs have length exactly three.

There is a carrier-free recursive normal form as well.  Retain the
rank-four variables of Section 7.2 and put

```text
T=135-n5-x4,
Delta_lit=x4+Delta3,
g=y1-(n4+s3-2)
 =369-2*n5-s3-x4-Delta3-n4 >=0.                  (7.6e)
```

The central rank-at-most-three component contains every nonliteral
rank-four pair witness and the lower-pair segment.  If its slack is
`tstar`, all other components have no nonliteral rank-four witness, have
total length `T-tstar`, and contribute
`g_sat=T-tstar-(s3-1)` embedded rank-five pairs.  With
`g_c=g-g_sat`, the number `k` of nonliteral masks below rank four is

```text
k=tstar-1-g_c=T-s3-g,
z1+z2+z3=231-k.                                   (7.6f)
```

As a formal normal form these identities retain

```text
T-tstar>=s3-1,
g_sat>=0,
g>=g_sat,
g_c>=0.
```

The central component is the `L`-vertex lower-pair segment plus exactly
`g_c` low tail vertices joined by rank-five pairs; every satellite is a
rank-five-pair path.  Equations (7.6b)--(7.6f) are the exact two-component
counterpart of (6.1h)--(6.1k).

### 7.1 Exact top slice `n5=134`

The chain-B branch also has a nested exact classification at maximum literal
rank-five mass.  Suppose `n5=134`, so the two low components have total
length 331.  Delete the intervening literal rank-five block and concatenate

```text
Cstar=C2 || C1.
```

Every old lower witness remains internal to one of the two pieces, so
`Cstar` is a genuine 331-entry word covering every mask through rank four.
Exact rank-four boundary--core rigidity gives

```text
Cstar=P4 || D3 || Q4,
n4=|P4|+|Q4|<=100,
|D3|=331-n4>=231.                                 (7.7)
```

All entries of `D3` have rank at most three, every mask through rank three
occurs literally there, and every adjacent pair of `D3` is a distinct
rank-four witness.

The artificial concatenation seam cannot lie inside `D3`.  To audit this
carefully, choose all rank-four witnesses in the original word before
concatenating.  They remain internal to `C2` or `C1`.  The nonliteral
rank-four family has size `|D3|-1`, and in a segment of that length plus one,
with no literal rank-four entry, its incomparable witnesses must be all
adjacent pairs.  If the seam lay inside `D3`, one of those required adjacent
pairs would be the artificial cross-component pair, contradicting the
original witness choice.

Moreover `D3` cannot lie in the slack-one component `C1`: every physical
adjacent pair of `C1` is a selected rank-five witness, whereas every
adjacent pair of `D3` has rank four.  Since `|D3|>=231`, it follows that

```text
D3 subseteq C2.                                   (7.8)
```

Consequently:

* the slack-two component `C2` is coordinate-complete, because `D3` already
  contains every singleton coordinate;
* every entry of the slack-one component `C1` is one of the distinct literal
  rank-four boundary entries;
* if `ell=|C1|`, then

  ```text
  1<=ell<=n4<=100;
  ```

* the `330-n4` rank-four pair witnesses and the `y1` rank-five pair
  witnesses are disjoint among the `329` physical pairs of the two low
  components, so

  ```text
  ell-1<=y1<=n4-1<=99;                            (7.9)
  ```

* the exact histogram and width identities are

  ```text
  F=100-n4,
  y2>=329-n4,
  y1+y2=328.                                      (7.10)
  ```

Thus the forced coordinate-complete component is specifically the
slack-two side in the top chain-B slice.  This is compatible with, but much
more precise than, the earlier statement that at least one of the two
components is coordinate-complete.

There is also a forced third layer inside this `D3`.  Put
`m=|D3|=331-n4`.  Every one of its `m-1` pairs is a distinct selected
rank-four witness.  No such pair is selected at rank five, and chain B has
no low triple, so every one of its `m-2` triples is a distinct selected
rank-five witness.  The rank-six endpoint count used in Section 6 now shows
that at least

```text
462-(465-m)=m-3
```

selected rank-six intervals lie in `D3`.  All shorter cells there have
rank at most five, and there are exactly `m-3` four-windows.  Therefore
every four-window is a distinct selected rank-six witness.

With the window and zero-run notation of (6.4), this gives

```text
U2=4*(m-1),  U3=5*(m-2),  U4=6*(m-3),
R^(2)=m+5,   R^(3)=m+3.                            (7.10a)
```

Thus exactly two coordinate zero runs have length exactly two.  Every
five-window has rank at least seven, so `R^(4)>=m+1`, and at most two zero
runs have length exactly three.  These are exact necessary rows for the
top chain-B component, independent of whether (7.10) has positive Hall
margin.

### 7.2 Finite rank-four classification for every chain-B slice

The same cell accounting classifies all `n5<=133` two-component words
through rank four.  Let `x4,z4=n4-x4` have the same meanings as in Section
5.9, and let `s3` count the physical rank-at-most-three components after all
literal rank-four positions are removed from both `C2` and `C1`.

The total low length is again `N=465-n5`, so

```text
0<=x4<=134-n5,
1<=s3<=135-n5-x4.                                 (7.11)
```

Unlike the outer nonsaturated core, the corrected two-component rank-five
mode has no low physical triple: every internal triple is selected at rank
five or contains a selected rank-five pair.  Hence every nonliteral
rank-four target uses a physical adjacent pair, and every rank-at-most-three
target uses a singleton/pair.  There is no carrier token at this level.

Let `Delta3` be the repetition excess of literal values of ranks one through
three in the `s3` physical components.  The same collision injection gives

```text
Delta3+n4 <=369-2*n5-s3-x4.                       (7.12)
```

The cross-rank collision map is one cell tighter than (5.38), because the
two rank-five low components have only `N-2` physical pairs:

```text
y1+(330-z4) <=N-2,
y1<=133-n5+z4.                                    (7.13)
```

For every coordinate set `B`, if `ZB3,RB3` count free positions and runs
across the physical rank-at-most-three components and `aB4` counts selected
rank-four pair values disjoint from `B`, then

```text
2*ZB3-RB3-aB4 >=L3(|B|).                          (7.14)
```

This is the carrier-free version of (5.39), with the same summed
`C(7,t)` moment for `0<=t<=10`; the pointwise row remains valid for every
`B`.  If `s3<4`, the transversal theorem forces one physical
rank-at-most-three component to be coordinate-complete.

At `n5=134`, equations (7.11)--(7.14) force `x4=0,s3=1`, give
`Delta3+n4<=100` and `y1<=n4-1`, and the seam argument of Section 7.1 locates
that unique component inside `C2`.  The equality
`Delta3+n4=100` uses the boundary--core rigidity of Section 7.1 (which says
that every rank-at-most-three target is literal in `D3`); it does not follow
from (7.11)--(7.14) alone.  For smaller `n5`, (7.11)--(7.14) are a
finite exact parameterization; no inference from a failed search is used.
This is again a necessary word-to-data parameterization, not a sufficiency
claim for the scalar tuples.

This reduction is deliberately not asserted for `(delta_5,s)=(1,1)`: the
one unselected duplicate occurrence can bridge one of the obligatory gaps
beside an internal diagonal block.  All three repaired schedule chains must
be retained there unless a separate argument removes that possibility.

## 8. Scope and audit findings

The proof is entirely combinatorial.  It uses no failed run, candidate
profile, solver output, fixed rank-six row, or computational enumeration.

Potential loopholes were checked explicitly:

* a nonliteral rank-five witness cannot cross a literal rank-five position;
* selected pair and selected triple cells cannot overlap by containment;
* the incident-triple count is on distinct physical cells, including two
  selected pairs sharing one triple only once;
* the selected pair set leaves at least two pair cells unselected, which is
  exactly what makes the incident count `>=y1` valid;
* one physical triple cannot carry two target masks;
* a rank-two triple target always has an adjacent-pair witness, so it cannot
  spend the effective carrier;
* empty endpoint-state blocks do not create a second carrier cell;
* the four-window saturation count uses arbitrary independently selected
  rank-six witnesses and only their distinct endpoints;
* the duplicate branch is excluded from the chain-A normalization for the
  stated bridging reason.

The theorem does not prove `nu(11)>465` and does not construct a universal
word.  It strictly sharpens the principal Type-II equality template.  A
future exact formula can exploit it by:

1. fixing chain A under the `(delta_5,s)=(0,1)` guard;
2. imposing `(H0-01+)`, `(H1-01)`, and the pointwise hierarchy (5.21);
3. replacing the 463 independent low-triple allowances by one transition
   carrier `H` of rank three or four;
4. using the zero-margin middle path, including its `y2` selected
   rank-six four-windows, the run
   identities (6.1b7), and the recursive normal form (6.1h)--(6.1k);
5. reusing the tight occurrence thresholds `ob>=59`, `Zb>=193` in this
   branch;
6. orienting the duplicate-free two-component branch as chain B with the
   slack-two component first.
