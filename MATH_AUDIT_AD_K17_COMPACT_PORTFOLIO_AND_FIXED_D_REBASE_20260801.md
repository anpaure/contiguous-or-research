# Audit: K17 compact portfolio and fixed-`D` staged rebase

Date: 2026-08-01

## 1. Verdict

The exact 613,656-variable compact projection was run independently with
Kissat and CaDiCaL for 1,200 seconds per solver.  Both runs terminated
authenticated `UNKNOWN`: neither emitted a SAT nor UNSAT line, no assignment
was obtained, and neither partial DRAT is a certificate.

The runtime result proves nothing about feasibility, even inside the frozen
loopless `Z_17` fixed-MASS age-bimatching skeleton.  It does justify a
nonduplicate structural rebase.  The strongest current exact next face fixes
only `D`, leaves ages and `H` variable, and adds upper-q1 directly over the
existing `H` variables.  It has 510,712 variables and 3,035,548 clauses.

## 2. Authenticated compact instance

Remote package:

```text
/home/amodo/or15/work/ad_k17_age_compact_929df903_5d4e717d_20260801
```

Inputs:

```text
p cnf 613656 3240006
9c431267864a819d1a58079ee50aea557279a17bda61dbfd97aecbb680a9c719  compact.composed.cnf
9255e0a94e0a278a9e92990b8534ee4d7ee7a96eebbe56631df1205adef31950  base.direct.map.tsv
6f77724052a0dad8571a5bc5b3177bc4c74077be9e698e2a44e38e74eba63dd1  rootfree.rank10.layer.map.tsv
aeae2850e0491ace333f8cba8958be165dd24ba7a3dea130a39507c8bbd8fe6e  Kissat 4.0.4
49c86c5f8447d768906dcd12d62fb4752e80a48a0d52bbc633929f32eec00b3d  CaDiCaL 3.0.1
```

The compact formula is projection-equivalent to the old staged-rank7/eager-
rank10 formula on the owner types, ages, survivor state and `D/H` incidence
variables.  This is a theorem about the stated semantic projection, not a
claim that either CNF has been decided.

## 3. Terminal compact telemetry

Round directory:

```text
/home/amodo/or15/work/ad_k17_age_compact_929df903_5d4e717d_20260801/solve_round0_compact_9c431267_20260801T1403Z
```

### Kissat

```text
core / seed             24 / 1712529
interval                2026-08-01T14:05:43Z--14:25:43Z
authenticated status    UNKNOWN
SAT / UNSAT lines       0 / 0
conflicts               8,429,933
decisions               410,871,771
propagations            10,877,222,102
remaining variables     302,922 (49%)
wall / process          1200.03 / 1199.69 seconds
peak RSS                436,976 KiB
partial DRAT bytes      2,414,427,602 (noncertifying)
```

Hashes:

```text
40a9d02b14b20ca6abe979866db1a01e2d75ade1f4d7f00de2c455c4fa19280d  solver.status.json
8d65a4b9eb195d5e86030347c80f76cf5f23d651a73643a82581979d2548c6bb  authenticated.status
79ea29a88fa9c6096ac0bcd06547fcb5449d37548ecb2d55815406cf2039d77f  solver.stdout.log
012219dc5b652ac0019e5d7405a2b78f474bcc56a7004bc68c62706032d47c1b  solver.resource.log
```

### CaDiCaL

```text
core / seed             25 / 1712530
interval                2026-08-01T14:05:43Z--14:25:43Z
authenticated status    UNKNOWN
model status            literal c UNKNOWN
SAT / UNSAT lines       0 / 0
conflicts               2,904,430
decisions               69,872,931
propagations            4,222,050,427
fixed / eliminated      102,358 / 125,035
wall / process          1200.17 / 1196.78 seconds
peak RSS                1,174,880 KiB
partial DRAT bytes      8,481,306,633 (noncertifying)
```

Hashes:

```text
1be2bd131a5434580db01d41baab5686642afe292d5c83a036273bb1ec21287a  solver.status.json
8d65a4b9eb195d5e86030347c80f76cf5f23d651a73643a82581979d2548c6bb  authenticated.status
d7ac588af48bd31dedd31c9710571058b6f13acbd1ccf270fbaf5aec036664ce  solver.stdout.log
6daa5e5439f760c3acb5b76917b5310cff7c4f9c62c007e8a7532db60ebe041e  solver.resource.log
```

Postprocessing is SAT-only, so correctly no rank-7 literal replay, topology,
voltage, residence or trim-3 output was produced.

## 4. Exact fixed-`D`, variable-age face

Let `B` be the authenticated compact base

```text
fc6dbf2469502e2e02be7818074e18ebcecd65403268e713917820515688c4f7  base.direct.cnf
p cnf 510712 3032974
```

and fix one selected perfect matching `D_0` with its 1,430 positive literals.
At a quotient facet the selected `D_0` edge fixes the physical tail.  Hence
every possible `H` incidence has a fixed rank-10 union colour even though
the age state remains variable.  The base already enforces every age bridge,
both perfect matchings and the loop exclusions.  Therefore adding one ALO
over the eligible existing `H` variables for each of the 1,144 colours is
exact.

Emitting the assumptions as units gives

```text
510712 variables
3032974 + 1430 + 1144 = 3035548 clauses.
```

A verified UNSAT certificate for this face justifies exactly the outer cut

```text
OR_{d in D_0} not D_d.
```

It excludes this `D_0` through every age state.  `UNKNOWN` yields no cut.

The append-only layer builder is

```text
scratch/build_ad_k17_fixed_D_variable_age_rank10_layer_20260801.cpp
SHA 6b4a10577717a26886bc6529df136490794bc6459c49612e8ad748a6799a7b6e
```

It was source-audited after correcting two quotient subtleties: parallel
same-owner incidences make the fixed-`D` candidate count merely at most
11,440, and an empty colour bank must emit the exact empty clause rather than
abort generation.  It is a layer and must be header-composed with the pinned
base; it is not meaningful alone.

The same audited builder has a canonical outer-master mode.  The quotient
owner--facet graph is 9-regular, so edge counting proves Hall and a
deterministic augmenting-path algorithm constructs a perfect `D_0` without
first solving the base.  Its authenticated output has

```text
candidate turns       11438
empty q1 rows         0
maximum colour bank   10
layer SHA             dc73be4d8c96ea572967e5a97c3469fda4f686555c41877015338865502cbbf1
composed face SHA     72a49ab9c4b15ba2cc6a8f9f661bf35eb6ba3c7c2066d67a185bbacc98b2d976
```

For SAT, the exact lift

```text
scratch/lift_ad_k17_fixed_D_sat_to_compact_model_20260801.cpp
SHA ec3657344e7e6a6a7e5a975dbefbacbbcf885af29ca43f5743cef913a82c0e8d
```

copies the complete base assignment and selects one actual `D/H` provider
per q1 colour.  It is deliberately not a standalone checker: the combined
base+layer model must first pass literal replay, then the emitted 613,656-
variable model must pass the original compact CNF and independent semantic
replay.

For proof-verified UNSAT, the outer-cut generator

```text
scratch/build_ad_k17_fixed_D_outer_nogood_20260801.cpp
SHA f60b2fabcb8dca407352eabaf952dbec64718211a8b11d9cdc9ec91c105e012e
```

requires the 1,430 mapped `D` rows to equal the layer's positive unit prefix
and requires the complete multiset of 1,144 q1 suffix clauses to equal the
mapped colour banks, including empty groups.  It emits the negative `D` row
only after the runner has independently verified the matching composed-face
proof.

## 5. Fixed-age residual-Hall fallback

After both age and `D` are fixed, the legal replacement-`H` graph has at most
11,440 incidence variables.  Pairwise facet/owner exact-one and 1,144 colour
ALOs use at most 95,524 clauses.

Equivalently choose a matching `P` containing one representative of every
colour, then complete the 286 remaining facets and owners.  For consumed
facet/owner indicators `x_f,y_o`, residual Hall is exactly the coefficient-
one family

