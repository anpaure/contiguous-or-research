# K16 upper-12874: exact delete-plus-one-substitution no-go

Date: 2026-07-30

## Result

Fix the verified universal word

```text
answers/k16_upper12874.word
length 12874
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

No length-`12,873` universal word is obtained by deleting one of its `12,874`
cells and then replacing at most one remaining cell by an arbitrary nonzero
16-bit mask.

This includes every adjacent two-cell-to-one-cell fusion: delete either member
of the pair and replace the survivor by the fused value.  It does not exclude
two or more substitutions after deletion, reorderings, a larger collar
reassignment, or an unrelated length-`12,873` word.  It is not an unrestricted
K16 no-go.

## Complete deletion census

For each zero-based position `p`, the exact multiplicity delta removes every
old interval through `p` and adds every new interval crossing the deletion
boundary.  An independent replay recomputed this delta for all `12,874`
positions and matched the retained ledger row for row.

No deletion remains universal.  The unique best deletion is `p=1`; its sole
hole is

```text
11373 = 0x2c6d.
```

The deletion-hole histogram is:

```text
holes:       1  2  3   4   5    6    7    8    9   10  11  12  13  14  15  16  17  18  19
positions:   1  3  3 184 931 1638 1889 1995 1655 1132 774 639 738 499 366 190 176   3  58
```

Every deletion has a nonzero intersection of its holes, so every branch was
passed to the substitution stage; none was discarded by an empty-intersection
shortcut.

## Why the substitution enumeration is exhaustive

Let `H_p` be the exact hole set after deleting `p`, and suppose changing one
remaining cell from `x` to `z` completes the word.  Every `h in H_p` was absent
before the change, so its new witness must contain the changed cell.  Therefore

```text
z is a nonzero submask of h for every h in H_p,
```

and hence `z` is a nonzero submask of `intersection H_p`.  The search enumerates
every such `z` at every remaining position.

At a tested position it removes exactly all old intervals through `x`.  A
target with an avoiding old witness survives automatically.  For every target
whose complete multiplicity was removed, the search enumerates every new
interval label

```text
left suffix OR z OR right prefix
```

and requires the label to reappear.  Thus a rejected row cannot be a universal
word, while any accepted row would be replayed and written literally.

Across all branches the capped H100 run evaluated `6,465,438,504`
position/value pairs, including `131,482` rows that installed all deletion
holes.  Every one of the `12,874` branch processes returned its exact
`NO_PASS` status; no candidate was materialized.  The full sweep took
`12:03.68` on one CPU core with a 4-GiB address-space cap.

## Authentication

The fail-closed audit independently:

1. replays all `65,535` targets on the source word;
2. reconstructs all `12,874` deletion hole sets and their intersections;
3. matches the deletion ledger and branch summary exactly;
4. reads all `12,874` retained branch transcripts from the compressed raw
   archive;
5. verifies each source-hole count, intersection, enumerated submask count,
   candidate-pair count, and terminal `NO_PASS`; and
6. requires the capped run to exit normally with no candidate file.

Artifacts:

```text
scratch/audit_k16_upper12874_delete_sub1_all12874_20260730.py
  SHA256 7616420cffdd0a715ed438a2cfd6075cc071294fcd1f733661257984529b1152
scratch/k16_upper12874_delete_sub1_all12874_20260730.audit.json
  SHA256 37a639798cacebd7c10dee0d529ecc9535d3a936daa1b82d16884da691894d1e
  payload 138b6c8cd9adb0d94c99dab9e2411091c09ce797157ab07b25ed71196aa506d9
scratch/k16_upper12874_delete_sub1_all12874_20260730/nonzero_common.tsv
  SHA256 d9b0f51d53f76ee2dcb85cbb0129c1db44225ba9055b87d4a10c847a270969d2
scratch/k16_upper12874_delete_sub1_all12874_20260730/summary.tsv
  SHA256 cb974199018493433ddfce8674b295323a87631dc61d996f10d24732b9e8ced5
scratch/k16_upper12874_delete_sub1_all12874_20260730/basin_stderr_logs.tar.gz
  SHA256 a59c41decf95e671973ebb4a1b96d903d3425b67c8245d236e63f8f3ae227031
scratch/k16_upper12874_delete_sub1_all12874_20260730/deletion_census.cpp
  SHA256 5d7a63e46391a71e966bdf8688165ec16acf6159fe43944abeb71b2e10cc9bd9
scratch/k16_upper12874_delete_sub1_all12874_20260730/search_k16_one_substitution_completion_nobest_20260730.cpp
  SHA256 2eaa69c150720783f565eee42f406619a6896e90d0216a8200984d0b24472847
scratch/k16_upper12874_delete_sub1_all12874_20260730/run.resource
  SHA256 87314b31ddb8a73f38b7f3979d18327b8f3f1fe14569feb591dd73dee1ed99fc
```

The raw run remains at
`/home/amodo/or15/work/root_k16_upper12874_delete_sub1_all12874_20260730`
on H100.
