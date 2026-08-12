# Self-audit: period-thirteen three-thirteenths closure

**Date:** 2026-08-04  
**Audited theorem:**  
`MATH_THEOREM_APERY_PERIOD13_THREE_THIRTEENTHS_COMPLETE_POSITIVITY_20260804.md`  
**Verdict:** **PASS / GO.**  The promoted compact floor, period-thirteen
ray locations, pair prices, theta ledger, chamber exhaustion, and all three
rational margins replay exactly.  No computation or search is used.

## 1. Dependency and scope check

The proof uses only the following already-frozen facts:

1. the exact reflected-ray identity and the `H<=2` scalar closure;
2. terminal-suffix maximality;
3. the global compact upper bound `G=1079/20000`;
4. decrease from `1/5` and `f(1/5)<101/2000`;
5. the quarter upper bound `Q=1129/25000` and quarter decrease;
6. `|g|<1/20000` and positivity of `g` from the quarter onward;
7. `C>5503/125000`, `f(1/4)>44739/1000000`, and the fact that every
   interior critical point on the first quarter is a strict maximum.

The proof does not cite the later six-slot outer-gate theorem with the two
pending endpoint-strictness corrections.  The theorem is purely formal,
exact-first-carry, and period thirteen; it makes no shoulder or physical
claim.

## 2. Promoted compact floor

The endpoint comparison is

\[
 {44739\over1000000}-{5503\over125000}
 ={44739-44024\over1000000}
 ={715\over1000000}>0.
\]

A continuous differentiable function on `[0,1/4]` whose every interior
critical point is a strict maximum cannot attain its minimum in the
interior.  Both endpoints strictly exceed `5503/125000`.  Therefore

\[
 f(x)>{5503\over125000}
 \qquad(0\le x\le1/4).
\]

This step is exact and has no hidden sampled estimate.

## 3. Ray geometry and middle terms

From `u+1<13-u`,

\[
 2u<12,
\]

so the integer bound is `u<=5`.  The terminal envelope gives

\[
 Y_i\ge\alpha+{i\over13}(1-\alpha)
 ={i\over13}+{13-i\over13}\alpha>{i\over13}.
\]

The anchor comparisons are exact:

\[
 {3\over13}>{1\over5},
 \qquad
 {4\over13}>{1\over4},
 \qquad
 {5\over13}>{1\over4}.
\]

The middle index interval is `[u+2,12-u]`.  Substitution gives

\[
\begin{array}{c|c|c}
u&[u+2,12-u]&\text{count}\\ \hline
3&[5,9]&5\\
4&[6,8]&3\\
5&[7,7]&1.
\end{array}
\]

All these terms are strictly positive and are discarded only after the
exact identity is written.

## 4. Pair-price replay

For a global pair, either `X<1/4`, giving

\[
 f(X)-f(Y)+g(Y)>L-G-\varepsilon,
\]

or both endpoints lie in the decreasing quarter band, giving a
nonnegative compact difference and positive theta.  Since `L-G-epsilon`
is negative, this is stronger.

For pair three, `Y_3>3/13>1/5`.  If `X_3<1/5`, then

\[
 f(X_3)>L,
 \qquad
 f(Y_3)<f(3/13)<f(1/5)<U.
\]

If `X_3>=1/5`, decrease gives `f(X_3)>=f(Y_3)`.  Thus the uniform price
is `L-U-epsilon`.

For pairs four and five, `Y_i>1/4`.  The same two-case argument gives
`L-Q`, with no theta charge because `g(Y_i)>0`.

Together with `g(alpha)>-epsilon`, exactly four negative theta allowances
are used.  No theta term is omitted or charged twice.

## 5. Rational ledger

With denominator `500000`,

\[
 L={5503\over125000}={22012\over500000},
\]

\[
 2G={2158\over20000}={53950\over500000},
 \qquad
 U={101\over2000}={25250\over500000},
\]

\[
 Q={1129\over25000}={22580\over500000},
 \qquad
 4\varepsilon={4\over20000}={100\over500000}.
\]

Therefore:

\[
\begin{aligned}
u=3:&\quad
4L-2G-U-4\varepsilon\\
&={88048-53950-25250-100\over500000}
 ={8748\over500000}
 ={2187\over125000}>0;
\end{aligned}
\]

\[
\begin{aligned}
u=4:&\quad
5L-2G-U-Q-4\varepsilon\\
&={110060-53950-25250-22580-100\over500000}
 ={8180\over500000}
 ={409\over25000}>0;
\end{aligned}
\]

\[
\begin{aligned}
u=5:&\quad
6L-2G-U-2Q-4\varepsilon\\
&={132072-53950-25250-45160-100\over500000}
 ={7612\over500000}
 ={1903\over125000}>0.
\end{aligned}
\]

All numerator arithmetic agrees with the theorem.

## 6. Chamber exhaustion

The overlap depth satisfies `H<=u`.  Thus `H>=3` implies
`u in {3,4,5}`, exactly the three ledgers above.  For `H<=2`, the worst
possible scalar is

\[
 360H+\tau\le720+(u+1)\le726<860,
\]

so the prior depth theorem applies.  These cases exhaust every honest
period-thirteen exact-first-carry clock.

**Final audit verdict:** **PASS / GO.**
