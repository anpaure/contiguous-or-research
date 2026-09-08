# K17 root-subset release, local Hall cuts, and exact 27-bit Benders search

Date: 2026-08-03

Status: exact theorem for the implemented forcing-only 27-bit root-action
face, with a local audit of the three canonical deficiency-21 summary rows.
The drop-12 parent has a complete locally frozen witness bundle.  Drops 15
and 16 presently have manifest-authenticated canonical hashes, action
ledgers, and audit JSONs, but not standalone local table/matching bundles.
No additive
action credit, deterministic-neighborhood optimality, chronology, residence,
upper, compiler, or word conclusion is claimed.

## 1. Canonical deficiency-21 records

All three records use one literal face:

- the strict SHA-bound bf5 carrier;
- the 7,213 protected ticket/host/token rows;
- the same ten selected LLR modes and 20 selected endpoint rows;
- ten phase-0 and ten phase-1 occurrence tickets;
- 20 distinct occurrence rows in each phase, 17 shared across phases, and 23
  rows in their union; and
- a subset of the 27 named roots on which direct-low presentation is forced.

The canonical freeze is

\[
\mathcal F=
\text{root\_action27\_joint\_incumbent\_20260803/
frozen\_def21\_subset\_descent\_20260803}.
\tag{1.1}
\]

Its 22-entry manifest verifies and has SHA-256

\[
\texttt{c1f696934bf93518c236d11d1fee570ec24b2b4b2a9a9e24de01e13526bab0c0}.
\tag{1.2}
\]

The manifest-bound leave-one-out summary, SHA
\(\texttt{ae94a99c0b0a39c1104d4a704ad4babc3e6e8abcea65806ee1962607483ddad9}\),
contains the following tied best records.

| omitted action | row | compressed carrier SHA | final table SHA | rank | deficiency | zero heads | maximum shore |
|---:|---:|---|---|---:|---:|---:|---:|
| 12 | 12948 | e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb | fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c | 16877 | 21 | 19 | 23/2 |
| 15 | 13641 | 7f9404a89903c1b2abb2d5bd933c617195f9d8d802f256352543f106a6af1ded | 687e1e7754615e6355188480cb016673d39cd0167cf7f55218151cccebf805f3 | 16877 | 21 | 20 | 22/1 |
| 16 | 14155 | 8d83a05da98d4cccfdf0e13bc764dba3f23fca7cb3cbc212e95a1777c0632f46 | e5afc9e090aa2293bc2a8585b3c0d913e56217aaacbc46e182cf44c49cb742c7 | 16877 | 21 | 20 | 22/1 |

Only drop 12 is fully frozen under \(\mathcal F\).  Its materialization
audit binds all parent, bank, mode, phase, occurrence, and action inputs and
proves:

\[
\begin{array}{c|c}
\text{retained forced roots satisfied} & 26/26\\
\text{residual augmented matching} & 29256/29256\\
\text{residual dummy capacity} & 785\\
\text{protected rows changed} & 0\\
\text{occurrence rows changed} & 0.
\end{array}
\tag{1.3}
\]

Its exact supplier projection has 74,935 edges, a 16,877-edge matching, and
a 23-head/two-neighbor Hall shore.  Thus the matching and shore prove
deficiency exactly 21.

The raw drop-15 and drop-16 directories additionally contain their 26-action
ledgers and individual materialization/supplier audit JSONs.  The ledgers
correctly omit actions 15 and 16 respectively.  Their materialization audits
bind the canonical output SHAs, prove residual matching \(29256/29256\),
and report zero protected/occurrence changes; their supplier audits report
the ranks and 22/1 shores in the table.  The actual compressed/final tables,
supplier matchings, and Hall files are absent, however, and these raw audits
are not entries in the canonical 22-file freeze.  They therefore strengthen
the summary audit but still do not form self-contained parent contracts.

## 2. What a root-action bit currently means

Let

\[
A=\{0,\ldots,26\}
\tag{2.1}
\]

index the named roots.  Fix the protected rows, ten modes, and 23 occurrence
pins, expand the residual dummy capacity into indistinguishable labelled
unit vertices, and let \(\mathcal M(\varnothing)\) be the resulting set of
integral perfect presentation matchings.

For a presentation matching \(M\), define its realized named direct-root set

\[
D(M)=\{a\in A:M\text{ matches a low target directly into }r_a\}.
\tag{2.2}
\]

The current materializer gives the bits implication semantics:

\[
z_a=1\quad\Longrightarrow\quad a\in D(M).
\tag{2.3}
\]

It implements (2.3) by deleting every rank-seven-middle-to-\(r_a\) arc.
When \(z_a=0\), both low-to-root and middle-to-root arcs remain available.
It does not impose \(a\notin D(M)\).

Consequently, for an enforced set \(S\subseteq A\),

