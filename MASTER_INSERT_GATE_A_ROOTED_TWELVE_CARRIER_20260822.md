# MASTER integration packet: rooted twelve-carrier Gate-A likelihood

**Date:** 2026-08-22  
**Purpose:** insertion-ready text only; this file does not modify
`MASTER_HANDOFF.md`.

Source note SHA-256:
`7180e0bc5d55a81d4360f295f966acd5b50168d879feaf5673c5cb31ee1f6490`.
Verifier SHA-256:
`39d03e9275732429821684d574f6efcf1fa4d4239b0d64093c25214941e04556`.

## 1. Exact insertion map

### 1.1 Executive-status bullet

Insert immediately after the top bullet ending

> `High moments do not prove their own stopped comparison.`

and before the bullet beginning

> `**[I]** Independently, the canonical Dyck phase paths ...`

Insert:

> - **[I]/[O]** Appendix G.2 resolves the normalization of the remaining
>   twelfth-moment comparison.  A polynomial (r^{\kappa+o(1)}) domination
>   of the rooted twelve-carrier Palm law transfers the uniform exact-slice
>   (U_{12}) bound; (kappa<2-20\alpha) is the full shore-safe threshold.
>   Palm normalization cancels carrier-averaged duplicate drift, but the
>   centered drift is not a martingale.  A finite two-type recursion and the
>   regular graph (K_{13}\dot\cup M K_{12,12}) show that static
>   pair-square/centered-defect variance cannot supply the comparison.  In
>   the literal deletion-only process an alive labelled carrier has a unique
>   parent, so no carrier refresh is available.  The exact open input is a
>   punctured-specific stopped one-sided bound on the cumulative full
>   centered Palm transition potential, including its conditional
>   residual-environment factor.

### 1.2 Main proof ledger

In the table headed `The current proof ledger is:`, insert immediately
after

> `| cap-only twelfth-moment shadow ledger | ... |`

the row

> `| rooted twelve-carrier Palm transfer | [I]/[O] | Palm normalization and obstruction are proved; prove the punctured-specific cumulative centered full-transition potential bound (ordinary refresh is unavailable) |`

### 1.3 Gate-A narrative

In the `Gate A` discussion, insert immediately after the paragraph ending

> `This alternative does not require the fine companion/pair-square gates, and it does not infer the stopped comparison from the cap.`

Insert:

> Appendix G.2 gives the exact probabilistic form of that missing
> comparison.  It is enough to dominate the rooted twelve-carrier Palm law
> by (r^{\kappa+o(1)}) relative to the uniform exact-slice Palm law.
> Carrier-averaged first-blocker drift cancels in the normalized Doob
> recursion, but a persistent rare carrier type can still acquire
> polynomial likelihood while the sum of static centered variances tends to
> zero.  Since deletion gives every alive labelled carrier a unique parent,
> the natural genealogy has no refresh.  Thus the live route is a
> punctured-specific cumulative tilted-occupation estimate for the full
> transition density, not a generic Freedman argument from current
> pair-square or centered-defect energies.

### 1.4 Source/certificate table

In the source table, insert immediately after

> `| high-even-moment cap-only shadow ledger | Appendix G.1 | ... |`

the row

> `| rooted twelve-carrier Palm likelihood and no-Freedman reduction | Appendix G.2 | source SHA 7180e0bc5d55a81d4360f295f966acd5b50168d879feaf5673c5cb31ee1f6490; checker SHA 39d03e9275732429821684d574f6efcf1fa4d4239b0d64093c25214941e04556 |`

### 1.5 Evidence/state table

In the table beginning

> `The objective nu(k)=(1+o(1))W(k) is not yet proved.`

insert immediately after

> `| cap-only one-sided twelfth-moment exponent ledger | Appendix G.1 | ... |`

the row

> `| rooted twelve-carrier Palm normalization, first-blocker tangent, and static-variance obstruction | Appendix G.2 | [I]; punctured-specific cumulative centered full-transition potential bound open |`

### 1.6 Appendix body

Insert all of Section 2 below immediately after the final sentence of
Appendix G.1,

