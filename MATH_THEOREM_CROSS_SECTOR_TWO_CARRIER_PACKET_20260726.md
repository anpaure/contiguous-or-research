# A minimal cross-sector \(Q_3\) two-carrier packet and its exact tensor capacity

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let

\[
 B=\{a,b,c,d,u,v,w,x\},\qquad
 A=\{a,b,c,d\},\quad U=\{u,v\},\quad W=\{w,x\},
\]

and work in the rank-four Johnson layer \(\binom B4\).  Put

\[
                         \tau=\{a,u,w\}.                 \tag{0.1}
\]

There are two vertex-disjoint literal \(Q_3\)-cells

\[
\begin{aligned}
 C^0&=\{a\}\star\{b,c\}\star\{u,v\}\star\{w,x\},\\
 C^1&=\{u\}\star\{v,x\}\star\{a,b\}\star\{w,d\},
\end{aligned}                                           \tag{0.2}
\]

where \(\star\) means that the singleton core is always selected and
one endpoint is selected independently from each displayed pair.  Both
cells carry the same labelled lower target \(\tau\): the carrier edge in
\(C^0\) has direction \(\{b,c\}\), while the carrier edge in \(C^1\)
has direction \(\{v,x\}\).  The second edge joins two different
macroprofile sectors.  Thus

\[
                         \Omega=C^0\mathbin{\dot\cup}C^1             \tag{0.3}
\]

is an exact two-cell owner packet on sixteen middle owners with carrier
multiplicity two.

This is sharp in three senses.

1. For a fixed rank-three target in an eight-coordinate block, the
   carrier edges of pairwise owner-disjoint \(Q_3\)-cells form a matching
   on its five middle extensions.  Hence there are at most two cells.
2. Every two-edge matching on those five extensions is realizable by two
   disjoint \(Q_3\)-cells.
3. Seven coordinates do not suffice: any two \(Q_3\)-cells in
   \(\binom{[7]}4\) carrying the same target intersect.  Thus eight is
   the least local ground-set size on which multiplicity two occurs.

The fifteen maximum matchings of the five-extension star give a symmetric
packet library.  Every extension is used in exactly twelve packets and
omitted in exactly three.  Its barycentre is exactly the uniform
\(4/5\)-slice of the labelled conditional macroprofile flow; after
aggregating by the three classes \(A,U,W\), the incidences are in the
required ratio \(3:1:1\).

Tensoring \(r\) copies of (0.3) gives an exact partition into \(2^r\)
cells \(Q_{3r}\).  A target touching \(q\) blocks has exactly \(2^q\)
carrier cells, and the corresponding physical \(q\)-matchings are all
different.  If each product cell receives one cyclic direction order,
the optimal reachable fraction \(\rho_{r,q}\) of the natural tensor
target family obeys

\[
 1-(1-p_{r,q})^{2^q}
 \ \leq\ \rho_{r,q}\ \leq\
 \min\{1,2^qp_{r,q}\},
 \qquad
 p_{r,q}={r-q+1\over\binom rq}.                        \tag{0.4}
\]

The lower bound is attained in expectation by independent random orders
and hence by some deterministic choice.  In particular, when
\(2^qp_{r,q}=o(1)\),

\[
               \rho_{r,q}=(1+o(1))\,2^q p_{r,q}.       \tag{0.5}
\]

Thus cross-sector routing produces a genuine and optimal local gain of
\(2^q\) over the unique-carrier packet, but does not remove the fine
window obstruction when \(q=o(r)\):

\[
 \log(2^qp_{r,q})
 =-q\log{r\over q}-(1-\log2)q
   +O\!\left({q^2\over r}+\log r+\log q\right).          \tag{0.6}
\]

Finally, after adjoining spectator axes so that the cell dimension is a
power of two, every one of the \(2^q\) carrier paths of one prescribed
target can simultaneously be put into an isometric long cycle, while the
remaining owners are completed to resolution classes.  This gives a
literal exact owner-cycle packet for one prescribed target.  Formula
(0.4), rather than local existence, is the obstruction to doing this for
all fine targets with one order per cell.

The theorem is local to the mixed-sector packet \(\Omega^r\).  It does
not prove that copies of \(\Omega^r\) tile the entire ambient middle
layer; that is a separate integral packing problem.

