# Lane F: root-scale \(H_r\)-conjugated leaf conveyor

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let

\[
 H_r=\langle(2\ 3),(4\ 5),\ldots,(2r-2\ 2r-1)\rangle
       \cong C_2^{r-1},                                      \tag{0.1}
\]

and let \(G_r\) have vertex set \(D_r\), with every
\(H_r\)-translate of every context-closed certified leaf-rectangle edge

\[
             C[1100R]\longleftrightarrow C[1010R].          \tag{0.2}
\]

Root-scale conjugation is much stronger than the untransformed leaf graph,
but it is not fully connected.

\[
 \boxed{G_r\text{ is connected exactly for }r\le3.}          \tag{0.3}
\]

For \(r\ge4\), its components have a complete normal form.  Pair the
coordinates as

\[
 (2,3),(4,5),\ldots,(2r-2,2r-1).                           \tag{0.4}
\]

Replacing a pair `11`, `00`, or a mixed pair by \(U,D,F\), respectively,
turns a Dyck word into a Motzkin path of length \(r-1\).  In these
coordinates an odd-depth conjugated leaf rotation is exactly

\[
                              UD\longleftrightarrow FF.     \tag{0.5}
\]

Erase every adjacent peak \(UD\) to \(FF\).  The result is a unique
peakless Motzkin path \(N\).  This \(N\) is invariant, but one further
decoration is sometimes needed.  An isolated flat of \(N\) is called
**frozen** if its predecessor is \(D\) or its successor is \(U\), with
the two outside boundaries regarded as compatible.  The orientation
`10` versus `01` of each frozen flat is also invariant.

Two Dyck roots lie in the same component of \(G_r\) if and only if they
have the same peak-erasure normal form and the same orientations at all
its frozen flats.

If \(c_r=|\pi_0(G_r)|\), then

\[
 c_r=\sum_{N\in\mathsf{PM}_{r-1}}2^{\kappa(N)},              \tag{0.6}
\]

where \(\mathsf{PM}_n\) is the set of length-\(n\) peakless Motzkin
paths and \(\kappa(N)\) is the number of frozen isolated flats.  The
component generating function is given explicitly in Section 7.  Its
first values are

\[
                 c_1,c_2,c_3,c_4,c_5,c_6,c_7,\ldots
                 =1,1,1,2,6,13,28,\ldots .             \tag{0.7}
\]

Consequently the certified edge transpositions generate

\[
 \boxed{
   \prod_{K\in\pi_0(G_r)}\operatorname {Sym}(K),}             \tag{0.8}
\]

not \(\operatorname {Sym}(D_r)\) once \(r\ge4\).

## 1. The \(H_r\)-orbit is a Motzkin skeleton

Write a Dyck root as a binary word

\[
                       x=x_1x_2\cdots x_{2r},             \tag{1.1}
\]

with `1` an up-step and `0` a down-step.  Necessarily \(x_1=1\) and
\(x_{2r}=0\).  For \(1\le i\le r-1\), define

\[
 M_i(x)=
 \begin{cases}
 U,&(x_{2i},x_{2i+1})=(1,1),\\
 D,&(x_{2i},x_{2i+1})=(0,0),\\
 F,&(x_{2i},x_{2i+1})\in\{(1,0),(0,1)\}.
 \end{cases}                                               \tag{1.2}
\]

### Lemma 1.1 (Motzkin orbit dictionary)

The word

\[
                         M(x)=M_1(x)\cdots M_{r-1}(x)     \tag{1.3}
\]

is a Motzkin path of length \(r-1\).  Two Dyck roots are in the same
\(H_r\)-orbit if and only if they have the same Motzkin path.  If \(M\)
has \(f(M)\) flat steps, its orbit has size \(2^{f(M)}\).

#### Proof

Immediately after the first bit the Dyck height is one.  After pair \(i\)
it has the form

\[
                              1+2q_i,                    \tag{1.4}
\]

