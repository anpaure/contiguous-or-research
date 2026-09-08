# Integral wreath circuits: a locality obstruction and a legal global move

## 1. Setting

Put

\[
        n=2m+1,
\]

and let \(\Omega\) be the unoriented cyclic orders of \([n]\).  For
\(C\in\Omega\), write

\[
        \mathcal W_m(C)
\]

for its \(n\) cyclic intervals of size \(m\).  A **partial wreath factor** is
a family of orders whose \(\mathcal W_m(C)\)'s are pairwise disjoint.  A
support-feasible trade is a vector

\[
 z=\sum_{C\in P}e_C-\sum_{C\in N}e_C,
 \qquad B_mz=0,                                      \tag{1.1}
\]

where both \(P\) and \(N\) are partial wreath factors.  It replaces \(N\)
by \(P\) inside any exact factor containing \(N\).

Petr--Turek's rank-\(a\) selector is a four-order square

\[
 q=e_C-e_{\tau C}-e_{\sigma C}+e_{\tau\sigma C},    \tag{1.2}
\]

where \(\tau\) and \(\sigma\) swap two disjoint adjacent pairs of entries
of \(C\), at cyclic separation \(a\).  It lies in \(\ker B_m\) for
\(a<m\), and changes no interval rank other than \(a,n-a\).  The question
addressed here is whether a bounded number of these signed squares can
cancel into an actual trade.

The answer is no.  More precisely, every connected support-feasible circuit
made from these squares uses \(\Omega(m)\) squares.  This rules out the
natural six-order, eight-order and Boolean-cube gadgets.  The obstruction is
metric, not spectral.

## 2. Disjoint wreaths are far apart

For \(C,D\in\Omega\), let \(d_\circ(C,D)\) be the minimum number of swaps of
neighbouring entries of a cyclic word needed to turn a representative of
\(C\) into a representative of \(D\), allowing a final rotation or reversal.

### Lemma 1 (overlap versus adjacent-swap distance)

For all \(C,D\in\Omega\),

\[
 |\mathcal W_m(C)\cap\mathcal W_m(D)|
       \ge n-2d_\circ(C,D).                           \tag{2.1}
\]

Consequently,

\[
 \mathcal W_m(C)\cap\mathcal W_m(D)=\varnothing
       \quad\Longrightarrow\quad
 d_\circ(C,D)\ge m+1.                                \tag{2.2}
\]

#### Proof

Swapping two neighbouring entries of a cyclic order changes exactly the two
length-\(m\) intervals whose boundary separates those entries.  All other
\(n-2\) intervals are unchanged.  Thus one adjacent swap changes the
incidence family by symmetric difference of size four.

Along a shortest sequence of \(d=d_\circ(C,D)\) adjacent swaps, the triangle
inequality for symmetric difference gives

\[
 |\mathcal W_m(C)\mathbin\triangle\mathcal W_m(D)|\le4d.
\]

Both families have size \(n\), so

\[
 |\mathcal W_m(C)\cap\mathcal W_m(D)|
 =n-\tfrac12|\mathcal W_m(C)\mathbin\triangle
                         \mathcal W_m(D)|
 \ge n-2d.
\]

If the families are disjoint, then \(2d\ge n=2m+1\), and hence
\(d\ge m+1\).  QED.

This elementary bound is the relevant integral geometry.  Every four-order
selector has cyclic adjacent-swap diameter at most two, whereas every two
orders on the same side of a legal trade must be at distance at least
\(m+1\).

## 3. A linear lower bound on selector-cell circuits

Consider an expression

\[
                         z=\sum_{j=1}^t\epsilon_jq_j, \tag{3.1}
\]

where \(\epsilon_j\in\{+1,-1\}\) and each \(q_j\) is a relabelled
Petr--Turek square (1.2).  Form the **cell-intersection graph** on
\([t]\), joining two cells when their four-order supports contain a common
cyclic order.  Equal order coordinates in (3.1) are then collected and
cancelled.

### Theorem 2 (mesoscopic selector lower bound)

Suppose the reduced vector \(z\) is a support-feasible trade.  Every
connected component of its cell-intersection graph whose reduced sum is
nonzero contains at least

\[
                         \left\lceil\frac{m+1}{2}\right\rceil            \tag{3.2}
\]

selector cells.

#### Proof

Let a connected component contain \(s\) cells.  The support of one cell has
diameter at most two in \(d_\circ\).  Walking through a spanning tree of the
cell-intersection graph therefore shows that the union of all order supports
in this component has diameter at most \(2s\).

Different components have disjoint order-coordinate supports.  Since every
cell belongs to \(\ker B_m\), the reduced sum of this one component also
belongs to \(\ker B_m\).  It inherits support-feasibility from \(z\).

Assume \(2s\le m\).  Lemma 1 says that every two distinct surviving orders
in the component have a common middle interval.  Hence a partial factor can
contain at most one positive surviving order and at most one negative
surviving order.

