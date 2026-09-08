# Gate B: a delocalized complete-`W_2` inverse and the exact full-exposure threshold

**Date:** 2026-08-22

**Status.**  The all-module boundary-profile theorem does more than close
the complete-state Hilbert scalar.  Retaining its binomial orbit factor
gives a coordinatewise-polynomial simultaneous right inverse for the
complete `W_2` compensated operator:

\[
 \boxed{
  \|f\|_\infty
  \le36\sqrt3\,r^6\sum_{j=2}^{r-2}\|J_j\|_2
  \le36\sqrt3\,r^{13/2}
       \left(\sum_{j=2}^{r-2}\|J_j\|_2^2\right)^{1/2}.}       \tag{0.1}
\]

Here `J_j` is an arbitrary relative shallow current in the
`V_(2r+1-j,j)` block, `f=delta/lambda^0` is the relative perturbation of
the uniform catalogue law, and all four complete `W_2` constraints vanish.
This statement includes dependent constraint modules.

For the actual full-exposure columns, however, the absolute remainder
bound is not enough.  On every rank-two conditioned module, a sufficient
sharp-scale input is

\[
 \boxed{
 {\|E\|_{\rm op}\over s_{\min}(W)}
 \le {1\over12\sqrt3\,r^3+1}.}                              \tag{0.2}
\]

It preserves at least one quarter of the `W_2` angle.  Rank-deficient
modules require a direct span-stability statement because an arbitrarily
small new column can add a new direction.  Thus (0.1) closes complete-state
`W_2` delocalization, while (0.2), or a direct full-exposure boundary
quotient, remains the exact transfer gate.

## 1. Normalized representation lemma

Let `G` be a finite group and let `V` be a real orthogonal **absolutely
irreducible** representation of dimension `d`; equivalently for the
argument below, assume `End_G(V)=R`.  Equip `L^2(G)` with uniform
probability measure.  The normalized matrix-coefficient map is

\[
 \Phi(v\otimes u)(g)=\sqrt d\,\langle v,g u\rangle.           \tag{1.1}
\]

Schur orthogonality gives

\[
 \|\Phi(v\otimes u)\|_2=\|v\|\,\|u\|,
 \qquad
 \|\Phi(v\otimes u)\|_\infty
 \le\sqrt d\,\|v\|\,\|u\|.                               \tag{1.2}
\]

For completeness, average the rank-one operator
`g u u'^T g^{-1}` over `G`.  The average commutes with the irreducible
action.  The hypothesis `End_G(V)=R` makes it a real scalar multiple of
the identity; its trace makes the scalar `d^-1 <u',u>`.  Pairing with
`v,v'` proves the bilinear form of (1.2), and Cauchy--Schwarz proves the
supremum bound.  The extra hypothesis is necessary for general real
irreducibles: real Schur commutants can also be complex or quaternionic.

Let `A:L^2(G)->V` be equivariant.  On this matrix-coefficient copy it has
the form

\[
 A\Phi(v\otimes u)=\langle a,u\rangle v                  \tag{1.3}
\]

for a unique multiplicity vector `a`.  If homogeneous equivariant
constraints restrict `u` to a subspace `K`, the constrained singular value
is `sigma=||P_K a||`.  For arbitrary `J in V`, choose

\[
 u_J={P_Ka\over\|P_Ka\|^2},
 \qquad f_J=\Phi(J\otimes u_J).                              \tag{1.4}
\]

Then `f_J` satisfies the constraints, `Af_J=J`, and

\[
 \boxed{
 \|f_J\|_2={\|J\|\over\sigma},\qquad
 \|f_J\|_\infty\le{\sqrt d\over\sigma}\|J\|.}             \tag{1.5}
\]

No independence of a displayed list of constraint columns is used: only
their span, through `K`, occurs.

## 2. Application to every depth-two module

Put

\[
 b=2r+1,\qquad k=r-2,\qquad \ell=r+3,
 \qquad N={b\choose k}.                                      \tag{2.1}
\]

For `2<=j<=k`, let

\[
 V_j=V_{(b-j,j)},\qquad
 d_j=\dim V_j={b\choose j}-{b\choose{j-1}}.                  \tag{2.2}
\]

These `S_b` modules satisfy the absolute-irreducibility hypothesis in
Section 1.  Indeed, the real module in the multiplicity-free subset
decomposition is the real Specht module `S^(b-j,j)`.  Its polytabloid
construction is defined over the integers, and the Specht irreducibility
theorem says that its complexification is an irreducible complex
`S_b`-module.  If a real equivariant endomorphism is complexified, complex
Schur's lemma makes it a complex scalar; preservation of the original real
form forces that scalar to be real.  Hence `End_(S_b)(V_j)=R`, exactly as
required above.  (Equivalently, one may use Young's real orthogonal model,
whose complexification is the same irreducible Specht module.)

The relative-density squared singular value of the complete compensated
`W_2` current operator is

\[
 \widehat\sigma_{r,j}^2
 =\alpha^{(2)}_{r,j}\Theta_{r,j}.                            \tag{2.3}
\]

The norm convention here is exact: the input is probability-normalized
`L^2(S_b)` and the output is the standard Euclidean norm on rank-`k`
targets after division by their uniform marginal `p=b/N`.  Indeed, for
`lambda^0_G=1/b!` and `delta_G=lambda^0_G f(G)`,

