# Union-rainbow cycle deletion reduces the first exterior rethread to two matroids

**Date:** 2026-08-07  
**Method:** complementation, Kruskal--Katona, and Edmonds matroid intersection  
**Status:** unconditional exact reduction.  A union-rainbow Hamilton cycle
exists in every dimension.  Conditional only on making its intersection
palette surjective, the remaining palette-safe endpoint deletion is one
explicit common-basis problem for a partition matroid and a transversal
matroid.  This note does not prove that common-basis inequality, the exterior
forest, residence, or deeper upper coverage.

## 1. The adjacent-layer cycle

Let \(|\Omega|=2m\), and put

\[
 \mathcal A={\Omega\choose m-2},\qquad
 \mathcal B={\Omega\choose m-1},\qquad
 \mathcal U={\Omega\choose m}.
\]

Write

\[
 W=|\mathcal U|={2m\choose m},\qquad
 C=\operatorname {Cat}_m={W\over m+1},\qquad
 V=|\mathcal B|=mC.
\]

For an edge \(e=XY\) of the Johnson graph on \(\mathcal B\), define

\[
 i(e)=X\cap Y\in\mathcal A,\qquad
 q(e)=X\cup Y\in\mathcal U.                         \tag{1.1}
\]

Call a Hamilton cycle \(K\) on \(\mathcal B\)
**union-rainbow** when \(q:E(K)\to\mathcal U\) is injective.  Such a cycle
exists for every \(m\ge2\): take an optimal alternating cycle in the two
consecutive Boolean levels \(\mathcal B\leftrightarrow\mathcal U\) which
contains every member of the smaller shore \(\mathcal B\), as supplied by
the Gregor--Micka--Mutze central-levels theorem, and suppress its
\(\mathcal U\)-vertices.  The visited \(\mathcal U\)-vertices are distinct,
so the suppressed edge unions are distinct.

Let

\[
 Q=q(E(K)),\qquad \mathcal O=\mathcal U\setminus Q.
\]

Then

\[
 |Q|=V=mC,\qquad |\mathcal O|=W-V=C.                \tag{1.2}
\]

The additional property needed below is

\[
 \{i(e):e\in E(K)\}=\mathcal A.                    \tag{1.3}
\]

It is not asserted that the published optimal cycle automatically has
(1.3).  Equation (1.3) is the remaining coloured-cycle row.

## 2. Palette-safe deletions

Assume (1.3).  For \(a\in\mathcal A\), put

\[
 E_a=\{e\in E(K):i(e)=a\},\qquad \mu_a=|E_a|\ge1.
\]

A set \(D\subseteq E(K)\) is **intersection-safe** when

\[
 |D\cap E_a|\le \mu_a-1\qquad(a\in\mathcal A).     \tag{2.1}
\]

Equivalently, deleting \(D\) leaves every intersection colour represented.
The safe sets are the independent sets of the partition matroid

\[
 \mathsf M_{\rm safe}
   =\bigoplus_{a\in\mathcal A}U_{\mu_a-1,\mu_a}.    \tag{2.2}
\]

Its total rank is the exact repeat surplus

\[
 \begin{aligned}
 r(\mathsf M_{\rm safe})
 &=V-|\mathcal A|\\
 &= {3m\over m+2}C
 >C\qquad(m>1).                                    \tag{2.3}
 \end{aligned}
\]

Thus scalar deletion capacity is not the issue.

## 3. The endpoint transversal matroid

Make a bipartite graph \(R_K\) with left shore \(E(K)\), right shore
\(\mathcal O\), and

\[
 e=XY\sim U
 \quad\Longleftrightarrow\quad
 X\subset U\text{ or }Y\subset U.                 \tag{3.1}
\]

Let \(\mathsf M_{\rm end}\) be the transversal matroid on ground set
\(E(K)\) represented by \(R_K\).  A set \(D\) has rank \(|D|\) in this
matroid exactly when its edges can be assigned to distinct omitted
\(m\)-sets, each containing one chosen endpoint of the assigned edge.

### Lemma 3.1 (the endpoint matroid has full rank \(C\))

\[
 r(\mathsf M_{\rm end})=C.                          \tag{3.2}
\]

#### Proof

First match \(\mathcal O\) into distinct members of \(\mathcal B\) by
containment.  Hall follows from Kruskal--Katona.  Indeed every
\(\mathcal F\subseteq\mathcal O\) has

\[
 |\mathcal F|\le C={1\over m+1}{2m\choose m}
              <{2m-1\choose m}.
\]

Write \(|\mathcal F|={x\choose m}\) with real \(x<2m-1\).  The Lovasz
form of Kruskal--Katona gives

\[
 |\partial\mathcal F|\ge{x\choose m-1}
 ={m\over x-m+1}{x\choose m}
 \ge |\mathcal F|.                                  \tag{3.3}
\]

Hence there is an injection \(U\mapsto X_U\in\mathcal B\) with
\(X_U\subset U\).

