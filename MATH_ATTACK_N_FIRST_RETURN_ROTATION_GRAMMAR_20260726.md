# Lane N: minimal rotation grammars and first-return-class mixing

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Outcome

Let \(\mathcal T_r\) be the ordered binary trees with \(r\) internal
nodes, and write

\[
T=N(L,R),\qquad
\kappa(T)=|L|+1\in[r].
\]

Under the Dyck encoding, the first return has length \(2\kappa(T)\).
The class

\[
\mathcal C_{r,j}=\{T:\kappa(T)=j\}
\]

has exact size

\[
|\mathcal C_{r,j}|
=\operatorname{Cat}_{j-1}\operatorname{Cat}_{r-j}.
\tag{0.1}
\]

The certified leaf rotation is the special Tamari associator with two
empty hanging trees.  Its first-return quotient has only the edge
\(1\leftrightarrow2\), as recorded in Section 16 of
MATH_AUDIT_PLATEAU_TRUNCATION_20260726.md.

This report gives the complete class-level answer and a minimal positive
enlargement.

1. A root associator

   \[
   N(N(A,B),C)\longleftrightarrow N(A,N(B,C))
   \]

   with \(a=|A|,b=|B|,c=|C|\) changes

   \[
   \boxed{a+b+2\longleftrightarrow a+1.}
   \tag{0.2}
   \]

   Every rotation strictly below the root preserves \(\kappa\) exactly.
   Thus merely moving the old leaf rule to more internal locations cannot
   mix any new first-return classes.

2. It is enough to release only one of the two forced-empty hangers.  The
   mirror-stable **middle-empty grammar**

   \[
   \boxed{
   N(N(A,\varnothing),C)
   \longleftrightarrow
   N(A,N(\varnothing,C))}
   \tag{M}
   \]

   has induced class graph

   \[
   \boxed{1-2-\cdots-r.}
   \tag{0.3}
   \]

   More strongly, the graph of (M) on all
   \(\operatorname{Cat}_r\) trees is connected for every \(r\).  Hence its
   edge transpositions generate
   \(\operatorname{Sym}(\mathcal T_r)\).

3. The root interface between \(j\) and \(j+1\) is a matching of exact
   size

   \[
   \boxed{
   \operatorname{Cat}_{j-1}\operatorname{Cat}_{r-j-1}.}
   \tag{0.4}
   \]

   It meets at least one quarter of each of the two adjacent classes.
   Thus (M) is not merely existentially connected at the class level.

4. If every new middle hanger must be nonempty, the smallest possible
   choice \(B=\bullet\), together with the old leaf rule, is still enough.
   Its quotient consists of

   \[
   1\leftrightarrow2,
   \qquad
   j\leftrightarrow j+2\quad(1\le j\le r-2),
   \tag{0.5}
   \]

   the two parity paths joined by \(1\leftrightarrow2\).  The full tree
   graph is again connected.  A fixed middle size \(t\ge2\) leaves a
   residue-class invariant and fails.

5. Geometric mirror synchronization of (M) connects all complementary
   pairs

   \[
   (j,r+1-j),\qquad 1\le j\le r,
   \]

   along a path, while conserving their sum \(r+1\).  However, exact
   pointwise cancellation of the two-row first-return histogram is much
   stronger: it preserves an unordered pair.  A rigid mirror pair can
   then only stay fixed or swap

   \[
   j\longleftrightarrow r+1-j.
   \]

   Hence its distance from the centre is conserved.  Complementary
   geometry alone removes the connectivity obstruction; complementary
   ledger neutrality does not.

These are tree-grammar theorems.  They do not prove that (M), its
\(B=\bullet\) variant, or their synchronized versions lift to legal exact
middle-factor packets preserving both the state and adjacent-union
ledgers.  The first new unproved exact-factor interface is the
\((a,b,c)=(1,0,0)\) associator, which connects classes
\(3\leftrightarrow2\).  Proposition 16.2 tested \((1,1,0)\), not this
minimal family.

## 1. Conventions and the general root formula

Put

\[
|\varnothing|=0,\qquad
|N(L,R)|=1+|L|+|R|.
\]

The Dyck word of a tree is recursively

\[
w(\varnothing)=\epsilon,\qquad
w(N(L,R))=1w(L)0w(R).
\tag{1.1}
\]

Thus if \(T=N(L,R)\), then its first-return decomposition is

\[
w(T)=1\,w(L)\,0\,w(R),
\]

