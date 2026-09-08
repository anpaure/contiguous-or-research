# Independent finite audit of the Catalan colour-incidence graph

Date: 2026-07-31  
Status: solver-free general graph lemmas and complete finite audits for the
listed \(m=3\) fibres and the frozen GMM \(m=4\) cycle; no all-\(m\)
existence claim

## 1. Setup

Let \(P\) be an oriented Hamilton cycle on \(\binom{[2m]}m\). For a
physical Johnson edge \(e=AB\), put

\[
                 \ell(e)=A\cap B,\qquad u(e)=A\cup B.
\]

The bipartite colour-incidence multigraph \(G(P)\) has left shore
\(\binom{[2m]}{m+1}\), right shore \(\binom{[2m]}{m-1}\), and one
occurrence-labelled graph edge for every physical edge of \(P\), joining
\(u(e)\) to \(\ell(e)\). The occurrence label matters if an abstract
version permits parallel physical edges.

For a Catalan cap-two lift, an unmatched upper block \(U_i\) contains the
sole edge \(C_iC_{i+1}\). If omitted facet \(X\) is hosted there, its two
edges are

\[
       e_i^- = C_iX \quad\hbox{(incoming)},\qquad
       e_i^+ = XC_{i+1}\quad\hbox{(outgoing)}.
\]

Every upper-colour vertex of \(G(P)\) therefore has degree one or two, with
profile \(1^{N-K}2^K\).

## 2. The exact graph theorem

### Theorem 2.1 (common transversal)

A set \(T\subseteq E(P)\) contains exactly one edge of every upper colour
and exactly one edge of every lower colour if and only if the corresponding
occurrence-labelled edges form a perfect matching of \(G(P)\).

This is immediate from the definition, but it fixes the physical
quantifier: a matching edge is one edge occurrence of \(P\), not merely an
abstract compatible pair of colours.

### Theorem 2.2 (degree-two forest/cycle criterion)

Suppose every vertex of \(G(P)\) has degree at most two. Then \(G(P)\) has
a perfect matching if and only if every path component is balanced between
the two shores. A balanced path has one perfect matching. An even cycle has
two. Hence, if all path components are balanced and there are \(c\) cycle
components, the total number of perfect matchings is \(2^c\); it is unique
exactly when \(G(P)\) is a balanced spanning path forest.

#### Proof

A degree-two bipartite multigraph is a disjoint union of paths and even
cycles, including a two-edge parallel cycle. Peeling an endpoint forces
alternating edges along a path. The peel covers the other endpoint exactly
when the endpoints lie on opposite shores, equivalently when the path is
balanced. A cycle has its two alternating states. Components are
independent. \(\square\)

There is a determinant refinement. After independent row and column
permutations, a balanced path block is triangular with determinant
\(\pm1\). A cycle of length \(2r\) has bipartite incidence block
\(I+P_r\), up to permutations, and therefore

\[
                 |\det(I+P_r)|=|1-(-1)^r|.
\]

Consequently a balanced forest has determinant \(\pm1\). More generally,
the determinant is nonzero exactly when every cycle has odd half-length;
then its absolute value is \(2^c\). A cycle with even half-length has two
matchings of opposite sign and cancels in the determinant.

## 3. Uniform orientation versus distinct cut seams

If \(T\) is a common transversal, it chooses one of \(e_i^-,e_i^+\) in
every hosted block. Selecting \(e_i^+\) cuts seam endpoint \(C_i\), while
selecting \(e_i^-\) cuts \(C_{i+1}\). Because all \(C_j\) are distinct,
two cut labels coincide if and only if, for some consecutive hosted blocks
\(i,i+1\), the selected orientations are

\[
                       e_i^-,e_{i+1}^+ .                 \tag{3.1}
\]

Thus the exact cut-injectivity criterion is absence of the cyclic local
word `incoming,outgoing` on consecutive hosted blocks. All-outgoing and
all-incoming are sufficient. Neither is necessary.

The frozen mixed \(m=3\) fixture is a literal counterexample to necessity.
Its unique orientation is

\[
 (4,+),(6,+),(8,-),(10,-),(13,-),
\]

where \(+\) denotes outgoing. Its cut labels are
\(38,19,26,56,28\), all distinct. Hence distinct cut seams do **not** imply
uniform outgoing orientation.

## 4. Exact diamond-tight equivalence and its qualifier

Call a three-level cyclic enumeration **block-respecting over \(P\)** when
its middle projection is \(P\) and:

1. the sole edge of every degree-one upper block receives both its lower
   intersection and its upper union, producing a diamond; and
2. in every degree-two upper block one physical edge receives only its
   lower intersection and the other receives only its upper union.

### Theorem 4.1 (block-respecting diamond equivalence)

A common transversal \(T\) of \(G(P)\) exists if and only if there is a
block-respecting \(P\)-projected tight enumeration of ranks
\(m-1,m,m+1\).

#### Proof

Given \(T\), use it as the lower distinguished-edge set. In a singleton
upper block, use its sole edge also as the upper distinguished edge. In a
double block, use the edge complementary to the unique member of \(T\) as
the upper distinguished edge. The two distinguished sets have size \(N\),
their union is all \(M=N+K\) edges, and their intersection is the \(N-K\)
singleton-block edges.

