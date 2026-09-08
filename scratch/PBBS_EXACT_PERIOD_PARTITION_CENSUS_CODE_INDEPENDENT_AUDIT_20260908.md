# Independent source review of the exact period partition census

2026-09-08. Read-only code audit by `exact_b_induction`. I read all of
`census_pbbs_exact_rotation_period_partitions_20260908.py`, written by
`exact_b_finite_frontier`, against the proved formulas in
`PBBS_EXACT_TRANSLATED_RETURN_PERIOD_AND_SIGNATURE_MULTIPLICITY_AUDIT_20260908.md`.
No code was executed for this review. Verdict: **PASS; no correction
required**. An execution result remains a separate certificate.

The row counter iterates divisors in increasing order. For each d|p it
counts all length-p compositions fixed by a shift d, with the required
mass divisibility p/d|ell, then subtracts exactly the already counted
proper-divisor least periods. Zero counts are excluded from signature
choices, and the complete row sum is checked against the weak-composition
count. The zero-row and one-slot conventions are explicitly asserted.

The partition generator enumerates every positive nonincreasing
partition of r once. Subtracting each peak count from the remaining
tail gives the next circumference p=2*tail+1. The row mass is the
current peak count minus the next one, with a zero next value at the
bottom. Thus the profiles and their Cartesian row sets have the
required exact correspondence.

The sigma numerator/denominator update adds 1/(nprev*p) exactly and
reduces by its integer gcd after every step. For a row least period d,
e=p/d, so the denominator factor is correctly computed as

    reduced_denominator / gcd(reduced_denominator,e).

The numerator need not appear in this gcd because the fraction is
already reduced. The factor is included for every row, including the
last one-site row.

Factoring a single-choice row into `base_v` and `base_mass` is exact.
Every row with multiple least-period classes remains a separate factor
in `itertools.product`. In particular, distinct signatures with the
same period factor are NOT merged or discarded. Empty branching still
produces one signature, as required. Each signature takes the lcm of
all its denominator factors and the product of all its row counts.

The physical-state multiplier is exactly n. The script checks
divisibility of n*mass by v for every separate signature before adding
its cycle count. This matches the rooted Cartesian bijection and the
orbit-invariance proof; there is no extra row-rotation quotient. It
also checks all periods are odd and multiples of n.

For each complete profile, the signature masses sum to the product
of row composition counts. For each dimension, the accumulated root
count equals the Catalan number and n times that count equals W(n).
The independently aggregated period histogram also accounts for
exactly W(n) physical states. These are useful completeness checks,
not replacements for the enumeration proof.

The collar overhead is summed as (2h-1) per cycle. It is cross-checked
against twice the height sum minus the component count, and against
the height histogram. The saved quoted entries and the independently
known canonical n=17 and n=19 totals are asserted, while the code
does not use those values to generate the census.

All percentage tests use integer inequalities. For even k the exact
trimmed lift is applied to the previous odd dimension, and the script
checks W(k)=2W(k-1) rather than assuming a monotone ratio in k.
The decimal displays are outward rational enclosures formed by integer
division. They do not enter the proof of any threshold.

The script's declared scope is correct: it evaluates the proved
unchanged height-adaptive construction, does not materialize an
astronomical literal word, and does not claim that its construction
length is nu(k). This is internal independent source review, not an
external or proof-assistant certification or a claim that a pending
execution has completed.
