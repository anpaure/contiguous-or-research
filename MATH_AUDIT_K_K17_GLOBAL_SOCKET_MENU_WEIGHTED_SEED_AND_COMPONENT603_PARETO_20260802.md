# K17 phase-zero global socket menu, weighted seed, and component-603 Pareto audit

**Date:** 2026-08-02  
**Status:** proof-audited phase-zero outer/menu results and one independently
replayed strict Pareto improvement.  This note does **not** certify `1S-ROTS`,
because the best fixed table below still has thousands of empty short-role
rows.  It makes no phase-one, chronology, residence, upper-shadow,
common-cap, compiler, or word claim.

## 1. Complete phase-zero dummy-short local overapproximation

The input is the authenticated original table

```text
scratch/ad_k17_seed4015_iterative_relay_projection_zero_20260802/
  in/original.res1972.tsv
SHA-256 db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185
```

For every one of the `18,646` eligible hard slots `v`, the census enumerates
all locally realizable predecessor/successor long states obtained from every
compatible moved bottom token, plus all `17` fixed soft longs, all four long
flags, and all nine relaxed short addresses.  The exact host index is:

* a predecessor root is one of the rank-eight subsets of the short owner;
* a successor owner is one of the rank-nine supersets of the short root.

This index is complete: the predecessor's three cells have union its root
and are capped by the short owner; the short's three cells have union its
root and are capped by the successor owner.  The complete fixed-table edge
census independently has `29,744` accepted predecessor and `29,775`
successor roles, with zero violations of these two identities.

The five-cell test is the literal relaxed-nine merge, with `beta<=alpha`.
If the endpoints use the same hard host, token and flag must agree; distinct
hard hosts must use distinct real bottom tokens.  Thus the menu is an exact
**local partial-matching-compatible overapproximation** of globally
extendable sockets.  Emptiness is a proof-safe global zero.  Nonemptiness is
not a residual matching extension certificate.

One nice-15 H100 CPU run under an 8-GiB address-space cap gave

```text
slots                                      18,646
candidate endpoint pairs checked      209,817,496
locally feasible occurrence tickets    71,289,574
proof-safe global-zero slots                 8,479
candidate short bank A                     10,167
elapsed                                     20.75 s
peak RSS                                    18,944 KiB
```

The output is explicitly `phase0_only_as_encoded_by_input_owner_root_bijections`.
It is not unioned with phase one.

Frozen files are under

```text
scratch/k_rots_k17_joint_1s_20260802/global_dummy_phase0_frozen/phase0_full/
```

with principal hashes

```text
builder source       0a114eac53e01c48370486bbd402c92035658288c2b9f6168753565cf784bb03
audit JSON           6ae6cc38c135e713406118bf30fdfbd50da4f2fc191c4855446c65e632e3a921
slot menu            af2fb59a6037785b68643332995f157e0b8a3fcf0d73bc908cc9f06afc50a31f
witness menu         1d78ed8411612c99cb7d9d92dfe4c0dfa84c7f71dc1a8f3afb58e31eb5d7dbfb
```

## 2. Exact outer Hall and weighted seed

Forcing every zero slot real leaves `A=10,167`, `Z=8,479`.  The two exact
augmented-matching Hall tests both pass at equality:

```text
full right shore                  cut/threshold/slack = 18646/18646/0
mandatory F union Z shore         cut/threshold/slack = 10227/10227/0
```

Weighted cotransversal-matroid greedy, with flag diversity primary and
local ticket degree secondary, gives a static exact table with

```text
X/P/S                           1748 / 16898 / 1748
selected-local-degree sum              33,479,147
selected flag-pair union                    0xc431
dummy cost                         -8007033479147
```

The table replays all `65,535` named lower targets.  Its complete fixed
relaxed-nine audit is nevertheless negative:

```text
supplier matching                      16,869 / 16,898 (deficiency 29)
socket triples                                      2,407
zero short roles                              5,949 / 7,395
```

An independent coordinatewise 32-state DP verifies every emitted triple and
all zero candidates.  Hence the weighted table is only a pricing incumbent;
no fixed-table SAT was launched.

Principal frozen hashes in
`global_dummy_phase0_frozen/weighted_seed_phase0/` are

```text
materialized table   3886de626d55d4393d3f71f51fa9799488608f26eb977a8ff60e7be39cfac7cd
selection            c880bcecb7c5ec95e812babe4afc7f1bc2ccb1df27a3708904cca94c7aa510e9
selector audit       d8879a6fab905fd5035c40bb5651d4acf4873b59836aee50c5c66078ab578aea
Hall audit           d8d7f5aa451d6ac8c3fb6b08b2cb06f3bf5b8ca8fe7ce7031ccc985998a5d92f
fixed audit          d5503a83a6482e349bc2f41e3993278c141ac3b039ab3123b351d03de95bf0cc
```

