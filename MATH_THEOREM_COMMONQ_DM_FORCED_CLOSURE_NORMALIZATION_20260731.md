# Dimension-independent DM/forced-closure normalization for common-Q compilers

Date: 2026-07-31  
Status: proved abstract reduction; generic fail-closed implementation and exhaustive finite audit

## 1. Abstract compiler state

Fix a coordinate universe \([k]\), a finite set of physical positions \(P\),
and nonempty envelopes

\[
 E_p\subseteq[k]\qquad(p\in P).
\]

An exact row is a pair \((T,I)\), where \(T\subseteq[k]\) and
\(I\subseteq P\).  Let \({\cal R}\) be the protected exact rows.  In the
compiler application these are all scheduled middle rows together with any
lower witnesses already proved forced.  Assume

\[
 E_p\subseteq T\quad(p\in I),\qquad
 \bigcup_{p\in I}E_p=T                                      \tag{1.1}
\]

for every initial protected row.

There is a proof-safe preflight before any cell catalogue is built.  If an
envelope is empty, or if the union of the maximal envelopes on a protected
row omits a bit of its target, the fixed chronology/schedule is infeasible:
every later physical letter is a submask of its envelope, so a missing bit
can never be restored by capping.  This is the carrier gate used by the K17
scout below.

Let \({\cal L}\) be a set of distinct outstanding target masks and
\({\cal C}\) a set of physical cells, each cell being a subset of positions.
The target/cell graph is complete when \((S,C)\) is present exactly when
capping \(E_p\) by \(S\) on \(C\)

1. leaves every position nonempty;
2. preserves every row of \({\cal R}\); and
3. has OR exactly \(S\) on \(C\).

A domain-specific individual-pin theorem may generate this graph more
cheaply.  Completeness is the only hypothesis used below.  After further
caps, an old infeasible incidence cannot become feasible: envelopes only
shrink, carriers cannot reappear, and allowed target bits cannot increase.
Thus later rounds only filter the original catalogue.

The physical problem is to find nonempty letters \(Q_p\subseteq E_p\) which
replay all protected rows and give every \(S\in{\cal L}\) at least one cell
of exact OR \(S\).

## 2. Maximal common-Q theorem

For a selected incidence family \(F\), define

\[
 A_p(F)=E_p\cap
 \bigcap_{(S,C)\in F:\ p\in C}S.                            \tag{2.1}
\]

### Theorem 2.1

The selection \(F\) has a simultaneous physical realization if and only if

1. every \(A_p(F)\ne\varnothing\);
2. every protected row \((T,I)\) has
   \(\bigcup_{p\in I}A_p(F)=T\); and
3. every selected \((S,C)\) has
   \(\bigcup_{p\in C}A_p(F)=S\).

When these conditions hold, \(A(F)\) itself is a realization.

### Proof

Any realizing word \(Q\) is contained in every active envelope and every
selected target cap, hence \(Q_p\subseteq A_p(F)\).  Enlarging \(Q\) to
\(A(F)\) cannot add a forbidden coordinate to a protected row, because of
envelope containment, or to a selected cell, because of its selected target
cap.  It cannot lose a required coordinate.  This proves necessity and the
maximalization claim.  Sufficiency is literal. \(\square\)

This theorem removes all source-letter value symmetry: once the selected
incidences are known, the canonical word is (2.1).

## 3. Exact matching support

Every physical solution induces a matching saturating \({\cal L}\): choose
one witness cell for each target.  Two distinct masks cannot have the same
cell, since a physical cell has one OR.

Fix any left-perfect matching \(M\).  On right-cell vertices put an arc

\[
 C\longrightarrow M(S)
\]

for every nonmatching incidence \((S,C)\).  An incidence belongs to some
left-perfect matching exactly when it is

1. in \(M\);
2. sourced at a cell reachable from a free right vertex; or
3. on a directed alternating cycle, equivalently its source and destination
   lie in one strongly connected component.

