# K16 upper-12,874 certificate and exact gap-one shortening frontier

Date: 2026-07-30

Status: authenticated upper certificate; exact scoped shortening no-gos;
the unrestricted length-12,873 problem and the 17-cell image-collar formula
remain unresolved unless a later retained solver artifact says otherwise.

## 1. Corrected frozen headline

The word

```text
answers/k16_upper12874.word
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

has length `12874` and literal contiguous-OR coverage `65535/65535` under
two independent start/end replays.  Hence

\[
                         12873\le \nu(16)\le12874.       \tag{1.1}
\]

The construction exposes the 18 positions in the `(5,9,4)` collar

\[
[0,5)\;\cup\;[6436,6445)\;\cup\;[12870,12874).
\]

Exactly **12** values differ from the append-`0200` source and **6** retain
their incumbent values.  The changed positions are

\[
0,1,3,4,6436,6438,6439,6440,6442,12871,12872,12873.     \tag{1.2}
\]

Thus the earlier wording “14 of 18 values differ” is false.  This correction
does not change the word, its hash, its literal verification, or (1.1).
The full 18-row decoded ledger is in

```text
MATH_THEOREM_AD_K16_UPPER12874_PHASE_COLLAR_CERTIFICATE_AUDIT_20260730.md.
```

## 2. Complete one-step shortening censuses

Every one of the `12874` pure deletions was evaluated by the exact
multiplicity identity that subtracts intervals containing the deleted cell
and adds intervals crossing the new seam.  No deletion is universal.  The
unique optimum deletes zero-based position `1`, whose value is `0x2800`, and
produces

```text
scratch/k16_upper12874_best_delete.word
SHA-256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

with sole hole

\[
                              h=0x2c6d.                 \tag{2.1}
\]

The authenticated census is

```text
scratch/k16_upper12874_deletion_census.audit.json
SHA-256 c2990f25c9ef15d7c3a4ddc5eda5f5ca4ce60e75dabe93dfc8c4988b349cd619
payload b117af6ec989f01ec619c6f9c902ef77a249b4c9abd4f40164c3b6199f3cc995.
```

More strongly, replace any adjacent pair by one arbitrary nonzero mask.  An
exact all-boundary argument covering every replacement value again finds no
universal length-12,873
word:

```text
scratch/k16_upper12874_arbitrary_two_to_one_fusion_census_20260730.audit.json
SHA-256 9c9451aa69f80778ec0843dbb4471757ce779d9678a43ed6f97161a99bf7597a
payload 02ecfdcdd561fd7bd727154ade27eb3bb561f60404da9ae94409e92390ba9861.
```

This closes all adjacent two-to-one fusions, not nonadjacent deletion plus
arbitrary rethreading.

### Theorem 2.1 (all low-hole delete-plus-one-edit basins)

The deletion census has exactly seven basins with at most three holes:

```text
deleted position   holes
0                  18553,26745
1                  11373
3                  5229,21613
6389               18041,27233,27489
6441               37997,43117,54381
12871              35943,36071,48367
12873              52833,52835
```

For each fixed basin, latest-start/earliest-end witness extrema identify
exactly the targets whose every old witness meets a proposed edit position.
The replacement value must be a nonzero submask of their intersection, and
the exact left-suffix/right-prefix join then decides whether it supplies all
of them.  This evaluates every arbitrary nonzero one-cell replacement,
while eliminating other values by a necessary forbidden-bit argument.

Across the seven basins the exact necessary-domain counts are respectively

```text
59604, 77153, 59541, 32958, 55882, 95327, 95291,
```

for `475756` tested replacements total.  No candidate is universal.  The
authenticated report is

```text
scratch/ad_k16_upper12874_lowhole_delete_sub1_20260730/audit.json
SHA-256 5a4f47b1a431241e26b9dfbe8e19af69a6e52d136892c670d131fb45d94740e5
payload f715897ea360dd45d28f05980bf47b9b68d881d4aa150b707df3e0428d6ffa16
status PASS_EXACT_SCOPED_UNSAT_ALL_7_CASES.
```

