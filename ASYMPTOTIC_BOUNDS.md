# Asymptotic bounds and finite approximation guarantees

Updated **2026-09-09**. Write

\[
W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]

This page records construction upper bounds relative to W(k). **Exact equality \(\nu(k)=B(k)\) is separately verified through dimension22**, including the [new21/22 literal certificates](scratch/K21_K22_OPTIMAL_INDEPENDENT_FORWARD_CERTIFICATE_20260909.md). Equality for every dimension remains open. A vanishing relative error does not mean that the additive error is zero.

**Proof status.** The height-adaptive results below are internally reviewed deductions from the linked finite PBBS construction, all-rank corridor, particle-return, original pruning-fibre and, where used, concentration lemmas. Their finite arithmetic certificates were independently executed where stated. They are **conditional on those retained mathematical inputs**, not claims of external review or formal verification. The older self-contained proof in the handoff is distinguished below.

## Strongest written rate

On those finite inputs, the strongest recorded bound is

\[
\boxed{\displaystyle
\nu(k)\le W(k)\left(1+
\exp\!\left[-\frac{93}{100}\bigl(k(\log k)^2\bigr)^{1/5}\right]\right)
\quad\text{for every integer }k\ge2^{131073}+1.}
\]

All logarithms are natural. This covers **all ranks and both parities**, and the onset is proved explicitly in the local record, not an unspecified “sufficiently large” condition. The bound implies coefficient one asymptotically, on the stated inputs. [Full harmonic-period proof](HEIGHT_ADAPTIVE_HARMONIC_PERIOD_RATE_20260908.md), [independent probability and parity audit](scratch/PBBS_HARMONIC_PERIOD_FINITE_PROBABILITY_AND_EXPLICIT_POINT_NINETY_THREE_RATE_AUDIT_20260908.md), [exact arithmetic certificate](scratch/HARMONIC_PERIOD_THREE_FINITE_ROWS_AND_INTEGRAL_RATIONAL_CERTIFICATE_20260908.md).

The underlying construction is concrete. In odd dimension n=2r+1 it emits each canonical component's erosion word and a collar of length 2h−1, giving

\[
N_n=W(n)+\sum_{\mathcal C}(2h_{\mathcal C}-1),\qquad
\frac{N_n-W(n)}{W(n)}=\mathbb E\frac{2h-1}{v}.
\]

Here the expectation is over uniform middle states, h is component height and v its period. The ordinary even lift doubles the length and width. The rate estimates this actual word; it does not use the earlier proposed clock/renewal coefficient-one proof. [Finite construction and all-rank support](HEIGHT_ADAPTIVE_PBBS_CONSTRUCTION_20260908.md).

Two useful comparisons are:

| Relative-error bound | Proved sufficient onset | Position in the record |
|---|---:|---|
| \(e^{-(93/100)(k(\log k)^2)^{1/5}}\) | \(2^{131073}+1\) | Strongest current written rate |
| \(e^{-(3/5)(k(\log k)^2)^{1/5}}\) | \(2^{131073}+1\) | Earlier [depth-product bound](HEIGHT_ADAPTIVE_DEPTH_PRODUCT_RATE_20260908.md), superseded on this domain |
| \(e^{-k^{1/5}/128}\) | \(2^{2048}+1\) | Weaker [fresh-prime bound](HEIGHT_ADAPTIVE_FRESH_PRIME_RATE_20260908.md), with a smaller explicit onset |

The fresh-prime proof also gives every fixed coefficient c<9/512 in \(e^{-c k^{1/5}}\), eventually, without the same explicit onset for every c. Earlier [logarithmic-gcd](HEIGHT_ADAPTIVE_LOG_GCD_RATE_20260908.md), [profile-sieve](HEIGHT_ADAPTIVE_PROFILE_SIEVE_RATE_20260908.md), [reverse-profile](HEIGHT_ADAPTIVE_REVERSE_PROFILE_RATE_20260908.md) and [fractional-LCM](HEIGHT_ADAPTIVE_FRACTIONAL_LCM_BOUND_20260908.md) estimates remain archived proof routes; submission order is not strength order.

## Uniform guarantees at smaller dimensions

These sufficient thresholds are proved for **every integer k from the listed start onward**, under the retained finite support inputs:

| Start | Guaranteed bound | Relative excess |
|---:|---|---:|
| 29 | \(\nu(k)<1.01W(k)\) | <1% |
| 327 | \(\nu(k)<1.001W(k)\) | <0.1% |
| 1,483 | \(\nu(k)<1.0001W(k)\) | <0.01% |
| 6,849 | \(\nu(k)<1.00001W(k)\) | <0.001% |

An exact finite bridge is joined to a proved decreasing analytic envelope; the even lift supplies the other parity. These are sufficient starts, not claims of minimality. [Uniform-threshold proof](HEIGHT_ADAPTIVE_UNIFORM_FINITE_THRESHOLDS_20260908.md), [executed rational threshold certificate](scratch/SYMMETRY_DESCENT_UNIFORM_THRESHOLD_EXACT_NUMERIC_CERTIFICATE_20260908.md).

## What has been checked at specific dimensions

