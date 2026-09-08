# Every localized initial-colex cut passes protected Ore

**Date:** 2026-08-04  
**Status:** unconditional asymptotic pure-mathematical theorem.  For the
constant-spread protected reservoir, every initial-colex complement in the
small-side localization satisfies the exact protected Ore inequality.
The proof combines the nested Macaulay gate current with a uniform scalar
estimate and absorbs the complete aperture-one tail.  It does not assert
that an arbitrary shifted or positive-defect cut is initial colex.

No computation, search, or solver result is used.

## 0. Setting

Put

\[
 n=2m-1,
 \qquad \mathcal L=\binom{[n]}{m-1}.
\]

Let `P` be the frozen constant-spread protected reservoir.  For a lower
cut `A`, write

\[
 \mu_P(A)=\sigma(A)-\lambda_P(A).
\]

The reservoir supplies the two uniform estimates

\[
 \boxed{\lambda_P(A)\le15|A|+2m}
\tag{0.1}
\]

for every cut and

\[
 \boxed{\lambda_P(\{x\})\le10}
\tag{0.2}
\]

for every lower vertex.

Let `F` be an initial colex segment of the `m`-sets with canonical
expansion

\[
 |F|=\sum_{j=s}^m\binom{c_j}{j},
 \qquad
 c_m>c_{m-1}>\cdots>c_s\ge s,
\tag{0.3}
\]

and put

\[
 \rho_j=c_j-j+1,
 \qquad b_j=\binom{c_j}{j}.
\tag{0.4}
\]

Let `A` be the lower-shore complement of `F`.  Thus `|A|=|F|`, and the
canonical Macaulay theorem expresses `A` both as a disjoint union of
two-sided intervals and as its principal-star DNF.

Assume the small-side localization

\[
 \boxed{|F|=O(m^2 2^m).}
\tag{0.5}
\]

The isolated endpoint `c_m=n` is the complete `m`-shore.  It violates
(0.5) for all sufficiently large `m`; independently, its complement is
the complete lower shore and is trivially safe.

## 1. Localization of the largest aperture

The aperture sequence is nondecreasing, because

\[
 \rho_{j+1}-\rho_j=c_{j+1}-c_j-1\ge0.
\tag{1.1}
\]

Put

\[
 r=\rho_m.
\tag{1.2}
\]

### Lemma 1.1 (top aperture is below one half)

Under (0.5), for all sufficiently large `m`,

\[
 \boxed{r<{m\over2}.}
\tag{1.3}
\]

#### Proof

The top term gives

\[
 |F|\ge b_m=\binom{m+r-1}{m}.
\]

If `r>=m/2`, its exponential rate is at least

\[
 {3\over2}H_2(1/3)>1,
\]

whereas the right side of (0.5) has rate one.  This is impossible for all
sufficiently large `m`. \(\square\)

## 2. All apertures at least two: small top aperture

First assume

\[
 \rho_j\ge2
\qquad(s\le j\le m).
\tag{2.1}
\]

The nested-gate active-core law shows that every nonempty owner fibre has
size at most `r+1`.  Since every lower vertex has degree `m`,

\[
 m|A|\le(r+1)|N(A)|.
\]

All nonempty fibres are two-covered, so

\[
 \boxed{
 \sigma(A)=2(|N(A)|-|A|)
 \ge {2(m-r-1)\over r+1}|A|.}
\tag{2.2}
\]

### Lemma 2.1 (small-aperture margin)

If `2<=r<=m/10`, then every nonempty `A` satisfying (2.1) is safe.  In
fact, for all sufficiently large `m`,

\[
 \boxed{\mu_P(A)>66.}
\tag{2.3}
\]

#### Proof

Uniformly for `r<=m/10`, the coefficient in (2.2) is at least `35/2`
once `m` is sufficiently large.

Suppose first that `|A|>=2m+1`.  Equations (0.1) and (2.2) give

\[
\begin{aligned}
 \mu_P(A)
 &\ge\left({2(m-r-1)\over r+1}-15\right)|A|-2m\\
 &\ge {5\over2}|A|-2m
 \ge3m+{5\over2}>66.
\end{aligned}
\tag{2.4}
\]

It remains to consider `0<|A|<2m+1`.  A single clause of aperture at
least three already has size

\[
 \binom{m+2}{2}>2m.
\]

Two distinct aperture-two clauses each have size `m+1` and intersect in
at most one lower vertex, so their union has size at least `2m+1`.
Therefore the only remaining case is one aperture-two principal star.
It has size `m+1` and exact slack

\[
 \sigma(A)=(m-2)(m+1).
\]

