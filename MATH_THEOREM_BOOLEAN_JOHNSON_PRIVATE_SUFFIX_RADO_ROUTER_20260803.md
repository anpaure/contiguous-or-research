# Boolean--Johnson containment and the residual typed private suffix router

**Date:** 2026-08-03
**Status:** exact fixed-linkage Rado/Hall theorem, an unconditional
occurrence-lifted Boolean specialization, and sharp obstructions.  The
theorem does not assert that the second occurrence coordinate of the current
`B+1` host has the required occurrence lift.

## 0. Answer

Boolean-lattice or Johnson **value** expansion does not by itself give the
simultaneous typed private suffix router required by the `B+1` pivot
architecture.  It does give such a router after one additional physical
statement: the relevant containments must lift, in one materialized state
and after one fixed compensation linkage has been deleted, to an
occurrence-capacity-faithful suffix network.

The weakest exact one-coordinate condition after private claim prefixes have
been fixed is the Rado inequality

\[
 \boxed{
 r_{\Gamma}\!\left(\bigcup_{g\in X}A_g\right)\ge |X|
 \qquad(X\subseteq G),}
\tag{0.1}
\]

where \(A_g\) is the complete physical port menu of claim \(g\), and
\(\Gamma\) is the typed suffix gammoid in the residual network.  The often
used full-port condition

\[
                         r_\Gamma(P)=|P|                 \tag{0.2}
\]

is sufficient for (0.1) when the claim--port incidence graph has Hall, but
is not necessary.

If the residual suffix network is an exact private incidence lift of a
bipartite port--sink graph \(H\), then (0.1) is the following pure nested
Hall condition:

\[
 \boxed{
 |A(X)\setminus Y|+|N_H(Y)|\ge |X|
 \quad(X\subseteq G,\;Y\subseteq A(X)),}
\tag{0.3}
\]

where \(A(X)=\bigcup_{g\in X}A_g\).  For routing every active port, this
reduces to ordinary Hall:

\[
                         |N_H(Y)|\ge |Y|\qquad(Y\subseteq P). \tag{0.4}
\]

Thus Boolean containment expansion can close the router by proving (0.3)
or (0.4) for the **residual occurrence graph**.  It cannot replace that
graph by a value projection.

For a `q1` two-factor there is an especially small positive theorem.  If
every factor incidence lifts after compensation deletion to its literal
typed Boolean diamond, the two-factor decomposes into perfect matchings and
one matching gives a full suffix linkage.  The native diagonal-interval
theorem proves this occurrence geometry for one coordinate; survival after
the frozen compensation deletion is still a coexistence premise.  No
current theorem supplies the analogous residual lift for the other
coordinate and the transported background under the same cap.

## 1. Fixed compensation linkage and residual typed network

Fix one complete cap, guard, common-state, occurrence, and terminal-type
state \(c\).  Fix one occurrence-labelled compensation linkage \(L_I\).
This note uses the frozen model:

\[
 D^{\rm res}=D^c-\operatorname{cap}(L_I),
 \qquad
 T^{\rm res}=T^c-T(L_I).                              \tag{1.1}
\]

Every unit physical capacity used by \(L_I\), and every sink slot occupied
by it, is deleted.  This is not adaptive matroid contraction.  In
particular, the number of compensation paths does not bound the number of
deleted physical capacities.

Let \(P\) be the active set of physical occurrence-labelled ports.  Equal
Boolean values at different addresses are different ports.  Aliases of one
physical cell pass through one common capacity-one gate and are not counted
as independent ports.

Let \(T^{\rm type}\subseteq T^{\rm res}\) be the residual typed sink bank.
All finite shared capacities are node-split and represented once.  Terminal
type is enforced by the network: either type blocks are capacity-disjoint,
or a proved type gadget prevents a port from reaching an illegal sink.  A
mere declaration on a path after an anonymous switch is not enough.

Reserve every literal claim-to-port prefix interior exclusively for its
claim catalogue and remove those interiors from the suffix network.  The
remaining suffix network is denoted \(D_{\rm suf}\).  Its strict gammoid on
the port vertices is

\[
             \Gamma=L(D_{\rm suf},T^{\rm type})|P.     \tag{1.2}
\]

All ranks below are computed in (1.2), hence after (1.1).  If a suffix
shares a deleted compensation capacity, it is absent.  If two suffixes
share a surviving physical capacity, that capacity occurs once in
\(D_{\rm suf}\).

## 2. The exact private-prefix Rado theorem

Let \(G\) be the gain-claim set.  For every \(g\in G\), let

