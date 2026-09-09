# Asymptotic bounds and finite approximation guarantees

Updated **2026-09-09**. Write \(W(k)=\binom{k}{\lfloor k/2\rfloor}\).
Exact equality \(\nu(k)=B(k)\) is separately verified through dimension 22;
equality for every dimension remains open. A vanishing relative error
does not mean an additive error of zero.

The public conditional proof, explicit finite hypotheses, numerical
certificate values and verification limits are consolidated in
[MASTER_HANDOFF.md, Appendix J](MASTER_HANDOFF.md#conditional-asymptotic-bounds).
Internal independent review and exact arithmetic checks are not external
or proof-assistant certification of those finite hypotheses.

## Strongest written conditional rate

On Appendix J.1's finite construction, corridor, period, pruning and
concentration inputs,
\[
\boxed{\displaystyle
\nu(k)\le W(k)\left(1+
\exp\!\left[-\frac{93}{100}\bigl(k(\log k)^2\bigr)^{1/5}\right]\right)
\quad\text{for every integer }k\ge2^{131073}+1.}
\]
All logarithms are natural. The proof covers all ranks and both parities,
including the explicit onset and finite rounding costs. It estimates the
actual height-adaptive construction, whose normalized collar charge is
\(\mathbb E[(2h-1)/v]\). See Appendix J.H–J.R.

## Proved uniform guarantees

Under the stated finite support inputs, the following hold for **every
integer dimension from the listed start onward**. These are sufficient
starts, not claims of minimality. Appendix J.U–J.N gives the decreasing
analytic envelope and the independently checked finite bridge.

| Start | Upper bound | Relative excess |
|---:|---|---:|
| 29 | \(\nu(k)<1.01W(k)\) | <1% |
| 327 | \(\nu(k)<1.001W(k)\) | <0.1% |
| 1,483 | \(\nu(k)<1.0001W(k)\) | <0.01% |
| 6,849 | \(\nu(k)<1.00001W(k)\) | <0.001% |

## Finite checks and unverified bands

Appendix J.S separates checks at specific dimensions from uniform starts:

- The exact census through odd dimension 101 and even lifts certifies
  the finite bands 29–102, 57–102, 87–102 at 1%, 0.1%, 0.01%, respectively.
- Independently generated prefix certificates give 137/138 below 0.001%
  and 327/328 below 0.01%. These isolated checks do not extend those bounds
  to every later dimension.
- The three exact harmonic certificates give errors below
  \(10^{-330},10^{-950},10^{-2600}\) at the pairs
  \(2\cdot10^{12}+1,+2\), \(2\cdot10^{14}+1,+2\), and
  \(2\cdot10^{16}+1,+2\), respectively. Only those parameter choices
  were evaluated; no enormous literal word was generated.

The **user-reported uniform starts 57/87** still require the complete
713-case forward-prefix band. The **user-reported uniform start 137**
still requires the complete 3,356-case moment-prefix band. Their methods
passed internal proof review, but these complete bands were not
independently replayed here. The established uniform starts therefore
remain 29, 327, 1483 and 6849.

## Earlier coefficients and scope

Appendix J.S records the comparison with earlier routes. The 0.93 rate
supersedes the 0.6 depth-product rate on the same stated domain. The
self-contained older proof in master Appendix A.7 gives coefficient
1.180703803847…; the selective 1.177987 result was internally reviewed and
numerically reproduced. The user-submitted 1.15325 claim remains unaudited
in the recorded continuation. The earlier clock/renewal coefficient-one
manuscript remains a proposed internally reviewed route, distinct from
Appendix J's finite hypotheses.

Even the strongest relative bound leaves a potentially large additive
gap. The native construction's exponential collar-cost barrier limits
that construction; it is not a lower bound on unrestricted
\(\nu(k)-B(k)\).
