# Period twenty-four: one-sixth and five-twenty-fourths anchors and complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves strict
formal Bellman positivity for every honest exact-first-carry cyclic Apéry
clock of period twenty-four.  The proof uses two new pre-quarter rational
anchors and a three-stage ordered far-ray dichotomy.  No search or sampled
computation is used.

Put

\[
A={\sqrt\pi\over2},\qquad
f(x)=F_A(Ax),\qquad C=F_A(0),\qquad g(x)=\rho(Ax),
\tag{0.1}
\]

and retain

\[
L={5503\over125000},\quad
G={1079\over20000},\quad
Q={1129\over25000},\quad
\varepsilon={1\over20000}.
\tag{0.2}
\]

We also retain

\[
f(2/7)<V_7={4083\over100000},\qquad
f(1/3)<V_8={29\over750},
\tag{0.3}
\]

and the rational bounds

\[
{333\over106}<\pi<{355\over113}.
\tag{0.4}
\]

## 1. Monotonicity from one sixth

At `x_0=1/6`, the first two positive/adverse derivative ratios are

\[
R_1={7\over5}e^{-\pi/6},\qquad
R_2={13\over5}e^{-\pi}.
\tag{1.1}
\]

Finite positive Taylor polynomials at the lower exponent bounds from
(0.4) give

\[
R_1<{21\over25},\qquad R_2<{3\over25}.
\tag{1.2}
\]

Beginning with the term `h(13/6)`, every successive positive-term ratio
is below `1/30`; at the first argument this follows from

\[
{19\over13}e^{-4\pi/3}<{1\over30},
\tag{1.3}
\]

and the ratio decreases afterward.  Thus the complete positive/adverse
ratio is below

\[
{21\over25}+{3/25\over1-1/30}
={699\over725}<1.
\tag{1.4}
\]

As in the period-twenty-three proof, every individual ratio has negative
logarithmic derivative on `[1/6,1/2]`: the first is bounded by
`8/3-pi<0`, and every later one by `5/2-3pi/2<0`.  Hence

