# PBBS diamond-table C6 switches and H-safe Johnson linearization

Date: 2026-07-28

Method: no web search, new broad finite search, or solver run was performed
in this lane.  Sections 1--10.7 are hand mathematics.  Sections 10.8--10.12
use separately audited exact finite inputs.  The new finite work in Sections
10.10--10.12 consists only of the 21 explicitly parametrized companion-edge
lookups, the four hand-sized two-cell flag-margin pairings per block, the
literal four-edit overlay, and a direct audit of the already specified
20-state certificate.

Status: The diamond switching lattice, the rectangle obstruction, the clean
component-merging C6, its exact ambient degree, the separated-seam
linearization system through protected depth \(H\), and the literal
central-band compiler interface are proved.  Section 10 additionally proves
the exact rank-eight Shadow--Braid/common-word criterion and a sharp scoped
finite obstruction: one transported clean C6 cannot realize the audited
24-unit-pin Hall-29 repair interface.  Sections 10.9--10.12 isolate the
first surviving two-state export blocks, rule out all three literal frozen
clean-C6 embeddings, and prove that the known exact 20-state \(B_1\) closure
is depth-three resident but has a nonzero adjacent-shadow boundary.  A
positive-density bank of
PBBS-realized, protected-depth-safe C6 circuits is not proved.  No
coefficient-one theorem is claimed.

## 0. Verdict

Let

\[
 m\ge2,\qquad n=2m+1,\qquad
 {\cal R}=\binom{[n]}{m-1},\qquad
 {\cal M}=\binom{[n]}m,\qquad
 {\cal U}=\binom{[n]}{m+1},
\qquad W=|{\cal M}|.
\]

The step-two PBBS factor is an exact disconnected table of Boolean
diamonds.  Every selected cell is a flag

\[
                         R\subset U,\qquad |U\setminus R|=2,
\]

and represents the unique Johnson edge through the two intermediate
members of \({\cal M}\).  The PBBS table has:

1. one selected cell in every \(U\)-column;
2. middle degree two at every \(A\in{\cal M}\);
3. positive load in every \(R\)-row; and
4. complete chronological lower and complementary upper support at every
   depth.

The exact conclusions of this note are these.

1. Within the upper-perfect projected-table class, a signed table change is
   a physical projected-factor trade precisely when it preserves every
   \(U\)-column and has zero middle-owner boundary.
   If it must also preserve the complete depth-one lower multiset, its
   \(R\)-row sums must vanish.  Row/column-neutral changes decompose into
   alternating cycles in the \(R\)-\(U\) flag graph, but the middle boundary
   is an additional, independent equation.

2. Every nontrivial alternating rectangle has a nonzero four-owner
   boundary.  Hence no isolated rectangle is an exact factor trade.

3. There is a clean alternating C6 which is exact.  It changes three
   diamonds, preserves every affected \(R\)-row and \(U\)-column, preserves
   every middle degree, and merges three distinct factor components into
   one.  Thus arity three is the minimum exact row/column-preserving merger.

4. A fixed rooted flag cell belongs to exactly

   \[
                            2m(m-1)
   \]

   clean ambient C6 shores.  This is the promised \(m^2\) local entropy.
   For PBBS, however, a candidate is present only if two further correlated
   columns have the prescribed PBBS rows.  No positive lower bound for this
   realized degree follows from the ambient count.

5. After retained fragments are fixed, exact rebundling is a permutation
   problem.  Column, row, flag support through protected depth \(H\),
   H-safe collar, and component conditions are explicit equations or
   inequalities on one permutation matrix, provided retained fragments
   have at least \(H+1\) vertices for independent seamwise safety.  This
   gives a necessary-and-sufficient separated-collar formulation, not an
   existence theorem.  At depths beyond \(H\), an exact itinerary formula
   remains available, but it is polynomial in several seam choices rather
   than linear.

6. Every old short residence interval wholly inside a retained fragment
   survives.  Consequently any segment-retaining H-safe rebundling on the
   chosen owner shore which changes \(J\) old transitions satisfies

   \[
                     J\ge \tau_H(F)\ge \nu_H(F).
   \]

   On the physical complement shore this is the authoritative PBBS
   \(\nu_H(P_m)\) gate.  On the rank-\(m\) table shore it is a different
   positive-run packing.  Complementation exchanges positive and zero runs,
   so the two are not identified without an additional theorem.

7. Full wreaths are unnecessary at the literal interface.  If the resulting
   projected factor is opened into \(p\) owner-disjoint compiler-H-safe
   Johnson paths and has actual depth-\(q\) holes \(h_q^\pm\), endpoint-capped
   erosion constructs a literal central-band word of length

   \[
                  W+Hp+\sum_{q=1}^{H}(h_q^-+h_q^+).
   \]

   Therefore a direct projected C6 need not lift back to an odd-graph
   factor.  If an odd-factor lift is demanded, the companion step-two
   parity shore and its collars must be switched and certified separately.

8. None of the three named target-envelope-survival blocks embeds in one
   clean C6 of the frozen Hall-29 chronology: all seven completions of each
   possible boundary seam lack a required companion old edge.  The nearby
   \(B_2+B_3\) overlay is not even a legal controller path.  The exact
   20-state nonseparated closure of \(B_1\) is a literal, depth-three-
   resident deck circulation, but it omits fourteen immediate lower colours
   and three immediate upper colours.  Clean C6s have zero adjacent-shadow
   boundary and therefore cannot repair it; a genuinely non-clean
   compensator is necessary.

The exact remaining theorem is a PBBS-realized safe-circuit packing or an
equivalent separated-seam permutation satisfying the protected-depth
support inequalities (and, if literal preservation of the entire PBBS
tower is demanded, the multi-seam polynomial inequalities of Theorem 5.3).
Pure component Hamiltonization is neither needed nor enough.

## 1. The three boundary maps of a diamond table

Let

\[
 {\cal D}=\{(R,U)\in{\cal R}\times{\cal U}:R\subset U\}.
\]

For \(d=(R,U)\in{\cal D}\), write

\[
                         U\setminus R=\{x,y\}.
\]

The cell \(d\) lifts to the Johnson edge

\[
                         e_d=\{R+x,R+y\}.
\tag{1.1}
\]

Thus cells of \({\cal D}\) and undirected edges of \(J(n,m)\) are in
bijection.

For an integral table \(z=(z_{R,U})_{(R,U)\in{\cal D}}\), define

\[
 (\partial_Rz)(R)=\sum_{U\supset R}z_{R,U},
\tag{1.2}
\]

\[
 (\partial_Uz)(U)=\sum_{R\subset U}z_{R,U},
\tag{1.3}
\]

and

\[
 (\partial_Mz)(A)
   =\sum_{\substack{R\subset A\subset U\\(R,U)\in{\cal D}}}z_{R,U}
       \qquad(A\in{\cal M}).
\tag{1.4}
\]

The last map is the degree vector of the lifted Johnson multigraph.

Let \(x^{\rm PBBS}\) be the step-two PBBS table.  The upper-colour identity
for the edge \(A_iA_{i+2}\) is

\[
                         A_i\cup A_{i+2}=\overline{A_{i+1}}.
\tag{1.5}
\]

Every middle set occurs once as the centre \(A_{i+1}\), so complementation
and (1.5) give

\[
 \partial_Ux^{\rm PBBS}={\bf1}_{\cal U}.
\tag{1.6}
\]

The step-two graph is a two-factor, hence

\[
 \partial_Mx^{\rm PBBS}=2{\bf1}_{\cal M}.
\tag{1.7}
\]

Finally, if \(c_R\) is the PBBS first-shadow load, complete depth-one support
gives

\[
 \partial_Rx^{\rm PBBS}=c,\qquad c_R\ge1.
\tag{1.8}
\]

The deeper PBBS flags are chronological data and are not determined by
(1.6)--(1.8).

### Theorem 1.1 (exact projected diamond-switch criterion)

Let \(x\) be a \(0\)-\(1\) diamond table whose lift is a spanning
two-factor of \(J(n,m)\), and let \(\delta\) be an integral signed table.
Assume \(x+\delta\ge0\).  Then:

1. \(x+\delta\) has the same number of selected cells in every
   \(U\)-column if and only if

   \[
                             \partial_U\delta=0;
   \tag{1.9}
   \]

2. its lifted Johnson graph has the same middle degree at every
   \(A\in{\cal M}\) if and only if

   \[
                             \partial_M\delta=0;
   \tag{1.10}
   \]

3. it has the same depth-one lower multiplicity in every \(R\)-row if and
   only if

   \[
                             \partial_R\delta=0.
   \tag{1.11}
   \]

In particular, under (1.9)--(1.10), \(x+\delta\) is another upper-perfect
spanning Johnson two-factor.  It retains lower depth-one support if and
only if

\[
                 (\partial_Rx)(R)+(\partial_R\delta)(R)\ge1
                 \qquad(R\in{\cal R}).
\tag{1.12}
\]

If every old \(U\)-column sum is one, nonnegativity and (1.9) imply
automatically that \(x+\delta\) is \(0\)-\(1\).

#### Proof

Equations (1.9), (1.10), and (1.11) are exactly the differences of
(1.3), (1.4), and (1.2), respectively.  Under (1.9), each new column is a
nonnegative integral vector of sum one and therefore contains exactly one
entry equal to one.  Under (1.10), every middle vertex retains degree two.
Thus the lift is a spanning two-factor.  Inequality (1.12) is precisely
positive new row load.  \(\square\)

### Proposition 1.2 (flag-cycle lattice and the extra owner equation)

Every integral \(\delta\) with

\[
                         \partial_R\delta=\partial_U\delta=0
\tag{1.13}
\]

is an integral sum of signed alternating even cycles in the bipartite flag
graph with shores \({\cal R}\) and \({\cal U}\) and edge set \({\cal D}\).
It is a physical middle-factor trade if and only if the sum of the middle
signatures of those cycles also satisfies

\[
                         \partial_M\delta=0.
\tag{1.14}
\]

#### Proof

Replace an entry of magnitude \(a\) by \(a\) parallel signed copies of its
flag edge.  At each \(R\)- and \(U\)-vertex, (1.13) says that the positive
and negative degrees agree.  Starting with any unused positive edge,
alternate negative and positive edges.  Balance prevents the trail from
stopping, and finiteness closes an alternating even circuit.  Subtract its
minimum multiplicity and iterate.  This proves the cycle decomposition.
The final assertion is Theorem 1.1(2).  \(\square\)

Thus an alternating flag cycle is only a row/column trade.  Middle
neutrality is not automatic.

## 2. The sharp rectangle obstruction

### Lemma 2.1 (normal form of a flag rectangle)

Every nontrivial \(2\)-by-\(2\) rectangle in the flag graph has the form

\[
 R_a=K+a,\qquad R_b=K+b,
\tag{2.1}
\]

\[
 U_c=K+a+b+c,\qquad U_d=K+a+b+d,
\tag{2.2}
\]

where \(|K|=m-2\) and \(a,b,c,d\) are distinct.

#### Proof

The two distinct rows \(R_a,R_b\) lie in both distinct columns \(U_c,U_d\).
Their union therefore has size at most \(m\), because two distinct
\((m+1)\)-sets intersect in at most \(m\) points.  Distinct
\((m-1)\)-sets have union of size at least \(m\), so equality holds.
Put \(K=R_a\cap R_b\), and write the two row differences as \(a,b\).
Each column is the common \(m\)-set \(K+a+b\) plus one new point.  The two
new points are distinct and outside the common set.  \(\square\)

### Theorem 2.2 (no nontrivial rectangle is factor-exact)

Switching the two rectangle diagonals

\[
 (R_a,U_c),(R_b,U_d)
 \quad\longleftrightarrow\quad
 (R_a,U_d),(R_b,U_c)
\tag{2.3}
\]

has middle-owner boundary

\[
 [K+a+d]+[K+b+c]-[K+a+c]-[K+b+d].
\tag{2.4}
\]

The four displayed middle sets are distinct.  Hence the boundary (2.4) is
nonzero and no isolated nontrivial flag rectangle preserves a two-factor.

#### Proof

The cell \((R_a,U_c)\) lifts to the edge between

\[
                         K+a+b\quad\hbox{and}\quad K+a+c.
\]

The other three cells give the same common middle owner \(K+a+b\) and,
respectively, the secondary owners

\[
 K+b+d,\qquad K+a+d,\qquad K+b+c.
\]

The common owner occurs twice on each shore and cancels.  The remaining
signed degree vector is (2.4).  Distinctness follows from distinctness of
\(a,b,c,d\).  \(\square\)

This is the precise rectangle cut obstruction: arity two can transport
row/column mass, but it leaves four uncompensated middle-owner ports.  A
compound of rectangles is physical only when all such signatures cancel.

## 3. The minimum exact clean C6

Fix \(K\in\binom{[n]}{m-2}\) and distinct