and the semilength of its first primitive component is

\[
\kappa(T)=|L|+1.
\tag{1.2}
\]

This proves (0.1), because \(L\) and \(R\) may be chosen independently
with sizes \(j-1\) and \(r-j\).

### Theorem 1.1 (exact first-return quotient of root rotations)

Let

\[
X=N(N(A,B),C),
\qquad
Y=N(A,N(B,C)),
\tag{1.3}
\]

where

\[
a=|A|,\qquad b=|B|,\qquad c=|C|,
\qquad r=a+b+c+2.
\tag{1.4}
\]

Then

\[
\boxed{
\kappa(X)=a+b+2,\qquad
\kappa(Y)=a+1.}
\tag{1.5}
\]

Conversely, for every \(1\le i<j\le r\), the unique size triple producing
the class edge \(i\leftrightarrow j\) is

\[
\boxed{
a=i-1,\qquad
b=j-i-1,\qquad
c=r-j.}
\tag{1.6}
\]

The number of root rotations with these endpoint classes is exactly

\[
\boxed{
m_r(i,j)=
\operatorname{Cat}_{i-1}
\operatorname{Cat}_{j-i-1}
\operatorname{Cat}_{r-j}.}
\tag{1.7}
\]

Every associator applied strictly below the root is a loop on
\(\kappa\).

#### Proof

The root-left subtree of \(X\) is \(N(A,B)\), of size \(a+b+1\), while
the root-left subtree of \(Y\) is \(A\), of size \(a\).  This gives
(1.5).  Solving

\[
i=a+1,\qquad j=a+b+2,\qquad r=a+b+c+2
\]

gives (1.6).  The three hanging trees are independent, so their numbers
multiply, proving (1.7).

A proper rotation occurrence lies entirely inside the root-left subtree
or entirely inside the root-right subtree.  It preserves the size of that
subtree, and therefore preserves \(|L|+1\).  \(\square\)

### Corollary 1.2 (complete quotient taxonomy)

At fixed \(r\):

1. The old leaf rule \(A=B=\varnothing\) gives only
   \(1\leftrightarrow2\).
2. The middle-empty rule \(B=\varnothing\), with \(A,C\) arbitrary, gives
   precisely \(j\leftrightarrow j+1\), hence \(P_r\).
3. The outer-left-empty rule \(A=\varnothing\), with \(B,C\) arbitrary,
   gives precisely \(1\leftrightarrow j\), hence the star
   \(K_{1,r-1}\).
4. The symmetric rule \(C=\varnothing\) gives the star centred at \(r\).
5. Full Tamari rotations give \(K_r\).

In particular, proper internal rotations alone never enlarge the
first-return quotient.  A class conveyor must permit new root instances.

#### Proof

Substitute the indicated zero sizes in (1.5).  For the full grammar,
(1.6) realizes every pair \(i<j\).  \(\square\)

## 2. The minimal mirror-stable one-hanger grammar

Let \(\mathcal M_r\) be the graph on \(\mathcal T_r\) obtained by allowing
(M) in every tree context.  In Dyck words, (M) is

\[
\boxed{
11u00v\longleftrightarrow1u010v,}
\tag{2.1}
\]

where \(u,v\) are arbitrary Dyck words.  If \(|u|_s=a\), the root
first-return class changes

\[
a+2\longleftrightarrow a+1.
\tag{2.2}
\]

### Theorem 2.1 (the middle-empty tree graph is connected)

For every \(r\ge0\), \(\mathcal M_r\) is connected.

#### Proof

Define the left and right combs by

\[
P_0=Q_0=\varnothing,
\qquad
P_{k+1}=N(P_k,\varnothing),
\qquad
Q_{k+1}=N(\varnothing,Q_k).
\tag{2.3}
\]

We prove by strong induction on \(r\) that every \(T\in\mathcal T_r\)
is joined to \(Q_r\).  The assertion is immediate for \(r=0\).

Write

\[
T=N(L,R),\qquad |L|=\ell,\qquad |R|=r-1-\ell.
\]

By induction inside the two proper root contexts, change \(L\) to
\(P_\ell\) and \(R\) to \(Q_{r-1-\ell}\).  The middle-empty rule then
gives

\[
\begin{aligned}
N(P_\ell,Q_{r-1-\ell})
&\longleftrightarrow
N(P_{\ell-1},Q_{r-\ell})\\
&\longleftrightarrow\cdots\longleftrightarrow
N(P_0,Q_{r-1})=Q_r.
\end{aligned}
\tag{2.4}
\]

