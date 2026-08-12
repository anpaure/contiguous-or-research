# Binary rotors as clustered de Bruijn cycle covers: exact divergence, switch toll, and the minimal-skeleton obstruction

Date: 2026-07-26

Method: pure mathematics.  No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m,
\]

and let \(A,B\) be the two state rotors from
`MATH_THEOREM_ANTI_DIHEDRAL_NESTED_UCYCLE_GAUSSIAN_RETHREADING_20260726.md`:

\[
 A(x_1,\ldots,x_n)=(x_2,\ldots,x_{n-1},x_1,x_n),
\]

\[
 B(x_1,\ldots,x_n)=(x_2,\ldots,x_n,x_1).
\]

This note removes three artificial difficulties from the surviving
non-symmetric rotor gate and proves one statewise obstruction.

1.  The Boolean owner-transversal rotor circulation is exactly a
    **clustered directed cycle cover** in the injective de Bruijn graph:
    vertices are injective \((n-2)\)-words, arcs are injective
    \((n-1)\)-words, and one arc is chosen from every middle-owner
    cluster.  Thus ordinary circulation integrality and Birkhoff--von
    Neumann solve only the unclustered/projected problem.

2.  For every depth at once, complementary upper-prefix load differs
    from lower-prefix load by an exact Johnson-graph divergence supported
    only on selected \(A\)-arcs:

    \[
    \boxed{
    R_r-L_r=
    \sum_{e\text{ selected with }A}
       \bigl(\mathbf e_{K_r(e)\cup\{x_n\}}
             -\mathbf e_{K_r(e)\cup\{x_1\}}\bigr).}
    \tag{0.1}
    \]

    Consequently, if \(a\) is the number of \(A\)-arcs, then at every
    depth

    \[
       \#\{\text{missing upper targets}\}
       \le
       \#\{\text{missing lower targets}\}+a.
    \tag{0.2}
    \]

    This gives an exact aggregate-divergence replacement for the upper
    systems.  The crude estimate by \(Ha\) is valid, but the global cut
    below proves it unusable when \(H\to\infty\).  What is needed is
    cancellation among the selected Johnson divergences, not sparse
    switching.

3.  If the rotor support has \(C\) components, \(a\) selected \(A\)-arcs,
    and \(c_1\) non-pure components, then consecutive supporting wreaths
    differ by one adjacent swap and every new supporting wreath introduces
    at most two new middle owners.  Consequently

    \[
       \boxed{W\le nC+2a-2c_1.}
    \tag{0.3}
    \]

    Hence \(C=o(W/m)\) forces

    \[
                         a\ge(1/2-o(1))W.
    \tag{0.4}
    \]

    Therefore \(Ha=o(W)\) is impossible for every \(H\to\infty\).
    The proposed one-sided sparse-switch compiler is closed.  A surviving
    rotor construction must make the \(\Theta(W)\) nested Johnson
    divergences cancel to aggregate \(o(W)\) across the protected depths.

4.  The most economical periodic skeleton is nevertheless impossible.
    If every non-pure maximal \(B\)-run has the largest possible length
    \(n-1\), then its component has control word

    \[
                       (B^{n-2}A)^{n-1}
    \tag{0.6}
    \]

    up to cyclic shift.  It contains \((n-1)^2\) states but at most
    \(2(n-1)\) distinct middle owners.  For \(m\ge2\) it cannot occur in
    an owner-transversal circulation.  Thus the naively optimal
    one-hole-per-wreath port skeleton is closed statewise; a successful
    circulation must use genuinely nonuniform run lengths.

The surviving sufficient theorem is an exact cancellation form of the
earlier two-sided rotor gate:

> construct an owner-transversal clustered de Bruijn cycle cover with
> \(o(W/m)\) cycles, aggregate lower-prefix holes \(o(W)\), and aggregate
> \(\ell^1\)-norm \(o(W)\) for the nested \(A\)-switch divergences.

The uniform half-\(A\), half-\(B\) fractional circulation has zero signed
divergence at every depth and matches the necessary switch scale exactly.
The unresolved theorem is therefore a genuine discrepancy/cancellation
rounding problem, not a network-flow margin problem.

## 1. The injective de Bruijn graph

Let \(\mathcal V\) be the set of injective ordered \((n-2)\)-tuples on
\([n]\).  Let \(\mathcal E\) be the set of injective ordered
\((n-1)\)-tuples.  For

\[
 e=(x_1,\ldots,x_{n-1})\in\mathcal E
\]

put

\[
 t(e)=(x_1,\ldots,x_{n-2}),\qquad
 h(e)=(x_2,\ldots,x_{n-1}).
\tag{1.1}
\]

Thus \(e\) is a directed arc \(t(e)\to h(e)\).  Write \(x_n\) for the
unique coordinate missing from \(e\), and associate to \(e\) the
permutation state

\[
                         \pi(e)=(x_1,\ldots,x_n).
\tag{1.2}
\]

The middle-owner colour of \(e\) is

\[
                         \kappa(e)=\{x_1,\ldots,x_m\}.
\tag{1.3}
\]

Notice that \(\kappa(e)\) depends only on the tail \(t(e)\).  In
particular, the two arcs leaving one vertex of \(\mathcal V\) have the
same owner colour.

### Theorem 1.1 (clustered de Bruijn equivalence)

Boolean rotor circulations satisfying the owner equations (1.17) and
state-balance equations (1.18) of the earlier note are in bijection with
Boolean vectors \(y\in\{0,1\}^{\mathcal E}\) satisfying

\[
 \sum_{e:\kappa(e)=X}y_e=1
 \qquad\left(X\in\binom{[n]}m\right),
\tag{1.4}
\]

and

\[
 \sum_{e:t(e)=v}y_e=\sum_{e:h(e)=v}y_e
 \qquad(v\in\mathcal V).
\tag{1.5}
\]

The selected arcs in (1.4)--(1.5) form vertex-disjoint directed cycles,
and these are exactly the rotor components.  The lower and upper prefix
conditions are the corresponding colour-cover conditions on the selected
arc labels.

