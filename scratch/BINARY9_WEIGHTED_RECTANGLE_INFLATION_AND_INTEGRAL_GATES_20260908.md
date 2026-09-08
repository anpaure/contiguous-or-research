# Binary-nine weighted rectangle inflation and integral gates

Date: 2026-09-08. Author: direct_route. Status: proved analytically; full-file
root review passed. Sections 1--4 and 6--7 passed cover_selectors' independent
full read, including the literal A.24 overhead, strict-prototype interface,
mixed-sign support constraints, and exact vertical-anchor catalogue;
Section 5 passed root's full analytical read; its forced matching and coordinate
balance were also used and independently checked in the finite inventories.
The short-only dual below
was independently derived by cover_selectors and checked by direct_route.
No computation is used here.

This note records a sufficient finite certificate for a strict improvement
of the accepted nine-factor compiler. It does **not** assert that a finite
certificate of cost at most 279 has been found.

## 1. Finite certificate and exact inflation ledger

Identify the Boolean nine-cube with subsets of a fixed nine-element set
\(E\). An axis-support rectangle consists of a partition
\(E=A\sqcup B\), with \(1\le |A|,|B|\le8\), and two nonempty strict
inclusion chains
\[
 C=(C_1\subsetneq\cdots\subsetneq C_c)\subseteq2^A,
 \qquad
 D=(D_1\subsetneq\cdots\subsetneq D_d)\subseteq2^B.
\]
Its targets are all \(C_i\cup D_j\). Chains need not be saturated, begin
at the empty set, or end at their whole support. A bank is a finite indexed
family of such rectangles covering **all 512** Boolean targets. Its cost is
\[
                         K=\sum_{\text{rows}}(c+d).                 \tag{1}
\]
Repeated targets and repeated indexed rows remain charged.

**Theorem 1.** For every positive integer \(s\), such a bank gives an
actual paired-chain cover of \([2s]^9\) with principal charge exactly
\(K s^8\). Its literal local OR-word compiler has length at most
\[
                              K s^8+O_{\rm bank}(s^7).              \tag{2}
\]
The same statement holds after replacing the nine index chains by nine
strict set chains of length \(2s\) on disjoint physical supports.

Here and below \([m]=\{0,\ldots,m-1\}\). To prove the theorem, replace
each Boolean point on a \(p\)-axis shore by its cell in \([2s]^p\):
the bit zero selects \([s]\), and bit one selects \(s+[s]\).
The general chain-inflation lemma in
`GRID_CHAIN_INFLATION_FOR_ASYMMETRIC_STAIRCASE_20260908.md` partitions the
union of the \(c\) cells along any strict Boolean chain into exactly
\(s^{p-1}\) increasing chains, with total membership \(c s^p\).
Its arbitrary-comparability extension is relevant here: a skipped Boolean
rank is allowed, and the joins between cells need not be saturated.

For completeness, a cell has \(s^{p-1}\) routes from any chosen entry
face to any chosen exit face. Equal entry and exit axes use straight
lines. Different axes use the two-dimensional hooks
\[
 (0,j),\ldots,(s-1-j,j),(s-1-j,j+1),\ldots,(s-1-j,s-1),
 \qquad 0\le j<s,
\]
tensored by fixed values in the other coordinates. Each entry and exit
face is met exactly once. Across a comparable macro jump \(x<y\), choose
an axis \(a\) with \(y_a>x_a\), exit its maximum face and enter its minimum
face, matching the other residual coordinates. The coordinate difference
in axis \(a\) is
\(s(y_a-x_a)-(s-1)\ge1\), and all other differences are nonnegative.
Thus every route is an actual increasing chain. A one-cell macro chain
uses straight routes. This proves the asserted count and membership.

Apply this separately to the two shores of a row, writing
\(p=|A|\), \(q=|B|\), so \(p+q=9\). The resulting families have
\[
 R=s^{p-1},\quad V=c s^p,
 \qquad S=s^{q-1},\quad Z=d s^q.
\]
Every pair of one left and one right chain is retained. Their principal
charge is exactly
\[
                       SV+RZ=(c+d)s^8.                             \tag{3}
\]
Orient the row so that the smaller-dimensional shore is on the right;
then \(q\le4\). The accepted literal compiler (MASTER_HANDOFF A.24) has
length at most
\[
 SV+RZ+2RS+Z+S
 =(c+d)s^8+2s^7+d s^q+s^{q-1}.                                  \tag{4}
\]
This orientation is necessary for the claimed overhead: it prevents an
eight-dimensional right membership term from contributing another
order-\(s^8\) charge. Summing finitely many rows proves (2). Concatenation
preserves all ordinary interval witnesses inside each row; any fixed
number of additional joining letters is also absorbed in the overhead.
The cell cover follows from the all-cube Boolean cover, and taking unions
along disjoint strict physical input chains preserves strictness.

