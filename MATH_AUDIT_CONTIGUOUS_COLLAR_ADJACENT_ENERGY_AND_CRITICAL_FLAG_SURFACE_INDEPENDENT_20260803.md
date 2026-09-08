# Independent audit: contiguous-collar adjacent energy and critical flag surface

**Date:** 2026-08-03  
**Object audited:**
`MATH_THEOREM_CONTIGUOUS_COLLAR_ADJACENT_ENERGY_AND_CRITICAL_FLAG_SURFACE_20260803.md`  
**Method:** independent symbolic replay; no finite search or numerical solver.  
**Verdict:** **GO**, after one nonmathematical wording correction in Section 2.

## 1. Scope checked

Put

\[
 k=2r,\qquad W={2r\choose r},\qquad
 b_j={{2r\choose r-j}\over W},
\]

and let

\[
 d=(\delta+o(1))\sqrt r,\qquad
 \delta={\sqrt\pi\over2},\qquad D=d+C,
\]

where `C` is fixed.  I checked all of the following claims.

1. The exact path-occupancy inequality and its boundary constant.
2. Its conversion, under the collar capacity constraint, into the exact
   Hall-energy inequality.
3. The Gaussian Riemann-sum constant
   \(\eta(c)\), including positivity at
   \(c=\sqrt{\log2}\).
4. The conversion from macroscopic energy to one adjacent pair of constant
   joint probability.
5. The implication from an `o(W)` named-target leave.
6. The uniform-order normalized flag-codegree calculation and the lower
   bound on the largest atom.
7. The label-sensitive extension for arbitrary weighted nested-chain atoms
   with named-target degree at most one.
8. All floor, ceiling and fixed-`C` effects.

The theorem is an obstruction to black-box degree/codegree rounding in the
specified atom model.  It is not a nonexistence theorem for Boolean-specific
absorbers or architectures which split the two adjacent-rank obligations
between different physical roles.

## 2. Exact path inequality

Let a selected subset of a path on `2t` vertices have `m` vertices, `h`
nonempty selected runs and `e` internal selected edges.  Then

\[
 e=m-h.
\]

The `2t-m` unselected vertices create at most `2t-m+1` selected runs, so

\[
 e=m-h\ge m-(2t-m+1)=2m-2t-1.
\]

Equivalently,

\[
 m\le t+{e+1\over2}.
\]

The `1/2` term is therefore the exact endpoint loss for a linear path.
Equality occurs, for example, when the unselected vertices separate all
selected runs and both path endpoints are selected.  Lemma 1.1 is correct.

## 3. Exact expectation and Hall-deficit conversion

Set

\[
 t=\left\lfloor{D\over2}\right\rfloor,
 \qquad A_t=\{a+1,\ldots,a+2t\}.
\]

For the theorem's fixed range

\[
 \sqrt{\log2}\le c<\delta,
 \qquad a=\lceil c\sqrt r\rceil,
\]

we have, for all sufficiently large `r`,

\[
 0<D-a<t<D,
 \qquad a+2t<r.
\]

Indeed, after division by \(\sqrt r\), these are respectively

\[
 0<\delta-c<\delta/2<\delta,
 \qquad {c+\delta\over\sqrt r}<1.
\]

The last displayed comparison is shorthand for
\((c+\delta)\sqrt r+O(1)<r\), which is immediate.  The fixed `C`, the
ceiling in `a`, and the floor in `t` contribute only `O(1)`.

For every realization,

\[
 |R\cap A_t|
 \le \min(t,D-L)+{E_t(R)+1\over2}.
\]

If \(D-L\le t\), this follows from capacity alone; if \(D-L>t\), it is
the path inequality.  Because `L` is integer-valued and
\(\Pr(L\ge j)=b_j\),

\[
 \begin{aligned}
 \mathbb E\min(t,D-L)
 &=t-\mathbb E(L-(D-t))_+\\
 &=t-\sum_{j=D-t+1}^{a}b_j.
 \end{aligned}
\]

