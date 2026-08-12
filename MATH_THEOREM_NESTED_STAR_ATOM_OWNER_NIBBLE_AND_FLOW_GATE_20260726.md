# Nested-star cancellation atoms: the owner nibble works, but de Bruijn flow becomes an orbit constraint

Date: 2026-07-26

Method: exact counting and structural reduction.  No computation or
solver is used.

## 0. Outcome

Let

\[
 n=2m+1,\qquad W=\binom n m.
\]

Proposition 2.8 of
`MATH_THEOREM_BINARY_ROTOR_DEBRUIJN_DIVERGENCE_AND_MINIMAL_SKELETON_20260726.md`
gives a legal three-switch atom whose nested Johnson divergences cancel
at every depth.  This note audits whether standard fixed-uniformity
matching theory can pack those atoms.

There are two sharply different answers.

1. **On middle-owner fibres alone, the answer is yes.**  The canonical
   atom catalogue is an exactly regular 6-uniform multihypergraph.  Its
   owner degree and maximum pair-codegree are

   \[
   D=m^2(m+1)(m-1)^3,
   \]

   \[
   \Delta_2=m(m-1)^2(3m-2),
   \qquad
   \frac{\Delta_2}{D}
     =\frac{3m-2}{m(m+1)(m-1)}=O(m^{-2}).
   \]

   Consequently the fixed-uniformity near-perfect matching theorem
   packs owner-disjoint atoms covering \(W-o(W)\) owner fibres.  These
   atoms contain

   \[
                     (1/2-o(1))W
   \]

   exactly cancelling \(A\)-switches.  This is precisely the switch
   density forced by the global adjacent-swap toll.

2. **This does not yet give a rotor circulation.**  A chosen atom has
   three source de Bruijn arcs and three \(A\)-successor arcs.  The
   successor arcs still need outgoing \(B\)-transitions and the source
   arcs still need incoming ones.  In the atom-only alternating
   completion (with no extra connector arcs), if \(S\) is the set of
   atom sources, exact balance is

   \[
                          \boxed{S=BA(S).}
   \]

   The permutation \(BA\) has orbit length exactly \(m(m+1)\) on every
   state.  Thus the full problem is not an ordinary 6-uniform matching:
   the selected sources must be unions of growing \(BA\)-orbits while
   simultaneously partitioning into nested-star triples and using each
   owner once.

The owner projection therefore has no local degree/codegree obstruction.
The exact remaining gate in this natural bulk model is a
**matching-circulation intersection**: round the uniform fractional
atom solution while preserving the signed de Bruijn flow rows.
Allowing an \(o(W)\) connector leave weakens exact orbit invariance only
near the leave.  Bundling the exact flow rows first creates blocks of
size \(m(m+1)\), outside fixed-uniformity near-perfect matching theory.

## 1. Canonical owner form of a star atom

Choose disjoint sets

\[
 R,E,K\subseteq[n],\qquad
 |R|=|K|=m-1,\quad |E|=3,\quad
 [n]=R\sqcup E\sqcup K,
\]

and a map

\[
                         \rho:E\longrightarrow R.
\]

For \(e\in E\), define the successor and source owners

\[
 Y_e=R\cup\{e\},
 \qquad
 X_e=(R\setminus\{\rho(e)\})\cup(E\setminus\{e\}).
\tag{1.1}
\]

The six sets in (1.1) are distinct: every \(Y_e\) contains exactly one
point of \(E\), whereas every \(X_e\) contains exactly two; within each
triple the omitted point of \(E\) distinguishes the sets.

### Lemma 1.1 (every canonical edge is a legal local atom)

For every \((R,E,K,\rho)\), the six owners in (1.1) are realized by a
nested-star atom of Proposition 2.8.  Moreover there are

\[
                         2((m-1)!)^4
\tag{1.2}
\]

labelled state realizations of each canonical parameter tuple.

#### Proof

Orient the three points of \(E\) cyclically in either of the two ways.
For the switch whose target endpoint is \(e\), use the common suffix
set \(K\), and order the corresponding \(P\)-block so that its final
entry is \(\rho(e)\).  The other \(m-1\) entries of that block may be
ordered arbitrarily.  The common \(K\)-block may also be ordered
arbitrarily.  Proposition 2.8 then gives successor owners \(Y_e\) and
source owners \(X_e\), after merely reindexing \(\rho\) around the
oriented triangle.

