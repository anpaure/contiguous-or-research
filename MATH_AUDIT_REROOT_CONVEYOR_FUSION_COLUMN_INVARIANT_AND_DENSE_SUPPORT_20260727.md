# Audit of the collar-neutral re-root conveyor and the dense-support reduction

Date: 2026-07-27

Method: pure mathematics.  No computation or finite search is used.

## 0. Verdict

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\]

and assume \(H\ge3\) and \(M\ge8H+1\).  The load-bearing claims of
`MATH_THEOREM_THREE_TOP_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_RECHARGE_20260727.md`
are correct:

1. the matched phase cuts give opposite retained derivatives at every
   complementary length \(0\le h\le2H\);
2. complementation across the three different tops commutes with the
   endpoint telescope;
3. both punctured shores are squarefree and have the same \(3d\) middle
   owners; and
4. one focal top admits \(m-O(H)\) successive root changes, using two
   fresh companion tops at each step.

Consequently, after interleaving the exact two-top boundary rectangle,
one focal top really does expose \(\Theta(m)\) linearly independent
middle rectangle directions with **zero**, not merely \(o(W)\), aggregate
protected-depth collateral.  This is a local theorem.  It uses
\(2\Theta(m)\) one-use helpers and therefore gives only constant average
reuse over all consumed tops.

There is no top-support shortage.  The abstract triangle hypergraph of
three-top re-root packets has

\[
 D=\binom M2(n-M),\qquad \Delta_2=M-1,
 \qquad {\Delta_2\over D}=O(m^{-2}).
\]

Pippenger--Spencer (here the uniformity is the fixed value three) and a
random-relabeling argument give \(\Theta(m)\) near-perfect packet rounds
in which almost every top is assigned \(\Theta(m)\) distinct exchanged
pairs.  Thus neither carrier degree nor top support is the remaining
gate.

The literal source-allocation problem has an exact invariant which was
not recorded previously.  For every rooted position \(j\) and ground
label \(v\), let

\[
 C_{j,v}=\#\{U:\text{the current word on }U\text{ has }v
                    \text{ in rooted position }j\}.
\]

Every three-top re-root packet and every collar-neutral two-top boundary
rectangle preserves the entire matrix \((C_{j,v})\).  Hence a dense
support schedule lifts literally only if all its source and target tables
lie in one fixed column-histogram fibre.  In that fibre a packet is a
coupled pair of opposite alternating six-cycle switches in the
top--label incidence graph.  This is a Latin/contingency-table routing
problem, not a remaining collar calculation.

The exact current boundary is therefore:

\[
\boxed{
\begin{array}{c}
\Theta(m)\text{ useful directions per focal top: proved},\\
\Theta(m)\text{ abstract packet incidences per typical top: proved},\\
\text{one coefficient-one chronology in a fixed }(C_{j,v})
\text{ fibre: open}.
\end{array}}
\]

## 1. Audit of the matched phase cut

Write \(L=2H-1\).  In the notation of the source theorem, the directed
arc from \(B\) to \(A\) in \(\omega\), with the placeholders deleted,
is

\[
             B^+,F_2,\overleftarrow{A^-}.
\]

The directed arc from \(A\) to \(B\) in \(\eta\) is the identical
labelled word.  Its length is at least

\[
             L+3+L=4H+1=(4H-1)+2.
\]

Choose the two deleted blocks of \(4H-1\) starts in these identical
arcs, leaving exactly two starts before the next placeholder.  A deleted
interval of length at most \(2H\) which misses the next placeholder sees
no placeholder.  If it reaches that placeholder, it cannot reach the
other one, and its core context is identical in the two bases.  The
placeholder signs are opposite.  This gives coefficientwise

\[
 c_h^{D_\eta}(\eta;u,v)=-c_h^{D_\omega}(\omega;u,v)
 \qquad(0\le h\le2H).
\]

Subtracting from the complete cyclic anti-collar identity proves the
retained identity.  There is no endpoint or wraparound exception.

## 2. Audit of physical complementation

For \(K\subseteq C\), put

\[
 g_K(u,v)=e_{K\cup\{v\}}-e_{K\cup\{u\}}.
\]

