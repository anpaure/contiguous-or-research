# `k=17`: directed-history rank-11/rank-12 upper witness automata and order-free CEGAR

Date: 2026-08-02  
Status: exact theorem/model interface.  No SAT/UNSAT claim and no new solve.

## 0. Outcome

On the protected `Z_17` quotient face, the directed-history master already
selects an oriented degree-two factor and eagerly excludes positive owner
runs of lengths one, two and three.  Connectivity and nonzero voltage remain
separate exact gates.

The smallest sound rank-11/rank-12 upper integration need not choose 24,310
absolute cycle positions:

1. every rank-11 target has a three-owner witness if it has any witness;
2. every rank-12 target has a first-hit witness of between four and 56
   owners;
3. for each target orbit a finite voltage-labelled reachability automaton
   recognizes exactly those witnesses from the selected quotient darts; and
4. an uncovered target yields one positive reachability-frontier clause in
   the dart variables.  The clause remains valid for every future quotient
   order and therefore does not freeze the incumbent cycle.

The resulting CEGAR loop can accept a residence-clean SAT incumbent only
after literal topology, voltage, physical residence and upper-deck replay.
It proves the cyclic rank-11/rank-12 owner-interval deck.  A physical opening,
exterior seam windows, a literal lower source, lower/common-cap matching and
the terminal compiler are not proved here.

## 1. Authenticated rebase

The directed-history builder and generated snapshot are

```text
82a20aeec38a0ebce6467c2558a1b604a32fbed26b2818d7d2575a82af75dc4a
  scratch/build_k17_marker58_directed_history_master_20260802.cpp
c7bd1ac496a7f6303a334aafd1531ec086faa2fd97a30cd82686bbb1fb7050b6
  marker58_directed_history.cnf
7827cb0c8b7925d5fca73f37d0cd6cbc8567eff51f6609ecca8b6681bf29a7fb
  marker58_directed_history.map.tsv
```

The CNF has 348,971 variables and 3,904,557 clauses.  Its 71,874 dart
variables orient all nonloop quotient options, and its 72,930 one-hot
history variables implement

\[
 h_0(v)=\chi_a-\delta_a,
 \qquad h_j(v)=h_{j-1}(u)-\delta_a\quad(j=1,2)             \tag{1.1}
\]

on a selected dart `a:u->v`.  The authenticated audit proves that (1.1)
forbids exactly insertion-to-next-deletion distances one, two and three on
the final connected nonzero-voltage face.  It does not impose a symmetric
gap.

The new descent calibration is bound to the final model, not its earlier or
later siblings:

```text
9aa9c8137b4b90508aa255536a6f683bfa448b60de497b498f7119e432eb24ec
  after_c10c12_2414_single/round003.model
eba52226952cda38d74e98fc7463f54640b0b59736ff88fc2949c8f0c02de1eb
  after_c10c12_2414_single/final2397.factor.tsv
```

It has one quotient component of voltage 13 modulo 17, hence one physical
cycle, all 24,310 rank-eight colours and rank-nine owners, all 19,448
rank-ten caps and all 3,944 protected edges.  Its positive short-run census
is

\[
                    1292+1105=2397=141\cdot17.            \tag{1.2}
\]

Thus it is not a history-master solution.  It is only the current descent
calibration.  Its cyclic upper holes are

\[
              (H_{11},H_{12},H_{13})=(1938,408,0),        \tag{1.3}
\]

or 114 missing rank-11 target orbits and 24 missing rank-12 target orbits;
ranks 13--17 are complete.  Its score in the frozen 504-row residence bank
is 127, while its true current motif count is 141.  No novel-row count is
inferred from that difference.  The bank SHA-256 is
`aa9cac6b3bac8bacfbfae90d5faabf462e6e4d6f1dc9ded9a65bdefc1205ee16`;
its independent manifest has SHA-256
`1fde2b6de8606a2a3e6820e56723d496e3d16f837111f76c0a283271faf1de92`
and passes.

## 2. Voltage-labelled path semantics

