# K16 exact229: Hall-24 braid and connected-support3 composition gate

Date: 2026-07-30.  Lane D.  Exact arithmetic and solver-free replay only.

## 1. Four authenticated nonlocal carriers

Let `Q` be `exact_229.targets`, SHA-256
`cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974`.
For a word `W`, write

```text
S(a,b,l)W
```

for the forward exchange of the two equal, half-open blocks
`W[a:a+l]` and `W[b:b+l]`.  The following four words have the exact normal
form

```text
S(6613,12721,nested) S(6611,12718,outer) Q.
```

The rightmost operation is performed first.

| pass | `(outer,nested)` | target SHA-256 | incidence count | Hall shore | matching/deficiency |
|---:|---:|---|---:|---:|---:|
| 33 | `(16,9)` | `2dbb84bc6467047d99019e58b6a33072cbca8f0bc6e62c451954603611fcf2ec` | 347,649 | 211/187 | 26,308 / 24 |
| 35 | `(18,9)` | `42420e0eea7102a07227b25e49663a127f89219b8c41cb18ee7de699385d9b04` | 347,649 | 198/174 | 26,308 / 24 |
| 46 | `(16,13)` | `bf3ee02110f70c168dc9863e1c8258cc54debfa408dd4c97fe5b57c6a4116754` | 347,809 | 211/187 | 26,308 / 24 |
| 55 | `(18,15)` | `e1166c6ae5f6c671c779bfb9f692fa8332aa7b9978cfcd93671b64244c5f1f69` | 347,737 | 198/174 | 26,308 / 24 |

For every row, an independent replay checks:

1. literal reconstruction by the displayed ordered pair of swaps;
2. exactly the old flats `6320,12869,12871`;
3. no zero maximal envelope and exact reconstruction of every middle row;
4. zero arbitrary-width accumulated-union upper holes;
5. all 26,308 recorded matching edges, with distinct left and right endpoints;
6. the complete neighbour set of the recorded deficient shore.

Thus each matching is a valid lower bound of 26,308 and each displayed shore
is an independent upper bound of 26,308.  The deficiency 24 is exact, not a
score.  All 24 recorded unmatched targets have rank seven.  The complete
matching and shore arrays remain frozen in the four `.hall.json` files; the
audit records separate canonical hashes of those arrays.

In every carrier, lower target `0x8000` has the unique provider cell
`(start,length)=(12720,1)` (cell id 31,761), while `0x4e70` still has degree
zero.  Thus any old-matching protection certificate must in particular retain
this named `0x8000` edge or replace it by a new augmentation.

## 2. Connected support-three result on the old root

The completed A/B-normal-form connected census contains all

```text
x<y<z,  1<=y-x<=6,  1<=z-y<=6,
```

and both directed 3-cycles, for exactly 926,352 directed candidates.  It has
one middle-exact row and no exact+upper row.  The unique descriptor is

```text
(x,y,z,orientation) = (12868,12870,12872,0),
(T_x,T_y,T_z)        = (8c67,cc63,ce61),
(T'_x,T'_y,T'_z)     = (cc63,ce61,8c67).
```

Independent replay gives:

```text
flats             = 6320,12868,12870
capacity          = 32061
zero envelopes    = 0
bad middle rows   = none
upper holes       = 8ce7,bcef,cc67
```

Applying this same, separated 3-cycle to each of the four Hall-24 carriers
again gives exactly these three upper holes.  Therefore it yields no legal
composition and no Hall run is warranted.

## 3. Exact interaction-shell reduction

For a connected support `x<y<z`, every target, changed flat edge, maximal
envelope, and reconstructed middle equation that the 3-cycle can affect lies
in the conservative interval

```text
[x-3,z+3].
```

The nonlocal words differ from `Q` on exactly two target intervals:

```text
outer=16: [6611,6626] and [12718,12733],
outer=18: [6611,6628] and [12718,12735].
```

Suppose `[x-3,z+3]` misses both intervals.  The local flat/depth/controller
response of the 3-cycle is then identical on `Q` and on the nonlocal carrier.
Outside that response interval the 3-cycle changes nothing and the nonlocal
carrier is already exact.  Hence exactness of the composition is equivalent
to exactness of the corresponding support-three row on `Q`.

The completed root census and the replay in section 2 consequently eliminate
every separated support.  Any exact+upper composition must belong to the
following finite shell:

| carrier | oriented shell | support directly meets changed targets | collar-only interaction | separated eliminated |
|---:|---:|---:|---:|---:|
| 33 | 4,176 | 3,312 | 864 | 922,176 |
| 35 | 4,464 | 3,600 | 864 | 921,888 |
| 46 | 4,176 | 3,312 | 864 | 922,176 |
| 55 | 4,464 | 3,600 | 864 | 921,888 |

Each shell splits equally between the first and second nonlocal collars:
2,088/2,088 for outer length 16 and 2,232/2,232 for outer length 18.  A
first-collar row leaves the named `(0x8000,(12720,1))` provider physically
untouched; this does not by itself protect the other 26,307 matching edges.

The total remaining quantifier is **17,280**, versus 3,705,408 raw
carrier/support pairs.  The 17,280 rows, including both orientations and a
protected-matching collar score, are frozen in
`scratch/threadD_k16_exact229_braid24_support3_interacting_shell_20260730.tsv`.
The reduction itself is not a negative census; the completed census is
recorded in section 7.

## 4. Exact gates for the 17,280 rows

The composition order is literal:

1. perform the outer forward swap;
2. perform the nested forward swap;
3. cycle the **current** values at `x,y,z` in the selected orientation.

This last point matters when the support overlaps a braid block.  Installing
the three old `exact229` values would be the wrong operation.

For each row the following gates are necessary.

### Middle chronology

Recompute all flats and the induced depth schedule, then compute every maximal
envelope and replay every row.  Neither the root support3 result nor a sum of
two local defect vectors is a substitute when the collars overlap.

### Arbitrary upper coverage

Run the full accumulated-union automaton over all widths.  Spatially separated
edits can still share or destroy a long occurrence-labelled witness, so no
fixed-width or hole-only composition rule is sound.

### Full matching protection and improvement

For a sufficient old-matching certificate, map each frozen right cell to its
canonical `(start,length)` key and check all 26,308 target-cell edges in the
final geometry.  Collar disjointness never proves this in the interaction
shell: every shell row's conservative affected-cell-start interval
`[x-5,z+6]` contains at least 16 frozen matched cells (maxima are 46,47,47,48
for passes 33,35,46,55).

Even preservation of the old 26,308-edge matching proves only deficiency at
most 24.  Every middle-exact and upper-complete shell row must receive a full
generalized Hall computation.  A claim of deficiency below 24 requires a
matching of at least 26,309 in that final graph; fixed-shore current alone is
diagnostic.

## 5. Frozen artifacts and scope

- Audit source:
  `scratch/audit_threadD_k16_exact229_braid24_support3_composition_20260730.py`,
  SHA-256 `0e4d47619b25c2dd87078c41559c1b9b08b9c99a32e3d259fc3fb024f54e17a7`.
- Audit certificate:
  `scratch/threadD_k16_exact229_braid24_support3_composition_20260730.audit.json`,
  SHA-256 `c255d4816a1d31acba826088d335875cbef744904d538d24a4d517a33fcfe9e7`.
- Complete 17,280-row shell:
  `scratch/threadD_k16_exact229_braid24_support3_interacting_shell_20260730.tsv`,
  SHA-256 `c4acabc7d096385706abbe2e6cf28d6e192562879e8537cfc7a9637fc86bbd11`.

The shell-construction audit took 13.19 seconds locally and used no SAT/CP or broad search.  It
authenticates the four carriers, the exact support3 descriptor, and the
composition quantifier.  The subsequent native and independent H100 runs in
section 7 enumerate that shell completely.

## 6. Exact execution package

The following fail-closed package was compiled/syntax-checked locally and run
only on one H100 CPU:

- native shell engine
  `scratch/threadD_k16_exact229_braid24_support3_shell_census_20260730.cpp`,
  SHA-256 `c4a8ec960013e1c00a5af3e2033df8a5540d0b3f161d87117bc3809a5cf789c7`;
- exact Hall orchestrator
  `scratch/threadD_k16_exact229_braid24_support3_shell_hall_orchestrator_20260730.py`,
  SHA-256 `50079293096533ecdc5477956bc896db6d7af0763a3dedb6541fee535ecd4c7f`;
- one-CPU, 2-GiB H100 launcher
  `scratch/run_threadD_k16_exact229_braid24_support3_shell_h100_20260730.sh`,
  SHA-256 `3514f684c92e973d3d3874e2b9f41184e428163b0d64b2d24b363837f3f16c5d`;
- frozen input manifest
  `scratch/threadD_k16_exact229_braid24_support3_shell_expected_20260730.sha256`,
  SHA-256 `a929de920ea57d0d38349a50beba90e67261d40975ae7563899afdb5899fdb4e`.

