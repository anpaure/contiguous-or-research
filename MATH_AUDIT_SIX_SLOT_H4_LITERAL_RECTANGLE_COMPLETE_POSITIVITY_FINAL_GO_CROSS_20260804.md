# Final cross-audit: complete six-slot `h=4` literal-rectangle positivity

**Date:** 2026-08-04  
**Method:** independent symbolic checking of the domain reductions, Gaussian
train ledgers, both inactive minimum branches, the active predecessor, and the
physical closure chain.  No search, solver, sampled computation, or numerical
optimization was used.

**Audited theorem:**
`MATH_THEOREM_SIX_SLOT_H4_LITERAL_RECTANGLE_COMPLETE_POSITIVITY_20260804.md`,
SHA256
`34b4c57f4f917fed9dbed8c455f0b8bf279183dfdee8f66073ccd16b7dc6dfba`.

## 0. Verdict

**FINAL GO.**  The theorem is valid at the frozen bytes above.  Its domain
implications are exhaustive, both train banks have the advertised strict
floors, both inactive low branches have the exact margin `21/20000`, and the
closed active theorem is strictly stronger.  Together with the literal
physical reduction and the corrected initial interval, this closes the
complete canonical six-slot inert `h=4` branch, with exactly the scope caveat
stated in the theorem.

## 1. Domain audit

The rectangle constraints are

\[
 {2\tau\over3}\le P\le A,
 \qquad 0\le u\le\min\{A-P,P/4\}.
\]

If `P<=4A/5`, then `u<=P/4<=A/5`.  If `P>=4A/5`, then
`u<=A-P<=A/5`.  These two closed cases exhaust the domain and agree at
`P=4A/5`.  Also `u>=0` and `u<=A-P` give

\[
 {2\tau\over3}\le P\le P+u\le A.
\]

Thus the low shift lies in `[0,A/5]`, while both upper shifts lie in the
common train-bank interval `[2tau/3,A]`.  No boundary point, including
`u=0`, `P+u=A`, or `P=4A/5`, is lost.

## 2. Upper train bank

For fixed admissible `w`, increasing `tau` increases every positive-period
term, because `q tau+w>A` for `q>=1` and the Gaussian tail branch of `K` is
strictly increasing.  Moreover, admissibility at `tau>=tau_0` implies
admissibility at `tau_0`.  The two compact/tail ledgers from the frozen
inactive-`u=0` theorem therefore give

\[
 -{51\over1000}-{9\over4000}
 =-{204+9\over4000}
 =-{213\over4000}
\]

on the lower range and

\[
 -{13\over250}-{1\over800}
 =-{208+5\over4000}
 =-{213\over4000}
\]

on the upper range.  Hence, uniformly,

\[
                         F_\tau(w)>-{213\over4000}.
\]

The same frozen theorem supplies

\[
 C(\tau)+F_\tau(w)>{11\over20000}
\]

on exactly the same interval, so both upper-bank uses in the final proof are
within scope.

## 3. Low train bank

The period-uniform critical-point theorem applies because
`tau>=tau_0>A`; it says every interior critical point of `F_tau` on
`[0,A/2]` is a strict local maximum.  Therefore the minimum on
`[0,A/5]` is attained at `0` or `A/5`.

At zero, the ceiling ledger is

\[
 C(\tau)>{881\over10000}-{343\over10000}
 ={538\over10000}={269\over5000}.
\]

At `A/5`, the frozen compact price gives `K(A/5)>9/125`.  The rational
input bounds imply

\[
 A+\tau+{A\over5}
 \ge {11A\over5}+\delta_*
 >{201779\over100000}.
\]

Indeed, the cited lower bounds `A>4431/5000` and
`delta_*>1363/20000` add to the displayed rational exactly.  Also

\[
 201779^2=40714764841>40710000000,
\]

so the first squared argument exceeds `4071/1000`.  A positive Taylor
partial sum gives `e^4>54`; consequently

