# Independent audit: exact finite-pool q4 k17 three-pair descent E58 to E56 and E54 boundary

**Date:** 2026-08-14

**Verdict:** **PASS**.  On the frozen 189,462-reflected-pair finite
instance, one exact three-pair exchange takes the audited E58 state to
E56.  On the later E54 state, no negative replacement of three selected
pairs by three distinct unselected pairs exists.  Self lifts remain fixed.
This does not claim completeness of the finite column catalogue or rule
out mixed pair/self moves.

## 1. Audited implementation

```text
scratch/search_q4_k17_z17_reflection_exact_three_pair_exchange_20260814.py
sha256 df4af7907cdd0937c7cf02d5c8f6a3fea28fbb917610d15790c2ecfb9795fa60
```

For each of the `binom(54,3)=24,804` outgoing faces, the implementation
computes the exact `c_R` and every `h_R` score from the quadratic exchange
identity.  It applies the exact distinct-index face minimum, the lossless
candidate exclusion minimum `mu_2(N)`, and the pair exclusion minimum
`mu_1(N,M)`.  It then scans every canonically ordered third candidate
satisfying the strict last-score bound and restores both missing pairwise
overlaps.  Selected incoming indices and repeated incoming indices are
excluded.  Score ties are harmless because only their values enter the
exclusion bounds and any two exclusions leave one of the first three
candidate entries.

## 2. E58 to E56 certificate

Of the 24,804 outgoing faces, 621 survive the face cut.  They retain 11,406
candidate incidences, generate 911,706 candidate-pair tests, and leave
2,726 exact incoming triples.  The deterministic best exchange is

```text
remove 20761,127008,169836
add    169767,174503,179488
Delta  -2.                                                     (2.1)
```

Direct replay changes the load histogram from

```text
E58: 29x0, 622x1, 29x2
E56: 28x0, 624x1, 28x2.                                      (2.2)
```

```text
scratch/audit_q4_k17_z17_augmented170k_exact_three_pair_20260814.h100.json
sha256 f2b1bbe294db81c0c462d2bf0cee66a12948acab51f406de010903140625d9d2

E58 source state sha256
002b7d989df86f1c592d2a57db6a8eab37e7912fad6bdb24f386745932e1749c

E56 output state sha256
fde908fb2648e62b94fd0fa8bf7a98fb5703945b180507de0553c4c3ef4880b2
```

## 3. Exact E54 three-pair boundary

At the later E54 state, 250 outgoing faces survive, retaining 3,872
candidate incidences and generating 303,716 pair tests.  All 424 exact
incoming triples are evaluated.  The best is neutral:

```text
remove 11131,157012,161711
add    158938,165436,167607
Delta   0.                                                      (3.1)
```

Thus the finite face has no negative three-pair exchange at E54.

```text
scratch/audit_q4_k17_z17_augmented170k_e54_exact_three_pair_20260814.h100.json
sha256 b9fc964839bbad3b4fd6e8b0f40e502e404e35474e444e380eac0407a993bff1

E54 source state sha256
afc99382982bafc30b96fd2c936e3c4ccbf4f36a99c29544cb13e991124c7e87

finite instance sha256
af928d3e2ad164b8f24e92d5cf0e219fdd43027249c68e5279e66d7d6e55fe31
```

The intervening E56-to-E54 descent is outside this audit unless its
separate two-exchange certificate is staged with it; the E54 state and its
literal load vector are nevertheless replayed here.

## 4. Independent full replay

```text
scratch/audit_q4_k17_z17_finite_pool_three_pair_exchange_e58_e54_20260814.py
sha256 565b74053a33f20da29c2bd99f5e521ce671db7f86aace29fce8d42ed23e490e

scratch/audit_q4_k17_z17_finite_pool_three_pair_exchange_e58_e54_20260814.h100.out
sha256 09251ceff035a3a98eed4beafdc1acf804d3b9dec9da54d153250507a12ec686
status PASS
```

The independent audit reconstructs both load vectors, recomputes every
one of the 49,608 outgoing-face minima and exact exclusion thresholds,
checks every retained pair and triple, verifies both global best values,
and replays the E56 output state.

## 5. Scope boundary

The E54 no-go is only a three-reflected-pair local statement for this
finite 189,462-option instance and fixed self selection.  It does not rule
out absent columns, a neutral pivot followed by descent, four-or-more
configurations, changing the fixed matching, mixed self/pair moves, or an
owner/lower-ticket exact cover.

All computation, replay, and hashing ran on H100.