The bounded H100 run used one CPU, 57,856 KiB maximum RSS, no swap, and
6.15 seconds wall time.  A separate local-light replay checks the report
payload, every materialized basin hash, all seven zero-candidate statuses,
and exhaustive-domain accounting:

```text
scratch/audit_threadD_k16_upper12874_lowhole_delete_sub1_artifact_20260730.py
SHA-256 4985f6b5072e00e8030ea3684989cad3e7468681433097bc3b15ba1395635fde

scratch/threadD_k16_upper12874_lowhole_delete_sub1_replay_20260730.audit.json
SHA-256 7bfe2050e9acae22eed1e4dc18a93fd172e1b02d043c2ec3b4376a125ce8de57
payload 11a3772c2b1f80b584b3c1c1604280e61a6f485979d4bbe02eb5758ab32c6c8d.
```

The replay also confirms that the `475756` tested assignments plus the
common-submask eliminations partition all `5905424385` arbitrary
position/value pairs.  It checks the p1 regression against the older
independent audit but does not recompute all replacement outcomes.

This closes deletion plus one arbitrary substitution only when the original
deletion leaves at most three holes.  It does not close four-plus-hole
basins, two auxiliary substitutions, or nonlocal reorderings.

## 3. Complete radius at most two around the best deletion

At radius one, every one of the `12873` positions and every arbitrary
nonzero replacement in its exact necessary target intersection was tested.
There are `77153` tested values and no completion:

```text
scratch/k16_12873_phase_delete_radius1.audit.json
SHA-256 475f35023004eb7402bfb7da42135b26f277a8bf3ccf3eb904b89af4d31196f2
status EXACT_SCOPED_UNSAT.
```

At radius two there are exactly two witness normal forms for the original
hole `h`.

1. A final `h`-witness contains exactly one edited position.  The complete
   provider-first branch contains `27064` first service rows and `646720`
   compatible second edits.  Its minimum final hole count is two.
2. A final `h`-witness contains both edited positions.  The complete joint
   branch contains `13235` position pairs and `102404745` replacement pairs,
   including synergistic pairs for which neither edit alone supplies `h`.
   Its minimum final hole count is one.

Same-position pairs collapse to radius one, so these two branches together
with the radius-zero/one audit exhaust every endpoint at substitution radius
at most two from the best-deletion basin.  The retained aggregate is

```text
scratch/r_k16_upper12874_delete_radius2_normal_form_20260730.audit.json
SHA-256 6ac56bab32034e179c26a0c3f3b82607c5d33abe94b402ad5e528feeefa8e6d0
payload 76cff97a63e396d2884497532a74edaf187422352c1bd13dcc986c479a49aee4
status PASS_COMPLETE_RADIUS2_NOGO_AND_BEST1_MATERIALIZED.
```

The best radius-two endpoint is

```text
scratch/k16_upper12874_delete_radius2_best1_43117.word
SHA-256 09a60d48584a737f452a5d53c8fadec9b26cdad354f36926fbc5b1b1ceb4d166
```

and has sole hole `43117=0xa86d`.  It changes shortened-word positions
`6439` to `0x206c` and `6440` to `0x046d`.

The aggregate checker binds the enumerator hashes, catalogue sizes and saved
extrema; it does not independently repeat all `102404745` joint outcomes.
Accordingly this is an authenticated exact-enumerator theorem, not a DRAT
certificate.

## 4. Exact 17-cell image-collar decision problem

After deleting source position `1`, the surviving image of the successful
collar is

\[
E=[0,4)\;\cup\;[6435,6444)\;\cup\;[12869,12873),       \tag{4.1}
\]

