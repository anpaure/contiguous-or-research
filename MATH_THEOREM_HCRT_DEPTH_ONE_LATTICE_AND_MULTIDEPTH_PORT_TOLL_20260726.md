# HCRT at depth one: the exact Johnson target lattice and the multidepth port toll

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver,
generic nibble, or web input is used.

## 0. Outcome

Let

\[
 \mathcal L=\binom{[2m]}{m-1},\qquad
 \mathcal U=\binom{[2m]}{m+1},\qquad
 W=\binom{2m}{m}.                                      \tag{0.1}
\]

This note continues the quartet-resolution construction of
`MATH_THEOREM_QUARTET_RESOLUTION_TRADES_AND_STRUCTURED_CPM_GATE_20260726.md`
and attacks its hierarchical cross-resolution gate `HCRT`.

The exact conclusions are as follows.

1.  At depth one, identify an upper target with its complement, another
    member of \(\mathcal L\).  If \(M\) is the point-versus-
    \((m-1)\)-set incidence matrix, the complete integral target-
    derivative lattice of unrestricted Johnson owner trades is

    \[
      \boxed{
      \Lambda_1=\{(x,y)\in\mathbb Z^{\mathcal L}\oplus
      \mathbb Z^{\mathcal L}:
      \mathbf1^Tx=\mathbf1^Ty=0,\ Mx=My\}.          \tag{0.2}
    \]

    It is generated integrally by Johnson squares and two-triangle
    bowties.  This is an integer statement, not merely equality of real
    spans.
2.  In the original lower/upper coordinates, the only real orthogonal
    invariants are

    \[
       \sum_Lx_L,qquad \sum_Uz_U,qquad
       \sum_{L\ni v}x_L+\sum_{U\ni v}z_U
       \quad(v\in[2m]).                                \tag{0.3}
    \]

    The displayed rows have one dependence, so their rank is \(2m+1\).
3.  A depth-one floor vector has load one or two on every target.  Put

    \[
                         C={W\over m+1}.               \tag{0.4}
    \]

    If \(\mathcal B^-\subseteq\mathcal L\) and
    \(\mathcal B^+\subseteq\mathcal U\) are the doubled targets, the
    complete lattice invariants are

    \[
      |\mathcal B^-|=|\mathcal B^+|=C,qquad
      \deg_{\mathcal B^-}(v)+\deg_{\mathcal B^+}(v)=C
      \quad(v\in[2m]).                                \tag{0.5}
    \]

    Thus the depth-one pilot has no hidden real target invariant beyond
    the common run-count law.
4.  The complete internal \(J(4,2)\) atlas realizes every bowtie
    generator as an *integral sum of two perfect-matching trades*.
    Changing block pairings embeds this identity on every active
    four-coordinate set, while active-carrier and cross-quartet trades
    move the embedding between frames.  The two-port lift then realizes
    paired exterior copies.  For each fixed active coordinate
    pattern, the exterior port graph is a connected nonbipartite Johnson
    distance graph.  Its unsigned incidence lattice has cokernel
    \(\mathbb Z/2\mathbb Z\).  Consequently the physical depth-one trade
    lattice has the same rational span as \(\Lambda_1\), and its only
    extra integral obstructions are at most one parity bit for each
    four-coordinate bowtie type.

    There are \(O(m^4)\) such types.  Hence every member of
    \(\Lambda_1\) can be changed on \(O(m^4)=o(W)\) target coordinates
    to enter the literal packet-trade lattice.  This proves depth-one
    lattice controllability up to negligible repair.
5.  The same port construction does not nest for free.  If it changes
    packet factors on \(B\) owners, it changes

    \[
                         \Theta\!\left({qB\over r}\right) \tag{0.6}
    \]

    certified length-\(q\) windows in its natural two-port lift.  Summing
    through \(H\) gives the exact scale

    \[
                         \Theta\!\left({H^2B\over r}\right). \tag{0.7}
    \]

    At the positive-density crossing scale \(B=\Theta(W)\), this cannot
    be charged as loss: in the required regime
    \(H/\sqrt m\to\infty\) and \(r=o(m)\), one has
    \(H^2/r\to\infty\).
6.  The two-sign cross-quartet theorem removes the last *local linear*
    sign obstruction.  On \(13/32+o(1)\) of the owners, cross versus
    large-layer changes the upper profile and fixes the lower profile;
    on another \(13/32+o(1)\), cross versus small-layer changes the lower
    profile and fixes the upper profile.  On their common sectors these
    give two integral directions, but the legal local choices form a
    triangle, not two independent switches.
7.  A one-crossing-axis packet changes at most a \(q/r\) fraction of its
    depth-\(q\) occurrences.  An independent audit of the full internal
    quartet atlas proves that at \(q=A\sqrt m+O(1)\) a successful factor
    needs \(\delta_AW\) cross-quartet window occurrences, for some
    \(\delta_A>0\).  Hence one disjoint two-sign round transports at most

    \[
             \left({13\over32}+o(1)\right){qW\over r} \tag{0.8}
    \]

    occurrences of either sign, while repairing the forced depth-\(q\)
    Hall deficit requires at least

    \[
             \left({32\delta_q\over13}-o(1)\right){r\over q} \tag{0.9}
    \]

    elementary rounds, or the same weighted number of crossing axes
    compiled simultaneously into the packets.  Density \(13/32\) alone
    therefore gives no common all-depth selection.
8.  Independently of those quantitative tolls, every genuine all-depth
    derivative has one common integer run vector \(s_v\):

    \[
    \boxed{
      \sum_{T\ni v}\delta_q^-(T)=-q s_v,qquad
      \sum_{U\ni v}\delta_q^+(U)=q s_v
      \quad(q\le H).}                                  \tag{0.10}
    \]

    Therefore independently chosen depthwise lattice corrections cannot
    be nested unless their point margins lie on this common affine line.

The depth-one lattice gate is thus closed up to a polynomial repair set.
The remaining `HCRT` theorem must be a genuinely multidepth coboundary:
it must make the \(\Theta(qB/r)\) connector windows beneficial or cancel
them between hierarchical rounds, while preserving the common run line
(0.10).  Repeating the depth-one construction separately at every depth
incurs a provably unusable \(H^2/r\) ledger.

## 1. Three-rank flag notation

Every undirected Johnson edge between middle owners has the unique form

\[
 X=L\cup\{a\},\qquad Y=L\cup\{b\},\qquad
 U=L\cup\{a,b\},                                      \tag{1.1}
\]

where \(L\in\mathcal L\), \(U\in\mathcal U\), and
\(a\ne b\).  Thus Johnson edges are in bijection with the flags

\[
                         \mathcal E=\{(L,U):L\subset U\}. \tag{1.2}
\]

Let

\[
 \partial_0:\mathbb Z^{\mathcal E}\longrightarrow
              \mathbb Z^{\binom{[2m]}m}              \tag{1.3}
\]

be unsigned middle incidence: a flag contributes one at each of its two
intermediate middle sets.  Let

\[
 \partial_1:\mathbb Z^{\mathcal E}\longrightarrow
              \mathbb Z^{\mathcal L}\oplus
              \mathbb Z^{\mathcal U}                 \tag{1.4}
\]

send a flag to its lower and upper endpoints.

The difference of two spanning middle \(2\)-factors is an integral edge
vector \(z\) satisfying

\[
                              \partial_0z=0.          \tag{1.5}
\]

Its signed target derivative is \(\partial_1z\).

Complement upper targets.  Write

\[
                         y_A=\delta^+_{[2m]\setminus A}
                         \qquad(A\in\mathcal L).      \tag{1.6}
\]

Let \(M\) be the \(2m\)-by-\(|\mathcal L|\) matrix

\[
                         M_{v,A}=\mathbf1_{\{v\in A\}}. \tag{1.7}
\]

### Lemma 1.1 (universal depth-one invariants)

Every \((x,y)=\partial_1z\), in complemented coordinates, satisfies

\[
                         \mathbf1^Tx=\mathbf1^Ty=0,
 \qquad Mx=My.                                      \tag{1.8}
\]

#### Proof

Every edge derivative contributes one lower and one upper target, so
their two total derivatives vanish.  At a coordinate \(v\), the number
of selected lower targets containing \(v\), plus the number of selected
upper targets containing \(v\), is invariant under a degree-preserving
middle-edge trade.  After upper complementation and use of
\(\mathbf1^Ty=0\), this becomes \((Mx)_v=(My)_v\). \(\square\)

The same statement follows from the run ledger: changing the number of
deletions of \(v\) changes the lower point count by the negative amount
and the upper point count by the positive amount.

## 2. Square and bowtie generators

Let \(K\) be an \((m-2)\)-set and let \(a,b,c,d\) be distinct outside
\(K\).  The four middle owners

\[
 Kac,\quad Kbc,\quad Kbd,\quad Kad                  \tag{2.1}
\]

form a Johnson square.  Replacing the two \(ab\)-edges by the two
\(cd\)-edges gives the lower derivative

\[
 \rho_K(a,b;c,d)
 =e_{K+a}+e_{K+b}-e_{K+c}-e_{K+d}.                  \tag{2.2}

\]

Its upper derivative is

\[
\begin{split}
 &e_{K+a+c+d}+e_{K+b+c+d}\\
 &\hspace{18mm}-e_{K+a+b+c}-e_{K+a+b+d}.             \tag{2.3}
\end{split}
\]

A bowtie is the even closed walk obtained by traversing two Johnson
triangles having one common middle owner.  Give its six consecutive edges
alternating signs.  At the common owner the four signed incidences cancel;
at every other owner the two cancel.  If the two triangles have lower
cores \(L_0,L_1\), its lower marginal is

\[
                              e_{L_0}-e_{L_1}.        \tag{2.4}
\]

The two lower cores are adjacent in \(J(2m,m-1)\).  More explicitly,
let \(K\) have size \(m-2\), let \(a,b,c,d\notin K\) be distinct, and
put

\[
                         D=[2m]\setminus(Kabcd).      \tag{2.5}
\]

Traverse the triangles with lower cores \(K+a\) and \(K+b\), shared
middle owner \(K+a+b\), and unused vertices \(c,d\).  In complemented
upper coordinates its full derivative is

\[
 \beta(K;a,b;c,d)=
 \bigl(e_{K+a}-e_{K+b},\ e_{D+a}-e_{D+b}\bigr).      \tag{2.6}
\]

### Lemma 2.1 (uniform-set exchange lattice)

For \(1\le k<n-1\), the integral kernel of the point-incidence map

\[
 \mathbb Z^{\binom{[n]}k}\longrightarrow\mathbb Z^n,
 \qquad e_A\longmapsto\mathbf1_A                   \tag{2.7}
\]

is generated by the symmetric exchanges

\[
 e_A+e_B-e_{A-a+b}-e_{B-b+a},                       \tag{2.8}
\]

where \(a\in A\setminus B\) and \(b\in B\setminus A\).

#### Proof

Write the positive and negative parts of a kernel vector as two
multisets of \(k\)-sets.  They contain the same number of sets and have
the same multiplicity of every ground element.  Regard either multiset as
a bipartite graph: its left vertices are the labelled set occurrences,
its right vertices are the ground elements, and incidence is membership.
After arbitrarily pairing the left occurrences, the two graphs have the
same degree at every vertex.

Their symmetric difference is a union of alternating even circuits.
On one such circuit, exchange the two opposite incidences in a
\(2\times2\) submatrix and shorten the circuit by two; induction reduces
it to the other graph.  Each \(2\times2\) switch replaces two rows
\(A,B\) by \(A-a+b,B-b+a\), and hence is exactly (2.8).  Conversely
every such switch preserves all point degrees. \(\square\)

### Lemma 2.2 (integral three-rank exactness)

For \(m\ge4\),

\[
 \boxed{
 \partial_1(\ker_{\mathbb Z}\partial_0)=\Lambda_1.} \tag{2.9}
\]

Moreover \(\ker_{\mathbb Z}\partial_0\) may be generated, for the
purpose of its target image, by Johnson squares and bowties.

#### Proof

Containment in \(\Lambda_1\) is Lemma 1.1.  For the reverse inclusion,
take \((x,y)\in\Lambda_1\).

Bowties lift every adjacent lower transfer
\(e_A-e_{A'}\).  Since \(J(2m,m-1)\) is connected and
\(\mathbf1^Tx=0\), a sum of lower bowties has lower marginal exactly
\(x\).  Subtract its full target derivative from \((x,y)\).  The
remaining pair is \((0,y')\), and (1.8) gives

\[
                              My'=0.                 \tag{2.10}
\]

By Lemma 2.1, decompose \(y'\) into symmetric exchanges.  Fixing the
lower transfer of a bowtie while changing its two unused triangle
coordinates changes the core \(D\) in the second component of (2.6).
Thus, whenever \(D_0,D_1\) are \((m-2)\)-sets avoiding \(a,b\) and
their Johnson distance is at most two, choose an \((m-2)\)-set \(K\)
disjoint from \(D_0\cup D_1\cup\{a,b\}\).  Such a \(K\) exists because
\(|D_0\cup D_1|\le m\).  Two bowties with this common
\((K;a,b)\) and complementary unused pairs have difference

\[
 \bigl(0,\,
 (e_{D_0+a}-e_{D_0+b})-
 (e_{D_1+a}-e_{D_1+b})\bigr).                       \tag{2.11}
\]

The Johnson graph on the \((m-2)\)-sets avoiding \(a,b\) is connected,
so (2.11) telescopes between arbitrary \(D_0,D_1\).  Every symmetric
exchange (2.8) is precisely such a difference of two adjacent transfers
with the same exchanged pair \(a,b\).  Hence every term in the
decomposition of \(y'\) has an integral bowtie lift with lower marginal
zero.

This proves (2.9).  Finally, the integral kernel of the unsigned incidence
matrix of a graph is generated by alternating even closed walks.  In a
Johnson graph, commute two disjoint consecutive exchanges to cut off a
square.  Two consecutive exchanges sharing a coordinate cut off a
triangle; triangles occur in pairs in an even walk and the intervening
segment turns them into a bowtie.  Induction on walk length leaves only
squares and bowties. \(\square\)

### Theorem 2.3 (exact depth-one derivative lattice)

The integral target-derivative lattice generated by unrestricted Johnson
owner trades is exactly \(\Lambda_1\).

Its real orthogonal complement consists precisely of functions

\[
\begin{aligned}
 f^-(L)&=\alpha+\sum_{v\in L}a_v,\\
 f^+(U)&=\beta +\sum_{v\in U}a_v,                    \tag{2.12}
\end{aligned}

with arbitrary \(\alpha,\beta,a_v\).  The parametrization has the one
expected redundancy coming from the fixed target ranks.

#### Proof

The lattice assertion is Lemma 2.2.  The equations defining
\(\Lambda_1\) show that every pair (2.9) annihilates it.  Conversely, the
annihilator of the kernel of an integer matrix is the row space of that
matrix over \(\mathbb R\).  The rows in (1.8) are exactly the two
constants and the coupled point incidences, giving (2.9). \(\square\)

## 3. Exact floor consequences at depth one

Since

\[
 {W\over|\mathcal L|}={m+1\over m}=1+{1\over m},     \tag{3.1}
\]

an exactly floor-balanced load has value two on

\[
                         C=W-|\mathcal L|={W\over m+1} \tag{3.2}
\]

targets and value one on all others.  Let these bonus families be
\(\mathcal B^-\) and \(\mathcal B^+\).

### Theorem 3.1 (complete depth-one floor invariants)

The necessary affine lattice conditions on a depth-one floor pair are
exactly

\[
 |\mathcal B^-|=|\mathcal B^+|=C,                  \tag{3.3}
\]

\[
 \deg_{\mathcal B^-}(v)+\deg_{\mathcal B^+}(v)=C
                  \qquad(v\in[2m]).                 \tag{3.4}
\]

Differences of any two floor pairs satisfying (3.3)--(3.4) belong to
\(\Lambda_1\).

#### Proof

The total number of surplus occurrences is (3.2) on each sign.  The
depth-one run identity gives

\[
 \deg_{\mathcal B^-}(v)=C-R_v,qquad
 \deg_{\mathcal B^+}(v)=R_v,                        \tag{3.5}
\]

where \(R_v\) is the number of deletions of coordinate \(v\).  This
proves (3.4).  Conversely, subtract two pairs satisfying (3.3)--(3.4),
complement the upper targets, and obtain exactly (1.8). \(\square\)

This is only a lattice statement.  It does not assert that every
nonnegative floor point is the target profile of one cyclic factor.  The
remaining distinction is cone and chronology, not an undiscovered linear
or congruence invariant at depth one.

## 4. Physical porting through the quartet trade atlas

Take one of the matching trades from the internal, active-carrier, or
cross-quartet resolutions.  Its two local shores are perfect matchings of
one common finite owner set, and their union is a disjoint collection of
even alternating cycles.

Fix one distinguished carrier direction in an isometric \(C_{2r}\)-factor
of a \(Q_r\) packet.  Deleting the two edges of that direction from every
cycle leaves two geodesic paths of length \(r-1\), with two exposed ports.
Keep all these path interiors fixed.  At each port, reconnect the paths by
one or the other local matching shore.

### Lemma 4.1 (two-port depth-one lift)

On every alternating local matching component, both reconnections are
spanning degree-two factors of the same owner set.  Every path-interior
depth-one edge is common to the two factors.  Their target derivative is
exactly two exterior copies of the local matching derivative, one at each
port.

#### Proof

Two-colour the vertices of the alternating local cycle.  Assign one
deleted-direction path shore to each colour.  Every edge of either local
matching joins opposite colours, so reconnecting at both exposed endpoints
closes the same path interiors into cycles.  Every vertex retains degree
two.  Only the two connector matchings change, proving the target
statement. \(\square\)

For the depth-one pilot, this is a literal legal cycle-factor trade.  It
does not yet assert the certified all-depth trace property after
reconnection; Section 6 audits that missing lift.

It remains to verify that a bowtie is genuinely in the *integral*
matching-trade lattice of one quartet.  For its four active coordinates
\(a,b,c,d\), abbreviate

\[
 A=ab,\quad B=cd,\quad C=ac,\quad D=bd,\quad E=ad,\quad F=bc. \tag{4.1a}
\]

Besides the four one-factors \(\Phi_0,\ldots,\Phi_3\) displayed in the
quartet-resolution theorem, the complete \(J(4,2)\) atlas has

\[
\begin{aligned}
 \Psi_0&=\{AC,BF,DE\},&
 \Psi_1&=\{AD,BE,CF\},\\
 \Psi_2&=\{AE,BC,DF\},&
 \Psi_3&=\{AF,BD,CE\}.                               \tag{4.1b}
\end{aligned}
\]

With the earlier convention

\[
\begin{aligned}
 \Phi_1&=\{AD,BF,CE\},\\
 \Phi_3&=\{AF,BC,DE\},
\end{aligned}
\]

direct cancellation gives

\[
 (\Psi_2-\Phi_1)+(\Psi_0-\Phi_3)
       =AC+AE+DF-AD-CE-AF,                          \tag{4.1c}
\]

which is precisely the six-edge bowtie used in (2.6).  Thus every
bowtie is an integral sum of two exact one-factor trades, not merely a
real combination.  Changing quartet decompositions places arbitrary
\(a,b,c,d\) in one carrier.  Active-carrier and cross-quartet trades move
that carrier between frames.  The remaining coordinates form an exterior
tag.

Fix one such active four-coordinate pattern \(\sigma\).  For a fixed
exterior rank, let \(G_{\sigma,d}\) join two tags when their Johnson
distance is the port distance \(d=r-O(1)\).

Since \(r=o(m)\),
both the tag rank and its corank exceed \(2d\) for all large \(m\).

### Lemma 4.2 (port graph lattice)

The graph \(G_{\sigma,d}\) is connected and nonbipartite.  The lattice
generated by its unsigned edge columns \(e_s+e_t\) is

\[
 \left\{z\in\mathbb Z^{V(G_{\sigma,d})}:
                 \sum_s z_s\equiv0\pmod2\right\}.    \tag{4.1}
\]

#### Proof

The distance-\(d\) Johnson graph is connected: if two tags differ, replace
up to \(d\) wrong coordinates at a time, padding a shorter final exchange
through fresh coordinates and undoing the padding on the next step.  The
rank and corank hypotheses supply those fresh coordinates.

It contains a triangle.  Take a common core of the tag rank minus \(d\)
and three pairwise disjoint \(d\)-sets outside it.  Their unions with the
core are pairwise at distance \(d\).

For any connected graph, differences of columns along an even walk give
\(e_s-e_t\) whenever the two vertices have the appropriate parity in a
spanning tree.  An odd cycle removes the parity restriction and gives
\(2e_s\).  Hence all even-total vectors lie in the column lattice.  Every
column has total two, proving the reverse inclusion. \(\square\)

### Theorem 4.3 (physical depth-one saturation up to negligible repair)

Let \(\Lambda_1^{\rm pkt}\) be the signed literal target lattice generated
by the two-port lifts of all internal, carrier-exchange, and cross-quartet
trades, allowing all changing quartet pairings.  Then

\[
                         \Lambda_1^{\rm pkt}\subseteq\Lambda_1, \tag{4.2}
\]

the two lattices have the same real span, and the quotient has at most one
\(\mathbb Z/2\mathbb Z\) generator for every active four-coordinate
bowtie pattern.

Consequently, for every \(z\in\Lambda_1\), there is
\(e\in\Lambda_1\) supported on \(O(m^4)\) target coordinates such that

\[
                              z-e\in\Lambda_1^{\rm pkt}. \tag{4.3}
\]

In particular \(\|e\|_0=O(m^4)=o(W)\).

#### Proof

Inclusion follows from Lemma 1.1.  Lemma 2.2 and its proof decompose
\(z\), for target-image purposes, into bowtie generators.  Identity
(4.1c) realizes each local bowtie integrally by exact matching trades,
and Lemma 4.1 realizes it in paired exterior tags.  Lemma 4.2 says that all
coefficient vectors of even total over those tags are integral
combinations of physical port pairs; there is only one possible parity
obstruction.

There are \(O(m^4)\) active bowtie patterns.  For each pattern with odd
coefficient total, remove one local generator from
the desired derivative.  Each removed generator changes only constantly
many literal target coordinates.  The remainder has even coefficient
sum in every port graph and is physically generated.  This proves (4.3).
\(\square\)

For a floor target, the exceptional coordinates in (4.3) may be left for
literal repair.  Their polynomial number is negligible compared with
\(W\).  No assertion is made that the signed lattice decomposition itself
stays inside the nonnegative cone at every intermediate trade.

## 4A. The exact two-sign cross-quartet menu

We now incorporate
\`MATH_THEOREM_TWO_SIGN_CROSS_QUARTET_PROFILE_TRANSPORT_20260726.md\`.
Let \(A,B\) be the paired four-blocks, and write

\[
 V_k^+=\binom Ak\times\binom B{k-1},\qquad
 V_k^-=\binom A{k-1}\times\binom Bk.                 \tag{4.4}
\]

There are three local matching shores:

\[
 L=\text{large-layer},\qquad C=\text{cross},\qquad
 S=\text{small-layer}.                              \tag{4.5}
\]

The shore \(L\) exists for \(k=1,2,3\), \(S\) exists for
\(k=2,3,4\), and \(C\) exists throughout.  Let \(\Pi_-\) and
\(\Pi_+\) denote projection of a literal target derivative to its lower
and upper *two-block size profile*.  The exact profile identities are

\[
\begin{array}{c|cc}
 \text{comparison}&\Pi_-&\Pi_+\\ \hline
 C-L&0&u_k\\
 C-S&\ell_k&0 ,
\end{array}                                         \tag{4.6}
\]

where \(u_k\ne0\) for \(k=1,2,3\), and
\(\ell_k\ne0\) for \(k=2,3,4\).  The zeroes in (4.6) are profile
zeroes; they do not say that every literal target on the unchanged sign
is fixed.

### Proposition 4.4 (rank two, but a triangular selection cone)

On the overlap sectors \(k=2,3\), the two signed directions
\(C-L\) and \(C-S\) are integrally independent after profile projection.
Consequently the two-sign theorem introduces no additional rational or
integral linear invariant at depth one.

It does not introduce two independent binary switches.  Encode a shore
by whether its lower and upper profiles are the balanced cross profiles.
Then

\[
                  L=(1,0),\qquad C=(1,1),\qquad S=(0,1). \tag{4.7}
\]

Thus the convex hull of legal one-shore selections is

\[
 0\le \lambda_-,\lambda_+\le1,\qquad
 \lambda_-+\lambda_+\ge1,                            \tag{4.8}
\]

not the full unit square.  Equivalently,

\[
                    S-L=(C-L)-(C-S).                 \tag{4.9}
\]

The signed lattice has two directions, but their nonnegative
realization is coupled by one local three-state choice.

#### Proof

For \(C\), the lower and upper profiles are respectively
\((k-1,k-1)\) and \((k,k)\).  The large shore has the same lower
profile and an unbalanced upper profile; the small shore has an
unbalanced lower profile and the same upper profile.  This proves
(4.6)--(4.7).  The two nonzero entries occupy different direct summands,
so they are integrally independent.  The convex hull of the three
vectors in (4.7) is exactly (4.8), and subtraction gives (4.9).
\(\square\)

The exact local masses sharpen the common-selection audit.  The two
overlap sectors \(k=2,3\) contain

\[
 2\binom42\binom41+2\binom43\binom42
             =48+48=96                              \tag{4.10}
\]

of the \(256\) local patterns.  The \(k=1\) upper-only boundary and the
\(k=4\) lower-only boundary contain \(8\) patterns each.  Hence

\[
 \begin{aligned}
  \mu(C-L)&={96+8\over256}+o(1)={13\over32}+o(1),\\
  \mu(C-S)&={96+8\over256}+o(1)={13\over32}+o(1),\\
  \mu(\text{common sectors})&={96\over256}+o(1)
                                      ={3\over8}+o(1).
 \end{aligned}                                      \tag{4.11}
\]

The two \(13/32\) resources overlap on \(3/8\) of all owners.  Counting
them as disjoint would therefore double-count almost their entire mass.
Counting them as simultaneous independent controls would ignore the
triangle constraint (4.8).

### Lemma 4.5 (crossing-axis occurrence budget)

Let an exact \(Q_r\) packet factor act on \(B\) owners and let
\(c(P)\) be the number of packet directions declared to cross the
current quartet partition.  For \(q<r/2\), the number of cyclic
length-\(q\) window occurrences meeting at least one crossing direction
is at most

\[
                         {q\,c(P)\,B\over r}.         \tag{4.12}
\]

For one crossing axis, equality holds.  Therefore one disjoint
cross-versus-large or cross-versus-small round can transport at most

\[
              \left({13\over32}+o(1)\right){qW\over r} \tag{4.13}
\]

depth-\(q\) occurrences of its designated sign.

#### Proof

An isometric \(C_{2r}\) uses each of its \(r\) directions twice.  Since
the factor has \(B/(2r)\) cycles, a fixed direction occurs on \(B/r\)
edges.  Each directed edge belongs to exactly \(q\) cyclic windows of
length \(q\).  Union bounding over \(c(P)\) crossing directions gives
(4.12).  For one direction its two appearances on a cycle are separated
by \(r\), so the corresponding window-start sets are disjoint when
\(q<r/2\), giving equality.  Restricting to the \(13/32+o(1)\) owner
sectors in (4.11) proves (4.13). \(\square\)

### Corollary 4.6 (necessary crossing multiplicity)

Suppose a sign-specific physical Hall deficit at depth \(q\) has size
\(\delta_qW\), with \(\delta_q>0\) fixed, and suppose it can be repaired
only by windows containing a crossing axis for the current quartet
partition.  Then any family of packet changes repairing it must satisfy

\[
       \sum_P c(P)|P|\ \ge\ (\delta_q-o(1)){r\over q}W. \tag{4.14}
\]

If it is assembled from disjoint elementary two-sign rounds, each with
one crossing axis and the \(13/32\) availability in (4.11), their number
\(t_q\) satisfies

\[
             t_q\ge
             \left({32\delta_q\over13}-o(1)\right){r\over q}. \tag{4.15}
\]

This is a necessary capacity inequality, not a sufficiency assertion.
For \(q=A\sqrt m\) and \(r/q\to\infty\), a bounded number of elementary
rounds cannot repair the positive Gaussian fixed-frame deficit.  A
positive HCRT construction must compile a growing number of
owner-dependent crossing axes into common packets, or prove that the
same physical crossing windows simultaneously discharge several
depths.  The local density \(13/32\) does neither by itself.

## 4B. Independent audit of the full-internal-atlas Hall cut

The premise of Corollary 4.6 is not optional.  We now verify it for the
complete atlas of quartet-internal \(J(4,1)\), \(J(4,2)\), and
\(J(4,3)\) factors.

Fix a partition of \([2m]\) into \(c=m/2\) labelled quartets and put

\[
                  F(S)=|\{Q:Q\subseteq S\}|.          \tag{4.16}
\]

### Lemma 4.7 (full-quartet conservation)

Let \(T\) be the intersection of a return-free depth-\(q\) window, and
let \(X\) be any middle owner on that window.  If every direction in the
window is internal to one quartet of the fixed partition, then

\[
                              F(T)=F(X).              \tag{4.17}
\]

#### Proof

An internal exchange preserves the cardinality in each quartet.  If a
quartet is full in \(X\), its local state is the unique four-set and no
internal Johnson edge can change it; it is full in every owner and in
their intersection.  If it is not full in \(X\), then the intersection
\(T\subseteq X\) cannot be full there.  This proves equality quartet by
quartet.  The argument permits arbitrary internal one-factors, active
quartets, direction orders, and compiler conjugates. \(\square\)

Let

\[
\begin{aligned}
 \mathcal T_{q,k}&=\{T\in\tbinom{[2m]}{m-q}:F(T)=k\},\\
 \mathcal X_k&=\{X\in\tbinom{[2m]}m:F(X)=k\}.
\end{aligned}                                       \tag{4.18}
\]

One owner supplies one start at a fixed signed depth.  Lemma 4.7
therefore gives the exact Hall lower bound

\[
       \sum_k\bigl(|\mathcal T_{q,k}|-|\mathcal X_k|\bigr)_+ \tag{4.19}
\]

for the number of missed lower targets in every all-internal factor.

### Lemma 4.8 (audited Gaussian coefficient ratio)

Let \(q=A\sqrt m+O(1)\), and put

\[
                   k={m\over32}+y\sqrt m+O(1).       \tag{4.20}
\]

Uniformly for \(y\) in a fixed compact interval,

\[
 \log{|\mathcal X_k|\over|\mathcal T_{q,k}|}
                  ={15A^2+64Ay\over11}+o(1).         \tag{4.21}
\]

In particular, at \(y=-A/4\),

\[
             {|\mathcal X_k|\over|\mathcal T_{q,k}|}
                         \longrightarrow e^{-A^2/11}<1. \tag{4.22}
\]

#### Proof

For a nonfull quartet the rank generating polynomial is

\[
                  h(z)=1+4z+6z^2+4z^3.              \tag{4.23}
\]

Choosing the \(k\) full quartets first gives

\[
\begin{aligned}
 |\mathcal T_{q,k}|&=\binom ck[z^{m-q-4k}]h(z)^{c-k},\\
 |\mathcal X_k|&=\binom ck[z^{m-4k}]h(z)^{c-k}.       \tag{4.24}
\end{aligned}
\]

The common binomial factor cancels.  Normalize \(h\) and let

\[
 \Pr(J=j)={\binom4j\over15}\quad(0\le j\le3).
\]

Direct calculation gives

\[
                 \mu={28\over15},\qquad
                 \sigma^2={176\over225}.             \tag{4.25}
\]

Writing \(d=c-k\), one has

\[
 d={15m\over32}-y\sqrt m+O(1),\qquad
 \sigma^2d={11m\over30}+O(\sqrt m).                  \tag{4.26}
\]

For \(s_T=m-q-4k\) and \(s_X=s_T+q\),

\[
\begin{aligned}
 s_T-\mu d&=\left(-A-{32y\over15}\right)\sqrt m+O(1),\\
 s_X-\mu d&=-{32y\over15}\sqrt m+O(1).               \tag{4.27}
\end{aligned}
\]

The span-one local central limit estimate for the bounded variable \(J\)
is uniform on compact \(y\)-intervals.  Substitution of (4.26)--(4.27)
into its Gaussian exponent gives

\[
 -{(s_X-\mu d)^2-(s_T-\mu d)^2\over2\sigma^2d}
                  ={15A^2+64Ay\over11}+o(1),
\]

which is (4.21).  Setting \(y=-A/4\) gives (4.22).
\(\square\)

### Theorem 4.9 (linear Hall deficit for the complete internal atlas)

For each fixed \(A>0\), there is \(\delta_A>0\) such that, at
\(q=A\sqrt m+O(1)\), every middle-owner factor whose depth-\(q\)
windows are internal to the fixed quartet partition misses at least

\[
                         (\delta_A-o(1))W             \tag{4.28}
\]

lower targets.  The same holds for upper targets.

Consequently every successful packet construction has
\(\Omega_A(W)\) depth-\(q\) windows containing a cross-quartet axis and
satisfies

\[
        {1\over W}\sum_P c(P)|P|
                         =\Omega_A\!\left({r\over q}\right). \tag{4.29}
\]

#### Proof

Restrict \(y\) to

\[
 -{A\over4}-{A\over128}\le y\le
 -{A\over4}+{A\over128}.                             \tag{4.30}
\]

Equation (4.21) is then at most
\(-A^2/22+o(1)\).  In the uniform target layer, \(F(T)\) has mean

\[
               {m\over32}-{A\over8}\sqrt m+O(1)      \tag{4.31}
\]

and conditional variance \(\Theta(m)\).  The bivariate local central
limit theorem for (total rank, number of full quartets), or equivalently
Stirling's formula applied to (4.24), shows that the window (4.30)
contains \(c_A+o(1)\) of the target layer for a constant \(c_A>0\).
Thus (4.19) is at least

\[
 (c_A-o(1))(1-e^{-A^2/22})
                    \binom{2m}{m-q}.                 \tag{4.32}
\]

Finally

\[
 {\binom{2m}{m-q}\over W}\longrightarrow e^{-A^2},  \tag{4.33}
\]

which proves (4.28).  Complementation replaces full lower quartets by
empty upper quartets and gives the upper statement.

Each changed start can fill at most one missing literal target, so
\(\Omega_A(W)\) successful starts must contain a crossing axis.  Applying
the union bound (4.12) packet by packet proves (4.29). \(\square\)

The exponent and centering in this audit are internally consistent:
\(\sigma^2(c-k)=11m/30+O(\sqrt m)\), the target profile mean is at
\(y=-A/8\), and the deficient cut at \(y=-A/4\) is only a constant
number of standard deviations away.  Hence its target mass is genuinely
positive; the proof does not confuse a positive-density owner sector with
a positive-density depth-\(q\) occurrence sector.

## 5. Universal multidepth run-line invariant

Let two \(H\)-safe factors have signed target derivative
\(\delta_q^-,\delta_q^+\) at depth \(q\).  Let \(s_v\) be the difference
of their coordinate deletion-run counts.

### Theorem 5.1 (common derivative line)

For every \(q\le H\) and every coordinate \(v\),

\[
 \boxed{
 \sum_{T\ni v}\delta_q^-(T)=-q s_v,
 \qquad
 \sum_{U\ni v}\delta_q^+(U)=q s_v.}                \tag{5.1}
\]

Moreover \(s_v\in\mathbb Z\) and

\[
                              \sum_vs_v=0.           \tag{5.2}
\]

Thus

\[
 {1\over q}\sum_{T\ni v}\delta_q^-(T)
 ={1\over j}\sum_{T\ni v}\delta_j^-(T)             \tag{5.3}
\]

for all protected \(q,j\), with the analogous upper and cross-sign
identities.

#### Proof

For one factor, the all-depth run theorem gives lower point load
\(W/2-qR_v\) and upper point load \(W/2+qR_v\).  Subtract the two factor
identities.  Each factor has \(W\) transitions and hence
\(\sum_vR_v=W\), proving (5.2). \(\square\)

### Corollary 5.2 (integral divisibility and floor compatibility)

Every depth-\(q\) point derivative is divisible by \(q\), and all
normalized derivatives use the same integer vector.  Therefore a family
of independently chosen depthwise floor vectors is nestable only if its
lower and upper high-quota point degrees lie on the common affine run line
of Theorem 5.1.

This is a true cross-depth lattice invariant.  The depth-one saturation
theorem does not remove it.

## 6. Exact toll of the natural two-port nesting

We now test the most literal attempt to use the depth-one construction at
all depths.  In a \(C_{2r}\), the two occurrences of one distinguished
direction are separated by \(r\) transitions.  Assume \(H<r/2\).

Let a two-port trade act on \(B\) owner states.  The affected factors have

\[
                         {B\over2r}                 \tag{6.1}
\]

isometric cycles and therefore

\[
                         J={B\over r}                \tag{6.2}
\]

changed connector edges on each shore.

### Theorem 6.1 (connector-window census)

At depth \(q<r/2\), exactly \(qJ\) cyclic windows on each shore contain a
changed connector.  For the canonical port lift their old and new literal
targets have different decoded direction supports.  Hence the complete
old-plus-new derivative is supported on

\[
                         2qJ={2qB\over r}             \tag{6.3}
\]

literal window occurrences.  Summing over \(q\le H\) gives

\[
 \sum_{q=1}^H{2qB\over r}
 ={B H(H+1)\over r}.                                \tag{6.4}
\]

#### Proof

One directed cycle edge belongs to exactly \(q\) cyclic intervals of
\(q\) transitions.  The two distinguished-direction connectors on one
cycle are distance \(r\) apart, so their interval sets are disjoint for
\(q<r/2\).  This gives \(qJ\) windows on one shore.

The old and new connectors use different physical coordinate pairs.
Every window counted in (6.3) contains that connector, so the
coordinate-disjoint local decoder distinguishes its completed support
from the support on the opposite shore.  Trace injectivity distinguishes
the starts within a shore.  Therefore no counted old occurrence cancels
its new counterpart.  Summation gives (6.4). \(\square\)

The theorem is a ledger statement, not automatically a hole lower bound:
new targets may be beneficial and old targets may have other occurrences.
It does prove that a method which charges every non-depth-one connector
window as collateral pays the exact scale \(BH^2/r\).

### Corollary 6.2 (separate-depth nesting is quantitatively unusable)

Put \(q_0=A\sqrt m+O(1)\).  Suppose the construction is assembled from
elementary one-crossing-axis rounds, and let \(B_i\) be the owner mass of
round \(i\).  Theorem 4.9 and the depth-\(q_0\) count in Lemma 4.5 force

\[
                    \sum_iB_i=\Omega_A\!\left({rW\over q_0}\right).
                                                               \tag{6.5}
\]

If the higher-depth connector windows of each round are charged
separately as loss, (6.4) gives aggregate charge

\[
       \Omega_A\!\left({H^2\over r}\sum_iB_i\right)
       =\Omega_A\!\left({WH^2\over q_0}\right).       \tag{6.6}
\]

In the coefficient-one regime

\[
                 {H\over\sqrt m}\longrightarrow\infty,
                 \qquad r=o(m),                       \tag{6.7}
\]

one has \(H^2/q_0\to\infty\).  Thus separate elementary rounds exceed
the entire \(O(W)\) error budget by an unbounded factor.  The estimate is
stronger than the old \(WH^2/r\) warning because the full internal-atlas
cut forces \(\Omega(r/q_0)\) crossing-axis multiplicity.

The only possible use of these windows is as a coordinated vertical
braid: their higher-depth derivatives must cancel between hierarchy rounds
or must directly transport the corresponding higher-depth defects.

## 6A. Exact common-depth scheduling of dense crossing axes

The chronological part of the dense-axis problem has an exact
one-dimensional form.  On an isometric \(C_{2r}\), write the cyclic
direction word as \(\pi\pi\), and let

\[
                         D\subseteq\mathbb Z/r\mathbb Z             \tag{6.8}
\]

be the positions in the first half occupied by cross-quartet directions.
For \(q<r\), define the start set

\[
       N_q(D)=D-\{0,1,\ldots,q-1\}\subseteq\mathbb Z/r\mathbb Z.    \tag{6.9}
\]

A depth-\(q\) window contains a crossing axis exactly when its start
modulo \(r\) belongs to \(N_q(D)\).

### Theorem 6.3 (gap formula and the all-depth envelope)

Suppose \(D\ne\varnothing\), and let \(g_1,\ldots,g_s\) be the positive
cyclic gaps between consecutive elements of \(D\), so
\(\sum_i g_i=r\) and \(s=|D|\).  Then

\[
                    |N_q(D)|=\sum_{i=1}^s\min(q,g_i).              \tag{6.10}
\]

Consequently

\[
 |N_{q+1}(D)|-|N_q(D)|=|\{i:g_i>q\}|,                             \tag{6.11}
\]

so the eligible-window count is nondecreasing and discretely concave in
\(q\).  Its complete protected-depth ledger is

\[
 \sum_{q=1}^H|N_q(D)|
   =\sum_{i=1}^s
     \begin{cases}
       H(H+1)/2,&g_i\ge H,\\
       g_iH-g_i(g_i-1)/2,&g_i<H .
     \end{cases}                                                   \tag{6.12}
\]

#### Proof

The crossing position ending a gap of length \(g_i\) covers the last
\(\min(q,g_i)\) start residues in that gap.  These pieces are disjoint
and exhaust \(N_q(D)\), proving (6.10).  Taking first differences gives
(6.11), and summing \(\min(q,g_i)\) over \(1\le q\le H\) gives
(6.12). \(\square\)

This exposes both the obstruction and the available repair.  The exact
overlap loss from the union bound is

\[
              qs-|N_q(D)|=\sum_{i=1}^s(q-g_i)_+.                  \tag{6.13}
\]

Thus a near-minimal family with \(s\asymp r/q_0\) can deliver a constant
fraction of the depth-\(q_0\) starts only when its crossing axes are not
clustered: the total short-gap deficit in (6.13) must be \(O(r)\), and
near equality requires it to be \(o(r)\).  Conversely, placing \(s\)
axes as evenly as possible makes all gaps equal to
\(\lfloor r/s\rfloor\) or \(\lceil r/s\rceil\) and gives

\[
             {|N_q(D)|\over r}
                  =\min\!\left(1,{sq\over r}\right)+O\!\left({s\over r}\right).
                                                                    \tag{6.14}
\]

Hence the scalar chronological capacity does *not* require a separate
axis family at every depth.  A single evenly spaced family with

\[
                         s=\Theta(r/\sqrt m)                       \tag{6.15}
\]

already gives positive start density at every \(q=A\sqrt m\), and,
once \(q\) exceeds the largest gap, every window contains a crossing
axis.  Formula (6.12), rather than a sum of independently paid
depthwise rounds, is the correct common-depth ledger.

This is only a support-level scheduling result.  It does not construct a
legal owner factor with the prescribed dense set \(D\), assign the
three-state shores without violating (4.8), or show that the resulting
literal targets fill the Hall-deficient profiles.  Those three demands
are now the substantive part of HCRT.

## 7. Exact remaining HCRT statement

Depth one is now separated into lattice, cone, and chronology.

### Closed at depth one

* The unrestricted integral derivative lattice is (0.2).
* Its only real invariants are total mass and the coupled coordinate point
  margins (0.3).
* Changing quartet pairings realizes that lattice up to one parity bit per
  polynomially many local generator types, hence up to \(o(W)\) literal
  repair.

### Closed on the owner and abstract-support side

* The independently audited rank-twisted macroblock construction tiles all
  but \(2^{m+o(m)}\) owners by exact \(Q_r\) packets with
  \(s(P)=r\) cross-half axes.
* Selector-fibre complete batching, with
  \(t=\log_2\binom{S-t}{r}+r+\log_2(r!)+\log_2H+\omega(1)=o(m)\),
  gives exact equal aggregate multiplicity to every ordered, signed
  nested deletion flag through depth \(H\), outside \(o(W/H)\) owners.
  Thus abstract support Poisson holes are not an obstruction.

### Not closed by the lattice theorem

* A signed lattice decomposition need not give a path through nonnegative
  packet tilings.
* The two-port q=1 factor is not automatically the certified all-depth
  context-array factor after reconnection.
* Independent depthwise corrections can violate the common run line
  (5.1).
* The full internal quartet atlas itself has a linear Gaussian Hall
  deficit, forcing average crossing multiplicity
  \(\Omega_A(r/q)\).
* The dense rank-twisted packets meet this multiplicity, but their exact
  lower compatibility is the coefficient

  \[
  [z^q]\prod_j\sum_{\ell=0}^d
      2^\ell\binom{e_{t_j+\ell}(T_j)}{\ell}z^\ell,
  \]

  with the complementary full-edge formula on the upper side.  No Hall
  cut theorem for the unions of compatible sources is known.
* Complete selector batching balances flags only after summing over
  selector labels.  Since the selector bits are frozen and literally
  decoded from targets inside a status cell, each label receives one
  active-set/conjugate column rather than the convex average.  This is an
  integral grouping obstruction.
* The exact grouped relaxation is a Minkowski sum of fibre configuration
  polytopes intersected with one translated hypersimplex for each sign
  and depth.  Its weighted Hall dual is known explicitly, including all
  quota resets, but no integer-decomposition theorem or
  \(\Omega(W)\) dual witness is currently proved.
* Saturated \(M\)-convex fibre option sets would make that dual integrally
  sufficient.  The actual atlas fails the exchange axiom: at depth one
  its direction-count projection is
  \((|V_f|/r)\mathbf1_A\), so a unit exchange leaves the legal set.
  Its primitive support-changing scale is \(2|V_f|/r\), ruling out
  bounded local-exchange/Graver rounding.
* Pairing fibres into exact \(Q_{r+1}\) slabs repairs the *normalized*
  direction projection: its \(r+1\) resolutions are the bases of
  \(U_{r,r+1}\), with zero owner interface and \(O(W/r)=o(W)\)
  direction-rounding cost.  Literal counts nevertheless remain divisible
  by \(2^r/r\), and cubical tiling differences by \(2^{r+1}/r\);
  higher target-labelled cancellation is not supplied.
* At depth \(q\), \(Q_{r+k}\) slab resolutions again give a normalized
  \(U_{r,r+k}\) IDP.  Literal face images retain antipodal pairing, even
  support multiplicity, exact active-direction degree \(q2^r/r\), lower/
  upper equality under empty/full identification, and one common nested
  flag lift.  Separate direction rounding costs \(WH^2/r\), so the
  normalized IDP does not close the all-depth target problem.

The next theorem must therefore be stronger than surjectivity of a signed
lattice:

> Prove the selector-conditioned Hall inequalities for the exact
> rank-twisted compatibility graph, and integralize the choice of one
> active \(r\)-set and one affine compiler conjugate per selector fibre.
> The resulting lower and upper literal loads must use one chronology,
> obey the common run vector, and respect the local \(L,C,S\) triangular
> cone.  Equivalently, lift the already exact complete-design flag
> marginals to a target-labelled grouped flow.

That is the precise multidepth HCRT gate.  A real-span calculation, a
separate Smith calculation at each depth, or repetition of the depth-one
port switch does not prove it.
