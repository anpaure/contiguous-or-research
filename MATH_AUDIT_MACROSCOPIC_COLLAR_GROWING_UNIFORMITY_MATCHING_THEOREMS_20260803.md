# Audit of black-box matching theorems for the macroscopic-collar law

**Date:** 2026-08-03  
**Status:** proof-safe negative applicability audit.  The macroscopic-collar
law has a genuinely favorable all-codegree profile, and the formal main terms
in the higher-codegree nibble would be strong enough.  No located published
theorem has uniform quantitative dependence in the growing atom size needed
to turn that formal calculation into an `o(W)` integral leave.

## 0. Verdict

Put

\[
 k=2r,\qquad W={2r\choose r}.
\]

For the parity-separated residual law of
`MATH_THEOREM_MACROSCOPIC_COLLAR_PARITY_DECORRELATION_20260803.md`, let
`N` be the number of owner and retained named-target vertices and let `K` be
the maximum atom size.  Then

\[
 N=\Theta(W\sqrt r),\qquad K=\Theta(\sqrt r).
 \tag{0.1}
\]

Consequently an ordinary `o(N)` matching theorem is insufficient.  The
required conclusion is a matching leaving

\[
 o(W)=o(N/K)
 \tag{0.2}
\]

vertices, i.e. relative leave `o(1/K)`.

The conclusions of this audit are as follows.

1. Fixed-uniformity Pippenger--Frankl--Rödl, Pippenger--Spencer, Kahn-type,
   and pseudorandom matching statements cannot be diagonalized merely from
   `K -> infinity` and `Delta_2/D -> 0`; their thresholds depend on both the
   fixed uniformity and the requested error.
2. The Alon--Bollobas--Kim--Vu growing-uniformity hypothesis fails
   exponentially:

   \[
   e^{2K}{\Delta_2\over D}\log D
   \ge e^{\Theta(\sqrt r)}r^{-2},
   \tag{0.3}
   \]

   so it cannot tend to zero.
3. Vu's pair-codegree bound and the Kang--Kuehn--Methuku--Osthus bound are
   quantitatively vacuous here even under formal substitution: their main
   exponent is `Theta(1/K)`, so a ratio `D/Delta_2=Theta(r^2)` produces a
   leave factor `exp(-Theta(log r / sqrt r))=1-o(1)`.
4. Vu's **higher-codegree** theorem is the first real near miss.  The full
   flag ledger formally permits `x=Theta(r^(2/3))`, whose unlogged main term
   is

   \[
   N/x=O(Wr^{-1/6})=o(W).
   \tag{0.4}
   \]

   But the theorem is a fixed-`K` statement and returns
   `O_K(N x^(-1) log^{c_K} D)`; neither `c_K` nor the degree threshold is
   controlled as `K -> infinity`.  The residual atoms are also only
   `K`-bounded, not uniform.  Thus (0.4) is not a valid diagonal conclusion.
5. Gould--Kelly's 2025 full-codegree theorem is even closer.  Its formal
   bottleneck is `B=Theta(r)`, so its unlogged main term would leave

   \[
   N/B=W r^{-1/2+o(1)}=o(W).
   \tag{0.5}
   \]

   Their bounded-hypergraph coloring corollary would also avoid the
   nonuniform-edge problem.  However the theorem assumes the fixed hierarchy

   \[
   1/D\ll1/A\ll\gamma\ll1/K\le1
   \tag{0.6}
   \]

   and its error is `B^(-1+gamma) log^A D`.  The paper gives no dependence
   `A=A(K), D_0=D_0(K,A,gamma)` from which this error can be proved
   `o(1/K)` along `K=Theta(sqrt r)`.
6. Delcourt--Postle likewise fixes the edge-size bound before the degree
   tends to infinity.  Its exponent `alpha=alpha(K,beta)` and threshold are
   nonuniform, and the power-codegree hypothesis is not stable under
   arbitrary multiplicity blow-up.

Accordingly, none of the audited black boxes proves an `o(W)` residual
matching.  The missing quantitative result is not ordinary pair-codegree
decay; it is a **uniform growing-rank, higher-codegree matching/coloring
theorem** with relative leave

\[
 r^{-1+o(1)}=o(r^{-1/2})=o(1/K)
 \tag{0.7}
\]

