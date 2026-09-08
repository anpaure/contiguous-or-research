# Lane A: exact full-signature collar portal at the $k=15$, Hall-29 gate

**Date:** 2026-07-28  
**Scope:** resident/all-upper bounded-support augmentation from the authoritative
Hall-29 chronology  
**Computation policy:** no combinatorial search was run on the Mac.  The heavy
run prepared below is for H100 CPU only.

## 0. Outcome and exact boundary of the result

This note proves the complete certificate theorem for a bounded successor
trade $H_{29}\to P$, including the endpoint collars and the all-shore moving
DM condition.  It also supplies two executable, independently separated
artifacts:

```text
scratch/laneA_k15_bounded_a29_upper_cpsat.py
scratch/laneA_k15_full_signature_collar_portal.py
```

The first artifact searches a precisely stated four-parent bounded-support
class.  The second does not trust the fixed-(A_{29}) objective: it rebuilds
the complete compiler graph, checks residence and every upper rank, computes
the exact all-shore maximum matching, pairs cells by their complete target
neighbourhoods, rematches every displaced old matching edge, and constructs
an explicit alternating-tree portal matching of size $16355$.

Remote transfer was unavailable in this task.  In accordance with the master
instruction, no heavy local substitute was run.  Therefore this note does
**not** claim that a Hall-$28$ carrier has been found, and it does not claim a
completed finite no-go.  The unconditional advance is the exact certificate
theorem and proof-safe H100 model.  The smallest candidate-specific gate is
the bounded Hall system (4.2) below.

## 1. Exact compiler graphs and endpoint signatures

Let

\[
 {\cal L}=\{T\subseteq[15]:1\le |T|\le7\},
 \qquad |{\cal L}|=16383.
\tag{1.1}
\]

For a factorable middle path (P) of length
(W=\binom{15}{8}=6435), let

\[
 G(P)=({\cal L},{\cal C}(P);E(P))
\tag{1.2}
\]

be the exact depth-three lower compiler graph.  The cell shore has

\[
 |{\cal C}(P)|=(W+3)+(W+2)+(W+1)=19311.
\tag{1.3}
\]

For (c\in{\cal C}(P)), define its **complete signature**

\[
 \Sigma_P(c):=N_{G(P)}(c)\subseteq{\cal L}.
\tag{1.4}
\]

This is the full rank-$1,\ldots,7$ target neighbourhood, not the envelope,
mandatory mask, endpoint vertex, (A_{29})-hit bit, or a projected local
state.

The graph builder uses the maximal truncated linear erosion on all (W+3)
letter positions.  At every row depth (h=0,1,2), it includes every start

\[
 0\le b\le W+2-h.
\tag{1.5}
\]

Thus the six left and six right boundary cells at each depth are literal
members of (1.3).  Their signatures are computed from the selected endpoint
collars.  There is no (+36) credit, no endpoint-identity proxy, and no
unconditioned boundary deletion.

## 2. Minimum exact cell replacement rank

For paths (P_0,P_1), let

\[
 a_i(S)=|\{c\in{\cal C}(P_i):\Sigma_{P_i}(c)=S\}|.
\tag{2.1}
\]

### Theorem 2.1 (full-signature replacement formula)

The minimum number of right cells that cannot be paired by a
neighbourhood-preserving partial bijection is

\[
 \boxed{
 s^*(P_0,P_1)
 =19311-\sum_S\min\{a_0(S),a_1(S)\}
 ={1\over2}\sum_S|a_0(S)-a_1(S)|.}
\tag{2.2}
\]

In particular, this formula includes the actual endpoint cells.  Physically
different cells with the same complete signature may be paired, because the
right shore consists of indistinguishable unit-capacity matching resources.

#### Proof

A zero-cost pair must belong to the same signature class, so class $S$
contributes at most $\min(a_0(S),a_1(S))$ pairs.  Pairing that many copies in
every class attains the sum.  Since both shores have size $19311$, the two
unpaired shore sizes agree and the total-variation identity in (2.2) follows.
$\square$

