# Regenerating bilateral banks via integral rotor fusion

**Date:** 2026-08-03

**Status:** unconditional fixed-child fusion, holonomy and quantitative
contraction theorems.  The all-dimensional existence lemma isolated in
Section 6 is unproved.  No finite K17 computation is used as an
all-dimensional premise.

## 0. Outcome

A crossed bilateral bank need not decompose into bounded helper orbits.
One large orbit is harmless if it can be lifted to a single protected
Eulerian rotor and its losses are priced directly.  This note proves the
exact implication.

The fixed-child theorem has four logically separate rows.

1. **Coboundary lift.**  The phase-helper incidences lift to literal trace
   packets whose state boundary and every localized additive protected
   signature are endpoint coboundaries.
2. **Integral fusion.**  Zero-boundary connector packets make the selected
   support weakly connected.  Permutation cancellation gives state balance,
   so the result has one Euler circuit and zero route sidecar.
3. **Full-state holonomy.**  Along some rooted block-Euler order, the
   complete continuation relation on address, history, reset, residence and
   exported parent state meets an allowed successor-parent conjugacy.
4. **Joint capacity.**  The same witness jointly realizes the complete
   occurrence/common-cap/supplier footprint, every physical reset adapter,
   and the continuation-state chain.  Private compensation and gain
   corridors in that same packing then give exact claim rank \(p=q+g\).

The first two rows imply zero named lower current and exact upper
transparency when those data are included in the additive signature.  They
do not imply rows 3 or 4.  Full-state holonomy and joint capacity are the
minimal missing interface: both have sharp constant-size counterexamples.

With uniform exposure

\[
                         g\ge\alpha\Phi-B_0            \tag{0.1}
\]

and bounded complete physical casualties, the rotor gives an explicit
contraction.  More generally suppose its joint claim rank satisfies

\[
 p\ge q-\beta+\eta g-\gamma,
 \quad c_{\rm phys}\le\chi g+C_P,
 \quad 0\le\chi<\eta\le1.                            \tag{0.2}
\]

Then

\[
 \boxed{
 \Phi'\le[1-\alpha(\eta-\chi)]\Phi
       +(\eta-\chi)B_0+\beta+\gamma+C_P.
 }                                                       \tag{0.3}
\]

Mutually vertex-disjoint private full corridors give
\(\eta=1,\beta=\gamma=0\).  They do not by themselves prove
\(\chi=0\).

Left-total regeneration on a dimension-covering invariant system with a
bounded exported carrier and bounded terminal Hall defect then implies
\(B(k)+O(1)\), with the constant displayed in Theorem 5.1.

## 1. Fixed-child completed rotor data

Work in one fully materialized and fully replayed child.  Fix an exact
baseline partition of the required owner/payload table into role-labelled
occurrences.  Let \(V\) be a finite set of selected source roles.  In the
split architecture, the phase helper maps are permutations

\[
                         \sigma_0,\sigma_1:V\to V.     \tag{1.1}
\]

The theorem itself only uses that they are permutations; derangement and
pointwise-disagreement conditions belong to the bilateral source
construction.

Let \({\cal S}\) be the literal trace-state set and let
\(\mathbb Z^{\cal S}\) be the free abelian state-boundary group.  For every
\(x\in V\) and phase \(\phi\), fix one **atomic macro record**
\(P_{x,\phi}\), including its complete occurrence label, role, owner, named
targets, upper witnesses and protected resources.  An atomic macro record
has one declared tail and head.  Its literal expansion is a directed Euler
trail between them, and its interior is private from every other record
except at declared interfaces.  Thus every Euler tour of the macro records
expands packet-contiguously and keeps every literal occurrence.

Let

\[
                 a_\phi:V\to{\cal S}                  \tag{1.2}
\]

be its state-potential map.

Each packet is a finite weakly connected directed multigraph with the
displayed one-unit boundary below.  Hence it has a directed Euler trail from
its tail interface to its head interface and may be contracted to one
labelled macro arc without losing any internal occurrence.

