# Repairing a partial binary-ten macro cover by actual small boxes

This note proves an analytic repair theorem. It does **not** exhibit a new 42-row near-cover and therefore does not claim a new unconditional coefficient. It also records why the retained frozen involution models do not admit a meaningful one-hole relaxation.

## 1. Literal macro object and transfer theorem

A binary-ten prefix row consists of two ordered disjoint five-tuples partitioning the ten coordinates. Its 36 targets are all unions of a prefix on each shore. Let a bank of `m` such rows cover every binary pattern except a set `H`.

Partition each of ten actual coordinate chains of length `2s` into its low and high halves. A missed binary pattern lifts to exactly one translated copy of `[s]^10`. Translations here mean restriction to the indicated actual chain segments; the physical coordinate supports are unchanged.

Every full prefix row lifts to two five-axis staircases. Each staircase has membership `6s^5` and an actual partition into `s^4` ascending chains by the hook construction. Thus its paired principal charge is `12s^9`.

Suppose additional actual paired chain families cover the missed boxes, with total principal charge

\[
 (R+o(1))s^9.
\]

Then the existing literal bridge/Euler compiler and eleven-accumulator transfer give

\[
 \boxed{\limsup_{k\to\infty}\frac{\nu(k)}{W(k)}
 \le\frac{12m+R}{512}\,\beta_{11},\qquad
 \beta_{11}=\sqrt{\pi/8}\,\mathbb E\sqrt{S_{11}}.}
\]

Here `S_11` is the sum of eleven independent unit-ball exit times of three-dimensional Brownian motion. The hypotheses concern one common, literal macro bank and its actual missed boxes; distinct repaired groups may overlap.

For completeness, each repaired left/right family below comes with an actual chain partition, not merely a rank-count bound. Pairing every left chain with every right chain gives a complete bipartite bridge graph. Its principal length is `left membership * right chain count + right membership * left chain count`; endpoints cost only `O(s^8)` and the finitely many closing components cost `O(s)`. The shortest eleventh accumulator is absorbed by product SCD, multiplying the principal upper bound by its length, which cancels in the volume normalization. Fixed-dimensional padding, the fallback compiler, reciprocal integrability, and all-dimension passage are exactly the same as in the proved finite-template transfer. Repairs also supply the full complements through the reverse bridge arcs. No target is repaired merely by an occurrence-count claim.

## 2. A single missed box

Let `w_5(s)` be the width of `[s]^5`. The standard iterated product SCD realizes this width as the number of ascending chains. Its central rank formula gives

\[
 w_5(s)=\rho_5s^4+O(s^3),\qquad
 \rho_5=\frac{(5/2)^4-5(3/2)^4+10(1/2)^4}{24}
       =\frac{115}{192}.
\]

Split a missed `[s]^10` box into two five-axis boxes and use their SCDs. Its **exact** principal charge is `2s^5 w_5(s)`, so one missed cell has repair charge

\[
 \boxed{R_1=2\rho_5=\frac{115}{96}.}
\]

In particular a 42-row bank with at most one missed binary target would give

\[
 \boxed{c\le\frac{48499}{49152}\beta_{11}
 <1.178728<1.1807038038.}
\]

The last strict numerical inequality is certified in Section 5. This finite antecedent is weaker than the old exact 42-row covering gate. It remains unconstructed in the inspected artifacts.

Repairing `h` arbitrary cells separately gives the valid ledger

\[
 R\le\frac{115h}{96}.
\]

At `h=2`, this particular upper-bound ledger gives coefficient `1.181522620122...`, already above the current record. That is a limitation of this repair strategy, not a lower bound excluding other repairs.

## 3. Grouping two comparable missed cells

Suppose the two missed bit patterns satisfy `a < b` coordinatewise and differ in exactly `h` coordinates, where `1<=h<=5`. Put all changing coordinates on one five-axis shore, adding `5-h` unchanged coordinates to that shore. The opposite five-axis shore is the same microcube in both cells.

The changing shore is order-isomorphic to

\[
 L_{h,s}=([s]^h\oplus[s]^h)\times[s]^{5-h},
\]

where `oplus` is ordinal sum. Its membership is `2s^5`; the opposite shore has membership `s^5` and chain count `w_5(s)`.

Here is an explicit chain partition of `L_(h,s)`. Take an SCD of `[s]^h`; if a chain has length `lambda`, glue its two corresponding copies in the ordinal sum to obtain a chain of length `2lambda`. This gluing is valid because all changing coordinates of the first box are below all changing coordinates of the second. Take an SCD of `[s]^(5-h)`, with chain lengths `mu`. For every resulting pair apply the two-chain product SCD, using `min(2lambda,mu)` chains. Thus an actual partition has

\[
 R_h(s)=\sum_{\lambda,\mu} n_{h,s}(\lambda)
 n_{5-h,s}(\mu)\min(2\lambda,\mu)
\]

chains, where `n_(d,s)(lambda)` is the SCD multiplicity. For `d=0`, use one singleton chain. Hence the exact paired principal charge is

