# Literal Singer skeleton and a four-profile completion ledger

2026-09-08. The literal skeleton and its exact incidence ledger have now
passed one fixed-construction replay on h100, in 0.065736 seconds of
mathematical runtime. The source is
`q3_d8_singer_different_profile_skeleton_verify_20260908.py`; the complete
saved certificate is
`Q3_D8_SINGER_DIFFERENT_PROFILE_SKELETON_CERTIFICATE_20260908.json`.
No candidate catalogue, LP, or integer search has run in this direction.
The proposed completion remains unconstructed.

## 1. Actual 29-row skeleton, charge 424

Let S=(0,2,4,6,3,1,7,5), acting on coordinate labels 0,...,7.
For the hand audit write the fixed coordinate as infinity, and write
the seven cyclic coordinates as k=0,...,6, corresponding to global
labels (1,2,4,3,6,7,5). Then S adds one modulo seven to k.

The endpoint words, in global coordinates, are

    C_end=00112244, D_end=33776655.

Take the seven Singer translates with both shore ranks 0,...,7,
and their seven global complements with ranks 1,...,8. Their cost
is 14*16=224. The lower first axes are global 0 and 3 and both
start with a repeated axis. Thus the lower orbit repairs every
axis and the global minimum; its complement repairs every coaxis
and the global maximum. In cyclic notation the words are
infinity,infinity,0,0,1,1,2,2 and 3,3,5,5,4,4,6,6.

The genuinely different-profile seed words are

    C_seed=01231230, D_seed=46746575.

Crop both shores to ranks 1,...,7 and develop under Singer and
global complementation. This gives fourteen rows of cost 196.
In cyclic notation the words are infinity,0,1,3,0,1,3,infinity
and 2,4,5,2,4,6,5,6. C is all-opening; D opens three axes,
closes two, then opens the fourth. Coordinate infinity is always
one in these cropped rows. D never has an all-ones state, so the
whole row never contains all ones. It covers the nonfixed seven-
one target orbit exactly once and avoids the fixed A_0 target.

Finally add the chain (0,1,2) on global coordinate 0 times the
singleton all-ones state on the other seven coordinates, cost 4.
It covers the three central fixed targets. The other six fixed
targets are already repaired by the endpoint rows. Total: 29 rows,
28 of them balanced, and charge 224+196+4=424.

## 2. Hand audit of the critical signatures

For seed targets, infinity has value one. The following table gives
the cyclic zero set Z and two set T at rank seven. The first six
are original splits (i,7-i), i=1,...,6. The last six are complements
of original rank-nine splits (i,9-i), i=2,...,7.

| Cell | Z | T |
| --- | --- | --- |
| Original 1 | 013 | 24 |
| Original 2 | 136 | 24 |
| Original 3 | 36 | 2 |
| Original 4 | 6 | empty |
| Original 5 | 56 | 0 |
| Original 6 | 456 | 01 |
| Complement 2 | 245 | 13 |
| Complement 3 | 24 | 3 |
| Complement 4 | 24 | 6 |
| Complement 5 | 02 | 6 |
| Complement 6 | 01 | 6 |
| Complement 7 | 013 | 56 |

There are five three-one, six five-one, and one seven-one orbit.
For the three-one entries, the zero triples have different cyclic
gap types except the two entries with Z=013; those have different
two sets. For the five-one entries, normalize the unique two to
cyclic position zero. The zero pairs become respectively

    14, 56, 16, 35, 13, 12,

which are distinct. Thus all twelve nonfixed critical orbits are
distinct. Complement symmetry proves the rank-nine statement.

Every endpoint critical target has exactly one one. Its fourteen
orbits are distinct by the following signatures. With infinity=2,
normalize the unique cyclic one to zero; the cyclic two pairs are

    16, 35, 25, 26, 45, 56.

With infinity=0 the normalized two triples are

    456, 123, 126, 245, 135, 146, 234.

