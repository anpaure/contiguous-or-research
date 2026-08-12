# Alternating exchanges in the calibrated packet-owner hypergraph

Date: 2026-07-25

Pure mathematics only. No computation, search, solver, web input, or
probabilistic black box is used.

## 0. Verdict

There is a clean signed local-to-global theorem, but the naive positive
alternating-cycle theorem is false.

Let

\[
M=m+H,
\qquad
N_H=\binom{2m}{m-H},
\qquad
N_H=(1+o(1))\frac Wm
\tag{0.1}
\]

at calibrated depth.  Write \(B_sP\) for the incidence vector of the
\(M\) cyclic \(s\)-intervals exposed by a directed packet \(P=(U,\pi)\),
and write \(TP=e_U\) for its top tag.

A signed packet vector \(z\) is an owner-preserving top trade when

\[
Tz=0,
\qquad
B_mz=0.
\tag{0.2}
\]

The conclusions are as follows.

1. **Signed band generation succeeds.**  For
   \(1\le q\le Q\le H-2\), owner-preserving top trades generate,
   independently at every rank \(m-q\) and \(m+q\), the complete lattice
   \[
   \ker_{\mathbb Z}A_{m-q}
   \quad\text{and}\quad
   \ker_{\mathbb Z}A_{m+q}.
   \tag{0.3}
   \]
   The generators are the exact four-order rank selectors.
2. **One alternating owner cycle is not normally a packet trade.**  For
   two exact packet matchings with the same owner set, contract the old and
   new packet at each top.  Every owner gives a directed edge from its old
   top to its new top, producing an \(M\)-in/\(M\)-out Eulerian multigraph.
   A subset of tops is an owner-preserving subtrade if and only if it is a
   union of weak connected components of this full multigraph.  A directed
   cycle from an Euler decomposition usually has other owner edges leaving
   its vertices and therefore has a nonzero, explicitly computable owner
   boundary.
3. **Small squarefree trades are rigid.**  If an active top has a
   coordinate contained in no other active top, its old and new packets are
   the same cyclic packet up to reversal and have identical shadows at
   every rank.  Peeling such tops shows that every nontrivial exchange is
   supported in the coordinate 2-core of its active top family.  In
   particular, there is no nontrivial two-top squarefree exchange.
4. **Adjacent rectangles have inadequate throughput at bounded
   congestion.**  Each one changes only four rank-\(r\) targets.  If every
   top supports at most \(\kappa=O(1)\) such atoms, their total rank-\(r\)
   variation is
   \[
   O(\kappa N_H)=O(W/m)=o(W).
   \tag{0.4}
   \]
   Correcting a macroscopic shallow deficit therefore requires long
   owner-preserving exchanges with \(\Theta(M)\) useful shadow change per
   active top, or else top congestion \(\Omega(m)\).
5. **Coordinate automorphisms give positive near-exchanges for free.**
   From any owner near-transversal \(\mathcal F\), every coordinate
   permutation \(g\) gives a second valid decomposition \(\mathcal F^g\)
   with only \(o(W)\) owner discrepancy.  Weak-component hybrids have
   congestion one; a general hybrid has an exact owner-boundary
   counterterm whose norm is bounded by its matched-overlay edge boundary.
   For involutive \(g\), component
   directions occur in the exact pairs \(z_{gC}=-gz_C\).

Thus alternating exchanges identify a plausible positive route, but only
after replacing “decompose the overlay into cycles” by a much stronger
packet-cycle reassembly theorem.  The exact remaining lemma is a
bounded-congestion construction or automorphism sparse-cut selection of
long exchanges inside the top-family 2-core.  The signed lattice, parity,
owner toll, and shallow-rank decoupling are already settled.

## 1. Packet maps and automatic margin invariants

Let \(\mathcal P\) be the set of directed top packets.  A packet
\(P=(U,\pi)\), with \(|U|=M\), has \(M\) distinct cyclic intervals at each
proper length \(1\le s<M\).  Define

\[
B_s:\mathbb Z^{\mathcal P}
\longrightarrow
\mathbb Z^{\binom{[2m]}s}
\tag{1.1}
\]

by interval incidence and

\[
T:\mathbb Z^{\mathcal P}
\longrightarrow
\mathbb Z^{\binom{[2m]}M}
\tag{1.2}
\]

by top incidence.

Let

\[
A_s:\mathbb Z^{\binom{[2m]}s}
\longrightarrow\mathbb Z^{[2m]}
\tag{1.3}
\]

be point-versus-\(s\)-set incidence.

### Lemma 1.1 (point margins factor through the top)

For every packet \(P=(U,\pi)\) and \(1\le s<M\),

\[
A_sB_sP=s\,\mathbf1_U.
\tag{1.4}
\]

Consequently every top-preserving trade satisfies

\[
Tz=0
\quad\Longrightarrow\quad
A_sB_sz=0
\tag{1.5}
\]

at every proper rank.

#### Proof

Every coordinate of \(U\) occurs in exactly \(s\) of the \(M\) cyclic
\(s\)-intervals, and a coordinate outside \(U\) occurs in none.  Summing
over the coefficients of \(z\) proves (1.5).  \(\square\)

Thus zero point margins are a necessary invariant of every
owner-preserving exchange.  Literal repair may absorb a total \(o(W)\)
margin error, but no exact exchange can change it.

## 2. The signed local-to-global theorem

Define the trade lattice

\[
\mathcal K
=\ker_{\mathbb Z}T\cap\ker_{\mathbb Z}B_m.
\tag{2.1}
\]

