# Tensor rectangles under recursive context orders: the exact signed kernel and outer Hall cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is used.

**Subsequent chronology audit.** The abstract outer cut isolated below is
violated by the canonical first-\(r\)-eligible rectangle atlas. In fact,
even after allowing all three rectangle shores, a positive Gaussian-mass
upper-target stratum has capacity at most \(2^{-q-1}\). See
MATH_AUDIT_RECTANGLE_RECURSIVE_CHRONOLOGY_ALL_SHORE_CUT_20260726.md.
Thus the remaining Hall gate in this report is a gate only for a redesigned
noncanonical atlas; the canonical A/S combination is ruled out.

## 0. Outcome

Let \(r\geq1\), suppose \(h=2r\) is a power of two, and tensor \(r\)
copies of the eight-owner rectangle. The owner packet has

\[
                         V=8^r                                      \tag{0.1}
\]

vertices and is the disjoint union of \(2^r\) physical cells \(Q_h\).
Put the recursive half-depth-rainbow factor \(F_h\) in every cell. Its
block-affine conjugate may be chosen independently in every cell, depending
on the full exterior cell context.

This removes the fixed-common-order obstruction, but the exact result is
signed and asymmetric.

For \(1\le q\le r\), every block-simple affine \(q\)-face in one cell has
exact incidence fraction

\[
                         p_{r,q}^{\rm ctx}={1\over\binom rq}          \tag{0.2}
\]

in the complete block-affine conjugacy menu. If a lower target has \(s\)
touched blocks in which its surviving singleton lies in the common
reservoir pair, then it is a face of exactly \(2^s\) rectangle cells.
Its exact menu-barycentre load is therefore

\[
 \boxed{\lambda^-_{r,q,s}={2^s\over\binom rq}.}                     \tag{0.3}
\]

The \(2^s\) is precisely the tensor power of the cross-sector rectangle
kernel. In contrast, every block-simple upper target determines its
rectangle cell uniquely, for every \(s\). Hence

\[
 \boxed{\lambda^+_{r,q,s}={1\over\binom rq}.}                       \tag{0.4}
\]

Thus context-dependent recursive orders turn the fixed-order run problem
into a literal candidate-cell problem, but they do not make the lower
carrier kernel two-sided.

The complete packet-local block-simple upper target universe has size

\[
                         \binom rq V.                               \tag{0.5}
\]

Every context-dependent recursive factor hits exactly \(V\) distinct
members of that universe. Consequently it leaves exactly

\[
 \boxed{\left(\binom rq-1\right)V}                                 \tag{0.6}
\]

of those physical upper targets to be supplied from other owner packets.
At depth one this is \((r-1)V\). This is independent of the orders chosen
in the \(2^r\) cells and is not a common-order bound.

There is a second order-independent constraint. If \(E_{q,s}\) is the
number of packet starts whose \(q\)-window uses \(s\) private rectangle
directions and \(q-s\) reservoir directions, then

\[
 \boxed{
  \sum_{s=0}^qE_{q,s}=V,\qquad
  \sum_{s=0}^q sE_{q,s}={qV\over2}.}                               \tag{0.7}
\]

It follows that

\[
 E_{q,s}\le \gamma_{q,s}V,\qquad
 \gamma_{q,s}=
 \begin{cases}
 {q\over2(q-s)},&s<q/2,\\[1mm]
 1,&s=q/2,\\[1mm]
 {q\over2s},&s>q/2.
 \end{cases}                                                       \tag{0.8}
\]

The exact lower type-\(s\) target count is

\[
 |\mathcal T^-_{r,q,s}|
 =V\binom rq\binom qs2^{-q-s},                                    \tag{0.9}
\]

so at least

\[
 V\left(\binom rq\binom qs2^{-q-s}-\gamma_{q,s}\right)_+           \tag{0.10}
\]

of these targets require an exterior packet. In particular, at depth one
the targets whose local singleton lies in the four-set have exact internal
deficit

\[
                         {r-1\over2}V.                             \tag{0.11}
\]

For a global owner-disjoint rectangle atlas the remaining condition is an
outer physical Hall cut. If \(\mathscr B\) is a subfamily of packets,
\(U^+_q(\mathscr B)\) is the union of their packet-local upper universes,
and \(G_{\mathscr B}\) is their owner mass, then any global factor has

