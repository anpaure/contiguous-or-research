# Protected boundary macros: the exact ordered-Hall connector min--max and the opening gate

Date: 2026-08-01  
Lane: protected upper-exact Catalan connector around a fixed boundary macro  
Status: unconditional owner/`q1` min--max theorem and exact quantifier audit.
No all-dimensional source-lift, arbitrary-width upper, residence, or compiler
theorem is claimed.

## 0. Verdict

Fix the boundary macro before making any global choices.  The fixed-`H`
planting theorem and the synchronized-common-basis marginal theorem then
remove two scalar obstructions, for all sufficiently large parameters:

1. the protected incidence bank is locally factor-consistent; and
2. some synchronized common basis avoids its fixed `O(Hh)` casualty
   projection.

They do **not** imply a common physical connector.  After a synchronized
common basis, a predecessor matching and an upper-exact rooted Catalan
forest have been chosen jointly, the exact remaining owner-layer obstruction
is the following ordered Hall number.

For the free-port digraph `D` on the `C=Cat_m` rooted components, and a total
order `prec`, retain only forward arcs and split every component into a tail
copy and a head copy.  Write `B_prec(D)` for this bipartite graph and put

\[
 \delta_D(\prec)=
 \max_{X\subseteq V(D)}
 \bigl(|X|-|N_{B_\prec(D)}(X)|\bigr).                 \tag{0.1}
\]

Then

\[
 \boxed{\operatorname {pc}(D)=
        \min_\prec\delta_D(\prec)}                    \tag{0.2}
\]

is the minimum number of directed paths in a spanning free-port path cover.
In particular a one-path Catalan connector exists exactly when

\[
 \boxed{\exists\prec\ \forall X\subseteq V(D):
 |N_{B_\prec(D)}(X)|\ge |X|-1.}                       \tag{0.3}
\]

The order can be required to put a prescribed boundary component first and,
for a two-ended boundary macro, another prescribed component last.

Optimizing (0.1) only after all upstream choices gives the exact protected
min--max.  Failure has a sharp alternative:

* no compatible upper-exact rooted state exists; or
* every compatible rooted state and every boundary-compatible order has a
  Hall cut `X` with

  \[
       |N_{B_\prec(D)}(X)|\le |X|-2.                  \tag{0.4}
  \]

Equation (0.4), not ordinary connectivity or separate graphic rank, is the
exact port obstruction.

For the J6 opening of item 2488V, (0.3) must be imposed only after declaring
the macro component to be the global first component, imposing its nested
outgoing socket, and protecting a surviving provider of the removed upper
colour.  The cyclic-reservoir theorem proves none of these three global
rows automatically.

## 1. Rooted coordinates and the fixed macro

Let `ML_m` be the incidence graph between

\[
 {\cal L}={[2m-1]\choose m-1},\qquad
 {\cal M}={[2m-1]\choose m}.
\]

Put

\[
 W=|{\cal L}|=|{\cal M}|,\qquad
 U={2m-1\choose m+1},\qquad
 C=W-U=\operatorname {Cat}_m.                         \tag{1.1}
\]

Fix a protected boundary macro `P`.  Let `Phi(P)` be the allowed proper
alternating phase assignments on its path components.  For
`alpha in Phi(P)`, write

\[
                P=P_0(\alpha)\mathbin{\dot\cup}P_1(\alpha).   \tag{1.2}
\]

If the literal source macro already fixes its predecessor/successor phase,
then `Phi(P)` is a singleton.  Otherwise the phase is an upstream
existential choice and must remain inside the global minimum below.

The fixed-input hypotheses used below are the following.

1. `P` is a path forest after its declared boundary opening.  For every
   allowed phase used below, the short-shore upper labels on `P_1(alpha)`
   are pairwise distinct.  This holds for one
   doubly-`q1`-rainbow shared-bank packet.  The attached two-ended
   comparator has the corresponding **abstract** Johnson palettes, but its
   displayed source has the literal lower-cell defect isolated in Section
   10.1.  Proposition 10.1 gives a one-letter repair; the unmodified source
   is not an input to the physical theorem unless that colour is externally
   hosted.
2. The source-level local relation of the macro is already authenticated.
   In particular its internal residence and its claimed local upper
   transparency are not inferred from the connector theorem.
