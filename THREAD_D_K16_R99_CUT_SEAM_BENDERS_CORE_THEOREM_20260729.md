# Thread D — exact radius-99 cut/seam Benders theorem

**Date:** 2026-07-29  
**Status:** proof-safe source and solver-free regressions complete; no H100 job
launched under the current memory hold.

**Current companion audit.**  Full-atlas guarded closure, its exact
depth-two dominance obstruction, and the non-equivariant fl73 scope are in
`THREAD_D_K16_R99_FULL_ATLAS_HYPERRESOLUTION_AND_FL73_SCOPE_20260729.md`.
The four syntactic depth-two rows found there are deliberately not installed
in this driver because existing primitive portal rows dominate them.

## 1. Frozen instance

Let (F) be the 858-edge source quotient factor in
`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`.  A radius-99
repair has source-cut vector (c\in\{0,1\}^{F}), with

\[
\sum_{e\in F}c_e=99,
\]

and an addition vector (a) on the complete set of 26,570 loopless
off-source quotient edges.  The two master branches fix whether edge 22511
is retained or cut.

The implementation is
`scratch/solve_k16_r99_cut_add_benders_cegar_20260729.py`.

## 2. Cut master

The master contains all 858 literal cut bits and the following necessary
rows.

1. Radius 99, the selected 22511 branch, and all 147 current residence-motif
   hitting rows.
2. The exact two-palette, endpoint-capacitated matching relaxation for
   double repairs, including the dynamic demand
   \(L_-(c)+L_+(c)-99\).
3. The audited branchwise Pareto facets.
4. All 1,328 unique-colour portal rows.
5. Three deduplicated level-2 same-palette portal-Hall rows (four audited
   branch/palette certificates, with the lower row shared).

For a source-unique q1 colour with source provider (e=uv), suppose no
off-source provider is parallel on ({u,v}).  Let (Z_e) be the other
endpoints used by all alternative providers, and let (I_F(Z_e)) be the
source edges incident to (Z_e).  Every exact completion satisfies

\[
c_e\leq \sum_{f\in I_F(Z_e)}c_f. \tag{P_e}
\]

Indeed, if (e) is cut, q1 coverage chooses an alternative seam incident
to a vertex of (Z_e).  Its positive added degree must be balanced by
positive cut degree at that vertex.  Thus ((P_e)) is cut-only and does not
depend on a proposed seam set.

The master is a necessary relaxation, not a claim that its double-matching
variables themselves form a complete seam solution.

### Same-palette portal-Hall hierarchy

For a set (T) of nonparallel source-unique colours in one palette, let
(P=\bigcup_{c\in T}P_c).  Distinct lost colours require distinct added
seams, and every replacement seam for (c) meets (P_c).  Exact degree
restoration therefore gives the valid cut-only inequality

\[
 \sum_{h\in F}|\operatorname{ends}(h)\cap P|c_h
 \;\ge\;\sum_{c\in T}c_{e(c)}. \tag{PH}_{T}
\]

This strictly dominates first-order portals: the frozen first-order-feasible
retain/delete cuts violate lower rows (5>3) and upper rows (8>4).
The implementation installs the exact linear inequalities, not the four
candidate-specific signed clauses emitted by the audit: after deduplicating
the shared lower row there are three rows, and each linear row already
subsumes its associated candidate no-good (including for fractional master
points).

Separation of the canonical **fixed portal-union subfamily** is polynomial.
This does not optimize over all alternative vertex covers of each provider
graph.  For a possibly fractional
cut vector (x), give colour (c) profit (x_{e(c)}), give portal vertex
(v) cost
(d_x(v)=\sum_{h\ni v}x_h) (endpoint multiplicity), and impose the closure
arcs (c\to v) for every (v\in P_c).  The maximum closure value is

\[
\max_T\left(\sum_{c\in T}x_{e(c)}-
\sum_{v\in\cup_{c\in T}P_c}d_x(v)\right),
\]

so a source–colour–portal–sink min-cut returns a most violated row in this
fixed-portal subfamily.  The driver performs this exact separation on every
integer master candidate before dispatching the seam subproblem and records
each new row in the replay ledger.

The family deliberately excludes the 20 source-unique colours having an
off-source provider parallel on the two base endpoints (8 lower, 12 upper):
such a provider need not use an external portal, so the stated implication
arc is unavailable.  Those colours remain handled by the exact seam
subproblem.

## 3. Universal seam subproblem

The subproblem retains the same symbolic 858 cut variables and the entire
26,570-column seam atlas.  It imposes

\[
\sum c_e=\sum a_f=99,
\qquad
\sum_{f\ni v}a_f=\sum_{e\ni v}c_e\quad(v\in V),
\]

together with all 764 lower-q1 and 764 upper-q1 rows.  The motif, Pareto,
portal, and aggregate repair rows are retained as redundant exact rows.
No cut is installed by equality, and no candidate endpoint halo is used.

This universality is essential: a core extracted after restricting seams to
the current cut's endpoints would not be valid for another cut containing
the same partial cut pattern.

