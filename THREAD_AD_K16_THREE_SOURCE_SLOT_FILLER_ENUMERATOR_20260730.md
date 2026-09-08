# K16 three-source-slot filler enumerator

Date: 2026-07-30  
Lane: AD  
Status: **source frozen and syntax-audited; H100-only census not run locally**

Source:

`scratch/search_ad_k16_three_source_slot_fillers_20260730.cpp`

SHA-256:

`62f877a8a966c7b054096365f6819e8c152739e24d9fa512ae5fcd540f572a90`.

Input manifest:

`scratch/ad_k16_three_source_slot_fillers_20260730.INPUTS.sha256`

SHA-256:

`d17c9fc071c2c0fa7eaa45e55a0b2133e1799646061389cc1cf58ee3b0f718ef`.

The authenticated two-return parent is

`scratch/ad_k16_exact229_two_source_slot_fillers_20260730/upper_0.targets`

with SHA-256

`37a711b51046e32cd3c529f70c5a71fb4b079c5bc1f0cd384ec755473d733a17`.

The binary reconstructs that entire vector from bad2 before enumeration.

## Exact normal form

In original bad2 coordinates:

```text
A=[2186,2217) forward
B=[1266,1295) reverse
F=[6253,6263) reverse
G=[1522,1547) reverse
```

The parent puts (G) at (F)'s source slot, (F) at (A)'s source slot,
and (A+B) before old row 3846.  The new packet (H), of length at most 64
and either orientation, is deleted from its source and inserted at (G)'s
source slot.  Its source deletion remains a literal gap.

Every origin is audited to occur exactly once.  The five packet halos must be
pairwise strict-disjoint.  The structural (H) catalogue has 757,873
oriented entries.  The safe old-gap prefilter, used only at distance at least
six from the destination, leaves 19,274 entries.  Near-destination candidates
bypass that prefilter and are judged only after materialization.

Each candidate receives literal depth-three checks at:

1. the actual (H)-source gap;
2. the actual (B)-source gap;
3. (H) at the old (G) slot;
4. (G) at the old (F) slot;
5. (F) at the old (A) slot;
6. (A+B) at the destination.

Final replay independently requires terminal dynamic depth zero,
nonnegative depths, nonzero maximal envelopes, every middle row equation,
and unrestricted upper interval-OR completeness.

Unique upper-complete words are deduplicated by their full 12,873-row vector.
For each word the summary records exact `(allowed,mandatory)` data for five
boundary cells at each of the three moved slots (A,F,G).  Output and summary
paths must be fresh; exceeding 4096 unique outputs aborts as UNKNOWN.

This is complete only for one strict-halo-separated (H) of length at most
64, the fixed cascade and fixed destination.  Touching halos, longer packets,
moved slots/cuts, and changed row values remain outside scope.

