# Independent audit: K17 greedy296 v2 exchange catalogue and generic evaluator

Date: 2026-07-31  
Lane: H3, independent audit for AD  
Verdict: **PASS after one genericity correction**

The corrected evaluator exactly replays both the original v1 checkpoint and
the greedy296 v2 checkpoint.  This note proves no nonempty repair selection,
compiler, common-cap matching, or K17 word.

## 1. Frozen source and artifacts

```text
scratch/evaluate_ad_k17_opt28_marked_exchange_20260731.cpp
SHA-256 037ad2f0a4ec332b7ccbfdfba05730a10f1ed1f86091905f45a3c8bef35cbc60

scratch/build_ad_k17_opt28_greedy296_exchange_catalogue_20260731.py
SHA-256 7fc96197f4254a635bc37b39c8b0d471173ac62d478527aa3fd7deb875ba44d5

scratch/ad_k17_opt28_greedy296_marked_exchange_seed_20260731.bin
SHA-256 73fa8c68bc4534866fa9acef378256e407ef3225c7f5ebddda8a04be86600147

scratch/ad_k17_opt28_greedy296_marked_exchange_catalogue_20260731.bin
SHA-256 7bb6ea4b1aae117c0f6b986b1c2892a24983d38fea57b511fe9635d285ab97ed

scratch/ad_k17_opt28_greedy296_marked_exchange_rank10holes_20260731.bin
SHA-256 8c35a600cf5f165b7da58cf090138a3461d1bc68077c32acb237df4fb74c6c82

scratch/ad_k17_opt28_greedy296_marked_exchange_catalogue_20260731.meta.json
SHA-256 aeb9aa3459978a3ce07e271dc32739346137113c0a254388a640c71defbad6f0

scratch/ad_k17_opt28_greedy296_marked_exchange_incumbent_20260731.eval.json
SHA-256 1477402454205f288226fa23bbc6792c0aecd5f19f25f27f01b0e62f4d9404e8
```

The corrected residual and owner carrier are

```text
scratch/k17_opt28_occurrence_greedy296_connected_bflow_v2_20260731.json
SHA-256 63b49db80ad983bcd440aba3ac4b449888e30dea2d3c83e140e15b07082f69d0

scratch/k17_opt28_occurrence_greedy296_connected_full_20260731.owner_cycle.word
SHA-256 801896cd15cc6b0b202db75421b93c1dc0e13a33b67fbc902ce283e242c381a6
```

Independent verifier and result:

```text
scratch/audit_h3_ad_k17_greedy296_v2_exchange_catalogue_20260731.py
SHA-256 44c9498b7c861084f2a805fed584732bd8d107a098f066f9c1fed12a3099b241

scratch/h3_ad_k17_greedy296_v2_exchange_catalogue_20260731.audit.json
SHA-256 7b8dc91614cd8b8def51f10747f1937e75f261e49a43a69b6b986ad8225ef24f
payload d8c5d7316fb48d0b399176058c149419c5e9903e5abe213d0ddfd30f5f589346
```

## 2. Correction found during audit

The first generic/v2 evaluator presented for audit still contained the v1
literal

```cpp
selected.size() < 218
```

in its one-gain-per-service-row assertion.  For a v2 seed the service bank
has `1908` rows.  This was a redundant weak assertion rather than a false
positive in the reported coverage or compiler guard: a selected edge has one
rank-ten union, and the evaluator separately computes the exact covered-row
set.  Nevertheless, it was not generic fail-closed code.

The frozen source replaces it by

```cpp
selected.size() < static_targets.size()
```

and uses generic diagnostic wording.  Thus the asserted floor is `218` for
v1 and `1908` for this v2 seed.

During the final freeze, the old “536-byte seed” header comment and
`SEED536.bin` usage label were also replaced by version-generic wording.  This
second correction was cosmetic; the parser already checked both version-one
and version-two lengths exactly.

## 3. Corrected b-flow provenance

I independently authenticated the greedy296 occurrence flow:

```text
scratch/k17_opt28_occurrence_greedy296_verified_20260731.flow.json
SHA-256 079f5cd96f713ef2d72dd43acff10f84416acdb670aeff96f61a3cb97f29c25f
```

The original residual sidecar has SHA
`c32349f7f962d69b23191e26b0f86aea1afab1d14fdfaf9ceb5ac25b626050e7`
and contains the known stale pre-finalization flow-file pin.  The v2 residual
changes that provenance pin to the exact current flow SHA.  Its `4872`
assignment rows and their authenticated payload

```text
327d60f1f1d072b3bcb60e84404e52f346e25a98499fcf688fde842cddf67a8c
```

are exactly unchanged.

I then checked the rows semantically rather than relying on the corrected
hash:

* the `133` packet U owners and `4872` residual U owners partition all `5005`
  old rank-nine U owners;
* each residual pair consists of two distinct rank-eight facets contained in
  its stated U owner;
* the `1430` macro edges plus the `133` packet edges leave total port demand
  `9744`;
* the residual rows fill that demand coordinate-for-coordinate; and
* all macro and U edges form a connected degree-two graph on the `6435` old
  rank-eight ports.

