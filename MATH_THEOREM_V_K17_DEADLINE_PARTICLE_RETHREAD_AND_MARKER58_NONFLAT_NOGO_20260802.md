# K17 deadline particles, a clustered rethread gate, and the marker58 nonflat no-go

Date: 2026-08-02  
Lane: V  
Status: exact staircase theorem, exact fixed-host finite no-go, and an exact
resource-preserving rethread reduction.  No K17 word or lower compiler is
claimed.

## 0. Outcome

Let

\[
 W={17\choose9}=24310,
 \qquad L=W+3=24313,
 \qquad \Lambda=\sum_{j=1}^{8}{17\choose j}=65535.
\]

The three extra positions do not force the flat equation \(D^3A=T\).
They are exactly three start/deadline particles.  Their six thresholds
determine every owner interval, its variable length, the exact lower-cell
loss, chain alignment, and every coordinate residence corridor.

For a lower-q1-rainbow rank-nine chronology there are no singleton positive
runs.  Consequently all short-run constraints collapse to two frontiers,
not one clause per run.  The exact row/scalar gate is a two-ended four-integer
optimization followed by an explicit schedule.

For the authenticated connected marker58 cycle, however, the 2,873
length-two starts are distributed too evenly.  In both orientations every
one of the 24,310 cuts has exact clean-gap statistic

\[
                              G_2=36.
\]

An optimal K17 staircase requires \(G_2\ge20610\).  The length-two runs
alone therefore force

\[
       \operatorname {Loss}\ge2(24310)-2(36)=48548>7401.
\]

Thus the 5,372 defects are deadline particles in the general model, but the
current connected chronology cannot absorb them: its factor edges must be
rethreaded or reselected.

There is a sharper symmetry conclusion.  In the connected
\(\mathbb Z_{17}\)-equivariant class, one short-run orbit is already fatal
to every optimal variable staircase.  Hence genuine nonflat absorption
requires breaking physical orbit tying and clustering the short runs near
the two ends, unless all short-run orbits are eliminated.

## 1. Authenticated host and exact scope

The proof-safe input is the frozen replay package

```text
scratch/r2_k17_marker58_upper_q1_double_fusion_replay_20260802/
```

Its manifest passes all eighteen checks.  The two directly used artifacts
are

```text
7d39e3aee641521df2d441d0342a2bd060dafb05cc7f5703ef206f53b6d21e3c
  c68b.double_fusion.factor.tsv
6667e2e676a69ee2faf772dad2fd1a37a841fe0c0616aca43287517b843ec63c
  c68b.double_fusion.residence.cycle.tsv
```

The cycle has, literally:

* all 24,310 rank-nine owners in one Johnson cycle;
* every rank-eight intersection exactly once;
* all 19,448 rank-ten unions covered;
* 3,944 protected marker edges; and
* rank-ten repeat excess 4,862.

Its rank-ten load histogram is

```text
load 1: 16728   load 2: 1632   load 3: 102
load 4:   918   load 5:   68.
```

The previous residence audit tested only the flat supports
\([i,i+3]\).  Its 5,372-run and 11,640-row mismatch counts do not, by
themselves, test the variable schedule below.  Its compiler was correctly
skipped.  The new no-go in Section 5 tests every monotone three-particle
schedule, but still only for this fixed chronology.

## 2. Exact three-particle parametrization

Write the three omitted physical starts and deadlines as

\[
 x_t=G_t+t,
 \qquad y_t=H_t+t,
 \qquad t=0,1,2,
\tag{2.1}
\]

where

\[
 0\le G_0\le G_1\le G_2\le W,
 \qquad
 0\le H_0\le H_1\le H_2\le W.
\tag{2.2}
\]

Conversely, every pair of threshold triples in (2.2) gives two sets of
three distinct physical holes, so this is a bijective parametrization.
Put

\[
 g_i=|\{t:G_t\le i\}|,
 \qquad
 h_i=|\{t:H_t\le i\}|.
\tag{2.3}
\]

The selected first-rank-nine occurrence of owner \(T_i\) has support

\[
 I_i=[s_i,q_i]=[i+g_i,\ i+h_i]
\tag{2.4}
\]

and hence variable length

\[
                        |I_i|=1+h_i-g_i.
\tag{2.5}
\]

The supports are nonempty exactly when \(H_t\le G_t\) for all \(t\).
They are chain aligned exactly when

\[
 H_t\le G_t-\mathbf1_{\{0<G_t<W\}}.
\tag{2.6}
\]

The complete physical lower-cell atlas has size

\[
 3W+6-\operatorname {Loss}(G,H),
\]

