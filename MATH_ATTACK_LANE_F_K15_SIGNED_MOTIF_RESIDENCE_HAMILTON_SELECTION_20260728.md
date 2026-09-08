# Lane F: signed Hall-29 motif selection with residence and Hamilton coupling

Date: 2026-07-28

Scope: the current \(k=15\) three-parent directed catalogue. This is a
mathematical formulation and audit of the finite selection gate; no new
computer search is claimed.

## 0. Audited input and verdict

Let \(V\) be the \(6,435\) middle vertices and let \(D=(V,A)\) be the
directed arc union of the three certified parents

\[
 P_{29},\qquad P_{30},\qquad P_{31}.
\tag{0.1}
\]

They are, respectively,
`scratch/k15_doubletrans_05_213_hall29.json`,
`scratch/k15_outer2_p1_h30_bridge.json`, and
`scratch/k15_trans1113_balanced_hall31.json`.

The current Hall-29 carrier has the seven zero-candidate targets

\[
 \mathcal Z=
 \{2575,5801,13616,13620,17738,21641,29776\}.
\tag{0.2}
\]

For each \(z\in\mathcal Z\), the three-parent catalogue contains exact
interior or endpoint compiler motifs which would make \(z\) nonzero. The
diagnostic minimum-novelty tuple in
`scratch/k15_h29_zero7_minimal_tuple.json` chooses one motif for every
target and has the following exact ledger:

\[
 \begin{array}{c|c}
 \text{distinct forced directed arcs}&60\\
 \text{arcs outside }P_{29}&4\\
 \text{selected forbidden residence motifs}&23\\
 \text{forced start/end}&2479\text{ and }22185.
 \end{array}
\tag{0.3}
\]

It is therefore not a near-solution: it is infeasible before upper-shadow
or Hall constraints are considered. It proves that novelty is the wrong
separable objective. Four novel arcs can have a large *correlated residence
shadow*.

This note gives three precise replacements.

1. An exact polynomial-size mixed circulation formulation couples all
   target OR clauses, every forbidden residence path, and one Hamilton
   circuit through a dummy vertex. This is the authoritative feasibility
   model.
2. Projecting to one motif choice per target gives an exact bounded-arity
   local CSP: degree clauses have arity two and residence clauses have
   arity at most four. An asymmetric LLL or the simpler first-moment
   criterion can select a residence-safe degree-compatible motif tuple.
   It cannot, by itself, prove Hamilton completion.
3. A certified-backbone-patch restriction restores a rigorous polynomial
   positive theorem. Disjoint collar-safe interval patches compose into one
   Hamilton path automatically, and a \(2^7\)-state interval dynamic
   program decides whether their labels cover all seven targets. This is a
   sharper pre-SAT filter than minimum novelty. Failure of the patch filter
   is only a restricted no-go, not a no-go for the full three-parent union.

The exact remaining global boundary is thus not motif supply and not raw
residence count. It is Hamilton-completable residence-safe *correlation* of
the seven OR clauses.

## 1. The exact circuit--motif--residence system

Adjoin a dummy vertex \(\partial\) to turn a spanning directed path into a
directed Hamilton circuit. Let

\[
 A^+=A\cup\{(\partial,v),(v,\partial):v\in V\}.
\tag{1.1}
\]

For \(a\in A^+\), let \(x_a\in\{0,1\}\) indicate selection. Write
\(s_v=x_{\partial v}\) and \(t_v=x_{v\partial}\).

For each target \(z\), let \(\mathcal P_z\) be its exact motif family.
A motif \(P\) has a set \(E(P)\subseteq A\) of directed arcs and may also
prescribe one start or end literal. Let \(L(P)\subseteq A^+\) be the full
set of its required literals. Introduce \(y_P\in\{0,1\}\).

Finally, let \(\mathcal R\) be the exact family of directed residence-
forbidden paths. In the current depth-three audit every
\(R\in\mathcal R\) has

\[
                         2\le |R|\le4.
\tag{1.2}
\]

### Theorem 1.1 (exact mixed circulation criterion)

There is a residence-safe Hamilton chronology in \(D\) which supplies all
seven targets if and only if the following system is feasible.

