# Period twenty-three: four- and six-twenty-thirds anchors and complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that every
honest exact-first-carry cyclic Apéry clock of period twenty-three has
strictly positive formal Bellman functional.  No search or sampled
computation is used.  The proof uses two literal rational Gaussian anchors
and an ordered-ray dichotomy through the maximal ray depth `u=10`.

Put

\[
A={\sqrt\pi\over2},\qquad
f(x)=F_A(Ax),\qquad C=F_A(0),\qquad g(x)=\rho(Ax).
\tag{0.1}
\]

Retain

\[
L={5503\over125000},\quad
G={1079\over20000},\quad
U={101\over2000},\quad
Q={1129\over25000},\quad
\varepsilon={1\over20000},
\tag{0.2}
\]

the quarter floor `f>L`, quarter-band decrease and positive theta, and
the already-proved two-sevenths anchor

\[
f(2/7)<V_7:={4083\over100000}.
\tag{0.3}
\]

We also use the rational bounds

\[
{333\over106}<\pi<{355\over113}.
\tag{0.4}
\]

## 1. A monotone four-twenty-thirds anchor

Let

\[
h(t)=t e^{-\pi t^2/4}.
\]

At `x_0=4/23`, the first two positive/adverse derivative ratios are

\[
R_1={27\over19}e^{-4\pi/23},\qquad
R_2={50\over19}e^{-93\pi/92}.
\tag{1.1}
\]

The positive Taylor polynomials at the lower rational exponents supplied
by (0.4) give

\[
R_1<{83\over100},\qquad R_2<{3\over25}.
\tag{1.2}
\]

Explicitly, it is enough to use degrees four and six respectively in

\[
e^{666/1219}>{2700\over1577},\qquad
e^{30969/9752}>{1250\over57}.
\tag{1.3}
\]

Beginning with the positive term `h(50/23)`, every successive ratio is
below `1/30`.  Indeed the ratio decreases with its argument, and at the
first argument the degree-five positive Taylor polynomial gives

\[
e^{40959/9752}>{219\over5},
\]

which is exactly stronger than

\[
{73\over50}e^{-123\pi/92}<{1\over30}.
\tag{1.4}
\]

Hence the complete positive/adverse derivative ratio at `x_0` is below

\[
{83\over100}+{3/25\over1-1/30}
={2767\over2900}<1.
\tag{1.5}
\]

Every individual ratio decreases on `[4/23,1/2]`.  For the first ratio,

\[
{d\over dx}\log R_1(x)={2\over1-x^2}-\pi
\le{8\over3}-\pi<0.
\]

For every later ratio, its logarithmic derivative is at most
`5/2-3pi/2<0`.  We have proved

