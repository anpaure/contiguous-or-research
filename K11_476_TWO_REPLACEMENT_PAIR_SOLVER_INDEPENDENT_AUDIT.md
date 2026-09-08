# Independent audit of `search_two_replacements_by_pair.cpp`

Date: 2026-07-24  
Scope: the 476-entry word obtained by dropping the last token from
`k11_completed_477.txt`, with replacement values restricted to the nonzero
11-bit masks `1,...,2047`.

## Verdict

The solver is sound and complete for arbitrary changes at zero, one, or two
positions of this 476-entry seed when invoked with `MAX_MISSING=33` and
`DROP_LAST=1`.  I found no solver bug and did not modify the main C++ source.

The completed full run is therefore a valid exhaustive negative result:

```text
UNSAT_SCREEN selected_pairs=113050 value_pairs=473703127450 max_base_counts=40,40,40
```

Here `113050 = binom(476,2)` and
`473703127450 = 113050 * 2047^2`.  Thus every position pair and every ordered
pair of nonzero replacement values was screened.  Exit status was 20.

This conclusion applies to the full `MAX_MISSING=33` run.  The earlier
`MAX_MISSING=10` result only screens its 296 selected position pairs and is not,
by itself, a global two-replacement UNSAT result.

Audited artifact hashes:

```text
69b6669501785d9fc8c15c226c109610cdd645029149dcd077eec19aff709f9d  scratch/search_two_replacements_by_pair.cpp
aa88d2c22431af19e4b4c4a2073251d1316d02a6e152d218cca2082bdc58d58b  k11_completed_477.txt
c41384848a1bf0e809de2421ae35cee4a3171bd9d68087e668c11e2514a49224  scratch/audit_two_replacements_by_pair.py
8d267ff32e2c92d387e16415d8e27cc49bec4a29a40ea5094d4cf745925df6ad  scratch/audit_two_replacements_by_pair_full.cpp
```

## Why the position-pair mask is exact

Fix positions `p < q` and a nonzero target `t`.  Let `W_t` be the old
intervals whose OR is `t`.  The target is guaranteed to survive a replacement
at `p,q` exactly when some interval in `W_t` avoids both positions.  Therefore
the target belongs to the pair's repair mask exactly when every interval in
`W_t` contains `p` or `q`.

For fixed `p`, intervals in `W_t` that already contain `p` impose no condition
on `q`.  Every remaining witness `[left,right]` requires
`q in [left,right]`.  Since these are ordinary integer intervals, their common
intersection is exactly

```text
[max(left), min(right)].
```

This is the `low/high` range computed by the solver.  If every witness contains
`p`, any `q` is allowed; if `W_t` is empty, every position pair needs to repair
`t`.  The final restriction `q > p` merely chooses the unique ordering of each
pair.  These observations cover all branches of the mask construction.

I also recomputed the masks for the full seed by a structurally different
Python-integer-bitset method.  Each bit represented a position pair, and for
each target I intersected the pair-bitsets that touch each direct witness
interval.  It found:

```text
length=476
position pairs=113050
targets missing before replacement=1
maximum pair repair-mask size=33
pairs with mask size <= 10: 296
pairs with mask size <= 33: 113050
input value range after dropping the last token: 1..1946
```

Consequently neither the `MAX_MISSING=33` threshold nor the implementation's
64-target bitmask ceiling excludes any pair for this input.

## Why the interval-category screen is exact

For an interval touching `p` or `q`, let `base` be the OR of its entries after
omitting the two selected positions.  Every such interval belongs to exactly
one of three categories:

1. contains `p` only, with repaired OR `base | a`;
2. contains `q` only, with repaired OR `base | b`;
3. contains both, with repaired OR `base | a | b`.

The C++ loop considers every possible left endpoint through `q`.  An interval
with a larger left endpoint cannot contain either selected position, so no
relevant interval is omitted.  Its incremental `base` excludes exactly `p`
and `q`; collapsing duplicate bases is safe because only existence of a
witness matters.

