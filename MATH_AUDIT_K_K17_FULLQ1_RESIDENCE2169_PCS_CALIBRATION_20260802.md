# K17 full-q1/residence-2169 calibration for the protected Catalan--pivot lane

**Date:** 2026-08-02  
**Status:** independent scope audit of frozen finite artifacts.  The immediate
rank-ten statement and the two endpoint models are authenticated.  This note
does not promote the finite trajectory to an all-`m` existence or descent
theorem.

## 1. Audited conclusion

There is an authenticated normalized `k=17`, `h=1` incidence factor with

\[
 |\mathcal U_{10}|={17\choose10}=19{,}448
\]

such that all `19,448` immediate-upper colours occur on ordinary rooted
diamonds.  Its augmented incidence graph is connected, and both licensed
linear openings cover `19,448/19,448` rank-ten colours.  The primary model is

```text
/home/amodo/or15/work/root_k17_fullq1_ordinary_circulation_20260802/
  fullq1_13.best.model
SHA-256 e7ea3841cde04129e3b0af008da0ab2ca2deb8936f09ae22d43a9174ac888a31
```

An exact sequence of guarded residence batches leads from this model to

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_fullq1_res2169/model
SHA-256 3107fc58bbf222bb5e00e6ff9ceb79d23623a156811591a033912f90ab29354d
```

while retaining zero rank-ten holes in **both** licensed openings, the fixed
boundary rows, all `16,261` frozen guard clauses, exact degrees, and one
augmented component.  The opened short-run count decreases from `5,588` to
`2,169`.

This is positive finite evidence that immediate-upper exactness and a large
residence improvement are compatible.  It is not a resident factor: `2,169`
short runs remain.

## 2. Primary full-shore authentication

The independent full-formula report is

```text
scratch/k17_h1_fullq1_ordinary_circulation_20260802/
  fullq1_13.fullaudit.report.json
SHA-256 6467b91bd7abb14a3ff381ef63a8dca86143e7c00d95caead04bdef8b957f2e2
```

It reconstructs `1,093,878` variables and passes all `7,163,170` clauses.
The exact structural rows are

```text
selected incidences                 48,620
selected ordinary diamonds          24,308
augmented incidence components           1
ordinary owner components                2
ordinary immediate-upper support   19,448 / 19,448
```

The ordinary provider multiplicities are

\[
 1^{15128}2^{3816}3^{471}4^{30}5^3,
\]

whose weighted sum is `24,308`.  Thus the seam is redundant for rank ten at
this primary model: all `19,412` non-`D` colours and all `36` `D`-superset
colours already have ordinary providers.

The independent semantic replay note has SHA-256
`24e05fb633a9f27972a822065810c73679e25176971e06dd67cb163a9db5176d`.
It derives the final seam roles from topology, rather than inheriting the
earlier q1-zero role.  The selected exceptional incidences are

```text
M owners  [511]
D owners  [8447,33023,65791]
```

and the two final `(internal,closing)` seam-colour pairs are

```text
(41215,66047), (73983,33279).
```

Both opened and both cyclic palettes are `19,448/19,448`.

## 3. Exact component profile

The component statement is stronger and more specific than merely saying
"connected".  There are `W=24,310` lower roots and `W` owners.  Every owner
has incidence degree two; every ordinary lower root has degree two; the
exceptional roots have

\[
 d(M)=1,\qquad d(D)=3.
\]

The selected graph has `2W` vertices and `2W` edges.  Since its independent
replay gives one connected component, it is unicyclic.  The degree signature
then forces a lollipop: a single path from the leaf `M` to `D`, together with
one cycle through `D`.  Removing the exceptional roots and contracting the
ordinary degree-two roots gives exactly **two ordinary owner paths**.  A
licensed opening cuts the `D` cycle in either direction and concatenates it
with the `M`--`D` tail, producing one owner Hamilton path.

This proof uses only the degree rows and augmented connectedness, so it also
applies to every audited residence checkpoint.  It does not assert that the
two ordinary path sizes are invariant under the batches.

There is a separate auxiliary decomposition at the primary model: choosing
one ordinary provider for each rank-ten colour gives a `19,448`-edge primary
forest with `4,862` components, and its residual complement is a `4,861`-edge
path after opening (a `4,862`-edge cycle before opening).  Those `4,862`
components are provider-forest components, not components of the carrier.

## 4. Authenticated residence descent

The strict batches use complete current-state alternating `C6` and
rank-seven-core four-petal star-`C8` catalogues.  Every retained batch endpoint
replays exact degrees, the frozen clauses, the protected boundary rows,
connectedness, all `19,412` necessary ordinary non-`D` rows, and both opened
rank-ten palettes.  The exact opened residence sequence is

```text
5588, 4081, 3325, 2916, 2632, 2470, 2349, 2265, 2207, 2169.
```

The accepted batch sizes after the primary model are

```text
839, 489, 314, 218, 123, 100, 72, 52, 31.
```

The corresponding descendant model hashes are

| checkpoint | opened residence | model SHA-256 |
|---:|---:|---|
| strict0 | 4081 | `d790aca46fe4b438919ab121ad0091af1a55f5822eddb3b9be5ed4432c48e844` |
| strict1 | 3325 | `bc0f6c7bdd16d98d24642fab7f1d6f770f591b829eb6a9b7f67ad44f97e3c135` |
| strict2 | 2916 | `d9f86919885836323831ba75d555ea0e301e04491223b0b6ce8a602f164ea21f` |
| strict3 | 2632 | `6b8a5e81253e47ecde192fa5b4d1e69987249eda4f00abf10c66ff7a195a9083` |
| strict4 | 2470 | `eee5bd7393c26738e04ab31624afa6085f1edd92d8d5fa4565569373ae2fb00c` |
| strict5 | 2349 | `4a5f58cbc740ae418eb28fa16d12b3d6a8b8925bc402ee294d9bae8e8fa93f8c` |
| strict6 | 2265 | `1ae4229612b54996dbd29fba156ce332f9d3dfe904d5cd252cb66e21e6335718` |
| strict7 | 2207 | `a846daea29080a3345f56840077f2becdd54c04734682f351df6007c5ecd4d0a` |
| strict8 | 2169 | `3107fc58bbf222bb5e00e6ff9ceb79d23623a156811591a033912f90ab29354d` |

For clarity, the batch audits also report an **ordinary cyclic auxiliary**
short-component count.  At the last checkpoint it is `2,167`, while the
passive cut count is `2,168`; neither is the opened objective `2,169`.

The final independent endpoint replay is

```text
scratch/k17_h1_fullq1_res2169_compound_20260802/
  checkpoint_fullq1_res2169__independent.audit.json