> `High moments remove the fine-variance numerical obstruction but do not create the stopped-law transfer.`

and before

> `## Appendix H. Compensated Gate-B switching and its complete-catalogue Gram gate`

## 2. Insertion-ready Appendix G.2

### G.2 Rooted twelve-carrier Palm likelihood and the no-Freedman obstruction

This subsection gives the exact form of the missing comparison (G.29).
It proves a reduction and an obstruction, not Gate A.

Fix one root shore (V) of size (n).  In a current simple hypergraph
(H), put

\[
 \Gamma(F)=\{G:G\cap F\ne\varnothing\},\qquad
 \mathcal S_v=\{G:v\in G\},\qquad
 \Delta_C=\max_F|\Gamma(F)|.                       \tag{G.36}
\]

A rooted ordered twelve-carrier is
(gamma=(v;F_1,\ldots,F_{12})), where the (F_i)'s are distinct and
contain (v\in V).  Define

\[
 N_i=\Gamma(F_i)\setminus\mathcal S_v,qquad
 B_i=N_i\setminus\bigcup_{h<i}N_h,qquad e_i=|N_i|,
\]

\[
 U(\gamma)=\left|\bigcup_iN_i\right|,qquad
 D(\gamma)=\sum_i e_i-U(\gamma).                   \tag{G.37}
\]

If (m_G(\gamma)=|\{i:G\in N_i\}|), first-blocker counting gives the
exact normalization

\[
 \boxed{D(\gamma)=\sum_{G\notin\mathcal S_v}
                     (m_G(\gamma)-1)_+.}           \tag{G.38}
\]

In one isolated-edge microbite with marking probability (p), conditional
on survival of (v), and uniformly for (p\Delta_C\le1/100),

\[
 \Pr(\gamma\text{ survives}\mid v\text{ survives})
 =1-pU(\gamma)+O(p^2\Delta_C^2),
\]

\[
 {\Pr(\gamma\text{ survives}\mid v\text{ survives})
       \over\prod_i\Pr(F_i\text{ survives}\mid v\text{ survives})}
 =1+pD(\gamma)+O(p^2\Delta_C^2).                  \tag{G.39}
\]

For proof, the coefficient of (p) is the number of edges in the union
of the relevant closed conflict neighbourhoods: with exactly one mark that
edge is accepted.  Every discrepancy needs at least two marks in a union
of at most (12\Delta_C) edges, hence costs
(O(p^2\Delta_C^2)).  Dividing by the analogous root-survival expansion
removes the common star (mathcal S_v), and (G.38) gives the ratio.

Here and below the constants may depend on twelve, but not on the current
residual.