Consequently

\[
 \sum_{j\in A_t}q_j
 \le t-\sum_{j=D-t+1}^{a}b_j
       +{\mathbb E E_t(R)+1\over2}.
\]

The collar interval \([D-t+1,a]\) and `A_t` are disjoint and adjacent, so
subtracting from the target mass gives exactly

\[
 \mathbb E E_t(R)
 \ge
 2\left(\sum_{j=D-t+1}^{a+2t}b_j-t\right)-1
 -2\sum_{j\in A_t}(b_j-q_j).
\]

Thus equations (2.3)--(2.6), including the factor `2` and the boundary
constant `-1`, are correct.

## 4. Gaussian constant and fixed-`C` rounding

Uniformly for \(j=O(\sqrt r)\),

\[
 \log b_j=-{j^2\over r}+O\left({j\over r}+{j^3\over r^2}\right),
\]

hence \(b_j=e^{-j^2/r+o(1)}\).  Furthermore,

\[
 {D-t+1\over\sqrt r}\to{\delta\over2},
 \quad {a+2t\over\sqrt r}\to c+\delta,
 \quad {t\over\sqrt r}\to{\delta\over2}.
\]

Therefore

\[
 \sum_{j=D-t+1}^{a+2t}b_j-t
 =\left(
   \int_{\delta/2}^{c+\delta}e^{-x^2}\,dx
     -{\delta\over2}+o(1)
  \right)\sqrt r.
\]

This verifies

\[
 \eta(c)=\int_{\delta/2}^{c+\delta}e^{-x^2}\,dx
              -{\delta\over2}.
\]

The function is increasing in `c`.  At
\(c_0=\sqrt{\log2}\), using
\(\delta=\int_0^\infty e^{-x^2}\,dx\),

\[
 \eta(c_0)
 =\int_0^{\delta/2}(1-e^{-x^2})\,dx
   -\int_{c_0+\delta}^{\infty}e^{-x^2}\,dx.
\]

The elementary bounds

\[
 1-e^{-x^2}\ge x^2-{x^4\over2},
 \qquad
 \int_A^\infty e^{-x^2}\,dx\le {e^{-A^2}\over2A}
\]

give

\[
 \eta(c_0)
 \ge {\delta^3\over24}-{\delta^5\over320}
       -{e^{-(c_0+\delta)^2}\over2(c_0+\delta)}>0.
\]

Thus the inclusive lower endpoint in the theorem is valid.  Since `C` is
fixed, it changes every endpoint by only `O(1)` and cannot change either
\(\eta(c)\) or any leading constant.  If \(c>\delta\), then
\(a>D\) eventually, while
\(\Pr(L=a)=b_a>0\), so the pointwise capacity law is infeasible.  The
theorem correctly restricts its nontrivial argument to \(c<\delta\).
The exact boundary \(c=\delta\) can depend on lower-order terms in
\(d+C-a\); the source now records this explicitly and makes no boundary
claim.

## 5. Macroscopic energy and one adjacent pair

Under

\[
 \sum_{j>a}(b_j-q_j)=o(\sqrt r),
\]

the exact Hall-energy row gives

\[
 \mathbb E E_t(R)
 \ge(2\eta(c)+o(1))\sqrt r.
\]

But

\[
 \mathbb E E_t(R)
 =\sum_{j=a+1}^{a+2t-1}\Pr(j,j+1\in R),
\]

and the number of terms is

\[
 2t-1=(\delta+o(1))\sqrt r.
\]

Hence some adjacent pair obeys

\[
 \theta_j\ge{2\eta(c)\over\delta}+o(1).
\]

No independence, stability or parity assumption on `R` is used.

If the atoms form a weighted named-target packing and their total leave is
`o(W)`, then the residual omitted mass is

