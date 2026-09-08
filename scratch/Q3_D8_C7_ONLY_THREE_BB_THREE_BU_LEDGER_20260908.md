# A C7-only three-BB/three-BU ledger and an actual 36-row partial bank

2026-09-08. Root proposed the ledger, literal BB orbit, and paired-orbit
obstruction. Ternary_lift independently audited all counts, all positive
literal signatures, both partial-bank masses, and the compact obstruction:
PASS. This note records pure constructions and proofs. No new mathematical
computation, source preparation, or catalogue has been performed.

The decisive scope change is that future short bundles are developed under
C7 only. They are NOT required to be closed under complementation. The
initial one-sided continuation retained only the first seven-row BB
bundle below.

Subsequent status: the Section5 charge2384 continuation is now CLOSED by
Q3_D8_C7_MIXED_ORIENTATION_FIXED_AXIS_QUOTAS_AND_223_OBSTRUCTION_20260908.md,
including independently reversed BU and Z choices. A different actual
seven-endpoint restoration gives the distinct charge2391 ledger in
Q3_D8_C7_ONE_SIDED_BB_ENDPOINT_RESTORATION_2391_LEDGER_20260908.md;
that specified completion was also subsequently CLOSED by
Q3_D8_C7_ONE_ENDPOINT_2391_QUOTAS_AND_PARITY_OBSTRUCTION_20260908.md.
The literal partial banks remain valid.

## 1. The twenty-bundle completion ledger

Start with the original independently replayed 29-row skeleton of charge424
from Q3_D8_SINGER_DIFFERENT_PROFILE_LITERAL_SKELETON_CHECKPOINT_20260908.md.
Its endpoint words are00112244/33776655, its different-profile short seed
is01231230/46746575, and its final row is the central line. Its positive
projection mass is845/2 and it has no positive-weight overlap.

The proposed remaining twenty seven-row short bundles have multiplicities

    3 BB + 3 BU + 2 TT + 2 NN + 10 NZ.

Each bundle is the seven Singer translates of one literal rectangle, with
both shore chains cropped to ranks1,...,7. Each has charge98. Use the
profiles

    B=AABBCCDD, U=ABCABCDD, T=ABCCDDAB,
    N=ABACBDCD, Z=ABCABDCD,

with disjoint coordinate embeddings on the two shores. Rank-nine flags
may be reflected to rank seven for notation; that does not add a reflected
row to the bank. The occurrence counts per seven-row bundle are:

| Pair | Critical (n1=1,3,5,7), at EACH of ranks7 and9 | Central (pure,two,four,six), in C7 units |
| --- | --- | --- |
| BB | (6,0,0,0) | (3,4,0,0) |
| BU | (3,3,0,0) | (1,5,1,0) |
| TT | (0,2,4,0) | (0,2,3,2) |
| NN | (0,6,0,0) | (0,4,3,0) |
| NZ | (0,5,1,0) | (0,3,4,0) |

Their total critical vector is(27,75,18,0) at each rank, against residual
demand(26,75,18,0). Thus a completed bank has precisely one extra one-one
C7 critical orbit at rank7 and one at rank9. Each costs seven in projection
mass, for total14. All other critical orbits must be covered exactly once.

The central completion counts are(12,69,55,4). The skeleton contributes
(6,12,6,4); the nonfixed target demands are(10,80,60,8). Therefore a full
completion has eight unweighted pure excess units, one two-one C7 excess
unit, and one four-one C7 excess unit. The positive central excess is

    7*(2/4) + 7*(4/4) = 7/2+7 = 21/2.

Together with the critical14 this is49/2, exactly the available excess.
The full candidate would have169 rows and charge424+20*98=2384.
This is an algebraic occurrence ledger, not an embedded full cover. In
particular, the later rows must cover every target, including zero-weight
targets, and may not spend more than the stated repetition allowances.

## 2. An actual seven-row BB bundle

Infinity is global coordinate0. Cyclic labels0,...,6 correspond to global
(1,2,4,3,6,7,5), so Singer adds one to the cyclic label. Take

    C=00772233, D=44661155.

Equivalently, their doubled block orders are

    (A,B,C,D)=(infinity,5,1,3),
    (E,F,G,H)=(2,4,0,6).

The two shores are disjoint, each axis occurs twice, and the chains are
saturated. Cropping to1,...,7 and developing under C7 gives seven distinct
rows of charge98. A nontrivial Singer translation cannot fix either
four-coordinate support.

At rank7 its six one-one flags are all new relative to the skeleton:

    infinity1: necklace223, represented by cyclic two-triple024;
    infinity2: normalized pairs24,46,15,14,36.

At rank9, reflect each target to rank7 and normalize its unique cyclic
one to zero. The six infinity-zero triple signatures are

    246,135,136,256,236,134.

Only135 belongs to the endpoint's old triple deck
123,126,135,146,234,245,456. The other five are new. The seed's critical
targets have at least three ones and cannot overlap these. All six flags
are distinct at each rank. Thus this bundle spends exactly seven units
of positive overcoverage at rank9, and none at rank7.

At rank8 its four positive C7 orbits have signatures

    infinity1: normalized two-triple135;
    infinity2: (two-set,one-set)=(24,05),(25,14),(15,23).

