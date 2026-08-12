# K17 c7be Pascal recursion and forced-closure scout

Date: 2026-07-31  
Status: solver-free fixed-domain no-go; rethreaded/different-source gate

## 1. Scope and source

The source is the authenticated K16 rank-eight chronology

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

which underlies the exact universal K16 word of SHA
`890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe`.
Write its 12,870 rank-eight states as
\(T_0,\ldots,T_{12869}\), and write \(z=2^{16}\) for the new coordinate.

This note tests two explicit recursions from that fixed chronology.  It
closes the strict common-colour recursion and the complete
one-occurrence-per-rank-nine-colour shore domain.  It does not exclude a
rethreaded edge chronology, a different source, a more general shore, or an
unrestricted K17 construction.

## 2. The direct common-colour recursion is closed

Each K16 Johnson edge has lower and upper colours

\[
 X_i=T_i\cap T_{i+1},\qquad U_i=T_i\cup T_{i+1}.
\]

A direct common-colour Pascal lift needs a transition set which is rainbow
on both colour shores.  This is a matching in the bipartite occurrence graph
\(X_i--U_i\).

For the displayed source, that graph is a forest of stars:

```text
component type       number
L1-U1-E1              7308
L1-U2-E2              1319
L1-U3-E3                55
L2-U1-E2              1229
L3-U1-E3               100
total components     10011
```

Every star contributes at most one matching edge, and selecting one edge in
each star attains that bound.  Hence the exact maximum common rainbow is

\[
 10011<\binom{16}{7}=11440,
 \qquad\text{deficiency }1429=\operatorname{Cat}_8-1.       \tag{2.1}
\]

Thus the strict common-colour recursion is solver-free impossible for this
fixed parent.

## 3. Exact two-shore Pascal deck

The next weaker construction chooses one occurrence of every old rank-nine
edge colour and orders the selected colours by their chosen edge position.
Call the resulting shore \(A\).  Put

\[
 B=(z\cup T_0,\ldots,z\cup T_{12869}).
\]

### Proposition 3.1 (deck identity)

\(A\mathbin{\dot\cup}B\) is exactly the K17 rank-nine layer.

### Proof

The shore \(A\) contains each of the \({16\choose9}=11440\) old rank-nine
masks once.  The shore \(B\) contains each of the
\({16\choose8}=12870\) rank-nine masks containing \(z\) once.  The shores
are disjoint, and Pascal's identity gives
\(11440+12870={17\choose9}=24310\). \(\square\)

### Proposition 3.2 (upper inheritance)

If \(B\) is one contiguous sector, its internal intervals cover every K17
upper target containing \(z\).  The remaining upper defects are exactly the
\(z\)-free rank-at-least-ten masks missing from the interval-OR spectrum of
\(A\).

### Proof

An interval internal to \(B\) has OR
\(z\cup\operatorname{OR}(T_i,\ldots,T_j)\).  The authenticated K16
chronology covers every old mask of rank at least eight, so these intervals
cover every \(z\)-containing K17 mask of rank at least nine.  Intervals
internal to \(A\) are \(z\)-free, while an interval crossing the shore seam
contains \(z\); therefore no crossing interval can repair a missing
\(z\)-free mask. \(\square\)

The first-occurrence transversal leaves 216 upper masks:

\[
 198\text{ of rank }10,\quad17\text{ of rank }11,\quad1\text{ of rank }12.
\]

A retained 30-second coordinate-descent witness over the 1,329 nonunique
occurrence choices (1,229 binary and 100 ternary) reduces this to 73:

\[
 63\text{ of rank }10,\quad9\text{ of rank }11,\quad1\text{ of rank }12.
                                                               \tag{3.1}
\]

This is a replayed witness, not an optimality certificate.

## 4. Schedule diagnostics for two displayed orders

For \(k=17\), middle width \(W=24310\), target length \(L=W+3=24313\),
and lower demand

\[
 \Lambda=\sum_{j=1}^{8}\binom{17}{j}=65535.
\]

If \(X\) and \(Y\) are the three omitted starts and deadlines, respectively,
the number of selected positive-depth cells is

