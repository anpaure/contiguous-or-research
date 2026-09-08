# Gate A: contemporaneous normalized exposure and the tail-local companion gate

**Date:** 2026-08-22  
**Status:** exact unpurged sequential-state reduction and typed-codegree
duplicate bound; the stopped tail-local companion regression remains open

## 0. Outcome

The sequential-clock theorem reduces the ancestor-row rate to the
contemporaneous profile

\[
 d\longmapsto
 \mathbb E\left[\frac{h_\gamma}{Z}\,\middle|\,d_v=d\right].
                                                               \tag{0.1}
\]

At first sight the random global edge count \(Z\) appears to leave another
Simpson factor.  Before any unequal purge it does not.  At a fixed jump
number every shore size \(n_\sigma\) is deterministic, and

\[
 z_\sigma=\frac{k_\sigma Z}{n_\sigma},\qquad
 \frac{h_\gamma}{Z}
 =\frac{k_\sigma}{n_\sigma}\frac{h_\gamma}{z_\sigma}.       \tag{0.2}
\]

The prefactor is common to every state history.  Averaging over the
ordered carriers at a root gives the exact normalized decomposition

\[
 \boxed{
 \frac{\overline h_m(v)}{z_\sigma}
 =g_{\sigma,j}+\frac{d_v}{z_\sigma}
   +m\,\frac{R_v-J_v}{z_\sigma}
   -\frac{\overline D_m(v)}{z_\sigma},}                    \tag{0.3}
\]

where \(g_{\sigma,j}\) is deterministic at jump \(j\).  Therefore, for
every increasing test of the normalized degree \(X=d_v/z_\sigma\), the
degree term is favorable and the common term has zero covariance.  The
only adverse quantities are

\[
 U_v=\frac{R_v-J_v}{z_\sigma}
 \quad\hbox{and}\quad
 Q_v=\frac{\overline D_m(v)}{z_\sigma}.                    \tag{0.4}
\]

More precisely, if \(\tau_\Psi\) is the carrier-Palm root law tilted by an
increasing test \(\Psi(X)\), then

\[
 \boxed{
 \frac{[-\operatorname {Cov}(h_\gamma/Z,\Psi)]_+}
      {\mathbb E\Psi}
 \le\frac{k_\sigma}{n_\sigma}
 \left\{
 m\bigl(\mathbb EU-\mathbb E_{\tau_\Psi}U\bigr)_+
 +\mathbb E_{\tau_\Psi}Q
 \right\}.}                                               \tag{0.5}
\]

Thus neither the random \(Z\), the large common exposure
\(\Theta(rz)\), nor the normalized degree itself remains in the open
regression.

The duplicate term has a pointwise typed-codegree bound.  If a row has at
most \(\rho_t\) companions of pair type \(t\) relative to any one of its
targets, and \(\Lambda_t\) is the maximum current codegree of a type-\(t\)
pair, then on the high-degree range

\[
 \boxed{
 Q_v\le
 {m\choose2}qK\,
 \frac{\sum_t\rho_t\Lambda_t}{d_v-1}.}                     \tag{0.6}
\]

For the punctured high/low pair split,
\(\rho_H\le4\), \(\rho_L\le4r-1\), and \(q=4r\).  Hence, when
\(d_v\ge a z_\sigma\),

\[
 Q_v\le C_{m,K,a}
 \left(r\frac{\Lambda_H}{z_\sigma}
       +r^2\frac{\Lambda_L}{z_\sigma}\right).               \tag{0.7}
\]

Equations (0.5)--(0.7) are a strict reduction, not Gate-A closure.  The
available boundary-polymer estimates prove the corresponding conflict and
pair statistics in product and uniform-slice reference laws.  They do not
yet prove under the reachable stopped carrier-Palm law that roots selected
by the upper-degree tail have

\[
 \mathbb E_{\tau_\Psi}U
 \ge\mathbb EU-O(1),                                       \tag{0.8}
\]

nor do the currently recorded average pair-square energies imply the
pointwise current codegree hypotheses needed in (0.7).  The exact surviving
Gate-A statistic is now the tail-local companion deficit (0.8), plus the
typed duplicate load if it is not discharged separately.

## 1. Fixed-jump unpurged state mixtures