Writing the equal input length as \(a=2s\), the principal coefficient is
\[
                      \kappa=K/256,
 \qquad \alpha=35/32=280/256.                                   \tag{5}
\]
Consequently **any verified all-cube bank with \(K\le279\)** satisfies
the actual equal-prototype hypothesis of
`STRICT_EQUAL_PROTOTYPE_TO_UNCONDITIONAL_C9_GAIN_20260908.md`.
That already proved transfer theorem supplies a strict unconditional
decrease below the accepted coefficient \(c_9\). This implication keeps
the bank and all constants fixed before taking the outer asymptotic limit;
it does not infer an improvement merely from a fractional cover or from
middle-rank coverage.

## 2. Forest dual and the universal integral lower bound 278

For one rectangle form a bipartite graph whose vertices are the \(c\)
members of \(C\) and the \(d\) members of \(D\). Join \(C_i\) to
\(D_j\) when \(|C_i|+|D_j|\in\{4,5\}\). Its edges are exactly the
row's critical targets, with no repetitions inside the row. Write their
number as \(f=f_4+f_5\).

Each vertex has degree at most two: counterpart chain ranks are strictly
increasing, and only the two specified sums are possible. At a degree-two
vertex one incident edge has sum four and the other sum five. A cycle
would therefore alternate these sums. Traverse a sum-four edge from a
left vertex to a right vertex, then a sum-five edge to the next left
vertex. The left rank increases by one. Continuing around the purported
cycle is impossible. The graph is a forest, and hence
\[
                              f\le c+d-1.                         \tag{6}
\]
Equality holds precisely when the whole bipartite graph is a spanning
path. In particular it implies \(|c-d|\le1\), and both chains have
consecutive rank sets. Indeed, successive left vertices along the path
have ranks differing by one, consistently in the same direction; the
same is true on the right. These are useful necessary structural
conditions on a row attaining equality in (6).

The support bounds give \(c+d\le(p+1)+(q+1)=11\), so each rectangle
contains at most ten critical targets. The two critical ranks contain
\(\binom94+\binom95=252\) targets. A cover with \(b\) rows therefore
satisfies
\[
                    b\ge26,\qquad K\ge252+b\ge278.               \tag{7}
\]
These inequalities apply to arbitrary strict axis-support rectangles,
including truncated and nonsaturated chains.

The small remaining integral cases are particularly rigid. If \(K=278\),
there are exactly 26 rows, both critical ranks are covered exactly once,
and every row attains (6). If \(K=279\), either there are 27 rows with
these same two exactness properties, or there are 26 rows and one of the
following happens: all rows attain (6) and there is exactly one extra
critical occurrence; or both critical ranks are exact and the sum of the
row deficits \((c+d)-f\) is 27, so one row has deficit two and all others
have deficit one. These alternatives exhaust the possibilities.

## 3. Why a fractional rank obstruction cannot settle the gate

Uniformly average all full prefix rectangles with support dimensions
four and five, and give them total fractional row weight \(126/5\).
Every such row has rank counts
\[
                      (1,2,3,4,5,5,4,3,2,1).
\]
Coordinate symmetry makes the load constant on each rank. The critical
loads are one, and the other loads are at least one. This is therefore
an all-cube fractional cover of total cost
\[
                              11(126/5)=1386/5=277.2.              \tag{8}
\]
Conversely give every rank-four or rank-five target weight \(11/10\)
and all other targets weight zero. For any rectangle, (6) and
\(c+d\le11\) give
\[
              (11/10)f\le (11/10)(c+d-1)\le c+d.
\]
This is a feasible fractional-cover dual of value \(252(11/10)=277.2\).
Thus the full fractional optimum is exactly 277.2. Any exclusion of
integral costs 278 or 279 needs additional integral structure; it cannot
come from an ordinary weighted-target fractional-cover dual.

## 4. An exact obstruction to replacing only old short rectangles

Start from an eight-axis bank of fourteen full four-by-four prefix rows
whose ranks three, four, and five are each exact. The literal bank in
MASTER_HANDOFF A.7.1 has this property. Adjoin a new bit \(z\) to either
shore of a row and split the resulting product of a five-member chain
and a two-member chain by its two-chain SCD. The short chain has four
members and is constantly \(z=0\) or constantly \(z=1\), according to
the chosen hook orientation. Pairing it with the unabsorbed five-member
chain gives a rectangle of cost nine and eight critical targets.

