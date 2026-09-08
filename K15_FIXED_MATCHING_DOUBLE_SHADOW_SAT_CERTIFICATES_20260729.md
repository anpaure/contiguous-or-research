# Two exact `k=15` double-shadow factors

Date: 2026-07-29

Status: independently replayed exact factor certificates.  Both have complete
upper-`q1` and lower-`q2` decks.  Neither is resident or connected, so neither
is a `nu(15)=6438` certificate and the rigorous bound remains
`6438 <= nu(15) <= 6458`.

## Exact model

Fix one perfect matching `M0` of the quotient rank-seven/rank-eight incidence
graph.  For each allowed incidence `e=(L,V)`, choose a Boolean variable saying
that `e` belongs to the second matching `P`.  The CNF contains:

1. exactly one `P` edge at every rank-seven orbit;
2. exactly one `P` edge at every rank-eight orbit;
3. at least one selected edge of each upper-`q1` orbit colour made by
   `{M0(L),e}`; and
4. at least one selected edge of each lower-`q2` turn colour made by
   `{M0(V),e}`.

Thus every SAT assignment is an exact first-rainbow quotient 2-factor with
both displayed shadow decks complete.  The decoded factor is expanded to all
6,435 physical rank-eight masks and independently checked by
`audit_k15_global_rainbow_factor_candidate_20260729.py`.

## Certificate A: strict-seed parent

Model: 3,002 variables, 19,534 clauses.  Kissat reports `s SATISFIABLE`.

Independent physical audit:

```text
selected edge orbits        429
rank-7 colour orbits        429
middle degree histogram     2^6435
physical components         20
upper-q1 holes              0 physical / 0 quotient
lower-q2 holes              0 physical / 0 quotient
upper-q2 holes              198 physical / 14 quotient
(P+,P-,Xi)                  (101,105,18)
minimum coordinate run      2
residence bad/shortfall      1425 / 1875
```

Artifacts and SHA-256:

* `scratch/k15_fixed_matching_double_shadow_strict_20260729.cnf`
  `a9a010da6007c43336918d25bbd848a6e4bdcbdfddcb0552ac0d243b29d8fb28`
* `scratch/k15_fixed_matching_double_shadow_strict_20260729.map.json`
  `5edaab89f5b488fd2a2bebf15e89300e4284775c72951731e92903fd1aa168a4`
* `scratch/k15_fixed_matching_double_shadow_strict_20260729.kissat.out`
  `3a3f307261b3b9f1ebf7652f50b9a78069abc6e13d8269244054dffbf4ebc769`
* `scratch/k15_fixed_matching_double_shadow_strict_xi18_20260729.json`
  `373e7d4983a3a8c459d21bced3f3a189fa43f67f792ec0e19877ebd942e661de`
* `scratch/k15_fixed_matching_double_shadow_strict_xi18_20260729.audit.json`
  `d88bd000e970cb93be80408f2fe0ecc14e8865df122997a49f9a18f3851fdf7b`

## Certificate B: phase-2 parent

Model: 2,999 variables, 19,498 clauses.  Kissat reports `s SATISFIABLE`.

Independent physical audit:

```text
selected edge orbits        429
rank-7 colour orbits        429
middle degree histogram     2^6435
physical components         11
upper-q1 holes              0 physical / 0 quotient
lower-q2 holes              0 physical / 0 quotient
upper-q2 holes              360 physical / 24 quotient
(P+,P-,Xi)                  (108,108,28)
minimum coordinate run      2
residence bad/shortfall      1110 / 1425
```

Artifacts and SHA-256:

* `scratch/k15_fixed_matching_double_shadow_phase2_20260729.cnf`
  `7dd11619cbdf0573f2c0642809890a36a425a14c69a4bf8684bfad5c6fa51470`
* `scratch/k15_fixed_matching_double_shadow_phase2_20260729.map.json`
  `e187435517c2ebfef972439629e6257c5b78bc0f5c963ae21ad8d95bc78acef6`
* `scratch/k15_fixed_matching_double_shadow_phase2_20260729.kissat.out`
  `38823a7677a2fc2c5610c6d9ceb140883b09a13bcbc3a31e79d4e08dd003b42d`
* `scratch/k15_fixed_matching_double_shadow_phase2_xi28_20260729.json`
  `3f7367a11a88cc7b7e1a86b1ee2e9ad59c3f12773caa0645887f5d2ecf12c7f2`
* `scratch/k15_fixed_matching_double_shadow_phase2_xi28_20260729.audit.json`
  `bf61e92fbf5a1ebd51d820e1158fc6e47f1d0fc62e5934a9e222911d30501141`

## Reproduction and independent replay

The model builder is
`scratch/k15_fixed_matching_double_shadow_sat_20260729.py`, SHA-256
`391c03a025a933f1c7a6431a04d9ee7002c63d86c957d51805348daaaab58da6`.
The exact C++ expander/evaluator is
`scratch/search_k15_global_rainbow_factor_fiber_20260729.cpp`, SHA-256
`90364d315ed6bf534895320feafa08c9eb2da1c3d008d0db8ea58f948c1b41c8`.
The independent Python auditor is
`scratch/audit_k15_global_rainbow_factor_candidate_20260729.py`, SHA-256
`0afdfe07046f3351075c2b7ecce979f94166a2d6fe7a1b93a9f0acfcf675f04b`.

Replay either retained candidate with:

```text
python3 scratch/audit_k15_global_rainbow_factor_candidate_20260729.py \
  CANDIDATE.json --audit /tmp/replay.audit.json
```

The auditor fails closed on duplicate keys, wrong dimensions, unstable choice
IDs, non-degree-two lifts, and every mismatch between the engine's claimed
physical/collision counts and its own reconstruction.

## Exact finite interpolation result

Relative to their parents, the SAT matchings differ on ten alternating cycles
for A and five for B.  Exhausting all `2^10+2^5=1056` subsets found exactly one
resident state in either cube: its original parent.  This is a negative result
only for these two SAT endpoints.  It motivates the active residence CEGAR,
which adds sound width-at-most-four blockers for short-run transition motifs
before requesting the next exact double-shadow matching.
