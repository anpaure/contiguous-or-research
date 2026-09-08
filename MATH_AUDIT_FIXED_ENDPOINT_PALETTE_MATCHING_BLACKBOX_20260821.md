# Black-box matching audit for the fixed-endpoint block palette

**Date:** 2026-08-21  
**Status:** rigorous negative applicability audit.  This note does not rule out
an integral near-factor in the tail-MTF palette.  It proves that none of the
standard nibble, conflict-free, rainbow, independent-transversal, or generic
absorption theorems supplies it, even after the exact fractional matching in
`MATH_CANDIDATE_FIXED_ENDPOINT_PALETTE_FRACTIONAL_MATCHING_20260821.md`.

## 1. The scale that a rounding theorem must attain

Put

\[
 n=2m+1,\qquad W={n\choose m},\qquad
 H=\lceil\sqrt{n\log n}\rceil,\qquad q=2H+2,
\]

and take equal free-core length

\[
 a=\lfloor e^{n/5}\rfloor,\qquad s=(1+o(1))W/a.
\]

After omitting the negligible remainder slot (or using the proved slot-type
normalization), a palette edge has

\[
 r=1+qa                                                   \tag{1.1}
\]

vertices: one slot and `a` claimed resources in each of the `q` rank parts.
The exact fractional law is finite and rational.  Clearing a common
denominator therefore produces a multihypergraph in which every relevant
vertex has common degree `D` (or `(1-o(1))D` at the two middle ranks in the
budget-normalized version).  Clearing denominators does not change any
normalized codegree.

Let

\[
 T=\sum_{k=m-H}^{m+1+H}{n\choose k}
\]

be the number of real target resources.  Hoeffding's inequality and central
Stirling give

\[
 T=2^n-o(W)
   =\left(\sqrt{\frac{\pi n}{2}}+o(\sqrt n)\right)W.       \tag{1.2}
\]

Thus the desired `o(W)` real leave is a relative leave `o(n^{-1/2})` on the
real-resource weight.  Merely obtaining an `o(1)` fraction of all augmented
vertices is not enough.

There is an exact structural pair bottleneck.  If
`S in binom([n],m)`, `T in binom([n],m+1)`, and `S subset T`, then the two
same-time/one-step incidences in a band-simple core give

\[
 \frac{\operatorname{codeg}(S,T)}D
 =\frac{2-o(1)}{n-m}
 =\frac{4+o(1)}n.                                       \tag{1.3}
\]

For comparison, two distinct targets in one fixed central rank have maximum
normalized codegree

\[
 \frac{2+o(1)}{m(n-m)}=\frac{8+o(1)}{n^2}.              \tag{1.4}
\]

The dummy decoration is genuine entropy, not artificial parallel
multiplicity.  If `Z_i` is the number of balanced decorations of one good
path in a typical slot, then

\[
 \log Z_i=(1-o(1))qa\log(W/a),\qquad
 \frac{\log D}{r}=(\log2-1/5)n+o(n).                   \tag{1.5}
\]

On the other hand an entire resource edge has multiplicity at most the
number of underlying good path labels, so

\[
 \frac{C_r}{D}\le
 \exp\{-(1-o(1))r\log(W/a)\}.                          \tag{1.6}
\]

Thus terminal/full-edge codegrees are exceptionally good.  The failure
below really is caused by the adjacent-rank pair (1.3), not by a fake degree
created through repeated copies.

Equation (1.3), rather than the same-rank value (1.4), is the decisive generic
nibble bottleneck.  It comes from a useful nested flag, not from a physical
collision, but ordinary matching theorems necessarily count it as a
codegree.

## 2. Pippenger, Pippenger--Spencer, and Kahn

Pippenger's theorem has the quantifier order

\[
 \text{fix }r,\varepsilon;\quad
 \text{then choose }\mu(r,\varepsilon)>0,
\]

and assumes an `r`-uniform almost-regular hypergraph with pair codegree at
most `mu D`.  Pippenger--Spencer and Kahn's list-edge-colouring theorem have
the same fixed-rank quantifier.  Here

