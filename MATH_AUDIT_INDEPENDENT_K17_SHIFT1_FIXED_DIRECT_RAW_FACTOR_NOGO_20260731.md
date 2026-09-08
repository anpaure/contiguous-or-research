# Independent K17 `s=1` fixed-direct raw-factor no-go

Date: 2026-07-31  
Verdict: **SCOPED NO-GO** for each of two independently selected 572-direct
ear banks.  The obstruction occurs before rank-nine turns, topology, ear
lengths, deletion labels, the prefix, or upper continuation.  It is not a
no-go for another direct bank, for more than 572 direct ears, for another
cyclic cut, or for K17 equality.

## 1. The tested raw extension problem

Fix the adjacent-cut `s=1` GK matching and one certified collection of 572
pairwise endpoint-disjoint direct `B-B` ears.  Delete the 1,144 used base
endpoints and their 572 rank-eight colours.  On the remaining base endpoints
`B` and unused rank-seven vertices `U`, select Johnson edges satisfying:

1. every selected rank-eight union is fresh and used at most once;
2. all 8,164 residual missing rank-six intersections occur;
3. every base endpoint has selected degree at most one;
4. every unused vertex has selected degree zero or two.

The catalogue also retains the necessary fixed-bank prefilter that a new
boundary turn may not equal one of the 1,144 turns already frozen by the
direct bank.  There is no global rank-nine all-different row and no central
turn row in the raw model.

The full scalar face additionally requires 12,698 edges, 6,134 used base
endpoints and 9,631 used unused vertices.  These are necessary incidence
conditions for any completion of the fixed direct bank.  No rank-nine or
component constraint appears here.

## 2. Exact result

For the independent direct certificate

```text
scratch/independent_k17_gk_shift1_exceptional_bb_20260731.tsv
SHA-256 7abcbd84c926a4b6fb7154b2b2554d07282508eae10e7b411e2b9a2217231b8d
```

the complete scalar model is `INFEASIBLE` in 6.03 seconds.  Re-enabling the
local rank-nine and global turn rows is also `INFEASIBLE`, already in round
zero and before any component CEGAR cut.

The same raw model is independently `INFEASIBLE` in 5.85 seconds for the
second direct certificate

```text
scratch/k17_gk_shift1_forced_direct_matching_20260731.tsv
SHA-256 8afb0d8f6e754ab31aa6d2f8f2dbe161cdcddce8c81883239195000d9f4afb71.
```

Thus the earlier marginal 8,164-provider b-capacity pass cannot be completed
by adding the 4,534 repeat edges on either fixed bank.  This is exactly why
the marginal pass must not be described as an ear factor.

## 3. Grouped core

For the first bank, an assumption-group model returns the sufficient core

```text
fresh/distinct q8 unions
+ cover all residual q6 colours
+ base endpoint cap one
+ unused-vertex degree in {0,2}.
```

The edge total, total base usage and number of selected unused vertices are
not in the core.  Solving this four-group core directly gives
`INFEASIBLE` in 8.57 seconds.  Removing q6 coverage, q8 injectivity, or
unused-vertex parity gives an exact feasible solution.  Removing only the
base cap remained `UNKNOWN` at the 120-second diagnostic limit, so minimality
with respect to that fourth group is not claimed.

The obstruction is therefore a coloured even-factor correlation, not an
arithmetic ear-length or global-turn failure.

## 4. Scope and next test

This does **not** refute the adjacent-cut route.  Direct-ear selection and
the residual factor were separated in the two failed tests.  A successful
construction may:

* choose a third 572-direct bank jointly with its residual factor;
* use a different direct bank, possibly with extra direct ears; or
* cut/rethread the base before the residual factor is chosen.

Allowing `z` additional direct ears changes the adjacent-length ledger to

\[
  x_1=572+z,\qquad x_4=2637-4z,\qquad x_5=430+3z.
\]

For the first fixed bank, the exact extra-direct model enumerates all 5,829
additional `B-B` edges which have fresh q8, avoid the fixed boundary-q9 bank,
and join different current components.  It allows an arbitrary number of
them while retaining the exact total edge/base/U ledger.  This enlarged
model is also `INFEASIBLE` (3.72 seconds, zero branches).  Thus merely adding
more direct ears cannot repair **that bank**.  Jointly choosing the original
direct bank and the residual factor remains open and is exactly the
unrestricted master in
`MATH_THEOREM_THREAD_D_K17_CYCLIC_CUT_S1_CAPACITATED_EAR_MASTER_20260731.md`.

## 5. Frozen artifacts

```text
scratch/independent_k17_gk_shift1_stageB_raw_20260731.result.json
  58cf8b1aca3c48a3bf0831a6676567501c1aa038514009df8e62c8113ed267ec
scratch/independent_k17_gk_shift1_stageB_alt_direct_raw_20260731.result.json
  7eb81fb6dec6ccb1cd4e875683ac9b47f4d9d5af72e09c16e1ecf0c03e566dbc
scratch/independent_k17_gk_shift1_stageB_raw_min_core_20260731.result.json
  a98b917134614fc4ae1353ec2d5c078493384b58579a6a89052518ec3b559ca3
scratch/independent_k17_gk_shift1_stageB_fullturn_20260731.result.json
  b1420b2f21975dd41dd96f21cdc218717b2c5ebc1cf640e141510a03c4fb52f6
scratch/diagnose_independent_k17_gk_shift1_stageB_turn_unsat_20260731.py
  a54201735994a402423c85f7e8a3d0a50371fa0238b9fa2f4ae3b5a8736baf83
scratch/diagnose_independent_k17_gk_shift1_raw_core_20260731.py
  96c04fc1bde80f02b4cd8626d88b98b61b17a83b6ca9ef4e16e4b47b3cba1f9d
scratch/independent_k17_gk_shift1_extra_direct_raw_20260731.result.json
  89a3496856adf00a7b412ae10a73369e722e2d514493a1692303cad94fe9510b
scratch/solve_independent_k17_gk_shift1_extra_direct_raw_20260731.py
  006f0d009ba27ab59f1d65742c699e875a91d3edf4319102364c2f5bda48c50a
```
