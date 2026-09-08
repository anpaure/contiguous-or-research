# State-relative joint expansion and the topology-transaction boundary

**Date:** 2026-08-02  
**Status:** exact finite-state theorem and audit interface, rebased on the
sole authoritative K17 promotion root `(R,H)=(1921,1694)`, model SHA-256
`353a9e97239666e88f93b3fbf89fdee95240ef1a5099af408b28692f930a6f15`
and checkpoint-manifest SHA-256
`abb3715e7f70dcfbb8917b061e8e8d591e542712091af944fb332c7a55639304`.
Its strict ancestry is
`1980 -> 1953 -> 1948 -> 1943 -> 1941 -> 1938 -> 1935 -> 1930 -> 1926 -> 1923 -> 1921`,
where the `1926 -> 1923` four-circuit batch is taken in an independently
audited strict reordering rather than its disconnected producer order, and
all six orders of the final three-circuit batch are strict.
The certified equal-`Phi` sibling `(1936,1727)` is a historical side branch,
not an active promotion root or an ancestor of the current root.  Together
with the residence-side parent `(1935,1729)`, it shows that `Phi` alone does
not determine the objective vector or literal product state.  It does not by
itself rule out a separately proved bisimulation or strict-transfer quotient.
A transition is called strict packet ancestry only where every primitive
prefix has separately passed.  The historical sixth commuting
circuit is a globally disconnected rejected boundary schema and is not part
of the promoted lineage.  No source, compiler, residency, or word conclusion
is made.

## 1. Product states and two different packet semantics

Let a **literal product state** contain the full selected-incidence vector,
rebuilt pair variables, all owner and degree rows, every frozen guard,
ordinary q1, protected incidences, the exact augmented topology partition,
both decoded opened histories, every opened target row, and any persistent
renewal ticket.  Write

\[
 v(x)=(R_0(x),H_0(x),R_1(x),H_1(x))\in\mathbb Z_{\ge0}^4,       \tag{1.1}
\]

where `R` is the length-one/two residence and `H` is the total rank-eleven
through rank-seventeen hole count.  Let `X` be the state set on which *all* hard
predicates, including the exact topology and both opened states, hold.

The current-state primitive exchange graph `G_X` has vertices `X`.  There is
an arc `x -> y` only when its C6/C8 circuit is alternating at `x`, its exact
materialized head is `y`, and `y in X`.  Let `C_omega(x)` denote the literal
covered-upper set in opening `omega`.  The zero-loss renewal graph used by the
finite audits is the subgraph whose arcs also satisfy
`C_omega(x) subseteq C_omega(y)` in both openings, together with containment
of the packet's fixed committed baseline when that is stronger.  Merely
storing opened target rows does not impose this monotonicity.  Thus an ordered
word

\[
             P=(x=x_0,x_1,\ldots,x_m=y)                         \tag{1.2}
\]

is a **strict packet** exactly when every transition `x_{i-1} -> x_i` is an
actual-tail arc of this graph.  In particular every `x_i in X`, every circuit
alternates at its actual tail, and every head is its exact materialization.
This is the semantics required by the phrase “every prefix stays hard-legal.”

There is a distinct transaction semantics.  Let `\bar X` relax only the
topology predicate and retain the complete fragment partition, port
permutation, and boundary-history tickets.  A **topology transaction** is a
path in `G_{\bar X}` whose endpoints lie in `X`.  It is not a strict packet
if an internal state lies outside `X`.  In particular, an internal split
cannot be hidden by checking only the connected terminal factor.

If opened histories are undefined on a disconnected intermediate topology,
then `\bar X` is not yet a legitimate physical state space.  In that case
the only meaningful weaker object is a simultaneous atomic batch: its net
head may be checked, but its circuit order is not a hard-prefix path.  A
topology-debt theorem must therefore define the partial histories and check
their exact rows; a component counter alone is insufficient.

## 2. The weakest state-relative regenerative hypothesis

Fix one of the semantics `sigma in {strict,transaction}`.  Let `Z subseteq X`
be a chosen renewal domain, `T subseteq Z` a declared terminal face, and let

\[
                    \Phi:Z\longrightarrow\mathbb Z_{\ge0}       \tag{2.1}
\]

be one common integer potential.  For `x in Z`, let `\mathcal P_sigma(x,Z)`
be the family of finite `sigma`-admissible packets that start at `x` and next
commit at an endpoint in `Z`.  Internal states need not belong to `Z`; under
strict semantics they must still belong to `X`.

### Hypothesis E (one-branch state-relative expansion)

For every `x in Z \ T`, there is a packet `P_x in \mathcal P_sigma(x,Z)`, ending at
`e(P_x)`, such that

\[
                    \Phi(e(P_x))\le \Phi(x)-1.                   \tag{2.2}
\]

Only the selected endpoint must return to `Z`.  There is no requirement that
all outgoing exchanges remain in `Z`, that both named payload types be
available, that every primitive have negative cost, or that every state of
the full hard component belong to `Z`.

### Theorem 2.1 (regenerative commit descent)

Hypothesis E implies that repeated selection of its witnessing packets
reaches `T` after at most `Phi(x_0)` commits from any `x_0 in Z`.

Conversely, for a fixed `Phi`, any state-feedback renewal proof which commits
only inside an invariant domain `Z` and decreases `Phi` at every nonterminal
commit necessarily supplies (2.2) at each state in its policy domain.
Consequently Hypothesis E is necessary and sufficient for a state-feedback
decreasing selector on that potential, packet language, and policy domain.
This is the precise sense of “weakest” here; it is not asserted to be the
weakest structural or all-`k` expansion hypothesis.

#### Proof

Each committed packet lowers a nonnegative integer by at least one and its
endpoint is again in `Z`.  Hence more than `Phi(x_0)` nonterminal commits are
impossible.  If the process stopped outside `T`, (2.2) would supply another
commit.  The converse follows by taking the first committed packet selected
by the alleged renewal policy at each nonterminal state.  \(\square\)

For a theorem from one specified seed, `Z` need only be the invariant domain
of the selected policy containing that seed.  Requiring (2.2) on every state
of the ambient hard component is strictly stronger.  If the retained K17
product graph is finite—including finite ranges for every history and ticket
coordinate—an accepting packet can be chosen simple and hence has length
less than the number of product states.  This gives a finite K17 bound, not
an all-`k` uniform bound.

