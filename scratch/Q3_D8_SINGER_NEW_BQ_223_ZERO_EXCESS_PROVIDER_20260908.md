# A new literal B/Q provider of the missing 223 necklace

2026-09-08. Pure hand calculation by ternary_lift. No computation,
candidate catalogue, or new source has been run or prepared for this
construction. Direct_route independently audited the entire hand proof,
including every signature and orbit size: PASS. Automated literal replay
remains pending. The result is a partial bank, not a complete cover.

## 1. A different profile that preserves the aggregate ledger

Put B=AABBCCDD and Q=AABBCDCD. Q has shore heights

    0,1,0,1,0,1,2,1,0.

For a cropped B/Q pair developed under G=C7 x complement, the critical
vector by numbers of ones 1,3,5,7 is (10,2,0,0). Its central occurrence
vector by numbers of ones 0,2,4,6 is (2,5,0,0). Consequently replacing
BB+BL by two BQ preserves both entire aggregate vectors:

    BB+BL : critical (20,4,0,0), central (4,10,0,0),
    2 BQ  : critical (20,4,0,0), central (4,10,0,0).

Thus 2BQ+BU+TT+NN+5NZ is a different ten-bundle multiset with the same
aggregate critical and central ledger as the closed BB+BL+BU proposal.
This equality alone asserts no feasible embeddings or fixed-axis quotas.

The literal B/Q pair uses letters A,B,C,D on its B shore and E,F,G,H
on its Q shore, so the words are AABBCCDD / EEFFGHGH. Its ten one-one
critical flags (two-set; unique one) are

    (AEF;G), (AEF;B), (ABE;F), (ABE;C), (ABC;E),
    (BCD;H), (CDH;G), (DGH;C), (DGH;F), (FGH;D).

Compared with the corresponding BB pair, the two flags (EFG;A) and
(CDH;B) have become three-one targets. Their removal is why the proved
all-position BB223 obstruction does not apply to BQ. The two odd
rank-four vertices of the BQ flag graph are AEFG and BCDH, a
complementary pair.

## 2. Actual fourteen-row bundle

Keep the ORIGINAL verified 29-row skeleton. Infinity is global 0;
cyclic axes 0,...,6 correspond to global (1,2,4,3,6,7,5). Choose

    (A,B,C,D,E,F,G,H)=(6,0,4,5,3,1,infinity,2)

in cyclic notation. In global coordinates the actual words are

    C=55116677, D=33220404.

Crop both shore chains to ranks 1,...,7 and take all seven Singer
translates and their complements. This gives fourteen distinct rows
of charge196. Each word uses its four axes twice, and the shores are
disjoint. A Singer stabilizer is impossible for a four-axis shore.
Complement cannot take the row into its Singer orbit: the fixed axis
occurs at positions5,7 on Q, whereas in the reversed word it occurs
at2,4. Thus the bundle really has fourteen rows.

The ten one-one critical signatures are:

| Infinity value | Signatures |
| --- | --- |
| 0 | normalized two-triples136,256,236,134,235 |
| 1 | two-triples136 and245, of necklace types223 and142 |
| 2 | normalized two-pairs15,14,34 |

For infinity0 or2, normalize the unique cyclic one to zero. These
signatures are all distinct. The infinity-zero list avoids the old
endpoint's123,126,135,146,234,245,456; the infinity-two list avoids
16,35,25,26,45,56; and the infinity-one list avoids endpoint115.
Therefore this actual bundle supplies the missing223 orbit while
repeating none of the endpoint's one-one critical targets.

## 3. All other positive-weight targets are new

At rank seven the other two targets have infinity1 and cyclic
(zero-set,two-set)

    (045,13), (136,45).

The first translates by3 to (013,46), different from the seed's
(013,24) and (013,56). The second has the seed's zero necklace136
but two-set45 instead of24. Neither agrees with the other seed
three-one orbits (456,01) and (245,13). They are distinct from each
other and from every endpoint critical orbit. Complementation gives
the rank-nine assertion.

At the central layer the five positive G-orbits can be represented
as follows. For infinity1, normalize the other one to cyclic zero
and give the two complementary two-triples. For infinity2, give
the cyclic two-set T and one-set O.

| Central type | Signatures |
| --- | --- |
| infinity1 | 146/235, 136/245 |
| infinity2 | (T,O)=(13,26), (25,14), (12,35) |

The infinity1 signatures avoid the skeleton's two-triples
456,123,356,156,124,234. The three infinity2 entries have respective
(one-pair distance,two-pair distance) (3,2),(3,3),(2,1), hence are
mutually distinct. The first two have the same distance pairs as
two endpoint entries but different relative position: translating
endpoint (35,04) to two-set13 gives one-set25, not26; translating
endpoint (03,15) to two-set25 gives one-set03, not14. The third
distance pair is absent from the endpoint. The seed has infinity1
at every central target. Therefore none of these five G-orbits
meets a positive central skeleton target.

The two other central occurrences are pure and have projection
weight zero; their repetitions are irrelevant to the claimed
zero positive-weight excess. Neither row shore pair can contain
all ones, since the B profile never has four ones.

Thus every positive-weight target in the new bundle has load one,
and none was positively covered by the skeleton. This hand check
uses all ranks where the projection dual is positive:7,8,9.

## 4. Exact partial-bank scope and next decision

The hand-checked union has43 rows, charge620, and zero positive
projection excess. Its projection mass is

    845/2 + 196 = 1237/2.

The difference3/2 between charge and projection mass remains the
original central line's deficit. The remaining critical demand
by one-count1,3,5,7 is (16,73,18,0). Its one-one demand by infinity
value0,1,2 is (8,2,6). No assertion of coverage away from the audited
positive-weight targets, or of a full-cube completion, is made.

The new BQ's fixed-axis positions are (5,7), giving gap2 and
endpoint indicator0. Its odd complementary rank-four class is223.
Any proposed remaining provider bank must respect that parity;
the aggregate replacement in Section1 does not bypass this condition.

The next informative computational question, if separately authorized,
would be a fixed-construction replay of these fourteen rows together
with the saved skeleton. It would not enumerate further placements.
No such replay or source preparation has been authorized here.