Let every edge of a finite simple hypergraph meet shore \(V_\sigma\) in
exactly \(k_\sigma\) vertices.  Consider a mixture \(\nu\) of current
states at one fixed jump number of the uniform-row deletion chain.  Assume
there has been no unequal auxiliary purge.  Since every selected row
removes \(k_\sigma\) vertices from shore \(\sigma\), all states in the
support of \(\nu\) have the same shore sizes

\[
                   n_{\sigma,j}=n_{\sigma,0}-jk_\sigma.    \tag{1.1}
\]

Here “fixed jump number” means that every live history has actually made
\(j\) selections.  A history frozen at an earlier stopping time does not
satisfy (1.1).  In a stopped proof one must retain the live indicator and
send frozen histories to a cemetery state, or index each live component by
its own jump count; one may not condition on future stop avoidance.

The edge count \(Z(H)\) may vary between states.  Put

\[
             z_\sigma(H)=\frac{k_\sigma Z(H)}{n_{\sigma,j}}.
                                                               \tag{1.2}
\]

For two shores \(\sigma,\tau\),

\[
 \boxed{
 \frac{z_\tau(H)}{z_\sigma(H)}
 =\frac{k_\tau n_{\sigma,j}}{k_\sigma n_{\tau,j}},}         \tag{1.3}
\]

which is deterministic throughout the mixture.

Fix a root shore \(\sigma\) and carrier order \(m\ge2\).  At a root \(v\)
of degree \(d_v\ge m\), choose an ordered \(m\)-carrier uniformly from the
distinct rows through \(v\).  Write

\[
 \overline h_m(v)=\mathbb E[h_\gamma\mid H,v],\qquad
 \overline D_m(v)=\mathbb E[D_\gamma\mid H,v],              \tag{1.4}
\]

where \(D_\gamma\) is the external duplicate count in the union of the
carrier conflict neighborhoods.  Let

\[
 C_F=|\Gamma(F)|,\qquad
 A_v=\frac1{d_v}\sum_{F\ni v}C_F,\qquad E_v=A_v-d_v.        \tag{1.5}
\]

The exact carrier-union identity is

\[
 \boxed{\overline h_m(v)=d_v+mE_v-\overline D_m(v)
       =mA_v-(m-1)d_v-\overline D_m(v).}                    \tag{1.6}
\]

It is purely deterministic and remains true state by state.

## 2. Removing the common exposure and global edge count

For \(u\in V_\tau\), put \(b_u=d_u-z_\tau\), and define

\[
 a_0=\sum_\tau k_\tau z_\tau,\qquad
 R_v=\frac1{d_v}\sum_{F\ni v}\sum_{u\in F-\{v\}}b_u.       \tag{2.1}
\]

For a row \(F\), let

\[
 \mathfrak E(F)=\sum_{G\in\Gamma(F)}(|F\cap G|-1),\qquad
 J_v=\frac1{d_v}\sum_{F\ni v}\mathfrak E(F).               \tag{2.2}
\]

The row identity

\[
 C_F=\sum_{u\in F}d_u-\mathfrak E(F)                       \tag{2.3}
\]

gives, after averaging over the root star,

\[
 \boxed{
 A_v=a_0+(d_v-z_\sigma)+R_v-J_v,}                          \tag{2.4}
\]

and hence

\[
 \boxed{
 E_v=a_0-z_\sigma+R_v-J_v.}                                \tag{2.5}
\]

By (1.3),

\[
 \frac{a_0}{z_\sigma}
 =\sum_\tau k_\tau
       \frac{k_\tau n_{\sigma,j}}{k_\sigma n_{\tau,j}}
 =:c_{\sigma,j}                                             \tag{2.6}
\]

is deterministic at fixed unpurged jump number.  Substituting (2.5) into
(1.6), and setting

\[
 X_v=\frac{d_v}{z_\sigma},\qquad
 U_v=\frac{R_v-J_v}{z_\sigma},\qquad
 Q_v=\frac{\overline D_m(v)}{z_\sigma},                    \tag{2.7}
\]

proves

\[
 \boxed{
 \frac{\overline h_m(v)}{z_\sigma}
 =m(c_{\sigma,j}-1)+X_v+mU_v-Q_v.}                         \tag{2.8}
\]

Finally, (1.2) gives

