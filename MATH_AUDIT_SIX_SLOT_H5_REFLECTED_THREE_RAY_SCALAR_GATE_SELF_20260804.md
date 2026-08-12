# Self-audit: six-slot `h=5` reflected three-ray scalar gate

**Date:** 2026-08-04  
**Verdict:** **SELF-AUDIT GO as a reduction theorem.**  The scalar gate is
not signed, so this audit does not claim complete `h=5` positivity.

## 1. Target

The audited target is

`MATH_THEOREM_SIX_SLOT_H5_REFLECTED_THREE_RAY_SCALAR_GATE_20260804.md`.

Its audited SHA-256 is
`2f26836e6c46974153136e45247ae10c3f5ff44a8bd9f55d60e511b98d091aef`.

The theorem is intended to be an exact change of coordinates plus a
sufficient reflected lower gate.  It does not replace the remaining
analytic minimization by an assertion.

## 2. Coordinate reconstruction

From

\[
 (u,x,y,v,m)=(A-c_5,c_1,c_2,A-c_4,A-c_3)
\]

the inverse map is

\[
 (c_1,c_2,c_3,c_4,c_5)=(x,y,A-m,A-v,A-u).
\]

Since `c_5=5a`, one has `a=(A-u)/5`.  Maximum density at size five gives

\[
 A+\delta\le {6(A-u)\over5},
 \quad
 y\le {2(A-u)\over5},
 \quad
 A-m\le {3(A-u)\over5},
 \quad
 A-v\le {4(A-u)\over5}.
\]

These are exactly (1.3)--(1.4).  Endpoint superadditivity gives
`x<=u+delta`; together with `6u+5delta<=A`,

\[
 x\le u+\delta\le {A-u\over5}=a,
\]

so the size-one density row is present.

The six internal rows replay as

\[
\begin{array}{rcl}
c_2\ge2c_1&\Longleftrightarrow&y\ge2x,\\
c_3\ge c_1+c_2&\Longleftrightarrow&m\le A-x-y,\\
c_4\ge c_1+c_3&\Longleftrightarrow&m\ge x+v,\\
c_4\ge2c_2&\Longleftrightarrow&v\le A-2y,\\
c_5\ge c_1+c_4&\Longleftrightarrow&v\ge x+u,\\
c_5\ge c_2+c_3&\Longleftrightarrow&m\ge y+u.
\end{array}
\]

The upper bounds `v<=A` and `m<=A` follow from the third and second rows,
respectively; their lower density bounds make them nonnegative.  Hence
`c_3,c_4` are nonnegative without a missing box constraint.

## 3. Endpoint replay

The endpoint deficits are

\[
\begin{aligned}
 (A+\delta)-(c_1+c_5)&=\delta-(x-u),\\
 (A+\delta)-(c_2+c_4)&=\delta-(y-v),\\
 (A+\delta)-2c_3&=\delta-(A-2m).
\end{aligned}
\]

Their nonnegativity gives the three weak inequalities in (1.6), while
endpoint saturation on `delta>0` makes at least one an equality.  Thus

\[
 \max\{x-u,y-v,A-2m\}=\delta
\]

is exact, including tied faces.  The face labels `X,Y,Z` are correct.

Conversely, all nonnegativity, density, internal superadditivity, and
endpoint rows reconstruct from (1.3)--(1.6).  The weak polytope is closed
and bounded.  It contains the literal physical stratum and only adds its
least-maximizer/first-crossing boundary.

## 4. Period-gain sign

For `0<=w<=A`, the `q=0` terms in

\[
 D_\delta(w)=F_{A+\delta}(w)-F_A(w)
\]

cancel.  Every `q>=1` argument lies on `[A,infinity)`, where `K` is
increasing, and

\[
 q(A+\delta)+w\ge qA+w.
\]

Therefore `D_delta(w)>=0` in the full range used by the theorem.

## 5. Reflection identity

For a pair `(p,A-q)`, direct expansion gives

\[
\begin{aligned}
F_{A+\delta}(p)+F_{A+\delta}(A-q)
={}&F(p)-F(q)\\
&+D_\delta(p)+D_\delta(A-q)+\Theta(q),
\end{aligned}
\]

which is exactly `G_delta(p,q)+Theta(q)`.  Applying this to `(x,u)` and
`(y,v)` prices all four paired shifts once.

For the remaining shift,

\[
 F_{A+\delta}(A-m)
 =D_\delta(A-m)+F(A-m)
 =M_\delta(m)+\Theta(m).
\]

Finally `C(A+delta)=C+D_delta(0)`.  Thus the displayed decomposition is
the literal six-residue endpoint train, not a lower relaxation.

## 6. Infimum and theta directions

The endpoint comparison gives \(\Phi\ge\mathscr E_5\).  Each theta term obeys
the strict lower bound `Theta> -epsilon`, while the correlated physical
part is at least its single-polytope infimum.  Therefore

\[
 \Phi>C+D_\delta(0)+\Gamma_5(\delta)-3\varepsilon.
\]

The strict direction is correct.  No separate infimum is taken for the
two pairs or the midpoint, so the max-equals-`delta` endpoint correlation
and every internal row survive.

## 7. Face-`Z` interlacing

On face `Z`,

\[
 m={A-\delta\over2},
 \qquad c_3={A+\delta\over2}={\tau\over2}.
\]

Splitting the half-period ceiling into even and odd indices gives the
literal identity

\[
\begin{aligned}
C(\tau/2)
&=\sum_{q\ge0}K(q\tau)
 +\sum_{q\ge0}K(q\tau+\tau/2)\\
&=C(\tau)+F_\tau(\tau/2).
\end{aligned}
\]

Hence (4.3) deletes neither a ceiling term nor a midpoint term; it
interlaces them exactly.

## 8. Scope verdict

**GO** for the implication

\[
 \text{physical inert `h=5` table}
 \Longrightarrow
 \Phi>C+D_\delta(0)+\Gamma_5(\delta)-3\varepsilon
\]

and for the exact face-`Z` identity.  This audit does not establish
\(\Gamma_5>0\), close an inert endpoint face, prove complete six-slot
positivity, or prove an OR-word theorem.
