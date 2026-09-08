# K19/K21 fixed-core normal splits and the all-\(k\) orbit-transport gate

**Date:** 2026-08-02  
**Status:** unconditional optimal-depth static chainization at K19 and K21,
an unconditional fixed-core transport theorem, and an unconditional
all-\(k\) polynomial-size capacity/Hall reduction. An all-\(k\)
depth-\(d+O(1)\) anchored factor and every literal serialization statement
remain explicitly **unproved**.

## 0. Main verdict

At K19, fix a triple \(H\subset[19]\) and put

\[
 Y=\left\{S\in{[19]\choose7}:H\subseteq S\right\},
 \qquad
 X={[19]\choose7}\setminus Y.                         \tag{0.1}
\]

Then

\[
 |Y|={16\choose4}=1\,820,\qquad |X|=48\,568,          \tag{0.2}
\]

so \(X\) lies in the certified window
\(33\,592\le |X|\le48\,583\). The blocks

\[
\begin{aligned}
 P_0&=\bigcup_{s=1}^{6}{[19]\choose s}\ \cup X,\\
 P_1&=Y\ \cup {[19]\choose8},\\
 P_2&={[19]\choose9}
\end{aligned}                                         \tag{0.3}
\]

admit uniform containment couplings

\[
                         P_0\longrightarrow P_1
                         \longrightarrow P_2.          \tag{0.4}
\]

For ordered disjoint blocks \(E_0,\ldots,E_m\), write

\[
 \mathsf Q(E_0,\ldots,E_m)
\]

for the auxiliary layered poset in which every \(E_i\) is an antichain and,
for \(i<j\), an element \(S\in E_i\) precedes \(T\in E_j\) exactly when
\(S\subset T\). Thus all within-block Boolean comparabilities are deleted,
while every cross-block containment, including the transitive
\(E_i\to E_j\) relations for \(j>i+1\), is retained. Every chain in
\(\mathsf Q(E_0,\ldots,E_m)\) is a Boolean inclusion chain and has size at
most \(m+1\). All compressed-poset LYM and Dilworth statements below refer
to this auxiliary poset. In particular, the two couplings in (0.4) are
supported on relations of \(\mathsf Q(P_0,P_1,P_2)\).

Therefore the K19 strict lower ideal partitions into exactly
\(W={19\choose9}=92\,378\) inclusion chains of size at most three,
each containing one rank-nine set and attaching to a distinct rank-ten
owner. This closes the K19 normalized-Hall split clause at the exact
deadline depth \(d(19)=3\).

The same orbit mechanism also closes K21. Together with the earlier
whole-rank compressions, every odd case with \(d(k)=3\), namely

\[
                         k=11,13,15,17,19,21,          \tag{0.5}
\]

now has an unconditional static anchored factor of depth three.

Neither conclusion is a contiguous-OR word.

## 1. Exact fixed-core orbit transport

Let \([n]=H\dot\cup K\), where \(|H|=h\). For admissible \((s,i)\), define

\[
 \mathcal O_{s,i}
 =\{S\subseteq[n]:|S|=s,\ |S\cap H|=i\},
 \qquad
 q_{s,i}=|\mathcal O_{s,i}|
 ={h\choose i}{n-h\choose s-i}.                       \tag{1.1}
\]

### Lemma 1.1 (biregular orbit incidence)

For \(s<t\), the containment graph
\(\mathcal O_{s,i}\to\mathcal O_{t,j}\) is nonempty exactly when

\[
                         i\le j,\qquad s-i\le t-j.     \tag{1.2}
\]

When nonempty, its left and right degrees are

\[
\begin{aligned}
 d^+_{(s,i),(t,j)}
   &={h-i\choose j-i}
     {n-h-s+i\choose t-j-s+i},\\
 d^-_{(s,i),(t,j)}
   &={j\choose i}{t-j\choose s-i}.
\end{aligned}                                         \tag{1.3}
\]

In particular the graph is biregular.

#### Proof

The two inequalities in (1.2) are exactly the extension conditions inside
\(H\) and \(K\). Formula (1.3) chooses the new elements on the two shores,
or reverses the count from a fixed target. Both products count the same
incidences:

\[
 q_{s,i}d^+_{(s,i),(t,j)}
 =q_{t,j}d^-_{(s,i),(t,j)}.                           \tag{1.4}
\]

\(\square\)

### Theorem 1.2 (orbit transport iff uniform coupling)