of widths `(4,9,4)`.  Freeze every position outside `E` and allow every
position in `E` an arbitrary nonzero 16-bit value.  Fixed-gap ORs imply that
each vulnerable proper target has a witness in one collar plus only its
adjacent fixed suffix/prefix.  Therefore the retained CNF is satisfiable if
and only if this entire 17-cell fibre contains a universal word.  It is not
an edit-radius relaxation: it includes arbitrary multicell fusion, synergy,
and every braid sequence whose final support is contained in `E`.

The exact model has

```text
57 vulnerable targets
461 legal interval patterns
272 cell-bit variables
4467 witness variables
4739 total variables
145704 clauses
2095906 DIMACS bytes.
```

Frozen deterministic artifacts are

```text
scratch/ad_k16_12873_phase_fusion_4_9_4.cnf
SHA-256 206581940afea13d9be331cf4d44f028dda9f79c7ffc705dea3dd2a1c928cf80

scratch/ad_k16_12873_phase_fusion_4_9_4.cnf.map.json
SHA-256 eb6f43d2b1a1b4838a6c5553840936a497abb8b4e57bccac8da6291bac378ac5
payload 31fa0be6295651058e4bc9e8057fbe868c97c0edd630d29423440996f9493b46
```

An independent deterministic reconstruction reproduces the DIMACS hash.
The missing target `h=0x2c6d` has exactly 65 compatible interval forms:
the `10`, `45`, and `10` nonempty contiguous subblocks of the three collars.
All have fixed outside OR zero.  This gives a complete 65-shard separator
that pins one exact `h`-witness while leaving all other editable cells free.

As of this note's freeze, one bounded CaDiCaL proof run ended with timeout
exit `124` and an incomplete proof stream.  Four further 30-minute CaDiCaL
seeds and one 30-minute Kissat seed also ended without a SAT/UNSAT status;
the bounded CP-SAT run remains live.  No retained run has returned a
conclusive artifact.
Therefore the formula's mathematical status is **UNKNOWN**.  A timeout,
resource exit, or unfinished proof stream is not UNSAT.

Any SAT assignment must be decoded and independently replayed on all
`65535` targets before it proves `nu(16)=12873`.  Any UNSAT claim must retain
and independently check a complete DRAT/LRAT proof.  Even a proof of UNSAT
would close only this 17-cell image collar, not all length-12,873 words.

## 5. Sharp remaining scope

The following are now exactly closed:

* every pure deletion of the authenticated upper word;
* every adjacent arbitrary two-to-one fusion of that word;
* every arbitrary one-cell continuation of each of the seven deletion
  basins having at most three holes;
* every arbitrary substitution endpoint at radius at most two from the
  unique best-deletion basin.

Still open are:

* the full `(4,9,4)` image-collar formula until a conclusive retained result;
* the sibling fixed-gap shortenings `(5,8,4)` and `(5,9,3)`, whose exact
  finite reductions are built but have no conclusive retained verdict;
* delete-plus-rethread basins rooted at nonminimum deletions beyond whatever
  separately retained exact censuses establish;
* arbitrary support outside the fixed-gap architecture;
* the global equality question `nu(16)=12873`.

No result in this note changes the authenticated gap-one bracket (1.1).

For completeness, a solver-free common reduction has since rebuilt all
three fixed-gap profiles using target-intersection closure and maximal
fixed-context dominance.  They share the same 57 repair targets and have
the following exact equisatisfiable dimensions:

```text
profile   variables   clauses
4/9/4       3977       124558
5/8/4       3749       109268
5/9/3       4034       127201
```

The reduction audit is

```text
scratch/k16_12873_three_profile_closure_model_20260730.audit.json
SHA-256 2753f984a606bee946423e1296198a80ff0f0c497c9c05cda3798606af0ce892
payload d33f79a5dbbc002471828cd286a482609b5780ec032daf13dc966f58252c0b47.
```

These dimensions are reductions of the full arbitrary-value fibres, not
solver verdicts, and the three-profile trichotomy retains both fixed gaps.
