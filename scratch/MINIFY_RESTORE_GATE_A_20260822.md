## Appendix C.12: Signed sixth-moment collision forcing

This section is only a product/uniform-slice theorem; it does not assert a
stopped comparison. Retain the two shores with
\(p_M=y\ge p_L=x\ge r^{-\alpha}\), and put
\[
q_0=x^{2r}y^{2r},\qquad
\mu_\sigma={d_\sigma q_0\over p_\sigma},\qquad
d_M=D_M,\quad d_L=D_L.                                    \tag{C.12.1}
\]
Fix an original row \(G\), a shore-\(\sigma\) target \(v\notin G\), and
condition on retaining \(G\cup\{v\}\). Define
\[
A_{G,v}=|\{F\ni v:F\cap G\ne\varnothing,\ F\text{ survives}\}|, \tag{C.12.2}
\]
\[
K_c(G,v)={1\over d_\sigma}
\sum_{\substack{F\ni v\\F\cap G\ne\varnothing}}
\prod_{u\in F\cap G}p_{\operatorname{sh}(u)}^{-c}.          \tag{C.12.3}
\]
Then \(\mathbb EA_{G,v}=\mu_\sigma K_1(G,v)\). For every fixed \(c\)
with \(c\alpha<1/3\),
\[
\boxed{\sum_{v\notin G}K_c(G,v)=O_c(r^2x^{-c}).}             \tag{C.12.4}
\]
Indeed, with \(a_c=x^{-c}-1\), expand
\[
W_c(G)=\sum_{F:F\cap G\ne\varnothing}
\prod_{u\in F\cap G}p_{\operatorname{sh}(u)}^{-c}.
\]
Singleton subsets cost \(O(D_Mrx^{-c})\); C.7 and C.1 bound all larger
subsets by \(O_c(D_M(a_c^2+a_c^4))\). Since
\(a_c^4=O(rx^{-c})\), \(W_c(G)=O_c(D_Mrx^{-c})\). Interchanging \(v,F\),
using \(2r\) shore targets per row and \(d_\sigma\ge D_M\), proves
(C.12.4).

C.8 also gives the time-zero external-star cap
\[
\max_{G\not\ni v}|\{F\ni v:F\cap G\ne\varnothing\}|
\le {32D_M\over r}.                                      \tag{C.12.4a}
\]
Only disjoint-middle and lower-in-middle containment pairs have codegree
above \(6D_M/r^2\); each has codegree at most \(2D_M/r\), and \(v\) has at
most four such partners in \(G\). Cauchy and (C.12.4) therefore give
\[
K_1(G,v)^2\le {32\over r}K_2(G,v),\qquad
\sum_vK_1(G,v)^2=O(rx^{-2}).                              \tag{C.12.6}
\]
For distinct \(F,H\ni v\), their conditional joint-survival monomial is
\[
w_\sigma^2s_Fs_H
\prod_{u\in(F\cap H)-(G\cup\{v\})}p_{\operatorname{sh}(u)}^{-1},
\quad w_\sigma={\mu_\sigma\over d_\sigma},\quad
s_F=\prod_{u\in F\cap G}p_{\operatorname{sh}(u)}^{-1}.
\]
The constant part sums with (C.12.6). For the remainder use
\(s_Fs_H\le(s_F^2+s_H^2)/2\) and C.3bis.6 with \(c=1\), obtaining
\[
\boxed{\sum_{v\notin G}\mathbb E[(A_{G,v})_2\mid G,v]
=O(\mu_\sigma^2rx^{-5}).}                                \tag{C.12.5}
\]

For \(f_z(d)=(d-z)^6\), define
\[
\mathfrak d_z(d,a)=a\nabla f_z(d)-[f_z(d)-f_z(d-a)].        \tag{C.12.7}
\]
Falling-factorial expansion and telescoping give
\[
\mathfrak d_z(d,a)=\sum_{\ell=1}^6c_\ell(z)
\{\ell a(d-1)_{\ell-1}-[(d)_\ell-(d-a)_\ell]\}
=\sum_{h=0}^{a-2}(a-1-h)\nabla^2f_z(d-h).                  \tag{C.12.8}
\]
Since \(f_z\) is convex and
\(\nabla^2f_z(d)=30t^4-120t^3+210t^2-180t+62\), \(t=d-z\),
\[
\boxed{0\le\mathfrak d_z(d,a)
\le C(a)_2(1+|d-z|^4+a^4).}                               \tag{C.12.9}
\]
For a residual \(H\), set
\[
a_G(v)=|\{F\in E(H):v\in F,\ F\cap G\ne\varnothing\}|,
\quad
\mathfrak D_{z,\sigma}(H)=
\sum_v\sum_{G\not\ni v}\mathfrak d_z(d_H(v),a_G(v)).       \tag{C.12.10}
\]
It is nonnegative. The first expression in (C.12.8), after interchanging
\(G\) and ordered tuples through \(v\), is exactly the signed recombination
of the five factorial collision defects in the first-order evolution of
the centered sixth degree mass.

