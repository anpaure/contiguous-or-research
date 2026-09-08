# K17 `2e9194` critical-shore support-three literal verifier

Date: 2026-08-01  
Lane: A / independent finite common-DM audit  
Status: **PASS, exact verifier and dormant-anchor census; no escape candidate claimed**

## 1. Frozen input and scope

The verifier authenticates the exact rooted flag table

```text
scratch/laneK_k17_commonfirst_serial_20260801/
  common_serial03_ae88_seed20260801.final_rows.tsv
SHA256 2e9194935b261dc178daee3aaf47fc9acc1bf1f2af5b6eb31e5004bb4ffd9ceb.
```

It independently reconstructs the complete type/lower-flag resource ledger,
all 12,870 attachment states, every literal nonloop state arc, the common
root--owner both-live graph, an exact maximum matching, and its canonical
alternating Hall/DM regions.  It deliberately does not infer topology,
upper coverage, residence, voltage, an opening, or compiler feasibility.

The frozen replay is

```text
common matching                         1141
canonical Hall shore                 309 -> 20
deficiency                               289
both-live states                         1928
DM minus left/right                   113 / 402
DM core left/right                  1008 / 1008.
```

No full common transversal exists, so no quotient component profile is
defined.

## 2. Accepted circuit certificate

The step schema is

```text
step_id arity slot root_id option_id type C0 C1 C2 delta
```

with tab separators.  A step has arity two or three, uses distinct roots,
and must have exact zero aggregate resource delta relative to the table at
the start of that step.  Roots may recur in later steps.  Consequently the
same verifier covers:

1. one direct support-three circuit; and
2. two or more serial support-two circuits with overlapping root support.

For every literal the verifier regenerates the 1,904-option lexicographic
root menu, checks the global option identifier, reconstructs the exact
resource delta, and rejects a claimed serialized delta that differs.  It
then checks the complete global resource ledger after every step.  If an
expected final table is supplied, all 1,430 final rows must agree literally.

Parallel live attachment states are ORed into one root--owner matching edge;
they are not rejected or counted as parallel matching capacity.

## 3. Dependency-halo and cut theorem

Let `X_0` and `Y_0=N_G(X_0)` be the frozen `309 -> 20` Hall shore.  If a
circuit changes rows `T`, let `H(T)` contain every endpoint of every physical
transition geometry incident with `T`.  Compatibility of a geometry depends
only on its two endpoint rows.  Therefore every common incidence outside
`H(T)` is unchanged.  Incidences at unchanged roots *inside* `H(T)` may
change, because an incoming or outgoing witness can use a changed partner.

The verifier checks this locality assertion literally and then rebuilds

```text
A+ = N_G'(X_0) \ Y_0,
A- = Y_0 \ N_G'(X_0).
```

Thus

```text
|N_G'(X_0)| = 20 + |A+| - |A-|.
```

Any candidate increasing the common matching must pass the exact necessary
filter

```text
|A+| - |A-| >= 1.                                      (3.1)
```

This is stronger and safer than requiring a changed root in `X_0`: a changed
row can alter a tail incidence at another root through the dependency halo.
Condition (3.1) remains only a filter.  Every survivor is scored by a fresh
maximum matching and new canonical Hall shore.

## 4. Exact dormant crossing profile

For every attachment state `(p,o)` with `p in X_0` and `o notin Y_0`, the
baseline census records current nonloop incoming/outgoing witnesses and all
inactive nonloop geometries that could supply a missing side.  Loops are
excluded because they emit no state arcs.  The exact profile is

| dormant profile | states |
|---|---:|
| incoming zero, outgoing positive | 2,198 |
| incoming positive, outgoing zero | 90 |
| both zero | 430 |
| both positive | 0 |
| **total** | **2,718** |

Every missing incoming side has exactly eight raw inactive nonloop witness
geometries.  Every missing outgoing side has exactly 64.  Hence

```text
missing-in sides     2,628, candidate sum 21,024, histogram {8:2628};
missing-out sides      520, candidate sum 33,280, histogram {64:520};
raw-zero candidate sides on either shore                         0.
```

This authenticates the anchor enumerator's raw scope, but it is not an
activation theorem: a geometry still has to satisfy its exact ordered-pair
flag relation while the resource ledger closes.

## 5. Reverse calibration

As a nonidentity regression, two exact reverse binary steps change roots

```text
{52,1090}, {184,1263}
```

and reproduce the authenticated `ae88fc0b...` table literally.  The
dependency halo has 263 roots.  The exact common matching stays 1,141 while
the canonical shore changes from `309 -> 20` to `306 -> 17`.  The old shore
itself remains `309 -> 20`, so the verifier correctly reports no fixed-shore
escape.  The common-edge delta contains changes at roots 856 and 1140 even
though neither row was replaced, directly confirming why root-only pruning
would be unsound.

## 6. Frozen artifacts

```text
scratch/threadA_k17_2e919_dm_support3_verify_exact.cpp
  8793a033d53f82e2d1266d8040b0b534fd1ce3f08a922f07302fbcfc57d13921
scratch/threadA_k17_2e919_dm_support3_verify_baseline.audit.json
  ce0856eb42cd5c214a1a11c412f982311e174b0361a670477cd99ccfb0f47df0
scratch/threadA_k17_2e919_dm_support3_verify_baseline.dormant.tsv
  8facf82d128d2e08469ccb2481ad650dc5a472a4bc45b515bc1097369a91d812
scratch/threadA_k17_2e919_dm_support3_verify_reverse_to_ae88.steps.tsv
  512aa6ab1a03633def64565888713c614fbb3db18fdc6f469dacb1ecb77caa2f
scratch/threadA_k17_2e919_dm_support3_verify_reverse_to_ae88.audit.json
  64f6717c208e1fb9ad4c6ff9211ef86e4b626f924ffad20174c3752bb3eb917c
scratch/threadA_k17_2e919_dm_support3_verify_reverse_to_ae88.ledger.tsv
  9178d6bf3f45aeb1611e983236222828f0aebc2bab10cc47c2f7b58881ccf6a5
scratch/threadA_k17_2e919_dm_support3_verify_reverse_to_ae88.edge_delta.tsv
  77e8c122b785c1e760ffff437c0b5aba50cb1cec3b90e295c1e6f38df102d392
scratch/threadA_k17_2e919_dm_support3_verify_reverse_to_ae88.cut.tsv
  1cf2824141a2d121cae727679546d23f6308b5d7420f45c0ecb6d626a09d9481.
```

The O3 verifier was compiled and run on H100 CPU under a 2 GiB address-space
cap.  The executable hash for the frozen source was

```text
2d7d8400f160de52be48dc94035a032535ff0a5d421231fb987a86add7b2fce8.
```

## 7. Boundary

The resource algebra, old-shore pruning condition, transition locality, and
literal replay are exact.  The dormant profile proves that the frozen shore
has many raw one-sided and two-sided geometric anchors, not that a
ledger-exact support-three circuit activates one.  No support-three escape,
perfect common transversal, chronology, topology, upper row, or compiler is
claimed.