The remaining orbit has infinity=1 and cyclic two triple 345.
The endpoint and seed critical targets are disjoint by number of
ones. They cover 26 of the 145 nonfixed rank-seven orbits, with
class counts (n1=1,3,5,7) equal to (14,5,6,1).

## 3. Hand audit of zero positive projection overlap

At rank eight the seed has fourteen distinct orbits, all with
positive projection weight. For its four two-one orbits, normalize
the unique cyclic one to zero; the two triples are

    356, 156, 124, 234.

For its four six-one orbits, normalize the unique zero to zero;
the position of the unique two is respectively 3,1,4,6. Its six
four-one orbits have (Z,T) pairs

    (13,24), (24,13), (36,24), (24,36), (56,01), (01,56).

The pair-distance signatures distinguish these, except the two
(2,2) and two (1,1) cases; their relative pair positions differ.

The endpoint rows have eight positive-weight central orbits. Two
have infinity=1 and normalized two triples 456 and 123, distinct
from the seed's four such triples. Three have infinity=2 and
one-pair/two-pair cyclic distances (3,2), (3,3), (1,1); their
complements have infinity=0. These six cannot meet the seed.

Thus no skeleton target with positive projection weight is repeated.
For y(x)=one-quarter times the number of seven-sum projections, the
balanced rows have y-charge 420 and the central line has y-charge
5/2. The skeleton covers y-mass 845/2 without excess. The remaining
140 short rows would cost 1960 and must cover residual y-mass
3871/2, leaving exactly 49/2 weighted excess in a completed bank.
There are 126 residual nonfixed positive central Singer orbits.

## 4. Residual quotas and overlap alternatives

The 145 nonfixed critical Singer orbits have n1-class counts
(40,80,24,1). After the skeleton the residual counts are
(26,75,18,0). Their splits by fixed-coordinate value x0=0,1,2 are

| n1 | x0=0 | x0=1 | x0=2 |
| ---: | ---: | ---: | ---: |
| 1 | 13 | 4 | 9 |
| 3 | 30 | 25 | 20 |
| 5 | 6 | 9 | 3 |

Ten generic fourteen-row bundles have 120 critical orbit-occurrence
units for those 119 residual nonfixed orbits. They may repeat one
nonfixed critical orbit. Alternatively, they may cover all 119
exactly and supply seven copies of fixed A_0; the central line
already covers A_0 once. This fixed-point alternative must not be
silently excluded from the general Singer direction.

All-ones load from a generic fourteen-row bundle would add excess
28 and is forbidden by the available 24.5. Nonfixed central Singer
orbits occur in distinct complement pairs, so central excess is a
multiple of seven. A unique nonfixed critical overlap with n1
equal to 1,3,5,7 has total rank-seven/rank-nine excess respectively
14,10.5,7,3.5. Consequently only n1=3 or n1=7 is possible, with
central excess 14 or 21. The fixed A_0 alternative also contributes
3.5 and belongs to the latter case.

## 5. A literal four-profile completion family

Use these literal word patterns, with arbitrary disjoint coordinate
embeddings:

    B=AABBCCDD, L=ABABCDCD,
    N=ABACBDCD, Z=ABCABDCD.

For a pair P,Q, let f_P(i) count its one-valued coordinates at
shore rank i. Its generic-bundle n1 vector is read from the six
sums f_P(i)+f_Q(7-i), i=1,...,6, and six sums
f_P(i)+f_Q(9-i), i=2,...,7. This gives:

| Pair | (n1=1,3,5,7) critical vector | Pure central cells per original row |
| --- | --- | ---: |
| B/B | (12,0,0,0) | 3 |
| L/N | (2,10,0,0) | 0 |
| Z/Z | (0,8,4,0) | 0 |
| N/Z | (0,10,2,0) | 0 |

The proposed remaining multiplicities are

    2(B/B) + 1(L/N) + 2(Z/Z) + 5(N/Z).

