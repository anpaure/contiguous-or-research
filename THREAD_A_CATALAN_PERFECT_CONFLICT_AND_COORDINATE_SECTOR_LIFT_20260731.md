# Perfect-conflict rounding and the coordinate-sector network lift

Date: 2026-07-31  
Lane: A, ordered four-transversal / bounded-rank integral lifts  
Status: unconditional rounding theorem and an explicit all-dimensional
rank-two integral catalogue.  The full ordered four-transversal theorem is
not proved.

## 0. Result and boundary

Let

\[
 \mathcal L=\binom{\Omega}{m-1},\qquad
 \mathcal X=\binom{\Omega}{m},\qquad
 \mathcal U=\binom{\Omega}{m+1},\qquad |\Omega|=2m,\qquad m\ge2,
\]

and put

\[
 K=\operatorname {Cat}_m,\qquad
 N=|\mathcal L|=|\mathcal U|=mK.
\]

An oriented Boolean-diamond atom is

\[
 q=(L;a,b),\qquad L\in\mathcal L,\quad
 a,b\in\Omega\setminus L,\quad a\ne b,                \tag{0.1}
\]

with resources

\[
 \lambda(q)=L,\quad \upsilon(q)=L+a+b,\quad
 \tau(q)=L+a,\quad \eta(q)=L+b.                       \tag{0.2}
\]

Its physical arc is \(\tau(q)\to\eta(q)\).

This note proves two positive statements.

1. A fractionally saturating atom catalogue rounds whenever its
   same-resource conflict graph is perfect, every conflict clique is
   centred at one physical resource, and all its arcs increase one common
   potential.  This properly extends the earlier bipartite-conflict
   theorem.
2. For every coordinate \(c\), the catalogue consisting of the atoms
   \((L;c,b)\) is an exact rank-two network lift.  Its four resource rows
   collapse to duplicated endpoint rows of a regular bipartite inclusion
   graph.  It therefore has an integral perfect sector matching in every
   dimension.

The second catalogue covers a fraction \((m+1)/(2m)\) of each outer
shore, not the whole shore.  At least \(m\) coordinate sectors are needed
even to make every lower and upper resource eligible.  Their union is no
longer protected by the one-sector network matrix.  Thus this theorem is a
genuine integral catalogue and a precise bounded-rank lift, but not a proof
of the central Catalan Linear Matching Theorem.

For every \(m\ge2\), the full Boolean catalogue cannot itself satisfy the
perfect-conformal hypothesis: it contains both an induced conflict
\(C_5\) and a non-centred conflict triangle.

## 1. Resource conflict and conformality

For a catalogue \(\mathcal C\) of atoms, its resource-conflict graph
\(G_{\mathcal C}\) has vertex set \(\mathcal C\).  Two atoms are adjacent
exactly when they have the same value of one of
\(\lambda,\upsilon,\tau,\eta\).  Notice that equality of a head and a tail
is not a conflict: the two middle roles are different resource classes.

Call \(\mathcal C\) **resource-conformal** when every clique of
\(G_{\mathcal C}\) is contained in one fibre of one of the four resource
maps.  Equivalently, every pairwise-conflicting family of atoms has a
single same-role resource common to all its members.

We use the following standard perfect-graph polyhedral theorem.

### Lemma 1.1 (perfect-graph stable-set theorem)

For a perfect graph \(G\),

\[
 \operatorname {STAB}(G)=
 \left\{x\ge0:\sum_{v\in Q}x_v\le1
       \text{ for every clique }Q\text{ of }G\right\}.              \tag{1.1}
\]

In particular, maximizing any integral linear objective over the right
side has an integral optimum.

This is the stable-set polyhedral form of the Perfect Graph Theorem.  It
is invoked here as the defining integral-class theorem; no claim is made
that an arbitrary Boolean atom conflict graph is perfect.

### Theorem 1.2 (perfect-conformal monotone rounding)

Let \(\mathcal C\) be a catalogue satisfying all of the following.

1. \(G_{\mathcal C}\) is perfect.
2. \(\mathcal C\) is resource-conformal.
3. There is a fractional vector \(x\ge0\) satisfying all resource rows

   \[
   \sum_{\rho(q)=R}x_q\le1
   \quad
   (\rho\in\{\lambda,\upsilon,\tau,\eta\}),             \tag{1.2}
   \]

   and having total weight

   \[
                         \sum_{q\in\mathcal C}x_q=N.       \tag{1.3}
   \]

