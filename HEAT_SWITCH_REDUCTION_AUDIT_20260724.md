# Audit of the exact heat-switch reduction for MWB

Date: 2026-07-24

This is a purely mathematical audit of the latest component-switching
proposal.  All transposition sums below are over the unordered coordinate
transpositions, each counted once, and all norms are unnormalized counting
norms.

## Verdict

**Material correction required.**  The exact switching lemma, the quadratic
integer floor, the fair-switch identity, and the global-minimizer inequality
are correct, including their directions and factors of (1/4).  The displayed
Johnson estimate with coefficient (2n) is also a valid generic estimate.

It is not, however, the sharp estimate applicable to exact wreath-factor
histograms.  Their centered histograms have zero point margins, so Johnson
degrees (0) and (1) are absent.  The applicable sharp coefficient is

\[
4(n-1),
\]

not (2n).  Consequently the proposed gate with baseline (2nB_H) is
asymptotically impossible on every fixed nontrivial Gaussian window.  The
spectrally compatible gate has baseline (4(n-1)B_H).  It remains unproved
and is substantially stronger than MWB.

## 1. Integer floor and overload

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad N_q=\binom n{m-q},
\]

and write

\[
a_q=\frac{W}{N_q}=c_q+\theta_q,\qquad
t_q=N_q\theta_q=W-c_qN_q.
\]

For an exact factor (F), let \(\mu_q(S)\) be its depth-(q) load and set

\[
V_q(F)=\sum_S(\mu_q(S)-a_q)^2,\qquad
V_q^{\min}=N_q\theta_q(1-\theta_q).
\]

Robin--Hood transfers prove that (V_q^{\min}) is the minimum over all
integer load vectors of mass (W).  More precisely, with

\[
d_S=\mu_q(S)-c_q,
\]

one has the exact identity

\[
\boxed{
V_q(F)-V_q^{\min}=\sum_S d_S(d_S-1)=:Q_q(F).}
\tag{1.1}
\]

If

\[
D_q^-:=\sum_S(-d_S)_+,\qquad
D_q^+:=\sum_S(d_S-1)_+,
\]

then the balanced overload is

\[
O_q(F)=\max\{D_q^-,D_q^+\}.
\]

For every integer (d),

\[
d(d-1)\ge 2\bigl((-d)_+ +(d-1)_+\bigr).
\]

Hence the proposal's bound is correct, and the exact stronger form is

\[
\boxed{
Q_q(F)\ge2(D_q^-+D_q^+)\ge2O_q(F).}
\tag{1.2}
\]

## 2. Exact ownership-component switching

Overlay (F) and \(\tau F\) in the bipartite ownership graph whose edges are
the middle (m)-sets.  Every row vertex has degree (n).  Therefore every
connected component has equally many rows on its two sides, and each complete
side partitions the same set of middle masks.  Choosing one complete side in
each component always gives another exact factor.  This remains true even if
the two factor families have coincident wreaths, because the left and right
copies are distinct vertices in the bipartite overlay.

For a component (C), let (u_{q,C}) and (w_{q,C}) be its two complete-side
histograms.  Fair independent side choices give

\[
\boxed{
\mathbb E V_q(F')=
\left\|\frac{\mu_q+\tau\mu_q}{2}-a_q\mathbf1\right\|_2^2
+\frac14\sum_C\|u_{q,C}-w_{q,C}\|_2^2.}
\tag{2.1}
\]

Since coordinate relabeling preserves the norm of the centered histogram,
the parallelogram identity gives

\[
\boxed{
V_q(F)=
\left\|\frac{\mu_q+\tau\mu_q}{2}-a_q\mathbf1\right\|_2^2
+\frac14\|\mu_q-\tau\mu_q\|_2^2.}
\tag{2.2}
\]

Thus every factor (1/4) and the subtraction direction in the proposal are
correct.

Fix (H\le m-1), and let (F) globally minimize

\[
E_H(F):=\sum_{q\le H}\frac{Q_q(F)}{c_q}
\]

over the finite exact-factor fibre.  Define

\[
\begin{aligned}
A_{\tau,H}&:=\sum_{q\le H}
  \frac{\|\mu_q-\tau\mu_q\|_2^2}{c_q},\\
N_{\tau,H}&:=\sum_C\sum_{q\le H}
  \frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q}.
\end{aligned}
\]

Every switched child is exact, so global minimality and (2.1)--(2.2) imply

\[
\boxed{A_{\tau,H}\le N_{\tau,H}}
\tag{2.3}
\]

for every transposition.  Equivalently,

