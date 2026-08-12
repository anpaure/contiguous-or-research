# K17 `1S-ROTS`: generalized relay outer columns and proof-safe Benders cuts

**Date:** 2026-08-02  
**Status:** **SUPERSEDED AS THE GLOBAL OUTER MASTER** by
`MATH_THEOREM_K17_TWO_MATCHING_DONOR_PATH_AND_JOINT_1S_ROTS_GATE_20260802.md`
(SHA-256
`b252f59b76e5ea613842d3633ecba8fb81f47477ae9b2fa1eee467cd9aff99a5`).
The atomic `O/R` construction below is only a strict subface.  Retained
load-bearing content is the independent donor-flow/coupled-matching replay,
the exact service/state boundary, and the signed-core/Benders cut scope.
Use the superseding note's `x,p,s` augmented-perfect-matching formulation
for global solves.

**Original scope:** exact static-column theorem and implemented audit
interface.  The frozen round-47 fixed-table relaxed-nine `1S` no-go is
recorded independently; no unrestricted joint-master verdict follows.  This
note makes no residence, upper-shadow, connected-topology, source,
common-cap, compiler, or word claim.

## 1. Atomic configurations

Work relative to the authenticated unrecoupled three-level table.  Write an
original singleton row as `F:(R_F)` and a hard long row as

\[
             D:(B_D,M_D,R_D).
\]

There are `1748` possible `F` rows, `18646` eligible hard rows, and exactly
`401754` containment pairs `B_D subsetneq R_F`.

An ordinary column is

\[
\begin{array}{rcl}
O(F,D):&F:(R_F)&\longmapsto (B_D,R_F),\\
      &D:(B_D,M_D,R_D)&\longmapsto(M_D,R_D).
\end{array}                                                    \tag{1.1}
\]

A generalized one-relay column is

\[
\begin{array}{rcl}
R(H,A,D,F):&F:(R_F)&\longmapsto(B_D,R_F),\\
            &A:(B_A,M_A,R_A)&\longmapsto(M_A,R_A),\\
            &D:(B_D,M_D,R_D)&\longmapsto(B_A,M_D,R_D),
\end{array}                                                    \tag{1.2}
\]

where `B_D subsetneq R_F` and `B_A subsetneq M_D`.  The label `H` records
the typed hard head served by the relay; it does not change the payload
identity (1.2).  A literal relay column is admitted only when at least one
of the three regenerated rows in (1.2) supplies `H` under the exact
complete-menu union projection.  This service test is a pricing condition,
not a common-state `1S` socket certificate.  A head-capacity-one row can be
imposed when the relay bank is required to be head-injective.

Let `z_c` be the selected-column bit.  The proof-safe atomic outer rows are

\[
 \sum_{c:F(c)=F}z_c=1\quad(F\in\mathcal F),                 \tag{1.3}
\]

and, for every original hard row `v`,

\[
 \sum_{c:D(c)=v}z_c+\sum_{c:R\text{ and }A(c)=v}z_c\le1.   \tag{1.4}
\]

Thus one physical row cannot be the `A` resource of one selected relay and
the `D` resource of another.  If head injection is requested, also impose

\[
                 \sum_{c:R,\ H(c)=H}z_c\le1.               \tag{1.5}
\]

### Theorem 1.1 (exact static equivalence)

Every selection satisfying (1.3)--(1.4), with every selected column passing
the literal tests above, materializes an exact target partition with chain
histogram

\[
                         (x_1,x_2,x_3)=(0,7395,16915).       \tag{1.6}
\]

Conversely, every table obtained from pairwise row-disjoint applications of
(1.1)--(1.2) has a unique selected atomic-column set satisfying
(1.3)--(1.4), apart from the non-payload service label `H`.

#### Proof

For (1.1), the old target multiset on `F,D` is

\[
       \{R_F,B_D,M_D,R_D\};
\]

the new multiset is the same.  For (1.2), the old and new multisets on
`F,A,D` are both

\[
 \{R_F,B_A,M_A,R_A,B_D,M_D,R_D\}.                           \tag{1.7}
\]

The strict-containment hypotheses make every new chain strict.  Equations
(1.3)--(1.4) make the affected row sets disjoint, so the local identities
can be summed.  Every column changes the length ledger by

\[
                         (\Delta x_1,\Delta x_2,\Delta x_3)=(-1,+2,-1).
\]

