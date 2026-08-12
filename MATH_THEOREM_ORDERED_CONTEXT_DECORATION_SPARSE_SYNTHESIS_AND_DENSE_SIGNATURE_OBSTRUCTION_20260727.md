# Ordered-context decoration: universal sparse synthesis and a dense signature-cost obstruction

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver, web input,
or probabilistic black box beyond elementary bounded differences is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,\qquad
 \kappa=4H-1,
\tag{0.1}
\]

and assume

\[
 H\to\infty,\qquad H=o(m),\qquad M\ge18H-10.
\tag{0.2}
\]

Let an **uncoloured carrier pair** consist of a common
\((M-2)\)-core \(C\), six outside labels \(S\), and two edge-disjoint
Hamilton six-cycles \(P,Q\) on \(S\).  Its twelve tops are

\[
                         C\cup e,\qquad e\in E(P)\dot\cup E(Q).
\tag{0.3}
\]

This note resolves the ordered-context decoration question at its
correct scope.

1. **Every uncoloured carrier pair can be decorated from scratch.**
   Colour the six \(P\)-edges bijectively by six colours.  Join a
   \(Q\)-edge to a colour when that colour is absent from the four
   \(P\)-edges incident with its endpoints.  This compatibility graph
   is 2-regular bipartite, hence has a perfect matching.  The matching
   colours \(Q\) so that both cycles are rainbow and the four incident
   colours at every outside vertex are distinct.  Fresh disjoint
   \(F/G\)-palettes and the usual König filler decomposition then give
   literal repaired words with

   \[
                         P_j=Q_j\qquad(1\le j\le M),
   \tag{0.4}
   \]

   squarefree shores, and all protected trace identities.

2. For a bank of \(p\) top-disjoint uncoloured carrier pairs, this
   from-scratch synthesis replaces at most

   \[
                         12dp
   \tag{0.5}
   \]

   middle-owner occurrences.  Consequently it costs \(o(W)\) whenever

   \[
                         p=o(N),
   \qquad N=\binom nM,\quad dN=(1-o(1))W.
   \tag{0.6}
   \]

   Thus fresh palettes and König alignment completely solve sparse
   ordered-context decoration.

3. They do **not** generically solve a positive-density layer at
   \(o(W)\) occurrence cost.  There is an absolute constant
   \(\delta>0\) and, for every sufficiently large \(m\), a rooted word
   table \(T\) such that

   \[
      \sum_C\beta(G_C(T))=\Omega(mN),
   \tag{0.7}
   \]

   so uncoloured reroot-realizable carrier cycle rank is extensive, but
   every exact equal-column twelve-word array \(D\) on every structural
   carrier support satisfies

   \[
   \boxed{
      c_{\rm occ}(T,D):=
      \sum_{U\in U(D)}
       \bigl(d-|O(t_U)\cap O(D_U)|\bigr)
      \ge\delta m.}
   \tag{0.8}
   \]

   The assertion is stronger than a palette obstruction: \(D\) may be
   any twelve legal words with equal six-row column signatures.  Hence
   it includes every possible choice of fresh palettes, edge colours,
   filler matchings, and roots.

4. Therefore a top-disjoint bank of \(p=\Theta(N)\) decorated packets
   in this state has total fresh owner-occurrence cost

   \[
                         \Omega(mp)=\Omega(mN)=\Omega(W).
   \tag{0.9}
   \]

   König alignment is an exact completion theorem once the filler
   occurrences may be freely permuted; it is not a low-cost alignment
   theorem relative to an arbitrary current word table.

5. The obstruction in (0.8) is an occurrence-cost obstruction.  It
   does not exclude a global owner circulation in which new occurrences
   on some tops cancel old occurrences on other tops, nor does the
   constructed random-state witness assert coefficient one.  Thus a
   specially correlated coefficient-one table may still have cheap
   extensive decorated fibres.  What is ruled out is the implication

   \[
   \boxed{
   \text{extensive uncoloured carrier rank}
   +\text{fresh palettes/König}
   \Longrightarrow o(W)\text{ local owner rethreading cost}.}
   \tag{0.10}
   \]

