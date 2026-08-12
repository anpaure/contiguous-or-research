# k=11 exact onion-split portfolio on RunPod (2026-07-24)

## Objective

Resolve the first unknown finite case.  For nonzero masks the proved rank
bound is

\[
465\le \nu(11)\le477.
\]

The portfolio tests the corrected exhaustive length-465 Type-I/Type-II
onion split.  A verified SAT witness in either type proves
`nu(11)=465`.  Only checked UNSAT for both exhaustive types can raise the
lower bound.  A killed, silent, timed-out, or resource-exhausted process is
not mathematical evidence.

## Host and executable

- RunPod host: Rose, `root@157.157.221.29:27423`, container
  `f93817d72edc`.
- Work directory: `/root/k11_exact_portfolio_20260724`.
- Solver source/binary family:
  `/root/k11_onion_20260723/k11_forest_sat_newcuts`.
- Audited source hash:
  `2ab8ce03f844884c1dc6c5b4f742fe6e447680589172610fcd9649906ebdc26c`.
- Binary hash:
  `bd7c79dd68e82d5045d589be45bd7099afacdd49f7fc10decd9157582b45e392`.
- Input `k11_upper549_natural_array.txt`, hash:
  `c508307dcc666b0e5c0b11ff96cb129df82d74d3b34d2d3aec4adf7b861c8ebd`.

The common cut set enables adjacent and rank-3 shadows, band and joint-band
cuts, endpoint alignment, canonical rank-6 entry, singleton pool, rank-6
boundary entry, local-density PB, containment caps, subcube deficiency,
named-cell Hall, residual-coordinate lex, and rank-7 truncated width.
Type I additionally enables its rank-6 branch, filtration, prefix-chain,
facet/ridge pin-load, and global pair-profile cuts.  Type II enables its
filtration plus two-component localization, reverse pin-load, and companion
pin-load cuts.

The audited formula inventories are:

- Type I: 3,671,659 variables and 20,175,646 clauses.
- Type II companion-pin: 3,686,611 variables and 20,247,467 clauses.

## Launch ledger

Nine exact searches were launched simultaneously at 2026-07-24 01:09:35
UTC, four Type I and five Type II:

| type | seed | pinned CPU | wrapper PID | status at 2026-07-24 01:15 UTC |
|---|---:|---:|---:|---|
| I | 401 | 0 | 172286 | `EXIT:137` |
| I | 402 | 2 | 172287 | live (solver 172297) |
| I | 403 | 16 | 172288 | live (solver 172301) |
| I | 404 | 18 | 172289 | live (solver 172298) |
| II | 411 | 20 | 172290 | `EXIT:137` |
| II | 412 | 21 | 172291 | `EXIT:137` |
| II | 413 | 22 | 172292 | `EXIT:137` |
| II | 414 | 28 | 172293 | `EXIT:137` |
| II | 415 | 31 | 172294 | live (solver 172303) |

At the 01:19 UTC poll all candidate files and solver stdout files were empty and no
SAT, UNSAT, or UNKNOWN marker existed.

At the final active-monitoring snapshot, 2026-07-24 01:38:01 UTC, the same
four solvers remained live with about 28m19s CPU time each.  Their current
RSS values were 3.44--3.93 GB and their observed high-water marks were
5.11--5.14 GiB.  Every candidate and stdout file was still empty, and no
terminal marker existed.

## Resource diagnosis

The five `EXIT:137` outcomes are cgroup OOM kills, not solver conclusions.
Although host-level `free` reports 124 GiB, this container is cgroup-v1
limited to exactly 32,000,000,000 bytes with no swap.  Read-only cgroup
evidence showed:

- `memory.max_usage_in_bytes = 32000004096` (the limit was hit);
- `memory.oom_control` reported `oom_kill 35`;
- the memory+swap failure counter was 15,835,644.

The surviving solvers had observed high-water marks around 5.11--5.14 GiB
each.  Three older `recombine_paths` jobs remained in the same cgroup.  At
01:38 UTC cgroup usage was 22,499,581,952 bytes, leaving 9,500,418,048
bytes.  One new solver at the worst observed high-water mark would leave
only about 4.24 GB of safety margin, below the required 5 GB.  Therefore no
killed job was relaunched.  Relaunches must be staggered and should wait
until at least a 5 GiB post-HWM margin is available.