Choose any \(m\) distinct old rows and one such short rectangle from
each, with hook orientations and absorbed shores allowed to vary. Let
\(P\) be the union of their critical targets. These targets are disjoint,
so \(|P|=8m\). Call a target hard if it is rank five with \(z=0\), or
rank four with \(z=1\). Each chosen short has exactly four hard targets.

There is no pair \(B,B\cup\{z\}\) in \(P\) with \(|B|=4\):
both would project to the same middle target of the eight-axis bank,
which belongs to only one old row, whereas the selected short in that
row has constant \(z\). This remains true with mixed orientations.

Give each member of \(P\) weight one, plus an additional quarter if it
is hard; give all other targets weight zero. The total weight is \(9m\).
Consider any arbitrary replacement axis-support rectangle, and keep in
its critical forest only those edges corresponding to targets in \(P\).
Every nontrivial component has constant \(z\). In fact, adjacent edges
share a chain member, so their targets differ by a single coordinate;
if that coordinate were \(z\), they would form the forbidden pair above.

Within such a component, the hard targets project to rank three or rank
five on the other eight coordinates. A product of two strict chains on
disjoint supports totaling eight has at most four targets at either
rank: the possible intersection ranks with one support have at most
\(\min(k+1,8-k+1)=4\) values for \(k=3,5\). Consequently a component
with \(e\) edges contains at most four hard edges and has weight at most
\(e+1\), its number of vertices. Sum over all components, including
isolated vertices if desired. The replacement rectangle's supported
weight is at most \(c+d\).

**Theorem 2 (short-only dual).** Any collection of arbitrary
axis-support rectangles covering \(P\) has total cost at least \(9m\).
It may cover other targets as well. In particular, no replacement of
only a selected pool of the old short rectangles can yield a saving,
even after mixing hook orientations or allowing truncated chains.

A whole old packet contains both its long and short rectangles and
introduces forbidden vertical pairs into \(P\). Thus this theorem does
not exclude a trade involving one whole packet and additional shorts.

## 5. A useful necessary balance for the uniform-z-one packet trade

The following condition is independent of all newly chosen chain
orders. Suppose one whole old packet and four other short rectangles
with \(z=1\) are to be replaced, with exact critical coverage, by five
full four-by-five prefix rectangles. Write the old packet's middle path
on eight coordinates as
\[
 B_0,U_1,B_1,U_2,B_2,U_3,B_3,U_4,B_4,
 \quad |B_i|=4,\ |U_i|=5,
 \quad U_i=B_{i-1}\cup B_i.
\]
The no-z rank-four/rank-five totals are five and four. In a full row,
their difference is one exactly when \(z\) is on its five-axis shore,
and zero when it is on its four-axis shore. Thus there is exactly one
of the former and four of the latter. Each full row has at least one
no-z rank-four target; their total five forces \(z\) to be first on its
shore in every replacement row. The four \(U_i\) must be matched to
four different \(B_i\), leaving a root \(B_j\); the path has precisely
one such matching for each choice of root, directed away from that root.

Project the z-present critical targets to ranks three and four on eight
coordinates. The packet gives one balanced four-by-four row, whose
coordinate incidence difference (rank four minus rank three) is one on
every coordinate. A short rectangle contributes the indicator of its
longer four-axis varying support. The new rows project to one balanced
four-by-four row and four shorts whose longer supports are exactly the
matched vertices \(B_i\), \(i\ne j\). If \(L_1,\ldots,L_4\) are the
four old shorts' longer supports, a necessary condition is therefore
\[
                 \sum_{k=1}^4\mathbf1_{L_k}
                     =\sum_{i\ne j}\mathbf1_{B_i}.                \tag{9}
\]
For a full old row with orders \((a_1,\ldots,a_4)\) and
\((b_1,\ldots,b_4)\), take
\(B_i=\{a_1,\ldots,a_i,b_1,\ldots,b_{4-i}\}\).
The four new shorts' forbidden coordinates are exactly the elements of
\(B_j\): the left-of-root edges exclude \(a_1,\ldots,a_j\), and the
right-of-root edges exclude \(b_1,\ldots,b_{4-j}\). These conditions
prune a finite search but are not asserted to be sufficient for either
critical coverage or full-cube coverage.

## 6. Mixed hook signs: support, position, and endpoint certificates

