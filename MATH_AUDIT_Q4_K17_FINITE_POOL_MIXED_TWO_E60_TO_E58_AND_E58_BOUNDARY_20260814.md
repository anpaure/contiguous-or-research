# Independent audit: exact finite-pool q4 k17 mixed two-exchange descent E60 to E58

**Date:** 2026-08-14

**Verdict:** **PASS**.  On the frozen 174,462-pair/3,749-self-lift
reflection face, one exact pair-plus-self exchange takes the certified E60
state to E58.  At the audited E58 state, no negative pair-plus-pair,
pair-plus-self, or self-plus-self two-exchange exists in that finite face.
This is a finite-pool local-optimality statement, not an exact-cover or
catalogue-completeness theorem.

## 1. Audited implementation

```text
scratch/search_q4_k17_z17_reflection_exact_mixed_two_exchange_20260814.py
sha256 c6e03fd3057cd6184668bb04d07a863cc8a735624dfd321c507ca4442b77f926
```

The implementation rebuilds the current row-load vector and uses the exact
quadratic energy identity for each outgoing pair/self face.  For a fixed
outgoing face it separates the incoming linear scores by column type,
applies only the proved lower-bound cut, excludes selected columns and the
removed self group, and then tests every retained legal incoming pair.  A
self replacement is restricted to the same fixed-matching group; incoming
columns are distinct.  The pair-plus-pair branch is the separately audited
directed-signature oracle.

## 2. Exact E60 to E58 descent

The finite instance has 174,462 reflected-pair columns and 3,749 self-lift
columns.  Of the 1,890 outgoing pair-plus-self faces, four survive the
lower-bound cut and generate seven exact tests.  None of the 595 outgoing
self-plus-self faces survives.  The best exchange is

```text
remove pair 21732, self 1884
add    pair 169836, self 1881
Delta  -2.                                                     (2.1)
```

Direct row-load replay changes the histogram

```text
E60: 30x0, 620x1, 30x2
E58: 29x0, 622x1, 29x2.                                      (2.2)
```

```text
scratch/audit_q4_k17_z17_augmented155k_exact_mixed_two_exchange_20260814.h100.json
sha256 60ae46257e7809939e19d4f7db5d472f1bafec3191b47e5ac173c3729af99559

E60 source state sha256
e04818df037cd62a99b119af59bad467f6ca02ccbac358c2542c1f51efa0288e

E58 emitted state sha256
775dc7b02249cadc58871b98ba8ba266ecdf36ee1db3a17b990cb91e4d2c4de0
```

## 3. Exact E58 two-local boundary

The audited post-descent E58 state has SHA
`002b7d989df86f1c592d2a57db6a8eab37e7912fad6bdb24f386745932e1749c`.
For pair-plus-pair moves, 31 outgoing faces survive the first cut, their
strict thresholds retain 35 candidate incidences, and all five legal
incoming pairs are tested.  The best value is `+4`.  For pair-plus-self
moves, one outgoing face survives and its unique legal incoming pair is
tested; its value is `+2`.  No self-plus-self face survives.  Hence the
reported two-local no-go is exhaustive inside this finite face.

```text
scratch/audit_q4_k17_z17_augmented155k_e58_exact_pair_two_20260814.h100.json
sha256 52f14f2f68e297189c3e51e0c65858d1c4c2583fcc6dea6f51948f8dbb0aa936

scratch/audit_q4_k17_z17_augmented155k_e58_exact_mixed_two_20260814.h100.json
sha256 c4da32f4b4fa6d9c6a4cf4acd2ab6d91b2d3e5c9f17f8a6b647379ff9ba8de1a

finite instance sha256
16ca6995a04309181d9f8caa6bd8671a73b837a770b6dcc4d2a9e6bb2416ed8a
```

## 4. Independent replay

The independent audit reconstructs the instance and source loads, checks
every reported face minimum and threshold, exhausts every retained legal
pair, verifies the E60-to-E58 state change, and independently replays the
pair-plus-pair and mixed E58 no-go reports.

```text
scratch/audit_q4_k17_z17_finite_pool_mixed_two_exchange_e60_e58_20260814.py
sha256 fc409134411f21bd74046052400997ede6d64a22a6544fcee34011c814cc79ab

scratch/audit_q4_k17_z17_finite_pool_mixed_two_exchange_e60_e58_20260814.h100.out
sha256 be7980ed9220bd7cda1a6c90147d0b07699d20e3889fe82366181aaaf8d6e582
status PASS
```

## 5. Exact scope boundary

The E58 boundary does not rule out a column absent from the finite pool, a
neutral pivot followed by a descent, a three-or-more-column exchange,
changing the fixed matching, or any owner/lower-ticket exact cover.  It is
only a complete one- and two-local statement for the frozen finite face.

All computation, replay, and hashing ran on H100.
