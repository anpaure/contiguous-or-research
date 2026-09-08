# Exact pair-repair audit for the current `k=11`, length-476 one-hole seeds

Date: 2026-07-24

## 1. The two named seeds need no new pair-CNF run

The two Rose files named in the task are byte-identical to already audited
local artifacts:

| seed | SHA-256 | direct coverage |
|---|---|---|
| `k11_476_drop_last_one_move.word` | `660cb2ac66e1e357e7276be2b01b6399f9781485715cd2afb0964eeea11089ad` | 2046/2047; missing `493` |
| `k11_unrestricted_476_best.word` | `e866a1fb22db8675d9e33fad6d803eaf75721fd5b6c85d4e4186d652688cd87` | 2046/2047; missing `1763` |

Their complete arbitrary two-position replacement neighborhoods have already
been exhausted by `scratch/search_two_replacements_by_pair.cpp`.  For each
seed the run checked

```text
C(476,2) * 2047^2 = 113050 * 4190209 = 473703127450
```

ordered value assignments.  The relocated seed finished in 310.67 seconds
with maximum base counts `40,40,40`; the unrestricted seed finished in 198.88
seconds with maximum base counts `40,40,38`.  Both returned status 20 and

```text
UNSAT_SCREEN selected_pairs=113050 value_pairs=473703127450
```

The exactness of the three changed-interval categories and of the pair repair
mask has a separate source audit and an independent full-instance checker in
`K11_476_TWO_REPLACEMENT_PAIR_SOLVER_INDEPENDENT_AUDIT.md`.  Thus applying the
new generic pair-neighborhood CNF to these same two seeds would reproduce an
already stronger exact negative result, at much greater disk cost.

## 2. Relation to the generic pair CNF

`scratch/k13_exact_pair_neighborhood_cnf.cpp` is actually generic in the bit
count and word length.  At `BITS=11` it expresses exactly the same exhaustive
neighborhood:

* intervals avoiding both selected positions are retained unchanged;
* changed intervals are partitioned into `p`-only, `q`-only and `p,q` types;
* their unchanged OR bases are enumerated exactly;
* the two new entries are unrestricted nonzero 11-bit values.

The provider reduction was already exhaustively audited on small words, and
the direct pair enumerator supplies a structurally independent implementation
for the present `k=11` instances.

For scale, the certified `k=13` 1,850-pair star had 80,423 variables and
886,887 clauses, with 38,316 unsafe pair-target incidences and 76,698 provider
selectors.  A `k=11` seed has about 22.8 unsafe targets per unordered pair.
Linear scaling predicts roughly 5--6 million variables and 45--55 million
clauses for one monolithic 113,050-pair formula, ordinarily around a gigabyte
of DIMACS before its DRAT proof.  A lower-endpoint cell has at most 475 pairs,
so a sequential 476-cell certificate portfolio would keep only roughly
20--25 thousand variables and 0.2--0.3 million clauses live at once.  A more
efficient proof portfolio would use about 64 balanced shards of roughly 1,767
pairs each and delete each checked DRAT after recording hashes.  This is
useful only if a machine-checkable SAT proof portfolio is specifically wanted;
it has no remaining candidate-search value for the two seeds above.

## 3. Higher-leverage current queue

Rose contained fourteen other distinct, verified one-hole 476-entry snapshots
that had not received the complete pair screen.  The most promising targeted
LNS states were placed first, followed by the strongest unrestricted-SA states
and the older plateau state.  They were frozen by SHA-256 before search.

The production artifacts are:

* `scratch/k11_exact_pair_seed_queue_20260724.tsv`;
* `scratch/run_k11_exact_pair_seed_queue.sh`;
* `scratch/search_two_replacements_by_pair.cpp`.

The wrapper:

1. preflights and hash-copies the **entire** manifest into an immutable seed
   directory before either worker solves anything;
2. verifies that every seed has length 476 and exactly one missing target;
3. accepts an UNSAT result only if all 113,050 pairs and all
   473,703,127,450 value pairs were visited;
4. independently checks any SAT candidate with both `verify_or_array` and
   `verify_or_suffix` before creating `SAT_VERIFIED`;
5. uses only small word/log artifacts, not CNFs or proofs.

Two workers on Rose CPUs 12 and 15 should finish the fourteen-seed snapshot in
roughly 25--40 minutes based on the two completed benchmarks.  The solver's
working memory and persistent disk use are small.  If a new seed unexpectedly
has a pair repair family larger than the solver's 64-target bit mask, the
wrapper detects `selected_pairs < 113050` and stops with
`INCOMPLETE_UNSAT_SCREEN`; only then should the generic CNF be used on the
omitted pair family.

No finite bound changes unless a 476-entry candidate passes both independent
verifiers.

## 4. Completed RunPod result

The full fourteen-seed queue has now finished.  Priorities 1 and 2 completed
on Rose; priorities 3 through 14 completed on Purple.  Every seed returned

```text
UNSAT_EXHAUSTIVE
```

with all 113,050 position pairs and all 473,703,127,450 value assignments
visited.  No `SAT_VERIFIED` marker or candidate was produced.  Two deliberately
stopped duplicate Rose rows (priorities 3 and 4, status `ERROR_143`) are
superseded by their complete Purple runs.

Durable queue-ledger hashes are:

```text
b70c2f5d9df71d25af615491a7f3b4096794b147d4fabed4ae3e25effe2de785  rose worker 0
a64db0a6767c6db7ad36b534d9294f118305032b3affad025ea89c1cecf6b6c8  rose worker 1
9dcbc92ed7458c606a5926bf4154ad568398f4b7f10f74b6bfee1842767c66b2  purple worker 0
ce0a3b8a41af45119e44a0029ed986c04879e78d92e2a82ea8f5f4e2c80a438f  purple worker 1
b00f851bdf9f5786f47e7690afe1f2141f8b3097bd0c5b047e4db9304639b77e  purple worker 2
```

Together with the two previously audited named seeds in Section 1, this
closes the arbitrary two-position replacement neighborhood of sixteen frozen
476-entry one-hole words.  This is an exact direct-exhaustion result for those
seeds, not a global impossibility theorem for length 476.  The certified bound
therefore remains `465 <= nu(11) <= 477`.