Inside the actual top \(C\cup\{u,v\}\), complementation sends

\[
 g_K(u,v)\longmapsto -g_{C\setminus K}(u,v).
\]

Therefore

\[
 -g_{C\setminus K}(x,a)-g_{C\setminus K}(a,y)
 =-g_{C\setminus K}(x,y).
\]

Thus complementation commutes with the \(x-a-y\) telescope even though
the three complements are taken in different tops.  The common core,
not a fictitious common ambient top, is what makes the identity valid.

## 3. Audit of squarefreeness

An \(H\)-window meets at most one placeholder because the two
placeholder gaps have separation greater than \(2H\).  Owners from two
different packet tops can agree only if both retain their shared outside
label.  Their deleted windows must then contain the two exclusive
outside labels and compare one \(A\)-context with one \(B\)-context.
Those radius-\((H-1)\) palettes lie in disjoint arms.  Hence no cross-top
collision occurs.  Individual cyclic decks are squarefree because the
word is injective and \(M>2H\).  Deleting phase starts cannot create a
collision.  Equality of the middle incidence vectors therefore is
equality of two \(0\)-\(1\) supports of size \(3d\).

## 4. Audit of the linear fresh-helper schedule

With the focal placeholder in rooted position three, all but \(O(H)\)
positions are remote.  There are exactly \(n-M=m-H\) labels outside the
focal top.  Thus one may choose

\[
 t\le \min\{M-O(H),m-H\}=m-O(H)
\]

distinct remote positions and distinct catalysts.  At a step with
current position-three label \(x\), remote label \(y\), and catalyst
\(a\notin U\), the companions are

\[
 U-y+a,\qquad U-x+a.
\]

Two companions from different steps cannot agree: symmetric difference
with \(U\) recovers both the deleted label and the added catalyst.
Within one step the two companions are distinct because \(x\ne y\).
The packet swaps \(x,y\) on the focal word and leaves its first two
positions fixed.  Distinct remote labels therefore give distinct
position-three labels and distinct boundary-swap middle traces.

This proves the advertised local chronology.  It does not prove that a
pre-existing coefficient-one table contains all companion source words.

### The smallest currently certified fused macro

Let \(p\) be the current focal word.  First apply its exact two-top
boundary rectangle, using a companion top \(V\), so that the focal word
becomes \(sp\).  Next apply the three-top re-root packet to \(sp\),
using two helper tops \(V_1,V_2\).  Choose the two outside catalysts
distinct, so that

\[
                         U,V,V_1,V_2
\]

are four distinct tops.  The complete ledger of this open four-top
macro is

\[
 \Delta_h=0\quad(h\ne H),\qquad
 \Delta_H=r,
\]

where \(r\) is the elementary hypersimplex rectangle of the first
step.  The second step changes the focal boundary component and has
zero derivative at every \(h\), including \(H\).  Thus the macro can be
iterated locally with a new middle direction after each re-root.

This is the smallest **certified** fused macro, not a support-minimality
theorem.  Its rectangle shore has the known two forced repeated owner
occurrences, and cross-macro owner compatibility is not supplied by the
trace identity.

## 5. A new exact column-histogram invariant

The matched roots put the two placeholders in the same two rooted
positions in all three words.  Call them \(s\) (the near position,
equal to three) and \(t\) (the remote position).  On the old shore the
labels in position \(s\) on the three tops are

\[
                         (x,a,y),
\]

and on the new shore they are

\[
                         (y,x,a).
\]

At position \(t\) the old and new triples are the opposite two cyclic
orders.  Every other rooted position is unchanged.  Hence every
\(C_{j,v}\) is preserved.

For a two-top boundary rectangle the source position-one labels are
\((a,b)\) and the target labels \((b,a)\); at position two the two
ordered pairs are reversed.  Again every \(C_{j,v}\) is preserved.

### Corollary 5.1

Every chronology generated by these two move families remains in one
fixed column-histogram fibre.  In particular, independently chosen
coordinate relabelings of packet banks cannot simply be concatenated:
their endpoint tables must first be shown to have the same
\((C_{j,v})\).

### Six-cycle interpretation

Fix one packet and one label, say \(x\).  At the two active positions,
\(x\) occupies the rectangle

