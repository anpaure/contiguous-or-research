# Fibre transversals admit an automatic short-gap refinement, with exact triangular capacity

**Date:** 2026-08-05  
**Method:** cyclic division with remainder and convex interval packing; no
computation or search  
**Status:** unconditional. Every surjective cyclic value word has a large
canonical-lock-free set whose components have length at most the deadline.
For a fixed choice of one representative per fibre, the largest possible
short-interval capacity has an exact formula. Maximizing this formula over
the representative choices is the complete scalar positional gate. A
doubled-word family proves that large free cardinality and perfect fibre
hitting alone can still leave only \(O(W)\) capacity.

## 1. Set-up

Let

\[
                         S=(S_i)_{i\in\mathbb Z_W}               \tag{1.1}
\]

be a cyclic word whose set of values has size \(M\), and assume every value
occurs. For a value \(X\), put

\[
                         O_X=\{i:S_i=X\}.                        \tag{1.2}
\]

Choose one representative from every fibre:

\[
                         L=\{p(X):p(X)\in O_X\}.                 \tag{1.3}
\]

Thus \(|L|=M\). Put \(U=W-M\), and write the lengths of the cyclic gaps of
\(\mathbb Z_W\setminus L\) as

\[
                         g_1,\ldots,g_M,
 \qquad \sum_{j=1}^M g_j=U.                                    \tag{1.4}
\]

Zero gaps are allowed. Fix a deadline \(d\ge1\). A set \(R\) is short-gap
if every cyclic component of \(R\) has length at most \(d\). Its triangular
capacity is

\[
 \operatorname{cap}_d(R)
   =\sum_{C\in\operatorname{Comp}(R)} {|C|(|C|+1)\over2}.       \tag{1.5}
\]

This is exactly the number of nonempty intervals contained in \(R\);
because the components have length at most \(d\), no further width
truncation is needed.

## 2. Exact separator refinement of one gap

Write

\[
                         g=q(d+1)+r,\qquad0\le r\le d.           \tag{2.1}
\]

### Lemma 2.1 (minimum separators and maximum capacity)

Among subsets of a gap of length \(g\) whose components have length at most
\(d\), the maximum triangular capacity is

\[
 \boxed{
                         q{d(d+1)\over2}+{r(r+1)\over2}.}        \tag{2.2}
\]

It is attained by deleting exactly

\[
                         q=\left\lfloor{g\over d+1}\right\rfloor \tag{2.3}
\]

separator positions, leaving \(q\) components of length \(d\) and one
component of length \(r\). The number (2.3) is the minimum possible number
of deleted positions.

#### Proof

If \(h\) positions are deleted, at most \(h+1\) linear components remain.
If all have length at most \(d\), then

\[
                         g-h\le d(h+1).                          \tag{2.4}
\]

Hence

\[
 h\ge\left\lceil{g-d\over d+1}\right\rceil
   =\left\lfloor{g\over d+1}\right\rfloor=q.                    \tag{2.5}
\]

Delete positions \(d+1,2(d+1),\ldots,q(d+1)\). This leaves precisely the
component lengths

\[
                         d,\ldots,d,r,                           \tag{2.6}
\]

and attains the deletion bound.

For a fixed number of remaining positions and a fixed component cap \(d\),
the convex function \(x(x+1)/2\) is maximized by transferring positions
from a shorter component to a longer one until all but at most one nonzero
component have length \(d\). Thus (2.6) maximizes capacity among all
minimum-separator refinements. Deleting an additional position either
shortens a component or splits it; in both cases it strictly decreases the
number of contained intervals. Therefore no refinement using more
separators has greater capacity. This proves (2.2). \(\square\)

## 3. Global exact formula

For a transversal \(L\), write

\[
 g_j=q_j(d+1)+r_j,\qquad0\le r_j\le d,                         \tag{3.1}
\]

and define

\[
 \mathcal C_d(L)=\sum_{j=1}^M\left[
       q_j{d(d+1)\over2}+{r_j(r_j+1)\over2}\right].             \tag{3.2}
\]

### Theorem 3.1 (exact fibre-safe triangular capacity)

