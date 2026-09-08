# Gate A: high even moments make cap-only protection summable

**Date:** 2026-08-22

**Status:** unconditional deterministic and exponent reductions; conditional
Gate-A closure theorem. The missing hypotheses are stated exactly in
Section 8. No stopped-law comparison is claimed.

## 0. Outcome

The sixth-power shadow potential leaves a factor-\(r\) loss if conflict
variance is bounded only by the degree cap. Raising the potential to a fixed
even power \(m>8\) removes that numerical obstruction.

For a microbite of size \(\varepsilon\), the positive protection term is

\[
\frac{C\varepsilon}{r}
\left(U_m+\sqrt{V_CU_m}\right),                       \tag{0.1}
\]

where \(U_m\) is a normalized degree-tail moment and
\(V_C=\operatorname{Var}_F(C_F)/z^2\). Under the degree cap and an explicit
two-shore average-degree comparability hypothesis,

\[
V_C=O(r^2).                                             \tag{0.2}
\]

The proved product/fixed-slice reference law has

\[
U_m^{\mathrm{ref}}
=O_m\!\left((rx^3)^{-m/2}\right),
\qquad \alpha<\frac1{3m},\qquad x\ge r^{-\alpha}.       \tag{0.3}
\]

The honest microbite clock then gives total cap-only protection

\[
O_m\!\left(
r^{\,1-m/4}x_J^{-3m/4}\right).                         \tag{0.4}
\]

This is \(o(1/r)\) exactly when
\(\alpha<(m-8)/(3m)\). Thus \(m=10\) is the first possible even power.
For \(m=12\), the reference range \(\alpha<1/36\) is stricter than the
protection restriction \(\alpha<1/9\), and

\[
U_{12}^{\mathrm{ref}}=O(r^{-6}x^{-18}),\qquad
F_{\mathrm{prot}}=O(r^{-2}x_J^{-9})=o(1/r).           \tag{0.5}
\]

The `o(1/r)` rate closes the shadow-potential ledger only up to a separate
shore-comparability stop. Using the crude unweighted purge telescope to
remove that stop requires `F=o(x_J/r)`, which changes the allowed comparison
loss from `kappa<2-18alpha` to

\[
                         \kappa<2-20\alpha.           \tag{0.5a}
\]

The lossless case `kappa=0`, `alpha<1/36` still has ample room.

There is also a cap-only bound for the order-\(m\) collision defect:
its total contribution is

\[
O_m\!\left(r^{\,1-m/2}x_J^{-3m/2}\right),             \tag{0.6}
\]

so the older sixth-defect comparison is not needed on this conditional
route.

This does **not** prove Gate A. Formula (0.3) is proved for independent
product residuals and uniform exact slices, not for the actual stopped
residual. The decisive remaining input is a density-localized stopped
comparison for one upper-tail moment, together with the finite-microbite
realized-center transfer. Moreover, an `o(1/r)` forcing ledger controls the
cap only up to the separate shore-comparability stop. To prove that this
stop is itself unlikely by the crude purge ledger, one needs the stronger
rate `o(x_J/r)`. High moments do not preserve the cap by themselves.

## 1. Capped two-shore setup

Let \(H\) be a finite simple hypergraph with two vertex shores
\(V_M,V_L\). Every edge contains \(k_M=k_L=2r\) vertices from the two
shores. Put

\[
Z=|E(H)|,\qquad n_\sigma=|V_\sigma|,\qquad
z_\sigma=\frac{2rZ}{n_\sigma}.                       \tag{1.1}
\]

Throughout a stopped interval assume, explicitly,

\[
d(v)\le Kz_\sigma\quad(v\in V_\sigma),\qquad
R_0^{-1}\le\frac{z_L}{z_M}\le R_0,\qquad
\min_\sigma z_\sigma\ge1.                            \tag{1.2}
\]

The second condition cannot be replaced by the exact unpurged shore-size
identity: unequal high-degree purges can change the two shore sizes
differently.

For an edge \(F\), let

\[
\Gamma(F)=\{G:G\cap F\ne\varnothing\},\qquad C_F=|\Gamma(F)|.
                                                               \tag{1.3}
\]

For a fixed shore, write \(z=z_\sigma\), \(n=n_\sigma\), and

\[
\bar C=\frac1Z\sum_FC_F,\qquad B=\bar C-z,
\]

\[
A_v=\frac1{d(v)}\sum_{F\ni v}C_F,\qquad
E_v=A_v-d(v),\qquad \Xi_v=E_v-B.                    \tag{1.4}
\]

