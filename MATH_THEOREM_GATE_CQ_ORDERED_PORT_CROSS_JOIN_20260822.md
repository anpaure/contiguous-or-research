# Gate \(C_{\rm Q}\): ordered packet ports, clean joins, and the exact post-matching obstruction

**Status (2026-08-22).** Every theorem and lemma below is proved.  This
note does not prove Gate \(C_{\rm Q}\).  It does three things which are
needed before an ordered-lift theorem can be stated correctly.

1. It identifies a phase packet with one directed arc between ordered
   FIFO boundary queues, including its reversal and its two-puncture
   freedom.
2. It proves that a matching in the **full** \((b+1)\)-vertex packet
   hypergraph cannot be chained unchanged: every exact join reuses one
   endpoint middle target.  A near-perfect full-support matching therefore
   has one trail per packet unless at least \(\Omega(W/b)\) boundary
   occurrences are switched.  This repair scale is \(o(W)\), so it is a
   precise obstruction to post-processing, not a disproof of the route.
3. It gives the exact path-cover statistic and the exact triangular
   condition for cleanliness at every cross-join through rank \(b+H\).
   The complete local port fibre has a clean perfect transition matching;
   hence cleanliness is locally feasible.  However, iterating that
   canonical perfect matching repeats \(b-2\) internal cores after only
   two joins, so it cannot be combined wholesale with a middle matching.
   The unresolved theorem is a *correlated internal-core matching and port
   circulation*, together with the colored cross-collar coverage ledger.

Throughout, \(b\ge 5\), \(|\Omega|=2b\),

\[
 W={2b\choose b},\qquad 2\le H\le b-2,\qquad g=b+H,
 \qquad m=b-1.                                           \tag{0.1}
\]

For the live application,
\(H=\lceil\sqrt{2b\log(2b)}\rceil=o(b)\).

## 1. A phase packet is an ordered-queue arc

Let \(\mathcal Q_b\) be the set of injective ordered \(b\)-tuples over
\(\Omega\).  For

\[
 Q=(q_0,\ldots,q_{b-1})
\]

write \([Q]=\{q_0,\ldots,q_{b-1}\}\) and
\(Q^{\leftarrow}=(q_{b-1},\ldots,q_0)\).

A labelled phase packet consists of distinct \(u,v\in\Omega\) and
ordered disjoint tuples

\[
 X=(x_1,\ldots,x_m),\qquad Y=(y_1,\ldots,y_m)           \tag{1.1}
\]

whose entries partition \(\Omega\setminus\{u,v\}\).  Its emitted word is

\[
              u,x_1,\ldots,x_m,y_1,\ldots,y_m,u.       \tag{1.2}
\]

Put

\[
 A=(u,x_1,\ldots,x_m),\qquad
 B=(y_1,\ldots,y_m,u).                                  \tag{1.3}
\]

The consecutive length-\(b\) windows of (1.2) are denoted
\(C_0,\ldots,C_b\); thus \([A]=C_0\) and \([B]=C_b\).

### Lemma 1.1 (exact port normal form)

The map (1.3) is a bijection between labelled directed phase packets and
ordered pairs \((A,B)\in\mathcal Q_b^2\) satisfying

\[
              [A]\cap[B]=\{a_0\}=\{b_{b-1}\}.          \tag{1.4}
\]

The unique omitted symbol is

\[
              v=\Omega\setminus([A]\cup[B]).           \tag{1.5}
\]

Reversing the same middle path replaces the arc

\[
                 A\longrightarrow B
 \quad\hbox{by}\quad
                 B^{\leftarrow}\longrightarrow A^{\leftarrow}. \tag{1.6}
\]

If only the internal middle path \(C_1,\ldots,C_{b-1}\) is retained,
then interchanging \(u\) and \(v\) leaves all these internal sets
unchanged and gives the second puncture choice.

#### Proof

Equations (1.1)--(1.3) give (1.4), and their union omits exactly \(v\),
giving (1.5).  Conversely, from (1.4) set

