# Gate A: rooted twelve-carrier likelihood, duplicate selection, and the exact refresh gate

**Date:** 2026-08-22  
**Status:** self-contained reduction and obstruction; the stopped comparison is
not proved

This note analyzes the remaining input in the cap-only $m=12$ Gate-A
theorem.  Its conclusions are deliberately separated.

1. The first-order likelihood of a rooted ordered twelve-carrier has an
   exact first-blocker decomposition.  Relative to an exact-slice
   checkpoint, its genuinely joint term is conflict-duplicate saving minus
   coordinate-overlap saving.
2. Palm normalization cancels the carrier-averaged part of that potential.
   It does **not** make the potential a martingale: a carrier type persists.
3. A two-type Feynman--Kac system has polynomial likelihood amplification
   while the sum of its static quadratic variances tends to zero.  The
   phenomenon is realized, to first order and over arbitrarily many
   survivor steps, by the simple hypergraph
   $K_{13}\mathbin{\dot\cup}M K_{12,12}$.  Its pair-square energy is zero
   and its normalized sixth row defect tends to zero.
4. A precise reverse-kernel refresh inequality *would* imply the required
   density-bin $U_{12}$ comparison.  The weakest form needed by the
   present argument is displayed in (8.8).  Neither the pair-square energy
   nor the centered row defect currently implies it.

Thus the common-drift cancellation is real, but a Freedman argument based
only on static variance is invalid.  The new remaining input is a stopped
carrier refresh/mixing theorem, or an equivalent bound on the reverse
Feynman--Kac density.

## 1. Rooted carriers and first blockers

Let $H$ be a finite simple hypergraph.  For an edge $F$, put

\[
 \Gamma(F)=\{G\in E(H):G\cap F\ne\varnothing\},\qquad
 \Delta_C=\max_F|\Gamma(F)|.                         \tag{1.1}
\]

Fix a target $v$, write

\[
 \mathcal S_v=\{G:v\in G\},\qquad d=d(v),           \tag{1.2}
\]

and let

\[
 \gamma=(v;F_1,\ldots,F_{12})                       \tag{1.3}
\]

be an ordered tuple of twelve distinct edges through $v$.  Define its
external conflict sets, first-blocker cells, and individual external
exposures by

\[
 N_i=\Gamma(F_i)\setminus\mathcal S_v,\qquad
 B_i=N_i\setminus\bigcup_{h<i}N_h,\qquad e_i=|N_i|. \tag{1.4}
\]

The external union exposure and duplicate saving are

\[
 U(\gamma)=\left|\bigcup_iN_i\right|=\sum_i|B_i|,
 \qquad
 D(\gamma)=\sum_i e_i-U(\gamma).                    \tag{1.5}
\]

For $G\notin\mathcal S_v$, let

\[
 m_G(\gamma)=|\{i:G\in N_i\}|.                     \tag{1.6}
\]

Then the first-blocker identity is exact:

\[
 \boxed{D(\gamma)=\sum_{G\notin\mathcal S_v}
                    (m_G(\gamma)-1)_+\ge0.}         \tag{1.7}
\]

Indeed $G$ is charged once by the union and $m_G$ times by the
individual sum.  This identity fixes both the ordering convention and the
normalization: $D$ counts conflict **edges**, not ordered pairs of
carriers.

## 2. The isolated-edge microbite

Independently mark every current edge with probability $p$.  A marked
edge is accepted when it has no other marked neighbour; delete all targets
of accepted edges and take the induced residual.  Let $R_v$ be the event
that $v$ survives, and $A_\gamma$ the event that all twelve carriers in
$\gamma$ survive.

### Theorem 2.1 (joint versus marginal carrier survival)

If $p\Delta_C\le1/4$, then, uniformly in $H,v,\gamma$,

\[
 \Pr(R_v)=1-pd+O(p^2\Delta_C^2),                    \tag{2.1}
\]

\[
 \Pr(A_\gamma\mid R_v)
       =1-pU(\gamma)+O(p^2\Delta_C^2),              \tag{2.2}
\]

and for one carrier

\[
 \Pr(F_i\hbox{ survives}\mid R_v)
       =1-pe_i+O(p^2\Delta_C^2).                    \tag{2.3}
\]

Consequently

