# Recursive pair omission: the exact Pascal recurrence and the Gray-seam gate

Date: 2026-07-25

## 0. Outcome

This note audits the proposed recursive pair-omission tower.  It gives an
exact signed-rank recurrence and a physical four-block fusion lemma.  The
recurrence is genuinely useful: it shows that complementation and
first-deviation assignment introduce no hidden rank or ownership error.

It does **not**, by itself, prove the constant-one theorem.  A block-diagonal
recursive lift merely transports the normalized defect of its children.  To
gain anything, almost all child components must be fused.  The correct
physical fusion order is

\[
        0\longrightarrow a\longrightarrow ab\longrightarrow b
        \longrightarrow0,
\]

not (0,a,b,ab).  In the correct order, the two coordinates of the exposed
pair remain fixed for an entire child block.  The remaining theorem is a
long-collar endpoint matching which makes these Gray seams service the
all-singleton Pascal boundary targets.

Throughout, put

\[
 \Omega_m=P_1\sqcup\cdots\sqcup P_m\sqcup\{z\},
 \qquad P_i=\{a_i,b_i\},
\]

and

\[
 N_m(d)=\binom{2m+1}{m+d},
\]

with an out-of-range binomial interpreted as zero.

## 1. Exact first-deviation decomposition

Call a pair singleton in (A\subseteq\Omega_m) when

\[
 |A\cap P_i|=1.
\]

If not every pair is singleton, let (j(A)) be the first nonsingleton
pair.  Before (P_{j(A)}), choose one of the two coordinates of every pair;
there are (2^{j-1}) such oriented singleton prefixes.  At (P_j), the
set is either empty or full.

### Theorem 1.1 -- signed Pascal identity

For every integer (d),

\[
\boxed{
 N_m(d)=E_m(d)+
 \sum_{j=1}^{m}2^{j-1}
 \bigl(N_{m-j}(d+1)+N_{m-j}(d-1)\bigr),}
\tag{1.1}
\]

where

\[
 \boxed{E_m(d)=2^m\bigl({\bf1}_{d=0}+{\bf1}_{d=1}\bigr).}
\tag{1.2}
\]

#### Proof

The exceptional sets have one coordinate from every pair.  There are
(2^m) of them without (z), in rank (m), and (2^m) with (z), in
rank (m+1).

Fix a first nonsingleton index (j), one of the (2^{j-1}) singleton
prefixes, and put (s=m-j).  If (P_j) is empty, deleting the fixed prefix
leaves a set of size

\[
 (m+d)-(j-1)=s+d+1
\]

in a universe of size (2s+1).  If (P_j) is full, deleting the prefix
and (P_j) leaves size

\[
 (m+d)-(j+1)=s+d-1.
\]

The cells are disjoint and exhaust every nonexceptional set.  This proves
(1.1).  \(\square\)

Equivalently, if

\[
 F_m(x)=\sum_dN_m(d)x^d=x^{-m}(1+x)^{2m+1},
\]

then

\[
 F_m(x)=2^m(1+x)+
 \sum_{j=1}^{m}2^{j-1}(x+x^{-1})F_{m-j}(x).
\tag{1.3}
\]

This identity is the exact rank ledger of recursive pair omission.  In
particular, neither sign is lost: empty pairs shift the residual centre by
(+1), and full pairs shift it by (-1).

## 2. Complementation exchanges the signed towers exactly

Let (Q) have size (2r+1), and let

\[
 S_0,S_1,\ldots,S_\ell\in\binom Qr
\]

be a physical two-sided path.  Put (X_i=Q\setminus S_i), so

\[
 |X_i|=r+1.
\]

For every (q\ge0), De Morgan gives

\[
\boxed{
 \bigcap_{h=0}^{q}X_{i+h}
 =Q\setminus\bigcup_{h=0}^{q}S_{i+h},
 \qquad
 \bigcup_{h=0}^{q}X_{i+h}
 =Q\setminus\bigcap_{h=0}^{q}S_{i+h}.}
\tag{2.1}
\]

Thus a local signed depth (+q) becomes global signed depth (-q), and
vice versa.  This is exact and costs no factorability or pin theorem.

More generally, adjoining a fixed prefix (K) commutes with both operations:

\[
 \bigcap_h(K\cup S_h)=K\cup\bigcap_hS_h,
 \qquad
 \bigcup_h(K\cup S_h)=K\cup\bigcup_hS_h.
\tag{2.2}
\]

Consequently every first-deviation cell carries a physical child system
without changing its signed depth.

## 3. Exact recurrence for holes and components without fusion

For a physical path system ({\cal P}_{m,d}) on rank (m+d), let

* (J_{m,d}) be its number of path components;
* (M_{m,d}(q)) be the number of rank-((m+d+q)) targets not represented
  by a consecutive signed-(q) window.

At a first-deviation cell with residual parameter (s=m-j), use a copy of
({\cal P}_{s,d+1}) in the empty branch and a copy of
({\cal P}_{s,d-1}) in the full branch.  Include every exceptional owner
at the centre rank as an isolated path.  Do not make any cross-cell seams.
Call the result ({\cal R}{\cal P}_{m,d}).

### Theorem 3.1 -- block-diagonal defect recurrence

One has

\[
\boxed{
 J({\cal R}{\cal P}_{m,d})
 =E_m(d)+\sum_{j=1}^{m}2^{j-1}
 \bigl(J_{m-j,d+1}+J_{m-j,d-1}\bigr).}
\tag{3.1}
\]

For (q=0), all exceptional centre owners are covered.  For (q\ne0),

