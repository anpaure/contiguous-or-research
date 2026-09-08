# Lane S: the tetrahedral \(C_6\) storage invariant

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The smallest moving-exterior \(C_6\) packet and its paired star-to-star
completion are literal positive packets. They do not compile into the
proposed three-reservoir tetrahedral closure.

Put

\[
 \alpha=(a\,b\,c),\qquad
 \beta=(a\,d\,b),\qquad
 \gamma=(a\,c\,d).
\]

With standard function composition,

\[
                         \alpha\beta\gamma=1.           \tag{0.1}
\]

Thus the transported endpoint-monodromy ledger can close. The physical
storage ledger cannot.

The obstruction occurs already between any two of the three faces.
Suppose a later outgoing \(C_6\) is required to use a coordinate-disjoint
reservoir of old petals. Its two petals on the strands shared with the
earlier face must already be present in the earlier face. Since they are
not the earlier active petals, the earlier common-core condition forces
both of them into the common core on both shared strands. To reach the
later star, each shared strand must delete the other strand's future
petal. The later \(C_6\) has the mandatory upper colour

\[
                         H\cup\{q_x,q_y\}.             \tag{0.2}
\]

One alternating orientation enters this colour from \(H+q_x\), thereby
reinserting \(q_y\); the other enters it from \(H+q_y\), thereby
reinserting \(q_x\). Both violate coordinate monotonicity on a Johnson
geodesic. Deleting the newly inserted coordinate immediately instead
repeats the same lower state and violates simple \(X\)-ownership.

Every two tetrahedral supports intersect in two strands:

\[
\begin{aligned}
 \{a,b,c\}\cap\{a,d,b\}&=\{a,b\},\\
 \{a,b,c\}\cap\{a,c,d\}&=\{a,c\},\\
 \{a,d,b\}\cap\{a,c,d\}&=\{a,d\}.
\end{aligned}                                          \tag{0.3}
\]

Hence every serial order fails at its second router. The inactive fourth
strand, arbitrary passive spectators, arbitrary monotone filler collars,
and higher-rank suspension do not repair the failed upper colour.

For completed paired star-to-star blocks there is an additional permanent
scar formulation. The first block inserts petal \(p_y\) on one root path
and removes that same physical coordinate from root path \(y\). Those
opposite statuses can never be equalized on geodesic continuations. Any
later star meeting the first support in two strands either has pairwise
Johnson distance at least two or is forced to reuse and then remove an
inserted scar.

Therefore:

\[
\boxed{
\begin{gathered}
\text{the relation (0.1) gives abstract identity endpoint monodromy;}\\
\text{no fixed-face serial rank-three packet using distinct petals
old and retained on the active paths has literal full \(X/Y\) collars;}\\
\text{indeed, no passive rank suspension of that star-to-star
architecture works.}
\end{gathered}}                                        \tag{0.4}
\]

The proof does not rule out a genuinely fused non-star atom which
interleaves the one-way packets before their terminal \(C_6\)'s, a
higher-distance multi-petal port, or a literal packet crossing the
infinity cut. Each would require a new complete collar construction.

## 1. Conventions and the algebraic relation

Permutations act on the left, and a product is evaluated rightmost first.
Direct calculation gives

\[
                         \alpha\beta=(a\,d\,c),
\]

whose inverse is \(\gamma=(a\,c\,d)\). This proves (0.1).

Under this convention the chronological order

\[
                         \gamma,\ \beta,\ \alpha        \tag{1.1}
\]

has identity endpoint action. Explicitly,

\[
\begin{array}{c|cccc}
x&a&b&c&d\\ \hline
\gamma x&c&b&d&a\\
\beta\gamma x&c&a&b&d\\
\alpha\beta\gamma x&a&b&c&d.
\end{array}                                            \tag{1.2}
\]

If a right-action convention is used instead, the same physical order is
written in the reverse algebraic convention. Nothing below depends on
this choice: in every serial order the first two face supports have
intersection two.

Two label frames must not be conflated.

1. Inside one completed setting, support labels may be transported back to
   the common entrance roots. A state on strand \(x\) then means the state
   on the physical path whose prefix begins at root \(x\), even when an
   earlier router has permuted its tail. Theorem 4.1 applies in this frame.
