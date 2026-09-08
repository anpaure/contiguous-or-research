# K15 facet-rail repair: fixed-H selector CNF audit

Date: 2026-07-29  
Status: exact source-relative CNF/CEGAR implemented and independently audited.
All 31 saved frontier witnesses are ruled out; the general choice of `H`
remains open.

## 0. Verdict

The fixed-collar-transversal problem is so much smaller than unrestricted
`RTR(7,4)` that it should be the first computational lane.

For the exact 60-orbit witness in
`scratch/k15_facet_rail_q1_rethread_frontier_20260729.audit.json`, the
old-choice-excluded model has:

| quantity | fixed `H`, `b=60` |
|---|---:|
| domain rows | 60 |
| semantic pair choices | 1,620 (`60*27`) |
| total CNF variables | 4,529 |
| clauses | 10,516 |
| literals | 22,037 |
| distinct degree rows | 298 |
| lower-restoration rows | 18 |

It is `INFEASIBLE` before residence clauses.  Kissat, CaDiCaL, and a direct
weighted CP-SAT model agree.

This is **not** an `FRR(7,4)` no-go.  It says the particular minimum collar
transversal selected by the old width-three DP cannot support any
degree-preserving, lower-rainbow rethread.  The correct next model must
choose `H` and the replacement pairs jointly, or enumerate alternative
degree-aware collar transversals.

## 1. Exact fixed-H model

Let `B0` be the saved facet derivative.  Its large component has length

\[
 6390=426\cdot15
\]

and voltage four:

\[
 X_{i+426}=\rho^4X_i.
\tag{1.1}
\]

Let `H subset Z_426` be a selected family of quotient upper-colour edges.
For each `q in H`, choose a pair

\[
 p_q\in\binom{U_q}{2}.
\]

Its fifteen physical lifts are obtained by rotating both `U_q` and `p_q`
by `4j`, `j in Z_15`.  One Boolean variable `x_(q,p)` represents the whole
physical orbit.

### Static constraints

1. **One replacement per upper orbit**

   \[
   \sum_{p\in\binom{U_q}2}x_{q,p}=1.
   \tag{1.2}
   \]

   If `H` is the actual cut set, the old pair is removed from the domain.
   If `H` is merely an eligible bank, it remains available.

2. **Endpoint degree conservation**

   If `d_H^0(X)` is the number of old cut edges incident with rank-seven
   vertex `X`, and `m_X(q,p)` is the number (zero, one, or two) of lifted
   new edges incident with `X`, impose

   \[
   \sum_{q,p}m_X(q,p)x_{q,p}=d_H^0(X).
   \tag{1.3}
   \]

   This is exactly equation (4.10).  Rotation-identical physical rows are
   deduplicated; the `b=60` instance has 298 distinct rows.

3. **Lower-colour restoration**

   For every rank-six colour whose retained load becomes zero, impose

   \[
   \sum_{(q,p):U_q\setminus p=R}x_{q,p}\ge1.
   \tag{1.4}
   \]

   The 270 physically lost colours collapse to 18 quotient rows.  Upper
   colours need no constraint: every `U` still selects exactly one edge.

Equations (1.2)--(1.4) are exactly the signed circulation and lower rows
(4.10)--(4.11), not a relaxation.

## 2. Exact residence CEGAR

After SAT, the implementation reconstructs all 6,435 physical edges:
unchanged edges off `H`, plus the fifteen lifted edges of every selected
pair.  It checks degree two and both q1 palettes literally, traverses all
components, and finds every positive coordinate run of length one, two, or
three and every component shorter than four.

For a bad run with closed path `P`, fixed edges are ignored and the selected
`H` variables occurring on `P` form a clause

\[
 \bigvee_{x_{q,p}\in P}\neg x_{q,p}.
\tag{2.1}
\]

This is universally sound: retaining every path edge forces the bordered
short run because each interior vertex has its two degrees exhausted.  If
`P` contains no variable edge, the chosen `H` can never repair that motif.

