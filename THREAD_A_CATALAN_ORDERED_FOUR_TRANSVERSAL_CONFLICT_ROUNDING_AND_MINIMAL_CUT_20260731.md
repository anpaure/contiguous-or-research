# Ordered four-transversals: conflict-graph rounding and the first exact cut

Date: 2026-07-31  
Status: exact conditional integrality theorem and an exact support-minimal
polyhedral obstruction.  The Catalan Linear Matching Theorem is not proved.

## 1. Oriented atoms and their conflict graph

Let \(|\Omega|=2m\), and use

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal X=\binom\Omega m,\qquad
 \mathcal U=\binom\Omega{m+1},
\]

\[
 N=|\mathcal L|=|\mathcal U|=m\operatorname {Cat}_m.
\]

An **oriented diamond atom** is a quadruple

\[
             a=(L,U,T,H)                                      \tag{1.1}
\]

where \(L\subset T,H\subset U\), \(|U\setminus L|=2\), and
\(T\ne H\).  Thus \(L=T\cap H\), \(U=T\cup H\), and the atom is the
directed Johnson edge \(T\to H\).

For a catalogue \(\mathcal A\) of oriented atoms, its **four-resource
conflict graph** \(\Gamma(\mathcal A)\) has vertex set \(\mathcal A\).
Two atoms are adjacent exactly when they have a common lower colour, a
common upper colour, a common tail, or a common head.  Hence an independent
set in \(\Gamma(\mathcal A)\) is precisely a partial ordered
four-transversal.

Call \(\mathcal A\) **order-monotone** if there is a real-valued function
\(\phi\) on \(\mathcal X\) such that

\[
                         \phi(T)<\phi(H)                       \tag{1.2}
\]

for every \((L,U,T,H)\in\mathcal A\).

## 2. A positive integral rounding theorem

### Theorem 2.1 (bipartite-conflict rounding)

Suppose \(\mathcal A\) is order-monotone and
\(\Gamma(\mathcal A)\) is bipartite.  Suppose there are nonnegative
weights \(y_a\) satisfying

\[
\begin{aligned}
 \sum_{a:L(a)=L}y_a&=1 &&(L\in\mathcal L),\\
 \sum_{a:U(a)=U}y_a&=1 &&(U\in\mathcal U),\\
 \sum_{a:T(a)=X}y_a&\le1 &&(X\in\mathcal X),\\
 \sum_{a:H(a)=X}y_a&\le1 &&(X\in\mathcal X).
                                                               \tag{2.1}
\end{aligned}
\]

Then \(\mathcal A\) contains an ordered four-transversal of size \(N\).
Consequently the corresponding diamonds form a perfect lower--upper
matching whose physical lift is a spanning
\(\operatorname {Cat}_m\)-path forest.

#### Proof

If two atoms are adjacent in \(\Gamma(\mathcal A)\), one row of (2.1)
contains both, and therefore

\[
                             y_a+y_b\le1.                       \tag{2.2}
\]

The edge--vertex incidence matrix of a bipartite graph is totally
unimodular (after signing one vertex bipartition, it is an oriented
incidence matrix).  Hence the
polytope

\[
 0\le z_a\le1,\qquad
 z_a+z_b\le1\quad(ab\in E(\Gamma))                             \tag{2.3}
\]

is integral.  Equivalently, every fractional stable set in a bipartite
graph is dominated in total weight by an integral stable set.  Applying
this with unit objective to \(y\), there is an independent set \(I\) with

\[
 |I|\ge\sum_{a\in\mathcal A}y_a
      =\sum_{L\in\mathcal L}\sum_{a:L(a)=L}y_a=N.              \tag{2.4}
\]

Atoms with the same lower colour form a clique, so an independent set has
at most one atom over each of the \(N\) lower colours.  Thus \(|I|\le N\),
and equality holds.  Equality forces every lower colour to occur once.
The identical argument on the upper shore forces every upper colour to
occur once.  Independence gives distinct tails and distinct heads.

The selected directed graph has indegree and outdegree at most one.  It
has no directed cycle because \(\phi\) strictly increases on every
selected arc.  In a graph of indegree and outdegree at most one, every
undirected cycle is directed consistently, so the underlying physical
graph is acyclic.  It has \(N\) edges on
\(|\mathcal X|=N+\operatorname {Cat}_m\) vertices and is therefore a
spanning forest of exactly \(\operatorname {Cat}_m\) paths, with isolated
vertices allowed. \(\square\)

The theorem is a genuine rounding statement: within this support, no
graphic inequalities are needed.  What is not known is how to choose an
order-monotone catalogue supporting (2.1) whose conflict graph is
bipartite.  The complete Boolean catalogue does not have this property.

### Corollary 2.2 (perfect-conflict rounding)

The word `bipartite' in Theorem 2.1 may be replaced by `perfect' provided
the fractional point satisfies

\[
                         \sum_{a\in Q}y_a\le1                  \tag{2.5}
\]