Let `rho` rotate coordinates modulo 17.  A quotient owner vertex `v` carries
a fixed rank-nine representative `R_v`.  A selected directed dart
`a:u->v` of voltage `delta_a` has the literal lift

\[
       (u,g)\longrightarrow(v,g+\delta_a),
 \qquad \rho^gR_u\longrightarrow\rho^{g+\delta_a}R_v.     \tag{2.1}
\]

For a directed quotient path

\[
 P=(v_0,a_0,v_1,\ldots,a_{m-2},v_{m-1}),
 \qquad \sigma_i=\sum_{j<i}\delta_{a_j}\pmod {17},       \tag{2.2}
\]

define its phase-zero owner union

\[
                 U(P)=\bigcup_{i=0}^{m-1}\rho^{\sigma_i}R_{v_i}. \tag{2.3}
\]

Starting at phase `g` rotates (2.3) to `rho^g U(P)`.  Therefore a selected
path whose union has canonical representative `Z` supplies every one of the
17 physical targets in the orbit of `Z`.  Conversely, rotating any physical
interval witness to its canonical target gives a path of the form (2.2).
Every proper nonempty target has orbit size 17 because 17 is prime.

There are consequently

\[
 {1\over17}{17\choose11}=728,
 \qquad {1\over17}{17\choose12}=364                     \tag{2.4}
\]

target orbits to certify.

## 3. Exact locality of upper witnesses

### Theorem 3.1 — first-hit bound

Let `Z` have rank `r` in a simple physical owner cycle.  If some cyclic
owner interval has union `Z`, then `Z` has a first-hit subinterval of owner
width `m` satisfying

\[
                  r-8\le m\le {r-1\choose9}+1.            \tag{3.1}
\]

#### Proof

Choose an inclusion-minimal witness and orient it from its first owner to
its last.  Each Johnson transition can introduce at most one new coordinate,
so starting from rank nine needs at least `r-9` transitions.  This proves the
lower bound.

Minimality says that the last owner introduces a coordinate not present in
the preceding prefix.  It introduces only one, so the union of that prefix
is one fixed `(r-1)`-set.  Every prefix owner is a distinct rank-nine subset
of that set.  There are at most `binom(r-1,9)` such owners, and adding the
last owner proves the upper bound.  `square`

### Corollary 3.2 — rank eleven is exactly local

Every covered rank-11 target has a witness of exactly three consecutive
owners.

#### Proof

The last owner in a first-hit witness adds the eleventh coordinate.  The two
owners immediately before it are distinct adjacent rank-nine subsets of the
same rank-ten prefix union.  Their union is therefore that whole rank-ten
set; adjoining the last owner gives the target.  Two owners cannot have
rank-eleven union.  `square`

### Corollary 3.3 — complete rank-twelve width range

It is necessary and sufficient to consider rank-12 owner widths

\[
                           4\le m\le56.                   \tag{3.2}
\]

The upper bound is `binom(11,9)+1=56`.  Hence neither a four-owner-only
encoding nor a scan out to all 24,310 positions is exact.  Since `56<1430`,
a witness may cross the arbitrary quotient root but cannot complete one
quotient lap.  No absolute quotient position is required.

## 4. Complete static provider formulation

For a target representative `Z`, let `P(Z)` be the complete family of
first-hit directed catalogue paths described above: two darts for rank 11,
and three through 55 darts for rank 12.  For each path use an exact
availability bit

\[
                 z_{Z,P}=\bigwedge_{a\in P}y_a            \tag{4.1}
\]

with the standard linearization

\[
 z_{Z,P}\le y_a\quad(a\in P),
 \qquad
 z_{Z,P}\ge1-|P|+\sum_{a\in P}y_a.                       \tag{4.2}
\]

Hard coverage is

\[
                         \sum_{P\in P(Z)}z_{Z,P}\ge1.     \tag{4.3}
\]

Equations (4.1)--(4.3) are exact because directed indegree and outdegree are
one: all selected darts of `P` are literal consecutive owner transitions.
For an exported hole bit, define the OR of all `z_(Z,P)` exactly and take its
Boolean complement.  A mere covering inequality gives an exact hole census
only under minimization.