## 1. The explicit packet

For a singleton \(c\) and three disjoint two-sets \(P_1,P_2,P_3\), write

\[
 \{c\}\star P_1\star P_2\star P_3
 =\bigl\{\{c,p_1,p_2,p_3\}:p_i\in P_i\bigr\}.          \tag{1.1}
\]

This is a literal isometric \(Q_3\) in the rank-four Johnson graph.  The
two cells in (0.2) therefore each have eight owners.

The edge of \(C^0\) obtained by fixing the \(U\)- and \(W\)-orientations
to \(u,w\) is

\[
                    \{\tau\cup\{b\},\tau\cup\{c\}\}.  \tag{1.2}
\]

Its lower intersection is \(\tau\).  In \(C^1\), fix the other two
active pairs to \(a,w\).  The resulting edge is

\[
                    \{\tau\cup\{v\},\tau\cup\{x\}\}.  \tag{1.3}
\]

Again its lower intersection is \(\tau\).

### Lemma 1.1

The cells \(C^0,C^1\) are vertex-disjoint.

#### Proof

Every member of \(C^0\) contains \(a\), so a hypothetical common member
must choose \(a\), rather than \(b\), in the pair \(\{a,b\}\) of
\(C^1\).  Every member of \(C^1\) contains \(u\), so the same common
member must choose \(u\), rather than \(v\), in the pair \(\{u,v\}\)
of \(C^0\).

After these forced choices, the two remaining coordinates of a member of
\(C^0\) consist of one element of \(\{b,c\}\) and one element of
\(\{w,x\}\).  The two remaining coordinates of the corresponding member
of \(C^1\) consist of one element of \(\{v,x\}\) and one element of
\(\{w,d\}\).  The latter pair of choices contains no element of
\(\{b,c\}\).  Equality is impossible. \(\square\)

The packet really crosses occupancy sectors.  With profiles ordered as
\((|X\cap A|,|X\cap U|,|X\cap W|)\), all eight members of \(C^0\) have
profile \((2,1,1)\), while \(C^1\) has two members in each of

\[
 (1,2,1),\qquad(1,1,2),\qquad(2,2,0),\qquad(2,1,1).    \tag{1.4}
\]

Consequently the complete packet census is

\[
\begin{array}{c|rrrr}
 k&(2,1,1)&(1,2,1)&(1,1,2)&(2,2,0)\\ \hline
 |\Omega_k|&10&2&2&2.
\end{array}                                             \tag{1.5}
\]

More importantly, the two endpoints in (1.3) have profiles \((1,2,1)\)
and \((1,1,2)\).  Thus its carrier edge itself, not merely an auxiliary
collar, crosses source macroprofiles.

## 2. The exact local maximum and the eight-coordinate minimum

Let \(T\) be any rank-three target in an eight-coordinate ground set
\(B\).  Its five rank-four middle extensions are

\[
                      T\cup\{y\},\qquad y\in B\setminus T.          \tag{2.1}
\]

### Lemma 2.1 (extension-matching invariant)

If pairwise vertex-disjoint literal \(Q_3\)-cells carry \(T\), their
carrier directions are pairwise disjoint two-sets in \(B\setminus T\).
In particular, at most two such cells can carry \(T\).

#### Proof

A cell carrying \(T\) contains an edge

\[
             \{T\cup\{y\},T\cup\{z\}\},qquad y\ne z,              \tag{2.2}
\]

and its carrier direction is \(\{y,z\}\).  If two carrier directions
shared \(y\), both cells would contain the same owner \(T\cup\{y\}\),
contrary to vertex-disjointness.  The directions therefore form a
matching on the five-element set \(B\setminus T\), whose matching number
is two. \(\square\)

A fixed \(Q_3\)-cell cannot carry \(T\) in two different directions.
Indeed, its core has size one, and \(T\) consists of that core plus one
chosen endpoint from exactly two active pairs; the third active pair is
then the unique carrier direction.

The upper bound in Lemma 2.1 always has a disjoint-cube realization.

### Lemma 2.2 (every two-edge matching extends)

Write

\[
 T=\{t_1,t_2,t_3\},\qquad
 B\setminus T=\{p_1,p_2,q_1,q_2,r\}.
\]