\[
\mathcal M(S)
=\{M\in\mathcal M(\varnothing):S\subseteq D(M)\}.
\tag{2.4}
\]

Thus “root subset” below means an enforced subset unless exact-pattern
semantics is stated explicitly.

For \(M\in\mathcal M(S)\), let \(\tau(M)\) be the table after the fixed
ten-mode overlay, let \(G(\tau(M))\) be its complete supplier graph, and put

\[
\delta(M)=16898-\nu(G(\tau(M))).
\tag{2.5}
\]

The exact recourse value and the deterministic materializer value are
different functions:

\[
\delta^*(S)=\min_{M\in\mathcal M(S)}\delta(M),
\qquad
\widehat\delta(S)=\delta(M_{\rm alg}(S)).
\tag{2.6}
\]

The frozen leave-one-out and radius tables record
\(\widehat\delta\), not a proof of \(\delta^*\).

## 3. Release/order-ideal theorem

### Theorem 3.1

For enforced subsets \(S\subseteq T\subseteq A\),

\[
\mathcal M(T)\subseteq\mathcal M(S)
\quad\text{and}\quad
\delta^*(S)\le\delta^*(T).
\tag{3.1}
\]

Therefore, for every supplier target \(d\),

\[
\mathcal F_d=\{S\subseteq A:\delta^*(S)\le d\}
\tag{3.2}
\]

is a downward-closed family.

#### Proof

Every matching satisfying all direct-root requirements in \(T\) satisfies
the subset of requirements in \(S\).  This proves the first inclusion.  The
minimum of the same objective over the larger feasible set cannot increase,
which proves the second statement. \(\square\)

No matroid, greedoid, submodularity, or additive-credit conclusion follows.
Downward closure is simply set inclusion of recourse spaces.

### Corollary 3.2 (inherit every good witness)

If \(M\) certifies target \(d\) for \(T\), the same literal
table/supplier-matching certificate certifies target \(d\) for every
\(S\subseteq T\).  A new deterministic replay on \(S\) that returns a worse
rank is merely a worse witness.

This phenomenon occurs in the frozen records.  The all-27 deficiency-22
matching remains feasible after dropping action 5, but the new deterministic
drop-5 replay reports deficiency 24.  Likewise, the drop-12 deficiency-21
witness remains feasible after every further release, while some radius-one
replays report deficiency 22 or 23.  These values are not lower bounds on
\(\delta^*\) and do not establish a local optimum of the existential
27-bit problem.

### Exact-pattern warning

If the scientific question instead requires

\[
z_a=1\quad\Longleftrightarrow\quad a\in D(M),
\tag{3.3}
\]

then impose the reverse implication by forbidding low-to-\(r_a\) arcs when
\(z_a=0\).  The cells

\[
\mathcal M_{=}(S)=\{M:D(M)\cap A=S\}
\tag{3.4}
\]

are disjoint rather than nested.  The order-ideal theorem and its upward
conflict cuts then do not apply; a failed exact vector excludes only that
vector unless a whole partial cube is universally refuted.

The drop-12 witness happens to realize its intended exact named pattern:
all retained 26 roots are verified direct-low, while omitted row 12948 is
middle-fed.  The corresponding fact has not been independently replayed
locally for summary-only drops 15 and 16.

## 4. Why deleting a forced root can raise supplier rank

Deleting action \(a\) restores all rank-seven-middle-to-\(r_a\) arcs.  It
does not delete the root or assign a numerical supplier credit.  If a new
matching uses one of the restored arcs, the symmetric difference between the
old and new dummy-expanded perfect matchings is a union of alternating even
cycles, one containing a restored arc.

In the rank-seven transversal-matroid layer, a forced direct-low action keeps
its root outside the receiver basis.  Releasing it permits that root to enter
the basis along a fundamental alternating path; cardinality forces other
roots to leave.  This is ordinary basis exchange structurally.  Supplier
rank after table/state compilation is not a matroid rank on the action bits.

For drop 12, the released root changes literally from

\[
\text{row }12948:\quad
(65578,66414)\longrightarrow(14,65902,66414).
\tag{4.1}
\]

The two complete tables differ on 22 chain rows.  Their receiver-basis
change is three-for-three:

\[
B_{12}\setminus B_{27}=\{12948,21693,22609\},
\qquad
B_{27}\setminus B_{12}=\{17961,21308,22483\}.
\tag{4.2}
\]

The supplier graph is regenerated from this whole rerouting.  Its controlling
shore changes from all-27's 23 heads and neighbor \(\{14851\}\) to a
different 23-head shore with neighbors \(\{12973,14851\}\).  Two old shore
heads are replaced, and zero heads fall from 21 to 19.  The rank increase is
therefore a property of the joint presentation and supplier matchings.

