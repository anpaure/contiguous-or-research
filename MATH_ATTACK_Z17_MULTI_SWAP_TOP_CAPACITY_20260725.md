# Multi-swap capacity in one calibrated top

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let

\[
 M=m+H,
 \qquad
 \mathcal B_Q=\{m-Q,\ldots,m+Q\}.
\]

Assume along the calibrated asymptotic regime that

\[
 H=o(m),\qquad Q=o(H),\qquad {Q\over\sqrt M}\longrightarrow\infty.
\tag{0.1}
\]

In particular, this applies to

\[
 H\asymp\sqrt{m\log m},
 \qquad
 Q\asymp\sqrt{m\log\log m}.
\]

There is a genuine positive multi-rectangle capacity theorem.
For every sufficiently large (m), one calibrated top admits two literal
complementary-segment deployments, each with

\[
 M+(2+o(1))Q
\tag{0.2}
\]

state occurrences, whose difference is a sum of

\[
 L^2=(1-o(1))M,
 \qquad L=\lfloor\sqrt M\rfloor,
\tag{0.3}
\]

pairwise support-disjoint elementary rank-isolating rectangles.  Their
total hard-band effect therefore has exact norm

\[
 \boxed{
 \sum_{s\in\mathcal B_Q}
 \bigl\|I_s(\mathcal C^-)-I_s(\mathcal C^+)\bigr\|_1
 =4L^2=(4-o(1))M.}
\tag{0.4}
\]

Both deployments retain at least (M-4L) distinct middle owners.  Their
owner-collision excess is at most

\[
 (2+o(1))Q.
\tag{0.5}
\]

All (2L) swaps can simultaneously be hidden in one unordered reserve
block.  Consequently the four composite cyclic frames have exact common
useful-state splice ports.  No reset or fragment is paid per elementary
rectangle.

There is also an exact limitation.  The (L^2) cells furnished by one
four-frame composite diagonal are **not (L^2) independently selectable
bits**.  Their coefficient matrix is an outer product.  In particular
their signs obey

\[
 c_{ij}c_{i'j'}=c_{ij'}c_{i'j}
\tag{0.6}
\]

on every four-cycle.  Thus the construction proves coefficient-scale
aggregate correction capacity at (O(Q)) owner duplication, and rules
out an \(\Omega(M)\)-duplication obstruction to aggregate capacity, but it
does not prove arbitrary residual absorption.  Breaking (0.6) requires a
genuinely multi-strand or phase-varying construction, not merely a hidden
splice of one composite diagonal.

Such a phase-varying construction exists at the static useful-state
level.  A second theorem below gives an exact (L^2=(1-o(1))M)-bit
Boolean cube of positive states with only (L=O(Q)) duplicated phase
positions and a middle-owner multiset independent of all (L^2) bits.
However, a worst vertex of that cube obeys the sharp path inequality

\[
 N\ge F+(2L-F)(H-6L+1),
\tag{0.7}
\]

where (N) is the number of useful-state occurrences and (F) is the
number of promotion paths containing the (2L) marked port states.
Thus (N=M+O(Q)) forces (F=(2-o(1))L), while (F=O(1)) forces
(N=\Omega(LH)=\omega(M)).  The independent cube therefore does not give
a coefficient-one literal word.  Hidden-reserve splicing solves the
aggregate grid but cannot change an orientation while the marked labels
are in the ordered deletion queue.

The rest of the note proves these assertions with constants and audits
the distinction between aggregate cells and independent choices.

## 1. Phase notation and a composite segment identity

Fix a top (U), (|U|=M), and a directed cyclic order (pi) on (U).
Index its positions and phase starts by \(\mathbb Z_M\).  For a cut (c),
meaning the cut between positions (c-1) and (c), let
\(\sigma_c\) interchange the entries in those two positions.

For a cyclic order \(\rho\), let

\[
 v_{s,t}(\rho)=e_{[t,t+s-1]_\rho}
\tag{1.1}
\]

be the basis vector of its length-(s) interval starting at phase (t),
and put

\[
 I_{s,A}(\rho)=\sum_{t\in A}v_{s,t}(\rho),
 \qquad I_s(\rho)=I_{s,\mathbb Z_M}(\rho).
\tag{1.2}
\]

### Lemma 1.1 (affected starts of a swap product)

Let (P) be a product of adjacent position swaps whose cuts form a set
(C\subseteq\mathbb Z_M).  Then

\[
 v_{s,t}(P\rho)=v_{s,t}(\rho)
\quad\hbox{whenever}\quad
 t\notin\bigcup_{c\in C}\{c,c-s\}.
\tag{1.3}
\]

Consequently every hard-band first difference under (P) is supported
on

