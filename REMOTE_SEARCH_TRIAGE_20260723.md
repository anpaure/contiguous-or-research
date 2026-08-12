# Remote exact-search triage — 2026-07-23 (Asia/Almaty)

## Scope and evidentiary rules

This record audits the live exact searches on the two supplied RunPods:

- **purple**: `root@213.173.111.107:48809`;
- **rose**: `root@157.157.221.29:27423`.

The following labels are used strictly:

- **live** means the solver process exists and is consuming CPU;
- **timeout/interrupted** means no mathematical conclusion;
- **SAT** is promoted only after the extracted array passes both independent
  interval-OR verifiers;
- **UNSAT** is promoted only after an independently checked proof against the
  exact archived CNF.

No solver silence, exit without a proof, partial proof trace, or missing
candidate file is interpreted as SAT or UNSAT.

All timestamps reported by the pods below are UTC; the filename date is local
Asia/Almaty time.

## 1. Purple host snapshot

At `2026-07-22T19:38:00Z`, the pod exposed 32 logical CPUs

```text
0,2,4-6,8,10-12,14-16,19-20,22-24,26,28-30,32,34-36,38-40,43-44,46-47
```

and all 32 were occupied by existing searches.  Therefore no additional job
was launched on an oversubscribed core.

### Exact unrestricted/minimal-component `k=11` searches

| Formula | solver PID | wrapper PID | requested core | elapsed at snapshot | output | status |
|---|---:|---:|---:|---:|---|---|
| generic branch 0, seed 61 | 164667 | 164664 | 36 | 1:51:41 | `/root/k11_forest_exact/candidate_branch_61.txt` | live; no candidate/terminal marker |
| generic branch 1, seed 62 | 164668 | 164665 | 38 | 1:51:41 | `/root/k11_forest_exact/candidate_branch_62.txt` | live; no candidate/terminal marker |
| `e0c1` + density, seed 81 | 170076 | 170072 | 44 | 0:17:36 | `/root/k11_forest_exact/candidate_density_e0_81.txt` | live; no candidate/terminal marker |
| `e1c2` + density, seed 82 | 170078 | 170073 | 47 | 0:17:36 | `/root/k11_forest_exact/candidate_density_e1_82.txt` | live; no candidate/terminal marker |
| `e0c1` + density + containment caps, seed 91 | 170487 | 170484 | 40 | 0:08:38 | `/root/k11_forest_exact/candidate_caps_density_e0_91.txt` | live; no candidate/terminal marker |
| `e1c2` + density + containment caps, seed 92 | 170488 | 170485 | 43 | 0:08:38 | `/root/k11_forest_exact/candidate_caps_density_e1_92.txt` | live; no candidate/terminal marker |

The density-free minimal-component seeds 71 and 72 were no longer running.
Their logs contain only the construction inventories and no `SAT`, `UNSAT`,
`EXIT`, or candidate artifact.  They are therefore recorded as
**interrupted/incomplete**, not as results.  Seeds 81/82 and 91/92 are not
restarts of an established terminal result; they are stronger parallel exact
searches.

### Replacement of the superseded density-only runs

At `2026-07-22T20:08:31Z`, after 48 minutes 8 seconds, seeds 81 and 82
still had no candidate and no terminal marker.  A subsequently audited
six-set density inequality strengthens the second PB threshold from 10,626
to 12,936, so exactly these two density-only processes were retired.  Seeds
91/92, the generic branches, and every `k=14` process were left untouched.

The pre/post-termination logs, process command lines, old binary hash, and
candidate-absence record are archived at

```text
/root/k11_forest_exact/retired_density_81_82_20260723/
```

The new source was copied as
`/root/k11_forest_exact/k11_forest_sat_strong_pb.cpp` and compiled remotely
with

```text
taskset -c 44 g++ -O3 -std=c++2a -I/root/cadical/src \
  k11_forest_sat_strong_pb.cpp /root/cadical/build/libcadical.a \
  -lpthread -o k11_forest_sat_strong_pb
```

