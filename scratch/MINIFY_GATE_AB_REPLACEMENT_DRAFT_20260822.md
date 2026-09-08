# Rigorous Gate-A/Gate-B minification draft

This is an editing aid for `MASTER_HANDOFF.md`, not a new mathematical
source.  It records (i) the dependency audit and (ii) compact standalone
replacement text for the parts of Appendices G and H that later retained
results actually use.  Equation numbers are local to this draft.

## 1. Dependency audit and recommended disposition

### Gate A

Retain, possibly after local compression:

* C.4 (cluster drift) and C.5 (one-cap stopped descent);
* C.7 (global boundary codegrees) and C.8 (the directed punctured
  catalogue/profile);
* the rooted boundary-polymer estimate inside C.3, and the fixed
  twelfth-moment specialization of C.3bis;
* G.1 (the conditional one-sided twelfth-moment/purge closure theorem);
* G.14, G.15, G.18, and G.19 (the present product-reference frontier).

Replace G.2--G.11 by the compact Palm/finite-bite bridge in Section 2
below.  Delete G.12--G.13 (counterexamples whose only live lesson is that
generic monotonicity and fixed-carrier FKG do not settle the between-carrier
term).  Delete G.16--G.17: G.18 recombines their two nested covariances into
one ordered-pair covariance and is algebraically stronger.  Delete the
unnumbered opening of G (the companion/pair-square alternative) if G.1 is
declared the sole Gate-A closure route.  C.2, the variance-only part of
C.3, C.3ter, C.3quater, C.6, C.12, and C.12a are not premises of this
route and may be archived.

Dependency warning: G.19.3 is currently attributed to C.1, but its rooted
kernel estimate uses the component-through-a-fixed-root argument printed in
C.3.  Do not delete that argument.  It can be retained as the following
single lemma (with `a=x^{-c}-1`):

\[
 \max_{F\ni v}{1\over D}\sum_{G\ne F}
       (x^{-c|(F\cap G)-\{v\}|}-1),\quad
 \max_{F\ni v}{1\over D}\sum_{\substack{G\ne F\\
                  |(F\cap G)-\{v\}|>0}}
       x^{-c|(F\cap G)-\{v\}|}
 =O_c\!\left({1\over rx^{3c}}+{1\over r^2x^{4c}}\right).
\]

The proof is the rooted component decomposition from C.3: the component
through the boundary edge of `v` contributes
`O(z/r+z^3/r+z^4/r^2)`, other components multiply it by
`exp(O(z/r+z^4/r^2))`, and `z=O_c(x^{-c})`.

### Gate B

Retain:

* C.9 (the `x=o(r^{-1/3})` occurrence-capacity threshold), C.10 (positive
  fractional cover and cheap integral rounding), and the exact protection
  identity C.13.16--C.13.19 if the stopped-hole formulation is kept;
* H.11 (sixteen local atoms), H.14 (uniform all-depth local conditioning),
  and H.15 (shore-difference remote cone);
* the newer near--far determinant/Venn-gap theorem
  `MATH_THEOREM_GATE_B_J2_NEAR_FAR_CUMULANT_AND_VENN_GAP_LOCALIZATION_20260822.md`
  in place of H.16.

Replace H.1--H.10 by the compact compensated zero-avoidance setup in
Section 3 below.  Delete H.2 (finite `r=4,5` calibration), H.4/H.4a and
H.5--H.7 (the superseded `W_2` perturbation branch), H.12--H.13 (fixed
`j=2,3` predecessors of H.14), and H.16 after the near--far theorem is
integrated.  C.11 may be reduced to its one-paragraph no-go conclusion;
C.14 may be reduced to the inequalities `K>=Omega(1/x)` and
`D(pi||u)>=Omega(log(1/x))`; C.15--C.16 are unsuccessful mechanism
diagnostics and need not remain in the authoritative proof chain.

Dependency warnings:

1. H.10 currently imports the boundary events and norm identities H.82,
   H.83, H.87, and H.93 from H.8.  Section 3 below restores them.
2. H.16 currently imports the finite-cell formula H.114--H.115 from H.12.
   H.12 may be removed only after replacing H.16 by the self-contained
   near--far theorem, which restates that formula.
