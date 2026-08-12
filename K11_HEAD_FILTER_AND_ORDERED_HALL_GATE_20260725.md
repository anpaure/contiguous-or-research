# The corrected K=11 head filter and ordered-Hall completion gate

Date: 2026-07-25

## 1. Outcome

Let

\[
 \mathcal H'=(\mathcal H_{\rm old}\setminus\{127(10)\})
              \cup\{347(10)\}.
\]

The corrected backward-tail calculation is now closed: the forty-two row
degrees have maximum ten, so the hole--tail graph has a matching of size at
least twenty-three.  This note starts after that result.

It proves four further facts.

1. The corrected splice (B3\to D3) is not merely a lower repair.  With
   the correct head orientation it simultaneously creates the two missing
   colours
   \[
      347(10),\qquad1269.
   \]
   Reflection supplies a second, group-disjoint simultaneous repair
   (A7\to A11), creating (1478) and (259(10)).
2. The abstract disjointness graph of the thirty-two displayed holes has a
   perfect matching.  Thus the requirement that at least six seams repair
   both ledgers has no set-theoretic obstruction.
3. The seven-letter hole digraph and the exact two-orientation head rule,
   by themselves, cannot prove that even one backward witness survives.
   An explicit seven-vertex local model satisfies every one of those
   axioms and blocks all seven witnesses.  A positive head-survival theorem
   must therefore use a further correlation of the named canonical factor.
4. Once one port per wreath is fixed, global six-path completion has an
   exact Hall certificate.  Restricting arcs to a common order makes
   acyclicity automatic; a prescribed support-repair seed extends to the
   required thirty-six-arc forest exactly when a residual bipartite graph
   has Hall deficiency at most six.

No program, solver, or search is used.

## 2. Audited inputs and the completeness caveat

