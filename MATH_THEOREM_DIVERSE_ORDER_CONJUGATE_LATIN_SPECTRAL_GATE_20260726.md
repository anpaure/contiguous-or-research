# Diverse-order packets: the exact conjugate-Latin coupling and its spectral gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is
used.

**Status correction.**  The CPCR/floor-covariance target used below is a
sufficient strengthening, not the authoritative constant-one target.  The
exact weaker objective is the missing-shadow hinge developed in
MATH_THEOREM_L1_MISSING_HINGE_COMPOUND_SLAB_EXCHANGE_20260726.md.  The
spectral floor identities remain correct, but their failure does not rule
out coefficient one.

## 0. Outcome

Let the retained diverse-order packets have size

\[
                              s=2^R,
 \qquad |\mathfrak P|s=G=W-o(W/H),                         \tag{0.1}
\]

and let \(\Gamma\) be the complete indexed affine-conjugate atlas of the
fixed trace-injective compiler.  At every signed depth \(c=(\epsilon,q)\),
one option in one packet emits an \(s\)-set of literal targets.

There are two exact conclusions.

First, a packetwise Birkhoff decomposition cannot turn the diffuse
ordered-profile point into polarized literal target marginals.  If an
\(s\)-set \(A\) has its indicator in the convex hull of the legal compiler
image indicators of one packet, then

\[
 \boxed{A\text{ is itself the image of one legal compiler option}.}       \tag{0.2}
\]

Thus an integral target-to-packet matching does not lift by Birkhoff unless
the entire target set assigned to every packet is already one compiler
image.  The complete conjugate orbit is not the hypersimplex of all
\(s\)-subsets.  In fact it contains at most
\(2^RR!\) image sets, whereas the local depth-\(q\) face universe has

\[
 V_{R,q}=\binom Rq2^{R-q}={s\over\theta_{R,q}},
 \qquad \theta_{R,q}={2^q\over\binom Rq},                         \tag{0.3}
\]

and hence has \(\binom{V_{R,q}}s\) possible \(s\)-sets.  In the protected
regime the logarithms of these two quantities are respectively
\(O(R\log R)\) and
\(\Omega(s\log(1/\theta_{R,q}))\).  The orbit restriction is enormous.

Second, there is an honest algebraic cross-packet coupling which can, in
principle, resolve diffuse one-point marginals.  Give every packet a shift
\(h_P\in\Gamma\).  For a common color \(u\in\Gamma\), install option
\(h_Pu\) in packet \(P\).  As \(u\) runs through \(\Gamma\), every packet
uses every conjugate exactly once, but different packets are correlated.
This is the exact **conjugate-Latin family**.

For this family the sum, over all colors, of the excess above the integer
floor has an exact nonabelian Fourier formula.  At one signed depth, put

\[
 L_T^h(u)=\sum_P {\bf1}_{\{T\in I_{P}^{h_Pu}\}},
 \qquad \lambda={G\over N}=c+\alpha,\quad c=\lfloor\lambda\rfloor. \tag{0.4}
\]

If \(a_{P,T}(g)={\bf1}_{\{T\in I_P^g\}}\), then

\[
\boxed{
\begin{aligned}
 &\sum_{u\in\Gamma}\left[
       \sum_T\binom{L_T^h(u)}2-\mathcal C_{\min}
                         \right]                                  \\
 &= {|\Gamma|\over2}\sum_T(\bar L_T-\lambda)^2
  +{1\over2|\Gamma|}\sum_T\sum_{\rho\ne{\bf1}}d_\rho
       \left\|\sum_P\widehat a_{P,T}(\rho)\rho(h_P)\right\|_F^2
  -{|\Gamma|N\over2}\alpha(1-\alpha),
\end{aligned}}                                                    \tag{0.5}
\]

where

\[
 \bar L_T={1\over|\Gamma|}\sum_g\sum_Pa_{P,T}(g),
 \qquad
 \mathcal C_{\min}=N\binom c2+(G-cN)c,                           \tag{0.6}
\]

