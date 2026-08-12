# Audit of the two-root extreme-wrap obstruction

**Date:** 2026-08-06  
**Audited note:**  
MATH_OBSTRUCTION_ODD_TWO_ROOT_EXCHANGE_CUBE_EXTREME_WRAP_ONLY_20260806.md  
**Method:** direct scan-order and coordinate replay; no computation  
**Verdict:** PASS after using opposite scan orders: \(M^-\) left-to-right
and \(M^+\) right-to-left.

## 1. Zipper order

The opposite scan orders are essential.  After a suffix quiet block is
shifted into the \(M^+\)-alignment, the right-to-left \(M^+\)-scan skips
that suffix and acts at the next carrier interface.  The left-to-right
\(M^-\)-scan then skips the untouched quiet prefix and closes the same
three-coordinate interface before reaching the shifted suffix.  The three
local replays are exactly

\[
001\to010\to100,\qquad
201\to210\to120,\qquad
221\to212\to122.
\]

Induction moves the singleton through every quiet block without changing
their order.  Hence the alternating endpoint is literal one-coordinate
rotation.  Using the same scan order in both phases would not prove this;
the theorem contains the corrected opposite-order statement.

## 2. Boundary equations

Writing \(q(a)=(2A(a),2B(a))\), interior equality across a wrap edge gives

\[
 B(u_j)=A(v_j),\qquad B(v_j)=A(u_{j+1}).
\]

Endpoint mass transfer supplies the cyclic final equation.  Since
\(B(a)\le A(a)\), the cyclic chain

\[
 A(u_j)\ge B(u_j)=A(v_j)\ge B(v_j)=A(u_{j+1})
\]

forces equality everywhere.  Thus every \(u_j\) is zero or every \(u_j\)
is two, and \(v=u\).  Both extreme words do give literal wrap edges, so
the classification is if and only if.

## 3. Scope

At fixed nonextreme compressed mass the entire induced wrap graph on
\(Q^-\cup Q^+\) is empty.  Every basis in the two-root exchange cube is a
subset of this union, so none can carry the required current.  This does
not exclude a noncanonical basis outside the exchange cube, and it makes
no hub-colour claim.

The stronger all-root statement also checks.  A canonical quiet residue
has exactly one coordinate of value one, namely its root; every other
coordinate is zero or two.  A fixed-boundary transfer changes only its two
boundary coordinates.  Therefore roots away from the boundary must agree
at both ends, after which the boundary coordinates would be forced from
even values to one and could not remain quiet.  Equal boundary roots are
also impossible because their value one changes.  The only possible root
pair is the two distinct boundary roots, already classified above.
