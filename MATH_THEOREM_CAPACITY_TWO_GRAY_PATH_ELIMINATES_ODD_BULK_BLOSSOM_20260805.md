# A multiset-combination Gray path matches the complete-transfer capacity-two graph

**Date:** 2026-08-05  
**Method:** exact identification with the Ruskey--Savage multiset
combination graph and alternating edges of a Hamilton path  
**Status:** unconditional near-perfect matching of the **abstract
complete-transfer** capacity-two graph.  It does not eliminate the odd
adjacent-necklace bulk-blossom gate: that physical sector permits only
cyclic nearest-neighbour transfers, is subsequently quotiented by a
background stabilizer, and carries a hub-colour partition constraint.

## 0. Capacity-two token graph

For integers `n>=1` and `0<=R<=2n`, let

\[
 \mathcal T_{n,R}
 =\{x=(x_1,\ldots,x_n)\in\{0,1,2\}^n:
                         \sum_i x_i=R\}.
\tag{0.1}
\]

Join `x` and `y` when, for distinct coordinates `p,q`,

\[
 y_p=x_p+1,\qquad y_q=x_q-1,
 \qquad y_i=x_i\ (i\ne p,q).
\tag{0.2}
\]

Call the resulting graph `G_(n,R)`.  This is the complete-transfer token
graph.  It must not be confused with the physical adjacent-necklace sector,
whose allowed transfer has `q=p+/-1 mod n`.

## 1. Identification with combinations of a multiset

Let

\[
 C(R;2,2,\ldots,2)
\tag{1.1}
\]

be the family of `R`-element combinations of a multiset having two copies
of each of `n` symbols.  A combination is encoded by its multiplicity
vector `(x_1,...,x_n)`, so (1.1) is precisely (0.1).

Ruskey and Savage define two multiset combinations to be adjacent when one
copy of one symbol is replaced by one copy of another symbol.  In
multiplicity coordinates this is exactly (0.2).  Their main theorem gives
an extreme Gray code for every nondecreasing capacity vector, and hence a
Hamilton path in the corresponding multiset-combination graph.

Reference: F. Ruskey and C. Savage, *A Gray Code for Combinations of a
Multiset*, European Journal of Combinatorics **17** (1996), 493--500,
doi:10.1006/eujc.1996.0043.

### Theorem 1.1 (capacity-two Hamilton path)

For every `n,R`, the graph `G_(n,R)` has a Hamilton path.

#### Proof

Apply the Ruskey--Savage theorem to the nondecreasing capacity vector
`(2,...,2)`.  The vertex and adjacency identifications above are
bijective. \(\square\)

No claim of a Hamilton **cycle** is needed here; the 1996 paper itself
lists cyclicity as a stronger open direction in its general setting.

## 2. Exact parity of the central sector

Put

\[
                         T_n=|\mathcal T_{n,n}|
                         =[z^n](1+z+z^2)^n.              
\tag{2.1}
\]

### Lemma 2.1

`T_n` is odd for every `n`.

#### Proof

Choose `j` coordinates carrying a two and `j` coordinates carrying a zero;
all remaining coordinates carry a one.  Therefore

\[
 T_n=\sum_{j=0}^{\lfloor n/2\rfloor}
          {n\choose 2j}{2j\choose j}.                    
\tag{2.2}
\]

The `j=0` term is one.  For every `j>=1`, the central binomial coefficient
`binom(2j,j)` is even.  Thus (2.2) is odd. \(\square\)

## 3. Near-perfect matching in one line

### Theorem 3.1 (odd central bulk matching)

For every `n`, the central capacity-two graph `G_(n,n)` has a matching
covering every vertex except one.

#### Proof

Let

\[
                         v_0,v_1,\ldots,v_{T_n-1}
\tag{3.1}
\]

be the Hamilton path from Theorem 1.1.  Since `T_n` is odd, the edges

\[
 v_0v_1,\ v_2v_3,\ \ldots,\ v_{T_n-3}v_{T_n-2}
\tag{3.2}
\]

are pairwise disjoint and cover every vertex except `v_(T_n-1)`.  Each is
a literal unit-transfer edge. \(\square\)

Reversing the path leaves the other extreme endpoint instead.  Coordinate
permutations give every permuted extreme socket of the same type.

### Corollary 3.2 (all parity cases)

Every graph `G_(n,R)` has a matching of size

\[
                         \left\lfloor{|\mathcal T_{n,R}|\over2}\right\rfloor.
\tag{3.3}
\]

Indeed, alternate the edges of the Hamilton path.  Thus the unrestricted
capacity-two layer never has matching deficiency exceeding one.

## 4. Why this does not close the dyadic blossom programme

Ruskey--Savage adjacency permits replacement of a copy of **any** symbol
by a copy of any other symbol.  The physical adjacent-necklace sector has
only the cyclic nearest-neighbour edges

\[
                         q=p\mathbin{+/-}1\pmod n.       \tag{4.1}
\]

It is a proper spanning subgraph of `G_(n,R)`.  Moreover the physical
objects are orbits under the cyclic stabilizer of the fixed background,
and selected edge occurrences must use every unpointed hub colour at most
once.  A labelled Hamilton path in `G_(n,R)` neither descends to a simple
path in that quotient nor obeys the hub partition matroid.

Consequently Theorem 3.1 supplies no physical wrap current and does not
replace the circulation-blossom theorem.  It is applicable only to a
different cap fibre in which all coordinate-to-coordinate transfers are
literally legal and no quotient or edge-colour restriction is present.

## 5. Exact scope

Proved here:

1. a Hamilton path in every bounded capacity-two layer;
2. odd cardinality of every central layer;
3. an unconditional one-socket near-perfect matching in that abstract
   complete-transfer graph.

Not proved here:

1. a Hamilton or near-perfect matching in the cyclic nearest-neighbour
   token graph;
2. descent through the background-stabilizer quotient;
3. the hub-colour partition constraint;
4. that an arbitrary prescribed finite matching extends;
5. occurrence-labelled typed-cap compatibility of the unmatched socket;
6. residence or upper-shadow properties of the surrounding OR carrier.

The first three are macroscopic physical constraints, not merely a finite
interface around the abstract Gray path.