#### Proof

At a vertex

\[
 v=(x_2,\ldots,x_{n-1})
\]

there are exactly two incoming arcs, obtained by prepending one of the
two coordinates absent from \(v\), and exactly two outgoing arcs,
obtained by appending one of those coordinates.  If the incoming arc is

\[
 e=(x_1,x_2,\ldots,x_{n-1})
\]

and \(x_n\) is its missing coordinate, the two outgoing arcs are

\[
 (x_2,\ldots,x_{n-1},x_1),\qquad
 (x_2,\ldots,x_{n-1},x_n).
\]

They are precisely the state successors \(A\pi(e)\) and \(B\pi(e)\).
Thus a selected rotor transition is exactly a passage from a selected
incoming de Bruijn arc to a selected outgoing one at their common vertex.
State balance gives (1.5), while the rotor owner equation is (1.4).

Conversely, (1.4) implies that at most one selected arc leaves any fixed
\(v\), because all arcs leaving \(v\) have the same owner colour.  By
(1.5), selected indegree and outdegree at \(v\) are therefore both zero
or both one.  Hence the selected arcs form disjoint directed cycles.  At
every used vertex, its unique incoming and outgoing selected arcs form
one of the two rotor transitions just displayed.  This reconstructs the
unique Boolean rotor circulation.  Component counts are unchanged.
\(\square\)

### Corollary 1.2 (what Birkhoff--von Neumann does and does not give)

For a fractional solution \(y\), define

\[
 p_{X,Y}=
 \sum_{\substack{e:\kappa(e)=X\\
                 \kappa(h(e))=Y}} y_e,
\tag{1.6}
\]

where \(\kappa(v)\) denotes the set of the first \(m\) entries of
\(v\).  Then \(p\) is a doubly stochastic matrix supported on directed
Johnson edges.

Consequently Birkhoff--von Neumann decomposes the **projection** into
Johnson cycle covers, but does not choose compatible \((n-2)\)-tuple
states.  The latter compatibility is exactly the residence/clustered
cycle-cover gate in Theorem 1.1.

#### Proof

Row sums are one by (1.4).  Sum (1.5) over all vertices \(v\) with
\(\kappa(v)=Y\).  Their total selected outdegree is one, again by (1.4),
so their total selected indegree is one; this is the column sum of
(1.6).  Shifting one position changes the middle prefix by deleting
\(x_1\) and adding \(x_{m+1}\), so the support lies in the Johnson graph.
\(\square\)

For the uniform fractional circulation, (1.6) is the simple random-walk
matrix on \(J(n,m)\): every directed Johnson neighbour receives mass
\(1/(m(m+1))\).  Thus the factorial local freedom and projected
Birkhoff integrality are real, but neither addresses the clustered lift.

## 2. Exact all-depth upper--lower divergence

Let \(y\) be an integral solution of (1.4)--(1.5), and let
\(z_e^A,z_e^B\) record its unique rotor transition, so

\[
 y_e=z_e^A+z_e^B.
\]

Put

\[
                         a=\sum_e z_e^A.
\tag{2.1}
\]

For \(1\le r\le m\) and \(T\in\binom{[n]}r\), define the lower-prefix
load

\[
 L_r(T)=
 \sum_e y_e\,
 \mathbf 1\!\left[\{x_1,\ldots,x_r\}=T\right],
\tag{2.2}
\]

and the complementary upper-prefix load

\[
 R_r(T)=
 \sum_e y_e\,
 \mathbf 1\!\left[
 \{x_{n-r+1},\ldots,x_{n-1},x_n\}=T\right].
\tag{2.3}
\]

For \(r=m-q\), (2.3) is the load of complements of the selected
rank-\((m+1+q)\) prefixes.

Put

\[
 K_r(e)=\{x_{n-r+1},\ldots,x_{n-1}\},
\tag{2.4}
\]

which has size \(r-1\).

### Lemma 2.1 (internal block stationarity)

For every \(r\le n-2\), the multiset of selected state blocks in any
fixed consecutive positions

\[
 1,\ldots,r;\quad 2,\ldots,r+1;\quad\ldots;\quad
 n-r,\ldots,n-1
\]

is independent of the starting position.  In particular,

\[
 L_r(T)=
 \sum_e y_e\,
 \mathbf 1\!\left[
 \{x_{n-r},\ldots,x_{n-1}\}=T\right].
\tag{2.5}
\]

#### Proof

Along every selected de Bruijn cycle, shifting from one selected arc to
the next shifts positions \(j,\ldots,j+r-1\) to positions
\(j+1,\ldots,j+r\), as long as the latter end at or before position
\(n-1\).  Summing around all selected cycles gives equality of the two
block multisets.  Iterate from \(j=1\) to \(j=n-r\). \(\square\)

### Theorem 2.2 (the \(A\)-switch divergence identity)

For every \(1\le r\le m\),

\[
 \boxed{
 R_r-L_r=
 \sum_e z_e^A
 \left(
   \mathbf e_{K_r(e)\cup\{x_n\}}
   -\mathbf e_{K_r(e)\cup\{x_1\}}
 \right).}
\tag{2.6}
\]

Thus \(R_r-L_r\) is the divergence of \(a\) oriented edges of the
Johnson graph \(J(n,r)\), and

\[
 \boxed{
 \frac12\lVert R_r-L_r\rVert_1
 =\sum_T(L_r(T)-R_r(T))_+
 \le a.}
\tag{2.7}
\]

#### Proof

Count the last internal \(r\)-block of every selected successor state.
By Lemma 2.1 and the bijection from selected arcs to their successors,
the resulting load is \(L_r\).

For a \(B\)-transition out of \(e\), the successor is

\[
 (x_2,\ldots,x_n,x_1),
\]

and its last internal \(r\)-block is
\(K_r(e)\cup\{x_n\}\), exactly the suffix counted by \(R_r\).
For an \(A\)-transition, the successor is

\[
 (x_2,\ldots,x_{n-1},x_1,x_n),
\]

and its last internal \(r\)-block is
\(K_r(e)\cup\{x_1\}\).  Subtracting the two load expressions proves
(2.6).

The two endpoints in every summand are distinct \(r\)-sets, so each
summand has \(\ell^1\)-norm two.  The triangle inequality proves (2.7).
\(\square\)

### Corollary 2.3 (upper holes cost at most one per switch per depth)

Let

\[
 M(L_r)=\#\{T:L_r(T)=0\},\qquad
 M(R_r)=\#\{T:R_r(T)=0\}.
\]

Then

\[
                         \boxed{M(R_r)\le M(L_r)+a.}
\tag{2.8}
\]

Consequently, through depths \(0\le q\le H\),

\[
 \sum_{q=0}^{H}M(R_{m-q})
 \le
 \sum_{q=0}^{H}M(L_{m-q})+(H+1)a.
\tag{2.9}
\]

#### Proof

Every target counted by \(M(R_r)\) but not by \(M(L_r)\) contributes at
least one to \((L_r-R_r)_+\).  Apply (2.7), then sum in \(q\).
\(\square\)

This is the aggregate substitute for the unusable anti-dihedral
symmetry.  Pure \(B\)-motion has exact lower/upper complementary load
equality.  Every nonlinear \(A\)-switch is allowed, but is charged once
per protected depth rather than forcing a second independent cover.

### Corollary 2.4 (one-sided rotor compiler)

Let an integral owner-transversal rotor circulation have \(C\) support
cycles, \(a\) selected \(A\)-arcs, and aggregate lower-prefix hole count

\[
 \mathcal M_H^-=
 \sum_{q=0}^{H}M(L_{m-q}).
\tag{2.10}
\]

Then the paired central band through depth \(H\) has a literal word of
length at most

\[
 \boxed{
 W+C(m+H)+2\mathcal M_H^-+(H+1)a.}
\tag{2.11}
\]

In particular, the three conditions

\[
 C=o(W/m),\qquad \mathcal M_H^-=o(W),\qquad Ha=o(W),
\tag{2.12}
\]

with \(H=o(m)\), suffice for a \(W+o(W)\) central-band word.

#### Proof

Linearize every rotor cycle by repeating its first \(m+H\) singleton
symbols, as in Theorem 2.4 of the earlier note.  This costs
\(C(m+H)\).  Append each missing lower target as one literal mask.
By (2.9), at most \(\mathcal M_H^-+(H+1)a\) complementary upper targets
remain missing; append those literally as well.  Every appended mask
costs one word position. \(\square\)

The criterion (2.12) is deliberately aggregate and the theorem is
correct, but Theorem 3.4 below proves that its switch hypothesis is
impossible when \(H\to\infty\) and \(C=o(W/m)\).  Its useful replacement
keeps the cancellation in (2.6) instead of applying the triangle
inequality term by term.

### Corollary 2.5 (cancellation rotor compiler)

Define the aggregate signed-divergence norm

\[
 \mathfrak D_H(z)=
 \frac12\sum_{q=0}^{H}
 \left\lVert R_{m-q}-L_{m-q}\right\rVert_1.
\tag{2.13}
\]

Then the paired central band through depth \(H\) has a literal word of
length at most

\[
 \boxed{
 W+C(m+H)+2\mathcal M_H^-+\mathfrak D_H(z).}
\tag{2.14}
\]

Consequently

\[
 C=o(W/m),\qquad \mathcal M_H^-=o(W),\qquad
 \mathfrak D_H(z)=o(W),\qquad H=o(m)
\tag{2.15}
\]

is a sufficient integral rotor theorem for coefficient one.

#### Proof

At depth \(q\), the proof of Corollary 2.3 gives the sharper estimate

\[
 M(R_{m-q})\le M(L_{m-q})+
 \frac12\lVert R_{m-q}-L_{m-q}\rVert_1.
\]

Sum, then repeat the literalization and repair proof of Corollary 2.4.
The lower repairs cost \(\mathcal M_H^-\), and the upper repairs cost at
most \(\mathcal M_H^-+\mathfrak D_H(z)\). \(\square\)

The immediate-rank divergence has an additional owner-transversal
structure which rules out pairwise cancellation.

### Theorem 2.6 (union-injective \(A\)-switch flow)

For a selected \(A\)-arc

\[
 e=(x_1,\ldots,x_{n-1}),\qquad x_n\text{ missing},
\]

put

\[
 S_e=K_m(e)\cup\{x_1\},\qquad
 T_e=K_m(e)\cup\{x_n\},\qquad
 U_e=S_e\cup T_e.
\tag{2.16}
\]

Thus its depth-zero divergence contribution is
\(\mathbf e_{T_e}-\mathbf e_{S_e}\), an oriented edge of \(J(n,m)\).
Then the map

\[
                         \boxed{e\longmapsto U_e}
\tag{2.17}
\]

is injective on the selected \(A\)-arcs.  Equivalently, at most one
selected \(A\)-switch edge lies in each upper Johnson clique

\[
 \binom{U}{m}\qquad\left(U\in\binom{[n]}{m+1}\right).
\]

Consequently:

1. two selected \(A\)-switches can never have exactly opposite
   depth-zero divergence;
2. a three-switch zero-sum at depth zero cannot be a top triangle inside
   one \((m+1)\)-set;
3. every three-switch zero-sum is therefore a star triangle

   \[
   K\cup\{a\}\longrightarrow K\cup\{b\}
   \longrightarrow K\cup\{c\}\longrightarrow K\cup\{a\}
   \tag{2.18}
   \]

   for a common \((m-1)\)-set \(K\).

#### Proof

Write the full state as

\[
 \pi(e)=(x_1,P,\mathbf K,x_n),
\]

where \(P=(x_2,\ldots,x_{m+1})\) is an ordered \(m\)-tuple and
\(\mathbf K=(x_{m+2},\ldots,x_{n-1})\) has underlying set \(K_m(e)\).
The
\(A\)-successor is

\[
 A\pi(e)=(P,\mathbf K,x_1,x_n).
\]

Its middle owner is the underlying set of \(P\), namely

\[
 [n]\setminus U_e.
\tag{2.19}
\]

If two selected \(A\)-arcs had the same \(U_e\), their selected
\(A\)-successors would lie in the same middle-owner fibre.  The owner
equation permits only one selected state in that fibre.  Since \(A\) is
a bijection, the two source arcs would be equal.  This proves (2.17).

Opposite oriented Johnson edges have the same union, proving item 1.
Three nonzero oriented graph edges sum to zero as vertex-incidence
vectors only when they form a directed triangle.  Triangles in
\(J(n,m)\) are of two types: three \(m\)-subsets of one common
\((m+1)\)-set (a top triangle), or three \(m\)-sets containing one common
\((m-1)\)-set (a star triangle).  All edges of a top triangle have the
same union colour and violate (2.17).  This leaves exactly (2.18).
\(\square\)

### Corollary 2.7 (minimum exact all-depth cancellation atom)

There is no two-switch exact cancellation of the nested divergence
family in (2.6).  If three selected switches cancel exactly at every
protected depth, then at each depth they form a star triangle with one
common core.  In particular their suffix cores satisfy

\[
 K_{m-q}(e_1)=K_{m-q}(e_2)=K_{m-q}(e_3)
 \qquad(0\le q\le H),
\tag{2.20}
\]

and their endpoint coordinates run around one directed 3-cycle.

#### Proof

Depth zero already excludes a two-switch cancellation by Theorem 2.6.
For three switches, Theorem 2.6 makes their depth-zero triangle a star
with common core \(K\), disjoint from its three endpoint coordinates.
At every lower protected rank, each switch core \(K_{m-q}(e_i)\) is a
subset of its depth-zero core and hence a subset of \(K\).  A top
triangle on the same three endpoint coordinates has, in the core of each
edge, the third endpoint coordinate.  That is impossible because
\(K\) is disjoint from all three endpoints.  The lower-rank triangle is
therefore also star type, whose three pairwise intersections are one
common \((m-q-1)\)-core.  This is (2.20). \(\square\)

Thus exact cancellation begins with **nested star triangles**, not
reverse pairs.  More generally the selected \(A\)-switches must form an
approximately Eulerian, union-rainbow directed subgraph of \(J(n,m)\),
whose lower-rank nested projections are approximately Eulerian
simultaneously.  This is the concrete discrepancy object left by
Corollary 2.5.

The star-triangle atom is not itself killed by the owner equations.

### Proposition 2.8 (local owner-compatible star atom)

Let \(K,R\) be disjoint \((m-1)\)-sets and let \(a,b,c\) be three further
coordinates, so

\[
 [n]=K\sqcup R\sqcup\{a,b,c\}.
\]

Fix one order \(\mathbf K\) of \(K\).  Choose orders

\[
 P_{ab}\text{ of }R\cup\{c\},\qquad
 P_{bc}\text{ of }R\cup\{a\},\qquad
 P_{ca}\text{ of }R\cup\{b\},
\]

each with its last entry in \(R\).  Define three states

\[
 \begin{aligned}
 \pi_{ab}&=(a,P_{ab},\mathbf K,b),\\
 \pi_{bc}&=(b,P_{bc},\mathbf K,c),\\
 \pi_{ca}&=(c,P_{ca},\mathbf K,a).
 \end{aligned}
\tag{2.21}
\]

If all three use their \(A\)-transition, then:

1. their nested divergence contributions cancel exactly at every rank
   \(1\le r\le m\);
2. their three source owners are pairwise distinct;
3. their three \(A\)-successor owners are pairwise distinct; and
4. no source owner equals a successor owner.

Thus there is no local owner-fibre obstruction to a three-switch exact
cancellation atom.

#### Proof

At every rank, all three switches have the same suffix core, while their
endpoint pairs are

\[
 a\to b,\qquad b\to c,\qquad c\to a.
\]

Their three signed Johnson edges therefore sum to zero.

The \(A\)-successor owners, by (2.19), are respectively

\[
 R\cup\{c\},\qquad R\cup\{a\},\qquad R\cup\{b\}.
\tag{2.22}
\]

They are distinct.  Because the last entry of every \(P\)-block lies in
\(R\), the source owners contain respectively the endpoint pairs

\[
 \{a,c\},\qquad\{a,b\},\qquad\{b,c\},
\tag{2.23}
\]

and omit one element of \(R\).  Hence they are pairwise distinct.
Every set in (2.22) contains exactly one of \(a,b,c\), whereas every
source owner in (2.23) contains exactly two.  The two triples of owners
are disjoint. \(\square\)

Completing many atoms (2.21) into one clustered de Bruijn cycle cover is
still a global problem: their \(A\)-successors need selected outgoing
arcs and their sources need selected predecessors.  Proposition 2.8
only proves that the newly isolated cancellation object is nonvacuous.

## 3. The sharp switch/component toll

Call a maximal consecutive segment of selected states joined by
\(B\)-transitions a **\(B\)-run**.  A component with no \(A\)-arc is a
pure \(B\)-component.

### Lemma 3.1 (run lengths)

A pure \(B\)-component has exactly \(n\) states.  Every \(B\)-run in a
non-pure component has at most \(n-1\) states.

#### Proof

The permutation \(B\) has order \(n\), and its orbit on a state has
exactly \(n\) elements, proving the first assertion.

Suppose a non-pure run contained all \(n\) states of one \(B\)-orbit.
At its last state \(e\), the selected \(A\)-successor and its
\(B\)-successor are distinct outgoing de Bruijn arcs at the same vertex.
The latter is the first state of the full run and is selected.  Those two
outgoing arcs have the same owner colour, contradicting (1.4).  Hence a
non-pure run has length at most \(n-1\). \(\square\)

### Theorem 3.2 (Catalan switch toll)

Let \(a\) be the total number of selected \(A\)-arcs, \(C\) the number
of rotor components, and \(c_0\) the number of pure \(B\)-components.
Then

\[
 \boxed{W\le (n-1)a+n c_0\le(n-1)a+nC.}
\tag{3.1}
\]

Consequently,