Assume

\[
1\le Q\le H-2,
\qquad
m>H+2Q.
\tag{2.2}
\]

These inequalities hold throughout the calibrated regime for every
\(Q\le H-2\) and sufficiently large \(m\).

### Theorem 2.1 (independent signed generation of the hard band)

The hard-band image map

\[
\Phi_Q:\mathcal K\longrightarrow
\bigoplus_{q=1}^{Q}
\left(
\ker_{\mathbb Z}A_{m-q}
\oplus
\ker_{\mathbb Z}A_{m+q}
\right)
\tag{2.3}
\]

is surjective.

More explicitly, for arbitrary vectors

\[
f_{m-q}\in\ker_{\mathbb Z}A_{m-q},
\qquad
f_{m+q}\in\ker_{\mathbb Z}A_{m+q},
\tag{2.4}
\]

there is \(z\in\mathcal K\) such that

\[
B_rz=f_r
\tag{2.5}
\]

at every prescribed hard-band rank and \(B_sz=0\) at every other
hard-band rank, including \(s=m\).

#### Proof

At rank \(r\), the elementary squares

\[
g(K;a,b;c,d)
=e_{Kac}-e_{Kbc}-e_{Kad}+e_{Kbd},
\qquad |K|=r-2,
\tag{2.6}
\]

generate \(\ker_{\mathbb Z}A_r\).  Since \(r+2\le M\) for every upper
rank in (2.2), and trivially for every lower rank, the support of each
square lies in a containing top \(U\).

Inside that top choose two disjoint adjacent swaps whose cut separation is
\(r\).  The four-order rectangle

\[
z_{U,r}
=e_{\pi_{10}}+e_{\pi_{01}}
-e_{\pi_{00}}-e_{\pi_{11}}
\tag{2.7}
\]

has zero top incidence.  Its interval incidence is zero at every length
except \(r\) and \(M-r\), and its rank-\(r\) image is (2.6), up to sign.
The complementary exceptional rank \(M-r\) lies below the hard band by
(2.2).  Since \(r\ne m\), the atom also satisfies \(B_mz_{U,r}=0\).

Decompose every vector in (2.4) into elementary squares, lift each square
as in (2.7), and sum.  Different target ranks do not interfere.  This
gives (2.5) and proves surjectivity.  \(\square\)

### Corollary 2.2 (no signed lattice or parity obstruction)

At each supported rank the exact exchange image lattice is

\[
\ker_{\mathbb Z}A_r,
\tag{2.8}
\]

and the unrestricted real cone generated by both orientations is

\[
\ker_{\mathbb R}A_r.
\tag{2.9}
\]

Hence an obstruction to the alternating-exchange route must come from
positive support, congestion, or packet reassembly.  It cannot come from a
new shallow incidence parity.

## 3. Exact packet matchings and their owner overlay

The positive problem is different.  Suppose that

\[
\mathcal F^-=\{P_U^-:U\in\mathcal T_0\},
\qquad
\mathcal F^+=\{P_U^+:U\in\mathcal T_0\}
\tag{3.1}
\]

are two families with one packet at each top in the same top set
\(\mathcal T_0\).  Assume each family is owner-disjoint and that the two
families cover exactly the same owner set \(\mathcal O\).  Thus both are
exact packet matchings on \(\mathcal O\).

Construct the directed owner-overlay multigraph \(G\) on vertex set
\(\mathcal T_0\) as follows.  For each owner \(X\in\mathcal O\), there are
unique tops \(U,V\) such that

\[
X\in B_mP_U^-,
\qquad
X\in B_mP_V^+.
\tag{3.2}
\]

Insert one directed edge

\[
U\xrightarrow{\,X\,}V.
\tag{3.3}
\]

Loops and parallel edges are retained.

### Lemma 3.1 (the overlay is Eulerian)

Every vertex of \(G\) has outdegree \(M\) and indegree \(M\).

#### Proof

The old packet at \(U\) contains exactly \(M\) owners, giving \(M\)
outgoing edges.  The new packet at \(U\) contains exactly \(M\) owners,
giving \(M\) incoming edges.  \(\square\)

The directed edges can therefore be decomposed into directed cycles.
This ordinary Euler decomposition is not a decomposition into packet
trades.

### Theorem 3.2 (component-closure theorem)

For \(A\subseteq\mathcal T_0\), define the top-balanced packet vector

\[
z_A=\sum_{U\in A}(e_{P_U^+}-e_{P_U^-}).
\tag{3.4}
\]

Then

\[
\boxed{
B_mz_A
=\sum_{U\xrightarrow{X}V}
\bigl(\mathbf1_A(V)-\mathbf1_A(U)\bigr)e_X.
}
\tag{3.5}
\]

Consequently the following are equivalent.

1. \(z_A\) is owner preserving.
2. No nonloop owner edge of \(G\) crosses between \(A\) and its complement.
3. \(A\) is a union of weak connected components of \(G\).

#### Proof

The coefficient of an owner \(X\), carried by the edge
\(U\xrightarrow{X}V\), is \(+1\) if its new top \(V\) is selected and
\(-1\) if its old top \(U\) is selected.  This is exactly (3.5).  Since
every owner labels a unique edge, the coefficient vanishes for every
\(X\) precisely when the two endpoints of every edge lie on the same side
of the cut.  That is equivalent to component closure.  \(\square\)

### 3.1 The exact alternating-cycle counterterm