Consider the same cost-56 source consisting of one whole packet, with
owner \(o\), and one short from each of four distinct other old rows.
The absorbed shore may be chosen separately in each row. Let \(J_k\)
be the unabsorbed four-axis support of short \(k\), and let \(n_0\) be
the number of selected shorts with \(z=0\). Suppose five full four-by-five
prefix rows replace this source with exact critical coverage. Denote their
longer, five-axis supports by \(L_1,\ldots,L_5\).

For a family of critical targets, take the coordinate incidence vector
on rank five minus the corresponding vector on rank four. A full
four-by-five row contributes \(\mathbf1_L\), where \(L\) is its longer
support: matching the five rank-four cells with the five rank-five cells
along the shorter chain adds each longer-shore coordinate exactly once.
The whole old packet contributes \(\mathbf1_E\). Each old short
contributes \(\mathbf1_{J_k}\), regardless of hook sign. For the zero
hook its first absorbed coordinate is fixed present; for the one hook
\(z\) is fixed present. In either case the critical counts are four and
four, so fixed-present coordinates have difference zero, and the same
cell matching adds precisely the four unabsorbed coordinates. Hence
\[
           \sum_{h=1}^5\mathbf1_{L_h}
                   =\mathbf1_E+\sum_{k=1}^4\mathbf1_{J_k}.          \tag{10}
\]
Its \(z\) coordinate is one. **Exactly one** new row therefore has
\(z\) on its five-axis shore; the other four have it on their four-axis
shores. In particular every ordinary coordinate occurs on at least one
of the five longer supports; a coordinate belonging to all four \(J_k\)
belongs to all five longer supports.

Let \(p_h\) be the one-based position of \(z\) in row \(h\). A full
row contributes \(p_h\) no-z rank-four targets. Its no-z rank-five count
is \(p_h-1\) when its z-shore has five axes, and \(p_h\) otherwise.
The source's no-z rank-four count is \(5+4n_0\). Thus
\[
             \sum_{h=1}^5p_h=5+4n_0,
             \qquad \sum_{h=1}^5(p_h-1)=4n_0.                      \tag{11}
\]
For \(n_0=0\), every position is one. For \(n_0=4\), every position
is its maximum: five in the unique z-long row and four in the others.
For intermediate signs, (11) is an exact bounded integer constraint,
with one variable in \(\{1,\ldots,5\}\) and four in
\(\{1,\ldots,4\}\).

There is a smaller necessary certificate using just owner and subset
data. Every full row contains both its whole longer shore \(L\), a
rank-five target, and its complementary whole shorter shore \(E\setminus
L\), a rank-four target. Both must belong to the source critical pool.
Moreover, the five \(L\)'s are distinct because the new critical deck
is exact.

On the fourteen base-row owners define a directed multigraph as follows.
For each base rank-five target \(U\subseteq E\setminus\{z\}\), draw
an edge from the row owning \(U\) to the row owning its eight-coordinate
complement, a rank-three target. Exactness of the base ranks gives
outdegree four and indegree four at every owner. There are no loops:
if a prefix union and its complement both belong to one four-by-four
row, each shore's prefix must be either empty or whole. Such a union
cannot have rank three or five.

Let
\[
 S_0=\{o\}\cup\{\text{owners of selected zero-hook shorts}\},
 \qquad
 S_1=\{o\}\cup\{\text{owners of selected one-hook shorts}\}.
\]
A zero-hook short includes all four rank-five targets of its old row;
a one-hook short includes all four rank-three targets of its old row
after deleting \(z\). Therefore the four new longer supports avoiding
\(z\) must be four distinct directed edges
\[
                         U_1,U_2,U_3,U_4:S_0\longrightarrow S_1.   \tag{12}
\]
In particular there must be at least four edges across this directed
owner cut. In the uniform-one case all four outgoing edges of \(o\)
must be available; in the uniform-zero case all four incoming edges
must be available. No self-edge can be used in either case.

Once these four \(U_h\) have been selected, (10) forces the remaining
longer support to be \(\{z\}\cup B\), where
\[
          \mathbf1_B=\mathbf1_{E\setminus\{z\}}
                        +\sum_{k=1}^4\mathbf1_{J_k}
                        -\sum_{h=1}^4\mathbf1_{U_h}.               \tag{13}
\]
Every coordinate on the right must be zero or one; its coordinate sum
is automatically four. Finally \(\{z\}\cup B\) and
\((E\setminus\{z\})\setminus B\) must both occur in the source
critical pool. The former is checked in the packet plus selected
one-hook shorts, and the latter in the packet plus selected zero-hook
shorts. Equations (11)--(13) and these endpoint tests are necessary
before choosing a single new prefix order. They are not sufficient:
the remaining critical cells and all noncritical targets must still be
checked.

