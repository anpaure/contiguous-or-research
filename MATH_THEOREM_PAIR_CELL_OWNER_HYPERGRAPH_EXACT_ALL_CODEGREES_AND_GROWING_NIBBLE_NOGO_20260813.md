# Pair-cell owner hypergraph: exact all-family codegrees and a growing-nibble no-go

**Date:** 2026-08-13  
**Method:** exact incidence counting, followed by direct substitution into the
published matching parameters.  Small cases and the arbitrary-family formula were
replayed by exact enumeration on `h100`.  
**Status:** unconditional theorem and black-box no-go.  The note does **not** prove
that a matching with the optimal residue leave is impossible.  It proves that whole
good pair cells, at dimension `M` or in a narrow good stratum, are the wrong atoms for
the presently available nibble and Delcourt--Postle theorems.

## 0. Outcome

Put

\[
 k=2p+1,\qquad R=p+1,\qquad
 \mathcal O={ [k]\choose R},\qquad W=|\mathcal O|.       \tag{0.1}
\]

For a fixed dimension `1<=m<=p`, let a hyperedge be the `2^m` owners in one
occurrence-labelled sentinel-plus-pair cell of dimension `m`.  Parallel occurrences
with the same owner set carry no matching power.  After quotienting them, the simple
owner hypergraph is exactly the orbit of physical pair packets

\[
 E(F,G,\mathcal P)=
 \{F\cup X:X\text{ chooses one endpoint of every pair of }\mathcal P\}, \tag{0.2}
\]

where `|F|=p+1-m`, `|G|=p-m`, and `\mathcal P` is a perfect matching of the
remaining `2m` labels.  It is `r=2^m` uniform and exactly regular of degree

\[
 \boxed{d_m={p+1\choose m}{p\choose m}m!.}               \tag{0.3}
\]

If two owners have Johnson distance `j`, their exact codegree is

\[
 \boxed{
 \lambda_{m,j}=j!(m-j)!
 {p+1-j\choose m-j}{p-j\choose m-j}}
 \quad(0\le j\le m),                                    \tag{0.4}
\]

and it is zero for `j>m`.  Consequently

\[
 {\lambda_{m,j}\over d_m}
 ={j!(m)_{\underline j}\over
   (p+1)_{\underline j}(p)_{\underline j}},\qquad
 \boxed{{\Delta _2\over d_m}={m\over p(p+1)}.}          \tag{0.5}
\]

There is also an exact formula for the codegree of **every** family of owners,
in terms of its binary coordinate-profile multiplicities; see Theorem 3.1.

These attractive pair codegrees do not support a whole-cell nibble.  At the OR-word
scale

\[
 m=M=q+\lceil3\log _2p\rceil=\Theta(\sqrt p),\qquad r=2^m, \tag{0.6}
\]

the pair-codegree bottleneck alone is only

\[
 \sqrt{d_m/\Delta _2}=\sqrt{p(p+1)/m}=p^{3/4+o(1)},       \tag{0.7}
\]

whereas reducing a leave from `W=exp(Theta(p))` to `<2^M=exp(o(p))`
requires an exponential reduction factor.  More decisively, a full physical cell has
codegree one.  Thus the Gould--Kelly full-codegree parameter satisfies

\[
 B\le d_m^{1/(2^m-1)}
 =\exp\!\left\{ {m\log(p^2/m)+O(m)\over2^m}\right\}
 =1+o(1).                                                \tag{0.8}
\]

The strongest current full-codegree nibble bound is therefore vacuous here.  The
Delcourt--Postle power gap is at best

\[
 \beta_*={\log(d_m/\Delta _2)\over\log d_m}
 ={1+o(1)\over m}=o(1),                                  \tag{0.9}
\]

while its host uniformity `2^m` grows and its only admissible power parameter shrinks
with `p`.
Adding transition or palette decorations does not repair either obstruction.

## 1. The physical quotient and exact occurrence multiplicity

An occurrence-labelled pair cell first chooses a sentinel `z`, pairs the remaining
`2p` labels, and gives each pair status singleton, double, or empty.  Fix the singleton
count `m`.  There is a unique `epsilon in {0,1}` satisfying

\[
 \epsilon\equiv p+1-m\pmod2.                              \tag{1.1}
\]

