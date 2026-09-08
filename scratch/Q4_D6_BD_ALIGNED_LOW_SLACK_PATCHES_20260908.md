# Explicit B/D-aligned patches with lower dual slack and a useful skip

2026-09-08. Author: appendix_a. Pure literal constructions and arithmetic;
no execution, enumeration, or search. Direct_route independently audited
Sections1–4, including their complete table, skip comparison, and ownership
map: PASS. The additional Section5 patch has independent appendix_a and
ternary_lift arithmetic/ownership audits; Section6 records the fixed-split
argument independently checked by root and ternary_lift.
These are actual local patches, not a completed improving full-cube trade.

## 1. One free axis and a spliced right chain

On an ordered support split I=(a,b,c), J=(d,e,f), keep b=c=1,
allow a to run through0,1,2,3, and let J follow members of

    F=(111,211,221,321,322,333).                     (1)

Equivalently the natural balanced shore chain is

    E=(011,111,211,311)

and the rectangle is E×F. It also has a literal1+5 representation:
the free-axis chain is(0,1,2,3), and the other five coordinates,
ordered b,c,d,e,f, follow

    11111,11211,11221,11321,11322,11333.

The final step322→333 changes two coordinates. The chains are strict
and the last step is genuinely nonsaturated. This coordinate relocation
does not change the target family or its charge. In particular, this
patch need not be regarded as essentially unbalanced.

Use the exact unrestricted quaternary dual y* recorded in Section3 of
`Q4_D6_UNBALANCED_TWENTY_POINT_PATCH_AND_PROJECTION_SCOPE_20260908.md`.
Its twelve-scaled loads at the four free-axis values are

| J state | a=0 | a=1 | a=2 | a=3 | Fiber total |
|---|---:|---:|---:|---:|---:|
|111|0|0|0|13|13|
|211|0|0|12|5|17|
|221|0|12|6|10|28|
|321|11|5|10|6|32|
|322|4|10|0|0|14|
|333|12|0|0|0|12|

Every entry follows directly from the target rank and coordinate
histogram. Thus the following four actual rows have exact costs:

| Retained J states | Targets | Charge |12-scaled dual load|12-scaled slack|
|---|---:|---:|---:|---:|
|111,211,221,321,322|20|9|104|4|
|111,211,221,321,322,333|24|10|116|4|
|211,221,321,322|16|8|91|5|
|211,221,321,322,333|20|9|103|5|

The second row is an explicit nonsaturated patch with true dual slack
1/3, strictly smaller than the earlier twenty-point patch's5/12.

## 2. Why the final skip and the initial deletion are useful

The new333 fiber has dual weight exactly one, equal to its extra
charge. It can therefore be adjoined without increasing slack.
Either saturated intermediate state323 or332 instead has fiber
weight11/12. Inserting either would increase slack by1/12.
The strict jump322→333 avoids paying for that intermediate state
while still covering the complete four-target333 fiber.

The initial111 fiber contains the high-weight target with one three
and five ones. Deleting that fiber raises slack only from4/12 to5/12.
After deletion, the row contains neither a target with one three and
five ones nor its reflected type with one zero and five twos. Indeed
J never equals111, while the permanently fixed b=c=1 prohibit the
second type. The last row in the table is consequently a genuinely
nonsaturated twenty-target patch of charge nine with no heavy-anchor
penalty of the kind proved in Section6 of the preceding note.

This does not assert that it has no other positive overlap with a
particular retained bank. Its actual private-target fit must still
be checked.

## 3. Exact fit into the inflated binary baseline

Use one of the baseline's five ordered shore splits and its chains

    A=000 100 200 300 310 320 330 331 332 333,
    B=001 101 201 301 311 321 322 323,
    D'=011 111 211 221 222 223.

The left E states011,111,211 belong to D', while311 belongs to B.
On the right,111,211,221 belong to D';321,322 belong to B;333
belongs to A. Therefore the twenty-four-point row in the table
has the following exact, disjoint ownership within that binary row:

    D'×D':9, B×D':3, D'×B:6, B×B:2, D'×A:3, B×A:1.

The heavy-free twenty-point row has counts

    D'×D':6, B×D':2, D'×B:6, B×B:2, D'×A:3, B×A:1. (2)

Thus the skip reaches actual A-chain endpoint strips while the main
part splices actual B and D' chain segments. The assertion uses complete
coordinate states, not merely a histogram or rank match.

For the heavy-free row, its positive-dual mass in those six old rows,
again twelve-scaled, is respectively

    30,15,40,6,12,0.                                (3)