Using (0.1),

\[
 \mu_P(A)
 \ge(m-2)(m+1)-15(m+1)-2m
 =m^2-18m-17>66
\]

for all sufficiently large `m`. \(\square\)

## 3. All apertures at least two: medium top aperture

Now assume

\[
 {m\over10}le r<{m\over2}.
\tag{3.1}
\]

For every Macaulay term define

\[
 g_j=\left({j\over\rho_j}-1\right)b_j.
\tag{3.2}
\]

The exact nested-gate scalar identity is

\[
 \boxed{{\sigma(A)\over2}=\sum_{j=s}^m g_j.}
\tag{3.3}
\]

The top term is

\[
 \boxed{
 g_m=\left({m\over r}-1\right)
      \binom{m+r-1}{r-1}.}
\tag{3.4}
\]

### Lemma 3.1 (all negative Macaulay credit is small)

One has

\[
 \boxed{
 \sum_{j:g_j<0}(-g_j)
 \le\binom{2r-1}{r-1}-1.}
\tag{3.5}
\]

#### Proof

A negative term satisfies `j<rho_j<=r`.  Since
`c_j=j+rho_j-1`,

\[
 -g_j
 =\left(1-{j\over\rho_j}\right)
   \binom{j+\rho_j-1}{j}
 \le\binom{j+r-1}{j}.
\]

Summing over the possible indices `1<=j<=r-1` and using the hockey-stick
identity gives

\[
 \sum_{j=1}^{r-1}\binom{j+r-1}{j}
 =\binom{2r-1}{r-1}-1.
\]

This proves (3.5). \(\square\)

For the constant-spread trace count put

\[
 N_q=H_q(m)+m+H_d,
 \qquad H_q(m)=\sum_{i=0}^q\binom mi.
\tag{3.6}
\]

The nested current theorem and monotonicity of `N_q` give

\[
\begin{aligned}
 \lambda_P(A)
 &\le2\sum_t|X_t|N_{\rho^{(t)}}\\
 &\le2mN_r,
\end{aligned}
\tag{3.7}
\]

because the disjoint run widths sum to at most `m`.

### Lemma 3.2 (uniform entropy domination)

Uniformly under (3.1),

\[
 \boxed{
 g_m-\binom{2r-1}{r-1}-mN_r\longrightarrow+\infty.}
\tag{3.8}
\]

In fact the left side has the exponential order of `g_m`.

#### Proof

Put `alpha=r/m`.  Uniform Stirling estimates on
`alpha in [1/10,1/2]` give

\[
 \log_2 g_m=f(\alpha)m+O(\log m),
\tag{3.9}
\]

where

\[
 f(\alpha)
 =(1+\alpha)\log_2(1+\alpha)
   -\alpha\log_2\alpha.
\tag{3.10}
\]

On the other hand,

\[
 \log_2(mN_r)\le H_2(\alpha)m+o(m)
\tag{3.11}
\]

and

\[
 \log_2\binom{2r-1}{r-1}
 \le2\alpha m+o(m).
\tag{3.12}
\]

The first exponent gap is

\[
 f(\alpha)-H_2(\alpha)
 =(1+\alpha)\log_2(1+\alpha)
  +(1-\alpha)\log_2(1-\alpha)>0.
\tag{3.13}
\]

It is uniformly positive on `[1/10,1/2]`.  The second gap is also
uniformly positive there.  Indeed `f(alpha)-2alpha` is concave, and its
values at both endpoints are positive:

\[
 f(1/10)-1/5>0,
 \qquad
 f(1/2)-1={3\over2}\log_2(3/2)-{1\over2}>0.
\tag{3.14}
\]

Thus `g_m` exponentially dominates both quantities in (3.8), uniformly
over the whole interval. \(\square\)

### Corollary 3.3 (medium-aperture margin)

Under (2.1) and (3.1), for all sufficiently large `m`,

\[
 \boxed{\mu_P(A)>66.}
\tag{3.15}
\]

#### Proof

Discard every positive term in (3.3) except `g_m` and apply Lemma 3.1:

\[
 {\sigma(A)\over2}
 \ge g_m-\binom{2r-1}{r-1}.
\]

Together with (3.7),

\[
 \mu_P(A)
 \ge2\left(
 g_m-\binom{2r-1}{r-1}-mN_r
 \right).
\]

Lemma 3.2 makes the right side larger than 66. \(\square\)

## 4. The aperture-one tail

Because the aperture sequence is nondecreasing, all indices with
`rho_j=1`, if any, form one initial interval of Macaulay indices.  On this
tail

