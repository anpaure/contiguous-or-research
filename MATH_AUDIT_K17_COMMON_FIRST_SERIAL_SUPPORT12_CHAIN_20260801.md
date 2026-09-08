# K17 common-first serial support-at-most-two recataloguing

Date: 2026-08-01  
Status: **PASS, exact certificate chain; heuristic plateau only**

## 1. Statement and scope

For a rooted-flag table `F` on the 1,430 quotient roots, let `G_F` be the
bipartite graph from roots to quotient owners in which `r--o` is present
exactly when the aligned attachment state `(r,o)` has at least one literal
incoming and one literal outgoing state transition after rebuilding the full
transition geometry of `F`.  Write

```text
mu(F) = maximum matching size of G_F.
```

This is the **common root--owner both-live relaxation**.  It is stronger than
the separate packet and owner projections and is necessary for a common
root/owner/state cycle cover.  It is not sufficient: even `mu(F)=1430` would
still leave the induced transition selection, components, voltage, upper
rows, opening, residence, and compiler to check.

Starting from the authenticated packet-first round-two table

```text
560d8d86a7728d1b1e6497c00547aafbcc75c8b5e2b52e9f7ff60144bdfe85fe,
```

four nontrivial serial rounds regenerated the complete seed-relative unary
and binary resource-circuit catalogue and selected a root-disjoint packet
with the lexicographic primary objective `mu(F)`.  A fifth catalogue rebuild
at the resulting table accepted no circuit.  Every selected packet was
applied literally and the terminal table was independently rebuilt.  The
exact common chain is

```text
936 -> 1099 -> 1132 -> 1141 -> 1141.
```

The last arrow improves only the secondary packet score.  Therefore the
authenticated conclusion is a common-primary **heuristic plateau at 1141**,
not a support-two ceiling, an UNSAT result, or an optimality theorem.

The terminal rebuild is relative to `2e9194...` itself.  It contains 2,547
unary and 215,299 binary circuits and, in the declared deterministic strict
sweep, accepts zero moves: the table remains byte-identical.  This is the
fixed point of that stated selector/order, not of the full circuit-packing
polytope.

## 2. Exact serial ledger

The pair `|X| -> |N(X)|` is the canonical alternating Hall shore obtained
from all unmatched roots.  In every row

```text
|X|-|N(X)| = 1430-mu(F).
```

| table | source catalogue `(unary,binary)` | selected `U+B` / roots | common `mu` | Hall shore | deficiency | packet `M / zero-out / zero-in` |
|---|---:|---:|---:|---:|---:|---:|
| `560d8d` | -- | -- | 936 | `652 -> 158` | 494 | `1178 / 103 / 235` |
| `4e7a5f` | `2545,214803` | `23+145 / 313` | 1099 | `365 -> 34` | 331 | `1156 / 56 / 237` |
| `4213de` | `2543,215262` | `7+62 / 131` | 1132 | `319 -> 21` | 298 | `1166 / 49 / 217` |
| `ae88fc` | `2548,215605` | `5+19 / 43` | 1141 | `306 -> 17` | 289 | `1171 / 42 / 216` |
| `2e9194` | `2545,215304` | `0+2 / 4` | 1141 | `309 -> 20` | 289 | `1172 / 42 / 215` |
| terminal rebuild | `2547,215299` | `0+0 / 0` | 1141 | `309 -> 20` | 289 | `1172 / 42 / 215` |

Thus common-first repricing materially differs from packet-first repricing.
The first common jump `936 -> 1099` sacrifices packet matching
`1178 -> 1156`, while the common-primary plateau packet recovers one packet
matching unit without changing the common deficiency.

The terminal Hall shore is literal, not inferred from its cardinality.  Its
root and owner ID lists have hashes

```text
tail (309): b4b53adeec2bee28d4940cf15d61ab9be14b3322c248dcdfffb7da8daf07c829
head  (20): b0a829233d98df7b6a48a77f9778ad95f32fedec372d75930cf8b7f63932c6bd.
```

The terminal table has 1,928 both-live attachment states, 271 roots with no
eligible owner, state dead-out/dead-in `1143/10787`, and owner
dead-out/dead-in `0/191`.  No full common transversal exists, so a quotient
component profile is undefined rather than merely uncomputed.

## 3. Literal replay theorem

Each round passes three independent layers.

1. The selector output binds the source, complete relative catalogue,
   selected circuits, and final rows by SHA-256.  A unary circuit has zero
   resource delta; a binary circuit has opposite nonzero deltas on two
   distinct roots.  Selected supports are pairwise root-disjoint.
2. The clean-room C++ verifier re-enumerates literal options at every changed
   root, re-derives resource signatures, applies the circuit packet, obtains
   the final table byte-for-byte, checks all type/lower-palette ledgers, and
   reconstructs every packet and labelled-state transition.  It consumes no
   selector catalogue, cached transition delta, or claimed score.
3. A separate direct-row decoder and a separate common-DM program rebuild
   liveness, run Hopcroft--Karp, and derive the alternating Hall shore.

For the terminal arrow `ae88fc -> 2e9194`, the clean-room verifier reports

