# Complete-layer block two-cut no-go and exact atomic histogram majorisation

**Date:** 2026-08-04

**Method:** pure mathematics; no computation, search, or solver
**Status:** unconditional asymptotic no-go for every unsplit contiguous
complete-layer block partition, and unconditional exact finite
majorisation theorem for the minimally richer atomically split rank model.
The enriched model has zero numerical suffix-cut deficiency for all
sufficiently large dimensions.  It does not by itself lift the split rank
occurrences to named nested Boolean flags.

## 0. Outcome

Put

\[
 r=\left\lceil {k\over2}\right\rceil,
 \qquad W={k\choose r},
 \qquad D=d(k),
 \qquad t_0=r-D,
 \qquad C_s={k\choose s}.
\tag{0.1}
\]

The collar-saturated joint-start theorem has residual suffix capacities

\[
 K_q=W-C_{t_0+q-1},\qquad 1\le q\le D.
\tag{0.2}
\]

This note proves two complementary statements.

1. Partitioning the residual ranks `1,...,t_0-1` into arbitrary
   contiguous blocks and treating every block as one unsplit
   complete-layer batch cannot satisfy (0.2).  In fact its weighted
   omission is `Omega(W)`.  Allowing variable block widths does not help.
2. Allow each residual rank layer to be split among individual collar
   sockets, while retaining the rule that one socket uses a rank at most
   once.  This atomically split rank model has an exact Gale--Ryser
   criterion.  For all sufficiently large `k`, every one of its proper
   majorisation cuts has a uniform linear margin.  Consequently any
   boundary deletion pattern whose total residual mass fits the scalar
   capacity has a zero-defect atomic histogram.

Thus the failed suffix cuts are not a scalar obstruction.  They are caused
by forbidding a complete layer to split.  The exact remaining theorem is a
Boolean lift of the atomic schedule to complete named nested flag batches.

## 1. The unsplit contiguous-block model

Partition the residual rank interval into contiguous blocks.  Write the
highest block as

\[
 I_1=[t_0-\ell_1,t_0-1],\qquad 1\le\ell_1\le D,
\tag{1.1}
\]

and the next block as

