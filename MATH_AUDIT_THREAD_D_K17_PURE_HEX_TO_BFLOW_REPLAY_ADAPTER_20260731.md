# K17 pure-hex selection: exact residual-flow and physical replay adapter

Date: 2026-07-31  
Lane: Thread D, `OPTIMAL28` physicalization  
Status: dependency-clean exact reduction and implementation contract; no
compatible hex selection or `K17` word is claimed

## 0. Result

The `5,433` active records in

```text
scratch/threadD_k17_opt28_hex_variant_catalogue_20260731.audit.json
```

are toggles in the **full rank-eight/rank-nine incidence factor**.  They are
not replacements of one of the old `1,430` macro objects.  Consequently a
selected set must first be composed in the incidence graph.  Only then may
the resulting fixed paths be contracted and handed to a fresh residual
`U`-owner flow.

There is a lossless five-stage adapter:

1. compose the selected hex columns literally and verify the degree-two
   owner/colour equations;
2. freeze every tagged-owner incidence, both incidences of the `133` packet
   `U` owners, and the complete final owner pair of every colour touched by
   a selected column;
3. contract the frozen incidence paths and solve one exact residual
   `U`-to-port pair flow with quotient connectivity cuts;
4. traverse the resulting incidence factor, anchor the unchanged marked
   packet, and materialize the literal two-bank row `Z`; and
5. replay maximal inversion, all upper interval providers, and export the
   exact common-cap input relation.

Every failure in this chain has a sharply delimited meaning.  In particular,
a failed greedy cycle-switch pass is not an infeasibility certificate.

## 1. Literal hex composition

Let

\[
 {\mathcal O}={ [17]\choose9},\qquad
 {\mathcal C}={ [17]\choose8}.
\]

The authenticated owner cycle determines

\[
 I_0=\{(c_i,T_i),(c_i,T_{i+1}):
          c_i=T_i\cap T_{i+1}\}.                 \tag{1.1}
\]

Thus every owner and every colour has incidence degree two.  An exported
hex `h` contains disjoint triples `R_h subset I_0` and
`A_h subset (C x O) \ I_0`.  For a selected set `X`, put

\[
 R(X)=\biguplus_{h\in X}R_h,\qquad
 A(X)=\biguplus_{h\in X}A_h,\qquad
 I_X=(I_0\setminus R(X))\cup A(X).                \tag{1.2}
\]

The disjoint-union signs in (1.2) are constraints: the adapter rejects a
repeated removed incidence or repeated added incidence.  More generally,
one may admit overlapping columns only by constructing the final set and
checking all the equations below; summing local scores is not sufficient.

### Lemma 1.1 (exact compatible-column criterion)

The selected columns give an owner/lower-palette factor if and only if

* every removed incidence belongs to `I0` and every added incidence does
  not;
* `I_X` is a set of containment incidences;
* every `T in O` has degree two in `I_X`; and
* every `c in C` has degree two in `I_X`.

Under the catalogue's duplicate-free convention, the last two equations
follow by adding the individually degree-neutral hex vectors.  They must
nevertheless be replayed literally, since future column families need not
be disjoint.

The proof is immediate: a two-regular bipartite inclusion graph is exactly
a disjoint union of alternating owner/colour cycles, and suppressing each
colour gives the corresponding lower-rainbow Johnson factor.  Notice that
this proves degree and palette exactness, not connectivity or residence.

## 2. The strong packet guard

Let `P` be the union of the `106` mandatory and `28` selected optional
packet components.  It contains `4,108` owners, including the `133` fixed
pure-`U` owners.  The safe packet-side guard is

\[
       N_{I_X}(w)=N_{I_0}(w)\quad(w\in P),          \tag{2.1}
\]

together with equality of the full two-owner pair for every **internal**
packet colour.  At each of the two boundary/socket colours only the
packet-side incidence is fixed; the exterior endpoint may lawfully change
under the fresh residual flow.  These rows preserve the literal component
words, their internal lower colours, and all `134` packet signatures,
rather than only their owner sets, without overfreezing the exterior.

For the frozen `5,433`-column catalogue this strong test is automatic but
should still be asserted: none of the three changed owners is marked, and
an independent scan finds zero columns whose recorded `fixed_other_owner`
is marked.  This is stronger than the producer's advertised
`marked_owner_safe` condition and is the reason the catalogue can be used
without rebuilding the packet path.

