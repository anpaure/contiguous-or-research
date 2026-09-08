# Single-bulge rings pack their first three rows; growing tight windows are the next Hall gate

**Date:** 2026-08-07  
**Method:** strengthened capacitated star packing, one fixed symmetric-chain
decomposition, and graphic/partition matroid intersection  
**Status:** unconditional.  The theorem closes the complete rank-\(s\),
rank-\((s+1)\), and rank-\((s+2)\) literal rows at density above theta,
and gives a
deterministic target-disjoint saturated-chain extension from the complete
base row.  It does **not** identify those SCD chains with all higher marked
and bridge values of the literal single-bulge word.  The next exact
obstruction is the growing-depth tight-window/shared-\(H\) system in
Section 6.

## 1. Parameters and the missing three bases

Use the odd triangular parameters

\[
 n=2m+1,\qquad s=m-2d,\qquad K=3d,
\tag{1.1}
\]

and assume \(d\ge2\), \(s\ge1\), and

\[
                         v:=n-s+1\ge4d.
\tag{1.2}
\]

The audited base-layer theorem reserves only the
\(3(d-1)\) low-phase bases

\[
                         P\cup\{x\}.
\]

The exact bridge completion has three further rank-\(s\) values, one at
each high phase: in (2.9) of
`MATH_THEOREM_SINGLE_BULGE_TRIANGULAR_RESET_FACTOR_20260807.md`, the first
high bridge value is \(P\cup\{g_u\}\).  Thus the complete base inventory
of a length-\(3d\) ring is the \(K\)-petal star

\[
                \mathcal B(P,F)=\{P\cup\{x\}:x\in F\},
 \qquad |P|=s-1,\quad |F|=K.                         \tag{1.3}
\]

The three extra petals are harmless.

## 2. Almost-spanning integral packing of the complete base inventory

Let

\[
 \mathcal V={ [n]\choose s},\qquad
 \mathcal C={ [n]\choose s-1},
 \qquad V=|\mathcal V|,\quad C=|\mathcal C|.
\]

The inclusion graph is \((v,s)\)-biregular, so \(Cv=Vs\).

Greedily choose an unused centre having at least \(K\) unused rank-\(s\)
supersets, reserve any \(K\), and stop when no such centre remains.  Let
\(M\) be the number of selected stars and \(U=KM\) the number of reserved
rank-\(s\) targets.

### Theorem 2.1 (complete-base star packing)

The greedy packing satisfies

\[
 \boxed{
 M\ge {C(v-K+1)\over Ks+v-K+1}}
\tag{2.1}
\]

and

\[
 \boxed{
 {U\over V}\ge
 {Ks(v-K+1)\over v(Ks+v-K+1)}=1-O(1/d).}
\tag{2.2}
\]

Every selected \(K\)-star lifts to a literal single-bulge ring, and all
rank-\(s\) marked **and bridge** values of the selected rings are distinct.

#### Proof

At termination each unused centre is incident with at least \(v-K+1\)
used targets.  Counting incidences between unused centres and used targets
gives

\[
                 (C-M)(v-K+1)\le Us=MKs.
\]

Rearrangement gives (2.1), and \(Cv=Vs\) gives (2.2).  Since
\(K=\Theta(d)\), \(s,v=\Theta(n)\), and \(n=\Theta(d^2)\), the two losses
are \(O(K/v)+O(v/(Ks))=O(1/d)\).

For a selected pair \((P,F)\), split \(F\) into three high labels and
\(3(d-1)\) low labels and place them in the periodic schedule
\(\mathsf L^{d-1}\mathsf H\).  Condition (1.2) leaves

\[
                         v-K\ge d
\]

coordinates outside \(P\cup F\); choose them as the reset bank \(H\).
The exact single-bulge theorem supplies the literal ring.  Its low
rank-\(s\) values are \(P+x\) for low \(x\), and (2.9) supplies
\(P+g\) for each of the three high labels.  Hence its complete rank-\(s\)
inventory is exactly (1.3), already disjoint by the greedy construction.
\(\square\)

### Corollary 2.2 (theta-sized complete-base bank)

Let

\[
 W={2m+1\choose m},\qquad
 \theta=4\sum_{a\ge1}e^{-4\pi a^2}.
\]

For all sufficiently large parameters, Theorem 2.1 contains a subfamily
of

\[
                         \left\lceil{\theta W\over3d}\right\rceil
\tag{2.3}
\]

