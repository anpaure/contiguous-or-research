# Phase-free joint quotient-path/residence theorem

Date: 2026-07-30

Status: proved normal form and solver-free catalogue audit.  This note gives
an exact compact model for choosing the two quotient paths **together with**
their physical phases and positive residence.  It does not assert that the
model is satisfiable at `K=16`, and it does not replace the deeper-shadow or
lower-compiler audits.

The light audit implementation is

```text
scratch/audit_joint_rail_quotient_history_model_20260730.py
scratch/solve_even_two_rail_joint_history_20260730.py
scratch/solve_even_two_rail_joint_history_kissat_20260730.py
```

## 1. Why paths-first, gauges-later is the wrong factorization

For the independently generated exact `K=16` A and B quotient paths, the
open-rail gauge problem is infeasible in both orientations even after both
cross-rail seams are deleted.  Thus the failure is intrinsic to each
chronology, not merely a bad endpoint pairing.  The exact audit and frozen
artifacts are recorded in

```text
AUDIT_CLAUDE_TWO_RAIL_K10_K16_SKELETONS_20260730.md
scratch/audit_k16_rail_path_phase_residence_20260730.py
```

Residence must therefore be present while the quotient path is selected.
The important simplification is that this does **not** require adding a
second large phase model.  The phase can be absorbed into directed quotient
edge options, and residence needs only `d` insertion-history values at each
quotient vertex.

The local ingredient is the directed-history theorem already proved for the
unrestricted Johnson factor in
`MATH_THEOREM_K16_DIRECTED_HISTORY_STATIC_RESIDENCE_20260729.md`.  The result
below is its exact equivariant, seam-aware specialization.

## 2. The transition-option graph

Let

\[
 K=2R,\qquad n=K-1=2R-1,\qquad
 M=\frac1n\binom nR=C_{R-1}.
\]

Put `X=Z_n`, and let `rho(x)=x+1`.  The two old-coordinate shores are

\[
 \mathcal A={X\choose R-1}/\langle\rho\rangle,
 \qquad
 \mathcal B={X\choose R}/\langle\rho\rangle.
\]

The A shore carries the top coordinate and the B shore does not.  Both
actions are free.  Indeed, a subset fixed by a nonidentity rotation is a
union of cycles of a common length `ell>1` dividing `n`, so its cardinality
is divisible by `ell`; but

\[
 \gcd(n,R)=\gcd(n,R-1)=1.
\]

Fix one representative `S_u` of every orbit.  A **transition option** is

\[
 e=(u,v;a,b,\delta)
\tag{2.1}
\]

such that

\[
 \rho^\delta S_v=(S_u\setminus\{a\})\cup\{b\}.
\tag{2.2}
\]

Here `a` or `b` may be the sentinel `bot`, with the following four allowed
types:

| transition | deleted `a` | inserted `b` |
|---|---:|---:|
| A to A | old coordinate | old coordinate |
| B to B | old coordinate | old coordinate |
| A to B | `bot` | old coordinate |
| B to A | old coordinate | `bot` |

Thus an A-to-B seam removes the top coordinate and inserts one old
coordinate; a B-to-A seam deletes one old coordinate and inserts the top.

If the physical source is `rho^g S_u`, option (2.1) sends it to
`rho^(g+delta) S_v`.  Its absolute deletion and insertion labels are `g+a`
and `g+b`.  Therefore a selected option already contains the entire relative
phase information.  There is no need for a phase variable at a quotient
vertex.

The exact option counts are

\[
\begin{array}{c|c}
\text{type}&\text{options}\\ \hline
A\to A&M R(R-1)\\
B\to B&M R(R-1)\\
A\to B&MR\\
B\to A&MR
\end{array}
\]

and hence

\[
 \boxed{|E_{\rm opt}|=2MR^2.}
\tag{2.3}
\]

At `K=16`, `R=8`, `n=15`, and `M=429`, this is exactly `54,912`
raw options.  There are 28 A-shore and 28 B-shore quotient self-loop
options.  A connected tour on more than one quotient vertex cannot use
them, so they are fixed to zero or omitted, leaving `54,856` selectable
Hamilton options.  (Cross-shore options are never graph self-loops even when
their two shore-local indices happen to agree.)

## 3. The phase-free residence condition

Let a directed quotient tour select options

\[
 e_i=(u_i,u_{i+1};a_i,b_i,\delta_i).
\]

Let `g_(i+1)=g_i+delta_i`.  The old coordinate inserted on edge `i-s`,
expressed in the canonical frame at `u_i`, is

\[
 b_{i-s}-(\delta_{i-s}+\cdots+\delta_{i-1})\pmod n.
\tag{3.1}
\]

### Theorem 3.1 (local forbidden-window form)

