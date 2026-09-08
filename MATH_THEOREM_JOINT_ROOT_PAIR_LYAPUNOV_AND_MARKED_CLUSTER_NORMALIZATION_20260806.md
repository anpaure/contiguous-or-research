# Joint root--pair Lyapunov and marked-cluster normalization

**Date:** 2026-08-06  
**Method:** exact future-overlap potentials, signed resource gradients,
killed exponential-clock hazards, and FIFO first-entry exposure; no
computation or search  
**Status:** exact reduction and a sharp obstruction to the scalar
root-energy Lyapunov.
The orbit-resolved root variance has a nonnegative centered future
potential whose ideal drift is the one-root survival factor.  Combining it
with the pair future potential closes every linear and service term.
The normalized incidence-gradient creation is a genuine four-edge
quantity, and the tempting centered near-isotropy row `(SG4-false)` is already
false in the pristine orbit by a factor `Theta(d)`: coordinate-star
Johnson harmonics are nearly constant along a length-`d` FIFO path.  The
smallest viable repair is the Johnson resolvent and stopped sector row
`(JSEC)` below.  The exact unmarked Eberlein tail and the pristine
multiplicity trace are proved; the sole local analytic gap is the adaptive
current-versus-pristine perturbation `(JRES)`/`(JSW)`.
Separately, the marked size-two and size-three product-residual
normalizations and their first-two-hit energies are closed by the same
finite FIFO entry audit.

This note continues
`MATH_THEOREM_RANK_COMPENSATED_DOUBLET_CLOCK_AND_ROOTED_OVERLAP_REDUCTION_20260806.md`.
All notation not redefined here is inherited from that note.

## 1. Orbit-resolved root quantities

Put

\[
 \Delta={2d\over M},\qquad
 \rho_i={p_{i+1}\over p_i},\qquad
 \rho_{s,i}={p_{s,i+1}\over p_{s,i}}.
 \tag{1.1}
\]

For a live lower root `v` and `h in {2,3}`, define

\[
 Y_v^{(h)}(i)=
 \sum_{\substack{E\in B_h, E\ni v\\E\ {\rm available}}}a_E(i),
 \qquad
 L_h(i)=\sum_{v\in\mathcal L_i}Y_v^{(h)}(i)=2dX_h(i).
 \tag{1.2}
\]

The number of live lower roots is

\[
                         n_i=|\mathcal L_i|=p_iM.
 \tag{1.3}
\]

For `E,F in B_h` through `v`, write

\[
 \begin{aligned}
 m_N(E,F;v)&=|((E\cap F)-\{v\})\cap
                  (\mathcal L\dot\cup\mathcal R)|,\\
 m_S(E,F)&=|(E\cap F)\cap([k]\times[L])|,\\
 u_N(E,F;v)&=|((E\cup F)-\{v\})\cap
                  (\mathcal L\dot\cup\mathcal R)|,\\
 u_S(E,F)&=|(E\cup F)\cap([k]\times[L])|.
 \end{aligned}
 \tag{1.4}
\]

Define the orbit-rooted future second moment

\[
 \mathcal Q_h(i)=
 \sum_{v\in\mathcal L_i}
 \sum_{\substack{E,F\in B_h\\E,F\supseteq v}}
 a_E(i)a_F(i)
 \left({p_i\over p_*}\right)^{m_N(E,F;v)}
 \left({p_{s,i}\over p_{s,*}}\right)^{m_S(E,F)}.
 \tag{1.5}
\]

The centered root potential is

\[
 \boxed{
 \mathcal V_h(i)=
 \mathcal Q_h(i)-2\lambda_hL_h(i)+\lambda_h^2n_i.}
 \tag{1.6}
\]

### Proposition 1.1 (positivity and initial scale)

For every state,

\[
 \boxed{
 \mathcal V_h(i)\ge
 \sum_{v\in\mathcal L_i}(Y_v^{(h)}(i)-\lambda_h)^2.}
 \tag{1.7}
\]

Moreover,

\[
                         \mathcal V_h(0)=O(M/(cd))
 \tag{1.8}
\]

when `p_*=c/d`.

#### Proof

All future-fugacity weights in (1.5) are at least one.  Therefore

\[
 \mathcal Q_h(i)\ge
 \sum_{v\in\mathcal L_i}(Y_v^{(h)}(i))^2.
 \tag{1.9}
\]

Substitution in (1.6) gives (1.7).  At time zero, (1.5) is exactly the sum
over lower roots of the `h`-restricted product-residual second moment at
`p_*`, up to the negligible slot convention.  Its mean-square baseline is
`M lambda_h^2`.  Corollary `(ROc)`, restricted to one orbit, bounds the
remaining variance by `O(M/(p_*d^2))=O(M/(cd))`.  This proves (1.8).
\(\square\)

## 2. Exact one-step drift of the centered root potential

For `E in B_h`, put

\[
 s_h(i)=\rho_i^{-(N_h-1)}\rho_{s,i}^{-2}.
 \tag{2.1}
\]

For a pair `E,F` in (1.5), set

\[
 R_h(E,F;v)=\rho_i^{-u_N(E,F;v)}
              \rho_{s,i}^{-u_S(E,F)},
 \tag{2.2}
\]

and

\[
 q_h(E,F;v)=1-\rho_i^{u_N(E,F;v)+1}
                    \rho_{s,i}^{u_S(E,F)}.
 \tag{2.3}
\]

Let `c_h(v,E,F)` denote the summand of (1.5), and retain

\[
                         \Lambda_i(U)=
 \sum_{G:G\cap U\ne\varnothing}a_G(i).
 \tag{2.4}
\]

### Proposition 2.1 (root future-potential drift)

The exact raw conditional drift is

\[
 \boxed{
 \begin{aligned}
 \mathbb E[\mathcal Q_h(i+1)-\mathcal Q_h(i)\mid\mathcal F_i]
 ={}&(\rho_i-1)\mathcal Q_h(i)\\
 &+\sum_{v,E,F}c_h(v,E,F)R_h(E,F;v)
 \left(q_h(E,F;v)-{\Lambda_i(E\cup F)\over X(i)}\right).
 \end{aligned}}
 \tag{2.5}
\]

