# Grouped owner paths: a linear atomic-to-deck gap, an integral-demand odd cycle, and the reroot cycle-rank gate

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver, web
input, or probabilistic black box is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad \kappa=4H-1,\qquad
 d=M-\kappa=m-3H+1,
\tag{0.1}
\]

and assume the calibrated range

\[
 H\to\infty,\qquad H=o(m),\qquad d\ge 2H+3.
\tag{0.2}
\]

For a top \(U\in\binom{[n]}M\), a literal retained row is the
complement of the \(d\) consecutive \(H\)-windows of an injective word
of length \(d+H-1\).  The atomic owner flow forgets that consecutive
window condition.

This note establishes three exact boundaries for lifting the atomic
flow back to literal rows.

1. **A linear one-top gap.**  There is a set \(F_U\) of exactly \(d\)
   distinct owners contained in one top \(U\) such that the atomic
   assignment uses all of \(F_U\), whereas every literal retained row
   on \(U\) uses at least

   \[
                         \lfloor d/2\rfloor
   \tag{0.3}
   \]

   owners outside \(F_U\).  Thus arbitrary integral top--owner
   \(b\)-matchings cannot even be rounded to grouped decks with
   \(o(m)\) error per top.  This strengthens the previously recorded
   one-window nonmatroid obstruction from a one-unit defect to a linear
   defect.

2. **An integral-demand odd cycle.**  There are three rank-\(M\) tops,
   with two explicitly constructible legal retained decks on each,
   such that:

   * the fractional choice \(1/2,1/2\) at every top satisfies every
     owner capacity and has top load one;
   * the same owner union has an integral atomic allocation of \(d\)
     distinct owners to every top; but
   * no integral choice of one of the two legal decks at each top is
     owner-disjoint.

   The obstruction is exactly the impossibility of two-colouring an
   odd triangle.  Hence the time-expanded path formulation is a
   genuinely coupled path-packing problem; it is not a network matrix,
   even when the top right-hand side is integral.

3. **The exact cheap-reroot gate for repaired twelve-top sources.**  For
   a current cyclic word table \(T\), define a graph \(G_C(T)\) on the
   labels outside every \((M-2)\)-core \(C\).  An edge \(xy\) is present
   precisely when the current word on \(C+\{x,y\}\) can be rerooted so
   that \(x,y\) occupy the two placeholder positions of a recharge
   source.  Then

   \[
    \sum_C |E(G_C(T))|=MN,
   \tag{0.4}
   \]

   while, writing \(s=n-M+2\),

   \[
    \frac1{\binom n{M-2}}\sum_C|E(G_C(T))|
      =\frac{s(s-1)}{M-1}
      =(s-1)-\frac{(s-1)(2H-3)}{M-1}.
   \tag{0.5}
   \]

   Thus the mean graph lies about \(2H\) edges **below** the forest
   threshold.  Counting cannot force even one carrier cycle.  More
   sharply, every top-disjoint bank of reroot-realizable repaired
   twelve-top sources satisfies

   \[
       2|\mathcal B|
       \le \sum_C \beta(G_C(T)),
   \tag{0.6}
   \]

   where \(\beta(G)=|E(G)|-|V(G)|+c(G)\) is cycle rank.  A state with
   forest \(G_C(T)\)'s has no such source at all, despite the exact
   atomic Hall theorem.

   Conversely, if a top-disjoint family of \(p\) repaired packet
   sources is literally obtainable only by rerooting current words,
   replacing its \(12p\) rows changes at most

   \[
                         12\kappa p
   \tag{0.7}
   \]

   middle-owner occurrences.  Even for \(p=\Theta(N)\), this is
   \(O(HN)=o(W)\).  Therefore cheap physical installation has been
   reduced to a **decorated cycle-rank/matching property of the current
   state**, not to scalar owner capacity.

The positive implication in Item 3 is conditional on actual decorated
source compatibility.  The uncoloured graphs \(G_C(T)\) record the
necessary carrier cycles, not the endpoint palettes and filler-column
identity.  The note therefore does not prove a positive-density source
layer.  It proves why an arbitrary atomic matching cannot be lifted and
identifies a sharp, statewise low-cost route which would suffice.

## 1. Deleted-window paths

Let

\[
 w=(w_1,\ldots,w_{d+H-1})
\tag{1.1}
\]

be injective and put

\[
 J_i(w)=\{w_i,w_{i+1},\ldots,w_{i+H-1}\},
 \qquad 1\le i\le d.
\tag{1.2}
\]

The retained owner deck on \(U\) is

\[
 D_U(w)=\{U\setminus J_i(w):1\le i\le d\}.
\tag{1.3}
\]

