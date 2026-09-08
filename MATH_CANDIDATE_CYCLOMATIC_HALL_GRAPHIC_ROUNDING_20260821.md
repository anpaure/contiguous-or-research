# Cyclomatic Hall reduction and detached graphic rounding

**Status (2026-08-21).**  Everything stated as a theorem below is proved.
The note does not select palette paths.  It converts every omitted-rank Hall
deficiency into a graphic-matroid quota deficiency up to at most the number
of blocks, and proves that the canonical central transition marginals have
an exact forest-valued dependent rounding.  The surviving obstruction is
that the rounded graph edges must be coinstantiated as whole queue-coherent
paths, with the same paths also satisfying the projected resource matching.

## 1. Setup

Use the budget-normalized fixed-endpoint palette.  Thus every selected core
has length `a`, there are `s` slots, and

\[
 N=sa\le W,\qquad s=o(W).                              \tag{1.1}
\]

Fix one rank `q` reconstructed from the opposite parity as in
`MATH_CANDIDATE_PARITY_PROJECTION_HALL_REDUCTION_20260821.md`.  Once a
band-simple path has been selected in slot `i`, retain its temporal order and
write

\[
 B_{i,1},B_{i,2},\ldots,B_{i,a},\qquad
 U_i=\{B_{i,1},\ldots,B_{i,a}\}.                       \tag{1.2}
\]

The sets in (1.2) are distinct.  Write the real and dummy quotas as

\[
 r_i+h_i=a.                                            \tag{1.3}
\]

Because `q<f`, one legal tail-MTF step replaces exactly one member of its
top-`q` set.  Thus every consecutive pair in (1.2) is an edge of the
Johnson graph `J(n,q)`.

For `I subseteq [s]`, let `Gamma(I)` be the multigraph whose vertex set is
`union_(i in I) U_i` and which has, with their slot labels retained, the
temporal edges

\[
 B_{i,1}B_{i,2},\ B_{i,2}B_{i,3},\ldots,
 B_{i,a-1}B_{i,a}\qquad(i\in I).                      \tag{1.4}
\]

Parallel copies belonging to different slots remain different graph edges.
There are no loops.  Let `g(I)` be the number of connected components of
`Gamma(I)`, with `g(emptyset)=0`, and let

\[
 \beta(I)=|E(\Gamma(I))|-|V(\Gamma(I))|+g(I)           \tag{1.5}
\]

be its cyclomatic rank.

## 2. Hall deficiency is cyclomatic rank plus a boundary term

### Theorem 2.1 (exact cyclomatic Hall identity)

For every `I subseteq [s]`,

\[
 a|I|-\left|\bigcup_{i\in I}U_i\right|
   =\beta(I)+|I|-g(I).                                 \tag{2.1}
\]

Consequently the exact colored-Hall deficiency at rank `q` is

\[
 \boxed{
 \delta_q=
 \max_{I\subseteq[s]}
 \left(\beta(I)+|I|-g(I)-\sum_{i\in I}h_i\right)_+ .}
                                                               \tag{2.2}
\]

#### Proof

Every slot contributes its `(a-1)`-edge path, so

\[
 |E(\Gamma(I))|=(a-1)|I|.
\]

Substitution in (1.5) gives

\[
 \beta(I)=(a-1)|I|-\left|\bigcup_{i\in I}U_i\right|+g(I),
\]

which rearranges to (2.1).  Substitution of (2.1) into the exact defect-Hall
formula

\[
 \delta_q=\max_I
 \left(a|I|-\left|\bigcup_{i\in I}U_i\right|
                -\sum_{i\in I}h_i\right)_+
\]

proves (2.2).  \(\square\)

At the omitted middle rank `q=m+1`, all `h_i=0`.  Duplicate mass is
monotone under adding slots, so the maximum in (2.2) is attained at all
slots.  Hence

\[
 \boxed{\delta_{m+1}=\beta([s])+s-g([s]).}             \tag{2.3}
\]