\[
 \boxed{
 \frac{\overline h_m(v)}{Z(H)}
 =\frac{k_\sigma}{n_{\sigma,j}}
   \{m(c_{\sigma,j}-1)+X_v+mU_v-Q_v\}.}                    \tag{2.9}
\]

Every coefficient outside \(X,U,Q\) in (2.9) is deterministic across the
whole state mixture.

## 3. Exact tail-tilt covariance reduction

Adjoin all current labelled ordered carriers to \(\nu\) with counting
multiplicity and normalize; call the resulting law \(\widehat\nu\).
Variables depending only on the root are identified with their root
values.  Let

\[
                 \Psi=\psi(X)\in[0,1]                      \tag{3.1}
\]

for a nondecreasing function \(\psi\), and assume
\(A_\Psi=\mathbb E_{\widehat\nu}\Psi>0\).  Define the tilted root law

\[
       \frac{d\tau_\Psi}{d\widehat\nu}
       =\frac{\Psi}{A_\Psi}.                               \tag{3.2}
\]

Since \(\Psi\) is root-measurable, averaging \(h_\gamma\) conditional on
the root replaces it by \(\overline h_m(v)\).  Equation (2.9) and the
identity

\[
 \frac{\operatorname {Cov}(Y,\Psi)}{A_\Psi}
 =\mathbb E_{\tau_\Psi}Y-\mathbb E_{\widehat\nu}Y           \tag{3.3}
\]

therefore give the exact formula

\[
\begin{aligned}
 -\frac{\operatorname {Cov}_{\widehat\nu}(h_\gamma/Z,\Psi)}
        {A_\Psi}
 =\frac{k_\sigma}{n_{\sigma,j}}\bigg[
 &-\{\mathbb E_{\tau_\Psi}X-\mathbb EX\}\\
 &+m\{\mathbb EU-\mathbb E_{\tau_\Psi}U\}\\
 &+\{\mathbb E_{\tau_\Psi}Q-\mathbb EQ\}\bigg].
                                                               \tag{3.4}
\end{aligned}
\]

Because \(X\) and \(\psi(X)\) are both nondecreasing,

\[
                  \mathbb E_{\tau_\Psi}X-\mathbb EX
 =\frac{\operatorname {Cov}(X,\Psi)}{A_\Psi}\ge0.           \tag{3.5}
\]

Also \(Q\ge0\).  Dropping the favorable first term and the nonpositive
\(-\mathbb EQ\) proves

\[
 \boxed{
 \frac{[-\operatorname {Cov}(h_\gamma/Z,\Psi)]_+}{A_\Psi}
 \le\frac{k_\sigma}{n_{\sigma,j}}
 \left[
 m\{\mathbb EU-\mathbb E_{\tau_\Psi}U\}_+
 +\mathbb E_{\tau_\Psi}Q
 \right].}                                                \tag{3.6}
\]

No conditioning on \(Z\), no deterministic edge-count center, and no
future-state likelihood ratio occurs in (3.6).

### 3.1 Relation to the exact falling-factorial carrier test

For a fixed \(a>1\), define

\[
 \psi_a(x)=\left(\frac{(x-a)_+}{x}\right)^m,\qquad
 \varphi_{a,z}(d)=\frac{(d-az)_+^m}{(d)_m}.                 \tag{3.7}
\]

On the positive branch \(d\ge az\),

\[
 \varphi_{a,z}(d)
 =\psi_a(d/z)\frac{d^m}{(d)_m}.                            \tag{3.8}
\]

For fixed \(m,a\), if \(z\ge2m/a\), then

\[
 \boxed{
 0\le\varphi_{a,z}(d)-\psi_a(d/z)
 \le\frac{C_{m,a}}{z}.}                                    \tag{3.9}
\]

Indeed

\[
 \frac{d^m}{(d)_m}
 =\prod_{i=0}^{m-1}\left(1-\frac{i}{d}\right)^{-1}
 =1+O_m(d^{-1}),                                           \tag{3.10}
\]

uniformly for \(d\ge az\), while both tests vanish below \(az\).
At the punctured degree floor \(z=e^{\Omega(r\log r)}\), and in the
relevant high-tail regime where the test mass is bounded below by a fixed
power of \(r\), replacing the exact test by \(\psi_a(X)\) costs
exponentially less than every Gate-A budget.  Without that tail-mass
hypothesis one must retain the displayed perturbation explicitly.  The
elementary covariance
perturbation

