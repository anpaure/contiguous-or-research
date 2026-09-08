# A twelve-top histogram-neutral bidirectional recharge connects all rooted positions

Date: 2026-07-27

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\]

and assume \(H\ge3\) and

\[
                         M\ge18H-10.
\tag{0.1}
\]

There is an explicit bounded packet on twelve **distinct** rank-\(M\)
tops with these properties.

1. Six words rotate one rooted position to the left and six words
   rotate one rooted position to the right.
2. The global rooted position--label histogram is unchanged.
3. The aggregate physical target derivative is zero at every protected
   complementary length \(0\le h\le2H\), including the middle.
4. Both shores are squarefree and have the same middle-owner support.
5. Consequently the packet is a coefficient-one, full-trace-neutral
   move inside one fixed position--label histogram fibre.

In particular it transports labels between positions \(j\) and
\(j+1\).  Together with the existing boundary rectangle and three-top
tail reroots, this closes the admitted-position graph \(\Gamma\) from
the position-label fibre note.

The construction is a paired circulation, not two independent copies:
the two six-row source tables have shifted phases and identical
column multisets.  Their histogram derivatives therefore cancel
coefficientwise.

This is still a local packet theorem.  It does not pack a positive
density of the twelve-top packets into one global owner resolution.

## 1. Even-cycle recharge

We first record the extension of the four-top telescope which is
implicit in its proof.

### Lemma 1.1 (even-cycle full-trace recharge)

Let

\[
 Z=(z_0,z_1,\ldots,z_{\ell-1})
\]

be a cyclic order of distinct labels, where \(\ell\ge4\) is even.
Let \(C\) be an \((M-2)\)-set disjoint from the \(z_i\), and put

\[
                         U_i=C\cup\{z_{i-1},z_i\}
\tag{1.1}
\]

with indices modulo \(\ell\).  Choose ordered
\((2H-1)\)-sets \(F_i\subset C\) such that

\[
                         F_{i-1}\cap F_i=\varnothing .
\tag{1.2}
\]

There are literal words \(p_i\) on \(U_i\) whose two protected endpoint
blocks are

\[
 (z_{i-1},F_i),\qquad (z_i,F_{i-1}),
\tag{1.3}
\]

and for which simultaneous left rotation \(p_i\mapsto rp_i\) has

\[
 \sum_{i=0}^{\ell-1}
 \bigl({\cal D}_h(U_i,rp_i)-{\cal D}_h(U_i,p_i)\bigr)=0
 \qquad(0\le h\le2H).
\tag{1.4}
\]

#### Proof

Condition (1.2) makes the two blocks in one word disjoint.  Fill the
remaining positions by the remaining labels of \(C\).  For
\(1\le h\le2H\), the one-word rotation derivative is

\[
 e_{(C\setminus (F_{i-1})^{h-1})\cup\{z_{i-1}\}}
 -
 e_{(C\setminus F_i^{h-1})\cup\{z_i\}} .
\tag{1.5}
\]

The positive term at \(i\) is the negative term at \(i-1\).
They telescope cyclically.  At \(h=0\) the derivative is zero top by
top.  This is exactly the proof of the four-top theorem, and does not
use \(\ell=4\). \(\square\)

The inverse exchange \(rp_i\mapsto p_i\) is equally literal and has the
negative derivative.

## 2. Two edge-disjoint six-cycles

Choose six labels \(v_0,\ldots,v_5\) outside \(C\).  On these labels use
the two Hamilton cycles

\[
\begin{aligned}
 P&=(0,1,2,3,4,5),\\
 Q&=(0,2,4,1,5,3).
\end{aligned}
\tag{2.1}
\]

Their edge sets are

\[
\begin{aligned}
 E(P)&=\{01,12,23,34,45,50\},\\
 E(Q)&=\{02,24,41,15,53,30\},
\end{aligned}
\]

and are disjoint.  Therefore the twelve tops

\[
 C\cup\{v_i,v_j\},
 \qquad ij\in E(P)\sqcup E(Q),
\tag{2.2}
\]

are distinct.

Choose six pairwise disjoint ordered palettes

\[
 F^{(0)},F^{(1)},\ldots,F^{(5)}\subset C,
 \qquad |F^{(a)}|=2H-1.
\tag{2.3}
\]

They fit by (0.1).

Choose in addition six pairwise disjoint ordered palettes

\[
 G^{(0)},G^{(1)},\ldots,G^{(5)}\subset C,
 \qquad |G^{(a)}|=H-1,
\tag{2.4}
\]

disjoint from all the \(F\)-palettes.  Colour the six \(P\)-edges in
the order displayed in (2.1) by