Degree equations:

\[
 \sum_{a\in\delta_D^-(v)}x_a+s_v=1,
 \qquad
 \sum_{a\in\delta_D^+(v)}x_a+t_v=1
 \quad(v\in V),
\tag{1.3}
\]

\[
                         \sum_vs_v=\sum_vt_v=1.
\tag{1.4}
\]

Motif implications and OR clauses:

\[
 y_P\le x_a\quad(a\in L(P)),
 \qquad
 \sum_{P\in\mathcal P_z}y_P\ge1
 \quad(z\in\mathcal Z).
\tag{1.5}
\]

Residence clauses:

\[
                         \sum_{a\in R}x_a\le |R|-1
 \quad(R\in\mathcal R).
\tag{1.6}
\]

Single-commodity circuit flow: introduce \(f_a\ge0\), with

\[
                         0\le f_a\le |V|x_a
 \quad(a\in A^+),
\tag{1.7}
\]

\[
 \sum_{a\in\delta^-(v)}f_a-
 \sum_{a\in\delta^+(v)}f_a=1
 \quad(v\in V),
\tag{1.8}
\]

\[
 \sum_{a\in\delta^+(\partial)}f_a-
 \sum_{a\in\delta^-(\partial)}f_a=|V|.
\tag{1.9}
\]

#### Proof

Suppose first that a desired chronology exists. Select its normal arcs and
the two dummy arcs closing its endpoints. Equations (1.3)--(1.4) hold.
For every target choose one witnessing motif contained in the chronology
and set its \(y_P\) to one. Residence safety gives (1.6). Send \(|V|\)
units from \(\partial\) around the selected circuit, consuming one unit at
each middle vertex. This gives (1.7)--(1.9).

Conversely, (1.3)--(1.4) make the selected arcs a vertex-disjoint directed
cycle cover of \(V\cup\{\partial\}\). The flow equations force every
middle vertex to be reachable from \(\partial\) through selected arcs;
therefore no second cycle exists. The selected cover is one Hamilton
circuit. Removing \(\partial\) gives a spanning directed path. Equations
(1.5) give a selected exact motif for every target, and (1.6) gives
residence safety. \(\square\)

No equivalence variable is needed in (1.5): \(y_P=1\) certifies that all
motif literals are selected. Extra selected motifs are harmless.

Theorem 1.1 is polynomial in the explicitly enumerated arc and motif
catalogues. Its integrality is essential. Relaxing \(x\) to \([0,1]\)
gives a useful infeasibility filter but not the Hamilton-circuit polytope.

## 2. The projected motif CSP

The exact model can be reduced before circuit search. Introduce one finite-
domain variable

\[
                         Z_z\in\mathcal P_z
 \quad(z\in\mathcal Z),
\tag{2.1}
\]

and put

\[
                         F(Z)=\bigcup_{z\in\mathcal Z}L(Z_z).
\tag{2.2}
\]

The target OR clauses are now automatic. We project the local obstructions
onto these seven variables.

### Lemma 2.1 (bounded-arity residence projection)

For every \(R\in\mathcal R\), the condition \(R\subseteq F(Z)\) is the
union of forbidden partial assignments involving at most \(|R|\le4\)
target variables.

#### Proof

If \(R\subseteq F(Z)\), assign each arc \(a\in R\) to one target
\(z(a)\) whose selected motif contains \(a\). At most \(|R|\) distinct
targets occur. For each used target record its selected motif. This partial
assignment forces every arc of \(R\), so it is forbidden. Conversely,
every such recorded assignment forces \(R\). Taking all maps
\(a\mapsto z(a)\) proves the statement. \(\square\)

Delete nonminimal partial assignments. Each remaining residence clause has
the form

\[
                         \bigvee_{z\in I}(Z_z\ne P_z),
 \qquad |I|\le4.
\tag{2.3}
\]

Degree incompatibility gives binary clauses of the same form: two motifs
cannot be selected together if their required arcs prescribe two distinct
successors or predecessors of one vertex, or incompatible dummy endpoints.
A directed cycle already forced by a motif tuple gives a further no-good
clause; such clauses can be separated lazily.

