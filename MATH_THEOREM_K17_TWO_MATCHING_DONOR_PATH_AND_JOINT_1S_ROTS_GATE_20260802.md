# K17 two-matching donor-path normal form and the joint `1S-ROTS` gate

**Date:** 2026-08-02  
**Status:** exact static equivalence, independently replayed round-47 fixture,
and an exact fixed-table `1S-ROTS` no-go.  The unrestricted joint master has
not been solved.  No residence, upper-shadow, source, connectivity,
common-cap, compiler, or word claim is made.

## 1. Base rows and the two assignment shores

In the authenticated original K17 table let

* `F` be the 1,748 singleton rows `(R_f)`;
* `H` be the 18,646 eligible hard donors
  `(B_u,M_u,R_u)`, with `rank(B_u)>1`;
* the other rows, including the 17 soft long rows, remain fixed.

Every `B_u` is a different named target.  Define two kinds of assignment:

\[
x_{u f}:B_u\longmapsto f
   \quad\Longleftrightarrow\quad B_u\subsetneq R_f,
\]

and

\[
p_{u v}:B_u\longmapsto v
   \quad\Longleftrightarrow\quad B_u\subsetneq M_v.
\]

The diagonal `p_{u u}` is the unchanged-donor assignment.  The exact rows are

\[
 \sum_f x_{u f}+\sum_v p_{u v}=1                     \tag{1.1}
\]

for every source bottom `u`,

\[
 \sum_u x_{u f}=1                                    \tag{1.2}
\]

for every singleton host `f`, and

\[
 s_v+\sum_u p_{u v}=1                                \tag{1.3}
\]

for every donor host `v`.  Here `s_v=1` means that donor row `v` is
shortened and receives no replacement bottom.  Thus `x` chooses the terminal
donor set `D`, `s` chooses the shortened set `S`, and `p` is the matching

\[
                 p:H\setminus D\longrightarrow H\setminus S. \tag{1.4}
\]

The cardinality `|S|=|F|=1,748` follows from (1.1)--(1.3), so it need not be
imposed separately.

Equivalently, add 1,748 distinguishable dummy bottom tokens.  On the left
put the 18,646 real bottoms and these dummies; on the right put the 18,646
donor hosts and 1,748 singleton hosts.  Real-bottom edges are exactly the
`p` and `x` edges above, while every dummy is adjacent to every donor host.
A perfect matching in this augmented bipartite graph is precisely a solution
of (1.1)--(1.3); quotienting the symmetric dummy labels replaces their
32,593,208 explicit edges by the 18,646 short-slot variables `s_v`.

Thus the **static** extended formulation is an ordinary bipartite perfect
matching polytope and is totally unimodular.  This TU statement ends before
address flags, five-cell socket configurations, chronological degrees, and
pulled-back Benders cuts; their common stack is not asserted to be TU.

## 2. Exact materialization theorem

### Theorem 2.1

Every integral solution of (1.1)--(1.3) materializes an exact lower-target
partition by

\[
 f\gets(B_u,R_f)\quad\text{when }x_{u f}=1,
\]

\[
 v\gets(B_u,M_v,R_v)\quad\text{when }p_{u v}=1,
\]

and

\[
 v\gets(M_v,R_v)\quad\text{when }s_v=1.
\]

The length histogram is exactly `(0,7395,16915)`, all original targets of
rank at most eight occur once, all owner/root labels are unchanged, and the
17 soft long rows are untouched.

Conversely, every table obtained by redistributing only the `B_u` targets
among compatible donor and singleton hosts, with one-copy target use and the
same optimal histogram, induces a unique integral solution of
(1.1)--(1.3).

### Proof

Equation (1.1) assigns each old bottom target exactly once.  Equations (1.2)
and (1.3) give capacity one at every possible host.  The arc definitions are
precisely the strict-containment conditions needed for the displayed chains.
All `M_v`, `R_v`, and all fixed-row targets stay at their original hosts.
Therefore no target is lost or duplicated.

Summing (1.1) and subtracting the filled donor-host count in (1.3) gives
`sum_v s_v=|F|=1,748`.  Hence the length-two rows are the 3,899 old
length-two rows, 1,748 extended singleton rows, and 1,748 shortened donors:
`3899+1748+1748=7395`.  The hard donors left long number
`18646-1748=16898`; adding the 17 soft rows gives 16,915.

For the converse, locate the unique final host of every named `B_u`.
One-copy use gives (1.1); host capacity gives (1.2)--(1.3); chain strictness
gives the allowed-edge conditions.  The host determines `x`, `p`, or `s`
uniquely.  QED.

## 3. Path interpretation and cycles

Orient every selected nonself assignment from its source donor to its host.
Each donor has one outgoing assignment when its diagonal self assignment is
included, each singleton is a sink, and each donor host has capacity one.
After suppressing self assignments, every component is either

* a donor path ending at one singleton, or
* a directed donor cycle.

Cycles are valid for the **simultaneous static** theorem: they merely permute
bottom targets around compatible donor hosts.  They need not be reachable by
an acyclic sequence of ordinary/relay moves.  A sequential-relay provenance
subclass must add lazy directed-cycle cuts (self assignments are not cut).
No static target argument may silently impose that stronger subclass.