Fix a maximum matching (M) of (G(P_0)).  Within each signature class, pair
(M)-occupied old cells before unoccupied copies.  This minimizes the number
of displaced (M)-edges among all pairings attaining (2.2): if the new class
has (b) copies, at most (b) occupied old copies can be retained, and the
matched-first choice attains this bound class by class.

### Proposition 2.2 (endpoint-conditioned collar bound)

Let $t$ be the number of sources, including the dummy source, whose
successors differ between the dummy-rooted paths $P_0,P_1$.  Let
$\beta_\partial$ be the total-variation replacement rank of the two exact
36-cell endpoint-signature multisets.  Then

\[
 s^*(P_0,P_1)\le30t+\beta_\partial\le30t+36.
\tag{2.3}
\]

#### Proof

Discard the endpoint cells temporarily.  The audited full rooted supports at
depths $0,1,2$ use $9,10,11$ directed successor arcs.  One changed real
successor arc can therefore destroy at most $9+10+11=30$ old rooted words.
Pair every remaining common word literally.  Pair endpoint cells optimally
by their complete signatures; this leaves exactly
$\beta_\partial\le36$ endpoint copies.  This constructs a
signature-preserving partial bijection with at most the right side of (2.3)
unpaired old cells.  The optimum $s^*$ cannot be larger.  Counting the dummy
source in $t$ is conservative. $\square$

Lane I's mandatory-mask identity gives shorter pointwise states of lengths
$5,6,7$.  I do not replace $30$ by $18$ here: after changing the dummy cut, a
common short state can move between the interior and endpoint classes without
containing the changed normal arc.  The full-support proof above remains
valid, while an $18t+\beta_\partial$ global injection needs an additional
cut-transition argument and is not claimed.

This is the corrected endpoint accounting.  The number $36$ is only a
worst-case upper bound; the checker computes $\beta_\partial$ exactly and
still lists every unpaired endpoint cell.

## 3. The old alternating shore

For the authoritative carrier

```text
scratch/k15_doubletrans_05_213_hall29.json
```

the exact regression is

\[
 \nu(G(P_0))=16354,
 \qquad \delta(G(P_0))=29.
\tag{3.1}
\]

Starting from the (M)-unmatched left vertices and alternating through
nonmatching then matching edges gives the frozen DM shore

\[
 |A_{29}|=1524,
 \qquad |N_{P_0}(A_{29})|=1495.
\tag{3.2}
\]

The checker requires the supplied (A_{29}) witness to agree exactly with
this alternating-reachable set for its independently reconstructed (M).
It rejects the run if (3.1) or (3.2) fails.

## 4. Exact protected-collar portal theorem

Choose the matched-first pairing from Theorem 2.1 and write

\[
 \phi:{\cal C}(P_0)\setminus J_0
       \longrightarrow {\cal C}(P_1)\setminus J_1,
 \qquad |J_0|=|J_1|=s^*.
\tag{4.1}
\]

Let

\[
 B=\{x\in{\cal L}:M(x)\in J_0\}.
\]

Delete (J_0) from the old (M)-alternating digraph and let
(R_M(J_0)) be the left shore still reachable from the old unmatched
targets.

### Theorem 4.1 (one-cell collar portal)

Suppose that there are a cell (z\in J_1), a matching

\[
 \rho:B\hookrightarrow J_1\setminus\{z\},
\tag{4.2}
\]

using new compiler edges, and a target (x\in R_M(J_0)) with

\[
 xz\in E(P_1).
\tag{4.3}
\]

Then the checker constructs an explicit matching of (G(P_1)) of size

\[
 \boxed{16355},
\tag{4.4}
\]

and therefore

\[
 \delta(G(P_1))\le28.
\tag{4.5}
\]

#### Proof