There are two orientations, \((m-1)!\) orders of the common suffix, and
\((m-1)!\) orders of the non-final entries of each of the three
\(P\)-blocks.  This is (1.2). \(\square\)

Let \(\mathcal H_{\rm own}\) be the 6-uniform multihypergraph on
\(\binom{[n]}m\) having one edge (1.1) for every tuple
\((R,E,K,\rho)\).  Multiplicity is retained if two parameter tuples
give the same six-set; codegrees below count that multiplicity.  This
is the natural convention for the labelled atom catalogue as well,
because the common factor (1.2) cancels from all normalized counts.

The multiplicities can also be removed without losing quasiregularity.

### Lemma 1.2 (the only parallel canonical atoms)

Let \(\overline{\mathcal H}_{\rm own}\) be the simple support of
\(\mathcal H_{\rm own}\).  A canonical owner edge has four parameter
representations precisely when \(\rho\) is constant, and otherwise has
one.  Consequently

\[
 |E(\overline{\mathcal H}_{\rm own})|
 =|\mathcal A_0|
 \left(1-\frac{3}{4(m-1)^2}\right),
\tag{1.3}
\]

and, by \(S_n\)-transitivity, the simple hypergraph is exactly regular
of degree

\[
 \overline D
 =D\left(1-\frac{3}{4(m-1)^2}\right).
\tag{1.4}
\]

#### Proof

The union of the six owners recovers
\[
 U=R\cup E,\qquad |U|=m+2.
\]
Replace every owner \(X\subset U\) by its omitted pair \(U\setminus X\).
The resulting six-edge graph on \(U\) is the triangle on \(E\), together
with the three spokes
\[
                         \{e,\rho(e)\}\qquad(e\in E).
\]
Any second parameter representation must choose another triangle in
this graph.  Such a triangle consists of two vertices \(e,f\in E\) and
one \(r\in R\), which requires
\(\rho(e)=\rho(f)=r\).  For its three remaining edges to be the required
spokes, the third value of \(\rho\) must also equal \(r\).  Thus a second
representation exists exactly when \(\rho\) is constant.  In that case
the graph is \(K_4\) on \(E\cup\{r\}\), and each of its four triangles
gives one representation.

Constant maps comprise a fraction
\((m-1)/(m-1)^3=1/(m-1)^2\) of all parameter tuples.  Collapsing each
fourfold class proves (1.3).  Relabelling acts transitively on owners,
so the simple support is regular; double-counting its six incidences
per edge and using (2.3) gives (1.4). \(\square\)

## 2. Exact owner degree and pair-codegree

The number of canonical parameter tuples is

\[
 |\mathcal A_0|
 =\binom n{m-1}\binom{m+2}{3}(m-1)^3.
\tag{2.1}
\]

### Theorem 2.1 (exact regularity)

Every owner belongs to

\[
 d_+=d_-=\frac{m^2(m+1)(m-1)^3}{2}
\tag{2.2}
\]

atoms as a successor, respectively as a source.  Hence

\[
                         \boxed{D=2d_+
                         =m^2(m+1)(m-1)^3.}
\tag{2.3}
\]

#### Proof

Fix an owner \(Y\).  To have \(Y=Y_e\), choose \(e\in Y\), choose the
other two points of \(E\) from the \(m+1\) points outside \(Y\), and
choose \(\rho\) arbitrarily.  This gives

\[
 m\binom{m+1}{2}(m-1)^3=d_+.
\]

Fix an owner \(X\).  To have \(X=X_e\), choose the two points
\(E\setminus\{e\}\) inside \(X\), choose the ordered pair
\((e,\rho(e))\) from the complement of \(X\), and choose the other two
values of \(\rho\).  This gives

\[
 \binom m2\,m(m+1)(m-1)^2=d_- =d_+.
\]

The source and successor roles of one atom are disjoint, so the degrees
add. \(\square\)

For two owners \(P,Q\), write

\[
                         j=|P\setminus Q|=|Q\setminus P|.
\]

The following table gives the codegree for prescribed roles.  A plus
means successor and a minus means source.