3. For each allowed phase, its casualty projection `R(P,alpha)` on the
   synchronized-common-basis ground is fixed before the common basis is
   selected.  When the projection is phase-independent we simply write
   `R(P)`.
4. The intended global boundary ports are declared.  For a prefix macro its
   incoming port must stay globally free.  For a two-ended macro the left
   incoming and right outgoing ports must stay globally free.

For the J6 opening, the extra boundary predicate is literal.  If the opened
path is oriented

\[
 H,L_0,\ldots,L_{h-1},M_0,\ldots,M_h,R_0,\ldots,R_{h-1},
\]

and the succeeding owners are `Y_1,Y_2,...`, then

\[
 p\in Y_1,\qquad
 d_i\in Y_1\cap\cdots\cap Y_{i+1}\quad(1\le i<h).     \tag{1.3}
\]

The removed immediate-upper colour must also have a surviving occurrence.
These are part of the admissibility predicate below, not consequences of
path connectivity.

## 2. Admissible common rooted states

For `alpha in Phi(P)`, let `B_sync(P,alpha)` be the family of synchronized
common bases which avoid the already fixed projection `R(P,alpha)`.  For
`beta in B_sync(P,alpha)`, an **admissible rooted state** is a pair
`(M_0,Q_0)` with the following properties.

1. `M_0` is a perfect incidence matching containing `P_0(alpha)` and
   realizing phase `alpha` of the macro.
2. For `e=LV notin M_0`, define

   \[
    \operatorname {up}(e)=M_0(L)\cup V,\qquad
    \lambda(e):L\longrightarrow M_0^{-1}(V).           \tag{2.1}
   \]

3. `Q_0 subset ML_m-M_0` is a matching containing `P_1(alpha)`, the map
   `up` is a bijection from `Q_0` to all `U` immediate-upper colours, and
   the labelled links `lambda(Q_0)` form a forest.
4. Every selected incidence is allowed by `beta` and by all fixed owner,
   guard, provider and cap decisions included in the declared state.
5. A protected prefix path begins at the free head of its `Q_0` component,
   and a protected suffix path ends at the free tail of its `Q_0` component.
   Thus these are literal global boundary ports, not merely named vertices
   somewhere inside a contracted component.

Write `Sigma(P)` for the set of quadruples

\[
                   \sigma=(\beta,\alpha,M_0,Q_0)       \tag{2.2}
\]

satisfying these conditions.  It is important that `Sigma(P)` is a **joint**
set.  Separate existence of `beta`, `M_0`, and an unprotected `Q_0` does not
prove that it is nonempty.

Since `|Q_0|=U`, its rooted forest has exactly

\[
                         W-U=C                         \tag{2.3}
\]

components, isolated vertices included.  Tail and head injectivity make
each component a coherently directed path.  For a component `K`, let
`t(K)` be its unique unused tail and `h(K)` its unique unused head.

The **guarded free-port digraph** `D_sigma` has these `C` components as
vertices.  It has the labelled arc

\[
                         K\longrightarrow K'           \tag{2.4}
\]

when the physical incidence from `t(K)` to the middle vertex `M_0(h(K'))`
exists, avoids all frozen resources, and passes every declared edge-local
splice guard.  Loops are excluded.  Distinct physical incidences remain
distinct labelled arcs, although parallel copies do not change the Hall
neighbourhoods.

Let `O_sigma(P)` be the allowed total orders of the components.  At the
owner/`q1` level it imposes only the declared boundary positions: the
component containing a prefix macro is first, and the two distinguished
components of a two-ended macro are first and last.  If those two protected
pieces lie in the same `Q_0` component while `C>1`, then
`O_sigma(P)=emptyset`: reserving both free ports of that component leaves no
way to traverse the other components.  If a source-level socket predicate
such as (1.3) has already been authenticated as a predicate of the **fully
expanded** component order, it may also be imposed here.  It is not an
edge-local port guard unless a state expansion or a single successor
component carries the whole required trace.

Arbitrary-width interval transparency is not automatically edge-local.  It
may be included in `O_sigma(P)` only when a separate source-lift theorem has
shown that the declared order predicate is sufficient.  Otherwise the
min--max below has exactly the owner/`q1` scope stated here.

## 3. Exact fixed-state path-cover theorem

For a total order `prec` on the components of `Q_0`, let
`D_sigma^prec` contain the arcs `K->K'` of `D_sigma` with `K prec K'`.
Let

