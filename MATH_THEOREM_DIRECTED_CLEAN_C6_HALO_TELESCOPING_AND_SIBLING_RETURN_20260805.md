# Directed clean-C6 halo overlaps telescope exactly

**Date:** 2026-08-05  
**Method:** directed row algebra and path-contour permutations; no search  
**Status:** unconditional for the compound q1/q2 identity and for the
displayed return permutation.  The application of the return permutation
to the full cool-lex recursion remains conditional on one explicitly
isolated directed parent-order premise.

## 1. Oriented clean C6 notation

For one clean Boolean-diamond circuit, read indices modulo three and write

\[
 e_i=u_i\longrightarrow v_i,
 \qquad
 e_i'=u_i\longrightarrow v_{i+1}.
\tag{1.1}
\]

Let the old q1 row on `e_i` be `R_i`.  The clean-C6 identities say

\[
 \operatorname{row}(e_i')=R_{i+1}.
\tag{1.2}
\]

There are two different consequences of (1.2), and their distinction is
the key point.

* At the tail `u_i`, the outgoing row changes from `R_i` to `R_(i+1)`.
* At the head `v_i`, the old incoming edge `e_i` is replaced by
  `e_(i-1)'`, whose row is again `R_i`.

Thus a clean C6 is **head-row transparent**:

\[
 \boxed{\text{the incoming q1 row at every old head is unchanged}.}
\tag{1.3}
\]

Its immediate upper colour is also preserved edgewise, while its three
outgoing lower rows are cyclically permuted.

## 2. Directed-halo telescoping theorem

Consider a family of coherently oriented clean C6 switches in one directed
two-factor.  Assume:

1. no directed old edge is changed by two switches;
2. no vertex is the tail of changed old edges from two switches;
3. whenever a changed old edge of one switch is an incoming companion of
   another switch, their orientations agree with the ambient factor
   direction; and
4. each individual switch satisfies the common-deletion criterion, hence
   is q2-neutral in isolation.

Other than the directed head-to-tail overlaps allowed in item 3, suppose
the protected q2 halos are disjoint.

### Theorem 2.1 (directed-halo telescoping)

Applying the whole family simultaneously preserves:

1. the lower q1 multiset;
2. every immediate upper colour edgewise; and
3. the complete selected q2 multiset.

The common deleted pivots of consecutive switches need not agree.

### Proof

The q1 and immediate-upper statements follow by summing the independent
clean-C6 edge identities.  It remains only to justify q2 at a shared
vertex.

Let `w` be the head of a changed edge of a first switch and the tail of a
changed edge of a second switch.  Write `L` for the old incoming q1 row at
`w`, `R` for its old outgoing q1 row, and `R'` for the second switch's new
outgoing row.  By head-row transparency (1.3), the first switch replaces
the physical incoming edge but leaves its row equal to `L`.  Therefore the
final q2 turn at `w` is exactly

\[
                         L\cap R',
\tag{2.1}
\]

which is the turn counted in the isolated q2 identity of the second
switch.  The first switch contributes zero q2 change at this head, exactly
as in its isolated identity.  Hence the signed q2 change at `w` is neither
lost nor double-counted.

At a vertex which is only a tail, its change is its unique isolated tail
change.  At a vertex which is only a head, (1.3) makes the incoming row
pointwise equal and its outgoing companion is unchanged.  All other turns
are untouched.  Consequently the global signed q2 change is the sum of the
isolated signed changes.  Every summand is zero as a multiset by item 4,
so the total is zero.  `square`

### Corollary 2.2 (one cool-lex sibling rail)

Along one cool-lex sibling-root path, consecutive leaf-plucking packets use
old factor edges

\[
 S_a\longrightarrow gS_a,
 \qquad
 gS_a\longrightarrow g^2S_a
\tag{2.2}
\]

on their common child.  The first edge is the incoming companion of the
second packet at `gS_a`.  Therefore the entire sibling family has one exact
compound q1/q2 identity, provided there are no additional halo collisions.
In particular, the canonical consecutive overlap is allowed and does not
have to be separated by rotations.

## 3. The PBBS velocity sign

For a hook of height `H`, put

\[
                         q_H=2H-1.
\tag{3.1}
\]

In the vacancy-slot convention of the hook-coordinate theorem, one rooted
PBBS factor step is `g=f^2`, and its displacement is

\[
                 2(1-H)=1-q_H\equiv +1\pmod {q_H}.
\tag{3.2}
\]

Equivalently,

\[
 g(x_0,x_1,\ldots,x_{q_H-1})
   =(x_{q_H-1},x_0,\ldots,x_{q_H-2}).
\tag{3.3}
\]

Thus the two occurrences on the common child in Corollary 2.2 really are
successive in the displayed order; reversing the rooted C6 reverses both
child shores and cannot be used to change the port sign independently.

For the promoted hook of height `H+1`, the same calculation gives

\[
 2(1-(H+1))=-2H=1-(2H+1)\equiv+1\pmod{2H+1}.
\tag{3.4}
\]

This determines directed PBBS time **within one fixed promoted necklace**.
It does not order ports lying on distinct promoted necklaces.

## 4. Exact sibling return permutation

Let a sibling path have `E>=1` connector edges, labelled `1,...,E` in its
root-to-last-child order.  Its two child-shore cut permutations are

\[
 \alpha=(2\ 3)(4\ 5)\cdots,
 \qquad
 \beta=(1\ 2)(3\ 4)\cdots,
\tag{4.1}
\]

with missing terminal transpositions omitted.  Put

\[
                         \pi=\beta\alpha.
\tag{4.2}
\]

The usual path-contour calculation gives

\[
 \pi=(1,2,4,6,\ldots,2\lfloor E/2\rfloor,
       \text{positive odd labels in decreasing order}).
\tag{4.3}
\]

Suppose the third-shore cuts occur in the monotone promoted-rail order

\[
                         \gamma=(1\ 2\ \cdots\ E).
\tag{4.4}
\]

For the coherent clean-C6 orientation (1.1), the directed three-shore
return is

\[
                         \sigma=\gamma\beta\alpha=\gamma\pi,
\tag{4.5}
\]

where the rightmost permutation acts first.

### Theorem 4.1 (sibling return)

For `E=1`, the return is the identity on its single label.  For odd
`E=2r+1>=3`,

\[
 \sigma=(1,3,2,5,4,\ldots,2r+1,2r),
\tag{4.6}
\]

is one `E`-cycle.  For `E=2`, the return is the identity on two labels.
For even `E=2r>=4`,

\[
 \sigma=(1,3,2,5,4,\ldots,2r-1,2r-2)(2r),
\tag{4.7}
\]

has one cycle on the first `E-1` labels and fixes `E`, so it has exactly
two cycles.  In every case the sibling return has at most two directed
contours.

### Proof

From (4.1)--(4.2), `pi` sends `1` to `2`, each nonterminal even label to
the next even label, and each odd label at least three to the preceding
odd label.  For odd `E=2r+1`, the terminal even label `2r` goes to
`2r+1`; for even `E=2r`, the terminal label `2r` goes to `2r-1`.
Composing on the left with the positive cyclic shift `gamma` gives exactly
the orbits displayed in (4.6)--(4.7).  The cases `E=1,2` follow directly
from (4.1)--(4.5).  `square`

## 5. What the triple-zero rail proves, and what it does not

For consecutive sibling edges, the promoted marked ports obey

\[
 A0001B\to A0010B\to A0100B\to A1000B.
\tag{5.1}

Hence they are joined by a canonical positive three-edge path in the next
hook angle graph.  Together with Theorem 2.1, this proves that the local
sibling strip has a coherent q1/q2-neutral orientation; the previously
identified companion overlap is not an obstruction.

However, (5.1) is an **angle-graph path between generally distinct PBBS
components**.  Equation (3.4) orders rooted occurrences only within one
component.  Therefore (5.1) by itself does not prove the physical
third-shore cut order (4.4) after the lower-level rails have been spliced.

The exact remaining all-`b` contour gate is now only this directed order
statement:

> recursively assemble the positive three-step promoted rails so that the
> inherited third-shore return on every sibling family is the monotone
> cycle `gamma=(1 2 ... E)` (or prove directly that the resulting `gamma
> beta alpha` has uniformly bounded cycle count).

The q1/q2 composition across the canonical halos is solved by Theorem 2.1,
and if the monotone-order statement holds, Theorem 4.1 gives the sharp
one-or-two-contour bound.  **The one-or-two-contour conclusion is
conditional on physical monotonicity (4.4); it is not an unconditional
consequence of the triple-zero angle rail.**  No claim about q3,
residence, arbitrary upper
targets, common-cap compilation, or `nu(k)<=B(k)+O(1)` is made here.