\[
\begin{array}{c|cc}
 &j=1&j=2\\ \hline
 ++&m(m-1)^3&0\\
 +-&m(m-1)^3&2(m-1)^2\\
 --&m(m-1)^2&4(m-2)(m-1)
\end{array}
\tag{2.4}
\]

All entries vanish for \(j>2\).

### Theorem 2.2 (maximum owner codegree)

For the untyped owner hypergraph,

\[
 \boxed{
 \Delta_2=m(m-1)^2(3m-2),
 \qquad
 \frac{\Delta_2}{D}
 =\frac{3m-2}{m(m+1)(m-1)}=O(m^{-2}).}
\tag{2.5}
\]

#### Proof

For completeness, the reconstruction counts behind (2.4) are as
follows.

* Two successors force their common \((m-1)\)-set \(R\); the third
  endpoint has \(m\) choices and \(\rho\) has \((m-1)^3\) choices.
* For a distance-one successor/source pair, the deleted point of the
  successor and the added endpoint of the source are fixed.  The common
  endpoint has \(m-1\) choices, the omitted endpoint has \(m\) choices,
  and the two unused values of \(\rho\) are free.
* For two distance-one sources, their two differing endpoints are
  fixed.  The third endpoint has \(m-1\) choices, the common deleted
  point of \(R\) has \(m\) choices, and the last value of \(\rho\) is
  free.
* At distance two, choosing which differing points are endpoints gives
  respectively the factors \(2\) and \(4\) in the last column.

Every two owners in one atom lie inside the common \((m+2)\)-set
\(R\cup E\), so \(j>2\) is impossible.

At distance one, sum the \(++\) contribution, the two orientations of
the \(+-\) contribution, and the \(--\) contribution:

\[
 m(m-1)^3+2m(m-1)^3+m(m-1)^2
 =m(m-1)^2(3m-2).
\]

At distance two the corresponding total is
\(4(m-1)(2m-3)\), which is smaller.  Divide by (2.3). \(\square\)

### Corollary 2.3 (owner atoms have a near-perfect matching)

There is an owner-disjoint family of canonical star atoms covering
\(W-o(W)\) middle owners.  It contains

\[
 (1-o(1))\frac W6
\]

atoms and therefore

\[
                         (1/2-o(1))W
\tag{2.6}
\]

pairwise owner-compatible, all-depth-cancelling \(A\)-switches.

#### Proof

Apply the fixed-uniformity near-perfect matching theorem to the exactly
regular simple 6-uniform hypergraph
\(\overline{\mathcal H}_{\rm own}\).  Its degree
\(\overline D=(1-o(1))D\) tends to infinity.  Collapsing parallel edges
can only decrease pair-codegrees, so (2.5) gives
\(\Delta_2(\overline{\mathcal H}_{\rm own})=o(\overline D)\).
Every matched edge covers six owners and contains three switches.
\(\square\)

This is a genuine positive theorem.  It says that owner integrality and
local cancellation do not conflict, and its switch count (2.6) matches
the necessary global switch density.  It does **not** say that the
chosen arcs satisfy de Bruijn balance.

## 3. The exact atom-circulation system

Let \(\mathcal A\) be the fully labelled atom catalogue from Lemma 1.1.
For \(\alpha\in\mathcal A\), write

\[
 I(\alpha)=\{e_1,e_2,e_3\}
\]

for its three source de Bruijn arcs and

\[
 O(\alpha)=A I(\alpha)=\{Ae_1,Ae_2,Ae_3\}
\]

for its three selected \(A\)-successor arcs.  Put

\[
 \Omega(\alpha)=
 \{\kappa(e):e\in I(\alpha)\cup O(\alpha)\}.
\]

By Proposition 2.8, \(|\Omega(\alpha)|=6\).

### Theorem 3.1 (exact alternating atom circulation)

A Boolean vector \(x\in\{0,1\}^{\mathcal A}\) gives an exact
owner-transversal rotor circulation alternating atom \(A\)-transitions
with \(B\)-transitions if and only if

\[
 \sum_{\alpha:X\in\Omega(\alpha)}x_\alpha=1
 \qquad\left(X\in\binom{[n]}m\right),
\tag{3.1}
\]

and

\[
 \sum_{\alpha:e\in I(\alpha)}x_\alpha
 =
 \sum_{\alpha:e\in B O(\alpha)}x_\alpha
 \qquad(e\in\mathcal E).
\tag{3.2}
\]