Let \(P,Q\) be disjoint unions of fixed-core orbits. A
containment-supported coupling uniform on \(P\) and uniform on \(Q\) exists
if and only if there are nonnegative amounts \(F_{uv}\), on compatible
orbit pairs \(u\to v\), with

\[
 \sum_vF_{uv}=|u|\,|Q|,
 \qquad
 \sum_uF_{uv}=|v|\,|P|.                               \tag{1.5}
\]

Thus all normalized-Hall cuts collapse exactly to one finite
transportation max-flow on the type graph.

#### Proof

Average any uniform coupling over
\(\mathfrak S_H\times\mathfrak S_K\) and collapse its mass to orbit pairs;
this proves necessity.

Conversely, let \(E_{uv}\) be the number of literal incidences between
compatible orbits. Put equal probability

\[
                         {F_{uv}\over |P||Q|E_{uv}}    \tag{1.6}
\]

on every such incidence. Biregularity and (1.5) give marginal \(1/|P|\)
at every source and \(1/|Q|\) at every target. \(\square\)

This is an equivalence, not a fractional relaxation of normalized Hall.

## 2. K19 orbit census

Use \(|H|=3\), \(|K|=16\). The K19 blocks in (0.3) have types

\[
\begin{aligned}
 P_0:\quad&
 1\le s\le6,\ 0\le i\le3,
 \quad\text{and}\quad s=7,\ i=0,1,2,\\
 P_1:\quad&
 (7,3),\quad (8,0),(8,1),(8,2),(8,3),\\
 P_2:\quad&
 (9,0),(9,1),(9,2),(9,3),
\end{aligned}                                         \tag{2.1}
\]

with zero-size types omitted. Their exact sizes are

\[
 |P_0|=92\,363=W-15,\qquad
 |P_1|=77\,402,\qquad
 |P_2|=92\,378=W.                                     \tag{2.2}
\]

Write

\[
 a=92\,363,\qquad b=77\,402,\qquad c=92\,378,         \tag{2.3}
\]

and name

\[
 Y_0=\mathcal O_{7,3},\qquad
 U_i=\mathcal O_{8,i},\qquad
 V_i=\mathcal O_{9,i}.                                \tag{2.4}
\]

## 3. K19 certificate for \(P_0\to P_1\)

Scale all amounts by \(ab\). A source orbit \(\mathcal O_{s,i}\) must emit
\(bq_{s,i}\), and a target orbit must receive \(aq_{t,j}\).

Use these rules.

1. Every source type with \(s\le3\) sends all \(bq_{s,i}\) to \(Y_0\).
2. Type \((4,0)\) sends

   \[
   R=78\,391\,742                                     \tag{3.1}
   \]

   to \(Y_0\), and its remaining \(62\,479\,898\) to \(U_0\).
3. Every other type \((s,i)\), \(4\le s\le6\), sends all
   \(bq_{s,i}\) to \(U_i\).
4. For \(i=0,1,2\), type \((7,i)\) sends \(z_i\) to \(U_i\) and its
   remainder to \(U_{i+1}\), where

   \[
   (z_0,z_1,z_2)
   =(168\,304\,760,\ 885\,797\,952,\ 664\,706\,016).  \tag{3.2}
   \]

Every route satisfies (1.2), and every amount is nonnegative. The
exceptional value is forced by

\[
 R=a{16\choose4}
      -b\sum_{s=1}^{3}{19\choose s}
  =a(1\,820)-b(1\,159).                               \tag{3.3}
\]

The row sums are correct by construction. Direct addition gives target
column sums

\[
\begin{array}{c|rrrrr}
\text{target}&Y_0&U_0&U_1&U_2&U_3\\ \hline
\text{incoming}&
168\,100\,660&
1\,188\,711\,810&
3\,169\,898\,160&
2\,218\,928\,712&
403\,441\,584
\end{array}                                           \tag{3.4}
\]

which equal

\[
 a(q_{7,3},q_{8,0},q_{8,1},q_{8,2},q_{8,3}).         \tag{3.5}
\]

Theorem 1.2 proves the uniform coupling \(P_0\to P_1\).

## 4. K19 certificate for \(P_1\to P_2\)

Scale by \(bc\). Send \(Y_0\) entirely to \(V_3\), with amount
\(168\,127\,960\). For \(U_i\), use

