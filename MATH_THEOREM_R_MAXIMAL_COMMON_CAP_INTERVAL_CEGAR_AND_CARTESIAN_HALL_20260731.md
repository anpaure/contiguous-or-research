# Maximal common caps, bounded interval-conflict CEGAR, and Cartesian Hall

## 0. Purpose

This note extracts the reusable theorem behind the genuine-four-filter K16
compiler audit.  The theorem is independent of K16, PBBS, and the particular
Pascal lift.  It separates three logically different objects:

1. ordinary target-to-interval Hall matching;
2. simultaneous erosion by overlapping exact-OR caps;
3. a guard-pruned Cartesian regime in which ordinary Hall becomes
   sufficient again.

The K16 chronology with SHA `c7beccc3...` appears only in Section 6 as an
exact calibration.  No finite carrier search or SAT computation is part of
the theorem.

## 1. General interval compiler system

Let (P={0,ldots,n-1}) be physical source positions and let
([k]={1,ldots,k}) be coordinates.  We are given:

* prescribed row labels (T_i\subseteq[k]);
* row intervals (I_i\subseteq P), each a nonempty integer interval;
* a family ({\cal C}) of physical witness intervals;
* a target family ({\cal L}\subseteq2^{[k]}\setminus\{\varnothing\}).

Define the maximal row envelope

\[
E_p=\bigcap_{i:p\in I_i}T_i.                            \tag{1.1}
\]

Assume

\[
E_p\ne\varnothing,
\qquad
\bigcup_{p\in I_i}E_p=T_i.                              \tag{1.2}
\]

A literal source is a sequence of nonempty sets (A_p\subseteq E_p).
It preserves the rows when

\[
\bigcup_{p\in I_i}A_p=T_i                               \tag{1.3}
\]

for all (i).  A target (S\in{\cal L}) is realized at (C\in{\cal C})
when

\[
\bigcup_{p\in C}A_p=S.                                  \tag{1.4}
\]

Let (G\subseteq{\cal L}\times{\cal C}) be any sound individual-candidate
graph: every edge ((S,C)) is individually realizable while preserving
(1.3).  In the depth-(d) compiler, the usual maximal-envelope individual
pin criterion produces exactly this graph.

## 2. Fixed-matching maximal-core theorem

Let (M\subseteq G) match every target to a distinct cell.  Put

\[
K_p(M)=E_p\cap\bigcap_{(S,C)\in M:p\in C}S.              \tag{2.1}
\]

### Theorem 2.1 (maximal common-cap criterion)

The matching (M) is realized by one literal source if and only if

\[
\begin{aligned}
K_p(M)&\ne\varnothing &&(p\in P),                        \tag{2.2}\\
\bigcup_{p\in I_i}K_p(M)&=T_i &&(i),                     \tag{2.3}\\
\bigcup_{p\in C}K_p(M)&=S &&((S,C)\in M).                \tag{2.4}
\end{aligned}
\]

When they hold, (A_p=K_p(M)) is a canonical literal realization.

#### Proof

Let (A) realize (M).  Equation (1.3) implies (A_p\subseteq T_i) for
every (i) with (p\in I_i), hence (A_p\subseteq E_p).  Equation (1.4)
implies (A_p\subseteq S) whenever (p\in C) and ((S,C)\in M).
Therefore (A_p\subseteq K_p(M)).  Nonemptiness of (A_p) gives (2.2).
The union of the (K_p)'s on a row or matched cell is contained in its
prescribed label and contains the corresponding union of the (A_p)'s, so
(2.3)--(2.4) follow.

Conversely, (A_p=K_p(M)) satisfies every requirement verbatim.  ∎

Thus common-cap verification of a fixed matching is deterministic; it does
not require a source-bit solver.

## 3. Coordinatewise interval-cover form

For coordinate (b\in[k]), define

\[
Z_b(M)=\bigcup\{C:(S,C)\in M,\ b\notin S\}.              \tag{3.1}
\]

Then

\[
b\in K_p(M)
\quad\Longleftrightarrow\quad
b\in E_p\text{ and }p\notin Z_b(M).                     \tag{3.2}
\]

Let

\[
H_{i,b}=\{p\in I_i:b\in E_p\},
\qquad
H_{C,b}=\{p\in C:b\in E_p\}.                           \tag{3.3}
\]

Theorem 2.1 is equivalent to

