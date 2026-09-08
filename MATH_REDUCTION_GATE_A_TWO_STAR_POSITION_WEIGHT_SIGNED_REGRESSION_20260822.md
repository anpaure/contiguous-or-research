# Gate A: exact signed position-weight regression for the punctured two-star

**Date:** 2026-08-22  
**Status:** exact product-law reduction at \(m=12\); the two signed
tail-relative estimates isolated below remain open

## 0. Outcome

The first connected punctured kernel has two kinds of dependence which
must not be conflated:

1. the first rooted carrier row has one of \(2r\) puncture positions; and
2. after that position is fixed, the second carrier still has a genuinely
connected response to the root-degree tail.

This note writes both effects as exact normalized covariances.  Let
\(a_i\) be the survival-weighted mean two-star kernel after the first
rooted carrier is fixed at position \(i\).  Let \(\pi_{12}(i)\) and
\(\pi_c(i)\) be the position laws induced respectively by the factorial
root tilt and by the normalized cutoff tail.  Then

\[
 \boxed{
 \mathbb E_{\omega_{12}}a-\mathbb E_{\omega_c}a
 =\sum_{i=1}^{2r}a_i\{\pi_{12}(i)-\pi_c(i)\}
 =-{\operatorname {Cov}_{\pi_{12}}(a_i,R_i)
       \over\mathbb E_{\pi_{12}}R_i},}                    \tag{0.1}
\]

where \(R_i\) is the exact tail-to-factorial likelihood ratio of position
\(i\).  Formula (0.1), rather than the full range of \(a_i\), is the live
tail-relative one-body statistic.

For the directionally centered pair response, let

\[
 c_{g,i}={\operatorname {Cov}_{\nu_i}(K,L_g)
                   \over\mathbb E_{\nu_i}L_g}.             \tag{0.2}
\]

Here \(\nu_i\) is the survival-weighted second-carrier law after fixing a
representative first carrier at position \(i\), \(K\) is the signed
two-star kernel, and \(L_g\) is the second-carrier conditional degree
profile for the weight \(g\).  The complete first-kernel difference is

\[
 \boxed{
 \Delta_{2,c}:=
 \mathbb E_{\lambda_{12}}\overline K_2
       -\mathbb E_{\lambda_c}\overline K_2
 =-{\operatorname {Cov}_{\pi_{12}}(b_i,R_i)
        \over\mathbb E_{\pi_{12}}R_i}
   +\mathbb E_{\pi_c}(c_{12,i}-c_{c,i}),}                 \tag{0.3}
\]

with \(b_i=a_i+c_{12,i}\).  Thus the exact \(s=2\) reference target is a
signed sum of

* one finite position-likelihood covariance, and
* one within-position change of the connected second-carrier response.

Neither term is replaced by an absolute range.  They may also cancel each
other, and \(\Delta_{2,c}\) itself remains inside the signed sum over
\(2\le s\le12\).

There is an equally exact nested form.  Let \(\nu_{12,i}^{\rm tail}\) be
the second-carrier law at position \(i\), additionally tilted by
\(L_{12}(F_i,H)\), and put

\[
 S_i(H)={L_c(F_i,H)\over L_{12}(F_i,H)}.                  \tag{0.4}
\]

Then \(R_i=\mathbb E_{\nu_{12,i}^{\rm tail}}S_i\), and

\[
 \boxed{
 \Delta_{2,c}
 =-{\operatorname {Cov}_{\pi_{12}}(b_i,R_i)\over\overline R}
  -\mathbb E_{\pi_c}
    \left[{\operatorname {Cov}_{\nu_{12,i}^{\rm tail}}(K,S_i)
                    \over R_i}\right].}                   \tag{0.5}
\]

Thus both surviving pieces are signed likelihood-ratio covariances: one
between puncture positions and one between second-carrier labels inside a
fixed position.

## 1. Rooted position types

Put \(b=2r+1\), and let \(\mathcal C_r\) be the complete directed-
punctured catalogue.  A row has the canonically oriented tagged
containment path

\[
 L_1,M_1,L_2,M_2,\ldots,L_{2r},M_{2r}.                    \tag{1.1}
\]

