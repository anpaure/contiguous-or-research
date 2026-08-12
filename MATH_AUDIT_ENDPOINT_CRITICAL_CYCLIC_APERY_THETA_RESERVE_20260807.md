# Independent audit: endpoint-critical cyclic Apéry theta reserve

**Date:** 2026-08-07  
**Audited file:**
`MATH_THEOREM_ENDPOINT_CRITICAL_CYCLIC_APERY_THETA_RESERVE_20260807.md`  
**Verdict:** **PASS.**  The theorem proves the strict positivity of the
formal period-one endpoint-critical Apéry phase.  It does not sign the
finite availability shoulder.

## 1. Cyclic inverse profile

With `E_r=r-ns_r`, the wrap inequality is exactly

\[
 E_{i+j\bmod n}\le E_i+E_j.
\]

Also `0<=E_r<=r` and `E_1<=1`.  Hence the lift

\[
 B(qn+r)=qn+r-E_r
\]

is nondecreasing and superadditive.  Its left inverse produces the
nonnegative subadditive circle function used in the cited inverse-circle
theorem.  On the interval

\[
 r-E_r<t<r+1-E_{r+1}
\]

the inverse discrepancy is literally `r+1-t`.  Direct integration gives

\[
 \mathbb E U={1\over2}+\mu,
 \qquad
 \operatorname {Var}(U)={1\over12}+\operatorname {Var}(E)
 \le { (1/2+\mu)^2\over3}.
\]

Zero-length phase intervals and repeated shifts have measure zero and do
not alter the calculation.

## 2. Stieltjes identity

The pieces in the definition of `F` tile `[0,infinity)`, so
`integral_0^1 F=1`.  If `H(z)` counts shifts strictly below `z`, then
`U(z)=H(z)-nz` away from the finitely many jumps.  Integrating each jump
explicitly gives

\[
 \int_0^1UF'
 =\sum_r(F(1)-F(s_r))-n(F(1)-\int_0^1F)
 =n-\sum_rF(s_r).
\]

Thus no endpoint term is missing at zero or one.

## 3. Fourier normalization

For `q=-K'` and `A=sqrt(pi)/2`, periodization gives

\[
 {F'(y)\over A}=\sum_{j\ge0}q(A(j+y)).
\]

After `x=A(j+y)`, the `k`-th Fourier coefficient is exactly

\[
 c_k=\int_0^\infty q(x)e^{-2\pi ikx/A}\,dx.
\]

There is no missing factor of `A`.  The previously proved variation
identity

\[
 \operatorname {Var}(q')=b_0+4
\]

therefore yields `|c_k|<B/(16 pi k^2)` for `k!=0`.

For `k=1`, the smooth measure `d eta=-q''dx` is positive on the two open
pieces.  The upward jump of `q'` at `A` is two, while
`exp(-2 pi i A/A)=1`; hence the boundary and jump terms combine to

\[
 c_1={1\over(it_1)^2}\int(1-e^{-it_1x})\,d\eta(x).
\]

The two moments used in the estimate check directly:

\[
 \int_0^A x(A-x)d\eta
 =A\varphi(2A)+2\int_0^Aq
 =2\gamma+(\pi+2)e^{-\pi},
\]

and

\[
 \eta((A,\infty))=-\varphi'(2A)
 =2(2\pi-1)e^{-\pi}.
\]

Thus the `|c_1|<1/10` estimate and the `k>=2` bounded-variation estimate
are compatible and cover every nonzero Fourier mode.

## 4. Parseval and final margin

Parseval gives

\[
 V_F=2\sum_{k\ge1}|c_k|^2.
\]

The displayed rational bounds imply

\[
 V_F<3(87/1000)^2,
 \qquad
 \gamma=1-2e^{-\pi/4}>88/1000.
\]

Consequently Cauchy--Schwarz gives

\[
 \int UF'
 >m(88/1000)-{m\over\sqrt3}\sqrt{3(87/1000)^2}
 ={m\over1000}\ge {1\over2000}.
\]

This proves the quantitative conclusion.  The finite shoulder term

\[
 \sum_{m<H}\bigl(K(AL(m))-K(AW_m)\bigr)
\]

is not present in the formal periodic phase and remains outside the
theorem, exactly as stated.

