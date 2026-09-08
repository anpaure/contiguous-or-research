# A recursive 2-factor of \(Q_{2^t}\) into maximum isometric cycles

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Result

For every \(t\ge1\), with \(n=2^t\), the cube \(Q_n\) has an explicit
2-factor

\[
                         \mathcal F_n
\tag{0.1}
\]

whose components are isometric cycles of length \(2n=2^{t+1}\).
Consequently

\[
                         |\mathcal F_n|
 ={2^n\over2n}=2^{\,n-t-1}.                             \tag{0.2}
\]

The construction is recursive. Given \(\mathcal F_h\), identify

\[
                         Q_{2h}=Q_h^L\square Q_h^R.
\tag{0.3}
\]

For every ordered pair \(C,D\in\mathcal F_h\), the product
\(V(C)\times V(D)\) is a \(2h\)-by-\(2h\) torus. It partitions explicitly
into \(h\) isometric \(4h\)-cycles by pairing adjacent difference
diagonals.

The cyclic direction permutation is also explicit. If the parent cycles
have direction words

\[
                         \pi_C\pi_C,\qquad\pi_D\pi_D,
\tag{0.4}
\]

then the child indexed by \(k\in\mathbb Z_h\) has direction word

\[
                         \Pi_{C,D,k}\Pi_{C,D,k},
\tag{0.5}
\]

where

\[
\boxed{
 \Pi_{C,D,k}
 =\operatorname{sh}\bigl(\operatorname{rot}_{2k}\pi_C,\pi_D\bigr).}
\tag{0.6}
\]

Here

\[
 \operatorname{sh}
 ((a_0,\ldots,a_{h-1}),(b_0,\ldots,b_{h-1}))
 =(a_0,b_0,a_1,b_1,\ldots,a_{h-1},b_{h-1}).             \tag{0.7}
\]

One may instead pair difference diagonals
\((2k+1,2k+2)\); this replaces \(2k\) in (0.6) by \(2k+1\).
That parity choice may be made independently in every product torus.

Every \(q\)-term consecutive direction block in a child splits exactly
into two consecutive parent blocks of sizes

\[
                         \left\lceil{q\over2}\right\rceil,
 \qquad                  \left\lfloor{q\over2}\right\rfloor.
\tag{0.8}
\]

Iterating, if the coordinate set is viewed as the leaves of the recursive
binary decomposition, then for every node \(B\) at depth \(a\),

\[
\boxed{
 |I\cap B|\in
 \left\{\left\lfloor{q\over2^a}\right\rfloor,
       \left\lceil{q\over2^a}\right\rceil\right\}}
\tag{0.9}
\]

for every cyclic \(q\)-block \(I\) of every direction permutation produced
by the construction. Thus the recursive factor has a dyadically balanced,
bit-reversal-type shallow-shadow geometry.

The construction is a genuine 2-factor, not merely a collection of
cycles: the product tori are disjoint, and the difference-diagonal cycles
partition each torus vertex by vertex.

## 1. Classification of maximum isometric cube cycles

Because \(Q_n\) is bipartite, an isometric cycle has even length \(2s\).
Its two antipodal cycle vertices are at distance \(s\), while
\(\operatorname{diam}(Q_n)=n\). Hence \(s\le n\), so \(2n\) is the
maximum possible isometric-cycle length.

Let a cycle in \(Q_n\) have edge-direction word

\[
                         d_0d_1\cdots d_{2n-1},
\tag{1.1}
\]

where \(d_i\in[n]\) is the coordinate flipped by its \(i\)-th edge.

### Lemma 1.1

A \(2n\)-cycle in \(Q_n\) is isometric if and only if its direction word
is

\[
\boxed{\pi\pi}                                           \tag{1.2}
\]

for a permutation \(\pi\) of the \(n\) coordinates.

#### Proof

Suppose first that the cycle is isometric. Two cycle vertices at distance
\(n\) must be at cube distance \(n\), so every \(n\)-edge semicircle flips
all \(n\) coordinates exactly once. Hence each length-\(n\) block

\[
                         d_i,d_{i+1},\ldots,d_{i+n-1}
\tag{1.3}
\]

is a permutation of \([n]\). Comparing the blocks beginning at \(i\) and
\(i+1\), the deleted direction \(d_i\) must equal the inserted direction
\(d_{i+n}\). Therefore

\[
                         d_{i+n}=d_i
\tag{1.4}
\]

for every \(i\), proving (1.2).

