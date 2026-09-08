# Exact numeric certificate for the symmetry-descent thresholds

2026-09-08. One bounded deterministic h100 execution by `exact_b_finite_frontier`. All four analytic-envelope comparisons, all 31 stored finite-band cases, the claimed unique maximum, and the quoted dimension-97 entry pass.

This note certifies the numerical inequalities. The general analytic envelope, its monotonicity, the exact construction theorem and the even-dimensional lift are separate proof inputs. No partition census or SAT solver was rerun.

## 1. The four outward-root comparisons

Use exactly

\[
J_r=\frac{3r+49}{3r(r+2)(r+3)}+\frac{43}{72\operatorname{Cat}_r},
\qquad
E_r=2\sqrt{\frac{2J_r}{2r+1}}+
86(r+1)\sqrt r\left(\frac{25}{36}\right)^r.
\]

The script also verifies the alternative displayed decomposition of J_r by exact rational equality.

For each nonnegative rational radicand a/b, put Q=10^{60} and compute an integer q using `isqrt`, adjusting upward if necessary. The two exact integer checks are

\[
(q-1)^2b<aQ^2\le q^2b.
\]

Thus `sqrt(a/b)<=q/Q`, including the perfect-square case. Apply this independently to `2J_r/(2r+1)` and to r. All coefficients multiplying the roots are positive; substituting the upward roots gives a rational U_r≥E_r. The complete numerator/denominator of U_r and both root certificates are retained.

The proved strict chains are:

| r | Rounded-up display of U_r | Exact claimed bound checked | Target |
|---:|---:|---:|---:|
| 45 | 0.009271845429338486 | E_45 < 0.009272 | < 0.01 |
| 163 | 0.000991315300369260 | E_163 < 0.000992 | < 0.001 |
| 741 | 0.000099868373195185 | E_741 < 0.00009987 | < 0.0001 |
| 3424 | 0.000009998021412266 | E_3424 < 0.000009999 | < 0.00001 |

Each comparison is an integer cross multiplication of exact rationals. The report also gives 45-place outward decimal enclosures of U_r. Those are enclosures of the certified upper quantity U_r, not a claim that its lower decimal endpoint is a lower bound for E_r.

## 2. The finite bridge uses the existing exact census

The program reused [the already verified rotation-period census](rotation_period_census_20260908/exact_rotation_period_census.json). Before reading its rows as premises, it checked the file SHA-256 against

`43b52c9d3ed72b9901dc7c6aca96a4ce8f46a12e322fc01c181da1a3412869b2`.

It then checked `125*C_r<W_r` for **all 31 values r=14,...,44**, corresponding to odd dimensions n=29,...,89. No monotonicity of the finite construction ratios was assumed.

The unique maximum is at r=16, meaning dimension n=33, with

\[
W_{33}=1,166,803,110,\quad C_{33}=8,959,232,\quad
N_{33}=1,175,762,342,
\]

\[
\frac{C_{33}}{W_{33}}=rac{4479616}{583401555}
<\frac1{125}<\frac1{100}.
\]

Its exact strict margin `W_33-125*C_33` is 46,899,110. The report retains every individual finite-band row and margin, as well as the exact ratio comparisons establishing uniqueness of the maximum.

Together with an established bound `epsilon_r<=E_r` and the separately proved decrease of E_r for r≥4, these numerical checks supply the finite-to-infinite bridge: the first band covers odd 29 through 89, E_45 starts at odd 91, and the other three envelope thresholds start at odd 327, 1483 and 6849. The exact even lift supplies their next even dimensions and therefore every dimension in each resulting range. This paragraph identifies the proof dependencies; it does not substitute a finite computation for the analytic envelope.

## 3. The quoted dimension-97 entry

The stored n=97 row matches exactly:

\[
\begin{aligned}
W_{97}&=12,738,806,129,490,428,451,365,214,300,\\
C_{97}&=99,533,441,612,804,133,661,134,\\
N_{97}&=12,738,905,662,932,041,255,498,875,434.
\end{aligned}
\]

The exact strict margin for `100000*C_97<W_97` is

\[
2,785,461,968,210,015,085,251,814,300>0.
\]

Its ratio has the outward enclosure

\[
0.000007813404223366230172100460794832272637380
\le C_{97}/W_{97}
<0.000007813404223366230172100460794832272637381.
\]

No word of this enormous length was materialized or scanned in this audit; this is a replay of the already certified exact construction census.

## 4. Reproduction and execution record

- [Reproducible script](verify_symmetry_descent_uniform_threshold_numbers_20260908.py).
- [Full exact certificate](symmetry_descent_thresholds_20260908/symmetry_descent_threshold_numeric_certificate.json).
- [Claim transcription](SYMMETRY_DESCENT_UNIFORM_THRESHOLDS_USER_CLAIMS_20260908.md).
- [Prior census proof and execution record](PBBS_EXACT_ROTATION_PERIOD_PARTITION_CENSUS_THROUGH101_CERTIFICATE_20260908.md).

Remote script: `/home/amodo/verify_symmetry_descent_uniform_threshold_numbers_20260908.py`.
Remote output: `/home/amodo/exact-b-symmetry-descent-thresholds-20260908/`.

The one run asserted the h100 hostname, enforced 30 CPU seconds, 45 wall seconds and 512 MiB address space, and returned PASS in approximately 0.084 seconds. The only floating-point value in the certificate is descriptive elapsed time. All mathematical claims use integers, exact fractions, and independently checked upward integer square roots.

Certificate SHA-256:

`acd7d2c2cfc8c067198c3e227c4011de09d32a28df79c41289c0da6fb337ebb4`.

The current k17 literal record and the unresolved SAT-proof capture issue are unchanged by this numerical task.
