# K17 core-augmenting parent rethread: exact bounded preflight

Date: 2026-07-31  
Status: solver-free scoped no-go with independent replay  
Scope: the authenticated K16 `c7be` chronology, one distinguished internal
reversal, and at most one prefix and one suffix reroot

## 1. Purpose

The fixed-`c7be` K17 occurrence-selector fibre is already closed.  This
audit changes the K16 parent edge chronology itself; it does not merely
choose different representatives from the old occurrence domains.

The parent is

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.
```

Every candidate is screened before any lower Hall, common-cap, or SAT model.

## 2. The minimal core-augmenting reversal

There are exactly 32,724 Johnson-legal, q1-complete inclusive internal-segment
representations of this parent; the enumeration includes degenerate
`[l,l]` identity rows.  Relative to the pivot colour `0x0bf5`, their
resulting multiplicities are

```text
1^14, 2^32709, 3^1.
```

The unique multiplicity-three move is nondegenerate:

```text
reverse parent rows [11148,12080] inclusive.
```

It changes the occurrence domain from

```text
{9176,10616}
```

to

```text
{9176,10616,11147}.
```

Thus this is the smallest canonical attempt to escape the first
opposite-choice core by changing the q1 occurrence domain itself.

## 3. Exhaustive endpoint family

Starting from that internally reversed parent, the audit exhausts every
prefix and suffix reroot which preserves Johnson adjacency and the complete
rank-nine q1 palette.  There are 115 valid representations and 91 distinct
parent chronologies after byte deduplication.

For every one of the 91 chronologies:

1. the 12,870 rows remain the complete rank-eight deck;
2. all 12,869 parent edges are Johnson edges;
3. all 11,440 rank-nine edge colours occur;
4. choosing the first occurrence of every colour gives an exact old
   rank-nine deck; and
5. adjoining the new coordinate to the parent deck gives, together with
   that old shore, all 24,310 K17 rank-nine masks exactly once.

Thirty-three of the 91 rethreaded parents retain every arbitrary-width K16
upper target.

## 4. Both forced-literal cores survive

For an upper target `S` and pivot colour `c`, the audit enumerates every
unique-blocker-free physical interval and every occurrence of `c`.  An
occurrence is retained precisely when some exact individual witness of `S`
can use it.  This is the literal interval criterion; no relaxation or SAT
inference is used.

Every one of the 91 parents retains both disjoint-choice obstructions:

```text
pivot 0x0bf5: targets 0x1bf5 and 0x0ff5 have disjoint allowed occurrences;
pivot 0x1ce7: targets 0x1def and 0x3de7 have disjoint allowed occurrences.
```

For example, the upper-best rethread in this family uses prefix end 6390
and suffix start 12727.  Its first core has

```text
O(0x0bf5)              = {9176,10616,11147}
allowed for 0x1bf5     = {9176,11147}
allowed for 0x0ff5     = {10616}.
```

The new third occurrence enlarges only the already-left side of the
partition; it does not resolve the conflict.  The second core on that same
parent is

```text
O(0x1ce7)              = {12781,12796,12811}
allowed for 0x1def     = {12796}
allowed for 0x3de7     = {12781}.
```

Consequently no one-occurrence-per-q1-colour U shore from any of these 91
parents can be upper-complete, regardless of the representative-selection
algorithm.

## 5. Independent upper and staircase preflights

The canonical first-occurrence K17 children are also far from the remaining
gates:

```text
minimum arbitrary-width K17 upper holes       218
minimum tail-start run-staircase loss        49,577
available K17 scalar loss budget              7,401.
```

More strongly, every child has a single interior coordinate run giving an
arbitrary-start loss lower bound greater than 7,401.  The minimum over the
whole family is 26,040.

For an interior run `[a,b]` of length `ell`, let `g` be the number of the
three start thresholds at most `b+1`.  Each such early threshold costs at
least

```text
L-(b+1+3),   L=24313,
```

while the exact clean-corridor condition forces at least

```text
max(0,3-ell-g+1)
```

deadline thresholds to be at least `a`.  Therefore this single run gives
the certified bound

```text
min_{0<=g<=3}
  g*(L-(b+1+3)) + max(0,3-ell-g+1)*a.
```

The family minimum 26,040 comes from the singleton run `[8680,8680]` in
bit 1.  It already exceeds the complete K17 scalar slack, so no monotone
three-hole start/deadline schedule can compile that child.

## 6. The other authenticated genuine-parent survivor

The independent genuine-four-filter endpoint audit supplies exactly one
other q1- and arbitrary-upper-complete K16 parent:

```text
scratch/k16_genuine_fourfilter_endpoint_reroot_12780_targets_20260731.word
SHA-256 3ce1e988e977dc84678d8c3926d0228f9fdc28f288ac53b753a3326ba4ede879.
```

Its provenance is frozen by

```text
scratch/k16_genuine_fourfilter_two_endpoint_reroots_20260731.audit.json
SHA-256 303de59c5b2c00ce5a4e440809b0d5f644f8f051de7fff21e61051d70d80e2a2.
```

This alternative also retains both forced-literal cores.  Its canonical
first-occurrence child has 215 upper holes and a single-run arbitrary-start
loss bound 34,317.  It is therefore not a viable replacement parent in the
tested two-shore normal form.

## 7. Verdict and exact scope

The scoped family is closed before lower compilation:

```text
PASS_SOLVER_FREE_SCOPED_NOGO.
```

The result proves neither a K17 no-go nor a no-go for all parent rethreads.
It closes exactly:

1. the unique single reversal that increases the first pivot multiplicity;
2. every q1-complete prefix/suffix endpoint reroot layered on that move;
3. the canonical first-occurrence K17 children of those parents; and
4. the other authenticated genuine-parent endpoint survivor as a fixed
   alternative.

A nonduplicate continuation must change a forced target's allowed-occurrence
set, not merely add another occurrence on the same side of its partition.
It must also remove the late singleton-run obstruction, most plausibly by a
genuine shore split/interleaving or a parent move through one of the forced
interval collars.

## 8. Artifacts

```text
scratch/audit_k17_coreaugment_endpoint_rethread_preflight_20260731.py
scratch/verify_k17_coreaugment_endpoint_rethread_preflight_20260731.py
scratch/k17_coreaugment_endpoint_rethread_preflight_20260731/audit.json
scratch/k17_coreaugment_endpoint_rethread_preflight_20260731/verification.json
scratch/k17_coreaugment_endpoint_rethread_preflight_20260731/best_parent.word
scratch/k17_coreaugment_endpoint_rethread_preflight_20260731/best_first_occurrence_u.word
scratch/k17_coreaugment_endpoint_rethread_preflight_20260731/best_child_sector.word
```

The independent verifier returns `PASS_SCOPED_NOGO_REPLAY` over all 91
distinct chronologies.
