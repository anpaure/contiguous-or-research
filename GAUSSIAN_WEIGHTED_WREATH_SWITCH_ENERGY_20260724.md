# Gaussian-weighted wreath energy and the balanced-switch gate

## 1. Result and limitation

Put

\[
 n=2m+1,
 \qquad W=\binom nm,
 \qquad N_q=\binom n{m-q},
 \qquad d_q=\left\lfloor\frac W{N_q}\right\rfloor.
\]

For an exact middle wreath factor \(F\), let \(O_q(F)\) be its minimum
overflow above a balanced floor/ceiling quota at depth \(q\), and let
\(Q_q(F)\) be its quadratic capacity energy.  Define

\[
 \mathcal G_H(F)=\sum_{q=1}^H\frac{Q_q(F)}{d_q}.    \tag{1.1}
\]

The Gaussian-capacity transfer and the symmetric-chain product tail imply
the following unconditional reduction:

> If \(\sqrt m\ll H=o(m)\) and exact wreath factors satisfy
> \(\mathcal G_H(F_m)=o(W)\), then
> \(\nu(2m+1)\le W+o(W)\), and the same leading constant follows in even
> dimensions.

This condition is stronger than the optimal weighted-overload condition

\[
 \sum_{q\le H}\frac{O_q(F)}{d_q}=o(W),             \tag{1.2}
\]

but it has two advantages: it is an exact quadratic harmonic norm, and its
change under every balanced alternating-eight switch is explicit.

The main new estimate is that the total quadratic switch toll in this
Gaussian norm is only

\[
 \boxed{16\sum_{q=1}^H\frac q{d_q}=O(m)}           \tag{1.3}
\]

uniformly for every \(H\le m/2\).  The corresponding unweighted toll is
\(O(H^2)\).  At the now-sufficient depth
\(H=\sqrt m\,\omega(m)\), (1.3) removes the entire \(\omega(m)^2\)
penalty.

This does not prove a descent theorem.  It reduces the old polynomial drift
gap to a constant-scale boundary: a mean linear drift
\(\kappa\mathcal G_H\) bounds every local minimum by \(O(m/\kappa)\), so a
coefficient-one proof follows if \(\kappa W/m\to\infty\).  The naive
two-wreath exposure scale is only \(\Theta(m/W)\), which gives \(O(W)\)
rather than \(o(W)\).  Neutral routing, a sharper overload potential, or a
larger amortized trade is still needed.

## 2. Weighted overload is the exact transfer parameter

At depth \(q\), write the load vector as \(\mu_q\), and write

\[
 W=c_qN_q+r_q,
 \qquad 0\le r_q<N_q.
\]

A balanced quota vector has entries in \(\{c_q,c_q+1\}\), with exactly
\(r_q\) high entries.  Define

\[
 O_q(F)=\min_b\sum_S(\mu_q(S)-b(S))_+.             \tag{2.1}
\]

The exact balanced-overflow identity from
`WREATH_MULTIDEPTH_8SWITCH_ENERGY_20260724.md` gives

\[
 \boxed{O_q(F)\le Q_q(F).}                         \tag{2.2}
\]

Since \(W\ge N_q\), every balanced quota is at least
\(d_q=\lfloor W/N_q\rfloor\).  If \(M_q\) targets are missing, their total
quota deficit is at least \(d_qM_q\).  Total underload equals total overload,
so

\[
 \boxed{M_q\le\frac{O_q(F)}{d_q}
 \le\frac{Q_q(F)}{d_q}.}                           \tag{2.3}
\]

Linearizing every wreath through depth \(H\) and repairing each lower hole
and its complementary upper hole therefore gives

\[
\begin{aligned}
 \nu(2m+1)\le{}&
 W+\frac{2H+1}{2m+1}W
 +2\sum_{q=1}^H\frac{Q_q(F)}{d_q}\\
 &+2L_m(m-H-1),                                   \tag{2.4}
\end{aligned}
\]

where \(L_m\) is the exact symmetric-chain product tail length.  The tail
theorem gives

\[
 L_m(m-H-1)=o\!\left(\binom{2m}m\right)=o(W)       \tag{2.5}
\]

whenever \(H/\sqrt m\to\infty\), uniformly for \(H=o(m)\).  The seam in
(2.4) is also \(o(W)\).  This proves the reduction in Section 1.

## 3. Exact harmonic form

Let \(\Omega\) be the oriented cyclic orders modulo rotation, and let
\(A_r\) record all \(n\) cyclic \(r\)-intervals in an order.  Orient the
wreaths of \(F\) arbitrarily and let \(x\) be their indicator.  Put

\[
 x_0=\frac1{m!(m+1)!}{\bf1}_\Omega,
 \qquad y=x-x_0.                                  \tag{3.1}
\]

Then

\[
 A_my=0,
 \qquad
 A_{m-q}y=\mu_q-\frac W{N_q}{\bf1}.               \tag{3.2}
\]

The exact integer-floor calculation gives

\[
 \boxed{
 Q_q(F)=\frac12\|A_{m-q}y\|_2^2
 -\frac{r_q(N_q-r_q)}{2N_q}.}                     \tag{3.3}
\]

The subtracted term is independent of \(F\).  Thus \(\mathcal G_H\) is a
Gaussian-weighted middle-kernel harmonic norm, up to a fixed quantization
constant.  Total and point margins are fixed, so every vector in (3.2) lies
in Specht degrees \(j\ge2\).