\[
 |\operatorname {Cov}(Y,\varphi)-\operatorname {Cov}(Y,\psi)|
 \le2\|Y\|_\infty\|\varphi-\psi\|_\infty                   \tag{3.11}
\]

records the complete error.

## 4. Pointwise typed-codegree control of the carrier duplicate

Partition unordered target pairs into finitely many types \(t\).  For each
type put

\[
 \rho_t=\max_{\substack{F\in E(H)\\v\in F}}
 |\{u\in F-\{v\}:\{u,v\}\hbox{ has type }t\}|,              \tag{4.1}
\]

\[
 \Lambda_t=\max_{\{u,v\}\ {\rm of\ type}\ t}d(u,v).        \tag{4.2}
\]

Let \(q=|F|\) be the common row size, and assume every target degree is at
most \(Kz_\sigma\) after changing \(K\) by a fixed shore-comparability
factor when necessary.

For a root \(v\), define

\[
 a_G(v)=|\{F\ni v:F\cap G\ne\varnothing\}|.                \tag{4.3}
\]

### Theorem 4.1 (typed duplicate bound)

For every root \(v\) with \(d_v\ge m\),

\[
 \boxed{
 \frac{\overline D_m(v)}{z_\sigma}
 \le {m\choose2}qK\,\frac{\sum_t\rho_t\Lambda_t}{d_v-1}.}   \tag{4.4}
\]

#### Proof

For a uniform ordered carrier, let \(N_G\) be the number of its carrier
rows meeting a fixed external row \(G\).  Its contribution to the external
duplicate count is \(N_G-\mathbf1_{\{N_G>0\}}\).  Since

\[
 N_G-\mathbf1_{\{N_G>0\}}\le {N_G\choose2},                 \tag{4.5}
\]

sampling without replacement from the root star gives

\[
 \overline D_m(v)
 \le {m\choose2}\frac1{(d_v)_2}
       \sum_{G\not\ni v}(a_G(v))_2.                         \tag{4.6}
\]

Write \(\lambda_{vu}=d(v,u)\).  Every root row meeting \(G\) does so at
some \(u\in G\), and hence

\[
 a_G(v)\le\sum_{u\in G}\lambda_{vu}.                       \tag{4.7}
\]

Cauchy's inequality, followed by double counting rows through \(u\), gives

\[
\begin{aligned}
 \sum_{G\not\ni v}a_G(v)^2
 &\le q\sum_G\sum_{u\in G}\lambda_{vu}^2\\
 &\le q\sum_u d_u\lambda_{vu}^2\\
 &\le qKz_\sigma\sum_u\lambda_{vu}^2.                     \tag{4.8}
\end{aligned}
\]

For each type,

\[
 \sum_{u:\,{\rm type}(u,v)=t}\lambda_{vu}
 =\sum_{F\ni v}
   |\{u\in F-\{v\}:{\rm type}(u,v)=t\}|
 \le\rho_t d_v.                                            \tag{4.9}
\]

Thus

\[
 \sum_u\lambda_{vu}^2
 \le d_v\sum_t\rho_t\Lambda_t.                            \tag{4.10}
\]

Use \((a)_2\le a^2\) in (4.6), then substitute
(4.8)--(4.10) and \(d_v/(d_v)_2=1/(d_v-1)\).  This proves
(4.4).  \(\square\)

### Corollary 4.2 (punctured high/low split)

In a directed punctured configuration the high-pair skeleton is the union
of the containment and disjoint-middle paths.  Its maximum degree is at
most four.  Therefore

\[
 \rho_H\le4,\qquad \rho_L\le4r-1,\qquad q=4r.               \tag{4.11}
\]

If \(d_v\ge az_\sigma\) and \(z_\sigma\) is above a fixed
\(m,a\)-dependent constant, (4.4) gives

\[
 \boxed{
 Q_v\le C_{m,K,a}
 \left(
 r\frac{\Lambda_H}{z_\sigma}
 +r^2\frac{\Lambda_L}{z_\sigma}
 \right).}                                                \tag{4.12}
\]

This is pointwise and therefore passes through every tail tilt without a
rare-tail normalization penalty.

## 5. What the boundary statistics do and do not supply

The companion statistic in (3.6) has the exact form