Here `epsilon` is the common membership of the sentinel in the cell.  Put

\[
 a={p+1-\epsilon-m\over2},\qquad
 b={p-1+\epsilon-m\over2}.                                \tag{1.2}
\]

Every such occurrence has the physical owner set (0.2): `F` consists of the sentinel
when `epsilon=1` and all coordinates in double pairs, `G` consists of the sentinel
when `epsilon=0` and all coordinates in empty pairs, and `\mathcal P` is the set of
singleton pairs.

### Proposition 1.1 (constant quotient multiplicity)

Every physical dimension-`m` packet has exactly

\[
 \boxed{
 \kappa_m={ (p+1-m)!(p-m)!\over
             2^{p-m}a!b!}}                              \tag{1.3}
\]

occurrence-labelled sentinel representations.  Hence occurrence labelling multiplies
every nonzero family codegree, including the degree, by the same `kappa_m`.

#### Proof

If `epsilon=1`, choose the sentinel from the `p+1-m` common-full coordinates, then
perfectly pair the remaining common-full coordinates into double pairs and the
common-empty coordinates into empty pairs.  If `epsilon=0`, choose the sentinel from
the `p-m` common-empty coordinates and make the analogous two perfect matchings.
Using `(2s-1)!!=(2s)!/(2^s s!)` gives (1.3) in both parities.  The active matching
`\mathcal P` is already determined by the physical packet.  \(\square\)

In particular the exact occurrence-labelled owner degree is

\[
 \boxed{
 D_m=\kappa_md_m
 ={(p+1)p!^2\over m!2^{p-m}a!b!}.}                       \tag{1.4}
\]

The number of distinct physical cells is

\[
 |\mathcal E_m|
 ={(2p+1)!\over(p+1-m)!(p-m)!2^m m!}
 ={Wd_m\over2^m}.                                        \tag{1.5}
\]

Parallel copies do not change which matchings exist.  Proposition 1.1 also prevents
an invalid gain from feeding occurrence multiplicity to a multihypergraph theorem:
the terminal codegree is multiplied by exactly the same factor.

## 2. Exact degree and pair codegrees

### Theorem 2.1

The simple physical packet hypergraph has degree (0.3), pair codegrees (0.4), and
maximum relative pair codegree (0.5).

#### Proof

Fix an owner `T`.  Choose the `m` active endpoints in `T`, choose the `m` opposite
active endpoints outside `T`, and biject them.  The unchosen points are the forced
full and empty cores.  This gives

\[
 {p+1\choose m}{p\choose m}m!=d_m.                       \tag{2.1}
\]

Now fix owners `T,U` at Johnson distance `j`.  Every point of `T-U` must be actively
paired with a point of `U-T`, in `j!` ways.  Choose the remaining `m-j` commonly
selected active endpoints from `T\cap U`, the remaining `m-j` commonly unselected
endpoints outside `T\cup U`, and biject them.  This is exactly (0.4).  Division by
(0.3) proves the first part of (0.5).

For `1<=j<=m`, divide that ratio by its value at `j=1`:

\[
 {\lambda_{m,j}/d_m\over m/[p(p+1)]}
 ={j!(m-1)_{\underline{j-1}}\over
   (p)_{\underline{j-1}}(p-1)_{\underline{j-1}}}
 \le {j!\over(p)_{\underline{j-1}}}
 ={j\over {p\choose j-1}}\le1.                          \tag{2.2}
\]

The last inequality holds for `1<=j<=p`; equality can also occur at the opposite
endpoint when `m=p`.  Thus the maximum is `m/[p(p+1)]`.  \(\square\)

There is useful aggregate spread despite the maximum-codegree obstruction.  Inside a
fixed packet there are `2^(m-1) binom(m,j)` unordered owner pairs at distance `j`.
Therefore

\[
 \sum_{\{T,U\}\subset E}\lambda_{m,d_J(T,U)}
 ={2^m d_m\over2}
 \sum_{j=1}^m{(m)_{\underline j}^2\over
                   (p+1)_{\underline j}(p)_{\underline j}}. \tag{2.3}
\]

For `m=o(p)`, the sum on the right is `O(m^2/p^2)`.  Bonferroni consequently gives
the conflict-neighbourhood estimate

