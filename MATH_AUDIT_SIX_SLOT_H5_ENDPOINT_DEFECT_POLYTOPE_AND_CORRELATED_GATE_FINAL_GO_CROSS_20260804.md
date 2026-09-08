# Final cross-audit: six-slot `h=5` endpoint-defect correlated reduction

**Date:** 2026-08-04  
**Method:** independent symbolic replay of the density-defect coordinate
change, all physical-polytope constraints, endpoint saturation, the literal
endpoint-period train, the compact-closure quantifiers, and the threshold
margin.  No search, solver, sampled computation, or numerical optimization
was used.

**Audited theorem:**
`MATH_THEOREM_SIX_SLOT_H5_ENDPOINT_DEFECT_POLYTOPE_AND_CORRELATED_GATE_20260804.md`,
SHA256
`4a751598067165d88cd1e01e0406c3dce09c941cbba7fa0dd95487d0ff3e4b59`.

## 0. Verdict

**FINAL GO as a reduction theorem.**  The variable transformation is exact,
the weak compact polytope contains every literal physical `h=5` point, the
minimum-zero condition is precisely endpoint saturation on the inert side,
and the two-pair/one-midpoint train is the literal six-residue endpoint
train.  The comparison and infimum directions are correct.  The threshold
face has the stated strict margin.  The theorem does not sign the inert gate
and correctly makes no complete `h=5` positivity claim.

## 1. Coordinate transformation and density bounds

Write `P=c_5=5a` and define

\[
 q_1=6a-\tau,\qquad r=a-c_1,\qquad q_j=ja-c_j
 \quad(j=2,3,4).
\]

The inverse transformation is literal:

\[
 c_1=a-r,\qquad c_2=2a-q_2,\qquad c_3=3a-q_3,
 \qquad c_4=4a-q_4,\qquad c_5=5a,\qquad c_6=\tau=6a-q_1.
\]

Maximum density at size five gives `c_j<=ja` and `tau<=6a`, hence
nonnegative defects and `a>=tau/6`.  Nonnegativity of the entries gives

\[
 r\le a,\qquad q_2\le2a,\qquad q_3\le3a,\qquad q_4\le4a.
\]

Internal superadditivity gives `c_1<=c_2/2<=a`, so `r>=0`.
Endpoint superadditivity gives `tau>=c_1+c_5>=c_5=5a`, and therefore

\[
 q_1=6a-\tau\le a.
\]

Thus the displayed `q_1<=a` is exactly the otherwise implicit constraint
`a<=tau/5`; it is not missing from the polytope.  First crossing gives
`5a<A`.  Combining these facts yields

\[
 A<\tau<{6A\over5},qquad {\tau\over6}\le a<{A\over5}
\]

on the literal inert stratum.

Least-maximizer assignment makes `q_2,q_3,q_4` strictly positive.  The
inequality `q_2<=2r` then makes `r>0`.  Allowing these strict quantities to
vanish and replacing `a<A/5` by `a<=A/5` is therefore a genuine closure
enlargement, not an asserted physical equivalence at the new boundary.

## 2. Internal physical polytope

Substitution into the four nontrivial internal rows gives

\[
\begin{array}{rcl}
c_2\ge2c_1&\Longleftrightarrow&q_2\le2r,\\
c_3\ge c_1+c_2&\Longleftrightarrow&q_3\le r+q_2,\\
c_4\ge c_1+c_3&\Longleftrightarrow&q_4\le r+q_3,\\
c_4\ge2c_2&\Longleftrightarrow&q_4\le2q_2.
\end{array}
\]

The remaining capacity-five inequalities reduce exactly to

\[
 c_5-(c_1+c_4)=r+q_4\ge0,
 \qquad
 c_5-(c_2+c_3)=q_2+q_3\ge0.
\]

There is no omitted internal row.  Nondecreasing order also follows from
these superadditive rows and `c_1>=0`, so no separate ordering inequality is
lost in the coordinate description.

## 3. Endpoint defects and the minimum-zero boundary

Define

\[
 \alpha=r-q_1,qquad
 \beta=q_2+q_4-q_1,qquad
 \gamma=2q_3-q_1.
\]

Direct expansion gives

\[
\begin{aligned}
\tau-(c_1+c_5)&=\alpha,\\
\tau-(c_2+c_4)&=\beta,\\
\tau-2c_3&=\gamma.
\end{aligned}
\]

Hence endpoint superadditivity is exactly
`alpha,beta,gamma>=0`.  On the inert range `tau>A`, endpoint saturation

\[
 \tau=\max\{A,c_1+c_5,c_2+c_4,2c_3\}
\]

holds if and only if at least one displayed deficit is zero.  Therefore

