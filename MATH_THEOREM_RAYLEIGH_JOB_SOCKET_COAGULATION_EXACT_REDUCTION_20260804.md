# Rayleigh job/socket limit: exact coagulation reduction and fragment-count ledger

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  This note identifies
the exact continuum primal hidden in the chain-dependent two-SCD cutting
problem.  It proves that aggregate trimming is impossible at the critical
coefficient, gives the precise necessary-and-sufficient configuration-measure
formulation, and evaluates every unavoidable fragment-count tail.  It does
**not** construct the required coagulation kernel and does not imply an
integral or literal SCD attachment.

## 1. The two limiting measures

Put

\[
 A={\sqrt\pi\over2}.
\]

In the central Gaussian scaling, a residual SCD job has scaled length
`x>0` with intensity

\[
 \mu(dx)=j(x)\,dx,
 \qquad
 j(x)=2(A+x)e^{-(A+x)^2},                            \tag{1.1}
\]

and an owner socket has scaled capacity `0<y<A` with intensity

\[
 \nu(dy)=s(y)\,dy,
 \qquad
 s(y)=2(A-y)e^{-(A-y)^2}.                            \tag{1.2}
\]

The endpoint-triangular sockets have vanishing intensity at this scale and
therefore do not appear in (1.2).

Let

\[
 p=e^{-A^2}=e^{-\pi/4}.
\]

Direct integration gives the exact count ledger

\[
 \boxed{\mu(0,\infty)=p,
 \qquad \nu(0,A)=1-p.}                              \tag{1.3}
\]

The workload ledger also closes exactly:

\[
\begin{aligned}
 \int_0^\infty x\,\mu(dx)
 &=\int_A^\infty (z-A)2ze^{-z^2}\,dz
   =\int_A^\infty e^{-z^2}\,dz,\\
 \int_0^A y\,\nu(dy)
 &=\int_0^A(A-z)2ze^{-z^2}\,dz
   =A-\int_0^A e^{-z^2}\,dz
   =\int_A^\infty e^{-z^2}\,dz.
                                                               \tag{1.4}
\end{aligned}
\]

The last equality uses

\[
 A=\int_0^\infty e^{-z^2}\,dz.
\]

Thus the coefficient forced by the original lower bound is exactly the
coefficient at which total job work equals total socket capacity.

## 2. Exact configuration-measure theorem

Let `C` be the disjoint union, over integers `n>=1`, of the spaces of
unordered configurations

\[
 (x;(y_1,z_1),\ldots,(y_n,z_n))                     \tag{2.1}
\]

with

\[
 x>0,\qquad 0<z_i\le y_i<A,
 \qquad \sum_{i=1}^n z_i=x.                         \tag{2.2}
\]

Here `y_i` is the physical capacity of the chosen socket and `z_i` is the
amount of the job placed in that socket.  A **fractional fragmentation
kernel** is a finite positive Borel measure `rho` on `C` such that

\[
 (\operatorname{job})_\#\rho=\mu                  \tag{2.3}
\]

and its aggregate socket marginal is `nu`:

\[
 \int_{\mathcal C}\sum_{i=1}^n
       \mathbf1_{\{y_i\in E\}}\,d\rho=\nu(E)
 \quad(E\subset(0,A)\text{ Borel}).                \tag{2.4}
\]

### Theorem 2.1 (zero trimming and exact coagulation)

For the measures (1.1)--(1.2), the following are equivalent.

1. A fractional fragmentation kernel `rho` satisfying (2.2)--(2.4)
   exists.
2. There is a finite positive Borel measure `rho_0` on the exact
   configuration space

   \[
    \mathcal C_0=
    \bigsqcup_{n\ge1}
    \{(x;y_1,\ldots,y_n):0<y_i<A,\ \sum_i y_i=x\}/\mathfrak S_n
                                                               \tag{2.5}
   \]

   whose job marginal is `mu` and whose aggregate piece marginal is `nu`.

Moreover every kernel in item 1 satisfies

\[
                         z_i=y_i
\]

for `rho`-almost every configuration and every one of its pieces.

#### Proof

Item 2 plainly implies item 1.  Conversely, integrate the nonnegative unused
capacity over a kernel from item 1.  Equations (2.2)--(2.4) and (1.4) give

\[
\begin{aligned}
 \int_{\mathcal C}\sum_i(y_i-z_i)\,d\rho
 &=\int_0^A y\,\nu(dy)-\int_0^\infty x\,\mu(dx)\\
 &=0.                                                     \tag{2.6}
\end{aligned}
\]

The integrand is nonnegative, so it vanishes almost everywhere.  Hence every
used piece fills its socket exactly, and `rho` is supported on (2.5).
\(\square\)

Because

\[
 \int_{\mathcal C_0}n\,d\rho_0=\nu(0,A)=1-p<\infty, \tag{2.7}
\]

the groups are finite almost everywhere; no separate finite-support premise
is hidden in item 2.

The theorem is the exact continuum meaning of the desired chain-dependent
fragmentation: **partition the socket measure into finite groups whose sums
have job intensity `mu`.**  Scalar capacity, fractional splitting, or a
coupling of size-biased mass is weaker and is not enough.

## 3. Uniform exponential-square coordinate

There is a useful lossless reparametrization.  Put

\[
 u=e^{-(A-y)^2},\qquad y<A.                          \tag{3.1}
\]

Then

\[
 du=2(A-y)e^{-(A-y)^2}\,dy.                         \tag{3.2}
\]