2. To compare two settings with one exact \(X/Y\) ledger, every router
   must also be one fixed physical incidence cycle in both settings.
   Reindexing a later face separately after an earlier tail permutation
   changes its literal vertices and is not a legal identification.

Section 7 records the resulting dichotomy.

## 2. The coordinatewise geodesic ledger

Let

\[
                         S_0,S_1,\ldots,S_L
\]

be a Johnson walk of \(m\)-sets from \(A=S_0\) to \(E=S_L\). For a
coordinate \(z\), let \(N_z\) be the number of times its membership
changes along the walk.

### Lemma 2.1 (exact excess identity)

\[
 \boxed{
 L-d_J(A,E)
 =\frac12\sum_z
   \left(N_z-\mathbf1_{\{z\in A\triangle E\}}\right).} \tag{2.1}
\]

In particular, the walk is geodesic if and only if every coordinate
changes membership at most once.

#### Proof

Every Johnson step deletes one coordinate and inserts one, so

\[
                         \sum_zN_z=2L.
\]

The parity of \(N_z\) records whether the two endpoint memberships differ,
and

\[
 |A\triangle E|=2d_J(A,E).
\]

Subtracting these two equalities gives (2.1). Each summand is a
nonnegative even integer, proving the final assertion. \(\square\)

Thus either history

\[
                         1\longrightarrow0\longrightarrow1
 \quad\hbox{or}\quad
                         0\longrightarrow1\longrightarrow0           \tag{2.2}
\]

forces

\[
                         L\ge d_J(A,E)+1.              \tag{2.3}
\]

This is the coordinatewise refinement of the mixed-phase endpoint law.
The scalar endpoint distance may be correct at each isolated router while
a serial packet still violates (2.1).

## 3. Literal outgoing \(C_6\) collars

Let \(K\) be an \((m-1)\)-set and let \(p,q,r\notin K\) be distinct. The
lower and upper shores of a common-core incidence hexagon are

\[
\begin{aligned}
 {\cal X}&=\{K+p,K+q,K+r\},\\
 {\cal Y}&=\{K+p+q,K+q+r,K+r+p\}.                      \tag{3.1}
\end{aligned}
\]

The two alternating outgoing matchings are

\[
\begin{aligned}
 M^+={}&\{(K+p,K+p+q),(K+q,K+q+r),(K+r,K+r+p)\},\\
 M^-={}&\{(K+q,K+p+q),(K+r,K+q+r),(K+p,K+r+p)\}.
                                                               \tag{3.2}
\end{aligned}
\]

Consequently every upper \(K+p+q\) is owned by exactly one of its two
cycle neighbours in either orientation. There is no third cycle lower
vertex to which that colour can be assigned.

### Lemma 3.1 (the shared-upper restitution test)

Suppose two physical geodesic rows arrive at

\[
                         X_p=K+p,\qquad X_q=K+q,
\]

and suppose coordinate \(q\) was present and then deleted earlier on the
row arriving at \(X_p\), while coordinate \(p\) was present and then
deleted earlier on the row arriving at \(X_q\). Then neither matching in
(3.2) can be the next outgoing \(C_6\) matching of two geodesic rows.

#### Proof

The upper colour

\[
                         Y_{pq}=K+p+q
\]

is matched from \(X_p\) in \(M^+\) and from \(X_q\) in \(M^-\).

In the first case, the ascent \(X_p\subset Y_{pq}\) reinserts \(q\).
If the following descent deletes a coordinate other than \(q\), the row
has the forbidden history \(1\to0\to1\). If it deletes \(q\), the next
lower state is \(X_p\) again, so the purported Johnson step is lazy and
the same lower \(X\)-resource occurs twice.

The second case is identical with \(p,q\) interchanged. Thus neither
orientation supplies a simple geodesic continuation. \(\square\)

This lemma audits the complete upper collar. Merely observing that the
three lower vertices and the three upper vertices are distinct does not
settle which physical row owns each upper colour.

## 4. The two-face old-reservoir obstruction

We now state the storage hypothesis precisely.

Consider two outgoing common-core \(C_6\) routers in one root-to-endpoint
geodesic half. Let their transported strand supports be \(T\) and \(U\),
with