\[
 \sum_G{\delta_G^2\over\lambda^0_G}=\mathbb E_G f(G)^2,
 \qquad
 {1\over p}\sum_G\delta_Gq_T(G)
 ={1\over p}\mathbb E_G[f(G)q_T(G)].                         \tag{2.3a}
\]

Thus the singular value in (2.3) is precisely the one to which the
probability-normalized matrix-coefficient lemma applies; there is no
unrecorded factor of `b!`, `N`, or `p`.

The boundary-profile theorem gives, without discarding the orbit-size
factor,

\[
 \alpha^{(2)}_{r,j}\ge
 {1\over3b^2k(k-1)\ell(\ell-1)},
\]

\[
 \Theta_{r,j}\ge
 {N\over b^2k(k-1)\ell(\ell-1)}.                            \tag{2.4}
\]

Since `b<=3r`, `k(k-1)<=r^2`, and
`ell(ell-1)<=4r^2`,

\[
 \boxed{
 \widehat\sigma_{r,j}^2
 \ge {N\over3888r^{12}}.}                                   \tag{2.5}
\]

Binomial coefficients increase up to the middle.  Here `j<=k< b/2`, so

\[
 d_j\le {b\choose j}\le {b\choose k}=N.                    \tag{2.6}
\]

Apply (1.5) to the compensated multiplicity subspace.  Equations
(2.5)--(2.6) give

\[
 {\sqrt{d_j}\over\widehat\sigma_{r,j}}
 \le\sqrt{3888}\,r^6\sqrt{d_j/N}
 \le36\sqrt3\,r^6.                                         \tag{2.7}
\]

For currents `J_j in V_j`, construct `f_j` by (1.4) and put
`f=sum_j f_j`.  Equivariance keeps the blocks separate, so this is a
simultaneous right inverse and all constraints vanish.  The triangle
inequality and then Cauchy--Schwarz over at most `r` modules give (0.1).

If `lambda^0_G=1/b!` and `delta_G=lambda^0_G f(G)`, then
`||delta/lambda^0||_infty=||f||_infty`.  Thus (0.1) is precisely a
coordinatewise delocalization estimate; choosing an amplitude below its
reciprocal preserves nonnegativity.

## 3. Exact perturbative threshold for full exposure

Let `C` be the span of the two central columns.  After projection away
from `C`, let `W` be the two-column `W_2` synthesis map and `E` the
higher-order remainder synthesis map, both with the weighted domain norm

\[
 \|x\|_\kappa^2=\kappa_{r,j}x_M^2+
                  \kappa_{r-1,j}x_L^2.                       \tag{3.1}
\]

The full-exposure columns are those of `W-E`.  Write

\[
 \beta_W={\operatorname {dist}(\bar q,\operatorname {ran}W)^2
                  \over\|\bar q\|^2},
 \qquad
 \varepsilon={\|E\|_{\rm op}\over s_{\min}(W)}.            \tag{3.2}
\]

When `W` has rank two and `epsilon<1`, the standard synthesis-map gap
bound gives

\[
 {\operatorname {dist}(\bar q,\operatorname {ran}(W-E))
       \over\|\bar q\|}
 \ge\left(\sqrt{\beta_W}-{\varepsilon\over1-\varepsilon}\right)_+.
                                                                    \tag{3.3}
\]

Let `a^(0)=||bar q||^2/||q||^2`.  The `W_2` angle is
`alpha^(2)=a^(0) beta_W`, so `beta_W>=alpha^(2)>=A`, where

\[
                         A={1\over108r^6}.                    \tag{3.4}
\]

If

\[
 {\varepsilon\over1-\varepsilon}\le{\sqrt A\over2}
 ={1\over12\sqrt3\,r^3},                                   \tag{3.5}
\]

then the right side of (3.3) is at least `sqrt(beta_W)/2`.
Solving (3.5) for `epsilon` gives exactly (0.2), and therefore

\[
 \boxed{\alpha^{(e)}_{r,j}\ge{1\over4}
        \alpha^{(2)}_{r,j}\ge{1\over432r^6}.}                \tag{3.6}
\]

The absolute remainder estimate supplies only

\[
                         \|E\|_{\rm op}\le\sqrt2 C_0D_M.    \tag{3.7}
\]

Consequently, using (3.7) in (0.2) would require the relative conditioned
scale

\[
 {s_{\min}(W)\over D_M}
 \ge\sqrt2 C_0(12\sqrt3\,r^3+1).                            \tag{3.8}
\]

But testing the weighted-domain unit vector supported on either shore,
then using projection contraction and the coefficient `l_1` lift bound,
gives

\[
 {s_{\min}(W)\over D_M}
 \le {\|W_{2,s}\|_1\over D_M}
 ={2rM_2(E_0)\over D_M}=24r+O(1).                            \tag{3.9}
\]

Thus the known absolute estimate is at least two powers of `r` above the
best scale at which this perturbative criterion could possibly be deduced.
This comparison does not say the actual remainder is large; it says that
(3.7) contains insufficient directional cancellation.  The exact missing
input is (0.2), a same-span version for reduced-rank modules, or a direct
full-exposure angle proof.

## 4. Scope

The complete `W_2` Hilbert scalar and its coordinatewise-delocalized
simultaneous inverse across the harmonic blocks of the **single rank**
`k=r-2` are now closed.  This is not yet a simultaneous inverse across
several shallow depths.  This note does not prove that the
full-exposure constraint span is close to the `W_2` span.  It also does not
prove stopped nonsymmetric stability or logarithmic terminal-hole-aligned
gain.