The endpoints lie on different tagged shores, so every rooted flag
\((v,F)\), with \(v\in F\), has a canonical position
\(i\in\{1,\ldots,2r\}\) within its shore.  Coordinate relabeling is
transitive on flags of a fixed shore and position.  For a fixed root
target \(v\in V_\sigma\), exactly

\[
 N_\sigma={D_\sigma\over2r}                              \tag{1.2}
\]

rows through \(v\) place it at each position.  Indeed prescribe the
retained start of \(v\), then order its labels and its complement; this
gives \(|v|!(b-|v|)!=D_\sigma/(2r)\) rows.

Retain every target independently with its shore probability.  Write
\(F\preceq X\) when the row survives, let

\[
 d=d_v(X)=|\{F\in\mathcal C_r:v\in F, F\preceq X\}|,      \tag{1.3}
\]

and let \(q_{FH}=\Pr(F,H\preceq X)\) for distinct root rows.

The signed two-star kernel \(K(F,H)\) is the root-reduced Möbius kernel:
for a further row \(G\), put

\[
 A=(G\cap F)-\{v\},\qquad B=(G\cap H)-\{v\}.             \tag{1.4}
\]

Its contribution is zero unless \(A,B\ne\varnothing\), and otherwise is

\[
 k_G(F,H)=
 \begin{cases}
 p_v^{-1}\{w(A\cup B)-w(A)-w(B)+1\},&v\in G,\\[3pt]
 w(A\cup B)-w(A)-w(B),&v\notin G,
 \end{cases}                                             \tag{1.5}
\]

where \(w(S)=\prod_{u\in S}p_u^{-1}\).  Thus

\[
                         K(F,H)=\sum_{G\in\mathcal C_r}k_G(F,H). \tag{1.6}
\]

For a representative first carrier \(F_i\) of position \(i\), define

\[
 A_i=\sum_{H\ne F_i}q_{F_iH},\qquad
 \nu_i(H)={q_{F_iH}\over A_i},\qquad
 a_i=\mathbb E_{\nu_i}K(F_i,H).                           \tag{1.7}
\]

All three quantities depend only on \(\sigma,i\), not on the chosen
representative.

## 2. Exact position likelihoods

For a nonnegative function \(g\), put

\[
 L_g(F,H)=\mathbb E[g(d)\mid F,H\preceq X],                \tag{2.1}
\]

and, for a representative \(F_i\),

\[
 \ell_{g,i}=\mathbb E_{\nu_i}L_g(F_i,H).                  \tag{2.2}
\]

The exact statewise extension count gives

\[
 \boxed{
 A_i\ell_{g,i}
 =\mathbb E[\mathbf1_{\{F_i\preceq X\}}(d-1)g(d)].}      \tag{2.3}
\]

Define

\[
 W_{g,i}:=A_i\ell_{g,i},\qquad
 \pi_g(i)={W_{g,i}\over\sum_{j=1}^{2r}W_{g,j}}.          \tag{2.4}
\]

Because every position orbit has the same size (1.2), \(\pi_g\) is
exactly the position marginal of the one-carrier law

\[
 \omega_g(F)\ \propto\
 \mathbb E[\mathbf1_{\{F\preceq X\}}(d-1)g(d)].           \tag{2.5}
\]

At the literal Gate-A order, put

\[
 g_{12}(d)=(d-2)_{10},\qquad
 g_c(d)={(d-c)_+^{12}\over(d)_2},\qquad c\ge11,           \tag{2.6}
\]

with value zero whenever the displayed extension count or denominator is
unavailable.  Hence

\[
 W_{12,i}=\mathbb E[\mathbf1_{\{F_i\preceq X\}}(d-1)_{11}], \tag{2.7}
\]

\[
 W_{c,i}=\mathbb E\left[\mathbf1_{\{F_i\preceq X\}}
                    {(d-c)_+^{12}\over d}\right].        \tag{2.8}
\]

Product measure has full support, so \(W_{12,i}>0\).  Assuming the tail
mass is positive, define

\[
 R_i={W_{c,i}\over W_{12,i}},\qquad
 \overline R=\mathbb E_{\pi_{12}}R_i.                    \tag{2.9}
\]

Then

