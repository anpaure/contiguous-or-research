# Cartesian caps, positional flags, and the exact seam-mixing gate

## 1. Outcome

Cutting a pointed wreath at its distinguished omitted coordinate turns it
into a complementary path in the middle-levels graph.  Complementary paths
have a natural Cartesian concatenation.  This gives a clean candidate for
lifting a wreath trade after adding any even number of coordinates.

The candidate has an exact obstruction.  The old first shadow splits into
four positional flags

\[
                       L, \qquad U, \qquad E_0, \qquad E_1.
\]

Equality of the old unpointed first shadow separates (U), but only sees
the sum (L+E_0+E_1).  An ordinary Cartesian cap decorates (L,E_0,E_1)
with three distinguishable cap sections.  Hence it preserves the lifted
first shadow only when the positional flags agree separately.

This proves an **all-cap obstruction**, not merely a failed two-coordinate
experiment.  For the certified four-for-four Haar trade at (m=4), the
middle-support endpoint condition can be met exactly at distinguished
coordinates (z=3,4,6), but the positional flags fail for every compatible
orientation.  At every other (z), middle support already fails.  Therefore
no unchanged-completion ordinary Cartesian cap of any dimension lifts that
trade.

The obstruction also identifies the correct escape.  A general monotone
shuffle through the product grid decorates each old (L)-flag by a chosen
lower vertex of the cap path.  In particular, a bottom--top split shuffle
can give internal (L)-flags exactly the two decorations carried by
(E_1) and (E_0).  The remaining problem is an integral, sealed
grid-rerouting theorem.  Section 8 states that gate precisely.

## 2. From a pointed wreath to a complementary path

Let (X) have size (2m), and let (z\notin X).  A wreath on
(X\cup\{z\}), cut at its unique edge whose omitted coordinate is (z),
becomes a saturated path

\[
 P=(x_0,y_0,x_1,y_1,\ldots,y_{m-1},x_m)             \tag{2.1}
\]

in the two middle levels of (2^X), where

\[
 |x_i|=m, \qquad |y_i|=m+1, \qquad
 x_i\subset y_i\supset x_{i+1}, \qquad
 x_m=X\setminus x_0.                                \tag{2.2}
\]

The two orientations of the cut wreath give the two orientations of this
path.  Conversely, (2.1)--(2.2) has (2m) edges and its endpoints differ
in all (2m) coordinates.  Every coordinate is therefore flipped exactly
once, and adjoining the closing coordinate (z) recovers a wreath.

If an exact wreath factor is cut at (z), the resulting paths partition
the two middle levels of (2^X).  Indeed, an old middle set not containing
(z) maps to itself in rank (m), while one containing (z) maps to the
complement in (X) of its non-(z) part, in rank (m+1).

For a path (P), write

\[
 r(P)=x_0, \qquad t(P)=x_m=\overline{x_0}, \qquad
 V(P)=\{x_0,y_0,\ldots,y_{m-1},x_m\}.               \tag{2.3}
\]

## 3. Ordinary Cartesian concatenation

Let (Y) have size (2s), disjoint from (X), and let

\[
 Q=(u_0,v_0,u_1,v_1,\ldots,v_{s-1},u_s)             \tag{3.1}
\]

be a complementary path on (Y).  Define (P\star Q) by first traversing
(P) while (Q) stays at (u_0), and then traversing (Q) while (P)
stays at (x_m):

\[
\begin{aligned}
P\star Q={}&(x_0u_0,y_0u_0,x_1u_0,\ldots,
             y_{m-1}u_0,x_mu_0,\\
            &\hspace{34mm}x_mv_0,x_mu_1,\ldots,
             x_mv_{s-1},x_mu_s).
                                                               \tag{3.2}
\end{aligned}
\]

Here juxtaposition denotes disjoint union.  This is a complementary path
on (X\sqcup Y), so closing it with the same distinguished coordinate
(z) gives a wreath in dimension (2(m+s)+1).

If (\mathcal P,\mathcal Q) are vertex-disjoint path packings, then

\[
             \mathcal P\star\mathcal Q
             =\{P\star Q:P\in\mathcal P,Q\in\mathcal Q\}          \tag{3.3}
\]

is also a path packing.  Its middle support is the disjoint union

