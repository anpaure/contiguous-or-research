# Separate-rank quotas close the nineteen-bundle C7 continuation

2026-09-08. Pure proof; no mathematical execution, catalogue, or optimizer.
Direct-route derivation, with root's final missing-223 argument independently
checked by direct-route and ternary_lift. Ternary_lift completed a full-file
independent audit: PASS. Root subsequently read and audited the entire
proof, including the reversed-profile quota tables and the final exact
infinity-zero restriction: PASS.

Scope: retain exactly the 36-row bank in
`Q3_D8_C7_ONLY_THREE_BB_THREE_BU_LEDGER_20260908.md`. The proposed additional
nineteen seven-row C7 bundles are

    2 BB + 3 BU + 2 TT + 2 NN + 10 NZ,

where B=AABBCCDD, U=ABCABCDD, T=ABCCDDAB, N=ABACBDCD,
Z=ABCABDCD. Both shores are cropped to ranks1,...,7. Independently reversed
BU bundles and independently reversed Z profiles in NZ are allowed.
No complement closure of the selected bank is assumed.

The conclusion is that this particular multiset cannot complete that
36-row bank. The partial bank itself, other profile multisets, and other
endpoint skeletons are not excluded.

## 1. Exact separate-rank fixed-axis equations

Write infinity for the coordinate fixed by C7. In each future full shore
word, its two occurrences have positions ell<j. Put

    g=j-ell, alpha=1[ell=1], beta=1[j=8].

Each local shore rank1,...,6 occurs once at total rank7; each local rank
2,...,7 occurs once at total rank9. Therefore their infinity-value counts
in the order(0,1,2) are exactly

    rank7:       (ell-1, g-beta, 7-j+beta),
    rank9 actual:(ell-2+alpha, g-alpha, 8-j).       (1)

Reflecting rank9 to rank7 notation reverses the first and third entries.
This is only notation and does not insert any reflected row.

After the retained BB, the exact residual class counts are

| n1 | Rank7, infinity=0,1,2 | Reflected rank9, infinity=0,1,2 |
| --- | --- | --- |
| 1 | (13,3,4) | (8,4,9) |
| 3 | (30,25,20) | (30,25,20) |
| 5 | (6,9,3) | (6,9,3) |

Rank9 must be exact. Rank7 has one extra one-one C7 orbit. Let e be its
infinity value. Summing(1) gives

    sum j=108,              sum ell=68+1[e=0],
    sum alpha=2-1[e=0],     sum beta=2+1[e=2],
    sum g=40-1[e=0].                              (2)

In particular sum(g+alpha+beta) is42,44,45 for e=0,1,2.

The respective per-bundle minimum values of g+alpha+beta are

    BB:1, BU:1, TT:1, NN:3, NZ:3.

They sum to43 for this nineteen-bundle multiset. Reversal preserves this
quantity. Hence e=0 is impossible. If e=1 there is exactly one unit above
the positional minima; if e=2 there are exactly two.

## 2. The rank7 repeat must have infinity=2

Use disjoint letters A,B,C,D for the B shore and E,F,G,H for U, so the
forward BU words are AABBCCDD/EFGEFGHH. A superscript minus means global
reversal of this row; it exchanges the two critical ranks. The allowed
independent U reversal is represented this way, since the reversed B
word is again B after renaming its axes.

The following table is literal. Its middle entry counts infinity-one
one-one flags at(rank7,rank9); its final entry is positional cost above
the BU minimum1.

| Forward infinity role | Flag counts | Extra cost |
| --- | --- | --- |
| B-shore A | (1,0) | 1 |
| B-shore B | (0,1) | 0 |
| B-shore C | (0,0) | 0 |
| B-shore D | (0,0) | 1 |
| U-shore E | (1,0) | 3 |
| U-shore F | (0,0) | 2 |
| U-shore G | (1,1) | 2 |
| U-shore H | (0,1) | 1 |

For a reversed row exchange the two flag counts. To check the table,
the B-shore local ranks of the one-one cells are{1,2,6} at rank7 and
{2,3,4} at rank9. On U they are respectively{1,5,6} and{5,6,7}.

