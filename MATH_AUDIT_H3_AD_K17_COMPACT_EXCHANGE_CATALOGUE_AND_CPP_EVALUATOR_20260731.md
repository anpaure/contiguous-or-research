# Independent audit: K17 compact marked-exchange catalogue and C++ evaluator

Date: 2026-07-31  
Lane: H3, independent audit for AD  
Verdict: **PASS in the stated marked-path-preserving exchange/evaluation scope**

No nonempty repair selection, exact compiler, or common-cap solution is proved
here.

## 1. Frozen objects

```text
scratch/build_ad_k17_opt28_compact_exchange_catalogue_20260731.py
SHA-256 142b85450187aedfa1b690212ee1846d93327300fd6bd3e1b2ecfb218b57e29d

scratch/evaluate_ad_k17_opt28_marked_exchange_20260731.cpp
SHA-256 7848bd556e41ec3c9ad515e547f205675c895b41904c1751259d4cb859407267

scratch/ad_k17_opt28_marked_exchange_catalogue_20260731.bin
SHA-256 9ccf24540e96f90e210b5f3538735e29d08e3ef0a42fb3e02026a5c67791526b

scratch/ad_k17_opt28_marked_exchange_static218_20260731.bin
SHA-256 acad22726208d692d35a09ff049af72a7aa30da0468f089dc335437ec5fff5a2

scratch/ad_k17_opt28_marked_exchange_seed536_20260731.bin
SHA-256 3a7dee9ab6c159d5b846787d504fc1c92f7946a6ce37f28cedaa3b191b713718

scratch/ad_k17_opt28_marked_exchange_catalogue_20260731.meta.json
SHA-256 ccc6519a0f05ec051a04d65c5da8ecbff814397ca87580a12f3b9252851dfced

scratch/ad_k17_opt28_marked_exchange_incumbent_20260731.selection
SHA-256 87cf4d579c53eafe75751220347d2143bb21b9adffee09e609ed93b49861a001

scratch/ad_k17_opt28_marked_exchange_incumbent_20260731.eval.json
SHA-256 f68952265e751c65934413997d7a24c980bc2fb4971d8a83a8442bf579f60cf4
```

Independent verifier and result:

```text
scratch/audit_h3_ad_k17_compact_exchange_catalogue_20260731.py
SHA-256 16abaa3a721251e49807339d5b924627c5e838eb252bffcb3d11dcea052f84c3

scratch/h3_ad_k17_compact_exchange_catalogue_20260731.audit.json
SHA-256 e37263ed35560e589af20cff9546691e493a3252a5d424d34a25456e40078c0f
payload eb33cda665b26a63e1d124f845db8f28f9547105f5483ebcc8bdc8074b595bd4
```

The carrier authenticated through the seed is

```text
scratch/k17_opt28_connected_owner_cycle_20260731.word
SHA-256 a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa
```

## 2. Independent reconstruction of the frozen interval

I reconstructed the marked set from the flow components, the `133` selected
U-owner connectors, the `106` mandatory components, and the `28` optional
components.  It has exactly `4108` owners.  In the authenticated carrier it
is one cyclic interval, beginning at source position `21331`.  After rotating
there, the edge ledger is exactly

```text
marked--marked                         4107
left marked--complement cross edge       1
complement--complement                 20201
right complement--marked closing edge     1
```

All `24310` owners are distinct rank-nine masks.  All cyclic adjacent pairs
are Johnson edges, and their `24310` intersections are the complete rank-eight
layer exactly once.

The complement has `20202` owners.  Hence its sorted owner indices fit in an
unsigned 16-bit field; the largest index is `20201`.

## 3. Exact binary and canonical-ID audit

The independent verifier did not import the producer.  It parsed the binary
headers directly and regenerated every record in the prescribed order:

1. sort the `20201` eligible source edges by their rank-eight colour;
2. for each colour, sort its complement rank-nine supersets numerically;
3. enumerate unordered pairs lexicographically; and
4. omit exactly the incumbent source pair.

Every one of the `20201` group records and every one of the `545721` column
records agrees byte-for-byte with this independent regeneration.  The exact
superset-count profile is

```text
number of complement supersets       3    4    5     6     7     8     9
eligible colours                    15  129  454  1601  3836  6748  7418
```

The seed is exactly `536` bytes.  Its carrier SHA and SHA of the trailing
`218` little-endian rank-ten IDs verify.  Those IDs decode to the same sorted
`218` static zero-support targets as the authenticated static-provider audit.

The separate static sidecar is also exact record-for-record:

```text
rows                                      218
canonical column references              6419
minimum support per row                     10
maximum support per row                     45
```

Thus column IDs are canonical and reproducible from the `536`-byte seed plus
the authenticated carrier.  The `2.6 MB` flat catalogue is a faithful cached
expansion, not a different model.

## 4. Factor and connectivity logic

For each eligible lower colour the evaluator either retains the old edge or
uses one selected off-source edge having exactly that intersection.  More
than one selected column in a colour group is rejected.  The marked path and
the two cross edges are inserted unconditionally.

The resulting graph is loopless.  Distinct selected edges cannot be parallel:
an unordered Johnson owner pair has only one intersection colour.  Therefore

```text
all degrees equal two + connected
```

