# Audit of the nonflat component-path and residual-flow criterion

Date: 2026-07-31  
Verdict: PASS after incorporating both finite rebases: six occurrence swaps
remove the old internal marked-bank obstruction, but the repaired fixed-port
face fails the singleton component-77 connectivity cut

## 1. Component arithmetic

For a linear forest (F=(T,E_F)) with (c) components,

\[
 \sum_{t\in T}(2-\deg_F(t))=2|T|-2|E_F|=2c.
\]

Thus (c) pure owners of degree two are exactly the zero-slack completion
bank.  A path through (m) distinct forest components uses (m-1) owners,
consumes (2m-2) halfports, and leaves one supercomponent with two
halfports.  Both the residual component count and residual owner count are
(c-m+1).  The claimed neutral contraction is exact.

For the frozen ledger (c=5005,m=106), this gives 105 marked connectors,
4,900 residual components/owners, and 9,800 residual halfports.

## 2. Hall and min--max rows

For a fixed oriented component order, the marked gaps have fixed endpoint
ports.  Assigning distinct pure owners is exactly an SDR, so ordinary Hall
is necessary and sufficient.

For a fixed labelled chain on a Cartesian residual incidence face, the
source--owner--port--sink min cut has value

\[
 2(|\mathcal U_P|-|A|)+
 \sum_t\min(d_t^P,|N(t)\cap A|).
\]

Requiring it to be at least (2|\mathcal U_P|) for every owner set (A)
gives precisely Theorem 3.2.  Unit owner--port arcs correctly forbid using
the same port colour twice at one owner.  The minimum over marked chains of
the maximum Hall deficit is therefore an exact degree-feasibility min--max.

This argument does **not** cover pair-specific residence or common-cap
constraints.  The theorem correctly restricts the flow statement to a
Cartesian pair face and uses occurrence-labelled pair columns otherwise.

## 3. Topology and contiguity

The pair-column equations use every owner and halfport once.  After the
fixed forest is contracted, every quotient vertex has degree two.  The
component-cut rows are therefore necessary and sufficient for one cycle.

The marked rows choose (m-1) internal marked connectors and require every
proper marked cut to be crossed.  Hence the marked induced graph is a tree.
Its degrees are at most two because each component has two halfports, so it
is a path.  Exactly two halfports remain for marked--unmarked connectors.
The marked path is consequently one cyclic interval; deleting one of the
two crossing incidences leaves one physical bank interface.  No hidden
Hamiltonicity assumption is used.

The fixed-orientation arc formulation is the common-independent-set problem
for two endpoint partition matroids, the owner-label partition matroid, and
the graphic matroid.  Size (m-1) makes it a directed Hamilton path.  This
is a valid four-matroid description, not an Edmonds two-matroid min--max.

## 4. Independent obstructions

The four parity columns

\[
 (g_1,c_1,u_1),(g_1,c_2,u_2),
 (g_2,c_1,u_2),(g_2,c_2,u_1)
\]

have complete two-coordinate projections and the half-integral quota point,
but no two columns are resource-disjoint.  Thus separate Hall projections
do not imply a coupled connector.

Likewise an integral residual degree flow may split into two closed groups;
ordinary capacitated Hall then passes while a component cut has zero chosen
crossing columns.  The topology row cannot be dropped.

For the old endpoint-only splice graph, 50 isolated outgoing states give the
literal path-cover Hall witness

\[
 |N(S)|=0<|S|-1=49.
\]

## 5. Correct finite scope

The initially reported claim that all 190 macros in the 106-component
closure are internally clean is false.  The independently replayed frozen
artifacts show six components with 32 strict internal D2 length-two runs,
all in optional macros; D3 has no internal defect.  Endpoint connectors and
component reversal cannot alter them.  Therefore the original whole-component
column family is empty on the residence row before Hall or connectivity.

Each bad component has its unique required macro at an endpoint.  At least
six component-local splits are necessary in the component-splitting class.
The later six-occurrence witness performs such a forest repair differently:
the marked closure becomes 106 components, 154 macros and 3,815 owner
tokens, with zero internal D2/D3 defects.  Its exact connector catalogue has
412 geometric and 312 residence-clean directed arcs using 140 owner labels.
Required singleton component 77 has no clean incident arc in either
orientation.  Therefore its marked singleton cut is

\[
                         x(\delta(\{77\}))=0<1.
\]

This is stronger than owner-label Hall and kills the repaired fixed-port
one-owner face before conditioned residual flow.  The unconditioned
owner-to-port max flow of 10010/10010 is only the undamaged marginal case.

