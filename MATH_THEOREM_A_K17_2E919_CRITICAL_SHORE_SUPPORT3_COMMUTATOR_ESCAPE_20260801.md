# K17 critical-shore support-three commutator escape

## 1. Scope and frozen input

The frozen rooted static factor is
`scratch/laneK_k17_commonfirst_serial_20260801/common_serial03_ae88_seed20260801.final_rows.tsv`,
SHA-256
`2e9194935b261dc178daee3aaf47fc9acc1bf1f2af5b6eb31e5004bb4ffd9ceb`.
Its packet matching is 1172. Its common both-live root--owner graph has
maximum matching 1141, canonical Hall shore 309 to 20, and deficiency 289.

This note exhausts one precise next shell: primitive three-row resource
circuits that factor as two overlapping support-two circuits through the
frozen table. It does not exhaust every support-three resource circuit. All
claims concern only the static flag ledger and physical attachment-state
graph. They do not assert chronology, topology, upper shadows, residence,
voltage, opening, or compiler feasibility.

## 2. Resource-delta normal form

For root r, let f_r be its incumbent flag and g another literal option. Let
delta_r(g) be the signed difference between their type and lower-flag resource
incidences.

### Lemma 2.1 (primitive support three)

Three distinct-root replacements preserve the complete static resource ledger
if and only if

    delta_1 + delta_2 + delta_3 = 0.                       (2.1)

Under (2.1), the circuit is primitive if and only if all three deltas are
nonzero.

Proof. The ledger change is the coordinatewise sum in (2.1). If one delta is
zero, the other two are opposites, so the move is a unary circuit plus a
binary circuit. Conversely, if two nonzero deltas sum to zero, (2.1) forces
the third to vanish. This proves both statements. QED.

### Definition 2.2 (overlapping support-two commutator)

A primitive triple belongs to C_ov(F) if there are distinct indices i,j and an
intermediate option h_j at final root r_j with

    delta_j(h_j) = -delta_i(g_i).                          (2.2)

The first binary circuit changes r_i,r_j to g_i,h_j. Relative to that
intermediate table, h_j to g_j and the third-root change are opposites by
(2.1). Thus the final triple is literally the endpoint of two resource-exact
binary moves sharing r_j.

### Lemma 2.3 (complete canonical enumeration of C_ov(F))

The following procedure emits every member of C_ov(F) exactly once.

1. Index every nonzero literal delta by its signed resource vector.
2. For every terminal literal g_i, enumerate every distinct root r_j carrying
   an intermediate option with delta -delta_i(g_i).
3. Enumerate every nonzero final option g_j at r_j, compute the forced third
   delta -delta_i(g_i)-delta_j(g_j), and look it up in the index.
4. Reject repeated roots. Among all valid factorization witnesses of the final
   triple, retain the lexicographically first pair (optionID(g_i),r_j).

Proof. Steps 2--3 are precisely (2.2) and (2.1), so every emitted triple lies
in C_ov(F). Conversely, Definition 2.2 supplies an iteration of Steps 2--3
for every member. The final finite nonempty witness set has a unique
lexicographically first member. QED.

The authenticated class census found 2,718,743 nonzero nonincumbent literal
records in 2,033,054 nonzero delta classes. Thus an unrestricted class-pair
product is not a practical exact catalogue; Lemma 2.3 avoids it for this
shell.

## 3. Exact critical-shore pruning

Let P0 be the old 309-root Hall tail and H0=N_F(P0), of size 20. For a fully
replayed candidate F', put

    A = N_F'(P0) minus H0,
    L = H0 minus N_F'(P0),
    kappa = |A|-|L|.                                       (3.1)

### Lemma 3.1 (old-shore escape is necessary)

If the common matching of F' exceeds 1141, then kappa>0.

Proof. The frozen shore has deficit 309-20=289. In F', its neighborhood has
size 20+kappa. If kappa is nonpositive, the same left set still has deficiency
at least 289, so every matching has size at most 1430-289=1141. QED.

This condition is not sufficient. The generator therefore performs this
proof-safe sequence for each canonical triple:

1. replace all three literal rows simultaneously;
2. recompute every physical transition geometry incident with them;
3. rebuild both-live attachment-state incidences, counting distinct owner
   neighbors rather than state multiplicity;
