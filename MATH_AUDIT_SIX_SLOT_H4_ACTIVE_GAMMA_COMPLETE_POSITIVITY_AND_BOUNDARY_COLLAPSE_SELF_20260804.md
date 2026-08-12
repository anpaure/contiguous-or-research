# Self-audit: six-slot `h=4` active-`Gamma` positivity and boundary collapse

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_SIX_SLOT_H4_ACTIVE_GAMMA_COMPLETE_POSITIVITY_AND_BOUNDARY_COLLAPSE_20260804.md`  
**Target SHA-256:**
`7c03b815964c30445234a5c19192bcbf23e7d7bb288233a1a159bb193a8830d9`  
**Verdict:** **SELF-AUDIT GO.**  The localization, Gaussian directions,
geometric tails, and final rational margin replay exactly.  This is not
an independent audit.

## 1. Dependency binding

| role | SHA-256 |
|---|---|
| literal correlated rectangle | `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd` |
| corrected upper convexity/KKT pruning | `07bc659e3a1eb6b0dbdab562559d2968de2af6c685d688e0ab6874b598594ff1` |
| compact quarter floor and Gaussian bounds | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |

## 2. One-third anchor

At `w=A/3`, the three retained adverse exponentials are exactly

\[
 e^{-\pi/9},\qquad e^{-4\pi/9},\qquad e^{-49\pi/36}.
\]

The first two come from the compact kernel and the third is the first
period tail.  Every omitted term is adverse, so retaining only these is
an upper bound for `F(A/3)`.

The three rational exponent majorants are

\[
 {\pi\over9}<{22\over63},
 \qquad
 {4\pi\over9}<{88\over63},
 \qquad
 {49\pi\over36}<{539\over126}.
\]

The displayed `U_24` comparisons therefore have the correct direction.
The final arithmetic is

\[
 {703\over1000}+{49\over200}+{1\over75}
 ={2884\over3000},
\]

so

\[
 F(A/3)<{116\over3000}={29\over750}
 <{57\over1400}.
\]

Since `F` is strictly decreasing on `[A/4,A/2]`, `F(v)>=L` forces
`v<A/3`.  The deductions

\[
 \delta=A-2v>A/3,
 \quad \tau>4A/3,
 \quad P\ge2\tau/3>8A/9,
 \quad u\le A-P<A/9
\]

are exact.

## 3. Ceiling tail

At `tau=4A/3`, the first tail exponent is `49\pi/36`; the next exponent
gap is exactly `2\pi`, and later gaps are larger.  The rational lower
bound on `\pi` gives

\[
 {49\pi\over36}>{16317\over3816}>{427\over100}.
\]

Thus the finite positive Taylor certificate gives first tail `<1/70`.
Also

\[
 e^{2\pi}
 >\left({29\over4}\right)^3{1649\over1250}
 ={40217461\over80000}>500.
\]

Hence the full tail is `<1/69`.  The final ceiling comparison has exact
surplus

\[
 {881\over10000}-{1\over69}-{73\over1000}
 ={419\over690000}>0.
\]

## 4. Upper rectangle train

For `t=w/A`, the derivative comparison is controlled by

\[
 r(t)={1+t\over1-t}e^{-\pi t}.
\]

Its logarithmic derivative is at least

\[
 {162\over17}-{22\over7}>0
\]

on `8/9<=t<1`.  At `t=8/9`, `r(t)>1` because
`8\pi/9<14/5` and `e^(14/5)<17`.  Thus `K` is increasing on the whole
needed upper interval.

For `x=\pi/324`, the elementary inequality

\[
 1-e^{-x}>x-x^2/2
 >{199\over200}{157\over16200}>{6\over625}
\]

has the correct direction.  Also

\[
 {289\pi\over324}>{14\over5}
\]

and the degree-eight positive Taylor sum is `>1000/61`, yielding the
adverse compact price `<61/1000`.

For the period tail,

\[
 {841\pi\over324}>8+{3\over20},
 \qquad
 {70\pi\over27}>8+{19\over135}.
\]

The two exact lower products are

\[
 \left({29\over4}\right)^4{23\over20}
 ={16267463\over5120}>3000,
\]

and

\[
 \left({29\over4}\right)^4{154\over135}
 ={108921274\over34560}>3000.
\]

Thus the complete tail is `<1/2999<1/2500`.  The train bound is

\[
 {6\over625}-{61\over1000}-{1\over2500}
 =-{259\over5000}>-{13\over250}.
\]

## 5. Low train and final margin

On the active side, `u<A/9<A/4`.  Since increasing the period makes
each negative tail less adverse,

\[
 F_\tau(u)>F_A(u)>L.
\]

The ceiling bound is also larger than `L`, so the minimum in the gate is
strictly larger than `L`.

Over denominator `700000`, the four contributions are

\[
 51100+28500-72800-3147=3653.
\]

Therefore

\[
 \mathfrak R>{3653\over700000}>0.
\]

The switch `F(v)=L` is included because the proof used the closed
inequality `F(v)>=L`.

## 6. Scope

The preceding KKT theorem eliminates the constant-low smooth interior
and forces every moving-low smooth interior point onto active `Gamma`.
The new sign theorem removes that complete side.  The remaining list is
therefore exactly the inactive geometric/low-switch boundary list, with
`delta=delta_*` retained for the reason stated in the theorem.

No claim is made that those remaining strata are positive.