\[
 \boxed{
 M_q^+\ge
 \left[
 |U^+_q(\mathscr B)|-G_{\mathscr B}
 -\sum_{c\notin\mathscr B}
       \min\{|c|,f^+_{c,q}(U^+_q(\mathscr B))\}
 \right]_+.}                                                       \tag{0.12}
\]

Here \(f^+_{c,q}(A)\) is the number of literal block-simple affine
\(q\)-faces of the outside cell \(c\) whose upper trace belongs to \(A\).
Replacing the minimum in (0.12) by the exact menu maximum gives the sharp
fractional weighted Hall system in Section 7.

Equation (0.12) is the surviving gate for an arbitrary redesigned atlas.
The canonical first-\(r\) atlas fails it by the subsequent chronology
audit quoted above. The macroprofile flow determines
the lower predecessor marginals and supplies the factor \(2^s\) in (0.3),
but it does not determine the physical outside terms in (0.12). Therefore
the A/S recursive construction is a genuine positive order theorem, yet it
does not by itself prove all-depth \(o(W)\)-hole coverage.

## 1. Rectangle cells and the two direction classes

In block \(i\), put

\[
 P_i=\{t_i,e_i\},\qquad A_i=\{a_i,b_i,c_i,d_i\},                   \tag{1.1}
\]

and fix the matching

\[
 E_i^0=\{a_i,b_i\},\qquad E_i^1=\{c_i,d_i\}.                       \tag{1.2}
\]

The local owner support is

\[
                         \Omega_i=P_i*A_i,                         \tag{1.3}
\]

and the two cells are \(P_i*E_i^0\) and \(P_i*E_i^1\). Suppressing a
fixed exterior core, the tensor packet is

\[
                         \Omega=\prod_{i=1}^r\Omega_i.             \tag{1.4}
\]

For \(\varepsilon\in\mathbb F_2^r\), its cell is

\[
 c_\varepsilon=\prod_{i=1}^r(P_i*E_i^{\varepsilon_i})
 \cong Q_{2r}.                                                     \tag{1.5}
\]

The \(2^r\) cells are disjoint and exhaust \(\Omega\). In block \(i\),
call the direction which flips the endpoint of \(P_i\) the reservoir
direction, and the direction which flips the endpoint of
\(E_i^{\varepsilon_i}\) the private direction. Thus every cell has
exactly \(r\) directions of each class.

## 2. The recursive block-affine menu

Let \(F_h\) be the recursive half-depth-rainbow neighbor permutation of
\(Q_h\), with the two directions in every rectangle block placed at one
bottom sibling pair of the recursion tree. We use the following proved
properties of \(F_h\).

1. Its cycles are isometric \(C_{2h}=C_{4r}\)'s.
2. For each \(q\le h/2=r\), the forward and reverse affine
   \(q\)-face maps are injective.
3. Every such \(q\)-window uses at most one direction from every bottom
   sibling pair.

Let

\[
 \mathcal G_r=\mathbb F_2^{2r}\rtimes(C_2\wr S_r)                  \tag{2.1}
\]

be the block-affine cube group. The translation part flips arbitrary
binary orientations. The wreath-product part permutes the \(r\) sibling
pairs and may interchange the two axes inside each pair. Every
\(g\in\mathcal G_r\) is a cube automorphism of the same physical cell, so
\(gF_hg^{-1}\) remains an exact physical cycle factor. The conjugate may
be selected independently in every \(c_\varepsilon\), because the cells
are owner-disjoint.

### Theorem 2.1 (exact context-dependent factor)

For every field

\[
 (g_\varepsilon:\varepsilon\in\mathbb F_2^r),\qquad
 g_\varepsilon\in\mathcal G_r,                                    \tag{2.2}
\]

the union of the factors \(g_\varepsilon F_hg_\varepsilon^{-1}\) is an
exact \(C_{4r}\)-factor of \(\Omega\). Every forward and reverse window
of length \(q\le r\) is block-simple and its affine face is unique among
starts in its own cell.

#### Proof

Conjugation preserves cycle lengths, isometry, and affine shadow
injectivity. It also sends bottom sibling pairs to bottom sibling pairs,
so the at-most-one-direction property is preserved. The cells in (1.5)
are disjoint and cover \(\Omega\), proving exact ownership. \(\square\)

This is the place where context dependence enters: no common direction
order, common recursive phase, or common conjugate is imposed on different
cells.

