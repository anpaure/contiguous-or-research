# Final internal audit of `K11_NONSATURATED_ONE_DEFECT_CORE_20260724.md`

## 1. Verdict

The late-added parts of the note pass the requested proof audit, conditional
on the earlier named-cell shortening, rank-four surplus-component,
boundary--core rigidity, and coordinate-transversal theorems that the note
invokes.

In particular, I found no algebraic, endpoint, seam, witness-distinctness, or
case-completeness failure in the following claims:

* zero Hall margin is impossible at `n5=134` in chain A;
* at `n5=133`, zero margin forces the stated double filtration
  `P4 || D3 || Q4`, with exactly two low seam pairs and the stated local seam
  forms;
* at `n5=132`, the five modes A, B, C0, C1, and D are exhaustive at the
  cell-template level;
* the chain-B collision row, equality segment, recursive normal form, and
  top-slice localization of `D3` are correct;
* the interval-antichain endpoint charge forces every four-window in each
  claimed central segment to be a distinct selected rank-six witness;
* all displayed window-sum and zero-run identities have the correct
  constants;
* the recursive formulas (6.1h)--(6.1k) and (7.6e)--(7.6f) are exact
  word-to-template identities.

The word “classification” must retain the scope already acknowledged in the
note: these are lossless necessary cell-family normal forms.  They do not
classify compatible bit assignments, and the integer rows are not sufficient
conditions for an OR word.

There are several repairs to make before treating the note as polished:

1. The summed recursive moment (5.40) is valid only for `0<=t<=10`; it is
   false at `t=11`.  The same restriction applies to the summed moment
   mentioned after (7.14).  The pointwise rows (5.39) and (7.14) remain valid
   for every `B`.
2. Section 2's assertion that only four listed facts are used is too narrow.
   The main application also uses named-cell shortening, and the late nested
   sections use the rank-four surplus, exact rigidity, and transversal
   results.
3. The sentence after (7.14) saying that equations (7.11)--(7.14) themselves
   “recover `Delta3+n4=100`” is too strong.  Those displayed inequalities
   directly give only `Delta3+n4<=100`.  Equality follows from the additional
   slack-one structural fact that every pair of the unique low component is
   a rank-four witness, so every rank-at-most-three target must occur
   literally.
4. “Finite exact parameterization/classification” should consistently mean
   that every word maps to the listed data, not that every feasible integer
   tuple lifts to a word.
5. Minor source repairs are needed at the malformed strings
   `R^(4)>=L+1):`, `p+1)-vertex`, `C2)`, and `L)-vertex`.  The quantity `x3`
   in (6.1b6)/(7.6c) should also be defined or replaced by a plain statement
   about the number of selected rank-six four-windows.  Section 7.2 is titled
   for `n5<=133` but then explicitly applies its formulas at `n5=134`; the
   title/scope should be aligned.

None of these repairs invalidates a requested late-stage conclusion.

This audit is proof-only.  It uses no web source, solver, programmatic
enumeration, random experiment, or brute-force search.

## 2. Rank-six interval saturation

This is the common hinge for all of the new four-window claims, so it is
worth recording the argument in a form that exposes every endpoint
assumption.

Choose one interval for each of the 462 rank-six targets and order them by
left endpoint.  Distinct equal-rank targets give pairwise incomparable
intervals: containment of intervals would imply containment of their
six-set OR values and hence equality.  Therefore the left endpoints are
distinct, the right endpoints are distinct, and the two endpoint orders
agree.

Indexing the intervals by `j=0,...,461` in a 465-position word gives

```text
j <= ell_j <= r_j <= j+3.
```

Thus every selected rank-six interval has physical length at most four.
The phrase “distinct endpoints, and hence length at most four” in the source
is valid only with this preceding incomparability/common-order argument
included.

Now let a contiguous central segment have positions

```text
[a,a+L-1].
```

Partition the selected rank-six intervals not contained in this segment as
follows:

* if its left endpoint is before `a`, charge it to that left endpoint;
* otherwise its right endpoint is after `a+L-1`, so charge it to that right
  endpoint.

The first class has at most `a` members, and the second at most
`465-a-L`, because the relevant endpoints are distinct.  The classes are
disjoint by construction.  Hence at most

```text
a+(465-a-L)=465-L
```

selected rank-six intervals lie outside, and at least

```text
462-(465-L)=L-3
```

lie inside.

In each segment to which the note applies this argument, every subinterval
of length at most three has OR-rank at most five.  Therefore every contained
rank-six witness has length exactly four.  There are only `L-3` physical
four-windows, so equality holds: all four-windows are selected.  Since the
selected intervals represent different rank-six targets, their OR values
are pairwise distinct.

This validates the saturation assertions for:

* the general chain-A zero-margin middle segment in (6.1b6);
* `D3` at `n5=133` in (6.3);
* every `M3` in the five `n5=132` modes;
* the chain-B zero-margin lower-pair segment in (7.6c); and
* the chain-B top-slice `D3` in Section 7.1.

There is no dependence here on a fixed or preselected rank-six row.  Only
equal-rank interval incomparability and endpoint distinctness are used.

## 3. General zero-margin recursion in chain A

At chain-A zero margin, the collision injection saturates all `N-1`
physical pairs.  Consequently every pair is exactly one of:

```text
a selected rank-five pair,
or a pair whose OR is a distinct nonliteral lower target.
```

The non-rank-five pairs form one contiguous middle segment.  Its edge count
is

```text
p=96+n5+Delta_lit-1,
```

and it has `L=p+1` vertices.  Among its `p-1` transitions, one is the low
seam `H`; the other

```text
p-2=93+n5+Delta_lit=y2
```

are the selected rank-five triples.  This proves the stated rainbow-path
description and also shows that no unnamed pair or triple remains.

No middle vertex can have rank four.  A rank-four middle vertex with value
`R` is contained in an incident lower edge color `B`; since `|B|<=4`, this
would force `B=R`, contradicting that every middle edge color is nonliteral.
Thus the middle vertices lie in one rank-at-most-three component, called the
central component below.

Retain the source notation

```text
T=135-n5-x4=sum_j tj,
```

and let `tstar` be the slack of the central component.  Every nonliteral
rank-four witness is central.  Every other rank-at-most-three component has
`qj=0`, hence length `tj`; all of its internal pairs are selected at rank
five.  The satellites therefore contribute exactly

```text
g_sat=T-tstar-(s3-1)
```

embedded rank-five pairs.  If `g_c=g-g_sat`, then the central component is
the middle segment with exactly `g_c` extra low vertices attached at its two
ends by rank-five pair edges.

Let `k` be the number of nonliteral masks of ranks at most three.  There are
two cases.

* If `rho=4`, the rank-four seam `H` is a triple witness.  The `k` low
  nonliteral targets are exactly the central pairs selected at neither rank
  four nor rank five.
* If `rho=3`, every nonliteral rank-four witness is a pair.  There are
  `k-1` remaining low pair colors, and `H` is the last low target.

In either case direct central length accounting gives

```text
k=tstar-g_c=T-s3+1-g,
z1+z2+z3=231-k.                                  (A1)
```

The two seam pairs are not selected at rank four.  If `rho=4`, the number
of central pairs not selected at rank four is `tstar`; if `rho=3`, it is
`tstar-1`.  Hence

```text
rho=4 => tstar>=2,
rho=3 => tstar>=3.                               (A2)
```

Equations (A1)--(A2) independently verify (6.1j)--(6.1k).  The identities

```text
Delta_lit=x4+Delta3,
g=y1-(n4+s3-1)
 =370-2*n5-s3-x4-Delta3-n4
```