\[
 U_v=\frac1{d_vz_\sigma}
 \sum_{F\ni v}\left[
 \sum_{u\in F-\{v\}}(d_u-z_{\operatorname {sh}(u)})
 -\mathfrak E(F)\right].                                  \tag{5.1}
\]

It is a signed, tail-local incidence statistic.  A sufficient theorem is

\[
 \boxed{
 \mathbb E_{\tau_\Psi}U
 \ge\mathbb E_{\widehat\nu}U-L}                            \tag{5.2}
\]

with \(L=O(1)\), uniformly over the stopped density bins and the relevant
tail tests.  Equation (3.6) then charges at most
\((k_\sigma/n_\sigma)mL\) per one-row jump.  Summing over the density
clock gives an \(O(mL\log r)\) carrier-Palm loss, hence a polynomial
comparison factor.  To close the current numerical ledger, the resulting
coefficient must still be below its recorded
\(\kappa<2-20\alpha\) threshold; a merely unspecified large constant in
\(L=O(1)\) is not sufficient.

The existing deterministic conflict-variance identity

\[
 C_F=\sum_{u\in F}d_u-\mathfrak E(F)                       \tag{5.3}
\]

and the boundary pair-square energies control global \(L^2\) averages of
the two terms in (5.1).  They do not imply (5.2).  The reason is
normalization, not a missing Cauchy step: \(\tau_\Psi\) is the upper-tail
root law, so a global \(L^2\) estimate pays the inverse square root of the
tail mass.  The tail-local conflict-square statistic isolated in the
finite-bite note would suffice, but it has not been propagated under the
actual stopped law.

Likewise, the boundary-codegree theorem gives sharp codegrees in the
complete catalogue and annealed product/slice descendants.  Codegrees only
decrease under induced deletion, but the current normalization
\(\Lambda_t/z_\sigma\) can increase as \(z_\sigma\) falls.  The recorded
average energies \(\Theta_H,\Theta_L\) do not imply the pointwise current
caps used in (4.12) after conditioning on an adaptive upper-tail root.

Accordingly the sequential route has removed the following from the live
ancestor-row problem:

1. future \(1/Z(H_K)\) variation;
2. survivor reweighting inside a predictably fixed ancestor cohort;
3. the random current edge count in the normalized degree and common
   exposure terms; and
4. child-degree rebinning.

What remains is exactly (5.2), together with either (4.12) at a summable
scale or a tail-local duplicate-energy substitute.  This is narrower than
full residual-state domination and narrower than a stopped theorem for all
boundary polymers, but it is not yet proved by the current global
statistics.

There is one further interface rather than an implicit identification.
The test in Section 3 is a common function of the normalized degree
\(d/z_\sigma(H)\), so its absolute threshold is state-dependent.  If the
Palm recursion is run with one fixed absolute terminal threshold \(c\)
across several realized centers, (3.6) does not directly apply.  One must
use the already planned shadow-center construction or localize the state
law to sufficiently narrow center bins and pay the explicit center-transfer
error.  The present note removes the random \(Z\) only after that normalized
test/center choice is made.

## 6. Global statistics do not force a numerically small tail-local loss

The normalization warning in Section 5 has a literal finite family.
It shows that even vanishing global companion variance, constant row
duplicate excess, pair codegree one, and a fixed degree cap do not force
the deficit in (5.2) to be \(o(1)\), or even uniformly smaller than one.

Fix integers \(D\ge\max\{m,3\}\), \(m\ge2\).  Let \(H_{D,M}\) be the
disjoint union of \(M\) copies of \(K_{D,D}\) and one star
\(K_{1,2D}\).  Regard it as a two-uniform hypergraph on one shore.  It has

\[
 n=2DM+2D+1,\qquad Z=MD^2+2D,\qquad
 z_{D,M}=\frac{2Z}{n}\longrightarrow D.                    \tag{6.1}
\]

The bulk vertices have degree \(D\), the star center has degree \(2D\),
and the star leaves have degree one.  Hence the maximum-to-average degree
ratio tends to two.  Every target-pair codegree is at most one.

For a graph edge \(F\), its duplicate excess is

\[
 \mathfrak E(F)=
 \sum_{G\in\Gamma(F)}(|F\cap G|-1)=1,                      \tag{6.2}
\]

because only the self row meets \(F\) twice.  Also