\[
 E_Q(P):=
 \bigcup_{c\in C}
 \left(\{c\}\cup\{c-s:s\in\mathcal B_Q\}\right).
\tag{1.4}
\]

#### Proof

A length-(s) positional interval notices the swap at cut (c) exactly
when one of its two boundary cuts is (c), namely when its start is (c)
or (c-s).  Outside the displayed union, every constituent transposition
exchanges either two positions inside the interval or two positions
outside it.  Each transposition, and hence their product, preserves the
interval's label set. \(\square\)

The next statement is the complementary-segment identity with an entire
swap product in place of one swap.

### Theorem 1.2 (composite complementary-segment identity)

Let (P,R) be products of position swaps, and assume their moved-position
supports are disjoint.  Let (A,B\subseteq\mathbb Z_M) satisfy

\[
 A\cup B=\mathbb Z_M,
 \qquad E_Q(P)\subseteq A\cap B.
\tag{1.5}
\]

Define two positive phase deployments

\[
 \begin{aligned}
 \mathcal C^-&=\pi|_A\ \sqcup\ PR\pi|_B,\\
 \mathcal C^+&=P\pi|_A\ \sqcup\ R\pi|_B.
 \end{aligned}
\tag{1.6}
\]

Then, for every (s\in\mathcal B_Q),

\[
 \boxed{
 I_s(\mathcal C^-)-I_s(\mathcal C^+)
 =I_s(\pi)+I_s(PR\pi)-I_s(P\pi)-I_s(R\pi).}
\tag{1.7}
\]

#### Proof

At a phase in (A-B), the left side of (1.7) has local contribution

\[
 v_{s,t}(\pi)-v_{s,t}(P\pi),
\]

which is zero by Lemma 1.1 because (t\notin E_Q(P)).  At a phase in
(B-A), its local contribution is

\[
 v_{s,t}(PR\pi)-v_{s,t}(R\pi),
\]

and this is zero for the same positional reason.  The disjointness of the
moved positions ensures that applying (R) does not move a (P)-cut.

At a phase in (A\cap B), all four terms occur and give the full local
mixed difference.  That full mixed difference is itself zero outside
(E_Q(P)), again by Lemma 1.1.  Summing over phases proves (1.7).
\(\square\)

This proof is integral and phasewise.  It neither divides a packet nor
uses a formal negative state.

## 2. A \(\sqrt M\) by \(\sqrt M\) swap grid

For all sufficiently large (m), (0.1) implies

\[
 4H<m,qquad 4Q<H,qquad 6L\le {Q\over8},
 \qquad L=\lfloor\sqrt M\rfloor.
\tag{2.1}
\]

Put (q_0=\lfloor Q/2\rfloor).  Choose the two cut families

\[
 a_i=6i,
 \qquad
 b_j=m+q_0+6j,
 \qquad 0\le i,j<L.
\tag{2.2}
\]

Let

\[
 \sigma_i=\sigma_{a_i},
 \qquad
 \tau_j=\sigma_{b_j},
\tag{2.3}
\]

and define

\[
 P_i=\sigma_{i-1}\cdots\sigma_0,
 \qquad
 R_j=\tau_{j-1}\cdots\tau_0,
\tag{2.4}
\]

with (P_0=R_0=1), and (P=P_L, R=R_L).
The spacing six makes all (2L) swapped position pairs disjoint.  The
last (b)-cut lies below (M=m+H) by (2.1), so all cuts are well-defined
without wrap ambiguity inside their two clusters.

Define the free four-frame difference

\[
 Z=e_\pi+e_{PR\pi}-e_{P\pi}-e_{R\pi}.
\tag{2.5}
\]

### Lemma 2.1 (exact grid telescoping)

In the free integer module on cyclic orders,

\[
 \boxed{
 Z=\sum_{i=0}^{L-1}\sum_{j=0}^{L-1}Z_{ij},}
\tag{2.6}
\]

where

\[
 \begin{aligned}
 Z_{ij}
 &=e_{P_iR_j\pi}+e_{P_{i+1}R_{j+1}\pi}\\
 &\quad-e_{P_{i+1}R_j\pi}-e_{P_iR_{j+1}\pi}.
 \end{aligned}
\tag{2.7}
\]

Each (Z_{ij}) is the elementary adjacent-swap square for the disjoint
swaps \(\sigma_i,\tau_j\), based at (P_iR_j\pi).

#### Proof

Sum (2.7) first in (j).  It telescopes to the difference between the
(R_L)-edge and the (R_0)-edge in row (i).  Summing those row
differences in (i) leaves exactly the four corners in (2.5).  All
coefficients are integral and no incidence relation has yet been used.
\(\square\)

