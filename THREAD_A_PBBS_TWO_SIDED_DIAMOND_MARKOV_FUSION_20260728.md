# Thread A: two-sided diamond Markov circuits and PBBS component fusion

Date: 2026-07-28

Status: unconditional two-sided table calculus, a minimum-support physical
component-merging circuit, and a literal odd-graph sufficient switch theorem.
Its three-owner, rank-\((m-2)\) effect is computed exactly.  The
four-owner \(q=3\) collar and every larger depth, existence of enough such
switches in PBBS, and the compiler owner-Hall extension remain unproved.

## 0. Outcome

The one-sided coloured Euler flow is not the correct PBBS surgery object.
A projected Johnson edge has two inseparable colours

\[
 R=A\cap B,\qquad U=A\cup B.
\]

PBBS already supplies an exact, generally disconnected, two-sided table:
every \(U\)-column occurs once, every intermediate owner has degree two,
every \(R\)-row is nonempty, and the complete deeper PBBS flag tower is
supported.

This note proves the following.

1. Fixed \(R\)- and \(U\)-margins have the usual alternating flag-circuit
   Markov lattice, but a table circuit lifts to a physical factor move only
   when its individual middle-state boundary also vanishes.
2. Every four-cell rectangle has a nonzero four-state boundary.  The
   canonical reciprocal two-rectangle repair is physical but merely swaps
   two whole vertex neighbourhoods, so it preserves the complete cycle
   length multiset.
3. There is a minimum-support six-cell physical circuit.  Its lifted
   symmetric difference is one alternating \(C_6\), and it merges three
   factor cycles whenever its three negative edges lie in three distinct
   cycles.
4. A common-retained-label realization of this circuit is a literal
   alternating \(C_6\) switch in the odd graph.  It automatically satisfies
   the undirected transpose condition, preserves every upper column and
   every lower multiplicity exactly, and merges three PBBS components
   under an explicit placement condition.  An explicit direction condition
   supplies rooted orientation coherence.
5. Only six projected states change their three-owner
   (trace-\(q=2\)) labels.  Their exact port substitutions, safety
   inequalities, and signed target ledger are displayed below.  The actual
   four-owner \(q=3\) row needs a wider collar and is not computed here.

Thus exact two-sided component fusion is algebraically possible.  The
remaining obstruction is not the table margins or component topology; it is
finding these literal circuits in PBBS with a support-safe three-owner
transition pairing and compatible collars from trace depth \(q=3\) onward.

## 1. The exact two-sided PBBS table

Fix a ground set \(\Omega\), and let

\[
 \mathcal R=\binom{\Omega}{s-1},\qquad
 \mathcal A=\binom{\Omega}{s},\qquad
 \mathcal U=\binom{\Omega}{s+1}.
\]

A diamond is a pair

\[
 (R,U),\qquad R\in\mathcal R,\quad U\in\mathcal U,\quad R\subset U.
\]

If \(U\setminus R=\{a,b\}\), its middle lift is the Johnson edge

\[
 e(R,U)=(R+a)(R+b).
\tag{1.1}
\]

For a nonnegative integral table \(z=(z_{R,U})\), define

\[
 c_R^-(z)=\sum_{U\supset R}z_{R,U},\qquad
 c_U^+(z)=\sum_{R\subset U}z_{R,U},
\tag{1.2}
\]

and the middle-state degrees

\[
 d_A(z)=\sum_{R\subset A\subset U}z_{R,U}.
\tag{1.3}
\]

The lifted multigraph \(G_z\) has \(z_{R,U}\) copies of (1.1).

### Proposition 1.1 (PBBS is an exact disconnected diamond table)

Let \(F_{\rm P}\) be the PBBS odd-graph factor on the \(m\)-sets of
\(\Omega=[2m+1]\), written locally as

\[
 \cdots,A_i,A_{i+1},A_{i+2},\cdots .
\]

Put

\[
 R_i=A_i\cap A_{i+2},\qquad
 U_i=A_i\cup A_{i+2}.
\]

Then

\[
 U_i=\overline{A_{i+1}}.
\tag{1.4}
\]

