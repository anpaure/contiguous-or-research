# One restored endpoint: exact 2391 quotas and a parity obstruction

2026-09-08. Pure proof; no mathematical execution. Root proposed the
endpoint restoration, exact moment equations, and final parity argument.
Direct-route independently checked those arguments and derived the complete
fixed-axis reduction below. Ternary_lift completed a full-file independent
audit: PASS. Root subsequently read and audited the entire proof, including
the three surviving repeat-value cases and the four-odd-vertex argument:
PASS.

This concerns only the nineteen-bundle continuation of the fixed36-row
bank, allowing independently forward/reversed BU and Z profiles, with
one specified endpoint restoration. It is not an obstruction to all
cost2391 banks or to other profile multisets.

## 1. The actual endpoint restoration and exact demands

In the retained seven-row C7 BB orbit

    C=00772233, D=44661155,

keep C cropped to ranks1,...,7 and extend D to ranks1,...,8. This adds
charge7. Its new cells have local ranks(i,8), i=1,...,7. Only i=1 has
positive projection weight: it is a rank9 one-one target with
infinity=1, and its reflected cyclic two-triple is135, necklace223.
The other new total ranks are at least10 and have zero projection weight.
The seven new rank9 targets form one previously missing C7 orbit.

Thus the restored partial bank has charge529 and positive projection
mass1041/2. The proposed remaining nineteen short C7 bundles still are

    2 BB + 3 BU + 2 TT + 2 NN + 10 NZ.

The total proposed charge is2391. The relevant profiles and orientation
conventions are those in
`Q3_D8_C7_MIXED_ORIENTATION_FIXED_AXIS_QUOTAS_AND_223_OBSTRUCTION_20260908.md`.

At each critical rank the remaining demand is(20,75,18) in n1 classes
(1,3,5). There are114 future occurrences at each rank, so exactly one
one-one orbit may repeat at each rank. The two rank8 allowances remain
one two-one and one four-one orbit. Let e7,e9 be the ACTUAL infinity
values of the future repeats at ranks7,9. The one-one residual tables
in actual rank notation are

    rank7: (13,3,4),      rank9: (9,3,8).

The three-one and five-one residual tables are unchanged.

## 2. Position moments and the central quota identity

For infinity positions ell<j, put g=j-ell, alpha=1[ell=1], beta=1[j=8].
The local critical counts are

    rank7: (ell-1,g-beta,7-j+beta),
    rank9: (ell-2+alpha,g-alpha,8-j).

Summing against the exact demands gives

    sum j=108-1[e9=2],
    sum ell=68+1[e7=0],
    sum alpha=2-1[e7=0]+1[e9=0],
    sum beta=2+1[e7=2]-1[e9=2].                    (1)

The positional minimum over the nineteen profiles is43. If E denotes
the excess above this minimum, its values are

| e7 \ e9 | 0 | 1 | 2 |
| --- | --- | --- | --- |
| 0 | 0 | -1 | -3 |
| 1 | 2 | 1 | -1 |
| 2 | 3 | 2 | 0 |

Negative entries are already impossible.

The unchanged six-one central demands force one TT infinity axis at
(3,4) and the other at(5,6). The ten NZ five-one value pairs at actual
ranks7,9 are still one each(2,2),(1,2),(0,1),(0,0), and six(1,1).
The exact16-role table in the preceding note consequently gives their
central two-one infinity1 contribution as4+L, where L counts the NZ
positions of cost4 rather than their minimum3.

Let b be the number of BB endpoint roles. For a BU let c be its excess
positional cost above1 and k its number of central two-one infinity1
cells. The following table is unchanged by reversal:

| Infinity role | c | k | k-c |
| --- | --- | --- | --- |
| B-shore A | 1 | 1 | 0 |
| B-shore B | 0 | 1 | 1 |
| B-shore C | 0 | 0 | 0 |
| B-shore D | 1 | 1 | 0 |
| U-shore E | 3 | 2 | -1 |
| U-shore F | 2 | 2 | 0 |
| U-shore G | 2 | 2 | 0 |
| U-shore H | 1 | 1 | 0 |

Every BB contributes one central two-one infinity1 cell, whether its
axis is interior or an endpoint. Every NN does also; the forced TT
contribute zero. If a1 indicates a central two-one extra at infinity1,
the unchanged demand13 gives

    sum_BU k + L =5+a1.

All NN positions are minimal and TT is forced minimal, so

    E=b+sum_BU c+L.

Let n_B,n_E count the BU roles B and E, respectively. Subtracting gives
the useful exact identity

    n_B-n_E-b=5+a1-E.                              (2)

The left side is at most3. Therefore E>=2+a1. Only the pairs
(e7,e9)=(1,0),(2,1),(2,0) survive this bound.

## 3. Exhaustive reduction of the three remaining repeat-value pairs

If E=2, equation(2) forces a1=0, n_B=3, b=0. Thus all three BU use
the B-shore B axis, both BB are interior, and L=2. Write B-plus for
forward orientation, B-minus for reversed orientation. Their one-one
infinity tables are

| Role | Rank7 | Actual rank9 |
| --- | --- | --- |
| B-plus | (2,0,1) | (1,1,1) |
| B-minus | (1,1,1) | (1,0,2) |

