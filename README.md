# Universal contiguous-subarray OR arrays

For a word of nonzero `k`-bit masks, consider the bitwise OR of every
contiguous subarray.  Let `nu(k)` be the minimum word length needed to obtain
all `2^k-1` nonzero masks, and let `N(k)=nu(k)+1` when the zero mask is also
required.

## Current status

The counting lower bound `B(k)` is proved for every `k`, and equality is
verified exactly through `k=14`:

| `k` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `nu(k)` | 0 | 1 | 2 | 4 | 7 | 12 | 21 | 37 | 72 | 128 | 254 | 465 | 926 | 1719 | 3434 |
| `N(k)` | 1 | 2 | 3 | 5 | 8 | 13 | 22 | 38 | 73 | 129 | 255 | 466 | 927 | 1720 | 3435 |

Machine-checkable optimal words are in [`answers/`](answers/).  Run

```sh
python3 verify_word.py --k 14 answers/k14.word
```

to verify universal coverage and the matching lower-bound length.

The first open case is `k=15`, where `B(15)=6438`.  The best current carrier
has exact compiler Hall deficiency 29; no length-6438 word is claimed.

## Research record

- [`MATHEMATICAL_HANDOFF.md`](MATHEMATICAL_HANDOFF.md) is the full
  chronological research log.  Its opening status block and later explicitly
  superseding sections are authoritative; older failed conjectures and stale
  numerical intervals are intentionally retained as history.
- [`RESEARCH_INDEX.md`](RESEARCH_INDEX.md) indexes the principal proofs,
  exact certificates, and the current `k=15` frontier.
- [`MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md`](MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md)
  records the general lower bound.

This repository deliberately excludes multi-gigabyte generated SAT inputs,
temporary portfolios, and compiled binaries.  The retained sources,
certificates, hashes, and verifiers are sufficient to inspect and reproduce
the published finite results.
