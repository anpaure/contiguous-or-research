# Factor-restricted Rado, degree-weighted suffix flow, and a Middle Levels corridor router

**Date:** 2026-08-04  
**Status:** pure-mathematical theorem.  This note weakens the full-active-port
router premise in
`MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`.
It also gives a sufficient router from a capacity-faithful bidirected Middle
Levels corridor.  It does **not** prove that the present all-dimensional
compiler contains such a literal corridor, and it does not prove
\(\nu(k)=B(k)+O(1)\).

## 0. Main conclusion

Fix one fully materialized cap/guard/occurrence state and one fixed
compensation linkage.  Let

\[
 B=(G,P;E)
\]

be the literal claim-to-port incidence factor, and let \(\Gamma\) be the
typed strict gammoid of the residual suffix network on the physical port
set \(P\).

The full-port condition

\[
                         r_\Gamma(P)=|P|                 \tag{0.1}
\]

is sufficient, but it is stronger than the factor needs.  The exact
factor-restricted condition is

\[
 \boxed{
 r_\Gamma(N_B(X))\ge |X|
 \qquad(X\subseteq G).}                                  \tag{0.2}
\]

Equivalently, the exact deficiency of the displayed factor-router
architecture is

\[
 \boxed{
 \delta_B=
 \max_{X\subseteq G}
 \bigl(|X|-r_\Gamma(N_B(X))\bigr).}                       \tag{0.3}
\]

There is an equivalent trapped-menu form.  For \(U\subseteq P\), put

\[
 H_B(U)=\{g\in G:N_B(g)\subseteq U\}.
\]

Then exact routing is equivalent to

\[
 \boxed{|H_B(U)|\le r_\Gamma(U)\qquad(U\subseteq P).}    \tag{0.3a}
\]

Equivalently again, every physical suffix separator must have capacity at
least the number of gains whose complete port menu is trapped behind that
separator.  This is the exact factor-specific cut invariant; it is smaller
than requiring every active trapped port to be linked.

There is also a one-flow sufficient certificate.  If

\[
 \deg_B(g)=h\quad(g\in G),\qquad
 \deg_B(p)\le h\quad(p\in P),                            \tag{0.4}
\]

put

\[
 d_p={\deg_B(p)\over h}.
\]

Then every gain is linkable whenever

\[
 \boxed{
 \sum_{p\in U}d_p\le r_\Gamma(U)
 \qquad(U\subseteq P).}                                  \tag{0.5}
\]

Condition (0.5) is exactly one capacitated suffix max-flow: multiply every
physical suffix capacity by \(h\), give port \(p\) supply
\(\deg_B(p)\), and ask to send all \(h|G|\) units to the typed sink bank.
It can hold when (0.1) fails.

Finally, the Middle Levels graph \(ML_m\) is \(m\)-vertex-connected.  Hence,
if the type-safe expanded residual suffix network contains a
capacity-faithful **bidirected** copy of \(ML_m-F\), all active ports and a
disjoint set of at least \(|G|\) legal sink vertices lie in that copy, every
directed corridor path is a legal typed suffix, and

\[
                         |G|+|F|\le m,                    \tag{0.6}
\]

then (0.5) holds.  Thus an \(O(d)\)-ticket bank with an \(O(d)\) deleted
private collar is routable through such a corridor for all sufficiently
large \(m\), since \(d=\Theta(\sqrt m)\).

The missing all-dimensional statement is therefore smaller than full-port
independence: it is enough to produce either the factor-restricted expansion
(0.2), the trapped-menu cuts (0.3a), the degree-weighted flow (0.5), or the
literal corridor in (0.6), in the same typed cap state as the prefixes and
the transported background.

## 1. Literal interface and scope

Work after deleting the capacities and sink slots of one fixed compensation
linkage.  Every incidence \(gp\in E\) has a directed occurrence-labelled
prefix

\[
                         Q_{gp}:s_g\leadsto p.             \tag{1.1}
\]

The prefix interiors are mutually private, except that prefixes from one
claim share their start and prefixes ending at one physical port share that
port.  Prefix interiors are disjoint from the residual suffix network.
Every physical port is represented by one capacity-one gate, even when
several incidences name it.

The residual suffix network has unit node capacities and a correctly typed
sink bank.  Linkable port sets form a strict gammoid \(\Gamma\) on \(P\).
All suffixes starting at a port are legal for every factor incidence using
that port; otherwise split into type-homogeneous blocks or retain the
identity-safe gadget in the suffix network.  All objects occur in one fixed
materialized state.  These are exactly the privacy, type, and state
requirements needed below.

