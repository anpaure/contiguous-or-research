# Grid-square rigidity prevents a product order map into the staircase

2026-09-08. Author: direct_route. Pure analysis, no computation. Root
full-file review passed. Appendix_a independently read and passed the
mathematical argument, including the scope clarification below; that audit
did not reread the external sources. This closes a proposed product-embedding
shortcut; it does not settle the asymmetric staircase width.

Use \([n]=\{0,\ldots,n-1\}\), with the coordinatewise order. An order
map below means an injective map preserving all comparisons. Reflection
of comparisons is not required.

## 1. Rank-preserving grid maps are rigid in equal dimension

**Lemma.** Let \(a_1,\ldots,a_d\ge2\). If an injective order map
\[
           f:\prod_{i=1}^d[a_i]\longrightarrow\mathbb Z^d
\]
preserves the sum-of-coordinates rank up to a constant, then there is a
permutation \(\pi\) such that
\[
                        f(x)=f(0)+\sum_i x_i e_{\pi(i)}.           \tag{1}
\]
In particular its image is an axis-aligned rectangular box.

Every source cover \(x<x+e_i\) maps to a strict comparison whose rank
difference is one, so
\(f(x+e_i)-f(x)=e_{\lambda_i(x)}\) for some target direction. Consider
an elementary source square in directions \(i\ne j\). The two
intermediate images are distinct, so their first directions \(a,b\)
are distinct. Equality at the far corner gives
\[
                         e_a+e_c=e_b+e_e.
\]
With \(a\ne b\), the only possibility is \(c=b\) and \(e=a\).
Opposite edges of every square consequently have the same direction.

By propagating across all the other coordinates, the direction of an
\(i\)-edge depends only on its starting \(i\)-coordinate. Let \(S_i\)
be the set of target directions used by the \(i\)-edges. Each \(S_i\)
is nonempty. For any \(i\ne j\) and any choices of an \(i\)-edge
level and a \(j\)-edge level, the corresponding square exists and
forces the two directions to differ. Thus the \(d\) nonempty sets
\(S_1,\ldots,S_d\) are pairwise disjoint subsets of \(\{1,\ldots,d\}\).
Each is a singleton, and these singletons form a permutation. Integrating
the edge increments proves (1).

**Equal-height corollary.** Suppose the target is a box
\(\prod_i[b_i]\), and
\[
                         \sum_i(a_i-1)=\sum_i(b_i-1).              \tag{2}
\]
Then every injective order map has the rank-preserving property required
by the lemma, even if rank preservation was not assumed. Every source
maximal chain has the maximum possible target length. Its image must
start at target rank zero, end at the top rank, and increase rank by one
at each step. Every source element, and every source cover, lies on such
a maximal chain. The lemma therefore applies to the whole map.

## 2. Application to the balanced staircase

The balanced \(d\)-axis staircase in \([2s]^d\) has rank polynomial
\[
                            [s](q)^{d-1}[(d+1)s](q),              \tag{3}
\]
where \([n](q)=1+q+\cdots+q^{n-1}\). Its cardinality and rank numbers
therefore agree with the product
\[
                              [s]^{d-1}\times[(d+1)s].            \tag{4}
\]
For \(s\ge2\) and \(d\ge2\), there is nevertheless **no injective
order map** from (4) into the staircase, or even into the full ambient
box \([2s]^d\). Both products have height \(d(2s-1)\), so the
equal-height corollary would force the map to be a coordinate-permuted
box. Its factor of length \((d+1)s>2s\) cannot fit in any target axis.

This already excludes a product order map from \([3s]\times[s]\) into
the two-dimensional L-shaped staircase. It also excludes the proposed
four-axis map from \([s]^3\times[5s]\). Adjoining an independent
\([2s]\) to source and target does not help: both products then have
five nontrivial axes and the same height, while the \([5s]\) factor
still cannot fit in an ambient axis.

There is no contradiction with the accepted balanced symmetric chain
decomposition. Equal rank polynomials and symmetric chain decompositions
allow chains of equal starting rank to be paired, giving a rank-preserving
bijection that preserves every comparison *within those chosen chains*.
Such a bijection must lose some comparisons between different chains.
Preserving a chosen chain partition is enough for some compiler tasks;
preserving the whole transverse product order is the extra requirement
ruled out here.

## 3. The ideal-lattice description and theorem scope

For coordinate lengths \(n_i\) and interior cuts
\(1\le u_i\le n_i-1\), introduce coordinate
chains
\[
             v_{i,1}<\cdots<v_{i,n_i-1}
\]
and add the threshold relations
\[
                         v_{i,u_i}<v_{i+1,u_{i+1}}.
\]
An ideal contains a prefix of length \(x_i\) on each coordinate chain.
These threshold relations impose exactly
\(\mathbf1_{x_i\ge u_i}\ge\mathbf1_{x_{i+1}\ge u_{i+1}}\).
The staircase is therefore the distributive lattice of these ideals,
ranked by \(\sum_i x_i\). The independent absorbed chain corresponds
to adjoining one disjoint coordinate chain to the underlying poset.

For the four-axis staircase under discussion, with \(n_i=2s\),
\(s\ge2\), and at least the three unchanged cuts equal to \(s\),
the underlying cover graph branches at threshold vertices. It is not an up-down fence
whose cover graph is a path. Gansner's result for the lattice of ideals
of an up-down poset consequently does not apply merely from this
description. Its published abstract asserts a nested chain decomposition
for its stated up-down class:
[Gansner, *On the lattice of order ideals of an up-down poset*](https://www.sciencedirect.com/science/article/pii/0012365X82901340).

A further checked primary source studies linked coordinate chains and
rank-polynomial symmetries. Definition 4.1 and Section 4 of
[Kantarcı Oğuz--Özel--Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*](https://arxiv.org/pdf/2211.08382)
do not supply a Sperner or normalized-matching theorem for this
asymmetric ideal lattice. Rank symmetry or unimodality alone would not
supply the missing chain-count upper bound.

No applicable general Sperner theorem was established in this bounded
inspection. The remaining constructive task is to build actual
rank matchings or reroute the asymmetric chains. Neither (3), the
ideal-lattice description, nor the negative embedding result proves
that the asymmetric staircase is or is not Sperner.
