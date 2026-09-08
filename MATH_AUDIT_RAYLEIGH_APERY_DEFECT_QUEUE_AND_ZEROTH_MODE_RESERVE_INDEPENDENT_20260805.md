# Independent audit: Rayleigh Apéry defect queue and zeroth-mode reserve

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_APERY_DEFECT_QUEUE_AND_ZEROTH_MODE_RESERVE_20260805.md`  
**Verdict:** **INDEPENDENT GO after one proof-safe premise clarification.**
The period cap, shortest-path normalizations, cyclic half-average estimate,
counting-queue formula, signed phase identity, shoulder-area inequality, and
total-defect spreading all replay exactly.  The clarification makes
nonnegativity of the original Bellman table explicit and records the
resulting `0<=s_r<=r lambda<P` fact used by the same-period-block argument.
No conclusion is enlarged.  The theorem remains a reduction, not an
all-price proof.

The audit also supplies a new exact calibration theorem:
`MATH_THEOREM_RAYLEIGH_ENDPOINT_ONLY_APERY_QUEUE_EXTREMAL_COVARIANCE_20260805.md`.
It proves that the half-average constant is attained by an honest
first-minimum family and that its centered covariance is negative of linear
size.  Thus the remaining proof must control the combined phase train, not
the centered covariance as a harmless error.

## 1. Normalization and least-critical period cap

Let `h` be the least index attaining maximum density `lambda`, and let `g`
be the gcd of the complete critical set.  Since `h` itself is critical,
`g<=h`.

If `h<N`, first-`zeta` normalization gives

\[
 g\lambda\le h\lambda=c_h<\zeta.
\]

If `h=N`, suppose endpoint saturation selected a proper partition with
value `P_N>=zeta`.  Criticality of `N` makes

\[
 \sum_i c_{j_i}=c_N=N\lambda=\sum_i j_i\lambda.
\]

Every summand satisfies `c_(j_i)<=j_i lambda`; equality of the sum forces
equality termwise, producing a critical `j_i<N`.  This contradicts the
least-critical choice.  Hence `P_N<zeta`, saturation gives `c_N=zeta`, the
only critical denomination is `N`, and `g=N`.  Therefore `P=g lambda=zeta`.
All strict and equality cases in Theorem 1.1 are correct.

## 2. Semigroup shortest paths and signs

For denomination cost

\[
 a_j=\lambda j-c_j\ge0,
\]

an exact-fill configuration of capacity `m` has value

\[
 \lambda m-\sum_i a_{j_i}.
\]

Maximizing value is therefore exactly minimizing cost, so

\[
 e_m=\lambda m-V_m
 =\min_{\sum j_i=m}\sum_i a_{j_i}.
\]

After forgetting ordinary capacity and retaining only its residue modulo
`g`, critical steps have zero cost and are residue loops.  The minimum cost
is `-beta_r=d_r`.  The empty walk is needed and valid only for residue zero.
Since exact fills are a subset of residue walks,

\[
 \delta_m=e_m-d_{m\bmod g}=U_m-V_m\ge0.
\]

Concatenating residue walks gives

\[
 d_{r+t}\le d_r+d_t
\]

with residues read cyclically.  There is no lost `P` term because `d` is
reduced cost, not physical value.

## 3. Cyclic half-average and its exact scale

Choose `a` with `d_a=Delta`.  For every residue `r`,

\[
 \Delta\le d_r+d_{a-r}.
\]

The involution `r -> a-r` permutes the residue group.  Summing gives

\[
 2\sum_r d_r\ge g\Delta,
\]

hence `mean(d)>=Delta/2`.  No divisibility, parity, or choice of an inverse
of `a` is used.  The endpoint-only family in the companion theorem attains
equality for every group order, confirming the constant is sharp on the
actual Bellman class.

## 4. Queue endpoints, half-open conventions, and periodicity

For `m=qg+r`,

\[
 U_m=qP+s_r,\qquad L_m=qP+r\lambda.
\]

The standard walk of `r` unit denominations proves
`s_r>=r c_1>=0`, while `beta_r<=0` proves
`s_r<=r lambda<P` for `0<r<g`.  This is the only hidden premise in the
original proof; the source now explicitly assumes the standard
nonnegative Bellman table and records this derivation.

Moving the counting atom at `qP+r lambda` left to `qP+s_r` changes the
strict counting function by

\[
 {\bf1}_{[qP+s_r,qP+r\lambda)}.
\]

Both endpoints lie in one `P`-block, so summing over residues yields the
stated periodic queue.  Duplicate atoms simply contribute multiplicity.
Changing half-open endpoint conventions affects only a countable null set,
while the Rayleigh deviation measure is absolutely continuous.

Its period area is exactly

\[
 \sum_r(r\lambda-s_r)=\sum_r d_r,
\]

so the normalization by `P=g lambda` in (3.4) is correct.

## 5. Signed phase pairing and zeroth mode

With `sigma(dx)=-K'(x)dx`, absolute continuity and `K(infinity)=0` give