Zero-degree terms are set to zero. For \(v\notin G\), define

\[
a_G(v)=|\{F:v\in F,\ F\cap G\ne\varnothing\}|.       \tag{1.5}
\]

The exact row identity is

\[
\sum_{G\not\ni v}a_G(v)=d(v)E_v.                    \tag{1.6}
\]

Indeed, for every \(F\ni v\), exactly \(C_F-d(v)\) conflicting edges do
not contain \(v\).

The cap and (1.2) imply

\[
C_F\le\sum_{u\in F}d(u)\le C_{K,R_0}rz,              \tag{1.7}
\]

and therefore

\[
0\le B,E_v\le C_{K,R_0}rz,\qquad
V_C:=\frac{\operatorname{Var}_{F\in E(H)}C_F}{z^2}
\le C_{K,R_0}r^2.                                    \tag{1.8}
\]

To prove `B>=0`, average
\(C_F\ge(2r)^{-1}\sum_{v\in F\cap V_\sigma}d(v)\) and use
\(\sum_vd(v)^2\ge(2rZ)^2/n\). The remaining bounds follow from (1.7).

## 2. The reference \(2s\)-moment envelope

This section records precisely what is already available at a product or
uniform exact-slice checkpoint.

Fix a retained target \(v\), let \(X_v\) be its residual degree, let
\(\mu=\mathbb EX_v\), and put \(Z_F=I_F-\mathbb EI_F\) for its incident
configuration indicators. For distinct configurations define
\(t(F,G)=|(F\cap G)-\{v\}|\). The proved rooted kernel bounds are

\[
R_c,Q_c
=O_c\!\left(r^{-1}x^{-3c}+r^{-2}x^{-4c}\right),       \tag{2.1}
\]

where \(R_c\) is the average \(x^{-ct}-1\) row sum and \(Q_c\) is the
positive-overlap row sum.

For an ordered tuple of \(j\) distinct configurations, its dependency
graph joins intersecting pairs. A singleton component has zero centered
expectation. A component of size two costs \(R_1\). A component of size
\(j\ge3\) costs

\[
Q_{j/2}^{\,j-1}.                                     \tag{2.2}
\]

The spanning-tree proof of (2.2) is as follows. A maximum spanning tree
carries at least \(2/j\) of the total pair-overlap weight; root it and sum
successive leaves with the \(Q_{j/2}\) kernel. There are only
\(j^{j-2}\) labelled trees. Repeated indicators reduce to fewer distinct
centered indicators because every fixed power of a centered Bernoulli
variable is affine in that variable plus a constant of size at most its
mean.

Consequently, for \(m=2s\),

\[
\frac{\mathbb E(X_v-\mu)^m}{\mu^m}
\le C_m
\sum_{\substack{(n_2,\ldots,n_m)\\
                 \sum_jjn_j=m}}
R_1^{n_2}\prod_{j=3}^m
Q_{j/2}^{(j-1)n_j}
+e^{-\Omega(r)}.                                    \tag{2.3}
\]

This is the exact fixed-\(m\) component envelope. If
\(\alpha<1/(3m)\), every term in (2.3) is bounded by the all-pair term,
giving

\[
\boxed{
\frac{\mathbb E(X_v-\mu)^m}{\mu^m}
=O_m((rx^3)^{-m/2})+e^{-\Omega(r)}.}                 \tag{2.4}
\]

Here is the exponent check. Put \(\varrho=r^{-1}x^{-3}\). The first
kernel monomial of a size-\(j\) component, divided by
\(\varrho^{j/2}\), is

\[
r^{\,1-j/2}x^{-3j(j-2)/2}\le1
\quad\text{when}\quad \alpha\le\frac1{3j}.
\]

Replacing one first kernel monomial by its second one costs the factor
\(r^{-1}x^{-j/2}\le1\); for \(j=2\), the analogous factor is
\(r^{-1}x^{-1}\le1\). Since \(j\le m\), every component costs at most
\(O_m(\varrho^{j/2})\), and the component sizes sum to \(m\). This proves
the compression in (2.4).

The same statement holds on every uniform exact two-shore slice. The
global edge-count \(m\)-moment is \(O_m((rx)^{-m/2})\), so replacing the
deterministic mean by the realized shore average leaves the larger bound
(2.4) unchanged.

For a center \(c\ge(1+\delta)z\), define the only tail statistic needed
below:

\[
U_{m,c}(H)
=\frac1{nz^m}\sum_{v:d(v)>c}|d(v)-z|^m.              \tag{2.5}
\]

At a reference checkpoint, (2.4) implies

\[
\mathbb E U_{m,c}
=O_m((rx^3)^{-m/2})+e^{-\Omega(r)}.                  \tag{2.6}
\]

Equation (2.6), not its stopped adaptive analogue, is currently proved.

## 3. Exact order-\(m\) one-sided tangent

Let \(m\ge2\) be even and let \(c\) be a moving center. Put

\[
f_c(d)=(d-c)_+^m,\qquad
\nabla_m(t)=t_+^m-(t-1)_+^m,                          \tag{3.1}
\]

\[
P_{m-2}(t)=mt_+^{m-1}-\nabla_m(t)\ge0.                \tag{3.2}
\]

For \(0\le a\le d\), define

\[
\phi_{m,c}(d,a)
=a\nabla_m(d-c)-\{f_c(d)-f_c(d-a)\},                 \tag{3.3}
\]

\[
\mathfrak D^+_{m,c}(H)
=\sum_v\sum_{G\not\ni v}\phi_{m,c}(d(v),a_G(v)).
                                                               \tag{3.4}
\]

Convexity gives \(\phi_{m,c}\ge0\). In an infinitesimal isolated-edge
bite, let `H_p` be the residual, let `n^{ann}(p)` be the expected surviving
shore size, and move the center at the annealed average-degree rate
`c'(0)/c=-B`. Define

\[
 \Psi_{m,c}(p)=
 {\mathbb E\sum_{v\in V_\sigma(H_p)}
       (d_{H_p}(v)-c(p))_+^m
  \over n^{\rm ann}(p)c(p)^m}.                       \tag{3.4a}
\]

At `p=0`, the logarithmic derivative of `n^{ann}` is `-z`, while that of
`c^m` is `-mB`. The same single-mark calculation gives the exact identity

\[
\begin{aligned}
nc^m\Psi_{m,c}'(0)
={}&\mathfrak D^+_{m,c}
 +(z-c)\sum_vt_v{}_+^m-\sum_vt_v{}_+^{m+1}\\
&+B\sum_vd(v)P_{m-2}(t_v)
 -\sum_vd(v)\Xi_v\nabla_m(t_v),
                                                        \tag{3.5}\\
&\hspace{35mm}t_v=d(v)-c.
\end{aligned}
\]

To verify the algebra, the fixed-center derivative is

\[
-\sum_vd(v)t_v{}_+^m-\sum_vd(v)E_v\nabla_m(t_v)
+\mathfrak D^+_{m,c}.
\]

The moving center contributes \(mcB\sum_vt_v{}_+^{m-1}\), and the
denominator contributes \((z+mB)\sum_vt_v{}_+^m\). Substituting
\(E_v=B+\Xi_v\) and \(d=t_v+c\) yields (3.5).

If \(c\ge z\), the second and third terms of (3.5) are nonpositive.
The positive terms requiring control are the collision defect, lattice
term, and signed protection.

## 4. Cap-only bounds using one tail moment

Assume

\[
(1+\delta)z\le c\le A_0z                              \tag{4.1}
\]

for fixed \(\delta,A_0>0\), and abbreviate \(U=U_{m,c}(H)\).

### Lemma 4.1 (order-\(m\) collision defect)

Under (1.2) and (4.1),

\[
\boxed{\mathfrak D^+_{m,c}(H)
\le C_{m,\delta,A_0,K,R_0}\,nr z^{m+1}U.}             \tag{4.2}
\]

#### Proof

Only \(T=\{v:d(v)>c\}\) contributes. Since
\(|d(v)-z|\ge\delta z\) there,

\[
|T|\le\delta^{-m}nU.                                  \tag{4.3}
\]

The second-difference representation is

\[
\phi_{m,c}(d,a)
=\sum_{h=0}^{a-2}(a-1-h)\Delta^2f_c(d-h).
\]

On the capped range,
\(0\le\Delta^2f_c(y)\le C_mz^{m-2}\). Hence

\[
\phi_{m,c}(d,a)\le C_m(a)_2z^{m-2}.                   \tag{4.4}
\]

For fixed \(v\), use \(a_G(v)\le d(v)\), (1.6), and (1.8):

\[
\sum_{G\not\ni v}(a_G(v))_2
\le d(v)\sum_{G\not\ni v}a_G(v)
=d(v)^2E_v\le C rz^3.                                \tag{4.5}
\]