\[
 \sum_i(d_i-s_i)=\sum_{x\in X}x-\sum_{y\in Y}y.             \tag{4.1}
\]

For the tail start holes \(X=\{24310,24311,24312\}\), omitted-start cells
contribute \(3+2+1=6\).

The flat schedule \(Y=\{0,1,2\}\) therefore has 72,936 physical cells and
7,401 scalar slack.  It does not preserve the source compiler: the retained
73-hole \(A+B\) chronology loses 4,594 middle rows under its maximal
envelope.

Putting \(B\) first permits the literal inherited K16 breakpoint

\[
 Y=\{0,1,6388\}.
\]

Equation (4.1) gives

\[
 66544+6=66550
\]

physical cells, still 1,015 above demand.  The depth histogram is exactly

\[
 2^{6386},\qquad3^{17924}.                                  \tag{4.2}
\]

This orientation is much closer: the retained 73-hole chronology loses
1,119 middle rows rather than 4,594.  Exactly two failures lie at the end of
the inherited \(B\) shore and 1,117 lie in \(A\).  The first-occurrence
version has 1,115 failures.

## 5. Forced-closure preflight gives a scoped no-go

Let \(E_p\) be the maximal envelope at physical position \(p\).  Every
common-Q word satisfies \(Q_p\subseteq E_p\).  Consequently:

1. a middle bit absent from the union of the \(E_p\)'s on its row can never
   be restored by a later cap; and
2. an exact interval of OR \(z\) consists only of nonempty submasks of
   \(z\), hence every position in that interval is itself the singleton
   letter \(z\).

The first statement makes the 1,119 maximal-envelope replay failures an
exact obstruction, not a heuristic score.  Independently, all 24,313
physical positions provide length-one cells, 12,870 maximal envelopes
contain \(z\), and **none** can be capped to \(z\) while retaining all
protected middle rows.  By item 2, no longer exact-\(z\) cell can exist
either.

Therefore the displayed \(B+A\) chronology and inherited P/Q schedule are
source-relative compiler-UNSAT before Hall.  The fail-closed normalization
correctly performs no lower graph, DM support, forced-cap iteration, or CNF
generation.  Scalar capacity passes, but carrier residence and the
singleton-new-coordinate socket fail.

This schedule-specific obstruction is superseded, for the entire fixed
occurrence-transversal domain, by an even smaller upper-core contradiction.
The rank-nine colour `0x0bf5` occurs only at edge positions 9176 and 10616.
Every exact witness for `0x1bf5` forces the first occurrence, whereas every
exact witness for `0x0ff5` forces the second.  Selecting one occurrence of
each colour therefore cannot cover both targets.  Independently, colour
`0x1ce7` has domain `{12784,12799,12814}` while `0x1def` forces 12799 and
`0x3de7` forces 12814.  Both cores are solver-free and literal-replayed.

The retained upper-73 two-shore word (SHA `ea103372...`) also fails a
distinct final-start-hole schedule gate.  Its exact short-run frontier is

\[
 (\rho_1,\rho_2,\rho_3)=(11440,11440,17824),
 \qquad \sum_j\rho_j=40704>7401.
\]

By the monotone-deadline run-staircase theorem it cannot have both exact
maximal-envelope row replay and enough lower cells in the canonical
length-24,313 schedule, even if its upper defects were repaired.  The
independent arbitrary-start extension is stronger for this same upper-73
word.  Its interior singleton run at row 11440 forces the following dichotomy for every three-hole
monotone P/Q schedule: moving a start threshold early enough to shield the run
costs at least 12,869 cells, while leaving all start thresholds late forces
deadline-threshold cost at least 34,320.  Both exceed slack 7,401.  Thus that
upper-73 concatenation is middle-plus-scalar UNSAT for all
start/deadline-hole choices, not only for the final-start-hole normal form.

## 6. The next structural law

