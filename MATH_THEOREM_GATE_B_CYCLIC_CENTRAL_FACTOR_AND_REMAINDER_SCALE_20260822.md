# A uniform cyclic-variance bound for the Gate-B central factor

**Date:** 2026-08-22

**Status.**  This note proves, for every `r>=4` and every depth-two
module `2<=j<=r-2`, the unconditional polynomial bound

\[
                         a^{(0)}_{r,j}\ge {1\over27r^4}.       \tag{1}
\]

Thus the central factor in H.56 is no longer an asymptotic input.  The
remaining rank-two scalar input is the conditional `W_2` volume (or the
weaker original quotient involving it).  The last section also gives the
exact norm in which H.59 must be compared with the conditioned `W_2`
columns; it explains rigorously why the existing absolute remainder bound
alone is not a relative perturbation theorem.  No uniform lower bound for
the conditional `W_2` volume is claimed here.

## 1. Harmonic lifts and cyclic decomposition

Put

\[
 b=2r+1,\qquad k=r-2,
\]

and choose `j` disjoint distinguished coordinate pairs.  For an `s`-set
`A`, write

\[
 H_s(A)=\prod_{i=1}^j
 \bigl(\mathbf1_{\{a_i\in A\}}-\mathbf1_{\{b_i\in A\}}\bigr).
\]

For a coefficient vector `x` on the `s`-sets, its harmonic lift is

\[
                 R_x(g)=\sum_Ax(A)H_s(gA),                    \tag{2}
\]

in `L^2(S_b)` with uniform probability measure.  Let
`I_s(t)` be the cyclic interval of length `s` starting at `t`, and set

\[
 d_{s,t}=R_{\mathbf1_{\{I_s(t)\}}},\qquad
 Q_s=\sum_{t\in\mathbb Z_b}d_{s,t},\qquad d_s=d_{s,0}.         \tag{3}
\]

Let \(\tau\) be the position-cycle permutation for which
\(I_s(t)=\tau^tI_s(0)\), and define the right-translation unitary by

\[
                         (Tf)(g)=f(g\tau).                    \tag{4a}
\]

Then \(d_{s,t}=T^td_s\), since
\(d_{s,t}(g)=H_s(g\tau^tI_s(0))=(T^td_s)(g)\).  Let

\[
                         P={1\over b}\sum_{t=0}^{b-1}T^t       \tag{4}
\]

be orthogonal projection onto the cyclic-invariant subspace.  Hence

\[
 Pd_s={Q_s\over b},\qquad
 u_s=(I-P)d_s,\qquad
 c_s=Q_s-d_s={b-1\over b}Q_s-u_s.                             \tag{5}
\]

The shallow current is `q=Q_k`, so `Pq=q`.  Consequently the invariant
and noninvariant parts are orthogonal and, for every pair of real
coefficients `x=(x_M,x_L)`,

\[
 \left\|q-x_Mc_r-x_Lc_{r-1}\right\|_2^2
 =\left\|q-{b-1\over b}(x_MQ_r+x_LQ_{r-1})\right\|_2^2
  +\left\|x_Mu_r+x_Lu_{r-1}\right\|_2^2.                     \tag{6}
\]

This is the promised exact Tikhonov decomposition.  It uses no
nonsingularity hypothesis on the two central columns.

The single-interval norms are

\[
 \kappa_s=\|d_s\|_2^2
 ={2^j{b-2j\choose s-j}\over{b\choose s}}.                   \tag{7}
\]

Indeed, a uniform image of one fixed `s`-set gives a nonzero value of
`H_s` exactly when it chooses one coordinate from each distinguished pair.

## 2. One cyclic difference is uniformly coercive

Write `m=r-j` and

\[
                         J=j(2r-j+2).                          \tag{8}
\]

Let `A` be the Gram matrix of the two first cyclic differences

\[
                         d_r-Td_r,\qquad d_{r-1}-Td_{r-1}.     \tag{9}
\]

### Lemma 2.1 (exact difference Gram)

For every `2<=j<=r-2`,

\[
 A_{11}=2\kappa_r{J\over r(r+1)},\qquad
 A_{22}=2\kappa_{r-1}{J\over(r-1)(r+2)},                     \tag{10}
\]

and its normalized off-diagonal entry is

