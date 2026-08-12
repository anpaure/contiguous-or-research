# Independent audit: every Rayleigh large-socket tail-capacity cut

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation or search  
**Audited file:**
`MATH_COROLLARY_RAYLEIGH_ALL_LARGE_SOCKET_TAIL_CAPACITY_20260805.md`

**Verdict:** **INDEPENDENT-GO.**  The strict large-socket count, its
layer-cake expectation, the arithmetic-comb identity, the uniform constant,
and the endpoint conventions all replay exactly.  The result closes only
the single-threshold family; it is not the full configuration-price cone.

## 1. The deterministic count is sharp

If a configuration of positive sockets has total size exactly `x` and
contains `k` sockets strictly larger than `t`, then `x>kt`.  Hence

\[
 k<\frac xt,
 \qquad
 k\le \left\lceil\frac xt\right\rceil-1.
\]

The strict socket threshold and the ceiling-minus-one are therefore paired
correctly.  Since the Rayleigh job law is continuous,

\[
 \mathbb E\!\left(\left\lceil\frac Xt\right\rceil-1\right)
 =\sum_{n\ge1}\Pr(X>nt)
 =\sum_{n\ge1}e^{-(A+nt)^2}.
\]

The socket mass above `t` is exactly
`1-exp(-(A-t)^2)` for `0<t<A`.

## 2. Exact comb algebra

Put `q=floor(A/t)`,

\[
 L_n=e^{-(A-nt)^2},\qquad R_n=e^{-(A+nt)^2}.
\]

The kernel formula remains valid at a lattice point `nt=A`, so no separate
case is needed when `A/t` is integral.  Direct summation gives

\[
 C(t)=q+1-\sum_{n=0}^{q}L_n-\sum_{n=0}^{\infty}R_n.
\]

Using `L_0=R_0=p` and isolating `L_1` yields exactly

\[
 \sum_{n\ge1}R_n-(1-L_1)
 =q-2p-\sum_{n=2}^{q}L_n-C(t).
\]

For `q=1` the middle sum is empty.  In general every `L_n<=1`, so

\[
 q-\sum_{n=2}^{q}L_n\ge1
\]

and the slack is at least `1-2p-C(t)=K(0)-C(t)`.

## 3. Uniform constant

The independently audited centered-phase identity is

\[
 C(t)=\mathbb E\left\{\frac{R-(A\bmod t)}t\right\}-p.
\]

Together with

\[
 \mathbb E\left\{\frac{R-(A\bmod t)}t\right\}
 \le\frac{467}{864},
 \qquad p<\frac{57}{125},
\]

it gives

\[
 K(0)-C(t)
 =1-p-\mathbb E\left\{\frac{R-(A\bmod t)}t\right\}
 >1-\frac{57}{125}-\frac{467}{864}
 =\frac{377}{108000}.
\]

All inequalities point in the claimed direction, and the last inequality
is strict because the bound on `p` is strict.

## 4. Scope

The theorem applies to every physical threshold `0<t<A`.  Thresholds at
the socket endpoints are irrelevant to the absolutely continuous measure.
It proves uniform slack for the one-row constraint

\[
 \#\{\text{sockets}>t\}
 \le \left\lceil x/t\right\rceil-1
\]

after aggregation over jobs.  Intersections of several such rows and
general nonarithmetic covering prices are not implied.