Every cyclic positive run of every old coordinate has length at least
`d+1` if and only if, for every edge `i` with `a_i != bot` and every
`1<=s<=d` with `b_(i-s) != bot`,

\[
 \boxed{
 a_i\ne b_{i-s}-(\delta_{i-s}+\cdots+\delta_{i-1})\pmod n.}
\tag{3.2}
\]

#### Proof

The run killed on edge `i` has length at most `d` exactly when its most
recent insertion occurred on one of the preceding `d` transitions.  Equality
of the absolute killed and inserted coordinates is, after subtracting
`g_i`, exactly the equality excluded in (3.2).  Conversely, if (3.2) fails,
the killed coordinate was inserted at most `d` transitions earlier.  If it
was deleted and reinserted in between, the more recent insertion is also in
that window, so its current run is still short.  Sentinel transitions insert
no old coordinate and are correctly ignored.  This is the cyclic
directed-history argument.  QED.

Thus residence is a finite forbidden-pattern condition on at most `d+1`
consecutive selected transition options.  For `K=16`, `d=3`: only length-two,
length-three, and length-four edge windows matter.

### Theorem 3.2 (first-order history form)

For each quotient vertex `u`, introduce

\[
 h_1(u),\ldots,h_d(u)\in\mathbb Z_n\cup\{\bot\},
\]

where `h_j(u)` is the old coordinate inserted `j` transitions before
reaching `u`, expressed in the canonical frame of `S_u`.  On a selected
option `e=(u,v;a,b,delta)`, impose

\[
\begin{aligned}
 a&\ne h_j(u) &&(a\ne\bot,\ 1\le j\le d),\\
 h_1(v)&=b-\delta &&(b\ne\bot),\\
 h_1(v)&=\bot &&(b=\bot),\\
 h_j(v)&=h_{j-1}(u)-\delta &&(2\le j\le d),
\end{aligned}
\tag{3.3}
\]

where subtraction fixes `bot`.  Then (3.3) is necessary and sufficient for
(3.2).

#### Proof

Induction along the selected tour gives formula (3.1) in slot `s`.  The
first row of (3.3) is therefore exactly (3.2).  Conversely, the actual last
`d` insertion labels supply a solution of (3.3).  QED.

The history form is much smaller than an element-by-element age encoding.
It uses exactly

\[
 \boxed{2Md}
\tag{3.4}
\]

small-domain integer variables.  At `K=16` this is `858*3=2,574` variables,
each with domain of size sixteen.

If zero-runs are also required, add the dual history of the last `d`
deletions and forbid a current insertion from matching it.  The same proof
applies verbatim.

## 4. Exact joint Hamilton model

Use one Boolean `x_e` for every transition option.  The following system is
exact for a one-block-per-shore equivariant carrier with positive residence:

1. every orbit vertex in `A union B` has selected indegree and outdegree one;
2. exactly one selected option is A-to-B and exactly one is B-to-A;
3. the selected directed cycle cover is connected (ordinary subtour rows,
   or one `AddCircuit` over the option arcs);
4. the selected voltage satisfies

   \[
   \sum_e\delta_e x_e\equiv1\pmod n;
   \tag{4.1}
   \]

5. the reified history equations (3.3) hold;
6. every required q1 label-orbit has at least one selected option carrying
   that label.

Any unit voltage is equivalent to one by the multiplier automorphism of
`Z_n`, so (4.1) loses no solutions up to relabelling.

The q1 labels are local option data:

| option | lower palette | upper palette |
|---|---|---|
| A-to-A | `top + rank(R-2)` | `top + rank(R)` |
| B-to-B | `rank(R-1)` | `rank(R+1)` |
| cross seam | `rank(R-1)` | `top + rank(R)` |

Canonicalize the displayed old-coordinate set under rotation.  Requiring
one selected option per canonical label-orbit is sufficient even when the
label action is not free: the physical lift traverses every member of that
orbit, with repetition only when the stabilizer is nontrivial.

### Theorem 4.1 (soundness and completeness inside the two-rail class)

The system above is satisfiable if and only if there exists a
`Z_n`-equivariant middle Hamilton cycle whose quotient chronology has one A
block and one B block, whose old-coordinate positive runs have length at
least `d+1`, and whose four q1 palettes are complete.

#### Proof

From a solution, begin with any physical phase and follow the selected
options.  Equations (2.2) reconstruct every Johnson or containment step.
Connectedness visits every one of the `2M` quotient vertex-orbits once.
Voltage one makes the lift traverse all `n` physical members of each free
orbit before closing, hence all `n*2M=binom(2R,R)` middle owners exactly
once.  The history theorem gives residence, and the label rows give q1
coverage.