\[
                         |T\cap U|\ge2.                \tag{4.1}
\]

The first router has petals in a reservoir \(R\). The second has petals
in a coordinate-disjoint reservoir \(Q\). For every \(x\in U\), let
\(q_x\in Q\) be its second-router petal. Assume:

1. the \(q_x\)'s are pairwise distinct;
2. \(q_x\) is an old coordinate on the physical root path \(x\), meaning
   that it belongs to that path's initial state;
3. it has not been deleted before the entrance of the second router; and
4. arbitrary intervening collars and arbitrary motion of strands outside
   \(T\cap U\) are allowed, but every complete row is geodesic.

### Theorem 4.1 (two-face storage obstruction)

Under these hypotheses the second router has no legal outgoing
orientation. Hence no literal packet satisfying them exists.

#### Proof

Choose distinct \(x,y\in T\cap U\). Write the first lower shore as

\[
                         A_z=K+p_z,\qquad z\in T,
\]

where \(p_z\in R\). Since \(R\cap Q=\varnothing\), neither \(q_x\) nor
\(q_y\) is an active first-router petal.

Coordinate \(q_x\) is old on row \(x\) and is present later at the second
entrance. A geodesic cannot delete and reinsert it, so \(q_x\in A_x\).
Because \(q_x\ne p_x\), it follows that \(q_x\in K\), and hence
\(q_x\in A_y\). Similarly,

\[
                         q_x,q_y\in A_x\cap A_y.        \tag{4.2}
\]

This is the forced cross-preload.

Write the second lower shore as

\[
                         B_z=H+q_z,\qquad z\in U.       \tag{4.3}
\]

Then

\[
 q_y\in A_x\setminus B_x,\qquad
 q_x\in A_y\setminus B_y.                             \tag{4.4}
\]

If either cross-petal was inserted at any earlier time before its cross
deletion rather than being present initially on the cross row, (4.4) is
already an inserted-then-deleted violation. Otherwise (4.4) says that row \(x\)
permanently deleted \(q_y\), and row \(y\) permanently deleted \(q_x\).

The second \(C_6\) necessarily contains the upper colour

\[
                         H+q_x+q_y.                    \tag{4.5}
\]

Lemma 3.1 shows that both of its alternating outgoing orientations are
illegal. This contradiction is independent of every intervening state
and of the fourth strand. \(\square\)

### Corollary 4.2 (exact failed storage minor)

On the two shared root paths, the second reservoir is forced to undergo

\[
 \begin{pmatrix}1&1\\1&1\end{pmatrix}
 \longrightarrow
 \begin{pmatrix}1&0\\0&1\end{pmatrix}.                 \tag{4.6}
\]

The mandatory upper (4.5) restores one of the two deleted off-diagonal
entries in every alternating orientation. Thus the failed cut consists
of exactly two lower resources and one upper resource.

### Corollary 4.3 (pair-distance form)

At the second entrance the two shared rows have Johnson distance one, and
their unique differences are \(q_x,q_y\). Any persistent difference
created by the first reservoir would raise this distance to at least two.
Therefore a distinct second-reservoir petal cannot coexist with such a
scar inside a common-core \(C_6\) shore.

Suspending the construction to higher rank only enlarges \(H\); it does
not change this pair-distance-one cut.

## 5. Application to tetrahedral closure

The supports of \(\alpha,\beta,\gamma\) are

\[
 T_\alpha=\{a,b,c\},\qquad
 T_\beta=\{a,d,b\},\qquad
 T_\gamma=\{a,c,d\}.                                  \tag{5.1}
\]

They satisfy (0.3). Therefore, in every serial order, the first and second
routers satisfy the hypothesis \(|T\cap U|=2\) of Theorem 4.1.

### Theorem 5.1 (rank-three tetrahedral no-go)

There is no serial packet consisting of these three outgoing \(C_6\)
routers such that:

1. each router is one fixed literal six-vertex incidence face common to
   both settings, and every intervening filler collar is owner-preserving
   on the four transported strands;
2. its active petals lie in a coordinate reservoir disjoint from the
   other two reservoirs and, in each completed setting, every active
   physical root's petal belongs to that root path's global initial state
   and remains undeleted until that router entrance;
