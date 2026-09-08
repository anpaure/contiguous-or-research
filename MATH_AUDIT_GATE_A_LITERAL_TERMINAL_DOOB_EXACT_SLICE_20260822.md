# Gate A: literal terminal Doob density for the isolated-edge deletion process

**Date:** 2026-08-22  
**Status:** exact self-contained reduction; no Gate-A comparison theorem is
claimed

This note derives the Radon--Nikodym identity underlying (G.63) without
factorizing away the residual environment.  There are two conclusions.

1. Relative to nested uniform exact slices, the literal isolated-edge
   process has an exact carrier-path density.  Conditional expectation over
   all reference histories ending at the terminal carrier state gives the
   terminal Palm density, with all exact-size and Palm normalizers visible.
2. Palm normalization removes constants and the carrier label from the
   *terminal* density, but it does not remove the residual-state likelihood.
   Even vertex- and edge-transitivity only makes the environment factor
   orbit-invariant.  A family of vertex- and edge-transitive 12-regular
   graphs makes that factor arbitrarily large in one exact-size bite while
   the carrier-survival ratio tends to one.

Thus the conditional-environment term in (G.63) is genuine.  It reduces to
an explicit signed log-likelihood statistic, not to zero.

## 1. Slices, residuals, and the literal bite

Let the labelled target universe be a disjoint union

\[
 V=\mathop{\dot\bigcup}_{\sigma=1}^q V_\sigma
\]

and let \(H_0\) be a fixed finite simple hypergraph on \(V\).  For
\(S\subseteq V\), write \(H(S)=H_0[S]\).  Fix a deterministic exact-size
schedule \(n_{j\sigma}\), and put

\[
 \Omega_j=\{S\subseteq V:|S\cap V_\sigma|=n_{j\sigma}\ \forall\sigma\},
 \qquad
 \lambda_j(S)={1\over|\Omega_j|}.                 \tag{1.1}
\]

The nested uniform-slice kernel is

\[
 U_j(S,S')={\mathbf1_{\{S'\subseteq S\}}\over C_j},
 \qquad
 C_j=\prod_\sigma {n_{j\sigma}\choose n_{j+1,\sigma}}.       \tag{1.2}
\]

The elementary nesting identity is

\[
                         \lambda_jU_j=\lambda_{j+1}.           \tag{1.3}
\]