## 3. Exact density of a block-simple physical face

A block-simple affine \(q\)-face of one cell is specified by

* its \(q\) touched sibling pairs;
* one of the two axes in every touched pair; and
* the binary orientations on the \(2r-q\) untouched axes.

Consequently their number is

\[
 \binom rq2^q2^{2r-q}=\binom rq2^{2r}.                              \tag{3.1}
\]

The group \(\mathcal G_r\) is transitive on this set: \(S_r\) moves the
touched blocks, the \(C_2^r\) axis interchanges move the selected axes,
and translations move all outside orientations.

For either orientation and every \(q\le r\), the recursive factor selects
exactly \(2^{2r}\) distinct affine \(q\)-faces, one from every starting
vertex. Orbit averaging therefore gives the following statement.

### Theorem 3.1 (block-affine face density)

For every block-simple affine \(q\)-face \(R\) of a fixed cell,

\[
 {1\over|\mathcal G_r|}
 \#\{g\in\mathcal G_r:R\text{ is selected by }gF_hg^{-1}\}
 ={1\over\binom rq}.                                               \tag{3.2}
\]

The same identity holds for the reverse factor.

#### Proof

For a transitive finite group action, the average number of translates of
a fixed catalogue containing a fixed point equals the catalogue density.
The numerator catalogue has size \(2^{2r}\), while (3.1) is the orbit
size. Their ratio is (3.2). \(\square\)

Thus the recursive factor removes the run loss \(r-q+1\): the complete
context menu is exactly uniform on the literal block-simple affine faces.

## 4. Signed candidate-cell census

Consider a block-simple lower target. In a touched block there are two
possibilities.

* If the private direction is used, the surviving local target is one
  singleton \(p_i\in P_i\). It does not reveal whether the private pair
  was \(E_i^0\) or \(E_i^1\), so both cells are candidates.
* If the reservoir direction is used, the surviving local target is one
  singleton \(a_i\in A_i\). This letter belongs to exactly one of
  \(E_i^0,E_i^1\), so the cell is determined.

Every untouched local owner also determines its cell. Therefore, if
\(s\) of the \(q\) touched blocks are of the first kind, the number of
candidate cells is exactly

\[
                              d^-_{q,s}=2^s.                        \tag{4.1}
\]

This is the physical tensor rectangle carrier cube.

For an upper target the situation is different.

* A private move has local union
  \(E_i^{\varepsilon_i}\cup\{p_i\}\), which displays the whole private
  pair and hence \(\varepsilon_i\).
* A reservoir move has local union \(P_i\cup\{a_i\}\), and the displayed
  \(A_i\)-letter again determines \(\varepsilon_i\).

Thus

\[
                              d^+_{q,s}=1                            \tag{4.2}
\]

for every \(s\). Combining (3.2), (4.1), and (4.2) proves
(0.3)--(0.4).

This also explains the two-sided coordinate-star constraint: the lower
target forgets a private matching pair, while the corresponding upper
target records that pair in full. The lower carrier multiplicity cannot
simply be copied to the upper sign.

## 5. Exact target counts and the packet-local obstruction

Fix the touched block set \(I\in\binom{[r]}q\). For a lower type-\(s\)
target:

* choose the \(s\) private-move blocks in \(\binom qs\) ways;
* choose one of two \(P_i\)-singletons there;
* choose one of four \(A_i\)-singletons in every other touched block; and
* choose any of eight owners in every untouched block.

Hence

\[
 |\mathcal T^-_{r,q,s}|
 =\binom rq\binom qs2^s4^{q-s}8^{r-q}
 =V\binom rq\binom qs2^{-q-s}.                                  \tag{5.1}
\]

Summing over \(s\) gives

\[
 |\mathcal T^-_{r,q}|
 =\binom rq6^q8^{r-q}
 =V\binom rq\left({3\over4}\right)^q.                            \tag{5.2}
\]

For an upper type-\(s\) target, either local direction type has exactly
four possible local triples:
\(E_i^\varepsilon\cup\{p_i\}\) in the private case and
\(P_i\cup\{a_i\}\) in the reservoir case. Therefore

\[
 |\mathcal T^+_{r,q,s}|
 =\binom rq\binom qs4^q8^{r-q}
 =V\binom rq\binom qs2^{-q}.                                    \tag{5.3}
\]

After summing over \(s\),