where `11`, `00`, and a mixed pair change \(q_i\) by \(+1,-1,0\).
Dyck nonnegativity gives \(q_i\ge0\), and immediately before the final
zero the height is one, so \(q_{r-1}=0\).  This is exactly a Motzkin path.

Conversely, orient every flat of a Motzkin path independently as `10` or
`01`, put a leading `1` and a terminal `0`, and read `U,D` as `11,00`.
At pair boundaries the height is positive.  A `D` step occurs only above
Motzkin height zero, while an `01` flat at height one merely touches zero.
Thus every orientation is Dyck.

The generators of \(H_r\) independently exchange the two bits of every
mixed pair and fix equal pairs.  They are therefore transitive on the
\(2^{f(M)}\) orientations and cannot change \(M\). \(\square\)

This also reproves that \(H_r\) preserves \(D_r\).  The identical parity
argument at a nonzero signed height proves preservation of every
Chung--Feller flaw layer.

## 2. Leaf rotations in Motzkin coordinates

A one-hole ordered-tree context inserts its argument as a contiguous Dyck
subword.  Thus every leaf edge (0.2) changes only the middle two bits of
one occurrence of

\[
                         1100\longleftrightarrow1010.     \tag{2.1}
\]

There are two parity cases.

### Lemma 2.1 (even-depth and odd-depth moves)

1. If the local occurrence starts in an odd coordinate, (2.1) flips the
   orientation of one flat \(F_i\) and leaves the Motzkin skeleton fixed.
   Such a flip exists in a skeleton \(M\) precisely when

   \[
       M_i=F,\qquad
       (i=1\text{ or }M_{i-1}\ne D),\qquad
       (i=r-1\text{ or }M_{i+1}\ne U).                 \tag{2.2}
   \]

   Once one such leaf edge exists, its \(H_r\)-orbit contains the full
   orientation edge in direction \(i\) at every vertex of that orbit.

2. If the occurrence starts in an even coordinate, two adjacent Motzkin
   steps change by

   \[
                              UD\longleftrightarrow FF. \tag{2.3}
   \]

   For fixed orientations outside these two positions, the two equal-pair
   swaps in the stabilizer of the \(UD\) endpoint connect that endpoint to
   all four orientations of the \(FF\) endpoint.

#### Proof

If the occurrence starts at position \(2i-1\), its changed bits are
positions \(2i,2i+1\), one of the pairs (0.4).  The preceding local bit
must be one.  It is either the leading bit or the second bit of pair
\(i-1\), which can equal one exactly when \(M_{i-1}\ne D\).  The following
local bit must be zero.  It is either the terminal bit or the first bit of
pair \(i+1\), which can equal zero exactly when \(M_{i+1}\ne U\).  This
proves (2.2).  The relevant pair transposition commutes with \(H_r\), and
\(H_r\) is transitive on all flat orientations, proving the last assertion.

If the occurrence starts at position \(2i\), the two affected coordinate
pairs are

\[
                (11)(00)\longleftrightarrow(10)(10),     \tag{2.4}
\]

which is (2.3).  The swaps inside the two pairs fix the left side of (2.4)
and independently orient the two flats on the right.  All other flat
orientations are again supplied by \(H_r\). \(\square\)

Every occurrence of \(UD\) in a Motzkin skeleton is realized by (2.4):
the literal bits are `1100`, whose first up-step is the root of a local
subtree with left child a leaf.  Hence no quotient edges are missing from
(2.3).

## 3. Peak erasure is the quotient invariant

Orient (2.3) by

\[
                              UD\longrightarrow FF.      \tag{3.1}
\]

Two redexes `UD` cannot overlap.  Replacing one by `FF` creates no new
`UD` across either boundary.  Therefore all redexes may be erased in any
order and give the same path.

### Definition 3.1

Let \(\nu(M)\) be the Motzkin path obtained from \(M\) by replacing every
adjacent \(UD\) by \(FF\).  It has no adjacent \(UD\), and will be called
the **peak-erasure normal form**.

### Lemma 3.2

Two Motzkin paths are connected by the quotient moves (2.3) if and only if
they have the same normal form \(\nu\).

#### Proof

