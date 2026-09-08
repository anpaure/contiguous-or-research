# Audit: proposal-first fresh-macro rain and the unit-intensity barrier

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_PROPOSAL_FIRST_FRESH_MACRO_RAIN_GIVES_COMPANION_CE_20260805.md`  
**Method:** independent symbolic scale and quantifier audit; no computation

## 1. One-point normalization

The total fractional weight of the `h`-orbit is `lambda_h M/d`, and every
macro has `h` marked level-two occurrences.  Since the marked occurrence
space has size `Wr`, its marginal is

\[
 {M\over dWr}(2\lambda_2+3\lambda_3)
 ={M\over dWr}{Wd\over M(d+1)}
 ={1\over r(d+1)}.
\]

This is exactly the required scale `H/(Wr)` before the harmless integral
rounding of `H`.

## 2. Same-macro codegree

For a fixed marked occurrence, the first prescribed companion fixes both
the common kernel and one private tail.  The full choice count is at least

\[
 {r-1\choose d-2}{k-r\choose d-2}.
\]

Once that companion is fixed, the third copy has at least

\[
 N_*={k-r-(d-2)\choose d-2}
\]

fresh tails.  There are at most two labelled companion roles.  Hence
`kappa_*=2/N_*` is a safe common upper bound for every additional member
of a prescribed cluster.  Since
`k-r=Theta(d^2)`, its logarithm is `-Theta(d log d)`.

## 3. Exact-partition union bound

For every block of the prescribed partition, choose the proposal which
will contain it.  Exactness requires different proposals for different
blocks.  Summing only over distinct proposals and then dropping that
restriction is bounded by the product of the blockwise proposal masses.
Independent Bernoulli proposals therefore give

\[
 \prod_{A\in\pi}\eta_*\kappa_*^{|A|-1}
 =\eta_*^{|\pi|}\kappa_*^{m-|\pi|}.
\]

Every retained event is a subevent of this proposal event.  Arbitrary
deletion, including bank exclusion after the banks are fixed, is therefore
safe.

## 4. Shared-mark scale

For `m=O(d)` and aperture `a=Theta(d^2)`,

\[
 {m^2a\kappa_*\over\eta_*}
 =\operatorname{poly}(d)\exp[-\Theta(d\log d)]=o(1).
\]

Thus the shared-mark partition expansion really does recover `(C2)` from
`(CE)` without an additional asymptotic factor.

## 5. Coverage scope

The proposal theorem is **not** a near-perfect matching theorem.  At one
lower resource, the complete fractional orbit has total proposal intensity
one.  Because the largest atom tends to zero, the probability of no
proposal is `e^{-1+o(1)}`.  An independent rain needs intensity
`log d+O(1)` to reduce this to `O(1/d)`, and the monotone union bound then
has one-point parameter `Theta(log d)eta_*`.

Therefore the theorem closes only the local cluster ledger and its
preservation under a unit-budget alteration.  It correctly leaves open a
spread dependent rounding or an acceptance-aware nibble.  No current
fresh-path packing theorem supplies that missing distribution.

## 6. Verdict

**PASS with the unit-total-intensity scope binding.**  The cluster count,
bank monotonicity, exact-partition argument, and coverage obstruction are
proof-safe.  It would be invalid to cite the theorem alone as an integral
macro selector or as an unconditional proof of `(C2)` for a near-perfect
macro packing.