## 3. Exact round47--weighted component face

The symmetric difference of the round-47 real matching and the weighted
real matching has

```text
alternating components       1,589
fundamental-exchange paths   1,571
same-short-bank cycles          18
paths removing a round47 global-zero short   693
```

The components are vertex-disjoint.  Flipping any one path is therefore an
exact `M_short` basis exchange; flipping a cycle is an exact same-basis
matching-fibre circuit.  A complete incremental replay of all `1,589`
single-component flips finds `1,425` supplier-perfect candidates, including
`622` paths which remove a globally zero round-47 short.

This does not make per-component gains additive.  Supplier edges depend on
up to two component bits and socket records on up to three; subset flips
must be recomputed by their exact truth tables.

## 4. Component 603: first strict Pareto incumbent

Component 603 is a non-atomic alternating path:

```text
difference edges             44
real-bottom steps            22
changed receiver rows        23
old short                  5022   (global local degree 0)
new short                 14492   (global local degree 90,632)
```

The occurrence ledger is frozen as `flip_ledger.tsv`.  It starts
`18342:18342->5022`, traverses twenty internal placements, and ends
`14492:14492->13511`; therefore it is not an atomic relay.

The full independent fixed-table audit gives

```text
hard supplier matching                 16,898 / 16,898
supplier deficiency                                  0
socket triples                                     2,207
zero short roles                           5,967 / 7,395
```

Relative to round47 this simultaneously preserves the perfect supplier
projection, increases sockets `2188 -> 2207`, and decreases zeros
`5969 -> 5967`.  The zero split changes

```text
             FIXED     F      H
round47       3200    1488   1281
component603  3199    1488   1280
```

The general 32-state coordinate DP independently verifies all `2,207`
emitted triples and all `2,209` tested combinations on the `5,967` zero
roles.  The candidate is therefore the first strict round47 Pareto
incumbent on the phase-zero one-component face, but it remains far from a
`1S` cycle cover.

Frozen package:

```text
scratch/k_rots_k17_joint_1s_20260802/pareto_component603_frozen/
```

Principal SHA-256 values:

```text
component table       54b8063b4f39afb8ffccabadb88f04b65edaa0a4321c343f84f15918d75f24f4
full audit            4ac8f356e7c4b6eb48b10f90210678981b097ba7db67756e8074d106c212dadb
socket summary        e63e5b35c7199b83f6cbf748081048230d129b401ee395850b1bd49688247535
socket triples        5a8fc3d76655ea27bef6910541187358ba7d86546ff8b3a6d5d867c3d47ae50e
zero roles            2ba38d567dc4ae3cfa8f31da2ffc93305ef6a4c2f6c87e012bdc89c1e5a3d446
coordinate-DP audit   cb8364c67dd8f486aadd2986231f579cb758fe02e2ffc7de522ab3293606c57b
flip ledger           ea6ef70c52a7f077d4443d5b406d23febf752784c5d2b590d5f28f0029f8426b
component evaluator   244dbf09cc2179518e17409f56c9b4e6b36fd7a555128dd60cfcd7f896de1bb8
indexed socket audit  b8f73de61ca62e880d417faac43c96f305c9c9a36bf8b00f038c74a9abac92e1
coordinate-DP source  0a2d5adeba2a3aeaa9229f7e15336207d857e1285868a73a1bd9004f5e5c9c6f
path-ledger source    8dd4ab2cc87cbb4cfcca9aa42f765a1fe2a3316b42795c43732744c98cc099cd
```

## 5. Exchange and current rebase

Aggregate slot degree/masks do not define a socket matroid.  The separate
authenticated occurrence-level audit in
`MATH_THEOREM_A_PRIVATE_SOCKET_RADO_FACE_AND_SHARED_HISTORY_NONMATROID_GATE_20260802.md`
(SHA `41e66d1cf46ba60760a21bfa8910639d3696cee423a5aa1b2f4045cf8520ee64`)
already gives the literal augmentation failure

```text
I={4183},   J={4218,4250}.
```

Thus no matroidality is inferred from the present global menu.

The authoritative next face is now the independently replayed protected
H-short bank in
`MATH_THEOREM_K17_PROTECTED_H_SHORT_PRIVATE_BANK_AND_FIXEDFREE_BRANCHFLOW_GATE_20260802.md`
(current SHA `cb787301bbab64ef0f2af4515b7e8ddf82f20031db7893ba76cca383fda5bd65`).
It pins `1,748` private H-short tickets and leaves the exact `5,647` fixed/F
role DNFs plus residual long--long and supplier Hall completion.  Therefore
component 603 is frozen only as a prior-face Pareto milestone; no further
H-only dummy-cost search is justified.
