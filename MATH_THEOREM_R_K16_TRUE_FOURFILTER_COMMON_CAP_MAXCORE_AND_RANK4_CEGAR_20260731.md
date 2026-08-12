# True-four-filter K16 common-cap theorem and rank-four exact gate

## 0. Verdict and exact scope

This note concerns only the authenticated rank-eight chronology

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

with the monotone depth-three schedule

```text
start holes    X = {12870,12871,12872}
deadline holes Y = {0,1,6388}.
```

The chronology is the genuine four-filter descendant, is a permutation of
all (12870) rank-eight masks, and is complete at every upper rank.  Its
selected lower area is (32224).  The exact physical lower-cell inventory
has (32230) cells: (32224) selected proper prefixes and the physically
present omitted-start prefixes of counts (3,2,1).

The new conclusions are:

1. A fixed target-to-cell matching has an exact solver-free maximal-core
   criterion for literal realizability.
2. The deterministic perfect Hall matching is not realizable.  A two-edge
   nested-interval contradiction already proves this.
3. The unique singleton (0x8000) pin and the complete matching-unit closure
   are safe.  They force (14060) targets without deleting any further
   maximal-envelope bit.
4. The remaining exact common-cap problem has (12272) target rows and an
   exact (y/q) formulation with (285232) Boolean variables.  Because all
   physical pins have length at most three and all middle carriers have
   length at most four, every violated integral assignment has a CEGAR
   no-good of rank at most four.

No SAT or CP solver was run.  The reduced common-cap system remains open, so
this note does **not** prove a length-(12873) K16 word.

## 1. Schedule and maximal envelopes

Write the target rows as (T_0,ldots,T_{W-1}), where (W=12870).  Pair the
retained physical starts and deadlines increasingly:

\[
 s_0<\cdots<s_{W-1},\qquad d_0<\cdots<d_{W-1}.
\]

For the displayed schedule,

\[
0\le d_i-s_i\le3,
\]

and in fact the span histogram is (2^{6386}3^{6484}).  Define

\[
 I_i=[s_i,d_i],
 \qquad
 E_p=\bigcap_{i:p\in I_i}T_i.                         \tag{1.1}
\]

The literal replay gives

\[
\bigcup_{p\in I_i}E_p=T_i                              \tag{1.2}
\]

for every row.  Before the singleton pin, the envelope-rank histogram is

\[
5^{6481}6^{6388}7^2 8^2.                               \tag{1.3}
\]

Let ({\cal C}) be the exact physical lower cells: every proper prefix of a
selected row interval, together with the (3+2+1) available prefixes from
the three omitted starts.

For (C\in{\cal C}), a lower mask (S) is an individual candidate exactly
when capping (E_p) by (S) on (C) keeps every cell nonempty, realizes
(S) on (C), and does not erase the final host of a row bit.  This is the
individual-pin graph already used by the generalized Hall audit.

## 2. Exact fixed-matching maximal-core theorem

Let (M) be an injective assignment of every lower target (S),
(1\le |S|\le7), to a candidate cell (C_S\in{\cal C}).  Define the maximal
common core at physical position (p) by

\[
 K_p
 =E_p\cap\bigcap_{S:p\in C_S}S,                       \tag{2.1}
\]

where the empty second intersection is the full coordinate set.

### Theorem 2.1 (fixed matching, necessary and sufficient)

There exist nonempty source letters (A_p) which preserve every middle row
and realize every matched lower pin if and only if

\[
\begin{aligned}
K_p&\ne\varnothing &&(0\le p<12873),                    \tag{2.2}\\
\bigcup_{p\in I_i}K_p&=T_i &&(0\le i<W),                \tag{2.3}\\
\bigcup_{p\in C_S}K_p&=S &&(1\le |S|\le7).              \tag{2.4}
\end{aligned}
\]

When these conditions hold, the canonical assignment

\[
A_p=K_p                                                   \tag{2.5}
\]

is a literal realization.

#### Proof

