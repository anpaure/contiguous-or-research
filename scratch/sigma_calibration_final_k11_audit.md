# Independent audit of the exact `k=11`, length-465 word

Date: 2026-07-27

Immutable input audited:

- `scratch/sigma_sat_k11_465.word`
- SHA-256:
  `746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850`

No file in the final certificate was modified.

## 1. Exact optimality

For `k=11`, put `r=6`.  Then

\[
W=\binom{11}{6}=462,
\qquad
\Lambda=\sum_{j=1}^{5}\binom{11}{j}=1023.
\]

Depth 2 has capacity

\[
2W+\binom32=927<1023,
\]

whereas depth 3 has capacity

\[
3W+\binom42=1392\ge1023.
\]

Thus the proved deadline lower bound gives

\[
\nu(11)\ge W+3=465.
\]

The final file contains exactly 465 nonzero masks.  Two independent
verification algorithms give

\[
\#\{\text{nonempty masks realized as contiguous ORs}\}=2047=2^{11}-1.
\]

Therefore

\[
\boxed{\nu(11)=465=B(11).}
\]

The two independent checks were:

1. the nested-interval exhaustive audit in
   `scratch/sigma_calibration_harness.cpp` (108,345 intervals);
2. the suffix-state dynamic program in `verify_or_suffix.cpp`, independently
   compiled as `scratch/sigma_calibration_verify_or_suffix`.

Both report zero missing masks in every rank.

Before Boolean labeling, the exact short-cell Hall audit was run on all 242
safe cuts of the cap-2 middle certificate.  Every one of the 242 flat-delay-3
compatibility graphs has matching number 1023, i.e. Hall deficiency zero.
The q369 schedule does not share this property (deficiencies 4 through 9).
Thus the flat schedule is not a cosmetic choice: it is the schedule that
removes the final integral obstruction.

## 2. Exact lower-bound equality ledger

The lower compiler has 1,392 short cells and every one has rank below 6.
Those cells contain all 1,023 lower masks, with duplicate excess exactly 369:

\[
1392=1023+369.
\]

This is exactly the equality decomposition predicted by the monotone-deadline
lower bound.  There is no depth loss; the entire positive slack is realized
as repeated lower masks.

The entries themselves have rank profile

\[
1^{11}\,2^{55}\,3^{399},
\]

with distinct profile

\[
1^{11}\,2^{55}\,3^{165}.
\]

So every singleton, every pair, and every triple already occurs literally as
an entry.  The remaining 234 entries repeat triples in exactly the pattern
needed to make the central and upper geometry work.

## 3. Middle sigma geometry

Every one of the 462 windows of length 4 has rank 6, and they form a
permutation of all six-sets.  All 461 path steps are Johnson edges.

Path shadow summary:

| depth | lower holes | upper holes |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 1 | 0 |
| 3 | 0 | 0 |
| 4 | 0 | 0 |
| 5 | 0 | 0 |

The path closes to a genuine Johnson cycle.  Cyclically, both lower depths 1
and 2 are complete, and all deeper lower and upper supports are complete as
well.

At q=1 the cyclic upper profile is exactly

\[
1^{198}2^{132};
\]

after the safe cut it becomes

\[
1^{199}2^{131}.
\]

Thus the upper load cap is 2, the integrality-optimal profile.

The cyclic residence minimum is exactly 4, matching `d+1`; there are no
linear or cyclic residence violations.  The chosen boundary is a safe cut:
the omitted lower colour is precisely the closing intersection, while upper
coverage survives.

## 4. Comparison with the exact `k=5,7,9` words

| k | B(k) | fixed middle row? | lower-ledger loss | q1 lower/upper holes | q2 lower/upper holes | residence |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 12 | no | 7 wrong-rank + 1 repeat = 8 | n/a | n/a | n/a |
| 7 | 37 | yes | 10 repeats = 10 | 1 / 0 | 1 / 0 | min run 3 |
| 9 | 128 | yes | 0 | 1 / 0 | 1 / 0 | min run 3 |
| **11** | **465** | **yes** | **369 repeats = 369** | **1 / 0** | **1 / 0** | **min run 4** |

Entry profiles (`occurrences/distinct masks`) are:

- `k=5`: `1:5/5, 2:7/7`;
- `k=7`: `1:8/7, 2:29/21`;
- `k=9`: `1:9/9, 2:36/36, 3:83/83`;
- `k=11`: `1:11/11, 2:55/55, 3:399/165`.

The persistent odd-k signature is now exact at three consecutive nontrivial
sizes: a flat middle permutation, one lower boundary hole at q=1 and q=2,
complete upper shadows, and residence at the deadline scale.  The `k=11`
solution is stronger than the displayed `k=7,9` solutions because its middle
path also closes to a safe, cap-2 cyclic sigma factor.

## 5. Runtime

The full structural harness, including exhaustive OR coverage and every
shadow/residence statistic, verifies `k=11` in below 0.01 seconds in a single
run.

To include process-startup overhead, 200 separate harness invocations took:

| k | total wall time | wall time per invocation |
|---:|---:|---:|
| 5 | 0.27 s | 1.35 ms |
| 7 | 0.27 s | 1.35 ms |
| 9 | 0.30 s | 1.50 ms |
| 11 | 0.36 s | 1.80 ms |

For the smaller independent suffix verifier, 1,000 separate invocations took
1.36 s, 1.34 s, 1.38 s, and 1.56 s respectively.  Again, executable startup
dominates the actual verification.

## 6. What this establishes and what it does not

This is a complete computer-checkable proof of the previously open finite
case `k=11`, conditional only on the already proved general lower bound.
Together with the existing exact `k<=10` and `k=12` words, the formula
`nu(k)=B(k)` is now verified for every `k<=12`.

It does **not** prove the formula for all `k`.  What it adds to the general
conjecture is unusually strong structural evidence: the exact solution was
found by imposing the equality geometry predicted by the lower-bound proof,
not by unconstrained brute force.
