# `k=17` alternating carrier descent — consolidated frontier

## Status

This is the consolidated audit of the exact equivariant carrier campaign on
2026-08-02.  Every promoted row below passed literal quotient/physical
topology, rank-8 facet, rank-9 owner, rank-10 cap, positive-residence, and
complete cyclic upper-deck replay.

It is **not** a `k=17` universal word.  No promoted carrier is depth-three
resident, no source antecedent has been produced, and no lower compiler has
been solved.  The proved numerical status therefore remains

```text
B(17)=24313 <= nu(17) <= 25746.
```

## 1. Exact chronology

```text
state                          residence  rank11  rank12   model / factor SHA prefix
clean mixed leader                 1513     1496     238   f9e3b28f / 9ac262aa
connected C14                      1496     1496     238   27ffb0bf / f7aac306
connected C16                      1479     1479     238   2edc8bbf / c8f9da35
joint C18                          1462     1428     204   68a46820 / 7e8cd432
depth-four transfer packet         1394     1479     170   19c10ec0 / fa523da2
C18 repair                         1394     1445     170   740f74f9 / 0dc63730
depth-eight transfer packet        1326     1530     204   a4448031 / b28b179b
C18 repair                         1326     1496     204   a9c26d63 / b5f8720e
C8 upper-Pareto rethread           1326     1479     204   c22eead7 / 0e55494c
depth-eight transfer packet        1292     1547     272   f8dbbc5d / 75c2101a
C18 single-circuit plateau          1292     1547     272   unchanged
connected C14                      1275     1530     306   587169d1 / 4738670b
depth-eight transfer packet        1241     1513     306   b04b8b9d / 0ba9cbc2
C18 single-circuit plateau          1241     1513     306   unchanged
```

All counts are physical counts.  They are multiples of 17 because these
states are `Z_17`-equivariant.

The strict-residence row is frozen at

```text
/home/amodo/or15/work/root_k17_c68b_c6xc6_20260802/
  promoted_depth8_res1241/
```

with full model SHA
`b04b8b9dd3e83b6b4dfcf024e7de23265f1626e2369266537f39b2f66bac7a1f`
and factor SHA
`0ba9cbc25fa2062cb61ef7018f0fbb49a475ed0083b6b0bf21537ea84bc1cb95`.

The complete eight-shard C18 single-circuit census on this row has zero
accepted joint candidates.  Its scoped plateau manifest SHA is
`2dd75af3d1ac73dc3584cfe5c7c0dea31d3712df9d954209492d85df26d48337`.
C18 pairs are being enumerated separately; longer or non-equivariant moves
remain outside that statement.

## 2. Current Pareto frontier

Before the next C18 repair, three authenticated states are retained:

```text
role                 residence  rank11  rank12    orbit coordinates
strict residence          1241     1513     306    (73,89,18)
balanced residence        1326     1479     204    (78,87,12)
upper-deck Pareto          1394     1445     170    (82,85,10)
```

None dominates another in all three coordinates.  Search promotion must
therefore retain the frontier, rather than overwrite it with one scalar-best
file.

## 3. Correct well-founded measure

Let `P` be the positive run defect and `H11,H12` the two remaining upper
defects.  The scalar sum `(P+H11+H12)/17` is not monotone: the packets that
improve residence can temporarily expose more upper holes.

The proof-safe alternating coordinate is

```text
Theta = (P/17, (H11+H12)/17)
```

in lexicographic order.  A residence packet strictly lowers the first
coordinate.  A C18/C8 upper repair keeps the first fixed and lowers the
second.  The three current frontier points have respective `Theta` values

```text
(73,107), (78,99), (82,95).
```

Thus residence-first promotion is a lexicographic descent even when the
scalar sum rises.  A general theorem still needs an actuator-existence lemma;
the finite descent does not prove that lemma.

## 4. Transfer hypergraph and exact replay

Every cap-safe circuit is represented by a directed blocker-current
hyperedge with facet support, cap current, old/new quotient edges, voltage,
and literal move list.  The beam keeps at most 25,000 states per depth and
extends to depth eight; it does not enumerate all tuples.

Three decisive exact products were:

```text
parent  predicted delta  exact delta  outcome
1462          -68             -68      connected, promoted to 1394
1394          -68             -68      connected, promoted to 1326
1326          -51             -34      connected, promoted to 1292
1292          -51             -51      connected, promoted to 1241
```

The last row has a nonzero higher-order blocker interaction current.  This is
why additive signatures are proposal data only.  Every finalist is rebuilt
as a physical factor before promotion.

The failed depth-eight probe on the 1462 parent is equally important: its
best additive current predicted `-102`, but exact connected finalists achieved
only `-34` and did not beat the already promoted 1394 state.  Topology and
halo interaction cannot be inferred from aggregate currents.

## 5. Fail-closed orchestration

The residence driver is

```text
scratch/run_k17_alternating_descent_failclosed_20260802.sh
```

and its deterministic selector and beam are

```text
scratch/select_k17_transfer_promotion_20260802.cpp
scratch/search_k17_transfer_augmenting_packets_20260802.cpp
```

The driver authenticates its input, acquires one lock, enumerates non-C18
signatures and reduced packets, replays every finalist literally, preserves
accepted Pareto branches, and emits an immutable hash root.  C18 is a separate
phase and is never duplicated inside the residence driver.  Superseded tails
are explicitly marked `FAILED exit=143` after their useful tables are hashed;
they are not plateau claims.

## 6. Exact remaining gates

Even a terminal carrier with zero entries in the three displayed coordinates
would still need:

1. a literal depth-three antecedent with legal occurrence pins;
2. all strict-lower targets assigned to its short physical cells; and
3. a final exhaustive `2^17-1` universal-word replay.

Consequently, the residence number `1292` is neither an additive length gap
nor a claim that the answer is 1292 positions away.  It counts forbidden
positive runs in the current carrier architecture.