The three precomputed coverage tables therefore describe every interval whose
OR can change.  Targets outside the pair repair mask retain an untouched old
witness.  Targets inside it are covered after replacement exactly when they
occur in the union of the three category tables.  Hence the bitmask equality
tested before candidate verification is both necessary and sufficient, not
merely a heuristic filter.

The combined-category lookup `cover[2][a | b]` is correct: that table maps a
supplied mask `v` to all targets of the form `base | v`, so supplying `a | b`
gives precisely `base | a | b`.

## Replacement-domain and at-most-two coverage

Both value loops run from 1 through `2^11-1`, inclusive, so all 2,047 allowed
nonzero values are included at each selected position.  They do not require a
new value to differ from the old value.  Thus:

- two actual changes use arbitrary new `a,b`;
- one actual change uses the old value at the companion position;
- zero actual changes use both old values.

Every one-position choice has a companion because the seed has 476 positions.
Accordingly enumeration of distinct position pairs covers all cases with at
most two actual changes.  This reasoning assumes the intended nonzero-word
domain; zero replacement values are deliberately outside it.

## Final candidate verification

On a screen hit, `verify_universal` independently enumerates every interval of
the materialized candidate, marks its exact OR, and requires all targets
`1,...,2047`.  A reported `SAT` is therefore independently checked before it
is printed or written.  For the completed exhaustive run there was no screen
hit, so the negative conclusion instead rests on the exact screen equivalence
proved above and regression-tested below.

## Independent exhaustive regression

I added `scratch/audit_two_replacements_by_pair.py`.  Its oracle recomputes all
candidate interval ORs directly and shares no coverage cache with its model of
the optimized screen.  For every tested position pair it separately compares:

- optimized versus direct missing-target masks;
- incremental versus direct category/base-OR sets;
- every screen decision versus direct universality of the repaired word;
- pair enumeration versus an explicit zero/one/two-change brute-force oracle.

The deterministic test set exhausts all nonzero words for `k=1,2` through
length 5 and for `k=3` through length 4, then adds 600 seeded random words of
length 2 through 8.  It also invokes the separately compiled C++ program as a
black box on 120 stratified cases.

```text
$ c++ -std=c++20 -O2 -Wall -Wextra \
    scratch/search_two_replacements_by_pair.cpp \
    -o /tmp/search_two_replacements_by_pair.audit
$ python3 scratch/audit_two_replacements_by_pair.py \
    --binary /tmp/search_two_replacements_by_pair.audit \
    --large-word k11_completed_477.txt --large-k 11 --drop-last
PASS cases=3757 sat_cases=2522 position_pairs=25934 value_pairs=938638 black_box_cases=120 seed=18274
LARGE_WORD length=476 pairs=113050 old_missing=1 max_pair_missing=33 pairs_le_10=296 pairs_le_33=113050 min_value=1 max_value=1946
```

A second build with Apple Clang 17 and AddressSanitizer plus
UndefinedBehaviorSanitizer passed 3,357 exhaustive/random cases and 60
black-box executions with no sanitizer finding:

```text
PASS cases=3357 sat_cases=2176 position_pairs=21283 value_pairs=844019 black_box_cases=60 seed=18274
```

## Independent full `K=11` exhaustive checker

I additionally implemented `scratch/audit_two_replacements_by_pair_full.cpp`
and ran it over the entire 476-entry instance.  It deliberately obtains the
pair masks without the main solver's witness lists or `low/high` calculation.
It first builds `C[L,R]`, the 2,048-bit set of every OR realized by an interval
wholly inside segment `[L,R]`.  For a pair `p<q`, the exact untouched coverage
is then

```text
C[0,p-1] union C[p+1,q-1] union C[q+1,n-1].
```

The complement on targets 1 through 2,047 is the pair's repair mask.  This is
valid because an interval avoiding both selected positions lies wholly in
exactly one of those three segments.

Changed-interval bases are also generated without the main solver's interval
scan.  The checker takes Cartesian OR-products of the distinct left, middle,
and right OR chains:

```text
first only:  OR(l..p-1) | OR(p+1..r), r<q
second only: OR(l..q-1) | OR(q+1..r), l>p
both:        OR(l..p-1) | OR(p+1..q-1) | OR(q+1..r)
```

