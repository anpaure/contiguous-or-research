# Rayleigh clocks reduce to one finite first-crossing block

**Date:** 2026-08-07  
**Status:** unconditional pure-mathematical tail bound and exact scope
obstruction.  It bounds the infinite tail of an arbitrary superadditive
clock by one explicit first-crossing block and identifies the exponentially
small Jacobi-theta defect which prevents a naive complementary-pair proof.
The proposed prefix-only inequality (3.4) is false; Section 6 records the
counterexample and points to the sharp max-plus replacement.

## 1. Kernel and clocks

Put

\[
 A={\sqrt\pi\over2},\qquad a=A^2={\pi\over4},
\tag{1.1}
\]

and define the signed Rayleigh tail

\[
 K(x)=
 \begin{cases}
  1-e^{-(A-x)^2}-e^{-(A+x)^2},&0\le x\le A,\\
  -e^{-(A+x)^2},&x>A.
 \end{cases}
\tag{1.2}
\]

Let

\[
 0=x_0<x_1<x_2<\cdots,
 \qquad x_{m+n}\ge x_m+x_n
\tag{1.3}
\]

be a strict superadditive clock.  Its Bellman functional is

\[
 \mathcal B(x)=\sum_{n\ge0}K(x_n).
\tag{1.4}
\]

The series is absolutely convergent because
\(x_n\ge n x_1\).

Let

\[
 p=\max\{n:x_n\le A\},\qquad h=p+1,
\tag{1.5}
\]

and normalize the first block by

\[
 y_r={x_r\over A}\quad(0\le r\le p),
 \qquad b={x_h\over A}>1.
\tag{1.6}
\]

Thus

\[
 0=y_0<y_1<\cdots<y_p\le1<b.
\tag{1.7}
\]

## 2. Exact first-crossing block bound

For \(b>1\) and \(0\le y\le1\), define

\[
 \boxed{
 \Phi_b(y)=e^{-a(1-y)^2}
   +\sum_{q\ge0}e^{-a(1+qb+y)^2}.}
\tag{2.1}
\]

### Theorem 2.1 (finite first-crossing reduction)

Every clock (1.3) satisfies

\[
 \boxed{
 \mathcal B(x)
 \ge p+1-\sum_{r=0}^{p}\Phi_b(y_r).}
\tag{2.2}
\]

Consequently the finite inequality

\[
 \boxed{
 \sum_{r=0}^{p}\Phi_b(y_r)\le p+1}
\tag{2.3}
\]

for every first-crossing prefix proves the complete Rayleigh clock
inequality.

#### Proof

Equation (1.2) gives the exact identity

\[
 \mathcal B(x)
 =p+1-
   \sum_{r=0}^{p}e^{-a(1-y_r)^2}
   -\sum_{n\ge0}e^{-(A+x_n)^2}.
\tag{2.4}
\]

Write every \(n\ge0\) uniquely as

\[
 n=qh+r,\qquad q\ge0,\quad0\le r<h.
\tag{2.5}
\]

Superadditivity gives

\[
 x_{qh+r}\ge qx_h+x_r=A(qb+y_r).
\tag{2.6}
\]

The function \(t\mapsto e^{-(A+t)^2}\) is decreasing on the
nonnegative line.  Hence

\[
 \sum_{n\ge0}e^{-(A+x_n)^2}
 \le
 \sum_{r=0}^{p}\sum_{q\ge0}
 e^{-a(1+qb+y_r)^2}.
\tag{2.7}
\]

Substituting (2.7) into (2.4) is exactly (2.2). \(\square\)

This is a genuine infinite-to-finite reduction: no Apéry conductor or
eventual periodicity is assumed.

The restriction to strict clocks loses nothing.  If
\(0=x_0\le x_1\le\cdots\) is a locally finite nondecreasing
superadditive clock, then

\[
 x_n^{(\varepsilon)}=x_n+\varepsilon n
\tag{2.8}
\]

is strict and superadditive.  Once the strict-clock Bellman inequality is
proved (using (2.2) or any sharper form), apply it to
\(x^{(\varepsilon)}\) and let \(\varepsilon\downarrow0\).
Continuity of \(K\) at \(A\), together with Gaussian domination of the
tail, gives the original clock inequality.  A clock with infinitely many
zero atoms has \(\mathcal B=+\infty\) and is harmless.  Thus proving the
finite prefix inequality for strict clocks proves it for the complete
anchored-window cone via the established counting-clock density theorem.

## 3. The complete finite constraints

The normalized prefix inherits

\[
 y_{i+j}\ge y_i+y_j
 \qquad(0\le i,j,\ i+j\le p),
\tag{3.1}
\]

and the crossing value obeys

\[
 b\ge y_i+y_{h-i}
 \qquad(1\le i\le p).
\tag{3.2}
\]

Put

\[
 \beta(y)=\max\left\{1,
       \max_{1\le i\le p}(y_i+y_{h-i})\right\}.
\tag{3.3}
\]

For fixed \(y\), the function \(b\mapsto\Phi_b(y)\) is strictly
decreasing: the \(q=0\) term is constant and every \(q\ge1\) term is
strictly decreasing.  Since the actual \(b\) is greater than one and at
least \(\beta(y)\), Theorem 2.1 has the following purely finite
sufficient form.

### Corollary 3.1 (a sufficient prefix-only target)

Universal Rayleigh positivity would follow from

\[
 \boxed{
 \sum_{r=0}^{p}\Phi_{\beta(y)}(y_r)\le p+1}
\tag{3.4}
\]

for every \(p\ge0\) and every finite sequence
\(0=y_0<\cdots<y_p\le1\) satisfying (3.1), with \(\Phi_1\)
interpreted as the decreasing limit
\(b\downarrow1\) when \(\beta(y)=1\).

