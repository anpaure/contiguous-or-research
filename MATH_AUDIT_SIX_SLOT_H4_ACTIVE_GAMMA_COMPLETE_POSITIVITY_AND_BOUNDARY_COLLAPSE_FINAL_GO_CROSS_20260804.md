# Final independent GO audit: six-slot `h=4` active-`Gamma` positivity

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_SIX_SLOT_H4_ACTIVE_GAMMA_COMPLETE_POSITIVITY_AND_BOUNDARY_COLLAPSE_20260804.md`  
**Audited SHA256:**
`3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953`

## Verdict

**PASS / GO in the exact stated scope.**  The source correctly binds the
corrected upper-convexity theorem SHA
`6f8daaba40de9d40c17d429fa4925d4d985d3374fa00d89a5d05651b2529aa11`.
Its one-third anchor, active-side localization, three train estimates,
final rational margin, and KKT boundary collapse all replay exactly.

The older self-audit and freeze manifest bind superseded target/dependency
hashes and are not part of this independent freeze.

## 1. One-third anchor and localization

At `w=A/3`, the three retained adverse exponents are

\[
\pi/9,\qquad4\pi/9,\qquad49\pi/36.
\]

The displayed Taylor majorants and `pi<22/7` give lower Gaussian bounds
`703/1000`, `49/200`, and `1/75`.  Hence

\[
F(A/3)<1-{703\over1000}-{49\over200}-{1\over75}
={29\over750}<{57\over1400}=L.
\]

Since `F` decreases strictly on `[A/4,A/2]`, the closed active condition
`F(v)>=L` forces

\[
v<A/3,\quad\delta>A/3,\quad\tau>4A/3,
\quad P>8A/9,\quad0\le u<A/9.
\]

All inequalities, including the strict endpoint directions, are correct.

## 2. Narrow-band train bounds

The ceiling train increases with the period.  At `tau=4A/3`, the first
tail exponent is `49pi/36`, successive exponent gaps are at least `2pi`,
and the rational Taylor bounds give complete tail `<1/69`.  Therefore

\[
C(\tau)>{881\over10000}-{1\over69}>{73\over1000}.
\]

For `8A/9<=w<=A`, the ratio controlling the compact derivative is

\[
{1+t\over1-t}e^{-\pi t}.
\]

Its logarithmic derivative is positive, and its value at `t=8/9` exceeds
one.  Thus `K` increases on the whole interval.  The compact endpoint and
period-tail ledgers give

\[
F_\tau(w)>{6\over625}-{61\over1000}-{1\over2500}
=-{259\over5000}>-{13\over250}.
\]

Finally `u<A/9<A/4`, and increasing the period makes every negative tail
less adverse, so

\[
F_\tau(u)>F_A(u)>L,
\qquad C(\tau)>L.
\]

Hence the low minimum is strictly greater than `L`.

## 3. Active-side margin

Both upper shifts lie in `[8A/9,A]`.  Combining the three train bounds
with `Gamma<3147/700000` gives

\[
\mathfrak R>
{73\over1000}+{57\over1400}-2{13\over250}
-{3147\over700000}
={3653\over700000}>0.
\]

The proof uses `F(v)>=L`, so it includes the `Gamma` switch itself.

## 4. Boundary collapse and scope

The corrected convexity theorem removes smooth branch `C`; every smooth
branch-`U` interior would have to lie on active `Gamma`; and the present
theorem removes the complete active side.  Therefore any nonpositive
minimum is inactive and lies on the explicitly retained geometric or
low-switch boundary list.  The far endpoint is already excluded, while
`delta=delta_*` is correctly retained because the earlier theorem signs
physical tables rather than this stronger sufficient gate.

No retained inactive boundary is signed here.  Complete six-slot `h=4`
positivity is not claimed.