If \(\alpha<1/18\), uniformly in \(G\),
\[
\boxed{\sum_{v\notin G}\mathbb E[
(A_{G,v})_2\{1+|X_v-\mu_\sigma|^4+A_{G,v}^4\}\mid G,v]
=O(\mu_\sigma^6r^{-1}x^{-33}).}                           \tag{C.12.11}
\]
Here \(X_v\) is the full residual degree under the conditioning above.
Here is the full carrier estimate. Put
\[
\theta={32\over r},\qquad \lambda=\theta+Q_3=O(r^{-1}x^{-9}). \tag{C.12.12}
\]
For an ordered pair meeting \(G\) and four further distinct centered
carriers, their absolute conditional contribution is at most
\[
Cw_\sigma^6\prod_{i\in R}s_i\,
x^{-\sum_{i<j}|(F_i\cap F_j)-(G\cup\{v\})|}.               \tag{C.12.13}
\]
Join carriers with positive displayed overlap. A centered singleton
component vanishes, hence at most two components avoid \(R\). A
maximum-weight tree in every other component carries at least one third of
its overlap weight and sums with \(Q_3\). Since
\(\prod_{i\in R}s_i\le |R|^{-1}\sum_{j\in R}s_j^{|R|}\), at least three
\(\theta\)- or \(Q_3\)-costs remain. Thus (C.12.4) gives
\[
C\mu_\sigma^6\lambda^3\sum_{h=2}^6\sum_vK_h(G,v)
=O(\mu_\sigma^6r^{-1}x^{-33}).                            \tag{C.12.14}
\]
Repeated Bernoulli labels reduce affinely to fewer centered labels; a term
with at most five distinct carriers is
\(O_m(\mu_\sigma^m r^2x^{-m})\), exponentially smaller because
\(\mu_\sigma\) is exponential. Finally,
\[
(A)_2A^4=16(A)_2+65(A)_3+55(A)_4+14(A)_5+(A)_6.           \tag{C.12.15}
\]
The all-\(j\)-carriers-meet-\(G\) sum is at most
\(C_j\mu_\sigma^j\lambda^{j-1}\sum_vK_j\). At \(j=6\) this is
\(O(\mu_\sigma^6r^{-3}x^{-51})\), absorbed because
\(r^{-2}x^{-18}=o(1)\); lower orders are smaller. This proves (C.12.11).

For the provisional product residual \(H^*\), put \(Z^*=|E(H^*)|\). Then
\[
\boxed{\mathbb E\mathfrak D_{\mu_\sigma,\sigma}(H^*)
=O((\mathbb EZ^*)p_\sigma\mu_\sigma^6r^{-1}x^{-33}).}      \tag{C.12.16}
\]
This follows by summing (C.12.11) over \(G\), multiplying by \(q_0p_\sigma\),
and using (C.12.9). C.3ter transfers it to every uniform exact two-shore
slice, with that slice's exact mean: each term queries at most seven rows;
the positive carrier envelope is \(O(\mu_\sigma^6rx^{-15})\), so the
exponentially small slice/product error remains negligible.

At paired densities, \(\pi_0=\gamma/(r\mu_M)\); if \(N_\sigma\) is the
full shore population, then
\((N_\sigma p_\sigma)\mu_\sigma=2r\mathbb EZ^*\), so
\[
{\pi_0\mathbb E\mathfrak D_{\mu_\sigma,\sigma}(H^*)
\over(N_\sigma p_\sigma)\mu_\sigma^6}=O(r^{-3}x^{-32}).    \tag{C.12.17}
\]
On \(x_{j+1}=x_j(1-\Theta(1/r))\), \(x_J\ge r^{-\alpha}\),
\[
\sum_{j<J}O(r^{-3}x_j^{-32})=O(r^{-2}x_J^{-32})=o(1).     \tag{C.12.18}
\]

