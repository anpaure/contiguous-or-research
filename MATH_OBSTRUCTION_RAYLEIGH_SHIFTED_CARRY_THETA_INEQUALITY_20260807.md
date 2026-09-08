# The first shifted carry does not absorb the Rayleigh theta defect

**Date:** 2026-08-07

**Status:** unconditional pure-mathematical counterexample to the
prefix-only shifted-carry inequality (3.4) in
MATH_THEOREM_RAYLEIGH_FIRST_CROSSING_BLOCK_THETA_REDUCTION_20260807.md.
The first-crossing tail bound remains valid.  What fails is its proposed
closure using only
\(\beta(y)=\max\{1,\max_i(y_i+y_{h-i})\}\).

## 1. Endpoint constants

Put \(a=\pi/4\) and

\[
 F(y)=\Phi_1(y)
 =e^{-a(1-y)^2}+\sum_{n\ge1}e^{-a(n+y)^2}.
\tag{1.1}
\]

The theta identity gives the strictly positive endpoint defect

\[
\boxed{
 \delta:=F(0)+F(1)-2
 =4\sum_{k\ge1}e^{-4\pi k^2}>0.}
\tag{1.2}
\]

The endpoint difference is even simpler.  Directly from (1.1),

\[
\begin{aligned}
 F(0)&=2e^{-a}+\sum_{n\ge2}e^{-an^2},\\
 F(1)&=1+\sum_{n\ge2}e^{-an^2},
\end{aligned}
\tag{1.3}
\]

and hence

\[
\boxed{
 \gamma:=F(1)-F(0)=1-2e^{-\pi/4}>0.}
\tag{1.4}
\]

Choose an integer \(m\) so large that

\[
 m\delta>\gamma.
\tag{1.5}
\]

No numerical search is involved: such an \(m\) exists because
\(\delta>0\).

## 2. A strict two-plateau prefix

Set

\[
 h=2m,\qquad p=h-1.
\tag{2.1}
\]

For \(0<\varepsilon<1/h\), define

\[
\boxed{
 y_r^{(\varepsilon)}
 =
 \begin{cases}
  r\varepsilon,&0\le r\le m,\\
  1-(h-r)\varepsilon,&m<r<h.
 \end{cases}}
\tag{2.2}
\]

This sequence is strict and satisfies

\[
 0=y_0<y_1<\cdots<y_p<1.
\tag{2.3}
\]

### Lemma 2.1 (all prefix constraints hold)

For \(i+j\le p\),

\[
 y_{i+j}\ge y_i+y_j.
\tag{2.4}
\]

Moreover,

\[
 \max_{1\le i\le p}(y_i+y_{h-i})=1,
\qquad\text{so}\qquad
\beta(y)=1.
\tag{2.5}
\]

#### Proof

If \(i,j\le m\) and \(i+j\le m\), (2.4) is an equality.  If
\(i,j\le m<i+j\), then

\[
 y_i+y_j=(i+j)\varepsilon
 \le1-(h-i-j)\varepsilon=y_{i+j},
\tag{2.6}
\]

because \(h\varepsilon<1\).  If one index is greater than \(m\) and
\(i+j<h\), the other index is at most \(m\), and the two sides of
(2.4) are equal:

\[
 1-(h-i)\varepsilon+j\varepsilon
 =1-(h-i-j)\varepsilon.
\tag{2.7}
\]

Two indices greater than \(m\) cannot have sum below \(h\).  This proves
(2.4).

For \(1\le i<m\), one member of the pair \(i,h-i\) is on each plateau,
and

\[
 y_i+y_{h-i}=i\varepsilon+(1-i\varepsilon)=1.
\tag{2.8}
\]

At \(i=m\), the sum is \(h\varepsilon<1\); the remaining cases are
symmetric.  Thus (2.5) follows. \(\square\)

## 3. Linear accumulation of the theta defect

For the prefix (2.2), the left side of the proposed inequality is

\[
 S_m(\varepsilon)
 =\sum_{r=0}^{m}F(r\varepsilon)
  +\sum_{k=1}^{m-1}F(1-k\varepsilon).
\tag{3.1}
\]

By continuity of \(F\),

\[
\begin{aligned}
 \lim_{\varepsilon\downarrow0}S_m(\varepsilon)
 &=(m+1)F(0)+(m-1)F(1),\\
 \lim_{\varepsilon\downarrow0}
   \bigl(S_m(\varepsilon)-h\bigr)
 &=m\bigl(F(0)+F(1)-2\bigr)
   -\bigl(F(1)-F(0)\bigr)\\
 &=m\delta-\gamma>0.
\end{aligned}
\tag{3.2}
\]

Therefore, for every sufficiently small positive \(\varepsilon\),

\[
\boxed{
 \sum_{r=0}^{p}\Phi_{\beta(y)}(y_r)
 =S_m(\varepsilon)>h=p+1.}
\tag{3.3}
\]

This is a strict feasible counterexample to the shifted-carry theta
inequality.

