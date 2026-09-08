# Gate A: a uniform finite-bite carrier-survival remainder

**Date:** 2026-08-22  
**Status:** proved for the unconditioned isolated-edge kernel; the separate
random-clock mixture theorem avoids exact-size fibre conditioning, while the
cumulative signed drift and reference-relative erosion remain open

This note upgrades the infinitesimal carrier-hazard identity in Appendix G.5
of `MASTER_HANDOFF.md` to a finite isolated-edge bite.  The point is that the
terminal root degree may depend on accepted edges throughout the catalogue,
but this causes only favourable erosion.  The sign-indefinite
survival-selection term depends solely on the conflict neighbourhood of the
fixed carrier and therefore has a uniform quadratic remainder.

For fixed carrier order \(m\), the result is

\[
 \log {A_c(\nu P_p)\over A_c(\nu)}
 \le p\{m\mathcal Y_c(\nu)+\mathcal Q_c(\nu)\}
       +C_m(p\Delta_C)^2.                              \tag{0.1}
\]

Here \(P_p\) is one **unconditioned** Bernoulli isolated-edge bite,
\(\mathcal Y_c\) is the signed root external-exposure deficit, and
\(\mathcal Q_c\) is the already controlled duplicate-carrier term.  The
nonnegative statistic \(\mathcal X_c\) may replace \(\mathcal Y_c\).

Consequently the Taylor-safe schedule already imposed in the master handoff
makes the cumulative finite-bite error \(o(r^{-1-\alpha})\).  Thus, for the
unconditioned kernel, finite-bite accumulation is no longer an open analytic
remainder.  This does **not** prove (G.95).  If one conditions a round on its
exact shore decrement, the residual-environment likelihood (G.76)--(G.77)
is not controlled by the local argument below.  The separate theorem
`MATH_REDUCTION_GATE_A_UNCONDITIONED_RANDOM_CLOCK_MIXTURE_REFERENCE_20260822.md`
rigorously avoids that conditioning; on the revised route, the stopped
signed drift and reference-relative erosion/realized-center comparison are
still open.

## 1. Carrier notation

Let \(H\) be a finite simple hypergraph with edge set \(\mathcal E\), and let
\(V_\star\) be a prescribed root set.  Put

\[
 \Gamma(F)=\{G\in\mathcal E:G\cap F\ne\varnothing\},\qquad
 \Delta_C=\max_{F\in\mathcal E}|\Gamma(F)|,
\]
\[
 \mathcal S_v=\{F:v\in F\},\qquad d_v=|\mathcal S_v|.
                                                               \tag{1.1}
\]

Fix an integer \(m\ge2\).  An ordered carrier is
\(\gamma=(v;F_1,\ldots,F_m)\), where \(v\in V_\star\) and the
\(F_i\in\mathcal S_v\) are distinct.  Define

\[
 B(\gamma)=\bigcup_{i=1}^m\Gamma(F_i),\qquad
 h(\gamma)=|B(\gamma)|.                                  \tag{1.2}
\]

For a root with \(d_v>0\), use the quantities from Appendix G.5,

\[
 E_v={1\over d_v}\sum_{F\in\mathcal S_v}
              (|\Gamma(F)|-d_v),                            \tag{1.3}
\]

and let \(\overline D_m(v)\) be the average duplicate count

\[
 D(\gamma)=\sum_{i=1}^m
       |\Gamma(F_i)\setminus\mathcal S_v|
 -\left|\bigcup_{i=1}^m
       (\Gamma(F_i)\setminus\mathcal S_v)\right|.            \tag{1.4}
\]

The exact union identity is

\[
 \boxed{\mathbb E[h(\gamma)\mid H,v]
       =d_v+mE_v-\overline D_m(v).}                          \tag{1.5}
\]

Let \(\nu\) be any nonzero finite measure on hypergraph states of this
form, all on the same labelled universe and root set.  Adjoin every alive
ordered carrier with its counting multiplicity and normalize.  Denote the
resulting carrier-Palm law by \(\widehat\nu\).  All variables in (1.1)--(1.5)
are evaluated in the current state under this law.  It is enough that the
states in the support of \(\nu\) satisfy the common bound
\(\Delta_C(H)\le\Delta\).

For real \(c\ge m-1\), put

\[
 \varphi_c(d)=
 \begin{cases}
 (d-c)_+^m/(d)_m,&d\ge m,\\
 0,&d<m,
 \end{cases}
 \qquad
 A_c(\nu)=\mathbb E_{\widehat\nu}\varphi_c(d_v).             \tag{1.6}
\]

As proved in Appendix G.4, \(\varphi_c\) is nondecreasing.  Induced
deletion therefore causes only nonnegative erosion.

Define

\[
 \overline E=\mathbb E_{\widehat\nu}E_v,
\]
\[
 \mathcal Y_c(\nu)=
 {\mathbb E_{\widehat\nu}[(\overline E-E_v)
                         \varphi_c(d_v)]\over A_c(\nu)},
                                                               \tag{1.7}
\]
\[
 \mathcal X_c(\nu)=
 {\mathbb E_{\widehat\nu}[(\overline E-E_v)_+
                         \varphi_c(d_v)]\over A_c(\nu)},
                                                               \tag{1.8}
\]
\[
 \mathcal Q_c(\nu)=
 {\mathbb E_{\widehat\nu}[\overline D_m(v)
                         \varphi_c(d_v)]\over A_c(\nu)}.      \tag{1.9}
\]