The A--E row audits prove that every member of \(\mathcal H'\) is absent.
They also prove that the internal-deletion incidence graph on this displayed
family has exactly

\[
 76+17+45+86=224=32\cdot7
\]

edges and right degree at most ten.  Hence Koenig's theorem gives a
backward-tail matching of size at least

\[
 \left\lceil\frac{224}{10}\right\rceil=23.
\tag{2.1}
\]

This exhausts the internal-deletion incidences belonging to
\(\mathcal H'\).  It does **not**, on its own, prove that no thirty-third
four-set is absent.  The equality

\[
 |\operatorname{supp}_4|=298
\tag{2.2}
\]

still depends on the separate 330-set union/multiplicity tally.  Every
statement below that uses the numerical support threshold 298 is therefore
conditional on (2.2); the local splice and Hall statements are not.

## 3. Exact simultaneous repair at the corrected seam

Use the displayed class-B row

\[
 B3=(0,2,1,6,5,9,4,3,8,7,10).
\]

Around index zero its last source and target are

\[
 W=(4,3,8,7,10),\qquad
 U=W\cup\{0\}.
\]

Delete the internal coordinate \(\beta=8\).  The forward-tail forbidden
pair is

\[
 (c,d)=(10,0),
\]

and the cross source is

\[
 H=U-8=\{0,3,4,7,10\}.
\]

The unique owner of (H) is the class-D row

\[
 D3=(0,4,5,2,1,9,8,6,7,3,10),
\]

where (H) occurs in the order

\[
 (7,3,10,0,4).
\]

Its first two forward deletion ports are (7,3).  They obey

\[
 7\notin\{10,0\},\qquad3\ne0,
\]

so the five exact seam inequalities hold.  The first insertion at the head
is \(\alpha=5\).  Consequently the two new colours are

\[
 B^*=W\cap H=\{3,4,7,10\},
\tag{3.1}
\]

and, since

\[
 D=[11]\setminus U=\{1,2,5,6,9\},
\]

\[
 Y^*=D-5=\{1,2,6,9\}.
\tag{3.2}
\]

Both (3.1) and (3.2) belong to \(\mathcal H'\).  Thus this is a complete
physical double-repair arc, not only a backward-tail witness.

Let

\[
 \sigma(0)=0,\qquad \sigma(x)=11-x\quad(1\le x\le10).
\]

The canonical factor is invariant under \(\sigma\), with the represented
coordinate order reversed.  Applying this symmetry to the preceding arc
gives a physical arc from row (A7) to row (A11), using the corresponding
reverse displayed port orientations, and creating

\[
 \sigma(347(10))=1478,
 \qquad
 \sigma(1269)=259(10).
\tag{3.3}
\]

The four row groups (B3,D3,A7,A11) are distinct.  Hence (3.1)--(3.3)
form a two-arc directed matching and may be included simultaneously in a
transversal port forest.

## 4. No abstract disjoint-hole obstruction

Every seam which repairs both ledgers produces two disjoint four-sets.
The converse is not automatic, because the ports still have to realize the
pair.  Nevertheless, the disjointness graph on \(\mathcal H'\) itself is
as nondeficient as possible: the following is a perfect matching.

\[
\begin{array}{c|c@{\qquad}c|c}
0147&2369&0169&247(10)\\
0237&1459&0247&158(10)\\
0256&1478&0257&1469\\
0258&1479&025(10)&1369\\
0347&1269&0369&258(10)\\
0469&257(10)&0478&259(10)\\
0479&136(10)&047(10)&2589\\
0489&267(10)&0569&347(10).
\end{array}
\tag{4.1}
\]

Each row of (4.1) is visibly a disjoint pair, and every displayed hole
occurs once.  In particular the forced lower bound of six simultaneous
repairs cannot fail merely because the two thirty-two-colour ledgers lack
enough disjoint pairs.  The obstruction, if any, is in cyclic realization
and common-port compatibility.

## 5. Exact paired-hole realization test

The preceding distinction can be made finite and exact.  Let (C,Y\in
\mathcal H'\) be disjoint and put

\[
 R=[11]\setminus(C\cup Y),\qquad |R|=3.
\]

Choose an ordering

\[
 R=(\beta,t,\alpha).
\tag{5.1}
\]

Define

\[
 W=C\cup\{\beta\},\quad
 H=C\cup\{t\},\quad
 U=C\cup\{\beta,t\},\quad
 D=Y\cup\{\alpha\}=[11]\setminus U.
\tag{5.2}
\]

### Proposition 5.1 (six-assignment criterion)

There is a canonical physical seam with new colours ((C,Y)) and seam
letters ((\beta,t,\alpha)) if and only if all of the following hold.

1. In the unique owner order of (W), the coordinate (\beta) is internal
   and (t) is the exterior neighbour selected by its unique backward-safe
   tail orientation.
2. In the unique owner order of (H), the coordinate (\alpha) is the
   exterior neighbour selected by one of the two head orientations.
3. For those two oriented windows, the ordered forbidden pair at the tail
   avoids the first two deletion ports at the head according to the exact
   five seam inequalities.
4. The owners of (W) and (H) are different.

There are only six choices in (5.1).

#### Proof

For a seam with new lower colour (C), its last old source and cross source
have the form (W=C+\beta) and (H=C+t).  Their common target is
(U=C+\beta+t).  Its complementary five-set is (D), and deleting the
first head insertion (\alpha) gives the new complementary-upper colour

\[
 D-\alpha=Y.
\]

This proves necessity of (5.1)--(5.2) and items 1--4.  Conversely, items
1--2 give the required tail target, cross source, and first head target;
item 3 is precisely the necessary-and-sufficient local splice theorem;
item 4 excludes the degenerate old-edge case.  The two new-colour formulas
then give (C,Y).  \(\square\)

Thus the physically realizable double-repair graph is obtained from the
large abstract graph (4.1) by six literal owner-window checks per pair.
Equations (3.1)--(3.3) certify two of its edges.

### Proposition 5.2 (directed two-path form)

Fix a lower hole \(C\), put \(X=[11]\setminus C\), and use its
seven-letter digraph

\[
 x\longrightarrow e_-(x),e_+(x).
\]

A simultaneous lower/upper repair is exactly a directed two-path

\[
 \beta\longrightarrow t\longrightarrow\alpha
\tag{5.3}
\]

whose first arc is backward-safe, whose second arc is the chosen legal
head orientation, and for which

\[
 Y=X\setminus\{\beta,t,\alpha\}\in\mathcal H'.
\tag{5.4}
\]

The full seven-letter digraph has exactly twenty-eight directed two-paths.
If \(m_C\) of the seven letters occupy internal position two in their owner
windows, then exactly

\[
 14+2m_C
\tag{5.5}
\]

of those paths have a backward-safe first arc, before the head test.

#### Proof

The first arc in (5.3) says that the tail six-set is
\(C+\beta+t\).  At the cross head \(C+t\), its two old outgoing target
choices insert precisely \(e_-(t)\) and \(e_+(t)\); choosing one of them is
the second arc \(t\to\alpha\).  Its complementary upper colour is (5.4).
This is Proposition 5.1 in the seven-letter notation.

There are fourteen directed first arcs and two continuations from the head
of each.  No continuation returns to \(\beta\), because a return would be a
reciprocal pair, so all are genuine three-letter paths.  Finally, a
position-one or position-three tail letter has one safe first arc, while a
position-two letter has two.  The number of safe first arcs is therefore
\(7+m_C\), and each has two continuations.  \(\square\)

The corrected position-two columns give

\[
 \#\{C:m_C=1,2,3,4,5\}=(4,12,12,2,2),
\tag{5.6}
\]

so

\[
 \sum_Cm_C=82,\qquad
 \sum_C(14+2m_C)=612.
\tag{5.7}
\]

Equations (5.3)--(5.7) are a substantially smaller coupled audit object
than the 924-port graph: the search for the four still-missing certified
double repairs may be performed inside thirty-two labelled
seven-vertex digraphs.  They do not by themselves force an upper hole;
condition (5.4) is the remaining named-factor correlation.

## 6. Why the seven-letter local axioms cannot close the head filter

The exact hole-digraph theorem associates to one hole (C) a directed
simple graph on the seven letters outside (C), with outdegree two and no
reciprocal pair.  A letter in internal position one has one backward-safe
outarc; a letter in position two has two; a letter in position three has
one.  An arc entering a position-two letter always survives, while an arc
entering positions one or three can be double-blocked by one prescribed
endpoint of the head window.

These facts alone admit complete blockage.

### Proposition 6.1 (all-blocked local countermodel)

There is a seven-letter datum satisfying every preceding local axiom in
which all seven backward-tail incidences are double-blocked.

#### Proof

Write the seven outside letters as \(\mathbb Z_7\), and fix four distinct
symbols (a,b,c,d\) for (C).  Give every rank-five owner the ordered
window

\[
 W_x=(a,x,b,c,d).
\]

Thus every (x) has internal position one and its unique safe extension is
declared to be

\[
 x\longrightarrow x+1.
\]

Add the second, unsafe owner extension

\[
 x\longrightarrow x+3.
\]

The resulting digraph is simple, has outdegree two, and has no reciprocal
pair, since neither (-1) nor (-3) is in \(\{1,3\}\pmod7\).  The fourteen
unordered rank-six pairs are therefore distinct, exactly as required by
rank-six ownership.

Every safe arc has protected endpoint (d).  Its head (W_{x+1}) again
has type one and last endpoint (d).  This is exactly the double-block
pattern ((\operatorname{pos}(d),\operatorname{pos}(x+1))=(4,1)).
Hence all seven safe arcs fail both head orientations.  \(\square\)

This is not asserted to be a subconfiguration of the named MSW factor.  It
proves a sharp logical point: no argument using only left degree seven,
absence of reciprocal rank-six pairs, and the position-one/two/three head
rule can establish a 21-matching after the head filter.  One must use an
additional named-factor correlation (or perform the finite owner-window
audit encoded by Proposition 5.1).

## 7. Ordered Hall completion after ports are fixed

Let \(\mathcal C\) be the forty-two wreath groups and let
\(\mathfrak P\) be the exact physical port graph.  A **port transversal**
is a choice (p(Q)) of one oriented cut port over every (Q\in\mathcal C).
Fix also a total order \(\prec\) on \(\mathcal C\).  Form the bipartite
graph

\[
 \Gamma^+(p,\prec)
\]

with a left and a right copy of \(\mathcal C\), placing an edge
(Q_LQ'_R) exactly when

\[
 p(Q)\longrightarrow p(Q')
\]

is a physical port arc and (Q\prec Q').

### Theorem 7.1 (ordered Hall path-cover lemma)

Let (R\) be a matching of (s\) prescribed edges of
\(\Gamma^+(p,\prec)\).  Delete from the left side the (s\) tails used by
(R\), and from the right side the (s\) heads used by (R\), obtaining
(\Gamma_R\).  Then (R\) extends to a thirty-six-arc transversal directed
linear forest if and only if

\[
 \boxed{|N_{\Gamma_R}(X)|\ge |X|-6
        \quad\hbox{for every }X\subseteq L(\Gamma_R).}
\tag{7.1}
\]

The resulting forest has exactly six directed path components.

#### Proof

The two residual sides have (42-s\) vertices.  By the deficiency form of
Hall's theorem, (7.1) is equivalent to a residual matching of size at least

\[
 (42-s)-6=36-s.
\]

Together with (R\), choose exactly thirty-six edges.  Matching means that
every group has indegree and outdegree at most one.  All arcs point forward
in the same strict order, so there is no directed cycle.  Under the degree
bounds, an undirected cycle would have one incoming and one outgoing arc at
every vertex and hence would itself be a directed cycle.  Thus the selected
arcs form an undirected forest.  It has forty-two vertices and thirty-six
edges, hence six components, each a directed path or an isolated vertex.

Conversely, any extension inside the forward graph leaves a residual
matching of size (36-s\), and Hall deficiency is at most six.  \(\square\)

### Corollary 7.2 (support-seed separation)

For the fixed transversal \(p\), let
\(\widehat L_B(p),\widehat L_Y(p)\) be the numbers of old supported
colours all of whose occurrences are among the forty-two cuts, before
allowing any seam to restore such a colour.  Suppose the prescribed seed
\(R\) creates at least

\[
 319-\sigma_B+\widehat L_B(p)
 \quad\hbox{and}\quad
 319-\sigma_Y+\widehat L_Y(p)
\tag{7.2}
\]

distinct initially missing colours in the two ledgers.  If (7.1) holds,
then the completed forest has support at least 319 in both ledgers.

#### Proof

The raw cut-extinction numbers are already determined by the transversal
\(p\), not by which outgoing port arcs are selected.  A seam which restores
one of these old colours only improves the bound.  The residual matching
can likewise only add seam colours; it cannot undo a gain made by \(R\).
Equation (7.2) and the exact replacement ledger therefore give the
assertion.  \(\square\)

When (2.2) holds, (7.2) becomes
\(21+\widehat L_B(p)\) and \(21+\widehat L_Y(p)\).

## 8. Sharply isolated remaining certificate

The backward Hall theorem supplies twenty-three lower colours on distinct
tail rows, but Proposition 6.1 proves that this fact cannot be pushed
through the head filter using the presently recorded local degree axioms.
The exact finite certificate which would establish the canonical
length-465 construction is now:

1. a port transversal (p\) and a total row order \(\prec\);
2. a forward seed matching \(R\) satisfying both inequalities (7.2), hence
   containing at least
   \(6+\widehat L_B(p)+\widehat L_Y(p)\) double-repair arcs;
3. the residual Hall inequalities (7.1).

The two arcs in Section 3 give a certified group-disjoint double-repair
seed of size two.  Four more simultaneous repairs are necessary even in
the zero-loss case.  Producing those four and proving the residual
deficiency-six inequalities are the smallest currently unclosed
canonical-splice tasks.  Abstract hole disjointness, backward-tail Hall,
and local head orientation are no longer the missing statements.
