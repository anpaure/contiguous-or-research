# Boolean-incidence pseudoflows and localized-overload suffix routing

**Date:** 2026-08-03  
**Status:** unconditional fixed-network theorem and sharp symbolic obstruction.
No finite search is used.  The theorem gives a strictly weaker sufficient
certificate than a pairwise-disjoint full-port suffix bank.  It does not
prove that the current parent/child occurrence interface supplies the
certificate.

## 0. Result

Fix one materialized cap, guard, occurrence, and terminal-type state, and
delete one fixed compensation linkage.  Let \(D\) be the resulting directed
node-split suffix network, let \(P\) be \(N\) active physical ports, and let
\(T\) be \(N\) unused interchangeable typed sinks.  Unit arcs from a
supersource to \(P\) and from \(T\) to a supersink are included.  Every
finite capacity is a positive integer; zero-capacity arcs are deleted.
Equivalently, an integral capacity may be expanded into parallel private
unit lanes.  Thus the maximum integral flow value is the rank of the
resulting strict gammoid on \(P\).

Suppose that a weighted catalogue of literal \(P\)-to-\(T\) paths sends one
unit from every port and one unit into every sink.  It need not respect the
internal unit capacities.  Let \(f(a)\) be its load on a finite-capacity arc
\(a\), whose capacity is \(c(a)\), and put

\[
 \Omega_{\rm cut}(f)=
 \max_W\sum_{a\in\delta^+(W)}(f(a)-c(a))_+,
 \qquad
 \Omega_{\rm tot}(f)=\sum_a(f(a)-c(a))_+ .           \tag{0.1}
\]

The maximum ranges over source sides of finite source--sink cuts.  Then

\[
 \boxed{
 N-r_\Gamma(P)
 \le \lfloor\Omega_{\rm cut}(f)\rfloor
 \le \lfloor\Omega_{\rm tot}(f)\rfloor ,}
                                                                    \tag{0.2}
\]

where \(\Gamma=L(D,T)|P\) is the typed suffix gammoid after the preceding
capacity expansion (equivalently, \(r_\Gamma(P)\) is the maximum integral
flow value in \(D\)).  Thus localized
fractional capacity excess, rather than worst congestion, controls the
*additive* router defect.

There is first a general balanced-factor version.  Let
\(H=(P,T;F)\) be \(h\)-regular on both equal shores and let every
\(e\in F\) have one literal \(P\)-to-\(T\) path.  Give every edge-path
weight \(1/h\), and let \(\ell(a)\) count the edge-paths using capacity
\(a\).  Then

\[
 \boxed{
 N-r_\Gamma(P)
 \le
 \left\lfloor {1\over h}
 \sum_a(\ell(a)-h c(a))_+\right\rfloor .}            \tag{0.3}
\]

Thus it is enough to construct a capacity-faithful *balanced semantic
port--sink factor* with localized physical overload; one does not need a
preselected disjoint suffix for every port.

The canonical Boolean version puts

\[
 {\cal L}={ [2m-1]\choose m-1},\qquad
 {\cal R}={ [2m-1]\choose m},\qquad |{\cal L}|=|{\cal R}|=W,
                                                                    \tag{0.4}
\]

and take \(s\) occurrence sheets.  For every containment \(A\subset B\)
and sheet \(\xi\), suppose there is one literal typed path

\[
 R_{A,B,\xi}:p_{A,\xi}\leadsto
 t_{B,\sigma_{A,B}(\xi)},                              \tag{0.5}
\]

where every \(\sigma_{A,B}\) is a permutation of the \(s\) sheets.  Give
every path weight \(1/m\).  If \(\ell(a)\) is the number of catalogue paths
using a finite-capacity arc \(a\), define the raw excess

\[
 E=\sum_a(\ell(a)-m c(a))_+.                           \tag{0.6}
\]

Then

\[
 \boxed{\,sW-r_\Gamma(P)\le\lfloor E/m\rfloor .\,}    \tag{0.7}
\]