rings, hence at least \(\theta W\) endpoints, whose complete rank-\(s\)
inventories are disjoint.

#### Proof

The local central estimate gives \(V/W\to e^{-\pi}\), while (2.2) gives
\(U=(e^{-\pi}-o(1))W\).  Since \(e^{-\pi}>3000\theta\), (2.3) follows.
\(\square\)

## 3. A deterministic abstract extension through every lower rank

The complete-base row has no further ordinary layer-Hall obstruction.

### Theorem 3.1 (one-SCD saturated extension)

Let \(\mathcal B\subseteq{[n]\choose s}\) be any family of distinct
rank-\(s\) sets.  There are pairwise disjoint saturated chains

\[
 S=S_s\subset S_{s+1}\subset\cdots\subset S_{m-1},
 \qquad S\in\mathcal B,                                \tag{3.1}
\]

one beginning at every \(S\in\mathcal B\).

In particular, the theta-sized complete-base bank of Corollary 2.2 has a
deterministic extension to pairwise disjoint full rank-\(s\)-through-
rank-\((m-1)\) chains.

#### Proof

Fix any symmetric-chain decomposition of \(B_n\).  Distinct sets of the
same rank \(s\) lie on distinct SCD chains.  A symmetric chain containing
a rank-\(s\) set starts at some rank \(a\le s\) and ends at rank
\(n-a\ge n-s>m-1\).  Truncate that chain at ranks \(s,\ldots,m-1\).
Different truncations are disjoint because their parent SCD chains are
disjoint. \(\square\)

This theorem is stronger than a separate Hall matching at every rank: the
same fixed SCD makes all rank choices coherent.  It also identifies the
remaining issue exactly.  A literal ring has already prescribed some of
the sets in (3.1); one may not replace those prescribed marked values by
the arbitrary SCD successors.

## 4. The first literal higher-row gate

Fix one selected low star

\[
                         (P,L),\qquad |L|=R:=3(d-1).
\]

Choosing the three low runs is the same as partitioning and ordering
\(L\) into three words of length \(d-1\).  At a low endpoint of age at
least two, the forced rank-\((s+1)\) marked target is

\[
                         P\cup\{x,y\},                   \tag{4.1}
\]

where \(x,y\) are consecutive labels in its low word.  Hence the forced
low marked values at rank \(s+1\) are precisely the edge colours of three
vertex-disjoint Hamilton paths covering \(L\).

For every selected star \(i\), put

\[
 E_i={L_i\choose2},\qquad
 \kappa_i(\{x,y\})=P_i\cup\{x,y\}\in{[n]\choose s+1}.
\tag{4.2}
\]

### Theorem 4.1 (exact first-row path formulation)

The low marked rank-\((s+1)\) targets of a family of selected rings can be
made pairwise distinct if and only if, for every \(i\), one can choose
three vertex-disjoint paths covering \(L_i\), with all
\(R-3\) edge colours (4.2), over every selected star, pairwise distinct;
each of the three paths must have exactly \(d-1\) vertices.

#### Proof

Every literal low schedule consists of three low words and gives their
three consecutive-edge paths.  Equation (4.1) identifies the target with
the edge colour, proving necessity.  Conversely, orient each of the three
chosen paths and use its vertex order as one low word.  Equation (4.1)
then gives exactly the selected colours, proving sufficiency for this
row. \(\square\)

The colours have considerably more structure than arbitrary edge colours.

### Lemma 4.2 (linear overlap of petal colour sets)

Assume the complete rank-\(s\) base stars are target-disjoint and no centre
is used twice.  For two distinct selected centres \(P,Q\), the colour
sets \(\kappa_P(E_P)\) and \(\kappa_Q(E_Q)\) intersect in at most one
rank-\((s+1)\) set.  If they intersect, then

\[
                         |P\setminus Q|=|Q\setminus P|=2
\tag{4.3}
\]

and their unique common colour is \(P\cup Q\).

#### Proof

If \(T\) is a common colour, then \(P,Q\subset T\), where
\(|P|=|Q|=s-1\) and \(|T|=s+1\).  Writing
\(h=|P\setminus Q|=|Q\setminus P|\), one obtains
\(|P\cup Q|=s-1+h\le s+1\), so \(h\le2\).

The case \(h=0\) would repeat the centre.  If \(h=1\), write
\(P-Q=\{a\}\), \(Q-P=\{b\}\).  A common colour has the form
\(T=P\cup Q\cup\{z\}\).  Its occurrence at \(P\) forces \(b\in L_P\),
and its occurrence at \(Q\) forces \(a\in L_Q\).  Then the rank-\(s\)
set