\[
\begin{array}{c|rr}
\text{source}&U_i\to V_i&U_i\to V_{i+1}\\ \hline
U_0&885\,478\,880&303\,425\,980\\
U_1&2\,685\,065\,240&485\,347\,720\\
U_2&2\,171\,088\,920&48\,200\,152\\
U_3&403\,507\,104&0
\end{array}                                           \tag{4.1}
\]

All routes satisfy (1.2). The row sums are \(cq_{7,3}\) or \(cq_{8,i}\),
and the target column sums are

\[
 (885\,478\,880,\ 2\,988\,491\,220,\
   2\,656\,436\,640,\ 619\,835\,216)
 =b(q_{9,0},q_{9,1},q_{9,2},q_{9,3}).                 \tag{4.2}
\]

Theorem 1.2 proves the uniform coupling \(P_1\to P_2\).

## 5. K19 depth-three chainization

### Theorem 5.1 (K19 fixed-triple factor)

The K19 strict lower ideal has a partition into \(92\,378\) inclusion
chains, each of size at most three and each containing one rank-nine set.
The chains attach bijectively to distinct rank-ten owners.

#### Proof

Glue the two couplings through their common uniform \(P_1\) marginal. This
gives a random chain \(Z_0\subset Z_1\subset Z_2\), uniform on every block.
All three comparisons are relations of the auxiliary poset
\(\mathsf Q(P_0,P_1,P_2)\). Hence every antichain \(D\) in that poset
satisfies

\[
 { |D\cap P_0|\over92\,363}
 +{ |D\cap P_1|\over77\,402}
 +{ |D\cap P_2|\over92\,378}\le1.                    \tag{5.1}
\]

Every block has size at most \(W\), while \(P_2\) has size \(W\), so the
width is exactly \(W\). Dilworth gives \(W\) chains. The \(W\) rank-nine
elements force one into every chain. Because each layer is an antichain in
\(\mathsf Q(P_0,P_1,P_2)\), every such chain has size at most three. The
regular equal-shore rank9--rank10 containment
graph has a perfect matching, which attaches the owners. \(\square\)

Since \(|P_0|>|P_1|\), the first coupling is not an injection. It is used
only for LYM and width. Dilworth supplies the integral chain partition and
may use comparabilities that skip \(P_1\).

## 6. K21 and the complete odd depth-three phase

For K21, fix \(H\subset[21]\) with \(|H|=8\), and put

\[
 Y=\left\{S\in{[21]\choose8}:|S\cap H|=4\right\},
 \qquad |Y|={8\choose4}{13\choose4}=50\,050.          \tag{6.1}
\]

The required upward-shift window is

\[
                         49\,213\le |Y|\le58\,786.     \tag{6.2}
\]

A single principal \(t\)-star cannot meet it: for \(t=1,\ldots,8\), its
possible sizes are

\[
 77\,520,\ 27\,132,\ 8\,568,\ 2\,380,\ 560,\ 105,\ 14,\ 1.     \tag{6.3}
\]

Thus K21 is an exact counterexample to extending the K19 repair using only
one principal star. The single intersection orbit in (6.1) is a genuinely
broader fixed-core move.

Let

\[
\begin{aligned}
 A&=\bigcup_{s=1}^{7}{[21]\choose s}
      \ \cup\left({[21]\choose8}\setminus Y\right),\\
 B&=Y\cup{[21]\choose9},\\
 C&={[21]\choose10}.
\end{aligned}                                         \tag{6.4}
\]

Then

\[
 |A|=351\,879,\qquad |B|=343\,980,\qquad
 |C|=352\,716=W.                                      \tag{6.5}
\]

### Theorem 6.1 (K21 single-orbit factor)

There are uniform containment couplings \(A\to B\to C\). Consequently the
K21 strict lower ideal has an anchored chain factor of depth three.

#### Proof

Use the \(\mathfrak S_8\times\mathfrak S_{13}\) orbit types. Write
\(y=(8,4)\), \(q_i=(9,i)\), \(c_i=(10,i)\), and order the \(B\)-types as

\[
 q_0,q_1,q_2,q_3,q_4,y,q_5,q_6,q_7,q_8.              \tag{6.6}
\]

Every \(A\)-type has an interval neighborhood in this order. Indeed, type
\((s,i)\) reaches rank-nine types

\[
 q_j,\qquad i\le j\le\min(8,i+9-s),                   \tag{6.7}
\]

and it reaches \(y\) exactly when \(i\le4\) and \(s-i\le4\), precisely
when the interval (6.7) straddles the insertion point. The sole same-rank
exception would be \((8,4)\), which was removed from \(A\).

Give source type \(u\) supply \(|u||B|\) and target type \(v\) demand
\(|v||A|\). In an interval-neighborhood network, max-flow is feasible iff
for every target interval \(I\), the supply of source intervals wholly
contained in \(I\) is at most the demand of \(I\): arbitrary target subsets
split into interval components.

After division by the common factor \(39\), the minimum slack among
intervals of lengths \(1,\ldots,10\) is

\[
\begin{split}
&(108473,\ 4750697,\ 54282865,\ 228843545,\ 449490965,\\
&\hspace{12mm}561723932,\ 251016788,\ 87408692,\
31370107,\ 0).
\end{split}                                           \tag{6.8}
\]

Thus every proper cut is strict and the full interval is tight, proving
the \(A\to B\) type transport.

For \(B\to C\), type \(q_i\) sees \(c_i,c_{i+1}\), while \(y\) sees
\(c_4,c_5,c_6\). Again all neighborhoods are intervals. After division by
\(14196\), the minimum slacks by interval length are

\[
 (1567,\ 41503,\ 327635,\ 521752,\ 285516,\
   141988,\ 24772,\ 10835,\ 0).                      \tag{6.9}
\]

Theorem 1.2 lifts both transports to literal uniform couplings. Both are
relations of the auxiliary poset \(\mathsf Q(A,B,C)\), which deletes all
within-block comparabilities and retains every cross-block containment.
LYM and Dilworth in this three-layer poset now give \(W\) chains; each has
size at most three and contains one rank-ten set. These are also Boolean
inclusion chains. The regular rank10--rank11 graph attaches owners.
\(\square\)

Exact evaluation and monotonicity of

\[
 {2^{k-1}-1\over {k\choose(k-1)/2}}
\]

over odd \(k\) show that \(d(k)=3\) precisely for
\(k=11,13,15,17,19,21\). The first four cases have separated complete-rank
three-block systems, while Theorems 5.1 and 6.1 close the last two.

## 7. What generalizes unconditionally at all \(k\)

### Theorem 7.1 (balanced complete rank-quotient factor)

Put

\[
 D=\left\lceil{\Lambda\over W}\right\rceil\le d+1.
\]

If every target is replaced only by a token bearing its rank, the strict
lower inventory partitions into \(W\) strictly increasing rank paths of
length at most \(D\).

#### Proof

Concatenate the tokens in increasing rank order and distribute consecutive
tokens cyclically among \(W\) columns. Since \({k\choose s}\le W\), a column
never receives rank \(s\) twice. Every column receives
\(\lfloor\Lambda/W\rfloor\) or \(D\) tokens. Sorting each column by its
distinct rank labels gives the paths. \(\square\)

Thus scalar rank sizes and ordinary injective rank-Hall do not obstruct
depth \(d+1\). This quotient theorem does not give normalized uniform
couplings between right-aligned rows. At \(k=6\), the far row is one
rank-one token while the next row has five rank-one and fifteen rank-two
tokens. A uniform strict coupling would need target rank at least two with
probability one, but the target probability is \(15/20\).

### Theorem 7.2 (polynomial fixed-core capacity reduction)

Fix \(h\) coordinates pointwise. The remaining symmetric group has orbits

\[
 \mathcal O_{A,j}
 =\{S:S\cap H=A,\ |S\setminus H|=j\},
 \qquad |\mathcal O_{A,j}|={k-h\choose j}.             \tag{7.1}
\]

Let

\[
 M_h={k-h\choose\lfloor(k-h)/2\rfloor},
 \qquad T_d={d+1\choose2}.                             \tag{7.2}
\]

If

\[
                         (d+1)M_h\le W-T_d,            \tag{7.3}
\]

then next-fit packing of the strict-lower orbits, ordered by total rank,
uses at most \(d+1\) blocks of size at most \(W\).

#### Proof

Every orbit has size at most \(M_h\), and every closed block has load
greater than \(W-M_h\). If there were at least \(d+2\) blocks, the first
\(d+1\) closed blocks would contain more than

\[
 (d+1)(W-M_h)\ge dW+T_d\ge\Lambda,
\]

a contradiction. \(\square\)

Taking

\[
 h=\left\lceil\log_2(8(d+1))\right\rceil             \tag{7.4}
\]

gives

\[
 {M_h\over W}
 =2^{-h}\sqrt{{k\over k-h}}\,(1+o(1)),                \tag{7.5}
\]

