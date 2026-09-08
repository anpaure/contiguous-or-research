# Fresh Johnson paths pack all but `O(M/d)` lower vertices

**Date:** 2026-08-05  
**Method:** the exact Johnson spectrum, greedy fresh-label extension,
all-order orbit counting, and the product-residual overlap polynomial; no
computation or search  
**Status:** unconditional first-stage integral rounding in the central
range.  A maximal packing of fresh `d`-vertex lower Johnson paths leaves at
most `30M/d` lower vertices.  The complete fresh-path hypergraph also has
normalized `j`-codegrees at most `(C d/k^2)^(j-1)`, and its product residuals
remain degree-concentrated down to density `1/d`.  This closes the lower
block-partition row of the connected `2/3` macro-factor programme.  It does
not select pairwise disjoint owner bundles above those blocks.

## 1. Fresh lower paths

Let

\[
                         \mathcal L={ [k]\choose t},
 \qquad M=|\mathcal L|,                                      \tag{1.1}
\]

and assume

\[
 {k\over3}\le t\le {k\over2},\qquad d^2\le k,
 \qquad d\longrightarrow\infty,qquad d=o(k).                \tag{1.2}
\]

These inequalities hold for all sufficiently large optimal central
parameters with `t=r-d`.

A **fresh `d`-path** is a sequence of `d` rank-`t` sets

\[
                         S_0,S_1,\ldots,S_{d-1}                \tag{1.3}
\]

such that

\[
                         S_j=S_{j-1}-a_j+b_j                  \tag{1.4}
\]

and all `2(d-1)` event labels

\[
                         a_1,b_1,\ldots,a_{d-1},b_{d-1}       \tag{1.5}
\]

are distinct.  Equivalently, every deletion belongs to `S_0`, every
insertion lies outside `S_0`, and no label is reused.  Such a path is the
common lower block in the punctured duplicate lift.

Let \(\mathcal H_{k,t,d}\) be the `d`-uniform hypergraph on
\(\mathcal L\) whose edges are the vertex sets of fresh `d`-paths.

## 2. A spectral fresh-path lemma

The Johnson graph `J(k,t)` has degree

\[
                         D_0=t(k-t)                             \tag{2.1}
\]

and least eigenvalue `-t`.  Indeed its eigenvalues are

\[
                         (t-i)(k-t-i)-i,
 \qquad 0\le i\le t,                                         \tag{2.2}
\]

and the last one is `-t` when `t<=k/2`.

### Lemma 2.1 (dense sets contain a fresh path)

If \(X\subseteq\mathcal L\) and

\[
                         |X|\ge {30M\over d},                  \tag{2.3}
\]

then the subgraph `J(k,t)[X]` contains a fresh `d`-path.

#### Proof

Put \(\alpha=|X|/M\).  The least-eigenvalue bound applied to the indicator
of `X` gives

\[
 {2e(X)\over|X|}
   \ge D_0\alpha-t(1-\alpha)
   \ge {D_0 30\over d}-t.                                    \tag{2.4}
\]

By (1.2), `D_0>=k^2/6` and `t<=k/2`.  Hence the average degree in the
induced graph is at least

\[
                         {5k^2\over d}-{k\over2}.              \tag{2.5}
\]

Every graph of average degree `q` contains a nonempty subgraph of minimum
degree at least `q/2`: repeatedly delete a vertex of degree below `q/2`;
deleting every vertex would remove fewer than all original edges.  We
therefore obtain an induced subgraph `G` of minimum degree at least

\[
                         {5k^2\over2d}-{k\over4}>dk,           \tag{2.6}
\]

where the last inequality uses `d^2<=k`.

Start at any vertex of `G`.  Suppose a fresh path of `j+1<d` vertices has
already been chosen.  At most `j` insertion labels and `j` deletion labels
have been used.  A Johnson neighbour is forbidden only if it deletes one
of the used insertion labels or inserts one of the used deletion labels.
There are at most

\[
                         j(k-t)+jt\le jk<dk                    \tag{2.7}
\]

such neighbours.  Inequality (2.6) therefore leaves an allowed neighbour
inside `G`.  Iterating constructs (1.3)--(1.5).  Because no event label is
reused, the path is geodesic from its initial state and cannot revisit a
vertex. \(\square\)

### Theorem 2.2 (integral fresh-block packing)

