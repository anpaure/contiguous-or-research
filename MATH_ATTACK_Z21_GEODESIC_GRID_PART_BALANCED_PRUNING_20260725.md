# Z21: part-balanced pruning for geodesic grids, and the long-thin obstruction

Date: 2026-07-25

Method: pure mathematics only. No finite search, computation, solver, or web
input is used.

## 0. Exact outcome

This report studies the buffered monotone-geodesic catalogue of
GEODESIC_GRID_STRIP_FLAG_REDUCTION_20260725.md.  Put

\[
        T={\log m\over\log\log m},
        \qquad C=2-\varepsilon ,
        \qquad 0<\varepsilon<1,
\tag{0.1}
\]

and let

\[
        h=\lfloor CT\rfloor .
\tag{0.2}
\]

Here a side-\(h\) product square means \(h\) coordinate increments in
each direction, hence \((h+1)^2\) grid cells.  If “\(s\times s\)” counts
cells instead, replace \(h\) everywhere by \(s-1\).  This harmless
one-unit convention is stated explicitly because it otherwise creates
off-by-one errors in the orbit denominator.

Four conclusions are proved.

1. **Part-balanced square pruning works.**  There is a subcatalogue
   containing no cross-tag pair whose full grids share a side-\(h\)
   square, and, outside \(o(W)\) total weighted tag/target exceptions,
   every fibre retains

   \[
       \exp\left[
          (4-2\varepsilon+o(1))
          {(\log m)^2\over\log\log m}
       \right]
\tag{0.3}
   \]

   candidates.  In every good fibre the retained degree is
   \((1+o(1))\) times the same sampling density times its original
   degree.  Thus the pruning is nearly uniform, not merely a lower-degree
   statement.

2. **Square pruning alone does not make the remaining overlap hierarchy
   summable.**  There are literal cross-tag geodesic chunks whose exact
   full-grid intersection is a long thin rectangle, contains no
   forbidden side-\(h\) square, and has a superpolynomially divergent
   weighted contribution at weight \(B_0\log m\).  The obstruction occurs
   for every fixed \(0<\varepsilon<1\).

3. **A sparse non-tautological repair exists.**  In addition to side-\(h\)
   squares, forbid a pair when the meet-to-join span \(A\) of its
   full-grid intersection exceeds

   \[
       A_0=\left(2C+\gamma\right)T,
       \qquad
       \gamma={C\varepsilon\over2(C-1)}.
\tag{0.4}
   \]

   The long-span conflict has exponentially smaller relative degree than
   the square conflict.  Among pairs surviving both conflicts, the
   complete width-at-least-two exponential overlap link is

   \[
       \kappa_{\rm cross}=m^{-1+o(1)}
\tag{0.5}
   \]

   uniformly for every fixed multiple of \(\log m\).  Width one is the
   previously proved nested hierarchy.

4. **The normalization can be transferred through the random pruning.**
   A second deterministic link trimming removes only \(o(W)\) additional
   weighted fibres and leaves normalized link

   \[
       Q(\log m)^2\kappa_{\rm cross}
       =m^{-1/2+o(1)}=o(1).
\tag{0.6}
   \]

   This uses the calibrated scale \(Q=m^{1/2+o(1)}\).  It is essential:
   lower fibre balance alone does not control pair-link numerators.

All retained objects are unchanged integral geodesic chunks, so this
static pruning preserves literal contiguous-OR realizability and adds no
physical fragmentation.  The ordinary initialization and omitted-tail
costs remain

\[
       O(QW/\ell)+O(\ell W/m)=o(W).
\tag{0.7}
\]

The report does **not** prove hereditary degree/link control after
adaptive matching bites and therefore does not prove the coefficient-one
theorem.  Its exact proved boundary is the initial static catalogue.

## 1. Catalogue and scale hypotheses

Write

\[
        W=\binom{2m}{m},\qquad M=m+H.
\tag{1.1}
\]

The buffered geodesic has

\[
        g=\ell+2Q-1
\tag{1.2}
\]

transition slots and an ordered partition

\[
 U=C_0\ \dot\cup\
   \{a_1,\ldots,a_g\}\ \dot\cup\
   \{b_1,\ldots,b_g\}\ \dot\cup R.
\tag{1.3}
\]

