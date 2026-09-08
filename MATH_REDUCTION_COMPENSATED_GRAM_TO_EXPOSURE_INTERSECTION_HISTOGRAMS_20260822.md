# The dimensionless compensated Gram is an exposure-intersection histogram gate

**Date:** 2026-08-22

**Status:** unconditional exact all-`r`, all-module reduction, with exact
`r=4,5` evaluations.  No asymptotic lower bound for the exposure determinant
is claimed.

## 1. Position vectors and the quantity to be bounded

Fix `r>=4`, put

\[
 b=2r+1,\qquad k=r-2,
\]

and identify a word with a coordinate relabeling of the identity word on
the position cycle `Z_b`.  For `s in {r,r-1,k}`, write `X_s` for the
`s`-subsets of `Z_b`.

The two punctured central position vectors are

\[
 c_r(S)=\mathbf1\{S=I_r(a),\ 1\le a\le b-1\},
 \qquad
 c_{r-1}(S)=\mathbf1\{S=I_{r-1}(a),\ 1\le a\le b-1\}.          \tag{1.1}
\]

The full shallow vector is

\[
                         q_k(S)=\mathbf1\{S=I_k(a),\ a\in Z_b\}.          \tag{1.2}
\]

Let `E_0` be the identity punctured configuration and define its two
unnormalized rooted-exposure vectors by

\[
 e_s(S)=\sum_{F:S\in F_s}(|F\cap E_0|-1)_+,
 \qquad s\in\{r,r-1\}.                              \tag{1.3}
\]

Here layer tags are retained in `F cap E_0`.  Dividing exposure rows by
their positive complete-catalogue target degrees only rescales the vectors
and has no effect on the span or on the angle below.

For `lambda=(b-j,j)`, `2<=j<=k`, let `m` be the shallow multiplicity
vector and let `M_B` be the span of the two central and two exposure
multiplicity vectors.  The dimensionless compensated loss is

\[
 \alpha_{r,j}={\|\operatorname {proj}_{M_B^\perp}m\|^2\over\|m\|^2}.
                                                               \tag{1.4}
\]

If `theta_(r,j)` is the exact unconstrained Fisher eigenvalue and
`p=b/binom(b,k)` is the uniform target marginal, the natural relative-
density compensated squared eigenvalue is

\[
 \boxed{\widehat\sigma_{r,j}^2
       =\alpha_{r,j}\Theta_{r,j},
 \qquad \Theta_{r,j}={\theta_{r,j}\over p^2}.}                 \tag{1.5}
\]

The factor `Theta` has the closed cyclic-overlap formula proved in the
Fisher-scale note.  This note computes `alpha` from five explicit position
vectors.

## 2. A closed cross-rank harmonic kernel

Choose disjoint labelled pairs `(a_i,b_i)`, `1<=i<=j`, and for every
`s>=j` put

\[
 H_s(A)=\prod_{i=1}^{j}
       (\mathbf1_{\{a_i\in A\}}-\mathbf1_{\{b_i\in A\}}),
 \qquad A\in{[b]\choose s}.                         \tag{2.1}
\]

This is the inclusion lift of one harmonic `j`-set vector and belongs to
the unique `V_(b-j,j)` copy in the `s`-set module.  The different `H_s`
represent the same abstract irreducible vector up to a nonzero scalar.

For `s,t>=j` and a feasible intersection size `ell`, let

\[
 D_{s,t}(\ell)={b\choose s}{s\choose\ell}
                         {b-s\choose t-\ell}.                  \tag{2.2}
\]

With an invalid multinomial interpreted as zero, define

\[
\begin{aligned}
 Z_{s,t,j}(\ell)
 &=2^j\sum_{c=0}^{j}(-1)^{j-c}{j\choose c}\\
 &\quad\cdot {b-2j\choose
       \ell-c,\ s-j-\ell+c,\ t-j-\ell+c,\ b-s-t+\ell-c},    \tag{2.3}\\
 \zeta_{s,t,j}(\ell)&={Z_{s,t,j}(\ell)\over D_{s,t}(\ell)}. \tag{2.4}
\end{aligned}
\]

### Lemma 2.1

If `g` is a uniform coordinate permutation and `S in X_s`, `T in X_t`
have `|S cap T|=ell`, then

\[
 \boxed{\mathbb E_g[H_s(gS)H_t(gT)]=\zeta_{s,t,j}(\ell).}     \tag{2.5}
\]

#### Proof

The ordered image pair `(gS,gT)` is uniform among the `D_(s,t)(ell)`
pairs of subsets with sizes `s,t` and intersection `ell`.

For a nonzero summand, each distinguished coordinate pair is split by
each image subset.  Suppose the two subsets make the same choice on `c`
of the `j` pairs.  There are `2^j binom(j,c)` choice patterns, their sign
product is `(-1)^(j-c)`, and they contribute `c` elements to the
intersection.  On the remaining `b-2j` labels the four Venn cells have
sizes

\[
 \ell-c,\quad s-j-\ell+c,\quad t-j-\ell+c,
 \quad b-s-t+\ell-c.                              \tag{2.6}
\]

The multinomial in (2.3) assigns those labels.  Summing over `c` and
dividing by (2.2) proves (2.5). `square`

## 3. Exact five-vector Gram from intersection histograms

For a coefficient vector `x` on `X_s`, put

\[
                         R_x(g)=\sum_{S\in X_s}x(S)H_s(gS).   \tag{3.1}
\]

For coefficient vectors `x` on `X_s` and `y` on `X_t`, define their
intersection histogram

