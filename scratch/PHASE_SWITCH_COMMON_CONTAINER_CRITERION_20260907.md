# Phase switches: exact common-container criterion

Date: 2026-09-07.  This note concerns local coalescence of centered-square
pairs.  It does not rule out arbitrary global target trades and does not prove
the full-cube coefficient-one conjecture.

Throughout assume `b>=3`, and put `Omega=[2b]`.  An oriented Johnson geodesic

\[
 P=(S_0,S_1,\ldots,S_{p-1})
\]

determines the centered-square pair `Q(P)` described in
`CENTRAL_TRACE_LOCAL_TRADES_20260907.md`.  Its middle support is the two
antipodal paths `P` and `P^c`, and its complete support includes all unions
and intersections of vertices of either path.

## 1. Geodesicity is consistency of the accumulated directions

Consider a Johnson walk of `L` edges.  On edge `i`, delete `d_i` and insert
`a_i`.  The following are equivalent:

1. the walk is a geodesic;
2. the sets `D={d_1,...,d_L}` and `I={a_1,...,a_L}` have size `L` and are
   disjoint;
3. there is a balanced split `Omega=P dotcup Q`, `|P|=|Q|=b`, for which
   every edge deletes from `P` and inserts into `Q`.

For (1) implies (2), endpoint distance `L` means that none of the `L`
changes is subsequently cancelled.  Conversely, (2) makes the endpoint
distance `L`.  Given (2), put `D subset P`, `I subset Q` and distribute the
remaining coordinates to make both shores have size `b`; this proves (3).
The implication (3) implies (2) is immediate.  In fact, when `L<=b`, the
number of balanced phases orienting the whole walk is exactly

\[
                 \boxed{{2b-2L\choose b-L}}.          \tag{1}
\]

Indeed, after forcing `D subset P` and `I subset Q`, choose the remaining
`b-L` coordinates of `P` from the `2b-2L` unused coordinates.

Thus a geodesic assembled from several nominal phases always admits one
common phase retrospectively.  Phase switching enlarges the mergeable class
only syntactically, not geometrically.

For two geodesics meeting at one endpoint,

\[
 P=(A= S_0,\ldots,S_{p-1}=V),\qquad
 R=(V=U_0,\ldots,U_{q-1}=B),
\]

put

\[
 D_P=A\setminus V,\quad I_P=V\setminus A,\qquad
 D_R=V\setminus B,\quad I_R=B\setminus V.
\]

Then

\[
 d_J(A,B)=p+q-2-|D_P\cap I_R|-|I_P\cap D_R|.        \tag{2}
\]

Consequently the glued walk is geodesic exactly when

\[
              \boxed{D_P\cap I_R=I_P\cap D_R=\varnothing.} \tag{3}
\]

The two intersections in (3) are precisely the two possible kinds of
cross-switch cancellation: reinserting a coordinate deleted before the
switch, or deleting one inserted before the switch.

A stronger phase-level condition is useful when the continuation has not
yet been chosen.  If the first path has accumulated history `(D_P,I_P)`,
then every forward continuation in a new phase `P' dotcup Q'` is compatible
with that history provided

\[
                         D_P\subseteq P',\qquad I_P\subseteq Q'. \tag{4}
\]

There are exactly `binom(2b-2(p-1),b-(p-1))` such balanced phases.  The
phase may therefore change freely on unused coordinates.  Condition (4)
also shows what information a dynamic construction would have to retain:
the accumulated deleted/inserted shores, not merely a phase name or two
local slots.

The same statements hold when the paths have an identical terminal/initial
overlap: delete the duplicate copy of the shared segment and apply (1)--(3)
to the resulting union walk.  Individual geodesicity already rules out all
cancellations except those between the two nonshared outer portions.

## 2. Designated square-family containment is rigid

**Embedded-trace lemma.**  Let `P` and `Z` be centered geodesics.  If

\[
                            Q(P)\subseteq Q(Z),       \tag{5}
\]

then, after possibly complementing and reversing `P`, its middle trace is a
contiguous subpath of the middle trace of `Z`.

Proof.  Write `F,G` for the two nonempty fixed caps of `Q(Z)`.  Every target
of `Q(Z)` either contains `F` and avoids `G`, or contains `G` and avoids
`F`.  Every middle vertex of `P` lies on one of the two complementary middle
branches of `Q(Z)`.

Two consecutive vertices of `P` cannot lie on opposite branches.  If they
did, their intersection would avoid both `F` and `G`; but that intersection
belongs to `Q(P)` and hence, by (5), would have to belong to `Q(Z)`, contrary
to the cap dichotomy.  (Their union, which contains both caps, gives the
same contradiction.)  Thus all vertices of `P` lie on one branch.  A
centered trace is an induced geodesic path:
`d_J(Z_i,Z_j)=|i-j|`.  Consecutive vertices of `P` therefore occupy
consecutive indices, and geodesicity prevents reversal of index direction
inside the path.  Hence the indices form one contiguous interval. `square`