Let \(C\) be one directed cycle in an Euler decomposition of \(G\), and let
\(A=V(C)\).  The cycle edges themselves cancel in (3.5), but all other
owner edges incident with \(A\) remain.  The counterterm is

\[
E_A
=\sum_{\substack{U\xrightarrow{X}V\\
                  |\{U,V\}\cap A|=1}}
\bigl(\mathbf1_A(V)-\mathbf1_A(U)\bigr)e_X.
\tag{3.6}
\]

Thus a single alternating cycle is a packet trade only if its vertex set is
closed under all \(M\) owner incidences at every packet.  Factoring the
\(M\)-regular bipartite old/new overlap graph into perfect matchings merely
produces \(M\) superposed cycle decompositions; a cycle in one factor is
not closed under the other \(M-1\) factors.

This is the exact failure of the naive local-to-global argument.  Packet
atomicity couples all \(M\) owner edges.

### 3.2 Exact component-switch reduction

Let

\[
\mathcal C(G)=\{C_1,\ldots,C_t\}
\tag{3.7}
\]

be the weak connected components of the full owner overlay, and put

\[
z_j=\sum_{U\in C_j}(e_{P_U^+}-e_{P_U^-}).
\tag{3.8}
\]

### Proposition 3.3 (independent positive component switches)

Every \(z_j\) is an owner-preserving top trade.  Starting from
\(\mathcal F^-\), for an arbitrary index set \(J\subseteq[t]\), replace
the old packet by the new packet at precisely the tops in
\(\bigcup_{j\in J}C_j\).  The result:

1. has one packet at every original top;
2. covers exactly the same owner set \(\mathcal O\);
3. uses every top in at most one switch; and
4. has rank-\(s\) incidence change
   \[
   \sum_{j\in J}B_sz_j.
   \tag{3.9}
   \]

Conversely, every squarefree owner-preserving mixture of the two
decompositions is obtained by choosing a union of these components.

#### Proof

The first assertion is Theorem 3.2 applied to one component.  Disjoint
components have disjoint top sets, so their switches can be made
simultaneously and the incidence changes add.  The converse is the
component-closure direction of Theorem 3.2.  \(\square\)

This is an exact local-to-global reduction with top congestion one.  Its
usefulness depends entirely on the component discrepancy vectors

\[
v_j^{(s)}=B_sz_j.
\tag{3.10}
\]

If \(G\) is connected, there is only one binary direction.  If it has many
components but every \(v_j^{(s)}\) is small or similarly oriented, there is
still inadequate correction power.  A successful construction must design
the second packet decomposition so that its overlay has many separated
long components and the vectors (3.10) have sufficiently diverse
multirank signs.

### 3.3 Exact collision-energy formulation

At every proper packet rank \(s\), any one-packet-per-top selection has the
same total occurrence count

\[
L=MN_H.
\tag{3.11}
\]

Let \(\mu_s(R)\) be the load of a rank-\(s\) target \(R\), and define its
collision count

\[
\mathcal E_s(\mu)
=\sum_R(\mu_s(R)-1)_+.
\tag{3.12}
\]

If \(h_s\) is the number of uncovered targets and \(N_s\) is the size of
the rank, then

\[
\boxed{
h_s=N_s-L+\mathcal E_s(\mu).
}
\tag{3.13}
\]

Equivalently,

\[
h_s-(N_s-L)_+
=\mathcal E_s(\mu)-(L-N_s)_+.
\tag{3.14}
\]

Thus flag-hole control is exactly excess-collision control; the scalar
deficiency or surplus forced by \(N_s-L\) is already accounted for.

For one overlay component \(C_j\), the exact collision change is

\[
\Delta_j\mathcal E_s(\mu)
=\sum_R
\left[
(\mu_s(R)+v_j^{(s)}(R)-1)_+
-(\mu_s(R)-1)_+
\right].
\tag{3.15}
\]

There is no linearization error in (3.15).  In the unit-occurrence special
case, adding an occurrence to a hole decreases the hole count by one,
whereas deleting the last occurrence of a singleton creates one hole;
changes at already occupied or multiply occupied targets contribute only
through these threshold crossings.

Consequently the positive local-to-global problem can be stated without an
arbitrary target vector: choose component switches so that the sum over
the controlled ranks of the excess energies in (3.14) is \(o(W)\).  This
is exactly equivalent to the aggregate flag-hole requirement because the
calibrated scalar deficiencies already sum to \(o(W)\).

### 3.4 Owner-successor alternating cycles

There is a second alternating structure, distinct from the top owner
overlay.  An exact packet decomposition \(\mathcal F\) defines a successor
permutation

\[
\sigma_{\mathcal F}:\mathcal O\longrightarrow\mathcal O
\tag{3.16}
\]

by sending every owner window to the next window in its directed promotion
packet.

For an owner \(X\), the lower and upper flags have the exact path formulas

\[
L_q^{\mathcal F}(X)
=\bigcap_{i=0}^{q}\sigma_{\mathcal F}^{\,i}(X),
\tag{3.17}
\]

\[
U_q^{\mathcal F}(X)
=\bigcup_{i=0}^{q}\sigma_{\mathcal F}^{\,-i}(X).
\tag{3.18}
\]

Indeed, for \(X=X_t\), the intersection in (3.17) is
\(\{u_{t+q},\ldots,u_{t+m-1}\}\), and the union in (3.18) is
\(\{u_{t-q},\ldots,u_{t+m-1}\}\).