follow from `D=0`, `y1+y2=462-n5`, and the fact that exactly
`n4+s3-1` core pairs are not internal to rank-at-most-three components.
Thus (6.1h)--(6.1i) also have the correct constants.

### 3.1 Ordered-color and incidence algebra

The other general zero-margin rows also check directly.  At every ordinary
transition, consecutive lower edge colors of ranks `r,s` have rank-five
union and nonempty intersection, so

```text
r+s=5+|intersection|>=6.
```

After deleting the seam transition, a rank-two color can be adjacent only
to rank-four colors.  Each of the at most two remaining paths has at most
one more rank-two than rank-four vertex, proving `p2<=p4+2`.  For a
rank-four seam of type `(2,3)` or `(3,2)`, only one resulting path has a
rank-two seam endpoint, giving `p2<=p4+1`; for type `(3,3)`, neither does,
giving `p2<=p4`.  Thus (6.1c)--(6.1d) have no endpoint exception.

Let `B_1,...,B_p` be the middle edge colors, let

```text
Rpair=sum_i |B_i|,
```

and let `V_0,...,V_p` be the underlying vertices.  Interior vertices obey
`V_i subseteq B_i intersect B_(i+1)`.  There are `p-2` ordinary
transitions, whose unions have rank five, and one seam transition of rank
`rho`.  Adding the two endpoint bounds therefore gives

```text
sum_i |V_i|
 <=2*Rpair-[5*(p-2)+rho]
 =2*Rpair-5*p+10-rho.
```

Exactly `y1` core vertices lie outside the middle segment, and each has
rank at most four.  Also

```text
Rpair=1936-Llit-rho.
```

Consequently

```text
S<=3882+4*y1-5*p-2*Llit-3*rho,
```

which is (6.1f).  Combining it with

```text
3*S-E-5*y1>=1938-rho
```

gives

```text
15*p+6*Llit+E+8*rho<=9708+7*y1.
```

Finally, zero margin gives

```text
p=95+n5+Delta_lit,
y1=369-2*n5-Delta_lit.
```

Substitution yields

```text
29*n5+22*Delta_lit+6*Llit+E+8*rho<=10866,
```

so every coefficient and constant in (6.1e)--(6.1g) is correct.

## 4. Elimination of `n5=134`

At `n5=134`, rank-four repetition satisfies `x4=0`, so the total inner
slack is

```text
T=135-134=1.
```

A genuine outer carrier would have rank three or four.  By (A2), it would
require central slack at least three or two, respectively.  Both exceed
`T=1`.  Therefore `D=0` is impossible.

This agrees with the independent top-slice rigidity argument.  In that
slice

```text
C=P4 || D3 || Q4,
|D3|=331-n4.
```

Every pair of `D3` is a distinct nonliteral rank-four witness, every mask of
ranks one through three occurs literally in `D3`, and the literal rank-four
targets occur in `P4,Q4`.  Hence all 561 lower targets already have
singleton/pair witnesses.  There is no effective carrier credit, so the
carrier-free Hall row is one unit stronger than `D=0` permits.

Both proofs are sound and have compatible constants.

## 5. Exact `n5=133` double filtration

Here `N=332`, `y1+y2=329`, and

```text
T=2-x4.
```

Zero margin needs a carrier.  If `x4=1`, then `T=1`, too small for either
carrier rank.  Thus `x4=0`.  A rank-three carrier would require
`tstar>=3`, again impossible.  Therefore

```text
rho=4,
tstar=2,
s3=1,
g=0.
```

The central component is all of `D3`; (A1) gives `k=2`.  Thus exactly two
masks below rank four are nonliteral.  Since

```text
|D3|=332-n4,
z1+z2+z3=231-k=229,
```

the lower repetition excess is `103-n4`, and therefore

```text
Delta_lit=103-n4,
y1=n4,
y2=329-n4,
n4<=103.
```

These are exactly (6.2).