Multiply (4.4)--(4.5) and sum over (4.3). \(\square\)

The lattice term is even smaller:

\[
\boxed{
B\sum_vd(v)P_{m-2}(t_v)
\le C_{m,\delta,A_0,K,R_0}\,nr z^mU.}                \tag{4.6}
\]

Indeed \(P_{m-2}(t)\le C_mz^{m-2}\) on the capped positive tail,
\(B=O(rz)\), \(d(v)=O(z)\), and (4.3) applies.
For clarity, when `t>=1`,

\[
 P_{m-2}(t)
 =m\int_{t-1}^t(t^{m-1}-s^{m-1})\,ds
 \le C_mt^{m-2},                                    \tag{4.6a}
\]

while `0<t<1` gives `P_(m-2)(t)<=m`; this is the cancellation responsible
for the power `z^(m-2)` rather than `z^(m-1)`.

### Lemma 4.2 (protection covariance)

Let

\[
\mathcal P_{m,c}
=-\sum_vd(v)\Xi_v\nabla_m(d(v)-c).                   \tag{4.7}
\]

If

\[
p\le\frac{C_p\varepsilon}{rz},                       \tag{4.8}
\]

then

\[
\boxed{
\frac p{nc^m}(\mathcal P_{m,c})_+
\le\frac{C\varepsilon}{r}
\left(U+\sqrt{V_CU}\right).}                         \tag{4.9}
\]

#### Proof

Put \(w_v=\nabla_m(d(v)-c)\) and
\(W_F=\sum_{v\in F\cap V_\sigma}w_v\). Double counting gives

\[
\mathcal P_{m,c}
=\sum_vd(v)(d(v)-z)w_v
-Z\operatorname{Cov}_F(C_F,W_F).                    \tag{4.10}
\]

On \(T\), \(0\le w_v\le C_mz^{m-1}\). Equations (4.3) and the cap give

\[
\sum_{v\in T}d(v)\le CnzU,
\]

\[
\sum_vd(v)|d(v)-z|w_v\le Cnz^{m+1}U.                \tag{4.11}
\]

Cauchy on each edge and \(Z=nz/(2r)\) give

\[
\mathbb E_FW_F^2
\le\frac{2r}{Z}\sum_vd(v)w_v^2
\le C(2r)^2z^{2m-2}U.                               \tag{4.12}
\]

Therefore

\[
Z|\operatorname{Cov}(C,W)|
\le Zz\sqrt{V_C}\sqrt{\mathbb E W_F^2}
\le Cnz^{m+1}\sqrt{V_CU}.                            \tag{4.13}
\]

Divide (4.11)--(4.13) by \(nc^m\) and multiply by (4.8).
\(\square\)

Combining (1.8), (4.2), (4.6), and (4.9), and discarding the negative
terms in (3.5), the positive normalized first-order contribution of one
microbite is at most

\[
\boxed{
C_m\left(\varepsilon U+\varepsilon\sqrt U
          +\frac{\varepsilon U}{r}
          +\frac{\varepsilon U}{z}\right).}          \tag{4.14}
\]

The \(\varepsilon\sqrt U\) term is the cap-only protection cost. The
\(\varepsilon U\) term is the collision cost. The lattice term contains
\(z^{-1}\), which is exponentially negligible under the established
degree floor.

For the shadow potential below, `c=aw` and the normalization is `nw^m`.
There is no missing power of the center: at every fixed state,

\[
 {1\over nw^m}\sum_v(d(v)-aw)_+^m
 =a^m {1\over n(aw)^m}\sum_v(d(v)-aw)_+^m.            \tag{4.15}
\]

Thus insertion into the shadow ledger multiplies the tangent forcing only
by the fixed constant `a^m`.

## 5. The order-\(m\) shadow purge telescope

For each shore carry a shadow center \(w_\sigma\). Across a bite, move it
by the same **realized** relative ratio as the provisional average
\(z_\sigma^*/z_\sigma\); across a purge, leave it fixed. This makes the
gap identity below pathwise. The tangent calculation uses the predictable
annealed ratio instead, and Section 7 isolates the error between the two.
Stop if

\[
\frac{w_\sigma}{z_\sigma}>R_*
\quad\text{or}\quad
\frac{z_L}{z_M}\notin[R_0^{-1},R_0].                 \tag{5.1}
\]

Fix constants

\[
1<a<aR_*<K_0<K,\qquad
0<\rho_0\le1-\frac{K_0}{K}.                          \tag{5.2}
\]

and define