\[
                         P\cup\{b\}=P\cup Q=Q\cup\{a\}
\]

belongs to both complete base stars, contradicting their disjointness.
Thus \(h=2\), in which case \(|P\cup Q|=s+1\) and necessarily
\(T=P\cup Q\).  Hence there is at most one common colour. \(\square\)

The path row can in fact be packed at positive density without invoking a
nibble.

### Theorem 4.3 (deterministic two-layer path packing)

Assume in addition that \(v\ge4R\), which holds for all sufficiently large
triangular parameters.  There is a family of literal low schedules such
that

* all \(K=3d\) rank-\(s\) bases of every ring are globally distinct;
* the three low words of every ring have length \(d-1\); and
* all forced low marked rank-\((s+1)\) values are globally distinct;

and, if \(M_2\) is its number of rings, then

\[
 \boxed{
 M_2\ge
 {C\over
  1+2Ks/v+16(R-3){s+1\choose2}/v^2}.}
\tag{4.4}
\]

Consequently its endpoint count satisfies

\[
 \boxed{
 {K M_2\over W}\longrightarrow {e^{-\pi}\over10}.}
\tag{4.5}
\]

In particular, it contains a theta-sized subfamily with both of these
bottom rows collision-free.

#### Proof

Maintain sets \(U_s\) and \(U_{s+1}\) of already used targets.  At an
unused centre \(P\), let

\[
 A_P=\{x\notin P:P\cup\{x\}\notin U_s\}
\tag{4.6}
\]

and make a graph \(G_P\) on \(A_P\) by declaring \(xy\) to be an edge
when

\[
                         P\cup\{x,y\}\notin U_{s+1}.
\tag{4.7}
\]

Whenever \(|A_P|\ge K\) and \(G_P\) contains a path on \(R\) vertices,
take those vertices in path order, split the order into three consecutive
blocks of \(d-1\) vertices, and use them as the low words.  The two path
edges crossing block boundaries are discarded, leaving exactly \(R-3\)
allowed colours.  Choose any three further vertices of \(A_P\) as the
high labels.  Add all \(K\) bases to \(U_s\), add the \(R-3\) chosen path
colours to \(U_{s+1}\), and mark \(P\) used.  Continue greedily.

At termination divide the unused centres into two classes.  In class I,
\(a:=|A_P|<v/2\).  Such a centre is incident with more than \(v/2\) used
rank-\(s\) targets.  Since every used rank-\(s\) target contains exactly
\(s\) centres,

\[
                         |\mathrm I|{v\over2}\le M_2Ks.
\tag{4.8}
\]

For a centre in class II, \(a\ge v/2\), but \(G_P\) has no path on
\(R\) vertices.  The Erdős--Gallai path theorem gives

\[
                         e(G_P)\le{(R-2)a\over2}.
\]

Hence the number of blocked pairs in \({A_P\choose2}\) is at least

\[
 {a\choose2}-{(R-2)a\over2}
 ={a(a-R+1)\over2}\ge {v^2\over16},                    \tag{4.9}
\]

where the last inequality uses \(a\ge v/2\) and \(R\le v/4\).
Every blocked pair gives a used rank-\((s+1)\) target containing \(P\).
One such target contains exactly \({s+1\choose2}\) rank-\((s-1)\)
centres.  Since \(|U_{s+1}|=M_2(R-3)\),

\[
 |\mathrm {II}|{v^2\over16}
 \le M_2(R-3){s+1\choose2}.                              \tag{4.10}
\]

Now \(C-M_2=|\mathrm I|+|\mathrm {II}|\).  Substituting (4.8)--(4.10)
and rearranging proves (4.4).

Finally, in the triangular regime

\[
 {C\over W}\to e^{-\pi},\qquad {s\over v}\to1,
 \qquad {K\over R}\to1,
 \qquad {{s+1\choose2}\over v^2}\to{1\over2}.
\]

Dividing the denominator of (4.4) by \(R\) gives the limit
\(2+8=10\), proving (4.5).  Because \(e^{-\pi}/10>300\theta\), the final
assertion follows. \(\square\)

The six rank-\((s+1)\) bridge values can be included as well.  We first
record that the fixed order on \(H\) used in the displayed bridge theorem
is not essential.

### Lemma 4.4 (endpointwise bridge orders)

