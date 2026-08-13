# Pair-cell long-run clocks: exact leave, literal source fan, and the splice/cap gate

**Date:** 2026-08-13  
**Status:** unconditional product-cell theorem and exact reduction.  It gives a
`q`-biresident owner cycle factor on all but an explicitly counted exponentially small
fraction of the odd middle layer.  Every component is already a literal depth-`q-1`
source clock and has simple immediate palettes internally.  The theorem also gives the
exact transition-collar splice test and the exact fixed-atlas source-cap test.  It does
not absorb the exceptional cells, make the palettes globally exact, or prove that an
arbitrary lower atlas passes the cap.

## 1. Odd middle-layer pair cells

Put

\[
                         k=2R-1,\qquad p=R-1,
 \qquad \mathcal O={ [k]\choose R},\qquad W=|\mathcal O|. \tag{1.1}
\]

Distinguish one coordinate `z` and partition the remaining `2p` coordinates into
ordered pairs

\[
                         P_i=\{a_i,b_i\},\qquad 1\le i\le p. \tag{1.2}
\]

For an owner `T`, put `epsilon=1_(z in T)`.  On the paired coordinates record the
indices on which `T` is double, empty, or singleton.  If `m` is the number of singleton
pairs and `s=R-epsilon`, then

\[
 a={s-m\over2},\qquad b=p-m-a                              \tag{1.3}
\]

are the numbers of double and empty pairs.  Fixing `epsilon` and the three occupancy
sets gives an induced cube `Q_m`: its bits choose one of `a_i,b_i` on each singleton
pair.  Flipping one bit is exactly one Johnson exchange.

The number of owners in dimension-`m` cells in sector `epsilon` is

\[
 N_m^{(\epsilon)}
 =\binom p m\binom{p-m}{a}2^m
 ={p!2^m\over m!a!b!},                                    \tag{1.4}
\]

when `a,b` are nonnegative integers, and zero otherwise.  These cells partition the
whole owner layer, so

\[
             \sum_{\epsilon=0}^1\sum_mN_m^{(\epsilon)}=W. \tag{1.5}
\]

## 2. Long-run cycles and exact leave

Let `q>=2`, and define the safe threshold

\[
                         M=q+\lceil3\log_2 p\rceil.        \tag{2.1}
\]

Assume `M<=p`.  Goddyn--Gvozdjak give every cube `Q_m`, `m>=M`, a cyclic Hamilton
Gray code whose repeated transition directions have cyclic separation at least

\[
                 m-3\log_2m\ge q.                         \tag{2.2}
\]

Embed one such cycle in every pair cell of dimension at least `M`.

### Theorem 2.1 (exact good-cell factor)

The embedded cycles form a vertex-disjoint Johnson cycle factor on precisely

\[
 \mathcal O_{\rm good}=\{T:\text{the singleton-pair count of }T\text{ is at least }M\}.
                                                                    \tag{2.3}
\]

Every physical coordinate has all cyclic positive and zero owner runs of length at
least `q`.  Inside each component, its immediate-lower intersections and
immediate-upper unions are separately pairwise distinct.

#### Proof

The cells partition the owner layer, and each Gray code is Hamilton in its cell.
Coordinates in fixed double, empty, and sentinel positions are constant.  On a
singleton pair, both physical coordinates change membership precisely at transitions
in its cube direction.  Equation (2.2) therefore gives both positive and zero run
floors `q`.

An internal cube edge is recovered from its lower intersection: the toggled pair is
the newly empty pair and all other singleton choices remain visible.  It is likewise
recovered from its upper union, where the toggled pair is newly double.  Distinct cube
edges hence have distinct lower values and distinct upper values.  A Hamilton cycle has
no repeated edges. \(\square\)

The omitted owner count is exactly

\[
 \boxed{
 L_{p,q}=\sum_{\epsilon=0}^1
         \sum_{\substack{m<M\\a,b\in\mathbb Z_{\ge0}}}
         {p!2^m\over m!a!b!}.}                           \tag{2.4}
\]

For `M<=p/2`, it obeys the explicit bound

