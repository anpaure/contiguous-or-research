# An infinity-G 3+5 primitive cannot supply both 223 and a 115 odd vertex

2026-09-08. Pure hand proof by appendix_a. Ternary_lift independently
checked the full reduction and every forbidden flag identity: PASS.
Root subsequently read and independently checked the complete proof,
including all six assignment cases: audit PASS. No mathematical execution,
catalogue, or search was performed.

Scope: consider the complement-closed Singer development of

    AABBCC / DEDEFFGHGH,                            (1)

with eight distinct coordinate labels, the three-axis shore retaining
ranks0,...,6, the five-axis shore retaining ranks2,...,8, and infinity=G.
It is impossible for such a primitive simultaneously to avoid every
original skeleton one-one target, supply an infinity-one target of
necklace223, and have an infinity-containing odd upper vertex of
necklace115. This note does not address coincident odd-vertex orbits
that cancel in the quotient, nor a different primitive or a BU supplier
of223.

## 1. The exact flags and the normalization

Write a one-one target as(T;o), with twos on the three-set T and its
unique one at o. The ten critical flags of (1), consisting of original
rank-seven cells and reflected rank-nine cells, are

    (DEF;G), (DEF;A), (ADE;F), (ADE;B), (ABD;E),
    (BCH;G), (CGH;B), (CGH;F), (FGH;C), (FGH;E).  (2)

Thus infinity-G placements have four infinity-zero flags, two
infinity-one flags, and four infinity-two flags. After translating
the unique cyclic one to zero, the relevant signatures are

    infinity0: (DEF)-A, (ADE)-F, (ADE)-B, (ABD)-E;
    infinity1: DEF and BCH, up to Singer translation;
    infinity2: (CH)-B, (CH)-F, (FH)-C, (FH)-E.     (3)

Subtraction from a set means subtracting that cyclic label from every
element, modulo7. The original skeleton forbids the normalized decks

    mathcal F={123,126,135,146,234,245,456},
    mathcal P={16,35,25,26,45,56},                 (4)

for infinity0 and infinity2, respectively. Its infinity-one one-one
target is the necklace115 orbit.

At upper vertices, the pairs of flags in (2) cancel except at DEFG
and EFGH. These are infinity+DEF and infinity+EFH. Since DEF itself
is an infinity-one target, exact avoidance of the skeleton excludes
DEF from necklace115. Therefore an odd vertex of necklace115 must
arise from EFH. Every necklace115 triple is three consecutive cyclic
coordinates. Translate all labels to normalize

    {E,F,H}={0,1,2}, {A,B,C,D}={3,4,5,6}.         (5)

The flag(FGH;E) immediately forces E=0: E=1 gives(FH)-E=16,
and E=2 gives(FH)-E=56, both forbidden by (4). Hence {F,H}={1,2}.
Next the flag(FGH;C) forces C=5 or6: C=3 gives(FH)-C=56,
and C=4 gives(FH)-C=45. Both possibilities for C=5,6 survive
this initial test, so neither is silently discarded.

For checking the remaining223 condition, its complete cyclic triple
orbit is

    {024,025,035,135,136,146,246}.                 (6)

At least one of DEF,BCH must belong to this list.

## 2. Complete six-case assignment reduction

After the forced choices E=0 and C in{5,6}, the following six rows
exhaust every assignment that could supply223. They use only literal
flags from (2); no extra collision assumption is needed.

| F,H,C | Remaining case | Consequence or forbidden flag |
|---|---|---|
|1,2,5|A,B,D permute3,4,6|Neither DEF nor BCH belongs to (6), so223 is absent.|
|1,2,6|A,B,D permute3,4,5|DEF cannot be223; BCH can be223 only if B=4. Then(CH)-B=(62)-4=25 is forbidden.|
|2,1,5|A,B,D permute3,4,6|223 requires B=3 or D=4. B=3 gives(CH)-B=(51)-3=25. Otherwise D=4 forces B=6,A=3, giving(CH)-B=(51)-6=26.|
|2,1,6|B=3; A,D permute4,5|(CH)-B=(61)-3=35 is forbidden.|
|2,1,6|B=4; A,D permute3,5|(ADE)-F=(350)-2=135 is forbidden, independent of the order of A,D.|
|2,1,6|B=5; A,D permute3,4|BCH is not223, so DEF requires D=4,A=3. Then(DEF)-A=(402)-3=146 is forbidden.|

For the third row, if B=3 is excluded and D=4 is required, the only
other possible B is6 because A,B,D are exactly3,4,6. For the last
three rows, B ranges over all of3,4,5. Thus the displayed cases omit
no order of the four labels A,B,C,D, and both possible orders of F,H
are covered.

Every nonempty223 branch yields a forbidden pair25,26,or35, or a
forbidden triple135 or146. All belong to (4). This proves the claim.

## 3. Exact conclusion and boundary

In this infinity-G primitive family, a skeleton-avoiding223 supplier
cannot also furnish the endpoint's infinity-containing115 odd orbit.
The contradiction already follows from avoidance of old one-one
targets; it does not require an assumption about internal distinctness
of the remaining primitive targets.

The proof concerns an actual115 odd vertex. It does not analyze the
separate possibility that the two displayed odd upper vertices lie
in one non-115 Singer orbit and cancel, and it does not exclude the
entire two-primitive-plus-BU family when BU supplies223 instead. Those
are separate questions.