The decisive entropy is the ordered filler signature.  Palette data use
only \(O(H)\) protected columns, whereas equality of the two six-row
signatures constrains all \(M\) columns.  A dense positive theorem must
therefore build extensive equal-signature fibres into the state, or
prove a genuinely global owner circulation which pays the linear local
rethreading toll by coefficientwise cancellation.

## 1. Universal edge-colour compatibility

Fix two edge-disjoint Hamilton cycles \(P,Q\) on the same six-set
\(S\).  Give the six edges of \(P\) six different colours.  Define a
bipartite graph

\[
                         \mathcal K(P,Q)
\tag{1.1}
\]

whose left vertices are \(E(Q)\) and whose right vertices are the six
\(P\)-edge colours.  A \(Q\)-edge \(uv\) is adjacent to the colour of a
\(P\)-edge \(e\) precisely when \(e\) is incident with neither \(u\)
nor \(v\).

### Lemma 1.1 (the compatibility graph is 2-regular)

Every vertex of \(\mathcal K(P,Q)\) has degree two.

#### Proof

Because \(P\) and \(Q\) are edge-disjoint, the endpoints \(u,v\) of a
\(Q\)-edge are nonadjacent in \(P\).  Four distinct \(P\)-edges are
incident with \(u\) or \(v\), leaving exactly two \(P\)-edges incident
with neither endpoint.  Thus every left degree is two.

Fix a \(P\)-edge \(ab\).  Its endpoints are nonadjacent in \(Q\).
Deleting the two nonadjacent vertices \(a,b\) from the six-cycle \(Q\)
removes four distinct \(Q\)-edges and leaves exactly two \(Q\)-edges
with neither endpoint in \(\{a,b\}\).  Thus every right degree is two.
\(\square\)

Every finite 2-regular bipartite graph is a disjoint union of even
cycles and has a perfect matching.  Match each \(Q\)-edge to one allowed
colour.

### Corollary 1.2 (universal repaired edge colouring)

For every uncoloured carrier pair, the twelve cycle edges admit a
six-colouring such that

1. each of \(P,Q\) uses every colour exactly once; and
2. the four edges incident with any outside label have four distinct
   colours.

#### Proof

The \(P\)-cycle is rainbow by construction.  A perfect matching of
\(\mathcal K(P,Q)\) gives different colours to the six \(Q\)-edges.
An allowed colour is absent from both \(P\)-edges at each endpoint of
its \(Q\)-edge.  The two incident \(Q\)-edges have different colours,
so all four incident colours are distinct. \(\square\)

This removes any dependence on the displayed model cycles in the
original repaired packet.  Every uncoloured pair has a suitable
palette-colour chart.

## 2. Fresh palettes and König filler synthesis

Choose pairwise disjoint ordered core palettes

\[
 F^{(0)},\ldots,F^{(5)}\subset C,\qquad |F^{(a)}|=2H-1,
\tag{2.1}
\]

and

\[
 G^{(0)},\ldots,G^{(5)}\subset C,\qquad |G^{(a)}|=H-1,
\tag{2.2}
\]

with every \(G\)-palette disjoint from every \(F\)-palette.  They fit
because

\[
                  6(2H-1)+6(H-1)=18H-12\le|C|.
\tag{2.3}
\]

Use the colour from Corollary 1.2 on both the endpoint \(F\)-block and
the preceding \(G\)-block of each edge word.  Each cycle sees every
colour once, and the four contexts at each outside label have distinct
colour pairs.  Hence the protected endpoint columns of the two
six-row tables have the same multisets and the repaired squarefreeness
argument applies.

For a core label \(x\), its number of still-unplaced occurrences in
each six-row table is

\[
 \begin{cases}
 6,&x\text{ lies in no palette},\\
 4,&x\text{ lies in one }F\text{-palette},\\
 5,&x\text{ lies in one }G\text{-palette}.
 \end{cases}
\tag{2.4}
\]

Match its available \(P\)-rows bijectively to its available \(Q\)-rows.
Over all core labels this is a regular bipartite multigraph on the six
\(P\)-rows and six \(Q\)-rows, of degree

\[
                         M-5H+1.
\tag{2.5}
\]

