# Independent audit: Boolean-incidence overload suffix router

**Date:** 2026-08-03  
**Audited theorem:** MATH_THEOREM_BOOLEAN_INCIDENCE_OVERLOAD_SUFFIX_ROUTER_20260803.md  
**Pre-audit SHA-256:** 000f26fc5186afa2002357cdc5f75676ec2b83c8c5fedd11d2cc2383c9e43746  
**Post-audit SHA-256:** cb04ec984aa7e9098375065093ef6d0228b2fcf38f0c72749522a6bbce67b6e2  
**Verdict:** **GO after scope corrections.**

This is a proof audit only. No finite search, numerical optimization, or
instance enumeration was used.

## 1. Network and capacity convention

The theorem is correct for one fixed finite directed residual network after
the compensation linkage and every other reserved capacity have been
deleted. All finite capacities must be nonnegative integers. Deleting
zero-capacity arcs and replacing larger capacities by the standard
unit-capacity expansion identifies maximum integral flow with the rank of a
strict gammoid on the unit source-port set. In the unexpanded presentation,
the notation \(r_\Gamma(P)\) is therefore exactly the maximum integral
source--sink flow value.

This convention is load-bearing in two places:

1. max-flow integrality turns cut capacity into an integer gammoid rank;
2. endpoint-star locality implies \(\ell(a)\le h c(a)\) only for a used
   positive integral capacity (zero-capacity arcs must be absent).

The theorem now states this convention explicitly.

## 2. Pseudoflow cut inequality and the floor

Let the weighted path catalogue have endpoint balance one at every
\(p\in P\) and \(t\in T\). After adding the unit source-port and
sink-terminal arcs, its path sum is a conserved pseudoflow of value \(N\).
For any finite source side \(W\),

\[
 N=f(\delta^+(W))-f(\delta^-(W))
 \le f(\delta^+(W)).
\]

Writing \(f(a)\le c(a)+(f(a)-c(a))_+\) on each outgoing finite arc gives

\[
 c(\delta^+(W))
 \ge N-\sum_{a\in\delta^+(W)}(f(a)-c(a))_+
 \ge N-\Omega_{\rm cut}(f).
\]

Taking the minimum cut gives

\[
 r_\Gamma(P)\ge N-\Omega_{\rm cut}(f).
\]

Hence the integer corank satisfies

\[
 N-r_\Gamma(P)\le\lfloor\Omega_{\rm cut}(f)\rfloor.
\]

This floor is in the correct direction: if an integer \(z\) obeys
\(z\le x\), then \(z\le\lfloor x\rfloor\). Finally every outgoing cut is a
subset of the finite arc set, so
\(\Omega_{\rm cut}\le\Omega_{\rm tot}\), and monotonicity of the floor gives
the second inequality. Backward cut flow is handled with the correct sign;
no assumption that the catalogue itself is capacity-feasible is used.

## 3. Balanced degree-\(h\) normalization

For a balanced bipartite port--sink factor \(H=(P,T;F)\), give every
edge-path weight \(1/h\). Exactly \(h\) paths leave each port and exactly
\(h\) enter each sink, so both endpoint equations equal one. The load on a
finite arc is

\[
 f(a)={\ell(a)\over h},
\qquad
 (f(a)-c(a))_+
 ={1\over h}\bigl(\ell(a)-h c(a)\bigr)_+.
\]

Therefore

\[
 N-r_\Gamma(P)
 \le
 \left\lfloor {1\over h}
 \sum_a(\ell(a)-h c(a))_+\right\rfloor.
\]

The advertised weaker hypothesis is also exact: if every left degree is
\(h\), every right degree is at most \(h\), and both shores have \(N\)
vertices, the \(hN\) incidences force every right degree to equal \(h\).

## 4. Middle-Levels specialization \(h=m\)

On ground set \([2m-1]\),

\[
 {\cal L}={[2m-1]\choose m-1},
 \qquad
 {\cal R}={[2m-1]\choose m}
\]

have equal size \(W\). Every \(A\in{\cal L}\) has exactly \(m\) containing
members of \({\cal R}\), and every \(B\in{\cal R}\) has exactly \(m\)
contained members of \({\cal L}\). With \(s\) sheets and one permutation
\(\sigma_{A,B}\) on the sheet set for every incidence:

* exactly \(m\) catalogue paths start at each \(p_{A,\xi}\);
* for fixed \(t_{B,\zeta}\) and each of the \(m\) lower neighbours \(A\),
  bijectivity of \(\sigma_{A,B}\) gives exactly one incoming sheet \(\xi\);
  hence exactly \(m\) paths end at \(t_{B,\zeta}\).

Weight \(1/m\) therefore gives exact endpoint conservation, and

\[
 (f(a)-c(a))_+
 ={1\over m}\bigl(\ell(a)-m c(a)\bigr)_+.
\]

This proves the raw-excess formula
\[
 sW-r_\Gamma(P)\le\lfloor E/m\rfloor.
\]

## 5. Endpoint-star locality

For the one-path-per-incidence Middle-Levels catalogue, an arc contained
only in paths from one fixed start port occurs in at most its \(m\) outgoing
catalogue paths. The same bound holds if all its users terminate at one
fixed sink. Thus \(\ell(a)\le m\). Since every used finite capacity has
\(c(a)\ge1\),

