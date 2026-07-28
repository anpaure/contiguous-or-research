# k=15 relabel-index audit

Date: 2026-07-28

Scope: the current Hall-29 relabel screen, its two frozen winner files, the
four-parent compiler artifacts built from the first winner, and the current
2026-07-28 mathematical notes which name that winner.  No active search file
was edited.

## 1. Authoritative convention and direct replay

`scratch/screen_k15_transposition_parents.py` loops

```python
for left in range(15):
    for right in range(left + 1, 15):
```

and `transpose_mask` shifts by `left` and `right`.  Its stored labels are
therefore **zero-based bit positions**.  Thus the frozen winner

```text
scratch/k15_transposition_parent_winner.json
transposition = [1,12]
```

is the mathematical one-based coordinate transposition `(2,13)`, not
`(1,12)`.

An independent replay from
`scratch/k15_doubletrans_05_213_hall29.json` gives:

| interpretation | equality with frozen winner | differing path positions |
|---|---:|---:|
| swap bits `(1,12)` = coordinates `(2,13)` | yes | 0 |
| swap bits `(0,11)` = coordinates `(1,12)` | no | 5,016 of 6,435 |

The SHA-256 of the compact JSON serialization of the correct winner middle
path is

```text
ee3dfb2ab0061551d2e204901b707d69f72c5fbdd12604500c022f6f9f90fefc
```

whereas the bits-`(0,11)` path has compact-middle hash

```text
5dcf1b56725123712f0442dd1ab8e3d67cf574bc87d4645aee262bc93e8157f6
```

The wrong one-based interpretation is not a second good screen winner.  Its
actual screen row is zero-based `[0,11]`, with old-zero count vector

```text
(0,1,0,0,0,2,0),
```

so it misses five of the seven frozen zeros.

## 2. One materially contaminated artifact

The file

```text
scratch/threadD_A29_4parent_payload.json
```

is built with the wrong interpretation.  It explicitly stores
`tau_one_based:[1,12]`, names its fourth parent `tau(1,12)H29`, and its fourth
indexed path begins

```text
(2003,397,293,181),
```

which decodes (using the increasing list of rank-eight masks) to

```text
(11948,3757,3247,2479).
```

Those are exactly the first four masks obtained by swapping bits `(0,11)`.
Its union has 18,814 directed arcs.  This payload must be quarantined and must
not be used as the canonical four-parent catalogue.

The corrected replacement already exists:

```text
scratch/threadD_A29_4parent_laneI_payload.json
```

It stores both

```text
tau_zero_based:[1,12]
tau_one_based:[2,13]
```

and its fourth indexed path begins

```text
(1519,397,1063,881),
```

decoding to the authoritative winner prefix

```text
(9901,3757,7341,6573).
```

Its union has 18,753 directed arcs.

The later named Thread-D outputs are on the corrected branch, not descendants
of the contaminated payload:

- `threadD_A29_4parent_laneI_static_audit.json` names
  `tau_zero(1,12)H29`;
- `threadD_A29_4parent_regression.json` explicitly records
  `threadD_A29_4parent_laneI_payload.json` as its payload;
- `threadD_A29_4parent_fixedH29_t1495.json`,
  `threadD_A29_4parent_fixedH29_t1496.json`, and
  `threadD_A29_4parent_fixedH29_t1524.json` all name the corrected parent and
  use the 18,753-arc / 1,610,645-pattern Lane-I catalogue.

No checked source file hard-codes a bits-`(0,11)` reconstruction of the frozen
winner.  The bad payload appears to have been made by an unretained inline
builder.  Any currently running or remote job should nevertheless be checked
for the literal input filename `threadD_A29_4parent_payload.json`.

The ten canonical two-parent exact-boundary-upper exclusions are also clean:
their `scratch/exactdm_pair*_boundaryupper.log` records name the frozen parent
JSON files directly.  In particular pairs `03`, `13`, `23`, and `34` consume
`k15_transposition_parent_winner.json`, never the contaminated Thread-D
payload.  Their infeasibility conclusions therefore survive this audit.

## 3. Correct frozen artifacts with ambiguous names

These artifacts are data-correct despite the shorthand `t1_12`:

- `scratch/k15_transposition_parent_winner.json` is exactly the zero-based
  `[1,12]` replay;
- `scratch/t1_12_h29zero7.interior.tsv` has all 6,434 edge records equal to
  the correct winner's directed path edges (only 809 overlap the wrong path);
- `scratch/directed2930314_t1_12_multi_A29_R3_R4_T29.p3.tsv` contains all
  6,434 correct-winner edges as its fourth-parent contribution;
- all five `scratch/directed_union_4p_t1_12zero7_hint3.round*.json` files name
  `k15_transposition_parent_winner.json` in `sources`; round 0 is literally
  the correct winner path;
- `scratch/k15_transposition_parent_winner.canonical_dm.json` and
  `scratch/k15_transposition_parent_winner.dm_witness.json` name the correct
  winner as source;
