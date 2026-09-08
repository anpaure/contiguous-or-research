# Two literal TT bundles compatible with the C7-only partial bank

2026-09-08. Author: appendix_a. Pure construction and hand proof; no
mathematical execution, catalogue, or search. Root subsequently read and
independently checked the full literal words, critical and central
signatures, and mass accounting: audit PASS. This gives a compatible
explicit extension of the36-row bank
in `Q3_D8_C7_ONLY_THREE_BB_THREE_BU_LEDGER_20260908.md`. It does not impose
these TT choices on the separate BB/BU provider problem and is not a
full-cube cover.

## 1. Literal rows and the four missing six-one orbits

Use infinity for global coordinate0, and cyclic labels0,...,6 for global
coordinates(1,2,4,3,6,7,5). Singer adds one to every cyclic label and fixes
infinity. A TT row has full shore words

    ABCCDDAB / EFGGHHEF,                             (1)

with eight distinct axis labels. Both shore chains are cropped to
ranks1,...,7. Its two six-one central cells are the splits(3,5),(5,3),
whose oriented zero-to-two axis pairs are

    D -> G, H -> C.                                 (2)

The skeleton already covers the four finite-pair differences1,3,4,6.
Thus the missing six-one C7 orbits are infinity-to-finite,
finite-to-infinity, and finite differences2 and5. A TT row contributes
exactly two such cells. Two TT rows covering this residual without
repetition must put infinity on a short role in each: one zero role
(D or H), and one two role(C or G). After shore swaps and translations,
the first may be written D=infinity,G=0,C-H=delta, with delta=2 or5;
the second must supply the opposite finite difference.

Here are explicit choices. First let P have cyclic role assignments

    (A,B,C,D)=(2,4,3,infinity),
    (E,F,G,H)=(6,5,0,1).

Let R be the precursor row with assignments

    (A,B,C,D)=(1,5,6,infinity),
    (E,F,G,H)=(2,3,0,4),

and let Q be the global complement of R's cropped rectangle. Equivalently,
reverse both full words for R before cropping. The literal global words
for the two rows to retain are

    P: 46330046 / 57112257,
    Q: 72005572 / 34661134.                         (3)

Every axis occurs twice on its shore, the shore supports are disjoint,
and the paths are saturated. Develop each of P,Q under C7, yielding
fourteen rows of total charge196. Only these two C7 orbits are added;
the complements of P and Q are not automatically included.

Their six-one zero-to-two pairs are respectively

    P: infinity -> 0, 1 -> 3;
    Q: 6 -> 4, 0 -> infinity.                      (4)

They supply exactly the four missing orbits. No nontrivial Singer shift
fixes a four-axis shore support, so each developed row orbit has size7.
The positive-target checks below also show that these two row orbits
are distinct and create no positive repetition.

## 2. Complete three-one critical signatures

For a target write Z,T for its cyclic zero and two sets; infinity's
value is displayed separately. Rank-nine targets are reflected to rank
seven solely for comparing signatures. This notation does not add any
row to the bank. The full three-one table is

| Rank/signature source | Row | infinity | Z | T |
|---|---|---:|---|---|
|7|P|0|34|01|
|7|P|2|015|3|
|7|Q|0|16|04|
|7|Q|2|024|6|
|reflected9|P|0|23|01|
|reflected9|P|2|016|3|
|reflected9|Q|0|56|04|
|reflected9|Q|2|034|6|

At either rank, the two infinity-zero entries cannot coincide: their
two pairs have cyclic distances1 and3. For infinity-two entries,
translate the unique cyclic two to zero. Their normalized zero triples
are245 versus135 at rank7, and345 versus145 at reflected rank9.
They are distinct. The skeleton's three-one critical targets all have
infinity=1; the retained BB bundle has only one-one critical targets.
Thus every target in this table is new, with no internal repetition.

## 3. Complete five-one critical signatures

When infinity=0, a five-one rank-seven target has one additional cyclic
zero z and a unique cyclic two t; record the difference z-t. When
infinity=1, translate the unique two to zero and record the zero pair.
When infinity=2, only the cyclic zero pair is needed, and its orbit is
determined by its cyclic distance. The complete table is

| Rank/signature source | Row | infinity=0 differences | infinity=1 normalized zero pair | infinity=2 zero pairs |
|---|---|---|---|---|
|7|P|3,1,5|45|none|
|7|Q|2|23|04,06|
|reflected9|P|2|26|01,03|
|reflected9|Q|6,4,5|15|none|

At either rank the four infinity-zero differences are distinct.
The two infinity-two pairs have different distances1 and3. The two
infinity-one signatures are distinct and avoid the skeleton's six
normalized pairs

    14,56,16,35,13,12.

