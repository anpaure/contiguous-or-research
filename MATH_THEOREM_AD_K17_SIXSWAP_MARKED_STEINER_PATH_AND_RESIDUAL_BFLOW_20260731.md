# The six-swap `K17` forest: marked Steiner packets and the exact residual `b`-flow gate

Date: 2026-07-31  
Status: exact conditional composition theorem and exact finite pre-master
obstruction; no `K17` carrier or word is claimed

## 0. Verdict

The six occurrence exchanges in

```text
scratch/k17_sixswap_macro_forest_20260731.flow.json
```

replace the old `108` independent nonflat blocks by a much better fixed
object.  The `108` required macros have closure

\[
       106\text{ macro-forest components},\qquad154\text{ macros},
                                                               \tag{0.1}
\]

and the literal concatenation inside every one of these components has no
internal depth-two run below three and no internal depth-three run below
four.  The marked owner bank has `3815` owner tokens.

This does **not** yet give a marked Hamilton path.  On the `212` oriented
marked states, the direct old-`U` catalogue has `412` geometric arcs and
only `312` residence-clean arcs, using `140` distinct old-`U` labels.
Marked component `77` has no incident clean direct arc.  Therefore the
direct `105`-connector marked-only master is infeasible before owner-label,
residual-flow, or connectivity constraints are imposed.

The smallest complement enlargement is already positive.  Identifying the
isolated object invariantly as the marked component containing macro `18`,
the complete one-internal-component census gives `110` clean,
capacity-feasible packets, through `61` different unmarked components and
to `53` different marked targets.  Hence its minimum number of internal
complement components is exactly one.  A canonical packet is

\[
 \begin{array}{c}
 C_{18}\ (22835\to16638)\\[-2mm]
 \xrightarrow{,U=16639,}\{16623\}
 \xrightarrow{,U=18671,}C_{280}\ (18669\to18869),
 \end{array}                                               \tag{0.2a}
\]

where `{16623}` is an isolated port component with empty owner word.
The expanded word has `111+2+21=134` distinct owner tokens and passes the
literal `D2/D3` replay.  Its two old-`U` labels are distinct; port `16623`
has macro degree zero and receives two incidences, while ports `16638` and
`18669` have macro degree one and receive one incidence each.

Globally, the complete direct/one-optional packet master is also solved.
It has `11532` candidates (`312` direct and `11220` one-optional), `2133`
distinct optional components, and `1286` old-`U` labels.  The exact CP-SAT
optimum in this scoped catalogue is

\[
                       \boxed{s_{\le1}=28}.             \tag{0.2b}
\]

The witness is one path through all `106` marked components, uses `28`
distinct optional components and `133=105+28` distinct old-`U` connectors,
and expands to `4108` distinct owners with no `D2/D3` defect.  Independent
literal replay passes.  Its exact conditioned residual incidence flow also
saturates `9744/9744`; one deterministic pairing has `17` cycles, of sizes

\[
                 6381,5,4,4,4,4,3^{11}.              \tag{0.2c}
\]

Thus degree Hall survives this marked path.  Connected pairing remains an
additional exact gate.  The optimum `28` is for the complete catalogue in
which each marked-to-marked packet has at most one internal complement
component.  A packet with two or more internal components is outside that
optimization and could in principle lower the total optional count.

The direct undirected support has component sizes

\[
                         99,2,2,2,1,                 \tag{0.2d}
\]

with one isolated vertex and `23` direct-degree-one vertices.  Since a
Hamilton path has only two global endpoints, these vertices force at least
`23` optional incidences and hence at least `12` optional packet edges.
This is a solver-free but nonsharp floor; the strengthening from `12` to
`28` currently comes from the exact CP-SAT optimum/bound, not from a saved
DRAT/LRAT certificate.

The exact replacement is a **marked Steiner packet path**: consecutive
marked components may be joined through unused unmarked macro components.
If the selected marked path uses `s` such optional components, then it uses
exactly

\[
                         105+s                              \tag{0.2}
\]