In one literal single-bulge ring, the elements of the common reset bank
\(H\) may be ordered independently at different endpoints in the bridge
completion.  The resulting complete marked-plus-bridge bank is still
collision-free within that ring.

#### Proof

For a low endpoint \(e\), intersection of any bridge target with the
private-label shore is its all-low cyclic interval \(I_e\).  Its size
recovers the age, and the interval (whose length is below the ring length)
recovers the endpoint.  After \(e\) is known, intersection with \(H\)
recovers the chosen initial segment of its local permutation.  Thus no two
low bridge targets collide, independently of the permutations.

For a high endpoint, the private intersection is its unique high label
\(g_e\), so the same argument applies.  A low private interval cannot
equal a high singleton because the low and high private labels are
disjoint designated classes.  The bridge-versus-marked argument from Theorem
2.2 is unchanged: a low bridge either omits part of \(H\), or, when it
contains all of \(H\), has an all-low private interval; a marked high
target crossing a reset has a high private label.  A high bridge withholds
one locally chosen last member of \(H\), whereas a marked high target
contains all of \(H\). \(\square\)

### Theorem 4.5 (complete first-two-row packing)

Assume \(d\ge6\) and

\[
                         v\ge4(K+6).
\tag{4.11}
\]

(This stronger inequality, like all asymptotic conclusions here, holds
for all sufficiently large triangular parameters.)  There are literal
single-bulge rings for which **every** rank-\(s\) and rank-\((s+1)\)
marked or bridge target is globally distinct.  If \(M_{01}\) denotes the
number of rings, then

\[
 \boxed{
 M_{01}\ge
 {C\over
  1+2Ks/v+16K{s+1\choose2}/v^2}.}
\tag{4.12}
\]

Consequently

\[
 \boxed{
 {K M_{01}\over W}\longrightarrow {e^{-\pi}\over10},}
\tag{4.13}
\]

so a theta-sized complete-two-row subfamily exists.

#### Proof

Use the same greedy construction as Theorem 4.3, but now ask \(G_P\) for
a path on

\[
                         J:=K+6=3d+6
\tag{4.14}
\]

vertices.  Split its ordered vertex list into six consecutive pieces of
sizes

\[
                         d,d,d,2,2,2.                    \tag{4.15}
\]

In each length-\(d\) piece, designate the first vertex as a member of
\(H\) and the remaining \(d-1\) vertices, in order, as one low word.  In
each length-two piece, designate one vertex as a high private label and
the other as a member of \(H\).  Thus the six designated \(H\)-labels are
distinct, and the remaining \(K\) vertices are exactly the \(K\) private
labels whose rank-\(s\) bases are reserved.

The edges internal to the first three pieces are the first-low bridge
edge followed by the \(d-2\) forced marked edges of that low word.  The
last three pieces supply the three high bridge edges.  There are exactly

\[
                         3(d-1)+3=3d=K                 \tag{4.16}
\]

such edges.  They are all unused by the definition of \(G_P\).  Discard
the five path edges between pieces.  Complete the six designated reset
labels to a \(d\)-set \(H\), possible because \(v\ge K+d=4d\), and use
Lemma 4.4 to put the designated reset label first in the corresponding
endpoint's bridge order.  This materializes exactly the complete
rank-\((s+1)\) row.

At termination, class I is counted exactly as in (4.8).  A class-II
centre has \(a\ge v/2\) but no path on \(J\) vertices.  Erdős--Gallai and
\(J\le v/4\) give at least \(v^2/16\) blocked pairs.  Now
\(|U_{s+1}|=KM_{01}\), so

\[
 |\mathrm {II}|{v^2\over16}
 \le M_{01}K{s+1\choose2}.                               \tag{4.17}
\]

Together with (4.8), this yields (4.12).  The same limit calculation as
in Theorem 4.3 gives (4.13). \(\square\)

The numerical hypothesis (4.11) is only a convenient uniform threshold
for the displayed \(v^2/16\) bound.  It does not alter the asymptotic
coefficient, since \(v/(K+6)\to\infty\).

The same idea survives one more row.  We use the following elementary
tight-path form of the deletion argument behind Erdős--Gallai.

### Lemma 4.6 (3-uniform tight-path bound)

Let \(\mathcal H\) be a 3-uniform hypergraph on \(a\) vertices.  If
\(\mathcal H\) has no tight path with \(k\) edges (equivalently, no
ordered list of \(k+2\) distinct vertices whose consecutive triples are
edges), then

