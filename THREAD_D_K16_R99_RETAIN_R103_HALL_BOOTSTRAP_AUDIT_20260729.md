# Thread D: retain-r103 Hall-bootstrap audit (2026-07-29)

## Result

The retain-r103 checkpoint can be used as a fail-closed Hall-history
bootstrap for the current r99 cut master.  The reusable source is

`scratch/threadD_prepare_k16_r99_retain_r103_hall_bootstrap_20260729.py`.

It is a provenance-locked specialization of the frozen r43 adapter.  It does
not build or solve a CP-SAT/SAT/LP model.  On explicit materialization, the
base adapter reconstructs the physical catalogue solely to replay the rows.

## Exact census

The authenticated checkpoint is

`scratch/k16_r99_joint_guarded_upper4_retain_r103_native_20260729.json`,

with file SHA-256
`b005a07ce33382e0d15e5fd86394164460338c9fa2d8839fd2bc699d739d6982`
and embedded payload SHA-256
`b3a4dd5e0c7c6ceb244e3ad830613a232f8721c534f8f944e46f05f021aa6b38`.
It contains 103 rounds, 142 same-palette Hall rows, and 103 joint-cover rows.
All Hall-row digests and all joint-row digests are individually distinct.

The sorted Hall-digest ledgers have the following newline-delimited hashes:

- frozen retain-r43, 86 rows:
  `20f57be716841e499b2afae48dd1b5d9ab6bfb844583b6820fc7eebbf06b1252`;
- retain-r103, 142 rows:
  `04f82e3f1869e329ee78a5a3c4b0620a70f8ed796f776614d7457fa1f39eb5bd`;
- the set difference, 56 rows:
  `849f986542dcfe4f150dc8191c28ecb3206b90b0ddc2d291cf9dd0801fab4b3a`.

The r43 Hall set is a subset of the r103 Hall set.  Therefore the two
current eager portal-Hall rows already found in the audited r43 replay remain
present exactly once in r103.  The other 140 historical Hall rows are the
only rows exported in `learned_portal_hall_rows`.  Materialization revalidates
all 142 physical portal unions and fails if this census changes.

## Upper4 and joint-row scope

The r103 producer predates the explicit `exact_add_hall_audit` field: both it
and its digest are null.  Consequently the filename's `upper4` token is not
accepted as evidence that the certified upper4 row was active.

The adapter reconstructs the current upper4 endpoint-cover inequality from
the frozen theorem audit:

\[
  \sum_h |\operatorname{ends}(h)\cap P|x_h
  \;\ge\;
  x_{4742}+x_{22511}+x_{23229}+x_{24034},
\]

where the four upper colours are
`(1,1883),(1,1907),(1,3255),(1,5939)` and `P` is the certified 26-node
endpoint cover.  No historical r103 Hall row selects exactly this four-colour
set.  No historical joint row has zero constant, so none is the same linear
row.  These zero-equivalence counts are asserted again after semantic replay.

All 103 historical joint rows are ignored.  They are neither copied to the
v4 checkpoint nor translated into Hall rows.  The current upper4 row appears
in the authenticated endpoint-cover hook and is independently reconstructed
as an eager production-driver input; the hook itself is explicitly marked
`DORMANT_NOT_CONSUMED_FROM_RESUME`.

## Fail-closed conditions

The wrapper rejects any change to the r103 bytes, embedded payload, source,
producer hashes, row counts, row-digest uniqueness, branch, or null upper4
metadata.  It accepts only `--branch retain`, erases the base adapter's delete
entry, and verifies that importing both adapter layers does not import
OR-Tools.  The frozen r43 source and artifacts are unchanged.

Only syntax compilation and solver-free static JSON/digest checks were run
locally.  No catalogue materialization, model construction, or solve was run
for this audit.
