# K17 serial rooted-flag recataloguing chain: fail-closed theorem audit

Date: 2026-08-01  
Status: **PASS**, with no numerical, hash-continuity, resource-ledger, replay,
packet-metric, or common-live Hall-witness mismatch in 13 accepted
transitions, plus one authenticated packet-first empty terminal pass.

## 1. Scope and theorem

Let a rooted-flag certificate assign one literal ordered three-age partition
to each of the 1,430 canonical rank-eight roots.  The exact static resource
signature consists of its type row, its canonical `C0` orbit when
`|C0| >= 2`, and its canonical `C0 union C1` orbit.  A unary recataloguing
circuit has zero resource delta.  A binary circuit changes two distinct roots
with opposite nonzero resource deltas.

**Authenticated serial-chain theorem.**  Each edge in

```text
d44b6061 -> e28a8ee5 -> 44971315 -> 560d8d86
                                      |  |  \
                     packet-first    |  |   \ common-first
                                      v  v    v
                               68d439c6 fe45c235 4e7a5fa3
                                   |                 |
                              6c0ed7db          4213de9d
                                   |                 |
                              452a332d          ae88fc0b
                                   |                 |
                              d32ed635          2e919493
                                   |
                              3e7af637 -> empty pass
```

is a root-disjoint packet of literal support-at-most-two circuits relative to
the displayed source certificate.  For every edge, the clean-room verifier:

1. binds the actual source, manifest, selected-packet, and final-row hashes;
2. recomputes option IDs and exact resource signatures from literal rows;
3. applies the packet to the authenticated source and obtains the supplied
   final table byte-for-byte;
4. rechecks the exact type and lower-target resource ledger; and
5. rebuilds the complete literal packet/state transition geometry from the
   reconstructed rows.

Consequently none of the packet scores below is inferred by adding isolated
or cached move deltas.  Each packet matching, degree census, state census, and
common both-live Hall witness belongs to the fully reconstructed final table.

This is a certificate theorem, not an optimization theorem.  It does not say
that any greedy packet is globally optimal.

## 2. Authenticated nodes and seed-relative catalogues

The support-two column counts indecomposable distinct-root binary circuits;
it does not include arbitrary pairs of unary circuits.

| node | full certificate SHA-256 | support 1 | support 2 | support-1 roots | support-2 root pairs |
|---|---|---:|---:|---:|---:|
| `d44b` | `d44b60611a3c9e4ba1533a774762fce825d327dcc7536cdcd9c10522404b1ad3` | 2,541 | 213,714 | 478 | 26,941 |
| `e28a8ee` | `e28a8ee5825564baf0d75720d8f3c1a53a911e9c53956aff49ed2460fd08c8dd` | 2,561 | 214,610 | 484 | 26,868 |
| `449713` | `449713150e945977420638c65ab411b2f26e188b9bd48d4949f2f64a46a9d207` | 2,548 | 214,766 | 478 | 26,907 |
| `560d8d` | `560d8d86a7728d1b1e6497c00547aafbcc75c8b5e2b52e9f7ff60144bdfe85fe` | 2,545 | 214,803 | 478 | 26,935 |
| `68d439` | `68d439c60ddf4db9f249ee7aa5fa58fd1df9bf2356b3ad4680d01066a5743d13` | 2,548 | 215,271 | 476 | 27,045 |
| `fe45c2` | `fe45c235bab4130ec953f6f8e0b96f9bdf2b6ad6187a5a72426be28823e31fdb` | 2,555 | 215,253 | 476 | 27,028 |
| `6c0ed7` | `6c0ed7db18b216e020e72f809431c7b714c79074ae2d6f713a2787373eb655e7` | 2,543 | 215,281 | 478 | 27,005 |
| `452a33` | `452a332d5eeb57c7b3742bf70bce4b405578d00df44cb71984c066ac7b143016` | 2,545 | 214,979 | 479 | 27,038 |
| `d32ed6` | `d32ed635fb93062d1539ebccc0e8266b5529d514b1bd696d3ca7056c7cf9aef9` | 2,546 | 215,119 | 480 | 27,040 |
| `3e7af6` | `3e7af637c3b840483e305e9e0f3494eaedd1378c1f445455e5551a3c047cbe77` | 2,546 | 215,115 | 480 | 27,038 |
| `4e7a5f` | `4e7a5fa38a661feea83dcc7bb9179e9194130b13a3fad3e810f169ce3e225402` | 2,543 | 215,262 | 477 | 26,967 |
| `4213de` | `4213de9d9edc881949b89e7bc0a65de8fe3446dd6e708c5cabe9001609490686` | 2,548 | 215,605 | 483 | 27,054 |
| `ae88fc` | `ae88fc0b489a5b436ca3c2fe10462d80a18aed6cec8e03df871d5abe96561beb` | 2,545 | 215,304 | 481 | 27,013 |
| `2e9194` | `2e9194935b261dc178daee3aaf47fc9acc1bf1f2af5b6eb31e5004bb4ffd9ceb` | 2,547 | 215,299 | 482 | 27,012 |

