# Independent audit: K17 `1S-ROTS` outer Benders, donor flow, and coupled matchings

**Date:** 2026-08-02  
**Verdict:** PASS for the static outer semantics, round-47 reconstruction,
and cut scopes stated below.  The fixed round-47 relaxed-nine oracle is
independently UNSAT.  No global outer-master SAT/UNSAT verdict follows.

**Authority:** the global master is now
`MATH_THEOREM_K17_TWO_MATCHING_DONOR_PATH_AND_JOINT_1S_ROTS_GATE_20260802.md`
(SHA-256
`b252f59b76e5ea613842d3633ecba8fb81f47477ae9b2fa1eee467cd9aff99a5`).
The atomic-column portion audited here is a strict subface; the donor-flow,
two-matching equivalence, service/state boundary, and proof-safe cut audit
agree with the superseding theorem.

## 1. Audited objects

The audited implementation is

```text
scratch/k_rots_k17_joint_1s_20260802/
  build_k17_outer_benders_columns_20260802.cpp
```

It compiled without diagnostics under

```text
clang++ -std=c++20 -O2 -Wall -Wextra -pedantic
```

The accompanying theorem is

```text
MATH_THEOREM_K17_1S_ROTS_GENERALIZED_RELAY_OUTER_BENDERS_AND_CUT_SCOPE_20260802.md
```

The local audit ran only linear-time table/lineage reconstruction.  It did
not run the multi-million-edge global catalogue locally.  An attempted H100
resource poll failed at DNS resolution and was not misreported as a solver
status.

The independently available authoritative streaming builder and size audit
are hash-bound as follows:

```text
build_k17_two_matching_outer_master_20260802.cpp
f2cf43c7e44d16e15ee6449587bc2e4a1c0cc8a37f6351c5726e8ce4e0867324

size.audit.json
f1600a3e65fa3597f60affc919bea79e8e2bfe8cdd52bd850f21a0658f841cad

round47_two_matching.selection.tsv
d56126ff3d1d8fde67dd6a6446c0974ded36921993fd093edc94a279c0e5a5b9
```

## 2. Atomic column replay

For every ordinary column, direct multiset comparison gives

```text
old  F,D: R_F ; B_D,M_D,R_D
new  F,D: B_D,R_F ; M_D,R_D
```

For every relay column, comparison gives

```text
old  F,A,D: R_F ; B_A,M_A,R_A ; B_D,M_D,R_D
new  F,A,D: B_D,R_F ; M_A,R_A ; B_A,M_D,R_D.
```

Thus exact `F` cover plus one shared capacity row for every occurrence as
`A` or `D` is sufficient for global target preservation.  Separate `A` and
`D` capacities would be unsound.  The implementation uses the shared row.
It also replays all 65,535 named targets, strict chains, the
`(0,7395,16915)` histogram, owner/root identity, and all 17 soft rows after
selection.

Typed service-head legality is not inferred from the payload identity.  A
relay column is admitted only after one regenerated `F/A/D` mode supplies
its declared hard head in the exact complete-menu union projection.  This is
still weaker than a common-state `1S` socket, which correctly remains in the
fixed-table oracle.

## 3. Round-47 atomic obstruction and exact donor-flow replay

The producer lineage has 47 listed strict exchanges.  Independent `A/D`
resource incidence finds exactly one cross-role row:

```text
row 520 is A in 520 -> 2117
row 520 is D in 29  -> 520
```

Therefore the final table is not a selection of cross-role-disjoint atomic
`R(H,A,D,F)` columns.  This is not a table defect; it is one compound relay
path.

Reconstruction directly from the original and final payload tables, without
using the producer lineage, gives:

```text
terminal arcs                         1748
internal arcs                            48
path components                       1748
cycle components                         0
internal-arc path histogram       0:1701, 1:46, 2:1
maximum internal arcs                    2
```

Every donor satisfies `outdegree>=internal indegree`, every free row has one
terminal, and the complete target partition replays.  The unique two-internal
arc path contains row 520.

Frozen artifacts:

```text
flow_reconstruction.audit.json  c29dbb3170adf6d217c5a40dc5ea9b24ff3edbdf2177f8355dac22833a339e9d
selected_flow_arcs.tsv          8ad274d4c4395c6ec74fd06ad3f171a9f1854f53e1e0fc3bd5cb5001d2cf7bdb
selected_coupled_matching.tsv   2260230d79a3d826f12ea5335dd305954adfc81160f77a32f4007b4972c74365
atomic resource audit           bdb9224fbcb03f2ecb86ace1ab99bdebccef6bbc732a78998a0c67f5801cfe71
```

## 4. Two-coupled-matching simplification

Let `H` be the hard donor set.  The donor flow is exactly equivalent to:

1. a terminal matching `t:D -> F` on edges `B_d subsetneq R_F`; and
2. a perfect residual matching

   \[
                    p:H\setminus D\longrightarrow H\setminus S
   \]

   on edges `B_u subsetneq M_v`, including self edges.

