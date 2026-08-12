# Protected Greene--Kleitman pruning and the exact hinge-detachment gate

Date: 2026-08-01  
Lane: Greene--Kleitman branching / Boolean-diamond exchanges / protected pivot  
Status: exact protected dynamic program, exact local exchange criterion, and a
sharp global-edit obstruction.  No all-dimensional Catalan linear matching is
claimed.

## 0. Outcome

Let

\[
 \mathcal L={ [2m]\choose m-1},\qquad
 \mathcal X={ [2m]\choose m},\qquad
 \mathcal U={ [2m]\choose m+1},
\]

and let (M_{\rm GK}) be the Greene--Kleitman perfect matching between
(\mathcal L) and (\mathcal U).  Its Boolean-diamond lift (G_{\rm GK})
is a forest on \(\mathcal X\) with

\[
 N=|M_{\rm GK}|={2m\choose m-1}=m\operatorname {Cat}_m
\]

edges and exactly \(\operatorname {Cat}_m\) components, but maximum degree
\(m\).

This note proves five facts.

1. For every prescribed linear bank (P\subseteq G_{\rm GK}), the largest
   degree-two GK subforest containing (P) is given by an exact forced-edge
   tree dynamic program.
2. If (R_m) is the unprotected optimum and (R_m(P)) is the protected
   optimum, then
   \[
        R_m-|P|\le R_m(P)\le R_m.
   \]
   Thus a protected (O(\sqrt m)) pivot bank changes the GK edit barrier by
   only (O(\sqrt m)).
3. A palette-preserving Boolean square is exactly a hinge rotation.  There
   is a necessary-and-sufficient component test for it to preserve
   acyclicity and an exact formula for its change in branching excess.
4. The two alternating GK stars have no one-square branch-reducing move.
   Hence a monotone local square descent cannot even begin at the extreme GK
   branches; mass must first be exported through a nonlocal rethreading.
5. The exact total- and coordinate-degree ledgers admit a degree-
   \(\{1,2\}\) target which respects every fixed \(O(\sqrt m)\) protected
   bank.  Hence degree arithmetic is not the obstruction; realization by
   one outer-palette matching is.

The conclusion is quantitative.  Writing

\[
 \Delta_m=N-R_m,
\]

the audited plane-tree analysis gives

\[
 {\Delta_m\over N}\longrightarrow
 \mu=0.356895867892\ldots .
\]

If (P) has (O(\sqrt m)) edges, then the protected removal number has the
same limit.  Greene--Kleitman is therefore a useful exact palette/forest
support, but not a near solution to the degree-two gate.

## 1. Boolean diamonds and the GK forest

An outer-palette edge is a pair ((L,U)\in\mathcal L\times\mathcal U) with
(L\subset U).  If (U-L=\{a,b\}), its physical lift is the Johnson edge

\[
             \psi(L,U)=\{L+a,L+b\}.                 \tag{1.1}
\]

The Greene--Kleitman matching chooses every lower and every upper colour
exactly once.  Its physical lift is the pointed-plane-tree forest: one tree
with (m+1) pointings for each rooted plane tree with (m) edges.

Root every component in the GK direction.  For a vertex (v), write
(\mathcal C(v)) for its children.  A protected bank \(P\) is assumed to be
a subgraph of (G_{\rm GK}) with maximum degree at most two.  This scope is
important: the theorem below calibrates a pivot bank already aligned with
the GK matching; it does not prove that an arbitrary external pivot collar
can be planted into the literal GK matching.

## 2. Exact protected pruning dynamic program

For a nonroot vertex (v), let (e_v) be its parent edge.  For
(p\in\{0,1\}), define (F_v^P(p)) as the maximum number of retained edges
strictly inside the rooted subtree of (v), not counting (e_v), subject
to:

* every edge of (P) in the subtree is retained;
* the parent edge (e_v) is retained exactly when (p=1); and
* every physical degree is at most two.

If (e_v\in P) and (p=0), set (F_v^P(0)=-\infty).  Let

\[
 K_v=\{u\in\mathcal C(v):vu\in P\},\qquad c_v=|K_v|. \tag{2.1}
\]

For an unforced child (u\notin K_v), put

\[
 g_u=1+F_u^P(1)-F_u^P(0).                            \tag{2.2}
\]

### Theorem 2.1 (forced-edge tree recurrence)

If (p+c_v>2), then (F_v^P(p)=-\infty).  Otherwise

\[
\boxed{
\begin{aligned}
 F_v^P(p)={}&
 \sum_{u\in K_v}\bigl(1+F_u^P(1)\bigr)
 +\sum_{u\notin K_v}F_u^P(0)\\
 &+\sum_{i=1}^{2-p-c_v}\max(0,g_{(i)}),
\end{aligned}}                                                   \tag{2.3}
\]