\[
\boxed{
 M({\cal R}{\cal P}_{m,d};q)
 =E_m(d+q)+\sum_{j=1}^{m}2^{j-1}
 \bigl(M_{m-j,d+1}(q)+M_{m-j,d-1}(q)\bigr).}
\tag{3.2}
\]

The equality is literal provided each child occurrence ledger is counted
inside its first-deviation cell; in particular, different cells cannot
collide.

#### Proof

Components in distinct cells are disjoint, giving (3.1).  A target in a
nonexceptional cell has the same signed distance (q) from the residual
centre (d+1) or (d-1), by the rank calculation in Theorem 1.1.
Equation (2.2) transports its witness in both directions.  A target with
all pairs singleton belongs to no cell.  Such a target exists only at
absolute offsets zero and one, giving the source (E_m(d+q)).  \(\square\)

For a depth (H), define the literal repair/reset functional

\[
 {\cal L}_{m,d,H}
 =(2H+1)J_{m,d}+
 \sum_{1\le |q|\le H}M_{m,d}(q).
\tag{3.3}
\]

Equations (3.1)--(3.2) give

\[
\boxed{
\begin{aligned}
 {\cal L}({\cal R}{\cal P}_{m,d})
={}&\sum_{j=1}^{m}2^{j-1}
 \bigl({\cal L}_{m-j,d+1,H}+{\cal L}_{m-j,d-1,H}\bigr)\\
&+(2H+1)E_m(d)
 +\sum_{1\le|q|\le H}E_m(d+q).
\end{aligned}}
\tag{3.4}
\]

This is the exact requested signed-hole/component recurrence.

### Consequence 3.2 -- recursion alone is not a contraction

Compare (3.4) with the identical mass recurrence (1.1).  Away from the
exponentially small (E_m)-terms, the normalized cost is a convex average
of the normalized child costs.  A block-diagonal recursive tower therefore
preserves, rather than improves, a positive relative loss.  Cross-cell
fusion is mathematically necessary.

Iterating the recursion all the way to singleton leaves with no seams makes
every centre owner an isolated component.  This is the extreme case
(J=N_m(d)), confirming that first-deviation assignment by itself is not a
constant-one proof.

## 4. The correct four-block physical braid

Expose one pair (P=\{a,b\}), and let (Q) be the remaining universe.
Put (k=s+d), so the parent centre rank is (k+1).  Consider four
oriented physical child paths

\[
 E\subseteq\binom Q{k+1},\quad
 A,B\subseteq\binom Qk,\quad
 D\subseteq\binom Q{k-1}.
\]

Embed them in the order

\[
\boxed{
 E,\qquad \{a\}\cup A,\qquad
 \{a,b\}\cup D,\qquad \{b\}\cup B.}
\tag{4.1}
\]

Suppose the four successive endpoint containments are

\[
 A_{\rm first}\subset E_{\rm last},\qquad
 D_{\rm first}\subset A_{\rm last},
\tag{4.2}
\]

\[
 D_{\rm last}\subset B_{\rm first},\qquad
 B_{\rm last}\subset E_{\rm first}^{\rm next},
\tag{4.3}
\]

each of codimension one.  Then the displayed blocks join by Johnson edges.

### Lemma 4.1 -- long-block Gray fusion is physically valid

Assume every child block has at least (H+1) centre vertices.  At each
seam, assume the residual coordinate exchanged by (4.2)--(4.3) does not
occur in the adjacent (H) child transition supports.  If every child is
already physical through depth (H), then the concatenation (4.1) is
physical through depth (H).

#### Proof

The pair occupancy follows

\[
 0\longrightarrow a\longrightarrow ab\longrightarrow b
 \longrightarrow0.
\]

Hence (a) changes only at the (E/A) and (D/B) seams, which are
separated by the whole (A) and (D) blocks.  Likewise (b) changes only
at the (A/D) and (B/E) seams, separated by the whole (D) and (B)
blocks.  Their residence and nonresidence intervals therefore have length
at least (H+1).

Every residual coordinate used at a seam is protected from another change
for (H) transitions on both adjacent sides by the collar hypothesis.
All other coordinates inherit the child residence property.  This is
exactly the two-sided residence criterion for the consecutive
intersection/union factor, proving the claim.  \(\square\)

The order matters.  The tempting order (0,a,b,ab) toggles both (a) and
(b) after one block boundary and creates length-one runs.  The Gray order
(4.1) is the unique cyclic ordering of the four pair states up to reversal
and rotation, and is the physically correct recursive order.

### Lemma 4.2 -- exact first-shadow seam labels

At an (E\to aA) seam, write

\[
 E_{\rm last}=A_{\rm first}\cup\{u\}.
\]

Then its lower and upper colours are

\[
 E_{\rm last}\cap(\{a\}\cup A_{\rm first})=A_{\rm first},
\tag{4.4}
\]

\[
 E_{\rm last}\cup(\{a\}\cup A_{\rm first})
 =\{a\}\cup E_{\rm last}.
\tag{4.5}
\]

The other three seams have the analogous Pascal labels.  Thus seam
windows are not arbitrary contamination: they are precisely endpoint
members of the adjacent child ranks with the appropriate pair prefix.

This is the local mechanism by which a recursive braid can replace child
endpoint fringes and serve the all-singleton source terms in (3.2).

## 5. Recurrence with useful seams

Let (S_{m,d}) be the number of seams joining distinct child components,
and let (G_{m,d}(q)) be the number of previously uncovered signed-(q)
targets represented by crossing windows at those seams.  If all seams are
physical and the useful targets are chosen distinctly, then

