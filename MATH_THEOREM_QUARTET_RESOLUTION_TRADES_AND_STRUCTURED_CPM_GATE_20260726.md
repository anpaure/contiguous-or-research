# Quartet-resolution packet trades and the structured colored-packet gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver,
generic nibble, or web input is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad R=2^r,
\tag{0.1}
\]

where \(r\) is a power of two, \(H=o(r)\), and \(r=o(m)\).  Start with
the deterministic fixed-frame near-tiling of the middle layer by physical
\(Q_r\) packets.  This note constructs an exact, highly resolved system
of frame-changing trades around that base.

The main conclusions are these.

1.  The three carrier layers

    \[
       J(4,1),\qquad J(4,2),\qquad J(4,3)
    \tag{0.2}
    \]

    have explicit one-factorizations into respectively \(3,4,3\)
    perfect matchings.  Tensoring one carrier matching edge with a common
    \(Q_{r-1}\) gives a legal \(Q_r\) packet.
2.  Two carrier factors differ by exact owner trades of mass \(2R\) or
    \(3R\).  Exchanging an active carrier \(C_i\) for another active
    carrier \(C_j\) is an exact four-packet square of mass \(2R\).  These
    trades use whole packets, so their target ledgers are additive and
    have no seam or collar term.
3.  There is a direct six-packet adapter from the original fixed-pair
    shore on a central \(B_4\) carrier to a mixed-frame resolved shore.
    It changes the frame on a region of \(6R\) owners and leaves no owner
    boundary.
4.  Partitioning the coordinates into quartets gives a deterministic
    packet near-tiling whose owner leave is at most

    \[
       4\,2^c\sum_{e<r}\binom ce7^e
       =2^{m/2+o(m)}=o(W/H),
       \qquad c=\lfloor m/2\rfloor.                 \tag{0.3}
    \]

    On every retained owner block, the active carrier set and the local
    one-factors can be changed through the preceding bounded trade atoms.
5.  The union of the resulting fixed-quartet packet/compiler options has
    only \(2^{m/2+o(m)}\) literal target holes at each protected signed
    depth.  This is only potential reachability.  It does **not** remove
    the Gaussian capacity cut: the corrected fixed-mosaic ratio

    \[
       R_q(g,u)={2^q\binom gq\over\binom{u+q}q}
       \longrightarrow e^{-6A^2}\quad(q=A\sqrt m)    \tag{0.4}
    \]

    is below one on a positive-density typical family for the earlier
    **restricted** three-edge \(Q_4\) mosaic.  The enlarged atlas here also
    uses \(J(4,1)\), every factor of \(J(4,2)\), and \(J(4,3)\); (0.4)
    does not count all of its sources.  The replacement theorem
    `MATH_THEOREM_FULL_INTERNAL_QUARTET_ATLAS_GAUSSIAN_HALL_CUT_20260726.md`
    proves a different Hall cut for the complete internal atlas: an
    internal lower window preserves the number of full quartets, and a
    Gaussian profile window has source/target ratio tending to
    \(e^{-A^2/11}<1\).
6.  There is an additional exact cross-quartet trade.  On two quartets it
    replaces internal Johnson one-factors by a one-factor of the regular
    bipartite graph which exchanges one coordinate between the quartets.
    Its owner mass is at most \(24R\), and the union of its local profile
    sectors has density \(7/16+o(1)\).  This changes the four-block
    occupancy profile on positive owner mass.  There are in fact two internal comparison shores:
    cross versus the large-layer shore transports upper profiles on
    \(13/32+o(1)\) owner density, while cross versus the small-layer shore
    transports lower profiles on \(13/32+o(1)\) owner density.  A packet
    in this elementary trade has only one crossing axis, so only a
    \(q/r\) fraction of its depth-\(q\) windows sees that axis; owner
    density is not occurrence density.  See
    `MATH_THEOREM_TWO_SIGN_CROSS_QUARTET_PROFILE_TRANSPORT_20260726.md`.
7.  After admitting those cross-quartet transports, the remaining
    selection problem is an exact hierarchical resolution-flow problem,
    not an owner hypergraph matching.  Every choice of one local resolved
    shore already gives an owner near-factor.  If \(Z_{a,T}\) is its
    literal target load and \(c_a=\lfloor(W-L)/N_a\rfloor\), it remains to
    reach

    \[
       Q=\sum_{a,T}(Z_{a,T}-c_a)(Z_{a,T}-c_a-1)=o(W). \tag{0.5}
    \]

    The exact change of \(Q\) under a trade with target derivative
    \(\delta\) is

    \[
       Q(Z+\delta)-Q(Z)
       =2\langle Z-c-\tfrac12,\delta\rangle
        +\|\delta\|_2^2.                              \tag{0.6}
    \]

    For every elementary trade constructed here,

    \[
                         \|\delta\|_2^2=O(HR)         \tag{0.7}
    \]

