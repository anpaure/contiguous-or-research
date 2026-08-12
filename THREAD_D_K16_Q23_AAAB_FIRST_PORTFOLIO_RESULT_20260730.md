# Thread D: K16 q2/q3 AAAB-first portfolio result

**Date:** 2026-07-30  
**Scope:** source-independent one-A-block/one-B-block K16 joint-history model;
bounded H100 CPU runs plus solver-free structural audits.  No source carrier,
edit radius, prescribed seam, or source-relative transition is used.

## Exact runtime conclusion

The unbranched master with the period-three q2 target `37449` and q3 target
`4681` preinstalled ended `UNKNOWN` after 1800.036 solver seconds
(1809.430 seconds including construction).  It produced no SAT carrier and no
UNSAT proof.

The exact disjoint 63-case partition was then installed, AAAB-first.  The four
smallest compact branches have the following retained terminal records:

| branch | seed | solver cap/result | joint / wrapper wall (s) | checked UNSAT proof | carrier / compiler |
|---|---:|---|---:|---|---|
| `AAAB_A380` | 20260750 | 180 s / `UNKNOWN` | 189.223 / 189.335 | none | none |
| `AAAB_A384` | 20260784 | 180 s / `UNKNOWN` | 189.226 / 189.371 | none | none |
| `AAAB_A395` | 20260801 | 180 s / `UNKNOWN` | 189.302 / 189.402 | none | none |
| `AAAB_A406` | 20260818 | 180 s / `UNKNOWN` | 190.196 / 190.314 | none | none |

Every run used one process, `--deep-cegar`, a 1536 MiB address-space cap, and
the exact compact branch formula.  Each formula had 320,831 variables and
3,781,332 clauses: the common 320,751-variable/3,781,072-clause base plus 80
exact q2-prefix variables and 260 exact branch clauses.  No branch reached a
SAT assignment, so physical replay, deeper CEGAR, the all-cut COMP3 bridge,
and literal 65,535-mask verification were not entered.

The aggregate result is therefore

\[
  \boxed{\texttt{UNKNOWN}:\quad
  0\text{ SAT carriers},\quad 0\text{ proved-UNSAT branches}.}
\]

This is not evidence that any of the four branches is infeasible, and it says
nothing terminal about the other 59 branches.  The launcher does not log a
checked proof; a solver `UNSAT_NO_PROOF` would also count as zero proved
branches.  Only a completed, independently checked proof may contribute to a
63-case UNSAT conclusion.

## Why execution was split

The first sequential wrapper completed `AAAB_A380`, then correctly stopped at
its live-process collision guard when an unrelated compact-CNF preprocessing
job appeared.  After that job ended, a second sequential wrapper completed
branches 1--3.  The retained first portfolio therefore has status
`BLOCKED_LIVE_PROCESS_CONFLICT_NO_LAUNCH`, while the resume portfolio has
status `UNKNOWN_BRANCH_PORTFOLIO`.  The independent runtime audit consumes
both authenticated parts and requires exact, nonoverlapping coverage of
indices 0--3.

Four earlier 600-second AAAB scouts also ended `UNKNOWN`, but they used the
old overlapping positive restrictions, omitted deep CEGAR, and are not four
cases of the new disjoint partition.  They remain a separate historical
sample in `scratch/threadD_k16_q23_aaab_small_external_20260730.audit.json`.

## Structural result after the four UNKNOWN branches

The capped run was not extended.  Instead, exact catalogue analysis gives the
next forced-provider decomposition.

For every one of the four branches, the AAAB terminal collar forces a shifted
q2 label:

\[
  380,395\mapsto4683,
  \qquad 384,406\mapsto4685.
\]

Positive depth-three residence leaves exactly 35 first B-to-B options.  They
partition, disjointly and exhaustively, into five sets of seven according to
the next q3 label:

\[
\begin{array}{c|c}
380,395 & 587,601,713,1609,2341\\
384,406 & 589,617,841,1171,2633.
\end{array}
\]

Thus each UNKNOWN AAAB branch has an exact five-way subportfolio.  A fixed
subcase needs 640 clauses of length nine and no new variables, reusing the 80
q2-prefix AND variables.  The five alternatives must be run separately; they
must not be conjoined.

There is also a sharp negative localization result.  In each branch, 150
terminal fragments consume the unique `top+rank(R)` q1 repeat token, forcing
the remaining 427 occurrences to be a rainbow.  All 600 resulting
colour--source and colour--target marginal graphs have matching number 427;
the weakest residual q1 row still has 18 providers, and residual node degrees
remain at least 35 outgoing and 34 incoming.  Consequently no one-level
marginal Hall cut closes these cases.  The surviving gate couples source,
target, colour, rail order, and three-step insertion history simultaneously.

The exact theorem and audit are
`THREAD_D_K16_AAAB_NEXT_COLLAR_AND_MARGINAL_HALL_20260730.md` and
`scratch/threadD_k16_aaab_next_collar_hall_20260730.audit.json`, whose stable
payload SHA-256 is
`53223ff5012658351730d396b4969ca8ca007d861010f843d7d591c31ce09e57`.

## Retained provenance

Runtime files are under
`scratch/k16_q23_disjoint_aaab_first_run_20260730/`.  The two producer
portfolio file hashes are

```text
portfolio_00_blocked.json  8bd18a26a9459d8f1bd7250eff17497c9372ed3706dfa0494442f0ae6b7d818e
portfolio_01_03.json       26082c13afc8456abd1877b56cef8695bad316808d2a908d54a35c811cd306c6
```

The retained `remote_full_sha256.txt` authenticates all four generated CNFs,
the common base body, result JSONs, and solver transcripts without retaining
the four 85 MB CNFs locally.  The independent solver-free result audit is
`scratch/threadD_k16_q23_disjoint_aaab_first_run_20260730.audit.json`.

