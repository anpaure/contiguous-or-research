# Universal contiguous-subarray OR arrays

## Proposed coefficient-one proof — September 8, 2026

The new manuscript proposes
`nu(k) = (1 + o(1)) binom(k, floor(k/2))` for all ranks and dimensions.
It has internal AI-agent reviews; external review and formal verification
have not been obtained. This asymptotic claim does not settle the exact
finite optimum or supply an explicit convergence rate.

- [Proof manuscript](COEFFICIENT_ONE_PROOF_20260908.md)
- [Full proof text and supporting lemmas](review/COEFFICIENT_ONE_REVIEW_20260908/FULL_PROOF_TEXT.md)
- [Portable review package and dependency notes](review/COEFFICIENT_ONE_REVIEW_20260908/README.md)
- [Download the complete review ZIP](review/COEFFICIENT_ONE_REVIEW_20260908.zip)
- [Finite construction recipe](COEFFICIENT_ONE_CONSTRUCTION_20260908.md)
- [Current master handoff](MASTER_HANDOFF.md)

The package includes complete local proof sources, exact originals, an
index and checksums. Its required published external theorem is cited in
its README. The finite-word verifier in the package checks the earlier
k=17 construction, not the proposed asymptotic theorem.

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

It is proved by explicit, machine-verified constructions through `k=16`.
For `k=17,...,20`, the numbers below are therefore **proved lower bounds and
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
| 15 | 8 | 6435 | 16383 | 3 | **6438** | exact |
| 16 | 8 | 12870 | 26332 | 3 | **12873** | exact |
| 17 | 9 | 24310 | 65535 | 3 | **24313** | `24313 <= nu(17) <= 25745` |
| 18 | 9 | 48620 | 106761 | 3 | **48623** | open target |
| 19 | 10 | 92378 | 262143 | 3 | **92381** | open target |
| 20 | 10 | 184756 | 431909 | 3 | **184759** | open target |

For the version that also requires the zero mask, the corresponding value is
`N(k)=nu(k)+1`; thus the conjectured formula is `N(k)=B(k)+1`.

Machine-checkable optimal words are in [`answers/`](answers/).  Run

```sh
python3 verify_word.py --k 16 answers/k16.word
```

to verify universal coverage and the matching lower-bound length.

The formerly open `k=16` case is now exact:

\[
                         \boxed{\nu(16)=12873}.
\]

The retained word is [`answers/k16.word`](answers/k16.word), with SHA-256
`890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe`.
Four independent replay paths cover all `65,535` nonempty masks.  The exact
common-cap matching construction, generated-model provenance, hashes, and
proof scope are in
[`MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md`](MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md).
The first unresolved finite case is therefore `k=17`, with conjectured value
`B(17)=24313`.  The former length-`12874`, length-`12875`, and standard
trimmed-lift `k=16` certificates remain historical checkpoints.

An earlier literal certified upper bound is

\[
                    24313\le\nu(17)\le25746.
\]

If `X` is the verified `k=16` optimum and `z` is the new coordinate, the
word

```text
X, {z}, (X without its last cell, with z added to every cell)
```

has length `2*12873=25746` and is universal on 17 coordinates.  The retained
word is [`answers/k17_upper25746.word`](answers/k17_upper25746.word), SHA-256
`f8ea81ab1f8f1280f638e7e607b32a7dd53fc541b30fe1005db8aae692be031b`.
Two independent literal scans cover all `131,071` nonempty masks.  This is an
upper bound only; the active construction still targets the lower-bound
length `24313`.

The later retained [25,745-letter word](answers/k17_upper25745.word)
improves the upper bound to `24313 <= nu(17) <= 25745`. Its
[deterministic boundary-splice generator](review/COEFFICIENT_ONE_REVIEW_20260908/finite_construction/scripts/k17_boundary_splice_20260906_b7e41_audit.py)
and [saved exhaustive verification](review/COEFFICIENT_ONE_REVIEW_20260908/finite_construction/scratch/k17_literal_compress_20260905_a19f7/worker3.standard.verify.json)
are included. This remains an upper bound, not an exact optimum; the saved
verification was not rerun when publishing the proof package.

## Research record

- [`MATHEMATICAL_HANDOFF.md`](MATHEMATICAL_HANDOFF.md) is the full
  chronological research log.  Its opening status block and later explicitly
  superseding sections are authoritative; older failed conjectures and stale
  numerical intervals are intentionally retained as history.
- [`RESEARCH_INDEX.md`](RESEARCH_INDEX.md) indexes the principal proofs,
  exact certificates, and current frontier.
- [`MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md`](MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md)
  records the general lower bound.

This repository deliberately excludes multi-gigabyte generated SAT inputs,
temporary portfolios, and compiled binaries.  The retained sources,
certificates, hashes, and verifiers are sufficient to inspect and reproduce
the published finite results.