\[
 {A_{12}\over\sqrt{A_{11}A_{22}}}
 ={1\over2}\sqrt{{(r-j)(r-j+2)\over r^2-1}}\le{1\over2}.    \tag{11}
\]

#### Proof

For fixed sets of sizes `s,t` and intersection `h`, the Hahn kernel is

\[
 \zeta_{s,t,j}(h)
 ={2^j\over {b\choose s}{s\choose h}{b-s\choose t-h}}
 \sum_{a=0}^j(-1)^{j-a}{j\choose a}
 {b-2j\choose
 h-a,\ s-j-h+a,\ t-j-h+a,\ b-s-t+h-a}.             \tag{12}
\]

Invalid multinomials vanish.  Formula (12) is obtained by splitting every
distinguished pair and is also a direct computation of
`<d_(s,0),d_(t,u)>` for a cyclic start \(u\), from the intersection size.

For two `r`-intervals shifted by one, only `a=j-1,j` survive in (12).
Dividing by (7) gives

\[
 {\zeta_{r,r,j}(r-1)\over\kappa_r}
 ={(r-j)(r-j+1)-j\over r(r+1)}.                    \tag{13}
\]

The identical calculation one rank lower gives

\[
 {\zeta_{r-1,r-1,j}(r-2)\over\kappa_{r-1}}
 ={(r-j-1)(r-j+2)-j\over(r-1)(r+2)}.               \tag{14}
\]

Subtracting (13)--(14) from one proves the diagonal formulas (10).

For the same-start containment `I_(r-1)(0) subset I_r(0)`, only `a=j`
survives and

\[
 z:=\zeta_{r,r-1,j}(r-1)={r-j\over r}\kappa_r,qquad
 {\kappa_{r-1}\over\kappa_r}
 ={(r-j)(r+2)\over r(r-j+2)}.                     \tag{15}
\]

Of the two shifted cross terms in (9), one is still a containment and the
other has intersection `r-2`.  The same two-term evaluation gives

\[
 {\zeta_{r,r-1,j}(r-2)\over z}
 ={(r-j)^2-1-2j\over r^2-1}.                       \tag{16}
\]

Thus

\[
                         A_{12}=z{J\over r^2-1}.    \tag{17}
\]

Substitution of (10), (15), and (17) gives (11).  Since `j>=2`, its
radicand is at most one.  `square`

Diagonal normalization of `A` and (11) now imply, for all real `x_M,x_L`,

\[
 x^{\mathsf T}Ax
 \ge {J\over r(r+1)}
       (\kappa_rx_M^2+\kappa_{r-1}x_L^2).           \tag{18}
\]

The finite-group variance identity says

\[
 \|(I-P)f\|_2^2
 ={1\over2b}\sum_{t=0}^{b-1}\|f-T^tf\|_2^2.       \tag{19}
\]

Apply (19) to `f=x_Md_r+x_Ld_(r-1)` and retain only the `t=1` term.
Equations (18)--(19) prove the uniform noninvariant penalty

\[
 \boxed{
 \|x_Mu_r+x_Lu_{r-1}\|_2^2
 \ge\mu_{r,j}(\kappa_rx_M^2+\kappa_{r-1}x_L^2),
 \quad
 \mu_{r,j}={j(2r-j+2)\over2br(r+1)}.}              \tag{20}
\]

In particular, concavity of `j(2r-j+2)` on `[2,r-2]` and direct endpoint
comparison give

\[
                         \mu_{r,j}\ge {2\over b(r+1)}.         \tag{21}
\]

This deliberately uses only one of the `b-1` nontrivial cyclic
differences.  It is therefore not sharp, but it is uniform and polynomial.

## 3. Uniform lower bound for the central angle

The shallow vector `q=Q_k` is nonzero on every module under discussion.
Here is a direct witness.  Choose a relabelling `g` whose induced cyclic
order puts two distinguished coordinate pairs across the two boundary
edges of `gI_k(0)`, with the designated positive endpoint of each pair
inside the interval.  A cyclic `k`-interval in this order splits both
adjacent pairs if and only if those are its two boundary edges, hence it is
the unique interval `gI_k(0)`.  Put the remaining `j-2` pairs with one
endpoint among the remaining `k-2` inside coordinates and the other among
the remaining outside coordinates.  This is possible because
\(j-2\le k-2\) and \(j-2\le b-k-2\).
For this relabelling, exactly one summand of `Q_k(g)` is nonzero, and its
value is one.