\[
 |\Gamma(E)|=2^m d_m\bigl(1-O(m^2/p^2)-O(1/d_m)\bigr).   \tag{2.4}
\]

Thus the failure below is not a hidden projective-plane concentration at the pair
level.  It is caused by making one exponentially large cube into one matching atom.

For comparison, independently sample every physical cell with probability
`theta/(2^m d_m)` and retain it only when no intersecting cell was sampled.  Equations
(1.5) and (2.4) give an expected covered-owner fraction

\[
 {\theta e^{-\theta}+o(1)\over2^m}.                       \tag{2.5}
\]

Thus even the optimally scaled safe isolated bite covers only one `2^m`-th of the
layer.  This is not by itself an impossibility theorem for a correlated multiround
process, but it agrees with the terminal-codegree barrier below.

## 3. Exact arbitrary-family codegrees

Let `\mathcal A={T_1,...,T_t}` be distinct owners.  For every binary column
`\sigma in {0,1}^t`, put

\[
 n_\sigma=|\{x\in[k]:(1_{x\in T_i})_{i=1}^t=\sigma\}|.   \tag{3.1}
\]

Choose one representative from every complementary pair
`{\sigma,\bar\sigma}` other than `{0^t,1^t}`, and call the representative set
`mathcal R`.  Put

\[
 u=\sum_{\sigma\in\mathcal R}n_\sigma,\qquad x=m-u.       \tag{3.2}
\]

### Theorem 3.1 (profile formula)

If

\[
 n_\sigma=n_{\bar\sigma}\quad(\sigma\in\mathcal R),
 \qquad0\le x\le\min(n_{1^t},n_{0^t}),                   \tag{3.3}
\]

then the physical dimension-`m` codegree of `\mathcal A` is

\[
 \boxed{
 \Lambda_m(\mathcal A)=
 \left(\prod_{\sigma\in\mathcal R}n_\sigma!\right)
 {n_{1^t}\choose x}{n_{0^t}\choose x}x!.}               \tag{3.4}
\]

If (3.3) fails, the codegree is zero.  The occurrence-labelled codegree is
`\kappa_m\Lambda_m(\mathcal A)`.

#### Proof

In a common packet, a coordinate with nonconstant profile `\sigma` can only be paired
with a coordinate of complementary profile: every owner must choose exactly one
endpoint.  Thus the two multiplicities must agree, and their bijection contributes
`n_\sigma!`.  These forced pairs use `u` active directions.

Every remaining active pair must join one all-one coordinate to one all-zero
coordinate.  Choose and biject `x=m-u` such pairs, giving the last three factors of
(3.4).  All remaining all-one and all-zero coordinates become the full and empty
cores.  Conversely every choice just described is a packet containing every owner in
`\mathcal A`.  \(\square\)

For example, if `\mathcal A` is the complete vertex set of an `s`-face generated by
`s` specified disjoint swaps, then

\[
 \Lambda_m(\mathcal A)
 ={p+1-s\choose m-s}{p-s\choose m-s}(m-s)!
 ={\lambda_{m,s}\over s!}.                              \tag{3.5}
\]

In particular a complete dimension-`m` physical packet has codegree exactly one:

\[
 \boxed{\Delta_{2^m}=1}                                  \tag{3.6}
\]

in the simple quotient, and exactly `kappa_m` in the occurrence multihypergraph.

## 4. The full-codegree parameter collapses

For `m=o(p)`, Stirling's formula in (0.3) gives

\[
 \log d_m=m\log(p^2/m)+O(m+m^2/p+\log p).                \tag{4.1}
\]