Since `1<=g([s])<=s`,

\[
 \beta([s])\le\delta_{m+1}\le\beta([s])+s-1.          \tag{2.4}
\]

Thus, because `s=o(W)`, the central almost-rainbow condition is equivalent
to cyclomatic rank `o(W)`.  Literal vertex-disjointness of the paths is not
needed: a forest union may identify path vertices, but it creates at most
`s-1` duplicate observations.

## 3. Exact graphic-matroid quota deficiency

The term `beta(I)` in (2.2) is itself an exact matroidal Hall obstruction.
For every slot `i`, add a new private leaf `z_i` and the edge
`z_i B_(i,1)` to its temporal path.  Denote this `a`-edge augmented path by
`E_i`, and regard parallel graph edges as distinct elements of the graphic
matroid of the resulting multigraph.  The new leaf edge is a bridge, so for
every `I`

\[
 \left|\bigcup_{i\in I}E_i\right|=a|I|,
 \qquad
 r_{\rm gr}\!\left(\bigcup_{i\in I}E_i\right)
      =a|I|-\beta(I).                                  \tag{3.1}
\]

Let `epsilon_q` be the minimum total unmet quota when one tries to choose a
forest containing `r_i` edges from each augmented slot path.  Equivalently,
make `r_i` clones of slot `i`, join every clone to all elements of `E_i`,
and ask for the largest matching of clones to a graphically independent set
of edges.

### Theorem 3.1 (matroidal Hall formula)

\[
 \boxed{
 \epsilon_q=
 \max_{I\subseteq[s]}
 \left(\beta(I)-\sum_{i\in I}h_i\right)_+.}           \tag{3.2}
\]

Moreover,

\[
 \boxed{\epsilon_q\le\delta_q\le\epsilon_q+s.}       \tag{3.3}
\]

#### Proof

The defect form of Rado's matroidal Hall theorem says that the unmatched
clone count is

\[
 \max_X\bigl(|X|-r_{\rm gr}(N(X))\bigr)_+ .            \tag{3.4}
\]

For a fixed set `I` of represented slots, (3.4) is maximized by taking all
`r_i` clones of every `i in I`, since this does not enlarge the neighborhood.
Using (1.3) and (3.1), its value is

\[
 \sum_{i\in I}r_i-
 r_{\rm gr}\!\left(\bigcup_{i\in I}E_i\right)
 =a|I|-\sum_{i\in I}h_i-(a|I|-\beta(I)),
\]

which is (3.2).  Each nonempty union of `|I|` connected paths has
`1<=g(I)<=|I|`.  Therefore

\[
 0\le |I|-g(I)\le s-1.
\]

Comparing (2.2) and (3.2), including the empty set convention, proves
(3.3).  \(\square\)

In particular, if the rank-`q` augmented path edges admit all their graphic
quotas, then `delta_q<=s`.  If this holds at every omitted rank, then

\[
 \sum_{q\in Q}\delta_q\le |Q|s=o(W),                  \tag{3.5}
\]

because `|Q|=O(sqrt(n log n))` and `s=O(W/a)` with
`a=exp(n/5+o(n))`.  This is a sufficient graphic reformulation of the
same-path parity gate.  At the central omitted rank, `r_i=a`; quota
feasibility says exactly that the union of all temporal paths is a forest.

## 4. The canonical central marginals are exactly forest-roundable

The graphic condition has no marginal-polytope obstruction.  Put

\[
 G=J(n,m+1),\qquad
 D=(m+1)m,
\]

so `G` has `W` vertices, is `D`-regular, and has `WD/2` edges.  Sample one
band-simple canonical core in every slot, but for the moment retain only the
`a-1` temporal edges of its rank-`(m+1)` trace.  Relabeling invariance and
transitivity on Johnson edges imply that the expected total multiplicity of
every edge of `G` is

\[
 x_e={N-s\over WD/2}={2(N-s)\over WD}.                 \tag{4.1}
\]