The directed separation of the two cuts in cell ((i,j)) is

\[
 r_{ij}=b_j-a_i=m+q_{ij},
 \qquad
 q_{ij}=q_0+6(j-i).
\tag{2.8}
\]

By (2.1), for all sufficiently large (Q),

\[
 {Q\over4}\le q_{ij}\le {3Q\over4}.
\tag{2.9}
\]

### Theorem 2.2 (rank isolation and noncancellation)

Inside the hard band, the interval incidence of (Z_{ij}) is supported
only at rank (r_{ij}), where it is one elementary four-mask rectangle.
Moreover, the four-mask supports belonging to different pairs ((i,j))
are disjoint.  Hence

\[
 \boxed{
 \sum_{s\in\mathcal B_Q}\|I_s(Z)\|_1=4L^2.}
\tag{2.10}
\]

#### Proof

An adjacent-swap square is noticed only by intervals whose two boundary
cuts are the two swap cuts.  Thus its only exceptional lengths are

\[
 r_{ij}quad\hbox{and}\quad M-r_{ij}=H-q_{ij}.
\tag{2.11}
\]

Equation (2.9) puts (r_{ij}) in the hard band.  The companion length is
below the central band because (H-q_{ij}<m-Q) under (2.1).  At rank
(r_{ij}), the usual four endpoint choices give four distinct masks with
coefficients (+1,+1,-1,-1).

It remains to rule out cancellation between cells.  Let (A_i\) be the
two-label block occupying positions (a_i-1,a_i) in the base order, and
let (B_j\) be the analogous block at (b_j-1,b_j).  The blocks

\[
 A_0,\ldots,A_{L-1},B_0,\ldots,B_{L-1}
\tag{2.12}
\]

are pairwise disjoint.  Every mask in the support of cell ((i,j))
contains exactly one label from (A_i), exactly one label from (B_j),
and either zero or two labels from every other block in (2.12).  Indeed,
the directed positional interval from cut (a_i) to cut (b_j) has
those two cuts as its boundaries, while every other swapped pair lies
wholly inside or wholly outside it.  The prefix products in (2.7) only
reverse labels inside these disjoint two-blocks.

Therefore the vector of intersection parities with the blocks in (2.12)
identifies the ordered pair ((i,j)).  Supports from two different cells
cannot share a mask.  Every cell contributes norm four, proving (2.10).
\(\square\)

Since

\[
 M-2\sqrt M\le L^2\le M,
\tag{2.13}
\]

this is a \(\Theta(M)\), indeed ((1-o(1))M), collection of genuine
rank-isolating rectangle cells.

## 3. One common \(O(Q)\) overlap

The (a)-cuts occupy a positional interval of length at most (6L).
Formula (1.4) therefore places (E_Q(P)) in two cyclic intervals:

1. the hull of the cuts (a_i), of length at most (6L);
2. the hull of all (a_i-s), (s\in\mathcal B_Q), of length at most
   (2Q+6L+2).

For large (m) these two intervals are disjoint because (Q=o(H)).
Enlarging endpoints harmlessly, choose their union (O) so that

\[
 E_Q(P)\subseteq O,
 \qquad
 |O|\le 2Q+12L+4=(2+o(1))Q.
\tag{3.1}
\]

If the circle is written (O_0,G_0,O_1,G_1), take one cyclic phase
interval through (O_0,G_0,O_1) and the other through
(O_1,G_1,O_0).  This gives cyclic intervals (A,B) with

\[
 A\cup B=\mathbb Z_M,
 \qquad A\cap B=O.
\tag{3.2}
\]

Apply Theorem 1.2 to the products (P,R) from Section 2.

### Theorem 3.1 (positive multi-rectangle deployment)

The two literal deployments

\[
 \mathcal C^-=\pi|_A\sqcup PR\pi|_B,
 \qquad
 \mathcal C^+=P\pi|_A\sqcup R\pi|_B
\tag{3.3}
\]

have (M+D) occurrences each, where

\[
 D=|A\cap B|\le2Q+12L+4=(2+o(1))Q.
\tag{3.4}
\]

Their exact hard-band difference is the (L^2)-cell grid of Theorem 2.2.
At middle rank their incidence vectors are exactly equal.  Each deployment
has at least (M-4L) distinct middle owners, and therefore owner-collision
excess at most

\[
 D+4L=(2+o(1))Q.
\tag{3.5}
\]

#### Proof

The occurrence count is

\[
 |A|+|B|=M+|A\cap B|.
\]

Theorem 1.2 and Lemma 2.1 identify the hard-band difference with (I_s(Z)),
and Theorem 2.2 gives its exact cell decomposition and norm.