The parameter in
[Gould--Kelly, *Advancing the Rodl Nibble*](https://arxiv.org/abs/2511.11375)
(Theorem 1.4),
must obey

\[
 B\le\min\left\{
 \sqrt{d_m/\Delta_2},
 \min_{4\le t\le2^m}(d_m/\Delta_t)^{1/(t-1)}
 \right\}.                                               \tag{4.2}
\]

The pair row gives (0.7).  The terminal row (3.6) gives (0.8), and hence

\[
 \boxed{B=1+o(1)}                                        \tag{4.3}
\]

at `m=M=Theta(sqrt p)`.  In the occurrence multihypergraph the same calculation is

\[
 \left({D_m\over\Delta_{2^m}^{\rm occ}}\right)^{1/(2^m-1)}
 =\left({\kappa_md_m\over\kappa_m}\right)^{1/(2^m-1)},  \tag{4.4}
\]

so indexing cannot change the answer.

The published conclusion is a leave at most
`W B^(-1+gamma) log^A d_m`, under the fixed-parameter hierarchy
`1/d_m << 1/A << gamma << 1/(2^m-1)`.  Equation (4.3) makes the formal bound
larger than `W`; independently, the hierarchy does not provide a theorem uniform in
the growing rank.  Thus this is an exact quantitative no-go, not merely a missing
quantifier citation.

Even deleting the terminal bottleneck by fiat would not approach the required scale.
Indeed (0.7) would give only a polynomial reduction, while

\[
 {W\over2^M}=\exp\{2p\log2-o(p)\}.                       \tag{4.5}
\]

Any `W/B^(1-o(1))` conclusion needs `B=exp(Theta(p))` to leave fewer than
`2^M` owners.

The finite scales already show the separation.  Exact logarithms evaluated on `h100`
give

\[
\begin{array}{c|c|c|c|c}
p&q&M&\sqrt{p(p+1)/M}&\log(d_M^{1/(2^M-1)})\\ \hline
100&10&30&18.35&1.79\cdot10^{-7}\\
150&12&34&25.81&1.42\cdot10^{-8}\\
200&14&37&32.96&2.08\cdot10^{-9}\\
280&16&41&43.81&1.56\cdot10^{-10}.
\end{array}                                               \tag{4.6}
\]

The last column is `log B`, not `B-1`; they are asymptotic at this scale.

## 5. Delcourt--Postle and other nibble black boxes

### 5.1 Delcourt--Postle

In the simple quotient the largest possible fixed power saving in
`Delta_2<=d_m^(1-beta)` is

\[
 \beta_*={\log(p(p+1)/m)\over\log d_m}={1+o(1)\over m}.  \tag{5.1}
\]

[Delcourt--Postle's matching and conflict-free results](https://arxiv.org/abs/2204.08981)
fix the host uniformity and a
positive `beta` before taking the degree threshold.  Here the host uniformity is
`2^m=2^{Theta(sqrt p)}` and `beta_*=o(1)`.  Their quantifiers therefore do not apply.
Using occurrence labels only increases `log D_m` while preserving the relative pair
codegree, so it makes the displayed power exponent smaller.

### 5.2 Genuinely growing-uniformity estimates

The
[Alon--Bollobas--Kim--Vu growing-rank condition](https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf)
includes

\[
 e^{2r}\Delta_2=o(d_m/\log d_m).                         \tag{5.2}
\]

Here `r=2^m` and `Delta_2/d_m=m/[p(p+1)]`, so the left-to-right ratio is

\[
 e^{2^{m+1}}{m\log d_m\over p(p+1)}\longrightarrow\infty. \tag{5.3}
\]

Its error term with exponent `1/(r-1)` is likewise asymptotic to the full vertex
scale.  Classical Pippenger--Frankl--Rodl, Ehard--Glock--Joos, Vu, and the usual
conflict-free nibble theorems fix the uniformity and also yield no uniform
subexponential absolute leave here.

### 5.3 Narrow good strata

Taking dimensions in a narrow interval `I=[M,M+w]` does not alter the conclusion.
All edge sizes remain divisible by `2^M`.  In the simple quotient the total owner
degree is `d_I=sum_(m in I)d_m`, and, for `m_+=M+w=o(p)`,

\[
 \log d_I=O(m_+\log p+\log|I|).                          \tag{5.4}
\]

A largest physical cell is still a simple edge of size `2^(m_+)`, so every analogous
full-codegree parameter is bounded by

\[
 d_I^{1/(2^{m_+}-1)}=1+o(1)                              \tag{5.5}
\]

for every genuinely narrow stratum.  Standard uniform matching theorems do not apply
directly to the mixed edge sizes in any case.

## 6. What transition and palette constraints can encode

There are two distinct issues.

1. **Hereditary collision constraints can be encoded.**  Once a Hamilton cycle and
   local schedule are attached to a cell occurrence, reusing a named lower palette
   value can be forbidden by a size-two configuration, or by adjoining the palette
   name as a resource vertex.  The same applies to a fixed list of genuinely pairwise
   forbidden decorations.

2. **The required global conditions are not forbidden-submatching properties.**
   Exact palette coverage, existence of a spanning compatible splice order, and the
   coordinate-cap hitting conditions are positive and/or order-dependent.  Avoiding
   a configuration hypergraph is hereditary under deleting selected cells; exact
   coverage and connectedness are not.  In particular, two components need compatible
   transition collars only when they are made adjacent.  Declaring every pair with
   incompatible collars forbidden would incorrectly demand all-to-all compatibility,
   while an unordered matching does not choose the needed splice order.

Resource augmentation also worsens the base parameter.  One cell cycle has `2^m`
immediate-lower occurrences and `2^m` immediate-upper occurrences.  Encoding just
owners plus both immediate palettes makes the host rank at least `3*2^m`; encoding
the complete depth-`q-1` fan makes it `Theta(q2^m)`.  In any symmetric catalogue of
cycle/schedule decorations, every physical cell receives the same number of
decorations.  Therefore an owner pair receives that same multiplier on every common
physical cell, and the relative owner-pair codegree remains exactly (0.5).  The
pair bottleneck (0.7) survives while the host rank becomes still larger.  Whether the
decorations are retained as parallel labels or distinguished by added resources can
change the terminal full-edge codegree, but it cannot remove this unchanged polynomial
pair bottleneck.  Collision avoidance would still not force coverage of every palette
shore.

Thus Delcourt--Postle cannot first choose the whole-cell matching and simultaneously
solve the transition, exact-palette, fusion, and cap gates.  Those constraints require
a separate flow/connector/absorber layer or a different, much smaller matching atom.

## 7. Divisibility and the exact surviving target

Every dimension at least `M` has size divisible by `2^M`.  Hence every matching of
whole good cells has owner leave `L` satisfying

\[
 L\equiv W\pmod {2^M}.                                   \tag{7.1}
\]

Legendre's formula gives

\[
 v_2(W)=s_2(p+1)-1<M,                                    \tag{7.2}
\]

so the residue is nonzero.  A leave below `2^M`, if it exists, is forced to be the
single value `W mod 2^M`.  None of the audited nibbles comes remotely close to this
exact residue scale.

The no-go does not rule out such a matching.  It identifies the remaining viable
choices:

* construct a deterministic correlated whole-cell packing together with an absorber
  that attains the exact residue; or
* cut the long-run cube cycles into much smaller resident paths, pay and later absorb
  their `q`-collars, and run any matching argument on those smaller atoms.

The second option removes both the `2^M` divisibility and the terminal
`2^m`-codegree root, at the price of a genuine collar-splicing theorem.

## 8. Exact H100 replay

An independent enumerator on `h100` generated every physical packet for

\[
 (p,m)=(3,1),(3,2),(3,3),(4,2),(4,3).                    \tag{8.1}
\]

It verified simplicity, (0.3), and every pair codegree at every Johnson distance.
For example it returned

\[
\begin{array}{c|c|c|c}
(p,m)&W&d_m&(\lambda_{m,1},\lambda_{m,2},\lambda_{m,3})\\ \hline
(3,2)&35&36&(6,2,0)\\
(3,3)&35&24&(6,4,6)\\
(4,2)&126&120&(12,2,0)\\
(4,3)&126&240&(36,12,6).
\end{array}                                               \tag{8.2}
\]

A second replay checked (3.4) against direct containment counts for 12,000 random
families of sizes one through six at `(p,m)=(4,3)`, and verified full-edge codegree
one.  These computations are checks only; the proofs above are exact and independent
of them.

## 9. Final verdict

\[
 \boxed{\text{Excellent pair spread does not overcome the exponential-rank
 full-codegree bottleneck.}}
\]

No current growing-uniformity nibble or Delcourt--Postle theorem yields even a useful
owner leave for this hypergraph, let alone `<2^M` or `exp(o(p))`; the transition and
palette requirements cannot be added as bounded forbidden configurations to change
that verdict.  The pair-cell route must use deterministic absorption or cut cells into
smaller resident atoms before matching.