### Corollary 2.2 (branchwise frontier expansion)

Let `B subseteq Z` be a set of certified reachable commit states with the
same value of `Phi`.  A renewal theorem covering this frontier must retain
the states separately and impose

\[
 \forall b\in B\setminus T\quad
 \exists P_b\in\mathcal P_\sigma(b,Z):
 \Phi(e(P_b))\le\Phi(b)-1.                              \tag{2.3}
\]

The weaker assertion that (2.3) holds for *some* `b in B` proves descent only
from that chosen branch.  It does not prove descent from another reachable
equal-potential state.  A strict zero-cost bridge from one branch to another
may be included inside `P_b`, but equality of `Phi` does not create that
bridge.  Equivalently, each branch has its own accepting flow (4.2) and may
have its own Farkas shore (4.3).

Thus a scalar level set is not a valid quotient of the product graph unless
one separately proves a bisimulation or strict transfer theorem on that level
set.  The state retained by the recurrence is at least the full vector (1.1),
and in fact the complete literal product state whenever provider, history, or
topology coordinates distinguish equal vectors.

## 3. Common linear integer potentials and the authoritative joint root

A useful special case of (2.1) is

\[
 \Phi_w(x)=w_R(R_0(x)+R_1(x))+w_H(H_0(x)+H_1(x)),
 \qquad w_R,w_H\in\mathbb Z_{>0}.                     \tag{3.1}
\]

The authenticated ancestry has the following common score in each opening:

\[
\begin{array}{c|c}
\text{commit}&(R,H)\\ \hline
x_0&(1980,1789)\\
x_1&(1953,1764)\\
x_2&(1948,1761)\\
x_3&(1943,1748)\\
x_4&(1941,1743)\\
x_5&(1938,1733)\\
x_6&(1935,1729)\\
x_7&(1930,1721)\\
x_8&(1926,1712)\\
x_9&(1923,1702)\\
x_{10}&(1921,1694).
\end{array}                                             \tag{3.2}
\]

The state `x_5` is the common parent of two certified, Pareto-incomparable
children.  Write their complete two-opening objective vectors as

\[
\begin{aligned}
 u&=(1936,1727,1936,1727),\\
 r&=(1935,1729,1935,1729),\\
 B&=\{u,r\}.
\end{aligned}                                           \tag{3.3}
\]

Here `u` is the upper branch and `r` the residence branch.  Neither dominates
the other: `u` has one more residence defect and two fewer upper holes.  To
remove a recurrent normalization ambiguity, write

\[
 \phi_{2,1}^{(\omega)}=2R_\omega+H_\omega,
 \qquad
 \Phi_{2,1}=\phi_{2,1}^{(0)}+\phi_{2,1}^{(1)}.          \tag{3.4}
\]

Both children have the same scalar score but remain different product states:

\[
 \phi_{2,1}^{(\omega)}(u)=\phi_{2,1}^{(\omega)}(r)=5599,
 \qquad \Phi_{2,1}(u)=\Phi_{2,1}(r)=11198.              \tag{3.5}
\]

Relative to `x_5=(1938,1733)`, the upper child has payload `(-2,-6)` and
the residence child `(-3,-4)` in each opening.  Each therefore has
`Delta phi=-10` per opening and `Delta Phi=-20` in aggregate.  Relative to
`x_0=(1980,1789)`, their payloads are respectively `(-44,-62)` and
`(-45,-60)`; both have `Delta phi=-150` per opening and `Delta Phi=-300`.

Only the residence child lies on the promoted route to the current root.
Put

\[
\begin{aligned}
 p&=(1930,1721,1930,1721),\\
 f&=(1926,1712,1926,1712),\\
 g&=(1923,1702,1923,1702),\\
 h&=(1921,1694,1921,1694).
\end{aligned}                                           \tag{3.6}
\]

Then

\[
 \phi_{2,1}^{(\omega)}(p)=5581,
 \qquad \phi_{2,1}^{(\omega)}(f)=5564,
 \qquad \phi_{2,1}^{(\omega)}(g)=5548,
 \qquad \phi_{2,1}^{(\omega)}(h)=5536,
 \qquad \Phi_{2,1}(h)=11072.                           \tag{3.7}
\]

The strict suffix `r -> p` consists of

```text
O66472, C6-90396, O43904, O33894
```

and has per-opening prefix scores

```text
5593, 5590, 5586, 5581.
```

Its endpoint payload is `(-5,-8)`, hence `Delta phi=-18`.  The next strict
suffix `p -> f` consists of

```text
O9441, O2259, C6-1756, O2665, O45130
```

with per-opening prefix scores

```text
5578, 5573, 5570, 5567, 5564.
```

Its endpoint payload is `(-4,-9)`, hence `Delta phi=-17`.  Every displayed
prefix in these two suffixes has exact circuit geometry and actual-tail
applicability, exact degrees and normalized boundary, all `16261` frozen
guards, ordinary q1 `19412`, opened q1 `19448` in both openings, one connected
component, and zero local and root-transitive literal upper losses in both
openings.  Thus these are strict packets, not terminal-only batches.

The producer order for the four-circuit endpoint `f -> g` is

```text
O49734, O1205, C6-68485, C6-55436.
```

Its third prefix is disconnected, so that displayed word is not strict.  The
four-support subset graph was therefore audited over all `4!=24` orders.
Exactly twelve orders are strict and twelve fail connectivity.  One strict
order is

```text
O49734, O1205, C6-55436, C6-68485,
```

with per-opening prefix triples `(R,H,phi)`

```text
(1925,1709,5559), (1925,1704,5554),
(1924,1703,5551), (1923,1702,5548).
```

Every prefix of this reordered word preserves the same hard rows and literal
two-opening no-loss conditions listed above, and its terminal assignment is
byte-identical to the authoritative model.  Thus `f -> g` is a strict packet
after topology-aware reordering, with payload `(-3,-10)` and
`Delta phi=-16`; no topology-debt semantics is needed for the promoted path.

The next suffix `g -> h` consists of

```text
C6-28842, S41329, C6-53810.
```