Source SHA-256 is
`c9b27476bfe62c1b0c75cda5f0dd713470a66db10fb2d697fd6cf6698b407049`;
remote binary SHA-256 is
`67e79659ba7d407fdf953d00522e54079773e58c7c6fc75c490e3e1deaed9ee5`.

Before solving, both formulas were constructed in `K11_FOREST_BUILD_ONLY=1`
mode under the complete production environment (minimal component, density,
and containment caps).  Both returned zero and reproduced the expected
topological inventories:

| mode | variables | clauses | build log SHA-256 |
|---|---:|---:|---|
| `e0c1` | 2,983,733 | 15,159,630 | `c51cb6b940c6c6db47fbbc4d7c6815a029b373d2de5a1f185d652d960f12a8e1` |
| `e1c2` | 2,983,974 | 15,199,352 | `589333e4afa049440b0541b706d3bf1f77518712b1acd1f02e004a76e8c1d8bb` |

The constant change does not alter the number of ripple/comparator clauses;
it changes their literals.  New production searches were launched as:

| mode | seed | solver PID | wrapper PID | core | log | candidate |
|---|---:|---:|---:|---:|---|---|
| `e0c1` + density(12,936) + caps | 101 | 171730 | 171726 | 44 | `strong_pb_e0_101.log` | `candidate_strong_pb_e0_101.txt` |
| `e1c2` + density(12,936) + caps | 102 | 171729 | 171727 | 47 | `strong_pb_e1_102.log` | `candidate_strong_pb_e1_102.txt` |

At `20:10:24Z` both were live at approximately 99% CPU with no terminal
marker or candidate.

The exact shared launch environment for seeds 101/102 is

```text
K11_FOREST_ADJACENT_SHADOWS=1
K11_FOREST_RANK3_SHADOWS=1
K11_FOREST_BAND_CUTS=1
K11_FOREST_JOINT_BAND_CUTS=1
K11_FOREST_ENDPOINT_ALIGNMENT_CUTS=1
K11_FOREST_CANONICAL_RANK6_ENTRY=1
K11_FOREST_SINGLETON_POOL_CUT=1
K11_FOREST_RANK6_BOUNDARY_ENTRY=1
K11_FOREST_LOCAL_DENSITY_PB=1
K11_FOREST_CONTAINMENT_CAPS=1
```

Seed 101 additionally sets
`K11_FOREST_RANK6_BRANCH=0 K11_FOREST_MIN_COMPONENT=e0c1` and executes

```text
taskset -c 44 nice -n 10 ./k11_forest_sat_strong_pb \
  k11_upper549_natural_array.txt candidate_strong_pb_e0_101.txt 101
```

Seed 102 sets
`K11_FOREST_RANK6_BRANCH=1 K11_FOREST_MIN_COMPONENT=e1c2` and executes the
same binary on core 47 with output `candidate_strong_pb_e1_102.txt` and seed
102.

### Exact fixed-prefix `k=14`, 241-entry append searches

| exact branch | solver PID | timeout PID | core | elapsed at snapshot | output stem | status |
|---|---:|---:|---:|---:|---|---|
| branch 36: `x=2,p=23,f=2,h=1` | 169302 | 169301 | 26 | 0:20:40 | `/root/k14_append241_x2p23f2` | live; no terminal marker |
| branch 5: `x=1,p=5,f=2,h=2` | 170134 | 170132 | 5 | 0:16:18 | `/root/k14_append241_x1p5f2` | live; no terminal marker |

Both have a 3,600-second external timeout.  Their logs contain only the exact
formula inventories (`1,012,539` variables and respectively `2,632,414` and
`2,632,175` clauses).  Neither had written an append candidate.

## 2. Rose host snapshot and disk intervention

At `2026-07-22T19:38:00Z`, the three hard delete-one/append-twelve formulas
were running under proof-producing Kissat:

| skip | solver PID | wrapper PID | core | seed | CNF | initial proof status |
|---:|---:|---:|---:|---:|---|---|
| 7 | 112326 | 112318 | 16 | 5007 | `/root/append_delete_runs/skip_7.cnf` | live, approximately 3.0 GB |
| 89 | 112325 | 112319 | 18 | 5089 | `/root/append_delete_runs/skip_89.cnf` | live, approximately 2.9 GB |
| 196 | 112324 | 112320 | 20 | 5196 | `/root/append_delete_runs/skip_196.cnf` | live, approximately 2.8 GB |

No log contained `SATISFIABLE`, `UNSATISFIABLE`, or a terminal exit marker.

The root filesystem then had only 158–190 MB free on a 20 GB overlay while
all three traces were growing.  Continuing unchanged would have caused an
`ENOSPC` failure and made all three runs worthless.  At approximately
`19:39Z` the following conservative intervention was made:

1. keep skip 7 running with its proof trace;
2. terminate only the skip 89 and skip 196 proof-producing processes;
3. remove their **incomplete and therefore uncheckable** proof traces;
4. preserve their CNFs and logs;
5. restart skip 89 and skip 196 without proof generation, on the same cores,
   with fresh seeds 6089 and 6196.

The resulting free space was 7.0 GB (66% used).  The replacement processes
were:

| skip | solver PID | wrapper PID | core | mode | status |
|---:|---:|---:|---:|---|---|
| 89 | 112745 | 112740 | 18 | no proof, seed 6089 | live |
| 196 | 112746 | 112741 | 20 | no proof, seed 6196 | live |

If either no-proof run returns UNSAT, that remains `UNSAT_UNCHECKED` and must
be rerun proof-producing, one branch at a time.  If it returns SAT, the first
132 DIMACS variables encode the twelve appended 11-bit masks and can be
reconstructed immediately before independent verification.

For that terminal path, a dedicated decoder was prepared at
`scratch/decode_append_completion_dimacs.cpp` and compiled on rose as
`/root/decode_append_completion_dimacs`.  It refuses a model lacking a full
assignment to the first 132 variables, reconstructs the delete-one plus
twelve-entry word, and performs both an exhaustive interval enumeration and
the distinct-suffix-OR recurrence before writing any candidate.  Source
SHA-256 is
`1eb672bc0a40c593b5423a7bbb53ce084a72e4d4f38a769780abad8aefce007c`;
remote binary SHA-256 is
`8ab07b880b4d777252bfb4ebd32e67964f7a69faf1afb97cf992b04554f25935`.

## 3. Scheduling decision

At the snapshot there was no unoccupied purple CPU.  Rose had no usable disk
margin for another proof-producing task, and its one nominally unused CPU did
not justify importing an additional million-variable `k=14` formula while
the disk emergency was being stabilized.  Therefore no job was
oversubscribed and no unrelated running search was killed.

The next exact `k=14` representatives recommended when branches 5 and 36
time out are:

1. branch 40, `x=3,p=0,f=1,h=1`, to sample the maximal-crossing/minimal-free
   profile;
2. branch 9, `x=2,p=0,f=1,h=2`, to sample the other `f=1` family.

This complements the already-running `x=1,f=2` and `x=2,f=2` branches.  It
is a coverage decision, not a claim that these branches are probabilistically
more likely to be SAT.

These two follow-ups were safely queued without oversubscription.  Queue PID
170815 waits for timeout PID 169301 and then starts branch 40 on core 26;
queue PID 170816 waits for timeout PID 170132 and then starts branch 9 on core
5.  Each queue first checks whether the preceding branch wrote a nonempty SAT
candidate and aborts the follow-up if so.  The queue logs are

```text
/root/k14_append241_queue_branch40.log
/root/k14_append241_queue_branch9.log
```

## 4. Terminal-results ledger

This section is updated only when a process terminates.

| search | terminal state | certified consequence | artifacts |
|---|---|---|---|
| all searches above at initial snapshot | none | none | none |

### Subsequent terminal events