\[
\boxed{
 J_{m,d}^{\rm new}
 =E_m(d)+\sum_{j=1}^{m}2^{j-1}
 (J_{m-j,d+1}+J_{m-j,d-1})-S_{m,d},}
\tag{5.1}
\]

and, for (q\ne0),

\[
\boxed{
\begin{aligned}
 M_{m,d}^{\rm new}(q)
={}&E_m(d+q)+\sum_{j=1}^{m}2^{j-1}
 (M_{m-j,d+1}(q)+M_{m-j,d-1}(q))\\
&-G_{m,d}(q).
\end{aligned}}
\tag{5.2}
\]

Consequently

\[
\boxed{
 {\cal L}^{\rm new}
 ={\cal L}^{\rm block}
 -(2H+1)S_{m,d}
 -\sum_{1\le|q|\le H}G_{m,d}(q).}
\tag{5.3}
\]

Equations (5.1)--(5.3) isolate the only possible gain in the recursive
architecture.  A seam simultaneously lowers reset cost and can pay a
Pascal boundary target.

## 6. Exact remaining recursive theorem

The recursive pair-omission line would prove constant one if one proves a
coherent endpoint-fusion theorem with the following content.

> **Long-collar Gray-seam resolution.**  At every recursive pair node and
> simultaneously for all centre offsets encountered in a fixed Gaussian
> window, orient and match all but (o(W/H)) child components into Gray
> braids (4.1), so that:
>
> 1. the endpoint containments (4.2)--(4.3) hold;
> 2. the exchanged residual coordinates avoid the adjacent (H)-collars;
> 3. the crossing windows supply every all-singleton source target in
>    (3.2), apart from total (o(W)) defect;
> 4. the unmatched component and uncovered-target ledgers, summed through
>    the recursion, are (o(W/H)) and (o(W)), respectively.

The matching at one node is fixed-uniformity: its primitive object is a
four-partite diamond/containment edge joining one component from each of

\[
 \binom Q{k+1},\quad \binom Qk,\quad
 \binom Q{k-1},\quad \binom Qk.
\]

Lemma 4.1 proves that no additional factorability theorem is hidden after
this matching.  What is not yet proved is the simultaneous abundance and
global accounting of such collar-clean endpoint diamonds.

## 7. Why phasewise boundary deletion cannot replace fusion

There is a simple exact loss bound which distinguishes genuine recursive
service from merely cutting every category change.

Let a physical centre path have (B) edges at which its full
first-deviation cell changes (the cell records the oriented singleton
prefix as well as the empty/full first deviation).  A signed-(q) window
whose target cell differs from the cell of its designated centre must cross
one of those edges.
Consequently at most (qB) starts in either orientation are affected, and

\[
 \boxed{
 \sum_{1\le |q|\le H}
 \#\{\hbox{category-mismatched signed-(q) starts}\}
 \le H(H+1)B.}
\tag{7.1}
\]

The bound follows by charging a crossing window to its first category
boundary; a fixed boundary lies in at most (q) length-((q+1)) windows
of one orientation.

For the coarser proved first-avoided pair extraction, which records only
the first avoided pair, the total category-boundary count is

\[
 B=O(W\log ^2m/m).
\tag{7.2}
\]

Thus (7.2) is already the optimistic scale before refining to the full
oriented cells used by the exact recursion.  Even the hypothetical Catalan
improvement (B=O(W/m)) would make (7.1)
of order (WH^2/m).  At the required scale

\[
 H=\sqrt m\,\omega(m),\qquad \omega(m)\to\infty,
\]

this is not (o(W)).  Hence deleting (H)-collars at category boundaries
cannot prove constant one.  The crossing windows must be retained and used
as the Pascal service terms (G_{m,d}(q)) in (5.2).

## 8. Static diamond supply is sufficient

The uncoloured endpoint-containment resource is not sparse.  Let (Q) have
size (n), and form the four-partite hypergraph

\[
 {\cal D}_{n,k}
 \quad\hbox{on}\quad
 \binom Q{k+1}\sqcup\binom Qk_A\sqcup
 \binom Q{k-1}\sqcup\binom Qk_B.
\]

Its edges are labelled Boolean diamonds

\[
 F\subset A,B\subset E,
 \qquad A\ne B,
 \qquad A\cap B=F,\quad A\cup B=E.
\tag{8.1}
\]

The two rank-(k) copies are distinguished.

### Proposition 8.1 -- degree and codegree ledger

The four part-degrees are respectively

\[
\boxed{
 (k+1)k,\qquad k(n-k),\qquad
 (n-k+1)(n-k),\qquad k(n-k).}
\tag{8.2}
\]

Every nonzero pair codegree is at most

\[
 \boxed{\max\{k+1,n-k+1\}=O(n).}
\tag{8.3}
\]

In particular, in a central window (k=n/2+O(\sqrt n)), degrees are
(\Theta(n^2)) and relative codegrees are (O(1/n)).

#### Proof

For fixed (E), choose the ordered deleted coordinates defining (A) and
(B), giving ((k+1)k).  For fixed (F), choose the ordered added
coordinates, giving ((n-k+1)(n-k)).  For fixed (A), choose one deleted
coordinate and one coordinate outside (A), giving (k(n-k)).  The same
holds for (B).

Two vertices in different parts either determine the diamond, leave one
choice of a coordinate in a set of size at most (k+1), or leave one
choice outside a set in a set of size at most (n-k+1).  Vertices in the
same part have codegree zero.  This proves (8.3).  \(\square\)