The theorem concerns the displayed prefix-plus-suffix architecture.  Other
routes in a larger physical network may only improve the true optimum.

## 2. Exact factor-restricted Rado theorem

### Theorem 2.1

Within the architecture of Section 1, a set \(S\subseteq G\) has
simultaneous paths to distinct legal sinks if and only if, for every
\(X\subseteq S\),

\[
                         r_\Gamma(N_B(X))\ge |X|.          \tag{2.1}
\]

Consequently, (0.3) is the exact number of claims omitted by a maximum
factor-router linkage.

#### Proof

For each claim \(g\), its menu is the port set \(N_B(g)\).  A family of
claims is feasible exactly when it has distinct representatives
\(p_g\in N_B(g)\) whose representative set is independent in \(\Gamma\).
Indeed, link the representative ports to typed sinks in the suffix network
and prepend the private paths \(Q_{g p_g}\).  Conversely, a linkage using
the displayed architecture chooses one first port per claim, and those
ports are linked in the suffix network.

Rado's theorem now gives (2.1).  Its rank formula says that the maximum
number of represented claims is

\[
 \min_{X\subseteq S}
 \bigl(|S\setminus X|+r_\Gamma(N_B(X))\bigr).
\]

Taking \(S=G\) and subtracting from \(|G|\) gives (0.3). \(\square\)

### Theorem 2.2 (exact trapped-menu cut form)

The factor-router is exact if and only if

\[
                         |H_B(U)|\le r_\Gamma(U)
                         \qquad(U\subseteq P).            \tag{2.2}
\]

Let \(C\) be a vertex cut in the node-split suffix network, and let
\(U_C\) be the full set of ports separated from the typed sink bank by
\(C\), including a port when its own capacity gate belongs to \(C\).  Then
(2.2) is equivalent to

\[
 \boxed{|H_B(U_C)|\le\operatorname{cap}(C)
        \qquad\text{for every suffix cut }C.}             \tag{2.3}
\]

#### Proof

Assume Theorem 2.1.  Apply it to \(X=H_B(U)\).  Since
\(N_B(X)\subseteq U\),

\[
 |H_B(U)|\le r_\Gamma(N_B(H_B(U)))\le r_\Gamma(U).
\]

Conversely, for \(X\subseteq G\), take \(U=N_B(X)\).  Then
\(X\subseteq H_B(U)\), so (2.2) gives

\[
 |X|\le |H_B(U)|\le r_\Gamma(U)=r_\Gamma(N_B(X)).
\]

This proves the first equivalence.

If (2.2) holds, \(C\) separates \(U_C\), and Menger gives

\[
 |H_B(U_C)|\le r_\Gamma(U_C)\le\operatorname{cap}(C).
\]

Conversely, fix \(U\subseteq P\), choose a minimum \(U\)-to-sink
separator \(C\), and enlarge \(U\) to the full trapped set \(U_C\).  Then
\(U\subseteq U_C\), and (2.3) gives

\[
 |H_B(U)|\le |H_B(U_C)|
 \le\operatorname{cap}(C)=r_\Gamma(U).
\]

Thus (2.2) and (2.3) are equivalent. \(\square\)

### Corollary 2.3 (bounded factor-restricted defect)

If

\[
 r_\Gamma(N_B(X))\ge |X|-K
 \qquad(X\subseteq G),                                  \tag{2.4}
\]

then all but at most \(K\) claims are linked.  Thus for additive-constant
work it is unnecessary to link all active ports even up to bounded port
corank; only the factor-neighbourhood shores in (2.4) matter.

## 3. Fractional incidence-to-gammoid interface

The next form permits nonuniform use of the factor incidences.

### Theorem 3.1

All claims in \(G\) are linkable if and only if there are numbers
\(x_{gp}\ge0\), \(gp\in E\), such that

\[
 \sum_{p:gp\in E}x_{gp}=1\quad(g\in G),                  \tag{3.1}
\]

and, on putting

\[
 d_p=\sum_{g:gp\in E}x_{gp},                             \tag{3.2}
\]

one has

\[
 \boxed{
 d(U):=\sum_{p\in U}d_p\le r_\Gamma(U)
 \qquad(U\subseteq P).}                                  \tag{3.3}
\]

#### Proof

Necessity follows from an integral linkage: put \(x_{g p_g}=1\) on the
chosen claim-to-port incidences and zero elsewhere.  The chosen port set is
independent in \(\Gamma\), so its incidence vector obeys (3.3).