\[
 W\sum_{j>a}(b_j-q_j)=o(W).
\]

Therefore

\[
 \sum_{j>a}(b_j-q_j)=o(1),
\]

which is indeed stronger than the `o(sqrt(r))` assumption used above.

## 6. Uniform-order normalized codegree and atom width

For the adjacent pair selected above, put

\[
 u=r-j,qquad s=u-1.
\]

In the symmetric uniform-order owner-chain law, every named cover flag
\(S\subset U\), with \(|S|=u-1\), \(|U|=u\), has

\[
 d_x(S,U)={\theta_j\over b_j u},
 \qquad
 d_x(U)={q_j\over b_j}.
\]

Thus

\[
 {d_x(S,U)\over d_x(U)}
 ={\theta_j\over q_j u}
 \ge {\theta_j\over r},
\]

because \(q_j\le1\) and \(u\le r\).  Since normalized pair codegree uses
the smaller incident degree, this ratio is a valid lower bound, and

\[
 \rho_2\ge
 \left({2\eta(c)\over\delta}+o(1)\right){1\over r}.
\]

The support condition \(L\le a\), together with its tail law, gives the
exact identity

\[
 \Pr(L=a)=\Pr(L\ge a)=b_a>0.
\]

Therefore a supported atom has at least `a` target vertices.  Pointwise
capacity gives at most `D` target vertices per atom.  Including the owner,

\[
 a+1\le K\le D+1.
\]

It follows that

\[
 K^2\rho_2
 \ge {2c^2\eta(c)\over\delta}+o(1).
\]

The constants in (0.9)--(0.10) are correct.

## 7. Label-sensitive nested-chain extension

The extension in Section 5 is also correct and does not require uniform
order.  Suppose the total atom weight at each of the `W` owners is one,
each atom's selected named targets form one inclusion chain, the empirical
rank law is `(L,R)`, and every named strict-lower target has weighted degree
at most one.

Every atom containing both adjacent ranks `u-1,u` contains exactly one
named cover flag of those ranks.  Hence the sum of all such flag codegrees
is

\[
 \sum_{S\lessdot U}d_x(S,U)=W\theta_j.
\]

There are

\[
 {2r\choose u}u=Wb_j u
\]

named cover flags.  Averaging gives one flag with

\[
 d_x(S,U)\ge {\theta_j\over b_j u}
              \ge {\theta_j\over r}.
\]

The positive flag ensures both incident degrees are positive; the
capacity-one hypothesis ensures both are at most one.  Therefore

\[
 {d_x(S,U)\over\min(d_x(S),d_x(U))}
 \ge d_x(S,U)
 \ge {\theta_j\over r}.
\]

This establishes the same \(\Omega(1/r)\) normalized-codegree lower bound
for an arbitrary label-sensitive ordering inside the stated
capacity-one nested-chain model.  The proof would not be valid without the
named-target degree cap, nor if the two adjacent-rank obligations were
physically assigned to different atoms.  The source theorem states both
scope exclusions explicitly.

## 8. Correction made

The original Section 2 said that `A_t` “lies below rank zero.”  Its proof
and formulas use the correct fact

\[
 a+2t<r,
\]

so the block lies inside the residual distance range and its corresponding
target ranks remain positive.  I replaced the erroneous phrase by that
statement.  This changes no formula or conclusion.

## 9. Final verdict

After the wording correction above, every claimed implication is valid:

\[
 \text{near-complete residual marginals}
 \Longrightarrow
 \Omega(\sqrt r)\text{ adjacent energy}
 \Longrightarrow
 \rho_2=\Omega(1/r),
\]

while \(K=\Theta(\sqrt r)\), hence

\[
 K^2\rho_2=\Omega(1).
\]

The theorem is proof-safe with fixed additive capacity `C`, at the inclusive
threshold \(c=\sqrt{\log2}\), and under arbitrary label-sensitive nested
chains satisfying named-target degree at most one.