## Verification policy

If a nonempty candidate appears, copy it to the workspace and independently
verify all masks by two separate verifiers before promoting it.  If a solver
reports UNSAT without a proof artifact, rerun the corresponding archived CNF
with a proof-producing solver; an uncheckable terminal string is not an
exact lower-bound certificate.

## Co-resident legacy jobs

Three older `recombine_paths_sat_new` searches (seeds 309, 310, and 312)
have run since 2026-07-22 11:37 UTC.  They currently consume about 5.8 GB
private memory in aggregate and have accumulated roughly 38 hours of
single-threaded solver state apiece.  They search a restricted fixed-row,
delay-three Hamilton-path construction neighborhood, not the globally WLOG
length-465 onion split.  Their stdout files are empty and they have no SAT,
UNSAT, UNKNOWN, candidate, or proof artifact.  Their logs preserve explicit
lazy-cut ledgers but not learned clauses or a resumable checkpoint.

Stopping them sacrificed no present mathematical evidence, but did destroy
three distinct non-checkpointed heuristic trajectories.  They were initially
left running.  When later cgroup use rose to 28.56 GB and threatened the four
globally exhaustive jobs, the three restricted solvers were terminated with
SIGTERM.  The exact binary and all inputs remain hashed for restart-only
reproducibility.

## Low-memory next deployment

The authoritative generator already supports DIMACS export.  The preferred
next portfolio builds each exhaustive branch once, hashes and audits the
immutable CNF, and then reuses that file for every search seed and any final
proof-producing run.  A build-only CaDiCaL API shim can stream the raw clause
sequence directly to DIMACS, avoiding an in-memory solver database during
generation.  It must first be compared against the audited inventory on
RunPod and must use persistent storage rather than cgroup-charged `/dev/shm`.
Commands and proof policy are recorded in
`K11_LOW_MEMORY_CNF_RUNBOOK_20260724.md`.

This deployment has now been validated on Rose.  Full Type-I and Type-II
streaming builds used only 148,472 KiB and 152,220 KiB peak RSS respectively,
and produced token-audited immutable CNFs with hashes

```text
79bb1c579bd44e274cf499adcbcb1aef83cf237c0aaac88002dbda09a99cd69e  Type I
508f389e2ad3fff49984a2117a060437fcf3446ccdc96b8b30ac6e69eb039c15  Type II
```

An external Type-II Kissat seed 411 is running against the latter file under
a hard 4 GiB virtual-memory cap.  This is an additional exhaustive Type-II
search, not a replacement for the four surviving integrated jobs.

At 2026-07-24 02:15 UTC that streamed Type-II run remained live at about
1.70 GB RSS and 2.27 GB virtual size, with no terminal marker.  Its measured
footprint permitted one further staggered launch while retaining several GB
of cgroup headroom.  External Type-I Kissat seed 421 was therefore started
against the immutable Type-I CNF on CPU 22 under a hard 3 GiB virtual-memory
cap.  Its wrapper/solver PIDs were 176901/176903.  At launch all four
integrated searches and both streamed-CNF searches were live, no candidate
file was nonempty, cgroup use was about 25.0/32.0 GB before the new process,
and the OOM-kill counter had not increased.

To protect those globally exhaustive searches when cgroup use reached
28.56 GB, the three legacy restricted `recombine_paths` jobs were terminated
with SIGTERM.  Their output files were still empty.  Their logs, frozen
binary, inputs, commands, and hashes remain; only their non-checkpointed
learned-clause/search state was lost.  Cgroup use immediately fell by about
6 GB.

## Strengthened core-incidence branch

The audited physical-cell inequalities were implemented in a separate
opt-in source; the frozen production source above remains unchanged.  The
new streamed CNFs have inventories and hashes

```text
Type I:  3,675,716 variables / 20,204,041 clauses
4b4c91b7b2fb801fc6b65329c6f94396d9199d6a6ff38666b74e252f7327ac68

Type II: 3,690,668 variables / 20,275,872 clauses
fface46a574c29b99425fc78725caa5535bcd740adba550391d85ba414885a1f
```

