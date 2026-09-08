# Extensive reciprocal-\(C_8\) Catalan factors, infinity-cut packets, and the exact annulus selection gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, web
input, or entropy heuristic is used.

## 0. Outcome

Fix constants

\[
 0<a<b<\infty,\qquad
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,
\tag{0.1}
\]

and put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 B=C_m={W\over m+1},
\tag{0.2}
\]

Let \(D_m\) denote the Dyck words of semilength \(m\), so
\(|D_m|=B\).

\[
 K_0=\left\lfloor{N_{q_0}\over2m}\right\rfloor
 =\left({e^{-a^2}\over2}+o(1)\right)B.
\tag{0.3}
\]

There is a genuine growing, non-row-power Catalan trade family.  Choose

\[
 u=\lfloor\alpha m\rfloor,\qquad 0<\alpha<{1\over2},
\tag{0.4}
\]

pairwise disjoint four-bit positions in a Dyck word and install, at every
chosen position, the sealed reciprocal replacement

\[
                  1100\longleftrightarrow1010.       \tag{0.5}
\]

Every one of the \(2^u\) global masks is a literal anchored exact factor.
For the all-on mask:

* all but \(O(B/m)\) Dyck rows change;
* the exact total adjacent-order edit mass is
  \[
       \boxed{D_{\rm edit}=4uC_{m-2}
       =\left({\alpha\over4}+o(1)\right)W;}          \tag{0.6}
  \]
* hence the bank has root-scale, rather than bounded-fringe, action.

Cutting the distinguished infinity coordinate out of every row gives
\(B\) literal ordinary directed cyclic orders on \([2m]\).  Thus one
all-on factor contains more than enough genuinely changed packets to
supply the required \(K_0\) packets in (0.3).

The middle-owner ledger of these cut packets has an exact new description.
Every anchored exact factor \(F\) determines a loopless
\((m-1)\)-regular multigraph \(G_F\) on its \(B\) rows such that for every
row set \(S\),

\[
 \boxed{
 C_0\bigl(\{\pi_x:x\in S\}\bigr)=2e_{G_F}(S).}
\tag{0.7}
\]

Here \(e_{G_F}(S)\) is the number of graph edges, with multiplicity, whose
two endpoints lie in \(S\).  Thus the vague middle-transversal problem is
exactly a prescribed-density sparse-induced-subgraph problem.

The ordinary packets already have the right physical component cost:

\[
 K_0=\Theta_a(W/m)=o(W/H),
\qquad
 2HK_0\le {H\over m}N_{q_0}=O_{a,b}(W/\sqrt m)=o(W).
\tag{0.8}
\]

What is not proved is productive all-depth selection.  The exact surviving
lemma is the following.  For some global reciprocal-\(C_8\) mask \(A_m\),
choose \(S_m\subseteq D_m\), \(|S_m|=K_0\), so that

\[
 e_{G_{F^{A_m}}}(S_m)=o(W)                            \tag{0.9}
\]

and

\[
 \sum_{q=q_0}^{H}
 \left[
 N_q-\left|\bigcup_{x\in S_m}E_{m-q}(\pi_x^{A_m})\right|
 \right]=o(W).                                       \tag{0.10}
\]

If (0.9)--(0.10) hold, the literal word length is

\[
 \boxed{
 W+2e_{G_{F^{A_m}}}(S_m)+2HK_0
 +2\sum_{q=q_0}^{H}
 \left[
 N_q-\left|\bigcup_{x\in S_m}E_{m-q}(\pi_x^{A_m})\right|
 \right]
 =W+o(W).}                                           \tag{0.11}
\]

Thus (0.9)--(0.10) are a theorem-level, literal annulus gate for this
specific positive-density non-row-power bank.  The construction below
proves supply, exact factor legality, root-scale action, and physical seam
cost.  It does not prove (0.9)--(0.10).  In particular, edit mass is only
capacity to act; it is not a lower bound on useful distinct target motion.
The common global mask is a structured sufficient sublane, not a necessary
compiler constraint.  Because the final word merely concatenates ordinary
packets, different selected rows may take variants certified in different
global factor states.  The strictly weaker, sharp rowwise gate is stated
in Section 6.

## 1. Infinity-cut packets from an anchored exact factor

Let

\[
 \Omega=[2m]\sqcup\{\infty\}.
\tag{1.1}
\]

An anchored exact wreath factor has \(B=C_m\) rows.  Write the associated
step-two coordinate order of row \(x\), rotated to put infinity first, as

\[
 r_x=(\infty,a_{x,1},a_{x,2},\ldots,a_{x,2m}).       \tag{1.2}
\]

Exactness says that the length-\(m\) cyclic intervals in all the \(r_x\)'s
partition \(\binom{\Omega}{m}\).  This is the ordinary interval form of
the omitted-label ownership identity.  The count is consistent because

\[
 (2m+1)B=\binom{2m+1}{m}.                            \tag{1.3}
\]