No cell has exceptional length (m): its central exceptional length is
(m+q_{ij}>m), while its companion is (H-q_{ij}<m).  Thus (2.6)
also gives

\[
 I_m(\mathcal C^-)=I_m(\mathcal C^+)
\tag{3.6}
\]

as an exact multiplicity vector.

For the distinct-owner count, select one occurrence over each of the
(M) phases.  In \(\mathcal C^-\), use the \(\pi\)-occurrence on (A)
and the (PR\pi)-occurrence only on (B-A).  The product (PR) contains
(2L) adjacent swaps, each of which affects exactly two middle starts.
At all but at most (4L) phases, the selected owner is therefore the
base owner of \(\pi\) at that phase.  The (M) middle cyclic intervals of
one labelled cyclic order are distinct, so these give at least (M-4L)
distinct owners.

For \(\mathcal C^+\), select the (P\pi)-occurrence on (A) and the
(R\pi)-occurrence on (B-A).  The union of their middle affected-start
sets again has size at most (4L), giving the same conclusion.  Subtracting
the distinct-owner lower bound from the total occurrence count proves
(3.5). \(\square\)

Thus the word-length and owner toll is paid once for the entire grid, not
once per cell.

## 4. Exact hidden-interior ports

The moved positions of (P) and (R) lie in the short cyclic arc which
starts at the (b)-cluster, passes through the end of the cyclic order,
and ends at the (a)-cluster.  Its length is at most

\[
 h_*:=H-q_0+6L+2.
\tag{4.1}
\]

By (0.1), for all sufficiently large (m),

\[
 h_*<m-H.
\tag{4.2}
\]

At a phase of a promotion packet, the unordered reserve (L_t) occupies
a cyclic positional block of length (m-H).  There are at least

\[
 m-H-h_*+1
\tag{4.3}
\]

phases for which that reserve block contains the entire moved-position
arc.  At every such phase, all swaps in (P) and (R) occur wholly
inside the unordered reserve.  Hence

\[
 \pi,quad P\pi,quad R\pi,quad PR\pi
\tag{4.4}
\]

have the same ordered deletion queue, the same ordered upper cache, and
the same reserve set.  They encode one and the same useful state.

This is an exact common splice port, not an equality merely at the owner
level.  One may cut the phase intervals at such a port and change among
the four cyclic representatives without an MTF entry or reset.  If a
chosen port is not already a boundary of (3.2), insert it as one additional
zero-difference overlap phase and split there.  This changes (3.4) by at
most one and leaves only (O(1)) promotion-path components.  In particular
the number of fragments and resets is independent of (L^2).

The point of the hidden-interior freedom is exactly here: all swaps are
installed before they become visible, their full interaction grid is
carried by the long pieces, and all swaps are removed again at one common
useful-state port.

## 5. Capacity bounds inside the two-product model

The preceding scale is essentially best possible for a Cartesian grid of
pairwise disjoint adjacent swaps.

### Proposition 5.1 (cross-separation capacity)

Let (p) disjoint primary adjacent swaps and (q) disjoint secondary
adjacent swaps have every directed cross-separation in
([m-Q,m+Q]).  Then

\[
 p,q\le Q+1,
 \qquad pq\le(Q+1)^2.
\tag{5.1}
\]

#### Proof

Fix one primary cut.  All secondary cuts lie in a block of (2Q+1)
consecutive cut positions.  Two cuts at distance one give adjacent swaps
sharing a position, so at most (Q+1) pairwise disjoint swaps fit in that
block.  This proves (q\le Q+1).  Interchanging the two families proves
the same bound for (p). \(\square\)

Thus the natural aggregate ceiling is (O(Q^2)).  The condition
(Q/\sqrt M\to\infty) is precisely what permits an (M)-cell subgrid
well below that ceiling.

There is also a sharp leading overlap lower bound for a universal primary
cut.

### Proposition 5.2 (universal overlap lower bound)

Fix a primary adjacent swap at cut (c).  Suppose one pair of
complementary phase sets is required to reproduce, for every
(s\in\mathcal B_Q), the full mixed square obtained by putting a secondary
swap at the other boundary of the corresponding length-(s) interval.
Then its overlap must contain

\[
 \{c\}\cup\{c-s:s\in\mathcal B_Q\},
\tag{5.2}
\]

and hence has size at least

\[
 \boxed{2Q+2.}
\tag{5.3}
\]

#### Proof

Every phase in (5.2) is a phase at which the primary first difference is
nonzero.  For that phase and length (s), put the secondary cut at the
other boundary of the same interval.  The local mixed difference is then
the nonzero elementary rectangle at rank (s), and it is the unique
central-rank phase having those two boundary cuts.  If the phase were not
duplicated, the truncated diagonal would retain only one first difference
there and would miss that rectangle.  Thus every displayed phase is
forced.  They are distinct because (1\le m-Q\le m+Q<M). \(\square\)

