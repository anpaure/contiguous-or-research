# The `D_3` conjugate current square closes algebraically but is not a simple factor trade

**Date:** 2026-08-06  
**Method:** pure mathematics; literal cancellation of the four conjugate
inverse-pair rows and their central-owner windows  
**Status:** unconditional obstruction for the fixed-slot
`<(2 3),(4 5)>` square.  The square has zero complete all-width current and
a nontrivial residual row action, but each of four central owners occurs
with multiplicity three on both sides.  It therefore cannot be planted as
a simple partial factor.  This does not exclude a split-row realization,
a later-slot circuit, or an exterior owner absorber.

## 1. The four conjugate moves

Put

\[
                         X=(V,\infty),\qquad Y=(1,U,6),
\tag{1.1}
\]

where `U,V` are the common suffix banks; the base case is obtained by
taking them empty.  For four distinct active labels `a,b,c,d`, write the
native inverse-pair move as

\[
\begin{array}{rcl}
 (a,b,X,c,d,Y),&(b,d,X,a,c,Y)\\[1mm]
 &\longleftrightarrow&\\[-3mm]
 (b,a,X,d,c,Y),&(d,b,X,c,a,Y).
\end{array}
\tag{1.2}
\]

Let `Delta(a,b,c,d)` denote new minus old in (1.2).  The persistent
negative edge `12` is `Delta(4,5,2,3)`.  Its orbit under

\[
                        H=\langle(2\ 3),(4\ 5)\rangle
\tag{1.3}
\]

consists of

\[
 \Delta(4,5,2,3),\quad \Delta(4,5,3,2),\quad
 \Delta(5,4,2,3),\quad \Delta(5,4,3,2).
\tag{1.4}
\]

Consider the alternating orbit square

\[
 \mathcal K=
 \Delta(4,5,2,3)-\Delta(4,5,3,2)
 -\Delta(5,4,2,3)+\Delta(5,4,3,2).
\tag{1.5}
\]

## 2. Its complete current is zero

The all-width current of (1.2) is

\[
                         \mathcal D_j(X,Y;a,d),
\tag{2.1}
\]

in the notation of
`MATH_THEOREM_D3_PENTAGON_PERSISTENT_EDGE_ALL_WIDTH_CURRENT_OBSTRUCTION_20260806.md`.
For fixed ordered banks `X,Y`, it is a difference of endpoint potentials:

\[
                         \mathcal D_j(X,Y;a,d)
                           =F_j(a)-F_j(d).
\tag{2.2}
\]

Consequently the current of (1.5) is, at every width `j`,

\[
 \mathcal D_j(4,3)-\mathcal D_j(4,2)
 -\mathcal D_j(5,3)+\mathcal D_j(5,2)=0.
\tag{2.3}
\]

Thus the rectangle is a genuine complete-current identity.  Unlike a
pairwise cancellation, it closes all proper widths simultaneously.

## 3. Literal row cancellation

Expanding (1.5) and cancelling identical rows leaves the following four
positive and four negative cyclic orders:

\[
\begin{array}{c|c}
\text{positive}&\text{negative}\\ \hline
(3,5,X,2,4,Y)&(5,3,X,4,2,Y)\\
(5,2,X,4,3,Y)&(2,5,X,3,4,Y)\\
(4,3,X,5,2,Y)&(3,4,X,2,5,Y)\\
(2,4,X,3,5,Y)&(4,2,X,5,3,Y).
\end{array}
\tag{3.1}
\]

The residual is not the zero row multiset.  The ordered block `X` fixes
the displayed alignment, and the four ordered active frames on the two
sides differ.  Reversal cannot identify them either: it interchanges the
two disjoint blocks `X,Y`, whose lengths differ by one.  Hence (3.1) has a
nontrivial formal row action.

## 4. The central-owner multiplicity is exactly three

Put `m=|X|+2`.  A row

\[
                         (a,b,X,c,d,Y)
\tag{4.1}
\]

has three consecutive rank-`m` windows containing the whole block `X`:

\[
                         X+ab,\qquad X+bc,\qquad X+cd.
\tag{4.2}
\]

For the four negative rows of (3.1), the three active pairs are

\[
\begin{array}{c|c}
53X42&53,34,42\\
25X34&25,53,34\\
34X25&34,42,25\\
42X53&42,25,53.
\end{array}
\tag{4.3}
\]

Therefore each member of

\[
                         \{X+53,X+34,X+42,X+25\}
\tag{4.4}
\]

occurs in exactly three negative rows.  The positive table gives

\[
\begin{array}{c|c}
35X24&35,52,24\\
52X43&52,24,43\\
43X52&43,35,52\\
24X35&24,43,35,
\end{array}
\tag{4.5}
\]

which is the same unordered owner family (4.4), again with multiplicity
three.

### Theorem 4.1 (owner-capacity obstruction)

The zero-current square (1.5) is not a simple exact partial-factor trade in
any suffix depth.  Each side uses four distinct central owners three times
each, whereas a simple factor has owner capacity one.

#### Proof

Equations (4.3)--(4.5) give the claimed multiplicities.  The four owners
are distinct because `X` is disjoint from the four active labels and the
four active pairs are distinct.  A simple owner factor cannot contain even
two, much less three, occurrences of one owner.  The calculation is
independent of `|U|=|V|`, so common-tail suspension does not remove the
collision. \(\square\)

## 5. Exact implication

The orbit rectangle solves the **linear current equation** but not the
**physical packing equation**:

\[
 \boxed{
 \text{zero all-width current}
 \quad\not\Longrightarrow\quad
 \text{simple occurrence-labelled trade}.}
\tag{5.1}
\]

Any realization based on this rectangle must add at least one genuinely
new ingredient: split the colliding rows into owner-disjoint fragments,
move some sides of the square to dynamically exposed slots with different
owner supports, or include an external owner-capacity absorber.  Merely
tensoring the four fixed conjugates preserves the multiplicity-three
obstruction.