The sum of all rows of \(B_mz=0\) says that the number of positive orders
equals the number of negative orders.  A nonzero component would therefore
have the form \(e_C-e_D\).  But \(B_m(e_C-e_D)=0\) says
\(\mathcal W_m(C)=\mathcal W_m(D)\).  For \(m\ge2\), the family of middle
cyclic intervals determines its unoriented cyclic order, so \(C=D\),
contradicting that the reduced component is nonzero.

Thus \(2s\ge m+1\), which is (3.2).  QED.

### Consequences

1. Any fixed number \(t\) of selector squares fails once \(m\ge2t\).
   Rank-local integrality cannot be obtained from a bounded local gadget.

2. For \(m\ge4\), no expression using at most two selector squares can be a
   nonzero support-feasible trade, regardless of how their terms are
   identified or cancelled.  In particular, the natural six-wreath and
   eight-wreath two-square attempts are impossible.

3. More generally, selector circuits must be **mesoscopic**: before they can
   even satisfy the middle packing constraint, they must propagate through
   linearly many adjacent-swap cells.  Energy improvement at rank \(a\) is a
   later issue.

There is also a direct obstruction to the most natural \(2^d\)-order
construction.

### Corollary 3 (no commuting adjacent-swap cube)

Let \(s_1,\ldots,s_d\), \(d\ge2\), be commuting swaps of pairwise disjoint
adjacent pairs in a cyclic order \(C\), and assume the \(2^d\) orbit orders
are distinct.  Then

\[
             \prod_{i=1}^d(1-s_i)e_C                 \tag{3.3}
\]

is not support-feasible for any \(m\ge2\).

#### Proof

The positive parity class in (3.3) contains both \(C\) and
\(s_1s_2C\).  Their distance is at most two, so by Lemma 1 they share at
least \(n-4>0\) middle intervals.  Thus the positive class is not a partial
factor.  QED.

The same test applies to character-sum kernel vectors.  If

\[
       v=\sum_{h\in H}\chi(h)e_{hC}                  \tag{3.4}
\]

is a nonzero Petr--Turek character vector with \(\chi:H\to\{\pm1\}\), then
support-feasibility requires

\[
 d_\circ(C,hC)\ge m+1
 \quad\text{for every }h\in\ker\chi
 \text{ with }hC\ne C.                               \tag{3.5}
\]

Indeed, \(C\) and \(hC\) have the same sign.  This immediately kills the
standard local sign-character choices whose even subgroup contains a
three-cycle on three consecutive entries: that three-cycle has adjacent-swap
length two.

## 4. A legal integral move does exist, but at factor scale

The locality theorem should not be misread as saying that the exact-factor
fibre has no integral moves.  There is a universal one.

### Proposition 4 (transposition trade)

Let \(F\subseteq\Omega\) be any exact middle wreath factor and let \(\pi\)
be a transposition of two ground-set coordinates.  For \(m\ge2\),

\[
                 F\cap\pi F=\varnothing,              \tag{4.1}
\]

and

\[
                 z_\pi={\bf1}_{\pi F}-{\bf1}_{F}      \tag{4.2}
\]

is a support-feasible trade.  It has \(\operatorname{Cat}_m\) orders on
each side.

#### Proof

First observe that every cyclic order \(C\) shares a middle interval with
\(\pi C\).  If \(\pi=(u\ v)\), the total number of incidences of \(u,v\)
among the \(n\) cyclic \(m\)-intervals is \(2m=n-1\).  Therefore not every
interval contains exactly one of \(u,v\).  An interval containing both or
neither is fixed as a set by \(\pi\), and is common to \(C\) and \(\pi C\).

Suppose now that \(C\in F\cap\pi F\).  Then \(C=\pi D\) for some \(D\in F\),
so \(D=\pi C\).  If \(D\ne C\), the preceding common interval contradicts
the pairwise disjointness of the wreaths in \(F\).  If \(D=C\), then a
single transposition stabilizes an unoriented odd cyclic order.  This is
impossible for \(n\ge5\): a nonidentity rotation moves every coordinate and
a reflection fixes one coordinate and swaps \(m\ge2\) pairs.  This proves
(4.1).

Both \(F\) and \(\pi F\) are exact factors, so

\[
                  B_m{\bf1}_{F}=B_m{\bf1}_{\pi F}={\bf1}.
\]

Together with (4.1), this proves (4.2).  QED.

This large trade has a canonical decomposition into smaller legal trades.
Construct a bipartite multigraph with left vertices \(F\), right vertices
\(\pi F\), and one edge for every middle set, joining the unique left and
right wreaths containing it.  Every vertex has degree \(n\), counting edge
multiplicity.  For each connected component \(K\), the wreaths on either side
cover exactly the same set of middle masks.  Hence

