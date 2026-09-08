# Exact classification of the local \(\mathcal V\)-frame into three \(Q_3\)-cells

Date: 2026-07-26

Method: pure mathematics only.

## 0. Statement and audit verdict

Put

\[
 A=\{a,b,c,d\},\qquad U=\{u,v\},\qquad W=\{w,x\},
\]

and let

\[
 \mathcal V=
 \left\{X\cup\{\epsilon,\delta\}:
 X\in\binom A2,\ \epsilon\in U,\ \delta\in W\right\}.
 \tag{0.1}
\]

Thus \(|\mathcal V|=6\cdot4=24\).  Give \(\mathcal V\) the physical
pair-flip graph: two states are adjacent when one selected coordinate is
exchanged for one unselected coordinate.  The induced graph is

\[
                  J(4,2)\mathbin\square Q_2.             \tag{0.2}
\]

The following facts are exact.

1. Every partition of \(\mathcal V\) into three physical isometric
   \(Q_3\)'s is obtained by choosing a graph-perfect-matching of the
   octahedron \(J(4,2)\) and multiplying each of its three edges by the
   reservoir \(Q_2\).
2. There are exactly eight such partitions, not three and not fifteen.
3. Two different partitions either share one complete \(Q_3\)-cell, or
   have connected ownership overlap \(C_6\).  There are respectively
   twelve and sixteen unordered pairs of these two kinds.
4. Tensoring \(r\) blocks gives, for each resolution vector, exactly
   \(3^r\) cells \(Q_{3r}\) partitioning \(24^r\) states.  If the two
   local matchings are edge-disjoint in every block, the tensor ownership
   overlap is connected; it has \(6^r\) nonempty owner pairs, each of
   intersection size \(4^r\).
5. The literal within-cell long-cycle bundling fails before any shadow
   estimate: a vertex partition of \(Q_{3r}\) into cycles of length
   \(6r\) would require \(6r\mid2^{3r}\), which is impossible for every
   \(r\ge1\).  Adding a spectator direction can repair this divisibility,
   but three local directions alone do not repair the consecutive-window
   count: one cyclic direction order exposes at most \(3r\) of the
   \(\binom rq\) profiles with one deletion in each of \(q\) blocks.

The last assertion is an architectural no-go for a fixed cyclic order.  It
does not rule out a construction which genuinely changes the global
interleaving of block directions or routes between different source
sectors.

## 1. The physical cubes in \(\mathcal V\)

For distinct \(i,j,k\in A\), define

\[
 \mathcal C(i;j,k)=
 \left\{\{i,t,\epsilon,\delta\}:
 t\in\{j,k\},\ \epsilon\in U,\ \delta\in W\right\}.
 \tag{1.1}
\]

Its active pairs are

\[
                       \{j,k\},\quad U,\quad W,       \tag{1.2}
\]

while \(i\) is fixed.  Hence \(\mathcal C(i;j,k)\) is an isometric
\(Q_3\), and it is precisely

\[
       \bigl\{\{i,j\},\{i,k\}\bigr\}\mathbin\square Q_2. \tag{1.3}
\]

It has eight vertices and twelve edges: four in each of its three active
directions.

Every isometric cube in a constant-weight layer is obtained by choosing
one endpoint from each of a family of pairwise disjoint active coordinate
pairs and fixing all other coordinates.  Here is the short verification
needed in the present dimension.  At a base vertex \(S\), write its three
cube neighbours as \(S-a_i+b_i\).  If two removals were equal, then the
corresponding two neighbours would be adjacent in the Johnson graph,
although they have cube distance two; the same argument excludes two
equal additions.  Thus the three swaps have pairwise disjoint removed and
added coordinates.  The unique fourth vertex on the square through
directions \(i,j\) is then

\[
                         S-a_i-a_j+b_i+b_j.             \tag{1.4}
\]

The three square faces force the last cube vertex to be
\(S-a_1-a_2-a_3+b_1+b_2+b_3\).  Hence the eight vertices are exactly the
independent choices from the three pairs \(\{a_i,b_i\}\).  The same
square-face argument proves the general-dimensional assertion.

In a cube contained in \(\mathcal V\), an active pair cannot meet two of
the three macroclasses

\[
                         A,\qquad U,\qquad W.           \tag{1.5}
\]

Indeed, flipping such a pair would change one of the required occupancies
\((2,1,1)\).  There are at most two disjoint active pairs inside \(A\),
and at most one inside each of \(U,W\).  Consequently a physical \(Q_3\)
in \(\mathcal V\) has exactly one of the following two forms:

\[
 \begin{array}{c|c|c}
 \text{type}&\text{active pairs in }A&
             \text{active reservoir pairs}\\ \hline
 \mathrm I&1&U,W\\
 \mathrm {II}&2&\text{exactly one of }U,W.
 \end{array}                                            \tag{1.6}
\]