For the prescribed carrier matching

\[
                         P=\{p_1,p_2\},\qquad Q=\{q_1,q_2\},        \tag{2.3}
\]

the cells

\[
\begin{aligned}
 D_P&=\{t_1\}\star P\star\{t_2,q_1\}\star\{t_3,q_2\},\\
 D_Q&=\{t_2\}\star Q\star\{t_1,p_1\}\star\{t_3,r\}
\end{aligned}                                                       \tag{2.4}
\]

are disjoint and carry \(T\) in directions \(P,Q\), respectively.

#### Proof

The carrier assertion follows by choosing \(t_2,t_3\) in the last two
pairs of \(D_P\), and \(t_1,t_3\) in the last two pairs of \(D_Q\).

A common owner would have to contain \(t_1\), the core of \(D_P\), so it
would choose \(t_1\), not \(p_1\), in \(D_Q\).  It would also have to
contain \(t_2\), the core of \(D_Q\), so it would choose \(t_2\), not
\(q_1\), in \(D_P\).  After these choices, every member of \(D_P\)
still contains one of \(p_1,p_2\), whereas the remaining available
choices in \(D_Q\) lie in \(\{q_1,q_2,t_3,r\}\).  These sets are
disjoint.  Thus no common owner exists. \(\square\)

The next lemma shows that the spare eighth coordinate in (2.4) is
essential.

### Lemma 2.3 (seven-coordinate obstruction)

Two literal \(Q_3\)-cells in \(\binom{[7]}4\) carrying the same
rank-three target necessarily intersect.

#### Proof

Let the common target be \(T\).  If the carrier pairs meet, the common
extension owner from (2.2) already lies in both cells.  We may therefore
suppose that the carrier pairs \(P,Q\) are disjoint.  Since
\(|[7]\setminus T|=4\), they exhaust the complement.

A rank-four \(Q_3\)-cell has a singleton core.  For the cell with carrier
\(P\), its core is one element of \(T\); its other two active pairs match
the other two elements of \(T\) bijectively to the two elements of
\(Q\).  The analogous statement holds with \(P,Q\) reversed for the
second cell.

If the two cores are the same element \(s\), write the other target
elements as \(y,z\).  Choose one of them, say \(y\).  Let \(q_y\) be the
element of \(Q\) paired with \(y\) in the first cell, and let \(p_y\) be
the element of \(P\) paired with \(y\) in the second.  Then

\[
                            \{s,z,p_y,q_y\}                         \tag{2.5}
\]

belongs to both cells.

If the cores are distinct, call them \(s,t\), and let \(z\) be the third
element of \(T\).  Let \(q_z\) be paired with \(z\) in the first cell
and \(p_z\) be paired with \(z\) in the second.  Then

\[
                            \{s,t,p_z,q_z\}                         \tag{2.6}
\]

belongs to both cells.  This proves the assertion in all cases. \(\square\)

A rank-four \(Q_3\) itself requires at least seven ground coordinates.
Lemma 2.3 and construction (0.2) therefore prove that eight is the exact
minimum for two disjoint carriers.  Since every cell has eight owners,
two cells and sixteen owners are also the smallest possible cell packet.

## 3. The symmetric matching library and the macroprofile flow

The five extensions (2.1) form the vertices of \(K_5\).  A maximum
carrier packet is precisely a two-edge matching at the extension level,
and Lemma 2.2 extends every such matching to disjoint physical cells.

There are

\[
             5\cdot3=15                                               \tag{3.1}
\]

two-edge matchings: choose the omitted extension and then one of the
three perfect matchings on the remaining four extensions.  A fixed
extension is omitted in three packets and is used in the remaining
twelve.  A fixed extension edge occurs in three packets.  Equivalently,

\[
 {1\over15}\sum_{M}\mathbf1_{V(M)}={4\over5}\mathbf1_{B\setminus T}.
                                                                    \tag{3.2}
\]

For the concrete target \(\tau=\{a,u,w\}\), its five extensions split
by source profile as

\[
 \begin{array}{c|ccc}
 \text{added coordinate}&b,c,d&v&x\\ \hline
 \text{source profile}&(2,1,1)&(1,2,1)&(1,1,2)\\
 \text{number}&3&1&1.
 \end{array}                                                        \tag{3.3}
\]

