# Exact rank-transfer braids in the punctured Johnson prism

## 1. Outcome

The upper-color imbalance in PRISM_SEGMENT_COMPLETION.md,

\[
                         (+D_m,-2D_m,+D_m),
\]

has an elementary local correction. If a \(t=0\) edge has endpoints
\(A,B\) and common part \(K=A\cap B\), it forms a Johnson rhombus with
the \(t=2\) rung \(Kp-Kq\):

\[
       (A-B)+(Kp-Kq)\longrightarrow(A-Kp)+(B-Kq).     \tag{1.1}
\]

The two right-hand edges have \(t=1\), so (1.1) realizes one unit of

\[
                        (1,0,1)\longrightarrow(0,2,0).             \tag{1.2}
\]

There is a sharp topological obstruction: applying (1.1) as a two-edge
switch between complementary paths cross-pairs their endpoints. The
smallest endpoint-safe operation in an arbitrary graph has three cut edges:
cut one path twice, extract the intervening segment, and insert it into the
rung cut of the other path. The exact ear braid is Theorem 3.2. However,
the geodesic outer paths admit no required shortcut, so this abstract
minimum is unavailable in the punctured-prism geometry. The usable local
operation has four boundaries and exchanges two segments (Theorem 3.4).

For any fixed lower-support completion, positivity is then an explicit
capacitated exact-matching system: every prism rung is used once, precisely
the excess \(t=0\) occurrences are removed, the \(t=1\) colors finish with
multiplicity one, and selected physical segments are disjoint. This is an
all-dimensional reduction, not yet a proof that the Catalan system is
feasible.

## 2. The elementary rank rhombus

Let \(|X|=2m\), and put

\[
 |K|=m,\qquad A=K\cup\{a\},\qquad B=K\cup\{b\},
 \qquad a\ne b,\quad a,b\notin K.                    \tag{2.1}
\]

The four lower vertices \(A,B,Kp,Kq\) span the relevant edges, with upper
colors

\[
\begin{array}{c|c|c}
\text{edge}&\text{upper color}&t\\ \hline
A-B&K\cup\{a,b\}&0\\
Kp-Kq&Kpq&2\\
A-Kp&Ap&1\\
B-Kq&Bq&1.
\end{array}                                                        \tag{2.2}
\]

The crossed orientation \(A-Kq,B-Kp\) is equally valid.

### Lemma 2.1

Replacing \(A-B,Kp-Kq\) by either crossed pair preserves the four lower
vertices and changes the upper-sector occurrence vector by

\[
                              (-1,+2,-1).             \tag{2.3}
\]

## 3. Endpoint topology and the legal braid

### Lemma 3.1 (one-cut obstruction)

Let \(P,Q\) be vertex-disjoint complementary paths. Delete one internal
edge from each and reconnect the four loose ends nontrivially with two
cross edges. Every resulting path has one endpoint from \(P\) and one from
\(Q\), and hence is not complementary.

#### Proof

The endpoint pairs are \(\{r,\bar r\}\) and \(\{s,\bar s\}\), with all
four vertices distinct. A cross-reconnected path has endpoints among
\(r,s\), \(r,\bar s\), \(\bar r,s\), or \(\bar r,\bar s\). None is an
antipodal pair. \(\square\)

### Theorem 3.2 (three-boundary ear braid)

Suppose two vertex-disjoint complementary paths contain

\[
 P:\quad \cdots-u-a\,S\,b-v-\cdots ,
 \qquad
 Q:\quad \cdots-c-d-\cdots .                         \tag{3.1}
\]

Assume the removed boundary sectors are

\[
 \operatorname{sec}(u a)=1,\qquad
 \operatorname{sec}(b v)=0,\qquad
 \operatorname{sec}(c d)=2,                         \tag{3.2}
\]

and that

\[
                              u-v,\qquad c-a,\qquad b-d             \tag{3.3}
\]

are four distinct \(t=1\) edges. Exchange the two segments:

\[
\begin{aligned}
 P'&:\quad\cdots-u-v-\cdots,\\
 Q'&:\quad\cdots-c-a\,S\,b-d-\cdots.                \tag{3.4}
\end{aligned}
\]

Then \(P',Q'\) are vertex-disjoint complementary paths with their original
endpoints and lower-vertex union, while their upper-sector vector changes
by \((-1,+2,-1)\).

#### Proof