The overlap in (3.4) is therefore asymptotically sharp at leading constant
two for a universal hard-band primary family.

## 6. The sign-lock obstruction

The cell count in Theorem 3.1 must not be confused with the number of
independently selectable bits.

Consider the Boolean cube generated by the disjoint swaps
(\sigma_0,\ldots,\sigma_{p-1}) and
(\tau_0,\ldots,\tau_{q-1}).  Choose two opposite primary corners and
two opposite secondary corners.  Traverse the primary coordinate (i)
with orientation (u_i\in\{+1,-1\}), and the secondary coordinate (j)
with orientation (v_j\in\{+1,-1\}).  Double telescoping, with the
standard orientation fixed for every elementary cell, gives coefficient

\[
 \boxed{c_{ij}=u_i v_j.}
\tag{6.1}
\]

This statement is simply Lemma 2.1 with some coordinate paths traversed
backwards.  It gives the exact four-cycle identities

\[
 c_{ij}c_{i'j'}=c_{ij'}c_{i'j}
\tag{6.2}
\]

for all (i,i',j,j').  Equivalently, modulo two the sum of the four edge
choices around every (K_{2,2}) is zero.  The family of nonzero sign
patterns has only

\[
 p+q-1
\tag{6.3}
\]

binary degrees of freedom, rather than (pq).  If some swap coordinates
are omitted, the nonzero cell support is a complete bipartite subgraph,
not an arbitrary subset of cells.

For the concrete deployment (3.3), there is only one binary diagonal
choice: exchanging \(\mathcal C^-\) and \(\mathcal C^+\) reverses all
(L^2) rectangles together.  Permuting the hidden reserve at the common
port can choose the row and column orientations (u_i,v_j), but it cannot
break (6.2), because (6.2) is an identity in the free order module before
any physical realization is chosen.

Therefore:

* **proved positive:** one top has \(\Theta(M)\) support-disjoint,
  rank-isolating rectangle cells and \(\Theta(M)\) aggregate
  \(\ell_1\)-capacity at only (O(Q)) duplicate owner phases;
* **proved negative within one composite diagonal:** those cells are
  sign-locked and do not form \(\Theta(M)\) independent selector bits;
* **constructed below at the state-multiset level:** a phase-varying
  (L^2)-bit cube which breaks the cycle identities with only (L)
  duplicated phases;
* **obstructed below at the literal low-fragment level:** worst vertices
  of that cube require either \(\Theta(L)\) promotion fragments or
  \(\Omega(LH)\) state occurrences.

## 7. An exact independent static port cube

The preceding sign lock belongs to one four-frame composite diagonal; it
is not an information-theoretic obstruction at the level of positive
state multisets.  This section gives the exact counterpoint.

Retain (L=\lfloor\sqrt M\rfloor), and assume, as follows from (0.1) for
all sufficiently large (m), that

\[
 6L\le Q,
 \qquad 8L<H.
\tag{7.1}
\]

Use a new collection of disjoint adjacent swaps.  Let the row swap
\(\alpha_i\) exchange positions (a_i,a_i+1), where

\[
 a_i=4L+2i,
 \qquad 0\le i<L,
\tag{7.2}
\]

and let the column swap \(\beta_j\) exchange positions (b_j,b_j+1),
where

\[
 b_j=m+2j-1,
 \qquad s_j=2j,
 \qquad 0\le j<L.
\tag{7.3}
\]

Here (s_j) is the (j)-th marked phase.  The row and column pairs are
all disjoint because (6L=o(m)).

For (x\in\{0,1\}^L), put

\[
 \alpha_x=\prod_{i=0}^{L-1}\alpha_i^{x_i},
 \qquad
 \bar x=\mathbf1-x,
 \qquad
 \beta=\prod_{j=0}^{L-1}\beta_j.
\tag{7.4}
\]

Let (S_t(\rho)) denote the radius-(H) useful state encoded by cyclic
order \(\rho\) at phase (t).  At port (s_j), define the positive
two-state multiset

\[
 \mathcal F_j(x)=
 \{S_{s_j}(\alpha_x\pi),
   S_{s_j}(\alpha_{\bar x}\beta\pi)\}.
\tag{7.5}
\]

For a bit matrix (E=(E_{ij})\in\{0,1\}^{L\times L}), let (x^j) be its
(j)-th column and define

\[
 \mathcal F(E)=
 \{S_t(\pi):t\notin\{s_0,\ldots,s_{L-1}\}\}
 \ \sqcup\ 
 \bigsqcup_{j=0}^{L-1}\mathcal F_j(x^j).
\tag{7.6}
\]

