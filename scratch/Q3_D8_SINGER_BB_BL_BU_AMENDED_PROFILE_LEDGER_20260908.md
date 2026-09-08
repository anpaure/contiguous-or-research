# Singer BB+BL+BU amended profile ledger

2026-09-08. Pure calculation of seven-entry height sequences; no mathematical
code, catalogue, or optimization was run. This is a necessary-quotas result,
not an embedded cover. Root and ternary_lift independently audited the full
note, including the literal flags, five position patterns, and quotient
parity rule; both audits passed.

Keep either of the hand-checked endpoint skeletons discussed in the Singer
continuation, the old different-profile seed, and the central line. They
have the same rank-class counts and charge 424. The original literal
skeleton is documented in
`Q3_D8_SINGER_DIFFERENT_PROFILE_LITERAL_SKELETON_CHECKPOINT_20260908.md`.

## 1. A genuinely different provider triple

Use the following profiles on four distinct axes:

    B=AABBCCDD, L=ABABCDCD, N=ABACBDCD,
    Z=ABCABDCD, T=ABCCDDAB, U=ABCABCDD.

Their height sequences, meaning numbers of coordinates equal to one at
shore ranks 0,...,8, are

    B: 0,1,0,1,0,1,0,1,0
    L: 0,1,2,1,0,1,2,1,0
    N: 0,1,2,1,2,1,2,1,0
    Z: 0,1,2,3,2,1,2,1,0
    T: 0,1,2,3,2,3,2,1,0
    U: 0,1,2,3,2,1,0,1,0.

All shores are cropped to ranks 1,...,7. Each bundle is developed under
Singer translations and global complementation, giving fourteen rows.
At rank seven its twelve occurrence units are read from the six original
splits (i,7-i) and the complements of six rank-nine splits (i,9-i).

| Pair | Critical vector by n1=1,3,5,7 |
| --- | --- |
| BB | (12,0,0,0) |
| BL | (8,4,0,0) |
| BN | (6,6,0,0) |
| BU | (6,6,0,0) |
| TT | (0,4,8,0) |
| NN | (0,12,0,0) |
| NZ | (0,10,2,0) |

In particular BU preserves BN's critical vector. Explicitly its original
critical one-counts are (1,1,3,3,3,1), and its complemented critical
one-counts are (1,1,1,3,3,3).

The amended ten-bundle multiset is

    BB + BL + BU + TT + NN + 5 NZ.

Its critical vector is (26,76,18,0), exactly the old desired vector.
Thus an actual completion would have one repeated nonfixed three-one
critical orbit. Its rank-seven/rank-nine projection cost is 21/2.

## 2. Exact central quota advantage

For the central layer, use G occurrence units: one original cell and its
complement developed under Singer give one complement-paired unit. These
are occurrence counts; collisions may prevent them from being distinct
target orbits. All profiles here avoid all ones, so the relevant positive
central target orbits have size fourteen.

| Pair | Central one-counts at splits (i,8-i), i=1,...,7 | (pure,two,four,six) |
| --- | --- | --- |
| BB | (2,0,2,0,2,0,2) | (3,4,0,0) |
| BL | (2,2,2,0,2,2,2) | (1,6,0,0) |
| BN | (2,2,2,2,2,2,2) | (0,7,0,0) |
| BU | (2,0,2,2,4,2,2) | (1,5,1,0) |
| TT | (2,4,6,4,6,4,2) | (0,2,3,2) |
| NN | (2,4,2,4,2,4,2) | (0,4,3,0) |
| NZ | (2,4,2,4,4,4,2) | (0,3,4,0) |

Consequently BB+BL+BU supplies (5,15,1,0), while BB+BL+BN would supply
(4,17,0,0). The BU substitution replaces two two-one central occurrences
by one pure occurrence and one four-one occurrence, preserving projection
mass and the whole critical vector.

The amended completion supplies (5,36,27,2). The endpoint adds
(3,4,0,0), and the seed adds (0,2,3,2). Thus the entire balanced bank
has central occurrence counts

    (pure,two,four,six) = (8,42,30,4).

The nonfixed central target demands are (5,40,30,4). Therefore the positive
central ledger permits exactly two excess occurrence units among the
two-one complement pairs, and no repetition among four-one or six-one
targets. The two units need not belong to two different repeated pairs.
Each such excess unit has projection cost 14*(2/4)=7, giving total 14.
Together with the critical excess 21/2, this is exactly the available
49/2 projection excess. The unweighted pure central repetitions are free
in this ledger; actual coverage of all five pure orbits remains required.