## 4. Scope of the obstruction

The exact first-crossing estimate

\[
 \mathcal B(x)\ge
 h-\sum_{r=0}^{h-1}\Phi_b(y_r)
\tag{4.1}
\]

is unaffected.  The false step is replacing the actual \(b>1\) by the
single first-carry lower bound \(\beta(y)\) and then demanding positivity
for every internally superadditive prefix.

The family (2.2) makes this failure transparent.  There are \(m-1\)
low/high pairs whose sums equal one.  Each limiting endpoint pair
contributes the positive theta defect \(\delta\), while the imbalance of
the two plateau sizes costs only the fixed amount \(\gamma\).  Hence the
defect wins linearly in \(m\).

The same prefix cannot have a nearly additive periodic continuation.
Indeed, for two high indices with \(i+j-h\le m\), the full periodic carry
condition would require

\[
 b\ge y_i+y_j-y_{i+j-h}=2-h\varepsilon,
\tag{4.2}
\]

not merely \(b\ge\beta(y)=1\).  A true nonperiodic clock may instead
absorb these high/high sums by making its second block much larger, but
then the Gaussian tail in (4.1) is strictly smaller than the
\(\beta\)-majorant.

Thus a valid finite closure must retain additional second-block
information or charge the superadditivity gaps created by high/high
shifted carries.  The first carry parameter \(\beta(y)\) alone is
provably insufficient.

## 5. A lossless repair by max-plus closure

There is an exact prefix-only replacement for the failed
\(\Phi_\beta\) majorant.  It retains all additive decompositions generated
by the first block.

For a feasible prefix \(y_0,\ldots,y_{h-1}\), put

\[
 v_i=y_i\quad(1\le i<h),\qquad v_h=\beta(y),
\tag{5.1}
\]

and define its max-plus partition closure by

\[
\boxed{
 L_y(n)=
 \max_{\substack{c_1,\ldots,c_h\in\mathbb Z_{\ge0}\\
                  \sum_{i=1}^{h}ic_i=n}}
       \sum_{i=1}^{h}c_i v_i.}
\tag{5.2}
\]

### Theorem 5.1 (sharp max-plus first-block bound)

Every strict superadditive clock having normalized prefix \(y\) satisfies

\[
\boxed{
 \mathcal B(x)\ge
 h-\sum_{r=0}^{h-1}e^{-a(1-y_r)^2}
   -\sum_{n\ge0}e^{-a(1+L_y(n))^2}.}
\tag{5.3}
\]

For \(\beta(y)>1\), equality is attained by the clock
\(x_n=A L_y(n)\).  For \(\beta(y)=1\), the right side is the limit of
Bellman functionals of strict first-crossing clocks with the same prefix.

#### Proof

First,

\[
 L_y(n)=y_n\quad(0\le n<h),\qquad L_y(h)=\beta(y).
\tag{5.4}
\]

For \(n<h\), internal superadditivity says that the weight of every
partition of \(n\) is at most \(y_n\), while the one-part partition
attains \(y_n\).  For a partition of \(h\) not using the part \(h\),
separate one part \(i\).  The remaining parts have total size \(h-i<h\)
and weight at most \(y_{h-i}\), so their total weight is at most
\(y_i+y_{h-i}\le\beta(y)\).  The one-part partition \(h\) attains
\(\beta(y)\).

Combining maximizing partitions shows

\[
 L_y(m+n)\ge L_y(m)+L_y(n).
\tag{5.5}
\]

Also \(L_y(n+1)\ge L_y(n)+y_1>L_y(n)\).  Thus \(A L_y(n)\) is a strict
superadditive clock and has the desired prefix.

For an arbitrary clock with actual crossing value \(b\ge\beta(y)\),
superadditivity applied to every partition in (5.2) gives

\[
 {x_n\over A}\ge L_y(n).
\tag{5.6}
\]

The Gaussian is decreasing on the nonnegative line, so inserting (5.6)
in the exact first-crossing identity proves (5.3).

If \(\beta(y)>1\), (5.4)--(5.5) show that \(A L_y\) itself is a
first-crossing clock and every inequality above is an equality.  If
\(\beta(y)=1\), replace \(v_h\) in (5.1) by \(1+\eta\), take the
corresponding max-plus closure \(L_{y,\eta}\), and let
\(\eta\downarrow0\).  Pointwise convergence and the bound
\(L_{y,\eta}(n)\ge ny_1\) give Gaussian dominated convergence. \(\square\)

The old block estimate keeps only the particular partitions
\(n=qh+r\):

\[
 L_y(qh+r)\ge q\beta(y)+y_r.
\tag{5.7}
\]

Replacing the full maximum (5.2) by (5.7) produces exactly the
\(\Phi_{\beta(y)}\) tail and discards all competing high-density parts.
The two-plateau counterexample exploits that discarded max-plus growth.
Thus (5.3), rather than (3.4), is the sharp first-block formulation.