\[
 \alpha,\beta,\gamma\ge0,qquad
 \min\{\alpha,\beta,\gamma\}=0
\]

is both necessary and sufficient, including all pairwise and triple face
intersections.  The three zero faces give respectively the literal endpoint
configurations `(1,5)`, `(2,4)`, and `(3,3)`.

## 4. Exact correlated train identity

For `J_tau(s,d)=F_tau(s)+F_tau(tau-d-s)`, the first pair satisfies

\[
 \tau-\alpha-(a-r)
 =(6a-q_1)-(r-q_1)-(a-r)=5a=c_5.
\]

The second pair similarly satisfies

\[
 \tau-\beta-(2a-q_2)=4a-q_4=c_4,
\]

and

\[
                         {\tau-\gamma\over2}=3a-q_3=c_3.
\]

Consequently

\[
 C(\tau)+J_\tau(a-r,\alpha)
 +J_\tau(2a-q_2,\beta)
 +F_\tau((\tau-\gamma)/2)
\]

is exactly

\[
                         C(\tau)+\sum_{j=1}^{5}F_\tau(c_j).
\]

No pair has been minimized independently and no residue train is missing.

## 5. Literal Bellman comparison

At capacity `6q+j`, `q` endpoint configurations together with the
size-`j` generator have value `q tau+c_j`.  At `q=0`, internal
superadditivity makes the displayed generator optimal, so `V_j=c_j`.
For `q>=1`, the candidate is at least `tau>A`; the Bellman optimum is no
smaller, and `K` is increasing on `[A,infinity)`.  Therefore

\[
                         K(V_{6q+j})\ge K(q\tau+c_j).
\]

Summing the six residue classes and all `q>=0` proves

\[
                         \Phi\ge\mathscr E_5.
\]

On each inert face the endpoint configuration is genuinely available from
the corresponding equality `(1,5)`, `(2,4)`, or `(3,3)`.  Thus this
comparison remains literal in the delayed five-generator interpretation
and does not use a fictitious capacity-six symbol or an availability-head
correction.

## 6. Compact closure and quantifiers

Fix `A<tau<6A/5`.  The set `overline P_5(tau)` is defined by finitely
many weak polynomial inequalities and the finite union of the three closed
zero-defect faces.  It is bounded by the displayed coordinate boxes and is
therefore compact.  It is also nonempty: take

\[
 a={\tau\over6},qquad r=q_2=q_3=q_4=0,
\]

which gives `q_1=alpha=beta=gamma=0` and satisfies every weak inequality.

Every physical point maps into this closure.  The train expression is
continuous there, so the infimum is finite and attained.  For a physical
table,

\[
 \Phi\ge\mathscr E_5
 \ge\inf_{\overline{\mathcal P}_5(\tau)}\mathscr E_5
 =\mathfrak R_5(\tau).
\]

Thus pointwise positivity of `mathfrak R_5(tau)` is sufficient.  Conversely,
if `Phi<=0`, then `mathscr E_5<=Phi<=0`, whence
`mathfrak R_5(tau)<=0`.  A nonpositive closure point need not reconstruct a
physical table, exactly as the theorem states.

## 7. Threshold face

At `tau=A`, endpoint superadditivity gives

\[
 c_1+c_5\le A,qquad c_2+c_4\le A,qquad 2c_3\le A.
\]

The table is nondecreasing, so the frozen subcomplementary-pair theorem
applies to the first two pairs, and the half-band theorem gives
`F_A(c_3)>0`.  Together with `C(A)>43/1000`,

\[
\begin{aligned}
\Phi
 &>{43\over1000}-2{8541\over420000}\\
 &={18060-17082\over420000}
 ={978\over420000}={163\over70000}>0.
\end{aligned}
\]

This argument indeed needs no maximum-density assumption.

## 8. Scope and frozen dependencies

The theorem proves an exact physical-coordinate reduction and a sufficient
closed correlated gate.  It signs only the threshold face `tau=A`; it does
not sign the inert gate, close the complete `h=5` branch, extend to larger
generator tables, or prove an OR-word bound.

All three direct dependencies exist at exactly their declared SHA256 values:

| role | SHA256 |
|---|---|
| canonical six-slot/least-density branch | `3b537980a6f18aae936979335cc6756079ff10b92a80019acf3a97df8be9bede` |
| thirteen-form `h=5` reduction | `b6a98dbf45f239f68f934ac0c14318ff8f5faa6b69d78cbad7796b46ee283024` |
| endpoint threshold closure | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |

The audited theorem remains unchanged at SHA256
`4a751598067165d88cd1e01e0406c3dce09c941cbba7fa0dd95487d0ff3e4b59`.