The following exact construction-length evaluations do **not** by themselves give uniform starts:

| Checked dimensions | Certified relative bound | Evidence |
|---|---|---|
| 29–102; 57–102; 87–102 | Respectively <1%, <0.1%, <0.01% | [Exact period census through odd dimension101, with even lifts](HEIGHT_ADAPTIVE_EXACT_ROTATION_PERIOD_AND_FINITE_CENSUS_20260908.md) |
| 97,98 | <0.001% | [Verified census row](HEIGHT_ADAPTIVE_UNIFORM_FINITE_THRESHOLDS_20260908.md) |
| 101,102 | <0.0006% (six parts per million) | [Exact period census](HEIGHT_ADAPTIVE_EXACT_ROTATION_PERIOD_AND_FINITE_CENSUS_20260908.md) |
| 137,138 | <0.001% | [Independently generated and fully replayed moment-prefix certificate](HEIGHT_ADAPTIVE_MOMENT_PREFIX_CERTIFICATE_METHOD_20260909.md) |
| 327,328 | <0.01% | [Independently generated and fully replayed forward-prefix certificate](HEIGHT_ADAPTIVE_FORWARD_PREFIX_CERTIFICATE_METHOD_20260908.md) |

The finite harmonic inequality also has three separately executed outward-rational certificates:

| Dimension pair | Relative error below |
|---|---:|
| \(2\cdot10^{12}+1,\ 2\cdot10^{12}+2\) | \(10^{-330}\) |
| \(2\cdot10^{14}+1,\ 2\cdot10^{14}+2\) | \(10^{-950}\) |
| \(2\cdot10^{16}+1,\ 2\cdot10^{16}+2\) | \(10^{-2600}\) |

Only those parameter choices were evaluated. They are individual pairs, not thresholds for all subsequent dimensions. These evaluations count the finite construction's length; they did not materialize enormous literal words. [Complete numerical certificates](scratch/HARMONIC_PERIOD_THREE_FINITE_ROWS_AND_INTEGRAL_RATIONAL_CERTIFICATE_20260908.md).

## Uniform improvements still awaiting their finite bands

The proof methods pass internal review, but the following complete arithmetic bands have **not** been independently replayed here:

| User-reported uniform claim | Outstanding evidence |
|---|---|
| <0.1% for every k≥57; <0.01% for every k≥87 | The [forward-prefix claim](HEIGHT_ADAPTIVE_FORWARD_PREFIX_CERTIFICATE_METHOD_20260908.md) requires 713 finite certificates across r=28–740, with the stated two tolerances. The existing smaller census ranges and the isolated r=163 check do not certify that whole band. |
| <0.001% for every k≥137 | The [moment-prefix claim](HEIGHT_ADAPTIVE_MOMENT_PREFIX_CERTIFICATE_METHOD_20260909.md) requires the 3,356-case band r=68–3423. Only r=68 was independently generated and replayed for this continuation. The claimed predecessor failure/minimality certificate is also outstanding. |

The previously proved decreasing envelope supplies the tail once a complete band is checked. Until then, the established uniform starts remain29,327,1483 and6849. Actual construction ratios need not be monotone.

## Earlier leading coefficients and the exact-equality boundary

All these coefficients refer to the **same full-cube normalization** \(\nu(k)\le(c+o(1))W(k)\):

| Coefficient | Recorded status |
|---|---|
| \(1.180703803847\ldots\) | Complete self-contained proof in [MASTER_HANDOFF.md](MASTER_HANDOFF.md), Appendix A.7; the strongest coefficient in that earlier proof core |
| \(1.177987\) | [Selective-truncation proof and exact certificate](scratch/USER_SELECTIVE_TRUNCATION_PROPOSED_1_177987_20260908.md) internally reviewed and numerically reproduced |
| \(1.15325\) | User-submitted endpoint-optimized claim; its proof/verifier have not been independently audited in the recorded continuation. See the status in [the construction companion](COEFFICIENT_ONE_CONSTRUCTION_20260908.md). |
| \(1\) | Earlier [clock/renewal manuscript](COEFFICIENT_ONE_PROOF_20260908.md) remains a proposed internally reviewed route. The later finite height-adaptive route above supplies quantitative coefficient-one deductions on its separate stated inputs. |

The later coefficient-one bounds are asymptotically stronger than either verified coefficient above one; no finite crossover follows just by comparing those coefficients. Earlier polynomial and superpolynomial estimates of the same construction are retained in [the period-bound record](HEIGHT_ADAPTIVE_PERIOD_BOUNDS_20260908.md).

Even the strongest displayed relative error leaves a potentially large additive gap. Moreover, the unchanged native construction has a proved exponential collar-cost barrier, so sharpening its period estimates alone cannot make it attain B(k). That is a limitation of this construction, not a lower bound on unrestricted \(\nu(k)-B(k)\). [Exact periods and native-construction barrier](HEIGHT_ADAPTIVE_EXACT_ROTATION_PERIOD_AND_FINITE_CENSUS_20260908.md). The separately verified finite optima and the search for an all-k construction must remain distinct from this asymptotic ledger.
