# Exact `k=14` append-241 fallback launch plan

## Scope and current snapshot

This is a launch plan, not a SAT or UNSAT result.  No job was launched or
interrupted while preparing it.

At `2026-07-24T11:42:39Z`, the two six-hour no-proof searches on the Purple
RunPod were still healthy:

| logical branch | PID | core | elapsed | CPU time | RSS | state |
|---:|---:|---:|---:|---:|---:|---|
| 5 (`x=1,p=5,f=2`) | 191197 | 35 | 4:10:08 | 4:10:06 | 1.69 GiB | running |
| 36 (`x=2,p=23,f=2`) | 191200 | 36 | 4:10:08 | 4:10:07 | 0.97 GiB | running |

Neither output directory contained an append candidate or terminal marker.
The overlay had 1.1 GiB free.  These processes should run to their existing
bounded timeout at approximately `2026-07-24T13:32Z`.

## Why the same two logical branches remain first

An exact enumeration of all 242 single deletions of `k14_append_242.txt`
gave 208 one-hole words, 31 two-hole words, and 3 three-hole words.  The 208
one-hole words were then scored by the exact phase-selection rule in
`scratch/k14_append241_exact.cpp`, including append-only and cross-seam
witnesses.

For branch 5, after its required first-entry change to `1031`, all 208
one-hole deletions retain 259/260 exact target phases and prefer the fixed
`3433:12393 -> 13423` crossing.  However, deleting one-based suffix entry
242 (the current phase seed) is the only one whose preferred hard-target
endpoints also have the branch's `f=2` profile.  The other 207 score as
`f=3`.  Thus the current branch-5 phase is the unique best simple deletion
variant.

For branch 36, after setting the first two entries to `1031,7182`, deleting
one-based entry 205 (the current phase seed) is the only one of the 208 that
prefers both fixed crossings.  It retains 257/260 exact target phases.  Every
other simple one-hole deletion retains only 256/260 and prefers an append-only
witness, rather than the forced second crossing, for `15407`.  The current
branch-36 seed is therefore also the unique best simple deletion variant.

Branches 9 and 40 have already each consumed a one-hour no-proof quantum and
timed out.  Their old phase files did not agree with their forced crossing
patterns.  They are profile-coverage samples, not better construction-led
successors to branches 5 and 36.

## Four launch slots

Run slots 1 and 2 only if the current six-hour jobs time out.  Run slots 3 and
4 only if the corresponding first retry also times out.  A verified SAT in
any slot cancels every later slot.

| priority | branch parameters | CaDiCaL seed | phase SHA-256 | initial quantum | leverage |
|---:|---|---:|---|---:|---|
| 1 | branch 5: `x=1,p=5,f=2` | 106 | `ef5abe185f628a3bbbbfc70c90f8f74d31281226910c2f4525b21f519201c6a9` | 7,200 s | best-aligned 259/260 phase; fresh search trajectory |
| 2 | branch 36: `x=2,p=23,f=2` | 137 | `692f3c15be148eff0b03554c736b2b601a683861fa8bfc55acd18d9264dceb3a` | 7,200 s | only simple phase preferring both successful-seam crossings |
| 3 | branch 5: `x=1,p=5,f=2` | 206 | same branch-5 SHA | 7,200 s | second independent trajectory on the strongest phase |
| 4 | branch 36: `x=2,p=23,f=2` | 237 | same branch-36 SHA | 7,200 s | second independent trajectory on the unique two-crossing phase |

Changing `sat_seed` changes only CaDiCaL's search order.  It adds no clause
and does not alter the logical branch.  A timeout has no mathematical
meaning, so using a fresh solver seed is preferable to moving immediately to
an unaligned logical branch.

## Separate seed-override launcher

The frozen priority launcher was not edited.  Its audited seed-override
companion is:

```text
launch_k14_append241_seed_override_runpod.sh
```

Local SHA-256:

```text
573ecc633df90b173be25608854fcc035f5ab3437c24455942379865eb9b8e14
```

The launcher fixes and checks the exact parameters of branches 5 and 36,
binds the solver, prefix, missing-family, 242-seed, both verifiers, and generated phase hashes,
refuses artifact overwrite, checks that the requested CPU is allowed and
idle, requires at least 5 GiB memory headroom and 1 GiB output-disk headroom,
sets a 4 GiB per-process virtual-memory ceiling, classifies exits 124 and 137
separately, and subjects every model to both independent verifiers.  It also
records hashes for both verifier binaries and for every verified candidate.

After staging and hashing the new launcher, representative commands for slots
1 and 2 are:

```bash
unset K14_APPEND241_PROOF_DIR

/root/launch_k14_append241_seed_override_runpod.sh \
  /root/k14_append241_exact \
  /root/k14_pinnable_factor_missing260.txt \
  /root/k14_missing_260.txt \
  /root/k14_append_242.txt \
  /root/verify_or_array \
  /root/k14_append242_audit/verify_or_suffix \
  /root/k14_append241_seed_portfolio_20260724 \
  7200 35 5 106

/root/launch_k14_append241_seed_override_runpod.sh \
  /root/k14_append241_exact \
  /root/k14_pinnable_factor_missing260.txt \
  /root/k14_missing_260.txt \
  /root/k14_append_242.txt \
  /root/verify_or_array \
  /root/k14_append242_audit/verify_or_suffix \
  /root/k14_append241_seed_portfolio_20260724 \
  7200 36 36 137
```

For slots 3 and 4, change only `106` to `206` and `137` to `237`.  Cores 35
and 36 are examples, not reservations: use them only after the old PIDs have
exited and the launcher's idle-core preflight passes.

## Promotion and safety gates

1. Do not auto-queue a successor.  First inspect the predecessor's status and
   candidate files.
2. Before every launch, require an idle allowed CPU, at least 1 GiB overlay
   space (preferably restore the earlier 1.4 GiB margin), and measured memory
   headroom.  Do not delete unrelated artifacts to manufacture space.
3. These four slots are no-proof discovery runs.  Keep
   `K14_APPEND241_PROOF_DIR` unset on the 20 GiB overlay.
4. Solver exit 20 remains `UNSAT_UNCHECKED`; it proves nothing.  A proof rerun
   requires the matching formula, external storage with at least 50 GiB free,
   and an independent successful proof check.
5. A candidate must contain exactly 241 suffix entries and 3,675 total
   entries, all in `1..16383`, pass both `verify_or_array 14` and
   `verify_or_suffix 14`, and retain the suffix/full-word hashes and logs.
6. Only after all four seed-diversified slots time out should endpoint sharding
   or a newly constructed aligned phase for another logical branch outrank
   this portfolio.