Applying exactly `1748` columns to the original
`(1748,3899,18663)` table gives (1.6).  No owner, root, or rank-one-bottom
soft row changes.  The converse follows by inspecting which original
singleton receives `B_D`, and, for a relay, which unique original bottom
`B_A` is moved to `D`.  Row disjointness prevents ambiguity.  \(\square\)

The implementation independently replays the complete rank-at-most-eight
target partition, not merely this scalar ledger.

### Theorem 1.2 (exact donor-path/cycle normal form)

The atomic face is not the full relay closure.  Let `V` be the `18646`
original hard donors.  Introduce an internal donor arc

\[
                          u\longrightarrow v
       \quad\Longleftrightarrow\quad B_u\subsetneq M_v              \tag{1.8}
\]

and a terminal arc

\[
                          v\longrightarrow F
       \quad\Longleftrightarrow\quad B_v\subsetneq R_F.             \tag{1.9}
\]

Choose arcs so that every donor has internal indegree at most one, total
outdegree at most one, and

\[
              \deg^+(v)\ge\deg^-_{V}(v),                            \tag{1.10}
\]

while every `F` has exactly one incoming terminal arc.  Then the selected
arcs are vertex-disjoint directed donor paths ending at the `1748` free
rows, together with optional directed donor cycles.

Materialize them by putting `B_u` at the head of each selected arc out of
`u`.  Thus:

* an untouched donor keeps `(B_v,M_v,R_v)`;
* a path source becomes `(M_v,R_v)`;
* an internal donor with predecessor `u` becomes `(B_u,M_v,R_v)`;
* a terminal `v->F` makes `F` equal `(B_v,R_F)`.

This is an exact target permutation and again yields (1.6).  Conversely,
every table obtained by arbitrary serial bottom relays has a unique such
arc set: locate each original `B_u`; its new row is precisely the head of
the unique outgoing arc of `u`, or `u` itself when no arc is selected.

#### Proof

Indegree and outdegree at most one give paths and cycles.  Condition (1.10)
forbids a donor sink, so every noncyclic component ends at an `F`.  The
`1748` terminal rows imply, after cancelling internal indegrees and
outdegrees,

\[
        |\{v:\deg^-(v)=0,\deg^+(v)=1\}|=1748.                       \tag{1.11}
\]

These are exactly the shortened donors.  Every original bottom `B_u`
either remains at `u` or traverses the unique outgoing arc; target
indegree at most one makes these destinations distinct.  Hence the bottom
targets are merely permuted, all middles/roots stay fixed, and (1.6)
follows.  The location reconstruction proves the converse and uniqueness.
\(\square\)

An ordinary column is a one-edge path `D->F`; an atomic relay is a two-edge
path `A->D->F`.  Longer paths are the exact compound columns needed for
serial relay CEGAR.  This normal form is strictly preferable to treating
overlapping relays as illegal local edits.

### Theorem 1.3 (two coupled matchings are exactly the same static object)

Let `H` denote the `18646` hard donor rows.  Use terminal variables
`t_(u,F)` on (1.9), and assignment variables `p_(u,v)` on (1.8), now also
including every self edge `p_(u,u)`.  Impose

\[
\begin{aligned}
 \sum_Ft_{uF}+\sum_vp_{uv}&=1 &&(u\in H),\\
 \sum_ut_{uF}&=1 &&(F\in\mathcal F),\\
 \sum_up_{uv}&\le1 &&(v\in H).                         \tag{1.12}
\end{aligned}
\]

Put

\[
 D=\{u:\sum_Ft_{uF}=1\},\qquad
 S=\{v:\sum_up_{uv}=0\}.                              \tag{1.13}
\]

Then `|D|=|S|=1748`, `t` is a perfect matching from `D` to the free rows,
and

\[
                     p:H\setminus D\longrightarrow H\setminus S \tag{1.14}
\]

is a perfect matching.  Conversely every pair `(t,p)` of this form is
equivalent to one and only one donor path/cycle flow from Theorem 1.2:
delete every self edge of `p`, orient each remaining `p_(u,v)` as `u->v`,
and orient every `t_(u,F)` as `u->F`.

#### Proof

The first two rows of (1.12) give exactly `1748` terminal assignments, so
`|D|=1748` and exactly `|H|-1748=16898` `p` edges are selected.  Head
capacity makes their images distinct; hence exactly `1748` heads are
missed, proving `|S|=1748` and (1.14).  If a donor has a nonself `p`
predecessor, injectivity prevents its own `p` edge from being a self edge;
it therefore has a nonself or terminal outgoing arc.  This is exactly
`outdegree>=indegree`.  Self `p` edges are precisely untouched donors.
The reverse construction restores those self edges, so the maps are
inverse.  \(\square\)

This is the cleanest static master.  Its complete assignment contains
exactly `18646` positive `t/p` variables.  Therefore a fixed-oracle failure
has the unconditional positive-only no-good

\[
             \sum_{e\in(t^*\cup p^*)}z_e\le18645.       \tag{1.15}
\]

Unlike the sparse flow encoding, no negative literals are needed: every
bottom already chooses exactly one terminal, nonself, or self destination.

The equivalence stops at the static payload.  A typed relay service label is
additional structure.  For an atomic macro `R(h,A,D,F)`, a service variable
must imply at least

\[
 p_{A,D}=1,qquad t_{D,F}=1,qquad
 sum_up_{u,A}=0,                                      \tag{1.16}
\]

and the regenerated `A,D,F` rows must pass the literal union-supplier test
for `h`; head labels must then be injected.  A longer path needs its own
path-fragment service semantics.  Neither (1.12) nor the abstract statement
“`p` is perfect” contains this legality.  Most importantly, neither contains
one common short address state: common-state `1S` remains the exact
fixed-table oracle.

### Corollary 1.4 (one augmented bipartite perfect matching; TU base)

There is an equivalent single-matching formulation.  On the left put one
vertex for each real donor in `H` and `1748` labelled dummy vertices.  On
the right put the `1748` free rows and one row slot for every donor in `H`.
Use edges

\[
\begin{array}{ll}
 u\longrightarrow F&\text{when }B_u\subsetneq R_F,\\
 u\longrightarrow v&\text{when }B_u\subsetneq M_v,\\
 \delta\longrightarrow v&\text{for every dummy }\delta\text{ and }v\in H.
\end{array}                                                    \tag{1.17}
\]

Then augmented perfect matchings are in bijection with the coupled objects
of Theorem 1.3 after quotienting permutations of the dummy labels.  Indeed,
no dummy can hit an `F`, so the real-to-`F` edges are exactly `t`; the
remaining real-to-`H` edges are exactly `p`; and the dummies occupy the
omitted row set `S`.

The explicit augmented graph has

```text
real-to-F edges                         401754
real-to-H edges including self         2129483
dummy-to-H edges                       32593208
total explicit augmented edges        35124445
```

The last family should not be materialized.  Introduce one quotient bit
`s_v` per donor row and use

\[
\begin{aligned}
 \sum_Ft_{uF}+\sum_vp_{uv}&=1,\\
 \sum_ut_{uF}&=1,\\
 \sum_up_{uv}+s_v&=1.                                  \tag{1.18}
\end{aligned}
\]

This is the projection by dummy symmetry.  It is integral: before
projection it is the bipartite perfect-matching polytope, whose incidence
matrix is totally unimodular; equivalently (1.18) is the same bipartite
incidence system with the dummy shore aggregated into row-slack variables.
Thus the determinant-two obstruction does not occur in the static table
layer.  It can first occur after the common state/socket rows are coupled.

For Benders, never block a particular labelled-dummy matching: its `1748!`
permutations represent one table.  Block the `18646` selected real `t/p`
edges as in (1.15); they determine every `s_v` and the complete payload.

## 2. Exact interface to the fixed-table oracle

For a selected outer vector `z`, materialize its table `T(z)`.  The exact
fixed-table oracle must regenerate all active long flags, all active short
states, every accepted direct arc, and every common-state short hyperarc.
It then decides equations (4.1)--(4.2) of the launch specification.  Denote
this Boolean oracle by

\[
                         \mathsf{Oracle}(z,y),                \tag{2.1}
\]

where `y` denotes its flag and arc variables.

The column interface records every changed physical row and a replay hash.
An ordinary or relay column is atomic: it is not legal to retain an old
supplier record of `A` or `D` after selecting the column.  The fixed oracle
is always rebuilt from `T(z)`.

## 3. The unconditional Benders no-good

Suppose the fixed oracle is exhaustive and UNSAT at an outer selection
`z*`.  Because (1.3) selects exactly `1748` columns, the clause

\[
                    \bigvee_{c:z_c^*=1}\neg z_c             \tag{3.1}
\]

or, equivalently,

\[
                    \sum_{c:z_c^*=1}z_c\le1747              \tag{3.2}
\]

excludes exactly that selected atomic configuration and is always valid.
It remains valid in the presence of relay columns because a different relay
or ordinary choice changes at least one selected column.  Multiple column
descriptions that happen to materialize the same payload merely make (3.1)
weaker, never unsound.

The implementation emits only (3.1) on the disjoint atomic face unless a
smaller cut has a separately verified global proof.  In the donor-flow
master of Theorem 1.2, the analogous unconditional no-good is the **signed
complete arc assignment**

\[
 \bigvee_{e:z_e^*=1}\neg z_e\ \vee
 \bigvee_{e:z_e^*=0}z_e.                                           \tag{3.3}
\]

The negative assumptions cannot be dropped: keeping every current path arc
while adding an arc from an unused donor into a current path source can
still satisfy (1.8)--(1.10) and changes the table.  Thus a positive-only
selected-arc no-good is not proof-safe in the path-flow master.

In the self-completed coupled-matching encoding of Theorem 1.3, use the
shorter positive-only no-good (1.15).  These two statements are consistent:
the missing negative sparse-flow assumptions are represented by selected
self edges in `p`.

## 4. Strongest generic pulled-back cut

Build one **global super-formula**

\[
 \Phi(z,y)=\mathsf{Outer}(z)\wedge\mathsf{AllModesAndSockets}(z,y), \tag{4.1}
\]

containing every ordinary and relay mode and every exact common-state
socket.  Let `A` be a set of signed outer literals.  If a checkable proof
establishes

\[
                         \Phi\wedge\bigwedge_{\ell\in A}\ell
                         \quad\text{UNSAT},                  \tag{4.2}
\]

then the exact Benders cut is

\[
                         \bigvee_{\ell\in A}\neg\ell.       \tag{4.3}
\]

This signed assumption-core clause is the strongest generic proof-safe
pullback: positive literals fix selected columns; negative literals may be
load-bearing because enabling a previously absent relay can create a new
long mode or a new socket.  A positive-only core is valid only when (4.2)
has been proved with positive assumptions only.

### Empty-short specialization

For a physical row `s`, let `Short_s(z)` be its active-short predicate and
let `H_s` be the **complete global** catalogue of common-state sockets which
could use `s`.  If `Act_h(z,y)` is the full activation predicate for socket
`h`, define

\[
 E_s(z,y)=\neg Short_s(z)\ \vee\bigvee_{h\in H_s}Act_h(z,y). \tag{4.4}
\]

An assumption set `A` proves a persistent empty short precisely by proving

\[
                 \mathsf{Outer}\wedge E_s\wedge
                 \bigwedge_{\ell\in A}\ell\quad\text{UNSAT}. \tag{4.5}
\]

The disjunct `not Short_s` is essential: a completion may otherwise evade
the cut by turning `s` into a long row.

### Hall-shore specialization

For a state-expanded demand shore `Q`, let `Match_Q(z,y,p)` assert either
that a demanded configuration in `Q` deactivates or that all active members
of `Q` inject into their globally active provider/socket configurations.
Then a pulled-back Hall cut is valid exactly after proving

\[
 \mathsf{Outer}\wedge Match_Q\wedge
                 \bigwedge_{\ell\in A}\ell\quad\text{UNSAT}. \tag{4.6}
\]

Equations (4.5)--(4.6) make no dependency-halo assumption.  They also show
why a Hall shore computed in one rebuilt fixed graph does **not** by itself
justify a smaller outer cut: a different column outside the visible shore
may activate a new provider mode.  Until the complete global socket/mode
catalogue and a proof of (4.2), (4.5), or (4.6) are available, (3.1) is the
only cut emitted by the interface.

## 5. Exact warm-table incompatibility with the atomic face

The authenticated round-47 relay lineage is an excellent fixed-table oracle
warm start: its union projection is perfect `16898/16898`.  It is **not** a
feasible warm vector for (1.3)--(1.4).

The independent resource replay finds that physical row `520` occurs first
as an `A` row in the exchange `520 -> 2117` and then as a `D` row in the
exchange `29 -> 520`.  Hence it violates (1.4).  The combined payload is the
length-two relay path

\[
 B_{29}\longrightarrow520,qquad B_{520}\longrightarrow2117, \tag{5.1}
\]

not two disjoint atomic relays.

Consequently one must choose one of two proof-safe scopes:

1. use the round-47 table only as a fixed-oracle warm start, while the
   atomic outer master starts from another feasible `O/R` selection; or
2. add one explicitly replayed compound path column whose internal row may
   be both the destination of one relay and source of the next, while its
   external row resources remain disjoint from all other selected columns.

Silently loading round 47 into the disjoint atomic `O/R` master is invalid.
Theorem 1.2 gives the cleaner resolution: load the complete donor-path flow,
where the row-520 overlap is a legal internal vertex.

Independent reconstruction from the original table and the final round-47
table, without using the producer lineage, gives

```text
terminal arcs                         1748
internal donor arcs                     48
path components                       1748
cycle components                         0
paths with 0 / 1 / 2 internal arcs 1701 / 46 / 1
maximum internal path length              2
selected-arc FNV64         b87618c0d8bec1f2
```

It exactly replays the full target partition and `outdegree>=indegree` at
every donor.  This independently identifies the unique two-relay path
through row `520`.

## 6. Frozen implementation and audit scope

The source

```text
scratch/k_rots_k17_joint_1s_20260802/
  build_k17_outer_benders_columns_20260802.cpp
```

implements:

* exact enumeration and literal validation of all `401754` ordinary columns;
* optional `R(H,A,D,F)` columns with exact payload and regenerated
  union-supplier validation;
* Sinz exact-one/at-most-one rows (1.3)--(1.5);
* exact materialization and complete target/chain/soft-row replay;
* the unconditional full-table no-good (3.1);
* a fail-closed separation between that no-good and unproved refined cuts;
* the round-47 `A/D` resource audit.

It also implements the linear-time donor-path reconstruction of Theorem
1.2, exact enumeration of all internal/terminal flow arcs by Boolean
submask lookup, a Sinz CNF for indegree/outdegree/terminal rows and
`outdegree>=indegree`, the complete signed flow no-good (3.3), and the exact
two-coupled-matching catalogue/CNF (1.12), including all self edges.  The
coupled CNF uses the quotient equations (1.18), so no labelled dummy edge is
ever emitted.  The
catalogue/CNF modes are intended for the authorized H100 CPU lane and were
not run locally.  The frozen lightweight reconstruction artifacts are

```text
scratch/k_rots_k17_joint_1s_20260802/outer_benders_flow_audit/
  flow_reconstruction.audit.json
  selected_flow_arcs.tsv
```

with SHA-256 values `a5411f3b...` and `8ad274d4...`, respectively.

The source compiles cleanly with `clang++ -std=c++20 -O2 -Wall -Wextra
-pedantic`.  The complete `401754`-column generation and any global socket
super-formula belong on the authorized H100 CPU lane; they were not run
locally in this audit.

The parallel finite lane has now frozen the exact relaxed-nine fixed-table
oracle for the round-47 table:

```text
common-state socket tuples                         2188
duplicate complete tuple rows                         0
short roles with no common-state socket            5969
fixed CNF variables / clauses             348687 / 617660
fixed CNF empty clauses                            9570
Kissat / DRAT-trim                                  UNSAT / VERIFIED
```

The load-bearing hashes are:

```text
census source       b3bed193dbbed859b8f24f9bd82d56a716f2493dba616e8a2d606d89de03505e
socket tuples       381a29b7d83dec652ac0da7bf63f7ae9b5bdb515ab325ac66ffe2d1409ea1e97
socket summary      3bbf173f17164bed8ca49eb3f4e017e02dec6a2df9f26c35bfdd15fb56bb99d5
fixed CNF           a7ff4da4d83a8346354960bf2f5c3efa04f3d3023518f4377106dced80fe0b88
independent replay  0c4f20b0c50231b3ef2aa7218b724db8665886a459fd4bfd39ce72a92894ce94
final manifest      bc026e77dd6d34c472bb21b01ffdcd0a52e48ef15bcc1ebf3593b992ae2b8a24
```

Thus the **fixed round-47 relaxed-nine `1S` oracle is exactly UNSAT**.  This
does not pull back to a global atomic outer cut: round 47 has no feasible
atomic outer vector by Section 5.  It is instead a sharp pricing signal for
the compound relay-path extension.  Even after that extension is added, the
only automatic learned clause is the full selected-configuration no-good;
the `5969` empty roles do not by themselves prove a smaller global cut.

## 7. Remaining exact gate

The next finite step is:

* use the exact donor-path flow rather than the disjoint atomic face;
* change at least one arc assignment (the unchanged round-47 table is
  already fixed-oracle UNSAT);
* regenerate the exact `1S` catalogue after each proposal; and
* learn either the complete signed arc no-good (3.3) or a verified signed
  assumption core of the global activation formula.

Smaller empty-short or Hall cuts should be admitted only as verified signed
assumption cores of a complete global activation formula.  This is the
minimal proof-safe Benders interface; no unproved locality halo is needed.