Also, if

\[
 q_h(E)=1-\rho_i^{N_h}\rho_{s,i}^2,
 \tag{2.6}
\]

then

\[
 \boxed{
 \begin{aligned}
 \mathbb E[L_h(i+1)-L_h(i)\mid\mathcal F_i]
 ={}&(\rho_i-1)L_h(i)\\
 &+{2ds_h(i)\over X(i)}
   \sum_{E\in B_h}a_E(i)
            [X(i)q_h(E)-\Lambda_i(E)].
 \end{aligned}}
 \tag{2.7}
\]

Since `n_(i+1)=rho_i n_i`, the centered potential satisfies

\[
 \boxed{
 \mathbb E[\Delta\mathcal V_h\mid\mathcal F_i]
 =(\rho_i-1)\mathcal V_h
     +\mathfrak D_h^{(2)}-2\lambda_h\mathfrak D_h^{(1)},}
 \tag{2.8}
\]

where the two displayed error terms in (2.5) and (2.7) are respectively
`mathfrak D_h^(2)` and `mathfrak D_h^(1)`.

#### Proof

After selecting `G`, a cross-term in (1.5) survives exactly when `G`
misses `E union F`.  The two rates scale by `s_h^2`.  Since

\[
 2(N_h-1)=u_N+m_N,
 \qquad                         4=u_S+m_S,
 \tag{2.9}
\]

rate scaling times the change of future weight is `R_h`.  Moreover

\[
 R_h(1-q_h)=\rho_i.
 \tag{2.10}
\]

The survival probability is `1-Lambda_i(E union F)/X`; expanding as in
`(FP7)` proves (2.5).

For (2.7), use `L_h=2dX_h`.  A surviving `h`-edge scales by `s_h`, whence

\[
 \mathbb E L_h(i+1)
 =2ds_h\sum_{E\in B_h}a_E
       \left(1-{\Lambda_i(E)\over X}\right).
 \tag{2.11}
\]

The identity `s_h(1-q_h(E))=rho_i` gives (2.7).  Substitute (2.5), (2.7),
and `Delta n_i=(rho_i-1)n_i` in (1.6) to obtain (2.8).  \(\square\)

The important point is that the large baselines in `Q_h`, `L_h`, and
`n_i` all have the same one-root survival multiplier.  No subtraction of
two unrelated `Theta(M)` estimates is needed.

## 3. Direct live-root energy identity

For comparison with (2.8), set

\[
 Z_v^{(h)}=Y_v^{(h)}-\lambda_h,
 \qquad
 \mathcal R_h=\sum_{v\in\mathcal L_i}(Z_v^{(h)})^2.
 \tag{3.1}
\]

If `G` misses `v`, define the killed incident load

\[
 D_v^{(h)}(G)=
 \sum_{\substack{E\in B_h, E\ni v\\E\cap G\ne\varnothing}}a_E.
 \tag{3.2}
\]

The unhit load increment is

\[
 U_v^{(h)}(G)=(s_h-1)Y_v^{(h)}-s_hD_v^{(h)}(G).
 \tag{3.3}
\]

### Proposition 3.1 (exact contraction plus injection)

Let

\[
 \beta_v^{(h)}={1\over X}
       \sum_{G\not\ni v}a_GU_v^{(h)}(G),
 \qquad
 \nu_v^{(h)}={1\over X}
       \sum_{G\not\ni v}a_G(U_v^{(h)}(G))^2.
 \tag{3.4}
\]

Then

\[
 \boxed{
 \mathbb E[\Delta\mathcal R_h\mid\mathcal F_i]
 =-{1\over X}\sum_{v\in\mathcal L_i}Y_v(Z_v^{(h)})^2
   +2\sum_vZ_v^{(h)}\beta_v^{(h)}
   +\sum_v\nu_v^{(h)}.}
 \tag{3.5}
\]

#### Proof

If `G` hits `v`, its square is removed.  The expected removed contribution
is

\[
                         -{1\over X}\sum_vY_v(Z_v^{(h)})^2.
 \tag{3.6}
\]

If `G` misses `v`, expand
`(Z_v^(h)+U_v^(h)(G))^2-(Z_v^(h))^2`.  Averaging the linear and square
terms gives (3.5).  \(\square\)

On the good interval, the first term is at most `-c_0 R_h/X`.  The other
two terms are exactly the signed drift and carré-du-champ injection which
the future potential (2.8) packages without a rank-by-rank expansion.

## 4. The joint pair--root Lyapunov

Let `mathcal P_i` be the pair future potential `(FP2)`, and put

\[
                         \eta_d=d^{-3},
 \qquad
 \mathscr L_i=\mathcal P_i+eta_d
                    (\mathcal V_2(i)+\mathcal V_3(i)).
 \tag{4.1}
\]

By `(SM7)` and Proposition 1.1,

\[
                         \mathscr L_0=O(M/d^4).
 \tag{4.2}
\]

The ideal part of its drift is

\[
 (\rho_i^2-1)\mathcal P_i
 +\eta_d(\rho_i-1)(\mathcal V_2+\mathcal V_3),
 \tag{4.3}
\]

which is nonpositive.  Multi-hit creation in the pair term is `(FE3)`;
multi-hit and square injection in the root term are `(ROc)` and its
rooted first-two-hit expansion.  After those contributions, only the
signed first-order incidence gradients remain.

For a pair-potential term `A=(Q,E,F)`, call the two resources of `Q` its
**distinguished roots** and put `U_A^circ=(E union F)-Q`.  Their hit terms
belong to the two-root service compensator.  Let `g_x^circ` be the
derivative of `mathcal P_i` obtained from incidences
`x in U_A^circ`, and define the weighted best-fit coefficient

\[
 \beta_T={\sum_{x\in T_i}g_x^\circ\over\sum_{x\in T_i}Y_x}.
 \tag{4.4}
\]

