# Audit of the exact Ferrers-boundary capacity owner flow

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_EXACT_FERRERS_BOUNDARY_AND_CAPACITY_D_OWNER_FLOW_20260807.md`  
**Verdict:** PASS after adding the trivial (d=0) branch.  The fractional
loads, boundary lower bounds, and total-unimodularity argument are exact.
The conclusion is an ordinary containment assignment only; it has no
ownerwise comparability content.

## 1. Fractional flow

For rank (s<R), put

\[
 C_s=\binom{k}{s},\qquad
 A_s=\binom{k-s}{R-s},\qquad
 W=\binom{k}{R}.
\]

A rank-(s) target sends (1/C_s) to each of the (b_s) boundary
slots, for total boundary mass (b_s/C_s).  It sends the remaining mass
uniformly to its (dA_s) labelled containing-owner slots.  Hence each such
edge receives

\[
 \frac{1-b_s/C_s}{dA_s}.
\]

Every boundary slot receives (C_s/C_s=1).  A fixed labelled owner slot
receives

\[
 \sum_{s<R}\binom Rs
 \frac{1-b_s/C_s}{dA_s}
 =\frac1{dW}\sum_{s<R}(C_s-b_s)\le1,
\]

using

\[
 C_sA_s=W\binom Rs.
\]

All displayed fractional identities pass.

When (d=0), the original displayed density divided by zero.  Condition
(1.3) then forces (b_s=C_s) for every (s), so every target is placed
in the boundary and no owner edge is needed.  This branch has now been
inserted in the source proof.

## 2. Integrality with boundary saturation

The network has:

* unit supply at every lower target;
* unit-capacity boundary and labelled-owner slots;
* lower bound one on every boundary-slot saturation requirement; and
* ordinary upper bounds on owner slots.

This is a bipartite flow network with integral lower/upper bounds.  Its
node-edge incidence matrix is totally unimodular, so fractional feasibility
implies an integral feasible flow.  At an integral point:

1. every target chooses exactly one slot;
2. every boundary slot receives a different target, because each target
   has total supply one;
3. exactly (b_s) distinct rank-(s) targets enter the boundary; and
4. at most (d) residual targets enter any owner.

Thus Theorem 2.1 and Corollary 2.2 are correct.

## 3. Audit boundary

The theorem proves exact feasibility for:

* prescribed rank counts in the boundary;
* containment of every residual target in its owner;
* owner capacity (d); and
* all ordinary Hall cuts of that bipartite network.

It does not constrain two targets assigned to the same owner to be
comparable.  Adding that requirement replaces the network matrix by a
configuration/flag hypergraph and destroys the TU proof.  The exact form
of the surviving flag gate is recorded separately in
`MATH_THEOREM_FERRERS_FLAG_HYPERGRAPH_AND_CHAINIZATION_BARRIER_20260807.md`.