```text
sum_{o in N(S)} y_o <= |N(S)|-|S| + sum_{f in S} x_f.
```

Necessity follows because a residual matching injects the `|S|-x(S)` free
facets into the `|N(S)|-y(N(S))` free owners.  Conversely, a deficient
residual Hall shore may be chosen among free facets and violates the row.
Alternating reachability returns such a shore with its exact deficiency.

The audited fallback builder is

```text
scratch/build_ad_k17_fixed_age_D_rank10_H_subproblem_20260801.cpp
SHA 8d5a7166e9ac690501f69be5b7893e54064309d91171d4e570e24285b9767beb
```

It is conditional on the pinned base CNF/map hashes.  If a new `H` is
installed into an old model, the sequential exact-one auxiliaries must also
be recomputed; the proof-safe default is to solve the composed formula and
replay its complete returned model.

## 6. Current staged execution

After the compact portfolio ended, one nonduplicate base-stage worker was
launched on H100 CPU core 24, seed 1722531, with one worker, nice 15, 16 GiB
address/file caps and a 1,200-second solver limit:

```text
/home/amodo/or15/work/ad_k17_age_compact_929df903_5d4e717d_20260801/solve_base_stage_fixedD_20260801T1429Z
```

Runner source:

```text
scratch/run_ad_k17_compact_base_stage_worker_20260801.sh
SHA 78f48bdc0b01993bd28d88f8c80b9e89aabc97900cb8f96a252d36d9375260f7
```

That worker terminated authenticated `UNKNOWN` after 1,200 seconds, with no
SAT/UNSAT line.  It reached 12,995,012 conflicts, 615,867,226 decisions and
7,950,804,992 propagations at peak RSS 360,716 KiB.  This authorizes no cut
and shows why a prior flat base incumbent should not be a prerequisite.

The exact successor worker now also accepts a canonical outer matching, so
it does not require that timed-out base model:

```text
scratch/run_ad_k17_fixed_D_q1_face_worker_20260801.sh
SHA f2bbf0b952a2022310046f5349c622649ca43e2c2cef9ada97674dc26634959f
```

It hash-binds and composes the fixed-`D` layer.  On SAT it first replays the
510,712-variable face, lifts one provider per actual colour, then replays the
original compact CNF and its semantic/topology pipeline.  On UNSAT it emits
the outer `D` no-good only after independent DRAT verification and exact
layer-map/unit/q1-clause reconciliation.  Every other exit is `UNKNOWN` and
emits no cut.

It was launched directly from the canonical `D_0` at

```text
/home/amodo/or15/work/ad_k17_age_compact_929df903_5d4e717d_20260801/solve_canonical_D0_q1_20260801T1453Z
```

It terminated exact runtime `UNKNOWN` after 1,200 seconds, with no SAT or
UNSAT line.  This is not a feasibility result and emits no `D_0` cut.  Exact
telemetry was

```text
conflicts       9,989,720
decisions       235,074,484
propagations    9,370,972,865
wall/process    1200.02/1198.94 seconds
peak RSS        200,660 KiB
```

Hashes:

```text
8d65a4b9eb195d5e86030347c80f76cf5f23d651a73643a82581979d2548c6bb  authenticated.status
1f6872f501ae43f16d857bdc6ea36ef0550c3d25fde7820602aad8dd0648382d  solver.status.json
d77c395a1d606507b6c58282f977cc36d8e5ee02f6145beaa41bd85753095c8c  solver.stdout.log
f4e5a3557fed2d790fdda1155d434a925cb47935c2260436022251a89d7286f0  solver.resource.log
```

## 7. Static residual-H and fixed-(D,H) Benders results

The independently reconstructed static `H` master for canonical `D_0` has

```text
11438 variables / 84056 clauses
```

and exactly the complete nonloop candidate catalogue, both perfect-matching
row systems, and all 1,144 fixed-`D_0` q1 colour ALOs.  Its independent
semantic replay is frozen in

```text
MATH_AUDIT_AD_K17_CANONICAL_D0_STATIC_H_INNER_MASTER_20260801.md
scratch/ad_k17_canonical_D0_static_H_semantic_audit_20260801/semantic.audit.json
```