Type I is an edge of \(J(4,2)\) times the full reservoir \(Q_2\), as in
(1.3).  Type II is a special \(Q_2\) times one reservoir edge.

## 2. Classification of all three-cell partitions

Suppose three disjoint physical \(Q_3\)'s partition \(\mathcal V\), and
let \(n_{\mathrm I}\) be the number of type-I cells.  Fix a reservoir
state \(Y=\{\epsilon,\delta\}\).  Each type-I cell covers two of the six
special states over \(Y\).  A type-II cell covers either four of them, if
\(Y\) belongs to its chosen reservoir edge, or none.  Hence for some
integer \(k_Y\),

\[
                         2n_{\mathrm I}+4k_Y=6,
 \qquad\text{or}\qquad n_{\mathrm I}+2k_Y=3.           \tag{2.1}
\]

Thus \(n_{\mathrm I}\) is odd, so it is one or three.

Assume first that \(n_{\mathrm I}=1\).  Equation (2.1) says that exactly
one of the two type-II cells is present above each reservoir state.  Their
reservoir edges therefore partition the four vertices of \(Q_2\).  Let
\(e\) be the special edge used by the type-I cell.  Above every reservoir
state, the active type-II cell would have to cover exactly the four
vertices of \(J(4,2)\setminus e\).  But every physical special \(Q_2\) in
\(J(4,2)\) consists of the four cross-pairs of a partition of \(A\) into
two pairs.  Its two omitted vertices are those two complementary pairs,
which are antipodal and therefore nonadjacent in \(J(4,2)\).  The two
vertices of \(e\), on the other hand, are adjacent.  This is impossible.

Therefore \(n_{\mathrm I}=3\).  The three special edges must be disjoint
on vertices and cover all six vertices of \(J(4,2)\); that is, they form
a graph-perfect-matching.  Conversely, every such matching plainly gives
a partition through (1.3).  We have proved:

### Theorem 2.1

The partitions of \(\mathcal V\) into three physical \(Q_3\)-cells are in
bijection with the perfect matchings of the octahedral graph \(J(4,2)\).

## 3. The eight resolutions, symbolically and explicitly

The six vertices of \(J(4,2)\) are the six edges of \(K_4\).  Two are
adjacent precisely when the corresponding \(K_4\)-edges meet.  A perfect
matching of \(J(4,2)\) therefore partitions the six edges of \(K_4\) into
three incident pairs.

The three incident pairs have three distinct centres.  Indeed, two pairs
cannot have the same centre, since four distinct edges incident with that
centre would be required.  Thus exactly one vertex \(r\in A\) is not a
centre.  If \((x,y,z)\) is a cyclic ordering of \(A\setminus\{r\}\), the
matching is

\[
 \mathsf M(r;x,y,z)=
 \bigl\{\{rx,xy\},\ \{ry,yz\},\ \{rz,zx\}\bigr\}.    \tag{3.1}
\]

Reversing the cyclic order gives the only other matching with omitted
centre \(r\).  Hence there are exactly

\[
                              4\cdot2=8               \tag{3.2}
\]

resolutions.  Equivalently, this follows from inclusion--exclusion in
\(K_6\): of its fifteen perfect matchings, nine contain a specified one
of the three forbidden antipodal edges, with the usual corrections
\(15-3\cdot3+3\cdot1-1=8\).

For reference, write the six special states as

\[
 A_0=ab,\quad A_1=ac,\quad A_2=ad,\quad
 A_3=bc,\quad A_4=bd,\quad A_5=cd.                  \tag{3.3}
\]

All eight matchings are:

\[
\begin{array}{c|ccc|c}
 &\multicolumn{3}{c|}{\text{special edges}}&\text{omitted centre}\\ \hline
M_1&(ab,ac)&(ad,bd)&(bc,cd)&b\\
M_2&(ab,ac)&(ad,cd)&(bc,bd)&c\\
M_3&(ab,ad)&(ac,bc)&(bd,cd)&b\\
M_4&(ab,ad)&(ac,cd)&(bc,bd)&d\\
M_5&(ab,bc)&(ac,ad)&(bd,cd)&c\\
M_6&(ab,bc)&(ac,cd)&(ad,bd)&a\\
M_7&(ab,bd)&(ac,ad)&(bc,cd)&d\\
M_8&(ab,bd)&(ac,bc)&(ad,cd)&a.
\end{array}                                           \tag{3.4}
\]

Replacing every edge \((ij,ik)\) in this table by
\(\mathcal C(i;j,k)\) gives the corresponding three \(Q_3\)-cells.  In
particular the two resolutions displayed in the earlier coarse audit are
\(M_1\) and \(M_3\):