Its full grid is

\[
 G_{i,j}
 =C_0\cup\{a_{i+1},\ldots,a_g\}
       \cup\{b_1,\ldots,b_j\},
 \qquad 0\le i,j\le g.
\tag{1.4}
\]

The physical strip consists of the \(\ell\) central phases

\[
        Q\le t\le Q+\ell-1,
\tag{1.5}
\]

and the exact lower and upper flags are

\[
        L_q(t)=G_{t+q,t},
        \qquad
        U_q(t)=G_{t-q,t}.
\tag{1.6}
\]

The only scale facts used below are

\[
\begin{split}
 &Q\ll\ell,\qquad g=m^{1/2+o(1)},\qquad Q=m^{1/2+o(1)},\\
 &g=o(m),\qquad h,A_0=o(Q),\qquad
 {Qg\over m}=m^{o(1)},\qquad
 \exp(g^2/m)=m^{o(1)}.
\end{split}
\tag{1.7}
\]

They hold at the calibrated Gaussian-window choices.  In particular,
every rectangle used below fits strictly inside the protected strip and
its marker collar fits inside the \(Q\)-buffer.

Let \(\mathcal C_m\) be the coordinate-symmetrized catalogue, \(D\) its
tag degree, and \(d\) the minimum degree of a calibrated tag or
protected-target fibre.  Exact symmetry gives

\[
             d=(1-o(1))D.
\tag{1.8}
\]

Weights are assigned as in the literal repair ledger: a tag fibre has
weight equal to the number of physical owner occurrences lost with that
tag, and a protected-target fibre has scalar weight one.  The total
weighted fibre mass is

\[
             O(QW).
\tag{1.9}
\]

Nothing below uses a union bound over the exponentially many fibres.

## 2. Deterministic grid facts

### Lemma 2.1 (Boolean product structure)

For cells of one full grid,

\[
 G_{i,j}\cap G_{i',j'}
     =G_{\max(i,i'),\,\min(j,j')},
\tag{2.1}
\]

\[
 G_{i,j}\cup G_{i',j'}
     =G_{\min(i,i'),\,\max(j,j')}.
\tag{2.2}
\]

Consequently the intersection of two full grids, ordered by Boolean
inclusion, is a sublattice of each product grid.

#### Proof

The \(a\)-coordinates occur as suffixes and the \(b\)-coordinates as
prefixes.  Intersection takes the shorter suffix and shorter prefix,
giving (2.1); union takes the longer ones, giving (2.2).  A common family
is closed under the same Boolean intersection and union in both grids.
\(\square\)

### Lemma 2.2 (antichain generates a square)

If a common sublattice contains the antichain

\[
        G_{i_0,j_0},\ldots,G_{i_h,j_h},
        \qquad
        i_0<\cdots<i_h,\quad
        j_0<\cdots<j_h,
\tag{2.3}
\]

then it contains every compressed cell

\[
        G_{i_p,j_q},\qquad 0\le p,q\le h.
\tag{2.4}
\]

Thus a common sublattice containing no side-\(h\) square has width at
most \(h\).

#### Proof

For \(p\le q\), intersecting and joining suitable members of (2.3) gives
the mixed coordinate cell \(G_{i_p,j_q}\); the same conclusion for
\(p>q\) follows with the roles reversed.  Equivalently, a sublattice
contains the product of the two coordinate projections of any antichain.
If its width were at least \(h+1\), an antichain of that size would give
(2.4). \(\square\)

### Lemma 2.3 (rank taper)

Let \(\mathcal L\) be a nonempty common sublattice.  Let

\[
        I=\bigcap\mathcal L,\qquad
        J=\bigcup\mathcal L,\qquad
        A=|J\setminus I|,
\tag{2.5}
\]

and let \(w\) be its width.  Then

\[
             |\mathcal L|\le w(A-w+2).
\tag{2.6}
\]

#### Proof

Rank the interval \([I,J]\) by \(|X\setminus I|\).  Every rank level is
an antichain, hence has at most \(w\) members.  In a product of two
chains, the first \(w-1\) rank levels have capacities at most

\[
             1,2,\ldots,w-1,
\]

and the last \(w-1\) levels have the reverse capacities.  All middle
levels have capacity at most \(w\).  Summing these capacities gives