All eight subset states and all `3!=6` orders of this commuting family are
strict.  In the displayed order its per-opening prefix triples `(R,H,phi)`
are

```text
(1922,1699,5543), (1922,1696,5540), (1921,1694,5536).
```

Thus this is a hereditary strict cube with payload `(-2,-8)` and
`Delta phi=-12`, rather than a topology-constrained cube requiring a reserved
last circuit.

Concatenating the independently audited ancestry gives 52 strict primitives
from `x_0` to `h`, with family census `36` octahedral C8, `13` C6, and `3`
star-C8.  Every primitive step in the chosen orders strictly decreases `phi`
in both openings.  The net payload is `(-59,-95)` and `Delta phi=-213` per
opening.  This is a finite authenticated path, not a proof of expansion from
`h`.

The common-parent `1938/1733` model has SHA-256
`fc6be42f7c52fa0d1da4733af10568adc1bb3e6a5b6d580f78920f11c6329d4b`.
The certified upper branch has model, audit, and manifest SHA prefixes
`699b7b45`, `ce8b903a`, and `c2e11fed`; the certified residence branch has
corresponding prefixes `919a34fb`, `ba001da3`, and `8f12c0dd`.  Both preserve
all ordinary and opened q1 rows, every frozen guard, connected topology, and
both-opening literal containment with zero losses.  These bindings certify
the two fork endpoints, not a uniform expansion theorem.  The promoted
`1930/1721` checkpoint has model and manifest SHA prefixes `96d35567` and
`bf840621`; its manifest binds the `1935/1729` manifest as parent.  The
`1926/1712` checkpoint has independent-audit, containment-audit,
containment-table, and manifest SHA prefixes `97c30214`, `e34ce5e1`,
`c88ccc2e`, and `44171fe4`; its manifest binds `bf840621` as parent.  Its
two-opening rank-10-through-rank-17 missing vector is
`[0,1469,241,2,0,0,0,0]` in each opening.  The `1923/1702`
checkpoint has model, independent-audit, containment-audit,
containment-table, and manifest SHA prefixes `7a80fe02`, `40ccf578`,
`74fd86d4`, `5f5d0cc7`, and `097ec68b`; its manifest binds `44171fe4` as
parent.  Its rank-10-through-rank-17 missing vector is
`[0,1463,237,2,0,0,0,0]` in each opening.  The current `1921/1694`
checkpoint has model, independent-audit, containment-audit,
containment-table, and manifest SHA prefixes `353a9e97`, `b4395ceb`,
`d380ebcf`, `96b8d5c1`, and `abb3715e`; its manifest binds `097ec68b` as
parent.  Its rank-10-through-rank-17 missing vector is
`[0,1457,235,2,0,0,0,0]` in each opening.

Let the older calibrated payload symbols be

\[
                    Q=(-1,+1),\qquad V=(+3,-7).         \tag{3.8}
\]

At the scalar level the two branches behave differently relative to the
formal calibrated payloads:

\[
\begin{aligned}
 u-x_5&=(-2,-6)=8Q+2V=2(4Q+V),\\
 r-x_5&=(-3,-4),\qquad
       nQ+mV=r-x_5\Longrightarrow(m,n)=(7/4,33/4),\\
 f-p&=(-4,-9),\qquad
       nQ+mV=f-p\Longrightarrow(m,n)=(13/4,55/4),\\
 f-x_5&=(-12,-21),\qquad
       nQ+mV=f-x_5\Longrightarrow(m,n)=(33/4,147/4),\\
 g-f&=(-3,-10),\qquad
       nQ+mV=g-f\Longrightarrow(m,n)=(13/4,51/4),\\
 g-x_0&=(-57,-87)=165Q+36V,\\
 h-g&=(-2,-8),\qquad
       nQ+mV=h-g\Longrightarrow(m,n)=(5/2,19/2),\\
 h-x_0&=(-59,-95),\qquad
       nQ+mV=h-x_0\Longrightarrow(m,n)=(77/2,349/2).
\end{aligned}                                           \tag{3.9}
\]

Thus only `u-x_5` and `g-x_0` among the displayed payloads have integral
`Q/V` coefficients; every other solution shown in (3.9) is fractional.  Even
the two integral identities are payload arithmetic, not decompositions of the
actual circuit words.  Likewise, the ancestral
`1980 -> 1953` net satisfied

```text
S33913, fifteen octahedral C8 circuits, two C6 circuits,
```

an 18-primitive strict word in which every actual-tail prefix is hard-legal
and strictly decreases `phi` in both openings.  Hence the actual word is not
`4Q+V`.  At the payload-lattice level only,

\[
              (-27,-25)=66Q+13V=13(5Q+V)+Q,            \tag{3.10}
\]

but the identity (3.10) is not a circuit decomposition: it uses seventy-nine
formal payloads and ignores their state-relative supports.  The proof-safe
conclusion is that each exact endpoint transition supplies a candidate
compound payload.  It becomes a finite **strict packet** type only after an
actual-tail, every-prefix hard audit, possibly of a different permutation,
passes.  Hypothesis E may use only that strict state-relative packet; no
scalar equality or `Q/V` factorization is sufficient.

More generally, let `A_x` be the set of exact payload vectors of admissible
return packets from `x` to `Z`.  A fixed positive integer linear potential
witnesses Hypothesis E on `Z` exactly when there exist one fixed vector
`w in Z_{>0}^4` and, for every `x in Z\setminus T`, a selectable
`a_x in A_x` with

\[
                         w\mathbin\cdot a_x\le-1
                         \quad(x\in Z\setminus T).       \tag{3.11}
\]

It is enough that one packet at each state satisfy (3.11).  Requiring every
packet, or a fixed `Q/V` inventory at every state, is unnecessary.

## 4. Exact cut and min-cost duals

Fix `x in Z \ T` and construct the appropriate finite product graph for the
chosen semantics.  Add an accepting sink `t_x` and a zero-cost arc to it from every
commit state

\[
             A^-_\Phi(x)=\{y\in Z:\Phi(y)\le\Phi(x)-1\}.          \tag{4.1}
\]

Use a one-bit “a physical move has occurred” layer if empty packets must be
excluded.  Let `N_x` be the head-minus-tail incidence matrix and
`d_x=e_{t_x}-e_x`.

