# Thread D: one-copy TPC coloured-Euler rounding—exact lattice gate and determinant-two obstruction

Date: 2026-08-01  
Status: exact reduction, an unconditional smallest literal obstruction to
automatic rounding, and a TU fixed-tail subclass.  This note assumes the
private-label pull-clock stationary fractional circulation.  The exact
`k=4` full-owner instance refutes a universal zero-bridge rounding theorem;
it does not refute bounded-sidecar rounding or a Boolean-specific absorber
at the remaining parameters.
It is an independent obstruction audit for
`MATH_THEOREM_THREAD_D_TPC_ONE_COPY_COLOURED_EULER_ROUNDING_20260801.md`.

## 0. Outcome

Let `D=(V,E)` be the literal order-`d` de Bruijn digraph and let
`E_T subset E` be the trace fibre of the rank-`r` owner `T`.  The fractional
TPC theorem gives a stationary point in

\[
 \sum_{e\in E_T}x_{T,e}=1,\qquad Bx=0,\qquad x\geq0,               \tag{0.1}
\]

where `B` is the head-minus-tail incidence matrix.  The one-copy problem is
not an ordinary network-flow rounding.  It asks for

\[
 x_{T,e}\in\{0,1\},\qquad
 \sum_{e\in E_T}x_{T,e}=1,qquad Bx=0,                            \tag{0.2}
\]

together with literal boundary pins and connected support (or bounded
route-inspection charge).

The matrix obtained by appending the owner-partition rows to `B` is not
totally unimodular.  The smallest owner fibre already contains the
determinant-two matrix

\[
             \begin{pmatrix}1&1\\-1&1\end{pmatrix}.              \tag{0.3}
\]

More decisively, the actual triangular instance `(k,r,d)=(4,2,1)` has an
exact private-clock fractional solution but no balanced one-copy selection:
one-copy selection orients every edge of `K_4`, and every vertex retains odd
degree three.  Thus fractional TPC stationarity alone does not imply (0.2).
The same literal construction at `(r,d)=(2,1)` for every even `k` has sharp
open/circuit route costs `k/2-1` and `k/2`, so generic bounded-sidecar
rounding is false as well.  This infinite family is not claimed to lie on
the central-rank/deadline slice when `k>4`.

The exact surviving gate is a discrete Minkowski-sum/lattice condition,
followed by a graphic support condition.  A useful positive island remains:
after an integral tail is fixed for every owner, the remaining head choice is
a bipartite `b`-matching and is TU.  What fails in general is the simultaneous
choice of both tail and head (and then connectivity).

## 1. Exact pinned route-inspection model

For an edge `e=u->v`, put

\[
                         \partial e={\bf1}_v-{\bf1}_u.             \tag{1.1}
\]

Let `p` be a fixed multiset of boundary/comparator edges, and let `b` be an
uncoloured bridge multiset.  If the final word is an open Euler trail from
`s` to `t`, then the exact balance equation is

\[
 \sum_T\partial e_T+\partial p+\partial b
                     ={\bf1}_t-{\bf1}_s.                          \tag{1.2}
\]

The positive support of the selected, pinned and bridge edges must be weakly
connected.  Conversely, (1.2) plus weak connectivity is sufficient by the
directed Euler theorem.  Therefore a one-copy realization with at most `C`
route-inspection edges exists if and only if there are

* one `e_T in E_T` for every owner;
* a nonnegative integral `b` with `|b|<=C`;
* endpoints `s,t` compatible with the boundary pins;
* (1.2) and weak connectivity.

This is the pinned specialization of the exact `chi` theorem in
`MATH_THEOREM_BOUNDED_CHAIN_TRACE_EULER_SERIALIZATION_AND_SIDECAR_DISTANCE_20260801.md`.
Before pinning, the boundary permutation/root must be selected as one
correlated configuration.  If `u_pi` selects root `pi`, its owner usage,
target vector, fixed boundary arcs and endpoint pair must all be gated by
the same `u_pi`.  Replacing this by independent boundary marginals is a
strict relaxation.  Likewise, an adjacent comparator passage is a
successor-pair constraint, not merely two selected edges; it must be
contracted to a protected macroedge or encoded by transition variables.
It separates three issues which must not be merged:

1. one-copy coloured integrality;
2. state balance (possibly after the pinned sidecar);
3. connectivity/overlap cost.