\[
                         e(\mathcal H)\le(k-1){a\choose2}.
\tag{4.18}
\]

#### Proof

Repeatedly choose a pair of positive codegree at most \(k-1\) and delete
all hyperedges containing it.  Charge those deleted edges to that pair.
If this deletes the whole hypergraph, every pair receives at most \(k-1\)
charges, proving (4.18).

Otherwise a nonempty subhypergraph remains in which every pair of positive
codegree has codegree at least \(k\).  Start with any edge and extend a
tight path greedily.  After \(j<k\) edges, the final pair lies in at least
\(k\) edges, while at most \(j\le k-1\) of their third vertices have
already appeared in the path.  A fresh third vertex therefore extends the
path.  This constructs \(k\) edges, a contradiction. \(\square\)

### Theorem 4.7 (complete first-three-row packing)

Assume \(d\ge12\) and, with

\[
                         J_3:=K+12=3d+12,
\]

assume \(v\ge100J_3\).  There are literal single-bulge rings for which
every rank-\(s\), rank-\((s+1)\), and rank-\((s+2)\) marked or bridge
target is globally distinct.  If \(M_{012}\) is the number of rings, then

\[
 \boxed{
 M_{012}\ge
 {C\over
  1+2Ks/v+
  {128K\over v^3}
   \left({s+2\choose3}+3v{s+1\choose2}\right)}.}
\tag{4.19}
\]

Consequently

\[
 \boxed{
 {K M_{012}\over W}
 \longrightarrow {3e^{-\pi}\over646}>14\theta.}
\tag{4.20}
\]

#### Proof

At an unused centre \(P\), retain the base-available vertex set \(A_P\)
from (4.6).  Define a 3-uniform hypergraph \(\mathcal H_P\) on \(A_P\):
the triple \(xyz\) is an edge exactly when

1. the rank-\((s+2)\) set \(P\cup\{x,y,z\}\) is unused; and
2. all three rank-\((s+1)\) sets
   \(P\cup\{x,y\}\), \(P\cup\{x,z\}\), and
   \(P\cup\{y,z\}\) are unused.

Whenever \(\mathcal H_P\) contains a tight path on \(J_3\) vertices,
split its ordered vertex list into six consecutive pieces of sizes

\[
                         d+1,d+1,d+1,3,3,3.             \tag{4.21}
\]

Write a long piece as

\[
                         h_2,h_1,x_1,\ldots,x_{d-1}.
\tag{4.22}
\]

Its \(x\)'s form one low word.  Its consecutive pairs used by the ring
are

\[
 h_1x_1,x_1x_2,\ldots,x_{d-2}x_{d-1},
\]

which are exactly that word's complete rank-\((s+1)\) row.  Its
consecutive triples are

\[
 h_2h_1x_1, h_1x_1x_2, x_1x_2x_3,\ldots,
 x_{d-3}x_{d-2}x_{d-1}.                                 \tag{4.23}
\]

These are respectively the age-one second bridge value, the age-two first
bridge value, and the forced marked triples at ages at least three.  Thus
(4.23) is exactly the complete rank-\((s+2)\) row of that low word.

Write a short piece as \(h_2,h_1,g\).  Its final pair \(h_1g\) and its
triple \(h_2h_1g\) are the high endpoint's rank-\((s+1)\) and
rank-\((s+2)\) bridge values.  Across all six pieces there are exactly
\(K\) private labels and twelve distinct designated reset labels.  Extend
the latter to one common \(d\)-set \(H\), and use Lemma 4.4 to begin each
relevant endpoint permutation with its designated \(h_1,h_2\).

Reserve the \(K\) actual rank-\(s\) bases and the \(K\) actual
rank-\((s+2)\) triples.  To preserve the definition of future
\(\mathcal H_P\)'s, also reserve every pair lying in an internal triple of
the six pieces.  There are at most \(3K\) such pair targets.  This includes
all actual rank-\((s+1)\) values and only adds harmless guard pairs.  All
reserved targets are new by the definition of \(\mathcal H_P\).  Discard
the five cross-piece transitions and continue greedily.

At termination, class I again satisfies (4.8).  For a class-II centre put
\(a=|A_P|\ge v/2\).  The hypergraph \(\mathcal H_P\) has no tight path on
\(J_3\) vertices, so Lemma 4.6, with \(k=J_3-2\), gives

\[
 e(\mathcal H_P)\le(J_3-3){a\choose2}.
\]

Since \(J_3\le v/100\le a/50\) and \(a\) is sufficiently large,

