# Independent exact21/22 forward certificate provenance

Executed exactly once on 2026-09-09, h100 / hostname arboghast, after root
and induction-agent full pre-execution source/plan review. The finite-frontier
agent also reread the complete source and derivative diff. No retries,
search, alternate inputs, cyclic extensions or source edits followed the
frozen-source approval. The earlier 352862/705724 forward checker was never run.

Source SHA-256:
`ce205cef9f5f2208bcaccd1bb2f1d25ecd29f19f01782c17040ab89874080312`.

Input hashes, checked both locally and remotely before execution:

- k21: `eb44ff87a669ae0163bdf926283c22c5494e08322efb5c947994a676dc3af1d2`.
- k22: `a32fe59af4511fcf1a0e032e3f57ae358a9b74492a3f6d56aa8f4564c77ba2dd`.

Remote output directory:
`/home/amodo/exact-b-k21-k22-optimal-forward-20260909/`.
The exact invoking command is in [exact_command.txt](exact_command.txt).

Hard limits: 60 CPU seconds, 90 wall seconds, 2 GiB address space,
256 MiB per file. External guard: `timeout 90s`. Exit code: 0.
Actual CPU: 7.738175413 seconds. Actual wall: 7.739107304718345 seconds.

Final status: PASS_OPTIMAL_FULL_CUBES. Complete ordinary coverage passed
for all 2,097,151 targets at k21 and all 4,194,303 targets at k22. The
independently computed lower bounds equal the respective 352,719- and
705,435-letter lengths. No cyclic-core, lift or constructor claim is
part of this independent forward run.

Paired report SHA-256:
`137029022789f1af18e949c870945a8b1d0bfb874b9e306f792b82770bdeb4fb`.

All 12 files in the remote-generated [SHA256SUMS](SHA256SUMS) were copied
locally and passed `shasum -a 256 -c SHA256SUMS`. This includes the raw
words, source snapshot, per-word and paired reports, all four complete
little-endian int32 witness arrays, started marker and log. The provenance
and exact-command files were added locally after that check. No additional
mathematical execution took place during copying or hash verification.
