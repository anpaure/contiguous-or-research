# Frozen j3959 provenance and scoped neighbourhood audit

Date: 2026-07-30

Status: **PASS_PROVENANCE_AND_SCOPED_NOGOS**.  This note authenticates the
current j3959 target, the exact scopes of the standard O4 and direct
service-macro closures, the frozen hard-motif near misses, and the new
5,166-row internal macro atlas.  It makes no claim that a K16 word has been
compiled.

## 1. Literal provenance

Put

```text
P = D^3(answers/k15.word),
S = D^3(scratch/k15_repeatfree_parents_20260730/k15seed_5.word).
```

Let `C` be the frozen carrier3 target and remove from `C`, by value, the set

```text
P[3:5725] union S[3876:4544].
```

Writing the surviving carrier3 rows in their old order as `R`, the target is
exactly

```text
P[3:3959] + S[3876:4544] + reverse(P[3959:5725]) + R.          (1.1)
```

The four half-open output spans are

```text
[0,3956)       P[3:3959]
[3956,4624)    S[3876:4544]
[4624,6390)    reverse(P[3959:5725])
[6390,12873)   R.
```

The removed value set has size 6,390 and `R` has length 6,483.  The three
inter-span joins are

```text
6665--2c6d,   5935--1975,   2e65--6639.
```

The input hashes are

```text
answers/k15.word                                           f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b
scratch/k15_repeatfree_parents_20260730/k15seed_5.word       4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6
carrier3 target                                             6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0
j3959 target                                                edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee
```

A 12,873-row literal origin table, including the source class and source
index of every row, is frozen at

```text
scratch/threadD_k16_j3959_frozen_audit_20260730/origin_map.tsv
SHA-256 c8f42ba7c2626ce410acd414bc9f3ed25c6de08f48bdd9940dabca8d1e683274.
```

## 2. Exact gates of the frozen target

The target has 12,870 distinct masks and repeat excess three.  Its only
repeated masks are the adjacent pairs

```text
4e71 at 6433,6434;
cc63 at 12869,12870;
ce61 at 12871,12872.
```

Consequently its flats are `6433,12869,12871`, its depth ledger is the
required `3,2,1,0` ledger, and its scalar capacity is 32,176.  Direct replay
of the maximal-envelope construction gives no empty envelope and reconstructs
every one of the 12,873 target rows exactly.

The arbitrary-width accumulated-union oracle has exactly five holes:

```text
4e79 (rank 9),  6f79 (rank 11),
ca79 (rank 9),  ea79 (rank 10),  eb79 (rank 11).              (2.1)
```

Thus they are the two nested chains `4e79 < 6f79` and
`ca79 < ea79 < eb79`.

The exact generalized lower Hall graph has

```text
left targets       26,332
right cells        32,176
incidences        347,797
maximum matching   26,329
deficiency              3.
```

Its canonical deficient shore is 9 versus 6:

```text
L = {0665,066d,0675,06e5,0765,1665,2665,8000,8665},
N(L) = cell IDs {803,2939,4349,9215,19070,27225}.
```

The displayed unmatched targets are `1665,2665,8000`.  The exact Hall audit
is

```text
scratch/threadA_k16_rf_halo_j3959_buffer_20260730/j3959.hall.audit.json
SHA-256 2b7e8e6b7474f367c2e930cb03365044532c65df037f19a8a056218be437f091.
```

## 3. Standard O4 closure

The standard four-cut census enumerates all 25 provenance-irreducible signed
block patterns in the pinned two-chain neighbourhood.  After exact
deduplication it has 28,429 candidate representations.  The gate ledger is

```text
G0 plus scalar capacity        22,439
exact maximal-envelope replay       0
upper complete                      0.
```

This is an exact failure before upper or Hall scoring.  It does not cover
nonstandard collars, substitutions, duplication/deletion, compound motif
braids, or moves with at least five cuts.

```text
result  scratch/k16_rf_halo_j3959_standard_o4_nogo_20260730/o4.full.json
        SHA-256 b5d71ba23844076568bc685f23219959fc1bee7008b950a72b7e687ff60dbc4d
source  scratch/k16_rf_halo_j3959_standard_o4_nogo_20260730/search.cpp
        SHA-256 d35f5ae07ff0e47f74d15b0e02afb063b8ee6590a5da35987b78669e7de5f5ab.
```

## 4. The direct 18,308-row X by Y macro is contained in a frozen no-go

The direct macro chooses

* one of 330 private-top masks `X`;
* one of 56 rank-eight children `Y` with `6879 | Y = 6f79`;
* the fixed moved block order `4a79,4e39,4d39`.

After source uniqueness and collision exclusions there are exactly 18,308
`(X,Y)` pairs.  Independently, the two definitions of the X domain agree:
the original private-cell test is equivalent on this source to
`X & 0071 = 0071`.

The frozen compound run contains those 18,308 rows as one of all six orders
of `4a79,4e39,4d39`.  It therefore contains `6*18,308=109,848` rows.  Every
row passes the flat and scalar-capacity gates, but none has exact maximal
envelope replay:

```text
generated 109,848; flat 109,848; capacity 109,848;
exact 0; upper complete 0.
```

Hence the direct 18,308-row order is structurally dead without relying on an
unfrozen direct stdout.  The original compact certificate is