\[
 \boxed{2s^5w_5(s)+s^5R_h(s).}
\]

The resulting asymptotic charges are

| Changed coordinates `h` | `R_h(s)/s^4 -> delta_h` | Repair charge `2rho_5+delta_h` | Certified coefficient upper bound for 42 rows |
| --- | --- | --- | --- |
| 1 | `11/12` | `203/96` | Does not beat the record by this ledger |
| 2 | `51/64` | `383/192` | `<1.180587` |
| 3 | `17/24` | `61/32` | `<1.180381` |
| 4 | `995/1536` | `945/512` | `<1.180240` |
| 5 | `115/192` | `115/64` | `<1.180126` |

These are constructive chain-partition upper bounds; no assertion of optimal width is required.

**Updated repair scope.** The five/five restriction in this section is unnecessary for added repair families. The root-audited [flexible-shore repair note](TWO_MACROCELL_MONOTONE_REPAIR_GEOMETRY_20260908.md) puts all changing axes on one shore and proves below-budget repairs for every comparable pair at Hamming distance 1 through 7. In particular, distance one has charge `1+2rho_9<2`, so the earlier distance-one entry above is only a limitation of this particular five/five ledger, not the best current repair.

### Evaluation of the five constants

Write `f_d` for the density of the sum of `d` independent uniforms on `[0,1]`. For `d>=2`,

\[
 f_d(x)=\frac1{(d-1)!}\sum_{j=0}^d(-1)^j\binom dj(x-j)_+^{d-1},
\]

and `f_1=1` on `(0,1)`. In an SCD, the number of chains with length at least `us` is the rank count at distance approximately `us/2` below the middle. The exact bounded-composition formula therefore gives its leading term `s^(d-1) f_d((d-u)/2)`. Applying

\[
 \min(2\lambda,\mu)=\int_0^\infty
 \mathbf1_{2\lambda\ge u}\mathbf1_{\mu\ge u}\,du
\]

to the preceding actual partition gives, for `1<=h<=4`,

\[
 \delta_h=\int_0^{\min(2h,5-h)}
 f_h\left(\frac h2-\frac u4\right)
 f_{5-h}\left(\frac{5-h-u}{2}\right)du.
\]

The finite-rank composition formulas yield `R_h(s)=delta_h s^4+O(s^3)`; parity and endpoints affect only the error. The four integrals reduce to

\[
\begin{aligned}
 \delta_1&=\int_0^2(2/3-u^2/4+u^3/16)du=11/12,\\
 \delta_2&=\int_0^1(1-u/4)(3/4-u^2/4)du
 +\int_1^3(1-u/4)(3-u)^2/8\,du=51/64,\\
 \delta_3&=\int_0^2(3/4-u^2/16)(1-u/2)du=17/24,\\
 \delta_4&=\int_0^1(2/3-u^2/16+u^3/128)du=995/1536.
\end{aligned}
\]

For `h=5`, the two SCD copies glue directly, so `R_5(s)=w_5(s)` and `delta_5=rho_5`.

The comparability hypothesis is essential for this ordinal-sum construction. Two different equal-rank targets are incomparable, so this lemma does not apply to them. In particular a nonfixed involution orbit consists of two equal-rank targets and is not covered by the improvement in this section.

## 4. General grouped-box ledger

For each repair group choose a five/five coordinate split and macro shore supports `C_j,D_j` such that their Cartesian products cover all missed bit patterns. Covering additional, already-covered patterns is harmless. Suppose the corresponding microcell unions have actual chain partitions with

\[
 |\mathcal T_s(C_j)|=|C_j|s^5,\quad
 |\mathcal T_s(D_j)|=|D_j|s^5,
\]

and chain counts at most `(rho(C_j)+o(1))s^4` and `(rho(D_j)+o(1))s^4`. The grouped repair charge is then

\[
 \boxed{R\le\sum_j\bigl(|C_j|\rho(D_j)+|D_j|\rho(C_j)\bigr).}
\]

The singleton and comparable-pair constructions above are instances. Axis-aligned groups can alternatively be enclosed in rectangular boxes whose side lengths are `s` or `2s`; an iterated product SCD gives their exact central-rank chain count. Arbitrary arrangements may require another explicit partition or a finite comparability-matching certificate. Rank polynomials alone do not certify an upper bound on chain count.

For a 42-row bank, the available repair budget against the existing `c_9` is exactly

\[
 R<512c_9/\beta_{11}-504=2.0448919776\ldots.
\]

## 5. Exact clock evaluation and rational certificates

The same Laplace-transform argument as Appendix A.7 gives

\[
 \beta_{11}=\frac12\int_0^\infty
 \left(x^{-2}-x^9\operatorname{csch}^{11}x\right)dx.
\]

Writing `D=d/dx`, the elementary recurrence for derivatives of powers of `csch` gives

