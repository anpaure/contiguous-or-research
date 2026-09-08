# Self-audit: six-slot `h=5` endpoint-defect polytope and correlated gate

**Date:** 2026-08-04  
**Audit status:** **GO**, with the compact-closure qualification stated
explicitly in the theorem.  This is a pure symbolic audit.  It does not
sign the resulting gate or claim complete six-slot positivity.

## 1. Object audited

The target is

`MATH_THEOREM_SIX_SLOT_H5_ENDPOINT_DEFECT_POLYTOPE_AND_CORRELATED_GATE_20260804.md`.

Its audited SHA-256 is
`4a751598067165d88cd1e01e0406c3dce09c941cbba7fa0dd95487d0ff3e4b59`.

Its claim is a reduction of the canonical inert `h=5` branch, not an
analytic positivity theorem.  The threshold face is separately closed in
Lemma 0.1.

## 2. Threshold-face arithmetic

For `tau=A`, the literal period-six comparison is

\[
 \Phi\ge C(A)+\sum_{i=1}^{5}F_A(c_i).
\]

Endpoint superadditivity supplies the two subcomplementary pairs
`(c_1,c_5)` and `(c_2,c_4)`, and `2c_3<=A`.  The frozen train estimates
therefore give

\[
 {43\over1000}-2{8541\over420000}
 ={18060-17082\over420000}
 ={978\over420000}
 ={163\over70000}>0.
\]

This calculation uses no maximum-density hypothesis, so it applies to the
`h=5` threshold face exactly as stated.

## 3. Coordinate bijection and ranges

At fixed `tau`, the change of variables is invertible:

\[
\begin{aligned}
 a&=c_5/5, & q_1&=6a-\tau,\\
 c_1&=a-r, & c_2&=2a-q_2,\\
 c_3&=3a-q_3, & c_4&=4a-q_4.
\end{aligned}
\]

The range checks are:

* maximum density gives `tau<=6a` and `c_j<=ja` for `j=2,3,4`;
* `c_2>=2c_1` gives `c_1<=a`;
* first crossing gives `5a=c_5<A`;
* endpoint superadditivity gives `tau>=c_5=5a`.

Hence

\[
 A<\tau<{6A\over5},
 \qquad {\tau\over6}\le a<{A\over5},
 \qquad 0\le q_1\le a,
\]

with the other coordinate bounds exactly equivalent to nonnegativity and
the density ceilings.  Least-maximizer assignment makes
`q_2,q_3,q_4>0`; the inequality `q_2<=2r` then makes `r>0`.

## 4. Complete internal-superadditivity ledger

The complete internal rows through capacity five are

\[
\begin{array}{c|c}
\text{original row}&\text{defect form}\\ \hline
c_2\ge2c_1&q_2\le2r\\
c_3\ge c_1+c_2&q_3\le r+q_2\\
c_4\ge c_1+c_3&q_4\le r+q_3\\
c_4\ge2c_2&q_4\le2q_2\\
c_5\ge c_1+c_4&r+q_4\ge0\\
c_5\ge c_2+c_3&q_2+q_3\ge0.
\end{array}
\]

Thus the four displayed nontrivial inequalities plus coordinate
nonnegativity are both necessary and sufficient.  No internal row has
been omitted.

## 5. Endpoint ledger

Direct substitution gives

\[
\begin{aligned}
 \tau-(c_1+c_5)&=r-q_1=\alpha,\\
 \tau-(c_2+c_4)&=q_2+q_4-q_1=\beta,\\
 \tau-2c_3&=2q_3-q_1=\gamma.
\end{aligned}
\]

On the inert region `tau>A`, endpoint saturation is therefore exactly

\[
 \alpha,\beta,\gamma\ge0,
 \qquad \min\{\alpha,\beta,\gamma\}=0.
\]

This verifies both necessity and sufficiency, including intersections of
the three faces.

## 6. Shift decomposition

The complementary identities are exact:

\[
 c_1+c_5=\tau-\alpha,
 \qquad c_2+c_4=\tau-\beta,
 \qquad c_3={\tau-\gamma\over2}.
\]

Consequently

\[
 C(\tau)+\sum_{j=1}^{5}F_\tau(c_j)
 =C(\tau)
  +J_\tau(a-r,\alpha)
  +J_\tau(2a-q_2,\beta)
  +F_\tau\left({\tau-\gamma\over2}\right).
\]

This confirms that the `h=5` object is two deficient complementary pairs
plus one deficient midpoint.  Treating the three defects independently
would discard the endpoint-minimum condition and the four internal
couplings, so the `h=4` rectangle cannot be imported.

## 7. Literal Bellman comparison

For capacity `6q+j`, the configuration consisting of `q` endpoint
blocks and the size-`j` block has value `q tau+c_j`.  At `q=0`, internal
superadditivity gives `V_j=c_j`.  At `q>=1`, both arguments are at least
`tau>A`, and the kernel is increasing there.  Therefore

\[
 K(V_{6q+j})\ge K(q\tau+c_j).
\]

Summing over `q>=0` and `0<=j<=5` gives the claimed literal comparison.
There is no finite-head or availability correction.

## 8. Compact-closure qualification

The literal physical stratum has the strict conditions
`a<A/5` and `r,q_2,q_3,q_4>0`.  It is not compact.  The theorem correctly
defines the gate on the closed enlargement obtained by replacing these
with weak inequalities.  For fixed `tau`, that enlargement is closed and
bounded, hence compact, and every physical table maps into it.

Therefore positivity of the closed gate is sufficient for physical
positivity.  A nonpositive physical table forces the gate to be
nonpositive.  The converse is intentionally not claimed because a
nonpositive minimizer could lie on an adjacent-stratum boundary.

At fixed `tau`, the affine coordinates have five scalar degrees.  On any
one endpoint face, one affine equality is imposed, leaving a generically
four-dimensional correlated optimization.  No unproved independent
pair minimization is used.

## 9. Dependency hashes checked

| role | SHA-256 |
|---|---|
| canonical six-slot theorem | `3b537980a6f18aae936979335cc6756079ff10b92a80019acf3a97df8be9bede` |
| thirteen-form `h=5` theorem | `b6a98dbf45f239f68f934ac0c14318ff8f5faa6b69d78cbad7796b46ee283024` |
| endpoint/subcomplementary closure | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |

## 10. Verdict

**GO** for the stated reduction:

\[
 \text{physical inert `h=5` table}
 \Longrightarrow
 \Phi\ge\mathfrak R_5(\tau).
\]

The audit does **not** establish
\(\mathfrak R_5(\tau)>0\), complete `h=5` positivity, complete six-slot
positivity, an all-grid Bellman theorem, or an OR-word result.
