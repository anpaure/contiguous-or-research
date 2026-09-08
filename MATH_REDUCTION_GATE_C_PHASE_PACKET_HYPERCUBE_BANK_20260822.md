# Gate C: the phase-packet hypercube bank and its ordered selector obstruction

**Status (2026-08-22).**  Every theorem and lemma below is proved.  The
result is a positive local factorization, not a proof of Gate C.  It gives:

1. the exact labelled degree and pair-codegrees of the packet hypergraph;
2. an explicit fixed-\((u,v)\) packet bank whose internal middle vertices
   are disjoint and exhaustive in a natural stratum;
3. exact literal coverage of adjacent lower and structured upper strata;
4. an \(O(b)\)-component Euler chaining at the level of **unordered**
   boundary middle sets; and
5. a rank-\((b-1)\) obstruction showing why the most direct fixed-order
   lift of those Euler tours is not a FIFO chaining theorem.

Thus the phase-packet normal form has substantially more integral structure
than its uniform fractional weighting reveals.  The remaining interface is
precise: the pairings or within-packet coordinate orders must vary so that
the cube-edge factors still partition their middle strata while the ordered
boundary queues form only \(o(W/b)\) trails.  In addition, the analogous
literal coverage has to be established through every offset
\(1\le q\le H\), not only at the adjacent lower rank proved here.

Throughout,

\[
 b\ge3\quad\hbox{is odd},\qquad m=b-1,\qquad
 |\Omega|=2b,\qquad W={2b\choose b}.
\]

## 1. Packets are punctured cyclic-interval blocks

A labelled phase packet is specified by distinct \(u,v\in\Omega\) and
ordered disjoint \(m\)-tuples

\[
 X=(x_1,\ldots,x_m),\qquad Y=(y_1,\ldots,y_m)
\]

whose entries partition \(\Omega\setminus\{u,v\}\).  Its middle vertices
are

\[
 C_0=\{u\}\cup X,
 \qquad
 C_i=\{x_i,\ldots,x_m\}\cup\{y_1,\ldots,y_i\}
 \quad(1\le i\le m),
 \qquad
 C_b=\{u\}\cup Y.                                      \tag{1.1}
\]

Put

\[
 z=(u,x_1,\ldots,x_m,y_1,\ldots,y_m),                  \tag{1.2}
\]

viewed as a directed cyclic order on \(\Omega\setminus\{v\}\), which has
length \(2b-1\).  Then \(C_0,\ldots,C_b\) are exactly the \(b+1\)
consecutive cyclic intervals of length \(b\) beginning at starts
\(0,1,\ldots,b\) in (1.2).  In particular, the packet vertices are
distinct.  This is the punctured-circle form of the normal form in I.11.

There are exactly

\[
 (2b)(2b-1)(2b-2)!=(2b)!                              \tag{1.3}
\]

labelled packets.

### Theorem 1.1 (exact packet degree and pair-codegrees)

Every middle vertex has labelled packet degree

\[
                         D_{\rm pkt}=(b+1)(b!)^2.       \tag{1.4}
\]

If two middle vertices are at Johnson distance \(d\), their labelled
packet codegree is

\[
 \lambda_d=
 \begin{cases}
 \displaystyle
 {2(b+1-d)(b!)^2\over {b\choose d}^2},&1\le d\le b-2,\\[7pt]
 \displaystyle {6(b!)^2\over b^2},&d=b-1,\\[5pt]
 0,&d=b.
 \end{cases}                                           \tag{1.5}
\]

Consequently

\[
 \boxed{
 {\Delta_2\over D_{\rm pkt}}={2\over b(b+1)}.}         \tag{1.6}
\]

#### Proof