Thus an ordinary base state is used at every unmarked phase, while the
one base occurrence at a marked phase is replaced by two positive states.

### Theorem 7.1 (positive (L^2)-bit state cube)

Every \(\mathcal F(E)\) has exactly

\[
 M+L
\tag{7.7}
\]

state occurrences.  Its middle-owner multiset is independent of (E)
and contains all (M) base owners.

For each pair ((i,j)), put

\[
 q_{ij}=a_i-s_j+1=4L+2i-2j+1.
\tag{7.8}
\]

Then

\[
 2L+3\le q_{ij}\le6L-1\le Q.
\tag{7.9}
\]

There are pairwise support-disjoint elementary rectangles
\(\rho_{ij}\), with \(\rho_{ij}\) supported only at lower rank
\(m-q_{ij}\) inside the calibrated band, such that

\[
 \boxed{
 I_{\mathcal B_Q}(\mathcal F(E))
 -I_{\mathcal B_Q}(\mathcal F(0))
 =\sum_{i,j}E_{ij}\rho_{ij}.}
\tag{7.10}
\]

Consequently the image is an actual (L^2)-dimensional Boolean cube and

\[
 \sum_{s\in\mathcal B_Q}
 \|I_s(\mathcal F(E))-I_s(\mathcal F(E'))\|_1
 =4\,d_{\rm Ham}(E,E').
\tag{7.11}
\]

#### Proof

At phase (s_j), the middle owner of the base order is the positional
interval

\[
 X_j=[s_j,s_j+m-1]=[2j,m+2j-1].
\tag{7.12}
\]

Every row pair lies wholly inside (X_j), so \(\alpha_x\) does not alter
this owner.  Among the column pairs, those with index below (j) lie
wholly inside (X_j), those with index above (j) lie wholly outside,
and only \(\beta_j\) crosses its right boundary.  Thus (7.5) has owner
multiset

\[
 \{X_j,\beta_jX_j\},
\tag{7.13}
\]

independent of (x).  Equation (7.6) therefore contains every one of the
(M) base owners and has exactly one extra occurrence at each of the
(L) ports.  This proves the occurrence and owner assertions.

Now toggle the (i)-th bit of (x) at port (j).  Suppose first that
(x_i=0), and separate the other row swaps as

\[
 G=\prod_{h\ne i}\alpha_h^{x_h},
 \qquad
 K=\prod_{h\ne i}\alpha_h^{1-x_h}.
\]

The signed change in the two port states is

\[
 e_{\alpha_iG\pi}+e_{K\beta\pi}
 -e_{G\pi}-e_{\alpha_iK\beta\pi}.
\tag{7.14}
\]

At a lower depth (q), the phase-(s_j) flag is the positional interval

\[
 [s_j+q,s_j+m-1].
\tag{7.15}
\]

It notices \(\alpha_i\) exactly when its left boundary is the
\(\alpha_i\)-cut, namely when (q=q_{ij}).  At that value, its right
boundary is the \(\beta_j\)-cut.  Every other row pair and every other
column pair lies wholly inside or wholly outside (7.15).  Their swaps
therefore disappear at the level of the interval label set, and (7.14)
is exactly the elementary \(\alpha_i\)-by-\(\beta_j\) rectangle.  At all
other lower depths \(\alpha_i\) is invisible, so (7.14) vanishes.

Every upper flag at this phase contains both positions of every row pair.
Hence (7.14) vanishes at every upper rank and at the middle rank.  The
same conclusion, with reversed sign, holds when (x_i=1).  Toggling the
matrix entries one at a time proves (7.10), because the resulting
rectangle is independent of the other bits.

It remains to audit support disjointness.  Different values of (q_{ij})
give different ranks.  If

\[
 q_{ij}=q_{i'j'},
\]

then (i'-i=j'-j=d).  Suppose (d>0).  Every mask in the later cell
\((i',j')\) contains both labels of the earlier right-boundary block
\(\beta_j\), because that whole block lies strictly inside its positional
interval.  Every mask in cell ((i,j)) contains exactly one of those two
labels.  Thus the supports are disjoint.  The case (d<0) is symmetric.
Each rectangle has four distinct masks, proving (7.11). \(\square\)

Theorem 7.1 answers the owner-phase capacity question affirmatively in
the strongest static sense: \(\Theta(M)\) independent cells coexist with
only \(\Theta(\sqrt M)=O(Q)\) duplicated phase positions, and their middle
histogram is fixed exactly.

The symmetric dimensions make the geometry transparent, but the duplicate
count can be sharpened.

### Corollary 7.2 (rectangular (M)-cell cube with (o(Q)) ports)

Put

\[
 p=\lfloor Q/4\rfloor,
 \qquad
 t=\left\lceil {M\over p}\right\rceil.
\tag{7.16}
\]

For all sufficiently large (m), (0.1) gives

\[
 4t+2p\le Q.
\tag{7.17}
\]

Use (p) row cuts (a_i=4t+2i), (0\le i<p), and (t) ports and
column cuts

\[
 s_j=2j,
 \qquad b_j=m+2j-1,
 \qquad 0\le j<t.
\]

The proof of Theorem 7.1, with (L\times L) replaced by (p\times t),
gives

\[
 pt\ge M
\tag{7.18}
\]

independent, support-disjoint hard-band rectangles using exactly (M+t)
positive useful-state occurrences and a fixed middle-owner multiset.  The
depths are

\[
 q_{ij}=4t+2i-2j+1,
 \qquad
 2t+3\le q_{ij}\le4t+2p-1\le Q.
\tag{7.19}
\]

Moreover

\[
 t=(4+o(1)){M\over Q}=o(Q),
\tag{7.20}
\]

because (Q^2/M\to\infty).  Thus even (O(Q)) duplication is not tight
for static independent capacity: (O(M/Q)) duplicated ports suffice.

It is not yet a literal low-overhead deployment, because the (2L) port
states in (7.6) need not lie on (O(1)) promotion paths.  The next section
shows that this is a real chronological obstruction, not a missing splice
observation.

## 8. Ordered-queue fragmentation obstruction

At every marked phase (s_j\le2L-2), all row-pair labels from (7.2) lie
among the first

\[
 R_*=6L
\tag{8.1}
\]

entries of the ordered deletion queue.  Their pair orientations record
the signature (x^j) in the first state of (7.5) and \(\bar x^j\) in the
second.  These labels are not in the unordered reserve, so the
hidden-interior splice cannot change that signature at a marked phase.

The queue update in one promotion step is

\[
 (a_1,\ldots,a_H)\longmapsto(a_2,\ldots,a_H,z)
\tag{8.2}
\]

for some newly selected tail (z).  After (d\le H-R_*) transitions,
the first (R_*) entries of the new queue are inherited, in their old
relative order, from entries (d+1,\ldots,d+R_*) of the old queue.  No
newly appended label has reached that prefix.

### Theorem 8.1 (exact path-length/fragmentation inequality)

Choose columns (x^0,\ldots,x^{L-1}\) such that the (2L) signatures

\[
 x^0,\bar x^0,\ldots,x^{L-1},\bar x^{L-1}
\tag{8.3}
\]

are pairwise distinct.  Such a choice exists for all sufficiently large
(L), since there are (2^{L-1}) complement classes.

Let a literal realization contain the corresponding (2L) marked port
states, use (N) useful-state occurrences in total, and decompose into
(F) promotion paths which contain marked states.  Put

\[
 D=H-6L+1.
\tag{8.4}
\]

Then

\[
 \boxed{N\ge F+(2L-F)D.}
\tag{8.5}
\]

In particular,

\[
 N\le M+O(Q)
 \quad\Longrightarrow\quad
 F\ge(2-o(1))L,
\tag{8.6}
\]

whereas

\[
 F=O(1)
 \quad\Longrightarrow\quad
 N=\Omega(LH)=\omega(M).
\tag{8.7}
\]

#### Proof

Suppose two marked states with different signatures occur on one
promotion path at distance (d<D).  Both states contain all marked row
pairs inside their first (R_*) queue entries.  By (8.2), the later
prefix is inherited from the earlier ordered queue, and the relative
order of the two labels in every marked pair is unchanged.  The two
signatures must therefore be equal, a contradiction.  Hence consecutive
marked states on one path are separated by at least (D) transitions.

If a path contains (k\ge1) marked states, it contains at least

\[
 1+(k-1)D
\]

state occurrences.  Sum this bound over the (F) nonempty paths and use
\(\sum k=2L\) to obtain (8.5).

Solving (8.5) for (F) gives

\[
 F\ge2L-{N-2L\over D-1}.
\tag{8.8}
\]

Here (D=(1-o(1))H), (M/H=o(L)), and (Q/H=o(1)).  Substituting
\(N\le M+O(Q)\) proves (8.6).  Equation (8.7) follows directly from
(8.5), and (LH/M\to\infty) in the calibrated regime. \(\square\)

For the rectangular sharpening of Corollary 7.2, all row labels lie in
the first

\[
 R=4t+2p\le Q
\]

queue entries at the marked ports.  Choosing the (2t) row signatures
pairwise distinct modulo complement and repeating the proof gives

\[
 \boxed{N\ge F+(2t-F)(H-R+1).}
\tag{8.11}
\]

Consequently

\[
 N\le M+O(Q)
 \quad\Longrightarrow\quad
 F=(2-o(1))t=\Theta(M/Q),
\tag{8.12}
\]

while (F=O(1)) forces

\[
 N=\Omega(tH)=\Omega(MH/Q)=\omega(M).
\tag{8.13}
\]

This is the quantitatively sharper static-yes/literal-no boundary.  It
uses only (o(Q)) duplicated owner phases, but the present initialization
ledger would cost order (HM/Q) per top, a factor (H/Q\to\infty) above
the top's coefficient-one budget.

There is a useful architecture-level corollary.  Suppose a port scheme
keeps all active selector pairs within the first (R=O(Q)=o(H)) entries
of an ordered queue, uses (N=O(M)) states and (F) paths, and every
change of port signature must recycle at least one marked label.  Then the
number of distinct signature runs is at most

\[
 F+{N\over H-R}.
\tag{8.9}
\]

One port signature can address at most (2Q+1=O(Q)) hard-band ranks.
Under the coefficient-one reset condition (HF=o(M)), the total number
of independently addressable port rectangles is therefore at most

\[
 O\!\left(Q{M\over H}\right)=o(M).
\tag{8.10}
\]

This is the exact hidden-interior boundary: the reserve may be permuted
freely, but a rank selector becomes active only after its labels enter an
ordered collar.  Reprogramming that collar has throughput one and latency
\((1-o(1))H\).

## 9. Coefficient-one ledger

If the construction is placed on (N_H) calibrated tops satisfying

\[
 MN_H=(1+o(1))W,
\tag{7.1}
\]

then its total duplicate-owner toll is

\[
 O(QN_H)=O(WQ/m)=o(W),
\tag{7.2}
\]

and its bounded number of path initializations costs

\[
 O(HN_H)=O(WH/m)=o(W).
\tag{7.3}
\]

The aggregate available hard-band norm over all such tops is

\[
 4L^2N_H=(4-o(1))MN_H=\Theta(W).
\tag{7.4}
\]

Thus the former one-bit (O(W/m)) magnitude obstruction is not a true
static capacity obstruction once multi-swaps are used.  The synchronized
grid has coefficient-scale aggregate magnitude and (O(1)) path pieces,
but only cut-space directions.  The independent port cube has the full
Boolean direction set and even smaller phase duplication, but Theorem 8.1
makes its worst vertices coefficient-one-incompatible as literal
promotion paths.  The remaining gate is therefore a new seam which
changes an ordered-collar signature without paying either an (H)-step
restitution delay or a fresh path initialization.

## 10. Internal audit

The decisive claims were checked independently in the following order.

1. **Integrality.**  Equation (2.6) is an identity in the free integer
   module on cyclic orders.  No rational averaging or cancellation of
   unavailable negative states is used.
2. **Rank isolation.**  Every constituent is an actual adjacent-swap
   square.  Its two exceptional lengths are exactly (r_{ij}) and
   (M-r_{ij}), and (2.9) places only the former in the hard band.
3. **No hidden cancellation.**  The endpoint-block parity signature
   identifies ((i,j)) and proves pairwise disjoint four-mask supports.
4. **Exact owner preservation between signs.**  Equality (3.6) is an
   equality of middle multiplicity vectors, not merely of counts.
5. **Positive physical realization.**  Each term of (3.3) is a literal
   cyclic promotion segment.  The overlap count is paid in actual state
   occurrences.
6. **Hidden splice.**  The entire moved-position support, not merely each
   swap separately, fits in one reserve block.  Hence all four frames have
   identical useful states at the ports counted in (4.3).
7. **Scope of the capacity claim.**  Equation (0.4) is aggregate norm.
   Equation (6.2) explicitly records why it is not an independent
   \(L^2\)-bit zonotope.
8. **Independent static cube.**  Equation (7.14) was checked phasewise:
   all nonendpoint swaps are wholly inside or outside the relevant lower
   interval, and every upper interval contains both row-swap positions.
9. **Cube injectivity.**  Equal-depth cells were separated by the earlier
   right-boundary block, which occurs once in one cell and twice in the
   other.  Thus no cancellation is hidden in (7.11).
10. **Literal obstruction.**  Inequality (8.5) uses only the exact queue
    recurrence (8.2).  It does not assume a particular cyclic-order
    representation between marked states and already permits arbitrary
    choices of the promoted reserve label.

This closes both static capacity questions in one calibrated top:
aggregate and independent rectangle capacity are not limited by owner
duplication.  What remains, and what Theorem 8.1 sharply obstructs for the
displayed cube, is literal low-fragment chronology rather than owner
capacity or integrality.