Conversely, suppose the word is \(\pi\pi\). Every cyclic block of at most
\(n\) consecutive directions has no repetition. Thus a path of length
\(s\le n\) along the cycle has endpoints at Hamming distance \(s\).
For any two cycle vertices the shorter cyclic path has length at most
\(n\), so their cube distance equals their cycle distance. The cycle is
isometric. \(\square\)

In particular, a \(2n\)-cycle of this kind reaches the complementary cube
vertex after exactly \(n\) edges.

## 2. The product-torus lemma

Let \(C,D\) be isometric \(2h\)-cycles on disjoint \(h\)-coordinate
cubes. Index their vertices cyclically as

\[
 C=(c_i:i\in\mathbb Z_{2h}),\qquad
 D=(d_j:j\in\mathbb Z_{2h}),
\tag{2.1}
\]

and write

\[
 a_i=\operatorname{dir}(c_ic_{i+1}),\qquad
 b_j=\operatorname{dir}(d_jd_{j+1}).                    \tag{2.2}
\]

By Lemma 1.1,

\[
                         a_{i+h}=a_i,\qquad b_{j+h}=b_j,
\tag{2.3}
\]

and every \(h\) consecutive \(a\)'s or \(b\)'s use all coordinates of
their respective cube once.

Inside \(V(C)\times V(D)\), define the difference diagonal

\[
 \Delta_s=\{(c_i,d_j):i-j=s\pmod{2h}\},
 \qquad s\in\mathbb Z_{2h}.                             \tag{2.4}
\]

For \(k\in\{0,\ldots,h-1\}\), let \(E_k(C,D)\) be the alternating cycle

\[
\begin{aligned}
 (c_{2k},d_0)&,(c_{2k+1},d_0),
 (c_{2k+1},d_1),(c_{2k+2},d_1),\\
 &\ldots,\,
 (c_{2k+s},d_s),(c_{2k+s+1},d_s),\ldots                 \tag{2.5}
\end{aligned}
\]

with indices modulo \(2h\), continuing until the starting vertex returns.
Equivalently, at every even step move forward in \(C\), and at every odd
step move forward in \(D\).

### Lemma 2.1

For fixed \(C,D\):

1. \(E_k(C,D)\) is a simple cycle of length \(4h\);
2. its vertex set is
   \[
             V(E_k)=\Delta_{2k}\mathbin{\dot\cup}\Delta_{2k+1};
                                                               \tag{2.6}
   \]
3. the \(h\) cycles \(E_k(C,D)\) partition \(V(C)\times V(D)\);
4. every \(E_k(C,D)\) is isometric in \(Q_{2h}\).

#### Proof

At even time \(2s\), the current vertex is

\[
                         (c_{2k+s},d_s)\in\Delta_{2k}.
\tag{2.7}
\]

At odd time \(2s+1\), it is

\[
                         (c_{2k+s+1},d_s)\in\Delta_{2k+1}.
\tag{2.8}
\]

As \(s\) runs through \(\mathbb Z_{2h}\), (2.7) visits every vertex of
\(\Delta_{2k}\) once and (2.8) visits every vertex of
\(\Delta_{2k+1}\) once. This proves simplicity, length \(4h\), and (2.6).

The pairs

\[
                         \{2k,2k+1\},
 \qquad 0\le k<h,                                      \tag{2.9}
\]

partition \(\mathbb Z_{2h}\). Since the diagonals partition the whole
torus, the cycles in (2.6) partition \(V(C)\times V(D)\).

The first \(2h\) edge directions of \(E_k\) are

\[
 a_{2k},b_0,a_{2k+1},b_1,\ldots,a_{2k+h-1},b_{h-1}.
\tag{2.10}
\]

The \(a\)-subsequence contains every left coordinate once, and the
\(b\)-subsequence contains every right coordinate once. Hence (2.10) is
a permutation of all \(2h\) coordinates. By (2.3), the next \(2h\)
directions repeat (2.10). Lemma 1.1 proves isometry. \(\square\)

There is a second diagonal matching,

\[
                         \{2k+1,2k+2\},
 \qquad 0\le k<h.                                      \tag{2.11}
\]

It gives the same theorem with \(2k\) replaced by \(2k+1\). Reversing both
parent orientations also gives a legal factor, so cyclic rotations and
reversals of the parent direction permutations remain available.

## 3. Recursive construction of the factor

Start at \(n=2\). The square \(Q_2\) itself is the factor

\[
                         \mathcal F_2=\{Q_2\},
\tag{3.1}
\]

and its direction word is \((1,2)(1,2)\).

Assume \(\mathcal F_h\) is a vertex partition of \(Q_h\) into isometric
\(2h\)-cycles. In