The rank-`t` layer has a family of pairwise vertex-disjoint fresh `d`-paths
covering all but fewer than

\[
                         {30M\over d}                           \tag{2.8}
\]

vertices.

#### Proof

Take a maximal family of pairwise disjoint fresh paths.  Its uncovered set
contains no edge of \(\mathcal H_{k,t,d}\).  Lemma 2.1 bounds that set by
(2.8). \(\square\)

Thus the lower-layer block partition needed by the punctured `h`-fold lift
exists with exactly the permitted `O(M/d)=O(W/d)` separator leave.  No
generic growing-uniformity matching theorem is used.

## 3. Exact degree of the labelled fresh-path orbit

For residual calculations it is convenient to retain path orientation and
roles.  Let \(\widetilde{\mathcal H}_{k,t,d}\) be the labelled
multihypergraph of all oriented fresh paths (1.3).  A fixed lower vertex
may occupy any one of the `d` roles.

### Lemma 3.1 (regular degree)

Every lower vertex has labelled degree

\[
                         D=d(t)_{d-1}(k-t)_{d-1},               \tag{3.1}
\]

where \((x)_q=x(x-1)\cdots(x-q+1)\).

#### Proof

Fix the vertex at role `a`.  Across the whole path, the event labels lying
inside the fixed set consist of the `a` earlier insertion labels and the
`d-1-a` later deletion labels.  Choose and order these disjoint roles in
`(t)_(d-1)` ways.  The `a` earlier deletion labels and `d-1-a` later
insertion labels similarly use `(k-t)_(d-1)` ordered choices outside the
fixed set.  These data reconstruct one path, and there are `d` choices of
`a`. \(\square\)

## 4. All-order normalized codegrees

For \(j\ge2\), let \(\Delta_j\) be the largest labelled codegree of `j`
distinct lower vertices in \(\widetilde{\mathcal H}_{k,t,d}\).

### Theorem 4.1 (power-decaying lower codegrees)

There is an absolute constant `C` such that, uniformly for
`2<=j<=d`,

\[
 \boxed{
 {\Delta_j\over D}
       \le\left({C d\over k^2}\right)^{j-1}.}                 \tag{4.1}
\]

#### Proof

Fix one prescribed vertex and one of its possible roles.  Assign the other
`j-1` prescribed vertices to distinct roles; there are at most `d^(j-1)`
assignments.  Sort the assigned roles and let

\[
                         g_1,\ldots,g_{j-1}\ge1                \tag{4.2}
\]

be their successive gaps.  Put `s=sum g_i`, so `s>=j-1`.

For a compatible prescribed tuple, crossing a gap `g_i` fixes the unordered
set of `g_i` deleted labels and the unordered set of `g_i` inserted labels.
Their internal orders may vary in at most `(g_i!)^2` ways.  Conditional on
the first prescribed state, the entire span uses `s` distinct labels from
that state and `s` distinct labels from its complement.  The event labels
outside the span are free and cancel from numerator and denominator.
Therefore the probability of the prescribed states at those roles is at
most

\[
 {\prod_i(g_i!)^2
       \over (t)_s(k-t)_s}.                                   \tag{4.3}
\]

Under (1.2), both factors in the denominator are at least `(c k)^s` for an
absolute `c>0` and all sufficiently large `k`.

Since `g!<=d^(g-1)` for `1<=g<=d`, multiplying (4.3) by the role count gives

\[
 d^{j-1}{d^{2(s-j+1)}\over(c k)^{2s}}
 \le
 \left({C d\over k^2}\right)^{j-1}
 \left({C d^2\over k^2}\right)^{s-j+1}.                       \tag{4.4}
\]

The last factor is at most one for all sufficiently large `k`.  Summing
over role assignments proves (4.1). \(\square\)

For `j=2`, the adjacent-role scale in (4.1) is sharp up to constants:
conditional on one state and one role, a specified adjacent state costs
one prescribed deletion and one prescribed insertion, hence `Theta(k^-2)`;
the second state has `Theta(d)` possible relative roles.

## 5. Product residuals remain regular down to density `1/d`

Retain every lower vertex independently with probability `rho`.  Conditional
on a fixed vertex `v` being retained, let `Z_v` count labelled fresh paths
through `v` which survive completely.  Then

\[
                         \mu=E Z_v=D\rho^{d-1}.                 \tag{5.1}
\]

For two paths `E,F` through `v`, put