\[
\Phi_{m,\sigma}(H;w)
=\frac1{n_\sigma w_\sigma^m}
\sum_{v\in V_\sigma}(d(v)-aw_\sigma)_+^m.            \tag{5.3}
\]

After a provisional bite, purge every target with
\(d(v)>K_0z_\sigma^*\), and all incident edges. Let \(\rho\) be the
removed-edge fraction, \(\tau_\sigma\) the removed shore-vertex fraction,
\(L_\sigma\) the bad shore incidence, and
\(\beta_\sigma=L_\sigma/Z^*\). Exactly as in the sixth-power proof,

\[
\tau_\sigma\le\frac{\rho}{K_0},\qquad
\rho\le\beta_M+\beta_L.                               \tag{5.4}
\]

Every bad target satisfies
\[
d-aw\ge c_1w,\qquad d-aw\ge c_2d.
\]
Thus, for every fixed even \(m\),

\[
\sum_{v\in B_\sigma}(d(v)-aw)^m
\ge c_mw^{m-1}L_\sigma.                              \tag{5.5}
\]

Induced deletion only lowers surviving degrees. Consequently,

\[
\Phi_{m,\sigma}(H^\circ;w)
\le\frac1{1-\rho/K_0}
\left(\Phi_{m,\sigma}(H^*;w)
-c_m\frac{\beta_\sigma}{2r}\frac{z_\sigma^*}{w_\sigma}
\right).                                             \tag{5.6}
\]

While \(\Phi_M+\Phi_L\le\eta/r\), for a sufficiently small fixed
\(\eta>0\), and \(\rho\le\rho_0\), the multiplicative term is absorbed,
and each purge charges

\[
\Omega(\rho/r).                                       \tag{5.7}
\]

Moreover the exact shadow-gap identity is

\[
\log\frac{w_{J,\sigma}}{z_{J,\sigma}}
=\sum_{j<J}\log\frac{1-\tau_{j,\sigma}}{1-\rho_j}
\ge\left(1-\frac1{K_0}\right)\sum_{j<J}\rho_j.        \tag{5.8}
\]

Let the process be stopped before the first purge with `rho>rho_0`, as well
as at the displayed potential and shadow bounds. Then total expected
positive bite forcing `F_r=o(1/r)` implies

\[
\mathbb E\sum_{j<\tau}\rho_j=O(rF_r)=o(1),            \tag{5.9}
\]

and the shadow-ratio stopping event has probability `o(1)`. A first large
purge must be handled separately: (5.5) implies that `rho>rho_0` forces
provisional potential `Omega(rho_0/r)`. If the pre-bite potential is at most
`eta/r`, with `eta` chosen below that constant, the bite has made a positive
increment `Omega(1/r)`. Markov's inequality against `F_r=o(1/r)` makes this
event `o(1)`. Thus (5.9) may include the single stopping large-purge step
after adding an `o(1)` error. This is a stopped-event telescope, not
conditioning on future cap persistence.

There is an important rate distinction for the shore-ratio stop. Every
accepted edge removes exactly `2r` targets from each shore, so only unequal
purges alter the absolute shore-size difference. While fixed comparability
holds, a purge performed at lower-shore density `x_j` removes at most

\[
             C\rho_jx_j|V_{L,0}|                       \tag{5.10}
\]

vertices from either shore. Consequently, down to `x_*=r^{-alpha}`,

\[
 \left|{n_M\over n_L}-1\right|
 \le O\!\left({1\over rx_*}
       +{1\over x_*}\sum_{j<\tau}\rho_jx_j\right)     \tag{5.11}
\]

Indeed the initial absolute shore-size difference is
`2|V_(L,0)|/r`; equal-size bites preserve it, while (5.10) bounds the
absolute change made by each purge. Divide the resulting bound by
`n_L>=x_*|V_(L,0)|`. In particular, the crude bound from (5.9) controls
this ratio if

\[
                         F_r=o(x_*/r).                 \tag{5.12}
\]

The weaker hypothesis `F_r=o(1/r)` does **not** suffice: an early unequal
purge of fraction `delta=o(1)` followed by equal-size bites down to density
`x_*<<delta` creates relative shore imbalance of order `delta/x_*`.
Therefore no shore-comparability conclusion may be inferred from (5.9)
alone. A sharper alternative would be a density-weighted purge telescope
controlling the second term of (5.11) directly.

## 6. Honest microbite and exponent ledger

Let round `j` use a deterministic microbite schedule

