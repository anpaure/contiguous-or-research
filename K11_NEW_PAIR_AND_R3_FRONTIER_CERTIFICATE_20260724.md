# Certified `k=11` pair and selected radius-three frontier

Date: 2026-07-24

## Result

Twenty-six previously unclosed complete arbitrary-two-replacement
neighborhoods were exhausted:

- three new live-search one-hole snapshots (`wide1704`, `lns705`, `lns706`)
  and one new radius-8--10 descendant (`ultra8101`);
- twenty-two ranked first-edit intermediates of the canonical 476-entry
  near-word.

Every run checked all

\[
 {476\choose2}2047^2=473{,}703{,}127{,}450
\]

position/value tuples and returned exactly

```text
UNSAT_SCREEN selected_pairs=113050 value_pairs=473703127450
```

No candidate file was written.  Thus the new runs exclude

```text
12,316,281,313,700
```

named seed/pair/value tuples.  This is a collection of exact local
neighborhood theorems, not a proof that unrestricted length 476 is
impossible.  The certified bound remains

\[
465\le\nu(11)\le477.
\]

## 1. New one-hole snapshots

The three snapshots were copied while their discovery processes remained
live and then frozen locally.  Three independent checks agreed that every
word has length 476 and covers exactly 2,046 of the 2,047 nonzero masks.

```text
09b1000cb01b5efb90091207e7110c8d74669d02d2fd6ec8c007a643ebf9406c  wide1704, hole 251
4d931369f0f1be2d5d07cdba9c51e6e90f919e7f5f988afc804ae63ed62976d6  lns705,   hole 1884
e885c50d392afeadeb10ea95f8a8546c5668590e889de51cb1a059e95b370228  lns706,   hole 1468
```

Their complete arbitrary-two-replacement neighborhoods are UNSAT.  The
`wide1704` snapshot is genuinely newer than the earlier frozen snapshot in
`K11_WIDE_R3_EXACT_CLOSURE_20260724.md`.

The subsequent radius-8--10 search produced a fourth distinct one-hole word,

```text
3ae0265b2a74bbf967c0b350354660f958dee4eabd8b7dc98979e3886e52412f  ultra8101, hole 1884
```

with 1,499 singleton-witness masks.  Its complete two-replacement
neighborhood is also UNSAT.

## 2. Canonical target-creating first-edit frontier

The canonical 476-entry word misses only mask 493.  The deterministic ranker

```text
scratch/rank_k11_target_creating_first_edits.py
```

enumerated all 4,514 one-position assignments that create 493, materialized
their exact intermediate words, computed every intermediate missing family,
and sorted them by complete missing count followed by witness-fragility
scores.  Its output agrees with the previously audited count of 4,514.

The best 24 assignments have intermediate missing counts

```text
1^7, 2^6, 5^3, 6^5, 7^3.
```

Ranks 2 (`469 -> 493`) and 12 (`0 -> 429`) had already received complete
residual pair screens in
`K11_LENGTH476_CANONICAL_TWO_REPLACEMENT_NO_GO_20260724.md`.  This run closed
the other 22.  Consequently every one of the top 24 first assignments is now
followed by an exact screen over all two residual positions and both arbitrary
nonzero values.

This closes only final words containing one of those 24 fixed
position/value assignments together with at most two further value changes.
The other 4,490 target-creating assignments remain without a complete
residual-pair screen.

## 3. Selected radius-three DRAT certificates

The exact fixed-position CNF generator was also applied to 24 newly selected
position triples from each live snapshot.  The inventories were:

```text
seed       variables  clauses  literals  repair max  provider terms
wide1704        1243     5629     13260           4             404
lns705          1236     5215     12110           5             397
lns706          1333     6322     14564           5             494
```

Kissat returned UNSAT for all three formulas.  Each binary DRAT proof was
checked independently by `drat-trim`; all three checker logs end in

```text
s VERIFIED
```

These certificates close 72 selected position triples with all `2047^3`
assignments of their three values.  They do not close the full radius-three
neighborhood of any snapshot.

## 4. Exact solver semantics

The pair solver groups every changed interval into exactly one of three
categories: first-only, second-only, or both.  For each unordered position
pair it computes the exact family of targets whose old witnesses are all
destroyed, and then checks the full `2047^2` value square.  A candidate is
materialized and independently enumerated before it can return SAT.

The solver and its separate small-instance/black-box audit are frozen as:

```text
69b6669501785d9fc8c15c226c109610cdd645029149dcd077eec19aff709f9d  search_two_replacements_by_pair.cpp
852b0219b53f8a58897ec98947405cc5c2cc7d789bccc921d02ee3365382ce2e  local arm64 binary
a67d7721ca01040664f9abdd9c7a60f4ee2d924ca7aa29152402568180315165  independent audit note
```

The ranker and its complete table have hashes

```text
aa4e9a73a17bd24be33767d96174d15a251a8453d8495cfd375fac5bba48cb5b  ranker
10d88bb251622eb77a52f7013efdf352189afb1ab31fc7687dce926ced1f950b  4,514-row TSV
```

## 5. Manifests

```text
604e1c773e41397f67a75c55450ea5af3ba2fd822be9c6e60fecd2bdef7064dc  pair-output manifest
2d03abadef5fa75e7dfbbbb46f7bec0857dbc00d895d5b9ceab81d035e0ef071  top-24 intermediate-word manifest
9b97f69e6bebe6fce8cd1f2cb40f0ecc58571609addd74c2bba2b0473cef4745  radius-three certificate manifest
```

## 6. Constructive successor

The live radius-6/7 search was plateauing, so its source was generalized
without changing the default regime.  Compile-time parameters now permit a
separate radius-8--10 binary.  A smoke run passed the compressed-evaluator
self-check and produced nonempty candidate quotas at every radius and creator
style.  Three 20-minute radius-8--10 searches completed without a universal
word.  They explored 791, 1,000, and 1,207 accepted states respectively.  The
first produced the new `ultra8101` one-hole word above; its exact pair
neighborhood was then closed.  No bound changed.
