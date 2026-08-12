# Independent audit: period-twenty-two nested far-ray closure

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_APERY_PERIOD22_NESTED_FAR_RAY_COMPLETE_POSITIVITY_20260804.md`  
**Audited theorem SHA-256:**
`455adc5d9558e6bebff177decac1df601a0e60f848aa58c81972f6b34d09e954`  
**Verdict:** **GO.**  Both new rational anchors, the nested `X_6/X_7`
case split, theta/base accounting, exhaustion of all `u` chambers, the
`301/250000` margin, and the exact period-23 method break replay
correctly.  No computation or search is used.

## 1. Byte and dependency binding

The theorem rehashes to the displayed SHA.  Its dependencies rehash to:

| role | SHA-256 |
|---|---|
| complete period-21 theorem and `2/7` anchor | `20b87ed61065d927c25f8721586cebc42df6c15d9daf56844776ccb4e94e2bb8` |
| prefix/ray/depth reduction | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
| compact monotonicity and standard prices | `fb9139813f93d8e5450b8ab3cee0238c289cd573222d0d05fd6174040fdbe601` |
| compact lower floor | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |

The independent period-21 cross-audit is separately frozen at
`27e1d896178b3648d4e24f4860dc3fdc51c7993f8990901e1bb536f795ac2650`.

## 2. Two-elevenths anchor

At `x=2/11`, the derivative ratios are exactly

\[
 {13\over9}e^{-22\pi/121},
 \qquad
 {8\over3}e^{-495\pi/484}.
\]

The certified prices `83/100`, `11/100`, followed by geometric ratio
`1/30`, sum to

\[
 {83\over100}+{11/100\over1-1/30}
 ={2737\over2900}<1.
\]

The logarithmic derivative of the first ratio is negative because

\[
 {2\over1-x^2}\le {8\over3}<\pi
 \qquad(2/11\le x\le1/2),
\]

and every later ratio uses the stronger coefficient `3pi/2` against a
sum smaller than `5/2`.  Thus decrease propagates from `2/11` through the
entire half band.

The first four adverse value exponents are

\[
 {81\pi\over484},\quad
 {169\pi\over484},\quad
 {144\pi\over121},\quad
 {1225\pi\over484}.
\]

After `pi<22/7`, their rational upper exponents are

\[
 {891\over1694},\quad
 {1859\over1694},\quad
 {3168\over847},\quad
 {13475\over1694}.
\]

The theorem's `U_24` majorants invert to the strict Gaussian lower bounds

\[
 {11819\over20000},\quad
 {3337\over10000},\quad
 {237\over10000},\quad
 {7\over20000}.
\]

Over denominator `100000`, their numerators sum to

\[
 59095+33370+2370+35=94870.
\]

Therefore

\[
                         f(2/11)<5130/100000=513/10000.
\]

The exponential directions and all denominators are correct.

## 3. Three-elevenths anchor

At `x=3/11`, the four retained adverse exponents are

\[
 {16\pi\over121},\quad
 {49\pi\over121},\quad
 {625\pi\over484},\quad
 {324\pi\over121}.
\]

Their rational upper exponents under `pi<22/7` are

\[
 {352\over847},\quad
 {1078\over847},\quad
 {6875\over1694},\quad
 {7128\over847}.
\]

The certified lower Gaussian numerators over denominator `10000` are

\[
 6598,\quad 2800,\quad 172,\quad 2,
\]

whose sum is `9572`.  Hence

\[
                         f(3/11)<428/10000=107/2500.
\]

The two useful credits are therefore exactly

\[
 L-V_6={44024-42800\over1000000}
 ={1224\over1000000},
\]

and, using the independently audited period-21 anchor,

\[
 L-V_7={44024-40830\over1000000}
 ={3194\over1000000}.
\]

## 4. Base and theta ledger

Through pair five, denominator `500000` gives

\[
 6L=132072,
 \quad3G=80925,
 \quad V_4=25650,
 \quad U=25250,
 \quad6\varepsilon=150.
\]

Thus

\[
 B_{22}={132072-80925-25650-25250-150\over500000}
 ={97\over500000}>0.
\]

The frozen prefix/ray ledger places exactly six potentially adverse theta
allowances in this base row.  From pair six onward,

\[
 Y_6>3/11>1/4,
\]

so every far theta term is strictly positive.  The nested proof does not
debit another theta allowance and does not double-count positive theta.

The `u=5` row is therefore closed by the base itself.  The established
`u=3,4` ledgers are stronger and remain valid.

## 5. Nested ordered-ray cases

The frozen geometry supplies

\[
 X_6<X_7<\cdots,
 \qquad
 X_i\le Y_i<1/2,
 \qquad
 Y_i>{i\over22}.
\]

### Case 1: `X_6>=1/4`

Every later `X_i` is also at least `1/4`.  Quarter-band decrease gives
`f(X_i)>=f(Y_i)`, and the far theta terms are positive.  Every appended
pair is strictly positive.

### Case 2: `X_6<1/4<=X_7`

Pair six has price `L-V_6`, because `Y_6>3/11>1/5` and decrease gives
`f(Y_6)<f(3/11)<V_6`.  All later pairs are strictly positive.

### Case 3: `X_7<1/4`

Orderedness also gives `X_6<1/4`.  Pair six has price `L-V_6`, while
`Y_7>7/22>2/7` lets pair seven use the independently audited price
`L-V_7`.  For each later pair, a pre-quarter left endpoint costs at most
`Q-L`, while a post-quarter left endpoint makes the pair positive.

Since `u<=10`, at most the three pairs `8,9,10` receive the adverse generic
quarter price.  This is the genuine worst nested case; every smaller `u`
deletes at least one negative term.

## 6. Final margin and `u` exhaustion

Converting the base to denominator one million gives `194`.  The worst
case is

\[
 E(s)>{194+1224+3194-3(1136)\over1000000}
 ={1204\over1000000}
 ={301\over250000}>0.
\]

Thus:

* `u=3,4` use the earlier stronger ledgers;
* `u=5` uses `B_22`;
* `u=6` uses at most the pair-six branch;
* `u=7` uses at most the two anchors;
* `u=8,9,10` add respectively one, two, or three generic quarter prices.

This exhausts every `3<=u<=10`.  For `H<=2`, the separate depth condition
is

\[
 360H+\tau\le720+11=731<860,
\]

so those cases are already covered.  No middle train is needed in the
new nested ledger.

## 7. Exact period-23 method break

At period 23,

\[
                         4/23<2/11,
\]

so the two-elevenths price is unavailable in the first new `u=5` row.
The present anchor set must price four pairs globally, giving

\[
\begin{aligned}
 6L-4G-U-6\varepsilon
 &=0.264144-0.2158-0.0505-0.0003\\
 &=-0.002456=-{307\over125000}.
\end{aligned}
\]

Replacing the fourth global price by an anchor value `V` closes exactly
when

\[
 V<6L-3G-U-6\varepsilon
 ={25747\over500000}.
\]

Thus `f(4/23)<25747/500000` is the exact next sufficient scalar for this
ledger.  The theorem correctly labels the break as a method frontier, not
a negative clock.

## 8. Scope verdict

All rational anchors, order cases, theta counts, chamber bounds, and the
period-23 frontier pass.  The theorem closes only honest
exact-first-carry formal period-22 clocks, exactly as stated.

The independent verdict is

\[
                         \boxed{\textbf{GO}.}
\]
