# Fixed-SCD contraction of proportional atoms: exact path gate and obstruction

Date: 2026-07-25

This note asks whether the (a+c=1) cover correlations in the proportional
tight-atom hypergraph can be removed by first assigning every Boolean mask
to one symmetric-chain decomposition.  The contraction is exact, but it
does not by itself prove the matching lemma: after contraction, the whole
problem becomes a long compatible-path packing inside the chosen SCD.

Throughout,

\[
 n=2m+1,qquad b=\lfloor m^{3/4}\rfloor,qquad
 H=\Theta(\sqrt{m\log m}),qquad p=\lfloor W/b\rfloor.
\]

Use the homogeneous proportional radius profile

\[
 a_d=b_{-d}-b_{-(d+1)}\ (d<H),\qquad a_H=b_{-H}
\tag{0.1}
\]

from `PROPORTIONAL_TIGHT_ATOM_MULTIRADIUS_EQUIVALENCE_20260725.md`.

## 1. Endpoint flags owned by one SCD

Fix an SCD (\mathcal D) of (B_n).  Every chain contains exactly one
rank-(m) owner.  For (X\in\binom{[n]}m), let (\tau(X)) be the radius of
its chain, and write its central members as

\[
 L_{\tau(X)}(X)\subset\cdots\subset L_1(X)\subset
 L_0(X)=X=U_0(X)\subset U_1(X)\subset\cdots
 \subset U_{\tau(X)+1}(X),
\tag{1.1}
\]

where (|L_q(X)|=m-q) and (|U_q(X)|=m+q).  The extra upper member is the
usual odd-dimensional central mate.  The radius census is forced:

\[
 |\{X:\tau(X)=d\}|=
 \binom n{m-d}-\binom n{m-d-1}\quad(d<m),
\tag{1.2}
\]

with the usual truncated top class when only depths (d\le H) are retained.

For Johnson-adjacent (X,Y\), call the directed transition (X\to Y)
**SCD-compatible through the available flags** when

\[
 \boxed{
 L_q(Y)=Y\cap L_{q-1}(X)}
\tag{1.3}
\]

whenever both sides belong to the prescribed lower flags, and

\[
 \boxed{
 U_q(X)=X\cup U_{q-1}(Y)}
\tag{1.4}
\]

whenever both sides belong to the prescribed upper flags.  At (q=1))
these are simply

\[
 L_1(Y)=X\cap Y,qquad U_1(X)=X\cup Y.
\tag{1.5}
\]

Let (G_{\mathcal D}) be this directed compatibility graph.  When chains
are clipped to prescribed radii (d(X)\le\min\{\tau(X),H\}), impose
(1.3)--(1.4) only through those radii and denote the resulting graph by
(G_{\mathcal D,\mathbf d}).

There is an endpoint qualification which matters.  The lower flag of the
first selected owner is read from windows *before* the selected central
path, and the upper flag of the last selected owner is read from windows
*after* it.  Thus internal compatibility in
(G_{\mathcal D,\mathbf d}) is necessary but is not, by itself, sufficient
for a physical row.

Call a directed path

\[
 X_0\to X_1\to\cdots\to X_{b-1}
\tag{1.6}
\]

**row-completable** when there is one cyclic coordinate order (\pi) and
consecutive starts (t_i=t_0+i) such that

\[
 X_i=I_\pi(t_i,m),
\tag{1.7}
\]

and, for every selected owner,

\[
 L_q(X_i)=I_\pi(t_i,m-q)\quad(0\le q\le d(X_i)),
\tag{1.8}
\]

\[
 U_q(X_i)=I_\pi(t_i,m+q)\quad(0\le q\le d(X_i)+1).
\tag{1.9}
\]

Equivalently, the central path has a two-sided coordinate collar deep
enough to realize all prescribed endpoint flags.  Since
(b+2H<m) for the present parameters, such a collar, when it exists, uses
fewer than (n) coordinate positions and is an ordinary injective tight
segment rather than a wraparound degeneracy.

### Lemma 1.1 (tight rows give row-completable compatible paths)