This is the standard alternating path/cycle decomposition of the symmetric
difference of two left-perfect matchings.  It gives a linear-time allowed-
edge filter after one matching.  Deleting every unsupported edge is exact:
no witness matching of a physical word can use one.

If no left-perfect matching exists, the current state is exactly
`UNSAT_RESIDUAL_HALL`.

## 4. Forced-closure iteration

After allowed-edge pruning, a degree-one target has an incidence which occurs
in every left-perfect matching and hence in every physical solution.  Process
all such forced incidences simultaneously.

### 4.1 Cap-neutral forced witnesses

A forced incidence \((S,C)\) is cap-neutral when

\[
 E_p\subseteq S\qquad(p\in C).                             \tag{4.1}
\]

It changes no maximal letter.  Its selector can be removed, and its positive
exact-OR clauses are added unconditionally.  The cell and target are removed
from the residual matching problem.

### 4.2 Nonneutral forced witnesses

A forced incidence which fails (4.1) must **not** be silently baked.  There
are only two proof-safe choices.

1. Retain its selector as a unit and keep all of its common-Q blocker clauses;
   or
2. eagerly replace
   \[
   E_p\leftarrow E_p\cap S\quad(p\in C),                   \tag{4.2}
   \]
   add \((S,C)\) to the protected exact rows, and replay the complete state.

For eager closure, all forced caps are intersected together.  The following
are exact no-go conditions:

- a physical envelope becomes empty;
- a protected middle row loses a coordinate;
- an earlier or newly forced lower row loses a coordinate;
- filtering leaves an outstanding target with no incidence; or
- the filtered residual graph has no left-perfect matching.

Nonneutrality by itself is **not** a no-go.  A nonneutral forced cap may pass
all replay checks, after which the new capped state is exact and the process
continues.  A collision in which two forced targets require the same cell is
also impossible; in a correctly supported graph it is already exposed by
Hall, but a fail-closed implementation checks it explicitly.

### Theorem 4.1 (forced-closure equivalence)

At every successful iteration, the capped residual state is feasible if and
only if the preceding state was feasible.

### Proof

Every physical solution must use every degree-one supported incidence, so it
is contained in all caps (4.2) and realizes every newly protected row.
Therefore any displayed replay failure is inherited by every putative
solution.  Conversely, a solution of the capped residual state together with
the protected forced rows is already a solution of the preceding state.
Removing their targets and occupied cells merely records obligations already
satisfied. \(\square\)

The iteration terminates because every successful nontrivial round removes
at least one target and cell.

## 5. Fixed-q propagation at the residual fixed point

For every remaining envelope atom \((p,b)\), define its blocker set

\[
 B_{p,b}=\{(S,C):p\in C,\ b\notin S\}.                     \tag{5.1}
\]

If \(B_{p,b}=\varnothing\), maximal closure fixes that atom true.  Otherwise
introduce \(q_{p,b}\) and encode

\[
 q_{p,b}\iff\bigwedge_{y\in B_{p,b}}\neg y                \tag{5.2}
\]

using one binary clause \((\neg q_{p,b}\vee\neg y)\) per
blocker and the reverse clause

\[
 q_{p,b}\vee\bigvee_{y\in B_{p,b}}y.
\]

Fixed-true atoms propagate through the rest of the formula:

- a position containing one makes its nonempty-letter clause tautological;
- a protected row-bit with one fixed carrier needs no positive clause; and
- a selected target-bit with one fixed carrier in its cell needs no
  conditional positive clause.

This propagation is exact because it is simply partial evaluation of the
canonical word (2.1).

## 6. ALO-only exact CNF

At the fixed point use one selector \(y_{S,C}\) for every supported residual
incidence and only an at-least-one row

\[
 \bigvee_{C\in N(S)}y_{S,C}                               \tag{6.1}
\]

for each outstanding target.  Add (5.2), residual nonempty-position clauses,
positive protected-row bit clauses, and the implications

