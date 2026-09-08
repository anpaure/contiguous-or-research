# Support-matched trade Dirichlet identity

Date: 2026-07-27

## 1. Exact identity

Fix a depth \(q\).  Let \(\mu_q(S)\) be the load of an exact wreath factor,
let \(c_q=\lfloor W/N_q\rfloor\), and put

\[
 \Phi_q(F)=\sum_S \binom{\mu_q(S)-c_q}{2}
 =\frac12\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\]

This is the CPCR potential.  Let \((R,A)\) be a support-matched wreath trade
and define its depth-\(q\) signed load change by

\[
 \Delta_q(S)=\mu_q^A(S)-\mu_q^R(S).
\]

Both sides contain the same number of wreaths, hence
\(\sum_S\Delta_q(S)=0\).  Expanding one quadratic gives

\[
\boxed{
 \Phi_q((F\setminus R)\cup A)-\Phi_q(F)
 =\langle\mu_q,\Delta_q\rangle
   +\frac12\|\Delta_q\|_2^2.
}                                                       \tag{1.1}
\]

Equivalently, with

\[
 G_q=-\langle\mu_q,\Delta_q\rangle,
 \qquad
 D_q=\frac12\|\Delta_q\|_2^2,
\]

the change is \(D_q-G_q\).  We call \(G_q\) the coherent compensation gain
and \(D_q\) the trade noise or Dirichlet cost.

### Proof

For \(f(x)=\frac12(x-c_q)(x-c_q-1)\),

\[
 f(x+d)-f(x)=d(x-c_q-	frac12)+\tfrac12d^2.
\]

Sum over \(S\).  The term
\(-(c_q+\frac12)\sum_S\Delta_q(S))\) vanishes.  This yields (1.1).  Since an
integer zero-mass vector has even squared norm, \(D_q\) is an integer. \(\square\)

## 2. Weighted form and the MWB implication

For a height \(H\), define

\[
 \Phi_H(F)=\sum_{q\le H}\frac{\Phi_q(F)}{c_q},\qquad
 G_H=\sum_{q\le H}\frac{G_q}{c_q},\qquad
 D_H=\sum_{q\le H}\frac{D_q}{c_q}.
\]

Then every support-matched trade satisfies exactly

\[
 \Phi_H(F')-\Phi_H(F)=D_H-G_H.            \tag{2.1}
\]

The quadratic certificate for balanced overload gives

\[
 O_q(F)\le \Phi_q(F).
\]

Consequently

\[
 \sum_{q\le H}\frac{O_q(F)}{c_q}\le\Phi_H(F).       \tag{2.2}
\]

Thus \(\Phi_H=o(W)\) is a sufficient, exact integral condition for MWB.

## 3. The remaining stochastic theorem in one inequality

Suppose that for every exact factor \(F\) one can choose a distribution on
legal support-matched trades such that

\[
 \boxed{
 \mathbb E(G_H-D_H)
 \ge \eta_m\Phi_H(F)-\varepsilon_m W,
 \qquad \varepsilon_m/\eta_m\longrightarrow0.
 }                                                     \tag{3.1}
\]

Let \(F_*\) minimize \(\Phi_H\) among exact factors.  Every outcome of the
trade distribution is another exact factor, so

\[
 0\le\mathbb E[\Phi_H(F_*')-\Phi_H(F_*)]
 =\mathbb E(D_H-G_H).
\]

Combining with (3.1) gives

\[
 \Phi_H(F_*)\le\frac{\varepsilon_m}{\eta_m}W=o(W).
\]

By (2.2), MWB follows.  This isolates the surviving compensation-coin gate:
the coherent correction must dominate the exact Dirichlet noise, on average,
by a positive fraction of the current CPCR excess.

This is not claimed as a proof of (3.1).  It is the lossless theorem that a
trade construction must establish.

### Deterministic supersaturation variant

For existence alone, no quantitative drift rate is needed.  It is enough to
prove the following statement for every fixed \(\varepsilon>0\): whenever

\[
 \Phi_H(F)\ge\varepsilon W,
\]

there is one legal support-matched trade with

\[
 G_H>D_H.                                             \tag{3.2}
\]

Indeed, a global minimizer of \(\Phi_H\) cannot admit a decreasing trade, so
(3.2) forces \(\Phi_H<\varepsilon W\).  Diagonalizing in \(\varepsilon\)
and using (2.2) proves MWB.  We call (3.2) the **mesoscopic
compensation-trade supersaturation theorem**.  It is weaker than a uniform
drift inequality and is the sharpest deterministic target exposed by the
search.

## 4. Search implementation and calibration

`quadratic_trade_stats` in
`scratch/math_aware_search_metrics.py` computes \(G_q,D_q,D_q-G_q\) and
checks (1.1) against independently recomputed CPCR values.  Every newly
emitted support-trade certificate contains the per-depth decomposition.

For the second complete five-block improvement at \(m=5\),

\[
\begin{array}{c|rrr}
q&G_q&D_q&\Delta\Phi_q\\ \hline
1&4&5& 1\\
2&24&13&-11\\
3&38&14&-24\\
4,5&0&0&0
\end{array}
\]

so the aggregate coherent gain is 66, the noise is 32, and CPCR falls by
34.  Depth one worsens by one unit, while the coupled depth-two and
depth-three correction more than pays for it.  This is a concrete
counterexample to any search or proof rule requiring monotone improvement at
each depth.

At the next five-block state, the complete trade catalogue contains 259
closed trades.  Uniform choice fails badly: mean weighted coherent gain is
\(19251/2072\), while mean weighted noise is \(37077/2072\).  Nevertheless,
20 trades improve unweighted CPCR and the selected trade has weighted gain
14 against weighted noise \(99/8\), hence weighted CPCR change \(-13/8\).
This finite calculation says exactly what (3.2) must capture: favorable
trades are a structured minority, not the output of uniform averaging.

## 5. Structural lesson

The finite trade search and the asymptotic gate are now expressed in the same
currency:

* support closure guarantees exact integrality at the middle layer;
* \(G_H\) measures correlation with the current imbalance;
* \(D_H\) measures the unavoidable collision cost of moving load; and
* (3.1) is precisely the assertion that compatible trades have a restoring
  bias larger than their quadratic noise.

The next mathematical target is therefore not generic expansion of the
wreath catalogue.  It is a structured family of support-matched trades for
which the averaged signed shadow vector has the compensation property (3.1)
simultaneously over the mesoscopic band.
