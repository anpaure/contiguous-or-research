# Exact conflict-free circulation no-go for the three \(k=15\) two-state exports

Date: 2026-07-28

Status: unconditional finite theorem for the separated ambient-UNIT model,
with a reproducible exact SAT encoding, three explicit LP/Farkas cut
certificates, binary DRAT cross-checks, and an independent cut verifier.
Physical pinning, the complete upper tower, and the one-common-word
compiler are kept outside the circulation core.

## 0. Verdict

The three previously surviving target-envelope-safe two-state blocks have
no separated closure in the audited \(10,370\)-edge ambient UNIT
operation graph once deck-vertex capacity and controller-position
conflicts are enforced.

Ordinary endpoint reachability was therefore strictly misleading in all
three cases.

The exact pairing-free closure problem needs only one binary ambient
circulation, not two labelled commodities.  For a fixed block, use one
variable per ambient UNIT operation, impose:

1. exact deck divergence created by the two block arcs;
2. deck-state capacity one; and
3. at most one selected operation in every controller window of length
   eight.

The direct or crossed pairing is then chosen automatically by the cycle
decomposition.

All three instances are infeasible already in their linear relaxations:

* \(B_1\) has a nine-vertex reachable shore containing deck source
  \(4452\), neither required sink, and no allowed ambient exit;
* \(B_2\) needs two first operations whose complete candidate set lies in
  the capacity-one window \([3120,3127]\);
* \(B_3\) has the same contradiction in \([2236,2243]\).

Thus no conflict branching is needed for these instances.  The displayed
cuts are independently checkable without trusting Kissat or the CNF
encoding.

This theorem closes only pairwise separated compensation by the current
isolated ambient UNIT catalogue.  It does not exclude:

* overlapping or interacting auxiliary blocks;
* a joint multi-state compensation packet;
* exact-support compositions which the distance-seven separation rule
  deliberately forbids;
* non-UNIT operations;
* a rethreaded middle chronology; or
* a physical repair outside the current carrier.

## 1. Exact finite input

The carrier has

\[
k=15,\qquad r=8,\qquad d=3,\qquad W=6435.
\tag{1.1}
\]

The rank-eight middle deck is indexed by

\[
0,1,\ldots,6434.
\]

The maximal lower controller has positions

\[
0,1,\ldots,6437.
\]

The ambient operation catalogue is reconstructed from

scratch/k15_doubletrans_05_213_hall29.json

and

scratch/k15_h29_one_owner_cia_audit.json.

An ambient operation is a five-tuple