Thus the minimum-novelty tuple is rejected in the projected CSP without
constructing a Hamilton model: it activates 23 clauses of type (2.3).

### Corollary 2.2 (treewidth filter)

Let \(G_{\rm CSP}\) be the primal graph on the seven target variables,
joining two targets when they occur in one projected clause. If a tree
decomposition of width \(w\) is supplied, local motif feasibility is
decidable by junction-tree dynamic programming in time

\[
 O\!\left(|\mathcal C|\,M^{w+1}\right),
 \qquad M=\max_z|\mathcal P_z|,
\tag{2.4}
\]

where \(\mathcal C\) is the projected clause family.

For the present seven variables, direct variable elimination is finite even
when \(w=6\). The value of the projection is not asymptotic complexity but
early exact rejection and the removal of millions of irrelevant arc
variables.

## 3. A rigorous LLL criterion

Choose the seven motif variables independently, with

\[
                         \Pr(Z_z=P)=\pi_z(P).
\tag{3.1}
\]

Let \(\mathcal B\) be the family of projected degree, endpoint, residence,
and forced-cycle bad partial assignments. If bad event \(B\) fixes
\(Z_z=P_{B,z}\) for \(z\in I_B\), then

\[
                         p_B:=\Pr(B)
 =\prod_{z\in I_B}\pi_z(P_{B,z}).
\tag{3.2}
\]

Join two bad events when their target-variable sets intersect.

### Theorem 3.1 (asymmetric motif LLL)

If there are numbers \(0<q_B<1\) satisfying

\[
 \boxed{
 p_B\le q_B
       \prod_{\substack{C\ne B\\I_C\cap I_B\ne\varnothing}}(1-q_C)
 \quad(B\in\mathcal B),}
\tag{3.3}
\]

then there is a choice of one motif for every target whose forced arc set is
degree-compatible, endpoint-compatible, residence-safe, and contains no
directed cycle.

#### Proof

Each event depends only on \(\{Z_z:z\in I_B\}\); disjoint variable sets
are independent. Equation (3.3) is the asymmetric Lovasz local lemma.
Avoiding every event gives the stated properties by construction.
\(\square\)

In the symmetric specialization, if every bad event has probability at
most \(p\) and meets at most \(\Delta\) other bad events, then

\[
                         e p(\Delta+1)\le1
\tag{3.3a}
\]

is sufficient. This is also the correct quick audit of whether an LLL lane
is plausible: one must count clause incidences per target motif, not merely
the total number of motifs.

A simpler sufficient condition is

\[
                         \sum_{B\in\mathcal B}p_B<1.
\tag{3.4}
\]

Indeed, the expected number of violated clauses is below one, so some
assignment violates none. It can be found deterministically by fixing the
seven variables one at a time while never increasing the conditional
expectation.

The LLL is useful only for the *local* projection. It does not imply that the
forced path forest extends to a Hamilton path in the sparse union of three
parents. Connectivity is a global event, and declaring it independent of
distant motif variables would be false.

For the present problem there are only seven variables. Exact projected-CSP
elimination is therefore stronger than an LLL unless the motif catalogue is
expanded enough that direct domains become unwieldy while clause incidence
remains sparse. The LLL should be treated as a scalable certificate for a
larger parent catalogue, not as a substitute for the exact seven-variable
filter.

There is an exact but potentially exponential extension: include every
inclusion-minimal partial assignment whose forced arcs have no feasible
completion in Theorem 1.1 as a Hamilton-blocker event. Then (3.3) implies a
full solution. The difficulty is precisely that these blockers can involve
all seven variables and have a dense dependency graph. This formulation is a
criterion, not a claim that its inequalities hold for the current catalogue.

## 4. The signed selection objective

Let \(A_{29}\) be the arc set of the Hall-29 parent. Raw novelty assigns

\[
                         c(a)={\bf1}_{\{a\notin A_{29}\}}.
\tag{4.1}
\]

The diagnostic tuple minimizes a version of \(\sum_{a\in F(Z)}c(a)\), yet
violates 23 residence clauses. The correct first relaxation is not another
scalar novelty weight. It is the multilinear signed functional

