# K16 H1 joint13: exact compact phase flip and 29-witness decomposition

Date: 2026-07-30  
Lane: AD  
Status: **proved solver-free preprocessing; fallback unlaunched**

## 1. Verdict

The known four-block near phase has been transported from the 1,790-variable
explicit-witness representation into the frozen **469-variable composed
proxy/supplycode CNF**, not merely reused in its older parent encoding.

The transport is exact:

```text
explicit phase true variables                         120
compact true binary chart-code bits                   120
compact true supply flags                              65
compact phase true variables                           185
false compact clauses                                    1
```

The unique false compact clause is zero-based row 8,836,

```text
(81, -82, 83, 84, 85, 301),
```

namely H-chart 2 (`flat 1` singleton) requiring its proxy bit 11 from supply
variable 301.  After polarity flipping around the phase this becomes the
single all-positive row

```text
(81, 82, 83, 84, 85, 301).
```

More strongly, the parent formula has been decomposed exactly by all 29
valid charts of (H=mathtt{0x2c6d}).  Each case is unit-propagated,
densely renumbered, and phase-flipped.  The resulting 29 formulas have
432--453 variables and 21,278--26,914 clauses.  An independent program
reconstructed every one of their clauses in order and returned
`PASS_SOLVER_FREE_UNLAUNCHED`.

No SAT solver was invoked.  The fallback runbook is deliberately unlaunched
while the independently owned seed-1731 parent run is active.

## 2. Frozen parent

The exact parent is

```text
scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.cnf
SHA-256 f03c8c3e38caf4d4f47bb7ae4569e07526afdd7689acc2c1b32b8dfd71ab488e

scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.map.json
SHA-256 f5f50ec0563adb1175500ef1426144f753dd72ed37f360f787ebb840feeb5ed8
```

It has exactly 469 variables, 28,233 clauses, and 174,662 literals.  Its
previous independent audit has SHA-256

```text
331f1d7d56c18c6c639c8abf27b9e177c692a012b9a20e6878b4397efb025c76.
```

The structural phase input is

```text
scratch/k16_h1_fourportal_joint13_witness_20260730/near.manifest.json
SHA-256 1ee42402edde3e7fc70400fbe45e5057fab08f1d255a48adb44162acec3e8b95.
```

All 55 chart choices in that phase survive the exact 16-chart normalization.
For every target (T), the old witness index identifies a unique retained
action and hence a unique five-bit compact code.  The 55 one-hot choices are
therefore replaced by their 275 binary code bits.  In this particular phase
exactly 120 of those code bits are true.  The canonical thirteen physical
cell values determine 65 true live supply flags.  Direct evaluation of all
28,233 compact rows gives the one-row ledger above.

This numerical equality between the old total `120` and the compact
code-bit total `120` is incidental.  The actual compact phase has 185 true
variables.

## 3. Exact H-case theorem

Let (F(x)) be the frozen 469-variable composed CNF.  The five chart-code
variables of (H=mathtt{0x2c6d}) are

```text
81, 82, 83, 84, 85.
```

The H action catalogue contains exactly codes (0,ldots,28).  The parent
contains exactly the three invalid-code exclusion rows for codes 29, 30,
and 31.

For (hin{0,ldots,28}), let (A_h) fix the five H bits to the binary
expansion of (h).  Starting from (F\wedge A_h):

1. take the complete unit-propagation closure (U_h);
2. delete every clause satisfied by (U_h) and every false assigned literal
   from the remaining clauses;
3. densely renumber the unassigned original variables in increasing order;
4. choose the deterministic canonical physical phase described in Section 4,
   overwrite its forced coordinates by (U_h), and flip the polarity of
   every free variable that is true in that phase.

Call the resulting formula (G_h).

### Theorem 3.1 (exhaustive compact H decomposition)

The following equivalence is exact:

\[
       F\text{ is satisfiable}
       \quad\Longleftrightarrow\quad
       \bigvee_{h=0}^{28} G_h\text{ is satisfiable}.
\]

The cases are pairwise disjoint when lifted to parent coordinates.

#### Proof

Every model of (F) assigns a five-bit H code.  The three parent exclusion
rows forbid 29, 30, and 31, so the code is a unique (h\in[0,28]).  Hence
the model belongs to exactly one (F\wedge A_h).

Each unit-propagation step replaces a formula containing a unit literal by
the result of assigning that logically forced literal.  It preserves
satisfiability in both directions, with the forced value retained for
lifting.  Iterating to closure proves that the residual formula after Step 2
is equisatisfiable with (F\wedge A_h).  Dense renumbering is a variable
bijection.  Finally, if (p_h(v)) is the preferred truth value of a free
original variable (v), the polarity transformation is

