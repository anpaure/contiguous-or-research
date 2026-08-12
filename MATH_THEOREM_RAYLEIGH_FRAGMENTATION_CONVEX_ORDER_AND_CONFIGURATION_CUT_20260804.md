# Rayleigh chain fragmentation: convex-order exactness and the configuration-cut frontier

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem and exact reduction.
The Gaussian scaling limit of the anonymous two-SCD chain-cutting problem
passes every Lorenz/concave fragmentation cut.  Whole-chain fragmentation is
nevertheless governed by a strictly stronger configuration LP.  An explicit
family shows that neither the scalar ledger, all receiving-side threshold
cuts, nor even adding one unit to every socket eliminates these configuration
cuts in general.  This is **not** a no-go theorem for the actual binomial
socket profile.

## 1. The two Rayleigh deviation measures

Work in even dimension `k=2r`, and put

\[
 A={\sqrt\pi\over2},\qquad d\sim A\sqrt r,\qquad t=r-d.
\]

Recall `H_b={2r\choose b}-{2r\choose b-1}`.  A residual SCD chain
starting at rank `t-l` gives one job of length `l`, with multiplicity
`H_(t-l)`.  A collar chain starting at rank `t+u` gives one socket of
capacity `u`, with multiplicity `H_(t+u)`.

At the scale

\[
 l=x\sqrt r,\qquad u=y\sqrt r,
\]

the local central-binomial estimate gives

\[
 {\sqrt r\over W}H_{t-l}\longrightarrow
 j(x):=2(A+x)e^{-(A+x)^2}\qquad(x\ge0),              \tag{1.1}
\]

and

\[
 {\sqrt r\over W}H_{t+u}\longrightarrow
 s(y):=2(A-y)e^{-(A-y)^2}\qquad(0\le y\le A).       \tag{1.2}
\]

Indeed, if `b=r-z sqrt(r)`, then

\[
 {{2r\choose b}\over {2r\choose r}}\to e^{-z^2},
\qquad
 H_b={2r\choose b}{2r+1-2b\over2r+1-b}
     \sim {2z\over\sqrt r}e^{-z^2}W.                \tag{1.3}
\]

Let `mu` be the job measure with density `j`, and let `nu` be the socket
measure with density `s`.  Their masses are

\[
 J:=\mu(\mathbb R_+)=e^{-A^2},
 \qquad
 S:=\nu([0,A])=1-e^{-A^2}.                           \tag{1.4}
\]

Their first moments agree:

\[
 \int_0^\infty x\,d\mu(x)
 =\int_A^\infty e^{-z^2}\,dz
 =A-\int_0^A e^{-z^2}\,dz
 =\int_0^A y\,d\nu(y).                              \tag{1.5}
\]

The middle equality is exactly the choice
`A=int_0^infty exp(-z^2) dz=sqrt(pi)/2`.

## 2. Exact Lorenz domination

Since `A^2=pi/4>log 2`, we have `S>J`.  Pad the job measure by zero-size
atoms:

\[
 \widetilde\mu:=\mu+(S-J)\delta_0.                  \tag{2.1}
\]

Then `nu` and `tilde(mu)` have the same total mass and the same first
moment.

### Theorem 2.1 (Rayleigh mean-deviation convex order)

For every `q>=0`,

\[
 \boxed{
 \int \min(z,q)\,d\nu(z)
 \ge
 \int \min(z,q)\,d\widetilde\mu(z).}
                                                               \tag{2.2}
\]

Equivalently,

\[
                         \nu\preceq_{cx}\widetilde\mu.         \tag{2.3}
\]

Thus every nonnegative concave price `phi` with `phi(0)=0` satisfies

\[
 \boxed{\int_0^A\phi(y)s(y)\,dy
       \ge\int_0^\infty\phi(x)j(x)\,dx.}             \tag{2.4}
\]

Such a `phi` is automatically subadditive, so every concave separable
fragmentation test passes.

#### Proof

Let

\[
 D(q)=\int\min(z,q)\,d(\nu-\widetilde\mu)(z).        \tag{2.5}
\]

The atom at zero contributes nothing.  For `0<=q<=A`, the two tail
functions give

\[
 D'(q)=1-e^{-(A-q)^2}-e^{-(A+q)^2}=1-F(q),           \tag{2.6}
\]

where

\[
 F(q)=2e^{-(A^2+q^2)}\cosh(2Aq).                    \tag{2.7}
\]

The logarithmic derivative of `F` has the sign of

\[
 h(q)=A\tanh(2Aq)-q.                                 \tag{2.8}
\]

Now