where

\[
 \boxed{
 \operatorname {Loss}(G,H)=
 \sum_tH_t+\sum_t(W-G_t)+
 |\{(t,u):G_t<H_u\}|.}
\tag{2.7}
\]

Since \(3W+6-\Lambda=7401\), scalar feasibility is exactly

\[
                         \operatorname {Loss}(G,H)\le7401.
\tag{2.8}
\]

Every schedule satisfying (2.8) automatically obeys

\[
 H_2\le7401<16909\le G_0,
 \qquad G_1\ge20610,
 \qquad G_2\ge21843.
\tag{2.9}
\]

Indeed, put \(\delta_t=W-G_t\).  The \(\delta_t\) are nonincreasing and
\(\sum H_t+\sum\delta_t\le7401\).  This gives (2.9).  In particular all
deadlines precede all starts, the crossing term in (2.7) vanishes, legality
and chain alignment are automatic, and

\[
             \operatorname {Loss}=\sum_tH_t+\sum_t\delta_t.
\tag{2.10}
\]

The owner-window profile has at most seven bands:

| owner indices | window length |
|---|---:|
| \([0,H_0)\) | 1 |
| \([H_0,H_1)\) | 2 |
| \([H_1,H_2)\) | 3 |
| \([H_2,G_0)\) | 4 |
| \([G_0,G_1)\) | 3 |
| \([G_1,G_2)\) | 2 |
| \([G_2,W)\) | 1 |

Empty bands are allowed.

## 3. Exact run corridors: defects become particles

For an internal positive coordinate run \([a,b]\), put
\(\ell=b-a+1\).  The safe physical corridor is

\[
                  [q_{a-1}+1,\ s_{b+1}-1].
\]

It is nonempty exactly when

\[
 \boxed{h_{a-1}-g_{b+1}\le\ell-1.}
\tag{3.1}
\]

The left side is the number of deadline particles activated before the run
and not discharged after it.  Runs touching either linear boundary are
automatic.

In the separated K17 regime (2.9), (3.1) has the explicit forms

\[
 \ell=3:
 \qquad a\le H_2\quad\text{or}\quad b+1\ge G_0,
\tag{3.2}
\]

and

\[
 \ell=2:
 \quad a\le H_1
 \quad\text{or}\quad
 (b+1\ge G_0\text{ and }a\le H_2)
 \quad\text{or}\quad
 b+1\ge G_1.
\tag{3.3}
\]

Thus a short run is not forbidden.  It may be assigned to an early deadline
band, a late discharge band, or a true boundary.  The obstruction is global:
only three ordered particles are available.

Every active envelope block contains at most four consecutive owners.  On a
rank-nine Johnson path their intersection has rank at least six.  Therefore
the maximal envelope is automatically nonempty once (3.1) holds.  Chain
alignment transfers every consecutive union of owners to a physical source
interval.  These facts establish middle replay and upper transfer, not the
lower common-cap compiler.

## 4. Exact no-singleton collapse

Pairwise distinct rank-eight edge colours exclude a singleton positive run:
if \(x\) is present only at \(T_i\), the two adjacent intersections both
equal \(T_i-\{x\}\).  Hence a lower-q1-rainbow chronology has no length-one
runs.

For such a chronology an optimal particle schedule may be normalized to

\[
 H=(0,A,C),
 \qquad
 G=(W-d_1,W-d_2,W),
 \qquad d_1\ge d_2\ge0.
\tag{4.1}
\]

Fix an orientation and cut.  For an internal run \([a,b]\), define

\[
 m_d(b)=
 \mathbf1_{\{d_1\ge W-b-1\}}+
 \mathbf1_{\{d_2\ge W-b-1\}}.
\tag{4.2}
\]

Set

\[
 \rho_2(d)=
 \max\bigl(\{a:\ell=2,\ m_d(b)=0\}\cup\{0\}\bigr),
\tag{4.3}
\]

and

\[
 \rho_3(d)=\max\Bigl(
 \{a:\ell=2,\ m_d(b)\le1\}
 \cup\{a:\ell=3,\ m_d(b)=0\}
 \cup\{0\}\Bigr).
\tag{4.4}
\]

The coordinatewise-minimal deadlines are

\[
                         A=\rho_2(d),\qquad C=\rho_3(d).
\tag{4.5}
\]

Consequently define the exact optimal-threshold row-OR/scalar gate of a
cyclic chronology by

\[
 \boxed{
 \Phi(T)=
 \min_{\substack{\text{orientation, cut}\\W\ge d_1\ge d_2\ge0}}
 \bigl(d_1+d_2+\rho_2(d)+\rho_3(d)\bigr).}
\tag{4.6}
\]