\[
 2{w(w-1)\over2}+w(A-2w+3)
      =w(A-w+2).
\]

The existence of width \(w\) already implies \(A\ge2(w-1)\), so the
displayed middle interval is nonnegative. \(\square\)

### Lemma 2.4 (nested-pair codegree)

Fix a nested Boolean pair \(I\subset J\) in the calibrated rank range and
put \(A=|J\setminus I|\).  The relative number of catalogue grids
containing both is at most

\[
       m^{o(1)}\,{A+1\over\binom{m-g}{A}}.
\tag{2.7}
\]

For a fixed grid, the number of its ordered nested cell pairs of gap
\(A\) is at most

\[
       (g+1)^2(A+1).
\tag{2.8}
\]

#### Proof

Anchor the occurrence of \(I\).  The prescribed difference
\(J\setminus I\) must occupy the transition coordinates between the two
cells.  There are at most \(A+1\) ways to split its \(A\) coordinates
between the two grid directions.  Conditional coordinate symmetry makes
the prescribed block one of at least
\(\binom{m-g}{A}\) possible blocks.  The normalized load of the anchor
rank is at most

\[
       \exp(g^2/m+o(1))=m^{o(1)}.
\]

This proves (2.7).  For (2.8), choose the first cell in at most
\((g+1)^2\) ways and split the total coordinate gap in at most \(A+1\)
ways. \(\square\)

## 3. Weighted part-balanced independent pruning

The probabilistic statement needed here is elementary and is recorded
with its constants.

### Theorem 3.1 (near-uniform weighted fibre pruning)

Let \(B\) be a graph of maximum degree \(\Delta\) on a finite catalogue
\(\mathcal C\).  Let \(\mathscr F\) be any family of fibres, with
nonnegative weights \(w_F\), and suppose \(|F|\ge d\) for every
\(F\in\mathscr F\).  Fix \(L\ge2\) and \(0<\zeta\le1\), and put

\[
             p={1\over L(\Delta+1)}.
\tag{3.1}
\]

There is an independent set \(\mathcal I\) in \(B\) such that, outside
fibres of weighted proportion at most

\[
       2\exp\left(-{\zeta^2pd\over12}\right)
          +{2\over\zeta L},
\tag{3.2}
\]

one has

\[
       (1-\zeta)p|F|
       \le|\mathcal I\cap F|
       \le(1+\zeta)p|F|.
\tag{3.3}
\]

#### Proof

Mark vertices independently with probability \(p\), and retain a marked
vertex exactly when none of its neighbours is marked.  The retained set
is independent.

For a fixed fibre \(F\), let \(Y_F\) be its marked count and \(Z_F\) the
number of its marked vertices deleted because they have a marked
neighbour.  With \(\mu_F=p|F|\), Chernoff gives

\[
 \Pr\left(|Y_F-\mu_F|>{\zeta\mu_F\over2}\right)
       \le2\exp\left(-{\zeta^2\mu_F\over12}\right).
\tag{3.4}
\]

For each \(v\in F\),

\[
 \Pr(v\hbox{ is marked and has a marked neighbour})
       \le p^2\Delta,
\]

so

\[
       \mathbb E Z_F\le |F|p^2\Delta
          \le{\mu_F\over L}.
\tag{3.5}
\]

Markov therefore gives

\[
       \Pr\left(Z_F>{\zeta\mu_F\over2}\right)
          \le{2\over\zeta L}.
\tag{3.6}
\]

Outside the two events, \(Y_F-Z_F\) lies in the interval (3.3).
Multiplying each exceptional indicator by \(w_F\), taking expectations,
and fixing one outcome proves the weighted assertion. \(\square\)

This theorem gives simultaneous balance at almost every tag and every
target in the coefficient ledger.  It neither assumes nor proves
independence between fibres.

## 4. The side-\(h\) square graph

Join two cross-tag catalogue vertices when their full grids share a
side-\(h\) compressed square.  Let \(\Delta_\square\) be the maximum
degree of this graph.

### Proposition 4.1 (square relative degree)

Uniformly in the catalogue,

\[
 {\Delta_\square\over D}
 \le
 m^{1+o(1)}
 \sum_{A\ge2h}
       {(A+1)^2\over\binom{m-g}{A}}
 =
 \exp\left[
      -(2h+o(h))\log m
 \right].
\tag{4.1}
\]

