# K17 Search Status

## Verified Word

The current proved interval is `24313 <= nu(17) <= 25745`.
The retained `answers/k17_upper25745.word` has SHA-256
`ef69969f6f72bc85173c9ccb413b7c111a398e725b956f2a91cbe5decbabca38`.
It is a deterministic reversed boundary splice of the authenticated k=16 word.
Appendix B of `MASTER_HANDOFF.md` contains the source-only proof and executable
replay. No new external word premise was added to the master.

At the numerical-bound update, the master audit passed on h100: 315164 bytes,
541 unique tags, all sixteen
source hashes/universality checks, the new k=17 splice, and the rational c4
certificate. The separate literal word verifier reported all 131071 targets
covered. The target length 24313 is NOT attained.

## Mathematical Research

After the user redirected away from brute-force search, the following
self-contained results were proved and independently reviewed in the master:

- Section 3.10: facet-forest repair on the same coordinates, the critical
  eleven/twelve-hole incidence bound, exact fixed-core Hall deficiency, and
  anchored component opening.
- Section 3.11: the prescribed invariant matching extension, optimal
  ten-deletion augmentation, and a further owner-avoiding extension. The
  latter reduces forbidden-owner deletion to a rank-four update with
  determinant ratio `-893/128125`, which is nonzero.
- Section 3.12: every length-24313 set-valued word covering both middle
  layers requires at least 28 edges in the symmetric difference between its
  selected owner chronology and its five-step old-coordinate rotation.

The invariant bulk can now be chosen to avoid all 60 packet owners. A choice
that is simultaneously degree at most two and acyclic is NOT established.
The conditional whole-cycle escape operation states its required off-cycle
destinations and degree slack explicitly; no existence of those moves is
claimed. No new numerical upper bound follows from these results alone.

The integrated master audit passed at 339445 bytes and 561 unique tags,
including both small rational inverse-block checks and all prior certificates.
No full catalogue or matching search was used for these mathematical proofs.

## Restartable Factors

Artifact root: `scratch/k17_quotient_search_20260905_f6c2e/`.
Remote root: `/home/amodo/or15/work/k17_quotient_search_20260905_f6c2e` on h100.

The second eight-worker, 360-second batch finished successfully. Independent
physical audits of all 32 exports passed. The strongest retained resident,
U1-complete restart is `continuation360/seed17091005.best.txt`, with JSON and
independent audit beside it. Body SHA-256:
`972444d25f8f2369bd47c130d97339953d3d3d430d36f73d29ca66b763b96a2e`.

- Positive short runs: zero; minimum positive run: four.
- Every rank-nine owner has degree two; every rank-eight facet occurs once.
- Missing orbit counts `[U1,L2,U2,L3]`: `[0,57,48,41]`.
- All-width upper misses at ranks 10 through 17: `[0,48,19,0,0,0,0,0]`.
- Physical cycles: `[24106,153,51]`.

The two-component alternative is `continuation360/seed17091002.residence.txt`,
with cycles `[24072,238]` and missing decks `[0,80,48,33]`.
These are incomplete factors, not source words or improved numerical bounds.

Two full-catalogue CP-SAT probes each returned UNKNOWN after approximately
609 seconds. The later fixed-M0 optimizer reduced L2 from 102 to 100, but is
inferior to the C++ continuation. Its hard-L2 probe returned UNKNOWN, not
UNSAT. Results are retained in `scratch/k17_fixed_matching_*600_result.json`;
full artifacts are under `/tmp/k17_fixed_matching_refine_20260906_d8a31`.

## Optimization And Scaling

The C++ search already uses exact alternating matching exchanges, compact
17-bit quotient tables, and signed local score updates. Physical expansion is
outside the proposal loop. The new performance changes preserve its semantics:

- Pass literal check messages as `const char *`, avoiding temporary strings.
- Cycle through incidence options without a variable-modulus operation per item.

Build: `g++ -std=c++20 -O3 -march=native -DNDEBUG -Wall -Wextra -Wpedantic`.
The updated source SHA-256 is
`5a5d09f4101f462d931dcb24a81a89764960f0a4d3d358f2556aa1350c491e4d`.
The old remote executable `search` and source were preserved; the new binary is
`search_fast`, built from `k17_quotient_search_fast_20260906.cpp`.

A same-seed, constant-temperature, two-million-attempt benchmark produced
exactly 1516131 evaluated proposals and 5774 acceptances in both builds.
Search time fell from 4.66817 to 2.70547 seconds, a 1.73x speedup. Saved body
hashes agree. Both release and ASan/UBSan passed the same four-factor suite:
1625 delta/full comparisons, 48 physical comparisons, 818 rollbacks, 55
parallel-incidence moves, and 25 preferred matching differences per build.

Sequential 12-second scaling measurements, including launch/finalization:

| Workers | Evaluated Proposals/Second |
|---:|---:|
| 8 | 4125757 |
| 28 | 13673271 |
| 56 | 18696827 |

The benchmark is `scripts/benchmark_k17_quotient_20260906.py`; its summary is
retained as `scaling_20260906_summary.json` in the local artifact root. These
are short throughput measurements, not counts of distinct states or a promise
of proportional mathematical progress. Hardware-counter profiling was denied
by `perf_event_paranoid=4`; no system settings were changed.

## Finished Timed Batch

The user subsequently redirected the work to mathematical research. Both
timed batches had already exited when the owned-worker stop check ran; no
workers remained and no unrelated process was signalled. No new brute-force
batch is scheduled. The resource figures below describe the earlier live
check, not current CPU usage. New checkpoint contents have not been promoted.

At the last check, 60 independently seeded C++ workers were runnable and
consuming approximately 6000% process CPU. Host `vmstat` measured 97% CPU busy,
zero I/O wait and no active swap traffic. Two unrelated long-running Python
jobs were left untouched. Machine: AMD EPYC 9354P, 32 cores/64 hardware threads.

Two bounded batches run under the remote root:

| Directory | Driver PID | Workers | Seeds | Per-Worker Budget |
|---|---:|---:|---|---:|
| `scaled56_1200_20260906` | 2959389 | 56 | 17100001..17100056 | 1200 seconds |
| `scaled4_alternate_1200_20260906` | 2959967 | 4 | 17100101..17100104 | 1200 seconds |

Both use `search_fast` and `k17_scaled_runner_20260906.py --phase repair`.
The first resumes the three-cycle best body; the second resumes the two-cycle
alternative. Improvements are checkpointed at five-second intervals when dirty.
The driver enforces a fallback timeout and reaps only its own children.

Each directory contains `commands.json`, per-seed logs and checkpoint bodies;
`finished.json` and `.stats.json` files appear at completion. Driver logs are
beside the directories, with `_driver.log` appended to the directory name.
These batches were RUNNING when this record was written, not verified results.
Audit any new exports before promoting their metrics, and require a literal
nonwrapping word replay before changing the numerical bound.

The separate partial-compiler attempt used four bounded workers under
`/home/amodo/or15/work/k17_partial_compile_20260906_c83a1`. Its driver had exited
at the last check, but no `summary.json` was present; its outcome still needs
inspection. No shorter word is inferred from that run.
