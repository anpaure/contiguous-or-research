# Exact absorbed benefit--drift Pareto frontier at the scalar extremizer

## 1. The extremizer fails even after drift optimization

Let

\[
 4A^3+24A^2-216A+279=0,
 \qquad A=A_*=1.70817256009\ldots,
\]

and put

\[
                         N={3-A\over2}.
\]

This is the saturated bottom-threshold scalar candidate from the absorbed
benefit ledger.  Marginal stationarity requires the absorbed length drift
to be cancellable by the nonabsorbed mass:

\[
 \left|\int_{\rho_A}(s-p)\right|\le N.               \tag{1.1}
\]

The unconstrained pointwise maximizers already have drift at least

\[
 A-{A^2\over3}=0.7355547\ldots>N=0.6459137\ldots.
\]

The exact Pareto problem remains infeasible even after sacrificing absorbed
benefit optimally to enforce (1.1).

## 2. Exact drift-constrained fill

Define

\[
 r={(3-A)(2A-3)\over12A},
 \qquad
 u={2A^2+9A-9\over12A}.                              \tag{2.1}
\]

Then

\[
 u-r={A\over3},qquad A(1-r-u)=N.                    \tag{2.2}
\]

At `A=A_*`,

\[
 r=0.02623886209\ldots,qquad
 u=0.59562971545\ldots.
\]

The optimal absorbed successor-level distribution has total density
`3 dt` on `[r,u]`.  Its marked seams are

\[
 p=1+t,\qquad s=2-t,
\]

and

\[
 z=\begin{cases}0,&t\le1/3,\\1,&t\ge1/3.\end{cases} \tag{2.3}
\]

Its drift is exactly `N`.

A Lagrange dual proves optimality.  Put

\[
 q={(4A+3)(7A-9)\over24A^2}.
\]

For each `t`, maximize

\[
                         \Delta_A-q(s-p)              \tag{2.4}
\]

under the exact absorbed constraints

\[
 p\le1+t,quad s\le2-t,quad p,s\ge1,quad p+s+z\le4.
\]

Splitting according to the order of `p,s`, the sign of
`min(p,s)-4/3`, and the two sides of `t=1/3` gives (2.3).  The superlevel
set selected by the density cap is exactly `[r,u]`.  The resulting maximum
benefit is

\[
 V(A)=-{8A^5+36A^4+162A^3-1575A^2+324A+729
           \over864A^2}.                              \tag{2.5}
\]

At the cubic root,

\[
 V(A_*)=0.8262062041\ldots,
\]

while scalar survival needs

\[
 {4N\over3}={2(3-A_*)\over3}=0.8612182933\ldots.      \tag{2.6}
\]

The strict gap is

\[
 {2(3-A_*)\over3}-V(A_*)
 =-{118A_*^2-446A_*+411\over64A_*^2}
 =0.0350120891\ldots>0.                               \tag{2.7}
\]

The numerator sign follows from the two roots
`(223+-sqrt(1231))/118` and the location of `A_*` between them.  Thus the
saturated scalar candidate cannot satisfy the equal predecessor/successor
marginal law.

## 3. Why scalar drift still cannot seal every profile

The nested alternating-pair broad process remains a coherent scalar marked
counterexample to every constraint used above.  It has length measure

\[
                         2\,1_{[1,2]}(s)\,ds,
\]

absorbed reflected seams

\[
                         p=3-s,\quad z=0,\quad t=2-s,
\]

and contracted nonabsorbed seams

\[
                         p=s,\quad z=3-s.
\]

Its predecessor and successor marginals agree, its per-direction absorbed
level density is `2/3 dt<=dt`, and it respects threshold contraction and
gap addition.  Since every nonabsorbed seam has `z=3-s<c`, dangerous-list
self-closure does not strengthen its old saving: `phi_c^star=phi`.  Its
scalar value remains

\[
                         U(c)>4\qquad(1<c<2).          \tag{3.1}
\]

It fails only at the complete selected-line gate.  As `c` decreases to one,

\[
 f=2,qquad\ell=3,qquad\tau=1,qquad\iota\ge1/4,
\]

so line-union geometry would require

\[
 3\le2f-\tau-\iota\le{11\over4},                    \tag{3.2}
\]

a contradiction.

## 4. Scope

Length drift is the correct missing scalar constraint and eliminates the
last saturated one-threshold candidate.  It cannot finish the general
three-box no-go theorem.  Any final seal must use the full cross-direction
line-intersection/additive-triple measure, or an equivalent theorem coupling
line direction to word order across thresholds.