\[
 {a\choose3}-(J_3-3){a\choose2}
 \ge {a^3\over12}-{a^3\over100}
 >{v^3\over128}.                                        \tag{4.24}
\]

Every missing triple in (4.24) is explained either by a used
rank-\((s+2)\) target or by one of its three used rank-\((s+1)\) pair
targets.  A rank-\((s+2)\) target contains \({s+2\choose3}\) possible
centres \(P\).  A used rank-\((s+1)\) target contains
\({s+1\choose2}\) possible centres, and for each such centre it lies in
at most \(v\) candidate triples.  Since the construction reserves at most
\(K M_{012}\) triples and \(3K M_{012}\) pairs,

\[
 |\mathrm {II}|{v^3\over128}
 \le M_{012}K
 \left({s+2\choose3}+3v{s+1\choose2}\right).            \tag{4.25}
\]

Combine (4.8) and (4.25) and rearrange to obtain (4.19).  Finally,

\[
 {{s+2\choose3}\over v^3}\to{1\over6},\qquad
 {3v{s+1\choose2}\over v^3}\to{3\over2}.
\]

After division by \(K\), the denominator in (4.19) tends to

\[
                         2+128\left({1\over6}+{3\over2}\right)
                         ={646\over3}.
\]

Together with \(C/W\to e^{-\pi}\), this proves (4.20). \(\square\)

Theorem 4.7 is close to the limit of this crude deletion count: its
remaining factor above theta is only about fourteen.  Iterating the same
argument with unoptimized higher-uniformity constants would lose that
margin.  An all-depth result therefore needs the coherent SCD/product
structure, not a row-by-row use of generic extremal bounds.

Nevertheless, the same proof gives a useful qualitative theorem: no fixed
finite target row is an obstruction.

### Lemma 4.8 (uniform tight-path deletion bound)

Let \(r\ge2\).  If an \(r\)-uniform hypergraph on \(a\) vertices has no
tight path with \(k\) edges, then

\[
                         e(\mathcal H)\le(k-1){a\choose r-1}.
\tag{4.26}
\]

#### Proof

Repeat the proof of Lemma 4.6 with \((r-1)\)-sets in place of pairs.
If deletion exhausts the hypergraph, charge at most \(k-1\) edges to each
\((r-1)\)-set.  Otherwise every positive \((r-1)\)-degree is at least
\(k\).  At the end of a tight path with \(j<k\) edges, precisely \(j\)
previous vertices lie outside its final \((r-1)\)-tuple, so one of the at
least \(k\) extensions uses a fresh vertex. \(\square\)

### Theorem 4.9 (every fixed number of rows packs at positive density)

Fix \(q\ge1\), put \(r=q+1\), and let the triangular parameters tend to
infinity.  For all sufficiently large parameters there is a family of
literal single-bulge rings whose complete marked-plus-bridge target banks
are globally disjoint at every rank

\[
                         s,s+1,\ldots,s+q.               \tag{4.27}
\]

Its endpoint density has a positive lower limit depending only on \(q\).
More explicitly, put

\[
 c_r={1\over2(2r)^r},
\qquad
 A_q=\sum_{h=1}^{q}
 { {r\choose h+1}\over (h+1)!(q-h)!}.
\tag{4.28}
\]

Then the family may be chosen with endpoint density at least

\[
 \boxed{
 \gamma_q-o(1),\qquad
 \gamma_q={e^{-\pi}\over 2+c_r^{-1}A_q}>0.}
\tag{4.29}
\]

#### Proof

For large parameters, \(d\ge6q\).  At an unused centre \(P\), retain the
base-available set \(A_P\).  Define an \(r\)-uniform hypergraph
\(\mathcal H_P^{(q)}\) on \(A_P\) as follows: an \(r\)-set \(X\) is an
edge if every target

\[
                         P\cup Y,qquad
 Y\subseteq X,\quad2\le |Y|\le r,                       \tag{4.30}
\]

is unused.

Ask for a tight path on

\[
                         J_q:=K+6q=3d+6q                \tag{4.31}
\]

vertices, and split it into three long pieces of length \(d-1+q\) and
three short pieces of length \(q+1\).  Write a long piece

\[
                         h_q,\ldots,h_1,x_1,\ldots,x_{d-1}.
\tag{4.32}
\]

For every \(0\le j\le q\), the consecutive \((j+1)\)-window ending at
\(x_a\) is

