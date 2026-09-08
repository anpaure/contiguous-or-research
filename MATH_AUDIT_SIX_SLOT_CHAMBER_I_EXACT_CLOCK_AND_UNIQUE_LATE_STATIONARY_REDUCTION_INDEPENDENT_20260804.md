# Independent audit: six-slot chamber-I exact clock and unique late-stationary reduction

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_SIX_SLOT_CHAMBER_I_EXACT_CLOCK_AND_UNIQUE_LATE_STATIONARY_REDUCTION_20260804.md`  
**Audited theorem SHA-256:**
`adcbced9bf28374e1df96466552dbe70704c720d4af81c2212978efd8e86895d`

**Verdict:** **PASS after proof-hygiene corrections.**  The exact clock,
the period-`2p` lower-bound direction, compact third-derivative sign,
endpoint/stationary classification, late-strip restriction, and `a=0`
closure are all correct.  The corrections made during this audit were:

1. closing several missing display delimiters;
2. separating a nontrivial closed fibre from the singleton equality case
   in the deduction `4a<A`;
3. replacing the false strict display `b<2a` by `b<=2a`;
4. spelling out why the `b=A-p` endpoint is literally an instance of the
   audited five-slot threshold theorem; and
5. binding `C(p)>0` to the actual all-ceiling theorem and audit rather
   than to the later four-slot scalar theorem which merely uses it.

None of these changes alters the reduction or closes one of its residual
gates.

## 1. Scope inherited from the three-chamber reduction

The object audited here is the retained-pulse lower gate
`mathcal G_I`, not the original arbitrary six-slot functional `Phi`.
The cited exact three-chamber theorem proves `Phi>=mathcal G_I` on
chamber I.  The present theorem correctly identifies `mathcal G_I` as
the exact Bellman functional of a particular auxiliary table and then
reduces the minimum of that exact gate.  It does not reverse the earlier
lower-bound direction.

The chamber conditions are

\[
 A/2\le p<A,\qquad 0\le a\le p/3,\qquad
 a\le b\le2a,\qquad p+b<A
\]

on the physical domain, with `p+b<=A` only for taking the closure.
Put `x=b-a`.  Then

\[
 0\le x\le a,\qquad b\le2a,\qquad p\ge3a.
\]

These are the only inequalities used below.

## 2. The displayed table is internally superadditive

For

\[
 (c_0,\ldots,c_6)=(0,x,b,p,p+a,p+b,2p),
\]

the nontrivial internal inequalities are consequences of

\[
 b\ge2x,\qquad p\ge2b-a,\qquad p\ge a+b,
\]

because

\[
 b\ge2x\iff b\le2a,
\]

and the other two right sides are at most `3a<=p`.  More explicitly,
`c_4>=c_1+c_3` is `a>=x`, `c_4>=2c_2` is
`p>=2b-a`, `c_6>=c_1+c_5` repeats `p>=2b-a`, and
`c_6>=c_2+c_4` is `p>=a+b`.  All remaining comparisons are equalities
or weaker consequences.

Also

\[
 c_5=c_2+c_3,\qquad c_6=2c_3,
\]

so the size-five and size-six displayed denominations are genuinely
inert in the max-plus recurrence.

## 3. Exact max-plus clock

Define the eventual envelope

\[
 U_{3q}=qp,\qquad U_{3q+1}=qp+a,\qquad
 U_{3q+2}=qp+2a.
\]

Each displayed denomination satisfies `c_j<=U_j`:
the only non-equalities are `x<=a`, `b<=2a`, and
`p+b<=p+2a`.  Moreover `U_i+U_j<=U_{i+j}`; when the two residues wrap
past three this is exactly `3a<=p`.  Hence every composition of capacity
`m` has value at most `U_m`.

The upper bound is attained by copies of `c_3=p`, with one copy of
`c_4=p+a` for residue one and two copies of `c_4` for residue two.
The latter construction is available from capacity eight onward.  Thus

\[
 V_{3q}=qp,\quad V_{3q+1}=qp+a,\quad V_{3q+2}=qp+2a
 \qquad(q\ge2),
\]

while direct recurrence gives

\[
 (V_0,\ldots,V_5)=(0,x,b,p,p+a,p+b).
\]

Comparing this head with the three residue trains gives exactly

\[
 \mathcal L_3(p;a,2a)
 +K(b-a)-K(a)+K(b)-K(2a)+K(p+b)-K(p+2a),
\]

so no availability pulse has been omitted.

## 4. The period-retaining lower bound has the correct direction

Superadditivity and `V_6=2p` give, for `0<=i<6`,

\[
 V_{6q+i}\ge qV_6+V_i=2qp+W_i.
\]

At `q=0` this is equality.  For `q>=1`, both arguments are at least
`2p>=A`.  The Rayleigh kernel is increasing on `[A,infinity)`, so

\[
 K(V_{6q+i})\ge K(2qp+W_i).
\]

Both Gaussian-tail series converge absolutely, making the termwise sum
legitimate.  This verifies the direction in (2.3); it is not the common
but invalid reversal caused by applying compact monotonicity in the tail.

The consecutive gaps of

\[
 0,x,b,p,p+a,p+b,2p
\]

are exactly

\[
 (x,a,p-b,a,x,p-b).
\]

They satisfy `0<=x<=a<=p-b`, and the compact pairs
`(0,p+b)`, `(x,p+a)`, `(b,p)` all sum to `p+b`.

## 5. Independent third-derivative check

On `0<=u<=1`, with `c=pi/4=A^2` and
`h(t)=t exp(-ct^2)`, direct differentiation gives

\[
 K'(Au)=2A\{h(1+u)-h(1-u)\}
\]

and, for `0<u<1`,

\[
 K'''(Au)={2\over A}
 \{h''(1+u)-h''(1-u)\}.
\]

For `0<u<=1/2`, the earlier compact lemma proves this difference is
strictly positive.  Its sign can also be checked directly: on
`[3/5,7/5]`,

\[
 h'''(t)=2ce^{-ct^2}(-4c^2t^4+12ct^2-3)>0,
\]

and on the remaining small endpoint strip the upper `h''` argument is
positive while the lower is negative.  For `1/2<=u<1`,
`1+u>=3/2>sqrt(6/pi)`, hence `h''(1+u)>0`, while
`0<1-u<=1/2` gives `h''(1-u)<0`.  Therefore

\[
 K'''(Au)>0\qquad(0<u<1).
\]

The point `u=1` is used only through a left derivative at a closed-fibre
endpoint; the interior argument always has `p+b<A`.

For a nontrivial closed fibre, `B(p,a)>a` implies `p+a<A`; together with
`p>=3a` this gives `4a<A`.  Hence every interior argument
`b-a`, `b`, and `p+b` is in the strict range needed above.  Thus

\[
 J'''_{p,a}(b)>0
\]

throughout the fibre interior, and `Sigma=J'` is strictly convex.
The possible equality `4a=A` forces `B=a`, so it has no interior to
analyze.

