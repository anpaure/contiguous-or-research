# Annular MTF bridges: ordered-tail flow and the complementary reversal cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom{2m+1}{m},
 \qquad H=\lceil A\sqrt m\rceil,
 \qquad h=o(\sqrt m),
\tag{0.1}
\]

where \(A>0\) is fixed.  The preceding radius-flow note gave the exact
Hall criterion for one-update, radius-decreasing annular switches, but it
left open whether the resulting \(\Theta(W/\sqrt m)\) components can be
joined at bounded excess.  This note derives the exact directed bridge
distance between two prescribed move-to-front states and inserts it into
a weighted integral flow.

There are three conclusions.

1. **Exact bridge distance.**  After \(k\) move-to-front updates, the
   untouched part of the old ordered partition remains an ordered tail.
   Consequently the minimum number \(d(\Pi,\Pi')\) of updates from one
   state to another is the least number of leading blocks which must be
   removed from \(\Pi'\) before its remaining tail is an order-preserving
   deletion of \(\Pi\); see (1.5).

2. **Exact weighted flow.**  For fixed annular states on the chains of an
   SCD, the minimum excess of every radius-decreasing, independently
   initialized compiler is

   \[
    \boxed{
    E_{\min}
    =\sum_C(|\Pi_C|-1)
     -\sum_{s\ge1}\Phi_s,}
   \tag{0.2}
   \]

   where \(\Phi_s\) is a maximum-weight bipartite matching value with edge
   saving \(|\Pi_D|-d(\Pi_C,\Pi_D)\).  Thus \(E_{\min}=o(W)\) is an exact
   min-cost-flow criterion, not an average-degree heuristic.

3. **Complementary reversal obstruction.**  If \(C\) has radius \(s\),
   put \(r_s=\min\{s,H\}\).  Every annular state for \(C\) contains a
   forced ordered list
   of

   \[
    L_s=2(r_s-h)-1
   \tag{0.3}
   \]

   singleton blocks.  The complementary chain \(C^c\) forces exactly the
   reversed list.  Hence every literal bridge from an annular state for
   \(C\) to any annular state for \(C^c\) uses at least

   \[
    \boxed{d\ge L_s-1=2(r_s-h)-2}
   \tag{0.4}
   \]

   updates, whenever \(r_s\ge h+1\).  In particular a direct complement
   switch at the peak radius \(s=\sqrt{m/2}+O(1)\) costs
   \(\Theta_A(\sqrt m)\).  Therefore direct chainwise complement switches
   cannot be the sole horizontal mechanism across the peak layer.

This is a statewise no-go for the canonical complementary-pair escape.  It
does not rule out cross-chain switches \(C\to D^c\) whose forced singleton
orders are almost aligned.  The exact surviving target is a matching of
Gaussian size between the two SCDs with ordered-tail defect \(O(1)\), not
the chainwise complement bijection.

## 1. Exact move-to-front bridge distance

Let

\[
 \Pi=(B_1,\ldots,B_r)
\tag{1.1}
\]

be an ordered partition of \([n]\).  For a nonempty mask \(X\), its
move-to-front update is

\[
 M_X(\Pi)
 =(X,B_1\setminus X,\ldots,B_r\setminus X),
\tag{1.2}
\]

with empty blocks deleted.

### Lemma 1.1 (last-touch normal form)

After \(k\) updates by masks \(X_1,\ldots,X_k\), put

\[
 L_i=X_i\setminus\bigcup_{j>i}X_j,
 \qquad
 U=\bigcup_{i=1}^kX_i.
\tag{1.3}
\]

The final state is

\[
 (L_k,L_{k-1},\ldots,L_1,
   B_1\setminus U,\ldots,B_r\setminus U),
\tag{1.4}
\]

after deleting empty blocks.  Conversely, for any pairwise disjoint
nonempty blocks \(L_k,\ldots,L_1\), the state in (1.4) is obtained in
exactly \(k\) updates.

#### Proof

The first assertion follows by induction.  At the final update, the
elements of \(X_k\) form the first block; deleting them from the state
after the first \(k-1\) updates changes every earlier last-touch class
\(X_i\setminus\bigcup_{i<j<k}X_j\) into \(L_i\), and changes every old
block into \(B_a\setminus U\).

For the converse, update first by \(L_1\), then by \(L_2\), and so on
through \(L_k\).  Disjointness makes the resulting state exactly (1.4).
\(\square\)

For an ordered partition \(\Pi\) and a set \(U\), write
\(\Pi-U\) for the ordered partition obtained by deleting \(U\) from each
block and then deleting empty blocks.

### Theorem 1.2 (ordered-tail distance formula)

Let

\[
 \Pi'=(B'_1,\ldots,B'_t),
 \qquad
 U_j=B'_1\cup\cdots\cup B'_j,
\]

with \(U_0=\varnothing\).  The minimum number of move-to-front updates
which changes \(\Pi\) exactly into \(\Pi'\) is

\[
 \boxed{
 d(\Pi,\Pi')
 =\min\bigl\{j:
   (B'_{j+1},\ldots,B'_t)=\Pi-U_j\bigr\}.}
\tag{1.5}
\]

The empty tail is allowed, so the minimum always exists and is at most
\(|\Pi'|\).

#### Proof

Suppose \(k\) updates reach \(\Pi'\).  By Lemma 1.1 the nonempty new
last-touch classes are an initial segment of \(\Pi'\), and the rest of
\(\Pi'\) is the old partition after deletion of their union.  If fewer
than \(k\) last-touch classes are nonempty, discard the vacuous updates.
Thus the right side of (1.5) is at most \(k\).

Conversely, if the equality in (1.5) holds for \(j\), update successively
by

\[
 B'_j,B'_{j-1},\ldots,B'_1.
\]

These blocks are disjoint.  Lemma 1.1 gives \(\Pi'\) after exactly \(j\)
updates. \(\square\)

Formula (1.5) is directed: generally
\(d(\Pi,\Pi')\ne d(\Pi',\Pi)\).  It is the exact algebraic form of a
directed prefix contaminant.  A one-update transition exists precisely
when deleting the first block of \(\Pi'\) leaves an ordered deletion of
\(\Pi\).

For a chain \(D\), let \(F_{h,H}(D)\) denote all ordered-partition states
which expose its central and annular target members.  The exact exposure
distance from a state \(\Pi\) is therefore

\[
 \boxed{
 \kappa(\Pi,D)=\min_{\Pi'\in F_{h,H}(D)}d(\Pi,\Pi').}
\tag{1.6}
\]

Unlike pairwise existential compatibility, a path schedule must retain
the particular minimizing successor state \(\Pi'\) for its next bridge.

## 2. Exact weighted matching criterion for a fixed state selection

Fix one state \(\Pi_C\in F_{h,H}(C)\) for every chain \(C\) of an SCD.
Let \(V_s\) be the radius-\(s\) chains.  Restrict temporarily to directed
arcs \(C\to D\) from \(V_s\) to \(V_{s-1}\).  Assign the exact bridge
length and saving

\[
 d_{CD}=d(\Pi_C,\Pi_D),
 \qquad
 w_{CD}=|\Pi_D|-d_{CD}.
\tag{2.1}
\]

Initializing a path at \(D\) costs \(|\Pi_D|\) letters.  If \(D\) instead
has predecessor \(C\), its bridge costs \(d_{CD}\), so \(w_{CD}\) is the
exact saving.

For each \(s\ge1\), let

\[
 \Phi_s=\max_{M_s}
  \sum_{CD\in M_s}(w_{CD})_+,
\tag{2.2}
\]

where \(M_s\) ranges over matchings between \(V_s\) and \(V_{s-1}\).
Equivalently one may retain all edge weights and allow an arbitrary
matching, including the empty matching.

### Theorem 2.1 (weighted annular path-flow identity)

Among all radius-decreasing path forests on the fixed states, compiled by
initializing each path at its first state and then using exact bridges, the
minimum word length and minimum excess over one letter per chain are

\[
 \boxed{
 L_{\min}
 =\sum_C|\Pi_C|-\sum_{s\ge1}\Phi_s,}
\tag{2.3}
\]

and

\[
 \boxed{
 E_{\min}=L_{\min}-W
 =\sum_C(|\Pi_C|-1)-\sum_{s\ge1}\Phi_s.}
\tag{2.4}
\]

In particular, this fixed state selection gives a constant-one annular
compiler within the architecture if and only if the right side of (2.4)
is \(o(W)\).

#### Proof

In any path forest, every chain \(D\) is either a path start, contributing
\(|\Pi_D|\), or has one predecessor \(C\), contributing \(d_{CD}\).
Replacing the former by the latter saves exactly \(w_{CD}\).  The selected
arcs between \(V_s\) and \(V_{s-1}\) form a matching.  Conversely,
independent matchings at consecutive interfaces give every vertex at most
one incoming and one outgoing edge; strict radius decrease prevents
cycles.  Hence every collection of interface matchings is a path forest.

The objective is additive over the interfaces, so a maximum-weight
matching can be chosen independently in each.  Edges of negative saving
are never needed for length minimization.  Subtracting the total maximum
saving from the all-start initialization cost proves (2.3), and (2.4)
follows because an SCD has exactly \(W\) chains. \(\square\)

The standard unit-capacity network

\[
 \mathbf s\longrightarrow V_s\longrightarrow V_{s-1}
 \longrightarrow\mathbf t
\]

with cost \(-w_{CD}\) on its middle arcs computes \(\Phi_s\).  Bipartite
integrality makes (2.3) an exact min-cost-flow criterion.  The state choice
remains global and nonlinear: optimizing \(\Pi_C\) separately on its
incoming and outgoing interfaces is invalid.

For later obstruction arguments, the exact dual form is

\[
 \boxed{
 \Phi_s=
 \min\left\{
 \sum_{C\in V_s}u_C+\sum_{D\in V_{s-1}}v_D:
 \begin{array}{l}
  u_C,v_D\ge0,\\
  u_C+v_D\ge(w_{CD})_+
       \quad\text{for every }C,D
 \end{array}\right\}.}
\tag{2.5}
\]

Thus a fixed state family succeeds precisely when its interface matching
values absorb all but \(o(W)\) of
\(\sum_C(|\Pi_C|-1)\).  Conversely, feasible potentials in (2.5) whose
total values leave a linear unabsorbed residue certify a literal
statewise no-go for that family.

The unweighted directed-prefix criterion is recovered by retaining only
the edges with \(d_{CD}=1\).  Let \(\nu_s^{(1)}\) be the maximum matching
size in that graph and put

\[
 \delta_s^{(1)}
 =|V_s|-\nu_s^{(1)}
 =\max_{X\subseteq V_s}\bigl(|X|-|N_s^{(1)}(X)|\bigr).
\tag{2.6}
\]

Exactly as in the graded path-cover proof, the minimum number of monotone
one-update components is

\[
 p_1=c_0+\sum_{s\ge1}\delta_s^{(1)}.
\tag{2.7}
\]

Concatenating these components requires exactly \(p_1-1\) joins outside
the certified one-update forest.  Hence, within this architecture, the
exact criterion for \(o(W)\) directed prefix-contaminant joins is

\[
 \boxed{
 \sum_{s\ge1}
 \max_{X\subseteq V_s}
 \bigl(|X|-|N_s^{(1)}(X)|\bigr)=o(W),}
\tag{2.8}
\]

because \(c_0=2W/(m+2)=o(W)\).  Condition (2.8) controls the number of bad
joins; the weighted identity (2.4) is the stronger condition that controls
their literal excess.

## 3. An ordered-subsequence obstruction

The distance formula has a useful statewise consequence which does not
depend on the rest of either partition.

### Lemma 3.1 (reversed singleton bound)

Let \(a_1,\ldots,a_L\) be distinct coordinates.  Suppose they occur as
singleton blocks of \(\Pi\) in the displayed relative order.  Suppose
\(\Pi'\) has the same coordinates as singleton blocks in the reverse
relative order

\[
 a_L,a_{L-1},\ldots,a_1.
\tag{3.1}
\]

Then

\[
 \boxed{d(\Pi,\Pi')\ge L-1.}
\tag{3.2}
\]

The same lower bound holds if the final state is allowed to be any state
which forces the relative singleton order (3.1).

#### Proof

By Lemma 1.1, after \(k\) updates the blocks not belonging to the first
\(k\) last-touch classes form an order-preserving deletion of \(\Pi\).
Every touched coordinate among the \(a_i\) must occupy a different
last-touch class: two of them in one class would lie in one state block
and could not be separated by a required prefix boundary.  Thus at least
\(L-k\) of the distinguished singleton coordinates remain in the old
ordered tail.

If \(L-k\ge2\), any two of those coordinates occur in their forward order
in the old tail but are required in reverse order in the final state, a
contradiction.  Hence \(L-k\le1\), proving \(k\ge L-1\).  The argument
uses only the forced order in the final state, so it also proves the last
assertion. \(\square\)

More generally, if \(S\) is a set of coordinates which are forced
singleton layers in both states, let \(\sigma\) and \(\tau\) be their two
relative orders.  The same proof gives

\[
 \boxed{
 d(\Pi,\Pi')
 \ge |S|-\operatorname {LCS}(\sigma,\tau),}
\tag{3.3}
\]

where \(\operatorname {LCS}\) is the longest common subsequence length.
Indeed the untouched distinguished coordinates must form a common
subsequence, while each touched distinguished coordinate consumes its own
new last-touch block.  Formula (3.3) is the relevant cross-SCD switching
screen: bounded-excess bridges require all but \(O(1)\) common forced
singletons to occur in a common order.

There is a stronger screen which also sees target singleton coordinates
that are not forced singletons of the source chain.

### Lemma 3.2 (source-block LIS bound)

Write \(\Pi=(B_1,\ldots,B_r)\), and suppose the final state is required to
contain distinct coordinates

\[
 \tau=(a_1,a_2,\ldots,a_L)
\tag{3.4}
\]

as singleton blocks in that relative order.  Let \(j_i\) be the unique
source-block index satisfying \(a_i\in B_{j_i}\), and let
\(\operatorname {LIS}(j_1,\ldots,j_L)\) denote the longest strictly
increasing subsequence length.  Every update sequence reaching such a
final state has length

\[
 \boxed{
 k\ge
 L-\operatorname {LIS}(j_1,\ldots,j_L).}
\tag{3.5}
\]

#### Proof

Every touched \(a_i\) belongs in the final state to a new last-touch
class.  Since the \(a_i\) must be distinct singleton blocks, no two
touched \(a_i\)'s can share a class.  Hence at most \(k\) of them are
touched.

The untouched \(a_i\)'s remain in \(\Pi-U\).  Two of them cannot originate
in the same source block, because then they would remain in the same final
block.  Their final order is the order of their distinct source blocks.
Thus, read in the required target order, their block indices form a
strictly increasing subsequence of \((j_1,\ldots,j_L)\).  At most
\(\operatorname {LIS}(j_1,\ldots,j_L)\) target singletons are untouched,
so at least the claimed number are touched. \(\square\)

For a target chain \(D\), let \(\tau_D\) be its forced annular singleton
order and define the statewise LIS defect

\[
 \zeta(\Pi,D)
 =|\tau_D|-\operatorname {LIS}
   \bigl(\operatorname {blk}_{\Pi}(\tau_D)\bigr).
\tag{3.6}
\]

Then

\[
 \boxed{\kappa(\Pi,D)\ge\zeta(\Pi,D).}
\tag{3.7}
\]

Unlike (3.3), this bound uses every forced target singleton.  It detects
both wrong order and collisions of several target singletons in one
source block.

## 4. Complementary annular chains force reversal

Write a radius-\(s\) symmetric chain as

\[
 C=(B;z_1,z_2,\ldots,z_{2s+1}),
\tag{4.1}
\]

meaning that its members are

\[
 B, B\cup\{z_1\},\ \ldots,\
 B\cup\{z_1,\ldots,z_{2s+1}\}.
\]

Put

\[
 r_s=\min\{s,H\}.
\tag{4.2}
\]

Assume \(r_s\ge h+1\).  Every state exposing the lower annulus, both
central ranks, and the upper annulus has the following coordinates as
singleton blocks in the displayed relative order:

\[
 \begin{split}
 \sigma_C={}&(
 z_{s-r_s+1},\ldots,z_{s-h-1},
 z_{s+1},\\
 &z_{s+h+3},\ldots,z_{s+r_s+1}).
 \end{split}
\tag{4.3}
\]

There are \(r_s-h-1\) coordinates in each outside run and one central
coordinate, so

\[
 |\sigma_C|=2(r_s-h)-1.
\tag{4.4}
\]

These indices agree with the truncated annular ranks
\([m-r_s,m-h-1]\) and \([m+h+2,m+1+r_s]\): only increments between two
consecutive required ranks are forced singleton blocks.

The complementary chain \(C^c\) has increment order

\[
 z_{2s+1},z_{2s},\ldots,z_1.
\tag{4.5}
\]

Applying (4.2) to this reversed order shows that its forced singleton list
is exactly

\[
 \sigma_{C^c}=\operatorname {rev}(\sigma_C).
\tag{4.6}
\]

### Theorem 4.1 (chainwise complementary-switch obstruction)

For every \(s\) with \(r_s\ge h+1\), every annular state
\(\Pi\in F_{h,H}(C)\), and every literal sequence of updates whose final
state exposes the annular targets of \(C^c\), the number \(k\) of updates
satisfies

\[
 \boxed{k\ge2(r_s-h)-2.}
\tag{4.7}
\]

Thus its excess over an ideal one-update chain transition is at least

\[
 2(r_s-h)-3.
\tag{4.8}
\]

#### Proof

The source state forces \(\sigma_C\) as singleton blocks in forward order,
and the final state forces the same \(2(r_s-h)-1\) coordinates in reverse
order by (4.6).  Lemma 3.1 gives

\[
 k\ge |\sigma_C|-1=2(r_s-h)-2.
\]

\(\square\)

### Corollary 4.2 (the naive two-SCD escape pays linear excess)

Suppose a stateful annular path cover uses \(b\) horizontal transitions
\(C\to C^c\), and all their source radii satisfy \(r_s\ge h+1\).  Their
total bridge excess is at least

\[
 \sum_{C\to C^c}
 \bigl(2(\min\{\operatorname {rad}(C),H\}-h)-3\bigr)_+.
\tag{4.9}
\]

In particular, if all \(b\) sources have radius
\(s=\alpha\sqrt m+O(1)\), where \(\alpha>0\) is fixed, and

\[
 b\ge \gamma {W\over\sqrt m}
\tag{4.10}
\]

for a fixed \(\gamma>0\), then their excess is
\(\Omega_{A,\alpha,\gamma}(W)\).

There is an exact horizontal layer cut.  In a path cover having no upward
arcs, let \(b_s\) be the number of selected horizontal arcs at radius
\(s\).  Then

\[
 \boxed{p+b_s\ge c_s.}
\tag{4.11}
\]

Indeed each path visits \(V_s\) in one contiguous horizontal segment, and
a segment containing \(a\) vertices uses \(a-1\) horizontal arcs.
Summing over paths proves (4.11).

At the maximizing radius

\[
 s_*=\sqrt{m/2}+O(1),
 \qquad
 c_{s_*}=
 \left(\sqrt{2/e}+o(1)\right){W\over\sqrt m},
\tag{4.12}
\]

we have

\[
 \min\{s_*,H\}-h
 =\bigl(\min\{1/\sqrt2,A\}+o(1)\bigr)\sqrt m.
\tag{4.13}
\]

Consequently, if \(p=o(W/H)\), there are no upward arcs, and every
horizontal arc at \(s_*\) is a direct complement switch, then
(4.11) forces \(b_{s_*}=c_{s_*}-o(W/\sqrt m)\), while (4.8) and (4.13)
give \(\Omega_A(W)\) total excess.  Direct chainwise complementation is
therefore a statewise no-go as the sole nondecreasing mechanism.

#### Proof

Sum (4.8) over the \(b\) transitions.  The fixed-radius assertion follows
from
\[
 \min\{\alpha\sqrt m,H\}-h
 =(\min\{\alpha,A\}+o(1))\sqrt m.
\]
The horizontal layer-cut argument and (4.12)--(4.13) prove the final
assertion. \(\square\)

## 5. Exact surviving complementary-pair criterion

Let \(\mathcal S\) and \(\mathcal S^c\) be complementary SCDs.  For a
chosen state \(\Pi_C\) of a source chain and a proposed successor \(D\),
define the ordered-tail screening defect

\[
 \zeta(C,D)
 =|\tau_D|-\operatorname {LIS}
   \bigl(\operatorname {blk}_{\Pi_C}(\tau_D)\bigr),
\tag{5.1}
\]

where \(\tau_D\) is the complete forced annular singleton order of \(D\).
Every directed bridge satisfies

\[
 d(\Pi_C,\Pi_D)\ge\zeta(C,D).
\tag{5.2}
\]

Consequently, a complementary-pair construction based on
\(\Theta(W/\sqrt m)\) horizontal cross-decomposition arcs can have
\(o(W)\) bridge excess only if all its selected cross arcs satisfy

\[
 \sum_{\text{selected }C\to D}\zeta(C,D)=o(W).
\tag{5.3}
\]

A sufficient bounded-bridge version is that the full ordered-tail
distance (1.5) is \(O(1)\) on all but \(o(W/H)\) selected arcs and is
\(O(H)\) on the exceptions.  The LIS condition is necessary, not
sufficient, because all nondistinguished coordinates must also lie in the
correct deleted tail.

Thus the exact next matching problem is not complement pairing.  It is a
cross-chain, state-decorated matching whose edges satisfy both:

1. the source-block LIS defect (5.1) is \(O(1)\); and
2. the complete residual ordered partitions satisfy (1.5) after deleting
   only \(O(1)\) leading target blocks.

The weighted matching functional (2.2) is the exact integral test for the
radius-decreasing interfaces once the states have been fixed.  Horizontal
or upward cross-decomposition arcs additionally need an acyclic
state-composable selection; an unrestricted directed matching could close
a cycle and is not by itself a path schedule.

## 6. Status

Proved here:

1. the exact directed MTF distance between two ordered-partition states;
2. the exact Hall criterion for \(o(W)\) directed contaminants and the
   exact min-cost-flow identity for their weighted literal excess;
3. the forced-singleton LCS and source-block LIS lower bounds;
4. the \(2(\min\{s,H\}-h)-2\)-update lower bound for every direct
   complementary-chain switch of radius \(s\); and
5. the resulting \(\Omega_A(W)\) obstruction when chainwise complement
   arcs are the sole horizontal mechanism across the peak stratum.

Not proved here:

1. a noncanonical SCD satisfying the weighted flow criterion;
2. a cross-chain complementary matching with ordered-tail defect \(O(1)\);
3. composable horizontal/upward arcs on the required
   \(\Theta(W/\sqrt m)\) scale; or
4. coefficient one.

The statewise conclusion is sharp in scope.  Complementation supplies the
right target sets but reverses every forced Gaussian singleton chronology.
Any successful complementary pair must therefore reroute between
different chains so that their annular orders nearly agree; the obvious
chainwise complement identification is unusable at constant one.