The note therefore proves the owner trade atlas, identifies the exact
failure of every fixed-quartet chronology, and supplies the first
profile-changing transport atoms needed by a positive hierarchy.  It
reduces `CPM` to one strictly smaller target-anticorrelation lemma on a
multiscale resolution graph.  It does not claim that union coverage alone
implies the required integral selection: the fixed-quartet capacity ratio
already proves otherwise.

## 1. The three exact \(B_4\) resolutions

Let \(C=\{1,2,3,4\}\).  At occupancy \(k\), a legal one-dimensional
orientation packet is an edge of the Johnson graph \(J(C,k)\).

For \(k=1\), identify a vertex with its unique element.  The following
three one-factors partition \(E(K_4)\):

\[
\begin{aligned}
 \Phi^1_0&=\{12,34\},\\
 \Phi^1_1&=\{13,24\},\\
 \Phi^1_2&=\{14,23\}.
\end{aligned}                                               \tag{1.1}
\]

Complementation gives the corresponding resolution of \(J(C,3)\).

For \(k=2\), abbreviate

\[
 A=12,\quad B=34,\quad C'=13,\quad D=24,\quad E=14,\quad F=23.
\tag{1.2}
\]

The nonedges of \(J(4,2)\) are the complementary pairs
\(AB,C'D,EF\).  Removing that one-factor from a one-factorization of
\(K_6\) leaves the following four one-factors of \(J(4,2)\):

\[
\begin{aligned}
 \Phi^2_0&=\{AC',BE,DF\},\\
 \Phi^2_1&=\{AD,BF,C'E\},\\
 \Phi^2_2&=\{AE,BD,C'F\},\\
 \Phi^2_3&=\{AF,BC',DE\}.
\end{aligned}                                               \tag{1.3}
\]

In literal subset notation, for example,

\[
 \Phi^2_0
 =\bigl\{\{12,13\},\{34,14\},\{24,23\}\bigr\}.
\tag{1.4}
\]

Every displayed pair consists of Johnson neighbors, and the four rows of
(1.3) partition all \(12\) edges of the octahedral graph \(J(4,2)\).

### Lemma 1.1 (carrier resolution)

For \(k\in\{1,2,3\}\), the graph \(J(4,k)\) has a one-factorization

\[
                  \mathfrak F_k
                  =\{\Phi^k_0,\ldots,
                     \Phi^k_{k(4-k)-1}\}.             \tag{1.5}
\]

Each local Johnson edge occurs in exactly one factor, and every local
owner occurs once in every factor.

#### Proof

Equations (1.1)--(1.4) give the factorizations for \(k=1,2\);
complementation gives \(k=3\).  The degree of \(J(4,k)\) is
\(k(4-k)\), equal to the displayed number of factors, so the edge counts
also certify exhaustion. \(\square\)

## 2. Tensoring a carrier resolution with packet reservoirs

Let \(Q\cong Q_{r-1}\) be a physical orientation packet on coordinate
pairs disjoint from \(C\).  For an edge \(e\in E(J(C,k))\),

\[
                              e\times Q               \tag{2.1}
\]

is a physical \(Q_r\): its first orientation coordinate is the exchange
pair labelling \(e\), and its other \(r-1\) coordinates are those of
\(Q\).

For a fixed \(\Phi\in\mathfrak F_k\), the family

\[
                         \{e\times Q:e\in\Phi\}       \tag{2.2}

partitions \(\binom Ck\times Q\) into \(Q_r\) packets.

### Theorem 2.1 (one-carrier frame trade)

Let \(\Phi,\Psi\in\mathfrak F_k\).  The union
\(\Phi\cup\Psi\) is a disjoint union of alternating even cycles.  For
every such cycle \(D\),

\[
 \{e\times Q:e\in D\cap\Phi\}
 \quad\longleftrightarrow\quad
 \{e\times Q:e\in D\cap\Psi\}                       \tag{2.3}
\]

is an exact owner trade on \(V(D)\times Q\).

For \(k=1,3\), every nontrivial component has length four and owner mass
\(4\cdot2^{r-1}=2R\).  For \(k=2\), two different factors in (1.3) are
edge-disjoint, so their union is a six-cycle and the owner mass is
\(6\cdot2^{r-1}=3R\).

#### Proof

The union of two perfect matchings is a disjoint union of alternating even
cycles, with common edges giving trivial two-cycles.  On a nontrivial
cycle, either colour class partitions the same vertex set.  Cartesian
product with \(Q\) preserves this equality of owner sets and turns every
selected edge into a \(Q_r\) packet.  The component sizes follow from
(1.1)--(1.3). \(\square\)

Every shore in (2.3) consists of whole packets.  Installing one certified
context-array factor in each packet therefore gives an additive literal
target ledger: no interval crosses between packets, and there is no port,
connector, or collar correction.

## 3. The active-carrier exchange square

Let \(C_i,C_j\) be disjoint quartets with occupancies
\(k_i,k_j\in\{1,2,3\}\).  Let

\[
 L_i=\binom{C_i}{k_i},\qquad
 L_j=\binom{C_j}{k_j},                                 \tag{3.1}
\]

and let \(Q\cong Q_{r-1}\) use directions disjoint from both carriers.
Choose \(\Phi_i\in\mathfrak F_{k_i}\) and
\(\Phi_j\in\mathfrak F_{k_j}\).

There are two packet tilings of

\[
                            L_i\times L_j\times Q.     \tag{3.2}
\]

The \(i\)-active shore is

\[
 \mathcal P_i
 =\{e\times\{y\}\times Q:e\in\Phi_i, y\in L_j\};  \tag{3.3}
\]

the \(j\)-active shore is

\[
 \mathcal P_j
 =\{\{x\}\times f\times Q:x\in L_i, f\in\Phi_j\}. \tag{3.4}
\]

### Theorem 3.1 (four-packet carrier exchange)

For every \(e=\{x_0,x_1\}\in\Phi_i\) and
\(f=\{y_0,y_1\}\in\Phi_j\),

\[
\begin{aligned}
 &\{e\times\{y_0\}\times Q,
     e\times\{y_1\}\times Q\}\\
 &\hspace{25mm}\longleftrightarrow
 \{\{x_0\}\times f\times Q,
     \{x_1\}\times f\times Q\}                     \tag{3.5}
\end{aligned}
\]

is an exact two-packet-versus-two-packet trade.  Its owner set is

\[
                             e\times f\times Q         \tag{3.6}
\]

and has mass \(4\cdot2^{r-1}=2R\).  The trades (3.5), over all
\((e,f)\), are disjoint and transform \(\mathcal P_i\) into
\(\mathcal P_j\).

#### Proof

Both shores of (3.5) plainly partition (3.6).  Distinct pairs
\((e,f)\) have disjoint Cartesian owner sets because \(\Phi_i,\Phi_j\)
are matchings.  Their union is (3.2), proving the last assertion.
\(\square\)

This is the basic frame-moving square.  It does more than change the pair
inside one carrier: it moves one complete active packet direction from
\(C_i\) to \(C_j\) while preserving every owner.

## 4. A literal adapter from the fixed-frame base

The central occupancy-two layer needs a separate audit because a fixed
pair frame does not tile all six carrier states by one-dimensional cells.
Let the old carrier matching be

\[
                             12\mid34.                 \tag{4.1}
\]

Let \(Q\cong Q_r\) be a disjoint outside packet, and assume \(r\ge2\).
On the owner region

\[
                             J(4,2)\times Q             \tag{4.2}
\]

there is an exact fixed-frame shore of six \(Q_r\) packets:

1. \(\{12\}\times Q\) and \(\{34\}\times Q\);
2. on the four cross states \(13,14,23,24\), use the two carrier axes
   \(12,34\), partition \(Q\) into the four subcubes obtained by fixing
   two chosen outside axes, and take the four products
   \(Q_2\times Q_{r-2}\).

Choose any \(\Phi\in\mathfrak F_2\).  Partition \(Q\) into two
\(Q_{r-1}\) halves by fixing one outside axis.  The six products

\[
                         e\times Q_{r-1},
             \qquad e\in\Phi,                         \tag{4.3}
\]

with both halves used, form a mixed-frame shore of six \(Q_r\) packets.

### Theorem 4.1 (six-packet fixed-to-moving adapter)

The two shores just described partition the same \(6R\) owners in
(4.2).  Replacing one shore by the other is therefore an exact
frame-changing packet trade with zero owner boundary.

#### Proof

The two singleton fixed-frame cells contribute \(2R\) owners.  The cross
cell has four carrier states, and its four
\(Q_2\times Q_{r-2}\) packets partition \(4R\) owners.  This is all
\(6R\) owners of (4.2).

On the moving shore, \(\Phi\) has three edges and each is tensored with
two disjoint \(Q_{r-1}\) halves.  The resulting six packets likewise
partition \(J(4,2)\times Q\). \(\square\)

At occupancies one and three, the restriction of a fixed coordinate
matching is already one member of (1.1), or its complement.  Theorem 2.1
then supplies the fixed-to-moving trade directly.  Occupancies zero and
four are frozen and require no carrier move.

Thus the deterministic fixed-frame near-tiling is not discarded: its
large outside cubes are reservoirs for exact local frame adapters.

## 4A. Cross-quartet profile transport

The preceding trades change pair frames but preserve the occupancy of
every fixed quartet.  The corrected Gaussian capacity theorem shows that
this is not enough.  We now construct an exact trade which changes the
quartet occupancy profile itself.

Let \(A,B\) be two disjoint four-sets.  For \(1\le k\le4\), put

\[
\begin{aligned}
 V_k^+&=\binom Ak\times\binom B{k-1},\\
 V_k^-&=\binom A{k-1}\times\binom Bk.
\end{aligned}                                                \tag{4A.1}
\]

Join \(X\in V_k^+\) to \(Y\in V_k^-\) when \(Y\) is obtained by
deleting one coordinate of \(X\cap A\) and inserting one coordinate of
\(B\setminus X\).  This is a literal Johnson edge crossing the old
quartet boundary.

### Lemma 4A.1 (cross-profile one-factorization)

The bipartite graph between \(V_k^+\) and \(V_k^-\) is
\(k(5-k)\)-regular and therefore decomposes into \(k(5-k)\) perfect
matchings.

#### Proof

The two shores have the common size

\[
                       \binom4k\binom4{k-1}.          \tag{4A.2}
\]

From a plus vertex one chooses one of its \(k\) occupied coordinates in
\(A\) and one of the \(5-k\) unoccupied coordinates in \(B\).  The same
count holds backwards.  Thus the graph is regular bipartite.  Repeated
application of Hall's theorem removes a perfect matching at every step
and proves the one-factorization. \(\square\)

There is also an internal shore on the same owner set.  On \(V_k^+\),
hold the \(B\)-state fixed and use one local Johnson one-factor on the
nontrivial layer in \(A\); on \(V_k^-\), do the symmetric operation in
\(B\).  For \(k=4\), use the occupancy-three layer in the opposite
quartet.  Thus both \(V_k^+\) and \(V_k^-\) are partitioned by internal
Johnson edges.

Let \(Q\cong Q_{r-1}\) be a disjoint packet reservoir.

### Theorem 4A.2 (internal-to-cross packet trade)

For every \(1\le k\le4\), tensoring the internal shore and any one
cross-profile factor from Lemma 4A.1 with \(Q\) gives two exact tilings of

\[
                         (V_k^+\dot\cup V_k^-)\times Q \tag{4A.3}
\]

by physical \(Q_r\) packets.  Replacing one shore by the other is an
exact owner trade of mass

\[
 \binom4k\binom4{k-1}R\le24R.                       \tag{4A.4}
\]

Every packet on the cross shore has one active coordinate pair meeting
both old quartets, so the trade moves owners between the two fixed
four-block profiles on positive packet mass.

#### Proof

Every internal or cross factor edge contains two owners.  Tensor product
with \(Q_{r-1}\) makes it a \(Q_r\) packet.  Both one-factors partition
the same local owner set, proving exactness.  The local owner set has
twice the size in (4A.2); multiplication by \(2^{r-1}=R/2\) gives
(4A.4). \(\square\)

The four local sectors in (4A.3) occupy

\[
 2\sum_{k=1}^4\binom4k\binom4{k-1}
 =112                                                   \tag{4A.5}
\]

of the \(2^8=256\) subsets of \(A\cup B\).  Therefore, under every
central rank conditioning with displacement \(o(m)\), one disjoint round
of paired-quartet transports is available on

\[
                              {7\over16}+o(1)           \tag{4A.6}
\]

of the owners.  This is positive density, not a boundary correction.
To supply the tensor factor \(Q_{r-1}\), apply the deterministic
fixed-frame near-tiling to the remaining \(2m-8\) coordinates in every
residual rank sector.  Its low-split exception has exponentially small
middle mass for \(r=o(m)\), so it changes (4A.6) only by \(o(1)\).

A hierarchy may try to pair the quartet blocks by successive matchings of
the quartet index set.  Theorem 4A.2 supplies an exact local move, but two
additional facts are not automatic: owner sectors for different quartet
pairs overlap globally, and one elementary cross packet has only one
crossing axis.  Hence a disjoint scheduler and a mechanism accumulating
many crossing axes are both still required before one obtains a genuine
round at target-occurrence scale.

There is a useful two-sign refinement.  For \(k\le3\), compare the cross
factor with the internal shore which factors the occupancy-\(k\) layer:
the lower profile agrees and the upper profile changes.  For \(k\ge2\),
compare it with the shore which factors the occupancy-\((k-1)\) layer:
the upper profile agrees and the lower profile changes.  Summing the local
sector sizes gives \(104/256=13/32\) owner density for each sign.  The
complete proof and profile table are in
`MATH_THEOREM_TWO_SIGN_CROSS_QUARTET_PROFILE_TRANSPORT_20260726.md`.

## 5. A deterministic all-quartet near-tiling

Partition all but at most two ground coordinates into

\[
                       C_1\dot\cup\cdots\dot\cup C_c,
              \qquad |C_i|=4,\quad c=\lfloor m/2\rfloor. \tag{5.1}
\]

Any leftover pair is frozen exactly and plays no further role.  For an
owner \(X\), put

\[
 k_i(X)=|X\cap C_i|,qquad
 E(X)=\{i:1\le k_i(X)\le3\}.                          \tag{5.2}
\]

Call \(X\) good if \(|E(X)|\ge r\).  For every occupancy vector
\(\mathbf k=(k_1,\ldots,k_c)\) with at least \(r\) eligible positions,
choose a deterministic \(r\)-subset

\[
                              A(\mathbf k)\subseteq E(\mathbf k). \tag{5.3}
\]

For every inactive position \(i\notin A(\mathbf k)\), freeze the exact
local subset \(S_i\in\binom{C_i}{k_i}\).  The resulting owner block is

\[
 \mathcal B(\mathbf k,\mathbf S)
 =\prod_{i\in A(\mathbf k)}\binom{C_i}{k_i}
  \times\prod_{i\notin A(\mathbf k)}\{S_i\}.          \tag{5.4}
\]

The rank is constant on (5.4), so it lies in the middle layer.  Choose one
factor \(\Phi_i\in\mathfrak F_{k_i}\) at every active position.  The
Cartesian products

\[
                              \prod_{i\in A}e_i,
              \qquad e_i\in\Phi_i,                    \tag{5.5}
\]

partition (5.4) into physical \(Q_r\) packets.

### Theorem 5.1 (resolved deterministic owner near-factor)

Equations (5.3)--(5.5), over all occupancy vectors and inactive tags,
give a deterministic owner-disjoint \(Q_r\)-packet tiling of every good
middle owner.  The owner leave \(L_r\) satisfies

\[
 L_r
 \le4\sum_{e<r}\binom ce14^e2^{c-e}
 =4\,2^c\sum_{e<r}\binom ce7^e.                      \tag{5.6}
\]

If \(r=o(m)\), then

\[
                 L_r=2^{m/2+o(m)},
 \qquad {L_r\over W}=2^{-3m/2+o(m)},                 \tag{5.7}
\]

and in particular \(L_r=o(W/H)\) for every \(H\le m\).

#### Proof

For a fixed block (5.4), every factor \(\Phi_i\) partitions its local
layer into two-element edges.  Their Cartesian products are disjoint
\(2^r\)-sets and exhaust the block.  The inactive tags and occupancy
vectors partition the good owners, proving exactness.

To count bad owners, ignore the global rank constraint.  Choose the
\(e<r\) eligible quartets; each has \(14\) nonempty, nonfull subsets, and
each ineligible quartet has the two choices empty or full.  The leftover
pair has at most four subsets.  This proves (5.6).  Since \(r=o(c)\),

\[
             \log_2\sum_{e<r}\binom ce7^e=o(m).       \tag{5.8}
\]

Finally \(W=2^{2m-o(m)}\), giving (5.7). \(\square\)

### Theorem 5.2 (connected resolution trade atlas)

Fix an occupancy sector.  The following operations connect all canonical
choices of active \(r\)-set and local one-factors:

1. change \(\Phi_i\) through the one-carrier trades of Theorem 2.1;
2. replace \(i\in A\) by \(j\in E(\mathbf k)\setminus A\) through the
   disjoint carrier-exchange squares of Theorem 3.1.

Every elementary owner component used in this connection has mass at most
\(3R\).  The owner leave remains exactly the fixed set of bad owners.

#### Proof

The graph of \(r\)-subsets of \(E(\mathbf k)\), joined when they exchange
one element, is the connected Johnson graph
\(J(|E(\mathbf k)|,r)\).  Theorem 3.1 implements each of its edges by
disjoint exact owner trades.  For a fixed active set, Theorem 2.1 connects
all choices inside each local one-factorization.  Concatenate the two
types of moves. \(\square\)

The atlas is therefore a deterministic resolution space around an owner
near-factor.  No random residual owner set is ever produced.

## 6. The option union has negligible literal target holes

We now allow every legal cube-affine conjugate of the certified local
compiler on each selected packet.  Such a conjugation permutes the packet
axes and reverses the two endpoints of any axes; it preserves the packet
owner set, whole-cycle legality, and simultaneous trace injectivity.

### Lemma 6.1 (prescribed return-free window)

Let \(P\cong Q_r\) be one physical packet, let \(X\in P\), and let
\(e_1,\ldots,e_q\) be distinct packet axes, where \(q\le H<r\).  There is
a cube-affine conjugate of the certified factor and a cycle start at
\(X\) whose next \(q\) directions, in order, are
\(e_1,\ldots,e_q\).

#### Proof

Choose any certified factor cycle and any start.  Isometry makes its next
\(q\) directions distinct.  A permutation of the \(r\) cube axes sends
that ordered direction list to \(e_1,\ldots,e_q\).  A cube translation,
equivalently reversing the endpoint labels on selected physical pairs,
sends the resulting start to \(X\).  Conjugation preserves the whole
factor and every trace-injectivity statement. \(\square\)

For a set \(T\subseteq[2m]\), let

\[
             e(T)=\#\{i:1\le|T\cap C_i|\le3\}.       \tag{6.1}
\]

Call a target quartet-typical if \(e(T)\ge r\).

### Theorem 6.2 (literal union coverage)

For every \(q\le H\), every quartet-typical lower target
\(T\in\binom{[2m]}{m-q}\) and every quartet-typical upper target
\(U\in\binom{[2m]}{m+q}\) occurs literally in some option of the resolved
packet atlas.

#### Proof

First take a lower target \(T\).  The number of quartets having
\(|T\cap C_i|\le2\) is at least

\[
 c-{|T|\over3}={m\over6}+{q\over3}+O(1).             \tag{6.2}
\]

Since \(q\le H=o(m)\), choose distinct such quartets
\(C_{i_1},\ldots,C_{i_q}\).  In \(C_{i_j}\), choose two coordinates
\(a_j,b_j\notin T\), and put

\[
                         X=T\cup\{a_1,ldots,a_q\}.   \tag{6.3}
\]

Then \(X\) is a middle owner, \(a_j\in X\), \(b_j\notin X\), and
\(\{a_j,b_j\}\) is a Johnson edge incident with the local state
\(X\cap C_{i_j}\).  The selected quartets are eligible for \(X\).
No previously eligible quartet was destroyed, so \(e(X)\ge e(T)\ge r\).
Extend them to an active \(r\)-set.

By Lemma 1.1, the desired incident edge lies in one local one-factor;
choose that factor in every selected quartet and choose arbitrary incident
factor edges in the other active quartets.  Their product is a packet
containing \(X\).  Lemma 6.1 supplies a window which performs
\(a_j\mapsto b_j\) for \(j=1,\ldots,q\).  Its literal intersection is

\[
                         X\setminus\{a_1,ldots,a_q\}=T. \tag{6.4}
\]

For an upper target \(U\), the number of quartets having
\(|U\cap C_i|\ge2\) is at least

\[
 {|U|-c\over3}={m\over6}+{q\over3}+O(1).             \tag{6.5}

Choose \(q\) of them and distinct ordered pairs
\(a_j,b_j\in U\cap C_{i_j}\).  Put

\[
                         X=U\setminus\{b_1,ldots,b_q\}. \tag{6.6}
\]

Again \(X\) is a good middle owner and the local exchanges
\(a_j\mapsto b_j\) lie in chosen carrier factors.  Lemma 6.1 gives a
window whose literal union is \(U\). \(\square\)

### Corollary 6.3 (negligible immutable union holes)

At every rank, the number of non-typical targets is at most

\[
 E_r
 \le4\,2^c\sum_{e<r}\binom ce7^e
 =2^{m/2+o(m)}.                                      \tag{6.7}
\]

Therefore

\[
                 \sum_{q\le H,\epsilon}E_r=o(W).     \tag{6.8}
\]

#### Proof

The counting argument is identical to (5.6) and does not use the target
rank.  Multiply by at most \(2H\le2m\), and use
\(W=2^{2m-o(m)}\). \(\square\)

This is stronger than saying that the full coordinate orbit has a
fractional cover.  It gives a fixed quartet resolution atlas whose literal
option union already misses only exponentially few targets.  In
particular a positive fixed-pair residual cut cannot be an immutable-union
invariant of this atlas.

It is not a capacity theorem.  The corrected theorem
`MATH_THEOREM_Q4_MIXED_FRAME_MOSAIC_POTENTIAL_GAUSSIAN_COVER_20260726.md`
computes, for a fixed product-cell target type with \(g\) good singleton
blocks and \(u\) two-set blocks, the exact compatible-source ratio

\[
                         R_q(g,u)
 =\frac{2^q\binom gq}{\binom{u+q}q}.                 \tag{6.9}
\]

At \(q=A\sqrt m\), this tends to \(e^{-6A^2}\) on a positive-density
typical profile and yields a linear Hall deficit.  Thus Corollary 6.3 may
be used only to rule out immutable union holes.  It may not be used to
deduce a chronology inside one fixed product decomposition.  The
cross-profile packets of Theorem 4A.2 are one possible escape: unlike
every option in the full block-internal atlas, they can change the number
of full quartets between a lower target and its middle source (and,
dually, the number of empty quartets on the upper side).  The full-atlas
Hall theorem cited above proves that \(\Omega_A(W)\) noninternal
depth-\(q\) occurrences are necessary.

## 7. Exact target optimization on the trade graph

Let \(\mathcal P\) be any resolved owner near-tiling and install one legal
compiler option in every selected packet.  For a typed signed depth
\(a=(q,\epsilon)\), let

\[
 Z_{a,T}(\mathcal P)
 =\#\{\text{selected packet occurrences with literal target }T\}. \tag{7.1}
\]

The total occurrence mass in every target part is

\[
                         S=W-L_r.                    \tag{7.2}
\]

Put

\[
 c_a=\left\lfloor{S\over N_a}\right\rfloor,
 \qquad
 Q_a(\mathcal P)
 =\sum_T(Z_{a,T}-c_a)(Z_{a,T}-c_a-1),                \tag{7.3}
\]

and \(Q=\sum_aQ_a\).  Every summand is a nonnegative even integer.

### Proposition 7.1 (floor energy is sufficient)

For every resolved tiling,

\[
 \sum_a\#\{T:Z_{a,T}=0\}
 \le 2HL_r+{Q(\mathcal P)\over2}.                    \tag{7.4}
\]

Consequently \(Q(\mathcal P)=o(W)\) proves `CPM` for the present atlas.

#### Proof

This is the exact floor-balanced inequality.  At target part \(a\), the
unavoidable cardinality deficit is at most \((N_a-S)_+\le L_r\).  Every
additional hole contributes at least two to (7.3).  Sum over the \(2H\)
parts and use (5.7). \(\square\)

Let \(\tau\) be one trade from Sections 2--4, with arbitrary legal
compiler labels on its two shores.  Its complete typed target derivative
is

\[
                         \delta_\tau=Z(\mathcal P+\tau)-Z(\mathcal P). \tag{7.5}
\]

### Theorem 7.2 (exact quadratic trade derivative)

For every legal trade,

\[
 \boxed{
 Q(\mathcal P+\tau)-Q(\mathcal P)
 =2\langle Z-c-\tfrac12,\delta_\tau\rangle
  +\|\delta_\tau\|_2^2.}                            \tag{7.6}
\]

For the elementary trades of Theorems 2.1 and 3.1,

\[
                         \|\delta_\tau\|_2^2\le36HR. \tag{7.7}
\]

For the fixed-frame adapter of Theorem 4.1 the corresponding bound is
\(144HR\).  For the cross-profile trade of Theorem 4A.2 it is at most
\(2304HR\).

#### Proof

For one coordinate, with \(f(z)=(z-c)(z-c-1)\),

\[
 f(z+d)-f(z)=2(z-c-\tfrac12)d+d^2.                  \tag{7.8}
\]

Summing proves (7.6).

An elementary shore has at most three packets.  At one signed depth it
has at most \(3R\) target occurrences.  Thus
\(\|\delta\|_1\le6R\) and \(\|\delta\|_\infty\le3\), whence

\[
                         \|\delta\|_2^2
 \le\|\delta\|_1\|\delta\|_\infty\le18R.           \tag{7.9}
\]

There are \(2H\) typed parts.  The adapter has six packets per shore,
giving \(\|\delta\|_1\le12R\),
\(\|\delta\|_\infty\le6\), and hence \(72R\) per typed part.  The
cross-profile shore has at most \(24\) packets, giving
\(\|\delta\|_1\le48R\), \(\|\delta\|_\infty\le24\), and hence
\(1152R\) per typed part.  The displayed bounds follow. \(\square\)

For literal holes rather than multiplicities, define

\[
\begin{aligned}
 G_\tau&=\#\{(a,T):Z_{a,T}=0, Z_{a,T}+\delta_{a,T}>0\},\\
 D_\tau&=\#\{(a,T):Z_{a,T}>0, Z_{a,T}+\delta_{a,T}=0\}.
\end{aligned}                                               \tag{7.10}
\]

Then exactly

\[
 \operatorname{Hol}(\mathcal P+\tau)-
 \operatorname{Hol}(\mathcal P)=D_\tau-G_\tau.       \tag{7.11}
\]

Thus any collection of currently legal trades satisfying

\[
                         \sum_\tau G_\tau>\sum_\tau D_\tau   \tag{7.12}
\]

contains a literal improving trade.  Equations (7.6) and (7.12) are the
two exact optimization forms supplied by the resolution.

## 8. The smaller remaining hierarchical lemma

The preceding construction removes two false obstructions but exposes one
real one.

1. Growing packet size causes no owner-matching problem: every resolution
   choice is already an owner near-factor.
2. Connected complete-frame support causes no frame lock: the local
   trades change frames on \(\Theta(R)\) owners with zero boundary.
3. Potential target abundance is not source capacity.  The old ratio
   (6.9) treats the restricted mosaic; the full-atlas theorem cited above
   rules out every version using only block-internal axes inside one
   permanent quartet decomposition.

The amount of profile crossing required is itself exact.

### Theorem 8.1 (baseline-alteration toll)

Fix \(A>0\) and \(q=\lfloor A\sqrt m\rfloor\).  Let
\(\delta_A>0\) be the full block-internal deficit coefficient from
`MATH_THEOREM_FULL_INTERNAL_QUARTET_ATLAS_GAUSSIAN_HALL_CUT_20260726.md`.
Suppose a packet factor uses physically cross-quartet axes on at most
\(B\) middle-owner occurrences at depth \(q\).
Then its lower target deficit is at least

\[
                         (\delta_A-o(1))W-B.          \tag{8.2}
\]

The same holds on the upper side.  Consequently every successful
construction needs \(\Omega_A(W)\) depth-\(q\) occurrences containing a
physically cross-quartet axis.

#### Proof

The full block-internal atlas misses \((\delta_A-o(1))W\) targets because
it preserves the full-quartet profile.  One noninternal owner occurrence
supplies only one depth-\(q\) literal target and can therefore add at most
one target from the deficient profile window.  After \(B\) such
occurrences, at least the quantity in (8.2) remains.  Complement for the
upper statement. \(\square\)

Theorem 4A.2 has positive owner scale, but not yet the required occurrence
scale.  If a packet has \(s\) crossing axes, at most an \(sq/r\) fraction
of its depth-\(q\) starts contain one.  The elementary cross packet has
\(s=1\), so a bounded number of such owner rounds contributes only
\(O((q/r)W)=o(W)\) crossing occurrences when \(q\le H=o(r)\).  Conditional
on a future theorem showing that linearly many physical crossings are
necessary, typical packets would need \(\Omega_A(r/q)\) crossing axes, or
an equivalent exterior-moving macro.  The unresolved issue is therefore
both to schedule overlapping rounds and to accumulate crossing axes while
preserving all-depth target anticorrelation.

### `HCRT` -- hierarchical cross-resolution transport

For some powers of two \(r=o(m)\) and heights
\(\sqrt m\ll H=o(r)\), there is a hierarchy built from

* the deterministic fixed-frame packet reservoirs;
* the internal carrier resolutions of Theorems 2.1 and 3.1;
* the fixed-to-moving adapters of Theorem 4.1;
* positive-density cross-quartet rounds from Theorem 4A.2, using changing
  pairings of the quartet index set; and
* legal cube-affine compiler conjugates,

which remains an owner near-factor with leave (5.7) and ends at a tiling
\(\mathcal P\) satisfying

\[
                              Q(\mathcal P)=o(W).       \tag{8.3}
\]

  The hierarchy must alter linearly many occurrences relative to any
  baseline for which a linear Hall deficit is proved.  It is not yet known
  whether the enlarged internal atlas itself has such a deficit or whether
  physically cross-quartet windows are necessary.

### Theorem 8.2 (`HCRT` implies `CPM`)

`HCRT` implies the simultaneous colored packet matching theorem with
owner leave \(o(W/H)\) and aggregate literal target leave \(o(W)\).

#### Proof

Every operation is an exact replacement of whole packet shores on one
common owner set.  Hence the owner leave remains (5.7), and every selected
packet retains a certified all-depth compiler.  Proposition 7.1 and
(8.3) give aggregate target leave \(o(W)\). \(\square\)

The useful next theorem is not a low-codegree nibble.  Any one of the
following structured conclusions would suffice.

* **Hierarchical floor-energy descent:** whenever \(Q\) is not \(o(W)\),
  a closed alternating cycle using internal and cross-quartet trades makes
  the right side of (7.6) negative.
* **Literal exchange expansion:** whenever the current hole mass is not
  \(o(W)\), a legal collection containing positive-density cross-profile
  trades satisfies (7.12).
* **Defect circulation:** overload units above \(c_a+1\) can be routed
  through the changing quartet decompositions to loads below \(c_a\),
  with total collateral quadratic cost \(o(W)\).

These statements retain exact physical target identities.  Proving only
potential path abundance, orbit balance, average frame mobility, or
independent-template variance would not establish them.

## 9. Audited boundary

Proved here:

* an explicit resolution of every nontrivial \(B_4\) carrier layer;
* exact fixed-to-moving, factor-changing, and active-carrier packet trades;
* an exact cross-quartet profile transport on at most \(24R\) owners per
  local atom, with local sector density \(7/16+o(1)\) for one fixed
  quartet pair;
* a deterministic all-quartet owner near-factor with exponentially small
  leave;
* connectivity of its canonical frame-resolution choices by trades of
  owner mass at most \(3R\);
* negligible potential holes in the union of all fixed-quartet options;
* the full internal-atlas Gaussian Hall cut and the necessity of
  \(\Omega_A(W)\) physically noninternal target occurrences;
* the consequent average toll \(\Omega_A(r/q)\) crossing axes per packet
  at depth \(q=A\sqrt m\);
* exact literal-hole and floor-energy derivatives; and
* the reduction `HCRT` \(\Rightarrow\) `CPM`.

Not proved here:

* that a pair of endpoint tilings has negligible union holes—two-factor
  trades cannot repair targets absent from both endpoints;
* a disjoint scheduler for overlapping quartet-pair owner sectors;
* closure of the packet class while accumulating the required number of
  crossing axes;
* that independent local template choices have sublinear collision
  energy; or
* the multiscale resolution-flow/augmenting-cycle inequality `HCRT`.

The construction nevertheless changes the shape of the remaining gate.
There is no longer a need to find an owner matching among \(2^r\)-edges.
The owners are tiled deterministically throughout.  The sole unresolved
step is a colored, all-depth circulation on an explicit hierarchy that
first builds dense cross-frame packets at the occurrence scale and then
rounds their common signed target ledger with sublinear aggregate loss.