Let

\[
 a^{(0)}_{r,j}
 ={\operatorname{dist}(q,\operatorname{span}\{c_r,c_{r-1}\})^2
   \over\|q\|_2^2}.                                \tag{22}
\]

For `x=(x_M,x_L)`, put

\[
 X^2=\kappa_rx_M^2+\kappa_{r-1}x_L^2,
 \qquad L=\sqrt2(b-1).
\]

The triangle and Cauchy inequalities applied to (3) give

\[
 \left\|{b-1\over b}(x_MQ_r+x_LQ_{r-1})\right\|_2
 \le (b-1)(|x_M|\sqrt{\kappa_r}+|x_L|\sqrt{\kappa_{r-1}})
 \le LX.                                             \tag{23}
\]

Combining (6), (20), and (23), with `Q=||q||_2`, gives

\[
 \|q-x_Mc_r-x_Lc_{r-1}\|_2^2
 \ge (Q-LX)_+^2+\mu_{r,j}X^2.                       \tag{24}
\]

The minimum of the right side over `X>=0` is

\[
                         {\mu_{r,j}\over L^2+\mu_{r,j}}Q^2.   \tag{25}
\]

Indeed, on `0<=X<=Q/L` this is a one-variable quadratic with minimizer
`LQ/(L^2+mu)`; on the remaining ray the second term is already larger
than (25).  Taking the infimum over the original two coefficients proves

\[
 \boxed{
 a^{(0)}_{r,j}\ge
 {\mu_{r,j}\over2(b-1)^2+\mu_{r,j}}
 \ge {2\over b(r+1)(2(b-1)^2+1)}
 \ge {1\over27r^4}.}                               \tag{26}
\]

For the middle inequality, the function `mu/(L^2+mu)` is increasing,
use (21), and note that `2/(b(r+1))<=1`.  For the last inequality use
`b<=3r`, `r+1<=2r`, and
`2(b-1)^2+1=8r^2+1<=9r^2`.  This proves (1).

### Consequence for the live scalar gate

In the independent rank-two case H.55 gives

\[
 \alpha^{(2)}_{r,j}=a^{(0)}_{r,j}{\xi_{r,j}\over\delta_{r,j}},
 \qquad0<\delta_{r,j}\le1.                         \tag{27}
\]

Therefore (26) removes `a^(0)` from the list of unproved asymptotic
factors: a uniform polynomial lower bound for

\[
                         \Theta_{r,j}\xi_{r,j}                  \tag{28}
\]

is sufficient for the Hilbert scalar gate, with four added powers of
`r` and the fixed factor \(1/27\) (or at most five added powers if the
target is written literally with leading constant one).  Dependent `W_2`
modules still use their reduced-rank Schur complement.
No lower bound for `xi` is supplied by cyclic variance, because `W_2` is
not a central deck.

## 4. The exact scale required for the remainder comparison

The symbols \(c_r,c_{r-1}\) in (5) already denote their \(L^2(S_b)\)
lifts.  Let \(C=\operatorname{span}\{c_r,c_{r-1}\}\) and project
orthogonally away from \(C\).
Write

\[
 w_s=(I-P_C)R_{W_{2,s}},\qquad
 \rho_s=(I-P_C)R_{R_s},\qquad s\in\{r,r-1\}.        \tag{29}
\]

The full-exposure residual columns are `w_s-rho_s`.  Give coefficient
pairs the weighted norm

\[
                         \|x\|_\kappa^2
 =\kappa_rx_M^2+\kappa_{r-1}x_L^2.                 \tag{30}
\]

The already proved modulewise estimate

\[
                         \|R_{R_s}\|_2\le C_0D_M\sqrt{\kappa_{s,j}}  \tag{31}
\]

and contraction of orthogonal projection imply the exact operator bound

\[
 \boxed{
 \|x_M\rho_r+x_L\rho_{r-1}\|_2
 \le\sqrt2C_0D_M\|x\|_\kappa.}                    \tag{32}
\]

Define the conditioned `W_2` scale