\[
p_j\le\frac{C\varepsilon_j}{rz_{M,j}},\qquad
0<\varepsilon_j\le1.                                  \tag{6.1}
\]

Put `x_*=r^{-alpha}`. Conditionally on the stopped cap and exponential
degree floor, the accepted-count bounds give a nonincreasing density clock
with

\[
\Delta\log(1/x_j)\ge c\frac{\varepsilon_j}{r}.        \tag{6.2}
\]

on every active step. Arbitrary purge jumps only skip density intervals.
Therefore, for every fixed `b>0`, pathwise,

\[
\sum_{j:x_j\ge x_*}\frac{\varepsilon_j}{r}r^{-a}x_j^{-b}
=O(r^{-a}x_*^{-b}).                                  \tag{6.3}
\]

The inequality direction in (6.2) is the one needed here. To see this
without assuming an upper bound on purge jumps, partition `[x_*,1]` into
fixed-ratio density bins. The sum of `epsilon_j/r` over step-starts in one
bin is `O(1)` by (6.2), with at most one final crossing step; a purge can
only skip later bins. Summing the resulting geometric series gives (6.3).

There are \(O(r\log r/\varepsilon)\) rounds when
\(\varepsilon_j=\varepsilon\).

Determinism of `epsilon_j` is used when the conditional estimates below are
multiplied by bin-occupancy probabilities. A predictable random schedule
would require the comparison (6.4) to be localized jointly in density and
the realized weight `epsilon_j`; that stronger formulation is not assumed
here.

The stopped comparison must be density-localized. The original expression
with a random `x_j` on the right of an unconditional expectation is not a
well-formed estimate for the Jensen sum. Let `[xi_ell,2xi_ell)` be the
fixed-ratio bins just used. Let `mathcal G_j` be the current-history event
that round `j` is reached before any active stop, and put

\[
 \mathcal G_{j,\ell}
 =\mathcal G_j\cap\{x_j\in[\xi_\ell,2\xi_\ell)\}.
                                                               \tag{6.4a}
\]

Assume, for each shore and uniformly in `j,ell`, whenever the conditioning
event has positive probability,

\[
\mathbb E[U_{m,aw_j}(H_j)\mid\mathcal G_{j,\ell}]
\le C_mr^{\kappa+o(1)}(r\xi_\ell^3)^{-m/2}
 +e^{-\Omega(r)}.                                    \tag{6.4}
\]

Conditional Jensen gives
`E[sqrt(U)|G_(j,ell)]<=sqrt(E[U|G_(j,ell)])`. Taking the
expectation of the pathwise bin-occupancy bound (6.3), then summing the
geometric bins, makes (4.14) give

\[
\begin{aligned}
F_{\mathrm{coll}}
 &=O\!\left(r^{\,1+\kappa-m/2}
             x_*^{-3m/2}\right),\\
F_{\mathrm{prot,size}}
 &=O\!\left(r^{\,\kappa-m/2}
             x_*^{-3m/2}\right),\\
F_{\mathrm{prot,cov}}
 &=O\!\left(r^{\,1+\kappa/2-m/4}
             x_*^{-3m/4}\right).                    \tag{6.5}
\end{aligned}
\]

The covariance term is the largest. With `x_*=r^{-alpha}`, all three
are \(o(1/r)\) provided

\[
\boxed{\kappa<\frac m2-4-\frac{3m}{2}\alpha.}         \tag{6.6}
\]

For a lossless comparison, this requires \(m>8\) and
\(\alpha<(m-8)/(3m)\).

For `m=12`, the proved reference range and the potential-only ledger are

\[
\boxed{\alpha<1/36,\qquad \kappa<2-18\alpha,}         \tag{6.7}
\]

and, when \(\kappa=0\),

\[
\begin{array}{c|c}
\text{term}&\text{all-round bound}\\ \hline
U_{12}^{\rm ref}&r^{-6}x_*^{-18}\\
\text{collision}&r^{-5}x_*^{-18}\\
\text{protection size part}&r^{-6}x_*^{-18}\\
\text{protection covariance}&r^{-2}x_*^{-9}.
\end{array}                                           \tag{6.8}
\]

At \(\alpha<1/36\), every entry contributing to the potential is
\(o(1/r)\).

For full shore-comparability bootstrap via the crude estimate (5.12), the
forcing must instead be `o(x_*/r)`. The covariance term is again decisive,
and the exact sufficient inequality is

\[
 \boxed{\kappa<\frac m2-4-
             \left(\frac{3m}{2}+2\right)\alpha.}      \tag{6.9}
\]