\[
 \sigma([u,v))=K(u)-K(v),\qquad
 \sigma((x,\infty))=K(x).
\]

The periodic queue is bounded and `K'` is integrable, so summation against
the signed measure is justified by absolute integrability, not by a false
Tonelli invocation for a positive measure.  Consequently

\[
 \Phi(U)-C(\lambda)=\int_0^\infty w\,d\sigma.
\]

Periodization gives

\[
 Q_P(x)=\sum_{q\ge0}-K'(qP+x),
\]

and telescoping over the half-open blocks gives

\[
 \int_0^P Q_P=K(0)-K(\infty)=M.
\]

Thus the sign and normalization of the zeroth term are exactly
`+M mean(w)`.  The density `Q_P` is signed; the theorem correctly makes no
pointwise-positivity claim.

## 6. Finite shoulder identity and area

Eventual Apéry equality makes only finitely many `delta_m` nonzero.  Since
`V_m<=U_m`, moving the formal counting atom left once more gives

\[
 z(x)=\sum_m {\bf1}_{[V_m,U_m)}(x)\ge0,
\]

and

\[
 \Phi(V)-\Phi(U)=\int z\,d\sigma.
\]

For `Q_0(x)=2x exp(-x^2)`,

\[
 \max Q_0=\sqrt{2/e}<1.
\]

On the compact branch `K'` is a difference of two values of `Q_0`; the
absolute value of a difference of two numbers in
`[0,sqrt(2/e)]` is at most `sqrt(2/e)`, not twice that number.  On the outer
branch it is one such value.  Hence `||K'||_infty<1`.  The termwise mean
value theorem proves

\[
 \mathscr S^-\le ||K'||_\infty\sum_m\delta_m,
\]

and debt at least `c*/2` forces area strictly greater than `c*/2` exactly
as claimed.

## 7. Total subadditivity and level-set spreading

Bellman superadditivity gives

\[
 e_{i+j}=\lambda(i+j)-V_{i+j}\le e_i+e_j.
\]

Summing this over all `m-1` proper splits of `m` counts every
`e_1,...,e_(m-1)` twice, proving

\[
 (m-1)e_m\le2\sum_{i=1}^{m-1}e_i.
\]

If `e_m>t`, each split has an endpoint above `t/2`; the active prefix set
and its reflection cover all `m-1` splits, giving the factor-two level-set
bound.  If the eventual cyclic profile keeps a level set infinite, the
extended inequality remains a valid one-way statement.

## 8. New covariance stress test

The companion endpoint-only theorem takes

\[
 c_1=\cdots=c_{N-1}=0,\qquad c_N=\zeta.
\]

It is a genuine saturated table with `P=zeta`, `V=U`,
`d_r=r zeta/N`, and

\[
 {1\over N}\sum_r d_r={\Delta\over2}.
\]

Its queue is the front-loaded staircase and its centered covariance is

\[
 \mathcal C_N
 =N C(\zeta)-C(\zeta/N)-{M(N-1)\over2}
 <{9-N\over200}.
\]

Therefore `mathcal C_N<0` for every `N>=9` and has linear magnitude.  This
is the requested exact obstruction to a nonnegative or dimension-free
centered-covariance estimate.  Yet

\[
 \Phi(U)=N C(\zeta)>0.
\]

The correct next analytic target is consequently a lower bound on the
combined phase functional over the cyclically superadditive Apéry cone, or
an exchange reduction of that cone to controlled phase-train extremizers.

## 9. Scope verdict

The audited theorem proves exact analytic resources but neither:

1. signs the combined formal-plus-shoulder functional;
2. proves the Rayleigh all-price/coagulation inequality; nor
3. converts queue area into occurrence-faithful Boolean capacity.

All three exclusions are stated correctly in the source.  Subject to the
single explicit-premise clarification above, the theorem is proof-safe.