### Lemma 4.1 (edge connectivity of a vertex-transitive graph)

Every finite connected `D`-regular vertex-transitive simple graph has edge
connectivity `D`.

#### Proof

The cut around one vertex gives connectivity at most `D`.  Let `A` be a
smallest shore, of size at most half the vertex set, among minimum cuts.  By
submodularity of the edge-boundary function, two translates of `A` are
either equal or disjoint: otherwise their nonempty intersection is a
smaller minimum-cut shore.  Transitivity then implies that the setwise
stabilizer of `A` acts transitively on `A`, so the induced graph on `A` is
`r`-regular for some `r`.  Put `c=D-r>=1`.  The cut has size `|A|c`, while
`r<=|A|-1`.  Therefore

\[
 D=r+c\le |A|-1+c\le |A|c.
\]

Thus every minimum cut has size at least `D`, proving equality.  \(\square\)

### Theorem 4.2 (exact detached forest rounding)

The vector `x` in (4.1) belongs to the graphic-matroid polytope of
`J(n,m+1)`.  More precisely, it is a convex combination of forests having
exactly `N-s` edges.

#### Proof

For a nonempty proper vertex set `X subsetneq V(G)`, Lemma 4.1 gives
`|partial X|>=D`, and hence

\[
 e_G(X)={D|X|-|\partial X|\over2}
       \le {D(|X|-1)\over2}.                           \tag{4.2}
\]

Equations (4.1)--(4.2) give

\[
 x(E_G(X))\le {N-s\over W}(|X|-1)\le |X|-1.           \tag{4.3}
\]

For the full vertex set,

\[
 x(E(G))=N-s\le W-1,                                  \tag{4.4}
\]

because `N<=W` and `s>=1`.  Equations (4.3)--(4.4) are precisely the
induced-subgraph inequalities for the graphic independence polytope.

Finally, `x(E(G))=N-s`.  The same inequalities show that `x` lies in the
base polytope of the rank-`(N-s)` truncation of the graphic matroid:
for every edge set `F`, `x(F)<=r_gr(F)` and `x(F)<=N-s`.  The integral-base
polytope theorem therefore decomposes `x` into incidence vectors of forests
of exactly `N-s` edges.  \(\square\)

The slot labels and private root edges from Section 3 can also be restored
at the one-edge-marginal level.  Given an `(N-s)`-edge forest from Theorem
4.2, partition its edges uniformly into `s` labeled parts of size `a-1`.
For a fixed slot `i` and Johnson edge `e`, the resulting marginal is

\[
 x_e{a-1\over N-s}={a-1\over WD/2},                   \tag{4.5}
\]

which is exactly the canonical slot-`i` marginal.  Independently, for each
`i` choose one edge `z_iB`, with `B` uniform in
`binom([n],m+1)`.  These private-leaf edges are always bridges.  Combining
the two choices gives a distribution on slot-labeled `N`-edge forests whose
individual edge marginals agree exactly with those of the canonical
augmented central paths.

Theorem 4.2 is deliberately called **detached**: a forest in its support need
not split into the `s` prescribed `a`-edge bundles, and even an arbitrary
split need not be the transition trace of a legal tail-MTF path.  It proves
that neither graphic acyclicity nor the one-edge marginals cause the
integrality gap.  The gap is whole-path coinstantiation.

This graphic feasibility coexists with the projected fractional resource
matching, rather than replacing it.  Let `y_(i,c)` be the canonical
fractional weight of decorated palette candidate `c` in slot `i`.  Give each
temporal or private-root edge occurrence in each candidate its own parallel
copy, and give that copy coordinate `y_(i,c)`.

### Theorem 4.3 (joint bundle LP has no fractional obstruction)

The same vector `y` simultaneously satisfies

1. one unit of weight in every slot;
2. all `P`-rank real/dummy resource-capacity constraints of the fractional
   near-factor; and