When `p=b=0` and `s=t`, (1.2) has an equivalent combinatorial form: the
chosen owner-coloured arcs decompose into directed cycles, with every owner
colour appearing exactly once in the whole cycle family.  Thus one-copy
balance is an **owner-rainbow directed cycle factor**, not merely an Euler
flow with integral capacities.  Connectedness asks that the positive
support of this cycle family be connected; it is not implied by the cycle
decomposition.

## 2. The exact additive and congruence obstruction

Ignore connectivity momentarily and include every protected pin statistic in
an integral signature `sigma(e)`.  Put

\[
 a(e)=(\partial e,\sigma(e))\in L,
 \qquad A_T=\{a(e):e\in E_T\},                                  \tag{2.1}
\]

where `L` is the corresponding integer lattice.  After moving fixed pins
and endpoints to the right side, call the required vector `q`.

### Theorem 2.1 (exact one-copy additive gate)

The owner/palette/state/pin rows have a one-copy solution if and only if

\[
                            q\in\sum_T A_T.                       \tag{2.2}
\]

The fractional TPC point proves only

\[
                            q\in\sum_T\operatorname{conv}A_T.    \tag{2.3}
\]

Consequently the precise algebraic assertion still needed is integer
decomposition/normality at this one-copy degree.  It is not a consequence of
the network total unimodularity of `B`.

#### Proof

Choosing one edge from owner `T` chooses one vector of `A_T`; summing the
constraint signatures gives (2.2), and the converse reads the selected edge
from every summand.  Replacing each finite set by its convex hull gives
exactly the fractional owner simplex, proving (2.3). \(\square\)

If `A_0` is the signature set of permitted uncoloured route edges, the
exact algebraic relaxation with at most `C` such edges is

\[
 q\in\sum_T A_T+
       \bigcup_{0\le j\le C}\underbrace{(A_0+\cdots+A_0)}_{j\text{ times}}.
\]

Weak connectivity remains additional.  This is the finite bounded-absorber
target: at most `C` uncoloured columns must move the one-copy Minkowski sum
onto the required lattice point.

Every homomorphism `phi:L->Z/gZ` gives a proof-safe obstruction:

\[
 \phi(q)\notin\sum_T\phi(A_T)\quad\Longrightarrow\quad
                         \text{one-copy infeasible}.              \tag{2.4}
\]

For a state cut `U subset V`, the integer functional is

\[
 \kappa_U(e)={\bf1}_{\operatorname{head}(e)\in U}
             -{\bf1}_{\operatorname{tail}(e)\in U}.              \tag{2.5}
\]

Thus even one cut has the exact necessary condition

\[
 q_U\in\sum_T K_T(U),\qquad
 K_T(U)=\{\kappa_U(e):e\in E_T\}\subseteq\{-1,0,1\}.             \tag{2.6}
\]

Fractional Hall sees only the interval/convex-hull version of (2.6).  If all
flexible sets on a cut are `{-1,+1}`, (2.6) retains a parity condition which
the fractional cut loses.

There is also an exact quantitative discrepancy ledger.  For a one-copy
choice `z` together with fixed pins `p`, put

\[
 D(z)=\sum_v\bigl(\operatorname{out}_{z+p}(v)
                       -\operatorname{in}_{z+p}(v)\bigr)_+
     ={1\over2}\|\partial(z+p)\|_1.                              \tag{2.7}
\]

One added edge can decrease `D` by at most one.  Therefore every open-trail
completion uses at least `D(z)-1` route edges, and every circuit completion
uses at least `D(z)`.  After minimizing over owner choices compatible with
the protected pins, this is the precise first flow-discrepancy obstruction
to `O(1)` route inspection.  State distance and support cuts can only raise
the cost.

### Conditional pull-clock cocycle

Suppose, additionally, that the literal TPC state support admits a genuine
global phase map

\[
 c:V\longrightarrow\mathbb Z/n\mathbb Z,qquad
 c(\operatorname{head}e)-c(\operatorname{tail}e)=1               \tag{2.8}
\]

for every selectable owner trace.  Then every one-copy pinned trail obeys

\[
 |\mathcal O|+\omega(p)+\omega(b)
                  \equiv c(t)-c(s)\pmod n,                       \tag{2.9}
\]

where `|O|=binom(k,r)` and `omega` is the edge voltage induced by `c`.
In particular, a bridge-free Euler circuit requires

\[
                              n\mid\binom{k}{r}.                 \tag{2.10}
\]

Equation (2.9) is an exact obstruction **only after** (2.8) is proved on
literal states.  Owner-local phase names do not define a global state
potential when the same literal state occurs in different owner fibres.
This qualification is essential for the private-label TPC support.

## 3. Literal counterexamples

### The actual triangular `k=4` obstruction