\[
 \pi_c(i)={\pi_{12}(i)R_i\over\overline R}.              \tag{2.10}
\]

### Theorem 2.1 (signed finite-position regression)

Equation (0.1) holds.  More generally, for every real position profile
\(u_i\),

\[
 \boxed{
 \mathbb E_{\pi_{12}}u_i-\mathbb E_{\pi_c}u_i
 =-{\operatorname {Cov}_{\pi_{12}}(u_i,R_i)\over\overline R}.} \tag{2.11}
\]

#### Proof

The first equality in (0.1) is (2.4)--(2.5) and the equal orbit sizes.
Substitute (2.10):

\[
 \mathbb E_{\pi_c}u_i
 ={\mathbb E_{\pi_{12}}u_iR_i\over\overline R}.
\]

Subtract this from \(\mathbb E_{\pi_{12}}u_i\).  This is (2.11), and
\(u_i=a_i\) gives (0.1).  \(\square\)

The Newton-series obstruction remains visible here: \(W_{c,i}\) is a
cutoff-tail transform of the entire conditional degree distribution at
position \(i\), not a fixed list of its moments.

## 3. Conditional pair-connected response

For a position with \(\ell_{g,i}>0\), define \(c_{g,i}\) by (0.2), namely

\[
 c_{g,i}={
 \mathbb E_{\nu_i}[(K(F_i,H)-a_i)
                  (L_g(F_i,H)-\ell_{g,i})]
 \over\ell_{g,i}}.                                      \tag{3.1}
\]

Set \(c_{g,i}=0\) if \(\ell_{g,i}=0\); that position has zero
\(\pi_g\)-mass.  The numerator of (3.1) is a genuine second-carrier
response: both factors have zero \(\nu_i\)-mean.

### Theorem 3.1 (positionwise connected decomposition)

For either weight \(g\),

\[
 \boxed{
 {\sum_{F\ne H}q_{FH}K(F,H)L_g(F,H)\over
       \sum_{F\ne H}q_{FH}L_g(F,H)}
 =\sum_{i=1}^{2r}\pi_g(i)\{a_i+c_{g,i}\}.}               \tag{3.2}
\]

Consequently (0.3) holds.

#### Proof

For a fixed representative \(F_i\),

\[
 \mathbb E_{\nu_i}[K L_g]
 =a_i\ell_{g,i}+\operatorname {Cov}_{\nu_i}(K,L_g)
 =\ell_{g,i}(a_i+c_{g,i}).                               \tag{3.3}
\]

Sum over all first carriers.  There are equally many in every position,
and their unnormalized weights are \(A_i\ell_{g,i}=W_{g,i}\).  Division
gives (3.2).

For \(g_{12}\), the left side of (3.2) is
\(\mathbb E_{\lambda_{12}}\overline K_2\); for \(g_c\), it is
\(\mathbb E_{\lambda_c}\overline K_2\), because

\[
 (d)_2g_{12}(d)=(d)_{12},\qquad
 (d)_2g_c(d)=(d-c)_+^{12}.                               \tag{3.4}
\]

Put \(b_i=a_i+c_{12,i}\).  Subtract the two instances of (3.2), add and
subtract \(\mathbb E_{\pi_c}b_i\), and apply (2.11) to \(b_i\).  This is
(0.3).  \(\square\)

### Corollary 3.2 (nested likelihood-ratio form)

Define the conditional second-carrier laws

\[
 \nu_{g,i}^{\rm tail}(H)
 ={\nu_i(H)L_g(F_i,H)\over\ell_{g,i}}.                    \tag{3.5}
\]

The superscript only distinguishes this tilted law from the baseline
\(\nu_i\); for \(g=g_{12}\) it is the factorial-extension law.  Put

\[
 b_{g,i}:=a_i+c_{g,i}.
\]

Then

\[
 \boxed{b_{g,i}=\mathbb E_{\nu_{g,i}^{\rm tail}}K(F_i,H).} \tag{3.6}
\]

Moreover, with \(S_i\) as in (0.4),

\[
 R_i={\ell_{c,i}\over\ell_{12,i}}
     =\mathbb E_{\nu_{12,i}^{\rm tail}}S_i,               \tag{3.7}
\]

