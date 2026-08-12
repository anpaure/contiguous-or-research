# Target-preserving large-neighborhood search for `k=11`, length 476

## Purpose and scope

This is a constructive heuristic.  A found word changes the certified upper
bound only after independent exact verification.  A timeout has no lower-bound
meaning.

The existing one-entry simulated annealer repeatedly reaches a word covering
2,046 of the 2,047 nonzero masks and then stalls.  That behavior is structural:

- the canonical, relocated, and unrestricted basins have audited no-go results
  for zero, one, or two arbitrary further value replacements;
- the recurrent holes `493`, `607`, and `1763` all have rank seven;
- exact RunPod interval enumeration gives the following brittleness ledger:

```text
seed                                      singleton  doubleton  capped32
canonical                                      1530        238      4303
one-relocation                                 1529        238      4309
plateau / unrestricted                         1508        256      4307
```

Thus most represented masks have only one interval witness.  An unguided edit
usually exchanges the current hole for one or more new holes.  In the old
annealer a one-hole increase alone costs at least 200,000 energy units against
a maximum temperature of 80,000, before the rank and distance charges.  A
coordinated three-edit escape consequently has negligible probability of being
assembled from accepted single edits.

## New move

The source is

```text
scratch/search_unrestricted_word_target_lns.cpp
```

For a selected missing mask `t`, one large-neighborhood round:

1. chooses an interval and includes as a **creator** every position in it whose
   old value has a bit outside `t`;
2. changes three to five positions simultaneously, with the remaining
   **repair** edits deliberately placed outside the protected interval;
3. restricts creator values to nonzero submasks of `t`, while repair values may
   be arbitrary nonzero masks;
4. maintains the invariant that the creator values together with the unchanged
   part of the selected interval have OR exactly `t`;
5. optimizes the changed values by a small simulated anneal while that exact
   witness is frozen.

This creator/repair split directly covers the unclosed radius-three cases in
which the final hole witness meets only one or two changed positions; an
all-inside variant is retained for other basins and radii four and five.
Candidate positions are first biased away from exact unique witnesses.  The
best 128 approximate candidates are then ranked by an exact quantity: the
number of masks having no witness in any untouched segment after the selected
positions are removed.  Eighteen candidates receive the inner assignment
search.  One-hole states are allowed to move around the plateau even when their
secondary score is worse; excursions to two or three holes are admitted
sparingly.

The coverage evaluator uses the standard at-most-`k+1` suffix-OR groups, but it
also stores each group's number of starting positions.  It therefore computes
the **exact number of interval witnesses**, not merely the number of right
endpoints.  A built-in deterministic self-test compares this compressed count
against quadratic enumeration on 96 random words before search starts.

The independent audit script is

```text
scratch/audit_target_lns_word.py
```

It uses direct quadratic interval enumeration and shares no coverage code with
the searcher.

An independent static source audit found the search/evaluator logic sound but
identified two launch-safety issues in the first version: it did not reject a
seed of the wrong length, and atomic output did not explicitly test stream
state after flushing and closing.  The final source now requires exactly 476
seed entries and throws on either write or close failure.  A 477-entry
negative smoke test exits 2 without creating an output file.

## RunPod build and smoke audit

The source was copied to Rose and compiled there, not locally:

```bash
g++ -std=c++2a -O3 -DNDEBUG -Wall -Wextra -Wpedantic -pthread \
  search_unrestricted_word_target_lns.cpp \
  -o search_unrestricted_word_target_lns
```

The final creator/repair build was warning-clean.  A zero-second invocation
passed the built-in evaluator audit.  (The preceding all-inside prototype also
completed two full target-LNS rounds under a one-second deadline, but that run
is not evidence about search quality.)  The independent Python audit reproduced

```text
length=476 covered=2046/2047 missing=[1763]
singleton=1508 doubleton=256 thin_le4=1906 capped32=4307
```

Current hashes after those safety fixes:

```text
be9ab52dbb365ffdaab09f1db9a97d10e1f795a081d9d1683925e123554918c7  scratch/search_unrestricted_word_target_lns.cpp
09cb8fb1cdb9c8819c8f46844444262091d12f540d37d6fd449e3fb9fb654bcf  RunPod binary
27e4fd5b44dd3d72536b602b70841f8ca35b34212493be4f3f3a333eeaf0fb29  scratch/audit_target_lns_word.py
```