\[
\boxed{f'(x)<0\qquad(1/6\le x\le1/2).}
\tag{1.5}
\]

## 2. The one-sixth anchor

For `0<z<25`, let

\[
U_{24}(z)=\sum_{j=0}^{23}{z^j\over j!}
+{z^{24}\over24!\,(1-z/25)},
\tag{2.1}
\]

so `e^z<U_24(z)`.  The literal train is

\[
f(1/6)<1-e^{-25\pi/144}-e^{-49\pi/144}
-e^{-169\pi/144}-e^{-361\pi/144}.
\tag{2.2}
\]

Using `pi<355/113`, direct positive-denominator substitution gives

\[
\begin{aligned}
U_{24}(8875/16272)&<{100000\over57959},\\
U_{24}(17395/16272)&<{100000\over34334},\\
U_{24}(59995/16272)&<{12500\over313},\\
U_{24}(128155/16272)&<{100000\over37}.
\end{aligned}
\tag{2.3}
\]

Therefore the four adverse Gaussians are respectively greater than

\[
{57959\over100000},\quad
{34334\over100000},\quad
{626\over25000},\quad
{37\over100000}.
\tag{2.4}
\]

Their lower numerator sum over `100000` is

\[
57959+34334+2504+37=94834.
\]

Thus

\[
\boxed{f(1/6)<V_4:={2583\over50000}.}
\tag{2.5}
\]

## 3. The five-twenty-fourths anchor

The literal train gives

\[
\begin{aligned}
f(5/24)<1
&-e^{-361\pi/2304}-e^{-841\pi/2304}\\
&-e^{-2809\pi/2304}-e^{-5929\pi/2304}.
\end{aligned}
\tag{3.1}
\]

The exact Taylor-majorant comparisons are

\[
\begin{aligned}
U_{24}(128155/260352)&<{100000\over61125},\\
U_{24}(298555/260352)&<{100000\over31766},\\
U_{24}(997195/260352)&<{10000\over217},\\
U_{24}(2104795/260352)&<{10000\over3}.
\end{aligned}
\tag{3.2}
\]

Hence the four Gaussians are greater than

\[
{61125\over100000},\quad
{31766\over100000},\quad
{217\over10000},\quad
{3\over10000}.
\tag{3.3}
\]

Their lower numerator sum over `100000` is

\[
61125+31766+2170+30=95091.
\]

Therefore

\[
\boxed{f(5/24)<V_5:={4909\over100000}.}
\tag{3.4}
\]

## 4. Base ledger

For period twenty-four, ray disjointness gives `u<=11`, and

\[
Y_i>{i\over24}.
\tag{4.1}
\]

In particular,

\[
Y_4>{1\over6},\quad
Y_5>{5\over24},\quad
Y_6>{1\over4},\quad
Y_7>{7\over24}>{2\over7},\quad
Y_8>{1\over3}.
\tag{4.2}
\]

Price the first three pairs globally and pairs four and five at the two
new anchors.  Including all six possible adverse theta terms, the exact
base through pair five is

\[
\begin{aligned}
B_{24}
&:=6L-3G-V_4-V_5-6\varepsilon\\
&={264144-161850-51660-49090-300\over1000000}\\
&={1244\over1000000}>0.
\end{aligned}
\tag{4.3}
\]

The shorter ray ledgers are stronger, so every `u<=5` chamber is closed.

## 5. Ordered far-ray exhaustion

If `X_6>=1/4`, all later pairs are strictly positive and `B_24` closes
the table.

Suppose `X_6<1/4`.  Pair six has the generic quarter price

\[
L-Q=-{1136\over1000000}.
\tag{5.1}
\]

If `X_7>=1/4`, all later pairs are positive, and the remaining margin is

\[
B_{24}+L-Q={108\over1000000}>0.
\tag{5.2}
\]

Suppose next that `X_7<1/4`.  Since `Y_7>2/7`, pair seven earns

\[
L-V_7={3194\over1000000}.
\tag{5.3}
\]

If `X_8>=1/4`, all later pairs are positive and the margin is already
`3302/1000000`.

Finally suppose `X_8<1/4`.  Since `Y_8>1/3`, pair eight earns

\[
L-V_8
={5503\over125000}-{29\over750}
={2009\over375000}.
\tag{5.4}
\]

At most three generic quarter pairs remain.  Over denominator three
million, the worst `u=11` ledger is

\[
\begin{aligned}
E(s)>{}&
{3732-3408+9582+16072-3(3408)\over3000000}\\
={15754\over3000000}>0.
\end{aligned}
\tag{5.5}
\]

The smallest margin among all ordered branches is therefore the value in
(5.2), namely

\[
\boxed{{27\over250000}.}
\tag{5.6}
\]

No middle train is used.

## 6. Complete closure

### Theorem 6.1

Every honest exact-first-carry period-twenty-four cyclic Apéry clock
satisfies

\[
\boxed{\Phi(W)>0.}
\tag{6.1}
\]

#### Proof

Depth at most two is already closed by the general reflected-depth theorem.
Otherwise Sections 4--5 exhaust every possible ray depth `0<=u<=11`.
The exact endpoint comparison gives `Phi(W)>=E(s)>0`. \(\square\)

## 7. Scope and dependencies

This theorem concerns only honest exact-first-carry formal cyclic Apéry
clocks.  It does not address overshoot, later first crossing, finite
physical shoulders, or an OR-word construction.

| role | file | SHA-256 |
|---|---|---|
| period 23 monotonicity and ordered template | `MATH_THEOREM_APERY_PERIOD23_FOUR_AND_SIX_TWENTYTHIRDS_COMPLETE_POSITIVITY_20260804.md` | `2f8078d67c08ec37529351d57defe0e73a67779550dec31456806bcaa5c1c46f` |
| two-sevenths far anchor | `MATH_THEOREM_APERY_PERIOD21_TWO_SEVENTHS_FAR_RAY_COMPLETE_POSITIVITY_20260804.md` | `20b87ed61065d927c25f8721586cebc42df6c15d9daf56844776ccb4e94e2bb8` |
| one-third anchor | `MATH_THEOREM_SIX_SLOT_H4_ACTIVE_GAMMA_COMPLETE_POSITIVITY_AND_BOUNDARY_COLLAPSE_20260804.md` | `3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953` |
| depth theorem | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