3. every graphic-matroid independence inequality for the candidate-labeled
   augmented rank-`(m+1)` edge copies.

#### Proof

The first two assertions are the budget-normalized fractional palette
theorem.  After parallel copies with the same Johnson endpoints are summed,
the temporal-edge coordinates are exactly (4.1).  The private-root
coordinates incident with a fixed `z_i` sum to one and have marginal `1/W`
for each possible central target.  Theorem 4.2, followed by the root-edge
construction above, shows that this aggregate vector is in the graphic
independence polytope.  Splitting the weight of any graph edge among
parallel labeled copies preserves every graphic rank inequality (and each
parallel class has total weight at most one).  Hence the candidate-labeled
copy vector is also in that polytope.  \(\square\)

An integral point satisfying the same constraints would have to take all
`a` edge copies of each chosen candidate together.  Theorem 4.3 asserts
only feasibility of the linear relaxation; it does not provide such an
integral bundle point.

There is an especially symmetric explicit decomposition of (4.1).  Choose a
uniform spanning tree `T` of `G`, and then choose a uniformly random
`(N-s)`-subset `F` of its `W-1` edges.  Edge-transitivity gives

\[
 \Pr(e\in T)={W-1\over WD/2},
 \qquad
 \Pr(e\in F)={2(N-s)\over WD}=x_e.                    \tag{4.6}
\]

Thus `F` is an exact realization of Theorem 4.2.  It also proves sharply
that a generic graphic rounding cannot be lifted after the fact.

### Theorem 4.4 (the symmetric forest rounding contains no palette block)

Let `F` have the uniform-spanning-tree thinning law above.  With probability
`1-o(1)`, `F` does not contain the full rank-`(m+1)` transition-edge trace of
even one band-simple legal `a`-step core.

#### Proof

The transfer-current determinantal formula for a uniform spanning tree,
followed by Hadamard's inequality, gives, for every set `L` of distinct
graph edges,

\[
 \Pr(L\subseteq T)\le
 \prod_{e\in L}\Pr(e\in T).                           \tag{4.7}
\]

(This is the standard negative-correlation inequality for spanning-tree
edges.)  A band-simple core trace is a path with `a-1` distinct Johnson
edges.  There are at most `n!d^a` seed-and-generator-labelled legal cores,
where `d=n-f+1=m-H`.  Put

\[
 p={2(W-1)\over WD}.
\]

Since `F subseteq T`, a union bound and (4.7) give

\[
 \Pr(\text{some legal core trace lies in }F)
 \le n!d^a p^{a-1}
 =n!d\,(dp)^{a-1}.                                    \tag{4.8}
\]

But

\[
 dp<{2d\over D}
 ={2(m-H)\over m(m+1)}<{2\over m+1}=O(1/n).           \tag{4.9}
\]

As `a=exp(n/5+o(n))`, the logarithm of the right side of (4.8) is
`O(n log n)-Omega(a log n)`, which tends to minus infinity.  This proves
the claim.  \(\square\)

Theorem 4.4 concerns this natural symmetric decomposition, not every
decomposition of `x`.  A successful proof must construct a highly
non-generic forest law supported on unions of legal path bundles, rather
than first round (4.1) and then look for paths inside the resulting forest.

The same proof gives a method-level obstruction broader than uniform
spanning trees.

### Corollary 4.4a (negative-cylinder rounding cannot contain a block)

Let `Y` be any random Johnson-edge set such that every edge has marginal at
most `C/D`, for an absolute constant `C`, and such that for every set `L` of
distinct edges belonging to a legal band-simple core trace,

\[
 \Pr(L\subseteq Y)\le\prod_{e\in L}\Pr(e\in Y).       \tag{4.10}
\]

Then, with probability `1-o(1)`, `Y` contains no complete legal `a`-step
trace.

#### Proof

The same union bound gives