\[
\boxed{f'(x)<0\qquad(4/23\le x\le1/2).}
\tag{1.6}
\]

For `0<z<25`, define

\[
U_{24}(z)=\sum_{j=0}^{23}{z^j\over j!}
+{z^{24}\over24!\,(1-z/25)},
\tag{1.7}
\]

so `e^z<U_24(z)`.  The literal train gives

\[
\begin{aligned}
f(4/23)<1
&-e^{-361\pi/2116}-e^{-729\pi/2116}\\
&-e^{-625\pi/529}-e^{-5329\pi/2116}.
\end{aligned}
\tag{1.8}
\]

Using `pi<355/113`, direct positive-denominator substitution in (1.7)
gives

\[
\begin{aligned}
U_{24}(128155/239108)&<{100000\over58509},\\
U_{24}(258795/239108)&<{100000\over33879},\\
U_{24}(221875/59777)&<{2500\over61},\\
U_{24}(1891795/239108)&<{25000\over9}.
\end{aligned}
\tag{1.9}
\]

Each comparison is a finite positive-integer cross multiplication.  Thus

\[
\begin{aligned}
e^{-361\pi/2116}&>{58509\over100000},&
e^{-729\pi/2116}&>{33879\over100000},\\
e^{-625\pi/529}&>{61\over2500},&
e^{-5329\pi/2116}&>{9\over25000}.
\end{aligned}
\tag{1.10}
\]

Their lower sum is `94864/100000`, so

\[
\boxed{f(4/23)<V_4:={321\over6250}.}
\tag{1.11}
\]

## 2. A six-twenty-thirds far anchor

The same literal train gives

\[
\begin{aligned}
f(6/23)<1
&-e^{-289\pi/2116}-e^{-841\pi/2116}\\
&-e^{-676\pi/529}-e^{-5625\pi/2116}.
\end{aligned}
\tag{2.1}
\]

The corresponding exact `U_24` comparisons are

\[
\begin{aligned}
U_{24}(102595/239108)&<{25000\over16277},\\
U_{24}(298555/239108)&<{100000\over28687},\\
U_{24}(239980/59777)&<{100000\over1803},\\
U_{24}(1996875/239108)&<{100000\over23}.
\end{aligned}
\tag{2.2}
\]

Consequently

\[
\begin{aligned}
e^{-289\pi/2116}&>{16277\over25000},&
e^{-841\pi/2116}&>{28687\over100000},\\
e^{-676\pi/529}&>{1803\over100000},&
e^{-5625\pi/2116}&>{23\over100000}.
\end{aligned}
\tag{2.3}
\]

The numerator sum over `100000` is

\[
65108+28687+1803+23=95621.
\]

Therefore

\[
\boxed{f(6/23)<V_6:={4379\over100000}.}
\tag{2.4}
\]

The useful far credit is

\[
L-V_6={44024-43790\over1000000}
={234\over1000000}.
\tag{2.5}
\]

## 3. The period-twenty-three base ledger

Ray disjointness gives `u<=10`, and terminal-suffix maximality gives

\[
Y_i>{i\over23}.
\tag{3.1}
\]

In particular

\[
Y_4>{4\over23},\quad
Y_5>{5\over23}>{1\over5},\quad
Y_6>{6\over23}>{1\over4},\quad
Y_7>{7\over23}>{2\over7}.
\tag{3.2}
\]

Price the first three pairs globally, pair four at `4/23`, and pair five
at one fifth.  Including the base theta term gives six adverse theta
allowances.  The exact lower margin through pair five is

\[
\begin{aligned}
B_{23}
&:=6L-3G-V_4-U-6\varepsilon\\
&={132072-80925-25680-25250-150\over500000}\\
&={67\over500000}>0.
\end{aligned}
\tag{3.3}
\]

For completeness, the shorter ray ledgers `u=1,2,3,4` have respective
lower numerators over `500000`

\[
16999,\qquad12011,\qquad7023,\qquad3330,
\tag{3.4}
\]

and `u=0` has the positive base `L-epsilon`.  Thus every chamber through
`u=5` is closed.

## 4. Ordered far-ray exhaustion through `u=10`

If `X_6>=1/4`, ordered early rays put every later `X_i` in the decreasing
quarter interval.  Every pair from six onward is then strictly positive,
so `B_23` closes the table.

Suppose `X_6<1/4`.  Since `Y_6>6/23`, (1.6) and (2.4) give

\[
f(X_6)-f(Y_6)+g(Y_6)>L-V_6
={234\over1000000}.
\tag{4.1}
\]

If `X_7>=1/4`, every later pair is positive.  Finally suppose
`X_7<1/4`.  The two-sevenths anchor gives pair seven the credit

\[
L-V_7={3194\over1000000}.
\tag{4.2}
\]

Every remaining pair has the valid generic quarter price

\[
L-Q=-{1136\over1000000}.
\tag{4.3}
\]

The worst case is `u=10`, with exactly three generic pairs after pair
seven.  Since `B_23=134/1000000`,

\[
\begin{aligned}
E(s)
&>{134+234+3194-3(1136)\over1000000}\\
&={154\over1000000}
={77\over500000}>0.
\end{aligned}
\tag{4.4}
\]

No middle train is needed.

## 5. Complete closure

### Theorem 5.1

Every honest exact-first-carry period-twenty-three cyclic Apéry clock
satisfies

\[
\boxed{\Phi(W)>0.}
\tag{5.1}
\]

#### Proof

If the reflected overlap depth is at most two, the general depth theorem
already closes every `u<=139`, hence every present `u<=10`.  Otherwise
the exact reflected identity and Sections 3--4 exhaust every possible ray
depth from zero through ten.  Finally `Phi(W)>=E(s)>0`. \(\square\)

## 6. Scope and dependencies

This theorem concerns only honest exact-first-carry formal cyclic Apéry
clocks.  It does not address overshoot, later first crossing, finite
physical shoulders, or any OR-word construction.

| role | file | SHA-256 |
|---|---|---|
| period 22 geometry and nested-ledger template | `MATH_THEOREM_APERY_PERIOD22_NESTED_FAR_RAY_COMPLETE_POSITIVITY_20260804.md` | `455adc5d9558e6bebff177decac1df601a0e60f848aa58c81972f6b34d09e954` |
| two-sevenths anchor | `MATH_THEOREM_APERY_PERIOD21_TWO_SEVENTHS_FAR_RAY_COMPLETE_POSITIVITY_20260804.md` | `20b87ed61065d927c25f8721586cebc42df6c15d9daf56844776ccb4e94e2bb8` |
| prefix minimum, ray identity, and depth theorem | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
| compact floor and Gaussian rows | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
