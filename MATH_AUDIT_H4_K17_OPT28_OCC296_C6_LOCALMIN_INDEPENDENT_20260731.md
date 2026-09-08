# Independent replay of the occurrence296 + C6 local minimum

Date: 2026-07-31

Status: **PASS exact sequential replay; FAIL remaining residence and upper completion**.

## Result

The frozen occurrence296 state and the clean 1,160-move residual-C6 candidate
were reconstructed without importing the root materializer or the C++ search
implementation.

All 1,160 advertised moves pass the alternating-C6 formula exactly.  After
every move, every rank-eight port has degree two, the 6,435-object graph is one
cycle, and the fixed 304-object / 4,108-owner marked path is reproduced
literally.  The final 4,872 residual assignments agree independently with all
three saved representations: the candidate, the verified residual, and the
transparent final state.

The final literal reconstruction has:

| quantity | exact value |
|---|---:|
| rank-nine owners | 24,310 distinct |
| lower-q1 colours | 24,310 distinct |
| marked D2 / D3 | 0 / 0 |
| complement D2 / D3 | 230 / 94 |
| strict nonflat D2 / D3 | 503 / 503 |
| inverse replay mismatches / missing bits | 748 / 776 |
| empty envelope cells / minimum size | 0 / 6 |
| host redundancy / envelope volume | 252,803 / 150,224 |
| upper holes r10 / r11 / r12 / r13 | 1,585 / 824 / 116 / 0 |

The independently written owner cycle is byte-identical to the root
materialization, SHA-256
`a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49`.
The independent nonflat row has SHA-256
`abfaab6541ee7d56cb11d5b208fbf4a34da214734113e399d15a355222d418a8`.

## Parent comparison

Negative deltas are improvements.  The exact comparison is:

| metric | occurrence296 parent | pure-C6 escape8 parent | combined child |
|---|---:|---:|---:|
| component-interior floor | 296 | 724 | 296 |
| complement D2 / D3 | 848 / 561 | 407 / 81 | 230 / 94 |
| strict D2 / D3 | 1,875 / 1,874 | 1,029 / 1,029 | 503 / 503 |
| replay rows / missing bits | 2,769 / 2,901 | 1,571 / 1,651 | 748 / 776 |
| upper r10 / r11 / r12 / r13 | 1,908 / 929 / 149 / 2 | 1,576 / 775 / 116 / 3 | 1,585 / 824 / 116 / 0 |
| upper q1--q3 total | 2,986 | **2,467** | **2,525** |

Thus the combined child contracts strict residence and inverse replay against
both parents.  It is **not** an all-coordinate contraction relative to the
latest pure-C6 parent: q1--q3 upper holes are worse by 58, and complement D3
is 94 rather than 81.  No informal “Pareto” label is valid for the whole
vector.

## Bound inputs

- occurrence296 search state: `a973d3bff87a4ae751f100c9548df4b5fb4bd8b786d20ecb2c970f5622f54097`
- transparent final state: `df816a09b5d0f1b2336e611ace3595298286116f3664c11556dbe25efd6d1321`
- clean candidate: `960ca8df23e7c4ea28c6381e6642b4ec1ab86288a57329115d72182e56be949c`
- verified residual: `6fcc91d45b2090b26b612020340a21088a2367c5c0bccd10d3d3614042c60fe4`, payload `c92b72db852a8362a2f99c8091dec072ef42af831e1ef83af5381375d6d2a6e4`
- occurrence296 flow: `079f5cd96f713ef2d72dd43acff10f84416acdb670aeff96f61a3cb97f29c25f`
- occurrence296 residual parent: `63b49db80ad983bcd440aba3ac4b449888e30dea2d3c83e140e15b07082f69d0`
- pure-C6 escape8 materialization audit: `24ac9474dfd605c356b4f596e5d79a49f664ef68319d97b04c13f83384ad056c`

The earlier `occ296_c6_iter104` monitor file was malformed and is not an
input to this certificate.

## Frozen independent artifacts

- checker: `scratch/h4_independent_audit_k17_opt28_occ296_c6_localmin_20260731.py`, SHA-256 `0be596135bffc24bafcbfb8363559670c67965976e27acf0f8901b4ee7371218`
- audit JSON: `scratch/h4_k17_opt28_occ296_c6_localmin_independent_20260731.audit.json`, SHA-256 `0bca08d71f42db8fc97ff599328fd725c32abb0de2c30396ce72bf70374d32a4`, payload `1466d61c961b3343151fa0e84fea2b6a9edce6d8b4bbf498ce751041eef1cc91`
- owner cycle: `scratch/h4_k17_opt28_occ296_c6_localmin_owner_cycle_20260731.word`, SHA-256 `a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49`
- nonflat row: `scratch/h4_k17_opt28_occ296_c6_localmin_zrow_20260731.word`, SHA-256 `abfaab6541ee7d56cb11d5b208fbf4a34da214734113e399d15a355222d418a8`

Two consecutive runs produced identical JSON, owner-cycle, and nonflat-row
hashes.  No common-cap assignment, compiler, K17 word, or value of
`nu(17)` is claimed.