### Corollary 8.2 -- near-perfect static diamond matching

Uniformly for (|k-n/2|=O_A(\sqrt n)), there is a diamond matching of size

\[
 \boxed{(1-o_A(1))
 \min\left\{\binom n{k-1},\binom nk,\binom n{k+1}\right\}.}
\tag{8.4}
\]

The same conclusion holds if every candidate vertex carries a forbidden
coordinate set of size (o(n)), and a diamond is retained only when its
two exchanged directions avoid all four relevant forbidden sets.

#### Proof

First independently thin each of the three larger parts to the size of the
smallest part.  Use inclusion probabilities equal to the ratio of the
smallest part size to the given part size.  Since a part-degree equals the
total edge count divided by the part size, all four expected surviving
degrees are equal.  Proposition 8.1 gives variance (O(n^3)) against mean
squared (Theta(n^4)).  Deleting the (o(1))-fraction of vertices and
edges with non-typical degree leaves a four-uniform
((1+o(1))D)-regular hypergraph with (D=\Theta_A(n^2)) and maximum
codegree (O(n)=o(D)).  The fixed-uniformity near-perfect matching theorem
then covers all but an (o(1))-fraction of its vertices, proving (8.4).

For the forbidden-coordinate version, a fixed vertex loses only
(O(n\,o(n))=o(n^2)) ordered coordinate pairs.  Thus all degrees change by
(o(D)), while the codegree bound is unchanged.  Apply the same theorem.
\(\square\)

Corollary 8.2 proves that there is no static Hall or collar-capacity
obstruction at one recursive node.  It does **not** yet splice prescribed
child paths.  A path splice consumes oriented child edges, not merely four
compatible states: after deleting one edge from each child component, the
four exposed ends must satisfy the cyclic containments (4.2)--(4.3).  Thus
the remaining object is an alternating-edge diamond matching inside the
four actual child path factors.  Arbitrary state diamonds from (8.4) need
not respect those successor edges.

## 9. A lossless synchronized orientation-cube braid

There is one substantial class of packets for which the successor-edge
alignment can be solved exactly.

Let

\[
 R=\{\{u_1,v_1\},\ldots,\{u_s,v_s\}\}
\]

be disjoint coordinate pairs.  For
\(\epsilon\in\{0,1\}^s\), let \(O(\epsilon)\) contain the selected member
of each pair.  Let \(K\), \(\{x,y,a,b\}\), and all coordinates in \(R\)
be pairwise disjoint.  Define four orientation-cube packets

\[
\begin{aligned}
 E(\epsilon)&=K\cup\{x,y\}\cup O(\epsilon),\\
 A(\epsilon)&=K\cup\{x,a\}\cup O(\epsilon),\\
 D(\epsilon)&=K\cup\{a,b\}\cup O(\epsilon),\\
 B(\epsilon)&=K\cup\{y,b\}\cup O(\epsilon).
\end{aligned}
\tag{9.1}
\]

For every fixed \(\epsilon\), these four sets form the Gray-order Johnson
cycle

\[
 E(\epsilon)-A(\epsilon)-D(\epsilon)-B(\epsilon)-E(\epsilon).
\tag{9.2}
\]

Let

\[
 \epsilon_0,\epsilon_1,\ldots,\epsilon_{L-1},
 \qquad L=2^s,
\]

be a cyclic Gray code of the orientation cube, and let \(c_i\) be the
pair direction flipped from \(\epsilon_i\) to \(\epsilon_{i+1}\).  Assume
its transition run length is \(\rho\): every \(\rho\) consecutive
directions are distinct.

### Theorem 9.1 -- shifted-cut packet fusion

Fix an index \(t\).  Traverse the packets, always in the forward Gray
direction, as follows:

\[
\begin{array}{c|c|c}
\text{packet}&\text{first orientation}&\text{last orientation}\\ \hline
E&\epsilon_{t+1}&\epsilon_t\\
A&\epsilon_t&\epsilon_{t-1}\\
D&\epsilon_{t-1}&\epsilon_{t-2}\\
B&\epsilon_{t-2}&\epsilon_{t-3}.
\end{array}
\tag{9.3}
\]

Each row of (9.3) traverses the whole Gray cycle with one edge cut.  Join
successive packets by the pointwise edges in (9.2).  The result is one
simple Johnson path containing all \(4L\) owners exactly once.

Moreover, for every

\[
 \boxed{H<\min\{\rho,L-1\},}
\tag{9.4}
\]

the path has two-sided coordinate residence greater than \(H\), and hence
is a genuine physical radius-\(H\) MTF/Pascal path.

#### Proof

The last orientation in each row of (9.3) equals the first orientation in
the next row.  Equation (9.2) therefore gives the three cross-packet
Johnson edges.  The four fixed cores in (9.1) are distinct, so packets do
not share an owner; within one packet, the orientation map is injective.

Inside the active pairs \(R\), the transition directions in the first
packet are

\[
 c_{t+1},c_{t+2},\ldots,c_{t-1},
\]

with cyclic indices and with \(c_t\) omitted.  The next packet begins with
\(c_t\), the third begins with \(c_{t-1}\), and the fourth begins with
\(c_{t-2}\).  After deleting the three cross-packet steps, the complete
active-direction list is therefore one consecutive segment of the
periodic word \((c_i)\).  Repeated active directions are separated by at
least \(\rho\) transitions.

