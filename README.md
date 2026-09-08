# Universal contiguous-subarray OR words

**Exact optima are verified through dimension 22. The first unresolved dimension is 23.**
The latest supplied words prove

\[
\nu(21)=352719,\qquad \nu(22)=705435.
\]

Both words passed independent exhaustive ordinary-interval checks and attain
proved endpoint lower bounds. Start with the
[21/22 optimality and cyclic 21 certificate](K21_K22_OPTIMAL_AND_CYCLIC21_VERIFIED_20260909.md),
the [independent forward certificate](scratch/K21_K22_OPTIMAL_INDEPENDENT_FORWARD_CERTIFICATE_20260909.md),
or the [word inventory and hashes](answers/README.md).

For a word of nonzero `k`-bit integer masks, take the bitwise OR of every
contiguous subarray. The minimum length that realizes all `2^k-1` nonzero
masks is `nu(k)`. Intervals are ordinary, without wraparound, unless a
result is explicitly labeled cyclic. If the zero mask is also required,
the minimum is `N(k)=nu(k)+1`.

## Exact finite results

Every value below equals the proved lower bound `B(k)` and has a retained
optimal word. The `k=0` value uses the empty word.

| k | Exact nu(k) | Word |
|---:|---:|---|
| 0 | 0 | Empty word |
| 1 | 1 | [k01.word](answers/k01.word) |
| 2 | 2 | [k02.word](answers/k02.word) |
| 3 | 4 | [k03.word](answers/k03.word) |
| 4 | 7 | [k04.word](answers/k04.word) |
| 5 | 12 | [k05.word](answers/k05.word) |
| 6 | 21 | [k06.word](answers/k06.word) |
| 7 | 37 | [k07.word](answers/k07.word) |
| 8 | 72 | [k08.word](answers/k08.word) |
| 9 | 128 | [k09.word](answers/k09.word) |
| 10 | 254 | [k10.word](answers/k10.word) |
| 11 | 465 | [k11.word](answers/k11.word) |
| 12 | 926 | [k12.word](answers/k12.word) |
| 13 | 1,719 | [k13.word](answers/k13.word) |
| 14 | 3,434 | [k14.word](answers/k14.word) |
| 15 | 6,438 | [k15.word](answers/k15.word) |
| 16 | 12,873 | [k16.word](answers/k16.word) |
| 17 | 24,313 | [k17_optimal24313.word](answers/k17_optimal24313.word) |
| 18 | 48,623 | [k18_optimal48623.word](answers/k18_optimal48623.word) |
| 19 | 92,381 | [k19_optimal92381.word](answers/k19_optimal92381.word) |
| 20 | 184,759 | [k20_optimal184759.word](answers/k20_optimal184759.word) |
| 21 | 352,719 | [k21_optimal352719.word](answers/k21_optimal352719.word) |
| 22 | 705,435 | [k22_optimal705435.word](answers/k22_optimal705435.word) |

The next targets are **proved lower bounds only**:

| k | B(k), the conjectured optimum | Status |
|---:|---:|---|
| 23 | 1,352,082 | Open; no upper word claimed here |
| 24 | 2,704,159 | Open; no upper word claimed here |

Separate cyclic certificates establish `mu(19)=92378` and
`mu(21)=352716`, where `mu` permits intervals wrapping around a cyclic
word. See the [19/20 record](K19_K20_OPTIMAL_AND_CYCLIC19_VERIFIED_20260909.md)
and [21/22 record](K21_K22_OPTIMAL_AND_CYCLIC21_VERIFIED_20260909.md).
These also document the corresponding verified periodic-core lifts.

## The lower bound and the all-dimension conjecture

For `k>=1` and each rank `s`, put

\[
m_s=\binom{k}{s},\qquad
L_s=\sum_{j=1}^{s-1}\binom{k}{j},\qquad
\tau_s=\min\left\{t\in\mathbb Z_{\ge0}:
L_s\le t m_s+\frac{t(t+1)}2\right\}.
\]

