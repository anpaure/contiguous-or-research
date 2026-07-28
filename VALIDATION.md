# Publication validation

Validated on 2026-07-28 before publication.

## Exact words

`verify_word.py` reports universal coverage and the matching counting-bound
length for every `answers/k01.word` through `answers/k14.word`:

```text
k=1..14: PASS
covered masks: 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023,
               2047, 4095, 8191, 16383
```

The independent `k=13` and `k=14` verifiers also pass the normalized words.

## Current `k=15` evidence

- `scratch/k15_exact_pair_nogos_20260728/verify_manifest.py`: `PASS`;
  20 payload files and ten exact pair summaries verified, with no retracted
  `allow6` artifacts.
- The compact support-3-through-7 and parent-pure-through-6 JSON audits parse
  successfully and carry the frozen source/parent hashes.
- The native Hall engine, small-support enumerator, `k=14` braid search, and
  current solver sources pass C++/Python syntax checks.

## Scope warning

No `k=15` optimal word is claimed.  The frozen best carrier remains at exact
Hall deficiency 29.  Five-face pair-local predicates are retained only as a
restricted positive-search architecture, never as a global no-go theorem.
