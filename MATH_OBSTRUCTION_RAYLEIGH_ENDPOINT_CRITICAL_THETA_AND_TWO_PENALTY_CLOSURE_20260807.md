# Endpoint criticality does not save the direct theta bound; max-plus carry gives an exact positive repair

**Date:** 2026-08-07

**Status:** unconditional pure mathematics.  The direct first-period
theta majorization is false even when the threshold endpoint is the
unique maximum-density denomination.  A fully strict counterfamily is
given.  Its exact max-plus clock is computed: after one finite shoulder
it is a period-\(n\) train with two residue penalties.  In the same
parameter regime which defeats the relaxed theta bound, this exact
Bellman clock is strictly positive.  The complete endpoint-critical
branch remains open, but its exact remaining scalar is isolated in
Section 5.

## 1. Two local signs and the uniform root sum

Put

\[
 A={\sqrt\pi\over2},\qquad a=A^2={\pi\over4},
\tag{1.1}
\]

and define

\[
 F(y)=\Phi_1(y)
 =e^{-a(1-y)^2}+\sum_{\ell\ge1}e^{-a(\ell+y)^2}.
\tag{1.2}
\]

At zero,

\[
\begin{aligned}
 F'(0)
 &=2ae^{-a}-2a\sum_{\ell\ge1}\ell e^{-a\ell^2}\\
 &=-2a\sum_{\ell\ge2}\ell e^{-a\ell^2}<0.
\end{aligned}
\tag{1.3}
\]

Also the normalized compact kernel

\[
 k(y):=K(Ay)
 =1-e^{-a(1-y)^2}-e^{-a(1+y)^2}
\tag{1.4}
\]

satisfies

\[
 k''(0)=-4a(2a-1)e^{-a}<0.
\tag{1.5}
\]

Choose \(c\in(0,1/2)\) so small that

\[
 F(t)<F(0),\qquad k(t)<k(0)
 \qquad(0<t\le c).
\tag{1.6}
\]

Then

\[
 D(c):=cF(0)-\int_0^cF(t)\,dt>0.
\tag{1.7}
\]

For the uniform \(n\)-grid, direct reindexing and Poisson summation give

\[
\boxed{
 U_n:=\sum_{j=0}^{n-1}F(j/n)
 =n-\frac12+e^{-a}
  +2n\sum_{\ell\ge1}e^{-4\pi n^2\ell^2}.}
\tag{1.8}
\]

In particular, with

\[
 c_*=\frac12-e^{-a}>0,
\tag{1.9}
\]

one has \(U_n>n-c_*\).

## 2. A strict endpoint-critical counterfamily

Choose \(n\) so large, and put \(k=\lfloor cn\rfloor\), that

\[
 1\le k,\qquad 2k+1<n,
\tag{2.1}
\]

and

\[
 G_{n,k}:=
 \sum_{j=1}^{k}\bigl(F(0)-F(j/n)\bigr)>c_*.
\tag{2.2}
\]

Such \(n\) exist because

\[
 {G_{n,\lfloor cn\rfloor}\over n}\longrightarrow D(c)>0.
\tag{2.3}
\]

For \(0<\tau<1/(3n)\), define

\[
\boxed{
 v_0=0,\qquad v_n=1,\qquad
 v_j=
 \begin{cases}
  \tau j,&1\le j\le k,\\
  j/n-\tau,&k<j<n.
 \end{cases}}
\tag{2.4}
\]

### Lemma 2.1 (strict endpoint-critical feasibility)

For all sufficiently small \(\tau>0\), the table (2.4) is strictly
increasing and internally superadditive.  Moreover,

\[
 {v_j\over j}<{1\over n}={v_n\over n}
 \qquad(1\le j<n).
\tag{2.5}
\]

Thus the endpoint \(n\) is the unique maximum-density denomination,
and its saturated value is exactly one.

#### Proof

The density inequalities in (2.5) are immediate:
the lower block has density \(\tau<1/n\), while an upper entry has
density \(1/n-\tau/j\).

Strict increase holds inside each block.  At the join it is

\[
 \tau k<(k+1)/n-\tau,
\tag{2.6}
\]

which holds for sufficiently small \(\tau\).

Take \(i+j\le n\).  If \(i,j,i+j\le k\), superadditivity is an equality.
If \(i,j\le k<i+j<n\), it is enough that