Let \(G\) be a free abelian group on every **localized signed
final-minus-initial incidence** which must be preserved exactly.  It may
include named lower-target current, role-indexed upper-witness occurrences
and owner/payload incidences relative to the fixed baseline.  Distinct
literal resources have distinct generators, so zero signature is exact
multiset equality, not cancellation of unrelated damage.  Ordinary
damage-set membership, context-dependent history, or an unlocalized
interval witness is not silently placed in \(G\); it belongs to the joint
physical witness or the full continuation relation of Section 4.

### Definition 1.1 (completed coboundary lift)

The horizontal packet bank is a completed coboundary lift when there is a
potential \(u_\phi:V\to G\) such that

\[
\begin{aligned}
 \partial P_{x,\phi}
   &={\bf1}_{a_\phi(\sigma_\phi x)}
      -{\bf1}_{a_\phi(x)},\\
 \lambda(P_{x,\phi})
   &=u_\phi(\sigma_\phi x)-u_\phi(x)                 \tag{1.3}
\end{aligned}
\]

for every \(x,\phi\), where \(\lambda\) is the complete localized additive
signature.

Let \(C\) be a fixed protected connector/root bank, decomposed into atomic
macro records of the same kind.  Require in aggregate

\[
                         \partial C=0,
                         \qquad\lambda(C)=0.           \tag{1.4}
\]

The connectors may be extensive when they are embedded equal-length packet
data.  What is bounded later is their total **live uncontracted physical
charge**, not their description count.  Every physical reset/pivot adapter
is a labelled member of \(C\); it cannot be hidden in an abstract terminal
conjugacy.

Put

\[
                  F=C\cup\{P_{x,\phi}:x\in V,
                                            \phi=0,1\}. \tag{1.5}
\]

All packet occurrences in (1.5) are literal and distinct even when two
arcs have the same endpoints.  The **macro support** of \(F\) is the
directed multigraph on the trace states incident with at least one selected
record, with one labelled arc for each atomic record.  All connectivity and
Euler statements below refer to this positive-degree macro support.

## 2. Permutation cancellation and integral Euler fusion

### Theorem 2.1 (completed bilateral rotor fusion)

For every completed coboundary lift,

\[
                         \boxed{\partial F=0,
                                \qquad\lambda(F)=0.}   \tag{2.1}
\]

If the macro support of \(F\) is weakly connected, then it has one labelled
Euler circuit.  The circuit uses every selected macro record exactly once
and expands packet-contiguously to every literal occurrence.  Relative to
the fixed exact baseline it preserves every role-indexed owner/payload
incidence and returns every localized lower and upper incidence exactly.
It needs no route list beyond the connector records already in \(F\).

#### Proof

For either phase, permutation invariance gives

\[
 \sum_{x\in V}{\bf1}_{a_\phi(\sigma_\phi x)}
 =\sum_{x\in V}{\bf1}_{a_\phi(x)},
 \qquad
 \sum_{x\in V}u_\phi(\sigma_\phi x)
 =\sum_{x\in V}u_\phi(x).                            \tag{2.2}
\]

Summing (1.3) over \(x,\phi\), then adding (1.4), proves (2.1).  Thus every
state has equal indegree and outdegree in the macro support.  A weakly
connected balanced finite directed multigraph has an Euler circuit.  Private
packet interiors let us expand every macro arc contiguously.  Every packet
keeps its occurrence label and fixed protected payload, while
\(\lambda(F)=0\) proves exact return of the role-indexed localized rows.
No connector edge outside \(F\) is appended. \(\square\)

Connectivity can be checked before serialization.  Take the weak components
of the horizontal macro support and the weak components of the connector
macro support.  Form their bipartite intersection graph, with an edge
exactly when two components share a declared interface state.  Include
every nonempty component, including connector-only isolated components.
The macro support in (1.5) is weakly connected if and only if this full
intersection graph is connected.  This is the
exact analogue of protected pool fusion; a bound on the number of
horizontal components alone is not a bounded-charge theorem.

### Corollary 2.2 (helper-orbit specialization)

