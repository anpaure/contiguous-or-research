# Audit and global gate for the context-hypercube tiling

Date: 2026-07-25

Method: exact enumeration and finite-group arguments only.

## 0. Verdict

`MATH_THEOREM_CONTEXT_HYPERCUBE_TILING_20260725.md` is correct, with the
following convention made explicit: cyclic orders are oriented modulo
rotation.  Reversal may subsequently be divided out everywhere and changes
no ratio or packing statement.

For `s=2^t` and one perfect matching `M` on a `2s`-set, its construction
really gives

\[
                         {2^{s-1}\over s}
\]

pairwise middle-disjoint and lower-rainbow context cycles.  The proof that
the lower colours are distinct uses the fixed matching `M`: an
`(s-1)`-interval missing the pair `P_i` determines the two adjacent folded
transversals obtained by adding the two elements of `P_i`.  Disjointness of
the folded cycles therefore forbids a repeated lower colour.

The restriction `s=2^t` is essential only for an **exact partition** of
one folded cube: divisibility already forces `s | 2^(s-1)`, hence forces
`s` to be a power of two.  It is harmless for the required
constant-density packing.  Theorem 3.2, added to the source note, maps the
prefix cycle injectively into the least power-of-two group of order
`r>=s` and gives `2^(s-1)/r >= 2^(s-2)/s` disjoint lower-rainbow cycles for
every integer `s`.  Thus no padding of the ambient dimension and no sparse
power-of-two subsequence is being used.

The global statement is not obtained merely by taking many whole cube
factors.  This note gives several precise advances toward that statement.

1. The intersection distribution of two matching cubes has an exact product
   generating function.
2. Consequently only `Theta(binomial(2s,s)/2^s)` matching cubes already have
   a union containing a positive proportion of all folded middle vertices.
3. A random matching cube has an exact Johnson-harmonic spectrum and sees
   the density of every fixed middle family to relative error
   `O(s^(-1/2))`.
4. The complete context-order hypergraph has a much stronger local
   pseudorandomness property than its maximum cross-codegree suggests: one
   selected row changes the degree of every surviving resource by only an
   `O(1/s)` fraction.
5. The remaining gap is now an exact finite-density anti-clustering/nibble
   statement.  A density assertion alone is insufficient, because `O(s)`
   deliberately placed rows can exhaust the useful facets around one middle
   vertex.

The matching-cube quotient is also compared below with the near-cyclic
wreath quotient.  They are structurally different quotients and the cube
factor does not itself supply a legal row-orbit edge for the latter.

## 1. Audit of the kernel tiling

Put

\[
 G=\mathbb F_2^s/\langle\mathbf 1\rangle,
 \qquad
 C=\{\bar p_0,\ldots,\bar p_{s-1}\},
 \qquad
 p_j=e_0+\cdots+e_{j-1}.
\]

The points of `C` are distinct.  Indeed, for `0<=i<j<s`, the vector
`p_i+p_j` is the indicator of a nonempty proper interval of coordinates,
and is therefore neither zero nor `1`.

The map

\[
 \psi(\bar e_i)=g_{i+1}+g_i
\]

is well defined because its values sum to zero, which is precisely the
relation killed in the quotient.  Telescoping gives

\[
 \psi(\bar p_j)=g_j+g_0.
\]

Thus `psi|C` is bijective, `H=ker psi` has size `2^(s-1)/s`, and the sets
`C+h`, `h in H`, partition `G`.

Replacing a representative `v` by `v+1` rotates `R_v` through `s` slots,
so the order depends only on `bar v`.  Every `(s-1)`-window of `R_v` chooses
one endpoint from `s-1` matching pairs and misses one complete pair.  The
two middle completions are consecutive vertices of `C+bar v`.  Hence a
repeated lower window between two selected orders would force a repeated
middle vertex.  Finally, proper cyclic intervals of a cyclic order of
distinct labels are distinct.  This verifies every step of Theorem 3.1.

The lower packet used by the factor has size

\[
 {2^{s-1}\over s}\,2s=2^s.
\]

The entire collection of lower sets compatible with `M` has size
`s2^(s-1)`, so one inner factor uses the exact fraction `2/s` of them.