Let (x_0,\ldots,x_{m+b+H}) be an injective tight word and put

\[
 X_i=\{x_i,\ldots,x_{i+m-1}\}\qquad(0\le i<b).
\]

If the radius-(d_i) interval chain at every (X_i) is the corresponding
central segment of its (\mathcal D)-chain, then

\[
 X_0\to X_1\to\cdots\to X_{b-1}
\tag{1.10}
\]

is a row-completable directed path in (G_{\mathcal D,\mathbf d}), and its
transition supports are pairwise disjoint.

#### Proof

For cyclic-window notation (A_{i,q}=\{x_i,\ldots,x_{i+m+q-1}\}),

\[
 A_{i+1,-q}=X_{i+1}\cap A_{i,-(q-1)},
\qquad
 A_{i,q}=X_i\cup A_{i+1,q-1}.
\tag{1.11}
\]

These are exactly (1.3)--(1.4).  The (i)-th transition support is
(\{x_i,x_{i+m}\}).  Since (b<m) and the word is injective, these
supports are pairwise disjoint.  \(\square\)

### Lemma 1.2 (the exact converse includes the endpoint collar)

A selected owner path comes from one fully (\mathcal D)-owned tight row
if and only if it is row-completable in the sense of (1.7)--(1.9).
Every row-completable path is a support-separated path in
(G_{\mathcal D,\mathbf d}).  The converse implication from an uncollared
path in (G_{\mathcal D,\mathbf d}) can fail at its two endpoints.

#### Proof

The forward implication is Lemma 1.1.  Conversely, (1.7) realizes the
middle owners as consecutive windows of one cyclic order, while
(1.8)--(1.9) say exactly that every designated member of the owner chain
is the corresponding shorter or longer interval.  This is precisely the
definition of the tight proportional row.

For clarity about the qualification, internal identities propagate a
lower flag from predecessors and an upper flag from successors.  They do
not determine (L_q(X_0)) from the displayed path, nor do they determine
(U_q(X_{b-1})) there.  Those data are supplied by the two-sided collar in
(1.8)--(1.9).  \(\square\)

Thus the durable-edge graph is an exact internal test and a useful
relaxation.  The exact physical-row objects are its row-completable paths.

## 2. Exact contraction theorem

Call a proportional atom **fully (\mathcal D)-owned** when every one of
its designated chains is the complete clipped central segment of the
unique (\mathcal D)-chain containing its middle owner.  Consequently a
middle owner cannot occur in two selected atoms, and no two selected owned
chains can share any Boolean mask.

### Theorem 2.1 (SCD contraction/path-packing equivalence)

For an integer (s\), the following are equivalent.

1. There is a matching of (s\) fully (\mathcal D)-owned proportional
   atoms.
2. The graph (G_{\mathcal D,\mathbf d}) contains (s\) vertex-disjoint
   row-completable directed paths, each on (b) vertices, such that every
   path has exactly (a_d) owners assigned clipped radius (d).

#### Proof

Lemma 1.1 maps every selected atom to a row-completable compatible path.
Disjoint Boolean targets imply distinct middle owners, so the paths are
vertex-disjoint.

Conversely, Lemma 1.2 turns every listed path into one tight proportional
row.  All designated chains lie in (\mathcal D).  Since the SCD partitions
the Boolean lattice and the paths have disjoint owners, all designated
targets in different rows are disjoint.  Hence the rows are a hypergraph
matching.  The radius count is exactly (0.1).  \(\square\)

This theorem contracts not only the (a+c=1) cover correlations but every
Boolean collision: after a common SCD is fixed, disjointness of chain
supervertices is exact.  There is no residual (O(m^{-2})) matching problem.
Instead, all difficulty has moved into finding long row-completable paths in
(G_{\mathcal D,\mathbf d}).

## 3. Quantitative necessary condition

If the proportional matching target holds inside one fixed SCD, then

\[
 s=p-o(p/\sqrt m).
\]