In particular \(E<m\) gives an exact full-port router.  A natural exact
certificate is **endpoint-star locality**: every finite suffix capacity is
used only by catalogue paths having one common start port, or only by paths
having one common terminal sink.  Exactly \(m\) catalogue paths leave each
port and exactly \(m\) enter each sink, so endpoint-star locality gives
\(\ell(a)\le m\), hence \(E=0\).

On an exact-period-\(q\), capacity-faithful invariant stratum for which the
audited stabilizer theorem applies to the **complete** residual gate and
gives

\[
 q\mid \bigl(sW-r_\Gamma(P)\bigr),                    \tag{0.8}
\]

the weaker inequality \(E<mq\) already forces exact routing.  If the
complete materialized gate retains the full fresh-pair \(C_k\) action, then
in the old-coordinate central band \(q\ge k/(2D+1)\).  Therefore raw excess

\[
 E<\frac{mk}{2D+1}                                    \tag{0.9}
\]

is sufficient on that stratum.  For \(D=O(\sqrt{k})\), any
\(E=o(k^{3/2})\) satisfies (0.9) eventually.  More generally, if the fully
pinned residual gate retains only a subgroup \(H_k\le C_k\) of order
\(h_k\), the valid lower bound and sufficient inequality are

\[
 q\ge {h_k\over 2D+1},
 \qquad
 E<{mh_k\over2D+1}.                                  \tag{0.9a}
\]

No growth follows merely from the ambient coordinate action after the pins
have broken it.

The scale is sharp.  Even when every Middle-Levels containment has a
literal path, all paths can be passed through \(c\) common unit bottlenecks.
The suffix gammoid is then \(U_{c,sW}\), and a balanced catalogue has

\[
 \Omega_{\rm cut}=\Omega_{\rm tot}=sW-c
 =sW-r_\Gamma(P).                                    \tag{0.10}
\]

Consequently Boolean shadow expansion and complete individual incidence
reachability do not prove the router.  The missing physical row is a
capacity-faithful occurrence lift with bounded normalized cut overload;
endpoint-star locality is one transparent sufficient form.

## 1. The overload lemma

All capacities below are on arcs and all finite capacities are positive
integers.  A unit vertex capacity is represented by its node-splitting arc;
larger integral capacities may be expanded into private unit lanes when a
literal strict-gammoid model is desired.  Infinite transport arcs never
contribute to a finite cut or to the overload sums.

Let \({\cal Q}\) be a finite family of directed simple \(P\)-to-\(T\) paths
and let \(w_Q\ge0\) for \(Q\in{\cal Q}\).  Assume the exact endpoint
balances

\[
 \sum_{Q:\,Q\text{ starts at }p}w_Q=1 \quad(p\in P),
 \qquad
 \sum_{Q:\,Q\text{ ends at }t}w_Q=1 \quad(t\in T).   \tag{1.1}
\]

The path sum is a conserved source--sink flow \(f\) of value \(N\), except
that an internal finite arc may have \(f(a)>c(a)\).  The unit source and
sink arcs have load exactly one and therefore zero overload.

### Theorem 1.1 (cut-overload router bound)

Under (1.1), equation (0.2) holds.

### Proof

Let \(W\) be the source side of any finite source--sink cut.  Flow
conservation gives

\[
 N=f(\delta^+(W))-f(\delta^-(W)).                     \tag{1.2}
\]

Since the backward term is nonnegative,

\[
 \begin{aligned}
 N
 &\le f(\delta^+(W))\\
 &\le c(\delta^+(W))
     +\sum_{a\in\delta^+(W)}(f(a)-c(a))_+\\
 &\le c(\delta^+(W))+\Omega_{\rm cut}(f).
 \end{aligned}                                       \tag{1.3}
\]

Thus every finite cut has capacity at least
\(N-\Omega_{\rm cut}(f)\).  Max flow/min cut gives

\[
 r_\Gamma(P)\ge N-\Omega_{\rm cut}(f).               \tag{1.4}
\]

The corank is an integer, so it is at most
\(\lfloor\Omega_{\rm cut}(f)\rfloor\).  The second inequality in (0.2)
is immediate because every outgoing cut is a subset of the finite arcs.
\(\square\)

### Remarks