Thus the v2 sidecar has both correct byte provenance and correct physical
b-flow semantics.  The independently generated H2 carrier order is exactly
the same parsed `24310`-owner order as the root materialization.

## 4. Version-two seed trailer

The v2 seed is exactly `3956` bytes:

```text
100-byte common header
1908 little-endian uint16 rank-ten target IDs
10 little-endian uint32 expectation fields
```

Its carrier SHA is exact.  The SHA stored at header bytes `68..99` equals the
SHA of every byte after the header, so it authenticates both the IDs and the
trailer.  The trailer decodes exactly to

```text
service references       66606
support min / max         10 / 45
D2 bad                    1875
D3 bad                    1874
empty envelopes              0
replay mismatches         2769
rank-10 holes             1908
rank-11 holes              929
rank-12 holes              149
```

The `1908` IDs decode to the independently recomputed sorted rank-ten hole
set, not merely to a list of the right length.

## 5. Complete record replay

I independently reconstructed the marked owner set from the greedy296 flow,
the fixed packet, and the `28` optional components.  It is a single
`4108`-owner cyclic interval at rotation `21331`.  The complement contains
`20202` owners and `20201` internal incumbent lower-colour edges.

Without importing the producer, the verifier regenerated columns in the
canonical order “lower colour, then numerically sorted unordered endpoint
pair, omitting the incumbent pair.”  It compared all cached records:

```text
colour groups                     20201
off-source columns               545721
rank-ten service rows              1908
service column references         66606
service support min / max         10 / 45
```

Every group record, every column record, every service offset, and every one
of the `66606` service column IDs agrees.  The complement-superset profile is

```text
supersets       3    4    5     6     7     8     9
colours        15  129  454  1601  3836  6748  7418.
```

The independently reconstructed textual column-stream SHA agrees with the
meta file.  Therefore the large binary and the compact v2 seed describe one
canonical catalogue, not merely equal-sized catalogues.

## 6. Literal baseline and compiler fields

The literal row is again

```text
4108 marked rank-nine owner cells
20203 rank-eight facet cells, including both cross-bank facets.
```

The independent replay gives

```text
D2 bad                       1875 = 849 length one + 1026 length two
D3 bad                       1874 = 848 length two + 1026 length three
empty maximal envelopes        0
replay mismatches            2769
replay missing bits          2901
envelope volume            150843
minimum envelope size           6
host redundancy            256785
rank-10/11/12 holes      1908/929/149
interval extensions          134848
```

The independently computed little-endian hashes are

```text
owner order f63d6810a4ee4210a9305e6e326e0def8ec868bc41de0fc43625f5c8931fb093
Z row       447a3fec0eea19e55b45d9b142d48d6e232ebda8f2cfb155999f8720a81fc170
```

They match the evaluator output.

The empty-checkpoint compiler guard is also arithmetically and logically
consistent:

```text
inversion_ready                         false
ranks10_12_complete                     false
pre_common_cap_gate_pass                false
scalar_available_cells                   7401
fixed_marked_cells                        4108
scalar_slack                              3293
upper_hole_demands           1908+929+149 = 2986
scalar_margin_after_upper_demands          307
common_cap_matching                    UNSOLVED
```

`inversion_ready` requires zero strict D2 defects, no empty envelope, and
exact replay including zero missing bits.  An exact D2 representation already
forces the associated D3 residence condition, so omitting a separate D3 term
from that Boolean is sound.  `ranks10_12_complete` is the exact conjunction
of the three zero-hole counts.  Their conjunction is correctly called only a
**pre**-common-cap gate.

The scalar subtraction is a necessary-budget diagnostic, not a matching or
chronology theorem.  Its positive value `307` must not be read as common-cap
feasibility.

## 7. Generic evaluator regression

I recompiled the frozen source with

```text
clang++ -std=c++20 -O2 -Wall -Wextra -Wpedantic
```

with no warnings.  The local executable SHA was
`176c482f7d29586aa62517db4ee0c838bc1e4357ef57eba9e74d7aefd6a3aa0b`.
It reproduced both frozen empty evaluations byte-for-byte:

```text
v1 checkpoint   3cc3740c6ccb18ddd2b0578926618eca49d23339486e242222f0067320396b18
v2 greedy296    1477402454205f288226fa23bbc6792c0aecd5f19f25f27f01b0e62f4d9404e8
```

Hence the final parser/evaluator is genuinely dual-version in behavior, not
only in its seed parser.

## 8. Exact boundary

This audit establishes only that the catalogue, v2 expectations, physical
b-flow provenance, and evaluator are exact in their stated scope.  It does
not establish a nonempty balanced exchange selection.

Further caveats:

1. The v2 seed must itself be authenticated; its internal payload SHA does
   not authenticate its 100-byte header.
2. The evaluator scans upper ranks ten through twelve.  The authenticated
   greedy296 Z row still has two rank-thirteen holes, which remain outside
   the compiler guard.
3. The current row is far from exact inversion and residence.
4. Common-cap matching remains entirely unsolved.

Subject to these explicit boundaries, I found no remaining v2 trailer,
provenance, record-order, service-index, JSON, run, envelope, upper-scan, or
compiler-guard defect.