old-`U` connector owners.  This is capacity-neutral.  After fixing the
path, the three residual quantities are all equal:

\[
 \#\text{remaining macro components}
 =\#\text{remaining old-}U\text{ owners}
 ={1\over2}\sum_Td(T)
 =4900-s.                                                   \tag{0.3}
\]

Theorem 4.1 below gives a necessary-and-sufficient joint model for the
Steiner path, exact owner/lower-`q1` preservation, residual degree
completion, and connected port closure.  It cleanly separates the current
positive result from the remaining gates: existence of the packet path,
conditioned (not unconditioned) Hall, quotient connectivity, upper/deeper
service, and one common-cap compiler.

## 1. Fixed objects

Put

\[
 {cal T}=\binom{[15]}8,\qquad {cal U}=\binom{[15]}9.
\]

The rebuilt `A/X/Y` macro forest is a loopless linear forest `M` on the
port deck `T`.  Its `1430` macro edges expand to `19305` pairwise-distinct
rank-nine child owners.  It has

\[
 |{cal C}(M)|=6435-1430=5005=|{cal U}|                 \tag{1.1}
\]

components.  Its port-degree profile is

\[
             \deg_M(T):\qquad0^{4016}1^{1978}2^{441}.   \tag{1.2}
\]

Consequently

\[
 \sum_{T\in{cal T}}(2-\deg_M(T))
 =2\cdot5005=10010.                                      \tag{1.3}
\]

Every nontrivial component `C` of `M` is a port path.  Choosing an
orientation gives an ordered pair of endpoint ports `(h_C,t_C)` and its
literal expanded owner word `W_C`.  A degree-zero port is a trivial
component: its word is empty, it has one port rather than two different
ends, and a traversal through it consumes the two residual incidences at
that same port.  This convention is needed because (1.2) contains `4016`
isolated ports.  Let `R` be the set of the `106` marked components in
(0.1); all marked components are nontrivial.

An old-`U` edge is a triple

\[
                  (S,U,T),\qquad S,T\in{cal T},\quad
                  S\ne T,\quad S\cup T=U\in{cal U}.     \tag{1.4}
\]

Equivalently, `S` and `T` are two distinct rank-eight facets of `U`.
Expanding (1.4) inserts the one owner `U` between the two incident macro
words.  The two new lower colours are literally `S` and `T`.

## 2. Residence-clean packet paths

For a linear owner word `W`, call it **clean** when every internal positive
coordinate run has length at least three and the adjacent-union word

\[
                     D(W)_i=W_i\cup W_{i+1}             \tag{2.1}
\]

has every internal positive run of length at least four.  This is the exact
local `D2/D3` condition used here.  Boundary runs are retained as capped
prefix/suffix state until the word is joined.

A **complement packet** from an oriented marked component `(C,epsilon)` to
an oriented marked component `(C',epsilon')` is a simple quotient path

\[
 C=C_0\;\xrightarrow{U_0}\;C_1\;\xrightarrow{U_1}\;\cdots
 \xrightarrow{U_s}\;C_{s+1}=C'                         \tag{2.2}
\]

such that

1. `C_1,...,C_s` are pairwise-distinct unmarked components; a trivial
   component contributes its single port twice and its empty owner word;
2. every arrow is a literal old-`U` edge (1.4) between the appropriate
   oriented endpoint ports;
3. the labels `U_0,...,U_s` are distinct;
4. the expanded owner word

