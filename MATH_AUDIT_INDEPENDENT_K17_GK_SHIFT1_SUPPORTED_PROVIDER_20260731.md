# Independent audit of the K17 adjacent-cut supported-provider theorem

Date: 2026-07-31  
Status: **GO** for the shift-one post-fixed support graph and its `8736/8736`
provider matching. **NO** for interpreting the displayed matching itself as a
wedge-consistent path cover. A joint capacitated matching remains open.

## 1. Seed reconstruction

I reconstructed the cyclic Greene--Kleitman seed from the last-maximum
pivots at cuts zero and one. It is a matching forest:

```text
rank-six edge colours       3640
rank-seven vertices         7280
components                  3640
endpoints                   7280
internal turns                 0
unused rank-seven vertices 12168
missing rank-six colours    8736
```

Every component consists of one old edge. The completion ledger is therefore

```text
target vertices             16911
inserted unused vertices     9631
component joins              3639
target edges                16910
new edges                   13270
missing-colour new edges     8736
repeat/decorated new edges   4534
```

## 2. Independent supported-edge reconstruction

Without reading the producer's active edge set, I enumerated every fresh
Johnson edge between an old endpoint and/or unused rank-seven vertex. The
raw local conditions are:

* its rank-eight union is not an old edge colour;
* an old-endpoint boundary turn has rank nine and is not an old turn;
* an endpoint--endpoint edge does not close one old component; and
* its two boundary turns, when both exist, are different.

This gives 458,934 raw edges, split by the number of unused ends as

```text
EE  20655
EU 147102
UU 291177.
```

I then computed the greatest edge/wedge post-fixed point. An edge survives at
an unused end only if another surviving incident edge forms a legal wedge
there. The deletion rounds are exactly

```text
4004, 0.
```

The post-fixed graph has

```text
active edges    454930
active wedges 20772564
EE               20655
EU              146530
UU              287745.
```

A final literal pass found zero unsupported sides among active edges. The
canonical active-edge tuple hash is

```text
613bd12f621bd3d8a3c387e149e5ae2302d15f87f19bf7b3f37f4fb07f75eaf0
```

## 3. Provider Hall theorem

For every missing rank-six colour `D`, each active edge with intersection
`D` supplies its fresh rank-eight union `Q`. Because `D subset Q` and their
ranks differ by two, the physical Johnson edge is uniquely determined by
the pair `(D,Q)`.

The independently reconstructed provider graph has

```text
left colours       8736
right q8 values   13817
incidences       272992
zero rows             0
matching rank       8736.
```

Thus the shift-one provider graph has a perfect matching. My independently
run Hopcroft--Karp algorithm reproduced the producer's exact pair stream;
both have hash

```text
faaa1c8dc294fe5462ef00f03129f4dca65fd3a04acc822c61261021140283f0
```

The independent compact certificate is
`scratch/independent_k17_gk_shift1_provider_matching_20260731.tsv`.

By cyclic reflection, shift 16 is isomorphic to shift one. The stronger claim
that these are the only full-rank shifts belongs to the H2 all-shift scan; this
audit independently reconstructs shift one only.

## 4. Why Hall is not yet an ear packing

I materialized the unique physical edge for every pair in the perfect
matching and counted its loads. The selected edges have types

```text
EE 1203, EU 2597, UU 4936.
```

Their selected-vertex degree profile is

```text
old endpoint: degree 1 = 3417, degree 2 = 730, degree 3 = 42
unused:       degree 1 = 3281, degree 2 = 3806,
              degree 3 =  492, degree 4 = 25.
```

A final path can use at most one new edge at an old endpoint and at most two
at an unused vertex. Therefore this explicit matching already has

```text
772 overloaded old endpoints,
517 overloaded unused vertices.
```

Even among the 3,806 unused vertices of selected degree two, 233 selected
edge pairs do not form a legal wedge. Among the presently forced valid
boundary and central turns, there are a further 1,191 repeated rank-nine
values.

Consequently the displayed Hall matching is **not** itself a partial
wedge-consistent path cover. This does not refute the shift-one architecture:
the provider graph contains many perfect matchings, and the extra 4,534 edges
can also alter degrees and wedges. It proves only that the next solve must
choose colour providers, vertex capacities, wedge partners, rank-nine values,
and topology jointly.

## 5. Scope

Proved here:

* the exact adjacent-cut seed census;
* raw provider-edge validity;
* the greatest post-fixed support graph;
* a perfect missing-rank6/fresh-rank8 provider matching; and
* the failure of the frozen perfect matching as a physical path cover.

Still open:

* whether another perfect provider matching satisfies the vertex caps;
* a simultaneous wedge selection;
* all 13,270 new edges and the 4,534 repeated/decorated occurrences;
* global rank-nine injectivity;
* the component Hamilton path;
* the prefix and upper continuation; and
* a length-24,313 universal word.

## 6. Artifacts

* `scratch/audit_independent_k17_gk_shift1_supported_provider_20260731.py`
* `scratch/independent_k17_gk_shift1_supported_provider_20260731.audit.json`
* `scratch/independent_k17_gk_shift1_provider_matching_20260731.tsv`

The canonical audit payload hash is

```text
0ff2b7e0128c7757eac05d0ca5108e10bb800d8823c0785601acf2e40468e067
```
