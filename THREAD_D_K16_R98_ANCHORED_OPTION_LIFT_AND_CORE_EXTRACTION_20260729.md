# Thread D: anchored option lift and proof-safe radius-98 core extraction

Date: 2026-07-29.

## 1. Frozen scope

Let $F$ be the persisted radius-147 round-0 factor with byte SHA-256

```text
d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8.
```

Its 147 current short-run motifs have transversal and packing number 97.  Their
edge union has 390 quotient edges and decomposes into 85 pairwise edge-disjoint
motif-overlap components.  The corresponding explicit min-max certificate is
`scratch/k16_dynamic_cross_r147_round0_residence_tau97_20260729.certificate.json`,
with byte SHA-256

```text
6d6261267e9d2e9883b4afb2929b27ccbc8e005d4cd35fc068b628fefa414117.
```

This note concerns only the radius-98 face in which cuts are restricted to
those 390 edges and new edges have both endpoints among the resulting 466
candidate nodes.  It does not include the known outside-node portal bank.

There are 649 nonfixed quotient q1 rows: 327 lower and 322 upper.  In the
deterministic row ordering used by the retained scripts, row 486 is

```text
palette = upper, colour = (1,1907),
source providers in the cut domain = {22511},
addable providers in the 466-node domain = empty.
```

Call this row $u_*$.  On the restricted face, $u_*$ is exactly the equation
$c_{22511}=0$, where $c_e=1$ means that source edge $e$ is cut.

## 2. Exact anchored option-lift lemma

For motif component \(j\), let \(E_j\) be its edge union and let
\(\tau_j^*\) be the minimum size of a transversal of its motifs using
\(E_j\setminus\{22511\}\).  The retained option atlas enumerates every
\(\tau_j^*\)-transversal.  Its exact censuses are

```text
local-rank histogram: 1^75, 2^8, 3^1, 4^1;
sum_j tau_j^* = 98;
option-count histogram: 1^10, 2^17, 3^31, 4^21, 5^1, 6^2, 8^3;
total options = 262.
```

**Lemma 2.1 (anchored exact lift).**  Fix any collection \(S\) of q1 rows
containing \(u_*\).  The raw 390-cut radius-98 model and the component-option
model have exactly the same feasible cut/add pairs after imposing \(S\),
degree two, and any further constraints expressed through selected edge
indicators.

**Proof.**  The sets \(E_j\) partition the 390-edge motif union.  A raw cut
\(C\) satisfying \(u_*\) avoids 22511.  If it hits every source motif, then

\[
  |C\cap E_j|\geq \tau_j^*\quad\hbox{for every }j.
\]

Because the cut domain is the disjoint union of the \(E_j\), while
\(|C|=98=\sum_j\tau_j^*\), equality holds in every component.  Thus
\(C\cap E_j\) is one of the enumerated options.  Conversely, one option in
each component hits all 147 motifs and has total cardinality 98.  The added
edges, degree equations, q1 provider ORs, and boundary/reach rows are the same
functions of the selected edge indicators in both models.  This gives the
claimed bijection.  \(\square\)

The anchor is essential for this proof.  Without \(u_*\), edge 22511 may be
cut, the unanchored component ranks sum to 97, and radius 98 admits local
excess patterns absent from the 262-option atlas.

## 3. Unguarded sufficient-subset extraction

Guarding all 649 q1 rows seriously weakens CP-SAT presolve.  It is unnecessary.
Use the following rebuild oracle instead.

A solver-free option-incidence audit removes many rows before any solve.  In
the anchored atlas, 216 rows (112 lower and 104 upper, including \(u_*\)) have
a source provider that no option ever cuts.  Of the remaining 433
syntactically variable rows, 14 are nevertheless unviolable under the local
exactly-one option correlations.  Thus only 419 q1 rows can actually fail.
The 433-row primitive option/add incidence graph is connected, so this
reduction does not conceal a further direct-sum decomposition.  The critical
halo is the union of 20 endpoint rows and 12 additional direct-neighbor rows;
all 32 are variable.  The 20-row endpoint layer is the natural first CEGAR
seed, while the 32-row union is the next closed seed.

The full row-ID ledgers and their digests are frozen in
`scratch/threadD_k16_r98_q1_block_structure_20260729.audit.json` (byte
SHA-256 `7ad545c01f9596c5a53d3df3199e5e6cd5e274d79b692e6184ed6972a7456f9b`).
Its solver-free reproducer is
`scratch/audit_threadD_k16_r98_q1_block_structure_20260729.py` (byte SHA-256
`490834510cfa9ab8058910cf274a92f49a9695cfd8ce87e9c03562d3d760176d`).

For $S\subseteq R\setminus\{u_*\}$, build the compressed model afresh with
$u_*$ hard and precisely the rows in $S$ present as ordinary, unguarded
constraints.  Call the result $M(S)$.  The initial all-row unguarded model
has already returned `INFEASIBLE` in 2.47 seconds.

There is also a frozen stronger top-relaxed transcript: the option, degree,
and both-q1 model without boundary/reach variables has 8,024 variables and
1,525 constraints and returned `INFEASIBLE` in 49.23 seconds.  The ordinary
LP relaxation is feasible, with 533 fractional variables, so this is an
integral obstruction rather than a Farkas cut.  A practical rebuild oracle
may race the top-relaxed and boundary/reach formulations and accept whichever
first returns `INFEASIBLE`; either result is sound for literal residence.