\[
 W_{C_0}^{\epsilon},U_0,W_{C_1}^{\epsilon_1},U_1,\ldots,
 U_s,W_{C_{s+1}}^{\epsilon'}                            \tag{2.3}
\]

   is clean.

The packet records its internal-component set, old-`U` label set, port
incidences, endpoint orientations, and literal capped run transition.
The case `s=0` is a direct marked-to-marked arc.

### Lemma 2.1 (exact packet decomposition)

A simple clean port path which contains every marked component decomposes
uniquely, after cutting at the marked components, into complement packets.
Conversely, a directed marked path of complement packets whose internal
component sets and old-`U` label sets are pairwise disjoint expands to one
simple port path through every marked component, provided its port loads do
not exceed `2-deg_M` and the recorded capped run transitions compose to an
accepting state.

#### Proof

Cutting at successive marked components leaves simple subpaths with only
unmarked internal components; these are exactly (2.2).  Simplicity makes
their internal resources disjoint, and literal expansion gives (2.3).

In the other direction, glue the packets at their common marked endpoints.
Resource disjointness prevents a repeated component or owner.  The port-load
condition prevents degree three.  Composition of the literal run transitions
is precisely direct replay of the expanded word, so it is equivalent to
cleanliness.  No marginal run count is used.  \(\square\)

Thus the packet catalogue is not a heuristic neighbourhood.  Taking **all**
simple packets gives an exact finite representation of the marked/complement
path problem.  A bounded packet catalogue is only a sufficient subclass and
must be labelled as such.

## 3. Capacity neutrality

### Lemma 3.1 (tree-neutral connector identity)

Let a simple selected path contain all `106` marked components and exactly
`s` optional unmarked components.  Then it has `106+s` component vertices
and exactly `105+s` old-`U` connector edges.  Let `P` be those edges and put

\[
 d_P(T)=2-\deg_M(T)-\deg_P(T),
 \qquad {cal U}_P={\cal U}\setminus\{\text{labels used by }P\}. \tag{3.1}
\]

If `d_P(T)>=0` for every `T`, then

\[
 \begin{aligned}
 |{cal C}(M\cup P)|&=5005-(105+s)=4900-s,\\
 |{cal U}_P|&=5005-(105+s)=4900-s,\\
 \sum_Td_P(T)&=10010-2(105+s)=2(4900-s).
 \end{aligned}                                             \tag{3.2}
\]

#### Proof

A path on `106+s` old components is a tree and hence uses `105+s` edges,
each joining two previously different components.  This gives the first
identity.  Distinct connector labels give the second.  Each connector uses
one unit of capacity at each of two port vertices, giving the third.  \(\square\)

For `s=0`, (3.2) is the audited ledger

```text
marked connectors                         105
marked owner tokens                      3920 = 3815+105
remaining old-U owners                   4900
remaining port half-demand               9800
components after the marked path         4900.
```

The equality is preserved for every `s`.  Optional components do not create
a scalar capacity penalty.  Their difficulty is correlation: which ports,
which owner labels, which residual Hall face, and which component cuts remain.

## 4. Exact joint path and residual-completion theorem

Fix the complete packet catalogue of Section 2.  For each packet `p` use a
Boolean variable `x_p`.  For every unused-owner candidate pair use

\[
 z_{U,\{S,T\}}\in\{0,1\},
 \quad U\in{cal U},\quad S,T\subset U,quad |S|=|T|=8,
 \quad S\ne T.                                         \tag{4.1}
\]

The `x` variables must select one directed path through all marked
components: one orientation per selected component, one start, one end,
indegree and outdegree one away from them, no directed subtour, pairwise
disjoint packet-internal component sets, and consistent capped run state.
Equivalently one may use the standard path-cover degree rows plus order
variables.  Every marked component is forced selected; an unmarked component
is selected iff it lies internally in one selected packet.

More explicitly, because packet endpoints are marked, exactly `105` packet
variables are selected.  Their directed endpoint graph has indegree/outdegree
profile

\[
 (0,1)^1,(1,1)^{104},(1,0)^1,                     \tag{4.0}
\]

with one consistent orientation at each marked vertex and no directed
cycle.  If `I(p)` and `L(p)` denote the internal complement components and
old-`U` labels of packet `p`, respectively, the resource rows are

\[
 \sum_{p:C\in I(p)}x_p\le1\quad(C\notin R),
 \qquad
 \sum_{p:U\in L(p)}x_p\le1\quad(U\in{cal U}).    \tag{4.0a}
\]

The exact capped-run automaton is propagated along the selected packet
order; accepting at the terminal state is equivalent to direct `D2/D3`
replay.  Thus (4.0)--(4.0a) are a finite path master, not a fractional or
rankwise relaxation.

For a packet `p`, let `E(p)` be its set of literal old-`U` edges.  Write
`inc_T(e)` for the number (`0` or `1`) of endpoints of edge `e` equal to
`T`.  Impose

\[
 \sum_{p}\sum_{e\in E(p)}inc_T(e)x_p
 +\sum_U\sum_{\{S,T'\}\ni T}z_{U,\{S,T'\}}
 =2-\deg_M(T)                                           \tag{4.2}
\]

for every port `T`, and

\[
 \sum_p[U\text{ labels an edge of }p]x_p
 +\sum_{\{S,T\}\subset U}z_{U,\{S,T\}}=1             \tag{4.3}
\]

for every old owner `U`.  Packet resource-disjointness makes the first sum
in (4.3) zero or one.

Let `kappa(T)` be the component of the fixed macro forest `M` containing
port `T`.  For every nonempty proper set `A` of the `5005` macro components,
impose the quotient cut

\[
 \sum_p\#\{e\in E(p):e\text{ crosses }\delta(A)\}x_p
 +\sum_{U,\{S,T\}:|\{\kappa(S),\kappa(T)\}\cap A|=1}
       z_{U,\{S,T\}}
 \ge1.                                                   \tag{4.4}
\]

In (4.4), an edge crosses when exactly one endpoint component lies in `A`.
The packet path rows already imply many of these cuts; retaining the full
family gives an exact lazy separator.

### Theorem 4.1 (marked Steiner path plus connected residual `b`-flow)

Equations (4.2)--(4.4), together with the exact packet-path rows, are
feasible if and only if the six-swap macro forest admits an extension with
all of the following properties:

1. every one of the `19305` macro owners and every old-`U` owner occurs
   exactly once;
2. every rank-eight lower colour occurs exactly once;
3. the marked closure lies on one literal clean owner path, possibly routed
   through optional unmarked macro components; and
4. the completed port graph is connected, hence is one cycle.

#### Proof

Given a physical extension, contract each fixed macro component.  Cutting
its distinguished clean marked path at marked components gives the packet
variables by Lemma 2.1.  Every old-`U` owner is either on that path or in the
residual completion, giving (4.3).  Degree two at every port gives (4.2).
Connectivity gives every cut (4.4).

Conversely, expand the selected packets and every selected pair (4.1).
The path rows and Lemma 2.1 give the clean marked path.  Equation (4.3) uses
each old-`U` owner exactly once; the fixed macros already partition all
other child owners.  Equation (4.2) makes every port degree two.  At a
degree-two port the two incident expanded owner blocks meet in that literal
rank-eight facet, so every port colour is used once.  The internal macro
colours were already pairwise distinct and disjoint from the port deck.
Finally (4.4) makes the quotient by the connected macro components
connected.  A finite connected two-regular graph is one cycle.  \(\square\)

The theorem is an owner/lower-palette and topology theorem.  It does not say
that the final cyclic owner chronology is globally flat-resident.  The
nonflat compiler uses the distinguished marked path, and its complementary
rail, upper shadows, envelopes, and common cap still require separate rows.

## 5. Fixed-path Hall and why the unconditioned pass is insufficient

For a fixed marked packet path `P`, discard the packet-used owners and put
`d_P` as in (3.1).  Ignoring connectedness, the residual degree equations
have an integral solution if and only if

\[
 \boxed{
 2|A|\le\sum_{T\in{cal T}}
 \min\bigl(d_P(T),|N(T)\cap A|\bigr)
 \quad\text{for every }A\subseteq{cal U}_P.}       \tag{5.1}
\]

Here `N(T)={U in U_P:T subset U}`.

### Proof

Use source-to-owner capacity two, unit owner-to-facet arcs, and
facet-to-sink capacity `d_P(T)`.  For a fixed source-side owner set `A`,
minimizing over the side of each facet contributes
`min(d_P(T),|N(T) intersection A|)`.  Max-flow/min-cut and integral
capacities prove (5.1).  \(\square\)

The deterministic unconditioned network for the six-swap forest has value

\[
                         10010/10010.               \tag{5.2}
\]

This checks only `P=emptyset`.  A selected packet path deletes owner labels
and port capacities in a correlated way, so (5.2) neither implies (5.1) for
that path nor supplies the pairing/connectivity cuts (4.4).  Correct Benders
order is:

1. choose a resource-disjoint marked packet path;
2. recompute `U_P,d_P` and separate (5.1);
3. if degree-feasible, solve or separate the pair-variable cuts (4.4).

Using only incidence-flow variables in the last stage is insufficient:
connectivity depends on which two facets of one owner are paired.

The unrestricted pair formulation has at most

\[
                 5005\binom92=180180                 \tag{5.3}
\]

`z` variables, `6435` port-degree rows and `5005` owner rows.  The quotient
cuts are best separated lazily on `5005` fixed macro components.  Packet
variables are generated only for literal clean complement paths; this keeps
the marked-path master separate from, but exactly coupled to, the residual
pairing model.

## 6. The first exact obstruction and the next finite catalogue

The complete direct marked-to-marked census is

```text
oriented marked states                   212
geometric direct arcs                    412
residence-clean direct arcs              312
distinct old-U labels                    140
zero-incident marked components            1  (component 77).
```

Therefore no direct `105`-arc marked Hamilton path exists.  This conclusion
is solver-free once the literal arc catalogue is reconstructed: an isolated
vertex cannot lie on a path through all marked vertices.  Owner-label
all-different, conditioned Hall, and connectedness can only remove further
solutions.

The minimal local enlargement is now closed: zero internal complement
components give no clean incident packet, while one internal component gives
`110`.  The complete radius-one census is

```text
geometric rows                            172
equal-U rows rejected                       9
port-capacity rows rejected                  0
residence rows rejected                     53
clean capacity-feasible packets            110
distinct internal complement components     61
distinct marked target components           53
internal macro-count profile          0^76 1^31 2^3.
```

The `0^76` class uses an isolated port component exactly as in (0.2a); it
does not use an optional owner or macro, but it is still one component of
the fixed quotient and consumes both of that port's residual incidences.

Every packet must export

```text
(marked endpoints and orientations,
 ordered internal unmarked components,
 ordered old-U labels and port pairs,
 exact capped D2/D3 transition,
 port-incidence vector).
```

Theorem 4.1 is the complete global test.  The positive packet (0.2a) removes
the direct-graph isolation but is not sufficient: it must participate in a
full resource-disjoint marked path whose conditioned residual Hall and
quotient cuts pass.  If a global marked path uses this one optional
component and no others, (3.2) specializes to

\[
 \#U_{\rm path}=106,\qquad
 |{cal U}_{\rm rem}|=4899,\qquad
 \sum_Td(T)=9798,\qquad
 |{cal C}_{\rm rem}|=4899.                         \tag{6.1}
\]

## 7. Frozen evidence and scope

Primary repaired forest:

```text
scratch/k17_sixswap_macro_forest_20260731.flow.json
SHA-256 4e3129d2604d3e41c226efa3bea71a203180538710dd97272cc734e23412441b
payload f1ab56555d744d2e527325c8617c2af1ee0f463ad13666f153d56efc588624db
```

Independent deterministic pre-master audit:

```text
scratch/audit_k17_sixswap_repaired_component_flow_gate_20260731.py
SHA-256 14b90b013dab73649b9b65097f14def799c2c4bbdb6fe8c0f60d362d8f7bf262

scratch/k17_sixswap_repaired_component_flow_gate_20260731.audit.json
SHA-256 f4ef27f5cff0da81552ab8025738de36e03ba1ec38789c36432401cb1a621ea6
payload aeb9f4741fc9553fa44594bfe0a31615c8a27fa34e4b1257bfc9adb9df2b3b5b
```

The audit verdict is deliberately `FAIL_SIXSWAP_PREMASTER_GATE`, because
the direct catalogue isolates component `77`.  The forest/residence and
unconditioned-flow subchecks pass.  No labelled Steiner path, conditioned
residual flow, connected completion, upper/deeper coverage, staircase, or
common-cap compiler is asserted here.

Exact minimal local bridge audit:

```text
scratch/audit_ad_k17_sixswap_one_steiner_bridge_20260731.py
SHA-256 7d88ed612f3a2a2b7f0f489b2e697f67808df88cf0f0573029c244978c57b8c8

scratch/ad_k17_sixswap_one_steiner_bridge_20260731.audit.json
SHA-256 a494fe8cff0632552fdbea87062f03a4e5f5ea14d54129a2e9eb0de4695a3ca7
payload f1f100988c993d28c761be2b5b1ec2669d8c3150580d34d28b583c867ac51b82
```

This last audit is complete only for packets with exactly one internal
unmarked forest component incident with macro `18`.  Its positive witness
settles that local minimum, not the global path master.

Complete direct/one-optional catalogue and exact path solver:

```text
scratch/solve_ad_k17_sixswap_oneoptional_marked_path_20260731.py
SHA-256 6f151aab87eae0df6be0ee9d1fbbcb0d131df9f7c28ee580250216cd06e52444

scratch/ad_k17_sixswap_oneoptional_catalogue_20260731.json
SHA-256 b803899bbf07b3cbc82e995c9fd1f6231e6eba679d6a60e4a447cb36c08e71f2
payload 58beedb46ec289b1059b11c095fc86e1e174fab8ad150a854c2c53eb7fe5ea0b

scratch/ad_k17_sixswap_oneoptional_marked_path_20260731.result.json
SHA-256 b60341b5cee0de1884d3af6561d8247722bad879d7b5322ca21d94f60472e351
payload 2440ee4a506932c4e7903dc327a6c8445c5c3c7b310c0e748d4520566c14ffae
```

The one-worker H100 CP-SAT run returned `OPTIMAL`, objective and best bound
both `28`, in `6.2567` seconds.  This is an exact solver result but not a
proof-producing CNF/DRAT certificate.

Independent witness, capacity and conditioned-flow replay:

```text
scratch/audit_ad_k17_sixswap_oneoptional_path_result_20260731.py
SHA-256 e26dbdd1c42e64331217e19e043ae20f685577b5f9ff9086a2e4ef4e68409d0a

scratch/ad_k17_sixswap_oneoptional_marked_path_20260731.audit.json
SHA-256 beea4edbc17e8046a1bc39759e1284d57357ae0b05261b90004e27c54e9a8e4f
payload f344a14ce0c89ecc377ffe58f4c4a5a69a0208d8645d1ff78e207fd4ac0a48de
```

This closes the abstract marked path and conditioned degree Hall only on the
direct/one-optional six-swap face.  It does not close the `17` residual
cycles, upper/deeper palettes, the complementary physical phase interface,
or the common-cap compiler.

Independent reconstruction of the complete `11532`-packet key set, CP model,
solver log and path witness:

```text
scratch/audit_ad2_k17_sixswap_full_radius1_steiner_path_20260731.py
SHA-256 d8f1703b97460306aaeb685f069b6b614e15d312fa97a9532080580771029eb9

scratch/ad2_k17_sixswap_full_radius1_steiner_path_20260731.audit.json
SHA-256 9b000c00751cb72da0444a46eb7c76135790304e2e18b5b59400db0d192a1f9f
payload c00441621cf7bdf1653b562f5be804b114720b4042d41e3dc059550425d7bd5a
```

Its verdict is `PASS_INDEPENDENT_COMPLETE_RADIUS1_WITNESS_AND_MODEL_AUDIT`.
It explicitly records the lack of a proof-producing certificate for the
`<=27` face.