## 4. Positive-core Benders lemma

**Lemma.** Let (C\subseteq F), (|C|=99), be a master cut.  In the
universal seam formula (Phi(c,a)), assume only the 99 positive literals

\[
\{c_e:e\in C\}.
\]

The radius equation forces (c_f=0) for every (f\notin C), so this is the
exact fixed-cut seam problem.  If CP-SAT proves it infeasible and returns a
sufficient assumption core (K\subseteq C), then every seam-completable
master cut satisfies

\[
\boxed{\sum_{e\in K}c_e\le |K|-1.} \tag{B_K}
\]

**Proof.** The sufficient core states that
(Phi(c,a)\land\bigwedge_{e\in K}c_e) is infeasible.  Therefore no feasible
projection of (Phi) contains all of (K), which is exactly ((B_K)).
The original candidate violates ((B_K)) by one.  This excludes every
radius-99 cut containing (K), not only (C).  ∎

The implementation deletion-shrinks (K), removing a literal only after an
exact INFEASIBLE re-solve; SAT or UNKNOWN retains it.  It claims deletion
minimality only when every retained-literal test was conclusive and the wall
budget was not exhausted.  It then exports an assumption-bearing model proto
and re-solves the final core.  A row is added only after that replay returns
INFEASIBLE.  UNKNOWN produces no row.  An empty replayed core proves the
entire locked branch infeasible.

This is an executable CP-SAT transcript, not a DRAT-style formal proof.

## 5. Exact high-slack diagnosis

The two high-slack double-capacity cuts are already excluded by the eager
master:

| branch | declared capacity slack | violated portal rows |
|---|---:|---:|
| retain 22511 | 25 | 7 |
| delete 22511 | 24 | 6 |

The solver-free reproducer is
`scratch/audit_threadD_k16_r99_highslack_portal_rows_20260729.py`; its output
is `scratch/threadD_k16_r99_highslack_portal_rows_20260729.audit.json`.
It also binds the two exact fixed-cut results, each INFEASIBLE with zero
branches and zero conflicts.  Consequently those presolve failures need no
seam-core explanation.  The Benders driver records the legacy hints as
rejected and does not send them to CP-SAT.

## 6. Exact algorithmic guarantee

For either fixed 22511 branch, assume every master and subproblem call ends
in FEASIBLE/OPTIMAL or INFEASIBLE.  Each infeasible seam call removes at
least its current cut by a valid row ((B_K)).  The cut space is finite.
Hence the loop terminates with either:

1. an exact degree-two factor passing both q1 palettes under literal replay;
   or
2. a master-INFEASIBLE transcript proving that this branch has no q1 seam
   completion.

Global scope requires both branches.  Connectivity, voltage, fresh
residence, and higher shadows are reported on a positive factor but are not
hard constraints in this q1 decomposition.

## 7. Reproduction status and deferred commands

Local lightweight checks completed:

- Python syntax compilation;
- thirteen pure core/polarity/hash regressions;
- the solver-free 7/6 portal replay;
- the replay verifier's self-test.

No H100 build or solve was run because the host is under explicit
memory/swap hold.  The authoritative launch surface is the frozen directory
`scratch/threadD_k16_r99_benders_lowmem_launch_20260729`, whose manifest
digest is
`4b473b172c9d30345aa81a3762dfa7c1229eb88ffe2d086297fc548224d147c4`.
It enforces one worker, hard address-space limits, a headroom/swap gate, fresh
output namespaces, and explicit authorization.  The raw command below is
retained only as an argument-order reference and must not be used to bypass
that launcher:

```bash
PYTHONPATH=/dev/shm/orlib python3 scratch/solve_k16_r99_cut_add_benders_cegar_20260729.py \
  scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json \
  scratch/threadD_k16_r99_cutspace_scope_20260729.audit.json \
  scratch/k16_r99_cut_double_capacity_relaxation_20260729.audit.json \
  scratch/ad_k16_r99_unique_colour_portal_rows_20260729.audit.json \
  scratch/k16_r99_portal_hall_strictness_20260729.audit.json \
  scratch/k16_r99_6c98_fourcolour_endpoint_cover_cut_20260729.audit.json \
  --branch retain \
  --output scratch/threadD_k16_r99_benders_retain_20260729.json \
  --checkpoint scratch/threadD_k16_r99_benders_retain_20260729.checkpoint.json \
  --master-model scratch/threadD_k16_r99_benders_retain_20260729.master.pb \
  --subproblem-model scratch/threadD_k16_r99_benders_retain_20260729.subproblem.pb \
  --core-proof-dir scratch/threadD_k16_r99_benders_retain_20260729.cores \
  --workers 1 --rounds 1
```

Replace `retain` by `delete` and use distinct output paths for the other
branch.  After copying the result and core protos back, replay with
`scratch/audit_threadD_k16_r99_cut_add_benders_20260729.py`; add
`--resolve-core-protos` on H100 for independent CP-SAT core re-solves.