The reflected infinity1 signature is246. Neither135 nor246 occurs in
the skeleton's central infinity1 list456,123,356,156,124,234. The three
infinity2 pair-distance types are(2,2),(3,3),(1,3), all distinct.
Only the middle distance type occurs in the endpoint's central deck:
translating its (03,15) to two-set25 gives one-set03, not14. The seed has
infinity1 at every central target. Consequently the new positive central
targets are distinct and disjoint from the skeleton.

The three other central cells have zero projection weight. No additional
positive ranks exist. These checks therefore audit all positive-weight
targets of this literal bundle, without a computer replay.

## 3. The two actual partial-bank masses

Retaining ONLY this first C7 bundle gives

    rows: 29+7=36;
    charge: 424+98=522;
    positive projection mass: 845/2+98-7=1027/2.

Its sole positive repetition is the rank9 orbit identified above. The
rank7 repetition allowance has not yet been spent.

If its seven reflected rows are also added, they spend another seven
units at rank7 and none elsewhere. The two new bundles are mutually
disjoint on positive targets: their critical infinity classes separate
them, and their infinity1 central signatures135 and246 are distinct after
the unique other one is normalized. This larger partial bank has

    rows: 43;
    charge: 620;
    positive projection mass: 845/2+196-14=1209/2.

The paired version is an actual partial construction too. However, the
specific twenty-bundle ledger cannot be completed after that choice, as
shown next. Neither partial bank is a whole-cube cover.

## 4. Why adding the BB complement closes this particular ledger

The three BU bundles in THIS section use the forward literal U profile.
Independent reversed-U choices require a separate orientation analysis;
the capacity equations here do not silently apply to them.

After adding both BB orbits, the remaining eighteen bundles would be

    1 BB + 3 BU + 2 TT + 2 NN + 10 NZ.

At EACH critical rank they must exactly cover(15,75,18,0), with no further
critical repetition. In particular, each rank still needs the three
infinity-one necklaces124,142,133. The single remaining BB contributes
at most one such flag at either rank, and TT,NN,NZ contribute none.
Thus the three BU bundles must supply at least two at each rank,
at least four in total.

Use the Boolean flag graph, retaining parity at rank-four vertices.
A BB six-edge path has even degree at every rank-four vertex. At rank7
a BU=AABBCCDD/EFGEFGHH has one odd upper vertex

    X=ABCE;

at reflected rank9 it has one odd upper vertex

    Y=CDGH.

For the paired partial bank, the required odd rank-four vertex orbits
at either critical rank are exactly

    H=infinity+012,
    H-complement={3,4,5,6},
    K={0,1,3,5}.

The first two are the endpoint's odd vertices. The third comes from the
already duplicated135 flag: its unique one is0, so its upper set isK.
These are three distinct orbits; exactly one contains infinity. The two
non-infinity vertices have complementary cyclic three-set classes115
and223. Exact coverage and exactly three BU odd vertices force each of
the three required odd orbits to be met once.

Let n_A,...,n_H count the infinity roles among the three BU bundles.
The exact infinity-containing odd-vertex counts give

    n_A+n_B+n_C+n_E=1,
    n_C+n_D+n_G+n_H=1.

BU's lower unique-one roles are A,E,G and its reflected-upper roles are
B,G,H. Its total infinity-one flag supply across both ranks is therefore

    n_A+n_E+n_B+2*n_G+n_H
      = 2-2*n_C-n_D+n_G
      <= 3,

because n_G<=1 by the second equation. This contradicts the required
total at least four. The paired partial bank cannot be completed with
the stated eighteen-bundle multiset, even though no complement symmetry
is imposed on those remaining bundles.

This is a scoped capacity obstruction. It neither excludes the full
C7-only ledger under a different initial choice nor invalidates the
actual partial BB construction.

## 5. The one-sided continuation, subsequently closed at charge2384

Carry forward the36-row, charge522 bank from Section3. Do NOT silently
add its complement. The remaining nineteen C7 bundles have multiplicities

    2 BB + 3 BU + 2 TT + 2 NN + 10 NZ.

Their required critical counts are

    rank7: (20,75,18,0), totaling113 target orbits;
    rank9: (21,75,18,0), totaling114 target orbits.

They have114 occurrences at each rank. Hence one future one-one
repetition remains available at rank7, while their rank9 coverage must
be exact. Every future three-one and five-one critical target must be
new. The remaining infinity-one deficits are three at rank7 and four
at rank9. Two BB bundles contribute at most two at each rank, so BU
must contribute at least one and at least two, respectively. This is
not contradicted by the paired-seed capacity argument: its exact
rank7 odd-vertex matching premise no longer applies while the remaining
rank7 repetition is free to occur.

The two central positive repetition allowances, one two-one and one
four-one C7 unit, remain unspent by the actual partial bank. Their
combined projection cost is21/2. A prospective completion must also
cover all noncritical and zero-weight targets; the quota ledger alone
does not establish their availability.

This19-bundle continuation was OPEN when the construction was saved.
It has since been closed by the separate-rank and central-quota proof
linked above. The actual36-row partial bank remains valid; the different
charge2391 endpoint-restoration question was a distinct continuation,
also subsequently closed for its specified companion multiset. No
catalogue or source was prepared for this charge2384 branch, and no
execution is reported here.
