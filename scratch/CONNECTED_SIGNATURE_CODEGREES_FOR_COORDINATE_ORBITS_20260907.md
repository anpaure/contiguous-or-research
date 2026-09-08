# Connected signature codegrees for coordinate-orbit hypergraphs

Date: 2026-09-07. Pure counting proof; no computation or matching theorem.

## 1. Setup

Let P be a nonempty family of b-subsets of a 2b-element ground set. The
ambient Johnson metric is d_J(X,Y)=|X minus Y|; diameter below always
refers to this metric, not to distances within an induced subgraph. Its
induced Johnson graph joins sets differing by one deletion and one
insertion. Suppose its maximum degree is at most Delta. Let H have all
b-subsets as vertices and the DISTINCT supports sigma(P), for coordinate
permutations sigma, as hyperedges. It is D-regular. Uniform permutations
induce uniform hyperedges, since every support has the same stabilizer size.

For a finite vertex family S, deg_H(S) is the number of edges containing
all its members. Fix a Johnson-connected family of distinct b-subsets

    S={S_0,...,S_(m-1)},
    d=|S_0 minus intersection S|,
    e=|union S minus S_0|.

The falling factorial (b)_j means b!/(b-j)!, with (b)_0=1.

## 2. Connected families have singleton variable signatures

The membership signature of a coordinate is its vector of membership
bits across the sets of S. Every nonconstant signature occurs at most
once. To prove this, suppose two coordinates have the same nonconstant
signature. Connectivity gives a Johnson edge of S on which that signature
changes. Both coordinates would be inserted on that edge, or both would
be deleted, contradicting the definition of a Johnson edge.

Thus the coordinate signature classes consist of d+e singleton variable
classes, a constant-in class of size b-d, and a constant-out class of
size b-e.

## 3. Exact permutation count and higher-order codegree

**Theorem.**

    deg_H(S)/D <= Delta^(m-1)/[(b)_d (b)_e].               (1)

Here deg_H(S)/D is exactly
P(S subset sigma(P) | S_0 in sigma(P)).

If m=1 the right side is one. For m>=2 choose a rooted spanning tree of
the Johnson graph on S, rooted at S_0. Conditional on a specified
template vertex X_0 mapping to S_0, each next tree vertex has at most
Delta possible template images. There are at most Delta^(m-1) candidate
ordered tuples X_0,...,X_(m-1) in P. Ignore repeated or incompatible
tuples, which cannot realize the target family.

For a compatible tuple, coordinate signature class sizes must agree.
By Section2 each variable coordinate image is forced. The constant-in
and constant-out coordinates can be bijected in exactly

    (b-d)!(b-e)!

ways. There are b!^2 coordinate permutations sending X_0 to S_0. Thus
the conditional probability for this tuple is exactly

    (b-d)!(b-e)!/b!^2 = 1/[(b)_d (b)_e].                  (2)

The events specifying which X_0 maps to S_0 partition the event that
S_0 belongs to sigma(P). Average the tuple union bound over those roles
to obtain (1). No factor |P| survives conditioning on the anchor.

For an m-vertex fresh-coordinate geodesic, d=e=m-1, so (1) specializes to

    deg_H(S)/D <= Delta^(m-1)/(b)_(m-1)^2.                (3)

### Complement-folded version

Suppose diam_J(P)<b-1 and P contains no complementary pair, so a Johnson
edge cannot connect one vertex of P with the complement of another.
Fold the ambient vertices into pairs [T]={T,T^c} and use the distinct
folded coordinate-orbit supports to form H_fold. Write D_fold for its
degree, which need not equal D. For a target family with distinct folded
vertices and coherent Johnson-connected actual representatives S_i,

    deg_(H_fold)({[S_i]})/D_fold
       <= Delta^(m-1)/[(b)_d (b)_e].

The left side is the corresponding conditional inclusion probability.
This statement does not assert that arbitrary quotient-connected target
families admit such a coherent lift.

Indeed, adjacent representatives in an embedding must have the same
choice of complement sign: differing signs give template distance b-1.
Connectivity makes that sign global. Conditioning on the anchor averages
over the two signs as well as its template role; complementation swaps
d,e and leaves (2) unchanged. The many-root grid has diameter<b/2, so it
satisfies this condition.

## 4. An edge-label multiplicity refinement