All its members are distinct.  In the Johnson graph on
\(\binom UH\),

\[
 |J_i(w)\cap J_j(w)|=H-1
 \quad\Longleftrightarrow\quad |i-j|=1.
\tag{1.4}
\]

Consequently the graph induced by the deleted windows is exactly the
path \(P_d\).  This is the grouped condition lost by the atomic
containment flow.

## 2. A linear one-top integrality gap

### Theorem 2.1 (independent-window reservoir)

For every sufficiently large \(m\), there is a family

\[
                         \mathcal A_U\subseteq\binom UH,
 \qquad |\mathcal A_U|=d,
\tag{2.1}
\]

which is independent in the Johnson graph \(J(M,H)\).  If

\[
                         F_U=\{U\setminus J:J\in\mathcal A_U\},
\tag{2.2}
\]

then every literal retained row \(D\) on \(U\) satisfies

\[
                         |D\cap F_U|\le\lceil d/2\rceil,
\tag{2.3}
\]

and hence

\[
                         |D\setminus F_U|\ge\lfloor d/2\rfloor.
\tag{2.4}
\]

#### Proof

The Johnson graph \(J(M,H)\) has degree \(H(M-H)\).  A greedy
independent-set construction therefore gives an independent set of
size at least

\[
                   \frac{\binom MH}{1+H(M-H)}.
\tag{2.5}
\]

In the range (0.2), (2.5) is much larger than \(m\), and hence larger
than \(d\).  Select any \(d\) of its vertices to obtain
\(\mathcal A_U\).

For a literal row, (1.4) identifies its deleted-window graph with
\(P_d\).  Its intersection with the Johnson-independent family
\(\mathcal A_U\) is an independent set in \(P_d\), of size at most
\(\lceil d/2\rceil\).  Complementation inside \(U\) gives (2.3), and
(2.4) follows. \(\square\)

### Corollary 2.2 (atomic saturation can be linearly far from physical)

The reservoir \(F_U\) has scalar capacity exactly \(d\), and assigning
all of it to the top is a valid integral atomic assignment.  No literal
row is contained in this reservoir.  In fact every literal row differs
from that atomic bundle in at least \(\lfloor d/2\rfloor=\Theta(m)\)
positive owner occurrences.

Thus no theorem of the form

\[
 \text{integral atomic }b\text{-matching}
 \Longrightarrow
 \text{literal rows with }o(m)\text{ changes per top}
\tag{2.6}
\]

can hold for arbitrary residual owner sets.  Special trajectory or
state structure is indispensable.

## 3. A three-top odd cycle with integral top demands

The determinant-two minor in the ordinary-frame note has fractional
top load \(1/2\).  The next construction removes that qualification.

Choose pairwise disjoint sets

\[
 |C|=m-H+2,\qquad |B_0|=|B_1|=|B_2|=H-1.
\tag{3.1}
\]

They use \(m+2H-1\le2m\) labels.  With indices modulo three, put

\[
                         U_i=C\cup B_{i-1}\cup B_i.
\tag{3.2}
\]

Then \(|U_i|=M\), and

\[
                         U_i\cap U_{i+1}=C\cup B_i,
 \qquad |U_i\cap U_{i+1}|=m+1.
\tag{3.3}
\]

Choose six distinct labels \(a_i,b_i\in C\), and define two
rank-\(m\) pair owners

\[
 X_i=(C\cup B_i)\setminus\{a_i\},\qquad
 Y_i=(C\cup B_i)\setminus\{b_i\}.
\tag{3.4}
\]

### Lemma 3.1 (two endpoint owners and no other cross owner)