Their total is (26,76,18,0), choosing exactly one n1=3 overlap.
Their positive central incidence is 128 Singer units for 126
residual positive central orbits. Thus exactly one complement
pair must repeat, with n1=4, giving central excess 14. This is an
exact profile ledger, not an embedded completion or cover.

Developing just these four literal pair prototypes under S8 and
then closing under complement gives respectively 1440,2880,2880,
5760 generic fourteen-row bundles, total 12960, before filters.
Identical-word pairs have a shore-swap stabilizer of size two;
different-word pairs have trivial stabilizer. Z/Z and N/Z require
the additional reversed-profile S8 orbit. None of these profiles
is all-opening, so none of these bundles can have size seven.
This finite family has not been generated.

## 6. The fixed-coordinate position theorem for this profile multiset

If coordinate 0 occurs at positions ell<j in its full shore word,
put g=j-ell and epsilon=1_(ell=1)+1_(j=8). Counting original local
ranks 1,...,6 and complemented local ranks 2,...,7 gives the
generic-bundle critical incidence by x0 as

    (7-g, 2g-epsilon, 5-g+epsilon).

The residual x0 demand is (49,38,32). An extra occurrence in x0
equal to 0,1,2 would require respectively

    (sum g, sum epsilon)=(20,2), (21,3), (21,4).

For the prescribed multiplicities, the minimum of sum(g+epsilon)
is 2 from the two B/B bundles, 2 from L/N, and 21 from the seven
Z/Z and N/Z bundles. Equality 25 is possible only in the x0=2
case. Therefore the repeated n1=3 target must have x0=2, and all
positional minima are forced:

- B/B: coordinate 0 is an interior B or C axis, positions (3,4)
  or (5,6), hence (g,epsilon)=(1,0).
- L/N: coordinate 0 lies on the L shore at (2,4) or (5,7), hence
  (g,epsilon)=(2,0).
- Z/Z or N/Z: coordinate 0 has (g,epsilon)=(2,1) or (3,0), with
  exactly four endpoint cases and three internal cases among the
  seven selected bundles. Z allows only B:(2,5) or D:(6,8);
  all four N axes are allowed.

These necessary position filters reduce the ungenerated family
to B/B720, L/N720, Z/Z1440, N/Z4320, total 7200 bundles. Root and
direct_route independently audited the position theorem: PASS.

The two B/B and one L/N bundles alone must partition all 26 residual
one-one critical orbits: their x0 counts are two copies of (6,2,4)
plus (1,0,1), totaling (13,4,9). Such targets are flags T subset
T union {o}, with |T|=3. Under Singer their rank-three/rank-four
quotient graph has 8+10 vertices and 40 edges. A B/B constituent
supplies an alternating six-edge path; its complement supplies
another. The four remaining x0=1 triple necklaces have circular
gap types 124,142,133,223; the endpoint pair used 115. The two
B/B bundles must pair those four necklaces, each using two
disjoint triples with one cyclic coordinate unused.

## 7. Completed skeleton verification and scope

The executed source expands exactly the fixed 29 rows, checks
chains, charge, Singer/complement closure, all extremes and fixed
targets, all 6561 loads, and zero positive-weight overlap. It also
saves the 945 Singer target orbits and their 473 orbits after
complementation, residual targets, and raw/distinct critical counts.
It contains no candidate generation or optimization. It ran once after
the master-reading task was complete, through ssh h100 with a three-second
timeout; the process returned exit code zero. All assertions passed.
The 29 rows cover 1423 of 6561 targets, or 211 of 945 Singer orbits;
367 of the 473 Singer/complement target orbits remain uncovered. Maximum
load is seven, but every positive-projection-weight target has load at
most one. The rank-seven class table, 126 residual positive central
Singer orbits, all 34 extremes, and all nine fixed targets were replayed
exactly from the literal chains. This is a partial construction certificate,
not a whole-cube cover or a record.

No 2384 whole cover exists in this checkpoint. The actual result
is a hand-audited charge-424 partial skeleton and a motivated,
position-constrained four-profile completion problem.