These counts are genuinely seed-relative.  In particular, inheriting the
`d44b` count for the `e28a8ee`, `449713`, or `560d8d` round would be wrong.

## 3. Exact transition ledger

Here `U/B` is the canonical unary/binary circuit census.  Thus
`changed roots = U + 2B` on every row.

| transition | selected-circuit SHA-256 | accepted | U/B | changed roots | source support 1/2 | exact ledger | exact final replay |
|---|---|---:|---:|---:|---:|---|---|
| `d44b -> e28a8ee` | `76141e89195968a3438b0ab5707308693f9dda41a119c7ede0951135a59fd191` | 449 | 42/407 | 856 | 2,541 / 213,714 | yes | yes |
| `e28a8ee -> 449713` | `ff607593b55407d703f5340c286b8a4bf1cfb70b4266e63f7e450d9416fc88e4` | 303 | 36/267 | 570 | 2,561 / 214,610 | yes | yes |
| `449713 -> 560d8d` | `2a62cc72bcb4117cc9117046beb0def4c9728564604124c7ddfe3438e8f748d0` | 197 | 27/170 | 367 | 2,548 / 214,766 | yes | yes |
| `560d8d -> 68d439` | `4d09c1292a5f952204bc0541e2fac2d035adbcbb8efdd9f91bbac6a40c8d57e8` | 87 | 6/81 | 168 | 2,545 / 214,803 | yes | yes |
| `560d8d -> fe45c2` | `3483de3840764eab0828d05c8049b975542e86d012a4e8bc83e65b369b66307e` | 97 | 8/89 | 186 | 2,545 / 214,803 | yes | yes |
| `68d439 -> 6c0ed7` | `18a6da04b36ef12902bfbad52515f4a8e0085b838145036c37c1741e5d7214e1` | 73 | 11/62 | 135 | 2,548 / 215,271 | yes | yes |
| `6c0ed7 -> 452a33` | `cadaaf1660e6addc0fef7eb8424895e4dc927faf5c7d58e29bf44411eaa9585f` | 19 | 2/17 | 36 | 2,543 / 215,281 | yes | yes |
| `452a33 -> d32ed6` | `7c8868d4064f25a06adbe5f8cf2bbe912096849d995146d031365ee0968f7ce2` | 5 | 0/5 | 10 | 2,545 / 214,979 | yes | yes |
| `d32ed6 -> 3e7af6` | `a5902392f800f173f6b9ca82aea7dcca972246b70c2ab3aebeb034419edd05e7` | 1 | 0/1 | 2 | 2,546 / 215,119 | yes | yes |
| `560d8d -> 4e7a5f` | `9207c840ad2bebb4214df184a037563ec745592348716bc6b1b3cccdc5299819` | 168 | 23/145 | 313 | 2,545 / 214,803 | yes | yes |
| `4e7a5f -> 4213de` | `bc38a9a18bfb9b1ecfa800e38f2dce225f99578e33fe2c77b7e7b4a93a145eb0` | 69 | 7/62 | 131 | 2,543 / 215,262 | yes | yes |
| `4213de -> ae88fc` | `bf5f2ad6d1d72d2a4dfe29b31def98396ab707d1ec3d923019b71171466ca827` | 24 | 5/19 | 43 | 2,548 / 215,605 | yes | yes |
| `ae88fc -> 2e9194` | `e84314fd3605545b1c69213657a4b4d2a6423d9d6509db6c69afefb2a8a8ae8a` | 2 | 0/2 | 4 | 2,545 / 215,304 | yes | yes |

For the common-first heuristic, the search accepted 238, 84, 25, and 2
intermediate incumbent updates, respectively; the table records the final
root-disjoint packets of 168, 69, 24, and 2 circuits that the clean verifier
replayed.  Intermediate update count is not a circuit count.

Every reconstructed final has the exact type masses

```text
(139, 297, 8, 20, 20, 140, 127, 237, 442)
```