Delete infinity and retain the induced directed cyclic order

\[
 \pi_x=(a_{x,1},\ldots,a_{x,2m})                    \tag{1.4}
\]

on \([2m]\).  It is a literal ordinary packet.  For any cyclic order
\(\pi=(\pi_1,\ldots,\pi_{2m})\), write

\[
 E_r(\pi)=
 \bigl\{\{\pi_j,\pi_{j+1},\ldots,\pi_{j+r-1}\}:
                    j\in\mathbb Z_{2m}\bigr\}.       \tag{1.4a}
\]

For
\(1\le j\le m+1\), put

\[
 P_{x,j}=\{a_{x,j},a_{x,j+1},\ldots,a_{x,j+m-1}\},  \tag{1.5}
\]

where the displayed indices do not wrap around the deleted infinity gap.

### Lemma 1.1 (primary-owner partition)

The sets

\[
 \mathcal P_F=\{P_{x,j}:x\in D_m,\ 1\le j\le m+1\}
\tag{1.6}
\]

are exactly all members of \(\binom{[2m]}m\), each once.

#### Proof

The length-\(m\) intervals of \(r_x\) which avoid infinity are precisely
the \(m+1\) intervals in (1.5).  Exactness of the anchored factor assigns
every infinity-avoiding \(m\)-subset of \(\Omega\), equivalently every
\(m\)-subset of \([2m]\), exactly once.  Also

\[
 (m+1)B=W,
\]

so there is no count discrepancy. \(\square\)

### Lemma 1.2 (exact cut-packet owner formula)

For every row \(x\),

\[
 \boxed{
 E_m(\pi_x)
 =\{P_{x,j}:1\le j\le m+1\}
 \mathbin{\dot\cup}
 \{P_{x,j}^{,c}:2\le j\le m\}.}
\tag{1.7}
\]

The union is disjoint.

#### Proof

The \(m+1\) ordinary cyclic \(m\)-windows which do not cross the new
edge \(a_{x,2m}a_{x,1}\) are the first family in (1.7).  A window which
does cross that edge starts at a position \(m+j\), with \(2\le j\le m\).
Its complement is the nonwrapping window starting at \(j\), namely
\(P_{x,j}\).  This gives the second family.

All cyclic intervals of one proper length in a cyclic order on distinct
labels are distinct.  Hence the displayed union is disjoint.  Equivalently,
the only complementary pair among the primary windows is

\[
                         P_{x,1}^{,c}=P_{x,m+1};    \tag{1.8}
\]

for \(2\le j\le m\), the opposite cyclic start lies after the infinity
cut and is not a primary start. \(\square\)

## 2. The complement graph and the exact collision identity

Call \(P_{x,1}\) and \(P_{x,m+1}\) the two ports of row \(x\), and call

\[
 \mathcal N_F=\{P_{x,j}:x\in D_m,\ 2\le j\le m\}
\tag{2.1}
\]

the nonport primary owners.

### Lemma 2.1 (nonports are complement-closed)

Complementation is a fixed-point-free involution of \(\mathcal N_F\),
and no complementary pair in \(\mathcal N_F\) belongs to one row.

#### Proof

By (1.8), complementation preserves the set of all port owners.  By
Lemma 1.1 the primary owners partition \(\binom{[2m]}m\).  Therefore the
complement of a nonport cannot be a port: if \(P^c\) were a port, then
\(P\) would be its other port partner by (1.8), contradicting unique
primary ownership.  Hence complementation preserves \(\mathcal N_F\).

If \(P_{x,j}^c=P_{x,k}\) with \(2\le j,k\le m\), their starts in the
ordinary \(2m\)-cycle would differ by \(m\) modulo \(2m\).  But
\(|j-k|\le m-2\).  Thus the two members cannot lie in one row. \(\square\)

Define the **cut complement graph** \(G_F\) as follows.  Its vertex set is
the \(B\) factor rows.  For every complementary pair
\(\{P,P^c\}\subseteq\mathcal N_F\), place one edge between the two rows
which own \(P\) and \(P^c\).  Parallel edges are retained.

### Proposition 2.2 (regularity)

The multigraph \(G_F\) is loopless and \((m-1)\)-regular.  In particular,

\[
 |E(G_F)|={(m-1)B\over2}.                            \tag{2.2}
\]

#### Proof

Lemma 2.1 rules out loops.  Every row owns exactly \(m-1\) nonports, and
each is one endpoint of one complementary pair.  Thus every row has degree
\(m-1\), with multiplicity.  The handshake identity gives (2.2).
\(\square\)

### Theorem 2.3 (exact middle collision formula)

For every row set \(S\subseteq D_m\), let

\[
 \mathcal F_S=\{\pi_x:x\in S\}.
\tag{2.3}
\]

Then

\[
 \left|\bigcup_{x\in S}E_m(\pi_x)\right|
 =2m|S|-2e_{G_F}(S),                                 \tag{2.4}
\]