## 6. Endpoint and stationary classification

A strictly convex real function has at most two zeros.  If it has two,
its derivative is negative at the smaller and positive at the larger;
therefore at most the larger zero can satisfy `Xi=Sigma'>=0`.  If there
is only one zero, the same condition leaves at most that one.  Thus the
set `mathcal S_{p,a}` has cardinality at most one.

Every interior minimum of the original one-variable function has
`Sigma=0` and the necessary second-order condition `Xi>=0`; if `Xi=0`
admits a false-positive stationary candidate, retaining it only weakens
the reduction and is proof-safe.  Compactness then leaves exactly the
two endpoints and this at-most-one candidate.

Direct substitution gives

\[
 \mathcal G_I(p,a,a)
 =\mathcal L_3(p;a,2a)+K(0)-K(2a)+K(p+a)-K(p+2a)
\]

and

\[
 \mathcal G_I(p,a,2a)=\mathcal L_3(p;a,2a).
\]

If the upper endpoint is `b=A-p<2a` and `a<b`, the auxiliary five-slot
table

\[
 (0,b-a,b,p,p+a,p+b)
\]

is internally superadditive, has `p+a<A=p+b`, and satisfies all hypotheses
of the audited threshold-endpoint theorem.  Its Bellman functional is
exactly `mathcal G_I`, so this endpoint is positive.  If `b=a`, the two
fibre endpoints coincide and it remains the explicitly retained
`mathcal E_0` gate.  No threshold theorem is being applied across that
degeneracy.