The solver is
`scratch/solve_k15_frr_fixed_h_selector_cegar_20260729.py`.

## 3. Independent validation

### Old-factor replay

With all 28 choices present and every old choice pinned, the CNF is SAT and
the independent physical replay recovers:

* two components;
* complete lower and perfect upper q1 palettes;
* exactly 1,425 positive runs of length three and no other violation type;
* 62 distinct selector clauses after the 95 quotient collars are projected
  through this particular `H`.

Thus the degree, palette, lift, cycle, and residence maps reproduce the
known source rather than merely satisfying internal bookkeeping.  Artifact:
`scratch/k15_frr_h60_pinold_audit_20260729.json`.

### Exact 60-orbit witness

Removing the old choice from each of the 60 domains makes (1.2)--(1.4)
infeasible without any residence cut:

| backend | verdict | time |
|---|---|---:|
| Kissat CNF | UNSAT | 0.006 s |
| CaDiCaL CNF | UNSAT | immediate |
| direct CP-SAT weighted equations | INFEASIBLE | 0.0014 s |

Excluding all old choices is sound here: 60 is the proved minimum collar
transversal, so retaining even one of these 60 edges leaves at most 59
actual changes and cannot hit every old collar.

Artifact: `scratch/k15_frr_h60_exact_result_20260729.json`.

### The 61--90 saved frontier witnesses

For every saved DP witness of size `b=60,...,90`, a broader eligible-bank
model was also tested: the old choice was allowed, so the actual changed set
could be any subset of the bank.  Each base model was SAT; its literal bad
paths generated 57--72 sound clauses; the second solve was UNSAT in every
case.

This proves that none of the 31 saved witness banks contains a positive-
resident repair.  It does not quantify over other collar transversals of the
same cardinalities.

Artifact: `scratch/k15_frr_frontier_witness_bank_scan_20260729.json`.

## 4. Size comparison

The unrestricted physical turn-selector fallback has:

| quantity | unrestricted RTR | fixed `H=60` | ratio |
|---|---:|---:|---:|
| semantic choices | 180,180 | 1,620 | 111x |
| total variables | 1,061,775 | 4,529 | 234x |
| clauses | 4,985,696 | 10,516 | 474x |
| literals | 29,749,006 | 22,037 | 1,350x |

Even against the not-yet-implemented 429-orbit quotient RTR, fixed `H` has
60 domain rows rather than 429 and 1,620 rather than 12,012 pair choices—a
factor 7.15--7.4.

`breager.py` allocates at least 5,889,312 mid/q1 channel variables before
its all-depth selectors.  The fixed-H CNF is over 1,300 times smaller than
that lower bound alone.

The unrestricted fallback implementation and count artifacts are:

* `scratch/search_odd_turn_selector_cnf_20260729.cpp`;
* `scratch/decode_odd_turn_selector_20260729.py`;
* `scratch/solve_odd_turn_selector_cegar_20260729.py`;
* `scratch/odd_turn_selector_k15_count_20260729.json`.

The fallback passed an end-to-end `n=7`, residence-three regression after
675 sound path cuts; see
`scratch/odd_turn_selector_k7_rtr3_PASS_20260729.json`.  A preliminary
`n=9` CEGAR run was stopped without a verdict when the fixed-H reduction
became available.

## 5. Correct strategic conclusion

The old DP optimized only collar coverage and lower-colour loss.  Its entire
saved Pareto frontier is incompatible with the endpoint circulation once
residence is enforced.  Therefore the new structural target is not “search
replacement pairs harder on this `H`.”  It is:

> choose the collar transversal and the alternating-circuit/endpoint flow
> jointly.

The fixed-H solver should remain the cheap oracle inside that outer search.
For every proposed `H` it gives one of three exact answers within a very
small model:

1. endpoint/lower infeasible before residence;
2. residence-infeasible after universal path clauses;
3. a literal repaired factor.

No heavy local execution is required.  Future banks should be evaluated on
the H100 CPU under a 512 MB--1 GB cap and one low-priority solver core; the
current instances use under 60 MB.
