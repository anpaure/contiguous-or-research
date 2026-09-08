# The endpoint-critical cyclic Apéry theta reserve is strictly positive

**Date:** 2026-08-07  
**Method:** pure mathematics; inverse-circle variance, an exact phase
identity, and a one-frequency Gaussian estimate  
**Status:** unconditional.  This closes the formal period-one scalar left
open in Section 5 of
`MATH_OBSTRUCTION_RAYLEIGH_ENDPOINT_CRITICAL_THETA_AND_TWO_PENALTY_CLOSURE_20260807.md`.
It does **not** sign the separate finite-availability shoulder.

## 1. Statement

Put

\[
 a={\pi\over4},\qquad A={\sqrt\pi\over2},
\tag{1.1}
\]

and, for \(0\le y\le1\),

\[
 F(y)=e^{-a(1-y)^2}+\sum_{q\ge1}e^{-a(q+y)^2}.
\tag{1.2}
\]

### Theorem 1.1 (cyclic Apéry theta reserve)

Let \(n\ge1\), let \(s_0=0\), and suppose

\[
 0\le s_r\le {r\over n}\qquad(0\le r<n)
\tag{1.3}
\]

and

\[
 s_{(i+j)\bmod n}
 \ge s_i+s_j-\left\lfloor{i+j\over n}\right\rfloor
 \qquad(0\le i,j<n).
\tag{1.4}
\]

Then

\[
 \boxed{
 n-\sum_{r=0}^{n-1}F(s_r)
 >{1/2+\mu\over1000}\ge {1\over2000}.}
\tag{1.5}
\]

Here \(\mu=n^{-1}\sum_r(r-ns_r)\).  In particular
\(\sum_rF(s_r)<n\).

Thus the weak inequality asked for at the endpoint-critical formal
Apéry gate is true, with strict reserve.  No extra condition beyond the
honest cyclic carry inequalities is needed.

The proof has two independent ingredients.  The cyclic inequalities give
a sharp variance bound for the phase-counting discrepancy.  A special
one-period estimate for the Rayleigh kernel says that its centered
derivative has variance strictly less than three times the square of its
mean.  Cauchy--Schwarz then has the correct sign with room to spare.

For (n=1), take the zero defect and (U(z)=1-z); the argument in
Sections 3--5 applies verbatim and gives (1-F(0)>0).  Hence below we
assume (n\ge2).

## 2. The cyclic defect and its inverse phase

Define

\[
 E_r=r-ns_r\qquad(0\le r<n).
\tag{2.1}
\]

Then \(E_0=0\), \(E_r\ge0\), and (1.4) is exactly cyclic
subadditivity:

\[
 \boxed{E_{(i+j)\bmod n}\le E_i+E_j.}
\tag{2.2}
\]

Moreover

\[
 c:=E_1=1-ns_1\le1.
\tag{2.3}
\]

Write

\[
 \mu={1\over n}\sum_{r=0}^{n-1}E_r.
\tag{2.4}
\]

The scale-sharp cyclic inverse-circle theorem gives

\[
 \boxed{\operatorname {Var}(E)\le{\mu(\mu+c)\over3}
 \le{\mu(\mu+1)\over3}.}
\tag{2.5}
\]

For completeness, its construction is recalled.  Extend

\[
 B(qn+r)=qn+r-E_r\qquad(q\in\mathbb Z,\ 0\le r<n).
\tag{2.6}
\]

Then \(B\) is nondecreasing and superadditive.  Its left generalized
inverse \(C(t)=\min\{m:B(m)\ge t\}\) is subadditive.  Hence

\[
 u(t)=C(t)-t
\tag{2.7}
\]

is a nonnegative subadditive function on the connected circle
\(\mathbb R/n\mathbb Z\).  Connected-circle Kneser implies that the
increasing quantile \(q_u\) is subadditive.  If \(m_u=\mathbb Eu\),
integration of
\(q_u(x+y)\le q_u(x)+q_u(y)\) shows that \(q_u\) is majorized by
\(2m_u x\), and therefore

\[
 \operatorname {Var}(u)\le {m_u^2\over3}.
\tag{2.8}
\]

On the phase interval

\[
 r-E_r<t<r+1-E_{r+1}
\tag{2.9}
\]

one has \(u(t)=r+1-t\).  Direct integration and cyclic telescoping give

\[
 \mathbb Eu={1\over2}+\mu,
 \qquad
 \operatorname {Var}(u)={1\over12}+\operatorname {Var}(E).
\tag{2.10}
\]

Equations (2.8)--(2.10), first after normalizing \(E_1=1\) and then
rescaling, give (2.5).

Now put

\[
 a_r=r-E_r=ns_r\qquad(0\le r<n),\qquad a_n=n.
\tag{2.11}
\]

