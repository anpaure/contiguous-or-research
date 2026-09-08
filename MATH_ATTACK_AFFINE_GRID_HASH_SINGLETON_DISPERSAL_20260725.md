# Affine grid hashes and the singleton-dispersal gate

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

For a coordinate hash \(h:[2m]\to\mathbb F_p\), extend it additively to
Boolean targets by

\[
 H(S)=\sum_{x\in S}h(x).                              \tag{0.1}
\]

On a geodesic grid

\[
 G_{i,j}=C\cup\{a_{i+1},\ldots,a_g\}
             \cup\{b_1,\ldots,b_j\},                 \tag{0.2}
\]

one has the exact identity

\[
 H(G_{i,j})=H(C)+\sum_{r>i}h(a_r)+\sum_{r\le j}h(b_r). \tag{0.3}
\]

The proposed low-entropy affine schedule works perfectly **inside one
fixed global hash**.  Choose a prime \(p>2g+2Q\), and choose
\(\gamma\in\mathbb F_p\) with

\[
 \gamma\notin\{-Q,-Q+1,\ldots,Q\}.                  \tag{0.4}
\]

Restrict the ordered grid coordinates by

\[
 h(a_r)=r,\qquad h(b_r)=r+\gamma\quad(1\le r\le g). \tag{0.5}
\]

Then every protected diagonal row is simultaneously injective:

\[
 \boxed{
 H(G_{t+q,t})=A_q+t(\gamma-q),\qquad
 H(G_{t-q,t})=B_q+t(\gamma+q).}                      \tag{0.6}
\]

Thus the independent-row cost \(e^{-\Theta(gQ)}\) is spurious.  Only the
\(2g\) coordinate-class prescriptions (0.5) are needed, and the retained
ordered-coordinate entropy is at least

\[
 \exp\!\left((2+o(1))g\log{m\over g}\right).         \tag{0.7}
\]

There are, however, two exact limitations.

1. If \(h\) is chosen separately for every grid, the same physical target
   receives different hash values in different grids.  Then (0.6) has no
   cross-grid consequence at all.
2. With one fixed balanced \(h\), (0.6) makes the support hypergraph
   \((2Q+1)p\)-partite, with every strip rainbow inside every tagged rank.
   This does **not** rule out a projective-plane-type singleton system.
   A projective plane truncated at one point is an \(r\)-partite linear
   intersecting non-star with \((r-1)^2\) edges.  Thus multipartiteness
   still permits the sharp quadratic scale \(\Theta(K^2)\).

Consequently the affine hash is a genuine entropy-saving and a useful
catalogue normal form, but it does not improve the decisive bound from

\[
 |{\cal F}|\le K^2-K+1=o(D)                           \tag{0.8}
\]

proved in
`MATH_ATTACK_FIRST_ORDER_PROTECTED_STRIP_INTERSECTING_EXPANSION_20260725.md`.
It independently confirms that singleton line systems are below the
near-\(D\) colour scale.  A stronger conclusion would require either
simultaneous balance for a fixed hash and every target histogram, or a
second algebraic constraint which excludes truncated affine planes; the
single cumulative hash does neither.

## 1. Exact affine-row calculation

Put

\[
 L_q(t)=G_{t+q,t},\qquad U_q(t)=G_{t-q,t}.             \tag{1.1}
\]

From (0.3),

\[
 \begin{aligned}
 H(L_q(t+1))-H(L_q(t))
 &=-h(a_{t+q+1})+h(b_{t+1}),\\
 H(U_q(t+1))-H(U_q(t))
 &=-h(a_{t-q+1})+h(b_{t+1}).                         \tag{1.2}
 \end{aligned}
\]

Substituting (0.5) gives

\[
 H(L_q(t+1))-H(L_q(t))=\gamma-q,\qquad
 H(U_q(t+1))-H(U_q(t))=\gamma+q.                     \tag{1.3}
\]

This proves (0.6), including the owner row \(q=0\).

### Proposition 1.1 (simultaneous injectivity)

Every map

\[
 t\longmapsto H(L_q(t)),\qquad
 t\longmapsto H(U_q(t))                               \tag{1.4}
\]

is injective on every phase interval of length at most \(g\),
simultaneously for \(0\le q\le Q\).

#### Proof

By (0.4), every step \(\gamma\pm q\) is nonzero in \(\mathbb F_p\).
If two phases at distance \(1\le d<g<p\) had equal hash, then

\[
 d(\gamma\pm q)=0\quad\hbox{in }\mathbb F_p.
\]

Since \(p\) is prime and both factors are nonzero, this is impossible.
\(\square\)

The construction is stronger than pairwise independent row hashing: all
\(2Q+1\) row events are forced by the two affine coordinate schedules.
The number of algebraic equations is \(2g\), not \(\Theta(gQ)\).

## 2. Entropy retained by a balanced fixed hash

Take \(p=\Theta(g)\), as permitted by Bertrand's postulate, and choose a
balanced map \(h:[2m]\to\mathbb F_p\), so every fibre has size

\[
 n_z\in\{\lfloor2m/p\rfloor,\lceil2m/p\rceil\}.
 \tag{2.1}
\]

The requirements (0.5) use any one hash fibre at most twice.  Since