Let \(\mathcal R\) be the family of all short-gap sets \(R\) such that no
value fibre is contained in \(R\). Then

\[
 \boxed{
   \max_{R\in\mathcal R}\operatorname{cap}_d(R)
     =\max_{p(X)\in O_X}\mathcal C_d(\{p(X)\}).}                 \tag{3.3}
\]

For every fixed transversal \(L\), the maximizing refinement constructed in
Lemma 2.1 has

\[
 |R|=U-\sum_jq_j
     \ge U-{U\over d+1}.                                       \tag{3.4}
\]

#### Proof

Fix \(L\). Refine every one of its gaps by Lemma 2.1. The resulting set
\(R\) is short-gap, is disjoint from \(L\), and hence cannot contain a
whole fibre. The gap capacities add, giving \(\mathcal C_d(L)\). Also

\[
                         \sum_jq_j\le{\sum_jg_j\over d+1}
                                           ={U\over d+1},
\]

which proves (3.4). This establishes the lower bound in (3.3).

Conversely, let \(R\in\mathcal R\). Since no fibre lies in \(R\), choose one
point \(p(X)\in O_X\setminus R\) for every value. These points form a
transversal \(L\subseteq\mathbb Z_W\setminus R\). Inside every \(L\)-gap,
the components of \(R\) have length at most \(d\); Lemma 2.1 bounds their
total capacity by the corresponding summand of \(\mathcal C_d(L)\).
Summing and then maximizing over transversals proves the reverse
inequality. \(\square\)

### Corollary 3.2 (exact scalar compiler cut)

If \(D_<\) exact target values must be assigned to pairwise distinct short
intervals while one canonical singleton lock per value fibre is retained,
then such an assignment is scalar-feasible if and only if

\[
                         D_<\le\max_L\mathcal C_d(L).            \tag{3.5}
\]

This is only scalar feasibility: inequality (3.5) does not assign the named
target values or enforce their coordinate positive-hit cuts.

## 4. Large free size does not imply large capacity

Fix \(N\ge1\) and consider the cyclic doubled word

\[
                         x_1,x_1,x_2,x_2,\ldots,x_N,x_N.        \tag{4.1}
\]

Here \(W=2N\), \(M=N\), and \(U=N\). Every transversal chooses one point
from each adjacent equal pair. Therefore every complementary gap has
length at most two. For every \(d\ge2\), no added separator is needed, and

\[
 \max_L\mathcal C_d(L)
   \le{3\over2}N={3\over4}W.                                  \tag{4.2}
\]

On the other hand, the free set has cardinality exactly \(N=W/2\), every
fibre has a locked representative outside it, and all its components have
length at most two.

Thus a linear-size fibre-safe short-gap bank can have only \(O(W)\)
interval capacity. In the OR-word regime the deep demand is
\(\Theta(dW)\), so cardinality, surjectivity, balanced multiplicity two,
and automatic separator refinement do not close the block-atlas gate.
The representative transversal must be positionally concentrated in the
precise sense of (3.3).

## 5. Consequence for PBBS and the delayed queue route

For the canonical depth-\(d\) maximal antecedent, put

\[
 D_{<}=\sum_{s=1}^{r-d-1}{k\choose s}.                          \tag{5.1}
\]

The first PBBS block-atlas clause now has an exact form:

\[
 \boxed{
   \text{choose a depth-\(d\) occurrence transversal \(L\) with }
   \mathcal C_d(L)\ge D_{<}.}                                  \tag{5.2}
\]

The bare statement \(O_X\not\subseteq R\) is automatic after choosing
\(L\), and a set \(R\) of size at least \(U-U/(d+1)\) is automatic as
well. What is not automatic is (5.2).

In the noncanonical delayed-Johnson formulation, one may instead construct
the lower trace so that its duplicate occurrences are already concentrated
in depth-sized blocks. That directly forces a transversal with large
\(\mathcal C_d(L)\). Static containment matching proves that duplicate
owner labels exist, but their FIFO-compatible chronological concentration
remains the open integral theorem.

## 6. Scope

This theorem is purely positional. It proves no PBBS-specific concentrated
section, no duplicate-block queue cycle, no coordinate-value interval atlas,
and no universal OR word.