with semantic-audit SHA
`e43d127de2871699323536a297efd283da6edbb3b5cbfd95a1036620764c76e7`.
The first static model `H_0` was SAT and completely replayed in 0.12 seconds:

```text
62c2fa5bca1ea80cf09b07e369bba60d2f405a67825e45a35023dcb1abc27dfb  solver.stdout.log
f145ce2e3d4a60446366fd6030554c1769a22d1134e3026503d17a90a913b9d8  assignment.audit.json
3d7716e42741207fbc9d093d66af2f0cb7743dd3003d40cbb46fbd164c70a9c6  authenticated.status
```

This means only that a static q1-complete matching exists.  The exact age
face

```text
B and D_0 and H_0
510712 variables / 3035834 clauses
f548ef314ce53d9c54cc34a59738148a1e61d38b0ac07015c2130675aef2eaa8  CNF
```

was UNSAT by input unit propagation.  DRAT-trim independently verified the
proof and reduced it to 11 input clauses.  Seven are base clauses and four
are selected role units:

```text
D_30, D_531, H_34, H_535.
```

The independently fail-closed projector authenticates the face as literal
`B` plus its 2,860 units, multiset-subtracts the core against `B`, and checks
the 11-clause core itself by unit propagation.  It therefore proves the
strong cuts

```text
fixed D_0:       not H_34 or not H_535
unrestricted:    not D_30 or not D_531 or not H_34 or not H_535.
```

In static local variables the first is `-74 -1298`.  Exact artifacts:

```text
0c7c7ffe4ef16392f54f37aed4661ee7fd66407fa383515d4941d07fbd5eb846  11-clause core
8f16ee9f184fd1c6cd97702f119f4d12956f6232ff518fa15c37ce14f5b44f0d  core LRAT
95a4f564abe051fe624f956ee65ec171d26bc68e8b5096afc1c3d74005b74532  local cut
e510e0d84c0f5b7d3e7afed4a6a45a7dc10c643087f835898003a33614303495  guarded global cut
```

Two independently replayed successor static matchings gave two further
proof-verified 11-clause UP cores and binary local cuts:

```text
H_1: local -289 -2841; global {D_82,D_1548,H_88,H_1550}
H_2: local -410 -3818; global {D_130,D_2187,H_131,H_2192}
```

Their local-cut hashes are respectively
`1a84064c53bddec0cfa915104c5cda5a2e5f256214c2b92c34dcf729bcf6babc`
and
`1d005f49a5f8bba6c63eea18552b9b29bdefe46a2dddef0c4bb94b337e517492`.
Thus the exact decomposition is already producing two-edge incompatibility
cuts rather than 1,430-edge incumbent no-goods.

The fixed-face builder and fail-closed core projector are

```text
scratch/build_ad_k17_fixed_DH_variable_age_face_20260801.cpp
SHA baf88291249ea5d7c7d04f856633d615fd6fd112d2c25133dffed45adf572118

scratch/extract_ad_k17_fixed_DH_assumption_core_cut_20260801.cpp
SHA c5549cc794454ab3571c24915eab97211a34ec81686a341f1b4baec01f99effb
```

The projector accepts only an independently `UP_UNSAT` core; a non-UP core
requires a separate reduced-face proof or falls back to the full incumbent
cut.  Exact cut scopes and the finite Benders loop are proved in
`MATH_THEOREM_AD_K17_FIXED_DH_CORE_BENDERS_LOOP_20260801.md`.

## 8. Exact omitted gates

Even a SAT fixed-`D` q1 face proves only the frozen age/rank-7 plus upper-q1
skeleton.  The following remain separate:

- quotient connectivity and nonzero voltage;
- cyclic depth-3 residence replay;
- lower ranks 2 through 6;
- upper ranks 11 through 16 and source-3-trimmed safe opening;
- opened lower-q1 boundary restitution;
- generalized lower compiler and common cap;
- literal contiguous-OR word realization.

Thus neither the compact runtime nor the staged face currently proves a K17
carrier or word.