Suppose the connector macro support contains, for every \(x\), a connected
component meeting both states \(a_0(x)\) and \(a_1(x)\), and every connector
component meets the horizontal support.  Then every orbit of

\(\langle\sigma_0,\sigma_1\rangle\) lies in one weak component of \(F\).
In particular, a transitive helper orbit gives one zero-route-list rotor
even when its cardinality is unbounded.  If, additionally, every horizontal
interior and every connector-support component is private to one group
orbit, and the only cross-phase contacts are the declared vertical
interfaces, the weak components are precisely those group orbits.

#### Proof

Horizontal edges generate the two permutation relations and each vertical
connector joins the two phase copies of one mode.  Thus group-orbit
reachability implies macro reachability.  Under the additional
orbit-privacy/no-cross-contact hypothesis there are no other macro
identifications, giving the converse. \(\square\)

Thus bounded helper-orbit size is sufficient for bounded local modules but
is not necessary for contraction.  A large transitive orbit can carry an
extensive bank in one Euler component, provided the remaining hypotheses of
this note are verified directly.

## 3. Twisted coboundaries and exact lower holonomy

Literal profiles need not be identical packet by packet.  Let an oriented
packet orbit have seam potentials

\[
                         U_0,U_1,\ldots,U_\ell         \tag{3.1}
\]

in one common named-resource group after the declared seam transports are
applied.  Suppose packet \(i\) has signed current

\[
                              \Delta_i=U_{i+1}-U_i.    \tag{3.2}
\]

If the closing seam has holonomy \(H_{\cal O}\), so that
\(U_\ell=H_{\cal O}U_0\), then

### Theorem 3.1 (twisted-coboundary orbit identity)

\[
                 \boxed{
                 \sum_{i=0}^{\ell-1}\Delta_i
                    =(H_{\cal O}-I)U_0.}              \tag{3.3}
\]

Hence the orbit has zero named current exactly when its literal seam
holonomy fixes the initial potential.

#### Proof

Equation (3.2) telescopes to \(U_\ell-U_0\); substitute the closing seam
identity. \(\square\)

The aligned birail theorem is the special case \(H_{\cal O}=I\).  Equation
(3.3) also permits conjugate profiles, but only when the seam transports are
literal identifications in one named-target group.  Equal cardinalities or
separately relabelled profiles are insufficient.

## 4. Complete continuation holonomy and joint capacity

Euler balance is not regeneration.  Let \(\Omega\) be the complete literal
continuation-boundary state needed by the next transition.  It includes
every exported address, flag, positive/negative history, reset, residence,
frame/coset and parent-authentication datum.  A quotient may replace the
literal boundary only after proving it is a compositional congruence with
the required fibre-product lifting property; equality of quotient labels
alone cannot splice incompatible representatives.  A purely terminal
compiler choice need not be exported, but every compiler or common-cap
state used to authenticate the successor must be included.

Let \(\mathfrak P(F)\) be the set of simultaneous capacity-faithful global
physical assignments for all atomic records in \(F\), including occurrence,
common-cap, supplier, seam, connector and reset resources.  For each record
\(P\), let

\[
 \widehat R_P\subseteq
 \Omega\times\Omega\times
 \{\Pi|_P:\Pi\in\mathfrak P(F)\}                     \tag{4.1}
\]

be the complete compatibility relation between its boundary states and the
restriction of the same physical assignment.  Let
\({\cal E}_{\rm blk}(F)\) be the set of **rooted block-Euler circuits** of
the labelled macro support.  Rooting records the first packet and the
initial boundary state.  For

\[
 W=(P_1,\ldots,P_m)\in{\cal E}_{\rm blk}(F)           \tag{4.2}
\]

a compatible chain is

\[
 (\omega_{i-1},\omega_i,\Pi|_{P_i})\in\widehat R_{P_i}
 \quad(1\le i\le m).                                  \tag{4.3}
\]