The summaries give a direct no-additivity example: drops 12 and 15 each
improve deterministic rank by one, while the joint drop
\(\{12,15\}\) remains at deficiency 21 rather than improving to 20.
The same holds for \(\{15,16\}\).  Restored alternating cycles can conflict,
and several changes can expose the same distinct supplier OR.

## 5. Exact subset-local Hall cuts

Fix a SHA-bound subset node \(\Pi_S\), including its compressed carrier,
fixed overlay, final-table semantics, protected ledger, phase occurrences,
root presentation, and supplier compiler.  For a complete state \(M\), let

\[
a_h^S(M)=1
\quad\Longleftrightarrow\quad
h\text{ is an active hard-head occurrence},
\tag{5.1}
\]

and let \(e_{hu}^S(M)\) be its literal incidence with supplier identity
\(u\).  For a semantic shore \(Q\), define

\[
\Gamma_Q^S(M)=
\sum_{h\in Q}(1-a_h^S(M))
+
\sum_u\bigvee_{h\in Q}
\left(a_h^S(M)\wedge e_{hu}^S(M)\right).
\tag{5.2}
\]

All alternatives exposing the same supplier belong inside one OR.

### Theorem 5.1 (local Hall separator)

Every completion of supplier deficiency at most \(d\) satisfies

\[
\boxed{\Gamma_Q^S(M)\ge |Q|-d}
\tag{5.3}
\]

for every \(Q\).  A maximum supplier matching either reaches the target or
returns a violated maximum shore.

#### Proof

The first sum in (5.2) counts inactive potential heads, and the second counts
the distinct supplier neighborhood of the active heads in \(Q\).  Equation
(5.3) is Hall's deficiency inequality after rearrangement. \(\square\)

The three current records are tight for target 21:

\[
\begin{array}{c|c|c|c}
\text{node}&|Q|&|N(Q)|&|Q|-21\\\hline
\text{drop 12}&23&2&2\\
\text{drop 15}&22&1&1\\
\text{drop 16}&22&1&1.
\end{array}
\tag{5.4}
\]

For target 20, the exact next local obligations are

\[
\Gamma_{Q_{12}}^{12}\ge3,
\qquad
\Gamma_{Q_{15}}^{15}\ge2,
\qquad
\Gamma_{Q_{16}}^{16}\ge2.
\tag{5.5}
\]

Each incumbent is short by exactly one **net** credit.  These are not the
same compiled cut.  Every activity predicate, incidence predicate, supplier
OR, and constant must be regenerated on its own carrier/final-table pair.
The drop-15 and drop-16 rows in (5.5) remain summary-level obligations until
their complete local bundles and semantic circuits are frozen.

## 6. Exact state-expanded 27-bit master

All current enforced subsets share one literal bf5 carrier, protected ledger,
ten-mode overlay, and occurrence-pin set.  Before accepting a winning subset
as a new recursive parent, their exact global comparison can therefore be
made in one state-expanded master.

Let \(x_e\) select presentation arcs in the dummy-expanded bipartite graph.
Impose the exact unit matching equations, the fixed protected/mode/occurrence
pins, and the residual dummy cardinality.  For each action \(a\), impose

\[
x_{m,r_a}\le1-z_a
\quad
\text{for every rank-seven }m\subset r_a.
\tag{6.1}
\]

Equation (6.1) is exactly the implemented forcing-only semantics.

Let \(\phi_{hu}(x)\) be the complete Boolean supplier-incidence compiler
after the fixed overlay, and let \(y_{hu}\) select supplier matching edges.
The exact matching layer is

\[
y_{hu}\le\phi_{hu}(x),
\qquad
\sum_u y_{hu}\le a_h(x),
\qquad
\sum_h y_{hu}\le1,
\tag{6.2}
\]

\[
\sum_{h,u}y_{hu}\ge\sum_h a_h(x)-d.
\tag{6.3}
\]

On the fixed 16,898-head universe, (6.3) becomes
\(\sum y_{hu}\ge16898-d\).  An arbitrary nonnegative action objective is

\[
\max\sum_{a\in A}w_a z_a.
\tag{6.4}
\]

Eliminating \(y\) yields precisely all Hall inequalities (5.3).  This gives
an exact finite branch-flow/Benders formulation.  No total-unimodularity
claim is made: the supplier compiler \(\phi\) couples the presentation
matching to head and edge state nonlinearly.

If the activity/incidence circuits are complete for the shared fixed face,
a Hall row may be compiled globally over \(x\).  A circuit derived only from
one materialized subset table must instead be guarded by that node's complete
state digest and regenerated elsewhere.

## 7. Universal subset cuts and global optimality

A bad deterministic completion \(M_{\rm alg}(S)\) excludes only that
completion.  It excludes enforced subset \(S\) only after proving