On a lower-only edge \(AB\), insert \(A\cap B\). On an upper-only edge,
insert \(A\cup B\). On a common edge, insert the literal diamond

\[
              A, A\cap B, A\cup B, B.
\]

Every lower, middle and upper set appears once. The Hamming length is

\[
       2(2K)+4(N-K)=4N,
\]

the exact three-level lower bound.

Conversely, the lower-decorated edges of a block-respecting enumeration
enumerate all lower colours once. The block rule makes them choose exactly
one edge in every upper block. They are therefore a common transversal,
hence a perfect matching of \(G(P)\). \(\square\)

The phrase “\(P\)-respecting” cannot mean only “has middle projection
\(P\).” On the positive \(m=3\) fixture there are exactly 75 tight pairs of
lower and upper edge transversals whose middle projection is \(P\), but
only one lower set is also an upper transversal. A frozen counterexample
has lower-edge loads

\[
                  (0,2,1,1,\ldots,1)
\]

on the 15 upper blocks: block 0 is upper-only, while block 1 supplies a
diamond on one edge and a second lower subdivision on the other. Its word
still has rank census \(15,20,15\) and Hamming length 60. Thus the
block-respecting qualifier is load-bearing.

## 5. Complete \(m=3\) finite results

The audit enumerates every injective host map and every one-of-two retained
orientation, without presupposing cut-label injectivity.

| fixed saturating cycle | host maps | decorated cases | common transversals | uniform outgoing | cut-distinct |
|---|---:|---:|---:|---:|---:|
| project positive | 144 | 4,608 | 1 | 1 | 1 |
| project mixed | 138 | 4,416 | 1 | 0 | 1 |
| vendored GMM SatCycle | 165 | 5,280 | 0 | 0 | 0 |

For the positive cap-two cycle, \(G(P)\) is a forest of ten balanced paths:
seven have two vertices, one has four, and two have six. Its determinant is
\(-1\), and leaf peeling gives its unique uniformly outgoing perfect
matching. The canonical diamond word has SHA
`507789d948690f2ab658825999cf210f472e86ff2830cb93c95d68833f6b1f62`,
rank census \(15,20,15\), step census \(1^{40}2^{10}\), and total Hamming
length 60.

For the mixed fixture, \(G(P)\) is again a ten-component balanced path
forest, now five two-vertex paths and five four-vertex paths. Its
determinant is \(+1\). The unique diamond word has SHA
`e2443fe640a13fb9b3b54e3776e4f78358eb4fd5ee5676f2359d6095f508cb71`
and the same exact census.

## 6. Frozen GMM \(m=4\) obstruction

The vendored GMM SatCycle output on levels 4 and 5 of \(Q_8\) has base
lower-colour profile

\[
                         0^{17}1^{22}2^{17}.
\]

A cap-two lift hosts exactly \(K=\operatorname{Cat}_4=14\) omitted facets.
Any common transversal starts from the 56 base edge occurrences and changes
only the selected edge in those 14 hosted blocks. One replacement can fill
at most one old hole. Therefore at least

\[
                              17-14=3
\]

lower colours remain missing, for **every** host injection and every local
orientation. This proves zero common transversals for this fixed GMM cycle
without a solver. It is not an obstruction to a different saturating cycle.

For an explicit degree-two calibration, the deterministic lexicographic
host injection gives lower-degree profile \(0^8 1^{26}2^{22}\). Its
\(G(P)\) has 8 isolated lower vertices and 34 path components, maximum
matching size 46, perfect-matching count zero, and determinant zero. This is
a literal demonstration that degree at most two alone is insufficient; the
balanced-path condition is exact. The hardcoded map in the primary graph
audit has genuine deterministic provenance: for every omitted facet in
increasing order, its least legal host index is still unused, so the stated
increasing-index augmenting scan makes zero displacements and returns that
map byte-for-byte.

## 7. Provenance and artifacts

The vendored-source tree SHA is
`23246c37855082200b9a705d054f6dbbdccb346baeb41c19c1439f8831967890`.
The complete alternating SatCycle outputs have SHAs

* \(m=3\): `9b23e93e658c8e35b0d98d14d2537329099770b73bd5bbfe45a27ca808e98509`;
* \(m=4\): `fde01fc13b87da9c9ba5d41f50ef5b9ca3af14cc53886d79015b5642fb045bab`.

Audit artifacts:

* `scratch/audit_catalan_colour_incidence_graph_m3_m4_20260731.py`, SHA
  `7c769fe857eeffe581ec0086e9a436c9980efd2858fc857700e7f294650beefb`;
* `scratch/catalan_colour_incidence_graph_m3_m4_20260731.audit.json`, SHA
  `60e386ac35cf24de63af0b6c73c81d924edaf02e305fcdaa349ef8a218495cf1`,
  payload
  `2dcdbb2481516a02fcce424ecac91b903be89d4876b9705c80e2ea16edacf52a`;
* `scratch/catalan_colour_incidence_graph_m3_m4_20260731.catalogue.tsv`, SHA
  `30937cb68c97f1c59760a250d96f9bdd956405651627c2f4d65793b761f5fdf6`.

The scope is source-relative and finite. No unrestricted Catalan
directed-repair theorem, and no global \(\nu(k)\) claim, follows from these
calibrations.
