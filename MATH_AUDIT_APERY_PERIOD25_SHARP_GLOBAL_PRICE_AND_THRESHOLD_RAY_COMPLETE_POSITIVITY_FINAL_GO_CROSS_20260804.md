# Independent audit: period-twenty-five sharp-price threshold-ray closure

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_APERY_PERIOD25_SHARP_GLOBAL_PRICE_AND_THRESHOLD_RAY_COMPLETE_POSITIVITY_20260804.md`  
**Target SHA-256:**
`61265fdf0e355aae0c6c786f9725ee639a427a1efb866fa21191ccb7b575653a`  
**Verdict:** **FINAL GO.**  The result is valid with its stated formal
exact-first-carry scope.

This audit is independent of the theorem's self-audit.  It uses exact
rational inequalities only; no search or sampled numerical computation is
part of the proof.

## 1. Lineage gate

The requested earlier SHA prefix `1c1acead` and the intermediate SHA
prefix `ac693301` are rejected lineage.  The latter used the false order

\[
 {7\over25}>{2\over7}.
\]

The authoritative theorem repairs that branch with

\[
 {7\over25}>{6\over23},
\]

and the frozen six-twenty-thirds anchor.  This audit binds only the exact
successor SHA displayed above.

## 2. Global price (f<533/10000)

The Jacobi split is correct:

\[
 f(x)=1-\Theta(x)+H(x)+R(x),
\]

where `H` consists of the `j=0,2` Gaussian terms and `R` begins at
`j=3`.  At an interior critical point of `H`,

\[
 \log{2-t\over t}=\pi(1-t),
 \qquad
 H(t)={2\over2-t}e^{-\pi t^2/4}.
\]

At `t_0=589/5000`, the degree-ten positive exponential polynomial already
proves

\[
 e^{(333/106)(1-t_0)}>{9411\over589}.
\]

The critical ratio is decreasing in the relevant interval, so the
direction `t_*<t_0` is correct.  Also

\[
 {d\over dt}\log\left({2\over2-t}e^{-\pi t^2/4}\right)
 ={1\over2-t}-{\pi t\over2}>0
 \qquad(0\le t\le t_0),
\]

so the critical envelope is used in the correct direction.

The number

\[
 z_0={115524693\over10600000000}
     ={333\over106}{t_0^2\over4}
     <{\pi t_0^2\over4}
\]

is exact.  Direct positive-denominator cross multiplication verifies

\[
 {10000\over9411}left(1-z_0+{z_0^2\over2}\right)
 <{10511\over10000}.
\]

The degree-eighteen positive exponential polynomial verifies

\[
 e^{16317/2650}>{25000\over53}.
\]

The first residual term is therefore below `53/25000`; the successive
ratio is below `1/100` because its smallest exponent gap is
`33*pi/20`.  Hence

\[
 R(x)<{53\over24750}.
\]

Finally,

\[
 {10511\over10000}-1+{53\over24750}+{1\over20000}
 <{533\over10000}.
\]

On `[1/5,1/2]`, the frozen inequality
`f(1/5)<101/2000` and frozen decrease from one fifth are stronger.  Thus
the global bound (1.9) is valid on the whole half interval.

## 3. Fixed-threshold monotonicity

At `x_0=4/25`, the first two positive/adverse derivative ratios are
exactly

\[
 {29\over21}e^{-4\pi/25},
 \qquad
 {18\over7}e^{-99\pi/100}.
\]

The first successor ratio is exactly

\[
 {79\over54}e^{-133\pi/100}.
\]

Exact positive Taylor lower bounds give, respectively,

\[
 R_1<{17\over20},
 \qquad R_2<{3\over25},
 \qquad {79\over54}e^{-133\pi/100}<{1\over30}.
\]

Every later successor ratio is smaller.  Therefore the complete ratio is

\[
 {17\over20}+{3/25\over1-1/30}
 ={113\over116}<1.
\]

For the ratio with positive argument `q+1+x`,

\[
 {d\over dx}\log R_q(x)
 ={1\over q+1+x}+{1\over1-x}-{\pi\over2}(q+2).
\]

For `q=0` this is at most `8/3-pi<0`; for `q>=1` the standard
`5/2-3pi/2<0` bound applies.  Thus each ratio decreases throughout
`[4/25,1/2]`, and the claimed strict monotonicity has no interval gap.

## 4. Literal anchor audit

For every retained Gaussian, replacing `pi` by `355/113` gives an upper
bound on its positive exponent.  Substitution in the exact majorant

\[
 U_{24}(z)=\sum_{j=0}^{23}{z^j\over j!}
 +{z^{24}\over24!(1-z/25)}
\]

was independently cross-multiplied.  All twelve arguments are below 25,
and all twelve reciprocal inequalities have the direction used in the
theorem.

The resulting lower Gaussian numerators are:

\[
\begin{array}{c|rrrr|r}
x&\multicolumn{4}{c|}{\text{lower numerators over }100000}&\text{sum}\\ \hline
4/25&57454&34754&2561&39&94808\\
1/5&60491&32271&2233&32&95027\\
6/25&63530&29890&1943&26&95389.
\end{array}
\]

Therefore

\[
 f(4/25)<{5192\over100000}={649\over12500},
\]

\[
 f(1/5)<{4973\over100000},
 \qquad
 f(6/25)<{4611\over100000}.
\]

The omitted Gaussian tail is adverse, so retaining only four terms gives
an upper bound on `f`, as required.

## 5. Base and short-ray ledgers

The exact first-five base is

\[
\begin{aligned}
6L-3G_{25}-V_4-V_5-6\varepsilon
&={264144-159900-51920-49730-300\over10^6}\\
&={2294\over10^6}>0.
\end{aligned}
\]

The corresponding lower numerators for ray depths `u=0,1,2,3,4,5` are

\[
43974, 34648, 25322, 15996, 8050, 2294,
\]

so the unexpanded statement that all shorter ledgers are stronger is
correct.  Ray disjointness gives `u+1<25-u`, hence `u<=11`, and the
terminal-suffix envelope gives `Y_i>i/25`.

## 6. Ordered cases and the tight margin

If `X_6>=4/25`, monotonicity makes its compact difference nonnegative;
only one theta allowance remains.  Every later `Y_i` is beyond one
quarter.  The margin is

\[
 {2294-50\over10^6}={2244\over10^6}.
\]

If `X_6<4/25`, then `Y_6>6/25`, giving

\[
 L-V_6-\varepsilon=-{2136\over10^6}.
\]

Crossing at pair seven therefore leaves

\[
 {2294-2136\over10^6}
 ={158\over10^6}>0.
\]

If pair seven also remains left of the threshold, the corrected order

\[
 {7\over25}>{6\over23}
\]

gives the exact credit

\[
 L-{4379\over100000}={234\over10^6}>0.
\]

The later comparisons are also in the correct order:

\[
 {8\over25}>{2\over7},
 \qquad
 {9\over25}>{1\over3}.
\]

They give credits `3194/10^6` and `2009/375000`.  At most two generic
quarter costs remain.  The fully un-crossed branch is

\[
 {2294-2136+234+3194-2(1136)\over10^6}
 +{2009\over375000}
 ={10007\over1500000}>0.
\]

Every earlier termination is stronger.  Thus the smallest displayed
margin really is

\[
                         {158\over10^6}.
\]

## 7. Scope verdict

The reflected-ray identity, the nonnegative middle train, and the exact
endpoint comparison then prove

\[
 \Phi(W)>0
\]

for every honest exact-first-carry formal cyclic Apéry clock of period
twenty-five.  The theorem does not cover overshoot, later first crossing,
finite physical shoulders, arbitrary Bellman clocks, or OR words.

**FINAL GO** for the exact SHA audited above.