\[
                         a_0,a_1,a_2,c\notin K.
\]

Read subscripts modulo three and put

\[
 R_i=K+a_i,
\qquad
 U_i=K+a_i+a_{i+1}+c,
\tag{3.1}
\]

\[
 P_i=K+a_i+a_{i+1},
\qquad
 Q_i=K+a_i+c.
\tag{3.2}
\]

The six flags

\[
 (R_i,U_i),\qquad (R_{i+1},U_i)
 \qquad(i\in{\mathbb Z}_3)
\tag{3.3}
\]

form the alternating flag cycle

\[
 R_0-U_0-R_1-U_1-R_2-U_2-R_0.
\tag{3.4}
\]

### Theorem 3.1 (clean C6 factor trade)

The old shore

\[
                         {\cal E}^-=\{(R_i,U_i):i\in{\mathbb Z}_3\}
\tag{3.5}
\]

lifts to the three Johnson edges

\[
                         P_iQ_i.
\tag{3.6}
\]

The new shore

\[
                         {\cal E}^+=\{(R_{i+1},U_i):i\in{\mathbb Z}_3\}
\tag{3.7}
\]

lifts to

\[
                         P_iQ_{i+1}.
\tag{3.8}
\]

Consequently the switch \({\cal E}^-\leftrightarrow{\cal E}^+\):

1. preserves each \(U_i\)-column pointwise;
2. preserves the multiset of the three \(R_i\)-rows;
3. preserves every middle-owner degree; and
4. is an exact projected Johnson-factor trade whenever the old shore is
   present.

If the three old edges \(P_iQ_i\) lie in three distinct factor cycles, the
switch merges those cycles into one.

#### Proof

For the old cell,

\[
 U_i\setminus R_i=\{a_{i+1},c\},
\]

so (1.1) gives endpoints \(P_i,Q_i\).  For the new cell,

\[
 U_i\setminus R_{i+1}=\{a_i,c\},
\]

so its endpoints are \(P_i,Q_{i+1}\).  The column labels \(U_i\) do not
move, while the row labels undergo the cyclic permutation
\(R_i\mapsto R_{i+1}\).  The six middle sets \(P_i,Q_i\) are distinct, and
each occurs once on each shore.  Theorem 1.1 proves exactness.

For the topology statement, orient the three old edges as

\[
                         P_i\longrightarrow Q_i.
\]

Deleting them opens the three old cycles into directed paths from \(Q_i\)
to \(P_i\).  Install the new arcs

\[
                         P_i\longrightarrow Q_{i+1}.
\]

The paths are concatenated cyclically into one directed cycle.  \(\square\)

### Corollary 3.2 (minimum arity and parity)

Among nontrivial row/column-preserving flag-cycle moves, arity three is
minimum for an exact factor switch.  Clean C6 switches change the number of
factor components by an even integer.  In particular, C6-only switching
preserves component-count parity.

#### Proof

The only smaller bipartite flag cycle is a rectangle, excluded by Theorem
2.2.  A clean C6 replaces one perfect matching on six touched middle
vertices by the other matching on their alternating six-cycle.  Relative
to the old successor permutation this is a 3-cycle, which is even.
Equivalently, direct cut-and-paste changes the number of cycles by
\(-2,0\), or \(2\).  \(\square\)

The parity obstruction concerns this connector library only.  It is not an
obstruction to coefficient one, since opening one or two remaining cycles
is asymptotically cheap.

### Corollary 3.3 (exact last-witness ledger of one three-cycle merger)

Assume the three old C6 edges lie in distinct factor cycles, each of length
greater than \(q\).  For a lower or upper target \(S\), let
\(o_{q,S}^{\pm}\) count old depth-\(q\) windows crossing one of the three
removed edges, and let \(n_{q,S}^{\pm}\) count new depth-\(q\) windows
crossing one of the three inserted edges.  Then

\[
 \boxed{
 \mu_{q,S}^{\pm,\rm new}
 =
 \mu_{q,S}^{\pm,\rm old}
 -o_{q,S}^{\pm}+n_{q,S}^{\pm}.}
\tag{3.9}
\]

Moreover,

\[
 \sum_So_{q,S}^{\pm}=3q,\qquad
 \sum_Sn_{q,S}^{\pm}=3q.
\tag{3.10}
\]

Hence the complete support at depth \(q\) survives if and only if

\[
 \mu_{q,S}^{\pm,\rm old}
 -o_{q,S}^{\pm}+n_{q,S}^{\pm}\ge1
\tag{3.11}
\]

for every required target.  In particular, a clean C6 preserves the entire
depth-one multiset, but it can erase a last witness at any deeper depth
unless (3.11) is checked.

#### Proof

Every unchanged window lies wholly in one retained segment and contributes
the same target before and after the switch.  A \(q\)-edge cyclic window on
a cycle longer than \(q\) contains a fixed transition edge in exactly
\(q\) start phases.  The three old edges lie on distinct cycles, so these
old window families are disjoint.  After the merger, the three inserted
edges are separated by the retained old cycles, each longer than \(q\);
their crossing-window families are also disjoint.  This proves (3.9) and
(3.10), and (3.11) is exactly positive new load.  \(\square\)

Every PBBS projected cycle has length at least \(2m+1\).  Thus (3.9)--(3.11)
apply simultaneously at every canonical PBBS depth \(q\le m\) for a
three-distinct-component clean C6.

## 4. Exact ambient C6 degree and the PBBS correlation gate

### Theorem 4.1 (rooted ambient degree)

Fix a rooted old flag cell \((R,U)\in{\cal D}\).  The number of clean C6
shores for which

\[
                         (R_0,U_0)=(R,U)
\]

is exactly

\[
                            \boxed{2m(m-1)}.
\tag{4.1}
\]

This is a rooted and oriented count.

#### Proof

Choose:

1. \(a_0\in R\), in \(m-1\) ways;
2. an ordering

   \[
                        U\setminus R=(a_1,c),
   \]

   in two ways;
3. \(a_2\in[n]\setminus U\), in \(m\) ways.

Then \(K=R-a_0\), and (3.1) determines the clean C6 uniquely.  Conversely,
the rooted clean C6 recovers \(a_0\), the ordered pair \(a_1,c\), and
\(a_2\).  Multiplication gives (4.1).  \(\square\)

This exact \(2m(m-1)\) count is the local \(m^2\) entropy which rectangles
fail to turn into physical moves.

Define the ambient clean-shore hypergraph \({\cal H}_{\rm cl}\) to have
vertex set \({\cal D}\), with one 3-edge for every clean old shore
\(\{(R_i,U_i):i\in{\mathbb Z}_3\}\).  The opposite shore of the same C6 is
a second 3-edge.

### Corollary 4.1a (exact ambient degree and pair codegree)

\({\cal H}_{\rm cl}\) is 3-uniform and regular of degree

\[
                         D_{\rm cl}=2m(m-1).
\tag{4.1a}
\]

Any two distinct flag cells lie together in at most one clean shore.
Therefore

\[
                         \Delta_2({\cal H}_{\rm cl})\le1,
\qquad
 \frac{\Delta_2({\cal H}_{\rm cl})}{D_{\rm cl}}
 \le\frac1{2m(m-1)}.
\tag{4.1b}
\]

#### Proof

The degree assertion is Theorem 4.1: once the containing cell is fixed,
its role as the rooted cell recovers the enumeration uniquely.

Suppose two cells \((R,U)\) and \((R',U')\) lie in one clean shore.  Their
rows are distinct and

\[
                         K=R\cap R',\qquad |K|=m-2.
\]

