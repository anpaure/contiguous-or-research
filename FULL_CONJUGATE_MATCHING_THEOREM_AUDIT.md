# Quantitative matching-theorem audit for the full conjugate reservoir

## 0. Verdict

The apparent factorial degree of the full ordered-conjugate reservoir is a
parallel-occurrence degree, not the degree of its ordinary simple support.
After equal conjugate blocks are collapsed, one recovers the earlier
parameter-necklace family.  If `D_s` is its degree, then

\[
 \frac12(m)_\ell^2\le D_s\le 2\ell(m)_\ell^2,
 \qquad
 \log D_s=(2+o(1))\ell\log m.                        \tag{0.1}
\]

Allowing all radius labels changes this by a factor at most `H+1` and does
not change its logarithmic scale.  Consequently the maximum edge size still
satisfies

\[
 \frac K{\log D_s}=(2+o(1))\frac H{\log m}\to\infty. \tag{0.2}
\]

Thus the much larger degree does **not** survive passage to the ordinary
support.  If parallel occurrences are retained, their degree can indeed be
`(2m)!`, but they create no new matching choices and multiply every relevant
codegree by the same factor.  Their full-edge codegree in fact forces the
Gould--Kelly parameter `B=1+o(1)`.

Independently of this correction:

* Every physical radius-certified cycle block contains exactly two
  depth-one facets below each middle vertex.  Consequently the full
  conjugate support has the exact normalized nested pair load

  \[
     D_2/D\ge (2-o(1))/m.                            \tag{0.3}
  \]

  Full symmetry makes it exactly `2/(m+1)` in the ideal system, hence
  `(2+o(1))/m` asymptotically.
* Gould--Kelly therefore still has

  \[
      B\le(1+o(1))\sqrt{m/2}.                        \tag{0.4}
  \]

  Since the central band has

  \[
      V_H=(\sqrt\pi+o(1))W\sqrt m,                  \tag{0.5}
  \]

  the smallest nominal upper bound obtainable from that theorem is still
  at least `(sqrt(2pi)+o(1))W`, not `o(W)`.

No audited Kahn, Pippenger--Spencer, Gould--Kelly,
Ehard--Glock--Joos, or Alon--Bollobas--Kim--Vu statement yields an
`o(W)` singleton-cost rounding for these parameters.  Thus the additive
square-root barrier persists.  A structural absorption theorem is still
needed.

The audit uses the primary-theorem statements and exact transcription already
checked in `TYPED_MATCHING_QUANTITATIVE_AUDIT.md`; it does not infer a
growing-uniformity diagonal from fixed-uniformity asymptotics.

## 1. Parameters and typed universe

Use

\[
 H=\sqrt{m\omega(m)},\qquad
 \ell=HL,qquad
 R=2\ell,                                             \tag{1.1}
\]

where `omega,L->infinity` arbitrarily slowly and `ell=o(m)`.  A radius-`d`
decorated block has size

\[
 K_d=R(1+2\min(d,H)),                                 \tag{1.2}
\]

so

\[
 K:=\max_dK_d=(4+o(1))\ell H=(4+o(1))m\omega L.      \tag{1.3}
\]

The average edge size under the exact radius distribution is

\[
 K_{\rm av}
 =R\left(1+2\sum_{q=1}^H\rho_q\right)
 =(2\sqrt\pi+o(1))\ell\sqrt m
 =(2\sqrt\pi+o(1))mL\sqrt\omega,                    \tag{1.4}
\]

where `rho_q=binom(2m,m-q)/W`.

The complete typed vertex set is

\[
 \mathcal V_H=\binom{[2m]}m
 \ \dot\cup\!
 \bigdotcup_{q=1}^H
 \left(\binom{[2m]}{m-q}\dot\cup
       \binom{[2m]}{m+q}\right),                     \tag{1.5}
\]

and the local central-binomial estimate gives (0.5).

An integral matching must leave `o(W)` vertices of (1.5), equivalently the
much stronger relative error

\[
 o(W/V_H)=o(m^{-1/2}).                                \tag{1.6}
\]

