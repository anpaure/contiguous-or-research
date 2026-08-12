# Thread D — K16 q2/q3 AAAB-first four-branch result audit

Date: 2026-07-30

## Result

The four smallest disjoint subgroup branches

\[
  \mathrm{AAAB}_{380},\quad \mathrm{AAAB}_{384},\quad
  \mathrm{AAAB}_{395},\quad \mathrm{AAAB}_{406}
\]

were run sequentially in the exact source-independent one-block two-rail
model.  Every branch ended **UNKNOWN** at its 180-second inner solver cap.
No retained Kissat output contains either a SAT or an UNSAT terminal line.
Consequently:

* proved UNSAT branches: **0**;
* unproved UNSAT branches: **0**;
* q1/residence carriers: **0**;
* deep-shadow CEGAR entries: **0**;
* physical carrier replays: **0**;
* COMP3 entries: **0**; and
* verified 65,535-mask words: **0**.

This is a bounded UNKNOWN result, not evidence of infeasibility.

## Exact branch structure installed

Each branch used the proved AAAB terminal-position/Hall compression.  For its
named exceptional A-node `m`, the q3 witness is equivalent to

1. selecting one of the 80 exact q2 prefixes through `m`, and
2. imposing `position_A(m)=427`.

The 80 prefixes have 8 terminal extensions each, hence represent 640 logical
q3 providers.  Exact q1 repeat-excess conservation excludes 10 terminal
triples.  The resulting local branch extension has 80 auxiliary variables
and 260 clauses: 241 prefix-DNF clauses, 9 position units, and 10 q1
no-goods.  The stale earlier-AAAB exclusions are absent.  All four retained
producer ledgers replay these numbers exactly and declare no source-relative
constraint.

Thus the requested forced-provider/Hall structure was extracted before this
portfolio.  The run establishes that this first compression alone does not
make the four smallest cases easy at a short cap.  The correct next step is a
second branch-level Hall/provider contraction on the 630 surviving terminal
fragments, not a blind increase of solver time.

## Split execution and provenance

The initial `[0,4)` driver completed branch 0 and then stopped at its live-job
collision guard.  A fresh `[1,4)` resume completed branches 1–3.  The audit
requires the completed branch rows to be disjoint and to cover exactly
indices `0,1,2,3`; the split does not duplicate or omit a mathematical case.

The two outer runs respectively used at most 362,472 KiB and 369,800 KiB RSS,
with zero swaps.  Both declared one sequential process, a 1,536 MiB branch
address-space cap, and a 2,048 MiB COMP3 cap.  The copied remote SHA manifest
authenticates all 12 retained result, solver-log, and round-output files.

The independently generated machine audit is
[`scratch/threadD_k16_q23_disjoint_aaab_first_run_20260730.audit.json`](scratch/threadD_k16_q23_disjoint_aaab_first_run_20260730.audit.json).
Its status is `NO_LITERAL_PASS_UNKNOWN`.  The auditor is
[`scratch/audit_threadD_k16_q23_disjoint_four_branch_run_20260730.py`](scratch/audit_threadD_k16_q23_disjoint_four_branch_run_20260730.py).

## Proof policy

The launcher deliberately emits no checked proof.  Therefore a future
`UNSAT_NO_PROOF` result in this portfolio would remain diagnostic and would
count as zero proved branches.  Only a separately completed and checked proof
artifact can change the proved-UNSAT count.  Time, memory, round, and state
limits remain UNKNOWN.
