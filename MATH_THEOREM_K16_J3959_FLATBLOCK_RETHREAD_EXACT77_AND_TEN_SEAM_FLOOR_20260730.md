# Exact flatblock catalogue, ten-signature floor, and thirteen-seam repair floor

The stage-two orientation/capacity trade is not intrinsic.  Its structurally
perfect orientation has one 8,920-row endpoint component containing all
three duplicate pairs.  Split that component into

```text
pair(2), pair(2), body(6443), pair(2), body(2471),
```

and combine those five blocks with the six remaining occurrence components.
An exact signed-component DFS checks variable-depth maximal-envelope replay
incrementally and uses the sharp scalar-capacity upper bound

```text
current_capacity + current_depth * remaining_length
                 - (remaining_flat_pairs)^2 >= LAMBDA.
```

This is exhaustive over the resulting eleven signed blocks.  It visits only
621 prefix states and 77 capacity-qualified leaves.  The result is

```text
capacity-sufficient exact carriers        77
carriers retaining all five service tokens 77
```

An independent audit reconstructs every depth schedule and maximal envelope,
replays every target row, and byte-compares all 77 recorded envelopes.  All
pass; the scalar capacities range from 26,424 to 27,505.

Thus independently moving the three duplicate pairs completely breaks the
orientation/capacity obstruction.  The earlier one-break no-go was sharp:
the flats, not the whole endpoint component, are the correct atoms.

## Full arbitrary-upper replay

Every one of the 77 carriers was replayed against every rank-above-eight
target.  The exact upper-hole histogram is

```text
20 holes: 16 carriers
21 holes: 47 carriers
22 holes:  2 carriers
23 holes: 12 carriers
```

No carrier is arbitrary-upper-complete, so the lower Hall compiler is not
yet reached.  The sixteen best carriers are sixteen distinct target words,
but all have exactly the same twenty missing upper masks:

```text
4779 477b 4f33 56d9 5753 6a79 6b79 7137
8f3c 8f3e 8f7c 8f7e cf45 cf75 da56 db56
df45 e566 f566 f766
```

The variation among those sixteen words lies in component orientations that
do not change this upper spectrum.  They are therefore one upper-repair
class despite being physically distinct carriers.

## Exact ten-seam necessary floor

Any new witness for a missing upper mask that crosses a new component seam
must contain both rank-eight carrier targets incident with that seam.  For
the twenty-hole spectrum above, enumerate every endpoint-mask pair that is
contained in at least one hole and record the set of holes it can possibly
serve.  There are

```text
44,622 endpoint-mask pairs
21 distinct hole-cover signatures
signature sizes: 11 of size 1, 6 of size 2, 3 of size 3, 1 of size 4.
```

An exact set-union DP gives

```text
new seams   maximum holes coverable
1           4
2           7
3          10
4          12
5          14
6          16
7          17
8          18
9          19
10         20
```

Hence **at least ten new seams are abstractly necessary** to repair any of the sixteen
best carriers.  This is independent of residence and occurrence
conservation, so ordinary 2-opt, 3-opt, 4-opt, and every other move changing
at most nine joins are impossible before those stronger constraints are
even considered.

There is exactly one minimum ten-signature cover.  Each of its ten
signatures is realized by a complete graph on nine physical carrier
positions (`36` endpoint pairs), and the ten nine-position domains are
pairwise disjoint.  An exactly ten-seam reconnection would have to remove
exactly ten original path edges whose twenty endpoints are precisely the
twenty selected signature endpoints.  Among all ninety special positions,
however, only eleven original adjacencies exist.  Nine are mutually
disjoint; the last two form the chain `11977--11978--11979`.  Any size-ten
matching is therefore forced to take the nine disjoint edges and one chain
edge, but those nine edges already select four positions from signature
group zero, while an exact ten-signature realization requires exactly two.

Thus there are **zero physical ten-seam realizations**.  The next level can
also be closed exactly.  For eleven cuts, write `c,s,z` for the numbers of
old edges with two, one, or zero special endpoints.  Exposing the twenty
mandatory endpoints requires

