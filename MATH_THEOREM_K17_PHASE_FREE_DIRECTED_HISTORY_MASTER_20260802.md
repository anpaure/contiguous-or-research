# `k=17` phase-free directed-history residence master

Date: 2026-08-02  
Status: exact formulation and generated finite instance, independently
audited clause-for-clause in
`MATH_AUDIT_AD_K17_DIRECTED_HISTORY_MASTER_20260802.md`; exploratory SAT
solves active.  No SAT, UNSAT, connected-factor, source, deeper-upper,
compiler, or universal-word claim is made here.

## 1. Purpose

The current marker58 CEGAR loop repeatedly selects a quotient factor, finds
its cyclic positive coordinate runs of lengths two and three, and adds one
forced-segment blocker for every new run orbit.  That loop has produced major
constructive descent, but it discovers the residence language incrementally.

This note gives a compact eager formulation of the entire language.  It is the
odd-`k` analogue of the phase-free directed-history theorem previously used
for even two-rail carriers.

The frozen marker58 quotient has:

* `1430` rank-nine owner orbits;
* `232` protected fixed edge orbits;
* `35713` residual option variables;
* exact rank-eight facet ownership and rank-nine degree two in the base CNF;
* complete rank-ten cap coverage in the base CNF.

The new master orients the selected factor and remembers only the last three
inserted coordinate labels at every owner orbit.

## 2. Directed quotient options

Fix canonical representatives `S_u` of the rank-nine `Z_17` owner orbits.  A
physical option joins

\[
 A=\rho^gS_u,
 \qquad
 B=\rho^{g+\delta}S_v,
\]

where `A-B={a}` and `B-A={b}`.  In the canonical frame at `u`, its directed
record is

\[
 e=(u,v; a,b,\delta).
\]

The reverse record is obtained by aligning `B` to `S_v`; its voltage is
`-delta mod 17` and its deleted/inserted labels are recomputed in that frame.
Thus the map's physical endpoints determine both orientations without a
separate phase variable.

For every nonloop residual option `x_e`, introduce orientations
`y_e^+,y_e^-` and impose

\[
 y_e^++y_e^-=x_e.
\tag{2.1}
\]

Every protected edge receives two orientation variables with sum one.
Quotient self-loops are fixed to zero: a degree-two factor using one has that
owner as a separate loop component, so no connected quotient factor can use
it.

At every owner orbit require at least one selected incoming and at least one
selected outgoing orientation.  The base factor already has undirected
degree exactly two.  Therefore these two clauses imply exactly one incoming
and one outgoing edge; no additional cardinality network is needed.

The result is a directed cycle cover.  Quotient connectivity and nonzero
voltage remain exact outer CEGAR gates.

## 3. Three-step history theorem

For each owner orbit `u`, introduce

\[
 h_1(u),h_2(u),h_3(u)\in\mathbb Z_{17},
\]

where `h_j(u)` is the coordinate inserted `j` transitions before reaching
the physical occurrence of `u`, expressed in the canonical frame `S_u`.

On a selected directed option `e=(u,v;a,b,delta)`, impose

\[
\begin{aligned}
 a&\ne h_j(u) &&(1\le j\le3),\\
 h_1(v)&=b-\delta,\\
 h_j(v)&=h_{j-1}(u)-\delta &&(j=2,3),
\end{aligned}
\tag{3.1}
\]

with arithmetic modulo seventeen.

### Theorem 3.1 — exact positive-residence encoding

A directed quotient cycle cover satisfies (3.1) if and only if every cyclic
positive coordinate run in every physical lift has length at least four.

### Proof

Traverse a selected directed component.  The coordinate deleted on the
current transition has a positive run of length at most three exactly when
its most recent insertion occurred on one of the preceding three
transitions.  Transporting those insertion labels into the current canonical
frame gives `h_1,h_2,h_3`; the first line of (3.1) excludes precisely these
events.

Conversely, along any cycle whose positive runs have length at least four,
record the actual last three insertion labels in the current canonical
frame.  Voltage transport gives the last two lines of (3.1), and no current
deletion equals one of the three recorded labels.  These actual histories
therefore satisfy the system.