The operation removes the segment \(aSb\) from \(P\), closes its old gap,
and inserts it into the cut edge \(c-d\) of \(Q\). The three new
boundaries are edges by hypothesis; each word retains its original
endpoints and all lower vertices are retained exactly once. The removed
sector vector is \((1,1,1)\), while the three inserted edges give
\((0,3,0)\). The difference is \((-1,+2,-1)\). \(\square\)

Lemma 3.1 rules out two cut edges total, while Theorem 3.2 uses three.
Thus the ear braid is a minimal endpoint-safe rank transfer.

### Lemma 3.3 (geodesic shortcut obstruction)

No nontrivial ear braid of Theorem 3.2 can use one of the explicit
\(O_0(P)\) paths as its \((t=1,t=0)\)-boundary path.

#### Proof

Write

\[
 O_0(P)=x_0p,y_0,y_1,\ldots,y_{m-1},x_mq.
\]

The only \(t=1\) edges are the two boundary edges. Suppose the extracted
segment begins at the left boundary and ends at an internal edge
\(y_i-y_{i+1}\). The required shortcut is \(x_0p-y_{i+1}\), which is a
Johnson edge exactly if \(x_0\subset y_{i+1}\).

The old path is geodesic from \(x_0\) to its complement. After \(j\)
Johnson moves, exactly \(j\) elements of \(x_0\) have been removed and no
removed element is ever reinserted. Hence

\[
                         |x_0\cap y_j|=m-j.           \tag{3.5}
\]

For \(j\ge1\), \(x_0\not\subset y_j\). Thus no nontrivial left shortcut
exists. Reversing the path gives the identical obstruction at the right
boundary: \(x_m\subset y_j\) only for \(j=m-1\). \(\square\)

Every endpoint-safe three-cut reconnection is, up to exchanging the path
names and reversing segments, an ear insertion of Theorem 3.2. Therefore
Lemma 3.3 shows that the explicit outer/prism transfer needs at least four
cut edges unless the outer paths are recolored first.

### Theorem 3.4 (four-boundary segment exchange)

Let

\[
 P:\ \cdots-u-a\,S\,b-v-\cdots,\qquad
 Q:\ \cdots-w-c\,T\,d-z-\cdots
\]

be vertex-disjoint complementary paths. Assume the removed boundary
sectors are respectively

\[
                         (1,0)\quad\text{on }P,\qquad
                         (1,2)\quad\text{on }Q,       \tag{3.6}
\]

and that

\[
                         u-c,\quad d-v,\quad w-a,\quad b-z         \tag{3.7}
\]

are four \(t=1\) edges. Exchanging \(S,T\) through these four joins
preserves both endpoint pairs and the lower-vertex partition and changes
the upper-sector vector by \((-1,+2,-1)\).

#### Proof

The removed sector vector is \((1,2,1)\), and the inserted vector is
\((0,4,0)\). The two paths retain their original endpoints. \(\square\)

This four-boundary exchange is the minimal direct braid available for the
explicit \(O_0\) geometry.

## 4. Canonical bases

For an old complementary path

\[
 P=(x_0,y_0,x_1,\ldots,y_{m-1},x_m),
\]

the internal \(t=0\) edges of \(O_0(P)\) are

\[
                         y_{i-1}-y_i\qquad(1\le i<m).               \tag{4.1}
\]

Both endpoints contain \(x_i\), so

\[
                         y_{i-1}\cap y_i=x_i.         \tag{4.2}
\]

The matching rung is canonically \(x_ip-x_iq\). Internal lower vertices
are globally distinct across the old path factor. Therefore at the
sector-count level there is no Hall problem: choosing removable \(t=0\)
occurrences is identical to choosing their prism rung bases via (4.2).
The hard constraints are endpoint-safe segment routing and the individual
\(t=1\) colors.

## 5. Exact color demands

Let \(\mu_0(C)\) be the multiplicity of a \(t=0\) upper color among the
\((m-1)\operatorname{Cat}_m\) internal \(O_0\) edges. There are

\[
 \binom{2m}{m+2}=(m-1)\operatorname{Cat}_m-D_m       \tag{5.1}
\]

possible targets.

If rank-transfer braids are the only operations changing this sector,
exactness is possible if and only if

\[
 \mu_0(C)\ge1\quad\text{for every }C,                \tag{5.2}
\]

and the selected removals obey

\[
 \#\{\text{selected occurrences of color }C\}
                              =\mu_0(C)-1.            \tag{5.3}
\]

