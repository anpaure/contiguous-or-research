# Four actual ternary repair rows and a 167-short-row gate

2026-09-08. Pure finite construction plus one bounded literal h100
verification; no optimization or search.
Author: appendix_a. Root full-file analytical review and literal
certificate review passed; direct-route independent full analytical/source
review also passed.
The four repair rows below are proved. The remaining 167-row cover is an open integral
selection problem, not a constructed improvement.

## 1. The literal repair

Work in [3]^8={0,1,2}^8, with the fixed shores
L=(0,1,2,3) and R=(4,5,6,7). On a local four-coordinate shore, let
e_a be its a-th unit vector and let 1 denote the all-one vector.
For t=0,1,2,3 put a=t and b=t+2 modulo four, and take the chain

    C_t=(0, e_a, 2e_a, 2(1-e_b), 2(1-e_b)+e_b, 2·1).       (1)

Every comparison is strict. In particular a differs from b, so
2e_a<=2(1-e_b); the two additional coordinates outside {a,b} make
that comparison strict. The four row pairs are (C_t,C_t), with the
second copy placed on R. Explicit local chains are

    t=0: 0000 1000 2000 2202 2212 2222
    t=1: 0000 0100 0200 2220 2221 2222
    t=2: 0000 0010 0020 0222 1222 2222
    t=3: 0000 0001 0002 2022 2122 2222.

Each row is an actual six-by-six rectangle, of charge twelve and
membership thirty-six. The total charge of the repair is therefore
exactly 48. It uses nonsaturated jumps, which the q-ary tube compiler
explicitly permits.

The repair covers every point with at most one nonzero coordinate:
on its shore use 0, e_a, or 2e_a, and on the other shore use 0.
It also covers every point with at most one coordinate below two:
on that shore use 2(1-e_b), 2(1-e_b)+e_b, or 2·1, and on the
other shore use 2·1. Both a and b run over all four local coordinates.
These two extremal classes are disjoint and contain 17 points each.

The choice b=t+2 makes the entire repair invariant under full
complementation x -> 2·1-x. Indeed, complementing and reversing C_t
gives C_(t+2).

The charge 48 is optimal for repairing these extremal classes using
four-by-four support splits, even with arbitrary nonsaturated chains
and varying partitions. Exclude the global minimum and maximum, so
there are 32 required axis or coaxis targets. In a row C×D let k_C
and k_D count which of the two shore endpoints are present. A chain
contains at most two positive axis points and at most two proper
coaxis points, since distinct axis directions are incomparable.
The productive special members of C can therefore account for at
most 2k_D targets, and those of D for at most 2k_C. In four shore
coordinates the axis, coaxis, and endpoint classes are disjoint;
each productive special member accounts for just one such global
target. If the row covers z of the 32 targets, its charge is at
least z+k_C+k_D, while z<=2(k_C+k_D). Its charge is at least 3z/2.
Summing over the cover, retaining any overlaps, gives charge at
least (3/2)·32=48. This optimality statement does not include one-
or two-axis shores, where the special classes can overlap.

## 2. Exact repaired sets, including the adjacent critical ranks

For t different from v,

    C_t intersect C_v = {0000,2222}.                       (2)

To see this, the two lower axis points in each chain identify a=t,
the two upper coaxis points identify b=t+2, and no lower axis point
equals an upper coaxis point in four coordinates. Consequently any
two repair rectangles intersect in exactly the same four points:

    (0,0), (0,2·1_R), (2·1_L,0), (2·1_L,2·1_R).           (3)

All other repair targets have a unique row. The union therefore has
4·36-3·4=132 distinct targets, of which 98 are additional to the
34 extremal targets from Section 1.

The rank polynomial of each shore chain is

    A(x)=1+x+x²+x⁶+x⁷+x⁸.

Thus the exact rank polynomial of the UNION of the four rectangles
is

    4A(x)²-3(1+2x⁸+x¹⁶).                               (4)

Its coefficients from ranks zero through sixteen are

    1,8,12,8,4,0,8,16,18,16,8,0,4,8,12,8,1.            (5)