\[
 \boxed{
 {L_{p,q}\over W}
 \le (2p+2)2^{-p}\sum_{m<M}\binom p m
 \le (2p+2)2^{-p}\left({ep\over M}\right)^M.}            \tag{2.5}
\]

Indeed, for fixed `epsilon,m`, the occupancy choice in (1.4) is at most
`2^p binom(p,m)`, while
`W=binom(2p+1,p+1)>=2^(2p+1)/(2p+2)`.  The last inequality is the standard lower-tail
binomial bound.

At the OR-word scale `q=Theta(sqrt p)`, (2.5) is

\[
                         \exp\{-\Theta(p)\}.              \tag{2.6}
\]

This is exponentially small **as a proportion**, but `L_(p,q)` is still exponentially
large in absolute value.  It cannot be charged as an `O(1)` leave.

## 3. Every good cell is already a direct `q`-window clock

Let one good cycle be

\[
                         T=(T_i)_{i\in\mathbb Z_{2^m}}.
\]

Define its maximal depth-`q-1` antecedent

\[
                         P_t=\bigcap_{u=0}^{q-1}T_{t-u}.   \tag{3.1}
\]

### Theorem 3.1 (literal cell clock and complete consecutive fan)

The letters `P_t` are nonempty and

\[
                         \bigcup_{t=i}^{i+q-1}P_t=T_i.     \tag{3.2}
\]

Moreover, for every `0<=ell<=q-1`,

\[
 \boxed{
 \bigcap_{j=0}^{\ell}T_{i+j}
 =\bigcup_{h=\ell}^{q-1}P_{i+h}.}                         \tag{3.3}
\]

The left side has rank `R-ell`.  Thus every consecutive-intersection fan through
depth `q-1` is materialized occurrence-injectively by literal suffix cells of one
source word.

#### Proof

No transition coordinate repeats among `q` consecutive cycle edges.  Hence the
intersection of `q` consecutive owners deletes exactly `q-1` distinct coordinates
from its first owner and has rank `R-q+1>0` in the intended range.  The positive-run
floor gives the maximal-antecedent identity (3.2).

For (3.3), a coordinate belongs to the left side exactly when its positive owner run
contains `[i,i+ell]`.  Since every such run has at least `q` vertices, it contains a
length-`q` erosion window ending at some `i+h`, `ell<=h<=q-1`; that is exactly
membership in one of the letters on the right.  The reverse inclusion is immediate.
Distinct pairs `(i,ell)` use distinct physical suffix intervals, giving occurrence
injectivity. \(\square\)

This is a direct middle-layer clock, not merely a residence statistic.  Its limitation
is coverage: it realizes the consecutive fan chosen by the cube cycle, not every named
lower target globally.

## 4. Exact analytic splice criterion

For a Johnson edge `T_iT_(i+1)`, put

\[
                         E_i=T_i\mathbin\triangle T_{i+1}. \tag{4.1}
\]

Thus `E_i` is the two-coordinate transition support.

### Lemma 4.1 (transition-collar criterion)

A cyclic Johnson trace is `q`-biresident if and only if every `q` consecutive edge
supports are pairwise disjoint as coordinate sets:

\[
 E_i,E_{i+1},\ldots,E_{i+q-1}
 \quad\text{contain no repeated physical coordinate}.     \tag{4.2}
\]

Consequently, when internally `q`-biresident paths are joined, the join is
`q`-biresident if and only if (4.2) holds for the `q`-edge windows meeting each seam.
Only the two `(q-1)`-edge endpoint collars and the connector transition word need be
examined.

#### Proof

A coordinate changes membership exactly on the edges whose supports contain it.  Its
successive positive and zero runs have lengths equal to the cyclic separations of these
edge occurrences.  A separation below `q` is equivalent to two occurrences lying in
one block of `q` consecutive edges. \(\square\)

This gives an exact finite port graph.  A port consists of an oriented cut together with
its two transition collars.  Draw a directed port arc when a Johnson connector exists
whose transition word passes (4.2) against both collars and whose resource values avoid
the protected bank.  A global resident joining is then a cycle-cover/Hamilton selection
in this port graph, coupled to the owner and palette rows.  Abstract endpoint adjacency
alone is insufficient.