\[
                              A_g\subseteq P            \tag{2.1}
\]

be its complete residual menu of legal physical ports.  For every
\(p\in A_g\), fix a literal prefix \(Q_{g,p}:s_g\leadsto p\).  Assume:

1. prefixes chosen for distinct claim--port incidences have disjoint
   interiors; prefixes of one claim may share only their claim start;
2. different prefixes may meet at a port only when they end at that same
   physical port;
3. a prefix meets the suffix network only at its own terminal port;
4. prefixes avoid every capacity and sink deleted in (1.1);
5. every prefix, port, suffix state, and sink type belongs to the same
   fixed state \(c\); and
6. the displayed interface is complete: every admitted physical service
   route uses one declared prefix and then a route represented in
   \(D_{\rm suf}\).

### Theorem 2.1 (weakest exact one-coordinate router condition)

A claim set \(S\subseteq G\) is serviceable through this interface if and
only if it has distinct representatives \(p_g\in A_g\) whose representative
set is independent in \(\Gamma\).  Consequently the serviceable claim sets
form a Rado matroid \(R\) on \(G\), with rank

\[
 \boxed{
 \rho_R(S)=
 \min_{X\subseteq S}
 \left(|S\setminus X|+
 r_\Gamma\!\left(\bigcup_{g\in X}A_g\right)\right).}
\tag{2.2}
\]

In particular, every claim is simultaneously serviceable if and only if
(0.1) holds.

#### Proof

Suppose first that representatives \(p_g\) form an independent set of
\(\Gamma\).  Link them by vertex-disjoint suffix paths to distinct legal
sinks.  The representatives are distinct.  Conditions 1--3 make the
selected prefixes mutually disjoint and disjoint from every suffix except
at the intended concatenation port.  Conditions 4--6 make the concatenated
paths literal routes in the same residual physical state.

Conversely, a service linkage through the complete interface chooses one
declared port for each serviced claim.  Unit port capacity makes those
ports distinct, and deleting the private prefixes leaves a suffix linkage,
so the chosen ports are independent in \(\Gamma\).

The rank formula is Rado's theorem.  Substituting \(S=G\), formula (2.2)
has value \(|G|\) exactly when

\[
 r_\Gamma(A(X))\ge |X|
 \quad\text{for every }X\subseteq G.
\]

This proves all assertions. \(\square\)

### Corollary 2.2 (bounded one-coordinate defect)

If

\[
 r_\Gamma(A(X))\ge |X|-C
 \qquad(X\subseteq G),                                \tag{2.3}
\]

then \(\rho_R(S)\ge |S|-C\) for every \(S\subseteq G\).  In particular,
all but at most \(C\) claims are serviceable.

The full-port rank (0.2) implies (0.1) whenever the abstract claim--port
incidence satisfies \(|A(X)|\ge|X|\).  A left \(h\)-regular,
right-at-most-\(h\) incidence factor has this property by edge counting.
However, (0.1) may hold even when some ports are loops in \(\Gamma\), so
(0.2) is strictly stronger than the exact claim condition.

## 3. Exact private incidence lifts and nested Hall

Let \(H=(P,Q;E_H)\) be a bipartite graph whose right vertices are distinct
residual typed sink occurrences.  Call \(H\) an **exact private incidence
lift** when an edge \(pq\) is a complete literal suffix bundle, every edge
interior is private, the only finite capacities shared by two edge bundles
are their displayed port or sink endpoints, and every catalogue suffix is
one of these bundles.  Equivalently, after contracting private interiors,
the suffix network is the directed unit-capacity realization of \(H\).

### Theorem 3.1 (nested Hall form)

For an exact private incidence lift,

\[
 r_\Gamma(Y)=
 \min_{Z\subseteq Y}
 \bigl(|Y\setminus Z|+|N_H(Z)|\bigr)                 \tag{3.1}
\]

for \(Y\subseteq P\).  Hence Theorem 2.1 services every gain if and only if
(0.3) holds.  The maximum number of active ports routable through the
catalogue is

\[
 |P|-\max_{Y\subseteq P}\bigl(|Y|-|N_H(Y)|\bigr).   \tag{3.2}
\]

#### Proof

The linkable port sets are exactly the partial transversals of \(H\), so
they form its transversal matroid and have rank (3.1).  Substitute (3.1)
into (0.1) to obtain (0.3).  Hall's deficiency theorem gives (3.2).
\(\square\)

If edge bundles share an internal capacity, (3.1) is not asserted.  One
must keep that capacity in \(D_{\rm suf}\) and use the gammoid rank in
(0.1).  Thus (0.1), not (0.3), is the weakest exact statement for a general
physical suffix network.