\[
\forall M\in\mathcal M(S)\;\exists Q:
\Gamma_Q^S(M)<|Q|-d.
\tag{7.1}
\]

The shore may depend on \(M\).  Interchanging the completion minimum with
the Hall maximum is not valid.

For a fixed shore, define the exact optimistic recourse credit

\[
U_Q(S)=\max_{M\in\mathcal M(S)}\Gamma_Q^S(M).
\tag{7.2}
\]

The bound

\[
U_Q(S)\le |Q|-d-1
\tag{7.3}
\]

is a sufficient universal one-shore infeasibility certificate.  Once either
(7.1) or (7.3) is authenticated, downward closure gives the valid outer
conflict

\[
\boxed{\sum_{a\in S}z_a\le |S|-1,}
\tag{7.4}
\]

which excludes \(S\) and every superset.  Without universal recourse
coverage, (7.4) is unsound.

A proof-safe global search maintains:

1. literal joint witnesses and the downward cones they certify;
2. an antichain \(\mathcal I\) of universally infeasible cores and their
   upward cones;
3. exact state-local Hall cuts for complete candidate presentations; and
4. lifted no-goods for individual bad completions that cannot yet be
   projected.

Let \(F^*\) be a feasible incumbent.  It is globally maximum weight under
(6.4) exactly when every \(S\subseteq A\) with

\[
\sum_{a\in S}w_a>\sum_{a\in F^*}w_a
\tag{7.5}
\]

contains some \(I\in\mathcal I\).  Equivalently, the Boolean master formed by
the core clauses and a strictly better objective bound is UNSAT.  Each core
must carry its structural Hall or exhaustive lifted Hall-Benders proof.

For unit weights and target 21, any deficiency-21 26-action witness gives
the lower bound 26.  The only possible larger set is all 27 actions.
Therefore

\[
\operatorname{OPT}_{21}=26
\quad\Longleftrightarrow\quad
\nexists M\in\mathcal M(A):\delta(M)\le21.
\tag{7.6}
\]

The known all-27 table of deficiency 22 proves failure of one \(M\), not the
universal statement in (7.6).  An exhaustive all-27 recourse proof is both
necessary and sufficient for the desired cardinality optimality; no
one-drop, two-drop, or larger radius enumeration can replace it.

The three feasible coatoms imply one limited structural fact.  If all 27 is
eventually proved target-21 infeasible, every inclusion-minimal infeasible
core \(I\subseteq A\) must contain actions 12, 15, and 16.  They do not imply
the stronger clause “drop one of 12, 15, or 16.”

More generally,

\[
\boxed{
\max_{\substack{S\subseteq A\\\delta^*(S)\le d}}|S|
=
\max_{\substack{M\in\mathcal M(\varnothing)\\\delta(M)\le d}}
|D(M)\cap A|.}
\tag{7.7}
\]

#### Proof

For every left-hand witness \(S,M\), equation (2.4) gives
\(S\subseteq D(M)\), so \(|S|\le|D(M)\cap A|\).  Conversely, every
right-hand matching is feasible for \(S=D(M)\cap A\), giving equality.
\(\square\)

If the objective is supplier deficiency alone rather than the number or
weight of enforced actions, subset enumeration is redundant:

\[
\min_{S\subseteq A}\delta^*(S)=\delta^*(\varnothing).
\tag{7.8}
\]

One should then optimize the presentation/common-basis matching directly and
derive the realized root types from it.

## 8. Audit boundary and remaining work

The complete drop-12 bundle is an exact deficiency-21 witness for the
complete 6/9/4 supplier row-pair projection on the fixed ten-mode,
23-occurrence face.  It remains outside address/state circulation,
long--long chronology, residence, upper, common-cap, compiler, and word
closure.

The current deterministic search covers all 27 one-drop sets and exactly 75
of the 351 two-drop sets: those containing at least one of actions 12, 15,
or 16.  The other 276 pairs and every set with at least three drops were not
replayed.  This coverage has heuristic value but no bearing on the exact
criterion (7.6).

Before treating drop 15 or drop 16 as a recursive parent, freeze and replay
its individual compressed and final tables, 26-action ledger,
materialization audit, supplier graph, maximum matching, Hall shore, compiler
input SHA, and source/transcript.  Also check whether each omitted root is
actually middle-fed; a 26-action materializer count alone does not prove the
false bit.

The proof-safe conclusion is:

\[
\boxed{
\begin{gathered}
\text{three canonical deterministic records attain deficiency 21;}\\
\text{drop 12 has one complete joint matching certificate;}\\
\text{subset-level pruning requires universal recourse proofs;}\\
\text{target-21 cardinality optimality reduces exactly to the all-27}\\
\text{existential recourse decision, not to a bounded drop neighborhood.}
\end{gathered}}
\tag{8.1}
\]