The argument includes containment in the **designated** family of a maximal
side-`b` square.  Although its two complementary middle branches have
Johnson edges between their extreme vertices, a side-two square crossing
such a seam has an intersection containing neither cap and a union containing
both; those targets are not in the designated family `Q(Z)`.

This distinction matters: the literal side-`b` source word consists of
singletons, and its unintended cyclic intervals do contain these seam
targets.  Section 4 gives the exact resulting exception for word-level,
rather than designated-family, containment.

## 3. Exact common-container theorem

Let two oriented geodesics have an identical terminal/initial overlap of
`r>=1` vertices, no other common folded middle vertex, and let their glued
union walk have

\[
                            ell=p+q-r
\]

vertices.  Then the following are equivalent:

1. there is a centered-square pair whose complete target support contains
   both old complete supports;
2. the glued union walk is a geodesic and `ell<=b`;
3. after deleting the repeated overlap, the accumulated deletion and
   insertion sets are disjoint and have size `ell-1`.

If these conditions hold, the union walk itself supplies the containing
side-`ell` square.  The diagonal-block lemma puts both old squares inside
it.  Conversely, apply the embedded-trace lemma to both old squares.  Their
common overlap puts them on the same branch of the proposed container; the
assumption on their common vertices then forces their union to be one
contiguous subpath of that branch.  It is therefore geodesic and has at most
`b` vertices. `square`

For a one-vertex switch, condition (3) is the explicit test in item 3.
Thus a direction label may change at the junction and the usual zero-charge
all-depth square-family merge still works, but only if the change has not
caused a coordinate cancellation.  If it has, no alternate ordering inside
one larger **designated centered-square family** can preserve both old
supports.  A maximal singleton cycle supplies the separate word-level
possibility in Section 4.

There is a corresponding monotone-replacement obstruction.  Suppose every
old square must be assigned to a new centered square which contains its
complete support.  At a nongeodesic switch the two old squares cannot be
assigned to the same new square.  The embedded-trace lemma also says that a
container of a side-`p` square has side at least `p`.  Hence any such
replacement still needs at least two components and principal charge at
least

\[
                              2p+2q.                 \tag{6}
\]

It cannot save either the overlap charge or one independent compiler
overhead payment.  Keeping and compiling the two old squares separately is
therefore optimal within this designated-containment-certified local model.

## 4. Exact maximal-cycle exception

Let

\[
 C=(c_0,c_1,\ldots,c_{2b-1})
\]

be a cyclic permutation of `Omega`, regarded as a singleton OR word.  Its
rank-`b` interval unions are the `2b` cyclic windows

\[
                    Z_i=\{c_i,c_{i+1},\ldots,c_{i+b-1}\}. \tag{7}
\]

They form a `2b`-cycle in the Johnson graph.  Every arc of at most `b`
vertices in this cycle is a geodesic.  More strongly, if `P` is such an arc,
then every target of `Q(P)` is a cyclic interval union of `C`: for `i<=j`,
`Z_i cap Z_j` is their overlap interval, `Z_i union Z_j` is their span
interval, and their complements are the opposite cyclic intervals.

Conversely, if every target of a centered-square pair `Q(P)` is a cyclic
interval union of `C`, then its middle vertices are rank-`b` windows (7).
Two such windows are Johnson adjacent exactly when their starts are adjacent
on the `2b`-cycle.  Geodesicity therefore makes `P` a contiguous arc of at
most `b` vertices.  We obtain:

**Maximal-cycle containment lemma.**  The literal maximal singleton cycle
`C` realizes the complete support of `Q(P)` if and only if, after possibly
complementing and reversing `P`, its trace is an arc of the central window
cycle (7).

This is the only extra case for a literal cyclic square-source container.
For a source square of side `m<b`, rank `b` lies in its exact purity range,
and its two middle branches have no cross-edge.  Hence any contained old
trace lies contiguously in one branch, reducing to the designated-family
criterion of Sections 2--3.  At `m=b` the two seam edges close those branches
into the central cycle (7), and the preceding lemma is exact.

This gives a genuine way to preserve two old all-depth square supports even
when their glued trace is not geodesic.  If both traces are arcs of one
central window cycle, the one singleton cycle realizes both.  Their union
arc may have more than `b` vertices and hence fail to define a legal
centered square; once it has more than `b+1` vertices, it is not even a
Johnson geodesic.  Each old trace separately still has at most `b` vertices.