Then (2.2) at `x` is exactly feasibility of

\[
                       N_x f=d_x,\qquad f\ge0.           \tag{4.2}
\]

If it is infeasible, let `S_x` be the states reachable from `x`.  It contains
`x`, excludes `t_x`, and has no outgoing arc.  Therefore

\[
 z=-\mathbf 1_{S_x},\qquad N_x^Tz\le0,\qquad d_x^Tz=1, \tag{4.3}
\]

which is the exact Farkas accepting cut.  This is the necessary-and-sufficient
reachability obstruction at `x`, relative to the chosen product graph and
domain.  No minimal-cardinality or universal structural-cut claim is made;
one needs to rule out (4.3) only on the selected invariant domain `Z`, not on
every state of the ambient factor state set.

For an arbitrary scalar arc ledger `c` rather than the endpoint set (4.1),
use a declared finite-length layered expansion of the product graph.  (For
an endpoint potential, an accepting path can be made simple, so fewer than
the number of product states layers suffice.)  On this acyclic graph the
shortest accepting packet is the integral unit-flow problem

\[
       \min c^Tf\quad\text{subject to }N_xf=d_x, f\ge0.          \tag{4.4}
\]

Its dual is

\[
       \max \pi^Td_x\quad\text{subject to }N_x^T\pi\le c.        \tag{4.5}
\]

A Bellman--Ford feasible potential `pi` with dual value at least zero proves
that no negative accepting packet exists, provided this cost-model sink is
reachable and accepts every declared closed return.  Strong duality on the
finite layered graph makes nonnegative optimum equivalent to such a feasible
dual potential.  If the sink is unreachable, (4.3), not a cost certificate,
is the relevant obstruction.

No objective need be defined on internal states.  Give every physical arc
cost zero and give the accepting arc `y -> t_x`, for `y in Z`, cost
`Phi(y)-Phi(x)`.  Every accepting path then has exactly its endpoint potential
difference as cost.  Equivalently, if `Phi` is explicitly extended to every
vertex of the chosen product graph, one may use the telescoping physical cost
`c_{uv}=Phi(v)-Phi(u)` and zero-cost sink arcs.  Under either convention,
reachability of `A^-_Phi(x)`, feasibility of (4.2), and a negative
accepting-path optimum in the all-return cost construction are equivalent.

For a two-coordinate Pareto requirement with no fixed `w`, one must instead
use the accepting endpoint set for the desired quadrant, or lift the exact
accumulated vector.  Adding two resource inequalities to an unlifted flow
relaxation is not an exact substitute.

## 5. The sixth-circuit topology split

Suppose a proposed compound packet consists of current-state circuits
`C_1,...,C_m`.  The following three claims are different.

1. **Recorded strict order.**  The displayed order is a strict packet iff
   every partial materialization is in `X` and every `C_i` alternates at its
   actual tail.
2. **Strictly reorderable batch.**  If the circuits are claimed to commute,
   form the subset-state graph whose vertex `S subseteq [m]` is the exact
   materialization after the circuits in `S`.  Retain `S -> S union {i}`
   only when `C_i` is alternating at that state and the head lies in `X`.
   A strict realization exists iff this graph has a path from the empty set
   to `[m]`.
3. **Atomic terminal batch.**  The combined toggle can have a hard-legal
   endpoint even when no such subset path exists.  This proves only an
   endpoint-certified atomic batch.  It is a topology transaction only when
   an explicitly defined relaxed path carries every intermediate ticket and
   returns to `X`.

### Proposition 5.1 (exact commuting-batch fan)

Assume the circuit supports are pairwise incidence-disjoint and every circuit
is alternating at the root.  If `chi` denotes only the selected-incidence
vector, put

\[
 \chi_S=\chi_\varnothing+\sum_{i\in S}z_i,
 \qquad x_S=\operatorname{Rebuild}(\chi_S).                    \tag{5.1}
\]

Disjointness makes `chi_S` independent of order and keeps every unused circuit
Boolean-alternating.  The proposition additionally assumes that all retained
product coordinates are deterministically rebuilt from `chi_S`; if a history
or ticket is not incidence-determined, it must be included explicitly and the
resulting subset product state must separately be shown order-independent.
Let `D` be the directed Boolean lattice retaining the
arc `S -> S union {i}` exactly when the corresponding actual-tail transition
passes the complete strict arc predicate, including literal no-loss when it
is required.  Then the batch has a strict ordering if and only if `D` has a
saturated path from `emptyset` to `[m]`.  If no such path exists, the subsets
reachable from `emptyset` form the exact Farkas shore for this batch-order
problem.

Indeed, a permutation is precisely a saturated Boolean-lattice path, and its
prefixes are precisely the visited subsets.  The retained-arc definition is
therefore equivalent term by term to strict legality.  The no-path certificate
is (4.3) applied to `D`.  This proof uses no independence assumption beyond
that needed to make each subset materialization well defined; overlapping
supports require the more general ordered product graph.

### Corollary 5.2 (repair-before-split interchange)

At an admissible subset `S`, let disjoint circuits `a,b` commute.  Suppose
`x_{S union {a}}` fails only topology, whereas `x_{S union {b}}` and
`x_{S union {a,b}}` pass every strict predicate and the two displayed arcs
are actual-tail applicable.  Then `b,a` is a strict two-step replacement for
the non-strict order `a,b`, with exactly the same endpoint and hence the same
subsequent subset states.  For an arbitrary fixed proper shore `W`, the
necessary connectivity ticket is

\[
 k_W(S)=|\delta(W)\cap E(x_S)|\ge1.                     \tag{5.2}
\]

If `W` contains an even number of the odd-degree exceptional vertices
`{M,D}`—in particular, if it contains neither—cut parity is even and one may
use the pair ticket `s_W=k_W/2>=1`.  Thus a circuit that raises the applicable
ticket can be moved before one that would spend it.  The ticket condition is
sufficient only for that fixed shore; all other cuts and every non-topology
row remain part of the retained-arc test in `D`.

### Proposition 5.3 (terminal-reserve fan certificate)

