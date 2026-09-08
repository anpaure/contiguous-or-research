# Audit of the corrected K16 upper-12,874 edit ledger

Date: 2026-07-30

## Exact scope

This note audits only the source-relative edit ledger for the authenticated
`(5,9,4)` phase-collar word.  It does not re-prove the SAT-model equivalence
or the literal coverage theorem.

The two compared words are

```text
source    scratch/k16_append0200_12874_onehole.word
          SHA-256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18

candidate answers/k16_upper12874.word
          SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

Both contain exactly `12874` whitespace-delimited masks.  The editable set is

```text
0, 1, 2, 3, 4,
6436, 6437, 6438, 6439, 6440, 6441, 6442, 6443, 6444,
12870, 12871, 12872, 12873.
```

It has size `18`.

## Independent source-to-candidate replay

Direct token comparison gives the exact changed set

```text
0, 1, 3, 4, 6436, 6438, 6439, 6440, 6442, 12871, 12872, 12873,
```

of size `12`, and the exact retained editable set

```text
2, 6437, 6441, 6443, 6444, 12870,
```

of size `6`.  No position outside the 18-cell collar changes.  Therefore the
correct ledger is

```text
18 editable = 12 changed + 6 retained.
```

The phrase “14 changed” is false relative to the authenticated append-`0200`
source.

## Agreement of retained artifacts

The primary decode audit

```text
scratch/ad_k16_upper12874_phase_collar_5_9_4.decode.audit.json
SHA-256 44b57f68223fff0cfab0d3dedafad4f4835c86db3e5085aca6776fa96e418a26
```

contains 18 replacement rows; exactly 12 have `old != new` and exactly 6 have
`old == new`.

The independent replay audit

```text
scratch/ad_k16_upper12874_phase_collar_independent_20260730.audit.json
SHA-256 dc800a738a0c771a50c01dd9b8cfb39df6e3b4e25769f713814d0926b5b458ea
```

records

```text
model.editable_cell_count             18
decode.actually_changed_cell_count    12
decode.unchanged_editable_cell_count   6
```

and retains the canonical answer SHA-256 above.  Thus the correction changes
only the prose ledger; it changes neither the word nor either retained audit
artifact.

## Prose-scope audit

The current repository surfaces are already consistent:

* `MATH_THEOREM_AD_K16_UPPER12874_PHASE_COLLAR_CERTIFICATE_AUDIT_20260730.md`
  states 18 editable cells at lines 55--56, lists the full ledger at lines
  100--121, and states 12 changed plus 6 retained at lines 123--124.
* `RESEARCH_INDEX.md` states 18 editable positions and 12 actual changes at
  lines 11--13.
* `MATHEMATICAL_HANDOFF.md` lines 99--106 identify the correct word, hash,
  `(5,9,4)` construction, and certificate without asserting an edit count.
* `THREAD_A_K16_GAP_ONE_DELETION_FUSION_AND_DYNAMIC_COLLAR_REDUCTION_20260730.md`
  states the exact 12-position changed set at lines 41--45 and explicitly
  rejects “fourteen of eighteen changed” at lines 53--55.
* `THREAD_D_K16_UPPER12874_GAP_ONE_SHORTENING_FRONTIER_20260730.md` states
  `12` changed and `6` retained at lines 25--39.
* `THREAD_K_K16_CLOSURE_NORMALIZED_THREE_PROFILE_COMPRESSION_20260730.md`
  states exactly 12 changed cells at lines 30--33.

A repository-wide targeted search found no surviving positive claim that this
candidate changes 14 of the 18 editable cells.  Matches to that wording are
explicit corrections, not stale assertions.  No canonical file requires a
ledger correction as of this audit.