The endpoint-count argument gives

\[
\nu(k)\ge B(k):=\max_{1\le s\le k}(m_s+\tau_s),
\qquad B(0)=0.
\]

For the dimensions tabulated above, the middle-rank calculation attains
this maximum; the latest certificates check every rank with exact integers.
The [monotone-deadline proof](MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md)
explains the endpoint argument. The remaining conjecture is

\[
\boxed{\nu(k)=B(k)\text{ for every }k.}
\]

The verified finite cases do not prove this for all dimensions. An
asymptotic formula `nu(k)=(1+o(1))W(k)`, with
`W(k)=binom(k,floor(k/2))`, also does not imply exact finite equality.

## Asymptotic proofs and review package

[ASYMPTOTIC_BOUNDS.md](ASYMPTOTIC_BOUNDS.md) is the current ledger of
leading coefficients, quantitative rates, explicit thresholds and
outstanding finite certificate bands. It separates the later
height-adaptive PBBS deductions, with their retained mathematical inputs,
from the earlier clock/renewal manuscript.

The original coefficient-one publication materials remain available:

- [Proposed proof manuscript](COEFFICIENT_ONE_PROOF_20260908.md).
- [Construction companion](COEFFICIENT_ONE_CONSTRUCTION_20260908.md).
- [Full unabridged review text](review/COEFFICIENT_ONE_REVIEW_20260908/FULL_PROOF_TEXT.md).
- [Review-package README and dependency scope](review/COEFFICIENT_ONE_REVIEW_20260908/README.md).
- [Downloadable review ZIP](review/COEFFICIENT_ONE_REVIEW_20260908.zip).

**Review status:** the coefficient-one manuscript is a proposed proof
with internal AI-agent reviews. It is not claimed to have external human
peer review or formal proof-assistant verification. The later asymptotic
results retain the hypotheses and review status stated in the ledger.
Internal `PASS` labels are not external certification. Exhaustive finite
word checks certify the named finite words; they do not verify an
asymptotic theorem.

The review package is a dated September 8 snapshot with stated external
theorem dependencies. Its older finite-status passages, and those in the
original construction companion, are historical. Use the current finite
table and linked literal certificates for today's exact answers.

## Historical upper bounds

The supplied 21/22 improvements are preserved as superseded constructions:

| Dimension | Verified progression |
|---:|---|
| 21 | [353,297](answers/k21_upper353297.word) → [353,094](answers/k21_upper353094.word) → [352,862](answers/k21_upper352862.word) → **[352,719, exact](answers/k21_optimal352719.word)** |
| 22 | [706,594](answers/k22_upper706594.word) → [706,188](answers/k22_upper706188.word) → [705,724](answers/k22_upper705724.word) → **[705,435, exact](answers/k22_optimal705435.word)** |

Earlier words, failed approaches and superseded numerical bounds remain
in the record for provenance. They do not replace the current exact
values. The [answers README](answers/README.md) and
[finite comparison](FINITE_BOUNDS_K18_K19_K20_20260908.md) link their
individual verification scopes and hashes.

## Repository guide

- [answers/](answers/README.md): literal words, hashes, exact values and historical upper bounds.
- [MASTER_HANDOFF.md](MASTER_HANDOFF.md): authoritative current status, proved interfaces and unresolved gates.
- [RESEARCH_INDEX.md](RESEARCH_INDEX.md): navigation through proofs, certificates and the current frontier.
- [ASYMPTOTIC_BOUNDS.md](ASYMPTOTIC_BOUNDS.md): asymptotic results and finite approximation guarantees.
- [MATHEMATICAL_HANDOFF.md](MATHEMATICAL_HANDOFF.md): chronological research history; later explicit corrections supersede older claims.

Each computational certificate records its source, fixed inputs, resource
limits, checks and retained witnesses. Follow those records for
reproduction rather than treating a historical status statement or a
filename as a correctness certificate.
