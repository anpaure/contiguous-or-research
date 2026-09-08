# A single dominance staircase for a cluster of PBBS cuts

Date: 2026-07-25

## 0. Theorem

The one-cut Pareto staircase extends exactly to every cluster of cuts lying
in one owner interval.  Let

\[
  X_i\in\binom{[n]}{m+1}
\]

be a directed Johnson trajectory, and let \(\mathcal C\) be selected cuts
between \(X_{c-1}\) and \(X_c\).  Put

\[
 c_0=\min\mathcal C,\qquad c_1=\max\mathcal C,
 \qquad S=c_1-c_0.                                  \tag{0.1}
\]

If

\[
 2H+S\le m+1,                                      \tag{0.2}
\]

then one nonzero word of length

\[
 \boxed{2H+2S-1}                                   \tag{0.3}
\]

represents every floor-correct intersection of at most \(H+1\)
consecutive owners which crosses at least one cut in \(\mathcal C\).

Together with the shared upper compiler in
`PBBS_GLOBAL_UPPER_SEAM_SHARING_20260725.md`, all lower and upper crossing
targets of this cluster have one word of length at most

\[
 \boxed{4H+3S+|\mathcal C|-2}.                     \tag{0.4}
\]

For \(S=0\), (0.3) is the \(2H-1\) one-cut staircase and (0.4) is the
exact \(4H-1\) one-cut chart.

This proves genuine cross-cut sharing: a cluster of arbitrarily many cuts
in span \(S\) costs by span, not by \(H|\mathcal C|\).  It still does not
by itself give an \(o(W)\) global excess, because the total span of active
clusters may be a positive fraction of all owner edges.

## 1. Global endpoint coordinates

Every maximal positive run of a coordinate \(x\) on the owner trajectory
is an integer owner interval

\[
  [L,R]\quad\text{on which }x\in X_i.              \tag{1.1}
\]

Consider the endpoint rectangle

\[
 \mathcal R=
 [\,1-c_1,\ H-c_0\,]
 \times
 [\,c_0,\ c_1+H-1\,].                             \tag{1.2}
\]

Discard a run if \(-L<1-c_1\) or \(R<c_0\), since it cannot contain any
owner interval indexed by a point of \(\mathcal R\).  To every remaining
run attach the upper-clipped point

\[
 p(L,R)=
 \left(
   \min\{-L,H-c_0\},
   \min\{R,c_1+H-1\}
 \right),                                          \tag{1.3}
\]

Let \(\mathcal D\) be the multiset of these points over all remaining
maximal positive runs of all coordinates.  Thus no lower clipping is
performed; points which lie below the rectangle in either coordinate are
discarded.

For \(z=(\alpha,\beta)\in\mathcal R\), put

\[
  W_z=\bigcap_{i=-\alpha}^{\beta}X_i.              \tag{1.4}
\]

### Lemma 1.1 (global dominance formula)

For every \(z\in\mathcal R\),

\[
 \boxed{
 W_z=\{x:\text{some }p\in\mathcal D
                 \text{ belonging to }x\text{ satisfies }p\ge z\}.}
                                                               \tag{1.5}
\]

#### Proof

A coordinate belongs to (1.4) precisely when one of its maximal positive
runs contains the full owner interval \([-\alpha,\beta]\).  Before
clipping, this is exactly

\[
  L\le-\alpha,\qquad R\ge\beta,
\]

or \((-L,R)\ge(\alpha,\beta)\).  Since \(z\) lies in \(\mathcal R\),
discarding points below the rectangle and clipping only above its upper
corner does not change either comparison. \(\square\)

## 2. Floor correctness again excludes southwest points

Let \([a,b]\) be an owner interval of length at most \(H+1\) which
crosses a selected cut, and write

\[
 q=(-a,b)\in\mathcal R.                            \tag{2.1}
\]

Its floor rank is

\[
 m+2-(b-a+1).                                      \tag{2.2}
\]

### Lemma 2.1 (global southwest exclusion)

If

\[
 \left|\bigcap_{i=a}^bX_i\right|
 =m+2-(b-a+1),                                     \tag{2.3}
\]

then no point of \(\mathcal D\) is strictly southwest of \(q\).

#### Proof

A point strictly southwest of \((-a,b)\) comes from a positive run with

\[
 L>a,\qquad R<b.                                   \tag{2.4}
\]

(Clipping cannot create strict inequalities which were absent before
clipping.)  Thus the coordinate has an internal arrival and a later
internal departure inside \(X_a,\ldots,X_b\).