This is exactly the labelled conditional slice of the explicit
macroprofile flow.  Indeed, for local target profile
\(\ell=(1,1,1)\), the aggregate inclusion incidences are

\[
\begin{aligned}
 \binom42\binom21\binom21\binom21&=48
       &&\text{from }k=(2,1,1),\\
 \binom41\binom22\binom21\binom21&=16
       &&\text{from }k=(1,2,1),\\
 \binom41\binom21\binom22\binom21&=16
       &&\text{from }k=(1,1,2).
\end{aligned}                                                       \tag{3.4}
\]

The last factor in each line is the relevant
\(\prod_i\binom{k_i}{\ell_i}\) contribution; (3.4) has ratio \(3:1:1\).
Alternatively, there are sixteen labelled targets of profile \(\ell\),
and each has respectively three, one, and one extensions in the displayed
source profiles.

By (3.2), taking every matching packet once uses each labelled extension
exactly twelve times.  Its profile aggregate is therefore

\[
                            36:12:12=3:1:1,                          \tag{3.5}
\]

so the packet library is exactly compatible with the relative weights of
\(F_{k,\ell}\).  The factor \(4/5\) in (3.2) is unavoidable for one
fixed target: two disjoint edges cover four of its five extensions.
This is a local star leave, not by itself a global deficit, because the
omitted owner can be used as a carrier for a different target.

## 4. Tensor multiplicity

Take \(r\) disjoint copies \(\Omega_i=C_i^0\dot\cup C_i^1\) and targets
\(\tau_i\).  Their product has the exact cell partition

\[
 \Omega_1\times\cdots\times\Omega_r
 =\mathop{\dot\bigcup}_{\epsilon\in\{0,1\}^r}
   C_1^{\epsilon_1}\times\cdots\times C_r^{\epsilon_r}.           \tag{4.1}
\]

There are \(2^r\) cells, every cell is \(Q_{3r}\), and both sides of
(4.1) have

\[
                    16^r=2^r8^r                                    \tag{4.2}
\]

owners.

For \(I\in\binom{[r]}q\), define a fine target by taking local target
\(\tau_i\) in blocks \(i\in I\), and an arbitrary owner of \(\Omega_j\)
in blocks \(j\notin I\).  Let \(\mathcal T_{r,q}\) be the union over
all \(I\).  Then

\[
                       |\mathcal T_{r,q}|=\binom rq16^{r-q}.         \tag{4.3}
\]

### Theorem 4.1 (exact carrier multiplicity)

Every target in \(\mathcal T_{r,q}\) has exactly \(2^q\) carrier cells
in (4.1), and their forced direction sets are \(2^q\) distinct physical
\(q\)-matchings.

#### Proof

In an untouched block, the prescribed owner lies in exactly one of the
two disjoint local cells.  In a touched block, either local cell carries
\(\tau_i\), and these are the only two cells in the packet.  The choices
are independent, giving exactly \(2^q\) product cells.

In each touched block the two possible directions are the disjoint
physical pairs corresponding to its two carrier edges.  Directions from
different blocks are disjoint as well.  Distinct binary choices in the
touched blocks therefore give distinct physical \(q\)-matchings. \(\square\)

Lemma 2.1 also gives the matching universal upper bound: in a tensor of
arbitrary eight-coordinate local cell partitions, no fixed rank-three
target can acquire more than \(2^q\) product carrier cells.  Thus (4.1)
attains the largest possible blockwise multiplicity.

## 5. Exact one-order capacity

Give each product cell one cyclic order of its \(3r\) axes.  In each
block, call the unique axis carrying \(\tau_i\) in that local cell the
distinguished axis.  There are \(r\) distinguished and \(2r\)
nondistinguished axes in every product cell.

A cyclic order can have at most \(r-q+1\) length-\(q\) intervals
consisting only of distinguished axes.  Indeed, if the distinguished
positions form cyclic runs of lengths \(s_1,\ldots,s_t\), the number is

\[
                  \sum_j(s_j-q+1)_+\le r-q+1.                       \tag{5.1}
\]

For a favorable touched set \(I\), a fixed product cell carries exactly
\(8^{r-q}\) members of \(\mathcal T_{r,q}\), according to the arbitrary
owner choices in untouched blocks.  Therefore every assignment of orders
reaches at most