\[
 \begin{cases}
  \{x_{a-j},\ldots,x_a\},&a\ge j+1,\\
  \{h_{j-a+1},\ldots,h_1,x_1,\ldots,x_a\},&a\le j.
 \end{cases}                                             \tag{4.33}
\]

The first line is the forced low marked target of rank \(s+j\); the
second is its bridge continuation after \(j-a+1\) reset additions.  A
short piece \(h_q,\ldots,h_1,g\) gives the corresponding high bridge
windows.  Thus the six pieces realize every row in (4.27).  There are
\(K\) private vertices and \(6q\) designated reset vertices; extend the
latter to a common \(d\)-set \(H\), and use Lemma 4.4 for the endpointwise
orders.

For every internal \(r\)-window reserve all targets (4.30).  At rank
\(s+h\), \(1\le h\le q\), this reserves at most

\[
                         K{r\choose h+1}                 \tag{4.34}
\]

targets per ring, because the six pieces contain exactly \(K\) internal
\(r\)-windows.  Continue greedily.

At termination, class I again gives (4.8).  In class II, \(a=|A_P|\ge
v/2\), but \(\mathcal H_P^{(q)}\) has no tight path on \(J_q\) vertices.
For fixed \(q\) and sufficiently large parameters, Lemma 4.8 and

\[
 { {a\choose r}\over {a\choose r-1}}
 ={a-r+1\over r}\gg J_q
\]

show that at least half of all \(r\)-sets are missing.  Using
\({a\choose r}\ge(a/r)^r\) and \(a\ge v/2\), the number missing is at
least

\[
                         c_rv^r.                          \tag{4.35}
\]

A used rank-\((s+h)\) target contains
\({s+h\choose h+1}\) possible centres \(P\).  For a fixed such centre,
its \((h+1)\)-set outside \(P\) extends to at most
\({v\choose q-h}\) candidate \(r\)-sets.  Equations (4.34)--(4.35)
therefore give

\[
 |\mathrm {II}|c_rv^r
 \le MK\sum_{h=1}^{q}
 {r\choose h+1}{s+h\choose h+1}{v\choose q-h}.          \tag{4.36}
\]

Combining this with class I yields

\[
 M\ge {C\over
 1+2Ks/v+{K\over c_rv^r}
 \sum_{h=1}^{q}
 {r\choose h+1}{s+h\choose h+1}{v\choose q-h}}.         \tag{4.37}
\]

Since \(s/v\to1\), division of the denominator by \(K\) gives
\(2+c_r^{-1}A_q\).  Also \(C/W\to e^{-\pi}\).  Multiplying (4.37) by
\(K/W\) proves (4.29). \(\square\)

The quantifiers in Theorem 4.9 are essential.  It fixes \(q\) first;
the constant \(\gamma_q\) deteriorates rapidly.  It neither supplies a
theta-sized bank uniformly for \(q=d\) nor permits \(6q\) distinct reset
seeds when \(q\) is comparable with \(d\).  The all-depth problem is
precisely to **reuse** one common \(d\)-set \(H\) coherently instead of
spending six fresh reset labels per protected row.

## 5. The sharp matroid-Hall shadow

The path requirement is stronger than ordinary matching.  Its exact
graphic relaxation already gives a sharp, explicit higher-row Hall cut.

Let

\[
                         E=\mathop{\dot\bigcup}_i E_i.
\]

On each \(E_i\), take the graphic matroid of the clique \(K_{L_i}\) and
truncate its rank to \(R-3\).  Let \(\mathsf G_3\) be the direct sum of
these truncated graphic matroids.  Let \(\mathsf C\) be the partition
matroid in which two edges conflict exactly when they have the same colour
\(\kappa\).

For \(A\subseteq E\), write \(A_i=A\cap E_i\), and let \(c_i(A_i)\) be
the number of connected components of \((L_i,A_i)\), isolated vertices
included.

### Theorem 5.1 (sharp forest Hall criterion)

There is, in every selected star, a three-component spanning forest whose
edge colours are globally distinct if and only if, for every
\(A\subseteq E\),

\[
 \boxed{
 |\kappa(E\setminus A)|
 \ge
 \sum_i\max\{0,c_i(A_i)-3\}.}
\tag{5.1}
\]

#### Proof

The desired forest family is a common independent set of size
\(\sum_i(R-3)\) in \(\mathsf G_3\) and \(\mathsf C\).  Matroid
intersection gives such a set if and only if

\[
 r_{\mathsf G_3}(A)+r_{\mathsf C}(E\setminus A)
 \ge\sum_i(R-3)                                           \tag{5.2}
\]