\[
 B_{\sigma,\prec}=(\mathcal C_L,\mathcal C_R;E_\prec) \tag{3.1}
\]

be its split-copy bipartite graph.  Thus an arc `K->K'` becomes the edge
`K_L K'_R`.  For `X subseteq mathcal C_L`, the neighbourhood in (3.1)
uses the independent **right copies**; an underlying component is not
removed merely because its left copy belongs to `X`.

### Theorem 3.1 (ordered-Hall port min--max)

For a fixed admissible state `sigma`, the minimum number of components in a
spanning directed path forest selected from `D_sigma` is

\[
 \boxed{
 p(\sigma)=
 \min_{\prec}
 \max_{X\subseteq\mathcal C_L}
 \bigl(|X|-|N_{B_{\sigma,\prec}}(X)|\bigr).}           \tag{3.2}
\]

There is no rounding term.  If orders are restricted to
`O_sigma(P)`, then a boundary-compatible directed Hamilton path exists if
and only if

\[
 \boxed{
 \min_{\prec\in O_\sigma(P)}
 \max_X\bigl(|X|-|N_{B_{\sigma,\prec}}(X)|\bigr)=1.}  \tag{3.3}
\]

#### Proof

Fix `prec`.  A matching `A` in `B_(sigma,prec)` chooses at most one outgoing
and at most one incoming connector at every rooted component.  Every chosen
arc increases `prec`, so there is no directed cycle.  Under the in/out
degree bounds an undirected cycle would have to be coherently directed, so
there is no undirected cycle either.  The selected arcs form a spanning
directed path forest, with isolated components retained.  It has

\[
                         C-|A|                         \tag{3.4}
\]

paths.

Conversely, every spanning directed path forest has a topological total
order.  Its arcs are a matching in the corresponding forward split-copy
graph.  Maximizing the number of selected arcs for a fixed order and then
minimizing over orders proves

\[
 p(\sigma)=C-\max_\prec\nu(B_{\sigma,\prec}).          \tag{3.5}
\]

The deficiency form of Hall's theorem gives

\[
 C-\nu(B_{\sigma,\prec})
 =\max_X\bigl(|X|-|N_{B_{\sigma,\prec}}(X)|\bigr),    \tag{3.6}
\]

which proves (3.2).

A forward digraph has no perfect split-copy matching: such a matching would
select indegree and outdegree one everywhere and hence contain a directed
cycle.  Its deficiency is therefore at least one.  Equality in (3.3) gives
a matching of size `C-1`, hence a path forest on `C` vertices with one
component, namely a directed Hamilton path.  A Hamilton path has a unique
topological total order, its path order.  Thus if its prescribed boundary
components are first and last, that order lies in `O_sigma(P)`; conversely a
`C-1` matching for an order in `O_sigma(P)` produces a Hamilton path with
those boundary positions.  This proves (3.3). `square`

### Remark 3.2 (prescribed terminal ports)

The first/last formulation can equivalently be written as ordinary Hall
after deleting the forbidden incoming copy of the prescribed first
component and the forbidden outgoing copy of the prescribed last component.
For several already fixed connector paths, contract those paths first,
delete their consumed port copies, and apply Theorem 3.1 to the resulting
component digraph.  A protected directed cycle is an immediate obstruction;
it must first receive a declared opening.

### Proposition 3.3 (the exact factor/graphic-rank alternative)

Fix `sigma`, and let `G_sigma` be the full split-copy bipartite graph of
its admissible free ports, without imposing an order.  Unlike the path
digraph `D_sigma`, this factor-closure graph may include a physically
admissible self-closing port edge.  For a perfect
matching `A` of `G_sigma`, view its edges as a directed permutation of the
`C` rooted components.  Let `c(A)` be the number of directed cycles,
counting such a loop as a one-cycle, and let `r_gr(A)` be the graphic
rank of the same labelled component edges.  Then

\[
 c(A)=C-r_{\rm gr}(A),                                \tag{3.7}
\]

and the least number of components of a perfect two-factor completion of
the fixed rooted forest is

\[
 \boxed{\kappa(\sigma)=
   \min_{A\in\operatorname {PM}(G_\sigma)}c(A)
   =C-\max_{A\in\operatorname {PM}(G_\sigma)}r_{\rm gr}(A).} \tag{3.8}
\]