\[
                         |\mathcal T^+_{r,q}|=V\binom rq.          \tag{5.4}
\]

### Theorem 5.1 (exact packet-local upper deficit)

Every context field (2.2) produces exactly \(V\) distinct upper targets in
\(\mathcal T^+_{r,q}\). Hence its internal uncovered set has cardinality
exactly (0.6).

#### Proof

Every start gives a block-simple upper target by Theorem 2.1. Such a
target determines its cell by (4.2). Within that cell, upper-shadow
injectivity recovers its unique start. Thus the packet-wide upper map is
injective and has image size \(V\). Equation (5.4) gives (0.6).
\(\square\)

For \(r=cq\), fixed \(c>1\), Stirling's formula gives

\[
 \binom{cq}{q}
 =(1+o(1))
 \sqrt{\frac{c}{2\pi(c-1)q}}
 \left(\frac{c^c}{(c-1)^{c-1}}\right)^q.                         \tag{5.5}
\]

Thus the packet-internal upper coverage fraction is exponentially small
at every fixed \(c>1\). Taking \(r=q\) repairs depth \(q\), but one factor
intended to serve all depths still has upper coverage fraction \(1/r\) at
depth one. In particular, \(r\ge H\to\infty\) forces packet-external
fusion already at \(q=1\).

## 6. The type-moment invariant

For a start \(x\), let \(s_q(x)\) be the number of private directions in
its forward \(q\)-window. Theorem 2.1 makes every such window block-simple.
Put

\[
                         E_{q,s}=|\{x:s_q(x)=s\}|.                  \tag{6.1}
\]

Every component is an isometric \(C_{4r}\), so its direction word is
\(\pi\pi\), where \(\pi\) contains each of the \(2r\) physical directions
once. Each of the \(r\) private directions occurs twice in the cyclic
word, and each occurrence belongs to exactly \(q\) forward \(q\)-windows.
Thus one component has \(2rq\) private-direction memberships among its
\(4r\) starts. Summing over all components and cells proves (0.7).

If \(s<q/2\), then

\[
 {qV\over2}=\sum_jjE_{q,j}
 \le sE_{q,s}+q(V-E_{q,s}),                                      \tag{6.2}
\]

which gives the first line of (0.8). If \(s>q/2\), then

\[
 {qV\over2}\ge sE_{q,s},                                         \tag{6.3}
\]

giving the third line. The middle line is trivial.

A type-\(s\) lower target can only be produced by a type-\(s\) start.
Therefore the number of distinct type-\(s\) lower targets supplied
internally is at most \(E_{q,s}\), and (5.1), (0.8) prove (0.10).

At \(q=1\), (0.7) forces

\[
                         E_{1,0}=E_{1,1}=V/2.                     \tag{6.4}
\]

A type-zero lower target identifies its cell, so these \(V/2\) outputs
are distinct. There are \(rV/2\) such targets by (5.1), proving the exact
deficit (0.11). This uses only maximum-isometric cycle structure, not a
direction-order catalogue.

## 7. The exact outer Hall cut

Let an owner-disjoint atlas of rectangle packets cover a set of middle
owners, and let \(\mathscr C\) be all its physical \(Q_{2r}\)-cells. Fix
a tagged depth and sign \(j=(q,\epsilon)\). For a physical target set
\(A\), let

\[
 f_{c,j}(A)
 =\#\{\text{block-simple affine \(q\)-faces of \(c\) whose trace lies
 in \(A\)}\}.                                                       \tag{7.1}
\]

For \(g\in\mathcal G_r\), let \(\mathcal S_j(c,g)\) be the set of
physical traces selected by the conjugated recursive factor in \(c\), and
put

\[
 \kappa_{c,j}(A)=\max_{g\in\mathcal G_r}
                     |\mathcal S_j(c,g)\cap A|.                   \tag{7.2}
\]

Cell shadow injectivity gives

\[
 \kappa_{c,j}(A)\le\min\{|c|,f_{c,j}(A)\}.                         \tag{7.3}
\]

For every deterministic context field, the number of distinct supplied
targets in \(A\) is at most \(\sum_c\kappa_{c,j}(A)\). Consequently

\[
 \boxed{
 M_j(A)\ge
 \left[|A|-\sum_{c\in\mathscr C}\kappa_{c,j}(A)\right]_+
 \ge
 \left[|A|-\sum_{c\in\mathscr C}
       \min\{|c|,f_{c,j}(A)\}\right]_+.}                           \tag{7.4}
\]