Retain the deterministic commuting cube of Proposition 5.1.  Let
`C=P disjoint-union {q}`, where `q` is reserved for the last step, and let
`B_x` be the inclusion-minimal hard-illegal proper subsets of `C`.  Then

\[
 q\in\bigcap_{B\in\mathcal B_x}B                         \tag{T1}
\]

is equivalent to every `q`-free subset being hard-legal; when
`\mathcal B_x` is empty, every choice of `q` qualifies.  If the full endpoint
is also hard-legal, any ordering of `P` followed by `q` is a strict packet.
Indeed, an illegal `q`-free subset contains an inclusion-minimal illegal
`q`-free subset, and conversely such a minimal subset violates (T1).

The topology part of this test has a bounded exact cut form.  For a fixed
shore `W`, put

\[
 k_x(W)=|\delta(W)\cap E(x)|,\qquad
 \tau(W)=\begin{cases}
 1,&|W\cap\{M,D\}|\text{ is odd},\\
 2,&|W\cap\{M,D\}|\text{ is even},
 \end{cases}                                             \tag{T2}
\]

and let `Delta_i(W)` be the crossing-count change of circuit `i`.  Every
preparer subset is connected exactly when, for every relevant nontrivial
shore,

\[
 k_x(W)+\sum_{i\in P}\min\{0,\Delta_i(W)\}\ge\tau(W),    \tag{T3}
\]

and the full commit is connected exactly when

\[
 k_x(W)+\sum_{i\in P}\Delta_i(W)+\Delta_q(W)\ge\tau(W). \tag{T4}
\]

To enumerate all relevant shores, delete from the root factor every old edge
used by `C`.  At most `4|C|` edges are deleted, so the resulting quotient has
at most `4|C|+1` components; every possible disconnection shore is a union of
these components.  For a fixed `W`, the least crossing count over all
preparer subsets is exactly the left side of (T3), proving necessity and
sufficiency.  The parity threshold (T2) follows because `M,D` are the only
odd-degree vertices.

Topology is only one coordinate of the certificate.  For every literal
provider, guard, opened-history, protection, or containment row `j`, let
`ell_j(S)` be its exact load after rebuilding the subset state and let `b_j`
be its threshold.  One must also check

\[
 \min_{S\subseteq P}\ell_j(S)\ge b_j,
 \qquad \ell_j(P\cup\{q\})\ge b_j                       \tag{T5}
\]

for both openings and every required row.  This is a bounded literal test,
not a scalar Hall projection.  If (T1) has no common terminal, a strict order
may still exist; the exact remaining criterion is saturated-path reachability
in the legal subset DAG of Proposition 5.1.

Consequently, if a materialized prefix has a forbidden topology split, the
recorded order cannot witness strict Hypothesis E, regardless of its negative
terminal payload.  If a later circuit repairs the split, the whole word may
witness transaction Hypothesis E, but it upgrades to strict semantics only
after one exhibits an ordering in the subset graph which avoids the split at
every prefix.  If no ordering exists, the empty-to-full subset reachability
shore and (4.3) give the exact topology-order cut.

A local splice described as “split” is not by itself dispositive: the audit
must evaluate the full augmented partition, since exterior connections may
keep the prescribed topology intact.  Conversely, checking only the final
component count does not certify intermediate opened histories.  The exact
audit row at the sixth circuit is therefore

```text
actual-tail alternation;
all non-topology hard predicates;
full augmented partition and prescribed one-lollipop type;
both rebuilt openings and all opened rows.
```

If all four pass, there is no hard topology split and the prefix belongs to
`G_X`.  If the topology row fails, that edge exists at most in the relaxed
graph `G_{\bar X}`, and only if the relaxed histories and tickets are actually
defined.  It is not by itself a topology transaction: a transaction must also
return to `X` at its endpoint.

The exact K17 audit gives the latter result for the historical sixth
commuting candidate after `joint1967`

```text
old 2449,4402,1381,291
new 2452,4403,1378,292.
```

The six circuit supports are pairwise incidence-disjoint, root-applicable,
and individually root-connected.  Nevertheless their common terminal shore
`W` is the unique component not containing `M,D`: it consists of `1022`
lower and `1022` owner vertices and is a `2044`-edge cycle.  The full cut
`delta(W)` contains `13,746` possible incidences and is exactly the frozen
passive connectivity clause.  The number `k_W` of selected crossings along
the declared prefix order is

\[
                     8,6,6,6,6,4,0.                    \tag{5.3}
\]

At the sixth tail, all four old incidences are the four selected crossings,
whereas all four new incidences are internal to a shore.  Hence the exact
augmented state changes from one to two components.  The passive audit
reports `NEEDS_CONNECTIVITY`, and the independent topology replay fails its
trail-length check: the main lollipop remains but the `2044`-edge cycle is
detached.  Passing the full round-five CNF does not repair this separate
topology/opening failure.

Therefore this sixth edge is absent from `G_X` and must be recorded as a
topology-blocked boundary schema.  It is not an accepted transaction and is
not a prefix of the authenticated promoted lineage.  Because the six
supports commute, reordering these same six circuits cannot alter their
disconnected common endpoint.  The terminal route must omit or replace the
sixth circuit, or a prior additional repair must change the selected cut.
The six-toggle word is not itself a topology transaction because its terminal
state lies outside `X`.  The sixth edge could occur only internally in a
longer `G_{\bar X}` transaction, and only if disconnected histories and
tickets are fully defined and a later repair returns to `X`.

The useful state-relative ticket is

\[
                         s_W(x)=k_W(x)/2.               \tag{5.4}
\]

Cut parity is even.  The sixth circuit consumes two crossing pairs, so its
strict applicability requires `s_W >= 3` at its actual tail, leaving at
least one pair.  Here `s_W=2`.  For this fixed shore `W` and unchanged sixth-
circuit crossing signature, a degree-preserving preparer must raise `k_W`
from `4` to at least `6`.  One net crossing pair is sharp for this single cut,
but does not certify other cuts, openings, providers, or guards.  This is an
exact local cut requirement, not a scalar component-count heuristic.

The frozen graphic-cut audit has SHA-256
`f73b43f3bddffb3a4d3fbfd6ff4301eac5d827e6ffe929f6719a1fd9dd62bd83`;
its bundle manifest has SHA-256
`56562606603701f5d1e20c75fbbe84e9e98300dc9c6019a22f2d5442e6f5c907`.

