# R2 k=17 exact3664 functional-q1 all-UNSAT theorem

Date: 2026-08-02

## Theorem

For every case in the frozen 3,664-row exact-clean-anchor catalogue, the
corresponding `Q1_ONLY` CNF for the cyclic relaxed-residence functional
owner/tail/head/lower-colour factor is unsatisfiable.

The catalogue is
[`cases.tsv`](scratch/r2_k17_exact3664_final_audit_20260802/cases.tsv),
SHA-256
`860924cbb256d320ee35790e98ebd1e78bf0b01cdabf1bdbf9fdaef0929fa109`.
It has case IDs exactly `0..3663`, 3,664 distinct jobs, and 3,664 distinct
canonical bank keys.

The exact proof ledger is
[`proof_manifest.tsv`](scratch/r2_k17_exact3664_final_audit_20260802/proof_manifest.tsv),
SHA-256
`0706fee2c9dba89c6339ca2088c9edc021f0d5107f0c1ddf1e344129fa3f92d3`.
It contains one `UNSATISFIABLE` row for every case and no SAT, unknown,
duplicate, or missing row.

## Proof audit

### Literal case and bank coverage

An O3 structural verifier independently parsed the complete candidate ledger
and round02 baseline, reconstructed both advertised recuts in every case, and
required every retained bank to equal the resulting 3,805-cut vector.  It
also bound jobs, keys, moves, formula dimensions, core sizes, and certificate
paths.

The resulting combined structural ledger is
[`combined.tsv`](scratch/r2_k17_exact3664_final_audit_20260802/structural/combined.tsv),
SHA-256
`5daca8ac4cbab07fec6994fb7c105a6411fd75e01920724cad711929056b7d2a`.
All 10,992 expected bank/core/lemmas hashes replayed successfully; the check
log has SHA-256
`496cb4a8920eea344ffb7aa318771d5d5f43ec784455ca0027164d9eea5ccfcf`.

### Uniform CNF and core-subset post-audit

The complete independent post-audit rebuilt each CNF from its retained bank,
required the fresh CNF SHA-256 to equal the proof-ledger value, checked the
retained core as a literal subset of that CNF, and verified its reduced DRAT
proof.  Its summary is
[`postaudit.summary.tsv`](scratch/r2_k17_exact3664_final_audit_20260802/postaudit.summary.tsv),
SHA-256
`8777f67313b010091e7596d3b3539a9bb6424abae40be1d1fccb2e69d3df5f81`.

All 3,664 rows are `PASS`.  The proof-ledger/post-audit join independently
checked case ID, worker provenance, and bank/CNF/core/lemmas hashes for every
row.  Its output has SHA-256
`2005ca06d30284d9868d9dc0322b4fd571f5933e2186ac88799e9547634984ea`.

Worker provenance is exactly:

```text
initial worker                 273
independent quarantine           3
patched worker                3388
total                         3664
```

### Retained artifact and proof replay

The retained certificate manifest is
[`certs.SHA256SUMS`](scratch/r2_k17_exact3664_final_audit_20260802/certs.SHA256SUMS),
SHA-256
`487170d4dfb48ef5315884d0b001762a22e5d8dcb00a75b99cf1cbe511f532cb`.
All 21,984 entries replayed without failure; the check log has SHA-256
`bbe1daf1ab0704f505fdd3670ff0fbc57c5bcfe75ed9c0d54f382b6034206c92`.

Finally, a separate proof-only pass independently rehashed every retained
core and lemmas file, checked the recorded clause/lemma counts, and reran
`drat-trim` on all 3,664 reduced proofs.  Every fresh checker invocation
returned `s VERIFIED`; no SAT solver was run.  The exact per-case ledger is
[`core_recheck/summary.tsv`](scratch/r2_k17_exact3664_final_audit_20260802/core_recheck/summary.tsv),
SHA-256
`0542f58ba29240337f0545b21013ea7d40ccc53175b17c5668cfca529c1223e4`.
Its theorem payload has SHA-256
`5f1cdb7089afbb17bfef91c0302efb09139d467195e9a8816b287c07f77c203a`,
and all 10,992 generated audit artifacts replayed successfully.

These checks establish case completeness, exact bank identity, fresh formula
identity, core containment, and a verified contradiction for every case.

## Cutover anomaly

Cases `273..275` were originally mislabeled `UNKNOWN:126` when the live worker
was edited in place.  Their Kissat logs already contained UNSAT/exit 20, but
the corrupted wrapper skipped proof checking.  A separate quarantine rebuilt
and solved exactly those three formulas, verified full and reduced proofs,
and was then explicitly adopted into the main ledger.  The quarantine audit
is frozen in
[`MATH_AUDIT_R2_K17_EXACT3664_UNKNOWN126_QUARANTINE_20260802.md`](MATH_AUDIT_R2_K17_EXACT3664_UNKNOWN126_QUARANTINE_20260802.md).

The adopted main rows retain markers and the original `UNKNOWN:126` rows in
provenance.  Their bank, CNF, proof, core, and lemmas hashes equal the
quarantine ledger exactly.

## Exact dimensions and authenticated tools

```text
variables       899376 .. 900784
clauses        2446642 .. 2450514
core clauses        16 .. 333
core lemmas         16 .. 1273

builder          9aeb67e7c8730c95da606213a79a415d1bfe8714aff9f6074d19e61a4fa9cd9e
core-subset tool 2083cbaca8b3d698c36e69d0d28287756d846d899c8564c1da6c8f0e7bd4d6bc
drat-trim        92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a
```

The producer theorem payload is
[`final.audit.json`](scratch/r2_k17_exact3664_final_audit_20260802/final.audit.json),
SHA-256
`2717e038b4e10ee478b791c614a80b83cea6ca01e5eb156d9bfc898e952b5f37`.

## Scope

This theorem closes only the exact `Q1_ONLY` functional factor for the frozen
3,664 clean-anchor banks.  The formulas explicitly have no rank10-row
encoding.  The result does not claim selected rank10 coverage, ranks 11--17,
component topology, exact global residence, exterior windows, rooted
`ae88` state, the terminal compiler, or a complete contiguous-OR word.

The 49 dirty-central compensated formulas form a separate proved package and
are not silently merged into this 3,664-case statement.
