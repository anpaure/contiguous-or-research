# Live audit: second `k=14` append-241 priority run

Snapshot time: `2026-07-24T09:47Z`.

## 1. Exact live scope

The Purple RunPod at `213.173.111.107:48809` is running two no-proof,
integrated CaDiCaL searches for the designated 3,434-entry prefix.

| branch | solver PID | core | elapsed | formula | phase inventory |
|---|---:|---:|---:|---|---|
| 5 | 191197 | 35 | 2:15 | `x=1,p=5,f=2`, 1,012,539 variables, 2,632,175 source clauses | `259/260` exact, crossing `3433:13423` |
| 36 | 191200 | 36 | 2:15 | `x=2,p=23,f=2`, 1,012,539 variables, 2,632,414 source clauses | `257/260` exact, crossings `3433:13423`, `3434:15407` |

The external wrappers are

```text
timeout --kill-after=30s 21600s ...
```

so the runs terminate at approximately `2026-07-24T13:32Z` if neither
solves earlier.  Each process is under a 4 GiB virtual-memory limit.

The phase files are heuristic only.  They add no clause and do not restrict
the decision problems.  Their hashes are

```text
branch 5:  ef5abe185f628a3bbbbfc70c90f8f74d31281226910c2f4525b21f519201c6a9
branch 36: 692f3c15be148eff0b03554c736b2b601a683861fa8bfc55acd18d9264dceb3a
```

The solver binary is the frozen audited binary

```text
236f3e1597aa9d7590e974915b2cecb73749eded640cae9529d82a173b585231.
```

## 2. Health verdict

Both runs are **meaningful and live**, not blocked or stuck.

* Each process reports approximately `99.9%` CPU.
* Over a two-second sample, each user-time counter advanced by approximately
  two seconds.
* Both states are `R` (running), with no I/O wait.
* RSS is approximately 0.94--1.05 GiB per process, well below the 4 GiB cap.
* Neither process incurred a new major page fault during the sample.
* The only output is the expected initial formula inventory.  The integrated
  API build runs CaDiCaL quietly, so the lack of periodic log lines is not a
  stall indicator.
* No append file, `SAT`, `UNSAT`, or terminal marker exists yet.

The process accounting is consistent with two uninterrupted CPU-bound SAT
searches.  There is no operational reason to interrupt them before their
bounded six-hour quantum ends.

## 3. Mathematical meaning of every possible exit

* `SAT` produces exactly 241 appended entries.  Concatenation with the fixed
  prefix has length 3,675 and would prove

  \[
                           \nu(14)\le3675.
  \]

* `UNSAT` from these runs is deliberately labelled `UNSAT_UNCHECKED`, because
  proof tracing is disabled.  It has no certified mathematical consequence.
  Even a checked proof would close only that one branch.  A fixed-prefix
  UNSAT result requires all 52 manifest branches.
* `TIMEOUT`, exit 137, or any other non-model exit has no mathematical
  consequence.

The launcher already performs two checks on a model:

1. `/root/verify_or_array 14` on the 3,675-entry concatenation;
2. `/root/k14_append242_audit/verify_or_suffix 14` on the same file.

For a candidate promotion, run an additional independent pass with

```text
/root/k14_append242_audit/verify_or_array 14 < candidate.full.txt
/root/k14_append242_audit/verify_or_suffix 14 candidate.full.txt
```

and retain token counts, value-range checks, both verifier logs, and
SHA-256 hashes of the suffix and full word.  The solver itself also
re-enumerates all interval ORs before writing a model, giving a third check.

## 4. Resource safety

At the snapshot:

```text
allowed CPUs: 0,2,4-6,8,10-12,14-16,19-20,22-24,26,28-30,
              32,34-36,38-40,43-44,46-47
load average: 32.88, 33.56, 34.36
available RAM: approximately 294 GiB
overlay free: approximately 914 MiB (96% used)
```

Every allowed compute core is occupied by a CPU-bound task.  The two current
`k=14` jobs own cores 35 and 36 and do not compete with another heavy process
on those cores.  RAM is ample, but overlay storage has only about 402 MiB
above the launcher's current 512 MiB hard minimum.

Therefore:

* do not launch a third process;
* do not enable proof tracing on this overlay;
* do not auto-queue a successor merely because a current process exits;
* before any retry, recheck both core idleness and disk space;
* require at least 1 GiB free for another no-proof integrated run, preferably
  restore the launch-time 1.4 GiB margin;
* require external storage with at least 50 GiB free before any DRAT rerun.

No unrelated files should be removed merely to make a retry fit.

## 5. Next bounded priority portfolio

The next logical priority remains branches 5 and 36, not a new unranked
formula family.  Earlier one-hour runs of branches 5, 36, 9, and 40 all
timed out; branch 9 and branch 40 were coverage samples, whereas branches 5
and 36 carry the successful `13423` seam and remain the construction-led
choices.

If the current six-hour runs time out, the next bounded portfolio should be:

1. one further no-proof branch-5 run with the same `259/260` aligned phase
   file and a fresh CaDiCaL seed (proposed seed `106`);
2. one further no-proof branch-36 run with the same two-crossing aligned
   phase file and a fresh CaDiCaL seed (proposed seed `137`);
3. cap each retry at two hours initially, one process per newly idle core;
4. launch neither until the post-exit CPU and disk preflight passes.

The proposed seeds change search order only.  They do not define new logical
branches.  The frozen priority launcher currently hardcodes seeds `6` and
`37`; therefore seeds `106` and `137` require a separately audited seed-
override wrapper (or a direct invocation followed by the full verification
protocol above).  Do not silently edit the frozen launcher in place.  If
these retries also time out, rank the 208 one-deletion phase
seeds by exact-target phase count and crossing agreement before spending
more CPU.  Do not pick an arbitrary deletion and do not endpoint-shard before
that phase portfolio has been evaluated.

No retry or successor was launched during this audit.