For `m=12` this becomes

\[
 \boxed{\alpha<1/36,\qquad\kappa<2-20\alpha.}         \tag{6.10}
\]

The distinction between (6.7) and (6.10) is substantive: the former
controls the potential, cap, and purges only up to the shore-ratio stop;
the latter also makes the crude absolute shore-imbalance ledger summable.

## 7. Finite-bite, purge-transfer, and realized-center bookkeeping

The tangent identity is not automatically a finite-bite theorem. The
required fixed-\(m\) microbite expansion, under the conflict cap
\(p_j\Delta_C=O(\varepsilon_j)\), is a normalized second-order remainder
\(O_m(\varepsilon_j^2)\) per round. If established under the stopped law,
its total is

\[
O\!\left(\frac{r\log r}{\varepsilon}\varepsilon^2\right)
=O(\varepsilon r\log r).                              \tag{7.1}
\]

Thus the Taylor-safe choice

\[
\boxed{\varepsilon=o((r^2\log r)^{-1})}               \tag{7.2}
\]

makes (7.1) \(o(1/r)\). For example \(\varepsilon=r^{-3}\) works and
still leaves only polynomially many rounds; accepted counts retain
exponential conditional means under the proved degree floor.

For the shore-safe forcing rate `o(x_*/r)`, the corresponding sufficient
choice is

\[
 \boxed{\varepsilon=o(r^{-2-\alpha}/\log r).}          \tag{7.2a}
\]

The concrete choice `epsilon=r^{-3}` still works because `alpha<1`.

There is a separate post-purge normalization correction if one transports
the older symmetric collision defect through the purge. Its unnormalized
charge is \(O(q\rho nz^{7})\) at power six. Multiplying by the next
microbite rate and dividing by \(nz^6\) gives

\[
\frac{\varepsilon}{rz}\frac{O(q\rho nz^7)}{nz^6}
=O(\varepsilon\rho),\qquad q=4r.                     \tag{7.3}
\]

The purge potential removes \(\Omega(\rho/r)\), so (7.3) is absorbable
only when \(\varepsilon=o(1/r)\). Condition (7.2) supplies this. The
cap-tail collision estimate (4.2) re-estimates the order-\(m\) defect
directly at each stopped state and therefore does not itself require this
transport, but (7.3) is the correct ledger if the sixth-defect route is
retained.

Finally, the center in (3.5) moves at a predictable annealed rate, whereas
the shadow construction must be compared with the realized provisional
average. Let \(\mathcal E_{\mathrm{ctr},j}\) denote the normalized change
in \(\Phi_m\) caused by replacing the predictable center update by the
realized one. The exact required bound is

\[
\sum_j\mathbb E[
\mathbf1_{\mathcal G_j}|\mathcal E_{\mathrm{ctr},j}|]
=o(1/r).                                               \tag{7.4}
\]

For the full shore-safe conclusion, (7.4) and the finite-bite remainder
must both hold with the stronger right side `o(x_*/r)`. An unquantified
`o(1/r)` error can be concentrated at the last density scale and is not
enough to deduce (5.12).

Reference global \(m\)-moment bounds supply the corresponding
one-checkpoint scale at independent and uniform-slice snapshots; they do
not prove (7.4) for an adaptive transition. Likewise, the
\(O_m(\varepsilon_j^2)\) expansion must hold under the actual stopped law.
These are finite-bite/center transfer statements, not consequences of the
exponent arithmetic.

## 8. Conditional closure theorem and exact remaining transfer

### Theorem 8.1 (exact two-level conditional `m=12` closure)

Choose

\[
0<\alpha<\min\{1/36,\ 1/(256K)\},\qquad x_*=r^{-\alpha}.
                                                               \tag{8.1}
\]

Run the isolated-edge microbite followed by the `K_0`-threshold purge,
with the shadow potential (5.3) at `m=12`. Degree-cap failure is checked
only at **post-purge checkpoints**. Let `tau_base` be the first density
target, shore-comparability failure, or exponential-degree-floor failure.
Before `tau_base`, also stop at the first large purge, shadow-ratio failure,
potential threshold (checked both provisionally and post-purge), or
post-purge cap failure.

Assume the standard stopped accepted-count estimates, including the clock
(6.2) and its upper bite/edge-loss companion, and assume the
density-localized moment comparison (6.4).