Let q be the number of BB infinity axes at early interior positions
(3,4); the others are at(5,6). Their combined tables are

    rank7: (8-2q,2,2+2q),
    rank9: (6-2q,2,4+2q).

For(e7,e9)=(1,0), the infinity-one demands force two B-minus and one
B-plus. Their lower infinity-zero count together with BB is12-2q,
which cannot equal the required13. This pair is impossible.

For(e7,e9)=(2,1), the demands force one B-minus and two B-plus. The
lower infinity-zero count is13-2q, so q=0. This pair would require

    both BB late at(5,6), BU={B-minus,B-plus,B-plus}, L=2.        (3)

It remains to exclude(e7,e9)=(2,0), where E=3. Its infinity-one demand
is three at either rank. If a1=1, equation(2) forces all three BU to
be B and both BB interior. They supply seven infinity-one occurrences,
but only six are permitted. Thus a1=0, and(2) reads n_B-n_E-b=2.
There are exactly two possibilities:

* Two BU use B, the third does not use B or E, and both BB are interior.
  The third BU must supply no infinity-one flag, since BB and the two B
  roles already supply six in total. Therefore it is C,D,or F, of either
  orientation. The two B roles are one plus and one minus. Subtracting
  their tables and the BB tables from the required counts forces q=0
  and requires the third BU to have(2,0,1) at BOTH actual critical ranks.
  None does:

| Zero-flag role | Rank7 | Actual rank9 |
| --- | --- | --- |
| C-plus | (2,0,1) | (3,0,0) |
| C-minus | (0,0,3) | (1,0,2) |
| D-plus | (3,0,0) | (3,0,0) |
| D-minus | (0,0,3) | (0,0,3) |
| F-plus | (1,0,2) | (0,0,3) |
| F-minus | (3,0,0) | (2,0,1) |

* All three BU use B and exactly one BB is an endpoint. If that endpoint
  is first, the BU orientations are one minus and two plus. If it is
  last, they are two minus and one plus. Let q=0 or1 according as the
  other BB axis is late or early interior. The total lower infinity-zero
  counts are respectively9-2q and14-2q. Neither can equal13.

This exhausts equation(2), so(e7,e9)=(2,0) is impossible.

Only(e7,e9)=(2,1) and the physical position pattern(3) remain. Their
moments in(1) are sum ell68, sum j108, sum alpha2, sum beta3, exactly
as in the previous note. The same central moment check forces the
two-one central extra at infinity2 and the four-one extra at infinity1.
In particular all infinity-zero critical flags are exact at both ranks
(and also at reflected rank9).

## 4. Four odd vertices force an unavailable upper repeat

Use the one-one flag graph whose lower vertices are three-sets T and
upper vertices are four-sets T union{o}; an edge is the target with
twos on T and its unique one at o. Pass to C7 orbits. The full graph
has even degree4 at every upper vertex. A cropped BB gives even upper
degrees; a cropped BU gives exactly one odd upper vertex at each
critical rank. These statements follow directly from the literal flag
patterns: for BU two edges share an upper vertex and the third supplies
the sole odd upper vertex. They remain true after reversal.

At reflected rank9 the restored partial bank leaves four odd upper
vertex orbits:

    H  = infinity+012,       infinity-containing, necklace115;
    Hc = {3,4,5,6},          not containing infinity;
    K  = {0,1,3,5},          not containing infinity;
    K' = infinity+135,       infinity-containing, necklace223.

The endpoint supplies the first two odd vertices. The retained BB has
even upper degrees as a multiset, but its already-covered135 flag is
counted only once in the residual complement; this toggles K. The new
endpoint target has infinity as its unique one and reflected two-set135,
so it toggles K'. These four orbits are distinct.

The future rank9 one-one edge multiset equals the residual edge set
plus its single repeated edge. Therefore its odd upper vertex set is
the four vertices above, toggled at the repeat's upper vertex. Three
BU can supply at most three odd vertices; BB supplies none. The repeat
must consequently cancel one of those four, rather than create a fifth.

The repeat has actual and reflected infinity value1. Its unique one is
infinity, so its upper vertex contains infinity. It must therefore be
H or K', with two-triple necklace115 or223.

But neither is available in the forced provider positions. For a late
BB, its infinity-one triples ABE and DGH also occur as infinity-zero
flags(ABE;F) and(DGH;F) at the two critical ranks. For a B-plus BU the
analogous exact infinity-zero flags are(AEF;G) and(CDH;G), and its upper
infinity-one triple is CDH. Reversal exchanges the ranks. Normalize
the unique cyclic one F or G to0. Both complementary triples must avoid
the endpoint infinity-zero deck

    {123,126,135,146,234,245,456}.

The only possible pairs are

    124/356, 125/346, 134/256, 145/236.

Their necklaces belong to124,142,133, never115 or223. The exact zero
decks make this restriction mandatory even when an infinity-one orbit
is allowed to repeat. TT,NN,NZ have no one-one targets to supply the
missing repeat instead.

Thus the parity-required rank9 repeat is impossible. The specified
2391 endpoint-restored nineteen-bundle continuation is CLOSED, including
independent BU and Z reversals. This conclusion requires no catalogue.
