# Exact k18 optimum: independent first-occurrence verification

2026-09-08. The newly supplied literal word independently passes an exhaustive ordinary-interval OR census by `exact_b_finite_frontier`:

    nu(18)=B(18)=48,623.

This is an exact finite result. The upper bound follows from the literal file itself and does not depend on the newly submitted general extension proof or its generation history.

## Literal input and independent algorithm

User input: `/Users/amir.nuriyev/Downloads/k18_optimal48623.word`.

SHA-256: `6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5`.

The file contains exactly 48,623 integer letters, each in `[1,262143]`. All are nonzero subsets of the 18 coordinates, with coordinate c represented by bit `c-1`.

The independent checker enumerates interval ORs by **first coordinate occurrences**. For each left endpoint i and each coordinate c, let p_c be the first position at or after i whose letter contains c, or infinity if none exists. As an interval's right endpoint increases, its OR changes precisely at the finite positions among the p_c. At an event position p, all coordinates with p_c=p must be added together before recording a target. Between event positions the union is constant. Thus these grouped events enumerate exactly all nonempty ordinary interval ORs beginning at i.

Scanning left endpoints backward updates the 18 first-occurrence positions directly. At each start the code groups coordinates by position, visits those positions in order, and records the cumulative OR and one actual inclusive interval witness. It uses neither the ending-suffix recurrence nor a segment tree, and it never wraps around the word. Grouping equal first-occurrence positions prevents any unrealizable intermediate subset from being counted.

The census visits exactly **607,684 grouped OR-change events** and finds **all 262,143 nonempty targets**, with **zero missing targets**. The distinct counts by ranks 1 through 18 are

    18,153,816,3060,8568,18564,31824,43758,48620,
    43758,31824,18564,8568,3060,816,153,18,1.

These equal the exact binomial counts at every rank. One ordinary nonwrapping witness interval is saved for each target.

The single deterministic run executed only on `ssh h100`, hostname `arboghast`, with limits of 30 CPU seconds, 45 wall seconds, and 1 GiB address space. The reported census time was 0.5496 seconds. Root separately checks the supplied file with the ending-suffix algorithm and independent interval replay; this note attributes only the first-occurrence computation to this agent.

## Matching finite lower bound

The established endpoint argument applied at rank nine gives W=binom(18,9)=48,620. There are 106,761 required nonempty targets below rank nine. If a universal word had length W+t with t≤2, every such lower target would have to occur in an interval of length at most t, giving at most

    tW+t(t+1)/2 <= 2W+3 = 97,243

possible lower targets. This is less than 106,761. Therefore every universal word has length at least W+3=48,623. The checked literal word attains this lower bound.

The same endpoint proof was already recorded and independently audited for the exact finite frontier; its general proof is unchanged by this new literal certificate.

## Reproducible artifacts and scope

* [Independent checker](verify_k18_optimal48623_first_occurrence_20260908.py).
* [Exact report](k18_optimal48623_first_occurrence_20260908/k18_optimal48623_first_occurrence_certificate.json).
* [Byte-identical literal word](k18_optimal48623_first_occurrence_20260908/k18_optimal48623.word).
* [All ordinary interval witnesses](k18_optimal48623_first_occurrence_20260908/k18_optimal48623_first_occurrence_witnesses.jsonl), each row `[target,zero_based_left,zero_based_right]`, endpoints inclusive.

Remote artifacts: `/home/amodo/exact-b-k18-optimal48623-first-occurrence-20260908/`. Execution source: `/home/amodo/verify_k18_optimal48623_first_occurrence_20260908.py`.

The earlier ten-tail one-seam obstruction concerns a narrowly specified family and remains valid. This supplied optimum is certified independently; no inference from failure of that family to impossibility of an optimal k18 word was made. The all-dimensional equality question remains separate from the now exact k18 answer.