Both passed token-level maximum-variable and clause-terminator audits.  The
source hash is

```text
02d2f1cf7089b10b529a0f66afb353638ec3946988038f77bf534850f5815c5d.
```

External Type-I baseline seed 421 was stopped after about twelve minutes,
with no terminal marker, and replaced at the same concurrency by strengthened
Type-I seed 431 under a hard 3 GiB virtual-memory cap.  The three older
integrated Type-I jobs remain live.  Thus this replacement spends the extra
external trajectory on the strictly stronger exact formula without reducing
the original branch coverage.

The subsequent rank-histogram surplus refinement strictly strengthens those
rows and was independently source-audited.  Its Type-I formula has

```text
3,680,003 variables / 20,233,379 clauses
SHA-256 437bd28e5a97a680a55f297a46d16312ed31797988aae9e1452cc207911ac616.
```

After confirming that seed 431 still had no terminal result, it was replaced
at the same concurrency by histogram Type-I seed 441.  The new source hash is
`447b17b9eb91910fb8159e6933b9e0e05b09ee884980a4303f07c4562f9867aa`.
The exact proof and implementation audit are in
`K11_HISTOGRAM_SURPLUS_CELL_CUTS_20260724.md` and
`K11_HISTOGRAM_CUTS_AUDIT_20260724.md`.

The matching Type-II histogram formula was subsequently streamed and audited:

```text
3,697,194 variables / 20,319,956 clauses
SHA-256 1f5c776c87b0efc8ec8fe249299626554e59d7c65960eed520c612ba5b5aeed7.
```

External baseline Type-II seed 411 had no terminal result and was replaced,
at unchanged concurrency and with the same 4 GiB cap, by histogram seed 451.
The older integrated Type-II seed 415 remains live.  Thus the active portfolio
now consists of three frozen integrated Type-I baselines, one frozen integrated
Type-II baseline, and one histogram-strengthened external search per branch.

The two now-unused intermediate core-incidence raw CNFs were compressed with
`zstd`; each compressed stream was decompressed through SHA-256 before its raw
copy was removed.  They remain fully recoverable as
`k11_type{1,2}_corecuts.cnf.zst` with the same archived raw hashes.
The two unused frozen-baseline raw CNFs were handled identically after both
external baseline solvers had stopped; their `.zst` streams reproduce raw
hashes `79bb1c...cd69e` and `508f38...39c15`.  The two live histogram CNFs
remain raw for their active solver processes.

At `2026-07-24T03:13:02Z`, all six exhaustive solver processes and the
terminal-verification watcher remained live.  The four integrated baselines
had elapsed about 7,406 seconds; histogram seeds 441 and 451 had elapsed
about 1,730 and 1,530 seconds.  No candidate file was nonempty and no
terminal marker had appeared.  Cgroup use was 28,878,581,760 of
32,000,000,000 bytes, and the `oom_kill` counter remained 35.  No additional
solver was launched.

## Exact short-cell rank-vector branch

The audited total-`R3` physical-cell refinement was implemented first and
confirmed by warning-free RunPod build-only streams.  A strictly stronger
length-resolved package was then added before committing solver time.  The
frozen opt-in source is

```text
scratch/k11_core_incidence/k11_forest_sat_rankvectorcuts.cpp
SHA-256 15eb618401de15257621f6a1ef695110ad3d8ac84a45af4f539f839fa713b1a3
```

and the warning-free RunPod streaming binary is

```text
SHA-256 30e200941dc619457a1a501bebe6e45f7ea013be1dab8ff4ed1b193fcb4de813.
```

Two independent source audits verified the exact pair/triple OR gates,
per-cell popcounts, rank flags, corrected Type-II guards, selected-rank-five
rows, and contaminated-triple tail.  Both build-only inventories matched the
symbolic prediction exactly:

```text
Type I:  3,742,531 variables / 20,651,922 clauses,
Type II: 3,762,230 variables / 20,754,457 clauses.
```