\[
                         2^r(r-q+1)8^{r-q}                          \tag{5.2}

targets.  Division by (4.3) proves

\[
                    \rho_{r,q}\le
                    \min\left\{1,{2^q(r-q+1)\over\binom rq}\right\}.
                                                                    \tag{5.3}
\]

This double count permits the same target to be counted from several
carrier cells, so it remains a valid upper bound.

The bound has a matching probabilistic lower estimate.  In every product
cell, place all \(r\) distinguished axes in one run, in an independently
uniform random permutation, and put all nondistinguished axes outside
that run.  For a fixed \(I\in\binom{[r]}q\), the probability that its
axes form one of the \(r-q+1\) intervals is

\[
                       p_{r,q}={r-q+1\over\binom rq}.                \tag{5.4}
\]

Fix a target.  Its \(2^q\) carrier cells are distinct, and their orders
were chosen independently.  Hence its probability of being reached is

\[
                         1-(1-p_{r,q})^{2^q}.                        \tag{5.5}
\]

Linearity of expectation shows that some deterministic assignment of
orders reaches at least this fraction.  This proves (0.4).  If
\(2^qp_{r,q}=o(1)\), expanding (5.5) and comparing with (5.3) gives
(0.5).

For \(q=o(r)\), Stirling's formula in the form

\[
 \log\binom rq
 =q\log{r\over q}+q
  +O\!\left({q^2\over r}+\log q\right)                              \tag{5.6}
\]

gives (0.6).  In particular \(\rho_{r,q}=o(1)\) whenever
\(q\to\infty\) and \(r/q\to\infty\).  At the transparent boundary
\(r=2q\),

\[
 2^qp_{2q,q}
 ={2^q(q+1)\over\binom{2q}q}
 =\Theta(q^{3/2}2^{-q}).                            \tag{5.7}
\]

Thus even the maximum possible local two-carrier multiplicity leaves an
exponential fine-window deficit at \(r=2q\), and a fortiori in the
larger-separation regime relevant to \(q=\Theta(\sqrt m)\).

## 6. Literal long-cycle realization for a prescribed target

The preceding tensor count concerns carrier faces and cyclic direction
orders.  There is nevertheless no local cycle-integrality obstruction for
one prescribed target.

### Lemma 6.1 (cycle completion)

Let \(h\) be a power of two.  Every geodesic cube path using distinct
directions is contained in an isometric \(C_{2h}\), and that cycle is a
member of a resolution class which partitions all vertices of \(Q_h\).

#### Proof

Extend the path's ordered direction list to a permutation \(\pi\) of all
\(h\) cube directions.  Starting from the initial path vertex, the doubled
word \(\pi\pi\) gives an isometric \(C_{2h}\).  The resolvable
power-of-two cube theorem supplies a vertex resolution containing the
standard doubled-permutation cycle.  A translation and a permutation of
coordinates send that standard cycle to the one just constructed and
send its whole resolution class with it. \(\square\)

Append \(d\) spectator axes to (4.1), where

\[
                         h=3r+d
\]

is a power of two.  The packet support is partitioned into \(2^r\)
disjoint \(Q_h\)-cells.  Fix one target in \(\mathcal T_{r,q}\).  In
each of its \(2^q\) carrier cells, order its forced \(q\) directions and
apply Lemma 6.1 to the corresponding geodesic path.  Complete the chosen
cycle to a resolution class in that cell.  Choose arbitrary resolution
classes in all other cells.  Since the cells are owner-disjoint, their
union is an exact owner factor, and the prescribed target has all
\(2^q\) carrier paths on distinct isometric long cycles.

For \(r=1\), one spectator axis gives two disjoint \(Q_4\)-cells.  Each
is partitioned into two isometric \(C_8\)'s, so the smallest explicit
cycle-completed packet has thirty-two owners and four cycles, with the
same labelled target carried in one cycle on each side.

This completion is target-adaptive.  It does not choose one collection of
resolution classes which simultaneously realizes every target in
\(\mathcal T_{r,q}\).  The simultaneous direction-order capacity is
exactly what Sections 4--5 measure, and coherent class selection remains
an additional constraint rather than an automatic consequence of local
completion.