Consequently its step-two projection gives a binary table \(z^{\rm P}\)
such that

\[
 c_U^+(z^{\rm P})=1\quad(U\in\mathcal U),\qquad
 d_A(z^{\rm P})=2\quad(A\in\mathcal A),
\tag{1.5}
\]

\[
 1\le c_R^-(z^{\rm P})\le3.
\tag{1.6}
\]

Every rank-\((m-2)\) PBBS target is also present, with load at most
\(\binom52=10\).

#### Proof

Both \(A_i\) and \(A_{i+2}\) are \(m\)-subsets of
\(\overline{A_{i+1}}\), an \((m+1)\)-set.  They are distinct, so their
union is the whole complement, proving (1.4).  Translation of the index
enumerates every odd-graph vertex once, hence every upper column once.
The projected factor has degree two at every intermediate state.  The
PBBS all-depth flag theorem at depths one and two gives (1.6) and the
rank-\((m-2)\) assertion. \(\square\)

Connectivity is not asserted in Proposition 1.1.  It is exactly the
missing Euler condition on \(G_{z^{\rm P}}\).

## 2. The table lattice and the physical state boundary

For a signed table vector \(g\), define

\[
 (Cg)_U=\sum_{R\subset U}g_{R,U},\qquad
 (Lg)_R=\sum_{U\supset R}g_{R,U},
\tag{2.1}
\]

\[
 (Dg)_A=\sum_{R\subset A\subset U}g_{R,U}.
\tag{2.2}
\]

Thus exact upper columns, exact lower loads, and exact middle degrees are
preserved precisely by

\[
 Cg=0,\qquad Lg=0,\qquad Dg=0.
\tag{2.3}
\]

If only lower support is required, \(Lg=0\) is replaced by

\[
 c_R^-(z)+(Lg)_R\ge1.
\tag{2.4}
\]

### Theorem 2.1 (flag-circuit Markov lattice)

The integer kernel of \((C,L)\) is generated conformally by the signed
simple alternating even cycles of the bipartite flag graph

\[
 \Gamma=(\mathcal R,\mathcal U;\ R\subset U).
\tag{2.5}
\]

A move in this table fibre is a physical fixed-endpoint factor move if
and only if it also lies in \(\ker D\) and its negative cells are available
while its positive cells respect the required simplicity.

#### Proof

At every row and column vertex, the positive and negative incidences of a
kernel vector balance.  Alternately follow a positive and a negative edge
until a flag-graph circuit closes; subtract the minimum absolute
coefficient on that circuit and iterate.  This gives a conformal
decomposition into simple alternating even circuits.

The lift of a cell contributes one incidence at each of its two
intermediate states.  Therefore (2.2) is exactly the signed middle-degree
change.  This proves the second assertion. \(\square\)

Point degrees do not detect the physical obstruction.  For one diamond
with intermediate states \(X,Y\),

\[
 \mathbf1_X+\mathbf1_Y=\mathbf1_R+\mathbf1_U.
\tag{2.6}
\]

Hence \(Cg=Lg=0\) automatically preserves the aggregate point-degree
vector of the middle states even when \(Dg\ne0\).  More generally,
\(Cg=Dg=0\) forces

\[
 \sum_R(Lg)_R\,\mathbf1_R=0.
\tag{2.7}
\]

Thus any lower-histogram change under fixed upper columns and fixed
middle degrees is a point-degree-neutral design trade.

## 3. Rectangles fail; the first physical circuit is a six-cycle

### Lemma 3.1 (exact rectangle boundary)

Let \(K\in\binom{\Omega}{s}\), let \(a,b\in K\) be distinct, and let
\(p,q\notin K\) be distinct.  The flag rectangle

\[
\begin{aligned}
 \rho={}&
 [K-a,K+q]+[K-b,K+p]\\
 &-[K-a,K+p]-[K-b,K+q]
\end{aligned}
\tag{3.1}
\]

has \(C\rho=L\rho=0\), but

\[
 D\rho=
 [K-a+q]+[K-b+p]-[K-a+p]-[K-b+q].
\tag{3.2}
\]

The four displayed states are distinct.  Therefore no isolated rectangle
is a physical cyclic or fixed-endpoint factor move.