## 4. Weighted Boolean containment

Fix one type and ranks \(a<b\) in a Boolean lattice on an \(n\)-point
ground set.  Let \(u(A)\) be the number of active unit port occurrences of
value \(A\in\binom{[n]}a\), and let \(w(B)\) be the number of residual unit
sink occurrences of value \(B\in\binom{[n]}b\).  All multiplicities are
physical capacities after compensation deletion; two labels aliasing one
unit cell contribute one, not two.

Assume every containment \(A\subset B\) between a positive-multiplicity
port value and sink value has an exact private occurrence lift.  For
\({\cal F}\subseteq\binom{[n]}a\), write

\[
 \nabla_b({\cal F})=
 \{B\in\tbinom{[n]}b:\text{some }A\in{\cal F}
                                      \text{ satisfies }A\subset B\}.
\tag{4.1}
\]

### Theorem 4.1 (exact weighted-shadow criterion)

Every active port routes to a distinct residual typed sink if and only if

\[
 \boxed{
 \sum_{B\in\nabla_b({\cal F})}w(B)
 \ge
 \sum_{A\in{\cal F}}u(A)
 \qquad
 (\mathcal F\subseteq\tbinom{[n]}a).}
\tag{4.2}
\]

#### Proof

Apply Hall to the occurrence graph.  The neighborhood of a port-occurrence
set depends only on the support \({\cal F}\) of its Boolean values.  For a
fixed support, the largest demand is obtained by taking all \(u(A)\)
occurrences of every \(A\in{\cal F}\).  Therefore the occurrence-level Hall
inequalities are equivalent to (4.2). \(\square\)

### Corollary 4.2 (uniform containment expansion)

Suppose \(u(A)\le u_0\) and \(w(B)\ge w_0\) on the two complete layers.  A
sufficient condition for (4.2) is

\[
 w_0{\binom{n-a}{b-a}}
 \ge
 u_0{\binom ba},                                      \tag{4.3}
\]

or equivalently

\[
                 w_0{\binom nb}\ge u_0{\binom na}.    \tag{4.4}
\]

#### Proof

Every \(a\)-set lies in \(\binom{n-a}{b-a}\) members of the upper layer,
and every \(b\)-set contains \(\binom ba\) members of the lower layer.
Double-count incidences from \({\cal F}\) to its upper shadow and use the
two multiplicity bounds. \(\square\)

For the odd `B+1` host, \(n=2r-1\).  Between ranks \(r-1\) and \(r\), the
two layers have equal size and (4.3) holds with \(u_0=w_0=1\).  This is the
ordinary balanced Middle-Levels Hall expansion.

Between ranks \(r-1\) and \(r+1\), however,

\[
 {\binom{2r-1}{r+1}\over\binom{2r-1}{r-1}}
 ={r-1\over r+1}.                                    \tag{4.5}
\]

One sink occurrence per upper value therefore cannot route the complete
rank-\((r-1)\) layer.  Two per upper value are a simple sufficient
condition, but are much stronger than the exact weighted criterion (4.2).

Upper-value surjectivity plus the correct total number of terminal
occurrences is not enough.  Put

\[
 W=\binom{2r-1}{r-1},\qquad
 U=\binom{2r-1}{r+1},\qquad E=W-U.
\]

Give every upper value one occurrence and put all \(E\) additional
occurrences on one upper set \(B_0\).  If

\[
                    1+E>\binom{r+1}{2},               \tag{4.6}
\]

take \({\cal Y}=\binom{B_0}{r-1}\) and
\({\cal F}=\binom{[2r-1]}{r-1}\setminus{\cal Y}\).  No occurrence of
value \(B_0\) lies in \(N({\cal F})\), so

\[
 |N({\cal F})|\le W-(1+E)<W-|{\cal Y}|=|{\cal F}|.
\tag{4.7}
\]

Indeed,

\[
 E={2W\over r+1},
 \qquad
 W=\prod_{i=1}^{r-1}{r+i\over i}\ge2^{r-1},          \tag{4.7a}
\]

so (4.6) holds throughout the sufficiently large `B+1` regime.
Thus even a surjective upper palette with \(W\) distinct physical sink
slots need not satisfy Hall when only its value multiplicities are known.

There is an important positive exception.  If the terminal occurrences
have distinct anchors \(a(q)\in P\), the anchor map is a bijection, and

\[
                         v(a(q))\subset v(q),          \tag{4.8}
\]