## 3. Exact release to a fresh residual b-flow

Put

\[
 {\mathcal U}={ [15]\choose9},\qquad
 {\mathcal T}={ [15]\choose8};                    \tag{3.1}
\]

these are the pure old-coordinate owners and ports.  Let `C_touch(X)` be
the colours appearing in a removed or added incidence.  The exact,
maximally released frozen incidence set is

\[
 F_X=\{(c,u)\in I_X:u\text{ is tagged}\}
   \cup\{(c,u)\in I_X:u\text{ is one of the 133 packet }U\text{ owners}\}
   \cup\{(c,u)\in I_X:c\in C_{touch}(X)\}.          \tag{3.2}
\]

The last term freezes the **whole final two-owner pair** at a selected
colour.  This includes a pure `fixed_other_owner` when one occurs.  It does
not freeze that owner's other, untouched colour.  Such an owner has one
frozen incidence and residual owner demand one.  Recursively freezing its
whole owner pair would be a sound but strictly stronger safe closure, not
the exact pure-hex face.

For every owner or colour vertex define

\[
 b_X(v)=2-\deg_{F_X}(v).                            \tag{3.3}
\]

The adapter fails closed unless `0 <= b_X(v) <= 2`.  Tagged colours have
demand zero, since no pure owner can contain a tagged colour.  Residual
incidences therefore run only between pure owners and old ports.

### Lemma 3.1 (path contraction)

Every connected component of `F_X`, after including all isolated owner and
colour vertices,
is one of:

* a path with total residual endpoint demand two;
* an isolated vertex, also with demand two; or
* a cycle with demand zero.

A zero-demand frozen cycle is an exact connectivity obstruction: no
residual pure owner can meet it.

#### Proof

Every vertex has frozen degree at most two.  A finite connected
maximum-degree-two graph is a path, a cycle, or an isolated vertex.  A path
has two unit-deficient endpoints, a cycle none, and an isolated vertex has
deficit two.  A zero-demand component has no socket for a released
incidence.  \(\square\)

Before solving any residual flow, orient each nontrivial frozen path both
ways and scan its literal owner trace.  In a complementary path that will
be facetized, a positive coordinate run bounded by zeros strictly inside
the path cannot have length below four: residual incidences attach only at
the two path endpoints, so no completion can extend such a run.  The marked
packet is used directly as rank-nine rows and has threshold three instead.
These are exact, solver-free rejection rows.  Runs meeting an endpoint are
not rejected locally; their two boundary trace states are exported to the
quotient chronology and checked after splicing.  On the empty-selection
regression this test returns exactly the authenticated `724` complementary
hazards, with no marked-packet defect.

Exact degree completion is the capacitated bipartite flow

\[
\begin{aligned}
 &\sum_{p\subset u:(p,u)\notin F_X}x_{u,p}=b_X(u) &&(u\in U),\\
 &\sum_{u\supset p:(p,u)\notin F_X}x_{u,p}=b_X(p)&&(p\in T),\\
 &x_{u,p}\in\{0,1\}.                              \tag{3.4}
\end{aligned}
\]

This is a network matrix.  Thus max flow is an exact integral decision
procedure for the degree rows; an unsaturated maximum flow plus its
source-side minimum cut is a proof certificate.

Connectivity is separate.  Contract every noncycle component of `F_X`.
Each selected residual incidence `(u,p)` is an edge between the components
containing its owner and colour endpoints.  Lemma 3.1 makes the quotient
two-regular.  It is a single cycle exactly when all proper quotient cuts
are crossed:

\[
 \sum_{u,p:|\{K(u),K(p)\}\cap S|=1}x_{u,p}\ge2    \tag{3.5}
\]

for every nonempty proper component set `S`.  These are the exact lazy
subtour rows.

The incidence rectangle

\[
 (u,a),(v,c)\longmapsto(u,c),(v,a)                 \tag{3.6}
\]

is legal when `c subset u`, `a subset v`, and both owner pairs remain
distinct.  If its two removed quotient edges lie in different cycles in
the crossing orientation, it merges those cycles while preserving every
degree.  The implementation in
`scratch/search_ad_k17_opt28_residual_cycle_switches_20260731.py` is a
sound sufficient merger.  Failure to find (3.6) is only `STUCK`, never
`UNSAT`; proof of infeasibility requires completion of (3.4)--(3.5).