The (s) paths in Theorem 2.1 use (sb) vertices and (s(b-1)) compatible
arcs.  Since (pb=W-O(b)), this forces

\[
 \boxed{
 \nu_{\rm row}(G_{\mathcal D,\mathbf d})
 \ge W-o(W/\sqrt m),}
\tag{3.1}
\]

where (\nu_{\rm row}) denotes the maximum number of vertices covered by
vertex-disjoint row-completable directed (b)-paths.  In particular, the
same lower bound is necessary for the relaxed maximum (\nu_{\rm path})
over support-separated paths.  Hence

\[
 \boxed{|E(G_{\mathcal D,\mathbf d})|
 \ge W-o(W/\sqrt m).}
\tag{3.2}
\]

The path cover must have only

\[
 s=(1+o(1))W/b=(1+o(1))Wm^{-3/4}
\tag{3.3}
\]

components.  This is substantially stronger than obtaining correct SCD
marginals or many isolated compatible arcs.

There is also an exact degree-collapse calculation.  The total number of
oriented support-separated Johnson paths on (b) middle owners is

\[
 |\mathcal P_b|
 =W\prod_{t=0}^{b-2}(m-t)(m+1-t).
\tag{3.4}
\]

Indeed, after (t) transitions, exactly (t) used support coordinates lie
inside the current owner and (t) lie outside it.  The next departure and
arrival therefore have respectively ((m-t)) and ((m+1-t)) choices.

Fixing the SCD upper mate (U_1(X)) forces the arrival coordinate of every
compatible transition out of (X).  Only the departure remains free.
Consequently the number of paths satisfying even just the upper half of
(1.5) is at most

\[
 W\prod_{t=0}^{b-2}(m-t).
\tag{3.5}
\]

Thus the retained fraction of the original tight-path orbit is at most

\[
 \boxed{
 \prod_{t=0}^{b-2}\frac1{m+1-t}
 =\exp\{-\Theta(b\log m)\}.}
\tag{3.6}
\]

The lower flags and endpoint collars can only reduce it further.  This
does not rule out a specially organized near-spanning path cover: the
absolute number in (3.5) is still huge.  It does rigorously rule out the
interpretation that fixing an SCD leaves a near-regular, mildly thinned
version of the original atom hypergraph to which the old nibble can simply
be reapplied.

At depth one, an arc (X\to Y) is equivalently a central Boolean square

\[
 L_1(Y)\subset X,Y\subset U_1(X).
\tag{3.7}
\]

For a fixed (X), (U_1(X)) has only (m) alternative middle facets, so
the outdegree is at most (m).  For an uncorrelated choice of lower and
upper endpoint matchings, each alternative satisfies the required lower
ownership with probability on the order of (1/m); the natural degree
scale is therefore constant, not a long-path theorem.  This last statement
is heuristic only; (3.1)--(3.2), not the heuristic, are the rigorous
obstruction test.

## 4. Why coordinate averaging does not help a fixed SCD

For every coordinate permutation (\sigma\),

\[
 G_{\sigma\mathcal D,\sigma\mathbf d}
 \cong G_{\mathcal D,\mathbf d}
\tag{4.1}
\]

under (X\mapsto\sigma X).  Thus the maximum compatible row packing, its
component count, and all residence/collar violations are invariant under
global coordinate relabeling.  Averaging over the coordinate orbit of one
SCD cannot improve (3.1).

Relabeling different chains independently is not an averaging argument: it
destroys the fact that the chains form one Boolean partition.  Likewise,
using a different SCD for every atom does not contract collisions between
atoms, because their chain supervertices then refer to different
partitions.

There is also a precise first-moment reason that independently averaging
the two central SCD matchings is insufficient.  Forget the deeper flags
temporarily.  Choose independently

- a uniform perfect matching (\mathsf U) between ranks (m) and (m+1);
- a uniform inclusion matching (\mathsf L) which saturates rank (m-1)
  into rank (m).

For an ordered Johnson edge (X\to Y), declare it centrally compatible
when

\[
 \mathsf U(X)=X\cup Y,
 \qquad
 \mathsf L(X\cap Y)=Y.
\tag{4.2}
\]

