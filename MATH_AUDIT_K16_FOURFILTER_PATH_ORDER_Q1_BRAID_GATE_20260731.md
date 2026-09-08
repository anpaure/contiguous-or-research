# K16 seed0-derived path-order q1 braid gate

Date: 2026-07-31  
Scope: the authenticated rank-eight target order
`scratch/k16_fourfilter_insert_aug_d2_1_targets_20260731.word` only.

Provenance correction: despite the historical filename, SHA `e483dae4...`
is seed0-derived.  It is not a descendant of the genuine four-filter K15
parent SHA `51f57125...`, and none of this note's braid conclusions transfers
to the canonical genuine chronology SHA `0f6d64e...`.

## 1. Authentication and conventions

Let $T=(T_0,\ldots,T_{12869})$ be the source order.  Its SHA-256 is

```text
e483dae43cce3ca3e678958daab49f4237628f9b129df4f030fd83d83ffaa452
```

Every $T_i$ is a distinct rank-eight mask.  The missing adjacent-union
rank-nine colours are exactly

```text
A = 0xa9ce,   B = 0xb8ce.
```

All indices below are zero-based.  A two-opt `2opt(i,j)` removes the edges
$(i,i+1)$ and $(j,j+1)$, reverses the vertex interval $i+1,\ldots,j$,
and hence produces

$$
T[0..i]\;\cdot\;T[j..i+1]\;\cdot\;T[j+1..12869].
$$

A three-cut splice removes three distinct source edges and perfect-matches
their six endpoint copies.  It is accepted only when the resulting graph is
one path through all four preserved segment interiors.  This endpoint-copy
definition also covers adjacent cuts without silently identifying the two
loose incidences of a singleton segment.

Whenever a target order is hashed below, the byte representation is its
decimal masks separated by one ASCII space, followed by one newline.

## 2. Complete single-two-opt theorem

The facet positions are

```text
F(A) = 2129,6479,7033,7238,7578,9330,9530,10447,12336
F(B) = 6404,6478,7578,8271,8780,9686,12519,12834,12869.
```

For an internal two-opt, the two new seams join positions $(i,j)$ and
$(i+1,j+1)$.  Enumerating only pairs induced by the displayed facet lists
therefore covers every two-opt that adds $A$ or $B$, without an
$O(W^2)$ scan.  There are exactly 136 such reversals: 72 add $A$, 64 add
$B$.  Their final q1-hole histogram is

```text
one hole: 4;  two holes: 45;  three holes: 87.
```

No reversal adds both missing colours.  Equivalently, the two possible
opposite-seam offset intersections are empty and the singleton `{6478}`;
one two-opt needs two distinct cut indices.  A prefix or suffix reversal
changes only one adjacency and also cannot add both colours.  Thus every
q1-exact path-order repair uses at least three cuts or at least two
successive reversals.

The independent complete audit is:

```text
scratch/audit_k16_fourfilter_aug_d2_1_q1_2opt_indexed_20260731.py
SHA-256 7ce2421a83b8eea59ec2472f2e27c5443364262c7ee1e42d8dfda8b5272973a4

scratch/k16_fourfilter_aug_d2_1_q1_2opt_indexed_20260731.audit.json
SHA-256 0160b17448816e620fbdba3a6427a08f2d76d9d9e320f907b837ce6c5b43775d
payload e4392f02ec864fdb58a3b89c16dd27cfdb4b12c74e3a8d64e4c73e1df01f95cb
```

## 3. The historically high-area one-hole router

Among the four one-hole reversals, the useful one is `2opt(2129,10447)`:

$$
P=T[0..2129]\cdot T[10447..2130]\cdot T[10448..12869].
$$

Its canonical-order SHA-256 is

```text
0a3a34c4f4c5e7e0fd474909a1010f2ca6d6df895bb869ac79cbacfbb757a08b.
```

It replaces q1 colours `29cf,a98f` by `a9ce,a9cf`.  Consequently its only
q1 hole is `b8ce`; its complete upper-hole set is

```text
{ a9fe, b8ce, b8cf }.
```

The unconstrained maximum-area three-start/three-deadline schedule gives
selected lower area 30098 and nominal capacity 30107, above the required
26332.  This made the order a useful historical diagnostic.  It does not make
the fixed order scalar-feasible once its mandatory upper debt is imposed:
the later exhaustive `b8ce`-pin theorem bounds every P/Q schedule by
`25745+9=25754<26332`.

## 4. Unique three-cut q1 completion of the source

In a q1-exact three-cut splice, two new endpoint pairs must have unions
$A$ and $B$.  Enumerate the $36\times36$ unordered facet pairs, the at
most two incident cut choices at each used endpoint, and the matching of the
two remaining endpoint copies.  Reject repeated cuts, loops, disconnected
segment graphs, and any loss of an old q1 colour whose source multiplicity
falls to zero.  Exactly one connected configuration remains:

```text
removed source edges: 2128, 6404, 6478
new endpoint pairs:    (2128,6405), (6404,6478), (2129,6479)
new unions:            39cf,        b8ce,        a9ce
```

Its order is

$$
T[0..2128]\cdot T[6405..6478]\cdot
T[6404..2129]\cdot T[6479..12869],
$$

where the third displayed block is descending.  Its canonical-order hash is

```text
1133c5d4c7aff3a9888125c9d34b5ac29b0463bb03d8d8fc34b9c5e745124a89.
```

The removed q1 colours `29cf` and `39ce` had source multiplicities 2 and 3;
the third removed union `b9ce` has rank ten.  Thus the final q1 deck is
exact.  Full interval replay nevertheless leaves precisely