The shifted carry constraint (3.2) is essential, but it is not sufficient.
It is only the first piece of information absent from a proof which pairs
\(y_r\) with \(y_{p-r}\); Section 6 shows that higher carries cannot be
discarded.

## 4. Exact theta defect at the false pairwise boundary

At the formal boundary \(b=1\), define

\[
 \Phi_1(y)=e^{-a(1-y)^2}
       +\sum_{n\ge1}e^{-a(n+y)^2}.
\tag{4.1}
\]

For \(0\le y\le1\), direct reindexing gives

\[
 \Phi_1(y)+\Phi_1(1-y)
 =\sum_{n\in\mathbb Z}e^{-a(n+y)^2}.
\tag{4.2}
\]

Poisson summation at \(a=\pi/4\) therefore yields

\[
 \boxed{
 \Phi_1(y)+\Phi_1(1-y)
 =2+4\sum_{m\ge1}e^{-4\pi m^2}\cos(2\pi my).}
\tag{4.3}
\]

In particular,

\[
 \Phi_1(0)+\Phi_1(1)
 =2+4\sum_{m\ge1}e^{-4\pi m^2}>2.
\tag{4.4}
\]

Thus the tempting pointwise assertion

\[
 y+z\le1
 \Longrightarrow
 \Phi_1(y)+\Phi_1(z)\le2
\tag{4.5}
\]

is false, by an exact theta amount.  This explains why the ordinary
complementary constraint

\[
 y_r+y_{p-r}\le y_p\le1
\tag{4.6}
\]

does not by itself finish the clock inequality.

The defect is exponentially small, but it is leading for the logical
argument.  The only available exact compensation in the finite block is
the strict crossing/carry datum

\[
 b>1,
 \qquad
 b\ge y_i+y_{p+1-i}.
\tag{4.7}
\]

This is precisely the datum retained in (3.4).

## 5. Equality and sharpness of the tail reduction

If a finite prefix admits the additive-periodic extension

\[
 x_{qh+r}=A(qb+y_r),
 \qquad q\ge0,\quad0\le r<h,
\tag{5.1}
\]

and that extension is superadditive, then every inequality in (2.6) is
an equality.  Consequently (2.2) is exact for that clock.

The required finite carry conditions for (5.1) are

\[
\begin{aligned}
 y_i+y_j&\le y_{i+j},&&i+j<h,\\
 y_i+y_j&\le b+y_{i+j-h},&&i+j\ge h.
\end{aligned}
\tag{5.2}
\]

Thus (2.2) is sharp on periodic Apéry clocks.  Such a clock lies on a
sharp face of the further relaxation (3.4) only when its actual period
\(b\) equals \(\beta(y)\); otherwise the monotonicity step in Section 3
is strict.

## 6. The prefix-only inequality is false

Put

\[
 \delta=\Phi_1(0)+\Phi_1(1)-2
 =4\sum_{k\ge1}e^{-4\pi k^2}>0,
 \qquad
 \gamma=\Phi_1(1)-\Phi_1(0)=1-2e^{-\pi/4}.
\tag{6.1}
\]

Choose an integer \(m\) with \(m\delta>\gamma\), set \(h=2m\), and,
for \(0<\varepsilon<1/h\), define

\[
 y_r=
 \begin{cases}
  r\varepsilon,&0\le r\le m,\\
  1-(h-r)\varepsilon,&m<r<h.
 \end{cases}
\tag{6.2}
\]

The sequence is strict, internally superadditive, and has
\(\beta(y)=1\).  As \(\varepsilon\downarrow0\), its first \(m+1\)
entries converge to zero and its last \(m-1\) entries converge to one.
Therefore

\[
 \sum_{r=0}^{h-1}\Phi_1(y_r)-h
 \longrightarrow
 (m+1)\Phi_1(0)+(m-1)\Phi_1(1)-2m
 =m\delta-\gamma>0.
\tag{6.3}
\]

This disproves (3.4).  The missing information is exactly the collection
of higher carries: in a periodic extension, two upper-cluster entries in
(6.2) force a block height close to two, while the relaxed envelope
\(qb+y_r\) continues to use block height one.

There is a sharp prefix-only replacement.  Put

\[
 v_i=y_i\quad(1\le i<h),\qquad v_h=\beta(y),
\tag{6.4}
\]

and define the max-plus partition closure

\[
 \boxed{
 L_y(n)=\max\left\{
  \sum_{i=1}^{h}c_iv_i:
  c_i\in\mathbb Z_{\ge0},\ 
  \sum_{i=1}^{h}ic_i=n
 \right\}.}
\tag{6.5}
\]

Every superadditive clock with the given prefix satisfies

\[
 {x_n\over A}\ge L_y(n).
\tag{6.6}
\]

Unlike the linear envelope \(qb+y_r\), the closure (6.5) retains every
high--high carry.  When \(\beta(y)>1\), the clock
\(x_n=A L_y(n)\) attains the resulting Gaussian-tail bound; the
\(\beta(y)=1\) face follows as a strict-crossing limit.  Thus (6.5), not
(3.4), is the lossless finite first-crossing formulation.

The proof and full audit of this correction are frozen in
`MATH_OBSTRUCTION_RAYLEIGH_SHIFTED_CARRY_THETA_INEQUALITY_20260807.md`.
The remaining continuum theorem is positivity after replacing every
later clock value by the exact max-plus closure (6.5).  This is the same
finite Apéry/Bellman gate in a sharper coordinate system; it still leaves
the discrete stability step needed for the exact PBBS coefficients.