The fixed coordinates \(a,b,x,y\) change only at cross-packet seams.  In
the order (9.2), consecutive changes of any one of them are separated by a
whole packet, of length \(L\).  Every coordinate of \(K\) is constant.
Thus every coordinate residence and nonresidence interval has length
greater than \(H\).  The canonical long-residence MTF theorem supplies the
literal radius-\(H\) factor.  \(\square\)

Goddyn--Gvozdjak long-run Gray cycles have

\[
 \rho\ge s-3\log_2s.
\tag{9.5}
\]

Thus choosing \(s=H+\omega(\log H)\) makes Theorem 9.1 applicable, while
one packet has the very large size \(L=2^s\).  The component/reset cost of
a packing of these braids is therefore exponentially below the required
\(W/H\) scale.

The remaining global question is no longer two-port routing inside such a
packet.  It is whether the four relevant Boolean rank systems can be
partitioned, up to (o(W)) owners, into **pointwise diamond quadruples of
orientation subcubes with a common active direction set \(R\)**.  This is a
fixed-four-packet matching problem.  It does not have growing uniformity in
\(H\), although candidate packets themselves have size \(2^s\).

### Corollary 9.2 -- exact packet matching criterion

For each active pair set \(R\), contract every packet

\[
 {\cal C}(R,K)=\{K\cup O(\epsilon):\epsilon\in\{0,1\}^s\}
\tag{9.6}
\]

to one vertex.  On the four adjacent roles, join four packet vertices when
they have the same \(R\) and their cores form the pointwise diamond (9.1).
Call the resulting four-partite hypergraph \({\mathfrak D}_R\).

If, after deleting a family of packets whose total owner mass is \(o(W)\),

1. every \({\mathfrak D}_R\) is \((1+o(1))D_R\)-regular on its four
   surviving parts;
2. \(D_R\to\infty\); and
3. every pair codegree is \(o(D_R)\),

then a fixed-four-uniform matching theorem and Theorem 9.1 give a physical
four-block fusion of all but \(o(W)\) owners.

For a fixed \(R\), if all admissible cores are retained, the degree and
codegree calculations reduce to Proposition 8.1 on the residual coordinate
set:

\[
 \boxed{D_R=\Theta(m^2),\qquad \Delta_2({\mathfrak D}_R)=O(m).}
\tag{9.7}
\]

Thus both the packet uniformity and the normalized codegree are independent
of \(H\):

\[
 \boxed{r_{\rm packet}=4,qquad
 \Delta_2/D_R=O(1/m).}
\tag{9.8}
\]

There is no common-port-label selection left in this synchronized model.
Once four packets share \(R\), the shifted cuts in (9.3) choose compatible
labels deterministically.  The live Hall condition is therefore only the
equitable common-\(R\) packetization in items 1--3 above.

This criterion is deliberately narrower than a matching on arbitrary path
blocks.  For arbitrary blocks, fixed endpoints are false and two arbitrary
ports need not span the block.  Synchronized orientation packets solve
both defects at once, but it remains unproved that the Boolean layers admit
the required near-resolution into common-\(R\) packet diamonds while
retaining the multidepth target ledger.

### Theorem 9.3 -- the packet state graph and cycle-factor expansion

The local packet geometry has an exact product description.  Let
\({\cal K}\) be any family of equal-sized cores, all disjoint from the
support of \(R\), and put an edge between two cores when they are Johnson
adjacent.  The state map

\[
 (C,\epsilon)\longmapsto C\cup O(\epsilon)
 \tag{9.9}
\]

embeds the Cartesian product

\[
 \boxed{J({\cal K})\mathbin\square Q_s}
 \tag{9.10}
\]

in the Johnson graph.  Horizontal edges flip one active pair and vertical
edges exchange one core coordinate while keeping the orientation label
fixed.

Let

\[
 C_0,C_1,\ldots,C_{\ell-1}
 \tag{9.11}
\]

be a simple core path.  In packet \(i\), cut the fixed cyclic Gray code at
edge \(c_{t-i}\), and traverse forward from
\(\epsilon_{t-i+1}\) to \(\epsilon_{t-i}\).  The last label in packet
\(i\) is exactly the first label in packet \(i+1\).  Joining them by the
vertical edge in (9.10) gives one simple Johnson path on all
\(\ell2^s\) owners.  If

\[
 H<\min\{\rho,2^s-1\},
 \tag{9.12}
\]

this expanded path is physical through depth \(H\).

Consequently, let packet vertices be divided into cyclic role classes
\({\cal P}_0,\ldots,{\cal P}_{r-1}\), and for every \(i\) let \(G_i\)
be a bipartite graph from \({\cal P}_i\) to \({\cal P}_{i+1}\).  An edge
is legal precisely when its two packets

1. have the same active pair set \(R\); and
2. have Johnson-adjacent cores in the role-prescribed direction.

If each \(G_i\) has a one-factor, the union of the chosen one-factors is a
disjoint union of packet cycles.  Delete one seam in each cycle and apply
the preceding expansion.  This gives one physical owner path per packet
cycle.  In particular, the common-label problem is exactly absent: the
cut indices are propagated deterministically by

\[
 t_{i+1}=t_i-1\pmod {2^s}.
 \tag{9.13}
\]

#### Proof

Both kinds of edge in (9.10) change exactly one element of the represented
set.  Distinct pairs \((C,\epsilon)\) represent distinct sets, proving the
embedding.  The endpoint equality follows directly from the chosen cuts.
The active transition directions in consecutive packets concatenate to a
single interval of the periodic transition word \((c_j)\), with vertical
core exchanges inserted between packets.  Hence repetitions of an active
coordinate are at least \(\rho\) steps apart.  A core coordinate can change
only at a vertical seam, and two such seams are separated by an entire
packet of \(2^s\) states.  This proves (9.12).  The cycle-factor statement
then follows component by component.  \(\square\)