This formulation is proof-safe only when `P(Z)` is complete.  An incomplete
provider catalogue may prove SAT after literal replay, but its UNSAT result
is scoped to the omitted columns.  For binary coverage, columns with the
same target and identical Boolean support may be merged.  Do not merge
across targets or when occurrence multiplicity, a width inventory or
provider capacity is part of the gate.

## 5. Compact target automata

The complete path columns need not be materialized.  Fix a physical target
representative `Z`.  Every physical rank-nine owner `S subset Z` has a unique
quotient representative and fibre.  A catalogue dart at that fibre gives a
physical transition

\[
                    S\longrightarrow S'                  \tag{5.1}
\]

labelled by its quotient dart variable `y_a`.  Retain (5.1) only when
`S' subset Z`.

### Rank eleven

Use a source, the 55 layer-zero owners `S subset Z`, the 110 layer-one states
`(S,U)` with `|U|=10` and `S subset U subset Z`, and a sink.  A first dart
maps `S_0` to `(S_1,S_0 union S_1)`; a second dart reaches the sink exactly
when `U union S_2=Z`.  This 167-node labelled DAG recognizes exactly the
three-owner witnesses of Corollary 3.2.

### Rank twelve

Use a source, a sink and transient states

\[
 {\cal Q}_Z=\{(S,U): |S|=9,\ S\subseteq U\subsetneq Z,
                         \ |U|\in\{9,10,11\}\}.           \tag{5.2}
\]

There are

\[
 {12\choose9}+{12\choose10}{10\choose9}
       +{12\choose11}{11\choose9}=220+660+660=1540       \tag{5.3}
\]

transient states.  The source enters every `(S,S)`.  A physical catalogue
transition `S->S'` maps `(S,U)` to `(S',U union S')` while that union is
proper, and to the sink when the union is `Z`.  Each such automaton edge is
gated by the corresponding `y_a`.

### Theorem 5.1 — automaton equivalence

For integral dart variables satisfying directed degree one, the sink of the
target automaton is reachable if and only if the selected physical factor
has a cyclic consecutive-owner witness for `Z`.

#### Proof

An open automaton path follows selected quotient darts at their forced
physical phases, so (2.1) makes its owner sequence literal and consecutive.
The accumulated state is exactly its owner union; reaching the sink gives
`Z`.

Conversely, take a first-hit witness.  Every owner lies in `Z`; its selected
darts and accumulated unions trace the automaton.  Corollaries 3.2--3.3 put
the whole witness in the stated automaton.  `square`

An exact static extended formulation sends one unit of continuous flow from
source to sink, conserves flow at transient states and imposes

\[
                         0\le f_e\le y_{\ell(e)}           \tag{5.4}
\]

on every gated automaton edge of quotient label `ell(e)`.  Flow
decomposition shows that (5.4) is exact for binary `y`, even though the
rank-12 automaton may contain cycles.  The fully static construction would
have 121,576 rank-11 and 561,288 rank-12 automaton nodes before pruning.
The lazy separator below starts with none of them.

## 6. Order-free Benders frontier cuts

Let `y*` be an integral incumbent and, for an uncovered target `Z`, let `R`
be all target-automaton states reachable from the source using unconditional
edges and transitions whose label has `y*_a=1`.  The sink is not in `R`.
Define the deduplicated frontier label set

\[
 H_Z(R)=\{a:\text{some automaton edge labelled }a
                 \text{ leaves }R\}.                     \tag{6.1}
\]

Add the single clause

\[
                   \boxed{\ \bigvee_{a\in H_Z(R)}y_a\ }
 \qquad\text{or equivalently}\qquad
                   \sum_{a\in H_Z(R)}y_a\ge1.            \tag{6.2}
\]

### Theorem 6.1 — validity and separation

Clause (6.2) is valid for every factor covering `Z` and is violated by the
incumbent `y*`.