for the explicit laminar flag profile below.  Equivalently, a uniform version
of the Gould--Kelly estimate with error `B^{-1+o(1)}` and no uncontrolled
`log^{A(K)}D` factor would close this particular rounding gate.

This audit concerns only the residual matching.  It does not solve the
separate joint collar-extension condition `(5.1)` in the macroscopic-collar
theorem.

## 1. Size and required precision

The retained rank band is

\[
 \mathcal I=\{r-b,\ldots,r-a-1\},\qquad
 a=\lceil c\sqrt r\rceil,
 \quad b=\lceil\sqrt{6r\log r}\rceil,
 \tag{1.1}
\]

where `c > sqrt(log 2)` is fixed.  With

\[
 p_s={{2r\choose s}\over W},
\]

the local central-binomial estimate gives

\[
 \sum_{s\in\mathcal I}p_s=\Theta(\sqrt r).
 \tag{1.2}
\]

Indeed a fixed-width `Theta(sqrt r)` subband beginning at distance
`c sqrt r` already has this mass, while the Gaussian tail gives the matching
upper bound.  Hence the named-target population is `Theta(W sqrt r)` and
adding the `W` owner vertices does not change (0.1).

The cap on a residual flag is `d`, where

\[
 d=\left({\sqrt\pi\over2}+o(1)\right)\sqrt r,
\]

so `K <= d+1=Theta(sqrt r)`.  Therefore a matching theorem with relative
leave `eta_r` gives the needed `o(W)` conclusion only if

\[
 \eta_r=o(W/N)=o(r^{-1/2})=o(1/K).
 \tag{1.3}
\]

This is the scale against which every theorem below must be tested.

## 2. The full flag-codegree profile

The pair estimate in the collar theorem extends uniformly to every supported
set of vertices.

### Lemma 2.1 (all-order normalized codegrees)

After clearing the rational edge weights, let `D` be the owner degree and
let `Delta_j` be the maximum `j`-codegree of the resulting
multihypergraph.  There is an absolute constant `C_0` such that, uniformly
for

\[
 2\le j\le K,
\]

\[
 {\Delta_j\over D}
 \le
 \left({C_0\over r^2}\right)^{j-1}.
 \tag{2.1}
\]

The same estimate holds if one of the `j` vertices is an owner.  The target
and owner degrees are `(1-o(1))D` and `D`, respectively.

At order two the scale is sharp:

\[
 {\Delta_2\over D}=\Theta(r^{-2}).
 \tag{2.2}
\]

#### Proof

Any supported collection of target vertices is a flag

\[
 S_1\subset\cdots\subset S_j
\]

whose ranks `s_1<...<s_j` all have the same parity.  Thus every consecutive
gap is at least two.  Conditional on the largest target and on the selected
ranks, a uniform owner ordering realizes this particular nested flag with
probability

\[
 \prod_{i=1}^{j-1}{1\over {s_{i+1}\choose s_i}}.
 \tag{2.3}
\]

Every retained rank is at least `r-b >= r/2`, and every rank gap is at most
`b=o(r)`.  Hence

\[
 {s_{i+1}\choose s_i}
 ={s_{i+1}\choose s_{i+1}-s_i}
 \ge {r/2\choose2}=\Omega(r^2).
 \tag{2.4}
\]

Before the capacity cap, the joint rank marginal is

\[
 2^{j-1}\prod_{i=1}^j p_{s_i};
\]

the cap only decreases it, and every `p_s<=1`.  Dividing by the
`(1-o(1))` degree of the largest target and combining with (2.3)--(2.4)
proves (2.1) for target-only flags.

If an owner is also prescribed, the largest target has codimension at least
`a+1 >=2` inside that owner.  Prescribing it therefore contributes another
factor

\[
 {1\over {r\choose s_j}}=O(r^{-2}),
\]

and the same argument handles all smaller targets.  Two distinct owners
have codegree zero.  This proves the lemma.  `square`

For sharpness at order two, choose consecutive retained ranks of the same
parity, `s<t=s+2`, at distance `c sqrt r+O(1)` below the middle layer.
Then `p_s,p_t=Theta_c(1)`.  Before the cap their joint rank probability is
`2p_sp_t`; removing the overflow event changes it by at most
`exp(-kappa sqrt r)=o(1)`.  For any fixed flag `S subset U` at these ranks,
the exact uniform-order conditional factor is