\[
                         m(E,F)=|(E\cap F)\setminus\{v\}|.     \tag{5.2}
\]

Define the normalized overlap kernel

\[
 \Omega_v(\rho)={1\over D^2}
   \sum_{E\ne F\ni v}(\rho^{-m(E,F)}-1).                      \tag{5.3}
\]

### Theorem 5.1 (exact residual-overlap bound)

Uniformly for `1/d<=rho<=1`,

\[
 \boxed{
 \Omega_v(\rho)
 \le
 \left(1+{C d\over k^2}(\rho^{-1}-1)\right)^{d-1}-1
 =O(1/d).}                                                     \tag{5.4}
\]

Moreover,

\[
 {Var(Z_v)\over\mu^2}\le{1\over\mu}+\Omega_v(\rho)=O(1/d),  \tag{5.5}
\]

and `mu` tends to infinity superpolynomially, even at `rho=1/d`.

#### Proof

For every `q>=1`, double count a path `E` through `v`, a `q`-subset of
`E-{v}`, and a second path `F` containing that subset.  Theorem 4.1 gives

\[
 {1\over D^2}\sum_{E,F\ni v}{m(E,F)\choose q}
 \le {d-1\choose q}\left({C d\over k^2}\right)^q.            \tag{5.6}
\]

Put `z=rho^(-1)-1`.  The binomial identity

\[
                         \rho^{-m}-1
                           =\sum_{q=1}^{m}{m\choose q}z^q       \tag{5.7}
\]

and (5.6) give the first inequality in (5.4).  Since `rho>=1/d`,

\[
 (d-1){C d\over k^2}(\rho^{-1}-1)
                         =O(d^3/k^2)=O(1/d),                   \tag{5.8}
\]

using `d^2<=k`.  This proves the last equality in (5.4).

Writing `Z_v` as a sum of surviving-path indicators gives

\[
 {Var(Z_v)\over\mu^2}\le{1\over\mu}+\Omega_v(\rho),          \tag{5.9}
\]

by direct covariance expansion.  Finally, (1.2) and (3.1) give at
`rho=1/d`

\[
 \mu\ge d(c k)^{2d-2}d^{-(d-1)},                              \tag{5.10}
\]

which tends to infinity faster than every power of `k`. \(\square\)

The standard Janson lower-tail inequality, applied to the surviving-path
indicators, also gives for every fixed `0<epsilon<1`

\[
 P(Z_v<(1-\epsilon)\mu)\le\exp(-c_\epsilon d).                \tag{5.11}
\]

Indeed its denominator is `mu+mu^2 Omega_v(rho)`, and (5.4)--(5.10) give
an exponent of order `d`.  Thus a product residual has only
`exp(-Omega(d))M=o(M/d)` low-degree vertices in expectation.

## 6. What this closes and what remains

Theorem 2.2 is the promised first integral stage of the connected `2/3`
macro-factor theorem:

* all but `O(M/d)` lower vertices are partitioned into literal fresh
  depth-sized blocks;
* the uncovered vertices fit in the already budgeted `O(W/d)` separator
  bank; and
* every packed block has the explicit `h=2,3` owner-disjoint local lifts.

Theorem 5.1 also proves that independent product residuals have exactly the
degree regeneration required at density `1/d`.  It does **not** prove that
the residual left by an actual sequence of matching bites is product-like.
The existing growing-uniformity audit therefore remains binding; (5.4) is
an input to a bespoke nibble, not permission to invoke a fixed-rank theorem.

The exact remaining integral statement is now an owner-bundle rainbow
matching:

> Given the fresh block packing of Theorem 2.2, choose for every packed
> block two or three punctured FIFO lifts so that all selected rank-`r`
> owners are distinct, all but `O(W/d)` owners are used, and the resulting
> macro component graph is connected.

Terminal permutations would then merge the cover into one cycle.  The
payload target atlas remains downstream and owner-invisible.

## 7. Dependencies

The local punctured lifts, terminal switches, and exact macro factor are in

`MATH_THEOREM_FRESH_FIFO_BLOCK_CHAIN_KERNEL_AND_PAYLOAD_ATLAS_GATE_20260805.md`.

The warning against fixed-uniformity diagonalization is in

`MATH_AUDIT_MACROSCOPIC_COLLAR_GROWING_UNIFORMITY_MATCHING_THEOREMS_20260803.md`.
