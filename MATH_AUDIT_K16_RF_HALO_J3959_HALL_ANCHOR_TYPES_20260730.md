# Exact local Hall and physical-anchor theorem for RF-halo j3959

Date: 2026-07-30

Status: **PASS_EXACT_LOCAL_CATALOGUE; WIDER PHYSICAL REPAIR OPEN**.
This note uses only the lower generalized-COMP3 geometry of the authenticated
`j=3959` chronology.  The five upper holes are deliberately not imposed.

## Canonical Hall core

Write

```text
P = 2665,  Q = 8000,  C = 0665,
A_b = 0665 union {b},  b in {3,4,7,8,12,15}.
```

The exact candidate graph induced by

```text
{P,Q,C,A_3,A_4,A_7,A_8,A_12,A_15}
```

has nine left vertices and the following six right vertices:

| cell | source interval | envelope | mandatory | targets in the core |
|---:|:---|:---|:---|:---|
| 803 | `[267,270)` | `0765` | `0465` | `C,A_8` |
| 2939 | `[979,982)` | `0675` | `0461` | `C,A_4` |
| 4349 | `[1449,1452)` | `066d` | `0464` | `C,A_3` |
| 9215 | `[3071,3074)` | `1665` | `0265` | `C,A_12` |
| 19070 | `[6356,6359)` | `06e5` | `0661` | `C,A_7` |
| 27225 | `[10395,10397)` | `8665` | `0660` | `C,A_15` |

Thus every arm has its own unique cell, the core sees all six cells, and
`P,Q` have no cell.  This is the disjoint union of two isolated vertices and
a seven-left/six-right extension star, hence exact deficiency three.

## Exact local compiler condition

For a proper-prefix interval `I`, let `E(I)` be the OR of its maximal source
envelopes, let `M(I)` be its mandatory mask, and let `E_p` be the envelope at
source position `p`.  A lower mask `T` has an exact interval witness on `I`
if and only if

```text
T subset E(I),       M(I) subset T,       E_p intersect T != empty for all p in I.       (1)
```

Necessity is literal.  For sufficiency, forbid every non-`T` bit on `I`, put
each bit of `T` on one allowed position, and give every still-empty position
one allowed `T` bit.  Every carrier clause wholly inside `I` asks only for a
bit of `M(I)`, hence for a bit of `T`; carrier clauses not wholly inside `I`
can be met outside `I`.  The maximal envelopes then keep every middle-row OR
exact.  This proves the local condition before any upper-mask coupling.

For one physical interval to be an *alternative* anchor for every mask in a
family `F`, (1) is equivalently

```text
union(F) subset E(I),
M(I) subset intersection(F),
E_p intersects every T in F for every p in I.                                  (2)
```

## Smallest abstract augmentation

Nine distinct masks require nine distinct physical interval outputs.  The
current neighbour union has size six.  Therefore every incidence-only repair
must introduce at least three new right-vertex identities; extra incidences
on the old six cannot lower this bound.  Three new vertices and three private
edges are sufficient abstractly: one edge for `P`, one for `Q`, and one for
any member of the seven-target star.

In the monotone external-anchor normal form, the exact size-three repair test
is an SDR for the three classes

```text
P-compatible, Q-compatible, star-compatible
```

on three distinct external intervals.  If old-cell incidences are also
changed, alternating paths through the old star are possible and the literal
nine-row matching must be replayed, but at least three new neighbour
identities are still necessary.  A multi-signature interval is only an
alternative provider: it still has capacity one in the matching and cannot
pay two of the three units simultaneously.

## Physical multi-signature consequences

Applying (2) gives the proof-safe types below.

* `P+Q`: since `P intersect Q=0`, the interval must have `M(I)=0`, must have
  `a665 subset E(I)`, and every position must intersect both `2665` and
  `8000`.
* `Q+star`, no top bit: for `C,A_3,A_4,A_7,A_8,A_12`, intersection with `Q`
  is empty.  Again `M(I)=0`; the envelope must contain `Q union T` and every
  position must intersect both masks.
* `Q+A_15`: here `Q subset A_15=8665`.  The exact type is
  `M(I) subset 8000`, `8665 subset E(I)`, with bit 15 available at every
  position.  The old top-arm interval has the right envelope but mandatory
  mask `0660`, so it is not a singleton-top anchor.
* `P+C`: the exact type is `M(I) subset 0665`, `2665 subset E(I)`, with every
  position meeting `0665`.
* `P+A_b`: the exact type is `M(I) subset 0665`,
  `P union A_b subset E(I)`, and every position intersects both `P` and
  `A_b`.  Each old arm interval already passes every condition except the
  missing `2000` envelope bit.  Making an old arm dual-purpose does not add a
  right vertex: if it serves `P`, its arm/core load must escape to a genuinely
  new anchor.

There are no exact multi-signature anchors of any of these types in the
frozen geometry.  In fact all 32,176 proper-prefix cells have nonzero
mandatory mask, immediately excluding `P+Q` and every no-top `Q+star` type.

## Exact repair frontier and disposition

The independently replayed one-predicate-bit frontier is:

| deficit class | exact frontier size | condition already satisfied |
|:---|---:|:---|
| `P` | 34 | all conditions except one missing `P` envelope bit |
| `Q` | 1,428 | singleton intervals with exactly one forbidden mandatory bit |
| external star | 207 | at least one star mask is one predicate bit away |

For example, the closest `Q+C` and `Q+A_15` alternatives are four singleton
positions, each missing one union bit and carrying one forbidden mandatory
bit.  A `P+Q` alternative is at least three predicate-bit violations away in
this geometry: two missing union bits plus one nonzero mandatory bit.

These counts do **not** prove that one chronology edit realizes one predicate
change: envelopes and mandatory masks are derived, coupled objects.  They do
show that the local physical conditions alone yield no wider solver-free
obstruction.  A broader no-go must couple how a chronology move changes the
three required anchor identities.  Only after such a lower repair survives
should the two upper chains

```text
4e79 < 6f79,       ca79 < ea79 < eb79
```

be imposed.

## Frozen artifacts

```text
scratch/k16_rf_halo_j3959_hall_anchor_types_20260730/
  audit_k16_rf_halo_j3959_hall_anchor_types_20260730.py
    SHA 64c41be90a684049dca770ca9b924b39d7d1824c8e79207b111249e08022374b
  hall_anchor_types.audit.json
    SHA 4cecacbf2291fd857f2b624dcd768a2d2abafb6fc8cf37c088fa44a9e99c2b24
    payload 4314e3f685318c751bd3887dddbfda3ae76368a3c58499e46f895ef5bd192219
  independent_replay_k16_rf_halo_j3959_hall_anchor_types_20260730.py
    SHA a083cacb8c972b468e64811ba16157a21da133a58096c9178d895f1625cf87f6
  independent_replay.audit.json
    SHA aeb91e3f1dfeb3b8b1a9357dd2017146b2e942d561dc106ed5643e1096e6fff0
    payload d4cf92d906eb76bf70989246538754c04070219e22f88e51b473d5cc2721b7c9
  physical_shore.tsv
    SHA 4805ce703535adedf5b43fa90a5df6b98888d1c2426365d8be731e13a9507620
  one_bit_anchor_frontier.tsv
    SHA bef3f6d400735ad2d329b3f5b52c7cb683c4a1938b7465989e6b4b6360a06ebc
  multi_signature_frontier.tsv
    SHA 1e63a6f90adc559452c08e35791895320e304a38677bce7efa817c8b299821b4
```

Input chronology SHA:
`edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee`.

