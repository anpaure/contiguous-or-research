# Exact rotation-period census of the construction through dimension 101

2026-09-08. One independent deterministic h100 census by `exact_b_finite_frontier`. The exact period and signature-count proof was separately audited by `exact_b_induction`; that agent also read the complete census source and found no code correction necessary. No enormous literal word was generated, and no construction parameter, cut, or ordering was optimized.

**Result: all supplied numerical claims pass.** The census checks every odd dimension 3 through 101, 1,295,970 peak-count partitions and 1,702,866 least-row-period signatures. It reproduces all quoted entries and all individually claimed odd/even percentage bounds.

## 1. What was counted

The exact theorem and counting interface are proved in
[the translated-return/signature audit](PBBS_EXACT_TRANSLATED_RETURN_PERIOD_AND_SIGNATURE_MULTIPLICITY_AUDIT_20260908.md), which was read for this task.

For n=2r+1, enumerate each nonincreasing positive peak-count partition

\[
m_0\ge m_1\ge\cdots\ge m_{h-1}>0,\qquad\sum_s m_s=r,
\]

once. Here h is the **length** of this peak-count partition. Put m_h=0 and

\[
n_s=1+2\sum_{j\ge s}m_j,\quad
\ell_s=m_s-m_{s+1},\quad p_s=n_{s+1}.
\]

For every d dividing p, the exact number of p-entry weak-composition rows of mass ell with period dividing d is

\[
F_{p,\ell}(d)=
\begin{cases}
\binom{\ell/(p/d)+d-1}{d-1},&p/d\mid\ell,\\
0,&\text{otherwise}.
\end{cases}
\]

Subtracting the proper-divisor counts gives the least-period count chi(d). The program checks all chi are nonnegative and their sum equals the full weak-composition count. A zero row has just the one least-period-one realization; the one-slot terminal row is treated directly by the same formula.

For each positive-multiplicity signature `(d_0,...,d_(h-1))`, let

\[
a=\prod_s\chi_s(d_s),\quad
\sigma_j=\sum_{s<j}\frac1{n_sn_{s+1}},\quad
v=\operatorname{lcm}_{1\le j\le h}
\operatorname{den}\left(\frac{n_j}{d_{j-1}}\sigma_j\right).
\]

The signature contains exactly a normalized Dyck roots and na physical states. The theorem proves v is their common physical f period, is odd, and is also their f² period. Thus its cycle count is exactly na/v.

The program checks na is divisible by v for **every separate signature**, not just after merging signatures with the same numerical period. Rows with one possible least period are factored into a base product/lcm; every Cartesian choice of all other rows remains separately enumerated.

Reduced rational sigma values are updated with integer numerator/denominator arithmetic. If sigma has reduced denominator q, then

\[
\operatorname{den}(e\sigma)=q/\gcd(q,e),
\]

which is used to avoid any floating-point period calculation.

Finally the exact overhead and construction length are

\[
C_n=\sum_{\rm signatures}(2h-1)\frac{na}{v},
\qquad N_n=W(n)+C_n.
\]

This counts the previously proved height-adaptive construction. It does not identify its length with ν(n).

## 2. Exhaustive consistency checks

At every dimension the run verifies:

- the signature masses of each profile sum to the independent product of its full weak-composition row counts;
- the sum over all roots is Catalan_r;
- n times that sum equals the central-binomial width W(n);
- every signature's physical-state count is an integral number of its exact cycles;
- all computed periods are odd and multiples of n;
- the period histogram weighted by period totals exactly W(n);
- the height histogram gives the same collar charge as the direct signature sum;
- `C_n=2 sum_C h_C - number_of_cycles`.

The mixed-symmetry example `(n_s)=(17,9,7,5,3,1)` is reproduced exactly: 162 roots give 18 cycles of period 153, and three roots give one cycle of period 51.

Two independent earlier literal constructions supply additional checks:

| Dimension | Cycles | Sum of component heights | Overhead | Full-collar length |
|---:|---:|---:|---:|---:|
| 17 | 146 | 519 | 892 | 25,202 |
| 19 | 360 | 1,384 | 2,408 | 94,786 |

These are exactly the canonical-cycle counts already obtained by directly traversing the physical map and constructing their source words. Existing repaired or externally supplied shorter words at those dimensions are separate and remain better finite upper bounds.

## 3. Quoted entries and requested construction values

All five quoted `(n,W,C_n)` entries agree exactly:

| n | W(n) | C_n | N_n |
|---:|---:|---:|---:|
| 17 | 24,310 | 892 | 25,202 |
| 31 | 300,540,195 | 1,355,845 | 301,896,040 |
| 41 | 269,128,937,220 | 327,229,518 | 269,456,166,738 |
| 61 | 232,714,176,627,630,544 | 33,239,463,842,328 | 232,747,416,091,472,872 |
| 101 | 199,804,427,433,372,226,016,001,220,056 | 1,187,277,484,185,535,019,897,550 | 199,805,614,710,856,411,551,021,117,606 |

The additional requested finite and threshold-boundary entries are:

| n | W(n) | C_n | N_n |
|---:|---:|---:|---:|
| 21 | 352,716 | 10,138 | 362,854 |
| 27 | 20,058,300 | 275,546 | 20,333,846 |
| 29 | 77,558,760 | 460,924 | 78,019,684 |
| 55 | 3,824,345,300,380,220 | 4,125,976,139,518 | 3,828,471,276,519,738 |
| 57 | 15,033,633,249,770,520 | 12,242,529,530,870 | 15,045,875,779,301,390 |
| 85 | 3,318,776,542,511,877,736,535,400 | 340,093,568,810,237,002,094 | 3,319,116,636,080,687,973,537,494 |
| 87 | 13,124,252,690,842,425,594,480,900 | 1,056,919,952,743,771,726,896 | 13,125,309,610,795,169,366,207,796 |

No decimal approximations are used to certify these integers.

## 4. The exact dimension-101 lower/upper comparison

There are 204,226 profiles and 271,728 least-period signatures at n=101. Their cycle count is

\[
60,824,931,090,531,194,200,072.
\]

The central-rank endpoint formula in the master handoff gives delay seven, checked by its two defining integer inequalities. Thus

\[
\begin{aligned}
B(101)&=199,804,427,433,372,226,016,001,220,063,\\
N_{101}-B(101)&=1,187,277,484,185,535,019,897,543.
\end{aligned}
\]

The exact relative overhead has the outward enclosure

\[
0.000005942198075572927182732101
\le\frac{C_{101}}{W(101)}
<0.000005942198075572927182732102.
\]

The endpoints are rationals with denominator 10^{30}. In particular

\[
N_{101}<1.000006\,W(101).
\]

So the construction is about 5.9422 parts per million above the width. That small relative overhead still corresponds to the enormous additive gap above B(101) displayed above; the census does not solve the exact optimum.

## 5. Every claimed finite percentage case, including both parities

The run checks integer inequalities `q*(N-W)<W`, separately for every requested k. For even k it uses the actual established doubling lift from odd k−1 and verifies `W(k)=2W(k-1)` exactly.

All requested cases pass:

\[
\begin{aligned}
\nu(k)&<1.01W(k)&&29\le k\le102,\\
\nu(k)&<1.001W(k)&&57\le k\le102,\\
\nu(k)&<1.0001W(k)&&87\le k\le102.
\end{aligned}
\]

These are finite checks, not a monotonicity inference. The preceding odd dimensions 27, 55, and 85 fail the corresponding strict construction-ratio test, respectively. The report retains the exact signed margins for those boundary cases and every successful individual case. No conclusion beyond k=102 is inferred from this census alone.

## 6. Artifacts and resource record

- [Independent executable census](census_pbbs_exact_rotation_period_partitions_20260908.py).
- [Complete exact report](rotation_period_census_20260908/exact_rotation_period_census.json), including every dimension, period/height histograms, exact endpoint bounds and every odd/even percentage case.
- [Requested plain-number extracts](rotation_period_census_20260908/requested_plain_numbers.json).
- [Exact period and counting proof](PBBS_EXACT_TRANSLATED_RETURN_PERIOD_AND_SIGNATURE_MULTIPLICITY_AUDIT_20260908.md).
- [User-claim transcription used for the comparison](ROTATION_PERIOD_ADVANCE_USER_CLAIMS_20260908.md).

The remote program is `/home/amodo/census_pbbs_exact_rotation_period_partitions_20260908.py`; output directory `/home/amodo/exact-b-rotation-period-census-20260908/`.

The one run enforced 300 CPU seconds, 360 wall seconds and 4 GiB address space, returning PASS in approximately 26.83 seconds. All mathematical operations are integer arithmetic, exact rational reductions, and combinatorial enumeration. Floating point is used only for elapsed-time metadata. No mathematical process remains running.

The complete report SHA-256 is

`43b52c9d3ed72b9901dc7c6aca96a4ce8f46a12e322fc01c181da1a3412869b2`.

This is an independently implemented finite census backed by internal proof and source review. It does not claim external or proof-assistant certification, and it does not claim literal interval scans of words whose lengths are the enormous numbers above.