\[
 C_F=
 \begin{cases}
 2D-1,&F\hbox{ lies in a }K_{D,D}\hbox{ component},\\
 2D,&F\hbox{ lies in the star}.
 \end{cases}                                                \tag{6.3}
\]

Thus

\[
 \frac{\operatorname {Var}_F C_F}{z_{D,M}^2}\longrightarrow0,
 \qquad
 \frac1{Zz_{D,M}^2}\sum_F
 \left(\sum_{u\in F}d_u-2z_{D,M}\right)^2\longrightarrow0. \tag{6.4}
\]

The second limit is the global companion energy.  For completeness, put

\[
 \varepsilon_{D,M}=D-z_{D,M}
 =\frac{D(2D-3)}{n}.
\]

If \(p_\star=2D/Z\) is the fraction of star rows, the two quantities in
(6.4) are exactly

\[
 \frac{p_\star(1-p_\star)}{z_{D,M}^2},\qquad
 \frac{MD^2(2\varepsilon_{D,M})^2
       +2D(1+2\varepsilon_{D,M})^2}
      {Zz_{D,M}^2}.
\]

Both are \(O_D(M^{-1})\).  More generally, for each fixed \(p\ge1\), the
normalized centered absolute degree moment is

\[
 \frac{2DM\varepsilon_{D,M}^p+
       (D+\varepsilon_{D,M})^p+
       2D(D-1-\varepsilon_{D,M})^p}
      {n z_{D,M}^p}
 =O_{D,p}(M^{-1}).
\]

For the star center \(v_\star\), every companion is a degree-one leaf.
Consequently

\[
 R_{v_\star}=1-z_{D,M},\qquad J_{v_\star}=1,\qquad
 U_{v_\star}=-1.                                           \tag{6.5}
\]

For every bulk vertex,

\[
 R_v=D-z_{D,M},\qquad J_v=1,\qquad
 U_v=\frac{D-z_{D,M}-1}{z_{D,M}}\longrightarrow-\frac1D.   \tag{6.6}
\]

Choose any fixed \(a\in(1,2)\) and use the increasing normalized-degree
test \(\psi_a\) from (3.7).  For all sufficiently large \(M\), it vanishes
on the bulk and is positive only at the star center among roots supporting
an \(m\)-carrier.  Under \(\widehat\nu\), the bulk and center have carrier
multiplicities \(2DM(D)_m\) and \((2D)_m\), respectively.  Hence

\[
 \mathbb E_{\widehat\nu}U
 =\frac{2DM(D)_m U_{\rm bulk}-(2D)_m}
        {2DM(D)_m+(2D)_m}
 \longrightarrow-\frac1D.
\]

Therefore

\[
 \mathbb E_{\tau_{\psi_a}}U=-1,\qquad
 \mathbb E_{\widehat\nu}U\longrightarrow-\frac1D,
 \qquad
 \boxed{
 \mathbb E_{\widehat\nu}U-\mathbb E_{\tau_{\psi_a}}U
 \longrightarrow1-\frac1D.}                              \tag{6.7}
\]

The carrier duplicate is identically zero.  At a bulk root, the external
conflict sets belonging to distinct carrier rows lie on distinct opposite
vertices; at the star center there are no external conflicts beyond its
root star.  Hence

\[
                         Q_v=0                              \tag{6.8}
\]

for every carrier-supporting root.

The high-degree center has hazard \(2D\), whereas a bulk ordered
\(m\)-carrier has hazard

\[
                         D+m(D-1).                          \tag{6.9}
\]

Thus the tail-local deficit in (6.7) is exactly the mechanism creating an
adverse survival preference, while every global statistic in (6.4) tends
to zero.

This graph family is not asserted to be a directed punctured residual.  It
proves the logical point needed here: the current global boundary-polymer
and conflict-variance bounds cannot, by averaging alone, establish (5.2)
with \(L=o(1)\), or with any universal \(L<1\).  Indeed, after choosing
\(D\) arbitrarily large, the limiting deficit in (6.7) is arbitrarily
close to one.  In particular these global bounds do not supply the
numerically required \(L<\kappa/m\) (before charging any duplicate budget),
because the current ledger has \(\kappa<2\) and \(m\ge2\).  A positive
proof must use a tail-local statistic or a punctured reachability property.
