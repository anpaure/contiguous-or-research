# Three-signature octahedral compression and the extensive top factor

Date: 2026-07-27

Scope: extensive decorated carrier cycles, as distinct from the
$O(n)$ broad-support seed bank.

## 0. Outcome

There is a sharp local answer to the random-signature no-go.

1.  **One coherent filler signature is too compressed.**  If all carrier
    tops over one core inherit their filler order from one circular order
    on that core, then the carrier graph is a blow-up of a single
    cyclic-distance graph.  In the calibrated range
    $M>12H$, it is triangle-free.  Since the twelve-top carrier support
    is

    \[
                         K_6\setminus J=K_{2,2,2},
    \]

    it contains no repaired twelve-top source.  Thus maximal signature
    compression destroys the required local topology even though its
    carrier graph can have extensive ordinary cycle rank.

2.  **Three signatures suffice exactly.**  Partition six exterior
    labels into pairs $A,B,C$.  Give the four $AB$ carrier tops one
    filler word, the four $BC$ tops a second filler word, and the four
    $CA$ tops a third.  The octahedral graph has an edge-disjoint
    Hamilton decomposition $P\sqcup Q$ in which each cycle contains
    exactly two edges of each of the three classes.  After orienting the
    cycles, the two exterior placeholder columns also contain the same
    six labels.  Hence

    \[
                         \boxed{\Sigma(P)=\Sigma(Q)}
    \]

    column by column.  This replaces an
    $\exp[\Theta(m\log m)]$ random signature by three deterministic
    states.

3.  The complete top catalogue has a near-perfect matching by such
    octahedral supports: the fixed-rank support hypergraph is regular
    and has $o(1)$ relative codegrees.  Therefore the three-signature
    construction supplies $(1-o(1))N/12$ top-disjoint decorated packet
    templates, not merely $O(n)$ seeds.

The remaining obstruction is not the decorated signature.  The
extensive factor uses $(1-o(1))dN=\Theta(W)$ middle-owner occurrences,
so collisions cannot be overwritten at polynomial cost.  One still
needs either an owner-resolved matching of these templates or a
row-mixed covariance factor embedded in an already coefficient-one
table.  This is exactly where the extensive problem differs from the
solved seed bank.

## 1. Coherent one-signature tables are triangle-free

Fix a core $C$ of size $M-2$ and a circular order

\[
                         \pi_C=(c_0,\ldots,c_{M-3}).       \tag{1.1}
\]

For every exterior pair $xy$, suppose the rooted word on
$C\cup\{x,y\}$ is obtained by inserting $x,y$ into two gaps of
$\pi_C$, while the restriction to $C$ remains (1.1).  Let
$B_i$ be the set of exterior labels inserted in the $i$-th gap of
$\pi_C$.  Put

\[
                         t=\kappa-1=4H-2.                  \tag{1.2}
\]

### Lemma 1.1 (gap blow-up)

The carrier graph on labels outside $C$ is a subgraph of

\[
                         \bigcup_{i\in\mathbb Z_{M-2}}
                         K_{B_i,B_{i+t}}.                  \tag{1.3}
\]

If both insertion orientations are admitted, equality holds after the
obvious convention for labels in a common gap.

#### Proof

Between a label in $B_i$ and a label in $B_j$, the restricted cyclic
word contains exactly $j-i$ core labels along the forward arc, with
indices modulo $M-2$.  The two exterior labels occupy carrier
placeholder positions at cyclic distance $kappa$ precisely when the
open arc contains $kappa-1=t$ core labels, or the reverse arc has that
property.  This is exactly (1.3).  \(\square\)

### Corollary 1.2 (one-signature topology obstruction)

If

\[
                         3t<M-2,                            \tag{1.4}
\]

then the graph in (1.3) is triangle-free and hence contains no
$K_{2,2,2}$.

#### Proof

The base graph on gap indices has edges $i\sim i\pm t$.  A triangle
would give a signed relation

\[
                         \epsilon_1t+\epsilon_2t+epsilon_3t
                         \equiv0\pmod{M-2},
                         \qquad\epsilon_i\in\{\pm1\}.
\]

Its absolute integer value is $t$ or $3t$, strictly between zero and
$M-2$ under (1.4), a contradiction.  Blowing up vertices by independent
sets creates no triangle.  Since $K_{2,2,2}$ contains triangles, it is
absent.  \(\square\)