\[
 \Pr(\text{some trace lies in }Y)
 \le n!d^a(C/D)^{a-1}
 =n!d\,(Cd/D)^{a-1}=o(1),                             \tag{4.11}
\]

because `Cd/D=O(1/n)` and `a=exp(n/5+o(n))`.  \(\square\)

In particular, any forest-valued rounding with the canonical
`Theta(n^(-2))` edge marginals that is supported on full palette paths must
create enormous positive cylinder correlation along those paths; a
negative-correlation or upper-cylinder-preserving rounding cannot be lifted
to path bundles.  Quantitatively, if such a law contains a legal trace with
probability one, then some trace `L` obeys

\[
 {\Pr(L\subseteq Y)\over\prod_{e\in L}\Pr(e\in Y)}
 \ge {1\over n!d}\left({D\over Cd}\right)^{a-1}
 =\exp\{(1+o(1))a\log n\}.                             \tag{4.12}
\]

Indeed, one of at most `n!d^a` traces has containment probability at least
their reciprocal, while its marginal product is at most `(C/D)^(a-1)`.

For a palette with fixed slot starts one does not pay the `n!` seed factor,
which makes the obstruction survive even for the new linear blocks.

### Corollary 4.4b (fixed-start linear palettes also require bundle correlation)

Consider `s` fixed-start slots whose legal cores have a common length `b`.
Under the marginal and upper-cylinder assumptions of Corollary 4.4a, the
probability that `Y` contains the transition trace of any candidate in any
slot is at most

\[
 s d^b(C/D)^{b-1}=sd\,(Cd/D)^{b-1}.                  \tag{4.13}
\]

In particular, for the common-endpoint palette with `b=n` and
`s<=W/n`, this probability is `o(1)`.

#### Proof

A fixed start has at most `d^b` generator words, so all slots together have
at most `sd^b` candidate traces.  The union bound gives (4.13).  When
`b=n` and `s<=W/n`,

\[
 \log(sd)+ (n-1)\log(Cd/D)
 \le n\log2-n\log n+O(n)\longrightarrow-\infty,
\]

because `d=Theta(n)` and `D=Theta(n^2)`.  \(\square\)

The absence of a graphic fractional obstruction is not restricted to the
middle rank.  Return to an arbitrary `q in Q`, put

\[
 M_q={n\choose q},\qquad D_q=q(n-q),\qquad
 R_q=\sum_i r_{i,q}\le M_q.                            \tag{4.14}
\]

Here `R_q=M_q` at an outer rank and `R_(m+1)=N`.  Given a canonical path in
slot `i`, choose uniformly `r_(i,q)` of its `a` augmented graph edges from
Section 3.  This is a fractional graphic-quota decoration; it is independent
of the real-target decoration.

### Theorem 4.5 (all omitted graphic quotas are fractionally integral)

For every `q in Q`, the expected candidate-labeled augmented-edge vector of
the graphic-quota decoration lies in the rank-`R_q` base polytope of a
truncation of its graphic matroid.  Hence it is a convex combination of
forests containing exactly `R_q` augmented edges.  These statements hold
simultaneously in the direct sum over all `q in Q`, together with the slot
constraints and the canonical `P`-resource fractional matching.

#### Proof

The expected total number of retained temporal edges is

\[
 {a-1\over a}R_q.
\]

Relabeling invariance makes their aggregate coordinate on every edge of
`J(n,q)` equal to

\[
 x^{(q)}_e={2(a-1)R_q\over aM_qD_q}.                  \tag{4.15}
\]

Applying Lemma 4.1 exactly as in (4.2)--(4.3), every proper nonempty target
set `X` satisfies

\[
 x^{(q)}(E(X))
 \le {R_q\over M_q}{a-1\over a}(|X|-1)
 \le |X|-1.                                           \tag{4.16}
\]

For the full target set,

\[
 x^{(q)}(E(J(n,q)))={a-1\over a}R_q\le M_q-1,         \tag{4.17}
\]