4. There is a function \(\varphi:\mathcal X\to\mathbb R\) such that

   \[
                \varphi(\tau(q))<\varphi(\eta(q))
                \qquad(q\in\mathcal C).                   \tag{1.4}
   \]

Then \(\mathcal C\) contains an integral acyclic ordered
four-transversal.

#### Proof

By resource conformality, every clique inequality in (1.1) is dominated
by one row of (1.2).  Hence \(x\in\operatorname {STAB}(G_{\mathcal C})\).
The fractional stable set \(x\) has weight \(N\), so perfect-graph
integrality gives an integral stable set \(I\) of weight at least \(N\).

No stable set contains two atoms with the same lower resource.  Since
there are exactly \(N\) lower resources, \(|I|\le N\).  Thus
\(|I|=N\), and \(I\) uses every lower resource exactly once.  The same
argument on the \(N\) upper resources shows that it uses every upper
resource exactly once.  Stability separately makes the tail and head maps
injective.  Therefore \(I\) is an ordered four-transversal apart from the
acyclicity assertion.

Every selected physical arc strictly increases \(\varphi\), so the
directed graph has no directed cycle.  With indegree and outdegree at most
one, an undirected cycle would have one incoming and one outgoing selected
edge at each of its vertices, and hence would be a directed cycle.  Thus
the physical lift is a linear forest. \(\square\)

The total-weight hypothesis can be replaced by saturation of all lower
rows, or of all upper rows.  Conversely, total weight \(N\) plus (1.2)
already forces every lower and every upper row to be tight.

### Remark 1.3 (balanced resource matrices)

Let \(A_{\mathcal C}\) be the zero-one matrix whose rows are the four
resource fibres and whose columns are atoms.  If \(A_{\mathcal C}\) is
balanced---that is, it has no odd square submatrix with exactly two ones
in every row and column---then the Balanced Matrix Theorem makes

\[
                       \{x\ge0:A_{\mathcal C}x\le\mathbf1\}          \tag{1.5}
\]

integral.  Consequently condition 3 alone rounds to a resource packing of
size \(N\): maximize the all-ones objective, use the feasible value \(N\),
and observe from the \(N\) lower rows that no packing has value above
\(N\).  Condition 4 again makes the resulting packing a linear forest.

Equivalently, this is the no-strong-odd-resource-circuit support class,
where a strong circuit means exactly an odd square resource--atom
submatrix having two ones in every selected row and every selected column.
The perfect-conformal formulation in Theorem 1.2 is useful because it also
covers perfect resource matrices that need not be balanced.  Either form
is a bounded-rank known-integral-class theorem: every atom column has four
resource incidences.

## 2. The one-coordinate sector is exactly bipartite matching

Fix \(c\in\Omega\), put \(\Omega_c=\Omega\setminus\{c\}\), and define

\[
 \mathcal C_c=\{(L;c,b):
   L\in\tbinom{\Omega_c}{m-1},\ b\in\Omega_c\setminus L\}.            \tag{2.1}
\]

Let \(I_c\) be the bipartite inclusion graph with shores

\[
 \mathscr L_c=\binom{\Omega_c}{m-1},\qquad
 \mathscr H_c=\binom{\Omega_c}{m},                                  \tag{2.2}
\]

and edge \(LH\) when \(H=L+b\) for one \(b\notin L\).  Both shores have

\[
                         Q=\binom{2m-1}{m-1}                         \tag{2.3}
\]

vertices, and \(I_c\) is \(m\)-regular.

### Theorem 2.1 (coordinate-sector network lift)

The map

\[
                  (L;c,b)\longmapsto (L,H=L+b)                       \tag{2.4}
\]

identifies the four-resource packing polytope of \(\mathcal C_c\) with
the matching polytope of \(I_c\).  More precisely,

\[
\begin{array}{c|cccc}
q=(L;c,b)&\lambda(q)&\tau(q)&\eta(q)&\upsilon(q)\\ \hline
 &L&L+c&H& H+c.
\end{array}                                                          \tag{2.5}
\]

Thus the \(\lambda\)- and \(\tau\)-rows are two copies of the left
endpoint row of \(I_c\), while the \(\eta\)- and \(\upsilon\)-rows are
two copies of its right endpoint row.  In particular:

1. the sector resource matrix is totally unimodular after one shore is
   signed;
2. its resource-conflict graph is the line graph \(L(I_c)\), which is
   perfect and resource-conformal;
3. the constant vector \(x_q=1/m\) rounds to a sector perfect matching of
   size \(Q\);
4. every such matching is physically a matching, hence a linear forest.

#### Proof

Formula (2.5) is immediate from (0.2).  Therefore two sector atoms
conflict exactly when their corresponding inclusion edges share their
left or right endpoint.  The resource incidence matrix is obtained from
the unsigned node-edge incidence matrix of the bipartite graph \(I_c\) by
duplicating every node row.  Signing one bipartition turns that node-edge
matrix into a directed incidence matrix, so it is totally unimodular;
duplicated rows preserve total unimodularity.

Equivalently, the conflict graph is \(L(I_c)\).  A line graph of a
bipartite graph is perfect.  Moreover, pairwise-intersecting edges of a
bipartite graph have a common endpoint: otherwise three of them would
form a triangle in the base graph.  Hence every clique of \(L(I_c)\) is
one endpoint star, proving resource conformality.

Each left vertex of \(I_c\) has the \(m\) extensions \(L+b\), and each
right vertex has its \(m\) rank-\((m-1)\) facets.  Thus \(x_q=1/m\)
saturates every endpoint row.  Total unimodularity, or the regular
bipartite matching theorem, supplies an integral perfect matching.

Finally, every selected tail \(L+c\) contains \(c\), while every selected
head \(H=L+b\) avoids \(c\).  Tails are distinct because the left
endpoints are distinct, and heads are distinct because the right endpoints
are distinct.  No middle vertex can occur in both roles.  The physical
arcs are therefore pairwise vertex-disjoint. \(\square\)

For \(m\ge3\), the conflict graph \(L(I_c)\) contains a clique \(K_m\)
at every endpoint star.  It is therefore nonbipartite.  Theorem 2.1 is a
strict extension of bipartite-conflict rounding, not a disguised use of
that earlier theorem.

The sector covers exactly the lower sets avoiding \(c\) and the upper
sets containing \(c\).  Its fraction of either full outer shore is

\[
 {Q\over N}={\binom{2m-1}{m-1}\over\binom{2m}{m-1}}
             ={m+1\over2m}.                                           \tag{2.6}
\]

## 3. Exact sector decomposition of the symmetric fractional point

Let \(f^c\) put weight \(1/m\) on every atom of \(\mathcal C_c\), and
zero elsewhere.  Every oriented atom \((L;a,b)\) belongs to the unique
sector \(\mathcal C_a\).  Hence

\[
                  z^*=\frac1{m+1}\sum_{c\in\Omega}f^c               \tag{3.1}
\]

puts weight

\[
                  z_q^*=\frac1{m(m+1)}
                         =\frac1{2\binom{m+1}{2}}                    \tag{3.2}
\]

on every oriented atom.  This is exactly the fully symmetric fractional
point of the ordered four-transversal relaxation.

Equation (3.1) is a conic sector decomposition, not a convex combination:
the coefficients sum to \(2m/(m+1)\), because one sector matching has
only \(Q<N\) atoms.  It pinpoints the missing operation.  Every sector is
integral by itself, but the global point fractionally assigns each lower
set among its \(m+1\) missing-coordinate sectors and each upper set among
its \(m+1\) contained-coordinate sectors.  An integral solution must make
these assignments coherently while also preventing cross-sector tail and
head collisions.

### Proposition 3.1 (sharp number of coordinate sectors for outer support)

For \(S\subseteq\Omega\), let

\[
                         \mathcal C_S=\bigcup_{c\in S}\mathcal C_c.
\]

Every lower and every upper resource occurs in \(\mathcal C_S\) if and
only if

\[
                              |S|\ge m.                              \tag{3.3}
\]

#### Proof

A lower set \(L\) occurs precisely when \(S\setminus L\ne\varnothing\).
If \(|S|\le m-1\), extend \(S\) to an \((m-1)\)-set \(L\), which then
has no sector.  If \(|S|\ge m\), no \((m-1)\)-set contains all of \(S\),
so every lower set occurs.

An upper set \(U\) occurs precisely when \(U\cap S\ne\varnothing\).  If
\(|S|\le m-1\), then \(|\Omega\setminus S|\ge m+1\), so some upper set
avoids \(S\).  If \(|S|\ge m\), the complement of \(S\) has size at most
\(m\), so no \((m+1)\)-set avoids it. \(\square\)