Only the Type-II raw CNF was materialized.  A token-level scan verified its
header, maximum literal, and all clause terminators:

```text
p cnf 0003762230 000020754457
maxvar=3762230 clauses=20754457
SHA-256 93b3ece194b2119d0a962cc7c548fa12d5dd0a2d21283a8504a5c59c02842343
```

The exact proof and implementation audits are
`K11_SHORT_CELL_RANK_VECTOR_CUTS_20260724.md`,
`K11_R3_CNF_ENCODING_AUDIT_20260724.md`, and
`K11_SHORT_CELL_RANK_VECTOR_CNF_AUDIT_20260724.md`.

External Type-II histogram seed 451 had run for about 3,386 seconds with no
SAT, UNSAT, UNKNOWN, or candidate marker.  It was terminated cleanly and
replaced at unchanged concurrency by rank-vector seed 461 under the same
4 GiB virtual-memory cap on CPU 20.  The older integrated Type-II seed 415
remains live, so exhaustive Type-II branch coverage was preserved.  At
`2026-07-24T03:44Z`, the new parser/solver was live, the cgroup used about
28.0/32.0 GB, and the OOM-kill counter remained 35.

The terminal watcher was updated to include the rank-vector log and restarted
without losing its status ledger.  Its new remote SHA-256 is

```text
9f8f2937ab533455625aeceb8dc632bb073d46560de48029a0dec63b40c9666d.
```

As before, SAT is promoted only after decoding and both independent OR
verifiers pass.  UNSAT is only a trigger for a proof-producing rerun.

The Type-I rank-vector formula was subsequently materialized and passed the
same token-level audit:

```text
p cnf 0003742531 000020651922
maxvar=3742531 clauses=20651922
SHA-256 c888989126ede379322b613a77c29eeeb835cf9f32ac91effbdb8fbbf11c9ec3
```

External Type-I histogram seed 441 had run for about 4,000 seconds with no
terminal marker or candidate.  It was replaced at unchanged concurrency by
rank-vector seed 471 under the same 3 GiB cap on CPU 22.  Three older
integrated Type-I baselines remain live.  Both unused histogram raw CNFs were
then compressed on RunPod, decompressed through SHA-256, and only after that
had their raw copies removed.  The recoverable archives reproduce hashes
`437bd28e...1ac616` and `1f5c776c...5aeed7`.  With both rank-vector searches
parsed and live, cgroup use returned to roughly 27.6/32.0 GB after clean page
cache eviction; the OOM-kill counter remained 35.

The terminal watcher was extended again to monitor Type-I rank-vector seed
471.  Its current remote SHA-256 is

```text
09d5cad763909f789ee5681330bb8d3349e7b57dd465774e4243d0e1f1dd7ee0.
```

At `2026-07-24T04:02:16Z`, all six exhaustive solvers and the watcher were
still live.  The four integrated baselines had elapsed about 10,360 seconds;
rank-vector seeds 461 and 471 had elapsed about 959 and 622 seconds.  Their
logs contained no SAT, UNSAT, or UNKNOWN marker, and every candidate file
remained empty.  The cgroup used `27,780,800,512` of `32,000,000,000` bytes;
the `oom_kill` counter remained 35.  No additional solver was launched.

## Coordinate-omission build-only refinement

The cheapest one-coordinate omission projection was added in a separate
opt-in clone, leaving all frozen formulas unchanged:

```text
scratch/k11_core_incidence/k11_forest_sat_omissioncuts.cpp
SHA-256 f851f651e7d61e7126e25d097ab7bdb9e8f5b7a253c012a3fb26f03be197c350
```

For every coordinate it exactly counts low positions omitting that
coordinate and enforces threshold 193 in Type I/tight Type II and 130 in
non-tight Type II.  Two independent source audits passed.  The static
checker passed on RunPod, compilation there emitted no warnings, and the
streaming binary has SHA-256

```text
91bac1a91a0cf90181e5bcd8bac2a4cbf5992e2ac02aca8aeb36ae461fabf98f.
```

Build-only `/dev/null` streams exactly matched:

```text
Type I:  3,757,755 variables / 20,738,107 clauses,
Type II: 3,777,488 variables / 20,840,854 clauses.
```

No raw CNF was retained and no live search was changed.  The source is being
kept build-only while the still cheaper coordinate-companion and PT5 rows
are integrated and audited.

Those final rows are now present in the further opt-in clone

```text
scratch/k11_core_incidence/k11_forest_sat_filtercuts.cpp
SHA-256 f08430662d2b3af8bf16c30748e78c5fa324423e18bed6977c48ea69338124fe
```

The coordinate companions add only `702/5,057` in Type I and `702/5,079`
in Type II.  The independent non-tight Type-II PT5 row adds `69/473`.
Independent source audit and static arithmetic checks passed.  RunPod
compilation emitted no warnings; streaming binary SHA-256 is
`1bcb40027d404639cdac54bd79a92ac08eeebacb3dceff3ca4e0247e2098582e`.
Build-only streams exactly matched

```text
Type I:  3,758,457 variables / 20,743,164 clauses,
Type II: 3,778,259 variables / 20,846,406 clauses.
```

The stronger source remains build-only.  No raw CNF was retained and no live
search was changed.

At `2026-07-24T04:26Z`, external Type-I rank-vector seed 471 terminated with
`KISSAT_EXIT:134`.  Its log states

```text
fatal error: out-of-memory reallocating from 536870912 to 1073741824 bytes
```

under its 3 GiB virtual-memory cap.  The cgroup OOM counter did not change,
and the log contains no SAT/UNSAT/UNKNOWN marker or candidate; this is not a
mathematical result.  Its immutable raw formula was compressed, decompressed
through SHA-256 `c8889891...f11c9ec3`, and only then deleted.

The freed slot was replaced at unchanged exhaustive concurrency by the
strictly stronger Type-I filter formula.  Its raw DIMACS passed a complete
token audit:

```text
p cnf 0003758457 000020743164
maxvar=3758457 clauses=20743164 literals=70887431
SHA-256 e9e4fdbf7e5aceb7f7dddb4283da81a383d70f741a5f478bea3599149ab115f0
```

Kissat seed 481 now runs on CPU 22 under a 4 GiB virtual-memory cap.  Its
wrapper/solver PIDs at launch were `202395/202398`.  The watcher was extended
to this log and restarted as PID 202394; its SHA-256 is
`5a3363a7...4508f56`.  The three integrated Type-I baselines and all Type-II
coverage were otherwise untouched.  At launch the cgroup used about
28.1/32.0 GB and
the OOM-kill counter remained 35.

## Coordinate-pair build-only refinement

The next opt-in source is

```text
scratch/k11_core_incidence/k11_forest_sat_paircuts.cpp
SHA-256 93ad0da8256f5d180c02627cadede23c00db1d58a2ccdb0c0ed25c4818924913.
```

It adds the 55 exact pair-omission counters, the optional non-tight
`3*Z_bc+n5>=384` boundary row, and the stronger non-tight incidence row

```text
2*Tge5+n5 >= Pge5+462.
```

The static checker passed under RunPod Python 3.11.  Two independent agents
audited the actual source diff.  Warning-free RunPod compilation against the
streaming shim produced binary SHA-256

```text
9bc92c38e838f4bbfa2b9afbc0a45a7cbda7e8e7166d5d23f79275c40f83092e.
```

Build-only streams matched the symbolic inventories exactly:

```text
Type I, rank vector + occurrence + companion + B2:
  3,834,577 variables / 21,173,979 clauses.

Type II, B2 + B2-r5 + PTge5 + retained PT5:
  3,858,089 variables / 21,301,899 clauses.
```

No raw formula was created and no solver was launched.  During both builds
the cgroup OOM counter remained 35.  The full implementation audit is
`K11_COORDINATE_PAIR_PTGE5_IMPLEMENTATION_20260724.md`.

At `2026-07-24T04:49:11Z`, the four integrated baselines, external Type-II
rank-vector seed 461, and external Type-I filter seed 481 were all live.
There was no SAT/UNSAT/UNKNOWN marker and no nonempty candidate.  Cgroup use
was about `29.06/32.00` GB with `oom_kill=35`; consequently the pair-cut
source remains build-only until a live external slot is deliberately
recycled.