Conversely, (3.3) says exactly that \(d\) lies in the independence
polytope of the matroid \(\Gamma\).  Hence \(d\) is a convex combination of
incidence vectors of independent port sets.  Choose one suffix linkage for
each independent set in that combination and average the corresponding
unit flows.  This gives a fractional suffix flow whose injection at port
\(p\) is exactly \(d_p\) and whose load on every physical suffix capacity
and sink slot is at most one.

Send \(x_{gp}\) units down prefix \(Q_{gp}\).  Equation (3.1) gives one
unit out of each claim start, and (3.2) matches the incoming prefix flow at
each port to its suffix injection.  Prefix privacy and the capacity-faithful
suffix representation show that the concatenated flow is feasible and has
value \(|G|\).

The physical network has integral capacities.  Integral max flow therefore
gives a value-\(|G|\) integral flow, hence one disjoint legal path for every
claim. \(\square\)

This theorem is an exact polyhedral form of Theorem 2.1; it is not an
additional relaxation.  Its use is that a convenient explicit choice of
\(x\) can prove feasibility without linking every port.

## 4. The degree-weighted regular-factor certificate

Assume (0.4) and take

\[
                         x_{gp}={1\over h}.               \tag{4.1}
\]

Then (3.1) holds and (3.2) becomes

\[
                         d_p={\deg_B(p)\over h}\le1.      \tag{4.2}
\]

Also

\[
 d(P)={1\over h}\sum_{p\in P}\deg_B(p)
     ={1\over h}\sum_{g\in G}\deg_B(g)=|G|.             \tag{4.3}
\]

Theorem 3.1 proves (0.5).  There is also a direct trapped-menu proof.  Every
gain in \(H_B(U)\) sends all \(h\) of its factor incidences into \(U\), so

\[
 h|H_B(U)|
 \le\sum_{p\in U}\deg_B(p)
 =h d(U).                                                \tag{4.3a}
\]

Thus (0.5) implies \(|H_B(U)|\le r_\Gamma(U)\), and
Theorem 2.2 applies.

### One scaled max-flow certificate

Multiply every node and sink capacity of the suffix network by \(h\).
Add a super-source with an arc of capacity \(\deg_B(p)\) to every port
\(p\).  Then (0.5) is equivalent to a flow of value

\[
                         \sum_p\deg_B(p)=h|G|.            \tag{4.4}
\]

Indeed, after division by \(h\), such a flow is precisely a suffix flow
with port injection vector \(d\).  Conversely, multiply a fractional flow
for \(d\) by \(h\).  Equivalently, by max-flow/min-cut, every suffix cut
must have \(h\) times its physical capacity at least the total factor degree
of the ports trapped behind it.

This is strictly weaker than (0.1).  For example, let one claim have two
ports, both leading through one common unit sink gate.  The full port set
has gammoid rank one rather than two.  At \(h=2\), however, each port has
demand \(1/2\), so (0.5) holds and the one claim is linked.

### Corollary 4.1 (a port-fan condition)

Put \(q=|G|\).  If

\[
 r_\Gamma(U)\ge\min\{|U|,q\}
 \qquad(U\subseteq P),                                  \tag{4.5}
\]

then all claims are linked.

#### Proof

By (4.2), \(d(U)\le |U|\); by (4.3), \(d(U)\le q\).  Thus
\(d(U)\le\min\{|U|,q\}\le r_\Gamma(U)\), and (0.5)
applies. \(\square\)

The required fan order is the number of claims \(q\), not the number of
active ports \(|P|\), which may be as large as \(hq\).

## 5. Connectivity of the Middle Levels graph

Let \(ML_m\) be the containment graph between ranks \(m-1\) and \(m\) of
\([2m-1]\).  Both shores have size

\[
                         W={2m-1\choose m},
\]

and the graph is \(m\)-regular.

The middle-shadow theorem in
`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`
states that, for every nonempty family \(A\) in either shore,

\[
 |N(A)|-|A|\ge\min\{m-1,W-|A|\}.                         \tag{5.1}
\]

The two shores are equivalent by complementation.

### Theorem 5.1

For \(m\ge2\), the vertex connectivity of \(ML_m\) is exactly \(m\).

#### Proof

It is at most \(m\), because deleting the \(m\) neighbours of one vertex
isolates that vertex.

Suppose that a set \(S=S_L\mathbin{\dot\cup}S_U\), with
\(|S|\le m-1\), disconnects the graph.  Choose one component of
\(ML_m-S\), and let its two shores be \(A\) and \(C\).  Every remaining
vertex retains a neighbour, since its degree is \(m>|S|\); hence every
component meets both shores.  Because there is another component,

