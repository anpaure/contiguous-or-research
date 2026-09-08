# Position–label histogram invariance gives a linear global recharge cut

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, web input,
or generic nibble is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
 \qquad N=\binom{2m}{M},\qquad W=\binom{2m}{m},
\tag{0.1}
\]

and assume \(H=o(m)\) and the calibrated relation

\[
                         \frac WN=M+O(H).
\tag{0.2}
\]

Let

\[
                         g=M-8H-3=m-7H-3.
\tag{0.3}
\]

The three-top collar-neutral recharge theorem certifies at least \(g\)
different position-three labels, and hence \(g\) different boundary
directions, at a top when compatible helpers are available.  Thus

\[
                         gN=W-o(W)
\tag{0.4}
\]

is the global direction target.

For a one-word-per-top table \({\bf p}=(p_U:U\in\binom{[2m]}M)\), define
its position–label histogram

\[
 H_{j,c}({\bf p})
 =\#\{U:p_U(j)=c\},
 \qquad 1\le j\le M,\quad c\in[2m].
\tag{0.5}
\]

This note proves the following exact obstruction.

1. Every literal three-top recharge packet preserves every entry
   \(H_{j,c}\).  At the two active positions it cyclically permutes the
   three external labels among the three tops, in opposite directions;
   all other position entries are fixed top by top.

2. Every packet swaps only position three and one remote position whose
   cyclic distance is greater than \(4H\).  Hence, at each fixed top,
   positions \(1,2,4,\ldots,H+1\) are invariant throughout a recharge
   chronology.  Within this packet library, the underlying middle
   boundary edge at a top is therefore determined by its position-three
   label.

3. Put

   \[
                         S_3({\bf p})=
                         \{c:H_{3,c}({\bf p})>0\}.
   \tag{0.6}
   \]

   In an arbitrarily long recharge chronology starting from \({\bf p}\),
   every position-three direction \((U,c)\) has \(c\in S_3({\bf p})\).
   Therefore the total number of distinct position-three direction atoms
   which can ever be exposed is at most

   \[
       \boxed{
       |S_3({\bf p})|\binom{2m-1}{M-1}
       =|S_3({\bf p})|\frac{M}{2m}N.}
   \tag{0.7}
   \]

4. Consequently an \(o(W)\)-leave schedule requires

   \[
       \boxed{|S_3({\bf p})|
       \ge \frac{2mg}{M}-o(m)=2m-O(H).}
   \tag{0.8}
   \]

   Thus almost every ground coordinate must already occur in position
   three somewhere in the initial coefficient-one table.  Top and owner
   capacity alone do not imply this condition.

5. There is an explicit physical histogram chamber with a linear cut.
   Give \([2m]\) its natural order and list every top increasingly.  Then

   \[
       H_{j,c}=\binom{c-1}{j-1}\binom{2m-c}{M-j},
   \tag{0.9}
   \]

   so

   \[
                         |S_3|=2m-M+1=m-H+1.
   \tag{0.10}
   \]

   Every recharge chronology in this histogram fibre can expose at most

   \[
       (m-H+1)\frac{m+H}{2m}N
       =\left(\frac12+o(1)\right)W
   \tag{0.11}
   \]

   distinct position-three directions.  Its unavoidable leave relative
   to (0.4) is at least

   \[
                         \left(\frac12-o(1)\right)W.
   \tag{0.12}
   \]

6. The increasing table is in fact an isolated vertex of the recharge
   state graph: no three-top packet source shore or inverse source shore
   occurs in it.  On a packet triangle, the three position-three labels
   must form a cyclic endpoint selection.  Third order statistics in a
   common total order cannot form such a cycle.

The capacity cut (0.7) applies verbatim to a coefficient-one table.  The
increasing all-top table is used only as an explicit physical state and
histogram counterexample; this note does not assert that its middle
owner decks are globally squarefree.  Hence the result is a decisive
obstruction to a universal source-allocation theorem and to rounding the
fully symmetric quotient flow inside an arbitrary histogram fibre.  It
does not rule out a specially constructed coefficient-one initial table
whose position-three support already has size \(2m-O(H)\).

## 1. The literal histogram action of one packet