An actual 29-row skeleton plus these ten bundles would have 169 rows and
charge 424+1960=2384. No coordinate embeddings satisfying these necessary
counts, or full-cube coverage, are asserted here.

## 3. Why the intermediate BB+BL+BN replacement cannot work

With the same seven higher bundles, BB+BL+BN leaves 66 positive central
G occurrence units for only 63 residual target orbits. Each positive
central excess unit costs at least seven. Hence three such units cost at
least 21, exceeding the central budget 14.

Changing only the seven higher profiles while retaining their zero
one-one critical contribution cannot fix this by adding pure central
cells. A pure central cell in a cropped saturated rectangle has shore
ranks i,j in {2,4,6}. Both immediate predecessors (i-1,j) and (i,j-1)
remain in the cropped rectangle and are one-one critical targets. Thus
every higher row with no one-one critical cell is pure-central-free.

The BU substitution avoids this obstruction by changing a provider that
already carries one-one critical targets. It is outside the proved
endpoint obstruction for the different provider triple 2BB+LN.

## 4. Exact fixed-coordinate class quotas

For the three providers, use disjoint letters A,B,C,D on a B shore and
E,F,G,H on its partner. In particular BU means

    AABBCCDD / EFGEFGHH.

Its six one-one critical flags, written (two-set; unique one), are

    (EFG;A), (AEF;G), (ABC;E),
    (BCD;H), (CDH;B), (CDH;G).

Let b be 1 when infinity occupies an endpoint pair of BB and 0 for an
interior pair. Let g and e be the gap and endpoint indicator for infinity
in BL, so g is 1 on its B shore and 2 on its L shore. The one-one vectors
by infinity=0,1,2 are

    BB: (6,2-b,4+b),    BL: (4,g-e,4-g+e).

The residual demand (13,4,9) therefore forces BU to have vector
(3,j,3-j), with

    g-e+j = 2+b.                                      (1)

The literal six flags give this table for BU:

| Infinity axis | BU one-one vector | gap | endpoint indicator |
| --- | --- | ---: | ---: |
| B-A | (3,1,2) | 1 | 1 |
| B-B | (3,1,2) | 1 | 0 |
| B-C | (2,0,4) | 1 | 0 |
| B-D | (3,0,3) | 1 | 1 |
| U-E | (3,1,2) | 3 | 1 |
| U-F | (4,0,2) | 3 | 0 |
| U-G | (3,2,1) | 3 | 0 |
| U-H | (3,1,2) | 1 | 1 |

Thus B-C and U-F are excluded immediately. Put t=1 for the two remaining
long placements U-E,U-G and t=0 for the others, and write e_U for BU's
endpoint indicator. Its gap is 1+2t; among its central cells infinity is
one at 1+t two-one cells and t four-one cells.

TT must put infinity on its short C or D axis. These are the only choices
that give the required six-one vector (1,2,1); putting infinity on a long
T axis gives (0,4,0). At the short positions TT has five-one critical
vector (4,2,2). Consequently the five NZ bundles must supply (2,7,1).
The literal NZ five-one states N4,N6,Z3 give exactly the following rule:

- One NZ placement Q is N-A or Z-D.
- One NZ placement R is N-D or N-B.
- The other three are N-C, Z-B, Z-A, or Z-C.

Here N and Z each use their own A,B,C,D labels. Let z count the long Z-A
or Z-C placements among the last three, let a count Z-A placements, and
let d=1 for R=N-D and d=0 for R=N-B. Then

    sum_NZ gap = 14-d+z-a,    sum_NZ epsilon = 1+d+a.

Let i=1 when infinity is on an internal N axis of NN, and i=0 at an
endpoint. NN's gap is 2+i and its epsilon is 1-i. It supplies 1+i
central four-one cells with infinity=1. Since the four-one deck must be
exact, its required middle count 24 gives

    d+a = 1+t+i.                                      (2)

Summing gaps and endpoint indicators over all ten bundles now yields

    sum gap = 18+g+t+z,
    sum epsilon = 3+b+e+e_U+t.                         (3)

The general critical incidence formula (7-gap,2gap-epsilon,5-gap+epsilon)
requires (sum gap,sum epsilon)=(20,2),(21,3),(21,4) when the repeated
three-one critical target has infinity=0,1,2 respectively. The first
case is impossible in (3). In the other two cases

    g+t+z=3,
    b+e+e_U+t = 0 or 1 respectively.                  (4)

Equation (1) excludes t=1 in the remaining case where it could contribute
the sole unit on the left of (4). Thus infinity in BU is restricted to
B-A, B-B, B-D, or U-H. The full provider position list is:

| Repeated critical infinity | BB | BL | BU | z |
| ---: | --- | --- | --- | ---: |
| 1 | interior | B-interior | B-B | 2 |
| 2 | endpoint | L-interior | B-B | 1 |
| 2 | interior | L-endpoint | B-B | 1 |
| 2 | interior | B-interior | B-A or U-H | 2 |
| 2 | interior | L-interior | B-D | 1 |

For NZ and NN, equation (2) simplifies to d+a=1+i. Together with their
literal choices above, this gives all remaining class-count conditions.
The central two-one/infinity=1 incidence is 2(5+g+t+z)=16, whereas the
residual demand is 14. Hence one excess two-one G unit has infinity=1
and the other has infinity=0/2. They therefore belong to different
fixed-coordinate classes, strengthening the aggregate allowance in
Section 2.

## 5. A quotient-parity rule for actual provider placements

A one-one critical target is an edge from its three-set of twos to the
four-set obtained by adding its unique one. A BB constituent has even
degree at each four-set after its six-edge path is counted. The BL flags
give odd four-sets

    AEFG, BCDH, ABCE, DFGH,

which are two complementary pairs. The BU flags above give odd four-sets

    X=ABCE, Y=CDGH.

The endpoint residual has odd four-set orbit vertices H,Hc. Passing to
the Singer quotient preserves all these degree parities. Therefore BU's
two odd orbit vertices must be complementary or must coincide. They
cannot coincide: this would require infinity in their intersection C or
outside their union F, precisely the two BU positions excluded by the
one-one x0 quota.

Hence Y and Xc=DFGH are in the same Singer orbit. They differ by the
replacement F to C. On their side containing infinity this says that two
distinct cyclic triples, sharing two coordinates, are translates. Such a
triple is a three-term arithmetic progression in the seven-cycle: its
intersection with a nonzero translate has size two, so the two translation
edges form a path on its three points. The possible circular-gap necklace
types are exactly 115,133,223.

Let u be this BU complementary-pair class, e the endpoint's class, and
l_1,l_2 the classes of BL's two complementary pairs. Parity gives:

    if u=e, then l_1=l_2;
    if u differs from e, then {l_1,l_2}={u,e}.

This is an additional necessary geometric rule. It does not assert that
an embedding satisfying the rule covers the one-one deck, or any other
rank.

## 6. AP normalization and the original endpoint's BU B-B restriction

The preceding parity test has a concrete normalization. Suppose first that
infinity is B-A or B-B. The two cyclic triples

    X without infinity,
    Yc without infinity

share the two axes in {A,B,E} other than infinity, and differ by C versus
F. They are translates. Hence, for some cyclic phase r and nonzero step
k modulo seven, they are

    {r,r+k,r+2k}, {r+k,r+2k,r+3k}.

C and F are the exchanged outer endpoints, the shared axes occupy the
middle two positions, and D,G,H occupy the complementary three-term AP
{r+4k,r+5k,r+6k}. The two directions of the exchange are allowed. If
infinity is B-D or U-H, apply the same statement to Xc and Y: C,F are
again the exchanged endpoints, the two cyclic axes in {D,G,H} are the
middle positions, and A,B,E occupy the complementary AP. This describes
necessary coordinate geometry using a phase, a nonzero step, and small
within-block orders; it asserts no sufficiency for the flag cover.

Now fix the ORIGINAL endpoint bank C=00112244, D=33776655, whose infinity
one-one necklace is 115. Suppose BU puts infinity on its B-B axis. Put

    T={A,E,F}, U={C,D,H}.

Normalize the unused cyclic axis G to zero. Both T and U occur as
infinity=0 one-one critical signatures with their unique cyclic one at
G: T is the original (2,5) cell; U is the complement of the rank-nine
(4,5) cell. The endpoint already covers the seven such signatures

    123,126,135,146,234,245,456.

Since T and U partition the six nonzero cyclic positions, avoiding those
seven signatures leaves exactly

    124/356, 125/346, 134/256, 145/236.

Their pairs of circular-gap necklace types are respectively

    (124,142), (133,124), (142,133), (133,133).

The AP parity condition says that T has the BU odd-pair class u, which
is one of 115,133,223. Thus u is forced to be133, and only the last three
displayed complementary pairs remain. The unique infinity-one critical
signature U can have type133,124,or142. This restriction uses only the
original endpoint's one-one critical deck; it does not use seed overlap
or any later rows. It is necessary, not a construction or a complete
provider obstruction.