## 2. Occurrence degree versus ordinary-support degree

Ignore the exponentially small bad-cell set, whose total repair cost is
`o(W)` by `MIXED_CONJUGATE_RESOLUTION.md`.

### 2.1 The factorial number is an occurrence degree

Let `G=S_{2m}`.  In the ideal no-defect system, for each `pi in G` the
conjugated base blocks partition the middle layer.  If repeated conjugates
are retained as parallel occurrences, every middle vertex therefore has
degree

\[
 D_{\rm occ}=|G|=(2m)!,\qquad
 \log D_{\rm occ}=\Theta(m\log m).                   \tag{2.1}
\]

The ideal simultaneous conjugate degree law gives the same occurrence
degree in every typed class.  In the actual system each class has relative
degree `1-o(1)` and the exact singleton completion pays `o(W)`.  These
statements are useful for the fractional matching, but they are not
statements about distinct available edges.

### 2.2 Collapsing stabilizers returns the parameter family

A length-`R=2ell` necklace uses `ell` active coordinate pairs.  Every middle
set in it contains the same core of `m-ell` coordinates and avoids the same
exterior set of `m-ell` coordinates.  Hence its pointwise stabilizer contains

\[
 S_{m-\ell}\times S_{m-\ell}.                        \tag{2.2}
\]

This already accounts for a factorial parallel multiplicity.

There are exactly

\[
 E_{\rm par}=W(m)_\ell^2                              \tag{2.3}
\]

parameter representations of the central necklaces.  Their represented
middle-vertex cycle recovers its cyclic order up to a dihedral choice and
then recovers the active coordinate pairs.  Thus one underlying necklace has
at most `4ell` parameter representations.  After parallel copies are
collapsed, transitivity and incidence counting give its simple middle degree
`D_s` satisfying

\[
 \frac12(m)_\ell^2
 \le D_s
 \le 2\ell(m)_\ell^2.                                \tag{2.4}
\]

In particular,

\[
 \log D_s
 =2\log (m)_\ell+O(\log\ell)
 =(2+o(1))\ell\log m.                                \tag{2.5}
\]

For a fixed radius label, conjugating any one source block produces this
same coordinate-labelled parameter family.  Allowing every radius
`d=0,\ldots,H` creates at most `H+1` decorated versions of a central
necklace, so

\[
 \log D_{\rm simple}
 =\log D_s+O(\log H)
 =(2+o(1))\ell\log m.                                \tag{2.6}
\]

Consequently

\[
 \frac K{\log D_{\rm simple}}
 =(2+o(1))\frac H{\log m}
 \longrightarrow\infty.                              \tag{2.7}
\]

The full conjugate reservoir therefore does not improve the ordinary
degree/uniformity ratio.

Keeping the parallel copies is even less useful for the quantitative
theorems.  Let `mu_H` be the common multiplicity of an underlying
maximum-radius decorated edge.  The type-`H` middle incidence is a
`rho_H` fraction of the full occurrence degree, so

\[
 \mu_H D_s=\rho_HD_{\rm occ},\qquad D_K\ge\mu_H.      \tag{2.8}
\]

In any formal max-uniform application that retains those identical edges,
the higher-codegree term in Gould--Kelly consequently forces

\[
 B\le (D_{\rm occ}/D_K)^{1/(K-1)}
 \le (D_s/\rho_H)^{1/(K-1)}.                         \tag{2.9}
\]

Since `-\log\rho_H=(1+o(1))H^2/m=(1+o(1))omega`,

\[
 (D_s/\rho_H)^{1/(K-1)}
 =\exp\left((1+o(1))\frac{\log m}{2H}+o(1)\right)
 =1+o(1).                                             \tag{2.10}
\]

Thus deduplication restores `K/\log D_s\to\infty`, while retaining
duplicates creates a fatal full-edge codegree.  There is no interpretation
of the factorial count that improves the matching theorem's parameters.

## 3. Correct ordinary sampling

The correct unweighted simple construction samples radius labels on
**distinct central necklaces**, not on their parallel conjugate
occurrences.  Give a central necklace radius `d` with probabilities