We recall only the positional data of the local recharge packet.  Let
\(C\) have size \(M-2\), choose distinct \(x,a,y\notin C\), and put

\[
 U_0=C\cup\{x,y\},\qquad
 U_1=C\cup\{x,a\},\qquad
 U_2=C\cup\{a,y\}.
\tag{1.1}
\]

The \(U_0\)-path uses the positional base \(\omega\), rooted two
letters before placeholder \(A\).  The \(U_1,U_2\)-paths use the
companion base \(\eta\), rooted two letters before placeholder \(B\).
The matched-cut construction makes the other placeholder occur at one
common rooted position, say \(b\), on all three paths.  The two shores
are obtained by swapping the labels in positions \(3,b\) at each top.

On the source shore, the ordered pairs in these two positions are

\[
\begin{array}{c|c|c}
 &3&b\\ \hline
 U_0&x&y\\
 U_1&a&x\\
 U_2&y&a
\end{array}
\tag{1.2}
\]

and on the target shore they are

\[
\begin{array}{c|c|c}
 &3&b\\ \hline
 U_0&y&x\\
 U_1&x&a\\
 U_2&a&y.
\end{array}
\tag{1.3}
\]

The multiset in either active column is \(\{x,a,y\}\) on both shores.
At every other rooted position, the label on each individual top is
unchanged.

### Theorem 1.1 (complete position–label invariance)

For every literal recharge packet \(P\), every position \(j\), and
every label \(c\),

\[
 H_{j,c}({\cal S}^+(P))-H_{j,c}({\cal S}^-(P))=0.
\tag{1.4}
\]

Consequently every chronological composition of packets preserves the
full array \((H_{j,c})\).

#### Proof

Equations (1.2)--(1.3) prove the assertion at positions \(3,b\).  All
other entries agree top by top.  Add the packet identities along a
chronology. \(\square\)

The theorem is strictly finer than preservation of the unordered top
sets or of the middle-owner incidence vector.  It is absent from the
top/owner projection of the recharge hypergraph.

The certified two-top boundary rectangles do not change position three
at either incident top.  They only interchange positions one and two,
and their two legs preserve the aggregate histograms in those columns.
Therefore Theorem 1.1 and every cut below remain valid when arbitrary
chronologically applicable boundary rectangles are interleaved with the
recharge packets.

## 2. Direction atoms and the support cut

A **position-three direction atom** for this recharge library is a pair

\[
                         (U,c),\qquad |U|=M,\quad c\in U,
\tag{2.1}
\]

meaning that a rooted path on \(U\) has \(c\) in position three.  On
every recharge incidence, the second active placeholder is remote from
the protected prefix.  Consequently positions

\[
                         1,2,4,5,\ldots,H+1
\tag{2.1a}
\]

on a fixed top are unchanged by every packet, irrespective of whether
that top is the \(\omega\)-row or one of the two \(\eta\)-rows.  The
unordered first pair and the remaining middle collar are therefore
fixed throughout the recharge chronology.

Different values of \(c\) give different boundary-swap traces: at
complementary length two the derivative is

\[
 e_{K_c\cup\{p_2\}}-e_{K_c\cup\{p_1\}},
 \qquad
 K_c=U\setminus\{p_1,p_2,c\}.
\tag{2.2}
\]

At the middle length the same conclusion follows from

\[
 K_H(c)=U\setminus
 \{p_1,p_2,c,p_4,\ldots,p_{H+1}\}.
\tag{2.2a}
\]

Conversely, the fixed entries (2.1a) show that returning the same label
\(c\) to position three returns the same underlying boundary edge (only
the two K2 orientations can differ).  Thus distinct useful underlying
directions generated by this packet library inject into the atoms
\((U,c)\).  The atom count is a valid upper bound here.  No assertion is
made for a larger move library which is also allowed to alter the
protected collar positions in (2.1a).

### Theorem 2.1 (fixed-histogram source-capacity cut)

Let a packet chronology start at \({\bf p}\), with arbitrary length,
arbitrary helper reuse, and arbitrary changing common cores.  The number
of distinct position-three atoms appearing anywhere in the chronology
is at most (0.7).

#### Proof