There is a monotone variable staircase of optimal length with enough lower
cells if and only if

\[
                              \Phi(T)\le7401.
\tag{4.7}
\]

The qualification “gate” is essential above threshold.  Formula (4.6)
omits the crossing indicator in the literal loss of an arbitrary expensive
schedule.  Every value at most 7,401 forces all deadline thresholds before
all discharged-start thresholds, so the crossing term is then zero and
(4.6)--(4.7) are exact.  No equality between \(\Phi(T)\) and the unrestricted
minimum literal loss is claimed when \(\Phi(T)>7401\).

For a passing minimizer, equations (4.1) and (4.5) give the schedule
explicitly.  Hence the current 2,873 length-two and 2,499 length-three rows
collapse to two maximum frontiers and a two-dimensional suffix optimization.
No run-by-run SAT variables are needed for a fixed chronology.

This reduction is exact.  In the general threshold theorem, absence of
length-one runs makes the first adjusted frontier zero, so the
coordinatewise-minimal first deadline is (H_0=0).  A third discharged
start particle can only change (m_d(b)=3) to (2).  Both a length-two and
a length-three run are already automatic at (m_d(b)=2), so moving that
third start threshold to (G_2=W) preserves every corridor and weakly
decreases loss.  The remaining minimal deadline thresholds are precisely
(4.3)--(4.5).  Conversely, substituting them into (3.1) verifies every run.

The cut still has resource semantics.  Removing the cyclic wrap edge removes
one adjacent rank-ten witness.  A cut whose cap has another provider is
q1-safe; otherwise that cap needs an explicit boundary/compiler witness.
The cut rank-eight facet is unique and must likewise be realized as a
physical boundary/top-port lower cell.

## 5. The two-gap obstruction and the fixed marker58 verdict

For a linear opening, let the starts of its internal length-two runs be
\(a_1\le\cdots\le a_m\).  Put

\[
 R_2(x)=\max\bigl(\{a_i:a_i+3\le x\}\cup\{0\}\bigr),
 \qquad
 G_2(T)=\max_{0\le x\le W}(x-R_2(x)).
\tag{5.1}
\]

Every row-exact arbitrary-start schedule satisfies

\[
 \boxed{\operatorname {Loss}\ge2W-2G_2(T).}
\tag{5.2}
\]

To see this, apply the length-two corridor first at \(G_0\) and then at
\(G_1\).  Before \(G_0\) no start particle has discharged, so the second
deadline is at least \(R_2(G_0)\).  Before \(G_1\) at most one has
discharged, so the third deadline is at least \(R_2(G_1)\).  Adding these
two deadline costs to \((W-G_0)+(W-G_1)\) gives (5.2).

At K17, (5.2) and the budget 7,401 require

\[
                         G_2(T)\ge20610.
\tag{5.3}
\]

The H100 O3 C++ replay of the frozen marker58 cycle gives, in each
orientation,

```text
cyclic length-2 runs          2873
cyclic length-3 runs          2499
D1 / D2 / D3 / D4        34 / 48 / 65 / 70
maximum boundary length-2        2
exact max G2 over all cuts       36
cuts attaining G2=36          24310
q1-safe cuts                   7582
```

Therefore

\[
 \boxed{\operatorname {Loss}\ge48548>7401}
\tag{5.4}
\]

for every cut and orientation.  Even the correlation-free displacement
bound \(G_2\le D_3+2=67\) gives loss at least 48,486 and already proves the
no-go.

For comparison, terminal omitted starts give best losses 48,562 forward
and 48,566 reverse.  These are diagnostics only; (5.4) is the theorem for
all arbitrary starts.

### Theorem 5.1 — fixed connected chronology nonflat no-go

The frozen marker58 connected owner cycle admits no row-exact monotone
three-particle schedule of length 24,313 with enough scalar lower cells.
This remains true after reversal and every cyclic opening.

The theorem does not obstruct a different connected rank-eight/rank-ten
factor, a non-equivariant rethread, a compiler outside the monotone
first-middle staircase class, or \(\nu(17)=24313\).

## 6. Equivariant rigidity of optimal deadline particles

The fixed-host result has a dimension-specific structural strengthening.

### Theorem 6.1 — connected equivariant staircase rigidity

Let \(T\) be a connected \(\mathbb Z_{17}\)-equivariant degree-two factor
on the physical rank-nine layer whose rank-eight edge colours are all
distinct.  Then the following are equivalent:

1. some opening and orientation of \(T\) passes the optimal K17
   three-particle row-OR/scalar gate;
2. every cyclic positive coordinate run has length at least four;
3. the flat depth-three schedule passes middle replay.

#### Proof

Distinct rank-eight colours exclude length-one runs.  Suppose a length-two
or length-three run remains.  The coordinate generator acts on the connected
physical cycle as a nontrivial order-seventeen rotation.  Its translated run
starts therefore occupy one coset of the 17 points spaced 1,430 positions
apart.

For any linear opening, the owner interval

\[
                         [7402,16905]
\tag{6.1}
\]

has length 9,504, so it contains a translated start from every such orbit.
Let \([a,b]\) be that run.  By (2.9), all three deadline particles are
active before it, while no start particle is discharged after it:

\[
 h_{a-1}=3,
 \qquad g_{b+1}=0.
\]

Indeed \(a>7401\), and for either \(\ell=2\) or \(3\),
\(b+1\le16908<G_0\).  Equation (3.1) fails.  This proves that 1 implies 2.

If every positive run has length at least four, the flat choice
\(H=(0,0,0)\), \(G=(W,W,W)\) has zero loss and satisfies every corridor.
This proves 2 implies both 1 and 3; the remaining implication is immediate.
\(\square\)

### Corollary 6.2

Within the connected equivariant marker58 quotient class, the 316 strong
cyclic short-run blocker clauses remain necessary even when the target is an
optimal variable staircase.  They are not merely flat-compiler clauses in
that scoped class.

This is not true without connected equivariance.  To use the deadline
particles rather than eliminate every short run, physical edge choices must
be untied across the 17 translates, or fragments must be braided
non-equivariantly so that their short runs cluster near the two ends.

## 7. A concrete clustered absorber theorem

The exact normal form also gives a positive target for a rethreaded cycle.
Choose

\[
 H=(0,A,C),
 \qquad
 G=(W-d_1,W-d_2,W),
 \qquad
 0\le A\le C,
 \quad d_1\ge d_2\ge0,
\tag{7.1}
\]

with

\[
                         A+C+d_1+d_2\le7401.
\tag{7.2}
\]

The owner-window lengths are

```text
2 on [0,A),  3 on [A,C),  4 on [C,W-d1),
3 on [W-d1,W-d2),  2 on [W-d2,W).
```

### Theorem 7.1 — two-ended deadline absorber

Let \(T\) be a linear rank-nine Johnson chronology with distinct adjacent
rank-eight intersections and no singleton positive runs.  Schedule (7.1)
is row-exact if and only if every internal short run satisfies

\[
 \ell=3:
 \qquad a\le C\quad\text{or}\quad b+1\ge W-d_1,
\tag{7.3}
\]

and

\[
 \ell=2:
 \quad a\le A
 \quad\text{or}\quad
 (b+1\ge W-d_1\text{ and }a\le C)
 \quad\text{or}\quad
 b+1\ge W-d_2.
\tag{7.4}
\]

Under (7.2)--(7.4), the schedule is legal and chain aligned, all maximal
envelopes are nonempty, and its lower atlas has at least 65,535 cells.
Every consecutive upper witness of \(T\) transfers to a physical interval.

#### Proof

The loss in (2.10) is exactly the left side of (7.2).  Equations
(7.3)--(7.4) are (3.2)--(3.3) for (7.1).  Nonempty envelopes and upper
transfer follow from the Johnson and chain-alignment observations after
(3.3).  \(\square\)

The useful symmetric specialization \(d_1=d_2=B\) has cost
\(A+C+2B\).  It asks that all length-two runs begin in the early
\(A\)-prefix or have endpoint boundary \(b+1\ge W-B\), and that all
length-three runs begin in the early \(C\)-prefix or satisfy the same
endpoint condition.  Thus a late run may start two or three positions before
\(W-B\), respectively.  This is the literal clustering target absent from
the current marker58 cycle.

## 8. Exact resource-preserving rethread master

The nonflat search should release the quotient orbit tie while keeping the
verified physical resource equations.

For each rank-eight facet \(F\), let \({\cal E}(F)\) be the 36 Johnson
edges between two of the nine rank-nine owners containing \(F\).  There are

\[
                         24310\cdot36=875160
\]

physical edge options.  For an option \(e\), write \(f(e)\) for its
rank-eight intersection, \(u(e)\) for its rank-ten union, and \(\partial e\)
for its two owners.  Choose \(x_e\in\{0,1\}\) subject to

\[
 \sum_{e:f(e)=F}x_e=1
       \qquad(F\in{[17]\choose8}),
\tag{8.1}
\]