The physical pair count is also exact.  `D3` has `331-n4` pairs.  Of the
`330-n4` nonliteral rank-four targets, `H` supplies one as a triple, leaving
`329-n4` selected rank-four pairs.  The two pairs under `H` are proper
subsets of `OR(H)`, so they cannot be among those rank-four witnesses.
They are exactly the two remaining pairs.  Outer pair saturation makes
their ORs distinct nonliteral targets of rank at most three.

There are exactly `n4` pairs outside `D3`, matching `y1=n4`; all are the
selected rank-five pairs.  Inside `D3` there is consequently no selected
rank-five pair.  Its `m-2` triples, with `m=332-n4`, consist of `H` plus

```text
m-3=329-n4=y2
```

selected rank-five triples.  This establishes every line of the
cell-family ledger in Section 6 and verifies that the selected witnesses
at each rank are distinct.

### 5.1 Seam ranks and local entries

Let the two seam-pair colors be `B` and `B'`, and let
`T=OR(H)`.  They are distinct nonliteral proper subsets of `T`, and their
intersection contains the nonempty middle entry.

If `|T|=4`, neither seam color can have rank one, and both have rank at most
three.  The only possible rank pairs are therefore

```text
(2,3), (3,2), (3,3).
```

For ranks `(2,3)`, the intersection has size one.  Writing

```text
B={x,y},
B'={y,c,d},
```

the middle entry must be `{y}`.  The left entry must supply `x`, and the
right entry must supply `c,d`.  Equality with `B` or `B'` is forbidden
because those two masks are nonliteral.  Thus the segment is exactly

```text
{x}, {y}, {c,d}
```

or its reversal.

For ranks `(3,3)`, write

```text
B=I union {a},
B'=I union {b},
|I|=2.
```

The middle entry is a nonempty `Y subseteq I`.  If `|Y|=1`, the outer
entries are forced to `(I minus Y) union {a}` and
`(I minus Y) union {b}`.  If `Y=I`, the left outer entry is `{a}` or
`{a,i}` for one `i in I`, and symmetrically on the right.  The excluded
three-set alternative would make a missing seam color literal.  Hence
(6.6) is exhaustive.

The literal-value profiles follow immediately:

```text
(2,3) or (3,2): (z1,z2,z3)=(11,54,164),
(3,3):          (z1,z2,z3)=(11,55,163).
```

### 5.2 Four-windows and zero runs

Section 2 of this audit proves that all `m-3` four-windows of `D3` are
distinct rank-six witnesses.  If `s0` is the sum of the two seam-pair ranks,
then the exact window sums are

```text
U2=4*(m-3)+s0,
U3=5*(m-3)+4=5*m-11,
U4=6*(m-3).
```

For any segment and any `l`, coordinatewise binary-window counting gives

```text
U_(l+1)-U_l=R^(l)-11,
```

where `R^(l)` is the total number of coordinate zero runs of length at least
`l`.  Therefore

```text
R^(2)=m+12-s0,
R^(3)=m+4,
R^(2)-R^(3)=8-s0.
```

Thus there are exactly three length-two zero runs in the `(2,3)` case and
exactly two in the `(3,3)` case.  Every five-window contains two distinct
rank-six four-window ORs, whose union has rank at least seven.  Hence

```text
R^(4)>=m+1,
```

and the number of length-three zero runs is at most three.  All constants in
(6.4)--(6.5) are correct.

## 6. Exhaustion of the five `n5=132` modes

At `n5=132`,

```text
N=333,
y1+y2=330,
T=3-x4.
```

For the central component let `g_c` be its number of rank-five tail edges.
Equation (A1) says

```text
k=tstar-g_c,
```

with `k>=2` for a rank-four carrier and `k>=3` for a rank-three carrier.
The complete case split is then forced.

* `x4=2` gives `T=1`, too small for a carrier.
* `x4=1` gives `T=2`.  Only a rank-four carrier is possible, all slack is
  central, `s3=1`, and `k>=2` forces `g_c=0`.  This is mode A.