The inequalities with \(j=1\) show that \(s_{r+1}\ge s_r\), so
\(a_0\le\cdots\le a_n\).  Define the phase discrepancy on \((0,1)\)
by

\[
 U(z)=r+1-nz
 \quad\hbox{when}\quad {a_r\over n}<z<{a_{r+1}\over n}.
\tag{2.12}
\]

Zero-length intervals cause no problem.  This is just the inverse-circle
profile \(u(nz)\).  Consequently

\[
 \boxed{
 \mathbb EU={1\over2}+\mu=:m,
 \qquad
 \operatorname {Var}(U)
 ={1\over12}+\operatorname {Var}(E)
 \le {m^2\over3}.}
\tag{2.13}
\]

## 3. Exact conversion of the theta reserve to a covariance

The intervals in (1.2) tile the positive half-line, so

\[
 \int_0^1F(y)\,dy
 =\int_0^\infty e^{-ax^2}\,dx=1.
\tag{3.1}
\]

Also direct cancellation gives

\[
 \boxed{
 \gamma:=\int_0^1F'(y)\,dy=F(1)-F(0)
 =1-2e^{-\pi/4}>0.}
\tag{3.2}
\]

Let \(H(z)\) count the phase points \(s_r\) strictly below \(z\),
with the zero phases included immediately to the right of zero.  Then
\(U(z)=H(z)-nz\).  Stieltjes integration by parts, including the jump at
zero, gives

\[
\begin{aligned}
 \int_0^1U(z)F'(z)\,dz
 &=n\int_0^1F(z)\,dz-\sum_{r=0}^{n-1}F(s_r)\\
 &=\boxed{n-\sum_{r=0}^{n-1}F(s_r)}.
\end{aligned}
\tag{3.3}
\]

Thus it remains only to prove that the covariance on the left is
positive.

## 4. The one-period Rayleigh derivative estimate

### Lemma 4.1

For the function (1.2),