and exactly one copy of every lower target orbit: 8 rank-two, 40 rank-three,
140 rank-four, 364 rank-five, 728 rank-six, and 1,144 rank-seven orbits.

The reverse catalogue implementation is bound by SHA-256
`289151cfcda8a559f0900c03239042f6a6c53ac93a6a05066d5ecb49722abbdd`.
The round-three forward branch is bound by
`3c892952b68350c1fc0c2e1c3ae02e7f222c8b5e1d9467b864e969e87a3530fd`.

## 4. Fully rebuilt packet metrics

The zero columns are ordered `zero packet out / zero packet in`.

| node | loop-free turns/edges | packet maximum matching | packet zeros | labelled state arcs | state zeros out/in | common both-live maximum |
|---|---:|---:|---:|---:|---:|---:|
| `d44b` | 970 | 556 | 723 / 826 | 7,760 | 6,997 / 11,950 | 287 |
| `e28a8ee` | 1,855 | 954 | 234 / 445 | 14,840 | 2,803 / 11,140 | 718 |
| `449713` | 2,089 | 1,110 | 134 / 307 | 16,712 | 1,918 / 10,928 | 867 |
| `560d8d` | 2,178 | 1,178 | 103 / 235 | 17,424 | 1,635 / 10,853 | 936 |
| `68d439` | 2,212 | 1,207 | 95 / 213 | 17,696 | 1,561 / 10,823 | 961 |
| `fe45c2` | 2,219 | 1,206 | 92 / 214 | 17,752 | 1,535 / 10,808 | 965 |
| `6c0ed7` | 2,250 | 1,220 | 87 / 204 | 18,000 | 1,478 / 10,784 | 976 |
| `452a33` | 2,264 | 1,221 | 81 / 203 | 18,112 | 1,425 / 10,770 | 983 |
| `d32ed6` | 2,263 | 1,223 | 84 / 201 | 18,104 | 1,448 / 10,770 | 981 |
| `3e7af6` | 2,265 | 1,223 | 84 / 201 | 18,120 | 1,447 / 10,769 | 981 |
| `4e7a5f` | 2,225 | 1,156 | 56 / 237 | 17,800 | 1,271 / 10,802 | 1,099 |
| `4213de` | 2,236 | 1,166 | 49 / 217 | 17,888 | 1,203 / 10,794 | 1,132 |
| `ae88fc` | 2,244 | 1,171 | 42 / 216 | 17,952 | 1,142 / 10,787 | 1,141 |
| `2e9194` | 2,245 | 1,172 | 42 / 215 | 17,960 | 1,143 / 10,787 | 1,141 |

The two round-three children are not ordered by a single objective.  The
forward child has packet matching 1,207 rather than 1,206 and one fewer
zero-in packet; the reverse child has common both-live matching 965 rather
than 961, three fewer zero-out packets, more literal turns, and fewer dead
states.  This is a real Pareto split, not an audit mismatch.

The authenticated packet-first terminal is `3e7af637...`: basin07 accepts
one binary circuit and changes only turns `2263 -> 2265` while packet score,
packet zeros, common score, and Hall deficiency stay fixed.  The subsequent
basin08 forward scan accepts zero circuits and reproduces the same SHA, so it
is a fixed point only for that frozen catalogue order.

The common-first terminal currently frozen is `2e919493...`.  Its two binary
circuits leave the primary common score at 1,141 while improving packet
matching `1171 -> 1172` and zero-in `216 -> 215`.  This is the first
**common-primary heuristic plateau**.  It is not a support-two ceiling and is
not an optimality result.

## 5. Common both-live Hall witnesses

For a fixed certificate, form the bipartite graph from roots to owners in
which an incidence is present exactly when its aligned attachment state has
at least one literal incoming and one literal outgoing arc.  The alternating
shore `S` from unmatched roots satisfies `N(S)` equal to the displayed head
shore.  Every row below obeys

```text
|S| - |N(S)| = 1430 - maximum_common_live_transversal.
```

The IDs themselves are retained in the machine audits; the table binds them
compactly by SHA-256.