3. H.11 and H.15 use C.7 and the polymer enumeration from C.1.  Those two
   inputs must remain.

## 2. Standalone replacement: exact Palm recursion and finite bites

The purpose of this block is only to connect G.1 to the product-reference
objects in G.14--G.19.  It contains no unproved mixing assertion.

Fix a shore `V` in a finite simple hypergraph state `H`, and fix an integer
`m>=2` (Gate A uses `m=12`).  A rooted ordered carrier is

\[
 \gamma=(v;F_1,\ldots,F_m),\qquad
 v\in V,\quad F_i\ne F_j,\quad v\in F_i.
\]

For a residual state `S`, write `d_S(v)` for the root degree and put

\[
 t(S)=\sum_{v\in V}(d_S(v))_m,
 \qquad F_c(S)=\sum_{v\in V}(d_S(v)-c)_+^m,
\]
\[
 \varphi_c(d)=
 \begin{cases}(d-c)_+^m/(d)_m,&d\ge m,\\0,&d<m,
 \end{cases}
 \qquad c\ge m-1.                                      \tag{A.1}
\]

For a nonzero finite measure `nu` on residual states with `nu(t)>0`, its
carrier Palm law is

\[
 \widehat\nu(S,\gamma)=
 {\nu(S){\bf1}_{\{\gamma\text{ alive in }S\}}\over\nu(t)}.
\]

Counting the `(d_S(v))_m` ordered carriers at each root gives the exact
identity

\[
 A_c(\nu):={\nu(F_c)\over\nu(t)}
           =\mathbb E_{\widehat\nu}\varphi_c(d_S(v)).       \tag{A.2}
\]

Let `P` be any deletion-only sub-Markov kernel, including a stopping
indicator.  For a current carrier state `x=(S,gamma)`, define