\[
 \ell(a)\le m\le m c(a).
\]

Every raw excess term vanishes. The argument is per capacity: different
capacities may choose different start or terminal stars. It does not
require all paths to be pairwise disjoint, and it does not assert that the
current OR-word child has such locality.

## 6. Balanced claim transfer and two coordinates

Under the separately proved edge-private, port-complete balanced-prefix
hypotheses, the maximum number of simultaneously serviced claims equals
\(r_\Gamma(P)\). Combining this equality with the overload bound is
therefore valid.

For coordinate \(p\), choose an actually serviced claim set \(S_p\) of size
at least \(N-C_p\). Restricting a valid linkage to
\(S_0\cap S_1\) preserves validity in each coordinate, and

\[
 |S_0\cap S_1|\ge N-C_0-C_1.
\]

Combining the two restricted linkages still requires the stated global
product-closure, typed-state, and cross-coordinate capacity hypotheses.
The marginal argument alone neither authenticates transported phase 1 nor
proves simultaneous physical compatibility.

## 7. Exact-period promotion and fresh-pair scope

If the **complete** residual gate is one capacity-faithful exact-period
\(q\) stratum, with free \(q\)-orbits for ports, terminals, internal
addressed vertices, and every finite-capacity arc, and every orbit quota is
divisible by \(q\), then both full demand and maximum integral flow are
multiples of \(q\). Hence

\[
 q\mid N-r_\Gamma(P).
\]

Together with \(N-r_\Gamma(P)\le\lfloor E/m\rfloor\), the strict inequality
\(E<mq\) forces zero corank.

The pre-audit statement used the ambient fresh-pair bound without explicitly
requiring that the pins preserve that action. This was too broad. The
correct alternatives are:

* if the full \(C_k\) action survives, then
  \(q\ge k/(2D+1)\) and \(E<mk/(2D+1)\) suffices;
* if only \(H_k\le C_k\) of order \(h_k\) survives, then
  \(q\ge h_k/(2D+1)\) and \(E<mh_k/(2D+1)\) suffices.

Indeed an addressed old-subset projection in the band has stabilizer order
at most \(2D+1\). For the full action and
\(D=O(\sqrt{k})\), the sufficient threshold is
\(\Omega(k^{3/2})\), because \(m=(k+1)/2\). Thus
\(E=o(k^{3/2})\) is eventually sufficient. No such conclusion follows
when the residual subgroup \(h_k\) is bounded or when a shared finite
capacity has smaller period.

## 8. Sharp \(U_{c,N}\) model

Take \(N=sW\) common-type sinks and \(c\) unit node-split bottlenecks. Join
every port to every bottleneck entrance and every bottleneck exit to every
sink. Any linkage uses distinct bottleneck capacities, so its size is at
most \(c\). Conversely, any at most \(c\) ports link by choosing distinct
bottlenecks and distinct sinks. The induced gammoid is exactly
\(U_{c,N}\), not merely a rank-\(c\) upper bound.

For every addressed Middle-Levels incidence and each bottleneck, take the
corresponding path with weight \(1/(mc)\). At each port there are \(mc\)
such paths, and at each sink the \(m\) lower neighbours, sheet
permutations, and \(c\) bottlenecks again give \(mc\) paths. Endpoint load
is one.

For a fixed bottleneck there are \(mN\) catalogue paths, hence its split arc
has load

\[
 {mN\over mc}={N\over c}.
\]

Source-port and sink-terminal loads are one; all remaining arcs are
infinite transport arcs. Therefore

\[
 \Omega_{\rm tot}
 =c\left({N\over c}-1\right)=N-c.
\]

The source side cut through all \(c\) bottleneck split arcs has the same
overload, so

\[
 \Omega_{\rm cut}=N-c=N-r_\Gamma(P).
\]

This proves equality in the overload theorem. Allowing extra
non-incidence port--sink routes in this symbolic common-type network does
not weaken the counterexample: it already has the maximum possible
individual reachability while retaining arbitrary corank \(N-c\).

## 9. Corrections and exact scope

The following corrections were applied:

1. finite capacities are now explicitly positive integral and the
   capacity-expansion/gammoid convention is stated;
2. the fresh-pair threshold is conditioned on the actual surviving
   stabilizer, with the subgroup formula recorded;
3. the bottleneck model explicitly uses a common terminal type and proves
   both inequalities needed for \(U_{c,N}\);
4. the exact-period corollary numbering was corrected.

After these corrections, every displayed inequality and specialization
audited above is valid.

The result remains a conditional fixed-network certificate. It proves
neither:

* the occurrence-sheet permutations and literal paths for the current
  parent-derived child;
* endpoint-star locality or \(E=O(m)\);
* global two-coordinate product closure;
* transported phase 1;
* preservation of a growing residual stabilizer after all pins; nor
* \(\nu(k)\le B(k)+O(1)\).

The mathematically exact new target is one simultaneous endpoint-balanced
literal occurrence catalogue whose normalized cut overload is bounded (or
falls below the authenticated exact-period modulus).