\[
 \boxed{
 {\Pr(A_\gamma\mid R_v)\over
   \prod_i\Pr(F_i\hbox{ survives}\mid R_v)}
 =1+pD(\gamma)+O(p^2\Delta_C^2).}                  \tag{2.4}
\]

#### Proof

For any fixed family $\mathcal A$ of at most twelve edges, its members all
survive unless an accepted edge lies in
\(\bigcup_{F\in\mathcal A}\Gamma(F)\).  The contribution of exactly one
mark is therefore minus the cardinality of that union.  The event that a
marked edge in the union is blocked by another mark, or that the union has
two marks, has probability $O(p^2\Delta_C^2)$.  Thus

\[
 \Pr(A_\gamma)=1-p\{d+U(\gamma)\}
                  +O(p^2\Delta_C^2),               \tag{2.5}
\]

because every $\Gamma(F_i)$ contains the whole star $\mathcal S_v$.
The same argument gives (2.1).  Division proves (2.2); applying it to a
single $F_i$ proves (2.3).  Multiplying the twelve marginal expansions
and using (1.5) proves (2.4).  $\square$

The term $pD$ is the exact tangent which is lost if the twelve carriers
are treated independently.

## 3. Exact-slice correction and the full tangent

Suppose the current shores have sizes $n_\sigma$, the next checkpoint
has sizes $n'_\sigma$, and the root is retained.  Put

\[
 r_\sigma=\mathbf1_{\{v\in V_\sigma\}},\qquad
 \delta_\sigma=1-{n'_\sigma-r_\sigma\over
                         n_\sigma-r_\sigma}.        \tag{3.1}
\]

For the external coordinate footprints define

\[
 b_{i\sigma}=|(F_i\setminus\{v\})\cap V_\sigma|,
 \quad
 b_{\gamma\sigma}=
   |((\bigcup_iF_i)\setminus\{v\})\cap V_\sigma|, \tag{3.2}
\]

\[
 O_\sigma(\gamma)=\sum_i b_{i\sigma}-b_{\gamma\sigma}\ge0. \tag{3.3}
\]

Put $q_{\gamma\sigma}=\sum_i b_{i\sigma}$.  In the nested uniform
exact-slice process, conditional on retaining $v$,
the exact one-step survival probability of the carrier is