4. retain only kappa>0;
5. run fresh Hopcroft--Karp on the complete common graph.

No additive matching score is used. The preliminary demand that some changed
active geometry be incident with P0 is exact: a common incidence rooted in P0
can change only through an incoming or outgoing physical geometry at that
rooted state.

## 4. Exhaustive shell census

Four deterministic H100 CPU shards used 202,322 oriented overlap anchors and
gave these aggregate exact counts.

| stage | count |
|---|---:|
| completion lookups | 383,603,199 |
| completion hits before canonicalization | 37,206,419 |
| distinct canonical primitive triples | 19,141,938 |
| triples changing a geometry incident with P0 | 12,948,128 |
| triples with kappa>0 | 1,711,267 |
| triples increasing the full common matching | **159** |

All four processes exited zero under one-core, 8-GiB-address-space,
1200-second CPU and 4-GiB-output caps. Audits and compressed cut-capable row
ledgers are in
`scratch/threadA_k17_2e919_dm_support3_commutator_20260801/`.

The generator is
`scratch/threadA_k17_2e919_dm_support3_commutator_generator_20260801.cpp`,
SHA-256
`01d8e60eeef744a3c066dc169b9f489601c412cd7c344052566bb08580d622a8`.

## 5. Literal one-unit escape

The lexicographically best retained triple is:

| root | option | old (type,C0,C1,C2) | new (type,C0,C1,C2) | delta |
|---:|---:|---|---|---|
| 81 | 155575 | (1,512,1260,1) | (5,676,1096,1) | -2,+6,+86 |
| 437 | 833409 | (5,5408,11,16) | (5,1314,4105,16) | -86,+132 |
| 1380 | 2627699 | (5,17413,2320,32) | (1,4,19729,32) | +2,-6,-132 |

The deltas sum coordinatewise to zero. Certificate hashes are:

```text
steps       cb7884b1118de28a8465b93c573979b5705dabc06975c9cac1d78ea14e1ab363
final rows  4f5fb7f2b0a5a29090925cddcdbfe124cd3930f0c36b88948f28d9cf41794acb
```

Independent literal replay gives:

| factor | common matching | Hall tail | Hall head | deficiency | old-shore head |
|---|---:|---:|---:|---:|---:|
| F | 1141 | 309 | 20 | 289 | 20 |
| F' | 1142 | 308 | 20 | 288 | 21 |

The old shore gains owner 246 through root 81 and loses no old-head owner.
The full common-incidence delta is

```text
+ (18,20)
+ (81,246)
- (437,208)
- (1415,1294)
```

The changed rows have a 215-root physical dependency halo. The final DM
regions are PLUS=(308,20), MINUS=(112,400), CORE=(1010,1010). A second
independent literal transition replay gives packet matching 1173, one above
the frozen value 1172; its audit SHA-256 is
`de061acb3c6d930aeeac3aa067a286cf86dd526030c0d585b29a1da24ecb2063`.

The independent verifier is
`scratch/threadA_k17_2e919_dm_support3_verify_exact.cpp`, SHA-256
`8793a033d53f82e2d1266d8040b0b534fd1ce3f08a922f07302fbcfc57d13921`.
Its audit SHA-256 is
`49b3f61d25bcc239055bbeed1977231c906eb0a751d6cbdd5464c580d13e6755`.

## 6. Exact boundary

The common-first plateau 1141 is not stable under primitive support three: an
explicit resource-exact three-row commutator reaches 1142, and 159 members of
the declared shell do so.

This remains far from a full common transversal; deficiency is 288. Hence no
quotient component profile or chronology exists to report, and no topology,
upper-shadow, residence, voltage, opening, or compiler conclusion is claimed.
The exhaustive claim is only for C_ov(F); primitive support-three circuits
without an intermediate opposite-delta option form a separate shell.

## 7. First serial rebase

The shell was regenerated from the independently verified factor
`4f5fb7f2...`, rather than reusing the old catalogue or old Hall shore.  The
new baseline is packet 1173, common 1142, Hall 308 to 20, deficiency 288.
A 1/100 pilot passed before four complete capped shards were launched.