Suppose (A) realizes the rows and pins.  If (p\in I_i), exactness of the
row OR gives (A_p\subseteq T_i).  Hence (A_p\subseteq E_p).  If
(p\in C_S), exactness of the pin OR gives (A_p\subseteq S).  Therefore
(A_p\subseteq K_p) for every (p).  Nonemptiness of (A_p) proves
(2.2).  Since the union of the (A_p)'s on a row or pin is the prescribed
mask and the corresponding union of (K_p)'s is contained in that mask,
(2.3)--(2.4) follow.

Conversely, put (A_p=K_p).  Equations (2.2)--(2.4) give nonempty letters,
all middle rows, and every matched lower pin literally.  ∎

This theorem is stronger than marginal Hall: it checks all overlapping caps
simultaneously and contains no independent-choice approximation.

### Corollary 2.2 (upper masks are automatic)

Assume the target chronology is upper-complete and the schedule has no chain
break, (s_{i+1}\le d_i+1).  Every assignment satisfying (2.3) realizes all
upper masks physically.

#### Proof

If (U=T_i\cup\cdots\cup T_j), the row intervals (I_i,ldots,I_j) cover
the physical interval ([s_i,d_j]).  Every (p\) in that physical interval
lies in some (I_h), (i\le h\le j), so (A_p\subseteq E_p\subseteq
T_h\subseteq U).  Conversely, (2.3) supplies every (T_h) inside the same
physical interval.  Its literal OR is therefore exactly (U).  ∎

Thus Theorem 2.1 plus the already audited upper-complete chronology is the
entire literal compiler gate for this fixed schedule.

## 3. Coordinatewise interval-cover form

For a matching (M) and coordinate (b), define the union of selected
(b)-opposing intervals

\[
 Z_b(M)=\bigcup\{C_S:b\notin S\}.                       \tag{3.1}
\]

Then

\[
b\in K_p\quad\Longleftrightarrow\quad
b\in E_p\text{ and }p\notin Z_b(M).                     \tag{3.2}
\]

Consequently Theorem 2.1 is equivalent to the following sixteen independent
interval-cover tests after the common matching has been chosen:

1. for every position (p), some (b\in E_p) obeys (p\notin Z_b);
2. for every row-bit carrier
   \[
   H_{i,b}=\{p\in I_i:b\in E_p\},
   \]
   one has (H_{i,b}\not\subseteq Z_b);
3. for every selected ((S,C_S)) and (b\in S),
   \[
   \{p\in C_S:b\in E_p\}\not\subseteq Z_b.             \tag{3.3}
   \]

The coordinates decouple after (M) is fixed; the only global coupling is
that all sixteen omission patterns come from the same target-to-cell
matching.

## 4. The deterministic perfect matching fails

The marginal graph has

```text
targets       26332
cells         32230
incidences   347734
matching      26332
matching SHA 73b815d0c891d73e88662f39b3ff40a1dc2bcb66191673ced88a0ec9aa280fb9
```

Applying (2.1) to this deterministic matching gives no empty source cell,
but it loses (1808) middle rows and (5045) matched lower pins.  Thus
nonemptiness alone is far from common-cap feasibility.

There is already a two-edge contradiction.  The matching contains

```text
target 0x0017 -> cell 16558 = [7648,7648]
target 0x4027 -> cell 16559 = [7648,7649].
```

The first equality requires coordinate (0x0010) in (A_{7648}).  The
second equality forbids that coordinate at both positions because
(0x0010\not\subseteq0x4027).  Hence this matching is impossible.

This is also a sharp warning against a purely laminar argument: the physical
cells are nested, yet the assigned labels are not inclusion-compatible.
The ordinary bipartite matching matrix remains integral, but interval
laminarity does not make its perfect matchings common-cap realizable.

## 5. Exact singleton closure and matching-unit closure

The target (0x8000) has exactly one individual cell,

\[
C_{8000}=[6389,6389].                                    \tag{5.1}
\]

Thus every literal completion forces

\[
A_{6389}=0x8000.                                         \tag{5.2}
\]

The pre-cap envelope at that position is (0xc304).  Substituting (5.2),
rebuilding the candidate graph, reserving its cell, and deleting (0x8000)
leaves

