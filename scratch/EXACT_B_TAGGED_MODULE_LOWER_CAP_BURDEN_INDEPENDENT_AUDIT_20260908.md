# Independent audit: tagged-module lower-cap burden

Date: 2026-09-08. Reviewer: `exact_b_induction`.

Reviewed source:
`scratch/EXACT_B_TAGGED_MODULE_SECTOR_MOMENTS_AND_LOWER_CAP_BURDEN_20260908.md`,
together with the width-preserving correspondence in
`scratch/EXACT_B_TAGGED_CONTEXT_FUSION_20260908.md`, Sections 1–2.

Verdict: valid for the stated primitive module architecture. This is an
internal mathematical review. No new mathematical computation was run.

The sector equations count occurrences per permanent hub and unordered
hub pair correctly. The point-incidence equations distinguish core
coordinates from positional coordinates; summing their two rows gives
the claimed congruence. At k17 the 1,287 duplicate excess follows by three
disjoint singleton-hub target classes. It does not depend on independence
or a successful named-target design.

The endpoint argument in Section 5 is valid: fixed-width cells have
distinct right endpoints, and all interval unions ending at one endpoint
form a chain. A repeated rank-eight occurrence therefore consumes an
endpoint that cannot provide another rank-eight label. Removing or changing
one selected cell can reduce duplicate excess by at most one; a cyclic cut
discards at most two width-three cells. The resulting 1,284-cell change
burden, or 1,282 beyond a single cut, is correctly stated. A fixed-address
source-letter change affects at most three selected width-three cells, so
the limited 428-position lower bound is also valid.

Most importantly, these are **literal-preservation restrictions**. The
source explicitly allows a common-cap compiler to shrink the repeated
rank-eight intervals while keeping all width-four owners. Neither the
25595 preservation bound nor the cell-change count is used as a lower
bound on unrestricted words. Altering a cell label does not itself add a
source letter, and the note does not charge it as added length.

The pulse cap is a valid example of that escape. In a period-seven cycle,
the accepted retained pair has cyclic distances three and four. Every
width-four interval hits it, while exactly one width-three interval misses
it. That interval avoids the next-hub screen, so it is the claimed
single-hub rank-eight occurrence. Both candidate pairs avoid R and at least
one avoids L. Applying the same modification in all three ports preserves
the shared base contexts required by the fusion theorem.

The fusion's per-width correspondence depends only on screen positions,
port indices, and fringe lengths; the modified base letters retain the
same admissible form. Hence every fused physical width-four owner is
unchanged. Longer source intervals are unions of their consecutive
width-four owner intervals, so their values are unchanged as well. The
note correctly stops short of claiming that the surviving rank-eight
labels are all distinct or that the missing double-hub targets have been
created. The cap repairs the numerical type imbalance, not the unresolved
named-target partition or full lower compiler.
