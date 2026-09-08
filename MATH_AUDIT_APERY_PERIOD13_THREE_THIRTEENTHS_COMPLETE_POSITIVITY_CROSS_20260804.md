# Cross-audit: period-thirteen three-thirteenths positivity

**Date:** 2026-08-04  
**Method:** independent symbolic and rational audit only; no search, numerical
experiment, or computational construction.

**Audited theorem:**
`MATH_THEOREM_APERY_PERIOD13_THREE_THIRTEENTHS_COMPLETE_POSITIVITY_20260804.md`,
SHA256
`236a857ccddb8cc0490902f9afc909b047180fcd54cf355e2c3c88fb88e2fb9f`.

## 0. Verdict

**GO.**  The promoted pre-quarter floor is logically valid, the reflected
chambers are exhausted, exactly four adverse theta charges are paid, and all
three displayed rational margins are correct and strictly positive.  No
scope repair to the theorem is required.

## 1. Promotion of the compact floor

The two certified endpoint inequalities are

\[
 f(0)=C>{5503\over125000}
 ={44024\over1000000},
\]

and

\[
 f(1/4)>{44739\over1000000}
       >{44024\over1000000}.
\]

The train `f` is analytic.  If its minimum on `[0,1/4]` occurred at an
interior point, that point would be critical and a local minimum.  The
authenticated one-mode classification says every interior critical point
is a strict local maximum, a contradiction.  The minimum is therefore at
an endpoint, and both endpoint bounds are strict.  Hence

\[
 \boxed{f(x)>{5503\over125000}}
 \qquad(0\le x\le1/4).
\]

This argument uses only the two endpoint certificates and the interior
critical-point classification.  It does not import any later six-slot
endpoint assertion.

## 2. Period-thirteen geometry

The ray disjointness inequality is

\[
                         u+1<13-u.
\]

Thus `2u<12` and

\[
                         u\le5.
\tag{2.1}
\]

Terminal-suffix maximality gives

\[
 Y_i\ge\alpha+{i\over13}(1-\alpha)
 ={i\over13}+\alpha\left(1-{i\over13}\right).
\]

Here `alpha>0` and `i<13`, so the inequality is strict above `i/13`.
Consequently

\[
 Y_3>{3\over13}>{1\over5},
 \qquad
 Y_4>{4\over13}>{1\over4},
 \qquad
 Y_5>{5\over13}>{1\over4}.
\tag{2.2}
\]

The middle-sum index range in the exact ray identity is

\[
                         u+2\le r\le12-u.
\]

It is therefore `5,...,9` for `u=3`, `6,7,8` for `u=4`, and just `7`
for `u=5`, exactly as stated.  These residues lie before the late ray, so
their normalized shifts are at most `1/2`; the authenticated compact bound
is strictly positive there.  Discarding the middle sum is safe and loses a
strictly positive quantity even in the critical `u=5` chamber.

## 3. Audit of the three pair prices

Write

\[
 L={5503\over125000},\quad
 G={1079\over20000},\quad
 U={101\over2000},\quad
 Q={1129\over25000},\quad
 \varepsilon={1\over20000}.
\]

For every ray pair, `0<X<=Y<1/2`.

### Global pair

If `X<1/4`, then

\[
 f(X)-f(Y)+g(Y)>L-G-\varepsilon.
\]

If `X>=1/4`, compact decrease gives `f(X)>=f(Y)` and the theta sign gives
`g(Y)>0`; this is stronger because `L-G-epsilon<0`.

### Three-thirteenths pair

When `Y>3/13`, first take `X<1/5`.  Then `f(X)>L`, while strict decrease on
`[1/5,1/2]` gives

\[
 f(Y)<f(3/13)<f(1/5)<U.
\]

Together with `g(Y)>-epsilon`, this gives `L-U-epsilon`.  If `X>=1/5`,
decrease gives a nonnegative compact difference and the absolute theta
bound gives more than `-epsilon`, which is stronger since `L-U<0`.

### Quarter pair

When `Y>1/4`, if `X<1/4` use `f(X)>L`, `f(Y)<Q`, and `g(Y)>0`.  If
`X>=1/4`, decrease and positive theta make the whole pair positive.  Both
cases imply the claimed strict lower bound `L-Q`.

All interval endpoints are used in the correct direction.  In particular,
the three-thirteenths price needs only `Y>3/13>1/5`, not a quarter
location.

## 4. Theta-charge count and ledger

For `u>=3`, the theorem uses:

* two global pairs, costing `2(G+epsilon)`;
* one three-thirteenths pair, costing `U+epsilon`;
* `u-3` quarter pairs, whose theta terms are positive and cost no
  `epsilon`; and
* the separate initial term `g(alpha)>-epsilon`.

The potentially adverse theta terms are therefore exactly

\[
 g(\alpha),\quad g(Y_1),\quad g(Y_2),\quad g(Y_3),
\]

four charges.  The constant train contributes one `L`, and the `u` pair
floors contribute another `uL`.  Thus

\[
 E(s)>
 (u+1)L-2G-U-(u-3)Q-4\varepsilon,
\]

with no omitted theta or compact term.

## 5. Rational margins

On denominator `500000`, the constants are

\[
 L={22012\over500000},\quad
 2G={53950\over500000},\quad
 U={25250\over500000},\quad
 Q={22580\over500000},\quad
 4\varepsilon={100\over500000}.
\]

For `u=3`, the numerator is

\[
 4(22012)-53950-25250-100
 =8748,
\]

so

\[
 E(s)>{8748\over500000}={2187\over125000}>0.
\]

For `u=4`, it is

\[
 5(22012)-53950-25250-22580-100
 =8180,
\]

so

\[
 E(s)>{8180\over500000}={409\over25000}>0.
\]

For `u=5`, it is

\[
 6(22012)-53950-25250-2(22580)-100
 =7612,
\]

so the critical margin is exactly

\[
 \boxed{E(s)>{7612\over500000}={1903\over125000}>0.}
\]

## 6. Chamber exhaustion

The overlap depth always satisfies `H<=u`.

If `H<=2`, the depth theorem has

\[
 \tau\le u+1\le6,
 \qquad
 360H+\tau\le720+6=726<860,
\]

and therefore gives strict positivity directly.

If `H>=3`, then `u>=H>=3`; equation (2.1) gives `u<=5`.  Hence the only
remaining values are

\[
                         u=3,4,5,
\]

all closed by the three rational ledgers above, independently of the exact
value of `H`.  Since `Phi(W)>=E(s)`, positivity of `E(s)` completes the
formal exact-first-carry branch.

The theorem correctly makes no claim about threshold overshoot, later first
crossing, or finite physical shoulders.