\[
 \boxed{
 \Psi(\pi)=
   \sum_z\sum_{P\in\mathcal P_z}\pi_z(P)c_z(P)
   +\Lambda\sum_{B\in\mathcal B}
      \prod_{z\in I_B}\pi_z(P_{B,z}),}
\tag{4.2}
\]

where \(c_z(P)\) is the incremental novelty of motif \(P\) after a fixed
tie-breaking ownership of shared arcs. The second term is the exact expected
number of projected local obstructions, not the sum of per-arc residence
degrees.

If the second term in (4.2) is below one, (3.4) and conditional expectation
produce a locally feasible tuple. Large \(\Lambda\) gives a penalty method;
treating (3.3) as hard constraints gives the sharper LLL version.

The interaction term is necessary. For a residence path \(R\), feasibility
depends on whether *all* its arcs occur in the selected union. Charging each
arc separately both overprices harmless partial paths and underprices the
four-arc conjunction seen in (0.3).

The same construction accepts a signed resource vector rather than one
novelty scalar. For example, attach to a motif or completed patch its exact
changes in

\[
 (\text{Hall-29 neighbourhood}, q_1, q_2, q_3,
   \text{upper shadows}, \text{novel arcs}).
\tag{4.3}
\]

The target-choice stage should retain the Pareto frontier of these vectors.
Optimizing novelty first and filtering residence afterward discards this
correlation.

## 5. Polynomial completion filters

Let \(F\subseteq A^+\) be the forced literals of a locally feasible motif
tuple. Degree compatibility makes \(F\) a collection of directed path
fragments, unless it already contains a directed cycle.

### Proposition 5.1 (flow and port necessary filters)

Every Hamilton completion of \(F\) passes all of the following polynomial
tests.

1. The fractional relaxation of (1.3)--(1.9), with every \(a\in F\)
   fixed to one, is feasible.
2. After forced fragments are contracted, the exposed-port graph has a
   matching of the required cardinality.
3. Its fragment graph is connected and, for every tested fragment set
   \(S\),

   \[
                         c(G-S)\le |S|+1.
   \tag{5.1}
   \]

4. Every maximum-weight matching upper bound for the required Hall witness
   reaches its threshold.

#### Proof

The first statement is relaxation. A Hamilton path uses exactly one external
seam at each nonendpoint exposed port, proving the matching condition.
Contracting its forced fragments produces a spanning path; deleting
\(|S|\) vertices from a path creates at most \(|S|+1\) components. Any
additive optimistic Hall weight on completion seams upper-bounds the value of
the actual completion. \(\square\)

These filters are necessary, not sufficient. The connected alternating-
Hamilton completion problem remains global.

## 6. A polynomial positive theorem: certified backbone patches

The global difficulty can be removed by restricting the action catalogue in
a way that still allows nontrivial correlated changes.

Fix one residence-safe base Hamilton path

\[
                         H_0=(v_1,v_2,\ldots,v_N)
\tag{6.1}
\]

in \(D\), where \(N=6,435\). A **certified patch** \(\alpha\) consists of:

1. an interval \([l_\alpha,r_\alpha]\);
2. a directed path \(Q_\alpha\) from \(v_{l_\alpha}\) to
   \(v_{r_\alpha}\) using exactly the vertices
   \(v_{l_\alpha},\ldots,v_{r_\alpha}\), each once;
3. a target label set \(L_\alpha\subseteq\mathcal Z\) supplied by exact
   compiler motifs inside the patched word;
4. a direct audit that replacing the base interval by \(Q_\alpha\) creates
   no residence violation in the interval enlarged by three vertices on
   each side; and
5. an optional signed resource vector \(g_\alpha\).

Call two patches compatible when their enlarged intervals are disjoint.

### Theorem 6.1 (collar-disjoint patch composition)

Every compatible family \(\mathcal A\) of certified patches composes with
\(H_0\) to one spanning directed Hamilton path. It is residence-safe and
supplies every target in

\[
                         \bigcup_{\alpha\in\mathcal A}L_\alpha.
\tag{6.2}
\]

