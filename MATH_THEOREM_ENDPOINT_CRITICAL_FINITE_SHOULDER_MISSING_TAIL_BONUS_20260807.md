# Endpoint-critical finite shoulders are exactly a missing-tail bonus

**Date:** 2026-08-07  
**Method:** pure mathematics; critical-chain layer cake and exact Gaussian
tail reindexing  
**Status:** unconditional identity and localization.  The endpoint-critical
physical Bellman functional is a direct first-block theta functional plus
one explicit nonnegative missing-tail bonus.  This does not yet prove that
the bonus always covers a possible direct-theta excess.

## 1. Endpoint-critical notation

Put

\[
 A={\sqrt\pi\over2},\qquad a=A^2={\pi\over4},
\tag{1.1}
\]

and let \(K\) be the Rayleigh kernel

\[
 K(x)=
 \begin{cases}
  1-e^{-(A-x)^2}-e^{-(A+x)^2},&0\le x\le A,\\
  -e^{-(A+x)^2},&x\ge A.
 \end{cases}
\tag{1.2}
\]

Let

\[
 0=v_0\le v_1\le\cdots\le v_n=1
\tag{1.3}
\]

be internally superadditive, and assume that the endpoint is the unique
maximum-density denomination:

\[
 {v_j\over j}<{1\over n}\qquad(1\le j<n).
\tag{1.4}
\]

Let \(L(m)\) be its max-plus Bellman closure.  Thus

\[
 L(m)=\max_{1\le j\le\min(m,n)}(v_j+L(m-j)).
\tag{1.5}
\]

Put

\[
 e_j={j\over n}-v_j>0\quad(j<n),\qquad e_n=0.
\tag{1.6}
\]

For \(0\le r<n\), let \(d_r\) be the least \(e\)-cost of a proper-step
walk whose total capacity is congruent to \(r\pmod n\), and put

\[
 s_r={r\over n}-d_r.
\tag{1.7}
\]

Then the formal Apéry clock is

\[
 W(qn+r)=q+s_r.
\tag{1.8}
\]

The exact physical defect chains are

\[
 \eta_{r,q}=W(qn+r)-L(qn+r)\ge0.
\tag{1.9}
\]

Adding one endpoint denomination gives

\[
 \eta_{r,0}\ge\eta_{r,1}\ge\cdots\ge0,
\qquad
 \eta_{r,q}=0\quad\hbox{for all sufficiently large }q.
\tag{1.10}
\]

Since the first block is already Bellman closed,

\[
 \eta_{r,0}=s_r-v_r.
\tag{1.11}
\]

For \(0\le u<\eta_{r,0}\), define

\[
 N_r(u)=\#\{q\ge0:\eta_{r,q}>u\}.
\tag{1.12}
\]

## 2. Exact endpoint derivative trains

For \(0\le z<1\) and \(N\ge1\), put

\[
 J_N(z)=\sum_{q=0}^{N-1}K'(A(q+z)).
\tag{2.1}
\]

The complete train is exactly the derivative of the theta function in
the companion theorem:

\[
 F(z)=e^{-a(1-z)^2}+\sum_{q\ge1}e^{-a(q+z)^2}.
\tag{2.2}
\]

Indeed,