Thus Lebesgue measure on `(0,p)` parametrizes jobs by

\[
 x(u)=\sqrt{-\log u}-A,                             \tag{3.3}
\]

while Lebesgue measure on `(p,1)` parametrizes sockets by

\[
 y(u)=A-\sqrt{-\log u}.                             \tag{3.4}
\]

The exact coagulation problem is consequently equivalent to grouping the
points of the uniform interval `(p,1)` into finite fibres indexed by the
uniform interval `(0,p)` so that

\[
 \sum_{v\text{ in the fibre of }u}
       \bigl(A-\sqrt{-\log v}\bigr)
 =\sqrt{-\log u}-A.                                \tag{3.5}
\]

This exposes the exponential memorylessness behind the marginal measures,
but (3.5) is an additive identity in the square roots.  Memorylessness of
`-log u` alone does not prove it.

## 4. Every unavoidable piece-count tail

Let `N` denote the number of sockets in the group assigned to a job of size
`x`.  Since every socket has capacity at most `A`,

\[
 N\ge\left\lceil{x\over A}\right\rceil.             \tag{4.1}
\]

For every integer `n>=1`, any exact coagulation therefore satisfies

\[
\begin{aligned}
 \int_{\mathcal C_0}\mathbf1_{\{N\ge n\}}\,d\rho_0
 &\ge \mu((n-1)A,\infty)\\
 &=e^{-n^2A^2}=e^{-\pi n^2/4}.                      \tag{4.2}
\end{aligned}
\]

Summing the tail identity for an integer-valued random variable gives the
sharp capacity-only lower bound

\[
 \boxed{
  \int_{\mathcal C_0}N\,d\rho_0
  \ge M_{\min}:=\sum_{n\ge1}e^{-\pi n^2/4}.}        \tag{4.3}
\]

The available piece intensity is

\[
 S=1-e^{-\pi/4}.                                    \tag{4.4}
\]

There is strict cardinality slack:

\[
 \boxed{
 \Delta_\#:=S-M_{\min}>0.}                         \tag{4.5}
\]

Here is an elementary verification, avoiding numerical optimization.  Put
`q=e^{-pi/4}`.  Since `n^2>=4(n-1)` for `n>=2`,

\[
 M_{\min}
 \le q+\sum_{n\ge2}q^{4(n-1)}
 =q+{q^4\over1-q^4}.                                \tag{4.6}
\]

The standard inequalities `pi>3.14` and the fourth-order Taylor lower bound
for the exponential give `q<11/24`.  Therefore

\[
 2q+{q^4\over1-q^4}
 <{11\over12}+{14641\over317135}<1,                \tag{4.7}
\]

which is exactly (4.5).

The complete minimum group-size census is also explicit.  Jobs which need
exactly `n` pieces under the bare upper bound `y<=A` have intensity

\[
 \boxed{
 e^{-\pi n^2/4}-e^{-\pi(n+1)^2/4}
 \qquad(n\ge1).}                                   \tag{4.8}
\]

Equation (4.5) says that the socket count exceeds this bare minimum by the
positive intensity `Delta_#`.  It does **not** imply that the sockets can be
grouped with the required sums: their full capacity distribution, not only
their number, must be respected.

The average number of pieces in any exact coagulation is forced:

\[
 \boxed{
 {\nu(0,A)\over\mu(0,\infty)}
 =e^{\pi/4}-1.}                                    \tag{4.9}
\]

Equivalently, the total excess-fragment intensity is

\[
 \boxed{
 \int(N-1)\,d\rho_0=1-2e^{-\pi/4}.}                \tag{4.10}
\]

This is the exact leading-scale price of chain-dependent splitting.

## 5. Dual certificate and exact remaining continuum gate

For a nonnegative Borel price `a(y)` on socket capacities, define its exact
configuration closure

\[
 a^\star(x)=
 \inf\left\{
  \sum_{i=1}^n a(y_i):
  n\ge1,\ 0<y_i<A,\ \sum_i y_i=x
 \right\}.                                         \tag{5.1}
\]

Every coagulation kernel necessarily satisfies

\[
 \boxed{
 \int_0^\infty a^\star(x)\,\mu(dx)
 \le\int_0^A a(y)\,\nu(dy).}                      \tag{5.2}
\]

Indeed, (5.1) holds on every group and integration uses the two marginals.
Under the standard closedness/tightness hypothesis for the corresponding
configuration-measure cone, the family (5.2) is also sufficient by
Hahn--Banach separation.  This note does not assert that analytic
closedness step and does not assert (5.2) for every price.

Thus the exact unresolved continuum alternatives are now sharp:

1. construct `rho_0` in Theorem 2.1; or
2. exhibit a nonnegative price `a` for which (5.2) fails (equivalently, a
   genuine nonconcave subadditive/configuration separator after taking the
   closure (5.1)).

Concave moment comparisons, first-moment equality, and the positive count
slack (4.5) cannot by themselves decide this gate.

## 6. Scope

The theorem settles the leading Gaussian **anonymous** fragmentation
formulation only.  Even a positive solution of Theorem 2.1 would still need:

* discrete rounding with only lower-order loss;
* a chain-dependent implementation inside one literal residual SCD;
* containment Hall against one correlated collar SCD;
* compatibility with the upper occurrence and residence host.

Conversely, failure of a common rank grid does not contradict Theorem 2.1:
the latter permits the cut pattern to depend on the individual job length.