At the \(k\)-th step, use

\[
P_k=N(P_{k-1},\varnothing),
\qquad
Q_{r-k}=N(\varnothing,Q_{r-k-1}).
\]

All moves in (2.4) are instances of (M).  This completes the induction.
\(\square\)

The proof actually uses only rotations between canonical bi-combs after
the two child subtrees have been normalized.  Thus the entire set of
arbitrary \(A,C\) is not needed for connectivity.

### Corollary 2.2 (full abstract mixing)

The edge transpositions of \(\mathcal M_r\) generate

\[
\boxed{\operatorname{Sym}(\mathcal T_r).}
\tag{2.5}
\]

Consequently no nonconstant invariant of individual trees survives (M),
and every first-return class can be transported to every other class.

#### Proof

The transpositions along the edges of a connected graph generate the full
symmetric group on its vertex set.  Apply Theorem 2.1.  \(\square\)

This is abstract permutation mixing, not a quantitative mixing-time
theorem.  A lazy random walk supported on the rotation edges is
irreducible, but no spectral estimate is asserted.

## 3. Exact adjacent-class interface sizes

For \(1\le j<r\), a root instance of (M) connecting classes \(j\) and
\(j+1\) has

\[
|A|=j-1,\qquad |C|=r-j-1.
\]

### Theorem 3.1 (positive-density adjacent matching)

The root rotation edges of (M) between
\(\mathcal C_{r,j}\) and \(\mathcal C_{r,j+1}\) form a matching of size

\[
\boxed{
M_{r,j}=
\operatorname{Cat}_{j-1}\operatorname{Cat}_{r-j-1}.}
\tag{3.1}
\]

The fractions of the two classes met by this matching are respectively

\[
\boxed{
\frac{M_{r,j}}{|\mathcal C_{r,j}|}
=\frac{\operatorname{Cat}_{r-j-1}}
       {\operatorname{Cat}_{r-j}},
\qquad
\frac{M_{r,j}}{|\mathcal C_{r,j+1}|}
=\frac{\operatorname{Cat}_{j-1}}
       {\operatorname{Cat}_{j}}.}
\tag{3.2}
\]

Both fractions are at least \(1/4\).

#### Proof

Each edge is uniquely indexed by the pair \((A,C)\), giving (3.1).
The endpoint tree determines \((A,C)\), so no endpoint lies on two of
these root edges.  Divide (3.1) by (0.1).

For \(n\ge1\),

\[
\frac{\operatorname{Cat}_{n-1}}{\operatorname{Cat}_n}
=\frac{n+1}{2(2n-1)}
\ge\frac14.
\tag{3.3}
\]

This proves (3.2).  \(\square\)

At a central interface \(j\asymp r/2\),

\[
M_{r,j}=\Theta(4^r/r^3)
=\Theta(\operatorname{Cat}_r/r^{3/2}).
\tag{3.4}
\]

Thus every adjacent interface covers a constant fraction of its two
classes, but the central classes themselves have vanishing
\(\operatorname{Cat}_r\)-density.  Connectivity alone does not supply a
one-shot Catalan-scale row-disjoint conveyor through the centre.

## 4. Edge-minimal enlargements

The old class graph has components

\[
\{1,2\},\{3\},\ldots,\{r\}.
\tag{4.1}
\]

Any connected enlargement must therefore add at least \(r-2\) new class
edge types.

### Theorem 4.1 (canonical spine slides attain the minimum)

Retain the old leaf grammar and add, in arbitrary contexts, only the
canonical rotations

\[
\boxed{
N(P_{a+1},Q_c)
\longleftrightarrow
N(P_a,Q_{c+1}),
\qquad a\ge1,\ c\ge0.}
\tag{4.2}
\]

At size \(r\), this adds exactly the \(r-2\) edges

\[
2\leftrightarrow3,\ldots,r-1\leftrightarrow r.
\]

The resulting quotient is \(P_r\), and the full tree graph is connected.
Hence (4.2) is minimal in the number of new first-return edge types.

#### Proof

The move in (4.2) is the middle-empty rotation with

\[
A=P_a,\qquad B=\varnothing,\qquad C=Q_c.
\]

Its classes are \(a+2\) and \(a+1\).  At total size \(r\), the equation
\(a+c+2=r\) supplies precisely one canonical root move for each adjacent
pair from \(2\leftrightarrow3\) through
\(r-1\leftrightarrow r\).  Together with the old
\(1\leftrightarrow2\) edge, this is \(P_r\).