\[
 \min_zn_z=(2+o(1)){m\over p}\to\infty,              \tag{2.2}
\]

the number of choices of the ordered \(a\)- and \(b\)-coordinates is at
least

\[
 \prod_{r=1}^g(n_r-2)(n_{r+\gamma}-2)
 \ge\left((1-o(1)){2m\over p}\right)^{2g}.           \tag{2.3}
\]

Taking logarithms and \(p=\Theta(g)\) proves (0.7).  The remaining core,
carrier-reservoir, and outside coordinates supply additional entropy, so
(0.7) is only a lower bound.

For a fixed carrier \(U\), (2.3) requires enough members of \(U\) in the
needed hash fibres.  A uniformly random carrier has this property with
probability \(1-e^{-\Omega(m/g)}\) by hypergeometric concentration.  Thus
only a negligible fraction of carriers is empty for the affine schedule.
Their degrees are not exactly equal, however; this is part of the global
regularity issue in Section 4.

## 3. The exact multipartite consequence

Partition the protected target vertices by

\[
 V_{d,z}=\{S:|S|=m+d,\ H(S)=z\},
 \qquad -Q\le d\le Q,\ z\in\mathbb F_p.              \tag{3.1}
\]

Proposition 1.1 says that an affine-scheduled strip contains at most one
target in each \(V_{d,z}\).  Hence:

### Theorem 3.1 (rainbow partite form)

The affine-scheduled protected support hypergraph is

\[
 \boxed{R=(2Q+1)p=O(gQ)=O(K)}                         \tag{3.2}
\]

partite, and every edge is rainbow in the parts belonging to each fixed
rank.

This conclusion is global only because the same \(h\) is used for every
edge.  If each grid chooses its own affine hash, (3.1) is not a partition
of physical target vertices and Theorem 3.1 disappears.

## 4. Why the partite theorem does not remove affine planes

Let \(\Pi\) be a projective plane of order \(q\), fix a point \(x\), and
let

\[
 L_1,\ldots,L_{q+1}                                  \tag{4.1}
\]

be the lines through \(x\).  Use the \(q+1\) sets

\[
 V_i=L_i\setminus\{x\}                               \tag{4.2}
\]

as vertex parts.  Take as hyperedges all lines not containing \(x\).
Every such line meets every \(V_i\) exactly once.  Two such lines meet in
one point, and there is no point common to all of them.  Their number is

\[
 q^2=(r-1)^2,\qquad r=q+1.                           \tag{4.3}
\]

Thus this is an \(r\)-partite, \(r\)-uniform, linear intersecting
non-star.  It obeys precisely the rainbow conclusion of Theorem 3.1 and
still has quadratic size.

The additional fact that each rank-row hash set is an arithmetic
progression does not, by itself, change this conclusion.  It constrains
the **parts used by one edge**, but not the identities of the physical
targets inside those parts.  A truncated plane is already a transversal
design, and its point fibres may be assigned inside any prescribed list of
distinct parts unless a second compatibility condition couples different
edges.  Formula (0.6) supplies no such cross-edge coupling.

In particular, an assertion that the affine schedule alone rules out
projective planes would again multiply two marginals: row-rainbowness of
each strip and pairwise physical intersection of different strips.  No
proved correlation connects them.

## 5. Fixed-hash regularity is the remaining algebraic gate

The full coordinate orbit is target-regular because the symmetric group is
transitive on every Boolean rank.  A fixed nonconstant \(h\) breaks that
transitivity.  The stabilizer of \(h\) preserves the complete histogram

\[
 \bigl(|S\cap h^{-1}(z)|:z\in\mathbb F_p\bigr),       \tag{5.1}
\]

not merely \((|S|,H(S))\).  Consequently two targets in the same part
\(V_{d,z}\) can have different affine-catalogue degrees.

Averaging over all coordinate permutations of \(h\) restores the exact
rank marginals, but it also makes the hash edge-dependent; then the common
partition (3.1) is lost.  This is the noncommutation

\[
 \boxed{
 \begin{array}{c}
 \text{fixed hash}\ \Longrightarrow\ \text{global parts but nonuniform target histograms},\\
 \text{symmetrized hashes}\ \Longrightarrow\ \text{uniform targets but no global parts}.
 \end{array}}                                        \tag{5.2}
\]

Therefore a useful algebraic strengthening would have to prove one of the
following genuinely joint statements.

1. **Fixed-hash balancing.**  Thin the affine catalogue so that all but an
   \(o(W)\) target ledger have comparable degrees simultaneously across
   the histogram classes (5.1), while retaining the global parts.
2. **Two-hash dispersal.**  Construct two fixed hashes whose joint affine
   schedules retain enormous degrees and prove that no truncated-plane
   transversal design is physically realizable in both hash partitions.
3. **Additive intersection energy.**  Bound, for every family of strips,
   the number of physical singleton intersections in terms of additive
   energy of their row offsets in (0.6), rather than merely observing that
   every row is injective.

None of these follows from (0.6).  The exact result of the present line is
therefore: simultaneous row injectivity at \(O(g)\) entropy cost is proved;
a projective-plane exclusion or near-\(D\) colouring theorem is not.