## 4. Direct factor materialization

After residual completion, combine its selected incidences with `F_X` and
recheck Lemma 1.1.  Do not feed the result to the old materializer as
`1,430` unchanged macros: a hex can split and rejoin macro interiors, so
those blocks are stale.

Instead, for each colour join its two incident owners.  This gives a
degree-two colour-labelled owner graph.  A connected graph is one Johnson
cycle.  Traverse it from the first packet boundary in the unique
orientation whose marked interval equals the authenticated marked word.
Fail closed unless:

* all `24,310` owners occur once;
* all `24,310` lower colours occur once;
* the marked owners induce exactly the authenticated `4,108`-owner path;
* exactly two factor edges cross the marked cut; and
* all declared packet incidences and source sockets agree literally.

Write the cycle as

\[
       P_1,\ldots,P_{4108},Q_1,\ldots,Q_{20202}.    \tag{4.1}
\]

Its two-bank target row is

\[
 Z=(P_1,\ldots,P_{4108},
     P_{4108}\cap Q_1,
     Q_1\cap Q_2,\ldots,Q_{20202}\cap P_1),        \tag{4.2}
\]

of length `24,311`.  Formula (4.2), not a concatenation of surviving old
macro arrays, is the authoritative physical chronology.

## 5. Exact residence, replay, and provider audit

For `0 <= p < |Z|+2`, put

\[
 E_p=\bigcap_{\max(0,p-2)\le i\le\min(|Z|-1,p)}Z_i.\tag{5.1}
\]

The row is physically invertible exactly when every `E_p` is nonempty and

\[
                 E_i\cup E_{i+1}\cup E_{i+2}=Z_i  \tag{5.2}
\]

for every row.  The exact replay must export both failed row IDs and failed
`(row,bit)` host obligations.  Counting only old hazards hit by selected
hexes is not a substitute: columns can create new short runs at their
sockets.  The derived `D3` row and every endpoint/cyclic run are replayed as
separate audit invariants.  This is the exact downstream interpretation of
the local `R3` signature.

For upper targets, scan every linear interval of `Z`, accumulating its OR
until the union is the full mask.  Record targetwise loads at every rank
`10,...,17`.  For ranks `10--12`, compare with the authenticated baseline
loads and export

```text
final holes,
baseline-covered targets with final load zero,
gained targets,
sum_T max(0, baseline_load(T)-final_load(T)),
and all surviving provider intervals for protected targets.
```

Ranks `13--17` must also be replayed; their baseline completeness is not
monotone under rethreading.  Rank ten has an additive owner-edge delta only
when the closing edge and every touched colour's other endpoint are fixed.
Ranks eleven and twelve are chronology-dependent and never admit a sum of
independent one-hex scores in the presence of interacting columns.
An upper hole is recorded as a residual short-target obligation rather than
called an immediate physicalization failure; the subsequent common-cap
instance decides whether the available singleton/pair cells can discharge
it simultaneously with the lower bank.

## 6. Common-cap-ready output

A row passing (5.1)--(5.2) should export, without claiming compiler
feasibility,

```text
owner_cycle, marked interval and its two boundary colours,
Z and the maximal envelope E,
failed/satisfied (row,bit) host rows,
all target-labelled upper provider intervals,
fixed prepins and occupied singleton/pair cells (possibly empty),
the exact residual target list, and every labelled singleton/pair cell with
its envelope masks.  The last two objects plus (6.1) are an authenticated
candidate-graph generator, equivalent to writing the generally much larger
residual target-to-cell graph explicitly.
```

For a residual target `S` and unused singleton/adjacent-pair cell `J`, the
candidate relation is exactly

\[
 E_p\cap S\ne\varnothing\ (p\in J),\qquad
 S\subseteq\bigcup_{p\in J}E_p.                    \tag{6.1}
\]

After fixed prepins, replace `E` by their capped envelope `B`.  A matching
in (6.1) is not by itself sufficient: the exact common-cap obstruction
clutter has unary, pair, and triple rows.  Therefore the adapter must pass
the target-labelled envelope and cell identities to the established
common-cap solver; it must not emit a scalar `cap_slack` certificate.