```text
scratch/k16_rf_halo_j3959_standard_o4_nogo_20260730/compound_all_orders.audit.json
SHA-256 aca4ba8f68a42269be99401648716fa6ef3cdc7f2f71ce393bd991fd91b753bf,
source SHA bec730de42a6c60d41c20b64917499935b23f5bbdacc9273bbd1698aed93dbea,
H100 binary SHA e9b6229f3f78302f8e687e54742513092204b81a78041603f17d54296a928e.
```

An enriched full-row replay additionally proves the minimum structural error
total is 12 (zero empty cells and 12 bad reconstructed rows):

```text
remote /home/amodo/or15/work/two_parent_k16_compound_service_20260730
source SHA 31e92886856195c5a598359ed68de962e1796639c16629c7243138d177919a69
binary SHA 54bee74438e3892a1f63b13c3703bc9a703b5ef2d711cfd0b6e05949873b9019
stdout SHA 6c19d575360dc58e3eaf45ed34bf2f375eab204223ef044e5722ce0bbd13287a
summary SHA 15facb561424bbd131df13f9de3e72f2f6641a8f2e5049bab2c2356bc7d93da0.
```

No resource/time log was frozen.  The binary and output mtimes give only a
20.486-second wall-time envelope, not an audited CPU-time or RSS claim.

## 5. Frozen hard-motif `s2/u2` near misses

The second hard-motif run is reproducibly frozen.  It enumerated 21,120
connected path ledgers and both orientations, for 42,240 audited target
orders.  It found no exact upper-complete carrier.  Its best profile has
capacity deficit zero, structural error count two, and two upper holes.

```text
remote /home/amodo/or15/work/two_parent_k16_3opt_comp3_20260730/j3959_hardmotif
source SHA 25c55daf4d21e199391e574bc10f6e66a3ec6631b0329f3b0cff7af80146c634
binary SHA 3a67a953553f3dd3c5098a5c938867d2e13e120059ee1e4688b91a59cbcc9fd0
summary2 SHA 277bb5330d35fae019608cf4d946febaa0886c2cb03e829527b689318e16b4a0
stderr2 SHA 14903c09e6ade38a4219b4a3d17a4e5f6d6645beb67ca18e12d9a4248592cfc7.
```

The two retained top `s2/u2` examples have hashes

```text
6b29f293f37b930859015e84b25178d1604a8cd3d80022105aae37f13f720af0
0c5d408e98f0e360a4f766418ab065ab6d8ab7703a7a072ba37d2f86b6c93821.
```

They are near misses, not valid carriers.  No resource log was frozen; the
binary-to-summary mtime envelope is 179.897 seconds.

## 6. Exact 5,166-block internal census

Consider ordered blocks

```text
(V0,V1,V2,4a79,4e39,4d39).                                  (6.1)
```

The complete raw domains used by the theorem are:

```text
V2: rank-8 subsets of ca79, V2 != 4a79, V2|4a79=ca79       (8)
V1: rank-8 subsets of ea79 using a bit of ea79\ca79        (36)
V0: rank-8 subsets of eb79 using a bit of eb79\ea79       (120).
```

Thus the raw product contains exactly `8*36*120=34,560` blocks.  For each
block the audit requires every one-run wholly internal to the block to have
length at least three.  This is precisely internal depth-two residence;
runs meeting either block boundary are deliberately deferred to the seam
test.  Exactly 5,166 blocks survive.

Every survivor satisfies

```text
V2 | 4a79             = ca79,
V1 | V2 | 4a79        = ea79,
V0 | V1 | V2 | 4a79   = eb79,
4a79 | 4e39           = 4e79,
```

and retains the final provider edge `4e39--4d39`.  The canonical block

```text
eb60,ea61,ca71,4a79,4e39,4d39
```

is among the survivors.

Clipping per-bit prefix and suffix run lengths at three gives 4,866 distinct
endpoint signatures: 4,566 signatures occur once and 300 occur twice.  This
is the provenance-reduced boundary state space for the next buffered search.

```text
audit  scratch/k16_j3959_alternative_upper_service_blocks_20260730.audit.json
       SHA-256 2f1b37317f7ad99271a459647aea58fdd41d863efa23f8f315336c08ffefb101
       payload a736c39b447d4fd9bbcaf77d7a8058ae3157bf6fad7f75107db159796378d4f3
source scratch/audit_k16_j3959_alternative_upper_service_blocks_20260730.py
       SHA-256 b355269642f50a45fecfb9a52a00bca3b7ef78c9ee44ec8378bd1da9c685244b.
```

The completeness claim is exactly the fixed ordered form (6.1), the displayed
raw domains, and internal depth-two residence.  It does **not** certify
boundary residence, source-mask uniqueness after placement, the `6f79`
service, the private top singleton, global G0/maximal-envelope geometry, or
Hall feasibility.

## 7. Independent replay package

The compact independent replay and its generated audit are

```text
scratch/audit_threadD_k16_j3959_frozen_provenance_20260730.py
  SHA-256 70db1ea74e20ef15a11f1bdfc5b43c881ff28e5f10ee2f35e8127ccf75eeb6f6
scratch/threadD_k16_j3959_frozen_audit_20260730/provenance.audit.json
  SHA-256 55ce21fbaaf36dd51aad778a93421ca84e85755543362ac06d245920ca81215f
  payload 74fa6a5e98468ffb14caf29a8b84ce6bb8f8325fbbb3f286141bff9003b66ad3.
```

The surviving search direction is therefore a provenance-reduced placement
of the 4,866 boundary signatures with explicit buffer rows.  The hard gates,
in order, are source uniqueness and boundary residence, G0, exact maximal
envelope replay, all five upper masks, and finally the exact Hall graph.
