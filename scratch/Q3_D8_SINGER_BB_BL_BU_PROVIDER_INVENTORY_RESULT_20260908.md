# The original Singer skeleton has no BB+BL+BU provider completion

2026-09-08. The sole authorized h100 inventory completed with exit 0.
The program reported 0.5875787 seconds including serialization; the saved certificate's
elapsed field, measured before serialization, is 0.2895804410800338 seconds.
There was no LP, CP, higher-profile catalogue, restart, or additional
mathematical computation. Root, direct_route, and ternary_lift independently
read the complete source before execution; all three static audits passed.

## 1. Exact scope

Fix the verified 29-row, charge-424 skeleton in
`Q3_D8_SINGER_DIFFERENT_PROFILE_SKELETON_CERTIFICATE_20260908.json`:

    lower endpoint: 00112244 / 33776655, ranks 0,...,7;
    short seed:     01231230 / 46746575, ranks 1,...,7;
    central line:   (0,1,2) on coordinate 0, all other coordinates 1.

The first two representatives are developed under the Singer cycle and
global complementation, with the endpoint complement using ranks 1,...,8.
The fixed coordinate is infinity = global 0. Cyclic coordinates 0,...,6
correspond to global labels (1,2,4,3,6,7,5).

The tested providers are one bundle of each literal profile pair

    BB = AABBCCDD / EEFFGGHH,
    BL = AABBCCDD / EFEFGHGH,
    BU = AABBCCDD / EFGEFGHH.

Each pair uses eight distinct axes, each shore is cropped to ranks 1,...,7,
and each physical G = C7 x complement bundle contains fourteen rows.
The five permitted infinity-position patterns are exactly Section 4 of
`Q3_D8_SINGER_BB_BL_BU_AMENDED_PROFILE_LEDGER_20260908.md`.

These providers must partition all 26 residual critical flag orbits with
exactly one coordinate equal to one. They are the complete one-one
providers in the proposed remaining profile multiset

    BB + BL + BU + TT + NN + 5 NZ.

The necessary positive-weight caps are imposed on the skeleton plus the
chosen providers. They permit at most one critical excess unit with three
ones and the pattern's infinity value, at most one central two-one excess
unit with infinity = 1, and at most one such central unit with infinity
in {0,2}. Every other positive-weight repetition is forbidden. The
remaining seven bundles cannot remove any excess, so applying these caps
to individual providers is a valid necessary filter.

## 2. Complete finite pools and terminal result

Normalizing the first nonzero axis to global 1 leaves 12,960 ordered
embeddings: 5,760 BB, 4,320 BL, and 2,880 BU. Quotienting Singer translation,
shore exchange, and simultaneous word reversal leaves respectively
1,440, 2,160, and 2,880 distinct G bundles, for 6,480 total. There are nine
placement pools, each of size 720. All asserted counts passed.

The following pool counts are after individual flag and positive-weight
filters. An exact flag triple is counted before the final joint-cap test.

| Pattern | Infinity positions (BB; BL; BU) | Repeated critical infinity | Pool sizes BB / BL / BU | Enlarged union missing flags | Exact flag triples |
| --- | --- | ---: | --- | --- | ---: |
| 1 | interior; B-interior; B-B | 1 | 4 / 44 / 114 | G316 | 0 |
| 2 | endpoint; L-interior; B-B | 2 | 1 / 31 / 106 | none | 0 |
| 3 | interior; L-endpoint; B-B | 2 | 4 / 26 / 106 | none | 0 |
| 4 | interior; B-interior; B-A or U-H | 2 | 4 / 38 / 162 | none | 0 |
| 5 | interior; L-interior; B-D | 2 | 4 / 31 / 56 | none | 0 |

The enlarged union in pattern 1 permits every individually admissible
provider simultaneously. Even this union misses G316, with representative
code 559 and rank-seven target

    (1,0,2,2,0,2,0,0).

Its infinity-one two-triple has circular-gap type 223. Thus this pattern
already has an availability obstruction. The other four enlarged unions
cover the residual flag set, but none admits a disjoint 12+8+6 partition.
The exhaustive join examined 411 BB--BL pairs. Both catalogue_complete
and join_complete are true; status is COMPLETE, and the saved list of
feasible provider triples is empty. In particular, no candidate reached
the final joint-cap filter.

This closes the stated amended profile completion of the ORIGINAL
verified skeleton. The conclusion uses the five position patterns and
necessary projection caps proved for that completion. It does not exclude
other endpoint words, arbitrary profile multiplicities, arbitrary Singer
banks, or the general charge-2384 construction problem.

## 3. Why the finite exclusion is inspectable

The certificate retains every actual pair of words, its canonical G key,
its exact load on each target orbit, its 40-bit one-one flag mask, all
five filtered pools, and all join results. For a representative row,
if n cells lie in a target G orbit of size m, its developed bundle has
uniform per-target load 14n/m. This gives exact integer loads, including
any intrinsic repetitions. The source checks the row-incidence total
14*49 for every candidate.

For each pattern, the join considers every allowed BB and BL. When their
flag masks are disjoint, the needed BU mask is exactly their complement
inside the 26 required flags. Lookup against every admissible BU with
that mask is therefore exhaustive. No heuristic or optimization solver
is a premise of the terminal result.

Artifacts:

- Source: `q3_d8_singer_bb_bl_bu_provider_inventory_20260908.py`.
- Complete certificate: `Q3_D8_SINGER_BB_BL_BU_PROVIDER_INVENTORY_20260908.json`.
- Pure quota and parity prerequisites:
  `Q3_D8_SINGER_BB_BL_BU_AMENDED_PROFILE_LEDGER_20260908.md`.

## 4. Subsequent pure strengthening

Patterns 1 and 3 have independently audited pure proofs in
`Q3_D8_SINGER_BB_BL_BU_PURE_PATTERN_1_3_OBSTRUCTIONS_20260908.md`.
The new note
`Q3_D8_SINGER_BB_ALL_POSITIONS_AND_PATTERN_2_OBSTRUCTION_20260908.md`
proves that no infinity placement of a B/B bundle can supply the
223 necklace while avoiding the original endpoint flags, and uses this
to give a pure endpoint-only proof of pattern 2. Root independently
derived and audited that argument.

The complete finite result above remains the established exclusion for
patterns 4 and 5. A separately labeled working pattern-5 derivation is
not a premise of this result. No broader pure claim is made here.