A BB contributes at most one infinity-one flag at either critical rank,
hence at most two in total. If e=1, the remaining demand is four at rank7
and four at rank9. Its positional budget excludes the double-flag G
role. Thus the total capacity is at most2*2+3=7<8. This excludes e=1.

Consequently

    e=2, sum ell=68, sum j=108, sum g=40,
    sum alpha=2, sum beta=3,                      (3)

and the positional excess above the minima is exactly two. The required
infinity-one flag counts are three at rank7 and four at rank9.

## 3. Six-one central targets force the TT and NZ five-one positions

The four remaining six-one central C7 orbits have infinity-value counts
(1,2,1). Only the two TT bundles supply them, with two cells each.
For T=ABCCDDAB, these are local shore ranks3 and5. Infinity on A or B
has value1 at both cells; on C:(3,4) it has values1,2; on D:(5,6) it has
values0,1. Thus the two TT bundles must put infinity on C and D, one
each. Both achieve their positional minimum.

Their combined five-one critical counts are(4,2,2) at rank7 and the same
at reflected rank9. The ten NZ bundles must therefore supply five-one
counts(2,7,1) at rank7 and(1,7,2) at actual rank9.

For forward NZ, its single five-one cell uses local N rank4 at rank7,
local N rank6 at rank9, and local Z rank3 at both ranks. For reversed Z,
the corresponding N ranks are2 and4, and the Z rank is5. The table lists
the infinity-value pair at the two actual critical ranks, the number
of central two-one cells with infinity=1, and the positional cost.
The Z-minus axis names preserve those of the original Z under reversal.

| Orientation and infinity role | Five-one pair | Central two-one, infinity1 | Cost |
| --- | --- | --- | --- |
| Forward N-A | (2,2) | 1 | 3 |
| Forward N-B | (1,2) | 1 | 3 |
| Forward N-C | (1,1) | 0 | 3 |
| Forward N-D | (0,1) | 1 | 3 |
| Forward Z-A | (1,1) | 1 | 4 |
| Forward Z-B | (1,1) | 0 | 3 |
| Forward Z-C | (1,1) | 1 | 4 |
| Forward Z-D | (0,0) | 1 | 3 |
| Reversed Z; N-A | (1,2) | 1 | 3 |
| Reversed Z; N-B | (1,1) | 0 | 3 |
| Reversed Z; N-C | (0,1) | 1 | 3 |
| Reversed Z; N-D | (0,0) | 1 | 3 |
| Reversed Z-A | (1,1) | 1 | 4 |
| Reversed Z-B | (1,1) | 0 | 3 |
| Reversed Z-C | (1,1) | 1 | 4 |
| Reversed Z-D | (2,2) | 1 | 3 |

For example the forward central two-one local ranks are{1,3,7} on N
and{1,5,7} on Z. Reversal gives the other half of the table.

Its critical marginals force exactly one pair of each kind

    (2,2), (1,2), (0,1), (0,0),

and six pairs(1,1). Indeed the rank7 value2 count fixes the first at1;
the rank9 value0 count fixes the last at1; the other two marginals then
fix the middle special pairs at1 each.

Call the cost4 positions in this table long. If L is their number,
the NZ contribution to central two-one infinity1 is exactly

    4+L.                                          (4)

## 4. Exact provider tables and the central quota force one pattern

Let b be the number of BB endpoint roles, z the number of BU zero-flag
roles, and t the number of BU double-flag G roles. BB endpoints lose
one from total flag capacity; zero BU roles lose one, while G gains one.
Since exactly seven infinity-one flags are required, we have

    t-z=b.

The positional budget is two. If t=1, it spends the whole budget; hence
b=0,z=1. The zero role is C, the remaining single role is B, and its
orientation must be forward to supply the upper flag not supplied by G.
This case cannot satisfy the other infinity classes. Write q for the
number of BB infinity axes at positions(3,4). Their rank7 and actual
rank9 infinity-zero one-one counts are8-2q and6-2q. Thus BU must have
counts5+2q and3+2q, with difference2. But B-plus contributes difference1,
C of either orientation difference-1, and G of either orientation
difference1. Their total difference is1, a contradiction.

Therefore t=z=b=0. Both BB are interior, and all three BU roles supply
exactly one flag: one lower and two upper. The possible roles are

    lower: B-minus (cost0), or A-plus/H-minus (cost1);
    upper: B-plus  (cost0), or H-plus/A-minus (cost1).