Let \(K\subseteq\Omega\times\Omega\) be the cost-free authenticated
successor-parent conjugacy.  Every pair in \(K\) must be sort-preserving,
actual-address injective, capacity-faithful and exterior-fixed wherever the
construction declares a protected exterior.  Literal cyclic reset uses the
diagonal.  Any physical pivot/reset adapter is already an atomic record in
\(C\), so its resources and state action occur in (4.1)--(4.3), rather than
being hidden in \(K\).  A purely terminal compiler deficit, unused for
successor authentication, may be measured separately by
\(\delta_{\rm term}(F)\).

### Theorem 4.1 (exact joint regenerated-rotor criterion)

The rotor has a literal packet-contiguous serialized successor accepted by
\(K\) if and only if

\[
 \boxed{
 \begin{gathered}
 \exists\,\Pi\in\mathfrak P(F),\
 W=(P_1,\ldots,P_m)\in{\cal E}_{\rm blk}(F),\
 \omega_0,\ldots,\omega_m\in\Omega:\\
 (\omega_{i-1},\omega_i,\Pi|_{P_i})\in\widehat R_{P_i}
 \quad(1\le i\le m),\qquad
 (\omega_0,\omega_m)\in K .
 \end{gathered}}                                      \tag{4.4}
\]

#### Proof

A witness in (4.4) gives one capacity-faithful physical assignment, a
rooted integral block-Euler order, and a compatible state at every seam.
Private macro interiors expand this to a literal packet-contiguous
serialization, and the last pair authenticates its successor.  Conversely,
read these three objects from any such literal serialization. \(\square\)

There is a useful factorized corollary, but it needs an extra hypothesis.
Suppose the packet lift is **rectangular**: every global packing
\(\Pi\in\mathfrak P(F)\) is compatible with every boundary pair in a
projected relation \(R_P\subseteq\Omega^2\), independently for every packet
and seam.  Then (4.4) is equivalent to

\[
 \mathfrak P(F)\ne\varnothing
 \quad\text{and}\quad
 \exists W\in{\cal E}_{\rm blk}(F):
 (R_{P_m}\circ\cdots\circ R_{P_1})\cap K\ne\varnothing. \tag{4.5}
\]

Without rectangular lifting, the two existentials in (4.5) can use
incompatible witnesses and (4.5) is not sufficient.  Even under
rectangular lifting, its two clauses are independent.

* Nonempty packet relations need not compose.  On two continuation states,
  take three nonempty relations
  \(R_1=\{(0,1)\}, R_2=\{(0,1)\}, R_3=\{(1,0)\}\).
  Their named currents may be assigned to a telescoping three-cycle, but
  \(R_2\circ R_1=\varnothing\).
* Two packet tasks can each have the singleton compiler neighbourhood
  \(\{c\}\).  Each is individually feasible, while their union has Hall
  deficiency one at the capacity-one cell \(c\).

An address permutation gives a third obstruction: zero named current may
return the projected state while the complete holonomy is a nontrivial
address permutation.  It is legal only if that permutation belongs to the
authenticated conjugacy \(K\).

Thus named lower current is merely a projection of the full continuation
state.  No scalar or additive-coboundary theorem can replace the joint
criterion (4.4).

## 5. Quantitative Regenerating Bilateral Bank theorem

Let \(\Phi\ge0\) be the complete carried defect potential of a reachable
parent state.  Fix uniform constants

\[
 0<\alpha\le1,\quad 0\le\chi<\eta\le1,\quad
 \beta,\gamma,B_0,C_P,C_R,C_S,C_T,A\ge0.              \tag{5.1}
\]

Assume every state in one reachable invariant class has a single common
child satisfying all of the following.

1. It contains a selected bilateral rotor bank obeying Theorems 2.1 and 4.1
   with \(g\) genuine gain claims and

   \[
                              g\ge\alpha\Phi-B_0.      \tag{5.2}
   \]

   Every required upper witness is either fixed in its role payload,
   occurrence-localized in \(\lambda\), or carried in the complete
   continuation relation.  Thus the selected Euler order has no unpriced
   upper-witness loss.