This explains the failure of independent atomic relay columns.  A row may be
`A` in one elementary relay and later `D` in another; in the final table it is
simply an internal path vertex.  Resource-disjoint atomic `R(H,A,D,F)`
columns exclude such paths incorrectly.

## 4. Exact round-47 reconstruction

Against original table SHA
`db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185`,
the authenticated round-47 table SHA
`95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735`
replays as

```text
selected terminal x edges       1,748
selected p edges               16,898
selected short slots s          1,748
nontrivial internal p edges         48
self p assignments             16,850
donor paths                     1,748
path lengths                  1^1701 2^46 3^1
nontrivial donor cycles             0
maximum path length                 3
row 520                    internal path vertex
```

Thus the previously observed cross-role use of row 520 is legal in the
two-matching master and is not representable by a family of pairwise
resource-disjoint atomic relays.

The complete K17 catalogues contain

```text
x terminal variables              401,754
p donor-host variables           2,129,483
explicit symmetric dummy edges  32,593,208
explicit augmented graph edges  35,124,445
short-slot variables                18,646
primary variables                2,549,883
exact-one rows                       39,040
exact-one incidences              5,081,120
Sinz auxiliaries                  5,042,080
CNF variables                     7,591,963
CNF clauses                      15,126,240
```

The `emit0` H100 size/replay run used one CPU for 0.87 seconds and peaked at
199,936 KiB RSS under the 8-GiB cap.  A full-CNF solver run under 8 GiB has
not yet been attempted, so this builder measurement is not a solver-memory
guarantee.

## 5. Exact interface to the joint address/reset child

The two-matching solution is the outer configuration.  Materialization fixes
all chain rows, including substituted long bottoms, before the child oracle
constructs:

1. one four-state address for every long role;
2. one nine-state launch-spec address for every length-two role;
3. every exact long--long state arc;
4. every exact five-cell common-state long--short--long hyperarc with
   `beta<=alpha`;
5. one incoming/outgoing contracted arc per long and one hyperarc per short.

This logic-based Benders decomposition is finite and exact.  A child UNSAT
always permits the full-table blocking clause formed by negating the 18,646
selected source-bottom assignments (one selected `x` or `p` per `u`).
Because (1.1) is exact-one, that clause excludes exactly that materialized
table, not its strict supersets.  A smaller pulled-back Hall/core cut is valid
only after replay proves that changing assignments outside its declared halo
cannot alter the child core.

Configuration-conditioned address catalogues are load-bearing: an internal
path vertex has bottom `B_u` rather than its original `B_v`.  Reusing a
fixed-original long-state catalogue there is unsound.

## 6. Fixed round-47 `1S` verdict

The exact relaxed-nine child census on the round-47 table gives

```text
flag-labelled long--long arcs       42,490
exact common-state socket triples    2,188
short roles with zero socket         5,969 / 7,395
long roles with zero incoming        2,468
long roles with zero outgoing        1,133
total empty exact-one rows            9,570
```

The emitted CNF has `348,687` variables and `617,660` clauses.  Kissat reports
UNSAT without search in 0.03 seconds and 8 MB; `drat-trim` reports
`trivial UNSAT` and `s VERIFIED`.  This closes only the fixed round-47 table,
even under the optimistic nine-state short relaxation.  It is not a global
ROTS no-go.

## 7. Artifacts

```text
scratch/k_rots_k17_joint_1s_20260802/
```

Principal hashes:

```text
build_k17_two_matching_outer_master_20260802.cpp
f2cf43c7e44d16e15ee6449587bc2e4a1c0cc8a37f6351c5726e8ce4e0867324

audit_k17_round47_donor_path_normal_form_20260802.cpp
81783bfdb08dcf473450de160a2e12821535769de40c97bbfcce36f4b3c1a933

size.audit.json
f1600a3e65fa3597f60affc919bea79e8e2bfe8cdd52bd850f21a0658f841cad

round47_two_matching.selection.tsv
d56126ff3d1d8fde67dd6a6446c0974ded36921993fd093edc94a279c0e5a5b9

round47_path.audit.json
f69af021871ca5e26c415cbad4d5ea12cb89844da914f3fcab91f0cf88ca405a

round47_path.audit.json.arcs.tsv
d3785dccb20d9ea60d696c508ffd82efcda0e0ad1733b4109e68e95ba06894f2

resource_run.err
48b5614782f55559548e057638dc38a5b7832af359efe8dbcc6c9ce7aa21c8f7

frozen_relaxed9/fixed_1s.cnf
a7ff4da4d83a8346354960bf2f5c3efa04f3d3023518f4377106dced80fe0b88

frozen_relaxed9/fixed_1s.ascii.drat
009aadf1eeb782d537099de4e10bb935b0f8809772782f5969b875594ac90242

frozen_relaxed9/short_reset_triples.tsv
381a29b7d83dec652ac0da7bf63f7ae9b5bdb515ab325ac66ffe2d1409ea1e97

frozen_relaxed9/independent_replay.audit.txt
0c4f20b0c50231b3ef2aa7218b724db8665886a459fd4bfd39ce72a92894ce94
```

The exact remaining row is now cleanly stated: select `x,p,s`, chain
allocation, literal addresses, and typed reset hyperarcs jointly, or derive a
dependency-certified Benders cut.  The perfect union hard-head projection of
round 47 is only a warm-start statistic and does not weaken its fixed-table
socket no-go.