\[
 I_2=[t_0-\ell_1-\ell_2,t_0-\ell_1-1].
\tag{1.2}

Each block is represented by the standard complete-layer SCD batch at its
top, and every flag in that batch is charged the full block width.  Thus
the first block contributes `C_(t_0-1)` flags of load `ell_1`; the second
contributes `C_(t_0-ell_1-1)` nonempty flags of load at least one.

Let

\[
                         a={\pi\over4},
 \qquad p=e^{-a},
 \qquad
 \alpha_*=1-\sqrt{{-\log(1-p)\over a}}.
\tag{1.3}
\]

Here `0<alpha_*<1`; numerically it is about `0.12`.

### Theorem 1.1 (two-cut no-go)

For every sufficiently large `k`, no unsplit contiguous-block partition
satisfies all the suffix inequalities

\[
                    A_q\le K_q\qquad(1\le q\le D).
\tag{1.4}
\]

More sharply, after imposing the cut at `q=ell_1`, its `q=1` overload is

\[
 A_1-K_1\ge(\varepsilon+o(1))W,
\tag{1.5}
\]

where

\[
 \varepsilon=
 2e^{-a}+e^{-a(1+\alpha_*)^2}-1>0.
\tag{1.6}
\]

The expression in (1.6) is about `0.285`.  Since every nonempty omitted
flag contains at least one marked target, the minimum omitted named-target
weight on this face is also `Omega(W)`.

### Proof

The standard central binomial estimate, uniformly for displacements
`O(sqrt(k))`, and

\[
                         D=\sqrt{{\pi k\over8}}+O(1)
\tag{1.7}
\]

give

\[
 {C_{r-xD+O(1)}\over W}=e^{-ax^2}+o(1)
\tag{1.8}
\]

uniformly for bounded `x`.  This holds on both parities; the half-integer
shift in the odd case is absorbed by `O(1)`.

The first batch belongs to `A_(ell_1)`.  Therefore (1.4) at
`q=ell_1` forces

\[
 C_{t_0-1}
 \le W-C_{t_0+\ell_1-1}.
\tag{1.9}
\]

Pass to any subsequence on which `ell_1/D -> alpha`.  Equations
(1.8)--(1.9) imply

\[
 e^{-a}\le1-e^{-a(1-\alpha)^2},
\tag{1.10}
\]

and hence `alpha<=alpha_*`.  Thus, without taking a subsequence,

\[
                  \limsup {\ell_1\over D}\le\alpha_*.
\tag{1.11}
\]

At the cut `q=1`, the first two batches alone give

\[
 A_1\ge C_{t_0-1}+C_{t_0-\ell_1-1}.
\tag{1.12}
\]

The second term decreases as `ell_1` increases.  Equations (1.8) and
(1.11) therefore give

\[
 {A_1\over W}\ge
 e^{-a}+e^{-a(1+\alpha_*)^2}+o(1).
\tag{1.13}
\]

On the other hand,

\[
 {K_1\over W}=1-{C_{t_0}\over W}=1-e^{-a}+o(1).
\tag{1.14}
\]

Subtracting proves (1.5).  Positivity in (1.6) follows directly from
`a=pi/4`; for example the elementary bounds
`3.1415<pi<3.1416`, together with alternating exponential-series bounds,
already give `epsilon>0.28`.  Every flag counted in (1.12) marks its top
target, so deleting one unit of overload costs at least one named target.
This proves the weighted assertion. `square`

### Scope

The theorem permits arbitrary block widths and arbitrary SCDs inside the
blocks.  It uses only the decision to charge one common declared width to
the whole complete top layer.  It does not rule out splitting a top layer,
mixing several decompositions inside one rank, or globally rechainizing
the residual ideal.

## 2. The minimally richer atomic rank model

For every start rank `t`, a collar-start socket has residual capacity

\[
                            c=t-t_0.
\tag{2.1}
\]

There are `h_t` such sockets, where

\[
 h_{t_0}=C_{t_0},\qquad
 h_t=C_t-C_{t-1}\quad(t_0<t\le r).
\tag{2.2}
\]

Include the capacity-zero sockets.  Let `c_1,...,c_W` be the resulting
multiset of `W` capacities.  Telescoping gives the exact conjugate law

\[
             |\{i:c_i\ge q\}|=K_q
                         \qquad(1\le q\le D).
\tag{2.3}
\]

Let `n_s` be the number of retained residual targets of rank `s`,
`1<=s<t_0`.  In the intended application

\[
                    0\le n_s\le C_s,
\tag{2.4}
\]

with the difference supplied by the literal triangular boundary bank.

An **atomic rank schedule** is a zero--one matrix

\[
 y=(y_{i,s}),
\tag{2.5}
\]

such that

\[
 \sum_i y_{i,s}=n_s,
 \qquad
 \sum_s y_{i,s}\le c_i.
\tag{2.6}
\]

It splits a rank layer among sockets but never puts two targets of the same
rank in one putative flag.

### Theorem 2.1 (exact finite majorisation)

An atomic rank schedule exists if and only if, after sorting the demands
decreasingly as `n_1^downarrow>=n_2^downarrow>=...` and extending this
finite list by zeros,

\[
 \boxed{
 \sum_{j=1}^{p}n_j^\downarrow
 \le
 \sum_{i=1}^{W}\min(c_i,p)
 =\sum_{q=1}^{\min(p,D)}K_q
 \quad(p\ge1).}
\tag{2.7}
\]

### Proof

Join every rank column to every socket row, with edge capacity one, demand
`n_s` at the column, and capacity `c_i` at the row.  For a set `Q` of `p`
rank columns, the rows can accept exactly

\[
                         \sum_i\min(c_i,p)
\]

units from `Q`.  Max-flow/min-cut therefore gives the inequalities in
(2.7), with the worst `p`-set formed by the `p` largest column demands.
The equality with the suffix sum follows by counting the Ferrers diagram
of the capacity sequence and using (2.3).  Integral capacities give an
integral max flow, which is exactly (2.5)--(2.6). `square`

This is the sharp scalar variational problem requested by the joint-start
theorem once complete layers are allowed to split.  There are no other
rank-histogram cuts.

## 3. Every proper atomic cut has uniform asymptotic slack

### Theorem 3.1 (zero-defect atomic histogram)

There are constants `eta>0` and `k_0` such that for every `k>=k_0` and
every `1<=p<=D`,

\[
 \sum_{j=0}^{p-1}
   \left(C_{t_0-1-j}+C_{t_0+j}\right)
 \le(1-\eta)pW.
\tag{3.1}
\]

Consequently, if (2.4) holds and

\[
                  \sum_{s<t_0}n_s\le\sum_{q=1}^{D}K_q,
\tag{3.2}
\]

then an atomic rank schedule exists.  It retains every one of the
`sum_s n_s` target occurrences, so its numerical weighted deficiency is
zero.  Its actual load histogram

\[
                 A_q=|\{i:\sum_s y_{i,s}\ge q\}|
\tag{3.3}
\]

satisfies `A_q<=K_q` for every `q`.

### Proof of the analytic margin

For `0<theta<=1`, define

\[
 G(\theta)={1\over\theta}
 \int_0^\theta
 \left(e^{-a(1-x)^2}+e^{-a(1+x)^2}\right)\,dx.
\tag{3.4}
\]

We first prove

\[
                         \max_{0\le\theta\le1}G(\theta)<1,
\tag{3.5}
\]

where `G(0)=2e^(-a)` by continuity.  Put

\[
 H(\theta)=\theta-
 \int_0^\theta
 \left(e^{-a(1-x)^2}+e^{-a(1+x)^2}\right)\,dx.
\tag{3.6}
\]

The endpoint values are

\[
 H(0)=0,
 \qquad
 H(1)=1-\int_0^2e^{-au^2}\,du
     =1-\operatorname{erf}(\sqrt\pi)>0.
\tag{3.7}
\]

Let

\[
 P(x)=e^{-a(1-x)^2}+e^{-a(1+x)^2}
     =2e^{-a(1+x^2)}\cosh(2ax).
\tag{3.8}
\]

The sign of `P'(x)` is the sign of

\[
                         \tanh(2ax)-x.
\tag{3.9}
\]

Its derivative is `2a sech^2(2ax)-1`, which is strictly decreasing;
it starts positive because `2a=pi/2>1`, while
`tanh(2a)-1<0` at `x=1`.  Hence (3.9) has exactly one positive zero and
`P` has one interior maximum.  Since

\[
                         P(0)=2e^{-a}<1,
 \qquad P(1)=1+e^{-4a}>1,
\tag{3.10}
\]

`P` crosses the level one exactly once.  Therefore
`H'=1-P` is first positive and then negative.  The minimum of `H` on the
interval is attained at an endpoint.  Equation (3.7) gives
`H(theta)>0` for `theta>0`.  Moreover `H(theta)/theta` extends continuously
and positively to `[0,1]`.  This proves (3.5), with some fixed margin
`eta_0>0`.

The uniform central binomial estimate (1.8), now used for all
`0<=j<D`, turns the left side of (3.1), divided by `pW`, into a Riemann
sum for (3.4) when `p/D` has a positive limit.  If `p/D->0`, the same
uniform estimate gives the limit `2e^(-a)<1`.  Compactness and (3.5)
therefore give (3.1), after reducing the fixed margin if necessary.

### Completion of the majorisation proof

For `p<=D`, the sum of the `p` largest demands satisfying (2.4) is at most
the sum of the `p` largest unpunctured residual layers:

\[
                 \sum_{j=1}^{p}n_j^\downarrow
 \le\sum_{j=0}^{p-1}C_{t_0-1-j}.
\tag{3.11}
\]

By (0.2), inequality (3.1) rearranges to

\[
 \sum_{j=0}^{p-1}C_{t_0-1-j}
 \le pW-\sum_{j=0}^{p-1}C_{t_0+j}
 =\sum_{q=1}^{p}K_q.
\tag{3.12}
\]

For `p>D`, the right side of (2.7) is the total capacity, so (3.2)
proves the cut.  Theorem 2.1 gives the matrix.  Finally, a row of actual
load at least `q` has capacity at least `q`; (2.3) therefore proves
`A_q<=K_q`. `square`

## 4. Application to the triangular residual inventory

Let `b_s` be any literal triangular-boundary deletion counts lying in the
residual ranks, and put

\[
                         n_s=C_s-b_s.
\tag{4.1}
\]

If the boundary bank removes

\[
                         h=(\Lambda-DW)_+
\tag{4.2}
\]

residual targets, then

\[
 \begin{aligned}
 \sum_{s<t_0}n_s
 &=\Lambda-\sum_{s=t_0}^{r-1}C_s-h,\\
 \sum_{q=1}^{D}K_q
 &=DW-\sum_{s=t_0}^{r-1}C_s.
 \end{aligned}
\tag{4.3}
\]

Thus (3.2) holds, with equality when `Lambda>DW` and with the pre-existing
scalar slack when `Lambda<=DW`.  Theorem 3.1 supplies a zero-defect atomic
histogram for every sufficiently large `k`, independently of how the
`h` deleted targets are distributed among the residual ranks.

This is stronger than a continuous Gaussian feasibility statement: the
Gaussian calculation proves a uniform margin in every proper cut, and
ordinary integral max flow rounds the exact finite integer marginals.

## 5. Exact surviving gate

The atomic matrix is not yet a family covered by the joint-start orbit
theorem.  It records only which ranks are assigned to each collar socket.
It does not choose named targets satisfying

\[
 S_{i,s_1}\subset S_{i,s_2}\subset\cdots\subset T_i
\tag{5.1}
\]

inside one owner, and its rows need not assemble into complete-layer
batches with one uniform structural-top orbit.

Accordingly, the theorem proves neither a lower deck nor an `O(1)` upper
bound for `nu(k)`.  It proves the following sharp boundary.

\[
\boxed{
\begin{array}{c}
\text{Unsplit complete-layer rank blocks have }\Omega(W)
\text{ weighted suffix deficiency};\\[2mm]
\text{atomically split layers have exactly zero numerical deficiency};\\[2mm]
\text{the remaining obstruction is precisely the named nested-flag lift.}
\end{array}}
\tag{5.2}
\]

A sufficient next theorem is therefore:

> **Atomic-to-complete flag lift.**  Choose the integral matrix in
> Theorem 3.1 together with distinct named rank targets and distinct
> rank-`r` owners so that every row is one literal inclusion flag, while
> retaining the complete-layer orbit structure needed by the joint-start
> matching.

No aggregate suffix capacity or Gaussian rank-count obstruction remains
after that lift is allowed.