Write \(R=K+a\), \(R'=K+b\).  Exactly one of the two displayed columns is
the clean column containing both rows, hence it is \(K+a+b+c\) and
determines \(c\).  The other column then has the form \(K+b+d+c\) or
\(K+a+d+c\) and determines the third row label \(d\) and the cyclic
orientation.  Thus the whole shore is unique.  If the two rows coincide,
or the two columns coincide, they cannot be distinct cells of one shore.
\(\square\)

Hence the favorable \(m^{-2}\) normalized codegree is an exact ambient
fact.  It does not pass automatically to PBBS: the induced hypergraph on
the selected PBBS cells can have much smaller and nonuniform degrees.

Because PBBS is upper-perfect, define its row map

\[
 \rho:{\cal U}\longrightarrow{\cal R},\qquad
 \rho(U)\subset U,
\tag{4.2}
\]

by declaring \((\rho(U),U)\) to be the unique selected PBBS cell in column
\(U\).

### Theorem 4.2 (exact PBBS realization test)

A clean candidate \((K,a_0,a_1,a_2,c)\) is present on the old PBBS shore if
and only if

\[
                         \rho(U_i)=R_i
                         \qquad(i=0,1,2).
\tag{4.3}
\]

After the switch, its three affected columns have

\[
                         \rho'(U_i)=R_{i+1},
\tag{4.4}
\]

and every other column is unchanged.  At the undirected table level it is
a three-component merger if and only if the old edges lie in three distinct
current components: orient those components independently as in Theorem
3.1.  If a directed chronology has already been frozen, its three cut arcs
must additionally have one coherent orientation or all three must be
reversed.

#### Proof

Equation (4.3) says exactly that each of the three old cells (3.5) is
selected by PBBS.  The new shore is (3.7), giving (4.4).  The topology
criterion is Theorem 3.1.  \(\square\)

Thus (4.1) is an ambient degree, not a PBBS-realized degree.  Starting from
one PBBS cell, two companion row-map equalities in (4.3) remain.  Neither
upper perfection, lower support, nor the all-depth PBBS theorem implies a
positive number of such coincidences for each root.  A nibble based on
clean C6 packets therefore needs a new correlation theorem for \(\rho\).

The exact static packet hypergraph is

\[
 {\cal H}_{\rm PBBS}
 =
 {\cal H}_{\rm cl}
 \left[
   \{(\rho(U),U):U\in{\cal U}\}
 \right].
\tag{4.5}
\]

It has \(W\) vertices, is 3-uniform, and has pair codegree at most one.
For a selected root cell \((R_0,U_0)\), its degree is exactly the number of
the \(2m(m-1)\) choices in Theorem 4.1 for which the two companion
equalities

\[
                         \rho(U_1)=R_1,\qquad
                         \rho(U_2)=R_2
\tag{4.6}
\]

hold.  A matching in \({\cal H}_{\rm PBBS}\) is a family of column-disjoint,
simultaneously applicable depth-one-exact C6 trades.  H-safety and
protected-depth support decorate this hypergraph by further collar and load
conditions; they are not consequences of (4.5).

### Remark 4.3 (projected versus odd-factor switches)

Theorem 3.1 is an exact direct switch of the projected step-two Johnson
factor.  If one insists that it arise from an odd-graph edge switch, the odd
switch also changes three seams on the companion step-two parity shore.
That companion table, its flags, and its H-collars must be certified
separately.  A one-shore clean C6 does not by itself prove an odd-factor
lift.

For a literal contiguous-OR construction no such lift is logically
required: the projected Johnson paths can be literalized directly by
Theorem 8.1 below.

## 5. Exact protected-depth ledger under fragment rethreading

The table identities control only depth one.  We now state the complete
chronological condition.

Let \(F\) be an oriented spanning Johnson two-factor.  Delete \(s\) directed
arcs, with at least one deleted arc on every component, and index the
resulting retained pieces as directed paths

\[
                         {\cal P}_i=(h_i,\ldots,t_i).
\tag{5.1}
\]

There is a unique old permutation \(\pi_0\in{\mathfrak S}_s\) for which the
deleted arcs are

\[
                         t_i\longrightarrow h_{\pi_0(i)}.
\tag{5.2}
\]

This formulation allows several cuts on one old factor component; the old
components are the cycles of \(\pi_0\).  Assume each retained path has at
least \(H\) vertices.  For every legal
Johnson adjacency \(t_i\sim h_j\), introduce \(p_{ij}\in\{0,1\}\).  Impose

\[
 \sum_jp_{ij}=1,\qquad \sum_ip_{ij}=1.
\tag{5.3}
\]

Thus \(p\) is a permutation matrix and installs the new seams
\(t_i\to h_j\).

Put

\[
 R_{ij}=t_i\cap h_j,\qquad U_{ij}=t_i\cup h_j.
\tag{5.4}
\]

Let \(c_R^{\rm cut}\) and \(c_U^{\rm cut}\) be the multiplicities of the
lower and upper colours of the deleted arcs
\(t_i h_{\pi_0(i)}\).

### Theorem 5.1 (exact separated-seam diamond and flag system)

Under the preceding hypotheses:

1. every permutation satisfying (5.3) preserves every middle degree;
2. it restores exactly the deleted depth-one lower and upper multisets if
   and only if

   \[
    \sum_{\substack{i,j\\R_{ij}=R}}p_{ij}=c_R^{\rm cut}
       \qquad(R\in{\cal R}),
   \tag{5.5}
   \]

   \[
    \sum_{\substack{i,j\\U_{ij}=U}}p_{ij}=c_U^{\rm cut}
       \qquad(U\in{\cal U}).
   \tag{5.6}
   \]

For \(1\le q\le H\) and \(1\le a\le q\), let

\[
 L_{i,a}^{\cap}
   =\bigcap\{\hbox{last \(a\) vertices of }{\cal P}_i\},
\qquad
 R_{j,q+1-a}^{\cap}
   =\bigcap\{\hbox{first \(q+1-a\) vertices of }{\cal P}_j\},
\tag{5.7}
\]

and define \(L_{i,a}^{\cup}\), \(R_{j,q+1-a}^{\cup}\) by unions.  Let
\(\mu_{q,S}^{-,\rm int}\) and \(\mu_{q,T}^{+,\rm int}\) count the depth-\(q\)
windows wholly internal to retained paths.  Then the exact new loads are

\[
 \boxed{
 \mu_{q,S}^{-,\rm new}
 =
 \mu_{q,S}^{-,\rm int}
 +
 \sum_{i,j}p_{ij}\sum_{a=1}^{q}
 {\bf1}\!\left[
 L_{i,a}^{\cap}\cap R_{j,q+1-a}^{\cap}=S
 \right],}
\tag{5.8}
\]

\[
 \boxed{
 \mu_{q,T}^{+,\rm new}
 =
 \mu_{q,T}^{+,\rm int}
 +
 \sum_{i,j}p_{ij}\sum_{a=1}^{q}
 {\bf1}\!\left[
 L_{i,a}^{\cup}\cup R_{j,q+1-a}^{\cup}=T
 \right].}
\tag{5.9}
\]

Consequently complete lower and upper support through depth \(H\) is
equivalent to

\[
 \mu_{q,S}^{-,\rm new}\ge1,\qquad
 \mu_{q,T}^{+,\rm new}\ge1
\tag{5.10}
\]

for every required target and \(q\le H\).

#### Proof

A permutation reconnects every old tail once and every old head once.
Every internal owner keeps its two retained incidences, and every boundary
owner regains its missing incidence, proving middle-degree preservation.
The colour of \(t_i h_j\) is exactly the pair (5.4), so (5.5)--(5.6) are
necessary and sufficient for the depth-one multisets.

A \(q\)-edge window has \(q+1\) vertices.  Because every retained path has
at least \(H\) vertices and \(q\le H\), it crosses at most one new seam.
It is therefore either internal or is uniquely described by:

* the installed seam \(t_i\to h_j\); and
* the number \(a\in\{1,\ldots,q\}\) of its vertices on the left.

Its intersection and union are exactly the terms in (5.8) and (5.9).
Summing the exhaustive disjoint cases proves both identities.  Inequalities
(5.10) are the definition of complete support.  \(\square\)

At \(q=1\), equations (5.8)--(5.9) reduce to the diamond row and column
ledgers.  No depth-one alternating-cycle identity implies the constraints
at \(q\ge2\).

### Corollary 5.2 (component and path constraints)

The components of the rethreaded two-factor are exactly the directed cycles
of the permutation \(p\).  It is one component if and only if, in addition
to (5.3),

\[
 \sum_{\substack{i\in A\\j\notin A}}p_{ij}\ge1
 \qquad
 (\varnothing\ne A\subsetneq[s]).
\tag{5.11}
\]

More generally, deleting \(p_0\) installed seams opens its cycles into
\(p_0\) paths.  The deleted seam colours and deeper crossing flags then
enter the hole ledger or must be reconstructed by boundary charts.

#### Proof

Contract each retained path to one directed vertex.  The installed seams
give the permutation digraph.  A permutation is one directed cycle exactly
when it has no nonempty proper closed subset, which is (5.11).  The path
statement is immediate after deleting one seam from each chosen cycle.
\(\square\)

Theorem 5.1 is an exact integral formulation.  Its matrix is not asserted
to be totally unimodular after (5.10) and (5.11) are added.

### Theorem 5.3 (exact multi-seam extension at every depth)

Keep the retained paths and permutation variables above, and write

\[
 {\cal P}_i=(V_{i,0},\ldots,V_{i,\ell_i-1}).
\]

For \(q\ge1\), let \({\mathfrak W}_q\) be the set of records

\[
 \omega=(i_0,u;i_1,\ldots,i_t;v),\qquad t\ge1,
\tag{5.12}
\]

such that

\[
 (\ell_{i_0}-u)
 +\sum_{r=1}^{t-1}\ell_{i_r}
 +(v+1)=q+1,
\tag{5.13}
\]

with

\[
 0\le u<\ell_{i_0},\qquad
 0\le v<\ell_{i_t}.
\]

Associate to \(\omega\) the ordered owner list consisting of:

1. the suffix \(V_{i_0,u},\ldots,V_{i_0,\ell_{i_0}-1}\);
2. every whole intermediate path \({\cal P}_{i_1},\ldots,
   {\cal P}_{i_{t-1}}\); and
3. the prefix \(V_{i_t,0},\ldots,V_{i_t,v}\).

Let \(I(\omega)\) and \(U(\omega)\) be the intersection and union of that
list.  Then, for every binary permutation matrix \(p\), the exact
depth-\(q\) loads are

\[
 \boxed{
 \mu_{q,S}^{-,\rm new}
 =
 \mu_{q,S}^{-,\rm int}
 +
 \sum_{\omega\in{\mathfrak W}_q}
 \left(\prod_{r=0}^{t-1}p_{i_r i_{r+1}}\right)
 {\bf1}[I(\omega)=S],}
\tag{5.14}
\]

\[
 \boxed{
 \mu_{q,T}^{+,\rm new}
 =
 \mu_{q,T}^{+,\rm int}
 +
 \sum_{\omega\in{\mathfrak W}_q}
 \left(\prod_{r=0}^{t-1}p_{i_r i_{r+1}}\right)
 {\bf1}[U(\omega)=T].}
\tag{5.15}
\]

The indices \(i_r\) need not be distinct; this includes windows which wrap
around a short final component.  On \(0\)-\(1\) permutation matrices,
repeated factors may be reduced using \(p_{ij}^2=p_{ij}\).

Consequently preservation of the complete PBBS flag tower at every desired
depth is exactly the family of polynomial inequalities obtained by putting
(5.14)--(5.15) at least one.  If every retained path has at least \(H\)
vertices and \(q\le H\), every contributing record has \(t=1\), and these
polynomials reduce to the linear formulas (5.8)--(5.9).

#### Proof

Every noninternal \(q\)-edge window has a unique first retained path, start
position, sequence of complete intervening retained paths, last retained
path, and end position.  Its total of \(q+1\) owners is exactly (5.13).
It occurs under \(p\) precisely when every seam on its itinerary is
installed, which is the product in (5.14)--(5.15).  Conversely every record
whose product is one is one such window.  The internal and noninternal
classes are disjoint and exhaustive, proving the identities.

If \(q\le H\) and every retained path has at least \(H\) vertices, a
\((q+1)\)-vertex window cannot traverse a whole intermediate path and hence
cannot cross two seams.  Thus \(t=1\), recovering Theorem 5.1.  \(\square\)

## 6. H-safe collars and the unavoidable cut transversal

Write an oriented Johnson transition as

\[
                         X_{r+1}=X_r-a_r+b_r.
\tag{6.1}
\]

Recall that compiler-H-safety requires:

1. the \(2H\) departure/arrival labels in every \(H\)-transition window to
   be pairwise distinct; and
2. every internally bounded positive coordinate run to have at least
   \(H+1\) vertices.

For a candidate seam \(t_i\to h_j\), its H-collar consists of the last
\(H\) transitions available on \({\cal P}_i\), the seam, and the first
\(H\) transitions available on \({\cal P}_j\), truncated only at genuine
path endpoints.

### Theorem 6.1 (exact separated-collar safety criterion)

Assume the retained paths are internally compiler-H-safe and each has at
least \(H+1\) vertices.  A rethreading \(p\) is compiler-H-safe if and only
if every transition window or positive run meeting an installed seam
passes the two safety tests above.

Equivalently, delete \(p_{ij}\) from the seam catalogue whenever its full
H-collar contains a forbidden H-transition repetition or an internally
bounded positive run of at most \(H\) vertices.  Under the separation
hypothesis, every remaining permutation is compiler-H-safe.

The stronger local condition \(G_{H+1}\) on every seam collar is sufficient,
but is not necessary.

#### Proof

Every unsafe window or run is either wholly internal to a retained path or
meets a new seam.  The first class is excluded by internal safety.  Since a
retained path has at least \(H+1\) vertices, neither an \(H\)-transition
window nor an internally bounded positive run of at most \(H\) vertices
can cross both seams adjacent to that path.  Hence every remaining bad test
lies in one listed seam collar.  This proves necessity and sufficiency.
The final statement follows from the usual
\(G_{H+1}\Rightarrow\) compiler-H-safe implication.  \(\square\)

The \(H+1\) here is sharp for a purely one-seam test: if a retained path has
exactly \(H\) vertices, one coordinate can be inserted at its incoming seam,
remain present on all \(H\) vertices, and be deleted at its outgoing seam.
That forbidden run meets two seams and is invisible to either truncated
one-seam collar.

The internal-safety hypothesis cannot be obtained from seam choices alone.

### Theorem 6.2 (sharp segment-retaining cut obstruction)

Let \({\cal I}_H(F)\) be the family of old positive-coordinate runs whose
residence length is at most \(H\), each represented by the transition-edge
interval from its insertion edge through its removal edge.  If a rebundling
retains the order of every fragment, then every member of
\({\cal I}_H(F)\) wholly contained in a retained fragment survives.
Therefore the set of deleted old transitions must be a transversal of
\({\cal I}_H(F)\) before the result can be compiler-H-safe.

Writing \(\tau_H(F)\) for the minimum transversal size and \(\nu_H(F)\)
for the maximum transition-edge-disjoint packing size, every such
rebundling changing \(J\) old transitions satisfies

\[
                         \boxed{J\ge\tau_H(F)\ge\nu_H(F).}
\tag{6.2}
\]

The assertion remains true when retained fragments are reversed.

#### Proof

Reversal changes neither the vertex set nor the equality pattern of a
coordinate run on a retained interval.  Thus an old bad interval avoiding
all cuts remains a bad internal interval.  Every globally safe result must
therefore cut every member of \({\cal I}_H(F)\), proving
\(J\ge\tau_H(F)\).  Any one deleted transition can meet at most one member
of an edge-disjoint packing, so the standard packing-transversal inequality
gives \(\tau_H(F)\ge\nu_H(F)\).  \(\square\)

For a fixed owner shore, (6.2) is exact.  Identifying which PBBS shore it
controls requires care.

### Corollary 6.3 (exact PBBS shore and complement audit)

Let \(F_A\) be the rank-\(m\) PBBS step-two factor used by the diamond
table, and let

\[
                         F_X=\{\overline A:A\in F_A\}
\tag{6.3}
\]

be its rank-\((m+1)\) complement factor.  Write
\({\cal I}_H^+(F_A)\) and \({\cal I}_H^0(F_A)\) for, respectively, the
short positive-run and short zero-run interval families on the \(A\)-shore.
Then:

1. a compiler-H-safe segment-retaining construction literalized directly
   on \(F_A\) must satisfy

   \[
    J\ge\tau_H^+(F_A)\ge\nu_H^+(F_A);
   \tag{6.4}
   \]

2. a compiler-H-safe construction on the physical complement shore \(F_X\)
   must satisfy

   \[
    J\ge\tau_H^0(F_A)\ge\nu_H^0(F_A)
      =\nu_H(F_X)=\nu_H(P_m).
   \tag{6.5}
   \]

Complementation preserves the \(G_H\) no-repeat property but exchanges the
positive-run and zero-run conditions.  It also takes every clean C6 switch
on \(F_A\) to an exact Johnson-factor switch on \(F_X\), and exchanges lower
intersections with complements of upper unions at every protected depth.

No equality between \(\nu_H^+(F_A)\) and \(\nu_H^0(F_A)\) is asserted.

#### Proof

For each coordinate, complementation replaces its binary owner indicator by
one minus that indicator.  Hence positive runs on \(F_X\) are exactly zero
runs on \(F_A\), with the same insertion-through-removal edge supports
after the direction labels are swapped.  Pairwise distinct transition
labels are unchanged as a property.  This proves the residence statements;
(6.4) is Theorem 6.2 on \(F_A\), and (6.5) is Theorem 6.2 on \(F_X\).

Complementation is an isomorphism from \(J(n,m)\) to \(J(n,m+1)\), so it
transports the clean C6 factor trade.  Finally De Morgan's laws give

\[
 \overline{\bigcap_j A_j}=\bigcup_j\overline{A_j},
\qquad
 \overline{\bigcup_j A_j}=\bigcap_j\overline{A_j},
\]

which proves the flag assertion.  \(\square\)

Thus the \(2m(m-1)\) ambient clean-C6 extensions do not remove the
authoritative PBBS cut obstruction on \(F_X\), but one must test zero-run
collars on the displayed rank-\(m\) table shore.

## 7. A conditional clean-C6 hypertree theorem

Form a 3-uniform hypergraph on the current projected-factor components.
A hyperedge is a PBBS-realized clean C6 satisfying the following
current-table conditions:

1. the three row-map equations (4.3), evaluated in the current table;
2. one old C6 edge in each of three distinct current components;
3. one of the two coherent orientations of Theorem 3.1;
4. unused old collars separated so that every retained fragment between
   installed seams has at least \(H+1\) vertices; and
5. legal new seam collars.

In a selected family, require affected columns and old edges of different
clean triples to be disjoint.  Under this disjointness, evaluating (4.3) in
the initial PBBS row map is equivalent to evaluating it when the switch is
installed.

Call an ordered family \(e_1,\ldots,e_s\) a loose spanning hypertree if
\(e_1\) uses three initial components and, after each contraction, \(e_j\)
meets the already merged component in one old component and introduces two
new components.

### Theorem 7.1 (conditional C6 linearization)

Suppose the initial factor has \(c=2s+1\) components and admits such a loose
spanning hypertree.  Sequential clean-C6 switching produces one projected
factor component.  Every depth-one \(R\)-load and every \(U\)-column is
preserved exactly.

For each switch and each target, let
\(\Delta_{e,q,S}^{\pm}\) be its signed current-context change in the
depth-\(q\) load.  If

\[
 \mu_{q,S}^{\pm}
 +\sum_{e}\Delta_{e,q,S}^{\pm}\ge1
 \qquad(q\le H)
\tag{7.1}
\]

for every required target, then the complete lower and upper flag tower
through \(H\) survives.  If the removed edges also hit every old bad
residence interval on the owner shore being literalized and all new collars
are safe, the resulting projected cycle is compiler-H-safe.  For the
physical \(F_X\)-shore, use the zero-run collar test on \(F_A\) from
Corollary 6.3.

If \(c\) is even, clean-C6 switching alone cannot produce one component,
but the identical conclusion gives two components when a loose forest with
\((c-2)/2\) mergers exists.

#### Proof

Each hyperedge meets three distinct current components and Theorem 3.1
merges them, reducing the count by two.  The loose order therefore leaves
one component from \(2s+1\), or two from an even initial count.  Theorem
3.1 preserves every row and column at each step.  Equation (7.1) is the
telescoped exact flag ledger; H-separation allows the changes to be read in
their disjoint collars, while current-context evaluation works without
that simplification.  The safety conclusion is Theorems 6.1--6.2.
Component parity is Corollary 3.2.  \(\square\)

Theorem 7.1 is deliberately conditional.  Neither a positive-density
PBBS-realized clean-C6 bank nor a spanning loose hypertree satisfying
(7.1) is proved.

## 8. Exact literal owner and boundary interface

The relevant compiler theorem does not require a wreath.

### Theorem 8.1 (H-safe projected paths suffice for central-band
literalization)