Every move has the same result under complete forward erasure, so \(\nu\)
is invariant.  Conversely, a path reaches \(\nu(M)\) by erasing its
disjoint `UD` factors.  Two paths with the same normal form are therefore
joined by following one reduction path and the reverse of the other.
\(\square\)

This already disproves connectivity for \(r\ge4\).  With \(n=r-1\), the
two peakless Motzkin paths

\[
                              F^n,\qquad UF^{n-2}D       \tag{3.2}
\]

are distinct whenever \(n\ge3\).

## 4. Frozen flat orientations

Peak erasure is not quite the full invariant.  Let \(N\) be peakless.
A flat step \(N_i=F\) is **isolated** if neither neighbour is flat.  It is
called **frozen** when

\[
             (i>1\text{ and }N_{i-1}=D)
             \quad\text{or}\quad
             (i<n\text{ and }N_{i+1}=U).                \tag{4.1}
\]

The outside boundaries are compatible, so they do not themselves freeze a
flat.  Write \(\kappa(N)\) for the number of frozen flats.

For a Dyck word whose skeleton reduces to \(N\), a frozen position stays a
flat in every skeleton in that quotient component: a reverse move can use
only an adjacent pair `FF` of \(N\), while this flat is isolated.  Record
its orientation by

\[
 \epsilon_i(x)=
 \begin{cases}
 0,&(x_{2i},x_{2i+1})=(1,0),\\
 1,&(x_{2i},x_{2i+1})=(0,1).
 \end{cases}                                               \tag{4.2}
\]

### Lemma 4.1 (orientation invariance)

For every frozen flat of \(N=\nu(M(x))\), the bit \(\epsilon_i(x)\) is
constant on the component of \(x\) in \(G_r\).

#### Proof

The quotient move (2.3) acts only on a pair of positions which are `FF` in
the normal form, so it cannot meet an isolated flat.  A fixed-skeleton move
at the isolated position would require (2.2).  Condition (4.1) is exactly
the negation of (2.2) for an isolated flat.  Moves elsewhere do not change
its two coordinates. \(\square\)

## 5. Completeness of the invariant

### Theorem 5.1 (complete component classification)

For \(x,y\in D_r\), the following are equivalent.

1. \(x\) and \(y\) lie in the same component of \(G_r\).
2. Their Motzkin skeletons have the same peak-erasure normal form \(N\),
   and

   \[
                    \epsilon_i(x)=\epsilon_i(y)          \tag{5.1}
   \]

   at every frozen flat of \(N\).

#### Proof

Necessity is Lemmas 3.2 and 4.1.

For sufficiency, first use (3.1) to carry both words to skeleton \(N\).
At every erased `UD`, Lemma 2.1(2) allows the two new flat orientations to
be chosen arbitrarily while all outside orientations are retained.

It remains to compare two orientations of \(N\).

* On every maximal flat run of length at least two, a reverse
  \(FF\to UD\) move supplies one common neighbour for all four
  orientations of each adjacent pair.  These overlapping two-coordinate
  stars connect all orientations of the run.
* At an isolated nonfrozen flat, (4.1) fails, so (2.2) holds and the
  within-skeleton edge flips its orientation.
* At isolated frozen flats, the two words agree by hypothesis.

Thus all remaining orientation differences can be removed independently,
which joins \(x\) to \(y\). \(\square\)

### Corollary 5.2

The graph \(G_r\) is connected for \(r=1,2,3\), and disconnected for
every \(r\ge4\).

#### Proof

For Motzkin lengths zero and one there is only the all-flat normal form.
At length two, the two Motzkin paths `FF` and `UD` have the same normal
form.  None has a frozen orientation class.  Hence \(r\le3\) is connected.
Equation (3.2) proves disconnection for \(r\ge4\). \(\square\)

## 6. Exact generated permutation group

For any finite graph, its edge transpositions generate the full symmetric
group on each connected component and cannot move a vertex between
components.  Therefore Theorem 5.1 gives