There is one proved local trade.  If two same-dimensional cells differ by transferring
one double status to a singleton pair, coherently relabelled copies of the same Gray
cycle form a twisted Cartesian square.  Cutting the distinguished edge in both cycles
and cross-splicing merges them, while decreasing transition separation by at most one.
Thus a matching of such cell pairs can be fused at no `q`-residence cost when the input
cycles have run at least `q+1`.  This is a matching theorem, not a multiport spanning-
tree theorem.  Cross-dimensional squares require the stronger endpoint-collar test;
the known crude relabelling argument makes it automatic only when the cube dimension is
at least `4q`, outside the critical exceptional window.

## 5. Exact source-cap criterion for a lower atlas

Fix any completed `q`-resident owner chronology `T`, its maximal antecedent `P` from
(3.1), and prospective source intervals `I_S` of width at most `q-1` for named strict-
lower targets `S`.  For every coordinate `x`, put

\[
 Q_x=\{t:x\in P_t\}\setminus
       \bigcup_{S:\,x\notin S}I_S.                       \tag{5.1}
\]

### Theorem 5.1 (fixed-atlas coordinate cap)

There is a nonempty source word `A`, with `A_t subseteq P_t`, satisfying

\[
 \bigcup_{t=i}^{i+q-1}A_t=T_i,
 \qquad
 \bigcup_{t\in I_S}A_t=S                                  \tag{5.2}
\]

for every owner and every selected target if and only if

\[
 Q_x\cap[i,i+q-1]\ne\varnothing
       \quad(x\in T_i),                                    \tag{5.3}
\]

\[
 Q_x\cap I_S\ne\varnothing
       \quad(x\in S),                                      \tag{5.4}
\]

and every source address belongs to at least one `Q_x`.  When these conditions hold,

\[
                         A_t=\{x:t\in Q_x\}                \tag{5.5}
\]

is the coordinatewise maximal solution.

#### Proof

A target omitting `x` forbids `x` throughout its selected interval, so every solution's
`x`-support is contained in `Q_x`.  The positive sides of the owner and target
equalities give (5.3)--(5.4), and nonempty letters give the last condition.  Conversely,
(5.1) excludes every forbidden coordinate, while (5.3)--(5.4) supply every required
coordinate.  Equation (5.5) therefore realizes all equalities. \(\square\)

This criterion answers the arbitrary-atlas question sharply: a product-cell clock is
**not** automatically compatible with an arbitrary `O(W)`-letter lower atlas.  For
example, two negative pins omitting a coordinate that is permanent in the owner block
can cover all positions of one central `q`-window and violate (5.3), even when each pin
is separately feasible.  Pair cells guarantee the maximal fan (3.3); all additional
pins must pass the joint coordinate cap.

## 6. Verdict for the global programme

Pair stratification plus long-run cube codes proves all of the following exactly:

1. a `q`-biresident owner factor outside the leave (2.4);
2. simple immediate palettes inside every component;
3. a literal depth-`q-1` source clock on every component;
4. the complete consecutive-intersection source fan through depth `q-1`;
5. an exact local seam test and an exact arbitrary-atlas cap test.

It does not prove a `B(k)+O(1)` word because three global operations remain coupled:

\[
 \boxed{
 \text{absorb the exponentially many low-dimensional cells}
 \ \longrightarrow\ 
 \text{select globally exact palettes/lower tickets}
 \ \longrightarrow\
 \text{join the components through collar-compatible ports}.}
\]

The first arrow cannot be replaced by declaring the proportional leave small, and the
second cannot be replaced by an arbitrary lower atlas.  A successful product-group
proof therefore needs a run-transparent cross-cell absorber together with the
coordinate cap (5.3)--(5.5), not a stronger within-cube Gray code.

**Primary input:** L. Goddyn and P. Gvozdjak, *Binary Gray Codes with Long Bit Runs*,
Electronic Journal of Combinatorics 10 (2003), R27, DOI `10.37236/1720`.