\[
                 x_v=y_{\rho_h(v)}\oplus p_h(v).
\]

It too is a bijection.  Thus (G_h) is equisatisfiable with precisely the
(h)-th conditioned parent.  Taking the disjoint union over all valid codes
proves the claim. \(\square\)

Consequently:

- SAT of any one slice lifts mechanically to SAT of the original composed
  CNF;
- independently proof-checked UNSAT of all 29 slices proves the original
  composed CNF UNSAT;
- one `UNKNOWN`, timeout, resource abort, or unverified proof leaves the
  parent status `UNKNOWN`.

## 4. Phase definition and its exact role

For a fixed (h), retain the 54 source-realized chart choices from the known
phase and replace only H's chart by code (h).  At editable flat cell (p),
put

\[
 C_p=\bigcap\{T:\text{the selected chart of }T\text{ crosses }p\},
\]

with empty intersection `0xffff`.  Encode the selected actions in the five
code bits and set each live supply flag to its literal membership in (C_p).
This is a complete 469-variable assignment before conditioning.

After computing (U_h), any canonical phase value that conflicts with a
forced value is replaced by the forced value.  Only free-variable values are
used for polarity flipping.  This phase has **no logical force**: it removes
no solutions, since polarity flipping is bijective.  The only genuine case
restriction is the exact H code (A_h).

For H code 2, unit closure forces variable 301 true.  The raw canonical phase
had it false, so the unit-consistent phase exposes exactly the three known
omitter blockers, at targets

```text
0x246d, 0x346d, 0x766d.
```

This is the composed-model version of the earlier singleton-bit-11 quotient.
It is not a contradiction.

Three different cases are even closer after closure:

| H code | H interval (flat) | residual variables | residual clauses | all-false defects | unique defect |
|---:|---:|---:|---:|---:|---|
| 4 | 2--3 | 449 | 24,804 | 1 | H proxy bit 2 |
| 5 | 2--4 | 441 | 22,928 | 1 | H proxy bit 2 |
| 14 | 6--7 | 448 | 25,471 | 1 | H proxy bit 10 |

Again, “one defect” describes a preferred total phase, not a one-variable
repair theorem.

## 5. Exact slice census

`forced` includes the five H code bits and every value obtained by complete
unit propagation.  `defects` counts clauses false at the all-false assignment
of the phase-flipped residual formula.

| H | vars | clauses | literals | forced | defects |
|---:|---:|---:|---:|---:|---:|
| 0 | 452 | 26,914 | 166,250 | 17 | 8 |
| 1 | 448 | 26,396 | 163,190 | 21 | 4 |
| 2 | 453 | 26,909 | 166,267 | 16 | 3 |
| 3 | 453 | 26,322 | 161,967 | 16 | 16 |
| 4 | 449 | 24,804 | 153,207 | 20 | 1 |
| 5 | 441 | 22,928 | 141,500 | 28 | 1 |
| 6 | 433 | 21,670 | 133,688 | 36 | 3 |
| 7 | 452 | 25,280 | 155,078 | 17 | 13 |
| 8 | 448 | 23,948 | 147,895 | 21 | 2 |
| 9 | 440 | 22,690 | 140,083 | 29 | 4 |
| 10 | 452 | 25,252 | 154,901 | 17 | 14 |
| 11 | 448 | 24,544 | 151,663 | 21 | 5 |
| 12 | 452 | 26,075 | 160,474 | 17 | 23 |
| 13 | 452 | 26,502 | 163,460 | 17 | 10 |
| 14 | 448 | 25,471 | 157,415 | 21 | 1 |
| 15 | 440 | 24,533 | 151,573 | 29 | 3 |
| 16 | 452 | 26,101 | 160,801 | 17 | 7 |
| 17 | 448 | 25,482 | 157,484 | 21 | 4 |
| 18 | 452 | 26,517 | 163,559 | 17 | 10 |
| 19 | 452 | 26,045 | 160,196 | 17 | 13 |
| 20 | 448 | 24,478 | 151,166 | 21 | 8 |
| 21 | 440 | 22,558 | 139,126 | 29 | 12 |
| 22 | 432 | 21,278 | 131,101 | 37 | 17 |
| 23 | 452 | 25,182 | 154,338 | 17 | 8 |
| 24 | 448 | 23,838 | 147,115 | 21 | 7 |
| 25 | 440 | 22,558 | 139,090 | 29 | 12 |
| 26 | 452 | 25,171 | 154,248 | 17 | 14 |
| 27 | 448 | 24,478 | 151,117 | 21 | 12 |
| 28 | 452 | 26,018 | 159,965 | 17 | 6 |

The frozen priority order is