These quantities are invoked only when \(A_c(\nu)>0\).  Clearly
\(\mathcal Y_c\le\mathcal X_c\).

## 2. Uniform carrier-survival expansion

Independently mark every edge with probability \(p\).  A marked edge is
accepted when no distinct conflicting edge is marked, all vertices of the
accepted edges are deleted, and the induced residual is retained.  Let
\(P_p\) denote this unconditioned kernel.  For a current carrier \(\gamma\),
write

\[
 a_p(\gamma)=\Pr(\gamma\hbox{ survives the bite}\mid H,\gamma).
                                                               \tag{2.1}
\]

### Lemma 2.1 (local quadratic remainder)

For every carrier,

\[
 \boxed{
 a_p(\gamma)=1-ph(\gamma)+r_p(\gamma),\qquad
 0\le r_p(\gamma)\le K_m(p\Delta)^2,}                       \tag{2.2}
\]

where one may take \(K_m=m^2/2+m\).

#### Proof

The carrier survives exactly when no accepted edge belongs to
\(B(\gamma)\).  If no member of \(B(\gamma)\) is marked, this certainly
happens.  Since \(b=|B(\gamma)|\le m\Delta\), Bernoulli's inequality and
Taylor's theorem give

\[
 0\le(1-p)^b-(1-pb)\le {b\choose2}p^2.                       \tag{2.3}
\]