2. Fix a parent maximum matching \(M\) of rank \(r\).  In one extension of
   the same global physical assignment \(\Pi\) that witnesses (4.4) to the
   claim network, retain a matching \(M_0\subseteq M\) of size \(r-q\).
   There are \(p\) jointly vertex-disjoint \(M_0\)-augmenting paths,
   disjoint from the rotor records outside their declared ports, and

   \[
                       p\ge q-\beta+\eta g-\gamma.     \tag{5.3}
   \]

   A capacity-faithful private full corridor for every compensation and gain
   claim gives the sharp specialization
   \(p=q+g\), hence \(\eta=1,\beta=\gamma=0\).

3. Complete casualty accounting, after the telescoped lower current and
   transparent upper bank are removed, gives

   \[
                     c_{\rm phys}\le\chi g+C_P.       \tag{5.4}
   \]

   Here \(c_{\rm phys}\) includes every supplier or non-supplier loss caused
   by packet, connector, reset and compiler-incidence changes which is not
   already priced by \(q-p\).  The output exceptional sidecar has size at
   most \(C_P\); it replaces the input sidecar and is not appended to it.
4. The authenticated conjugacy in (4.4) returns the child to the next member
   of the same invariant system.  The exported exceptional continuation
   carrier has physical support at most \(C_S\), and all live uncontracted
   connector/reset records have total charge at most \(C_R\).  These
   carriers and records are recycled or replaced at the next transition,
   never accumulated.  The structural bulk parent may be large, but it is
   not charged as a hidden sidecar.
5. The complete potential row is

   \[
                          \Phi'\le\Phi+q-p+c_{\rm phys}. \tag{5.5}
   \]

6. Every declared terminal map from the regenerated class has a
   physicalization satisfying

   \[
             \nu(k)\le B(k)+A\Phi+C_R+C_S+C_T,        \tag{5.6}
   \]

   where \(C_T\) includes the complete terminal Hall/compiler defect and is
   paid once.  A terminal-only compiler matching may change from one
   dimension to the next.

   One proof-safe sufficient certificate for \(C_T\) is the zero-block
   theorem: the two literal simple-positive ray cross graphs have perfect
   matchings in physical cells disjoint from an admissible full-block lift
   of the background matching.  Then the ray defect is zero, and a
   background deletion bound \(C\) plus upper defect \(u\) permits
   \(C_T=C+u\).  Host embedding, cell disjointness and cross-graph Hall are
   hypotheses of this certificate, not consequences of telescoping.

### Theorem 5.1 (explicit regenerated contraction)

Under hypotheses 1--6, put

\[
 s=\eta-\chi,\qquad
 \lambda=\alpha s,\qquad
 \kappa=sB_0+\beta+\gamma+C_P.                       \tag{5.7}
\]

Every transition satisfies

