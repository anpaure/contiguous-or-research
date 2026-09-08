# The ABCABC primitive M and a scoped P+M+BB obstruction

2026-09-08. Pure proof; no mathematical execution, placement search, or
catalogue. Root proposed M and the final parity argument. Appendix_a
independently verified every count and closure step below. Root read and
independently checked the completed file, including every table, exact
scope of the referenced lemmas, and both parity arguments: audit PASS.

The changed primitive is real and projection-tight. The closure concerns
only one complement-closed Singer bundle of each profile P,M,BB supplying
the original29-row skeleton's remaining one-one targets exactly, with
all other rows supplying no one-one target. It is not a general
obstruction to M, other endpoint decks, or ledgers permitting repeats.

## 1. Actual states, charge, and flags of M

Use distinct axes A,B,C and D,E,F,G,H, with

    M: ABCABC, ranks0,...,6 / DEDEFFGHGH, ranks2,...,8.

The retained states are

    left:  000,100,110,111,211,221,222;
    right: 11000,21000,22000,22100,22200,22210,22211.

Both are strict saturated chains of length7, giving49 targets and charge14.
Their one-count sequences are(0,1,2,3,2,1,0) and(2,1,0,1,0,1,2).
At ranks7,9,8 the combined one-count sequences are respectively

    rank7: 1,1,3,3,3,3;
    rank9: 3,3,3,3,1,1;
    rank8: 2,2,2,4,2,2,2.

Thus each critical rank has two one-one and four three-one targets;
the central layer has six two-one and one four-one target, and no pure
target. The actual projection load is

    2*(2+4*3/4)+(6*2/4+4/4)=14,

equal to charge. This is an actual row calculation.

For a one-one flag(T;o), T is its three-set of twos and o its unique one.
The original rank-seven flags are(DEF;G),(DEF;A). The rank-nine flags,
reflected only for notation, are(FGH;C),(FGH;E). Therefore a Singer-plus-
complement bundle has the four flag occurrences

    (DEF;G),(DEF;A),(FGH;C),(FGH;E),                (1)

and odd upper vertices

    DEFG, ADEF, CFGH, EFGH.                       (2)

These are distinct physical sets but can coincide after taking Singer
orbits; all parity arguments below allow such cancellations.

## 2. Fixed-axis table and exact aggregate replacement

Write infinity for the Singer-fixed coordinate. Reading (1) gives the
following counts in the order infinity=0,1,2, measured in C7 occurrence
units at rank7. Reflected rank9 has the same table; actual rank9 reverses
the first and third entries.

| M infinity role | One-one counts | Infinity-containing vertices in (2), before cancellations |
|---|---|---:|
|A or C|(3,1,0)|1|
|B|(4,0,0)|0|
|D or H|(2,0,2)|2|
|E or G|(1,1,2)|3|
|F|(0,0,4)|4|

Let P be the old AABBCC/DEDEFFGHGH primitive with the same retained
intervals, and BB the cropped4+4 double-block pair. A generic bundle
contains14 rows and has charge196. The occurrence identities are

| Provider | Critical counts(n1=1,3,5,7), at either rank | Central complementary occurrence units(pure,two,four,six) |
|---|---|---|
|P|(10,2,0,0)|(2,5,0,0)|
|M|(4,8,0,0)|(0,6,1,0)|
|BB|(12,0,0,0)|(3,4,0,0)|
|P+M+BB|(26,10,0,0)|(5,15,1,0)|

These equal the aggregates of2P+BU, at the same charge588. They are
occurrence identities; an embedding may have repeated or missing targets.

The original skeleton's exact remaining one-one table is(13,4,9).
The P one-one table is A/C:(6,1,3), B:(6,2,2), D/H:(5,0,5),
E/F/G:(4,2,4). BB contributes(6,2,4) at an interior fixed-axis block
and(6,1,5) at an endpoint. Combining these with the M table leaves
exactly three patterns:

| Pattern | P infinity | M infinity | BB infinity block |
|---|---|---|---|
|i|A/C|E/G|interior|
|ii|E/F/G|A/C|endpoint|
|iii|B|E/G|endpoint|

For completeness, the zero-coordinate equation is P0+M0=7 because BB
contributes6. Pairing5 with2 gives only two infinity-one occurrences
even with interior BB, so fails. Pairing6 with1 gives patterns i,iii;
pairing4 with3 gives ii. The infinity-one counts then force the indicated
BB endpoint choice. No other displayed values can sum to7.

## 3. Endpoint facts and the parity requirement

Use the original endpoint's forbidden zero triples and two-pairs

    F0={123,126,135,146,234,245,456},
    P2={16,35,25,26,45,56}.

The endpoint covers infinity-one necklace115; necklace223 must be newly
supplied. The following already-audited endpoint facts are used with
their original, purely local scope:

* No BB placement avoiding the endpoint flags supplies223:
  `Q3_D8_SINGER_BB_ALL_POSITIONS_AND_PATTERN_2_OBSTRUCTION_20260908.md`, Section1.
* A P supplier of223 must use E/G, and its two odd infinity vertices
  cannot form a quotient loop:
  `Q3_D8_THREE_FIVE_TIGHT_PRIMITIVE_FIXED_AXIS_AND_PROVIDER_QUOTAS_20260908.md`, Sections5,7.
* Such a P supplier cannot have an odd infinity vertex of necklace115:
  `Q3_D8_THREE_FIVE_INFINITY_G_115_223_OBSTRUCTION_20260908.md`.

In the one-one flag graph every full upper vertex has degree4, and this
remains even in the C7 quotient. BB has even upper degrees. On the
infinity-containing side, the exact remaining deck has the single odd
orbit H=infinity+012, of necklace115. Thus the XOR of all provider odd
vertices containing infinity must be{H}. This statement permits quotient
loops and all other cancellations.

## 4. Pattern ii is impossible

Here P has two infinity-containing odd vertices and M has one, the latter
being precisely M's own infinity-one flag. If P supplies223, the preceding
P lemmas exclude a loop. Parity then requires one of its two distinct
odd vertices to be H, contradicting the P115/223 lemma.

Otherwise M must supply223. Its sole infinity odd vertex is then223,
so parity forces P's two odd vertices to be exactly115 and223. For
P at E or G, one odd triple is also one of P's infinity-one flags.
Either choice would repeat the endpoint115 or M's223, violating exactness.

For P at F, its odd triples are DEG and EGH. Reversal swaps them, so
normalize DEG=012 to be the115 triple. The pair DE-G forces G=0:
G=1 gives16 and G=2 gives56. If E=1, EGH contains adjacent0,1 and
cannot be223. If E=2, EGH=223 forces H=4 or5; the pair GH-E is then
25 or35, both forbidden. Thus P at F is impossible as well. This is
the115/223 argument, distinct from the earlier115/124 two-pair lemma.

## 5. Patterns i and iii are impossible

P on its three-shore cannot supply223, and BB cannot either. Hence M
must supply it. Reversal exchanges M's E/G roles while preserving the
Singer-plus-complement bundle, so take infinity=G. Its infinity-one
flag has triple DEF=223, and its three infinity odd triples are

    DEF, CFH, EFH.

P has no infinity odd vertex in these patterns. Parity therefore forces
the other two triples CFH,EFH to have necklaces223 and115, one each.

If CFH=115, normalize CFH=012. The literal M flag(FGH;C) requires the
pair FH-C to avoid P2. C=1 gives16 and C=2 gives56, so C=0 and
FH=12. But then EFH contains the adjacent pair12 and cannot have
necklace223. If EFH=115 instead, the identical argument uses(FGH;E),
forces E=0,FH=12, and excludes CFH=223. Both possibilities fail.

All three necessary patterns are closed. Consequently P+M+BB cannot
provide an exact one-one completion of this original skeleton. This
does not invalidate M's new height profile or its tight actual charge;
it excludes only the stated generic-bundle provider ledger.