\[
 p_0=1-\rho_1,\qquad
 p_d=\rho_d-\rho_{d+1}\ (d<H),\qquad
 p_H=\rho_H.                                         \tag{3.1}
\]

Every middle degree is then exactly `D_s`.  Since
`sum_(d>=q)p_d=rho_q=N_q/W` and the untyped depth-`q` degree is
`D_sW/N_q`, every depth-`q` target has expected degree `D_s`.  Chernoff or
Bernstein bounds give simultaneous near-regularity and preserve the
conjugate pair-codegree bounds, because

\[
 D_s/m\gg m.                                         \tag{3.2}
\]

This is precisely the ordinary pretyping already audited in
`TYPED_MATCHING_QUANTITATIVE_AUDIT.md`.  Its logarithmic degree is (2.5),
so it retains `K/\log D_s\to\infty`.

Alternatively, one may sample conjugate **occurrences** and keep
multiplicity.  That gives an unweighted multihypergraph with any desired
degree up to `D_occ`, but its parallel copies do not change the set of
matchings.  Deduplicating it caps the degree at (2.6), while retaining the
copies multiplies degrees and codegrees together.  Neither interpretation
creates a factorial-sized ordinary simple support.

## 4. The unavoidable nested pair load

Let `B` be one decorated cycle block of radius at least one.  It contains
`R` middle vertices and `R` rank-`m-1` lower shadows.  A lower shadow is
contained in exactly the two endpoints of its physical Johnson edge.
Equivalently, each middle cycle vertex contains exactly its incoming and
outgoing lower facets.  Hence `B` contains exactly

\[
 2R                                                     \tag{4.1}
\]

ordered nested incidences `(X,S)` with `S subset X`, `|X|=m`, and
`|S|=m-1`.

Suppose an ordinary support has middle degrees `(1+o(1))D` and the exact
radius law up to `o(1)`.  Its total middle--edge incidence is
`(1+o(1))WD`; the fraction with radius at least one is

\[
 \rho_1=\frac{m}{m+1}=1-o(1).                        \tag{4.2}
\]

Summing (4.1) gives `(2+o(1))WD` nested pair incidences.  There are exactly

\[
 Wm                                                     \tag{4.3}
\]

ordered middle--facet pairs.  Therefore their average codegree is

\[
 (2+o(1))D/m,                                         \tag{4.4}
\]

and the maximum codegree is at least this large.

In the complete conjugate occurrence support, `S_(2m)` is transitive on nested pairs,
so every such pair has exactly

\[
 \codeg(X,S)=\frac{2D_{\rm occ}}{m+1}.               \tag{4.5}
\]

The harmless `m+1` correction is the certification probability (4.2).
For the ordinary radius-pretyped support, the incidence average (4.4) and
concentration give maximum codegree at least `(2-o(1))D/m` and uniform
`O(D/m)` control on these nested pairs.

This proves (0.3) without any coarse orbit bound.  Increasing `D` multiplies
both degree and codegree and leaves their ratio unchanged.

The other exact conjugate codegrees are smaller: equal-rank middle pairs at
Johnson distance `r` have normalized load at most

\[
 (R-1)/\binom{m}{r}^2,                                \tag{4.6}
\]

and the diagonal-orbit formula in `MIXED_CONJUGATE_RESOLUTION.md` controls
all remaining types.  None can remove the lower bound (4.4).

## 5. Pippenger--Spencer and Kahn-type asymptotics

The classical Pippenger--Spencer edge-coloring theorem and the standard
Pippenger--Frankl--Roedl almost-perfect matching theorem take the uniformity
as fixed.  Their qualitative conclusion is a matching leaving `o(V_H)`
vertices when degrees are asymptotic and relative codegrees vanish.

Even if one ignored the growing uniformity (1.3), that conclusion would be

\[
 o(V_H)=o(W\sqrt m),                                  \tag{5.1}
\]

not the required `o(W)`.  One needs a quantitative relative error
`o(m^(-1/2))`, which their fixed-uniformity statements do not provide.