and \(\rho\) ranges over the nontrivial irreducible unitary
representations of \(\Gamma\).  Formula (0.5) is exact, not an inequality.
The same shifts occur inside the sum for every sign and depth.

Consequently the present inputs do **not** yet construct the required
fractional packet distributions:

* the proved selected-profile and within-profile Hall theorems control
  literal source capacity after profile allocation, but they do not choose
  the shared cross-profile allocation or force the compiler-atlas
  occurrence square \(\sum_T(\bar L_T-\lambda)^2\) in (0.5); and
* completeness of the conjugate atlas gives the exact row averages, but
  gives no cancellation of the nontrivial matrices in (0.5).

Ordinary independent conjugates retain the diagonal Fourier energy and
give the already-audited \(\Omega(W)\) floor loss.  Ordinary packetwise
Birkhoff does not change the marginals at all.  A positive continuation
must prove a **Fourier-Latin resolution theorem**: choose the packet shifts
and, if necessary, the coordinate-permutation rows so that the right-hand
side of (0.5), summed over all protected signed depths, is
\(o(|\Gamma|W)\).  Then some common color gives one integral whole-packet
choice with \(o(W)\) total floor excess and hence \(o(W)\) holes.

This is strictly sharper than the previous multilinear sufficient
functional.  It supplies the only natural algebraic coupling of the
complete atlas, proves exactly what Birkhoff can and cannot do, and splits
the missing theorem into a literal zero-mode statement and a simultaneous
nontrivial-mode cancellation statement.

## 1. Packet image orbit polytopes

Fix one packet \(P\) and one signed depth \(c\).  Write

\[
                       I_{P,c}^g\subseteq\mathcal T_c,
 \qquad |I_{P,c}^g|=s
 \qquad(g\in\Gamma).                                  \tag{1.1}
\]

Repeated group labels are allowed: the atlas is indexed, and a stabilizer
may give the same physical image more than once.  Define its image orbit
polytope

\[
 \mathcal K_{P,c}
 =\operatorname {conv}\{ {\bf1}_{I_{P,c}^g}:g\in\Gamma\}.       \tag{1.2}
\]

For all depths and both signs together, the legal packet polytope is

\[
 \mathcal K_P
 =\operatorname {conv}\left\{
   \bigl({\bf1}_{I_{P,c}^g}\bigr)_c:g\in\Gamma\right\}.         \tag{1.3}
\]

The same coefficient of \(g\) occurs in every component of (1.3).

### Theorem 1.1 (zero-one rigidity of an image orbit polytope)

Let \(A\subseteq\mathcal T_c\) have \(|A|=s\).  Then

\[
 {\bf1}_A\in\mathcal K_{P,c}
 \quad\Longleftrightarrow\quad
 A=I_{P,c}^g\text{ for some }g\in\Gamma.                         \tag{1.4}
\]

#### Proof

The reverse implication is immediate.  Conversely, suppose

\[
 {\bf1}_A=\sum_gx_g{\bf1}_{I_{P,c}^g},
 \qquad x_g\ge0,\quad\sum_gx_g=1.                               \tag{1.5}
\]

For \(T\in A\), the left side is one.  Since every summand on the right
is zero or one, every \(g\) with \(x_g>0\) must contain \(T\).  Hence
\(A\subseteq I_{P,c}^g\) for every positive-weight \(g\).  Both sets have
size \(s\), so equality holds. \(\square\)

This proves the precise failure of the proposed packetwise Birkhoff step.
A target-to-packet matching gives one \(s\)-set \(A_P\) to a saturated
packet.  Birkhoff lifts that assignment only if \(A_P\) is already one
of the orbit columns.  Splitting the \(s\) targets into owner slots and
applying the ordinary Birkhoff theorem would mix entries from different
compiler columns and would no longer be one legal packet option.

### Lemma 1.2 (quantitative polarization rigidity)