This is an invariant physical Hall obstruction. It permits arbitrary
cycle-dependent recursive orders and arbitrary context choices.

There is also an exact weighted fractional form. Allow one probability
distribution \(x_{c,g}\) on the menu of each cell and require expected
load at least one on every tagged target. Such a fractional field exists
if and only if

\[
 \boxed{
 \sum_T\alpha_T
 \le
 \sum_{c\in\mathscr C}
       \max_{g\in\mathcal G_r}
       \sum_{T\in\mathcal S_j(c,g)}\alpha_T
 \qquad(\alpha_T\ge0).}                                           \tag{7.5}
\]

Indeed, the possible fractional load vectors form the Minkowski sum of
the convex hulls of the cell incidence vectors. Separation from the
coordinatewise upper orthant of the all-one vector gives exactly (7.5);
the separating normal may be taken nonnegative because that orthant is
upward closed.

Average over the complete menus in (7.5). Theorem 3.1 gives the exact
barycentre

\[
 \lambda_j(T)
 ={1\over\binom rq}
   \#\{c:T\text{ is a block-simple \(q\)-trace candidate in }c\}. \tag{7.6}
\]

Inside one rectangle packet this specializes to (0.3)--(0.4). Hence
candidate-load lower tails control every fractional Hall weight, while
no macro-support census can replace (7.6).

To obtain (0.12), take a packet subfamily \(\mathscr B\) and

\[
 U_q^+(\mathscr B)
 =\bigcup_{P\in\mathscr B}\mathcal T^+_{P,q}.                     \tag{7.7}
\]

The cells belonging to \(\mathscr B\) have total owner mass
\(G_{\mathscr B}\), so they supply at most \(G_{\mathscr B}\) distinct
members of (7.7). Apply (7.4) to all remaining cells. This proves (0.12).

For one packet \(P\), (0.12) reads

\[
 M_q^+\ge
 \left[
  \left(\binom rq-1\right)V
  -\sum_{c\notin P}
       \min\{|c|,f^+_{c,q}(\mathcal T^+_{P,q})\}
 \right]_+.                                                       \tag{7.8}
\]

Thus every packet needs an explicit exterior rescue of its
\((\binom rq-1)V\) internally absent upper targets. Overlaps among the
sets \(\mathcal T^+_{P,q}\) may allow one exterior target occurrence to
serve several packet requests; exactly that overlap is retained by the
union and candidate terms in (0.12). Ignoring it would double-count the
outer carrier.

## 8. Relation to the macroprofile flow and exact boundary

The explicit macroprofile flow

\[
 F_{k,\ell}
 ={V_k\over\binom mq}\prod_j\binom{k_j}{\ell_j}                    \tag{8.1}
\]

records the allowed predecessor marginals. On a lower type-\(s\)
rectangle target, the \(s\) forgotten private matching choices form the
literal \(2^s\)-vertex predecessor cube. This is exactly the factor
\(2^s\) in (0.3). The recursive context menu independently contributes
the face density \(1/\binom rq\). Their product is the exact joined
kernel, not a heuristic tensor product.

For the upper trace none of those private choices is forgotten: the union
contains the whole chosen private pair. Therefore the predecessor cube
collapses to one point and gives (0.4). Sectorwise flow balance does not
encode this signed physical identification.

What is proved here is:

1. a literal owner-one recursive factor with independently chosen
   context orders in every rectangle cell;
2. exact removal of the fixed-order run loss;
3. the exact lower and upper physical carrier kernels (0.3)--(0.4);
4. an order-independent packet-local upper deficit and type-moment
   obstruction; and
5. the precise exterior weighted Hall cut which must be verified or
   violated by a global packet atlas.

The exterior inequality is not proved for a general redesigned atlas, nor
is an integral rounding theorem after its fractional version. For the
canonical first-\(r\) atlas, however, the separate chronology audit proves
that the inequality fails by \(\Theta_A(W)\) at one upper Gaussian depth.
Hence no coefficient-one conclusion is asserted. The remaining
constructive statement is now exact: alter the packet chronology itself so
that the unions in (7.7) acquire enough outside candidate-cell capacity to
satisfy (7.5) simultaneously at both signs and all depths. The lower
macroprofile flow alone cannot supply that theorem.
