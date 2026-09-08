# Self-complementary translation orbits miss an explicit rank-seven target

2026-09-08. One complete h100 catalogue, followed by a pure analytic
obstruction. No LP or CP-SAT solve ran. The proposed charge-2368 bank
cannot be built from this restricted family, regardless of how many
of its rows are selected.

The cover_selectors agent independently read the full note, source,
and saved summary and reported an analytical/source audit PASS with
no corrections.

## 1. Family audited

Coordinates are E = F_2^3, labelled 0,...,7 with xor addition. Choose a
linear hyperplane H, a vector v outside H, and a full four-coordinate
ternary geodesic C on H. Its partner is D = C+v, meaning coordinate
translation. Develop the rectangle C x D by all eight translations.
Translation by v swaps the shores. Each orbit has exactly four physical
rectangles: a translation preserving a shore must preserve its rank-one
unit vector, hence must be zero. The other stabilizer element is v.

Require complement-reversal of C to equal C+h for some h in H. In step
word notation this is

    w[7-i] = w[i] xor h,  0 <= i < 8.                  (1)

For h=0 the first half is a permutation of H, giving 24 words. For any
nonzero h, the first half has exactly two entries from each of the two
h-pairs, giving 6*2^4 = 96 words. The value of h is recovered from
w[0] xor w[7], so these possibilities are disjoint. There are 312 words
before translating the first axis to zero, or 78 canonical words per H.
Seven H choices and four v choices therefore give 2184 short-orbit
candidates. A short shore retains ranks 1,...,7.

A full-orbit candidate also requires its first two steps to use the
same coordinate. With first axis zero, the first two entries are 0,0.
This forces h nonzero, and the remaining two first-half entries can
each be either element of the other h-pair. There are 3*4 = 12 words
per H, hence 7*4*12 = 336 full-orbit candidates.

The proposed bank would use one full orbit and 41 short orbits, giving
four full rectangles and 164 short rectangles, of charge

    4*18 + 164*14 = 2368.

Its rank-seven occurrence budget is exactly 32+41*24 = 1016, so every
rank-seven target would have to be covered exactly once. Each orbit is
self-complementary, giving the same requirement at rank nine.

## 2. Complete catalogue result

There are 891 target orbits under the eight translations, of which 127
are rank-seven orbits. Every rank-seven target orbit has size eight.
The complete candidate catalogue gave:

| Quantity | Count |
| --- | ---: |
| Short orbit candidates | 2184 |
| Full orbit candidates | 336 |
| Candidates surviving the internal critical-collision test | 2520 |
| Target orbits covered by at least one candidate | 751 of 891 |
| Rank-seven orbits covered by at least one candidate | 99 of 127 |
| Entirely missing target orbits | 140 |

All short candidates cover precisely three distinct rank-seven target
orbits; all full candidates cover precisely four. Thus internal
critical collisions are not the obstruction. The entire catalogue
misses 28 orbits at rank seven, 84 at rank eight, and 28 at rank nine.
All 140 missing orbits have size eight. Equivalently, 1120 individual
targets are absent from every candidate.

The first missing representative has little-endian ternary code 203,
namely

    x = (2,1,1,1,2,0,0,0).                            (2)

No solver was invoked because the catalogue itself excludes coverage.

## 3. Analytic obstruction for the explicit missing target

Write E = V direct-sum <u>, with

    V = {0,1,2,3},  u=4.

The target (2) has value 2 at 0 and u, value 1 at the three nonzero
elements of V, and value 0 at the three elements u+t with nonzero t in V.

Suppose an orbit row covered x. Orient its two shores as H and H+v and
translate the right restriction back to H. Then a strict chain C on H
must contain

    a_p = x_p,  b_p = x_(p+v),  p in H.

Because C satisfies (1), it also contains R_h(a) and R_h(b), where

    (R_h(z))_p = 2 - z_(p+h).                         (3)

Coordinatewise comparable vectors of different ranks occur in their
rank order. We show that these necessary chain memberships are
impossible for every linear hyperplane H.

Case 1: H=V. Here a=(2,1,1,1) has rank 5. The vector b has one entry 2
and three zero entries, with its 2 at p=u+v. Comparability of a and b
forces that 2 to be at p=0, so v=u and b=2000 has rank 2. But R_h(a)
has rank 3 and all its entries are at most 1. The required chain order
b <= R_h(a) is impossible at coordinate zero.

Case 2: H contains u. For some nonzero t in V, write

    H = {0,u,t,u+t},  a=(2,2,1,0).

The vector a has rank 5. If v is in V outside {0,t}, then
b=(1,0,1,0), of rank 2. The other choices of v give b=(0,1,0,1),
which is incomparable with a because its last coordinate is positive.
For the comparable choice, R_h(a) has rank 3 and vanishes at the two
coordinates h+{0,u}. This coset contains exactly one of 0 and t, the
two positive coordinates of b. Thus b <= R_h(a) is again impossible.

Case 3: H differs from V and does not contain u. Its intersection with
V is {0,t} for one nonzero t. It contains zero and two points outside V
other than u. Hence a has rank 3, with a_0=2 and a_t=1, and b has
rank 4. The required comparison is a <= b. At coordinate zero this
forces x_v=2. Since v is outside H, the only possibility is v=u.
Then b_t=x_(u+t)=0, contradicting a_t=1.

These cases exhaust the seven linear hyperplanes. They exclude x
even for arbitrary strict self-complementary chains C with translated
partner C+v; saturation and endpoint retention are unnecessary for
this obstruction. In particular, adding more rows from the stated
family, or admitting all full rows instead of only the first-two-equal
ones, cannot repair the missing target.

The proof does not exclude translation orbits with different partner
chains, with shore partitions outside the affine hyperplane family,
or without the individual complement-translation symmetry (3).

## 4. Reproducibility and limits

Only one mathematical process ran, on h100. Catalogue runtime was
0.26377706974744797 seconds, under a five-second outer process cap,
two-CPU affinity, and a 3 GiB address-space limit. No restart or solver
attempt ran. The source contains a solver stage, but that stage was
not invoked.

Local files:

* `q3_d8_translation_orbit_attempt_20260908.py`;
* `Q3_D8_TRANSLATION_ORBIT_CATALOGUE_SUMMARY_20260908.json`;
* `Q3_D8_TRANSLATION_ORBIT_CATALOGUE_20260908.json`.

The complete catalogue was copied from the remote artifact
`/tmp/Q3_D8_TRANSLATION_ORBIT_CATALOGUE_20260908_ternarylift.json`.
It contains all target representatives, target ranks and orbit sizes,
all 2520 candidate words and symmetry parameters, and each candidate's
complete target-orbit incidence list.

The exact catalogue command was:

```text
ssh h100 'timeout 5s python3 - catalogue' < scratch/q3_d8_translation_orbit_attempt_20260908.py > scratch/Q3_D8_TRANSLATION_ORBIT_CATALOGUE_SUMMARY_20260908.json
```