\[
 r=1+qa\longrightarrow\infty,
 \qquad \varepsilon=o(n^{-1/2})\longrightarrow0.
\]

Consequently none of these statements can be diagonalized from (1.3).

Ehard--Glock--Joos, *Pseudorandom hypergraph matchings*, Theorem 1.2, is
quantitative but still fixes `r` and `delta`; it puts

\[
 \epsilon=\frac{\delta}{50r^2},\qquad
 C_2\le D^{1-\delta},
\]

and returns relative error `D^{-epsilon}`.  There is a scale-independent
reason this cannot help here.  From (1.3), its power-codegree hypothesis
would force

\[
 D^\delta\le(1+o(1))n/4.
\]

Therefore

\[
 D^{-\epsilon}
 \ge \exp\!\left\{-\frac{\log n+O(1)}{50r^2}\right\}
 =1-o(1).                                                \tag{2.1}
\]

Even a hypothetical growing-`r` reading of its displayed estimate would be
vacuous.  The actual theorem fixes `r` in addition.

## 3. The genuinely growing-uniformity theorem

Alon--Bollobas--Kim--Vu, *Economical covers with geometric applications*,
Theorem 3.9/Corollary 1.5, assumes for an `r`-uniform `D`-regular
hypergraph of maximum pair codegree `C` that

\[
 e^{2r}C=o(D/\log D).                                   \tag{3.1}
\]

In the palette, (1.3) makes the left-to-right ratio at least

\[
 e^{2r}\frac{C}{D}\log D
 \ge e^{2qa}\frac{4+o(1)}n\log D\longrightarrow\infty. \tag{3.2}
\]

Thus the principal published theorem that genuinely permits growing
uniformity fails exponentially, not marginally.

## 4. Higher-codegree nibbles

Vu's higher-codegree theorem, in the modern statement reproduced as
Theorem 1.2 of Gould--Kelly, fixes the edge size and assumes a parameter `x`
with, in particular,

\[
 x^2\le D_1/D_2.                                       \tag{4.1}
\]

It leaves at most `N log^A N/x` vertices.  Equation (1.3) forces

\[
 x\le(1/2+o(1))\sqrt n.                                \tag{4.2}
\]

Even after deleting the polylogarithmic loss and pretending the theorem were
uniform in the growing edge size, its real-target leave scale is

\[
 T/x=\Theta(W),                                        \tag{4.3}
\]

not `o(W)`.  The favorable `Theta(n^{-2})` same-rank codegrees cannot be used
because the adjacent-rank ratio (1.3) is the first ratio in (4.1).

Kang--Kuehn--Methuku--Osthus (2023) is still weaker at this edge size.  Its
pair-codegree conclusion has relative factor

\[
 (D/D_2)^{-1/(r-1)-\eta_r},
 \qquad \eta_r=O(r^{-3}),
\]

which here equals `n^{-1/(r-1)-O(r^{-3})}=1-o(1)`; its hypotheses also fix
the uniformity.

The closest current result is Gould--Kelly, *Advancing the Rodl Nibble*,
Theorem 1.4.  It assumes

\[
 1/D\ll1/A\ll\gamma\ll1/(r-1)
\]

and permits

\[
 B\le\min\left\{
 \sqrt{D/D_2},
 \min_{4\le j\le r}(D/D_j)^{1/(j-1)},
 1/\varepsilon
 \right\}.                                             \tag{4.4}
\]

It then leaves at most `N B^{-1+gamma} log^A D` vertices.  By (1.3),

\[
 B\le(1/2+o(1))\sqrt n.                                \tag{4.5}
\]

Its weighted conclusion is especially decisive.  For the indicator weight
of all real targets, its stated upper guarantee has main scale `T/B`; by
(1.2) and (4.5),

\[
 T/B=\Omega(W).                                        \tag{4.6}
\]

Thus even the unlogged formal upper guarantee is exactly one factor short
and does not imply `o(W)`.  The
actual theorem additionally fixes `r` and has uncontrolled
`log^{A(r)}D` loss.  No estimate in this nibble family proves `o(W)`.

