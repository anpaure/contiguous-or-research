# Independent audit: five-slot size-four-efficient three-face boundary reduction

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FIVE_SLOT_FOUR_EFFICIENT_THREE_FACE_BOUNDARY_REDUCTION_20260804.md`  
**Method:** exact symbolic proof audit only; no finite search, numerical
optimization, or sampled sign check.

## Verdict

**PASS**, with the stated scope.  The endpoint reduction, the literal
five-residue train lower bound, the three-face decomposition, and the two
inert-face assertions are correct.  The theorem does not prove positivity
of any of the three remaining train functions.

## 1. Constraint audit

Internal superadditivity gives

\[
2x\le y,
\qquad x+y\le z,
\qquad x+z\le P,
\qquad2y\le P,
\qquad P+x\le T,
\qquad y+z\le T.
\]

Maximal efficiency of the size-four generator gives

\[
x\le P/4,
\qquad y\le P/2,
\qquad z\le3P/4,
\qquad T\le5P/4.
\]

Since `A<=T<=5P/4`, necessarily `P>=4A/5`; first crossing gives
`P<A`.  These reproduce (0.3)--(0.4).

Every exact capacity-five partition is dominated by `4+1` or `3+2`:

- `3+1+1` is at most `z+y` because `2x<=y`;
- `2+2+1` is at most `P+x` because `2y<=P`;
- refinements using more ones are smaller by the same prefix inequalities.

Hence `R=max(P+x,y+z)` is exactly the strongest lower bound on the
size-five endpoint imposed by internal superadditivity.

## 2. Endpoint reduction audit

For

\[
T_*=\max(A,P+x,y+z),
\]

the original constraints give `T_*<=T<=5P/4`.  Thus lowering `T` to
`T_*` preserves nonnegativity, first crossing, internal
superadditivity, and maximal size-four efficiency.

Bellman values below capacity five are unchanged.  Bellman values at every
capacity at least five are at least the endpoint, hence at least `A`, and
are nondecreasing as `T` increases.  Since the signed-tail kernel is
increasing on `[A,infinity)`, every changed summand is nondecreasing.  This
proves

\[
\Phi(x,y,z,P,T)\ge\Phi(x,y,z,P,T_*).
\]

The active maximum defining `T_*` yields exactly the three closed faces
`F_A`, `F_14`, and `F_23`, including their overlaps.

## 3. Endpoint-period train audit

For `m=5q+r`, `0<=r<5`, the exact-fill configuration with `q` copies of
the size-five generator and one size-`r` generator has value

\[
qT_*+c_r.
\]

At `q=0`, internal superadditivity gives the exact prefix value
`V_r=c_r`.  At `q>=1`, both the candidate and the Bellman optimum lie in
the monotone tail `[A,infinity)`.  Therefore termwise kernel comparison and
absolute tail convergence give

\[
\Phi(x,y,z,P,T_*)
\ge
\sum_{r=0}^{4}\sum_{q\ge0}K(qT_*+c_r)
=\mathscr B_{T_*}(x,y,z,P).
\]

Together with endpoint monotonicity this proves the same lower bound for
the original table.  For `tau>=A`, the `q=0` term of `F_tau(v)` is fixed
and every `q>=1` argument increases with `tau`, so
`F_tau(v)>=F_A(v)` is also correct.

## 4. Exact-head audit

At maximal size-four efficiency the reduced weights are

\[
d_1=T_*-5P/4,
\qquad d_2=y-P/2,
\qquad d_3=z-3P/4,
\]

which agrees with the theorem's `d_1=e_*-P/4` because `e_*=T_*-P`.
All are nonpositive.  The four displayed maximum-walk formulas for each
nonzero residue are exactly the simple residue walks on `Z/4Z`.  The
availability delay is bounded by three size-five steps, so the literal
correction through capacities `0,...,14` is the complete finite head.  The
endpoint-period lower bound was proved directly from the literal Bellman
clock and therefore does not discard or sign any of these corrections.

## 5. Inert-face audit

On `F_14`, each size-five generator can be replaced by one size-four and
one size-one generator because `T_*=P+x`.  On `F_23`, it can be replaced
by one size-two and one size-three generator because `T_*=y+z`.  Capacity
and value are identical, so the size-five denomination is Bellman-inert on
those faces.  On overlaps with `F_A`, it remains inert; the theorem's
wording explicitly restricts genuine activity to the nonoverlap part of
`F_A`.

## 6. Logical direction of the final reduction

If all three face train bounds are positive, then the two lower bounds
above force every original table positive.  Conversely, if an original
table has `Phi<=0`, endpoint monotonicity gives

\[
\Phi(T_*)\le\Phi(T)\le0,
\]

while the train comparison gives

\[
\mathscr B_{T_*}\le\Phi(T_*).
\]

Hence its boundary face necessarily satisfies `mathscr B_(T_*)<=0`.
This verifies both directions claimed in Section 5.

## 7. Exact scope

The audited result is a sharp endpoint-level reduction.  It does **not**
establish the signs of `B_A`, `B_(P+x)`, or `B_(y+z)`, and therefore does
not close the five-slot size-four-efficient branch or the all-slot Bellman
inequality.
