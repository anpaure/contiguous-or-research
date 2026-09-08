# Independent audit: complete `k=13` relative-permutation architecture

Date: 2026-07-24

## Verdict

**PASS.**  The Purple RunPod certificate formally excludes the whole specified
relative-bit-permutation architecture

\[
B\;\Vert\;(2^{12})\;\Vert\;
\bigl(2^{12}\vee\pi(O_i):i\notin\{a,b\}\bigr),
\]

where `B` is the fixed 926-entry optimal nonzero `k=12` word, `O` is either
`B` or its reversal, `0 <= a < b < 926`, and `pi` is any permutation of the
12 old coordinates.

The exact excluded count is

```text
2 * C(926,2) * 12! = 410,288,820,480,000 architectures.
```

This is a theorem about this one length-1,851 architecture.  It does **not**
exclude other length-1,851 words and does not change the certified finite
bound on `nu(13)`.

## Checks performed

### 1. Full deletion-pair scans

The profile source and base word were compiled/read afresh on Purple.  Both
orientation scans reproduced the original outputs and ranked profiles
byte-for-byte:

```text
pairs=428275 feasible=1318 retained=5000 reverse=0 suffixes=8
pairs=428275 feasible=1318 retained=5000 reverse=1 suffixes=8
```

For each orientation:

- the hole histogram totals exactly 428,275;
- the retained profile has 5,000 distinct valid deletion pairs in the exact
  source-defined order;
- precisely its first 1,318 rows are individually feasible;
- the source scans all `C(926,2)` pairs and sorts feasible rows before every
  infeasible row.

Therefore the top-5,000 retention did not discard a feasible pair.  The exact
rank filter excludes every permutation of each of the other 426,957 pairs.

The fresh ranked-profile hashes are the original hashes:

```text
7ee09326c2c45f81260f0f15ec350acb6f62df5ffe2509f56eda9ee3d15b7588  forward
534d99011f32a2d794bf22b425f9f16fbf444eb2b0c6326b620beeac147ac840  reversed
```

### 2. Exact manifest partition

Each orientation has six manifests of sizes

```text
250, 250, 250, 250, 250, 68.
```

The JSON block hashes match the current pair files.  Within each orientation,
the 1,318 manifest rows are distinct, all have the feasible flag set, and
their ordered union equals the complete set of feasible rows in the ranked
profile.  No feasible row is omitted or repeated.

### 3. Certified CNFs are reproducible

The exact generator was freshly compiled from the hash-recorded source using
`-Wall -Wextra -Wpedantic`.  It regenerated every block from the base word and
its pair manifest.  All 36 regenerated artifacts matched their certified
counterparts byte-for-byte:

```text
12 CNFs + 12 maps + 12 stats = 36 exact matches.
```

For every map, the audit also checked independently that:

- all 144 source/target entries of the `12 x 12` permutation matrix occur
  exactly once;
- its pair selectors equal exactly the deletion pairs in that block;
- the DIMACS variable/clause counts equal the block stats;
- `impossible_holes=0`, as required for a feasible manifest.

This ties each DRAT proof to the actual architecture CNF, rather than merely
to an opaque stored formula.

### 4. All twelve UNSAT proofs

Every original pre-solve and UNSAT-certificate SHA-256 ledger passes
`sha256sum -c`.  Each Kissat status is `KISSAT_EXIT:20`, each original
`drat-trim` log contains `s VERIFIED`, and each block has its
`UNSAT_VERIFIED` marker.

The proofs were then independently checked again on Purple.  All twelve fresh
`drat-trim` invocations returned exit code zero and printed `s VERIFIED`.
Their durable rerun ledger is

```text
/root/k13_relperm/certified/audit_rerun_20260724/exit_codes_rerun2.tsv
SHA-256 488be37f3f8887bf8434c081ffeea0589bbf62daacab64db27a7f8eb90204888
```

Both six-block ledgers end in `SEARCH_COMPLETE_NO_SAT`.  There is no genuine
`.SAT_VERIFIED` marker and no candidate word in the certification directory.

## Exact partition of the excluded family

```text
closed by the exact infeasibility filter:
  2 * (428275 - 1318) * 12! = 409,026,172,262,400

closed by the twelve DRAT-certified CNFs:
  2 * 1318 * 12! = 1,262,648,217,600

total:
  410,288,820,480,000
```

The earlier portfolio note printed `1,262,808,422,400` for the middle line.
That was only an arithmetic typo; the certified scope is the corrected value
`1,262,648,217,600`, and the full-family total was already correct.

## Reproduction artifacts

Remote, preserved on Purple:

```text
/root/k13_relperm/certified/audit_profile_regen_20260724
/root/k13_relperm/certified/audit_regen2_20260724
/root/k13_relperm/certified/audit_rerun_20260724
```

Local compact auditor:

```text
scratch/audit_k13_relative_bitperm_full_certificate.py
SHA-256 2437aa1d9032bb7922263ee1138002469cb7456bd0fe5bc0393425ccfb8b722a
```

Its successful output is:

```text
PASS k13 relative-permutation full-certificate audit
pair_scans=2*428275 feasible_rows=2*1318
manifest_blocks=12 certified_unsat_blocks=12 fresh_drat_exit0=12
regenerated_profile_matches=2 regenerated_cnf_map_stats_matches=36
architectures_closed=410288820480000
architectures_closed_by_drat=1262648217600
architectures_closed_by_exact_filter=409026172262400
```

The compact auditor also reruns the independent small-instance reduction audit
through five bits, which checks the maximal-prefix dominance and provider
reduction against direct enumeration.