The pair-filter companion was then implemented additively in

```text
scratch/k11_core_incidence/k11_forest_sat_pairfiltercuts.cpp
SHA-256 a525f21560379b65a157cc73dc475872a2290931bb5118a4f0ffe1eb7627c139.
```

An independent actual-diff audit and the static checker passed.  Warning-free
RunPod compilation produced streaming binary SHA-256
`7ae02db8...e39781`.  Build-only streams exactly matched

```text
Type I:  3,838,007 variables / 21,198,649 clauses.
Type II with PTge5 and retained PT5:
         3,859,429 variables / 21,311,994 clauses.
```

Again no raw formula or solver was started, and `oom_kill` remained 35.
Audit: `K11_COORDINATE_PAIR_FILTER_IMPLEMENTATION_20260724.md`.

External Type-II rank-vector seed 461 was then retired after roughly 3,786
solver seconds and about 2.68 million conflicts.  Its log had no
SAT/UNSAT/UNKNOWN marker and no candidate, so this has no mathematical
meaning.  The raw CNF was compressed, decompressed through its audited
SHA-256

```text
93b3ece194b2119d0a962cc7c548fa12d5dd0a2d21283a8504a5c59c02842343,
```

and only then deleted; the recoverable archive is
`k11_type2_rankvector.cnf.zst` (about 65 MiB).

The freed external slot now runs the stronger Type-II pair-filter formula.
The raw DIMACS passed a complete token audit:

```text
p cnf 0003859429 000021311994
maxvar=3859429 clauses=21311994 literals=72838065
SHA-256 1ad016707e9ce955caa2473d89a3cb2d7ad4b21d3da7878d3c74d373b3312b72.
```

Kissat seed 491 runs on CPU 20 under a 4 GiB virtual-memory cap; launch
wrapper/solver PIDs were `208079/208082`.  The watcher was extended to this
log and restarted as PID 208078, with script SHA-256
`e3069438...dd9a0f`.  At launch, cgroup use was about 28.57/32.00 GB and
`oom_kill` remained 35.  The older integrated Type-II seed 415 remains live,
so exhaustive branch coverage was never dropped.

As the four integrated processes grew, total cgroup use approached 30.1 GB.
To protect those frozen baselines from a cgroup-wide OOM, the address-space
limits of only the two external Kissat processes (Type-I filter seed 481 and
Type-II pair-filter seed 491) were tightened in place from 4 GiB to 3 GiB.
At the change their VSZ/RSS values were about `2.29/1.86` and `2.27/1.76`
GiB.  Hitting either cap will be logged as an inconclusive resource exit,
never as SAT or UNSAT.  The cgroup OOM counter remained 35.

Four low-priority one-entry SA controls (`sa504,sa508,sa509,sa510`) were
retired after roughly 43--45 minutes with no verified hit and replaced on the
same CPUs by target-preserving 3--5-edit LNS runs `lns701--lns704`.  The six
other old SA trajectories remain live as controls.  The LNS source and binary
were warning-clean compiled and smoke-tested on RunPod, including a negative
477-entry seed test.  Each wrapper uses a unique output and creates a marker
only after both C++ verifiers and an independent quadratic Python verifier
all accept a 476-entry word.  This changes no exact bound unless such a marker
appears.

At `2026-07-24T05:21:32Z`, external Type-II pair-filter seed 491 terminated
with `KISSAT_EXIT:134`.  Its log states

```text
fatal error: out-of-memory reallocating from 67108864 to 134217728 bytes
```

under the tightened address-space cap.  It had used about 1,200 solver
seconds and 650,873 conflicts.  There is no SAT, UNSAT, UNKNOWN, or candidate
marker; the cgroup OOM counter stayed 35.  This is an inconclusive resource
exit and has no mathematical meaning.  Integrated Type-II seed 415 remains
live.

The two post-B2 refinements then completed independent source audits and
RunPod build-only validation.  Type-II pair-component projection and exact
rows add respectively `77,275/439,065` and `154,990/880,110`, yielding