\[
\begin{aligned}
M_1&:\quad
 \mathcal C(a;b,c),\ \mathcal C(d;a,b),\ \mathcal C(c;b,d),\\
M_3&:\quad
 \mathcal C(a;b,d),\ \mathcal C(c;a,b),\ \mathcal C(d;b,c).
\end{aligned}                                         \tag{3.5}
\]

These matchings are edge-disjoint.  Their union is the special six-cycle

\[
 ab-ac-bc-cd-bd-ad-ab,                                \tag{3.6}
\]

up to reversal.

The antipodal pairing

\[
                 (ab,cd),\quad(ac,bd),\quad(ad,bc)     \tag{3.7}
\]

is not one of the eight resolutions: its pairs are nonedges of
\(J(4,2)\), and multiplying one of them by \(Q_2\) gives two disjoint
\(Q_2\)'s rather than a \(Q_3\).

## 4. Exact local edge and ownership counts

The octahedron has six vertices, degree four, and twelve edges.  Therefore

\[
 |E(J(4,2)\square Q_2)|
 =12\cdot4+6\cdot4=72.                              \tag{4.1}
\]

Each resolution has three \(Q_3\)'s, hence

\[
 \#\text{vertices}=3\cdot8=24,\qquad
 \#\text{internal cube edges}=3\cdot12=36.           \tag{4.2}
\]

Thus a resolution partitions all vertices but uses exactly half of the
seventy-two induced ambient edges.  The other thirty-six edges join
different cells: they are the nine octahedral edges outside the selected
matching, independently at each of four reservoir states.  It is therefore
a vertex resolution, not an edge decomposition of the induced graph.

There are twelve possible type-I cells in all, one for each edge of the
octahedron.  A fixed middle state belongs to four of them, one for each
octahedral edge incident with its special two-set.  Every possible cell
occurs in exactly two of the eight resolutions.  The resulting incidence
checks are

\[
 12\cdot8=24\cdot4=96,
 \qquad
 8\cdot3=12\cdot2=24.                                \tag{4.3}
\]

The first identity counts state--cell incidences, and the second counts
cell occurrences among all resolutions.

Let \(M,N\) be two distinct octahedral perfect matchings.  They cannot
share two edges, since then their third edge is forced.  Hence they either
share one edge or are edge-disjoint.

If they are edge-disjoint, \(M\cup N\) is a two-regular graph on six
vertices with no two-cycle, and is therefore a \(C_6\).  The bipartite
ownership-overlap graph of the two \(Q_3\)-partitions is the same \(C_6\):
each special vertex gives one nonempty owner pair, and that intersection
is the complete reservoir \(Q_2\), of size four.  Thus

\[
 \begin{array}{c|c}
 \text{owners on each shore}&3\\
 \text{nonempty owner pairs}&6\\
 \text{states per owner intersection}&4\\
 \text{total states}&6\cdot4=24.
 \end{array}                                          \tag{4.4}
\]

This is a connected exact three-cell-versus-three-cell associator.

If \(M,N\) share one edge, the common special edge produces one identical
\(Q_3\)-cell.  The remaining four special vertices form an alternating
\(C_4\).  After cancelling the common cell, one obtains an exact connected
two-cell-versus-two-cell associator on sixteen states.  Before cancellation
the common owner pair has intersection size eight, while each of the four
remaining nonempty owner pairs has intersection size four.

Every octahedral edge belongs to exactly two of the eight perfect
matchings.  Hence a fixed matching has exactly three other matchings with
which it shares an edge, and four which are edge-disjoint.  Consequently
the twenty-eight unordered pairs split as

\[
 \boxed{12\text{ one-common-cell pairs}+16\text{ edge-disjoint,
 connected pairs}.}                                  \tag{4.5}
\]

## 5. Tensor resolutions and counts

Take \(r\) disjoint copies of the eight-coordinate frame.  A resolution
vector

\[
                  \boldsymbol M=(M^{(1)},\ldots,M^{(r)})
                  \in\{M_1,\ldots,M_8\}^r             \tag{5.1}
\]

gives the product partition

\[
                       \mathcal V^r
                       =\mathop{\dot\bigcup}_{3^r\text{ cells}}Q_{3r}.
 \tag{5.2}
\]

The exact ledger is

\[
\begin{array}{c|c}
\text{global resolution vectors}&8^r\\
\text{states in }\mathcal V^r&24^r\\
\text{cells in one resolution}&3^r\\
\text{vertices in one cell}&8^r=2^{3r}\\
\text{edges in one }Q_{3r}&3r\,2^{3r-1}\\
\text{internal edges in one resolution}&(3r/2)24^r.
\end{array}                                           \tag{5.3}
\]

The induced ambient product graph is \(6r\)-regular, so it has