3. every row lies in one root-to-complement Johnson-geodesic half;
4. the two settings have identical complete \(X/Y\) multisets, with every
   collar resource simple and owned once; and
5. the three endpoint actions are composed to identity.

This remains impossible with arbitrary passive spectator coordinates,
arbitrary owner-preserving monotone filler collars, and arbitrary motion
of the inactive fourth strand.

#### Proof

Grant the algebraic identity (0.1) and choose any serial order.

Because the three faces are fixed physically in both settings, transport
their owner labels back to the common entrance roots. The first two
supports meet in two physical root paths by (0.3). Their reservoirs are
disjoint, and condition 2 is exactly the old-and-retained hypothesis of
Theorem 4.1 in each setting. Hence the second router has no legal outgoing
orientation. The third router and endpoint product are never reached.
\(\square\)

If instead the support name is reassigned after the first tail
permutation, the later physical face changes. Indeed

\[
       \gamma^{\pm1}T_\beta\ne T_\beta.                \tag{5.2}
\]

Such a construction is not covered by Theorem 5.1. It must use an
adaptive union of physical faces and prove that the two larger aggregate
resource unions agree. That is a different packet, not the proposed
three-fixed-face closure.

The result is stronger than a failure of a particular table: it rules out
all passive rank suspensions of the distinct-old-reservoir architecture.
It does not assert that three arbitrary \(C_6\)'s in a pre-existing global
factor cannot have the abstract relation (0.1). It says they cannot be
compiled serially by the proposed storage rule into literal minimum-wreath
rows.

## 6. The completed paired-packet scar

The preceding theorem directly addresses distinct old reservoirs. The
positive paired star-to-star packet has a second, intrinsic obstruction.

Let \(T\) be a strand triple, let \(p_x\) be its input star petals, and let
\(\sigma\) be either orientation of a 3-cycle. A completed paired packet
has boundary action

\[
 S_x^{\rm in}=K+p_x,\qquad
 S_x^{\rm out}=K'+p_{\sigma x},
 \qquad x\in T.                                       \tag{6.1}
\]

Its literal exchange list removes \(p_x\) and inserts \(p_{\sigma x}\).

### Theorem 6.1 (permanent-scar obstruction)

After a completed paired packet on \(T\), no later completed paired
star-to-star packet can have support \(U\) with

\[
                         |T\cap U|\ge2                \tag{6.2}
\]

on the same geodesic half.

#### Proof

Choose \(x,y\in T\cap U\) with \(\sigma x=y\). Every unordered pair in a
3-cycle has one of its two directions in the cycle.

During the first packet, coordinate \(p_y\) changes

\[
\begin{array}{c|cc}
 &\text{entrance}&\text{exit}\\ \hline
\text{row }x&0&1\\
\text{row }y&1&0.
\end{array}                                            \tag{6.3}
\]

By Lemma 2.1 these two statuses are permanent thereafter: row \(x\)
cannot remove \(p_y\), and row \(y\) cannot reinsert it.

At the later star, write

\[
                         W_z=G+r_z,\qquad z\in U.
\]

Since \(p_y\in W_x\setminus W_y\) and two star members have exactly one
coordinate on each side of their difference, \(r_x=p_y\). A completed
paired packet removes every input petal from its own row. It would
therefore remove \(p_y\) from row \(x\), producing

\[
                         0\longrightarrow1\longrightarrow0,
\]

contrary to Lemma 2.1. \(\square\)

### Corollary 6.2 (scar graph)

After a paired packet on \(T\), place a labelled arc

\[
                         x\longrightarrow\sigma x
\]

for every \(x\in T\), labelled by \(p_{\sigma x}\). Its label is
permanently present on the tail row and permanently absent on the head
row. The underlying scar graph is \(K_3\).

Every later completed paired-star support must be an independent set in
that scar graph. Hence it meets \(T\) in at most one strand. On four total
strands no new three-strand support has this property.

This proves the paired-packet no-go even without prescribing a distinct
old reservoir for the later block.

## 7. Full \(X/Y\), endpoint, and scope audit

### Lower resources

The contradiction does not arise from a repeated lower vertex before the
second router. Grant all three distinct lower states in (4.3). The
cross-preload and the later one-hot form (4.6) are compatible as sets.
Their incompatibility is temporal.