\[
\boxed{
 V(\mathcal P\star\mathcal Q)
 =\bigl(V(\mathcal P)\boxplus R(\mathcal Q)\bigr)
  \;\dot\cup\;
  \bigl(T(\mathcal P)\boxplus
        (V(\mathcal Q)\setminus R(\mathcal Q))\bigr),}             \tag{3.4}
\]

where

\[
 R(\mathcal Q)=\{u_0(Q):Q\in\mathcal Q\}, \qquad
 T(\mathcal P)=\{x_m(P):P\in\mathcal P\},                         \tag{3.5}
\]

and (\boxplus) means all disjoint unions of one set from each family.

The two terms in (3.4) cannot intersect.  A root of one cap path cannot be
a non-root vertex of another path in the same packing.

### Proposition 3.1 (exact endpoint condition)

Suppose (\mathcal P^-) and (\mathcal P^+) are path packings with the
same middle support, and (\mathcal Q) is nonempty with (s\ge1).  Then

\[
 V(\mathcal P^-\star\mathcal Q)
 =V(\mathcal P^+\star\mathcal Q)
 \quad\Longleftrightarrow\quad
 T(\mathcal P^-)=T(\mathcal P^+)                    \tag{3.6}
\]

as multisets.

#### Proof

The first terms in (3.4) agree by hypothesis.  Equality of the terminal
sets makes the second terms agree.  Conversely, fix any non-root vertex
(q\in V(\mathcal Q)\setminus R(\mathcal Q)).  The targets whose
(Y)-section is (q) in the second term of (3.4) recover the multiset
(T(\mathcal P)), and no target from the first term has that section.
\(\square\)

Thus an ordinary product lift first requires an oriented endpoint/root
compatibility condition.  Completion of the resulting packing to a full
path factor is a separate issue.

## 4. The four positional first-shadow flags

For (2.1), define the multisets

\[
\begin{aligned}
 L(P)&=\{x_i\cap x_{i+1}:0\le i<m\},\\
 U(P)&=\{X\setminus(y_{i-1}\cup y_i):1\le i<m\},\\
 E_0(P)&=X\setminus y_0,\\
 E_1(P)&=X\setminus y_{m-1}.                         \tag{4.1}
\end{aligned}
\]

The rank-((m-1)) cyclic intervals of the corresponding wreath are
exactly

\[
 \boxed{
 B_{m-1}(P)
 =L(P)\;\dot\cup\;\{E_0(P),E_1(P)\}
  \;\dot\cup\;\{z\cup A:A\in U(P)\}.}             \tag{4.2}
\]

This follows either by tracing the cyclic intervals, or by intersecting
the appropriate distance-two vertices of the odd cycle.  Formula (4.2)
contains the key distinction:

* targets containing (z) determine (U) separately;
* targets avoiding (z) see only the aggregate (L+E_0+E_1).

Consequently, for two old trades with equal (B_{m-1}),

\[
 \Delta U=0, \qquad
 \Delta L+\Delta E_0+\Delta E_1=0,                  \tag{4.3}
\]

but none of (Delta L,Delta E_0,Delta E_1) need vanish separately.

Path reversal leaves (L) and (U) unchanged and exchanges (E_0,E_1).
Thus reversal averaging can merge the two endpoint flags, but it can never
merge (L) with an endpoint flag.  In particular, it cannot remove a
nonzero (L)-versus-endpoint defect.

## 5. Exact first shadow of an ordinary product

Let

\[
\begin{aligned}
L(Q)&=\{u_j\cap u_{j+1}:0\le j<s\},\\
U(Q)&=\{Y\setminus(v_{j-1}\cup v_j):1\le j<s\},\\
E_0(Q)&=Y\setminus v_0, \qquad
E_1(Q)=Y\setminus v_{s-1}.                           \tag{5.1}
\end{aligned}
\]

Substitution of (3.2) into (4.2), now on (X\sqcup Y), gives

\[
\boxed{
\begin{aligned}
B_{m+s-1}(P\star Q)= {}&
 \{A\cup u_0:A\in L(P)\}\\
&\dot\cup\{x_m\cup B:B\in L(Q)\}\\
&\dot\cup\{E_0(P)\cup\overline{u_0},
             x_0\cup E_1(Q)\}\\
&\dot\cup\{z\cup A\cup\overline{u_0}:A\in U(P)\}\\
&\dot\cup\{z\cup E_1(P)\cup E_0(Q)\}\\
&\dot\cup\{z\cup x_0\cup B:B\in U(Q)\}.
                                                               \tag{5.2}
\end{aligned}}
\]

