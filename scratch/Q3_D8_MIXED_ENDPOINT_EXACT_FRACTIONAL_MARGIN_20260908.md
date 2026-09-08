# Endpoint-truncated ternary rows have exact fractional charge2358

2026-09-08. Cover-selectors. One bounded h100 LP and exact rational
certificate. Root full-file analytical review and direct_route's full
analytical/source audit passed. Root subsequently supplied the projection dual in Section 4A,
independently checked by cover_selectors, which extends the2358 lower bound
to ALL strict balanced4+4 chain rectangles. This is a fractional result,
not an integral grid cover or a new OR word.

## 1. Complete small row family

A full ternary four-axis geodesic has nine members, at ranks0,...,8.
Its histogram profile is determined by one of the fourteen Dyck height
paths h_0,...,h_8 of semilength four. At rank r its coordinate histogram is

    (4-(r+h_r)/2, h_r, (r-h_r)/2).

For each full profile retain one of the following four rank intervals:

    mode0:0..8; mode1:1..8; mode2:0..7; mode3:1..7.

This gives56 distinct shore profiles, of lengths9,8,8,7. Pair any two,
on complementary four-axis supports. Up to exchanging shores there are
1596 row types. Their actual principal costs are the sums of the two
retained chain lengths, between14 and18.

Targets in {0,1,2}^8 have45 coordinate histograms (n_0,n_1,n_2), summing
to eight. A row column counts ALL its retained pairs by histogram. The
demand for a histogram is8!/(n_0!n_1!n_2!). Thus the LP is

    minimize sum_j cost_j x_j,
    subject to sum_j column_(h,j) x_j >= orbit_size_h for EVERY h,
    and x_j>=0.                                      (1)

No ranks or boundary histograms are omitted. Uniformly averaging each
physical row over all coordinate permutations converts any feasible
solution of (1) into a fractional cover of every individual target.
Conversely, averaging an arbitrary fractional cover from this row family
preserves cost and gives (1). Therefore this is the complete fractional
cover problem for the stated endpoint-truncated family, not merely a
central-rank relaxation. The family is also closed under reflection,
although all45 histograms are retained separately.

## 2. Exact optimum and margin

The sole LP returned an objective numerically near2358. Rationalization
required no corrective scaling: all45 primal inequalities and all1596
dual inequalities already held exactly, and both objectives equal2358.
Hence

    K_fractional = 2358.                            (2)

The existing eight-axis tube gate is

    K < (35/32)*3^7 = 76545/32 = 2392.03125.

The exact fractional headroom is

    76545/32 - 2358 = 1089/32 = 34.03125.             (3)

An ACTUAL integral bank of charge at most2392 would meet the strict
improvement gate. Equation (2) does not supply such a bank: the weights
below are total weights of coordinate-averaged row families, not integer
physical row multiplicities.

## 3. Rational primal certificate

Index the56 profiles by4t+m, where t is the old full Dyck-profile index
and m is the endpoint mode above. The old catalogue order is the DFS
which takes a Dyck opening step before a closing step. All fourteen
height sequences and all56 profile metadata are saved in the certificate.

The following nineteen pair weights give cost2358 and dominate all45
orbit demands exactly or with nonnegative slack:

| Shore-profile pair | Cost | Total row weight |
|:---:|---:|---:|
|(1,3)|15|1|
|(3,11)|14|6|
|(3,39)|14|6|
|(6,31)|15|16/9|
|(7,7)|14|217/18|
|(7,23)|14|286/9|
|(7,35)|14|70/9|
|(7,55)|14|236/9|
|(9,19)|15|53/9|
|(11,11)|14|17/18|
|(18,43)|15|16/9|
|(20,22)|17|37/9|
|(27,38)|15|1|
|(28,31)|16|34/3|
|(33,50)|16|23/3|
|(35,49)|15|7/9|
|(35,51)|14|92/3|
|(45,46)|16|47/9|
|(52,53)|17|1|

The exact45-element coverage vector is saved along with the complete
integer incidence matrix. These row weights need not give a uniform
number of copies before averaging.

## 4. Rational dual and independent physical replay

Give every target of a listed histogram the indicated weight, and give
all other targets zero weight:

| Histogram | Weight per target |
|:---:|---:|
|(0,7,1)|1/2|
|(0,8,0)|2|
|(1,5,2)|2/3|
|(1,6,1)|3/2|
|(2,3,3)|5/6|
|(2,4,2)|1|
|(2,5,1)|1/3|
|(3,1,4)|1|
|(3,2,3)|1/2|
|(3,3,2)|2/3|
|(4,1,3)|1|