This follows directly by multiplying the displayed six-term
polynomial; it is not a sampled or inferred coverage statement.
In particular the repair covers sixteen DISTINCT rank-seven
targets and sixteen DISTINCT rank-nine targets. In each row the
rank-seven pairs of shore ranks are (0,7),(1,6),(6,1),(7,0), and
the rank-nine pairs are (1,8),(2,7),(7,2),(8,1). None is in (3),
so there are no collisions between rows on either rank.

All sixteen repaired rank-seven points have histogram (4,1,3),
where the entries count zeros, ones and twos. Their complements
give the sixteen rank-nine points of histogram (3,1,4). At rank
eight, the repair consists of ten binary corners of histogram
(4,0,4) and eight points of histogram (3,2,3). Indeed the rank-eight
pairs (0,8),(2,6),(6,2),(8,0) are corners and (1,7),(7,1) have two
ones; only the first and last corner pairs are shared between rows.

## 3. Every unrepaired target is individually eligible for a short row

Call a short row a pair of four-axis saturated chains containing
one member at each shore rank 1,...,7. Each is obtained by removing
both endpoints of a full four-axis geodesic. Its charge is fourteen.

A point x can belong to SOME such short row if and only if it has
at least two nonzero coordinates and at least two coordinates
strictly below two. Necessity holds because each of the two shores
must contain both a nonzero coordinate and a coordinate below two.

For sufficiency, construct a balanced partition as follows.

* If x has at least two coordinates equal to one, put one such
  coordinate on each shore, then distribute the other six to make
  each shore have four coordinates.
* If x has exactly one coordinate equal to one, there is also a
  coordinate equal to two and one equal to zero, by the two count
  hypotheses. Put the one-valued coordinate on L and the selected
  zero and two on R. Fill L with three and R with two of the five
  remaining coordinates.
* If x has no one-valued coordinate, there are at least two zeros
  and two twos. Put one zero and one two on each shore, then fill
  both shores to size four.

In every case neither shore restriction is the all-zero or all-two
vector, so its rank lies between one and seven. Any point of a
product of chains lies on a full saturated path from its minimum
to maximum: increase coordinates one unit at a time to the point,
then onward to the maximum. Removing the endpoints retains the
point. This proves the claimed eligibility using one COMMON
balanced partition for both requirements.

Every target left by the explicit repair satisfies these count
hypotheses, by Section 1. This is individual eligibility only; it
does not provide a small simultaneous cover.

## 4. The precise finite improvement target

Let R be the actual 132-point repair union above. The open finite
target is an integral family of at most 167 short rows covering
every point of [3]^8 outside R. Together with the four proved
repair rows, its charge would be

    M <= 167·14+48 = 2386.                             (6)

The target is not ruled out by the elementary adjacent-rank count,
but is tight there. The cube has 1016 points at each of ranks seven
and nine. The repair removes sixteen at each, leaving exactly
1000. A short row has six points at either of these ranks, since
its rank polynomial is (x+...+x⁷)². Therefore any such interior
cover requires at least

    ceil(1000/6)=167                                  (7)

short rows. A successful 167-row family has only two excess
occurrences on EACH adjacent rank, where an occurrence on an
already repaired point counts as excess as well.

The literal q-ary amplification and extra-accumulator theorem in
QARY_TUBE_AMPLIFICATION_AND_FINITE_GATE_20260906_c52e9.md would then
give the unconditional coefficient

    (2386/3⁷) beta_9
       = (76352/76545) c_9 < c_9,                     (8)

because c_9=(35/32) beta_9. Indeed 3⁷·35=76545 and
2386·32=76352. The charge threshold for improving c_9 is
76545/32=2392+1/32, so (6) has margin 193/32.

There is no active-radius probability condition in this implication:
it is a full q-ary template followed by the proved minimum-clock
transfer. Equation (8) remains CONDITIONAL on the missing integral
167-row interior cover. No fractional template has been substituted
for that cover.

## 5. An alternative repair with 138 distinct targets

The following four rows retain charge 48 and the same adjacent-rank
repair, but increase the actual union by six central corners. They
need not be invariant under coordinatewise complementation. On each
shore S use the six-point formula (1) with the global first and last
axes a,b from this table:

| L | R | a_L | b_L | a_R | b_R |
|---|---|---:|---:|---:|---:|
| 0246 | 1357 | 0 | 2 | 1 | 3 |
| 0145 | 2367 | 4 | 1 | 2 | 6 |
| 0123 | 4567 | 3 | 0 | 5 | 7 |
| 0356 | 1247 | 6 | 5 | 7 | 4 |

Every coordinate occurs exactly once among the first axes and once
among the last axes. Any shores belonging to different rows intersect
in exactly two coordinates: these are the four distinct linear
hyperplane partitions given by the three binary digits and their sum.

No nonbinary point belongs to two rows. If a one-valued coordinate
occurred in both, it would be a first axis in one and a last axis in
the other, because each role occurs only once globally. Its first-axis
shore has zeros at the other three coordinates, whereas its last-axis
shore has twos at the other three. Their two-coordinate intersection
contains a coordinate other than the selected one, a contradiction.

For binary points, identify the support of the coordinates equal to
two. Support sizes one and seven are unique by the first/last-axis
condition. Sizes two and six are unique by the disjoint first/last
pairs. A support of size three, or the complement of a support of
size five, is a three-subset of a shore; equality between two rows
would contradict the two-coordinate shore intersections. At size
four, the eight full shores are distinct. A mixed target has three
coordinates on one of its shores, so it cannot equal a full shore
from another row. The eight mixed supports are explicitly

    0157, 0146, 2347, 0245, 3456, 1235, 1267, 0367,

and are pairwise different. These cases exhaust all binary targets.
Thus the ONLY targets repeated between rows are the global minimum
and maximum. The exact union polynomial is

    4A(x)²-3(1+x¹⁶),                                 (9)

giving 138 distinct targets. Its central rank contains sixteen
corners and eight noncorners; all other rank counts agree with (5).
This union size is optimal among four six-by-six rectangles that
all contain the global minimum and maximum: their 144 occurrences
must repeat each of those two targets at least four times, leaving
at most 144-3·2=138 distinct targets.
Every extremal target is still repaired because all first and last
axes occur. Sections 3 and 4 therefore apply with this alternative
actual repair as well, with the same 167-row lower bound and the
same conditional charge 2386. The additional six repaired targets
are an explicit improvement of the repair set, not a proof that
the missing simultaneous short-row cover exists.

## 6. Literal certificate and inherited necessary histogram optimum

The authorized literal check ran only on h100, in 0.025843 seconds
of mathematical runtime, under a one-second outer process cap.
It checked all support partitions, strict chain comparisons, all
pairwise rectangle intersections, and all 6,561 ambient target
memberships independently from the row-pair union. It also checked
extremal coverage, (9), and every one of the 45 histogram counts.
The source and exported literal rows/coverage certificate are

* `q3_d8_affine_extremal_repair_verify_20260908.py`;
* `Q3_D8_AFFINE_EXTREMAL_REPAIR_CERTIFICATE_20260908.json`.

The exact command was

```text
ssh h100 'timeout 1s python3 -' < scratch/q3_d8_affine_extremal_repair_verify_20260908.py > scratch/Q3_D8_AFFINE_EXTREMAL_REPAIR_CERTIFICATE_20260908.json
```

The difference from the simple repair's histogram union counts is
zero on 44 histograms and +6 on the central-corner histogram (4,0,4).
The previously certified necessary 105-type histogram relaxation
for the simple repair had optimum 500/3 rows; see
`Q3_D8_FIXED_REPAIR_SHORT_HISTOGRAM_SUMMARY_20260908.json` and its
source `q3_d8_fixed_repair_short_histogram_gate_20260908.py`.
Its exact primal remains feasible for the affine repair because
only that one demand decreases. Its rank-nine dual remains valid
and still has value 1000/6=500/3. Consequently the new necessary
histogram relaxation also has exact optimum 500/3, without running
another LP.

These are histogram-count inequalities only. The fixed repair
breaks full coordinate symmetry; a feasible histogram relaxation
is not a fractional cover of its individual residual targets.
The two repair sets need not be contained in one another. The
167-row actual interior selection remains open.