The matching equations are

\[
 \sum_Ft_{uF}+\sum_vp_{uv}=1,
 \qquad \sum_ut_{uF}=1,
 \qquad \sum_up_{uv}\le1.                              \tag{4.1}
\]

They force `|D|=|S|=1748`.  Deleting self `p` edges gives precisely the
nontrivial donor arcs; restoring self edges reverses the map.  The round-47
fixture has

```text
t edges                 1748
p edges                16898
p self edges           16850
p nonself edges           48
```

so it is an exact positive calibration.

The simplification is **not** equivalent to a typed service-head bank.
Equations (4.1) contain no service label.  To encode an atomic
`R(h,A,D,F)`, one additionally needs `p_(A,D)=t_(D,F)=1`, `A` omitted from
the image of `p`, a literal regenerated supplier for `h`, and head
injection.  Longer donor paths need path-fragment rather than atomic
`A,D,F` semantics.  Finally, no static matching equation chooses one common
short address state.

Equivalently, add 1,748 labelled dummy bottoms, join them completely to the
donor-host shore, and forbid them from the singleton-host shore.  Perfect
matchings of this augmented graph project exactly to `(t,p,s)`.  The base is
TU because it is a bipartite perfect-matching incidence system.  Quotienting
dummy permutations is exact:

\[
 \sum_Ft_{uF}+\sum_vp_{uv}=1,
 \quad\sum_ut_{uF}=1,
 \quad\sum_up_{uv}+s_v=1.
\]

The audited global counts are `401754` terminal edges, `2129483` real
donor-host edges including self, and `32593208` dummy edges.  The quotient
has `2549883` primary variables.  This TU scope ends before typed service
labels, address flags, common-state sockets, and Benders child rows.

## 5. Benders cut audit

Three scopes are distinct.

1. **Atomic exact-F columns.** Exactly 1,748 columns are selected, so the
   positive full-table no-good is valid.
2. **Sparse donor-flow arcs without self variables.** A current arc set can
   be extended by changing a stationary donor into a predecessor of a path
   source.  The safe complete-assignment no-good is signed and includes
   unselected arcs.
3. **Self-completed coupled matching.** Exactly one `t/p` destination is
   selected for every one of the 18,646 donor bottoms.  Hence the positive
   no-good

   \[
                \sum_{e\in t^*\cup p^*}z_e\le18645
   \]

   is again complete and valid.

For any smaller cut, the exact criterion is a verified signed assumption
core of a single global super-formula containing all outer modes and all
common-state sockets.  In particular:

* a fixed-table empty short does not prove persistence if it may become long;
* a fixed-table Hall shore does not prove persistence when an outside relay
  can activate a provider;
* negative unselected-column assumptions may be load-bearing.

The implementation therefore emits only complete no-goods automatically.
This is proof-safe and deliberately weaker than an unverified dependency
halo.

## 6. Fixed round-47 oracle no-go

The final relaxed-nine fixed census has:

```text
exact common-state socket tuples       2188
duplicate tuple rows                      0
short roles with zero sockets          5969
```

The emitted fixed CNF has 348,687 variables and 617,660 clauses.  It is
trivially UNSAT because of empty exact-one rows; Kissat returns 20 and
DRAT-trim verifies the proof.  Independent replay reports 2,188 tuples,
5,969 zero short roles, and 9,570 literal empty CNF clauses.

Load-bearing hashes:

```text
census source       b3bed193dbbed859b8f24f9bd82d56a716f2493dba616e8a2d606d89de03505e
socket tuples       381a29b7d83dec652ac0da7bf63f7ae9b5bdb515ab325ac66ffe2d1409ea1e97
socket summary      3bbf173f17164bed8ca49eb3f4e017e02dec6a2df9f26c35bfdd15fb56bb99d5
fixed CNF           a7ff4da4d83a8346354960bf2f5c3efa04f3d3023518f4377106dced80fe0b88
independent replay  0c4f20b0c50231b3ef2aa7218b724db8665886a459fd4bfd39ce72a92894ce94
final manifest      bc026e77dd6d34c472bb21b01ffdcd0a52e48ef15bcc1ebf3593b992ae2b8a24
```

This closes only the unchanged round-47 relaxed-nine fixed table.  Its
perfect union projection is not a common-state cycle-cover certificate, and
the no-go is not a global outer no-go.

## 7. Exact next finite interface

Use the self-completed coupled matching (4.1) as the outer master.  Warm it
with the frozen `t/p` fixture, but require at least one assignment change.
For each proposal, rebuild the exact fixed-table common-state oracle.  Learn
the 18,646-positive complete no-good on failure; admit a smaller empty-short
or Hall cut only with a verified global assumption-core proof.  Typed
service-head variables are optional pricing/coverage structure and must not
be mistaken for common-state socket variables.