Now perform one literal isolated-edge bite in \(H(S)\).  Mark every edge
independently with probability \(p_j(S)\).  An edge is accepted exactly
when it is marked and has no marked conflict neighbour.  Accepted edges
are pairwise disjoint; delete all of their vertices.  Let
\(P_j(S,S')\) be the resulting transition probability, restricted to
\(S'\in\Omega_{j+1}\).  Hence \(P_j\) is generally a subkernel: its lost
mass is the probability that the prescribed next exact sizes do not occur.
An imposed stopping condition can be incorporated afterward by multiplying
the displayed kernel by its measurable zero-one survival indicator.

There is a completely explicit formula.  Let \(G_S\) be the conflict graph
whose vertices are the edges of \(H(S)\), let \(N_{G_S}(A)\) and
\(N_{G_S}[A]\) be the open and closed neighbourhoods of \(A\), and define

\[
 \zeta_p(J)=\Pr(\text{the marks in }J\text{ have no isolated marked
 vertex}).                                           \tag{1.4}
\]

For \(D=S\setminus S'\), put

\[
 \begin{split}
 W_{p,S}(D)=\sum_{\substack{A\subseteq E(H(S))\text{ independent in }G_S\\
                            \bigcup_{F\in A}F=D}}
 &p^{|A|}(1-p)^{|N_{G_S}(A)|}\\
 &\cdot\zeta_p\!\left(G_S[E(H(S))\setminus N_{G_S}[A]]\right).
                                                               \tag{1.5}
 \end{split}
\]

Then, exactly,

\[
 \boxed{P_j(S,S')=
 \mathbf1_{\{S'\subseteq S\}}W_{p_j(S),S}(S\setminus S').}
                                                               \tag{1.6}
\]

Indeed the accepted set must be an independent set \(A\); all of \(A\)
is marked, its open neighbourhood is unmarked, and the remaining induced
conflict graph has no isolated marked vertex.  Formula (1.6) also sums
correctly when more than one accepted-edge family has the same vertex
union.

Conditioning the *whole history* on its exact-size schedule is effected by
the final global normalizer below.  Dividing each row of \(P_j\) by its
own exact-size probability would instead define an adaptively redrawn
process and is not the same operation.

## 2. Persistent carrier Palm kernels

Fix a prescribed root set \(R_\star\subseteq V\) (in the punctured
application, one chosen shore).  Let \({\cal C}\) be the set of all
labelled rooted ordered twelve-carriers

\[
 \gamma=(v;F_1,\ldots,F_{12}),
\]

where \(v\in R_\star\) and the \(F_i\) are distinct edges of \(H_0\)
containing \(v\).  Write
\(\gamma\preceq S\) when every vertex used by the carrier belongs to
\(S\), and define

\[
 t(S)=|\{\gamma\in{\cal C}:\gamma\preceq S\}|
     =\sum_{v\in R_\star}(d_{H(S)}(v))_{12}.       \tag{2.1}
\]

The reference Palm mass and law are

\[
 Z_j^0=\mathbb E_{\lambda_j}t(S),\qquad
 \pi_j(S,\gamma)={\lambda_j(S)\mathbf1_{\{\gamma\preceq S\}}
                         \over Z_j^0}.              \tag{2.2}
\]

On carrier states \(x=(S,\gamma)\), \(y=(S',\gamma')\), introduce the
raw persistent reference kernel

\[
 \overline U_j(x,y)=U_j(S,S')
        \mathbf1_{\{\gamma'=\gamma\}}\mathbf1_{\{\gamma\preceq S'\}}.
                                                               \tag{2.3}
\]

It is a killed kernel.  Its row mass is the exact slice probability that
the labelled carrier remains alive.  Nevertheless (1.3) gives the exact
global balance

\[
 \pi_j\overline U_j=c_j\pi_{j+1},\qquad
 c_j={Z_{j+1}^0\over Z_j^0}.                       \tag{2.4}
\]

Consequently

\[
 K_j={\overline U_j\over c_j},\qquad
                         \pi_jK_j=\pi_{j+1}.        \tag{2.5}
\]

The forward \(K_j\) need not have row mass one.  This is not a defect:
its reverse operator is Markov.  In fact it is the completely explicit
uniform-enlargement operator

\[
 K_j^\leftarrow g(S',\gamma)=
 \sum_{\substack{S\in\Omega_j\\S\supseteq S'}}
 {\lambda_j(S)U_j(S,S')\over\lambda_{j+1}(S')}
 g(S,\gamma),                                      \tag{2.5a}
\]

and the coefficient is the reciprocal of

\[
 \prod_\sigma {|V_\sigma|-n_{j+1,\sigma}
                    \choose n_{j\sigma}-n_{j+1,\sigma}}.      \tag{2.5b}
\]

All Palm normalizers cancel from the reverse kernel.  For every fixed
terminal time \(J\)

\[
 Q_J(dx_0\cdots dx_J)=\pi_0(dx_0)
                       \prod_{j<J}K_j(x_j,dx_{j+1})              \tag{2.6}
\]

is a probability measure with terminal marginal \(\pi_J\).
Equivalently, \(Q_J\) is obtained by running the ordinary nested uniform
residual chain to time \(J\), Palmizing at the terminal state, and tracing
the chosen terminal carrier label backwards.  It is therefore a legitimate
probability law for each fixed horizon.  Because the forward \(K_j\) are
generally not Markov, the family of terminal-Palmized history laws for
different horizons need not be projectively consistent; no such consistency
is used in the terminal conditional expectation.

The literal persistent-carrier kernel is

\[
 \overline P_j(x,y)=P_j(S,S')
        \mathbf1_{\{\gamma'=\gamma\}}\mathbf1_{\{\gamma\preceq S'\}}.
                                                               \tag{2.7}
\]

On its support it has density relative to \(K_j\)

\[
 \boxed{
 r_j(x,y)=c_j{P_j(S,S')\over U_j(S,S')}
          =c_jC_jW_{p_j(S),S}(S\setminus S').}     \tag{2.8}
\]

Zero actual probabilities simply give \(r_j=0\).  Let

\[
                              L_J=\prod_{j<J}r_j(X_j,X_{j+1}).  \tag{2.9}
\]

The factors \(c_j\) and \(C_j\) have been retained in (2.8); both are
essential in the raw identity, although endpoint-independent products
cancel after the final normalization.

For completeness, if
\(f_j=d\widehat\nu_j/d\pi_j\), the literal one-step Doob recursion is

\[
 \widetilde f_{j+1}(y)=
 K_j^\leftarrow\!\left[x\mapsto f_j(x)r_j(x,y)\right](y),
 \qquad
 f_{j+1}(y)={\widetilde f_{j+1}(y)\over m_j},       \tag{2.10}
\]

with the exact scalar normalizer

\[
                         m_j={\nu_{j+1}(t)\over\nu_j(t)}.       \tag{2.11}
\]

Here \(K_j^\leftarrow\) averages the displayed function of the predecessor
\(x\), while the terminal \(y\) in \(r_j(x,y)\) is held fixed.  This is
the non-factorized version of the recursion; pulling \(r_j\) outside the
reverse average would discard the conditional environment.

## 3. Exact terminal Radon--Nikodym identity

Assume the initial actual residual law is \(\lambda_0\), as it is when
the initial slice is the full target universe.  Define the unnormalized
actual residual measure

\[
                         \nu_J=\lambda_0P_0P_1\cdots P_{J-1}.   \tag{3.1}
\]

Its total mass \(\nu_J(1)\) is the probability of the exact-size/good
history.  Conditionalizing the residual law would divide by this number,
but that factor cancels again when the law is Palmized.  The actual
terminal Palm law is therefore exactly

\[
 \widehat\nu_J(S,\gamma)=
 {\nu_J(S)\mathbf1_{\{\gamma\preceq S\}}\over\nu_J(t)}.       \tag{3.2}
\]

### Theorem 3.1 (literal terminal Doob formula)

With the definitions above,

\[
 {d\{\pi_0\prod_{j<J}\overline P_j\}
       \over dQ_J}(x_0,\ldots,x_J)=L_J,             \tag{3.3}
\]

\[
 \mathbb E_{Q_J}L_J={\nu_J(t)\over Z_0^0},          \tag{3.4}
\]

and for every terminal carrier state \(y=(S,\gamma)\) with
\(\gamma\preceq S\),

\[
 \boxed{
 \mathbb E_{Q_J}[L_J\mid X_J=(S,\gamma)]
 ={Z_J^0\over Z_0^0}{\nu_J(S)\over\lambda_J(S)}.}  \tag{3.5}
\]

Consequently

\[
 \boxed{
 {d\widehat\nu_J\over d\pi_J}(S,\gamma)
 ={\mathbb E_{Q_J}[L_J\mid X_J=(S,\gamma)]
          \over\mathbb E_{Q_J}L_J}
 ={Z_J^0\nu_J(S)\over\lambda_J(S)\nu_J(t)}.}      \tag{3.6}
\]

Equivalently one may omit the endpoint-independent \(c_j\)'s altogether.
Under the same terminal-Palm reference history law \(Q_J\), set

\[
 L'_J=\prod_{j<J}{P_j(S_j,S_{j+1})\over U_j(S_j,S_{j+1})}.
                                                               \tag{3.6a}
\]

Then

\[
 \mathbb E_{Q_J}L'_J={\nu_J(t)\over Z_J^0},\qquad
 {d\widehat\nu_J\over d\pi_J}(y)
 ={\mathbb E_{Q_J}[L'_J\mid X_J=y]\over\mathbb E_{Q_J}L'_J}. \tag{3.6b}
\]

#### Proof

Equations (2.5), (2.7), and (2.8) give
\(r_jK_j=\overline P_j\), proving (3.3).  Induction in the residual
state gives

\[
 \left(\pi_0\prod_{j<J}\overline P_j\right)(S,\gamma)
 ={\nu_J(S)\mathbf1_{\{\gamma\preceq S\}}\over Z_0^0}.       \tag{3.7}
\]

Summing (3.7) proves (3.4).  The terminal marginal of \(Q_J\) is
\(\pi_J\); division of (3.7) by (2.2) proves (3.5).  Dividing once more
by (3.4) proves (3.6), which agrees directly with (2.2) and (3.2).
\(\square\)

Formula (3.6) is the exact content of the conditional expectation in
(G.63).  It exposes two facts which are easy to obscure:

* conditional on a fixed residual \(S\), the terminal density is
  independent of the carrier label \(\gamma\); Palmizing both laws
  multiplies them by the same alive-carrier indicator;
* the residual-state density \(\nu_J(S)/\lambda_J(S)\) remains in full.
  It is centered by its \(t\)-size-biased reference mean

  \[
   {\nu_J(t)\over Z_J^0}
   =\mathbb E_{\pi_J}{\nu_J(S)\over\lambda_J(S)},              \tag{3.8}
  \]

  not removed.

Thus the precise endpoint form of (G.63) is

\[
 \operatorname*{ess\,sup}_{S:t(S)>0}
 \log {\nu_J(S)/\lambda_J(S)\over\nu_J(t)/Z_J^0}.             \tag{3.9}
\]

For an initial density \(f_0=d\widehat\mu_0/d\pi_0\), simply replace
\(L_J\) by \(f_0(X_0)L_J\).  Killing at a stopping boundary is covered by
multiplying (1.6) by the appropriate transition indicator; all later
formulas use the resulting subkernel without change.

## 4. Survival versus conditional environment

For a carrier state \(x=(S,\gamma)\), set

\[
 a_j(x)=\sum_{S'\in\Omega_{j+1}}
 P_j(S,S')\mathbf1_{\{\gamma\preceq S'\}},\qquad
 s_j^0(\gamma)=\sum_{S'\in\Omega_{j+1}}
 U_j(S,S')\mathbf1_{\{\gamma\preceq S'\}}.        \tag{4.1}
\]

If \(b_\sigma(\gamma)=|V(\gamma)\cap V_\sigma|\), then

\[
 \boxed{s_j^0(\gamma)=
        \prod_\sigma{(n_{j+1,\sigma})_{b_\sigma(\gamma)}
                         \over(n_{j\sigma})_{b_\sigma(\gamma)}}.}       \tag{4.2}
\]

Conditional on retaining a distinguished root, replace each factor by

\[
 {(n_{j+1,\sigma}-r_\sigma)_{b_\sigma-r_\sigma}
       \over(n_{j\sigma}-r_\sigma)_{b_\sigma-r_\sigma}},
 \qquad r_\sigma=\mathbf1_{\{v\in V_\sigma\}}.     \tag{4.3}
\]

When the quantities in (4.1) are positive, define the two conditional
environment kernels

\[
 P_j^{\rm env}(x,S')={P_j(S,S')\mathbf1_{\{\gamma\preceq S'\}}
                              \over a_j(x)},\qquad
 U_j^{\rm env}(x,S')={U_j(S,S')\mathbf1_{\{\gamma\preceq S'\}}
                              \over s_j^0(\gamma)}.              \tag{4.4}
\]

Then (2.8) has the exact factorization

\[
 \boxed{
 r_j(x,y)=c_j\,{a_j(x)\over s_j^0(\gamma)}
                  \exp\{\chi_j(x,S')\},}           \tag{4.5}
\]

where the signed conditional-environment statistic is

\[
 \boxed{
\chi_j(x,S')=
 \log{P_j^{\rm env}(x,S')\over U_j^{\rm env}(x,S')}
 =\log W_{p_j(S),S}(S\setminus S')+\log C_j
       +\log s_j^0(\gamma)-\log a_j(x).}            \tag{4.6}
\]

Since \(U_j\) is constant on a nested exact-slice fibre, this can be
written even more transparently as

\[
 \boxed{\chi_j(x,S')=
 \log W_{p_j(S),S}(S\setminus S')
 -\log\mathbb E_{U_j^{\rm env}(x,\cdot)}
             W_{p_j(S),S}(S\setminus S'').}         \tag{4.6a}
\]

It is normalized, rather than zero:

\[
 \mathbb E_{U_j^{\rm env}}e^{\chi_j}=1,
 \qquad
 \mathbb E_{U_j^{\rm env}}\chi_j
   =-D_{\rm KL}(U_j^{\rm env}\Vert P_j^{\rm env})\le0,
 \qquad
 \mathbb E_{P_j^{\rm env}}\chi_j
   =D_{\rm KL}(P_j^{\rm env}\Vert U_j^{\rm env})\ge0,         \tag{4.7}
\]

with the usual extended-value convention when supports differ.

The first factor after \(c_j\) is the exact carrier-survival/exact-size
factor.  Its small-bite tangent contains the first-blocker, marginal, and
coordinate-overlap terms.  The last factor is the law of the *rest of the
residual conditional on that survival*.  Terminal conditioning in (3.5)
averages products of both factors over all predecessor histories; it does
not average \(e^{\chi_j}\) under the one-step forward reference law, so
the first identity in (4.7) supplies no cancellation in (3.5).

Using (1.6), all of the environment dependence is explicit through the
accepted-family multiplicity, its conflict neighbourhood, and the
\(\zeta_p\) no-further-isolated-mark factor.  No unnamed probability
factor remains.

## 5. What symmetry does and does not do

Let a group \({\cal G}\) act on \(V\), preserve shores and \(H_0\), and
suppose the marking rate and stopping rule are equivariant.  Then

\[
 W_{p,gS}(gD)=W_{p,S}(D),\qquad
 \chi_j(gS,g\gamma,gS')=\chi_j(S,\gamma,S').       \tag{5.1}
\]

Thus symmetry makes the environment statistic constant on
\({\cal G}\)-orbits of transitions.  It makes it constant on the entire
conditional slice only under the much stronger assertion that those
transitions form one orbit and have common accepted-family weights.
Vertex-, edge-, root-, or carrier-transitivity does not imply this.
Precisely, \(\chi_j\equiv0\) on a conditional fibre if and only if the
weight \(W_{p_j(S),S}(S\setminus S')\) is constant there, equivalently
\(P_j^{\rm env}=U_j^{\rm env}\).  Transitivity of the stabilizer of
\((S,\gamma)\) on that entire fibre is one sufficient condition, but the
usual global transitivity hypotheses are much weaker.

### Proposition 5.1 (transitive one-bite obstruction)

For \(m\ge5\), let

\[
 H_m=C_m\mathbin\square C_m\mathbin\square\cdots
          \mathbin\square C_m\quad(6\text{ factors}).          \tag{5.2}
\]

Take \(R_\star=V(H_m)\).

This graph has \(N=m^6\) vertices, is 12-regular, and is vertex- and
edge-transitive.  Regard it as a 2-uniform hypergraph with one shore.
Start from the full vertex set and take one isolated-edge bite with
\(0<p<1\).  Condition
on the exact next size \(N-2\).  Then the actual deleted pair is uniform
over the \(6N\) graph edges, whereas the nested exact-slice reference
deletes a uniform pair.  Hence the residual-state density is

\[
 {d\mu^{\rm act}\over d\lambda_1}(V\setminus D)
 =\begin{cases}
   (N-1)/12,&D\in E(H_m),\\
   0,&D\notin E(H_m).
  \end{cases}                                      \tag{5.3}
\]

Every root has exactly twelve incident carrier edges.  For the full-star
twelve-carrier Palm laws,

\[
 \left\|{d\widehat\mu^{\rm act}\over d\pi_1}\right\|_\infty
 \ge {N-1\over12}{N-26\over N}.                   \tag{5.4}
\]

In particular the terminal Palm likelihood is unbounded as \(m\to\infty\)
despite full vertex- and edge-transitivity.

#### Proof

In a graph, accepted edges are a matching and delete two vertices each.
Thus exact next size \(N-2\) is precisely the event that the accepted set
has size one.  Edge-transitivity makes each singleton accepted set equally
likely, proving (5.3).

For \(S=V\setminus D\), a root contributes \(12!\) to \(t(S)\) exactly
when it lies outside the union of the two deleted closed neighbourhoods.
That union has size at most \(2(12+1)=26\).  Consequently

\[
                         (N-26)12!\le t(S)\le N12!.             \tag{5.5}
\]

Palmizing (5.3) multiplies its nonzero value by
\(\mathbb E_{\lambda_1}t/\mathbb E_{\mu^{\rm act}}t\).  Bound the numerator
below and the denominator above using (5.5) to obtain (5.4).
\(\square\)

The obstruction can be localized entirely in the conditional environment.
Fix a full-star carrier \(\gamma\), whose vertex footprint has size 13.
Given exact size \(N-2\), its actual survival probability and its uniform
slice survival probability are both \(1-O(1/N)\).  Conditional on survival,
however, the reference deletion is uniform over all
\({N-13\choose2}\) pairs outside the footprint, while the actual deletion
is supported only on graph edges outside it.  Therefore on every such edge

\[
 e^{\chi}\ge{{N-13\choose2}\over6N}
             ={N\over12}+O(1),                    \tag{5.6}
\]

and \(e^\chi=0\) on the nonedges.  The survival factor tends to one; the
environment factor alone has order \(N\).

The same support mechanism occurs in the directed punctured catalogue at
a one-accepted-configuration reveal.  With \(b=2r+1\), there are \(b!\)
distinct directed configurations, each deleting \(2r\) middle and \(2r\)
lower targets.  The corresponding uniform exact slice has

\[
 {N_M\choose2r}{N_L\choose2r},\qquad
 N_M={2r+1\choose r},\quad N_L={2r+1\choose r-1},               \tag{5.7}
\]

possible deletion pairs.  Conditional on exactly one accepted
configuration, the actual support has at most \(b!\) elements.  Its
reference mass is therefore at most

\[
 {b!\over {N_M\choose2r}{N_L\choose2r}}=e^{-\Omega(r^2)}.      \tag{5.8}
\]

Catalogue transitivity makes the supported atoms equiprobable; it does not
turn their union into a uniform exact slice.  This is a sequential
one-configuration obstruction, not a theorem that a whole-round statistic
cannot regenerate.

## 6. The exact weaker functional gate

Full Palm \(L^\infty\) domination is stronger than Gate A needs.  For
\(c\ge11\) (in the punctured application \(c\ge12\)), define

\[
 F_c(S)=\sum_{v\in R_\star}(d_{H(S)}(v)-c)_+^{12},\qquad
 h_J(S)={\nu_J(S)\over\lambda_J(S)},               \tag{6.1}
\]

and let \(\mu_J=\nu_J/\nu_J(1)\) be the actual residual law conditional on
the exact-size/good history.  For the positive carrier test

\[
 \psi_c(S,\gamma)={(d_{H(S)}(v)-c)_+^{12}
                           \over(d_{H(S)}(v))_{12}},            \tag{6.2}
\]

with value zero below degree twelve, summing over alive carriers gives
\(\sum_{\gamma\preceq S}\psi_c(S,\gamma)=F_c(S)\).  Therefore the two
Palm expectations are exactly

\[
 \mathbb E_{\widehat\nu_J}\psi_c
 ={\mathbb E_{\lambda_J}[h_JF_c]
       \over\mathbb E_{\lambda_J}[h_Jt]},
 \qquad
 \mathbb E_{\pi_J}\psi_c
 ={\mathbb E_{\lambda_J}F_c\over\mathbb E_{\lambda_J}t}.       \tag{6.3}
\]

Thus the exact functional substitute for full \(L^\infty\) domination is

\[
 \boxed{
 {\mathbb E_{\lambda_J}[h_JF_c]
       \over\mathbb E_{\lambda_J}[h_Jt]}
 \le r^{\kappa+o(1)}
 {\mathbb E_{\lambda_J}F_c
       \over\mathbb E_{\lambda_J}t}.}             \tag{6.4}
\]

Equation (6.4) is **if and only if** the required comparison for this one
terminal Palm test \(\psi_c\).  It retains the exact-history conditioning:
\(\mathbb E_{\lambda_J}h_J=\nu_J(1)\),
\(\mathbb E_{\lambda_J}[h_Jt]=\nu_J(t)\), and the former normalizer cancels
from the quotient.
The stopped functional gate requires (6.4) uniformly for the prescribed
\(c\), every density bin, and every \(J\le\tau_{\rm stop}\); it does not
require domination for unrelated terminal tests.

The relation to the original tail moment has one additional, explicit
carrier-mass factor.  If

\[
 n=|R_\star|,\qquad z>0\text{ is the chosen root-set degree scale},\qquad
 U_{12,c}(S)={F_c(S)\over nz^{12}},                 \tag{6.5}
\]

then, whenever the reference tail expectation is nonzero,

\[
 \boxed{
 {\mathbb E_{\mu_J}U_{12,c}\over
       \mathbb E_{\lambda_J}U_{12,c}}
 ={\mathbb E_{\mu_J}t\over\mathbb E_{\lambda_J}t}
 \cdot
 {\mathbb E_{\lambda_J}[h_JF_c]/
       \mathbb E_{\lambda_J}[h_Jt]
  \over
  \mathbb E_{\lambda_J}F_c/
       \mathbb E_{\lambda_J}t}.}                  \tag{6.6}
\]

If the reference tail expectation is zero, the comparison is interpreted
directly: it holds exactly when the actual tail expectation is also zero.

This is the precise equivalence, including every normalizer.  Under the
already used density-bin hypotheses

\[
 t(S)\le n(Kz)^{12},\qquad
 \mathbb E_{\lambda_J}t\ge a\,nz^{12},             \tag{6.7}
\]

the first factor in (6.6) is at most \(K^{12}/a\).  Hence (6.4) implies

\[
 \boxed{
 \mathbb E_{\mu_J}U_{12,c}
 \le {K^{12}\over a}\,r^{\kappa+o(1)}
                 \mathbb E_{\lambda_J}U_{12,c}.}  \tag{6.8}
\]

Conversely, a raw \(U_{12,c}\) comparison implies (6.4) only after the
reciprocal carrier-mass ratio in (6.6) is included.  Calling (6.4)
literally equivalent to the unnormalized \(U\)-comparison without this
factor would drop a normalization.

For comparison, the strong terminal Palm domination used in the current
twelve-carrier reduction is

\[
 \boxed{
 \sup_{J\le\tau_{\rm stop}}
 \operatorname*{ess\,sup}_{S:t(S)>0}
 \log{\nu_J(S)/\lambda_J(S)\over\nu_J(t)/Z_J^0}
 \le(\kappa+o(1))\log r.}                          \tag{6.9}
\]

Equations (2.8), (3.5), and (4.5) show that (6.9) is identical to the
terminal conditional-history formulation in (G.63).  It implies (6.4)
for every nonnegative terminal carrier test, but the converse is false.
The constants \(\prod_jc_j=Z_J^0/Z_0^0\), the uniform-transition constants
\(\prod_jC_j\), and the probability of the exact-size/good history all
cancel only in the displayed centered ratio.  The orbit-dependent product
of the explicit weights (1.5), equivalently the cumulative signed
statistics (4.6), does not cancel.

The transitive obstruction proves that exchangeability alone cannot prove
(6.9).  It also demonstrates why this strengthening can be irrelevant to
the target functional: in the 12-regular torus example, for
\(11\le c<12\), \(F_c(S)=(12-c)^{12}t(S)/12!\), so (6.4) holds with equality,
even though the Palm \(L^\infty\) norm in (5.4) diverges.  For \(c\ge12\),
both tail functionals vanish.  A punctured proof may therefore target
(6.4) directly, exploiting signed cancellation after testing against
\(F_c\), rather than prove the likely much harder full-state condition
(6.9).