The native engine regenerates the shell internally and requires equality with
the TSV, so a missing or duplicate descriptor is fatal.  It composes each
cycle with the current parent values, performs dynamic exact replay and full
upper replay, and materializes every exact+upper chronology.  The orchestrator
independently reconstructs each materialized word from its parent, repeats the
geometry and upper audits, and runs full generalized Hall on every survivor.
It retains full artifacts exactly when deficiency is below 24.  Timeout,
memory exhaustion, malformed output, or a nonstandard subprocess exit is
`UNKNOWN`, never `UNSAT`.

The unique root exact row also has a separate independent certificate:

- source
  `scratch/audit_threadD_k16_exact229_support3B_unique_exact_independent_20260730.py`,
  SHA-256 `b214636b8c1c36b955c14c5ffd7b7b2104483e47a9eed420a59c839c1ed52a6b`;
- audit
  `scratch/threadD_k16_exact229_support3B_unique_exact_independent_20260730.audit.json`,
  SHA-256 `91b079aadea7eba2acc39d1307c8e5be6b0a29f87802a40d5d6d66e09f5db225`.

## 7. Completed census and theorem

The native H100 run regenerated the 17,280-key shell internally and required
literal equality with the frozen TSV.  Its exact counts are

| parent | interacting descriptors | middle-exact | exact+upper |
|---:|---:|---:|---:|
| 33 `(16,9)` | 4,176 | 0 | 0 |
| 35 `(18,9)` | 4,464 | 0 | 0 |
| 46 `(16,13)` | 4,176 | 0 | 0 |
| 55 `(18,15)` | 4,464 | 0 | 0 |
| **total** | **17,280** | **0** | **0** |

Thus there is no upper or Hall survivor hidden in the interaction shell.
The exact Hall orchestrator verifies an empty, complete initial interval of
candidate IDs: expected `0`, completed `0`, deficiency-below-24 count `0`.
Its return code 2 is the documented no-candidate status.

A second C++ implementation, sharing no production-engine include,
independently regenerates the shell and computes the depth-three row-cover
meets directly.  It gives the sharper partition

```
flat-count 3 / schedule-valid       17,280
zero-envelope-free                  17,278
one zero envelope                         2
reconstruction-free                       0
middle-exact                              0
minimum number of bad middle rows         2
descriptors attaining two bad rows       10
```

Its complete bad-row histogram is

```
2:10, 3:258, 4:285, 5:605, 6:836, 7:1828, 8:2405,
9:2971, 10:3042, 11:2070, 12:1540, 13:915, 14:422, 15:93.
```

Combining this with the locality theorem gives the result for the entire raw
class of `4*926352=3,705,408` parent/support pairs.  Among the 3,688,128
separated pairs, each parent has exactly the already-classified tail rotation
`(12868,12870,12872,o0)` as its sole middle-exact row; it has upper holes
`8ce7,bcef,cc67` on every parent.  The interaction shell has no middle-exact
row.  Consequently the full four-parent composition class has exactly four
middle-exact rows, **zero exact+upper rows, zero Hall candidates, and no
Hall-deficiency-below-24 chronology**.

Production run:

```
native census: 4.95 s wall, 7,472 KiB RSS, documented rc2
Hall ledger:   4.20 s wall, 89,088 KiB RSS, documented rc2
```

Independent run:

```
direct replay: 9.02 s wall, 6,144 KiB RSS, documented rc2
```

All three stages completed under their caps; none is `UNKNOWN`.

Frozen result hashes:

```
production native result  3da9dfae3bfbb4ea1f233136f64e515a2f2da9aedb55ce0f777220a2a752095c
production exact ledger   e7da9add860dbba1d753f660e75be75e0cf1752e56146d2a91e262cc4ade0f00
production patch ledger   ab326c225b9ec9ab16f5081dda9cf03c01e35e6b4cd672654d7617aebc8ae741
production Hall summary   8f6925c625a1a577842956ce03f4a93942aa16bd29482de94a82e84e3f64d475
independent source        f54ea074b351428c93dc9610fde4d917336d3e2f60bbd192e38204ad2d90fe05
independent audit         26b4ac16ba0468d0fbb1e803253bd4d72885b60a53d0a4980b832900345d0e33
```

This closes one connected support-three cycle after either authenticated
nested braid.  It does not close two interacting local cycles, class A's
remote third position, a larger support permutation, or a new nonlocal braid.
