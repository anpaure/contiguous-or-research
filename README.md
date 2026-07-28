# Universal contiguous-subarray OR arrays

For a word of nonzero `k`-bit masks, consider the bitwise OR of every
contiguous subarray.  Let `nu(k)` be the minimum word length needed to obtain
all `2^k-1` nonzero masks, and let `N(k)=nu(k)+1` when the zero mask is also
required.

## Formula and current status

Put

\[
r=\left\lceil\frac{k}{2}\right\rceil,
\qquad W=\binom{k}{r},
\qquad \Lambda=\sum_{j=1}^{r-1}\binom{k}{j},
\]

and define

\[
d(k)=\min\left\{d\ge0:
  dW+\binom{d+1}{2}\ge\Lambda\right\},
\qquad B(k)=W+d(k).
\]

The monotone-deadline argument proves `nu(k) >= B(k)` for every `k`.
Briefly, the triangular array of contiguous ORs is monotone down each column.
The `W` different rank-`r` masks force `W` distinct nondecreasing physical
deadlines.  If a word has length `L=W+e`, those deadlines allow at most

\[
\sum_{i=1}^{L}\min(e,L-i+1)
  =eW+\binom{e+1}{2}
\]

cells below rank `r`.  All `Lambda` nonzero masks of smaller rank must occur
in those cells, forcing `e>=d(k)`.  The proof is written out in
[`MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md`](MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md).

The conjecture is that this lower bound is always exact:

\[
\boxed{\nu(k)=B(k)}.
\]

It is proved by explicit, machine-verified constructions through `k=14`.
For `k=15,...,20`, the numbers below are therefore **proved lower bounds and
conjectured optimal values**, not claimed solutions.

| `k` | `r` | `W=binom(k,r)` | `Lambda` | `d(k)` | `B(k)` / conjectured `nu(k)` | status |
|---:|---:|---:|---:|---:|---:|:---|
| 0 | 0 | 0 | 0 | 0 | **0** | exact |
| 1 | 1 | 1 | 0 | 0 | **1** | exact |
| 2 | 1 | 2 | 0 | 0 | **2** | exact |
| 3 | 2 | 3 | 3 | 1 | **4** | exact |
| 4 | 2 | 6 | 4 | 1 | **7** | exact |
| 5 | 3 | 10 | 15 | 2 | **12** | exact |
| 6 | 3 | 20 | 21 | 1 | **21** | exact |
| 7 | 4 | 35 | 63 | 2 | **37** | exact |
| 8 | 4 | 70 | 92 | 2 | **72** | exact |
| 9 | 5 | 126 | 255 | 2 | **128** | exact |
| 10 | 5 | 252 | 385 | 2 | **254** | exact |
| 11 | 6 | 462 | 1023 | 3 | **465** | exact |
| 12 | 6 | 924 | 1585 | 2 | **926** | exact |
| 13 | 7 | 1716 | 4095 | 3 | **1719** | exact |
| 14 | 7 | 3432 | 6475 | 2 | **3434** | exact |
| 15 | 8 | 6435 | 16383 | 3 | **6438** | open target |
| 16 | 8 | 12870 | 26332 | 3 | **12873** | open target |
| 17 | 9 | 24310 | 65535 | 3 | **24313** | open target |
| 18 | 9 | 48620 | 106761 | 3 | **48623** | open target |
| 19 | 10 | 92378 | 262143 | 3 | **92381** | open target |
| 20 | 10 | 184756 | 431909 | 3 | **184759** | open target |

For the version that also requires the zero mask, the corresponding value is
`N(k)=nu(k)+1`; thus the conjectured formula is `N(k)=B(k)+1`.

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