\[
 W-|A|\ge |S_L|+1,
 \qquad
 W-|C|\ge |S_U|+1.                                      \tag{5.2}
\]

No edge leaves the component except through \(S\), so (5.1) gives

\[
 |C|\ge |A|+\min\{m-1,W-|A|\}-|S_U|,                    \tag{5.3}
\]

and, symmetrically,

\[
 |A|\ge |C|+\min\{m-1,W-|C|\}-|S_L|.                    \tag{5.4}
\]

Adding (5.3)--(5.4) yields

\[
 |S_L|+|S_U|
 \ge
 \min\{m-1,W-|A|\}+
 \min\{m-1,W-|C|\}.                                    \tag{5.5}
\]

By (5.2), the right side is strictly larger than
\(|S_L|+|S_U|\): normally its two terms are at least
\(|S_L|+1\) and \(|S_U|+1\); if one of \(|S_L|,|S_U|\)
equals \(m-1\), its term is \(m-1\) and the other term is at least one.
This contradiction proves \(m\)-connectivity. \(\square\)

### Lemma 5.2 (set-to-set fan)

Let \(H\) be a bidirected copy of a \(q\)-vertex-connected undirected
graph.  If \(U\) and \(T\) are disjoint vertex sets with \(|T|\ge q\),
then

\[
 r_{L(H,T)}(U)\ge\min\{|U|,q\}.                         \tag{5.6}
\]

#### Proof

Put \(a=\min\{|U|,q\}\).  If fewer than \(a\) disjoint
\(U\)-to-\(T\) paths exist, set-Menger gives a separator of size less than
\(a\).  It deletes neither all of \(U\) nor all of \(T\), and its size is
less than \(q\), contradicting \(q\)-connectivity.  Bidirection makes each
undirected path a directed suffix path. \(\square\)

### Corollary 5.3 (literal Middle Levels corridor)

Delete a set \(F\) of \(f<m\) vertices from \(ML_m\).  The remainder is
\((m-f)\)-vertex-connected.  Suppose the type-safe expanded residual
suffix network contains a capacity-faithful bidirected copy of this
remainder, with the active physical ports \(P\) and a set \(T\) of at least
\(q=|G|\) distinct legal sink vertices in the copy, disjoint from \(P\).
Every directed path in the copy is required to be a legal typed suffix for
its starting port.  If \(q+f\le m\), then every claim in a
left-\(h\)-regular/right-at-most-\(h\) factor is linked.

#### Proof

The connectivity assertion follows because deleting fewer than \(m-f\)
additional vertices would delete fewer than \(m\) vertices from \(ML_m\).
Apply Lemma 5.2 with \(q=|G|\), then Corollary 4.1. \(\square\)

In particular, if \(q=O(d)\), \(f=O(d)\), and
\(d=\Theta(\sqrt m)\), the scalar inequality \(q+f\le m\) is automatic
for all sufficiently large \(m\).  The non-scalar obligation is the literal
embedding: the ports, typed sinks, compensation deletion, occurrence state,
and every physical capacity must all be those of one actual bidirected
suffix corridor.

## 6. Exact obstruction and current scope

The quantity in (0.3), not the corank of the whole port set, is the exact
router obstruction contributed by the factor.  In particular:

* full-port independence (0.1) implies \(\delta_B=0\), but is not
  necessary;
* individual nonloop ports do not bound \(\delta_B\);
* a common unit suffix bottleneck gives
  \(\delta_B=|G|-1\), even with an exact abstract factor and an unrelated
  exact parent matching; and
* for additive-constant work the sharp sufficient target is
  \(\delta_B=O(1)\), or its two-coordinate/common-cap analogue in the
  frozen Rado theorem.

The degree-weighted certificate (0.5) is a convenient one-flow sufficient
condition for \(\delta_B=0\).  It is not necessary: a nonuniform incidence
weighting from Theorem 3.1 may succeed when the uniform weighting fails.

The current small protected-factor theorem supplies the abstract factor
\(B\), but it does not identify its right vertices with physical supplier
ports.  Nor does it embed a bidirected copy of \(ML_m-F\) in the typed
suffix network.  Consequently Corollary 5.3 is a new conditional bridge,
not an assertion that the present all-dimensional parent already satisfies
the router gate.

For the two occurrence coordinates of the common-cap theorem, Sections
2--5 must be instantiated in the same complete cap state, with all
cross-coordinate shared capacities allocated and global product closure
proved.  A separate corridor or flow in each coordinate is insufficient if
the two choices still compete for one physical resource.