Thus a bounded number of coordinate-sector network lifts cannot cover the
full problem uniformly in \(m\).  The threshold \(m\) concerns only outer
eligibility; it does not assert that a union of \(m\) sectors has a
resource-perfect packing.

## 4. Why the full Boolean catalogue is outside the class

Two independent physical fixtures exclude a direct application of
Theorem 1.2.

### Proposition 4.1 (induced odd hole in every dimension)

For \(m\ge2\), fix \(R\subseteq\Omega\) of size \(m-2\), and choose four further points
\(0,1,2,3\).  The five atoms

\[
\begin{array}{c|cccc}
 &\lambda&\upsilon&\tau&\eta\\ \hline
q_0&R0&R012&R01&R02\\
q_1&R0&R013&R01&R03\\
q_2&R3&R013&R03&R13\\
q_3&R1&R123&R12&R13\\
q_4&R1&R012&R12&R01
\end{array}                                                           \tag{4.1}
\]

induce \(C_5\) in the resource-conflict graph.

#### Proof

Consecutive pairs share, cyclically, the displayed resources

\[
 \lambda=R0,\quad \upsilon=R013,\quad \eta=R13,\quad
 \lambda=R1,\quad \upsilon=R012.
\]

Inspection of (4.1) shows that no nonconsecutive pair has any equal
same-role resource.  Thus the induced graph is \(C_5\), which is not
perfect. \(\square\)

### Corollary 4.2 (three coordinate sectors already recreate the odd hole)

If \(S\subseteq\Omega\) has \(|S|\ge3\), then
\(G_{\mathcal C_S}\) contains an induced \(C_5\), and hence is not
perfect.  Consequently, for \(m\ge3\), every coordinate-sector union
which touches every lower and upper resource lies outside Theorem 1.2.

#### Proof

Choose distinct \(0,1,2\in S\), then choose a fourth point \(3\) and a
disjoint \((m-2)\)-set \(R\).  In (4.1), the tail-added coordinates of
\(q_0,\ldots,q_4\) are respectively

\[
                              1,1,0,2,2.
\]

Thus all five atoms lie in \(\mathcal C_S\), and Proposition 4.1 gives
the induced \(C_5\).  Proposition 3.1 says that outer support requires
\(|S|\ge m\); for \(m\ge3\), this implies \(|S|\ge3\). \(\square\)

### Proposition 4.3 (non-conformal triangle in every dimension)

For \(m\ge2\), fix \(L\in\mathcal L\), \(\ell\in L\), and distinct
\(p,q,r\in\Omega\setminus L\).  Put

\[
 \alpha=(L;p,r),\qquad \beta=(L;q,p),\qquad
 \gamma=((L-\ell)+p;\ell,q).                                        \tag{4.2}
\]

Then \(\{\alpha,\beta,\gamma\}\) is a clique, but no resource row
contains all three atoms.

#### Proof

The three pair conflicts are

\[
 \lambda(\alpha)=\lambda(\beta)=L,
\]

\[
 \upsilon(\beta)=\upsilon(\gamma)=L+p+q,
\]

and

\[
 \tau(\gamma)=\tau(\alpha)=L+p.
\]

The remaining same-role resources are distinct, so no one row contains
the three atoms. \(\square\)

The induced \(C_5\) says that any perfect-conflict candidate subcatalogue
must delete at least one atom from every coordinate conjugate of (4.1).
The triangle says that any resource-conformal candidate must delete at
least one atom from every conjugate of (4.2).  These are exact local
hitting conditions.  They are not a nonexistence theorem: an unknown
fractionally saturating subcatalogue could avoid both or could belong to a
different integral class.

The strong odd-resource-circuit inequalities cut the half-vector on
(4.1) and the triangle clique inequality cuts the half-vector on (4.2).
Adding those inequalities to the full relaxation does not by itself turn
the full conflict graph into the perfect-conformal catalogue required by
Theorem 1.2.  Reciprocal-completion suspensions impose a further,
completion-level incompatibility not represented by same-resource
conflict edges.  Thus the theorem here is a positive support-class
rounding result, not an exact description of the full convex hull.

## 5. Direct-ground-set lift audit