Map every coordinate of \(X_a\) missing from the total intersection to
its first departure transition.  The map is injective, because one
Johnson transition removes one coordinate.  The later departure in (2.4)
is not used by this map: the coordinate is either absent from \(X_a\), or
it already departed before its internal arrival.  Hence at most
\((b-a)-1\) of the \(b-a\) transitions are used.  The intersection has
size at least

\[
 (m+1)-((b-a)-1)=m+2-(b-a),
\]

one larger than (2.3), a contradiction. \(\square\)

## 3. One global Pareto path

Discard multiplicities from \(\mathcal D\), take its Pareto-minimal
points, and list them with increasing first and decreasing second
coordinate.  Construct an east-before-south unit path \(\Gamma\) through
them, beginning at the northwest corner

\[
  (1-c_1,c_1+H-1)                                  \tag{3.1}
\]

and ending at the southeast corner

\[
  (H-c_0,c_0).                                     \tag{3.2}
\]

The horizontal and vertical ranges both equal \(H+S-1\), so

\[
 \boxed{|V(\Gamma)|=2H+2S-1.}                     \tag{3.3}
\]

The rectangle-interception proof from the one-cut theorem applies
verbatim:

### Lemma 3.1

If \(q\in\mathcal R\) has no point of \(\mathcal D\) strictly southwest
of it and \(p\in\mathcal D\) satisfies \(p\ge q\), then

\[
 V(\Gamma)\cap[q,p]\ne\varnothing.                \tag{3.4}
\]

Indeed, descend under \(p\) to a Pareto minimum.  If it is west/north of
\(q\), follow the east-before-south path forward to the vertical line of
\(q\); if it is east/south, follow backward to the horizontal line.  A
premature crossing would exhibit a Pareto point strictly southwest of
\(q\).

## 4. Literal cluster identity

Emit the actual set-letters \(W_z\) from (1.4) in the order of \(\Gamma\).

### Theorem 4.1

For every floor-correct query \(q=(-a,b)\) corresponding to a
length-at-most-\((H+1)\) owner interval crossing a selected cut,

\[
 \boxed{
 \bigcap_{i=a}^bX_i
 =\bigcup_{\substack{z\in V(\Gamma)\\z\ge q}}W_z.} \tag{4.1}
\]

The letters on the right are one contiguous subword, and every emitted
letter is nonempty.

#### Proof

Along \(\Gamma\), the first coordinate is nondecreasing and the second is
nonincreasing.  Hence \(z_1\ge q_1\) selects a suffix and
\(z_2\ge q_2\) a prefix; their intersection is contiguous.

Lemma 1.1 shows every selected \(W_z\) is contained in the query
intersection.  Conversely, if \(x\) belongs to the query, Lemma 1.1 gives
a run point \(p\ge q\) belonging to \(x\).  Lemmas 2.1 and 3.1 supply a
path vertex \(z\in[q,p]\), and then \(x\in W_z\).  This proves (4.1).

Finally every path vertex lies in \(\mathcal R\).  The owner interval in
(1.4) has at most

\[
 (H-c_0)+(c_1+H-1)+1=2H+S                         \tag{4.2}
\]

owners.  An intersection of \(L\) consecutive rank-\((m+1)\) Johnson
owners has size at least \(m+2-L\).  Assumption (0.2) therefore makes every
letter nonempty. \(\square\)

The upper transition neighbourhood of this cluster is contained in one
interval of at most \(2H+S-1\) transition indices.  The shared upper theorem
therefore costs at most

\[
 2H+S-1+|\mathcal C|.                              \tag{4.3}
\]

Adding (3.3) and (4.3) proves (0.4).

## 5. Remaining accounting boundary

Partition selected cuts on a long owner component into clusters satisfying
(0.2).  The chart cost is controlled by the sum of the internal cluster
spans plus \(H\) times the number of clusters.  Taking clusters of maximum
allowed span can recover all local \(H\)-multiplicity caused by dense cuts.
But in the worst distribution allowed by the present residence estimates,
the internal spans of the clusters can sum to a positive fraction of the
owner component lengths.  After deck lifting this is \(\Theta(W)\), not
\(o(W)\).

Thus the cross-cut geometry itself is now linear both locally and by
cluster.  The coefficient-one issue has moved to an accounting/reuse
question: either these global chart letters must replace principal
\(W\)-letters, rather than being appended, or PBBS-specific support
collisions must make the active cluster span \(o(W)\).

## 6. The span term is unavoidable for arbitrary Johnson collars

The dependence on \(S\) in (0.3) is not an artifact of the global
staircase proof.

