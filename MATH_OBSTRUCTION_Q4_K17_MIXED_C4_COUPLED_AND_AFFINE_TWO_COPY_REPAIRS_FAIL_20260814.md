# Mixed-C4 coupled and affine two-copy repairs fail for the q4 k17 typed reserve

**Date:** 2026-08-14

**Status:** exact scoped no-go on the literal fourteen-rail recoupled states.
All 480 minimum whole-rail polarity assignments are exhausted for a mixed
C4 followed by one owner-disjoint C6 or C8.  The two-copy fallback is
exhausted for every common owner-simple affine relabelling of `Z_17` and
fails before resource testing: no collision-touching cut pair supports a
Johnson C4.  This is not a no-go for arbitrary `S_17` relabellings or for a
larger transition cable.

## 0. Typed setting and collision bank

The occurrence lift is the frozen pure-rail lift.  Each closed owner rail
is wholly lower or wholly upper; an edgewise mixture is outside this host.
The two recoupled states have respectively `160` and `320` polarity
assignments with minimum active collision excess one.  Their seven sole
collision types are

```text
state one
  64 lower-q2  10011000000001111  p10c4_1[1] = p11c0[6]
  32 lower-q2  00100000110001111  p11c2[0]   = pX1[2]
  64 upper-q2  11011100110001111  p10c4_1[3] = p11c1[7]

state two
 128 lower-q2  01000000110001111  n10c1[4] = nX2[5]
  64 lower-q1  01100000110001111  n10c2[0] = nX2[5]
  64 upper-q1  11101000110001111  n10c1[3] = n10c2[0]
  64 lower-q2  00010000110001111  n11c3[10] = nX1[2].
```

All owner edges, lower/upper q1 resources, lower/upper q2 resources, and
three-support collars below are rebuilt from the literal owner cycles in
the positive q4 k17 reserve certificate.

## 1. One mixed C4 plus one C6 or C8

For every minimum assignment, the first switch is every distinct exact
mixed unit C4 with one cut touching a provider window of its sole
collision and the other cut on an owner-disjoint rail edge of the same
polarity.  Thus its complete q1 current is one positive and one negative
ticket on each shore.

The second switch is independently every owner-simple alternating C6 or
C8 on existing edges of one pure polarity.  It is required to be
owner-disjoint from the C4 and to have the exact inverse **lower and upper**
q1 current.  Only after aggregate q1 cancellation would the verifier
rebuild the factor and require all four active q1/q2 decks to be simple and
the minimum union of three consecutive clock supports to be at least six.

The H100 census is

```text
                                            state one   state two
minimum polarity assignments                       160         320
distinct collision-touching mixed unit C4s         256         480
raw alternating C6 switches                       2576        3344
raw alternating C8 switches                       5840        6816
unit-current second switches                        80           0
inverse-current C4/second pairs                       0           0.
```

In state one all `80` eligible second switches are C6s, but none has the
inverse ordered pair of lower/upper q1 currents of any first C4.  State two
has no unit-current C6 or C8 at all.  Hence no owner, q2, or collar filter
is concealing a witness: the exact aggregate q1 matching is already empty.

This exhausts precisely

```text
one collision-touching exact mixed C4
  + one owner-disjoint same-polarity alternating C6 or C8
  + zero aggregate lower/upper q1 current.
```

It does not exhaust two further switches, a new-owner dummy phase, or a
transition cable whose second atom uses edges not present in the original
pure rails.

## 2. Two affine reserve copies with one cross-copy mixed C4

Fix one reserve copy.  Relabel the second by the same affine map

```text
x |-> a*x+b mod 17,  a in Z_17^*, b in Z_17
```

in both recoupled states.  Of the `272` affine maps, exactly `103` make the
two 146-owner banks disjoint in **both** states.  This common-map condition
is essential: a relabelling usable on only one shore is not a two-state
reserve package.

For a q1 collision, its unique provider edge is the only local cut that can
change that occurrence.  For a q2 collision at owners
`O_i,O_(i+1),O_(i+2)`, the cut menu is the two incident edges
`O_i--O_(i+1)` and `O_(i+1)--O_(i+2)`.  The cross-copy C4 class selects one
such collision-touching edge from each copy, deletes the two old edges, and
tries both cross matchings of their four endpoints.