\[
                         Q_{2h}=Q_h^L\square Q_h^R,
\tag{3.2}
\]

the sets

\[
                         V(C)\times V(D),
 \qquad C,D\in\mathcal F_h,                             \tag{3.3}
\]

partition the vertex set. Apply Lemma 2.1 in every product (3.3), and set

\[
\boxed{
 \mathcal F_{2h}
 =\{E_k(C,D):
      C,D\in\mathcal F_h,\ 0\le k<h\}.}                 \tag{3.4}
\]

The factors of the product tori are disjoint and spanning, so
\(\mathcal F_{2h}\) is a spanning 2-regular subgraph. Every component is
an isometric \(4h\)-cycle.

If \(f(h)=|\mathcal F_h|\), then

\[
                         f(2h)=h f(h)^2.                \tag{3.5}
\]

Using \(f(h)=2^h/(2h)\),

\[
 h\left({2^h\over2h}\right)^2
 ={2^{2h}\over4h}
 ={2^{2h}\over2(2h)},                                  \tag{3.6}
\]

which is the required component count. This completes the induction for
all \(n=2^t\).

The construction is algorithmically explicit: recursively find the unique
parent cycles \(C,D\) containing the left and right halves of a vertex,
read their phase indices \(i,j\), and choose the unique \(k\) for which
\(i-j\in\{2k,2k+1\}\).

## 4. Exact recursion for direction permutations

Root \(C,D\) so that their direction permutations are

\[
 \pi_C=(a_0,\ldots,a_{h-1}),\qquad
 \pi_D=(b_0,\ldots,b_{h-1}).                            \tag{4.1}
\]

Equation (2.10) gives

\[
 \Pi_{C,D,k}
 =(a_{2k},b_0,a_{2k+1},b_1,\ldots,
   a_{2k+h-1},b_{h-1}),                                \tag{4.2}
\]

with the \(a\)-indices reduced modulo \(h\). This is exactly (0.6).
The same \(\Pi_{C,D,k}\) occurs in both antipodal halves of the child.

The direction necklace may repeat for different \(k\). Since rotation is
modulo \(h\), the even-diagonal matching supplies the rotations

\[
                         0,2,4,\ldots,2h-2\pmod h.
\tag{4.3}
\]

For even \(h\), these are the \(h/2\) even rotations, each twice. The
odd-diagonal matching supplies all odd rotations, each twice. Thus the
recursion gives controlled phase diversity, but not \(h\) unrelated
direction permutations per product torus.

With zero rotations and a fixed left/right binary coordinate labeling,
the canonical recursion is

\[
                         \pi_{2h}=\operatorname{sh}
                           (\pi_h^L,\pi_h^R).            \tag{4.4}
\]

Starting from \((0,1)\), this is the bit-reversal order on the \(t\)-bit
coordinate labels. The permitted local rotations and reversals give
recursive phase-twisted bit-reversal orders.

## 5. Consecutive direction blocks

Put

\[
 A_s=a_{2k+s},\qquad B_s=b_s.
\tag{5.1}
\]

Then the child permutation is

\[
                         A_0,B_0,A_1,B_1,\ldots,A_{h-1},B_{h-1}.
\tag{5.2}
\]

For a block of length \(q\) beginning at the even phase \(2s\), its
direction set is

\[
\boxed{
\begin{aligned}
 I_{2s,q}={}&
 \{A_s,A_{s+1},\ldots,
       A_{s+\lceil q/2\rceil-1}\}\\
 &\mathbin{\dot\cup}
 \{B_s,B_{s+1},\ldots,
       B_{s+\lfloor q/2\rfloor-1}\}.
\end{aligned}}                                         \tag{5.3}
\]

For a block beginning at the odd phase \(2s+1\),

\[
\boxed{
\begin{aligned}
 I_{2s+1,q}={}&
 \{B_s,B_{s+1},\ldots,
       B_{s+\lceil q/2\rceil-1}\}\\
 &\mathbin{\dot\cup}
 \{A_{s+1},A_{s+2},\ldots,
       A_{s+\lfloor q/2\rfloor}\}.
\end{aligned}}                                         \tag{5.4}
\]

All indices are cyclic. Equations (5.3)--(5.4) prove (0.8).

### Proposition 5.1 (dyadic balance)

Let \(I\) be a cyclic block of \(q\) directions in any recursively
constructed permutation on \(2^t\) coordinates. At recursive depth \(a\),
each of the \(2^a\) coordinate subcubes \(B\) receives either

\[
                         \lfloor q/2^a\rfloor
 \quad\hbox{or}\quad
                         \lceil q/2^a\rceil
\tag{5.5}
\]

