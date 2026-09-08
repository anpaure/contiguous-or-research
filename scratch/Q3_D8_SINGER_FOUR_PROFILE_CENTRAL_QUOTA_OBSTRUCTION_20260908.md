# Singer four-profile central quota obstruction

2026-09-08. Pure proof; no computation. Root independently checked the
two incompatible scalar quotas below: PASS. This note closes the literal
four-profile completion and the amendment that independently reverses one
Z shore. It does not close different profile multisets.

The fixed partial bank and its literal certificate are in
`Q3_D8_SINGER_DIFFERENT_PROFILE_LITERAL_SKELETON_CHECKPOINT_20260908.md`.
Write infinity for its fixed coordinate 0. A generic bundle consists of
seven Singer translates of a cropped rank-1-through-7 chain rectangle
and the seven globally complemented rectangles. Counts below are
occurrence counts in units of one seven-point Singer orbit; they need
not be counts of distinct covered orbits.

## 1. Exact residual demands and allowed repetitions

Use profiles

    B=AABBCCDD, L=ABABCDCD, N=ABACBDCD, Z=ABCABDCD.

The proposed ten bundles have multiplicities 2BB+LN+2ZZ+5NZ. Their
rank-seven counts by number of ones are (26,76,18,0), whereas the
residual demand is (26,75,18,0). Thus the unique critical repetition
has three ones. The position theorem in the checkpoint forces its
fixed-coordinate value to be 2. Its rank-seven and rank-nine weighted
excess is 21/2. The remaining projection budget is 14, and the 128
positive central occurrences must cover 126 residual central orbits.
Consequently the only positive central repetition is a complement pair
of four-one orbits. In particular every two-one and six-one central
orbit, and every five-one critical orbit, must be covered exactly once.

The positive central residual demand, split by infinity's value, is

| Number of ones | infinity=0 | infinity=1 | infinity=2 |
| ---: | ---: | ---: | ---: |
| 2 | 27 | 14 | 27 |
| 4 | 15 | 24 | 15 |
| 6 | 1 | 2 | 1 |

Indeed the whole-cube counts are respectively (30,20,30), (15,30,15),
and (1,6,1), by fixing the coordinate in the elementary multinomial
counts. The endpoint bank subtracts (3,2,3) in the two-one class.
The seed subtracts (0,4,0), (0,6,0), and (0,4,0).
The five-one rank-seven residual demand is (6,9,3).

## 2. The literal ZZ family misses all residual six-one orbits

The one-count sequences at ranks 0 through 8 are

    B: 0,1,0,1,0,1,0,1,0
    L: 0,1,2,1,0,1,2,1,0
    N: 0,1,2,1,2,1,2,1,0
    Z: 0,1,2,3,2,1,2,1,0.

At central splits (i,8-i), i=1,...,7, literal ZZ has one-counts
(2,4,4,4,4,4,2), and NZ has (2,4,2,4,4,4,2). Neither BB nor LN
has six ones either. Coordinate development and global complement do
not change these counts. Therefore the literal family cannot cover
the four residual six-one Singer orbits.

## 3. Independently reversing one Z shore still gives a contradiction

Let R be the literal reverse of Z, namely DCDBACBA, with the same axis
names. ZR has central one-counts (2,4,6,4,2,4,2). Its generic critical
vector remains (0,8,4,0), and it supplies exactly two six-one central
occurrences. Thus both ZZ bundles must be changed to ZR in any such
amendment. BB, LN, and NZ cannot supply any six-one target.

The fixed-coordinate position theorem still applies: BB uses a short
interior pair; LN uses the L shore's B or C; each ZR or NZ placement
has type E=(g,epsilon)=(2,1) or I=(3,0), with exactly four E and
three I placements among these seven bundles. On Z, I means axis B
at positions (2,5), and E means D at (6,8); on R these become (4,7)
and (1,3).

The unique original six-one ZR cell is (Z3,R5). Its zero axis is
Z's D, and its two axis is R's D. Type I therefore contributes
(0,2,0) to the six-one central vector, and type E contributes
(1,0,1). The residual (1,2,1) forces one ZR of each type. The five
NZ bundles consequently have three E and two I placements.

For completeness, the following are the two-one central vectors:

| Bundle/placement | infinity=0,1,2 |
| --- | --- |
| BB, either allowed interior pair | (3,2,3) |
| LN, either allowed L pair | (4,2,4) |
| ZR, I | (3,0,3) |
| ZR, E | (2,2,2) |
| NZ, E | (2,2,2) |
| NZ, I on N-B at (2,5) | (2,2,2) |
| NZ, I on N-C at (4,7) or Z-B at (2,5) | (3,0,3) |

These follow by checking whether infinity is one at the original
two-one central cells: BB has indices 1,3,5,7; LN has 1,3,4,5,7;
ZR has 1,5,7; NZ has 1,3,7. Complementation swaps values 0 and 2
and keeps value 1. Choosing a different global-complement
representative merely reexpresses the same entire bundle, so the
normalization N-left/Z-right loses no NZ case.

Let r be the number of the two internal NZ placements on N-B. The
central two-one/infinity=1 count of the whole completion is

    2*2 + 2 + 2 + 3*2 + 2r = 14+2r.

The exact residual demand 14 forces r=0.

Now count critical five-one targets with infinity=0. A ZR bundle's
five-one cells are original splits (2,5),(3,4), and complements of
rank-nine splits (3,6),(4,5). Type I contributes (0,4,0) and type E
contributes (2,0,2), so the two ZR bundles contribute exactly two
occurrences with infinity=0.

For NZ the only five-one cells are the original (N4,Z3) and the
complement of (N6,Z3). In coordinate order A,B,C,D their states are

    N4=(2,1,1,0), N6=(2,2,1,1), Z3=(1,1,1,0).

Thus its five-one vectors are

| NZ fixed-axis placement | infinity=0,1,2 |
| --- | --- |
| E on N-A or Z-D | (1,0,1) |
| E on N-D | (1,1,0) |
| I on N-B | (1,1,0) |
| I on N-C or Z-B | (0,2,0) |

BB and LN have no five-one critical targets. The entire completion
therefore has exactly 2+3+r=5+r five-one/infinity=0 occurrences.
The exact residual demand six forces r=1, contradicting r=0.

This argument allows arbitrary disjoint coordinate embeddings of
the profiles, either shore containing infinity, and independent
reversal of a Z shore. It requires no assumptions about collision
avoidance: insufficient occurrence counts already prevent coverage.

## 4. Pure central corners introduce no hidden extra requirement

The endpoint bank's pure central complement pairs, represented by
the cyclic two-triple when infinity=2, are 345,035,013. Their cyclic
gap types are 115,223,124, leaving types 142 and 133 uncovered.

For a BB row C=aabbccdd, D=eeffgghh with infinity=b, its three pure
central pairs have cyclic two-triples {c,d,h}, {a,e,f}, {a,c,e}.
The first two are exactly its two infinity=1 one-one critical
necklaces. If infinity=c, the triples are {b,d,h}, {d,g,h}, {a,b,e},
and the last two are its critical necklaces. Since the two BB bundles
must supply all four remaining critical necklaces of types
124,142,133,223, they automatically cover the two missing pure
central pairs. The contradiction above concerns positive-weight
central and critical targets, not a missing pure-corner condition.