```text
projection: 3,936,704 variables / 21,751,059 clauses
exact:      4,014,419 variables / 22,192,104 clauses.
```

The Type-I rank-four pair row adds `152,625/890,230`, yielding

```text
3,990,632 variables / 22,088,879 clauses.
```

The corrected Type-I checker passed on RunPod after fixing an audit-only
10-bit/11-bit typo; the generator was already correct.  Streaming binary
SHA-256 values are `d1bcd864...08d693` and `39802756...e46fe`.
No raw CNF or new solver was started, and `oom_kill` remained 35.

The freed Type-II slot was then assigned to the exact pair-component formula.
Before replacement, the dead pair-filter raw file was compressed to a
recoverable `.zst` archive, streamed back through SHA-256
`1ad01670...3312b72`, and only then removed.  The new raw DIMACS passed a
complete token audit:

```text
p cnf 4014419 22192104
maxvar=4014419 clauses=22192104 literals=75793325
SHA-256 ae2bfab5e9841754cd193f45c32455d18719fb588372ecff23e892ef6c27617b.
```

Kissat seed 501 now runs on CPU 20 under a 4 GiB virtual-memory cap.  The
watcher was updated and restarted before launch.  Parsing succeeded, page
cache was evicted afterward, cgroup use was about 28.5/32.0 GB, and
`oom_kill` remained 35.  No exact bound changes without a verified terminal
result.

The coordinate-triple omission/filter package was then implemented in two
branch-specific strongest-parent clones.  The theorem and actual source diffs
passed independent audits, and the static checker passed again under RunPod
Python 3.11.  Warning-clean binary hashes are `558d6c32...d6db95` for
Type II and `77757c75...5a24fd` for Type I.  Build-only streams matched:

```text
Type II exact pair-component + triple: 4,253,504 / 23,563,749
Type I pair-rank-four + triple:         4,229,222 / 23,454,749
```

where the slash separates variables and clauses.  No raw formula or solver
was launched for the triple tier, and `oom_kill` stayed 35.

At `2026-07-24T06:14:57Z`, external Type-I pair-filter seed 481 terminated
with `KISSAT_EXIT:134` after about 5,531 solver seconds and 4.45 million
conflicts.  Its fatal line is an allocation failure under the tightened
virtual-memory cap; there is no SAT, UNSAT, UNKNOWN, or candidate marker, and
the cgroup OOM counter stayed 35.  This is an inconclusive resource exit.

The old Type-I raw file was then compressed to a recoverable `.zst` archive,
streamed back through its audited SHA-256 `e9e4fdbf...9ab115f0`, and only
then deleted.  Its freed slot now runs the strictly stronger Type-I
pair-rank-four plus triple-filter formula.  The new DIMACS token audit is:

```text
p cnf 4229222 23454749
maxvar=4229222 clauses=23454749 literals=79993676
SHA-256 4ebb66ae319c8dded33901890c83f7e6e261bcc76ae2e9141991262d43b5f972.
```

Kissat seed 511 runs on CPU 22 under a 4 GiB virtual-memory cap.  Parsing
succeeded and the watcher was updated before launch.  No exact bound changes
without a verified result.

## New wide-LNS fixed-triple closure

Four distinct one-hole snapshots from the live radius-6/7 wide-LNS search
were frozen and independently checked.  Each has length 476, covers exactly
2,046 nonzero masks, and misses only `1884`.  For each word, 24 selected
radius-three position sets have exact repair-family size four.

The audited fixed-edit encoding batched each word's 24 cases into one exact
CNF.  There were three distinct formulas because the formulas and maps for
wide1703 and wide1704 are byte-identical.  CaDiCaL returned UNSAT on all
three, and every DRAT proof was accepted by `drat-trim` with `s VERIFIED`.
This certifies all 96 named triples, covering 823,426,351,008 possible
seed/case/value tuples.  It is a local closure only and changes no bound.

The full certificate, hashes, and scope limitation are recorded in
`K11_WIDE_R3_EXACT_CLOSURE_20260724.md`; the complete proof bundle is
`scratch/k11_wide_r3_certified_20260724/`.