The common-column spectrum is computed in
`WREATH_CROSS_RANK_SPECTRAL_20260724.md`.  In particular, the exact fraction
of the degree-two rank-\((m-q)\) frame which survives projection to
\(\ker A_m\) is

\[
\boxed{
 \sin^2\theta_{m,m-q;2}
 =\frac{2q(q+1)
 \bigl((2q+1)m-(2q^2+2q-1)\bigr)}
 {(m^2-1)
 \bigl(m^2+(2q+1)m-3q(q+1)\bigr)}.}
\tag{3.4}
\]

Uniformly for \(q=o(m)\),

\[
 \sin^2\theta_{m,m-q;2}
 =\frac{2q(q+1)(2q+1)}{m^3}
 \left(1+O\!\left(\frac qm\right)\right).         \tag{3.5}
\]

Hence the slow degree-two mode remains thin throughout the reduced vertical
range; at \(q=\sqrt m\,\omega\) its relative leakage is
\(\Theta(\omega^3/m^{3/2})\).

## 4. Exact Gaussian-weighted switch update

For a balanced two-wreath alternating-eight switch \(C\), let
\(\delta_{C,q}\) be the exact depth-\(q\) load change.  The seam-cancellation
theorem gives

\[
 \sum_S\delta_{C,q}(S)=0,
 \qquad
 \|\delta_{C,q}\|_2^2\le32q.                     \tag{4.1}
\]

The quadratic identity is

\[
 Q_q(F\triangle C)-Q_q(F)
 =\sum_S\mu_q(S)\delta_{C,q}(S)
 +\frac12\|\delta_{C,q}\|_2^2.                   \tag{4.2}
\]

Define the Gaussian linear score

\[
 \Lambda_C^{\rm G}(F)
 =\sum_{q=1}^H\frac1{d_q}
 \sum_S\mu_q(S)\delta_{C,q}(S).                  \tag{4.3}
\]

Summing (4.2) gives the exact upper bound

\[
 \boxed{
 \mathcal G_H(F\triangle C)-\mathcal G_H(F)
 \le \Lambda_C^{\rm G}(F)
 +16\sum_{q=1}^H\frac q{d_q}.}                   \tag{4.4}
\]

## 5. The Gaussian curvature sum is \(O(m)\)

The exact binomial ratio is

\[
 u_q:=\frac W{N_q}
 =\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}.             \tag{5.1}
\]

Using \(\log(1-z)\le-z\),

\[
 u_q\ge
 \exp\!\left(\frac{q(q+1)}{m+q+1}\right).       \tag{5.2}
\]

Let \(q_0=\lceil2\sqrt m\rceil\).  For sufficiently large \(m\), (5.2)
gives \(u_q\ge2\) whenever \(q\ge q_0\).  Hence

\[
 d_q=\lfloor u_q\rfloor\ge\frac{u_q}{2}
 \qquad(q\ge q_0).                                \tag{5.3}
\]

For \(q<q_0\), use \(d_q\ge1\).  For
\(q_0\le q\le m/2\), equations (5.2)--(5.3) give

\[
 \frac1{d_q}
 \le2\exp\!\left(-\frac{q(q+1)}{m+q+1}\right)
 \le2e^{-2q^2/(3m)}.                              \tag{5.4}
\]

Therefore

\[
\begin{aligned}
 \sum_{q=1}^H\frac q{d_q}
 &\le \sum_{q<q_0}q
 +2\sum_{q\ge q_0}q e^{-2q^2/(3m)}\\
 &=O(m),                                           \tag{5.5}
\end{aligned}
\]

uniformly for every \(H\le m/2\).  Equations (4.4) and (5.5) prove (1.3).

## 6. The remaining drift statement

Suppose that throughout a balanced-switch-connected class there is a
probability distribution on legal balanced switches satisfying

\[
 \mathbb E_C\Lambda_C^{\rm G}(F)
 \le-\kappa\mathcal G_H(F).                       \tag{6.1}
\]

Then every local minimum of \(\mathcal G_H\) satisfies

\[
 \boxed{\mathcal G_H(F)=O(m/\kappa).}             \tag{6.2}
\]

Indeed, average (4.4) and use (5.5); if the right side were negative, some
legal switch would decrease the energy.

The Gaussian transfer needs \(\mathcal G_H=o(W)\), so (6.2) is sufficient
provided

\[
 \boxed{\kappa\gg m/W.}                           \tag{6.3}
\]

An unstructured random pair of the \(B=W/n\) wreaths has exposure scale
\(1/B=n/W=\Theta(m/W)\).  Thus Gaussian weighting eliminates the previous
diverging \(H^2/m\) loss, but a bare pair-exposure drift still lands at
\(O(W)\), not \(o(W)\).  A proof must obtain a growing gain from the many
seams, amortize curvature through a neutral route, or work directly with the
piecewise-linear overload \(O_q\), which has no integer quantization floor.

## 7. Status

**Proved here:** the sufficient Gaussian quadratic gate, its exact harmonic
form, the all-depth degree-two leakage formula, the weighted balanced-switch
update, and the uniform \(O(m)\) curvature bound.

**Still open:** the drift/neutral-routing theorem (6.1) at a scale beating
\(m/W\), or a direct weighted-overload switching theorem.  Hence this note
does not prove the coefficient-one bound.