More generally, let a depth-one pure-private owner family be the edge set of
a graph `G` on singleton states, with the two orientations available for
each owner edge.  The half-half point is always a stationary fractional
circulation.  A one-copy balanced selection is exactly an Eulerian
orientation of `G`, and therefore exists if and only if every vertex of `G`
has even degree.  If `G` is connected, a one-copy open trail exists if and
only if it has zero or two odd-degree vertices.  Indeed,

\[
 \deg_G(v)=\operatorname{out}(v)+\operatorname{in}(v),\qquad
 \operatorname{div}(v)=\operatorname{out}(v)-\operatorname{in}(v),
\]

have the same parity, and the converse is Euler's orientation theorem.
Thus fractional splitting erases an exact odd-degree boundary.

Take `(k,r,d)=(4,2,1)`.  The owners are the six pairs of `[4]`.  For every
owner `{u,v}`, use its two private-clock traces

\[
                          {u}\longrightarrow {v},qquad
                          {v}\longrightarrow {u}.                 \tag{3.1}
\]

Give each direction total weight `1/2`, split as marked weight `1/3` and
unmarked weight `1/6`.  Every owner has mass one; every literal singleton
state has incoming and outgoing mass `3/2`; and every singleton target has
marked load `3(1/3)=1`.  This is the exact triangular marked-trace point
`b_1=0,q_1=2/3`.

A one-copy selection orients the six edges of `K_4`.  At every state the
underlying selected degree is three, so its divergence is odd.  It can be
neither zero at all four states nor nonzero at exactly two states.  Hence
there is no one-copy Euler circuit and not even an open Euler trail before
bridges.

The exact owner-plus-three-independent-balance matrix has a displayed
`9 x 9` minor of determinant `-8`.  Route inspection sharply distinguishes
the conclusions: two duplicate edges are necessary and sufficient for an
Euler circuit, while one is necessary and sufficient for an open Euler
trail.  Thus the actual `k=4` obstruction kills exact balanced rounding, but
does not kill an additive-one open serialization.

The exact 64-orientation audit is

`scratch/audit_threadD_tpc_onecopy_k4_parity_20260801.py`,

with payload

`scratch/threadD_tpc_onecopy_k4_parity_20260801.audit.json`.

### The literal even-`k` route family

For every even `k>=4`, keep `r=2,d=1,b_1=0` and all pair-owners.  Give each
orientation total mass `1/2`, marked mass `1/(k-1)`, and unmarked mass
`(k-3)/(2(k-1))`.  Every owner has mass one, every singleton state has
incoming and outgoing mass `(k-1)/2`, and every singleton target receives
marked load `(k-1)/(k-1)=1`.  The support is the connected bidirected `K_k`.

Every one-copy selection is an orientation of `K_k`, so all `k` state
divergences are odd.  An open trail must toggle at least `k-2` of these
parities and a circuit all `k`; one route arc toggles at most two.  This gives
lower bounds `k/2-1` and `k/2`.  They are attained by adding respectively a
matching on all but two vertices and a perfect matching, then applying the
undirected Euler-trail/Euler-circuit orientation theorem.

The independent exact checker
`scratch/audit_threadD_tpc_evenk_route_obstruction_20260801.py` constructs
and replays the sharp witnesses for `k=4,6,8,10,12`.  Its payload is
`scratch/threadD_tpc_evenk_route_obstruction_20260801.audit.json`.

### The minimal determinant-two owner fibre

Take `d=1`, one rank-two owner `T={a,b}`, and the two admissible traces

\[
 e_+=(\{a\},\{b\}),\qquad e_-=(\{b\},\{a\}).                    \tag{3.2}
\]

They are the two arcs between the literal states `{a}` and `{b}`.  Give
each weight `1/2`.  Owner mass is one and literal divergence is zero.

Keeping the owner row and one independent state-balance row gives (0.3),
whose determinant is two.  The two integral owner choices have divergence
`+1` and `-1`, respectively, so neither is balanced.  Equivalently, with
`c({a})=0,c({b})=1` modulo two, both arcs have voltage one and a one-edge
circulation cannot have voltage zero.

This one-owner example is literal Boolean/private-label data, not an abstract
projective-plane gadget.  It proves:

* the general owner-plus-incidence matrix is not TU;
* a rational stationary pull clock need not have a one-copy stationary
  section;
* a discrepancy or torsion absorber is genuinely required.

By itself it does **not** prove that a complete all-owner TPC instance has
the same obstruction; the preceding `k=4` instance supplies that missing
literal all-owner calibration.