Every union in (5.2) is disjoint across coordinate blocks, not necessarily
as a multiset of targets.  The formula itself is an equality of multisets.

### Theorem 5.1 (all-cap flag obstruction)

Let (\mathcal P^-,\mathcal P^+) be two old path packings satisfying

1. equal old middle support;
2. equal old rank-((m-1)) wreath shadow; and
3. equal oriented terminal multiset (T(\mathcal P^-)=T(\mathcal P^+)).

Let (\mathcal Q) be any nonempty complementary-path packing on (2s)
coordinates, (s\ge1).  Then

\[
 B_{m+s-1}(\mathcal P^-\star\mathcal Q)
 =B_{m+s-1}(\mathcal P^+\star\mathcal Q)            \tag{5.3}
\]

if and only if

\[
                 \Delta L=0, \qquad \Delta E_0=0.     \tag{5.4}
\]

Under the old-shadow hypothesis these two equations also force
(Delta E_1=0); (Delta U=0) already follows from the (z)-section.

#### Proof

Sufficiency follows term by term from (5.2), (4.3), and equality of the
oriented roots and terminals.

For necessity, the root set of a complementary-path packing contains no
complementary pair.  Indeed, if (u_0) is a root then
(overline{u_0}=u_s) is already the other endpoint of the same path and
cannot occur in another vertex-disjoint path.

Fix a cap root (R=u_0(Q)).  Among the targets in (5.2) which avoid (z),
have (X)-rank (m-1), and have (Y)-section (R), only the first line
can occur.  Therefore equality of the product shadows gives
(Delta L=0).

Now inspect targets avoiding (z), with (X)-rank (m-1), and
(Y)-section (overline R).  Since no cap root equals (overline R),
only the (E_0(P)\cup\overline{u_0}) term can occur.  Hence
(Delta E_0=0).  Equation (4.3) gives (Delta E_1=0), completing the
proof. \(\square\)

The theorem is independent of the size or internal structure of the cap.
Adding more Cartesian coordinates does not average away the obstruction;
it merely tensors each old positional flag with a different cap section.

## 6. Audit of the certified (m=4) Haar trade

Apply the cut construction to the two four-wreath sides in
`NONLOCAL_HAAR_M4.md`.  The exact audit in
`audit_haar_cartesian_flags.cpp` gives:

* the unoriented endpoint-pair multisets agree exactly for
  (z=3,4,6);
* they disagree for (z=1,2,5,7,8,9);
* for each of (z=3,4,6), there are exactly (16) pairs of orientation
  assignments with equal terminal multisets;
* over every such compatible pair, the positional flags fail; the minimum
  symmetric-difference counts are

\[
        (\lvert\Delta L\rvert,
         \lvert\Delta U\rvert,
         \lvert\Delta E_0\rvert,
         \lvert\Delta E_1\rvert)=(4,0,2,2).          \tag{6.1}
\]

For one minimizing orientation pair, negative-only (L)-witnesses are

\[
 \{2,4,6\}\quad(z=3), \qquad
 \{1,3,8\}\quad(z=4), \qquad
 \{1,3,4\}\quad(z=6).                              \tag{6.2}
\]

The old first shadow is nevertheless equal: the four (L)-discrepancies
cancel against the two endpoint discrepancies on each side, exactly as
(4.3) permits.

### Corollary 6.1

Keep the ten common completion wreaths identical on the two sides of the
certified (m=4) factors.  Choose any distinguished old coordinate, any
orientations, any cap dimension (s\ge1), and any complementary cap path
packing (\mathcal Q).  Replacing every changed old path by its ordinary
Cartesian products with (\mathcal Q) cannot give a lifted trade preserving
the new middle and first-lower rows.

For (z\notin\{3,4,6\}), Proposition 3.1 fails.  For
(z\in\{3,4,6\}), Theorem 5.1 and (6.1) fail.  A successful lift must
therefore reroute ownership through the common completion or use paths
which genuinely cross the Cartesian seam.

This does not rule out a state-level lift.  It rules out the entire
unchanged-completion, block-concatenation paradigm in every cap dimension.

## 7. General grid shuffles

The product of two complementary paths is an ((m+1)\times(s+1)) grid.
A word

\[
                         \sigma\in\{H,V\}^{m+s},
       \qquad |\sigma|_H=m,quad |\sigma|_V=s        \tag{7.1}
\]