Transport every $M$-edge whose cell is outside $J_0$ through $\phi$.
Complete these edges with $\rho$.  This gives a matching $M_1$ of size
$|M|=16354$, with the same unmatched left targets as $M$, and leaves $z$
free.  Complete signatures preserve every old alternating edge outside
$J_0$, so the old alternating path to $x$ transports to $G(P_1)$.
Toggle that path and append $xz$.  The result is an augmenting path for
$M_1$, hence a matching of size $16355$. $\square$

This is an all-shore statement.  It excludes relocation of another
deficiency-(29) block and is strictly stronger than increasing the old
(A_{29}) neighbourhood by one.

The local repair (4.2) is equivalent to the exact bounded Hall family

\[
 |N_{P_1}(X)\cap(J_1\setminus\{z\})|\ge |X|
 \qquad(X\subseteq B).
\tag{4.6}
\]

It has the immediate, genuine obstruction

\[
 |B|\le s^*-1.
\tag{4.7}
\]

Thus if every old unpaired cell is (M)-occupied, a collar-only rematch
cannot leave a portal cell free.  Condition (4.7) is necessary, not
sufficient; (4.6) is the exact remaining local test.

A negative result from one recorded (M,phi) excludes only that pair.  It
does not exclude another old maximum matching, another optimal within-class
pairing, deliberately sacrificing a pairable copy, or an augmentation that
uses several changed cells before entering the old alternating tree.

## 5. The H100 search model and its exact scope

The candidate generator uses the directed union of

\[
 H_{29},\quad H_{30},\quad H_{31},\quad \tau(1,12)H_{29}.
\tag{5.1}
\]

Let ({\cal P}_{b_0,b}) be the following finite class.

1. (P) is one dummy-rooted Hamilton circuit in the union, hence a Hamilton
   path after deleting the dummy.
2. Its augmented successor support relative to (H_{29}) lies in
   ([b_0,b]).  Start and terminal changes are counted exactly.
3. The maximal truncated erosion is exactly depth-three factorable.
4. For every $q=1,\ldots,7$ and every rank-$(8+q)$ upper target, $P$
   retains one complete directed witness window from one of the four parents.
5. The exact full-boundary fixed-shore inequality holds:

\[
 |N_P(A_{29})|\ge1496.
\tag{5.2}
\]

The retained-parent condition in item 4 is sufficient for all-upper coverage
but is stronger than it: synthesized mixed windows are not credited.

### Catalogue identity requirement

The producer and consumer catalogues are now required to be literally equal.
The generator canonicalizes every directed arc as an ordered pair of physical
rank-eight masks and freezes the resulting catalogue hash in both its report
and every candidate.  The full-signature consumer rebuilds that catalogue
from the required `--producer-payload`, recomputes its hash, checks every
candidate successor arc against it, and rejects unless both catalogues and
their cardinalities agree.  The endpoint/rooting contract is frozen as
`ANY_VERTEX_LINEAR_CUT_IN_PAYLOAD_CATALOGUE` on both sides, so equality covers
not only normal arcs but also the admissible linear-cut policy.

This is a full-union search, not the newer five-cycle face surrogate.  The
five-cycle face predicates are restricted sufficient architecture and are not
globally exact shore predicates.  No UNSAT or endpoint statement from those
restricted predicates is imported here.  If Lane A is later run on a branch,
the producer payload itself must contain exactly that branch catalogue and the
consumer must receive that same payload.

Likewise, no catalogue-level endpoint maximum is used in the portal proof.
Both endpoint palettes are evaluated on the two literal selected
chronologies, and $\beta_\partial$ is computed from those actual 36-cell
signature multisets.  Any future endpoint-maximum relaxation must be generated
on the identical producer/consumer catalogue before it can support a no-go.
The already audited pair no-gos remain exact on their pair catalogues, but
they are not silently promoted to mixed full-catalogue predicates.

### Theorem 5.1 (model equivalence and obstruction scope)