Each integral choice in (3.2) has route-inspection cost exactly one: add the
opposite uncoloured edge and obtain a two-edge Euler circuit.  Hence exact
balance and `O(1)` repair are different assertions.

## 4. Comparator pins are not free owner edges

At an ordered-singleton state `v`, a same-guard passage

\[
                              G,v,G                               \tag{4.1}
\]

uses two distinct trace edges, both of owner `F union G`.  A one-copy owner
selection has capacity one in that fibre.  Therefore (4.1) cannot be
realized wholly among selected owner edges.  One such guarded comparator
visit needs at least one uncoloured/boundary edge or an owner puncture.  Two
distinct equal-rank guards need two visits and hence at least two such
non-owner edges in this immediate address geometry.

This is the one-copy form of Proposition 4.1 in
`MATH_REDUCTION_PRIVATE_PHASE_STATIONARY_TRACE_CONE_AND_TWO_GUARD_ROOT_20260801.md`.
It does not rule out another comparator address.  It says that a rounding
theorem must declare whether comparator edges are:

* selected owner traces (then the immediate same-guard pin is infeasible),
* part of the `O(1)` route-inspection sidecar, or
* supplied by a punctured/auxiliary boundary bank.

## 5. A TU subclass after fixing one shore

There is one useful integral reduction which survives intact.

### Theorem 5.1 (fixed-tail bipartite-flow rounding)

Suppose every owner `T` has a prescribed tail state `u_T`, and every allowed
trace in its residual fibre is `u_T->v`.  Put

\[
 a(v)=|\{T:u_T=v\}|.
\]

Then a balanced one-copy selection is exactly a bipartite `b`-matching from
owners to head states, with owner degree one and head demand `a(v)`.  Its
constraint matrix is TU.  Thus every fractional feasible point rounds
integrally, including any compatible integral pin deletions/capacity
changes.

#### Proof

The outgoing multiplicity at `v` is fixed as `a(v)`.  State balance asks
that exactly `a(v)` selected traces have head `v`.  These are precisely the
two shores of a bipartite `b`-matching.  Bipartite incidence matrices are
totally unimodular. \(\square\)

The head-fixed dual statement is identical.  The theorem pinpoints the
actual coupling: TPC options generally change both the tail and the head.
An integral owner-to-tail section followed by Theorem 5.1 would solve the
balance rows, but the first section is exactly where odd circuits/torsion
can live.

Connectivity is still separate.  A balanced integral selection is an Euler
circuit if and only if its positive support is weakly connected.  If it has
`c` weak components, every route inspection needs at least `c-1` added
edges.  In the full order-`d` de Bruijn graph, joining components in an order
`P_1,...,P_c` costs exactly the corresponding suffix-prefix overlap deficits

\[
 \sum_{i=1}^{c-1}
   \bigl(d-\operatorname{ov}(\operatorname{end}P_i,
                              \operatorname{start}P_{i+1})\bigr).        \tag{5.1}
\]

Therefore bounded component count by itself gives only `O(d)`, not `O(1)`.

## 6. Precise surviving TPC gate

Assuming the private-label fractional TPC circulation, the weakest exact
one-copy theorem still needed is:

1. prove the degree-one integer-decomposition property (2.2) for the actual
   Boolean owner fibres, with the comparator pins charged to a declared
   sidecar; or exhibit an actual character/cut obstruction (2.4)--(2.6);
2. select an integral point whose positive support is connected, or whose
   exact overlap route-inspection cost (5.1) is `O(1)`;
3. retain the protected boundary comparator signatures.

The fractional stationary law certifies none of these three automatically.
The determinant-two example closes the generic-TU route.  The fixed-tail
theorem shows what additional structural resolution would restore a true
network-flow proof.

## 7. Independent exact audit

The accompanying independent checker

`scratch/audit_threadD_tpc_onecopy_euler_obstruction_20260801.py`

uses exact rational/integer arithmetic.  It verifies (0.3), the half-and-half
stationary point, both failed integral choices, the modulo-two voltage, the
one-edge route-inspection repair, and the owner-capacity failure of the
same-guard passage.  Independently of the other `k=4` checker, it also
reconstructs the six owner fibres, exhausts all 64 orientations, recomputes
the determinant-eight minor, and checks the sharp bridge witnesses.  Its
payload is

`scratch/threadD_tpc_onecopy_euler_obstruction_20260801.audit.json`.

The separate `k=4` checker cited in Section 3 supplies a second replay of the
same exact triangular loads and finite obstruction.

No SAT, exhaustive catalogue search, or heavy local computation was used.