\[
 h''(q)=-8A^3\operatorname{sech}^2(2Aq)\tanh(2Aq)<0
 \qquad(q>0),                                        \tag{2.9}
\]

while

\[
 h(0)=0,qquad h'(0)=2A^2-1={\pi\over2}-1>0,
 \qquad h(A)=A(\tanh(2A^2)-1)<0.                    \tag{2.10}
\]

Hence `F` increases and then decreases, with one positive maximum.  Also

\[
 F(0)=2e^{-A^2}<1,qquad F(A)=1+e^{-4A^2}>1.         \tag{2.11}
\]

It follows that `F(q)=1` has exactly one solution in `(0,A)`: after the
upward crossing, the decreasing branch remains above its endpoint value
`F(A)>1`.  Therefore `D'` is first positive and then negative on `[0,A]`.

We have `D(0)=0`, and equality of first moments gives

\[
 D(A)=\int_A^\infty(x-A)\,d\mu(x)>0.                \tag{2.12}
\]

Thus `D(q)>=0` on `[0,A]`.  For `q>A`,

\[
 D'(q)=-\mu((q,\infty))<0,                           \tag{2.13}
\]

and `D(q)` decreases to zero as `q` tends to infinity.  This proves
(2.2).  The standard stop-loss characterization of convex order gives
(2.3), and Jensen/convex-order duality gives (2.4).

Finally, concavity and `phi(0)=0` imply

\[
 \phi(x)\ge{x\over x+y}\phi(x+y),\qquad
 \phi(y)\ge{y\over x+y}\phi(x+y),                   \tag{2.14}
\]

so `phi(x+y)<=phi(x)+phi(y)`.  \(\square\)

### Interpretation

The leading Gaussian job/socket pair has no obstruction detectable by
majorization, stop-loss, power moments, or any other concave separable
fragmentation price.  A successful composition, if it exists, must still
choose whole finite groups of sockets for each job; convex order alone does
not do that grouping.

## 3. The exact anonymous configuration LP

Return to finite integer data.  Let `n_l` be the number of jobs of length
`l`, and let `m_u` be the number of sockets of capacity `u`, where
`1<=u<=d`.  Trimming is allowed: a socket of capacity `u` may carry any
positive integer fragment of size at most `u`.

For a job of length `l`, define its capacity-pattern set

\[
 \mathcal Q_l=
 \left\{p\in\mathbb Z_{\ge0}^d:
        |p|:=\sum_u p_u\le l\le\sum_u u p_u\right\}. \tag{3.1}
\]

This condition is exact.  Starting every selected socket at load one gives
load `|p|`; the remaining `sum_u (u-1)p_u` units can be added one at a
time, so every integer load through `sum_u u p_u` is attainable.

A fractional whole-job composition is a family `z_(l,p)>=0` satisfying

\[
 \sum_{p\in\mathcal Q_l}z_{l,p}=n_l,                 \tag{3.2}
\]

and

\[
 \sum_l\sum_{p\in\mathcal Q_l}p_u z_{l,p}\le m_u
 \qquad(1\le u\le d).                               \tag{3.3}
\]

### Theorem 3.1 (exact configuration-price criterion)

The system (3.2)--(3.3) is feasible if and only if, for every price vector
`theta in R_+^d`,

\[
 \boxed{
 \sum_l n_l\,\psi_\theta(l)
 \le\sum_u m_u\theta_u,}
 \qquad
 \psi_\theta(l):=min_{p\in\mathcal Q_l}\theta\mathbin\cdot p.
                                                               \tag{3.4}
\]

#### Proof

Let `C` be the convex set of socket-usage vectors generated by (3.2).
There is a feasible composition exactly when

\[
                  m\in C+\mathbb R_{\ge0}^d.         \tag{3.5}
\]

The right side is a closed polyhedron.  If (3.5) fails, strong separation
gives a linear functional bounded below on its positive orthant.  Its
coefficient vector must therefore satisfy `theta>=0`, and separation says

\[
 \min_{c\in C}\theta\mathbin\cdot c>\theta\mathbin\cdot m.     \tag{3.6}
\]

The minimum over `C` separates job by job and is exactly
`sum_l n_l psi_theta(l)`.  Conversely, any such price violation excludes
(3.5).  \(\square\)

The integral problem additionally requires integer `z_(l,p)`; Theorem 3.1
does not claim configuration-matrix total unimodularity.

The rank-density threshold inequalities check whether an already declared
fragment histogram can be injected into capacities.  Theorem 3.1 is
strictly earlier: it checks whether that histogram can arise by composing
whole jobs at all.  Its general prices are nonconcave and can detect residue
and mixed-size obstructions invisible to all one-threshold cuts.