* `x4=0,rho=3` needs `tstar=3`.  All slack is central, `s3=1`, and
  `k>=3` forces `g_c=0`.  This is mode D.
* `x4=0,rho=4,tstar=2` leaves one unit of satellite slack.  It is one
  length-one component, so `s3=2`; `k>=2` forces `g_c=0`.  This is mode B.
* `x4=0,rho=4,tstar=3` has `s3=1`.  Now
  `k=3-g_c>=2`, so `g_c` is zero or one.  These are C0 and C1.

There is no sixth allocation of the three slack units.

For all five modes, the number of rank-at-most-three positions is
`333-n4`, so

```text
Delta3=(333-n4)-(231-k)=102-n4+k,
Delta_lit=x4+Delta3,
y1=n4+s3-1+g,
y2=330-y1.
```

Substitution gives exactly the source table:

| mode | `(x4,s3,rho,tstar,g)` | `Delta_lit` | `y1` | `y2` |
|---|---:|---:|---:|---:|
| A | `(1,1,4,2,0)` | `105-n4` | `n4` | `330-n4` |
| B | `(0,2,4,2,0)` | `104-n4` | `n4+1` | `329-n4` |
| C0 | `(0,1,4,3,0)` | `105-n4` | `n4` | `330-n4` |
| C1 | `(0,1,4,3,1)` | `104-n4` | `n4+1` | `329-n4` |
| D | `(0,1,3,3,0)` | `105-n4` | `n4` | `330-n4` |

The geometric descriptions also follow without an omitted witness class.

* In A, C0, and D, `M3` is the full central component of length
  `333-n4`.
* In B, the central component has length `332-n4`; the remaining slack-one
  satellite has `qj=0`, hence is one isolated literal lower entry.
* In C1, `M3` has length `332-n4`, and the remaining central low vertex is
  attached at an end through the unique embedded rank-five pair.

In A, B, and C1, `k=2`, so the only nonliteral masks below rank four are the
two seam-pair colors.  In C0, `k=3`, adding one further lower pair color.  In
D, the seam has rank three; its two pair colors must both have rank two, and
the three entries under the seam are distinct singletons.  Thus

```text
(z1,z2,z3)=(11,53,164)
```

in mode D.  The rank-four-carrier seams are exactly the forms audited in
Section 5.1.

Every triple internal to `M3` except `H` is a selected rank-five witness.
Its count is `|M3|-3`, which equals the table's `y2` in every mode.  The
four-window saturation lemma then makes every four-window a distinct
rank-six witness.  This verifies both witness distinctness and completeness
of the five cell modes.

The table does not fix the left/right location of the satellite or tail,
the split between `P4` and `Q4`, the seam position, or the compatible set
labels.  Those are intentionally free parameters inside a mode, not missing
sixth modes.

## 7. Chain-B analogues

### 7.1 Outer two-component accounting

After reversal, the duplicate-free two-component schedule is

```text
00,01,02,12,22,23,33,
```

with a slack-two component `C2` and a slack-one component `C1`.  Every pair
of `C1` is selected at rank five.  In `C2`, the pair blocks flanking the
triple block cover every internal triple not itself selected.  Hence no
rank-at-most-four target needs a triple anywhere in the two low components.

There are `N-2` internal low pairs.  Injecting the
`96+n5+Delta_lit` nonliteral lower targets and the `y1` selected rank-five
pair targets gives

```text
y1+2*n5+Delta_lit<=367,
y2>=95+n5+Delta_lit.
```

The constant `367` is correct and is exactly one below the one-component
carrier-resolved capacity because the second component removes one physical
pair and provides no low triple carrier.

At `D2=0`, every internal low pair is used.  The non-rank-five pairs form
one contiguous segment in `C2`, with

```text
p=96+n5+Delta_lit,
L=p+1,
p-1=y2.
```