## 5. Delcourt--Postle and conflict-free matching

Delcourt--Postle's bipartite `A`-perfect matching theorem fixes integers
`r` and a real `beta>0`, then chooses `alpha>0,D_0`; it assumes an
`r`-bounded bipartite multihypergraph `(A,B)` with

\[
 \Delta_2\le D^{1-\beta},\qquad
 d(x)\ge(1+D^{-\alpha})D\ (x\in A),\qquad
 d(y)\le D\ (y\in B).                                 \tag{5.1}
\]

The exact-capacity palette has no `A`-side degree surplus, and both `r` and
the needed accuracy vary.  Deleting `o(s)` slots can manufacture a vanishing
surplus, but does not repair the fixed-`r`, fixed-`beta` quantifiers or the
adjacent-pair bottleneck.  Hence (5.1) is not verified.

The conflict-free theorems of Glock--Joos--Kim--Kuehn--Lichev and of
Delcourt--Postle fix both the host rank and the maximum conflict size.  In a
standard simplified form they require

\[
 \Delta_2(\mathcal H)\le D^{1-\epsilon},\qquad
 \Delta(\mathcal C^{(j)})\le \ell D^{j-1},             \tag{5.2}
\]

with additional power-saving conflict codegrees.  Applying them directly to
the resource hypergraph runs into Sections 2--4.

Re-encoding resource intersections as size-two conflicts does not evade the
problem.  Make the base objects the candidates, partitioned by block slot,
and declare two candidates conflicting when they claim a common resource.
Fix one candidate `e` and choose
`t=floor(n^2/16)` of its distinct middle-rank targets.  If `E_x` is the
multiset of candidates claiming `x`, then (1.4) and Bonferroni give

\[
 \left|\bigcup_{x\in X}E_x\right|
 \ge tD-{t\choose2}\frac{(8+o(1))D}{n^2}
 =\Omega(n^2D).                                        \tag{5.3}
\]

Removing the at most `D` alternatives in `e`'s own slot still leaves
`Omega(n^2D)` conflicting candidates.  But (5.2) with conflicts of size two
allows only `2D`.  Thus the conflict-degree hypothesis fails polynomially.

The same calculation rules out graph independent-transversal black boxes:
each candidate part has size `D`, while the conflict graph has maximum degree
at least `Omega(n^2D)`.  Haxell's `|part|>=2Delta` condition, and its locally
sparse refinements with part size `(1+epsilon)Delta`, are far outside their
range.

## 6. Rainbow and topological Hall theorems

Regard the slot palettes as colors on the `qa`-uniform resource hypergraph.
There are `s=(1+o(1))W/a` colors and `(1+o(1))qW` resource vertices.

The Aharoni--Haxell Hall condition for an `r`-uniform bipartite hypergraph
requires, for every slot set `I`, a transversal larger than
`(2r-3)(|I|-1)`.  For all slots, its right side is

\[
 (2qa+O(1))(s-1)=(2-o(1))qW,                           \tag{6.1}
\]

whereas every resource-edge family has a transversal of size at most the
whole resource universe, `(1+o(1))qW`.  Thus the sufficient condition is
capacity-impossible by a factor approaching two.

The stronger Aharoni--Berger--Meshulam topological criterion says that

\[
 \nu^*\!\left(\bigcup_{i\in I}\mathcal P_i\right)
   >qa(|I|-1)                                           \tag{6.2}
\]

for every `I` suffices for a full rainbow matching.  For all slots,

\[
 \nu^*\le\frac{qW}{qa}=W/a=(1+o(1))s,                  \tag{6.3}
\]

while the right side of (6.2) is `(1-o(1))qW`.  It fails by the full factor
`qa`.  Equivalently, the bounded-degree rainbow theorem needs color classes
of order `rDelta`; the palette classes have order only `Delta`.  Recent
constructions of Pokrovskiy show that this generic factor is essentially
sharp.

## 7. Treating a same-time nested chain as one atom