#### Proof

The row and column cancellations are the rectangle identities.  Every
cell in (3.1) has \(K\) as one middle endpoint; those four copies cancel.
The other endpoints give (3.2), and their distinctness follows from the
distinct deleted and inserted coordinates. \(\square\)

For a path with movable endpoint stubs, the two positive and two negative
state defects in (3.2) could only be paid by moving both endpoints.  That
changes the nested boundary flags and is outside the fixed-boundary claim.

### Lemma 3.2 (the reciprocal rectangle is topologically sterile)

Pair a rectangle on opposite middle centres

\[
 X=C+\{a,b\},\qquad Y=C+\{c,d\},
\]

where \(|C|=s-2\) and \(a,b,c,d\) are distinct, with its oppositely
oriented reciprocal rectangle.  Among repairs using one additional
rectangle, this reciprocal choice is unique.  The combined eight-cell move
lies in \(\ker(C,L,D)\).

Whenever it is applicable to a two-factor, it merely swaps the complete
selected neighbourhoods of \(X\) and \(Y\).  Hence the old and new lifted
graphs are isomorphic by the transposition \(X\leftrightarrow Y\), and
their cycle-length multisets are identical.

#### Proof

The four peripheral states are

\[
 C+ac,\quad C+ad,\quad C+bc,\quad C+bd.
\]

They have exactly two common Johnson neighbours, namely \(X\) and \(Y\).
Thus cancellation of the four-state boundary (3.2) by one further
rectangle forces the reciprocal rectangle at \(Y\).  A distributed
combination of larger circuits is not excluded.  The reciprocal repair
assigns to \(X\) the old two
neighbours of \(Y\), and conversely.  Since both centres have degree two,
no other selected edge is incident with either centre.  All remaining
edges are unchanged, proving the transposition statement. \(\square\)

The first component-changing circuit is smaller and is not a union of a
reciprocal rectangle pair.

### Theorem 3.3 (minimum-support physical \(C_6\) circuit)

Let \(|C|=s-2\), and take distinct \(1,2,3,4\notin C\).  Put

\[
\begin{array}{lll}
R_1=C+1,&R_2=C+2,&R_3=C+3,\\
U_1=C+134,&U_2=C+124,&U_3=C+234.
\end{array}
\tag{3.3}
\]

Delete the three cells

\[
 (R_1,U_1),\qquad(R_2,U_2),\qquad(R_3,U_3)
\tag{3.4}
\]

and add

\[
 (R_1,U_2),\qquad(R_2,U_3),\qquad(R_3,U_1).
\tag{3.5}
\]

The resulting signed vector \(g_6\) lies in
\(\ker(C,L,D)\).  Its deleted Johnson edges are

\[
 (C+13)(C+14),\quad
 (C+12)(C+24),\quad
 (C+23)(C+34),
\tag{3.6}
\]

and its added edges are

\[
 (C+12)(C+14),\quad
 (C+23)(C+24),\quad
 (C+13)(C+34).
\tag{3.7}
\]

Their symmetric difference is the alternating cycle

\[
 C+13,\ C+14,\ C+12,\ C+24,\ C+23,\ C+34,\ C+13.
\tag{3.8}
\]

No nonzero physical fixed-margin circuit has support below six cells.
If the three edges in (3.6) lie in three distinct factor cycles, the
switch merges those cycles into one.

#### Proof

Every row and every column in (3.3) occurs once with each sign.
Inspection of (3.6)--(3.7) shows that every one of the six intermediate
states has one deleted and one added incidence, so \(Dg_6=0\).
Equation (3.8) follows.

Every nonzero vector in \(\ker(C,L)\) contains an even flag circuit and
therefore has support at least four.  Moreover every incident vertex of
its simple bipartite support graph has at least two supported edges, one
of each sign.  A five-edge bipartite graph cannot have minimum degree two:
with at most four incident vertices it has at most the four edges of
\(K_{2,2}\); with five vertices one bipartition shore has at least three
vertices and already demands at least six incidences; and with at least
six vertices the degree sum requires at least six edges.  Hence support
below six is exactly a four-cell rectangle, excluded
by Lemma 3.1.  Thus six is minimum.