Global complementation of **all nine coordinates** preserves this trade
problem and all costs. It reverses the two orders in each full row,
preserves its longer axis support, exchanges \(n_0\) with \(4-n_0\),
and sends the unique long-shore position to \(6-p\) and the four
short-shore positions to \(5-p\). It also reverses both orders of every
base row. Thus it relates the original bank to its order-reversed bank;
without a further symmetry proof it does not justify identifying sign
cases within the literal fixed bank.

In particular the uniform-zero analogue of (9), expressed using the
original packet path, is
\[
          \sum_{k=1}^4\mathbf1_{J_k}
                 =4\mathbf1_{E\setminus\{z\}}
                            -\sum_{i\ne j}\mathbf1_{B_i}.          \tag{14}
\]
This follows because reversing the two packet orders changes its middle
path to \(B'_i=(E\setminus\{z\})\setminus B_{4-i}\). Both uniform
endpoint cases can therefore be screened from the same stored path
data, while retaining the distinction between the two orientations.

## 7. Five vertical anchors force all new z-positions

The preceding endpoint certificate can be strengthened for every mixture
of signs. The critical source pool contains exactly five pairs
\[
                              B_i,\ B_i\cup\{z\},
                         \qquad i=0,\ldots,4,                      \tag{15}
\]
where the \(B_i\) are the old packet's middle path. To see that there
are no others, any such pair projects to one rank-four target of the
base bank. Its unique owner must contribute both signs. Among the
source owners only the packet does so, and it contributes all five of
its middle targets.

Every full four-by-five prefix row has exactly one vertical critical
pair: use the two prefixes immediately before and after its \(z\),
and the unique opposite-shore prefix making their ranks four and five.
That prefix always exists for every permissible position of \(z\).
Since critical coverage in the proposed replacement is exact, two new
rows cannot use the same pair. The five replacement rows are therefore
in bijection with the five anchors \(B_0,\ldots,B_4\).

Fix the longer support and the assigned anchor \(B\).

* If the longer support is \(\{z\}\cup T\), with \(|T|=4\), then
  \[
                              p=1+|B\cap T|.                      \tag{16}
  \]
  The longer order is an order of \(B\cap T\), followed by \(z\),
  followed by an order of \(T\setminus B\). The shorter order begins
  with \(B\setminus T\) and ends with the remaining coordinates.
  Its exact number of possible order pairs is
  \[
                         ((p-1)!(5-p)!)^2,
  \]
  namely \(576,36,16,36,576\) for \(p=1,\ldots,5\).

* If the longer support is \(U\subseteq E\setminus\{z\}\), with
  \(|U|=5\), then
  \[
                              p=5-|B\cap U|.                      \tag{17}
  \]
  The shorter order is an order of \(B\setminus U\), followed by
  \(z\), followed by an order of
  \((E\setminus(\{z\}\cup U))\setminus B\). The longer order
  begins with \(B\cap U\) and then uses \(U\setminus B\). Its exact
  number of possible order pairs is
  \[
                          (p-1)!(4-p)!(5-p)!p!,
  \]
  namely \(144,24,24,144\) for \(p=1,\ldots,4\).

All listed set sizes follow directly from \(|B|=4\); in particular the
positions in (16)--(17) are in their permitted ranges. These are exact
descriptions of all full prefix rows with that support and anchor, not
just upper bounds on a larger catalogue.

For a fixed five-support certificate from Section 6 there are at most
\(5!=120\) assignments to anchors. Every assignment forces all positions
and must satisfy (11) before any internal orders are considered. If the
z-long row has support \(\{z\}\cup T\) and anchor \(B_j\), this
condition becomes
\[
           \sum_{i\ne j}|B_i\cap U_i|-|B_j\cap T|
                               =16-4n_0.                           \tag{18}
\]
For \(n_0=0\), the left side is at most sixteen; equality forces each
\(U_i\) to contain its anchor and \(T\) to be disjoint from its anchor.
This recovers the uniform-one path matching of Section 5. For \(n_0=4\),
the left side is at least zero, since each intersection with a five-set
in an eight-set has size at least one; equality forces those four
intersections to have size one and \(T=B_j\). Intermediate values give
a small exact assignment test. As before, passing these tests does not
prove that the remaining critical targets, or the whole Boolean cube,
are covered.