then the anchor edges themselves form an abstract perfect matching.  A
`q1` transition ledger has exactly this semantic form: its lower transition
is contained in its upper union.  What remains to be proved is that (4.8)
lifts to residual typed occurrence routes; value containment alone does not
create those routes.

## 5. The `q1` factor-diamond router

Let \(F=(P,O;E_F)\) be a spanning two-factor of the Middle-Levels incidence
graph: every lower port \(p\in P\) and every owner occurrence \(o\in O\)
has degree two.  For each \(p\), let \(q_p\) be a distinct residual terminal
occurrence whose declared value is the union of the two owner values
adjacent to \(p\).

Assume that, after (1.1), every incidence \(po\in E_F\) has a literal typed
diamond suffix

\[
                            R_{p,o}:p\leadsto o\leadsto q_p, \tag{5.1}
\]

and that different displayed bundles share finite capacity only at the
ports, owner occurrences, or their common terminal \(q_p\).  Every
\(q_p\) is legal for every claim which may select \(p\).  Prefix interiors
are private from all bundles (5.1).

### Theorem 5.1 (unconditional factor-diamond router)

The full port set \(P\) has pairwise vertex-disjoint typed suffixes to the
distinct terminals \(\{q_p:p\in P\}\).

#### Proof

Every component of \(F\) is an even alternating cycle.  Choose one of its
two alternating perfect matchings, independently on every component.  The
union \(M\) is a perfect matching from \(P\) to \(O\).  Use the bundle
\(R_{p,M(p)}\) for every \(p\).  The selected ports, owners, and terminals
are separately injective, and the private-interior hypothesis accounts for
all other capacities. \(\square\)

This theorem needs neither a Hamilton factor nor global Johnson expansion.
It needs the physical occurrence diamonds in one residual state.  The
native diagonal-interval theorem supplies their occurrence geometry for one
coordinate by the explicit routes

\[
 p_i-o_i-q_i,
 \qquad
 p_i-o_{i+1}-q_i.                                    \tag{5.2}
\]

They are residual routes only when the chosen compensation linkage and the
reserved prefix interiors avoid their finite capacities and terminal slots.
That additional coexistence is not supplied by the abstract diamond
identities.

For a linear opening, the interior bundles route every interior port.  One
external boundary bundle restores the omitted seam; without it the
canonical catalogue has deficiency at most one.

### Residual damage inside the factor catalogue

Let \(F^{\rm res}\) retain precisely those incidences whose complete bundle
(5.1) survives compensation deletion, type filtering, and prefix
reservation.  If no extra suffix bundles are admitted, the factor catalogue
has a full router exactly when

\[
 |N_{F^{\rm res}}(X)|\ge|X|\qquad(X\subseteq P).      \tag{5.3}
\]

On one undeleted factor cycle there are only two perfect matchings.
Therefore, when every port, owner, and terminal remains and only incidence
bundles are removed, (5.3) holds on that component exactly when one of its
two alternating matching classes survives in full.  Extra residual
suffixes may repair a failed factor catalogue, in which case the general
gammoid condition (0.1) is the correct test.

## 6. Sharp physical obstructions

### Proposition 6.1 (one fixed compensation path can erase arbitrary rank)

For every \(N\), there is a suffix network with \(N\) pairwise-disjoint
typed containment routes before compensation and a single compensation
path whose frozen deletion leaves suffix rank zero.

#### Proof

Take distinct ports \(p_i\), unit vertices \(v_i\), and distinct legal
sinks \(q_i\), with private routes

\[
                         p_i\to v_i\to q_i
                         \qquad(1\le i\le N).          \tag{6.1}
\]

Give the endpoints any distinct Boolean labels satisfying the desired
containments.  Add a compensation start \(b\), a compensation sink \(t\),
and arcs making

\[
                         b\to v_1\to v_2\to\cdots\to v_N\to t \tag{6.2}
\]

one directed path.  Before (6.2) is protected, the routes (6.1) are
pairwise disjoint.  Freeze (6.2) as \(L_I\).  Equation (1.1) deletes every
\(v_i\), so every port is a loop in the residual suffix gammoid. \(\square\)

Thus neither the number of compensation claims nor abstract containment
expansion bounds residual router damage.  One needs privacy from the
complete footprint of \(L_I\), or the residual rank/cut inequality itself.

### Proposition 6.2 (marginal coordinate Hall does not give a joint router)

For every \(N\), two occurrence coordinates may each have a full typed
containment router while their joint demand has rank only \(N\).

#### Proof