\[
     {\bf1}_{K\cap\pi F}-{\bf1}_{K\cap F}             \tag{4.3}
\]

is itself a support-feasible trade.

The component moves have disjoint middle supports and may therefore be
switched independently.  If the interaction graph has components
\(K_1,\ldots,K_c\), then every choice \(J\subseteq[c]\) gives an exact
factor

\[
 \left(F\setminus\bigcup_{j\in J}(K_j\cap F)\right)
       \cup
 \bigcup_{j\in J}(K_j\cap\pi F).                     \tag{4.4}
\]

Thus a single coordinate transposition canonically exposes a genuine
\(c\)-dimensional cube **inside the exact-factor fibre**.  This is very
different from the forbidden order-level cube (3.3): its coordinates are
whole interaction components, so both ends of every coordinate move are
already partial factors.

The component trades (4.3), rather than isolated four-order selectors, are
the first natural integral generators of the exact-factor fibre.  Their
actions at noncentral ranks are coupled.  A viable successor theorem would
show that suitable combinations of these genuine component trades span or
approximately span the same rank-local discrepancy spaces that the signed
Petr--Turek selectors span over \(\mathbb R\).  Concretely, if
\(\delta_{K,r}\) denotes the rank-\(r\) effect of (4.3), choosing a subset in
(4.4) is an exact vector-balancing problem for the family
\((\delta_{K,r})_{K,r}\), with no subsequent rounding back to the middle
fibre.

## 5. The complementary-path involution is not a shortcut

Fix a distinguished coordinate and use the complementary Johnson-path
normal form on \([2m]\).  Thus a block is

\[
       P=(P_0,P_1,\ldots,P_m),\qquad
       P_m=\overline{P_0},                            \tag{5.1}
\]

and an exact path factor partitions all rank-\(m\) vertices while its edge
unions partition rank \(m+1\).  Define

\[
       P_i^*=\overline{P_{m-i}}.                       \tag{5.2}
\]

Then

\[
 \begin{aligned}
 P_i^*\cup P_{i+1}^*
   &=\overline{P_{m-i}\cap P_{m-i-1}},                \tag{5.3}\\
 P_0^*&=P_0,\qquad P_m^*=P_m.                          \tag{5.4}
 \end{aligned}
\]

### Proposition 5 (exact star obstruction)

Let \(\mathcal P\) be an exact complementary path factor.

1. The starred paths \(\mathcal P^*=\{P^*:P\in\mathcal P\}\) partition the
   rank-\(m\) vertices automatically.

2. They form an exact wreath factor if and only if the lower edge colours

   \[
              P_i\cap P_{i+1}
   \]

   of \(\mathcal P\) are all distinct, equivalently enumerate rank
   \(m-1\).

3. Two distinct paths \(P,P^*\) cannot both occur as blocks of one exact
   path factor, because they share the endpoints (5.4).

4. If \(\mathcal P=\mathcal P^*\) as a block family, then every block must
   satisfy \(P=P^*\).  For even \(m\), this is impossible, since at the
   middle index it would require

   \[
                      P_{m/2}=\overline{P_{m/2}}.
   \]

#### Proof

Complementation permutes all rank-\(m\) sets, proving part 1.  Formula (5.3)
says that the starred upper edge colours are exactly the complements of the
original lower edge colours.  The two ranks have equal size, so they
partition rank \(m+1\) exactly when the original lower colours partition
rank \(m-1\).  This proves part 2.

Part 3 follows from (5.4) and the fact that path blocks in a factor are
vertex-disjoint.  Consequently setwise invariance under star can only fix
blocks individually.  When \(m\) is even, (5.2) at \(i=m/2\) gives the
impossible equality in part 4.  QED.

Thus pairing paths with their stars inside one factor is impossible, not
merely obstructed by the parity of the number of Catalan blocks.  Moreover,
global starring produces another exact factor precisely after the desired
first lower shadow has already been solved.  The involution diagnoses the
two-sided condition but does not construct it.

## 6. Consequence for the global program

The continuous rank-selector theorem remains valuable: it proves that no
real-linear obstruction exists and that different ranks decouple before
integrality.  The present results locate the cost of integrality more
precisely.

* Every direct local cube fails.
* Every connected selector circuit has linear-in-\(m\) cell size.
* Star symmetrization is equivalent to, rather than a proof of, the first
  two-sided shadow condition.
* Exact-factor component switches (4.3) are genuine integral moves, but their
  vertical actions are not rank-local.

Accordingly the next mathematically honest target is:

> Prove an expansion theorem for the rank-\(a\) action of transposition
> component trades, or construct a mesoscopic \(\Omega(m)\)-cell selector
> strip whose two boundary sign classes are cyclic-order codes of minimum
> adjacent-swap distance at least \(m+1\).

Either theorem would bridge the current gap.  Searching for another bounded
six/eight-order cancellation cannot.