\[
 c_j=j,
 \qquad b_j=1.
\tag{4.1}
\]

### Lemma 4.1 (the total erosion debt is at most 66)

If `A^head` is the union of all blocks with aperture at least two, then

\[
 \boxed{\mu_P(A)\ge\mu_P(A^{\rm head})-66.}
\tag{4.2}
\]

#### Proof

The exact Macaulay head--tail erosion theorem gives

\[
 \mu_P(A)
 \ge\mu_P(A^{\rm head})
   +\sum_{j:\rho_j=1}(j-12).
\]

The complete negative part of the last sum is

\[
 \sum_{j=1}^{11}(j-12)=-66.
\]

Any actual consecutive tail omits some of these negative terms or adds
nonnegative terms, proving (4.2). \(\square\)

If the head is nonempty, it is itself a localized canonical initial-colex
complement with all apertures at least two and the same top aperture `r`.
Lemmas 2.1 and Corollary 3.3 therefore give

\[
 \mu_P(A^{\rm head})>66.
\tag{4.3}
\]

Combining (4.2)--(4.3) proves `mu_P(A)>=0`.

It remains only to treat the case in which every aperture equals one.

### Lemma 4.2 (the pure aperture-one run is safe)

If every Macaulay term has aperture one, then `A` is safe for all
sufficiently large `m`.

#### Proof

The common-root representation writes

\[
 A=\{R\cup\{x\}:x\in X\},
 \qquad |R|=m-2,
 \qquad h=|X|\le m.
\tag{4.4}
\]

Every upper owner contains at most two selected facets.  The regular
slack identity therefore gives

\[
 \boxed{\sigma(A)=h(m-2).}
\tag{4.5}
\]

The exact path-forest identity, (0.2), and the fact that there are exactly
`binom(h,2)` owners containing two selected facets give

\[
 \lambda_P(A)
 \le10h+\binom h2.
\tag{4.6}
\]

Since `h<=m`,

\[
 h(m-2)-10h-\binom h2
 =h\left(m-12-{h-1\over2}\right)\ge0
\]

for all sufficiently large `m`. \(\square\)

## 5. Main theorem

### Theorem 5.1 (localized initial-colex Ore closure)

For the constant-spread protected reservoir and all sufficiently large
`m`, every initial colex segment satisfying (0.5) has a lower-shore
complement `A` satisfying

\[
 \boxed{\lambda_P(A)\le\sigma(A).}
\tag{5.1}
\]

Equivalently,

\[
 \boxed{\mu_P(A)\ge0.}
\tag{5.2}
\]

#### Proof

Lemma 1.1 gives `r<m/2`.  If every aperture is at least two, apply
Lemma 2.1 when `r<=m/10` and Corollary 3.3 when `r>=m/10`.

If an aperture-one tail and a nonempty head are both present, apply
Lemma 4.1 and the strict head margins (2.3), (3.15).  If the head is empty,
apply Lemma 4.2.  These cases exhaust the canonical expansion. \(\square\)

## 6. What this closes and what it does not

The theorem closes the entire canonical initial-colex family left by the
small-side localization.  In particular:

* constant-aperture runs no longer need separate width restrictions;
* all strict aperture jumps compose without an additional current;
* all negative Macaulay block credits are absorbed by the top block; and
* the complete aperture-one tail costs at most 66 and is absorbed exactly.

The theorem is not, by itself, a proof that every residual low-expansion
cut is safe.  A general protected compression theorem would still have to
show that an arbitrary violating cut can be replaced by an initial-colex
cut without decreasing its protected deficit.  The present result proves
that no canonical initial-colex cut can be the obstruction.

## 7. Dependencies

| role | file | SHA-256 |
|---|---|---|
| corrected Macaulay decomposition and erosion | `MATH_THEOREM_MACAULAY_INTERVAL_DNF_EROSION_AND_TRIANGULAR_CROSSING_20260804.md` | `77253694d02d6d11c41a21b9875af843ede525d1751bca7d2463ac014b174cec` |
| corrected common-root run theorem | `MATH_THEOREM_COMMON_ROOT_MACAULAY_RUN_EXACT_CURRENT_20260804.md` | `83db1a8e67e359025a03b0d704feb5aad81aaaae49a3e4f5339eb948edbfd189` |
| nested multi-run current and scalar criterion | `MATH_THEOREM_NESTED_MACAULAY_GATE_MULTI_RUN_CURRENT_20260804.md` | `0e63df633f3d89879b05ec076cb0254a5ab74036b5b7ff10d97225f5d236d5de` |
| constant-spread all-cut bound and localization | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |
