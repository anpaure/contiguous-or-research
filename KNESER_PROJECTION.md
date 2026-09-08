# Kneser cycles and Catalan projection

This note audits the idea of obtaining the Catalan linear forest from a
Hamilton cycle in a Kneser graph.  All assertions before the final missing
lemma are proved.  No computational evidence is used.

Fix `m>=3`, let `Omega=[2m]`, and put

\[
 \mathcal A=\binom{\Omega}{m-1},\qquad
 \mathcal M=\binom{\Omega}{m},
\]

\[
 N=|\mathcal A|=\binom{2m}{m-1},\qquad
 W=|\mathcal M|=\binom{2m}{m},\qquad
 K=W-N=\frac{W}{m+1}.                                      \tag{0.1}
\]

The Kneser graph `KG=K(2m,m-1)` has vertex set `mathcal A`; two vertices are
adjacent when they are disjoint.

## 1. Successor projection

Orient a Hamilton cycle of `KG` and write it as

\[
 C=(S_0,S_1,\ldots,S_{N-1}),                               \tag{1.1}
\]

with cyclic indices.  Its successor map

\[
 g(S_i)=S_{i+1}                                             \tag{1.2}
\]

is a permutation of `mathcal A` satisfying `S cap g(S)=emptyset`.

For every directed arc `A -> B` of `C`, the complement of `B` is an
`(m+1)`-set containing `A`.  Pair

\[
 A\longmapsto U_A:=\Omega\setminus B.                       \tag{1.3}
\]

These pairs form a perfect matching between ranks `m-1` and `m+1`.  If

\[
 \Omega\setminus(A\cup B)=\{x,y\},                          \tag{1.4}
\]

then the matched interval `[A,U_A]` induces the Johnson edge

\[
 (A\cup\{x\})(A\cup\{y\})                                  \tag{1.5}
\]

on the middle layer.

### Proposition 1 (cycle-cover equivalence)

The construction above works without Hamiltonicity.  Arbitrary perfect
matchings between ranks `m-1` and `m+1` are equivalent to directed cycle
covers of `KG`: permutations `g` of `mathcal A` for which every arc
`S -> g(S)` is a Kneser edge.

Requiring `g` to be the successor permutation of one Hamilton cycle is
therefore a genuine extra restriction, not an equivalent reformulation of
the Catalan linearization problem.

#### Proof

Given a perfect matching `h` from a lower set `S` to a containing upper set,
put `g(S)=Omega minus h(S)`.  Complementation is a bijection between the two
colour layers, and `S subset h(S)` is equivalent to `S cap g(S)=emptyset`.
Thus `g` is a permutation consisting of directed disjointness cycles.  The
reverse construction is (1.3).  QED.

## 2. Canonical facet bicliques

For a middle set `P`, define its facet family

\[
 \mathcal F(P)=\{P\setminus\{a\}:a\in P\}.                 \tag{2.1}
\]

Both `mathcal F(P)` and `mathcal F(P^c)` have size `m`, and every member of
one is disjoint from every member of the other.  For `m>=3`, there are no
Kneser edges inside either family.  Hence they induce a canonical copy

\[
 \mathcal K(P)=K_{m,m}                                     \tag{2.2}
\]

in `KG`.  Notice that `mathcal K(P)=mathcal K(P^c)`.

For an oriented Hamilton cycle or cycle cover `C`, let

\[
 e_C^+(P)=
 \#\{A\longrightarrow B\in C:
       A\in\mathcal F(P),\ B\in\mathcal F(P^c)\},          \tag{2.3}
\]

and let `t_C(P)` be the total number of directed arc occurrences between the
two sides of `mathcal K(P)` after orientation is forgotten but multiplicity
is retained.  Thus, if a cycle cover contains both arcs `A -> B` and
`B -> A`, their common underlying Kneser edge is counted twice.

### Theorem 2 (exact cut-projection formula)

The degree of `P` in the projected Johnson graph is

\[
 d_C(P)=e_C^+(P),                                          \tag{2.4}
\]

and

\[
 t_C(P)=d_C(P)+d_C(P^c).                                   \tag{2.5}
\]

Consequently, the projection has maximum degree at most two if and only if,
for every complementary middle pair `(P,P^c)`,

\[
 e_C^+(P)\le2\quad\hbox{and}\quad e_C^+(P^c)\le2.          \tag{2.6}
\]

Equivalently:

* `t_C(P)<=4` for every `P`;
* if `t_C(P)=3`, the three arc occurrences are not all oriented the same way
  across the biclique; and
* if `t_C(P)=4`, the four occurrences split two in each direction.

#### Proof

A projected edge from an arc `A -> B` is incident with `P` precisely when

\[
 A\subset P\subset\Omega\setminus B.                       \tag{2.7}
\]

The first containment says `A in mathcal F(P)`, and the second says
`B in mathcal F(P^c)`.  This proves (2.4).  Reversing the two sides gives
the contribution to `P^c`, so every arc occurrence crossing the biclique is
counted in exactly one of the two directed quantities.  This proves (2.5)
and the stated criterion.  QED.

This is the exact property that ordinary Kneser Hamiltonicity does not
address.  Each of the `W/2` canonical bicliques must be crossed only four
times, with a nearly perfect directional balance.

### Proposition 3 (the four-crossing budget is sharp)

For every directed cycle cover,

\[
 \sum_{P\in\mathcal M}d_C(P)=2N,\qquad
 \sum_{P\in\mathcal M}t_C(P)=4N.                           \tag{2.8}
\]

If the projection has maximum degree two, then

\[
 \sum_{P\in\mathcal M}(2-d_C(P))=2K,                       \tag{2.9}
\]

and

\[
 \sum_{P\in\mathcal M}(4-t_C(P))=4K.                      \tag{2.10}
\]

#### Proof

Every projected Johnson edge has two endpoints, proving the first identity.
For one directed Kneser arc occurrence `A -> B`, write the two unused
coordinates as `x,y`.  After orientation is forgotten, it contributes to the
four indexed summands belonging to

\[
A\cup\{x\},\ A\cup\{y\},\ B\cup\{x\},\ B\cup\{y\},
\]

which represent two complementary pairs and hence two distinct canonical
bicliques.  Since the sum is indexed by all middle sets `P`, each biclique is
indexed from both sides.  The arc therefore contributes four to the sum of
`t_C`.  This proves the second identity.
Equations (2.9)--(2.10) now follow from `W-N=K`.  QED.

The average value of `t_C(P)` is

\[
 \frac{4N}{W}=4-\frac{4}{m+1}.                             \tag{2.11}
\]

Thus the desired upper bound `t_C(P)<=4` is not a loose pseudorandom
condition: it is an almost-everywhere equality condition with total Catalan
defect only `4K`.

## 3. Exact projected-cycle criterion

The cut condition controls degrees but not cycles.  A projected cycle also
has a direct description in the Kneser successor word.

### Proposition 4 (cycle certificate)

The projected Johnson graph contains the cycle

\[
 P_0P_1\cdots P_{q-1}P_0                                  \tag{3.1}
\]

if and only if the directed cycle cover contains, for every cyclic `i`, the
arc

\[
 (P_i\cap P_{i+1})
 \longrightarrow
 \Omega\setminus(P_i\cup P_{i+1}).                         \tag{3.2}
\]

#### Proof

For a Johnson edge `P_i P_(i+1)`, its lower colour is the intersection in
(3.2) and its upper colour is the union.  Under successor projection, an arc
`A -> B` has lower colour `A` and upper colour `Omega minus B`.  Equating
these two colours gives exactly (3.2).  QED.

Accordingly, acyclicity is a pattern-avoidance condition on the directed
Kneser successor arcs, independent of the four-crossing inequalities.

## 3A. The symmetric fractional point already satisfies every global bound

The preceding conditions may look overdetermined.  Fractionally, however,
they are perfectly compatible.

Let `H_m` be the bipartite inclusion graph between ranks `m-1` and `m+1`.
Its edges are the intervals `(S,U)` with `S subset U`; every such interval
is also one edge of `J(2m,m)`.  Put

\[
 D=\binom{m+1}{2}=\frac{m(m+1)}2.                         \tag{3.3}
\]

Every lower or upper vertex of `H_m` has degree `D`.

### Theorem 4A (common fractional feasibility)

Assign weight

\[
 x_e=\frac1D                                                \tag{3.4}
\]

to every edge `e` of `H_m`, equivalently to every edge of `J(2m,m)`.  Then:

1. every rank-`m-1` and rank-`m+1` colour has total incident weight one;
2. every middle vertex has weighted degree

   \[
    \frac{2m}{m+1}<2;                                      \tag{3.5}
   \]

3. for every nonempty family `X subseteq mathcal M`,

   \[
    x(E_J(X))\le |X|-1.                                    \tag{3.6}
   \]

Thus the same symmetric point lies simultaneously in the bipartite perfect
matching polytope, the relaxation defined by all middle-vertex degree-two
inequalities, and the graphic forest polytope of the Johnson graph.  Here
"degree-two relaxation" means only the displayed linear inequalities; no
claim about the convex hull of all maximum-degree-two subgraphs is needed.

#### Proof

The first assertion follows from `D`-regularity.  A fixed middle set `P` is
an intermediate set of precisely the `m^2` intervals

\[
 (P\setminus\{a\},\ P\cup\{b\}),\qquad a\in P, b\notin P.
\]

Its weighted degree is therefore `m^2/D=2m/(m+1)`.

For (3.6), write `s=|X|`.  The Johnson graph has maximum degree `m^2`.  If
`s>=m+1`, then

\[
 \frac{|E_J(X)|}{D}
 \le \frac{m^2s/2}{m(m+1)/2}
 =\frac{m}{m+1}s\le s-1.                                  \tag{3.7}
\]

If `s<=m+1`, the elementary bound `|E_J(X)|<=binom{s}{2}` gives

\[
 \frac{|E_J(X)|}{D}
 \le\frac{s(s-1)}{m(m+1)}\le s-1.                         \tag{3.8}
\]

These are exactly the rank inequalities for the graphic forest polytope.
QED.

Consequently there is no fractional density obstruction to the Catalan
linearization problem.  An integral point in this intersection would be a
perfect colour matching whose projected graph is an acyclic graph of maximum
degree two, hence exactly the desired `K`-component linear forest.  The
missing mathematics is an integrality or rounding theorem for this highly
symmetric intersection; none of the three constituent systems alone is the
problem.

There is an equivalent factorization target which may be more constructive.
For `P in mathcal M`, let

\[
 \mathcal Q(P)=
 \{(P\setminus\{a\},P\cup\{b\}):a\in P, b\notin P\}.
                                                                    \tag{3.9}
\]

This is a canonical `K_(m,m)` inside the inclusion graph `H_m`; its edges
are exactly the Johnson edges incident with `P`.

### Proposition 4B (equitable one-factorization reformulation)

The following are equivalent.

1. The full edge set of `H_m` can be decomposed into `D` perfect matchings,
   each of whose Johnson projections has maximum degree at most two.
2. `H_m` has a proper `D`-edge-colouring `chi` such that

   \[
    |\chi^{-1}(c)\cap\mathcal Q(P)|\le2                  \tag{3.10}
   \]

   for every middle set `P` and every colour `c`.

#### Proof

Since `H_m` is `D`-regular and bipartite, every proper `D`-edge-colouring
has each colour exactly once at every lower and upper vertex.  Its colour
classes are therefore perfect matchings.  Formula (3.9) says that the number
of colour-`c` edges in `mathcal Q(P)` is exactly the degree of `P` in the
projection of that matching.  This proves both directions.  QED.

Kőnig's line-colouring theorem supplies an ordinary `D`-edge-colouring of
`H_m`; what is missing is the simultaneous balance (3.10).  It is the
sharp integral analogue of Theorem 4A: each `mathcal Q(P)` has `m^2` edges,
so its average load per colour is

\[
 \frac{m^2}{D}=\frac{2m}{m+1}<2.                          \tag{3.11}
\]

Moreover, every edge of `H_m` belongs to exactly two of the systems
`mathcal Q(P)`, namely its two intermediate middle sets.  Thus the first
global target can be stated as a frequency-two equitable one-factorization
problem.  If it is solved, all `D` colour classes simultaneously clear the
maximum-degree obstruction; one must then eliminate projected cycle
components, for example by colour-preserving alternating exchanges.  This
separates the balancing problem from the later acyclicity problem.  In fact,
if one projected colour class has `p` path components (isolated vertices
included as length-zero paths) and any number of cycle components, then its
edge count gives

\[
 p=W-N=K.                                                   \tag{3.12}
\]

Thus the Catalan number of path components is automatic as soon as the
degree bound is achieved; only the cycle components remain extraneous.

## 4. A symbolic block obstruction

The canonical bicliques expose a broad class of Hamilton constructions that
cannot work.

### Theorem 5 (biclique-block obstruction)

Suppose an oriented Hamilton cycle `C` contains, as one contiguous segment,
a spanning alternating path through `s` vertices on each side of a canonical
biclique `mathcal K(P)`.  Then

\[
 \max\{d_C(P),d_C(P^c)\}\ge s,
 \qquad
 \min\{d_C(P),d_C(P^c)\}\ge s-1.                          \tag{4.1}
\]

in some order.  In particular, if `s>=3`, the successor projection does not
have maximum degree two.

#### Proof

The segment has `2s-1` internal edges.  Along its orientation, the edge
directions across the bipartition alternate.  One direction occurs `s`
times and the other `s-1` times.  Theorem 2 identifies these counts as
contributions to `d_C(P)` and `d_C(P^c)`, respectively.  Any other cycle
edges can only increase those degrees.  QED.

Thus a successful Kneser cycle must be **dispersed** with respect to every
canonical facet biclique.  Traversing one such biclique efficiently as a
block is fatal for the projection.

### Corollary 5A (boundary cost of dispersion)

If the successor projection has maximum degree two, then for every canonical
biclique `mathcal K(P)` at least

\[
 4m-8                                                        \tag{4.2}
\]

Hamilton-cycle edges have exactly one endpoint in
`mathcal F(P) union mathcal F(P^c)`.

Indeed, the `2m` vertices have total cycle degree `4m`.  The `t_C(P)<=4`
internal cycle edges consume at most eight degree incidences, leaving at
least `4m-8` boundary incidences, one per leaving edge.

Thus refining a block construction is not a constant-size seam repair.  A
good cycle must shatter every canonical `K_(m,m)` block at linearly many
places.

## 5. Audit of Johnson's inductive construction

J. Robert Johnson's published induction is [*An Inductive Construction for
Hamilton Cycles in Kneser Graphs*](https://doi.org/10.37236/676).  Specialize
its notation to the target graph

\[
 K(2m,m-1).                                                  \tag{5.1}
\]

The construction partitions `Omega` into `m` fixed pairs.  Its initial
stratum `K_0` consists of the `(m-1)`-sets that choose one element from
`m-1` pairs and leave one pair empty.

For a sign vector `v`, let `P_v` be the middle transversal that chooses from
every fixed pair the element prescribed by `v`.  The `(L,R)` block in
Johnson's Lemma 1 is exactly

\[
 L_v=\mathcal F(P_v),\qquad R_v=\mathcal F(P_v^c).          \tag{5.2}
\]

When `r=m-1` is odd (equivalently, `m` is even), these are full canonical
`K_{m,m}` blocks.  When `r` is even, Johnson uses `H'` blocks obtained by
deleting at most one vertex from each side and performs an additional family
of exceptional vertex-pair insertions.  The clean protected-block conclusion
below is made only in the odd-`r` case.

Johnson's Lemma 5 constructs the initial cycle by traversing every `(L,R)`
block as a spanning alternating path.  More importantly, the proof chooses a
first block whose internal path is protected: the designated edges used to
insert the next family of cycles are chosen outside that block.  At later
induction stages the new designated edges lie in the cycles inserted at the
previous stage.  Therefore no later splice deletes an edge of the protected
first block.

### Theorem 6 (an infinite Johnson obstruction family)

For every even `m>=4`, the Hamilton cycle produced by the protected-block
version of Johnson's induction for `K(2m,m-1)` has

\[
 \max_{P\in\mathcal M}d_C(P)\ge m>2.                       \tag{5.3}
\]

#### Proof

Here `r=m-1` is odd, so the protected first block is the full canonical
`K_(m,m)`.  Johnson's designated first-stage insertion edges are explicitly
chosen outside this block.  The designated edges for every later stage lie
inside cycles added at the preceding stage, so the block's spanning
alternating path survives.  Apply Theorem 5 with `s=m`.  QED.

This is a symbolic obstruction to the construction as written, not a claim
that every Hamilton cycle in the Kneser graph is bad.  It also identifies the
precise conflict: Johnson's proof gains Hamiltonicity by keeping long
complete-bipartite blocks intact, whereas Catalan projection requires at most
four edges from every such block.

For odd `m`, the exceptional `H'` insertion prevents the same protected-block
claim from being read off without further analysis; no assertion is made for
that parity.  One could attempt to redesign all block traversals and all
splice locations in either parity, but that would be a new theorem.  The
connector invariants tracked in Johnson's paper do not imply the
four-crossing condition.

## 6. Audit of the modern Kneser and middle-level constructions

The general Hamiltonicity theorem of Merino, Mütze, and Namrata is
[*Kneser graphs are Hamiltonian*](https://arxiv.org/abs/2212.03918).  Its new
glider construction applies when `n>=2k+3`.  The paper explicitly treats
`n=2k+1` by the earlier odd-graph/middle-level construction and obtains
`n=2k+2` from Johnson's induction.

Our graph has

\[
 n=2m=2(m-1)+2,                                             \tag{6.1}
\]

so it is exactly the boundary case not handled by the glider construction.
Consequently the modern all-Kneser theorem supplies existence of a Hamilton
cycle here, but its proof routes this case through Johnson's construction.
For every even `m>=4`, the standard protected-block realization is provably
overloaded by Theorem 6; in the other parity, the published invariants still
do not furnish the four-crossing property.

The odd-graph and middle-level Hamilton cycles are crucial inputs to that
induction, but ordinary Hamiltonicity of the input controls neither the
canonical cut counts (2.3) nor their directional balance.  The Johnson lift
then creates the long protected biclique block.  Therefore none of these
published constructions, without a new refinement, proves the desired
projection property.

This conclusion is deliberately limited:

* it does not say that their cycles cannot be modified;
* it does not say that some other Kneser Hamilton cycle fails; and
* it does not disprove the Catalan linearization lemma, which allows an
  arbitrary cycle cover rather than a single Hamilton cycle.

## 7. Exact Kneser-cycle target

The Hamilton-cycle version of the missing theorem is now precise.

### Dispersed Kneser projection lemma (open)

For every `m`, there is an oriented Hamilton cycle `C` in `K(2m,m-1)` such
that:

1. every canonical facet biclique satisfies the directed two-by-two bound
   (2.6); and
2. the forbidden projected-cycle pattern (3.2) never occurs.

These conditions say exactly that the successor projection is an acyclic
graph of maximum degree at most two.  It then has exactly `K=Cat_m` path
components by the edge count `N=W-K`.

For the OR-array program one needs one further endpoint condition: those
`K` paths must be orientable and orderable so that `K-1` Johnson bridge edges
join them into one Hamilton path.

The Hamilton-cycle target is stronger than necessary.  By Proposition 1, the
original Catalan matching problem only asks for a directed cycle cover of the
Kneser graph with the same projection properties.  Relaxing one Hamilton
cycle to many disjointness cycles may be essential.

What is proved here is the exact projection criterion, its sharp global
budget, the cycle-pattern criterion, and a symbolic failure of the standard
inductive construction.  No dispersed Kneser projection lemma is claimed.