The exact Hall condition for selecting every local seam is therefore only

\[
 \boxed{|N_{G_i}({\cal X})|\ge |{\cal X}|
 \quad({\cal X}\subseteq{\cal P}_i),\quad 0\le i<r.}
 \tag{9.14}
\]

There is no growing-\(H\) hyperedge and no auxiliary port-label matching.
If a seam graph is completed to a regular bipartite multigraph by dummy
edges, choose a one-factor and then omit its selected dummy edges.  The
remaining packet graph has maximum degree two and hence is a union of paths
and cycles; Theorem 9.3 expands every component.  A dummy edge therefore
costs at most one extra component, not a packet of owners.  If \(D_i\) is
the regularized degree and \(B_i\) dummy edges were added, a uniformly
chosen one-factor uses \(B_i/D_i\) dummy edges in expectation.  Thus some
choice has total additional component cost at most

\[
 \boxed{\sum_i B_i/D_i.}
 \tag{9.15}
\]

This answers the common-label selection question: it reduces to ordinary
bipartite one-factors with the explicit dummy ledger (9.15).

There is one further global ledger which Hall alone does not control.  Let
the four chosen seam one-factors be regarded as bijections

\[
 \phi_i:{\cal P}_i\longrightarrow{\cal P}_{i+1}
 \qquad(i\in\mathbb Z_4).
 \tag{9.15a}
\]

Their union has exactly as many packet cycles as the permutation

\[
 \boxed{
 \pi=\phi_3\phi_2\phi_1\phi_0
 \quad\hbox{on }{\cal P}_0
 }
 \tag{9.15b}
\]