For arbitrary `s`, the same calculation with
`r=2^(ceil(log_2 s))` gives `2^(s-1)/r` cycles and covers the fraction
`s/r>1/2` of the folded cube.  This is enough for every `Omega`-scale use
of the local theorem.  What cannot be claimed for non-powers of two is the
exact word "factor" inside one full cube.

## 2. Exact intersection polynomial for matching cubes

Fix a perfect matching `M_0` on `[2s]`.  For another perfect matching `M`,
let `c(M_0,M)` be the number of alternating components of the two-coloured
multigraph `M_0 union M`, counting a common edge as an alternating
two-cycle.

### Theorem 2.1 (component polynomial)

\[
 \boxed{
 \sum_M u^{c(M_0,M)}=\prod_{j=0}^{s-1}(u+2j).}
 \tag{2.1}
\]

#### Proof

Contract the `s` edges of `M_0`.  A connected alternating component on a
specified set of `ell` contracted vertices can be made in

\[
                         2^{\ell-1}(\ell-1)!
\]

ways.  This formula includes `ell=1`, when the component is a common edge.
The labelled exponential formula, marking every component by `u`, gives

\[
 \exp\left(
   u\sum_{\ell\ge1}{2^{\ell-1}(\ell-1)!\over\ell!}z^\ell
 \right)
 =(1-2z)^{-u/2}.
\]

Multiplying the coefficient of `z^s` by `s!` gives

\[
 2^s(u/2)^{\overline s}
 =\prod_{j=0}^{s-1}(u+2j),
\]

as claimed.  \(\square\)

The common transversal set has `2^c` unfolded vertices and `2^(c-1)`
folded vertices.  Hence, for a uniformly random perfect matching `M`,

\[
 \boxed{
 \mathbb E\,|Q(M_0)\cap Q(M)|
 ={2^{2s-1}\over\binom{2s}s}
 =\left({\sqrt{\pi s}\over2}+o(\sqrt s)\right).}
 \tag{2.2}
\]

Here `Q(M)` denotes the folded transversal cube.

### Corollary 2.2 (positive-density union of matching cubes)

Let `N=binom(2s,s)` and fix `0<alpha<1`.  There are

\[
 L=\left\lfloor {\alpha N\over2^s}\right\rfloor
\]

perfect matchings whose folded transversal cubes have union of size at
least

\[
 \boxed{
 \left({\alpha\over2}-{\alpha^2\over4}-o(1)\right)N.}
 \tag{2.3}
\]

#### Proof

Choose the matchings independently and uniformly.  Every cube has
`2^(s-1)` folded vertices.  Bonferroni and (2.2) give

\[
 \begin{aligned}
 \mathbb E\left|\bigcup_{i=1}^LQ(M_i)\right|
 &\ge L2^{s-1}
   -\binom L2{2^{2s-1}\over N}\\
 &=\left({\alpha\over2}-{\alpha^2\over4}-o(1)\right)N.
 \end{aligned}
\]

Some choice attains the mean.  Repetitions may simply be discarded.
\(\square\)

Thus the number of source cubes required at the global scale is not an
obstruction.  The obstruction is rounding their overlapping vertex sets
to whole prefix cycles.

### Proposition 2.3 (a large low-component code)

For every constant `A>log 2` and all sufficiently large `s`, there is a
family of at least `2^s/sqrt(s)` perfect matchings such that