If the three deleted edges lie in distinct cycles, deleting one edge from
each leaves three paths.  Contract them.  The three added edges form a
triangle on the contracted paths, hence one cycle containing all three.
\(\square\)

### Proposition 3.4 (general component ledger)

Let \(F=G_z\) be a two-factor and let \(g\) be any applicable physical
move.  Delete the negative edges of \(g\), contract every resulting path
piece, and insert the positive edges in the quotient.  If \(h\) old cycles
were touched and the positive quotient has \(p\) connected components,
then

\[
 \boxed{c(F+g)-c(F)=p-h.}
\tag{3.9}
\]

In particular, all touched cycles merge into one if and only if the
positive quotient is connected.

For orientation coherence, every positive edge must run from the tail of
one inherited oriented path to the head of another, and the directed
quotient must be one directed cycle.

#### Proof

Removing the negative edges partitions the touched old cycles into the
contracted path pieces.  Re-expanding a quotient component gives exactly
one component of the switched factor.  Untouched cycles contribute
equally on both sides, proving (3.9).  The directed statement is the same
contraction with inherited path orientations retained. \(\square\)

## 4. A literal odd-graph \(C_6\) preserving both table shores

The circuit in Theorem 3.3 is a Johnson-table circuit.  Now specialize
to \(s=m\) on the ground set \([2m+1]\).  An arbitrary such
circuit need not be the square of an odd-graph switch.  The following
common-retained-label configuration gives an exact literal lift.

For a table on \([2m+1]\), define its copy-incidence matrix by

\[
 M_{X,N}(z)=
 \sum_{\substack{R\subset X\subset U\\U=\overline N}}z_{R,U}.
\tag{4.0}
\]

When every upper column has load one and every middle state has degree
two, both shores of \(M(z)\) have degree two.

### Proposition 4.0 (undirected odd-factor transpose invariant)

Such a table is the step-two projection of an undirected odd-graph factor
if and only if

\[
 \boxed{M(z)=M(z)^{\mathsf T}.}
\tag{4.0a}
\]

Consequently a signed Johnson-table move \(g\) based at PBBS has an
undirected odd-factor lift only if

\[
 M(g)=M(g)^{\mathsf T}.
\tag{4.0b}
\]

#### Proof

A selected column \(U=\overline N\) joins its two intermediate states
\(X,Y\); equivalently it records the two odd incidences \(XN,YN\).
These incidences come from an undirected graph on the common vertex set
exactly when their matrix is symmetric.  In that case the common row and
column degree two makes the graph an odd-graph factor, and taking the two
neighbours of every \(N\) recovers the original table. \(\square\)

A lone six-cell circuit from Theorem 3.3 need not satisfy (4.0b).  The
condition is an undirected lift criterion; a prescribed rooted orientation
or phase is additional.  The configuration below supplies the transpose
companion and the needed orientation explicitly.

Let \(m\ge3\), and decompose

\[
 \Omega=C\mathbin{\dot\cup}D\mathbin{\dot\cup}\{1,2,3,4\},
\qquad |C|=m-2,\quad |D|=m-1.
\tag{4.1}
\]