No further search over the fixed c7be occurrence choices is admissible: the
opposite-choice core closes that complete domain, not merely the retained
73-hole witness.  Follow-on exact censuses now also close every one-block
reversal, the unique single reversal adding a third `0x0bf5` occurrence plus
all legal endpoint reroots above it, and the only other authenticated
genuine-parent endpoint survivor.  The next genuinely new scout must move
multiple intervals, split/interleave so that a forced target changes its
allowed-occurrence side, or start from a different K16 source.

Every such candidate should be screened in this proof-safe order:

1. exact short-run frontier and staircase budget;
2. exact maximal-envelope middle replay and nonempty envelopes;
3. zero arbitrary-width upper holes;
4. a legal singleton-\(z\) cap and any other protected prepins;
5. complete literal lower incidence graph and marginal Hall;
6. DM support, forced closure, fixed-q propagation, and only then a common-Q
   CNF if a materially smaller residual survives.

This is the reusable computational law extracted here: residence, upper
coverage, and schedule capacity must be rebuilt jointly by the rethread.
Optimizing an unchanged occurrence transversal or launching a blind lower
SAT model cannot cross either frozen obstruction.

## 7. Audits and frozen hashes

The original primary audit reconstructed all identities, schedules, spectra,
middle failures, and the singleton frontier:

```text
scratch/audit_k17_c7be_pascal_forced_closure_scout_20260731.py
scratch/k17_c7be_pascal_forced_closure_scout_20260731.audit.json
```

That JSON is retained as historical evidence only.  Its driver authenticates
the producer source at SHA `eb684414...`, whereas the live file now has SHA
`0d2549bb...`; consequently a fail-closed rerun aborts and this note does not
promote the live C++ or refresh the primary JSON.  The output words themselves
remain byte-frozen and independently replayable.

The independent audit imports neither executable code from the primary audit
nor the common-Q normalizer or live search producer.  It does read the
historical primary JSON to cross-check its frozen identities, then derives
(2.1) from the star components, uses a different compressed suffix-OR scan
for (3.1), and separately replays the frozen upper-73 word, inherited
envelopes, and singleton frontier.  Because that cross-check pins stale
primary bytes, this independent JSON is corroboration rather than a promoted
canonical artifact:

```text
scratch/audit_k17_c7be_pascal_forced_closure_independent_20260731.py
scratch/k17_c7be_pascal_forced_closure_independent_20260731.audit.json
```

The retained output artifacts are

```text
scratch/k17_c7be_pascal_shadow_upper73_choices_20260731.tsv
  SHA d3486988c600c3294bd789e74b9ce8aa0ce5554ea25cb941dcc44b871f92d37c
scratch/k17_c7be_pascal_shadow_upper73_old_rank9_20260731.word
  SHA 7e32dc140e2e2aa29105e8c07ccc6045686056f2c264ddefebf7cb1401ef7514
scratch/k17_c7be_pascal_shadow_upper73_sector_targets_20260731.word
  SHA ea10337264c7998d227cf4c8ef5d5df463d5fb4efd9c29c7a1e0171d7b4897a4
```

The fixed-domain obstruction is independently replayed by

```text
scratch/audit_k17_pascal_occurrence_selection_nogo_20260731.py
scratch/audit_k17_c7be_u_opposite_choice_cores_20260731.py
scratch/k17_c7be_u_opposite_choice_cores_20260731.audit.json
scratch/audit_k17_u_transversal_compact_model_20260731.py
scratch/k17_u_transversal_compact_model_20260731.audit.json
scratch/audit_monotone_deadline_run_staircase_arbitrary_starts_20260731.py
scratch/monotone_deadline_run_staircase_arbitrary_starts_20260731.audit.json
```

The compact exact interval presentation has 1,529 occurrence-choice
variables and 510 clauses; the second contradiction is the three-clause core
`(142)`, `(143)`, `(-142 or -143)`.  A separate 3,114-variable/4,111-clause
CEGAR encoding has a retained, verified DRAT proof, but the solver-free cores
are the theorem.  Final source/JSON hashes and payload hashes are recorded in
the handoff after all lightweight replayable audits are rerun.  No theorem
claim in this note depends on the stale producer source.