This rejected edge alone is not a Farkas proof that all negative expansion
from the five-circuit state is impossible.  It is one certified absent arc,
or one rejected candidate-boundary schema in a larger proposal graph.  A
genuine Farkas shore must show that no **retained** arc leaves the reachable
set, equivalently classifying every candidate route to a lower-potential
return as absent.

The `1943/1748 -> 1941/1743` promotion requires a correction to the raw
candidate-file interpretation.  The selected mask is `0b1011`: it uses rows
`0,1,3` only, in the order

```text
O24932, O49299, C6-18539.
```

Its exact prefixes are

\[
 (1943,1748)\to(1942,1747)\to(1941,1746)\to(1941,1743), \tag{5.5}
\]

and every prefix is connected, hard-legal, and has zero two-opening
containment losses.  Thus the actual three-circuit promotion is a strict
packet.

The fourth raw candidate, row `2`, is unselected; it deletes old incidences
`74513,83370,83325,74473`.
Any order audit of the four-row **superset** concerns that different support
set and says nothing against the selected `0b1011` packet.  The next promotion
`1941/1743 -> 1938/1733` is also an audited strict packet, using selected rows
`1,2,3,4` of its candidate bank with every declared prefix hard-legal.
Neither strict promotion needs topology-debt semantics.

The current `1926/1712 -> 1923/1702` batch realizes case 2 above.  Its
producer order reaches a disconnected subset after

```text
O49734, O1205, C6-68485,
```

then returns to a connected terminal assignment after `C6-55436`.  That
producer order is not strict.  Exhaustive traversal of the four-support
Boolean order graph finds twelve strict permutations and twelve orders whose
only reported hard failure is connectivity.  Number the four circuits
`1=O49734`, `2=O1205`, `3=C6-68485`, and `4=C6-55436`; packet `4` here is
producer id `5` in the separate strict-reorder bundle, so order `1243` here is
its file-labelled order `1253`.  The exact rule is

```text
an order is strict  iff  packet 1 or packet 3 is last;
```

equivalently, no proper prefix may contain both `{1,3}`.  This accounts for
all twelve passing and all twelve failing permutations; it is stronger than a
global precedence claim between the two C6 circuits.

For the producer prefix after packets `1,2`, denote the exact threatened shore
by `W_*`.  It has `6369` lower and `6369` owner vertices and two selected
crossings.
Packet 3 deletes precisely its crossing edges `120397,120565` and adds none,
whereas packet 4 deletes no crossing and adds `101681,102774`.  Hence

\[
 \text{producer }1,2,3,4:\quad k_{W_*}:2\to0\to2,\qquad
 \text{strict }1,2,4,3:\quad k_{W_*}:2\to4\to2.         \tag{5.6}
\]

Moving the repairing packet 4 before packet 3 at the fixed prefix `{1,2}` is
therefore exactly Corollary 5.2 and gives the strict order displayed in
Section 3.  This is an exact bounded topology-bypass fan: the endpoint toggle
is unchanged, but the graphic-cut coordinate induces an ordering constraint.
It is not evidence that arbitrary endpoint-connected batches are reorderable.
The split/repair ledger is `res1923.split_repair.tsv`, SHA-256
`b4ea5d5cd6489ab207e0750f1845651b22817541d63bf09ce7a4a89e834f5465`,
inside the separate strict-reorder bundle whose `MANIFEST.local.sha256` has
SHA-256
`aa871e36789ac237fa1f99986ee14a3ab254ff2edcdeac8da88fd25e432d8c62`.
The frozen combined lineage/order bundle has manifest SHA-256
`7d0ebf68b0f153ad63d6052a65820f6924ddd07e92d7703b2c6ffb8fee167c64`;
its manifest verifies the complete 24-order table, the selected-prefix table,
the checkpoint bindings, and the O3 C++ audit sources.

The next `1923/1702 -> 1921/1694` cube has
`\mathcal B_x=emptyset`: every one of its eight subsets is hard-legal and all
six orders are strict.  Consequently every circuit can serve as the reserved
terminal in Proposition 5.3.  This hereditary cube is a stronger local fan
certificate than the preceding common-terminal cube, but it is still an
incoming certificate at the new root, not a uniform outgoing expansion
theorem.  The corrected carrier/fan bundle has manifest SHA-256
`76b49b3b474d77095047ecfed7cc6cbbbc944749cc3ee5b9c55bfe9b52bf8a71`
and verifies the six-order table, all subset/topology ledgers, checkpoint
bindings, and audit sources.

The provisional three-spoke fan at `h` supplies the complementary obstruction.
Each of `A1=C6-25905`, `A2=O74976`, and `A3=S72132` is individually negative
and connected.  The `A1A2` and `A1A3` subsets are connected, but `A2A3` and
the full three-spoke endpoint are disconnected.  For `A2A3`, the smaller
shore has `7586` lower and `7586` owner vertices and the exact pair ticket is

\[
                  s_W:2\longrightarrow1\longrightarrow0.       \tag{5.7}
\]

Each of `A2,A3` consumes a different crossing pair; neither inserts a crossing
for that shore.  Adding `A1` changes the terminal shore but still leaves a
final `2 -> 0` split, so `A1` is not a bridge.  A compound packet containing
both `A2,A3` therefore requires at least one additional planted crossing pair,
and (T3)--(T5) must still certify all other cuts and literal rows.  This is a
sharp topology counter-cut to the rule “pack all individually negative
spokes,” while all three endpoints remain unpromoted.

### Proposition 5.4 (serial relay paths are compound fan arms)

The fixed lower-table common-socket model and the strict product graph must
not be conflated.  In a lower table, write a long donor row as
`v=(B_v,M_v,R_v)` and a free singleton as `f=(R_f)`.  If

\[
 B_{v_i}\subsetneq M_{v_{i+1}}\quad(0\le i<\ell),
 \qquad B_{v_\ell}\subsetneq R_f,                              \tag{5.8}
\]

then the donor path

\[
              v_0\longrightarrow v_1\longrightarrow\cdots
              \longrightarrow v_\ell\longrightarrow f
\]