\[
 a(x)=\sum_{S'}P(S,S')\mathbf1_{\{\gamma\text{ alive in }S'\}},
\]
\[
 e_c(x)=\sum_{S'}P(S,S')\mathbf1_{\{\gamma\text{ alive in }S'\}}
       \{\varphi_c(d_S(v))-\varphi_c(d_{S'}(v))\}.          \tag{A.3}
\]

Whenever both carrier masses are positive,

\[
 \boxed{A_c(\nu P)=
 {\mathbb E_{\widehat\nu}[a\varphi_c-e_c]
       \over\mathbb E_{\widehat\nu}a}},                  \tag{A.4}
\]
and therefore

\[
 \boxed{A_c(\nu P)-A_c(\nu)=
 {\operatorname {Cov}_{\widehat\nu}(a,\varphi_c)
       -\mathbb E_{\widehat\nu}e_c
       \over\mathbb E_{\widehat\nu}a}.}                  \tag{A.5}
\]

Indeed, terminal alive carriers have unique labelled parents, so the
terminal carrier mass divided by the initial carrier mass is `E a`.
Summing the terminal test over those carriers gives
`E(a varphi_c-e_c)`, which proves (A.4); centering proves (A.5).

The erosion term is nonnegative.  For `d>c`,

\[
 {\varphi_c(d+1)\over\varphi_c(d)}
 =\left(1+{1\over d-c}\right)^m{d-m+1\over d+1}\ge1,       \tag{A.6}
\]

because Bernoulli's inequality and `c>=m-1` give
`(1+1/(d-c))^m >= 1+m/(d-m+1)=(d+1)/(d-m+1)`.
Deletion cannot increase `d`, hence `e_c>=0`.  Thus survival selection is
the only sign-indefinite term in (A.5).

For a reference pair `(lambda,U)`, define `Delta` and `Delta^0` to be the
right side of (A.5) for `(nu,P)` and `(lambda,U)`, respectively, before
adding `A_c` itself.  If the four adjacent scalars are positive, then

\[
 {A_c(\nu P)/A_c(\lambda U)\over A_c(\nu)/A_c(\lambda)}
 ={1+\Delta/A_c(\nu)\over1+\Delta^0/A_c(\lambda)}.          \tag{A.7}
\]

Consequently, for a fixed terminal cutoff `c`, put
\(A_{j,c}=A_c(\nu_j)\) and \(B_{j,c}=A_c(\lambda_j)\).  Iteration is
exact:

\[
 \log{A_c(\nu_J)\over A_c(\lambda_J)}
 =\log{A_c(\nu_0)\over A_c(\lambda_0)}
 +\sum_{j<J}\left[
  \log\!\left(1+{\Delta_{j,c}\over A_{j,c}}\right)
 -\log\!\left(1+{\Delta^0_{j,c}\over B_{j,c}}\right)
 \right].                                                  \tag{A.8}
\]

Zero reference tail is harmless: full support and nonnegativity make
`F_c` identically zero on that reference slice.  Formula (A.8), with one
fixed `c` while telescoping backward, is the exact stopped scalar
comparison; it neither assumes nor requires full-state likelihood
domination.

We next remove the infinitesimal-bite fiction.  In a deterministic state
put

\[
 \Gamma(F)=\{G:G\cap F\ne\varnothing\},\qquad
 B(\gamma)=\bigcup_{i=1}^m\Gamma(F_i),\qquad
 h(\gamma)=|B(\gamma)|,
\]
\[
 \Delta_C=\max_F|\Gamma(F)|.
\]

Mark every row independently with probability `p` and accept exactly the
isolated marks.  If `a_p(gamma)` is the probability that the carrier
survives, then

\[
 \boxed{a_p(\gamma)=1-ph(\gamma)+r_p(\gamma),\qquad
 0\le r_p(\gamma)\le\left({m^2\over2}+m\right)
                         (p\Delta_C)^2.}                    \tag{A.9}
\]

If no member of `B(gamma)` is marked, the carrier survives, and
`0<=(1-p)^h-(1-ph)<=binom(h,2)p^2`.  Any additional survival has a marked
row in `B(gamma)` that is rejected by a distinct marked conflict
neighbour.  The ordered-pair union bound is at most
`p^2 h Delta_C`; since `h<=m Delta_C`, (A.9) follows.

Let `Delta` bound `Delta_C` on the support of the current law and assume
`p Delta` is a sufficiently small constant.  Substitution of (A.9) in
(A.5), use of `e_c>=0`, and
`|Cov(r_p,varphi_c)|<=2||r_p||_infty A_c` give

\[
 \boxed{
 \log{A_c(\nu P_p)\over A_c(\nu)}
 \le -p{\operatorname {Cov}_{\widehat\nu}(h,\varphi_c)
             \over A_c(\nu)}+C_m(p\Delta)^2.}              \tag{A.10}
\]

If \(p_j\Delta_j\le C\varepsilon\) for every microbite and their number is
at most \(C r\log r/\varepsilon\), then

\[
 \sum_j(p_j\Delta_j)^2=O(\varepsilon r\log r)
                        =o(r^{-1-\alpha}).                  \tag{A.11}
\]

The last equality holds under
\(\varepsilon=o(r^{-2-\alpha}/\log r)\).  More generally the exact
finite-bite budget is \(\sum_j(p_j\Delta_j)^2\); no constant-rate or
stopped-mixing assertion is hidden here.

The actual clock may choose its marking probability predictably from the
current state.  If the state is \(S\), write \(p=p(S)\), put

\[
 \theta=\sup_Sp(S)\Delta_C(S),\qquad
 s(S,\gamma)=p(S)h(S,\gamma),                              \tag{A.11a}
\]

and assume \(\theta\) is a sufficiently small constant depending only on
\(m\).  Applying (A.9) conditionally on \(S\) gives
\(a=1-s+r\), \(0\le r\le C_m\theta^2\).  Repeating the proof of
(A.10), without taking \(p\) outside the Palm expectation, yields

\[
 \boxed{
 \log{A_c(\nu P_{p(\cdot)})\over A_c(\nu)}
 \le-{\operatorname {Cov}_{\widehat\nu}(s,\varphi_c)
              \over A_c(\nu)}+C_m\theta^2.}                 \tag{A.11b}
\]

Thus the live regression variable is the weighted hazard \(p(S)h\), not
the unweighted hazard with \(p\) replaced by a constant.  In particular,
conditioning first on the root degree gives the literal profile
\(\zeta_s(d)=\mathbb E_{\widehat\nu}[p(S)h\mid d_S(v)=d]\).
Along a varying schedule, its remainder is the sum of the corresponding
\(\theta_j^2\).

Finally, exact shore sizes introduce no fibre-probability penalty.  Let
`N_j` be the vector of actual shore sizes with law `w_j`, let
`lambda_n` be uniform on the slice of size vector `n`, and put

\[
 \Lambda_j=\sum_nw_j(n)\lambda_n.
\]

If `kappa_j(n,n')` is the actual joint law of successive size vectors and
`K_j(n,n')=kappa_j(n,n')/w_j(n)`, define, for `S` in the `n`-slice,

\[
 U_j(S,S')=\sum_{n'\le n}K_j(n,n')
 {\mathbf1_{\{S'\subseteq S,\ |S'|=n'\}}
       \over\prod_\sigma {n_\sigma\choose n'_\sigma}}.     \tag{A.12}
\]

Double counting nested pairs proves

\[
                         \boxed{\Lambda_jU_j=\Lambda_{j+1}.} \tag{A.13}
\]

Moreover, for nonnegative observables `F,t`, with `F=0` on every
positive-mass zero-`t` fibre,

\[
 {\mathbb E_{\Lambda_j}F\over\mathbb E_{\Lambda_j}t}
 \le\sup_{n:w_j(n)\mathbb E_{\lambda_n}t>0}
 {\mathbb E_{\lambda_n}F\over\mathbb E_{\lambda_n}t}.     \tag{A.14}
\]

This is just a weighted average of the fibrewise ratios with weights
`w_j(n) E_(lambda_n)t`.  Hence every uniform exact-slice estimate in a
density bin passes to the random-size reference mixture without division
by a small size probability.

For completeness, let \(r_\sigma\in\{0,1\}\) indicate whether the carrier
root lies on shore \(\sigma\).  If a carrier footprint uses
\(b_{\gamma,\sigma}\) nonroot targets on that shore, then, conditional on
retaining the root target, the exact nested-slice survival factor is

\[
 \prod_\sigma{(n'_\sigma-r_\sigma)_{b_{\gamma,\sigma}}
                   \over(n_\sigma-r_\sigma)_{b_{\gamma,\sigma}}}.
                                                                  \tag{A.15}
\]

Without conditioning on the root, multiply (A.15) by the common factor
\(\prod_\sigma(n'_\sigma/n_\sigma)^{r_\sigma}\).  For a fixed root shore
this factor is independent of the carrier label and cancels from every
Palm ratio used here.

Put \(N_\sigma=n_\sigma-r_\sigma\) and
\(N'_\sigma=n'_\sigma-r_\sigma\).  When
\(\delta_\sigma=1-N'_\sigma/N_\sigma\le1/4\) and
\(b_{\gamma,\sigma}\le N_\sigma/2\), termwise expansion of
\(\log(1-z)\) gives

\[
 \log{(N'_\sigma)_{b_{\gamma,\sigma}}
             \over(N_\sigma)_{b_{\gamma,\sigma}}}
 =-b_{\gamma,\sigma}\delta_\sigma
 +O\!\left(b_{\gamma,\sigma}\delta_\sigma^2+
   {b_{\gamma,\sigma}^2\delta_\sigma\over N_\sigma}\right).
 \tag{A.16}
\]

The logarithm of (A.15) is the sum of (A.16) over the shores.

At the punctured scale \(b_{\gamma,\sigma}=O_m(r)\), shore sizes are
exponential, and \(\delta_\sigma=O(\varepsilon/r)\), so (A.16) is
\(O_m(\varepsilon)\), while its displayed remainder is
\(O_m(\varepsilon^2/r)+e^{-\Omega(r)}\). Accepted-count concentration is
the separate theorem in Appendix C.5.

Equations (A.2)--(A.16) are the complete bridge needed by G.1.  Under the
independent product reference, conditioning on a fixed labelled carrier
leaves independent target indicators.  Both its live conflict hazard `h`
and the degree-tail test are increasing, so Harris association makes the
within-carrier covariance favorable.  The only possible adverse reference
term is therefore the between-carrier covariance.  G.14 rewrites that
term as the tail tilt of the signed connected statistic
`q_0 Xi_gamma^circ`; G.15 decomposes it into carrier U-statistics; G.18
gives the exact two-shore cell determinant for `s=2`; and G.19 localizes
the factorial pair law.  What remains open is exactly:

1. cutoff-tail leakage and kernel-weighted uniform integrability outside
   the disjoint overlap cell;
2. the signed dominant-cell determinant and the signed `s=3,...,12`
   remainder;
3. the stopped twelfth-moment comparison (G.29), with
   \(\kappa<2-20\alpha\) for the present shore ledger; and
4. actual/reference survival-payoff and realized-center comparison, plus
   the purge/cemetery ledger, within the exponent budget of G.2.

## 3. Standalone replacement: compensated zero-avoidance setup

This block contains the definitions and norm bridge imported by H.11,
H.14, H.15, and the near--far theorem.  It does not assert stopped
stability or hole alignment.

Put

\[
 b=2r+1,
 \qquad E(w)=\{(M,I_r^w(a)):a\ne0\}
       \mathbin{\dot\cup}\{(L,I_{r-1}^w(a)):a\ne0\},       \tag{B.1}
\]

where `w` ranges over `S_b` and starts are cyclic.  The alternating tagged
containment path recovers `w`, so the complete directed-punctured catalogue
is a free transitive `S_b`-set.

Let every row have `k_sigma=2r` targets on shore `sigma`.  For a rate law
`lambda` on rows define

\[
 q_v=\sum_{G\ni v}\lambda_G,
 \qquad
 P_{vG}={1\over d(v)}\sum_{F\ni v}(|F\cap G|-1)_+.          \tag{B.2}
\]

Assume the load is constant on each shore, so \(q_v=q_\sigma\) for
\(v\in V_\sigma\).  The identity
`1_(|F cap G|>0)=|F cap G|-(|F cap G|-1)_+` shows that the
first-order logarithmic erosion of the degree at `v in V_sigma` is

\[
 e_v=\sum_\tau k_\tau q_\tau-q_\sigma-\sum_GP_{vG}\lambda_G.
                                                                  \tag{B.3}
\]

Indeed the first two terms count the expected total row load meeting a
uniform row through `v`, with the root incidence removed, and the last
term corrects multiple intersections.  Thus preserving target loads and
rooted exposures is the linear constraint

\[
 B\lambda=B\lambda^0,
 \qquad B=[A;P],                                          \tag{B.4}
\]

where `A` is target incidence and `lambda^0` is a positive baseline.
The compensated polytope is nonempty because it contains `lambda^0`.

For any row objective `f`, the entropy-regularized optimizer

\[
 \lambda^\theta=\arg\max_{\lambda\ge0,\ B\lambda=B\lambda^0}
 \{\theta f\cdot\lambda-D(\lambda\Vert\lambda^0)\}       \tag{B.5}
\]

is unique.  Differentiating the Lagrange equations at zero gives

\[
 {\dot\lambda_G\over\lambda_G^0}=f_G+(B^{\mathsf T}\xi)_G,
 \qquad B\dot\lambda=0,
\]
and hence

\[
 {d\over d\theta}f\cdot\lambda^\theta\big|_{0}
 =\sum_G{\dot\lambda_G^2\over\lambda_G^0}\ge0,           \tag{B.6}
\]

with equality exactly when `f` lies in the row space of `B`.  This is the
precise compensated-switching criterion.

The physical collision objective also has an exact finite-cell form.  At
one external rank let `X(T)` be the row degree of target `T`, let

\[
 Z=|\mathcal C|,\qquad S=\sum_TX(T)^2,
 \qquad \mathcal K={NS\over b^2Z^2}.
\]

Deleting a cell `mathcal B_G` of size `C_G`, with
`Y_G(T)=|mathcal B_G cap mathcal S(T)|`,
`R_G=sum_T X(T)Y_G(T)`, and `Q_G=sum_TY_G(T)^2`, gives

\[
 {\mathcal K'\over\mathcal K}
 ={1-2R_G/S+Q_G/S\over(1-C_G/Z)^2}.                         \tag{B.7}
\]

This follows by substituting `X'=X-Y_G` and `Z'=Z-C_G`.
Consequently any predictable row law turns the logarithm of the right side
minus its predictable mean into a stopped martingale, stopped before a
denominator vanishes.  This identity makes no assertion about a support
chosen from terminal holes; Appendix C.13 gives the exact fixed-target
protection martingales used for that purpose.

We now state the relative-current norm in which a polynomial inverse is
possible.  Put

\[
 k=r-2,\qquad \ell=b-k=r+3,\qquad N={b\choose k},
 \qquad p={b\over N}.                                      \tag{B.8}
\]

For a `k`-set `T`, let `q_T(w)` indicate that `T` is a full cyclic
`k`-window of `w`, and define

\[
 (\widehat Sf)(T)=p^{-1}\mathbb E_{w\in S_b}[f(w)q_T(w)].  \tag{B.9}
\]

The permutation module on `k`-sets decomposes multiplicity-freely as

\[
 \mathbb R^{{[b]\choose k}}
 =\bigoplus_{j=0}^k V_{(b-j,j)}.                            \tag{B.10}
\]

One elementary proof maps each `j`-set to the sum of its containing
`k`-sets.  The nested images have successive dimensions
`binom(b,j)-binom(b,j-1)`; polytabloid differences give nonisomorphic
irreducible two-row modules and the dimensions telescope.

On the block `V_j=V_(b-j,j)`, the compensated constraints contribute at
most four multiplicity vectors (the two incidence and two exposure
orbits), while the rank-`k` current contributes one.  Let
`widehat sigma_(r,j)` be the constrained singular value of (B.9).
The following standard matrix-coefficient lemma converts it to a
coordinatewise rate perturbation.  If `V` is a real orthogonal irreducible
of dimension `d`, `End_G(V)=R`, and an equivariant map acts by
`Phi(v tensor u) -> <a,u>v`, then for any allowed current `J`,

\[
 f_J=\Phi\!\left(J\otimes{P_Ka\over\|P_Ka\|^2}\right),
 \quad Af_J=J,
 \quad \|f_J\|_\infty\le{\sqrt d\over\|P_Ka\|}\|J\|_2. \tag{B.11}
\]

Here `K` is the orthogonal complement of the constraint vectors.  To
prove the norm formula, average `guu'^Tg^-1` over the group; Schur's lemma
makes it `d^-1<u',u>I`, whence
`Phi(v tensor u)(g)=sqrt(d)<v,gu>` is an isometry and has the displayed
supremum bound.  The real endomorphism condition holds for two-row Specht
modules by complexification.  Since
`dim V_j<=binom(b,j)<=N`, a lower bound

\[
                         \widehat\sigma_{r,j}^2\ge Nr^{-C} \tag{B.12}
\]

gives a polynomial `L^infty` right inverse on that block.  Orthogonal
blocks may be solved separately and their bounds summed.  This conclusion
is for one rank; coinstantiation of several depths is a separate theorem.

For precision, let \(m_{r,j}\) be the rank-\(k\) current vector in this
multiplicity block and let \(K_{r,j}\) be the orthogonal complement of the
four constraint vectors.  Define the squared constraint angle and the
unconstrained relative orbit factor by

\[
 \alpha^{(e)}_{r,j}={\|P_{K_{r,j}}m_{r,j}\|^2\over\|m_{r,j}\|^2},
 \qquad
 \Theta_{r,j}=\text{the squared singular value of }\widehat S
 \text{ before imposing the constraints}.                       \tag{B.12a}
\]

The multiplicity-one form used in (B.11) gives exactly

\[
                 \widehat\sigma_{r,j}^2
                 =\alpha^{(e)}_{r,j}\Theta_{r,j}.                 \tag{B.12b}
\]

Indeed the unconstrained and constrained singular values in the block are
respectively \(\|m_{r,j}\|\) and \(\|P_{K_{r,j}}m_{r,j}\|\), with the
same orbit normalization.  Thus (B.12b) is a definition-free consequence
of orthogonal projection, not an additional representation-theoretic
hypothesis.

The four vectors just named are exactly the harmonic images of the row
constraints in (B.4), not merely analogous profiles.  In the complete
catalogue put

\[
 D(F,G)=(|F\cap G|-1)_+.
\]

The incidence row of a target \(v\) is
\(a_v(G)=\mathbf1_{\{v\in G\}}\),
and its rooted-exposure row is

\[
 P_{vG}=d(v)^{-1}(a_vR_D)(G),
\]

where \(R_D\) is right convolution by \(D\).  Simultaneous relabelling
commutes with \(R_D\).  On a two-row Specht block the permutation module of
each shore has multiplicity one, so the two incidence orbits and the two
exposure orbits have harmonic profiles
\(c_r,c_{r-1},e_r,e_{r-1}\), respectively, up to their nonzero constant
degree normalizations.  Hence their span is exactly the restriction of
\(\operatorname {row}B\) to that block, including when some displayed
vectors are dependent.  Therefore the \(\alpha^{(e)}_{r,j}\) used below is
the compensated angle required by (B.6), and a nonzero zero-avoidance
residual really does produce a feasible compensated switching direction.

It remains to express the full exposure singular value through zero
avoidance.  Put

\[
 X=\{I_r(u),I_{r-1}(u):u\in\mathbb Z_b\},
 \quad A_0=I_r(0),\quad B_0=I_{r-1}(0),\quad E_0=X-\{A_0,B_0\}.
\]

For a configuration \(F\), let \(F_s\) be its set of tagged rank-\(s\)
targets.  For a rank-\(s\) target \(S\), \(s\in\{r,r-1\}\), define

\[
 d_s(S)=|\{F:S\in F_s\}|,
 \quad W_{1,s}(S)=\sum_{T\in E_0}\deg(S,T),
\]
\[
 e_s(S)=\sum_{F:S\in F_s}(|F\cap E_0|-1)_+,
 \quad Z_s(S)=|\{F:S\in F_s,\ F\cap E_0=\varnothing\}|.   \tag{B.13}
\]

The integer identity `(t-1)_+=t-1+1_(t=0)` gives

\[
                         \boxed{e_s=W_{1,s}-d_s+Z_s.}       \tag{B.14}
\]

Inclusion--exclusion gives the exact blocker expansion

\[
 Z_s(S)=\sum_{J\subseteq E_0}(-1)^{|J|}\deg(S,J),           \tag{B.14a}
\]

where \(\deg(S,J)\) counts configurations whose shore-\(s\) target is
\(S\) and which contain every tagged blocker in \(J\).  A blocker is an
edge of the boundary graph representing one target; \(V(J)\) denotes the
set of boundary cuts incident with its blocker edges.

Fix \(2\le j\le k\) disjoint ordered coordinate pairs `(a_i,b_i)` and put

\[
 H_{s,j}(S)=\prod_{i=1}^j
 (\mathbf1_{\{a_i\in S\}}-\mathbf1_{\{b_i\in S\}}).      \tag{B.15}
\]

For \(K_t=I_k(t)\), let \(\mathcal B_t\) be the ordered injective placements of
the `2j` distinguished labels in which pair one occupies the boundary edge
`(t-1,t)`, pair two occupies `(t+k-1,t+k)`, and every remaining pair has
one endpoint in `K_t-{t,t+k-1}` and the other in its complement after the
two boundary positions are removed.  Either orientation is allowed.  Then

\[
 |\mathcal B_t|=2^j(k-2)_{j-2}(\ell-2)_{j-2}.              \tag{B.16}
\]

The events are disjoint, because pair one's undirected edge determines
\(t\).  Complete a placement \(z\) arbitrarily to a permutation; every
quantity below depends only on the distinguished positions and is therefore
independent of that completion.  Put

\[
 q(z)=\sum_{u\in\mathbb Z_b}H_{k,j}(zI_k(u)),\qquad
 c_s(z)=\sum_{u=1}^{b-1}H_{s,j}(zI_s(u)).
\]

If \(\varepsilon(z)=H_{k,j}(zK_t)\), the two forced boundary pairs imply

\[
 q(z)=\varepsilon(z),\qquad c_r(z)=c_{r-1}(z)=0,           \tag{B.17}
\]

where \(q\) is the rank-\(k\) cyclic current and \(c_s\) is the central incidence
current: a cyclic interval splitting both forced pairs must use their two
boundary edges, and the two intervening arcs have unequal lengths `k` and
`ell`.

For any coefficient vector `x(S)`, write its signed boundary profile as

\[
 \omega_x(t)={1\over|\mathcal B_t|}
 \sum_{z\in\mathcal B_t}\epsilon(z)
       \sum_Sx(S)H_{s,j}(zS).                              \tag{B.18}
\]

The complete-catalogue degree vector \(d_s\) is constant, so its
\(j\ge2\) harmonic profile is zero.  For each single central target
\(T\in E_0\), the profile of \(S\mapsto\deg(S,T)\) is also zero.  If the
two positions on either forced event
edge have equal membership in `T`, transpose them: the degree constraint
is fixed and the harmonic sign reverses.  Otherwise `T` would split both
event edges, making them its two boundaries and forcing its size to be
`k` or `ell`, not `r` or `r-1`.  Hence (B.14) gives

\[
                         \boxed{\omega_{e_s}(t)=\omega_{Z_s}(t).} \tag{B.19}
\]

Write \(z_s(t)=\omega_{Z_s}(t)\) and

\[
 \rho^{(0)}_{r,j}={1\over b}\min_{x,y}
 \sum_{t\in\mathbb Z_b}(1-xz_r(t)-yz_{r-1}(t))^2.         \tag{B.20}
\]

Jensen's inequality on the disjoint boundary events gives the full
exposure angle bound

\[
 \alpha^{(e)}_{r,j}\ge
 {\rho^{(0)}_{r,j}\over b\,k(k-1)\ell(\ell-1)}.           \tag{B.21}
\]

For clarity, divide the event probability (B.16) by the one-window
harmonic norm

\[
 \kappa_{k,j}={2^j(k)_j(\ell)_j\over(b)_{2j}}.
\]

On `mathcal B_t` the squared cyclic current equals one.  Therefore its
relative orbit factor satisfies

\[
 \Theta_{r,j}\ge
 {N\over b^2k(k-1)\ell(\ell-1)}.                          \tag{B.22}
\]

Multiplying (B.21)--(B.22) yields the exact scale needed in (B.12):

\[
 \boxed{\widehat\sigma_{r,j}^2
 =\alpha^{(e)}_{r,j}\Theta_{r,j}
 \ge {N\rho^{(0)}_{r,j}\over
 b^3[k(k-1)\ell(\ell-1)]^2}.}                             \tag{B.23}
\]

Thus a uniform polynomial lower bound on the zero-avoidance residual
`rho^(0)_(r,j)` supplies a polynomial coordinatewise compensated inverse
at that depth.  No `W_2` approximation is needed.

Finally, inclusion--exclusion for `Z_s` is organized by the boundary
graph.  Multiplication of cut positions by `-2 mod b` sends central window
boundaries to

\[
 B_r=\operatorname {Cay}(\mathbb Z_b,\{\pm1,\pm3\}),       \tag{B.24}
\]

with the two start-zero edges punctured; the two boundary-event roots may
be placed at `0,5`.  H.11 enumerates the sixteen four-cut local atoms in
this graph.  H.14 proves that their two shore columns have a uniform
all-`j` polynomial inverse.  H.15 controls the remote transverse shore
direction.  H.16 proves a Venn-gap localization theorem for one-edge
extensions of every fixed \(O(1)\) rooted-core family.  A fully certified
near--far determinant after the rootless dressing remains part of the
open gate.

The exact remaining Gate-B assertions are not hidden by this setup:

1. prove a nonzero fully dressed near--far determinant at \(j=2\), including
   the pure rooted `|V|>=7` tail and all rootless-component families, and
   obtain the corresponding depth-sensitive bound uniformly in `j`;
2. coinstantiate the compensated directions for all needed depths in one
   positive physical rate law and keep the inverse stable along the stopped
   trajectory;
3. accumulate `Omega(log(1/x))` gain on the terminal holes, thereby
   producing the fractional cover required by C.10, and round it there;
4. pass the resulting literal all-depth bank to Gate C.

## 4. Expected compression

With the two replacement blocks above, the following current ranges can be
removed or collapsed without losing a live premise:

* G opening and G.2--G.13, plus G.16--G.17: about 2,950 lines;
* H.2, H.4/H.4a, H.5--H.7, H.12--H.13, and old H.16: about
  1,350 lines;
* superseded C material listed in Section 1: roughly 1,500--2,000 further
  lines depending on whether the protection identities are retained.

The Gate-A and Gate-B prose is also repeated in the front status narrative,
the Section 4 ledger, Section 5, and the completion audit.  Keep one exact
gate statement and make the other three locations one-line cross-references.
