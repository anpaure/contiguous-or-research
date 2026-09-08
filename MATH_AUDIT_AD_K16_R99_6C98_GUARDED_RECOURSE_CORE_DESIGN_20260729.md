# AD audit: the `6c98` fixed-add conflict and a guarded radius-99 recourse core

Date: 2026-07-29

This note is solver-free.  It audits the semantics of the persisted `6c98`
fixed-cut instance and gives an exact parametric model from which a genuine
cut-space Benders core can be extracted.  It does **not** report a new solve.

## 1. Frozen inputs and the present evidentiary boundary

The relevant persisted objects are:

* cut digest
  `6c98aa96b824b580be70fb9bab617e80fef233b4bf11b33a7a83adce5d9c39b4`;
* fixed CNF
  `scratch/k16_r99_fixed_delete_6c98_degree_q1_20260729.cnf`, SHA-256
  `fbcbace828f3aad11e61291e4244a51a23adedee384182a8ec5ea26eefc67dfc`;
* fixed-CNF solve transcript
  `scratch/k16_r99_fixed_delete_6c98_degree_q1_20260729.solve.json`, SHA-256
  `2955a67b70a615ba199e6a61cf03031e33478eacf9e099f44b9941bccc261902`;
* q1-row shrinking result
  `scratch/k16_r99_fixed_delete_6c98_q1_core_20260729.json`, SHA-256
  `d4c434aca2c5ccb8e90356e8dd110ace1b41c53d210588dec32cbe68a5f81f06`.

The fixed CNF has 9,938 variables and 19,816 clauses.  Its semantic census is
1,448 usable add seams, 198 cut endpoints of demand one, 68 lost lower q1
rows, and 70 lost upper q1 rows.  The saved CaDiCaL transcript says UNSAT.
There is currently no saved DRAT/LRAT proof in this artifact chain.  Thus the
UNSAT status is an independently reproduced exact-solver transcript, not yet
a formally replayable proof certificate.

The q1-row shrinker reports that degree restoration together with just the
following four upper rows is UNSAT, while deleting any one of the four makes
that reduced instance SAT:

| upper colour | unique source provider | usable add providers | endpoints of usable providers |
|---|---:|---:|---|
| `(1,1883)` | `4742` | `4737,4740,18552,18555,21385` | `92,499,576,617` |
| `(1,1907)` | `22511` | `18171,18172` | `490,611,617` |
| `(1,3255)` | `23229` | `21408,21411` | `576,638,754` |
| `(1,5939)` | `24034` | `22529,22530` | `611,663,739` |

That result is deletion-minimal among q1 rows relative to the fixed degree
system.  It is not a minimum-cardinality result, and its saved evidence is a
Kissat transcript rather than a proof trace.

Most importantly, these four q1 rows are **not** by themselves a cut-space
core.  The other 95 cut edges determine the active endpoint set and hence the
perfect-matching graph.  Nothing presently proves the tempting row

\[
 x_{4742}+x_{22511}+x_{23229}+x_{24034}\leq 3.                 \tag{1.1}
\]

It must not be added to the master without a parametric replay.

## 2. Exact universal recourse relation

Let `S` be the 858 selected source edge orbits, let `A` be all 26,570
loopless off-source seams, and let `V` be the 858 quotient nodes.  Endpoint
incidence is counted with multiplicity; write `mu(v,e)` for that incidence.
For every lower or upper quotient q1 colour `c`, let `S_c` and `A_c` be its
providers in `S` and `A`, respectively.

For Boolean cut variables `x_e`, `e in S`, and Boolean add variables `y_a`,
`a in A`, define `REC_99(x,y)` by

\[
 \sum_{e\in S}x_e=99,                                       \tag{2.1}
\]

\[
 \sum_{a\in A}\mu(v,a)y_a
 =\sum_{e\in S}\mu(v,e)x_e \quad(v\in V),                  \tag{2.2}
\]

and, for every one of the 764 lower and 764 upper q1 colours,

\[
 \sum_{e\in S_c}(1-x_e)+\sum_{a\in A_c}y_a\geq1.          \tag{2.3}
\]

### Theorem 2.1 (exact q1 recourse)

For a radius-99 cut `C`, the add set `B` gives exact quotient degree
restoration and both complete q1 palettes if and only if its incidence vector
`y` satisfies (2.2)--(2.3) with `x=1_C`.

#### Proof

The selected orbit set after rethreading is `(S\C) union B`.  At node `v`,
its degree changes by minus the right side of (2.2) and plus the left side,
so (2.2) is exactly degree restoration.  Colour `c` survives precisely when
some source provider is not cut or some add provider is selected, which is
exactly (2.3).  These are the only asserted gates.  QED.

The explicit constraint `sum y=99` is redundant.  Summing (2.2) over all
nodes counts every source edge and every allowed add seam twice, and hence