### Proposition 6.1 (fixed-rank span obstruction)

Let \(2H\le T\le m\).  There is a rank-\((m+1)\) Johnson path of \(T\)
transitions and a set of cuts with gaps at most \(H\) for which
\(\Theta(T)\) distinct floor-correct depth-\(H\) lower targets cross the
cuts.  Every word covering these targets has length \(\Omega(T)\).

#### Proof

Take pairwise distinct coordinates

\[
 a_1,\ldots,a_{m+1},b_1,\ldots,b_T,
\]

which is possible because \(m+1+T\le2m+1\).  Start with

\[
 X_0=\{a_1,\ldots,a_{m+1}\}
\]

and, for \(1\le i\le T\), put

\[
 X_i=X_{i-1}-\{a_i\}+\{b_i\}.                     \tag{6.1}
\]

This is a Johnson path.  For every \(0\le j\le T-H\),

\[
 \bigcap_{i=j}^{j+H}X_i
 =\{b_1,\ldots,b_j\}
  \cup\{a_{j+H+1},\ldots,a_{m+1}\}.              \tag{6.2}
\]

These sets all have rank \(m+1-H\), are floor-correct, and are pairwise
distinct.

Choose cuts at \(H,2H,3H,\ldots,kH\), where
\(kH\le T-H+1<(k+1)H\).  The depth-\(H\) owner window beginning at \(j\)
crosses one of these cuts for every \(0\le j<kH\), since the start ranges

\[
 [c-H,c-1]
\]

tile \([0,kH-1]\).  Hence \(kH=T-O(H)=\Theta(T)\) distinct targets of
one rank require coverage.

Suffix ORs ending at one word position form a chain and contain at most
one set of a fixed rank.  Thus the word has at least \(kH=\Omega(T)\)
positions. \(\square\)

This does not assert that the monotone collar occurs with positive density
in the canonical PBBS factor.  It proves the sharp logical limitation:
no theorem using only Johnson adjacency, floor correctness, and cut
spacing can improve the global cluster cost from order active span to
little-oh active span.  A coefficient-one gain beyond the cluster theorem
must use additional PBBS structure or replacement of baseline letters.

## 7. Removing the \(HJ\) endpoint-initialization ledger by clustering

The cluster chart can also share the \(H\) dummy erosion entries formerly
paid at every path start.  This is important: sharing only the crossing
targets would leave the endpoint term \(HJ\) untouched.

Cut an owner cycle at a set \(\mathcal C\), and write every resulting path
with local owner indices \(0,\ldots,v-1\).  Use the endpoint-capped erosion
letters

\[
 D_i=\bigcap_{h=0}^H\widetilde X_{i+h},
 \qquad 0\le i\le v-1,                             \tag{7.1}
\]

but omit the usual negative-index prefix
\(D_{-H},\ldots,D_{-1}\).  Thus the base erosion contribution is exactly
\(v\), and over all paths exactly the original component length \(\ell\).

### Lemma 7.1 (which witnesses the omitted prefix carried)

Let an intended owner window in one path begin at offset \(b\ge0\) and
contain \(p\le H+1\) owners.

1. Its lower-intersection witness from (22.4) uses only nonnegative
   erosion indices unless

   \[
      b+p-1\le H-1.                                \tag{7.2}
   \]

2. Its upper-union witness from (22.5) uses only nonnegative erosion
   indices whenever \(b\ge H\).

#### Proof

For the lower target, Lemma 22.1 chooses

\[
 i=b-H+p-1.
\]

Thus \(i<0\) is exactly (7.2).  For the upper target it chooses
\(i=b-H\), which is nonnegative exactly when \(b\ge H\). \(\square\)

Therefore all lower targets lost by omitting the dummy prefix lie wholly
inside the first \(H\) owners of a path.  All upper targets lost this way
begin among the first \(H\) owners and end no later than the first \(2H\)
owners.

Now take one cluster of actual path starts/cuts \(\mathcal C_0\), of span
\(S\).  Add the virtual cuts

\[
 \mathcal V=
 \bigcup_{c\in\mathcal C_0}
 \{c,c+1,\ldots,c+H-1\}.                           \tag{7.3}
\]

Its span is at most \(S+H-1\).  Every lower target in (7.2) containing at
least two owners crosses a member of \(\mathcal V\); singleton targets are
owners and will be covered by the upper owner halo below.  Every original
crossing lower target crosses the actual member \(c\in\mathcal V\).

If

\[
 3H+S\le m+1,                                      \tag{7.4}
\]