1. This is not worst-congestion scaling.  A bounded amount of excess on a
   bounded region costs only its total normalized excess; it does not scale
   down the flow on every unaffected path.
2. Serial bottlenecks may be charged more than once by
   \(\Omega_{\rm tot}\).  The cut quantity is sharper and is the direct
   certificate.  The total quantity is often easier to prove.
3. The argument needs one simultaneous weighted path catalogue.  A list of
   paths available one at a time does not define \(f\).
4. All occurrence identities and terminal types must already be represented
   in \(D\).  Anonymous switching at a shared vertex is not validated by
   this theorem.

## 2. Balanced semantic factors

Let

\[
                         H=(P,T;F)                   \tag{2.1}
\]

be a bipartite graph with \(|P|=|T|=N\).  Assume every vertex has degree
\(h\ge1\).  It is enough to assume left degree \(h\) and right degree at
most \(h\): counting the \(hN\) incidences forces every right degree to be
exactly \(h\).

For every \(e=pt\in F\), suppose one legal literal path \(R_e:p\leadsto t\)
has been fixed in the same residual typed suffix network.  Paths may share
physical capacities, which remain represented once.  Put

\[
 \ell(a)=|\{e\in F:a\in R_e\}|,\qquad
 E_H=\sum_a(\ell(a)-h c(a))_+.                        \tag{2.2}
\]

### Theorem 2.1 (balanced-factor overload router)

\[
 \boxed{\,N-r_\Gamma(P)\le\lfloor E_H/h\rfloor .\,}  \tag{2.3}
\]

### Proof

Give every edge-path \(R_e\) weight \(1/h\).  Exactly \(h\) such paths
leave every port and exactly \(h\) enter every sink, so (1.1) holds.  The
load on \(a\) is \(\ell(a)/h\).  The total positive overload is \(E_H/h\);
apply Theorem 1.1. \(\square\)

If every capacity used by the catalogue lies in one start star or one
terminal star, then \(\ell(a)\le h\) and the factor routes exactly.  More
generally, fewer than \(h\) raw excess edge--capacity incidences cause no
defect, while \(E_H=O(h)\) gives bounded defect.

This theorem is deliberately a **second** factor statement.  The protected
Middle-Levels theorem currently supplies an abstract claim--port factor.
To invoke Theorem 2.1 as a suffix theorem, one must additionally realize a
balanced addressed port--sink factor by literal paths after compensation.
The two abstract uses cannot be identified without that occurrence and
capacity proof.

## 3. The Middle-Levels occurrence lift

Let \(\Sigma\) be a sheet set of size \(s\), and put

\[
 P={\cal L}\times\Sigma,\qquad T={\cal R}\times\Sigma .
                                                                    \tag{3.1}
\]

For every base incidence \(A\subset B\), choose a permutation
\(\sigma_{A,B}\in\operatorname{Sym}(\Sigma)\), and suppose (0.5) is one
legal path in the same residual typed network.  Different catalogue paths
may share physical capacities; those capacities occur once in \(D\).

Every \((m-1)\)-set has exactly \(m\) containing \(m\)-sets.  Hence exactly
\(m\) paths in (0.5) start at each \(p_{A,\xi}\).  Conversely, every
\(m\)-set has exactly \(m\) contained \((m-1)\)-sets.  For fixed \(A\subset
B\), the permutation \(\sigma_{A,B}\) sends exactly one sheet to any fixed
terminal sheet.  Hence exactly \(m\) paths end at each \(t_{B,\zeta}\).

Giving every path weight \(1/m\) therefore satisfies (1.1).  The load on a
finite arc is

\[
 f(a)=\ell(a)/m.                                      \tag{3.2}
\]

For a capacity-\(c(a)\) arc,

\[
 (f(a)-c(a))_+=\frac{1}{m}(\ell(a)-mc(a))_+.          \tag{3.3}
\]

Summing (3.3) and applying Theorem 1.1 proves (0.7).

### Corollary 3.1 (endpoint-star locality)

If every finite capacity arc is used only by paths with one common start
port, or only by paths with one common terminal sink, then the full port set
links to \(T\).

