# Six-slot `h=4`: complete positivity of the inactive complement boundary

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sign theorem.  It proves the
literal correlated rectangle gate strictly positive on the complete
inactive boundary `u=A-P`.  Together with the active-`Gamma` theorem, the
whole complement boundary is closed.  No search or sampled computation is
used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
 \qquad
 C(\tau)=F_\tau(0),
\tag{0.1}
\]

and let

\[
                         \varepsilon={1\over20000}.
\tag{0.2}
\]

The inactive side has

\[
                         \Gamma(\delta)=\varepsilon.
\tag{0.3}
\]

The preceding `u=0` theorem proves, uniformly for every residual
admissible period and every `2tau/3<=w<=A`,

\[
 \boxed{
 H_\tau(w):=C(\tau)+F_\tau(w)>{11\over20000}.}
\tag{0.4}
\]

## 1. Complementary-pair transport

Let

\[
                         a=A-P.
\tag{1.1}
\]

On the boundary `u=A-P`, the physical domain also gives `a<=P/4`, hence
`P>=4A/5`; in particular both `P` and `A` lie in the range of (0.4).

For every fixed shift `w`, increasing the period moves every negative
tail away.  Therefore, since `tau>A`,

\[
                         F_\tau(w)>F_A(w).
\tag{1.2}
\]

The exact Jacobi reflection identity gives

\[
 F_A(a)+F_A(A-a)=\rho(a),
 \qquad
                         |\rho(a)|<\varepsilon.
\tag{1.3}
\]

Since `P=A-a`, equations (1.2)--(1.3) imply

\[
 \boxed{
 F_\tau(a)+F_\tau(P)>-\varepsilon.}
\tag{1.4}
\]

## 2. Complete boundary sign

On `u=a`, the rectangle gate is

\[
 \mathfrak R
 =C(\tau)+F_\tau(P)+F_\tau(A)
  +\min\{C(\tau),F_\tau(a)\}-\varepsilon.
\tag{2.1}
\]

### Theorem 2.1

On the complete inactive boundary `u=A-P`,

\[
                         \boxed{\mathfrak R>{9\over20000}>0.}
\tag{2.2}
\]

#### Proof

There are only two low branches.

If the minimum in (2.1) is `C(tau)`, then

\[
 \mathfrak R
 =H_\tau(P)+H_\tau(A)-\varepsilon
 >{11\over20000}+{11\over20000}-{1\over20000}
 ={21\over20000}.
\tag{2.3}
\]

If the minimum is `F_tau(a)`, then (1.4) gives

\[
\begin{aligned}
 \mathfrak R
 &=H_\tau(A)+\{F_\tau(P)+F_\tau(a)\}-\varepsilon\\
 &>{11\over20000}-{1\over20000}-{1\over20000}
 ={9\over20000}.
\end{aligned}
\tag{2.4}
\]

The two cases exhaust the minimum and prove (2.2). \(\square\)

The active side and the `Gamma` switch were already closed with the
stronger margin `3653/700000`.  Hence the entire geometric boundary
`u=A-P` is positive.

## 3. Exact scope

This theorem closes the complete complement boundary and, in particular,
its junction with `u=P/4` at `P=4A/5`.  It does not sign the interior of
the `u=P/4` boundary, the moving boundary `P=2tau/3`, or the low-branch
switch away from the closed faces.

## 4. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| inactive `u=0` theorem | `MATH_THEOREM_SIX_SLOT_H4_INACTIVE_U0_BOUNDARY_COMPLETE_POSITIVITY_20260804.md` | `ba327b06397a9190de23c62c6a0ca0f985bbb75bff12188540518550e03ecd8f` |
| active-`Gamma` theorem | `MATH_THEOREM_SIX_SLOT_H4_ACTIVE_GAMMA_COMPLETE_POSITIVITY_AND_BOUNDARY_COLLAPSE_20260804.md` | `3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953` |
| literal rectangle and reflection reduction | `MATH_THEOREM_SIX_SLOT_H4_LITERAL_RECTANGLE_CORRELATED_GATE_20260804.md` | `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd` |