There is a necessary exact-slice correction.  Suppose the current and next
shore sizes are (n_\sigma,n'_\sigma), the root is retained, and

\[
 r_\sigma=\mathbf1_{\{v\in V_\sigma\}},\qquad
 \delta_\sigma=1-{n'_\sigma-r_\sigma\over n_\sigma-r_\sigma}.
\]

Let (b_{i\sigma}=|(F_i-\{v\})\cap V_\sigma|), let
(b_{\gamma\sigma}) be the corresponding union footprint, and put

\[
 q_{\gamma\sigma}=\sum_i b_{i\sigma},\qquad
 O_\sigma(\gamma)=\sum_i b_{i\sigma}-b_{\gamma\sigma}.
\]

The finite-population expansion requires the literal hypotheses

\[
 \boxed{\delta_\sigma\le1/4,qquad
 q_{\gamma\sigma}\le(n_\sigma-r_\sigma)/2}         \tag{G.40}
\]

on each shore.  They are automatic here because
(q_{\gamma\sigma}=O(r)) while retained shore sizes are exponential.
The exact uniform-slice survival factor is

\[
 s^{\rm sl}(\gamma)=
 \prod_\sigma{(n'_\sigma-r_\sigma)_{b_{\gamma\sigma}}
                    \over(n_\sigma-r_\sigma)_{b_{\gamma\sigma}}}.
\]

Writing (zeta_\sigma=\delta_\sigma/p) and
(B_i=e_i-\sum_\sigma\zeta_\sigma b_{i\sigma}), direct expansion gives

\[
 \log {s^{\rm act}(\gamma)\over s^{\rm sl}(\gamma)}
 =p\left\{D(\gamma)-\sum_iB_i
             -\sum_\sigma\zeta_\sigma O_\sigma(\gamma)\right\}
 +O(p^2\Delta_C^2+E_{\rm sl}),                    \tag{G.41}
\]

where

\[
 E_{\rm sl}=\sum_\sigma\left(
 q_{\gamma\sigma}\delta_\sigma^2+
 {q_{\gamma\sigma}^2\delta_\sigma\over n_\sigma}\right).
\]

Indeed, for (N=n_\sigma-r_\sigma), deleted count
(delta_\sigma N), and (b\le q_{\gamma\sigma}),

\[
 \log{(N-\delta_\sigma N)_b\over(N)_b}
 =\sum_{t<b}\log\left(1-{\delta_\sigma N\over N-t}\right)
 =-\delta_\sigma b
  +O\left(b\delta_\sigma^2+{b^2\delta_\sigma\over N}\right).
\]

Summing this identity over shores and combining it with (G.39) proves
(G.41).

Thus conflict-duplicate saving (D), marginal exposure bias (B_i), and
coordinate-overlap saving (O_\sigma) are distinct.  A proof using only
(D) must justify a one-sided disposal of the other two terms.

Let

\[
 T_{12}(H)=\sum_{v\in V}(d_H(v))_{12}
\]

and let (widehat\mu) be the Palm law obtained from a residual law
(mu) by adjoining a uniformly counted alive rooted twelve-carrier:

\[
 \widehat\mu(H,\gamma)=
 {\mu(H)\mathbf1_{\{\gamma\text{ alive in }H\}}
       \over\mathbb E_\mu T_{12}}.                 \tag{G.42}
\]

For (c\ge12), put

\[
 \psi_{c,z}(H,\gamma)={(d_H(v)-c)_+^{12}\over(d_H(v))_{12}},
 \qquad
 U_{12,c}(H)={1\over nz^{12}}
       \sum_{v\in V}(d_H(v)-c)_+^{12},
\]

with value zero below degree twelve.  Then exactly

\[
 \sum_{\gamma\text{ alive}}\psi_{c,z}(H,\gamma)
 =\sum_{v\in V}(d_H(v)-c)_+^{12}.                 \tag{G.43}
\]

Consequently, let (mu) be an actual stopped law in one deterministic
density bin and (mu_0) the uniform exact-slice law, applied fiberwise at
the same exact shore sizes.  If

\[
 d_H(v)\le Kz,qquad
 \mathbb E_{\mu_0}T_{12}\ge a\,nz^{12},qquad
 \left\|{d\widehat\mu\over d\widehat\mu_0}\right\|_\infty
       \le r^{\kappa+o(1)},                        \tag{G.44}
\]

then

\[
 \boxed{
 \mathbb E_\mu U_{12,c}
 \le {K^{12}\over a}r^{\kappa+o(1)}
           \mathbb E_{\mu_0}U_{12,c}.}             \tag{G.45}
\]

Indeed (T_{12}\le n(Kz)^{12}), and (G.43) converts both sides to Palm
expectations.  If (z=n^{-1}\sum_{v\in V}d(v)\ge22), the reference mass
lower bound is automatic with (a=2^{-12}), since
((d)_{12}\ge(d-11)_+^{12}) and Jensen gives
(T_{12}\ge n(z-11)^{12}).  Fixed-ratio bin variation only changes the
constant.

Combining (G.45) with the reference estimate
(U_{12,c}^{\rm ref}=O((r\xi^3)^{-6})+e^{-\Omega(r)}) proves precisely
(G.29).  The already audited ledger then gives full shore-safe descent
only under

\[
 \boxed{\kappa<2-20\alpha;}                         \tag{G.46}
\]

(kappa<2-18\alpha) reaches only the separately imposed shore/floor
stop.

The Palm likelihood has an exact Doob form.  Let (pi_jK_j=\pi_{j+1})
be reference Palm transitions, and let the actual possibly killed
transition have density (r_j(x,y)) with respect to (K_j).  If
(f_j=d\widehat\mu_j/d\pi_j), then

\[
 \widetilde f_{j+1}(y)=
 {\int f_j(x)r_j(x,y)K_j(x,dy)\pi_j(dx)
       \over\pi_{j+1}(dy)},\qquad
 f_{j+1}={\widetilde f_{j+1}\over
                 \pi_{j+1}(\widetilde f_{j+1})}.   \tag{G.47}
\]

If (r_j(x,y)=w_j(x)) and the carrier type persists, this becomes

\[
 \log f_{j+1}-\log f_j
 =\ell_j-\log\mathbb E_{\widehat\mu_j}e^{\ell_j},
 \qquad \ell_j=\log w_j.                           \tag{G.48}
\]

For the duplicate part, (ell_j=p_jD_j+O(p_j^2\Delta_{C,j}^2)), so the
first-order increment is
(p_j(D_j-\mathbb E_{\widehat\mu_j}D_j)).  The common drift therefore
cancels, but the expectation is under the already tilted Palm law.

This centered increment is not a martingale difference.  In the exact
two-type recursion with initial rare mass (eta), persistent transition,
and weights (w(A)=1,w(B)=e^\delta),

\[
 \pi_t(B)={\eta e^{t\delta}\over1-\eta+\eta e^{t\delta}},
 \qquad
 f_t(B)={e^{t\delta}\over1-\eta+\eta e^{t\delta}}. \tag{G.49}
\]

At the first (T) with (e^{T\delta}\ge\eta^{-1}), one has
(f_T(B)\ge(3\eta)^{-1}), while

\[
 \sum_{t<T}\operatorname {Var}_{\pi_t}
       (\delta\mathbf1_B)
 =\delta^2\sum_{t<T}\pi_t(B)(1-\pi_t(B))\le2\delta. \tag{G.50}
\]

The last bound follows from

\[
 \pi_{t+1}(B)-\pi_t(B)
 ={\pi_t(B)(1-\pi_t(B))(e^\delta-1)
       \over1+\pi_t(B)(e^\delta-1)}
 \ge{\delta\over2}\pi_t(B)(1-\pi_t(B)),
\]

followed by telescoping.

Thus (eta=r^{-\kappa}), (delta\to0) gives polynomial likelihood
amplification while the static quadratic sum tends to zero.  Freedman's
inequality cannot be applied to this predictable positive type drift.

The phenomenon has a simple-hypergraph realization.  In

\[
 H_M=K_{13}\mathbin{\dot\cup}M K_{12,12},           \tag{G.51}
\]

every target has degree twelve and every edge has closed conflict degree
23.  For a full rooted star, (D=66) in (K_{13}) and (D=0) in
(K_{12,12}).  Every target-pair codegree is zero or one, so the
pair-square energy is exactly zero.  The sixth centered row defect is zero
on the bipartite components and equals
(13\binom{12}{2}\phi_{12}(12,2)=13\cdot66\cdot62) on (K_{13});
after division by (|V(H_M)|12^6) it tends to zero.  Yet a full-star
carrier survives a bite exactly when its component accepts no edge.  If
(a_G(p)) is that probability, then

\[
 \log{a_{K_{13}}(p)\over a_{K_{12,12}}(p)}
 =66p+O(p^2).                                       \tag{G.52}
\]

With (M\asymp r^\kappa), (p=o(1/\log r)), and
(T\sim\kappa\log r/(66p)), the rare carrier type acquires likelihood
(r^{\kappa+o(1)}).  This is a general-hypergraph obstruction to deriving
Palm domination from the static energies alone; it is not asserted to be
a punctured residual.

For completeness, current centered defect does give an un-tilted first
moment.  Define

\[
 a_G(v)=|\{F\ni v:F\cap G\ne\varnothing\}|,\qquad
 Q_{2,v}=\sum_{G\not\ni v}(a_G(v))_2,
\]

\[
 f_z(d)=(d-z)^6,\qquad
 \phi_z(d,a)=a\{f_z(d)-f_z(d-1)\}
              -\{f_z(d)-f_z(d-a)\},
\]

\[
 \mathfrak D_z=\sum_{v\in V}\sum_{G\not\ni v}
                      \phi_z(d(v),a_G(v)).
\]

a uniform ordered twelve-tuple in a degree-(d) root star satisfies

\[
 \mathbb E_\gamma D(\gamma)
 \le{\binom{12}{2}\over(d)_2}Q_{2,v}.              \tag{G.53}
\]

The high-root sixth row defect further yields, under
(T_{12}\ge a_0nz^{12}), (d\le Kz), and (d-z\ge\delta z),

\[
 {1\over T_{12}}\sum_{v:d(v)-z\ge\delta z}
 (d(v))_{12}\mathbb E_\gamma D(\gamma)
 \le C_{\delta,K,a_0}{\mathfrak D_z\over nz^6}.    \tag{G.54}
\]

Indeed a hypergeometric pair count gives (G.53).  Twice differencing
(f_z) gives

\[
 \phi_z(d,a)=\sum_{s=0}^{a-2}(a-1-s)
 \{30(d-z-s-1)^4+30(d-z-s-1)^2+2\}.
\]

On (d-z\ge\delta z), (d\le Kz), this is at least
(c_{\delta,K}z^4(a)_2): if (a\le(d-z)/2), every summand has a
fourth-power factor of order (z^4); otherwise retain the first
$\lfloor(d-z)/4\rfloor$ summands to obtain
$\Omega_{\delta,K}(a(d-z)^5)\ge c_{\delta,K}z^4a^2$.
Multiplying (G.53) by ((d)_{12}), using
((d)_{12}/(d)_2=(d-2)_{10}\le(Kz)^{10}), summing, and dividing by
(T_{12}\ge a_0nz^{12}) proves (G.54).

This is under the current un-tilted Palm law and does not control the
successively tilted occupation in (G.48).

Finally, refresh is not currently available.  In the literal deletion-only
residual, every alive labelled carrier at checkpoint (j+1) has a unique
persistent parent at checkpoint (j).  The natural carrier genealogy is
therefore identity on the label: its projective contraction parameter is
$\tau_j=1$, and its forced-refresh rate is $\lambda_j=0$.  Redrawing a
carrier for analysis does not refresh its residual component or hidden
type.

Accordingly, the exact remaining Gate-A input for the unchanged process is
a punctured-specific stopped one-sided bound on the cumulative full
centered transition potential.  In the state-factorized identity case it
is enough to prove

\[
 \boxed{
 \sup_{J\le\tau_{\rm stop}}\operatorname*{ess\,sup}_\gamma
 \sum_{i<J}\left\{\ell_i(\gamma)
       -\log\mathbb E_{\widehat\mu_i}e^{\ell_i}\right\}
 \le(\kappa+o(1))\log r,\qquad \kappa<2-20\alpha.} \tag{G.55}
\]

For the actual transition (G.47), the summand must be the full log
transition density, including the conditional residual-environment factor,
and past histories must be averaged conditional on the terminal state.
Equivalently, if (Q) is the reference carrier-history law and
(L_J=\prod_{i<J}r_i(X_i,X_{i+1})), the exact full gate is

\[
 \boxed{
 \sup_{J\le\tau_{\rm stop}}\operatorname*{ess\,sup}_y
 \log {\mathbb E_Q[L_J\mid X_J=y]\over\mathbb E_Q L_J}
 \le(\kappa+o(1))\log r,
 \qquad\kappa<2-20\alpha.}                         \tag{G.56}
\]

This may use signed punctured-specific cancellation.  Static pair-square
or centered-defect variance does not prove it.  The only alternative is a
separately authorized modified algorithm with genuine carrier rewiring or
resampling.  The finite-bite and predictable-to-realized-center errors in
(G.35) remain separate requirements.