## 7. Reusable implementation surfaces

The existing code separates naturally as follows.

| role | existing source | action |
|---|---|---|
| exact selected-hex to residual-flow sidecar | `scratch/prepare_threadD_k17_pure_hex_bflow_instance_20260731.py` | implemented; composes toggles, guards packet, contracts frozen paths, scans internal residence, and emits capacitated incidence rows |
| residual flow, topology and physical replay | `scratch/solve_threadD_k17_pure_hex_bflow_replay_20260731.py` | implemented; exact degree max-flow/min-cut, legal rectangles or quotient-cut export, direct incidence traversal, full `Z`/upper replay and common-cap handoff |
| authenticated hex data | `scratch/threadD_k17_opt28_hex_variant_catalogue_20260731.audit.json` | consume `minimal_hex_catalogue.columns`; verify payload |
| baseline incidences and packet owner set | `scratch/audit_threadD_k17_opt28_hex_variant_catalogue_20260731.py` | reuse its literal reconstruction; do not trust only row IDs |
| residual degree flow and legal rectangles | `scratch/search_ad_k17_opt28_residual_cycle_switches_20260731.py` | extract `Dinic`, pair validation, quotient and switch kernels; remove hard-coded macro/path globals |
| independent flow replay | `scratch/audit_ad_k17_opt28_residual_connected_bflow_20260731.py` | generalize input to frozen-component sidecar |
| literal `Z`, inverse, and arbitrary-width upper replay | `scratch/materialize_k17_opt28_connected_owner_cycle_20260731.py` | retain the scan, replace stale macro-object expansion by direct incidence traversal |
| exact common-cap handoff | `MATH_THEOREM_R_K17_OPT28_ONECYCLE_DEEP_SHADOW_AND_COMMON_CAP_CUTS_20260731.md`, Section 5 | emit `(Z,B,candidates,prepins)` and solve its rank-three clutter |

The proposed generic sidecar schema is

```json
{
  "schema": "threadD-k17-opt28-compatible-pure-hex-selection-v1",
  "selected_hex_ids": [],
  "removed_incidences": [[0, 0]],
  "added_incidences": [[0, 0]],
  "frozen_incidences": [[0, 0]],
  "owner_demands": [{"owner": 0, "demand": 0}],
  "frozen_components": [{
    "component": 0,
    "owners": [],
    "endpoint_ports": [0, 0],
    "residual_demand": 2
  }],
  "port_demands": [{"port": 0, "demand": 0}],
  "packet_signature_sha256": "...",
  "payload_sha256": "..."
}
```

Cycle components use an empty endpoint list and are rejected before flow.
An isolated owner or port has two residual demand slots; it must not be
serialized as a loop edge.

The implemented preparer has a solver-free empty-selection regression:

```text
frozen incidences                              38876
frozen bipartite components                     9744
zero-socket cycles                                  0
strict internal complementary hazards             724
residual incidence demand                        9744
candidate residual incidences                   39353.
```

Thus it recovers the exact `724` obstruction while leaving precisely the
old `9744` incidence units for the residual flow.  The `9,744` bipartite
components are equivalent to the older `4,872` port components after each
degree-two free owner is suppressed; the counts must not be compared as if
they used the same contraction.

The executable handoff is

```sh
python3 scratch/prepare_threadD_k17_pure_hex_bflow_instance_20260731.py \
  SELECTED_HEX_IDS SELECTION.bflow-instance.json

python3 scratch/solve_threadD_k17_pure_hex_bflow_replay_20260731.py \
  SELECTION.bflow-instance.json OUTPUT_PREFIX --attempts 200 --seed 1731
```

The second command is the H100-side step.  Its degree-flow `UNSAT` status
comes with a literal minimum cut.  A saturated but disconnected result is
`TOPOLOGY_OPEN` together with exact quotient-cut rows unless one such row
has fewer than two candidates, in which case that static cut is a proof.
Only a connected factor is allowed to enter direct `Z` replay.

## 8. Failure taxonomy and principal pitfalls

Use distinct terminal statuses:

```text
INVALID_HEX_COMPOSITION
PACKET_SIGNATURE_CHANGED
FROZEN_ZERO_SOCKET_CYCLE
RESIDUAL_BFLOW_UNSAT_WITH_MINCUT
RESIDUAL_BFLOW_SAT_TOPOLOGY_OPEN
CONNECTED_FACTOR_R3_REJECT
COMMON_CAP_UNSAT_WITH_CORE
PASS_Z_REPLAY_COMMON_CAP_INSTANCE_EXPORTED
```

The principal unsound shortcuts are:

1. applying hexes to macro endpoint pairs instead of full incidences;
2. freezing only the toggled endpoint, rather than both final endpoints, of
   a selected-touched colour, or conversely overfreezing the fixed-other
   owner's unrelated incidence and silently shrinking the exact face;
3. reusing the old residual assignment without checking its new port
   demand;
4. calling a failed greedy rectangle search `UNSAT`;
5. materializing from stale macro blocks after an interior split;
6. treating old-row coverage as absence of newly created residence defects;
7. adding rank-eleven/twelve provider deltas columnwise;
8. omitting the linear closing-edge correction in rank ten;
9. assuming ranks `13--17` remain covered; and
10. treating nonempty envelopes, ordinary Hall, or scalar slack as an exact
    common-cap certificate.

This reduction is exact for the declared pure-hex plus released-`U` face.
It neither proves that the face is feasible nor excludes the arity-two
split/merge extension if it is not.

## 9. Authoritative occurrence296+C6 rebase

The later, strictly different base is frozen by

```text
scratch/k17_opt28_occurrence_greedy296_verified_20260731.flow.json
  SHA 079f5cd96f713ef2d72dd43acff10f84416acdb670aeff96f61a3cb97f29c25f
  payload fed50b14fda074d87f5fc610b9c529550a9e2a85f550bc6a298bc8b4fd561cb4

scratch/k17_opt28_occ296_c6_localmin_verified_20260731.residual.json
  SHA 6fcc91d45b2090b26b612020340a21088a2367c5c0bccd10d3d3614042c60fe4
  payload c92b72db852a8362a2f99c8091dec072ef42af831e1ef83af5381375d6d2a6e4

scratch/k17_opt28_occ296_c6_localmin_verified_20260731.owner_cycle.word
  SHA a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49

scratch/h4_k17_opt28_occ296_c6_localmin_zrow_20260731.word
  SHA abfaab6541ee7d56cb11d5b208fbf4a34da214734113e399d15a355222d418a8

scratch/h4_k17_opt28_occ296_c6_localmin_independent_20260731.audit.json
  SHA 0bca08d71f42db8fc97ff599328fd725c32abb0de2c30396ce72bf70374d32a4
  payload 1466d61c961b3343151fa0e84fea2b6a9edce6d8b4bbf498ce751041eef1cc91
```

The governing theorem is
`MATH_THEOREM_H2_K17_OPT28_PORT_CIRCUIT_INVARIANT_AND_OCC296_C6_VECTOR_20260731.md`.
This base has central/lower-`q1` defect zero, a `296` component-interior
residence floor, `503` strict nonflat defects, `748` replay-failing rows with
`776` missing bits, and upper holes `1585/824/116/0/.../0` in ranks
`10,...,17`.

Nothing indexed by the old `a736ef9d...` owner cycle may be transplanted.
Before using the v1 adapter on this base one must regenerate:

1. every alternating-hex column and its IDs from the `a47aa9d7...`
   incidence factor;
2. marked-owner and fixed-other packet safety against the `079f5cd9...`
   occurrence forest, even though the literal marked word replayed unchanged;
3. all removed/added incidence resource cliques;
4. the `296` inherited hazard rows, their disjoint-interval packing, and the
   resulting column-count lower bound (the old `724/452/151` ledger is void);
5. every guarded final-edge residence/replay motif;
6. all target-labelled rank-ten--twelve provider occurrences and weights
   from the `abfaab65...` row, its linear closing-edge correction, and the
   rank-thirteen--seventeen replay;
7. the selected-touched colour pairs, owner/colour residual demands,
   contracted fixed components and residual candidate incidences; and
8. the common-cap generator instance, only after literal replay succeeds.

In particular, the old `5,433`-column selection result, its lazy cuts, and
any old-base infeasibility core have no certified implication for the
occurrence296+C6 base.