\[
\begin{aligned}
&\forall p\ \exists b\in E_p:\ p\notin Z_b,            \tag{3.4}\\
&H_{i,b}\not\subseteq Z_b
  &&(b\in T_i),                                          \tag{3.5}\\
&H_{C,b}\not\subseteq Z_b
  &&((S,C)\in M,\ b\in S).                              \tag{3.6}
\end{aligned}
\]

After (M) is fixed, the (k) coordinates are independent interval-cover
tests.  The hard coupling is solely that all (Z_b)'s arise from the same
matching.

## 4. Bounded conflict clutter and exact CEGAR

Write

\[
h=\max_i|I_i|,
\qquad
c=\max_{C\in{\cal C}}|C|,
\qquad
e=\max_p|E_p|.                                           \tag{4.1}
\]

### Theorem 4.1 (bounded no-good rank)

If a matching (M) fails Theorem 2.1, one can extract a valid matching-edge
no-good

\[
\sum_{f\in F}y_f\le |F|-1                               \tag{4.2}
\]

violated by (M), with

\[
|F|\le\max\{e,h,c+1\}.                                  \tag{4.3}
\]

More precisely:

* an empty-position violation has a certificate of rank at most (e);
* a lost row bit has a certificate of rank at most (h);
* a lost matched-pin bit has a certificate of rank at most (c+1).

#### Proof

If (K_p=\varnothing), then for each (b\in E_p) choose one selected edge
whose interval contains (p) and whose label omits (b).  These at most
(|E_p|) selections jointly force (K_p=\varnothing), so they cannot all
belong to a literal solution.

If row bit (b) is lost, then every (p\in H_{i,b}) is covered by a
selected (b)-opposing interval.  Choose one such selected edge per
position.  At most (|H_{i,b}|\le h) edges suffice.

If selected pin (f=(S,C)) loses (b\in S), include (f) and choose one
selected (b)-opposing edge for every (p\in H_{C,b}).  This uses at most
(1+|H_{C,b}|\le c+1) edges.  Each chosen family alone forces its displayed
violation, proving (4.2).  ∎

### Corollary 4.2 (protected-nonempty specialization)

Suppose every position has an immune coordinate (a_p\in E_p) such that no
remaining candidate interval containing (p) has a label omitting (a_p).
Then empty-position cuts never occur, and every common-cap cut has rank at
most

\[
\max\{h,c+1\}.                                           \tag{4.4}
\]

In the depth-three setting (h\le4,c\le3), all cuts have rank at most four.

### Exact CEGAR algorithm

Start with the ordinary bipartite matching master.  Given an integral
matching, compute (2.1).  If (2.2)--(2.4) hold, emit (A=K).  Otherwise add
the bounded no-good from Theorem 4.1.  The process is finite, sound, and
complete because there are finitely many matchings and each rejected
matching violates its new no-good.

This is a theorem about the integral matching master.  It does not assert
that the master augmented by all no-goods is totally unimodular.

## 5. Cartesian-guarded Hall sufficiency

The bounded-clutter theorem still permits correlated conflicts.  The next
definition gives a checkable regime in which those correlations disappear
and ordinary Hall alone is sufficient.

For an edge (e=(S,C)\in G) and (b\in S), an **edge guard** is a position

\[
g(e,b)\in H_{C,b}.                                       \tag{5.1}
\]

For a row bit (b\in T_i), a **row guard** is

\[
r(i,b)\in H_{i,b}.                                       \tag{5.2}
\]