All these positive targets have threshold-bit rank two, three, or
four under the cut at two. They are therefore globally private to
their indicated baseline owner, by exact middle-rank ownership in
the binary template and disjoint staircase chain partitions.
The zeros in (3) do not mean that the B×A target is dispensable:
zero-dual-weight targets still require actual coverage.

## 4. Construction implication and remaining work

The tables provide adjustable actual patch pieces with controlled
slack, including one below5/12 and another avoiding both heavy-anchor
types. The pieces may be relabeled under any coordinate permutation
and simultaneously reflected. They can also be placed on a different
ordered split, so their coarse target patterns can be distributed
among several old binary rows.

For the heavy-free piece, the positive-weight threshold patterns are
exactly the pairs{a,d},{d,e} and triples{a,d,e},{d,e,f}. The first
three include interior targets of weights1,1,1/2 in old D'×D' rows.
Consequently its lack of a heavy anchor does not automatically fit
it into the smallest old trade budgets; retained D'×D' points may
still force positive overlap.

No old row is deleted merely because a subfamily now has a cheaper
or lower-slack cover. A full trade must cover the complete residual
of every modified row, including its zero-weight private targets.
No such replacement family, full-cube cover below1280, or coefficient
improvement is asserted here. The bounded constructive outcome is
the explicit lower-slack nonsaturated patch and its literal baseline
ownership map, obtained without retrying any old search.

## 5. A heavy-free B/C'/D' patch with exact private ownership

Root supplied the following additional literal row on the same ordered
split I=(a,b,c), J=(d,e,f):

    E=(201,211,221,231), F=(210,220,221,222).         (4)

Appendix_a and ternary_lift independently checked the complete matrix
and ownership assertions below: PASS. This audit uses only the exact
dual formula and the displayed baseline chains; no execution or search
was performed.

Both chains are strict. The sixteen targets have charge eight. The
first shore fixes a=2,c=1 while b runs through all four values; therefore
the same rectangle also has the support split {b} against {a,c,d,e,f},
with the latter chain

    21210,21220,21221,21222.

This is a literal alternative support representation, not a claim that
the target set requires an unbalanced split. The fixed coordinate two
excludes a target with one three and five ones, and the fixed coordinate
one excludes its reflection with one zero and five twos.

The twelve-scaled dual matrix is

| E state / F state |210|220|221|222|Row total|
|---|---:|---:|---:|---:|---:|
|201|0|6|10|5|21|
|211|0|10|6|12|28|
|221|10|5|12|0|27|
|231|4|11|0|0|15|
|Fiber total|14|32|28|17|91|

Thus its load is91/12 and its true row slack is5/12. Its left states
201,211,221,231 belong respectively to B,D',D',C'; its right states
210,220,221,222 belong respectively to C',C',D',D'. Here

    C'=010 110 210 220 230 231 232 233.

Consequently its exact ownership within this binary macro row is

| Old row |Number of targets|Twelve-scaled dual mass|
|---|---:|---:|
|B x C'|2|6|
|B x D'|2|15|
|D' x C'|4|25|
|D' x D'|4|30|
|C' x C'|2|15|
|C' x D'|2|0|

All positive entries have threshold-bit rank three or four. More
precisely, their threshold supports are the triples {a,d,e},{a,b,d}
and the quadruples {a,d,e,f},{a,b,d,e}. They are globally private to
the indicated baseline row by the exact binary middle-rank ownership.
The remaining zero-weight points are still part of the actual patch
and cannot be omitted from a full residual-cover check.

The patch reaches B x C', which is dual-tight and has private credit
zero. The earlier identification of this shape as credit sixteen was
incorrect and is withdrawn; it does not alter the patch matrix or
ownership table above. If used while the old
owner rows are retained, its unavoidable twelve-scaled overcoverage
from these private points is at least

    6 1_{B x C' retained} +15 1_{B x D' retained}
   +25 1_{D' x C' retained}+30 1_{D' x D' retained}
   +15 1_{C' x C' retained}.                       (5)

Its own five scaled units of row slack are additional. Formula (5)
does not include other overlap caused by companion replacement rows.

## 6. Exact remaining recombination problem and the fixed-split closure

The full same-split square (B union C' union D') squared has minimum
charge132 among rows using that support split, so (4) cannot improve
the full square by same-split stitching alone. To see this without a
search, put X=B union C' union D'. It has22 points and width three:
the displayed chains give width at most three, while the three
rank-four points301,220,211, one in each chain, are an antichain.

