# K=16 compound radius-three one-hole basin audit (2026-07-30)

## Result

A new length-12,873 basin was obtained from the reverse blocker annealer by a
finish edit followed by the exact two-edit provider census.  It is not a
universal word: its sole missing OR is `43117 = 0xa86d`.  It is nevertheless
useful because it is a genuinely different low-defect basin, 43 positions
away from the previous `43117` joint-pair basin.

Authenticated word:

- `scratch/k16_compound_rev_provider_auth.h1.0.word`
- length: `12873`
- canonical SHA-256:
  `a92509fd4f60490588973e7a70d457b369e4b0192a65f3de7adef105727e33fa`
- missing masks after a fresh all-65,535 replay: `[43117]`

## Exact compound ledger

The immediately preceding two-hole state was:

- `scratch/rex3_rev_h3_finished.word`
- length: `12873`
- canonical SHA-256:
  `35857a7ac9793df18503119b657eed893b710ac0b140eff3e3e5b08ddb188833`
- holes: `[18553,26745]`

The exact provider census applied precisely these two substitutions (zero-based
positions):

| position | old | new |
|---:|---:|---:|
| 0 | 11373 | 18553 |
| 6440 | 32873 | 1097 |

The resulting word differs in 44 positions from
`scratch/k16_upper12874_best_delete.word` and in 43 positions from the old
joint-pair `43117` basin.  Thus it is not a whitespace or serialization copy
of a previously saved state.

## Independent replay boundary

The low-hole rows in the C++ exact-search audit were materialized and replayed
by a separate Python implementation using the distinct-suffix OR recurrence:

```text
python3 scratch/postprocess_k16_compound_radius3_audits_20260730.py \
  scratch/rex3_rev_h3_finished.word \
  scratch/k16_compound_rev_provider.audit.json \
  scratch/k16_compound_rev_provider_auth --max-holes 1
```

Output (abridged only for line wrapping, not mathematically):

```json
{"authenticated_candidates":[{"audit_row":0,
  "sha256":"a92509fd4f60490588973e7a70d457b369e4b0192a65f3de7adef105727e33fa",
  "missing":[43117],
  "edits":[{"position":0,"value":18553},
            {"position":6440,"value":1097}]}]}
```

The complete machine-readable record is
`scratch/k16_compound_rev_provider_auth.authentication.json`.

## Scope and next test

This is a search advance, not an upper-bound improvement.  Exact provider and
joint radius-two searches rooted at this new basin were launched on the H100
CPU.  A zero-hole result from either lane must again pass an independent full
65,535-mask replay before it is promoted to `answers/`.

## Finish-readiness correction

For all subsequent blocker work, raw interval multiplicity must not be called a
reserve.  A finish at position `p` destroys every witness interval containing
`p`; only witnesses whose intervals avoid `p` survive.  In particular, a later
one-hole state derived from the long forward anneal had raw multiplicities
`mult(18553)=1`, `mult(26745)=2`, but **both external multiplicities relative
to p=0 were zero**.  Replaying the p=0 finish therefore left both masks absent.

The corrected annealing statistic is the p-external witness count for each
blocker, with finish readiness requiring at least one external witness for
each.  Machine record:
`scratch/k16_Hfinal_doubleblocker_h1b3.audit.json`.

## External-witness state and exact donor atlas

Blocker-aware replica exchange subsequently produced an authenticated
38-hole state with genuine witnesses outside the finishing cell:

- word: `scratch/k16_Hfinal_externalblockers_v2.word.blocker2_h38.word`
- SHA-256:
  `575f9e5b3453618636918cb410cff88390e12c2dd09fc4d635820b40e1bd4880`
- blocker `18553`: singleton witness `[111,111]`
- blocker `26745`: singleton witness `[6522,6522]`

A fresh replay gives exactly the 38 masks recorded in
`scratch/k16_Hfinal_externalblockers_h38.audit.json`.  Backtracking one source
witness for each collateral hole localizes their destruction to 12 cells.
However, exact CNF searches prove both the ten-cell repair with the two
planted cells frozen and the full twelve-cell arbitrary-domain repair
unsatisfiable.  Thus a witness at a position outside that causal collar is
necessary for this state.

The exhaustive one-edit provider atlas is:

- generator: `scratch/k16_h38_exact_provider_atlas_20260730.cpp`
- record: `scratch/k16_h38_exact_provider_atlas.audit.json`
- evaluated unique provider edits: `2,046,050`
- edits creating no new private debt: `78`
- frozen positions: `0,111,6522`

The complete list of positions supporting any of the 78 zero-debt moves is
`{666,667,6524,9958}`.  The unique one outside the causal collar is therefore
`6524`.  Consequently the first atlas-prioritized collar expansion is the
causal 12-cell set plus position `6524`.  The one-edit atlas itself freezes
positions `111` and `6522`, but the exact expanded13/expanded14 simultaneous
formulas leave both positions editable as members of the causal twelve.
The next ranked external donor is `668`, whose best edit fills the three
current holes `5677,5933,22317` while creating two debts.  These are search
priorities, not existence claims; every zero-hole candidate still requires
the independent 65,535-mask replay.

## Phase-centred h21 state and monotone-frontier theorem

The causal collar plus donor `6524` is itself exactly UNSAT.  Its focused
anneal nevertheless produced an authenticated 22-hole phase.  An exhaustive
provider atlas for that phase found 46 edits which each fill one hole and
create no new hole.  The lexicographically selected edit was
`position 81: 4384 -> 4128`, producing:

- `scratch/k16_h22_zero_debt_descent.h21.word`
- SHA-256:
  `c0bf592c0f8082afe0af24648f7ab393c204db70692ecb948922ff7448f9b890`
- exactly 21 missing masks under an independent replay
- planted singleton witnesses at positions `111` and `6522` unchanged

All 46 first edits were then swept independently.  After every one, the exact
provider enumeration found no second zero-debt edit.  Therefore there is no
two-step monotone zero-debt path from this h22 phase.  Any continuation must
temporarily create a private debt or use a simultaneous compound edit.  The
complete 46-way evidence archive is
`scratch/k16_zd_choice_sweep_evidence.tar.gz` (SHA-256
`b2ea515c4fc1c19b9528e3c0b93cc406f154450d263a7e957f2fbb48eede2fa1`).

At the selected h21 state there are exactly nine provider edits with at most
one new private debt: one transfer at position `6523` and eight values at the
new donor position `6552`.  All nine were swept exactly.  Every resulting
h21 state has no zero-debt continuation.  Hence the one-debt frontier is also
closed under a following monotone repair; the next successful compound move,
if any, must carry at least two simultaneous debts.  Evidence archive:
`scratch/k16_h21_debt1_sweep_evidence.tar.gz` (SHA-256
`988873be22109bcb41954016dd6aabf44f634e4c6ab8c9792f39f18496bee5b5`).