\[
                    \boxed{\Phi'\le(1-\lambda)\Phi+\kappa.} \tag{5.8}
\]

After \(N\) regenerated transitions,

\[
 \boxed{\displaystyle
 \Phi_N\le(1-\lambda)^N\Phi_0+
          {\kappa\{1-(1-\lambda)^N\}\over\lambda}
       \le(1-\lambda)^N\Phi_0+{\kappa\over\lambda}.}  \tag{5.9}
\]

If, for every sufficiently large requested \(k\), the invariant system
supplies a compatible spine and terminal map with \(N=N(k)\) transitions
and

\[
                         (1-\lambda)^N\Phi_0\le1,      \tag{5.10}
\]

then

\[
 \boxed{
 \nu(k)\le B(k)
   +A\left(1+
     {(\eta-\chi)B_0+\beta+\gamma+C_P
      \over\alpha(\eta-\chi)}\right)
   +C_R+C_S+C_T.
 }                                                       \tag{5.11}
\]

In particular, these uniform hypotheses imply \(B(k)+O(1)\) for every
dimension covered by the spine/terminal system.  A concrete sufficient
coverage scheme is a left-total odd spine
\({\cal G}_m\to{\cal G}_{m+1}\) with
\(k({\cal G}_{m+1})=k({\cal G}_m)+2\), together with a valid adjacent-even
terminal map at every \(m\).  In the ideal private one-step case
\(\alpha=\eta=1,\chi=\beta=\gamma=0\),

\[
                 \Phi'\le B_0+C_P,                   \tag{5.12}
\]

and the harmless `1` in (5.11) may be omitted.

#### Proof

Simultaneous augmentation along the \(p\) jointly vertex-disjoint paths
gives child rank at least \(r-q+p\), and the complete potential row (5.5)
then applies.  Substitute (5.3) and (5.4) into (5.5):

\[
 \Phi'\le\Phi-(\eta-\chi)g+\beta+\gamma+C_P.
\]

Now use (5.2) to obtain (5.8).  Iteration of the affine recurrence gives
(5.9).  Equations (5.6), (5.9) and (5.10) give (5.11). \(\square\)

Left-totality of the invariant class, or one explicitly constructed
infinite compatible spine, is load-bearing.  A separate transition at every
dimension need not compose, and a spine which misses dimensions does not
give an all-\(k\) theorem.  For \(0<\lambda<1\), (5.10) follows from

\[
 N(k)\ge {\log\max\{1,\Phi_0(k)\}\over-\log(1-\lambda)};
\]

when \(\lambda=1\), one transition suffices.  Likewise, a fresh \(O(1)\)
sidecar or reset apparatus appended at each step would accumulate and does
not satisfy hypotheses 3--4.

The strict inequality \(\eta>\chi\) is the asymptotic sign condition.
For one finite child the displayed upper bound strictly decreases precisely
when

\[
             (\eta-\chi)g>\beta+\gamma+C_P.           \tag{5.13}
\]

Private corridors establish \(\eta=1,\beta=\gamma=0\), but complete
casualty pricing is still needed to show \(\chi<1\).

### Theorem 5.2 (regular incidence factor plus private port router)

Let \({\cal N}\) be one directed vertex-capacitated, capacity-faithful
state-expanded claim network with unit physical capacities.  Thus every
directed claim-to-sink path decodes to a legal literal claim corridor; any
occurrence identity which cannot switch at a shared vertex is retained in
the state expansion.  Let

\[
                         B=(G,P;E)                    \tag{5.14}
\]

be a bipartite incidence graph such that every gain \(g\in G\) has degree
exactly \(h\ge1\) and every port \(p\in P\) has degree at most \(h\).
For each \(gp\in E\), let \(Q_{gp}\) be a literal directed claim-to-port
prefix.  For each \(p\), let \(S_p\) be a directed suffix from \(p\) to its
own unused sink \(t_p\), with all \(t_p\) distinct.  Put
\(L_{gp}=Q_{gp}S_p\).  Require the exact cross-bank condition

\[
 V(Q_{gp})\cap V(S_q)=
 \begin{cases}\{p\},&q=p,\\ \varnothing,&q\ne p,\end{cases} \tag{5.14a}
\]

so every \(L_{gp}\) is a directed simple path and no suffix traverses
another gain, prefix vertex or port.  If

\[
 {1\over h}\bigl|\{gp\in E:v\in L_{gp}\}\bigr|\le1
 \qquad\text{for every physical vertex }v,            \tag{5.15}
\]

then \({\cal N}\) contains \(|G|\) pairwise vertex-disjoint paths linking
every gain to distinct unused sinks.

#### Proof

Node-split every physical vertex with a unit-capacity arc, add a unit arc
from a supersource to each gain, and add a unit arc from every \(t_p\) to a
supersink.  Send \(1/h\) along every concatenation \(L_{gp}\).  Each gain
emits \(h/h=1\), while (5.15) makes this a feasible flow of value \(|G|\).
Integral max flow has the same value.  Since the total capacity leaving the
supersource is \(|G|\), every gain arc is saturated; after deleting flow
cycles, path decomposition gives the asserted linkage. \(\square\)

A clean sufficient form of (5.15) is **strong privacy**: in addition to
(5.14a), prefixes of different gains have disjoint interiors; a prefix
visits no other gain, port or sink; and the suffixes are pairwise
vertex-disjoint.  Shared copies of the same gain source and the declared
terminal port are then the only permitted contacts.  Under strong privacy
there is also a direct Hall proof:

\[
 h|X|=e_B(X,N_B(X))\le h|N_B(X)|                    \tag{5.16}
\]

for every \(X\subseteq G\), so \(B\) has a matching saturating \(G\);
concatenate the matched prefixes and suffixes.

There is also a quantitative congestion version after a fixed compensation
linkage has been removed.  Assume the prefix clauses of strong privacy,
require each prefix to meet the suffix bank only at its own terminal port,
but allow suffixes to overlap, and put

\[
 \rho=\max_v\sum_{p:v\in S_p}\deg_B(p),\qquad
 \eta_{\rm rt}={h\over\max\{h,\rho\}}.               \tag{5.16a}
\]

Weight every \(L_{gp}\) by \(1/\max\{h,\rho\}\).  The resulting feasible
flow has value \(\eta_{\rm rt}|G|\), so integral max flow links at least
\(\lceil\eta_{\rm rt}|G|\rceil\) gains.  If the already-fixed compensation
linkage consists of \(q\) mutually disjoint \(M_0\)-augmenting paths and
this residual router is disjoint from it, then (5.3) holds with
\(\eta=\eta_{\rm rt}\) and \(\beta=\gamma=0\).  Pairwise disjoint suffixes
give \(\rho\le h\) and hence \(\eta_{\rm rt}=1\).  To iterate Theorem 5.1,
\(\eta_{\rm rt}\) must have a uniform positive lower bound strictly larger
than \(\chi\); child-dependent positivity alone is insufficient.

The exact weaker router condition is a Rado inequality.  Let \(\Gamma\) be
the strict gammoid on \(P\) defined by linkability through the fixed
claim-free residual network to its unused sink bank.  Assuming the
**uniform prefix-transparency** condition that, for every
\(\Gamma\)-independent one-port-per-gain transversal, the selected
occurrence-labelled prefixes and some witnessing \(\Gamma\)-suffix linkage
are jointly vertex-disjoint (strong privacy suffices), there is one port
choice per gain and a simultaneous full claim-to-sink linkage if and only if

\[
             \boxed{r_\Gamma(N_B(X))\ge |X|
                    \quad\text{for every }X\subseteq G.} \tag{5.17}
\]

This is precisely Rado's transversal theorem.  Pairwise disjoint suffixes
for all ports imply (5.17), but are stronger than necessary and may be
impossible when the residual sink bank is smaller than the full factor
shore.  Rado selects only the router-good port subset needed by the gains.

For \(h=2\), the proved small protected-factor theorem in \(ML_m\) supplies
the **abstract incidence row**: every set-valued protected subgraph
\(H_0\subseteq ML_m\) with

\[
                 \Delta(H_0)\le2,\qquad |E(H_0)|\le m-2 \tag{5.18}
\]

lies in some spanning two-factor.  Restricting that factor to selected
gain-side vertices gives a left-2-regular, right-degree-at-most-2 graph
\(B\).  This statement becomes literal only after an injective
occurrence-labelled realization of its factor incidences and private
prefixes in the same child.

Neither the protected-factor theorem nor a parent/reference perfect
matching proves (5.17).  The factor theorem chooses some two-factor and
need not retain a pre-existing matching as one colour class.  Even if such
a colour class is co-instantiated, it sends a port to a matched
parent/root, not to an unused supplier sink, and gives no residual
reachability or separator bound.  Indeed, orienting the two perfect colour
classes of an internal two-factor alternately produces directed cycles,
with every vertex matched and no unused terminal.  A six-cycle incidence
factor whose every
port-to-sink route crosses one unit vertex has ordinary Hall expansion but
\(\Gamma\)-rank one.  Thus the all-\(k\) private port router, or equivalently
the Rado cuts (5.17) in the same regenerated child after the compensation
linkage is fixed, remains an explicit premise.

## 6. Exact missing all-dimensional lemma

The preceding theorems reduce the general route to the following concrete
existence statement.

> **Completed Regenerating Bilateral Bank Lemma (UNPROVED).**  There are
> uniform constants as in (5.1), dimension-indexed reachable parent classes
> \({\cal G}_m\), and left-total transitions between them such that every
> state of potential \(\Phi\) has one common fully replayed child with:
>
> 1. an atomic extensive bilateral bank with
>    \(g\ge\alpha\Phi-B_0\), exact role/owner/payload baseline, private macro
>    interiors and the completed coboundary lift (1.3);
> 2. an atomic zero-boundary connector/root/reset bank whose full
>    horizontal--connector component-intersection graph is connected;
> 3. one **joint** witness \((\Pi,W,\omega_0,\ldots,\omega_m)\) satisfying
>    (4.4), where the successor conjugacy is sort-preserving,
>    actual-address injective and exterior-fixed;
> 4. after fixing that same child and one compensation linkage, either
>    private full compensation/gain corridors or the exact port-gammoid Rado
>    cuts (5.17), giving (5.3) in the same physical assignment;
> 5. exact lower telescoping, occurrence-local upper transparency, the
>    complete potential row (5.5), and the bounded complete physical
>    casualty row (5.4);
> 6. a replacement, rather than accumulation, theorem for an exported
>    continuation carrier of support at most \(C_S\), live connector/reset
>    charge at most \(C_R\), and exceptional sidecar at most \(C_P\);
> 7. a terminal map at every odd-spine state and its adjacent even
>    dimension satisfying the complete physicalization inequality (5.6),
>    including bounded terminal Hall/compiler defect \(C_T\) and the
>    one-time \(C_R+C_S\) charges; and
> 8. for every sufficiently large requested \(k\), a compatible horizon
>    \(N(k)\) satisfying (5.10).

The completed package is sufficient for \(B(k)+O(1)\) by Theorem 5.1, with
the explicit constant (5.11).  It is not presently proved.

The **first single missing row**, before supplier expansion and terminal
transfer, is narrower:

> **Atomic full-state Euler-return factor lemma (UNPROVED).**  Every
> authenticated parent of potential \(\Phi\) has one fully replayed child
> containing an atomic helper-closed factor on at least
> \(\alpha\Phi-O(1)\) gain roles whose macro support is connected and
> coboundary-balanced, and for which the same capacity-faithful physical
> assignment realizes a rooted block-Euler continuation chain returning
> through a bounded-carrier, exterior-fixed successor conjugacy.

Even this first row does not imply the supplier linkage.  The new
regular-factor theorem proves that a private router would close it, while
the \(ML_m\) protected-factor theorem supplies only the abstract
left-2-regular incidence graph.  The additional all-\(k\) statement is
exactly (5.17) in the residual supplier gammoid after the compensation
linkage is fixed.

The interface is irreducible in two directions.  Omitting full-state
holonomy permits empty history composition or unauthenticated address
permutation; omitting joint capacity permits a shared-cell Hall obstruction.
Therefore zero named lower current, phasewise occurrence, separate phase
Hall, a protected two-factor, or bounded helper depth cannot prove the
missing lemma by themselves.

## 7. Proof inputs and scope

The Euler, twisted-holonomy, joint-witness, contraction and
regular-factor/router theorems in this note are proved here.  The two
imported pure results used only for the stated sufficient applications are:

* `MATH_THEOREM_ZERO_BLOCK_BIRAIL_COLLAPSE_AND_C8_CROSSMATCH_GATE_20260801.md`
  for the simple-positive zero-block terminal certificate; and
* `MATH_THEOREM_RESET_OPEN_PATH_PHASE_COMMON_Q1_HOST_20260801.md`,
  Section 2, for the \(ML_m\) small protected-factor theorem.

The fractional pull clock can at most help certify an exposure row such as
(5.2).  It does not imply the atomic integral factor, the joint witness
(4.4), or the supplier-gammoid cuts (5.17).  No finite-dimensional oracle
fact is used as an all-\(k\) premise in this note.
