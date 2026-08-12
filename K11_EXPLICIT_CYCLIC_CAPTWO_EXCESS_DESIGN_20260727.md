# An explicit optimally pair-balanced cap-two excess design for \(k=11\)

Date: 2026-07-27

## 1. Difference-orbit lemma

Work in \(\mathbb Z_{11}\).  For a four-set \(B\), write

\[
 {\cal O}(B)=\{B+t:t\in\mathbb Z_{11}\}
\]

and, for \(d\in\{1,2,3,4,5\}\), let

\[
 c_d(B)=\#\bigl\{\{x,y\}\in\tbinom B2:y-x\equiv\pm d\pmod {11}\bigr\}.
\]

Every orbit \({\cal O}(B)\) has size \(11\), gives every point degree four,
and gives every pair of cyclic distance \(d\) codegree \(c_d(B)\).

Moreover, if \(a=1,2,3,4,5\) ranges over representatives of
\(\mathbb Z_{11}^{\!*}/\{\pm1\}\), then

\[
 \sum_{a=1}^5 c_d(aB)=\binom42=6
 \qquad(d=1,\ldots,5).                         \tag{1.1}
\]

Indeed multiplication by the five values of \(a\) carries each fixed
nonzero difference through all five unoriented difference classes exactly
once.  Thus five multiplier images of any seed form a translation-orbit
packet of pair codegree exactly six.

## 2. The twelve base blocks

Take two complete multiplier packets

\[
 A=\{0,1,2,3\},\qquad B=\{0,1,2,4\},
\]

and two further blocks

\[
 C=\{0,1,3,5\},\qquad 2C=\{0,2,6,10\}.
\]

Explicitly, let the twelve translation-orbit representatives be

\[
\begin{array}{lllll}
 \{0,1,2,3\},&\{0,2,4,6\},&\{0,3,6,9\},
 &\{0,1,4,8\},&\{0,4,5,10\},\\
 \{0,1,2,4\},&\{0,2,4,8\},&\{0,1,3,6\},
 &\{0,4,5,8\},&\{0,5,9,10\},\\
 \{0,1,3,5\},&\{0,2,6,10\}.&&&
\end{array}                                           \tag{2.1}
\]

The five profiles in the first packet are permutations of
\((3,2,1,0,0)\), while those in the second are permutations of
\((2,2,1,1,0)\).  Inside each packet the five displayed profiles are
distinct.  The last two profiles are

\[
 c(C)=(1,2,1,1,1),\qquad c(2C)=(1,1,1,2,1).       \tag{2.2}
\]

Consequently all twelve translation orbits are distinct: translation
preserves the difference profile, the three sorted profile types above are
different, and within each type the displayed profiles are different.

Let

\[
 {\cal D}=\bigcup_{R\text{ in }(2.1)}{\cal O}(R)
 \subseteq\binom{\mathbb Z_{11}}4.
\]

Then \({\cal D}\) is simple and

\[
 |{\cal D}|=12\cdot11=132,\qquad d_{\cal D}(x)=12\cdot4=48. \tag{2.3}
\]

By (1.1), the two complete packets contribute pair codegree \(12\) in
every difference class.  Equation (2.2) supplies the remaining vector
\((2,3,2,3,2)\).  Therefore

\[
 \boxed{(d_1,d_2,d_3,d_4,d_5)=(14,15,14,15,14).}   \tag{2.4}
\]

This is optimally balanced: the five integer class codegrees have sum
\(12\binom42=72\), hence mean \(14.4\), and (2.4) has discrepancy one.

## 3. Translation to the upper excess design

Let

\[
 \widetilde {\cal D}=\{\mathbb Z_{11}\setminus R:R\in{\cal D}\}
 \subseteq\binom{\mathbb Z_{11}}7.
\]

For \(k=11,r=6\),

\[
 W=\binom{11}{6}=462,\qquad C_5=42,\qquad C_6=132.
\]

Thus \(\widetilde {\cal D}\) has exactly the cardinality of a cap-two upper
excess design.  Complementation gives

\[
 d_{\widetilde {\cal D}}(x)=132-48=84=2C_5,       \tag{3.1}
\]

and, for a pair of cyclic distance \(d\),

\[
 d_{\widetilde {\cal D}}(ij)
 =132-48-48+d_{\cal D}(ij)
 =36+d_{\cal D}(ij).                              \tag{3.2}
\]

Hence the forced swap-pair inventory is

\[
 h_{ij}=d_{\widetilde {\cal D}}(ij)-C_5
       =d_{\cal D}(ij)-6,
\]

with difference-class vector

\[
 \boxed{(h_1,h_2,h_3,h_4,h_5)=(8,9,8,9,8).}       \tag{3.3}
\]

In particular every quota is nonnegative.  Since each point has two
neighbours in each unoriented distance class,

\[
 \sum_{j\ne i}h_{ij}=2(8+9+8+9+8)=84=2C_5,       \tag{3.4}
\]

and, since each distance class contains eleven unordered pairs,

\[
 \sum_{i<j}h_{ij}=11(8+9+8+9+8)=462=W.            \tag{3.5}
\]

## 4. What this proves, and what it does not

The construction satisfies every presently isolated **static moment and
pair-capacity condition** for a translation-equivariant cap-two
\(q=1\) solution:

1. the excess family is simple and has size \(C_6=132\);
2. it is a union of twelve full translation orbits;
3. its upper point degree is exactly \(2C_5=84\);
4. every forced swap quota is nonnegative;
5. the quota row sums and total are exactly (3.4)--(3.5).

It does **not** construct the map

\[
 \sigma:\binom{\mathbb Z_{11}}5\longrightarrow
             \binom{\mathbb Z_{11}}7.
\]

Realizability still asks for an assignment with prescribed upper loads
\(1+\mathbf1_{\widetilde {\cal D}}\), middle degree exactly two, and (for
the desired cycle) connected quotient with nonzero voltage.  Equivalently,
one still needs a perfect matching in the prescribed diamond hypergraph.
The general Farkas inequalities for that hypergraph are not consequences of
the point and pair moments, and the equality matrix is not totally
unimodular.  Thus (2.1) removes the known arithmetic and second-order static
obstructions, but it is not a realization theorem.