Second, the vertex-edge incidence graph of a cycle has a perfect matching:
orient \(K\) cyclically and send every vertex to its outgoing edge.
Restricting this matching to the distinct vertices \(X_U\) assigns them
to distinct incident cycle edges \(e_U\).  Then \(e_U\sim U\) in (3.1).
Thus the \(C\) right vertices are saturated by distinct ground elements,
which proves (3.2). \(\square\)

The two matroids therefore have enough rank separately.  Their correlation
is exact rather than heuristic.

### Theorem 3.2 (exact safe-endpoint min--max)

There is an intersection-safe deletion set \(D\) of order \(C\), together
with a bijection \(\eta:D\to\mathcal O\) and endpoint choices
\(p(e)\in e\) satisfying

\[
                         p(e)\subset\eta(e),          \tag{3.4}
\]

if and only if

\[
 \boxed{
 \min_{S\subseteq E(K)}
 \bigl(r_{\rm safe}(S)+r_{\rm end}(E(K)\setminus S)\bigr)
 \ge C.}                                             \tag{3.5}
\]

#### Proof

The desired \(D\) is precisely a common independent set of order \(C\)
in \(\mathsf M_{\rm safe}\) and \(\mathsf M_{\rm end}\).  Edmonds'
matroid-intersection theorem gives (3.5).  A representing matching of
\(D\) in \(R_K\) is exactly the data \((\eta,p)\). \(\square\)

Thus the former simultaneous deletion, lower-colour, and endpoint-Hall
rows collapse to one ordinary two-matroid inequality.

In this particular pair of matroids the min--max has an even simpler
capacitated-Hall form.  For \(\mathcal X\subseteq\mathcal O\), let

\[
 N_K(\mathcal X)=
 \{e\in E(K):e\sim U\text{ for some }U\in\mathcal X\}.
\]

### Corollary 3.3 (single capacitated Hall system)

Condition (3.5) is equivalent to

\[
 \boxed{
 \sum_{a\in\mathcal A}
   \min\bigl(\mu_a-1,\ |N_K(\mathcal X)\cap E_a|\bigr)
 \ge |\mathcal X|
 \quad(\mathcal X\subseteq\mathcal O).}             \tag{3.6}
\]

#### Proof

Use the integral network

\[
 \mathcal O\longrightarrow E(K)\longrightarrow\mathcal A
                     \longrightarrow\{\mathrm{sink}\}.
\]

Give every first and second arc unit capacity, where the first arcs are
the incidences (3.1) and an edge node has only the arc to its colour
\(i(e)\).  Give the final arc at colour \(a\) capacity \(\mu_a-1\).
An integral flow of value \(C\) chooses distinct cycle edges, assigns them
to all omitted colours, and deletes at most \(\mu_a-1\) edges of every
intersection colour.  The capacitated form of Hall's theorem says that it
saturates \(\mathcal O\) exactly when every \(\mathcal X\) has total
neighbour capacity at least \(|\mathcal X|\).  Since the edge nodes split
by their unique colour, that capacity is precisely the left side of
(3.6). \(\square\)

The full right degree before the safety capacities are imposed is exact:
every omitted \(U\in\mathcal O\) contains \(m\) members of \(\mathcal B\),
each with two incident cycle edges, and no cycle edge has both endpoints
inside \(U\) (otherwise its union would be the omitted colour \(U\)).
Hence

\[
                         |N_K(U)|=2m.                \tag{3.7}
\]

Thus any failure of (3.6) is caused specifically by concentration on
intersection colours whose deletion capacities are exhausted; it is not
an ordinary endpoint-degree shortage.

There is a particularly transparent sufficient certificate.  For
\(U\in\mathcal O\), an **\(U\)-hinge** is a length-two segment

\[
 Y^-_U-X_U-Y^+_U                                      \tag{3.8}
\]

of \(K\), where \(X_U\subset U\), and

\[
 X_U\cap Y^-_U=X_U\cap Y^+_U=:a_U.                   \tag{3.9}
\]

Thus both hinge edges have the same intersection colour.  Say that a bank
of hinges is private when the segments are edge-disjoint and the colours
\(a_U\) are distinct.

### Corollary 3.4 (private omitted-colour hinges close the cut)

If every \(U\in\mathcal O\) has a private \(U\)-hinge, then (3.5)--(3.6)
hold.

#### Proof

Choose one of the two hinge edges for every \(U\).  Edge-disjointness makes
the choices distinct, and use \(X_U\) as the endpoint in (3.4).  The other
edge of the same hinge remains, so deleting the chosen edge does not erase
the colour \(a_U\).  Distinctness of the \(a_U\)'s means no colour loses
more than one occurrence.  Hence the chosen bank is both endpoint-matchable
and intersection-safe. \(\square\)

In the alternating \(\mathcal B\leftrightarrow\mathcal U\) lift, a hinge
has the explicit local form

\[
 (X_U-b+x)- (X_U+x)-X_U-(X_U+y)-(X_U-b+y),           \tag{3.10}
\]