### Proof

There are only \(m\) catalogue paths at a fixed start and only \(m\) at a
fixed terminal.  Therefore \(\ell(a)\le m\) on every unit capacity arc.
For a larger integral capacity the inequality
\(\ell(a)\le mc(a)\) is even weaker.  Thus \(E=0\), and (0.7) gives full
rank. \(\square\)

This permits arbitrary sharing among the \(m\) alternative paths incident
with one port or one sink.  It is strictly weaker than demanding one
pairwise-disjoint suffix for every port in advance; max-flow integrality
chooses the compatible alternatives.

### Corollary 3.2 (exceptional collision budget)

Let \(Z\) be the finite capacities not certified endpoint-star-local.  If

\[
 E_Z=\sum_{a\in Z}(\ell(a)-mc(a))_+,                 \tag{3.4}
\]

then the suffix corank is at most \(\lfloor E_Z/m\rfloor\).  In particular:

* fewer than \(m\) raw excess route--capacity incidences cause no defect;
* \(E_Z=O(m)\) causes only \(O(1)\) defect; and
* \(E_Z=o(msW)\) is not by itself enough for bounded defect--the relevant
  normalization is by \(m\), not by the exponentially large shore size.

## 4. Balanced claims and two occurrence coordinates

Suppose in addition that \(B=(G,P;E_B)\) is balanced \(h\)-regular on
\(|G|=|P|=N\), every incidence has an edge-private, port-complete literal
claim-to-port prefix, and prefix interiors are disjoint from the suffix
network.  The exact balanced-rank transfer theorem gives

\[
 \max\{\text{simultaneously serviced claims}\}=r_\Gamma(P).
                                                                    \tag{4.1}
\]

Combining (4.1) with Theorem 1.1 yields

\[
 \boxed{
 |G|-\nu_{\rm claim}
 \le\lfloor\Omega_{\rm cut}(f)\rfloor
 \le\lfloor\Omega_{\rm tot}(f)\rfloor .}            \tag{4.2}
\]

Thus the Boolean path catalogue closes both the suffix rank and the claim
selection; no preselected router-good port transversal is required.

For the two physical occurrence coordinates of a common-cap ticket system,
apply (4.2) in the same fixed cap state after all cross-coordinate shared
capacities have been allocated.  Put

\[
 C_p=\lfloor\Omega_{{\rm cut},p}\rfloor,\qquad p=0,1.
                                                                    \tag{4.3}
\]

Coordinate \(p\) services some claim set of size at least \(N-C_p\).
Heredity services their intersection in both coordinates, whose size is at
least \(N-C_0-C_1\).  Under the global product-closure and typed lifting
hypotheses of the two-coordinate common-cap theorem, those two marginal
linkages combine.  Consequently the common claim deficiency is at most

\[
                         C_0+C_1.                    \tag{4.4}
\]

Named structural-zero tickets or transported-background omissions are
added exactly as in that theorem.  Formula (4.4) does not authenticate
transported phase 1 or prove product closure.

## 5. Exact-period promotion

Assume now that the complete residual suffix gate belongs to one exact
period-\(q\), capacity-faithful stratum and satisfies the hypotheses of the
stabilizer-stratified corank theorem.  Concretely, the source ports, sink
terminals, internal addressed vertices, and every finite-capacity arc are
partitioned into free \(q\)-orbits; all capacities, lower bounds, and exact
quotas have orbit totals divisible by \(q\); and no nonfree capacity is
silently shared with the stratum.  That theorem supplies the arithmetic
conclusion

\[
                 q\mid N-r_\Gamma(P).                \tag{5.1}
\]

Theorem 1.1 therefore gives the following immediate promotion.

### Corollary 5.1

If \(\Omega_{\rm cut}(f)<q\), then \(r_\Gamma(P)=N\).  For the uniform
Middle-Levels catalogue it is enough that \(E<mq\).