```text
{ 7bce, b8cf, b9ce, b9fe }.
```

The exact three-hole DP has area 25830 and capacity upper bound
$25830+9=25839<26332$.  Hence the unique minimum-cut q1 completion is both
upper-incomplete and compiler-dead.

This row and the strict two-opt corollary below were independently replayed
by:

```text
scratch/audit_k16_fourfilter_aug_d2_1_threecut_strict2opt_20260731.py
SHA-256 72aa84ebf26d413adc73eb08b64938f18f270a9e78d660fec9ed958737add1f5

scratch/k16_fourfilter_aug_d2_1_threecut_strict2opt_20260731.audit.json
SHA-256 cc6978a298e8580735d18432c630990769970fe4ef89ad58ef6a6445b82b9af0
payload fa76e28bcfaa388894bf34fe32b4ab7cebb7d57d3e532cd56e5072adc4234af1
```

## 5. Complete three-cut second-braid obstruction

For the historical local census, work from the high-area parent $P$.  Its nine $B$-facet
positions are

```text
2891,3797,4306,4999,6099,6173,12519,12834,12869.
```

The enumeration is complete as follows.

1. Choose the unordered facet pair forming the required new `b8ce` seam.
2. Choose one incident removed edge for each selected occurrence.
3. Choose the third distinct removed edge.
4. Perfect-match the four remaining endpoint copies in all three ways.
5. Retain exactly the connected four-segment paths with a complete q1 deck.

The indexed endpoint-copy loop has 4,940,208 generated rows before
deduplication and gives 15,652 distinct q1-exact cut/matching
representations.  This count is of
literal representations; an inertly reinserted third edge can give the same
final target order as a two-opt.

The target `a9fe` is absent from every preserved segment interior.  If a
rethreaded path witnesses it, the witnessing interval crosses a new seam,
so the union of that seam's two endpoint masks is a subset of `a9fe`.
This necessary seam test leaves exactly 73 representations: 72 with
nonadjacent cuts and one adjacent/inert representation.  Exact arbitrary-
width interval replay on all 73 gives

```text
number of upper holes  3   4   5   6
number of cases       60   8   4   1
```

In particular no three-cut second braid is upper-complete.  The closest
defect sets include

```text
{ 7bce, a9fe, b8cf }
{ 7bce, b8cf, b9ce }.
```

This closes every three-cut completion of the high-area one-hole
router, not merely the obvious 74-row reversal.

The frozen complete atlas is:

```text
scratch/audit_k16_fourfilter_aug_d2_1_second_threecut_upper_20260731.py
SHA-256 a53e7c9ff85b7d8957601a33e92d248d6b39c22dfea0043ea3fafc6e7c5ef8f0

scratch/k16_fourfilter_aug_d2_1_second_threecut_upper_20260731.audit.json
SHA-256 f970162ddfe5a541e030782d2dcff297bf54475f3065649f8caee728b60a77d1
payload d7c3ab5dce72559e50654fc7d7877e659ee9b698e98734792e5a62496570c821

scratch/replay_k16_fourfilter_aug_d2_1_second_threecut_upper_20260731.py
SHA-256 70e5672cd526435022fefd197bdb815235fc3f409a8370d8dad566e3cead2fec

scratch/k16_fourfilter_aug_d2_1_second_threecut_upper_20260731.replay.json
SHA-256 e2a160be3925516d1ecb6f2da963e230b76b97b68032c644ccce22afcb46e7b0
payload 9b8129b4d12a0b05e9a74480fa9f348200680f4ed45de6159ab328be1e8a46b6
```

The replay independently reconstructs all 73 literal paths from their
endpoint-copy records and rechecks their q1 and full upper languages.  The
bound generator, not the replay, is the load-bearing completeness proof for
the 15,652-to-73 enumeration.

## 6. Two-reversal monotone-descent corollary

Among all first two-opts that add at least one original missing q1 colour and
leave at most two q1 holes, there are 49 candidates: four with one hole and
45 with two.  Reapplying the same exact indexed q1 test yields six labelled
two-reversal completions and only three distinct final orders.  Their hashes
and scalar capacity upper bounds are

```text
1133c5d4c7aff3a9888125c9d34b5ac29b0463bb03d8d8fc34b9c5e745124a89  25839
dfbc14ffc786b93b8ed2a69ed1feee32f65745a99947135a33142bbe69c55063  25751
261643b0d4d6c5f5022916b882d7fa06b410b5003da6e19791c0c3643c5b57a6  22113
```

All are below 26332.  This is a scoped monotone q1-service theorem: it does
not cover a first neutral router that serves neither old hole, a first move
that temporarily creates at least three q1 holes, a four-or-more-cut second
braid, or an endpoint-changing splice.

## 7. Archival scope after the all-schedule scalar closure

The fixed source order, every one-reversal repair, the unique minimum-cut
q1 completion, every three-cut completion of the high-area one-hole router,
and every monotone two-reversal completion above were closed within this
local census.  The later mandatory-`b8ce` all-schedule theorem closes the
entire P/Q fibre of `0a3a34c4...`, so the formerly advertised second-braid
branch is no longer live.  A genuinely different construction would need at
least one of:

- a neutral path-order router before serving either q1 hole;
- a second braid with at least four genuine cuts;
- a splice changing one or both path endpoints;
- a different middle target order.

Nothing here is a no-go for those larger architectures, nor for arbitrary
K16 words.  In particular it does not turn a finite local braid census into
a global lower bound.