```text
5,4,14,8,6,15,2,9,17,1,11,28,24,16,20,23,0,13,18,21,25,27,7,19,26,10,3,22,12.
```

It sorts by `(phase defects, residual clauses, H code)`.  It is a search
heuristic only and is not part of Theorem 3.1.

## 6. Independent audit

The independent auditor does not import the builder.  It performed all of
the following checks from the frozen parent map and CNF:

1. reconstructed all 28,233 parent clauses in their exact order;
2. verified that H codes 0--28 are present and that exactly 29--31 are
   blocked;
3. independently remapped all 55 selected old charts into retained compact
   codes;
4. recomputed all thirteen canonical phase cells in each H case;
5. recomputed the complete unit closure of every case;
6. recomputed every residual clause, dense variable map, and polarity flip;
7. matched all 29 emitted CNFs clause-for-clause and hash-for-hash;
8. matched every false-phase clause back to its original parent row and
   semantic family; and
9. rederived the exact schedule.

The audit is

```text
scratch/ad_k16_h1_joint13_proxy_phaseflip_h29_20260730/model.independent_audit.json
SHA-256 987641279f1186ce3f53f14d320b1f86257facbeab8b9b9ed5e337fa95b0601f
payload SHA-256 737dba74bb0602ca0fb75d01745af2fe78e50cdf16aa87f7cc8a01fb83956196.
```

## 7. SAT lift and proof-retaining fallback

The fail-closed lift utility accepts only an explicit, complete SAT model of
one exact slice.  It:

1. verifies the slice hash and every slice clause;
2. reverses dense renumbering and phase flipping;
3. restores every unit-forced parent variable;
4. verifies the recovered H code;
5. evaluates all 28,233 original parent clauses; and
6. writes a complete 469-variable parent assignment for the already-audited
   physical decoder.

It was regression-tested to reject a missing/non-SAT model without writing
either output artifact.  A positive regression cannot be manufactured until
a genuine slice model exists.

The unlaunched H100 runbook uses, sequentially, one CPU, `/home` storage,
an 1,800-second wall cap, an 8-GiB address-space cap, and proof output.  It
refuses non-`/home/amodo/or15/work/...` paths, checks the three frozen parent
hashes, and treats timeout, abort, ENOSPC/resource failure, incomplete SAT
output, or failed DRAT checking as `UNKNOWN`.  It never interprets one slice
UNSAT as parent UNSAT.  On SAT it lifts to the parent, invokes the physical
decoder, and then runs both `verify_word.py` and `verify_or_array`.

This runbook must not be started concurrently with the active seed-1731
parent job.

## 8. Artifact ledger

| artifact | SHA-256 |
|---|---|
| builder | `9c4a90dbb9d25d73f0489a8b7da9adfee5a1ea6680087a751164e351386f3721` |
| independent auditor | `8fcccc404a1bceaac9552c2c0794e2e20d981925491d0dedfe7d58ae7f3038f0` |
| SAT assignment lifter | `37d17b88c06a92421b90b08d929cfbfc46d208ffe314c2846489a8c0deb7820e` |
| unlaunched H100 runbook | `f01c5b9d7341c38729620940133901d93e92b1b6ccd29084d8f69a5d4377f959` |
| H29 package map | `8aaefe02f75f6f249d7dbf907d6a7ff9ad24f23b56b66f4be4bfc474634493e0` |
| H29 package payload | `d52e2aed71f1bc96366b3ec4a3d5ac226b3d2a3fd1656f17564d3fc21b1c4801` |
| independent audit | `987641279f1186ce3f53f14d320b1f86257facbeab8b9b9ed5e337fa95b0601f` |
| independent audit payload | `737dba74bb0602ca0fb75d01745af2fe78e50cdf16aa87f7cc8a01fb83956196` |
| unconditioned H2 phase-flipped parent | `8867307178913035218469be3f090e5c212e60b18856d66bd664898e7a7ab81a` |
| schedule | `7f5928c70bcff04580f6e3fc4f85b192b5fa55ae2631c9cb842d4849aca2b59d` |

All 29 slice hashes are embedded in the package map and independently
replayed in the audit JSON.  The package occupies approximately 20 MiB.

## 9. Scope boundary

This result is exact only for arbitrary nonzero substitutions on the frozen
joint13 support of the authenticated length-12,873 source.  It does not prove
that the global optimum word must lie in this support.  It does not impose an
edit radius or a preferred-value restriction.  The canonical phases are
heuristics connected by bijective polarity changes, not WLOG assumptions.

The formula and every slice remain **UNSOLVED/UNKNOWN** until an authenticated
SAT model or complete proof-checked UNSAT certificate is obtained.  The
global bracket remains

```text
12873 <= nu(16) <= 12874.
```
