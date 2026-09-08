# Post-purge stability of the centered collision defect

**Date:** 2026-08-22

**Status:** unconditional deterministic theorem.  It removes a separate
post-purge comparison from Gate A.  Its sharp hypothesis and charge use the
removed-edge fraction `rho`; the larger bad-target incidence fraction
`beta` is needed only as a convenient reference-law majorant.  The note does
not prove the two remaining stopped pre-purge estimates.

## 1. Purpose and notation

Let \(H\) be a finite simple hypergraph.  Its vertices are partitioned into
shores \(V_\sigma\), and every edge contains exactly \(k_\sigma\) vertices
of shore \(\sigma\).  Put

\[
 q=\sum_\sigma k_\sigma,\qquad Z=|E(H)|,\qquad
 n_\sigma=|V_\sigma|,\qquad
 z_\sigma={k_\sigma Z\over n_\sigma}.
                                                        \tag{1.1}
\]

For \(v\notin G\), define the external row

\[
 a_G^H(v)=|\{F\in E(H):v\in F,\ F\cap G\ne\varnothing\}|. \tag{1.2}
\]

For a real center \(z\), integers \(0\le a\le d\), and
\(f_z(d)=(d-z)^6\), put

\[
 \phi_z(d,a)
 =a\{f_z(d)-f_z(d-1)\}-\{f_z(d)-f_z(d-a)\}.          \tag{1.3}
\]

Thus the centered collision defect on shore \(\sigma\) is

\[
 {\mathfrak D}_{z,\sigma}(H)
 =\sum_{v\in V_\sigma}\sum_{\substack{G\in E(H)\\v\notin G}}
       \phi_z(d_H(v),a_G^H(v)).                       \tag{1.4}
\]

Also define its rooted order-two row mass

\[
 Q_{2,v}(H)
 =\sum_{\substack{G\in E(H)\\v\notin G}}(a_G^H(v))_2.
                                                        \tag{1.5}
\]

The point of this note is that \({\mathfrak D}\) is not monotone under
induced deletion, but its failure of monotonicity has an exact local charge.
For the high-degree purge used in the punctured nibble, that charge is at
most a constant times the purged incidence fraction after bite
normalization.

## 2. The rowwise two-center inequality

Write

\[
 P(t)=t^6-2(t-1)^6+(t-2)^6.
                                                        \tag{2.1}
\]

If \(U,V\) are independent uniform random variables on \([0,1]\), twice
integrating the second derivative gives

\[
 P(t)=30\,\mathbb E(t-U-V)^4.                         \tag{2.2}
\]

In particular \(P(t)\ge0\).  The shifted second-difference formula is

\[
 \phi_z(d,a)=
 \sum_{h=0}^{a-2}(a-1-h)P(d-z-h).                    \tag{2.3}
\]

### Lemma 2.1 (tunable deletion inequality)