where (g_{(1)}\ge g_{(2)}\ge\cdots) are the gains of the unforced
children, nonexistent terms are omitted, and any summand involving
(-\infty) makes that choice infeasible.

Consequently the exact maximum size of a degree-two GK subforest containing
(P) is

\[
                    R_m(P)=\sum_{r\text{ root}}F_r^P(0).         \tag{2.4}
\]

#### Proof

Every forced child edge must be retained and contributes
(1+F_u^P(1)).  Omitting an unforced child edge contributes (F_u^P(0)),
while retaining it has additional gain (2.2).  After the parent edge and
the (c_v) forced child edges are counted, exactly (2-p-c_v) degree slots
remain at (v).  Child subtrees are otherwise disjoint, so the optimum
takes the largest positive gains fitting those slots.  This proves (2.3)
by induction from the leaves.  Summing the root states proves (2.4).
\(\square\)

Because (P\) itself is a linear forest, every state needed by (2.4) is
feasible.  Thus (2.3) is also an exact certificate-producing algorithm, not
only a numerical recurrence.

### Theorem 2.2 (protected stability)

Let (R_m=R_m(\varnothing)).  For every protected linear bank
(P\subseteq G_{\rm GK}),

\[
                     \boxed{R_m-|P|\le R_m(P)\le R_m.}           \tag{2.5}
\]

#### Proof

The upper bound is immediate.  For the lower bound, start from an
unprotected optimum (F).  Insert the edges of (P-F) one at a time.  On
inserting \(xy\), each saturated endpoint requires deletion of at most one
currently retained nonprotected incident edge.  Such an edge always exists:
after the insertion, the protected degree at that endpoint is at most two,
so a degree-three violation cannot consist entirely of protected edges.

At most two old edges are deleted while one edge is inserted.  Hence each
forced insertion decreases cardinality by at most one.  Deletion and
insertion stay inside the ambient tree, so acyclicity is automatic.  The
final set contains (P), has degree at most two, and has size at least
(R_m-|P-F|\ge R_m-|P|).  \(\square\)

Put

\[
                 \Delta_m(P)=N-R_m(P).                         \tag{2.6}
\]

Then

\[
                  \Delta_m\le\Delta_m(P)\le\Delta_m+|P|.       \tag{2.7}
\]

In particular, for a fixed number (H) of aligned tight-pivot paths of
total size (3Hh=O_H(\sqrt m)), provided those paths are literal GK edges,

\[
             {\Delta_m(P)\over N}\longrightarrow\mu.           \tag{2.8}
\]

Any outer-palette perfect matching whose lift is linear and which keeps
all edges of (P) in their GK phase shares at most (R_m(P)) matching
edges with (M_{\rm GK}).  Hence it must replace at least
(\Delta_m(P)) GK diamonds.  This lower bound is exact for the support
pruning problem; it does not assert that the residual outer colours can
always be rematched.

## 3. Exact Boolean-square detachment

Let (M) be any perfect outer-palette matching and suppose its physical
lift (F=\Psi(M)) is a forest.  Every alternating four-cycle in the diamond
graph has a unique hinge (X\in\mathcal X).  For distinct (a,b\in X) and
distinct (y,z\notin X), its old physical edges are

\[
 XP=X\!-!(X-a+y),\qquad XQ=X\!-!(X-b+z),            \tag{3.1}
\]

and its new physical edges are

\[
 XP'=X\!-!(X-a+z),\qquad XQ'=X\!-!(X-b+y).          \tag{3.2}
\]

The four leaves (P,Q,P',Q') are pairwise distinct.  The exchange preserves
every lower and upper colour because it is an alternating matching square.

### Theorem 3.1 (safe hinge rotation)

Put (F_0=F-\{XP,XQ\}).  The switched graph

\[
                    F'=F_0+\{XP',XQ'\}                       \tag{3.3}
\]

is a forest if and only if the three (F_0)-components containing

\[
                         X,\quad P',\quad Q'                    \tag{3.4}
\]

are pairwise distinct.

Moreover, for the branching excess

\[
                  \mathfrak b(F)=\sum_V(\deg_F(V)-2)_+,
\]

one has the exact identity