\[
 {1\over {t\choose s}}={1\over {t\choose2}}=\Theta(r^{-2}).
\]

Since the degree of `U` is `(1-o(1))D`, this supplies a pair of codegree
`Theta(D/r^2)` and proves (2.2).

The important point is that (2.1) is much stronger than pair-codegree
control.  It is exactly why the higher-codegree theorems have a favorable
*formal* main term.

## 3. Fixed-uniformity Pippenger theory

The classical Pippenger matching theorem says, in one standard formulation,
that for every fixed uniformity `K` and fixed requested error `epsilon`,
there are constants `delta(K,epsilon)` and `D_0(K,epsilon)` such that a
nearly `D`-regular `K`-uniform hypergraph with pair codegree at most
`delta D` has a matching leaving at most `epsilon N` vertices.

Here the requested error itself is

\[
 \epsilon_r=o(1/K),
\]

while `K -> infinity`.  The statement gives no estimate proving

\[
 C_0r^{-2}\le\delta(K,\epsilon_r)
\]

or that the rational blow-up degree exceeds the associated threshold.
The same quantifier issue applies to Pippenger--Spencer edge coloring,
fixed-rank Kahn results, and fixed-rank pseudorandom matching refinements.
Thus `Delta_2/D=o(1)` does not justify a diagonal invocation.

Primary fixed-rank references include:

* N. Pippenger and J. Spencer,
  [*Asymptotic Behavior of the Chromatic Index for Hypergraphs*](https://scholarship.claremont.edu/hmc_fac_pub/1041/),
  JCTA 51 (1989), 24--42;
* N. Alon, J.-H. Kim, and J. Spencer,
  [*Nearly perfect matchings in regular simple hypergraphs*](https://math.nyu.edu/~spencer/papers/alonkimjs.pdf),
  Israel J. Math. 100 (1997), 171--187.

## 4. Alon--Bollobas--Kim--Vu

The relevant growing-uniformity ABKV matching theorem assumes, in
particular,

\[
 e^{2K}C=o(D/\log D),
 \tag{4.1}
\]

where `C` is the maximum pair codegree.  Equivalently,

\[
 e^{2K}{C\over D}\log D=o(1).
 \tag{4.2}
\]

By (2.2), `C/D=Theta(r^-2)`.  This is only polynomially small, whereas
`e^{2K}=e^{Theta(sqrt r)}`.  The left side is therefore at least at the
exponential-versus-polynomial scale

\[
 e^{\Theta(\sqrt r)}r^{-2},
\]

before the additional factor `log D`.  Thus the ABKV hypothesis is not
verified and, at the audited collision scale, fails overwhelmingly.

The source is N. Alon, B. Bollobas, J. H. Kim, and V. H. Vu,
[*Economical covers with geometric applications*](https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf),
Proc. LMS 86 (2003), especially Theorem 3.9 and condition (8).

## 5. Pair-codegree quantitative theorems

Vu's pair-codegree estimate for a fixed `K`-uniform hypergraph has main
factor

\[
 \left({C\over D}\right)^{1/(K-1)}
\]

up to a fixed-`K` polylogarithmic factor.  With `D/C=Theta(r^2)` and
`K=Theta(sqrt r)`, this is

\[
 \exp\left(-{2\log r+O(1)\over K-1}\right)=1-o(1).
 \tag{5.1}
\]

The 2023 theorem of Kang--Kuehn--Methuku--Osthus improves the exponent to

\[
 {1\over K-1}+\eta_K,
 \qquad \eta_K=\Theta(K^{-3}),
\]

but (5.1) remains `1-o(1)`.  Thus even formal substitution leaves
`(1-o(1))N`, far larger than `o(W)`.

In addition, KKMO fixes `K,gamma,mu,eta` before `N,D -> infinity` and
requires

\[
 D\ge\exp((\log N)^\mu),\qquad C\le D^{1-\gamma}.
\]

These hypotheses have not been verified for the rational blow-up with
parameters varying in `r`.

Primary sources:

* V. H. Vu,
  [*New bounds on nearly perfect matchings in hypergraphs: higher codegrees do help*](https://doi.org/10.1002/1098-2418(200008)17:1%3C29::AID-RSA4%3E3.0.CO;2-W),
  RSA 17 (2000), 29--63;
* D. Y. Kang, D. Kuehn, A. Methuku, and D. Osthus,
  [*New bounds on the size of nearly perfect matchings in almost regular hypergraphs*](https://arxiv.org/abs/2010.04183),
  JLMS 108 (2023), Theorem 1.4.

## 6. Vu's higher-codegree theorem: the first formal success

Vu's higher-codegree theorem is stated for a `(k+1)`-uniform,
`D`-regular hypergraph.  Given bounds

\[
 D=D_1\ge D_2\ge\cdots\ge D_s>0,
\]

it assumes

\[
 x^3\le {D_j\over D_{j+1}}\quad(j<s),
 \qquad
 x^{k-s+2}\le {D_{s-1}\over D_s},
 \tag{6.1}
\]

and concludes

\[
 U(H)=\widetilde O_K(N/x).
 \tag{6.2}
\]

Here the tilde hides a power of `log D`, and both its exponent and the
sufficiently-large-degree threshold are allowed to depend on the fixed
uniformity.

The fixed-uniformity quantifier is also explicit in Gould--Kelly's modern
restatement of Vu's theorem: their Theorem 1.2 assumes

\[
 1/D\ll1/A\ll1/k\le1
\]

and writes the leave as `N log^A N/x`.  Thus `A` is selected only after the
uniformity is fixed; it is not an absolute exponent available on a growing
`K` diagonal.

If, for the moment, one ignores the nonuniform atom sizes, Lemma 2.1 permits

\[
 D_j=D\left({C_0\over r^2}\right)^{j-1}.
 \tag{6.3}
\]

Taking `s=K` makes the last condition in (6.1) weaker than the preceding
ones, and the choice

\[
 x=\Theta(r^{2/3})
 \tag{6.4}
\]

satisfies the displayed power conditions.  Equations (0.1) and (6.4) give
the favorable unlogged main term

\[
 {N\over x}=O(Wr^{-1/6})=o(W).
 \tag{6.5}
\]

This calculation is useful: higher codegrees really remove the pair-only
exponent obstruction.

It is not, however, a theorem application.  There are two exact gaps.

1. The parity atoms have sizes between one and `K`; Vu's theorem is uniform.
   Padding by global dummy vertices creates large codegrees, while padding
   by private vertices destroys regularity.  No lossless regular
   uniformization is currently supplied.
2. More decisively, (6.2) is a fixed-`K` estimate.  It does not give a
   uniform bound of the form

   \[
   U(H)\le N r^{-2/3+o(1)}
   \]

   when `K=Theta(sqrt r)`.  The notation `widetilde O_K` permits both an
   uncontrolled `K`-dependent constant and an uncontrolled power
   `log^{c_K}D`.  Therefore (6.5) is only a formal main-term calculation.

The precise primary statement is Vu's Theorem 1.2.2 in the paper cited in
Section 5.

## 7. Gould--Kelly: closest current theorem, still nonuniform

Gould and Kelly's full-codegree nibble theorem gives, for fixed edge size
`K=k+1`, a matching with relative leave

\[
 B^{-1+\gamma}\log^A D,
 \tag{7.1}
\]

under the hierarchy

\[
 1/D\ll1/A\ll\gamma\ll1/k\le1,
 \tag{7.2}
\]

where

\[
 B\le
 \min\left\{
 \sqrt{D/D_2},
 \min_{4\le j\le K}(D/D_j)^{1/(j-1)},
 1/\epsilon
 \right\}.
 \tag{7.3}
\]

Their edge-coloring theorem for `(k+1)`-bounded hypergraphs has the same
error and adds the harmless formal bottleneck `D^(1/K)`.  This bounded form
is the correct one for the variable-size parity atoms.  Since a coloring
partitions the edges into matchings, near regularity implies that one color
class leaves at most the coloring error times `N` vertices.

Lemma 2.1 gives

\[
 \sqrt{D/D_2}=\Theta(r),
 \qquad
 (D/D_j)^{1/(j-1)}=\Omega(r^2).
 \tag{7.4}
\]

The degree spread from the capacity cap is exponentially small in
`sqrt r`, so it is not the formal bottleneck.  If the multiplicity scale is
also chosen so that `D^(1/K)>=Theta(r)`, then (7.3) permits

\[
 B=\Theta(r).
 \tag{7.5}
\]

Omitting the error factor in (7.1), this would leave

\[
 {N\over B}=O(Wr^{-1/2})=o(W).
 \tag{7.6}
\]

Again, (7.6) is not a valid diagonal invocation.  In (7.2), `k` is fixed
first.  As `K -> infinity`, one must send `gamma ->0` and then choose
`A=A(K,gamma) -> infinity`; the theorem gives no uniform rate.  It therefore
does not establish

\[
 B^{-1+\gamma}\log^A D=o(1/K).
 \tag{7.7}
\]

Increasing a rational blow-up multiplicity does not resolve this: it helps
the `D^(1/K)` bottleneck but worsens the logarithmic factor, and the theorem
provides no admissible quantitative window balancing the two.

The primary source is S. Gould and T. Kelly,
[*Advancing the Rodl Nibble: New bounds on matchings and the list chromatic index of hypergraphs*](https://arxiv.org/abs/2511.11375),
Theorems 1.4 and 1.7.

## 8. Delcourt--Postle and conflict-free coloring

With an empty conflict system, Delcourt--Postle's Corollary 1.17 is an
edge-coloring theorem for an `R`-bounded hypergraph of maximum degree `D`
and codegree at most `D^(1-beta)`.  It gives at most

\[
 D(1+D^{-\alpha})
\]

colors for some `alpha=alpha(R,beta)>0`, after a threshold
`D_0(R,beta)`.  Averaging incidence mass over the colors would give a
matching with relative leave `O(D^-alpha)` in a near-regular hypergraph.

This does not yield the required diagonal.

* The theorem fixes `R` and `beta` before `D -> infinity`; neither
  `alpha(R,beta)` nor `D_0(R,beta)` is uniform for
  `R=K=Theta(sqrt r)`.
* For a multiplicity blow-up with `C/D=Theta(r^-2)`, the condition

  \[
  C\le D^{1-\beta}
  \]

  is equivalent to `D^beta=O(r^2)`.  Thus arbitrarily increasing the
  multiplicity to pass the degree threshold eventually destroys the
  power-codegree hypothesis.
* No published dependence proves simultaneously the threshold, the
  power-codegree condition, and

  \[
  D^{-\alpha}=o(1/K).
  \]

The conflict configuration machinery does not improve this when the
conflict hypergraph is empty.  Its extra hypotheses can only add
requirements.

The primary source is M. Delcourt and L. Postle,
[*Finding an almost perfect matching in a hypergraph avoiding forbidden submatchings*](https://arxiv.org/abs/2204.08981),
Corollaries 1.17--1.18.

## 9. Exact missing quantitative estimate

The macroscopic collar has crossed the genuine combinatorial collision
threshold:

\[
 K^2\Delta_2/D=O(r^{-1})=o(1),
\]

and in fact has the geometric all-codegree profile (2.1).  The remaining
black-box gap can be stated cleanly.

> **Uniform laminar-flag matching estimate.**  Let `K=Theta(sqrt r)` and
> let `H_r` be a `K`-bounded, `(1+o(1))D`-regular multihypergraph on
> `N=Theta(WK)` vertices satisfying
> \[
> \Delta_j(H_r)/D\le(C_0/r^2)^{j-1}
> \quad(2\le j\le K).
> \]
> Prove that `H_r` has a matching leaving
> \[
> N r^{-1+o(1)}=o(W)
> \]
> vertices.

A theorem with the weaker Vu-scale conclusion

\[
 N r^{-2/3+o(1)}=o(W)
\]

would already suffice.  What is unavailable is a uniform error estimate;
the time-zero codegrees themselves are no longer the obstruction.

Even such a theorem would settle only the residual rounding step.  The
residual atom assigned to an owner must still lie below that owner's collar
bottom and fit its remaining capacity.  That joint collar-extension theorem
remains separate.

## 10. Scope

This note proves no impossibility theorem for a tailored nibble or Boolean
absorber.  It proves only that the located published black boxes do not, as
stated, supply the needed diagonal conclusion.  In particular:

* the formal Vu and Gould--Kelly powers are favorable and should be retained;
* their fixed-uniformity error terms may not be silently treated as uniform;
* pair-codegree control alone remains insufficient;
* a flag-specific regeneration/absorption argument could still exploit the
  exact nested geometry and avoid the generic logarithmic losses.