The induction in Theorem 2.1 first normalizes the two child subtrees to
the combs \(P_\ell,Q_{r-1-\ell}\), and then uses only the moves (4.2)
and the \(a=0\) leaf case.  It therefore proves connectivity for this
smaller grammar as well.  The lower bound \(r-2\) follows from (4.1).
\(\square\)

There is also a syntactically minimal statement.  The leaf rule fixes
both \(A=\varnothing\) and \(B=\varnothing\).  Releasing neither fails;
releasing either one succeeds:

\[
B=\varnothing,\ A\text{ arbitrary}
\quad\leadsto\quad P_r,
\]

\[
A=\varnothing,\ B\text{ arbitrary}
\quad\leadsto\quad K_{1,r-1}.
\]

The middle-empty choice is preferable for complementary synchronization,
because tree mirror preserves the condition \(B=\varnothing\).

## 5. The smallest genuinely nonempty middle hanger

Suppose every new rotation must have a nonempty middle tree.  The smallest
choice is

\[
B=\bullet=N(\varnothing,\varnothing),
\qquad |B|=1.
\]

Allow

\[
N(N(A,\bullet),C)
\longleftrightarrow
N(A,N(\bullet,C))
\tag{5.1}
\]

for arbitrary \(A,C\), together with the old leaf rule.

### Theorem 5.1 (leaf plus one-node-middle connectivity)

For every \(r\), the induced first-return graph of (5.1) and the leaf rule
is the tree with edges

\[
\boxed{
\{1,2\}\cup
\{\{j,j+2\}:1\le j\le r-2\}.}
\tag{5.2}
\]

The full graph on \(\mathcal T_r\) is connected.

#### Proof

Equation (1.5) gives displacement \(|B|+1=2\), proving (5.2).  Its
step-two edges form the odd and even paths, and the leaf edge joins them.

For full connectivity, use strong induction.  If the root-left subtree
has size \(\ell\ge2\), induction inside it changes it to a tree of the
form \(N(A,\bullet)\), for example one with any fixed \(A\) of size
\(\ell-2\).  Apply (5.1) at the root; the root-left size drops by two.
Repeat.  A remainder of size one is \(\bullet\) and is removed by the old
leaf rule; a remainder of size zero needs no move.  The root-left subtree
is now empty, and induction in the right subtree finishes at the right
comb.  \(\square\)

### Proposition 5.2 (fixed-middle residue invariant)

Fix \(t\ge0\), allow root rotations with \(|B|=t\) and arbitrary \(A,C\),
and write

\[
d=t+1.
\]

Their class edges are exactly

\[
j\longleftrightarrow j+d.
\tag{5.3}
\]

Without the leaf rule, \(j\bmod d\) is conserved.  Adding the leaf edge
\(1\leftrightarrow2\) merges only the residue classes \(1\) and \(2\).
For \(t\ge2\) and all sufficiently large \(r\), exactly \(t\) quotient
components remain.

Thus \(t=1\) is the unique fixed positive middle size which, together with
the old leaf rule, connects every first-return class uniformly in \(r\).

#### Proof

The displacement formula (1.5) is \(b+1=d\), giving (5.3).  Step-\(d\)
edges preserve residues modulo \(d\).  The extra leaf edge joins only the
two residue paths containing \(1\) and \(2\); the other \(d-2\) residue
paths remain separate.  Hence there are \(d-1=t\) components once all
residues occur.  \(\square\)

For comparison, the isolated \((a,b)=(1,1)\) shape considered in
Proposition 16.2 adds only \(2\leftrightarrow4\).  Together with the old
\(1\leftrightarrow2\), it leaves class \(3\) and every class at least
\(5\) isolated.  That failed packet therefore neither supplies nor tests
the minimal conveyor above.

## 6. Synchronized complementary rotations

Define tree mirror by

\[
\varnothing^\dagger=\varnothing,\qquad
N(L,R)^\dagger=N(R^\dagger,L^\dagger).
\tag{6.1}
\]

If \(T\in\mathcal T_r\), then

\[
\boxed{
\kappa(T^\dagger)=r+1-\kappa(T).}
\tag{6.2}
\]

Write

\[
\bar j=r+1-j.
\]

The mirror of a middle-empty rotation is again middle-empty, in the
opposite orientation:

\[
\begin{aligned}
N(N(A,\varnothing),C)^\dagger
 &=N(C^\dagger,N(\varnothing,A^\dagger)),\\
N(A,N(\varnothing,C))^\dagger
 &=N(N(C^\dagger,\varnothing),A^\dagger).
\end{aligned}
\tag{6.3}
\]

### Theorem 6.1 (geometric mirror pairs are connected)

On rigid mirror pairs \((T,T^\dagger)\), synchronized applications of (M)
have class quotient

\[
\boxed{
(1,r)-(2,r-1)-\cdots-(r,1).}
\tag{6.4}
\]

The full rigid-pair graph is isomorphic to \(\mathcal M_r\) and is
connected.  The exact pair invariant is

\[
\boxed{\kappa(T)+\kappa(T^\dagger)=r+1.}
\tag{6.5}
\]

#### Proof

The map

\[
T\longmapsto(T,T^\dagger)
\]

is a graph isomorphism from \(\mathcal M_r\) to the rigid synchronized
pair graph, by (6.3).  Apply Theorem 2.1 and (6.2).  A root adjacent move
\(j\leftrightarrow j+1\) in the first coordinate is accompanied by
\(\bar j\leftrightarrow\overline{j+1}\) in the second, giving (6.4).
\(\square\)

More generally, if two unconstrained class indices make equal and
opposite unit moves,

\[
(x,y)\longleftrightarrow(x-1,y+1),
\tag{6.6}
\]

then \(x+y\) is conserved, and each fixed-sum diagonal is a path and hence
connected.  With allowed displacements in a set \(D\), the additional
residue obstruction is the gcd of \(D\).  The presence of the
middle-empty displacement \(1\) removes that residue obstruction.

This is only sum-level synchronization.  It does not preserve the entire
pointwise class histogram.

## 7. Exact class-ledger neutrality leaves an invariant

Let \(e_1,\ldots,e_r\) be the standard basis of the first-return class
ledger.  A rigid mirror move

\[
(k,\bar k)\longrightarrow(j,\bar j)
\]

changes that two-row ledger by

\[
\boxed{
\Delta_{j,k}
=e_j+e_{\bar j}-e_k-e_{\bar k}.}
\tag{7.1}
\]

### Theorem 7.1 (rigid ledger-neutral mirror moves are only reflections)

One has \(\Delta_{j,k}=0\) if and only if

\[
j=k
\qquad\text{or}\qquad
j=\bar k.
\tag{7.2}
\]

Thus every nontrivial ledger-neutral rigid mirror move merely swaps the
two complementary classes.  It preserves

\[
\boxed{
\left|j-\frac{r+1}{2}\right|.}
\tag{7.3}
\]

Under the middle-empty adjacent grammar, the only nontrivial such edge is
the central edge when \(r\) is even; for odd \(r\) there is none.  Under
full Tamari rotations, the ledger-neutral quotient is the reflection
matching, plus the possible central singleton.

#### Proof

The equality \(\Delta_{j,k}=0\) is exactly equality of the two-element
multisets

\[
\{j,\bar j\}=\{k,\bar k\}.
\]

The two possible identifications give \(j=k\) and \(j=\bar k\).
Equation (7.3) follows.  An adjacent pair is complementary precisely when

\[
j+1=r+1-j,
\]

or \(2j=r\), which occurs only for even \(r\).  \(\square\)

For \(j<(r+1)/2\), the full-root multiplicity of the reflection edge
\(j\leftrightarrow\bar j\) is, by (1.7),

\[
\boxed{
\operatorname{Cat}_{j-1}^{\,2}
\operatorname{Cat}_{r-2j}.}
\tag{7.4}
\]

There is a general two-row form of the obstruction.

### Theorem 7.2 (unordered-pair invariant)

Let \(\chi:[r]\to[r]\) be an involution used to identify the second row's
class labels with the first, and define

\[
\Lambda_\chi(x,y)=e_x+e_{\chi(y)}.
\tag{7.5}
\]

If a nonidentity two-row move

\[
(x,y)\longrightarrow(x',y')
\]

preserves \(\Lambda_\chi\), then

\[
\boxed{
(x',y')=(\chi(y),\chi(x)).}
\tag{7.6}
\]

Equivalently, the unordered pair

\[
\boxed{\{x,\chi(y)\}}
\tag{7.7}
\]

is conserved.  A fixed pair can visit at most two ordered states.

#### Proof