For every \(i\), there is a literal deck \(A_i\) on \(U_i\) which
contains \(X_{i-1},X_i\) and whose only owners contained in another
displayed top are those two.  There is likewise a deck \(B_i'\) which
contains \(Y_{i-1},Y_i\) and no other owner contained in another
displayed top.

#### Proof

Inside \(U_i\), the deleted \(H\)-windows complementary to the two
desired \(X\)-owners are

\[
 B_i\cup\{a_{i-1}\},\qquad
 B_{i-1}\cup\{a_i\}.
\tag{3.5}
\]

They are disjoint.  Put the first set in positions \(1,\ldots,H\) of
an injective word and the second in the last \(H\) positions
\(d,\ldots,d+H-1\).  Fill the intervening positions injectively from
the remaining labels.  At the first endpoint put a member of \(B_i\)
in position one.  At the last endpoint put a member of \(B_{i-1}\) in
the final position.

An owner of a row on \(U_i\) can also lie in \(U_{i-1}\) only when its
deleted window contains the complete exclusive block \(B_i\).  By the
endpoint ordering, only the first window contains that block: after
one shift a member of \(B_i\) has left and never re-enters.  Similarly,
only the last window contains the complete block \(B_{i-1}\).  Thus
the only cross-top owners are the two prescribed ones.  This constructs
\(A_i\).  Replace every \(a\) by the corresponding \(b\) to construct
\(B_i'\). \(\square\)

The unused filler orders may be chosen so that each \(B_i'\) has at
least two private owners not in \(A_i\).  Here is a direct choice.  For
sufficiently large \(m\), choose two disjoint \(H\)-subsets
\(Z_1,Z_2\subset C\), avoiding the at most \(d\) deleted windows of
\(A_i\), and place them as two separated interior \(H\)-blocks of the
word for \(B_i'\).  There is room because \(m/H\to\infty\).  Their
complementary owners contain both blocks \(B_{i-1},B_i\), so they are
contained in neither other displayed top and are private.  They do not
belong to \(A_i\) by construction.

### Theorem 3.2 (integral-demand grouped odd cycle)

Restrict the row catalogue on \(U_i\) to the two options
\(A_i,B_i'\).  Then the path-packing LP has the feasible point

\[
                         x(A_i)=x(B_i')=\frac12
                         \qquad(i=0,1,2),
\tag{3.6}
\]

which gives top load one and owner load at most one everywhere.  There
is no integral selection of one row on every top.  Nevertheless the
union of the six options admits an integral atomic assignment of \(d\)
distinct owners to every top.

#### Proof

By Lemma 3.1, two options on different tops meet precisely as follows:

\[
 A_i\cap A_{i+1}=\{X_i\},\qquad
 B_i'\cap B_{i+1}'=\{Y_i\},\qquad
 A_i\cap B_{i+1}'=B_i'\cap A_{i+1}=\varnothing.
\tag{3.7}
\]

Thus (3.6) loads every \(X_i,Y_i\) exactly one.  A private owner lies
on only one displayed top and hence in at most its two listed options,
so its load is at most one.  The top equations are also exact.

An integral choice assigns each top colour \(A\) or \(B\).  Adjacent
tops cannot both receive colour \(A\), because they would repeat
\(X_i\); they cannot both receive colour \(B\), because they would
repeat \(Y_i\).  It would therefore be a proper two-colouring of a
triangle, which is impossible.

For the atomic assignment on \(U_i\), take the \(d-2\) private owners
of \(A_i\), and add two private owners of \(B_i'\setminus A_i\).
Private owners belonging to different displayed tops are distinct by
Lemma 3.1.  This supplies \(d\) distinct contained owners to each top
with no global repetition. \(\square\)

The theorem is a restricted-catalogue obstruction.  It does not say
that the complete row catalogue on these three tops is deficient; in
fact the abundance results for complete catalogues point the other
way.  It proves the exact logical boundary needed here: a generic
augmenting-path or total-unimodularity theorem for arbitrary permitted
grouped-deck lists is false even with integral top demands and a
simultaneously feasible atomic allocation.

## 4. The cheap-reroot carrier graphs

Return to a current table \(T\) with one rooted cyclic word \(\pi_U\)
on every top.  The repaired recharge source has its near placeholder
at rooted position \(1\) and its far placeholder at position \(d+1\).
Their cyclic separation is

\[
                         M-d=\kappa.
\tag{4.1}
\]

For every \((M-2)\)-set \(C\), let \(G_C(T)\) be the simple graph on

\[
                         V_C=[n]\setminus C,
 \qquad |V_C|=s=n-M+2,
\tag{4.2}
\]

in which \(xy\) is an edge when, in the underlying cyclic order on
\(U=C\cup\{x,y\}\), the two labels \(x,y\) occur at cyclic distance
\(\kappa\).  Equivalently, some rerooting of the current word puts them
in source-placeholder positions \(1,d+1\).

### Theorem 4.1 (exact carrier-edge census)

One has (0.4)--(0.5).  In particular the total edge census is compatible
with every \(G_C(T)\) being a forest; no averaging or Hall count forces
a recharge carrier cycle.

#### Proof

Because \(\kappa<M/2\), every cyclic word of length \(M\) has exactly
\(M\) distinct unordered chords at distance \(\kappa\).  A chord
\(\{x,y\}\subset U\) contributes the edge \(xy\) to the unique core
\(C=U\setminus\{x,y\}\).  Summing first over tops proves

\[
                         \sum_C|E(G_C(T))|=MN.
\]

Also

\[
 \frac{MN}{\binom n{M-2}}
 =M\frac{\binom nM}{\binom n{M-2}}
 =\frac{(n-M+2)(n-M+1)}{M-1}
 =\frac{s(s-1)}{M-1}.
\tag{4.3}
\]

Finally

\[
 M-1-s=(m+H-1)-(m-H+2)=2H-3,
\]

which gives (0.5).  Since a forest on \(s\) vertices may have
\(s-1\) edges, the last assertion follows. \(\square\)

### Theorem 4.2 (cycle-rank obstruction)

Let \(\mathcal B\) be a top-disjoint family of repaired twelve-top
source packets, each obtained from current words solely by rerooting.
Then (0.6) holds.

#### Proof

Every repaired packet on a core \(C\) uses two edge-disjoint six-cycles
in \(G_C(T)\).  Top-disjointness says that distinct selected packets
on the same core use disjoint graph edges, because the edge \(xy\)
identifies the top \(C+\{x,y\}\).

The maximum number of edge-disjoint cycles in a graph is at most its
cycle rank \(\beta(G)\): deleting one edge from every member of an
edge-disjoint cycle family lowers cycle rank by the number deleted.
Thus packets on \(C\) are at most \(\beta(G_C(T))/2\).  Sum over
cores. \(\square\)

The bound is necessary, not sufficient.  It ignores the proper
six-colouring of packet edges, disjoint endpoint palettes, filler-column
identity, and squarefreeness certificates.

## 5. Rerooting costs only the omitted collar

Let \(I\subset\mathbb Z_M\) be the interval of the \(d\) retained
window starts.  Rerooting by \(t\) replaces it by \(I+t\).  Since the
full cyclic \(H\)-window deck is injective and the complement of \(I\)
has size \(\kappa\),

\[
 |I\setminus(I+t)|
 =|(I+t)\setminus I|
 \le\kappa.
\tag{5.1}
\]

### Theorem 5.1 (conditional low-discrepancy source installation)

Suppose \(\mathcal B\) is a top-disjoint family of \(p\) fully
decorated repaired packets whose source word on every incident top is
a cyclic rerooting of the current word there.  Remove the old rows on
the \(12p\) tops and insert the packet source rows.  If \(o,b\) are the
old removed and new inserted owner-occurrence vectors, then

\[
                         \frac12\|b-o\|_1\le12\kappa p.
\tag{5.2}
\]

Consequently, for \(p\le N/12\),

\[
                         \frac12\|b-o\|_1
                         \le\kappa N=O(HN)=o(W).
\tag{5.3}
\]

If the current table has \(o(W)\) middle repeat excess, the installed
source table also has \(o(W)\) repeat excess and hence \(o(W)\) middle
holes.

#### Proof

Equation (5.1) bounds the positive owner difference on one changed row
by \(\kappa\).  Sum over the \(12p\) rows and use the triangle
inequality to obtain (5.2).  The calibrated identity

\[
                         HN=O(HW/m)=o(W)
\]

gives (5.3).  The deterministic relative-installation inequality

\[
 \operatorname{Exc}(\mu_0-o+b)
 \le \operatorname{Exc}(\mu_0)+\frac12\|b-o\|_1
\]

then proves the repeat statement.  Total owner mass remains
\(dN=W-o(W)\), so holes differ from repeat excess by the fixed
\(W-dN=o(W)\). \(\square\)

This theorem permits duplicate source owners across different packets:
they are already charged in \(\|b-o\|_1\).  Exact coefficient one is
stronger and still requires owner-parent closure.  For the
constant-one asymptotic, however, (5.3) proves that an extensive
reroot-realizable source layer has negligible middle discrepancy.

## 6. Exact implication boundary

Proved:

1. an explicit \(\Theta(m)\) per-top distance between atomic owner
   allocation and every literal retained deck;
2. a three-top, integral-demand odd-cycle obstruction with a feasible
   atomic allocation and feasible fractional path packing;
3. the exact carrier-edge and forest-deficit census for cheap rerooted
   repaired sources;
4. the cycle-rank necessary condition for any top-disjoint reroot-only
   source bank; and
5. an \(O(HN)=o(W)\) owner-discrepancy theorem conditional on an
   extensive decorated reroot-realizable packet family.

Not proved:

1. that the carrier graphs of a useful coefficient-one table have
   positive total cycle rank;
2. that their cycles satisfy the endpoint-palette and filler-column
   decoration constraints;
3. a fixed-uniformity matching theorem for the resulting
   state-dependent decorated packet hypergraph; or
4. exact parent-closed installation with zero owner discrepancy.

Thus the atomic \(b\)-matching is not a partially grouped solution: it
can lie linearly far from every grouped row.  The shortest surviving
deterministic lift is state-aware.  It must prove extensive decorated
cycle rank (or create it by a controlled preliminary rethreading) and
then use Theorem 5.1; scalar Hall feasibility cannot substitute for
that statement.