\[
 2\sum_a y_a=2\sum_e x_e=198.
\]

No connectivity, voltage, residence, or deeper-shadow claim follows.

### Theorem 2.2 (canonical degree/loss-state compression)

For a cut `x`, define

\[
 d_v(x)=\sum_{e\in S}\mu(v,e)x_e,
 \qquad
 \ell_c(x)={\bf1}[\text{no edge of }S_c\text{ is retained}]
 = {\bf1}[x_e=1\text{ for every }e\in S_c].                \tag{2.4}
\]

The all-quantifier is vacuous when `S_c` is empty, so such a colour has
`ell_c=1` as required.

The existence of q1 recourse depends on `x` only through the vector `d(x)`
and the lower/upper loss indicators `ell(x)`.  Equivalently, it is the
feasibility of

\[
 \sum_{a\in A}\mu(v,a)y_a=d_v \quad(v\in V),              \tag{2.5}
\]

\[
 \sum_{a\in A_c}y_a\geq\ell_c \quad(c\text{ a q1 colour}).\tag{2.6}
\]

#### Proof

Equation (2.2) is (2.5).  If at least one source provider of `c` is retained,
(2.3) is automatic; if all are cut, it is exactly (2.6) with right side one.
Thus (2.3) is equivalent to (2.6) in both cases.  QED.

This is an exact recourse-state quotient, not merely a necessary
aggregation.  It suggests a second assumption interface: use integer state
variables `d_v in {0,1,2}`, loss bits `ell_c`, `sum_v d_v=198`, all add
variables, and (2.5)--(2.6).  Guarded assumptions fixing selected `d_v`
values and selected loss bits can yield a state no-good that is substantially
more reusable than an edge-identity no-good.  Translation back to the master
requires the exact links (2.4), including both directions of each loss-bit
equivalence.

In CP-SAT, the pure universal recourse model therefore needs 27,428 Boolean
variables and exactly

\[
 1+858+1528=2387
\]

native constraints.  This removes the branch lock, 147 motifs, Pareto rows,
1,328 first-order portal rows, eager Hall rows, and aggregate repair rows from
the present recourse model.  Those rows belong in the master.  Omitting them
from recourse makes any extracted conflict valid across both branches and
across all master strengthenings.

The production driver now implements this reduction: its exact full recourse
has 2,387 constraints in both branches and contains no branch lock or imported
master-valid cut row.  Every replayed positive assumption core is therefore
valid across both branch masters and across later master strengthenings.  Old
branch-scoped resume ledgers fail the new subproblem-scope digest.  The current
code also omits the two explicit joint-cover rows from the master itself,
because the lifted `y` matching layer already implies them.

## 3. The exact four-row relaxation

Let

\[
 T=\{(1,1883),(1,1907),(1,3255),(1,5939)\}.
\]

Define `REC_T` by (2.1), all 858 equations (2.2), and only the four instances
of (2.3) indexed by `T`.

### Lemma 3.1 (safe reduced oracle)

Every full q1 recourse satisfies `REC_T`.  Consequently, UNSAT of `REC_T`
under any cut assumptions is already a sound no-recourse certificate for the
full model.

This reduced parametric model has the same 27,428 Boolean variables but only

\[
 1+858+4=863
\]

native constraints.  All 26,570 add columns are still needed for exactness:
non-`T` seams may be required to complete the degree-restoring matching.

For cut `6c98`, every positive cut-degree node has demand one.  Presolve of
`REC_T` therefore leaves exactly the 1,448 seams joining the 198 active nodes,
198 exact-one vertex equations, and four colour clauses.  Thus the smallest
straight native fixed-cut formulation is 1,448 Boolean variables and 202
constraints.  It is exactly a perfect matching required to use at least one
edge of each of four colours.  The 9,938-variable CNF is larger only because
its hand-built sequential counters introduce auxiliary variables.

## 4. Positive and signed cut-assumption cores

### Theorem 4.1 (positive-core Benders row)

Let `F` be either the exact universal encoding of `REC_99` or the relaxation
`REC_T`.  Let `K subseteq S`.  If

\[
 F\wedge\bigwedge_{e\in K}(x_e=1)
\]

is UNSAT, then every radius-99 cut containing `K` has no full q1 recourse.
The following is therefore a valid master row:

\[
 \sum_{e\in K}x_e\leq |K|-1.                               \tag{4.1}
\]

#### Proof

Any full recourse for a cut containing `K` supplies a satisfying assignment
of `REC_99`, hence of `REC_T`, with all assumptions true.  This contradicts
UNSAT.  QED.

To fix a radius-99 candidate `C`, it is enough to assume the 99 positive
literals `x_e`, `e in C`: equation (2.1) forces all other cut variables to
zero.  This is why the present Benders driver's positive assumption polarity
is correct.  The full 99-edge no-good is immediately valid after a certified
fixed-cut UNSAT.  A proper assumption subcore `K` is the desired stronger
generalization.