for every clique \(Q\) of \(\Gamma(\mathcal A)\).  In particular, the
four resource rows alone suffice whenever \(\Gamma(\mathcal A)\) is
perfect and every clique is contained in one resource class.

Indeed, the stable-set polytope of a perfect graph is exactly the
nonnegative polytope cut out by its clique inequalities.  It therefore
has an integral optimum of value at least \(\sum_a y_a=N\); the size bound,
palette saturation, and acyclicity argument from Theorem 2.1 are unchanged.
This corollary identifies a concrete rounding programme: construct a
perfect order-monotone support and certify its non-Helly clique rows.  It
does not assert that the complete Boolean conflict graph is perfect.

## 3. The first oriented correlation cut is a literal Boolean triangle

### Proposition 3.1 (non-Helly conflict triangle)

For every \(m\ge2\), the complete oriented-diamond catalogue contains
three atoms which are pairwise conflicting but have no common resource.
Consequently the four resource rows in (2.1) do not imply the valid clique
inequality for these three atoms.

#### Proof

Fix \(X\in\binom\Omega m\), distinct \(p,s\in X\), and distinct
\(q,r\in\Omega\setminus X\).  Put

\[
\begin{aligned}
 a_1&=(X-p,\ X+q,\ X,\ X-p+q),\\
 a_2&=(X-p,\ X+r,\ X-p+r,\ X),\\
 a_3&=(X-s,\ X+r,\ X,\ X-s+r).                       \tag{3.1}
\end{aligned}
\]

Each line is an oriented Boolean diamond.  The pair \(a_1,a_2\) shares
the lower colour \(X-p\); the pair \(a_2,a_3\) shares the upper colour
\(X+r\); and the pair \(a_3,a_1\) shares the tail \(X\).  There is no
resource common to all three, and all other displayed resources are
distinct.  Thus every integral partial four-transversal satisfies

\[
                         y_{a_1}+y_{a_2}+y_{a_3}\le1.           \tag{3.2}
\]

But \(y_{a_i}=1/2\) satisfies every individual lower, upper, tail, and
head row: the three shared rows have load one and every other row has load
one half.  Hence (3.2) is not implied by (2.1). \(\square\)

The three underlying unoriented Johnson edges form a star at \(X\), so
their half-weight vector also violates no physical graphic inequality and
has middle load \(3/2\).  Inequality (3.2) is nevertheless an
**orientation-level** cut: the two underlying edges of \(a_1,a_3\) may
coexist if one is oriented toward \(X\).  It must not be advertised as a
new inequality in the unoriented system of
`MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md`.

Among occurrence-resource cuts, (3.2) is support-minimal.  A one-atom
inequality is only \(0\le y_a\le1\), already implied by any one of its
resource rows; two conflicting atoms are already controlled by their
shared row.  Three pairwise conflicts with three different resource rows
are the first possible non-Helly clique.

## 4. A support-minimal cut in the original unoriented polytope

The orientation triangle does not settle whether matching, cap-two, and
all graphic inequalities describe the convex hull of unoriented Catalan
linear matchings.  Already \(m=2\) gives an exact negative answer.

Let \(\Omega=\{0,1,2,3\}\).  Write

\[
 L_i=\{i\},\qquad U_j=\Omega\setminus\{j\},
\]

and let \(e_{ij}=(L_i,U_j)\), defined for \(i\ne j\).  A perfect diamond
matching is a derangement \(\pi\in S_4\), selecting \(e_{i,\pi(i)}\).

### Proposition 4.1 (reciprocal-completion inequality)

For every distinct \(i,j\), every Catalan linear perfect matching at
\(m=2\) satisfies

\[
                              x_{ij}+x_{ji}\le1.                \tag{4.1}
\]

This inequality is not implied by the complete system (3.1) of
`MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md`.
Moreover, it has minimum possible column support among strict valid
inequalities not already forced one column at a time.

#### Proof of validity

If a derangement contains both \(i\mapsto j\) and \(j\mapsto i\), then
on the two remaining letters \(k,l\) bijectivity and the forbidden fixed
points force \(k\mapsto l\) and \(l\mapsto k\).  Thus the derangement is
a product of two transpositions.  By coordinate symmetry it suffices to
inspect

\[
                    P=(01)(23).                              \tag{4.2}
\]

Its four lifted edges are

\[
 02{-}03,\qquad 12{-}13,\qquad 02{-}12,\qquad 03{-}13,         \tag{4.3}
\]

which form the four-cycle

\[
                         02-03-13-12-02.                       \tag{4.4}
\]

Hence it is not a linear forest.  This proves (4.1).

#### Proof that (4.1) is new

Let \(u_e=1/3\) on every one of the twelve edges of the crown graph
\(B_2\), and let \(\chi^P\) be the incidence vector of (4.2).  Define

\[
                         x={1\over2}\chi^P+{1\over2}u.          \tag{4.5}
\]