Let \(d'=d-\ell\), let \(0\le a'\le d'\), \(a'\le a\le d\), and let
\(z,z'\) be real.  For every \(\eta>0\),

\[
\boxed{
 \phi_{z'}(d',a')
 \le (1+\eta)^3\phi_z(d,a)
 +15(1+\eta^{-1})^3(a')_2
       |\ell-(z-z')|^4.}                             \tag{2.4}
\]

In particular, at \(\eta=1\),

\[
 \phi_{z'}(d-\ell,a')
 \le 8\phi_z(d,a)+120(a')_2|\ell-(z-z')|^4.          \tag{2.5}
\]

#### Proof

Convexity of \(x\mapsto |x|^4\), with weights
\((1+\eta)^{-1}\) and \(\eta(1+\eta)^{-1}\), gives

\[
 |x-y|^4
 \le(1+\eta)^3|x|^4+(1+\eta^{-1})^3|y|^4.            \tag{2.6}
\]

Apply this inside (2.2), with

\[
 x=d-z-h-U-V,\qquad y=\ell-(z-z').
\]

It follows that

\[
 P(d'-z'-h)
 \le(1+\eta)^3P(d-z-h)
 +30(1+\eta^{-1})^3|\ell-(z-z')|^4.                 \tag{2.7}
\]

For \(0\le h\le a'-2\), the weight \(a'-1-h\) is at most
\(a-1-h\).  Sum (2.7), use \(P\ge0\), and use

\[
 \sum_{h=0}^{a'-2}(a'-1-h)={(a')_2\over2}.
\]

This proves (2.4), and (2.5) is its specialization. \(\square\)

The meaningful shift in (2.4) is not the lost degree \(\ell\) by itself.
It is

\[
 \ell-(z-z'),                                       \tag{2.8}
\]

the difference between the local degree loss and the loss of the global
center.

## 3. Exact deletion stability

Let \(H'\) be any subhypergraph induced on a subset of the vertices of
\(H\).  For a surviving target \(v\), put

\[
 \ell_v=d_H(v)-d_{H'}(v).
                                                        \tag{3.1}
\]

### Theorem 3.1 (exact post-deletion charge)

For arbitrary real centers \(z,z'\) and every \(\eta>0\),

\[
\boxed{
 {\mathfrak D}_{z',\sigma}(H')
 \le (1+\eta)^3{\mathfrak D}_{z,\sigma}(H)
 +15(1+\eta^{-1})^3
 \sum_{v\in V_\sigma(H')}
 Q_{2,v}(H')|\ell_v-(z-z')|^4.}                     \tag{3.2}
\]

#### Proof

For \(G\in E(H')\) and surviving \(v\notin G\), set

\[
 a'=a_G^{H'}(v),\qquad a=a_G^H(v).
\]

Induced deletion gives \(a'\le a\), while (3.1) gives
\(d_{H'}(v)=d_H(v)-\ell_v\).  Apply Lemma 2.1 to every surviving
pair \((v,G)\).  The first terms sum over a subfamily of the terms in
\({\mathfrak D}_{z,\sigma}(H)\), all of which are nonnegative by
(2.2)--(2.3).  The second terms sum to the displayed rooted
\(Q_2\) charge. \(\square\)

The final sum in (3.2) is the sharpest general-purpose sufficient deletion
statistic established by the row calculation here.  No maximum-degree
estimate has yet been used.

There is a useful cap-free local majorant.  For every surviving \(v\),

\[
\begin{aligned}
 Q_{2,v}(H')
 &\le d_{H'}(v)
       \sum_{\substack{G\in E(H')\\v\notin G}}a_G^{H'}(v)\\
 &\le d_{H'}(v)
       \sum_{\substack{F\in E(H')\\v\in F}}
       \sum_{u\in F-\{v\}}d_{H'}(u).                 \tag{3.3}
\end{aligned}
\]

Indeed, \(a_G^{H'}(v)\le d_{H'}(v)\), and swapping the \(F,G\)
sums bounds every external conflict \(G\) by one incidence at a member of
\(F-\{v\}\).  Thus (3.2) may alternatively be charged to the local
sixth-order deletion energy

\[
 \sum_v |\ell_v-(z-z')|^4 d_{H'}(v)
       \sum_{F\ni v}\sum_{u\in F-\{v\}}d_{H'}(u).    \tag{3.4}
\]

## 4. The actual high-degree purge

Fix \(K_0>1\).  In every shore define

\[
 B_\sigma=\{v\in V_\sigma:d_H(v)>K_0z_\sigma\},
 \qquad B=\bigcup_\sigma B_\sigma,                  \tag{4.1}
\]

and let \(H^\circ=H[V(H)-B]\).  Write

\[
 L_\sigma=\sum_{v\in B_\sigma}d_H(v),\qquad
 L=\sum_\sigma L_\sigma,\qquad
 \beta={L\over Z},\qquad
 M=Z-Z^\circ,\qquad \rho={M\over Z}.                 \tag{4.2}
\]

Let \(Z^\circ,n_\sigma^\circ,z_\sigma^\circ\) denote the parameters of
\(H^\circ\).  Suppose

\[
 0\le\rho\le\rho_0<1,\qquad
 { \max_\tau z_\tau\over\min_\tau z_\tau}\le R_0. \tag{4.3}
\]

### Lemma 4.1 (center and lost-degree ledger)

For every shore \(\sigma\), every surviving \(v\in V_\sigma\), and a
constant \(C_0=C_0(K_0,\rho_0)\),

\[
\begin{gathered}
 d_H(v)\le K_0z_\sigma,\qquad
 0\le\ell_v\le K_0z_\sigma,                         \tag{4.4}\\
 \sum_{v\in V_\sigma(H^\circ)}\ell_v
       \le k_\sigma\rho Z=\rho n_\sigma z_\sigma,   \tag{4.5}\\
 0\le z_\sigma-z_\sigma^\circ
       \le C_0\rho z_\sigma,                        \tag{4.6}\\
 z_\sigma^\circ\ge(1-\rho)z_\sigma,\qquad
 n_\sigma^\circ\ge
 \left(1-{\rho\over K_0}\right)n_\sigma.            \tag{4.7}
\end{gathered}
\]

Consequently

\[
 \sum_{v\in V_\sigma(H^\circ)}
 |\ell_v-(z_\sigma-z_\sigma^\circ)|^4
 \le C_1\rho n_\sigma z_\sigma^4,                   \tag{4.8}
\]

where \(C_1=C_1(K_0,\rho_0)\).

#### Proof

The first statement is the definition of \(B_\sigma\).  Every removed
edge contributes at most \(k_\sigma\) lost incidences to surviving
shore-\(\sigma\) targets, proving (4.5).  Moreover, counting bad-target
incidences by removed edges gives the useful exact sandwich

\[
 M\le L=\sum_{F\in E(H)-E(H^\circ)}|F\cap B|\le qM,
 \qquad\hbox{hence}\qquad
 \rho\le\beta\le q\rho.                              \tag{4.5a}
\]

Put

\[
 \tau_\sigma={|B_\sigma|\over n_\sigma}.
\]

There is a sharper shorewise count than the global sandwich (4.5a):

\[
 L_\sigma
 =\sum_{F\in E(H)-E(H^\circ)}|F\cap B_\sigma|
 \le k_\sigma M.                                    \tag{4.9}
\]

Since every member of \(B_\sigma\) has degree greater than
\(K_0z_\sigma=K_0k_\sigma Z/n_\sigma\), (4.9) gives

\[
 0\le\tau_\sigma\le {\rho\over K_0}\le\rho.       \tag{4.9a}
\]

The exact center identity is

\[
 {z_\sigma^\circ\over z_\sigma}
 ={1-\rho\over1-\tau_\sigma}.                       \tag{4.10}
\]

Equations (4.6)--(4.7) follow from (4.9a)--(4.10); explicitly,

\[
 {z_\sigma-z_\sigma^\circ\over z_\sigma}
 ={\rho-\tau_\sigma\over1-\tau_\sigma}
 \le {\rho\over1-\rho_0/K_0}.                     \tag{4.11}
\]

This also proves that a high-degree purge cannot increase a shore average.
The global incidence fraction `beta` is not needed for the center ledger.

Finally, (4.4), (4.5), (4.11), and
\(|x-y|^4\le8(x^4+y^4)\) give

\[
\begin{aligned}
 \sum_v|\ell_v-(z_\sigma-z_\sigma^\circ)|^4
 &\le8(K_0z_\sigma)^3\sum_v\ell_v
   +8n_\sigma|z_\sigma-z_\sigma^\circ|^4\\
 &\le C_1\rho n_\sigma z_\sigma^4,
\end{aligned}
\]

using \(\rho^4\le\rho_0^3\rho\).  \(\square\)

### Lemma 4.2 (post-purge rooted \(Q_2\) cap)

For every surviving \(v\in V_\sigma\),

\[
\boxed{
 Q_{2,v}(H^\circ)
 \le(q-1)K_0^3R_0z_\sigma^3.}                       \tag{4.12}
\]

#### Proof

All surviving targets \(u\in V_\tau\) have
\(d_{H^\circ}(u)\le d_H(u)\le K_0z_\tau\), so the maximum
post-purge degree is at most \(K_0R_0z_\sigma\).  From (3.3),

\[
\begin{aligned}
 \sum_{G\not\ni v}a_G^{H^\circ}(v)
 &\le\sum_{F\ni v}\sum_{u\in F-\{v\}}d_{H^\circ}(u)\\
 &\le d_{H^\circ}(v)(q-1)K_0R_0z_\sigma.
\end{aligned}
\]

Since \(a_G^{H^\circ}(v)\le d_{H^\circ}(v)\le K_0z_\sigma\),
multiplication proves (4.12). \(\square\)

### Theorem 4.3 (purge-deletion stability)

Under (4.1)--(4.3), for every shore \(\sigma\) and every \(\eta>0\),

\[
\boxed{
 {\mathfrak D}_{z_\sigma^\circ,\sigma}(H^\circ)
 \le(1+\eta)^3{\mathfrak D}_{z_\sigma,\sigma}(H)
 +C_{\eta,K_0,\rho_0,R_0}\,
       q\,\rho n_\sigma z_\sigma^7.}                 \tag{4.13}
\]

Equivalently, since \(n_\sigma z_\sigma=k_\sigma Z\), the last term is

\[
 C_{\eta,K_0,\rho_0,R_0}\,
       qk_\sigma\rho Zz_\sigma^6.                   \tag{4.14}
\]

#### Proof

Insert (4.8) and (4.12) into Theorem 3.1. \(\square\)

For the punctured hypergraph, \(k_M=k_L=2r\) and \(q=4r\).
Thus (4.14) is \(O_{K_0,R_0}(r^2\rho Zz_\sigma^6)\).  Since
\(\rho\le\beta\), this is at least as strong as the scale suggested by
the bad-incidence ledger.

## 5. Bite-normalized and stopped forms

In the punctured application suppose a post-purge marking rate \(\pi\)
satisfies

\[
 \pi\le {C_\pi\over r z_M^\circ}.                   \tag{5.1}
\]

The paired shore schedule gives a fixed \(R_0\) in (4.3).  Equations
(4.7), (4.13), and \(q=4r\) then imply

\[
\boxed{
 {\pi{\mathfrak D}_{z_\sigma^\circ,\sigma}(H^\circ)
  \over n_\sigma^\circ(z_\sigma^\circ)^6}
 \le
 C\,{\pi{\mathfrak D}_{z_\sigma,\sigma}(H)
  \over n_\sigma z_\sigma^6}
 +C\rho.}                                           \tag{5.2}
\]

where \(C\) depends only on the fixed constants
\(\eta,K_0,\rho_0,R_0,C_\pi\).

Indeed, (4.7) bounds both
`n_sigma/n_sigma^circ` and `(z_sigma/z_sigma^circ)^6` by fixed constants.
For the additive term in (4.13),

\[
 {\pi q\rho n_\sigma z_\sigma^7
       \over n_\sigma^\circ(z_\sigma^\circ)^6}
 \le C\pi q\rho z_\sigma
 \le C\rho\,{q\over r}\,{z_\sigma\over z_M^\circ}
 \le C\rho,                                         \tag{5.2a}
\]

because `q/r=4`, (5.1) holds, and
`z_sigma/z_M^circ<=R_0/(1-rho_0)`.

Consequently, fix `rho_0<1`.  For a stopped sequence of provisional
residuals \(H_j^*\), their high-degree purges \(H_j^\circ\), and active
events \(\mathcal G_j\) on which the degree-ratio part of (4.3) and (5.1)
hold, put

\[
 \widehat{\mathcal G}_j
 =\mathcal G_j\cap\{\rho_j\le\rho_0\}.              \tag{5.2b}
\]

The two conditions

\[
 \sum_{j,\sigma}\mathbb E\!\left[
 {\bf1}_{\mathcal G_j}
 {\pi_j{\mathfrak D}_{z_{j,\sigma}^*,\sigma}(H_j^*)
  \over n_{j,\sigma}^*(z_{j,\sigma}^*)^6}\right]=o(1),          \tag{5.3}
\]

\[
 \sum_j\mathbb E[{\bf1}_{\mathcal G_j}\rho_j]=o(1)              \tag{5.4}
\]

imply

\[
 \sum_{j,\sigma}\mathbb E\!\left[
 {\bf1}_{\widehat{\mathcal G}_j}
 {\pi_j{\mathfrak D}_{z_{j,\sigma}^\circ,\sigma}(H_j^\circ)
  \over n_{j,\sigma}^\circ(z_{j,\sigma}^\circ)^6}\right]=o(1).
                                                                    \tag{5.5}
\]

Moreover,

\[
 \Pr(\exists j:\mathcal G_j\text{ and }\rho_j>\rho_0)
 \le {1\over\rho_0}
       \sum_j\mathbb E[\mathbf1_{\mathcal G_j}\rho_j]=o(1). \tag{5.5a}
\]

Thus (5.2) is used only before the first current purge which violates its
hypothesis; this is a stopped-event union bound, not conditioning on future
cap persistence.  If a desired post-purge cap is `K>K_0`, choosing
\(\rho_0\le1-K_0/K\) also gives
\(\Delta_\sigma(H_j^\circ)/z_{j,\sigma}^\circ\le K\) from (4.7).

The exact, weaker replacement for (5.4) is summability of the charge

\[
 \sum_{j,\sigma}\mathbb E\!\left[
 {\bf1}_{\widehat{\mathcal G}_j}
 {\pi_j\over n_{j,\sigma}^\circ(z_{j,\sigma}^\circ)^6}
 \sum_vQ_{2,v}(H_j^\circ)
 |\ell_{j,v}-(z_{j,\sigma}^*-z_{j,\sigma}^\circ)|^4
 \right]=o(1).                                      \tag{5.6}
\]

Equation (5.4) is merely a clean sufficient condition for (5.6), together
with the exceptional-purge estimate (5.5a).  The stronger condition

\[
 \sum_j\mathbb E[{\bf1}_{\mathcal G_j}\beta_j]=o(1)             \tag{5.6a}
\]

also suffices because \(\rho_j\le\beta_j\).

For scale bookkeeping, suppose a uniform-slice reference law gives per
checkpoint bounds

\[
 \mathbb E\beta_j=O(r^{-2}x_j^{-9}),\qquad
 \mathbb E\!\left[
 {\pi_j{\mathfrak D}_j\over n_jz_j^6}\right]
 =O(r^{-3}x_j^{-32}).                               \tag{5.7}
\]

The first estimate also bounds the reference removed-edge fraction because
`rho_j<=beta_j` pointwise.  Thus a stopped comparison may be posed directly
for `rho`, or more strongly for `beta`; no factor `q` is lost in passing from
the latter to the former.

If

\[
 x_{j+1}=x_j(1-\Theta(1/r)),\qquad x_J\asymp r^{-\alpha},
\]

then geometric summation gives

\[
 \sum_jO(r^{-2}x_j^{-9})=O(r^{-1}x_J^{-9}),\qquad
 \sum_jO(r^{-3}x_j^{-32})=O(r^{-2}x_J^{-32}).        \tag{5.8}
\]

Therefore a common stopped comparison loss \(r^{\kappa+o(1)}\) would
suffice for (5.3) and the stronger condition (5.6a) whenever

\[
 \boxed{\kappa<\min\{1-9\alpha,\ 2-32\alpha\}.}       \tag{5.9}
\]

No such stopped comparison is proved here.

## 6. Why monotonicity and an incidence-only statement need hypotheses

Even aggregate \({\mathfrak D}\) is not monotone under arbitrary induced
vertex deletion.  Regard a graph as a one-shore \(2\)-uniform
hypergraph.  Let \(H\) be a triangle plus one isolated vertex.  Its center
is \(z=3/2\).  In a graph, a row has \(a_G(v)=2\) precisely when \(v\)
and the edge \(G\) form a triangle, so

\[
 {\mathfrak D}_{3/2}(H)
 =3P(1/2)={273\over8}.                              \tag{6.1}
\]

Delete the isolated vertex.  The residual is the triangle, its center is
\(z'=2\), and

\[
 {\mathfrak D}_{2}(H')=3P(0)=186>{273\over8}.        \tag{6.2}
\]

No edge and hence no edge incidence was removed.  Thus arbitrary vertex
deletion cannot be charged solely to removed edge incidence.  The
high-degree condition (4.1) is what forces the deleted vertex fraction,
the center shift, and the removed incidence to be tied together.

Even with the center held fixed, rowwise monotonicity is false.  Take
3-uniform edges

\[
 G=\{x,y,g\},\quad F_1=\{v,x,a\},\quad
 F_2=\{v,y,b\},\quad F_3=\{v,c,d\}.                 \tag{6.3}
\]

For the row \((v,G)\), initially \(d(v)=3\) and \(a_G(v)=2\).
Deleting \(c\) removes only \(F_3\), so the retained row has \(d'(v)=2\)
and \(a'_G(v)=2\).  At the fixed center \(z=3\),

\[
 \phi_3(3,2)=P(0)=62,\qquad
 \phi_3(2,2)=P(-1)=602.                             \tag{6.4}
\]

The mismatch charge in Theorem 3.1 is therefore structurally necessary.

## 7. Exact remaining Gate A statement

Theorem 4.3 proves the complete deterministic transfer from a provisional
pre-purge residual to its post-purge capped residual.  It shows that no
third post-purge statistic has to be compared with a reference law.

What remains probabilistic is exactly the pair of pre-purge stopped
estimates (5.3)--(5.4):

1. the centered collision defect under the actual provisional law; and
2. the removed-edge fraction `rho` generated by the high-degree purge.

Product and uniform-slice calculations give the reference scales (5.7),
with the bad-incidence fraction `beta` as a pointwise majorant for `rho`.
The missing theorem is their stopped transfer to the history-induced
punctured residual law.  Comparing `beta` remains a sufficient, stronger
route, but is not required by the deterministic deletion theorem.  Neither
deletion stability nor cap trimming by itself proves either transfer.