\[
 u=a_0=b_{b-1},\qquad
 X=(a_1,\ldots,a_{b-1}),\qquad
 Y=(b_0,\ldots,b_{b-2}),
\]

and use (1.5).  This recovers a unique labelled directed packet.

Reading (1.2) backwards gives

\[
 u,y_m,\ldots,y_1,x_m,\ldots,x_1,u,
\]

whose boundary queues are \(B^{\leftarrow}\) and
\(A^{\leftarrow}\), and whose length-\(b\) windows are
\(C_b,C_{b-1},\ldots,C_0\).  Finally, for \(1\le i\le b-1\),

\[
 C_i=\{x_i,\ldots,x_m\}\cup\{y_1,\ldots,y_i\},         \tag{1.7}
\]

which contains neither \(u\) nor \(v\).  Swapping them therefore changes
only the two boundary sets and proves the last assertion. \(\square\)

Thus orientation provides two directed realizations of a full packet,
not an arbitrary ordering of either endpoint queue.  An internal path has
the additional two choices of which missing symbol is the repeated pivot.

## 2. Why a full-support packet matching has no unchanged joins

For a phase packet \(P\), let

\[
                  \mathsf S(P)=\{C_0,C_1,\ldots,C_b\}   \tag{2.1}
\]

be its full middle support.  A full-support packet matching is a family
whose sets (2.1) are pairwise disjoint.

### Theorem 2.1 (endpoint-reuse obstruction)

No two members of a full-support packet matching can be joined as
unchanged phase packets, in either orientation.  Hence a family of \(N\)
matched full supports has exactly \(N\) packet trails under unchanged
post-hoc orientation and ordering.

If those supports cover \(W-o(W)\) middle targets, then

\[
                    N={W-o(W)\over b+1},               \tag{2.2}
\]

and consequently

\[
                    gN=(1-o(1))W,                       \tag{2.3}
\]

not \(o(W)\).  Such a matching cannot by itself satisfy the fragment
overhead condition in the direct-hole compiler.

#### Proof

