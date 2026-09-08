# Lane W: the in-place QCF crossing-border compiler

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Exact verdict

Put

\[
 N=2m+1,\qquad B=\operatorname {Cat}_m,\qquad W=NB,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed.  Let a long quotient cycle be partitioned into
blocks of quotient length

\[
 H\ll b\le \ell<2b,
 \qquad b\log N=o(m).
 \tag{0.1}
\]

All asymptotic statements below are for fixed \(A\) and sufficiently
large \(m\), so every displayed rank-versus-\(H\) condition is in force.

This report separates the literal block-border problem from the internal
chronological-recoding problem.  The separation is exact.

1. **The two outer borders are not the missing gate.**  At one physical
   Johnson cut, all floor-correct lower crossing intersections and all
   upper crossing unions through depth \(H\) have a standalone nonzero
   chart of exact length

   \[
      \boxed{4H-1}.                                      \tag{0.2}
   \]

   Thus both boundaries of an all-\(N\)-phase block cost less than
   \(8NH\).  In a cyclic block partition, every boundary is shared by
   two blocks, so the global charge is only \(N(4H-1)\) per block.  This
   proves the desired \(O(NH)\) crossing-border toll without any port
   matching or primitive-invariance assumption.

2. **Long correlated atoms do have an in-place compiler.**  If every
   internally bounded positive coordinate run in a chronological owner row
   has length at least \(H+1\), endpoint-capped \(H\)-erosion replaces a
   row of \(v\) owners by at most \(v+H\) nonzero letters and represents
   every internal lower intersection and upper union through depth \(H\),
   with literal upper prefix and suffix arms.  For a fixed-core rainbow
   row this hypothesis is automatic.  If the chronological phase-successor
   permutation has \(c\) cycles, its complete phase deck has exact length

   \[
      \boxed{Nv+N(3H-1)+2Hc\le Nv+N(5H-1)}.       \tag{0.3}
   \]

   It covers the packet interiors, every floor-correct crossing lower
   window, and every crossing upper window at all \(N\) chronological
   seams.  If both fixed-core parity rows of a packet with \(H\le s\)
   separately have the actual physical successor permutations required in
   Theorem 2.3, the
   exact bound is

   \[
      \boxed{
      N(2s+2)+N(6H-2)+2H(c_0+c_1)
      \le N(2s+2)+N(10H-2).}                     \tag{0.4}
   \]

   Consequently a block split into \(k\) such correlated atoms has
   relative excess \(O(kH/\ell)\).  This proves QCF for this nontrivial
   class whenever \(kH=o(\ell)\).

3. **Literal chronological cells are rigorously impossible.**  Suppose
   the original owners remain in pairwise disjoint ordered witness cells.
   If the cells have total internal excess \(E\), the outside gaps have
   total length \(G\), and the word represents \(M\) distinct targets at
   one proper lower rank, then

   \[
      \boxed{M\le G+2E.}                          \tag{0.5}
   \]

   Hence a word with \(n\) owner cells has length at least

   \[
      \boxed{n+\lceil M/2\rceil}.                 \tag{0.6}
   \]

   If the owners are retained as literal one-letter cells, the sharper
   bound is \(n+M\).  Applied globally to the middle owners and the full
   rank-\((m-1)\) layer, (0.6) gives

   \[
      L\ge
      W+\left\lceil {1\over2}{N\choose m-1}\right\rceil
      =\left({3\over2}-{1\over m+2}\right)W+O(1). \tag{0.7}
   \]

   Thus the strict cellwise meaning of “keep chronological order” cannot
   prove coefficient one.  A valid braid must replace almost all owner
   letters and use overlapping or nonlocal owner witnesses.  On one
   rainbow height-\(s\) packet, (0.6) gives the exact lower bound
   \(3s+2\), matching the known linear two-core chart.  The circular
   baseline-plus-one chart escapes precisely by abandoning ordered owner
   cells.

4. **There is no generic endpoint, phase, or pin obstruction to QCF.**
   An explicit rotational all-phase Johnson deck, locally liftable to the
   odd graph and reindexable with the exact unit rotor \(u\mapsto u-1\),
   has maximal distinct signed support in the full radius-\(H\) collar and
   a literal word of exact length

   \[
      \boxed{N\ell+4NH}.                          \tag{0.8}
   \]

   It also contains compatible pin bundles of size \(H\).  Therefore no
   lower bound using only rank, endpoint injection, Johnson chronology,
   all \(N\) rotations, unit voltage, or compatible-pin necessity can
   force \(\Omega(N\ell)\) excess.  A negative theorem must use the
   actual PBBS quotient-template dynamics or exact-factor extendibility.

The full PBBS QCF is **not proved**.  What is proved is sharper than the
former formulation of its gate: outer block borders already cost
\(O(NH)\), and long fixed-core atoms already compile.  The sole remaining
problem is the wholesale internal replacement of the depth-one core spine
through a long block containing many changing cores or short positive
runs.  No coefficient-one conclusion is claimed here.

## 1. One physical border has an exact \(4H-1\) chart

Let

\[
 X_{i+1}=X_i-\{r_i\}+\{a_i\}
 \tag{1.1}
\]

be a rank-\((r+1)\) Johnson trajectory, cut between \(X_{-1}\) and
\(X_0\), and assume

\[
 2H\le r+1.                                       \tag{1.2}
\]

For \(1\le s,t\le H\), put

\[
 P_{s,t}=\bigcap_{i=-s}^{t-1}X_i.                \tag{1.3}
\]

It is floor-correct when

\[
 |P_{s,t}|=r+2-s-t.                               \tag{1.4}
\]

Every required lower window crossing the cut and using at most \(H+1\)
owners has \(s+t-1\le H\).

Put \(C=X_{-1}\cap X_0\).  For \(x\in C\), let \(u_x,v_x\in[H]\)
be its capped left and right positive-run extents through the cut.  Then

\[
 P_{s,t}=\{x\in C:u_x\ge s,\ v_x\ge t\}.         \tag{1.5}
\]

### Lemma 1.1 -- southwest exclusion

If \(P_{s,t}\) is floor-correct, no extent point \((u_x,v_x)\) is
strictly southwest of \((s,t)\).

#### Proof

The window in (1.3) has \(s+t\) owners and \(s+t-1\) transitions.
Map every coordinate of the first owner which is absent from the total
intersection to its first departure transition.  This map is injective.
If \(u_x<s\) and \(v_x<t\), then \(x\) arrives internally and later
departs internally.  Its later departure is not the first departure of an
initial coordinate: either \(x\) was not initial, or it had already
departed before its internal arrival.  Hence at most \(s+t-2\) transitions
are used by the injection, and

\[
 |P_{s,t}|\ge(r+1)-(s+t-2)=r+3-s-t,
\]

contrary to (1.4). \(\square\)

Discard multiplicities from the extent points and sort their Pareto-minimal
points by increasing first coordinate.  Join the initial endpoint, each
successive minimum, and the terminal endpoint by moving horizontally east
first and then vertically south.  This gives a unit path \(\Gamma\) from
\((1,H)\) to \((H,1)\) through all the minima.  It has exactly \(2H-1\)
vertices.  At a
vertex \(z=(a,b)\), emit the actual set-letter \(W_z=P_{a,b}\).

### Lemma 1.2 -- lower dominance staircase

For every floor-correct \(P_{s,t}\),

\[
 P_{s,t}
 =\bigcup_{\substack{z\in V(\Gamma)\\z\ge(s,t)}}W_z,     \tag{1.6}
\]

and the selected vertices form one contiguous subpath.  Every \(W_z\) is
nonempty.

#### Proof

The two coordinate inequalities in (1.6) select a suffix and a prefix of
the southeast path, hence a contiguous subpath.  Every selected \(W_z\)
is contained in \(P_{s,t}\) by (1.5).

Conversely, take \(x\in P_{s,t}\), so
\((u_x,v_x)\ge(s,t)\).  Descend below this extent point to a Pareto
minimum.  If that minimum lies northeast of the query, it itself works.
If it lies west and north, follow \(\Gamma\) forward to first coordinate
\(s\); the east-before-south rule and Lemma 1.1 keep the second coordinate
at least \(t\).  The east-and-south case is the reverse argument.  Thus
some \(z\in[(s,t),(u_x,v_x)]\) lies on \(\Gamma\), and (1.5) puts
\(x\in W_z\).

Finally, \(W_z\) is an intersection of at most \(2H\) consecutive
rank-\((r+1)\) owners.  At most one initial coordinate is lost at each
transition, so

\[
 |W_z|\ge r+2-2H\ge1
\]

by (1.2). \(\square\)

The upper crossing targets need no new geometry: the literal word

\[
 X_{-H},X_{-H+1},\ldots,X_{H-1}                  \tag{1.7}
\]

has length \(2H\) and contains each crossing upper window as its original
contiguous owner subword.  Concatenating (1.6) and (1.7) proves:

### Theorem 1.3 -- exact one-border compiler

Every floor-correct lower intersection and every upper union through depth
\(H\) crossing one physical Johnson cut has a nonzero literal chart of
exact length

\[
 \boxed{(2H-1)+2H=4H-1.}                         \tag{1.8}
\]

No return, phase, or endpoint-order hypothesis is used.

### Corollary 1.4 -- all-phase block borders

Suppose an all-phase quotient block has an internal literal compiler of
length

\[
 N\ell+\eta_mN\ell+C_0NH                         \tag{1.9}
\]

covering every required window wholly inside the block.  Appending the
chart of Theorem 1.3 at every lift of both outer boundaries gives a
standalone block compiler of length less than

\[
 N\ell+\eta_mN\ell+(C_0+8)NH.                    \tag{1.10}
\]

In a cyclic partition, charge each shared boundary only once.  The global
boundary charge is then exactly \(N(4H-1)\) per quotient block, and the
constant \(C_0+8\) in (1.10) becomes \(C_0+4\) after summation.

The copied owner collars in (1.7) are charged helper positions.  They do
not claim ownership of another block's baseline slots.  The statement is
literal target preservation through depth \(H\); it does not preserve
arbitrary owner intervals longer than \(H+1\).

## 2. Endpoint-capped erosion for long correlated atoms

The previous section removes the two external borders.  This section
gives a full internal compiler under an exact run-length condition.

Let \(X_0,\ldots,X_{v-1}\) be nonempty set-letters.  Extend them
constantly to all integer indices:

\[
 \widetilde X_i=X_0\quad(i<0),
 \qquad
 \widetilde X_i=X_{v-1}\quad(i\ge v).             \tag{2.1}
\]

Assume that every finite maximal positive run of every coordinate in
\((\widetilde X_i)_{i\in\mathbb Z}\) has length at least \(H+1\).
Define

\[
 D_i=\bigcap_{h=0}^{H}\widetilde X_{i+h},
 \qquad -H\le i<v.                                \tag{2.2}
\]

Delete the empty \(D_i\)'s and retain the index order.

### Theorem 2.1 -- exact long-run erosion identities

For every \(0\le a\le b<v\) with \(b-a\le H\),

\[
 \boxed{
 \bigcap_{j=a}^{b}X_j
   =\bigcup_{i=b-H}^{a}D_i,}                      \tag{2.3}
\]

and, for every \(0\le a\le b<v\) without a depth restriction,

\[
 \boxed{
 \bigcup_{j=a}^{b}X_j
   =\bigcup_{i=a-H}^{b}D_i.}                      \tag{2.4}
\]

The displayed \(D\)-ranges remain contiguous after empty letters are
deleted.  Hence the word

\[
 \mathcal E=(D_{-H},D_{-H+1},\ldots,D_{v-1})     \tag{2.5}
\]

has length at most \(v+H\), represents every internal lower window through
depth \(H\) whose target is nonempty, represents **every** internal upper
owner interval, and
represents every upper prefix and suffix by a literal prefix and suffix of
\(\mathcal E\).

#### Proof

Fix a coordinate \(x\) and one of its positive runs \(R=[p,q]\), allowing
one infinite endpoint or the doubly infinite run \(R=\mathbb Z\).  One
has \(x\in D_i\) exactly when
\([i,i+H]\subseteq R\).

The coordinate belongs to the left side of (2.3) exactly when
\([a,b]\subseteq R\).  Since \(b-a\le H\) and every finite run has length
at least \(H+1\), some length-\((H+1)\) interval contained in \(R\)
also contains \([a,b]\).  Its initial index lies in \([b-H,a]\), proving
(2.3) coordinatewise.  Conversely every \([i,i+H]\) with
\(b-H\le i\le a\) contains \([a,b]\), so no extra coordinate is added.

The coordinate belongs to the left side of (2.4) exactly when its positive
run meets \([a,b]\).  A run of length at least \(H+1\) which meets
\([a,b]\) contains an \((H+1)\)-interval whose initial index lies in
\([a-H,b]\), irrespective of the length of \([a,b]\).  The converse is
immediate, proving (2.4) for every owner interval.

For \(a=0\), the range in (2.4) begins at \(-H\), so upper prefixes are
prefixes of (2.5).  For \(b=v-1\), it ends at \(v-1\), so upper suffixes
are suffixes.  Deleting empty entries preserves every convex index range.
\(\square\)

The run hypothesis is sharp for this erosion architecture.  If a
coordinate has a finite positive run of length at most \(H\), it occurs in
no \(D_i\), while it occurs in every owner indexed inside that run.  Thus
even the singleton-owner case of (2.4) fails for the \(D\)-word.  Repairing
these short internal runs is exactly the part not handled by erosion.

### Corollary 2.2 -- fixed-core rows

Let \(\Gamma=(\gamma_0,\ldots,\gamma_{2s})\) have pairwise distinct
coordinates, let \(C\cap\Gamma=\varnothing\), and put

\[
 X_j=C\cup\{\gamma_j,\gamma_{j+1},\ldots,\gamma_{j+s-1}\},
 \qquad 0\le j\le s.                              \tag{2.6}
\]

If \(H\le s\), the hypothesis of Theorem 2.1 holds.  Every active
positive run touches at least one endpoint of the displayed row, while
the core coordinates persist forever under (2.1).  If the owners have
rank \(r+1\), so \(|C|=r+1-s\), then

\[
 |D_i|\ge r+1-H\ge1,                              \tag{2.7}
\]

so no erosion letter is deleted and \(|\mathcal E|=s+1+H\).

### Theorem 2.3 -- chronological all-phase fixed-core braid

Assume in addition that (2.6) is one actual physical fixed-core return row
in one fixed exact factor, that all \(N\) phase lifts are used, and that
their chronological successor map at the return is a permutation
\(\sigma\) of \(\mathbb Z_N\).  Let \(c\) be the number of cycles of
\(\sigma\), and assume \(2H\le r+1\).

There is a direct nonzero literal word, respecting the chronological
\(\sigma\)-cycles, which represents every internal lower window through
depth \(H\), every floor-correct crossing lower window through depth
\(H\), every crossing upper window through depth \(H\), and every
internal upper owner interval of arbitrary length.  Its exact length is

\[
 \boxed{N(s+1)+N(3H-1)+2Hc.}                     \tag{2.8}
\]

#### Proof

For each phase \(u\), form the erosion word \(\mathcal E_u\) of length
\(s+1+H\).  Concatenate these words along the cycles of \(\sigma\).  By
Theorem 2.1, every internal target is represented.

At a nonclosing chronological seam
\(\mathcal E_u\mathcal E_{\sigma(u)}\), an upper crossing union is the
OR of a suffix of \(\mathcal E_u\) and a prefix of
\(\mathcal E_{\sigma(u)}\), by the prefix/suffix clause of Theorem 2.1.
Thus it is already a contiguous OR.  The same suffix--whole-block--prefix
argument preserves every upper interval along a linearized
\(\sigma\)-cycle which does not cross its chosen linear cut.  Append the
\((2H-1)\)-letter lower
staircase of Theorem 1.3 for each of the \(N\) seams.  These charts may be
banked in an appendix; each lower target has a witness wholly inside its
own chart.

Linearizing each of the \(c\) cycles destroys its closing upper seam.
Append the original \(2H\)-owner collar for each such closure.  Every
closing upper target is a contiguous subword of that collar.  The length
is therefore

\[
 N(s+1+H)+N(2H-1)+2Hc,
\]

which is (2.8).  Every helper letter is an actual intersection or owner
set, and (1.2) and (2.7) make it nonzero. \(\square\)

For the exact unit rotor \(\sigma(u)=u-1\), one has \(c=1\), since
translation by one is a single cycle on \(\mathbb Z_N\).

If the two fixed-core parity rows of a height-\(s\) rainbow packet with
\(H\le s\) are actual physical return rows in one fixed factor and each
has its chronological successor permutation on the complete phase deck,
applying Theorem 2.3 to them gives (0.4).  No assertion is made for a
formal fixed-core chart without these physical successor maps.

### Corollary 2.4 -- a quantitative long-atom QCF class

Suppose each of the \(N\) physical chronological lifts of a long block is
partitioned at the same \(k-1\) quotient indices into \(k\) disjoint row
segments satisfying Theorem 2.1 (in particular, fixed-core segments from
Corollary 2.2), and the raw owner counts sum to \(N\ell\).  Assume every
inter-segment and outer cut is an actual rank-\((r+1)\) Johnson edge and
\(2H\le r+1\).  The erosion
words have total length at most \(N\ell+kNH\).  Apply Theorem 1.3 at the
\(k-1\) inter-segment borders and the two outer block borders in every
phase.  The certified length is

\[
\begin{aligned}
 L
 &\le N\ell+kNH+(k+1)N(4H-1)\\
 &=N\ell+N\bigl((5k+4)H-k-1\bigr).
\end{aligned}                                    \tag{2.9}
\]

Consequently, if \(kH=o(\ell)\), then

\[
 L=N\ell+o(N\ell)+O(NH),                          \tag{2.10}
\]

which is QCF at coefficient one for this class.  The estimate deliberately
does not assert that arbitrary PBBS long blocks admit such a decomposition.
For Gaussian atoms of length only \(\Theta(H)\), the atomwise charge in
(2.9) can be \(\Theta(N\ell)\); their internal seams still require a new
fusion.

## 3. Exact obstruction to chronological owner cells

The positive theorem above replaces the baseline by erosion letters.  The
replacement is necessary.

### Lemma 3.1 -- literal-owner augmentation bound

Suppose a word retains \(R\) distinct rank-\(r\) owners as literal
set-letters and represents \(M\) distinct targets of one rank \(d<r\).
Then

\[
 \boxed{L\ge R+M.}                                \tag{3.1}
\]

#### Proof

A witness for a rank-\(d\) target cannot contain a retained rank-\(r\)
letter, because its OR would then have rank at least \(r\).  Hence every
proper-rank witness lies wholly among the other \(L-R\) positions.  Two
distinct targets of the same rank cannot have witnesses with the same left
endpoint: such intervals are nested, their ORs are comparable, and two
equal-rank comparable sets are equal.  Thus the \(M\) witnesses need
\(M\) distinct nonowner left endpoints. \(\square\)

On a physical step-two PBBS row, if \(X_j\) is a rank-\((m+1)\)
complement-projected owner and \(C_j\) is the intervening rank-\(m\)
middle owner, exact odd-graph adjacency gives

\[
 X_j=C_{j-1}\cup C_j.                             \tag{3.2}
\]

Thus the chronological core spine \((C_j)\) already represents every
owner and every upper owner interval.  Conversely, retaining all
rank-\((m+1)\) owners literally while adding their distinct depth-one
cores invokes Lemma 3.1 and doubles the block scale.  The correct baseline
is a replacement spine, not an augmentation of raw owners.

The following stronger theorem allows each owner to occupy a longer but
still ordered cell.

### Theorem 3.2 -- chronological proper-rank endpoint-slot theorem

Let \(Y=(Y_1,\ldots,Y_L)\) be a word of nonempty set-letters.  Let
\(A_1,\ldots,A_n\) be rank-\(r\) sets with pairwise disjoint ordered
witness cells

\[
 I_i=[a_i,b_i],\qquad b_i<a_{i+1},\qquad
 \bigcup_{j\in I_i}Y_j=A_i.                      \tag{3.3}
\]

Put

\[
 E=\sum_{i=1}^{n}(|I_i|-1),
 \qquad
 G=L-\sum_{i=1}^{n}|I_i|.                        \tag{3.4}
\]

If \(M\) distinct rank-\(d\) sets with \(d<r\) are represented anywhere
in \(Y\), then

\[
 \boxed{M\le G+2E.}                              \tag{3.5}
\]

Consequently

\[
 \boxed{L=n+E+G\ge n+\lceil M/2\rceil.}          \tag{3.6}
\]

The same statement holds for cyclically ordered disjoint cells in a
circular word, where every witness is a proper forward-oriented cyclic
interval.

#### Proof

Choose one witness \(J_T\) for every proper-rank target \(T\).  It cannot
contain a whole cell \(I_i\), since then \(T\) would contain \(A_i\) and
would have rank at least \(r\).

If \(J_T\) avoids all cells, assign it to its right endpoint in the outside
gaps.  There are \(G\) such slots.  Otherwise let \(I_i\) be the first
cell met by \(J_T\).  If the left endpoint of \(J_T\) lies strictly after
\(a_i\), assign the oriented left slot to that endpoint; the available
left slots in \(I_i\) are \(a_i+1,\ldots,b_i\).  If the left endpoint is
at or before \(a_i\), the witness cannot contain \(I_i\), so its right
endpoint lies in \(a_i,\ldots,b_i-1\); assign that oriented right slot.
The total number of oriented cell slots is \(2E\).

Two distinct equal-rank targets cannot receive the same oriented slot.
Intervals with one fixed left endpoint form a nested chain as the right
endpoint moves, and intervals with one fixed right endpoint form a nested
chain as the left endpoint moves.  Their ORs are comparable, so equality
of ranks forces equality of sets.  This proves the injection (3.5).
Since \(G+2E\le2(E+G)=2(L-n)\), (3.6) follows.

On a circle, a proper-rank witness cannot be the full circle, since it
would contain a whole rank-\(r\) cell.  Start from its oriented left
endpoint and take the first cell it meets; the identical slot assignment
is cyclic.  Fixed oriented endpoints again give nested proper forward
intervals, so the same injection applies. \(\square\)

### Corollary 3.3 -- the cellwise coefficient-one architecture is false

For \(N=2m+1\), there are

\[
 W={N\choose m}
\]

middle owners and

\[
 {N\choose m-1}={m\over m+2}W                    \tag{3.7}
\]

required rank-\((m-1)\) targets.  If a universal word keeps the owners in
ordered disjoint cells, Theorem 3.2 gives (0.7).  If it retains them as
literal letters, Lemma 3.1 gives

\[
 L\ge W+{N\choose m-1}
   =\left(2-{2\over m+2}\right)W.                \tag{3.8}
\]

Blockwise, \(n=N\ell\) ordered owner cells and a budget

\[
 L\le N\ell+\eta_mN\ell+C_ANH                    \tag{3.9}
\]

can represent at most

\[
 M_B\le2\eta_mN\ell+2C_ANH                       \tag{3.10}
\]

distinct targets at any proper rank.  Under \(\eta_m=o(1)\) and
\(H/\ell=o(1)\), this is \(o(N\ell)\).  Hence ordered cells cannot carry
the central lower support needed by coefficient one.

### Corollary 3.4 -- the linear packet toll is cellwise sharp

In a rainbow packet of height \(s<m\), the \(s\) depth-one shadows in
each fixed-core parity row are all distinct rank-\((m-1)\) sets.  Shadows
from the first row contain its nonempty core \(K\), while shadows from the
second row avoid \(K\), so all \(2s\) are distinct.  The packet has
\(2s+2\) owners.  Theorem 3.2 therefore gives

\[
 L\ge(2s+2)+{2s\over2}=3s+2.                     \tag{3.11}
\]

This equals the exact length of the known linear two-core word.  Thus one
cannot concatenate many packet charts in literal owner-cell chronology and
hope to reduce their order-\(s\) openings.  The required escape is a split
or interleaved noncellular braid.

## 4. The exact unsplit-port ledger

There is a complementary obstruction to concatenating whole canonical
two-core charts without splitting them.  A height-\(s\) chart has length
\(3s+2\) and paired-owner baseline \(2s+2\).  For two charts \(I,J\), let
\(h(I,J)\), \(0\le h(I,J)\le s\), be their largest literal
suffix--prefix port overlap.  If \(F\) is an acyclic directed path forest
on \(t\) charts, direct overlap concatenation has length

\[
 \boxed{
 t(3s+2)-\sum_{I\to J\in F}h(I,J).}              \tag{4.1}
\]

If \(F\) has \(p\) paths, its exact excess over \(t(2s+2)\) is

\[
 \boxed{
 sp+\sum_{I\to J\in F}\bigl(s-h(I,J)\bigr).}    \tag{4.2}
\]

Indeed every overlap identifies exactly \(h(I,J)\) letters, and
\(|E(F)|=t-p\); subtracting the baseline gives (4.2).

Thus an unsplit chronological chart construction at Gaussian height needs
both \(p=o(t)\) and total overlap defect \(o(ts)\).  Full-port equality is
sufficient but not necessary; a maximum-cardinality matching without the
weighted defect and cycle-opening ledger is insufficient.  This is an
architecture obstruction only.  It does not rule out the split erosion
braid of Section 2 or a more general interleaving.

## 5. Why generic endpoint and phase invariants cannot refute QCF

The obstruction in Section 3 is deliberately tied to ordered cells.  Once
owner witnesses may overlap, the desired \(O(NH)\) scale is genuinely
possible in a maximally difficult abstract deck.

### Theorem 5.1 -- rotational maximal-support deck

Let \(r\in\{m,m+1\}\) and assume

\[
 H<\ell,\qquad r>5H,
 \qquad \ell+2H+1\le N-r.                        \tag{5.1}
\]

There is an all-\(N\)-phase rotational deck of chronological rank-\(r\)
Johnson paths with the following properties.

* Its \(N\ell\) assigned owners \(X_{u,i}\),
  \(u\in\mathbb Z_N\), \(0\le i\le\ell-1\), are distinct.
* At every depth \(1\le q\le H\), its internal-plus-two-collar lower
  targets are \(N(\ell+q)\) distinct rank-\((r-q)\) sets, and its upper
  targets are \(N(\ell+q)\) distinct rank-\((r+q)\) sets.
* It has a direct nonzero literal compiler of exact length

  \[
     \boxed{N\ell+4NH}.                           \tag{5.2}
  \]

* For \(r=m\), every Johnson edge has an integral two-edge odd-graph lift;
  for \(r=m+1\), the same holds after complementation.
* The phase indexing may be chosen so the layer transition is the exact
  unit rotor \(v\mapsto v-1\).

#### Proof

Regard the ground set as \(\mathbb Z_N\).  Choose a cyclic interval \(G\)
of size \(r-2H\).  In its complement choose consecutive distinct
coordinates

\[
 a_j,\qquad -H\le j\le\ell+3H-2,                 \tag{5.3}
\]

with one unused separator at each end.  The capacity condition is exactly
the last inequality in (5.1).  Put

\[
 G_u=\rho^uG,
 \qquad a_{u,j}=\rho^ua_j,
\]

and

\[
 X_{u,i}=G_u\cup
 \{a_{u,i},a_{u,i+1},\ldots,a_{u,i+2H-1}\},
 \qquad -H\le i\le\ell+H-1.                     \tag{5.4}
\]

Then

\[
 X_{u,i+1}=X_{u,i}-\{a_{u,i}\}+\{a_{u,i+2H}\}. \tag{5.5}
\]

The large core \(G_u\) is the unique cyclic component of size greater than
\(3H\), while every active component below has size at most \(3H\).
Since a proper cyclic interval has trivial rotational stabilizer, equality
of two owners or two same-sign, same-depth targets first identifies \(u\)
and then the active start.  Thus all asserted targets are distinct.

Directly,

\[
 \bigcap_{h=0}^{q}X_{u,i+h}
 =G_u\cup\{a_{u,i+q},\ldots,a_{u,i+2H-1}\},      \tag{5.6}
\]

and

\[
 \bigcup_{h=0}^{q}X_{u,i+h}
 =G_u\cup\{a_{u,i},\ldots,a_{u,i+2H+q-1}\}.     \tag{5.7}
\]

There are \(\ell+q\) starts \(-q\le i\le\ell-1\), proving the support
counts and ranks.

Emit

\[
 E_{u,j}=G_u\cup\{a_{u,j}\},
 \qquad -H\le j\le\ell+3H-2,                    \tag{5.8}
\]

followed by the core letter \(G_u\).  This phase word has length
\(\ell+4H\).  For every owner interval \([i,j]\) in the full collar,

\[
 \bigcup_{h=i}^{j}X_{u,h}
 =\bigcup_{t=i}^{j+2H-1}E_{u,t},                 \tag{5.9}
\]

and, if \(j-i<2H\),

\[
 \bigcap_{h=i}^{j}X_{u,h}
 =\bigcup_{t=j}^{i+2H-1}E_{u,t}.                 \tag{5.10}
\]

For \(j-i\ge2H\), the intersection is the terminal letter \(G_u\).
Concatenating the \(N\) phase words proves (5.2).

For \(r=m\), the set

\[
 Y_{u,i}=\mathbb Z_N\setminus(X_{u,i}\cup X_{u,i+1})
\]

has rank \(m\) and is disjoint from both owners, so
\(X_{u,i},Y_{u,i},X_{u,i+1}\) is an integral odd-graph path.  Complement
for \(r=m+1\).

Finally relabel the phase at layer \(i\) by \(v=u-i\) and put
\(\overline X_i=\rho^iX_{0,i}\).  Then

\[
 \rho^v\overline X_i=X_{u,i},
\]

while the same physical strand has phase \(v-1\) at the next layer.  This
is the exact unit rotor. \(\square\)

The lower flags in this construction have compatible pin bundles of size
\(H\): at an interior active index \(j\), the single letter
\(E_{u,j}\) serves the \(H\) different starts \(i=j-h\),
\(1\le h\le H\), whose appropriate flag increment is the common pin
\(a_{u,j}\).  Hence even the sharp harmonic pin necessity is attained.

Theorem 5.1 is not a PBBS or exact-factor construction.  It proves only
that local Johnson legality, an odd-graph lift, all phase rotations, unit
voltage, maximal distinct support, and large pin bundles do not obstruct
QCF.  The complete construction and audit are also recorded in
`MATH_ATTACK_W_QCF_PHASE_DECK_INVARIANT_LIMITATION_20260725.md`.

## 6. The exact remaining theorem

The following is now the sole internal statement needed for QCF.

> **Internal noncellular PBBS block compiler \(\operatorname{IQCF}_A\)
> -- unproved.**  For every long quotient block of length
> \(b\le\ell<2b\), use one fixed exact PBBS factor and its complete
> \(N\)-phase deck to replace the \(N\ell\)-position depth-one core spine
> by a nonzero literal word of length
> \[
>   N\ell+\eta_mN\ell+C_ANH,
>   \qquad \eta_m=o_A(1),                         \tag{6.1}
> \]
> such that:
> 
> 1. every assigned middle owner has a literal witness;
> 2. every selected floor-correct lower intersection and every upper union
>    through depth \(H\) wholly inside the block has a literal witness;
> 3. upper prefix and suffix targets needed by adjacent blocks remain
>    exposed, or are replaced by explicitly equal-OR witnesses;
> 4. exact middle ownership is never mixed between factors; and
> 5. owner witnesses may overlap or cross chronological cells, but all
>    target witnesses are ordinary contiguous intervals of the one output
>    word.

Corollary 1.4 proves that \(\operatorname{IQCF}_A\) implies the original
QCF, with only an additional \(O(NH)\) charge per block.  Summing over at
most \(B/b\) blocks gives

\[
 O(\eta_mW)+O(WH/b)=o(W).                        \tag{6.2}
\]

Sections 2--5 give the exact boundary around this statement.

* It is true for long-run/fixed-core blocks and, more generally, for
  decompositions with \(kH=o(\ell)\).
* It is false if “chronological” means disjoint ordered owner cells.
* It cannot be refuted by endpoint, rank, phase-rotation, unit-voltage,
  Johnson-legality, or compatible-pin data alone.
* Unsplit canonical port concatenation needs a near-perfect weighted
  overlap forest; bare port balance is insufficient.
* A genuine negative theorem must use the actual PBBS template recurrence,
  exact-factor extendibility, or an invariant which survives arbitrary
  overlapping owner witnesses.

Thus the requested in-place **outer crossing-border compiler is proved**,
with exact constant \(4H-1\) per physical boundary.  The complete QCF for
arbitrary long PBBS blocks remains open only at its internal noncellular
replacement clause.  No coefficient-one theorem is asserted.

## 7. Audit of decisive scopes

Two independent adversarial audits checked Theorems 1.3, 2.1, 2.3,
3.2, and 5.1.  They forced two substantive corrections now incorporated
above: crossing lower seams are qualified as floor-correct, and every
inter-segment cut in Corollary 2.4 is charged its own \((4H-1)\)-letter
chart.  After those corrections, the displayed constants and coordinatewise
identities were independently confirmed.

1. The lower staircase covers only floor-correct intersections.  Oversized
   intersections are not silently assigned the floor target.
2. The chart in Section 1 covers windows through depth \(H\), not arbitrary
   long ambient intervals.
3. The erosion theorem uses constant endpoint extension and the explicit
   minimum positive-run length \(H+1\).  Without that hypothesis, a short
   internal run can occur in an owner target while occurring in no
   \(D_i\), so (2.4) fails.
4. Theorem 2.3 assumes actual physical chronological seams in one fixed
   factor and a complete phase deck.  Quotient adjacency alone is not
   promoted to physical ownership.  Its arbitrary-length upper preservation
   applies inside each row and along a linearized \(\sigma\)-cycle away
   from the chosen linear cut; only depth-\(H\) upper intervals crossing a
   closing cut are restored by the \(2H\)-owner collar.
5. Theorem 3.2 is a no-go only for disjoint chronological owner cells.  It
   does not refute formal QCF, which permits overlapping and nonlocal owner
   witnesses.
6. Theorem 5.1 has the exact unit rotor after reindexing but is not asserted
   to satisfy the PBBS first-avoided template map or to extend to one exact
   factor.
7. Every positive construction is a literal nonzero OR word.  No fractional
   matching, labelled cross-factor synchronization, or complement-to-OR
   inference is used.