Equality of (7.5) before and after is equality of two two-element
multisets.  Besides the identity matching, the only matching crosses the
two entries:

\[
x'=\chi(y),\qquad
\chi(y')=x.
\]

Since \(\chi^2=\mathrm{id}\), this is (7.6).  \(\square\)

Dynamic re-pairing can move a tagged row through successive swaps, but the
global class histogram remains fixed.  It cannot by itself transfer mass
from the Catalan-heavy boundary classes to the central classes.

Without exact cancellation, arbitrary mirror-synchronized moves preserve
all antisymmetric differences

\[
h_j-h_{\bar j}
\tag{7.8}
\]

and the parity of every mirror-orbit total

\[
h_j+h_{\bar j}\pmod2.
\tag{7.9}
\]

These follow immediately from (7.1), which adds or removes mirror pairs.
They do not prevent a tagged complementary pair from traversing (6.4),
but they are genuine global histogram invariants.

## 8. Uniform obstructions to smaller fixed grammars

### Proposition 8.1 (bounded root shapes cannot mix uniformly)

Suppose every permitted nonloop root rotation satisfies

\[
|A|+|B|\le M
\]

for a constant \(M\).  Then every class \(j>M+2\) is isolated in the
first-return quotient.  Hence no finite list of fixed local rotation
shapes connects all classes as \(r\to\infty\).

#### Proof

By (1.5), the upper endpoint of every class edge is

\[
a+b+2\le M+2.
\]

Proper internal rotations are loops by Theorem 1.1.  \(\square\)

Thus a uniform conveyor needs an unbounded hanging subtree, as in (M), or
a synchronized macro-operation whose support grows with \(r\).

If all three hanging trees \(A,B,C\) are required to be nonempty, then

\[
a+1\ge2,\qquad
a+b+2\le r-1.
\]

Classes \(1\) and \(r\) are frozen, so that grammar is disconnected for
every relevant \(r\).

## 9. Exact-factor implication boundary

The report proves:

1. the exact quotient formula (1.5)--(1.7);
2. invariance of first-return class under every proper internal rotation;
3. connectivity of the entire Catalan tree graph under the one-hanger
   grammar (M);
4. a positive-density matching at every adjacent class interface;
5. edge-minimal connectivity after adding only the canonical spine
   slides;
6. connectivity under the leaf-plus-\(B=\bullet\) grammar and the sharp
   fixed-middle residue obstruction;
7. connected geometric mirror synchronization; and
8. the unordered-pair obstruction under exact two-row class-ledger
   neutrality.

It does **not** prove that any new associator is a legal exact-factor
switch.  Let

\[
\Gamma=
\mathbb Z^{\binom{\Omega}{m}}
\oplus
\mathbb Z^{\binom{\Omega}{m+1}}
\tag{9.1}
\]

be the state and adjacent-union ledger group, and let
\(\Delta\in\Gamma\) be the discrepancy of one proposed associator packet.
If \(\tau\) is the coordinate action induced by a complementary hole, an
oppositely oriented synchronized pair has discrepancy

\[
\boxed{\Delta-\tau_*\Delta.}
\tag{9.2}
\]

It cancels only if

\[
\tau_*\Delta=\Delta.
\tag{9.3}
\]

The class-sum identity (6.5) implies no such equality.  Phasewise Johnson
path legality is another independent condition.

Accordingly, the sharp next exact-factor theorem is:

> **Middle-empty associator packet gate (unproved).**  Realize (M), or at
> least the canonical spine slides (4.2), in arbitrary aligned contexts by
> a finite exact packet preserving both ownership ledgers and all boundary
> states.

If this gate is proved, Theorem 2.1 supplies a genuine Catalan conveyor:
the local rotation graph is connected, its edge transpositions generate
the full symmetric group, and the old first-return normal-form invariant
disappears.  If only two-row pointwise ledger-neutral complementary
packets are allowed, Theorems 7.1--7.2 show that route cannot reshape the
first-return profile without dynamic re-pairing or packets of at least
three rows.

The decisive new interface is

\[
\boxed{
N(N(\bullet,\varnothing),\varnothing)
\longleftrightarrow
N(\bullet,N(\varnothing,\varnothing)),}
\tag{9.4}
\]

the \((1,0,0)\) rotation from class \(3\) to class \(2\).  It is the first
move not present in the certified leaf grammar and is not ruled out by
the failed \((1,1,0)\) two-bracketing packet.