The serial census is:

| stage | count |
|---|---:|
| completion lookups | 383,591,803 |
| completion hits before canonicalization | 37,202,607 |
| distinct canonical primitive triples | 19,142,330 |
| triples changing a geometry incident with the current Hall tail | 12,868,050 |
| triples with positive current-shore kappa | 1,693,259 |
| triples increasing the full common matching | **136** |

The deterministic global winner under the exact score
(common matching, packet matching, -zero-out, -zero-in) changes roots
216, 558, 1348 with option IDs 413152, 1062472, 2568479.  Its hashes are

```text
steps       1aca38dd0ce089b0b01ca5d0822adb6c9b2457470506de3ffaf1188030b8f830
final rows  18527121e80e5d6d2918128e98cb86b79d83e7fb4934db10a460a08e16f038bb
```

Independent replay gives common matching 1143, Hall 306 to 19, deficiency
287, while packet matching stays 1173.  The old 308-root shore expands from
20 to 22 owners, gaining two and losing none.  The exact common-incidence
changes are

```text
+ (210,83)
+ (216,121)
+ (216,695)
- (558,391)
+ (1259,1138)
- (1259,976)
+ (1348,1138)
+ (1348,1169)
```

The dependency halo has 180 roots.  The independent DM audit SHA-256 is
`e156cf8aaf4c02902aac34eb8e24d906c271b586b08421f7cddb44df48fa5d5a`,
and the independent packet/common audit SHA-256 is
`1534e1ff7e57ca3e76c7d2d4e2e0d5a7b31a4135de65b050b0dd18fe98e7bcb2`.
This is a second static attachment-state gain only; all exclusions in Section
6 remain in force.

## 8. Second serial rebase

Regenerating C_ov from `18527121...` starts at packet 1173, common 1143,
Hall 306 to 19, deficiency 287.  The required 1/100 pilot already contained
one strict gain; the subsequent complete four-shard census found:

| stage | count |
|---|---:|
| distinct canonical primitive triples | 19,139,420 |
| current-tail geometry-changing triples | 12,782,490 |
| positive-current-shore triples | 1,658,932 |
| full common-matching gains | **134** |

The deterministic winner changes roots 93, 1251, 1306.  Its steps SHA-256 is
`dadce66fa9fc177099e57d05bf70c547178dc47e59aa327fdc1426ad2fbdf489`
and final-row SHA-256 is
`0c277832fbe429b9c579d6ba2406e90f337e1dc505ac290bdffcd108c7eb07da`.

Independent replay gives packet 1173, common 1144, Hall 305 to 19, deficiency
286.  The old shore expands 19 to 20.  Its exact common-incidence delta is

```text
- (700,403)
+ (1251,1103)
- (1289,1123)
- (1305,1120)
```

The dependency halo has 200 roots.  Independent DM and packet/common audit
hashes are respectively
`61b568f7b5c3af5449389f7926843449527ee078b30b1eec1189fe3d26d2873c`
and
`847f57440393ad94ebc4e43e2843815927a30e71c81ac633a52e3a752d74401c`.
Again this is only a static attachment-state gain.

## 9. Third serial rebase

From `0c277832...`, the baseline is packet 1173, common 1144, Hall 305 to
19, deficiency 286.  The complete regenerated shell has 19,141,418 canonical
triples, 12,740,319 current-tail geometry-changing triples, 1,660,278
positive-current-shore triples, and **128** full common-matching gains.

Two shard winners tied in the complete score.  The deterministic final
tie-break chooses the lexicographically smaller root/option tuple
(353,365,503)/(673724,694980,957726).  Its steps SHA-256 is
`f6fcb9b8b5b11758e63d3822ab9ed6cd9f7dc45424974fbd2557356f9aa8a48e`
and final-row SHA-256 is
`b355192dd85927aaf41767c3eb38ce07a74314a3941c602db960c015b0667700`.

Independent replay gives packet 1173, common 1145, Hall 303 to 18,
deficiency 285.  The old shore expands 19 to 21.  The exact common-incidence
delta is

```text
+ (353,807)
- (365,1247)
+ (421,610)
+ (503,284)
- (949,610)
- (1253,1105)
+ (1299,1088)
```