Choose \(d\in D\) and put \(D'=D-\{d\}\).  Define the twelve \(m\)-sets

\[
\begin{array}{lll}
A_1=C+14,&A_2=C+24,&A_3=C+34,\\
N_1=D+2,&N_2=D+3,&N_3=D+1,\\
P_1=C+13,&P_2=C+12,&P_3=C+23,\\
Q_1=D'+23,&Q_2=D'+13,&Q_3=D'+12.
\end{array}
\tag{4.2}
\]

### Theorem 4.1 (literal two-sided neutral \(C_6\) fusion)

Suppose an odd-graph two-factor \(F\) contains the undirected local segments

\[
 P_i-N_i-A_i-Q_i
 \qquad(i=1,2,3)
\tag{4.3}
\]

as local path segments.  Replace

\[
 A_1N_1,\quad A_2N_2,\quad A_3N_3
\tag{4.4}
\]

by

\[
 A_1N_2,\quad A_2N_3,\quad A_3N_1.
\tag{4.5}
\]

Then:

1. (4.5) is a literal alternating \(C_6\) odd-graph switch and produces
   another odd-graph two-factor \(F'\);
2. the step-two diamond tables of \(F,F'\) have exactly the same
   \(U\)-column vector and exactly the same \(R\)-row vector;
3. their middle degrees are both identically two; and
4. if the three edges (4.4) belong to three distinct components, \(F'\)
   merges those components into one.

If the old components are oriented so that every deleted arc is
\(A_i\to N_i\), then the new arcs

\[
 A_1\to N_2,\qquad A_2\to N_3,\qquad A_3\to N_1
\tag{4.6}
\]

make the fusion orientation-coherent.

#### Proof

The six sets

\[
 A_1,N_2,A_2,N_3,A_3,N_1
\]

form an alternating odd-graph \(C_6\): successive displayed sets are
disjoint, its three old edges are (4.4), and its other three edges are
(4.5).  Degree two is therefore preserved.

For any vertex \(V\) of an odd factor, its two neighbours are distinct
\(m\)-subsets of the \((m+1)\)-set \(\overline V\).  Their union is
\(\overline V\).  Thus every odd-factor switch preserves one projected
upper column for every \(V\); the \(U\)-column vector is unchanged.

Only the projected upper columns

\[
 \overline{N_1},\overline{N_2},\overline{N_3},
 \overline{A_1},\overline{A_2},\overline{A_3}
\]

(corresponding to odd centres \(N_1,N_2,N_3,A_1,A_2,A_3\))
change their lower colours.  Direct intersection gives

\[
\begin{array}{c|ccc}
\text{upper column}&\overline{N_1}&\overline{N_2}&\overline{N_3}\\ \hline
\text{old lower colour}&C+1&C+2&C+3\\
\text{new lower colour}&C+3&C+1&C+2,
\end{array}
\tag{4.7}
\]

and

\[
\begin{array}{c|ccc}
\text{upper column}&\overline{A_1}&\overline{A_2}&\overline{A_3}\\ \hline
\text{old lower colour}&D'+2&D'+3&D'+1\\
\text{new lower colour}&D'+3&D'+1&D'+2.
\end{array}
\tag{4.8}
\]

Both triples are merely permuted.  All other columns are unchanged, so
the complete lower multiplicity vector is preserved.

Finally, remove (4.4) and contract the three old components.  The new
edges (4.5) form a directed or undirected triangle on the three contracted
paths.  This proves the last two assertions. \(\square\)

The common elements \(4\in C+\{4\}\) and \(d\in D\) are exactly the two
common retained omitted labels on the opposite core sides of the odd
hexagon.  Without this common-retained-label condition, the two triples
in (4.7)--(4.8) need not be permutations.

At the table level, the six changed upper columns split into two copies of the
minimum circuit of Theorem 3.3, one on core \(C\) and one on core \(D'\).
Together they satisfy the transpose condition required by an undirected
odd factor.  The explicit directions (4.6) additionally give orientation
coherence for this placement.  No general rooted phase theorem is inferred,
whereas a lone Johnson \(C_6\) circuit need not even have the undirected
transpose lift.

## 5. Exact three-owner (\(q=2\)) transition effect

The labels in this section have rank \(s-2\).  They are the third row in
the four-row convention \((s+1,s,s-1,s-2)\), but they are the
three-owner, trace-\(q=2\) intersections
\(T_i\cap T_{i+1}\cap T_{i+2}\).  They are **not** the four-owner
trace-\(q=3\) row.

For a degree-two projected table, let

\[
 h_{X,a}=\sum_{y\notin X}z_{X-a,X+y}.
\tag{5.1}
\]

Thus \(h_{X,a}\) counts incident projected edge copies whose lower facet
at \(X\) is \(X-a\).  A correct local three-owner state has

\[
 \sum_{a\in X}h_{X,a}=2,\qquad h_{X,a}\le1.
\tag{5.2}
\]

If the two nonzero types are \(a,b\), its three-owner label is

\[
 S_X=X-\{a,b\}.
\tag{5.3}
\]

### Theorem 5.1 (six-port three-owner ledger for Theorem 4.1)

Under the switch of Theorem 4.1, the changed half-edge type is unchanged
at \(A_1,A_2,A_3\) (type \(4\)) and at \(N_1,N_2,N_3\) (type \(d\)).
It changes only at the following six projected states:

\[
\begin{array}{c|ccc}
X&P_1=C+13&P_2=C+12&P_3=C+23\\ \hline
\eta_X^-&3&1&2\\
\eta_X^+&1&2&3,
\end{array}
\tag{5.4}
\]

\[
\begin{array}{c|ccc}
X&Q_1=D'+23&Q_2=D'+13&Q_3=D'+12\\ \hline
\eta_X^-&3&1&2\\
\eta_X^+&2&3&1.
\end{array}
\tag{5.5}
\]

Let \(t_X\) be the type of the unchanged incident projected edge at one
of these six states.  Assume the old factor is three-owner correct there,
equivalently

\[
 t_X\ne\eta_X^-
 \qquad\text{at all six states.}
\tag{5.5a}
\]

Then:

1. the new chronology has the correct three-owner rank at \(X\) if and only if

   \[
     t_X\ne\eta_X^+;
   \tag{5.6}
   \]

2. its local target changes by

   \[
   X-\{\eta_X^-,t_X\}
   \longmapsto
   X-\{\eta_X^+,t_X\};
   \tag{5.7}
   \]

3. the complete signed three-owner change is

   \[
   \delta^{(2)}=
   \sum_{X\in\{P_1,P_2,P_3,Q_1,Q_2,Q_3\}}
   \left(
   [X-\{\eta_X^+,t_X\}]
   -
   [X-\{\eta_X^-,t_X\}]
   \right);
   \tag{5.8}
   \]

4. \(\delta^{(2)}\) has zero point-degree vector.

If the old factor is three-owner correct and \(\mu_2\) is its old
correct-rank target histogram, then the switched factor is three-owner
correct with complete support if and only if (5.6) holds at all six states
and

\[
 \mu_2(S)+\delta^{(2)}(S)\ge1
 \qquad\text{for every rank-}(m-2)\text{ target }S.
\tag{5.9}
\]

Exact three-owner multiplicities are preserved under the stronger
condition \(\delta^{(2)}=0\).

#### Proof

Equations (4.7)--(4.8), read at their two intermediate endpoints, give
(5.4)--(5.5).  The other endpoint in each projected visit is unchanged,
so its type is \(t_X\).  Two equal types remove only one point from \(X\);
two distinct types give exactly (5.3).  This proves (5.6)--(5.8).

In each of (5.4) and (5.5), the old and new type multisets are both
\{1,2,3\}.  The unchanged partners occur once with each sign at the same
state.  Expanding the six incidence-vector differences in (5.8) therefore
cancels every point coordinate.  Finally (5.9) is the exact targetwise
support condition. \(\square\)

The zero point-degree conclusion does not imply (5.9).  A PBBS target may
have load one, so last-occurrence protection is a genuine statewise
condition.

## 6. The general three-owner pairing system

The local ledger has an exact integral formulation which does not assume
degree two or a previously chosen ordering.

For \(a\ne b\in A\), let \(p_{A,\{a,b\}}\) be the number of local
transition pairs using half-edge types \(a,b\), and let \(u_{A,a}\)
be the number of endpoint stubs of type \(a\).  Then exact pairing of all
distinguishable half-edge copies is equivalent to

\[
 \sum_{b\in A\setminus\{a\}}p_{A,\{a,b\}}+u_{A,a}
   =h_{A,a}.
\tag{6.1}
\]

For prescribed rank-\((s-2)\) three-owner loads \(d_S\), one additionally needs

\[
 \sum_{\substack{A\supset S\\|A\setminus S|=2}}
 p_{A,A\setminus S}=d_S.
\tag{6.2}
\]

The total number of stubs is zero for a cyclic carrier and two for a
linear one.  Every nonnegative integral solution of (6.1)--(6.2) can be
implemented by pairing the distinguishable edge copies of each type.  It
spells one common chronology exactly when the transition graph on diamond
edge copies is connected: one cycle in the cyclic case, or one path in the
two-stub case.

This is the proper next layer after a two-sided \(z\)-table has been found.
The system is local in states, but its connectedness and support
requirements are global.  Pair--pair switches can join transition
components without changing \(z\); their three-owner effect is exactly a
two-for-two target trade.

From trace depth \(q=3\), i.e. four owners, onward, the statewise variables
\((z,p,u)\) are no longer sufficient.  One must retain the ordered
transition graph and check the corresponding longer de Bruijn windows or
the exact PBBS seam coboundary.

### Lemma 6.1 (the actual four-owner \(q=3\) port test)

Let consecutive diamonds in one chosen order be

\[
 d_i=(R_i,U_i).
\]

Assume the adjacent three-owner rows have the correct ranks, so

\[
 |R_{i-1}\cap R_i|=|R_i\cap R_{i+1}|=s-2,
\]

\[
 |U_{i-1}\cup U_i|=|U_i\cup U_{i+1}|=s+2.
\]

Put

\[
 a_i=R_i\setminus R_{i-1},\qquad
 b_i=R_i\setminus R_{i+1},
\]

\[
 c_i=U_{i-1}\setminus U_i,\qquad
 d_i^+=U_{i+1}\setminus U_i.
\]

Then the lower and upper four-owner labels are

\[
 R_{i-1}\cap R_i\cap R_{i+1}
   =R_i\setminus\{a_i,b_i\},
\tag{6.3}
\]

\[
 U_{i-1}\cup U_i\cup U_{i+1}
   =U_i\cup\{c_i,d_i^+\},
\tag{6.4}
\]

and have the correct ranks \(s-3,s+3\) if and only if

\[
 a_i\ne b_i,\qquad c_i\ne d_i^+.
\tag{6.5}
\]

#### Proof

Under the adjacent-rank hypotheses, each neighbouring lower colour removes
one element from \(R_i\), and each neighbouring upper colour adds one
element to \(U_i\).  The two removals, respectively additions, have full
size two exactly when their port labels are distinct. \(\square\)

For the switch of Theorem 4.1, every index whose triple
\((d_{i-1},d_i,d_{i+1})\) meets one of the changed diamonds must be
retested using (6.3)--(6.5).  This is a wider collar than the six-state
ledger of Theorem 5.1; no claim that only six actual \(q=3\) occurrences
change is made.

## 7. Exact proved/open boundary

The following statements are unconditional.

1. PBBS supplies the exact disconnected two-sided table
   (1.4)--(1.6).
2. Fixed \(R/U\) table moves are alternating flag circuits, while physical
   moves are their intersection with \(\ker D\).
3. A rectangle cannot move a fixed-boundary factor, and its canonical
   reciprocal repair is component-neutral.
4. The six-cell circuit (3.3)--(3.8) is a minimum-support physical circuit
   and can merge three components.
5. The local odd-graph configuration (4.1)--(4.3) gives a literal
   odd-factor realization of two such circuits.  It preserves all
   \(R\)-loads and \(U\)-columns exactly and merges three components;
   (4.6) is the additional rooted orientation condition.
6. Its entire three-owner (\(q=2\)) effect is the six-port ledger
   (5.4)--(5.9); its actual four-owner \(q=3\) collar is not computed.

What is not proved is that the PBBS factor contains a joining family of
configurations (4.3) which:

* meets enough distinct PBBS components;
* satisfies the orientation condition (4.6);
* passes all six three-owner safety and last-occurrence inequalities
  (5.6), (5.9);
* passes the four-owner lower/upper port tests (6.5) and remains
  support-complete in every longer flag row; and
* extends through the separate compiler owner-Hall system.

Thus the minimum surviving PBBS fusion lemma is now concrete:

> Find a sequence of common-retained-label odd \(C_6\) switches of
> Theorem 4.1 whose contracted component graph is connected and whose
> telescoped depth-\(q\) target ledger is nonnegative for every required
> \(q\).

The theorem in this note proves that such a sequence would be literal,
two-sided, and owner-degree exact.  It does not prove that the sequence
exists.