because `R_q<=M_q` and `a<=M_q` for all sufficiently large `n`.  Thus the
temporal vector is in the Johnson graphic independence polytope.

The private-root coordinates at slot `i` have total `r_(i,q)/a<=1` and are
supported on edges incident with the private vertex `z_i`.  This vector is a
convex combination of the empty set and one root edge.  Adding these
independent private-leaf extensions to any temporal forest preserves graphic
independence.  The combined vector has
total coordinate sum exactly

\[
 {a-1\over a}R_q+{1\over a}R_q=R_q.
\]

It therefore lies in the base polytope of the rank-`R_q` truncation and is
a convex combination of `R_q`-edge forests.  Splitting aggregate edge
weights among candidate-labeled parallel copies is legitimate exactly as in
Theorem 4.3.  Finally choose all graph-quota decorations and all
real/dummy resource decorations independently conditional on the same
canonical path.  The direct sum of the graphic matroids shares no graph
edge elements between ranks, so all asserted fractional constraints hold
simultaneously.  \(\square\)

Theorem 4.5 still rounds only individual graph-edge coordinates.  Its
forest decompositions need not keep the `r_(i,q)` chosen edges from a slot
together, still less instantiate all ranks with one legal palette path.

## 5. Why ordinary matroid rounding still does not select paths

For a collection of candidate path bundles, declaring a set of candidates
independent when the union of all their graph edges is a forest does not in
general define a matroid on the candidates.  The exchange axiom can already
fail for path bundles.  Let

\[
 A=(12,23,34),
\]

and let `B_1` be a three-edge path beginning with the chord `13`, while
`B_2` is a vertex-disjoint three-edge path beginning with the chord `24`
(apart from their displayed endpoints).  The singleton family `{A}` and
the two-bundle family `{B_1,B_2}` both have forest unions.  But `A union B_1`
contains the cycle `1-2-3-1`, and `A union B_2` contains
`2-3-4-2`.  Thus no member of the larger independent family augments the
smaller one.

This abstract example is not a no-go theorem for the tail-MTF palette; its
candidate paths have additional queue structure.  It shows only that the
graphic-matroid decomposition in Theorem 4.2 cannot be lifted by invoking
the ordinary matroid exchange theorem on whole candidates.

## 6. Exact remaining theorem after the graphic reduction

The subsequent one-central reduction
`MATH_REDUCTION_ONE_CENTRAL_MATCHING_PLUS_GRAPHIC_COLORS_20260821.md`
shows that it is enough to select one legal palette path in every slot such
that

1. the retained rank-`m` decks are pairwise disjoint; and
2. for every `k in K\setminus\{m\}`, the augmented temporal path-edge
   bundles have graphic quota deficiencies satisfying

   \[
   \sum_{k\in K\setminus\{m\}}\epsilon_k=o(W).          \tag{6.1}
   \]

Indeed, (3.3) gives

\[
 \sum_{k\ne m}\delta_k
 \le \sum_{k\ne m}\epsilon_k+|K|s=o(W),              \tag{6.2}
\]

and the one-central theorem then gives the coefficient-one DCC.

At every postponed rank, (6.1) asks for only `o(W)` excess cycle rank in
total among the queue-coherent transition paths.  The canonical marginals
already admit an exact forest decomposition by Theorem 4.2.  What remains
is a **one-middle-resource/bundled-graphic coinstantiation theorem**.  It is
not proved here.

## 7. Finite audit

All computations were run on `ssh h100`, not on the local machine.  For
1,800 deterministic-seed random path systems with `1<=s,a<=3`, arbitrary
quotas `0<=h_i<=a`, and a six-vertex target universe, exhaustive enumeration
of every augmented-edge subset agreed with both (2.2) and the Rado
deficiency (3.2).  Separately, exhaustive enumeration of every vertex subset
of `J(3,2)` and `J(5,3)` verified the forest inequalities used in Theorem
4.2.  These checks audit the normalizations only; the proofs are analytic.