\[
 e^{4071/1000}=e^4e^{71/1000}
 >54\left(1+{71\over1000}\right)>57.
\]

For successive terms, the smallest squared-argument gap is

\[
 A\left(2\cdot{11A\over5}+A\right)
 ={27A^2\over5}={27\pi\over20}.
\]

Using `pi>333/106`, this exponent is larger than
`8991/2120=4+511/2120`; hence

\[
 e^{27\pi/20}>54\left(1+{511\over2120}\right)>60.
\]

Thus the complete adverse period tail is strictly smaller than

\[
 {1/57\over1-1/60}={20\over1121}<{9\over500},
\]

where the last comparison is `10000<10089`.  It follows that

\[
 F_\tau(A/5)>{9\over125}-{9\over500}
 ={27\over500}>{269\over5000}.
\]

Both endpoint values exceed the claimed floor, so

\[
                         F_\tau(u)>{269\over5000}
 \qquad(0\le u\le A/5).
\]

## 4. Cross-bank and inactive-branch audit

Combining the low and upper banks gives the exact strict margin

\[
 F_\tau(u)+F_\tau(P+u)
 >{269\over5000}-{213\over4000}
 ={1076-1065\over20000}={11\over20000}.
\]

There are exactly two values of the minimum in the rectangle gate.

If it selects `C(tau)`, then

\[
 \mathfrak R
 =H_\tau(P)+H_\tau(P+u)-{1\over20000}
 >{21\over20000}.
\]

If it selects `F_tau(u)`, then

\[
 \mathfrak R
 =H_\tau(P)+\{F_\tau(u)+F_\tau(P+u)\}-{1\over20000}
 >{21\over20000}.
\]

At the low-branch tie both identities agree, so there is no omitted
nonsmooth case.  This proves the claimed strict sign on the complete
inactive side.

## 5. Active dependency and total rectangle

The frozen active theorem applies to the same literal gate on the closed
side

\[
 F((A-\delta)/2)\ge {57\over1400},
\]

including equality at the switch, and proves

\[
 \mathfrak R>{3653\over700000}.
\]

The comparison with the inactive margin is exact:

\[
 {3653\over700000}-{21\over20000}
 ={3653-735\over700000}
 ={1459\over350000}>0.
\]

The strict inactive side and closed active side exhaust all values of the
switch function.  Therefore

\[
                         \mathfrak R>{21\over20000}>0
\]

on the whole closed rectangle domain.

## 6. Physical closure and scope

For every residual physical inert table, the frozen literal correlated
reduction gives `Phi>mathfrak R`; hence `Phi>0` for
`delta_*<delta<A/2`.  The corrected initial-interval theorem, together
with its exact two-gate predecessor, gives positivity for
`0<delta<=delta_*`; the threshold `delta=0` is already closed by the
endpoint predecessor.  Formal closed-domain endpoints used in the compact
gate proof introduce no uncovered physical case.

Thus every canonical six-slot size-four-efficient inert table has strictly
positive Bellman functional.  This does not imply arbitrary-grid Bellman
positivity, an all-`n` theorem, or an OR-word upper bound.

## 7. Frozen dependency verification

Each direct dependency exists at exactly the SHA256 declared by the audited
theorem:

| role | SHA256 |
|---|---|
| literal correlated reduction | `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd` |
| active-`Gamma` positivity | `3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953` |
| inactive `u=0` theorem | `ba327b06397a9190de23c62c6a0ca0f985bbb75bff12188540518550e03ecd8f` |
| quarter compact endpoint price | `60ebf810ad63bafd01fa19661780fad8a0fc1a52c2266f1a58995cc5fe635dc1` |
| corrected initial interval | `badc46480b85ef794e784ca2f62273aa6258cdf3dcfecbd915553102c6acd6af` |
| period-uniform critical-point theorem | `f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3` |
| compact Gaussian prices | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |

The audited theorem itself remains unchanged at SHA256
`34b4c57f4f917fed9dbed8c455f0b8bf279183dfdee8f66073ccd16b7dc6dfba`.
