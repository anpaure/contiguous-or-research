# Correction: C106 row-slack truncation in continuous seed LPs

Date: 2026-07-30

## Scope

This correction concerns only the frozen K16 length-eight source, its
211,604-seam catalogue, and the C106 balanced/service/capacity relaxations.
It changes no authenticated C105 impossibility proof and no source-relative
floor `C >= 106` theorem.

## The issue

Earlier positive-slack LP scripts retained only seams whose individual direct
dual row slack was at most the requested aggregate slack `R`.  That reduction
is valid for a **binary** seam selection: a selected seam of row slack greater
than `R` would by itself violate the equality

```text
sum_e row_slack(e) x_e = R.
```

It is not valid when `x_e` is continuous.  For example, in an `R=2`
fractional solution a row-slack-three seam may carry mass at most `2/3`, with
the remaining mass carried by slack-zero seams.  Such a point is removed by
the old filter.

The exact row-slack census over all 211,604 seams is

```text
slack 0: 41,491
slack 1: 33,388
slack 2: 74,860
slack 3: 29,927
slack 4: 30,191
slack 5:  1,568
slack 6:    178
slack 7:      1
```

There are no self-loop seams.

## Correct interpretation of the archived R1 results

The archived 405-signature R1 census and the archived R1 group-convex run are
infeasible on the cycle-eligible `row_slack <= 1` arc set.  This remains a
numerical no-go for **integral** R1 selections, because the truncation is WLOG
in the binary model.  No exact Farkas certificate is presently claimed.

Those artifacts do **not** exclude full-continuous R1 fractional seeds using
positive mass on row-slack-two through row-slack-seven seams.  In particular,
the earlier inference that fractional seed search must start at `R >= 2` is
withdrawn.

The corrected audit is

```text
scratch/k16_floor106_r1_capacity_lp_numeric_census_20260730.audit.json
payload 1aa918a07c35417d015ea19bece2245971f16d64f8acc5995aa275e991eb1236
```

The old group-convex artifact has been retained with corrected scope as

```text
scratch/k16_floor106_r1_group_convex_capacity_20260730.audit.json
payload 92045d1f5e818bf2011679d12c5fb114bd33d86785d4121fb57d59c00d7d63c2
```

## Corrected solvers

The fixed-signature disjunctive MIP now has two explicit modes.

1. Full-continuous mode retains every nonnegative-row-slack seam and applies
   only the valid bound `x_e <= min(1,R/row_slack(e))`.
2. `--binary-wlog-presolve` retains only `row_slack <= R`; a negative verdict
   then excludes integral seam selections but is not a full-fractional no-go.

The group-convex and per-signature census drivers now retain all nonnegative
row-slack seams in their continuous modes.

## Corrected R2 bounded-search status

The first signature obtained by rounding the feasible group-convex point was
`1SS01`.  Its corrected fixed-signature LP retained all 211,604 seams and
reported `INFEASIBLE`, but no exact Farkas ray was frozen.  It is therefore
numerical negative evidence, not a theorem.

Two one-CPU SCIP disjunctive searches then ranged over all 270 `R=2`
signatures.  The full-continuous run retained every nonnegative-slack cyclic
arc and imposed `x_e<=min(1,2/row_slack(e))` on each positive-slack arc; the comparison
run used the binary-WLOG `row_slack<=2` presolve.  Both reached their
1,200-second limits with status `NOT_SOLVED`, no signature, and no primal
support.  Consequently no corrected fixed-signature fractional `R=2`
witness has been authenticated, but no `R=2` infeasibility claim follows.

```text
scratch/floor106_R2_1SS01_full.json
  SHA-256 d57ce799ff5fccf6f0a5c0d09b352380dfeb1f70a9d655dbdc2feeef7e2a45a2

scratch/floor106_R2_signature_mip_full.json
  SHA-256 b95b6bfc14ba1f215b35468ca7d96f9282df531ea97955fd268eb2544a884748
  payload 336bd1beecfd000d6587b97120ebc5379d7eae4d39bbdb61fb87f933a942c816

scratch/floor106_R2_signature_mip_binarywlog.json
  SHA-256 620d6fc4c0ca6f9758d355eec7137de0f3350543aa47f08b865362aabfb7e497
  payload 70e4472465c75d9e0a59942ac1932d29a311291a6b1dd05dd3baabfe6fcbcd48

scratch/solve_k16_floor106_signature_mip_capacity_20260730.py
  SHA-256 e88b1ab9121ec461277b3850672884e2096e57a4f034dbd5093a3e17162dc9b1
```

## Status consequences

* `R=0`: the old truncation is exact even fractionally; its results stand.
* `R=1`: this correction reopened full fractional feasibility at the time it
  was written.  The later exact all-arc Farkas certificate in
  `MATH_THEOREM_A_K16_C106_R1_FULL_ARC_EXACT_FARKAS_20260730.md` now excludes
  the full continuous layer without the invalid truncation.
* `R=2,3,4`: old negative truncated-LP reports are scoped only to binary
  solutions and, absent exact certificates, are numerical negative evidence
  rather than proofs; they do not classify full fractional signatures.  The
  corrected bounded `R=2` searches above are also inconclusive.
* `R=5`: the exact all-slack fractional seed remains valid because it is a
  positive witness; omitted arcs cannot invalidate an exhibited point.

## Subsequent resolution of R1

After this correction reopened the full-continuous R1 question, the corrected
211,469-column common relaxation was solved and its ray exactified.  The
canonical integer certificate in
`MATH_THEOREM_A_K16_C106_R1_FULL_ARC_EXACT_FARKAS_20260730.md` excludes all
405 R1 signatures even fractionally.  Thus the old truncated argument was not
a valid proof of that stronger statement, but the stronger statement is now
an independent exact theorem.
