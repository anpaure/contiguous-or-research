# Odd antipodal completion: residual Hall and component-colour overload

Date: 2026-08-01  
Status: exact conditional completion theorem for the half-length outer sector
at odd `m`.  It corrects the tempting but false inference that an arbitrary
antipodal matching can be chosen independently of the full-orbit cap state.

## 0. Setup

Let `m=2h+1`.  Fix an exact full/full outer selector `F_0` under
`C_(2m)` and assume its literal middle load is at most two.  The unsatisfied
outer margins are the half-length lower and upper necklaces from Theorem 2.1
of
`MATH_THEOREM_CATALAN_ROTATION_PARITY_SECTOR_AND_SLACK_DESIGN_20260801.md`.

Write their representatives as `A in binom(Z_m,h)` and
`B in binom(Z_m,h+1)`, modulo rotation.  A containment orbit

\[
                         A\subset B=A+\{b\}             \tag{0.1}
\]

adds the antipodal physical matching on the free middle necklace

\[
 \mathcal O(A,b)=C_{2m}\bigl(L(A)+\{b\}\bigr).          \tag{0.2}
\]

The map from the quotient containment edge `(A,B)` to `mathcal O(A,b)` is
injective.

## 1. Exact cap-completion Hall theorem

Form a bipartite graph `H(F_0)` on the half-length lower and upper
necklaces.  Retain the quotient edge `(A,B)` exactly when every literal
vertex of `mathcal O(A,b)` has `F_0`-degree at most one.  Rotation invariance
makes this one check on a necklace representative.

### Theorem 1.1

There is an invariant antipodal-sector completion which preserves all outer
margins and literal cap two if and only if `H(F_0)` has a perfect matching,
equivalently

\[
                     |N_{H(F_0)}(S)|\ge |S|             \tag{1.1}
\]

for every family `S` of half-length lower necklaces.

#### Proof

Every half/half orbit contributes load exactly one on `mathcal O(A,b)` and
zero elsewhere.  Distinct quotient containment edges have distinct middle
necklaces: a literal endpoint has `h` complete antipodal pairs and one
singleton, from which `A`, `b`, and the edge orbit are recovered.  Therefore
an edge is cap-compatible exactly when it survives in `H(F_0)`, with no
additional cross-edge cap conflict.

The remaining outer requirement is one selected edge at every lower and
upper half-necklace.  This is exactly a perfect matching of `H(F_0)`, and
(1.1) is Hall's theorem.  \(\square\)

Thus the periodic outer margins are easy only after the residual Hall row
has been checked.  The unconditional regular matching from the parity-sector
theorem is the special case `F_0=emptyset`.

## 2. Exact topology cost when the full support is a forest

Assume now that the ordinary quotient support of `F_0` is a forest.  Colour
an allowed edge `(A,B)` of `H(F_0)` by the ordinary tree component containing
the middle necklace `mathcal O(A,b)`; a necklace unused by `F_0` is its own
singleton component.

For a perfect matching `P` of `H(F_0)`, let `k_C(P)` be the number of its
edges of component colour `C`.

### Theorem 2.1 (component-colour formula)

The completed selector has frame nullity

\[
                 \boxed{\delta_{\rm fr}(F_0\cup P)
                    =\sum_C (k_C(P)-1)^+.}            \tag{2.1}
\]

In particular its literal lift is a forest if and only if `P` is a rainbow
perfect matching with respect to the component colours.

#### Proof

Each antipodal orbit is one negative half-loop at its coloured quotient
vertex.  The ordinary support is a forest.  By the signed-frame criterion,
the first negative half-loop in an ordinary tree component is independent
and every further one contributes one unit of frame nullity.  Summing over
components gives (2.1).  \(\square\)

This isolates the remaining correlation sharply:

* cap-compatible outer completion is ordinary bipartite Hall;
* exact topology is a third, component-colour injectivity condition;
* bounded topology asks only for a perfect matching with bounded total
  colour overload in (2.1).

The last object is a three-partition matching problem, not a consequence of
the separate Hall rows.  It is nevertheless much smaller and more explicit
than the original literal graphic constraint.

## 3. General full-support defect

If `F_0` already has ordinary quotient cycles, its ordinary graphic nullity
adds to (2.1).  More generally one simply evaluates the exact frame rank
formula

\[
 \delta_{\rm fr}=e_0+q_0-|V_0|+c_0-u_0
\]

from
`MATH_THEOREM_CATALAN_ODD_ROTATION_FRAME_MATROID_AND_DEFECT_20260801.md`.
No separate literal component expansion is required.

This theorem does not prove that `H(F_0)` always has a perfect matching for
an arbitrary full selector, nor that a bounded-overload perfect matching
always exists.  Those are the exact residual Hall and correlation gates.