Let \({\cal P}\) be an owner-disjoint family of compiler-H-safe Johnson
paths in \(J(k,r)\).  Suppose it contains \(M\) distinct middle owners in
\(p\) paths.  For \(q\le H\), let \(h_q^-\) and \(h_q^+\) be the numbers of
missing actual lower intersections and upper unions.  Assume

\[
                         H\le\min(r-1,k-r).
\tag{8.1}
\]

Then there is a literal nonzero contiguous-OR word covering every middle
owner and every target through depth \(H\), of length

\[
 \boxed{
 L_H\le
 \binom kr+Hp+
 \sum_{q=1}^{H}(h_q^-+h_q^+).}
\tag{8.2}
\]

#### Proof

For a path \(T_0,\ldots,T_{\ell-1}\), use a block of length \(\ell+H\)
and define the endpoint-capped envelope

\[
 E_s=
 \bigcap_{\substack{0\le i<\ell\\s\in[i,i+H]}}T_i.
\tag{8.3}
\]

Let \(D\) denote one-step adjacent union,
\((DE)_i=E_i\cup E_{i+1}\).  The positive-run condition gives
\(D^HE=T\).  The no-repeat trace identities
give, whenever the indicated window exists,

\[
 (D^{H-q}E)_{i+q}=\bigcap_{j=0}^{q}T_{i+j},
\qquad
 (D^{H+q}E)_i=\bigcup_{j=0}^{q}T_{i+j}.
\tag{8.4}
\]

Thus all actual packet traces are literal contiguous ORs.  Concatenating
the \(p\) blocks costs \(M+Hp\).  Append every unused middle owner once and
every missing target once.  Cross-block intervals can only add
occurrences.  The total is (8.2).  \(\square\)

### Corollary 8.2 (the exact interface for switched PBBS tables)

Start with the rank-\(m\) projected PBBS table and apply any integral
diamond switches satisfying Theorem 1.1.  Either literalize the resulting
rank-\(m\) paths directly, or complement the entire switched factor and
literalize its rank-\((m+1)\) paths.  Cut the chosen factor into \(p\)
owner-disjoint paths, and suppose:

1. the paths pass Theorem 6.1 on the chosen shore (equivalently, use the
   zero-run audit of Corollary 6.3 when the chosen shore is \(F_X\));
2. their actual chronological flag holes through \(H\) total \(h\).

Then a literal central-band word exists with

\[
                            L_H\le W+Hp+h.
\tag{8.5}
\]

If the path traces themselves retain complete support, then \(h=0\) in
(8.5).  Suppose instead that \(J_{\rm chart}\) final cut collars have
separately certified boundary charts of length at most \(4H-1\); the known
dominance-staircase theorem supplies such charts at eligible old PBBS cuts,
not at arbitrary new seams.  Their letters must be charged.  Writing
\(h_{\rm res}\) for all remaining one-letter repairs, the corresponding
ledger is

\[
 L_H\le
 W+Hp+h_{\rm res}+(4H-1)J_{\rm chart}.
\tag{8.5a}
\]

Thus a boundary chart repairs holes but does not make its physical cost
disappear from (8.5).

This proves the requested logical point:

\[
\boxed{
\text{H-safe Johnson path packets, not full wreath packets, suffice for
central-band literalization.}}
\tag{8.6}
\]

What they do not supply automatically is H-safety, the protected-depth flag
support, or a small hole ledger.  A full universal word additionally uses
the proved outer-tail theorem.

Every operation in this interface is integral: the diamond table remains a
single \(0\)-\(1\) owner factor until it is cut, and (8.3) then constructs
one literal OR word.  No averaging or diagonalization between unrelated
factors is used.

For a fixed finite length with central pins and no explicit repair letters,
one retains the existential packet pin-compatible sandwich condition.  It
chooses a compatible interval injection even when the witness intervals
were not prescribed in advance.  This is an additional placement
constraint, not a prerequisite for the extra-letter provider-union theorem
(8.2).

## 9. The exact proved and conditional boundary

The clean C6 is the first physical manifestation of the \(m^2\) flag-graph
entropy:

\[
\begin{array}{c}
\text{one rectangle: row/column exact but owner-unbalanced;}\\
\text{one clean C6: row/column/owner exact and capable of a three-cycle
merge.}
\end{array}
\]

Nevertheless, four independent gates remain.

1. **PBBS realization.**  The ambient degree is \(2m(m-1)\), but every
   usable C6 needs the two companion coincidences in (4.3).  No realized
   minimum-degree or expansion theorem is known.

2. **Residence cutting.**  Every segment-retaining H-safe construction
   still pays \(J\ge\tau_H(F)\ge\nu_H(F)\) on the literalized shore.
   For the physical \(F_X\)-shore this is the authoritative
   \(\nu_H(P_m)\); on the displayed \(F_A\)-shore it is the separate
   positive-run packing.  Local merging does not erase internal bad
   intervals.

3. **Protected-depth chronology.**  Depth-one row/column preservation is
   automatic for a clean C6.  At depths \(2\le q\le H\), the exact
   separated-seam conditions are (5.8)--(5.10), or equivalently the signed
   current-context loads (7.1).  Beyond \(H\), the exact conditions are the
   multi-seam polynomial ledgers (5.14)--(5.15); what fails is linearity,
   not the characterization.

4. **Boundary service.**  Opening the final cycles costs \(Hp\), and every
   lost crossing flag must be supplied by a safe boundary chart or counted
   as a literal repair.

Thus the hoped-for implication

\[
 \text{ambient C6 degree }\asymp m^2
 \Longrightarrow
 \text{owner leave or flag defect }O(W/m)
\]

is false as an inference.  The missing theorem is a correlated integral
selection in the PBBS row map, not another Hamiltonization theorem and not
another rankwise balancing lemma.

The strongest exact positive target exposed here is:

> Construct a PBBS-realized clean-C6 loose forest, or a separated-seam
> permutation satisfying (5.3), (5.5), (5.6), (5.10), and the H-collar
> exclusions, whose removed transitions form a residence transversal and
> whose final path count and literal hole ledger are \(o(W/H)\) and \(o(W)\),
> respectively.

That target would compose directly with Theorem 8.1.  Its existence remains
unproved.

## 10. The exact \(k=15\) Shadow--Braid and the unit-pin obstruction

This section specializes the clean C6 to the physical rank-eight shore of
the frozen \(k=15\), depth-three compiler.  It uses the corrected finite
input from

```text
MATH_K15_HALL29_UNIT_PIN_COVER_20260728.md
```

namely that a 29-address repair by **unit-boundary pins** needs at least 24
distinct pins.  The superseded number 14 allowed arbitrary erosion-incidence
additions with as many as four deficient carrier owners and is not used.

Throughout this section, a clean C6 is installed by cutting three internal
transitions, transporting the retained fragments without changing their
interiors, and reconnecting them.  Every retained fragment has at least four
owners.  Thus a four-owner window crosses at most one seam.  Endpoint-moving
relinearizations are treated separately in Section 10.7.

### 10.1 The complement-shore C6 preserves the two adjacent shadows

Set \(m=7\).  In the notation of Section 3, let

\[
 K\in\binom{[15]}5,
 \qquad a_0,a_1,a_2,c\notin K
\]

be distinct, and put

\[
 D=[15]\setminus(K\cup\{a_0,a_1,a_2,c\}),
 \qquad |D|=6.
\tag{10.1}
\]

On the rank-eight complement shore write, modulo three,

\[
 X_i=\overline{P_i}=D\cup\{a_{i+2},c\},
 \qquad
 Y_i=\overline{Q_i}=D\cup\{a_{i+1},a_{i+2}\}.
\tag{10.2}
\]

The old and new arcs are respectively

\[
 X_i\longrightarrow Y_i=(-c,+a_{i+1}),
 \qquad
 X_i\longrightarrow Y_{i+1}=(-c,+a_i).
\tag{10.3}
\]

#### Proposition 10.1 (exact adjacent-shadow transport)

At the \(i\)-th affected physical seam,

\[
 X_i\cap Y_i=X_i\cap Y_{i+1}
 =D\cup\{a_{i+2}\}=:\Lambda_i.
\tag{10.4}
\]

Thus the adjacent lower shadow is preserved pointwise.  The adjacent upper
shadows satisfy

\[
 X_i\cup Y_{i+1}=X_{i+1}\cup Y_{i+1},
\tag{10.5}
\]

so the three upper shadows are cyclically permuted.  Hence both complete
cyclic depth-one shadow multisets, with their multiplicities, are preserved
exactly.

#### Proof

Equations (10.4)--(10.5) follow immediately from (10.2):

\[
 X_i\cap Y_i=X_i\cap Y_{i+1}=D+a_{i+2},
\]

while both sides of (10.5) equal

\[
 D\cup\{c,a_i,a_{i+2}\}.
\]

The old upper label at seam \(i+1\) therefore becomes the new upper label
at seam \(i\).  \(\square\)

The word *preserve* in Proposition 10.1 is essential.  Lower shadows are
pointwise fixed at the three seams; upper shadows are preserved only as a
multiset.  Requiring both the old intersection and the old union at the
same affected slot would force the old Johnson edge itself, because a
Johnson edge is determined by its intersection and union.  Thus a
nontrivial clean C6 cannot preserve both shadows pointwise.

Opening a cyclic owner factor into a linear path removes one adjacent edge.
That lost cyclic shadow must be supplied by the endpoint-capped compiler.
Proposition 10.1 does not make this linear boundary obligation disappear.

### 10.2 The exact depth-three envelope current

Delete the old arcs \(X_i\to Y_i\), and orient the retained fragments as

\[
                         {\cal S}_i=(Y_i,\ldots,X_i).
\]

For \(1\le a\le3\), let \(L_{i,a}\) be the intersection of the last
\(a\) owners of \({\cal S}_i\), and let \(R_{j,a}\) be the intersection of
the first \(a\) owners of \({\cal S}_j\).  If a crossing four-owner window
uses \(b\) owners on the right of a seam, its old and new maximal erosion
masks are

