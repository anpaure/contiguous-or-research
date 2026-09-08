# Coefficient-one proof: external review package

Snapshot date: 2026-09-08.

The coefficient-one result is a **proposed proof with internal AI-agent reviews**. It has not received external review or formal verification. Internal PASS labels are not independent human certification. No computational verifier of the coefficient-one theorem is supplied.

Start with [MANUSCRIPT.md](MANUSCRIPT.md), then [CONSTRUCTION.md](CONSTRUCTION.md). [FULL_PROOF_TEXT.md](FULL_PROOF_TEXT.md) and [FULL_PROOF_TEXT.txt](FULL_PROOF_TEXT.txt) contain the entire manuscript and construction companion, followed by the full, unabridged text of every selected essential source. The TXT file contains the same Markdown-readable text. Contextual sources are supplied separately, including the full current MASTER_HANDOFF.md. [SOURCE_INDEX.md](SOURCE_INDEX.md) maps every document to its source and portable copy.

## What needs external mathematical review

1. The stationary core and Palm laws, and the endpoint permutation used in growing-depth clock flux.
2. Whether original insertion maps represent the actual shifted labels with the stated no-repeat and no-wrap guarantees.
3. The exact multipoint shifted-triangle law and the order r -> infinity, then S -> infinity, then K -> infinity, keeping later parameters fixed until their turn.
4. The passage to actual native partners, cross-cutoff occupied support, and packing.
5. The literal all-rank compiler, exterior tails, and even-dimension lift.

These are proof-review questions; checking selected finite dimensions cannot certify the asymptotic theorem.

## Status, finite construction, and historical sources

If correct, coefficient one is a stronger leading asymptotic constant. The manuscript supplies no explicit convergence rate or crossover dimension. It does not deliver an improved finite k=17 word or an executable implementation of the new PBBS construction.

The files under `finite_construction/` preserve the earlier 25,745-letter k=17 word, its k=16 input, generator/audit script, verifier, saved verification result, and run log. **The supplied k=17 verifier pertains only to that older finite 25,745-letter word. It was not rerun for this packaging task.** The saved result is prior provenance, not a fresh validation. The finite ledger note records its own earlier remote evaluation; packaging only copied it.

Historical precursor text marked open or retracted is preserved. The newest manuscript proposes resolving a specific overlap/packing gate; it does not adopt every assertion in the older notes. The handoff and companion may mention the user's later 1.15325 coefficient claim as awaiting audit; that claim is not promoted to an independently certified result in this package.

## External theorem and scope of completeness

The full-label foundation uses Kuniba–Sakamoto, *Combinatorial Bethe ansatz and ultradiscrete Riemann theta function with rational characteristics*, [arXiv:nlin/0611046v2](https://arxiv.org/abs/nlin/0611046v2), particularly Theorem 5.1. The local coordinate-homomesy audit explaining that use is included. The paper is not redistributed. **This package is not claimed to be entirely self-contained.**

Portable copies rewrite local Markdown links when their targets are included. References outside the selected dependency chain, including unrelated historical links in the handoff and precursor material, are flagged in [UNINCLUDED_LOCAL_LINKS.md](UNINCLUDED_LOCAL_LINKS.md). Bare filenames in source prose can be resolved through the source index. Byte-for-byte source texts are preserved under `originals/`, including all original local links.

## Integrity and packaging validation

`SHA256_SOURCES.tsv` records source paths, byte counts, hashes, originals, and portable copies. `SHA256SUMS` covers package files other than itself. `PACKAGING_VALIDATION.json` records file-assembly checks. The ZIP archive was tested for member integrity after creation. No mathematical calculations, enumerations, word searches, proof scripts, or finite-word verifiers were executed to build this package.