\[
                         0,1,2,3,4,5
\]

and the six \(Q\)-edges in their displayed order by

\[
                         3,0,5,2,1,4.
\tag{2.5}
\]

At every outside vertex, its four incident edges have four distinct
colours.  Each cycle uses every colour once.

For either cycle \(Z=(z_0,\ldots,z_5)\), write

\[
 e_i=\{z_{i-1},z_i\},
 \qquad
                         F_i=F^{(\gamma(e_i))}
\tag{2.6}
\]

in Lemma 1.1.  Adjacent palettes are disjoint.  Let the resulting word
tables be

\[
 {\bf p}=(p_0,\ldots,p_5)
 \quad\hbox{for }P,
 \qquad
 {\bf q}=(q_0,\ldots,q_5)
 \quad\hbox{for }Q.
\]

In the word belonging to an edge \(e\), place the block \(G^{(\gamma(e))}\)
in the \(H-1\) positions immediately preceding its far endpoint
placeholder, where \(\gamma\) is (2.5).  These positions were arbitrary
fillers in Lemma 1.1, so its telescope is unchanged.  The palette count
in (0.1) is exactly

\[
             6(2H-1)+6(H-1)=18H-12\le |C|=M-2.
\]

## 3. Matching the filler columns

The protected columns of \({\bf p}\) and \({\bf q}\) already have the
same multisets: the endpoint columns contain every \(v_i\) once, each
\(F\)-palette-offset column contains one entry from every \(F^{(a)}\),
and each column in the protected block immediately before the far
endpoint contains one entry from every \(G^{(a)}\), because each cycle
uses all six edge colours once.
The unprotected filler columns can be matched too.

### Lemma 3.1 (columnwise filler alignment)

The remaining labels can be ordered in the twelve words so that

\[
 \boxed{
  \{p_i(j):0\le i<6\}_{\rm multi}
  =
  \{q_i(j):0\le i<6\}_{\rm multi}
  \quad\text{for every rooted position }j .}
\tag{3.1}
\]

#### Proof

For each core label \(c\), count the rows of \({\bf p}\) and
\({\bf q}\) in which \(c\) remains to be placed in a filler position.
If \(c\) lies outside all palettes, both counts are six.  If
\(c\in F^{(a)}\), its palette is used in two protected blocks in each
cyclic table, so both counts are four.  If \(c\in G^{(a)}\), its palette
is used once in each cyclic table, so both counts are five.

For each \(c\), match its available \({\bf p}\)-rows bijectively to its
available \({\bf q}\)-rows.  This produces a bipartite multigraph
between the six \(P\)-rows and six \(Q\)-rows, with one edge labelled
\(c\) for each matched occurrence.  Every row has degree equal to the
number of filler positions.  By König's theorem, this regular
bipartite multigraph decomposes into perfect matchings.  Use one
perfect matching per filler column, placing its edge label in its two
endpoint rows.  Every row uses every required label once, and the two
column multisets agree. \(\square\)

Write

\[
 P_j=\{p_i(j):0\le i<6\}_{\rm multi},
 \qquad
 Q_j=\{q_i(j):0\le i<6\}_{\rm multi}.
\]

Then

\[
                         P_j=Q_j\qquad(1\le j\le M).
\tag{3.2}
\]

## 4. The paired bidirectional packet

Take as the old shore

\[
                         {\bf p}\ \sqcup\ r{\bf q}
\tag{4.1}
\]

and as the new shore

\[
                         r{\bf p}\ \sqcup\ {\bf q}.
\tag{4.2}
\]

Thus the \(P\)-cycle recharge runs forward and the \(Q\)-cycle recharge
runs backward.

### Theorem 4.1 (histogram and trace cancellation)

The exchange (4.1)--(4.2) preserves every rooted position--label
histogram and has zero aggregate physical derivative at all
\(0\le h\le2H\).

#### Proof

At rooted position \(j\), the old label multiset is

\[
                         P_j+Q_{j+1},
\]

while the new multiset is

\[
                         P_{j+1}+Q_j.
\]

Here column indices are cyclic, so \(P_{M+1}=P_1\) and
\(Q_{M+1}=Q_1\).  They agree by (3.2).  This is coefficientwise in the ground labels, so
every \(C_{j,v}\) is fixed.

The forward \(P\)-recharge has zero derivative by Lemma 1.1.  The
backward \(Q\)-recharge is the inverse of another instance of that
lemma and separately has zero derivative.  Their union therefore has
zero derivative at every protected length. \(\square\)

The net word action is a left rotation on six tops and a right rotation
on six other tops.  It moves labels across every adjacent pair of
rooted positions while remaining in one histogram fibre.  Hence it
supplies the missing edge between the boundary-position component and
the position-three/remote component of the admitted-position graph.