\[
 Q^-_{i,b}=L_{i,4-b}\cap R_{i,b},
 \qquad
 Q^+_{i,b}=L_{i,4-b}\cap R_{i+1,b},
 \qquad b=1,2,3.
\tag{10.6}
\]

Here the new clean-C6 seam is \(X_i\to Y_{i+1}\).

#### Theorem 10.2 (two mutable masks and twelve gained incidences)

For every seam \(i\),

\[
                         Q^-_{i,1}=Q^+_{i,1}.
\tag{10.7}
\]

For \(b=2,3\), both masks in (10.6) lie in the same seven-set
\(\Lambda_i\), and

\[
                  |Q^+_{i,b}\setminus Q^-_{i,b}|\le2.
\tag{10.8}
\]

Consequently one seam creates at most four genuinely new
coordinate-position erosion incidences, and one three-seam clean C6 creates
at most

\[
                         \boxed{12}
\tag{10.9}
\]

such incidences.

#### Proof

Because \(L_{i,3}\subseteq X_i\), (10.4) gives

\[
\begin{aligned}
 Q^-_{i,1}
 &=L_{i,3}\cap Y_i
   =L_{i,3}\cap\Lambda_i\\
 &=L_{i,3}\cap Y_{i+1}
   =Q^+_{i,1},
\end{aligned}
\]

proving (10.7).

For \(b=2,3\), the left intersection is still contained in \(X_i\), while
the right intersection is contained in its first owner, \(Y_i\) or
\(Y_{i+1}\).  Hence both old and new masks lie in \(\Lambda_i\).  The old
mask is the intersection of four consecutive rank-eight Johnson owners.
Three transitions can delete at most three distinct members of the first
owner, so

\[
                         |Q^-_{i,b}|\ge8-3=5.
\]

It follows that \(|\Lambda_i\setminus Q^-_{i,b}|\le2\), and the new-minus-old
set is contained in this complement.  This proves (10.8).  There are two
mutable masks per seam and three seams.  \(\square\)

No rank-five equality was used in the proof.  Thus (10.9) remains valid
under positive depth-three residence alone; repeated transition labels can
only make an old four-owner intersection larger and reduce its possible
gain.

For a weight tensor \(w_{i,b,x}\), the complete signed pin current is the
literal identity

\[
 \Delta(w)=
 \sum_{i=0}^{2}\sum_{b=1}^{3}\sum_{x\in[15]}
 w_{i,b,x}{\bf1}[x\in L_{i,4-b}]
 \left({\bf1}[x\in R_{i+1,b}]
      -{\bf1}[x\in R_{i,b}]\right).
\tag{10.10}
\]

It records dependencies exactly; the pin signs are not independent cube
choices.

### 10.3 Unit-boundary pins and the one-C6 no-go

An old interior erosion position \(p\) is defined by four consecutive
owners.  A pair \((p,x)\) is a unit-boundary pin when exactly one of those
four owners omits \(x\).  It is **locally implemented** by the C6 when the
canonically corresponding new four-owner mask contains \(x\).  Equivalently,
for a crossing phase in (10.6),

\[
 \#\{V\text{ in the old four-owner window}:x\notin V\}=1,
 \qquad x\in Q^+_{i,b}.
\tag{10.11}
\]

The first condition implies \(x\notin Q^-_{i,b}\), so every implemented
unit pin is counted by (10.8).

#### Corollary 10.3 (one clean C6 cannot install the Hall-29 unit interface)

In the transported, fixed-endpoint model, one clean C6 implements at most
12 distinct unit-boundary pins.  In the audited frozen Hall-29 atlas, \(t\)
unit pins expose at most \(t+5\) pairwise target- and cell-disjoint
target/address records.  Therefore one clean C6 exposes at most

\[
                         12+5=17
\tag{10.12}
\]

of the 29 required records through this interface.  In particular, it
cannot realize any full unit-boundary-pin Hall-29 repair, whose sharp
optimistic pin minimum is 24.

#### Proof

Theorem 10.2 gives \(t\le12\).  The exact finite unit-pin theorem says that
no pin serves three disjoint records and that at most five double-serving
pins can coexist, giving at most \(t+5\) records.  Since \(17<29\), the
conclusion follows.  Equivalently, \(12<24\) already contradicts the sharp
pin-cover lower bound.  \(\square\)

There is a useful strengthening when the word *safe* includes the full
\(G_3\) trace-rainbow condition, not merely positive residence.

#### Proposition 10.4 (six-pin bound under full compiler-3-safety)

Assume every three-transition window has six pairwise distinct departure
and arrival labels.  Then each mutable four-owner window implements at most
one old unit-boundary pin.  Hence one seam implements at most two, and one
clean C6 at most

\[
                         \boxed{6}
\tag{10.13}
\]

unit pins.  The corresponding optimistic record bound is \(6+5=11\).

#### Proof

The membership trace of a unit coordinate on the old four-owner window has
one zero.  The first owner lies in the unchanged left suffix.  If it is the
zero, the new window still omits \(x\), so the pin is not gained.  An
interior zero would delete and reinsert \(x\) within the three transitions,
repeating \(x\) among their change labels and violating \(G_3\).  Therefore
the only gainable trace is

\[
                         1110.
\]

Its zero is produced by the unique departure on the final old transition,
so at most one coordinate has this trace.  There are two mutable windows
per seam and three seams.  \(\square\)

The main no-go, Corollary 10.3, uses only the weaker bound (10.9), so it
does not depend on \(G_3\).

The displayed audited 24-pin witness is even more dispersed.  Its 24 pairs
occupy 24 distinct source positions, and no two displayed positions are
consecutive.  Under the tail-anchored canonical identification in which a
seam's mutable pair is matched to the two consecutive old slots immediately
following its deleted transition, the three mutable pairs of one C6 can
therefore meet at most three pins of that displayed witness.  This last
statement concerns the displayed witness; Corollary 10.3 concerns every
possible 24-pin cover.

### 10.4 Exact residence and exact local pin criterion

For completeness, the positive-residence test at a new seam can be written
without any probabilistic or rankwise relaxation.  Index the seam transition
by zero,

\[
 B_{t+1}=B_t-\alpha_t+\beta_t,
 \qquad (\alpha_0,\beta_0)=(c,a_i).
\]

Assuming the two retained interiors are already depth-three resident, the
new seam is depth-three resident if and only if

\[
\begin{array}{lll}
 \beta_{-1}\ne c,&a_i\ne\alpha_1,\\
 \beta_{-2}\ne c,&\beta_{-1}\ne\alpha_1,
     &a_i\ne\alpha_2,\\
 \beta_{-3}\ne c,&\beta_{-2}\ne\alpha_1,
     &\beta_{-1}\ne\alpha_2,
     \quad a_i\ne\alpha_3.
\end{array}
\tag{10.14}
\]

These are exactly the pairs

\[
                         \beta_s\ne\alpha_t,
 \qquad s<t,\quad t-s\le3,
\tag{10.15}
\]

whose insertion-to-deletion interval crosses the seam.  Thus (10.14) is
necessary and sufficient: it excludes every newly created internally
bounded positive run of at most three owners.  Coherent reversal gives the
same criterion after reversing the transition labels.

Now fix an audited defect-one record \((T,\chi,p,x)\), where \(T\) is a lower
target, \(\chi=(b,h)\) is its proposed physical cell,

\[
                         I_\chi=[b,b+h],\qquad0\le h\le2,
\]

