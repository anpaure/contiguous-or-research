# The `K17` OPTIMAL28 packet path: conditioned Hall and the exact residual switch gate

Date: 2026-07-31  
Status: exact path/degree/Hall audit and connected owner/lower-`q1` port
factor; deep shadows, complementary residence and one common compiler are
not claimed

## 0. Verdict

The saved direct/one-optional packet master has a literal residence-clean
path through all `106` marked components.  It uses `28` pairwise-distinct
optional forest components and `133` pairwise-distinct pure-old-`U` owners.
The expanded marked owner word has length `4108` and has no internal `D2`
run below three and no internal `D3` run below four.

After conditioning on this exact path, the residual degree problem is
feasible.  The fixed macro-plus-packet graph is an acyclic forest with

```text
rank-eight port vertices                         6435
macro edges                                      1430
packet connector edges                            133
fixed forest components                          4872
remaining pure-U owners                           4872
residual port half-demand                         9744
residual demand profile                   0^691 1^1744 2^4000.
```

The exact conditioned incidence network has maximum flow

\[
                         9744/9744.                 \tag{0.1}
\]

Thus there is no conditioned marginal Hall obstruction.  A first,
deterministic integral maximum flow closes the ports into `17` cycles of
port sizes

\[
6381,5,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3.           \tag{0.2}
\]

This shows that max-flow saturation alone does not imply connectivity.  A
second exact max-flow run, with a different deterministic incidence order,
is already connected: attempt `86` of the frozen `300`-order list produces
one cycle directly and uses no post-flow switch.  Independent replay checks
all `4872` owner pairs, every port load, connectedness, and the unchanged
marked path.  The conditioned owner/lower-`q1` topology gate is therefore
closed for this packet witness.

The switch theorem below remains useful for other saturated flows.  A
rectangle joining two different current cycles merges them while preserving
every owner row and every port degree.  Hence the `17`-cycle replay would
require at least `16` such merging rectangles, and `16` would suffice for a
monotone legal merger sequence.

Conditional on obtaining a connected completion without changing the
marked word, the marked path is automatically one contiguous bank and its
complement is the other bank.  The `D2` scalar common-cap guard then has

\[
             a=4108,\qquad 7401-a=3293             \tag{0.3}
\]

units of slack.  Its two exact cross-bank sockets are

\[
 (18230,,18294,,18290),\qquad
 (6394,,22778,,22762),                              \tag{0.4}
\]

where each triple is `(marked endpoint port, residual U owner, complement
port)`.  This scalar margin and these literal sockets do not prove the
common-cap matching, residence of the complementary bank, or deep-shadow
coverage.

## 1. The fixed packet forest

Let

\[
 \mathcal T={ [15]\choose 8},\qquad
 \mathcal U={ [15]\choose 9}.
\]

The six-swap macro graph `M` is a linear forest on \(\mathcal T\) with `1430`
edges and therefore

\[
             c(M)=6435-1430=5005.                  \tag{1.1}
\]

Its port-degree profile is

\[
                 0^{4016}1^{1978}2^{441}.          \tag{1.2}
\]

The saved packet path visits `106` marked components and `28` optional
components.  These `134` original forest components are pairwise distinct.
Its `133` connector edges join consecutive components, so they form a tree,
indeed a path, on those `134` vertices.  Consequently every connector joins
two different current components and

\[
        c(M\cup P)=5005-133=4872.                  \tag{1.3}
\]

The connector labels are `133` distinct members of \(\mathcal U\); hence

\[
        |\mathcal U\setminus U(P)|=5005-133=4872.  \tag{1.4}
\]

For \(T\in\mathcal T\), define the conditioned residual demand

\[
 d_P(T)=2-\deg_M(T)-\deg_P(T).                     \tag{1.5}
\]

Literal reconstruction gives nonnegative demand at every port and the exact
profile in (0.1).  In particular,

\[
                  \sum_T d_P(T)=9744=2\cdot4872.   \tag{1.6}
\]