Equivalently,

\[
 {\Delta_\square\over D}
 \le
 \exp\left[
      -(4-2\varepsilon+o(1))
      {(\log m)^2\over\log\log m}
 \right].
\tag{4.2}
\]

#### Proof

A side-\(h\) square has coordinate spans at least \(h\) in each
direction.  Its minimum and maximum form a nested pair of total gap
\(A\ge2h\).  Sum Lemma 2.4 over all such pairs in the fixed grid.  This
gives the first inequality in (4.1), with the factor
\((g+1)^2=m^{1+o(1)}\) absorbed.

For \(A\le2g=o(m)\), the summand decreases geometrically once
\(A\ge2h\), up to polynomial factors.  Also

\[
 \log\binom{m-g}{2h}
      =2h\log m-o(h\log m).
\]

The first term therefore determines the logarithmic asymptotic in
(4.1), and (0.1)--(0.2) give (4.2). \(\square\)

The exact orbit identity behind the exponent is

\[
 \#\{\hbox{oriented ambient side-\(h\) squares}\}
      =W(m)_h^2.
\tag{4.3}
\]

Indeed a square records a bottom set of size \(m-h\) and two ordered
strings of \(h\) singleton increments:

\[
 \binom{2m}{m-h}(m+h)_h(m)_h
      ={(2m)!\over(m-h)!^2}
      =W(m)_h^2.
\]

Thus (4.1) has the correct leading denominator, not merely a crude
entropy exponent.

### Corollary 4.2 (coefficient-safe balanced square pruning)

Take

\[
        L=Q(\log m)^2,\qquad
        \zeta={1\over\log m}.
\tag{4.4}
\]

There is a square-bad-pair-free subcatalogue such that the total weighted
mass of exceptional tag and protected-target fibres is \(o(W)\), and in
every other fibre

\[
 |\mathcal I\cap F|=(1+O(1/\log m))p|F|.
\tag{4.5}
\]

Moreover,

\[
 \log(p|F|)
 \ge
 (4-2\varepsilon+o(1))
 {(\log m)^2\over\log\log m}.
\tag{4.6}
\]

#### Proof

By (1.8) and Proposition 4.1,

\[
 pd\ge
 {1-o(1)\over
  L\left(\Delta_\square/D+D^{-1}\right)}
 =
 \exp\left[
 (4-2\varepsilon+o(1))
 {(\log m)^2\over\log\log m}
 \right].
\tag{4.7}
\]

The exponential term in (3.2) is \(o(1/Q)\), while

\[
       {2\over\zeta L}
          ={2\over Q\log m}=o(1/Q).
\tag{4.8}
\]

Multiplication by the total fibre weight \(O(QW)\) gives \(o(W)\).
Equations (4.5)--(4.6) follow from Theorem 3.1. \(\square\)

## 5. Decisive obstruction: long thin exact intersections

The preceding corollary is not enough.  The failure is geometric, not a
defect of the random pruning theorem.

For integers \(a,b\ge1\), define the consecutive rectangle

\[
 \mathcal R_{a,b}(t)
   =\{G_{t+p,t+q}:0\le p\le a,\ 0\le q\le b\}.
\tag{5.1}
\]

It has \(k=(a+1)(b+1)\) cells.

### Lemma 5.1 (exact rectangular orbit count)

The number of oriented ambient copies of \(\mathcal R_{a,b}\) is

\[
 \mathscr R_{a,b}
   =\binom{2m}{m-a}(m+a)_{a+b}
   =W(m)_a(m)_b.
\tag{5.2}
\]

#### Proof

Choose the minimum cell of size \(m-a\), then the ordered \(a+b\)
coordinates which form the two increment strings.  Algebraically,

\[
 \binom{2m}{m-a}(m+a)_{a+b}
   ={(2m)!\over(m-a)!(m-b)!}
   =W(m)_a(m)_b.
\]

\(\square\)

### Lemma 5.2 (literal exact-intersection companions)

Suppose

\[
       a+b=o(Q),\qquad a+b=o(g).
\tag{5.3}
\]

