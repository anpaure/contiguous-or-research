# RunPod audit and priority plan for the exact `k=14` append-241 search

## Verdict

The frozen 52-branch encoding remains a sound-and-complete reduction for the
designated 3,434-entry prefix.  The frozen source and manifest hashes still
match their independent audit:

```text
b4b7b586766906bf0727adeb587cccb98cb57b9783e9e3059498bce292fab964  scratch/k14_append241_exact.cpp
5f5881811446be60dd83e51da8adfe7577e6331b7277219161800eb95280602e  k14_append241_branch_manifest.txt
```

A model in any branch gives a 241-entry suffix and hence
`nu(14) <= 3675`.  A global fixed-prefix UNSAT statement still requires all
52 branches, and every claimed UNSAT branch requires an independently checked
proof.

No heavy computation was launched during this audit.

## Exact priority scope

The first two branches remain:

```text
branch 5:  x=1, pattern=5,  f=2, h=2
           3433:12393 -> 13423, required prefix 1030

branch 36: x=2, pattern=23, f=2, h=1
           3433:12393 -> 13423, required prefix 1030
           3434:12329 -> 15407, required cumulative prefix 3078
```

The direct solver arguments are respectively

```text
sat_seed=6,  x=1, pattern=5,  f=2
sat_seed=37, x=2, pattern=23, f=2
```

Each source formula has 1,012,539 variables.  The source clause counts are
2,632,175 and 2,632,414.  A representative unit-simplified DIMACS is 47 MB
and has 2,617,305 clauses.  The integrated API solve does not need to store a
DIMACS file.

## Phase-only improvement

The phase seed is not constrained by the CNF, so changing it preserves the
exact decision problem.

The old first-241 seed has 259 exact target witnesses, but its shortest phase
for `13423` uses old start 3434, whereas both priority branches fix old start
3433.  The following branch-specific seeds are better aligned.

1. Branch 5: take the first 241 entries of `k14_append_242.txt` and replace
   its first entry `1095` by `1031`.  It still has 259/260 exact target phases,
   and its preferred crossing is now exactly

   ```text
   12393 OR 1031 = 13423.
   ```

2. Branch 36: delete one-based entry 205, the literal `15407`, from the full
   242-entry seed; then replace the first two entries by `1031,7182`.  It has
   257/260 exact target phases and makes both fixed crossings preferred:

   ```text
   12393 OR 1031 = 13423,
   12329 OR (1031 OR 7182) = 15407.
   ```

The only inexact target phases in the second seed are `8014,8015,16206`.
This is a heuristic tradeoff, not a logical restriction.  The priority
launcher constructs these seeds deterministically and logs their hashes.

There are 208 one-hole deletions of the certified 242-entry suffix.  They are
a cheap later phase portfolio because they change no clause.  Formula
partitioning should not precede this phase diversification.

## Operational defects in the generic launcher

The generic 52-branch launcher is adequate as an inventory driver, but not as
the final priority/proof harness:

* it labels exit 137 as `TIMEOUT`, although 137 can be OOM or another SIGKILL;
* it promotes solver exit zero to `SAT` without two external verifiers;
* it has no artifact SHA binding or memory preflight;
* proof tracing on a timed run can leave a large incomplete proof;
* it cannot select only branches 5 and 36.

`launch_k14_append241_priority_runpod.sh` addresses these points.  It refuses
the frozen inputs on a SHA mismatch, constructs the branch-specific phase
seed, enforces a default 4 GiB per-process virtual-memory cap, requires at
least 5 GiB host/cgroup headroom, distinguishes exit 137, and independently
checks any model with both `verify_or_array` and `verify_or_suffix`.

The launcher uses `/usr/bin/time -v` when that optional executable is present
and otherwise runs the same capped command without resource-formatting output.
This fallback is needed on the staged 377 GiB RunPod image, which has the Bash
`time` keyword but no `/usr/bin/time` executable.  It does not change the
decision problem or any verification step.

## Measured RunPod state at audit time

The 32 GB Rose pod had approximately 30.1 GB in use and only 1.2 GB disk free.
It was not safe to add even one exact append process.  Finishing the live
radius-4 proof checker would free only about 0.5 GB, still below the preflight.

The already staged RunPod at `213.173.111.107:48809` had the exact audited
binary and inputs, 296 GiB available RAM, and 1.4 GB disk free.  Its frozen
binary hash was

```text
236f3e1597aa9d7590e974915b2cecb73749eded640cae9529d82a173b585231.
```

That pod is suitable for no-proof integrated solves once two CPU slots are
explicitly assigned.  It is not suitable for proof tracing on the overlay.
The missing independent suffix verifier must be staged there before a launch.

## Recommended launch order

1. Stage `scratch/verify_or_suffix` and the priority launcher on the RunPod;
   recheck all frozen hashes.
2. Run branch 5 and branch 36 without proof tracing, each under a 4 GiB
   virtual-memory cap and `/usr/bin/time -v`.  Six hours per phase seed is a
   reasonable first quantum.  Two simultaneous runs require at least 10 GiB
   measured headroom; otherwise run one at a time.
3. If either returns SAT, require exactly 241 suffix entries and 3,675 total
   entries, then retain the two independent verification logs and SHA-256 of
   both suffix and full word.
4. If they time out, repeat these same two logical branches with several of
   the 208 one-hole deletion seeds and different CaDiCaL random seeds.  This
   is cheaper than adding clauses or producing a DIMACS portfolio.
5. Only after phase portfolios stall, add an audited exhaustive partition of
   one target's endpoint.  For example, the unique `end[p]` flag for `13757`
   can be partitioned into disjoint endpoint ranges.  The range clauses must
   cover all positions `0..240`; otherwise the split is not complete.  A
   first two-way split by append-only versus the sole compatible crossing old
   start (3434) is also exact.
6. An UNSAT proof rerun must use storage outside the 20 GB overlay, with at
   least 50 GB free as a conservative preflight.  Generate the matching
   DIMACS and binary DRAT for the same branch/seed run, check it independently
   with `drat-trim`, and promote only an explicit verifier success.  A timeout,
   exit 20 without a checked trace, or an incomplete proof has no mathematical
   force.

The final launcher SHA-256 after adding the optional-`time` fallback is

```text
0666ed768745171b0433c34f7568cf56a9520396a4768ec9e163b7870868020f
```

## Presolve and partition conclusion

CaDiCaL already preprocesses the in-memory formula, and the DIMACS writer's
unit simplification saves only about 15,000 clauses.  External DIMACS solving
also discards the unusually strong 259/260 phase information.  There is no
audited cheaper presolve currently worth replacing the integrated solver.

Endpoint sharding is exact and available, but it multiplies proof obligations
and total learned-state startup.  The branch-aware phase seeds and random-seed
portfolio are therefore the correct first intervention.  No CNF soundness or
completeness issue was found.
