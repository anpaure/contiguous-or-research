# Self-audit: inactive quarter boundary

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_SIX_SLOT_H4_INACTIVE_QUARTER_BOUNDARY_COMPLETE_POSITIVITY_20260804.md`  
**Target SHA-256:**
`60ebf810ad63bafd01fa19661780fad8a0fc1a52c2266f1a58995cc5fe635dc1`  
**Verdict:** **SELF-AUDIT GO.**  The geometry, both train prices, and both
low-branch ledgers replay exactly.  This is not an independent audit.

## 1. Geometry

On `u=P/4`, the second upper constraint gives `P<=4A/5`.  Together with
`P>=2tau/3`,

\[
 \tau\le6A/5,
 \quad \tau/6\le u\le A/5,
 \quad 5\tau/6\le P+u\le A.
\]

Thus both upper shifts are legal inputs to the frozen `H` theorem.

## 2. Low train

On `[A/6,A/5]`, the compact kernel decreases, so its minimum is at
`A/5`.  The two exponential prices give

\[
 K(A/5)>1-{121\over200}-{323\over1000}
 ={9\over125}.
\]

The first period-tail argument exceeds `239953/120000`; its square is
`>1999/500`.  The first tail is `<1/54`, and successive ratios are
`<1/60`.  Hence

\[
 \text{tail}<{10\over531}<{19\over1000}.
\]

Therefore

\[
 F_\tau(u)>{9\over125}-{19\over1000}={53\over1000}.
\]

## 3. Upper train

The upper shift satisfies `(P+u)/A>17/20`, so the authenticated compact
bound is `K(P+u)>-13/250`.  The first period-tail argument exceeds
`316301/120000`; its square is `>6947/1000`.  The first tail is
`<1/1030`, and the ratio is `<1/100`, giving complete tail `<1/1000`.
Thus

\[
 F_\tau(P+u)>-{13\over250}-{1\over1000}
 =-{53\over1000}.
\]

The low and upper prices are strict, so their sum is strictly positive.

## 4. Gate ledger

If the low minimum is `C(tau)`, the gate is the sum of two `H` terms less
one epsilon:

\[
 \mathfrak R>{11+11-1\over20000}={21\over20000}.
\]

If the low minimum is `F_tau(u)`, then

\[
 \mathfrak R
 =H_\tau(P)+F_\tau(u)+F_\tau(P+u)-{1\over20000}
 >{10\over20000}={1\over2000}.
\]

The second is the uniform margin.  The active predecessor supplies the
other side and the switch.

## 5. Scope

Only the full `u=P/4` face is claimed.  No conclusion is drawn for the
moving `P=2tau/3` face or the free low-branch switch.