specifies a monotone path through that grid.  Before a move at grid
coordinate ((i,j)), the lower vertex is

\[
                              a=x_i\cup u_j.          \tag{7.2}
\]

An (H)-move uses upper vertex (y_i\cup u_j) and ends at
(x_{i+1}\cup u_j).  A (V)-move uses upper vertex (x_i\cup v_j) and
ends at (x_i\cup u_{j+1}).

Every such shuffle is a complementary path.  Its complete first shadow is
described by the following local table.

### Lower intersections

\[
\begin{array}{c|c}
\text{move at }(i,j)&\text{(z)-free first-shadow target}\\ \hline
H&(x_i\cap x_{i+1})\cup u_j\\
V&x_i\cup(u_j\cap u_{j+1}).
\end{array}                                           \tag{7.3}
\]

Thus, if the horizontal step (i) is taken at height (h_i), its old
(L_i(P))-flag is decorated by (u_{h_i}).  The sequence

\[
                       0\le h_0\le\cdots\le h_{m-1}\le s             \tag{7.4}
\]

is nondecreasing.  Dually, if vertical step (j) is taken at column
(c_j), it contributes (x_{c_j}\cup L_j(Q)).

### Consecutive upper vertices

Put

\[
 C_i(P)=X\setminus y_i, \qquad C_j(Q)=Y\setminus v_j. \tag{7.5}
\]

For two consecutive moves, the (z)-containing target is

\[
\begin{array}{c|c}
\text{move pair}&\text{target after deleting (z)}\\ \hline
HH\text{ at height }j&U_{i+1}(P)\cup\overline{u_j}\\
VV\text{ at column }i&\overline{x_i}\cup U_{j+1}(Q)\\
HV\text{ or }VH\text{ around cell }(i,j)&C_i(P)\cup C_j(Q).
\end{array}                                           \tag{7.6}
\]

The two orientations of a corner give exactly the same target.  Only its
ownership path changes.

### Endpoint flags

\[
\begin{array}{c|c}
\text{first move}&\text{initial endpoint target}\\ \hline
H&E_0(P)\cup\overline{u_0}=E_0(P)\cup u_s\\
V&\overline{x_0}\cup E_0(Q)=x_m\cup E_0(Q),
\end{array}                                           \tag{7.7}
\]

and

\[
\begin{array}{c|c}
\text{last move}&\text{terminal endpoint target}\\ \hline
H&E_1(P)\cup\overline{u_s}=E_1(P)\cup u_0\\
V&\overline{x_m}\cup E_1(Q)=x_0\cup E_1(Q).
\end{array}                                           \tag{7.8}
\]

Equations (7.3)--(7.8) are the exact transportation form of the shuffle
problem.  The variables are monotone lattice paths, or equivalently the
nondecreasing height and column sequences.  Their constraints are:

1. balance every selected middle lower vertex and upper edge between the
   two factor sides;
2. balance the decorated horizontal and vertical (L)-flags in (7.3);
3. balance all (HH,VV,) and corner targets in (7.6); and
4. balance the two endpoint tables (7.7)--(7.8).

This is substantially smaller and more structured than arbitrary wreath
completion, but it is not automatically feasible.

## 8. Why seam crossing is genuinely different

The ordinary product is the boundary word (H^mV^s).  All old (L)-flags
then carry (u_0), while (E_0) carries (u_s=\overline{u_0}); Theorem
5.1 follows from this separation.

Consider instead

\[
                         H^aV^sH^{m-a}.              \tag{8.1}
\]

The first (a) old (L)-flags carry (u_0), and the remaining ones carry
(u_s).  If the first and last moves are horizontal, (7.7)--(7.8) give

\[
                  E_0(P)\cup u_s, \qquad E_1(P)\cup u_0.             \tag{8.2}
\]

Thus (8.1) can place internal (L)-occurrences in exactly the same cap
sections as the two endpoint flags.  It is the first product mechanism
which can use the old cancellation

\[
                         \Delta L+\Delta E_0+\Delta E_1=0           \tag{8.3}
\]

rather than demanding three separate zeroes.

It also creates new obligations: the vertical arm is pinned at the cut
state (x_a), the two corners expose (C_{a-1}(P)) and (C_a(P)), and
the (HH/VV) rows split the old (U)-flags.  These are precisely the
ownership constraints absent from ordinary concatenation.