\[
 (C+xy,s),\ (C+xa,t)
 \quad\longleftrightarrow\quad
 (C+xy,t),\ (C+xa,s).
\]

This is a \(2\times2\) switch.  The three labels \(x,a,y\) couple three
such switches around the alternating six-cycle

\[
 C+xy-x-C+xa-a-C+ay-y-C+xy
\]

of the top--label incidence graph.  Thus the missing global theorem is
an integral routing theorem for coupled six-cycle switches with fixed
row sets and fixed column margins, plus the middle-owner capacity at
every prefix.

## 6. Dense abstract packet support

Let \(\mathcal H_\triangle\) have the rank-\(M\) tops as vertices and
one hyperedge

\[
 \{C+xy,C+xa,C+ay\}
\]

for every \((M-2)\)-set \(C\) and distinct \(x,y,a\notin C\).

### Lemma 6.1

\(\mathcal H_\triangle\) is regular of degree

\[
 D=\binom M2(n-M),
\]

and its maximum pair codegree is \(M-1\).

#### Proof

For a top \(U\), choose its common core by deleting an unordered pair
from \(U\), and then choose the third outside label.  This gives the
degree formula.  Two tops occur together only when they are
Johnson-adjacent.  If their intersection is \(S\) of size \(M-1\),
the common core is \(S\setminus\{z\}\), where \(z\in S\); every
choice of \(z\) gives one third top.  Hence the codegree is \(M-1\).
\(\square\)

Since the uniformity is the fixed value three and
\(\Delta_2/D=O(m^{-2})\), Pippenger--Spencer gives a matching covering
\((1-o(1))N\) tops, where \(N=\binom nM\).

### Theorem 6.2 (linear many abstract rounds)

For every fixed sufficiently small \(c>0\), there are
\(r=\lfloor cm\rfloor\) top-disjoint packet rounds such that the total
number of distinct exchanged-pair incidences over all tops is

\[
                         (1-o(1))rN.
\]

In particular all but \(o(N)\) tops receive \(\Theta(m)\) distinct
abstract re-root directions.

#### Proof

Take one near-perfect matching \(\mathcal M\).  Independently relabel it
by \(r\) uniform coordinate permutations.  Every relabeling is again a
top matching and covers the same number of tops.  Conditional on a
fixed top \(U\) being covered, its exchanged pair \(U\setminus C\) is
uniform on \(\binom U2\), by the transitive action of the stabilizer of
\(U\).

The expected number of covered incidences is
\((1-o(1))rN\).  The expected number of colliding pairs of directions at
one top is at most

\[
                         {\binom r2\over\binom M2}=O(1).
\]

Summing over tops shows that some choice of the \(r\) relabelings has
\((1-o(1))rN-O(N)=(1-o(1))rN\) distinct incidences.  Since no top has
more than \(r\) incidences, all but \(o(N)\) tops have \(\Theta(m)\)
of them after decreasing the implicit constant if necessary.
\(\square\)

Theorem 6.2 is only a support theorem.  It neither chooses one current
word per top shared by consecutive rounds nor enforces coefficient-one
middle ownership.  Corollary 5.1 explains exactly why those facts do not
follow from relabeling.

There is an even stronger static resource statement.  Let

\[
 \mathcal R=\{(U,x):U\in\tbinom{[n]}M,\ x\in U\}
\]

be the top--label incidence set.  A packet on
\(C+xy,C+xa,C+ay\) uses the six resources consisting of its two special
labels at each of its three tops.

### Lemma 6.3 (near-perfect special-label packing)

The resulting 6-uniform hypergraph on \(\mathcal R\) is regular of
degree

\[
                         (M-1)(n-M),
\]

and has maximum pair codegree at most

\[
                         \max\{M-1,n-M\}.
\]

Consequently it has a matching covering \((1-o(1))MN\) top--label
resources.  Equivalently, there is a static packet family in which
almost every top participates in \((1-o(1))M/2\) packets and no label of
one top is used in two packet pairs.

#### Proof