There are `234` ports used once by packet connectors, `16` ports used twice,
and no port used more than its residual capacity.  The `28` optional
components contain `160` rank-nine owner tokens in total.  Therefore the
marked word length is exactly

\[
                  3815+160+133=4108.               \tag{1.7}
\]

The first term is the owner content of the `106` marked components, the
second is the optional content, and the last is the connector content.

Every component `C` of the fixed forest is a path (an isolated port is the
length-zero case), so it has exactly two residual halfports:

\[
                    \sum_{T\in C}d_P(T)=2.          \tag{1.8}
\]

For a nontrivial path this is the pair of endpoint deficits; for an isolated
port it is the two units at that port.  Thus contracting the fixed forest
turns every degree-feasible residual pairing into a two-regular multigraph
on exactly `4872` vertices.  Loops are allowed in this contracted picture
and mean that one residual owner closes one fixed path by itself.

## 2. Exact conditioned Hall theorem

Put \(R=\mathcal U\setminus U(P)\).  Consider the network

\[
 s\longrightarrow U\longrightarrow T\longrightarrow t,
 \qquad U\in R,\quad T\in\mathcal T,\quad T\subset U,           \tag{2.1}
\]

with capacities `2`, `1`, and `d_P(T)`, respectively.

### Theorem 2.1 (conditioned incidence criterion)

There is a choice of two distinct incident ports for every `U in R`, using
each port `T` exactly `d_P(T)` times, if and only if

\[
 2|A|\le
 \sum_{T\in\mathcal T}
 \min\left(d_P(T),\,|\{U\in A:T\subset U\}|\right)             \tag{2.2}
\]

for every \(A\subseteq R\).

#### Proof

For a cut whose source-side owner set is `A`, minimizing independently over
the side of each port contributes

\[
 \min\left(d_P(T),|\{U\in A:T\subset U\}|\right).
\]

The source arcs of owners outside `A` contribute `2(|R|-|A|)`.  Thus every
cut has capacity at least `2|R|` exactly when (2.2) holds.  Max-flow/min-cut
gives a flow of value `2|R|`.  Since all capacities are integral, the flow
can be integral.  The unit middle arcs force the two ports of one owner to
be distinct.  Finally, equality of total source supply and total port
demand forces every port demand to be met exactly.  The converse follows by
counting the incidences used by any owner subset `A`.  \(\square\)

For the saved path the network has `4872` owner vertices, `6435` port
vertices, and `9*4872=43848` possible owner-port incidences.  The independent
replay obtains (0.1), so every inequality (2.2) holds.  This establishes
only degree feasibility; the theorem deliberately has no connectivity row.

## 3. From an integral flow to a port two-factor

Every residual owner `U` with selected ports `{S,T}` is a literal singleton
object joining `S` to `T`: both are rank-eight facets of `U`, and their union
is `U`.  Add all `4872` such object edges to \(M\cup P\).  Equations
(1.5)--(1.6) imply that every port has degree exactly two.  Hence the result
is a loopless two-regular object multigraph on all `6435` ports, namely a
disjoint union of cycles.

The marked packet path remains intact.  Every internal port of that path
already has degree two, so no residual object can enter it.  Only its two
end ports can meet the residual bank.  Therefore:

### Lemma 3.1 (automatic two-bank contiguity)

If a conditioned residual pairing makes the port two-factor connected, its
unique cycle contains the entire marked packet path as one contiguous
subpath.  Deleting the two cross-bank incidences leaves exactly the marked
path and one complementary path.

#### Proof

The fixed packet graph is a simple path.  Each internal vertex already has
fixed degree two and each endpoint has fixed degree one.  In any degree-two
completion, the complement therefore meets the fixed path exactly once at
each endpoint and nowhere internally.  A connected two-regular graph is one
cycle, so removing those two meeting edges gives the asserted two paths.
\(\square\)

This is the exact splice reduction: topology can be solved entirely on the
residual port factor.  It need not be imposed during the marked packet-path
optimization.

### Corollary 3.2 (the saved connected completion)