\[
 s^{\rm sl}(\gamma)=
 \prod_\sigma{(n'_\sigma-r_\sigma)_{b_{\gamma\sigma}}
                    \over
                    (n_\sigma-r_\sigma)_{b_{\gamma\sigma}}}. \tag{3.4}
\]

Assume for this expansion that

\[
 \delta_\sigma\le1/4,qquad
 q_{\gamma\sigma}\le{n_\sigma-r_\sigma\over2}      \tag{3.4a}
\]

on every shore.  These conditions are automatic in the punctured regime,
where (q_{\gamma\sigma}=O(r)) and the retained shore sizes are
exponential in (r).

Expansion of the finite product gives, uniformly also when the edge size
grows,

\[
 \log s^{\rm sl}(\gamma)
 =-\sum_\sigma\delta_\sigma b_{\gamma\sigma}
  +O\!\left(\sum_\sigma
       \{q_{\gamma\sigma}\delta_\sigma^2
        +q_{\gamma\sigma}^2\delta_\sigma/n_\sigma\}\right). \tag{3.5}
\]

Here one only uses $\log(1-y)=-y+O(y^2)$ and
$(n_\sigma-r_\sigma-t)^{-1}=(n_\sigma-r_\sigma)^{-1}\{1+O(q_{\gamma\sigma}/n_\sigma)\}$.
Assume from now on the Taylor-safe bound
$p\Delta_C\le1/100$.  It follows from (2.2)--(2.3) and (3.5) that the joint-to-product
correlation relative to the slice has tangent

\[
 \boxed{
 \log {s^{\rm act}(\gamma)/\prod_i s^{\rm act}(F_i)
             \over
             s^{\rm sl}(\gamma)/\prod_i s^{\rm sl}(F_i)}
 =pD(\gamma)-\sum_\sigma\delta_\sigma O_\sigma(\gamma)
  +O(p^2\Delta_C^2+E_{\rm sl}),}                  \tag{3.6}
\]

where

\[
 E_{\rm sl}=\sum_\sigma
       (q_{\gamma\sigma}\delta_\sigma^2
        +q_{\gamma\sigma}^2\delta_\sigma/n_\sigma). \tag{3.7}
\]

For the full rather than correlation-only likelihood, put

\[
 \zeta_\sigma=\delta_\sigma/p,\qquad
 B_i=e_i-\sum_\sigma\zeta_\sigma b_{i\sigma}       \tag{3.8}
\]

when $p>0$.  Then

\[
 \boxed{
 \log {s^{\rm act}(\gamma)\over s^{\rm sl}(\gamma)}
 =p\left\{D(\gamma)-\sum_iB_i
                 -\sum_\sigma\zeta_\sigma O_\sigma(\gamma)\right\}
  +O(p^2\Delta_C^2+E_{\rm sl}).}                  \tag{3.9}
\]

Thus $D$ is only one of three shape terms.  The $B_i$'s are marginal
exposure biases and the $O_\sigma$'s are the exact-slice coordinate
duplicate savings.  Any likelihood proof which retains $D$ but discards
the other two terms must justify the resulting one-sided inequality.

## 4. Palm normalization and the density-bin target

Fix one root shore $V$ of size $n$.  For a residual $H$, let

\[
 \mathcal T_{12}(H)=\{(v;F_1,\ldots,F_{12}):v\in V,
              F_i\ne F_j,\ v\in F_i\},
 \quad T_{12}(H)=|\mathcal T_{12}(H)|
                =\sum_{v\in V}(d(v))_{12}.         \tag{4.1}
\]

If $\mu$ is a law on residuals, its rooted twelve-carrier Palm law is

\[
 \widehat\mu(H,\gamma)=
 {\mu(H)\mathbf1_{\{\gamma\in\mathcal T_{12}(H)\}}
       \over \mathbb E_\mu T_{12}}.                \tag{4.2}
\]

This is a probability measure.  For a threshold $c\ge12$, define

\[
 \psi_{c,z}(H,\gamma)=
 { (d_H(v)-c)_+^{12}\over(d_H(v))_{12}},            \tag{4.3}
\]

with value zero when $d_H(v)<12$.  The exact positive-carrier identity is

\[
 \boxed{
 \sum_{\gamma\in\mathcal T_{12}(H)}\psi_{c,z}(H,\gamma)
 =\sum_{v\in V}(d_H(v)-c)_+^{12}.}                 \tag{4.4}
\]

### Theorem 4.1 (Palm domination implies the stopped $U_{12}$ comparison)

Let $\mu$ be an actual stopped density-bin law and $\mu_0$ the uniform
exact-slice reference law on the same labelled shores.  Suppose throughout
the bin that

\[
 d_H(v)\le Kz,\qquad
 \mathbb E_{\mu_0}T_{12}\ge a\,nz^{12},           \tag{4.5}
\]

where $a,K>0$ are fixed; fixed-ratio variations of $n,z$ are absorbed
in these constants.  If

\[
 \left\|{d\widehat\mu\over d\widehat\mu_0}\right\|_\infty
 \le r^{\kappa+o(1)},                              \tag{4.6}
\]

then

\[
 \boxed{
 \mathbb E_\mu U_{12,c}
 \le {K^{12}\over a}\,r^{\kappa+o(1)}
             \mathbb E_{\mu_0}U_{12,c},}           \tag{4.7}
\]

where $U_{12,c}=(nz^{12})^{-1}\sum_{v\in V}(d(v)-c)_+^{12}$.

When $z=n^{-1}\sum_{v\in V}d(v)$ is the actual shore average and
$z\ge22$, the second part of (4.5) is automatic, state by state, with
$a=2^{-12}$.  Indeed
$(d)_{12}\ge(d-11)_+^{12}$, and convexity plus Jensen gives

\[
 T_{12}\ge n(z-11)^{12}\ge2^{-12}nz^{12}.          \tag{4.5a}
\]

If the bin center differs from the actual average by a fixed factor, only
the constant changes.  The theorem is applied fiberwise at exact shore
sizes inside a deterministic density bin; averaging the fiberwise
inequality preserves (4.7).

#### Proof

By (4.4),

\[
 \mathbb E_\mu U_{12,c}
 ={\mathbb E_\mu T_{12}\over nz^{12}}
       \mathbb E_{\widehat\mu}\psi_{c,z}.
\]

The cap gives $T_{12}\le n(Kz)^{12}$.  Equations (4.5)--(4.6) and
(4.4), now under $\mu_0$, give

\[
 \mathbb E_{\widehat\mu}\psi
 \le r^{\kappa+o(1)}\mathbb E_{\widehat\mu_0}\psi
 \le {r^{\kappa+o(1)}\over a}
          \mathbb E_{\mu_0}U_{12,c}.
\]

Multiplication proves (4.7).  $\square$

The normalization audit is important.  The common carrier mass is not
silently set to one: the actual mass is bounded by the cap and the
reference mass is bounded below in (4.5).  In the punctured application
the latter is a separate fixed-slice factorial-moment check.  With the
reference estimate

\[
 \mathbb E_{\mu_0}U_{12,c}=O((r\xi^3)^{-6})+e^{-\Omega(r)}, \tag{4.8}
\]

(4.7) is exactly the stopped comparison required by the high-moment
ledger.  Its full shore-safe conclusion requires

\[
 \boxed{\kappa<2-20\alpha,\qquad x_*=r^{-\alpha};}  \tag{4.9}
\]

$\kappa<2-18\alpha$ reaches only the separate shore/floor stop.

## 5. Exact Doob--Feynman--Kac recursion

The carrier state must include enough of the residual history to make the
transition Markov.  Let $\pi_j$ be a reference carrier-Palm law and let
$K_j(x,dy)$ be a reference carrier transition satisfying
$\pi_jK_j=\pi_{j+1}$.  Its reverse operator is

\[
 K_j^\leftarrow g(y)=
 {\int g(x)K_j(x,dy)\pi_j(dx)\over\pi_{j+1}(dy)}.  \tag{5.1}
\]

It is a Markov operator.  More generally, let the actual possibly killed
carrier kernel be absolutely continuous with respect to $K_j$, with
transition density $r_j(x,y)$.  If
$f_j=d\widehat\mu_j/d\pi_j$, its unnormalized and normalized next
densities are exactly

\[
 \widetilde f_{j+1}(y)=
 {\int f_j(x)r_j(x,y)K_j(x,dy)\pi_j(dx)
        \over\pi_{j+1}(dy)},\qquad
 f_{j+1}={\widetilde f_{j+1}\over
                    \pi_{j+1}(\widetilde f_{j+1})}. \tag{5.1a}
\]

This is the general Doob recursion; it includes the conditional residual
environment.  If the density factors as $r_j(x,y)=w_j(x)$, it reduces to

\[
 \boxed{
 f_{j+1}=K_j^\leftarrow
 \left({f_jw_j\over\pi_j(f_jw_j)}\right).}          \tag{5.2}
\]

For a persistent carrier with a fixed reference type law,
$K_j^\leftarrow$ is the identity.  Writing
$\ell_j=\log w_j$ and letting $\widehat\mu_j$ denote the already tilted
Palm law, (5.2) becomes

\[
 \log f_{j+1}(x)-\log f_j(x)
 =\ell_j(x)-\log\mathbb E_{\widehat\mu_j}e^{\ell_j}. \tag{5.3}
\]

If $\ell_j=p_jD_j+O(p_j^2\Delta_{C,j}^2)$, then

\[
 \boxed{
 \log f_{j+1}-\log f_j
 =p_j\{D_j-\mathbb E_{\widehat\mu_j}D_j\}
   +O(p_j^2\Delta_{C,j}^2).}                       \tag{5.4}
\]

This is the promised cancellation of common drift.  The expectation in
(5.4) is under the **current tilted Palm law**, not the un-tilted slice
law.

For the actual isolated-edge process, (3.9) supplies the survival part of
$\ell_j$.  A comparison with a uniform nested-slice process can also have
a Radon--Nikodym factor from the residual environment conditional on
carrier survival.  That factor is the $y$-dependent part of $r_j(x,y)$ in
(5.1a); it cannot in general be replaced by a state-only $w_j$.  The
first-blocker calculation alone does not identify or control it.

## 6. What the current defect controls

For $G\not\ni v$, put

\[
 a_G(v)=|\{F\ni v:F\cap G\ne\varnothing\}|,\qquad
 Q_{2,v}=\sum_{G\not\ni v}(a_G(v))_2.               \tag{6.1}
\]

Choose $\gamma$ uniformly from the ordered distinct twelve-tuples in the
star of a root of degree $d\ge12$.  For each $G$, its selected
multiplicity is hypergeometric, so

\[
 \mathbb E(m_G)_2={(12)_2(a_G(v))_2\over(d)_2}.     \tag{6.2}
\]

Since $(m-1)_+\le{m\choose2}$, (1.7) gives the exact bridge

\[
 \boxed{
 \mathbb E_\gamma D(\gamma)
 \le {\binom{12}{2}\over(d)_2}Q_{2,v}.}            \tag{6.3}
\]

Now let $f_z(d)=(d-z)^6$ and

\[
 \phi_z(d,a)=a\{f_z(d)-f_z(d-1)\}
              -\{f_z(d)-f_z(d-a)\}.                \tag{6.4}
\]

Twice differencing gives

\[
 \phi_z(d,a)=\sum_{s=0}^{a-2}(a-1-s)
 \{30(d-z-s-1)^4+30(d-z-s-1)^2+2\}\ge(a)_2.       \tag{6.5}
\]

Hence the total centered row defect

\[
 \mathfrak D_z=\sum_{v\in V}\sum_{G\not\ni v}
                         \phi_z(d(v),a_G(v))        \tag{6.6}
\]

controls $\sum_{v\in V}Q_{2,v}$.  On the genuinely high tail it controls four
additional powers of $z$.

### Lemma 6.1 (high-root strengthening)

Fix $\delta,K>0$.  If $z\ge8/\delta$,
$(1+\delta)z\le d\le Kz$, and $0\le a\le d$, then

\[
 \boxed{\phi_z(d,a)\ge c_{\delta,K}z^4(a)_2.}       \tag{6.7}
\]

#### Proof

Put $t=d-z\ge\delta z$.  If $a\le t/2$, every summand in (6.5) has
$|d-z-s-1|\ge t/3$, after decreasing the constant to cover endpoints.
The sum of the triangular weights is $(a)_2/2$, proving (6.7).

If $a>t/2$, retain the first $\lfloor t/4\rfloor$ summands.  Their
fourth-power factors are at least $ct^4$, their weights are at least
$ca$, and there are at least $ct$ of them.  The retained sum is at
least $cat^5$.  Since $a\le Kz$ and $t\ge\delta z$,
$at^5\ge c_{\delta,K}z^4a^2$, which is (6.7).
$\square$

If $T_{12}\ge a_0nz^{12}$ and $d\le Kz$, equations (6.3) and (6.7)
therefore imply the un-tilted high-carrier estimate

\[
 {1\over T_{12}}
 \sum_{\substack{v:(d(v)-z)\ge\delta z}}
 (d(v))_{12}\,\mathbb E_\gamma D(\gamma)
 \le C_{\delta,K,a_0}{\mathfrak D_z\over nz^6}.    \tag{6.8}
\]

Indeed $(d)_{12}/(d)_2=(d-2)_{10}\le(Kz)^{10}$.
This is a useful static first-moment estimate.  It is not a bound on the
same quantity under the successively tilted laws in (5.4).  Also,
$D\le12\Delta_C$ gives only

\[
 \operatorname {Var}_\pi(pD)
 \le p^2\mathbb E_\pi D^2
 \le12p^2\Delta_C\,\mathbb E_\pi D,                \tag{6.9}
\]

again under the current un-tilted Palm law.

## 7. Why centered static variance is not Freedman variance

### Proposition 7.1 (exact two-type selection obstruction)

Let a carrier have types $A,B$, with initial masses
$\pi_0(B)=\eta$ and $\pi_0(A)=1-\eta$.  At every step use the persistent
identity transition and weights

\[
 w(A)=1,\qquad w(B)=e^\delta,\qquad0<\delta\le1.  \tag{7.1}
\]

Then

\[
 \pi_t(B)={\eta e^{t\delta}\over1-\eta+\eta e^{t\delta}},
 \qquad
 f_t(B)={e^{t\delta}\over1-\eta+\eta e^{t\delta}}. \tag{7.2}
\]

If $T$ is the first integer with $e^{T\delta}\ge\eta^{-1}$, then

\[
 f_T(B)\ge {1\over3\eta}                            \tag{7.3}
\]

for $\delta\le1$, whereas the sum of the static centered quadratic
terms satisfies

\[
 \boxed{
 \sum_{t<T}\operatorname {Var}_{\pi_t}
       (\delta\mathbf1_B)
 =\delta^2\sum_{t<T}\pi_t(B)(1-\pi_t(B))
 \le2\delta.}                                      \tag{7.4}
\]

#### Proof

Equation (7.2) is the exact normalized Feynman--Kac recursion.  At the
chosen $T$, $1\le\eta e^{T\delta}\le e^\delta$, which gives (7.3).
Moreover

\[
 \pi_{t+1}(B)-\pi_t(B)
 ={\pi_t(B)(1-\pi_t(B))(e^\delta-1)
       \over1+\pi_t(B)(e^\delta-1)}
 \ge{\delta\over2}\pi_t(B)(1-\pi_t(B)).           \tag{7.5}
\]

Summing (7.5) proves (7.4).  $\square$

Taking $\eta=r^{-\kappa}$ and $\delta\to0$ yields likelihood
$\Omega(r^\kappa)$ with a quadratic sum tending to zero.  Along the
persistent $B$-carrier, the centered quantity
$\delta\{1-\pi_t(B)\}$ is predictable positive drift, not a martingale
difference.  Therefore neither (7.4) nor (6.9) is a predictable quadratic
variation to which Freedman's inequality can be applied.

### Proposition 7.2 (simple-hypergraph realization)

Let

\[
 H_M=K_{13}\mathbin{\dot\cup}
       \underbrace{K_{12,12}\mathbin{\dot\cup}\cdots
       \mathbin{\dot\cup}K_{12,12}}_{M\ {\mathrm{copies}}},   \tag{7.6}
\]

viewed as a simple $2$-uniform hypergraph.  Then:

1. every target has degree $12$, and every edge has
   $|\Gamma(F)|=23$;
2. for the ordered full star at a root,

   \[
    D=66\quad\hbox{in }K_{13},\qquad D=0\quad\hbox{in }K_{12,12}; \tag{7.7}
   \]

3. every target-pair codegree is zero or one, so

   \[
    \sum_P\lambda_P(\lambda_P-1)^2=0;              \tag{7.8}
   \]

4. with $z=12$, the sixth centered row defect is zero on every bipartite
   component and equals

   \[
    13\binom{12}{2}\phi_{12}(12,2)
    =13\cdot66\cdot62                              \tag{7.9}
   \]

   on $K_{13}$.  Hence
   $\mathfrak D_{12}/(|V(H_M)|12^6)\to0$.

#### Proof

In a simple $12$-regular graph, the closed conflict neighbourhood of an
edge has $12+12-1=23$ edges.  At a $K_{13}$ root, the 66 nonstar edges
each meet two of the twelve star carriers, so (1.7) gives $D=66$.  At a
$K_{12,12}$ root, every nonstar edge meets exactly one star carrier, so
$D=0$.  Statement (7.8) is immediate for a $2$-uniform simple
hypergraph.

For a row $(v,G)$, $a_G(v)=2$ precisely when both endpoints of $G$
are neighbours of $v$.  This never occurs in the triangle-free
$K_{12,12}$, while it occurs for all 66 nonstar edges at every
$K_{13}$ root.  Formula (6.5) gives
$\phi_{12}(12,2)=30+30+2=62$, proving (7.9).  $\square$

This realization also persists for arbitrarily many survivor steps.  For
a finite graph $G$, let $a_G(p)$ be the probability that one
isolated-edge microbite accepts no edge of $G$.  A full-star carrier in
either component of (7.6) survives exactly when its component accepts no
edge; on that event the component is unchanged.  Since a one-mark set
always produces one accepted edge,

\[
 a_G(p)=1-|E(G)|p+O_G(p^2).                         \tag{7.10}
\]

As $|E(K_{13})|=78$ and $|E(K_{12,12})|=144$,

\[
 \log{a_{K_{13}}(p)\over a_{K_{12,12}}(p)}
 =66p+O(p^2).                                       \tag{7.11}
\]

The initial full-star Palm mass of the $K_{13}$ type is

\[
 \eta_M={13\over13+24M}.                            \tag{7.12}
\]

Choose $M\asymp r^\kappa$, $p=o(1/\log r)$, and
$T\sim\kappa\log r/(66p)$.  Independence of successive markings and
the unchanged-on-survival observation make the type weight ratio exactly
$(a_{K_{13}}(p)/a_{K_{12,12}}(p))^T=r^{\kappa+o(1)}$.
Thus the abstract selection obstruction is not an artefact of arbitrary
weights.  This graph is an obstruction to a *general hypergraph
implication* from the displayed static energies; it is not asserted to be
a punctured residual.

## 8. The exact sufficient refresh/mixing gate

Let

\[
 \omega_j=\operatorname {osc}(\log w_j)
 =\sup_x\log w_j(x)-\inf_x\log w_j(x).              \tag{8.1}
\]

The cap-only first-blocker estimate gives
$\omega_j=O(p_j\Delta_{C,j})=O(\epsilon_j)$ for the duplicate part, but
the full $\omega_j$ must also include the marginal, coordinate, and
conditional-environment factors identified after (3.9) and (5.4).

### Theorem 8.1 (projective contraction criterion)

Assume the factorized reverse carrier kernels in (5.2) obey, for every
positive $g$,

\[
 \operatorname {osc}\log K_j^\leftarrow g
 \le\tau_j\operatorname {osc}\log g,\qquad0\le\tau_j\le1. \tag{8.2}
\]

If $f_0=1$, then

\[
 \operatorname {osc}\log f_J
 \le\sum_{i<J}\omega_i\prod_{t=i}^{J-1}\tau_t.     \tag{8.3}
\]

Consequently the stopped inequality

\[
 \boxed{
 \sup_{J\le\tau_{\rm stop}}
 \sum_{i<J}\omega_i\prod_{t=i}^{J-1}\tau_t
 \le(\kappa+o(1))\log r}                           \tag{8.4}
\]

implies (4.6), and therefore the density-bin $U_{12}$ comparison.

#### Proof

Multiplication by $w_j$ adds at most $\omega_j$ to log oscillation;
normalization adds a constant and changes no oscillation.  Apply (8.2) in
(5.2) and iterate.  A probability density with log oscillation at most
$R$ has supremum at most $e^R$, because its mean is one.  Equations
(4.6)--(4.7) finish.  $\square$

There is also a completely explicit forced-refresh version which does not
pretend that a Doeblin atom automatically contracts log oscillation.

### Theorem 8.2 (forced resampling recurrence)

Suppose after selection the reverse carrier step has the form

\[
 K_j^\leftarrow g
 =\lambda_j\pi_j(g)+(1-\lambda_j)R_jg,              \tag{8.5}
\]

where $R_j$ is Markov and $0\le\lambda_j\le1$.  Put

\[
 a_j=(1-\lambda_j)e^{\omega_j},\qquad
 b_j=(1-\lambda_j)(e^{\omega_j}-1).                 \tag{8.6}
\]

If $M_j=\|f_j\|_\infty$ and $f_0=1$, then

\[
 M_J-1\le\sum_{i<J}b_i\prod_{t=i+1}^{J-1}a_t.      \tag{8.7}
\]

Hence the exact stopped refresh condition

\[
 \boxed{
 \sup_{J\le\tau_{\rm stop}}
 \left(1+\sum_{i<J}b_i\prod_{t=i+1}^{J-1}a_t\right)
 \le r^{\kappa+o(1)}}                              \tag{8.8}
\]

implies (4.6).  In particular, if
$\omega_j\le\omega\le1/4$ and
$\lambda_j\ge\lambda\ge2\omega$, then $M_J=O(1)$ uniformly in $J$.
For the cap-scale $\omega=O(\epsilon)$, a worst-case forced refresh rate
of order $\epsilon$, with a sufficiently large constant, is enough.

#### Proof

The selected normalized density is
$g_j=f_jw_j/\pi_j(f_jw_j)$.  Since the ratio between the largest and
smallest values of $w_j$ is $e^{\omega_j}$,
$\|g_j\|_\infty\le e^{\omega_j}M_j$.  Equation (8.5), positivity of
$R_j$, and $\pi_j(g_j)=1$ give

\[
 M_{j+1}-1
 \le(1-\lambda_j)(e^{\omega_j}M_j-1)
 =a_j(M_j-1)+b_j.                                   \tag{8.9}
\]

Iteration proves (8.7).  If $\lambda\ge2\omega$, then
$a_j\le e^{-\lambda+\omega}\le e^{-\lambda/2}$ and
$b_j\le2\omega$; summing the geometric bound proves the last assertion.
$\square$

Equation (8.8), rather than a pointwise static variance estimate, is the
weakest single stopped refresh inequality used by this reduction.  With
no refresh, $\lambda_j=0$, it reduces to the cumulative oscillation
bound and Proposition 7.1 is sharp in order of magnitude.

For the literal deletion-only residual, an alive labelled carrier at
checkpoint $j+1$ has a unique persistent parent at checkpoint $j$.
Its natural reverse genealogy is therefore deterministic on the carrier
label: in the notation above, $\tau_j=1$ and $\lambda_j=0$.  Merely
redrawing a carrier from the current residual for purposes of analysis
does not refresh the residual component or its hidden type and does not
create (8.5).  Thus forced refresh is a sufficient *hypothetical* route,
not a property currently available in the isolated-edge process.  Without
an authorized rewiring/resampling modification, the literal remaining
route is a punctured-specific stopped one-sided bound on the cumulative
centered potential (equivalently, its tilted occupation).  Such a bound
may exploit signed cancellation and need not pass through the cruder sum
of nonnegative oscillations in (8.4).

In the factorized identity-genealogy case, the exact direct substitute is

\[
 \boxed{
 \sup_{J\le\tau_{\rm stop}}\operatorname*{ess\,sup}_{\gamma}
 \sum_{i<J}\left\{\ell_i(\gamma)
       -\log\mathbb E_{\widehat\mu_i}e^{\ell_i}\right\}
 \le(\kappa+o(1))\log r.}                          \tag{8.9a}
\]

Equation (5.3) shows immediately that (8.9a) implies (4.6).  With the
general transition density in (5.1a), the summand must be replaced by the
full log transition density along a carrier history and then averaged over
past histories conditional on the terminal state.  That conditional
environment term is part of, not an error outside, the remaining gate.

For comparison, a genuine spectral-mixing hypothesis also explains where
a Freedman argument would enter.  In the homogeneous stationary case,
suppose $K$ preserves $\pi$, $g$ is $\pi$-centered, and

\[
 \|K^tg\|_\infty\le(1-\lambda)^t\|g\|_\infty.      \tag{8.10}
\]

Then $h=\sum_{t\ge0}K^tg$ solves $g=h-Kh$ and
$\|h\|_\infty\le\|g\|_\infty/\lambda$.  Along a stationary carrier
chain,

\[
 \sum_{j<T}g(X_j)=h(X_0)-h(X_T)
 +\sum_{j<T}\{h(X_{j+1})-Kh(X_j)\}.                \tag{8.11}
\]

The last sum is a martingale.  Thus a bound on its **predictable**
quadratic variation, together with
$\|g\|_\infty/\lambda=o(1)$, gives the desired exponential estimate by
Freedman.  Static estimates such as (6.8)--(6.9) concern
$\operatorname {Var}_\pi g$; they do not establish either (8.10) or the
predictable bound in (8.11).  This is exactly the missing logical step.

## 9. Surviving theorem and remaining Gate-A input

The following implication is now rigorous and has no hidden future-event
conditioning.

> In every deterministic density bin, if the reference carrier mass lower
> bound (4.5) holds and either the projective refresh condition (8.4) or
> the forced-refresh condition (8.8) holds for the full Palm likelihood,
> then the actual stopped tail moment is at most
> $r^{\kappa+o(1)}$ times its uniform exact-slice value.  With
> $\kappa<2-20\alpha$, this is the exact moment input needed for the
> previously audited full shore-safe $m=12$ Gate-A ledger.

What remains open for the unchanged deletion-only algorithm is the
$\tau_j=1$, $\lambda_j=0$ specialization: prove a punctured-specific
one-sided cumulative centered-potential/tilted-occupation bound that
directly replaces (8.4), including the conditional residual-environment
factor in (5.1a).
Alternatively one would have to construct and separately authorize a
modified process with genuine carrier rewiring or resampling.  The current
pair-square and centered-defect inventories give the un-tilted estimate
(6.8), but Propositions 7.1--7.2 prove that they cannot, by themselves, be
reinterpreted as stopped predictable quadratic variation or carrier
refresh.