The complement needs a separate scope guard.  The repaired marked closure is
clean, but among the 883 nonempty unmarked macro components, 82 retain 320
strict internal D2 defects and no D3 defect.  Thus a global chronology using
the raw complementary macro words is already residence-infeasible.  A
two-bank construction must either rethread that complement or certify an
independent facet phase.

Occurrence choice must precede all these rows.  For each protected occurrence
state, fixing component orientations leaves exactly the four-matroid
common-independent-set rank described in the theorem.  Taking the minimum
path deficiency over occurrence states is therefore exact; treating an
occurrence move as a fixed-flow perturbation would be unsound because the
forest, marked set, endpoint ports, owner labels and residual demands can all
change.

The complete radius-one theorem gives 1,430 neighbours, 1,411 internally
clean states and 122 with no isolated marked component.  None has a connected
clean connector projection, and none satisfies the necessary at-most-two
forced-leaf condition.  The best weak-component shapes are ([102,2,2])
and ([103,2,2]); the minimum number of forced leaves is 21.  If a frozen
state is augmented by new socket edges, one edge can touch at most two forced
leaves, so at least

\[
                         \left\lceil(21-2)/2\right\rceil=10
\]

new socket adjacencies are necessary.  This is not an occurrence-distance
bound.  Only twelve states attain the three-component frontier; they are the
exact radius-two source family.  No path CNF is needed for the radius-one
no-go.

For the literal seventh move
`21006:(0,1121)->(0,4318)`, direct replay gives component shape
([102,2,2]), 22 forced leaves and tail--head matching number 103.
The Hall witness has eight left vertices
({47,52,66,73,75,78,92,97}) and five neighbours
({15,31,51,56,84}).  Hence the three independent socket lower bounds
are (2,10,2), and the exact maximum is ten.  At equality the ten added
edges must touch 20 distinct forced leaves and bridge both two-vertex
islands to the large component.  This verifies the theorem's stated
equality structure.

The common-cap statement is also correctly one-way: fixing a cap and pruning
to columns literally realized by it is sufficient.  If the cap is variable,
it must remain in the joint column state.  Provider counts or bounded span
alone do not lift marginal Hall.

## 6. Audited dependencies

```text
MATH_THEOREM_K17_MARKED_MACRO_COMPONENT_TWO_BANK_OBSTRUCTION_20260731.md
SHA-256 65819b0a7ef73a48729d14b7e20e944072cf7fc8ca1c732c21cd7361f5a9886a

scratch/k17_marked_macro_component_two_bank_obstruction_20260731.audit.json
SHA-256 c4a7e2477186247bdbdace01967426a1cf55db8bcacc99296b679c681451e259

scratch/k17_marked_macro_component_two_bank_obstruction_20260731.independent.json
SHA-256 b668fbc5e75a9ccd25c3571a9c4938f2a6167b0e66ca18d8c35c096afe90bdec

scratch/k17_sixswap_repaired_macro_forest_20260731.flow.json
SHA-256 004c782c5b7af630f3d30b704eed4a90c2431db7895cd7217d463216b7f9a283

scratch/audit_k17_sixswap_repaired_component_flow_gate_20260731.py
SHA-256 14b90b013dab73649b9b65097f14def799c2c4bbdb6fe8c0f60d362d8f7bf262

scratch/k17_sixswap_repaired_component_flow_gate_20260731.audit.json
SHA-256 90fbffaf6fc35c159ce81b4730f1d37b503bec49617bdda77cd2f435d92f14d6
payload 8fb977c1bb10ad904f4dcd2a904d92c7c3d5f2f9243d62822898bb13ec024a73

scratch/census_k17_two_bank_single_occurrence_swaps_20260731.py
SHA-256 0b2fa2802fb5562d453b8122864cbe0fe0c2c91aadd24d1b00afa3ccf0ce812d

scratch/k17_two_bank_single_occurrence_swaps_20260731.census.json
SHA-256 e9797343a3d6e841195b01b3541814562f8af8c6645f0d8e4795e2f0a9fa1d83

scratch/k17_sevenswap_premaster_macro_forest_20260731.flow.json
SHA-256 56f6701224913c1b3c09cedd1483595ef627d1bc946a87af43a8e73098dda0dc
payload 153644883597d6bd2f37f9f6271f7423f4db5302c304a83801bf66116566c5d7
```

The census JSON was enriched in place after its embedded payload field was
computed.  The audit therefore authenticates its current byte SHA and the
literal aggregate rows, not that stale embedded payload.  The pinned
seven-move flow has a valid independent payload digest.

The audit proves no `K17` word, no endpoint-changing socket, and no all-(k)
recurrence.
