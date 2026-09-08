# Period twenty-five: a sharper global price and threshold-ray complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves strict
formal Bellman positivity for every honest exact-first-carry cyclic Apéry
clock of period twenty-five.  The proof introduces one reusable device: a
sharper global compact price plus a fixed left-ray threshold.  Once a left
endpoint crosses the threshold, every later compact difference is free;
otherwise the forced right endpoint earns an explicit anchor credit.  No
search or sampled computation is used.

Put

\[
A={\sqrt\pi\over2},\qquad
f(x)=F_A(Ax),\qquad C=F_A(0),\qquad g(x)=\rho(Ax),
\tag{0.1}
\]

and retain

\[
L={5503\over125000},\quad
Q={1129\over25000},\quad
\varepsilon={1\over20000},
\tag{0.2}
\]

as well as

\[
f(2/7)<V_7={4083\over100000},\qquad
f(6/23)<V_{23}={4379\over100000},\qquad
f(1/3)<V_9={29\over750}.
\tag{0.3}
\]

We use `333/106<pi<355/113` throughout.

## 1. A reusable sharper global compact price

For `0<=x<=1/5`, Jacobi completion writes

\[
f(x)=1-\Theta(x)+H(x)+R(x),
\tag{1.1}
\]

where

\[
H(x)=e^{-\pi x^2/4}+e^{-\pi(2-x)^2/4},
\qquad
R(x)=\sum_{j\ge3}e^{-\pi(j-x)^2/4},
\tag{1.2}
\]

and `|Theta(x)-2|<epsilon`.

The unique interior maximum `t_*` of `H` satisfies

\[
\log{2-t_*\over t_*}=\pi(1-t_*).
\tag{1.3}
\]

Put `t_0=589/5000`.  The lower bound `pi>333/106` and a finite positive
Taylor polynomial give

\[
e^{\pi(1-t_0)}>{9411\over589}={2-t_0\over t_0},
\tag{1.4}
\]

so `t_*<t_0`.  The critical-value envelope

\[
E(t)={2\over2-t}e^{-\pi t^2/4}
\]

is increasing on `[0,t_0]`.  With

\[
z_0={115524693\over10600000000}
<{\pi t_0^2\over4},
\]

the elementary bound `e^{-z}<1-z+z^2/2` and direct rational
cross multiplication give

\[
H(t_*)<E(t_0)
<{10000\over9411}\left(1-z_0+{z_0^2\over2}\right)
<{10511\over10000}.
\tag{1.5}
\]

The first residual-tail term is at most its value at `x=1/5`.  Since

\[
{49\pi\over25}>{16317\over2650},
\]

a degree-eighteen positive Taylor polynomial gives

\[
e^{49\pi/25}>{25000\over53}.
\tag{1.6}
\]

Every successive tail ratio is below `1/100`, as in the earlier global
bound.  Hence

\[
R(x)<{53/25000\over1-1/100}={53\over24750}.
\tag{1.7}
\]

Equations (1.1), (1.5), (1.7), and the theta bound give

\[
f(x)<{10511\over10000}-1+{53\over24750}+{1\over20000}
<{533\over10000}
\qquad(0\le x\le1/5).
\tag{1.8}
\]

For `1/5<=x<=1/2`, the old one-fifth value and monotonicity are stronger.
Thus the new global price is

\[
\boxed{f(x)<G_{25}:={533\over10000}
\qquad(0\le x\le1/2).}
\tag{1.9}
\]

This sharpening is independent of period twenty-five and may be reused.

## 2. Monotonicity from four twenty-fifths

At `x_0=4/25`, the first two positive/adverse derivative ratios are

\[
R_1={29\over21}e^{-4\pi/25},\qquad
R_2={18\over7}e^{-99\pi/100}.
\tag{2.1}
\]

Finite positive Taylor bounds give

\[
R_1<{17\over20},\qquad R_2<{3\over25}.
\tag{2.2}
\]

Beginning with `h(54/25)`, every successor ratio is below `1/30`; at the
first argument this is

\[
{79\over54}e^{-133\pi/100}<{1\over30}.
\tag{2.3}
\]

Therefore the complete ratio is below

\[
{17\over20}+{3/25\over1-1/30}
={113\over116}<1.
\tag{2.4}
\]

Every individual ratio decreases on `[4/25,1/2]`, by the same logarithmic
derivative calculation used at periods twenty-three and twenty-four.
Hence

