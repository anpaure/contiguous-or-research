# One cheap top step has an exact delayed-wrap clock and a sharp positive asymptotic reserve

**Date:** 2026-08-07  
**Status:** unconditional pure mathematics.  The endpoint-critical family
with linear costs below the top proper denomination and one cheaper
\((n-1)\)-step is solved exactly.  Its finite shoulder can be negative, but
its complete Bellman functional has a sharp, uniformly positive
large-\(n\) lower limit.  Thus this natural one-wrap family cannot furnish
a total counterexample.

## 1. Family and parameters

Put

\[
 A={\sqrt\pi\over2},\qquad a=A^2={\pi\over4},
\tag{1.1}
\]

and let \(K\) be the Rayleigh signed-tail kernel

\[
 K(Ay)=
 \begin{cases}
  1-e^{-a(1-y)^2}-e^{-a(1+y)^2},&0\le y\le1,\\
  -e^{-a(1+y)^2},&y\ge1.
 \end{cases}
\tag{1.2}
\]

Fix \(n\ge3\), \(0<\alpha<1/n\), and

\[
 0<\beta\le n-1.
\tag{1.3}
\]

Define endpoint costs

\[
 e_j=
 \begin{cases}
  \alpha j,&1\le j\le n-2,\\
  \alpha\beta,&j=n-1,\\
  0,&j=n,
 \end{cases}
\tag{1.4}
\]

and \(v_j=j/n-e_j\).  It is convenient to put

\[
 x=n\alpha\in(0,1).
\tag{1.5}
\]

The table is internally superadditive.  Indeed, sums below \(n-1\) are
linear; at \(i+j=n-1\), the required inequality is precisely
\(\beta\le n-1\); and all pairs summing to \(n\) lie below the endpoint.
All proper densities are strictly below \(1/n\), so \(n\) is the unique
maximum-density denomination.  The table is strictly increasing throughout
\(0<\beta\le n-1\); the limiting case \(\beta=n-1\) is the completely
linear proper table.

Let

\[
 \delta(m)=\min_{\sum_{j=1}^n jx_j=m}\sum_{j=1}^n e_jx_j,
 \qquad
 L(m)={m\over n}-\delta(m)
\tag{1.6}
\]

be the physical min-plus cost and max-plus clock.

## 2. Exact cyclic cost and delayed availability

For \(0\le r<n\), let \(d_r\) be the least proper-step cost in residue
\(r\pmod n\).

### Theorem 2.1 (exact cyclic metric)

For every \(0\le r<n\),

\[
 \boxed{d_r=\alpha\min\{r,\beta(n-r)\}.}
\tag{2.1}
\]

#### Proof

In a proper-step walk, let \(\ell\) be the number of
\((n-1)\)-steps and let \(t\) be the total capacity supplied by steps at
most \(n-2\).  The normalized cost is

\[
 {\operatorname{cost}\over\alpha}=t+\beta\ell,
\tag{2.2}
\]

and the residue is \(t-\ell\pmod n\).  Conversely every \(t\ge0\) is
available, using denomination \(1\).  Write

\[
 t-\ell=r+nz.
\tag{2.3}
\]

If \(z\ge0\), then \(t+\beta\ell\ge r\).  If \(z\le-1\), put
\(h=-z\).  Then \(\ell-t=nh-r\ge n-r\), and

\[
 t+\beta\ell\ge\beta(n-r).
\tag{2.4}
\]

The two bounds are attained by \((t,\ell)=(r,0)\) and
\((0,n-r)\), respectively.  \(\square\)

Write \(r=n-k\).  A genuine cyclic shortcut occurs exactly when

\[
 2\le k,\qquad (\beta+1)k<n.
\tag{2.5}
\]

For such a \(k\), define

\[
 v_k=(1-x)\left(1-{k\over n}\right),
 \qquad
 s_k=1-{(1+\beta x)k\over n}.
\tag{2.6}
\]

Here \(v_k=v_{n-k}\) is the direct first-row phase and
\(s_k=(n-k)/n-d_{n-k}\) is the stable cyclic phase.  Their gap is

\[
 s_k-v_k
 =x\left(1-{(\beta+1)k\over n}\right)>0.
\tag{2.7}
\]

### Theorem 2.2 (one sharp availability time)

For a shortcut residue \(r=n-k\),

\[
 \boxed{
 \delta(qn+n-k)=
 \begin{cases}
  \alpha(n-k),&0\le q\le k-2,\\
  \alpha\beta k,&q\ge k-1.
 \end{cases}}
\tag{2.8}
\]