König's line-colouring theorem decomposes it into \(M-5H+1\) perfect
matchings.  Put one matching in each filler column.

### Theorem 2.1 (universal ordered-context synthesis)

Every uncoloured carrier pair has a fully decorated repaired
twelve-top source satisfying (0.4), the proper endpoint-context
conditions, internal squarefreeness, and every protected trace identity.

#### Proof

Corollary 1.2 supplies the colour chart.  Equations (2.1)--(2.3)
supply the disjoint ordered palettes.  The regular multigraph
decomposition supplies every filler entry exactly once in each row and
makes the two six-row column multisets identical.  The histogram and
trace telescope, and the repaired pure/mixed-context squarefreeness
proof, now apply verbatim. \(\square\)

### Corollary 2.2 (sparse \(o(W)\)-cost decoration)

Let \(p\) uncoloured carrier pairs have disjoint top sets.  Relative to
an arbitrary old rooted row on every selected top, replacing the rows
by the freshly synthesized sources introduces at most \(12dp\) fresh
middle-owner occurrences.  If \(p=o(N)\), this is \(o(W)\).

#### Proof

One old and one new row have \(d\) owner occurrences each, so at most
\(d\) new occurrences are introduced on one top.  There are \(12p\)
tops.  Under \(dN=(1-o(1))W\), equation (0.6) gives the conclusion.
\(\square\)

This statement concerns the decoration cost.  Packetwise
squarefreeness does not by itself make distinct packets owner-disjoint;
the owner-aware source-allocation theorem remains necessary for exact
coefficient one.

## 3. Deck neighbourhoods of one word

For a rooted word \(w=(w_1,\ldots,w_M)\) on a top \(U\), define its
retained deleted-window deck

\[
 \mathcal J(w)=
 \bigl\{\{w_i,\ldots,w_{i+H-1}\}:1\le i\le d\bigr\}.
\tag{3.1}
\]

Complementation inside \(U\) identifies \(\mathcal J(w)\) with its
middle-owner deck \(O(w)\).  The retained windows use the active word
segment of length

\[
                         d+H-1=M-3H;
\tag{3.2}
\]

the final \(3H\) word positions are invisible to this retained deck.

For two words on the same top put

\[
 k(w,v)=d-|\mathcal J(w)\cap\mathcal J(v)|
       =d-|O(w)\cap O(v)|.
\tag{3.3}
\]

### Lemma 3.1 (low owner-cost word neighbourhood)

Fix a rooted word \(v\).  For \(0\le k<d\), the number \(B_k(v)\) of
rooted words \(w\) satisfying \(k(w,v)\le k\) obeys

\[
 B_k(v)\le
 (k+1)\,2^d\,(k+1)!\,2^{k+1}4^{k+1}
 M^{2k}(3H)!.
\tag{3.4}
\]

In particular, uniformly for \(k\le m/10\),

\[
 \log B_k(v)
 \le 3k\log m+O(m+H\log H).
\tag{3.5}
\]

#### Proof

Let \(j=k(w,v)\le k\).  Choose the common subfamily
\(\mathcal J(w)\cap\mathcal J(v)\); the crude bound \(2^d\) suffices.
Deleting \(j\) vertices from the intrinsic path \(P_d\) of
\(\mathcal J(v)\) leaves at most \(j+1\) path runs.  In the intrinsic
path of \(\mathcal J(w)\), every common run remains consecutive,
because Johnson adjacency of two retained windows is intrinsic.

Order and orient the runs in at most
\((j+1)!2^{j+1}\) ways.  Distribute the \(j\) new windows before,
between, and after them in at most \(4^{j+1}\) ways.  Starting from a
neighbouring common window and exposing each gap forwards or backwards,
every new window has at most

\[
                         H(M-H)\le M^2
\tag{3.6}
\]

choices in the Johnson graph.  This gives the factor \(M^{2j}\).

An ordered valid length-\(d\) sliding-window path determines its active
injective word segment uniquely: consecutive differences give all
departing and entering letters, and \(d>H\).  The remaining \(3H\)
labels may be ordered arbitrarily, giving \((3H)!\).  Sum over
\(0\le j\le k\) and replace \(j\) by \(k\) in the upper factors to get
(3.4).  Stirling's elementary upper bound gives (3.5). \(\square\)

