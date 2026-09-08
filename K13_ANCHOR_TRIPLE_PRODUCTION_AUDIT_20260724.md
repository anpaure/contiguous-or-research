# Exact `k=13` anchor-three-edit production audit

Date: 2026-07-24

## Verdict

The encoding in `scratch/k13_exact_triple_neighborhood_cnf.cpp` is exact for
the supplied position triples: it is satisfiable if and only if one listed
triple of positions can be assigned three arbitrary nonzero 13-bit values so
that the resulting 1,851-entry word covers all 8,191 nonzero targets.

This is an exact *candidate* encoding.  An UNSAT result changes a mathematical
lower bound only when its DRAT trace is independently checked.  The production
runs below deliberately used search mode and are therefore recorded only as
`UNSAT_UNCERTIFIED` no-hit results.

## Encoding audit

For sorted edited positions `a<b<c`, an interval that meets the edits contains
one of exactly six nonempty consecutive edit sets:

```text
{a}, {b}, {c}, {a,b}, {b,c}, {a,b,c}.
```

For each type, the generator enumerates the exact unchanged base ORs as the
cross product of the relevant monotone left/right chains and the fixed gaps.
For a target `t` and base `b`, a provider is encoded by:

1. every involved replacement value is a subset of `t`;
2. their union contains every bit of `t & ~b`.

The provider selector implies its triple selector.  Every unsafe target has a
triple-gated disjunction of all its providers.  Exactly one triple selector is
true, and every replacement value is constrained nonzero.  Providers for
unselected triples are forced false, so the 39 primary value bits can safely
be shared across all listed triples.

Removing a dominated need is sound: if `need1` is a subset of `need2`, every
assignment satisfying the provider for `need2` also satisfies the one for
`need1`, while the same target-subset clauses apply.

Independent RunPod checks reproduced:

```text
PASS words=24 assignments=164640 target_checks=1152480
PASS cases=80 sat=65 unsat=15
```

A separate SAT decoder smoke test generated a three-entry `k=2` model,
decoded it, checked it quadratically in Python, and then passed it through the
independent C++ `verify_or_array` verifier (`covered=3 required=3`).

## Input integrity

The seed words are:

```text
forward   3c1b70651f319b9a8c58adba16308c6be88157d40721271aef4770e1eeb78225
reversed  15e15d71856823fda819a4303cb4fb46d45d1f603038f4f30f882dc1b9a63d23
```

Each word has exactly 1,851 nonzero entries.  Every manifest has exactly 250
distinct sorted triples, every position is in `0..1850`, and every row contains
the declared anchor.  The four manifest hashes are:

```text
forward anchor 961
6e19d1a169f2ddac840ba9bcf6a3783249c6fa8b32df0a7e1f77f2cc3fc28ad7
9b164195eccdd4986e26035e033968c26fba12deaa9ea140e4ef36dd4a292913
069ec8a93ad3083e7f70dd68afd9daf3ae2efcde353223cd407eb0ddaa97072c
4161dc560d6f9ed1bc0842e369d452f4aa2aa94e4258fc75c49896bfc9954e8d

reversed anchor 1470
4c7ac4f2237e372aa2dffada2d92846d86591d5852c6949f23c68cab30bc29a2
faf2b51b8eda5d00d4beb8c620ed95b4e395e3e571baa6bad0b2f9b36998c952
55babede100820186d7c1f8e24601c59839fcd8e3ccd22dbb004244c3fa99426
a8f00a66bfeeac86083fddc17a024387f6513dea5fc412b3b579da922ea206a8
```

The union has 1,000 distinct triples per orientation.

## Wrapper corrections

Two operational hazards were found and corrected:

1. The original runner changed to its work directory before using the word,
   manifest, generator, and decoder paths.  Relative caller paths could
   therefore fail.  The runner now canonicalizes all paths first and defaults
   the generator/decoder relative to the runner itself.
2. Reusing a tag could overwrite a prior formula or result.  The runner now
   refuses an existing formula/model/marker tag.  Its candidate length check
   is derived from the input word rather than hard-coded, and the independent
   verifier output must explicitly report `covered=8191 required=8191`.

`scratch/run_k13_anchor_triple_portfolio.sh` additionally freezes the word and
manifest hashes, checks row counts, handles search-only UNSAT exit code 1, and
stops immediately on a doubly verified SAT candidate.

Current wrapper hashes:

```text
00b8760de0fba0b5e2aa22c27844565a321c56095ec4beedcd044130378e933c  run_k13_exact_triple_neighborhood.sh
b7918e7ae6c5aea10bd55659d0b667ddfff46aabb58f0052cb25c9515460122b  run_k13_anchor_triple_portfolio.sh
```

## RunPod production recipe

After copying the source, scripts, words, and manifest directory to
`/root/k13_triple_neighborhood_20260724`, compile remotely:

```bash
cd /root/k13_triple_neighborhood_20260724
taskset -c 30 g++ -O3 -std=c++20 -Wall -Wextra -pedantic \
  k13_exact_triple_neighborhood_cnf.cpp \
  -o k13_exact_triple_neighborhood_cnf \
  2>compile.warnings
test ! -s compile.warnings
```

Run one orientation sequentially on one free RunPod CPU:

```bash
export K13_TRIPLE_WORK=/root/k13_triple_neighborhood_20260724
export K13_TRIPLE_GENERATOR=$K13_TRIPLE_WORK/k13_exact_triple_neighborhood_cnf
export K13_TRIPLE_DECODER=$K13_TRIPLE_WORK/decode_verify_k13_triple_neighborhood.py
export K13_TRIPLE_RUNNER=$K13_TRIPLE_WORK/run_k13_exact_triple_neighborhood.sh
export VERIFY_OR_ARRAY=/root/verify_or_array

nohup "$K13_TRIPLE_WORK/run_k13_anchor_triple_portfolio.sh" \
  forward 30 \
  /root/k13_pair_neighborhood_20260724/k13_1851_onehole.word \
  "$K13_TRIPLE_WORK/manifests" search 13000 21600 \
  >"$K13_TRIPLE_WORK/forward.portfolio.log" 2>&1 &
```

For the reverse orientation, replace `forward`, the word path, and seed base:

```bash
nohup "$K13_TRIPLE_WORK/run_k13_anchor_triple_portfolio.sh" \
  reversed 30 \
  /root/k13_pair_neighborhood_20260724/k13_1851_reversed_onehole.word \
  "$K13_TRIPLE_WORK/manifests" search 14000 21600 \
  >"$K13_TRIPLE_WORK/reversed.portfolio.log" 2>&1 &
```

Do not run both commands on the same CPU simultaneously.

## Actual Purple search-only run

Purple had 1.3 GiB free before launch.  All eight formulas generated and
solved without pressure:

```text
orientation/block       variables  clauses  peak RSS  solve time
forward 0000                17170   219387     18 MB      0.60 s
forward 0001                16538   203852     16 MB      0.48 s
forward 0002                19340   251219     17 MB      0.82 s
forward 0003                17887   223683     18 MB      0.59 s
reversed 0000               16764   217126     16 MB      0.64 s
reversed 0001               16712   210610     16 MB      0.66 s
reversed 0002               16801   213928     16 MB      0.54 s
reversed 0003               18450   237857     19 MB      0.79 s
```

Every run returned Kissat exit 20 and has an `UNSAT_UNCERTIFIED` marker.  All
eight pre-solve SHA manifests rechecked successfully against the exact word,
triple manifest, CNF, map, and stats files.  Therefore the top 1,000 ranked
anchor triples in each orientation contain no candidate, but this search-only
portfolio is not an UNSAT certificate and does not change any finite bound.