SHA-256 a84e1c54a77ae925c06e3ca68b6aaf0189d667c9e0cdc9de0f114e938db90184
```

and the independent passive replay has SHA-256
`6db482243150fb7986eeaefa6e81e6cdcb111206489c16f20659dd1de9583dc5`.
They agree on

```text
ordinary short-component histogram lengths 1..3  (0,1361,806)
seam short components                              12
opened histogram lengths 1..2                (1361,808)
opened residence                                  2169
rank-10 holes in both openings                       0
```

The primary and final deeper-upper profiles are, respectively,

```text
primary orientation 0  ranks11..13 = (1528,288,6)
primary orientation 1  ranks11..13 = (1529,288,6)
final both orientations ranks11..13 = (1516,267,4)
```

Ranks `14` through `17` are complete at both endpoints.  This extra finite
improvement is useful evidence, but deep completeness remains false.

## 5. What is actually protected

The primary full-formula replay fixes

```text
M=383, D=255, B=511, M intersection D=127,
```

and selects the normalized boundary incidences

```text
M -- B,
(B - {0})=510 -- B.
```

The residence batch implementation rejects every move deleting either the
`M--B` incidence or the selected normalized boundary branch.  It also checks
all `16,261` frozen clauses after the derived ordinary-pair variables are
rebuilt.  Consequently this **two-edge endpoint aperture** and its lollipop
semantics survive to residence `2,169`.

This is not an audit of a depth-`d` protected Catalan pivot collar.  The
artifacts do not name a pivot-rich flat collar, do not freeze its full owner
and history ledger, and do not replay global address consistency for one.
The word "protected" in this finite lineage therefore means the normalized
`M/D` boundary branch and frozen formula rows, not the full `PCS(m,d)` collar
state.

## 6. Exact PCS calibration and exclusions

The finite factor verifies the following compatible rows at `m=8`:

1. a rooted one-path opening (equivalently, a two-path ordinary support plus
   the normalized exceptional lollipop join);
2. complete immediate-upper occurrence availability;
3. a fixed two-edge endpoint aperture;
4. a large q1-safe residence descent inside that face.

It does **not** verify:

* positive depth-three residence (`2,169>0`);
* the prescribed pivot collar or its global pin/history replay;
* an all-width upper-exact factor (ranks `11--13` are incomplete);
* a source antecedent, lower/common-cap compiler, exterior windows, or a
  length-`24,313` word;
* any uniform all-`m` abundance, expansion, pull-tree, or descent theorem.

Thus the proof-safe use in `PCS` is as a finite compatibility witness: the
immediate-upper row, bounded carrier-component row, and a protected boundary
aperture can coexist, and residence can improve substantially without losing
them.  The remaining all-`m` theorem must still install the **literal pivot
collar** and force residence to zero; neither conclusion follows from this
trajectory.

## 7. Lightweight independent reproducer

The local read-only reproducer

```text
scratch/audit_k_k17_fullq1_residence2169_scope_20260802.sh
```

checks the frozen endpoint hashes, the primary full-formula/component rows,
the final q1/residence/deep-upper rows, the passive metric separation, and the
strict1--strict8 residence sequence.  It emits

```text
PASS_K_K17_FULLQ1_RESIDENCE2169_SCOPE_AUDIT
primary_q1=19448/19448 primary_residence=5588
final_q1_openings=19448/19448 final_residence=2169
augmented_components=1 ordinary_owner_components=2 (degree consequence)
pivot_collar=NOT_CERTIFIED
```
