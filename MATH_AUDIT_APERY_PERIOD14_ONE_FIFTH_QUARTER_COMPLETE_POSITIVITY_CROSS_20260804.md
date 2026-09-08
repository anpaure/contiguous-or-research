# Cross-audit: period-fourteen one-fifth/quarter positivity

**Date:** 2026-08-04  
**Method:** independent symbolic and rational audit only; no search, numerical
experiment, or computational construction.

**Audited theorem:**
`MATH_THEOREM_APERY_PERIOD14_ONE_FIFTH_QUARTER_COMPLETE_POSITIVITY_20260804.md`,
SHA256
`662ce674cd921d94567382033ff2f7a42eaf0e726dc8d8b990a32b7df6ebbe17`.

## 0. Verdict

**GO.**  The promoted floor, period-fourteen ray geometry, theta accounting,
chamber exhaustion, and all four rational margins are correct.  There are
two cosmetic missing backslashes before `quad` in (1.2) and (1.4); they do
not change either inequality or the proof.

## 1. Promoted compact floor

The endpoint certificates give

\[
 f(0)=C>{5503\over125000}
 ={44024\over1000000}
\]

and

\[
 f(1/4)>{44739\over1000000}
       >{44024\over1000000}.
\]

The compact train is analytic, and every interior critical point on the
interval is a strict maximum.  An interior global minimum would be a local
minimum and an interior critical point, which is impossible.  Therefore the
minimum on `[0,1/4]` is attained at an endpoint, and both endpoint bounds
are strict.  This proves

\[
                         f(x)>{5503\over125000}
 \qquad(0\le x\le1/4).
\]

The dependency chain is exactly the one cited in the theorem: the two
endpoint estimates come from the compact Gaussian gate, and the critical
point classification comes from the one-mode compact theorem.  No six-slot
endpoint statement is used.

## 2. Ray geometry and quarter cutoff

Ray disjointness gives

\[
                         u+1<14-u.
\]

Thus `2u<13` and, integrally,

\[
                         u\le6.
\tag{2.1}
\]

The terminal-suffix envelope is

\[
 Y_i\ge\alpha+{i\over14}(1-\alpha)
 ={i\over14}+\alpha\left(1-{i\over14}\right).
\]

Since `alpha>0` and `i<14`, this is strictly greater than `i/14`.  Hence

\[
 Y_3>{3\over14}>{1\over5},
\]

and, for every `i>=4`,

\[
 Y_i>{i\over14}\ge{4\over14}={2\over7}>{1\over4}.
\tag{2.2}
\]

The exact middle index range is `u+2<=r<=13-u`.  It gives

\[
\begin{array}{c|c}
u&\text{middle residues}\\ \hline
3&5,6,7,8,9,10\\
4&6,7,8,9\\
5&7,8\\
6&\varnothing.
\end{array}
\]

Every nonempty listed middle shift is at most `A/2`, so its compact train is
strictly positive.  For `u=6` there is no middle term to discard, exactly as
the theorem records.

## 3. Pair prices and theta count

Let

\[
 L={5503\over125000},\quad
 G={1079\over20000},\quad
 U={101\over2000},\quad
 Q={1129\over25000},\quad
 \varepsilon={1\over20000}.
\]

The first two ray pairs use the global price `L-G-epsilon`.  Pair three has
`Y_3>1/5`, so one-fifth decrease gives the price `L-U-epsilon`.  Every pair
from four onward has `Y_i>1/4`, so quarter decrease and positive theta give
`L-Q` with no adverse theta charge.

The only possibly negative theta terms are therefore

\[
                         g(\alpha),g(Y_1),g(Y_2),g(Y_3),
\]

exactly four.  The constant train contributes one `L`, and the `u` pairs
contribute `uL`, yielding

\[
 E(s)>(u+1)L-2G-U-(u-3)Q-4\varepsilon.
\tag{3.1}
\]

No theta charge is omitted: all `g(Y_i)` for `i>=4` are strictly positive
by (2.2).

## 4. Exact rational margins

On denominator `500000`,

\[
 L={22012\over500000},\quad
 2G={53950\over500000},\quad
 U={25250\over500000},\quad
 Q={22580\over500000},\quad
 4\varepsilon={100\over500000}.
\]

Substitution into (3.1) gives:

\[
\begin{array}{c|c|c}
u&\text{numerator over }500000&\text{reduced margin}\\ \hline
3&4(22012)-53950-25250-100=8748&2187/125000\\
4&5(22012)-53950-25250-22580-100=8180&409/25000\\
5&6(22012)-53950-25250-2(22580)-100=7612&1903/125000\\
6&7(22012)-53950-25250-3(22580)-100=7044&1761/125000.
\end{array}
\tag{4.1}
\]

Every numerator is positive.  The maximal-chamber calculation in the
theorem is therefore exact.

## 5. Chamber exhaustion

The overlap depth satisfies `H<=u`.

If `H<=2`, then `tau<=u+1<=7`, and

\[
                         360H+\tau\le720+7=727<860.
\]

The reflected-depth theorem gives strict positivity.

If `H>=3`, then `u>=H>=3`; equation (2.1) gives `u<=6`.  Thus the remaining
values are exactly

\[
                         u=3,4,5,6,
\]

all covered by (4.1).  This includes every possible value of `H` without
requiring `H=3`.  Finally `Phi(W)>=E(s)` transfers the strict ledger margin
to the formal Bellman functional.

The result remains scoped to the honest exact-first-carry branch.  It does
not cover threshold overshoot, later first crossing, or finite physical
shoulders.