One may instead use signed assumptions.  If `P` is assumed cut and `N` is
assumed uncut, replayed UNSAT gives the exact clause

\[
 \bigvee_{e\in P}\neg x_e\;\vee\!
 \bigvee_{e\in N}x_e,                                      \tag{4.2}
\]

or equivalently

\[
 \sum_{e\in P}x_e-\sum_{e\in N}x_e\leq |P|-1.             \tag{4.3}
\]

A signed core can be shorter but is not generally stronger than a positive
core.  Positive-only extraction should be attempted first because it gives a
monotone radius-99 no-good.

### Theorem 4.2 (degree-signature transfer of the `6c98` conflict)

Let `d*` be the 858-entry endpoint-demand vector of cut `6c98`; it is one on
198 nodes and zero on the other 660.  Put

\[
 P=\{4742,22511,23229,24034\}.
\]

Assume the persisted four-row fixed matching conflict is UNSAT.  Then every
radius-99 cut vector `x` satisfying

\[
 \sum_{e\in S}\mu(v,e)x_e=d^*_v\quad(v\in V),
 \qquad x_p=1\quad(p\in P)                                \tag{4.4}
\]

has no full q1 recourse.

#### Proof

The degree equations of `REC_T` depend on `x` only through the endpoint-demand
vector.  If that vector is `d*`, they reduce to the same perfect-matching
system on the same 198 active nodes and the same 1,448 usable seams as in the
fixed artifact.  Each colour in `T` has the displayed unique source provider;
the four assumptions `x_p=1` therefore reduce its guarded clause to exactly
the same add-provider clause.  Thus `REC_T` is literally the persisted
four-row fixed system, which is UNSAT.  Lemma 3.1 transfers the conclusion to
full q1 recourse.  QED.

This is a genuine stronger logical consequence of the existing conflict; it
can reject source-cut variants with the same endpoint-demand vector.  It is
not the unsupported four-edge row (1.1), because all equalities in (4.4) are
essential to the present proof.

There is a smaller linear representation.  Let `D` be the 198-node support of
`d*`, and define the exact node-activity bit

\[
 h_v={\bf1}[d_v(x)\geq1].                                  \tag{4.5}
\]

For every radius-99 cut, `sum_v d_v(x)=198`.  Hence

\[
 d(x)=d^*\quad\Longleftrightarrow\quad h_v=1
 \text{ for every }v\in D.                                \tag{4.6}
\]

Indeed, 198 positive integer demands on the 198 nodes of `D` already consume
the entire demand sum, forcing value one there and zero outside.  Theorem 4.2
therefore gives the single 202-term inequality

\[
 \sum_{v\in D}h_v+\sum_{p\in P}x_p\leq 201.               \tag{4.7}
\]

Since source degree is two, `d_v in {0,1,2}` and exact activity is imposed by

\[
 h_v\leq d_v\leq2h_v,\qquad h_v\in\{0,1\}.                \tag{4.8}
\]

Thus no 858-way equality table is needed.  Both inequalities in (4.8) are
required; a freely settable activity bit would invalidate (4.7).

A still smaller signature core can be sought by assuming selected demand
equalities through guard literals, extracting a subset `G`, and replaying
UNSAT.  The resulting clause uses exact equality indicators only for `G`.
This guard-core route is complementary to the explicit activity cut (4.7)
and the direct positive edge core of Theorem 4.1.

For OR-Tools Boolean variable index `i`, a positive assumption is encoded by
`i` and a negative assumption by `-i-1`.  A signed-core extractor must use an
explicit literal-to-edge-and-polarity registry.  Taking `abs(index)` is
incorrect.  The present driver avoids this hazard because it installs only
positive assumptions and rejects every returned index outside that positive
registry.

## 5. Exact guarded clauses

The q1 constraint needs no auxiliary loss variable.  Its exact CNF clause is

\[
 \left(\bigvee_{e\in S_c}\neg x_e\right)
 \vee\left(\bigvee_{a\in A_c}y_a\right).                  \tag{5.1}
\]

For a fixed cut, a retained source provider satisfies the clause; a lost
colour reduces it to the add-provider clause.  For the four `6c98` colours,
each `S_c` is the singleton displayed in Section 1.

If an implementation nevertheless introduces a loss variable `l_c`, exact
feasible-set preservation requires the full equivalence

\[
 l_c\Longleftrightarrow\bigwedge_{e\in S_c}x_e.            \tag{5.2}
\]

The one-way implication `l_c -> all x_e` is insufficient: setting `l_c=0`
could disable a genuinely lost colour.  A one-way relaxation can still be
used for an UNSAT-only filter, but a SAT output would not be an exact recourse
witness.

