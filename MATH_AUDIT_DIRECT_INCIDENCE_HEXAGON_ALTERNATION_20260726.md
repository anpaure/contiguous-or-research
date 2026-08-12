# Direct incidence hexagons: exact census, prescribed alternation, and the physical splice gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let \(r\ge2\), let \(J=[2r]\),

\[
 \mathcal X=\binom Jr,\qquad
 \mathcal Y=\binom J{r+1}.
\]

For \(K\in\binom J{r-1}\) and a three-set
\(\{a,b,c\}\subset J\setminus K\), define the incidence hexagon

\[
 H(K;a,b,c)=
 \{K+a,K+b,K+c;\ K+ab,K+bc,K+ca\}.
\tag{0.1}
\]

The unrestricted six-uniform hypergraph of these hexagons has exact
degrees

\[
 \boxed{
 D_X=r\binom r2={r^2(r-1)\over2},\qquad
 D_Y=(r-1)\binom{r+1}2={r(r+1)(r-1)\over2}.}
\tag{0.2}
\]

Its maximum pair codegree is

\[
 \boxed{\Delta_2=r(r-1),}
\tag{0.3}
\]

attained by an incident pair \(X\subset Y\).  Thus
\(\Delta_2/D_X=2/r\), and the unrestricted geometric hypergraph is in the
small-relative-codegree regime.

This does not imply a large alternating packing relative to a prescribed
incidence matching \(M\).  For every core \(K\), define a directed graph
\(D_K(M)\) on \(J\setminus K\) by

\[
                         a\longrightarrow b
 \quad\Longleftrightarrow\quad
                 (K+a,K+ab)\in M.
\tag{0.4}
\]

Then \(H(K;a,b,c)\) is \(M\)-alternating if and only if
\(a,b,c\) form a directed 3-cycle in \(D_K(M)\), in one of the two
orientations.  Consequently