is one exact compound column.  It is serialized by first moving
`B_{v_ell}` to `f` and then applying the relays in decreasing index order.
Immediately before each relay its donor is long and its receiver is short.
Thus internal use of one physical row first as a donor and later as a
receiver is legal; it is a temporal interface, not simultaneous double use.

Let `L_v,S_v` retain only the long/short mode of donor row `v`, and let
`N_f,T_f` retain the singleton/short mode of the free row.  The elementary
mode boundaries telescope to

\[
 \partial P=(T_f-N_f)+(S_{v_0}-L_{v_0}).                       \tag{5.9}
\]

Every internal row therefore has coefficient zero.  Equivalently, after
subtracting the universal one-free/one-source signature in (5.9), the reduced
mode boundary is zero.  More strongly, the aggregate named-target multiset
and all owner/root data have zero boundary.  This does **not** say that the
fully payload-labelled state of an internal row is unchanged: in general it
changes from `L_v(B_v)` to `L_v(B_u)`.  Palette, opened-history, cap, aperture,
topology, and voltage labels must likewise be glued literally before the
column is an arm of the full product graph.

The authenticated round-47 witness is

```text
29 -> 520 -> 2117 -> F15856,
```

and its last two relays are

```text
round21 -> round22:  A520 -> D2117, moving bottom 4174;
round22 -> round23:  A29  -> D520,  moving bottom 158.
```

Thus row `520` has the exact trace

\[
 L_{520}(4174)\longrightarrow S_{520}\longrightarrow L_{520}(158). \tag{5.10}
\]

The short interface and the projected mode boundary cancel, while the two
bottom-labelled long states correctly remain distinct.  In the full
row-labelled basis the suffix has boundary

\[
 \begin{split}
 \partial P_{21,23}={}&(S_{29}-L_{29}(158))
 +(L_{2117}(4174)-S_{2117})\\
 &+(L_{520}(158)-L_{520}(4174)),
 \end{split}                                                   \tag{5.11}
\]

which is not zero.  Thus the unqualified statement “net state boundary is
zero” would be false: exactly the internal short interface, reduced mode
boundary, aggregate target multiset, and owner/root projections close.  A
direct application of the compound suffix to round 21 is byte-identical to
round 23, SHA-256
`3bd462908bd8df71684a53c42d6e6698ab9ba638245e72f28b21ea1a588da900`.
The independently frozen complete lower projections along the two exact
lower-table prefixes are

```text
state       matching  deficiency  zero heads
round21       16871       27          16
round22       16872       26          15
round23       16874       24          13.
```

Consequently the macro endpoint has exactly the successful round-23 lower
projection, not merely the same scalar ledger.

For Proposition 5.1, a compound path may be treated as one fan arm only after
expanding its fixed serial word and checking every microscopic actual-tail
state in the relevant hard product graph.  Completed path arms commute at the
lower-table level when their donor/free vertex sets are disjoint; internal
row reuse inside one arm is charged once.  If arms overlap externally, or if
their nonlinear halos interact, the exact criterion is the ordered product
graph rather than a Boolean commuting cube.

### Corollary 5.5 (strict four-arm path contraction)

Let `A={a_1,a_2,a_3,a_4}`.  Arm `a_i` has a fixed serial expansion of
microscopic length `ell_i<=ell`, and every completed-arm subset has one
order-independent exact product state `x_S`.  This order independence may
come from pairwise disjoint external supports and deterministic rebuilding,
or from an exact interaction replay; lower-table disjointness alone is not
sufficient.  Choose a reserved terminal arm `q` and put `P=A\setminus{q}`.
Assume:

1. the completed-arm states satisfy (T1), the preparer cut and literal rows
   (T3),(T5), and the full endpoint satisfies (T4),(T5);
2. for every `q`-free completed subset `S` and every `a_i in P\setminus S`,
   every microscopic transition in the fixed expansion of `a_i`, started at
   its actual tail over `x_S`, is applicable and has its head in `X`;
3. every microscopic transition in the expansion of `q`, started at its
   actual tail over `x_P`, is applicable and has its head in `X`.

Then every order of the three preparer arms followed by `q`, with each arm
expanded in its fixed internal order, is a strict word.  Its microscopic
length is

\[
                         \sum_{i=1}^4\ell_i\le4\ell.            \tag{5.12}
\]

Indeed, (T1),(T3),(T5) make every completed preparer context hard-legal, and
conditions 2--3 induct over every internal actual-tail transition.  The full
endpoint passes by (T4),(T5).  No internal row of a contracted arm is
available to another arm unless its overlap was included in the exact replay.

When every microscopic factor exchange deletes at most four selected
incidences, the exact topology quotient for all these microprefixes is
obtained by deleting every root edge that any expansion can remove.  It has
at most

\[
                 4\sum_i\ell_i+1\le16\ell+1                 \tag{5.13}
\]

components.  Every possible intermediate disconnection shore is a union of
those components.  Thus the contraction remains a bounded exact cut test;
using `4|A|+1` after hiding nontrivial arm depth would be unsound.

The four-circuit `f -> g` fan is the `ell_i=1` primitive instance of this
corollary.  Replacing any one of its generators by a relay path would require
the new full subset-context and microprefix audit above; the round-47 lower
witness is not asserted to be such a replacement.

This also locates the exact scope of the authenticated `2188/5969`
obstruction.  The unchanged round-47 table has `2188` accepted five-cell
socket hyperarcs and `5969` short roles of socket degree zero, so its fixed
downward/neutral relaxed-nine `1S` face has no complete cover.  This census
alone is not an unrestricted-socket chronology theorem.  A compound path
changes row modes and bottom labels, however, so that fixed-table empty-row
shore is not a valid global no-good for a variable path-column master.  Every
selected path endpoint must regenerate the entire literal socket bank.
Nothing here gives the displayed path, round 23, or any other table a full
`1S` lift.
The detailed path-column theorem has SHA-256
`db2bc9091625db6be51862fc895dd3e7e00d51dc0fb92d03d2b29953ef56c431`;
its frozen audit-bundle manifest has SHA-256
`7a9372ae724e0a3b077483d4719cd7b97ef5e0dffe243cbfbc22b2600e61d216`.

## 6. Renewal statement at the authoritative root