is equivalent to being one simple spanning cycle.  The evaluator checks
exactly these conditions.  Starting from the left cross edge, a connected
degree-two graph must traverse every complement owner before leaving through
the right cross edge, because the frozen marked vertices already form one
path and have no other complement ports.  Hence the explicit complement
traversal and its requirement to end at marked owner `0` are sound.

The lower-palette check is also exact.  It takes the `4107` frozen marked
turns and the `20203` literal facet tokens (two cross facets plus `20201`
complement facets).  Having `24310` distinct rank-eight masks is equivalent
to the whole rank-eight palette.

## 5. Literal boundary and closing-edge audit

For a complement order `q_0,...,q_20201`, the evaluator constructs

```text
Z = marked owners,
    (last marked) intersection q_0,
    q_0 intersection q_1, ...,
    q_20200 intersection q_20201,
    q_20201 intersection (first marked).
```

Thus `|Z|=24311`.  Both cross-bank lower facets occur literally.  In the
incumbent they are `18230` and `6394`.

Upper intervals are intentionally **linear**, not cyclic.  The owner-order
rank-ten reduction scans adjacent pairs at indices `0,...,24308`; it does not
wrap the final complement owner to the first marked owner.  The Z interval
scan likewise does not wrap.  This is the correct chronology for a literal
linear word.  The frozen cycle-closing rank-ten union is `88314`; it happens
to occur elsewhere in the linear support, so equality of support sets alone
would not expose an accidental wrap.  Direct source inspection and the
independent reconstruction confirm that no wrap is performed.

For every tested one-cycle chronology, the code also compares the rank-ten
interval support of `Z` to the linear adjacent-owner support.  The signed
rank-ten delta removes each selected old union and adds its selected new
union, using the same non-wrapping baseline.  This is exact.

## 6. Residence, maximal envelope, and upper scans

The strict run code counts a positive run only when it has a zero on both
sides in the linear row.  It applies threshold three to `Z`, and threshold
four to the adjacent-union row `D(Z)`.  Boundary runs are deliberately not
charged.

For every envelope position `p`, the code computes the intersection of
`Z[p-2],Z[p-1],Z[p]` that exists inside the word.  It then replays cell `i` as
the union of envelope cells `i,i+1,i+2`.  These are the exact maximal-envelope
and replay identities for D2.

The rank-ten through rank-twelve scan starts with one Z cell, extends by at
least one further cell, records ranks `10,11,12`, and stops after the union
rank exceeds twelve.  Monotonicity of OR makes the stop exact.  A single Z
cell has rank eight or nine, so omitting length-one intervals loses no target
in these ranks.

The evaluator does not scan ranks `13` through `17`; this is an explicit
scope boundary, not evidence that a rethread preserves their incumbent
coverage.

## 7. Recompiled empty-selection replay

I compiled the final source with

```text
clang++ -std=c++20 -O2 -Wall -Wextra -Wpedantic \
  scratch/evaluate_ad_k17_opt28_marked_exchange_20260731.cpp \
  -o /tmp/audit_ad_k17_exchange_eval_final
```

Compilation emitted no warnings.  The executable SHA in this environment was
`3ed54cde8795ec1f048160c6da2c58122086a5a166a3e5bfff69a05e0b4a1ea0`.
The empty run took about `1.5 s` wall time and reproduced the frozen evaluation
byte-for-byte, including

```text
one cycle                                      yes
degree-bad vertices                              0
lower palette exact                            yes
D2 bad runs                                   2392 = 1025 length one + 1367 length two
D3 bad runs                                   2392 = 1025 length two + 1367 length three
empty maximal-envelope cells                     0
maximal-envelope replay mismatches             3568
upper holes rank 10 / 11 / 12             1900 / 911 / 128
interval extensions through the rank-12 stop 136379
```

The independently computed little-endian hashes agree with the evaluator:

```text
owner order 38e83e5a2ab1fb25145f80736a3bc82b9dbc2f29167518941c10252e0f1104ef
Z row       3c4dbc7cd6a416dd952cc1b4d7fa3da65da1476c375387979b238be94b49c73c
```

Negative regressions also fail closed:

* changing the carrier bytes is rejected by the carrier SHA check;
* repeating a column ID is rejected before evaluation; and
* selecting column `0` alone yields valid JSON but is rejected as a factor,
  with exactly four degree-bad vertices.

## 8. Exact scope and caveats

The audit supports the following statement only:

> The catalogue is a complete, canonical list of every off-source
> complement Johnson edge that can replace an incumbent complement edge
> while preserving its lower colour and freezing the marked path and the two
> cross edges.  The evaluator exactly recognizes one-cycle selections,
> materializes their linear Z row, and evaluates D2/D3 runs, maximal-envelope
> replay, and ranks ten through twelve.

Remaining caveats are substantive:

1. The evaluator authenticates the carrier through `seed536`; a consumer must
   authenticate `seed536` itself (or the meta hash).  It regenerates the
   catalogue and does not consume the large flat binary.
2. No nonempty one-cycle exchange selection was supplied or proved feasible
   in this audit.
3. Passing residence requires zero D2 bad runs, zero empty envelopes, and zero
   replay mismatches; the incumbent fails badly.
4. Completeness at ranks ten through twelve, let alone preservation at higher
   ranks, has not been achieved.
5. Common-cap Hall is not implemented or tested by this evaluator.

Within these boundaries I found no factor-of-one, boundary, closing-edge,
canonical-ID, JSON, hash, or connectivity error.