For every fixed chunk \(P\) and every interior occurrence of
\(\mathcal R_{a,b}(t)\), there are cross-tag catalogue chunks \(P'\)
whose full-grid intersection with \(P\) is exactly that rectangle.  Their
relative mass is at least

\[
 { \exp[-O(Qg/m)]\over
        \ell\,(m)_a(m)_b}.
\tag{5.4}
\]

#### Proof

Write

\[
 K=G_{t+a,t}.
\tag{5.5}
\]

The rectangle is determined by \(K\), the consecutive departure string

\[
       a_{t+1},\ldots,a_{t+a},
\]

and the consecutive arrival string

\[
       b_{t+1},\ldots,b_{t+b}.
\]

Build \(P'\) with the same anchor \(K\) and the same two strings at an
interior phase \(t'\).  Four marker slots make the intersection exact.

* Put a coordinate outside the carrier of \(P\) in the departure slot
  immediately before the copied departure block.  Every earlier row of
  \(P'\) contains this alien coordinate and hence is not a cell of \(P\).
* Put a coordinate of the fixed core \(C_0\) in the departure slot
  immediately after the block.  Every later row of \(P'\) omits this
  coordinate, whereas every cell of \(P\) contains it.
* Put a second core coordinate in the arrival slot immediately before the
  copied arrival block.  Every earlier column of \(P'\) omits it.
* Put a second coordinate outside the carrier of \(P\) in the arrival
  slot immediately after the block.  Every later column of \(P'\)
  contains it.

The marker coordinates can be chosen distinct because
\(|C_0|=m-g\) and \(|[2m]\setminus U|=m-H\) both tend to infinity.
They force

\[
 t'\le i'\le t'+a,\qquad
 t'\le j'\le t'+b
\]

for any cell \(G'_{i',j'}\) which could equal a cell of \(P\).  Inside
these bounds, the common anchor and copied strings give exactly the cells
in (5.1).  Hence the full-grid intersection is precisely
\(\mathcal R_{a,b}(t)\).  The two alien markers also force the carrier,
and therefore the tag, to differ from that of \(P\).

It remains to count rather than merely construct.  Lemma 5.1 and
coordinate double counting give the basic factor
\(((m)_a(m)_b)^{-1}\).  Restricting to one of the \(\ell\) physical
alignments costs at most \(\ell^{-1}\).  Sequentially reserving the four
markers and a \(Q\)-slot collar costs at most the reciprocal of

\[
 { (m-g)_Q\over(m-O(a+b))_Q}
       =\exp[-O(Qg/m)].
\tag{5.6}
\]

All other slots remain free.  This proves (5.4). \(\square\)

### Theorem 5.3 (square-only hierarchy is nonsummable)

Fix

\[
        0<\delta<1-\varepsilon,
\tag{5.7}
\]

and put

\[
        a=\lfloor(1+\delta)T\rfloor,
        \qquad
        b=\lfloor T^2\rfloor.
\tag{5.8}
\]

For large \(m\), the exact intersection in Lemma 5.2 contains no
side-\(h\) square.  Nevertheless, for every fixed \(B_0>0\), at
\(y=B_0\log m\) its single contribution to the usual exponential
overlap hierarchy has logarithm at least

\[
 \delta T^2\log m-o(T^2\log m),
\tag{5.9}
\]

and therefore tends to \(+\infty\).

#### Proof

Because \(1+\delta<C=2-\varepsilon\), one has \(a<h\).  The rectangle
has width \(a+1\), so its exact full-grid intersection contains no
side-\(h\) square.

Let \(k=(a+1)(b+1)\).  Lemma 5.2 gives a hierarchy term at least

\[
 { \exp[-O(Qg/m)]\over
   \ell(m)_a(m)_b}\,y^{k-2}.
\tag{5.10}
\]

Since \(a+b=o(Q)\), (5.3) holds.  Taking logarithms and using
\(\log(m)_r=r\log m+O(r^2/m+r\log r)\) gives

\[
\begin{split}
 \log(5.10)
 &\ge k\log\log m-(a+b)\log m\\
 &\qquad{}-O(Qg/m+\log\ell+a\log a+b\log b).
\end{split}
\tag{5.11}
\]

Now

\[
 ab\log\log m
       =(1+\delta+o(1))T^2\log m,
\]

whereas

\[
 b\log m=(1+o(1))T^2\log m,
 \qquad
 a\log m=o(T^2\log m).
\]

Every error in (5.11) is \(o(T^2\log m)\) under (1.7).  This proves
(5.9). \(\square\)

Thus the true anisotropic threshold is governed, to first order, by

\[
        {ab\over a+b}
           \approx{\log m\over\log\log m},
\tag{5.12}
\]

not by the square side alone.  Aspect ratio one gives the familiar
threshold \(2T\); arbitrarily long rectangles lower the critical short
side to \(T\).

## 6. A sparse long-span repair

For a cross-tag pair with nonempty common full-grid sublattice
\(\mathcal L\), define its span

\[
        A(\mathcal L)
          =\left|\bigcup\mathcal L
                    \setminus\bigcap\mathcal L\right|.
\tag{6.1}
\]

Add a conflict whenever \(A(\mathcal L)>A_0\), with \(A_0\) from (0.4).
Let \(\Delta_{\rm span}\) be the maximum degree of this conflict graph.

### Proposition 6.1 (the added conflict is cheaper)

\[
 {\Delta_{\rm span}\over D}
 \le
 {m^{1+o(1)}\over\binom{m-g}{\lceil A_0\rceil}}
 =
 \exp\left[
   -(2C+\gamma+o(1))
   {(\log m)^2\over\log\log m}
 \right].
\tag{6.2}
\]

In particular,

\[
 {\Delta_{\rm span}\over\Delta_\square}
 \le
 \exp\left[
   -(\gamma+o(1))
   {(\log m)^2\over\log\log m}
 \right]
\tag{6.3}
\]

whenever the square degree has its natural orbit scale.  Even without a
matching lower bound for \(\Delta_\square\), the sum of the two degree
upper bounds is governed by the square exponent \(2C\).

#### Proof

For each competitor in the long-span graph, the meet and join of its
intersection form a nested pair in the fixed grid with gap \(A>A_0\).
Apply Lemma 2.4 and sum over \(A>A_0\).  Since \(A_0=O(T)\) and
\(2g=o(m)\), the first term dominates up to \(m^{1+o(1)}\).  Finally,

\[
 \log\binom{m-g}{A_0}
       =(A_0+o(T))\log m,
\]

which gives (6.2). \(\square\)

Apply Theorem 3.1 to the union of the square and long-span conflict
graphs.  Equations (4.4)--(4.6) remain unchanged, including the retained
degree exponent and the \(o(W)\) weighted exceptional ledger.

## 7. Summation of every remaining non-square crossing shape

For \(y\ge1\), define the normalized width-at-least-two link of a fixed
chunk \(P\) by

\[
 \kappa_y(P)
 ={1\over D}
 \sum_{\substack{P':\ {\rm tag}(P')\ne{\rm tag}(P)\\
                  2\le w(\mathcal L)\le h\\
                  A(\mathcal L)\le A_0}}
 y^{|\mathcal L|-2},
 \qquad
 \mathcal L=\mathcal G(P)\cap\mathcal G(P').
\tag{7.1}
\]

The use of the full-grid intersection only enlarges the protected-strip
link.

### Theorem 7.1 (raw crossing hierarchy)

For every fixed \(B_0>0\), uniformly for

\[
             1\le y\le B_0\log m,
\tag{7.2}
\]

one has

\[
             \sup_P\kappa_y(P)=m^{-1+o(1)}.
\tag{7.3}
\]

#### Proof

Group competitors by the meet and join of their common sublattice.
Lemmas 2.3 and 2.4 give

\[
 \kappa_y(P)
 \le
 m^{o(1)}g^2
 \sum_{A=2}^{\lfloor A_0\rfloor}
 { (A+1)^2\over\binom{m-g}{A}}
 \max_{2\le w\le\min(h,\lfloor A/2\rfloor+1)}
 y^{\,w(A-w+2)-2}.
\tag{7.4}
\]

There is no missing shape factor in (7.4): fixing the meet and join and
counting every competitor containing them overcounts all possible
intersection shapes at once.

For the growing-width range, write

\[
       w=cT+o(T),\qquad A=dT+o(T).
\]

After division by

\[
       {(\log m)^2\over\log\log m},
\]

the logarithm of a summand, apart from the lower-order \(g^2\) factor, is

\[
       f(c,d)=(c-1)d-c^2.
\tag{7.5}
\]

If \(0<c\le1\), the constraint \(d\ge2c\) and the fact that
\(c-1\le0\) give

\[
       f(c,d)\le(c-1)2c-c^2
               =c^2-2c<0.
\tag{7.6}
\]

If \(1\le c\le C\), then \(f\) increases with \(d\), so \(d\le
2C+\gamma\) gives

\[
 f(c,d)\le f(c,2C+\gamma).
\]

The last expression is increasing on \([1,C]\), because its derivative
is \(2C+\gamma-2c>0\).  Hence

\[
\begin{split}
 f(c,d)
 &\le f(C,2C+\gamma)\\
 &=(C-1)(2C+\gamma)-C^2\\
 &=-{C\varepsilon\over2}<0.
\end{split}
\tag{7.7}
\]

If \(w=o(T)\), then \(w\log y=o(\log m)\), so each extra unit of span
costs \(m^{1-o(1)}\); this directly covers the regime omitted by the
positive limiting-\(c\) calculation.

It remains to identify the largest fixed case, because
\(g^2=m^{1+o(1)}\).  The minimum possible width-at-least-two interval has
\(A=2,w=2\), and its contribution is

\[
       m^{o(1)}{g^2y^2\over\binom{m-g}{2}}
          =m^{-1+o(1)}.
\tag{7.8}
\]

Every other fixed pair \((A,w)\) is smaller by a power of \(m\), and
there are only \(O(T^2)\) pairs.  Equations (7.6)--(7.8) prove the upper
bound in (7.3).  The equality notation \(m^{-1+o(1)}\) records the
correct leading upper scale supplied by the \(2\times2\) diamond; only
the upper bound is used later. \(\square\)

Width-one intersections are chains.  They are exactly the nested
hierarchy already bounded in
MATH_ATTACK_GEODESIC_ORBIT_TRP_OVERLAP_PRUNING_20260725.md and are not a
new square-grid contribution.

## 8. Transfer of the link bound through the pruning

Part balance by itself gives no upper bound on a pair-link numerator.
The following deterministic cleanup supplies the missing transfer.

### Lemma 8.1 (sample-square link trimming)

Let \(\mathcal C\) have \(n\) vertices, and let
\(\omega(u,v)=\omega(v,u)\ge0\) be a link kernel with

\[
          \sum_v\omega(u,v)\le D\kappa
          \qquad(u\in\mathcal C).
\tag{8.1}
\]

Run the isolated Bernoulli experiment of Theorem 3.1 with density \(p\),
obtaining \(\mathcal I_0\).  There is an outcome which satisfies the
weighted fibre conclusion of Theorem 3.1 up to a factor four in its
exception bound and also satisfies

\[
 \sum_{u,v\in\mathcal I_0}\omega(u,v)
       \le4p^2nD\kappa.
\tag{8.2}
\]

For any \(\Theta\ge1\), delete from \(\mathcal I_0\) every \(u\) for
which

\[
       \sum_{v\in\mathcal I_0}\omega(u,v)
             >\Theta pD\kappa.
\tag{8.3}
\]

At most

\[
             {4pn\over\Theta}
\tag{8.4}
\]

vertices are deleted, and every remaining vertex has normalized retained
link at most

\[
             \Theta\kappa
\tag{8.5}
\]

relative to a retained fibre degree \(pD\).

#### Proof

Membership in \(\mathcal I_0\) implies that a vertex was marked.  Hence

\[
 \mathbb E\sum_{u,v\in\mathcal I_0}\omega(u,v)
 \le
 p^2\sum_{u,v}\omega(u,v)
 \le p^2nD\kappa.
\tag{8.6}
\]

Markov gives (8.2) with failure probability at most \(1/4\).  The
weighted exceptional-fibre random variable from Theorem 3.1 exceeds four
times its expectation with probability at most \(1/4\).  Thus an outcome
satisfying both exists.  Summing (8.3) over deleted vertices and using
(8.2) gives (8.4).  Dividing (8.3) by \(pD\) gives (8.5). \(\square\)

### Lemma 8.2 (fibre incidence transfer)

Assume that, within each calibrated fibre stratum, every catalogue vertex
has the same number \(r\) of fibre incidences and every fibre has degree
\((1+o(1))D_r\).  If at most \(\rho pn\) sampled vertices are deleted,
then the proportion of fibres in that stratum losing more than
\(\zeta pD_r\) vertices is at most

\[
             (1+o(1)){\rho\over\zeta}.
\tag{8.7}
\]

The same statement holds for the standard weighted tag stratum.

#### Proof

The total lost fibre incidences are at most \(r\rho pn\).  A bad fibre
accounts for more than \(\zeta pD_r\) of them.  The number of fibres in
the stratum is \((1+o(1))nr/D_r\), by double counting all incidences.
Dividing proves (8.7).  Tag fibres partition the catalogue, and their
standard physical weights are constant within the stratum, so the same
calculation applies. \(\square\)

### Corollary 8.3 (static normalized hierarchy after pruning)

Let \(\omega\) be the sum of the width-at-least-two kernel in (7.1) and
the previously controlled width-one nested kernel.  Choose

\[
        \Theta=Q(\log m)^2,
        \qquad
        \zeta={1\over\log m}.
\tag{8.8}
\]

After the square-plus-span isolated pruning and the trimming of Lemma
8.1, the following hold.

* No retained pair has a side-\(h\) square or span exceeding \(A_0\).
* Outside \(o(W)\) total weighted tag/target fibres, retained degree is
  \((1+o(1))p\) times original degree.
* Every retained candidate outside the removed high-link set has
  normalized nontrivial exponential link

  \[
       O(\Theta m^{-1+o(1)})
          =m^{-1/2+o(1)}=o(1).
\tag{8.9}
  \]

#### Proof

Theorem 7.1 and the nested census give \(\kappa=m^{-1+o(1)}\).
Lemma 8.1 deletes at most \(4pn/\Theta\) vertices.  Lemma 8.2 shows that
the fraction of fibres lost to this cleanup in each stratum is at most

\[
       {4+o(1)\over\zeta\Theta}
          =O\left({1\over Q\log m}\right).
\tag{8.10}
\]

Across \(O(Q)\) protected target strata and the tag stratum, the weighted
exceptional ledger is \(O(W/\log m)=o(W)\).  The original isolation
exceptions are already \(o(W)\) by (4.8).  Finally,

\[
 \Theta\kappa
   =Q(\log m)^2m^{-1+o(1)}
   =m^{-1/2+o(1)}.
\]

Deleting vertices cannot recreate a forbidden pair. \(\square\)

## 9. Audit and exact boundary

The decisive claims were checked in two independent ways: by the
min/max nested-pair census of Lemma 2.4 and by the exact rectangle orbit
identity (5.2).  They agree on the two-dimensional entropy cost
\((m)_a(m)_b\).  The constants in the span cutoff were audited directly:

\[
\begin{split}
 &(C-1)(2C+\gamma)-C^2\\
 &\qquad=C(C-2)+(C-1)\gamma\\
 &\qquad=-C\varepsilon
       +{C\varepsilon\over2}
       =-{C\varepsilon\over2}.
\end{split}
\tag{9.1}
\]

The verdicts are:

* **Valid:** the exact grid/flag identities and square orbit count.
* **Valid:** isolated-vertex retention gives coefficient-safe, nearly
  uniform tag/target degrees when \(L=Q(\log m)^2\).
* **False:** forbidding only side-\(h\) squares makes the complete
  non-square overlap hierarchy summable.
* **Valid repair:** add the explicit span conflict \(A>A_0\); it is
  exponentially sparser than the square conflict and leaves a raw
  \(m^{-1+o(1)}\) crossing hierarchy.
* **Necessary correction:** fibre lower balance alone cannot normalize
  pair links; Lemmas 8.1--8.2 supply an aggregate-square sampling and
  trimming step.
* **Unsupported here:** hereditary preservation under adaptive target
  deletion, a common matching, or the final coefficient-one conclusion.

No full-Graver or tautological “join every harmful pair” closure is used.
The added graph is described by the single explicit statistic
\(|\bigcup\mathcal L\setminus\bigcap\mathcal L|\), has the quantified
degree (6.2), and is therefore a genuine sparse geometric move set.

