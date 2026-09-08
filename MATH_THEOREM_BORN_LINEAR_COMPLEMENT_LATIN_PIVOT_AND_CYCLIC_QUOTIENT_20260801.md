# Complement Latinization of \(Q_0\), protected pivot cells, and the clean cyclic quotient

Date: 2026-08-01  
Lane: joint \(M_0/Q_0\) construction / Latin transversal / cyclic rules  
Status: exact equivalence, exact fractional theorem, exact quotient reduction,
one positive base, and three sharp rule-family obstructions.  No all-\(m\)
integral Latin forest is claimed.

## 0. Outcome

Let \(|\Omega|=2m-1\), and put

\[
 \mathcal C=\binom{\Omega}{m-2},\qquad
 \mathcal B=\binom{\Omega}{m-1},\qquad
 \mathcal D=\binom{\Omega}{m}.                         \tag{0.1}
\]

The rooted upper-exact Catalan-forest problem has the following exact
prospective form.

1. Choose the first incidence matching jointly as a perfect matching
   \[
                  \mu:\mathcal B\longrightarrow\mathcal D,
                  \qquad B\subset\mu(B).
   \]
2. Put \(\alpha(B)=\mu(B)-B\).  For a row \(C\subset B=C+\{b\}\), define
   the symbol
   \[
                         A_\mu(C,B)=C+\{\alpha(B)\}.
   \]
3. Choose one cell in every row, with columns and symbols both injective,
   and require the directed column-to-symbol graph to be acyclic.

Complementation turns this selected partial Latin transversal exactly into
\(Q_0\).  The tight pivot is already a prescribed directed path in the
table when the predecessor phase of \(\mu\) is chosen.

For every fixed \(\mu\), the uniform cell weight \(1/(m+1)\) satisfies all
row, column, symbol, and graphic-forest inequalities.  Thus the surviving
gate is purely integral correlation.

There is also an exact clean cyclic quotient.  The maximal subgroup of
\(\mathbb Z_{2m-1}\) whose order is prime to three acts freely on all four
needed ranks; its quotient always admits the matching \(\mu\).  The remaining
problem is a quotient Latin matching whose voltage graph is a forest.

Three simple rules are ruled out sharply.

* Every translation-covariant affine-linear point rule fails incidence
  legality for all \(m\ge4\).
* Requiring every row to be Latin would force a Steiner
  \(S(m-2,m-1,2m-2)\), impossible for every even \(m\ge4\).
* Full rotation equivariance fails whenever \(m\equiv2\pmod3\).

At \(m=3\) there is an explicit cyclic positive base.

## 1. Exact complement Latinization

Start in the original middle-levels graph between ranks \(m-1\) and \(m\)
of \(\Omega\).  Let \(M_0\) be a perfect incidence matching.  Complementing
both endpoints gives a perfect incidence matching

\[
                  \mu:\mathcal B\longrightarrow\mathcal D.       \tag{1.1}
\]

For \(B\in\mathcal B\), write

\[
                         \mu(B)=B+\alpha(B).            \tag{1.2}
\]

In particular \(\alpha(B)\notin B\).

For every flag \(C\subset B\), where \(C\in\mathcal C\) and
\(B=C+\{b\}\), define

\[
                         A_\mu(C,B)=C+\{\alpha(B)\}.    \tag{1.3}
\]

Then \(A_\mu(C,B)\in\mathcal B\), \(A_\mu(C,B)\ne B\), and

\[
        C=A_\mu(C,B)\cap B,\qquad
        \mu(B)=A_\mu(C,B)\cup B.                       \tag{1.4}
\]

### Theorem 1.1 (Latin-forest equivalence)

The following are equivalent.

1. A perfect first matching \(M_0\) and a rooted upper-exact Catalan forest
   \(Q_0\).
2. A perfect matching \(\mu\) as in (1.1) and a row-saturating selection
   \[
                         \sigma:\mathcal C\longrightarrow\mathcal B,
                         \qquad C\subset\sigma(C),      \tag{1.5}
   \]
   such that
   * \(\sigma\) is injective;
   * \(C\mapsto A_\mu(C,\sigma(C))\) is injective; and
   * the directed graph
     \[
                    \sigma(C)\longrightarrow
                    A_\mu(C,\sigma(C))                 \tag{1.6}
     \]
     is acyclic.

The selected graph has

\[
 |\mathcal C|=\binom{2m-1}{m+1}=U                    \tag{1.7}
\]

edges on

\[
 |\mathcal B|=\binom{2m-1}{m}=W                      \tag{1.8}
\]

vertices and therefore exactly

\[
                         W-U=\operatorname {Cat}_m     \tag{1.9}
\]

components.

#### Proof

Take one upper colour \(R\in\binom{\Omega}{m+1}\) and put
\(C=\Omega-R\in\mathcal C\).  A representative edge of \(Q_0\) has two
owner endpoints

\[
                         T=L+\{a\},\qquad V=L+\{b\},
                         \qquad R=L+\{a,b\}.            \tag{1.10}
\]

Assume \(M_0(L)=T\).  Put

\[
                         B=\Omega-T=C+\{b\},\qquad
                         A=\Omega-V=C+\{a\}.            \tag{1.11}
\]

Complementing the matched incidence \(L\subset T\) gives

\[
                         \mu(B)=\Omega-L=C+\{a,b\},
                         \qquad \alpha(B)=a,            \tag{1.12}
\]

so \(A=A_\mu(C,B)\).

Under the rooted identification induced by \(M_0\), the tail root \(L\) is
represented by \(B=\Omega-M_0(L)\), while the head root
\(M_0^{-1}(V)\) is represented by \(A=\Omega-V\).  Hence the rooted link is
exactly \(B\to A\).

Choosing one edge for every upper colour is choosing one cell for every
row \(C\).  Distinct lower endpoints of \(Q_0\) are distinct columns
\(B\), and distinct owner endpoints are distinct symbols \(A\).  Graphic
acyclicity is exactly acyclicity of (1.6).  This proves \(1\Rightarrow2\).

All formulas reverse: from a cell \((C,B,A)\), put

\[
 T=\Omega-B,\qquad V=\Omega-A,\qquad L=\Omega-\mu(B).
\]

Equation (1.4) gives \(L=T\cap V\) and \(T\cup V=\Omega-C\), while
\(\mu\) defines \(M_0(L)=T\).  Thus every selected cell becomes one
\(Q_0\) incidence of the required upper colour.  Injectivity and
acyclicity give the matching and forest rows.  This proves \(2\Rightarrow1\).
The component count is (1.7)--(1.9).  \(\square\)

This is a partial Latin transversal, not a complete Latin square: there are
\(U\) rows but \(W>U\) columns and symbols.

## 2. The tight pivot is a prescribed Latin path

Let

\[
                         V_0,V_1,\ldots,V_\ell          \tag{2.1}
\]

be a simple Johnson owner path with distinct consecutive lower and upper
colours.  Put

\[
 B_i=\Omega-V_i,\qquad
 C_i=B_i\cap B_{i+1},\qquad
 D_i=B_i\cup B_{i+1}.                                  \tag{2.2}
\]

Choose the predecessor phase

\[
                         \mu(B_i)=D_i
                         \qquad(0\le i<\ell).           \tag{2.3}
\]

### Theorem 2.1 (protected path cells)

Under (2.3), the selected cell

\[
                         (C_i,B_i)
\]

has symbol

\[
                         A_\mu(C_i,B_i)=B_{i+1}.        \tag{2.4}
\]

Hence the pivot cells form the literal directed path

\[
                         B_0\to B_1\to\cdots\to B_\ell. \tag{2.5}
\]

The prescribed rows, columns, symbols, and matched values \(D_i\) are all
distinct.  If \(\ell\le m-1\), the partial matching (2.3) extends to a
perfect \(\mu\).

#### Proof

Because \(B_i,B_{i+1}\) are adjacent,

\[
 D_i-B_i=B_{i+1}-B_i.
\]

Thus (2.3) gives

\[
 \alpha(B_i)=B_{i+1}-B_i,
\]

and adjoining this point to \(C_i=B_i\cap B_{i+1}\) proves (2.4).
Distinct original owners give distinct \(B_i\); distinct original upper and
lower transition colours give distinct \(C_i,D_i\).  The protected
small-matching extension theorem supplies the perfect extension when
\(\ell\le m-1\).  \(\square\)

For the tight pivot, \(\ell=3d=O(\sqrt m)\), and the established prospective
planting range implies the matching extension bound.  The remaining problem
is extension of this partial Latin path to the complete row transversal,
not its local phase.

## 3. Uniform fractional Catalan forest for every fixed \(\mu\)

Give every table cell \((C,B,A_\mu(C,B))\) weight

\[
                              x_e={1\over m+1}.          \tag{3.1}
\]

### Theorem 3.1

For every perfect \(\mu\), the vector (3.1) satisfies:

1. every row equation with equality one;
2. every column capacity with load \((m-1)/(m+1)\);
3. every symbol capacity with load at most \(m/(m+1)\); and
4. every graphic-forest inequality
   \[
                              x(E(Y))\le |Y|-1
                              \qquad(\varnothing\ne Y\subseteq\mathcal B).
                                                               \tag{3.2}
   \]

Thus all scalar, endpoint, and graphic LP rows are feasible for every
choice of the first matching.  The obstruction is integral
row/column/symbol/graphic correlation.

#### Proof

A row \(C\) has \(m+1\) extensions \(B=C+\{b\}\), giving load one.  A
column \(B\) contains \(m-1\) rows, giving the displayed column load.

Fix a symbol \(A\).  An occurrence \(B\to A\) satisfies

\[
                         \mu(B)=A+\{y\}
\]

for one \(y\notin A\).  For each of the \(m\) choices of \(y\), bijectivity
of \(\mu\) gives at most one \(B\).  Hence the symbol degree is at most
\(m\).

The cell digraph has no loop by \(\alpha(B)\notin B\).  It has at most one
edge on an unordered pair \(\{A,B\}\): a cell determines
\(C=A\cap B\) and \(\mu(B)=A\cup B\), while opposite cells would force
\(\mu(A)=\mu(B)=A\cup B\).

For \(s=|Y|\), simplicity gives

\[
                  x(E(Y))\le{\binom s2\over m+1},      \tag{3.3}
\]

which is at most \(s-1\) when \(s\le2(m+1)\).  The total outgoing cell
degree of a column is \(m-1\), so also

\[
                  x(E(Y))\le{(m-1)s\over m+1},         \tag{3.4}
\]

which is at most \(s-1\) when \(2s\ge m+1\).  The two ranges cover every
positive integer \(s\), proving (3.2).  \(\square\)

## 4. The exact clean cyclic quotient

Let \(n=2m-1\) and let \(G\le\mathbb Z_n\) have order \(g\) satisfying

\[
                 \gcd\bigl(g,(m-2)(m-1)m\bigr)=1.      \tag{4.1}
\]

The canonical maximal choice is

\[
                         g={n\over3^{v_3(n)}}.          \tag{4.2}
\]

Then \(G\) acts freely on \(\mathcal C,\mathcal B,\mathcal D\).  The
quotient of the \(\mathcal B\)--\(\mathcal D\) incidence graph is an
\(m\)-regular balanced bipartite multigraph.

### Theorem 4.1 (cyclic prospective reduction)

For every clean subgroup \(G\):

1. there exists a \(G\)-equivariant perfect matching \(\mu\);
2. relative to such a \(\mu\), a \(G\)-invariant rooted upper-exact Catalan
   forest is equivalent to selecting atom orbits so that
   * every row orbit is used exactly once;
   * every column and symbol orbit is used at most once; and
   * the voltage-labelled quotient digraph \(B\to A\) is loopless and
     acyclic;
3. a quotient forest lifts to a physical forest, while every quotient
   cycle, including a loop of nonzero voltage, lifts to physical cycles; and
4. the quotient forest has
   \[
             {U\over g}\text{ edges on }{W\over g}\text{ vertices and }
             {\operatorname {Cat}_m\over g}\text{ components}.   \tag{4.3}
   \]

#### Proof

Freeness makes the quotient incidence graph balanced and preserves degree
with multiplicity.  Every regular bipartite multigraph has a perfect
matching; lifting its selected edge orbits gives an equivariant perfect
\(\mu\).

All table resources are free \(G\)-orbits.  Therefore an invariant selected
set is precisely an orbit selection, and the row/column/symbol conditions
descend exactly.  A quotient tree has zero gauged cycle voltage and lifts to
\(g\) disjoint trees.  Conversely, a quotient cycle of net voltage \(v\)
lifts to cycles of length multiplied by the order of \(v\); a loop is the
same statement.  Hence physical acyclicity is equivalent to a loopless
quotient forest.  The counts in (4.3) follow by freeness and subtraction.
\(\square\)

The quotient theorem constructs the cyclic first matching automatically;
it does not prove the integral orbit transversal.  A literal one-copy pivot
is also not invariant.  Retaining it in this quotient architecture requires
planting its entire resource-compatible \(G\)-orbit, whereas the unrestricted
Theorem 2.1 retains one pivot directly.

## 5. No automatic locally-Latin matching for even \(m\)

Call \(\mu\) locally Latin when, for every row \(C\), the map

\[
          b\longmapsto\alpha(C+\{b\})
          \qquad(b\in\Omega-C)                        \tag{5.1}
\]

is injective.  It is then a fixed-point-free permutation of
\(\Omega-C\).

For a coordinate \(a\), put

\[
                 \mathcal S_a=\{B\in\mathcal B:\alpha(B)=a\}.    \tag{5.2}
\]

Every member of \(\mathcal S_a\) avoids \(a\).

### Theorem 5.1 (Steiner obstruction)

If \(\mu\) is locally Latin, then, on \(\Omega-\{a\}\),

\[
                         \mathcal S_a
                 \text{ is an }S(m-2,m-1,2m-2)        \tag{5.3}
\]

for every \(a\).  Consequently a locally Latin \(\mu\) is impossible for
every even \(m\ge4\).  At \(m=4\) this is the nonexistence of an
\(S(2,3,6)\).

#### Proof

Fix an \((m-2)\)-set \(C\) avoiding \(a\).  In the row (5.1), the symbol
\(a\) occurs exactly once.  Hence exactly one block
\(B=C+\{b\}\) lies in \(\mathcal S_a\).  This is precisely (5.3).

Fix an \((m-3)\)-set \(E\subseteq\Omega-\{a\}\).  There are

\[
                         (2m-2)-(m-3)=m+1
\]

target \((m-2)\)-sets containing \(E\).  Every block of size \(m-1\)
containing \(E\) contains exactly two of them.  Therefore \(E\) must lie in

\[
                              {m+1\over2}              \tag{5.4}
\]

blocks of the Steiner system.  This is impossible when \(m\) is even.
\(\square\)

This refutes only the attempt to make every row automatically Latin.  The
desired partial transversal may exist in a non-Latin table.

## 6. No affine-linear cyclic point rule beyond \(m=3\)

Identify \(\Omega=\mathbb Z_n\), \(n=2m-1\).  Consider the most general
affine-linear point rule

\[
                         \alpha(B)=v+\sum_{x\in B}c_x
                         \pmod n.                      \tag{6.1}
\]

Assume translation covariance:

\[
                         \alpha(B+1)=\alpha(B)+1.      \tag{6.2}
\]

### Lemma 6.1 (affine collapse)

Every rule (6.1)--(6.2) has the form

\[
                         \alpha(B)=(m-1)^{-1}\sum_{x\in B}x+v'
                         \pmod n.                      \tag{6.3}
\]

#### Proof