\[
 y_{S,C}\Longrightarrow
 \bigvee_{p\in C:\ b\in E_p}q_{p,b}\qquad(b\in S).      \tag{6.2}
\]

No target AMO, cell AMO, or cardinality auxiliary is needed.

### Lemma 6.1 (cell AMO is semantic)

If \((S,C)\) and \((T,C)\) are both selected, closure makes the cell OR a
subset of \(S\cap T\), while (6.2) makes it contain all of both \(S\) and
\(T\).  Hence the one cell OR equals both targets and \(S=T\).  Distinct
targets cannot share a cell.

### Lemma 6.2 (extra same-target witnesses are harmless)

Several selected cells for one target are already sound: all are required to
have that literal OR.  For normalization, retain one and delete the extras.
Removing caps only enlarges the maximal word.  It stays inside every
protected envelope and, on the retained cell, inside its retained target.
Exact protected and retained-target ORs therefore remain exact.

### Theorem 6.3 (dimension-independent ALO-only equivalence)

Under the completeness and initial replay hypotheses of Section 1, the
forced-closure fixed point is physically feasible if and only if the CNF
(5.2), (6.1), (6.2) and the displayed positive replay clauses is satisfiable.

### Proof

A physical solution chooses one witness per target, giving a supported
left-perfect matching; maximalize it by Theorem 2.1 and assign the resulting
bits.  Conversely, a CNF model defines the maximal word through (5.2).
Nonempty and protected clauses replay all old obligations, while blocker and
positive clauses make every selected cell exact.  Equation (6.1) covers all
outstanding targets.  Lemmas 6.1--6.2 account for the omitted AMOs. \(\square\)

## 7. Fail-closed implementation and audit

The reusable normalizer is

```text
scratch/commonq_forced_closure_normalizer_20260731.py.
```

It accepts arbitrary \(k\), positions, envelopes, exact protected rows,
cells, targets and a complete initial incidence catalogue.  Each round:

1. filters incidences against the current cap and protected rows;
2. rejects zero targets or Hall failure;
3. keeps only matching-supported edges;
4. classifies degree-one edges as neutral or nonneutral;
5. intersects the complete forced batch and replays it; and
6. repeats before emitting the ALO-only ledger.

The independent audit

```text
scratch/audit_commonq_forced_closure_normalizer_generic_20260731.py
```

exhaustively compares the original physical problem with the reduced problem
on seven finite fixtures.  They cover:

- a neutral forced pass;
- a nonneutral forced pass;
- a collective nonneutral empty-position contradiction;
- a collective middle-carrier loss;
- a collective protected-lower loss;
- marginal Hall failure; and
- a feasible ALO-only state where selecting two witnesses for one target is
  explicitly replayed.

All seven truth tables agree.  The same audit also authenticates the separate
c7be large-instance regression:

```text
285,232 variables
1,149,235 clauses
65,535 / 65,535 literal masks replayed
```

No SAT solver is called by either generic artifact.

## 8. K17 scout interface

For \(k=17\), the equality-scale parameters are

\[
 r=9,\quad W={17\choose9}=24310,\quad d=3,\quad B(17)=24313,
\]

and the lower target set has

\[
 \sum_{s=1}^{8}{17\choose s}=65535
\]

masks.  The scalar three-depth budget is

\[
 3W+{4\choose2}=72936,
\]

with slack 7,401 over the lower target count.

The normalizer gives a proof-safe lean scout, but not a blind SAT command:

1. authenticate one complete rank-nine chronology and fixed depth-three P/Q
   schedule;
2. replay maximal envelopes, all middle rows and arbitrary upper intervals;
3. stream the complete ranks-1--8 individual-pin graph;
4. stop immediately on zero candidates or Hall deficiency;
5. compute right-quotient matching support in \(O(|E|+|V|)\);
6. run forced closure, treating every nonneutral unit by Section 4.2 rather
   than c7be's neutral shortcut;
