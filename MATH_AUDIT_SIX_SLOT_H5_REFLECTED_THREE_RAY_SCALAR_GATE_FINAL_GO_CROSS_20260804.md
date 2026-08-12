# Final cross-audit: six-slot `h=5` reflected three-ray scalar gate

**Date:** 2026-08-04  
**Method:** independent symbolic reconstruction from the frozen endpoint-defect
coordinates, followed by literal replay of the period trains, the correlated
infimum, and the repeated-middle period split.  No search, solver, sampled
computation, or numerical optimization was used.

**Audited theorem:**
`MATH_THEOREM_SIX_SLOT_H5_REFLECTED_THREE_RAY_SCALAR_GATE_20260804.md`,
SHA256
`2f26836e6c46974153136e45247ae10c3f5ff44a8bd9f55d60e511b98d091aef`.

## 0. Verdict

**FINAL GO as an exact reduction theorem.**  The reflected coordinate
face-union, train identity, correlated sufficient gate, and face-`Z`
half-period identity are correct.  The theorem does not sign the remaining
scalar envelope and therefore does not claim complete `h=5` positivity.

There is one harmless terminology point: the max-equals-`delta` locus is a
compact union of three polyhedral faces and need not itself be a convex
polytope.  The proof uses only compactness and the full correlated face
union, never convexity.

## 1. Coordinate and density replay

Write `tau=A+delta` and set

\[
(u,x,y,v,m)=(A-c_5,c_1,c_2,A-c_4,A-c_3).
\]

Since `c_5=5a`, the inverse relation is

\[
a={A-u\over5},
\qquad
(c_1,c_2,c_3,c_4,c_5)=(x,y,A-m,A-v,A-u).
\]

The endpoint density row `tau<=6a` becomes

\[
6u+5\delta\le A,
\]

and hence `0<=u<=(A-5delta)/6`.  The size-two, size-three, and size-four
density rows become respectively

\[
y\le {2(A-u)\over5},
\qquad
m\ge {2A+3u\over5},
\qquad
v\ge {A+4u\over5}.
\]

Endpoint superadditivity gives `x<=u+delta`; combining it with the first
row yields

\[
x\le u+\delta\le {A-u\over5}=a,
\]

so the size-one density constraint is not missing.

## 2. Internal rows and box constraints

Substitution in the six internal superadditivity inequalities gives exactly

\[
\begin{gathered}
y\ge2x,
\qquad m\le A-x-y,
\qquad m\ge x+v,\\
v\le A-2y,
\qquad v\ge x+u,
\qquad m\ge y+u.
\end{gathered}
\]

No box row is lost.  Indeed `m<=A-x-y<=A` and `v<=A-2y<=A`, while the
density lower bounds make `m,v` nonnegative.  Together with the explicit
nonnegative `u,x,y`, all arguments subsequently supplied to `D_delta` and
`Theta` lie in `[0,A]`.

The endpoint deficits are literally

\[
\begin{aligned}
\tau-(c_1+c_5)&=\delta-(x-u),\\
\tau-(c_2+c_4)&=\delta-(y-v),\\
\tau-2c_3&=\delta-(A-2m).
\end{aligned}
\]

Thus endpoint superadditivity gives the three weak inequalities and
endpoint saturation gives

\[
\max\{x-u,y-v,A-2m\}=\delta.
\]

Conversely these rows reconstruct every density, internal, and endpoint
row of the frozen defect formulation.  Replacing the strict
least-minimizer/first-crossing rows by weak rows produces precisely the
claimed compact face-union.

## 3. Period-gain sign and exact train identity

For `0<=w<=A`, the `q=0` terms in

\[
D_\delta(w)=F_{A+\delta}(w)-F_A(w)
\]

cancel.  For every `q>=1`, both arguments lie in `[A,infinity)`, where the
Rayleigh signed-tail kernel is increasing, and

\[
q(A+\delta)+w\ge qA+w.
\]

Hence `D_delta(w)>=0` on the entire domain used by the theorem.

For any reflected pair `(p,A-q)`, direct expansion gives

\[
\begin{aligned}
F_{A+\delta}(p)+F_{A+\delta}(A-q)
={}&F(p)-F(q)+D_\delta(p)+D_\delta(A-q)\\
&+F(q)+F(A-q)\\
={}&G_\delta(p,q)+\Theta(q).
\end{aligned}
\]

Using `(p,q)=(x,u)` and `(y,v)` accounts for the four paired shifts
exactly once.  The fifth shift obeys

\[
F_{A+\delta}(A-m)
=D_\delta(A-m)+F(A-m)
=M_\delta(m)+\Theta(m).
\]

Finally `C(A+delta)=C+D_delta(0)`.  Adding these identities reproduces
the complete right-hand side of the endpoint-period comparison; no train
term is dropped or duplicated.

## 4. Correlated scalar gate

The frozen endpoint theorem gives `Phi>=mathscr E_5`.  The exact Jacobi
identity supplies the three strict lower bounds

\[
\Theta(u),\Theta(v),\Theta(m)>-\varepsilon.
\]

The remaining three-ray expression is bounded below by its infimum over
the single compact physical face-union.  Therefore

\[
\Phi>C+D_\delta(0)+\Gamma_5(\delta)-3\varepsilon.
\]

The direction is correct and strict.  In particular, the proof does not
replace the joint domain by three independent marginal minima; all internal
rows and the condition that at least one endpoint deficit vanishes remain
active in `Gamma_5`.

## 5. Face-`Z` collapse

On face `Z`,

\[
m={A-\delta\over2},
\qquad
c_3=A-m={A+\delta\over2}={\tau\over2}.
\]

Absolute convergence permits the half-period ceiling to be split into its
even and odd index classes:

\[
\begin{aligned}
C(\tau/2)
&=\sum_{n\ge0}K(n\tau/2)\\
&=\sum_{q\ge0}K(q\tau)
 +\sum_{q\ge0}K(q\tau+\tau/2)\\
&=C(\tau)+F_\tau(\tau/2).
\end{aligned}
\]

This is the stated exact interlacing identity and gives the four remaining
shift terms in (4.3) with no residual midpoint or ceiling charge.

## 6. Dependencies and scope

All three dependency hashes in the theorem match their current files.
They support exactly the endpoint-period comparison, period-gain/reflection
algebra, and Jacobi theta bound used here.

The audited implication is only

\[
\text{physical inert `h=5` table}
\Longrightarrow
\Phi>C+D_\delta(0)+\Gamma_5(\delta)-3\varepsilon.
\]

Neither this audit nor the theorem signs `Gamma_5`, proves any inert face
positive, establishes complete six-slot positivity, or makes an OR-word
claim.