Here A,B mean the B-shore axes; H is the U-shore axis. Let l be0 or1
according as the lower role is interior or an endpoint, and u be the
number of upper endpoint roles. For one lower and two upper roles,
the combined BU one-one infinity-value counts are

    rank7:        (5-l+u, 1, 3+l-u),
    rank9 actual: (3-l+u, 2, 4+l-u).

The required tables give

    u-l=2q,              l+u<=2.

Exactly three positional possibilities remain:

    (q,l,u)=(0,0,0), (0,1,1), (1,0,2).             (5)

The first leaves both extra cost units to NZ, so L=2. The other two
spend both in BU, so L=0. All NN positions have cost3; TT is already
forced to its minimum, so no hidden source of excess remains.

At rank8 the remaining two-one demand has infinity-value counts
(27,13,24), with one permitted extra two-one orbit. Let a1 indicate
whether that extra has infinity=1. Each interior BB contributes one
central two-one infinity1 cell, each of these single-role BU contributes
one, each NN contributes one, and the forced TT contribute zero.
Together with(4), their total is

    2+3+2+(4+L)=11+L=13+a1.

Thus L=2 and a1=0. Both endpoint cases in(5) are impossible. Necessarily:

    both BB: infinity at late interior positions(5,6);
    BU:      one B-minus and two B-plus;
    NZ:      exactly two long positions.

This derivation uses no quotient-parity assertion and no complement
closure.

For completeness, it also fixes the central repetition classes. In
this forced pattern the two BB and three BU together have central
two-one counts(9,5,9), four-one counts(1,0,2), and pure counts(6,0,3).
The TT two-one counts are(2,0,2), and their four-one counts are(3,0,3).
Since sum g=40, while the residual positive central infinity1 demand
is39, exactly one of the two allowed positive central extras has
infinity1. The two-one extra does not, so the four-one extra does.
There are sum(ell-1)=49 future central infinity-zero incidences. The
positive residual demand there is43 and the pure contribution is6,
leaving no room for an infinity-zero extra. Hence the two-one extra
has infinity2. All repetition classes would have to be

    rank7 one-one: infinity2;
    rank9 critical: none;
    rank8 two-one: infinity2;
    rank8 four-one: infinity1.                     (6)

## 5. The surviving providers all miss the upper 223 orbit

The endpoint's infinity-zero rank7 triple deck, also valid for reflected
rank9, is

    F={123,126,135,146,234,245,456}.

Normalize a unique cyclic one to0. Two complementary three-sets in the
remaining six coordinates which both avoid F can only be

    124/356, 125/346, 134/256, 145/236.              (7)

This is the complete ten-pair list with every pair meeting F removed.
None of the eight triples in(7) has cyclic gap necklace223. This table
is a ten-case hand identity, not a new enumeration run.

Consider a late-interior BB with infinity=C in
AABBCCDD/EEFFGGHH. Its infinity-one two-triples are ABE at rank7 and
DGH at reflected rank9. The cell(4,3) gives the infinity-zero flag
(ABE;F) at rank7. The cell(6,3) at rank9, after reflection, gives
(DGH;F). Thus both complementary triples must avoid F after normalizing
the coordinate F to0. They cannot have necklace223.

For forward BU with infinity=B in AABBCCDD/EFGEFGHH, the cell(2,5)
gives the lower infinity-zero flag(AEF;G), and the cell(4,5), after
reflection, gives the upper infinity-zero flag(CDH;G). Its sole
infinity-one flag is the upper triple CDH. Again the two complementary
triples must avoid F, now after normalizing G to0. Reversal exchanges
the critical ranks and preserves the same conclusion.

These infinity-zero flags must be new in both ranks: by(6), the only
future critical repeat is rank7 infinity2. Therefore both BB and all
three BU in the forced pattern miss necklace223 at either rank where
they supply an infinity-one flag.

The 36-row bank still needs the reflected-rank9 infinity-one223 orbit.
TT, NN, and NZ supply no one-one critical targets. Hence this orbit
cannot be covered. The proposed nineteen-bundle continuation is CLOSED,
even with independently reversed BU and Z profiles. No candidate
catalogue is needed for this conclusion.