and \((p,x)\), \(p\in I_\chi\), is its unit pin.  Let \(Q'_u\) be the final
maximal erosion masks.  Define

\[
 E'_\chi=\bigcup_{u\in I_\chi}Q'_u
\tag{10.16}
\]

For \(x\in T'_t\), put

\[
 C'(t,x)=\{u\in[t,t+3]:x\in Q'_u\},
\]

and define the exact mandatory mask

\[
 M'_\chi=
 \{x:\text{some nonempty }C'(t,x)\text{ is contained in }I_\chi\}.
\]

Both masks are computed from the final chronology.

#### Theorem 10.5 (exact carrier-level one-address test)

Assume every retained fragment interior is already depth-three resident.
Then the clean C6 implements the displayed pin of \((T,\chi,p,x)\), makes
\((T,\chi)\) a final carrier candidate, and preserves depth-three residence
if and only if all of the following hold:

1. \(p\) is one of the two mutable crossing phases at a selected seam and
   satisfies the literal pin condition (10.11);
2. the three seam collars satisfy (10.14);
3.

   \[
               M'_\chi\subseteq T\subseteq E'_\chi;
   \tag{10.17}
   \]

4.

   \[
               T\cap Q'_u\ne\varnothing
               \qquad(u\in I_\chi).
   \tag{10.18}
   \]

It is a genuinely new unpeeled Hall-29 address precisely when, in addition,
\(\chi\notin N_0(A_{29})\).  In the retained peeled architecture it must instead
be unreserved and distinct from every other chosen residual cell.

#### Proof

Conditions 1--2 say exactly that the proposed erosion incidence was created
by a legal resident C6; the retained-interior hypothesis excludes every
non-seam residence defect.  Conditions (10.17)--(10.18) are the exact
necessary-and-sufficient carrier-candidate criterion from equations
(1.6)--(1.7) of
MATH_LANE_I_K15_HALL29_EXACT_BOUNDARY_INDICATOR_COMPILER_20260728.md,
evaluated after the C6.  The two final assertions are the definitions of a
new unpeeled neighbour and an available peeled cell.  \(\square\)

The old statement “the record had only one missing coordinate” is not
enough: changing the seam can also change its mandatory mask or destroy a
nonempty letter hit.  This is why (10.17)--(10.18) must be recomputed.

### 10.5 The one-common-word Shadow--Braid theorem

Carrier eligibility is still not literal realizability.  We now give the
exact simultaneous criterion in one physical word.

Let

\[
                         T'_0,\ldots,T'_{W-1}
                         \in\binom{[15]}8,qquad W=6435,
\]

be the final linear chronology, and put

\[
 Q'_p=
 \bigcap_{j=\max(0,p-3)}^{\min(p,W-1)}T'_j,
 \qquad0\le p\le W+2.
\tag{10.19}
\]

Let \({\cal L}\) be one family of exact interval-label requirements
\((I,S)\).  It must include every selected compiler target occurrence and
every protected lower-shadow occurrence.  In particular, the latter are

\[
 \left([i+1,i+3],\,T'_i\cap T'_{i+1}\right),
 \qquad0\le i<W-1.
\tag{10.20}
\]

Any prescribed values of the two endpoint cells in the linear
depth-one-lower row must also be included in \({\cal L}\); (10.20) lists
only the edge-determined interior occurrences.

If lower carrier traces through depths \(q=2,3\) are also protected, add

\[
 \left([i+q,i+3],\,
       \bigcap_{j=0}^{q}T'_{i+j}\right),
 \qquad q=2,3,
\tag{10.20a}
\]

for every displayed occurrence.  Their existence in the final carrier, and
all required upper support beyond depth one, must separately pass the exact
last-witness seam ledgers (5.8)--(5.10).

Let \(\Pi\subseteq[0,W+2]\times[15]\) be the prescribed positive pins.  For
each coordinate \(x\), define its surviving positions

\[
 Z_x=
 \{p:x\in Q'_p\}
 \setminus
 \bigcup_{\substack{(I,S)\in{\cal L}\\x\notin S}} I.
\tag{10.21}
\]

#### Theorem 10.6 (necessary and sufficient one-word criterion)

There exists one nonzero physical word

\[
                         A_0,A_1,\ldots,A_{W+2}
\]

such that

\[
 D^3A=T',
 \qquad
 \bigcup_{p\in I}A_p=S\quad((I,S)\in{\cal L}),
 \qquad
 x\in A_p\quad((p,x)\in\Pi)
\tag{10.22}
\]

if and only if all four conditions below hold:

\[
 (p,x)\in\Pi\Longrightarrow p\in Z_x;
\tag{10.23}
\]

\[
 [i,i+3]\cap Z_x\ne\varnothing
 \qquad(0\le i<W, x\in T'_i);
\tag{10.24}
\]

\[
 I\cap Z_x\ne\varnothing
 \qquad((I,S)\in{\cal L}, x\in S);
\tag{10.25}
\]

and

\[
 \bigcup_{x\in[15]}Z_x=[0,W+2].
\tag{10.26}
\]

When they hold, the coordinatewise maximal common word is

\[
                         \boxed{A_p=\{x:p\in Z_x\}.}
\tag{10.27}
\]

#### Proof

Every factor of \(T'\) satisfies \(A_p\subseteq Q'_p\).  If
\(x\notin S\) and \(p\in I\), exactness of the union on \(I\) forces
\(x\notin A_p\).  Therefore every possible support position of \(x\) lies
in \(Z_x\), proving the necessity of (10.23)--(10.26).

Conversely, take (10.27).  Its entries are nonempty by (10.26).  Since
\(A_p\subseteq Q'_p\), every central union is contained in \(T'_i\), while
(10.24) supplies every coordinate of \(T'_i\); hence \(D^3A=T'\).  For an
interval \((I,S)\), definition (10.21) excludes every coordinate outside
\(S\), and (10.25) supplies every coordinate in \(S\).  Thus its union is
exactly \(S\).  Finally (10.23) gives every prescribed pin.  \(\square\)

The adjacent upper shadows require no extra word constraint: (10.22)
implies

\[
 (D^4A)_i=(D(D^3A))_i=T'_i\cup T'_{i+1}.
\tag{10.28}
\]

The lower shadows do require (10.20), because shrinking maximal erosion
letters can otherwise lose a coordinate from the overlap interval.

For the frozen trace-two architecture one must not require the maximal word
(10.27) itself to have controller dimension two: a smaller feasible word
might.  The exact refinement is instead the following existential
condition.  At every position \(p\), choose a set \(\Gamma_p\) of at most
two actually active **controller-eligible owner labels**, each active at
\(p\), and put

\[
 B_p(\Gamma)=Q'_p\cap\bigcap_{S\in\Gamma_p}S.
\tag{10.29}
\]

Then require:

\[
 B_p(\Gamma)\ne\varnothing,
 \qquad
 B_p(\Gamma)\subseteq S
 \quad\text{for every }(I,S)\in{\cal L}\text{ with }p\in I;
\tag{10.30}
\]

\[
 (p,x)\in\Pi\Longrightarrow x\in B_p(\Gamma);
\tag{10.31}
\]

and the positive-hit conditions (10.24)--(10.25) with

\[
                         Z_x^\Gamma=\{p:x\in B_p(\Gamma)\}
\tag{10.32}
\]

in place of \(Z_x\).  These conditions are necessary and sufficient for a
trace-two common word, with \(A_p=B_p(\Gamma)\).  This is exactly the
bulk-terminal-controller criterion.  Ordinary Hall eligibility and the
unrestricted maximal-word test do not imply it.

Combining Theorems 10.5--10.6 gives the promised exact finite answer for the
requested adjacent-shadow, depth-three-residence version.  A realized safe
C6 acts as a one-address Shadow--Braid precisely when it passes the
complement-shore shadow identities, all three residence collars, the final
carrier test (10.17)--(10.18), and conditions (10.23)--(10.26), with the
word then given by (10.27).  If trace two is retained, replace the maximal
word by the existential controller conditions (10.29)--(10.32).  If the
move is to remain inside the complete finite universal carrier, it must in
addition pass every required deeper lower/upper last-witness ledger
(5.8)--(5.10).  Every conclusion refers to this one \(A\); no independently
chosen rankwise row is used.

### 10.6 Compiler locality and the Hall current

At an internal seam between owner positions \(s,s+1\), only

\[
                         Q'_{s+2},\quad Q'_{s+3}
\tag{10.33}
\]

can differ from their transported old masks.  An interior depth-\(h\) cell,
\(h=0,1,2\), is determined by the masks from \(Q_{b-1}\) through
\(Q_{b+h+1}\).  Hence one seam can change exact eligibility on at most

\[
                         4,\quad5,\quad6
\tag{10.34}
\]

cells in the three rows, respectively.  One clean C6 therefore has at most
45 active interior compiler cells, not the generic 54 obtained when all
three crossing erosion masks are allowed to vary.

Let \(\Gamma_T(c)\) denote the candidate set of a cell.  Identify all
inactive old and new cells by transported fragments, and let
\({\cal A}^-\) and \({\cal A}^+\) be the old and new copies of every
remaining mutable address; an address active on both sides occurs in both
sets.  For any target shore \(X\), the exact Shadow current is

\[
 |N_{\rm new}(X)|-|N_{\rm old}(X)|
 =
 \sum_{c\in{\cal A}^+}{\bf1}[\Gamma_{\rm new}(c)\cap X\ne\varnothing]
 -
 \sum_{c\in{\cal A}^-}{\bf1}[\Gamma_{\rm old}(c)\cap X\ne\varnothing].
\tag{10.35}
\]

For the frozen shore \(A_{29}\), a complete repair must have current at
least 29.  Exposing one new address is only the first gate: losing one old
neighbour cancels it, every other Hall shore must remain valid, the residual
addresses must admit a matching, and Theorem 10.6 must hold for the full
selected owner family.

### 10.7 Exact proved boundary

The conclusions of this section have the following precise scope.

1. **One unit-pin C6 is ruled out as a full repair.**  Under canonical
   transport of retained fragments and fixed endpoints, one C6 creates at
   most 12 unit-pin incidences and at most 17 disjoint records, versus the
   sharp requirements 24 and 29.  Under full \(G_3\) safety these bounds
   improve to 6 and 11.

2. **One new address is conditional, not impossible.**  The clean-C6
   algebra neither forces nor forbids one actual Hall-29 pin.  Theorems
   10.5--10.6 are a finite necessary-and-sufficient test for it.  No
   concrete PBBS-realized C6 is proved here to pass that test.

3. **The no-go is interface-scoped.**  A C6 might create a candidate whose
   old defect involved two or more deficient carrier owners, change a
   mandatory core rather than add a unit pin, or participate in a correlated
   multi-C6 compound.  Corollary 10.3 does not exclude those routes.

4. **Absolute relocation is not a pin gain.**  Long block permutation can
   move an unchanged candidate profile to a different numerical address.
   Under the canonical right-shore braid this is a permutation and does not
   change any Hall-neighbourhood cardinality provided endpoints,
   reservations, protected occurrences, deadlines, and base eligibility
   are transported with it.  Otherwise the entire peeled matching and
   common-word certificate must be rebuilt; the 12-pin comparison is then
   not an absolute-index statement.

5. **Endpoints are separate.**  Moving the linear cut changes the exact
   eighteen-cell palette at either endpoint.  Such a construction must add
   those endpoint masks to (10.21) and re-audit the full Hall current.  It is
   not a one-internal-C6 consequence.

6. **Several switches are not independent signs.**  The bounds add for
   disjoint transported collars.  For overlapping nonmonotone compounds,
   a later defect need not remain unit-boundary relative to the original
   carrier; use the signed current (10.10), the exact seam ledgers
   (5.8)--(5.10), and the final common word (10.21)--(10.32).

Thus the safe C6 is a legitimate local Shadow--Braid carrier, but it is too
small to be the whole audited 24-pin Hall-29 repair.  The sharp surviving
finite target is a multi-collar or non-unit braid whose final selected
occurrences pass one simultaneous physical-word/controller test.

### 10.8 Isolated UNIT collars are acyclic: the surviving object is a
closed interacting deck circuit

The preceding pin-capacity theorem still allowed the misleading strategy of
installing many far-separated UNIT pins as independently checked
one-controller-state edits.  The exact finite replacement graph now rules
out that strategy at every cardinality.

Let \(P_0,\ldots,P_{W+2}\) be the maximal erosion controller of the frozen
Hall-29 chronology; the audited factor identity is

\[
                         T_i=\bigcup_{p=i}^{i+3}P_p.
\]

For an interior UNIT pin \((p,x)\), an isolated
rank-preserving edit has the form

\[
 P'_p=P_p-\{y\}+\{x\},
 \qquad
 P'_j=P_j\quad(j\ne p).
\tag{10.36}
\]

It is locally admissible only when the two controller adjacencies, every
affected four-controller union, and every affected middle Johnson adjacency
remain legal.  The exact census in
MATH_K15_UNIT_PIN_ISOLATED_CONTROLLER_CYCLE_NOGO_20260728.md gives:

\[
\begin{array}{c|r}
\text{UNIT pin types}&1602\\
\text{admitting one isolated edit}&1318\\
\text{admitting none in the flat model}&283\\
\text{boundary pin outside the flat model}&1\\
\text{vertices of the replacement digraph}&2295.
\end{array}
\tag{10.37}
\]

Every admissible edit has a unique deletion \(y\), changes exactly one
middle state \(T_q\) to one other deck state \(T_{q'}\), and hence defines
an arc \(q\to q'\).  The full 1,318-arc digraph is acyclic.  Only 14 of the
24 pins in the displayed UNIT witness even admit (10.36).

#### Theorem 10.7 (no separated isolated UNIT deck repair)

No nonempty family of pairwise distance-at-least-eight locally admissible
flat edits (10.36), drawn from the audited 1,602-pin Hall atlas and compared
pointwise in the frozen address system, preserves the exact middle deck.

#### Proof

At separation eight the affected controller states, four-window unions,
and adjacency tests are disjoint.  Thus each selected edit independently
removes one old deck value \(T_q\) and inserts \(T_{q'}\), and the selected
source indices are distinct.  Exact preservation of the deck multiset says
that the selected arcs have equal indegree and outdegree at every vertex.
They would therefore be a nonzero nonnegative circulation, equivalently a
nonempty union of directed cycles.  An acyclic digraph has no such
circulation.  \(\square\)

This is the exact meaning of the independent-collar no-go.  It rules out a
pin bank whose members are separately installed as one-state controller
replacements.  It does **not** rule out a separated bank of collar packets
in which each packet already changes several interacting controller states,
nor does it rule out a clean C6 reordering: one clean C6 has two adjacent
mutable controller masks per seam and its three seams are coupled by one
deck-preserving factor trade.

The surviving object can be stated without ambiguity.  For a finite
controller-edit support \(J\), take \(P'_p=P_p\) outside \(J\), and put

\[
 {\cal I}(J)=\{i\in[0,W-1]:[i,i+3]\cap J\ne\varnothing\},
 \qquad
 T'_i=\bigcup_{p=i}^{i+3}P'_p.
\tag{10.38}
\]

In the free abelian group on the rank-eight deck, define the exact deck
signature

\[
 \Sigma(J,P')
 =
 \sum_{i\in{\cal I}(J)}
 \left([T'_i]-[T_i]\right).
\tag{10.39}
\]

#### Proposition 10.8 (closed interacting-controller criterion)

Assume every \(T'_i\) in (10.38) has rank eight.  The controller edit
preserves the complete middle deck if and only if

\[
                         \boxed{\Sigma(J,P')=0.}
\tag{10.40}
\]

Since the frozen deck contains every rank-eight state exactly once and all
indices outside \({\cal I}(J)\) are fixed, (10.40) is equivalently the
existence of a permutation \(\phi\in\operatorname{Sym}({\cal I}(J))\) such
that

\[
                         T'_i=T_{\phi(i)}
 \qquad(i\in{\cal I}(J)).
\tag{10.41}
\]

It is a legal chronology only if, in addition, consecutive \(T'_i\)'s are
Johnson-adjacent.  A physical erosion controller further requires the
correct controller ranks and adjacencies,

\[
 P'_p=
 \bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T'_i,
\]

together with all residence, shadow, and common-word ledgers.

#### Proof

All middle windows outside \({\cal I}(J)\) are unchanged and cancel.
Inside \({\cal I}(J)\), equality of the old and new multisets is precisely
equality of the coefficient of every basis symbol in (10.39), which is
(10.40).  Uniqueness of the old deck values gives the equivalent permutation
(10.41).  Multiset equality alone contains no order information, so the
adjacency and chronological conditions remain separate.  \(\square\)

One may componentize \(J\) by overlap of the affected middle-index intervals
\([p-3,p]\cap[0,W-1]\).  If \(\Sigma_C\) denotes (10.39) restricted to one
such component, then

\[
                         \Sigma(J,P')=\sum_C\Sigma_C.
\tag{10.42}
\]

Separated multi-state components can therefore have nonzero signatures
which cancel globally; the isolated replacement DAG says nothing about
those new signatures.

For pairwise separated isolated UNIT edits, (10.39) reduces to the sum of
the replacement-graph arc boundaries, and Theorem 10.7 says its kernel is
zero.  Therefore any nonempty exact repair assembled from the audited flat
UNIT one-state edits must leave that linear regime: some controller
supports overlap, some local packet changes several states jointly, or the
middle chronology is globally reordered.  A boundary edit, a UNIT type
outside the audited Hall atlas, or a non-UNIT move is instead outside
Theorem 10.7.  In the interacting regime the edits must be selected as one
closed interaction satisfying (10.40), followed by the residence, all-depth
shadow, Hall-current, and common-word/controller tests of Sections
10.4--10.7.  The ten displayed witness pins with no isolated flat edit
already force such interaction.

### 10.9 The first target-safe two-state export and the exact
position-conflict two-commodity gate

The isolated Hall-service edit of Theorem 10.7 always deletes another
coordinate required by its advertised target.  The first surviving
mechanism in the **restricted flat UNIT census** uses two nearby controller
changes simultaneously.  That census considers pairs of distinct
theoretical flat UNIT-state edits of gap at most seven, with at least one
Hall-service UNIT demand.  Among 1,011,150 raw choices, 27,838 pass every
listed local controller, middle-rank, middle-adjacency, and maximal-erosion
test.  None is locally deck-closed.  Exactly 59 additionally retain at
least one advertised Hall-target envelope.  These counts make no claim
about non-UNIT or larger controller mechanisms.

Only three of those 59 have both exported deck arcs individually routable
through the ambient UNIT replacement graph, allowing direct or crossed
pairing at the level of unconstrained reachability:

\[
\begin{array}{c|c|c}
\text{controller edits }(p,x,y)&\text{exported deck arcs}&
 \text{advertised surviving rank-five value}\\ \hline
(3151,12,13),(3152,11,13)&3148\to685,\ 3149\to4452&6308\\
(3266,12,6),(3267,11,6)&3263\to3120,\ 3264\to3121&6308\\
(3268,2,6),(3269,12,6)&3268\to2236,\ 3269\to2237&6308.
\end{array}
\tag{10.43}
\]

In each row the indicated edited singleton controller letter is literally
the mask \(6308\), so the maximal local word realizes that one rank-five
value.  Thus the three rows are alternatives, not three additive Hall
gains.  Each row exports a two-arc deck imbalance.  It proves neither exact
deck closure nor compatibility with the other selected cells in one common
physical word.

Let \({\cal G}_{\rm amb}=(V,E)\) be the directed multigraph of all 10,370
locally admissible ambient isolated-UNIT operations.  An edge
\(e\in E\) carries:

* a deck arc \(s(e)\to d(e)\);
* its controller position \(\rho(e)\);
* its actual coordinate exchange; and
* its certified local support.

In the separated model, for **distinct** auxiliary edges declare \(e\# f\)
when

\[
                         |\rho(e)-\rho(f)|\le7,
\tag{10.44}
\]

and declare \(e\# B\) when \(\rho(e)\) is within seven of either controller
position of the chosen atomic two-state block \(B\).  More generally,
\(\#\) may be replaced by the exact overlap relation of the two certified
local supports.  Write the two exported block arcs as

\[
                         \beta_i:a_i\longrightarrow b_i,
 \qquad i=1,2.
\tag{10.45}
\]

#### Theorem 10.9 (position-conflict two-commodity closure)

Fix one block \(B\) in (10.43), and assume its four deck ports are distinct.
There is an exact middle-deck closure of \(B\) by separated isolated ambient
UNIT operations if and only if there is a set \(F\subseteq E\) satisfying:

1. no edge of \(F\) conflicts with \(B\);
2. the edges of \(F\) are pairwise nonconflicting; and
3. in the directed graph

   \[
                         F\cup\{\beta_1,\beta_2\},
   \]

   every deck vertex \(v\) satisfies

   \[
             \deg^-(v)=\deg^+(v)\in\{0,1\}.
   \tag{10.46}
   \]

Equivalently, for one permutation \(\pi\in{\mathfrak S}_2\), there are two
internally vertex-disjoint directed paths

\[
 b_i\leadsto a_{\pi(i)}
 \qquad(i=1,2),
\tag{10.47}
\]

whose operation sets are mutually position-compatible, compatible with
\(B\), and whose internal vertices avoid all four block ports.  The identity
pairing is the direct closure; the transposition is the crossed closure.

#### Proof

An ambient edge \(e\) has deck signature

\[
                         [T_{d(e)}]-[T_{s(e)}],
\]

while the block signature is

\[
 \Sigma_B=[T_{b_1}]+[T_{b_2}]
          -[T_{a_1}]-[T_{a_2}].
\tag{10.48}
\]

Condition (10.46) is exactly zero coefficient at every deck state, together
with the capacity-one requirement forced by the fact that every old and new
deck state occurs once.  A finite directed graph satisfying (10.46) is a
vertex-disjoint union of directed cycles.  Delete the two marked block arcs.
If they lie on different cycles, the two remainders give the direct paths;
if they lie on the same cycle, they give the crossed paths.  Cycles
containing neither marked arc may be discarded.  Conflict-freeness is
preserved under deletion.

Conversely, adjoining either path pair (10.47) to the two marked block arcs
forms one or two vertex-disjoint directed cycles, so the total signature is
zero and (10.46) holds.  Position compatibility makes the certified
local predicates in the ambient edge catalogue compose independently with
one another and with the atomic block.  It does not certify a predicate
whose dependency collar was omitted from the conflict relation.  \(\square\)

For reference, the two path-pair instances are:

\[
\begin{array}{c|c|c}
&\text{direct}&\text{crossed}\\ \hline
B_1&
685\leadsto3148,\ 4452\leadsto3149&
685\leadsto3149,\ 4452\leadsto3148\\
B_2&
3120\leadsto3263,\ 3121\leadsto3264&
3120\leadsto3264,\ 3121\leadsto3263\\
B_3&
2236\leadsto3268,\ 2237\leadsto3269&
2236\leadsto3269,\ 2237\leadsto3268.
\end{array}
\tag{10.49}
\]

An equivalent exact \(0\)-\(1\) formulation fixes one pairing \(\pi\), uses
variables \(f^i_e\in\{0,1\}\), and imposes

\[
 \sum_{e\in\delta^+(v)}f^i_e
 -
 \sum_{e\in\delta^-(v)}f^i_e
 =
 {\bf1}_{v=b_i}-{\bf1}_{v=a_{\pi(i)}}.
\tag{10.50}
\]

Put \(u_e=f^1_e+f^2_e\).  In addition to \(u_e\le1\), impose the
deck-vertex capacities

\[
 \sum_{i=1}^{2}\sum_{e\in\delta^+(v)}f^i_e
 +\#\{j:a_j=v\}\le1,
\qquad
 \sum_{i=1}^{2}\sum_{e\in\delta^-(v)}f^i_e
 +\#\{j:b_j=v\}\le1
\tag{10.51}
\]

for every \(v\), together with

\[
 u_e+u_f\le1\quad(e\ne f,\ e\# f),
 \qquad
 u_e=0\quad(e\# B).
\tag{10.52}
\]

For deck-only feasibility, any extraneous zero-divergence cycles can be
removed.  Thus (10.50)--(10.52) are an exact position-conflict
two-commodity formulation of (10.46)--(10.47).

The finite reachability screen behind (10.43) checks only that the endpoint
pairs in (10.49) are separately reachable for at least one pairing.  It
does not impose the deck-vertex capacities (10.51) or the conflict
inequalities (10.52).  The currently shortest closing
paths collide near the local block or with one another.  This rejects those
particular paths only; it is not a cut certificate against longer paths,
the other pairing, or an interacting auxiliary block.

Deck closure is still not the complete Shadow--Braid.  Give every auxiliary
edge and \(B\) their exact adjacent lower/upper signed shadow vector
\(\omega\).  Exact preservation of both adjacent-shadow multisets requires

\[
                         \omega(B)+\sum_{e\in F}\omega(e)=0.
\tag{10.53}
\]

This additive equation is valid when \(\omega\) contains every affected
adjacent colour and the conflict supports separate their full colour
collars.  Otherwise the combined shadow signature must be recomputed in
context.  Auxiliary deck cycles which were removable for deck-only
feasibility may be needed to satisfy (10.53) or another signed resource.
For support rather than multiset preservation, replace (10.53) by the exact
one-sided last-witness inequalities

\[
                    \mu_{\rm old}(c)+\Delta(c)\ge1
\]

for every required colour \(c\).  The composed controller must then pass:

1. all controller-rank, maximal-erosion, Johnson-adjacency, and residence
   tests;
2. every deeper lower/upper shadow ledger;
3. the full Hall current, including all 1,489 retained pairs and the other
   residual targets; and
4. the one-common-word and trace-two conditions of Theorem 10.6.

The local certificate in (10.43) guarantees the displayed singleton value
\(6308\) before compensation.  It makes no uniqueness claim about other
locally surviving envelopes.  A successful conflict-free closure must
retain the advertised occurrence in the final common word.

Finally, the adjacent support of a block in (10.43) has only the necessary
two-mask cardinality to model the mutable erosion masks at one clean-C6
seam.  No row of (10.43) has yet been embedded in a realized clean C6.  Such
an embedding would have to identify its two edits literally with
\(Q^-_{i,2},Q^-_{i,3}\mapsto Q^+_{i,2},Q^+_{i,3}\) under one actual segment
transport.  It would additionally need the common seven-set
\(\Lambda_i\), the fixed first crossing mask, the other two C6 seams,
cyclic upper-shadow transport, and all nine residence tests at every seam.
Those other seam pairs might close the exported commodities themselves;
isolated ambient paths are only one possible compensation mechanism.

### 10.10 The three named blocks do not embed in one frozen clean C6

We now test the preceding possibility against the actual frozen chronology,
not merely against ambient reachability.  Let \(T^{(j)}\) be the middle
chronology obtained from the isolated two-state block \(B_j\) in (10.43),
before any auxiliary compensation.  Its two changed deck values are

\[
\begin{array}{c|c}
B_1&T_{3148}\mapsto T_{685},\quad T_{3149}\mapsto T_{4452}\\
B_2&T_{3263}\mapsto T_{3120},\quad T_{3264}\mapsto T_{3121}\\
B_3&T_{3268}\mapsto T_{2236},\quad T_{3269}\mapsto T_{2237}.
\end{array}
\tag{10.54}
\]

Here and below an edge of the frozen linear factor means an unordered pair
\(T_rT_s\) with \(|r-s|=1\).  None of the states used below is an endpoint,
so adding a cyclic endpoint edge would not change the test.

#### Lemma 10.10 (unique possible boundary clean seam in each block)

Among the three changed adjacent transitions of each \(B_j\), exactly one
has its lower colour fixed.  The three possibilities, oriented so that the
unchanged middle owner is \(X\), are

\[
\begin{array}{c|c|c|c|c|c}
 &\text{slot}&X&Y^-&Y^+&\Lambda=X\cap Y^-=X\cap Y^+\\ \hline
B_1&3147&T_{3147}&T_{3148}&T_{685}&\{0,2,3,4,5,7,10\}\\
B_2&3262&T_{3262}&T_{3263}&T_{3120}&\{1,2,3,5,7,8,9\}\\
B_3&3269&T_{3270}&T_{3269}&T_{2237}&\{0,3,4,5,7,10,11\}.
\end{array}
\tag{10.55}
\]

Moreover \(X\cap Y^+=Y^-\cap Y^+=\Lambda\) in every row.  Thus each row
passes the one-seam ambient clean-C6 **edge** algebra, but there is no second
possible boundary anchor transition inside that atomic block.

#### Proof

Literal intersections at the other two changed slots are

\[
\begin{array}{c|c|c}
 &\text{old lower colours}&\text{new lower colours}\\ \hline
B_1&
\{2,3,4,5,7,10,13\},\ \{2,3,4,5,7,12,13\}&
\{2,3,4,5,7,10,12\},\ \{2,3,4,5,7,11,12\}\\
B_2&
\{1,2,3,5,6,7,8\},\ \{1,2,3,5,6,7,12\}&
\{1,2,3,5,7,8,12\},\ \{1,2,3,5,7,11,12\}\\
B_3&
\{0,5,6,7,10,11,12\},\ \{0,4,5,6,7,10,11\}&
\{0,2,5,7,10,11,12\},\ \{0,4,5,7,10,11,12\}.
\end{array}
\tag{10.56}
\]

No old entry in (10.56) equals its corresponding new entry.  At the one
remaining changed slot, direct intersection gives (10.55), and intersecting
\(Y^-\) with \(Y^+\) gives the same seven-set.  Proposition 10.1 says that
every clean-C6 seam fixes its lower colour pointwise, proving uniqueness.
\(\square\)

The local algebra makes the remaining clean-C6 test especially small.  In
one row of (10.55), write

\[
 X=\Lambda+c,\qquad Y^-=\Lambda+a_1,\qquad
 Y^+=\Lambda+a_0.
\tag{10.57}
\]

The triples \((a_0,a_1,c)\) for \(B_1,B_2,B_3\) are respectively

\[
                     (12,13,8),\qquad(12,6,10),\qquad(12,6,13).
\tag{10.58}
\]

Every clean-C6 completion is obtained by choosing the distinguished
\(a_2\in\Lambda\), putting \(D=\Lambda-\{a_2\}\), and using the companion
old edge

\[
              X_1Y_1=(D+\{a_0,c\})(\Lambda+\{a_0\}),
              \qquad Y_1=Y^+.
\tag{10.59}
\]

This is not only necessary: together with the second companion edge from
(10.2), it is the complete seven-choice parametrization of clean-C6
extensions of the rooted old/new seam.

#### Theorem 10.11 (frozen clean-C6 embedding obstruction)

No block \(B_1,B_2,B_3\) in (10.43) is the collar of a clean C6 in the
frozen Hall-29 middle factor, under the fixed-address/canonical-retained-
segment identification.

#### Proof

Let \({\rm pos}(S)\) be the unique index of the rank-eight deck state \(S\)
in the frozen middle path.  For all seven choices in (10.59), the exact
positions of \(X_1\) are

\[
\begin{array}{c|c|c|c}
 &a_2\text{ in the displayed order}&{\rm pos}(X_1)&{\rm pos}(Y_1)\\ \hline
B_1&(0,2,3,4,5,7,10)&
(2725,1452,1451,4455,5428,2724,4454)&685\\
B_2&(1,2,3,5,7,8,9)&
(1573,1072,2202,5531,1574,5677,4366)&3120\\
B_3&(0,3,4,5,7,10,11)&
(711,6420,3718,4127,361,712,1453)&2237.
\end{array}
\tag{10.60}
\]

No entry in the third column differs by one from the corresponding fixed
entry in the fourth column.  Hence none of the required companion old edges
\(X_1Y_1\) occurs in the frozen factor.  Lemma 10.10 leaves no other anchor
transition, so no clean C6 contains the block.  Reversing a retained segment
does not help, because the edge test is unordered.  \(\square\)

This is a statewise obstruction for the frozen physical address system.  A
global reindexing which moves the retained cells is outside it and must
rebuild the peeled Hall architecture and the common-word certificate.

There is a distinct controller-mask interpretation which must not be
conflated with the boundary-edge test.  If the two edited masks are aligned
formally with the two mutable crossing masks of Section 10.2, the three
possible old seam orientations are

\[
\begin{array}{c|c|c|c}
 &\text{oriented old seam}&\Lambda&\text{fixed first crossing mask}\\ \hline
B_1&T_{3151}\to T_{3150}&\{2,3,5,7,11,12,13\}&P_{3153}\\
B_2&T_{3266}\to T_{3265}&\{2,3,5,6,7,11,12\}&P_{3268}\\
B_3&T_{3266}\to T_{3267}&\{2,5,6,7,10,11,12\}&P_{3267}.
\end{array}
\tag{10.60a}
\]

In each row all four old/new edited masks lie in, and jointly fill, the
displayed \(\Lambda\).  Thus abstract two-mask containment passes.  But the
atomic block leaves the corresponding middle seam edge itself unchanged;
it supplies no new end owner \(Y^+\ne Y^-\).  Therefore (10.60a) is not a
clean-C6 embedding.  It confirms exactly why matching the two-mask arity
alone was insufficient: an explicit retained-segment transport is still
needed, and Theorem 10.11 rules out the literal boundary transport available
in the frozen chronology.

### 10.11 The nearest block compound is illegal

The three atomic deck signatures are

\[
\begin{aligned}
 \Sigma_1&=[T_{685}]+[T_{4452}]-[T_{3148}]-[T_{3149}],\\
 \Sigma_2&=[T_{3120}]+[T_{3121}]-[T_{3263}]-[T_{3264}],\\
 \Sigma_3&=[T_{2236}]+[T_{2237}]-[T_{3268}]-[T_{3269}].
\end{aligned}
\tag{10.61}
\]

There is a second, independent obstruction to the smallest non-clean
multi-seam completion.  Regard a middle transition \(AB\) as the flag cell

\[
                         (A\cap B,\ A\cup B)
\]

in the rank-seven/rank-nine incidence graph.

#### Proposition 10.11a (no two-transition shadow compensator)

Fix one atomic block \(B_j\) and its three changed transition slots.  There
is no completion using exactly two further old transition cells and two
further new transition cells which both

1. preserves the adjacent lower and upper multisets, and
2. is an exact middle-owner factor trade.

Indeed, even the row/column-balanced two-cell shore is not installed in the
frozen factor.

#### Proof

For each \(B_j\), after the one fixed lower colour and one fixed upper colour
cancel, the signed shadow margin has two distinct gained and two distinct
lost lower colours, and likewise at the upper rank.  A two-cell compensator
must therefore pair the two gained lower colours bijectively with the two
gained upper colours on its old shore, and pair the two lost lower colours
with the two lost upper colours on its new shore.  Of the two bijections on
each shore, the containment condition \(R\subset U\) leaves exactly one
combined choice.  Its lifted old and new Johnson edges are

\[
\begin{array}{c|c|c}
 &\text{required old auxiliary edges}&\text{required new auxiliary edges}\\
\hline
B_1&T_{685}T_{2725},\ T_{4453}T_{4452}&
    T_{3148}T_{5091},\ T_{4302}T_{3149}\\
B_2&T_{3120}T_{4366},\ T_{3121}T_{6279}&
    T_{3263}T_{5148},\ T_{3264}T_{5150}\\
B_3&T_{2327}T_{2236},\ T_{2237}T_{6420}&
    T_{5300}T_{3268},\ T_{3269}T_{6159}.
\end{array}
\tag{10.61a}
\]

In row \(B_1\), only the second old edge occurs in the frozen path, at slot
4452.  Neither old edge occurs in rows \(B_2,B_3\).  Thus no required old
two-cell shore is present.

There is also an intrinsic middle-degree failure independent of presence.
The atomic substitution replaces the three consecutive transition edges
around its two changed middle states.  Each changed state loses both old
incidences and gains both new incidences, so its middle-degree boundary is
\(2\Sigma_j\), not merely the one-copy deck signature (10.61).  Adding the
two-old/two-new auxiliary shore cancels one copy of each atomic port and
leaves, respectively, the nonzero boundaries

\[
\begin{array}{c|l}
B_1&
[T_{685}]+[T_{4452}]+[T_{5091}]+[T_{4302}]
-[T_{3148}]-[T_{3149}]-[T_{2725}]-[T_{4453}]\\
B_2&
[T_{3120}]+[T_{3121}]+[T_{5148}]+[T_{5150}]
-[T_{3263}]-[T_{3264}]-[T_{4366}]-[T_{6279}]\\
B_3&
[T_{2236}]+[T_{2237}]+[T_{5300}]+[T_{6159}]
-[T_{3268}]-[T_{3269}]-[T_{2327}]-[T_{6420}].
\end{array}
\tag{10.61b}
\]

All eight terms in each row are distinct, so no boundary vanishes.  This
proves both assertions.  \(\square\)

Thus the smallest possible row/column repair of an atomic block already
fails before residence or the common word is considered.  This result is
scoped to two further transition replacements; a larger non-clean
alternating flag circuit is not excluded.

All twelve displayed deck states are distinct.  Thus the separated pairs
\(B_1+B_2\) and \(B_1+B_3\) have nonzero deck signature.  The tempting
nearby overlay \(B_2+B_3\) is worse: applying its four advertised controller
edits simultaneously gives

\[
 P'_{3267}=P'_{3268}=\{2,5,7,11,12\},
\tag{10.62}
\]

so the equal-rank controller step has Hamming distance zero rather than two.
The reconstructed middle owners \(T'_{3265},T'_{3266},T'_{3267}\) all have
rank seven rather than eight.  Consequently the simultaneous overlay is not
a controller path or a middle Johnson path.

There is also a clean-C6 obstruction before any companion-edge search.
The two formal mask seams in (10.60a) share \(X=T_{3266}\), but their
departing coordinates are respectively \(c=10\) and \(c=3\).  More
invariantly,

\[
 \Lambda_2\cap\Lambda_3=\{2,5,6,7,11,12\}=:D,
 \qquad X=D\cup\{3,10\},
\]

so the two seams force different members of \(X-D\) to play the one common
clean-C6 coordinate \(c\).  They therefore cannot be two seams of the same
clean C6.

In particular, no nonempty compound made only from the three named blocks
is an exact braid: singletons
and the two separated pairs have nonzero deck boundary, while every subset
containing both \(B_2,B_3\) fails local legality.

There is also no route which appends separately exact clean C6 packets to one
atomic block.  Every clean C6 has zero middle-deck signature, so any such
sum still has signature \(\Sigma_j\ne0\).  The only way that “the other C6
seams” could close the two exports was for the atomic collar to be part of
that same clean C6; Theorem 10.11 rules out precisely this possibility.
Thus every remaining deck closure must use a genuinely non-clean auxiliary
component with signed deck boundary \(-\Sigma_j\).

### 10.12 An exact resident interacting closure exists, but its shadow
boundary is nonzero

The all-path separated no-go is not an unrestricted no-go.  The exact
certificate in

```text
THREAD_H_K15_POSITION_CONFLICT_TWO_COMMODITY_CIRCULATION_20260728.md
```

adds eighteen specified auxiliary UNIT edits to \(B_1\).  Simultaneous
recomputation produces the single deck cycle

\[
\begin{aligned}
3148&\to685\to3149\to4452\to4726\to5100\to5738\to461
\to3153\to2792\\
&\to4096\to901\to6079\to4710\to3170\to4359\to1429
\to2095\to3196\to686\to3148.
\end{aligned}
\tag{10.63}
\]

It therefore preserves the middle deck exactly.  The same literal audit
proves every middle and controller rank, both Johnson chronologies, maximal
erosion, and \(P'_{3152}=6308\).  Hence \(A=P'\) is one common nonempty word
with \(D^3A=T'\) and realizes the advertised singleton value.  The following
additional fact was not needed for the deck theorem.

#### Proposition 10.12 (the 20-state closure preserves depth-three residence)

Write \(T'_{i+1}=T'_i-\alpha'_i+\beta'_i\).  Then

\[
             \beta'_i\ne\alpha'_{i+t}
             \qquad(1\le t\le3)
\tag{10.64}
\]

for every valid \(i\).  Thus the exact interacting closure (10.63) is
depth-three resident.

#### Proof

The frozen chronology already satisfies (10.64).  Only the following 38
transition labels change; each entry is \(i:(\alpha'_i,\beta'_i)\):

\[
\begin{array}{r|c@{\qquad}r|c@{\qquad}r|c}
460&(3,4)&461&(6,2)&684&(9,13)\\
685&(12,0)&686&(3,11)&900&(7,13)\\
901&(12,1)&1428&(10,7)&1429&(0,14)\\
2094&(9,4)&2095&(10,14)&2791&(0,3)\\
2792&(6,5)&3147&(8,12)&3148&(0,11)\\
3149&(10,13)&3152&(2,14)&3153&(12,4)\\
3169&(6,4)&3170&(5,8)&3195&(8,4)\\
3196&(2,14)&4095&(12,6)&4096&(4,1)\\
4358&(11,0)&4359&(8,10)&4451&(10,2)\\
4452&(9,0)&4709&(7,13)&4710&(6,3)\\
4725&(2,11)&4726&(8,6)&5099&(2,13)\\
5100&(12,7)&5737&(8,4)&5738&(7,0)\\
6078&(13,4)&6079&(0,5)&&
\end{array}
\tag{10.65}
\]

For every listed \(i\), direct substitution in the frozen neighbouring
labels gives

\[
 \alpha'_i\notin\{\beta'_{i-1},\beta'_{i-2},\beta'_{i-3}\},
 \qquad
 \beta'_i\notin\{\alpha'_{i+1},\alpha'_{i+2},\alpha'_{i+3}\}.
\tag{10.66}
\]

Any new violation of (10.64) would have a changed label at its left or right
endpoint, hence would contradict (10.66).  Pairs whose two endpoint labels
are unchanged retain the old residence inequality.  \(\square\)

The circuit nevertheless fails the requested Shadow--Braid condition.  Its
new immediate lower and upper supports are strict subsets of the old ones.
The missing lower colours are

\[
\begin{split}
\{&3000,4796,5301,7352,10992,12476,13217,15144,19160,23065,\\
  &31280,31297,31304,31392\},
\end{split}
\tag{10.67}
\]

and the missing upper colours are

\[
                         \{9661,23257,31457\}.
\tag{10.68}
\]

In particular, even support is not preserved, so the stronger multiset
identity fails.  This gives two rigorous consequences.

1. Composing (10.63) with any number of clean C6 trades cannot repair it.
   Every clean C6 has zero exact adjacent lower/upper multiset boundary by
   Proposition 10.1, so the nonzero boundary (10.67)--(10.68) remains.
2. Any non-clean shadow repair of this particular circuit must introduce at
   least fourteen further transition occurrences: one transition has only
   one rank-seven lower colour, while the fourteen colours in (10.67) are
   all absent from the current support.

Thus there is an explicit exact, literal, depth-three-resident interacting
deck closure of \(B_1\), but there is **no** requested complete
Shadow--Braid certificate.  The obstruction is no longer abstract
reachability: all three one-C6 embeddings fail the seven-choice companion-
edge test, the only adjacent named-block overlay is locally illegal, and the
known 20-state closure has the exact nonzero shadow boundary
(10.67)--(10.68).  A positive construction must contain a genuinely
non-clean compensating component with the opposite signed shadow vector;
clean C6 seams alone can never supply it.  Deeper flags, the 1,489 retained
physical occurrences, trace two, and the final Hall matching remain later
gates even after such a compensation is found.