Equivalently, if

\[
 S=\bigcup_{\alpha:x_\alpha=1}I(\alpha),
\]

then

\[
                              \boxed{S=BA(S).}
\tag{3.3}
\]

#### Proof

Equation (3.1) is precisely the owner equation for the six selected
arcs of every atom.  Inside an atom, each \(e\in I(\alpha)\) uses the
transition \(e\to Ae\).  Every \(f\in O(\alpha)\) must then use its
\(B\)-transition \(f\to Bf\), and the target \(Bf\) must be a source of
some selected atom.  This is exactly (3.2).  Since \(O=A I\), (3.2) is
equivalent to (3.3).  Conversely (3.1)--(3.2) assign one incoming and
one outgoing transition to every selected arc, hence give the clustered
de Bruijn cycle cover. \(\square\)

The matrix in (3.1)--(3.2) is sparse: an atom column has six positive
owner entries and three positive and three negative flow entries.  The
uniform assignment

\[
 x_\alpha=\frac1{D_{\rm lab}},
 \qquad
 D_{\rm lab}=2((m-1)!)^4D,
\tag{3.4}
\]

satisfies (3.1) and (3.2) exactly.  Indeed the owner rows have degree
\(D_{\rm lab}\), and relabelling symmetry gives equal source and
\(BA\)-image degree at every state.  Thus the full gate has an exact
fractional point; its unresolved part is integral rounding with signed
flow preservation.

### Proposition 3.2 (the flow rows are not matching vertices)

Adding the de Bruijn ports to the six owner vertices does not turn
(3.1)--(3.2) into an ordinary fixed-uniformity matching problem.

#### Proof

A matching constraint says that a port is used at most once.  Equation
(3.2) instead says that its positive and negative uses are equal.  In
particular a source occurrence at \(e\) must be accompanied by an output
occurrence at the same \(e\), rather than avoided by it.  Splitting the
two signs into separate vertex copies loses this equality.

There is also a scale mismatch.  The number of labelled atoms through
a fixed source arc is

\[
 d_{\rm state}=(m-1)^3((m-1)!)^2,
\tag{3.5}
\]

whereas the owner degree is \(D_{\rm lab}\), larger by a factorial
factor.  The selected solution uses only \(W/2\) source states among
\(|\mathcal E|=n!\) possible states.  Therefore the flow rows are sparse
signed equalities, not a second near-regular vertex class that a nibble
could cover. \(\square\)

## 4. The growing-orbit form of the remaining gate

Let \(C=BA\).  On a permutation state,

\[
 C(x_1,\ldots,x_n)
  =(x_3,x_4,\ldots,x_{n-1},x_1,x_n,x_2).
\tag{4.1}
\]

### Lemma 4.1 (exact \(BA\)-orbit length)

Every \(C\)-orbit on permutation states, and hence on de Bruijn arcs,
has length

\[
                              \boxed{m(m+1).}
\tag{4.2}
\]

#### Proof

The coordinate permutation in (4.1) has two cycles, of lengths \(m\)
and \(m+1\).  Its order is therefore \(\operatorname{lcm}(m,m+1)
=m(m+1)\).  Since all coordinates of a state are distinct, no
nonidentity coordinate permutation can fix it, so every state orbit has
the full length. \(\square\)

### Corollary 4.2 (orbit normal form)

An exact alternating atom circulation is equivalently the following
two-level object.

1. Choose a family of full \(BA\)-orbits of source states.
2. Partition their union into legal nested-star triples.
3. Require the owner sets of every source \(e\) and successor \(Ae\) to
   partition \(\binom{[n]}m\).

Every selected \(BA\)-orbit produces one rotor component of length
\(2m(m+1)\).  Hence, whenever the exact divisibilities permit such a
solution, it automatically has

\[
 C=\frac{W}{2m(m+1)}=o(W/m)
\]

components.  In the asymptotic compiler one may instead leave
\(o(W)\) owners to absorb the parity and divisibility residues; obtaining
a leave small enough for the protected-height error ledger is part of
the open completion problem.

The orbit blocks in item 1 have growing size \(m(m+1)\).  Consequently,
after eliminating the signed flow rows, the effective packing problem
is no longer fixed-uniformity.  Moreover the star triples in item 2 may
join states from different \(BA\)-orbits, so even the existence of the
required orbitwise triple factor is a coupled constraint rather than a
local packet check.