\[
 \boxed{
 b_{12,i}-b_{c,i}
 =-{\operatorname {Cov}_{\nu_{12,i}^{\rm tail}}(K,S_i)
        \over R_i}.}                                      \tag{3.8}
\]

Consequently (0.5) holds.

#### Proof

Equation (3.6) is (3.3) divided by \(\ell_{g,i}\).  Since

\[
 \nu_{c,i}^{\rm tail}(H)
 ={\nu_{12,i}^{\rm tail}(H)S_i(H)\over
       \mathbb E_{\nu_{12,i}^{\rm tail}}S_i},             \tag{3.9}
\]

normalization gives (3.7), and the elementary tilted-expectation identity
gives (3.8).  Finally rewrite the second term of (0.3) as
\(\mathbb E_{\pi_c}(b_{12,i}-b_{c,i})\), then use (3.8).
\(\square\)

Every denominator in (3.5)--(3.9) is positive on a position of positive
tail mass.  A zero-tail position has zero \(\pi_c\)-mass and contributes
zero by convention.

## 4. Exact remaining signed target

The signed \(s=2\) contribution to the product-reference hazard comparison is

\[
 q_0{12\choose2}\Delta_{2,c}.                            \tag{4.1}
\]

It remains inside the positive part of the full signed sum over
\(2\le s\le12\).  A sufficient local scale is

\[
 q_0\left[
 -{\operatorname {Cov}_{\pi_{12}}(b_i,R_i)\over\overline R}
 -\mathbb E_{\pi_c}
   {\operatorname {Cov}_{\nu_{12,i}^{\rm tail}}(K,S_i)\over R_i}
 \right]=o(z),                                          \tag{4.2}
\]

uniformly in the relevant deterministic thresholds, with cancellation
retained.  The exact coefficient-one requirement is the corresponding
cumulative signed bound after division by \(Z\), together with the higher
Möbius kernels.

Equation (4.2) separates two boundary-polymer tasks:

1. compare the full conditional root-degree tails across the \(2r\)
   puncture positions in the signed covariance with \(b_i\); and
2. control the signed likelihood covariance of the two-star kernel with
   the tail-to-factorial ratio \(S_i\) within each position.

Neither task permits division by a generic global \(L^2\) bound.  Nor is
it enough to show that the full range of \(a_i\) is small.

## 5. Why the range shortcut is not being used

The deterministic inequality

\[
 |\mathbb E_{\pi_{12}}a-\mathbb E_{\pi_c}a|
 \le\operatorname {osc}_i a_i                            \tag{5.1}
\]

is true but appears structurally too strong.  It discards the exact
likelihood covariance (0.1).  The following computations are evidence
only and are not premises of any theorem in this note.

* A complete floating-point \(r=3\) census at equal shore retention
  \(p=0.9\) gives \(q_0\operatorname {osc}(a_i)/z\approx0.14053\).
* A seeded unbiased catalogue Monte Carlo, validated against that census,
  gives observed values about \(0.213,0.262,0.342\) at
  \(r=4,5,6\), again at \(p=0.9\).  The per-position naive standard errors
  were at most \(0.0051,0.0102,0.0143\), respectively.

These finite computations do not prove a nonzero asymptotic limit.  They
do show that an \(o(z)\) oscillation theorem should not be inserted into
the proof without a new argument.  At \(r=2\), the exact checker below
also shows strong cancellation: the one-body factorial-to-tail shift is
tiny compared with the range of the position profile.

The exhaustive \(r=3\) program is

`scratch/research_gate_a_r3_two_star_position_profile_20260822.cpp`,

and the seeded sampler is

`scratch/research_gate_a_two_star_position_monte_carlo_20260822.cpp`.

## 6. Exact checker

The script

`scratch/verify_gate_a_two_star_position_weight_regression_20260822.py`

uses the complete \(r=2\) punctured catalogue, its full root star, literal
order \(m=12\), and rational arithmetic.  It verifies the equal position-
orbit sizes, (2.3), the likelihood-ratio covariance (2.11), the
positionwise connected decomposition (3.2), and the combined identity
(0.3) for the factorial and cutoff-tail weights.