The important scale is that a radius-\(\delta m\) owner-deck
neighbourhood has entropy only \(3\delta m\log m+o(m\log m)\), while an
unconstrained rooted word has entropy \((1+o(1))m\log m\).

## 4. Equal-signature arrays are far from a generic state

Fix twelve structural tops forming an uncoloured carrier support.
An **equal-signature array** is a collection

\[
 D=(p_0,\ldots,p_5,q_0,\ldots,q_5)
\tag{4.1}
\]

of rooted words on these tops such that

\[
 \{p_i(j):0\le i<6\}_{\rm multi}
 =
 \{q_i(j):0\le i<6\}_{\rm multi}
 \qquad(1\le j\le M).
\tag{4.2}
\]

Every freshly decorated repaired source is such an array.

### Lemma 4.1 (signature-array count)

The number of equal-signature arrays on a fixed structural support is
at most

\[
                         (M!)^6(6!)^M.
\tag{4.3}
\]

#### Proof

Choose the six \(P\)-words arbitrarily, in at most \((M!)^6\) ways.
At each column, its six displayed labels can be assigned to the six
\(Q\)-rows in at most \(6!\) ways.  This gives (4.3).  The count ignores
row-top membership and the requirement that a \(Q\)-row be a
permutation, so it is an upper bound. \(\square\)

Now choose independently a uniformly random rooted word \(t_U\) on
every rank-\(M\) top.  For a candidate array \(D\), define the fresh
owner-occurrence cost by (0.8).

### Theorem 4.2 (uniform dense signature separation)

There is an absolute \(\delta>0\), for example any sufficiently small
fixed \(\delta<1/10\), such that with probability \(1-o(1)\),
simultaneously for every structural carrier support and every
equal-signature array \(D\) on it,

\[
                         c_{\rm occ}(T,D)>\delta m.
\tag{4.4}
\]

#### Proof

Fix a support and an equal-signature array \(D\).  If the total cost is
at most \(K=\delta m\), write its twelve row costs as
\(k_1+\cdots+k_{12}\le K\).  Lemma 3.1 and the polynomial number of
such compositions show that the number of twelve-word current arrays
within this cost is at most

\[
 \exp\!\left(
      3K\log m+O(m+H\log H)
      \right).
\tag{4.5}
\]

There are \((M!)^{12}\) equally likely current arrays.  By Lemma 4.1,
the probability that some equal-signature array lies within cost \(K\)
on this fixed support is at most

\[
 { (M!)^6(6!)^M\over(M!)^{12}}
 \exp\!\left(
      3\delta m\log m+O(m+H\log H)
      \right).
\tag{4.6}
\]

Since \(H=o(m)\), Stirling's formula makes (4.6)

\[
 \exp\!\left(
    -(6-3\delta-o(1))m\log m
      \right).
\tag{4.7}
\]

The complete structural catalogue has at most

\[
 \binom n{M-2}\binom{n-M+2}{6}\,(6!)^2
 =\exp[O(m)]
\tag{4.8}
\]

members, even when both cycle orders are retained.  A union bound over
(4.8) proves (4.4). \(\square\)

Fresh \(F/G\)-palettes and every König filler decomposition are already
included in this union: they merely select a special equal-signature
array \(D\).  Hence they cannot evade (4.4).

## 5. Extensive uncoloured rank coexists with separation

For the same random table, let \(G_C(T)\) be the reroot carrier graph:
an outside pair \(xy\) is an edge when \(x,y\) occur at cyclic distance
\(\kappa\) in the current word on \(C\cup\{x,y\}\).  For a fixed core,

\[
                         G_C(T)\stackrel d=
 G\!\left(n-M+2,{2\over M-1}\right).
\tag{5.1}
\]

The elementary isolated-vertex estimate gives

\[
 \mathbb E\sum_C\beta(G_C(T))
 \ge(e^{-2}+o(1))m\binom n{M-2}
 =\Omega(mN).
\tag{5.2}
\]

### Lemma 5.1 (cycle-rank concentration)

With probability \(1-o(1)\),