These demands sum to \(D_m\). Condition (5.2) is sharp: a pure transfer
only deletes \(t=0\) colors and cannot create a missing one. A contractive
lift for factors with old holes therefore needs additional recoloring
braids proportional to the inherited defect.

Every \(t=1\) target is \(yp\) or \(yq\), for one old upper vertex \(y\).
Let \(\mu_1(yr)\) be its provisional multiplicity. A selected canonical
base \(x_i=y_{i-1}\cap y_i\) has two orientations:

\[
\begin{array}{c|cc}
\text{orientation}&\text{first new color}&\text{second new color}\\ \hline
+&y_{i-1}p&y_iq\\
-&y_{i-1}q&y_ip.
\end{array}                                                        \tag{5.4}
\]

After accounting for the removed \(t=1\) boundary in Theorem 3.2,
the targetwise equation is

\[
 \mu_1(yr)
 -\#\{\text{removed \(t=1\) boundaries of color }yr\}
 +\#\{\text{new cross boundaries of color }yr\}
 =1.                                                \tag{5.5}
\]

The global imbalance gives the right total mass but does not imply (5.5).

## 6. The exact braid hypergraph

Fix the outer paths, a lower-support partition of the punctured prism into
\(D_m\) complementary paths, and all orientations. Define a hypergraph
\(\mathcal H\). Its resources are:

* prism rungs;
* removable \(t=0\) occurrences;
* removable \(t=1\) occurrences;
* missing required \(t=1\) occurrences; and
* physical path boundaries and segments.

A hyperedge is one admissible four-boundary braid from Theorem 3.4,
together with its rung, one \(t=0\) occurrence, two removed \(t=1\)
occurrences, four supplied \(t=1\) occurrences, and its two exchanged
physical segments.

### Theorem 6.1 (exact positivity criterion)

The imbalance is corrected by simultaneous four-boundary braids,
without changing lower ownership, if and only if \(\mathcal H\) has a
family \(\mathcal B\) of \(D_m\) hyperedges such that:

1. every prism rung occurs exactly once;
2. (5.3) holds for every \(t=0\) color;
3. (5.5) holds for every \(t=1\) color; and
4. physical segments in different selected hyperedges are
   interior-disjoint.

#### Proof

Necessity is the resource ledger above. Conversely, perform all selected
braids. Segment disjointness makes them simultaneous. Theorem 3.2
preserves the lower partition and antipodal endpoints. Conditions 1--3
make upper colors exhaustive in sectors \(t=2,0,1\), respectively.
\(\square\)

This is an exact matching formulation, but in general it is a hypergraph
exact-cover problem, not an automatic max-flow. The Catalan recursion must
supply laminar segments or another structure before Hall's theorem applies.

## 7. The tag-orientation flow

Ignore physical segment conflicts temporarily. Make a graph whose vertices
are the old upper states \(y\). Every selected base
\(x_i=y_{i-1}\cap y_i\) contributes the edge

\[
                              y_{i-1}y_i.             \tag{7.1}
\]

Before color identifications, this is a subgraph of the disjoint union

\[
                    y_0-y_1-\cdots-y_{m-1}
\qquad(P\in\mathcal P).                              \tag{7.2}
\]

Call a four-boundary braid **color-transparent at its auxiliary joins**
when two of its four inserted \(t=1\) colors equal, as a multiset, the two
removed \(t=1\) colors. Its net \(t=1\) contribution is then the two
remaining insertion colors, which form one of the rows in (5.4). For a
family of transparent braids, orienting
(7.1) chooses which endpoint receives tag \(p\) and which gets \(q\).

Let \(p_y\) be the required number of selected incident edges which must
give tag \(p\) to \(y\).  Orient an edge toward the endpoint receiving
\(p\).  The exact integral-flow criterion is the standard prescribed-
indegree criterion

\[
 \sum_{y\in V(G)}p_y=|E(G)|,\qquad
 |E(U)|\le\sum_{y\in U}p_y
          \le |E(U)|+|\delta(U)|\quad(U\subseteq V(G)).             \tag{7.3}
\]

Indeed, every internal edge of \(U\) contributes exactly one head inside
\(U\), while a boundary edge contributes zero or one.  These inequalities
are also sufficient by the integral orientation theorem (and reduce to
leaf stripping because (7.2) is a forest).

Thus transparent tag orientation is ordinary integral flow.  Without
transparency, the full target equations (5.5) in the braid hypergraph are
the correct formulation.  In either case the remaining problem is to
choose removable \(t=1\) boundaries and disjoint segments so that the flow
inequalities hold.