In the calibrated regime $M\gg H$, condition (1.4) holds.  Thus a
single globally coherent restriction order is anti-random in the wrong
way: it compresses signatures but rules out the repaired support.

## 2. The exact three-signature Hamilton decomposition

Let

\[
 A=\{a_0,a_1\},\qquad B=\{b_0,b_1\},\qquad C'=\{c_0,c_1\}.
\tag{2.1}
\]

The octahedral carrier graph is the complete tripartite graph
$K_{A,B,C'}=K_{2,2,2}$.  Define

\[
 P=(a_0,b_0,c_0,a_1,c_1,b_1,a_0),                         \tag{2.2}
\]

and

\[
 Q=(a_0,c_0,b_1,a_1,b_0,c_1,a_0).                         \tag{2.3}
\]

### Lemma 2.1 (balanced Hamilton decomposition)

The cycles $P,Q$ are edge-disjoint and exhaust $K_{2,2,2}$.  Each
contains exactly two $AB$, two $BC'$, and two $C'A$ edges.

#### Proof

The edges of $P$ are

\[
 a_0b_0, b_0c_0, c_0a_1, a_1c_1, c_1b_1, b_1a_0.
\]

The remaining two edges in each bipartite class are

\[
 a_0c_0, c_0b_1, b_1a_1, a_1b_0, b_0c_1, c_1a_0,
\]

which are exactly the edges of $Q$.  The class count is visible in
either list.  \(\square\)

## 3. Exact signature compression

Fix a common $(M-2)$-core $D$.  Choose three rooted filler words on
$D$,

\[
                         \rho_{AB},\qquad\rho_{BC},qquad
                         \rho_{CA}.                         \tag{3.1}
\]

They may be arbitrary permutations of $D$.  On a carrier top
$D\cup\{x,y\}$ of class $XY\in\{AB,BC,CA\}$, put $x,y$ in the two
exterior placeholder positions and put the core labels in the remaining
positions according to $\rho_{XY}$.  Orient the row by the orientation
of its edge in $P$ or $Q$: the tail occupies the first placeholder and
the head the second.

### Theorem 3.1 (three-signature equality)

The two six-row rooted tables on $P$ and $Q$ have identical column
multisets.

#### Proof

At a filler column belonging to $ho_{AB}$, each cycle has exactly two
$AB$ rows by Lemma 2.1, and those rows display the same prescribed core
label.  The other four rows display the labels prescribed by their two
classes.  Thus the six-entry filler multiset depends only on the class
count $(2,2,2)$ and is the same for $P$ and $Q$.  This holds at every
filler column, even when the three words in (3.1) are different.

Each directed Hamilton cycle has every exterior vertex once as a tail
and once as a head.  Hence the first placeholder column of each table is
the multiset $A\cup B\cup C'$, and so is the second placeholder column.
Therefore all $M$ rooted column multisets agree.  \(\square\)

The local $F/G$ palette and squarefree repair may now be applied exactly
as in the established twelve-top packet theorem: Theorem 3.1 supplies
the filler-column hypothesis which random words fail.

### Minimality

Theorem 3.1 does not claim that three is information-theoretically
minimal among every possible encoding.  It proves the relevant sharp
structural dichotomy:

* one coherent core signature forces a triangle-free carrier support;
* three edge-class signatures realize the required octahedron exactly.

## 4. An extensive top-only factor

Let $\mathcal K$ be the $12$-uniform hypergraph whose vertices are the
rank-$M$ tops and whose hyperedges are

\[
 \mathcal P(D,S,J)
 =\{D\cup e:e\in E(K_S)\setminus J\},                    \tag{4.1}
\]

where $|D|=M-2$, $S$ is a disjoint six-set, and $J$ is a perfect
matching on $S$.  Every hyperedge is an octahedral twelve-top support.

### Lemma 4.1 (regularity and small codegrees)

$\mathcal K$ is regular, and its maximum pair codegree is $o$ of its
degree.

#### Proof

Fix a top $U$.  To form a block containing it, choose its exterior edge
$e\in\binom U2$, choose the other four exterior labels in
$\binom{[n]\setminus U}4$, and choose a perfect matching on the resulting
six-set which does not contain $e$.  Of the fifteen perfect matchings of
$K_6$, exactly three contain $e$.  Thus

\[
 d_{\mathcal K}(U)
 =12\binom M2\binom{n-M}4,                                \tag{4.2}
\]

independent of $U$.

Two distinct tops in one block share the same $(M-2)$-core and their
exterior edges are either adjacent or disjoint.  Hence their Johnson
distance is one or two.  Fixing both tops determines at least one more
exterior label and removes a factor tending to infinity from either
$\binom M2$ or $\binom{n-M}4$ in (4.2).  A direct split into the
distance-one and distance-two cases gives

\[
                         \Delta_2(\mathcal K)
                         =O(d_{\mathcal K}/m).             \tag{4.3}
\]

This proves the assertion.  \(\square\)

### Theorem 4.2 (top-factor consequence)

The hypergraph $\mathcal K$ has a matching covering $(1-o(1))N$ tops.

#### Proof

Apply the standard fixed-uniformity near-perfect matching theorem to
the regular $12$-uniform hypergraph $\mathcal K$, using (4.3).  \(\square\)

Assign the three-signature table of Section 3 independently on every
block of this matching.  Since the blocks are top-disjoint, the word of
each used top is assigned once.  The result is an extensive decorated
top factor with

\[
                         (1-o(1)){N\over12}               \tag{4.4}
\]

literal twelve-top templates and no random signature collision.

## 5. Why this is not the coefficient-one theorem

Each packet source shore contains twelve retained rows and therefore
$12d$ middle-owner occurrences.  The factor (4.4) contains

\[
                         (1-o(1))dN=\Theta(W)              \tag{5.1}
\]

owner occurrences.  Owner collisions between different blocks are not
controlled by the top-only matching theorem.  Deleting one conflicting
row can expose $Theta(m)$ further uncovered owners, so the
$O(m^3)=o(W)$ overwrite argument used for the $O(n)$ seed bank does not
extend to (4.4).

Consequently Theorem 4.2 is an extensive decorated carrier theorem but
not yet a coefficient-one table.  The exact remaining hypergraph has

* one resource for every top;
* one resource for every middle owner; and
* one hyperedge for every three-signature source shore on an octahedral
  support.

A near-perfect matching in this mixed top--owner hypergraph would give
the desired coefficient-one extensive source layer.  Its rank is
$12(1+d)=\Theta(m)$, so the fixed-rank theorem used in Section 4 does
not apply.  This is precisely the owner-resolved growing-rank gate, not
a signature or carrier-rank gate.

## 6. Interface with row-mixed covariance

The three signature classes are stable under row mixing.  A successor
packet need not receive all twelve rows from one predecessor block; it
is enough that it receive

\[
                         4\ AB\text{-rows},\qquad
                         4\ BC\text{-rows},\qquad
                         4\ CA\text{-rows},                \tag{6.1}
\]

with the two Hamilton shores using class counts $(2,2,2)$.  Under this
condition Theorem 3.1 proves the filler-column equality independently
of predecessor identities.

Thus the signature component of RMCF$_{12}$ reduces to a three-colour
transportation constraint.  In a successor multigraph, let
$n_{B,B'}^{XY}$ be the number of rows of class $XY$ sent from predecessor
block $B$ to successor block $B'$.  The exact signature transportation
equations are

\[
 \boxed{
 \sum_B n_{B,B'}^{AB}=4,qquad
 \sum_B n_{B,B'}^{BC}=4,qquad
 \sum_B n_{B,B'}^{CA}=4.}                                 \tag{6.2}
\]

Together with one outgoing arc per row, (6.2) is a bipartite
transportation system and hence integral.  It supplies no determinant-
two or signature-level obstruction to genuine row mixing.

The unsolved covariance constraints are now the physical ones:

1. incoming rows must have a common core and the correct exterior
   top pairs;
2. unrooted cyclic words and seam necklaces must match;
3. orbitwise signs must have zero voltage and linear excursion; and
4. the initial mixed source shores must be coefficient one.

In particular, the random-signature obstruction has been removed before
the row-mixed covariance problem is attacked.

## 7. Status

Proved:

1. a one-signature coherent-order obstruction;
2. an exact three-signature filler-column identity on the repaired
   octahedron;
3. an extensive top-disjoint decorated template factor; and
4. an integral three-colour row-mixing transportation law.

Not proved:

1. owner-disjointness of the extensive factor;
2. a coefficient-one initial table containing its source shores; or
3. the full seam/voltage/core realization of RMCF$_{12}$.

This is strictly beyond the $O(n)$ seed bank: it constructs
$(1-o(1))N/12$ decorated top blocks, but it also exposes the
$\Theta(W)$ owner-resolution cost which the seed bank was designed to
avoid.