Its signed resource change is \(\sum_{\alpha\in\mathcal A}g_\alpha\) for
every resource whose audit collar is included in the patch definition.

#### Proof

Replace the indicated base subpaths. Disjoint vertex intervals ensure that
every middle vertex still occurs exactly once and that consecutive pieces
share only their prescribed endpoints. Hence the result is one spanning
path. Every residence window uses at most four arcs. It is either wholly
outside all enlarged intervals, where it agrees with the safe base path, or
lies in the audited collar of one patch. Thus it is safe. Exact motif labels
and additive collar-local resource changes give the remaining statements.
\(\square\)

### Theorem 6.2 (the \(2^7\)-state patch filter)

Given a certified patch catalogue, a minimum-cost compatible family covering
all seven targets can be found in time

\[
                         O\bigl((N+|\mathcal A|)2^7\bigr)
\tag{6.3}
\]

after sorting the patches by their right endpoints.

#### Proof

For each patch \(\alpha\), let \(p(\alpha)\) be the last patch ending
before its enlarged interval begins. Maintain

\[
 D(i,M)=\text{minimum cost using the first }i\text{ patches
 and covering target mask }M.
\tag{6.4}
\]

The transition either skips patch \(i\), or, for each old mask \(M'\),
takes it from state \(D(p(i),M')\) and updates the new mask to
\(M'\cup L_i\). Thus every patch examines \(2^7\) old masks once.
Standard predecessor computation after sorting is linear. \(\square\)

For vector resources, retain the nondominated Pareto states at each
\((i,M)\), or add bounded resource coordinates to the dynamic-programming
state. At fixed \(k=15\) and seven zero targets this is a practical exact
filter.

The patch theorem is sufficient, not necessary. A chronology may mix the
three parents globally without decomposing into disjoint base intervals.
Therefore failure of Theorem 6.2 cannot be reported as an exhaustive no-go.

## 7. Consequences for the current Hall-29 frontier

The existing minimum-novelty tuple establishes three facts.

1. **Local target capacity is present.** All seven targets have motifs in the
   three-parent union.
2. **Arc novelty is badly calibrated.** The tuple needs only four arcs
   outside \(P_{29}\), but those choices jointly complete 23 forbidden
   residence paths.
3. **Residence must be imposed before Hamilton search.** Forcing that tuple
   into the exact model is rejected prior to upper or Hall separation. No
   endpoint choice or circuit completion can delete a forbidden path whose
   arcs are all forced by the seven witnesses.

The next polynomial screening order should therefore be:

\[
 \boxed{
 \begin{array}{c}
 \text{project degree and residence clauses to the seven motif variables}\\
 \longrightarrow\text{ eliminate/LLL-filter motif tuples}\\
 \longrightarrow\text{ flow, port matching, and cut filters}\\
 \longrightarrow\text{ exact Hamilton circuit plus Hall separation}.
 \end{array}}
\tag{7.1}
\]

In parallel, the certified-patch catalogue provides a genuinely positive
polynomial lane. It should be generated from all three parents, not only from
the four novel arcs of the rejected tuple. The useful score is the Pareto
vector (4.3), while the hard state is the seven-bit covered-target mask.

## 8. Exact remaining alternatives

One of the following would advance the finite frontier rigorously.

1. Verify the LLL inequalities (3.3), then show one resulting local tuple
   passes the exact completion model of Theorem 1.1.
2. Find a certified-patch DP state covering mask \(2^7-1\) with admissible
   signed resources. This directly constructs a residence-safe Hamilton
   chronology supplying all seven targets.
3. Prove the projected CSP infeasible. This would show that the current
   three-parent union cannot even select residence-safe degree-compatible
   motifs for the seven targets, independently of Hamilton connectivity.
4. If the projected CSP is feasible but every surviving tuple fails exact
   completion, extract inclusion-minimal Hamilton blockers. These are the
   correct clauses for a fourth-parent search and for the exact LLL
   obstruction.

What is already ruled out is the strategy “minimize novel arcs, then test
residence.” The 60-arc/four-novel tuple with 23 forbidden paths is a literal
counterexample to that ordering of objectives.