An exact FIFO join from packet \(P\) to packet \(P'\) identifies the
ending ordered queue of \(P\) with the starting ordered queue of \(P'\).
Their underlying \(b\)-sets are therefore equal.  This set is an endpoint
member of both \(\mathsf S(P)\) and \(\mathsf S(P')\), contradicting
disjointness.  Reversal only exchanges the two endpoint queues, so it does
not change the argument.  Thus every packet is an isolated trail.

Every full support has \(b+1\) vertices, which gives (2.2).  Since
\(g/(b+1)\to1\), (2.3) follows. \(\square\)

The obstruction has exactly the admissible asymptotic repair scale.

### Corollary 2.2 (minimum boundary-switch scale)

Start with \(N\) pairwise-disjoint full packet supports.  Suppose their
packet interiors are kept, but endpoint occurrences may be changed so
that the packets form \(t\) linear trails.  Then at least

\[
                         N-t                              \tag{2.4}
\]

original endpoint occurrences must be changed.

In particular, \(t=o(N)\) requires \((1-o(1))N=\Theta(W/b)\) endpoint
switches.  This is \(o(W)\), so a joint matching-and-switching theorem is
still possible, but a zero-switch post-processing theorem is false.

#### Proof

The trails use exactly \(N-t\) joins.  At each join, two endpoint
occurrences which were originally distinct must become one common boundary
set.  Hence at least one endpoint in that pair changes.  No endpoint
occurrence participates in two joins, so these lower bounds add. \(\square\)

This is why the viable selector must match the internal cores
\(C_1,\ldots,C_{b-1}\), permitting deliberate boundary overlap, or must
build the boundary switches into the selection itself.

## 3. Exact trail statistic and queue imbalance

Fix orientations of \(N\) selected packet occurrences and regard them as
arcs \(A\to B\) in the queue digraph of Lemma 1.1.  A transition pairing
\(\mathcal J\) is a set of ordered packet pairs \((P,P')\) such that the
head queue of \(P\) equals the tail queue of \(P'\), and every packet has
at most one predecessor and at most one successor.  It decomposes the
packet occurrences into directed paths and directed cycles.  A cycle is
linearized by cutting one of its joins.  Let \(c(\mathcal J)\) be the
number of directed cycle components.

### Lemma 3.1 (exact number of linear trails)

The number of resulting linear packet trails is

\[
                 \boxed{t=N-|\mathcal J|+c(\mathcal J).} \tag{3.1}
\]

#### Proof

A path component on \(r\) packets contains \(r-1\) joins and contributes
one trail; a cycle component on \(r\) packets contains \(r\) joins and,
after one cut, also contributes one trail.  Summing the two identities over
components gives (3.1). \(\square\)

For a queue \(Q\), write \(d^+(Q)\) and \(d^-(Q)\) for the numbers of
selected arcs leaving and entering \(Q\), respectively, and put

\[
 \Delta_{\rm port}
   ={1\over2}\sum_{Q\in\mathcal Q_b}|d^+(Q)-d^-(Q)|
   =N-\sum_Q\min\{d^+(Q),d^-(Q)\}.                     \tag{3.2}
\]

### Corollary 3.2 (necessary port circulation)

Every trail decomposition satisfies

\[
                         t\ge\Delta_{\rm port}.          \tag{3.3}
\]

It also has at least one trail in every nonempty weak component of the
selected queue multigraph.  Thus a coefficient-one lift with
\(N=\Theta(W/b)\) necessarily has

\[
 \Delta_{\rm port}=o(N),\qquad
 \#\{\text{nonempty queue components}\}=o(N).          \tag{3.4}
\]

#### Proof

At \(Q\), at most \(\min\{d^+(Q),d^-(Q)\}\) incoming and outgoing packet
ends can be paired.  Summing over \(Q\), then applying (3.1), gives
\(t\ge N-|\mathcal J|\ge\Delta_{\rm port}\).  A trail cannot move between
weak components, proving the second assertion. \(\square\)

There is an equivalent short-connector lower bound.  For two queues
\(Q,R\), define their ordered overlap

\[
 \operatorname{ov}(Q,R)=max\{0\le\ell\le b:
 (q_{b-\ell},\ldots,q_{b-1})=(r_0,\ldots,r_{\ell-1})\}. \tag{3.5}
\]

### Lemma 3.3 (FIFO reset lower bound)

Any FIFO bridge which changes state \(Q\) into state \(R\) by appending
\(d<b\) singleton letters must satisfy

\[
                         d\ge b-\operatorname{ov}(Q,R). \tag{3.6}
\]

Therefore replacing exact joins by bridges at \(N-o(N)\) packet
boundaries has total bridge length \(o(W)\), with \(N=\Theta(W/b)\), only
if the average ordered overlap is \(b-o(b)\).

#### Proof

After \(d\) FIFO steps, the first \(b-d\) entries of the new queue are
the last \(b-d\) entries of \(Q\).  Equality with \(R\) forces an ordered
overlap of length \(b-d\), proving (3.6).  Summing (3.6) over the joins
gives the last assertion. \(\square\)

The overlap condition is necessary only; repeated symbols elsewhere can
make a nominal short reset nonclean.

## 4. Exact all-offset cleanliness at one packet join

Consider two exactly joined directed packets

\[
                         A\longrightarrow B\longrightarrow C, \tag{4.1}
\]

so the local singleton word is the concatenation \(ABC\) of three
ordered \(b\)-tuples.  Write tuple indices from \(0\) to \(b-1\).

### Theorem 4.1 (triangular cross-join criterion)

Every contiguous window in \(ABC\) of length at most \(g=b+H\) which
meets the join of the two packets is clean if and only if

\[
 \boxed{
 A_r\ne C_s\quad
 \text{whenever }0\le s\le H-2
 \text{ and }b-H+1+s\le r\le b-1.}                    \tag{4.2}
\]

There are exactly

\[
                         {H(H-1)\over2}                 \tag{4.3}
\]

potentially forbidden position pairs in (4.2).  Consequently a packet
trail is a physical clean word through all ranks
\(b-H,\ldots,b+H\) if and only if (4.2) holds at every internal packet
join.

#### Proof

Inside \(A\), \(B\), or \(C\) there is no repetition.  Legality of the
two packets gives

\[
 [A]\cap[B]=\{A_0=B_{b-1}\},\qquad
 [B]\cap[C]=\{B_0=C_{b-1}\}.                           \tag{4.4}
\]

The two occurrences in either intersection are separated by exactly
\(2b-1\) positions in \(ABC\), so no window of length at most
\(b+H\le2b-2\) contains both.  The only other possible repetition is
between \(A_r\), at global position \(r\), and \(C_s\), at global
position \(2b+s\).  These two occurrences fit in a window of length at
most \(b+H\) exactly when

\[
              2b+s-r\le b+H-1,
\]

which rearranges to the range in (4.2).  Summing its row lengths gives
\((H-1)+(H-2)+\cdots+1=H(H-1)/2\).

Since \(g<2b\), any window meets at most two successive packet joins, and
any new repetition at such a crossing is covered by the preceding
three-block calculation.  Cleanliness at every join is therefore
equivalent to cleanliness of the entire trail through length \(g\).
Every shorter band window is included. \(\square\)

The upper-offset targets which genuinely depend on both packets can also
be written exactly.  For \(2\le q\le H\) and \(1\le t\le q-1\), put

\[
 U_{q,t}(A,B,C)=
 \{A_{b-t},\ldots,A_{b-1}\}\cup[B]\cup
 \{C_0,\ldots,C_{q-t-1}\}.                             \tag{4.5}
\]

### Lemma 4.2 (cross-collar ledger)

Under (4.2), (4.5) is a \((b+q)\)-set.  It is the length-\((b+q)\)
window beginning \(t\) starts before the common packet boundary.  These
are exactly the upper-band occurrences not contained in either individual
two-queue packet word.  There are \(q-1\) at rank \(b+q\), and

\[
                  \sum_{q=2}^H(q-1)={H(H-1)\over2}      \tag{4.6}
\]

per joined boundary.  No analogous triple-queue occurrence is needed
below the middle rank.

#### Proof

The window beginning \(t\) positions before the boundary contains the
last \(t\) symbols of \(A\), all \(b\) symbols of \(B\), and the first
\(q-t\) symbols of \(C\), which is (4.5).  Equation (4.4) makes each
outer piece disjoint from \(B\), while (4.2) makes the two outer pieces
disjoint from each other, so the size is \(b+q\).

For a length-\((b+q)\) window, the starts strictly between the last start
contained in \(AB\) and the boundary start contained in \(BC\) are
exactly \(t=1,\ldots,q-1\).  A window of length below \(b\) beginning in
one packet never needs letters beyond the next packet word.  This proves
the ledger. \(\square\)

For \(N-o(N)\) joins and \(N=\Theta(W/b)\), (4.6) contains

\[
       \Theta\!\left({WH^2\over b}\right)
       =\Theta(W\log b)                                 \tag{4.7}
\]

occurrences at the live value of \(H\).  Equation (4.7) is not a lower
bound on the number of holes—many occurrences may cover the same required
targets—but it proves that discarding or repairing every cross-collar
occurrence separately is not a coefficient-one argument.  Their colored
coverage must be controlled collectively.

## 5. Clean transitions are locally abundant

Fix a boundary queue \(B=(b_0,\ldots,b_{b-1})\).  There are exactly
\(b!\) legal packet arcs entering \(B\) and \(b!\) legal packet arcs
leaving \(B\).  Indeed, on either side one chooses the omitted point from
a \(b\)-element complement and orders the remaining \(b-1\) points.

For an incoming queue

\[
                         A=(b_{b-1},a_1,\ldots,a_{b-1}), \tag{5.1}
\]

define

\[
                         \Phi_B(A)=(a_1,\ldots,a_{b-1},b_0). \tag{5.2}
\]

### Theorem 5.1 (a clean perfect local transition matching)

The map \(A\mapsto\Phi_B(A)\) is a bijection from all legal incoming
packet queues at \(B\) to all legal outgoing packet queues at \(B\).
Every transition

\[
                         A\longrightarrow B\longrightarrow\Phi_B(A) \tag{5.3}
\]

satisfies (4.2) for every \(H\le b-2\).

#### Proof

The tuple \((a_1,\ldots,a_{b-1})\) consists of all but one point of
\(\Omega\setminus[B]\).  Hence (5.2) meets \(B\) only in its last
entry \(b_0\), so it is a legal outgoing queue.  Conversely every legal
outgoing queue has the form

\[
 C=(c_0,\ldots,c_{b-2},b_0),
\]

and its unique preimage is
\((b_{b-1},c_0,\ldots,c_{b-2})\).  Thus \(\Phi_B\) is a bijection.

The only common symbols of \(A\) and \(\Phi_B(A)\) are
\(a_r\) at positions \(r\) and \(r-1\), for \(1\le r\le b-1\).
Their index difference is one, whereas (4.2) forbids only differences at
least \(b-H+1\ge3\).  Thus every transition is clean. \(\square\)

There are in fact factorially many clean continuations.  Put \(h=H-1\)
and suppose \(2h\le b\).

### Corollary 5.2 (explicit clean continuation degree)

Every incoming packet at \(B\) has at least

\[
                  d_H=(b-h)_h\,(b-h)!                  \tag{5.4}
\]

outgoing packets which satisfy (4.2), where
\((x)_h=x(x-1)\cdots(x-h+1)\).  Moreover,

\[
 {d_H\over b!}
 ={(b-h)!^2\over(b-2h)!b!}
 =\exp\!\left\{-{h^2\over b}+O\!\left({h^3\over b^2}\right)\right\}. \tag{5.5}
\]

At the live scale this is \((2b)^{-2+o(1)}\), so
\(d_H=b!\,b^{-2+o(1)}\).

#### Proof

Let \(v\) be the point omitted by the incoming packet.  The pool for the
first \(b-1\) entries of an outgoing queue is

\[
 R=\{a_1,\ldots,a_{b-1},v\}.                            \tag{5.6}
\]

Represent an outgoing choice by a permutation of \(R\), whose last entry
is omitted.  A sufficient condition for (4.2) is that its first \(h\)
entries avoid

\[
                  \{a_{b-h},\ldots,a_{b-1}\}.           \tag{5.7}
\]

There are \((b-h)_h\) ordered choices for those first positions and
\((b-h)!\) orders of the remaining entries, proving (5.4).  Dividing by
\(b!\) gives the first equality in (5.5).  Also

\[
 \log{d_H\over b!}
 =\sum_{j=0}^{h-1}\log\left(1-{h\over b-j}\right)
 =-{h^2\over b}+O\!\left({h^3\over b^2}\right),
\]

uniformly for \(h=o(b^{2/3})\).  The live \(h\) is in this range and has
\(h^2/b=2\log(2b)+o(\log b)\), proving the final assertion. \(\square\)

Theorem 5.1 shows that the full local port fibre has no cleanliness or
Hall obstruction.  It does **not** imply that the subfamilies left by a
middle-core matching contain any compatible transition: the matching can
select a very sparse and adversarial subset of the factorial port fibre.

There is also an exact reason why the particular perfect matching
\(\Phi_B\) cannot simply be imposed during the middle matching.

### Theorem 5.3 (the canonical clean factor repeats after two packets)

Start from a legal packet arc \(A\to B\), and at every later boundary use
the canonical successor (5.2).  Put

\[
 Z=(a_0,a_1,\ldots,a_{b-1},b_0,b_1,\ldots,b_{b-2}),     \tag{5.8}
\]

viewed as a cyclic word of length \(2b-1\).  Then:

1. the omitted point stays fixed, and the successive boundary queues are
   the length-\(b\) cyclic blocks of \(Z\) whose starting phases advance
   by \(b\);
2. every canonical packet orbit has exactly \(2b-1\) packets; and
3. three consecutive canonical packets are not internally
   middle-disjoint.  More precisely, the first and third packets share
   exactly \(b-2\) of their internal middle targets.

Consequently every internally middle-disjoint trail which uses only the
canonical transitions of Theorem 5.1 has at most two packets.  Such a
choice gives at least \(N/2\) trails and cannot satisfy (6.5).

#### Proof

The first two queues in the periodic reading of \(Z\) are

\[
 A=(a_0,\ldots,a_{b-1}),\qquad
 B=(b_0,\ldots,b_{b-2},a_0).
\]

The next is

\[
 (a_1,\ldots,a_{b-1},b_0)=\Phi_B(A).
\]

Repeating this identity proves the first assertion.  In particular no new
symbol is omitted.  Since
\(\gcd(b,2b-1)=1\), the boundary phase returns for the first time after
\(2b-1\) packets, proving part 2.

Index cyclic start phases modulo \(2b-1\).  The internal targets of the
first packet start at

\[
                         1,2,\ldots,b-1.                \tag{5.9}
\]

Those of the second start at

\[
                         b+1,b+2,\ldots,2b-2,0,          \tag{5.10}
\]

so the first two internal supports are disjoint.  The third packet begins
at phase \(2b\equiv1\), and its internal starts are

\[
                         2,3,\ldots,b.                  \tag{5.11}
\]

The intersection of (5.9) and (5.11) is
\(\{2,\ldots,b-1\}\), of size \(b-2\).  Distinct cyclic starts of \(Z\)
give distinct length-\(b\) sets: equality of two proper arcs in an odd
cycle would force either equal starts or complementary arcs, and the
complement has size \(b-1\).  Thus the start overlap is exactly a target
overlap.  Every three consecutive canonical packets are a cyclic translate
of this calculation. \(\square\)

The obstruction is special to \(\Phi_B\).  An arbitrary exact clean join
does not preserve the omitted point or a fixed cyclic order; Theorem 5.3
does not force general packet trails to be coherent fixed-order cycles.

## 6. The exact repaired Gate-\(C_{\rm Q}\) interface

For a fixed oriented selected packet family \(\mathcal P\), and a queue
\(B\), form a bipartite graph \(G_B^H\).  Its left vertices are selected
packets ending at \(B\), its right vertices are selected packets starting
at \(B\), and an edge is present precisely when (4.2) holds.  Let
\(\mu_B^H\) be its matching number.  Local matchings at distinct queues
are independent, so the largest possible number of clean packet joins is

\[
                         J_H(\mathcal P)=\sum_B\mu_B^H. \tag{6.1}
\]

Choose local matchings attaining (6.1), or smaller local matchings if this
reduces the number of resulting directed cycles, and define

\[
 \tau_H(\mathcal P)=
 \min_{\mathcal J}
 \{N-|\mathcal J|+c(\mathcal J):
       \mathcal J\text{ uses only edges of the }G_B^H\}. \tag{6.2}
\]

If packet orientations, and for internal paths their two puncture choices,
are still free, minimize (6.2) over those choices.

### Proposition 6.1 (exact serialization criterion)

The selected packet occurrences can be ordered into exactly
\(\tau_H(\mathcal P)\) packet trails whose every band window is clean.
If a trail contains \(r\) packets, its concatenated word has
\((r+1)b\) letters and contains

\[
                         br-H+1                         \tag{6.3}

consecutive core starts with every window through length \(g\) contained.
Consequently, for \(N\) packets and
\(t=\tau_H(\mathcal P)\), the total available core length and the exact
linearization overhead are

\[
 \boxed{M=bN-(H-1)t,\qquad
        \text{word length}=M+(g-1)t=bN+bt.}             \tag{6.4}
\]

Subject to global distinctness of the retained middle targets,
\(N=(1+o(1))W/b\) satisfies the two size conditions of the direct-hole
compiler exactly when

\[
                         t=o(W/b).                       \tag{6.5}

#### Proof

Equations (3.1) and (6.2) give exactly \(t\) linear trails.  Theorem 4.1
makes their contained band windows clean.  A word of \((r+1)b\) letters
has \((r+1)b-g+1=br-H+1\) starts whose length-\(g\) windows are contained,
which proves (6.3).  Summing over trails proves the first identity in
(6.4); adding \((g-1)t\) gives the second.

When \(N=(1+o(1))W/b\), equation (6.4) gives \(M=W-o(W)\) after the
usual vanishing adjustment in packet count precisely when the trail loss
is negligible.  The compiler overhead is \(gt\), so its required
condition is (6.5). \(\square\)

The band-hole condition also has an exact occurrence form.  For a clean
trail family with the \(M\) retained starts in (6.4), let \(a_s(T)\) be
the number of retained length-\(s\) windows equal to
\(T\in{\Omega\choose s}\), and put

\[
 C_s=\sum_{T\in{\Omega\choose s}}(a_s(T)-1)_+,
 \qquad
 h_s=|\{T:a_s(T)=0\}|.                                  \tag{6.6}
\]

### Lemma 6.2 (exact trail collision identity)

For every band rank \(s\),

\[
                 \boxed{h_s={2b\choose s}-M+C_s.}       \tag{6.7}
\]

In particular, the remaining colored requirement is exactly

\[
                 \sum_{s=b-H}^{b+H}h_s=o(W).            \tag{6.8}
\]

The cross-collar occurrences contributing to the upper-rank loads
\(a_{b+q}\) are precisely (4.5); omitting them from the load ledger does
not verify (6.8).

#### Proof

Every retained start supplies exactly one clean rank-\(s\) window, so
\(\sum_Ta_s(T)=M\).  The positive-load targets contribute one unit each,
plus their excess multiplicity:

\[
 M=\sum_Ta_s(T)=\left({2b\choose s}-h_s\right)+C_s.
\]

Rearrangement gives (6.7), and (6.8) is the definition of aggregate band
holes. \(\square\)

The remaining positive theorem is therefore not “find a packet matching,
then orient it.”  It must jointly select internal packet cores and ports so
that all of the following hold:

1. the retained middle starts are globally distinct and total
   \(W-o(W)\);
2. the clean transition system has
   \(\tau_H=o(W/b)\), in particular the port imbalance in (3.2) is
   \(o(W/b)\);
3. the local packet windows together with the explicit cross-collar sets
   (4.5) miss only \(o(W)\) band targets in aggregate.

The first item is the middle packing.  The second is the minimal ordered
circulation/path-cover gate.  The third is the genuine all-offset colored
coverage gate.  Theorem 5.1 removes a local cleanliness obstruction from
item 2, while Theorem 2.1 proves that a disjoint full-support matching
cannot be used as its input without \(\Theta(W/b)\) boundary switches.

## 7. Finite verification

The companion checker

`scratch/verify_gate_cq_ordered_port_cross_join_20260822.py`

uses a normalized legal pair \(A\to B\), exhausts all \(b!\) legal
continuations for \(b=3,4,5,6,7\), and verifies:

1. the equivalence of the triangular criterion (4.2) with brute-force
   cleanliness of every contained window through length \(b+H\);
2. the cross-collar formula and count (4.5)--(4.6);
3. the bijectivity and cleanliness of the canonical matching (5.2); and
4. the continuation lower bound (5.4); and
5. the orbit length and exact third-packet collision in Theorem 5.3.

The checker is confirmatory; all proofs are contained above.