Let \(g,g'\) be independent with a common packet distribution \(x\), and
put

\[
 p(T)=\Pr_x(T\in I_{P,c}^g).
\]

Then

\[
 \boxed{
 \sum_Tp(T)(1-p(T))
 ={1\over2}\mathbb E_{g,g'}
       |I_{P,c}^g\triangle I_{P,c}^{g'}|.}                       \tag{1.6}
\]

In particular, if the left side is \(o(s)\), there is one option \(g_0\)
such that

\[
 \mathbb E_g|I_{P,c}^{g_0}\triangle I_{P,c}^g|=o(s).            \tag{1.7}
\]

#### Proof

For one target, the probability that exactly one of the two images contains
it is \(2p(T)(1-p(T))\).  Sum over targets.  Some first sample \(g_0\)
has conditional expectation at most the pair average. \(\square\)

Thus a near-zero-one marginal is not created by a diffuse decomposition.
It says that the distribution is supported, in image distance, near one
actual compiler column.  If the distinct orbit images have a positive
relative separation, (1.7) reduces to concentration on a single physical
image (up to its stabilizer).

## 2. Exact product covariance is exact polarization

The covariance alternative in the preceding reduction can be sharpened.
Fix one signed depth and suppose first that the literal one-point means are
exactly constant:

\[
                       \sum_Pp_P(T)=\lambda=c+\alpha
                       \qquad(T\in\mathcal T),                    \tag{2.1}
\]

where \(0\le\alpha<1\).  Then

\[
 \widetilde{\mathcal C}
 =\sum_T\sum_{P<Q}p_P(T)p_Q(T)
 ={1\over2}\left(N\lambda^2-\sum_{P,T}p_P(T)^2\right).          \tag{2.2}
\]

The integer minimum is

\[
 \mathcal C_{\min}
 =N\left[\binom c2+c\alpha\right]
 ={N\over2}(\lambda^2-c-\alpha^2).                              \tag{2.3}
\]

Therefore

\[
 \boxed{
 \widetilde{\mathcal C}-\mathcal C_{\min}
 ={1\over2}\left[
 N(c+\alpha^2)-\sum_{P,T}p_P(T)^2\right].}                      \tag{2.4}
\]

For a fixed target, among vectors
\((p_P)_P\in[0,1]^{\mathfrak P}\) of sum
\(c+\alpha\), the square sum is at most \(c+\alpha^2\), with equality
exactly for

\[
                  (p_P)_P=(\underbrace{1,\ldots,1}_{c},
                         \alpha,0,\ldots,0)                     \tag{2.5}
\]

up to permutation.  Hence (2.4) says:

\[
 \boxed{
 \text{product covariance at the integer floor}
 \Longleftrightarrow
 \text{targetwise polarization as in (2.5)}.}                  \tag{2.6}
\]

There are not two independent fractional escape routes.  Under product
sampling, alternative (ii) is precisely alternative (i) in its quadratic
form.

There is also the exact uncertainty ledger

\[
 \boxed{
 \sum_{P,T}p_P(T)(1-p_P(T))
 =N\alpha(1-\alpha)
  +2(\widetilde{\mathcal C}-\mathcal C_{\min}).}                \tag{2.7}
\]

When \(\alpha=0\), floor covariance forces all but \(o(W)\) packet-target
marginals to be zero-one.  For general \(\alpha\), the only permitted
diffuse mass at equality is one fractional packet of mass \(\alpha\) per
target.  Combining (2.7) packetwise with Lemma 1.2 shows why a successful
product point must be assembled from almost-common image cores, not by
uniformly averaging the full atlas.

If (2.1) has aggregate \(o(W)\) error and \(\lambda\) stays bounded, the
same equations hold with an \(o(W)\) error after truncating the exceptional
targets.  This is the relevant Gaussian regime.

## 3. The common-color conjugate-Latin construction

The preceding rigidity concerns product distributions.  A correlated
algebraic resolution can do something genuinely different.

Put \(K=|\Gamma|\).  For each packet choose a row shift \(h_P\in\Gamma\).
For every color \(u\in\Gamma\), define the integral global configuration

\[
                        \omega_P(u)=h_Pu.                         \tag{3.1}
\]

Because left multiplication is a permutation of \(\Gamma\), every packet
uses every indexed conjugate exactly once as \(u\) runs over the colors.
The choice (3.1) is common through all depths and both signs.

For a literal target \(T\) at a fixed signed depth, define

\[
 a_{P,T}(g)={\bf1}_{\{T\in I_P^g\}},
 \qquad
 L_T^h(u)=\sum_Pa_{P,T}(h_Pu).                                  \tag{3.2}
\]

Its color average is

\[
 \bar L_T={1\over K}\sum_uL_T^h(u)
 ={1\over K}\sum_{P,g}a_{P,T}(g),                              \tag{3.3}
\]

independent of all shifts.  Thus row shifts cannot repair a bad literal
zero mode.  They only redistribute each target's fixed total occurrence
capacity among the colors.

At every color, the total target load is \(G\).  Put

\[
 \lambda={G\over N}=c+\alpha,
 \qquad
 \mathcal C_{\min}=N\binom c2+(G-cN)c.                          \tag{3.4}
\]

Discrete convexity gives the following exact identity.

### Lemma 3.1 (color-averaged floor identity)

For every shift array \(h=(h_P)_P\),

\[
\boxed{
\begin{aligned}
 \sum_{u\in\Gamma}
 \left[\sum_T\binom{L_T^h(u)}2-\mathcal C_{\min}\right]
  &={1\over2}\sum_{u,T}(L_T^h(u)-\lambda)^2
       -{KN\over2}\alpha(1-\alpha)                         \\
  &={K\over2}\sum_T(\bar L_T-\lambda)^2
    +{1\over2}\sum_{u,T}(L_T^h(u)-\bar L_T)^2
       -{KN\over2}\alpha(1-\alpha).
\end{aligned}}                                                   \tag{3.5}
\]

#### Proof

For one color,

\[
 \sum_T\binom{L_T}2
 ={1\over2}\left(\sum_TL_T^2-G\right).                         \tag{3.6}
\]

Since \(\sum_TL_T=G=N\lambda\), expanding
\(\sum_T(L_T-\lambda)^2\) and substituting (2.3) proves the first
line.  The second is the orthogonal decomposition around the color mean
\(\bar L_T\). \(\square\)

The left side is nonnegative.  More importantly, if its sum over all
protected signed depths is \(o(KW)\), then some color \(u\) has total
floor excess \(o(W)\).  The conditional-expectation theorem in the
preceding reduction is not even needed: that color is already one integral
whole-packet choice.

## 4. Exact nonabelian Fourier formula

Let \(\widehat\Gamma\) be the irreducible unitary representations of
\(\Gamma\).  For a scalar function \(f:\Gamma\to\mathbb C\), use the
unnormalized transform

\[
                     \widehat f(\rho)
 =\sum_{g\in\Gamma}f(g)\rho(g)^*.                               \tag{4.1}
\]

If \(f_h(u)=f(hu)\), then

\[
                     \widehat {f_h}(\rho)
 =\widehat f(\rho)\rho(h).                                     \tag{4.2}
\]

Consequently

\[
 \widehat {L_T^h}(\rho)
 =\sum_P\widehat a_{P,T}(\rho)\rho(h_P).                       \tag{4.3}
\]

Nonabelian Parseval gives

\[
 \sum_u|L_T^h(u)-\bar L_T|^2
 ={1\over K}\sum_{\rho\ne{\bf1}}d_\rho
 \left\|\sum_P\widehat a_{P,T}(\rho)\rho(h_P)\right\|_F^2. \tag{4.4}
\]

Substitution in (3.5) proves (0.5).

Two features of (4.4) matter.

1. The target zero mode \(\bar L_T\) is invariant under every Latin row
   shift.  Profile balance of \(\sum_{T\in\Pi}\bar L_T\) on a coarse cell
   \(\Pi\) does not bound
   \(\sum_{T\in\Pi}(\bar L_T-\lambda)^2\).
2. The nontrivial terms are nonnegative and add over signs and depths.
   Cancellation obtained at one depth cannot pay for a failure at another.
   The same \(\rho(h_P)\) must cancel all of them simultaneously.

For a fixed \(\rho\), summing over signed targets and depths produces the
positive semidefinite packet Gram form

\[
 \sum_{c,T}d_\rho
 \left\|\sum_P\widehat a_{P,c,T}(\rho)\rho(h_P)\right\|_F^2.
                                                                    \tag{4.5}
\]

Thus a positive theorem needs near-null phase vectors for the actual sum
of these Gram forms.  The selected-profile Hall theorem, including its
arbitrary-subset form inside each exact ordered profile, supplies no
information about these compiler-occurrence spectra.

## 5. The translation subatlas is an explicit cylinder Fourier problem

The general formula can be made completely literal on the translation
subgroup \(A=\mathbb F_2^R\).  Fix the coordinate-permutation part of the
compiler option in one packet.  A physical depth-\(q\) face is written

\[
                         T=(D,\eta),
 \qquad D\in\binom{[R]}q,\quad
 \eta\in\mathbb F_2^{[R]\setminus D}.                           \tag{5.1}
\]

Let \(B_{P,T}\) be the set of outside orientations \(\zeta\) for which
the un-translated compiler image contains \((D,\zeta)\).  Trace
injectivity makes these orientations distinct.  The translations which
make the image contain \(T\) form the disjoint cylinder union

\[
 A_{P,T}
 =\{a\in\mathbb F_2^R:
       a|_{D^c}=\eta+\zeta\text{ for some }\zeta\in B_{P,T}\}.  \tag{5.2}
\]

Hence

\[
                         |A_{P,T}|=2^q|B_{P,T}|.                 \tag{5.3}
\]

For the character \(\chi_\xi(a)=(-1)^{\xi\cdot a}\),

\[
\boxed{
 \widehat{{\bf1}_{A_{P,T}}}(\xi)=
 \begin{cases}
  0,&\operatorname {supp}\xi\cap D\ne\varnothing,\\[2mm]
  2^q(-1)^{\xi\cdot\eta}
       \displaystyle\sum_{\zeta\in B_{P,T}}(-1)^{\xi\cdot\zeta},
       &\operatorname {supp}\xi\subseteq D^c.
 \end{cases}}                                                    \tag{5.4}
\]

If packet shifts are \(h_P\in\mathbb F_2^R\), the nonzero-mode term is

\[
 \sum_{\xi\ne0}\sum_{c,T}
 \left|\sum_P(-1)^{\xi\cdot h_P}
       \widehat{{\bf1}_{A_{P,c,T}}}(\xi)\right|^2.              \tag{5.5}
\]

Formula (5.4) identifies the exact object which must cancel.  Complete
translation averaging proves only the value at \(\xi=0\).  Direction-set
balance proves only averages of (5.3).  Neither statement controls the
Walsh sums in (5.5).

Random independent shifts kill cross terms only in expectation and leave
the diagonal energy

\[
 \sum_{\xi\ne0,c,T,P}
       \left|\widehat{{\bf1}_{A_{P,c,T}}}(\xi)\right|^2,         \tag{5.6}
\]

which is the spectral form of the Poisson-floor obstruction.  Thus the
common-color construction is useful only with a deterministic resolution
of the cylinder spectra, not with random row shifts.

## 6. Why the proved profile Hall theorems do not supply the shifts

The selected-profile theorem and its exact-profile refinement provide
the required Hall expansion, including arbitrary target subfamilies inside
each exact ordered profile outside the proved negligible overlap strata.
This closes the within-profile Hall gate.  It does not choose the weighted
allocation of a source profile shared by several target profiles, and it
does not group the resulting incidences into complete compiler image
columns.

In the present notation, the Hall input controls capacities represented by
quantities of the form

\[
                       \sum_{T\in\Pi}\bar L_T                    \tag{6.1}
\]

for a profile cell \(\Pi\), together with the corresponding
arbitrary-subset inequalities.  It does not prove either

\[
 \sum_T(\bar L_T-\lambda)^2=o(W)                                \tag{6.2}
\]

or the joint zero/nontrivial-mode estimate

\[
 \sum_c\left[
  \sum_T(\bar L_{c,T}-\lambda_c)^2
  +{1\over K^2}\sum_T\sum_{\rho\ne{\bf1}}d_\rho
   \left\|\sum_P\widehat a_{P,c,T}(\rho)\rho(h_P)\right\|_F^2
  -N_c\alpha_c(1-\alpha_c)\right]=o(W),                         \tag{6.3}
\]

which is (0.5) after division by \(K/2\).

This is not a defect which Birkhoff decomposition repairs:

* decomposing a fixed row barycenter leaves every \(p_{P,c}(T)\), hence
  the product functional, unchanged;
* decomposing an integral home set is possible only for an actual orbit
  image by Theorem 1.1; and
* a common-color decomposition is governed by (0.5), whose nontrivial
  modes are absent from the profile flow.

The complete atlas and the profile Hall theorems therefore establish row
regularity and literal capacity inside the resolved profiles,
respectively.  They do not establish a cross-profile compiler-image
resolution or a resolvable block design.

## 7. Exact surviving theorem

For every protected signed depth \(c\), let the quantities in (0.5) carry
the subscript \(c\).  Define

\[
\begin{aligned}
 \mathfrak E(h)
 :=\sum_c\Bigg[&{K\over2}\sum_T(\bar L_{c,T}-\lambda_c)^2\\
 &+{1\over2K}\sum_T\sum_{\rho\ne{\bf1}}d_\rho
   \left\|\sum_P\widehat a_{P,c,T}(\rho)\rho(h_P)\right\|_F^2
 -{KN_c\over2}\alpha_c(1-\alpha_c)\Bigg].                     \tag{7.1}
\end{aligned}
\]

By (0.5), \(\mathfrak E(h)\ge0\) and is exactly the total floor excess
of all \(K\) integral colors.

### Theorem 7.1 (conjugate-Latin completion)

If the packet axes, coordinate-permutation rows, and shifts \(h_P\) can be
chosen so that

\[
                              \mathfrak E(h)=o(KW),              \tag{7.2}
\]

then one color \(u\in\Gamma\) gives a legal integral diverse-order
compiler choice in every packet with

\[
 \sum_c\bigl(\mathcal C_c-\mathcal C_{c,\min}\bigr)=o(W),      \tag{7.3}
\]

and therefore \(o(W)\) aggregate lower and upper target holes.

#### Proof

Average (7.3) over the \(K\) colors.  Its average is
\(\mathfrak E(h)/K=o(W)\), so one color has at most that excess.  Apply
the exact collision-to-hole ledger from
`MATH_REDUCTION_DIVERSE_ORDER_CROSS_PACKET_MULTILINEAR_ROUNDING_20260726.md`.
\(\square\)

What remains unproved is (7.2).  It has two logically separate parts:

1. **literal zero-mode regularity:** control the targetwise square of the
   complete-atlas occurrence capacities, not merely their profile sums;
2. **simultaneous spectral resolution:** choose one packet shift array
   cancelling the actual nontrivial occurrence spectra at every sign and
   depth down to the integer-floor variance.

This is the precise surviving algebraic gate.  A packetwise Birkhoff
theorem is ruled out by Theorem 1.1; a conjugate-Latin/Fourier resolution
would prove the CPCR statement of
MATH_EXACT_REMAINING_CROSS_PARENT_COMPILER_RESOLUTION_20260726.md, since
its functional is exactly twice the collision excess in (7.3).  No owner,
local compiler, component-count, selected-profile Hall, common-order, or
within-packet gate is being reopened here.
