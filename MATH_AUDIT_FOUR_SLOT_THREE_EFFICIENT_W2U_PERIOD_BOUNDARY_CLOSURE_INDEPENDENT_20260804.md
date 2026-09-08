# Independent audit: closure of the three-efficient `w=2u` face

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_W2U_PERIOD_BOUNDARY_CLOSURE_20260804.md`  
**Audited theorem SHA-256:**
`64451d508cc73c5ac5baf04bd749695358eea7fffb3d4c93a8c5eafa8c3bfae1`  
**Verdict:** **PASS.**  The proof retains the adverse tail pulse and closes
the complete `w=2u` face.  No search, solver, H100 computation, or
floating-point sign decision was used.

## 1. Current dependency binding

The proof-safe current inputs used in this replay are

\[
\begin{array}{c|l}
\text{input}&\text{SHA-256}\\ \hline
\text{three-efficient pulse and period theorem}
&0b46d0b2e073cc9eab4171198e2b4686ce08ef055887fd3f72cd0a506cdfef35\\
\text{threshold-surface theorem}
&7e1a12d5cce9a16b6fd9a1b65d7d9d625d114c5b8810fa7f2d6baf95bfed722b\\
\text{four-efficient scalar closure}
&2b334fc6670ec73d4eba0f9de7a211b5e64f38a77f205ee822bebc4f3a79e776\\
\text{all-grid first-crossing theorem}
&72e532231483e7d107ac103097a0507aea56afe09ca865dc743df153bdc597b1.
\end{array}
\]

The earlier audit table cites the pre-edit pulse-theorem hash
`b620128f...`.  The present audit binds and checks the current
`0b46d0b...` file directly, in particular its Theorem 2.3.  This is a
provenance correction only; it does not change a mathematical claim.

## 2. Exact normal form and pulse orientation

The general three-efficient normal form is

\[
 \mathcal B_4=\mathcal L_3(z;u,w)
 +K(x)-K(u)+K(y)-K(w)+K(z+v)-K(z+w),
\]

where

\[
 u=T-z,qquad w=\max(y,2u),qquad v=\max(y,u+x).
\]

On `w=2u` this becomes exactly

\[
 \mathcal L_3(z;u,2u)+K(x)-K(u)+K(y)-K(2u)
 +K(z+v)-K(z+2u).
\]

The inherited inequalities give

\[
 x\le u,qquad y\le2u,qquad u\le v\le2u.
\]

Thus the last difference is the occurrence-labelled interval
`sigma([z+v,z+2u))`.  Both endpoints are in the Gaussian tail, and the
interval generally has negative signed mass.  The audited proof keeps it;
it is not dropped as nonnegative.

## 3. Feasible descent interval

In first-crossing form,

\[
 x,y,z<A\le z+u,qquad z\ge3u,qquad y\le2u.
\]

Hence

\[
 z_0=\max(3u,A-u)\le z.
\]

For every `z'` in `[z_0,z]`, all defining inequalities replay as follows:

\[
\begin{aligned}
 z'&\ge3u\ge u+y,\\
 z'&\ge3u\ge x+y,\\
 z'+u&\ge A,\\
 z'+u&\ge4u\ge2y,\\
 z'/3&\ge y/2,\\
 z'/3&\ge(z'+u)/4.
\end{aligned}
\]

Thus internal superadditivity, the three-efficient inequalities, and the
same `w=2u` and `v` state all persist.  Moreover

\[
 \min_{u>0}\max(3u,A-u)=3A/4,
\]

so the period theorem's normalized range is valid throughout.  Since
`z<A` and `z>=3u`, one also has `0<u<A/3`.

## 4. Derivative audit, including the far-tail term

For

\[
 \Psi(z)=\mathcal L_3(z;u,2u),
\]

the current period theorem applies with second residue `2u`:

\[
 3A/4\le z\le A,qquad u\le z/3,qquad
 2u\le2z/3,qquad z+u\ge A.
\]

Its exact `q=1` derivative lower bound is

\[
 -h(1-p)+h(1+p)+h(1+4p/3)+h(1+5p/3)>0,
 \qquad p=z/A,
\]

and all `q>=2` derivatives are positive tail terms.  Therefore

\[
                         \Psi'(z)>0.
\]

For the remaining pulse, the tail identity is

\[
 K'(t)=2(A+t)e^{-(A+t)^2}.
\]

Its derivative is strictly decreasing for `t>=A`, because

\[
 {d\over dt}\big((A+t)e^{-(A+t)^2}\big)
 =(1-2(A+t)^2)e^{-(A+t)^2}<0.
\]

Since

\[
 z+v\ge z+u\ge A,qquad z+v\le z+2u,
\]

the direction is

\[
 K'(z+v)-K'(z+2u)\ge0.
\]

This confirms the delicate sign: the pulse itself can be adverse, but it
becomes no more adverse as the period increases.  The other two transient
differences are independent of `z`.  Hence the full functional is
strictly increasing.

## 5. Boundary split and endpoint-`A` replay

The two lower constraints meet at `u=A/4`, so

\[
 z_0=A-u\quad(0<u\le A/4),
 \qquad
 z_0=3u\quad(A/4\le u<A/3).
\]

On the first boundary, `T=z+u=A`.  The endpoint-period Bellman inequality
is applied to the actual four-slot clock:

\[
 \Phi\ge C(A)+F_A(x)+F_A(y)+F_A(A-u).
\]

It is valid because, at capacity `4q+r`, `q` endpoint generators and the
physical size-`r` generator supply value `qA+c_r`; the `q=0` terms are
equalities and every `q>=1` comparison is in the increasing tail.
Therefore this lower bound already contains every exceptional Bellman
value and does not silently delete the pulse.

The ranges

\[
 x\le u\le A/4,qquad y\le2u\le A/2
\]

allow the frozen train bounds and reflection identity:

\[
\begin{aligned}
 \Phi
 &>{1\over25}+{1\over25}
   -{1593\over22000}-{1\over20000}\\
 &={1659\over220000}>0.
\end{aligned}
\]

The arithmetic is exact.

## 6. Density-tie replay

On the second boundary,

\[
 z=3u,qquad T=4u,qquad z/3=T/4=u\ge y/2.
\]

Thus this is exactly the four-efficient density-tie boundary.  The Apéry
formula retains its capacity-five delayed correction and gives

\[
 \Phi\ge J(u)=C(u)+K(4u)-K(5u).
\]

Since `A/4<=u<A/3`, the scalar theorem gives

\[
 J(u)>{1117\over94500}.
\]

Exact subtraction yields

\[
 {1117\over94500}-{1659\over220000}
 ={177929\over41580000}>0,
\]

so `1659/220000` is a valid uniform margin on the full subcritical face.

## 7. First-crossing completion and scope

For an arbitrary `w=2u` table, truncate at its first displayed threshold
crossing.  If the crossing has capacity at most three, the complete
`n<=3` theorem makes the prefix strictly positive, and first-crossing
deletion says that prefix is a lower bound for the original functional.
If the crossing is at capacity four, then `x,y,z<A<=T`, so the theorem
above applies.  This exhausts the face.

The conclusion is exactly the complete positivity of `w=2u`.  Locally,
combining it with the already proved neighboring faces reduces the only
then-unresolved `n=4` row to

\[
                         w=y,\qquad P+u=2y,\qquad y>2u.
\]

This audit does not itself sign that separate surface, prove the all-grid
Bellman inequality, or imply `nu(k)<=B(k)+O(1)`.

**Final independent verdict: PASS.**