\[
e=(p,x,y,q,q'),
\tag{1.2}
\]

meaning that controller position \(p\) is changed by

\[
P'_p=P_p-\{y\}+\{x\},
\tag{1.3}
\]

and exactly one locally affected rank-eight state changes from deck value
\(T_q\) to deck value \(T_{q'}\).  Write

\[
\rho(e)=p,\qquad s(e)=q,\qquad d(e)=q'.
\tag{1.4}
\]

The audited reconstruction has:

\[
13,122\text{ theoretical UNIT pairs},
\tag{1.5}
\]

\[
10,370\text{ locally admissible ambient operation edges},
\tag{1.6}
\]

on \(6,359\) active deck vertices.

The present catalogue checks each isolated operation's controller
neighbour adjacencies, four-window middle ranks, and affected middle
adjacencies.  It is an overcatalogue for a complete physical compiler:
maximal erosion and every global pin/shadow condition are recomputed only
after operations are combined.  Infeasibility in this overcatalogue is
therefore a valid no-go for its physically admissible subset.

### 1.1 The three blocks

The three blocks are:

\[
\begin{array}{c|c|c|c}
&\text{controller edits }(p,+x,-y)
&\text{exported deck arcs}
&\text{controller-envelope service}\\ \hline
B_1&
(3151,+12,-13),(3152,+11,-13)&
3148\to685,\ 3149\to4452&
(6308,\text{ cell }3152)\\
B_2&
(3266,+12,-6),(3267,+11,-6)&
3263\to3120,\ 3264\to3121&
(6308,\text{ cell }3267)\\
B_3&
(3268,+2,-6),(3269,+12,-6)&
3268\to2236,\ 3269\to2237&
(6308,\text{ cell }3268).
\end{array}
\tag{1.7}
\]

Here

\[
6308=\{2,5,7,11,12\}
\tag{1.8}
\]

in zero-based coordinate notation.

All three are alternatives for one target, not three additive Hall gains.
The singleton controller states after the atomic edits equal \(6308\) at
the displayed cells.  This is a controller-envelope fact.  It is not yet
the assertion that a final physical letter \(A'_p\) equals \(6308\).

The four deck ports of every block are distinct.

## 2. Conflicts and the smallest exact circulation

Fix one block \(B\), with exported arcs

\[
\beta_i:a_i\longrightarrow b_i,
\qquad i=1,2.
\tag{2.1}
\]

An ambient operation conflicts with \(B\) when

\[
\min_j|\rho(e)-p_j|\le7,
\tag{2.2}
\]

where \(p_1,p_2\) are the two controller positions of \(B\).
Delete every such operation.

Two retained ambient operations conflict when

\[
|\rho(e)-\rho(f)|\le7.
\tag{2.3}
\]

This is the audited separated-position model.  A future exact-support
model may replace (2.2)--(2.3) by overlap of complete dependency supports.

For a deck vertex \(v\), define

\[
\alpha_v=|\{i:a_i=v\}|,
\qquad
\beta_v=|\{i:b_i=v\}|.
\tag{2.4}
\]

Because the four ports are distinct,

\[
\alpha_v,\beta_v\in\{0,1\},
\qquad
\alpha_v\beta_v=0.
\tag{2.5}
\]

Use one binary variable

\[
x_e\in\{0,1\}
\tag{2.6}
\]

for every retained ambient operation.

### Theorem 2.1 (pairing-free exact circulation ILP)

The block has a separated ambient UNIT deck closure if and only if
\(x\) satisfies, for every deck vertex \(v\),

\[
\boxed{
\sum_{s(e)=v}x_e+\alpha_v
=
\sum_{d(e)=v}x_e+\beta_v
\le1,}
\tag{2.7}
\]

and, for every integer controller-window start \(t\),

\[
\boxed{
\sum_{\substack{e:\\t\le\rho(e)\le t+7}}x_e\le1.}
\tag{2.8}
\]

No direct/crossed pairing variable and no commodity label are needed.

#### Proof

Given a separated closure \(F\), put \(x_e=1\) precisely on \(F\).
Condition (2.7) is exactly

\[
\deg^-_{F\cup\{\beta_1,\beta_2\}}(v)
=
\deg^+_{F\cup\{\beta_1,\beta_2\}}(v)
\in\{0,1\}.
\]

Condition (2.8) is equivalent, for binary variables, to all pairwise
position conflicts (2.3).

Conversely, let \(x\) satisfy (2.7)--(2.8).  The selected ambient edges
together with the two block arcs form a vertex-disjoint union of directed
cycles.  Delete every cycle containing no block arc.  If the two block arcs
lie on different cycles, deleting them leaves the direct path pair.  If
they lie on one cycle, deleting them leaves the crossed path pair.  The
remaining operations stay conflict-free. \(\square\)

The formulation has one binary variable per retained ambient operation.
Fixing the direct or crossed pairing gives an equivalent two-commodity
formulation, but uses a strictly larger variable formulation when either
pairing is acceptable; it does not enlarge the fixed-pairing feasible set.

### 2.1 Single-commodity interpretation

Equivalently, add a super-source \(\sigma\) with unit arcs to
\(b_1,b_2\), add unit arcs from \(a_1,a_2\) to a super-sink \(\tau\),
and node-split every deck vertex with capacity one.  Ignoring position
conflicts, closure is an integral \(\sigma\)-to-\(\tau\) flow of value two.

The position rows (2.8) add a stable-set constraint on operation edges.
Thus the exact object is a conflict-free, vertex-capacitated,
single-commodity value-two flow.  It is not an ordinary reachability test.

## 3. Dual and exact certificate systems

Write the balance equations as

\[
Mx=r,
\tag{3.1}
\]

the vertex and conflict inequalities as

\[
Ax\le c,
\tag{3.2}
\]

and retain \(x\ge0\).

### Proposition 3.1 (LP/Farkas certificate)

The linear relaxation is infeasible whenever there are a free vector
\(y\) and a nonnegative vector \(\lambda\) such that

\[
M^\top y\le A^\top\lambda,
\tag{3.3}
\]

\[
r^\top y>c^\top\lambda.
\tag{3.4}
\]

#### Proof

For any feasible \(x\),

\[
r^\top y
=x^\top M^\top y
\le x^\top A^\top\lambda
=\lambda^\top Ax
\le\lambda^\top c,
\]

contradicting (3.4). \(\square\)

The explicit cuts in Section 4 are integer linear combinations of deck
balance and nonnegativity rows.  The \(B_2,B_3\) certificates additionally
use one controller-window row; the \(B_1\) certificate instead uses a
closed reachable shore.  Hence all three certify LP infeasibility and
automatically certify integer infeasibility.

### Proposition 3.2 (complete conflict-branch/mincut certificate)

For a general instance not refuted by an LP cut, an exact finite
infeasibility certificate is a binary conflict-branch tree:

1. at an internal node choose one unresolved conflict \(e\#f\);
2. its two children delete \(e\) and delete \(f\), respectively;
3. at every leaf, after no conflict remains, attach a unit-capacity
   \(\sigma\)-to-\(\tau\) cut of capacity at most one.

Such a tree certifies that no conflict-free closure exists.  Conversely,
if no closure exists, exhaustive branching produces such a certificate.

#### Proof

Every stable operation set omits at least one member of each conflict pair,
so it survives at least one child at every internal node.  At a
conflict-free leaf the residual problem is an ordinary vertex-capacitated
network flow.  Network integrality says that failure of a value-two flow is
equivalent to a cut of capacity at most one.  Exhaustive branching is
finite. \(\square\)

Conflict rows destroy network total unimodularity in general.  For example,
take the reduced directed-incidence rows of a directed three-cycle and add
the valid conflict row selecting two consecutive cycle edges.  The
resulting square minor is

\[
\begin{pmatrix}
1&0&-1\\
-1&1&0\\
1&1&0
\end{pmatrix},
\qquad
\det=2.
\tag{3.5}
\]

Therefore an LP/Farkas certificate is sufficient but not complete for
arbitrary integer instances; Proposition 3.2 is the exact fallback.

For the present three blocks, the direct LP cuts below make branching
unnecessary.

## 4. The three explicit cut certificates

### Theorem 4.1 (all three separated closures are infeasible)

None of \(B_1,B_2,B_3\) has a solution to (2.7)--(2.8) in the audited
ambient UNIT catalogue.

#### Proof for \(B_1\)

After deleting every ambient operation within seven positions of
\(3151\) or \(3152\), the exact reachable deck shore from \(4452\) is

\[
\begin{split}
R=\{&
461,1732,3153,4452,4499,\\
&4726,5100,5738,5752\}.
\end{split}
\tag{4.1}
\]

It contains block destination \(4452\), neither block source
\(3148,3149\), and has no allowed ambient edge leaving \(R\).

Before block-conflict deletion, the only ambient exits from \(R\) are

\[
(3153,+2,-12):3153\to3609,
\tag{4.2}
\]

\[
(3156,+14,-4):3153\to2792.
\tag{4.3}
\]

Both positions lie within seven of the atomic block and are therefore
deleted.

Sum (2.7) over \(v\in R\).  Internal ambient edges cancel.  Since one block
arc enters \(R\) and no block arc leaves,

\[
x(\delta^+R)-x(\delta^-R)=1.
\tag{4.4}
\]

But \(\delta^+R\) is empty in the retained ambient graph, so the left side
is nonpositive.  This contradicts (4.4).

Equivalently, in the supernetwork of Section 2.1,
\(\{\sigma\}\cup R\) is a cut of capacity one: only the unit arc from
\(\sigma\) to the other block destination crosses it.

#### Proof for \(B_2\)

The marked block arcs enter deck vertices \(3120\) and \(3121\).
At each vertex, capacity one forbids an ambient incoming edge and balance
forces exactly one ambient outgoing edge.

The complete retained outgoing catalogue is:

\[
\begin{array}{c|c}
\text{deck source}&\text{ambient options}\\ \hline
3120&
(3120,+0,-9):3120\to2325,\\
&
(3123,+11,-7):3120\to4788,\\[2mm]
3121&
(3121,+9,-1):3121\to4789,\\
&
(3124,+6,-11):3121\to3264.
\end{array}
\tag{4.5}
\]

All four positions lie in the controller window

\[
[3120,3127].
\tag{4.6}
\]

The two balance equalities force the sum of the four variables in (4.5) to
be \(2\), while the single window inequality (2.8) bounds that sum by
\(1\).  Contradiction.

#### Proof for \(B_3\)

The marked block arcs enter deck vertices \(2236\) and \(2237\), so again
one ambient outgoing edge is forced at each.

The complete retained outgoing catalogue is:

\[
\begin{array}{c|c}
\text{deck source}&\text{ambient options}\\ \hline
2236&
(2236,+1,-2):2236\to3573,\\
&
(2239,+3,-4):2236\to2327,\\[2mm]
2237&
(2237,+2,-7):2237\to4973,\\
&
(2240,+9,-3):2237\to2412.
\end{array}
\tag{4.7}
\]

All four positions lie in

\[
[2236,2243].
\tag{4.8}
\]

The two forced-outgoing equalities give total \(2\); the one window row
gives total at most \(1\).  Contradiction. \(\square\)

The three proofs choose neither direct nor crossed pairing.  They exclude
both simultaneously.

## 5. Exact SAT encoding and reproducible certificates

The solver is

scratch/solve_k15_two_state_conflict_circulation.py.

It reconstructs the ambient catalogue, removes block conflicts, and writes
an exact CNF:

* one Boolean variable per retained ambient operation;
* pairwise clauses for every distance-seven position conflict;
* at-most-one clauses for ambient indegree and outdegree at every deck
  vertex;
* exact balance implications at ordinary vertices; and
* forced predecessor/successor clauses at the four block ports.

This CNF is propositionally equivalent to (2.7)--(2.8).  Ambient-only
cycles are permitted; a SAT witness would be pruned to the one or two
cycles containing the block arcs and independently rechecked.

Kissat \(4.0.4\) returns UNSAT for all three blocks.

\[
\begin{array}{c|c|c|c|c}
&\text{variables}&\text{clauses}&
\text{block-conflicting operations removed}&\text{cut type}\\ \hline
B_1&10,338&157,061&32&\text{reachable shore}\\
B_2&10,350&157,400&20&\text{controller window}\\
B_3&10,348&157,377&22&\text{controller window}.
\end{array}
\tag{5.1}
\]

The machine-readable result is

scratch/k15_two_state_conflict_circulation_certificate.json.

The independent verifier is

scratch/verify_k15_two_state_conflict_circulation_certificate.py.

It does not invoke Kissat and does not trust the CNF encoder.  It
reconstructs the \(10,370\) operations, checks the exact reachable shore or
window catalogue for each block, verifies the corresponding linear
contradiction, and separately recomputes each atomic block.

The three optional binary DRAT traces are:

scratch/k15_two_state_conflict_proofs/block_1.drat

scratch/k15_two_state_conflict_proofs/block_2.drat

scratch/k15_two_state_conflict_proofs/block_3.drat.

Their sizes and SHA-256 hashes are:

\[
\begin{array}{c|r|c}
&\text{bytes}&\text{SHA-256}\\ \hline
B_1&79,784&
02069112fb394f746348076e7b8fc2912e3a225e35e541b0ebb7ec3c5fa4f5fb\\
B_2&33,049&
d3515dc2935c60938d7a473ff61ab44c71da6743f0a6c979875efe9a699a6d02\\
B_3&92,718&
4a2586b6a9beff6974aa633e2dc074a19f4995e34602e624bf7a2ef2532339b8.
\end{array}
\tag{5.2}
\]

The theorem does not depend on trusting or checking these DRAT traces:
the JSON cut certificates and independent verifier prove the stronger LP
contradictions directly.  The traces are retained as a solver cross-check.

### 5.1 Reproduction

From the repository root, run:

    python3 scratch/solve_k15_two_state_conflict_circulation.py \
      --output scratch/k15_two_state_conflict_circulation_certificate.json \
      --proof-directory scratch/k15_two_state_conflict_proofs

Then run both verification paths:

    python3 scratch/solve_k15_two_state_conflict_circulation.py \
      --verify scratch/k15_two_state_conflict_circulation_certificate.json

    python3 scratch/verify_k15_two_state_conflict_circulation_certificate.py \
      scratch/k15_two_state_conflict_circulation_certificate.json

The generation run prints:

    {"statuses": {"1": "UNSAT", "2": "UNSAT", "3": "UNSAT"},
     "verified": true}

The solver's self-verification run prints:

    {"blocks_verified": 3,
     "sat_witnesses_verified": 0,
     "verified": true}

The independent cut verifier prints:

    {"ambient_operations": 10370,
     "blocks_verified_infeasible": 3,
     "controller_window_certificates": 2,
     "reachable_shore_certificates": 1,
     "verified": true}

The certificate records the carrier hash

5516482eadaba4f8fb9549b41c79c3b949df2e3224ce68f9dacd3b5b6bc2d21c

and hashes of the Hall audit, reconstruction sources, solver source, every
CNF, and every proof trace.

## 6. Physical pin and upper-shadow separation

The circulation core contains no physical-letter variables.  It proves or
refutes only exact rank-eight deck closure inside the declared separated
ambient catalogue.

The independent block diagnostics verify, before compensation, that every
one of \(B_1,B_2,B_3\):

1. retains rank-five controller states;
2. retains controller Johnson adjacency;
3. produces rank-eight middle states;
4. retains middle Johnson adjacency;
5. satisfies

   \[
   P'=\operatorname{erosion}(T');
   \tag{6.1}
   \]

6. has precisely the two exported deck arcs in (1.7); and
7. has controller state \(P'_p=6308\) at its displayed singleton cell.

Each atomic block is not deck-closed and changes the immediate-upper
multiset by deleting two and adding two colours.  These upper differences
are not circulation constraints in the present solver.

Even item 7 is not a physical pin theorem.  A final compiler must still
construct nonempty physical letters \(A'_p\subseteq P'_p\) and verify the
exact target interval union.  The current target-safe census tested
controller-envelope containment, not the one-common-word criterion.

Had a deck closure existed, the required post-solver audit would have
reconstructed the combined controller and middle word and checked:

* the exact advertised physical cell and pin;
* all \(1,489\) retained cells and the six old residual cells;
* the complete Hall current;
* every adjacent and deeper upper shadow;
* residence and deadlines;
* one common nonzero physical word;
* trace two and the owner skeleton.

No such post-solver audit is reached, because the deck circulation already
fails for all three blocks.

Additive upper-shadow rows may be appended only after every operation
exports a complete signed shadow signature and the conflict relation
separates the full relevant shadow collars.  The current distance-seven
controller separation does not automatically justify additivity through
all depths.  Recomputing the full tower on a final witness remains the
proof-safe route.

## 7. Proved boundary

The exact positive gate posed by the three rows of (1.7) is closed in the
separated isolated-UNIT model:

\[
\boxed{
\text{none of the three target-envelope-safe two-state blocks admits a
conflict-free ambient UNIT deck closure}.}
\tag{7.1}
\]

This is stronger than failure of the currently shortest paths and stronger
than integer infeasibility: each row has an explicit linear cut.

The next surviving positive mechanisms must leave at least one frozen
hypothesis of this theorem.  They may use:

1. an overlapping auxiliary interaction represented as one joint packet;
2. a larger target-safe local block;
3. a non-UNIT compensation operation;
4. an exact-support composition not admitted by distance-seven separation;
5. a middle-deck reordering; or
6. a different carrier/controller pair.

The separated no-go is now known to be sharp.  The independently verified
certificate in

THREAD_H_K15_POSITION_CONFLICT_TWO_COMMODITY_CIRCULATION_20260728.md

uses \(B_1\) inside a simultaneous nonseparated \(20\)-controller-state
circuit.  Fresh global recomputation proves exact middle-deck closure,
Johnson chronology, maximal erosion, and the literal singleton
\(P'_{3152}=6308\).  That interacting circuit is outside constraints
(2.2)--(2.3).  It is not a Hall repair: it loses eight rank-six lower
colours, fourteen rank-seven lower colours, and the three rank-nine upper
colours

\[
\{9661,23257,31457\}.
\tag{7.2}
\]

Thus the current positive gate beyond this report is a shadow-compatible
interacting circuit, beginning with preservation of the complete
immediate-upper shore.  Physical retained-cell and common-owner checks
remain later and separate.

No Hall-zero \(k=15\) compiler and no complete Shadow--Braid follows from
this finite no-go.

## 8. Independent audit

Two independent audits reconstructed the operation graph and checked:

* the orientation and signs of every deck-balance equation;
* the CNF equivalence at ordinary vertices and all four block ports;
* the exact distance-seven position clauses;
* the nine vertices and two removed exits of the \(B_1\) shore;
* every outgoing operation in (4.5) and (4.7);
* both controller windows and their capacity-one contradictions;
* all variable, clause, and removed-operation counts;
* every recorded source, data, CNF, and DRAT hash; and
* the separation between deck closure, controller-envelope service,
  physical pinning, and upper shadows.

The audits required only documentation corrections: “at most one” in the
window statement, correct attribution of the three console summaries,
separate descriptions of the shore and window Farkas cuts, and removal of
one stale pre-cut JSON artifact.  After these corrections neither audit
found a theorem-level defect.