```text
2c+s >= 20,  c+s+z=11,  hence c-z>=9.
```

The carrier has 11 double-special, 158 single-special, and 12,703 irrelevant
old edges.  Exhaustively enumerating the only possible `c=9,10,11` cases
gives 823,637 distinct eleven-edge cut sets.  **None** exposes two distinct
positions in every mandatory `K9` group (`covered=0`), before new-edge
pairing, phase, or residence is considered.

Therefore the occurrence-level lower bound is at least twelve new seams.
Exact signature enumeration shows moreover that there are `1,11,55` cover
subsets at widths `10,11,12`, and **every one through width twelve contains
the same unique ten-signature core**.  This makes the twelve-cut search
complete when formulated as ten mandatory signature seams plus two slack
seams.

That physical search was run on all sixteen best carriers.  Twelve carriers
have only ten double-special old adjacencies and have zero deficit-feasible
twelve-cut exposures.  Only IDs `47,54,63,70` have eleven double-special
edges.  Each has exactly seven feasible double-edge subsets and yields
253,952 covered cutsets and 270,336 mandatory-pair allocations.  Their
connected quotient-tree counts are respectively

```text
77,936; 184,160; 77,936; 184,112.
```

Full literal variable-depth replay finds **zero exact carriers** across all
four catalogues.  Therefore, for this complete sixteen-carrier common-hole
class, every upper-repair reconnection changing at most twelve seams is
excluded.  Its exact local repair floor is **at least thirteen seams**.  The
next search must use thirteen or more joins, or change the flatblock macro
before applying the upper repair.

Artifacts:

```text
scratch/search_k16_structural_flatblock_signature_dfs_20260730.cpp
SHA-256 c95192ced846ce8806c9c7310f4331ce636497e10884e3db21aa5b63fdd82fa8

scratch/k16_j3959_flatblock_rethread_20260730/audit_pruned.tsv
SHA-256 b0c0b34ef164633b9b3599718a14818b84e7c6ec01da35203185e5cc9a9dbf05

scratch/k16_j3959_flatblock_rethread_20260730/exact77_catalogue_remote.tgz
SHA-256 71ee4138dd6737807bb030c434a88cd1d67dfacf0f8b4c458c59d859bf12a71d

scratch/audit_k16_j3959_exact77_upper_signature_cover_20260730.py
SHA-256 197f3652bd49c067a495727b7012be3623f449e1810b3d7db17ad3d85f4476db

scratch/k16_j3959_flatblock_rethread_20260730/
  upper_signature_cover.audit.json
SHA-256 7ea0d786071c8df82186916069be887aa1ce1a16e1fbc77b061756976514ccb6
payload SHA-256 5a08758f97160c8e87fdd1d50e09e72f45db6df6c53314c6ddea5a508eb15a72

scratch/search_k16_j3959_exact11_signature_reconnection_20260730.cpp
SHA-256 b21725a7836ede5302b0b38cb33deddc704fffe9c8b7d4574f58c9d24660e4d8

scratch/k16_j3959_exact11_signature_reconnection_20260730/run.stdout
SHA-256 8ce1498b806186103e506e4ea8ca672911439f07c80331a7604c5d2545a12df6

scratch/search_k16_j3959_exact12_signature_reconnection_20260730.cpp
SHA-256 2f68f789fa20e6ff28b3366be216da8a63a69037309fd9a47c049e9f4c46ed4d

scratch/k16_j3959_exact12_all16_20260730/exact12_all16_results.tgz
SHA-256 134e26a68b7d6338151e05aad8ac79c68d2b992c17bd109ff7c8027e432c6d4e
```

Scope: the 77-carrier catalogue is exhaustive only for this eleven-block
flat-splitting of one stage-two structurally perfect carrier.  The
ten-signature and thirteen-repair-seam bounds apply to reconnections of this
sixteen-carrier common twenty-hole class.  They do not exclude changing the
eleven-block flat-splitting itself or starting from another one of the 61
non-best exact carriers.