All `p-1` transitions are distinct selected rank-five triples.  Consecutive
edge-color ranks `r,s` satisfy `r+s>=6`, because their union has rank five
and their intersection contains the shared nonempty entry.  A rank-two
color can therefore neighbor only rank-four colors, which gives

```text
p2<=p4+1.
```

The endpoint lemma forces all `L-3=y2-1` four-windows to be distinct
rank-six witnesses.

The carrier-free window sums are

```text
U2=Rpair,
U3=5*(L-2),
U4=6*(L-3),
```

and hence

```text
R^(2)=5*L+1-Rpair,
R^(3)=L+3,
# exact length-two zero runs=4*L-2-Rpair.
```

Every five-window has rank at least seven, so `R^(4)>=L+1`; at most two
zero runs have exact length three.  Equations (7.6b)--(7.6d) are correct.

The two-component coordinate ledger also has the right boundary constants.
For a coordinate `b`, the `b`-free singleton/pair cells across the two low
components number `2*Zb-Rb`, and the cells containing `b` number
`2*ob+Rb-2`.  Removing the selected rank-five pair cells gives

```text
2*Zb-Rb-ab>=385,
2*ob+Rb-2-cb>=176.
```

Using `Rb>=1`, `Rb<=ob+2`, `sum_b ab=6*y1`, and
`sum_b cb=5*y1` gives

```text
Zb>=193+ceil(ab/2),
ob>=ceil((176+cb)/3),

649+max(0,ceil((5*y1-11)/3))
 <=S
 <=11*N-2123-3*y1.
```

Thus (7.3)--(7.5) have the correct `-2`, `2123`, and `3*y1` terms.  In the
slack-one component of length `m`, all `m-1` adjacent pairs have rank five.
Summing pair incidences coordinatewise gives

```text
5*(m-1)=S1+R1-11,
S1+R1=5*m+6,
```

so (7.6) is also exact.

### 7.2 Chain-B recursive normal form

At `D2=0`, after deleting literal rank-four entries, the number of pairs not
internal to the `s3` rank-at-most-three components is

```text
n4+s3-2.
```

Every such pair is selected at rank five.  Therefore

```text
g=y1-(n4+s3-2)
 =369-2*n5-s3-x4-Delta3-n4>=0,
T=135-n5-x4.
```

All nonliteral rank-four pair witnesses lie in the central component that
contains the lower-pair segment.  Satellites have total length
`T-tstar` and contribute

```text
g_sat=T-tstar-(s3-1)
```

embedded rank-five pairs.  With `g_c=g-g_sat`, central length accounting
gives

```text
k=tstar-1-g_c=T-s3-g,
z1+z2+z3=231-k.
```

The `-1` relative to chain A is correct: chain B has no triple carrier, so
all rank-four witnesses are pairs and all `k` lower nonliteral targets are
pairs.  The central component consists of the `L`-vertex lower-pair segment
plus `g_c` tail vertices, and every satellite is a rank-five-pair path.
Thus (7.6e)--(7.6f) are exact.

Away from zero margin, the finite chain-B rank-four rows are valid as
necessary data for every word.  The total inner slack is still

```text
T=135-n5-x4,
```

so `1<=s3<=T`.  Since chain B has no low physical triple, all nonliteral
rank-four and lower targets use pairs.  Injecting the rank-at-most-three and
rank-four pair targets into the internal pairs of the `s3` components gives

```text
Delta3+n4<=369-2*n5-s3-x4.
```

Injecting rank-four and rank-five pair targets into the `N-2` physical low
pairs gives

```text
y1+(330-z4)<=N-2,
y1<=133-n5+z4.
```

These independently verify (7.11)--(7.13).  The pointwise omission count
(7.14) is the same collision injection restricted to masks disjoint from a
coordinate set `B` and is correct.  Its summed `C(7,t)` form, like (5.40),
must be restricted to `0<=t<=10` because the extra run term is unavailable
for `B=[11]`.

### 7.3 Top chain-B slice