| search | terminal state | certified consequence | artifacts |
|---|---|---|---|
| rose skip 7, seed 5007 | `TIMEOUT` after 3,599.77 CPU seconds; wrapper exit 124 | none | CNF SHA-256 `7bee63cc6bd6576e1cbc0fd3b6c1e6c1ad5f14342eb9c3d95c4bb5c07602c56b`; local timeout log `scratch/remote_search_triage_20260723/skip_7.kissat.timeout.log`, SHA-256 `fc404ee04c7c59cf578cfe32dba835218437e1db608e1f1f6c753b1b565a5c33` |
| purple `k=14` branch 36, `x=2,p=23,f=2,h=1` | `TIMEOUT` at the 3,600-second external limit; no candidate | none | `/root/k14_append241_x2p23f2.log` |
| purple `k=14` branch 5, `x=1,p=5,f=2,h=2` | `TIMEOUT` at the 3,600-second external limit; no candidate | none | `/root/k14_append241_x1p5f2.log` |
| rose skip 89, no-proof seed 6089 | `TIMEOUT`, 3,599.87 CPU seconds, exit 124 | none | local log `scratch/remote_search_triage_20260723/skip_89.noproof.timeout.log`, SHA-256 `7d073e46d1cbd59d959c1b495198c273980db509f90e7d4f11b1a19232c5d162` |
| rose skip 196, no-proof seed 6196 | `TIMEOUT`, 3,599.91 CPU seconds, exit 124 | none | local log `scratch/remote_search_triage_20260723/skip_196.noproof.timeout.log`, SHA-256 `b38c6f9be14c66ed1ae2778a38af6d83065655447b643a8c3de87e23fea2a75b` |

The skip-7 run ended with SIGTERM from the timeout wrapper, not an UNSAT
line.  Its 6,375,342,080-byte trace was incomplete and could not be checked;
after recording its exact size and preserving the log, it was removed.  This
restored 10 GB free space on rose.  It is deliberately not listed as a proof.
The freed core 16 was immediately reused for a no-proof exact retry with seed
7007 (wrapper PID 114436, timeout PID 114438, solver PID 114439, log
`/root/append_delete_runs/skip_7.noproof.log`).  An UNSAT line from that retry
would still require a later proof-producing rerun before promotion.

The queued branch 40 started at `2026-07-22T20:17:25Z` on core 26 (timeout
PID 171964, solver PID 171965).  Its independently printed inventory is
1,012,539 variables and 2,632,632 clauses.  Branch 36's timeout is only a
portfolio observation; branch 36 remains unresolved.

The queued branch 9 started at `2026-07-22T20:21:55Z` on core 5 (timeout PID
172086, solver PID 172087).  Its independently printed inventory is 1,012,539
variables and 2,632,394 clauses.  Branch 5's timeout likewise leaves branch 5
unresolved.

The skip-89 and skip-196 exits contain neither SAT nor UNSAT, so the three
delete-one candidates 7, 89, and 196 all remain unresolved.  No replacement
was launched after these two timeouts: per the updated scheduling instruction,
newly released capacity is reserved for the exact `k=11`, `q=19`
mixed-delay suffix continuation rather than consumed by an unrelated retry.

## 5. Final snapshot for this triage pass

At `2026-07-22T20:41:51Z`, every still-listed process below was live and
CPU-bound, with no candidate and no SAT/UNSAT marker:

| search | solver PID | elapsed |
|---|---:|---:|
| generic `k=11` branch 0, seed 61 | 164667 | 2:55:33 |
| generic `k=11` branch 1, seed 62 | 164668 | 2:55:33 |
| old-threshold caps `e0c1`, seed 91 | 170487 | 1:12:30 |
| old-threshold caps `e1c2`, seed 92 | 170488 | 1:12:30 |
| corrected-threshold caps `e0c1`, seed 101 | 171730 | 0:31:58 |
| corrected-threshold caps `e1c2`, seed 102 | 171729 | 0:31:58 |
| `k=14` append branch 40 | 171965 | 0:24:26 |
| `k=14` append branch 9 | 172087 | 0:19:56 |
| skip 7 no-proof retry, seed 7007 | 114439 | 0:22:43 |

Rose had approximately 10 GB free after removal of the incomplete trace.
No exact bound changed during this pass: every terminal solver event was a
timeout or an intentional retirement of a superseded formula.