\[
\boxed{f'(x)<0\qquad(4/25\le x\le1/2).}
\tag{2.5}
\]

## 3. Three literal value anchors

For `0<z<25`, let

\[
U_{24}(z)=\sum_{j=0}^{23}{z^j\over j!}
+{z^{24}\over24!\,(1-z/25)}.
\tag{3.1}
\]

All comparisons below follow from `pi<355/113` and direct
positive-denominator substitution in `U_24`.

### 3.1 Four twenty-fifths

The four retained adverse exponents are

\[
{441\pi\over2500},\quad {841\pi\over2500},\quad
{2916\pi\over2500},\quad {6241\pi\over2500}.
\]

Their Gaussian values are greater than

\[
{57454\over100000},\quad {34754\over100000},\quad
{2561\over100000},\quad {39\over100000}.
\]

The numerator sum is `94808`, so

\[
\boxed{f(4/25)<V_4:={649\over12500}.}
\tag{3.2}
\]

### 3.2 One fifth

At `1/5`, the four retained Gaussian values are greater than

\[
{60491\over100000},\quad {32271\over100000},\quad
{2233\over100000},\quad {32\over100000}.
\]

Their numerator sum is `95027`, and hence

\[
\boxed{f(1/5)<V_5:={4973\over100000}.}
\tag{3.3}
\]

### 3.3 Six twenty-fifths

At `6/25`, the four retained adverse exponents are

\[
{361\pi\over2500},\quad {961\pi\over2500},\quad
{3136\pi\over2500},\quad {6561\pi\over2500}.
\]

The corresponding Gaussian lower bounds are

\[
{6353\over10000},\quad {2989\over10000},\quad
{1943\over100000},\quad {26\over100000}.
\]

Their lower sum is `95389/100000`, so

\[
\boxed{f(6/25)<V_6:={4611\over100000}.}
\tag{3.4}
\]

## 4. Base ledger and the fixed-threshold rule

For period twenty-five, ray disjointness gives `u<=11`, and

\[
Y_i>{i\over25}.
\tag{4.1}
\]

Price pairs one through three globally, pair four at `4/25`, and pair
five at `1/5`.  The first-five base is

\[
\begin{aligned}
B_{25}
&:=6L-3G_{25}-V_4-V_5-6\varepsilon\\
&={264144-159900-51920-49730-300\over1000000}\\
&={2294\over1000000}>0.
\end{aligned}
\tag{4.2}
\]

The shorter ray ledgers are stronger.

Use the fixed left threshold `x_0=4/25`.  Once some `X_i>=x_0`, every
later compact difference is nonnegative by (2.5).  From `i>=7`, every
right endpoint lies beyond the quarter, so all those later pairs are
strictly positive.

## 5. Ordered-ray exhaustion

If `X_6>=4/25`, pair six is greater than `-epsilon`, and all later pairs
are positive.  The margin is at least `2244/1000000`.

Suppose `X_6<4/25`.  Since `Y_6>6/25`, pair six is greater than

\[
L-V_6-\varepsilon=-{2136\over1000000}.
\tag{5.1}
\]

If `X_7>=4/25`, every later pair is positive, leaving the strict margin

\[
B_{25}-{2136\over1000000}
={158\over1000000}>0.
\tag{5.2}
\]

If `X_7<4/25`, then

\[
Y_7>{7\over25}>{6\over23}.
\]

The period-twenty-three anchor therefore gives pair seven the positive
credit

\[
L-{4379\over100000}={234\over1000000}.
\tag{5.3}
\]

If `X_8>=4/25`, all later pairs are positive.  Otherwise pair eight earns
the two-sevenths credit `3194/1000000`, because `Y_8>8/25>2/7`.

If `X_9>=4/25`, all later pairs are positive.  Otherwise `Y_9>9/25>1/3`,
so pair nine earns

\[
L-{29\over750}={2009\over375000}.
\tag{5.4}
\]

At most two generic quarter pairs remain.  The completely un-crossed
`u=11` branch is therefore larger than

\[
{2294-2136+234+3194-2(1136)\over1000000}
+{2009\over375000}>0.
\tag{5.5}
\]

The smallest branch margin is the `158/1000000` in (5.2).

## 6. Complete closure and emerging pattern

### Theorem 6.1

Every honest exact-first-carry period-twenty-five cyclic Apéry clock
satisfies

\[
\boxed{\Phi(W)>0.}
\tag{6.1}
\]

#### Proof

Depth at most two is already closed by the general reflected-depth theorem.
Otherwise Sections 4--5 exhaust every possible `0<=u<=11`, and the exact
endpoint comparison gives `Phi(W)>=E(s)>0`. \(\square\)

The reusable pattern is now explicit:

1. sharpen one global compact price once;
2. prove monotonicity from one fixed pre-quarter threshold;
3. split on the first left endpoint crossing that threshold;
4. while the left ray remains below it, charge forced right endpoints by
   a sparse nested anchor grid.

This is a finite-threshold transport scheme rather than one unrelated new
anchor per reflected pair.

## 7. Scope

The result concerns only honest exact-first-carry formal cyclic Apéry
clocks.  It does not address overshoot, later first crossing, finite
physical shoulders, or an OR-word construction.

| role | file | SHA-256 |
|---|---|---|
| Jacobi completion, theta bound, and original global-price proof | `MATH_THEOREM_APERY_PERIOD10_H34_ONE_FIFTH_TRAIN_AND_COMPLETE_POSITIVITY_20260804.md` | `1697def0ed72f30c6972a706a968a3efed68e470ebe511b813c7eedc7259095e` |
| six-twenty-thirds anchor | `MATH_THEOREM_APERY_PERIOD23_FOUR_AND_SIX_TWENTYTHIRDS_COMPLETE_POSITIVITY_20260804.md` | `2f8078d67c08ec37529351d57defe0e73a67779550dec31456806bcaa5c1c46f` |
| two-sevenths anchor | `MATH_THEOREM_APERY_PERIOD21_TWO_SEVENTHS_FAR_RAY_COMPLETE_POSITIVITY_20260804.md` | `20b87ed61065d927c25f8721586cebc42df6c15d9daf56844776ccb4e94e2bb8` |
| one-third anchor | `MATH_THEOREM_SIX_SLOT_H4_ACTIVE_GAMMA_COMPLETE_POSITIVITY_AND_BOUNDARY_COLLAPSE_20260804.md` | `3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953` |
| reflected identity and depth theorem | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