\[
                         \sum_C\beta(G_C(T))=\Omega(mN).
\tag{5.3}
\]

#### Proof

Changing the word on one top changes at most \(M\) old carrier chords
and at most \(M\) new carrier chords.  Each chord belongs to one core
graph, and adding or deleting one graph edge changes cycle rank by at
most one.  Thus the sum in (5.3) has bounded difference at most \(2M\)
in each of the \(N\) independent top-word variables.

The expectation in (5.2) is \(c\,mN\) for some fixed \(c>0\) and all
large \(m\).  The bounded-differences inequality gives

\[
 \Pr\!\left[
  \sum_C\beta(G_C(T))<\tfrac12 c\,mN
 \right]
 \le
 \exp\!\left[-\Omega\!\left(
 {m^2N^2\over NM^2}\right)\right]
 =\exp[-\Omega(N)].
\tag{5.4}
\]

This proves (5.3). \(\square\)

Theorem 4.2 and Lemma 5.1 hold simultaneously with probability
\(1-o(1)\).  Selecting one realization proves the state asserted in
(0.7)--(0.8).

### Corollary 5.2 (positive-density occurrence-cost wall)

In that state, any top-disjoint bank of \(p\) freshly decorated repaired
packets has

\[
 \sum_{\text{selected tops }U}
 \bigl(d-|O(t_U)\cap O(D_U)|\bigr)
 \ge\delta mp.
\tag{5.5}
\]

If \(p\ge cN\) for a fixed \(c>0\), the right side is
\(\Omega(mN)=\Omega(W)\).

#### Proof

Apply Theorem 4.2 to each packet.  Top disjointness makes the twelve-row
costs additive over packets.  The calibrated identity
\(dN=(1-o(1))W\) and \(d=(1-o(1))m\) convert the scale. \(\square\)

## 6. What the obstruction does and does not say

For old and new owner-occurrence vectors on a selected bank, one always
has

\[
 {1\over2}\|b-o\|_1
 \le
 \sum_U\bigl(d-|O(t_U)\cap O(D_U)|\bigr).
\tag{6.1}
\]

The inequality can be strict because an owner removed on one top may be
inserted on another.  Therefore (5.5) proves a linear **local
rethreading/occurrence** toll; it does not prove a linear aggregate
load-vector toll against a globally correlated circulation.

Likewise, the random witness table is not conditioned to be coefficient
one.  It proves a statewise separation between uncoloured carrier rank
and cheap decoration, not a counterexample inside the still-unconstructed
class of full coefficient-one physical tables.

The exact deterministic positive targets left open are consequently:

1. construct a coefficient-one table whose carrier cycles have
   extensive fibres of equal or \(o(m)\)-cost column signatures;
2. prove that cross-top owner circulation cancels the local toll in
   (5.5) coefficientwise while preserving every nonmiddle trace; or
3. replace exact column equality by a new bounded packet whose signature
   entropy is only \(\exp[O(m)]\).

## 7. Final boundary

### Proved

1. Every uncoloured pair of edge-disjoint Hamilton six-cycles admits
   the repaired six-colour endpoint chart.
2. Fresh core palettes and König alignment synthesize a complete
   compatible ordered-context decoration on every such pair.
3. The synthesis costs \(o(W)\) owner occurrences for every
   \(o(N)\)-packet bank.
4. There are states with extensive uncoloured reroot cycle rank in which
   every exact decorated packet costs \(\Omega(m)\) fresh owner
   occurrences.
5. Hence a positive-density bank costs \(\Omega(W)\) occurrences in
   those states.

### Not proved

1. A coefficient-one state satisfying the dense signature obstruction.
2. A lower bound on aggregate \(\frac12\|b-o\|_1\) after arbitrary
   cross-top cancellation.
3. A dense equal-signature construction in a specially correlated
   coefficient-one state.
4. Chronological handoff between successive freshly decorated layers.

Thus ordered-context decoration is universally constructible but not
universally cheap.  Sparse carrier banks can be decorated at \(o(W)\)
cost; positive-density cheap decoration is a genuine state property,
not a consequence of uncoloured cycles plus fresh palettes and König
alignment.