In fact, for the canonical atoms they must join different orbits.

### Lemma 4.3 (one source per \(BA\)-orbit in an atom)

For \(m\ge3\), the three source states of a canonical nested-star atom
belong to three distinct \(BA\)-orbits.

#### Proof

The two coordinate cycles of \(BA\) are the odd positions, of length
\(m\), and the even positions together with position \(n\), of length
\(m+1\).  The common ordered suffix block of a canonical atom occupies
positions \(m+2,\ldots,n-1\).  For \(m\ge3\), this interval contains at
least one odd and one even position.

Suppose two distinct powers \(C^a\pi,C^b\pi\), \(C=BA\), had the same
ordered suffix block.  Equality at an odd suffix position, and
distinctness of all coordinate labels, imply \(a-b\equiv0\pmod m\).
Equality at an even suffix position implies
\(a-b\equiv0\pmod{m+1}\).  Hence
\(a-b\equiv0\pmod{m(m+1)}\), so the two states are equal, a
contradiction. \(\square\)

Thus, after choosing the source orbits, the atom partition is a
3-uniform incidence structure on those orbits in which every chosen
orbit has degree exactly \(m(m+1)\), with an additional phase/state
used on each incidence.  Fixed edge size at this quotient level does
not remove the growing-degree exact-factor and owner-transversality
constraints.

The local statistics of this orbit projection are nevertheless
favourable.

### Proposition 4.4 (orbit-projected atom codegrees)

Let \(\mathcal G_{\rm orb}\) be the 3-uniform multihypergraph whose
vertices are \(BA\)-orbits of source states and whose edges are the
three orbit labels of a fully labelled atom.  Put
\(L=m(m+1)\).  Then every orbit vertex has degree

\[
 D_{\rm orb}
 =L(m-1)^3((m-1)!)^2,
\tag{4.3}
\]

and

\[
 \Delta_2(\mathcal G_{\rm orb})
 \le L(m-1)(m-1)!,
\qquad
 \frac{\Delta_2(\mathcal G_{\rm orb})}{D_{\rm orb}}
 \le\frac1{(m-1)^2(m-1)!}.
\tag{4.4}
\]

#### Proof

A fixed source state lies in
\((m-1)^3((m-1)!)^2\) labelled atoms, as in (3.5).  By Lemma 4.3 an
atom uses at most one state of a fixed orbit, so summing over its \(L\)
states proves (4.3).

Two fixed source states can lie in one atom only if they have the same
ordered suffix block.  If compatible, their two directed endpoint
edges determine the endpoint triangle, its orientation, the common
set \(R\), and the two fixed \(P\)-blocks.  Only the third \(P\)-block
remains; it has at most
\((m-1)(m-1)!\) orders ending in \(R\).

By the proof of Lemma 4.3, a \(BA\)-orbit contains at most one state
with any prescribed ordered suffix block.  Hence two orbit vertices
offer at most \(L\) compatible state pairs.  Multiplying the last two
bounds gives (4.4). \(\square\)

Thus a standard matching theorem can also choose many **single**
atom incidences on distinct orbit vertices.  The required object is
different: an activated orbit must contribute all \(L\) of its states,
each exactly once, whereas an inactive orbit contributes none.  This
all-or-none \(L\)-factor condition is the flow equation in quotient
form.

There is a tempting but invalid way to try to meet that condition:
take three \(BA\)-orbits related by automorphisms of the two position
cycles and match equal suffix phases.  Ordered suffixes make this
rigid.

### Proposition 4.5 (no exact three-orbit suffix-grid packet)

Let \(m=2r+1\ge5\).  There do not exist three distinct \(BA\)-orbits
whose states can be partitioned phase-by-phase into canonical
nested-star atoms, one state from each orbit in every atom.

#### Proof

The two position cycles of \(BA\) have lengths
\[
 p=m=2r+1,\qquad q=m+1=2r+2.
\]
Write the labels around them as directed cyclic sequences
\[
 A=(a_0,\ldots,a_{p-1}),\qquad
 B=(b_0,\ldots,b_{q-1}).
\]
The common suffix positions
\[
                         \{m+2,\ldots,2m\}
\]
meet each position cycle in a directed interval of length \(r\).
Because \(\gcd(p,q)=1\), the \(pq\) powers of \(BA\) run through every
pair of phase shifts.  Hence the ordered suffix deck of the orbit is
the Cartesian product
\[
 \mathcal K(A,B)=
 \left\{\operatorname{interleave}
   (A[u,u+r),B[v,v+r)):(u,v)\in\mathbb Z_p\times\mathbb Z_q
 \right\}.
\tag{4.5}
\]

A phase-by-phase partition into canonical atoms forces the three
orbits to have the same ordered suffix deck, because the three source
states of every atom have one common ordered suffix.

Project the odd and even positions of every word in (4.5).  This
recovers the deck of all directed ordered \(r\)-windows of \(A\), each
with multiplicity \(q\), and the analogous deck of \(B\), each with
multiplicity \(p\).  Since \(r\ge2\), the ordered \(r\)-window deck of a
cyclic sequence with distinct labels determines its directed cyclic
order: the unique window beginning with a label records its successor
in its second position.  Thus equal suffix decks force \(A\) and \(B\)
separately to agree up to rotations.

By the Chinese remainder theorem, arbitrary rotations on the
\(p\)- and \(q\)-cycles are realized simultaneously by one power of
\(BA\).  The supposedly distinct state orbits are therefore the same
orbit, contradicting Lemma 4.3. \(\square\)

The non-rotational elements of
\(D_m\times D_{m+1}\) preserve the **sets** of cyclic intervals, but
reverse at least one directed ordered-window deck.  They therefore do
not evade Proposition 4.5.  In fact only four protected depths already
retain the rigidity.

### Corollary 4.6 (the three-orbit grid packet also fails at finite height)

Let \(m=2r+1\) and \(H\ge4\).  Three distinct full \(BA\)-orbits cannot
be phase-matched so that every phase triple cancels its switch
divergence at every depth \(0\le q\le H\).

#### Proof

For a source state with full ordered suffix
\(\mathbf K=(k_1,\ldots,k_{m-1})\), the nested core sets through depth
\(H\) determine
\[
 \left(k_1,\ldots,k_H,\ \{k_{H+1},\ldots,k_{m-1}\}\right):
\]
the difference between two consecutive core sets reveals the next
ordered symbol.  Hence a phase-by-phase cancellation partitions the
three orbits by identical height-\(H\) suffix flags.

In the two-cycle representation used in Proposition 4.5, projecting
the first \(H\) symbols of these flags onto alternating positions gives
all directed \(\lceil H/2\rceil\)-windows of \(A\) and all directed
\(\lfloor H/2\rfloor\)-windows of \(B\).  When \(H\ge4\), both lengths
are at least two, so each deck determines its directed cyclic order.
The Chinese remainder argument from Proposition 4.5 again says the
three \(BA\)-orbits coincide, a contradiction. \(\square\)

Thus a surviving orbitwise completion cannot repeatedly use one fixed
triple of orbit grids.  Its atom partners must vary with phase across a
larger incidence network.  That more global \(L\)-factor problem is not
excluded here.

## 5. Precise frontier

What is now proved:

* nested-star atoms exist with no local owner collision;
* their owner hypergraph is exactly regular with relative codegree
  \(O(m^{-2})\);
* standard fixed-uniformity matching packs \((1/2-o(1))W\) cancelling
  switches on \(W-o(W)\) owners;
* the fully constrained atom system has an exact uniform fractional
  solution;
* in the atom-only alternating system, exact de Bruijn flow is
  equivalent to union of \(BA\)-orbits of length \(m(m+1)\), and would
  automatically solve the component-count gate.

What is not proved:

\[
\boxed{
\begin{minipage}{0.87\linewidth}
Round the uniform atom solution so that (i) owner rows are integral,
(ii) the selected source states are unions of \(BA\)-orbits up to a
sufficiently small leave, and (iii) those source states partition into
nested-star triples.  For a growing protected height, the leave must
also be quantitatively small enough that its uncancelled divergence is
\(o(W)\), not merely an unspecified \(o(W)\).
\end{minipage}}
\]

Thus fixed-uniformity matching theory rigorously solves the owner
projection, but it does not solve the full atom circulation.  The next
theorem is a structured orbit-rounding/absorption theorem, not another
degree-codegree estimate for the 6-uniform owner catalogue.