The two selected cycles must have the same whole-rail polarity.  Joining a
lower rail to an upper rail would create one component with no legal pure
polarity, so opposite-polarity collision-type pairs are correctly outside
this occurrence class.

Quotienting the `13,184,000` minimum assignment pairs by their seven literal
collision types gives the exact geometric census

```text
                                                    state one   state two
common-map same-polarity collision-type pairs              515        1030
collision-touching old-edge pairs                          8240       10712
distinct C4 cross matchings                               16480       21424
legal Johnson C4 cross matchings                              0           0.
```

Thus no affine two-copy candidate reaches q1 current, q2 simplicity, or
residence.  The obstruction is the sharper endpoint-distance statement:
for every one of the `18,952` old-edge pairs, neither cross pairing consists
of two Johnson edges.

The search program also enumerates all `2,636,800` state-one and
`10,547,200` state-two assignment pairs.  The independent hostile replay
does not need that expansion: it reconstructs the same `103` maps and all
seven collision types, then proves the zero-Johnson result on the exact
collision-type quotient.

## 3. Exact remaining gate

The smallest surviving classes are now:

1. a non-affine `S_17` relabelling of the second reserve copy;
2. a cross-copy C6 or longer recut using more than one cut per copy; or
3. a joint transition cable/dummy phase adding new owners and changing the
   fixed-side q2 collar before the mixed-current move.

No generic claim is made against those classes.  In particular, the
`103/272` affine owner-simple count is not an assertion about all
permutations of the seventeen coordinates.

## 4. H100 provenance

The positive reserve source used by every run has SHA-256

```text
cae68fd6542d1925c3663c901f981fee596dfa10560fc01b278d367960c7573d
  MATH_THEOREM_Q4_K17_POSITIVE_ONE_OWNER_COMMON_RESERVE_20260814.md
```

Coupled C4 plus C6/C8 search:

```text
71ef130c9b64d4e5d305e4e164a0ed89d3181d3912aec8de279c461c01423a0d
  scratch/search_q4_k17_mixed_c4_plus_c6_c8_coupled_repair_20260814.py
627d052723abd509829d0b53c309770e457eee3a132444990e6f1baf4c9f7a15
  scratch/search_q4_k17_mixed_c4_plus_c6_c8_coupled_repair_20260814.h100.out
ac212b7085039dd67927bac835956d00a704642345e276e4697cfa2b5dc7ee55
  scratch/search_q4_k17_mixed_c4_plus_c6_c8_coupled_repair_20260814.h100.log
```

Affine two-copy cross-C4 search:

```text
140ef8ac641a0e3a1712c252a71e1959e34d36dc8fc4dc8c1a6ccfdc3f3e167f
  scratch/search_q4_k17_two_affine_copy_cross_c4_repair_20260814.py
635e7a8dec48b2f702ac7aa17883402e644525f5636f297fd2632469d27a96f9
  scratch/search_q4_k17_two_affine_copy_cross_c4_repair_20260814.h100.out
d4267b7b14f93fe72d24c9630c0d53666816fdd8cd87aa4abfe3052d07937626
  scratch/search_q4_k17_two_affine_copy_cross_c4_repair_20260814.h100.log
```

Independent hostile replay:

```text
16b36625ba50bd6f73b196efe01551b629a91877a7b047b705b20ff488c1a26a
  scratch/hostile_replay_q4_k17_affine_two_copy_cross_c4_no_go_20260814.py
5ad29a312ae026d8fa296c3a5b2c09a3d5c6b93682539fb8033407420ca7f83c
  scratch/hostile_replay_q4_k17_affine_two_copy_cross_c4_no_go_20260814.h100.out
568a8818654ba92dcf0d9d394aeb2413a5020e6cf0fa12a5d71b615b9ceac343
  scratch/hostile_replay_q4_k17_affine_two_copy_cross_c4_no_go_20260814.h100.log
```

All compilation, enumeration, replay, and hashing ran through SSH on H100.
The local Mac was used only for reading, editing, transfer, and Git.