The same issue applies to the locally cited Kahn-type asymptotic
edge-coloring paradigm.  A `(1+epsilon)D` edge coloring of an ideal
`K`-uniform `D`-regular support has a largest color class covering at least a
`1/(1+epsilon)` fraction of its vertices.  Its uncovered set is only bounded
by `O(epsilon V_H)`.  To reach `o(W)` one needs

\[
 \epsilon=o(m^{-1/2}).                                \tag{5.2}
\]

No audited fixed-rank Kahn/Pippenger--Spencer statement supplies (5.2)
uniformly for `K` in (1.3).  The ordinary simple support still has
`K/\log D_s\to\infty`.  The fact that the parallel occurrence degree
`D_occ` is factorial does not constitute an explicit diagonal threshold.

Replicating edges can make `D` arbitrarily large without changing the set of
available matchings, so degree magnitude by itself cannot justify such a
diagonalization.

## 6. Gould--Kelly: the square-root barrier is unchanged

Theorem 1.4 of Gould--Kelly, in the notation audited in
`TYPED_MATCHING_QUANTITATIVE_AUDIT.md`, requires

\[
 B\le\sqrt{D/D_2}.                                    \tag{6.1}
\]

Equation (4.4) forces (0.3).  Even delete every logarithmic loss and pretend
that the nonuniform, growing-`K` support satisfies all remaining hypotheses.
Then

\[
 \frac{V_H}{B}
 \ge(\sqrt{2\pi}+o(1))W.                             \tag{6.2}
\]

The actual bound is

\[
 V_HB^{-1+\gamma}(\log D)^A,                         \tag{6.3}
\]

so it is worse.  The tracked-weight clause also places the lower bound
`tau(V)/B` on the leftover weight promised for each accepted weight.  Taking
the disjoint rank indicators and summing reproduces the `Theta(W)` scale.

This is the optimistic **simple-support** calculation.  If the factorial
parallel occurrences are retained instead, the full-edge codegree
(2.8)--(2.10) forces `B=1+o(1)` before the pair-codegree estimate is even
used.

The factorial occurrence degree would formally remove the inequality
`K/\log D\to\infty` if parallel multiplicities were allowed as degree.
The ordinary simple degree does not remove it.  Even under the favorable
multihypergraph reading, three further issues remain:

1. the published theorem fixes `K` in its parameter hierarchy;
2. our edge sizes range over `R,3R,...,(1+2H)R`;
3. the mandatory bound (6.1) already prevents `o(W)`.

Thus no choice of `D` or slower `omega,L` makes Gould--Kelly close the
problem.

## 7. Uniformization does not help

Padding every edge privately to size `K` produces degree-one dummy vertices
and destroys near-regularity.  Even an optimistic public regular padding has
a fatal cost.

The number of dummy vertices required at degree `D` is at least

\[
 V_H\left(\frac K{K_{\rm av}}-1\right)
 =\left((2/\sqrt\pi+o(1))\sqrt\omega-1\right)V_H.    \tag{7.1}
\]

The padded universe therefore has order `Theta(WH)`.  Dividing by the same
`B=O(sqrt m)` gives at least

\[
 \Omega(W\sqrt\omega),                               \tag{7.2}
\]

even worse than (6.2).

Splitting the support by radius `d` makes each piece uniform but destroys
regularity across its middle and depth classes.  More importantly, the
different radius pieces compete for the same middle vertices.  Matching
them independently and stitching their outputs is exactly the invalid
operation excluded by the radius-bundled formulation.

## 8. Ehard--Glock--Joos

Their audited quantitative theorem uses a codegree exponent `delta` with

\[
 D_2\le D^{1-\delta},\qquad
 \varepsilon=\delta/(50K^2),                         \tag{8.1}
\]

and error `D^{-\varepsilon}`.  From `D_2/D>=c/m`,

\[
 \delta\le\frac{\log m+O(1)}{\log D}.                \tag{8.2}
\]

Therefore, for every sampled degree `D`,

\[
 D^{-\varepsilon}
 \ge\exp\left(-\frac{\log m+O(1)}{50K^2}\right)
 =1-o(1).                                             \tag{8.3}
\]