### Atomic rhombus

Commuting adjacent moves (HV\leftrightarrow VH) around cell ((i,j))
has the same two lower endpoints and the same corner target

\[
                         z\cup C_i(P)\cup C_j(Q).      \tag{8.4}
\]

Its two (z)-free targets change by the tensor-square divergence

\[
\begin{aligned}
 &e_{L_i(P)\cup u_j}+e_{x_{i+1}\cup L_j(Q)}\\
 &\hspace{12mm}-e_{x_i\cup L_j(Q)}-e_{L_i(P)\cup u_{j+1}}.          \tag{8.5}
\end{aligned}
\]

However, the two routes use different three-vertex interiors in the
middle-level graph.  A rhombus commute is therefore not by itself a legal
factor switch.

### Minimal missing lemma (sealed seam mixer)

To evade Theorem 5.1 it is enough to prove the following genuinely new
statement for the MSW/Dyck completion sectors.

> **Sealed seam-mixer lemma.**  Product-grid rhombi can be completed by
> auxiliary paths in the adjacent active-atom sectors so that:
>
> 1. every changed middle vertex is rerouted exactly once and no vertex
>    outside the selected Catalan sectors changes ownership;
> 2. the induced first-shadow changes are the rhombus divergences (8.5)
>    together with explicitly paired (HH,VV,) and endpoint terms from
>    (7.6)--(7.8); and
> 3. these legal switches connect the bottom and top horizontal boundary
>    slots, so a signed defect satisfying (8.3) can be transported to zero.

The third clause is the essential one.  Rhombi confined to one boundary
row preserve the (L)-versus-endpoint separation and cannot help.  A legal
chain must cross the whole cap seam, moving some horizontal steps from
height (0) to height (s).

Once such a middle-support-preserving mixer is available, the remaining
choice of shuffles is the explicit integral transportation system
(7.3)--(7.8), not a search over arbitrary cyclic orders.  A nonzero deeper
shadow still has to be certified separately (or by an injective boundary
map).  No existence claim for the sealed seam mixer is made here.

## 9. Reproducibility

The standalone audit

```text
audit_haar_cartesian_flags.cpp
```

enumerates only the two orientations of each of the eight changed wreaths.
It checks endpoint compatibility and the four flag multisets directly.
The calculation has (9\cdot2^4\cdot2^4=2304) orientation pairs and is a
finite certificate for Section 6, not evidence for the all-dimensional
theorems.  Theorems 5.1 and the shuffle tables are symbolic and require no
enumeration.

## 10. The coordinate-cut double sector

The obstruction in Theorem 5.1 disappears if both orientations of a
one-coordinate cap are used and they are spliced at the unique flip of a
fixed old coordinate.

Fix (c\in X).  Orient every complementary path (P) so that

\[
                         c\in x_0, \qquad c\notin x_m.                \tag{10.1}
\]

There is a unique (a=a_c(P)\in\{0,\ldots,m-1\}) for which

\[
               c\in x_a\subset y_a, \qquad c\notin x_{a+1}.         \tag{10.2}
\]

Thus the down edge (y_a\to x_{a+1}) is the unique flip of (c).
Let the two new coordinates be (p,q).  Form two shuffled paths:

\[
\begin{aligned}
 A_c(P)&=H^a,V_{p\to q},H^{m-a},\\
 B_c(P)&=H^a,V_{q\to p},H^{m-a}.                  \tag{10.3}
\end{aligned}
\]

Both vertical moves are made at the last (c)-containing lower state
(x_a).  Away from that vertical arm, the two paths contain exactly both
tagged copies of every old path vertex:

\[
 \{S\cup\{p\},S\cup\{q\}:S\in V(P)\}.              \tag{10.4}
\]

The only failure of vertex-disjointness is exact and local.  The two paths
share the three-vertex cap diamond

\[
 x_a p\quad-\quad x_a pq\quad-\quad x_a q.           \tag{10.5}
\]

There is one such duplicated diamond per old path and no other overlap.

The same statement holds for every old first-shadow flag away from the two
joins adjacent to (10.5).  In one orientation a pre-cut flag is decorated
by (p) and a post-cut flag by (q); in the other orientation the tags are
reversed.  Hence their union contains both tagged copies of every old flag.
Only flags whose defining window meets the cap diamond or one of its two
joins fail this literal two-copy description.