Every nonspecial residue has \(\delta(qn+r)=d_r\) in every row.

#### Proof

Consider a physical partition of \(qn+r\).  After discarding its endpoint
parts, suppose the remaining proper capacity is \(r+nw\), where
\(0\le w\le q\).  Maximizing the number of cheap \((n-1)\)-steps gives

\[
 \ell_{\max}
 =\left\lfloor{r+nw\over n-1}\right\rfloor
 =w+\left\lfloor{r+w\over n-1}\right\rfloor.
\tag{2.9}
\]

For \(r=n-k\) and \(0\le w\le k-2\), the last floor is zero.  The
maximally cheap path therefore has \(\ell=w\), residual small-step
capacity \(t=r+w\), and cost

\[
 \alpha\{r+(\beta+1)w\}\ge\alpha r.
\tag{2.10}
\]

Thus no improvement is available before row \(k-1\).  At \(w=k-1\), the
last floor becomes one: \(\ell=k,t=0\), so \(k\) copies of denomination
\(n-1\) realize the stable cost \(\alpha\beta k\).  Adding endpoints
keeps this path available forever.  The cyclic lower bound (2.1) proves
optimality.  If (2.5) fails, the direct path already realizes the cyclic
minimum in row zero.  \(\square\)

## 3. Exact complete functional

Define the period-one Rayleigh train

\[
 \Psi(y)=\sum_{q\ge0}K(A(q+y)),
 \qquad 0\le y\le1.
\tag{3.1}
\]

For the special direct residue \(n-1\), put

\[
 u=1-{1+\beta x\over n}.
\tag{3.2}
\]

Let

\[
 {\cal K}_{n,\beta}
 =\{k\in\mathbb Z:2\le k,\;(\beta+1)k<n\}.
\tag{3.3}
\]

### Theorem 3.1 (direct grid plus a nonnegative delayed-tail correction)

The complete Bellman functional

\[
 Q_{n,x,\beta}=\sum_{m\ge0}K(AL(m))
\tag{3.4}
\]

has the exact form

\[
 \boxed{
 Q_{n,x,\beta}=D_{n,x,\beta}+T_{n,x,\beta},}
\tag{3.5}
\]

where

\[
 \boxed{
 D_{n,x,\beta}
 =\sum_{r=0}^{n-2}\Psi\!\left((1-x){r\over n}\right)
  +\Psi(u),}
\tag{3.6}
\]

and

\[
 \boxed{
 T_{n,x,\beta}
 =\sum_{k\in{\cal K}_{n,\beta}}\sum_{q\ge k-1}
 \left[
  K(A(q+s_k))-K(A(q+v_k))
 \right]\ge0.}
\tag{3.7}
\]

Moreover,

\[
 0\le T_{n,x,\beta}
 \le \sum_{q\ge1}q\,e^{-a(q+1)^2}<\infty
\tag{3.8}
\]

uniformly in all parameters.

#### Proof

For a shortcut \(k\), Theorem 2.2 says that rows
\(0,\ldots,k-2\) use phase \(v_k\), while every later row uses phase
\(s_k\).  Starting from the complete direct train \(\Psi(v_k)\) therefore
produces exactly the correction in (3.7).  All other residues keep their
direct phase in every row, proving (3.5)--(3.7).

Every corrected row has \(q\ge k-1\ge1\), hence lies on the increasing
Gaussian tail of \(K\).  Equation (2.7) proves each bracket nonnegative.
Also the bracket is at most the absolute value of its earlier tail term,
which is at most \(e^{-a(q+1)^2}\).  For fixed \(q\), at most \(q\)
integers \(k\ge2\) satisfy \(k-1\le q\).  This proves (3.8).
\(\square\)

The negative one-state shoulder in
MATH_COUNTEREXAMPLE_ENDPOINT_CRITICAL_FINITE_APERY_SHOULDER_NEGATIVE_20260807.md
is the instance \(n=20,\beta=6,x=1/1000\).  Formula (3.7) shows the
separate positive tail correction which remains after that negative
formal-versus-physical shoulder is recombined with the direct train.

## 4. The continuum scalar at period \(A\) is positive

Put

\[
 G(x)=\int_0^1\Psi((1-x)t)\,dt
 ={1\over1-x}\int_0^{1-x}\Psi(y)\,dy
 \qquad(0\le x<1),
\tag{4.1}
\]

and set \(G(1)=\Psi(0)\).

The exact Jacobi reflection identity for the threshold-period train is

\[
 \Psi(y)+\Psi(1-y)=\rho(y),
\tag{4.2}
\]