\[
                         3r\,24^r                    \tag{5.4}
\]

edges.  Again a cube resolution retains exactly half of them.

Now compare two resolution vectors \(\boldsymbol M,\boldsymbol N\) which
are edge-disjoint in every block.  Each left product owner meets exactly
\(2^r\) right product owners.  Hence there are

\[
                         3^r2^r=6^r                  \tag{5.5}
\]

nonempty owner pairs, and every intersection is the product of \(r\)
reservoir squares, hence a \(Q_{2r}\) of size \(4^r\).  Formula
\(6^r4^r=24^r\) audits every physical owner once.

The tensor overlap is connected.  To see this without invoking a product
graph theorem, label the three local owners on each shore by
\(\{0,1,2\}\).  After relabelling, local nonintersection is a perfect
matching, so the local biadjacency matrix is \(B=J-I\).  The tensor
biadjacency matrix is \(B^{\otimes r}\), and

\[
 B B^{\mathsf T}=(J-I)^2=J+I.                        \tag{5.6}
\]

Every entry of \((J+I)^{\otimes r}\) is positive.  Thus every two left
owners have a common right neighbour, proving connectedness.

More generally, suppose the two resolution vectors agree in \(r-s\)
blocks and use edge-disjoint local matchings in the other \(s\) blocks.
The unchanged local overlap is the identity on its three cells, while
each changed block has biadjacency \(B=J-I\).  Hence the tensor overlap
has exactly

\[
                             3^{r-s}                  \tag{5.7}
\]

connected components, indexed by the common cell choices in the unchanged
blocks.  Each component has \(3^s\) owners on each shore,
\(6^s\) nonempty owner pairs, and every owner intersection has size

\[
                             4^s8^{r-s}.              \tag{5.8}
\]

Thus one-block recoupling permits \(3^{r-1}\) independent raw component
switches, whereas recoupling all blocks at once is a single connected
three-to-the-\(r\) associator.  Equations (5.7)--(5.8) also audit the
total support:

\[
 3^{r-s}6^s4^s8^{r-s}=24^r.                           \tag{5.9}
\]

For a fixed local matching there are four edge-disjoint alternatives.
Thus every tensor resolution has exactly \(4^r\) alternatives satisfying
the blockwise-disjoint hypothesis above.

## 6. What three local directions do not fix

First, the most literal long-cycle substitution is arithmetically
impossible.  A factor of \(Q_{3r}\) into cycles of length \(2(3r)=6r\)
would contain

\[
                         \frac{2^{3r}}{6r}             \tag{6.1}
\]

cycles.  This must be an integer, but \(3\mid6r\) and
\(3\nmid2^{3r}\).  Therefore no such vertex factor exists for any
\(r\ge1\).  This is an edge-versus-vertex audit: individual isometric
\(C_{6r}\)'s exist, but they cannot partition the vertices of
\(Q_{3r}\).

Second, even after a spectator repair of the divisibility, the fine
consecutive-window count survives.  In an isometric \(C_{2h}\subset Q_h\),
the transition word is \(\pi\pi\) for a permutation \(\pi\) of the
\(h\) directions.  Indeed every cyclic interval of at most \(h\)
transitions must have distinct directions; consecutive length-\(h\)
windows therefore contain all directions and force period \(h\).

Put \(h=3r\) formally and label the three directions in block \(i\) by
the same macro-label \(i\).  For \(q\le r\), consider just the deletion
profiles

\[
 d^J_i=\mathbf1_{\{i\in J\}},\qquad
                         J\in\binom{[r]}q.             \tag{6.2}
\]

There are \(\binom rq\) such profiles.  A cyclic word \(\pi\) has only
\(3r\) starting positions modulo its repeated half, so its length-\(q\)
windows realize at most \(3r\) of them.  Consequently \(K\) fixed global
direction orders which are required to supply every profile obey

\[
             \boxed{K\ge \frac1{3r}\binom rq.}         \tag{6.3}
\]

For \(q=o(r)\),

\[
 \log K\ge q\log(r/q)-O(q+\log r).                    \tag{6.4}
\]

In particular this is superpolynomial at \(q=\Theta(\sqrt m)\) whenever
\(r/q\to\infty\).  Choosing any of the eight local octahedral matchings
changes which special coordinate swap realizes the special direction.  It
does not change the macro-label of that direction.  Therefore all
\(8^r\) alternative local resolution vectors have exactly the same
macroprofile support if they are bundled with the same abstract cyclic
block word.

Thus three local directions improve the old linear denominator from
\(2r\) to at most \(3r\); they do not remove the consecutive-window
obstruction.  Evading (6.3) requires genuinely different global
interleavings, cross-sector transport, or a non-cycle operation.  It
cannot follow solely from the eight exact local associator choices.