\[
\boxed{
 \mathfrak b(F')-\mathfrak b(F)
 =-1_{\deg_F P\ge3}-1_{\deg_F Q\ge3}
  +1_{\deg_F P'\ge2}+1_{\deg_F Q'\ge2}.}             \tag{3.5}
\]

The hinge load is invariant:

\[
                         \deg_{F'}(X)=\deg_F(X).       \tag{3.6}
\]

If the two old diamonds are outside a protected matching bank and the new
diamonds use no protected outer endpoint, the switch retains that bank
literally.

#### Proof

After the old hinge edges are removed, adding (XP') creates a cycle
exactly when (X) and (P') already lie in one component.  If this first
edge is safe, adding (XQ') creates a cycle exactly when (Q') lies in the
new component containing either (X) or (P').  This is precisely the
pairwise-distinct condition (3.4).

At the hinge two edges are removed and two are added.  Each old leaf loses
one edge and each new leaf gains one.  Since the four leaves are distinct,
applying ( (d-2)_+ ) gives (3.5), while the hinge statement gives (3.6).
Alternating matching exchange proves the palette and protected assertions.
\(\square\)

### Corollary 3.2 (strict branch detachment)

If (3.4) holds, at least one of (P,Q) has degree at least three, both new
leaves have degree at most one, and the square avoids the protected bank,
then the switch preserves both outer palettes and acyclicity, creates no new
branch, and strictly decreases (\mathfrak b).

Thus a sequence with such a square available at every nonzero branch state
terminates in an outer-exact Catalan linear forest.  This is an exact
conditional detachment theorem.  Its missing hypothesis is availability;
the next result shows that Greene--Kleitman fails it at its two extremal
branches.

### Theorem 3.3 (complete protected orbit inside one rectangle)

Fix the hinge (X).  Every selected diamond in its rectangle has the form

\[
                  (X-a,X+y),\qquad a\in X,\ y\notin X.           \tag{3.7}
\]

Because (M) is a matching, (M\cap\mathcal R_X) is the graph of a
partial bijection

\[
                 \phi_X:A_X\longrightarrow Y_X,
                 \qquad |A_X|=|Y_X|=\deg_F(X).                  \tag{3.8}
\]

The alternating squares contained in (\mathcal R_X) generate every
permutation of the image assignments in (3.8).  If (p) spokes are
protected literally, the free orbit is the full symmetric group on the
remaining (\deg_F(X)-p) assignments.

For any such multi-rewire, delete all changed old (X)-spokes and call the
remaining forest (F_0).  The rewire preserves acyclicity if and only if
the (F_0)-components of (X) and of all new leaves are pairwise distinct.
It respects the degree-two cap away from (X) if and only if every new leaf
has residual degree at most one.  The degree of (X) is unchanged.

#### Proof

Two selected rows ((a_1,y_1),(a_2,y_2)) form an alternating square whose
other half is ((a_1,y_2),(a_2,y_1)).  Thus a square is a transposition of
two images of the partial bijection.  Transpositions generate the full
symmetric group, and fixing the protected pairs leaves the symmetric group
on the free pairs.

After the changed spokes are deleted, all new edges form a star centered at
(X).  Adding that star to a forest creates no cycle exactly when its
leaves and center lie in distinct old components.  The leaves are distinct,
so their literal residual degree bound is exactly one.  The same number of
spokes is removed and inserted at (X).  \(\square\)

This theorem identifies what squares *can* do: they can globally optimize
where the spokes of one fixed hinge land, even with protected spokes, but
they cannot reduce the hinge load itself.

## 4. Sharp square obstruction at the alternating GK stars

Let

\[
 E_m=\{0,2,\ldots,2m-2\},\qquad E_m^c=[2m]-E_m.
\]

The GK forest has degree (m) at each of these two vertices, and every
neighbor of either vertex has GK degree one.

### Theorem 4.1 (no one-square extreme-branch descent)

Every matching-alternating Boolean square applicable to the original GK
matching preserves the degree of (E_m), and likewise of (E_m^c).

#### Proof

An applicable square which changes the degree of (E_m) must contain one
of its selected star spokes (E_mY).  The two selected physical edges of
an alternating square share its unique hinge.  That hinge is one endpoint
of (E_mY).

If the hinge is (E_m), equation (3.6) preserves its degree.  If the hinge
is (Y), the square would require a second selected GK edge incident with
(Y).  But every GK neighbor (Y) of (E_m) has degree one.  This is
impossible.  A square not containing a star spoke does not affect the
degree of (E_m).  The complement argument is identical.  \(\square\)

Therefore no greedy theorem of the form

\[
 \text{positive branch excess}\Longrightarrow
 \text{one immediately branch-decreasing square}
\]

can hold from the GK seed.  A successful square-only route must first make
nonimproving preparatory moves, while any direct improving route needs an
alternating cycle crossing the overloaded rectangle.  Combined with
(2.7), the required rethreading changes a positive fraction of all GK
diamonds.

## 5. Exact degree ledgers do not obstruct a protected bank

Let (M) be any perfect lower--upper outer-palette matching, not
necessarily Greene--Kleitman, and write (d_M(X)=\deg_{\Psi(M)}(X)).  For
one diamond ((L,U)), with physical middle endpoints (T,H), one has the
coordinate-vector identity

\[
                         1_T+1_H=1_L+1_U.             \tag{5.1}
\]

Summing over the exact outer palettes gives

\[
 \sum_X d_M(X)=2m\operatorname {Cat}_m,               \tag{5.2}
\]

and, for every coordinate (i\in[2m]),

\[
 \sum_{X\ni i}d_M(X)
 ={2m-1\choose m-2}+{2m-1\choose m}.                 \tag{5.3}
\]

Equivalently, for the endpoint deficits

\[
                             y_X=2-d_M(X),             \tag{5.4}
\]

the exact ledgers are

\[
 \boxed{
 \sum_Xy_X=2\operatorname {Cat}_m,
 \qquad
 \sum_{X\ni i}y_X=\operatorname {Cat}_m
 \quad(i\in[2m]).}                                   \tag{5.5}
\]

These are necessary for every Catalan linear matching, but they do not
conflict with a small protected bank.

### Theorem 5.1 (protected capacity-feasible deficit design)

Let \(P\) be any protected physical linear forest, and put

\[
                  D_2=\{X:\deg_P(X)=2\}.              \tag{5.6}
\]

If

\[
              {1\over2}{2m\choose m}-|D_2|
                    \ge\operatorname {Cat}_m,          \tag{5.7}
\]

then there is an integral vector (d^*(X)\in\{1,2\}) satisfying

* (d^*(X)\ge\deg_P(X)) for every (X); and
* the exact total and coordinate ledgers (5.2)--(5.3).

In particular, (5.7) holds for every fixed (O(\sqrt m))-edge protected
bank once (m) is sufficiently large.

#### Proof

The middle layer splits into complementary pairs ({X,X^c}).  At most
(|D_2|) of these pairs meet (D_2), so (5.7) permits choosing
(\operatorname {Cat}_m) complementary pairs avoiding (D_2).  Set
(y_X=1) on both members of every chosen pair and (y_X=0) elsewhere, and
put (d^*(X)=2-y_X).

There are (2\operatorname {Cat}_m) selected middle sets, giving the first
ledger in (5.5).  Every coordinate lies in exactly one member of each
complementary pair, giving the second ledger.  A degree-two protected vertex
was avoided, while a protected vertex of degree at most one fits under
either value of (d^*).  \(\square\)

Thus neither total degree, coordinate balance, nor a fixed pivot bank forces
branching.  The unresolved obstruction is the correlated realization of a
capacity-feasible deficit design by one outer-palette matching and one
acyclic physical support.

## 6. Exact residual gate after protected pruning

The protected DP separates the owner-layer problem into two exact stages.

1. Choose the maximum protected linear support (S\subseteq G_{\rm GK})
   using (2.3).  This keeps (R_m(P)) old diamonds and exposes
   \(\Delta_m(P)\) lower colours and the same number of upper colours.
2. Rematch those residual outer colours by diamonds whose physical edges
   use the free ports of (S), do not create a cycle after contraction, and
   do not collide with the protected bank.

The second stage is the real integrality gate.  It is not ordinary Hall:
every candidate diamond simultaneously consumes a residual lower colour, a
residual upper colour, and two physical endpoint ports, together with a
graphic rank unit.  Equivalently, orient every component of (S) as a path
and use oriented residual diamonds.  A completion is a common independent
set of the lower-colour, upper-colour, tail-port, head-port, and contracted
graphic systems, of size \(\Delta_m(P)\).

If a candidate reservoir is already acyclic after contraction and has
unique tail and head ports built into its indexing, this collapses to the
corresponding residual perfect-matching Hall condition.  Without those two
extra hypotheses, Hall on the outer colours alone is insufficient.

This is the even-ground analogue of the rooted head-injective (Q_0) gate.
Once a completed physical lift is a linear forest, orient each path.  The
tail and head maps are automatically injective.  A prescribed pivot path
is retained exactly when the orientation constraints it imposes are
coherent on its component; for one protected pivot path this is automatic.
In the odd rooted formulation, choosing the correlated predecessor phase
turns that same protected path into the already proved head-injective
(Q_0) path.

## 7. Revised frontier

The exact Greene--Kleitman facts now say:

* outer-palette exactness and acyclicity are free;
* protected degree-two pruning is exactly solvable by (2.3);
* a fixed (O(\sqrt m)) protected bank costs only (O(\sqrt m)) additional
  retained GK edges;
* all exact total/coordinate degree ledgers remain feasible with that bank;
* nevertheless degree linearization requires replacing
  \((\mu+o(1))N\) GK diamonds;
* Boolean squares have an exact safe detachment criterion but cannot start
  by repairing either extreme GK star; and
* after pruning, the unresolved object is precisely a protected
  outer-colour/tail/head/graphic completion.

Thus Greene--Kleitman should be used as a calibration and a source of
protected forest support, not as a locally repairable seed.  The positive
construction still has to be born in, or globally rethreaded into, the
head-injective upper-exact (Q_0) fibre.
