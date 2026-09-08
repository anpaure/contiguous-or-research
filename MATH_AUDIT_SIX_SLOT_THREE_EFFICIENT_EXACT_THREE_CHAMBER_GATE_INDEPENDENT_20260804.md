# Independent audit: six-slot size-three exact three-chamber gate

**Date:** 2026-08-04  
**Status:** **GO**.  The theorem is a correct proof-safe reduction of the
normalized six-slot `h=3` branch to the three displayed scalar gates.  This
audit checks the parameter domain, the chamber partition, every
availability pulse, every monotonicity direction, and both wall identities.
It does not assert that any of the three residual gates is positive.

## 1. Frozen inputs

| role | file | SHA-256 |
|---|---|---|
| audited theorem | `MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_EXACT_THREE_CHAMBER_GATE_20260804.md` | `a3a79b92148b1b4b415c7795473b70f50bd6d0b84f20f6899a3275f62af9b0dd` |
| canonical six-slot normal form | `MATH_THEOREM_SIX_SLOT_CANONICAL_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md` | `3b537980a6f18aae936979335cc6756079ff10b92a80019acf3a97df8be9bede` |
| compact monotonicity through `3A/4` | `MATH_THEOREM_FIVE_SLOT_TWO_EFFICIENT_SMALL_PERIOD_WEDGE_CLOSURE_20260804.md` | `a678fc5a33c6457d9d640aa963d902fdb8c7ed932ade6a14fd320caf8d285e43` |

All hashes were recomputed from the local files before this audit was
written.

## 2. Rebinding the canonical domain

Write

\[
 p=c_3,\qquad a=c_4-p,\qquad b=c_5-p.
\]

The canonical theorem gives

\[
 c_6=2p,\qquad A/2\le p<A,
\]

and

\[
 c_1\le a\le p/3,\qquad c_2\le b\le2p/3,
 \qquad a,b<A-p.
\]

The extra projected inequality `a<=b` in the audited theorem is valid:
superadditivity at capacities `1+4=5` gives

\[
 p+b=c_5\ge c_1+c_4=c_1+p+a,
\]

so in fact

\[
                         c_1\le b-a.
\tag{2.1}
\]

Likewise, superadditivity at `2+3=5` gives `c_2<=b`.  Thus no
parameter was lost when the theorem projected to `(p,a,b)`.

## 3. Exhaustive chamber partition

The two maxima are

\[
 s_1=\max(a,2b-p),\qquad s_2=\max(b,2a).
\]

Their walls are

\[
 b={p+a\over2},\qquad b=2a.
\]

Since `3a<=p`,

\[
                         2a\le{p+a\over2}.
\]

Together with `b>=a`, this gives exactly the three closed chambers

\[
 [a,2a],\qquad[2a,(p+a)/2],\qquad[(p+a)/2,A-p),
\]

intersected, throughout, with the remaining canonical constraint
`b<=2p/3`.  Empty intersections cause no problem.  Direct substitution
gives respectively

\[
 (s_1,s_2)=(a,2a),\quad(a,b),\quad(2b-p,b).
\]

Hence the partition is exhaustive and has no reversed or missing wall.

## 4. Chamber I pulse audit

Here `b<=2a`.  The size-four pulse is identically zero.  For the
capacity-seven maximum,

\[
 p+b+c_2\le p+2b\le p+4a\le2p+a,
\]

where the last inequality is `3a<=p`.  Therefore

\[
 V_7=2p+a=2p+s_1,
\]

so that pulse is also exactly zero.

Equation (2.1) and `c_2<=b` give

\[
 c_1\le b-a\le a,
 \qquad c_2\le b\le2a.
\]

Moreover `2a<=2p/3<2A/3<3A/4`.  The cited compact lemma proves that
`K` is decreasing on `[0,3A/4]`; consequently

\[
 K(c_1)-K(a)\ge K(b-a)-K(a),
\]

and

\[
 K(c_2)-K(2a)\ge K(b)-K(2a).
\]

The size-five pulse is not assigned a sign and is retained literally as
`K(p+b)-K(p+2a)`.  These are exactly the three replacements used to
obtain `G_I`; every inequality points in the lower-bound direction.

## 5. Chamber II pulse audit

Here `(s_1,s_2)=(a,b)`, so both the size-four and size-five pulses
cancel exactly.  Also

\[
 p+b+c_2\le p+2b\le2p+a,
\]

and therefore `V_7=2p+a=2p+s_1`; the capacity-seven pulse cancels.

Finally

\[
 0\le c_1\le a<A-p\le A/2,
 \qquad
 0\le c_2\le b<A-p\le A/2.
\]

Compact monotonicity therefore gives

\[
 K(c_1)-K(a)\ge0,
 \qquad K(c_2)-K(b)\ge0.
\]

Dropping only these nonnegative pulses leaves precisely
`L_3(p;a,b)`.  The claimed ordered-gap inequalities are equivalent to

\[
 b\ge2a,
 \qquad 2b\le p+a,
\]

which are exactly the chamber walls.

## 6. Chamber III pulse and tail audit

The wall ordering implies `b>=2a`, while
`b>=(p+a)/2` gives `2b-p>=a>=0`.  Hence

\[
 (s_1,s_2)=(2b-p,b).
\]

The canonical upper bound `b<A-p` and `p>=A/2` give

\[
 2b-p<2A-3p\le A/2.
\]

Thus

\[
 0\le c_1\le a\le2b-p<A/2,
 \qquad0\le c_2\le b<A/2,
\]

so the size-one and size-two pulses are nonnegative and may be dropped.
The size-five pulse cancels exactly.  The size-four pulse is exactly

\[
 K(p+a)-K(p+s_1)=K(p+a)-K(2b).
\]

For the last pulse,

\[
 2p+a\le p+2b,
 \qquad p+b+c_2\le p+2b,
\]

and therefore

\[
 2p+a\le V_7\le p+2b.
\]

Both endpoints are at least `A`, since `2p+a>=A`.  On `[A,infinity)`,

\[
 K(x)=-e^{-(A+x)^2}
\]

is strictly increasing.  Hence the proof-safe direction is

\[
 K(V_7)-K(p+2b)
 \ge K(2p+a)-K(p+2b),
\]

exactly as stated.  No compact monotonicity is incorrectly extended into
the tail, and no adverse pulse is discarded.

## 7. Wall continuity

At `b=2a`, all three finite differences in `G_I` vanish:

\[
 K(b-a)-K(a)=K(b)-K(2a)=K(p+b)-K(p+2a)=0.
\]

Thus `G_I=G_II=L_3(p;a,2a)`.

At `b=(p+a)/2`, one has `2b-p=a`, `2b=p+a`, and
`p+2b=2p+a`.  Both retained differences in `G_III` vanish and its
lattice is `L_3(p;a,b)`.  Thus `G_II=G_III` on the second wall.

## 8. Verdict and exact scope

**GO.**  The three chambers exhaust the canonical projected domain; all
five availability pulses are either cancelled exactly, bounded in the
correct direction on an authenticated monotonicity interval, or retained
explicitly.  The tail comparison in chamber III has the correct direction,
and the gates glue continuously on both walls.

The theorem remains only a reduction.  This audit proves neither
`G_I>0`, `G_II>0`, nor `G_III>0`.