Let each coordinate route its \(N\) ports bijectively to the same physical
bank of \(N\) unit terminal occurrences.  Marginally both ranks are \(N\).
If the two coordinate roles require distinct terminal units, their joint
demand is \(2N\) behind a terminal cut of capacity \(N\). \(\square\)

The only escapes are a capacity-separated terminal copy for each
coordinate, an allocated common-cap split, or a proved coalesced bundle in
which the two roles legally consume one occurrence.  Two marginal Hall
proofs do not establish any of these.

The same warning applies to type.  Untyped Boolean Hall can match a port to
a sink of the wrong terminal type.  Type blocks must be built into
\(D_{\rm suf}\) or into the exact incidence graph before Hall is applied.

## 7. Exact two-coordinate premise for the `B+1` architecture

Let \(I\) now be the union of the logical cross-ray tickets, let \(Z\) be
the structural-zero set in the two coordinate Rado systems, and put
\(G=I\setminus Z\).  The index \(j\in\{0,1\}\) denotes the two physical
occurrence coordinates required of every ticket, not the two alternating
matchings of a `q1` factor.  In one common state \(c\), after deleting the
fixed coordinate-specific realizations of the declared compensation service
and allocating every shared cross-coordinate capacity, let

\[
 D_j^{\rm res}=D_j^c-\operatorname{cap}(L_{I,j}),
 \qquad T_j^{\rm res}=T_j^c-T(L_{I,j}).               \tag{7.1}
\]

Reserve the coordinate-\(j\) prefix interiors and define

\[
 \Gamma_j=L(D_{{\rm suf},j},T_j^{\rm res})|P_j,
 \qquad A_{j,g}\subseteq P_j.                         \tag{7.2}
\]

The weakest exact zero-defect marginal premise is

\[
 \boxed{
 r_{\Gamma_j}\!\left(\bigcup_{g\in X}A_{j,g}\right)
 \ge |X|
 \quad(X\subseteq G,\ j=0,1).}
\tag{7.3}
\]

Under global product closure, (7.3) services every ticket in \(G\) in both
coordinates.  For common ray deficiency on \(G\) at most \(C\), the exact
premise is the two-Rado inequality

\[
 \boxed{
 \max_{\substack{X_0,X_1\subseteq G\\X_0\cap X_1=\varnothing}}
 \left[
 |X_0|-r_{\Gamma_0}(A_0(X_0))
 +|X_1|-r_{\Gamma_1}(A_1(X_1))
 \right]\le C.}
\tag{7.4}
\]

The total terminal deficiency is obtained by adding \(|Z|\) and any omitted
background targets exactly as in the terminal common-cap theorem.  A
convenient stronger sufficient form is

\[
 r_{\Gamma_j}(A_j(X))\ge|X|-C_j
 \quad(X\subseteq G),\qquad C_0+C_1\le C.            \tag{7.5}
\]

The current `B+1` inventory proves the native diagonal occurrence geometry
and its one coalesced boundary ticket.  It does not prove that this whole
catalogue survives the fixed compensation deletion, nor (7.3), (7.4), or a
factor-diamond lift for the remaining coordinate.  It also does not prove
global product closure with the transported background.

Accordingly, the exact remaining geometric premise can be stated in either
of two proof-safe forms:

1. **minimal:** prove (7.4) directly in the two residual typed suffix
   gammoids, together with global product closure; or
2. **structural:** construct, for the unclosed coordinate, residual literal
   factor diamonds satisfying Theorem 5.1 (allowing a fixed exceptional
   set), private from prefixes and \(L_I\), and then prove cross-coordinate
   capacity separation or legal coalescence.

The endpoint-balanced bounded-overload certificate of
`MATH_THEOREM_BOOLEAN_INCIDENCE_OVERLOAD_SUFFIX_ROUTER_20260803.md` is a
third, weaker-than-preselected-linkage sufficient route to (7.5).  Its
occurrence catalogue and normalized residual overload are themselves
physical hypotheses; Boolean containment does not supply them automatically.

## 8. Scope

Theorems 2.1, 3.1, 4.1, and 5.1 are unconditional mathematical statements
under their displayed fixed-network hypotheses.  Proposition 6.1 is a
sharp reason that compensation deletion must occur before any expansion
claim.  Proposition 6.2 is a sharp reason that two marginal routers require
product closure or a joint capacity theorem.

No assertion is made that the current all-dimensional Pascal host has the
second occurrence lift, typed terminal acceptance, compensation privacy,
or common-cap product closure.  Transported phase 1 remains theorem input
only.  Therefore this note proves no unconditional `B(k)+O(1)` or `B+1`
upper bound.
