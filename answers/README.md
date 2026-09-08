# Exact answers through `k=20`

The files below are optimal nonzero words. Dimensions 1–16 use the legacy
`kNN.word` names; dimensions 17–20 use the linked descriptive filenames.
Every contiguous-subarray OR is computed over ordinary integer bitmasks.
Each listed length attains the endpoint lower bound B(k). The next
unresolved dimension is 21.

| `k` | `nu(k)` | SHA-256 |
|---:|---:|---|
| 1 | 1 | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` |
| 2 | 2 | `f251ddc12234e0da8d3b778bd0f7463fb477f16f47757f5617dc8b4ff4d4f14a` |
| 3 | 4 | `aafa934d13be209cc39a9b5cb0b140af652fc0eebd127c42c6c982422964a790` |
| 4 | 7 | `efe145ebc697686a2e3bf53a36362b5025835f2eb0ba16a1a0e64e2abd4ec1ca` |
| 5 | 12 | `72195450d0361b37fbf58442203014eff475b3f59222c907fab99743106eee06` |
| 6 | 21 | `7d30e058f98e6c09d65515e3f3971ae8bd7637f711670fa06a8a1dc536852d6d` |
| 7 | 37 | `dda4b06c2e35bda3ea8a876a90807172adee166567d84b587ef5ae68cae9bec7` |
| 8 | 72 | `df6d76b468bd816fd014d9b6f5259ba60e5f1ea06e4c4313901fe6155c8780eb` |
| 9 | 128 | `c7e8cbfbe1a3531ffae4c9a01bd4b3b51dad0856b38486bacc56dbcaa73e3221` |
| 10 | 254 | `24b6fc4f4c054e46ef54553ca37eded126150542d51a61256a837d666e0c74fd` |
| 11 | 465 | `746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850` |
| 12 | 926 | `6d598c62f5925d1d2dfce8279eea82069318bd93ff66d0b204c639cf06297851` |
| 13 | 1719 | `8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0` |
| 14 | 3434 | `7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17` |
| 15 | 6438 | `f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b` |
| 16 | 12873 | `890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe` |
| [17](k17_optimal24313.word) | 24313 | `7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9` |
| [18](k18_optimal48623.word) | 48623 | `6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5` |
| [19](k19_optimal92381.word) | 92381 | `1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414` |
| [20](k20_optimal184759.word) | 184759 | `047b990b9e9f7a4585ba5d8fadf9c3d191cd218c989c3ffacf6e351d91b88d02` |

The empty word is optimal for the nonzero `k=0` problem, so no `k00.word`
file is needed.  Prepending `0` to any listed word gives an optimal word for
the version that also requires the zero mask.

Verify the legacy filenames for dimensions 1–16 with:

```sh
for k in $(seq 1 16); do
  python3 verify_word.py --k "$k" "answers/k$(printf '%02d' "$k").word"