Likewise, the fixed `6c98` domain of 1,448 seams must not be installed
unconditionally in a cross-cut model.  The other 25,122 seams are excluded
only because their endpoints have zero demand under that particular cut.
Across cuts, either retain every seam variable and impose (2.2), or guard
every column exclusion by exact endpoint-capacity conditions.  Merely fixing
the current usable domain makes any proper cut-assumption core unsound.

For a universal CNF, (2.2) can be encoded locally because each source node
has source-cut demand at most two.  A standard audited totalizer may equate
the two threshold bits `[add degree >=1]`, `[add degree >=2]` to the
corresponding source-incidence thresholds and prohibit add degree three.
The radius equation (2.1) needs its own exact cardinality encoding.  A known,
independently replayed cardinality encoder is preferable to another custom
counter.  The fixed-CNF census audit currently checks hashes and structural
counts, but does not independently reconstruct every auxiliary counter
clause; source-code review is still part of its semantic trust base.

## 6. Proof and core extraction protocol

There are two distinct evidence levels.

### 6.1 CP-SAT

1. Build the branch-free `REC_T` model once.
2. Clear all assumptions, then add the 99 positive literals of the candidate.
3. On `INFEASIBLE`, read `sufficient_assumptions_for_infeasibility()` and
   reject repeated, unknown, or wrong-polarity indices.
4. Replay the returned core on the same frozen proto.  `UNKNOWN` learns
   nothing.
5. Optionally deletion-shrink, but every deletion is accepted only after an
   `INFEASIBLE` replay.
6. Emit (4.1), binding the proto hash, literal registry hash, core literal
   indices, edge IDs, and replay transcript.

This gives an exact-solver assumption certificate, but CP-SAT currently does
not supply a standalone DRAT/LRAT proof.

### 6.2 CaDiCaL with a checkable proof

1. Build and independently audit a universal guarded CNF for `REC_T`.
2. Use IPASIR assumptions only to discover a failed-assumption subset.
3. Never treat the failed set as certified merely because `failed(lit)` is
   true.  Materialize the proposed core literals as unit clauses in a fresh
   DIMACS instance.
4. Run CaDiCaL on that augmented CNF with proof tracing enabled.
5. Verify the proof with an independent DRAT/LRAT checker.
6. Record the SHA-256 hashes of the base CNF, variable registry, unit list,
   augmented CNF, proof, checker, and checker transcript.

For positive units `K`, verified UNSAT of the augmented formula proves the
clause `OR_{e in K} not x_e`, hence (4.1), by the deduction theorem.  For
signed units it proves (4.2).  A proof generated only for the fully fixed
1,448-column CNF certifies at most the complete 99-edge candidate no-good; it
does not certify a proper cross-cut core.

## 7. Implemented full oracle and recommended first tier

The complete branch-free 2,387-row oracle is now the production recourse.
The smallest useful first-tier oracle is not another joint-cover layer; it is
the branch-free 863-constraint `REC_T` model:

* 858 cut variables;
* all 26,570 loopless off-source add variables;
* exact radius 99;
* all 858 node degree equations;
* the four guarded upper clauses in Section 1;
* no motif, branch, Pareto, portal, cover, or aggregate rows.

Run it first under the 99 positive `6c98` assumptions and extract/replay a
proper cut core.  If it returns SAT for a later candidate, escalate that
candidate to the 2,387-constraint full `REC_99` oracle.  This two-tier design
preserves the exact feasible set at the full tier, gives a sound UNSAT-only
prefilter at the four-row tier, and ensures every learned no-good generalizes
solely through cut literals rather than through duplicated master logic.

In parallel, the same four-row oracle should expose the compressed state
interface of Theorem 2.2.  Fix `d=d*` through equality guards and assume the
four loss bits.  A replayed guard subcore gives

\[
 \bigvee_{(v,t)\in G_d}[d_v(x)\ne t]
 \;\vee\!
 \bigvee_{c\in G_\ell}[\ell_c(x)=0],                       \tag{7.1}
\]

with exact master reification.  The unshrunk version is Theorem 4.2.  This is
the most promising compact conflict because it projects away irrelevant cut
edge identities while retaining precisely the two data types seen by the add
problem: endpoint demand and lost colours.

The sharp present boundary is:

* proved from model semantics: Theorems 2.1 and 4.1, the counts 2,387 and 863,
  the exact clauses (5.1), and the redundancy of `sum y=99`;
* persisted solver evidence: fixed `6c98` UNSAT and a deletion-minimal
  four-upper-row conflict;
* companion solver-free proof: the 26-node endpoint-cover row closes `6c98`
  globally, so the fixed-CNF transcript is no longer needed for that
  conclusion;
* not yet certified: a proper CP-SAT/DRAT assumption subcore extracted from
  the universal 863-row oracle, or any validity of the unsupported bare
  four-edge inequality (1.1).
