# The old non-Johnson PBBS prefix cannot have a one-pivot completion

Date: 2026-09-08.
Status: proved source/schedule obstruction. The old prefix is superseded by the separately constructed all-ports Johnson prefix; no claim here concerns that replacement.

## 1. Exact one-pivot obstruction

The old prefix is

    scratch/badsix_relaxed_306_owner_path.word.

It contains three non-Johnson adjacencies, at zero-based edge positions 50,101,152.

Suppose a complete chronology through all W=24310 rank-nine owners begins with this prefix and is realized by a universal word on the one-pivot schedule

    I_i=[i,i+2] for i<306,
    I_i=[i,i+3] for i>=306,

ending at physical position W+2.

Write b for the total non-Johnson steps and e for repeated rank-eight color occurrences among its Johnson steps. Since distinct rank-nine owners have an eight-element intersection precisely when adjacent in the Johnson graph, the number of distinct rank-eight adjacency colors is

    W-1-b-e.

Universal rank-eight coverage therefore requires 1+b+e rank-eight targets outside that palette.

The proved exceptional-facet theorem in

    scratch/K17_PBBS_PREFIX_RANK8_PROVIDER_INTERFACE_20260908.md

gives at most three such targets on this schedule: one initial prefix, the pivot cell [306,308], and one terminal suffix. Hence b+e<=2 is necessary. The prefix already has b>=3, a contradiction.

No Q ordering or lower common cap can repair this deficit while the old prefix and one-pivot schedule are fixed. This is not an unrestricted impossibility theorem for nu(17)=B(17).

## 2. General consecutive-start budget

Let a word of length W+d end at the last of W selected owner deadlines, and let its distinct rank-m owners be realized on intervals [i,r_i], with i=0,...,W-1 and strictly increasing r_i. Thus every position 0,...,W-1 is a selected start, and exactly d physical positions are unselected deadlines.

A rank-(m-1) witness ending at a selected deadline r_i, i<W-1, cannot contain the owner starting at i. Its start is therefore at least i+1, and it lies inside both consecutive owners. Its value belongs to their intersection palette. A witness ending at the last selected deadline belongs to one nested suffix family and contributes at most one distinct rank-(m-1) target outside that palette. Each of the d unselected deadlines similarly supports at most one distinct target of that rank.

Consequently

    missing adjacent rank-(m-1) colors <=d+1.

This needs no restriction on a final depth jump. For odd middle layers, where both adjacent layer sizes are W, it gives

    b+e<=d.

At k17,d=3, the old prefix with b=3 could only extend under a more general consecutive-start schedule if every future adjacency is Johnson and no rank-eight color is ever repeated.

The prefix itself has no rank-eight repeated color: e_inside=0. Thus this broader necessary condition does not alone exclude it.

## 3. Initial-depth restriction

Write h_i=r_i-i. Strictly increasing integer deadlines imply that h_i is nondecreasing, ending at d. If h_0>0, all rank-(m-1) targets using one of the initial h_0 missing deadlines and absent from the adjacency palette must start at zero; they form one nested prefix family. The other d-h_0 missing deadlines each give at most one exception, as does the final selected deadline. Hence

    missing adjacent facets <=d-h_0+2  when h_0>0.

For d=3 and h_0>=2 this is at most three, incompatible with the old prefix's b=3. Thus any conceivable consecutive-start extension of that old prefix must begin at depth at most one; keeping its early depth-two schedule cannot work.

If all strict depth jumps occur before the final owner, the sharper J+2 bound (or J+1 when h_0=0) further requires at least two jumps for b=3. In a k17 universal consecutive-start schedule, a final jump cannot be the sole way of reaching depth three: the exact lower-cell census is sum_i h_i+6, which must be at least 65535, forcing at least16909 owners at depth three. In particular the final two depths agree. These facts explain why simply sliding the old one-pivot location cannot rescue it.

## 4. Exact repetition location

The old prefix's two new Johnson seams have colors

    13654 at edge203,
    103764 at edge254.

Each occurs exactly once inside the prefix. The one repeated color in the mixed prefix/cycle stage is 13654: its second occurrence is the original edge of canonical cycle69 with upper owners

    30038,13655.

Both endpoints lie outside the prefix, and their intersection is13654. Any consecutive-start d3 completion preserving the old b3 prefix would have to omit this old Q edge, since retaining it would make e>=1 and violate b+e<=3.

The relevant mathematical checks were made only on h100 and retained remotely as

    /home/amodo/exact-b-k17-pbbs-inventory-20260908/prefix_internal_rank8_repetition.json.

They count all prefix adjacent intersections and identify the original repeated-color edge using the exact canonical f map. No new construction or port search was performed.

## 5. Supersession

The all-ports Johnson prefix announced later on September8 has b=0 and a different cut assignment. It is stored separately and does not satisfy the obstruction's fixed-prefix premise. The old 306/308 files remain a valid component construction and a useful failed one-pivot route; they must not be silently substituted for the replacement.