In default mode the CP-SAT model is feasible exactly when
({\cal P}_{b_0,b}\ne\varnothing).  Therefore an initial solver status
`INFEASIBLE` proves, subject to the trusted finite solver, that no carrier in
this precise retained-parent subclass can improve Hall (29\to28).

In `--no-retained-upper` mode item 4 is omitted.  Initial infeasibility there
is stronger: it rules out every factorable Hamilton path in the four-parent
union and support interval satisfying the necessary cut (5.2), hence every
resident/all-upper Hall-(le28) path in that interval.

#### Proof

`AddCircuit`, the inverse order variables, and the selected union-arc
implications describe one dummy-rooted Hamilton path and the same chronology
as the exact Thread-D automaton.  Since each source has one selected
successor,

\[
 (W+1)-\#\{\hbox{selected base-successor arcs}\}
\tag{5.3}
\]

is exactly augmented-successor Hamming support.  The Thread-D erosion and
carrier clauses are equivalent to depth-three factorability.  Its (19311)
cell claims are sound and complete existential witnesses for (5.2), including
all 36 endpoint cells.  A retained upper-witness Boolean implies every arc of
one literal parent window; the circuit then makes that window consecutive.
The OR over witnesses is imposed for every upper target.  These implications
prove both directions. (\square)

The count of activated claim variables printed by the solver is **not** the
exact value of (|N_P(A_{29})|); it is only a chosen sound witness count.  The
second artifact recomputes the exact value.

If candidates have already been emitted and a later solve says
`INFEASIBLE_AFTER_EMITTED_NOGOODS`, only the residual model is empty.  The
original model was satisfiable, and every emitted candidate must be audited.
Reaching `--solutions` is reported as `SOLUTION_LIMIT_REACHED`, never as
exhaustion.  An OR-Tools `INFEASIBLE` result plus the frozen model is a
reproducible trusted-solver obstruction, not a standalone formal UNSAT proof
trace.  When no-goods have been added, the artifact freezes both the initial
model and a `.final` model containing those exact emitted-candidate no-goods.

## 6. Independent acceptance conditions

An emitted candidate is accepted for this lane only if the second artifact
reports all of the following.

1. It is the complete rank-eight layer with Johnson adjacency.
2. It has zero residence defects, satisfies the exact (D^3) identity, and
   has zero upper holes at all depths $1,\ldots,7$.
3. Its augmented successor support is at most the explicitly supplied bound.
4. The declared producer catalogue hash and cardinality equal the consumer
   payload exactly, and every selected successor belongs to that catalogue.
5. The exact old regressions are (16354), (29), and (1524/1495).
6. The candidate full-shore maximum matching has size at least (16355).
7. For the requested mechanism, the output status is
   `PROTECTED_COLLAR_PORTAL_FOUND`; the JSON lists $J_0,J_1$, the full
   equal-signature pairing, $\rho$, the old and transported alternating
   path, the portal edge, and all (16355) edges of the constructed matching.
8. Every target--cell edge of that matching is independently rechecked from
   the candidate erosion.  Endpoint cells are treated exactly like all other
   physical cells.

The artifact also writes a complete maximum matching of the candidate, so an
all-shore Hall-(28) result remains checkable even if it uses a more general
augmentation than Theorem 4.1.

## 7. H100-only reproduction

After transferring the listed files to the H100 host, a first retained-upper
run at support (b) is:

```bash
PYTHONPATH=/dev/shm/orlib python3 \
  scratch/laneA_k15_bounded_a29_upper_cpsat.py \
  scratch/threadD_A29_4parent_payload.json \
  --output-dir out/laneA_b${b} \
  --report out/laneA_b${b}.report.json \
  --model-out out/laneA_b${b}.model.pb \
  --base-parent H29 --threshold 1496 \
  --support "${b}" --support-min 1 \
  --solutions 16 --seconds 14400 --workers 32 --seed 1
```

Every emitted chronology is then checked on the H100 CPU by