\[
 \boxed{
 A(M)=\sum_{K\in\binom J{r-1}}
       \#\{\text{directed 3-cycles of }D_K(M)\}}
\tag{0.5}
\]

is the exact number of alternating hexagons.

There is no lower bound on \(A(M)\) from the size of \(M\) alone.  Fix
\(z\in J\) and take

\[
 M_z=\{(X,X+z):X\in\binom{J\setminus\{z\}}r\}.
\tag{0.6}
\]

This is a matching of size

\[
                         |M_z|=\binom{2r-1}r
                         ={1\over2}\binom{2r}r,
\tag{0.7}
\]

but every arc in every \(D_K(M_z)\) points toward \(z\), so
\(A(M_z)=0\).

There is an exact conditional packing statement.  If \(A(M)\) alternating
hexagons exist, every lower or upper vertex lies in at most \(r\) of them.
Consequently greedy selection gives a vertex-disjoint family of size

\[
 \boxed{
 \nu_6(M)\ge
 {A(M)\over6r-5}.}
\tag{0.8}
\]

Since the total number of geometric hexagons is

\[
 |\mathcal H_6|
 =\binom{2r}{r-1}\binom{r+1}3
 =\binom{2r}r\,{r^2(r-1)\over6},
\tag{0.9}
\]

the natural triangle-density hypothesis
\(A(M)\ge\eta|\mathcal H_6|/r^2\) implies

\[
                         \nu_6(M)\ge
 {\eta(r-1)\over6(6r-5)}\binom{2r}r
 =\left({\eta\over36}+o(1)\right)\binom{2r}r.
\tag{0.10}
\]

The scale \(|\mathcal H_6|/r^2\) is the right one.  Each core digraph has
only \(r+1\) vertices and its directed 3-cycles are vertex-disjoint, so

\[
 A(M)\le
 \binom{2r}{r-1}\left\lfloor{r+1\over3}\right\rfloor
 =O(|\mathcal H_6|/r^2).
\tag{0.11}
\]

Also \(3A(M)\le |M|r\), since every alternating hexagon uses three
matched lower vertices and each such vertex lies in at most \(r\)
alternating hexagons.

Thus an \(\Omega\bigl(\binom{2r}r\bigr)\) alternating packing follows
from a positive directed-triangle density at its natural scale, not from
the unrestricted degree/codegree census.

Even (0.10) is initially only an abstract matching or \(b\)-factor
certificate.  To be a physical equal-length path splice, each hexagon
must pass the strand test.  A clean hexagon needs three distinct paths,
coherent orientations, and equal cut phases.  It then gives an
equal-length twisted path cover with a 3-cycle endpoint permutation, not
an anchored port factor.  Three switch-stable serial copies with the same
transported 3-cycle can restore the ports.  A fixed-exterior \(r\)-step
local slab cannot realize the nonidentity twist at all; an exterior-moving
seam is necessary.  Moreover, a vertex-disjoint family of hexagons need
not be strand-disjoint: two members can cut different edges of the same
old path, in which case their simultaneous lift requires one global
strand calculation.

The geometric hypergraph, the alternating subhypergraph, the abstract
path-splice subhypergraph, and the physically aligned port-conveyor
subhypergraph are therefore four strictly different objects.  The exact
degrees (0.2) and codegrees (0.3) belong only to the first.

## 1. Edge count and vertex degrees

An edge is determined uniquely by its common lower core \(K\) and its
unordered petal triple \(T=\{a,b,c\}\).  Since
\(|J\setminus K|=r+1\),

\[
 |\mathcal H_6|=\binom{2r}{r-1}\binom{r+1}3.
\tag{1.1}
\]

### Proposition 1.1 (lower degree)

Every \(X\in\mathcal X\) has degree

\[
                         d(X)=r\binom r2.
\tag{1.2}
\]

#### Proof

If \(X=K+a\), then \(K=X-a\).  There are \(r\) choices of
\(a\in X\).  The two other petals must be chosen from
\(J\setminus X\), which has size \(r\).  This gives
\(r\binom r2\), and the core recovers the representation uniquely.
\(\square\)

### Proposition 1.2 (upper degree)

Every \(Y\in\mathcal Y\) has degree

\[
                         d(Y)=(r-1)\binom{r+1}2.
\tag{1.3}
\]

#### Proof

If \(Y=K+ab\), choose the unordered pair
\(\{a,b\}=Y\setminus K\) in \(\binom{r+1}2\) ways.  The third petal
\(c\) must lie outside \(Y\), giving \(2r-(r+1)=r-1\) choices.
\(\square\)

As checks, every hyperedge contains three vertices of each shore, and

\[
 {|\mathcal X|D_X\over3}
 ={|\mathcal Y|D_Y\over3}=|\mathcal H_6|.
\tag{1.4}
\]

The hypergraph is biregular, not regular; \(D_Y/D_X=(r+1)/r\).

## 2. Exact pair codegrees

### Theorem 2.1 (complete codegree table)

For distinct vertices:

1. If \(X,X'\in\mathcal X\), then

   \[
   \lambda(X,X')=
   \begin{cases}
   r-1,&|X\cap X'|=r-1,\\
   0,&\text{otherwise}.
   \end{cases}
   \tag{2.1}
   \]

2. If \(Y,Y'\in\mathcal Y\), then

   \[
   \lambda(Y,Y')=
   \begin{cases}
   r,&|Y\cap Y'|=r,\\
   0,&\text{otherwise}.
   \end{cases}
   \tag{2.2}
   \]

3. For \(X\in\mathcal X,Y\in\mathcal Y\),

   \[
   \lambda(X,Y)=
   \begin{cases}
   r(r-1),&X\subset Y,\\
   1,&|X\cap Y|=r-1,\\
   0,&\text{otherwise}.
   \end{cases}
   \tag{2.3}
   \]

In the second line of (2.3), \(X\not\subset Y\) automatically.

#### Proof

Two lower petals in one hexagon share its unique core
\(K=X\cap X'\).  Once their two new labels are fixed, the third may be
any element outside \(X\cup X'\), a set of size \(r-1\).  This proves
(2.1).

If two upper vertices share a hexagon, they have the form
\(K+ab,K+bc\), so their intersection is \(K+b\) of size \(r\).  Conversely
let \(R=Y\cap Y'\) have size \(r\).  Choose the shared petal
\(b\in R\), put \(K=R-b\), and use the two labels in
\(Y\setminus Y'\) and \(Y'\setminus Y\) as the other petals.  Every
\(b\in R\) gives one distinct hexagon, proving (2.2).

Suppose \(X\subset Y\), say \(Y=X+b\).  Choose
\(a\in X\), put \(K=X-a\), and choose the third petal outside \(Y\).
There are \(r(r-1)\) choices.  If \(|X\cap Y|=r-1\), then the intersection
is the core and \(X\cup Y\) determines all three petals, so there is one
hexagon.  The set geometry excludes every remaining case. \(\square\)

This proves (0.3), and the maximum is attained for every incident pair
\(X\subset Y\).

## 3. Prescribed alternation is a directed-triangle condition

Let \(M\) be any matching in the incidence graph
\((\mathcal X,\mathcal Y;\subset)\).  A hexagon has two cyclic perfect
matchings.  It is \(M\)-alternating when one of these three-edge sets is
contained in \(M\).

### Theorem 3.1 (directed triangle equivalence)

For fixed \(K\), define \(D_K(M)\) by (0.4).  Then
\(H(K;a,b,c)\) is \(M\)-alternating exactly when

\[
                         a\to b\to c\to a
\tag{3.1}
\]

or the reverse directed cycle occurs in \(D_K(M)\).

#### Proof

One cyclic half of the hexagon is

\[
 (K+a,K+ab),\quad(K+b,K+bc),\quad(K+c,K+ca),
\tag{3.2}
\]

which is precisely the three arcs in (3.1).  The other half gives the
reverse cycle.  Since \(M\) is a matching, it cannot contain both halves.
\(\square\)

For each fixed \(K\), every vertex of \(D_K(M)\) has outdegree at most
one: the lower vertex \(K+a\) is incident with at most one edge of \(M\).
Thus its directed cycles are vertex-disjoint, and its directed 3-cycles
are exactly the alternating hexagons on core \(K\).  Formula (0.5) and
the upper bound (0.11) follow.

### Proposition 3.2 (large triangle-free prescribed matching)

The matching \(M_z\) in (0.6) has no alternating hexagon.

#### Proof

For a matched edge \(X\to X+z\), every representation
\(X=K+a\) gives the arc \(a\to z\).  Hence every directed edge in every
\(D_K(M_z)\) points to \(z\), and no directed cycle exists. \(\square\)

This refutes any theorem asserting that positive matching density alone
forces a positive density of alternating \(C_6\)'s.

### Remark 3.3 (the saturated-layer qualification)

The example \(M_z\) does not saturate \(\mathcal Y\), and it cannot be
extended to one that does: every \((r+1)\)-set avoiding \(z\) has all of
its lower neighbours among the \(r\)-sets avoiding \(z\), all of which
are already used by \(M_z\).

Therefore, if the application assumes that the prescribed matching
saturates every upper vertex, Proposition 3.2 alone is not a
counterexample.  But saturation still gives no *local* triangle forcing.
Indeed, every matched incidence contributes one arc to \(D_K(M)\) for
each of its \(r\) lower subcores, so

\[
 \sum_{K\in\binom J{r-1}}e(D_K(M))
 =r|M|=r\binom{2r}{r+1}.
\tag{3.3}
\]

Since \(\binom{2r}{r+1}=\binom{2r}{r-1}\), a saturated matching has
exactly \(r\) arcs per core on average, on a vertex set of size \(r+1\).
A functional digraph with \(r\) arcs on \(r+1\) vertices can be a
triangle-free directed forest.  Thus any theorem forcing many triangles
for saturated matchings must exploit compatibility between different
cores; neither saturation nor the one-core edge count proves it.

## 4. Conditional alternating packing

Let \(\mathcal A_6(M)\) be the six-uniform hypergraph of
\(M\)-alternating hexagons.  The matching condition improves its maximum
degree from cubic to linear.

### Proposition 4.1 (linear alternating degree)

Every vertex of \(\mathcal A_6(M)\) has degree at most \(r\).

#### Proof

Let \(X\in\mathcal X\).  If \(X\) is unmatched, no alternating hexagon
contains it.  Otherwise write its unique matched edge as
\(X\subset X+b\).  In an alternating hexagon containing \(X\), that edge
must be the selected edge incident with \(X\).  Choose the petal
\(a\in X\) for which \(K=X-a\).  In \(D_K(M)\), the selected edge is the
arc \(a\to b\).  Because outdegree is at most one, this arc lies in at
most one directed 3-cycle.  There are \(r\) choices of \(a\), so
\(d_{\mathcal A}(X)\le r\).

The same argument applies to \(Y\in\mathcal Y\).  If its unique matched
edge is \(Y-b\subset Y\), choose \(a\in Y-b\), put
\(K=Y-\{a,b\}\), and again observe that the arc \(a\to b\) belongs to
at most one directed 3-cycle.  Thus \(d_{\mathcal A}(Y)\le r\).
\(\square\)

### Proposition 4.2 (greedy packing)

\[
                         \nu(\mathcal A_6(M))
 \ge {|\mathcal A_6(M)|\over6r-5}.
\tag{4.1}
\]

#### Proof

One selected hexagon meets at most

\[
                         6(r-1)
\]

other alternating hexagons, by Proposition 4.1 and summing over its six
vertices.  Including the selected edge itself, greedy selection deletes
at most \(6r-5\) candidates per chosen edge. \(\square\)

Substitution of (0.9) gives (0.10).  This is a hand-proof linear packing
theorem under the exact directed-triangle density hypothesis.

The unrestricted small-codegree census does not transfer to
\(\mathcal A_6(M)\): after imposing \(M\), neither degree regularity nor
even nonemptiness survives without a new triangle theorem.

## 5. Abstract matching and \(b\)-factor switches

Suppose \(H\) is \(M\)-alternating.  Replacing its three \(M\)-edges by
the opposite cyclic half gives another matching on the same six vertices.
Vertex-disjoint alternating hexagons can therefore be toggled
simultaneously, preserving the cardinality and all matching degrees.

If \(M\) is only one incidence layer of a degree-two \(b\)-factor \(F\),
this is insufficient.  The three inserted edges must also be absent from
the other incidence layer of \(F\); otherwise the six-cycle is not
\(F\)-alternating.  Even when all six degree equations are preserved, the
toggle may create

* an internal cycle component;
* a path with two roots;
* a path with two barred endpoints; or
* a nonidentity endpoint permutation.

These are invisible to the local matching ledger.  The full strand
diagram, recording every cut segment and the root/sink type of both of
its ends, is necessary and sufficient for an abstract path-cover switch.

There is a second completion distinction.  If one first prescribes one
cyclic half on a geometric hexagon packing and then asks for a global
incidence matching containing those edges, the residual graph must still
satisfy Hall.  Vertex-disjointness of the hexagons does not imply those
Hall inequalities.

There is also a quotient-to-ambient edge gate.  The six displayed
vertices give literal ambient Hasse edges after adjoining one common
exterior \(O\): for example the new edge is exactly

\[
 (O\cup K+a,\ O\cup K+ab).
\tag{5.1}
\]

If the six quotient states have instead been represented with different
top, box, or collar tags, equality of their local masks does not create
this ambient edge.  Every proposed lift must identify the exterior on
both ends of each of the three deleted and three inserted edges before
the strand calculation even begins.

## 6. Clean equal-length strand splices

Orient every old path from its Dyck root to its barred endpoint.  Suppose
an alternating hexagon's three selected edges lie on three distinct paths.
Let their orientations along those paths be
\(\epsilon_a,\epsilon_b,\epsilon_c\in\{+,-\}\), and let their phases be
\(t_a,t_b,t_c\), where a phase is the number of incidence edges before
the selected edge on its oriented old path.

### Theorem 6.1 (clean physical splice)

The toggle is a root-to-barred-endpoint path cover if and only if

\[
                         \epsilon_a=\epsilon_b=\epsilon_c.
\tag{6.1}
\]

When this holds, it permutes the three old suffixes by a 3-cycle.  If all
old paths have common incidence-edge length \(L\), the three new paths
have lengths

\[
 L+t_b-t_a,\qquad L+t_c-t_b,\qquad L+t_a-t_c
\tag{6.2}
\]

up to cyclic reversal.  Hence every new path still has length \(L\) if
and only if

\[
                         t_a=t_b=t_c.
\tag{6.3}
\]

#### Proof

Deleting the three selected edges leaves one root prefix and one barred
suffix on each path.  A new hexagon edge joins a prefix to a suffix
exactly when adjacent selected edges have the same orientation.  This
gives (6.1).  In the all-positive orientation, the deleted edges are

\[
 K+a\to K+ab,\qquad K+b\to K+bc,\qquad K+c\to K+ca,
\tag{6.4}
\]

and the inserted half is

\[
 K+b\to K+ab,\qquad K+c\to K+bc,\qquad K+a\to K+ca.
\tag{6.5}
\]

Thus the exact chronological reconnections are

\[
 \operatorname{pref}(b)\to\operatorname{suf}(a),\qquad
 \operatorname{pref}(c)\to\operatorname{suf}(b),\qquad
 \operatorname{pref}(a)\to\operatorname{suf}(c).
\tag{6.6}
\]

Their lengths, in that order, are the three quantities in (6.2).
The all-negative case reverses the cycle.  All three differences vanish
exactly under (6.3). \(\square\)

Thus a same-phase clean alternating hexagon is an equal-length twisted
path switch.  Hypergraph vertex-disjointness does not imply the three
distinct-strand condition, common orientation, or common phase.

For a family of switches, checking this theorem member by member is
sufficient only if no old path is cut by two different members.  Without
that strand-disjointness, delete all selected edges at once and inspect
the single global reconnection graph; local 3-cycle endpoint actions can
interlace and need not compose as disjoint permutations.

### Corollary 6.2 (not yet an anchored port factor)

One clean switch right-composes the endpoint pairing by a nontrivial
3-cycle \(\tau\).  Therefore it does not preserve the complementary port
pairing.

Three switch-stable serial stages can restore it algebraically:

\[
                              \tau^3=1.
\tag{6.7}
\]

For a physical port factor, the stages must act successively on the same
transported labels, every seam and crossing collar must have an exact
owner, and the carrier charts must remain coherent.  Three independent
recursive holes act tensorially and do not realize \(\tau^3\).

## 7. Folded strand splices

If two selected hexagon edges lie on one old path and the third on another,
cycle length no longer determines the endpoint action.  For the legal
sign pattern \(+,-,+\), in cyclic order, the toggle is a transposition of
the two path suffixes.

Let the two cuts on path \(A\) occur at phases \(t_0<t_1\), and the cut on
path \(B\) occur at phase \(t_2\).  If both old paths have common
incidence-edge length \(L\), the new path lengths are

\[
                         L+t_0-t_2,\qquad L+t_2-t_0.
\tag{7.1}
\]

More explicitly, write \(L_i,R_i\) for the root-side and sink-side ends
of the cut \(e_i\).  For the chronological/sign pattern above, the three
inserted edges pair

\[
                         R_0R_1,\qquad L_1L_2,\qquad R_2L_0.
\tag{7.2}
\]

The first new path is the root prefix of \(A\), then \(L_0R_2\), then
the sink suffix of \(B\).  The second is the root prefix of \(B\), then
\(L_2L_1\), the middle segment of \(A\), then \(R_0R_1\), then the sink
suffix of \(A\).  This gives (7.1) and shows directly why \(t_1\)
cancels.

Thus this folded transposition is equal-length exactly when

\[
                              t_0=t_2.
\tag{7.3}
\]

The internal phase \(t_1\) cancels between the middle and final segments.
Other sign/order patterns may act trivially, or create an internal cycle
or wrong endpoint types; only the full strand diagram decides.

One folded transposition again breaks complementary port pairing.  Two
coherent serial stages can restore it, but require the same exterior and
carrier checks as Corollary 6.2.

## 8. Fixed-exterior metric obstruction

Suppose a nominal local slab has fixed exterior \(O\), local coordinates
\(J\), and \(r\) Johnson steps.  A clean hexagon twist sends the row
entering at \(O\cup P\) to

\[
                         O\cup(J\setminus\tau(P)).
\tag{8.1}
\]

Their Johnson distance is

\[
                         |P\cap\tau(P)|<r
\tag{8.2}
\]

for every moved port.  A contiguous \(r\)-step segment of a minimum
wreath must have endpoint distance \(r\).  Hence a nonidentity hexagon
twist cannot be installed as an ordinary fixed-exterior local port slab.

If the left and right exteriors are \(O_L,O_R\), put
\(e=|O_L\setminus O_R|\).  The necessary metric equation becomes

\[
                         e+|P\cap\tau(P)|=r,
\qquad\text{or equivalently}\qquad
                         e=|P\setminus\tau(P)|.
\tag{8.3}
\]

The same \(e\) must work for every moved port in the packet.  An
exterior-moving conveyor must additionally prove its complete state,
adjacent-union, seam, and crossing-collar ledgers.

## 9. Decision for constant one

The unrestricted incidence-hexagon hypergraph has excellent geometric
packing parameters, and a positive directed-triangle density at the
natural \(|\mathcal H_6|/r^2\) scale gives an
\(\Omega\bigl(\binom{2r}r\bigr)\) alternating packing by (0.8).
But an arbitrary prescribed matching can have no alternating hexagons at
all, even at density one half.

Furthermore, an alternating packing is not automatically a packing of
physical switches:

1. the prescribed halves must extend to the intended global matching or
   \(b\)-factor;
2. every hexagon must pass the clean or folded strand test;
3. a family must be strand-disjoint, or pass one global reconnection test;
4. equal path length requires the phase equations (6.3) or (7.3);
5. one switch has nontrivial monodromy and is not an anchored port factor;
6. serial finite-order closure needs transported labels and exact seams;
7. fixed-exterior local realization is metrically impossible for a moved
   port.

Thus the exact missing theorem is a degree/triangle lower bound not in the
geometric hexagon hypergraph, but in the much smaller subhypergraph of
completion-compatible, strand-admissible, synchronized,
exterior-moving hexagons.  No such lower bound follows from the census
proved here.