\[
N_{\tau,H}-A_{\tau,H}
=4\bigl(\mathbb E E_H(F')-E_H(F)\bigr)\ge0.
\tag{2.4}
\]

This conclusion requires a global minimizer of the same (H)-window
objective.  It is not valid for an arbitrary exact factor merely because the
switch is legal.

## 3. The sharp Johnson coefficient

Let (r=m-q) and

\[
f_q=\mu_q-a_q\mathbf1.
\]

The generic Johnson identity is

\[
\sum_\tau\|f-\tau f\|_2^2
=2\sum_j j(n-j+1)\|f^{(j)}\|_2^2,
\tag{3.1}
\]

where (f^{(j)}) is the Johnson harmonic of degree (j).  For a general
mean-zero function the first possible degree is (j=1), and (3.1) indeed
gives the proposal's valid estimate

\[
\sum_\tau\|f-\tau f\|_2^2\ge2n\|f\|_2^2.
\]

Exact wreath loads have more symmetry.  For every coordinate (x), each
wreath has exactly (r) cyclic (r)-intervals containing (x), so

\[
\sum_{S\ni x}\mu_q(S)=\frac{rW}{n}.
\]

The constant vector has the same point margin:

\[
a_q\binom{n-1}{r-1}=\frac{rW}{n}.
\]

Thus every point-star sum of (f_q) is zero.  Both Johnson degrees (0) and
(1) vanish, and (3.1) yields the sharp applicable bound

\[
\boxed{
\sum_\tau\|f_q-\tau f_q\|_2^2
\ge4(n-1)\|f_q\|_2^2.}
\tag{3.2}
\]

The coefficient is attained on the ambient degree-(2) subspace.  This is a
spectral sharpness statement, not an assertion that an exact factor attains
equality.

## 4. Correct aggregate ledger

Put

\[
\begin{aligned}
B_H&:=\sum_{q\le H}\frac{V_q^{\min}}{c_q},\\
S_H&:=\sum_{q\le H}\frac{V_q(F)}{c_q}=B_H+E_H(F),\\
D_H&:=\sum_\tau A_{\tau,H},\\
R_H&:=\sum_\tau N_{\tau,H},\\
P_H&:=\sum_{q\le H}\frac{O_q(F)}{c_q}.
\end{aligned}
\]

At the global minimizer, (2.3), (3.2), and (1.2) give

\[
\boxed{
R_H\ge D_H\ge4(n-1)(B_H+E_H(F))}
\tag{4.1}
\]

and

\[
\boxed{
P_H\le\frac{E_H(F)}2
\le\frac{R_H-4(n-1)B_H}{8(n-1)}.}
\tag{4.2}
\]

This is the strongest direct overload consequence of the minimizer argument.

There is an exact nonnegative slack decomposition:

\[
\boxed{
\begin{aligned}
R_H-4(n-1)B_H
={}&(R_H-D_H)\\
&+\bigl(D_H-4(n-1)(B_H+E_H)\bigr)\\
&+4(n-1)E_H.
\end{aligned}}
\tag{4.3}
\]

The middle slack is exactly

\[
2\sum_{q\le H}\frac1{c_q}\sum_{j\ge3}
\bigl(j(n-j+1)-2(n-1)\bigr)\|f_q^{(j)}\|_2^2.
\tag{4.4}
\]

## 5. The proposed (2nB_H) gate is impossible

The submitted gate was

\[
R_H\le2nB_H+o(nW).
\tag{5.1}
\]

Together with (4.1), it would force

\[
(2n-4)B_H+4(n-1)E_H=o(nW).
\tag{5.2}
\]

On every fixed window (H_A=\lceil A\sqrt m\rceil), (A>0), the floor
baseline is not small.  Uniformly for (q\le A\sqrt m),

\[
a_q=\exp\left(\frac{q(q+1)}m+O_A(m^{-1/2})\right).
\]

If

\[
g(y)=\frac{\{y\}(1-\{y\})}{y\lfloor y\rfloor},
\]

with (g(k)=0) at the positive integers, then (g) is continuous on the
relevant compact interval and

\[
\frac{V_q^{\min}}{c_qW}=g(a_q).
\]

Therefore the Riemann-sum limit is

\[
\boxed{
\frac{B_{H_A}}{W\sqrt m}\longrightarrow
\kappa_A:=\int_0^A
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
{e^{x^2}\lfloor e^{x^2}\rfloor}\,dx>0.}
\tag{5.3}
\]

The first term in (5.2) is consequently
\(\Theta_A(nW\sqrt m)\), not (o(nW)).  Thus (5.1) is infeasible on every
fixed nontrivial Gaussian window and hence on the intended growing MWB
window as well.  It is not a usable remaining lemma.

## 6. Repaired gate and strongest exact consequence

The spectrally compatible sufficient condition is

\[
\boxed{
R_H\le4(n-1)B_H+o(nW),}
\tag{6.1}
\]

imposed at a global minimizer of the same (H)-window objective.  By (4.2),
it implies

\[
E_H=o(W),\qquad P_H=o(W),
\]

and hence the desired fixed-window MWB conclusion.

More is forced.  Since all three terms in (4.3) are nonnegative, (6.1)
implies simultaneously

\[
\begin{aligned}
R_H-D_H&=o(nW),\\
D_H-4(n-1)(B_H+E_H)&=o(nW),\\
E_H&=o(W).
\end{aligned}
\tag{6.2}
\]

For (n\to\infty), (4.4) further gives

\[
\boxed{
\sum_{q\le H}\frac1{c_q}
\sum_{j\ge3}\|f_q^{(j)}\|_2^2=o(W).}
\tag{6.3}
\]

Thus a factor satisfying (6.1) must be simultaneously floor-balanced up to
(o(W)), have almost all of its centered variance in Johnson degree (2),
and have only (o(nW)) aggregate fair-switch drift.  The corrected gate is
therefore a highly rigid component-noise theorem, not merely a reformulation
of MWB.

## Final status

* Exact component switching: **accepted**.
* Quadratic floor and (2O_q\le V_q-V_q^{\min}): **accepted**, with the
  stronger pointwise ledger (1.2).
* Fair-switch identity and global-minimizer direction: **accepted**.
* Generic (2n) Johnson estimate: **valid but inapplicably weak**.
* Sharp exact-factor coefficient: **(4(n-1))**.
* Submitted (2nB_H) gate: **formally sufficient but asymptotically
  impossible**.
* Repaired (4(n-1)B_H) gate: **sufficient but unproved**, with the rigid
  consequences (6.2)--(6.3).