directions of \(I\).

#### Proof

At the root, (5.3)--(5.4) split \(q\) into its floor and ceiling halves.
The intersection with either child is a cyclic consecutive block in that
child's direction permutation. Apply the same assertion recursively.
After \(a\) splittings, each count is obtained by \(a\) successive
floor/ceiling halvings, hence is one of the two integers in (5.5).
\(\square\)

This gives the exact shallow-shadow carrier shape. The construction does
not merely say that every \(q\)-window uses \(q\) distinct coordinates;
it says how those coordinates are distributed through the full recursive
cube hierarchy.

### Corollary 5.2 (fixed-hierarchy direction deficit)

At the top decomposition \([2h]=L\mathbin{\dot\cup}R\), every cyclic
\(q\)-block satisfies

\[
 \bigl||I\cap L|-|I\cap R|\bigr|\le1.                  \tag{5.6}
\]

In particular, every two-direction block contains one left and one right
coordinate. No pair contained wholly in \(L\), and no pair contained
wholly in \(R\), occurs consecutively in any cycle of this factor.

More generally, at recursive depth \(a\), the direction blocks are
restricted to the balanced occupancy vectors in (0.9). Hence the exact
vertex 2-factor is not an all-direction shallow design relative to one
fixed binary coordinate hierarchy.

#### Proof

Equation (5.6) is (5.3)--(5.4). For \(q=2\), both the floor and ceiling
in (0.8) equal one. The general assertion is Proposition 5.1.
\(\square\)

Thus any application requiring all shallow coordinate blocks must mix
different binary coordinate splittings, or use trades which change the
direction necklaces. Translations or phase choices inside the present
factor do not remove (5.6).

## 6. The induced monotone faces

Let a child cycle be rooted at a vertex \(x_0\), with direction
permutation \(\Pi=(\pi_0,\ldots,\pi_{n-1})\). Put

\[
                         x_i=x_0+\sum_{j<i}e_{\pi_j},
 \qquad0\le i\le n.                                    \tag{6.1}
\]

Then \(x_n=x_0+\mathbf1\), and the second half is the complementary copy
of the first. A consecutive \(q\)-edge segment beginning at phase \(i\)
is a monotone chain in the axis-parallel face

\[
\boxed{
 x_i+\operatorname{span}
 \{e_{\pi_i},e_{\pi_{i+1}},\ldots,e_{\pi_{i+q-1}}\}.}   \tag{6.2}
\]

The antipodal occurrence beginning at \(i+n\) lies in the complementary
face obtained by adding \(\mathbf1\). Thus each cyclic direction block
has exactly two occurrences within a cycle, one in each antipodal half.

Equations (5.3)--(5.4) recursively identify the free-coordinate set in
(6.2). They are the precise data needed by any shallow-shadow coverage
argument.

Two cautions remain.

1. Different cycles can span the same physical face even when their
   direction blocks agree. The direction recursion alone does not control
   basepoint collisions.
2. Every child direction block is constrained by dyadic balance (0.9).
   Therefore this factor is highly structured, not a surrogate for a
   uniform random permutation factor. Any constant-one shadow theorem
   must exploit this bit-reversal structure or mix recursive coordinate
   frames; it cannot assume arbitrary direction necklaces.

## 7. Optional phase freedom

In each product torus one may independently:

1. choose the even or odd perfect matching of the difference diagonals;
2. reverse \(C\), reverse \(D\), or reverse both;
3. cyclically re-root either parent cycle before applying (2.5);
4. swap the left and right factors.

These operations preserve the vertex partition and isometry proof. On
direction permutations they generate cyclic rotations, reversals, the
two shuffle parities, and interchange of the two parent blocks.

This is substantial recursive phase freedom, but it preserves the
floor/ceiling split (0.8) and the dyadic-balance invariant (0.9). Hence
the invariant is intrinsic to this alternating product construction.

## 8. Verdict

The induction through

\[
                         Q_{2h}=Q_h\square Q_h
\tag{8.1}
\]

does produce the requested exact factor. The essential local object is
not a rectangular boundary in the product torus but the union of two
adjacent difference diagonals. Alternating horizontal and vertical edges
turns that union into one isometric cycle, and the \(h\) diagonal pairs
tile the whole torus.

The resulting cyclic direction permutations obey the exact shuffle law
(0.6). Consequently shallow direction blocks obey the recursive formulas
(5.3)--(5.4) and the dyadic-balance law (0.9). This solves the pure
2-factor existence problem explicitly while exposing, rather than hiding,
the remaining shadow-coverage constraint.