The exact normalized gradient defect is

\[
 \boxed{
 \mathfrak G_T(i)=
 \sum_{x\in T_i}{(g_x^\circ-\beta_TY_x)^2\over Y_x}
 =\sum_{x\in T_i}{(g_x^\circ)^2\over Y_x}
   -{(\sum_xg_x^\circ)^2\over\sum_xY_x}.}
 \tag{4.5}
\]

It is nonnegative and vanishes exactly when the potential incidence is
proportional to the current root load.  On `c_0<=Y_x<=C_0`, it is
equivalent up to fixed factors to the normalized derivative variance
`J_T` in `(GDIR)`.

The signed first-order pair defect has the exact decomposition

\[
 \sum_{x\in T_i}(\bar Y_T-Y_x)g_x^\circ
 =-\beta_T\sum_{x\in T_i}(Y_x-\bar Y_T)^2
  -\sum_{x\in T_i}(Y_x-\bar Y_T)(g_x^\circ-\beta_TY_x).
 \tag{4.6}
\]

Thus

\[
 \sum_x(\bar Y_T-Y_x)g_x^\circ
 \le-{\beta_T\over2}\sum_x(Y_x-\bar Y_T)^2
     +{1\over2\beta_T}\mathfrak G_T,
 \tag{4.7}
\]

after changing the fixed constant using the good-load bounds.  The owner
shore additionally has the parallel mixture/ledger term already displayed
in `(FP16)`.

Equation (4.7) proves that the root variance itself has the favorable sign.
The only positive quantity not already priced by `(ROc)` or `(FE3)` is
`mathfrak G_T/beta_T`.

## 5. The scalar spectral shortcut fails

The gradient and hazard Dirichlet forms are dual faces of one centered
incidence operator.  At a fixed state let `mathfrak A_i` index either the
pair-potential cross-terms `A=(Q,E,F)` or the root-potential cross-terms
`A=(v,E,F,h)`, and give `A` its corresponding future-potential weight

\[
 \mu_A=c_i(Q,E,F)R_i(E,F;Q)
 \quad\hbox{or}\quad
 \mu_A=c_h(v,E,F)R_h(E,F;v).
 \tag{5.1}
\]

For a resource type `T`, define

\[
 (K_Tf)(A)=\sum_{x\in U_A^\circ\cap T}f_x
 \tag{5.2}
\]

on functions satisfying `sum_(x in T)Y_xf_x=0`.  The most tempting scalar
closure would be

\[
 \boxed{
 \sum_{A\in\mathfrak A_i}\mu_A(K_Tf)(A)^2
 \le (1+\epsilon_c)\beta_T(i)
                  \sum_{x\in T_i}Y_xf_x^2}
 \tag{SG4-false}
\]

for every such `f`, for the union incidence and for either side incidence.
In the pair family remove `Q`; in the root family remove `v`.  Distinguished
roots are omitted because their hazards are already paid by the killed
service term.  The owner parallel component is handled separately by the
orbit-mixture ledger.  The same row is required for the finitely many
marked-cluster-rooted families in Section 7.  Here
`epsilon_c=o_c(1)+o_d(1)`; choosing the fixed separator constant `c` large
makes it smaller than the service slack below.  Use the individual root
stop `|Y_x-1|<=epsilon_0` with a sufficiently small fixed `epsilon_0`;
`(ROc)` still charges its failures at `O(1/d)` after enlarging `c`.

### Proposition 5.1 (counterfactual sufficiency of `(SG4-false)`)

If `(SG4-false)` held until the global bootstrap stop, then

\[
 \mathfrak G_T(i)\le (1+\epsilon_c)\beta_T(i)\mathcal P_i.
 \tag{5.3}
\]

Consequently

\[
 \boxed{
 \mathbb E\sum_{i<T}{1\over X(i)}
       \sum_T{\mathfrak G_T(i)\over\beta_T(i)}
                         =O(M/d^4).}
 \tag{XG4}
\]

The same spectral row bounds the squared first-order part of the edge
hazard defect in `(HDIR)` by

\[
 {(1+\epsilon_c)\beta_T\over 2X(i)}
                 \sum_{x\in T_i}Y_x(Y_x-\bar Y_T)^2,
 \tag{5.4}
\]

which is absorbed by `eta_d` times the root contraction (3.6), uniformly
for `p_i>=c/d`.  Multi-hit terms are `(FE3)` and the root square injection
is `(ROc)`.  Hence the false scalar row would prove the joint local
stopped transfer.

#### Proof

Use the Hilbert spaces with norms

\[
 \|f\|_Y^2=\sum_xY_xf_x^2,
 \qquad
 \|z\|_\mu^2=\sum_A\mu_Az_A^2.
 \tag{5.5}
\]

The weighted adjoint satisfies

\[
 (K_T^*1)_x={1\over Y_x}
       \sum_{A:x\in U_A^\circ}\mu_A={g_x^\circ\over Y_x}.
 \tag{5.6}
\]

Projecting away constants replaces the right side by
`g_x^circ/Y_x-beta_T`.  Thus `(SG4-false)` and duality give

\[
 \mathfrak G_T=|K_T^*1-\beta_T\|_Y^2
 \le (1+\epsilon_c)\beta_T\|1\|_\mu^2
 \le (1+\epsilon_c)\beta_T\mathcal P_i,
 \tag{5.7}
\]

proving (5.3).  Divide by `beta_TX`, sum over types and time, and use the
occupation estimate `E sum_i P_i/X(i)=O(P_0)` from `(FP5)` and Lemma 7.4.
This proves `(XG4)`.

For the hazard face start from `f_x=Y_x-bar Y_T` and split it into its
`Y`-orthogonal component plus its `Y`-weighted constant component.  The
constant component is exactly the favorable variance term already
extracted in (4.6); apply `(SG4-false)` to the orthogonal component.  The
first-order defect of a side
`E-Q` is `X^-1(K_Tf)(A)`.  In `(HDIR)`,

\[
 h_iX(i)=2+o_c(1)+o_d(1)
 \tag{5.8}
\]