The assignment in
`scratch/ad_k17_opt28_residual_connected_bflow_20260731.json` satisfies all
conditioned owner and port rows and has one component.  Therefore it induces
one literal object cycle containing the fixed marked path contiguously.  An
independent reconstruction finds exactly two residual edges crossing the
marked-path vertex set, namely the two triples in (0.4).

The macro words contain `19305` distinct rank-nine owners and the `5005`
pure-old-`U` singleton objects contain the remaining owners.  Their union has
size

\[
                         19305+5005=24310.           \tag{3.1}
\]

The macro interiors supply `17875` distinct tagged rank-eight intersections,
while the port cycle supplies all `6435` untagged rank-eight intersections.
Thus a traversal of the connected object factor is a literal Hamilton cycle
on all rank-nine owners with every lower-`q1` colour exactly once.  This is a
carrier-level conclusion; no upper or deeper palette is inferred from it.

## 4. Exact residual incidence switches

Represent an integral residual flow by selected incidences
\(B\subseteq R\times\mathcal T\).  Suppose distinct residual owners `U,V`
currently select

\[
             \{A,S\}\subset {U\choose8},\qquad
             \{B,T\}\subset {V\choose8}.           \tag{4.1}
\]

Assume also

\[
 T\subset U,\qquad S\subset V,                     \tag{4.2}
\]

and that `(U,T)` and `(V,S)` are not already selected.  The **incidence
rectangle** replaces

\[
 (U,S),(V,T)\quad\hbox{by}\quad(U,T),(V,S).         \tag{4.3}
\]

### Lemma 4.1 (literal switch legality)

The rectangle (4.3) preserves:

1. two selected incidences at every residual owner;
2. the selected-incidence count at every port;
3. every fixed macro and marked-packet edge;
4. the sets of used rank-nine owners and rank-eight lower colours.

In the projected port graph it replaces the two object edges

\[
                 AS, BT\quad\hbox{by}\quad AT, BS.             \tag{4.4}
\]

If `AS` and `BT` lie in different current cycles, the rectangle merges
those two cycles into one.

#### Proof

Each of the four affected owner and port degrees loses and gains one.
Conditions (4.2) make the two new incidences literal facets of their assigned
owners.  No fixed incidence occurs in (4.3), so the packet path is untouched.
Deleting one edge from each of two cycles leaves two paths, with endpoint
pairs `(A,S)` and `(B,T)`.  The crossed edges `AT,BS` join those two paths
into one cycle.  \(\square\)

The lemma is exact for the port factor.  It does **not** say that the changed
complementary chronology preserves residence, upper shadows, or a selected
common-cap witness.

### Theorem 4.2 (dynamic and static merger criteria)

Let an integral conditioned pairing have `c` cycles.

1. Any sequence of incidence rectangles that produces one cycle has length
   at least `c-1`.
2. A sequence of exactly `c-1` legal rectangles, each joining two different
   cycles at the moment it is applied, produces one cycle.
3. A useful static sufficient certificate is a tree on the initial cycles
   whose tree edges carry legal rectangles and whose rectangle owner pairs
   are pairwise disjoint.  Applying the rectangles in a leaf-elimination
   order produces one cycle.

#### Proof

A two-edge switch changes the number of cycles by at most one, proving the
lower bound.  Lemma 4.1 proves the second assertion by induction.  For the
third, pairwise owner-disjointness means that applying one rectangle cannot
change a selected incidence used by another.  At each leaf-elimination step
the labelled rectangle still exists and joins the already merged leaf
subtree to a different current component.  The second assertion completes
the induction.  \(\square\)

For the replay (0.2), `c=17`; thus `16` is both the unavoidable switch count
and the target count for a monotone merger certificate.  The separately
saved connected assignment starts with `c=1`, so it needs zero rectangles.

Equivalently, without choosing a starting flow, one may use pair variables
`z_(U,{S,T})` and impose, in addition to the owner and port-degree rows, the
component cuts

\[
 \sum_{U,\{S,T\}:|\{S,T\}\cap X|=1}z_{U,\{S,T\}}\ge1            \tag{4.5}
\]