Conversely, quotient an equivariant two-rail carrier and canonicalize each
visited owner.  Every physical transition produces one option (2.1), its
actual last-insertion history satisfies (3.3), its lift voltage is a unit,
and its q1 coverage selects every required label-orbit.  QED.

This is a bounded-memory **colourful Hamilton cycle** problem: one state is
chosen from the history-state cluster of each quotient owner.  It is not a
pure exact-cover problem.  Vertex degree and palette rows form an exact/set
cover, but connectivity and chronological residence remain essential.  An
equivalent expanded-state graph has states `(u,h_1,...,h_d)` and ordinary
local arcs; one must choose exactly one state from each owner cluster.

For `K=16`, the compact semantic model has

```text
quotient owner vertices                       858
selectable transition-option Booleans       54,856
history integers (domain Z_15 plus bot)      2,574
q1 label-orbit coverage rows                 1,528
```

before the solver's connectivity/table auxiliaries.  The compact CP-SAT
table encoding has exactly

```text
58,289 proto variables
376,881 proto constraints
2.42 seconds build time
306,096 KiB peak RSS for a build-only audit
```

at `K=16`.  Its exact one-hot DIMACS translation, including a modulo-15
voltage automaton and sequential exactly-one counters, has

```text
299,301 variables
2,746,474 base clauses
61,395,523-byte clause body
3.38 seconds build time
39,936 KiB peak RSS for a build-only audit
```

Connectivity in the DIMACS lane is fail-closed CEGAR: a SAT directed cycle
cover is decoded, and every proper component receives the sound outgoing
subtour clause.  Only a connected assignment is materialized.  This is
orders of magnitude smaller than retaining the generic `~150M`
palette-selector catalogue after fixing rail representatives.

## 5. What this does and does not solve

This theorem removes the artificial serial gate

```text
find marginal quotient paths -> solve their phases -> test residence.
```

The correct gate is one joint local model.  The separately certified K=16
paths fail because they were optimized in the projection that forgets
history; they are not evidence against the joint class.

The model still needs the deeper-shadow conditions required by the final
compiler.  Those can be handled fail-closed: materialize every SAT candidate,
audit its lifted q2/q3 and arbitrary upper windows, and add sound motif cuts
or eager bounded-window rows.  A SAT carrier must still pass the independent
physical replay.  Conversely, an UNSAT claim is only as broad as the eager
shadow catalogue included in the model.

For a proof of the general formula, one would need an existence theorem for
these residence-decorated quotient tours (or a more flexible multicomponent
braid), not merely a solver success at `K=16`.

## 6. Solver-free validation

The audit script independently enumerates the transition catalogue.  It
returns at `K=16`:

```text
A->A  24,024       B->B  24,024
A->B   3,432       B->A   3,432
raw total 54,912; internal self loops 56; selectable total 54,856
history integers 2,574
q1 label orbits 335 + 429 + 429 + 335 = 1,528
```

It also reconstructs the known equivariant `K=10` carrier

```text
scratch/even_multicomponent_waksman_k10_20260729_PASS.json
SHA-256 b0fd491c03a2d76c34c8de71534a365ce7dd1ac6a1e6e6ccddb546498abab7ef
```

and obtains

```text
middle_distinct=252
johnson_bad=0
history_violation_count=0
direct_short_old_run_count=0
pass_residence=true
```

Thus the quotient-history criterion agrees with a fresh direct cyclic run
audit on a nontrivial known optimum.  No heavy search is performed by this
validation.

There are two further independent checks.

1. `scratch/search_k16_moving_frame_resident_rail_portfolio_20260730.py`,
   written independently from this note, implements the same moving-frame
   recurrence for an open rail.  Its `n=9` A/B regressions are SAT and its
   literal replay agrees with the earlier phase-expanded model.  This checks
   the sign of `delta`, the sentinel convention, and the exact option-label
   semantics independently.
2. Both executable joint models solve `K=8` and `K=10`.  The DIMACS lane
   needs 7 subtour-cut rounds at `K=8` and 15 at `K=10`, then literal replay
   passes.  The fresh `K=8` carrier compiles through `sandwich2.py` to a word
   of length 72, and the independent exhaustive verifier reports
   `255/255`.  The known compact two-rail `K=10` artifact
   `ck10t2r_PASS.json` satisfies the exact one-block, unit-voltage,
   moving-history and both-q1 conditions; its length-254 word independently
   verifies `1023/1023`.

The first 300-second K=16 DIMACS/Kissat round returned `UNKNOWN` before even
a cycle cover was found; it added no subtour cut and is inconclusive.  A
single controlled 1,800-second CP-SAT table run is still in progress on the
remote CPU box under a 24 GiB address-space guard.  Any run terminated by its
memory/runtime guard is recorded only as `UNKNOWN`.  Neither a build nor an
`UNKNOWN` solve is evidence for satisfiability or unsatisfiability.
