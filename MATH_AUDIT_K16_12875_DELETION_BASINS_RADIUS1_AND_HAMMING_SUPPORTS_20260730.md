# K16 current-upper deletion basins: radius one and Hamming-one supports

Date: 2026-07-30

## Scope

This report authenticates five named 12,874-entry words as literal single
deletions of the current retained 12,875-entry answer and recomputes their
holes.  It also proves a scoped no-go for one arbitrary nonzero substitution
of each fixed word and freezes complete symmetric Hamming-distance-one
provider-support unions for bounded multi-substitution SAT searches.

The support unions are search scopes.  They do not prove that positions
outside the files are unnecessary.  None of the results below is a global
length-12,874 impossibility theorem.

The retained answer is `answers/k16_upper12875.word`, length 12,875, SHA-256
`d4690a0d11f1d8e69765ec988d9fbcbac63d354ebd6ab07aa8081b577a9ac0c9`.
It independently replays as universal.

## Exact deletion authentication

All positions are zero-based.

| Deleted position | Deleted cell | Partial SHA-256 | Exact holes |
|---:|---:|---|---|
| 0 | `0x882c` | `992ca911870dfc85046819e99343547b37f5f5622c87318eb39c5f993b253110` | `0xa86d, 0xac6d` |
| 1 | `0x2829` | `e3d374011d2dc2260f9e31240157907816d47f28e0bad744f0172bf802ce7bcf` | `0x286d, 0x2c6d` |
| 6435 | `0x0600` | `f13597f56397aca9dc889bcb621148a026e2d23b3581e9945873c0faa13a0e26` | `0x4e61, 0x4e63` |
| 12873 | `0x0200` | `b8dd119d0be3bd7ec52d9b786aa2c85fad291081604c6b830d58b940501e0bd3` | `0xce61, 0xce63` |
| 12874 | `0x287d` | `aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18` | `0x287d` |

For every row, direct list deletion from the authenticated answer equals the
partial word entry-for-entry and byte-for-byte in canonical decimal format.
The last row is exactly the append-`0x0200` basin.

## Exact arbitrary one-substitution replay

The repository's generic enumerator is
`scratch/search_k16_one_substitution_completion_20260730.cpp`, SHA-256
`1c6fa9466354dc91d5ac3b9997e51370fa774a9ae863dd4260def185b47fcbcf`.
It enumerates every position and every nonzero submask of the intersection of
the old holes.  This restriction is necessary: every new hole witness contains
the edited cell.  It then removes exactly all old through-cell intervals and
creates exactly all `left suffix OR replacement OR right prefix` intervals.

Current-byte replay gave:

| Basin | Full enumerator rows | Best remaining debt | Result |
|---|---:|---:|---|
| delete p0 | 3,282,870 | 2 | `NO_PASS` |
| delete p1 | 1,634,998 | 2 | `NO_PASS` |
| delete p6435 | 1,634,998 | 4 | `NO_PASS` |
| delete p12873 | 3,282,870 | 1 | `NO_PASS` |
| delete p12874 | 3,282,870 | 1 | `NO_PASS` |

An independent Python replay uses a different reduction.  Separate forward
and backward OR-state passes compute the latest witness start and earliest
witness end of every target.  At each position it tests every nonzero submask
of the intersection of all targets whose old witnesses all cross that
position, followed by direct target-by-target join checks.  Candidate count is
zero for every deletion basin.  Necessary assignment counts are respectively
95,860; 59,831; 59,492; 95,414; and 77,283.

The independent audit also rejects every one-substitution completion of
`scratch/k16_fivephase_rex_hole20067.word`, SHA-256
`eef3555aa12675de8707de994d20300aaf8e96538b4691880810d84454fbb1b5`,
whose sole hole is `0x4e63`; it checks 77,159 necessary assignments.

The conclusion is exact only for radius one around each named fixed word.

## Complete symmetric Hamming-one support scopes

For every hole `h`, all sixteen masks `h XOR (1<<bit)` are included.  Every
provider interval of every such mask is enumerated exactly, then all physical
positions in those intervals are united.  Compressed left-endpoint-range
enumeration agrees with an independent target-local backwards scan.

| Basin | Unique near labels | Provider intervals | Positions | Position file SHA-256 |
|---|---:|---:|---:|---|
| delete p0 | 32 | 33 | 68 | `1bc34078cbd7869f193410c070c48fdcd7078b59a7716bcc414221e0e7f84155` |
| delete p1 | 32 | 33 | 65 | `2caa2ede0f08006ba3e4328e4792af783cfca081426eadc09a16341ce0890965` |
| delete p6435 | 32 | 37 | 85 | `0e07fa8ddd92849ab7a147618c77f2e94d3a98de4da981495d0e545d33ad3d8f` |
| delete p12873 | 32 | 37 | 86 | `952a4a7089918be94656611eee360f7dec1c30d9840649ec71fa709cae5618a4` |
| delete p12874 | 16 | 17 | 52 | `ab9dd48954b37e99f44d798e09b17386863f152ae18c3eb0df70a77e2bcc35f5` |
| five-phase `0x4e63` basin | 16 | 20 | 55 | `16bf51eb5a7351cbc86346378b68233fdffbf8957811871b40e4ebf6545c7502` |

The append-`0x0200` p12874 support is exactly equal to the existing support52
file, so no duplicate was created.  The four new deletion files are intended
for exact-budget `b >= 2` runs of the dynamic affected-witness encoder.

## Lineage warning

The correct current H100 batch lives under
`/dev/shm/k16_insert_basin_20260730/d_{0,1,101,191,192}.*`.  Its basin map has
SHA-256 `6aea820dbf2f9a4f384241fc2b44766361675acb31901e75466597a6bd74e9ba`
and aggregate result has SHA-256
`0575715adfedf16dd6ba72e6d06f418182cb2d28c9c18e44de946080c1f64562`.
Those H100 runs lack per-run command/resource/build manifests, but the new
local independent audit now replays their mathematical conclusions from the
authenticated current bytes.

Do not cite `c_*.word` or `sol_*.stderr` in that directory: they predate the
current upper word and are stale.  Likewise the older
`ad_k16_12874_one_substitution_{exact,independent}` artifacts concern input
SHA `5ac147...`, not this deletion family.

## Audited artifacts

- `scratch/audit_k16_delete12875_and_fivephase_supports_20260730.py`
  - SHA-256 `f914c74fd08d1725748d8e03357fcd5432f32e48c3b95cf135c10673b2b5e29c`
- `scratch/k16_delete12875_and_fivephase_supports_20260730.audit.json`
  - SHA-256 `a979b644f09727b478c7d0ae1fefe9d5c7b46eb0cd0f4b3bcfa66e7c17998603`
  - payload SHA-256 `8575215af7d01ae54a9df53f8a00fdbc95c6c5e086d9459d9efe462852b7ce14`
- `scratch/audit_k16_current_12874_radius1_independent_20260730.py`
  - SHA-256 `ead22926a26db6571936c23dcc30487b31d2aab317be55cdfab4a6ffc7441715`
- `scratch/k16_current_12874_radius1_independent_20260730.audit.json`
  - SHA-256 `42e1f26f5ddee681dfdd303d85b1adb9b51a823b78a89ecd1612ba869e495994`
  - payload SHA-256 `451fdb5afeff638e6164c288f4052535420ca10775e1357c06e9d8ce8a87d802`
