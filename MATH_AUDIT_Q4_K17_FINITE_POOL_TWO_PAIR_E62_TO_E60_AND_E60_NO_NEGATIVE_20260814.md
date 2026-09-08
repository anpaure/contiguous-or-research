# Independent audit: exact finite-pool q4 k17 two-pair descent E62 to E60 and the E60 two-pair boundary

**Date:** 2026-08-14

**Verdict:** **PASS**.  One exact two-reflected-pair exchange takes the
certified E62 state to E60.  On the later 174,462-pair finite instance, the
same selected E60 state has no negative exchange replacing two selected
pairs by two distinct unselected pairs.  Self lifts are held fixed and no
claim is made about missing columns or mixed pair/self moves.

## 1. Audited implementation

The implementation is a direct realization of
`MATH_REDUCTION_Q4_K17_EXACT_TWO_PAIR_EXCHANGE_DIRECTED_SIGNATURE_ORACLE_20260814.md`
(source SHA `296b90db85ae7684464eee115b6242b5058bb74f68282742d1a97adfacdd3e72`).

```text
scratch/search_q4_k17_z17_reflection_exact_two_pair_exchange_20260814.py
sha256 0703b10030bb7919d303b38af936340e68e2e9bd5ac44d28bb188e7d1b01599e
```

For each of the `binom(54,2)=1,431` outgoing faces, it computes the exact
constant `c`, every finite-pool score `h`, and `m=min h`.  A face is removed
only by the proved cut `c+2m>=0`.  On a surviving face it retains exactly
the strict-threshold candidates `h<-c-m` and tests every unordered pair,
adding the exact `2|N intersect M|` term.  Selected incoming indices and a
repeated incoming index are excluded.

## 2. E62 to E60 certificate

The 166,614-pair instance has 45 surviving outgoing faces, 120 threshold
candidate incidences across those faces, and 359 exact incoming-pair tests.
The deterministic lexicographically selected best exchange is

```text
remove 2186,16754
add    157012,161711
Delta  -2.                                                     (2.1)
```

Direct row-load replay changes the histogram

```text
E62: 31x0, 618x1, 31x2
E60: 30x0, 620x1, 30x2.                                      (2.2)
```

The emitted output state has exactly the source pair list with the two
indices in `(2.1)` replaced, the same self indices, and energy 60.

```text
scratch/audit_q4_k17_z17_augmented145k_exact_two_pair_exchange_20260814.h100.json
sha256 c9d1e678c3a659c83249ac88329133db6c31f65b2c0f80aae93adf311d09905f

E62 source state sha256
20b15c498906422e18e101c3f342cf064e4f45b0e408778405ab631d4bda82e5

E60 output state sha256
463183d13a3518d603a32ed45b26f8af9c39042458654f4d1ead3becef12b036
```

## 3. Expanded finite-pool E60 boundary

After expanding the pair instance to 174,462 options, the selected pair and
self index lists are unchanged from the E60 output above.  The exact oracle
has 41 surviving faces, 70 threshold candidate incidences, and only 55
incoming-pair tests.  Their best value is zero:

```text
remove 5703,152016
add    152345,174138
Delta   0.                                                      (3.1)
```

All 1,390 omitted faces satisfy `c+2m>=0`; all 41 surviving faces are
exhausted literally.  Therefore `NO_NEGATIVE_TWO_PAIR_EXCHANGE` is exact
for this finite instance and this fixed self selection.

```text
scratch/audit_q4_k17_z17_augmented155k_exact_two_pair_20260814.h100.json
sha256 b0e51a0699d4c811b9d824648489ccfa18069b03384263923f1f56bf2739c5ca

expanded E60 source state sha256
e04818df037cd62a99b119af59bad467f6ca02ccbac358c2542c1f51efa0288e

174,462-pair instance sha256
16ca6995a04309181d9f8caa6bd8671a73b837a770b6dcc4d2a9e6bb2416ed8a
```

## 4. Independent full replay

The independent audit rebuilds both instances and both source load vectors,
recomputes all 1,431 minima and thresholds in each case, checks every face
record, retests all 414 surviving incoming pairs, and verifies the E60
output state.

```text
scratch/audit_q4_k17_z17_finite_pool_two_pair_exchange_e62_e60_20260814.py
sha256 673b20d7d159cf2453b66f5684faef8f6f4a611c17bebb34b650f8161fa9c948

scratch/audit_q4_k17_z17_finite_pool_two_pair_exchange_e62_e60_20260814.h100.out
sha256 5fef81a5487ac1f2cd792505475d5517a3a38c901ae5797341c203e3e30d42e5
status PASS
```

## 5. Exact scope boundary

The E60 no-go is not a statement about:

* a pair column absent from the 174,462-option instance;
* replacing a self lift, or a mixed pair/self two-exchange;
* a neutral two-pair pivot followed by another move;
* a three-or-more-configuration exchange; or
* feasibility of the owner exact cover or any lower-ticket ledger.

All computation, replay, and hashing ran on H100.