7. propagate fixed-q atoms and publish the exact residual variable/clause
   ledger; and
8. emit a CNF only if that independently replayed ledger is materially
   smaller than the raw selector model.

The translation quotient may help construct a K17 middle chronology, but the
final compiler reduction must use literal physical cells: quotient-equal
cells at different positions need not have the same overlap conflicts.
On H100 CPU, the adjacency should be stored as sorted integer pairs, the DM
graph contracted to right cells, and CNF clauses streamed after an audit-only
pass.  A timeout, memory cap, incomplete incidence catalogue, or non-replayed
forced cap is `UNKNOWN`, never a no-go.

The authenticated c7be-derived scout

```text
scratch/audit_k17_c7be_pascal_forced_closure_scout_20260731.py
```

stops exactly at this preflight.  Its best retained strict two-shore witness
has 66,550 physical cells (1,015 scalar slack) but loses 1,119 protected
middle rows, leaves 73 upper targets, and has no legal singleton for the new
coordinate.  More strongly, the entire fixed c7be occurrence-transversal
domain is closed before a lower compiler is built.  Although all 14,893
strict upper targets are individually feasible, the colour `0x0bf5` has
occurrence domain `{9176,10616}`, while targets `0x1bf5` and `0x0ff5`
force the two opposite choices.  An independent core uses colour `0x1ce7`
and targets `0x1def,0x3de7`.

The retained upper-73 two-shore word (SHA `ea103372...`) also fails the
independent final-start-hole monotone-deadline gate: its short-run frontier is

\[
 (\rho_1,\rho_2,\rho_3)=(11440,11440,17824),\qquad
 \sum_j\rho_j=40704>7401.
\]

The independently audited arbitrary-start extension closes every monotone
three-hole P/Q schedule for this same upper-73 word.  Its singleton run at
row 11440 forces either an early-start loss of at least 12,869 or a
deadline-threshold loss of at least 34,320, both above slack 7,401.

These are source-relative obstructions, not a K17 no-go.  Subsequent lean
rethread audits close every single contiguous reversal of this parent, the
unique reversal that adds a third `0x0bf5` occurrence together with all its
legal endpoint reroots, and the only other authenticated genuine-parent
endpoint survivor.  A new input must therefore move multiple intervals,
split/interleave so that a forced target changes its allowed-occurrence side,
or use a genuinely different source.  Any replacement candidate is screened
in the order: run-staircase
budget, exact maximal-envelope middle replay, arbitrary upper completeness,
required singleton/prepins, complete marginal Hall, and only then
DM/forced-closure/common-Q compilation.  No lower CNF is justified before
those gates pass.

This is an interface for the first unresolved finite case.  It makes no K17
existence or impossibility claim.

## 9. Scope

The theorem is dimension-independent but source-relative: it decides the
common-Q compiler only after a chronology, schedule, envelopes, protected
rows, cells and a complete incidence catalogue are fixed.  It does not prove
that such a carrier exists, and it does not transfer a fixed-fibre no-go to
another chronology or to an unrestricted construction architecture.

## 10. Frozen hashes

```text
generic normalizer source
  scratch/commonq_forced_closure_normalizer_20260731.py
  SHA 3bfefdc34f9965b9ba8f8628c7915b718332b72ad73966332e7dae353cae6343

generic independent audit source
  scratch/audit_commonq_forced_closure_normalizer_generic_20260731.py
  SHA 6d158c004a73890b2a60a05b51178c7aa7e1ed5fae0ae67f98541c790c41de35

generic audit JSON
  scratch/commonq_forced_closure_normalizer_generic_20260731.audit.json
  SHA 3a0eab91c3f710d4969150b7450edc14b239be1fc17a4c8763bcd4ee803c1243
  payload f860d3047082be8072ab01cb31dd005a0f09ebaea79b1b032c98a7b2b385ec9b
```