Theorem 4.1 applied to \(\mathcal V\) gives all these lower targets in at
most

\[
 2H+2(S+H-1)-1=4H+2S-3                           \tag{7.5}
\]

letters.

All crossing upper targets and all upper targets beginning among the first
\(H\) owners of a path lie in the original owner interval

\[
 X_{c_0-H},X_{c_0-H+1},\ldots,X_{c_1+2H-1}.       \tag{7.6}
\]

Emitting this chronological owner halo costs \(S+3H\) letters and covers
each such union by its literal owner subinterval.  It also covers every
singleton omitted in the lower accounting.

### Theorem 7.2 (clustered endpoint-and-seam compiler)

For a cut cluster of span \(S\) satisfying (7.4), the endpoint-capped base
may be truncated to the \(v\) nonnegative erosion letters on every path.
All correct lower and upper targets lost either at the cuts or through the
omitted negative prefixes are restored by an auxiliary word of length at
most

\[
 \boxed{7H+3S-3.}                                  \tag{7.7}
\]

Consequently, if the cut set of a component is partitioned into clusters
\(\mathcal C_1,\ldots,\mathcal C_K\) of spans \(S_j\) satisfying (7.4),
then the complete central-band word has length at most

\[
 \boxed{
 \ell+\sum_{j=1}^K(7H+3S_j-3).}                  \tag{7.8}
\]

#### Proof

Keep the \(\ell\) nonnegative erosion entries (7.1).  Lemma 7.1 shows that
every target they no longer certify belongs to one of the two halo families
just described.  The virtual-cut dominance chart proves the lower
witnesses, and the owner segment (7.6) proves the upper witnesses and
singletons.  Concatenate the blocks; all designated witnesses remain
internal to one block.  Summing (7.5) and (7.6) gives (7.7), then (7.8).
\(\square\)

This removes the old \(HJ\) endpoint charge together with the independent
seam charges.  Dense cuts are now paid only by cluster span.  Nevertheless,
the sum of the spans in (7.8) can still be \(\Theta(\ell)\), and
Proposition 6.1 shows that this order cannot be beaten for arbitrary
Johnson collars by an append-only repair.  The remaining coefficient-one
step is still PBBS-specific baseline replacement or defect collapse.

## 8. Exact clustered-span sufficient gate for constant one

For a fixed \(A>0\), put \(H=\lceil A\sqrt m\rceil\).  On every active
physical PBBS owner cycle, choose a cut transversal of all positive
residences of length at most \(H\), and partition its cuts into clusters
with spans \(S_j\) satisfying

\[
 3H+S_j\le m+1.                                    \tag{8.1}
\]

Define the physical clustered-span cost

\[
 \mathfrak S_H
 =\sum_{\text{all clusters }j}(7H+3S_j-3).        \tag{8.2}
\]

### Theorem 8.1 (global-fusion reduction)

If, for every fixed \(A\), such transversals and partitions can be chosen
with

\[
 \boxed{\mathfrak S_{\lceil A\sqrt m\rceil}=o_A(W),} \tag{CS_A}
\]

then

\[
 \nu(k)\le(1+o(1))
 \binom{k}{\lfloor k/2\rfloor}.                    \tag{8.3}
\]

#### Proof

Use cyclic erosion on inactive cycles, costing their owner lengths plus at
most \(2H\) per cycle.  On active cycles use Theorem 7.2.  The total owner
length is \(W\), and the number of projected owner cycles is at most
\(B_m=W/(2m+1)\).  Hence the complete literal central-band word has length

\[
 W+2HB_m+\mathfrak S_H.                            \tag{8.4}
\]

It covers every correct lower and upper PBBS target through depth \(H\),
by the all-depth support theorem and the internal, endpoint, and seam
ledgers above.  For fixed \(A\),

\[
 \frac{HB_m}{W}=O_A(m^{-1/2})=o_A(1),
\]

and \((CS_A)\) handles the remaining term.  Diagonalize over integer
\(A\) exactly as in Theorems 22.2 and 9.1, then append the audited
product-SCD tail and use the trimmed parity lift. \(\square\)

The deck-invariant quotient version asks for clustered-span cost
\(o_A(B_m)\), since every quotient chart has \(2m+1\) spatial lifts.  The
best present direct packing estimate and the cluster construction give only
\(O_A(B_m)\): the cuts may form clusters whose internal spans cover a
positive fraction of all quotient edges.  Thus the exact remaining factor
is now a vanishing **active-span density**, not an \(H\)-factor in the
one-cut literal repair.