Label each edge of the induced template graph by its two changed ground
coordinates. Suppose Gamma>=1 and each coordinate labels at most Gamma template edges.
If the family S embeds in P, the m-1 edges of its spanning tree contribute
2(m-1) label incidences. Only its d+e variable coordinates can occur, each
at most Gamma times. Hence

    d+e >= 2(m-1)/Gamma.                                  (4)

Suppose also that each of d,e is at most a<b, as is true when P has a
common included set and a common excluded set each of size b-a. Then
(b)_d(b)_e >= (b-a)^(d+e), and (1) gives

    deg_H(S)/D
      <= [Delta (b-a)^(-2/Gamma)]^(m-1).                 (5)

For the grid one may take a=8Kh. Section6 proves its needed O(K) edge-label
bound separately from this general conditional lemma.

## 5. A uniform connected-overlap sum

Fix a hyperedge E and v in E. For z>=0 define

    theta=4z Delta^2 (b-a)^(-2/Gamma).

Under Section4's hypotheses, if theta<1, then

    sum_{S subset E: v in S, |S|>=2, S Johnson-connected}
      z^(|S|-1) deg_H(S)/D <= theta/(1-theta).            (6)

The number of rooted connected m-vertex sets in a graph of maximum
degree Delta is at most (4Delta)^(m-1). To see this without an external
counting theorem, give each such set a spanning tree and an ordering of
the children. Rooted plane trees with j edges have at most 4^j shapes:
their depth-first traversals are balanced parenthesis strings, a subset
of the 2^(2j) binary strings of length2j. For each shape there are at
most Delta^j neighbor choices. This overcounts and so is an upper bound.
Combine it with (5) and sum the geometric series.

## 6. Grid specialization: coordinate load, not total edge size

For the many-root four-group grid, one can take

    Delta=12, a=8Kh, Gamma=6(2K+1).                       (7)

The degree bound follows because prefix-set Johnson neighbors differ by
e_i-e_j in one of twelve ordered group pairs. There are2(2K+1) main
traces and2(2K+1) backup traces, each geodesic, so any one coordinate
labels at most4(2K+1) trace edges.

Every additional induced Johnson edge joins a main unit-neighbor and a
backup unit-neighbor of the same root. Here is the localization: in
coordinates p=(c_1+c_4-2B)/2 and q=(c_1+c_2-2B)/2, main rows have q=jh
and backup columns p=ih. A Johnson edge changes each of p,q by at most
1/2. A nonroot main point adjacent to a nonroot backup point must
therefore be one unit step from the root with those i,j. Points on
different main rows or different backup columns cannot be adjacent;
within one line, the only adjacencies are trace edges, as the two
L-shaped paths differ by at least two in Johnson distance away from
their shared ends.

At an interior root the four main and four backup unit-neighbors give
eight additional edges. They pair neighbors whose changes share either
the same inserted coordinate or the same deleted coordinate. Each of
the eight boundary coordinates (top included and next excluded in each
group) labels exactly two such edges. A boundary root only removes edges.
For a fixed ground coordinate, being top or next requires a group prefix
count equal to that coordinate's index or one less. These two levels
cannot both be root levels because h>=2. Its one possible root level
fixes i+j or i-j, giving at most2K+1 roots. Additional edge load is
therefore at most2(2K+1), proving (7).

Taking z=1/rho in (6) gives

    theta <= 576 / [rho (b-8Kh)^(1/[3(2K+1)])].           (8)

For fixed rho in (0,1), K=o(log b), and Kh=o(b), this tends to zero.
More generally it tends to zero whenever the logarithm of the denominator
in (8) exceeds log576 by a quantity tending to infinity. The connected
overlap estimate is uniform over every root and macro; it does not carry
a factor equal to the growing number of vertices in an edge.

In the folded version of Sections4-6, replace H,D everywhere by
H_fold,D_fold and use the coherent oriented lift of a fixed orbit edge
when defining connected subsets and their variable-coordinate counts.
Each folded edge has such a lift by construction; the no-cross-complement
adjacency condition makes its induced graph the same as that of P.

The grid edge-label bound was supplied independently by the long-geodesic
task and checked against the explicit root-neighbor geometry by root.

## 7. Scope

These are exact connected-family incidence bounds, independent of edge
uniformity. They are not a near-perfect matching theorem, a residual
degree-cap theorem, or a product estimate for disconnected families.
Disconnected overlaps can share coordinate constraints, and their
probabilities must not be multiplied without proof. Even a successful
central matching would still need actual off-rank coverage control.

Independent audit passed Sections2-6 after the explicit ambient-metric,
conditional-probability, and folded-degree clarifications above.
