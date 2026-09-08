# Odd current: every quiet source enters a noncanonical clock minor

**Date:** 2026-08-06  
**Method:** literal first-nonquiet scan dynamics; no computation or search  
**Status:** unconditional labelled strict-gammoid minor, explicit
macroscopic noncanonical surplus basis, and exact terminal obstruction.
Every central quiet source enters a noncanonical active-clock slice, and a
reversible zipper links all sources disjointly to one root-coded terminal
basis.  Inside each clock slice the contracted digraph contains an exact
subdivision of the remaining nearest-neighbour token graph, and hub colours
are read injectively from the clock signature and the merged tail.  A
fixed clock-tail component nevertheless fixes one boundary coordinate, so
it contains no complete physical boundary edge.  The remaining labelled
odd theorem is therefore a boundary-aperture paired linkage from the new
basis, not construction of a noncanonical basis.

## 1. A boundary-last scan

Put

\[
 n=2m+1
\]

and cut the coordinate cycle at

\[
 e_\partial=\{2m,0\}.
\]

Use the coordinate pairs

\[
 p_i=(2i-1,2i)\quad(1\le i<m),
 \qquad p_m=(2m,0),
\]

leaving coordinate (2m-1) unpaired.  Inspect the pairs in the order

\[
                         p_1,p_2,\ldots,p_m,
\tag{1.1}
\]

so the physical boundary pair is last.  On every ordered pair use

\[
 01\leftrightarrow10,
 \qquad02\leftrightarrow11,
 \qquad12\leftrightarrow21,
\tag{1.2}
\]

and call

\[
 q(0)=00,\qquad q(1)=20,\qquad q(2)=22
\tag{1.3}
\]

