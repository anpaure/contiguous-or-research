# State-adaptive octahedral \(Q_3\) mosaics retain the unique-carrier lock

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let

\[
 \mathcal V_i=J_i\times R_i,
 \qquad J_i=J(4,2),\qquad R_i=Q_2,
 \tag{0.1}
\]

and call

\[
 C_i(e)=e\times R_i\qquad(e\in E(J_i))               \tag{0.2}
\]

an elementary local \(Q_3\)-cell.  A product cell is

\[
 C(\boldsymbol e)=\prod_{i=1}^r C_i(e_i)\cong Q_{3r}. \tag{0.3}
\]

A *product-cell mosaic* is any partition of
\(\mathcal V^r\) into cells (0.3).  Every mosaic obtained by any sequence
of ownership-component switches among the eight local octahedral
resolutions is of this form.  The results below therefore allow more
state adaptivity than component switching itself.

Fix \(I\subseteq[r]\), \(|I|=q\).  A fine singleton target has local
restriction

\[
 T_i=\{z_i\}\cup Y_i\quad(i\in I),qquad
 T_j=X_j\cup Y_j\in\mathcal V_j\quad(j\notin I),       \tag{0.4}
\]

where \(z_i\) is one of the four special coordinates and \(Y_i\in R_i\).
The exact conclusions are:

1. In the complete catalogue of product cells, \(T\) has exactly

   \[
                         3^q4^{r-q}                    \tag{0.5}
   \]

   candidate carriers.
2. These candidate cells are pairwise intersecting; indeed any two share
   a middle extension of \(T\).  Consequently a single exact mosaic
   contains at most one of them.  The exact simultaneous carrier
   multiplicity is therefore

   \[
                              \boxed{0\text{ or }1}.    \tag{0.6}
   \]

3. Every mosaic contains \(3^r\) cells and, for the fixed touched set
   \(I\), makes exactly

   \[
                  3^r4^q8^{r-q}                       \tag{0.7}
   \]

   fine targets compatible.  Since there are
   \(16^q24^{r-q}\) fine targets with this \(I\), the compatible fraction
   is exactly

   \[
                              \boxed{(3/4)^q}.          \tag{0.8}
   \]

   Thus state adaptivity does not improve even the pre-consecutiveness
   singleton loss.
4. On every one-block fiber, every mosaic induces a perfect matching of
   the octahedron.  The matching may depend on the other block states, but
   it still has a unique omitted singleton.  This is the precise
   state-adaptive invariant.
5. Allowing an arbitrary cyclic direction order separately in every
   mosaic cell still reaches at most

   \[
                 3^r(r-q+1)4^q8^{r-q}                 \tag{0.9}
   \]

   targets after imposing a consecutive \(q\)-window.  Hence the earlier
   reachable fraction

   \[
                 \left(\frac34\right)^q
                 \frac{r-q+1}{\binom rq}              \tag{0.10}
   \]

   holds verbatim for arbitrary state-adaptive mosaics.

Across \(K\) different mosaics, rather than inside one, the maximum number
of distinct carrier cells which a fixed target can acquire is exactly

\[
                   \min\{K,3^q4^{r-q}\}.              \tag{0.11}
\]

Thus multiplicity can only be bought by using genuinely different exact
factors; a componentwise mosaic cannot create it internally.

## 1. Exact candidate-carrier catalogue

Suppress the reservoir coordinates temporarily.  In a touched block
\(i\in I\), a special-axis lower face equal to the singleton \(z_i\)
must come from an octahedral edge whose two vertices are special two-sets
containing \(z_i\).  There are three such two-sets.  They form a triangle
in \(J_i\), and its three edges are exactly the possible local carriers.
Thus there are three choices in a touched block.

In an untouched block \(j\notin I\), the prescribed special state \(X_j\)
must be a vertex of the carrier edge.  The octahedron has degree four, so
there are exactly four incident carrier edges.  Choices in different
blocks are independent, proving (0.5).

Every candidate cell really occurs in an ordinary tensor resolution.  An
edge of \(J(4,2)\) lies in exactly two of its eight perfect matchings.
Choose one such matching independently in every block.  The resulting
tensor resolution contains the prescribed product cell.

There is a useful occurrence audit.  A fixed candidate product cell lies
in exactly \(2^r\) of the \(8^r\) ordinary tensor resolutions.  Therefore
the total number of compatible resolution-vector occurrences of \(T\) is

\[
 3^q4^{r-q}2^r=6^q8^{r-q}.                            \tag{1.1}
\]

Equivalently, each touched block permits six of the eight matchings and
each untouched block permits all eight.

## 2. The carrier-clique lemma

### Lemma 2.1

Any two candidate product cells for the same fine target \(T\) have a
common middle vertex extending \(T\).

### Proof

Consider two candidates \(C(\boldsymbol e)\) and
\(C(\boldsymbol f)\).  If \(i\in I\), then \(e_i,f_i\) are two edges of
the triangle on the three special two-sets containing \(z_i\).  Any two
edges of a triangle share a vertex.  Choose such a common special two-set
and adjoin the prescribed reservoir orientation \(Y_i\).  This is a
middle extension of \(T_i\) lying in both local cells.