\[
 \boxed{
 V_F:=\int_0^1\bigl(F'(y)-\gamma\bigr)^2\,dy
 <3\gamma^2.}
\tag{4.1}
\]

#### Proof

Let

\[
 \varphi(x)=2x e^{-x^2}
\tag{4.2}
\]

and let \(K\) be the compact Rayleigh kernel whose derivative
\(q=-K'\) is

\[
 q(x)=
 \begin{cases}
  \varphi(A-x)-\varphi(A+x),&0<x<A,\\
  -\varphi(A+x),&x>A.
 \end{cases}
\tag{4.3}
\]

Periodizing (4.3) gives

\[
 {F'(y)\over A}=\sum_{j\ge0}q(A(j+y)).
\tag{4.4}
\]

Hence, for \(k\in\mathbb Z\),

\[
 c_k:=\int_0^1F'(y)e^{-2\pi iky}\,dy
 =\int_0^\infty q(x)e^{-it_kx}\,dx,
 \qquad t_k={2\pi k\over A}.
\tag{4.5}
\]

In particular \(c_0=\gamma\).  Two bounded-variation integrations by
parts give, for \(k\ne0\),

\[
 |c_k|<{B\over t_k^2}
 ={B\over16\pi k^2},
 \qquad B={5324\over875}.
\tag{4.6}
\]

Indeed, with

\[
 b_0=q'(0)=2(\pi-2)e^{-\pi/4},
\tag{4.7}
\]

the exact variation is \(\operatorname {Var}(q')=b_0+4\), so the
Fourier numerator is at most \(4+2b_0<B\).

We need one modest sharpening at \(k=1\).  On the two open intervals
\((0,A)\) and \((A,\infty)\), put

\[
 d\eta=-q''(x)\,dx.
\tag{4.8}
\]

The reflected-curvature inequality

\[
 \varphi''(A+x)>\varphi''(A-x)\qquad(0<x<A)
\tag{4.9}
\]

and \(\varphi''(A+x)>0\) for \(x>A\) show that \(\eta\) is positive.
The derivative \(q'\) has an upward jump of exactly two at \(A\), and

\[
 \eta((0,\infty))=b_0+2.
\tag{4.10}
\]

Integrating twice and using \(e^{-it_1A}=1\), the jump cancels exactly:

\[
 c_1={1\over(it_1)^2}
 \int_{(0,\infty)}(1-e^{-it_1x})\,d\eta(x).
\tag{4.11}
\]

On \([0,A]\), the elementary inequality

\[
 2\sin(\pi u)\le8u(1-u)\qquad(0\le u\le1)
\tag{4.12}
\]

gives

\[
 |1-e^{-it_1x}|\le {8x(A-x)\over A^2}.
\tag{4.13}
\]

On the tail use \(|1-e^{-it_1x}|\le2\).  The two required quantities
are exact.  If

\[
 I=\int_0^A x(A-x)\,d\eta(x),
\tag{4.14}
\]

then integration by parts in (4.3) gives

\[
 I=A\varphi(2A)+2\int_0^Aq(x)\,dx
 =2\gamma+(\pi+2)e^{-\pi}.
\tag{4.15}
\]

The tail mass is

\[
 \eta((A,\infty))=-\varphi'(2A)
 =2(2\pi-1)e^{-\pi}.
\tag{4.16}
\]

Since \(A^2=\pi/4\) and \(t_1^2=16\pi\), (4.11)--(4.16) yield

\[
 |c_1|
 \le {4\gamma\over\pi^2}
 +{2(\pi+2)e^{-\pi}\over\pi^2}
 +{(2\pi-1)e^{-\pi}\over4\pi}
 <{1\over10}.
\tag{4.17}
\]

Here, and below, the strict rational estimates can be checked without
decimal arithmetic from

\[
 {31415\over10000}<\pi<{355\over113},
\quad
 {4559\over10000}<e^{-\pi/4}<{57\over125},
\quad
 e^{-\pi}<{2161\over50000}.
\tag{4.18}
\]

For example, the right side of (4.17) is at most

\[
 {277342451352413\over2802802319000000}
 <{1\over10}.
\tag{4.19}
\]

The inequalities in (4.18) follow from the usual alternating Taylor
bounds after inserting the displayed rational bounds for \(\pi\).

Parseval, (4.6), and (4.17) now give

\[
\begin{aligned}
 V_F
 &=2\sum_{k\ge1}|c_k|^2\\
 &<{1\over50}
 +2\left({B\over16\pi}\right)^2
   \sum_{k\ge2}{1\over k^4}\\
 &<{1\over50}
 +{1\over6}\left(
 {B\over16(31415/10000)}\right)^2\\
 &={6511609483\over290149254150}.
\end{aligned}
\tag{4.20}
\]

We used
\(\sum_{k\ge2}k^{-4}=\pi^4/90-1<1/12\), which follows from
\(\pi<355/113\).  Finally (4.18) gives

\[
 \gamma>{11\over125},
\tag{4.21}
\]

and the exact comparison is

\[
 3\left({11\over125}\right)^2
 -{6511609483\over290149254150}
 ={143211243383\over181343283843750}>0.
\tag{4.22}
\]

This proves (4.1). \(\square\)

## 5. Completion

Center both factors in (3.3).  Equations (2.13), (3.2), and
Cauchy--Schwarz give

\[
\begin{aligned}
 n-\sum_rF(s_r)
 &=\int_0^1U F'\\
 &=m\gamma+\int_0^1(U-m)(F'-\gamma)\\
 &\ge m\gamma-\sqrt{\operatorname {Var}(U)}\sqrt{V_F}\\
 &>m\gamma-{m\over\sqrt3}\sqrt{3\gamma^2}=0.
\end{aligned}
\tag{5.1}
\]

The rational bound (4.20) is smaller than

\[
 3\left({87\over1000}\right)^2,
\tag{5.2}
\]

while (4.21) gives \(\gamma>88/1000\).  Therefore

\[
 n-\sum_rF(s_r)>{m\over1000}\ge {1\over2000}.
\tag{5.3}
\]

This proves the quantitative form of Theorem 1.1.

## 6. Consequence and exact remaining scope

For an endpoint-critical max-plus clock, the stable Apéry shifts obey
(1.3)--(1.4).  Therefore its complete formal period contributes

\[
 \boxed{
 n-\sum_{r=0}^{n-1}F(s_r)>0.}
\tag{6.1}
\]

The direct first-block residues need not obey the wrap inequalities and
can violate the analogous theta bound; that earlier counterexample is
unaffected.  The finite Bellman functional is

\[
 n-\sum_rF(s_r)
 +\sum_{m<H}\bigl(K(AL(m))-K(AW_m)\bigr).
\tag{6.2}
\]

Theorem 1.1 closes the first term.  The signed finite-availability
shoulder in the second term remains a separate gate and is not claimed
positive here.

## 7. Dependencies

1. the connected-circle inverse theorem, reproved in
   `MATH_THEOREM_CYCLIC_APERY_INVERSE_CIRCLE_VARIANCE_CLOSURE_20260805.md`;
2. the reflected-curvature inequality and the exact variation calculation
   from
   `MATH_THEOREM_RAYLEIGH_DUTY_CYCLE_ALL_APERY_PERIOD_FOURIER_POSITIVITY_20260805.md`;
3. only elementary Gaussian integration, Parseval, and
   Cauchy--Schwarz beyond those two results.
