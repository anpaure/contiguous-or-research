# Current compact missing theorems

Either problem below, proved for every fixed (A>0), completes the
coefficient-one contiguous-OR upper bound after the audited fixed-window
diagonalization and tails.

## Problem 1: fractional survival-packet cover

Put

\[
n=2m+1,qquad W=\binom{n}{m},qquad
t=W/n=\operatorname{Cat}_m,qquad H=\lceil A\sqrt m\rceil .
\]

Construct one exact middle wreath factor (F).  For every (q\le H),
choose a balanced quota vector

\[
\beta_q(S)\in\{c_q,c_q+1\},qquad
c_q=\left\lfloor\frac{W}{\binom{n}{m-q}}\right\rfloor,qquad
\sum_S\beta_q(S)=W.
\]

Let (mathcal O(q,S)\subseteq F) be the wreaths in which (S) occurs as a
cyclic interval of length (m-q).  Find weights (x_E\in[0,1]), (E\in F),
such that

\[
\sum_{E\in P}x_E\ge1
\]

for every (q\le H), every (S), and every subset

\[
P\subseteq\mathcal O(q,S),qquad |P|=\beta_q(S)+1,
\]

while

\[
\boxed{\sum_{E\in F}x_E=o_A(t/\sqrt m).}
\]

This is the exact fractional survival-packet theorem (mathrm{FSP}_A).
Bounded-rank threshold rounding already converts it into one integral
quota-safe exceptional family, and the direct ledger gives

\[
\sum_{q\le H}\frac{O_q(F)}{c_q}\le3nH\sum_Ex_E=o(W).
\]

Fractional marginals chosen separately at different depths, a factor chosen
separately for each depth, or an unextendible near-factor do not count.

## Problem 2: stateful global-portal extraction

Put

\[
W_e=\binom{2m}{m},qquad H=\lceil A\sqrt m\rceil.
\]

Construct one literal (H)-legal middle-owner MTF path system, one ordering
of its pieces, exact MTF bridges, and one proper trace set (Z\), such that

\[
\boxed{\mathfrak P_H+\Phi_Z(\mathcal H_H)=o(W_e).}
\]

Here (mathfrak P_H) is the exact initialization-plus-bridge excess and
(Phi_Z) is the audited fixed-trace repair functional for the canonical
band holes.  Equivalently, extract (W_e-o(W_e)) distinct useful central
portal targets along one legal state walk with only (o(W_e)) connectors
and (o(W_e)) trace repair.

The portal incidence is already available at the sharp scale:
(Theta(W_e/\sqrt m)) high-degree endpoints can carry (Theta(W_e))
cross-box incidence.  The missing part is stateful fusion.  Canonical pieces
also obey the proved residual dichotomy: with (o(W_e)) portal excess and
deepest-upper defect, only (o(W_e/H)) components may be depleted, but
those components must contain a positive fraction of all middle owners and
have average length (omega(H)).  Isolated arms, singleton pieces, cyclic
strips, and odd-cut geodesics do not solve the problem.

There is now a genuine sub-Gaussian positive theorem: long projected-strip
components give a (W_e+o(W_e)) word for any selected signed-depth set
(D) satisfying

\[
|D|\,\max_{d\in D}|d|\,\log\log m=o(\log m).
\]

In particular, fixed many rows reach
(H=o(\log m/\log\log m)), while a full band reaches
(H=o(\sqrt{\log m/\log\log m})).  The missing theorem must extend this
simultaneous support from sparse/sublogarithmic rows to every row of a fixed
Gaussian window.

## Exact status

Neither boxed theorem is proved.  The former dominant three-box and uniform
compact four-box local coefficient-one prompts are false and should not be
assigned as missing lemmas.  Nonlocal exact-factor trades and rotor/SCD
low-switch resolution remain additional live routes.