for every \(A\subseteq E\).  Here

\[
 r_{\mathsf G_3}(A)
 =\sum_i\min\{R-3,R-c_i(A_i)\},
 \qquad
 r_{\mathsf C}(E\setminus A)=|\kappa(E\setminus A)|.
\]

Subtracting the first rank from \(\sum_i(R-3)\) gives exactly the
right-hand side of (5.1). \(\square\)

Every literal three-path solution satisfies (5.1).  Conversely, (5.1)
produces three-component forests, but those components need not be paths
or have the required equal size \(d-1\); the degree-two/equal-path
condition is an additional physical row.  Thus (5.1) is the first sharp
polynomial matroid-Hall obstruction, not a claimed solution of the literal
path problem.

Theorems 4.3 and 4.5 show that this cut can be satisfied with enormous
margin by choosing the stars and paths jointly.  The cut remains the exact
obstruction for an already frozen base-star family; it is not the final
gate of the jointly constructed two-layer family.

## 6. The bridge-row Hall systems

After the low orders are chosen, the exact bridge theorem associates to a
low endpoint \(e\) of age \(a\) the Boolean interval

\[
 [A_e,A_e\cup H_i],\qquad
 A_e=P_i\cup I_e,\quad |H_i|=d,                           \tag{6.1}
\]

and chooses a maximal chain through it.  At bridge offset \(r\), its menu
is

\[
\mathcal N_r(e)=
 \{A_e\cup J:J\subseteq H_i,\ |J|=r\}.                  \tag{6.2}
\]

For the six endpoints whose rank-\((s+1)\) bridge value was fixed in
Theorem 4.5, (6.2) must be restricted to subsets \(J\) containing that
endpoint's designated first reset label.  This conditions the remaining
menu without changing the already packed row.

Therefore every literal full-chain extension necessarily satisfies the
ordinary Hall inequalities

\[
 \boxed{
 \left|\bigcup_{e\in X}\mathcal N_r(e)\right|\ge |X|
 \quad\hbox{for every endpoint family }X
 \hbox{ and every }1\le r\le d.}
\tag{6.3}
\]

These row inequalities are not sufficient by themselves: choices at
successive \(r\)'s must be nested, i.e. arise from one permutation of
\(H_i\), and the same \(H_i\) is shared by all endpoints of ring \(i\).
They are nevertheless exact, named higher-row Hall cuts.  A failed cut
(5.1) or (6.3) certifies that an SCD extension cannot be relabelled into
the literal marked-plus-bridge completion.

There is a simultaneous forced-window row.  At rank \(s+2\), every low
endpoint of age at least three carries

\[
                         P_i\cup\{x_{a-2},x_{a-1},x_a\}. \tag{6.4}
\]

Thus the ordered low words chosen at rank \(s+1\) must also have globally
distinct consecutive triples.  Theorem 4.7 packs this row jointly with
the corresponding conditioned bridge values.  At rank \(s+3\) the same
statement becomes a consecutive-quadruple condition, and in general rank
\(s+j\) sees the consecutive \((j+1)\)-windows that remain wholly inside
a low run, while the shorter-age endpoints enter the conditioned interval
menus (6.2).  The remaining extension is therefore a coupled all-depth
rainbow tight-window and nested-interval problem; solving the bridge Hall
rows alone would not suffice.

## 7. Verdict

The following two statements are now unconditional:

1. a theta-sized family of literal rings can reserve **all** of its
   rank-\(s\) marked and bridge bases without collision;
2. those bases admit a deterministic, globally disjoint saturated-chain
   extension through rank \(m-1\).

Moreover, a theta-sized family can be chosen so that its **complete**
rank-\((s+1)\) marked-and-bridge row is already collision-free (Theorem
4.5), and even its complete rank-\((s+2)\) row can be included (Theorem
4.7).

The extension is abstract rather than literal.  For a frozen family, the
first correlation is the rainbow-path cut (5.1); joint greedy selection
now closes the entire first three rows.  The first unclosed literal values
are at rank \(s+3\), and the same pattern grows into higher-uniformity
tight windows coupled to conditioned shared-\(H\) extensions.  Thus no scalar layer
count or ordinary base-row Hall argument can finish the hinge factor.  The
next theorem must be an **all-depth rainbow tight-window plus shared-\(H\)
interval-chain extension theorem**, starting from the complete-three-row
family of Theorem 4.7.