A subgraph (G'\subseteq G) is **Cartesian guarded** if there exist:

1. a position guard coordinate (a_p\in E_p) for every (p);
2. row guards (r(i,b)) for every row bit;
3. edge guards (g(e,b)) for every (e\in G') and (b) in its target;

such that the following independent edge tests hold.

### Global-guard test

For every (f=(T,D)\in G'):

\[
\begin{aligned}
p\in D&\Longrightarrow a_p\in T,                        \tag{5.3}\\
r(i,b)\in D&\Longrightarrow b\in T.                     \tag{5.4}
\end{aligned}
\]

### Cartesian cross-edge test

For every two co-selectable edges

\[
e=(S,C),\qquad f=(T,D)                                   \tag{5.5}
\]

with distinct targets and distinct cells, and every (b\in S),

\[
g(e,b)\in D\Longrightarrow b\in T.                      \tag{5.6}
\]

The condition is ordered in (e,f); requiring it for all ordered pairs
includes the reverse protection automatically.

### Theorem 5.1 (Cartesian Hall theorem)

If (G') is Cartesian guarded and satisfies Hall's inequalities for the
whole target family, then the interval compiler has a literal realization.
Indeed, every matching of (G') saturating the target side is common-cap
realizable.

#### Proof

Hall supplies a matching (M\subseteq G').  Consider its maximal core.

For each position (p), every selected edge whose interval contains (p)
contains (a_p) by (5.3).  Hence (a_p\in K_p(M)), proving nonemptiness.

For a row bit (b\in T_i), every selected edge covering (r(i,b)) contains
(b) by (5.4).  Thus (b\in K_{r(i,b)}(M)), proving (2.3).

Let (e=(S,C)\in M) and (b\in S).  The owner edge contains (b).  Every
other selected edge is co-selectable with (e), so (5.6) says that any such
edge covering (g(e,b)) also contains (b).  Therefore
(b\in K_{g(e,b)}(M)), proving (2.4).  Theorem 2.1 now gives the literal
source.  ∎

The importance of Theorem 5.1 is quantifier separation.  One first chooses
guards and prunes to (G') using edgewise and pairwise Cartesian tests; the
remaining existence question is ordinary Hall.  No empirical compilation
claim and no independent-cap assumption is used.

The exact remaining positive lemma for a PBBS/Pascal induction can therefore
be stated cleanly:

> Construct a Cartesian-guarded candidate subgraph retaining Hall after all
> row, position, and edge guards are installed.

Failure of that lemma does not imply compiler infeasibility; it only means
that genuinely correlated rank-three or rank-four CEGAR cuts are necessary.

## 6. Genuine-four-filter K16 calibration

The solver-free audit

```text
scratch/audit_r_k16_true_fourfilter_commoncap_gate_20260731.py
scratch/k16_true_fourfilter_commoncap_gate_20260731.audit.json
```

gives the following exact calibration for target SHA `c7beccc3...` and
(X=\{12870,12871,12872\},Y=\{0,1,6388\}).

### Marginal Hall versus common cap

The graph has (26332) targets, (32230) physical cells, (347734)
incidences, and a perfect matching.  The deterministic matching has no empty
maximal-core cell but fails (1808) row equations and (5045) pin equations.
It contains the rank-two nested conflict

```text
0x0017 -> [7648,7648]
0x4027 -> [7648,7649],
```

because the first pin requires bit `0x0010` at position 7648 and the second
forbids it there.  This is a minimal counterexample to “perfect Hall plus
laminar physical intervals is automatically literal.”  It is not a global
no-go: each of the two targets has an unused one-edge augmenting exit.

### Safe unit closure

The singleton `0x8000` has the unique cell `[6389,6389]`.  After fixing it,
exact matching-unit propagation fixes (14060) targets.  Their common cap
leaves the capped maximal envelope unchanged and has zero row/pin failures.
The reduced problem has

```text
targets          12272
cells            18170
candidate edges 238472.
```

Every position has an immune coordinate.  Since middle carriers have length
at most four and pins length at most three, Corollary 4.2 gives rank-at-most-
four CEGAR cuts.

### Exact reduced Boolean interface

After constant and unit elimination, the direct (y/q) formulation has

```text
y variables                                      238472
q variables                                       46760
total Boolean variables                          285232

target exactly-one rows                           12272
cell at-most-one rows                              18170
killer binary implications                       561707
q reverse-definition rows                         46760
nonempty rows                                          0
middle-survival rows                               28940
conditional pin-recovery rows                    465611
direct semantic constraint groups              1,133,460
```

These figures calibrate the general theorem; they are no longer a K16
frontier claim.  The independently completed K16 construction does not alter
any theorem or counterexample above.

### Subsequent exact closure

The later direct common-cap model on the same endpoint-rerooted target order
and pinned schedule is SAT.  It produces `answers/k16.word`, length `12873`,
SHA-256
`890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe`.
Thus this frozen fibre now has an explicit compatible matching and maximal
common cap.  See
`MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md`.
This positive instance does not imply that Cartesian guards or the LLL
profile exist uniformly in other dimensions.

## 7. Audited boundary

Proved unconditionally:

* the fixed-matching maximal-core theorem;
* the coordinatewise interval-cover equivalence;
* bounded-rank conflict extraction and exact CEGAR;
* Cartesian-guarded Hall sufficiency.

Not proved:

* that an arbitrary perfect matching can be repaired by bounded exchanges;
* that a Cartesian-guarded Hall subgraph always exists in PBBS or Pascal
  chronologies;
* total unimodularity after adding common-cap conflicts.

Those are the exact implication boundaries.