```bash
python3 scratch/laneA_k15_full_signature_collar_portal.py \
  scratch/k15_doubletrans_05_213_hall29.json \
  out/laneA_b${b}/laneA_b${b}_seed1_s*.json \
  --a29-witness scratch/k15_doubletrans_05_213_hall29.dm_witness.json \
  --producer-payload scratch/threadD_A29_4parent_payload.json \
  --max-support "${b}" --require-resident-all-upper \
  --output out/laneA_b${b}.collar_audit.json
```

The necessary relaxation is obtained by adding `--no-retained-upper` to the
first command.  No heavy part of either command should be run on the Mac.

Required transferable sources are

```text
scratch/laneA_k15_bounded_a29_upper_cpsat.py
scratch/laneA_k15_full_signature_collar_portal.py
scratch/threadD_A29_cpsat.py
scratch/threadD_A29_4parent_payload.json
scratch/k15_doubletrans_05_213_hall29.json
scratch/k15_doubletrans_05_213_hall29.dm_witness.json
scratch/fast_k15_compiler_hall.py
scratch/fast_k15_hall_dm_cli.py
scratch/sigma_multirow_linear_compiler.py
scratch/sigma_sat_solver.py
```

The search report freezes the payload, search script, Thread-D script, model,
and OR-Tools version hashes.  The independent audit freezes both chronology
hashes, the (A_{29}) witness hash, and its own checker hash.

## 8. Iteration boundary

A successful (29\to28) certificate does not automatically iterate against
the old (A_{29}).  For the next step one must:

1. take the certified candidate as the new incumbent;
2. recompute an exact maximum matching and its current maximum-deficiency DM
   shore;
3. rebuild the fixed-shore payload for that new obstruction; and
4. rerun Theorems 2.1 and 4.1 with the new old matching.

This is the precise moving-DM iteration.  Reusing only the old fixed shore
would again permit relocation and is not accepted.

## 9. Final proved/conditional boundary

Unconditionally proved here:

* the exact full-signature replacement formula (2.2);
* the endpoint-conditioned bound (2.3);
* the protected-collar portal theorem producing a literal (16355)-edge
  matching;
* the exact local Hall obstruction (4.6)--(4.7); and
* the model-equivalence and UNSAT-scope theorem for the bounded four-parent
  search.

Not proved here:

* existence of a carrier satisfying (4.2)--(4.3);
* a completed H100 infeasibility certificate for any numerical support bound;
* an unrestricted no-go beyond the four-parent union or beyond retained parent
  upper witnesses; or
* any iteration from Hall (28) to Hall zero.

The minimum remaining candidate-specific lemma is exactly:

> There is a resident/all-upper candidate in the chosen bounded-support class
> for which the matched-first full-signature collar satisfies (4.6) for some
> free portal cell meeting (R_M(J_0)).

The two artifacts decide that statement for every emitted chronology without
discarding or relaxing an endpoint boundary cell.

## 10. Frozen source ledger

At the close of this task the relevant SHA-256 values are

```text
56efba859a418783a6a9f36319676ed2e4c83aeb24493a610255225470bb7c5e  scratch/laneA_k15_bounded_a29_upper_cpsat.py
a4dddbd42d35818e2360bb26b7350da0a6e266e4b8bb4b52590cb278003a2b11  scratch/laneA_k15_full_signature_collar_portal.py
6e68ae34b872a7aab71a43b2b1b3019b5a112233e17d7629b5ba0f7325f56463  scratch/threadD_A29_cpsat.py
d17b69e4385cdef7c5c74db074f39c38b2451ab3cb24ccd4156d7b4c4a727df9  scratch/threadD_A29_4parent_payload.json
5516482eadaba4f8fb9549b41c79c3b949df2e3224ce68f9dacd3b5b6bc2d21c  scratch/k15_doubletrans_05_213_hall29.json
d329d6302257dcd31ad83192ea8f88e86b46eb364719b1bb040e75e761ebb6d6  scratch/k15_doubletrans_05_213_hall29.dm_witness.json
```