There is an exact test for this exception.  Let

\[
 W_0,W_1,\ldots,W_L
\]

be the glued Johnson walk, where edge `i` deletes `d_i` and inserts `a_i`.
On the residue set `Z_(2b)`, make the partial assignments

\[
                         c_i=d_i,\qquad c_{i+b}=a_i
                         \quad(0\le i<L).             \tag{8}
\]

After making any allowed complement/reversal choices which align the shared
trace, the walk is an arc of a central window cycle if and only if:

1. assignments to the same residue in (8) agree;
2. different residues receive different coordinates;
3. an assigned residue lies in `[0,b-1]` exactly when its coordinate lies
   in `W_0`.

Necessity follows from shifting (7): at step `i` the leaving coordinate is
`c_i` and the entering coordinate is `c_(i+b)`.  For sufficiency, extend the
partial injection on the first `b` residues by the unused coordinates of
`W_0`, and extend the other half by the unused coordinates of its complement.
The resulting cyclic permutation starts at `W_0`, and (8) inductively gives
every subsequent `W_i`.

When `L<b`, the two residue intervals in (8) are disjoint, and this test
reduces to ordinary geodesicity.  When `L>=b`, consistency forces the rigid
FIFO cancellations

\[
 d_{i+b}=a_i\quad(0\le i<L-b),\qquad
 a_{i+b}=d_i\quad(0\le i<L-b).                       \tag{9}
\]

Thus an incompatible phase switch has only one single-block escape inside
the present bridge architecture: it must continue as part of a common
maximal cyclic coordinate order, with cancellations occurring exactly after
`b` shifts.  Arbitrary cancellations are not absorbed.

The escape necessarily spends folded-middle overlap.  Suppose the two arc
traces have `p,q` vertices, share exactly `r` actual consecutive windows,
and their union arc has `n=p+q-r` vertices.  Projection of window starts
modulo `b` is precisely antipodal folding, so their number of common folded
middle targets is

\[
 |P_{\rm fold}\cap R_{\rm fold}|
 =p+q-\min(n,b)
 =r+\max(0,n-b).                                    \tag{10}
\]

Thus every maximal-cycle absorption with `n>b` creates `n-b` additional
folded overlaps beyond the displayed actual overlap.  In particular, under
the central-simple hypothesis that the two traces have no other common
folded target, the maximal-cycle exception disappears and necessarily
`n<=b`; word-level containment then again reduces to ordinary geodesic
coalescence.  It also gives no pairwise escape for sublinear arms
`p+q=o(b)`, the scale relevant to a direct Gaussian-depth block strategy.

The cyclic block costs `2b` letters and preserves all ranks cyclically.  It
can be linearized once with the general cyclic-linearization lemma if a
linear all-depth block is required.  For a band `[b-H,b+H]`, with
`H<min(p,q)`, applying the derivative compiler directly to `C` costs
`2b+2H` and preserves the band targets of every contained arc-square.  Hence
two long arms with
`2b+2H<2p+2q+4H` can be cheaper in one maximal cyclic block even though
their full glued trace is nongeodesic.

There is a concise central-simple reformulation.  Let a connected
maximum-degree-two graph of folded middle targets carry the side-two squares
of its edges, and suppose one canonical cyclic square-source block realizes
all those edge-square supports.  If the source side is `<b`, its folded
middle graph is a path, so the selected component is a geodesic subpath.  If
the source side is `b`, its folded middle graph is the `b`-cycle obtained by
folding (7).  A selected path in that cycle again has a geodesic lift; the
only nongeodesic connected central-simple possibility is the entire folded
`b`-cycle.

Hence, inside one canonical bridge block, a phase-switch component has the
exact dichotomy

\[
 \boxed{\text{one geodesic path}\quad\text{or}\quad
        \text{one complete maximal tight cycle}.}    \tag{11}
\]

The second alternative is the familiar cyclic-singleton/tight-middle-deck
architecture, not a new all-rank covering theorem.  It shows precisely what
a successful nongeodesic phase closure would have to build; selecting enough
such cycles with Gaussian-band coverage remains the global problem.

## 5. Scope

The theorem closes the direct local escape from the phase barrier:

* a compatible phase switch is merely a relabelling of unused coordinates
  and is already one common-phase geodesic;
* an incompatible switch cannot be absorbed by a larger designated
  centered-square family;
* it can nevertheless be compiled through unintended intervals of one
  maximal singleton cycle exactly under the cyclic-lag test (8).

This does **not** exclude a global trade in which targets of several old
squares are redistributed among several new squares without any old square
being individually contained in a new one.  Such a trade would need a new
all-depth coverage proof; adjacent-edge or central-multiset preservation
alone is insufficient by the local-trade ledger.