It then explicitly visits every `a,b` in `1,...,2047` for every lexicographic
position pair.  Any survivor is materialized and checked by direct interval
enumeration.  The full run completed with process exit status 20:

```text
INPUT k=11 length=476 pair_count=113050 old_missing=1
PAIR_MISSING_HIST 3:21 4:38 5:7 6:1 7:15 8:17 9:55 10:142 11:406 12:857 13:1271 14:1310 15:1127 16:991 17:1029 18:1720 19:3372 20:6317 21:10656 22:14907 23:17372 24:17170 25:14188 26:9904 27:5784 28:2799 29:1107 30:356 31:88 32:21 33:2
PAIR_MISSING_SUMMARY max=33 total_incidence=2580006 pairs_le_10=296 pairs_le_33=113050 fnv1a64=0xa837efe3e195f0ec
CHECK_UNSAT position_pairs=113050 value_pairs=473703127450 max_base_counts=40,40,40 elapsed_seconds=221.344
```

This independently agrees with the main run on the negative verdict, all
113,050 pairs, all 473,703,127,450 replacement pairs, and maximum category
base counts `40,40,40`.  Its exact missing-size histogram agrees entry for
entry with both the separately generated
`scratch/k11_476_base_two_replacement_pairs.analysis` and the Python
target/pair-bitset cross-check.  In particular, the histogram sums to 113,050
pairs and 2,580,006 pair-target incidences; its two size-33 pairs are
`(85,179)` and `(179,357)`.  The similarly named
`scratch/k11_476_two_replacement_pairs.analysis` concerns a relocated word and
was not used as evidence for this prefix.

Full-check evidence hashes:

```text
8d267ff32e2c92d387e16415d8e27cc49bec4a29a40ea5094d4cf745925df6ad  scratch/audit_two_replacements_by_pair_full.cpp
04d11d1f1b1a093337c934042f61115ece0913578cdb7ddbca7aed125019cc06  scratch/audit_two_replacements_by_pair_full
04b668e3c6fd960a721c046628b7d9d1fd3dc52a70345f8a5cd789a97e6d0331  scratch/k11_476_two_replace_independent_full.out
b808a9e8f57b641e5db467cdfb2b9b0ed9d06913855c1df2ee94d8fff9aa75c4  scratch/k11_476_two_replace_independent_full.log
7bc010c2ae8e4dff5da91b49be62610c76ea40a5d6fa44b6eef28102fae0e421  scratch/k11_476_two_replace_python_bitset_crosscheck.out
f789a8c39d1df49c5b9f421b2886683db5d0b685da0a85c9c35704a43d42eaee  scratch/k11_476_base_two_replacement_pairs.analysis
f1acf4ea4dc696a8083de66ef233e9776dba5db13e64fb81ede90d31c5040b09  scratch/k11_476_two_replace_pairwise_full.out
fbfad674e7bcf7c412234455fe3081709b8ef16a72aada849988155f1438cf2b  scratch/k11_476_two_replace_pairwise_full.log
aa88d2c22431af19e4b4c4a2073251d1316d02a6e152d218cca2082bdc58d58b  k11_completed_477.txt
```

The independent run used Apple Clang 17 with `-std=c++20 -O3 -DNDEBUG`.
The parsed source contains 477 tokens and the dropped token is 493.  To bind
the result to the effective input independently of whitespace, concatenating
the first 476 values as little-endian unsigned 16-bit integers has SHA-256
`820ec9daffbcc33305092b9ed3501794eb1e3c1c7dfae532bf0f657674520bf6`.

## Scope limitations of the generic CLI

These do not affect the audited invocation, but the program is not hardened as
a general-purpose parser:

- `DROP_LAST=1` assumes the input contains at least one token;
- values are assumed to lie in `0,...,2^K-1` (the audited values are all
  nonzero and in range);
- the `uint16_t` interval endpoints assume a word length at most 65,535;
- construction of `1 << K` assumes a sensible nonnegative `K` before the later
  size check;
- a global UNSAT interpretation requires every pair to pass both
  `MAX_MISSING` and the hard 64-target mask bound.

All of these preconditions hold for `K=11`, length 476, and
`MAX_MISSING=33`.