This is the useful difference from one ordinary Cartesian sector.  It does
not ask (L,E_0,E_1) to vanish separately: every positional flag receives
both endpoint tags before the local overlap is resolved.

## 11. All-depth seam provenance and repair coefficient two

For a wreath, all occurrences of a fixed coordinate form one cyclic run in
its middle-window incidence word.  The cut (10.2) is a boundary of that
run.  A depth-(h) lower shadow is an intersection of (h+1) consecutive
middle windows, and the corresponding upper shadow is a union of (h+2)
consecutive middle windows.  Therefore every inherited shadow window whose
start is farther than (h+1) from the two joins in (10.5) is transported
literally to both tagged endpoint sections.  Every exception is a window
of length (O(h)) crossing one of a constant number of joins.

Summed through depths (0\le h\le H), a raw slot count gives
(O(H^2)) exceptional windows per old path.  Their repair-word cost is
only (O(H)): take an (O(H))-entry halo around each join.  Every crossing
window is a subinterval of one of these halos.  This is precisely Lemma 3
of `CONTRACTIVE_DEFECT_LIFT.md`.

Old holes have coefficient two rather than four.  If an old repair word
(R) represents every missing old central-band target, the two fixed
tagged copies

\[
                  (\{p\}\cup R), \qquad(\{q\}\cup R)                \tag{11.1}
\]

represent both inherited endpoint descendants.  It does not matter whether
an old target contains the distinguished closing coordinate (z): the two
desired tags are merely exchanged.  Taking both fixed tagged copies still
covers them.  Thus the inherited repair cost is exactly at most (2|R|).

### Conditional contractive-lift theorem

Suppose the double sectors (10.3), over all paths of an arbitrary exact old
factor, can be completed to an exact new factor after changing only a
constant-size neighbourhood of each duplicated diamond (10.5).  Suppose
also that every completion path has only a bounded number of joins with the
unchanged bulk sectors.  Then, for every (H=o(m)),

\[
 R_{m+1,H}\le 2R_{m,H}+O(H\operatorname{Cat}_m).      \tag{11.2}
\]

#### Proof

Use the two tagged copies (11.1) for inherited holes.  Every other target
lost by replacing the ideal double sector by the completed factor has a
witness window crossing one of (O(1)) joins per old path.  Append the
corresponding (O(H))-halos.  There are (\operatorname{Cat}_m) old paths,
so the halo cost is (O(H\operatorname{Cat}_m)).  Completion can only add
further witnesses.  This proves (11.2). \(\square\)

Since (2<4), Theorem 2 of `CONTRACTIVE_DEFECT_LIFT.md` would then imply

\[
                  \nu(k)=(1+o(1))
                         \binom{k}{\lfloor k/2\rfloor}.             \tag{11.3}
\]

No exact vertical preservation is required.

## 12. The exact Catalan completion gate

The new dimension contains

\[
 \operatorname{Cat}_{m+1}
 =2\operatorname{Cat}_m+
   \sum_{i=1}^{m-1}\operatorname{Cat}_i
                         \operatorname{Cat}_{m-i}                  \tag{12.1}
\]

wreath paths.  The two extreme terms are exactly the two endpoint-oriented
Cartesian sectors in (10.3).  The remaining first-return Dyck sectors have
the correct Catalan convolution size to provide a global completion.

The all-dimensional problem has therefore reduced to the following local
positive statement.

> **Catalan seam completion lemma.**  For every complementary path factor
> on (2m) coordinates and every fixed coordinate (c), the two extreme
> endpoint sectors (10.3) can be combined with paths indexed by the
> interior terms of (12.1) to form a complementary path factor on
> (2m+2) coordinates.  Outside a constant-size neighbourhood of the
> duplicated cap diamonds (10.5), the two extreme sectors remain unchanged,
> and every interior completion path has bounded seam complexity.

This is strictly smaller than arbitrary factor suspension.  The bulk is
already forced and correct; only one three-vertex duplicated diamond per
old wreath must be absorbed into the interior Catalan sectors.  It is also
exactly the positive/integral part missing from the Eilenberg--Zilber
shuffle identity: signed rhombus cancellation is automatic, whereas
vertex-disjoint ownership of the rhombus interiors is not.

Proving this lemma gives the coefficient-two recurrence (11.2).  Proving
that some family of old factors necessarily forces at least four inherited
repair sections would refute this route.  At present neither statement is
claimed.