on the global bootstrap interval.  Hence `(SG4-false)` gives (5.4), with the
factor `1/2` coming from `1/(h_iX(i)^2)`.  The signed first-order drift
(4.6) supplies `-beta_T R_T/X`; because `epsilon_0` and `epsilon_c` are
small, one half absorbs the adjoint-gradient cross term and the other
absorbs (5.4), after taking `c` large.  The
root-potential contraction (3.6) and the distinguished-root service terms
absorb the corresponding rooted pieces.  Previously isolated multi-hit
and slot terms are smaller.  \(\square\)

The convention is that a zero `beta_T` contributes zero.

### Proposition 5.2 (the scalar row is fourth order)

Writing the kernel of `K_TK_T^*` gives

\[
 \sum_x{g_x^2\over Y_x}
 =\sum_{A,A'}\mu_A\mu_{A'}
       \sum_{x\in U_A^\circ\cap U_{A'}^\circ}{1\over Y_x}.
 \tag{5.9}
\]

Its numerator contains two pair-potential terms, hence four macro edges
`E,F,E',F'`, sharing a first free resource.  In contrast, `(ROc)` is
quadratic in macro weights and `(FE3)` is cubic.  Positivity and
Cauchy--Schwarz alone cannot reduce (5.9) to those lower-degree moments
without a maximum bound on a pair-potential derivative.

Equivalently, `(SG4-false)` would have been supplied by a four-edge first-common-resource
estimate for the centered kernel of (5.9), or by a direct contraction
identity for the normalized gradient `g_x^circ/Y_x`.  The complete orbit
has zero centered gradient by transitivity, but that does not bound its
dynamic creation.  Claiming that `(FE3)` alone proves `(SG4-false)` would
conflate a third moment with a fourth moment.

This fourth-order diagnosis remains correct, but the proposed scalar
operator bound is not: the complete orbit has slow Johnson modes on which
the normalized covariance is `Theta(d) beta_T`.  The next subsections give
the counterexample and replace `(SG4-false)` by the sector row `(JSEC)`.

### Proposition 5.3 (coordinate-star counterexample)

Let `Omega_q` be a central Johnson layer, with
`epsilon k<=q<=(1-epsilon)k`, and let one side of a macro contain a fresh
FIFO path

\[
                         S_0,S_1,\ldots,S_{r-1},
                         \qquad r=d+O(1).
 \tag{5.10}
\]

In the pristine complete orbit take

\[
                   f_a(S)={\bf1}_{\{a\in S\}}-{q\over k}.
 \tag{5.11}
\]

This is a degree-one Johnson harmonic.  A fixed coordinate `a` is among
the `O(r)` FIFO deletion/insertion labels with probability `O(r/k)`.
Since `k=Theta(d^2)` and `r=Theta(d)`, with probability `1-O(1/d)` its
membership does not change anywhere on (5.10).  Consequently

\[
 \mathbb E_{\rm orbit}\left(\sum_{j<r}f_a(S_j)\right)^2
       \ge c r^2\mathbb E_{\rm orbit} f_a(S_0)^2.
 \tag{5.12}
\]

The transitive first-incidence double count is

\[
 \sum_A\mu_A|U_A^\circ\cap T|
             =\beta_T|\Omega_q|.
 \tag{5.13}
\]

For the template actually used in the parent note, the constantly many
paths are based at two macroscopically separated, noncomplementary headers.
The sum of their degree-one incidence vectors has norm bounded below by a
fixed multiple of either norm, so their `E_1` contributions in (5.12)
cannot cancel; the common port changes only
`O(1/k)` of the orbit average.  Consequently the full side-incidence
operator satisfies

\[
 {\sum_A\mu_A(K_Tf_a)(A)^2
       \over \beta_T\sum_{S\in\Omega_q}f_a(S)^2}
                         \ge c d.
 \tag{5.14}
\]

This contradicts `(SG4-false)` by a factor `Theta(d)` before any greedy
deletion has occurred.  Centering removes only the constant sector and
does not remove (5.11).  Neither `(ROc)` nor `(FE3)` changes this
counterexample, because both are static moment bounds while (5.12) is a
one-path covariance.

### Proposition 5.4 (a near-antipodal doublet cancels only odd sectors)

One might replace the macroscopically separated headers by a stronger
near-antipodal pair: apart from the common port, pair the nonport
coordinates by complementation and leave a gap

\[
                         g=k-2q+O(1)=Theta(d).
 \tag{5.15}
\]

For the star (5.11), the two paired path sums cancel.  The `g` unpaired
coordinates and the common port give normalized covariance

\[
                         O(1+g/d)=O(1),
 \tag{5.16}
\]

so this redesign really does repair the degree-one obstruction.  It does
not repair the operator.  Under exact complementation the primitive
Johnson sector `E_s` has parity `(-1)^s`.  Hence the two halves cancel on
odd `s` and add on even `s`.  Take a nonzero pure degree-two harmonic,
for example the degree-two projection of pair membership.  On all but an
`O(g/k)` fraction of coordinates its values on the paired headers agree
up to `O(g/k)`.  Therefore

\[
 {\sum_A\mu_A(K_Tf)(A)^2
       \over \beta_T\sum_{S\in\Omega_q}f(S)^2}
                         \ge c d,
             \qquad 0\ne f\in E_2.
 \tag{5.17}
\]

Thus near-antipodality kills the first odd slow mode but preserves the
first even slow mode.  More generally it alternately cancels and doubles
the Johnson sectors.  A multi-header design would have to annihilate all
slow sectors through degree `Theta(d)`; treating the required number of
headers as one edge would threaten both the rank and the hereditary
cylinder, so it is not a free template repair.

### 5.5 Exact Johnson-sector scales

Let `A_(q,ell)` be the normalized distance-`ell` operator on `Omega_q`,
and let `Pi_s^(q)` be the orthogonal projection onto its primitive sector
`E_s`.  Its exact scalar on `E_s` is the normalized Eberlein polynomial

\[
 \phi_s^{(q)}(\ell)=
 {1\over {q\choose\ell}{k-q\choose\ell}}
 \sum_{a=0}^{\ell}(-1)^{\ell-a}
 {q-a\choose\ell-a}{q-s\choose a}{k-q+a-s\choose a}.
 \tag{5.18}
\]

In particular the normalized one-exchange Bernoulli--Laplace operator
`P_q=A_(q,1)` has eigenvalue and gap

\[
 \lambda_s^{(q)}
    =1-{s(k-s+1)\over q(k-q)},
 \qquad
 \vartheta_s^{(q)}=1-\lambda_s^{(q)}
    ={s(k-s+1)\over q(k-q)}.
 \tag{5.19}
\]

A fresh FIFO path has Johnson distance `|i-j|` between `S_i` and `S_j`.
Therefore complete-orbit averaging gives the **exact** normalized sector
covariance

\[
 \widehat\chi_{s,r}^{(q)}
 =1+2\sum_{j=1}^{r-1}\left(1-{j\over r}\right)
                    \phi_s^{(q)}(j).
 \tag{5.20}
\]

For comparison, the with-replacement one-exchange chain has the Fejer
multiplier

\[
 \chi_{s,r}^{(q)}
 =1+2\sum_{j=1}^{r-1}\left(1-{j\over r}\right)
                    (\lambda_s^{(q)})^j
       \asymp \min\{d,k/s\}
 \tag{5.21}
\]

for a central layer and `r=Theta(d)`.  The fresh-word scalar (5.20) is
nonnegative because it is a covariance eigenvalue.  The untouched-witness
argument behind (5.12), applied to a standard degree-`s` harmonic
depending on `O(s)` witness coordinates, gives

\[
 \widehat\chi_{s,r}^{(q)}=Theta(d)
       \qquad\hbox{uniformly for }1\le s\le c_1k/d,
 \tag{5.22}
\]

where `c_1>0` is a sufficiently small absolute constant; the upper bound
is Cauchy--Schwarz.  Thus there are `Theta(k/d)=Theta(d)` rigorously slow
sectors.  The sharper tail comparison of (5.20) with the benchmark (5.21)
is one finite association-scheme component of the remaining sector proof,
not an assumption hidden in `(ROc)` or `(FE3)`.  Projecting away only stars
is therefore insufficient.  For each actual resource type `T`, write
`mathcal W_T` for the fixed multiset of Johnson states of that type in the
relevant side or union word, and define its exact complete-orbit scalar by

\[
 \widehat\chi_{T,s}={1\over|\mathcal W_T|}
   \sum_{u,v\in\mathcal W_T}
       \phi_s^{(q(T))}\bigl(d_J(S_u,S_v)\bigr).
 \tag{5.23}
\]

This includes all cross-track and cross-half terms; (5.20) is its
single-fresh-path specialization.

### 5.6 The corrected stopped sector row

For a current resource type `T`, extend
`Y_x-bar Y_T` by zero from the live resources to its complete original
Johnson layer and call the resulting mean-zero function `f_(T,i)`.  Put

\[
 s_0(T)=\min\left\{\left\lceil Ck/d\right\rceil,q(T),k-q(T)\right\},
 \qquad
 w_{T,s}(i)\asymp
 {\beta_T(i)\widehat\chi_{T,s}\over\vartheta_s^{(q(T))}},
 \qquad
 \mathcal C_i=
 \sum_T\sum_{1\le s\le s_0(T)}
       w_{T,s}(i)\|\Pi_s^{(q(T))}f_{T,i}\|_2^2.
 \tag{5.24}
\]

Predictable changes of `w_(T,s)` are included in the error below.  The
factor `1/vartheta_s` is forced: a greedy root-removal comparison can
contract sector `s` only at the Bernoulli--Laplace gap scale
`vartheta_s`, whereas the FIFO covariance to be paid is
`widehat chi_(T,s)`.

Write the two positive first-order Dirichlet faces as

\[
 \mathfrak D_i=
 \sum_T\left{
 {\mathfrak G_T(i)\over\beta_T(i)X(i)}
 +{1\over h_iX(i)^2}
   \sum_{A\in\mathfrak A_i}\mu_A
       (K_Tf_{T,i})(A)^2\right},
 \tag{5.25}
\]

with a zero convention when `beta_T=0`, and with union and side incidence
forms, distinguished roots, owner-ledger terms, and marked roots treated
as above.  The precise replacement for `(SG4-false)` is the following
cumulative stopped comparison, with nonnegative predictable injections
`mathcal I_i`:

\[
 \boxed{
 \mathfrak D_i
 \le-\mathbb E[\Delta\mathcal C_i\mid\mathcal F_i]
       +{C\over X(i)}\mathscr L_i+\mathcal I_i,
 \qquad
 \mathcal C_0+\mathbb E\sum_{i<T}\mathcal I_i
                         =O(M/d^4).}
 \tag{JSEC}
\]

For `s<=s_0(T)`, a sufficient proof of `(JSEC)` is a finite list of sector
drift comparisons: covariance at scale `widehat chi_(T,s)` is absorbed by
a counterterm weighted by
`widehat chi_(T,s)/vartheta_s`.  For `s>s_0(T)`, the required assertion is
that the cumulative tail and every sector-mixing error caused by the
stopped residual are included in `sum_i mathcal I_i`; this is the place
where `(ROc)`, `(FE3)`, slot errors, and the owner mixture ledger may be
used.  The complete orbit diagonalizes the pristine operator, but it does
not by itself prove this stopped perturbation statement.

Since `mathcal C_i>=0`, summing `(JSEC)`, using the occupation bound for
`mathscr L_i`, and discarding the terminal counterterm gives `(GDIR)` and
the first-order part of `(HDIR)`.  Multi-hit terms remain `(FE3)`, root
square injection remains `(ROc)`, and the killed-hazard argument then
closes the local transfer.  Conversely, (5.14) and (5.17) show that no
sector-blind version of `(JSEC)` with a constant scalar weight can do so.
The proof of `(JSEC)`, not `(SG4-false)`, is the exact remaining local
analytic gate.

### 5.7 Actual-vector resolvent reduction

There is a sharper route to `(JSEC)` which does not ask for a uniform
operator norm on any `E_s`.  On the pristine complete fibre define

\[
 \mathsf B_T=\sum_{s\ge1}\widehat\chi_{T,s}\Pi_s,
 \qquad
 \mathsf L_T=\sum_{s\ge1}\vartheta_s\Pi_s,
 \qquad
 \mathsf R_T=\mathsf L_T^\dagger\mathsf B_T
       =\sum_{s\ge1}{\widehat\chi_{T,s}\over\vartheta_s}\Pi_s.
 \tag{5.26}
\]

For the **actual predictable vector** `f_(T,i)`, rather than every vector
in the sector, use

\[
             \widetilde{\mathcal C}_i
       =\sum_T\beta_T(i)
          \langle f_{T,i},\mathsf R_Tf_{T,i}\rangle.
 \tag{5.27}
\]

The pristine linear drift is diagonal and the payment identity is exact:

\[
 \langle f,\mathsf R_T\mathsf L_Tf\rangle
                  =\langle f,\mathsf B_Tf\rangle.
 \tag{5.28}
\]

Thus the predictable resolvent cancels the FIFO covariance on the one
vector generated by the process; it never takes a supremum over the
`dim(E_s)` possible directions.

The deterministic high-sector estimate needed for its noise trace is

\[
 0\le\widehat\chi_{T,s}\le C\min\{d,k/s\}.
 \tag{JT}
\]

### Lemma 5.5 (`(JT)` for the macroscopically separated template)

Estimate `(JT)` holds for every fixed macro side word of the template in
the parent note, and hence for the pair/root union covariance after a fixed
change of constant.

#### Proof

Use the standard pure `E_s` witness

\[
 F_s(S)=\prod_{b=1}^s
       \left({\bf1}_{\{a_b\in S\}}-
                    {\bf1}_{\{b_b\in S\}}\right)
 \tag{5.29}
\]

on `2s` distinct coordinates.  Conditional on `F_s(S_0)\ne0`, exactly one
coordinate of each pair lies in `S_0`.  A uniformly chosen distance-`ell`
neighbour deletes an `ell`-subset of `S_0` and inserts an independent
`ell`-subset of its complement.  The product at the neighbour is nonzero
only if the deletion and insertion restrictions choose the same subfamily
of the `s` witness pairs.  For any fixed restriction `A`, the elementary
hypergeometric atom bound gives, uniformly for `ell<=C_0d`,

\[
 \mathbb P\{I\cap W_{\rm out}=A\}
 \le \exp(-c_\epsilon s\ell/k).
 \tag{5.30}
\]

If `|A|=a`, the probability on the left is

\[
 { {k-q-s}\choose{\ell-a}\over {k-q}\choose\ell}.
 \tag{5.31}
\]

To verify (5.30), put `N=k-q` and `mu=s ell/N`.  If
`a>=mu/2`, the probability of including the specified `a` labels is at
most `(2ell/N)^a<=e^{-c mu}`.  If `a<mu/2`, then, after those labels are
included, avoiding the other `s-a` witness labels has probability at most

\[
 \exp\left(-{(s-a)(\ell-a)\over N-a}\right)
                         \le e^{-c\mu};
\]

here `ell=O(d)=o(N)`, while `a<mu/2` implies both
`s-a>=s/2` and `ell-a>=ell/2`.  This proves the atom bound directly from
(5.31).  Averaging over the deletion restriction and retaining the signs
in (5.29) yields

\[
                         |\phi_s^{(q)}(\ell)|
       \le \exp(-c_\epsilon s\ell/k),
                 \qquad \ell\le C_0d.
 \tag{5.32}
\]

Insert (5.32) into (5.20):

\[
 \widehat\chi_{s,r}^{(q)}
 \le 1+C\sum_{j<d}e^{-c_\epsilon sj/k}
 \le C\min\{d,k/s\}.
 \tag{5.33}
\]

For two geodesic tracks based at the same lower header,
`d_J(S_i,T_j)>=|i-j|`; hence (5.32) and summation over diagonals give the
same bound as (5.33).  Distinct owner tails remain at distance `Theta(d)`;
their normalized cross contribution is at most
`C d exp(-c s/d)<=C min{d,k/s}`.  Pairs based at the two different macro
headers have Johnson distance bounded away, by a fixed
multiple of `k`, from both coincidence and complementation.  Repeating the
witness restriction gives `|phi_s|<=e^{-cs}` for every such cross pair;
their `O(d^2)` terms, divided by the `Theta(d)` word length in (5.23), are
also at most `C min{d,k/s}`.  There are constantly many track pairs.  This
proves `(JT)` for one macro side.

For a union of the two potential sides use

\[
 \left(\sum_{x\in E\cup F}f_x\right)^2
 \le2\left(\sum_{x\in E}f_x\right)^2
    +2\left(\sum_{x\in F}f_x\right)^2.
\]

In the pristine complete orbit the two side marginals of the pair/root
weight are transitive copies of the single-side law.  Thus the same bound,
with twice the constant, holds for the union covariance.  \(\square\)

For a fixed marked cluster the stabilizer is smaller, so the last argument
cannot simply be called full Johnson transitivity.  Its anchored analogue
must be replayed over the finite entry patterns of Proposition 6.2; that
marked perturbation is included in `(JRES)` rather than asserted here.

Let `m_s={k\choose s}-{k\choose{s-1}}` be the multiplicity of `E_s` and
`M_q={k\choose q}`.  By `(JT)`, centrality gives

\[
 {1\over M_q}\sum_{s=1}^{\min(q,k-q)}m_s
       {\widehat\chi_{T,s}\over\vartheta_s}=O(1).
 \tag{5.34}
\]

Indeed the sum through `s<=epsilon k/2` is exponentially small even after
the polynomial weight `O(d^3)`, while for `s>=epsilon k/2` the weight is
`O_epsilon(1)`.
The unmarked pristine noise covariance is itself a complete-orbit average
of `O(d)`-supported FIFO words.  By Schur orthogonality, the fraction of a
word's squared norm in sector `s` is `m_s/M_q` times its normalized sector
multiplier; `(JT)` bounds the latter by a polynomial in `d`.  Hence the
total low-sector weighted fraction is exponentially negligible, while on
the remaining sectors the resolvent weight is bounded.  The pristine
carré-du-champ of (5.27) therefore costs only the unweighted
`(ROc)`/`(FE3)` injection scale.  This is a trace calculation, not a union
bound, and it remains valid for an unconditioned equivariant process.

To state exactly what is left, let `mathsf B_(T,i)` and
`mathsf L_(T,i)` be the current stopped incidence covariance and current
linearized root-removal operator, with the same normalizations as (5.26).
After (5.28), every non-noise error is contained in the two actual-vector
forms

\[
 \mathcal E_i^{\rm pert}={1\over X(i)}\sum_T\beta_T(i)
 \left(
  \left|\langle f_{T,i},(\mathsf B_{T,i}-\mathsf B_T)f_{T,i}\rangle\right|
 +\left|\langle f_{T,i},\mathsf R_T
       (\mathsf L_{T,i}-\mathsf L_T)f_{T,i}\rangle\right|
 \right),
 \tag{5.35}
\]

together with the adjoint version for the normalized gradient profile and
the predictable variation of the changing weights `beta_T(i)`.  Therefore
a sufficient, strictly nonuniform replacement for `(JSEC)` is

\[
 \boxed{
 \mathbb E\sum_{i<T}\left(
      \mathcal E_i^{\rm pert}+\mathcal N_i^{\rm noniso}\right)
                         =O(M/d^4),}
 \tag{JRES}
\]

where `mathcal N_i^(noniso)` is the excess resolvent carré-du-champ after
the pristine trace (5.34).  Expanding (5.35) shows a weighted four-edge
selected-relation form.  Its algebraic degree is compatible with the pair
future potential and its square injection with `(FE3)`/`(ROc)`, but the
existing statements do not yet imply `(JRES)`: a Cauchy--Schwarz step
recreates precisely this weighted fourth-order term.  Thus the resolvent
removes the false uniform norm and every sector-dimension union bound, but
does not silently close the adaptive stopped perturbation.

Finally, unconditional exchangeability can justify the trace calculation
after averaging over the whole history.  An arbitrary doublet-closed
stopped prefix need not be exchangeable.  A hereditary proof must either
establish `(JRES)` conditionally after every allowed prefix or charge the
prefix imbalance in the separate cleanup quantifier.

### 5.8 A leave-one-root switch is not an exact martingale identity

It is tempting to condition only on the current resource-deletion set
`D_i` and declare the difference between the stopped operators and their
product-residual expectations to be a martingale.  This is false at the
level needed in (5.35).  Both
`mathsf B_(T,i)-mathsf B_T` and
`mathsf L_(T,i)-mathsf L_T` are `mathcal F_i`-measurable once `D_i` is
fixed.  An `mathcal F_i`-measurable martingale difference has conditional
mean zero only when it vanishes.

There is a literal one-step witness.  Delete one allowed macro word and
consider two surviving Johnson states, one at distance one from a deleted
state and one outside that distance shell.  Their current one-exchange
degrees differ from their pristine degrees by different amounts.  Hence
`mathsf L_(T,i)-mathsf L_T` is not zero on the mean-zero difference of
their point masses; the analogous side-incidence covariance difference is
also nonzero.  A coordinate switch maps this stopped prefix to a different
stopped prefix.  It does not cancel the discrepancy after conditioning on
the first prefix.  For the quadratic actual-vector form, the two switched
values have the same even component, so unconditional orbit averaging does
not turn (5.35) itself into a martingale difference.

Only the **change** of the perturbation admits a Doob decomposition,

\[
                  \Delta\mathcal R_i
          =\Delta\mathcal M_i+\mathcal A_i,
 \qquad
          \mathbb E[\Delta\mathcal M_i\mid\mathcal F_i]=0.
 \tag{5.36}
\]

Its predictable quadratic variation is a resolvent-weighted four-edge
form.  The pair future potential is its unweighted rooted-pair component,
and `(FE3)`/`(ROc)` identify the first collision injections, but they are
not literally equal to the bracket: the weights
`widehat chi_(T,s)/vartheta_s` and the cross-track terms remain.  The exact
leave-one-root version of `(JRES)` is therefore

\[
 \boxed{
 \mathbb E\sum_{i<T}\mathcal A_i^+
   +\mathbb E[\mathcal M]_T^{\rm weighted}
                         =O(M/d^4).}
 \tag{JSW}
\]

This formulation may permit Cauchy--Doob cancellation on the one adaptive
vector, but `(JSW)` is not a consequence of exchangeability alone.  It is
equivalent to proving that the selected-relation future potential controls
the resolvent-weighted compensator and bracket, rather than merely their
unweighted degree-two and degree-three marginals.

## 6. Marked cluster product normalization

Let `A` be a compatible set of `m in {2,3}` marked occurrences on distinct
owner carriers, and put

\[
                         D_A=d_\omega(A).
 \tag{6.1}
\]

The base cluster row gives

\[
                         D_A\le
 \theta\kappa^{m-1}\ell(v(A)).
 \tag{6.2}
\]

For product density `p`, define

\[
 \Gamma_A(p)=D_A^{-2}
 \sum_{E,F\supseteq A}\omega_E\omega_F
 p^{-|((E\cap F)-A)\cap(\mathcal L\dot\cup\mathcal R)|}
 p_s^{-| (E\cap F)\cap([k]\times[L])|}.
 \tag{6.3}
\]

### Proposition 6.1 (exact marked-cluster second moment)

For

\[
                         H_A=p^{m-1}Y_A,
 \tag{6.4}
\]

one has

\[
 \boxed{
 \mathbb E[H_A\mid A\ {\rm live}]=D_A,
 \qquad
 \mathbb E[H_A^2\mid A\ {\rm live}]=D_A^2\Gamma_A(p).}
 \tag{6.5}
\]

#### Proof

The first identity is (2.5) multiplied by `p^(m-1)`.  For the second,
multiply the two compensated edge weights by `p^(2m-2)`.  Conditional on
the `m` live roots, every additional common non-slot in `E,F` leaves one
factor `p^-1`, and every common slot leaves `p_s^-1`; all other survival
factors cancel.  Summation gives (6.5).  \(\square\)

### Proposition 6.2 (cluster-rooted FIFO closure)

For every compatible marked `A` of size two or three,

\[
 \boxed{
                         \Gamma_A(p)=O(1)}
 \tag{6.6}
\]

uniformly for `p>=c/d`.

#### Proof

Fix the roles of the marked occurrences in the at most two constituent
macros.  Conditioning on `A` fixes only a constant number of level-two
owner states and port labels.

* On a track already anchored by `A`, remaining common states of two
  completions have the synchronized-chain moment of Lemma 5.8 with a
  constant number of prescribed levels.  Splitting at those levels only
  replaces `d` by positive subinterval lengths; the composition proof is
  unchanged.
* On first entry into any additional lower or owner track, its private
  visible block is still chosen from a `Theta(d^2)` pool.  The conditioning
  fixes one ambient state, but every additional marked state differs from
  its header in only `O(d)` labels; within each membership shore the
  remaining coordinate pool is still `Theta(d^2)`.  Lemma 5.9 and
  `(MT1)`--`(MT2)` therefore
  give the same bounded product of entry factors.
* If the marked states force the private split, the lower/owner,
  owner/owner, and visible-singleton cases are respectively `(MT3)`,
  `(MT4)`--`(MT5)`, and the fan calculation `(TF1)`--`(TF3)`.
* If one macro half is not rooted by `A`, rigid same-base and cross-half
  coincidences retain the `exp[-Omega(k)]` reserve of Propositions
  5.6--5.7.  If `A` roots both halves, it uses at most three level-two
  states in total.  In the normal form
  `T_2^c=H union(R_c-{x_2^c})`, two states in one half determine at most
  `H union {a}`; the missing heads, the remaining `(d-2)!` queue orders,
  and the lower continuation banks remain.  Their normalized overlap is
  exactly the anchored chain/private-split moment in the preceding bullets,
  so no macroscopic-header factor is being assumed in this subcase.

There are constantly many marked role patterns because `m<=3` and
`h<=3`.  The entropy factors used in (6.2) occur in both numerator and
`D_A^2` and cancel under this conditional normalization.  The remaining
track moments multiply to `O(1)`, proving (6.6).  Slot intersections are
negligible as in Proposition 5.3.  \(\square\)

## 7. Marked first-two-hit normalization

For `E,F` through `A`, put

\[
 m_A(E,F)=|((E\cap F)-A)\cap
                      (\mathcal L\dot\cup\mathcal R)|,
 \qquad
 j(G;E,F)=|G\cap(E\cup F)\cap
                      (\mathcal L\dot\cup\mathcal R)|.
 \tag{7.1}
\]

Define

\[
 \begin{aligned}
 \mathcal F_{3,A}(p_*)={}&
 \sum_{E,F\supseteq A}\sum_G
 \omega_E\omega_F\omega_Gp_*^{-m_A(E,F)}\\
 &\hspace{25mm}\cdot {j(G;E,F)\choose2}K_{p_*}(j(G;E,F)).
 \end{aligned}
 \tag{7.2}
\]

### Proposition 7.1 (cluster-rooted first-two-hit closure)

Uniformly for compatible marked `A` of size two or three,

\[
 \boxed{
 \mathcal F_{3,A}(p_*)
 \le {C\over d}D_A^2\Gamma_A(p_*).}
 \tag{7.3}
\]

#### Proof

Expand the binomial coefficient by choosing the first two resources
`x,y` where `G` meets `E union F`.  There are `O(d^2)` role pairs and
`d_omega(x,y)=O(d^-3)`, giving `O(1/d)`.  Conditional on those anchors and
on `A`, (FE3.5) turns the remaining kernel into a fugacity moment for
further intersections.  Proposition 6.2's anchored-track exposure bounds
that moment by a constant.  Forced splits, fans, rigid bases, cross-half
entries, and slots use the same exceptional estimates listed in its proof.
Summing the normalized `E,F` mass gives
`D_A^2Gamma_A(p_*)`, proving (7.3).  \(\square\)

Thus no marked size-two/three static normalization remains open.  Their
dynamic processes `p^(m-1)Y_A` have ideal root-survival factor `rho_i^m`
and enter the same killed-hazard argument.  Their remaining dynamic issue
is again the stopped Johnson-sector transfer `(JSEC)`, now with an
exponentially smaller initial mass.

## 8. Proof-safe boundary

The direct joint Lyapunov succeeds through every term of degree at most
three in the macro weights:

* root means and global rate are exact double counts;
* centered root future energy is nonnegative and has one-root survival
  drift;
* pair future energy has two-root survival drift;
* `(ROc)` and `(FE3)` identify the degree-two and degree-three injections;
* the killed-hazard Hardy lemma removes accumulated service logarithms;
* marked clusters of sizes two and three have bounded rooted normalization
  and the same first-two-hit gain.

The remaining normalized incidence-gradient/squared-hazard operator is
degree four.  No identity in the present notes reduces its slow Johnson
sectors to `(ROc)` or `(FE3)`, and the scalar row `(SG4-false)` is refuted
by (5.14) and (5.17).  The pristine unmarked sector tail `(JT)` and its
dimension-free trace are closed, but the adaptive resolvent perturbation
`(JRES)`--`(JSW)` (including the anchored marked version) is not.  Therefore
the balanced-doublet packing theorem is still conditional on this adaptive
part of `(JSEC)`, together with the already stated prefix-uniform cleanup
and global component-connectivity rows.