quiet.  Let \(M_{\rm scan}=P\mathbin{\dot\cup}N\), where \(P\) consists
of the selected edges supported on \(p_m\), and orient the cut-open graph
relative to \(N\) as in the first-scan gammoid theorem.  Delete \(V(P)\)
and call the resulting digraph \(D'\).

At odd mass (R=2s+1), the source set is

\[
 Q=\{q(u_1)\cdots q(u_m)\text{ with root digit }1:
          u\in{\cal T}_{m,s}\}.
\tag{1.4}
\]

At central mass (R=n), one has (s=m).

## 2. The active-clock subdivision

Fix an index (i<m).  Fix quiet values on every earlier scan pair
(p_1,\ldots,p_{i-1}), and fix one of the three nonquiet rows

\[
                         \alpha\leftrightarrow\bar\alpha
\tag{2.1}
\]

from (1.2) on \(p_i\).  All later coordinates, including the two boundary
coordinates, will be called the tail.

Let (G_{\rm tail}) be any induced nearest-neighbour token graph obtained
by allowing physical nonwrap transfers whose support is disjoint from

\[
                         p_1\cup\cdots\cup p_i.
\tag{2.2}
\]

The total mass and all fixed coordinates are held constant.  For a tail
state \(z\), exactly one of

\[
 (\alpha,z),\qquad(\bar\alpha,z)
\]

lies on the majority shore.  Denote it by \(\iota(z)\).

### Theorem 2.1 (clocked tail minor)

Every directed version (z\to z') of an edge of (G_{\rm tail}) lifts
to a directed two-arc path

\[
                  \iota(z)\longrightarrow \eta(z,z')
                    \longrightarrow\iota(z')
\tag{2.3}
\]

in (D').  If tail paths are pairwise vertex-disjoint, their lifted
directed paths are pairwise vertex-disjoint.  Thus, after suppressing the
middle vertices in (2.3), \(D'\) has a strict-gammoid minor isomorphic to
the bidirected graph (G_{\rm tail}).

#### Proof

Apply the tail transfer (z\to z') to the majority-shore state
\(\iota(z)\).  It is a nonmatching edge, because its support is disjoint
from \(p_i\).  It reverses the cut-open shore and changes none of the
earlier quiet pairs or the active pair \(p_i\).  Hence \(p_i\) is still
the first nonquiet scan pair at the intermediate state.  The matching edge
of \(N\) therefore toggles (2.1), producing the unique majority-shore
state over \(z'\), namely \(\iota(z')\).  This is (2.3).

The middle vertex in a lifted arc entering (z') is exactly the
\(N\)-mate of \(\iota(z')\).  Consequently two lifted paths can share a
middle vertex only when their tail paths share the corresponding tail
vertex.  Vertex-disjoint tail paths therefore lift vertex-disjointly.
All vertices in (2.3) have first nonquiet pair \(p_i\), which precedes the
boundary pair in (1.1), so none belongs to \(V(P)\).  Hence the paths lie
in \(D'\).  \(\square\)

This is a genuinely noncanonical minor: every one of its ordinary
majority vertices has an active nonquiet clock pair, whereas the canonical
source basis is entirely quiet.

## 3. A two-arc entrance from a quiet digit one

Suppose a quiet source \(x(u)\in Q\) has

\[
                         u_i=1\qquad(i<m).
\tag{3.1}
\]

On \(p_i\), perform the physical transfer

\[
                         20\longrightarrow11.
\tag{3.2}
\]

This edge is not selected by the scan, whose mass-two row is
(02\leftrightarrow11).  The scan then uses

\[
                         11\longrightarrow02.
\tag{3.3}
\]

### Lemma 3.1 (one-clock entrance)

If every earlier pair is quiet, (3.2)--(3.3) is a directed path in \(D'\)
from the quiet source to the clocked tail minor with active row
(02\leftrightarrow11).

#### Proof

The quiet source lies on the majority shore.  The nonwrap edge (3.2)
reverses the shore.  Its endpoint has first nonquiet pair \(p_i\), so the
oriented matching edge is exactly (3.3), back to the majority shore.
Since \(i<m\), neither vertex is deleted with \(V(P)\).  \(\square\)

For a family of sources, choosing the first internal digit one makes the
entrance paths disjoint between different clock indices, different quiet
prefixes, and different tails.

## 4. Quiet sources with no internal digit one

The remaining sources have

\[
                         u_1,\ldots,u_{m-1}\in\{0,2\}.
\tag{4.1}
\]

There are two literal two-pair entrances.  Across a connector between
successive scan pairs,

\[
\begin{aligned}
 22\mid00&\longrightarrow21\mid10,\\
 00\mid22&\longrightarrow01\mid12.
\end{aligned}
\tag{4.2}
\]

The earlier of the two changed scan pairs is nonquiet, so \(N\) toggles
it by respectively

\[
                         21\leftrightarrow12,
 \qquad                  01\leftrightarrow10.
\tag{4.3}
\]

The same construction works across the connector \(\{0,1\}\) between
the second coordinate of \(p_m\) and the first coordinate of \(p_1\);
then \(p_1\) is the first nonquiet pair.  The boundary pair itself is only
a later marker and hence the state is not in \(V(P)\).

### Lemma 4.1 (binary-change entrance)

Every transition in (4.2), followed by the appropriate row in (4.3), is
a directed two-arc path from the quiet source into a clocked tail minor.

The proof is identical to Lemma 3.1: the first edge reverses the shore and
the second is precisely the first-nonquiet matching edge.

### Theorem 4.2 (complete central clock activation)

Assume (m\ge3) and central compressed mass

\[
                         \sum_{j=1}^m u_j=m.
\tag{4.4}
\]

Every quiet source admits one of the entrances in Lemma 3.1 or Lemma 4.1.
Moreover the sources can be partitioned by their first chosen entrance so
that different parts occupy disjoint clock slices.

#### Proof

If some internal digit \(u_i\) equals one, use the least such \(i\) and
Lemma 3.1.

Otherwise all internal digits are zero or two.  They cannot all be zero:
then (4.4) would give \(u_m=m>2\).  They cannot all be two: then
\(u_m=2-m<0\).  Thus, for \(m\ge3\), the internal word contains both
symbols, and two successive internal pairs with different digits give
(4.2).

Partition by the least scan index at which the selected entrance becomes
nonquiet, its quiet prefix, and its active row.  Distinct data cannot meet:
the least nonquiet pair, its local row, or an earlier fixed quiet value is
different.  \(\square\)

The only residue one sees before applying Lemma 4.1 is the binary middle
layer

\[
 \{u\in\{0,2\}^m:\sum u_i=m\},
\tag{4.5}
\]

which is empty for odd \(m\) and has size \({m\choose m/2}\) for even
\(m\).  Lemma 4.1 absorbs this entire residue; it is not a new scalar
defect.

## 5. A reversible zipper moves every clock to the first pair

The previous section puts the active clock at a source-dependent scan
pair.  There is an exact directed handoff which moves it toward \(p_1\).

For \(b\in\{0,2\}\), write

\[
                         c(b)=(1,b).
\tag{5.1}
\]

Thus \(c(0)=10\) and \(c(2)=12\).  For \(b,c\in\{0,2\}\), the connector
between two successive scan pairs gives the directed rewrite

\[
             q(b)\mid c(c)
       \longrightarrow
             \begin{cases}
                01\mid(0,c),&b=0,\\
                21\mid(2,c),&b=2,
             \end{cases}
       \longrightarrow
             c(b)\mid(b,c).
\tag{5.2}
\]

The first arrow is a physical connector transfer.  The second is the
first-nonquiet scan edge \(01\to10\) or \(21\to12\).

### Lemma 5.1 (binary clock zipper)

For \(b_1,\ldots,b_j\in\{0,2\}\), repeated use of (5.2) gives a directed
path

\[
 q(b_1)\cdots q(b_{j-1})c(b_j)
 \leadsto
 c(b_1)(b_1,b_2)\cdots(b_{j-1},b_j).
\tag{5.3}
\]

Every majority-shore state in (5.3) has a unique first active clock, and
the state together with that clock position recovers the original binary
prefix.

#### Proof

Equation (5.2) moves the least nonquiet pair one place to the left.  It
leaves behind the ordered pair \((b,c)\), so one can reverse the rewrite
by reading its two entries.  Induction gives (5.3) and the recovery
statement.  \(\square\)

The two source activations also have a reversible binary form.  If the
first internal code one is preceded by \(b\in\{0,2\}\), then

\[
                         q(b)q(1)\leadsto c(b)c(b).
\tag{5.4}
\]

For \(b=0\), this is the two-arc path

\[
                         00\mid20\to01\mid10\to10\mid10.
\]

For \(b=2\), use the separate literal route

\[
 22\mid20\to22\mid11\to22\mid02
       \to21\mid12\to12\mid12.
\]

Its final connector step has the same binary output as (5.2), but its
input clock is \(02\), not \(c(2)\), so it is not literally an instance
of (5.2).  A binary change has instead

\[
                 q(b)q(2-b)\leadsto c(b)c(2-b).
\tag{5.5}
\]

Thus equality of the two final \(c\)-labels identifies the code-one
activation, while inequality identifies the binary-change activation.

Choose the activations deterministically as follows.

1. If \(i\) is the first internal index with \(u_i=1\), use Lemma 3.1
   when \(i=1\).  When \(i>1\), use (5.4); in its \(b=2\) branch this
   includes the preliminary \(20\to11\to02\) step displayed above.
2. If there is no internal code one, inspect the internal connectors
   \(p_1p_2,p_2p_3,\ldots\), and use (5.5) at the first zero/two
   change.  Theorem 4.2 proves that such a change exists.

After an internal activation, apply the zipper (5.3) until the active
clock is \(p_1\).  Call the resulting terminal set \(A_{\rm clk}\).

### Theorem 5.2 (noncanonical root-coded surplus basis)

The canonical promotion paths from all \(q\in Q\) to \(A_{\rm clk}\) are
pairwise vertex-disjoint.  Consequently

\[
                         |A_{\rm clk}|=|Q|
\]

and \(A_{\rm clk}\) is a basis of the contracted surplus gammoid
\(S/V(P)\).  Every member of \(A_{\rm clk}\) has \(p_1\) nonquiet relative
to the original scan.  Except for the direct \(p_1:20\to11\to02\) branch,
the terminal has at least two literal coordinates equal to one and hence
lies outside the union of all canonical quiet-root bases.

#### Proof

At a majority-shore vertex on a promotion path, the least nonquiet scan
pair is the current clock position.  Starting there, reverse (5.2).  The
overlapping markers \((b_j,b_{j+1})\) recover the binary prefix uniquely.
At the terminal activation, (5.4)--(5.5) distinguish a first code one
from a binary change and recover the activation source.  The untouched
suffix and boundary pair recover every remaining quiet code.  Hence a
majority-shore state on
the selected paths determines its source and its position on that source
path.

Every minority-shore intermediate is the unique \(N\)-mate of the next
majority-shore state.  Collision of two intermediate vertices would
therefore imply collision of the corresponding next majority vertices.
The whole path family is vertex-disjoint.

The strict-gammoid representation theorem now says that the terminal set
of a linkage from all sources \(Q\) is a basis of \(S/V(P)\).  Finally
\(p_1\) is visibly nonquiet at every terminal.  \(\square\)

This is an explicit macroscopic surplus basis beyond all canonical
quiet-root exchange cubes.  It does not yet pair that basis by boundary
edges.

## 6. A universal coordinate-zero aperture

The root-coded basis can be pushed all the way to the boundary coordinate.
First take a promoted terminal with

\[
                         p_1=c(b)=(1,b),
 \qquad b\in\{0,2\},
\tag{6.1}
\]

and let \(d\in\{0,2\}\) be its value at coordinate zero.  Across
\(\{0,1\}\), make the unique transfer which changes coordinate zero to
one:

\[
\begin{cases}
\text{move coordinate }1\text{ to }0,&d=0,\\
\text{move coordinate }0\text{ to }1,&d=2.
\end{cases}
\tag{6.2}
\]

At the intermediate state,

\[
                         p_1=(d,b),
 \qquad                  t_0=1.
\tag{6.3}
\]

If \((d,b)\ne(0,2)\), the pair \(p_1\) is one of \(00,20,22\) and is
quiet.  The scan therefore toggles the next readable nonquiet marker in
the zipper trail.  Such a marker exists: it is at worst the terminal
\(c\)-label left by (5.4) or (5.5).  In the exceptional case
\((d,b)=(0,2)\), the pair \(p_1=02\) is itself nonquiet and the scan
toggles it to \(11\).

There is one source class not covered by (6.1).

1. If the first code one occurs already at \(p_1\), then the usual
   entrance ends at \(p_1=02\).  When \(d=2\), use
   \[
       20\to11\to02,\qquad
       (02,t_0=2)\to(12,t_0=1)\to(21,t_0=1).
   \tag{6.4}
   \]
   When \(d=0\), bypass the \(02\) entrance and use \(\{0,1\}\)
   directly from the quiet source:
   \[
       (20,t_0=0)\to(10,t_0=1)\to(01,t_0=1).
   \tag{6.5}
   \]

Call the resulting terminal set \(A_\partial\).

### Theorem 6.1 (injective boundary aperture)

The source paths to \(A_{\rm clk}\), with the direct \(u_1=1,d=0\)
branch replaced by (6.5), give pairwise vertex-disjoint directed paths
from all \(Q\) onto \(A_\partial\).  Every
\(a\in A_\partial\) satisfies

\[
                         a_0=1.
\tag{6.6}
\]

Consequently \(A_\partial\) is another basis of \(S/V(P)\).

#### Proof

For a terminal of the form (6.1), the physical arrow (6.2) reverses the
cut-open shore.  If \(p_1\) becomes quiet, the next nonquiet zipper marker
is the first scan row and its \(N\)-edge returns to the majority shore.
If \(p_1=02\), its own \(N\)-edge does so.  Equations (6.4)--(6.5) are
the same physical-edge-then-\(N\)-edge rule written out for the direct
\(p_1\) activation.

The extension is reverse-decodable.  In the generic branch, the post-step
state of \(p_1\) is respectively

\[
                         00,\quad11,\quad20,\quad22
\]

for \((d,b)=(0,0),(0,2),(2,0),(2,2)\).  It therefore recovers \(d,b\)
and the direction of (6.2); the toggled marker then recovers the zipper
trail.  The direct branches end with the distinct signatures

\[
 (p_1,\text{boundary pair})=(01,01\text{ or }21),\quad(21,21),
\]

Thus every majority vertex in an aperture extension recovers its source
and its route.  Every minority intermediate is again the unique
\(N\)-mate of its next majority vertex.

All new aperture vertices have coordinate zero equal to one, whereas the
earlier promotion paths have coordinate zero zero or two.  The generic
and direct signatures displayed above are disjoint.  Hence no new path
meets an old path or another extension.
The strict-gammoid basis conclusion follows.  \(\square\)

### Corollary 6.2 (automatic hub rainbow on the aperture bank)

Choose one physical boundary occurrence incident with every
\(a\in A_\partial\).  The resulting occurrences have pairwise distinct
unpointed hub colours.

#### Proof

The hub keeps every nonboundary coordinate and replaces coordinates
\(2m,0\) by their sum.  Inside \(A_\partial\), coordinate zero is known
to equal one.  Hence the merged value recovers coordinate \(2m\) by
subtracting one, and the hub recovers the entire terminal \(a\).
Distinct terminals therefore have distinct hubs.  In fact the construction
above leaves boundary pair only \(01\) or \(21\), so every selected
terminal has a unique boundary partner \(10\) or \(12\), respectively.
\(\square\)

This closes individual boundary reachability and hub-colour separation.
At the central mass \(|Q|\) is odd, so the remaining task is to select
\((|Q|-1)/2\) complete boundary edges together with one allowed socket
endpoint inside one surplus basis.

## 7. Exact fundamental-matrix form of the last labelled gate

Index

\[
                         A_\partial=\{a_1,\ldots,a_\delta\},
 \qquad                  \delta=|Q|,
\]

and choose one boundary partner \(b_i\) of every \(a_i\).  Corollary 6.2
implies that the edges \(a_i b_i\) have distinct hubs.  They are also a
matching: different hubs have disjoint boundary fibres, and within one
hub only one edge was chosen.

In the present aperture normal form every boundary pair is \(01\) or
\(21\).  Hence its partner is \(10\) or \(12\), and, literally,

\[
                         b_i=\tau(a_i),
 \qquad                  \tau=(0\ \ 2m).
\tag{7.1}
\]

Thus the partner bank is one fixed coordinate transposition of the
root-clock basis, even though \(\tau\) is not an automorphism of the
cut-open scan digraph.

Normalize a representation of the contracted surplus matroid so that the
columns of \(A_\partial\) form the identity matrix.  Write

\[
                         C=(c_1\ \cdots\ c_\delta)
\tag{7.2}
\]

for the columns representing \(b_1,\ldots,b_\delta\).

### Theorem 7.1 (complementary-minor criterion)

Assume \(\delta\) is even.  For
\(I\subseteq[\delta]\) with \(|I|=\delta/2\), the union of the boundary
edges indexed by \(I\),

\[
                         U_I=\{a_i,b_i:i\in I\},
\tag{7.3}
\]

is a surplus basis if and only if

\[
                         \det C[I^c,I]\ne0.
\tag{7.4}
\]

Consequently the remaining labelled paired-basis theorem is equivalent to
the existence of one nonzero complementary minor (7.4).

#### Proof

The columns of \(U_I\) consist of the identity columns indexed by \(I\)
and the \(C\)-columns indexed by \(I\).  Expanding the determinant along
the identity columns leaves, up to sign, exactly the rows \(I^c\) of the
chosen \(C\)-columns.  This is (7.4).  \(\square\)

At the central mass relevant here, \(\delta\) is in fact odd:

\[
 \delta=[z^m](1+z+z^2)^m
        =\sum_j{m\choose2j}{2j\choose j}\equiv1\pmod2.
\tag{7.5}
\]

Every summand with \(j\ge1\) is even.
Equivalently, the complement involution

\[
                 (u_1,\ldots,u_m)\longmapsto
                 (2-u_1,\ldots,2-u_m)
\]

preserves \(\sum_i u_i=m\) and has the unique fixed point
\((1,\ldots,1)\).  It pairs every other quiet source, proving the same
oddness without coefficient arithmetic.

### Theorem 7.2 (one-socket complementary minor)

Let \(\delta\) be odd, let \(k\) be an allowed socket index, and let

\[
 I\subseteq[\delta]\setminus\{k\},
 \qquad |I|={\delta-1\over2}.
\]

Put

\[
 J=[\delta]\setminus(I\cup\{k\}).
\]

Then

\[
 U_{I,k}=\{a_k\}\cup\{a_i,b_i:i\in I\}
\tag{7.6}
\]

is a surplus basis if and only if

\[
                         \det C[J,I]\ne0.
\tag{7.7}
\]

#### Proof

The retained identity columns have indices \(I\cup\{k\}\).  Expanding
along them leaves the \(C\)-columns indexed by \(I\) and the complementary
row set \(J\).  Both have size \((\delta-1)/2\).  \(\square\)

There is an equivalent skew form.  Put

\[
                         D_x=\operatorname{diag}(x_1,\ldots,x_\delta)
\]

and

\[
                         K(x)=D_xC^{\mathsf T}-CD_x.
\tag{7.8}
\]

### Corollary 7.3 (root-clock Pfaffian)

For even \(\delta\),
\[
                         \operatorname{Pf}K(x)\ne0
\tag{7.9}
\]

if and only if some \(U_I\) in (7.3) is a surplus basis.

For odd \(\delta\), let \(y\) have an independent entry \(y_k\) at every
allowed socket and form

\[
 \widetilde K(x,y)=
 \begin{pmatrix}
 K(x)&y\\
 -y^{\mathsf T}&0
 \end{pmatrix}.
\tag{7.10}
\]

Then \(\operatorname{Pf}\widetilde K(x,y)\ne0\) if and only if some
\(U_{I,k}\) in (7.6) is a surplus basis.

#### Proof

The boundary two-form of the matching \(\{a_i b_i\}\) is

\[
                         \sum_i x_i\,e_i\wedge c_i.
\]

Its matrix in the normalized basis \(A_\partial\) is exactly (7.8).
Pfaffian expansion chooses a set of \(\delta/2\) boundary pairs, and the
coefficient of the corresponding squarefree \(x\)-monomial is, up to
sign, (7.4).  Independent variables prevent cancellation between
different \(I\).  In odd rank, expansion through the dummy row first
chooses one \(y_k\), and the remaining coefficient is exactly (7.7).
\(\square\)

The hub-colour variables are unnecessary in (7.8): Corollary 6.2 has
already made every edge colour private.  For odd \(\delta\), append the
one allowed socket column exactly as in the one-socket coloured Pfaffian
theorem.

Thus the remaining labelled task is no longer an arbitrary coloured
matroid-parity instance.  It is:

\[
\boxed{\text{prove one complementary minor of the root-clock
fundamental matrix \(C\) is nonzero}.}
\tag{7.11}
\]

One sufficient route would be a directed exchange matching in the support
of \(C\) with a unique leading orientation.  Producing that exchange
matching by counter-circulation paths is the exact next physical lemma.

There is a literal linkage form of that statement.  Let
\(\mathcal P=\{P_i\}\) be the constructed source linkage onto
\(A_\partial\).

### Lemma 7.4 (last-intersection counterflow)

In even rank, suppose there are a half-set \(I\subseteq[\delta]\), a
bijection

\[
                         \sigma:I\longrightarrow I^c,
\]

and directed paths \(R_i\) in \(D'\) such that

1. \(R_i\) starts at a vertex \(v_i\) of \(P_{\sigma(i)}\) and ends at
   \(b_i\);
2. after \(v_i\), \(R_i\) is disjoint from every path in
   \(\mathcal P\); and
3. the \(R_i\) are pairwise vertex-disjoint.

Then \(U_I\) is a surplus basis and the odd current is closed on the
labelled sector.

#### Proof

For \(j\in I\), retain the original path \(P_j\) to \(a_j\).  For
\(j=\sigma(i)\in I^c\), retain the prefix of \(P_j\) ending at \(v_i\)
and append \(R_i\), ending at \(b_i\).  The three hypotheses make all
resulting paths vertex-disjoint.  Their terminal set is exactly
\(\{a_i,b_i:i\in I\}=U_I\), so the strict-gammoid theorem makes \(U_I\)
a basis.  The boundary edges indexed by \(I\) then pair that basis, and
Corollary 6.2 makes their hubs distinct.  \(\square\)

In odd rank the identical argument applies with one retained socket path
\(P_k\) and a bijection

\[
                         \sigma:I\longrightarrow
 [\delta]\setminus(I\cup\{k\}).
\tag{7.12}
\]

For a boundary edge \(a_i b_i\), the natural candidate \(R_i\) is the
long-way nonwrap counter-circulation from one boundary endpoint to the
other.  The remaining positive theorem can therefore be phrased as an
even-cycle last-intersection packing for these counter-circulations.  It
must be proved relative to the literal zipper paths; arbitrary individual
reachability is not enough.

### Corollary 7.5 (exact permutation-parity obstruction)

Suppose a disjoint counterflow bank gives every \(i\) exactly one possible
last-intersection source \(\pi(i)\), and \(\pi\) is a permutation of
\([\delta]\).

* In even rank, a half-set satisfying Lemma 7.4 exists if and only if
  every cycle of \(\pi\) is even.
* In odd rank, a socket version (7.12) exists if and only if the cycle
  containing the socket is odd and every other cycle is even.

#### Proof

In even rank the required condition is

\[
                         \pi(I)=I^c.
\]

Along every cycle of \(\pi\), membership in \(I\) must alternate.  This is
possible exactly on even cycles, and then either alternating choice works
independently on each cycle.

In odd rank, leave the socket index in neither side.  Membership alternates
around every other cycle, so those cycles must be even.  On the socket
cycle there are two consecutive unselected indices across the socket;
the remaining memberships alternate consistently exactly when that cycle
is odd.  \(\square\)

If the socket may be chosen rather than prescribed, the odd-rank
criterion has the particularly sharp form

\[
 \boxed{\text{a socketed half-selection exists if and only if
              \(\pi\) has exactly one odd cycle.}}
\tag{7.13}
\]

Indeed, the socket must lie on every odd cycle, so necessity allows at
most one; the oddness of \(\delta\) guarantees at least one.  Conversely,
place the socket anywhere on the unique odd cycle and alternate membership
around the remaining vertices of that cycle and around every even cycle.
In particular a single Hamilton cycle on \(Q\) is sufficient, because
\(|Q|=\delta\) is odd.  This is only a criterion on a deterministic
counterflow permutation; it does not assert that such counterflows exist.

Thus a deterministic one-successor counterflow can still fail for a
purely integral reason.  In the actual central sector \(\delta\) is odd,
so the sharp deterministic target is **one** odd cycle carrying the
socket and only even cycles elsewhere.  Alternatively, enough additional
counterpaths may break and recombine the odd cycles.

## 8. Boundary occurrences and hub colours

Let a physical boundary occurrence join two majority states \(a,b\) in
clock slices.  Its unpointed hub is obtained by merging coordinates
\(2m,0\).  In the labelled sector it records

\[
 (\text{least active clock},\text{fixed quiet prefix},
   \text{active clock row and phase},
   \text{merged tail}).
\tag{8.1}
\]

### Proposition 8.1 (exact colour separation)

Two selected boundary occurrences have different hub colours whenever
their data in (8.1) differ.  Within one clock slice, distinct merged-tail
states give distinct hub colours.

#### Proof

Merging the two boundary coordinates changes no scan pair before the
boundary pair and changes no nonboundary clock coordinate.  Therefore the
first three entries of (8.1) can be read from the hub.  After they are
fixed, equality of hubs is exactly equality of the remaining merged-tail
state.  \(\square\)

For a quotient by an odd stabilizer \(H\), the identical statement holds
with equality replaced by equality of \(H\)-orbits.  Thus a linkage chosen
with pairwise \(H\)-inequivalent data (8.1) is automatically hub-rainbow.
This is the exact colour condition; pointed occurrences must not be
counted as distinct when their merged tails lie in one \(H\)-orbit.

## 9. Sharp obstruction to closing inside one clock slice

The minor in Theorem 2.1 deliberately allows only transfers disjoint from
the active clock and every earlier scan pair.  In every such connected
tail component, coordinate zero is fixed: its only nonwrap incident edge
is \(\{0,1\}\), and coordinate one lies in \(p_1\), which is either the
clock or belongs to the protected prefix.

Every physical boundary edge changes coordinate zero by one.

### Theorem 9.1 (one-slice boundary obstruction)

No connected clocked tail minor from Theorem 2.1 contains both endpoints
of a physical boundary edge.  Consequently no direct sum of independent
one-clock tail matchings proves the quiet-source paired-linkage theorem.

#### Proof

Coordinate zero is constant on a connected component of the restricted
tail graph and hence on its lifted minor.  The two endpoints of a boundary
edge have different values at coordinate zero.  They cannot both lie in
that component.  \(\square\)

This identifies the first missing operation exactly.  A positive proof
must either

1. hand the active clock across an earlier scan pair so that the edge
   \(\{0,1\}\) becomes usable;
2. pair terminal paths coming from two different clock slices with the
   required adjacent boundary values; or
3. realize the same coupling by a nonlocal protected Pfaffian minor.

Reachability inside one smaller tail graph is insufficient.

## 10. Stabilizer boundary

If a background has nontrivial odd stabilizer \(H\), a quotient-safe
clock choice cannot select one literal pair from a free \(H\)-orbit.  An
\(H\)-invariant set of clock pairs is a union of complete \(H\)-orbits.
Thus the literal one-clock theorem descends directly only after replacing
the clock by its complete orbit, or after pointing the quotient and later
removing the point.

The literal rewrite rules above are \(H\)-equivariant, so a complete orbit
of identical clock rows is the necessary candidate for an equivariant
multi-clock minor.  This observation alone does **not** prove that the
first-nonquiet matching descends to the required quotient matching: one
must still choose the phase-cube matching on the active orbit and prove
injectivity after orbit coalescence.  Terminal merged tails must in
addition be distinct \(H\)-orbits as required by Proposition 8.1.

This is a sharp symmetry constraint, not a scalar shortage.  It explains
why a labelled private-clock proof cannot simply be quoted in a periodic
necklace sector.

## 11. Consequence for the odd current programme

The contracted digraph \(D'\) is not an opaque black box around its quiet
sources.  Every central source has a two-arc entrance into an explicit
noncanonical nearest-neighbour token minor, and the entire binary quiet
core has such entrances as well.  Distinct hub colours are transparent in
the terminal signature (8.1).

The remaining labelled theorem is now the following narrower statement.

> **Hub-distinct one-socket paired-basis theorem.**  From the boundary
> edges incident with \(A_\partial\), choose \((|Q|-1)/2\) edges and one
> allowed socket endpoint such that their union is a basis of \(S/V(P)\).

Corollary 6.2 makes every such choice automatically hub-rainbow.  The
paired-basis theorem therefore makes the contracted coloured Pfaffian
nonzero by the first-scan coefficient identity.  Theorem 9.1 proves that
the second endpoints cannot be obtained inside independent fixed-clock
components.

Proved here:

1. an exact noncanonical strict-gammoid minor at every active clock;
2. a two-arc entrance for every central quiet source;
3. complete absorption of the zero/ two binary quiet core;
4. a vertex-disjoint zipper from every source to one explicit
   noncanonical surplus basis;
5. an exact readable hub-colour signature; and
6. a sharp obstruction to an independent one-component completion.

Not proved here:

1. the hub-distinct paired-basis selection;
2. a hub-rainbow terminal matching in every stabilizer quotient;
3. compatibility with the complementary nonwrap fan/receiver bank; or
4. the all-dimensional upper bound.