\[
 \boxed{
 J_\infty(z):=\sum_{q\ge0}K'(A(q+z))
 =-{F'(z)\over A}.}
\tag{2.3}
\]

For \(q\ge1\), the argument \(A(q+z)\) is on the increasing tail of
\(K\), and hence

\[
 K'(A(q+z))=2A(q+1+z)e^{-a(q+1+z)^2}>0.
\tag{2.4}
\]

Consequently

\[
 \boxed{J_N(z)\le J_\infty(z)=-{F'(z)\over A}.}
\tag{2.5}
\]

In particular, an adverse layer \(J_N(z)>0\) is possible only where
\(F'(z)<0\).  Moreover, if \(K'(Az)\le0\), an adverse layer must have
\(N\ge2\).  This is an exact sign localization, not a numerical
approximation to the zero set.

The train itself has the closed form

\[
 \boxed{
 J_N(z)=2A\left(
 \sum_{p=1}^{N}(p+z)e^{-a(p+z)^2}
 -(1-z)e^{-a(1-z)^2}
 \right).}
\tag{2.6}
\]

## 3. Exact missing-tail identity

Let

\[
 \mathcal H
 =\sum_{m\ge0}\bigl(K(AL(m))-K(AW(m))\bigr)
\tag{3.1}
\]

be the finite availability shoulder.  The standard critical-chain
layer-cake identity, in the present normalization, is

\[
 \mathcal H
 =-A\sum_{r=0}^{n-1}
 \int_0^{\eta_{r,0}}
 J_{N_r(u)}(s_r-u)\,du.
\tag{3.2}
\]

### Theorem 3.1 (direct theta plus missing-tail bonus)

One has the exact decomposition

\[
 \boxed{
 \mathcal H
 =\sum_{r=0}^{n-1}\bigl(F(s_r)-F(v_r)\bigr)
 +\mathcal T,}
\tag{3.3}
\]

where

\[
\boxed{
\begin{aligned}
 \mathcal T
 &:=A\sum_{r=0}^{n-1}
 \int_0^{s_r-v_r}
 \sum_{q\ge N_r(u)}K'(A(q+s_r-u))\,du\\
 &=\sum_{r=0}^{n-1}\sum_{q\ge1}
 \left[
 K(AL(qn+r))-K(A(q+v_r))
 \right]
 \ge0.
\end{aligned}}
\tag{3.4}
\]

Therefore the complete physical Bellman functional is

\[
\boxed{
 \sum_{m\ge0}K(AL(m))
 =n-\sum_{r=0}^{n-1}F(v_r)+\mathcal T.}
\tag{3.5}
\]

#### Proof

At a fixed layer, split the complete train into its active prefix and
omitted tail:

\[
 J_{N_r(u)}(s_r-u)
 =J_\infty(s_r-u)
 -\sum_{q\ge N_r(u)}K'(A(q+s_r-u)).
\tag{3.6}
\]

Use (2.3) in (3.2).  Since

\[
 -A\int_0^{s_r-v_r}J_\infty(s_r-u)\,du
 =F(s_r)-F(v_r),
\tag{3.7}
\]

the first line of (3.4) and (3.3) follow.

For \(0<u<\eta_{r,0}\), the omitted indices are exactly those
\(q\ge1\) for which \(\eta_{r,q}\le u\).  Tonelli's theorem therefore
gives

\[
 \mathcal T
 =A\sum_{r=0}^{n-1}\sum_{q\ge1}
 \int_{\eta_{r,q}}^{\eta_{r,0}}
 K'(A(q+s_r-u))\,du.
\tag{3.8}
\]

Integrating and using

\[
 q+s_r-\eta_{r,q}=L(qn+r),
 \qquad
 q+s_r-\eta_{r,0}=q+v_r,
\tag{3.9}
\]

proves the second line of (3.4).  Both arguments in each bracket are at
least \(A\), and

\[
 L(qn+r)\ge q+L(r)=q+v_r
\tag{3.10}
\]

by \(q\) endpoint denominations.  The tail of \(K\) is increasing, so
every bracket is nonnegative.

Finally, the formal theorem gives

\[
 \sum_mK(AW(m))=n-\sum_rF(s_r).
\tag{3.11}
\]

Adding (3.3) proves (3.5). \(\square\)

## 4. A literal first-wrap lower bound

For \(0\le r<n\), define the largest one-wrap improvement

\[
 g_r=\max\left(
 0,
 \max_{\substack{1\le i,j<n\\i+j=n+r}}
 (v_i+v_j-1-v_r)
 \right).
\tag{4.1}
\]

Internal superadditivity prices no wrapped pairs, so \(g_r\) is exactly
the part of the first cyclic carry not already present in the displayed
table.  Bellman superadditivity gives

\[
 L(n+r)\ge1+v_r+g_r.
\tag{4.2}
\]

Keeping only \(q=1\) in (3.4) yields the unconditional bound

\[
\boxed{
 \mathcal T\ge
 \sum_{r=0}^{n-1}
 \left[
 K(A(1+v_r+g_r))-K(A(1+v_r))
 \right].}
\tag{4.3}
\]

There is a stronger whole-tail form.  Put

\[
 w_r=v_r+g_r,
 \qquad
 H_2(y)=\sum_{\ell\ge2}e^{-a(\ell+y)^2}.
\tag{4.4}
\]

The same wrapped pair, followed by \(q-1\) endpoint denominations, gives

\[
 L(qn+r)\ge q+w_r\qquad(q\ge1).
\tag{4.5}
\]

Since the tail of \(K\) is increasing, (3.4) implies

\[
\boxed{
\begin{aligned}
 \mathcal T
 &\ge\sum_{r=0}^{n-1}\sum_{q\ge1}
 \left[K(A(q+w_r))-K(A(q+v_r))\right]\\
 &=\sum_{r=0}^{n-1}\bigl(H_2(v_r)-H_2(w_r)\bigr).
\end{aligned}}
\tag{4.6}
\]

Equation (4.3) is just the \(q=1\) part of (4.6).  The whole-tail
bound is sharp when every stable improvement is already furnished by a
single wrapped binary carry.  Higher Bellman carries add further
nonnegative terms to \(\mathcal T\).

## 5. The now-exact remaining lemma

The companion cyclic theorem proves

\[
 n-\sum_rF(s_r)>{1\over2000}.
\tag{5.1}
\]

Theorem 3.1 shows why that formal reserve alone does not immediately sign
the physical head: the direct residues \(v_r\) need not obey cyclic wrap
inequalities and can satisfy \(\sum_rF(v_r)>n\).  But every such excess
must now be paid against one explicit positive scalar.

The endpoint-critical finite shoulder problem is exactly

\[
 \boxed{
 \mathcal T\ge
 \left(\sum_{r=0}^{n-1}F(v_r)-n\right)_+.}
\tag{5.2}

A stronger, purely one-wrap sufficient statement is obtained by replacing
\(\mathcal T\) with the right side of (4.6).

Thus the remaining obstruction is no longer an unsigned shoulder area or
an arbitrary family of derivative trains.  It is a correlation theorem:
show that the same wrapped superadditivity failures which create a direct
theta excess force enough first- and higher-wrap Bellman gain to pay that
excess through (3.4).

## 6. Exact scope

This note proves:

1. all adverse shoulder layers lie in the two sign regions of \(F'\);
2. low-side adverse layers require at least two unavailable tail points;
3. the complete shoulder equals a direct-theta correction plus a literal
   nonnegative missing-tail bonus;
4. the first wrapped Bellman row supplies the whole-tail lower bound
   (4.6), not merely one Gaussian term.

It does **not** prove (5.2), nor does it prove that every endpoint-critical
shoulder is nonnegative.  Cross-residue coupling in the min-plus recursion
is the remaining input.

## 7. Dependencies

1. `MATH_THEOREM_APERY_FINITE_SHOULDER_CRITICAL_CHAIN_LAYER_CAKE_REDUCTION_20260804.md`;
2. `MATH_THEOREM_ENDPOINT_CRITICAL_CYCLIC_APERY_THETA_RESERVE_20260807.md`;
3. only the exact endpoint Bellman recurrence and elementary Gaussian
   differentiation beyond those results.