## 8. Catalan first-return target

\[
 D_m=\operatorname{Cat}_{m+1}-2\operatorname{Cat}_m
    =\sum_{i=1}^{m-1}\operatorname{Cat}_i
                         \operatorname{Cat}_{m-i}.                  \tag{8.1}
\]

This suggests indexing braid segments by interior first-return pairs

\[
 (u,v),\qquad u\in\mathcal D_i,\quad v\in\mathcal D_{m-i},
 \quad1\le i<m.                                      \tag{8.2}
\]

The precise all-dimensional target is to map every pair (8.2) injectively
to one removable edge \(y_{j-1}-y_j\), its canonical rung
\(x_jp-x_jq\), and a laminar pair of \(t=1\)-bounded segments satisfying
Theorem 3.2. The images must obey (5.3)--(5.5), and the total number of
cuts must be \(O(\operatorname{Cat}_m)\).

If only prefix/suffix ports are used, segment conflicts reduce to a
capacitated bipartite matching with at most two ports per outer path. The
cardinality has strict slack:

\[
 D_m=2\operatorname{Cat}_m
       -{6\over m+2}\operatorname{Cat}_m
       <2\operatorname{Cat}_m.                       \tag{8.3}
\]

What remains is Hall expansion with the target-color restrictions, not
raw capacity.

## 8.1 An explicit Catalan parent schedule

The raw Catalan indexing does not require Hall's theorem. Let
\(\ell(w)\) be the length of the final descent of a Dyck word
\(w\in\mathcal D_m\). The standard Catalan ECO generating tree obtains
the children of \(w\) by inserting one peak at any of the
\(\ell(w)+1\) sites along its final descent. Every word of
\(\mathcal D_{m+1}\) has a unique parent under deletion of this inserted
rightmost peak. Consequently,

\[
             \sum_{w\in\mathcal D_m}(\ell(w)+1)
                    =\operatorname{Cat}_{m+1}.       \tag{8.4}
\]

Reserve the two endpoint insertion sites for the two outer sectors. The
remaining internal sites form

\[
 \mathscr I_m=\{(w,h):w\in\mathcal D_m,\ 1\le h<\ell(w)\}.          \tag{8.5}
\]

Then

\[
 |\mathscr I_m|
 =\sum_w(\ell(w)-1)
 =\operatorname{Cat}_{m+1}-2\operatorname{Cat}_m
 =D_m.                                               \tag{8.6}
\]

Thus every required rank transfer has a canonical old Dyck parent and an
internal seam site. For one parent, the sites lie on one final descent and
are nested. They may therefore be processed sequentially; the total number
of local braid operations is \(D_m<2\operatorname{Cat}_m\), even though
one exceptional parent can have many children.

This removes the cardinality and abstract parent-assignment parts of the
Catalan Hall problem. The exact remaining statement is local.

> **ECO seam-compatibility lemma.** Under the MSW flip-word recursion, the
> internal peak insertion \((w,h)\) supplies a four-boundary exchange of
> Theorem 3.4 whose \(t=0\) edge and prism rung have their canonical common
> base, whose four cross joins have \(t=1\), and whose individual colors
> satisfy (5.3)--(5.5). Processing the sites in their nested order preserves
> admissibility of the later sites.

If this lemma holds, (8.5) is already the desired global disjoint schedule:
different parents occupy disjoint old factor paths, while sites of one
parent are handled by the nested sequential order. Total seam complexity is
\(O(D_m)=O(\operatorname{Cat}_m)\).

The ECO count alone does not prove seam compatibility. In particular, the
geodesic shortcut obstruction in Lemma 3.3 shows why the three-boundary
version cannot be assigned to these sites; the four-boundary MSW identities
are essential.

## 9. Sharp conclusions

The four-vertex rhombus is not itself a factor move. Antipodal endpoint
topology forces at least a three-boundary ear braid, and the geodesic
shortcut obstruction raises this to four boundaries for the explicit
outer paths. The imbalance vector alone is
also insufficient:

* \(t=0\) coverage is the sharp obstruction (5.2);
* \(t=1\) target balance is the forest flow (5.5);
* lower-support completion supplies the rung paths; and
* segment disjointness is the final integral condition.

A Catalan first-return proof must establish these simultaneously. Failure
of (5.2) for a chosen old factor does not refute the contractive program;
it shows that extra recoloring braids proportional to inherited defect are
necessary.