### Upper resources

The exact failed upper is (4.5). It must occur once in the \(C_6\) upper
shore. The two alternating matchings exhaust its two possible cycle
owners, and both owners backtrack. Assigning it to the inactive fourth
path would no longer be the stated \(C_6\) switch and would leave one of
its cycle lower degrees unmatched. Thus there is no exact full upper
collar ledger.

### Physical versus transported supports

Fix a physical tail frame \(\Lambda\) which labels the literal suffix
segments and their \(X/Y\) vertices. If two fixed physical faces
\(F_1,F_2\subseteq\Lambda\) share \(x,y\), let
\(\pi_\varepsilon\) be the predecessor map from the second cut back to the
first in setting \(\varepsilon\). Assume the intervening collars are
owner-preserving on these transported strands. The first face-supported
3-cycle then maps \(F_1\) setwise, so

\[
 \pi_\varepsilon^{-1}(\{x,y\})\subseteq F_1,
 \qquad \varepsilon=0,1.                              \tag{7.1}
\]

The oldness argument therefore forces both future petals into every
first-face predecessor in both settings. At the second physical face one
setting owns the shared upper from \(H+q_x\), while the toggled setting
owns it from \(H+q_y\). They contain respectively the two forbidden
restitutions.

If (7.1) is evaded by transporting the face name differently in the two
settings, the physical lower and upper shores differ. A larger adaptive
union of those faces is not covered by Theorem 4.1, but it is also not a
three-\(C_6\) packet with a common exact resource ledger.

Likewise, an intervening owner-changing seam can invalidate (7.1), but
that seam is another router. Its endpoint action, state resources, and
collars must be included in the monodromy and storage ledgers.

### Endpoint monodromy

Equation (0.1) is correct. The no-go grants it. Monodromy records which
tail owner reaches which endpoint; it does not record how many times a
physical coordinate changes membership. By Lemma 2.1 the offending row
has at least one exchange of excess over its endpoint distance. Hence it
cannot be a minimum root-to-complement wreath row even though the formal
tail permutation is identity.

### Floor and integrality

The obstruction is finite and integral. It uses two physical root paths,
two old coordinates, and one mandatory upper colour. There are no
asymptotic estimates, fractional matchings, floor baselines, or omitted
resources.

### Exact scope

The theorem applies inside one chosen root-to-complement geodesic half.
It does not automatically apply across the cyclic infinity edge, where a
literal cyclic word and both crossing collars would have to be displayed.

The theorem permits arbitrary collars between completed outgoing routers,
provided they remain on the same geodesic rows. It rules out passive
storage and passive rank suspension. It does not rule out:

1. a fused use of one-way star-to-triangle packets which avoids presenting
   any later common-core old-petal shore after the forced cross deletions;
   merely delaying their terminal \(C_6\)'s is not sufficient;
2. replacing the second common-core star by a genuine higher-distance
   multi-petal alternating atom;
3. an additional owner-changing router whose monodromy and all resources
   are included in a larger relation; or
4. a packet deliberately crossing infinity with a literal OR-word proof.

None of these escapes is supplied by the identity (0.1), and none is
constructed here.

## 8. Independently audited boundary

Three independent audits agree on the following points.

1. The permutation identity is exact, with chronological order (1.1)
   under the stated convention.
2. The three support intersections are exactly the pairs in (0.3).
3. The forced cross-preload (4.2) follows from oldness, geodesicity, and
   the first common-core shore.
4. The second shore forces the two deletions in (4.4).
5. The upper colour (4.5) is mandatory, and its two possible owners give
   the two prohibited restitutions.
6. Completed paired packets satisfy the stronger permanent-scar theorem.
7. Fixed physical face labels make the obstruction simultaneous in both
   settings; setting-dependent transported labels instead destroy the
   common literal \(X/Y\) ledger.

Accordingly the precise proved boundary is:

\[
\boxed{
\begin{gathered}
\text{fixed-face, distinct-old-and-retained three-reservoir
tetrahedral storage is impossible;}\\
\text{abstract identity monodromy survives;}\\
\text{an adaptive multi-face, fused non-star, or infinity-crossing
construction remains unproved rather than disproved.}
\end{gathered}}                                        \tag{8.1}
\]