| node | maximum | tail/head | deficiency | tail-ID SHA-256 | head-ID SHA-256 |
|---|---:|---:|---:|---|---|
| `d44b` | 287 | 1,153 / 10 | 1,143 | `963fe61c58dbef66231b8257c26cef1082f4340338fcc8926748373f3bef6fcb` | `ba43856eb1e43f068e5778da929f45c8bae86d19f44231d49b3b07e04e811e44` |
| `e28a8ee` | 718 | 770 / 58 | 712 | `980087d9fa6dbd3fc87a8c5ba90179a31aa727f71db5aaffdbbde6395dcd4773` | `87a3c7dfbcb139dfe64c5f6994f063599247ae18c3f9e1a74820288ac36e25dd` |
| `449713` | 867 | 684 / 121 | 563 | `48f6ed9429429831306782eb06ae2fee81e2124cd9e00b4b1092a3b870178ec7` | `f0f3387add3791fc498cff2730f242682414509b85a544fa91c0b4ac07b81bd2` |
| `560d8d` | 936 | 652 / 158 | 494 | `1937e4cfef6d33d11297aff530cf642cc1eeccd5622603ac26ea89e1559e7b26` | `a2484f72ed948962144e45fbd7657d1f2174f01bf359f37a88ef350ae8c3b6ed` |
| `68d439` | 961 | 657 / 188 | 469 | `3d18dd9e6cd12b25ebef135c4d6f474032c3a203d4b1db31a0506bd8dd813b18` | `57bb7fe7a9061c47a3e92a2915e4a20cf0f9266a310c893f0ce36bbc973d2e03` |
| `fe45c2` | 965 | 654 / 189 | 465 | `b08c20923c5d26a14ef9be07fcfe3392a0f6681a62ec912e562126861e5e1f01` | `bc0c0f5c1dcb0d690c1db25112bd2851bee6f43c06be5f6deacbbcc85de4fd87` |
| `6c0ed7` | 976 | 637 / 183 | 454 | `487148e0cc527b49a4c75a0510875ba59a37d86026cb013aa95ad6dc3dd92847` | `f1c84cd5163b60fdeeb21d2200eb8c19c8fe954130b50a0fad4f1a470e959f64` |
| `452a33` | 983 | 641 / 194 | 447 | `a2b257d13b7857078180fcfe02a859056a36ec43cb6d90b49eb4d136f51f5fb7` | `c24a83231fe65477bebf6930ec7984c247c332c6a8b3e71bf5185e4fbb567271` |
| `d32ed6` | 981 | 637 / 188 | 449 | `1b30f08460a7133776623cb50f96714fd5d4ff63fcba302f88c5add7458d38f8` | `782e9bafec4e9bb7cdbcc9d4eecbc52cadc4dc8ca626936fa6cfa13569da5e71` |
| `3e7af6` | 981 | 637 / 188 | 449 | `1b30f08460a7133776623cb50f96714fd5d4ff63fcba302f88c5add7458d38f8` | `782e9bafec4e9bb7cdbcc9d4eecbc52cadc4dc8ca626936fa6cfa13569da5e71` |
| `4e7a5f` | 1,099 | 365 / 34 | 331 | `d1cb52d97a74c9b473c373bee73a976f4f806c66c28ec666d208f19ce8a84009` | `5fd4ba21cd2a68faa28753835e4ef0a21907a7e81c06f7053cff736a7ea8453d` |
| `4213de` | 1,132 | 319 / 21 | 298 | `53857e20985a4cd35dfb878efdc669b3894c2842db9e57dc44575552f465f341` | `745d89a4f43f5c91ec3dfb13795e1dcaddc2235aac0c3d57b2f9cef75c620f5b` |
| `ae88fc` | 1,141 | 306 / 17 | 289 | `f7649d2bf4b72fbfe5e9d7fc9f1da6da4b4c4f064009f5c49be1d40757056e71` | `bb68f0844a0fad7d52fa8071d3f94c4c420909d547e9ba9c404702579c4169b5` |
| `2e9194` | 1,141 | 309 / 20 | 289 | `b4b53adeec2bee28d4940cf15d61ab9be14b3322c248dcdfffb7da8daf07c829` | `b0a829233d98df7b6a48a77f9778ad95f32fedec372d75930cf8b7f63932c6bd` |

Thus none of the fourteen frozen nodes has a perfect common root-owner both-live
transversal.  This is an exact obstruction for that frozen certificate and
that necessary common-state relaxation; it is not a general impossibility
theorem for other recataloguings.

## 6. Proof and independence ledger

The canonical packet converter reads the source and move rows but is not
trusted as a verifier.  It only expresses each literal replacement in the
public support-at-most-two schema.  The independent C++ verifier then
re-enumerates all 1,904 literal options at every changed root, derives the
resource signature of each old and new option, checks unary-zero or
binary-opposite delta semantics, and checks pairwise root disjointness.  It
applies those literal replacements, compares all 1,430 reconstructed rows
with the supplied final table, and independently accumulates the final
resource ledger.