The larger `log D` cancels between (8.1) and (8.2); it gives no improvement.
The theorem also fixes uniformity and has an edge/weight count restriction
which fails under the formal growing-`K` substitution, as detailed in the
earlier audit.

## 9. Alon--Bollobas--Kim--Vu

The locally audited growing-uniformity theorem requires

\[
 e^{2K}C=o(D/\log D),                                 \tag{9.1}
\]

where `C` is maximum codegree.  With `C/D>=c/m`, this implies

\[
 e^{2K}\frac{\log D}{m}=o(1),                        \tag{9.2}
\]

which is impossible for `K->infinity`.  Increasing `D` only increases the
remaining logarithm after the ratio `C/D` cancels.

Even without (9.1), its uncovered fraction contains a
`1/(K-1)` power of `C log(1+C)/D`.  Since `K` is of order `m omega L`, this
power tends to one and gives no useful relative defect.

## 10. What the full reservoir actually resolves

The full conjugate construction proves several facts that were absent in the
earlier typed-family audit:

* exact occurrence degree `(2m)!` and its stabilizer collapse to (2.4);
* simultaneous transitive regularity at every radius and depth;
* much smaller equal-rank middle codegrees;
* an exact low-cost fractional singleton completion.

These facts eliminate density and fixed-pair bias as explanations of the
failure.  They do not improve the ordinary-support logarithmic degree, and
they leave the independent exact bottleneck:

\[
 \boxed{\text{nested depth-one load }2/m
        \quad\Longrightarrow\quad
        V_H\sqrt{D_2/D}=\Theta(W).}                  \tag{10.1}
\]

This is a barrier to the audited black-box theorem rates, not a lower bound
on the optimum matching of the structured conjugate reservoir.  The
Mixed-Conjugate Resolution Conjecture may still be true through correlated
trades or absorption.

## 11. The theorem family that could still succeed

The missing conclusion is:

> In the radius-bundled full conjugate reservoir, the exact fractional
> matching with `o(W)` singleton mass has an integral perfect matching with
> `o(W)` singleton cost.

No theorem based only on `K,D,D_2` can imply it: parallel projective-plane
examples have arbitrarily large `D`, relative codegree `O(1/m)`, and
matching number one.  A successful proof must use the properties absent
there--the nested-chain flags, the symmetric-group orbit structure, and
explicit multi-conjugate absorbers.

The closest existing paradigm is exact-design or iterative absorption, not
a stronger nibble--in particular, the Keevash design paradigm and the
Glock--Kuehn--Lo--Osthus iterative-absorption paradigm.  Their standard
theorems cannot simply be quoted:
their fixed template/complex and extendability hypotheses have not been
verified for the growing, nonuniform radius bundles.  What would suffice is
the following concrete structural package.

### 11.1 Kuperberg--Lovett--Peled exact averaging

