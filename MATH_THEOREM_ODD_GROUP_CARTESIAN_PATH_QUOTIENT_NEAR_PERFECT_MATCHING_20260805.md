# Odd-group quotients of Cartesian path products are parity-perfect

**Date:** 2026-08-05  
**Method:** a graded tensor-chain skew Dirac operator and Pfaffian support;
no computation  
**Status:** unconditional abstract matching theorem.  Its use in a concrete
adjacent-necklace fibre requires an exact, collision-free identification of
that fibre with the stated path-product quotient.

## 1. Statement

For positive integers `n_1,...,n_t`, let

\[
 X=P_{n_1}\square\cdots\square P_{n_t},
\]

where `P_n` is the path on `0,1,...,n-1`.  Let an odd-order group `H`
act by permuting factors of equal size.  The action is by graph
automorphisms, so the ordinary orbit graph `X/H` is defined.

### Theorem 1.1

The orbit graph `X/H` has a matching of deficiency at most one.  More
precisely:

1. if some `n_i` is even, `X/H` has a perfect matching;
2. if every `n_i` is odd, `X/H` has either a perfect matching or a matching
   missing exactly one orbit vertex, according to the parity of `|X/H|`.

No freeness of the action is required.

## 2. The local path complex

Give the standard basis `e_0,...,e_(n-1)` of `C_n` degree `j mod 2`, and
define

\[
 d_ne_{2a+1}=e_{2a},\qquad d_ne_{2a}=0.             \tag{2.1}
\]

Then `d_n^2=0`.  Its homology is zero when `n` is even and is one
dimensional, represented by `e_(n-1)`, when `n` is odd.

On the graded tensor product

\[
 C=C_{n_1}\widehat\otimes\cdots\widehat\otimes C_{n_t},
\]

take the usual tensor differential

\[
 d=\sum_i(-1)^{\deg(v_1)+\cdots+\deg(v_{i-1})}d_{n_i}. \tag{2.2}
\]

Its matrix connects only tuples differing by one unit in one path
coordinate.  By the tensor homology formula,

\[
 \dim H(C,d)=
 \begin{cases}
 0,&\text{some }n_i\text{ is even},\\
 1,&\text{all }n_i\text{ are odd}.
 \end{cases}                                      \tag{2.3}
\]

Equip the displayed basis with the standard orthonormal inner product and
put

\[
                         K=d-d^*.                  \tag{2.4}
\]

The matrix `K` is real skew-symmetric and is supported on edges of `X`.
Moreover

\[
 -K^2=dd^*+d^*d,                                  \tag{2.5}
\]

so Hodge decomposition and (2.3) give

\[
 \dim\ker K=
 \begin{cases}
 0,&\text{some }n_i\text{ is even},\\
 1,&\text{all }n_i\text{ are odd}.
 \end{cases}                                      \tag{2.6}
\]

## 3. Descent through an odd permutation group

Permute tensor factors with the Koszul sign.  This makes every element of
`H` a chain isometry, hence it commutes with `d`, `d^*`, and `K`.

For a tuple `v`, an element of its stabilizer permutes equal tensor factors.
Every cycle of that permutation has odd length, because `H` has odd order.
On a cycle whose common basis element has odd degree, the Koszul sign is

\[
                         (-1)^{\ell-1}=1;
\]

on an even-degree cycle it is also one.  Thus the stabilizer acts trivially
on the line spanned by `v`.  Consequently every ordinary `H`-orbit gives
one nonzero signed orbit sum, and these sums form an orthogonal basis of
the invariant space `C^H`.  They are naturally indexed by the vertices of
the ordinary orbit graph `X/H`.

Restrict `K` to `C^H` and call the resulting skew matrix `K_H`.  A nonzero
off-diagonal entry of `K_H` can occur only when the two corresponding
orbits contain adjacent tuples.  Hence the support graph of `K_H` is a
subgraph of `X/H`.

If some `n_i` is even, `K` is invertible.  Since `K^{-1}` also commutes with
`H`, `K_H` is invertible.  If all `n_i` are odd, restriction cannot increase
the kernel dimension, so

\[
                         \dim\ker K_H\le1.         \tag{3.1}
\]

## 4. Pfaffian extraction

An invertible skew-symmetric matrix has nonzero Pfaffian.  A nonzero term
in its Pfaffian expansion is a perfect matching of its support graph.
Therefore an invertible `K_H` certifies a perfect matching of `X/H`.

If `K_H` has odd order and nullity one, it has rank `N-1`.  Some principal
`(N-1)`-minor is then nonsingular: equivalently, at least one maximal
principal Pfaffian is nonzero.  Indeed, a skew form of rank `2r` has
nonzero exterior power `omega^r`; a nonzero coefficient of that power is
the Pfaffian of a principal `2r` coordinate minor.  Its Pfaffian term is a matching covering all
but the deleted orbit vertex.  This proves Theorem 1.1.

## 5. Allocation-rail corollary

Fix disjoint ordered adjacent coordinate pairs.  On pair `i`, fix total
mass `m_i` and allow the allocations

\[
 (m_i-a_i,a_i),\qquad0\le a_i<m_i.                \tag{5.1}
\]

Changing `a_i` by one is one literal adjacent chip transfer, so the labelled
allocation graph is `box_i P_(m_i)`.  If an odd cyclic stabilizer permutes
equal pair roles and equal masses, the necklace quotient of this **fixed
tagged allocation fibre** has deficiency at most one, and is perfect as
soon as one `m_i` is even.

This includes the endpoint transition

\[
                         (m_i,0)\leftrightarrow(m_i-1,1),
\]

rather than puncturing a separate positive-allocation phase fibre at that
endpoint.

The corollary does not assert that allocation fibres coming from different
untagged zero skeletons are disjoint.  A canonical fibre/normal-form theorem
is still required before taking their union in the adjacent-necklace graph.