and consequently

\[
 \boxed{C_0(\mathcal F_S)=2e_{G_F}(S).}              \tag{2.5}
\]

#### Proof

By Lemma 1.1, all primary occurrences belonging to selected rows are
distinct.  By injectivity of complementation, all extra occurrences
\(P_{x,j}^c\), \(2\le j\le m\), belonging to selected rows are also
distinct.  Thus collisions can occur only between one primary and one
extra occurrence.

Let an edge of \(G_F\) be represented by complementary nonports
\(P\) in row \(x\) and \(P^c\) in row \(y\).  If both \(x,y\in S\),
then the extra \(P^c\) from row \(x\) duplicates the primary \(P^c\)
from row \(y\), and the extra \(P\) from row \(y\) duplicates the primary
\(P\) from row \(x\).  This contributes exactly two to the collision
excess.  If at most one endpoint is selected, neither duplication occurs.
No target belongs to two different complement pairs, so these contributions
are disjoint.  Summing over internal edges proves (2.4)--(2.5).
\(\square\)

Since \(G_F\) is \((m-1)\)-regular, (2.5) is equivalently

\[
 \boxed{
 C_0(\mathcal F_S)
 =(m-1)|S|-|\delta_{G_F}(S)|.}                       \tag{2.5a}
\]

Thus \(C_0=o(W)\) asks the cut out of \(S\) to use all but
\(o(mB)\) of the edge incidences at \(S\).  There is no scalar shore-size
obstruction because \(|S|/B\to e^{-a^2}/2<1/2\); the obstruction, if any,
is failure of this near-independent cut condition.
Indeed the uniform fractional row value
\(x_v=e^{-a^2}/2+o(1)\) satisfies \(x_u+x_v\le1\) on every graph edge.
The issue is entirely the integral hard-core/trace coupling.

This is stronger than a generic owner-transversal formulation.  For a
common exact factor, middle collision \(o(W)\) is equivalent to finding a
row set of the prescribed density with

\[
                         e_{G_F}(S)=o(mB).            \tag{2.6}
\]

Regularity alone neither proves nor refutes (2.6): a nearly bipartite
graph permits it, while a uniformly expanding dense-degree graph may not.
The needed conclusion is a structural statement about the complement
graphs generated by the Catalan trade family.

## 3. An extensive reciprocal-\(C_8\) exact-factor bank

Choose \(u\) pairwise disjoint four-coordinate slots in the Dyck word.
At slot \(j\), let \(\tau_j\) interchange the two middle coordinates of
the slot, so that it exchanges

\[
                         1100\longleftrightarrow1010. \tag{3.1}
\]

For a Dyck root \(x\), put

\[
 J(x)=\{j:x|_{I_j}\in\{1100,1010\}\}.              \tag{3.2}
\]

The positive-height reciprocal-\(C_8\) identity says that one slot is a
sealed two-row exact-factor trade.  Disjoint slots occupy disjoint MSW
chronology slabs.  Hence they commute even when their root supports
overlap.  For a global mask \(A\subseteq[u]\), put

\[
 h_{A,x}=\prod_{j\in A\cap J(x)}\tau_j,
 \qquad
 F^A(x)=h_{A,x}F(h_{A,x}x).                          \tag{3.3}
\]

### Theorem 3.1 (extensive exact cube)

Every \(F^A\), \(A\subseteq[u]\), is a literal anchored exact factor.
For any prescribed set of \(h\) slots,

\[
 \#\{x:\hbox{all prescribed slots belong to }J(x)\}
                         =2^hC_{m-2h}.               \tag{3.4}
\]

For the all-on state \(A=[u]\), the rowwise adjacent-order edit distance
is

\[
                         d(x)=2|J(x)|,               \tag{3.5}
\]

and therefore

\[
 \boxed{
 \sum_{x\in D_m}d(x)=4uC_{m-2}.}                    \tag{3.6}
\]

#### Proof

For one slot, the two old rows and the two new rows have the same complete
\(X/Y\) ownership, the same ports, and the same outside chronology.  On
a root which supports several disjoint slots, each later operation
conjugates the earlier sealed equality by a permutation supported away
from it.  Induction gives (3.3) and exactness for every mask.

Deleting the prescribed four-bit blocks leaves an arbitrary Dyck word of
semilength \(m-2h\); each deleted block has two choices.  This is the
bijection proving (3.4).

Every active slot makes one adjacent transposition in each of the two
rooted order halves, and disjoint slots do not cancel.  This proves (3.5).
The transposed labels lie in the finite four-coordinate slot, so neither
transposition involves \(\infty\); deleting \(\infty\) preserves the same
two adjacent transpositions in the ordinary cut packet.
For a fixed slot, (3.4) with \(h=1\) gives \(2C_{m-2}\) active rows.
Summing (3.5) first over slots proves (3.6). \(\square\)

