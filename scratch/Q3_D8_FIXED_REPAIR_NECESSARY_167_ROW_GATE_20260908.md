# A fixed four-row repair leaves a necessary minimum of167 short rows

2026-09-08. Cover-selectors diagnostic using appendix-a's literal repair.
One h100 LP, with exact rational certificates. Root full-file analytical
review and direct_route's full analytical/source audit passed. The LP below is ONLY a
necessary histogram relaxation for a fixed residual target set; its
feasible primal is not a fractional physical cover of that set.

## 1. Literal repair and independent union census

Use fixed shores (0,1,2,3) and (4,5,6,7). For t=0,...,3 set a=t and
b=t+2 modulo4 in each shore. On both shores use the six-member chain

    0, e_a, 2e_a, 2(1-e_b), 2(1-e_b)+e_b, 2*1.

All comparisons are strict, including the nonsaturated middle jump.
The four products have charge4*(6+6)=48. Each has36 distinct targets;
any two intersect in exactly the four products of the zero and top
shore corners. Thus their actual union has132 targets, not144.

The h100 checker rebuilt every chain and product, checked all six
pairwise row intersections, and independently enumerated all6561
ambient tuples using shore membership. It found exactly the same132
covered targets. They include all targets with at most one nonzero
coordinate or at most one coordinate different from two.

The union has16 rank7 targets,16 rank9 targets, and18 rank8 targets.
The middle targets comprise ten binary corners and eight members of
histogram(3,2,3). The repair is invariant under coordinatewise reflection.

The earlier variant b=t+1 was also rebuilt independently. It has the
same132-point union size and exactly the same45-bin histogram counts.
The two actual unions need not coincide. The diagnostic therefore has
the same orbit-count input for either variant; the saved physical repair
uses the finalized complement-invariant b=t+2 choice.

## 2. Necessary all-histogram relaxation

Every residual row is the product of two full ternary four-axis geodesics
with both endpoints removed. Its shore ranks are1,...,7, its charge is14,
and it has49 targets. The fourteen Dyck histogram paths yield105
unordered row types. For each of all45 target histograms h, subtract
the number of DISTINCT repair targets of that histogram from its full
orbit size; call the result d_h. The necessary LP is

    minimize sum_j x_j,
    subject to sum_j A_(h,j) x_j >= d_h for EVERY h,
    and x_j>=0.                                      (1)

All ranks and all histogram classes are included. The fixed repair
breaks coordinate symmetry. Consequently a feasible solution of (1)
does not give an averaged physical cover of the unrepaired targets:
an averaged row may cover the already repaired part of an orbit instead.
The LP is necessary for any physical completion, and is not sufficient.

## 3. Exact optimum500/3

The sole LP and exact rational replay gave

    minimum histogram row count = 500/3.             (2)

The dual is especially simple: put weight1/6 on every rank9 target and
zero elsewhere. The repair covers16 of the1016 rank9 targets, leaving
1000. Every double-truncated row has exactly six rank9 cells, so its
dual price is one. Thus every physical completion needs at least

    ceil(1000/6) = 167 rows.                          (3)

The residual rank9 histogram counts are8,168,560,264 for
(0,7,1),(1,5,2),(2,3,3),(3,1,4), respectively. The matching rational
primal below satisfies all45 inequalities, showing that the histogram
relaxation has no stronger obstruction than (2).

Shore indices refer to the existing fourteen full Dyck profiles, each
restricted to ranks1,...,7:

| Shore pair | Row weight |
|:---:|---:|
|(0,0)|1|
|(0,2)|6|
|(0,4)|6|
|(0,7)|151/6|
|(1,1)|15|
|(5,5)|277/6|
|(6,9)|59/3|
|(8,13)|20|
|(11,11)|41/3|
|(12,13)|14|

No corrective scaling was needed. Every primal constraint and all105
dual prices were checked with exact fractions; the primal-dual gap is zero.

## 4. Meaning of the remaining finite gate

The proposed167-short-row completion plus repair would have charge

    167*14+48 = 2386,

below the improvement threshold76545/32. The necessary LP does NOT
exclude this proposal, but leaves only1/3 row of fractional room.
Ranks7 and9 each have1000 unrepaired targets, while167 short rows supply
1002 occurrences at each rank. Therefore a valid completion has at most
two excess occurrences at EACH of these ranks, counting both duplicates
among short rows and occurrences already supplied by the repair.

The construction question remains open. No integral model or physical
167-row cover was sought in this diagnostic.

## 5. Provenance

The run took0.350761 seconds on arboghast through ssh h100, including
imports, both independent literal repair censuses, one105-variable LP,
and exact certificates for all45 histogram constraints. It used two-CPU
affinity,1GiB memory cap and a three-second outer timeout.

- q3_d8_fixed_repair_short_histogram_gate_20260908.py
- Q3_D8_FIXED_REPAIR_SHORT_HISTOGRAM_CERTIFICATE_20260908.json
- Q3_D8_FIXED_REPAIR_SHORT_HISTOGRAM_SUMMARY_20260908.json

The full saved certificate contains both literal repair unions, all45
residual demands, every integer column, and the exact primal coverage
vector. See Q3_D8_FOUR_ROW_EXTREMAL_REPAIR_AND_SHORT_GATE_20260908.md for
appendix-a's independent analytical repair construction.