If \(c\notin S_3({\bf p})\), then \(H_{3,c}=0\) initially.  Theorem 1.1
makes it zero at every later state, so no atom \((U,c)\) can appear.
For a fixed allowed label \(c\), the number of eligible tops is exactly

\[
                         \#\{U:c\in U\}
                         =\binom{2m-1}{M-1}.
\tag{2.3}
\]

Sum this bound over \(c\in S_3({\bf p})\). \(\square\)

No chronological repetition can evade Theorem 2.1.  A positive
histogram entry may move among many tops, but a zero entry is an absent
token species and remains absent forever.

### Corollary 2.2 (necessary histogram breadth)

If a chronology exposes at least \(gN-o(W)\) distinct atoms, then (0.8)
holds.

#### Proof

Combine Theorem 2.1 with

\[
 |S_3|\frac{M}{2m}N\ge gN-o(W).
\tag{2.4}
\]

Divide by \(MN/(2m)=\Theta(W/m)\).  Since \(o(W)/(W/m)=o(m)\), this
gives

\[
                         |S_3|\ge\frac{2mg}{M}-o(m).
\tag{2.5}
\]

Finally \(g=M-O(H)\), proving (0.8). \(\square\)

The same argument works at every rooted position \(j\).  Position three
is singled out only because it directly indexes the rechargeable
boundary direction in the literal packet.

## 3. The increasing histogram chamber

Fix the order

\[
                         1<2<\cdots<2m
\tag{3.1}
\]

and, for every top \(U\), let \(p_U\) list the elements of \(U\) in
increasing order.

### Lemma 3.1 (exact order-statistic histogram)

For this table,

\[
 H_{j,c}=\binom{c-1}{j-1}\binom{2m-c}{M-j}.
\tag{3.2}
\]

In particular,

\[
 S_3=\{3,4,\ldots,2m-M+3\},
 \qquad |S_3|=2m-M+1=m-H+1.
\tag{3.3}
\]

#### Proof

For \(c\) to occupy position \(j\), the top must contain \(c\), exactly
\(j-1\) labels below it, and exactly \(M-j\) labels above it.  This
gives (3.2).  The two binomial factors in (3.2) at \(j=3\) are positive
exactly when

\[
                         c\ge3,\qquad c\le2m-M+3,
\]

proving (3.3). \(\square\)

### Theorem 3.2 (linear histogram deficiency)

Every recharge chronology in the histogram fibre of the increasing
table misses at least \((1/2-o(1))W\) of the \(gN\) certified direction
target.

#### Proof

Theorem 2.1 and (3.3) give the upper bound

\[
 D_{\rm inc}
 \le(m-H+1)\frac{m+H}{2m}N.
\tag{3.4}
\]

Since \(W/N=M+O(H)=m+O(H)\), the right side is

\[
                         \left(\frac12+o(1)\right)W.
\tag{3.5}
\]

On the other hand \(gN=W-o(W)\).  Subtraction proves the theorem.
\(\square\)

This is a capacity cut for an arbitrarily long, fully helper-recycled
chronology.  It is not the fresh-helper forest bound: even unlimited
reuse cannot create a label species absent from position three.

## 4. The increasing table has no source packet

The preceding cut can be sharpened to zero first-step capacity.

Fix a proposed packet common core \(C\) and write its three external
labels in increasing order as

\[
                         \alpha<\beta<\gamma.
\tag{4.1}
\]

For \(t\notin C\), put

\[
                         r(t)=\#\{c\in C:c<t\}.
\tag{4.2}
\]

The function \(r\) is nondecreasing.  On a top \(C\cup\{u,v\}\),
where \(u<v\), the third smallest label is

\[
\begin{cases}
 u,&r(u)=2,\\
 v,&r(v)=1,
\end{cases}
\tag{4.3}
\]

whenever it is one of the two external labels.  In all other cases it
belongs to \(C\).

A recharge packet source or target shore requires the three
position-three labels on the edge tops

\[
 C\cup\{\alpha,\beta\},\quad
 C\cup\{\alpha,\gamma\},\quad
 C\cup\{\beta,\gamma\}
\tag{4.4}
\]

to use each of \(\alpha,\beta,\gamma\) exactly once.  There are exactly
two such endpoint selections:

