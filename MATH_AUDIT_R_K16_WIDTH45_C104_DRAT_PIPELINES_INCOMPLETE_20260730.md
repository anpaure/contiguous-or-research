# K16 WIDTH45 C104 DRAT pipelines: fail-closed incomplete status

Date: 2026-07-30  
Lane: R  
Status: **no certificate; no freeze; no theorem**

Two already-running H100 Kissat proof pipelines were monitored without a
restart or duplicate. Neither returned a recorded SAT/UNSAT verdict.

## 1. Repeat-free pipeline

The repeat-free CNF has SHA-256
`a5b657078ec4adb1ff130b56277d470f60489c3af61b857dc5f2267310bf67d7`,
3,075,424 variables, 9,164,911 clauses, and 28,748 cycle variables. Its exact
scope is only the repeat-free ledger: every target exactly once, global Sep5,
and total slack eight; the per-cycle identity then forces length 104.

Wrapper PID 70496 and Kissat PID 70499 ended before their 1,800-second
deadline. Both solver logs remained empty, no exit code was preserved, and
the partial proof was absent at the first post-termination audit. A separate
CaDiCaL lane said only `c UNKNOWN`. Therefore there was no proof to replay.
No negative conclusion follows.

The solver wrapper had one thread and a time bound, but no hard address-space
cap and no resource log. The largest observed RSS was 500,768 KiB.

## 2. Complete-atlas pipeline

The complete CNF has SHA-256
`4e71ab504c4adb1ff130b56277d470f60489c3af61b857dc5f2267310bf67d7`,
5,869,298 variables, 20,090,876 clauses, and all 29,284 cycle variables. Its
exact scope is the complete frozen residual-cost-at-most-eight cycle atlas:
pairwise Sep5-compatible cycles, all 93 targets covered, exact total length
104, and physical slack at most eight. A verified UNSAT proof would exclude
C104 only inside this frozen WIDTH45 seam/atlas model. It would not cover
another carrier, absent reverse/exterior-moving seams, unrestricted
rethreading, or a literal K16 word theorem.

Wrapper PID 76156 and Kissat PID 76157 ran to the 1,800-second timeout with
empty solver logs and no preserved verdict or exit code. The retained partial
proof is 1,929,379,840 bytes with SHA-256
`dee65944f23d967513416d9e2846ddbf9990eb2d0c009da8a74f830187015273`.
It was not copied locally.

The existing fail-closed auditor was run once, on one H100 CPU, under an
external 2 GiB address-space cap and 660-second wrapper timeout. `drat-trim`
reported return code zero but its complete transcript was:

```text
c turning on binary mode checking
c parsing input formula with 5869298 variables and 20090876 clauses
c MEMOUT: reallocation of clause database failed
```

There is no literal `s VERIFIED` line. The fail-closed Python auditor
therefore rejected the run, returned status 1, and created no PASS JSON.
Maximum RSS was 1,887,232 KiB and wall time was 56.14 seconds. No further
checker or solver run was launched.

The original complete Kissat wrapper itself had no hard memory cap or
resource harness. Its maximum observed RSS was 3,598,092 KiB, exceeding the
2 GiB working envelope; that number is an observation, not a guaranteed
peak.

## 3. Frozen small records

```text
scratch/k16_width45_c104_drat_pipeline_fail_closed_status_20260730.audit.json
scratch/k16_width45_c104_norepeat_exact_cnf_20260730.manifest.json
scratch/k16_width45_c104_complete_exact_cnf_20260730.manifest.json
scratch/k16_width45_c104_complete_partial_drat_20260730.stderr.txt
scratch/k16_width45_c104_complete_partial_drat_20260730.resource.txt
```

The 1.8 GiB partial proof is deliberately not duplicated locally. Neither
pipeline authorizes a freeze, a C104 no-go, or any theorem-level promotion.