#### Proof

Every source-to-sink provider path begins in `R` and ends outside `R`, so it
uses some frontier transition.  The label of that transition must be
selected, proving (6.2).  If any frontier label were selected by `y*`, its
head would be reachable and belong to `R`.  Hence every literal in (6.2) is
false at `y*`.  `square`

Deduplicating repeated transition labels is Boolean-equivalent because one
selected quotient dart opens all of its physical lifts; it is stronger only
than a repeated-coefficient fractional relaxation.  If the frontier is
empty, the full frozen catalogue contains no provider for that target and
the empty clause is an exact scoped obstruction.  This is a positive
existence cut.  A residence-style negative clause breaking a guessed path is
unsound for a missing target, because no incumbent provider exists to break.

The cut uses no position, root, order or path variable.  A new solution may
choose any new dart on the frontier and may rethread the entire cycle.

## 7. Fail-closed CEGAR loop

Run the following loop without pinning the incumbent order.

1. Solve the immutable directed-history base plus all retained topology,
   voltage and upper frontier cuts.  Accept UNSAT only with a checked proof
   and a manifest covering every generated row.
2. Decode the complete primary and dart assignment.  Replay all fixed marker
   paths, facet exactness, owner degree, rank-ten caps and directed
   indegree/outdegree.
3. Separate every quotient component by the exact two-edge shore row.  Once
   one quotient cycle remains, compute its total voltage and reject voltage
   zero by an exact voltage constraint or full assignment no-good.
4. Develop the 24,310-owner lift.  Replay the history equations and directly
   require zero positive runs of lengths one, two and three.  Any disagreement
   with the eager history CNF is a verifier failure, not a heuristic cut.
5. Scan every cyclic triple for rank 11.  For rank 12, start at every owner,
   accumulate widths four through 56, and stop once the union rank exceeds
   twelve.  Canonicalize the unions and compare against all 728 and 364
   target orbits.
6. For every missing rank-11/rank-12 orbit, build its complete automaton from
   the immutable dart map, compute `R` under the incumbent and append (6.2).
   Store the target, reachable-state digest, sorted frontier literals and
   input hashes.
7. Recompute ranks 13--17 as well.  They are complete in `final2397` but that
   fact is not hereditary under rethreading.  Until their own complete
   provider separator is installed, any regression is safely rejected by
   the orientation-free factor no-good

   \[
                    \sum_{e\in X^*}(1-x_e)\ge1,           \tag{7.1}
   \]

   where `X*` is the incumbent's 1,198 selected residual primaries.  Facet
   exactness makes (7.1) exclude exactly that undirected factor; reversal has
   the same cyclic interval deck.
8. Re-solve.  Stop with a positive certificate only when no resource,
   component, voltage, residence or rank-11--17 upper separator fires.

The loop is finite: every rejected integral assignment violates a newly
retained valid clause or no-good.  A positive result is accepted only by
literal replay.  A proof-checked UNSAT result is exact for the frozen
protected quotient catalogue and accumulated complete cuts; it is not a
global impossibility theorem outside that catalogue.

The acceptance bundle exports the selected primaries and darts, quotient
cycle, voltage, physical owner cycle, history replay, one literal witness
path for every rank-11/rank-12 target orbit, and the complete cut manifest.
It records the final order for audit but never freezes a previous order in
the master.

## 8. Source and compiler scope

The theorem proves cyclic owner-interval coverage at some width.  It does
not assert a width-by-width multiplicity inventory.  A future literal
depth-three antecedent can transport long strict-upper source intervals only
after its physical opening and the three boundary collars are fixed and
verified.  A cyclic witness crossing that future seam is not automatically
a nonwrapping linear witness.

Accordingly this theorem does not claim:

* an upper-safe physical opening or exterior cross-window deck;
* a literal lower source, lower/root/head correlation or common-cap matching;
* a terminal compiler matching or regeneration; or
* a contiguous-OR word.

Those gates must be conditioned on the finally exported chronology and
physical seam.  The quotient voltage gauge is not that seam.
