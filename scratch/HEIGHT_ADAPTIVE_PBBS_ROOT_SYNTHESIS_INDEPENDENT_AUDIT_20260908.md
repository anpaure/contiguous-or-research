# Independent audit of the assembled height-adaptive PBBS proof

2026-09-08. `exact_b_induction` read the complete
`HEIGHT_ADAPTIVE_PBBS_CONSTRUCTION_20260908.md`, the complete complementary
`PBBS_HEIGHT_ADAPTIVE_FINITE_WORD_AND_RANGE_BOUND_INDEPENDENT_AUDIT_20260908.md`,
and the finite construction certificate and root-owned literal verification
report. This was a pure proof/code-record review; no mathematical program
was executed for this audit.

Verdict: PASS. No mathematical transcription, boundary, or proof-scope
correction is required. This is an internal mathematical review, not
external or formal certification.

## Exact witness borders

With `D_i = intersection_(j=0)^h X_(i+j)`, a finite positive owner run
`[a,b]` of length at least `h+1` gives precisely the positive D run
`[a,b-h]`. Consequently an intersection of `p <= h+1` owners starting
at `i` is the union of the D letters from `i+p-1-h` through `i`, inclusive.
The corresponding union of `p` owners uses D indices `i-h` through
`i+p-1`.

For a nonempty rank-`r-q` lower target, the strict corridor gives `q+2`
interleaved owners at the same height `h >= q+1`. The literal lower
witness therefore has `h-q >= 1` letters. For the complementary upper
target, `q+1` direct owners require `h+q+1 <= 2h` letters. The case `q=0`
and the smallest dimension `r=1` satisfy these same formulas. Permanent
positive or negative coordinates satisfy the erosion identities too.

The physical equality-edge potential proves `n | v` for each actual
labelled g-cycle. Thus `v >= n = 2r+1 > 2h`, and copying exactly `2h-1`
letters after one period supplies every possible crossing witness above.
All joins are ordinary concatenations; the full-ground target follows
from the already supplied singleton witnesses.

## Counting, thresholds, and scope

The finite reflection identity is exactly
`sum_A range(A) = 2^n-W_r`. Combined with positive charge `2h-1`,
period `v >= n`, and `h(A) <= range(A)`, it gives the stated floor
`floor((2^(n+1)-3W_r)/n)`. The even formula retains the correct doubled
floor. The more precise asymptotic upper envelope and the stated
`O(W(k)/sqrt(k))` gap to the established lower bound are consistent.

The displayed subtraction for `e_r-e_(r+1)` is correct, including its
separate `r=1` check. The exact finite signs recorded at `r=283,284` and
`r=31115,31116`, followed by the parity lift, give thresholds `569` and
`62233` for all larger dimensions. No minimality assertion about the
unknown optimum is made.

The executed report
`witnesses/k17_upper24957/literal24957_verification.json` records length
24957, all 131071 targets, and 131071 independently re-evaluated ordinary
interval witnesses. Its input checksum matches the synthesis and the
construction certificate. The construction accounting
`24310+2*519-146=25202`, shortened length `24310+519=24829`, and repair by
128 explicitly listed targets all match. The improvements `417` and
`788`, and remaining gap `644` above 24313, are correct. The different
unprovided user count is distinguished from this executed certificate.

The strict-height argument and height preservation are user-supplied
advances independently proved in the separate audit. The complete proof
explicitly identifies its retained finite PBBS inputs and does not rely
on the earlier probabilistic asymptotic claims. It correctly leaves
exact equality unresolved.

The residence margin can additionally be sourced directly to
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md:1383`, Theorem 16.1, as well
as to the finite marked-step derivation displayed in the synthesis.