with \(b\in X_U\) and distinct \(x,y\notin X_U\).  The omitted colour is
\(U=X_U+u\) for a third outside label \(u\).  Consequently the strengthened
cycle target is concrete: arrange one private same-deletion wedge around a
facet of every unvisited upper vertex.

## 4. Complementation produces the complete interior forest

Assume (1.3) and (3.5), and fix \(D,\eta,p\) as above.  Delete \(D\) from
the cycle \(K\).  It becomes a spanning linear forest on \(\mathcal B\)
with exactly \(C\) path components.

Complement every vertex:

\[
 X\in\mathcal B\longmapsto \bar X=\Omega\setminus X
       \in{\Omega\choose m+1}.                      \tag{4.1}
\]

For a retained edge \(e=XY\), its complemented Johnson edge has

\[
 \bar X\cap\bar Y=\overline{q(e)}\in{\Omega\choose m},
 \qquad
 \bar X\cup\bar Y=\overline{i(e)}\in{\Omega\choose m+2}. \tag{4.2}
\]

Because \(q\) is injective, all internal lower colours in (4.2) are
distinct.  Because \(D\) is safe, the upper colours of the retained edges
cover the complete rank-\((m+2)\) layer.

It remains to attach the unused rank-\(m\) lower colours to the endpoint
occurrences.  For every deleted edge \(e=XY\), assign

\[
 \overline{\eta(e)}\subseteq\overline{p(e)}          \tag{4.3}
\]

to the endpoint occurrence corresponding to \(p(e)\).  Assign

\[
 \overline{q(e)}                                     \tag{4.4}
\]

to the other endpoint occurrence.  Formula (4.4) is contained in both
\(\bar X\) and \(\bar Y\).

The assignments are distinct.  The colours in (4.3) are the complements
of \(\mathcal O\); those in (4.4) are the complements of \(q(D)\); and
the internal colours are the complements of \(q(E(K)\setminus D)\).
These three families partition \({\Omega\choose m}\).

Consequently, subdividing every retained owner edge by its colour in
(4.2), and adjoining (4.3)--(4.4) as terminal lower vertices, produces a
spanning incidence path forest

\[
 F_0\subseteq
 {\Omega\choose m}\longleftrightarrow{\Omega\choose m+1} \tag{4.5}
\]

with exactly \(C\) components.  It has all of the following properties:

1. every rank-\((m+1)\) owner occurs once and has degree two;
2. every rank-\(m\) lower vertex occurs once, internally with degree two
   or terminally with degree one;
3. internal lower colours are injective;
4. consecutive owner unions cover every rank-\((m+2)\) target; and
5. the complete endpoint set is explicitly matched.

Adjacent deleted edges cause no problem.  Their common cycle vertex becomes
an isolated owner component and has two endpoint occurrences; the two
assignments above are distinct because \(\eta\) is injective and
\(q(D)\cap\mathcal O=\varnothing\).

### Corollary 4.1 (protected segment form)

If a prescribed owner segment lies in the complement of \(K-D\), then it
survives verbatim in \(F_0\).  Thus the sharp pivot can be protected by
requiring that the union-rainbow cycle contain its complementary segment and
solving the deletion problem on the ground-set minor obtained by removing
the protected edges.  Concretely, if \(P\subseteq E(K)\) is the protected
edge set, replace \(E(K)\) by \(E(K)\setminus P\) in Theorem 3.2 and replace
the colour capacity in (3.6) by

\[
 \min\bigl(\mu_a-1,\ |(E_a\setminus P)\cap N_K(\mathcal X)|\bigr).
 \tag{4.6}
\]

It is not enough merely to know the unrestricted inequality (3.6): the
protected minor must itself have a common independent set of order \(C\).

## 5. Revised first-upper rethread gate

The first exterior-moving rethread no longer needs to choose lower colours,
upper targets, and endpoint colours simultaneously from scratch.  It is
enough to prove the following three statements.

1. **Doubly adequate cycle.**  Choose a union-rainbow Hamilton cycle
   \(K\) on \({\Omega\choose m-1}\) satisfying the intersection
   surjectivity (1.3) and containing the complementary protected pivot
   segment.
2. **Two-matroid cut.**  Prove (3.5), with the protected segment excluded
   from the deletion ground set.
3. **Exterior completion.**  On the same endpoint set, construct the lower
   exterior forest \(F_1\) whose vertical union with \(F_0\) is connected
   and whose seams satisfy the required residence state.

Items 1--2 give the complete immediate-upper deck, lower-colour
injectivity, and the endpoint matching in one literal interior forest.
They do not imply Item 3, arbitrary-width upper coverage, or a common
depth-\(d\) antecedent/compiler.

The gain is exact: the first two correlated resource rows have become one
coloured Hamilton-cycle condition followed by ordinary two-matroid
intersection.  No four-matroid or post-hoc arbitrary endpoint matching is
hidden in the statement.
