# K16 genuine-four-filter standard 3-opt q1 no-go — independent audit

Date: 2026-07-31  
Status: **PASS, scoped theorem**

## Scope

The only input is

`scratch/k16_genuine_fourfilter_natural_targets_20260731.word`,

SHA-256

`0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c`.

The theorem covers endpoint-preserving standard linear 3-opt rethreads of
this order. It does not cover endpoint-changing rethreads, four-or-more-cut
rethreads, arbitrary alternating circuits, different middle chronologies, or
global K16 nonexistence.

## Independent reconstruction

The source is a permutation of all 12,870 rank-eight masks. Its two absent
rank-nine adjacent-union colours are exactly

`0xb3cc` and `0xd3cc`.

For a missing rank-nine colour to be realized after a rethread, some newly
added seam must have that colour: an interval of distinct rank-eight subsets
whose total union has rank nine contains an adjacent pair of distinct facets,
and that pair already has the full rank-nine union. Since the source lacks
the colour, this pair must be a new seam.

Both endpoints of such a seam are rank-eight facets of the missing colour.
Mark a cut special when one of its incident vertices is a facet of either
hole. If only one of three cuts were special, only its two endpoint copies
could be facets; they can form at most one new seam. Two distinct missing
colours therefore force at least two special cuts.

There are exactly 31 special cuts among the 12,869 source edges. The reduced
triple family is the disjoint union

\[
 \binom{31}{2}(12869-31)+\binom{31}{3}
 =5,969,670+4,495
 =5,974,165.
\]

For fixed cuts, preserving the path endpoints leaves two orders of the two
middle segments and two orientations of each, hence eight labelled
reconnection templates. Thus the exhaustive audit evaluates

\[
8\cdot5,974,165=47,793,320
\]

labelled representations. With adjacent cuts, reversing a one-vertex segment
can duplicate a final order; the displayed number is therefore an evaluation
count, not necessarily a distinct-order count. Duplication only enlarges the
census and does not weaken the no-go.

An independent C++20 implementation enumerates exactly two-special and
three-special triples separately, uses its own explicit segment endpoint
formulas, and updates the complete affected-colour multiplicity ledger. It
finds

```text
holes=b3cc,d3cc
special_cuts=31
ordinary_cuts=12838
triples_exact2=5969670
triples_exact3=4495
triples_total=5974165
reconnections=47793320
q1_complete=0
```

Therefore no member reaches the scalar P/Q or upper-language filters:

> **Theorem.** No endpoint-preserving standard 3-opt rethread of the
> authenticated genuine-four-filter natural chronology completes its
> rank-nine adjacent-union deck.

## Implementation audit

The original source was rebuilt with `clang++ -std=c++20 -O3 -DNDEBUG` and
reproduced the frozen standard output byte-for-byte. The independent audit is

`scratch/audit_k16_genuine_fourfilter_3opt_q1_independent_20260731.cpp`,

SHA-256

`1dd2d61be1bf08f9802b65f3d895eb35dae4cef63819667a8b50037cabf3c627`.

Its output is

`scratch/k16_genuine_fourfilter_3opt_q1_independent_20260731.out`,

SHA-256

`c5ddc0138064fb526d156bcb4aa6e71ab4fabd38457c69d3b8f7b8dc008a76f1`.

The frozen compact audit is

`scratch/k16_genuine_fourfilter_3opt_q1_independent_20260731.audit.json`.

One non-load-bearing defect was found in the original program: the comparator
used to sort retained post-q1 hits is not a strict weak ordering when two rows
have equal upper defect and unequal area. Since the census has zero q1 hits,
the retained vector is empty and that comparator is never load-bearing for
this theorem. The original parser also narrows before checking range, but the
authenticated input consists entirely of valid rank-eight K16 masks.