## Launch recommendation

Do not add memory pressure to the currently saturated exact portfolio.  When
four of the old one-entry SA slots finish, use those freed allowed CPUs for
four independent one-thread runs, one from each latest verified one-hole
basin.  A six-hour first batch is appropriate:

```bash
timeout 21900s taskset -c CPU nice -n 19 \
  ./search_unrestricted_word_target_lns SEED OUT 21600 1 RNG \
  >OUT.stdout 2>OUT.log
```

The program's live memory is tiny; a 256 MiB per-process cap is ample.  Use
independent RNG seeds, for example `701` through `704`.  The wrapper should
create a success marker only after all three checks pass:

```bash
/root/verify_or_array 11 <OUT
/root/verify_or_suffix 11 OUT
python3 audit_target_lns_word.py OUT --bits 11 --length 476 --require-universal
```

The larger timeout grace is intentional: the program checks its soft deadline
between complete LNS rounds, not inside every candidate loop.  Every process
must use a unique output path because atomic writes use `OUT.tmp`.

If this batch again accumulates many distinct one-hole states without a hit,
the next escalation should increase the simultaneous edit radius to 6--7, not
retune the old one-entry temperature schedule.

## Live RunPod batch

Four old one-entry workers with no verified hit were retired after roughly
43--45 minutes; this has no negative mathematical meaning.  Four target-LNS
runs now occupy the same low-priority CPU slots:

```text
lns701  CPU 9   canonical basin    RNG 701
lns702  CPU 21  relocated basin    RNG 702
lns703  CPU 25  plateau basin      RNG 703
lns704  CPU 28  unrestricted basin RNG 704
```

Each uses a unique output path, a 256 MiB address-space cap, 21,600 search
seconds, and 21,900 seconds of external timeout.  A zero exit triggers both
C++ verifiers and the independent Python verifier; `.VERIFIED` is created
only if all three return zero.  Launch memory stayed essentially unchanged
and the RunPod cgroup OOM counter remained 35.

## Radius-six/seven successor

The first four runs (`lns701`--`lns704`) ended normally after 309,356 total
large-neighborhood rounds without a universal word.  This is heuristic
evidence only and has no lower-bound meaning.  The two later radius-three-to-
five runs (`lns705`,`lns706`) remain independent.

The audited successor is

```text
scratch/search_unrestricted_word_target_lns_wide.cpp
```

It includes the frozen evaluator/search source, but replaces the targeted
move by exactly six or seven simultaneous edits.  Its final candidate pool
has separate quotas for all six `(radius,creator-style)` classes, so radius
six cannot crowd radius seven out of either ranking stage.  Candidate
selection uses precomputed randomized unique-load orders, and the assignment
search draws mostly from masks whose untouched witnesses are endangered.
Every protected-target invariant is checked at runtime even under
`-DNDEBUG`; the inner loop also polls the deadline.

The final source hashes are

```text
be9ab52dbb365ffdaab09f1db9a97d10e1f795a081d9d1683925e123554918c7  scratch/search_unrestricted_word_target_lns.cpp
5e0aa12bff815a29cb971dd69d94658516a05c009ab8be2fabf42644567bd06d  scratch/search_unrestricted_word_target_lns_wide.cpp
```

The warning-clean Rose binary has SHA-256

```text
08a0004fb7891f4f4a3ad83895a935ff1c63411dd1a95a5c33e7aaa10c422bd9
```

A 60-second remote smoke completed 258 rounds.  Its first exact-pool ledger
was

```text
raw/proxy/exact=
4007/64/4,29/29/4,523/64/4,32/32/4,4342/64/4,568/64/4
```

so every radius/style class was represented, and no invariant or evaluator
check failed.  Four six-hour one-thread production runs are live on Rose:

```text
wide1701  CPU 9   canonical basin    RNG 1701
wide1702  CPU 21  relocated basin    RNG 1702
wide1703  CPU 25  plateau basin      RNG 1703
wide1704  CPU 28  unrestricted basin RNG 1704
```

Independent watcher processes run all three exact verifiers after each
search ends and create `.VERIFIED` only when every verifier returns zero.
The watcher source is `scratch/watch_verify_k11_candidate.sh`.