\[
 {i+j\over n}-\tau\ge\tau(i+j),
\tag{2.7}
\]

which follows from \(\tau<1/(3n)\).  If exactly one summand is in the
upper block and \(i+j<n\), the desired inequality reduces to
\(\tau\le1/n\).  If both are in the upper block and \(i+j<n\), the
left side pays one setup penalty \(\tau\), while the right side pays two.
Finally, when \(i+j=n\), every lower pair has total value at most one by
the same formulas.  This proves internal superadditivity.

The best lower partition of \(n\) equals
\(\max_i(v_i+v_{n-i})\le1\), so endpoint saturation is the threshold
value one. \(\square\)

### Theorem 2.2 (the direct endpoint theta inequality is false)

For every sufficiently small positive \(\tau\),

\[
\boxed{
 \sum_{j=0}^{n-1}F(v_j)>n.}
\tag{2.8}
\]

#### Proof

As \(\tau\downarrow0\), the left side tends to

\[
\begin{aligned}
 (k+1)F(0)+\sum_{j=k+1}^{n-1}F(j/n)
 &=U_n+G_{n,k}\\
 &>n-c_*+c_*=n.
\end{aligned}
\tag{2.9}
\]

The sum is finite and continuous in \(\tau\), proving (2.8). \(\square\)

Thus neither the coordinate bounds \(v_j<j/n\), their induced
prefix-sum majorization, nor internal superadditivity suffices to compare
the direct residues with the uniform theta grid.

## 3. Exact max-plus closure

Let

\[
 L_\tau(m)=
 \max_{\substack{x\in\mathbb Z_{\ge0}^{n}\\
                  \sum_{j=1}^{n}jx_j=m}}
       \sum_{j=1}^{n}v_jx_j.
\tag{3.1}
\]

Put

\[
 \Delta={1\over n}-\tau>2\tau.
\tag{3.2}
\]

A lower-block part of size \(j\le k\) has reward
\(j/n-\Delta j\); an upper-block part \(k<j<n\) has reward
\(j/n-\tau\); and an endpoint part has reward \(n/n\).
Therefore every partition of \(m\) has reward

\[
 {m\over n}-\Delta\,\ell-\tau t,
\tag{3.3}
\]

where \(\ell\) is the total ordinary length carried by lower-block parts
and \(t\) is the number of nonendpoint upper-block parts.

### Theorem 3.1 (one shoulder and two residue penalties)

For \(0\le m<n\),

\[
 L_\tau(m)=v_m.
\tag{3.4}
\]

For \(m=qn+r\) with \(q\ge1\) and \(0\le r<n\),

\[
\boxed{
 L_\tau(qn+r)=q+{r\over n}-
 \begin{cases}
  0,&r=0,\\
  2\tau,&1\le r\le k,\\
  \tau,&k<r<n.
 \end{cases}}
\tag{3.5}
\]

#### Proof

Equation (3.4) follows from internal superadditivity.

For \(r=0\), \(q\) endpoint parts attain reward \(q\), which is optimal
by the maximum-density bound.

For \(k<r<n\), use \(q\) endpoint parts and one size-\(r\) upper part.
This has deficit \(\tau\).  Every nonendpoint exact fill of a nonzero
residue uses either a lower length, costing at least
\(\Delta>2\tau>\tau\), or at least one upper part, costing at least
\(\tau\).  Hence the deficit is exactly \(\tau\).

Let \(1\le r\le k\).  Since \(2k+1<n\), the two sizes

\[
 k+1,\qquad n+r-k-1
\tag{3.6}
\]

both lie in the upper block and sum to \(n+r\).  Together with
\(q-1\) endpoints they attain deficit \(2\tau\).  A partition of smaller
deficit cannot use a lower part, because every positive lower length
costs at least \(\Delta>2\tau\).  It would therefore use at most one
upper part.  One upper size has residue strictly larger than \(k\), so
it cannot fill residue \(r\).  Thus deficit \(2\tau\) is optimal.
\(\square\)

The exact clock is not a two-denomination train.  Every upper
denomination is indispensable at its own capacity: replacing its
one-penalty value requires either a lower loss or at least two upper
penalties.  What becomes periodic is the clock after its first block,
not the generator support.

## 4. The exact clock passes in the no-go regime

Let

\[
 \mathcal Q_n(\tau)=\sum_{m\ge0}K\!\left(A L_\tau(m)\right).
\tag{4.1}
\]