Under the full common fresh-pair action on \(k=2m-1\) old coordinates, every
addressed object retaining an equivariant old-subset label in the band
\(|s-m|\le D\) has orbit order at least \(k/(2D+1)\).  On a \(q\)-pure
capacity-separated stratum, (0.9) follows.  If the pins preserve only
\(H_k\le C_k\), the same stabilizer argument gives the subgroup version
(0.9a), not (0.9).

The qualifications are load-bearing.  Mixed exact periods sharing one
capacity need not have a growing common modulus.  A fresh-only fixed
bottleneck does not retain the old-subset address and is outside the
promotion theorem.  Symmetry is used only after the analytic overload
bound; it does not create a path catalogue or capacity expansion.

## 6. Sharp bottleneck model

Let \(N=sW\) and choose \(1\le c\le N\).  For this symbolic counterexample,
give all \(N\) sinks one common terminal type.  Introduce \(c\) unit
node-split bottleneck vertices \(b_1,\ldots,b_c\), join every port to every
bottleneck entrance, and join every bottleneck exit to every sink.  This is
the three-layer suffix network representing \(U_{c,N}\): at most \(c\)
ports link because every path uses a bottleneck capacity, while any at most
\(c\) ports link by choosing distinct bottlenecks and distinct sinks.  Hence

\[
                         r_\Gamma(P)=c.              \tag{6.1}
\]

It also contains a path for every addressed Middle-Levels incidence in the
sheet lift (and possibly additional port--sink paths, which only strengthen
the counterexample).
For every \(A\subset B\), every sheet \(\xi\), and every bottleneck \(b_j\),
use the path

\[
 p_{A,\xi}\to b_j\to t_{B,\sigma_{A,B}(\xi)}
                                                                    \tag{6.2}
\]

with weight \(1/(mc)\).  Endpoint balance is again one.  Each bottleneck
has load \(N/c\), and all other finite capacities have load at most one.
Therefore

\[
 \Omega_{\rm tot}
 =c\left(\frac Nc-1\right)=N-c.                     \tag{6.3}
\]

The cut through the \(c\) node-splitting bottleneck arcs has exactly the
same overload, so

\[
 \Omega_{\rm cut}=N-c=N-r_\Gamma(P).                 \tag{6.4}
\]

Thus Theorem 1.1 is sharp, including on a network containing every Boolean
containment route with perfectly balanced endpoint marginals.  Complete
semantic shadows do not control physical simultaneous capacity.

## 7. Exact remaining occurrence row

The theorem replaces the full pairwise-disjoint-suffix premise by the
following weaker, checkable certificate in one materialized child:

1. **Occurrence completeness.**  The ports and sinks admit a sheet-balanced
   literal lift (0.5), or more generally a weighted endpoint-balanced path
   catalogue (1.1).
2. **Capacity faithfulness.**  Every shared physical resource is represented
   once by its finite capacity arc, all state and type restrictions are
   retained, and the fixed compensation linkage has already been deleted.
3. **Localized overload.**  The catalogue has
   \(\Omega_{\rm cut}=O(1)\), or the stronger easily audited
   \(\Omega_{\rm tot}=O(1)\).  Endpoint-star locality gives zero.
4. **For exact symmetry promotion.**  The complete gate is one
   capacity-separated exact-period stratum and its normalized overload is
   smaller than the stratum order.

The current all-\(k\) record proves neither item 1 nor item 3 for the actual
parent-derived occurrence/phase suffixes.  The protected Middle-Levels
two-factor supplies an abstract incidence factor, not the sheet permutations
and literal paths in (0.5).  Physical provider nesting does not imply
supplier-port nesting, and transported phase 1 remains theorem input.

Conversely, the bottleneck model proves that no argument using only Boolean
containment, individual route existence, endpoint balance, or common
symmetry can omit the capacity-overload row.  The smallest new structural
target is therefore:

\[
 \boxed{
 \text{one same-state occurrence lift of the Middle-Levels incidences}
 \quad+\quad
 E=O(m)
 }
                                                                    \tag{7.1}
\]

for bounded defect, or \(E<mq\) on a \(q\)-pure stratum for exactness.
This is strictly weaker than constructing pairwise-disjoint suffixes for
all ports, but it is not a consequence of the presently proved Boolean
owner or Ferrers geometry.