The value is infinity when `G_sigma` has no perfect matching.  Hall's
condition for `G_sigma` says only that the set in (3.8) is nonempty; it
does not bound `kappa(sigma)`.

#### Proof

A perfect split-copy matching gives every contracted component indegree
and outdegree one, hence is a disjoint union of directed cycles.  Its
underlying labelled graph has `C` vertices and `c(A)` connected
components, so its graphic rank is `C-c(A)`.  Expanding the already fixed
rooted paths does not change their number of cyclic components.  Taking
the minimum, equivalently the maximum graphic rank, proves (3.8). `square`

Deleting one arc from every cycle of an optimizer in (3.8) leaves a
`kappa(sigma)`-path cover.  Because `Q_0` itself retains one occurrence of
every immediate-upper colour, these deletions are automatically
immediate-upper transparent.  They need not be residence- or
higher-witness-transparent.  Thus (3.8) is the exact graphic-rank version
of the factor-first route, while Theorem 3.1 is the exact ordered-Hall
version of the path-first route.

## 4. The global protected connector min--max

Define

\[
 \Delta(P)=
 \min_{\substack{\sigma=(\beta,\alpha,M_0,Q_0)\in\Sigma(P)\\
                   \prec\in O_\sigma(P)}}
 \max_{X\subseteq\mathcal C_L}
 \bigl(|X|-|N_{B_{\sigma,\prec}}(X)|\bigr),           \tag{4.1}
\]

with value `infinity` when there is no admissible state or order.

### Theorem 4.1 (protected upper-exact boundary connector)

Assume the fixed macro's short-shore protected upper labels are pairwise
distinct in its selected allowed phase.  At the
owner/lower-`q1`/immediate-upper layer, there is a jointly
compatible spanning alternating Hamilton path which

1. contains the fixed opened macro;
2. uses a synchronized common basis avoiding `R(P,alpha)` in its selected
   phase;
3. realizes every immediate-upper colour; and
4. has the declared macro component(s) at the global boundary positions,

if and only if

\[
                              \boxed{\Delta(P)=1.}       \tag{4.2}
\]

#### Proof

Suppose (4.2) holds.  Choose its state, order and a `C-1` connector matching
`Q_1` supplied by Hall.  By Theorem 3.1 the connectors form a directed
Hamilton path on the components of `Q_0`.  Therefore

\[
                         Q=Q_0\mathbin{\dot\cup}Q_1     \tag{4.3}
\]

is an incidence matching, its labelled links form a spanning tree on the
`W` rooted vertices, and

\[
                         |Q|=U+(C-1)=W-1.              \tag{4.4}
\]

Contracting `M_0`, or equivalently applying the rooted Hamilton-path
identity, shows that `M_0 union Q` is a spanning alternating Hamilton path.
The bank `Q_0` contains exactly one occurrence of every immediate-upper
colour, so the path is upper-surjective.  All protected and boundary rows
hold because they were part of `Sigma(P)` and `O_sigma(P)`.