Fix a middle set \(C\) and a position \(i\in\{0,\ldots,b\}\).  There are
exactly \((b!)^2\) packet labels having \(C_i=C\).  At \(i=0\), for
example, choose \(u\in C\), order \(C\setminus\{u\}\), choose
\(v\notin C\), and order the other \(b-1\) outside points.  This gives
\(b^2((b-1)!)^2=(b!)^2\).  For \(1\le i\le b-1\), first split \(C\) into
the \(b-i\) surviving \(X\)-entries and the \(i\) entered \(Y\)-entries;
their ordered choices give

\[
 {b\choose i}(b-i)!i!=b!.
\]

The two omitted points and the remaining ordered positions give another
\(b!\).  The case \(i=b\) is symmetric.  Summing over the \(b+1\)
positions proves (1.4).

For positions \(i\ne j\) with \(|i-j|=d<b\), the corresponding packet
vertices are at Johnson distance \(d\).  The sole exception is the endpoint
pair \(\{0,b\}\), which is at distance \(b-1\).  Conditional on
\(C_i=C\), the stabilizer of \(C\) is transitive on the
\({b\choose d}^2\) vertices at distance \(d\).  Hence each ordered
position pair at distance \(d\) contributes
\((b!)^2/{b\choose d}^2\) labels to a fixed ordered pair \((C,C')\).

For \(1\le d\le b-2\), there are \(2(b+1-d)\) ordered position pairs at
separation \(d\).  For \(d=b-1\), the separations \(b-1\) and \(b\)
give respectively four and two ordered position pairs, for a total of six.
No packet contains complementary middle vertices.  This proves (1.5).
The first line is maximal at \(d=1\), where its ratio to (1.4) is
\(2/[b(b+1)]\); the exceptional \(d=b-1\) ratio is
\(6/[(b+1)b^2]\), no larger for \(b\ge3\).  This proves (1.6). \(\square\)

The decay (1.6) is stronger than the \(4/b^2\) fragment bound, but it is
not by itself a matching theorem: the growing-uniformity counterexample in
Appendix C.6 already shows that even
\(b\Delta_2/D\to0\) does not force a fixed-fraction matching in a generic
regular hypergraph.

## 2. A fixed-\((u,v)\) hypercube factor

Fix distinct \(u,v\), and partition
\(R=\Omega\setminus\{u,v\}\) into the ordered coordinate pairs

\[
 P_i=\{a_i^0,a_i^1\},\qquad 1\le i\le m.              \tag{2.1}
\]

Identify a bit vector \(x\in\mathbb F_2^m\) with the transversal

\[
 V(x)=\{a_i^{x_i}:1\le i\le m\}.                     \tag{2.2}
\]

Let \(e_i\) be the \(i\)-th unit vector and
\(p_i=e_1+\cdots+e_i\), with \(p_0=0\).  For every even-weight
\(x\), take the antipodal geodesic

\[
 x, x+p_1, x+p_2,\ldots,x+p_m=\bar x              \tag{2.3}
\]

in \(Q_m\).  Its \(i\)-th cube edge is represented by the
\((m+1)=b\)-set

\[
 E_i(x)=V(x+p_{i-1})\cup V(x+p_i).                   \tag{2.4}
\]

Equivalently, use in (1.1)

\[
 X=(a_1^{x_1},\ldots,a_m^{x_m}),\qquad
 Y=(a_1^{1-x_1},\ldots,a_m^{1-x_m}).                 \tag{2.5}
\]

Then the internal packet vertices \(C_1,\ldots,C_m\) are exactly
\(E_1(x),\ldots,E_m(x)\).

Define the eligible middle stratum

\[
 \mathcal B(P)=\{C\in{R\choose m+1}:
       \text{one }P_i\text{ is doubled and every other }P_j
       \text{ is split}\}.                           \tag{2.6}
\]

Also define the adjacent lower transversal stratum

\[
 \mathcal L(P)=\{V(x):x\in\mathbb F_2^m\}.           \tag{2.7}
\]

### Theorem 2.1 (integral middle factor and exact lower coverage)

The \(2^{m-1}\) packets in (2.3)--(2.5), one for every even \(x\), have
the following exact properties.

1. Their internal middle vertices partition \(\mathcal B(P)\).  In
   particular,
   \[
   |\mathcal B(P)|=m2^{m-1}.                          \tag{2.8}
   \]
2. At internal start \(i\), the designated rank-\((b-1)=m\) token is
   \(V(x+p_{i-1})\).  Every member of \(\mathcal L(P)\) occurs exactly
   \(m/2\) times among these literal lower tokens.
3. The two boundary middle sets of the packet are
   \(\{u\}\cup V(x)\) and \(\{u\}\cup V(\bar x)\).
   Every even transversal occurs exactly twice as a boundary, and every
   antipodal pair supports exactly two packets.
4. For \(1\le i<m\), the designated rank-\((b+1)=m+2\) token at internal
   start \(i\) doubles exactly the consecutive pairs \(P_i,P_{i+1}\),
   splits every other pair, and avoids \(u,v\).  Every target of that form
   occurs exactly twice.  At start \(m\), the upper token contains \(u\),
   doubles \(P_m\), and splits the other pairs; every target of this
   boundary form occurs exactly once.

#### Proof

An element of \(\mathcal B(P)\) is precisely the union of the two
endpoints of one cube edge: the doubled pair specifies the edge direction,
and the choices on all other pairs specify that edge.  For a fixed
direction \(i\), the map

\[
 x\longmapsto\{x+p_{i-1},x+p_i\},\qquad |x|\equiv0\pmod2, \tag{2.9}
\]

is a bijection onto the \(2^{m-1}\) direction-\(i\) edges of \(Q_m\).
Indeed translation by \(p_{i-1}\) takes the even shore bijectively to one
endpoint choice on every direction-\(i\) edge.  Varying \(i\) proves the
partition and (2.8).

The length-\(m\) word window at the same start as \(E_i(x)\) is
\(V(x+p_{i-1})\).  Fix \(z\in\mathbb F_2^m\).  It occurs at index \(i\)
exactly when \(x=z+p_{i-1}\) is even, or equivalently when

\[
 |z|\equiv i-1\pmod2.                                 \tag{2.10}
\]

Among \(i=1,\ldots,m\), precisely \(m/2\) indices have either parity.
This proves the exact lower multiplicity.

Finally, (2.5) gives the two stated boundaries.  Because \(m\) is even,
\(x\) and \(\bar x\) have the same parity.  Hence every even transversal
is the first boundary for its own packet and the last boundary for the
packet indexed by its complement.  The two indices \(x,\bar x\) give the
two packets on an antipodal boundary pair.

For \(i<m\), the length-\((m+2)\) window at internal start \(i\) is

\[
 \{a_1^{1-x_1},\ldots,a_{i-1}^{1-x_{i-1}}\}
 \cup P_i\cup P_{i+1}
 \cup\{a_{i+2}^{x_{i+2}},\ldots,a_m^{x_m}\}.          \tag{2.11}
\]

Fixing this target determines every bit except \(x_i,x_{i+1}\); exactly
two of their four completions make \(x\) even.  At \(i=m\), the upper
window is

\[
 \{u\}\cup P_m\cup
 \{a_1^{1-x_1},\ldots,a_{m-1}^{1-x_{m-1}}\}.          \tag{2.12}
\]

Its split choices determine \(x_1,\ldots,x_{m-1}\), and parity determines
the remaining bit \(x_m\) uniquely.  This proves part 4. \(\square\)

This is an actual integral packet factor, not an annealed count.  Its
limitation is equally exact: for fixed \((u,v)\), every packet boundary
pair is antipodal in \(R\).  Thus the unordered boundary multigraph of the
bank is a disjoint union of doubled edges.  Fixed \((u,v)\) alone cannot
make long packet chains.

The banks also refine the uniform fractional packet weighting into explicit
integral blocks.  Let \(\mathfrak P(R)\) be the set of perfect pairings of
\(R\), and apply Theorem 2.1 to every pairing, using any fixed ordering of
its pairs.

### Corollary 2.2 (exact fractional decomposition by integral banks)

Every \(C\in{R\choose m+1}\) belongs to \(\mathcal B(P)\) for exactly

\[
\rho_m={m+1\choose2}(m-1)!={(m+1)!\over2}             \tag{2.13}
\]

pairings \(P\in\mathfrak P(R)\).  Consequently, assigning weight
\(1/\rho_m\) to every integral bank gives exact middle load one on the
entire layer \({R\choose m+1}\).  On the adjacent layer
\({R\choose m}\), the same weighting gives every target exact load

\[
                         {m\over m+1}.                 \tag{2.14}
\]

#### Proof

For a fixed \((m+1)\)-set \(C\), choose its unique doubled pair in
\({m+1\choose2}\) ways and biject the remaining \(m-1\) points of \(C\)
to the \(m-1\) points of \(R\setminus C\).  This gives (2.13), and
Theorem 2.1(1) gives middle load one after normalization.

A fixed \(m\)-set is a transversal of exactly \(m!\) perfect pairings of
\(R\).  Theorem 2.1(2) gives it multiplicity \(m/2\) in each corresponding
bank.  Hence its normalized load is

\[
 {m!\,(m/2)\over (m+1)!/2}={m\over m+1},
\]

proving (2.14). \(\square\)

Thus there is an exact fractional middle factor which is an average of
integral cube-edge banks, rather than merely an average of individual
packets.  Rounding can therefore be sought at the bank/transition
interface.  The next section shows that one fixed global pairing has
excellent set-level chaining, while Section 4 identifies the ordered
obstruction.

## 3. A global fixed-pairing stratum and unordered Euler chaining

Now partition all of \(\Omega\) into

\[
 P_j=\{a_j^0,a_j^1\},\qquad 1\le j\le b.              \tag{3.1}
\]

For each \(j\), put \(u=a_j^0\), \(v=a_j^1\), and apply Theorem 2.1 to
the other \(m=b-1\) pairs.  Let \(\mathcal S_1(P)\) be the middle
stratum consisting of the \(b\)-sets having exactly one empty pair,
exactly one doubled pair, and all other pairs split.

### Corollary 3.1 (exact defect-one factor)

The internal middle vertices of the \(b2^{b-2}\) resulting packets
partition \(\mathcal S_1(P)\), whose size is

\[
                     |\mathcal S_1(P)|
                     =b(b-1)2^{b-2}.                  \tag{3.2}
\]

Their internal rank-\((b-1)\) tokens cover every \((b-1)\)-set having
one empty pair and all other pairs split exactly \((b-1)/2\) times.

#### Proof

Every member of \(\mathcal S_1(P)\) has a unique empty pair \(P_j\), so
it belongs to exactly the bank indexed by \(j\).  Theorem 2.1 partitions
that bank's eligible stratum.  The same uniqueness of the empty pair and
Theorem 2.1(2) prove the lower-token assertion. \(\square\)

There is also a favorable unordered chaining fact.  Encode a transversal
by \(x\in\mathbb F_2^b\).  All boundaries used above have even weight,
and the bank with special pair \(j\) supplies two parallel packet edges

\[
 x\longleftrightarrow T_jx,qquad
 (T_jx)_j=x_j=0,qquad
 (T_jx)_k=1-x_k\ (k\ne j).                            \tag{3.3}
\]

### Proposition 3.2 (only \(O(b)\) unordered boundary components)

The underlying simple graph in (3.3) has one connected component for each
unordered weight pair

\[
                         \{s,b-1-s\},qquad
                         s\in\{0,2,\ldots,b-1\}.       \tag{3.4}
\]

In particular it has \(O(b)\) components.  Since every edge occurs twice,
the packet boundary multigraph is Eulerian in every component.

#### Proof

Regard \(x\) as an even subset \(S\subseteq[b]\).  An edge labelled
\(j\notin S\) sends it to

\[
                         T_j(S)=[b]\setminus(S\cup\{j\}), \tag{3.5}
\]

whose size is \(b-1-|S|\).  Thus (3.4) is invariant.  If
\(j\notin S\) and \(k\in S\), then \(k\notin T_j(S)\) and

\[
                         T_kT_j(S)=(S\setminus\{k\})\cup\{j\}. \tag{3.6}
\]

Two moves therefore perform any single exchange, so all sets of a fixed
even size are connected; one further move joins the two sizes in (3.4).
This proves the component description.  Doubling every edge makes all
degrees even. \(\square\)

At the level of boundary **sets**, Proposition 3.2 would concatenate the
entire defect-one factor into only \(O(b)\) closed trails.  Its seam would
be negligible.  The next section explains why this is not yet a physical
FIFO concatenation.

## 4. The fixed-order FIFO selector obstruction

An ordered packet starts with the queue

\[
 (u,x_1,\ldots,x_m)
\]

and ends with

\[
 (y_1,\ldots,y_m,u).                                  \tag{4.1}
\]

Thus equality of boundary **sets** does not suffice: consecutive packets
must have identical ordered boundary queues.  Consider the most direct
attempt to lift Section 3.  Fix one cyclic order of the \(b\) coordinate
pairs.  At every packet, take the current special pair first and toggle the
other pairs in the inherited cyclic order.  One packet rotates the pair
order by one place and flips every nonspecial bit.  After \(b\) packets the
ordered pair list and every bit return to their starting values, because
each coordinate was flipped \(b-1\) times.  Hence these coherent objects
are \(b\)-packet ordered cycles.

To partition the eligible cube edges for a fixed special pair, the start
vectors on the other \(m\) pairs must be one parity shore of \(Q_m\), as
in (2.9).  The shore is allowed to depend on the special pair.

### Proposition 4.1 (no simultaneous fixed-order shore selector)

For \(b\ge5\), no collection of \(2^{b-2}\) fixed-order coherent
\(b\)-packet cycles can induce a cube-edge decomposition at every one of
the \(b\) special-pair stages.

#### Proof

Let \(x\in\mathbb F_2^b\) be the initial transversal bits of a coherent
cycle.  Before the stage whose special coordinate is \(j\), previous
packets have added a fixed vector depending only on the stage.  Therefore
the parity of the other \(b-1\) start bits has the form

\[
                         \ell_j(x)+c_j,qquad
 \ell_j(x)=\sum_{k\ne j}x_k,                           \tag{4.2}
\]

where \(c_j\) is a fixed constant.  If a family \(S\) of initial states
uses one parity shore at stage \(j\), then \(\ell_j\) is constant on
\(S\).

The \(b\) linear forms \(\ell_j\) have rank \(b-1\) over
\(\mathbb F_2\).  Indeed
\(\ell_i+\ell_j=x_i+x_j\), and these differences span the even-weight
dual subspace of dimension \(b-1\); on the other hand
\(\sum_j\ell_j=(b-1)\sum_kx_k=0\) because \(b-1\) is even.  Hence a
common affine fibre of all \(\ell_j\) contains at most
\(2^{b-(b-1)}=2\) points.

A cube-edge decomposition at one stage needs all \(2^{m-1}=2^{b-2}\)
antipodal geodesics.  Each coherent cycle supplies one such packet at that
stage, so \(|S|=2^{b-2}>2\) for \(b\ge5\), a contradiction. \(\square\)

There is a second, quantitative form of the same fixed-order obstruction.
For a directed cyclic order \(\rho\) of the \(b\) coordinate pairs and an
initial transversal \(x\in\mathbb F_2^b\), let \(\mathcal C_\rho(x)\)
denote the resulting coherent \(b\)-packet cycle.  It contains exactly one
defect-one target for every ordered pair \((j,i)\) of distinct empty and
doubled coordinates.  The split bits of that target are

\[
             (x+f_{\rho,j,i})\big|_{[b]\setminus\{j,i\}},      \tag{4.3}
\]

where the fixed vector \(f_{\rho,j,i}\) records the flips performed before
that target.

### Proposition 4.2 (fixed-order cycles are an error-correcting code)

For one fixed \(\rho\), two coherent cycles
\(\mathcal C_\rho(x)\) and \(\mathcal C_\rho(x')\) are internally
middle-disjoint if and only if

\[
                              d_H(x,x')\ge3.            \tag{4.4}
\]

Consequently a matching of fixed-\(\rho\) cycles has at most

\[
                              {2^b\over b+1}            \tag{4.5}
\]

members and covers at most a \(4/(b+1)=o(1)\) fraction of the defect-one
stratum.

#### Proof

For a fixed ordered pair \((j,i)\), the constants in (4.3) cancel between
the two cycles.  They share that target exactly when \(x+x'\) vanishes
outside \(\{j,i\}\).  Such a pair \(j\ne i\) exists exactly when
\(d_H(x,x')\le2\), proving (4.4).

Thus the initial states of pairwise disjoint cycles form a binary code of
minimum distance at least three.  The radius-one Hamming balls about its
codewords are disjoint; each contains \(b+1\) vectors.  This proves (4.5).
An exact defect-one factor would require \(2^{b-2}\) coherent cycles, so
the covered fraction from one \(\rho\) is at most
\((2^b/(b+1))/2^{b-2}=4/(b+1)\). \(\square\)

Proposition 4.2 makes mixing cyclic orders quantitatively unavoidable: a
bounded menu still covers only \(o(1)\) of this stratum, and a near-factor
requires packet cycles from \(\Omega(b)\) distinct cyclic orders.

This obstruction is deliberately narrow.  It rules out only the common
fixed-pairing, fixed-cyclic-order selector.  It does **not** rule out:

* changing the coordinate pairing between packets;
* using different antipodal path decompositions in different banks;
* a switching construction which joins ordered queues while changing a
  vanishing fraction of the internal cube-edge factor; or
* a direct long-fragment matching which uses the packet bank only as an
  absorber.

## 5. Exact consequence for the live Gate-C route

The positive part supplies an integral, literal three-rank building block:

\[
 \boxed{
 \begin{array}{c}
 \text{defect-one middle targets are covered exactly once,}\\
 \text{and the associated lower targets are all covered exactly }(b-1)/2
 \text{ times,}\\
 \text{while the consecutive-double upper classes have multiplicity two}
 \text{ (and the boundary upper class multiplicity one).}
 \end{array}}                                             \tag{5.1}
\]

The unordered boundary graph already has only \(O(b)\) Euler components.
Thus neither middle integrality nor set-level chaining is the missing fact
for this stratum.  What remains is an **ordered boundary lift** that avoids
Proposition 4.1, together with corresponding literal offset-image coverage
for every \(1\le q\le H\).  Any successful lift may alter
\(o(|\mathcal S_1(P)|)\) packet interiors or boundary occurrences without
affecting coefficient one, because one repeated boundary per packet costs
only

\[
 {b2^{b-2}\over b(b-1)2^{b-2}}={1\over b-1}            \tag{5.2}
\]

relative to the exact internal middle mass.  This identifies a concrete
switching scale: an \(o(1)\) fraction of each cube-edge bank is available
for ordered-queue repair, whereas a separate \(\Theta(b)\)-letter reset per
packet is not.

## 6. Finite audit

The companion checker

`scratch/verify_gate_c_phase_packet_hypercube_bank_20260822.py`

exhaustively enumerates every labelled packet for \(b=3,5\) and verifies
(1.4)--(1.6).  For \(b=3,5,7,9\) it verifies the cube-edge partition, the
exact adjacent lower and upper multiplicities, the doubled antipodal
endpoint ledger, the component classification (3.4), the rank calculation
in Proposition 4.1, and the distance-three equivalence in Proposition 4.2.
The checker is confirmatory; all proofs are contained above.