```text
free targets     26331
free cells       32229
free incidences 347677
matching          26331
matching SHA 7bb9086c5168a29f74560d3846cbd1579a6273874f39f13145214341eb6c36c0
```

So unit propagation preserves marginal Hall.  This second deterministic
matching still contains the same (0x0017/0x4027) contradiction.  Its
maximal core loses (1808) middle rows and (5037) pins.

Now repeatedly apply only the logically forced matching rules:

1. a target with one remaining cell must use it;
2. that cell is deleted from all other target domains.

There are (10053) initial non-(0x8000) units.  Closure fixes exactly

\[
14060                                                   \tag{5.3}
\]

targets including (0x8000), and leaves

\[
12272\text{ targets},\qquad18170\text{ cells},qquad
238472\text{ candidate edges}.                          \tag{5.4}

Most importantly, the simultaneous maximal core of all (14060) forced
pins is byte-for-byte the singleton-capped envelope.  It has no empty cell,
no row failure, and no forced-pin failure.  Therefore unit closure is a
positive exact reduction, not another hidden erosion obstruction.

The displayed two-edge conflict is not forced: in the pin-aware matching,
(0x0017) has an unused candidate ([7960,7961]), and (0x4027) has an
unused candidate ([10259,10260]).  Either is a one-edge augmenting exit.
Moving (0x4027) alone reduces the deterministic pin-failure count from
(5037) to (5035), but leaves all (1808) row failures.  Thus the local
conflict can be repaired, while a one-conflict greedy rule does not solve
the coupled system.

## 6. Exact reduced (y/q) system

Let ({\cal R}) be the (12272) targets remaining after unit closure, and
let (D(S)) be each reduced candidate domain.  Introduce

\[
y_{S,C}\in\{0,1\}\qquad(S\in{\cal R},\ C\in D(S)).       \tag{6.1}
\]

For every envelope coordinate ((p,b)) which some remaining candidate can
kill, introduce (q_{p,b}\).  It means that (b) survives in the maximal
common core at (p).  Coordinates which no remaining edge can kill are
fixed to one and are eliminated.

For

\[
{\cal D}_{p,b}
=\{(S,C):p\in C,\ b\notin S\},                          \tag{6.2}
\]

use the exact definition

\[
q_{p,b}=1-\bigvee_{e\in{\cal D}_{p,b}}y_e.               \tag{6.3}
\]

In direct Boolean form this is one binary implication
(y_e+q_{p,b}\le1) per (e\in{\cal D}_{p,b}), together with

\[
q_{p,b}+\sum_{e\in{\cal D}_{p,b}}y_e\ge1.               \tag{6.4}
\]

The complete system is:

\[
\begin{aligned}
\sum_{C\in D(S)}y_{S,C}&=1 &&(S\in{\cal R}),             \tag{6.5}\\
\sum_{S:C\in D(S)}y_{S,C}&\le1 &&(C\text{ free}),        \tag{6.6}\\
\bigvee_{p\in H_{i,b}}q_{p,b}&=1 &&(i,b\in T_i),         \tag{6.7}\\
y_{S,C}&\Longrightarrow
\bigvee_{p\in C:\ b\in E_p}q_{p,b}
&&(S\in{\cal R},C\in D(S),b\in S).                    \tag{6.8}
\end{aligned}

Tautologies containing a fixed-one (q) are deleted.  Every physical
position has at least one fixed-one envelope coordinate after unit closure,
so source nonemptiness requires no residual row.

### Theorem 6.1 (reduced system is exact)

The genuine four-filter fixed schedule has a literal compiler if and only if
(6.3)--(6.8) is feasible.

#### Proof

Every literal compiler chooses one witness cell for each remaining target;
these choices satisfy (6.5), and two distinct target labels cannot use the
same physical interval, giving (6.6).  Equation (6.3) is exactly (2.1) in
coordinate form.  Conditions (6.7)--(6.8) are precisely (2.3)--(2.4).

Conversely, a solution defines the common core through (6.3).  The forced
unit pins are already exact and leave the capped envelope unchanged.
Equations (6.7)--(6.8), together with the fixed-one nonempty coordinates,
therefore satisfy Theorem 2.1.  Taking (A_p=K_p) gives every lower mask,
every middle mask, and by Corollary 2.2 every upper mask.  ∎

The exact simplified model size is

```text
y variables                                      238472
q variables                                       46760
total Boolean variables                          285232

target exactly-one cardinality rows               12272
cell at-most-one cardinality rows                  18170
killer binary implications                       561707
q reverse-definition rows                         46760
nonempty rows after constant simplification           0
middle-survival rows                               28940
conditional pin-recovery rows                    465611
--------------------------------------------------------
direct semantic constraint groups              1,133,460
```

The last total counts each cardinality or long disjunction as one semantic
constraint; it is not a claim about a particular CNF cardinality encoding.

## 7. Rank-four CEGAR theorem

The reduced system admits an exact matching-only lazy interface.

### Theorem 7.1 (every common-cap violation has rank at most four)

Let (M) be any integral matching satisfying (6.5)--(6.6).  If its maximal
core fails Theorem 2.1, then one can extract a no-good

\[
\sum_{e\in F}y_e\le |F|-1                              \tag{7.1}
\]

with (|F|\le4), violated by (M) and valid for every literal compiler.

#### Proof

The exact catalogue verifies that after unit closure every position has an
envelope coordinate which no remaining candidate edge can kill.  Therefore
an empty-cell violation is impossible.

Suppose a row bit (b) is lost.  Its carrier (H_{i,b}) has at most four
positions.  For every (p\in H_{i,b}), choose one selected interval whose
label omits (b) and contains (p).  The chosen set (F) has size at most
four and its simultaneous selection covers the whole carrier by
(b)-opposing intervals.  No literal compiler can retain all of (F), so
(7.1) is valid.

Suppose instead that a selected pin (e=(S,C)) loses (b\in S).  Include
(e) in (F).  For each position (p\in C) at which (b\in E_p), choose
one selected (b)-opposing interval covering (p).  Since (|C|\le3), the
result has size at most (1+3=4).  Retaining all of these selections makes
the pin OR omit (b), so again (7.1) is valid.  ∎

### Corollary 7.2 (finite exact solve interface)

Begin with the ordinary reduced bipartite perfect-matching master
(6.5)--(6.6).  For each integral matching, compute (2.1).  Accept exactly
when Theorem 2.1 passes; otherwise add the rank-at-most-four cut from Theorem
7.1.  This finite CEGAR procedure is sound and complete for the fixed
schedule.

The base matching polytope is totally unimodular.  The new rank-two through
rank-four exclusions are the precise additional common-cap content which
ordinary Hall omits.  No claim is made here that a particular augmented
constraint matrix is or is not totally unimodular.  The
(0x0017/0x4027) certificate is the smallest rank-two calibration.

## 8. Exact remaining boundary

What is proved:

* the true-four-filter chronology, schedule, scalar capacity, and marginal
  Hall gate are live;
* both saved deterministic perfect matchings are literally impossible;
* all forced matching units are simultaneously safe;
* the common-cap gate reduces exactly to either the (285232)-variable
  (y/q) system or matching CEGAR with cuts of rank at most four.

What remains unproved:

* feasibility or infeasibility of that reduced system;
* a deterministic exchange theorem guaranteeing that rank-at-most-four
  conflicts can all be removed;
* a literal length-(12873) K16 word.

The minimal countercondition to “perfect Hall matching implies compiler” is
therefore explicit: the chosen matching must also avoid complete coverage of
every middle carrier and selected-pin bit by the corresponding opposing
intervals (Z_b(M)).  For this carrier those obstructions are local of rank
at most four, but they are not absent automatically.

## 9. Replay artifacts

```text
scratch/audit_r_k16_true_fourfilter_commoncap_gate_20260731.py
scratch/k16_true_fourfilter_commoncap_gate_20260731.audit.json
```

The checker is standard-library only, runs solver-free, authenticates the
target SHA, reconstructs both candidate graphs and matchings, verifies the
two-edge certificate, performs complete unit closure, and recomputes every
model-size count above.