\[
 c(M,M')\le {As\over\log s}
 \qquad(M\ne M').                                             \tag{2.4}
\]

Consequently every two of their folded cubes meet in at most

\[
                         \exp(O(s/\log s))                     \tag{2.5}
\]

vertices.

#### Proof

From (2.1), for `u>=1`,

\[
 \mathbb E u^c
 =\prod_{j=0}^{s-1}{u+2j\over1+2j}.
\]

For `j>=1`, use `log(1+x)<=x`; this gives

\[
 \log\mathbb E u^c
 \le \log u+{u-1\over2}(\log s+O(1)).                         \tag{2.6}
\]

Put `r=As/log s` and `u=2r/log s`.  Markov's inequality and (2.6) yield

\[
 \Pr(c\ge r)\le \exp(-As+o(s)).                              \tag{2.7}
\]

Join two perfect matchings when their component count exceeds `r`.  This
graph is vertex-transitive and its relative degree is bounded by (2.7).
The elementary greedy independent-set bound therefore gives an independent
set of size `exp(As-o(s))`, from which one may retain `2^s/sqrt(s)` members.
Equation (2.5) follows from the `2^(c-1)` intersection formula. \(\square\)

This is a genuine permutation-code construction, but it does not by itself
prove the context packing.  Even `exp(o(s))` shared vertices per pair can
touch different inner cycles, and deleting every touched cycle may multiply
the loss by `s`.  More importantly, at the necessary number
`L asymp N/2^s`, a generic middle vertex has constant cube load.  Whole-cube
overlap estimates therefore do not supply a cycle-level matching.

## 2A. Exact spectral mixing of a random matching cube

There is a stronger statement than the first two moments of the component
polynomial.  Work first on the unfolded middle layer.  Given an `s`-set
`S`, choose a uniformly random perfect matching across `(S,S^c)`, and then
choose a uniformly random transversal `T` of that matching.  Let `K` be the
resulting Markov operator on functions on `binom([2s],s)`.

### Theorem 2.4 (matching-cube spectrum)

On the degree-`j` Johnson harmonic, the eigenvalue of `K` is

\[
 \boxed{
 \theta_j=
 \begin{cases}
  0,&j\text{ odd},\\[1mm]
  \displaystyle{\binom{2\ell}{\ell}
       \over4^\ell\binom{s}{\ell}},&j=2\ell.
 \end{cases}}                                                  \tag{2.8}
\]

In particular, on the complement-invariant folded space the largest
nonconstant eigenvalue is

\[
                         \theta_2={1\over2s}.                  \tag{2.9}
\]

#### Proof

Write `z_x=1` when `x in S` and `z_x=-1` otherwise.  A random crossing
matching pairs every plus label to one minus label.  The random transversal
then chooses one endpoint of every pair independently.  For a label set
`A` of size `j`, the conditional expectation of `prod_(x in A)z_x(T)` is
zero unless every matching pair meeting `A` lies wholly in `A`.  Hence it
is zero for odd `j`.  For `j=2ell`, it equals

\[
 {(-1)^\ell\over\binom{s}{\ell}}
 \mathbf1_{\{|A\cap S|=\ell\}}.                               \tag{2.10}
\]

The coefficient of the full monomial `prod_(x in A)z_x` in the last
indicator is

\[
                         {(-1)^\ell\binom{2\ell}{\ell}\over4^\ell}.
\]

The squarefree monomials give the usual filtration whose successive
quotients are the Johnson harmonics.  Reading the leading coefficient in
(2.10) proves (2.8).  Positivity follows also from the incidence
factorization of `K`.  The displayed eigenvalues decrease after `ell=1`,
which proves (2.9). \(\square\)

### Corollary 2.5 (uniform density seen by a random cube)

Let `U` be any family of folded middle vertices of density `rho`, and let
`M` be a uniformly random perfect matching.  Then

\[
 \boxed{
 \operatorname {Var}|U\cap Q(M)|
 \le {2^{2s-2}\over2s}\rho(1-\rho).}                          \tag{2.11}
\]

Equivalently, for fixed `rho>0`, the relative standard deviation of the
intersection density is at most

\[
                         \sqrt{{1-\rho\over2s\rho}}.           \tag{2.12}
\]

#### Proof

Let `B` be the incidence matrix between perfect matchings and unfolded
transversals, let `q=2^s`, let `d=s!`, and let `N=binom(2s,s)`.  Then

\[
                         BB^*=dqK,
 \qquad
                         |\mathcal M|q=Nd.
\]

For the centered indicator `f=1_U-rho`, Theorem 2.4 gives

\[
 {1\over|\mathcal M|}\|B^*f\|_2^2
 ={q^2\over N}\langle f,Kf\rangle
 \le {q^2\over2sN}\|f\|_2^2.
\]

Dividing both the cube count and the universe by two gives exactly (2.11)
on the folded space. \(\square\)

Thus no globally clustered middle family can systematically hide from a
random matching cube: its **vertex density** is seen to relative accuracy
`O(s^(-1/2))`.  This still does not tile the residual.  A positive-density
subset of a Boolean cube can contain no prefix cycle (one parity class is
the elementary example).  The longitudinal theorem must therefore track
the higher-order geodesic availability, not merely cube intersection size.

## 3. The complete context-order hypergraph

Let `V_0` be the `N/2` folded middle vertices and let

\[
                         V_1=\binom{[2s]}{s-1}.
\]

An edge corresponding to a cyclic order contains `s` vertices of `V_0`
and `2s` vertices of `V_1`.  With oriented cyclic orders modulo rotation,

\[
 D_0=s!^2,
 \qquad
 D_1=(s-1)!(s+1)!={s+1\over s}D_0.                            \tag{3.1}
\]

Uniform edge weight `1/D_1` is a fractional matching which saturates every
lower vertex.  Its value is

\[
                         {1\over2(s+1)}\binom{2s}s,             \tag{3.2}
\]

the counting upper bound.  Thus there is no fractional capacity loss.

The pair codegrees needed below admit closed forms.  If `P={A,A^c}` and
`Q={B,B^c}` are distinct folded middle vertices and
`d=|A\setminus B|` after choosing representatives, then

\[
 {d(P,Q)\over D_0}={2\over\binom sd^2}\le {2\over s^2}.       \tag{3.3}
\]

If `T` is lower and `a=|A\cap T|`, then

\[
 \boxed{
 {d(P,T)\over D_0}
 ={2\over\binom sa\binom s{a+1}}.}                            \tag{3.4}
\]

The maximum `2/s` occurs precisely when `T` is a facet of `A` or of
`A^c`.  At every nonnested value `1<=a<=s-2`,

\[
                         {d(P,T)\over D_0}le {4\over s^2(s-1)}.
                                                                    \tag{3.5}
\]

For two distinct lower sets `T,U`, put `a=|T cap U|`.  If `a>0`, then

\[
 d(T,U)=2a!(s-1-a)!^2(a+2)!,                                  \tag{3.6}
\]

whereas for disjoint `T,U`,

\[
 d(T,U)=6(s-1)!^2.                                             \tag{3.7}
\]

Consequently

\[
 \boxed{
 {d(T,U)\over D_1}\le {6\over s(s+1)}.}                       \tag{3.8}
\]

All formulae follow by cutting the cyclic order into the successive Venn
arcs.  In (3.7), contraction leaves the four cyclic objects `T,U,x,y`,
and hence `(4-1)!=6` arrangements.

## 4. Aggregate codegree, the useful nibble parameter

The apparent `2/s` cross-codegree in (3.4) does not accumulate over all
`3s` resources of one edge.

### Lemma 4.1 (geometric nonaccumulation)

Let `E(R)` be the resource packet of one context order.

1. If a folded middle vertex `P={A,A^c}` is not in `E(R)`, at most one
   lower interval of `R` is a facet of `A`, and at most one is a facet of
   `A^c`.
2. If a lower set `T` is not in `E(R)`, at most one folded middle window of
   `R` has a representative containing `T`.

#### Proof

Two distinct `(s-1)`-intervals contained in the same `s`-set must start one
step apart; their union is then that `s`-set, which is a middle interval.
This proves the first assertion.  Similarly, two distinct `s`-intervals
containing one `(s-1)`-set start one step apart and have intersection equal
to that lower interval, proving the second. \(\square\)

### Theorem 4.2 (one-row aggregate codegree bound)

There is an absolute constant `C` such that for every resource vertex `v`
and every context edge `E(R)` not containing `v`,

\[
 \boxed{
 \sum_{u\in E(R)}d(v,u)\le {C\over s}\,d(v).}                 \tag{4.1}
\]

One may take `C=20` for every sufficiently large `s`.

#### Proof

If `v=P` is middle, the `s` other middle resources contribute at most
`2D_0/s` by (3.3).  Lemma 4.1 leaves at most two nested lower resources;
they contribute at most `4D_0/s` by (3.4).  The other lower resources
contribute `O(D_0/s^2)` by (3.5).  This is at most `7D_0/s` for large `s`.

If `v=T` is lower, Lemma 4.1 leaves at most one nested middle resource.
It contributes at most `2D_0/s`; the remaining middle resources contribute
`O(D_0/s^2)`.  All `2s` lower resources together contribute at most
`12D_1/(s+1)` by (3.8).  Since `D_0/D_1=s/(s+1)`, the claimed constant
follows. \(\square\)

This is the correct small parameter for a finite-density nibble.  In one
legal row selection, the degree of any still-unused resource drops by at
most an `O(1/s)` fraction.  The large nested cross-codegree cannot be hit
`Theta(s)` times by a single selected row unless that row already contains
the middle or lower resource itself.

## 5. The exact remaining finite-density gate

The preceding results isolate a substantially sharper matching statement.

> **Finite-density context nibble.** In the two-type context hypergraph of
> Section 3, construct a matching of at least
> \[
>                         c\,{\binom{2s}s\over s}
> \]
> edges for an absolute `c>0`.

A natural bite has edge probability `Theta(1/(sD_0))`.  Its candidate
conflict mean is `Theta(1)`, and one bite supplies `Theta(N/s^2)` accepted
rows.  Theorem 4.2 makes every surviving degree `O(1/s)`-Lipschitz under one
accepted row.  Thus `Theta(s)` bites are exactly the required scale and do
not encounter the entropy stall: at any fixed residual density `z>0`, the
heuristic degree is

\[
                         D_0 z^{3s-1}
 =\exp(2s\log s-O(s)),                                        \tag{5.1}
\]

which remains enormous.

The first bite is completely rigorous.

### Proposition 5.1 (one wasteful context bite)

There is an absolute `c_0>0` such that the complete context catalogue has a
matching of size at least

\[
                         c_0{N\over s^2}.                       \tag{5.2}
\]

More precisely, for every sufficiently small fixed `theta>0`, independent
sampling with probability

\[
                         p={\theta\over sD_0}                  \tag{5.3}
\]

and retention of the sampled edges which meet no other sampled edge has
expected size at least

\[
                         {\theta e^{-8\theta}\over2}
                         {N\over s^2}.                          \tag{5.4}
\]

#### Proof

One context edge meets at most

\[
 sD_0+2sD_1=(3s+2)D_0                                       \tag{5.5}
\]

catalogue edges, with multiplicity only making this upper bound safer.
Thus a fixed edge is sampled and isolated with probability at least

\[
 p(1-p)^{(3s+2)D_0}
 \ge p e^{-8\theta}.
\]

Also `|E|/D_0=N/(2s)`.  Summing the last probability over all catalogue
edges proves (5.4); some outcome attains its expectation. \(\square\)

The point of (5.4) is not its cardinality--the deterministic greedy bound
has the same order--but that it specifies the bite whose `Theta(s)`-round
iteration would reach the sharp scale, while Theorem 4.2 supplies the
correct `O(1/s)` one-step influence.

### Proposition 5.2 (exact longitudinal reduction)

Fix positive constants `a,b,gamma`.  Suppose that for
`R=floor(gamma s)` stages one can expose a residual context catalogue
`H_i`, disjoint from all rows previously retained, and a scale `d_i>0`
such that

\[
 |E(H_i)|\ge a{N d_i\over s},
 \qquad
 \max_{e\in E(H_i)}|N_{H_i}(e)|\le bs d_i.                    \tag{5.5a}
\]

Then the original context catalogue contains a lower-rainbow middle
matching of size

\[
                         \Omega_{a,b,\gamma}(N/s).             \tag{5.5b}
\]

#### Proof

At stage `i`, sample the edges of `H_i` independently with probability
`p=theta/(sd_i)`, where `theta>0` is a sufficiently small constant depending
only on `b`.  Retaining isolated sampled edges gives, in expectation,

\[
 |E(H_i)|p(1-p)^{bsd_i}
 \ge c(a,b,\theta){N\over s^2}.
\]

Choose an outcome attaining the expectation and delete every resource it
uses before the next stage.  The stage matchings are mutually disjoint by
the hypothesis on `H_i`.  Summing over `floor(gamma s)` stages proves
(5.5b). \(\square\)

Thus the global theorem needs neither an asymptotically perfect nibble nor
an `o(1)` leave.  It needs only a fixed-time, `Theta(s)`-bite preservation
of the two inequalities (5.5a).  The time-zero case is Proposition 5.1,
and Theorem 4.2 gives the requisite one-row Lipschitz scale.  The sole
longitudinal issue is to prevent facet/Johnson-sphere concentration from
destroying (5.5a) in an endogenous residual.

What is not yet proved is the necessary hereditary anti-clustering.  Global
density alone does not rule out concentration on the `2s` facets around one
folded middle vertex; exhausting those facets would make its residual degree
zero while changing the global density by an exponentially negligible
amount.  Whether such a configuration is reachable by a lower-rainbow
context matching is itself part of the hereditary question and is not
asserted here.  One must show that the random bites keep every facet
neighbourhood and every Johnson sphere close to its trajectory, or supply
an algebraic balancing rule that enforces this statewise.

There is, however, an exact trajectory invariant which rules out the crudest
residuals.  Unfold the middle resources, so that selecting one folded packet
removes all `2s` middle windows of its context order.

### Lemma 5.1 (two-rank residual one-design)

After deleting any lower-rainbow context matching of `k` rows, every ground
coordinate occurs equally often in the residual middle `s`-sets and equally
often in the residual lower `(s-1)`-sets.  More precisely, every coordinate
has lost exactly

\[
                         ks
 \quad\hbox{middle incidences, and}\quad
                         k(s-1)
 \quad\hbox{lower incidences}.                                \tag{5.6}
\]

#### Proof

In one cyclic order on `2s` labels, a fixed coordinate lies in exactly `s`
of the `2s` length-`s` windows and in exactly `s-1` of the `2s`
length-`(s-1)` windows.  The packets in a context matching are disjoint, so
the losses add. \(\square\)

Thus the endogenous residual has no degree-zero or degree-one Boolean
harmonic in either rank.  Point balance alone is not a supersaturation
theorem, but the finite-density nibble may exploit this exact invariant in
addition to Theorem 4.2; an arbitrary common-core residual is not reachable
by legal context rows.

Theorem 4.2 reduces the prospective martingale increments by a factor `s`
and is the main new input: the open statement is no longer a generic
growing-uniformity matching theorem with maximum codegree `2D/s`, but a
finite-time anti-clustering theorem for a system with aggregate influence
`O(D/s)`.

## 6. Comparison with the near-cyclic wreath quotient

The two quotient constructions should not be identified.

* In the matching cube, `G=F_2^s/<1>` parametrizes complementary
  **middle targets inside one fixed antipodal matching**.  A tile `C+h`
  is the folded packet of windows of one context row.
* In the near-`Z_n` wreath quotient, one fixes a coordinate `n`-cycle
  `sigma`.  A quotient edge is an orbit of `n` different wreath rows
  `{sigma^aR}` whose middle supports are mutually disjoint and transverse
  to the `sigma`-necklaces of middle targets.

Windows of one row are not the same object as coordinate translates of
that row.  Although the windows of `R_v` form an orbit under the coordinate
cycle induced by the order `R_v` itself, this cycle depends on `v`.  The
near-invariant quotient requires one common `sigma` for every chosen row.

Moreover, the family `R_(v_h)` is generated by independent endpoint flips
in the fixed matching.  It has `2^(s-1)/s` members, far more than one cyclic
coordinate orbit, and in general it is not closed under powers of any one
`2s`-cycle.  After the seven-coordinate balanced suspension, a context tile
still gives a `21`-row trade indexed by seed phases; it does not become an
`n`-row orbit with transversal middle necklaces.  A prime `n`-cycle cannot
even preserve the proper seed/context coordinate split.

Therefore the exact cube tiling supplies no automatic admissible row-orbit
packet for the near-invariant exact-cover hypergraph.  The constructions
are presently parallel:

1. the context cube attacks positive-density packing of suspended finite
   trades;
2. the cyclic quotient attacks phase transport or invariant quotient
   covering in one exact wreath factor.

Any bridge would require an additional theorem: after suspension, group
cube tiles into full orbits of one common coordinate cycle and prove that
their middle packets are necklace-transversal.  Neither the kernel tiling
nor its lower-rainbow property implies this condition.  In particular one
must not combine same-cycle invariance with the `1/n` projection gain from
conjugacy averaging; those are mutually different regimes.

## 7. Current mathematical status

The fixed-cube theorem is exact and audited.  The global source-cube count,
fractional capacity, exact overlap distribution, a large low-component
matching code, and the aggregate `O(1/s)` influence estimate are all now
proved.  The missing theorem is the finite-density anti-clustered nibble (or
an explicit recursive substitute) that rounds these partial cube factors to
whole context cycles while keeping both resource types disjoint.