\[
 \sum_{e:v\in\partial e}x_e=2
       \qquad(v\in{[17]\choose9}),
\tag{8.2}
\]

\[
 \sum_{e:u(e)=U}x_e\ge1
       \qquad(U\in{[17]\choose10}),
\tag{8.3}
\]

and \(x_e=1\) for every protected marker edge.  Connectivity is exactly the
subtour family

\[
 \sum_{e\in\delta(S)}x_e\ge2
       \qquad(\varnothing\ne S\subsetneq{[17]\choose9}).
\tag{8.4}
\]

Equations (8.1)--(8.4) select one physical Hamilton cycle retaining the
authenticated rank-eight, rank-nine, rank-ten, and protected resources.
Let \(T(x)\) be its cycle.  The exact nonflat residence/scalar master row is

\[
                              \boxed{\Phi(T(x))\le7401,}
\tag{8.5}
\]

where \(\Phi\) is (4.6).  A passing integer incumbent exports its explicit
cut and thresholds.  A failing incumbent can be rejected by its exact cycle
no-good; stronger particle-aware separators may use (3.2)--(3.3) or the
two-gap shore (5.2).  This gives a finite exact Benders model even before a
more efficient integrated encoding is chosen.

If the variables in (8.1)--(8.4) are tied in \(\mathbb Z_{17}\) orbits,
Theorem 6.1 collapses (8.5) back to strong cyclic residence.  Therefore a
genuinely nonflat attack must use physical variables, partial orbit release,
or a non-equivariant fragment braid.

## 9. Lower, upper, and compiler boundary

Passing (8.1)--(8.5) would prove only:

* all middle owners once;
* exact rank-eight edge resources as an abstract palette;
* all rank-ten owner-edge unions, subject to a q1-safe opening or a boundary
  replacement;
* protected-edge containment;
* exact variable-staircase middle replay;
* nonempty maximal envelopes; and
* enough scalar lower cells.

It would not prove the word.  The remaining proof-safe order is:

1. bind the cut rank-eight facet and any cut-unique rank-ten cap to literal
   boundary/top-port cells;
2. materialize the complete P/Q lower-cell atlas for the chosen thresholds;
3. build the occurrence-labelled target--cell graph, including all root,
   head, graphic, and protected-marker predicates;
4. find a matching saturating all 65,535 lower targets;
5. replay the simultaneous maximal common cap
   \[
     A_p=P_p\cap\bigcap_{(S,C):\ p\in C}S
   \]
   and require every letter, owner row, selected lower cell, and protected
   trace to remain exact; and
6. replay ranks 11--17 and finally run the literal universal-word verifier.

The present owner chronology has 1,972, 510, and 51 consecutive-union holes
at ranks 11, 12, and 13.  Nonflat source intervals may change that ledger,
but no inheritance is claimed; the upper replay remains mandatory.

## 10. Frozen lane-V audit

The finite audit is deterministic O3 C++ and was run on H100 CPU at

```text
/home/amodo/or15/work/v_k17_marker58_deadline_particles_20260802
```

The local proof package is

```text
scratch/v_k17_marker58_deadline_particles_20260802/
```

with manifest SHA-256

```text
572f2b245e10a1235c75a7d85208972794e741f48b9f4418b9f3fa1298e9d7ea
```

and entries

```text
0c85b7a1903c71eff20b0eea47c6f63d7fac4edd509875c582d5a644d0af99ef
  scratch/audit_v_k17_marker58_deadline_particles_20260802.cpp
b54ab366b43f892bac94b6b1972ddbfbee8c0407cebb7804914e43f3be23a8d8
  marker58.deadline.audit.json
57741e39226d1f62af1f0488f8515f58bb5f254c2cc6c1ceb136560bba66b726
  marker58.deadline.cuts.tsv
99c6d3525192ad0fee3f1846ef12dbb42d4206ed6b1090cd224f8ccea2254bcc
  marker58.deadline.runs.tsv
```

The source revalidates every owner, facet, cap, and outgoing cycle edge before
auditing runs.  It imports the protected-edge flags from the authenticated
cycle and verifies their total; it does not independently derive marker58
protection semantics.  The cut table contains both orientations and all
48,620 openings; reverse cut indices are orientation-local.  The executable
exhausts cuts and runs, while the universal schedule conclusion invokes the
proved two-gap bound (5.2).  The audit status is

```text
PASS_FIXED_CONNECTED_CHRONOLOGY_NONFLAT_NO_GO
```

No SAT/UNSAT claim is made for the rethread master (8.1)--(8.5).