Both summands satisfy the lower and upper matching equalities, so does
\(x\).  The lift of \(P\) has physical degrees zero or two, while the
uniform point has physical load \(4/3\); hence the cap-two rows hold.

It remains to check every graphic row.  Let

\[
                       W=\{02,03,12,13\}.                      \tag{4.6}
\]

The only graphic inequality violated by \(\chi^P\) is the row on exactly
\(W\): a proper induced subgraph of its four-cycle is a forest, and adding
either isolated physical vertex gives a set of size at least five and so
restores the rank bound.  The Johnson graph induced by \(W\) is precisely
the same four-cycle, so

\[
 x(E(W))={1\over2}\,4+{1\over2}\,{4\over3}
         ={8\over3}<3=|W|-1.                                \tag{4.7}
\]

Every other graphic row holds by convexity, since both summands satisfy
that row.  Therefore \(x\) satisfies the complete matching, cap-two, and
graphic system.

But \(P\) contains \(e_{01},e_{10}\), while the uniform point gives each
of them weight \(1/3\).  Thus

\[
                         x_{01}+x_{10}={4\over3}>1,             \tag{4.8}
\]

so (4.1) is not implied.

Finally, every single diamond \(e_{ij}\) belongs to a four-cycle
derangement, and all four-cycle derangements have linear-forest lifts
(check \((0123)\), then conjugate by a coordinate permutation).  Therefore
the maximum feasible value of each individual variable is one, exactly
the existing matching bound.  No strict one-column valid inequality
exists, while (4.1) uses two columns. \(\square\)

For completeness, the representative four-cycle derangement \((0123)\)
lifts to

\[
 02{-}03,\quad 01{-}13,\quad 02{-}12,\quad 13{-}23,            \tag{4.9}
\]

which is the disjoint union of two two-edge paths and two isolated
vertices.  Thus the last symmetry assertion in the proof is literal.

### Corollary 4.2 (dimension-uniform four-shore escape cut)

The reciprocal obstruction occurs as an exact local completion circuit in
every dimension.  Choose pairwise disjoint sets

\[
                    \Omega=C\sqcup A\sqcup R,
 \qquad |C|=|R|=m-2,\quad |A|=4.                       \tag{4.10}
\]

For \(i,j\in A\), put

\[
             L_i=C\cup\{i\},\qquad
             U_j=C\cup(A\setminus\{j\}).               \tag{4.11}
\]

Then \(L_i\subset U_j\) exactly when \(i\ne j\).  Let

\[
 \eta_C(x)=
 \sum_{i\in A}\ \sum_{\substack{U\supset L_i\\
                         U\notin\{U_j:j\in A\}}}x_{L_i,U}.     \tag{4.12}
\]

For every integral Catalan linear perfect matching and every distinct
\(i,j\in A\),

\[
                         x_{L_i,U_j}+x_{L_j,U_i}
                         \le 1+\eta_C(x).                       \tag{4.13}
\]

Indeed, if \(\eta_C(x)\ge1\), (4.13) is immediate from the individual
upper bounds.  If \(\eta_C(x)=0\), the four active lower colours are
matched injectively into the four active upper colours, hence bijectively.
Selecting the reciprocal pair \(L_iU_j,L_jU_i\) forces the two remaining
active colours to form the other reciprocal pair.  Their four physical
edges lie on the six middle vertices

\[
                    \{\,C\cup B:B\in\tbinom{A}{2}\,\}         \tag{4.14}
\]

and, after deleting the common core \(C\), are exactly the four-cycle
(4.4).  This contradicts linearity.

By perfect-matching flow across the equal four-vertex shores, the number
of active lower vertices matched outward equals the number of active upper
vertices matched inward.  Thus (4.12) may equivalently be written using
upper-shore incoming escape edges.  At \(m=2\), \(C=R=\varnothing\) and
there are no escape edges, so (4.13) reduces exactly to (4.1).  No claim is
made here that (4.13), for fixed \(m>2\), is independent of every row of
(3.1); the proved non-implication is the \(m=2\) member.

## 5. Exact boundary of the result

Theorem 2.1 is a valid integral rounding theorem, but no suitable
bipartite, order-monotone support is presently constructed for all \(m\).
Proposition 3.1 shows why the complete oriented catalogue cannot be rounded
from the four marginal resource rows alone.  Proposition 4.1 is stronger
at the projection level: even matching, all middle cap-two rows, and the
complete graphic-forest system leave a fractional point outside the
Catalan-linear-matching hull.

Accordingly, the global quotient perfect matching removes outer-palette
Hall but does not imply an integral ordered four-transversal.  A successful
rounding theorem must add genuine correlation information.  The first
such information is:

* non-Helly clique cuts such as (3.2) in an occurrence-oriented model; and
* completion cuts such as (4.1) after projecting to unoriented diamonds.

No claim is made that these cuts suffice in higher dimension, and no
projection-edit bound from the retracted Greene--Kleitman estimate is used.