Let `Z` be any policy-invariant family of hard K17 states containing the
authoritative state `h=(1921,1694,1921,1694)`.  A sufficient and, relative to
`Phi_{2,1}`, the declared packet language, and `Z`, pointwise weakest
regenerative hypothesis from this seed is:

> For every nonterminal state `x in Z` reachable from `h` under the selected
> renewal policy, the strict product graph from `x` contains some finite
> hard-prefix packet returning to `Z` with `Delta Phi_{2,1} <= -1`.

The terminal-reserve fan gives a more structural sufficient hypothesis.  Fix
in advance a current-state generator `Gamma`, integers `L,delta>0`, a renewal
domain `Z`, and terminal set `T`.  An arm may be one circuit or a compound
relay path from Proposition 5.4; its length is the number of microscopic
actual-tail transitions in its fixed serialization.  Require that for every
`x in Z\setminus T`, `Gamma(x)` returns a strict stem followed by a
deterministic commuting fan, of total expanded length at most `L`, satisfying
the literal conditions (T1)--(T5) at completed-arm subsets and Corollary 5.5
(or its exact `m`-arm version) in every completed-subset context: each
microscopic transition must be actual-tail applicable and have a hard-legal
head.  Require that the full endpoint `y` lies again in `Z` and obeys

\[
                 \Phi_{2,1}(y)\le\Phi_{2,1}(x)-\delta.   \tag{6.1}
\]

### Theorem 6.1 (bounded regenerative terminal-reserve descent)

Under this hypothesis, regenerating `Gamma` at each committed endpoint reaches
`T` after at most

\[
 \left\lfloor\frac{\Phi_{2,1}(x_0)-\inf_{z\in Z}\Phi_{2,1}(z)}{\delta}
 \right\rfloor                                           \tag{6.2}
\]

commits and at most `L` times that many primitive exchanges.  Every prefix is
strict by Proposition 5.3, every endpoint regenerates in `Z`, and the
nonnegative integer potential falls by at least `delta`.  This is a
state-feedback theorem: it does not reuse a stale root catalogue or assume a
preselected infinite word.

Positive residence, the complete positive q1-provider multiplicity vector,
and connectedness do not imply this statement.  An abstract typed-twin
factor/exchange construction keeps all those coarse data fixed while changing
one planted half-pair compatibility bit `M_{j,p}`.  The compatible twin has a
pivot--quench fan; in the incompatible twin every proposed quench leaves the
two-state reachable shore `{F,AF}` and is rejected by a typed provider,
history, guard, or topology row.  Then

\[
 z=-\mathbf1_{\{F,AF\}},\qquad N^Tz\le0,\qquad
 (e_t-e_F)^Tz=1                                             \tag{6.3}
\]

is a two-state Farkas cut, the smallest nontrivial shore once the legal pivot
state `AF` is required in this countermodel.  This is an abstract
factor/exchange construction, not an authenticated K17 sink.  It shows why the
additional hypothesis must live in the literal product graph rather than in
the objective and multiplicity projection.

This hypothesis allows the packet shape, length, primitive families, and
payload exchange ratio to depend on `x`.  It includes only those promotion
transitions for which some ordered primitive realization passes every hard
prefix.  When the sink is attached only to `A^-_Phi(x)`, failure is exactly
the reachability/Farkas cut (4.3).  Alternatively, if a sink accepts every
closed return and arc costs record payload, a reachable sink with nonnegative
optimum is certified by (4.5).  No positive-residence statistic, q1
multiplicity vector, connected root state, or terminal-only compound toggle
rules out either certificate.

For any hard return domain `Y` on which this aggregate potential is defined,
define the bounded strict accepting value

\[
 \mu_{L,Y}(x)=\min\{\Phi_{2,1}(y)-\Phi_{2,1}(x):
       1\le\operatorname{len}(x\leadsto y)\le L,
       \ x\leadsto y\text{ is strict},\ y\in Y\},             \tag{6.4}
\]

with value `+infinity` when no such return exists.  On the certified corridor

\[
 Y_{\rm corr}=\{r,p,f,g,h\},
\]

the four successive strict commits have the following calibrated bounds for
the aggregate potential:

\[
\begin{array}{c|c|c|c}
\text{tail}&\text{head}&\text{length}&\Delta\Phi_{2,1}\\ \hline
r&p&4&-36\\
p&f&5&-34\\
f&g&4&-32\\
g&h&3&-24.
\end{array}                                               \tag{6.5}
\]

Thus, with terminal set `{h}`, this is a four-commit bounded policy with
`L=5,delta=24`, not merely one isolated hop.  It proves regeneration along
this finite certified corridor only.

At the current root `h`, three distinct direct candidates have provisional
per-opening score `5533`: `C6-25905` with payload `(0,-3)`, `O74976` with
payload `(-1,-1)`, and `S72132` with payload `(0,-3)`.  Their root-local
producer audits report full guards, q1, topology, and two-opening no-loss, so
they form a provisional three-way one-step fan with aggregate potential drop
`-6`.  They are not credited as promoted endpoints: none currently has a
frozen checkpoint manifest and immutable independent prefix replay.  Even a
frozen child would certify only the next local commit; regeneration requires
that its endpoint return to one fixed `Z` satisfying the quantified
terminal-reserve hypothesis again.

The displayed strict ancestry therefore proves negative incoming packets to
`h` and a provisional outgoing fan, but not the quantified outgoing condition
at every future state.  The historical sixth-circuit shore proves that one
specific topology-blocked edge is absent, not that every negative return from
`h` is blocked.  The typed-twin cut shows that positive residence, provider
multiplicity, and connectedness cannot fill this gap.

Under the stated hypotheses Theorems 2.1 and 6.1 give repeated descent of the
common scalar `Phi_{2,1}` from `h`.  Coordinatewise descent of `R,H`, or a
separate descent assertion in both openings, requires adding those endpoint
inequalities explicitly.  A stronger theorem covering the earlier fork must
impose the same condition separately from `u` and `r`, unless a strict
transfer or bisimulation between them is proved.  Their common scalar value
`5599` cannot identify the branches or lend a packet from one to the other.
The result does not identify the terminal state set with a resident factor
unless that identification is separately proved, and it makes no source or
compiler claim.