The preceding obstructions can be sharpened into a classification of the
most immediate integral-lift proposals.  All statements in this section
refer to the natural oriented-atom ground set and its natural resource
rows.  They do not exclude a nonlocal extended formulation with auxiliary
gadgets.

### Proposition 5.1 (no natural network or TU matrix)

The full resource incidence matrix has a determinant-three minor in every
dimension \(m\ge2\).  Consequently it is neither totally unimodular nor a
network matrix.

#### Proof

On four active coordinates \(1,2,3,4\), and with a common disjoint core
\(R\) of size \(m-2\), take the five columns obtained by adjoining \(R\)
to all sets in

\[
\begin{array}{c|cccc}
 &L&U&T&H\\ \hline
e_1&1&134&14&13\\
e_2&3&234&34&23\\
e_3&4&234&24&34\\
e_4&4&124&14&24\\
e_5&4&134&34&14.
\end{array}                                                          \tag{5.1}
\]

On the five resource rows

\[
 T_{R34},\quad U_{R234},\quad U_{R134},\quad
 L_{R4},\quad T_{R14},
\]

the incidence minor is

\[
\begin{pmatrix}
0&1&0&0&1\\
0&1&1&0&0\\
1&0&0&0&1\\
0&0&1&1&1\\
1&0&0&1&0
\end{pmatrix},
\qquad \det=-3.                                                       \tag{5.2}
\]

Every network matrix is totally unimodular, while (5.2) is not.
\(\square\)

### Proposition 5.2 (no natural two-matroid or gammoid-intersection lift)

For \(m\ge2\), the hereditary resource-and-graphic feasibility system on
the natural atoms is not the intersection of two matroids.  In particular
it is not the intersection of two gammoids on those atoms.

#### Proof

On the five atoms in (4.1), every nonconflicting pair has two distinct
physical edges and is graphic-independent.  Hence the restricted
hereditary system is exactly the stable-set system of \(C_5\).

Suppose this system were \(\mathcal I(M_1)\cap\mathcal I(M_2)\).
Every singleton is feasible, so every element is a nonloop in each
matroid.  Every adjacent pair of the \(C_5\) is therefore a two-element
circuit, hence a
parallel pair, in at least one \(M_i\).  Two incident cycle edges cannot
be assigned to the same \(M_i\), because transitivity of parallelism would
make the intervening nonadjacent pair dependent.  The five edges of
\(C_5\) would therefore have a proper two-edge-colouring, impossible.
Gammoids are matroids, so the specialization follows. \(\square\)

### Proposition 5.3 (no bounded-treewidth conflict formulation)

The full natural resource-conflict graph has treewidth at least

\[
                            m(m+1)-1.                                \tag{5.3}
\]

#### Proof

Fix \(L\in\mathcal L\).  There are
\((m+1)m\) ordered pairs \(a\ne b\) in \(\Omega\setminus L\), and all
atoms \((L;a,b)\) share the lower resource \(L\).  They induce a clique of
order \(m(m+1)\).  Treewidth is at least clique number minus one.
\(\square\)

Thus the coordinate-sector theorem is a genuine structural reduction:
inside one sector the rank-four resource column collapses to a rank-two
bipartite incidence column.  No analogous collapse exists for the full
natural matrix, conflict graph, or two-matroid system.  Propositions
5.1--5.3 do not exclude a bounded-state recursive gadget whose projection
is nonlocal in the atom coordinates.  In particular, determinant three
alone is not asserted to exclude every binet extended formulation.

## 6. Exact remaining gate for this lift

For a Chung--Feller factor and its coordinate conjugates, the bounded-rank
route is now an exact test rather than a heuristic:

1. choose an occurrence-labelled atom subcatalogue carrying a fractional
   resource packing of total \(N\);
2. verify that every conflict clique is resource-centred;
3. verify perfection of its resource-conflict graph (balancedness of its
   resource matrix is a stronger sufficient certificate);
4. orient the physical atoms through one common strict potential.

If all four hold, Theorem 1.2 supplies the desired ordered
four-transversal.  The one-coordinate sectors prove that the local
network-matrix pieces exist in every dimension and already cover more than
half of each outer shore.  Proposition 3.1 and Section 4 identify the two
nonlocal obstacles to gluing them: at least \(m\) sector labels are needed,
and cross-sector unions can recreate both induced odd holes and non-centred
cliques.

No claim is made here that the canonical Chung--Feller conjugate catalogue
passes or fails those global tests.
