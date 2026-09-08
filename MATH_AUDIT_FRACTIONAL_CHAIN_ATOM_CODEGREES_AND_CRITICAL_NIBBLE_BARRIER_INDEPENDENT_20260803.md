# Independent audit: fractional chain-atom codegrees and the critical nibble barrier

**Date:** 2026-08-03  
**Audited source:**
`MATH_THEOREM_FRACTIONAL_CHAIN_ATOM_CODEGREES_AND_CRITICAL_NIBBLE_BARRIER_20260803.md`  
**Source SHA-256:**
`7eca907ebf10be4671360a6f48c8ef7df4ed9e7fb5538f4a3d2e413c98541826`

## Verdict

**GO.**  The exact codegree ledger, the uncollared critical obstruction, the
collar statement with its now-explicit exchangeable-law scope, the constants,
and the ABKV non-applicability conclusion are correct.

The corrected source now states exactly the scope proved in Section 3: the
same exchangeable owner-chain law after removing the top `a` rank classes,
or a symmetrized residual law retaining the uniform-order flag formulas.  It
also explicitly excludes an arbitrary fixed named prechainization that can
condition the residual ordering and physically restrict compatible atoms.

The two normalization definitions needed by the proof are now explicit:

* `K=1+max{|R|: Pr(R)>0}` is the maximum supported atom cardinality,
  counting its owner vertex;
* `rho_2` is taken over pairs of supported positive-degree vertices.

No further theorem correction is required.

## Checks

### 1. Exact degrees and all flag codegrees

For a fixed owner containing a rank-`s` target `S`, a uniform owner ordering
has `S` as its initial `s`-set with probability `1/binom(r,s)`.  Multiplying
by `q_s` and by the number `binom(2r-s,r-s)` of containing owners gives

\[
 d_x(S)=\frac{\binom{2r-s}{r-s}q_s}{\binom rs}
       =\frac{q_s}{p_s}.
\]

The owner-target formula (1.2) follows from the same one-owner calculation.

Several distinct-rank initial subsets of one ordering must form a flag.  For
a prescribed flag of ranks `s_1<...<s_j`, the probability within a fixed
containing owner is

\[
 \frac{\eta_{s_1,\ldots,s_j}}
 {\binom r{s_j}\binom{s_j}{s_{j-1}}\cdots\binom{s_2}{s_1}},
\]

which verifies (1.3)--(1.4).  Direct cancellation verifies both normalized
pair identities in (1.5).  Collections containing two owners, incomparable
targets, or two distinct targets of the same rank have zero codegree, so the
ledger is complete.

### 2. Forced adjacent-top correlation

The referenced fractional construction has `0<=q_s<=p_s`.  Missing target
load `o(W)` is therefore exactly

\[
 W\sum_{s<r}(p_s-q_s)=o(W).
\]

Since

\[
 p_{r-1}=\frac r{r+1},\qquad
 p_{r-2}=\frac{r(r-1)}{(r+1)(r+2)},
\]

both top marginals are `1-o(1)`.  Inclusion--exclusion forces
`eta_{r-2,r-1}=1-o(1)`, and (1.5) gives

\[
 \frac{d_x(S,U)}{d_x(U)}
 =\frac{1-o(1)}{r-1}=\frac{1-o(1)}r.
\]

Normalizing by the smaller endpoint degree can only increase this ratio,
so (0.1) follows.

### 3. Atom size and the `pi/4` constant

For `k=2r`,

\[
 \frac{\Lambda}{W}
 =\left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt r.
\]

Thus `E|R|` has this value up to `o(1)`, and a supported atom has at least
that many target vertices.  With the explicit definition of `K` above,

\[
 K^2\rho_2
 \ge\left(\frac{\pi}{4}+o(1)\right)r\,
      \frac{1-o(1)}r
 =\frac\pi4-o(1).
\]

The constant in (0.3) is correct.

### 4. Collar threshold and its quantifier

Within the residual exchangeable law, deleting the top `a` rank classes
leaves highest ranks `r-a-2` and `r-a-1`.  For `a=o(sqrt(r))`, both binomial
ratios tend to one and the same `1/r` pair-correlation lower bound survives;
the deleted `o(sqrt(r))` expected targets do not change the leading atom-size
constant.

For `a=(c+o(1))sqrt(r)`, both highest residual marginals tend to
`exp(-c^2)`.  Inclusion--exclusion forces joint mass at least
`(2exp(-c^2)-1)_+-o(1)`.  Its vanishing requires

\[
 c\ge\sqrt{\log2}.
\]

Since `d=(sqrt(pi)/2+o(1))sqrt(r)`, the ratio is

\[
 \frac{\sqrt{\log2}}{\sqrt\pi/2}
 =2\sqrt{\frac{\log2}{\pi}}
 =0.939437\ldots,
\]

so (0.4) and `0.9394` are numerically correct.  This remains only a
necessary threshold.

The proof does **not** show that an arbitrary fixed named collar can be
prechainized and then ignored while retaining the exchangeable residual atom
law: compatibility may alter the available owner orderings and residual
atoms.  The corrected source now states this exclusion explicitly, so its
collar quantifier is proof-safe.

### 5. ABKV citation and hypothesis failure

The primary paper is N. Alon, B. Bollobas, J. H. Kim, and V. H. Vu,
*Economical covers with geometric applications*, Proc. London Math. Soc.
86 (2003), 273--301.  Its condition (8), inherited by Theorem 3.9, is

\[
 C=o\!\left(\frac{D}{e^{2K}\log D}\right),
\]

along with the stated near-regular degree window; Theorem 3.9's matching
leave for `K>4` is

\[
 O\!\left(K\left(\frac{C\log(1+C)}D\right)^{1/(K-1)}|V|\right)
\]

plus the exceptional low-degree set.  Thus equations (4.1)--(4.2) quote the
relevant hypothesis and error factor correctly.

In a favorable regular-uniform blow-up preserving the saturated normalized
pair codegree, `C/D>=(1-o(1))/r` and `K=Omega(sqrt(r))`.  Hence

\[
 e^{2K}(C/D)\log D
 \ge \frac{e^{2K}\log D}{(1+o(1))r}\to\infty,
\]

so the ABKV hypothesis fails.  Its displayed leave factor is also far from
`o(r^{-1/2})`.  The source correctly treats this only as failure of a
black-box theorem, not as a nonexistence result.

Primary-source check: <https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf>.
