# Period twenty-six: sharp overlap-depth closure and two residual threshold chambers

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It proves strict
formal Bellman positivity for every honest exact-first-carry period-twenty-six
cyclic Apéry clock of reflected overlap depth at most four, and for every
remaining ordered-ray chamber except two explicitly stated threshold
chambers.  On those chambers it gives exact nonnegative slack functionals
and the precise missing scalar credits.  It does **not** claim complete
period-twenty-six positivity.  No search, solver, sampled computation, or
numerical optimization is used.

Put

\[
A={\sqrt\pi\over2},\qquad
f(x)=F_A(Ax),\qquad C=F_A(0),\qquad g(x)=\rho(Ax),
\tag{0.1}
\]

and retain

\[
L={5503\over125000},\qquad
G={533\over10000},\qquad
Q={1129\over25000},\qquad
\varepsilon={1\over20000}.
\tag{0.2}
\]

Thus

\[
C>L,qquad f(x)<G\quad(0\le x\le1/2),
\tag{0.3}
\]

and on the compact quarter band one has the frozen floor, decrease, and
theta signs used below.  We also retain

\[
f(6/23)<{4379\over100000},\qquad
f(2/7)<{4083\over100000},\qquad
f(1/3)<{29\over750}.
\tag{0.4}
\]

## 1. A two-thirteenths monotonicity ray and three anchors

Let

\[
h(t)=t e^{-\pi t^2/4}.
\]

At `x_0=2/13`, the first two positive/adverse derivative ratios are

\[
R_1={15\over11}e^{-2\pi/13},
\qquad
R_2={28\over11}e^{-51\pi/52}.
\tag{1.1}
\]

Finite positive Taylor bounds using `pi>333/106` give

\[
R_1<{17\over20},
\qquad
R_2<{3\over25}.
\tag{1.2}
\]

Beginning with the successor of `h(28/13)`, every positive-term ratio is
below `1/30`; at the first argument this is

\[
{41\over28}e^{-69\pi/52}<{1\over30}.
\tag{1.3}
\]

Hence the complete positive/adverse ratio is below

\[
{17\over20}+{3/25\over1-1/30}
={113\over116}<1.
\tag{1.4}
\]

Every individual ratio decreases on `[2/13,1/2]`: for the first ratio use
`2/(1-x^2)<=8/3<pi`, and for every later ratio use
`5/2<3pi/2`.  Therefore

\[
\boxed{f'(x)<0\qquad(2/13\le x\le1/2).}
\tag{1.5}
\]

For `0<z<25`, put

\[
U_{24}(z)=\sum_{j=0}^{23}{z^j\over j!}
+{z^{24}\over24!\,(1-z/25)}.
\tag{1.6}
\]

Using `pi<355/113`, direct positive-denominator substitution in `U_24`
gives the following strict lower Gaussian ledgers.  The exact finite
comparisons are displayed so that every reciprocal direction is explicit.

At `2/13`, for the exponents

\[
{121\pi\over676},\quad {225\pi\over676},\quad
{196\pi\over169},\quad {1681\pi\over676},
\]

the lower numerators over `100000` are

\[
56980,\quad35140,\quad2610,\quad40.
\]

Indeed,

\[
\begin{aligned}
U_{24}(42955/76388)&<{100000\over56980},&
U_{24}(79875/76388)&<{100000\over35140},\\
U_{24}(69580/19097)&<{100000\over2610},&
U_{24}(596755/76388)&<{100000\over40}.
\end{aligned}
\tag{1.7a}
\]

Their sum is `94770`, and hence

\[
\boxed{f(2/13)<V_4:={523\over10000}.}
\tag{1.7}
\]

At `5/26`, the four exponents are

\[
{441\pi\over2704},\quad {961\pi\over2704},\quad
{3249\pi\over2704},\quad {6889\pi\over2704}.
\]

The corresponding lower numerators are

\[
59905,\quad32740,\quad2290,\quad33,
\]

with exact certificates

\[
\begin{aligned}
U_{24}(156555/305552)&<{100000\over59905},&
U_{24}(341155/305552)&<{100000\over32740},\\
U_{24}(1153395/305552)&<{100000\over2290},&
U_{24}(2445595/305552)&<{100000\over33}.
\end{aligned}
\tag{1.8a}
\]

with sum `94968`.  Thus

\[
\boxed{f(5/26)<V_5:={63\over1250}.}
\tag{1.8}
\]

Finally, at `3/13`, the exponents

\[
{25\pi\over169},\quad {64\pi\over169},\quad
{841\pi\over676},\quad {441\pi\over169}
\]

have strict lower Gaussian numerators

\[
62828,\quad30428,\quad2007,\quad27.
\]

Here the exact certificates are

\[
\begin{aligned}
U_{24}(8875/19097)&<{100000\over62828},&
U_{24}(22720/19097)&<{100000\over30428},\\
U_{24}(298555/76388)&<{100000\over2007},&
U_{24}(156555/19097)&<{100000\over27}.
\end{aligned}
\tag{1.9a}
\]

Their sum is `95290`, so

\[
\boxed{f(3/13)<V_6:={471\over10000}.}
\tag{1.9}
\]

## 2. Sharpened overlap-depth closure

For the ordered early and reflected late rays, write

\[
P_i=f(X_i)-f(Y_i)+g(Y_i),
\]

and retain the exact decomposition

\[
E(s)=C+g(\alpha)+\sum_{i=1}^{u}P_i+\mathcal M,
\qquad
\mathcal M=\sum_{r=u+2}^{25-u} f(s_r/A)\ge0.
\tag{2.1}
\]

Let

\[
H=\max_{0\le t\le1/2}
\#\{i:X_i\le t<Y_i\}
\tag{2.2}
\]

be the reflected interval-overlap depth.  The layer-cake identity gives

\[
\sum_{i=1}^{u}\bigl(f(X_i)-f(Y_i)\bigr)
\ge-H(\sup f-C).
\tag{2.3}
\]

Using (0.3), the crude theta bound, and `u<=12`, one obtains

\[
\begin{aligned}
E(s)
&>(H+1)L-HG-(u+1)\varepsilon.
\end{aligned}
\tag{2.4}
\]

The right side decreases with both `H` and `u`.  Therefore, if `H<=4`,

\[
E(s)>
5L-4G-13\varepsilon
={6270\over1000000}>0.
\tag{2.5}
\]

Thus every period-twenty-six clock of overlap depth at most four is
strictly positive.

## 3. The first-five ordered base

Ray disjointness gives

\[
u+1<26-u,
\qquad u\le12,
\tag{3.1}
\]

and terminal-suffix maximality gives

\[
Y_i>{i\over26}.
\tag{3.2}
\]

Price pairs one through three globally, pair four at `2/13`, and pair five
at `5/26`.  The exact first-five base is

\[
\begin{aligned}
B_{26}
&:=6L-3G-V_4-V_5-6\varepsilon\\
&={264144-159900-52300-50400-300\over1000000}\\
&={1244\over1000000}>0.
\end{aligned}
\tag{3.3}
\]

Every shorter ray ledger is stronger.

## 4. Ordered exhaustion and the two residual chambers

Use the fixed threshold `x_0=2/13`.  Once an `X_i` reaches `x_0`, every
later compact difference is nonnegative by (1.5).  From `i>=7`, one also
has `Y_i>1/4`, so every later theta term is positive.

If `X_6>=2/13`, pair six is greater than `-epsilon` and every later pair
is positive.  The remaining margin is

\[
{1244-50\over1000000}={1194\over1000000}>0.
\tag{4.1}
\]

Suppose `X_6<2/13`.  Since `Y_6>3/13`, pair six is greater than

\[
L-V_6-\varepsilon
=-{3126\over1000000}.
\tag{4.2}
\]

If the ray terminates at `u=6`, or if `X_7>=2/13`, the displayed ledger
has debt

\[
{1244-3126\over1000000}
=-{1882\over1000000}.
\tag{4.3}
\]

This is residual chamber `R_6`.

Now suppose `X_7<2/13`.  Since

\[
Y_7>{7\over26}>{6\over23},
\]

pair seven earns

\[
L-{4379\over100000}={234\over1000000}.
\tag{4.4}
\]

If the ray terminates at `u=7`, or if `X_8>=2/13`, the remaining debt is

\[
{1244-3126+234\over1000000}
=-{1648\over1000000}.
\tag{4.5}
\]

This is residual chamber `R_7`.

Finally suppose `X_8<2/13`.  Then `Y_8>4/13>2/7`, so pair eight earns
`3194/1000000`.  The margin becomes

\[
{1244-3126+234+3194\over1000000}
={1546\over1000000}>0.
\tag{4.6}
\]

If `X_9>=2/13`, every later pair is positive.  Otherwise
`Y_9>9/26>1/3`, so pair nine earns `2009/375000`.  At most three generic
quarter costs remain.  The longest branch therefore has numerator

\[
3(1546)+16072-3(3408)=10486>0
\tag{4.7}
\]

over denominator three million.  Thus no chamber with `X_8<2/13`
survives.

Combining with Section 2, every residual table necessarily satisfies

\[
\boxed{H\ge5}
\tag{4.8}
\]

and lies in exactly one of `R_6,R_7`.

## 5. Exact nonnegative residual credits

The two debts above are not heuristic.  They are exact deficits of two
explicit decompositions into nonnegative slack.

Let

\[
(R_1,R_2,R_3,R_4,R_5,R_6)
=(G,G,G,V_4,V_5,V_6).
\tag{5.1}
\]

On chamber `R_6`, define

\[
\begin{aligned}
\mathcal S_6={}&(C-L)
+\sum_{i=1}^{6}\{f(X_i)-L+R_i-f(Y_i)\}\\
&+\{g(\alpha)+\varepsilon\}
+\sum_{i=1}^{6}\{g(Y_i)+\varepsilon\}
+\mathcal M+\sum_{i=7}^{u}P_i.
\end{aligned}
\tag{5.2}
\]

Every summand is nonnegative, and the literal identity is

\[
\boxed{E(s)=-{1882\over1000000}+\mathcal S_6.}
\tag{5.3}
\]

Here the last sum is empty when `u=6`; otherwise `X_7>=2/13` makes every
one of its terms positive.

On chamber `R_7`, put additionally

\[
R_7={4379\over100000}
\]

and define

\[
\begin{aligned}
\mathcal S_7={}&(C-L)
+\sum_{i=1}^{7}\{f(X_i)-L+R_i-f(Y_i)\}\\
&+\{g(\alpha)+\varepsilon\}
+\sum_{i=1}^{6}\{g(Y_i)+\varepsilon\}
+g(Y_7)+\mathcal M+\sum_{i=8}^{u}P_i.
\end{aligned}
\tag{5.4}
\]

Again every summand is nonnegative, and

\[
\boxed{E(s)=-{1648\over1000000}+\mathcal S_7.}
\tag{5.5}
\]

The final sum is empty when `u=7`; otherwise `X_8>=2/13` makes all its
terms positive.

Consequently the present endpoint comparison closes period twenty-six as
soon as one proves either of the chamber-specific scalar credits

\[
\boxed{
\mathcal S_6>{1882\over1000000}
\quad\text{on }R_6,
\qquad
\mathcal S_7>{1648\over1000000}
\quad\text{on }R_7.}
\tag{5.6}
\]

The displayed anchor-only accounting does not supply these credits.  A
closure must either extract correlated slack from the ceiling, early compact
positions, theta ray, discarded middle train, or overlap geometry, or prove
strictly stronger prices than those used here.

## 6. Theorem and scope

### Theorem 6.1

Every honest exact-first-carry period-twenty-six cyclic Apéry clock is
strictly positive unless it has overlap depth at least five and belongs to
one of the two residual chambers `R_6,R_7` in Section 4.  On those chambers
the sufficient remaining scalar gates are exactly (5.6).

The emerging finite-threshold pattern is therefore precise.  Periods
twenty-three through twenty-five close by sparse anchor transport alone.
At period twenty-six the sharpened global price still eliminates every
low-overlap geometry, and the anchor grid eliminates every long
below-threshold ray, but two short high-overlap transition chambers remain.

This theorem concerns only honest exact-first-carry formal cyclic Apéry
clocks.  It does not address overshoot, later first crossing, finite
physical shoulders, complete period-twenty-six positivity, or an OR-word
construction.

## 7. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| sharpened global compact price | `MATH_THEOREM_APERY_PERIOD25_SHARP_GLOBAL_PRICE_AND_THRESHOLD_RAY_COMPLETE_POSITIVITY_20260804.md` | `61265fdf0e355aae0c6c786f9725ee639a427a1efb866fa21191ccb7b575653a` |
| six-twenty-thirds anchor | `MATH_THEOREM_APERY_PERIOD23_FOUR_AND_SIX_TWENTYTHIRDS_COMPLETE_POSITIVITY_20260804.md` | `2f8078d67c08ec37529351d57defe0e73a67779550dec31456806bcaa5c1c46f` |
| two-sevenths anchor | `MATH_THEOREM_APERY_PERIOD21_TWO_SEVENTHS_FAR_RAY_COMPLETE_POSITIVITY_20260804.md` | `20b87ed61065d927c25f8721586cebc42df6c15d9daf56844776ccb4e94e2bb8` |
| one-third anchor | `MATH_THEOREM_SIX_SLOT_H4_ACTIVE_GAMMA_COMPLETE_POSITIVITY_AND_BOUNDARY_COLLAPSE_20260804.md` | `3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953` |
| exact ray identity and overlap-depth theorem | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
| compact ceiling and quarter endpoint bounds | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| promoted pre-quarter floor | `MATH_THEOREM_APERY_PERIOD13_THREE_THIRTEENTHS_COMPLETE_POSITIVITY_20260804.md` | `236a857ccddb8cc0490902f9afc909b047180fcd54cf355e2c3c88fb88e2fb9f` |
| terminal suffix cutoff `Y_i>i/26` | `MATH_LEMMA_APERY_TERMINAL_SUFFIX_MAXIMUM_AND_QUARTER_CUTOFF_20260804.md` | `6ef133e15f8635db9a91fb837ef2df65fadedc6a52ff923b0b5895f215324639` |
| theta absolute bound and quarter sign | `MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md` | `f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3` |