The maps \(h_{A,x}\) depend on the root.  Thus a nontrivial extensive
state is not one uniform coordinate relabelling or one row power of the
canonical factor.  It is a literal row-dependent exact factor assembled
from commuting sealed trades.

### Proposition 3.2 (almost every row changes)

Let \(u=\lfloor\alpha m\rfloor\) with fixed
\(0<\alpha<1/2\), and let \(x\) be uniform in \(D_m\).  Then

\[
 \mathbb E|J(x)|={\alpha\over8}m+O_\alpha(1),
 \qquad
 \operatorname {Var}|J(x)|=O_\alpha(m),              \tag{3.7}
\]

and

\[
 \boxed{
 \#\{x:J(x)=\varnothing\}=O_\alpha(B/m).}           \tag{3.8}
\]

Consequently the all-on factor changes a \(1-O_\alpha(1/m)\) fraction
of all Catalan rows.

#### Proof

For one prescribed slot and two prescribed disjoint slots, respectively,
(3.4) gives

\[
 p_m=\Pr(j\in J)={2C_{m-2}\over C_m}
 ={m(m+1)\over2(2m-1)(2m-3)}
 ={1\over8}+O(m^{-1}),                               \tag{3.9}
\]

\[
 p_{2,m}=\Pr(i,j\in J)={4C_{m-4}\over C_m}
 ={1\over64}+O(m^{-1}).                              \tag{3.10}
\]

Thus \(p_{2,m}-p_m^2=O(m^{-1})\).  Writing
\(|J|=\sum_{j=1}^uI_j\) gives

\[
 \operatorname {Var}|J|
 =up_m(1-p_m)+u(u-1)(p_{2,m}-p_m^2)=O_\alpha(m),     \tag{3.11}
\]

while \(\mathbb E|J|=up_m=\alpha m/8+O_\alpha(1)\).
Chebyshev's inequality gives

\[
 \Pr(J=\varnothing)
 \le {\operatorname {Var}|J|\over(\mathbb E|J|)^2}
 =O_\alpha(m^{-1}),                                  \tag{3.12}
\]

which is (3.8). \(\square\)

Combining (3.6) with \(C_{m-2}/C_m=1/16+O(1/m)\) and
\(mB=(1+o(1))W\) gives the exact asymptotic (0.6).

There is an important component caveat.  Across all masks, the full
ownership component through root \(x\) is its Boolean cube of size

\[
                              2^{|J(x)|}.             \tag{3.13}
\]

By (3.7) and Chebyshev, all but \(O_\alpha(B/m)\) roots lie in components
of size at least \(2^{\alpha m/17}\), for all sufficiently large \(m\).
Hence the growing construction does
not have bounded overlay components and does not license independent
rootwise shore choices.  The literal positive theorem instead fixes one
global mask, for example the all-on mask, which is already one exact
factor.  After that choice, ordinary packet compilation treats selected
rows as separate physical cycles; the large comparison-overlay components
create no seam charge.

There is also a legitimate packet-only use of the cube.  For a fixed root
\(x\), every local mask \(L\subseteq J(x)\) occurs as that row in the
literal global state \(F^L\).  Therefore it is an individually certified
ordinary packet.  Distinct local masks give distinct orders because the
slot swaps have disjoint support.  Proposition 3.2 consequently supplies
at least \(2^{\alpha m/17}\) row-labelled packet variants on all but
\(O_\alpha(B/m)\) roots.  A final packet family may choose these variants
row by row; it need not complete their union to one anchored factor.
What is lost in this relaxation is the common complement-graph formula
(2.5), not literal packet legality.

### Proposition 3.3 (complement-graph action of the cube)

Let \(F'\) be obtained from \(F\) by one sealed reciprocal-\(C_8\)
rectangle on two rows, and identify the row vertices by their fixed ports.
Then at most eight labelled edges of \(G_F\) change an endpoint.  Hence,
for every \(S\subseteq D_m\),

\[
 \bigl|e_{G_{F'}}(S)-e_{G_F}(S)\bigr|\le8.           \tag{3.14}
\]

If a global mask \(A\) contains \(t\) complete slot layers, then

\[
 \boxed{
 \bigl|e_{G_{F^A}}(S)-e_{G_F}(S)\bigr|
       \le8tC_{m-2}.}                                \tag{3.15}
\]

The same estimate holds after minimizing over all row sets of a fixed
cardinality:

\[
 \left|
 \min_{|S|=K}e_{G_{F^A}}(S)
 -\min_{|S|=K}e_{G_F}(S)
 \right|\le8tC_{m-2}.                                \tag{3.16}
\]

#### Proof

In one rectangle, each of the two cut orders undergoes two adjacent
transpositions.  By Lemma 4.1 below, one adjacent transposition can change
at most two designated middle-window occurrences.  Thus at most eight
primary target occurrences across the two rows can change owner.
The sealed trade preserves the aggregate primary ownership and fixes the
two ports.  Every changed occurrence is therefore a reassignment of a
nonport primary target between the same two row vertices.

A nonport target labels one endpoint of exactly one complement-graph edge.
Reassigning it changes at most that one endpoint.  Thus at most eight
labelled edges can change their internal/noninternal status with respect
to \(S\), proving (3.14).  A complete slot layer consists of exactly
\(C_{m-2}\) rectangles.  Telescope over the rectangles and then over the
\(t\) layers to obtain (3.15).  Since (3.15) is uniform in \(S\), applying
it to minimizers on the two sides proves (3.16). \(\square\)

Because \(C_{m-2}=(1/16+o(1))B\), every \(t=o(m)\) slot bank changes the
best possible middle-collision value by only

\[
 16tC_{m-2}=o(mB)=o(W).                              \tag{3.17}
\]

Thus, if the canonical complement graph has a macroscopic
prescribed-density induced-edge minimum, a bounded or sublinear number of
slot layers cannot repair it.  The extensive choice \(t=\Theta(m)\) is
the first scale at which this graph obstruction can move by \(\Theta(W)\).
This statement is conditional on the canonical minimum being macroscopic;
no such expansion theorem is asserted here.

## 4. Cyclic interval locality and the exact action budget

The following elementary statement is useful beyond the reciprocal-
\(C_8\) bank.

### Lemma 4.1 (adjacent-transposition locality)

Let \(\pi\) be a cyclic order on \(n\) distinct labels, let
\(1\le r<n\), and interchange two adjacent positions.  Exactly two
indexed length-\(r\) windows can change: the window ending at the first
position and the window beginning at the second.  Therefore

\[
 |E_r(\pi)\triangle E_r(\pi')|\le4.                 \tag{4.1}
\]

At \(r=1\) and \(r=n-1\), the unlabelled target sets in fact agree, but
the upper bound remains valid.

#### Proof

A window changes only if it contains exactly one of the two transposed
positions.  For two adjacent positions there are exactly two such cyclic
windows, with starts \(t-r+1\) and \(t+1\).  Replacing two old occurrences
by two new occurrences gives (4.1). \(\square\)

### Lemma 4.2 (contiguous-block locality)

Suppose \(\pi'\) is obtained from \(\pi\) by arbitrarily permuting the
labels in one contiguous block of \(\ell\) positions.  If

\[
                         \ell\le r,\qquad \ell\le n-r,       \tag{4.2}
\]

then at most

\[
                              2(\ell-1)              \tag{4.3}
\]

indexed length-\(r\) windows can change.  For disjoint blocks satisfying
(4.2), the sum of (4.3) is a valid upper bound.

#### Proof

A window disjoint from the block is unchanged.  A window containing the
whole block is unchanged as a set.  A potentially changed window must cut
one of the two block boundaries.  There are \(\ell-1\) windows which
enter through either boundary without containing the other one.  Condition
(4.2) keeps the two lists disjoint, giving (4.3).  A union bound proves the
last assertion. \(\square\)

For equal-mass integral histograms \(\mu,\nu\), write

\[
                         \mathsf A(\mu,\nu)
 ={1\over2}\|\mu-\nu\|_1.                           \tag{4.4}
\]

This is the number of occurrence units which must be moved.  The number of
uncovered targets is \(1\)-Lipschitz in \(\mathsf A\): moving one unit can
alter the hole count by at most one.

### Corollary 4.3 (extensive-bank annular action)

Let \(\mu_r^0,\mu_r^1\) be the complete rank-\(r\) histograms of the
canonical and all-on cut-packet catalogues.  Then, for every
\(1\le r<2m\),

\[
 \boxed{
 \mathsf A(\mu_r^0,\mu_r^1)
 \le2D_{\rm edit}=8uC_{m-2}.}                        \tag{4.5}
\]

At a paired annular depth \(q\), lower rank \(m-q\) and upper rank
\(m+q\) together have action at most

\[
                         4D_{\rm edit}=16uC_{m-2}.   \tag{4.6}
\]

Across all \(q_0\le q\le H\), the bound is

\[
 \boxed{
 4(H-q_0+1)D_{\rm edit}
 =\bigl(\alpha+o(1)\bigr)(H-q_0+1)W.}               \tag{4.7}
\]

#### Proof

Resolve the row edits into the \(D_{\rm edit}\) adjacent transpositions
counted in (3.6).  Lemma 4.1 changes at most two occurrence starts per
transposition, which proves (4.5).  Apply the same statement to the
complementary upper length and sum first over the two signs, then over
the depths. \(\square\)

Thus the extensive bank has the correct order of raw all-depth action:
\(\Theta(W)\) per Gaussian depth and \(\Theta(W\sqrt m)\) across a fixed
Gaussian annulus.  This is only an upper capacity.  Orbit cancellations,
repeated new targets, or a bad choice of the selected row set may make the
productive action much smaller.

The same lemma gives a rigorous bounded-fringe obstruction.  Suppose a
Catalan bank changes row \(x\) only inside contiguous blocks of lengths
\(\ell_{x,t}\), and put

\[
 \Lambda=\sum_{x,t}(\ell_{x,t}-1).                  \tag{4.8}
\]

At every rank satisfying the block condition (4.2), its histogram action
is at most \(2\Lambda\).  Therefore repairing an \(\eta W\) hole defect
at even one such rank requires

\[
                         \Lambda\ge {\eta\over2}W.   \tag{4.9}
\]

Since \(B=W/(m+1)\), the mean positional block action per Catalan row is
then \(\Omega_\eta(m)\).  In particular, a positive-density family with
\(o(m)\) block width per row cannot repair a macroscopic fixed-depth
defect.  This is an exact locality obstruction, not an entropy heuristic.
The extensive bank meets the necessary root-scale order in (4.9).

### Proposition 4.4 (exact orbit-provider cut)

Let

\[
 \Gamma_u=\langle\tau_1,\ldots,\tau_u\rangle
          \cong C_2^u                                      \tag{4.10}
\]

act on subsets of \([2m]\), and let

\[
 \mathcal V_r^0=\bigcup_{x\in D_m}E_r(\pi_x^0)              \tag{4.11}
\]

be the canonical full-catalogue support.  The union of all rank-\(r\)
targets available from all rowwise local cube variants is contained in

\[
                         \Gamma_u\mathcal V_r^0.             \tag{4.12}
\]

Consequently every rowwise packet selection obeys

\[
 \boxed{
 h_q\ge
 N_q-\left|\Gamma_u\mathcal V_{m-q}^0\right|.}               \tag{4.13}
\]

In particular, a necessary condition for
\(\mathrm{ECAP}^{*}_{a,b}(\alpha)\) is

\[
 \boxed{
 \sum_{q=q_0}^{H}
 \left(N_q-\left|\Gamma_u\mathcal V_{m-q}^0\right|\right)
 =o(W).}                                                    \tag{4.14}
\]

#### Proof

For a local mask \(L\subseteq J(x)\), formula (3.3) gives

\[
 \pi_x^L=h\,\pi_y^0,\qquad
 h=\prod_{j\in L}\tau_j\in\Gamma_u,\qquad y=hx.              \tag{4.15}
\]

Coordinate permutations commute with taking cyclic interval targets.
Thus every target of \(\pi_x^L\) is the \(h\)-image of a target in the
canonical row \(\pi_y^0\), proving (4.12).  No selected family can cover a
target outside this provider union, which gives (4.13); summing proves
(4.14). \(\square\)

At rank \(m\), Lemma 1.1 already gives
\(\mathcal V_m^0=\binom{[2m]}m\), so the provider cut is empty there.
At Gaussian lower ranks, (4.14) is a genuine unevaluated statewise test.
The edit moment (0.6) does not imply it.

### Theorem 4.5 (selected-row action ceiling against \(N_{q_0}\))

For \(0\le K\le B\), define the canonical optimal defects

\[
 \mathfrak c_0(K)=
 \min_{\substack{S\subseteq D_m\\|S|=K}}
 \left(2mK-\left|\bigcup_{x\in S}E_m(\pi_x^0)\right|\right),       \tag{4.16}
\]

\[
 \mathfrak h_q^0(K)=
 \min_{\substack{S\subseteq D_m\\|S|=K}}
 \left(N_q-\left|\bigcup_{x\in S}E_{m-q}(\pi_x^0)\right|\right). \tag{4.17}
\]

Let \(\mathcal Q=\{\pi_x^{L_x}:x\in S\}\) be any \(K\)-row packet
family using arbitrary certified local masks \(L_x\subseteq J(x)\), and
put

\[
 Z_K=\max_{\substack{S\subseteq D_m\\|S|=K}}
                         \sum_{x\in S}|J(x)|.                      \tag{4.18}
\]

Then, at every \(1\le q<m\),

\[
 \boxed{
 2mK-\left|\bigcup_{\pi\in\mathcal Q}E_m(\pi)\right|
 \ge \mathfrak c_0(K)-4Z_K,}                                  \tag{4.19}
\]

\[
 \boxed{
 N_q-\left|\bigcup_{\pi\in\mathcal Q}E_{m-q}(\pi)\right|
 \ge \mathfrak h_q^0(K)-4Z_K.}                                \tag{4.20}
\]

For \(u=\lfloor\alpha m\rfloor\) and \(K=K_0\),

\[
 \boxed{
 Z_{K_0}\le
 \left({\alpha e^{-a^2}\over16}+o(1)\right)W,\qquad
 4Z_{K_0}\le
 \left({\alpha\over4}+o(1)\right)N_{q_0}.}                    \tag{4.21}
\]

In particular, because \(\alpha<1/2\), rowwise reciprocal-\(C_8\)
variants can repair at most

\[
                         \left({1\over8}+o(1)\right)N_{q_0}       \tag{4.22}
\]

of a canonical fixed-depth defect. Thus either
\(\mathfrak c_0(K_0)\) or \(\mathfrak h_{q_0}^0(K_0)\) exceeding
\((\alpha e^{-a^2}/4+\eta)W\), for some fixed \(\eta>0\), is a
statewise obstruction to the entire rowwise cube.

#### Proof

For a chosen rooted row, the ambient-distance part of the reciprocal
\(C_8\) identity says directly that \(\pi_x^{L_x}\) differs from the
same-root canonical order \(\pi_x^0\) by exactly
\(2|L_x|\) adjacent transpositions. By Lemma 4.1 its occurrence action
at any proper rank is at most \(4|L_x|\). The support size, and hence
either displayed defect, is one-Lipschitz in occurrence action. The
canonical roots are the same distinct set \(S\), so its canonical defect
is at least the corresponding minimum (4.16) or (4.17). Summing the
action bounds proves
(4.19)--(4.20).

It remains to estimate (4.18). Put \(z_x=|J(x)|\). Equations
(3.7)--(3.11) give

\[
 {1\over B}\sum_xz_x={\alpha m\over8}+O_\alpha(1),\qquad
 {1\over B}\sum_x(z_x-\bar z)^2=O_\alpha(m).        \tag{4.24}
\]

For every \(K\)-set \(S\), Cauchy--Schwarz gives

\[
 \sum_{x\in S}z_x
 \le K\bar z+sqrt{K\sum_{x\in D_m}(z_x-\bar z)^2}. \tag{4.25}
\]

With \(K=K_0=(e^{-a^2}/2+o(1))B\), the first term is

\[
 \left({\alpha e^{-a^2}\over16}+o(1)\right)mB
 =\left({\alpha e^{-a^2}\over16}+o(1)\right)W,      \tag{4.26}
\]

whereas the square-root term is \(O_\alpha(B\sqrt m)=o(W)\).
This proves the first part of (4.21). Since
\(N_{q_0}=(e^{-a^2}+o(1))W\), the second part and (4.22) follow.
\(\square\)

## 5. Supply and physical compilation

By (0.3),

\[
 {K_0\over B}={e^{-a^2}\over2}+o(1)<{1\over2}.      \tag{5.1}
\]

By Proposition 3.2, the all-on factor contains
\((1-O(1/m))B\) changed rows.  Hence, for every fixed \(a>0\) and all
sufficiently large \(m\), one can choose \(K_0\) genuinely changed
ordinary packets from this one literal factor.  This proves packet supply,
but not trace dispersion.

Every ordinary cyclic order on \([2m]\) gives a strongly \(H\)-safe
middle Johnson cycle whenever \(H<m\): the two uses of one coordinate in
the cyclic swap sequence are separated by \(m\) transitions.  The cyclic
erosion compiler therefore realizes one selected packet in length

\[
                             2m+2H.                  \tag{5.2}
\]

For \(K_0\) selected packets, the physical component count and collar are

\[
 K_0=\left({e^{-a^2}\over2}+o(1)\right)B
 =\Theta_a(W/m)=o(W/H),                              \tag{5.3}
\]

\[
 2HK_0\le {H\over m}N_{q_0}
 =O_{a,b}(W/\sqrt m)=o(W).                           \tag{5.4}
\]

These are the physical cycles in the final OR word.  They are not the
Boolean components of the comparison overlay in (3.13).

For a common factor state \(F^A\) and row set \(S\), Theorem 2.3 gives
the exact middle union size

\[
 \left|\bigcup_{x\in S}E_m(\pi_x^A)\right|
 =2m|S|-2e_{G_{F^A}}(S).                             \tag{5.5}
\]

At lower depth \(q\), put

\[
 h_q(S,A)=N_q-\left|\bigcup_{x\in S}
                         E_{m-q}(\pi_x^A)\right|.    \tag{5.6}
\]

The upper hole count equals \(h_q(S,A)\), because complementation sends
the lower interval family bijectively to the upper interval family at
the antipodal starts.

Concatenate the \(|S|=K_0\) packet words, append every absent middle owner
once, and append every absent signed annular target once.  Equations
(5.2), (5.5), and (5.6) give the exact length

\[
 \boxed{
 W+2e_{G_{F^A}}(S)+2HK_0
             +2\sum_{q=q_0}^{H}h_q(S,A).}            \tag{5.7}
\]

This proves (0.11).

## 6. The exact remaining lemmas

The common-factor sublane has the following precise target.

> **Extensive Catalan annulus packet lemma
> \(\mathrm{ECAP}_{a,b}(\alpha)\).**  For some fixed
> \(0<\alpha<1/2\), with \(u=\lfloor\alpha m\rfloor\) disjoint slots,
> there are global masks \(A_m\subseteq[u]\) and row sets
> \(S_m\subseteq D_m\) such that
> \[
> |S_m|=K_0,
> \qquad e_{G_{F^{A_m}}}(S_m)=o(W),                  \tag{6.1}
> \]
> and
> \[
> \sum_{q=q_0}^{H}h_q(S_m,A_m)=o(W).                \tag{6.2}
> \]

By (5.7), \(\mathrm{ECAP}_{a,b}(\alpha)\) gives a literal fixed-annulus
word of length \(W+o(W)\).  It preserves integrality and uses actual
ordinary cyclic packets; no fractional row, incomplete factor, or
post-selected internal decoration occurs.

The actual packet compiler permits a strictly weaker statement.

> **Rowwise extensive Catalan annulus packet lemma
> \(\mathrm{ECAP}^{*}_{a,b}(\alpha)\).**  There are a row set
> \(S_m\subseteq D_m\), \(|S_m|=K_0\), and local masks
> \(L_x\subseteq J(x)\), \(x\in S_m\), such that, for the individually
> certified packets
> \[
> \mathcal Q_m=\{\pi_x^{L_x}:x\in S_m\},
> \]
> one has
> \[
> 2mK_0-\left|\bigcup_{\pi\in\mathcal Q_m}E_m(\pi)\right|
> =o(W),                                             \tag{6.3}
> \]
> and
> \[
> \sum_{q=q_0}^{H}
> \left[
> N_q-\left|\bigcup_{\pi\in\mathcal Q_m}E_{m-q}(\pi)\right|
> \right]=o(W).                                      \tag{6.4}
> \]

Every \(\pi_x^{L_x}\) occurs in the literal exact factor \(F^{L_x}\), so
there is no local legality or completion assumption in this statement.
The selected packets need not be rows of one common factor because the
final construction concatenates their separate erosion words.  The exact
length furnished by (6.3)--(6.4) is

\[
 W+
 \left[
 2mK_0-\left|\bigcup_{\pi\in\mathcal Q_m}E_m(\pi)\right|
 \right]
 +2HK_0
 +2\sum_{q=q_0}^{H}
 \left[
 N_q-\left|\bigcup_{\pi\in\mathcal Q_m}E_{m-q}(\pi)\right|
 \right].
\tag{6.5}
\]

Thus \(\mathrm{ECAP}^{*}\) is the sharp literal packet gate, while
\(\mathrm{ECAP}\) is a structured sufficient version with the additional
benefit of the exact complement graph (2.5).

In either version the middle and trace clauses are genuinely coupled.

1. Clause (6.1) asks for a prescribed-density induced subgraph with only
   \(o(mB)\) edges in the cut complement graph.
2. Clause (6.2) asks the same row set to be an all-depth coloured partial
   factor: its rank-\(q_0\) intervals and every consecutive deeper path
   intersection must have aggregate leave \(o(W)\).

The extensive bank removes three former objections: insufficient Catalan
row count, bounded-fringe action, and physical component/seam cost.  It
does not remove the grouped selection obstruction.  The full-factor
coordinate-orbit identities also do not settle (6.1)--(6.2): they apply
after summing all \(B\) rows, whereas the annulus uses a selected set of
only \((e^{-a^2}/2+o(1))B\) rows.  Conversely, the large edit mass
(0.6) does not prove that the selected new targets are distinct.

## 7. Proved boundary

The following statements are proved.

1. There are \(2^{\Theta(m)}\) literal global reciprocal-\(C_8\) states
   on one Catalan base, and every state is an anchored exact factor.
2. The all-on state changes \(1-O(1/m)\) of the rows and has exact edit
   mass \(4uC_{m-2}=(\alpha/4+o(1))W\).
3. Infinity cutting produces \(B=C_m\) literal ordinary even packets.
   Their primary middle owners partition \(\binom{[2m]}m\).
4. For every common factor state, selected-packet middle collision is
   exactly twice the induced-edge count in a loopless
   \((m-1)\)-regular complement multigraph.
5. The packet supply exceeds the corrected demand
   \(K_0=(e^{-a^2}/2+o(1))C_m\), even when only genuinely changed rows
   are allowed.
6. The final physical packet count is \(o(W/H)\) and its exact collar is
   \(o(W)\).
7. Bounded or \(o(m)\)-width row rewrites cannot repair a macroscopic
   fixed-depth defect; the extensive bank attains the necessary
   root-scale order.
8. Every rowwise cube target lies in the explicit orbit-provider union
   \(\Gamma_u\mathcal V_r^0\); failure of (4.14) is a literal hereditary
   obstruction.

The following statements remain open and are not claimed:

* some global cube state and some \(K_0\)-row subset simultaneously
  satisfy (6.1)--(6.2);
* more weakly, independently chosen certified row variants satisfy the
  sharp literal conditions (6.3)--(6.4).

This is the precise proved/conditional boundary of the positive-density
Catalan non-row-power lane.