\[
 \operatorname{csch}^{11}x=
 \frac{D^{10}-165D^8+8778D^6-172810D^4+1057221D^2-893025}{10!}
 \operatorname{csch}x.
\]

Integrate against `x^9` on `[epsilon,infinity)`. The highest derivative supplies the cancelling `1/epsilon`; the other boundary terms vanish, and the odd Laurent expansion has no finite boundary constant. The remaining moments are `J_1=pi^2/4`, `J_3=pi^4/8`, `J_5=pi^6/4`, `J_7=17pi^8/16`, and `J_9=31pi^10/4`. The last follows from `J_9=2*9!*(1-2^-10) zeta(10)` and `zeta(10)=pi^10/93555`. For a direct extension of A.7's Parseval proof, the sine coefficients of `x^5` on `[-pi,pi]` are `2(-1)^(n+1)(pi^4/n-20pi^2/n^3+120/n^5)`; Parseval together with the already evaluated lower even zeta values gives this tenth-order value.

Substitution proves

\[
 \boxed{\beta_{11}=\frac{33}{16}\pi^2-\frac{1463}{160}\pi^4
 +\frac{17281}{960}\pi^6-\frac{1996973}{179200}\pi^8
 +\frac{1953}{2048}\pi^{10}.}
\]

The following exact-rational certificate was executed only through `ssh h100`. It proves the numerical upper bounds above without floating-point quadrature.

```python
from fractions import Fraction as F

def atan_interval(q):
    lo = sum((F((-1)**j, (2*j+1)*q**(2*j+1))
              for j in range(40)), F(0))
    return lo, lo + F(1, 81*q**81)

al, au = atan_interval(5)
bl, bu = atan_interval(239)
pl, pu = 16*al - 4*bu, 16*au - 4*bl
coef = {2:F(33,16), 4:-F(1463,160), 6:F(17281,960),
        8:-F(1996973,179200), 10:F(1953,2048)}
lower = sum(v*(pl**i if v >= 0 else pu**i) for i,v in coef.items())
upper = sum(v*(pu**i if v >= 0 else pl**i) for i,v in coef.items())
assert F(1194598260259498,10**15) < lower <= upper
assert upper < F(1194598260259499,10**15)
for cost, cap in [(F(48499,96),F(1178728,10**6)),
                  (F(97151,192),F(1180587,10**6)),
                  (F(16189,32),F(1180381,10**6)),
                  (F(258993,512),F(1180240,10**6)),
                  (F(32371,64),F(1180126,10**6))]:
    assert cost*upper/512 < cap < F(11807038038,10**10)
```

For orientation, the exact expressions give full-42-row coefficient `1.175932662442944...` and one-hole coefficient `1.178727641282662...`.

## 6. Inspection of the retained binary-ten candidates

The local binary-ten notes and the durable directory `/home/amodo/or-research-20260907-QiqXT3` on h100 were inspected. The retained involution work has ten-row fixed cores, rational fractional completions, and bounded integer tests with `UNKNOWN` or `INFEASIBLE` status. It contains no retrieved literal 42-row near-cover whose all-cube hole count can be used here. Numerical primals and compatible partial hints are not 42-row banks.

The recoverable canonical MSW 42-row bank has the recorded all-rank inventory of 118 holes, including 54 at rank four, in `CATALAN_THRESHOLD_EIGHT_COVER_AND_TRANSFER_20260906_c58e2.md`. This is the available documented bank, not a claim of global optimality among 42-row near-covers. Older parameter-five Catalan forests and cyclic wreath certificates do not automatically define two ordered five-tuples per row; they cannot be substituted into this macro compiler without checking the literal object.

### Why no one-hole solver retry was launched

Let `tau` exchange coordinate `i` with `i+5`. Any completed bank in the retained model is tau-invariant. Its holes are therefore unions of tau-orbits. A one-hole bank can miss only a tau-fixed target, namely a union of coordinate pairs.

Every inspected literal frozen core already covers all 32 tau-fixed targets. This was directly verified on h100 for all 24 distinct saved cores in the index-2/index-29 primals and saved phase primals. The first pair-label orientation is regular, hence every pair label occurs first and all five fixed rank-two targets are covered. The tight fixed ranks four and six are covered by construction. Every inspected last-label assignment uses every label, hence all fixed rank-eight targets are covered; empty and full targets occur in every row. Index 2 has last-label multiplicities `2,2,1,2,3`, while the other retained cores have `2,2,2,2,2`; all are positive.

Consequently, for these frozen models, allowing at most one uncovered target is **exactly the same constraint as full coverage**. A requested bounded relaxed retry would be redundant, so no such solver was launched. A nonfixed two-target orbit has equal-rank, incomparable members and does not meet Section 3's hypothesis. A different core/symmetry, an unrestricted near-cover, or a cheaper repair for an incomparable orbit would be needed for a new finite search target.

All calculations in this note, including the exact rational clock certificate and finite SCD-partition checks, were performed through `ssh h100`. Local activity was limited to reading and writing proof artifacts.