has cycles.  With full packets of size \(2^s\gg H\), even the trivial
bound \(\#\mathrm{cyc}(\pi)\le W/2^s=o(W/H)\) is enough.  At the critical
profile-changing scale identified in Theorem 10.3, however, blocks have
size \(b=\Theta(H)\) and their number is \(J=\Theta(W/H)\).  Then the exact
cycle-factor requirement is

\[
 \boxed{\#\mathrm{cyc}(\pi)=o(J).}
 \tag{9.15c}
\]

Thus ordinary Hall plus arbitrary one-factors is not quite sufficient at
critical block length: the selected factors must compose to a low-cycle
permutation.  Equivalently, after fixing three seam factors, the fourth
seam graph (transported back to \({\cal P}_0\)) must contain a cycle cover
with \(o(J)\) cycles.  A Hamilton cycle is more than sufficient.  Selected
dummy edges simply cut these cycles and add at most their number to the
component ledger, as in (9.15).

### Proposition 9.4 -- the exact face-load dictionary

The packet fusion theorem settles physicality, but not by itself the
multidepth shadow ledger.  The latter has a particularly sharp description.
For a cyclic start \(j\) and \(1\le q\le H\), put

\[
 D_j(q)=\{c_j,c_{j+1},\ldots,c_{j+q-1}\}.
 \tag{9.16}
\]

The long-run hypothesis makes these \(q\) directions distinct.  The lower
and upper signed targets of the \(q+1\) consecutive packet states beginning
at \(\epsilon_j\) are respectively

\[
\boxed{
\begin{aligned}
 L_j(q)&=C\cup
 O(\epsilon_j)\big|_{[s]\setminus D_j(q)},\\
 U_j(q)&=C\cup
 O(\epsilon_j)\big|_{[s]\setminus D_j(q)}
 \cup\bigcup_{h\in D_j(q)}\{u_h,v_h\}.
\end{aligned}}
\tag{9.17}
\]

Thus both targets are determined by the same \(q\)-face of \(Q_s\): its
free directions are \(D_j(q)\), and its fixed outside orientation is that
of \(\epsilon_j\).  Two cyclic starts give the same lower target if and
only if they traverse the same \(q\)-face; the same equivalence holds for
the upper targets.  Hence the lower and upper multiplicity histograms inside
one packet are identical and equal to the visit histogram of length-\(q\)
Gray segments on \(q\)-faces.

#### Proof

Each direction in \(D_j(q)\) is flipped exactly once in the segment.  Its
two coordinates therefore have empty intersection and full union.  Every
other active pair keeps its initial selected coordinate throughout.  This
is (9.17).  Since \(C\) and \(R\) are fixed, either target recovers both the
free-direction set and every fixed outside orientation, proving the
collision assertion.  \(\square\)

There are

\[
 F_{s,q}=2^{s-q}\binom{s}{q}
 \tag{9.18}
\]

available \(q\)-faces and \(2^s\) cyclic starts.  Therefore any packet
whose depth-\(q\) multiplicities are bounded by \(c_q\) must satisfy the
necessary capacity inequality

\[
 \boxed{2^q\le c_q\binom{s}{q}.}
 \tag{9.19}
\]

This exposes a constraint hidden by residence alone.  If \(c_q=O(1)\) and
\(q=\alpha s\), (9.19) asymptotically requires

\[
 h_2(\alpha)\ge\alpha.
 \tag{9.20}
\]

The equality root is \(\alpha_0\approx0.7729\).  Thus taking merely
\(s=H+o(H)\) cannot give balanced depth-\(H\) shadows even though it gives
physical residence.  One needs at least

\[
 s\ge(\alpha_0^{-1}+o(1))H\approx1.294H
 \tag{9.21}
\]

in the bounded-quota regime; \(s=2H\) safely clears this purely local
capacity barrier.

Deleting one Gray edge to linearize a packet loses at most \(q\) cyclic
starts at depth \(q\).  Across a packetization of \(W\) owners this costs at
most

\[
 \frac{W}{2^s}\sum_{q\le H}q
 =O\!\left(WH^2/2^s\right)=o(W).
 \tag{9.22}
\]

Accordingly the remaining constant-one theorem in this lane has two, and
only two, global clauses:

* near-resolve the middle owners into common-\(R\) orientation packets and
  satisfy the ordinary Hall conditions (9.14); and
* choose the packet Gray cycles/packet assignment so that the aggregate
  \(q\)-face visit histograms from (9.17), simultaneously for
  \(q\le H\), have total balanced excess \(o(W)\).

The first clause is a fixed-uniformity packet-factor problem.  The second
is the genuine multidepth colour problem; physical ports and common labels
are no longer part of it.

## 10. A canonical packetization eliminates the fusion gate entirely

There is an exact global orientation-cube partition which makes the first
clause above unnecessary.  Fix once and for all

\[
 [2m+1]=P_1\sqcup\cdots\sqcup P_m\sqcup\{z\},
 \qquad |P_i|=2.
 \tag{10.1}
\]

For a middle set \(X\), record the pair indices on which \(X\) is full,
empty, or singleton.  Fix disjoint index sets \(F,E\subseteq[m]\) and a
bit \(\delta\in\{0,1\}\) satisfying

\[
 2|F|+|R|+\delta=m,
 \qquad R=[m]\setminus(F\cup E).
 \tag{10.2}
\]

Let \({\cal C}(F,E,\delta)\) consist of all middle sets which are full on
\(F\), empty on \(E\), singleton on \(R\), and contain \(z\) precisely
when \(\delta=1\).  It is an orientation packet of dimension \(|R|\).

### Theorem 10.1 -- exact middle-layer cube partition

The nonempty packets \({\cal C}(F,E,\delta)\) partition
\(\binom{[2m+1]}m\).  Their number is at most \(2\cdot3^m\), and a packet
of dimension \(s\) has exactly \(2^s\) owners.

For every \(S=o(m/\log m)\), the total owner mass in packets of dimension
at most \(S\) is

\[
 \boxed{
 B_{\le S}\le 2(S+1)2^m m^S=o(W/H)
 }
 \tag{10.3}
\]

whenever \(H\le S=O(H)\) and \(H\log m=o(m)\).

Hence, choose any fixed \(\kappa>1\), put \(S=\lceil\kappa H\rceil\),
emit the \(B_{\le S}\) exceptional owners separately, and on every other
packet use a long-run Gray Hamilton path.  For large \(m\), its run length
is greater than \(H\).  The resulting exact middle-owner path partition
has at most

\[
 \boxed{2\cdot3^m+B_{\le S}=o(W/H)}
 \tag{10.4}
\]

components and is physical through depth \(H\).

#### Proof

The pair-status pattern and the orientation on its singleton pairs recover
each middle set uniquely, proving the partition and packet size.  There are
at most three statuses per pair and two choices of \(\delta\), giving the
packet count.

For fixed \(s\), choose the singleton pair indices, their orientations,
and then the full pair indices among the remaining pairs.  Ignoring the
rank constraint only enlarges the count, and gives

\[
 2\binom ms2^s2^{m-s}=2^{m+1}\binom ms.
\]

Summing and using \(\binom ms\le m^S\) proves the first inequality in
(10.3).  Since
\(W=\Theta(4^m/\sqrt m)\), the final asymptotic follows.  The long-run
Gray theorem gives run at least \(s-3\log_2s>H\) for
\(s>\kappa H\).  Finally \(3^m=o(4^m/(H\sqrt m))\), proving (10.4).
\(\square\)

This theorem is important conceptually: neither recursive four-block
fusion nor a packet Hall theorem is needed to make the middle path system
physical at width-scale cost.  The entire remaining obstruction is now
the shadow-colour ledger of these already integral packets.

### Proposition 10.2 -- exact incidence of packet faces with Boolean targets

Let a lower target \(T\) of rank \(m-q\) have pair-status classes
\((F_T,E_T,R_T)\) and \(z\)-bit \(\delta\).  Then

\[
 |E_T|-|F_T|-\delta=q.
 \tag{10.5}
\]

For every \(D\in\binom{E_T}{q}\), there is exactly one middle packet

\[
 \boxed{
 {\cal C}\bigl(F_T,E_T\setminus D,\delta\bigr),
 \qquad\text{active set }R_T\cup D,
 }
 \tag{10.6}
\]

and exactly one \(q\)-face of that packet whose lower target is \(T\).
These are all the packet faces producing \(T\).  Thus the lower target has
packet-face degree

\[
 \boxed{\deg_-(T)=\binom{|E_T|}{q}.}
 \tag{10.7}
\]

Dually, an upper target \(T\) of rank \(m+q\) satisfies

\[
 |F_T|-|E_T|+\delta=q
 \tag{10.8}
\]

and has one producing packet face for each
\(D\in\binom{F_T}{q}\), hence

\[
 \boxed{\deg_+(T)=\binom{|F_T|}{q}.}
 \tag{10.9}
\]

#### Proof

For (10.5), subtract
\(2|F_T|+|R_T|+\delta=m-q\) from
\(|F_T|+|E_T|+|R_T|=m\).  If \(D\subseteq E_T\), promote exactly those
empty pairs to active singleton pairs.  The resulting packet lies in the
middle rank, and the face which frees the directions \(D\) while fixing
the orientations on \(R_T\) has intersection exactly \(T\).  Conversely,
every producing middle packet must promote precisely \(q\) empty pairs,
so it arises uniquely in this way.  Complementation proves the upper
statement.  \(\square\)

The tempting next step would be to choose the Gray cycles so that these
packet faces cover almost every target.  That step is in fact impossible
at square-root depth.  The obstruction is an exact profile-capacity
imbalance, not a defect of a particular Gray code.

### Theorem 10.3 -- fixed-pair packets have a square-root profile obstruction

Fix \(A>0\) and put \(q=\lfloor A\sqrt m\rfloor\).  Any path system whose
edges and all but \(o(W)\) of its depth-\(q\) windows remain inside the
packets of Theorem 10.1 misses \(\Omega_A(W)\) lower rank-
\((m-q)\) targets.  This holds even if one may choose an arbitrary ordering
inside every packet; in particular it holds for every choice of Gray
cycles.

#### Proof

Fix the \(z\)-bit \(\delta\).  A lower target profile is determined by the
number \(f\) of full pairs; it then has

\[
 e=f+q+\delta,
 \qquad r=m-2f-q-\delta
 \tag{10.10}
\]

empty and singleton pairs.  The number of targets with this profile is

\[
 T_{f,\delta}
 =\frac{m!}{f!e!r!}\cdot2^r.
 \tag{10.11}
\]

Every internal producing window must lie in one of the source packets in
(10.6).  The total number of middle starts in all those source packets is

\[
 S_{f,\delta}
 =\frac{m!}{f!(f+\delta)!(r+q)!}\cdot2^{r+q}.
 \tag{10.12}
\]

Consequently, regardless of how the packet owners are ordered, at most
\(S_{f,\delta}\) distinct targets of this profile can be represented.  The
exact capacity ratio is

\[
 \boxed{
 \Lambda_{f,\delta}
 :=\frac{S_{f,\delta}}{T_{f,\delta}}
 =2^q\frac{\binom{f+q+\delta}{q}}
                 {\binom{r+q}{q}}.
 }
 \tag{10.13}
\]

Stirling's formula gives the following local limit.  Put

\[
 f_*=\frac m4-\frac q2+\frac{q^2}{4m}+O(1).
 \tag{10.14}
\]

For a uniformly chosen target (with either fixed value of \(\delta\)),

\[
 Z_m=\frac{4(f-f_*)}{\sqrt m}
 \Longrightarrow Z\sim N(0,1),
 \tag{10.15}
\]

and, uniformly for bounded \(Z_m\),

\[
 \boxed{\log\Lambda_{f,\delta}=-A^2+2AZ_m+o(1).}
 \tag{10.16}
\]

Indeed, the second derivative of \(\log T_{f,\delta}\) at its mode is
\(-16/m+o(1/m)\), and expanding the logarithm of (10.13) gives (10.16).
Consequently the normalized unavoidable profile deficit has the explicit
positive limit

\[
\begin{aligned}
 \Delta(A)
 &:={\mathbb E}\bigl(1-e^{-A^2+2AZ}\bigr)_+\\
 &=\Phi(A/2)-e^{A^2}\Phi(-3A/2)>0,
\end{aligned}
\tag{10.17}
\]

where \(\Phi\) is the standard normal distribution function.  Hence

\[
 \sum_f(T_{f,\delta}-S_{f,\delta})_+
 =(\Delta(A)+o(1))\sum_fT_{f,\delta}
 =\Omega_A(W).
 \tag{10.18}
\]

Finally, a depth-\(q\) window not internal to a packet must begin within
\(q\) positions of a packet seam.  Under the hypothesis there are only
\(o(W)\) such windows.  In particular, the canonical traversal with each
packet contiguous has at most \(2\cdot3^m\) seams and hence only
\(O(q3^m)=o(W)\) crossing windows.  They cannot repair (10.18).
\(\square\)

Thus the canonical packetization is a useful exact physical scaffold but
not a constant-one construction.  It proves something sharper about the
remaining gate: a successful argument must transport a linear number of
square-root-depth windows **between different pair-status profiles**.
Fusion cannot be used merely to reduce the component count; it must perform
macroscopic vertical target service.  This agrees with the boundary charge
warning in Section 7 and rules out any recursion which treats packet seams
as only an \(o(W)\) perturbation.

More quantitatively, each seam creates at most \(q\) new depth-\(q\)
windows.  Equation (10.18) therefore forces

\[
 \boxed{\Omega_A(W/q)=\Omega_A(W/H)}
 \tag{10.19}
\]

genuine profile-changing seams at \(q=\lfloor A\sqrt m\rfloor\).  This is
exactly the critical seam density: a construction in which all blocks have
length \(\omega(H)\) is too sparse, even if its reset cost is negligible.
A positive construction needs a linear share of its owners separated by
profile-changing gaps of average length \(O(H)\), and must fuse essentially
all of those boundaries, so that the crossing windows themselves supply a
linear part of the shadow band.

## 11. Verdict

The recursive proposal is mathematically sound up to one sharply stated
fusion theorem.

* The signed rank shifts are exact.
* Prefix cells have disjoint owners and disjoint target ledgers.
* Complementation exchanges lower and upper flags exactly.
* The correct four-block order is physically valid with long collars.
* The complete hole/component recurrence is (5.1)--(5.3).

But the recurrence also proves that recursion without fusion has no
asymptotic contraction.  The live constant-one problem in this lane is the
long-collar Gray-seam resolution, not another rankwise balancing or
first-avoided assignment.