By coordinate transitivity, every upper incidence belongs to
(\mathsf U) with probability (1/(m+1)), and every lower incidence belongs
to (\mathsf L) with probability (1/(m+2)).  There are
(Wm(m+1)) ordered Johnson edges.  Independence therefore gives the exact
expectation

\[
 \boxed{
 \mathbb E|E(G_{\mathsf L,\mathsf U})|
 =\frac{Wm(m+1)}{(m+1)(m+2)}
 =\binom n{m-1}=N_1.}
\tag{4.3}
\]

Thus independent central averaging gets the *total* arc count on exactly
the correct first-order scale.  What it does not provide is the almost
partial-permutation structure needed to concatenate those arcs into only
(W/b) long components.  Any proof by randomizing SCDs must therefore
control branching, endpoints, support reuse, and the deeper collars; the
first moment (4.3) contains none of that information.

The known standard two-coordinate recursive SCDs fail an even weaker rotor
path objective by a positive leading toll; this is quantified in
`MATH_ATTACK_S_MASTER_RSCD_RECURSIVE_SELECTION_NOGO_20260725.md`.  That
result does not rule out a new densely modified SCD, but it rules out using
the canonical recursive family as the fixed contraction.

## 5. Relation to the (O(m^{-2})) residual overlap

Before fixing an SCD, deleting the adjacent-cover pairs from the atom
codegree row leaves (O(m^{-2})) normalized overlap.  Theorem 2.1 explains
why this does not directly invoke a matching theorem:

- an exact SCD contraction removes *all* overlap, including the
  (O(m^{-2})) part;
- but it retains only atoms which are long row-completable paths in the
  selected durable graph;
- there is no proved lower bound showing that an arbitrary, random, or
  canonical SCD retains enough such atoms.

Therefore “contract the vertical chains and nibble the remainder” is not a
valid two-stage proof unless the first stage simultaneously establishes
(3.1).  Establishing (3.1) for some integral SCD is precisely the
balanced-flag/rotor fusion theorem, now with the stronger proportional
block length (b=m^{3/4}).

## 6. Exact remaining fixed-SCD theorem

A fixed-SCD proof of the proportional matching lemma is equivalent to:

> Construct an SCD (\mathcal D_m), choose the floor-proportional clipped
> radius labels, and pack
> (p-o(p/\sqrt m)) row-completable directed (b)-paths in
> (G_{\mathcal D_m,\mathbf d}), every path having radius histogram
> ((a_0,\ldots,a_H)).

This would prove constant one, but it is not a consequence of SCD
integrality or coordinate averaging.  The contraction is mathematically
sound; the missing content is exactly a new SCD whose endpoint flags are
already organized into almost spanning tight rows.

There is a stronger, especially clean positive target.  Let (\mathcal F)
be an exact middle wreath factor, and assign a radius (d(v)) to every
pointed middle start (v=(\pi,j)).  Require, for every (1\le q\le H), that
the active starts (d(v)\ge q) give bijections

\[
 v\longmapsto I_\pi(j,m-q),
 \qquad
 v\longmapsto I_\pi(j,m+1+q)
\tag{6.1}
\]

onto the two symmetric rank layers.  Nesting of the active sets is
automatic from the single radius label.  Then the interval chains at all
starts are pairwise disjoint and partition the entire central band.  In
other words, (\mathcal F,d) is a cyclic-interval SCD resolution through
depth (H).

This stronger object immediately gives the desired word: linearize each
wreath once using base windows of length (m-H).  The total length is

\[
 \frac Wn(n+2H+1)
 =W+O(HW/m).
\tag{6.2}
\]

For (H=o(m)) this is (W+o(W)); once (H/\sqrt m\to\infty), the established
outer-tail word is also (o(W)).  Such a resolution exists in the audited
(m=4) instance, but no all-dimensional construction is known.  It is the
full-cycle version of the row-completable path theorem above, and it
pinpoints what a successful correlated-SCD construction would have to
produce.