done
```

## Exact `k=15` certificate

The monotone-deadline lower bound and the retained word give

\[
                         \nu(15)=6438.
\]

The construction and independent exhaustive verification are recorded in
[`K15_OPTIMAL_6438_TWO_CYCLE_ARBITRARY_SEAM_CERTIFICATE_20260729.md`](../K15_OPTIMAL_6438_TWO_CYCLE_ARBITRARY_SEAM_CERTIFICATE_20260729.md).

## Exact `k=16` certificate

The monotone-deadline lower bound and the retained word give

\[
                         \nu(16)=12873.
\]

The construction, exact common-cap matching model, and four independent
literal replays are recorded in
[`MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md`](../MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md).

## Exact `k=17` and `k=18` certificates

The supplied [24,313-letter word](k17_optimal24313.word) is optimal:
nu(17)=B(17)=24313. The
[independent direct-forward certificate](../scratch/K17_OPTIMAL24313_DIRECT_FORWARD_AND_TWO_CYCLE_SEAM_CERTIFICATE_20260908.md)
verifies all 131,071 targets and the literal two-cycle seam. Its matching
endpoint lower bound is recorded in the
[standalone lower-bound audit](../scratch/K17_STANDALONE_ENDPOINT_LOWER_BOUND_AND_LITERAL_OPTIMALITY_AUDIT_20260908.md).

The supplied [48,623-letter word](k18_optimal48623.word) is also optimal:
nu(18)=B(18)=48623. Its complete checks cover all 262,143 nonempty targets
by independent first-occurrence enumeration and suffix/range-OR replay.
See the [exact 18 record](../K18_OPTIMAL48623_VERIFIED_20260908.md).

## Exact `k=19` and `k=20` certificates

The supplied [92,381-letter word](k19_optimal92381.word) covers all 524,287
nonempty targets, and the supplied
[184,759-letter word](k20_optimal184759.word) covers all 1,048,575.
The independent forward verifier explicitly checks every target and every
rank, and computes the endpoint bound over all ranks with exact integers.
Both literal lengths equal that bound, proving

```text
nu(19) = B(19) = 92381.
nu(20) = B(20) = 184759.
```

The completed [forward proof and certificate](../scratch/K19_K20_OPTIMAL_INDEPENDENT_FORWARD_CERTIFICATE_20260909.md)
links its independent source, raw hashes, full reports and every ordinary
interval witness. The actual
[combined machine report](../scratch/k19_k20_optimal_forward_20260909/k19_k20_forward_complete_certificate.json)
has PASS for both words. See the
[consolidated 19/20 record](../K19_K20_OPTIMAL_AND_CYCLIC19_VERIFIED_20260909.md)
and the [finite comparison](../FINITE_BOUNDS_K18_K19_K20_20260908.md).
These ordinary optimality claims do not depend on a reconstructed generator.

The separate [suffix/range/cyclic/lift report](../witnesses/k19_k20_optimal/complete_suffix_range_cyclic_lift_certificate.json)
also passes every saved interval query. The
[92,378-letter cyclic core](k19_cyclic92378.word) attains mu(19), and the
20-coordinate file regenerates byte for byte from its safe three-letter
opening and periodic continuation. This checks the supplied lift, without
claiming a replay of the unavailable search that produced the19 core.

| Dimension | Current optimal word | Endpoint lower bound |
| ---: | --- | ---: |
| 18 | [48,623 letters](k18_optimal48623.word) | 48,623 |
| 19 | [92,381 letters](k19_optimal92381.word) | 92,381 |
| 20 | [184,759 letters](k20_optimal184759.word) | 184,759 |

## Historical upper bounds in dimensions 18–20

The earlier dimension 18 lifts of
[48,626](k18_upper48626.word), [49,316](k18_upper49316.word) and
[49,336](k18_upper49336.word) letters remain as historical artifacts.
The [94,161-letter height-adaptive 19 word](k19_upper94161.word), SHA-256
`1c039f3225afa9fa32306c26d44cd7d79a05a83077dd928889b2d43286f86224`,
and its [188,322-letter 20 lift](k20_upper188322.word), SHA-256
`0d42106351f630eda5693e91a246ceb738f0704004a38b803eba8456aeec3874`,
are also retained unchanged. Their construction and complete verification
records remain linked from the
[finite comparison](../FINITE_BOUNDS_K18_K19_K20_20260908.md).
They are universal words but are now known not to be optimal.

## Historical `k=17` upper-bound words

[`k17_upper24658.word`](k17_upper24658.word) is the last recorded supplied
upper word before exact 17 closure. It has 24,658 nonzero letters, covers
all 131,071 targets, and has SHA-256
`24f7f831b7446e942cc0927472296b2d20069f694b8bbad6374e65cc07b6f7fb`.
Its complete suffix-OR and independent range-OR checks remain in the
[verification report](../witnesses/k17_upper24658/literal24658_verification.json)
and [target witnesses](../witnesses/k17_upper24658/literal24658_target_witnesses.json).
The user's rewrite/search regeneration procedure was not supplied; the
certificate verifies that historical literal word. It is 345 letters
longer than the now-proved optimum. Reproduce its check on h100 with:

```sh
python3 scripts/verify_k17_upper24658.py answers/k17_upper24658.word witnesses/k17_upper24658
```

[`k17_upper24668.word`](k17_upper24668.word) is retained with its
[complete verification](../K17_UPPER24668_VERIFIED_20260908.md), including
its original hash and all target witnesses.

[`k17_upper24715.word`](k17_upper24715.word) is the preceding supplied
universal word, retained unchanged with SHA-256
`3e7da8c69f8d32ca73750e12b8746fc483f9d56a441ad94f1d3a2e9b4c11b2fe`.
Its [literal verification](../witnesses/k17_upper24715/literal24715_verification.json)
and [target witnesses](../witnesses/k17_upper24715/literal24715_target_witnesses.json)
remain available. Its rewrite/search regeneration procedure was not
supplied or independently verified.

The independently constructed
[24,947-letter forest word](../scratch/k17_height_adaptive_20260908/binary_forest_repair/k17_height_forest24947.word)
is retained with SHA-256
`a358c7d539ea8af286c61a45f621b7d9bc1227c292829ea3bb981acd1f975389`.
It keeps the 24,829-letter prefix below and replaces its 128-letter repair
by a 118-letter binary-forest repair. That repair is optimal within the
specified forest model; the full word is now known not to be optimal. Its
[exact proof and full witness certificate](../scratch/K17_HEIGHT_ADAPTIVE24947_OPTIMAL_BINARY_FOREST_REPAIR_20260908.md)
remain available.

[`k17_upper24957.word`](k17_upper24957.word) is the independently implemented
deterministic height-adaptive PBBS construction, retained unchanged with
SHA-256 `dc7c7af32feb73c91fd14e00c6a046de6d753af4d2fc632f71960dcdbdd820db`.
Open each of the 146 canonical cycles at its least lower-owner mask, form
the intersection of each future `h+1` upper owners, and append the first
`h` letters of that period. Here `h` is the invariant Dyck height, and
cycles are ordered by their initial masks. This fixed concatenation has
24,829 letters and 128 missing targets. Appending all missing masks as
letters in increasing order gives the 24,957-word without a cut or ordering
search. Its [complete construction certificate](../scratch/K17_HEIGHT_ADAPTIVE_25202_AND_REPAIRED24957_EXACT_CERTIFICATE_20260908.md),
[literal verification](../witnesses/k17_upper24957/literal24957_verification.json),
and [target witnesses](../witnesses/k17_upper24957/literal24957_target_witnesses.json)
are retained.

`k17_upper25374.word` is an earlier supplied and verified universal word,
retained unchanged. Its SHA-256 is
`16951cef9e2efff841c6bbf9cc72f2061f35650dda850714fcceee7a7bb43208`.
Its [literal verification](../witnesses/k17_upper25374/literal25374_verification.json)
and [target witnesses](../witnesses/k17_upper25374/literal25374_target_witnesses.json)
remain available. The search's intermediate and Hall-count claims were not
independently verified. The 24,957-word saved 417 letters relative to it.

`k17_upper25745.word` is the earlier verified 25,745-letter boundary-splice
construction and is retained unchanged for provenance:

```text
SHA-256: ef69969f6f72bc85173c9ccb413b7c111a398e725b956f2a91cbe5decbabca38
```

For `X` equal to `k16.word`, its exact zero-based construction is
`X[1:][::-1] + [65536,50122,33642] + [x|65536 for x in X[3:]]`.
Appendix B of `MASTER_HANDOFF.md` proves coverage using seven source interval
identities, without requiring another external word body. Rebuild and verify:

```sh
python3 scripts/k17_boundary_splice_20260906_b7e41_audit.py --word answers/k17_upper25745.word
python3 scratch/verify_exact_or_word.py --k 17 --allow-longer answers/k17_upper25745.word
```

The 24,957-word saved 788 letters relative to that construction. The older
`k17_upper25746.word` is also retained unchanged for provenance.

## Historical nonoptimal K16 upper-bound words

`k16_upper12874.word` was the final upper bound before exact closure.  It is
retained for construction history but is not optimal.

Its SHA-256 is
`631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e`.
Verify it with

```sh
python3 verify_word.py --k 16 --allow-nonoptimal answers/k16_upper12874.word
```

`k16_upper12875.word` is the preceding verified upper bound.  It appends two
masks to an authenticated length-12,873 partial word and proves

```text
12873 <= nu(16) <= 12875.
```

Its SHA-256 is
`d4690a0d11f1d8e69765ec988d9fbcbac63d354ebd6ab07aa8081b577a9ac0c9`.
Verify it with

```sh
python3 verify_word.py --k 16 --allow-nonoptimal answers/k16_upper12875.word
```

`k16_upper12876.word` is a verified universal word, but is **not** claimed
optimal.  It is the standard trimmed lift of `k15.word` from which the newer
12,875 certificate was derived.

Its SHA-256 is
`9d0214f6c7cea45a1f26d031687ecada9ac34500e925dcfc127bdf1514b624c8`.
Verify it with

```sh
python3 verify_word.py --k 16 --allow-nonoptimal answers/k16_upper12876.word
```