```text
PASS_K17_DISJOINT_SUPPORT2_SELECTOR_INDEPENDENT
circuits=2 roots=4 matching=1171->1172
zero_out=42->42 zero_in=216->215,
```

and the independent DM replay reports

```text
PASS_K17_COMMON_ROOT_OWNER_LIVE_TRANSVERSAL_DM 1141 309 20.
```

Consequently the unchanged common score and changed Hall shore belong to the
fully materialized final table; neither is an additive move-delta estimate.

## 4. Hash ledger

The serial final-row chain is

```text
560d8d86a7728d1b1e6497c00547aafbcc75c8b5e2b52e9f7ff60144bdfe85fe
4e7a5fa38a661feea83dcc7bb9179e9194130b13a3fad3e810f169ce3e225402
4213de9d9edc881949b89e7bc0a65de8fe3446dd6e708c5cabe9001609490686
ae88fc0b489a5b436ca3c2fe10462d80a18aed6cec8e03df871d5abe96561beb
2e9194935b261dc178daee3aaf47fc9acc1bf1f2af5b6eb31e5004bb4ffd9ceb.
```

Per-round catalogue / selected-packet hashes are

| final | catalogue | selected packet |
|---|---|---|
| `4e7a5f` | `fcf4a215b18489529a3f30c96ac6edd7071b484a3bd562402834f5b9d1eb0249` | `9207c840ad2bebb4214df184a037563ec745592348716bc6b1b3cccdc5299819` |
| `4213de` | `2871d0856afa93f0e513cc2e4ddb7ef65c1f41b5ad5a825a4f29aeee440e5bea` | `bc38a9a18bfb9b1ecfa800e38f2dce225f99578e33fe2c77b7e7b4a93a145eb0` |
| `ae88fc` | `21bb05041ec10134affe2bf3768c8d6f2da9c618f1038ecb6d1b6f780f1396ab` | `bf5f2ad6d1d72d2a4dfe29b31def98396ab707d1ec3d923019b71171466ca827` |
| `2e9194` | `28ee08bdcac1f654694aca842288dccf74a9f6dcb67b676119a71713a229ce8b` | `e84314fd3605545b1c69213657a4b4d2a6423d9d6509db6c69afefb2a8a8ae8a` |

The terminal selector manifest, clean-room selector audit, direct-row audit,
and common-DM audit have file hashes

```text
8f2e57271a2102cf0818d6e5f38bd4465e87d5dbb0ae1930ed52901352a452c3
3e30ef7f5b05ffba7d7652b99d1be79d275c8fd7aa81f50d10c741c361df31e9
afc0ef1a169ffe0a263f3132009c28dd034d680b82ed164abcacbe7d06bbca27
ff3c6b16c8198ab9b7fc1c6b3145bf12e03d6b345d9877fe94c43ebb0d4da76d.
```

The no-move terminal rebuild is bound by

```text
scratch/laneK_k17_commonfirst_serial_20260801/
  common_serial04_2e91_seed20260805.audit.json
    f3a6698bacee48d8d64a9d7915f40373d88c0b87b8ae779cd3e6d4539b56bdea
  common_serial04_2e91_seed20260805.catalogue.tsv
    100a6bfb90b2a40728a494158c65023fda4c06d60f7b899e71ac0eb7e2bd1860.
```

The engine and clean-room verifier are bound by

```text
scratch/search_k17_disjoint_support2_exact_lns_20260801.cpp
  97e63e66ebeb0f6426aced56ec158699e99a8bdd6a4de61b1d8603e2856fde45
scratch/verify_k17_disjoint_support2_selector_20260801.cpp
  0d0f68bc3524579b940f8797a7dacc2dd531d7417f132c92ffbf09ee906e7d23.
```

All frozen common-first artifacts are under

```text
scratch/laneK_k17_commonfirst_serial_20260801/.
```

## 5. Packet-first control and exact boundary

The independently frozen packet-first control reaches packet matching 1,223
and then a declared deterministic fixed point, but its terminal common
matching is only 981 with Hall shore `637 -> 188` and deficiency 449.  The
common-first branch instead reaches common matching 1,141 and deficiency 289
while its terminal packet matching is 1,172.  This exact Pareto separation is
why packet projection scores cannot stand in for the common root--owner
transversal.

What is proved:

- every displayed table is an exact static lower-palette factor;
- every displayed arrow is a literal, root-disjoint support-at-most-two
  circuit packet relative to its actual source;
- every packet, common matching, and Hall shore is independently rebuilt;
- the declared common-first strict-sweep run accepts no common-improving
  circuit after reaching `ae88fc`; its accepted secondary packet reaches
  `2e9194` without lowering deficiency, and a complete fresh recatalogue at
  `2e9194` then accepts no circuit at all.

What is not proved:

- optimality over disjoint packets, jointly nonimproving circuits, other
  orders/random seeds, overlapping serial moves, or support at least three;
- a full common root-owner-state transversal or any quotient component
  profile;
- upper-shadow, topology, voltage, opening, residence, or compiler
  feasibility.

The sharp next finite object is therefore the terminal Hall shore itself:
price a newly regenerated circuit or circuit packet by exact gain outside
its 20-owner neighbourhood (net of lost old neighbours), then replay the
whole table.  The present `289` deficiency is an authenticated target, not a
claimed minimum.