where

\[
 \rho(y)=-4\sum_{\ell\ge1}e^{-4\pi\ell^2}\cos(2\pi\ell y).
\tag{4.3}
\]

The authenticated compact-train theorem gives

\[
 \Psi(y)>0\qquad(0\le y\le1/2).
\tag{4.4}
\]

### Lemma 4.1 (integrated reflection error has the favorable sign)

For \(0<z<1/2\),

\[
 \boxed{\int_0^z\rho(y)\,dy<0.}
\tag{4.5}
\]

#### Proof

Put \(\theta=2\pi z\in(0,\pi)\).  Integration of (4.3) gives

\[
 \int_0^z\rho(y)\,dy
 =-{2\over\pi}\sum_{\ell\ge1}
 {e^{-4\pi\ell^2}\over\ell}\sin(\ell\theta).
\tag{4.6}
\]

For \(0\le\theta\le\pi\),
\(\lvert\sin(\ell\theta)\rvert\le\ell\sin\theta\).  Hence the sum in
(4.6) is at least

\[
 \sin\theta\left(
 e^{-4\pi}-\sum_{\ell\ge2}e^{-4\pi\ell^2}
 \right)>0.
\tag{4.7}
\]

For the last inequality, use
\(\ell^2\ge1+3(\ell-1)\) for \(\ell\ge2\) and sum the resulting geometric
tail.  Equation (4.6) now proves the claim.  \(\square\)

### Theorem 4.2 (strict period-\(A\) duty-cycle positivity)

For every \(0<x\le1\),

\[
 \boxed{G(x)>0.}
\tag{4.8}
\]

Also

\[
 G(0)=0,\qquad
 G'(0)=-\Psi(1)=K(0)-\Psi(0)
 =\sum_{p\ge2}e^{-ap^2}>0.
\tag{4.9}
\]

#### Proof

Write \(h=1-x\).  If \(0<h\le1/2\), (4.4) directly gives
\(\int_0^h\Psi>0\).  If \(1/2<h<1\), put \(z=1-h<1/2\).  Since

\[
 \int_0^1\Psi(y)\,dy
 ={1\over A}\int_0^\infty K(w)\,dw=0,
\tag{4.10}
\]

reflection gives

\[
 \begin{aligned}
 \int_0^h\Psi(y)\,dy
 &=-\int_h^1\Psi(y)\,dy\\
 &=\int_0^z\{\Psi(y)-\rho(y)\}\,dy>0
 \end{aligned}
\tag{4.11}
\]

by (4.4) and Lemma 4.1.  This proves (4.8); the endpoint \(x=1\) follows
from \(\Psi(0)>0\).

Finally differentiate (4.1) at zero, use (4.10), and reindex the train:

\[
 \Psi(1)=\Psi(0)-K(0)
 =-\sum_{p\ge2}e^{-ap^2}.
\tag{4.12}
\]

This proves (4.9).  \(\square\)

Thus the continuum scalar controlling the family is not merely
nonnegative: it leaves zero with a strictly positive slope and stays
strictly positive throughout the open duty-cycle interval.

## 5. Uniform macroscopic asymptotics

### Theorem 5.1

Uniformly for \(0<x<1\) and \(0<\beta\le n-1\),

\[
 \boxed{Q_{n,x,\beta}=nG(x)+O(1),}
\tag{5.1}
\]

where the absolute \(O(1)\) constant is independent of \(n,x,\beta\).
Consequently, for every fixed \(\varepsilon>0\),

\[
 \inf_{\substack{\varepsilon\le x<1\\0<\beta\le n-1}}
 Q_{n,x,\beta}\longrightarrow+\infty.
\tag{5.2}
\]

#### Proof

The full left grid

\[
 \sum_{r=0}^{n-1}\Psi((1-x)r/n)
\tag{5.3}
\]

differs from \(nG(x)\) by at most the total variation of \(\Psi\) on
\([0,1]\).  Formula (3.6) replaces only its last term by another value of
\(\Psi\), so \(D_{n,x,\beta}=nG(x)+O(1)\) uniformly.  The correction
\(T\) is uniformly bounded by (3.8), proving (5.1).

On the compact interval \([\varepsilon,1]\), Theorem 4.2 and continuity
give a positive minimum for \(G\).  Equation (5.2) follows.  \(\square\)

## 6. The only low-energy scaling and its exact limit

Put

\[
 M=K(0)=1-2e^{-\pi/4},
\qquad
 c_*={M\over2}={1\over2}-e^{-\pi/4}.
\tag{6.1}
\]