Put \(d_x=c_{x+1}-c_x\).  Equation (6.2) says that the sum of the \(d_x\)
over every \((m-1)\)-subset is one.  Comparing two subsets differing in one
point shows that every \(d_x\) has one common value \(d\), and then
\((m-1)d=1\pmod n\).  Integrating \(c_{x+1}-c_x=d\) and absorbing the
constant contribution into \(v'\) gives (6.3).  \(\square\)

### Lemma 6.2 (distinct nonzero subset sums)

For \(m\ge4\), every residue of \(\mathbb Z_{2m-1}\) is the sum of
\(m-2\) distinct nonzero residues.

#### Proof

Put \(k=m-2\), so \(n=2k+3\).

If \(k=2q\), choose distinct nonzero \(x,y\) with \(x+y=w\), avoiding the
at most three forbidden choices \(x=0,w,w/2\).  Complete them by
\(q-1\) unused pairs \(\{t,-t\}\).

If \(k=2q+1\), choose three distinct nonzero residues \(x,y,z\) with
\(x+y+z=w\).  Fixing \(x=1\), at most five values of \(y\) violate
nonzeroness or distinctness of \(y,z=w-1-y\); since \(n\ge9\), a valid
choice exists.  Complete by \(q-1\) unused pairs \(\{t,-t\}\).

There are \(k+1\) nonzero opposite pairs in total, while the initial two or
three points occupy at most two or three of them, so the required unused
pairs exist.  \(\square\)

### Theorem 6.3 (affine cyclic no-go)

For every \(m\ge4\), no affine-linear translation-covariant rule can satisfy
the incidence legality condition

\[
                              \alpha(B)\notin B
                              \qquad(B\in\mathcal B).   \tag{6.4}
\]

#### Proof

Let \(u=(m-1)^{-1}\) and choose, by Lemma 6.2, an \((m-2)\)-set
\(S\) of distinct nonzero residues with sum

\[
                              \sum S=-u^{-1}v'.
\]

For \(B=\{0\}\cup S\), equation (6.3) gives \(\alpha(B)=0\in B\), violating
(6.4).  \(\square\)

Thus the natural affine sum/midpoint construction dies at the first
nontrivial extension beyond \(m=3\).

## 7. Full-rotation row obstruction

Suppose \(m=3r+2\), so \(n=2m-1=3(2r+1)\).  Let \(H\) be the order-three
subgroup of \(\mathbb Z_n\).

### Theorem 7.1

There is no fully \(\mathbb Z_n\)-equivariant row selector

\[
                         \sigma:\mathcal C\longrightarrow\mathcal B,
                         \qquad C\subset\sigma(C),      \tag{7.1}
\]

and hence no fully rotational \(Q_0\), regardless of the joint choice of
\(\mu\).

#### Proof

The \(H\)-orbits on coordinates have size three.  Choose a row
\(C\in\mathcal C\) as the union of \(r\) such orbits; then
\(|C|=3r=m-2\), and \(C\) is \(H\)-fixed.

Equivariance would make \(\sigma(C)\) \(H\)-fixed.  But every \(H\)-fixed
coordinate set is a union of 3-orbits and therefore has size divisible by
three, whereas

\[
                         |\sigma(C)|=m-1=3r+1.
\]

Contradiction.  \(\square\)

This is sharper than a component divisibility warning: the selector itself
already fails at one fixed row.  It explains why the three-free subgroup in
Section 4 is the canonical symmetry scale.

### Corollary 7.2 (the fixed-row obstruction has Catalan orbit size)

Under the full rotation group, the \(H\)-fixed rows form exactly

\[
                           \operatorname {Cat}_r
\]

row orbits, while no column or symbol vertex is \(H\)-fixed.
Consequently a selector which agrees with a fully equivariant rule outside
\(s\) full-rotation row orbits must have

\[
                              s\ge\operatorname {Cat}_r.             \tag{7.2}
\]

#### Proof

There are \(2r+1\) coordinate triples.  An \(H\)-fixed row has size
\(m-2=3r\), so it is the union of exactly \(r\) triples; hence there are
\(\binom{2r+1}{r}\) fixed rows.  The residual quotient
\(\mathbb Z_{2r+1}\) acts freely on these \(r\)-subsets: a subset fixed by
a nontrivial translation has size divisible by a nontrivial divisor of
\(2r+1\), impossible because \(\gcd(r,2r+1)=1\).  Therefore the number of
full-rotation row orbits is

\[
 {1\over2r+1}{2r+1\choose r}
   ={1\over r+1}{2r\choose r}
   =\operatorname {Cat}_r.
\]

Columns and symbols have size \(m-1=3r+1\), whereas every \(H\)-fixed set
is a union of triples.  Thus none is \(H\)-fixed.  Every fixed-row orbit
must consequently be included among the exceptional row orbits of an
equivariant-core selector. \(\square\)

This is a lower bound on exceptional **row orbits**, not on final additive
length.  A recursive off-support packet may rework all these rows while
exporting only a bounded interface.

## 8. Explicit positive base at \(m=3\)

Let \(\Omega=\mathbb Z_5\), and for a two-set \(B=\{x,y\}\) put

\[
                         \alpha(B)={x+y\over2}\pmod5,
                         \qquad \mu(B)=B+\alpha(B).     \tag{8.1}
\]

The midpoint is outside \(B\), and \(\mu\) bijects the ten two-sets with the
ten three-sets.  It is locally Latin.

For a row \(C=\{c\}\), choose

\[
                         \sigma(C)=\{c,c+1\}.           \tag{8.2}
\]

Then

\[
                         A_\mu(C,\sigma(C))=\{c,c+3\}. \tag{8.3}
\]

The five columns in (8.2) are the cyclic distance-one two-sets, while the
five symbols in (8.3) are the distance-two two-sets.  They are disjoint
orbits.  Hence the selected graph is five isolated directed edges: an exact
upper-exact Catalan forest with

\[
                         U=5,\qquad W=10,\qquad C=5.
\]

This supplies a genuine cyclic base, but Theorems 5.1 and 6.3 show that its
automatic midpoint/Latin mechanism cannot continue unchanged.

## 9. Revised frontier

Joint choice of \(M_0\) has converted the fixed-root rainbow matching into
one transparent object:

\[
\boxed{
\text{row-saturating partial Latin transversal}
\ +\ 
\text{acyclic column-to-symbol graph}.}
\]

The pivot is a prescribed path in this table, every fractional and graphic
rank has slack, and the clean cyclic quotient always supplies the first
matching.  What is not proved is the integral quotient transversal.

The correct next target is therefore either:

1. an integral matching/absorption theorem for the clean quotient table
   with a quotient-forest constraint; or
2. a noncyclic induction extending the prescribed pivot path while
   maintaining row, column, symbol, and graphic independence.

Local Latin completion, affine cyclic formulas, and full rotation in the
order-three dimensions are now rigorously excluded.