\[
 \boxed{
 \langle(x\ y):xy\in E(G_r)\rangle
   =\prod_{K\in\pi_0(G_r)}\operatorname {Sym}(K).}       \tag{6.1}
\]

In particular root-scale \(H_r\)-conjugation generates
\(\operatorname {Sym}(D_r)\) exactly for \(r\le3\).

## 7. Component generating function

Let \(\mathsf{PM}_n\) be the peakless Motzkin paths of length \(n\), and
put

\[
 d_n=\sum_{N\in\mathsf{PM}_n}2^{\kappa(N)}.
                                                               \tag{7.1}
\]

Then \(c_r=d_{r-1}\).  The following algebraic expression is an explicit
component generating function.

Put

\[
 A(z)=1+2z+\frac{z^2}{1-z}
     =\frac{1+z-z^2}{1-z},
 \qquad
 B(z)=z+\frac{z^2}{1-z}=\frac z{1-z}.                 \tag{7.2}
\]

Let

\[
 \mathcal N(x,t)
   =\sum_{k\ge1}\sum_{p=1}^k
       \frac1k\binom{k}{p}\binom{k}{p-1}x^kt^p       \tag{7.3}
\]

be the Narayana generating function.  Equivalently,

\[
 \mathcal N(x,t)=
 \frac{1-x(1+t)-
  \sqrt{1-2x(1+t)+x^2(1-t)^2}}{2x}.                   \tag{7.4}
\]

### Theorem 7.1 (component GF)

\[
 \boxed{
 D(z):=\sum_{n\ge0}d_nz^n
 =\frac1{1-z}
  +A(z)\,
    \mathcal N\!\left(z^2A(z)^2,\frac{B(z)}{A(z)}\right).}
                                                               \tag{7.5}
\]

Consequently

\[
                d_0,d_1,d_2,d_3,d_4,d_5,d_6,\ldots
                =1,1,1,2,6,13,28,\ldots,              \tag{7.6}
\]

and \(c_r=d_{r-1}\).

#### Proof

Delete all flat steps from a peakless Motzkin path which is not all-flat.
The remaining \(U,D\)-word is an ordinary nonempty Dyck path.  Suppose it
has semilength \(k\) and \(p\) peaks.

Flat runs may be reinserted before the first nonflat step, after the last,
and between consecutive nonflat steps.  At a boundary, or between any
pair other than \(UD\), the possibilities are:

* no flat, weight one;
* one frozen flat, weight two; or
* a run of at least two flats, whose orientations lie in one component.

Their generating function is \(A(z)\).  Between an adjacent \(UD\),
peaklessness forbids the empty run; one flat is the flippable pattern
\(UFD\), and a longer run is again one orientation component.  This gives
\(B(z)\).

There are two boundary gaps, \(p\) peak gaps, and
\(2k-1-p\) other internal gaps.  The contribution of the underlying Dyck
path is therefore

\[
 z^{2k}A(z)^{2k+1-p}B(z)^p
 =A(z)\,[z^2A(z)^2]^k[B(z)/A(z)]^p.                  \tag{7.7}
\]

Narayana numbers count Dyck paths by semilength and peaks, giving the
second term of (7.5).  An all-flat normal form has one orientation component
in every length, including lengths zero and one, and contributes
\(1/(1-z)\).  This proves (7.5).  Expanding the first few terms gives
(7.6). \(\square\)

## 8. Scope

The obstruction is genuinely root-scale.  It is not the old normal form
from unconjugated leaf rotations, and it is not the collapsed
size-three-skeleton invariant from embedded pentagons.  The group \(H_r\)
does merge those older components: at \(r=3\) it makes the full Catalan
graph connected.  What survives is the coarser peak-erasure normal form,
plus the explicitly identified frozen orientations.

Therefore root-scale \(H_r\)-conjugated leaf rectangles still do not supply
a full Catalan conveyor at growing \(r\).  Any complete conveyor library
must contain an exact rooted packet whose induced Motzkin action changes
the peak-erasure normal form (for example by moving a separated pattern
\(U F^k D\), not merely an adjacent peak), or must directly couple the
resulting components by a different port-transversal path factor.