\[
\begin{array}{c|ccc}
 &\alpha\beta&\alpha\gamma&\beta\gamma\\ \hline
 \text{I}&\beta&\alpha&\gamma\\
 \text{II}&\alpha&\gamma&\beta.
\end{array}
\tag{4.5}
\]

They are the two cyclic orientations of the triangle.

### Theorem 4.1 (isolated monotone chamber)

Neither selection in (4.5) can occur in the increasing table.  Hence
that table contains no source shore of a three-top recharge packet and
no source shore of its inverse.

#### Proof

For selection I, the edge \(\alpha\beta\) chooses its larger endpoint,
so (4.3) gives \(r(\beta)=1\).  The edge \(\alpha\gamma\) chooses its
smaller endpoint, giving \(r(\alpha)=2\).  This contradicts

\[
                         r(\alpha)\le r(\beta).
\tag{4.6}
\]

For selection II, the edge \(\alpha\beta\) chooses its smaller endpoint,
so \(r(\alpha)=2\), while \(\alpha\gamma\) chooses its larger endpoint,
so \(r(\gamma)=1\).  This contradicts

\[
                         r(\alpha)\le r(\gamma).
\tag{4.7}
\]

If one of the third-smallest labels belongs to \(C\), it is not a
packet placeholder and cannot repair either selection.  Thus no packet
or inverse packet is incident with the table. \(\square\)

The proof uses only the three position-three source labels.  It is
independent of arm choices, deleted-phase blocks, owner supports, or
the choice of which top is named focal.

## 5. Consequence for the symmetric fractional flow

The symmetric top/owner quotient assigns equal weight to the full
\(S_{2m}\)-orbit of role-labelled packets.  Its exact loads are
favorable:

\[
 \text{top load}=g,\qquad
 \text{owner load}=\frac{gd}{W/N}<g.
\tag{5.1}
\]

This remains a correct fractional identity in the quotient resource
hypergraph.  It is not a fractional flow inside one literal state
fibre.  Coordinate permutations move the position–label histogram:

\[
                         H_{j,c}\longmapsto H_{j,\sigma^{-1}c}.
\tag{5.2}
\]

Orbit averaging therefore mixes mutually unreachable histogram fibres.
The increasing chamber has zero incident packet columns by Theorem 4.1,
whereas the orbit-averaged quotient gives every top positive degree.
This is the exact reuse error.

### Corollary 5.1 (no universal owner/top rounding theorem)

There is no theorem which, from only the top capacities, middle-owner
capacities, and the symmetric fractional packet weights, rounds a
legal recharge schedule from every literal initial table.  Any correct
positive theorem must additionally assume or construct a coefficient-one
initial table satisfying at least the histogram breadth condition
(0.8), and must round using packet columns which remain inside that one
histogram fibre.

#### Proof

The increasing table has the same complete top set as the quotient
problem but has no incident literal packet column.  More quantitatively,
its invariant fibre violates (0.8) and has the linear deficiency
(0.12). \(\square\)

## 6. Exact implication boundary

Proved:

1. complete global position–label histogram invariance of every
   three-top recharge packet;
2. the fixed-histogram direction-capacity cut (0.7);
3. the necessary breadth \(|S_3|\ge2m-O(H)\) for an \(o(W)\) leave;
4. the exact increasing histogram (0.9)--(0.10);
5. its \((1/2-o(1))W\) missing-direction cut;
6. absence of every packet and inverse-packet source shore at the
   increasing table; and
7. failure of the fully symmetric quotient flow to live in one state
   fibre.

Not proved:

1. existence of a near-perfect coefficient-one initial table with
   \(|S_3|=2m-O(H)\);
2. a helper-recycling schedule inside such a broad histogram fibre;
3. sufficiency of histogram breadth for source expansion; or
4. a universal obstruction applying to every broad coefficient-one
   histogram fibre.

Thus the global source-allocation problem has a rigorous capacity cut,
but not yet a universal negative answer.  The next surviving positive
target is sharply constrained: first construct a coefficient-one table
whose position-three histogram has almost full coordinate support, then
build the recurrent packet circulation without leaving that fixed
histogram fibre.