At `n5=134`, concatenate `C2` and `C1` after removing their literal
rank-five separator.  All previously chosen lower witnesses remain internal
to one piece.  Rank-four rigidity gives

```text
Cstar=P4 || D3 || Q4,
|D3|=331-n4>=231.
```

The artificial seam cannot be internal to `D3`.  The `|D3|-1` nonliteral
rank-four targets already have witnesses internal to the original pieces,
while slack-one rigidity forces those witnesses to occupy every adjacent
pair of `D3`; an internal artificial seam would demand a nonexistent
cross-piece witness.

Nor can `D3` lie in `C1`, because every physical pair of `C1` is selected at
rank five, while every pair of `D3` is a distinct rank-four witness.  Since
`|D3|>1`, it follows that

```text
D3 subseteq C2.
```

Therefore `C2` is coordinate-complete, every entry of `C1` is a distinct
literal rank-four boundary entry, and among the 329 internal low pairs the
`330-n4` rank-four pairs are disjoint from the `y1` rank-five pairs.  Hence

```text
1<=|C1|<=n4<=100,
|C1|-1<=y1<=n4-1<=99,
F=100-n4,
y2>=329-n4,
y1+y2=328.
```

Inside `D3`, every pair is rank four.  Every triple is therefore an
uncontaminated selected rank-five witness, and the rank-six endpoint lemma
forces every four-window.  With `m=|D3|`,

```text
U2=4*(m-1),
U3=5*(m-2),
U4=6*(m-3),
R^(2)=m+5,
R^(3)=m+3.
```

Thus there are exactly two length-two zero runs and at most two
length-three zero runs.  Section 7.1's top chain-B conclusions are correct.

## 8. Witness-distinctness ledger

The late arguments use four different kinds of distinctness; all are
available, but they should not be conflated.

1. Selected witnesses for different targets in the same rank have distinct
   OR values by construction.
2. Their intervals are incomparable; hence their left endpoints and right
   endpoints are distinct and occur in a common order.
3. At zero margin, equality in the pair injection is surjective onto all
   physical pair cells not selected at rank five.  Thus such a pair cannot
   secretly have a literal lower OR value; it is the witness of exactly one
   nonliteral lower target.
4. Once the endpoint count shows that all central four-windows are selected
   rank-six intervals, their target values are distinct because the global
   selected rank-six family contains one interval for each distinct six-set.

These facts justify, respectively, the rank-four and rank-five cell ledgers,
the endpoint charges, the assertion that the seam pairs are genuinely
nonliteral, and the claim that adjacent four-window ORs are different.
Consequently every five-window used in the zero-run argument has rank at
least seven: it is the union of two distinct six-sets.

## 9. Final classification ledger

The requested late-stage status is:

| claim | audit status | qualification |
|---|---|---|
| `n5=134`, chain-A zero margin eliminated | pass | two independent proofs agree |
| `n5=133` double filtration and counts | pass | cell-family classification, not bit assignment |
| `n5=133` seam forms | pass | all `(2,3)/(3,2)/(3,3)` cases exhausted |
| five `n5=132` modes | pass | satellite/tail side and labels remain free within a mode |
| general chain-A recursive normal form | pass | necessary and lossless word-to-data form |
| chain-B collision/equality skeleton | pass | guarded by `(delta_5,s)=(0,2)` and reversal |
| chain-B recursive normal form | pass | only asserted at `D2=0` |
| chain-B top slice | pass | artificial-seam argument is valid |
| rank-six four-window saturation | pass | requires antichain common endpoint order, not merely endpoint distinctness |
| zero-run identities | pass | malformed punctuation near (6.1b7) should be repaired |
| summed recursive moments | repair | restrict to `0<=t<=10` |
| numerical rows as sufficient classifications | not claimed/invalid reading | retain necessary-template scope |

No requested late addition supplies a contradiction to a length-465 word,
and none is presented as doing so.