so (7.3) holds for all sufficiently large \(k\). The number of orbit types
is

\[
                         O(2^hk)=O(k^{3/2}).           \tag{7.6}
\]

Thus actual targets have an explicit \(d+1\)-block capacity chronology
with only polynomially many fixed-core types. For the finitely many
exceptions, take \(h=k\): all orbits are singletons and next-fit uses
\(D=\lceil\Lambda/W\rceil\le d+1\) blocks. Finite exceptions are absorbed
in the asymptotic constant in (7.6). This is not yet a chain factor.

### Theorem 7.3 (exact global orbit-Hall lift)

For any fixed-core orbit chronology \(\tau\), existence of an anchored
chain factor following strictly increasing \(\tau\)-times is equivalent to
one finite product-order type max-flow.

#### Proof

Make a bipartite graph with a left copy of every target and right copies of
all targets and owners. A left target may use a right target only if it is a
strict subset at a later \(\tau\)-time; it may also use a containing owner.
A matching saturating all left targets forms vertex-disjoint increasing
paths ending at distinct owners, hence the desired factor.

Average such a matching over \(\mathfrak S_{k-h}\). This gives a type flow
with supply \(|\mathcal O_{A,j}|\), right capacities
\(|\mathcal O_{B,\ell}|\), and an arc exactly when

\[
 \tau(A,j)<\tau(B,\ell),\qquad A\subseteq B,\qquad j\le\ell,   \tag{7.7}
\]

or when the target type is an owner type. This proves necessity.

Conversely, every allowed orbit-incidence graph is biregular. Spread a
feasible type flow uniformly over its literal incidences to obtain a
fractional matching saturating the left shore. Bipartite matching
integrality gives an integral saturating matching. \(\square\)

This global flow is strictly weaker than demanding normalized uniform
couplings at every adjacent block: paths may skip times, and adjacent block
sizes need not be monotone.

**UNPROVED all-\(k\) Hall clause.** For some absolute \(C\), one can choose
the within-rank orbit order, controlled underfill, or an adaptive orbit
refinement so that a fixed-core chronology with at most \(d+C\) blocks has
a saturating global type flow for every \(k\).

The capacity proof in Theorem 7.2 is independent of the within-rank order;
it does not specify a Hall-valid order. Deterministic ascending-mask,
serpentine, and monotone diagonal orders have since been refuted by exact
chronological-upset Hall cuts. See
`MATH_THEOREM_CHRONOLOGICAL_UPSET_HALL_COMPRESSION_AND_ADAPTIVE_ORBIT_REPAIRS_20260802.md`.

This is the first exact remaining static clause after rank size and orbit
count are removed.

## 8. Strength of the surviving all-\(k\) clause

### Proposition 8.1 (uniform-chain consequence)

If, for one absolute \(C\), every strict lower ideal has an anchored chain
factor of depth at most \(d(k)+C\), then the full Boolean lattice has a
minimum \(W\)-chain decomposition whose largest chain has size strictly less
than

\[
                         {2^k\over W}+2C+3.            \tag{8.1}
\]

#### Proof

Complement and concatenate paired lower factors. In even dimension the
resulting maximum is at most \(2(d+C)+2\); in odd dimension it is at most
\(2(d+C)+1\). Use

\[
\begin{aligned}
 {2^k\over W}
 &=2{\Lambda\over W}+1+{2\over W}
 &&\text{in even dimension},\\
 {2^k\over W}
 &=2{\Lambda\over W}+{2\over W}
 &&\text{in odd dimension},
\end{aligned}
\]

and \(d\le\lceil\Lambda/W\rceil<\Lambda/W+1\). In either parity the
difference is less than \(2C+3\). \(\square\)

Thus the all-\(k\) \(d+O(1)\) anchored theorem lies on the strong
uniform-chain frontier. The orbit reduction isolates one polynomial
global Hall system, but does not prove its feasibility.

## 9. Static chainization versus literal serialization

The K19 and K21 theorems are static factors only. They do not imply
contiguous-OR words of lengths \(B(19)\) or \(B(21)\). A literal theorem
still requires, on one frozen owner table:

* a balanced and connected overlap-state digraph;
* endpoint aperture;
* global address and propagated-history guards;
* residence and every required upper witness;
* common-cap and lower-compiler closure; and
* a same-frozen-slice regenerative relay.

Every item is **UNPROVED** here. No new value of \(\nu(k)\), and no
all-\(k\) \(B(k)+O(1)\) upper bound, is claimed.