\[
 \sigma^W_{r,j}
 ={1\over D_M}\inf_{\|x\|_\kappa=1}
 \|x_Mw_r+x_Lw_{r-1}\|_2.                         \tag{33}
\]

If `H_W` is the conditioned two-by-two Gram from H.53, then literally

\[
 (\sigma^W_{r,j})^2
 ={1\over D_M^2}\lambda_{\min}
 \left(
 \begin{pmatrix}\kappa_r&0\\0&\kappa_{r-1}\end{pmatrix}^{-1/2}
 H_W
 \begin{pmatrix}\kappa_r&0\\0&\kappa_{r-1}\end{pmatrix}^{-1/2}
 \right).                                           \tag{34}
\]

Equations (32)--(34) show exactly what H.59 does and does not prove.  When
\(\sigma^W_{r,j}>0\), the relative synthesis-operator perturbation is at
most

\[
                         {\sqrt2C_0\over\sigma^W_{r,j}}.        \tag{35}
\]

Thus this upper bound yields an `o(1)` column perturbation if
\(\sigma^W_{r,j}\to\infty\) uniformly (or if (31) is sharpened by a
matching vanishing factor).  If \(\sigma^W_{r,j}=0\), one must first pass
to a nonredundant basis and use the reduced-rank quotient.  A merely
polynomial nonzero determinant, or the `O(1/r)` total-mass ratio before
harmonic conditioning, does not imply (35) is small.  Moreover an
\(o(1)\) column perturbation alone need not preserve the polynomially small
angle in H.56: the perturbation must be small relative to the relevant
conditioned angular scale, for example
\(\sqrt{\xi_{r,j}/\delta_{r,j}}\) in the independent rank-two case, or
one must prove the full-exposure scalar directly.  This is a conditioning-
scale diagnosis, not a sufficient perturbation theorem and not a negative
theorem; the actual remainder may have cancellation not visible in (31).

For completeness, the quantitative range-gap statement is as follows.  In
an independent rank-two module put
\(\beta=\xi_{r,j}/\delta_{r,j}\) and let
\(W:x\mapsto x_Mw_r+x_Lw_{r-1}\) and
\(E:x\mapsto x_M\rho_r+x_L\rho_{r-1}\), with the domain norm (30).  If

\[
 \varepsilon={\|E\|_{\mathrm{op}}\over s_{\min}(W)}<1,
\]

then \(W-E\) has the same rank and

\[
 {\operatorname{dist}(\bar q,\operatorname{ran}(W-E))\over\|\bar q\|_2}
 \ge
 \left(\sqrt\beta- {\varepsilon\over1-\varepsilon}\right)_+,
 \qquad \bar q=(I-P_C)q.                             \tag{36}
\]

Indeed, for \(y=(W-E)x\) of norm one,
\(\operatorname{dist}(y,\operatorname{ran}W)\le\|Ex\|\), while
\(1\ge(s_{\min}(W)-\|E\|_{\mathrm{op}})\|x\|_\kappa\).
The equal-dimensional principal-angle identity therefore bounds the two
range projectors by \(\varepsilon/(1-\varepsilon)\); the triangle inequality
for their distances to \(\bar q\) proves (36).  Hence a worst-case
constant-factor angle guarantee follows when
\(\varepsilon\le c\sqrt\beta\) for a sufficiently small fixed \(c\), not
from \(\varepsilon=o(1)\) alone.  If \(W\) is rank deficient, even an arbitrarily
small perturbation on its kernel can add a new span direction, so the
actual full-exposure dependency must be analyzed rather than inferred from
the reduced \(W_2\) span alone.

The remaining Gate-B work is therefore sharply separated into:

1. prove (28), or directly prove the quotient in (27), uniformly over
   `2<=j<=r-2`;
2. prove a lower bound for (33) strong enough for (35), or improve (31)
   relative to the same conditioned directions;
3. then establish the required simultaneous `L^infinity` inverse and its
   stopped stability.

The verifier `scratch/verify_gate_b_cyclic_central_factor_20260822.py`
recomputes (10)--(17) from the Hahn kernel in exact rational arithmetic,
checks (20), and independently evaluates the three-deck central Schur
complement and (26) over a nontrivial finite range.  Those computations
audit the algebra; the proof above is uniform in `r,j`.
