# Certified improvement: `nu(14) <= 3668`

Date: 2026-07-27

The 3,668-entry word `scratch/k14_249_complete_3668_oneedit.word`
exhaustively covers every nonzero 14-bit mask by a contiguous OR.  Therefore

\[
                         \boxed{3434\le\nu(14)\le3668}.
\]

Its prefix `scratch/k14_block_transposition_249.word` has optimal candidate
length 3,434 and misses 249 upper masks (227 of rank 9 and 22 of rank 10).
It is obtained by compiler-safe block transpositions from the earlier
251-miss core.  The completion suffix has length 234.

```text
da6ef45b489bf2a6dbde818003aa1a31921d63a6ab3a4d4a6385308ecb20b2fb  scratch/k14_block_transposition_249.word
ae975d97cc048ab2b245f2986419edf47078ce479447b2233bef8a775815dc29  scratch/k14_249_append234_oneedit.txt
2bab8941bd66305050cdcc4d1244fcc20cecc5412c656a4ead0b187e3a463e26  scratch/k14_249_complete_3668_oneedit.word
```

Run `python3 scratch/verify_k14_completed_3668.py`.  It checks the hash,
length, entry range, exhaustive coverage of all 16,383 targets, and then
recomputes one interval witness per target.  Two independent C++ verifiers
also pass.

The restricted 234-to-233 delete-one/edit-one search examined 203 one-hole
deletions and 47,647 exact repairs without success.  This is not an arbitrary
completion lower bound.