The total target weight is2358. Each of all1596 rows has supported
weight at most its actual cost. This proves the matching lower bound.
The displayed dual need not be reflection symmetric to be valid.

An independent recursion on actual four-tuples generated all2520 physical
four-axis geodesics, without using the Dyck histogram formula. Their
histogram paths were exactly the fourteen full profiles, and endpoint
deletions gave precisely the56 profiles. Rebuilding every pair column
from these physical profiles reproduced the full matrix and checked all
1596 dual inequalities exactly. All45 primal orbit inequalities passed,
and the exact primal-dual gap was zero.

## 4A. Universal projection dual for arbitrary strict balanced rows

The root supplied the following simpler dual after reading the certificate;
cover_selectors independently checked its formula and full quantifier.
For a target x in {0,1,2}^8, put

    y(x) = (1/4) * #{a : sum_(i!=a) x_i = 7}.         (4)

Equivalently y is n_0/4 on rank7, n_1/4 on rank8, n_2/4 on rank9,
and zero at every other rank. This is exactly the reflection-average
of the displayed numerical-LP dual, now given by a structural formula.

Let C and D be ANY nonempty strict coordinatewise chains on complementary
four-axis supports. They may be nonsaturated, arbitrarily truncated, and
need not come from the56 profiles. For a coordinate a in the C support
and a fixed member c of C, the equation in (4) fixes the required rank
of d in D. A strict coordinatewise chain has distinct total ranks, so
at most one d qualifies. Summing over the four such coordinates gives
at most4|C| incidences. The four coordinates in the D support give at
most4|D|. Dividing by four proves

    sum_(x in C x D) y(x) <= |C|+|D|.                (5)

For each deleted coordinate, its own value has three choices and the
other seven coordinates have rank7. Hence the total dual weight is

    (8*3/4) * [t^7](1+t+t^2)^7
      = 6*(1+42+210+140) = 2358.                    (6)

Together with the exact primal in Section 3, this proves that the
fractional optimum for the FULL family of arbitrary strict balanced
4+4 ternary chain rectangles is exactly2358.

Every row in the endpoint-profile family is tight in (5): each shore
retains all ranks1,...,7, while deleting one coordinate from a member
of the other shore leaves a sum between0 and6. The required counterpart
rank7-minus-that-sum is always present exactly once. This explains why
the restricted family already attains the universal balanced optimum.

## 4B. General balanced projection lower bound

The same argument works on [q]^(2m), with q>=2 and m>=1. Choose a
central rank t of [q]^(2m−1), and assign

    y(x)=(1/m) sum_a 1{sum_(i!=a)x_i=t}.

For an arbitrary strict m+m rectangle, the m deletion tests on either
shore contribute at most m times that shore's chain length. Hence y is
a valid nonnegative cost dual, with total weight

    (2m*q/m) W_q(2m−1) = 2q W_q(2m−1).

Thus every integral or fractional balanced chain-pair cover satisfies

    M_balanced(q,2m) >= 2q W_q(2m−1).

This proof permits arbitrary skips, truncations, and overlaps, but requires
every row to have the balanced support split. It does not establish the
same bound for mixed unequal splits. Direct_route independently checked
this general argument and the preceding ternary specialization.

## 5. Runtime, files, and scope

The full run, including imports, one LP, rationalization and physical
replay, took0.559223 seconds on arboghast through ssh h100. It had a
five-second outer timeout, two-CPU affinity,1GiB memory limit and one
two-second LP allowance. No integral search or second optimization ran.

- Source: q3_d8_mixed_endpoint_histogram_lp_20260908.py
- Complete certificate: Q3_D8_MIXED_ENDPOINT_HISTOGRAM_LP_CERTIFICATE_20260908.json
- Compact output: Q3_D8_MIXED_ENDPOINT_HISTOGRAM_LP_SUMMARY_20260908.json

The full-geodesic input catalogue is
q3_d8_full_geodesic_histogram_gate_20260908.py and its saved JSON, whose
logic is reused. The projection proof in Section 4A excludes cheaper
fractional covers even with arbitrary strict balanced4+4 rows. Other
support splits are outside that lower-bound argument, and no part of
the result converts the fractional margin into an integral cover.