If \(j\notin I\), both \(e_j,f_j\) are incident with \(X_j\).  Hence the
prescribed middle state \(X_j\cup Y_j\) lies in both local cells.  Taking
the product of these local common vertices gives a middle extension of
\(T\) in the intersection of the two product cells. \(\square\)

The cells of a product-cell mosaic are pairwise vertex-disjoint.  Lemma
2.1 immediately proves (0.6).  Notice that the three local candidates in
a touched block have no common special vertex all together; pairwise
intersection, which is exactly what disjoint ownership tests, is the
correct invariant.

The upper bound one is attained whenever the target is compatible with a
mosaic.  It is also attained for every target in some ordinary tensor
resolution, by the last paragraph of Section 1.  Thus it is the exact
maximum, not merely a universal upper bound.

## 3. Exact compatible-target count in every mosaic

Every product cell has \(8^r\) vertices, while
\(|\mathcal V^r|=24^r\).  Hence every mosaic contains exactly

\[
                              24^r/8^r=3^r             \tag{3.1}
\]

cells.

Fix a product cell and the touched set \(I\).  In a touched block its
special carrier edge determines one singleton, namely the intersection of
its two special two-sets; only the reservoir orientation remains free,
giving four fine targets.  In an untouched block any of the eight local
cell vertices may be prescribed.  The cell therefore carries exactly

\[
                              4^q8^{r-q}                \tag{3.2}
\]

fine targets with touched set \(I\).

By Lemma 2.1 no target is counted for two different cells of the mosaic.
Multiplying (3.1) and (3.2) proves (0.7).  On the other hand, a touched
block has \(4\cdot4=16\) possible singleton-plus-reservoir targets, and an
untouched block has twenty-four middle states.  Division gives

\[
 \frac{3^r4^q8^{r-q}}{16^q24^{r-q}}
 =\left(\frac34\right)^q,                              \tag{3.3}
\]

proving the exact invariant (0.8).  Summing over all
\(I\in\binom{[r]}q\) simply multiplies numerator and denominator by
\(\binom rq\).

## 4. Fiberwise perfect matching and omitted-singleton field

Write only the special support of a product cell as the box

\[
                              e_1\times\cdots\times e_r
                              \subseteq J_1\times\cdots\times J_r.
 \tag{4.1}
\]

Fix a block \(i\) and an outside special state

\[
                 \xi=(X_j)_{j\ne i}\in\prod_{j\ne i}V(J_j).        \tag{4.2}
\]

Intersect the mosaic boxes with the fiber

\[
                    V(J_i)\times\{\xi\}.              \tag{4.3}
\]

A box either misses this fiber or intersects it in exactly the edge
\(e_i\).  Since the mosaic boxes are disjoint and cover the product, these
edge intersections partition the six vertices of \(J_i\).  They are
therefore a perfect matching, denoted

\[
                              M_i(\xi).                 \tag{4.4}
\]

By the octahedral omitted-centre lemma, the three intersection labels of
\(M_i(\xi)\) are distinct.  Consequently there is a unique omitted label

\[
              o_i(\xi)\in\{a_i,b_i,c_i,d_i\}.          \tag{4.5}
\]

This proves the promised invariant.  A mosaic can make the field
\(o_i(\xi)\) depend on the other block states, but it cannot assign all
four singleton labels on one fiber.  Component switches merely alter this
field on unions of fibers permitted by their overlap components.

## 5. Consecutive windows remain locked

Assign an arbitrary cyclic order of the \(3r\) genuine axes, together
with any spectator axes, independently in every mosaic cell.  A fine
target with touched set \(I\) forces precisely the \(q\) special axes of
those blocks.  Among a cyclic word containing \(r\) special axes and at
least the \(2r\) reservoir axes, at most

\[
                              r-q+1                    \tag{5.1}
\]

all-special \(q\)-sets can be intervals: split the special positions into
runs of lengths \(\ell_j\) and use

\[
                 \sum_j(\ell_j-q+1)_+\le r-q+1.        \tag{5.2}
\]

For each permitted touched set, the cell carries (3.2) targets.  There are
\(3^r\) cells, proving (0.9).  Dividing by

\[
                 \binom rq16^q24^{r-q}                 \tag{5.3}
\]

gives (0.10).

Thus neither a common direction order nor a uniform tensor matching was
responsible for the prior no-go.  The two exact inputs are instead:

1. pairwise collision of all carrier boxes for one fine target; and
2. the fiberwise omitted-singleton law in every integral box tiling.

## 6. Multiplicity across several mosaics

Let \(N(T)=3^q4^{r-q}\) be the complete candidate catalogue from (0.5).
One mosaic contributes at most one distinct candidate by Lemma 2.1, so
\(K\) mosaics contribute at most \(\min\{K,N(T)\}\).

Conversely, choose any \(L\le N(T)\) distinct candidate cells.  Section 1
places each candidate in an ordinary tensor resolution.  Using those
\(L\) resolutions as \(L\) mosaics realizes all of them.  This proves the
equality (0.11).

The result identifies the exact escape requirement.  To give one target
several simultaneous orders, a future construction must allow owner
pieces which are not complete product cells, or must route the target from
different rank/macroprofile sectors.  State-dependent component switches
among the eight complete local \(Q_3\) resolutions cannot do it.