The same verifier enumerates the aligned survivor/refresh recurrence from
the reconstructed final rows.  It does not consume the greedy audit's
matching values, zero sets, transition deltas, or degree scores.  Its packet
and state metrics agree with the separate direct-row decoder.  Its common
both-live maximum matchings and alternating Hall shores agree with the
separate Python DM audit, including all five counts/hashes per shore.

The orchestration audit additionally checks actual certificate hashes,
source/final continuity, catalogue counts against each round, move-row counts,
arity/root-support identities, frozen-vs-clean-room baseline and final
metrics, and every compact Hall field.  It terminates on the first mismatch.

Machine-readable result:

`scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/serial_chain.fail_closed.audit.json`

Verifier:

`scratch/audit_k17_serial_rooted_flag_recataloguing_chain_20260801.py`

The machine result has status
`PASS_K17_SERIAL_ROOTED_FLAG_RECATALOGUING_CHAIN_FAIL_CLOSED`, an empty
`mismatches` array, and payload SHA-256
`4e16ce035105b5003219ce16b2de6717a12f822125061371ccf0ae24a9efee9f`.

For the serial03 common-primary plateau, the byte SHA-256 of the independent
clean selector audit is
`3e30ef7f5b05ffba7d7652b99d1be79d275c8fd7aa81f50d10c741c361df31e9`,
and the independent common-DM payload SHA-256 is
`0972cca56dbf0576d3d09a5fbef8a0ad3de80854325bc64ad9c0d1ef7b266d61`.

## 7. Mismatch and limitation ledger

No mismatch was found in the 13 accepted transitions or the terminal empty
packet-first pass.

One apparent lineage mismatch was found and resolved.  The basin05 forward
sibling `e9b175c0...` has seed-relative counts `2546 / 215002`, which do not
match basin06's declared source catalogue `2545 / 214979`.  The basin05
reverse child `452a332d...` has exactly `2545 / 214979`; therefore the
authenticated packet-first lineage goes through `452a332d`, not
`e9b175c0`.  This is a rejected path assumption, not a mismatch in the
accepted certificate chain.

One non-error diagnostic deserves explicit treatment: the clean-room
selector verifier's built-in calibration table recognizes the original
`d44b` seed but not the later serial sources.  The later transitions are
nevertheless authenticated by exact chain hashes, full source-ledger checks,
literal packet replay, exact final reconstruction, and independent geometry
rebuild.  `recognized_seed=false` is therefore expected metadata, not a
failed check.

Excluded claims remain: upper rows, a selected 12,870-state root-owner
transversal, an induced directed cycle cover, connectivity, voltage,
residence beyond the three-age recurrence, opening, and compiler feasibility.

## 8. Proposed handoff and index text

Proposed handoff paragraph:

> The authenticated K17 rooted-flag support-1/2 recataloguing ledger now has
> two independently replayed continuations from SHA `560d8d86...`.  The
> packet-first lineage is `560d8d86 -> 68d439c6 -> 6c0ed7db -> 452a332d ->
> d32ed635 -> 3e7af637`, ending at packet matching 1,223, packet zeros
> 84/201, and common both-live matching 981 with Hall shore 637/188
> (deficiency 449); an empty next scan certifies only catalogue-order
> maximality.  The common-first lineage is `560d8d86 -> 4e7a5fa3 ->
> 4213de9d -> ae88fc0b -> 2e919493`, ending at packet matching 1,172,
> packet zeros 42/215, and common matching 1,141 with Hall shore 309/20
> (deficiency 289).  Every edge has exact source-relative catalogue counts,
> a root-disjoint canonical packet, exact lower/type ledger, byte-exact final
> replay, fully rebuilt transition geometry, and an independent common-DM
> witness.  These are heuristic incumbents; neither endpoint is claimed
> support-two optimal.

Proposed `RESEARCH_INDEX.md` entry:

> **K17 rooted-flag serial recataloguing chain (fail-closed audit, 2026-08-01).**
> See `K17_SERIAL_ROOTED_FLAG_RECATALOGUING_CHAIN_THEOREM_AUDIT_20260801.md`
> and
> `scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/serial_chain.fail_closed.audit.json`.
> Authenticates the packet-first `3e7af637` terminal and common-first
> `2e919493` first common-primary plateau through literal support-1/2 packet
> replay, exact resource ledgers, full transition rebuilds, and Hall shores;
> no global-optimality or support-two-ceiling claim.