Conversely, take such a protected upper-surjective Hamilton path.  Choose
the induced allowed phase `alpha` for which `P_0(alpha)` lies on its perfect
alternating shore; call that shore `M_0` and its `W-1`-edge shore `Q`.  (If
the literal macro prescribed a unique phase, compatibility with that phase
is part of the theorem's hypothesis.)  For every upper colour choose one
carrying edge of `Q`; for the colours carried by `P_1(alpha)`, choose their
protected edges.  Pairwise distinctness of those labels makes this possible.
The selected set `Q_0` is a subset of a rooted path,
hence is a matching and a forest, and it is upper-exact.  Its `C` components
are joined by `Q-Q_0` into a directed Hamilton path.  Its component order is
boundary-compatible, and Theorem 3.1 gives deficiency one.  The common-basis
and fixed guards belong to the assumed certificate, so the resulting
`sigma` is admissible.  Thus (4.2) holds. `square`

### Corollary 4.2 (sharp obstruction)

Suppose `B_sync(P,alpha)` is nonempty for every
`alpha in Phi(P)` under consideration.  If the connector of Theorem 4.1
does not exist, exactly one of the following occurs.

1. For every avoiding synchronized common basis, no compatible
   `(M_0,Q_0)` or no allowed boundary order exists.
2. Compatible states and orders exist, but

   \[
   \forall\sigma\in\Sigma(P)\ \forall\prec\in O_\sigma(P)\
   \exists X\subseteq\mathcal C_L:
   |N_{B_{\sigma,\prec}}(X)|\le |X|-2.                \tag{4.5}
   \]

The second alternative is the exact min--max port obstruction.  Notice the
quantifier order: the Hall witness `X` may depend on both the common rooted
state and the total order.

## 5. Where the upper-exact state can fail

Theorem 4.1 does not hide the rooted representative problem.  For a fixed
predecessor matching `M_0`, let

* `M_L` and `M_H` be the tail and head partition matroids;
* `M_G` be the labelled rooted graphic matroid; and
* `M_U` be the immediate-upper-colour partition matroid.

If `P_1(alpha)` has `ell` edges, then a rooted state `Q_0` exists exactly
when the
four contractions

\[
 M_L/P_1(\alpha),\ M_H/P_1(\alpha),\
 M_G/P_1(\alpha),\ M_U/P_1(\alpha)                           \tag{5.1}
\]

have a common independent set of size `U-ell`, subject also to the declared
common-basis and guard restrictions.  Separate full rank of the four
contractions is not sufficient: this is a four-matroid correlation, not an
application of Edmonds' two-matroid min--max theorem.

Equivalently, one may use the exact binary system consisting of tail and
head capacities, one representative of every upper colour, and all graphic
forest cuts.  This characterizes `Sigma(P)` but does not prove it nonempty.

Thus the complete exact obstruction has two levels:

\[
 \boxed{
 \text{common four-row rooted-state feasibility}
 \quad+\quad
 \text{ordered split-copy Hall deficiency}.}          \tag{5.2}
\]

## 6. Transparent opening is extra data

There are two distinct transparency notions.

1. A **`q1`-transparent opening** deletes one incidence from each factor
   cycle while leaving a surviving selected occurrence of every
   immediate-upper colour.
2. A **witness-transparent opening** additionally leaves a surviving
   physical interval occurrence of every declared higher upper target and
   preserves its residence/source guards.

Let `F=M_0 union M_1` be an upper-surjective factor containing the protected
bank.  If one can choose one unprotected `M_1` edge in each of its `c`
cycles and the cuts are `q1`-transparent, then the retained shore

\[
                         Q=M_1-D                       \tag{6.1}
\]

is a rooted spanning path forest with `c` components.  Choosing one retained
occurrence of every upper colour gives `Q_0`; the remaining retained edges
give a `C-c`-edge port path cover.  Hence its topological order has
ordered-Hall deficiency at most `c`.  For `c=1` this is exactly a certificate
for (4.2).

Conversely, Theorem 4.1 constructs the path directly and therefore needs no
residual closure edge and no final factor opening.  This is the cleanest
additive-one certificate.

Neither Hamiltonicity nor the fixed-`H` planting theorem supplies a
transparent cut.  For the shared-bank cycle, every one of its `3h+2` cuts
creates exactly `2h` short positive endpoint fragments.  At J6, placing the
left end at the global boundary removes only that side's obligation; the
right side must still satisfy (1.3).  The removed upper colour must still
have a provider.  These conditions are logically prior to applying
Theorem 4.1 to the opened path.

Witness transparency is still stronger.  A single cut can cross many nested
higher-width witnesses.  No immediate-upper graphic-rank argument bounds
that exposure without a separately selected occurrence bank or a source
lift.  Therefore Theorem 4.1 becomes a full OR-word connector theorem only
after witness transparency, exterior residence and the common compiler cap
are supplied independently.

There is nevertheless an exact target-level opening test.  For one fixed
cyclic chronology `C` and a target `S` already represented in it, let
`W_C(S)` be all cyclic intervals whose OR is `S`, and define its witness
core

\[
 b_C(S)=\bigcap_{I\in W_C(S)}\operatorname {int}(I), \tag{6.2}
\]

where `int(I)` is the set of cyclic cut edges strictly crossed by `I`.
For every cut edge `e`,

\[
 \boxed{S\text{ survives the recut at }e
        \iff e\notin b_C(S).}                         \tag{6.3}
\]

Indeed, the recut retains exactly those cyclic intervals which do not
cross `e`; at least one witness survives precisely when `e` is absent from
the intersection in (6.2).  Consequently a whole target family `T`
survives one cut if and only if

\[
 e\notin\bigcup_{S\in T}b_C(S).                       \tag{6.4}
\]

For several factor cycles, with one cut variable `e_j` on each, the exact
row is the family of clauses

\[
 \bigvee_{I\in W(S)}
       \bigl(e_{\operatorname {cyc}(I)}
             \notin\operatorname {int}(I)\bigr)
 \qquad(S\in T).                                      \tag{6.5}
\]

Thus transparent opening is a joint occurrence-labelled cut system.  A
fixed-bank avoidance lemma can be applied to it only after the witness
system and its resulting forbidden projection have been fixed independently
of the common basis.  If connector choices create new witnesses or change
the chronology, the bank in (6.2)--(6.5) is adaptive and the marginal
avoidance argument does not apply.

## 7. What fixed-`H` planting and common-basis avoidance really prove

For `H` resource-disjoint shared-bank cycles, fixed before the ambient
choices, the existing theorems give:

\[
 H(6h+4)\le m-2
 \quad\Longrightarrow\quad
 \text{the cycles lie in some spanning `q1` two-factor},             \tag{7.1}
\]

and, for a fixed casualty projection with

\[
                    |R(P,\alpha)|\le aHh+bH,           \tag{7.2}
\]

the uniform synchronized-common-basis marginal gives

\[
 \exists\beta\in B_{\rm sync}:
                    \beta\cap R(P,\alpha)=\varnothing \tag{7.3}
\]

for every fixed `a,b,H` and all sufficiently large parameters.

Consequently (7.3) makes `B_sync(P,alpha)` nonempty for each phase whose
fixed projection obeys (7.2).  Equation (7.1) proves local owner/lower-`q1`
consistency.  Neither statement makes `Sigma(P)` nonempty, and neither
bounds `Delta(P)`: the two existential witnesses may be incompatible.

There is an additional topology qualification.  Each protected shared-bank
cycle in (7.1) is already saturated: all of its incidence vertices have
protected degree two.  Hence it is a whole factor component and cannot be
joined while all its transitions remain protected.  Before the path-cover
theorem applies, one transition (such as J6) must be declared replaceable,
and its exact residence, palette-provider and source-socket debts must be
included in the state.

The order of quantifiers in (7.3) is

\[
       \boxed{\text{fix }P,\alpha\text{ and }R(P,\alpha),\quad
              \text{then choose }\beta.}               \tag{7.4}
\]

If the casualty set is allowed to depend on `beta`, the one-point marginal
argument does not apply.

The failure is visible in the two-point toy family
`B_sync={{a},{b}}` with its uniform distribution.  Every fixed singleton
bank is avoided by one common basis, since each marginal is `1/2`; but the
adaptive rule `R({a})={a}`, `R({b})={b}` is met by every selected basis.
This is exactly the invalid exchange from `for every fixed R, there exists
beta` to `there exists beta avoiding R(beta)`.

Also, (7.1) is only asymptotic at fixed `H`.  At the active `k=17` values
`m=9,h=3,H=1`, its required inequality is `22<=7` for the protected cycle
(and the older path bound already required `18<=7`).  Thus it supplies no
finite `k=17` planting theorem.

## 8. Quantifier audit

The exact proof order is

\[
 \begin{gathered}
 \text{fix the macro }P;\\
 \exists\alpha\text{ among the source-compatible proper phases};\\
 \text{fix its literal projection }R(P,\alpha);\\
 \exists\beta\text{ avoiding that projection};\\
 \exists(M_0,Q_0)\text{ jointly compatible with }\beta\text{ and }P;\\
 \exists\prec\text{ satisfying the declared boundary/socket state};\\
 \forall X\subseteq\mathcal C_L:
        |N_{B_{\sigma,\prec}}(X)|\ge |X|-1;\\
 \exists\text{ the resulting connector matching};\\
 \exists\text{ a source lift and common cap, if the full OR word is claimed}.
 \end{gathered}                                         \tag{8.1}
\]

The following exchanges are invalid.

1. `exists beta` and `exists factor` cannot be replaced by an unproved
   compatible pair.
2. `M_0` cannot be fixed arbitrarily before phasing the protected macro;
   when the source has not fixed the phase, `alpha` belongs inside the outer
   existential.
3. `Q_0` cannot be chosen after proving Hall in an averaged port graph;
   the port graph depends on `Q_0`.
4. The ordered-Hall row is `exists order, for every cut`.  It is neither an
   all-orders assertion nor `for every cut, exists an order`.
5. An arbitrary cycle edge cannot be deleted and called transparent.
6. A local all-width-transparent macro cannot be promoted to a globally
   upper-complete source without a spanning source-lift theorem.

## 9. Sharpness and counterexamples to weaker projections

### 9.1 Strong connectivity is insufficient

Take a bidirected star on `n` port components.  It is strongly connected,
but its centre can have at most one selected incoming and one selected
outgoing arc.  At most two leaves can lie on the path containing the centre,
so every spanning path cover has at least `n-2` paths.  By Theorem 3.1 its
optimized ordered-Hall deficiency is exactly `n-2`.

Thus connectivity, and even strong connectivity, does not give a bounded
connector.

### 9.2 Distinct ports, colours and protected acyclicity are insufficient

For the authenticated `m=3` predecessor matching, the protected arcs

\[
                        A\to D,\qquad C\to H,\qquad J\to F             \tag{9.1}
\]

have distinct tails, heads and upper colours and form a directed linear
forest, but they lie in no directed Hamilton path.  Therefore the predecessor
matching and protected phase must be chosen correlatively; separate local
ranks cannot replace (4.1).

### 9.3 Upper exactness is insufficient

The authenticated `m=4` upper-exact rooted forest has `C=14` components but
residual physical matching rank `11/14`.  This is an actual middle-level
fixture showing that a rooted Catalan forest alone does not provide the
free-port connector.

These examples do not disprove a future large-dimensional theorem which
chooses the whole state jointly.  They do prove that the four ingredients
listed in Section 7 cannot be concatenated without the min--max row (4.1).

## 10. Application to the two present boundary macros

### 10.1 Two-ended clipped double-rainbow comparator

At its stated **two-global-boundary** placement, most of the attached
comparator's symbolic ledger is valid: it has the asserted
phase-independent simple owner chronology, both *abstract* Johnson edge
palettes are injective, its owner runs have the claimed clipped lower
bound, and its phase difference consists of the stated endpoint rays.
The transport is not width-preserving: an old interval crossing the
insertion acquires one source position.  Thus it does not by itself protect
a prescribed derivative-row address.

There is also one literal-source defect in the attached theorem as written.
At the central transition the two owners are

\[
 O_L=K+a_1+a_3+p_L+F,
 \qquad O_R=K+a_1+a_3+p_R+F.                           \tag{10.1}
\]

Their rank-`r-1` intersection is

\[
 I=K+a_1+a_3+F.                                       \tag{10.2}
\]

But the `d` shared source letters are exactly the bridge
`G=(f_d,\ldots,f_1)`, whose OR is only `F`.  Hence the central abstract
lower colour `I` is **not** the literal depth-`d-1` source cell.  In fact no
displayed interval realizes `I`: every displayed source letter containing
`K,a_1,a_3` also contains an extra marker.  Therefore the attached claim of
a literal double-`q1` physical source is false at this edge.  The connector
theorem may use the comparator only after a source repair is proved, or
with `I` carried as an explicit external lower ticket.  Merely observing
that the owner intersection exists is insufficient.

### Proposition 10.1 (one common bridge screen repairs literal `q1`)

In both phase words replace the **single first bridge position**
`{g_1}` in `G` by

\[
                 K+\{a_1,a_3,g_1\}.                  \tag{10.3}
\]

Do not alter the later endpoint letter which also contains coordinate
`g_1`.  Then all `4d+2` owners and their order are unchanged; every
abstract lower edge intersection is now the OR of the corresponding `d`
shared source letters; every upper edge union remains the OR of the
corresponding `d+2` source letters; and both literal `q1` palettes are
injective.  The phase-to-phase signed interval difference remains exactly
the original `2d-2` endpoint rays, and all rank-`r` and strict-upper
occurrences are unchanged.

#### Proof

The bridge position `g_1` immediately follows `Q_L`, while `Q_R` occurs
exactly `d` positions after it.  Every length-`d+1` window containing that
position therefore contains `Q_L`, except the window starting there, which
contains `Q_R`.  Both screens already contain `K,a_1,a_3`; hence (10.3)
changes no owner.

Every noncentral shared `d`-letter block containing the position `g_1`
also contains an old common screen and was already tight.  The only changed
shared block is the central bridge `G`.  Its repaired OR is

\[
                 K+\{a_1,a_3\}+F=O_L\cap O_R,        \tag{10.4}
\]

which repairs the unique defect.  Upper cells and the abstract owner
palettes are unchanged, proving the literal `q1` claims.

The only source intervals changed by (10.3) are

\[
                 (g_1,g_2,\ldots,g_j),\qquad1\le j\le d. \tag{10.5}
\]

Their old ranks are `j`; their new ranks are

\[
 |K|+2+j=r-d-1+j\le r-1.                              \tag{10.6}
\]

Thus no rank-`r` or strict-upper value is altered.  The same common repair
is made in both phases, and none of the endpoint intervals responsible for
the signed ray difference reaches this bridge position; the phase ledger
is unchanged. `square`

The qualification in (10.5) is load-bearing.  Proposition 10.1 is not
pointwise deck-transparent relative to the unmodified source: it replaces
those `d` low cells and deliberately creates the missing rank-`r-1`
central cell.  It preserves the owner and upper decks and the exact
phase-to-phase relation, which are the claims used here.

The endpoint hypothesis is load-bearing.  If the left variable letter
`Z_epsilon=K+z+x_epsilon+f_1` is moved into the interior and is preceded by
the `d` singleton letters

\[
                c_1,c_2,\ldots,c_{d-1},\ell,          \tag{10.7}
\]

then the new length-`d+1` window ending at `Z_epsilon` has OR

\[
 K+z+x_\varepsilon+f_1+C+\ell,                       \tag{10.8}
\]

which has rank `r` and depends on the phase.  The successive crossing
windows may themselves be chosen as a Johnson collar, so this is an
owner-level obstruction, not merely a hostile arbitrary source context.
Adding one exterior coordinate also gives a changed strict-upper interval.
The right endpoint has the symmetric obstruction.  Hence generic
fixed-`H` factor planting cannot internalize this comparator without a new
two-sided screening collar.

The two internal collar paths alone have `d` Johnson transitions on each
side, hence `4d` incidence edges in total.  Conditional on resource
disjointness, `H` pairs can be planted by the small protected-factor theorem
when `4Hd<=m-2`.  This only plants their owner/`q1` paths; it does not put
them at the two global ends or supply the intervening source cocycle.

For a repaired genuine two-ended application, contract the left and right
protected paths inside `Q_0`, require their **distinct** components to be
first and last in `O_sigma(P)`, and apply (4.1).  If they lie in one
component and `C>1`, no such order exists.

At the owner/`q1` layer, the exact remaining boundary-completion statement
is precisely

\[
                              \Delta(P)=1.              \tag{10.9}
\]

The repaired comparator does not prove (10.9): it constructs the fixed
boundary state but not the common rooted state or the Catalan-scale port
expansion.  Even after (10.9), the terminal lower compiler and the ambient
arbitrary-width upper source lift remain separate.

### 10.2 Shared-bank J6 prefix

Open the resident cycle at `R_(h-1)->H`, protect a surviving provider of the
removed upper colour, and put its protected component first.  Restrict
`O_sigma(P)` to expanded orders satisfying (1.3).  Then (4.2) is the exact
owner-layer protected Hamilton connector theorem around J6.

The cycle planting and common-basis avoidance theorems say that the fixed
packet is asymptotically consistent and avoidable.  They do not prove that
the restricted minimum in (4.1) is one.  This is the sharp remaining
connector obstruction.

## 11. Final theorem boundary

The new unconditional conclusion is the exact equivalence

\[
 \boxed{
 \text{protected upper-exact owner connector exists}
 \iff
 \min_{\substack{\text{avoiding common rooted states}\\
                  \text{boundary-compatible orders}}}
 \max_{\text{split-copy Hall cuts}}
 \text{deficiency}=1.}                                 \tag{11.1}
\]

This is a genuine min--max theorem, with an explicit cut obstruction when it
fails.  It does not turn the current ingredients into an unconditional
all-dimensional connector: the common four-row rooted state, the ordered
one-defect Hall bound, the J6 socket/provider, witness-transparent source
opening, exterior residence and the common cap still require a joint
construction.