For two decompositions \(\mathcal F^-,\mathcal F^+\), split every owner
into a tail copy and a head copy.  The edges

\[
X_{\mathrm L}\sigma_-(X)_{\mathrm R}
\quad\text{and}\quad
X_{\mathrm L}\sigma_+(X)_{\mathrm R}
\tag{3.19}
\]

are two perfect matchings.  After common edges are removed, their union is
a disjoint family of even alternating cycles.  Switching either matching
on any collection of those cycles gives another successor permutation on
the same owner set.

### Lemma 3.4 (exact shallow-path locality)

Let \(\sigma\) and \(\sigma'\) be two successor permutations on the same
owner set, and put

\[
D=\{X:\sigma'(X)\ne\sigma(X)\}.
\tag{3.20}
\]

At lower depth \(q\), a start \(X\) can change only if

\[
\{\sigma^i(X):0\le i<q\}\cap D\ne\varnothing.
\tag{3.21}
\]

Consequently at most \(q|D|\) lower starts change and

\[
\|B_{m-q}(\sigma')-B_{m-q}(\sigma)\|_1
\le2q|D|.
\tag{3.22}
\]

The upper analogue holds with inverse successors, again with at most
\(q|D|\) changed starts and the same \(2q|D|\) variation bound.

#### Proof

If the first \(q\) old successor arcs from \(X\) have tails outside \(D\),
then \(\sigma'\) agrees with \(\sigma\) along the entire path, so the
intersection (3.17) is unchanged.  The possible old starts lie in

\[
\bigcup_{i=0}^{q-1}\sigma^{-i}(D),
\]

whose size is at most \(q|D|\).  Each changed occurrence deletes at most
one old target and inserts at most one new target, proving (3.22).  Apply
the same argument to \(\sigma^{-1},(\sigma')^{-1}\) and (3.18) for the
upper claim.  \(\square\)

At depth one this says exactly that lower flags are intersection colors
and upper flags are union colors of promotion edges.  At larger depths the
flags are \(q\)-path statistics, and the discrepancy is confined to
\(q\)-neighborhoods of the switched successor arcs.

The alternating cycles of (3.19) preserve owner vertices but need not
preserve packet validity.  A hybrid successor permutation may join pieces
from different tops into a cycle whose owners do not have one common
\(M\)-set union, or may split the required \(M\)-cycle at a top.  Therefore
an alternating successor cycle is a legal packet exchange only when the
hybrid permutation again decomposes into one directed cyclic-window packet
at every top.  This is the exact top-reassembly counterterm left out by an
owner-only successor switch.

The full overlay-component switches of Proposition 3.3 satisfy this
condition automatically because they choose whole old or whole new packets
at every top.  The role of (3.17)--(3.22) is to expose their shallow
discrepancy and its boundary neighborhoods, not to bypass component
closure.

For truncated carrier-rotor paths, these path formulas become even more
literal; see `MATH_ATTACK_TRUNCATED_CARRIER_ROTOR_ACD_20260725.md`. The
hidden rotor choice made at time \(t\) is forced by the owner departure at
time \(t+Q\). Hence two lifts of the same directed owner sequence differ in
only the endpoint collars and have \(O(Q^2)\) total band discrepancy. At
depth one, \(\Theta(M)\) movement per carrier requires rethreading
\(\Theta(M)\) owner-successor arcs. This rules out local rotor branching as
a substitute for the long exchange component required here.

## 4. A reconstruction lemma from one private coordinate

The overlay obstruction has a useful geometric strengthening.

Fix a cyclic packet \(P=(U,\pi)\) and a coordinate \(a\in U\).  Let

\[
\mathcal S_a(P)
=\{X\in B_mP:a\in X\}.
\tag{4.1}
\]

Exactly \(m\) packet owners contain \(a\).

### Lemma 4.1 (private-star reconstruction)

Assume \(2\le H<m\).  The family \(\mathcal S_a(P)\) determines the cyclic
order \(\pi\) up to rotation and reversal.  In particular, if

\[
\mathcal S_a(P)=\mathcal S_a(P'),
\tag{4.2}
\]

then

\[
B_sP=B_sP'
\qquad(1\le s<M).
\tag{4.3}
\]

#### Proof

Place \(a\) at phase \(0\).  The \(m\) windows containing \(a\) have starts

\[
-m+1,-m+2,\ldots,0.
\tag{4.4}
\]

Join two members of \(\mathcal S_a(P)\) when their symmetric difference
has size two.  Consecutive starts in (4.4) are joined.  No other pair is
joined: after taking complements, this says that two cyclic
\(H\)-intervals with \(H\ge2\) differ in one point only when their starts
are cyclically adjacent.  The endpoints in (4.4) are separated in the
other cyclic direction by \(H+1\ge3\).  Hence the resulting graph is a
path on the \(m\) windows.

Its order is determined up to reversal.  Along the path, every consecutive
difference identifies the label leaving the window and the label entering
it.  These \(m-1\) transitions, together with the common label \(a\),
recover the labels and their cyclic positions.  They cover the whole top
because

\[
2m-1\ge m+H=M.
\tag{4.5}
\]

Thus the cyclic order is recovered up to reversal.  Reversal preserves the
unlabelled family of cyclic intervals at every length, proving (4.3).
\(\square\)

### Theorem 4.2 (private-coordinate rigidity)

Consider a squarefree top-balanced owner trade with one old and one new
packet at each active top.  If an active top \(U\) contains a coordinate

\[
a\in U\setminus\bigcup_{V\ne U}V
\tag{4.6}
\]

private to \(U\) among the active tops, then the old and new packets at
\(U\) have identical interval incidence at every rank.  The top is
shadow-inert and can be deleted from the trade.

#### Proof

Every old owner at \(U\) containing \(a\) must be supplied positively by a
packet whose top also contains \(a\).  By privacy, only the new packet at
\(U\) can supply it.  Owner balance and the fact that both private stars
have size \(m\) give equality of the two families in (4.2).  Lemma 4.1
then gives (4.3).  \(\square\)

Iteratively delete shadow-inert tops having a private coordinate.

### Corollary 4.3 (coordinate 2-core condition)

The support of every reduced nontrivial squarefree owner-preserving trade
is a family of tops in which every coordinate occurring in the union occurs
in at least two active tops.

In particular, a trade on two distinct tops is trivial, since each of the
two equal-size distinct tops has a private coordinate.  A trade on one top
is also trivial: equality of the whole middle packet reconstructs the
cyclic order up to reversal.

This 2-core condition is necessary, not sufficient.  It sharply excludes
tree-like attempts to propagate an exchange through successively attached
tops: every leaf carrying a new coordinate peels off.

There is also a quantitative clustering consequence.  If a reduced
component contains \(k\) tops, and \(d_x\) is the number of those tops
containing coordinate \(x\), then \(d_x\ge2\) on the union and

\[
\left|\bigcup_UU\right|
\le\frac{kM}{2}.
\tag{4.7}
\]

Moreover,

\[
\sum_{\{U,V\}}|U\cap V|
=\sum_x\binom{d_x}{2}
\ge\frac12\sum_xd_x
=\frac{kM}{2}.
\tag{4.8}
\]

Hence some pair of active tops has intersection at least

\[
\frac{M}{k-1}.
\tag{4.9}
\]

Every bounded-size nontrivial exchange is therefore supported on a
strongly clustered top family.  This does not construct the exchange, but
it rules out a bounded trade whose tops are mutually diffuse.

## 5. Pairwise overlap and forced nonlocality

Let \(P=(U,\pi)\) and \(P'=(V,\rho)\) be packets on distinct tops.  Put

\[
d=|U\setminus V|=|V\setminus U|.
\tag{5.1}
\]

### Lemma 5.1 (distinct-top packet overlap)

If \(d>H\), the two packets have no common owner.  If \(1\le d\le H\),
then

\[
\boxed{
|B_mP\cap B_mP'|\le H.
}
\tag{5.2}
\]

#### Proof

A common owner \(X\) must lie in \(U\cap V\).  Equivalently, the
complementary \(H\)-interval \(U\setminus X\) in the first packet must
contain the nonempty set \(U\setminus V\).  Fix one point of
\(U\setminus V\).  Exactly \(H\) cyclic \(H\)-intervals of \(U\) contain
that point, so there are at most \(H\) possible owners \(X\).  If \(d>H\),
no \(H\)-set can contain \(U\setminus V\).  \(\square\)

In the exact overlay \(G\), a pair of distinct old/new tops therefore
carries at most \(H\) parallel owner edges.  If the old packet at \(U\)
retains \(\ell_U\) owners in the new packet at the same top, then the
number of distinct new-top neighbors receiving moved owners from \(U\) is
at least

\[
\frac{M-\ell_U}{H}.
\tag{5.3}
\]

Also, every nonloop overlay edge joins tops at top-layer Johnson distance
at most \(H\).  Thus a connected reassembly component is assembled from
locally neighboring tops, even though the component itself may have to be
large.

Thus an exchange which moves a positive fraction of every packet's owners
has local overlay degree

\[
\Omega(M/H)=\Omega(m/H).
\tag{5.4}
\]

At calibrated depth this tends to infinity.  Long exchanges are therefore
genuinely multi-top objects; they cannot be assembled from a bounded-degree
chain of pairwise packet replacements.

## 6. Throughput audit for bounded congestion

Theorem 2.1 proves span, but its local rectangle atoms are too sparse for
macroscopic positive repair.

For a rank-selecting rectangle \(z_{U,r}\),

\[
\|B_rz_{U,r}\|_1=4.
\tag{6.1}
\]

Suppose a collection of such atoms uses every top in at most \(\kappa\)
atoms.  Then the number of atoms is at most \(\kappa N_H\), and hence

\[
\left\|
B_r\sum_j z_j
\right\|_1
\le4\kappa N_H
=(4+o(1))\frac{\kappa W}{m}.
\tag{6.2}
\]

### Proposition 6.1 (local-selector capacity barrier)

If \(\kappa=O(1)\), bounded-congestion adjacent rectangles can change only
\(o(W)\) rank-\(r\) occurrences.  Any correction of total variation
\(\Theta(W)\) requires

\[
\kappa=\Omega(m)
\tag{6.3}
\]

when built solely from these atoms.

This does not contradict the desired bounded-congestion route.  Replacing
one whole packet order by another can change at most \(2M\) interval
occurrences at a fixed rank.  A squarefree exchange on
\(\Theta(N_H)\) active tops can therefore have \(\Theta(MN_H)=\Theta(W)\)
throughput with congestion one.  What is necessary is that the owner
cancellations package \(\Theta(M)\) coherently directed elementary square
effects per active top.  Alternating exchange must be long both in owner
space and in shallow-shadow effect.

## 7. Exact reassembly formulation

An exact owner matching supplies a set

\[
\mathcal O\subseteq\binom{[2m]}m,
\qquad
|\mathcal O|=MN_H,
\tag{7.1}
\]

partitioned into \(N_H\) tagged packet cycles:

\[
\mathcal O=\bigsqcup_U B_mP_U.
\tag{7.2}
\]

An owner-preserving squarefree exchange is exactly a second partition

\[
\mathcal O=\bigsqcup_U B_mP'_U
\tag{7.3}
\]

such that \(P'_U\) is a cyclic packet on the same top \(U\).  Thus the
positive problem is not merely a matching symmetric-difference problem.
It is connectivity of the space of tagged packet-cycle decompositions of
one fixed owner set.

The owner overlay records how the blocks of (7.2) are cut and reassembled
in (7.3).  Theorem 3.2 says that its true exchange atoms are connected
components, not individual alternating cycles.  Corollary 4.3 says every
nontrivial component has a coordinate 2-core.  Lemma 5.1 says components
which move many owners have growing local degree.

### 7.1 Automorphism-produced near-exchanges

Exact equality of the two owner sets is stronger than the coefficient-one
compiler needs.  Near-full owner coverage supplies a canonical second
decomposition with only \(o(W)\) owner error.

Let \(\mathcal F=\{P_U\}\) be any one-packet-per-top family.  Its owner
load vector is

\[
\mu=B_m\mathcal F,
\qquad
\sum_X\mu(X)=L=MN_H.
\tag{7.4}
\]

Let

\[
C_0=\sum_X(\mu(X)-1)_+
\tag{7.5}
\]

be its owner collision.  For a coordinate permutation \(g\in S_{2m}\),
define the reindexed packet family

\[
\mathcal F^{g}
=\{P_U^{g}:U\in\tbinom{[2m]}M\},
\qquad
P_U^{g}=gP_{g^{-1}U}.
\tag{7.6}
\]

This again selects exactly one valid packet at every top, and at every
rank

\[
B_s\mathcal F^{g}=g(B_s\mathcal F).
\tag{7.7}
\]

### Theorem 7.1 (automorphism near-exchange)

For every coordinate permutation \(g\),

\[
\boxed{
\|g\mu-\mu\|_1
\le2(W-L+2C_0).
}
\tag{7.8}
\]

In particular, if \(W-L=o(W)\) and \(C_0=o(W)\), then
\(\mathcal F\) and \(\mathcal F^g\) differ by only \(o(W)\) owner
occurrences.

Match as many old and new occurrences of every owner as possible, and
form the directed top overlay from those matched occurrences.  For an
arbitrary union \(A\) of weak overlay components, use \(P_U^g\) at
\(U\in A\) and \(P_U\) outside \(A\).  Every such hybrid:

1. contains one valid packet at every top;
2. uses each top in at most one component switch;
3. has owner load \(\mu_A\) satisfying
   \[
   \|\mu_A-\mu\|_1\le2(W-L+2C_0)=o(W);
   \tag{7.9}
   \]
4. has owner collision and owner-hole count \(o(W)\).

More generally, for an arbitrary top set \(A\), let
\(\partial_GA\) be the matched owner edges with exactly one endpoint in
\(A\).  There is an unmatched-stub vector \(u_A\) such that

\[
\mu_A-\mu
=\sum_{U\xrightarrow{X}V}
\bigl(\mathbf1_A(V)-\mathbf1_A(U)\bigr)e_X+u_A,
\qquad
\|u_A\|_1\le2(W-L+2C_0).
\tag{7.10a}
\]

Thus the same hybrid satisfies

\[
\boxed{
\|\mu_A-\mu\|_1
\le |\partial_GA|+2(W-L+2C_0).
}
\tag{7.10}
\]

#### Proof

The all-ones owner vector \(\mathbf1\) satisfies

\[
\|\mu-\mathbf1\|_1
=\bigl(W-|\operatorname{supp}\mu|\bigr)+C_0
=W-L+2C_0.
\tag{7.11}
\]

Coordinate permutation preserves the norm and fixes \(\mathbf1\).
Therefore

\[
\|g\mu-\mu\|_1
\le\|g\mu-\mathbf1\|_1+\|\mu-\mathbf1\|_1
=2(W-L+2C_0),
\]

proving (7.8).

After the maximal occurrence matching, the total number of unmatched old
and new stubs is exactly \(\|g\mu-\mu\|_1\).  A union of weak components
has no matched owner edge crossing its top boundary.  Hence every matched
occurrence cancels in the hybrid difference, and only unmatched stubs
contribute.  This proves (7.9).  For arbitrary \(A\), every internal
matched edge still cancels and each boundary edge contributes one unit,
giving (7.10a) and hence (7.10).  Collision energy is 1-Lipschitz in
\(\ell^1\), so it remains \(o(W)\) when \(|\partial_GA|=o(W)\); the exact
owner identity

\[
h_m(\mu_A)=W-L+\mathcal E_m(\mu_A)
\]

then gives \(o(W)\) holes as well.  \(\square\)

Theorem 7.1 is a genuine positive local-to-global exchange theorem at the
owner scale.  It mixes coordinate frames, automatically retains a
near-transversal, and has top congestion one.  A whole global switch from
\(\mathcal F\) to \(\mathcal F^g\) only relabels every shadow load and
therefore preserves every hole count.  Its power can come only from
choosing different overlay components on different sides.

The theorem does not assert that the matched overlay has many components.
It may be connected.  Formula (7.10) gives the exact relaxation: one may
cut a connected overlay provided the total matched owner boundary is
\(o(W)\).  The exact interface counterterm is the boundary sum in
(7.10a), and its worst-case norm is \(|\partial_GA|\).  An expanding
overlay would obstruct all balanced low-toll mixtures, whereas a
deliberately clustered overlay supplies many independent or nearly
independent frame choices.

### Theorem 7.2 (involutive frame symmetry)

Suppose \(g^2=1\).  The maximal occurrence matching between
\(\mathcal F\) and \(\mathcal F^g\) can be chosen so that \(g\) reverses
every matched owner edge:

\[
U\xrightarrow{\,X\,}V
\quad\Longleftrightarrow\quad
gV\xrightarrow{\,gX\,}gU.
\tag{7.12}
\]

Consequently \(g\) permutes the weak overlay components.  For a component
\(C\), let

\[
z_C=\sum_{U\in C}(e_{P_U^g}-e_{P_U}).
\tag{7.13}
\]

Then

\[
\boxed{
z_{gC}=-g z_C,
\qquad
B_sz_{gC}=-g(B_sz_C)
}
\tag{7.14}
\]

at every rank \(s\).  If \(C=gC\), its discrepancy is \(g\)-antisymmetric.
If \(C\) and \(gC\) are distinct, they supply a paired pair of component
directions.

#### Proof

For every owner orbit \(\{X,gX\}\), match the same number

\[
\min\{\mu(X),\mu(gX)\}
\]

of occurrences in the two conjugate directions.  If an old occurrence of
\(X\) at \(U\) is matched to the new occurrence obtained by applying \(g\)
to an old occurrence of \(gX\) at \(gV\), it gives the first edge in
(7.12).  Pair the two old occurrences in the reverse direction to obtain
the conjugate edge.  Fixed owners are handled by a \(g\)-symmetric matching
of their occurrence lists.  This proves the edge-reversing symmetry and
therefore the component permutation.

For \(V=gU\),

\[
P_{gU}^g=gP_U,
\qquad
P_{gU}=gP_U^g.
\]

Substitute these identities into (7.13) over \(gC\) to get
\(z_{gC}=-gz_C\).  Applying \(B_s\), which commutes with coordinate
permutation, proves the second identity.  \(\square\)

Theorem 7.2 gives exact directional symmetry but not component
fragmentation.  A single \(g\)-invariant expanding component still leaves
only one global switch and no hole improvement.  The desired construction
must combine this involutive sign structure with many components or
\(o(W)\)-boundary sparse cuts.

The remaining automorphism-specific gate is:

> **Automorphism component descent \(\mathrm{ACD}_Q\).**  Given a packet
> owner near-transversal \(\mathcal F\), choose a coordinate permutation
> \(g\) and a top set \(A\) with matched-overlay boundary \(o(W)\), such
> that the hybrid family has aggregate hard-band excess collision \(o(W)\).

The owner toll in \(\mathrm{ACD}_Q\) is already \(o(W)\) by Theorem 7.1.
Only the shallow component-direction assertion is open.  Allowing a
bounded sequence of coordinate permutations retains \(o(W)\) owner toll
and bounded top congestion, and explicitly supplies the phase-changing
frame mechanism excluded by the fixed-pair capacity audit.

These facts give the correct local-to-global target.

> **Long packet-exchange theorem \(\mathrm{LPX}_Q\).**  There is an
> owner-near-transversal which, after changing only \(o(W)\) owner
> occurrences, admits a family of squarefree owner-preserving or
> automorphism-near-preserving packet
> exchanges such that:
>
> 1. every top belongs to \(O(1)\) exchange components;
> 2. every nontrivial component lies in the coordinate 2-core of its top
>    family;
> 3. the aggregate useful shadow variation per active top is
>    \(\Omega(M)\), rather than \(O(1)\);
> 4. signs or sequential applications of the components reduce the total
>    shallow flag holes through depths \(q\le Q\) to \(o(W)\); and
> 5. the total endpoint, owner-collision, and component-interface loss is
>    \(o(W)\).

The statement allows exchange components themselves to be long.  The
bounded quantity is top congestion, not component size.  That distinction
is forced by (5.4).

## 8. A smaller exact combinatorial gate

The core construction can be isolated without mentioning the final word.

> **Packet-cycle reassembly gate \(\mathrm{PCR}_Q\).**  Find a set
> \(\mathcal O\) of \(W-o(W)\) distinct owners and two tagged packet
> decompositions \(\mathcal F^-,\mathcal F^+\) of \(\mathcal O\), one
> packet at each used top, such that:
>
> \[
> \sum_{U}\sum_{q=1}^{Q}
> \left(
> \|B_{m-q}(P_U^+-P_U^-)\|_1+
> \|B_{m+q}(P_U^+-P_U^-)\|_1
> \right)
> =\Omega(WQ)
> \tag{8.1}
> \]
>
> while every top occurs once and the connected
> owner-overlay components can be oriented to give descent for the current
> flag-hole vector with only \(o(W)\) residual.

The left side of (8.1) is raw per-top variation before cancellation between
tops.  It is the throughput requirement.  The last clause is the
discrepancy-direction requirement.  Separating them prevents a highly
nonlocal reassembly with almost identical shallow shadows from being
mistaken for an absorber.

For one prescribed rank, an even smaller gate is:

> **One-rank component descent \(\mathrm{ORCD}_r\).**  Whenever a
> top-tagged owner matching has rank-\(r\) hole vector of size
> \(\Omega(W)\) and point-margin error \(o(W)\), it has a union of
> owner-overlay components, using each top at most once, whose exchange
> decreases the hole count by \(\Omega(M)\) per changed top on average and
> creates only \(o(W)\) total new holes after all chosen components are
> applied.

For a fixed number of ranks, \(\mathrm{ORCD}_r\) can be iterated using
separate reservoirs.  For growing \(Q\), that loses a factor \(Q\) and is
insufficient: the same long components must deliver useful discrepancy at
many ranks simultaneously.  No generic probabilistic rounding theorem gives
even \(\mathrm{ORCD}_r\), because it must respect both packet reassembly and
component closure.

## 9. Routing the signed square demands

Although signed generation is already proved, its top congestion can be
separated as an exact deterministic allocation problem.

A rank-\(r\) elementary square has support on \(r+2\) coordinates.  The
number of calibrated tops containing that support is

\[
d_r=
\binom{2m-r-2}{M-r-2}.
\tag{9.1}
\]

Thus

\[
d_{m-q}
=\binom{m+q-2}{H+q-2},
\qquad
d_{m+q}
=\binom{m-q-2}{H-q-2}.
\tag{9.2}
\]

For a multiset \(\mathcal D\) of signed square demands, assign each demand
to one containing top.  An assignment of top load at most \(\kappa\)
exists if and only if

\[
|\mathcal D'|
\le
\kappa\,|N(\mathcal D')|
\qquad
(\mathcal D'\subseteq\mathcal D),
\tag{9.3}
\]

where \(N(\mathcal D')\) is the family of tops containing at least one
demand in \(\mathcal D'\).  This is the exact capacitated Hall condition.

For shallow \(q\), (9.2) gives many possible top lifts for each square.
Near the upper packet boundary \(q=H-2\), however, \(d_{m+q}=1\), so
congestion cannot be spread at all.  This is another reason to reserve the
outer upper rows for literal \(o(W)\) repair and use exchanges only in a
strictly shallower band.

Even a perfect solution of (9.3) would only route signed rectangles.  By
Proposition 6.1 it would not supply macroscopic positive throughput at
bounded congestion.  It is useful as a final absorber routing lemma after
long exchanges have reduced the residual to \(o(W)\).

## 10. Audit ledger

### Proved

1. Every owner-preserving top trade has zero point margins at every exposed
   rank.
2. Owner-preserving packet trades generate the full zero-margin lattice
   independently at all supported hard-band ranks.
3. There is no additional signed parity or cross-rank obstruction.
4. The exact owner overlay of two packet matchings is an
   \(M\)-in/\(M\)-out directed multigraph.
5. Owner-preserving subtrades are exactly unions of weak overlay
   components.
6. Formula (3.6) is the exact owner counterterm left by an unclosed
   alternating cycle.
7. Whole overlay components are independent positive binary switches with
   top congestion one, and every mixture of two decompositions arises this
   way.
8. Flag holes are exactly excess collisions through identities
   (3.13)--(3.15).
9. Lower and upper flags are exact forward-intersection and
   backward-union path statistics of the owner successor permutation.
10. Switching \(d\) successor arcs affects at most \(qd\) starts at depth
    \(q\), but an arbitrary successor alternating cycle need not be
    top-packet-valid.
11. A packet is reconstructed up to reversal by the \(m\) middle windows
   containing one fixed coordinate.
12. Every reduced nontrivial squarefree trade lies in the coordinate 2-core
   of its active top family; in particular no nontrivial two-top exchange
   exists.
13. A \(k\)-top reduced component obeys the clustering bounds
   (4.7)--(4.9).
14. Two packets on distinct tops share at most \(H\) owners, and every
    nonloop overlay edge has top distance at most \(H\).
15. Moving a positive fraction of packet owners forces growing overlay
    degree \(\Omega(M/H)\).
16. Bounded-congestion adjacent rectangles have only \(o(W)\) aggregate
    one-rank throughput.
17. The signed top-routing problem has the exact Hall criterion (9.3).
18. Every coordinate permutation produces a second valid packet
    decomposition with owner discrepancy at most \(2(W-L+2C_0)=o(W)\).
19. Arbitrary weak-component hybrids of the matched automorphism overlay
    have top congestion one and retain \(o(W)\) owner collision and holes.
20. For arbitrary automorphism hybrids, the exact additional owner
    counterterm is (7.10a), with norm at most the matched-overlay cut size
    plus the baseline \(o(W)\) unmatched-stub toll.
21. Involutive coordinate changes reverse the matched overlay and pair
    component discrepancies by \(z_{gC}=-gz_C\).

### Open

1. Existence of a large owner near-transversal with a second nontrivial
   tagged packet-cycle decomposition.
2. Long exchange components with \(\Omega(M)\) useful shallow discrepancy
   per active top.
3. Deterministic orientation or sequencing of those components with
   bounded top congestion and simultaneous descent across \(q\le Q\).
4. Automorphism component descent \(\mathrm{ACD}_Q\).
5. The packet-cycle reassembly gate \(\mathrm{PCR}_Q\), hence
   \(\mathrm{LPX}_Q\).
6. Coefficient one by this owner-preserving exchange route.

The alternating-cycle idea is therefore neither empty nor complete.  Its
signed span is exactly right, but its positive atoms are full connected
packet-reassembly components.  Any successful local-to-global theorem must
construct and orient those long components, or find automorphism-overlay
cuts of \(o(W)\) boundary.  Ordinary alternating-cycle decomposition alone
leaves the boundary counterterm (3.6).