for every nonempty proper union `X` of fixed-forest components.  These cuts
are necessary and sufficient for connectedness and can be separated by the
connected components of an incumbent port factor.

## 5. Common-cap interface and exact boundary

The marked packet word has `a=4108` rank-nine tokens.  If a connected
completion also supplies the literal lower-rainbow Johnson cycle required
by the two-bank zipper, the complementary facet bank has `24311-a` tokens
and the depth-two row has length `24311`.  The scalar lower-cell guard from
the exact `D2` compiler theorem is

\[
                         a\le7401.                  \tag{5.1}
\]

Thus this witness has the positive scalar margin (0.3).  At each of the two
bank interfaces, exact inversion is checked by the four-row cap halo and
the crossing singleton/pair cell.  The switch construction above preserves
the marked bank but can change these complementary cap rows.  Consequently
the final switch/flow model must export, for each bank endpoint,

```text
endpoint port and incident residual owner,
two complementary owner rows on the outside,
the exact crossing lower colour,
the capped D2/D3 run state,
any preassigned singleton/pair common-cap cell.
```

No aggregate Hall or scalar slack substitutes for this finite interface.

## 6. Frozen evidence and scope

```text
scratch/k17_sixswap_macro_forest_20260731.flow.json
SHA-256 4e3129d2604d3e41c226efa3bea71a203180538710dd97272cc734e23412441b

scratch/ad_k17_sixswap_oneoptional_catalogue_20260731.json
SHA-256 b803899bbf07b3cbc82e995c9fd1f6231e6eba679d6a60e4a447cb36c08e71f2

scratch/ad_k17_sixswap_oneoptional_marked_path_20260731.result.json
SHA-256 b60341b5cee0de1884d3af6561d8247722bad879d7b5322ca21d94f60472e351

scratch/ad_k17_sixswap_oneoptional_marked_path_20260731.audit.json
SHA-256 beea4edbc17e8046a1bc39759e1284d57357ae0b05261b90004e27c54e9a8e4f

scratch/ad_k17_opt28_residual_connected_bflow_20260731.json
SHA-256 b3cbb0663409463cb24a2ed78db154cc88a042b633e979cba3506ba74e610ef6

scratch/audit_ad_k17_opt28_residual_connected_bflow_20260731.py
SHA-256 a6f306a8ac9885cf6556b2746d516f831b53bb1e93e8e8dd4a996a298a0d6c01

scratch/ad_k17_opt28_residual_connected_bflow_20260731.audit.json
SHA-256 95e8b27426d9ac62ccbe490a55c2a1e256e63faa1bc561a5d5a0462380870cfd
payload 05d8685b325abc3311732f032becf2c7f158776a83c6cb36f16fca56d23056f9

scratch/audit_ad_k17_optimal28_conditioned_hall_switch_gate_20260731.py
scratch/ad_k17_optimal28_conditioned_hall_switch_gate_20260731.audit.json
```

The first independent audit literally reconstructs the saved path and runs
one conditioned max-flow.  The first AD audit independently reconstructs the
resource and forest ledgers and authenticates that flow result without
duplicating the solve.  The second AD audit checks the connected assignment
directly, reverse/forward replays every saved rectangle (there are zero in
the connected witness), and verifies the two cross-bank sockets.  The
reported `OPTIMAL28` status and matching lower bound are CP-SAT solver scope,
not a proof-producing certificate; existence of the saved path is
independently replayed.

What is proved is:

* a literal clean `4108`-owner marked path;
* exact residual equality `4872` components = `4872` owners = `9744/2`
  half-demand;
* conditioned Hall/max-flow feasibility and a connected saturated pairing;
* one literal owner/lower-`q1` Hamilton carrier with the marked bank intact;
* an exact connectivity cut system and an exact cycle-merging switch lemma;
* positive conditional scalar common-cap slack `3293`.

What remains unproved is complementary residence, all upper/deeper shadows,
the two interface cap state, and one integral common-cap matching on this
connected carrier.  No `K17` word or claim about `nu(17)` follows from this
note.