More generally, for any finite shore posets X,Y with maximum antichains
A,B, assign weight 1_A(x)+1_B(y) to targets in X x Y and zero elsewhere.
A same-split chain pair C x D has weight at most |D|+|C|, because
each of C,D meets its corresponding antichain at most once. The total
target weight is |A||Y|+|B||X|. This remains a valid lower bound even
if replacement rows include extra targets outside X x Y. Minimal
chain partitions of X and Y attain the bound. For the present square
it is3*22+3*22=132, exactly the charge of the nine original products.
Root and ternary_lift independently checked this fixed-split argument.

The next legitimate construction must therefore use a residual with
different geometry: it may delete rows from several baseline support
splits, discard points already covered by retained rows, or employ
replacement rows on changed support splits. The precise coverage
obligation is as follows. For the fixed eighty-row baseline, let
O(x) be the set of baseline rows containing x. For any proposed set
J of removed rows, define

    U_J={x in [4]^6 : O(x) is a subset of J}.        (6)

Since the baseline covers the full grid, O(x) is never empty. Thus
U_J is exactly the set no longer covered after removing J. A valid
trade containing (4) must supply literal companion chain pairs whose
union with (4) covers every point of U_J, including all zero-dual-weight
points, at total charge strictly less than the sum of the charges of
the removed rows. The ownership table and (5) specify the patch's
actual interaction with this residual; matching only its histograms
or its positive-dual points is insufficient.

No companion family meeting (6) at a saving has been constructed in
this bounded attempt. The fixed-split full-square attempt is stopped.
The concrete outcome is the checked sixteen-point row (4), its exact
six-row geometry, and the residual condition above; no improved1280
cover or coefficient improvement is asserted.

## 7. Correction audit: B x C' has credit zero; A x D' has credit sixteen

Root identified and corrected the earlier false assignment of credit
sixteen to B x C'. Appendix_a then independently checked every entry
of the two matrices below from the dual formula: PASS. The correction
does not change any E/F patch entry, owner mass, or fixed-split result.
This is a pure hand audit, with no program execution or search.

Write R for total coordinate rank and n_j for the number of coordinates
equal to j. The twelve-scaled dual weight used in the audit is

    R=7:  6(n_0-1)_+;
    R=8:  (12+n_3-2n_0^2)_+;
    R=9:  n_1+n_2;
    R=10: (12+n_0-2n_3^2)_+;
    R=11: 6(n_3-1)_+;
    other ranks: 0.

First, with the displayed orders of B and C', its full matrix is

| B / C' |010|110|210|220|230|231|232|233|Total|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|001|0|0|0|0|0|6|5|2|13|
|101|0|0|0|0|6|11|4|5|26|
|201|0|0|0|6|5|4|11|6|32|
|301|0|0|6|5|2|5|6|0|24|
|311|0|0|11|4|5|6|0|0|26|
|321|6|11|4|11|6|0|0|0|38|
|322|5|4|11|0|0|0|0|0|20|
|323|2|5|6|0|0|0|0|0|13|

The sum is192=12*(8+8). To check privacy explicitly, the numbers of
coordinates at least two along B and C' are respectively

    B:  0,0,1,1,1,2,3,3;
    C': 0,0,1,2,2,2,3,3.

For every positive matrix entry, the corresponding two numbers sum
to two, three, or four. Every positive point is therefore globally
private by exact binary middle-rank ownership. Consequently both raw
slack and private credit are zero. The same holds for C' x B.

Second, for A and D' the full matrix is

| A / D' |011|111|211|221|222|223|Total|
|---|---:|---:|---:|---:|---:|---:|---:|
|000|0|0|0|0|0|12|12|
|100|0|0|0|0|6|5|11|
|200|0|0|0|6|4|3|13|
|300|0|0|6|5|3|6|20|
|310|0|0|11|4|11|6|32|
|320|6|11|4|11|0|0|32|
|330|6|3|5|6|0|0|20|
|331|3|4|6|0|0|0|13|
|332|5|6|0|0|0|0|11|
|333|12|0|0|0|0|0|12|

The sum is176, against twelve-scaled charge12*(10+6)=192. The
threshold counts along its shores are

    A:  0,0,1,1,1,2,2,2,3,3;
    D': 0,0,1,2,3,3.

Again every positive entry has combined threshold count two, three,
or four, and is globally private. Hence the private credit is exactly
192-176=16 for A x D' and D' x A. Their two occurrences per binary
macro row give the ten credit-sixteen rows in the saved census.

The corrected construction rationale is therefore that the earlier
heavy-free twenty-point patch already meets a genuine credit-sixteen
row, D' x A, in positive scaled mass12 as recorded in (3). The new
E/F patch's B x C' intersection has scaled mass6 but belongs to a
credit-zero row. It provides no new credit-sixteen access. No trade
claim is inferred from either ownership fact.