Collapsing the `q` nested targets observed at one time into one flag atom
removes (1.3) from the **base** atom hypergraph, but it changes the problem.
Two distinct flag atoms may share a target at one rank.  Disjoint flag atoms
therefore do not imply target coverage without repetition.

There are only two honest ways to restore the original condition.

1. Add a conflict between flag atoms sharing any coordinate.  After lifting
   to block candidates, this is exactly the conflict graph of Section 5 and
   again has degree `Omega(n^2D)`.
2. Restrict to one fixed target-disjoint **augmented** flag factor.  Such a
   factor has at most `W` atoms because every padded rank part has `W`
   resources; supplying `as=W` observations forces it to be perfect in every
   part.  The global Aharoni--Haxell capacity calculation (6.1) applies again.
   At outer ranks such a factor necessarily uses dummies, so it is not even a
   family of full observed real flags.  Even if one grants an ideal family of
   at most `W` acceptable full flags, no theorem says that a tail-MTF state has
   an outgoing flag in it: the total number of full real flags is
   \[
   {n\choose m-H}(m+H+1)_{2H+1},
   \]
   which exceeds `W` by `n^{Theta(H)}`, while a state has only `d=Theta(n)`
   eligible successors.

Thus atomization either forgets the target constraint or replaces it by the
same unresolved tail-MTF-compatible chain-factor problem.

## 8. Configuration-model and absorption approaches

Independent sampling from the exact fractional law does not give a useful
starting configuration.  At a padded rank, a fixed resource is selected in
one slot with probability `a/W`, independently between slots.  Hence

\[
 \Pr(\text{resource missed})=(1-a/W)^s=e^{-1}+o(1).     \tag{8.1}
\]

The expected rank leave is `(e^{-1}+o(1))W`; over the real band it has the
coupon-scale mass `Theta(W\sqrt n)`.  Conditioning this configuration on
capacity one is precisely the integral matching event one is trying to
prove, so the configuration model by itself is circular rather than a
rounding theorem.

Generic iterative-absorption and design theorems fix the local template
size and require an explicit absorber/transformer plus divisibility and
typicality hypotheses.  Here the template size is `qa -> infinity`, the
best generic nibble guarantee stops at the critical `Theta(W)` real scale,
and no
tail-MTF-compatible absorber is present.  The reserve versions of
Gould--Kelly, Delcourt--Postle, and Joos--Mubayi--Smith likewise fix the host
and reserve ranks and require a separately verified reserve hypergraph.
Exact fractional balance is not a substitute for those hypotheses.

The 2026 unbounded-rank chromatic-index theorem of
Kang--Kelly--Kuehn--Methuku--Osthus also does not help.  For an `N`-vertex
hypergraph of absolute codegree `t` it gives a color bound on the scale
`tN`.  Here `t/D=Theta(1/n)` and `N=Theta(qW)`, so `tN/D=Theta(qW/n)` is
exponential.  Averaging its color classes covers only a negligible fraction.

## 9. Why a parameter-only repair cannot exist

The failure is not merely a missing estimate.  A regular projective
decoration supplies an explicit generic obstruction at the same pair scale.
Let a projective plane of order `p` have `b=p^2+p+1` points and lines.  Fix
`c>=1`, take a disjoint set `U` of size `bc`, put `t=c(p+1)`, and form all
edges

\[
 \ell\ \dot\cup\ F,
 \qquad \ell\text{ a projective line},\quad
 F\in{U\choose t}.                                     \tag{9.1}
\]

This is `r=(c+1)(p+1)` uniform and exactly regular of degree

\[
 D=(p+1){bc\choose t}.                                 \tag{9.2}
\]

Its normalized pair codegrees are

\[
 \frac1{p+1},\qquad
 \frac{p+1}{b},\qquad
 \frac{t-1}{bc-1},                                    \tag{9.3}
\]

