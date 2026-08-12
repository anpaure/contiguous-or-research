# Audit: nested balanced quotas and wreath synchronization

Date: 2026-07-24

## Verdict

The overload identity, the lower-bounded-flow construction, and the labelled
synchronization inequality are correct.  They give a clean unconditional
reduction of MWB to one common integral synchronization problem.

The displayed Gaussian criterion (31), however, is vacuous for the stated
choice `H=sqrt(m) log log(m+e^e)`: even perfect agreement through depth `H`
cannot satisfy it.  The defect comes from replacing the finite Gaussian tail
by an infinite tail and then charging that positive bound to owners with
`a(X)=H`, whose true remaining cost is zero.  A truncated-tail correction is
given below.

## 1. Exact overload identity

For integer loads of total `W=cN+rho`, put

\[
 A=\sum_i(c-\mu_i)_+,
 \qquad
 B=\sum_i(\mu_i-c-1)_+.
\]

If `t=#{i:mu_i>=c+1}` and `P=sum_i(mu_i-c)_+`, then

\[
 P-A=\rho,
 \qquad
 B=P-t.
\]

Raising exactly `rho` quotas from `c` to `c+1` removes
`min(rho,t)` overload units, so

\[
 O=P-\min\{\rho,t\}=\max\{A,B\}.
\]

The equivalent balanced `L1/2` formula follows because the load and quota
vectors have equal total mass.  At every proper lower depth `c_q>=1`, and
every hole contributes `c_q` to `A`; hence `M_q<=O_q/c_q`.

## 2. Integral nested balanced-chain resolution

The proposed layered network is valid.  At rank `r`, the uniform real split
flow is

\[
 \lambda_r=\frac{W}{\binom nr}.
\]

Sending `lambda_r/r` through every immediate-subset arc gives a fixed
rank-`r-1` set incoming flow

\[
 (n-r+1)\frac{\lambda_r}{r}
 =\frac{W}{\binom n{r-1}}=\lambda_{r-1}.
\]

Thus the lower/upper bounds `floor(lambda_r),ceil(lambda_r)` admit a real
circulation.  Integral lower and upper capacities then give an integral
circulation by the standard lower-bound reduction.  Removing the return arc
leaves an acyclic integral `s`--`t` flow of value `W`; unit-path decomposition
produces exactly one nested deletion flag for every middle owner.  Every
rank fiber is simultaneously floor/ceiling balanced.

This removes marginal integrality and nesting, but not cyclic bundling.

## 3. Synchronization inequality

Let `b_q` be the balanced histogram of `P_q`, and let `mu_q` be the histogram
of the wreath flag `L_q^F`.  Changing the label attached to one middle owner
changes two histogram coordinates by one, so

\[
 \|\mu_q-b_q\|_1\le 2e_q(F,P).
\]

Since `O_q` is half the minimum `L1` distance to any balanced histogram,

\[
 O_q(F)\le\tfrac12\|\mu_q-b_q\|_1\le e_q(F,P).
\]

Therefore

\[
 \sum_{q\le H}\frac{O_q(F)}{c_q}
 \le
 \sum_{q\le H}\frac{e_q(F,P)}{c_q}.
\]

This part of the reduction is exact.

## 4. The Gaussian criterion needs truncation

For initial agreement depth `a(X)`, the exact owner charge is

\[
 \Psi_{m,H}(a)=\sum_{q=a+1}^{H}\frac1{c_q}.
\]

The identity

\[
 \sum_{q\le H}\frac{e_q}{c_q}
 \le\sum_X\Psi_{m,H}(a(X))
\]

is correct.  So are the uniform estimates

\[
 \log\frac{W}{N_q}=\frac{q(q+1)}m+o(1),
 \qquad
 \frac1{c_q}\le
 2\exp\!\left(-\frac{q(q+1)}m+o(1)\right)
\]

for `q<=H=o(m^(2/3))`.

The submitted criterion replaces the finite sum by an infinite Gaussian
tail and asks

\[
 \sum_X
 \frac{e^{-a(X)^2/m}}{1+a(X)/\sqrt m}
 =o(W/\sqrt m).
\]

For every owner `a(X)<=H`, and the summand is decreasing in `a`.  Hence its
left side is at least

\[
 W\frac{e^{-H^2/m}}{1+H/\sqrt m}.
\]

With `H=sqrt(m) log log(m+e^e)`, division by `W/sqrt(m)` gives

\[
 \frac{\sqrt m\,e^{-(\log\log m)^2}}
      {1+\log\log m}\longrightarrow\infty.
\]

Thus the condition fails even when every owner agrees through all `H`
depths.  It is formally an implication with an impossible premise, but it is
not a usable synchronization gate.

The finite tail gives the sharper nonvacuous correction

\[
 \Psi_{m,H}(a)
 \le C e^{-a^2/m}\min\left\{
 H-a,
 \frac{\sqrt m}{1+a/\sqrt m}
 \right\}.
\]

Indeed, the finite sum has at most `H-a` terms, all at most a constant
multiple of `e^(-a^2/m)`, while the infinite-tail estimate supplies the
second bound.  Consequently either of the following conditions really is
sufficient for MWB:

\[
 \boxed{
 \sum_X (H-a(X))e^{-a(X)^2/m}=o(W),
 }
\]

or the slightly weaker minimum-of-the-two-bounds condition

\[
 \sum_X e^{-a(X)^2/m}
 \min\left\{
 \frac{H-a(X)}{\sqrt m},
 \frac1{1+a(X)/\sqrt m}
 \right\}
 =o(W/\sqrt m).
\]

Equivalently, and more cleanly, one may retain the exact requirement

\[
 \boxed{
 \sum_X\Psi_{m,H}(a(X))=o(W).
 }
\]

Fully synchronized owners now contribute zero, as they must.

## 5. The cyclic obstruction is genuine

Every exact wreath factor satisfies the point marginal

\[
 \sum_{S\ni x}\mu_q(S)=(m-q)W/n.
\]

For `m=3`, a nested resolution with first-deletion counts
`(9,5,4,4,5,4,4)`, balanced pair loads `1/2`, and singleton loads all `5`
is feasible.  An independent exact SAT reconstruction confirmed all 35
owner flags.  It cannot be a wreath factor, because five wreaths delete each
coordinate exactly once apiece, forcing first-deletion count `5` at every
coordinate.

Therefore the balanced-chain theorem is not a disguised wreath
factorization; the synchronization condition is a real extra constraint.
This obstructs that particular balanced resolution, not dimension `m=3`
itself: the standard explicit `Q_7` wreath factor induces another balanced
resolution with deletion margins `5^7`, pair loads `1^7 2^14`, and singleton
loads `5^7`.

## Corrected status

Unconditional:

- exact overload formula and `M_q<=O_q/c_q`;
- simultaneous integral balanced nested flags through every depth;
- `O_q<=e_q` and the exact owner-tail synchronization reduction;
- an explicit point-marginal obstruction to automatic cyclic bundling.

Still open:

- an exact wreath factor and balanced nested resolution satisfying
  `sum_X Psi_(m,H)(a(X))=o(W)` for `H=sqrt(m) omega(m)`;
- or the weaker rankwise hybrid hole-energy condition already recorded in
  the project.