For \((U,x)\), choose the other special label
\(y\in U\setminus\{x\}\) and the catalyst \(a\notin U\).  This gives
the degree.  Two resources on the same top force their two labels to be
the special pair and leave at most \(n-M\) catalysts.  For adjacent
tops \(U=S+u,V=S+v\), a common packet has core
\(S\setminus\{z\}\).  Unless the two resources are the two private
labels, \(z\) is fixed; in the private/private case there are \(M-1\)
choices.  Nonadjacent tops have codegree zero.  The ratio of maximum
codegree to degree is \(O(m^{-1})\), so fixed-uniformity
Pippenger--Spencer applies. \(\square\)

Lemma 6.3 shows that even the supply of distinct label pairs at each top
is not deficient.  It still does not order those pairs into a literal
trajectory.  The local theorem needs the successive special pairs at a
top to form a trail (the current position-three label is one endpoint of
the next pair), while one common chronological order must synchronize
the trails at all three tops of every packet.  That trail-and-precedence
condition is the nonlinear part absent from the resource matching.

### The simultaneous triangular-colouring form of the source gate

Fix one literal word \(p_U\) on every top.  For every
\((M-2)\)-set \(C\), let

\[
 Q_C=[n]\setminus C,
\]

and colour the edge \(xy\in\binom{Q_C}{2}\) by

\[
 \chi_C(xy)=
 \{\operatorname{pos}_{C+xy}(x),
   \operatorname{pos}_{C+xy}(y)\}
 \in\binom{[M]}2.
\]

Three tops \(C+xy,C+xa,C+ay\) can be the source of one matched-root
packet only if the triangle \(xya\) is monochromatic under \(\chi_C\).
The additional \(\omega/\eta\) core-order condition refines this
necessary condition, but cannot weaken it.

For a fixed core, both the number of extension edges and the number of
available colours are of order \(m^2\):

\[
 \binom{|Q_C|}{2}\asymp\binom M2\asymp {m^2\over2}.
\]

Thus the average colour class has constant size.  A random word table
is useless: treating the edge colours as uniform, the expected number
of monochromatic triangles for one core is

\[
 \binom{|Q_C|}{3}\binom M2^{-2}=O(m^{-1}).
\]

In contrast, a dense literal round requires a positive fraction of the
extension edges to lie in monochromatic triangles.  The required object
is therefore an algebraic **simultaneous triangular edge-colouring** of
all the graphs \(K_{Q_C}\), induced consistently by one permutation on
each top.  This is the exact place where the abstract support theorem
loses physical source states.  It also shows that independent or
generic word choices cannot close the gate.

## 7. A bounded-carrier necessity

Let \(\mathcal S\) be the family of tops ever used by a chronology, and
fix a focal top \(U\).  Every new position-three label \(y\) imported
into \(U\) by a three-top packet produces a companion

\[
                         U-y+a\in\mathcal S
\]

for some \(a\notin U\).  Distinct imported labels produce distinct
neighbors, because symmetric difference with \(U\) recovers the deleted
label.  Therefore

\[
 \boxed{
 \#\{\text{distinct imported focal labels}\}
 \le \deg_{J(n,M)[\mathcal S]}(U)\le|\mathcal S|-1.}
\]

Thus no bounded top carrier can yield linear local reuse.  A successful
literal bank must use a Johnson carrier of average degree \(\Omega(m)\),
which Theorem 6.2 supplies abstractly but not yet in one compatible
state fibre.

## 8. Exact implication boundary

Proved here:

1. the full independent audit of the three-top re-root packet;
2. exact zero protected-depth collateral for every local re-root;
3. \(m-O(H)\) distinct local directions with fresh helpers;
4. the column-histogram invariant for both re-root and rectangle moves;
5. a dense abstract top-support schedule with \(\Theta(m)\) distinct
   directions per typical top; and
6. the bounded-carrier degree necessity.

Not proved:

1. a source table in one column-histogram fibre supporting the rounds of
   Theorem 6.2;
2. a chronology ordering the coupled six-cycle switches;
3. coefficient-one middle ownership at every prefix; or
4. the required \(\Theta(W)\) installed rectangle displacement.

Accordingly the conveyor--rectangle fusion is locally and abstractly
dense, and its collateral ledger is already exact.  The remaining gate
is the physical Latin/source allocation, not a hidden trace term.