\[
 \boxed{
 a\ge\frac{W-nC}{n-1}.}
\tag{3.2}
\]

In particular,

\[
 C=o(W/m)\quad\Longrightarrow\quad
 a\ge(1-o(1))\frac{W}{n-1}
       =(1-o(1))\frac{W}{2m}.
\tag{3.3}
\]

#### Proof

Every non-pure component with \(a_C\) \(A\)-arcs has exactly \(a_C\)
maximal \(B\)-runs, including a one-state run when two \(A\)-arcs are
consecutive.  Lemma 3.1 bounds their total number of states by
\((n-1)a_C\).  Every pure component contributes \(n\) states.  Sum over
components; there are exactly \(W\) selected states by (1.4).  This is
the first inequality in (3.1); the second is \(c_0\le C\).  Rearranging
proves the rest. \(\square\)

The basic toll alone would appear compatible with the one-sided repair
criterion, because for every \(H=o(m)\),

\[
 \frac{2W}{n+2}=o\!\left(\frac WH\right).
\tag{3.4}
\]

The next two theorems show that this conclusion is false: it ignores the
large overlap of all supporting wreaths along one component.  The true
switch toll is linear in \(W\), not Catalan-order.

There is a stronger local bound because consecutive runs cannot both use
nearly all of their supporting wreaths.

### Theorem 3.3 (adjacent-run overlap cut)

Let \(\ell_1,\ldots,\ell_k\) be the cyclic sequence of \(B\)-run lengths
in one non-pure component.  Then

\[
                         \boxed{
 \ell_i+\ell_{i+1}\le n+2\qquad(i\bmod k).}
\tag{3.5}
\]

Consequently, globally,

\[
                         \boxed{
 W\le \frac{n+2}{2}a+n c_0,}
\tag{3.6}
\]

and therefore

\[
 C=o(W/m)\quad\Longrightarrow\quad
 a\ge(2-o(1))\frac{W}{n+2}
   =(1-o(1))\frac Wm.
\tag{3.7}
\]

#### Proof

The sign of \(A\) is odd and the sign of \(B\) is even, because
\(n=2m+1\).  Closure of a state cycle therefore makes its number of
\(A\)-arcs even.  A non-pure component has at least two runs, so
consecutive runs below are distinct occurrences.

Let the last state of run \(i\) be

\[
                         \pi=(x_1,\ldots,x_n).
\]

The supporting \(B\)-orbit is the cyclic coordinate order represented by
\(\pi\).  The next run begins at

\[
 A\pi=(x_2,\ldots,x_{n-1},x_1,x_n).
\]

Rotate the first cyclic order to

\[
 (x_2,\ldots,x_{n-1},x_n,x_1).
\]

The second order is obtained by transposing the adjacent final symbols
\(x_n,x_1\).  Among the \(n\) cyclic intervals of length \(m\), only the
two intervals which contain exactly one of this adjacent pair can change
as sets.  Hence the two full wreath supports have at least \(n-2\)
middle owners in common.

Run \(i\) selects \(\ell_i\) of the \(n\) owners in its supporting
wreath, and run \(i+1\) selects \(\ell_{i+1}\).  Since the whole rotor
circulation is owner-transversal, the two selected subsets are disjoint.
Every one of the at least \(n-2\) common owners must therefore be among
the \((n-\ell_i)+(n-\ell_{i+1})\) omitted occurrences.  Thus

\[
 n-2\le 2n-\ell_i-\ell_{i+1},
\]

which is (3.5).  Sum (3.5) cyclically: every run length appears twice,
so the non-pure component has at most \(k(n+2)/2\) states.  It has
exactly \(k\) \(A\)-arcs.  Sum over non-pure components and add the
\(n\) states of each pure component to obtain (3.6).  Finally
\(c_0\le C=o(W/m)\) gives (3.7). \(\square\)

Equation (3.5) also says that at least half the runs in every non-pure
component have length at most \((n+2)/2\): those runs form a vertex cover
of the cyclic adjacency graph of the runs.

The decisive estimate uses the same adjacent-swap overlap cumulatively,
instead of only on adjacent run lengths.

### Theorem 3.4 (global supporting-wreath growth cut)

Let \(c_1=C-c_0\) be the number of non-pure components.  Then

\[
                         \boxed{
 W\le nC+2a-2c_1.}
\tag{3.8}
\]

In particular,

\[
 C=o(W/m)\quad\Longrightarrow\quad
                         \boxed{a\ge(1/2-o(1))W.}
\tag{3.9}
\]

#### Proof

Fix a non-pure component with \(a_C\) runs.  Every run is contained in
the full middle-owner support of one \(B\)-orbit, hence in one wreath.
As proved in Theorem 3.3, the supporting wreaths of two consecutive runs
have at least \(n-2\) common owners.  Therefore adjoining the next
supporting wreath to the union introduces at most two new owner sets.
Starting with \(n\) owners, all supporting wreaths of this component have
union size at most

\[
                         n+2(a_C-1).
\]

Owner transversality makes all states of the component have distinct
middle owners.  Hence its length is at most \(n+2(a_C-1)\).  A pure
\(B\)-component has length \(n\).  Summing over the \(c_1\) non-pure and
\(c_0\) pure components gives

\[
 W\le nc_0+nc_1+2a-2c_1=nC+2a-2c_1,
\]

which proves (3.8).  Since \(nC=o(W)\), (3.9) follows. \(\square\)

### Corollary 3.5 (the sharp common fractional point)

Give every state total mass \(1/D\), where
\(D=m!(m+1)!\), and split its outgoing mass between the rotors with

\[
 t_A=\frac12,\qquad t_B=\frac12.
\tag{3.10}
\]

This is a fractional owner-transversal circulation with

\[
 a_{\rm frac}=\frac W2,
\tag{3.11}
\]

and, simultaneously at every rank \(r\),

\[
 L_r(T)=R_r(T)=\frac{W}{\binom nr}
 \qquad\left(T\in\binom{[n]}r\right).
\tag{3.12}
\]

Thus the prefix margins and the asymptotically necessary switch scale in
Theorem 3.4 have one exact common fractional point.

#### Proof

The circulation and prefix calculations are Theorem 1.7 of the earlier
rotor note.  The total selected root mass is \(W\), so the \(A\)-mass is
\(t_AW=W/2\).  Uniformity of the permutation states gives (3.12);
it also follows for the upper side by averaging (2.6), whose signed
Johnson edges cancel under the uniform state distribution. \(\square\)

The half--half point is informative.  Its mean \(B\)-run length is two,
exactly the order forced by Theorem 3.4, and its signed divergence is
zero at every depth.  Hence the remaining gap is not a scalar margin or
switch-budget gap: it is correlated integral rounding with simultaneous
all-depth divergence cancellation.

## 4. The maximally long-run skeleton is owner-degenerate

The numerical compatibility in (3.4) makes the equality shape in
Theorem 3.2 the first natural construction to test.  It fails exactly.

### Theorem 4.1 (one-hole rotor classification)

Suppose a non-pure rotor component has every maximal \(B\)-run of length
exactly \(n-1\).  Then, up to cyclic shift, its rotor control word is

\[
                         (B^{n-2}A)^{n-1},
\tag{4.1}
\]

and it has \((n-1)^2\) states.

More explicitly, if \(h_j\) is the unique omitted state in the
\(B\)-orbit supporting the \(j\)-th run, then

\[
                         h_{j+1}=A^{-1}h_j.
\tag{4.2}
\]

The \(h_j\)'s run through one complete \(A\)-orbit, of length \(n-1\).

#### Proof

A run of length \(n-1\) in a \(B\)-orbit contains every state except a
unique hole \(h_j\).  It begins at \(Bh_j\), ends at \(B^{-1}h_j\), and
has \(n-2\) internal \(B\)-transitions.  Its outgoing \(A\)-arc must
enter the beginning of the next run, so

\[
 A B^{-1}h_j=B h_{j+1}.
\]

Hence

\[
 h_{j+1}=B^{-1}AB^{-1}h_j=A^{-1}h_j,
\tag{4.3}
\]

where the last identity follows directly from the displayed definitions
of \(A,B\).  The permutation \(A\) rotates the first \(n-1\) positions
and fixes the last one, so every state has an \(A\)-orbit of exact length
\(n-1\).  Nor can two earlier holes lie in the same \(B\)-orbit:
their two full runs would each contain \(n-1\) of that orbit's \(n\)
states and hence would intersect, whereas a directed support component
is a simple cycle.  Thus there is no premature state recurrence; the
first return occurs after all \(n-1\) holes have been visited.  There are
therefore \(n-1\) runs of \(n-1\) states each, with chronological
control word \((B^{n-2}A)^{n-1}\).  This proves all assertions.
\(\square\)

### Theorem 4.2 (middle-owner collapse of the one-hole skeleton)

For \(m\ge2\), the component in Theorem 4.1 has at most

\[
                              2(n-1)
\tag{4.4}
\]

distinct middle owners among its \((n-1)^2\) states.  Consequently it
cannot be a component of an owner-transversal rotor circulation.

#### Proof

Write the initial hole state as

\[
 h_0=(c_1,\ldots,c_{n-1},z).
\]

The holes \(A^{-j}h_0\) rotate the first \(n-1=2m\) coordinates and
leave \(z\) last.  Their \(B\)-orbits are therefore precisely the cyclic
orders obtained by inserting \(z\) into each of the \(2m\) gaps of the
fixed cyclic order

\[
                         (c_1,\ldots,c_{2m}).
\]

An \(m\)-interval in any one of these inserted cyclic orders is of one
of two kinds.

* If it avoids \(z\), it is a cyclic interval of length \(m\) in the
  fixed \(2m\)-cycle on the \(c_i\)'s.  There are at most \(2m=n-1\)
  such sets.
* If it contains \(z\), deleting \(z\) leaves a cyclic interval of
  length \(m-1\) in that same fixed cycle.  Again there are at most
  \(2m=n-1\) such sets.

Removing one hole from every \(B\)-orbit cannot introduce a new owner.
Thus the whole component uses at most \(2(n-1)\) owner sets.  For
\(m\ge2\),

\[
 (n-1)^2>2(n-1),
\]

so some owner repeats, contradicting (1.4). \(\square\)

### Corollary 4.3 (strict run defect)

Every non-pure component of an owner-transversal rotor circulation has at
least one \(B\)-run of length at most \(n-2\).  If \(c_1=C-c_0\) is the
number of non-pure components, then

\[
                         \boxed{
 W\le(n-1)a+n c_0-c_1.}
\tag{4.5}
\]

#### Proof

The first statement is Theorem 4.2.  Relative to the proof of Theorem
3.2, each non-pure component therefore loses at least one state from its
maximal \((n-1)a_C\) allowance.  Sum the losses. \(\square\)

The improvement in (4.5) is not asymptotically large when \(C=o(W/m)\),
but it is structurally decisive: the periodic equality skeleton is not a
candidate.  Any construction must vary its run lengths and thereby leave
the fixed inserted-cycle geometry of Theorem 4.2.

The variation cannot be confined to one exceptional run per long
component.  There is a positive-density reset toll.

### Theorem 4.4 (many short-run resets are necessary)

Let \(s\) be the total number of maximal \(B\)-runs of length at most
\(n-2\) in all non-pure components.  Then

\[
                         \boxed{
 s\ge\frac a2,\qquad
 W\le n c_0+(3n-4)s.}
\tag{4.6}
\]

Consequently, if \(C=o(W/m)\), then

\[
                         \boxed{
 s\ge(1/4-o(1))W.}
\tag{4.7}
\]

In particular, a low-component circulation has a positive density of
short runs; the failed periodic skeleton cannot be repaired at a sparse
set of exceptional ports.

#### Proof

Fix one non-pure component.  Its cyclic run sequence contains at least
one short run by Theorem 4.2.  Delete the short runs from the sequence.
The remaining full runs split into at most \(s_C\) consecutive blocks,
where \(s_C\) is the number of short runs in this component.

Within one block of consecutive full runs, the proof of Theorem 4.1 gives

\[
                         h_{j+1}=A^{-1}h_j.
\]

Thus all their supporting \(B\)-orbits are obtained by inserting one
fixed distinguished coordinate into gaps of one fixed cyclic order on
the other \(n-1\) coordinates.  The proof of Theorem 4.2 applies without
requiring the block to contain all \(n-1\) gaps: the union of the middle
owners of all full runs in this block has size at most \(2(n-1)\).

Each short run has at most \(n-2\) states and therefore contributes at
most \(n-2\) additional owners.  Hence the number of distinct owners in
this component is at most

\[
 s_C\bigl(2(n-1)+(n-2)\bigr)=(3n-4)s_C.
\]

Owner transversality makes the component length equal to its number of
distinct owners.  Sum over non-pure components and add the \(n\) states
of each pure component.  This proves the second inequality in (4.6).
Since \(c_0\le C=o(W/m)\)
and \(n\sim2m\), the second inequality alone gives the weaker bound
\(s\ge(1/3-o(1))W/n\).

For the sharp bound, a run not counted by \(s\) has length \(n-1\).
The adjacent-run inequality (3.5) forbids two such runs from being
consecutive when \(n\ge5\).  Hence the uncounted runs form an independent
set in each cyclic run sequence, and \(s\ge a/2\).  Theorem 3.4 gives
\(a\ge(1/2-o(1))W\), so

\[
 s\ge a/2\ge(1/4-o(1))W.
\]

This proves (4.7). \(\square\)

The reset toll is not a hidden group-orbit obstruction.  A defect of one
in the run length already restores the full state group.

### Proposition 4.5 (two consecutive run lengths generate all states)

For \(1\le\ell\le n-2\), put

\[
                         F_\ell=A B^{\ell-1}.
\tag{4.8}
\]

This is the state transformation from the beginning of a \(B\)-run of
length \(\ell\) to the beginning of the next run.  Then

\[
                         \boxed{
 \langle F_\ell,F_{\ell+1}\rangle=S_n.}
\tag{4.9}
\]

In particular, allowing run lengths \(n-2\) and \(n-1\) destroys the
inserted-cycle confinement of Theorem 4.2 completely.

#### Proof

As position permutations,

\[
 F_\ell^{-1}F_{\ell+1}
 =B^{-(\ell-1)}A^{-1}AB^\ell=B.
\]

It follows that

\[
 A=F_\ell B^{-(\ell-1)}
\]

also lies in the generated group.  Proposition 1.6 of the earlier rotor
note proves \(\langle A,B\rangle=S_n\). \(\square\)

Proposition 4.5 is only an ambient connectivity statement.  A macro walk
using \(F_{n-2},F_{n-1}\) must still keep all expanded \(B\)-runs
state-disjoint and all middle owners distinct.  Theorem 4.4 says it must
use the shorter macro a positive-density number of times; Proposition
4.5 says that doing so supplies enough algebraic mobility in principle.

The global half-switch bound in Theorem 3.4 points instead to the
opposite extreme: alternate \(A\) and \(B\) at every step.  This produces
a genuine long owner-simple component in one parity.

### Theorem 4.6 (alternating owner-simple component and parity split)

Let

\[
                         G=BA.
\tag{4.10}
\]

For any state \(\pi\), consider the alternating rotor orbit

\[
 \pi,\ A\pi,\ G\pi,\ AG\pi,\ G^2\pi,\ AG^2\pi,\ldots .
\tag{4.11}
\]

Then:

1. \(G\) has order \(m(m+1)\), and (4.11) is a rotor component of
   length \(2m(m+1)\);
2. if \(m\ge3\) is odd, all \(2m(m+1)\) middle owners in (4.11) are
   distinct;
3. if \(m\) is even, the owner orbit of the states \(G^j\pi\) equals the
   owner orbit of the states \(AG^j\pi\), so (4.11) repeats every owner
   and cannot lie in an owner-transversal circulation.

Thus for odd \(m\) the binary rotor graph contains explicit
owner-transversal components of length \(\Theta(m^2)\), using exactly
half \(A\)-arcs.  A packing of their coordinate relabels leaving
\(o(W/m)\) owners would already meet the component and switch scales.

#### Proof

Acting on a tuple,

\[
 G(x_1,\ldots,x_n)
 =(x_3,x_4,\ldots,x_{n-1},x_1,x_n,x_2).
\tag{4.12}
\]

As a permutation of positions it has the two cycles

\[
 C_0=(1,3,5,\ldots,2m-1),\qquad
 C_1=(2,4,6,\ldots,2m,2m+1),
\tag{4.13}
\]

of respective lengths \(m\) and \(m+1\).  They are coprime, so \(G\)
has order \(L=m(m+1)\).  The two parity classes in (4.11) are the
\(G\)-orbit of \(\pi\) and its \(A\)-image.  Their owner position sets,
measured in \(\pi\), are the \(G\)-orbits of

\[
 P=\{1,\ldots,m\},
 \qquad Q=\{2,\ldots,m+1\}.
\tag{4.14}
\]

The two state orbits are disjoint.  Indeed every power of \(G\) preserves
the two position cycles \(C_0,C_1\), whereas \(A\) does not (it sends a
position from one of them to the other).  With all labels distinct,
\(A\pi=G^k\pi\) would imply equality of these position permutations.
Thus (4.11) has length \(2L\).

In each position cycle in (4.13), \(P\) is a nonempty proper consecutive
interval.  Its rotational stabilizer is therefore trivial.  The same is
true of \(Q\).  Hence both owner orbits have full length \(L\).

Suppose first that \(m=2r+1\) is odd.  The intersection cardinalities
with the two invariant position cycles are

\[
 \begin{array}{c|cc}
      &C_0&C_1\\ \hline
 P&r+1&r\\
 Q&r&r+1
 \end{array}
\tag{4.15}
\]

No power of \(G\) changes these cardinalities, so the two owner orbits
are disjoint.  This proves item 2 and also prevents a collision between
the two state orbits in (4.11).

Now let \(m=2r\).  On \(C_0\), the set \(Q\) is a one-step translate of
\(P\); on \(C_1\), it is the same interval as \(P\).  By the Chinese
remainder theorem there is a power of \(G\) which translates by one on
the \(m\)-cycle \(C_0\) and by zero on the \((m+1)\)-cycle \(C_1\).
Thus \(Q=G^kP\) for some \(k\), and the two owner orbits coincide.  This
proves item 3. \(\square\)

Theorem 4.6 is a component theorem, not a factor theorem.  In odd
parameter it reduces the owner/cycle portion of the rotor gate to a
near-perfect matching problem in the coordinate orbit of one explicit
\(2m(m+1)\)-edge owner block.  Lower-prefix coverage and nested
divergence cancellation remain additional simultaneous requirements.

The subsequent exact orbit audit in
MATH_THEOREM_ALTERNATING_ROTOR_ORBIT_HYPERGRAPH_AND_PREFIX_PROFILE_20260726.md
shows that the lower-prefix qualification is fatal for a bulk use of
these components.  At depth one, each alternating component's
\(2m(m+1)\) occurrences have support only \(m(m+1)\).  Hence any
owner-disjoint packing covers at most \(W/2\) of the
\(N_1=mW/(m+2)\) first-shadow targets and leaves
\((1/2-o(1))W\) holes.  More generally, a successful hybrid can place
only \(o(W)\) owner occurrences in alternating components.  Thus
Theorem 4.6 supplies a reserve module, not a bulk factor architecture.

## 5. Exact cycle-master formulation and LP dual

Theorem 1.1 also gives a clean Dantzig--Wolfe formulation.  Let
\(\mathscr C\) be the set of directed simple cycles in the injective de
Bruijn graph.  For \(C\in\mathscr C\), let

\[
 a_X(C)=\#\{e\in C:\kappa(e)=X\}.
\]

For every protected lower or upper target \(T\), let \(b_T(C)\) be its
prefix multiplicity on \(C\).  Then the exact integral minimum-component
problem is

\[
 \begin{aligned}
 \min\quad &\sum_{C\in\mathscr C}\xi_C\\
 \text{subject to}\quad
 &\sum_C a_X(C)\xi_C=1 &&(X\in\binom{[n]}m),\\
 &\sum_C b_T(C)\xi_C\ge1 &&(T\text{ protected}),\\
 &\xi_C\in\mathbb Z_{\ge0}.
 \end{aligned}
\tag{5.1}
\]

The owner equations automatically exclude any selected cycle which
repeats an owner, and automatically make distinct selected cycles
state-disjoint.  Hence (5.1) is exactly equivalent to the Boolean rotor
problem, not a relaxation.

Dropping integrality gives the exact fractional cycle master.  Its dual
is

\[
 \boxed{
 \begin{aligned}
 \max\quad
 &\sum_X\alpha_X+\sum_T\beta_T\\
 \text{subject to}\quad
 &\sum_Xa_X(C)\alpha_X+\sum_Tb_T(C)\beta_T\le1
       &&(C\in\mathscr C),\\
 &\alpha_X\in\mathbb R,qquad \beta_T\ge0.
 \end{aligned}}
\tag{5.2}
\]

This is the exact LP dual requested by the circulation formulation.  It
also identifies why ordinary flow integrality is insufficient: the
network part decomposes into cycles, but the owner rows make those cycles
the hyperedges of a set-partitioning problem.  Birkhoff--von Neumann is
the still coarser projection in Corollary 1.2.

For the coefficient-one theorem, exact upper targets can be replaced by
the aggregate cancellation objective \(\mathfrak D_H\) in (2.13).
Theorem 3.4 refutes the simpler sparse-switch surrogate
\(a=o(W/H)\): a low-component integral circulation has
\(a\ge(1/2-o(1))W\).

## 6. Audited frontier

The following statements are proved here.

1. The corrected integral rotor problem is a clustered injective-de
   Bruijn cycle cover (Theorem 1.1), not an ordinary network circulation.
2. Its Johnson projection is doubly stochastic and admits a Birkhoff
   decomposition, but this forgets residence (Corollary 1.2).
3. Lower and complementary upper loads differ by a nested family of
   \(A\)-switch divergences (Theorem 2.2).
4. The crude sparse-switch compiler (2.12) is formally sufficient, but
   impossible in the target regime.  The surviving sufficient quantity
   is aggregate signed-divergence cancellation (Corollary 2.5).
5. Few components force \((1/2-o(1))W\) nonlinear switches (Theorem
   3.4), closing every \(Ha=o(W)\) argument for \(H\to\infty\).
6. All prefix margins, zero signed divergence, and the sharp half-switch
   scale have an exact common fractional point (Corollary 3.5).
7. The maximally long, one-hole-per-wreath run skeleton is owner-degenerate
   and cannot be used (Theorem 4.2); indeed a positive density of short-run
   resets is necessary (Theorem 4.4).
8. Two consecutive run lengths already generate the full state group, so
   no residual subgroup obstruction remains (Proposition 4.5).
9. The remaining fractional relaxation has the exact cycle dual (5.2).

What is not proved is the reduced integral construction:

\[
 \boxed{
 \begin{gathered}
 \text{one de Bruijn arc per middle owner,}\qquad
 C=o(W/m),\\
 \sum_{q\le H}M(L_{m-q})=o(W),\qquad
 \mathfrak D_H(z)=o(W),\qquad H=\sqrt m\,\omega(m)=o(m).
 \end{gathered}}
\tag{6.1}
\]

Theorems 3.4 and 4.4 say that (6.1) must use \(\Theta(W)\) switches and
a positive density of nonuniform short-run resets.  The exact signed
vectors in (2.6) must nevertheless cancel across all protected depths.
The next live construction is therefore a nested Johnson-discrepancy
rounding of the half--half fractional circulation, coupled to the
cycle-master set partitioning problem.  Ordinary sparse repair, ordinary
network flow, and the uniform \(B^{n-2}A\) port rotor are all closed.
