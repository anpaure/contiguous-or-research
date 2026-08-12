# Proposed global component-noise minimizer reduction (raw)

This note records the corrected component-switching proposal submitted in
the main thread. It does not claim MWB.

Put

\[
n=2m+1,\quad W=\binom nm,\quad N_q=\binom n{m-q},\quad
a_q=W/N_q=c_q+\theta_q,
\]

and let \(t_q=W-c_qN_q=N_q\theta_q\).

## Exact switching

For exact factors \(F\) and \(\tau F\), form the bipartite ownership
overlap graph whose edges are the middle \(m\)-sets. In each connected
component, the two sides have the same number of wreaths and partition the
same middle sets. Independently choosing one complete side of every
component therefore gives another exact factor.

## Quadratic floor

Define

\[
V_q(F)=\sum_S(\mu_q(S)-a_q)^2,
\]

and

\[
V_q^{\min}
=(N_q-t_q)\theta_q^2+t_q(1-\theta_q)^2
=N_q\theta_q(1-\theta_q).
\tag{1}
\]

The proposal proves by Robin-Hood transfers that

\[
2O_q(F)\le V_q(F)-V_q^{\min}.
\tag{2}
\]

## One switch

For one transposition \(\tau\) and ownership component \(C\), let
\(u_{q,C}\) and \(w_{q,C}\) be its two side-load vectors. A fair independent
component choice gives

\[
\mathbb E V_q(F')
=\left\|\frac{\mu_q(F)+\tau\mu_q(F)}2-a_q\mathbf1\right\|_2^2
+\frac14\sum_C\|u_{q,C}-w_{q,C}\|_2^2,
\tag{3}
\]

whereas

\[
V_q(F)
=\left\|\frac{\mu_q(F)+\tau\mu_q(F)}2-a_q\mathbf1\right\|_2^2
+\frac14\|\mu_q(F)-\tau\mu_q(F)\|_2^2.
\tag{4}
\]

## Global minimizer and proposed criterion

Let \(F\) globally minimize

\[
\Phi_H(F)=\sum_{q=1}^H\frac{V_q(F)-V_q^{\min}}{c_q}.
\]

Minimality and (3)--(4) imply for every transposition

\[
\sum_q\frac{\|\mu_q(F)-\tau\mu_q(F)\|_2^2}{c_q}
\le
\sum_C\sum_q\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q}.
\tag{5}
\]

For functions on rank-\(r\) subsets, the proposal uses

\[
\sum_{\tau\text{ transposition}}\|f-\tau f\|_2^2
\ge2n\|f-\bar f\mathbf1\|_2^2.
\tag{6}
\]

Define

\[
R_H(F)=\sum_\tau\sum_{C\in\mathcal C_\tau(F)}
\sum_{q=1}^H\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q}.
\tag{7}
\]

Then (2), (5), and (6) give

\[
\sum_{q=1}^H\frac{O_q(F)}{c_q}
\le\frac{R_H(F)}{4n}
-\frac12\sum_{q=1}^H\frac{V_q^{\min}}{c_q}.
\tag{8}
\]

Thus the unproved sufficient criterion is

\[
R_{H_m}(F_m)
\le2n\sum_{q=1}^{H_m}\frac{V_q^{\min}}{c_q}+o(nW).
\tag{9}
\]

It involves only exact factor-preserving switches. The open issue is the
component-noise upper bound in (9); crude component-size estimates are much
too large. The proposal also rejects a wildcard-marker matching idea because
one-marker/n-middle incidence forces equal average weighted degrees across
the two parts, while the wreath system has no separate one-marker completion
edges.