For every \(z,z'\),
\[
\boxed{\mathfrak D_{z',\sigma}(H)\le
C\mathfrak D_{z,\sigma}(H)+C|z'-z|^4\mathcal Q_{2,\sigma}(H),} \tag{C.12.19}
\]
where \(\mathcal Q_{2,\sigma}=\sum_v\sum_{G\not\ni v}(a_G(v))_2\).
Indeed \(P(t)=t^6-2(t-1)^6+(t-2)^6=30\mathbb E(t-U-V)^4\), so
\(P(t-u)\le C(P(t)+|u|^4)\); apply this in (C.12.8).
With \(\eta=r^{-1/8}\) and \(\bar d_\sigma=2rZ/n_\sigma\), C.3bis.11
and C.3t.10 give, over
\(O(r\log r)\) checkpoints,
\[
\Pr(\exists j,\sigma:|\bar d_{\sigma,j}/\mu_{\sigma,j}-1|>\eta)
=O(r^{-2+6/8+3\alpha}\log r)+e^{-\Omega(r)}=o(1).          \tag{C.12.20}
\]
Product shore sizes add only an exponential tail; slice sizes are fixed.
Summing (C.12.5) over \(G\) gives
\[
\mathbb E\mathcal Q_{2,\sigma}(H^*)
=O((\mathbb EZ^*)p_\sigma\mu_\sigma^2rx^{-5}).             \tag{C.12.20a}
\]
Thus the cumulative center-shift contribution is
\[
O(\eta^4x_J^{-4})=O(r^{-1/2+4\alpha})=o(1).                \tag{C.12.21}
\]
Therefore the pre-purge product and exact-slice forcing is summable for
\(\alpha<1/18\). No adaptive stopped conclusion is asserted.

## Appendix C.12a: Deterministic post-purge stability

Let \(H\) be finite, simple, shore-uniform, every edge using \(k_\sigma\)
vertices of shore \(\sigma\), and put
\[
q=\sum_\sigma k_\sigma,\quad Z=|E(H)|,\quad
n_\sigma=|V_\sigma|,\quad z_\sigma={k_\sigma Z\over n_\sigma}. \tag{C.12a.1}
\]
Use \(a_G^H,\mathfrak d_z,\mathfrak D_{z,\sigma}\) above and set
\[
Q_{2,v}(H)=\sum_{G\not\ni v}(a_G^H(v))_2.                  \tag{C.12a.3}
\]
If \(d'=d-\ell\), \(0\le a'\le d'\), \(a'\le a\le d\), then for every
\(\varepsilon>0\),
\[
\boxed{\mathfrak d_{z'}(d',a')\le(1+\varepsilon)^3\mathfrak d_z(d,a)
+15(1+\varepsilon^{-1})^3(a')_2|\ell-(z-z')|^4.}          \tag{C.12a.4}
\]
This follows from (C.12.8),
\[
\mathfrak d_z(d,a)=\sum_{h=0}^{a-2}(a-1-h)P(d-z-h),\quad
P(t)=30\mathbb E(t-U-V)^4,                               \tag{C.12a.5}
\]
and \(|X-Y|^4\le(1+\varepsilon)^3|X|^4+
(1+\varepsilon^{-1})^3|Y|^4\); the new weights sum to \((a')_2/2\).

If \(H'\) is vertex-induced and
\(\ell_v=d_H(v)-d_{H'}(v)\), then \(a_G^{H'}(v)\le a_G^H(v)\), so
\[
\boxed{\mathfrak D_{z',\sigma}(H')\le
(1+\varepsilon)^3\mathfrak D_{z,\sigma}(H)
+15(1+\varepsilon^{-1})^3\sum_{v\in V_\sigma(H')}
Q_{2,v}(H')|\ell_v-(z-z')|^4.}                           \tag{C.12a.8}
\]
Also
\[
Q_{2,v}(H')\le d_{H'}(v)\sum_{\substack{F\in E(H')\\v\in F}}
\sum_{u\in F-\{v\}}d_{H'}(u).                             \tag{C.12a.9}
\]

Fix \(K_0>1\), purge
\[
B_\sigma=\{v:d_H(v)>K_0z_\sigma\},\quad
H^\circ=H[V(H)-\bigcup_\sigma B_\sigma],\quad
Z^\circ=|E(H^\circ)|,                                    \tag{C.12a.10}
\]
and set
\[
L_\sigma=\sum_{v\in B_\sigma}d_H(v),\quad
\beta={\sum_\sigma L_\sigma\over Z},\quad
\rho={Z-Z^\circ\over Z}.                                  \tag{C.12a.11}
\]
Assume \(0\le\rho\le\rho_0<1\) and
\(\max_\tau z_\tau/\min_\tau z_\tau\le R_0\). Then
\[
\rho\le\beta\le q\rho,\qquad L_\sigma\le k_\sigma(Z-Z^\circ), \tag{C.12a.14}
\]
because each removed edge contains between one and \(q\) bad vertices and
at most \(k_\sigma\) on shore \(\sigma\).
\[
\tau_\sigma:={|B_\sigma|\over n_\sigma}\le{\rho\over K_0},
\qquad {z_\sigma^\circ\over z_\sigma}={1-\rho\over1-\tau_\sigma}, \tag{C.12a.16}
\]
\[
z_\sigma^\circ\ge(1-\rho)z_\sigma,\quad
n_\sigma^\circ\ge(1-\rho/K_0)n_\sigma,\quad
0\le z_\sigma-z_\sigma^\circ\le
{\rho z_\sigma\over1-\rho_0/K_0}.                         \tag{C.12a.17}
\]
For surviving \(v\), \(d_H(v),\ell_v\le K_0z_\sigma\) and
\(\sum_v\ell_v\le\rho n_\sigma z_\sigma\). Hence
\[
\sum_v|\ell_v-(z_\sigma-z_\sigma^\circ)|^4
\le C_{K_0,\rho_0}\rho n_\sigma z_\sigma^4,               \tag{C.12a.18}
\]
\[
Q_{2,v}(H^\circ)\le(q-1)K_0^3R_0z_\sigma^3.               \tag{C.12a.19}
\]
The first bound uses
\(\sum\ell_v^4\le(K_0z_\sigma)^3\sum\ell_v\) and the center bound;
the second is (C.12a.9) with the post-purge cap and the shore ratio.
Substitution in (C.12a.8) proves
\[
\boxed{\mathfrak D_{z_\sigma^\circ,\sigma}(H^\circ)\le
(1+\varepsilon)^3\mathfrak D_{z_\sigma,\sigma}(H)
+C_{\varepsilon,K_0,\rho_0,R_0}q\rho n_\sigma z_\sigma^7.} \tag{C.12a.20}
\]
Equivalently, its additive term is \(Cqk_\sigma\rho Zz_\sigma^6\).

For the punctured hypergraph \(k_M=k_L=2r\), \(q=4r\). If
\(\pi\le C_\pi/(rz_M^\circ)\), the paired shore ratio is bounded, and
(C.12a.20) normalizes to
\[
\boxed{{\pi\mathfrak D_{z_\sigma^\circ,\sigma}(H^\circ)
\over n_\sigma^\circ(z_\sigma^\circ)^6}\le
C{\pi\mathfrak D_{z_\sigma,\sigma}(H)\over n_\sigma z_\sigma^6}+C\rho.}
                                                                    \tag{C.12a.22}
\]
For provisional \(H_j^*\), purged \(H_j^\circ\), and active events
\(\mathcal G_j\) on which the displayed rate and ratio hypotheses hold,
the exact two remaining stopped inputs are
\[
\boxed{\sum_{j,\sigma}\mathbb E\!\left[
\mathbf1_{\mathcal G_j}{\pi_j\mathfrak D_{z_{j,\sigma}^*,\sigma}(H_j^*)
\over n_{j,\sigma}^*(z_{j,\sigma}^*)^6}\right]=o(1),}      \tag{C.12a.24}
\]
\[
\boxed{\sum_j\mathbb E[\mathbf1_{\mathcal G_j}\rho_j]=o(1).} \tag{C.12a.25}
\]
Then (C.12a.22) gives the post-purge \(o(1)\) sum on
\(\mathcal G_j\cap\{\rho_j\le\rho_0\}\), and
\[
\Pr(\exists j:\mathcal G_j,\rho_j>\rho_0)
\le\rho_0^{-1}\sum_j\mathbb E[\mathbf1_{\mathcal G_j}\rho_j]=o(1). \tag{C.12a.26}
\]
If \(K>K_0\) and \(\rho_0\le1-K_0/K\), the post-purge cap is at most \(K\).
Since \(\rho_j\le\beta_j\), stopped summability of \(\beta_j\) is sufficient
but stronger.

At a product or exact-slice checkpoint, the fixed sixth moments, with
(C.12.20) replacing \(\mu_\sigma\) by the realized average, give
\[
\mathbb E\beta_j=O(r^{-2}x_j^{-9}),\qquad
\mathbb E{\pi_j\mathfrak D_j\over n_jz_j^6}
=O(r^{-3}x_j^{-32}).                                    \tag{C.12a.27}
\]
For the first estimate use
\(u\mathbf1_{\{u>K_0\}}\le C_{K_0}(u-1)^6\), sum the fixed-target sixth
moment over both shores, and use total incidence \(2rZ\). Along a geometric
schedule the sums are \(O(r^{-1}x_J^{-9})\) and
\(O(r^{-2}x_J^{-32})\). Thus a common stopped comparison loss
\(r^{\kappa+o(1)}\) suffices if
\[
\boxed{\kappa<\min\{1-9\alpha,\ 2-32\alpha\}.}             \tag{C.12a.28}
\]
No such stopped comparison is proved. There is no third post-purge
statistic: this branch is exactly (C.12a.24) plus (C.12a.25).
