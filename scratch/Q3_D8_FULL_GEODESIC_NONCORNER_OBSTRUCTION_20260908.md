# Full ternary eight-axis rows need at least 149 rectangles

2026-09-08. Pure proof plus one bounded exact h100 certificate. Author:
direct_route. Root full-file analytical review passed. Appendix_a independently
read and passed the full analytic argument, including the general
unequal-full-split extension; that audit did not rerun the saved finite
primal certificate. This note excludes **full
geodesic** rows. It does not exclude truncated or general q-ary chains.

## 1. The elementary obstruction

Work in \(\{0,1,2\}^8\). A full geodesic four-axis chain runs from
\((0,0,0,0)\) to \((2,2,2,2)\), increasing one coordinate by one at
each step. It has nine members, one at every rank from zero through
eight. A full balanced row is a product of two such chains on disjoint
four-axis supports. Its charge is eighteen and it has 81 targets.

The rank polynomial of every row is
\[
                            (1+x+\cdots+x^8)^2.
\]
Its rank counts are \(1,2,\ldots,9,\ldots,2,1\). The entire cube's
rank counts, from rank zero to rank sixteen, are
\[
 1,8,36,112,266,504,784,1016,1107,1016,784,504,266,112,36,8,1.        \tag{1}
\]
Thus the strongest inequality using only a weighted sum of whole ranks
is 127 rows, from ranks seven or nine: \(1016/8=127\). Any nonnegative
combination of rank inequalities has ratio at most the maximum of their
individual ratios, so it cannot improve this bound.

The decisive class is the central rank with the binary corners removed.
There are 1107 rank-eight targets, of which \(\binom84=70\) use only
zero and two. Let
\[
        F=\{x\in\{0,1,2\}^8:\sum_i x_i=8,
                                      \text{some }x_i=1\}.
\]
Then \(|F|=1037\). A full row has nine central cells, indexed by
shore ranks \((i,8-i)\), \(0\le i\le8\). The two extreme cells
\((0,8)\) and \((8,0)\) are binary corners. Consequently every row
contains at most seven members of \(F\), even if other central cells
are also corners. Any cover by \(N\) full balanced rows obeys
\[
                     7N\ge1037,
                \qquad N\ge\left\lceil\frac{1037}{7}\right\rceil
                         =149.                                    \tag{2}
\]
This applies with arbitrary overlaps. In particular the proposed gate
\(N\le132\) is impossible in this row class.

The same obstruction also covers other full proper support splits in
this particular ternary eight-axis problem. If the smaller shore has
\(p\le3\) axes, the row has at most \(2p+1\le7\) cells at rank eight,
and hence at most seven in \(F\). Every full split still has charge
eighteen. Thus allowing a full one-by-seven, two-by-six, or three-by-five
row does not evade (2).

## 2. Exact histogram dual and complete fractional optimum

A coordinate histogram is \((n_0,n_1,n_2)\), with sum eight. The four
noncorner central histograms and their orbit sizes are

| Histogram | Number of targets | Weight per target |
|:--|--:|--:|
| \((0,8,0)\) | 1 | \(1/7\) |
| \((1,6,1)\) | 56 | \(1/7\) |
| \((2,4,2)\) | 420 | \(1/7\) |
| \((3,2,3)\) | 560 | \(1/7\) |

All other target weights are zero. Each full balanced row has total
weight at most one, and the total target weight is \(1037/7\).
This is the exact dual behind (2).

For completeness, the authorized histogram diagnostic found a matching
fractional primal of \(1037/7\) rows. No integral cover is inferred.
To describe the complete finite catalogue, let \(h_r\) be the number
of coordinates equal to one after step \(r\) on a shore. The sequence
\(h_0,\ldots,h_8\) is a Dyck path of semilength four: opening a fresh
coordinate increases it, and changing one to two decreases it. Conversely
every one of the fourteen such paths is realizable. Its shore histogram
at rank \(r\) is
\[
                 \left(4-\frac{r+h_r}{2},\ h_r,
                                      \frac{r-h_r}{2}\right).       \tag{3}
\]
Thus every full balanced row has one of 105 unordered pairs of shore
histogram paths. There are 45 target histograms. Summing the 81 pairs
of shore states gives the exact integer incidence matrix for this
105-type, 45-orbit fractional-cover problem.

The eight shore types used by the exact primal are listed with their
indices in the saved complete catalogue:

| Type | Height sequence \(h_0\ldots h_8\) |
|--:|:--|
| 0 | \(0,1,2,3,4,3,2,1,0\) |
| 1 | \(0,1,2,3,2,3,2,1,0\) |
| 2 | \(0,1,2,3,2,1,2,1,0\) |
| 3 | \(0,1,2,3,2,1,0,1,0\) |
| 4 | \(0,1,2,1,2,3,2,1,0\) |
| 7 | \(0,1,2,1,0,1,2,1,0\) |
| 11 | \(0,1,0,1,2,1,0,1,0\) |
| 12 | \(0,1,0,1,0,1,2,1,0\) |

For each pair below take any physical representative and average it
uniformly over all eight-coordinate permutations. The indicated weight
is the **total row weight**, not the weight of each developed copy.

| Shore-type pair | Total fractional row weight |
|:--|--:|
| \((0,0)\) | \(1\) |
| \((0,1)\) | \(6\) |
| \((0,11)\) | \(106/21\) |
| \((1,1)\) | \(325/21\) |
| \((1,7)\) | \(19/6\) |
| \((2,3)\) | \(1070/21\) |
| \((2,12)\) | \(2167/42\) |
| \((4,12)\) | \(313/21\) |

The exact verifier checks that their weighted histogram counts dominate
all 45 orbit sizes and that their total is \(1037/7\). Coordinate
permutation symmetry turns these histogram inequalities into a
fractional cover of every individual target. The matching lower
certificate therefore proves that the complete histogram relaxation,
equivalently the full coordinate-symmetric fractional-cover problem
for balanced full geodesics, has optimum exactly
\[
                              1037/7.                              \tag{4}
\]

## 3. General full balanced q-ary inequality

Let \(q\ge2\), \(d=2m\), and \(m(q-1)>1\). Consider products of
two full geodesics on disjoint \(m\)-axis supports in
\(\{0,\ldots,q-1\}^{2m}\). Each shore has \(m(q-1)+1\) members,
and each row has that many central-rank cells at rank \(m(q-1)\).
Its two extreme cells are binary corners using only zero and \(q-1\).
There are exactly \(\binom{2m}{m}\) such central corners in the whole
grid. If \(W_q(2m)\) denotes the central rank size, then every cover
by \(N\) full balanced rows satisfies
\[
       N\ge
       \left\lceil
       \frac{W_q(2m)-\binom{2m}{m}}{m(q-1)-1}
       \right\rceil.                                               \tag{5}
\]
The corresponding full-row charge is
\(2[m(q-1)+1]N\). If (5) already exceeds a proposed row budget,
there is no reason to search full balanced paths at those parameters.
Additional corner cells inside a row only strengthen the counting
argument. For \(q=2\) the numerator is zero and the inequality is
vacuous, as it should be.

For \(q\ge3\), (5) also holds for a bank of full proper support splits
of varying sizes. If the smaller support has \(p\le m-1\) axes, its
central-rank count is at most
\[
                 p(q-1)+1\le(m-1)(q-1)+1\le m(q-1)-1.
\]
Balanced rows have the same bound after the two corners are removed.
This extension still assumes that every shore is a **full** geodesic.

## 4. Verification, runtime, and limitations

The complete source is
`q3_d8_full_geodesic_histogram_gate_20260908.py`; its exact integer
matrix, rational primal, rational dual, and all results are saved in
`Q3_D8_FULL_GEODESIC_HISTOGRAM_GATE_20260908.json`.

The sole optimization call was the authorized 105-variable,
45-constraint fractional LP. Its floating output was rationalized and
then checked entirely with exact fractions. A separate physical-path
enumerator generated all 2520 actual four-axis geodesics, without using
the Dyck histogram formula, recovered precisely the fourteen histogram
paths, and independently verified the dual on all 105 pair types.
All 45 primal inequalities and exact zero primal-dual gap also passed.
The h100 mathematical runtime, including imports, was 0.374949 seconds;
the process had a five-second outer timeout. No integral search ran.

The exact command was

```text
ssh h100 'timeout 5s env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 - /tmp/q3_d8_full_geodesic_histogram_gate_20260908_direct_route.json' < scratch/q3_d8_full_geodesic_histogram_gate_20260908.py
```

The obstruction does **not** apply unchanged to general q-ary chain
rectangles. For example, deleting both endpoints from both ternary
four-axis chains reduces the charge from eighteen to fourteen while
retaining the seven interior central cells. Other targets are lost, so
this is not itself a cover, but it explains why full-row waste cannot
be charged to arbitrary truncated rows. Neither the lower bound149 nor
the fractional primal above settles a general weighted ternary gate.