- `scratch/k15_accumulated_zero_parent_screen.json` uses the correct winner
  file as its fourth parent.

Do not rename these frozen files without also updating their reference and
hash ledgers.  The safe repair is a convention sidecar or new metadata, not a
silent rewrite.

## 4. Stale mathematical notation

The following notes use `(1,12)` as if it were ordinary one-based
mathematical coordinate notation while attaching data from the zero-based
screen winner.  Their structural theorems are unaffected, but their explicit
parent labels must be changed to `(2,13)`, or else written unambiguously as
`[1,12]_0`.

1. `MATH_ATTACK_R_K15_SMALL_FAMILY_FIFO_RESIDENCE_COUPLING_20260728.md`:
   lines 10, 876, and 1015.  Its line 955 old label `(10,11)` likewise means
   `[10,11]_0=(11,12)_1`.
2. `MATH_ATTACK_W_K15_CAA29_FINITE_MOVING_DM_SEARCH_UPDATE_20260728.md`:
   lines 57--60.
3. `MATH_ATTACK_W_K15_CAA29_FINITE_PACKET_CERTIFICATE_20260728.md`:
   line 77.
4. `MATH_ATTACK_W_K15_PARENT_HAMILTON_ENTROPY_COMPRESSION_20260728.md`:
   lines 72--86, 167, and 810.
5. `MATH_K15_L_RESIDENCE_SAFE_COMPILER_MOTIF_HALL_20260728.md`:
   lines 118, 124, 581, and 650.  Its fifth-parent labels on lines 131, 136,
   582, and 666 also need `[5,7]_0=(6,8)_1` if one-based notation is intended.
6. `MATH_LANE_B_K15_COORDINATE_RELABEL_PARENT_COVER_DESIGN_20260728.md`:
   lines 179, 738, 861, 1102, and 1107, together with the other screen labels
   listed below.

For all four first-screen positives, the complete conversion is

| stored screen label | one-based mathematical label |
|---|---|
| `[1,12]_0` | `(2,13)_1` |
| `[3,4]_0` | `(4,5)_1` |
| `[10,11]_0` | `(11,12)_1` |
| `[3,13]_0` | `(4,14)_1` |

The accumulated-zero winner converts as `[5,7]_0=(6,8)_1`.

`MATHEMATICAL_HANDOFF.md`, item 1463, already states the convention correctly
and should be treated as the authoritative prose correction.

## 5. Exact file hashes

```text
5516482eadaba4f8fb9549b41c79c3b949df2e3224ce68f9dacd3b5b6bc2d21c  scratch/k15_doubletrans_05_213_hall29.json
45e12373e33ed714b29612db88194798597e0a5d9bdea27093b8b3ccf48d0522  scratch/screen_k15_transposition_parents.py
eccfb6c9cd3d97392ef16bcf3ed0332d4bad2a9f9ca33d41538ca3a56b7a587c  scratch/k15_transposition_parent_screen.json
8d0f732c28a552e919857b1a1c80794ac65f390816d2b89b66a67ed63475d2dd  scratch/k15_transposition_parent_winner.json
7c472a1a98f8d43f114e6b973ffe3b7b0f8e1aa8cee8f7e3d3f590b03b65b9db  scratch/t1_12_h29zero7.interior.tsv
726548e2d9fd5219a283e89f365c9676144b17a4d48851ec875c6a6cbc3020eb  scratch/directed2930314_t1_12_multi_A29_R3_R4_T29.p3.tsv
d17b69e4385cdef7c5c74db074f39c38b2451ab3cb24ccd4156d7b4c4a727df9  scratch/threadD_A29_4parent_payload.json              [WRONG INDEX BASE]
cd754db2437b572a5d64642a362f4a662f7d93acaff5cd0cc075795df4d85287  scratch/threadD_A29_4parent_laneI_payload.json        [CORRECT]
```

## 6. Required corrections

1. Quarantine the one contaminated payload and ensure no local or remote
   command consumes it.
2. Use `threadD_A29_4parent_laneI_payload.json` for the corrected four-parent
   exact-DAG/CP-SAT lane.
3. Make every future generated transposition artifact carry both
   `transposition_zero_based` and `transposition_one_based`; patch both screen
   generators accordingly before regenerating frozen outputs.
4. Correct the six stale notes by either translating every screen tuple to
   one-based notation or adding one explicit global declaration that all
   displayed screen tuples are zero-based.  Translation is preferable in
   documents formulated over `[15]`.
5. Preserve the existing correct frozen JSON/TSV files and their hashes; their
   ambiguity is nomenclature, not data corruption.

No pre-existing `.sha256` manifest dedicated to the Thread-D payload pair was
found.  The hash table in this audit is therefore the first durable distinction
between the contaminated and corrected payloads; any future certificate
manifest should carry the corrected payload hash `cd754db2...` and exclude the
contaminated hash `d17b69e4...`.