After one quotient revolution, a physical occurrence returns with every
absolute label and the current phase shifted by the same component voltage.
The canonical-frame history is consequently unchanged.  Hence one history
state per quotient owner is sufficient even for nonzero-voltage lifts.  QED.

For a connected `Z_17`-equivariant factor, strict cyclic residence is
equivalent to the existence of a depth-three-resident linear opening: any
short run would have seventeen disjoint translates, which one opening cannot
simultaneously clip.

## 4. CNF size

Use a one-hot encoding for the three history values at every owner orbit.
The generated master has

```text
base variables                 204167
base clauses                   439463
directed arcs                   71874
history variables               72930
final variables                348971
added clauses                 3465094
final clauses                 3904557
```

The base is the independently audited round-one factor CNF.  Its two
component cuts and 316 incumbent blocker rows are redundant but sound on the
strict-residence face and provide propagation.

For each directed arc, the CNF has:

* one reified `h_1` insertion clause;
* three reified deletion-exclusion clauses;
* `2*17` reified history-transport clauses.

The complete generator is

```text
scratch/build_k17_marker58_directed_history_master_20260802.cpp
```

and the generated H100 root is

```text
/home/amodo/or15/work/root_k17_directed_history_master_20260802
```

## 5. Deterministic negative control

The same generator was run over the no-cut base CNF.  The authenticated
`3502`-short-run factor was then fixed by all `35713` primary-unit clauses.
Kissat returned `UNSATISFIABLE` during preprocessing in `0.45` seconds with
zero decisions and zero conflicts.  This statistic does **not** establish a
raw unit-propagation refutation; the independent decoder instead checks the
two coherent orientations semantically.

This is the expected control: the fixed quotient factor is connected and
therefore has an orientation, but its positive coordinate trace is not
resident.  The control does not prove completeness of the implementation;
an independent rotation/history audit is still required before promoting a
solver verdict.

The primary-fixing utility is

```text
scratch/fix_k17_primary_selection_units_20260802.cpp
```

Frozen hashes at generation time are

```text
82a20aeec38a0ebce6467c2558a1b604a32fbed26b2818d7d2575a82af75dc4a
  scratch/build_k17_marker58_directed_history_master_20260802.cpp
3756b3e7ad72b8e2f1186b6bfef02a2df002697915cbd3f77f9997ebcca57ab1
  scratch/fix_k17_primary_selection_units_20260802.cpp
c7bd1ac496a7f6303a334aafd1531ec086faa2fd97a30cd82686bbb1fb7050b6
  marker58_directed_history.cnf
4e9094251ee930a1f4de2cb8dac26a6c230ce8a288f7186c09cbc135d5bab94b
  marker58_directed_history_nocut.cnf
077b8d803cdada42a376387244764b9f77dea5cb5a336668738ebd617f95028d
  marker58_directed_history_floor3502_fixed.cnf
a5f7031fa872c814104581c5ff6cf3f896149b248e49bba1088c3b4de5701283
floor3502_fixed_kissat.control.out
```

The independent implementation reconstructed all `71,874` directed arcs,
all seventeen physical developments of each arc, and all `3,904,557` clauses
in order.  Its audit JSON has SHA-256
`058ea27da915f591b7214256d7b1e4ca22a21b8c94a36eb7a125b3f0b8f74970`.

## 6. Exact scope after a SAT model

A SAT assignment of the current master would prove only that its directed
cycle cover satisfies all base resources and strict positive residence.  It
must still be decoded fail-closed and subjected to:

1. quotient connectivity cuts;
2. nonzero component voltage;
3. literal physical residence replay;
4. arbitrary upper ranks eleven through seventeen;
5. source-letter/nonempty-envelope construction;
6. the strict-lower compiler and exhaustive universal-word verifier.

Thus the master removes open-ended residence-clause discovery.  It does not
collapse the later upper/source/compiler gates or prove `nu(17)=24313`.