The only additional way the carrier can survive is for a member \(G\) of
\(B(\gamma)\) to be marked but suppressed by a distinct marked conflict
neighbour.  A union bound over ordered pairs \((G,G')\), with
\(G\in B(\gamma)\) and
\(G'\in\Gamma(G)\setminus\{G\}\), bounds this probability by

\[
 p^2|B(\gamma)|\Delta\le mp^2\Delta^2.                       \tag{2.4}
\]

Combining (2.3)--(2.4) proves (2.2).  \(\square\)

The proof uses neither regularity nor punctured geometry.  Its usefulness
comes from applying it only to the sign-indefinite carrier-selection part;
attempting to localize the entire terminal degree would be false.

There is a parallel estimate for the nested uniform-slice reference.  Let a
shore of size \(n_\sigma\) be reduced uniformly to size
\(n' _\sigma\), put

\[
 \delta_\sigma=1-{n'_\sigma\over n_\sigma},
\]

and let \(b_{\gamma\sigma}\) be the number of distinct shore-\(\sigma\)
targets in the union of the carrier configurations.  Define

\[
 g(\gamma)=\sum_\sigma\delta_\sigma b_{\gamma\sigma},\qquad
 \eta=\sup_\gamma g(\gamma),
\]
\[
 \rho=\sup_\gamma\sum_\sigma
              {\delta_\sigma b_{\gamma\sigma}^2\over n_\sigma}. \tag{2.5}
\]

### Lemma 2.2 (uniform-slice survival remainder)

Suppose \(b_{\gamma\sigma}\le n_\sigma/2\) and
\(\delta_\sigma\le1/4\) for every carrier and shore.  The exact uniform
carrier-survival probability

\[
 a^0(\gamma)=\prod_\sigma
 { (n'_\sigma)_{b_{\gamma\sigma}}
       \over (n_\sigma)_{b_{\gamma\sigma}}}                 \tag{2.6}
\]

satisfies

\[
 \boxed{a^0(\gamma)=1-g(\gamma)+r^0(\gamma),\qquad
 |r^0(\gamma)|\le C(\eta^2+\rho),}                          \tag{2.7}
\]

provided \(\eta\) is bounded by a sufficiently small absolute constant.

#### Proof

For \(0\le i<b_{\gamma\sigma}\), write

\[
 {n'_\sigma-i\over n_\sigma-i}
 =1-x_{\sigma i},\qquad
 x_{\sigma i}={\delta_\sigma n_\sigma\over n_\sigma-i}.
\]

The hypotheses give

\[
 \sum_{\sigma,i}x_{\sigma i}
 =g(\gamma)+O\!\left(\sum_\sigma
       {\delta_\sigma b_{\gamma\sigma}^2\over n_\sigma}\right).
                                                               \tag{2.8}
\]

For nonnegative \(x_i\) of sufficiently small total mass,
\(\prod_i(1-x_i)=1-\sum_i x_i+O((\sum_i x_i)^2)\).
Equations (2.6)--(2.8) prove (2.7).  \(\square\)

## 3. Finite-bite scalar theorem

### Theorem 3.1

For every fixed \(m\ge2\), there are constants
\(\theta_m,C_m>0\) such that the following holds.  Suppose

\[
 A_c(\nu)>0,\qquad p\Delta\le\theta_m.                       \tag{3.1}
\]

Then

\[
 \boxed{
 \log {A_c(\nu P_p)\over A_c(\nu)}
 \le p\{m\mathcal Y_c(\nu)+\mathcal Q_c(\nu)\}
       +C_m(p\Delta)^2}                                     \tag{3.2}
\]

and hence also

\[
 \boxed{
 \log {A_c(\nu P_p)\over A_c(\nu)}
 \le p\{m\mathcal X_c(\nu)+\mathcal Q_c(\nu)\}
       +C_m(p\Delta)^2.}                                    \tag{3.3}
\]

The conclusion remains valid for an unnormalized \(\nu\), since its total
mass cancels in both Palm scalars.

#### Proof

Every terminal ordered carrier has a unique labelled parent.  Summing over
parents gives

\[
 {A_c(\nu P_p)-A_c(\nu)}
 ={\operatorname {Cov}_{\widehat\nu}
          (a_p,\varphi_c)-\mathbb E_{\widehat\nu}e_c
     \over\mathbb E_{\widehat\nu}a_p},                      \tag{3.4}
\]

where \(e_c\ge0\) is the exact erosion from Appendix G.4.  Equivalently,
one may obtain the needed upper bound directly by replacing the terminal
test of every surviving carrier by its no-larger current value.

Write \(a_p=1-ph+r_p\), and put \(R=K_m(p\Delta)^2\).  Lemma 2.1 gives
\(0\le r_p\le R\), while \(0\le h\le m\Delta\).  Therefore

\[
 |\operatorname {Cov}(r_p,\varphi_c)|
 \le2R A_c(\nu),                                             \tag{3.5}
\]

and

\[
 \mathbb E a_p=1+O_m(p\Delta).                               \tag{3.6}
\]

Choose \(\theta_m\) so that the last expectation is at least \(1/2\).
Since

\[
 {|\operatorname {Cov}(h,\varphi_c)|\over A_c(\nu)}
 \le2m\Delta,                                                \tag{3.7}
\]

replacing \((\mathbb E a_p)^{-1}\) by one in (3.4) costs only
\(O_m((p\Delta)^2)\).  Dropping erosion and using
\(\log x\le x-1\) now gives

\[
 \log {A_c(\nu P_p)\over A_c(\nu)}
 \le-p{\operatorname {Cov}_{\widehat\nu}
                    (h,\varphi_c)\over A_c(\nu)}
       +C_m(p\Delta)^2.                                     \tag{3.8}
\]

Because \(\varphi_c(d_v)\) is root-measurable, conditioning (1.5) on the
current state and root yields

\[
\begin{aligned}
 -\operatorname {Cov}(h,\varphi_c)
={}&-\operatorname {Cov}(d_v,\varphi_c)
    -m\operatorname {Cov}(E_v,\varphi_c)\\
 &+\operatorname {Cov}(\overline D_m(v),\varphi_c).           \tag{3.9}
\end{aligned}
\]

The first covariance is nonnegative because both factors are
nondecreasing functions of \(d_v\).  Furthermore

\[
 -{\operatorname {Cov}(E_v,\varphi_c)\over A_c}=\mathcal Y_c,
 \qquad
 {\operatorname {Cov}(\overline D_m,\varphi_c)\over A_c}
 \le\mathcal Q_c.                                            \tag{3.10}
\]

Substitution in (3.8) proves (3.2), and
\(\mathcal Y_c\le\mathcal X_c\) proves (3.3).  \(\square\)

### Corollary 3.2 (cumulative unconditioned form)

Let \(\nu_{j+1}=\nu_jP_{p_j}\), and suppose every state in the support of
\(\nu_j\) has conflict degree at most \(\Delta_j\).  For a fixed terminal
\(c\), assume \(A_c(\nu_j)>0\) and
\(p_j\Delta_j\le\theta_m\) for \(j<J\).  Then

\[
 \boxed{
 \log{A_c(\nu_J)\over A_c(\nu_0)}
 \le\sum_{j<J}p_j\{m\mathcal Y_{j,c}+\mathcal Q_{j,c}\}
       +C_m\sum_{j<J}(p_j\Delta_j)^2.}                       \tag{3.11}
\]

The same statement holds with every \(\mathcal Y\) replaced by
\(\mathcal X\).  This is just the sum of (3.2) at a fixed \(c\); it is not
a changing-threshold telescope.

### Corollary 3.3 (finite uniform-slice drift)

Let \(\lambda\) be uniform on a current exact slice and \(U\) the nested
uniform-slice kernel described in Lemma 2.2.  If
\(A_c(\lambda)>0\) and \(\eta\) is sufficiently small, then

\[
 \boxed{
 \log{A_c(\lambda U)\over A_c(\lambda)}
 \le-{\operatorname {Cov}_{\widehat\lambda}
                   (g,\varphi_c)\over A_c(\lambda)}
       +C_m(\eta^2+\rho).}                                  \tag{3.12}
\]

Indeed, the exact Palm recursion (3.4) applies with \(a^0\) in place of
\(a_p\); Lemma 2.2, favourable erosion, and the proof of Theorem 3.1 apply
verbatim.  This also makes the coordinate-overlap correction explicit.  If
each carrier member has \(k_\sigma\) targets on shore \(\sigma\), write

\[
 O_\sigma(\gamma)=mk_\sigma-b_{\gamma\sigma}.
\]

The constant part of \(g=\sum_\sigma\delta_\sigma
(mk_\sigma-O_\sigma)\) has zero covariance, and hence

\[
 -\operatorname {Cov}(g,\varphi_c)
 =\sum_\sigma\delta_\sigma
       \operatorname {Cov}(O_\sigma,\varphi_c).              \tag{3.13}
\]

Thus both the unconditioned actual bite and the uniform reference have
summable quadratic remainders.  What is not supplied is permission to
replace the actual exact-size conditional kernel by the unconditioned one.
The random-clock mixture theorem does not make that replacement: it keeps
the actual bite unconditioned from the start and constructs a mixture of
uniform slices as the nested reference.

There is an exact erosion-inclusive quotient which identifies what the
revised route must still compare.  For a current carrier state
\(x=(H,\gamma)\) with \(\varphi_c(d_v)>0\), define

\[
 \beta_c(x)={1\over\varphi_c(d_v)}
 \sum_{H'}P(x,H')\mathbf1_{\{\gamma\ {\rm survives}\}}
                    \varphi_c(d_{H'}(v)),                    \tag{3.13a}
\]

and set it to zero when \(\varphi_c(d_v)=0\).  Thus

\[
                         0\le\beta_c(x)\le a(x),             \tag{3.13b}
\]

and the exact erosion satisfies
\(e_c(x)=\varphi_c(d_v)\{a(x)-\beta_c(x)\}\) on the positive
tail.  Let \(\tau_c^\nu\) be the tail-tilted carrier law

\[
 {d\tau_c^\nu\over d\widehat\nu}(x)
 ={\varphi_c(d_v)\over A_c(\nu)}.                            \tag{3.13c}
\]

The Palm recursion then rearranges exactly to

\[
 \boxed{
 {A_c(\nu P)\over A_c(\nu)}
 ={\mathbb E_{\tau_c^\nu}\beta_c
       \over\mathbb E_{\widehat\nu}a}.}                     \tag{3.13d}
\]

For any reference pair \((\lambda,U)\), with corresponding
\(a^0,\beta_c^0,\tau_c^\lambda\), division gives

\[
 \boxed{
 \log {A_c(\nu P)/A_c(\lambda U)
             \over A_c(\nu)/A_c(\lambda)}
 =\log{\mathbb E_{\tau_c^\nu}\beta_c
             \over\mathbb E_{\widehat\nu}a}
  -\log{\mathbb E_{\tau_c^\lambda}\beta_c^0
             \over\mathbb E_{\widehat\lambda}a^0}.}        \tag{3.13e}
\]

Zero terminal-tail factors are interpreted in the extended sense.  Formula
(3.13e) contains no rare-tail normalization: tilting cancels \(A_c\)
exactly.  For the random-clock mixture route, the remaining
reference-relative erosion statement is precisely a one-sided comparison
of the two bounded survival-payoff quotients in (3.13e), not a comparison
of full residual-state densities.

### Lemma 3.4 (one-dimensional regression inversion)

Let \(D\) have the root-degree marginal of \(\widehat\nu\), and let
\(q(d)\) be any real function on its support.  For the nondecreasing
\(\varphi_c\), define the weighted downward-inversion statistic

\[
 \mathfrak J_c(q)= {1\over A_c}
 \sum_{d<e}\Pr(D=d)\Pr(D=e)
       (q(d)-q(e))_+\{\varphi_c(e)-\varphi_c(d)\},            \tag{3.14}
\]

and its uniform majorant

\[
 \mathfrak I_c(q)=
 \sup_{\substack{d<e\\
              \Pr(D=d)\Pr(D=e)>0\\
              \varphi_c(d)<\varphi_c(e)}}
       (q(d)-q(e))_+,                                        \tag{3.15}
\]

with an empty supremum equal to zero.  Then

\[
 \boxed{
 -{\operatorname {Cov}(q(D),\varphi_c(D))\over A_c}
 \le\mathfrak J_c(q)\le\mathfrak I_c(q).}                   \tag{3.16}
\]

#### Proof

For two independent copies of \(D\), grouping unordered degree pairs gives

\[
 \operatorname {Cov}(q(D),\varphi_c(D))
 =\sum_{d<e}\Pr(D=d)\Pr(D=e)
   \{q(e)-q(d)\}\{\varphi_c(e)-\varphi_c(d)\}.              \tag{3.17}
\]

Discard the terms with the favourable sign to obtain the first inequality.
For the second, the sum of the remaining \(\varphi_c\)-increments is at
most

\[
 \sum_{d<e}\Pr(D=d)\Pr(D=e)\varphi_c(e)
 \le\sum_e\Pr(D=e)\varphi_c(e)=A_c.                         \tag{3.18}
\]

This proves (3.16).  \(\square\)

This lemma removes the rare-tail factor completely.  Define the
degree-conditioned mean carrier-union hazard

\[
 \zeta_m(d)=\mathbb E_{\widehat\nu}[h(\gamma)\mid d_v=d].    \tag{3.19}
\]

By (1.5), if

\[
 \eta(d)=\mathbb E_{\widehat\nu}[E_v\mid d_v=d],\qquad
 \delta_m(d)=\mathbb E_{\widehat\nu}
                   [\overline D_m(v)\mid d_v=d],             \tag{3.20}
\]

then exactly

\[
 \boxed{\zeta_m(d)=d+m\eta(d)-\delta_m(d).}                 \tag{3.21}
\]

There is an equivalent avoidance form with an especially direct
boundary-polymer interpretation.  For a deterministic state \(H\), a root
with \(d_v\ge m\), and \(a_G(v)\) from Appendix G.5, put

\[
 \mathcal R_m(v)=
 \sum_{G\not\ni v}{(d_v-a_G(v))_m\over(d_v)_m}.              \tag{3.21a}
\]

The summand is exactly the probability that a uniform ordered
\(m\)-carrier in the star of \(v\) avoids \(G\).  Substitution of the exact
duplicate formula (G.104) into (3.21) gives

\[
 \boxed{
 \mathbb E[h(\gamma)\mid H,v]=|E(H)|-\mathcal R_m(v).}       \tag{3.21b}
\]

Indeed the \(ma_G(v)/d_v\) terms in \(mE_v\) cancel those in
\(\overline D_m(v)\), leaving one for every external \(G\), together with
the \(d_v\) star edges.  Thus the regression gate can equivalently be read
as follows: after conditioning on root degree, a larger-degree root must not
have substantially **more** configurations avoided by a random carrier.
Unlike \(E_v\) and \(\overline D_m\) separately, (3.21a) retains their exact
union cancellation and is directly expressed through bounded-family
avoidance probabilities.

Since \(\varphi_c\) depends only on \(d_v\), conditioning before taking
the covariance in (3.8), followed by Lemma 3.4, proves the sharper
self-normalized finite-bite estimate

\[
 \boxed{
 \log {A_c(\nu P_p)\over A_c(\nu)}
 \le p\mathfrak J_c(\zeta_m)+C_m(p\Delta)^2
 \le p\mathfrak I_c(\zeta_m)+C_m(p\Delta)^2.}                \tag{3.22}
\]

Thus exact monotonicity of mean carrier hazard with root degree makes the
entire survival-selection term favourable.  More generally, an
\(o(z)\) downward regression defect makes its cumulative contribution
\(o(\log r)\) on the punctured density clock.  This formulation retains
the cancellation among the favourable root hazard, the external exposure,
and duplicate overlap; splitting those three terms as in (3.2) can be much
weaker.

There is also an external-only version.  Applying Lemma 3.4 to \(\eta\)
gives

\[
 \boxed{\mathcal Y_c(\nu)\le
        \mathfrak J_c(\eta)\le\mathfrak I_c(\eta).}          \tag{3.23}
\]

In particular, the exact signed external deficit depends only on the
one-dimensional regression \(d\mapsto\mathbb E[E_v\mid d_v=d]\);
fluctuations of \(E_v\) among roots of the same degree cancel identically.
The remaining punctured-specific question may therefore be posed as
approximate monotonicity of (3.19), rather than concentration of every
root exposure.

For a shore-uniform residual this regression has a concrete companion
form.  Put \(b_u=d_u-z_{\operatorname{sh}(u)}\),
\(a_0=\sum_\tau k_\tau z_\tau\), and let

\[
 R_v={1\over d_v}\sum_{F\ni v}
          \sum_{u\in F-\{v\}}b_u,qquad
 J_v={1\over d_v}\sum_{F\ni v}\mathfrak E(F),               \tag{3.23a}
\]

where
\(\mathfrak E(F)=\sum_{G\in\Gamma(F)}(|F\cap G|-1)\).
The exact conflict identity gives, for \(v\in V_\sigma\),

\[
 \boxed{E_v=a_0-z_\sigma+R_v-J_v.}                          \tag{3.23b}
\]

Hence the downward inversions in (3.23) are exactly those of
\(d\mapsto\mathbb E[R_v-J_v\mid d_v=d]\).  The large common exposure
scale \(\Theta(rz)\) cancels before any estimate: the desired \(O(z)\)
regression theorem is a statement about companion-degree and duplicate
*variation*, not their absolute sizes.

The argument also permits a predictable state-dependent marking rate.  If
the current state is \(H\), mark with probability \(p(H)\), and assume

\[
                         \theta=\sup_Hp(H)\Delta_C(H)\le\theta_m. \tag{3.24}
\]

Set

\[
 s(H,\gamma)=p(H)h(H,\gamma),\qquad
 \zeta_s(d)=\mathbb E_{\widehat\nu}[s(H,\gamma)\mid d_v=d].   \tag{3.25}
\]

Applying Lemma 2.1 conditionally on \(H\) gives uniformly
\(a=1-s+r\), \(|r|\le K_m\theta^2\).  The proof of (3.8) and Lemma 3.4
therefore give

\[
 \boxed{
 \log {A_c(\nu P_{p(\cdot)})\over A_c(\nu)}
 \le\mathfrak J_c(\zeta_s)+C_m\theta^2
 \le\mathfrak I_c(\zeta_s)+C_m\theta^2.}                    \tag{3.26}
\]

This version is the one compatible with an unconditioned random density
clock, where the marking probability is chosen from the current edge count
or average degree.

## 4. Punctured scale and the part this closes

In a two-shore punctured residual, every edge contains \(4r\) targets.  If
the shore degrees are capped by \(Kz_\sigma\) and their average scales are
within a fixed ratio, then deterministically

\[
 \Delta_C\le\max_F\sum_{u\in F}d(u)\le C_{K,R_0}rz_M.        \tag{4.1}
\]

For a Taylor-safe microbite

\[
 p_j\le {C\epsilon_j\over rz_{M,j}},                         \tag{4.2}
\]

equation (4.1) gives \(p_j\Delta_j=O(\epsilon_j)\).  If a schedule uses
\(O(r\log r/\epsilon)\) equal microbites, then

\[
 \sum_j(p_j\Delta_j)^2=O(\epsilon r\log r).                  \tag{4.3}
\]

Thus the shore-safe choice already recorded in (G.35),

\[
 \epsilon=o(r^{-2-\alpha}/\log r),                           \tag{4.4}
\]

makes the cumulative remainder in (3.11)

\[
 o(r^{-1-\alpha})=o(x_*/r),\qquad x_*=r^{-\alpha}.           \tag{4.5}
\]

For \(m=12\), under the cap/high-tail hypotheses (G.111), Appendix G.5
also gives

\[
 \mathcal Q_{j,c}
 \le C_{\delta,K,a_0}
 {\mathfrak D_{z_j}(H_j)\over n_jz_j^6A_c(H_j)}.             \tag{4.6}
\]

Accordingly (3.11) is a literal finite-bite version of (G.114): after
splitting off the sixth defect, the only sign-indefinite first-order term is
the stopped sum

\[
                         \sum_jp_j\mathcal Y_{j,c},           \tag{4.7}
\]

or, more strongly, \(\sum_jp_j\mathcal X_{j,c}\).
Without splitting, the sharper remaining statistic is
\(\sum_jp_j\mathfrak J_c(\zeta_{12,j})\), by (3.22).

## 5. An exact \(L^2\) compression of the external-exposure deficit

The remaining statistic can itself be bounded by two familiar global
variances.  The resulting estimate is useful diagnostically but is not
strong enough at the rare-tail scale.

Fix one shore \(V_\sigma\) of size \(n\), suppose every edge contains
exactly \(k\) targets from that shore, and write

\[
 Z=|\mathcal E|,\qquad z={kZ\over n},\qquad
 \overline C={1\over Z}\sum_{F\in\mathcal E}|\Gamma(F)|.     \tag{5.1}
\]

For \(d_v>0\), put

\[
 A_v={1\over d_v}\sum_{F\ni v}|\Gamma(F)|,qquad
 E_v=A_v-d_v,qquad B=\overline C-z.                         \tag{5.2}
\]

Let

\[
 V_C={\operatorname {Var}_{F\in\mathcal E}|\Gamma(F)|\over z^2},
 \qquad
 U_2={1\over nz^2}\sum_{v\in V_\sigma}(d_v-z)^2.            \tag{5.3}
\]

Also write
\(U_6=(nz^6)^{-1}\sum_v(d_v-z)^6\).

### Lemma 5.1 (incidence Jensen bridge)

Suppose

\[
 d_v\le Kz\quad(v\in V_\sigma),\qquad
 T_m=\sum_v(d_v)_m\ge a_0nz^m.                              \tag{5.4}
\]

Then under the ordered-\(m\)-carrier Palm root law,

\[
 \boxed{
 \operatorname {Var}_{\widehat P}(E_v)
 \le {2K^{m-1}\over a_0}z^2\{V_C+KU_2\}.}                  \tag{5.5}
\]

Consequently, whenever \(A_c>0\),

\[
 \boxed{
 \mathcal Y_c\le\mathcal X_c
 \le z\left{{2K^{m-1}\over a_0A_c}
                 (V_C+KU_2)\right\}^{1/2}.}                 \tag{5.6}
\]

One may replace \(U_2\) by \(U_6^{1/3}\).

#### Proof

Introduce the incidence-root law

\[
                         \rho(v)={d_v\over nz}.              \tag{5.7}
\]

Jensen inside each root star and then double counting incidences give

\[
\begin{aligned}
 \mathbb E_\rho(A_v-\overline C)^2
 &={1\over nz}\sum_vd_v
   \left({1\over d_v}\sum_{F\ni v}(C_F-\overline C)\right)^2\\
 &\le {1\over nz}\sum_v\sum_{F\ni v}(C_F-\overline C)^2
  ={1\over Z}\sum_F(C_F-\overline C)^2.                    \tag{5.8}
\end{aligned}
\]

Also

\[
 \mathbb E_\rho(d_v-z)^2
 ={1\over nz}\sum_vd_v(d_v-z)^2\le Kz^2U_2.                \tag{5.9}
\]

Since

\[
 E_v-B=(A_v-\overline C)-(d_v-z),                            \tag{5.10}
\]

equations (5.8)--(5.9) bound its squared \(\rho\)-mean by
\(2z^2(V_C+KU_2)\).

The density of the carrier-Palm root law relative to \(\rho\) is

\[
 { (d_v)_m/T_m\over d_v/(nz)}
 ={nz(d_v-1)_{m-1}\over T_m}
 \le {K^{m-1}\over a_0}.                                   \tag{5.11}
\]

Thus (5.5) follows from
\(\operatorname {Var}_{\widehat P}E_v
 \le\mathbb E_{\widehat P}(E_v-B)^2\).
Finally, Cauchy--Schwarz and \(0\le\varphi_c\le1\) yield

\[
 \mathbb E_{\widehat P}[(\overline E-E_v)_+\varphi_c]
 \le\sqrt{\operatorname {Var}_{\widehat P}(E_v)
            \mathbb E_{\widehat P}\varphi_c^2}
 \le\sqrt{\operatorname {Var}_{\widehat P}(E_v)A_c}.       \tag{5.12}
\]

Division by \(A_c\) proves (5.6), and Lyapunov gives
\(U_2\le U_6^{1/3}\).  \(\square\)

There is a genuinely self-normalized tail-local refinement.  For a
deterministic current state, put

\[
 F_c=\sum_{v\in V_\sigma}f_c(d_v),
\]

and, when \(F_c>0\), define

\[
 V^{\rm tail}_{C,c}={1\over z^2F_c}
 \sum_v{f_c(d_v)\over d_v}
       \sum_{F\ni v}(C_F-\overline C)^2,                    \tag{5.13}
\]

\[
 U^{\rm tail}_{2,c}={1\over z^2F_c}
       \sum_vf_c(d_v)(d_v-z)^2.                              \tag{5.14}
\]

Only roots with \(f_c(d_v)>0\) occur, so the divisions by \(d_v\) are
legitimate.

### Lemma 5.2 (tail-local self-normalization)

Under (5.4), let \(\overline E=\mathbb E_{\widehat P}E_v\).  Then

\[
\boxed{
 {\mathbb E_{\widehat P}[(E_v-\overline E)^2
                          \varphi_c(d_v)]\over A_c}
 \le4z^2\left\{V^{\rm tail}_{C,c}+U^{\rm tail}_{2,c}
 +{K^{m-1}\over a_0}(V_C+KU_2)\right\}.}                   \tag{5.15}
\]

Consequently

\[
\boxed{
 \mathcal X_c\le2z\left\{V^{\rm tail}_{C,c}
       +U^{\rm tail}_{2,c}
       +{K^{m-1}\over a_0}(V_C+KU_2)\right\}^{1/2}.}        \tag{5.16}
\]

There is no \(A_c^{-1/2}\) factor.

#### Proof

Tilting the carrier-Palm root law by \(\varphi_c/A_c\) cancels the falling
factorial exactly: the resulting tail law \(\tau_c\) has root mass

\[
                         \tau_c(v)={f_c(d_v)\over F_c}.       \tag{5.17}
\]

Jensen in the star of each tail root gives

\[
 \mathbb E_{\tau_c}(A_v-\overline C)^2
 \le {1\over F_c}\sum_v{f_c(d_v)\over d_v}
       \sum_{F\ni v}(C_F-\overline C)^2
 =z^2V^{\rm tail}_{C,c}.                                    \tag{5.18}
\]

Together with (5.10) and (5.14), this yields

\[
 \mathbb E_{\tau_c}(E_v-B)^2
 \le2z^2\{V^{\rm tail}_{C,c}+U^{\rm tail}_{2,c}\}.          \tag{5.19}
\]

Equations (5.8)--(5.11) likewise give

\[
 (\overline E-B)^2
 \le {2K^{m-1}\over a_0}z^2(V_C+KU_2).                     \tag{5.20}
\]

Apply \((x-y)^2\le2x^2+2y^2\) to
\(E_v-\overline E=(E_v-B)-(\overline E-B)\), and use
(5.19)--(5.20).  This is (5.15).  Finally

\[
 \mathcal X_c
 =\mathbb E_{\tau_c}(\overline E-E_v)_+
 \le\sqrt{\mathbb E_{\tau_c}(E_v-\overline E)^2},          \tag{5.21}
\]

which proves (5.16).  \(\square\)

Lemma 5.2 answers the normalization question exactly: a tail-local
conflict-square theorem would control \(\mathcal X_c\) without paying for
the rarity of the tail.  The current boundary-codegree results estimate
fixed bounded carriers in product or exact-slice reference states; they do
not yet bound (5.13) along the actual stopped law.  The signed regression
form (3.22) remains sharper because it can use cancellation even when the
tail-local variance is not small.

The same regression idea sharpens the reference-free shadow tangent.  Keep
the notation (5.1)--(5.3), let \(m\ge2\) be even, and assume

\[
 (1+\delta)z\le c\le A_0z,
 \qquad d_v\le Kz.                                           \tag{5.22}
\]

Put

\[
 w(d)=\nabla_m(d-c)=(d-c)_+^m-(d-c-1)_+^m,                   \tag{5.23}
\]

\[
 \Xi_v=E_v-(\overline C-z),qquad
 \mathcal P_{m,c}=-\sum_vd_v\Xi_vw(d_v),                    \tag{5.24}
\]

and use the incidence-root law \(\rho(v)=d_v/(nz)\).  Define

\[
 \chi(d)=\mathbb E_\rho[\Xi_v\mid d_v=d],                   \tag{5.25}
\]

\[
 \mathfrak I_c^{\rm sh}(\chi)=
 \sup_{\substack{d<e\\w(d)<w(e)}}(\chi(d)-\chi(e))_+,      \tag{5.26}
\]

where only degree values of positive \(\rho\)-mass are used.  Finally let

\[
 U_{m,c}={1\over nz^m}\sum_{v:d_v>c}|d_v-z|^m.              \tag{5.27}
\]

### Lemma 5.3 (regression bound for shadow protection)

Under (5.22),

\[
 \boxed{
 (\mathcal P_{m,c})_+
 \le C_{m,\delta,A_0,K}\,nz^m
       \{\mathfrak I_c^{\rm sh}(\chi)+zU_2\}U_{m,c}.}       \tag{5.28}
\]

Consequently, if \(p\le C_p\epsilon/(rz)\) and

\[
                         \mathfrak I_c^{\rm sh}(\chi)\le Lz, \tag{5.29}
\]

then

\[
 \boxed{
 {p\over nc^m}(\mathcal P_{m,c})_+
 \le {C\epsilon\over r}(L+U_2)U_{m,c}.}                    \tag{5.30}
\]

This replaces the \(\epsilon\sqrt{U}\) cap-only protection term by a
linear tail term whenever the downward degree/exposure regression has
scale \(O(z)\), rather than the trivial \(O(rz)\) scale.

#### Proof

The incidence identity (5.5) in the master handoff, or a direct double
count, gives

\[
 \mathbb E_\rho\Xi_v
 =z-{\sum_vd_v^2\over nz}=-zU_2.                            \tag{5.31}
\]

Because \(w\) is a function of the degree,

\[
 -\mathbb E_\rho[\Xi_vw(d_v)]
 =-\operatorname {Cov}_\rho(\chi(D),w(D))
       +zU_2\mathbb E_\rho w(D).                             \tag{5.32}
\]

The pairwise proof of Lemma 3.4, now with \(w\) in place of
\(\varphi_c\), yields

\[
 -\operatorname {Cov}_\rho(\chi(D),w(D))
 \le\mathfrak I_c^{\rm sh}(\chi)\mathbb E_\rho w(D).        \tag{5.33}
\]

Indeed the sum of positive \(w\)-increments over unordered degree pairs is
at most \(\mathbb E_\rho w\).

Only \(T=\{v:d_v>c\}\) contributes to \(w\).  On this set,
\(w(d_v)\le C_mz^{m-1}\), while

\[
 |T|\le\delta^{-m}nU_{m,c}.                                 \tag{5.34}
\]

The cap therefore gives

\[
 \mathbb E_\rho w(D)
 ={1\over nz}\sum_{v\in T}d_vw(d_v)
 \le C_{m,\delta,A_0,K}z^{m-1}U_{m,c}.                     \tag{5.35}
\]

Finally \(\mathcal P_{m,c}=-nz\mathbb E_\rho[\Xi_vw]\).
Substitute (5.33)--(5.35) to get (5.28), then use
\(c=\Theta(z)\), the bound on \(p\), and (5.29) to obtain
(5.30).  \(\square\)

Since subtracting the constant \(\overline C-z\) does not change downward
inversions, (5.29) is equivalently an \(O(z)\) downward-inversion theorem
for \(d\mapsto\mathbb E_\rho[E_v\mid d_v=d]\).  This is the same
one-dimensional geometric profile isolated in (3.23), now at the
incidence-root weighting natural for the moving-center shadow potential.

The loss \(A_c^{-1/2}\) in the **global** estimate (5.6) is load-bearing.
At the reference
twelfth-moment scale \(A_c\) can be polynomially small, so the conflict
variance estimate currently available in the master handoff does not make
\(\sum_jp_j\mathcal X_{j,c}\) small.  Closing the logarithmic gate needs a
tail-localized exposure estimate, a signed cancellation for
\(\mathcal Y_c\), or a stronger joint Lyapunov function; global \(L^2\)
control alone is insufficient.

## 6. Why this is not yet (G.95)

There are three precise limitations.

1. **Exact-size conditioning.**  If a round is restricted to the event
   \(Q=q\) of exactly \(q\) accepted configurations, its carrier submass is

   \[
    a_{p,q}(\gamma)=a_p(\gamma)
       \Pr(Q=q\mid\gamma\hbox{ survives}).                  \tag{6.1}
   \]

   The second factor is a global residual-environment likelihood.  It need
   not have a local \(O((p\Delta_C)^2)\) expansion and is exactly the factor
   isolated in (G.76)--(G.77).  Therefore Theorem 3.1 must not be quoted for
   the exact-size kernel without an equivalence-of-ensembles theorem.  This
   remains a true limitation of the **conditioned formulation**, but it is
   no longer an obligation on the revised route: the random-clock mixture
   theorem keeps the actual bite unconditioned and thereby avoids G.76.

2. **Cumulative signed exposure.**  Boundary codegrees control overlaps
   among a fixed bounded family of configurations.  The statistic
   \(\mathcal Y_c\), however, asks whether the roots selected by a terminal
   high-degree test have systematically below-average marginal conflict
   exposure under the already tilted Palm law.  Theorem 3.1 removes the
   finite-bite remainder but supplies no sign or summability for (4.7).

3. **Reference-relative erosion and center.**  The unconditioned actual
   and random-size mixture reference both have exact Palm recursions, but
   this note does not compare their favourable erosion terms or transfer
   the predictable mixture center to the realized stopped center.  Those
   are still needed unless the reference-free shadow route is closed using
   Lemma 5.3.

Thus the new proved conclusion is sharp in scope:

\[
 \boxed{\begin{array}{c}
 \text{unconditioned finite-bite error is summable and G.76 is avoidable;}\\
 \text{cumulative signed regression plus erosion/center control remain.}
 \end{array}}                                                \tag{6.2}
\]