\[
 \mathcal H_{x,y}(\ell)
   =\sum_{\substack{S\in X_s,T\in X_t\\|S\cap T|=\ell}}
                    x(S)y(T).                                \tag{3.2}
\]

### Theorem 3.1 (factorial catalogue eliminated)

The exact Gram entry of the two module row functions is

\[
 \boxed{
 \langle R_x,R_y\rangle_{L^2(S_b)}
 =\sum_\ell\mathcal H_{x,y}(\ell)\zeta_{s,t,j}(\ell).}       \tag{3.3}
\]

Take the five coefficient vectors, in order,

\[
                         c_r,\ c_{r-1},\ e_r,\ e_{r-1},\ q_k.            \tag{3.4}
\]

Let `G_(r,j)` be their `5 by 5` Gram matrix computed by (3.3), let `G_B`
be its leading `4 by 4` block, and let `g` be the first four entries of
its last column.  Then

\[
 \boxed{
 \alpha_{r,j}=1-{g^{\mathsf T}G_B^\dagger g\over G_{55}}.}   \tag{3.5}
\]

If `G_B` is nonsingular, equivalently

\[
 \boxed{
 \alpha_{r,j}={\det G_{r,j}\over G_{55}\det G_B}.}           \tag{3.6}
\]

#### Proof

Equation (3.3) is (2.5) summed with coefficients `x(S)y(T)`.  The row
function (3.1) is the matrix coefficient obtained by pairing the target
rows with the harmonic vector `H_s`.  Normalizing the different `H_s`
only independently rescales the five vectors; this neither changes the
constraint span nor the residual fraction.  Hence their Gram residual is
exactly (1.4).  Orthogonal projection gives (3.5), and the Schur determinant
identity gives (3.6). `square`

Thus all factorially many catalogue columns disappear from the Gram
calculation.  The remaining all-`r` data are the intersection histograms
involving the two exposure vectors (1.3).  The histograms involving only
`c_r,c_(r-1),q_k` are elementary cyclic-arc counts.

## 4. Exact finite calibration

Literal complete-catalogue exposure enumeration followed by (3.3)--(3.6)
gives

\[
 \boxed{
 \alpha_{4,2}
 ={189833430275409744043\over952911127398052338603}
 =0.1992142024\ldots}                               \tag{4.1}
\]

and

\[
\boxed{\begin{aligned}
 \alpha_{5,2}
 &= {25610183932380883339249166148
       \over280256277166865583655644272238}
    =0.0913813035\ldots,\\
 \alpha_{5,3}
 &= {2824584316655122245743670177
       \over5429668689045287473387817249}
    =0.5202130145\ldots.
\end{aligned}}                                                \tag{4.2}
\]

Using

\[
 \Theta_{4,2}=4,\qquad
 \Theta_{5,2}={180\over7},\qquad
 \Theta_{5,3}={75\over7},                                  \tag{4.3}
\]

the natural compensated squared eigenvalues are

\[
\boxed{\begin{aligned}
 \widehat\sigma_{4,2}^2
 &= {759333721101638976172\over952911127398052338603}
    =0.7968568099\ldots,\\
 \widehat\sigma_{5,2}^2
 &= {109757931138775214311067854920
       \over46709379527810930609274045373}
    =2.3498049481\ldots,\\
 \widehat\sigma_{5,3}^2
 &= {211843823749134168430775263275
       \over38007680823317012313714720743}
    =5.5737108700\ldots.
\end{aligned}}                                                \tag{4.4}
\]

These values quantitatively strengthen the earlier modular rank tests at
`r=4,5`.  They are calibration, not an asymptotic extrapolation.

## 5. Exact remaining scalar gate

There is no finite evidence here for a true exponential obstruction in the
natural relative-density norm: all three values in (4.4) are bounded away
from zero.  Conversely, two ranks cannot prove a uniform lower bound.

The exact complete-catalogue problem is now:

\[
 \boxed{
 \inf_{2\le j\le r-2}
 \alpha_{r,j}\Theta_{r,j}\ge r^{-C}?}                       \tag{5.1}
\]

By (2.3)--(3.6), this is a determinant inequality for the intersection
histograms of `e_r,e_(r-1)`.  Aggregate duplicate moments alone do not
establish it: (3.6) is sensitive to signed harmonic cancellations between
the two exposure shores.  A proof needs either

1. asymptotic formulas with errors for all exposure histograms in (3.2),
   uniform in `j`; or
2. a direct lower bound on the harmonic distance of `q_k` from the four
   vectors in (3.4).

Even a proof of (5.1) remains only the Hilbert-space part of Gate B.  A
polynomial relative-`l_infinity` simultaneous inverse and stopped-residual
stability are still separate requirements.

## 6. Exact verifiers

The standard-library `r=4` checker is

```text
python3 scratch/verify_r4_dimensionless_compensated_gram_angle_20260822.py
```

It independently verifies (2.3)--(2.5) by literal harmonic averaging,
enumerates the complete exposure vector, and checks (4.1) and the first
line of (4.4) as exact rational numbers.

The exact `r=5` checker reuses the independently audited streaming `11!`
exposure enumerator and uses GMP rational arithmetic:

```text
clang++ -std=c++20 -O3 -march=native -pthread -Wall -Wextra -Wpedantic \
  $(pkg-config --cflags gmpxx) \
  scratch/research_r5_compensated_gram_angles_20260822.cpp \
  $(pkg-config --libs gmpxx) \
  -o /tmp/research_r5_compensated_gram_angles_20260822
/tmp/research_r5_compensated_gram_angles_20260822
```

It checks both fractions in (4.2) and the last two lines of (4.4) exactly;
floating output is diagnostic only.