At \(\tau=0\), Theorem 3.1 gives

\[
 L_0(m)=
 \begin{cases}
  0,&1\le m\le k,\\
  m/n,&m=0\text{ or }m>k.
 \end{cases}
\tag{4.2}
\]

Consequently

\[
\boxed{
 \mathcal Q_n(0)
 =C(A/n)+\sum_{j=1}^{k}\bigl(K(0)-K(Aj/n)\bigr)>0,}
\tag{4.3}
\]

where \(C(A/n)=\sum_{m\ge0}K(Am/n)>0\) is the proved
reciprocal-ceiling sum.  The last inequality uses \(j/n\le c\) and
(1.6).

For every \(\tau\), the endpoint generator gives

\[
 L_\tau(m)\ge\lfloor m/n\rfloor.
\tag{4.4}
\]

Thus the Gaussian tail has a summable majorant independent of small
\(\tau\).  Equations (3.4)--(3.5) also give pointwise convergence
\(L_\tau(m)\to L_0(m)\).  Dominated convergence now yields

\[
 \mathcal Q_n(\tau)\longrightarrow\mathcal Q_n(0)>0.
\tag{4.5}
\]

Combining (2.8) and (4.5), the same sufficiently small strict
\(\tau>0\) satisfies

\[
\boxed{
 \sum_{j<n}\Phi_1(v_j)>n,
 \qquad
 \sum_{m\ge0}K(A L_\tau(m))>0.}
\tag{4.6}
\]

The first-carry theta relaxation fails, but the exact endpoint-critical
clock passes strictly.

## 5. The exact remaining endpoint-critical scalar

Let \(v_0,\ldots,v_n\) be an arbitrary normalized endpoint-critical
table:

\[
 v_n=1,\qquad {v_j\over j}<{1\over n}\quad(j<n).
\tag{5.1}
\]

Put

\[
 e_j={j\over n}-v_j>0\quad(j<n),\qquad e_n=0.
\tag{5.2}
\]

Internal superadditivity of \(v\) is exactly

\[
 e_{i+j}\le e_i+e_j\qquad(i+j\le n).
\tag{5.3}
\]

If

\[
 \delta_e(m)=
 \min_{\substack{x\in\mathbb Z_{\ge0}^{n}\\
                  \sum_{j=1}^{n}jx_j=m}}
       \sum_{j=1}^{n}e_jx_j,
\tag{5.4}
\]

then the max-plus clock has the exact deficit form

\[
\boxed{
 L(m)={m\over n}-\delta_e(m).}
\tag{5.5}
\]

Thus every carry is a shortest path for the positive subadditive cost
table \(e\); replacing \(L(qn+r)\) by \(q+v_r\) amounts to keeping only
the direct residue path.

The unique critical denomination is \(n\), so the critical gcd is \(n\)
and the formal Apéry period is one.
For \(0\le r<n\), define

\[
 d_r=
 \min_{\substack{x\in\mathbb Z_{\ge0}^{n-1}\\
                  \sum_{j<n}jx_j\equiv r\pmod n}}
       \sum_{j<n}e_jx_j,
 \qquad
 s_r={r\over n}-d_r.
\tag{5.6}
\]

Then

\[
 W_{qn+r}=q+s_r
\tag{5.7}
\]

is the formal Apéry clock,

\[
 0\le L(m)\le W_m,\qquad
 L(m)=W_m\quad(m\ge H),\qquad H=n(n-1),
\tag{5.8}
\]

and \(0\le s_r<1\).  Since

\[
 \sum_{q\ge0}K(A(q+s))=1-F(s)
 \qquad(0\le s<1),
\tag{5.9}
\]

the endpoint-critical Bellman functional has the exact form

\[
\boxed{
\begin{aligned}
 \sum_{m\ge0}K(A L(m))
 ={}&n-\sum_{r=0}^{n-1}F(s_r)\\
 &+\sum_{m=0}^{H-1}
   \bigl(K(A L(m))-K(AW_m)\bigr).
\end{aligned}}
\tag{5.10}
\]

Thus the complete branch is reduced to one periodic theta reserve plus
one finite, availability-coupled shoulder.  The direct-residue
substitution \(s_r\mapsto v_r\) is invalid by Theorem 2.2.  Any proof of
the endpoint-critical branch must control the Apéry-improved shifts and
the finite shoulder together; neither term can be dropped.