for point--point, point--decoration, and decoration--decoration pairs,
respectively.  Thus `Delta_2/D=Theta(1/p)`, while `D` can be enormous and
the rank can be made arbitrarily larger than `p`.  Nevertheless every two
edges intersect because their projective lines intersect, so its matching
number is one.  Its uniform fractional matching has value
`b/(p+1)=Theta(p)`.  Taking disjoint unions makes the fractional optimum
arbitrarily large while preserving an integral/fractional gap of order `p`.

Taking `p=Theta(n)` and `c` large matches the palette scales
`Delta_2/D=Theta(1/n)` and `r\gg n`.  Therefore no theorem seeing only
regularity, enormous degree, growing rank, normalized pair codegree, and a
fractional perfect matching can prove the desired rounding.  A positive
theorem must use the Boolean nested-chain and tail-MTF chronology in an
essential way.  Higher codegrees distinguish (9.1), but Sections 4 and 7
show exactly why the published higher-codegree and chain-atom theorems still
stop at the critical `Theta(W)` boundary.

## 10. Exact remaining matching target

The fractional theorem has removed Hall/capacity and endpoint balance.  The
missing result is now an anisotropic integral theorem, not a generic nibble:

> Select one path from every fixed-endpoint block palette so that the union
> of the selected same-time Boolean flags has total real-resource collision
> and leave `o(W)`, while treating the forced adjacent-rank containment
> codegrees as factorable structure rather than as generic dependence.

A viable proof would need, for example, an entropy-preserving sequence of
rank-spaced roundings followed by a proved common-chain coinstantiation, or a
tail-MTF-compatible random chain factor with an explicit absorber.  None of
the audited black boxes contains that conclusion.

There is one useful positive diagnostic.  On one rank parity, same-time rank
gaps are at least two and the structural pair scale drops to `O(n^{-2})`.
If the corresponding all-codegree hypotheses were available, substitution
into the **unlogged leading term** of the Gould--Kelly bound would permit
`B=Theta(n)`, so that this stated upper-bound term would be
`O(T/n)=o(W)`.  This scale calculation neither verifies that fixed-rank
theorem for `r -> infinity` nor proves that such a matching exists here.
The unresolved issue is exactly that the even- and odd-rank projections must
use the **same** palette edge in every slot.  Applying a matching theorem to
one parity chooses the paths and leaves no theorem-backed freedom for
rounding the other.  This identifies a possible target--a two-projection
common matching theorem--but is not supplied by any result audited above.

## Primary sources used

- Ehard--Glock--Joos, *Pseudorandom hypergraph matchings*,
  <https://arxiv.org/abs/1907.09946>.
- Alon--Bollobas--Kim--Vu, *Economical covers with geometric applications*,
  <https://doi.org/10.1112/S0024611502013886>.
- Vu, *New bounds on nearly perfect matchings in hypergraphs: higher
  codegrees do help*,
  <https://doi.org/10.1002/1098-2418(200008)17:1%3C29::AID-RSA4%3E3.0.CO;2-W>.
- Kang--Kuehn--Methuku--Osthus, *New bounds on the size of nearly perfect
  matchings in almost regular hypergraphs*,
  <https://arxiv.org/abs/2010.04183>.
- Gould--Kelly, *Advancing the Rodl Nibble*,
  <https://arxiv.org/abs/2511.11375>.
- Delcourt--Postle, *Finding an almost perfect matching in a hypergraph
  avoiding forbidden submatchings*, <https://arxiv.org/abs/2204.08981>.
- Glock--Joos--Kim--Kuehn--Lichev, *Conflict-free hypergraph matchings*,
  <https://arxiv.org/abs/2205.05564>.
- Aharoni--Haxell, *Hall's theorem for hypergraphs*,
  <https://doi.org/10.1002/1097-0118(200010)35:2%3C83::AID-JGT2%3E3.0.CO;2-V>.
- Pokrovskiy, *Bounded degree graphs and hypergraphs with no full rainbow
  matchings*, <https://arxiv.org/abs/2401.06029>.
- Kang--Kelly--Kuehn--Methuku--Osthus, *Solution to a problem of Erdos on
  the chromatic index of hypergraphs with bounded codegree*,
  <https://arxiv.org/abs/2110.06181>.