All skeleton five-one targets have infinity=1, and the BB bundle has
none. This verifies novelty and absence of repetition for every entry.

For clarity, these tables exhaust the critical cells: each TT row has
two three-one and four five-one cells at each of ranks7 and9, with no
one-one or seven-one cell. Consequently the two bundles add, separately
at each critical rank, infinity-class counts(2,0,2) for three-one targets
and(4,2,2) for five-one targets. The corresponding remaining five-one
demand after the skeleton and these TT rows is(2,7,1).

## 4. Complete central checks

TT's central one-count sequence is(2,4,6,4,6,4,2), so all seven cells
have positive projection weight. Their six-one cells were checked in
(4). The four-one cells have infinity0 or2. For infinity0, normalize
the unique cyclic zero to zero and record the cyclic two pair. For
infinity2, normalize the unique cyclic two to zero and record the zero
pair. All six four-one signatures are

| infinity | From P | From Q |
|---:|---|---|
|0|45,26|15|
|2|45|15,23|

They are distinct within each infinity class. The skeleton's four-one
central targets have infinity1, and the retained BB bundle has no
four-one cell. Thus all six are new.

For two-one central targets with infinity2, use the pair(T,O) of cyclic
two and one sets. For infinity0, reflect the target only for notation,
and use its reflected(T,O). The four two-one signatures are

| Actual infinity | Row and source | (T,O) |
|---:|---|---|
|0|P, central split(1,7)|(34,25)|
|2|P, central split(7,1)|(23,46)|
|2|Q, complement of R split(1,7)|(56,13)|
|0|Q, complement of R split(7,1)|(16,25)|

The skeleton's infinity2 endpoint deck is

    (35,04),(03,15),(01,23),                        (5)

and its infinity0 deck is the reflected deck. Their pair-distance types
(two-pair distance,one-pair distance) are(2,3),(3,3),(1,1).
The retained BB bundle's infinity2 deck is

    (24,05),(25,14),(15,23),                        (6)

with types(2,2),(3,3),(3,1); it has no infinity0 central cell. All other
two-one targets in the partial bank have infinity1 and cannot coincide
with the new entries.

The new types are(1,3),(1,2),(1,2),(2,3). The first three therefore
avoid the relevant old decks by distance alone. For the last entry,
the only possible old match is(35,04): the unique translation sending
35 to16 adds3, and sends04 to03, not25. It is therefore new too.
Finally, the two new infinity0 entries have different two-pair distances.
For the two infinity2 entries, the unique translation sending23 to56
adds3 and sends46 to02, not13. They too are distinct.

This checks all fourteen central occurrences. There is no central
positive repetition, either internally or against the36-row bank.

## 5. Actual partial extension and its scope

The projection weight y(x)=one-quarter times the number of coordinate
deletions whose remaining sum is7 is supported only at total ranks7,8,9.
Sections2–4 therefore check every positive target of both TT rows. Each
TT row has projection load14: its critical ranks contribute7/2 each
and its central rank contributes7. All positive target orbits in the
two bundles are nonfixed and have size7.

The36-row bank had charge522 and covered positive mass1027/2. Adding
the fourteen literal TT rows yields

    rows: 50;
    charge: 718;
    positive projection mass: 1419/2.

Its only positive repetition remains the already recorded rank-nine
one-one BB orbit. Neither central repetition allowance is spent, and
the remaining rank-seven one-one repetition allowance is unchanged.

The remaining profile multiset, if this compatible extension is used,
is2 BB+3 BU+2 NN+10 NZ. This is a literal partial bank with correctly
covered six-one orbits, not a completion theorem. In particular the
separate provider question should continue to use the original36-row
bank unless these TT choices are deliberately fixed: a failure after
fixing them would not close all possible TT choices. No further TT
catalogue or execution is proposed or reported here.

Subsequent scope update: the entire specified nineteen-bundle provider
multiset has now been closed independently of these TT choices, in
`Q3_D8_C7_MIXED_ORIENTATION_FIXED_AXIS_QUOTAS_AND_223_OBSTRUCTION_20260908.md`.
Its endpoint-restored charge2391 variant is also closed in the separate
`Q3_D8_C7_ONE_ENDPOINT_2391_QUOTAS_AND_PARITY_OBSTRUCTION_20260908.md`.
The actual fifty-row partial extension above remains valid. The same TT
rows can be added to the endpoint-restored bank: that restoration adds
only a positive one-one target, while TT has none, so the restored
fifty-row bank has charge725 and positive mass1433/2.
