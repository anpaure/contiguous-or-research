# Lane C: a reflected-chart two-cut Haar block with quantitative Gaussian-window contraction

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or probabilistic experiment is used. Random signs below are only an
averaging device over a finite family of literal integral exact factors.

The only imported exact inputs are: the MSW reflection identity from
MATH_ATTACK_C_NONLOCAL_INVOLUTION_REFLECTION_NOGO_20260725.md; the genuine
\((2\ 3)\)-packet components and their four-arm profile from
MATH_ATTACK_AB5_AFR_OVERLAY_FRAGMENTATION_20260725.md and
MATH_ATTACK_M_HARMONIC_FLOOR_COMPONENT_NOGO_20260725.md; and the universal
growing-degree run-cap bound from
MATH_ATTACK_L_GROWING_HARMONIC_ROBUST_CUT_BOUNDARY_20260725.md, with its
dated cross-audits.  Every new compositional and quantitative step is proved
below.

## 0. The positive theorem

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
B=\operatorname{Cat}_m=\frac Wn,\qquad
H=\lceil A\sqrt m\rceil,
\tag{0.1}
\]

where \(A>0\) is fixed. At depth \(q\), put

\[
N_q=\binom n{m-q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\tag{0.2}
\]

and use the exact unhalved floor energy

\[
\mathcal Q_H(F)
=\sum_{q=1}^H\frac1{c_q}
 \sum_{|S|=m-q}
 (\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1).
\tag{0.3}
\]

Let \(F^0=F_m^{\rm MSW}\) be the canonical exact factor, let

\[
\sigma(i)=n-i\quad(1\le i\le2m),\qquad \sigma(n)=n,
\tag{0.4}
\]

and put

\[
\tau=(2\ 3),\qquad
\tau'=\sigma\tau\sigma=(2m-2\ \ 2m-1).
\tag{0.5}
\]

The exact MSW reflection theorem gives \(\sigma F^0=F^0\).

For \(R\in\mathcal D_{m-2}\), let \(K_R\) be the genuine size-two
\(\tau\)-component whose old rows are indexed by

\[
1100R,\qquad1010R.
\tag{0.6}
\]

Let \(\mathcal I\) be the terminal-chart-free indices

\[
\mathcal I=
\left\{R\in\mathcal D_{m-2}:
R\ne Q1100,Q1010\text{ for every }Q\in\mathcal D_{m-4}
\right\}.
\tag{0.7}
\]

Switch every \(K_R\), \(R\in\mathcal I\), and no other component:

\[
F^*=F^0+\sum_{R\in\mathcal I}z_R,
\qquad
z_R=\mathbf1_{\tau K_R}-\mathbf1_{K_R}.
\tag{0.8}
\]

This is a literal exact factor. Pair \(K_R\) with its reflected terminal
component \(\sigma K_R\). For a sign vector
\(\varepsilon\in\{\pm1\}^{\mathcal I}\), choose, independently for every
pair, exactly one of the following two exact states:

\[
\begin{array}{c|cc}
&U_R&\sigma U_R\\ \hline
\varepsilon_R=+1&\tau K_R&\sigma K_R\\
\varepsilon_R=-1&K_R&\sigma\tau K_R.
\end{array}
\tag{0.9}
\]

All unlisted roots retain their rows from \(F^0\). Denote the resulting
factor by \(F_\varepsilon\).

> **Reflected-chart contraction theorem.** For every fixed \(A>0\) and all
> sufficiently large \(m\), every \(F_\varepsilon\) in (0.9) is a literal
> exact factor reachable from \(F^*\) by at most two freshly recomputed
> transposition-component cuts, first in colour \(\tau\) and then in colour
> \(\tau'\). Every mixed sign vector is reached by exactly two nonempty
> proper cuts. If the signs are independent and fair, then
> \[
> \boxed{
> \mathbb E_\varepsilon\mathcal Q_H(F_\varepsilon)
> \le
> \mathcal Q_H(F^*)
> -\frac{B4^H}{512M_AH^4}+8HB,}
> \tag{0.10}
> \]
> where
> \[
> M_A=\left\lceil e^{2(A+1)(A+2)}\right\rceil.
> \tag{0.11}
> \]
> Consequently one nonconstant, non-global sign vector satisfies
> \[
> \boxed{
> \mathcal Q_H(F_\varepsilon)
> \le\mathcal Q_H(F^*)
> -\frac{B4^H}{1024M_AH^4}.}
> \tag{0.12}
> \]

There is also a full product version of the same block.  Let
\(G_{\alpha,\beta}\) use \(\tau K_R\) or \(K_R\) on \(U_R\) according as
\(\alpha_R=+1\) or \(-1\), and use \(\sigma\tau K_R\) or \(\sigma K_R\)
on \(\sigma U_R\) according as \(\beta_R=+1\) or \(-1\).  For independent
fair \(\alpha,\beta\),

\[
\boxed{
\mathbb E_{\alpha,\beta}\mathcal Q_H(G_{\alpha,\beta})
\le
\mathcal Q_H(F^*)
-\frac{B4^H}{512M_AH^4}+4HB.}
\tag{0.12a}
\]

Every product corner is again reachable by at most two fresh cuts.  The
diagonal specialization \(\beta=-\alpha\) is (0.9); it is retained because
its two constant corners are \(F^*\) and \(\sigma F^*\), so its strict
average decrease forces a mixed corner and hence two proper stages.

The block also contracts its entire reflection-anti-invariant Gaussian-window
profile by an exponentially small factor. With

\[
f(F)=(\mu_q^F-W/N_q)_{q\le H},\qquad
P_\sigma=\frac{I+\sigma}{2},\qquad
\|x\|_H^2=\sum_{q=1}^H\frac{\|x_q\|_2^2}{c_q},
\tag{0.13}
\]

one has

\[
\boxed{
\frac{\mathbb E_\varepsilon
 \|(I-P_\sigma)f(F_\varepsilon)\|_H^2}
 {\|(I-P_\sigma)f(F^*)\|_H^2}
\le
\frac{4096M_AH^5}{4^H}=o_A(1).}
\tag{0.14}
\]

The independently heated product block has the stronger right side
\(2048M_AH^5/4^H\) in (0.14).

Thus this is an actual correlated two-cut shield-burning block: neither the
empty choice nor the all-pairs choice improves energy, since they are the
equal-energy factors \(F^*\) and \(\sigma F^*\), but a mixed pairwise
choice has the strict quantitative decrease (0.12).

For the growing Johnson cutoff

\[
J=\left\lfloor\frac{\gamma H}{\log(108m)}\right\rfloor,
\qquad0<\gamma<\log4,
\tag{0.15}
\]

the same block satisfies

\[
\boxed{
\mathfrak A_\sigma^{>J}(F^*)
\ge\frac{B4^H}{128M_AH^4}-4U,
\qquad
\mathfrak V_{\times,\sigma}^{>J}(F^*)<16HB,}
\tag{0.16}
\]

where \(U=BH^3e^{\gamma H}/n\). Hence

\[
\boxed{
\frac{\mathfrak V_{\times,\sigma}^{>J}(F^*)}
{\mathfrak A_\sigma^{>J}(F^*)}=o_{A,\gamma}(1),
\qquad
\frac{\mathfrak V_{\Delta,\sigma}^{>J}(F^*)}
{\mathfrak A_\sigma^{>J}(F^*)}=o_{A,\gamma}(1).}
\tag{0.17}
\]

This is a suffix-weighted burnout theorem for the genuine two-chart
comparison and for its correlated diagonal circuit.  It is not a bound for
either individual transposition heat in isolation: \(\sigma\) is a nonlocal
reflection, whereas the literal implementation uses the two transpositions
\(\tau,\tau'\).  It also does not bound the reflection-invariant part of
\(f(F^*)\), so no constant-one conclusion is claimed.

Section 7 supplies the complementary same-phase block.  It stays entirely
inside the \(\sigma\)-invariant subspace and, from the higher-energy one of
two explicit coherent endpoints, two nonempty proper cuts give the same
decrease \(B4^H/(1024M_AH^4)\) and the same exponentially small contraction
factor.  What remains uncontrolled is the invariant midpoint, not both
chart parities.

## 1. Disjoint reflected chart roots

The components \(K_R\) are pairwise row-disjoint and their middle roots
\(U_R\) are pairwise disjoint. Reflection reverses the Dyck blocks and fixes
both gadgets \(1100,1010\), so \(\sigma K_R\) has old rows indexed by

\[
\mu(R)1100,\qquad\mu(R)1010.
\tag{1.1}
\]

The reflected components are genuine size-two \(\tau'\)-components and are
pairwise root-disjoint.

### Lemma 1.1

The roots

\[
\{U_R,\sigma U_R:R\in\mathcal I\}
\tag{1.2}
\]

are pairwise disjoint.

#### Proof

Disjointness within each of the two displayed families is already part of
the exact component decompositions. Suppose a row of \(K_R\) were also a
row of \(\sigma K_S\). The first representation begins with \(1100\) or
\(1010\), while the second ends with one of those two gadgets. Hence the
suffix \(R\) itself ends with \(1100\) or \(1010\), contrary to
\(R\in\mathcal I\). Thus the old row sets in the two families are mutually
disjoint.

Distinct rows of the exact factor \(F^0\) have disjoint middle ownership.
Therefore their two-row middle roots are disjoint as well. \(\square\)

It follows at once that (0.8) is an exact factor. It also shows that the
comparison of \(F^*\) with \(\sigma F^*\) has precisely two active connected
root components for every \(R\in\mathcal I\):

\[
\tau K_R\longleftrightarrow K_R
\quad\text{on }U_R,
\qquad
\sigma K_R\longleftrightarrow\sigma\tau K_R
\quad\text{on }\sigma U_R.
\tag{1.3}
\]

Reflection interchanges the two components in (1.3). Correlating their two
side choices oppositely gives exactly the binary bundle (0.9). Since all
roots are disjoint, the bundle choices are independent and every corner is
an exact factor.

## 2. Literal two-cut realization

Fix a subset \(S\subset\mathcal I\). Starting at \(F^*\), first use the
fresh \(\tau\)-overlay and switch exactly the persistent components on
\(U_R\), \(R\in S\), back from \(\tau K_R\) to \(K_R\). Next use the
freshly recomputed \(\tau'\)-overlay and switch exactly the components on
\(\sigma U_R\), \(R\in S\), from \(\sigma K_R\) to
\(\sigma\tau K_R\).

Every \(U_R\) is \(\tau\)-invariant, and every \(\sigma U_R\) is
\(\tau'\)-invariant. Therefore neither an overlay edge nor a freshly
recomputed ownership component can cross one of these root boundaries.
The first cut does not change any reflected root, so the terminal components
in the second cut persist exactly. This proves that the two stages are legal
fresh component cuts and that their endpoint is the corner with
\(\varepsilon_R=-1\) exactly on \(S\).

For the decreasing corner supplied below, \(S\) is neither empty nor all of
\(\mathcal I\). Thus both cuts are nonempty and proper. The construction has
no fractional intermediate state.

The product corner \(G_{\alpha,\beta}\) is realized similarly, now with
two independently prescribed index sets.  In the first fresh overlay revert
exactly the \(U_R\) for which \(\alpha_R=-1\); in the second fresh overlay
switch exactly the \(\sigma U_R\) for which \(\beta_R=+1\).  The same
invariance and persistence argument proves literal exactness and reachability
by at most two cuts for every product corner.

## 3. Exact Haar identity for the reflected bundles

Let

\[
d_R=(B_{m-q}z_R)_{q\le H},\qquad
D=\sum_{R\in\mathcal I}d_R,
\tag{3.1}
\]

where the stacked norm is

\[
\|x\|_H^2=\sum_{q=1}^H\frac{\|x_q\|_2^2}{c_q}.
\tag{3.2}
\]

Put

\[
h_R=d_R-\sigma d_R,
\qquad
\mathfrak A=\left\|\sum_{R\in\mathcal I}h_R\right\|_H^2,
\qquad
\mathfrak V_\Delta=\sum_{R\in\mathcal I}\|h_R\|_H^2,
\tag{3.3}
\]

Because \(F^0\) is \(\sigma\)-invariant,

\[
f(F^*)-\sigma f(F^*)=D-\sigma D=\sum_Rh_R.
\tag{3.4}
\]

The exact load at a corner is

\[
f(F_\varepsilon)
=P_\sigma f(F^*)+\frac12\sum_{R\in\mathcal I}\varepsilon_Rh_R.
\tag{3.5}
\]

The two terms on the right are orthogonal. Independent fair signs kill all
cross terms between distinct bundles, so

\[
\mathbb E_\varepsilon
\|(I-P_\sigma)f(F_\varepsilon)\|_H^2=\frac{\mathfrak V_\Delta}4,
\qquad
\|(I-P_\sigma)f(F^*)\|_H^2=\frac{\mathfrak A}4.
\tag{3.6}
\]

To keep the floor baseline explicit, write
\(W/N_q=c_q+\theta_q\), \(0\le\theta_q<1\).  Since every exact factor has
total depth-\(q\) load \(W\), one has \(\sum_S f_q(F)(S)=0\), and hence

\[
\frac1{c_q}\sum_S
 (\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)
=\frac{\|f_q(F)\|_2^2}{c_q}
 +\frac{N_q\theta_q(\theta_q-1)}{c_q}.
\tag{3.6a}
\]

The second term is independent of \(F\). Consequently

\[
\boxed{
\mathbb E_\varepsilon
[\mathcal Q_H(F_\varepsilon)-\mathcal Q_H(F^*)]
=\frac{\mathfrak V_\Delta-\mathfrak A}{4}.}
\tag{3.7}
\]

This identity is exact and uses one common sign per reflected component
pair at every retained depth.

For completeness, the independently signed product block satisfies

\[
f(G_{\alpha,\beta})
=P_\sigma f(F^*)+\frac12\sum_R
 (\alpha_Rd_R+\beta_R\sigma d_R).
\tag{3.8}
\]

Put

\[
\mathfrak V_\times
=\sum_R(\|d_R\|_H^2+\|\sigma d_R\|_H^2)
=2\sum_R\|d_R\|_H^2.
\tag{3.9}
\]

Independence, orthogonality of distinct Rademacher monomials, and the same
floor cancellation give the second exact Haar identity

\[
\boxed{
\mathbb E_{\alpha,\beta}
[\mathcal Q_H(G_{\alpha,\beta})-\mathcal Q_H(F^*)]
=\frac{\mathfrak V_\times-\mathfrak A}{4}.}
\tag{3.10}
\]

Moreover, since
\((I-P_\sigma)d_R=h_R/2\) and
\((I-P_\sigma)\sigma d_R=-h_R/2\),

\[
\mathbb E_{\alpha,\beta}
\|(I-P_\sigma)f(G_{\alpha,\beta})\|_H^2
=\frac{\mathfrak V_\Delta}{8}.
\tag{3.11}
\]

## 4. Catalan coherent lower bound

Put

\[
d=m-H-2.
\tag{4.1}
\]

For \(V_0\in\mathcal D_d\), the private-pair formula restricts the packet
indices to

\[
R=UV_0,\qquad U\in\mathcal D_H.
\tag{4.2}
\]

All \(\operatorname{Cat}_H\) choices of \(U\) contribute the same oriented
unit dipole on the target pair

\[
\{\mathcal C_{V_0}\cup\{2\},
  \mathcal C_{V_0}\cup\{3\}\},
\qquad
\mathcal C_{V_0}
=(4+2H+\mathsf A(V_0))\cup\{n\}.
\tag{4.3}
\]

Every other arm omits the marker \(n\), so it cannot cancel these
coefficients.

Call \(V_0\) terminal-chart-free when it does not end in \(1100\) or
\(1010\). There are exactly

\[
L^\circ=\operatorname{Cat}_d-2\operatorname{Cat}_{d-2}
\tag{4.4}
\]

such words. If \(V_0\) is terminal-chart-free, every index \(UV_0\) in
(4.2) lies in \(\mathcal I\). Hence \(D_H\) has an oriented dipole whose
coefficient has magnitude at least \(\operatorname{Cat}_H\) on each of these
\(L^\circ\) disjoint pairs; any further private contribution has the same
orientation.

Every target in (4.3) contains both \(2m\) and \(n\), and omits \(1\).
Indeed, the last down-step of \(V_0\) is at position \(2d\), so

\[
4+2H+2d=2m.
\tag{4.5}
\]

Reflection fixes \(n\), sends \(2m\) to \(1\), and sends \(1\) to
\(2m\). Thus the reflected private targets contain \(1,n\) and omit
\(2m\); the original and reflected private families are disjoint. Since
all nonprivate arms omit \(n\), neither family receives any coefficient
from a reflected nonprivate arm of the other family.

It follows that

\[
\boxed{
\mathfrak A\ge\frac{4L^\circ\operatorname{Cat}_H^2}{c_H}.}
\tag{4.6}
\]

For \(d\ge3\), the exact Catalan ratio gives

\[
2\frac{\operatorname{Cat}_{d-2}}{\operatorname{Cat}_d}
=\frac{d(d+1)}{2(2d-1)(2d-3)}\le\frac12,
\tag{4.7}
\]

so \(L^\circ\ge\operatorname{Cat}_d/2\). Also

\[
\operatorname{Cat}_H\ge\frac{4^H}{4H^2},
\qquad
\operatorname{Cat}_d>\frac B{4^{H+2}}.
\tag{4.8}
\]

For completeness, the first inequality follows from
\(\binom{2H}{H}\ge4^H/(2H+1)\), and the second follows by multiplying

\[
\frac{\operatorname{Cat}_{s-1}}{\operatorname{Cat}_s}
=\frac{s+1}{2(2s-1)}>\frac14
\]

from \(s=d+1\) through \(s=m\).  Finally,

\[
\frac W{N_H}
=\prod_{j=0}^{H-1}\frac{m+2+j}{m-j}
\le \exp\!\left(\frac{H(H+1)}{m-H+1}\right)
\le e^{2(A+1)(A+2)}
\tag{4.8a}
\]

for all sufficiently large \(m\).  Thus \(c_H\le M_A\). Substitution in
(4.6) proves

\[
\boxed{\mathfrak A>\frac{B4^H}{128M_AH^4}.}
\tag{4.9}
\]

## 5. Component variance and contraction

The exact four-arm profile of one contextual packet is

\[
\|d_R\|_H^2
=\frac4{c_1}+8\sum_{q=2}^H\frac1{c_q}<8H.
\tag{5.1}
\]

Since coordinate permutations are isometries,

\[
\|h_R\|_H^2
=\|d_R-\sigma d_R\|_H^2
\le4\|d_R\|_H^2<32H.
\tag{5.2}
\]

There are fewer than \(B\) selected packets. Therefore

\[
\boxed{\mathfrak V_\Delta<32HB,
\qquad \mathfrak V_\times<16HB.}
\tag{5.3}
\]

Equations (3.7), (4.9), and (5.3) prove (0.10), while (3.10),
(4.9), and (5.3) prove (0.12a). Since
\(4^H/(M_AH^5)\to\infty\), eventually

\[
\frac{B4^H}{512M_AH^4}-8HB
\ge\frac{B4^H}{1024M_AH^4}.
\tag{5.4}
\]

Thus some corner proves (0.12). The empty sign change gives \(F^*\), while
changing every pair gives \(\sigma F^*\); these two factors have equal
energy. Hence a corner attaining the positive gain in (0.12) is a genuinely
mixed choice. Section 2 realizes it by two proper cuts.

Finally, (3.6), (4.9), and (5.3) give

\[
\frac{\mathbb E_\varepsilon
\|(I-P_\sigma)f(F_\varepsilon)\|_H^2}
{\|(I-P_\sigma)f(F^*)\|_H^2}
=\frac{\mathfrak V_\Delta}{\mathfrak A}
<\frac{4096M_AH^5}{4^H},
\tag{5.5}
\]

which proves (0.14).  Equation (3.11) divides this ratio by two for the
independently heated product block.

## 6. Growing-harmonic shield burnout

Use the degree split in (0.15), and let

\[
\mathcal L_J(F)
=\sum_{q\le H}\sum_{2\le j\le J}
\frac{\|P_{q,j}f_q(F)\|_2^2}{c_q}.
\tag{6.1}
\]

Write \(P_{>J}\) for the stacked orthogonal projection onto Johnson
degrees \(j>J\), and define

\[
\begin{aligned}
\mathfrak A^{>J}_\sigma(F^*)&=
 \left\|P_{>J}\bigl(f(F^*)-f(\sigma F^*)\bigr)\right\|_H^2,\\
\mathfrak V^{>J}_{\times,\sigma}(F^*)&=
 \sum_{R\in\mathcal I}
 \left(\|P_{>J}d_R\|_H^2+
       \|P_{>J}\sigma d_R\|_H^2\right),\\
\mathfrak V^{>J}_{\Delta,\sigma}(F^*)&=
 \sum_{R\in\mathcal I}\|P_{>J}h_R\|_H^2.
\end{aligned}
\tag{6.1a}
\]

The exact run-cap theorem gives \(\mathcal L_J(F)\le U\) for every exact
factor, where

\[
U=\frac{BH^3}{n}e^{\gamma H}.
\tag{6.2}
\]

The low-sector squared displacement between \(F^*\) and \(\sigma F^*\)
is at most

\[
2\mathcal L_J(F^*)+2\mathcal L_J(\sigma F^*)\le4U.
\tag{6.3}
\]

Consequently the coherent high-sector displacement obeys

\[
\mathfrak A_\sigma^{>J}(F^*)\ge \mathfrak A-4U
>\frac{B4^H}{128M_AH^4}-4U.
\tag{6.4}
\]

Projection can only decrease each component norm, so

\[
\mathfrak V_{\times,\sigma}^{>J}(F^*)<16HB,
\qquad
\mathfrak V_{\Delta,\sigma}^{>J}(F^*)<32HB.
\tag{6.5}
\]

Because \(\gamma<\log4\),

\[
\frac{U}{B4^H/(M_AH^4)}
=\frac{M_AH^7}{n}e^{-(\log4-\gamma)H}\longrightarrow0,
\tag{6.6}
\]

and \(M_AH^5/4^H\to0\). Equations (6.4)--(6.5) prove (0.16)--(0.17),
with the product comparison variance enjoying the sharper constant \(16\).
This is the nonlocal two-chart variance burnout missing from the elementary
single-colour fair-heat block: it is created by first making the reflected
chart phases state-dependent and then either heating the two charts
independently or correlating the two fresh cuts pair by pair.  No assertion
about either single-transposition variance is made here.

## 7. A companion contraction inside the reflection-invariant subspace

The opposite-phase code (0.9) contracts the anti-invariant chart signal.
The same two physical charts also carry a nontrivial invariant code.  Put

\[
F^{++}=F^0+\sum_{R\in\mathcal I}(z_R+\sigma z_R),
\qquad
\sigma z_R=\mathbf1_{\sigma\tau K_R}-
             \mathbf1_{\sigma K_R}.
\tag{7.1}
\]

For \(\varepsilon\in\{\pm1\}^{\mathcal I}\), define \(F^+_\varepsilon\)
by the same-phase choices

\[
\begin{array}{c|cc}
&U_R&\sigma U_R\\ \hline
\varepsilon_R=-1&K_R&\sigma K_R\\
\varepsilon_R=+1&\tau K_R&\sigma\tau K_R.
\end{array}
\tag{7.2}
\]

All these factors are literal and exact by Lemma 1.1, and every one is
\(\sigma\)-invariant.  Define

\[
k_R=d_R+\sigma d_R,\qquad
K=\sum_Rk_R,\qquad
\mathfrak A_+=\|K\|_H^2,\qquad
\mathfrak V_+=\sum_R\|k_R\|_H^2,
\tag{7.3}
\]

and put \(f_{\rm mid}=f(F^0)+K/2\).  Then

\[
f(F^+_\varepsilon)=f_{\rm mid}+\frac12\sum_R\varepsilon_Rk_R,
\quad
f(F^0)=f_{\rm mid}-\frac K2,
\quad
f(F^{++})=f_{\rm mid}+\frac K2.
\tag{7.4}
\]

Thus fair signs and the exact floor identity (3.6a) give

\[
\boxed{
\mathbb E_\varepsilon\mathcal Q_H(F^+_\varepsilon)
=\frac{\mathcal Q_H(F^0)+\mathcal Q_H(F^{++})}{2}
 +\frac{\mathfrak V_+-\mathfrak A_+}{4}.}
\tag{7.5}
\]

The original and reflected private-coordinate families used in Section 4
are still disjoint; replacing their relative minus sign by a plus sign does
not change their squared contribution.  Therefore the same proof gives

\[
\mathfrak A_+>\frac{B4^H}{128M_AH^4},
\qquad
\mathfrak V_+<32HB.
\tag{7.6}
\]

Let \(F^{\rm hi}\) be whichever of \(F^0,F^{++}\) has the larger
\(\mathcal Q_H\)-value, breaking a tie arbitrarily.  From (7.5)--(7.6),

\[
\mathbb E_\varepsilon\mathcal Q_H(F^+_\varepsilon)
\le \mathcal Q_H(F^{\rm hi})
-\frac{B4^H}{512M_AH^4}+8HB.
\tag{7.7}
\]

Consequently, for all sufficiently large \(m\), some literal
\(\sigma\)-invariant corner satisfies

\[
\boxed{
\mathcal Q_H(F^+_\varepsilon)
\le \mathcal Q_H(F^{\rm hi})
-\frac{B4^H}{1024M_AH^4}.}
\tag{7.8}
\]

This endpoint is reached from \(F^{\rm hi}\) by exactly two nonempty proper
fresh cuts: switch or revert the same nonempty index set first on the
\(U_R\)'s in colour \(\tau\), then on the unchanged \(\sigma U_R\)'s in
colour \(\tau'\).  Nonemptiness follows from the strict decrease.  To see
properness even when every \(R\in\mathcal I\) is selected, put
\(U=\bigsqcup_{R\in\mathcal I}U_R\).  It is \(\tau\)-invariant and

\[
|U|=2n|\mathcal I|
\le2n\operatorname{Cat}_{m-2}<n\operatorname{Cat}_m=W
\tag{7.9}
\]

for \(m\ge3\).  Hence its nonempty \(\tau\)-invariant complement contains
a fresh component that is not selected.  The reflected argument applies to
\(\bigsqcup_R\sigma U_R\) in the second overlay.

The invariant chart phase contracts quantitatively around its fixed
midpoint:

\[
\boxed{
\frac{\mathbb E_\varepsilon
 \|f(F^+_\varepsilon)-f_{\rm mid}\|_H^2}
 {\|f(F^{++})-f_{\rm mid}\|_H^2}
=\frac{\mathfrak V_+}{\mathfrak A_+}
<\frac{4096M_AH^5}{4^H}=o_A(1).}
\tag{7.10}
\]

It also burns the growing-degree part of this phase.  If
\(\mathfrak A_+^{>J}=\|P_{>J}K\|_H^2\) and
\(\mathfrak V_+^{>J}=\sum_R\|P_{>J}k_R\|_H^2\), then the run-cap bound
applied to the two exact endpoints gives

\[
\mathfrak A_+^{>J}>\frac{B4^H}{128M_AH^4}-4U,
\qquad
\mathfrak V_+^{>J}<32HB,
\qquad
\frac{\mathfrak V_+^{>J}}{\mathfrak A_+^{>J}}\longrightarrow0.
\tag{7.11}
\]

## 8. Exact boundary

The theorem proves explicit opposite-phase and same-phase two-proper-cut
blocks with:

1. literal exact intermediate and terminal factors;
2. one common bundle bit across every depth;
3. a strict full floor-energy decrease of order
   \(B4^H/H^4\);
4. an \(o_A(1)\) contraction factor for the reflection-anti-invariant
   profile of \(F^*\), and for an explicit reflection-invariant coherent
   chart phase; and
5. high-harmonic coherent-to-variance ratios tending to infinity in both
   chart parities.

The remaining positive task is to renew the construction on the
reflection-invariant midpoint residue, either by selecting a new
state-adaptive involution or by overlapping reflected blocks so their
invariant subspaces have a uniform spectral gap.  The same-phase theorem
contracts \(K\), not an arbitrary invariant midpoint.  That coverage and
iteration are not proved here, so the constant-one theorem is not claimed.