## 7. The late-strip condition

The sign of `K'(Au)` is the sign of

\[
 f(u)=\log{1+u\over1-u}-\pi u
     =2\operatorname{arctanh}u-\pi u.
\]

Now `f(0)=0`, `f'(0)=2-pi<0`, `f'` is strictly increasing on `(0,1)`,
and `f(u)` tends to infinity as `u` tends to one.  It therefore has one
positive zero `theta`; since `f(1/2)=log3-pi/2<0`, one has
`theta>1/2`.  With `xi=A theta`,

\[
 K'(u)<0\ (0<u<\xi),\qquad K'(u)>0\ (\xi<u\le A).
\]

For `a>0`, the compact arguments obey

\[
 0\le b-a\le b\le2a<A/2<\xi.
\]

Thus the first term of `Sigma` is nonpositive and the second is strictly
negative.  If `p+b<=xi`, the third is also nonpositive, so `Sigma<0`.
Every stationary candidate therefore has

\[
 \xi<p+b<A.
\]

If the whole fibre satisfies `p+B<=xi`, the function is strictly
decreasing and its minimum is its upper endpoint.

## 8. Degenerate boundary and exact scope

If `a=0`, then `b=0` and all three pulses cancel.  Hence

\[
 \mathcal G_I(p,0,0)=3C(p).
\]

The audited all-ceiling theorem proves `C(p)>0` for every `p>0`, including
the whole present range `A/2<=p<A`.  This closes the degenerate boundary.

The theorem therefore leaves exactly:

1. `mathcal E_0(p,a)`;
2. `mathcal L_3(p;a,2a)` on `p+2a<=A`; and
3. at most one stationary value with
   `Sigma=0`, `Xi>=0`, and `xi<p+b<A`.

It does **not** prove any of those residual values positive, and therefore
does not close chamber I, the six-slot Bellman inequality, the all-grid
inequality, or an OR-word upper bound.

## 9. Dependency hashes used in this audit

| role | file | SHA-256 |
|---|---|---|
| exact chamber-I lower gate | `MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_EXACT_THREE_CHAMBER_GATE_20260804.md` | `a3a79b92148b1b4b415c7795473b70f50bd6d0b84f20f6899a3275f62af9b0dd` |
| independent exact-gate audit | `MATH_AUDIT_SIX_SLOT_THREE_EFFICIENT_EXACT_THREE_CHAMBER_GATE_INDEPENDENT_20260804.md` | `d6f89ab80a67b193e9ee6e5d31ccb82f906ec460ded4c382e13b1708c8d44a11` |
| compact derivative lemma | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_DELAYED_B_CONCAVITY_AND_PURE_LATTICE_GATE_20260804.md` | `b494371c790ed20f14e29bd4beba67b27aa30f7f5b1447e4ef8da4e74db8ea14` |
| independent derivative audit | `MATH_AUDIT_FIVE_SLOT_THREE_EFFICIENT_DELAYED_B_CONCAVITY_AND_PURE_LATTICE_GATE_INDEPENDENT_20260804.md` | `9eec90787605f06568446c353153503c51570c6dc218597181c09fafa160edaf` |
| threshold endpoint | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md` | `1e15d736592bce3103786fb965f62fe6f028436c0d35b763b195157a2cf3d0b6` |
| independent threshold audit | `MATH_AUDIT_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_INDEPENDENT_20260804.md` | `6d07121018046f26f4ab5377e37dd692efffa8389b9d939668e2f1a73ae14425` |
| all-ceiling positivity | `MATH_THEOREM_RAYLEIGH_CEILING_DOMINATION_AND_FINITE_MIR_CONE_NOGO_20260804.md` | `18a5d75526774673909d29a26d93710a1d56e9298c51d3a4cebaa8ebcd62baf3` |
| independent all-ceiling audit | `MATH_AUDIT_RAYLEIGH_CEILING_DOMINATION_AND_FINITE_MIR_CONE_NOGO_20260804.md` | `9f807a2a044469bed61c2943adf51b48f71ce594748cc8d3fb41ceea3394ac39` |