## 5. Squarefreeness and coefficient one

For a cycle \(Z\), orient its edges as
\(e_i=z_{i-1}z_i\).  At an outside vertex \(v\), write
\(e^-_Z(v)\) and \(e^+_Z(v)\) for the incoming and outgoing edges.
The colouring (2.5) has

\[
 \gamma(e^-_P(v)),\ \gamma(e^+_P(v)),\
 \gamma(e^-_Q(v)),\ \gamma(e^+_Q(v))
 \quad\hbox{pairwise distinct for every }v.
\tag{5.1}
\]

Consequently the four incident \(F\)-palettes and the four incident
\(G\)-palettes at a fixed outside vertex carry four distinct colour
indices.  Every \(G\)-palette is also disjoint from every
\(F\)-palette.

### Lemma 5.1 (squarefree combined shores)

Both (4.1) and (4.2) have squarefree middle-owner decks.

#### Proof

Inside one top, injectivity of the word and \(M>2H\) make the retained
middle owners distinct.

A protected \(H\)-window meets at most one of the two outside
placeholders.  If it meets neither, its complementary owner contains
both outside labels, and the unordered outside pair identifies the top
because the twelve edges in (2.2) are distinct.

If it meets one placeholder, the owner retains the other outside label.
Two owners from different tops can then agree only when those tops share
that retained outside label.  We classify the possible deleted core
contexts at such a label \(v\).

For the unrotated word on \(e_i=z_{i-1}z_i\), deleting the near
placeholder retains \(z_i\) and deletes the pure context
\(F_i^{H-1}\).  Deleting the far placeholder retains \(z_{i-1}\) and
deletes

\[
 \operatorname{suf}_t G^{(\gamma(e_i))}
 \ \cup\ 
 \operatorname{pre}_{H-1-t}F_{i-1},
 \qquad 1\le t\le H-1.
\tag{5.2}
\]

After left rotation the near placeholder is in the invisible last
position, while deleting the far placeholder gives the same family
with \(0\le t\le H-1\).  Thus, on the old shore
\({\bf p}\sqcup r{\bf q}\), the contexts retaining \(v\) are:

* the pure \(F\)-context of \(e^-_P(v)\);
* the mixed \((G,F)\)-contexts of
  \((e^+_P(v),e^-_P(v))\), with \(1\le t\le H-1\); and
* the mixed \((G,F)\)-contexts of
  \((e^+_Q(v),e^-_Q(v))\), with \(0\le t\le H-1\).

The pure contexts in the first and third families have distinct
\(F\)-colours by (5.1).  Two genuinely mixed contexts can agree only
if their \(G\)-colours, their \(F\)-colours, and \(t\) all agree,
because all palettes are pairwise disjoint; (5.1) excludes this.  A
pure context cannot equal a genuinely mixed one because the \(F\)- and
\(G\)-families are globally disjoint.  Hence the old shore is
squarefree.  Interchanging \(P\) and \(Q\) gives the identical argument
for \(r{\bf p}\sqcup{\bf q}\).

This also shows why the edge-coloured assignment (2.6) is necessary.
The vertex assignment \(F_i=F^{(z_i)}\) would make the pure
\(P\)-incoming and rotated \(Q\)-outgoing contexts at \(v\) identical,
creating six duplicate middle owners on each shore. \(\square\)

Theorem 4.1 at \(h=H\) gives equality of the two middle incidence
vectors.  Lemma 5.1 says both are \(0\)-\(1\).  Therefore:

### Corollary 5.2 (coefficient-one recharge)

The old and new shores of (4.1)--(4.2) have exactly the same
middle-owner support.  Replacing one shore by the other inside a
coefficient-one table preserves coefficient one exactly.

## 6. Exact boundary

Proved:

1. an even-cycle extension of the full-trace recharge telescope;
2. two edge-disjoint six-top recharge carriers;
3. exact columnwise matching of their word tables;
4. a twelve-top bidirectional exchange preserving every
   position--label histogram and every protected trace;
5. squarefree, identical middle-owner supports; and
6. a bounded physical macro connecting adjacent rooted-position
   colours inside one histogram fibre.

Not proved:

1. a positive-density packing of these twelve-top packets;
2. a chronology interleaving them with \(\Theta(W)\) rectangle moves;
3. compatibility with a preassigned PBBS/MSW owner resolution; or
4. an all-position Markov-basis theorem with nonnegative intermediate
   tables.

The admitted-position graph obstruction is therefore closed locally.
The surviving deterministic gate is global packing and chronology of
the now-connected packet palette.