1. If

   \[
   \kappa<2-18\alpha,\qquad
   \varepsilon=o((r^2\log r)^{-1}),                  \tag{8.2}
   \]

   and the finite-bite and realized-center errors have stopped total
   `o(1/r)`, then before `tau_base`

   \[
   F_r=o(1/r),\qquad
   \mathbb E\sum_{j<\tau}\rho_j=o(1).                \tag{8.3}
   \]

   Potential-threshold, first-large-purge, shadow-ratio, and post-purge
   cap failures have probability `o(1)`. This is cap preservation only up
   to the still-uncontrolled base stop; it does not assert that the shore
   ratio or degree floor reaches `x_*`.

2. If, more strongly,

   \[
   \boxed{
   \kappa<2-20\alpha,\qquad
   \varepsilon=o(r^{-2-\alpha}/\log r),}              \tag{8.4}
   \]

   and both finite-bite and realized-center stopped errors are
   `o(x_*/r)`, then

   \[
   F_r=o(x_*/r),\qquad
   \boxed{\mathbb E\sum_{j<\tau}\rho_j=o(x_*).}       \tag{8.5}
   \]

   The shore-comparability and degree-floor stops are then also unlikely,
   the post-purge maximum-degree cap persists with probability `1-o(1)`,
   and the cap-only descent reaches `x=x_*`.

#### Proof

For Item 1, (6.5)--(6.8) make collision, lattice, and protection forcing
`o(1/r)`; the two error assumptions add the same order. The initial full
hypergraph is regular, so the elevated one-sided potential is zero. Apply
the drift inequality to the process stopped immediately before the listed
events. Optional stopping is legitimate because every increment is taken
on a current-history event, not conditioned on future cap persistence.
Markov's inequality makes a hit of
`Phi_M+Phi_L=eta/r` improbable. Equations (5.6)--(5.9) telescope the
small purges. As explained after (5.9), a first large purge forces a
provisional positive-potential jump `Omega(1/r)`, so it too has probability
`o(1)` and contributes `o(1)` to the stopped purge sum.

For every nonlarge purge and every shore,

\[
 {z_\sigma^\circ\over z_\sigma^*}
 ={1-\rho\over1-\tau_\sigma}
 \ge1-\rho\ge1-\rho_0\ge {K_0\over K}.              \tag{8.6}
\]

Every survivor has `d^circ<=K_0z_sigma^*`; hence (8.6) gives
`d^circ<=Kz_sigma^circ`. Thus the cap cannot be the first post-purge
failure except on the first-large-purge event. The gap identity (5.8)
handles the shadow stop. This proves Item 1 and also shows why it cannot
dispose of `tau_base`.

For Item 2, (6.9)--(6.10) give algebraic forcing `o(x_*/r)`, and the
stronger error assumptions preserve that rate. The same telescope and
first-large-purge argument give (8.5). Until the shore stop, (5.11),
`x_j>=x_*`, and Markov's inequality show uniformly that the shore ratio
differs from its initial `1+O(1/r)` value by `o(1)`; because
`1/(rx_*)=o(1)`, it cannot reach a fixed comparability boundary.

On the same event, purges multiply the edge count by
`prod_j(1-rho_j)=exp(-o(1))`. The accepted-count upper bound and cap give
the usual `O(epsilon)` fractional edge loss per microbite. Over
`O(r log r/epsilon)` active microbites, the standard initial
`log Z_0=(2+o(1))r log r` bootstrap with
`alpha<1/(256K)` therefore retains the exponential average-degree floor.
The lower clock reaches `x_*`, and (8.6) preserves the cap throughout.
\(\square\)

### Exact logical status

The high-moment route removes the need for a fine conflict-variance theorem:
the crude cap bound \(V_C=O(r^2)\) is numerically sufficient at \(m=12\).
It also bounds the order-\(12\) collision defect from the same tail moment.

It does **not** turn the reference moment theorem into a stopped theorem.
The remaining probabilistic statement is the density-localized one-scalar
comparison (6.4), posed on actual stopped residuals, plus the finite-bite
realized-center transfer. A loss `r^(kappa+o(1))` is allowed up to
`kappa<2-18alpha` for potential/cap control before the shore stop, and up to
`kappa<2-20alpha` for the full shore-safe closure. The corresponding error
rate must strengthen from `o(1/r)` to `o(x_*/r)` in the latter statement.
These inputs are substantially narrower than comparison of full residual
state laws, but they are not presently proved.

Therefore the correct conclusion is:

\[
\boxed{
\text{fixed }m=12\text{ closes the exponent ledger under the cap, but
not the stopped-law transfer.}
}
\]