The [Kuperberg--Lovett--Peled
theorem](https://arxiv.org/abs/1302.4295) is superficially an exact fit.
Take `B` to be the set of decorated conjugate **occurrences** and let `V`
contain every typed-vertex incidence function

\[
 f_v(e)=1_{\{v\in e\}}.                              \tag{11.1}
\]

In the ideal system,

\[
 |B|=|S_{2m}|W/R,\qquad
 |B|^{-1}\sum_{e\in B}f_v(e)=R/W.
\]

Thus a KLP subset of size `N=W/R` with the exact average would cover every
typed vertex exactly once and would be the required perfect matching.

However, KLP's Main Theorem requires

\[
 \min(N,|B|-N)
 \ge Cc_2c_3^2\dim(V)^6
       \log(2c_3\dim(V))^6,                          \tag{11.2}
\]

where `c_2,c_3>=1` are the bounded integer-basis constants.  Here the
dimension is essentially `W`, not a small number of orbit types.

Indeed, let `A` be the `W`-by-`|B|` middle-incidence matrix and put
`M=AA^T`.  Its diagonal is `D_occ`.  A pair of middle vertices at Johnson
distance `r` has codegree at most
`D_occ(R-1)/binom(m,r)^2` and has codegree zero for `r>ell`.  Therefore

\[
\begin{aligned}
 \operatorname{tr}M&=WD_{\rm occ},\\
 \operatorname{tr}(M^2)
 &\le WD_{\rm occ}^2
 \left(1+(R-1)^2
       \sum_{r=1}^{\ell}\binom{m}{r}^{-2}\right)\\
 &=WD_{\rm occ}^2(1+O(R^2/m^2)).
\end{aligned}                                        \tag{11.3}
\]

The trace-rank inequality gives

\[
 \dim(V)\ge\operatorname{rank}A
 \ge\frac{(\operatorname{tr}M)^2}
          {\operatorname{tr}(M^2)}
 =(1-o(1))W.                                         \tag{11.4}
\]

Since `N=W/R`, condition (11.2) is impossible even after setting
`c_2=c_3=1` and deleting the logarithm.  Tracking fewer functions does not
help in the natural linear formulation: orbit sums certify only aggregate
coverage, not one use of each middle vertex.  One can arithmetically encode
many coordinates into a few rational functions only by introducing huge
integer-basis constants, which reappear as `c_2` in (11.2).  No
bounded-basis compression of the pointwise incidence constraints is known;
the statement here is an audit of the natural incidence space, not a
universal impossibility theorem for every exotic encoding.

There are additional unverified hypotheses.  The available coordinate
action is not transitive across different radius types; KLP also needs a
bounded `ell_1` integer basis for `V^perp`, which here is precisely a
bounded decorated-trade theorem, and its divisibility condition asks for a
signed integral exact cover rather than merely the known fractional one.
The dimension-six condition already rules out the theorem, independently
of these issues.

### 11.2 Keevash's Designs II

[Designs II](https://arxiv.org/abs/1802.05900) genuinely handles labelled
faces, colours, orders, lattices, and Baranyai-type decompositions, so it is
the right conceptual family.  Its theorem does not apply to the present
parameters.

Encoding one decorated block as a copy of a template requires template size
`q=K` (or at least `q=R` after the unproved chain contraction), and the
radius/type data also grow.  Keevash's theorem first fixes `q,r,D` and then
takes `n>n_0(q,D)`.  Its displayed hierarchy contains

\[
 h=2^{50q^3},\qquad
 \delta=2^{-10^3q^5},\qquad
 n^{-\delta}<\Omega<\Omega_0(q,D).                  \tag{11.5}
\]

Here `n=V_H=\exp(Theta(m))` while already `q>=R=m^{1/2+o(1)}`.  Hence
`delta log n=o(1)` and `n^{-delta}=1-o(1)`, incompatible with the required
small-`Omega` hierarchy (normalize the stated small constant
`Omega_0(q,D)` to be at most `1/2`).  More fundamentally, its quantifiers
fix `q,r,D` before `n` tends to infinity; the published theorem supplies no
growing-template diagonal.

More structurally, coordinate transitivity proves only one-point degree
regularity.  Designs II requires a robust fractional decomposition,
extendability for every bounded partial labelled embedding, and membership
of the target in the signed decomposition lattice.  The radius bundles have
strong orbit-dependent nested correlations, and none of these
multi-extension or lattice hypotheses has been established.  Proving them
would amount to constructing the multiconjugate trades and cascades sought
below.

Thus KLP is defeated quantitatively by the incidence rank, while Designs II
is blocked by growing template size and the unproved extendability/lattice
structure.  Neither is an exact rounder available off the shelf.

### 11.3 Robust packet absorbers

Call a small typed set `U` admissible if its incidence vector satisfies the
local type and orbit lattice conditions generated by real decorated blocks.
An absorber for `U` is a pair of real-edge matchings `(P_U^0,P_U^1)` such
that

\[
 V(P_U^1)=V(P_U^0)\mathbin{\dot\cup}U.                 \tag{11.6}
\]

A sufficient absorber hypothesis is:

1. every admissible packet of size at most `s_m=m^{O(1)}` has
   `D^{Omega(1)}` absorbers using `m^{O(1)}` real blocks;
2. these absorbers are spread: prescribing any additional typed vertex or
   real block reduces their number by a factor `D^{Omega(1)}`;
3. every leftover produced by a coarse matching can, after discarding
   `o(W)` vertices, be partitioned into admissible packets; and
4. a disjoint absorber reservoir can be chosen for all those packets while
   occupying `o(V_H)` vertices.

Reserve the `P_U^0` states, find the coarse matching outside the reservoir,
assign its packets to disjoint absorbers, and switch `P_U^0` to `P_U^1`.
This absorbs the entire `Theta(W)` square-root residue and pays singletons
only for the final `o(W)` discarded vertices.  These four assertions are the
precise hypotheses under which the iterative-absorption paradigm crosses
(6.2).

The local work already shows why clause 1 is nontrivial.  The elementary
decorated Johnson-square and cactus candidates do not supply the required
multidepth trades (`CACTUS_ABSORBER_AUDIT.md`), and concatenation-local MSW
trades cannot alter a deeper shadow while fixing depth one
(`MSW_MULTIRANK_LOCAL_TRADES.md`).  A valid absorber must therefore combine
several conjugates or larger interaction components.

### 11.4 Chain-quotient alternative

There is a second, potentially weaker route.  First resolve almost all typed
band vertices into compatible oriented vertical chain segments, and contract
each whole segment to one atom.  The remaining necklace problem has edge
size `R=2ell` instead of `Theta(ell sqrt(m))`; its same-rank relative
codegree is `O(m^{-2})`, while the forced `Theta(m^{-1})` incidences have
become internal links of one atom rather than competing hypergraph pairs.

The exact missing hypothesis is a **shift-compatible chain resolution**:

\[
 \text{all but }o(W)\text{ band vertices lie in disjoint admissible chains,}
 \tag{11.7}
\]

with their contracted atoms admitting a matching that bundles all but
`o(W)` initialization cost into length-`R` pair-flip necklaces.  This is the
two-stage radius-typed chain-bundle theorem isolated in
`TYPED_MATCHING_QUANTITATIVE_AUDIT.md`.  It would also evade (4.5), because
the nested pairs are deliberately contracted rather than treated as
codegrees.

Thus there are two honest routes beyond the audited barrier:

* prove abundant, bounded-overlap multiconjugate packet absorbers; or
* prove the shift-compatible chain quotient and round only the contracted
  necklace hypergraph.

Neither structural hypothesis is currently established.  Merely increasing
the conjugate degree, resampling more occurrences, or invoking an exact
design theorem without verifying one of these hypotheses does not advance
the proof.

## 12. Ledger

| question | result |
|---|---|
| full parallel occurrence degree | `(2m)!` |
| ordinary simple degree | between `(m)_ell^2/2` and `2ell(m)_ell^2` per radius family |
| ordinary simple log-degree | `(2+o(1))ell log m` |
| maximum uniformity | `(4+o(1))m omega L` |
| can `K=o(log D_simple)`? | no; `K/log D_simple~2H/log m->infinity` |
| sampled regular simple support? | yes, by radius pretyping, at degree `D_s` |
| keeping factorial parallel degree | full-edge codegree forces `B=1+o(1)` |
| normalized nested codegree | exactly `2/(m+1)` for ideal occurrences; `(2+o(1))/m` after pretyping |
| Pippenger--Spencer/Kahn qualitative leftover | only `o(W sqrt m)` |
| Gould--Kelly nominal leftover | at least `(sqrt(2pi)+o(1))W` |
| Ehard--Glock--Joos error | `1-o(1)` after substitution |
| Alon--Bollobas--Kim--Vu hypothesis | fails |
| Kuperberg--Lovett--Peled | natural incidence space has `dim V=(1-o(1))W`, so its size hypothesis fails |
| Keevash Designs II | growing template and unproved extendability/lattice hypotheses |
| `o(W)` singleton-cost integral rounding | not obtained |

The factorial reservoir degree is useful for proving the symmetric
fractional laws.  It is not a larger ordinary support and it cannot cross
the last square-root.  The additive barrier persists exactly where the
physical chain geometry forces it.