Maintain a set $S$ for which `INFEASIBLE` has been proved.  For a block
$B\subseteq S$:

1. solve a fresh $M(S\setminus B)$;
2. on `INFEASIBLE`, replace $S$ by $S\setminus B$;
3. on `FEASIBLE`, split $B$ and test its children;
4. on `UNKNOWN`, leave $S$ unchanged and either split $B$ or retry with a
   larger bound;
5. never remove $u_*$.

Start with large deterministic blocks and recurse toward single rows.  Since a
row is removed only after a proved infeasible rebuild, the invariant
`M(S) is INFEASIBLE` is exact even if some tests time out.  A final fresh
rebuild and infeasibility solve freezes the sufficient subset.  If every
retained singleton deletion is proved feasible, the result is
inclusion-minimal; otherwise it is honestly only a sufficient subset.

An often faster seed is unguarded q1 CEGAR: begin with $u_*$, solve, add all
q1 rows literally missed by the witness, and repeat until infeasible.  The
resulting row set can then be block-deleted as above.

Every query artifact should contain the sorted row IDs, their SHA-256 digest,
model-proto digest, solver status, and—when feasible—the decoded cut/add
witness.  An `UNKNOWN` query never justifies deleting a row.

By Lemma 2.1, the final anchored compressed infeasibility is already an exact
raw-390 infeasibility theorem on the stated restricted face.

## 4. Small guarded core and literal replay

After Section 3 produces a small sufficient set $S$, add assumption guards
only to those rows.  Keep $u_*$ hard.  A CP-SAT sufficient assumption core
$C\subseteq S$ then yields the anchored core

\[
  \{u_*\}\cup C.
\]

Rebuild the raw-390 model with only these rows, solve it independently, and
deletion-minimize $C$ with $u_*$ fixed.  For a proposed deletion of row
$r$, impose the remaining positive assumptions and require one of:

* `INFEASIBLE`, in which case $r$ is deleted permanently; or
* `FEASIBLE`/`OPTIMAL` together with a replayed witness having exactly 98 cuts
  and 98 additions, hitting all 147 source motifs, satisfying degree two and
  every active q1 provider OR, and passing the literal top-biresidence audit.

The dynamic boundary/reach rows are a necessary relaxation, not a complete
literal residence encoding.  Therefore a SAT witness that fails literal top
residence is not a minimality witness.  Its exact short-run motif must be added
as a valid no-good and the deletion test repeated.  Infeasibility in the
relaxation is already sound for the literal problem.

A single forward deletion pass is enough for inclusion-minimality when every
retained-row test is conclusive: a witness for deleting $r$ continues to
satisfy the model after other rows are subsequently removed.  The final core
itself must be re-solved as infeasible.  All intended positive assumptions
must then be restored before exporting the frozen model proto.

If desired, test $u_*$ last in the raw model.  A literal-valid SAT witness
proves full inclusion-minimality.  Until that test is conclusive, the correct
label is **$u_*$-anchored deletion-minimal core**, not an unrestricted
minimal core.

## 5. Executable realization

The unguarded compressed CEGAR/QuickXplain stage is
`scratch/threadD_k16_r98_stageA_anchored_q1_cegar_20260729.py`, byte SHA-256
`84133741d23a938a102b090cea8dd7ce4fcd6a284d27f3e86c6181a6e3759045`.
Its default `top-mode=none` extracts the stronger pure degree/joint-q1 core.
The optional boundary mode adds the necessary top relaxation and literal
short-run separation.  The source also pins the solver-free block audit and
uses the frozen unique-provider-loss Pareto audit only to order QuickXplain
rows; that audit does not add a constraint.

The independent guarded raw-390 replay is
`scratch/threadD_k16_r98_stageB_raw_guarded_core_20260729.py`, byte SHA-256
`d721618b29f32939137cae93cd619b22877d5e78e93b956b83cc25cb80e58c50`.
It checks the Stage-A row metadata, guards only the small candidate plus row
486, retains row 486 through nonanchor minimization, replays every SAT
deletion witness, checkpoints each deletion, and restores all candidate
assumptions before exporting its final proto.  The raw top-free model has
(8152+h) variables and (1007+h) constraints for (h) guarded rows.

Both scripts are H100-CPU-only for solving.  Static compilation and all
solver-free row/census audits pass.  No Stage-A or Stage-B solver result is
claimed in this note until the corresponding H100 transcript and payload are
persisted.

## 6. What the result does and does not prove

An infeasible anchored core proves that no radius-98 repair exists inside the
390-edge cut/466-node seam face satisfying its listed q1 rows, degree two, and
the dynamic top relaxation; hence none exists satisfying full literal top
residence.  It is a genuine explanation of the failed recentered step.

It does not exclude repairs that cut a source edge outside the current motif
union to expose an outside provider.  In particular, the known alternative
providers for upper colour ((1,1907)) lie behind such portals.  The next
global model must add that portal bank rather than interpreting the anchored
core as a global radius-98 no-go.