## 4. A sharp configuration obstruction

The distinction is not formal.  For one block, take

\[
 \text{jobs }(10,10),\qquad
 \text{declared fragments }(6,6,3,3,2).             \tag{4.1}
\]

They have equal total load.  The fragment vector is majorized by
`(10,10,0,0,0)`, since its successive largest-part sums are

\[
                         6,12,15,18,20
 \le 10,20,20,20,20.                                 \tag{4.2}
\]

It also passes every uniform host-count bound

\[
 \#\{\hbox{fragments of size at least }q\}
 \le2\left\lfloor{10\over q}\right\rfloor.          \tag{4.3}
\]

Nevertheless no submultiset sums to ten.  Hence the fragments cannot be
partitioned into the two jobs.  The configuration price taking

\[
 \theta_6=2,\qquad\theta_3=\theta_2=1,
 \qquad\theta_u=10\ (u\notin\{2,3,6\})               \tag{4.4}
\]

certifies the obstruction: every capacity-exact partition of ten has cost
at least four.  The same is true under the trimming convention of Section
3: the minimum is attained by 6+6, 6+3+2, 6+2+2, 6+3+3, and
3+3+2+2.  Thus the two jobs cost at least eight while the available socket
price is

\[
                   2\cdot2+2\cdot1+1\cdot1=7.
\]

This is the
smallest kind of mixed-residue cut that Lorenz tests cannot see.

## 5. One extra unit per socket is not a generic cure

The extra `W`-scale scalar capacity at length `B+1` is important, but no
argument using only that scalar increment can remove Theorem 3.1.

For `m>=1`, start with

\[
 2m\text{ jobs of length }11,qquad
 3m\text{ sockets of capacity }7,\quad
 m\text{ sockets of capacity }1.                    \tag{5.1}
\]

The base capacity is exactly the demand:

\[
 3m\cdot7+m\cdot1=22m=2m\cdot11.                    \tag{5.2}
\]

Now increase **every** socket capacity by one.  The new capacities are

\[
                    3m\text{ copies of }8,qquad
                    m\text{ copies of }2,            \tag{5.3}
\]

and their total slack is `4m`, exactly one new unit per socket.

Yet at most `7m/4` jobs can be packed.  Indeed, an 11-job using at least
two 8-sockets is of type `A`; one using exactly one 8-socket needs at least
two 2-sockets and is of type `B`; one using no 8-socket needs at least six
2-sockets and is of type `C`.  Therefore

\[
 2A+B\le3m,\qquad 2B+6C\le m.                       \tag{5.4}
\]

It follows that

\[
 A+B+C\le {3m-B\over2}+B+C
          ={3m\over2}+{B\over2}+C
          \le {7m\over4}.                           \tag{5.5}
\]

Thus at least `m/4` jobs remain unpacked.  The exact price certificate is

\[
 \theta_8=2,qquad\theta_2=1,qquad
 \theta_u=10\ (u\notin\{2,8\}).                    \tag{5.6}
\]

Every 11-pattern costs at least

\[
 \min\{2\theta_8,\theta_8+2\theta_2,6\theta_2\}=4,
                                                               \tag{5.7}
\]

so the job side costs `8m`, whereas the entire socket side costs only
`7m`.

At the receiving-side level, the anonymous fragments

\[
                         (8,8,4,2)                   \tag{5.8}
\]

per two jobs have total load 22 and fit coordinatewise into
`(8,8,8,2)`.  Hence the scalar and socket-threshold relaxation accepts
them.  The failure is precisely that no global whole-job composition can
realize the accepted histogram.

This example does **not** have the binomial/Rayleigh multiplicity profile.
It proves only the necessary scope correction:

\[
 \boxed{\text{one extra unit per socket is not, by itself, a
 configuration-rounding theorem.}}                   \tag{5.9}
\]

## 6. Consequence for the two-SCD programme

The anonymous chain-dependent gate has three levels.

1. **Scalar capacity.**  This is exact in the current two-SCD ledger.
2. **Rayleigh/Lorenz shape.**  Theorem 2.1 closes every convex separable
   obstruction in the scaling limit.
3. **Whole-job configuration.**  Theorem 3.1 is the exact fractional gate;
   its nonconcave price vectors remain unproved for the binomial profile.

Therefore the common-slab no-go is not explained by a Gaussian
mean-deviation mismatch.  A successful chain-dependent cut must prove the
configuration inequalities (3.4), or give an explicit pattern mixture,
and then still solve literal cross-SCD containment Hall.  The present note
neither proves nor disproves that final binomial construction.
