# Self-audit: complete six-slot `h=4` literal rectangle positivity

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_SIX_SLOT_H4_LITERAL_RECTANGLE_COMPLETE_POSITIVITY_20260804.md`  
**Target SHA-256:**
`34b4c57f4f917fed9dbed8c455f0b8bf279183dfdee8f66073ccd16b7dc6dfba`  
**Verdict:** **SELF-AUDIT GO.**  The two uniform train banks, their domain
coupling, both low branches, and the physical implication replay exactly.
This is not an independent audit.

## 1. Upper bank

The frozen `u=0` proof gives, after period reduction to `tau_0`, two
exhaustive normalized ranges.

For `w/A<=17/20`,

\[
 F_\tau(w)>-{51\over1000}-{9\over4000}
 =-{213\over4000}.
\]

For `w/A>=17/20`,

\[
 F_\tau(w)>-{13\over250}-{1\over800}
 =-{213\over4000}.
\]

Thus the upper floor applies uniformly to every
`2tau/3<=w<=A`.  The companion bound

\[
                         C(\tau)+F_\tau(w)>{11\over20000}
\]

is the exact main conclusion of the same theorem.

## 2. Low bank

The domain-wide upper bound `u<=A/5` follows by splitting at `P=4A/5`:
use `u<=P/4` below and `u<=A-P` above.

The period-uniform critical-point theorem implies that the minimum of
`F_tau` on `[0,A/5]` occurs at an endpoint.  At zero,

\[
 C(\tau)>{881-343\over10000}={269\over5000}.
\]

At `A/5`, the compact price is `>9/125`.  The first period-tail argument
exceeds `201779/100000`, whose square is `>4071/1000`; the first tail is
`<1/57`.  Successive ratios are `<1/60`, so

\[
 \text{tail}<{20\over1121}<{9\over500}.
\]

Therefore

\[
 F_\tau(A/5)>{9\over125}-{9\over500}
 ={27\over500}>{269\over5000}.
\]

This proves the low floor on the complete domain.

## 3. Cross-bank margin

The domain also gives

\[
 {2\tau\over3}\le P\le P+u\le A.
\]

Thus the low and upper floors apply simultaneously, with exact surplus

\[
 {269\over5000}-{213\over4000}
 ={1076-1065\over20000}
 ={11\over20000}.
\]

This is the physical correlation that the earlier independent envelopes
discarded.

## 4. Inactive gate

If the low minimum is `C(tau)`,

\[
 \mathfrak R=H_\tau(P)+H_\tau(P+u)-{1\over20000}
 >{21\over20000}.
\]

If it is `F_tau(u)`,

\[
 \mathfrak R
 =H_\tau(P)+F_\tau(u)+F_\tau(P+u)-{1\over20000}
 >{21\over20000}.
\]

The branch switch is included.  No KKT or boundary assumption remains.

## 5. Active gate and physical scope

The active predecessor, including its switch, has margin

\[
 {3653\over700000}>{21\over20000}.
\]

Hence the residual rectangle has uniform margin `21/20000` everywhere.
The literal reduction has strict inequality `Phi>mathfrak R`, while the
corrected local theorem covers the earlier interval through `delta_*`.
Therefore the stated six-slot inert `h=4` branch is completely positive.

No claim beyond that frozen Bellman branch is inferred.