The dependency halo has 194 roots.  Independent DM and packet/common audit
hashes are
`a93abbfd1bce99225dbcb058037ee849e73479f25df9f0b7f1ae5f9e92e0e629`
and
`afecbc88ba1e8ce6f627400620e14809f99b1e37d2b6292b80008c4d4167c164`.

## 10. Fourth serial rebase

From `b355192d...`, the baseline is packet 1173, common 1145, Hall 303 to
18, deficiency 285.  The complete regenerated shell has 19,118,526 canonical
triples, 12,667,903 current-tail geometry-changing triples, 1,657,577
positive-current-shore triples, and **122** common-matching gains.

The unique packet-preserving shard winner changes roots 449, 563, 1055.  Its
steps SHA-256 is
`962ec03ba064cd5b88b153b1b94ff6033365748cbefcb33c0e23922ae015b885`
and final-row SHA-256 is
`45a0fd760309fdb85382c410e61b543ea7a0cb5c49199b43bd43f6689159888d`.

Independent replay gives packet 1173, common 1146, Hall 301 to 17,
deficiency 284.  The old shore expands 18 to 20.  Exact common-incidence
changes are

```text
- (175,340)
+ (449,265)
- (563,396)
- (705,396)
- (712,405)
- (1045,899)
+ (1055,692)
- (1202,1312)
```

The dependency halo has 184 roots.  Independent DM and packet/common audit
hashes are
`6056280d00e7fbc6e68212a592969bfbc3c13aa8cbc423a35e44b3e7c8aed549`
and
`865b2b58ab253f4b2ccd19c30d7b87be6f9713eb030a79a6c3224909d7835aea`.

## 11. Fifth and final serial rebase

From `45a0fd76...`, the baseline is packet 1173, common 1146, Hall 301 to
17, deficiency 284.  The complete regenerated shell has the following exact
census:

| stage | count |
|---|---:|
| completion lookups | 383,715,044 |
| completion hits before canonicalization | 37,168,732 |
| distinct canonical primitive triples | 19,125,439 |
| current-tail geometry-changing triples | 12,614,461 |
| positive-current-shore triples | 1,677,599 |
| full common-matching gains | **132** |

Two shard winners tied at common 1147 and packet 1173.  They also tied in
packet zero-in count 212.  The declared deterministic common-first score
therefore selects shard 3, whose packet zero-out count is 43 rather than 45.
An independent two-table selector replay has audit SHA-256
`ed33cd9be9b2294f8e47a388accbcbc3a3b7967369f770ea43bb50a5bcd67119`.
It changes roots 1001, 1062, 1202 with option IDs 1906090, 2023934,
2290354.  Its hashes are

```text
steps       cad55f440fd64040ed5d3fa835c375182c4f6546a2db377af4f1e33db4fe6908
final rows  89c9e92e23e1b38f067d32f6e46f8c44d2e51ee27c89b3eeda686cc50988b78a
```

Independent literal replay gives packet 1173, common 1147, Hall 300 to 17,
deficiency 283.  The old shore expands from 17 to 19 owners, gaining two and
losing none.  The exact common-incidence delta is

```text
+ (825,870)
+ (998,638)
- (1001,636)
- (1001,645)
+ (1062,697)
- (1102,1302)
+ (1202,1312)
```

The dependency halo has 198 roots.  Independent DM and packet/common audit
hashes are
`89316f7e04317213cec040efafbeaeae4309061d007d61df33540e1e3fd7e987`
and
`6760c73f537e9f5e714114ba0ed8d7e24560d055c2ad8e389d09d183bb04bb4a`.
The complete round manifest is
`scratch/threadA_k17_45a0_dm_support3_commutator_20260801/aggregate.audit.json`,
SHA-256
`4ba09a4fc564cde58f463f17208cea67ad453302c83f098668e8da88197db92f`.

Across the initial shell and five serial regenerations, the independently
replayed common matching rises from 1141 to 1147 and the deficiency falls
from 289 to 283.  The process stops here because of the agreed five-round
cap, not because the next regenerated shell was searched or proved empty.
There is still no common transversal; all scope exclusions in Section 6
remain in force.