### Theorem 6.1 (boundary-layer limit)

Let \(n\to\infty\), allow any \(0<\beta_n\le n-1\), and suppose

\[
 nx_n\longrightarrow\xi\in[0,\infty).
\tag{6.2}
\]

Then

\[
 \boxed{
 Q_{n,x_n,\beta_n}
 \longrightarrow
 c_*+\xi\{K(0)-\Psi(0)\}
 =c_*+\xi\sum_{p\ge2}e^{-ap^2}>0.}
\tag{6.3}
\]

#### Proof

At \(x=0\), residue reindexing gives the arithmetic comb

\[
 B_n:=\sum_{r=0}^{n-1}\Psi(r/n)
 =\sum_{m\ge0}K(Am/n),
\tag{6.4}
\]

and the small-mesh comb limit is \(B_n\to K(0)/2=c_*\).

Compare (3.6) with (6.4).  For \(0\le r\le n-2\), Taylor's theorem,
uniformly on \([0,1]\), gives

\[
 \Psi((1-x_n)r/n)-\Psi(r/n)
 =-x_n{r\over n}\Psi'(r/n)+O(x_n^2).
\tag{6.5}
\]

After summation, the error is \(O(nx_n^2)=o(1)\), and

\[
 -x_n\sum_{r=0}^{n-2}{r\over n}\Psi'(r/n)
 \longrightarrow
 -\xi\int_0^1y\Psi'(y)\,dy
 =-\xi\Psi(1).
\tag{6.6}
\]

The special last phase differs from \((n-1)/n\) by

\[
 -{\beta_nx_n\over n},
\tag{6.7}
\]

whose absolute value is at most \(x_n=o(1)\); hence its train difference
vanishes.

For each shortcut, (2.7) bounds the phase displacement by \(x_n\).
The mean-value theorem on the Gaussian tail, summed as in (3.8), gives

\[
 0\le T_{n,x_n,\beta_n}
 \le Cx_n\longrightarrow0
\tag{6.8}
\]

for an absolute \(C\).  Combine (6.4)--(6.8) with (4.9).  \(\square\)

### Corollary 6.2 (sharp asymptotic lower envelope)

\[
 \boxed{
 \lim_{n\to\infty}
 \inf_{\substack{0<x<1\\0<\beta\le n-1}}
 Q_{n,x,\beta}
 =c_*={1\over2}-e^{-\pi/4}>0.}
\tag{6.9}
\]

In particular, the entire one-cheap-\((n-1)\) family is uniformly
positive for all sufficiently large \(n\).

#### Proof

Take any parameter sequence.  If \(x\) stays bounded away from zero,
Theorem 5.1 sends \(Q\) to \(+\infty\).  Suppose \(x\to0\).  From
(4.9), \(G(x)\ge\frac12\{K(0)-\Psi(0)\}x\) for all sufficiently small
\(x\).  If \(nx\to\infty\), (5.1) again sends \(Q\) to \(+\infty\).
If \(nx\) is bounded, pass to a convergent subsequence and apply
Theorem 6.1; every resulting limit is at least \(c_*\).

Conversely, choose any \(\beta_n\) and any positive \(x_n=o(1/n)\).
Theorem 6.1 with \(\xi=0\) gives \(Q\to c_*\).  This proves (6.9).
\(\square\)

## 7. Consequence

The cheapest possible total values in this family occur not at a
macroscopic wrapped shortcut, nor at the negative-shoulder example, but
in the degenerate nearly uniform limit \(x=o(1/n)\).  Their sharp limit is
the positive half-kernel mass \(c_*\).

Therefore the one-cheap-top-step ansatz is a genuine no-go for constructing
a total endpoint-critical counterexample.  It also shows exactly why the
negative finite shoulder is harmless here: every fixed-density
deformation creates a linear period-\(A\) duty-cycle reserve, while the
only scaling which keeps the total \(O(1)\) converges to the strictly
positive arithmetic-comb constant.

## 8. Dependencies

1. the compact threshold-train positivity
   \(\Psi(y)>0\) on \(0\le y\le1/2\), frozen in
   MATH_THEOREM_APERY_LONG_WRAP_EUCLIDEAN_SHIFT_AND_THETA_RESIDUAL_20260804.md;
2. the exact Jacobi reflection identity in
   MATH_THEOREM_FIVE_SLOT_REPEATED_GAP_EXACT_THETA_ENDPOINT_DESCENT_20260804.md;
3. the all-mesh arithmetic-comb theorem and its small-mesh limit in
   MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md.
