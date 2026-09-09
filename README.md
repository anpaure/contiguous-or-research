# Universal contiguous-subarray OR words

**Exact equality is verified through dimension 22. The first open case is 23.**

For a word of nonempty sets, every target must occur as the union of one
ordinary contiguous interval. The minimum word length is `nu(k)`; `B(k)`
is the proved endpoint-count lower bound. The all-dimension conjecture
`nu(k)=B(k)` remains open.

The [master handoff](MASTER_HANDOFF.md) contains the consolidated mathematical
record. This branch keeps the publication materials and final solutions;
exploratory notes, failed searches, duplicate outputs and bulk witness arrays
belong to the separate local research workspace.

## Exact results

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

The next lower-bound targets are **B(23)=1,352,082** and
**B(24)=2,704,159**; neither is claimed attained here.
The cyclic minima `mu(19)=92,378` and `mu(21)=352,716` are also verified.

See [the new finite results](EXACT_FINITE_RESULTS.md) for the lower-bound
proof, cyclic openings, even-dimensional lifts and verification scope.
[The answer inventory](answers/README.md) gives the exact file hashes.

## Verify a word

The standard-library verifier enumerates all distinct suffix unions without
a witness-length cutoff and checks the endpoint lower bound at every rank:

```bash
python3 verify_word.py answers/k21_optimal352719.word --k 21
python3 verify_word.py answers/k22_optimal705435.word --k 22
```

[Compact verification results](answers/verification.json) record the fixed
six-word check for dimensions 17–22. The explicit finite words do not depend
on the asymptotic PBBS claims.

## Asymptotic bounds

[ASYMPTOTIC_BOUNDS.md](ASYMPTOTIC_BOUNDS.md) summarizes the strongest recorded
rates, explicit thresholds and the numerical bands still awaiting independent
replay. Their conditional proofs and premises are consolidated in the master
handoff. A small relative error does not establish exact equality.

The previously published [coefficient-one manuscript](COEFFICIENT_ONE_PROOF_20260908.md),
[construction companion](COEFFICIENT_ONE_CONSTRUCTION_20260908.md) and
[review package](review/COEFFICIENT_ONE_REVIEW_20260908/README.md) remain available.
They retain their stated internal-review status; no external or formal
verification is claimed.
