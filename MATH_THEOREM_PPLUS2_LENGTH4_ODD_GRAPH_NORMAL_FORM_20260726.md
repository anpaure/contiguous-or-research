# Odd-graph normal form of a legal length-four \(p+2\) phase direction

Date: 2026-07-26

Method: pure mathematics only.

## 1. Input from phase completion

Let \(p=2m+1\) be prime and let \(\sigma\) be the chosen coordinate
\(p\)-cycle.  Suppose a size-\(p+2\) singleton component has a length-four
complement cycle

\[
 A^+,B^-,C^+,D^-
\]

and that the nonzero alternating phase direction \(t\varepsilon\) is
legal.  The phase-pairing theorem gives the two disjoint middle-packet
identities

\[
 \boxed{
 \sigma^tA\sqcup\sigma^tC=B\sqcup D,}
\tag{1.1}
\]

\[
 \boxed{
 \sigma^{-t}B\sqcup\sigma^{-t}D=A\sqcup C.}
\tag{1.2}
\]

Each side is a disjoint union of two wreath packets.  The ownership overlay
in each identity has underlying graph \(K_{2,2}\).

Write

\[
 \mathcal R_-=B\sqcup D,qquad
 \mathcal S_-=\sigma^tA\sqcup\sigma^tC,
\tag{1.3}
\]

and

\[
 \mathcal R_+=A\sqcup C,qquad
 \mathcal S_+=\sigma^{-t}B\sqcup\sigma^{-t}D.
\tag{1.4}
\]

The special \(\{0,2\}\) partial-count completion performs only the trade
\(\mathcal R_-\to\mathcal S_-\).  The ordinary one-shift-per-row lift
performs both trades simultaneously.

---

## 2. The two trades are conjugate inverses

### Theorem 2.1 -- exact conjugacy

As colored odd-graph 2-factors,

\[
 \boxed{
 \sigma^t\mathcal R_+=\mathcal S_-,\qquad
 \sigma^t\mathcal S_+=\mathcal R_-.}
\tag{2.1}
\]

Consequently the odd-graph edge symmetric difference of the positive-side
trade is carried by \(\sigma^t\) to the symmetric difference of the
negative-side trade with old and new colors reversed.  In particular the
two trades have identical alternating-circuit lengths and identical
multi-cut path-length data.

#### Proof

The first identity in (2.1) is the definition of \(\mathcal S_-\).  The
second is the definition of \(\mathcal S_+\) translated by \(\sigma^t\).
Coordinate translation is an automorphism of the odd graph and preserves
all edge and path lengths. \(\square\)

Thus the common coordinate shift imposes a strong relation between the two
degree-two trades, but it does not yet say that either trade is a single
alternating \(C_8\).

---

## 3. General two-wreath multi-cut normal form

The next theorem applies to every squarefree two-for-two wreath trade, not
only to (1.1).

Let

\[
 \mathcal R=R_1\sqcup R_2,qquad
 \mathcal S=S_1\sqcup S_2
\tag{3.1}
\]

be two factorizations of the same \(2p\) middle vertices into two wreath
cycles.  Regard them as 2-factors of the induced odd-graph subgraph.

### Theorem 3.1 -- alternating-path normal form

Assume the trade is nontrivial and every new wreath \(S_j\) meets both old
wreath supports.  Then there is an integer \(k\ge2\) with the following
properties.

1. Exactly \(k\) edges are deleted from each old cycle \(R_i\).
2. The retained common edges split each \(R_i\) into \(k\) (possibly
   single-vertex) paths.  If their vertex lengths are

   \[
   r_{i,1},\ldots,r_{i,k},
   \]

   then

   \[
   \sum_{a=1}^kr_{i,a}=p
   \qquad(i=1,2).
   \tag{3.2}
   \]
3. Every new noncommon edge joins a vertex of \(R_1\) to a vertex of
   \(R_2\).  There are exactly \(2k\) such edges.
4. Each new wreath is a cyclic alternating concatenation of retained paths
   from \(R_1\) and \(R_2\).  It contains equally many paths from the two
   old cycles, and the sum of their vertex lengths is exactly \(p\).
5. The complete red/blue edge symmetric difference contains \(2k\) old
   edges and \(2k\) new edges and decomposes into alternating even
   circuits.  Individual circuits need not themselves preserve the
   two-wreath condition when toggled separately.

Conversely, any such cross-reconnection by genuine odd-graph edges which
produces two cycles of length \(p\) gives a two-for-two wreath trade.

#### Proof

Every length-\(p\) wreath cycle in \(KG(p,m)\) is induced.  Therefore a
new edge whose endpoints both lie in one old support \(R_i\) must already
be an edge of \(R_i\), hence is common.  All genuinely new edges cross
between \(R_1\) and \(R_2\).

Let \(k_i\) be the number of old noncommon edges in \(R_i\).  After common
edges are cancelled, every vertex has the same red and blue degree.  The
sum of red-exclusive degrees on vertices of \(R_i\) is \(2k_i\).  Every
blue-exclusive edge has exactly one endpoint in \(R_i\), so its total
number is \(2k_i\).  The same count on the other old cycle gives
\(k_1=k_2=:k\), and there are \(2k\) blue-exclusive edges.

Deleting \(k\) edges from a cycle gives \(k\) retained paths, with the
vertex-length sum (3.2).  All blue-exclusive edges cross, so every new
cycle alternates between paths of the two old colors.  Its length is the
sum of the path vertex lengths it uses and must equal \(p\).  This proves
items 1--4.

The red and blue exclusive degrees agree at every vertex, so the colored
symmetric difference is Eulerian and decomposes into alternating circuits,
proving item 5.  The converse is immediate, using the theorem that every
odd-graph \(p\)-cycle is a wreath.  Finally \(k=1\) would leave one
\(p\)-vertex path from each old cycle; the two cross edges reconnect them
into one \(2p\)-cycle, not two \(p\)-cycles.  Hence \(k\ge2\). \(\square\)

### Corollary 3.2 -- the \(k=2\) case is exactly balanced \(C_8\)

If \(k=2\), the old path-length profiles have the form

\[
 \{a,p-a\},\qquad\{b,p-b\}.
\]

The two new cycles have length \(p\) if and only if

\[
 \boxed{
 \{a,p-a\}=\{b,p-b\}.}
\tag{3.3}
\]

The symmetric difference then has four old and four new edges and is the
balanced alternating \(C_8\) switch of the existing two-wreath theorem.

For \(k\ge3\), Theorem 3.1 is the larger-circuit normal form.  The exact
constraint is no longer equality of two unordered two-part profiles; it is
a partition of the two \(k\)-part profiles into two alternating path
collections, each of total length \(p\).

---

## 4. What the common shift does not force

Apply Theorem 3.1 to \(\mathcal R_-\to\mathcal S_-\).  The ownership
\(K_{2,2}\) proved from the four complement columns ensures the trade is
nontrivial and that each new cycle meets both old supports.  It does not
control odd-graph adjacency between consecutive physical sets in the four
rows.  Hence it does not bound the cut number \(k\) from above.

The exact consequences of the common phase \(t\) are:

1. the negative and positive trades have the same \(k\), alternating
   circuit lengths, and path-length data, by Theorem 2.1;
2. their old/new colors are reversed under \(\sigma^t\);
3. the four special complement columns force all four ownership cells to
   be nonempty.

No implication \(k=2\) follows from the column phase equations alone.
Therefore a legal length-four completion reduces to two conjugate balanced
\(C_8\)'s only under the additional edge statement \(k=2\).  When
\(k\ge3\), it is rigorously described by the conjugate pair of multi-cut
normal forms in Theorem 3.1.

This isolates the next genuinely wreath-specific question: whether the
actual phase arrays force \(k=2\), permit \(k\ge3\), or forbid the legal
length-four completion altogether.

### Theorem 4.1 -- exact necklace-square construction criterion

The existence question can be restated entirely in terms of one genuine
two-for-two wreath trade.  Let

\[
 \mathcal U=A\sqcup C=E\sqcup F
\tag{4.1}
\]

be two wreath factorizations of the same \(2p\) physical middle sets.  Fix
a coordinate cycle \(\sigma\).  Assume every one of the four rows is
transversal to the \(\sigma\)-necklace partition.  For a row family
\(\mathcal V\), write \(m_{\mathcal V}(O)\) for its number of physical
sets in necklace \(O\).

Then (4.1) produces a local legal length-four \(p+2\) phase configuration
with nonzero amplitude \(t\) if and only if all of the following hold.

1. The necklace support

   \[
   \Omega=\{O:m_{\mathcal U}(O)>0\}
   \]

   has size \(p+2\).  Consequently exactly \(p-2\) necklaces have mass
   two and exactly four have mass one.
2. On the four mass-one necklaces, the unique physical vertex has the
   four owner types

   \[
   (A,E),\quad(A,F),\quad(C,E),\quad(C,F)
   \tag{4.2}
   \]

   once each.  Equivalently, the four missing row pairs form one length-four
   complement cycle rather than two length-two cycles.
3. The translate is disjoint:

   \[
   \boxed{\mathcal U\cap\sigma^t\mathcal U=\varnothing.}
   \tag{4.3}
   \]

Under these conditions take the old four rows to be

\[
 A,C,\sigma^tE,\sigma^tF.
\tag{4.4}
\]

Their nonconstant alternating shift replaces them by

\[
 \sigma^tA,\sigma^tC,E,F.
\tag{4.5}
\]

Both sides are squarefree wreath packings of the same \(4p\) middle sets,
and their four-row necklace complement is exactly the required length-four
cycle.

#### Proof

Suppose first that (4.1)--(4.3) hold.  Transversality makes every row's
necklace incidence zero-one.  Since \(A\sqcup C\) has \(2p\) vertices on
\(p+2\) necklaces and at most two vertices per necklace, its mass profile
must be \(2^{p-2}1^4\).  The same profile and the same physical vertices
belong to the alternative factorization \(E\sqcup F\).

At a mass-two necklace, all four rows \(A,C,E,F\) are incident.  At a
mass-one necklace, exactly one row from each factorization is incident.
Condition (4.2) makes the four missing-pair types a single 4-cycle.  After
translating \(E,F\), necklace incidences are unchanged.  Condition (4.3)
makes the four old rows in (4.4) pairwise middle-disjoint.

Finally,

\[
 \sigma^t(A\sqcup C)=\sigma^t\mathcal U
 =\sigma^t(E\sqcup F),
\]

so the phase pairing in every necklace is automatic.  Shifting the positive
rows by \(+t\) and the negative rows by \(-t\) gives (4.5).

Conversely, start from a legal length-four configuration and put

\[
 E=\sigma^{-t}B,qquad F=\sigma^{-t}D.
\]

The phase-pairing identity gives \(A\sqcup C=E\sqcup F\).  Its four-row
incidence pattern has common support \(p+2\), mass profile
\(2^{p-2}1^4\), and all four owner types because the complement cycle has
length four.  Squarefreeness of the old factor gives (4.3). \(\square\)

There is an exact phase-difference form of (4.3).  In every mass-two
necklace write its two phases as \(x_O,y_O\), and put

\[
 \Delta_\sigma(\mathcal U)
 =\{\pm(y_O-x_O):m_{\mathcal U}(O)=2\}.
\tag{4.6}
\]

Then

\[
 \boxed{
 \mathcal U\cap\sigma^t\mathcal U=\varnothing
 \quad\Longleftrightarrow\quad
 t\notin\Delta_\sigma(\mathcal U).}
\tag{4.7}
\]

Thus actual local existence is reduced to a **necklace-square
two-for-two trade** with a missing phase difference.  This is a genuine
finite geometric criterion, not an entropy heuristic.  Extending the four
rows to a complete exact factor, and realizing the remaining \(p-2\) rows
of the same incidence component by wreaths, remain separate completion
requirements.

### Corollary 4.2 -- the endpoint-frame tax does not lengthen the circuit

For either two-for-two trade in (1.3)--(1.4), put

\[
                         t_{ij}=|R_i\cap S_j|.
\]

Here `K(S_j,R_i)` is the signed endpoint-coordinate transition matrix
of Section 12 of the affine-grid gate, and `nu_-` counts its negative
entries.

Then

\[
 \boxed{
 \sum_{i,j=1}^2
 \left(\nu_-\bigl(K(S_j,R_i)\bigr)-(p-t_{ij})\right)\ge1,}
\tag{4.8}
\]

and consequently

\[
 \boxed{
 \sum_{i,j=1}^2\|K(S_j,R_i)\|_F^2\ge8p+2.}
\tag{4.9}
\]

The conjugate inverse trade satisfies the same inequalities.  Thus the
ordinary length-four completion pays at least four endpoint-frame support
positions beyond the two formal trade baselines counted together.

#### Proof

Apply Theorem 17.9 of the affine-grid gate with resolution size `r=2`.
The conjugacy in Theorem 2.1 preserves transition supports and reverses
the two factorizations. \(\square\)

This tax does not alter the length-four complement cycle: equations
(25.4)--(25.5) in the prime-cycle rigidity ledger depend only on the four
missing row--necklace incidences, whereas (4.8) is a coordinate-pair
statistic inside the completed wreath packets.  No current equation
bounds (4.8) from above by the complement-cycle length or by the odd-graph
multi-cut number `k`.

---

## 5. Exact lower-shadow relation between the two trades

For a wreath row \(R\), let \(u_q(R)\) be its depth-\(q\) cyclic-interval
load vector.  Coordinate equivariance gives

\[
 u_q(\sigma^tR)=\sigma^tu_q(R).
\tag{5.1}
\]

Define the change made by the special partial completion
\(\mathcal R_-\to\mathcal S_-\):

\[
 d_q=
 u_q(\sigma^tA)+u_q(\sigma^tC)-u_q(B)-u_q(D).
\tag{5.2}
\]

At the middle rank, \(d_0=0\) by (1.1).  The ordinary phase lift makes the
additional conjugate-inverse trade, and its total depth-\(q\) change is

\[
 \boxed{
 g_q=d_q-\sigma^{-t}d_q
     =(I-\sigma^{-t})d_q.}
\tag{5.3}

#### Proof

The second trade changes the load by

\[
 u_q(\sigma^{-t}B)+u_q(\sigma^{-t}D)-u_q(A)-u_q(C)
 =-\sigma^{-t}d_q.
\]

Add it to (5.2). \(\square\)

Thus the ordinary length-four direction is a literal coordinate
coboundary at every lower rank.  In particular, its total load change on
every \(\langle\sigma\rangle\)-orbit of targets is zero.  The partial
\(\{0,2\}\) completion is not constrained by this cancellation; its
change is \(d_q\) itself.

---

## 6. First-shadow support and exact drift

Consider the partial two-for-two trade with cut number \(k\).  For a middle
vertex \(X\) in its \(2p\)-vertex support, let

\[
 c^-(X)=\text{intersection of the two old factor neighbors of }X,
\]

\[
 c^+(X)=\text{intersection of the two new factor neighbors of }X.
\tag{6.1}
\]

Let \(Z\) be the set of vertices incident to at least one of the \(2k\)
deleted old edges.  A vertex outside \(Z\) keeps both factor neighbors, so
its depth-one color is unchanged.  Therefore

\[
 \boxed{
 d_1=\sum_{X\in Z}
 \bigl(e_{c^+(X)}-e_{c^-(X)}\bigr),}
\tag{6.2}
\]

and

\[
 |Z|\le4k,qquad
 \|d_1\|_1\le8k.
\tag{6.3}
\]

For the ordinary lift, (5.3) gives

\[
 \|g_1\|_1\le16k.
\tag{6.4}
\]

Let \(\mu\) be the full old factor's first-shadow load vector.  The exact
hole-count change is

\[
 \boxed{
 \begin{aligned}
 H_1(\mu+g_1)-H_1(\mu)
 ={}&\#\{S:\mu(S)>0,\ \mu(S)+g_1(S)=0\}\\
 &-\#\{S:\mu(S)=0,\ g_1(S)>0\}.
 \end{aligned}}
\tag{6.5}
\]

There is no sign determined by \(k\), the balanced path profiles, or the
coordinate coboundary alone.  It depends on the ambient multiplicities at
the positive and negative coordinates of (6.2).

For the centered quadratic energy, put

\[
 f_1=\mu-\frac W{N_1}\mathbf1,qquad S=\sigma^{-t}.
\]

The ordinary lift satisfies the exact identity

\[
 \boxed{
 \begin{aligned}
 \Delta\|f_1\|_2^2
 ={}&2\langle f_1-S^{-1}f_1,d_1\rangle\\
 &+2\bigl(\|d_1\|_2^2-\langle d_1,Sd_1\rangle\bigr).
 \end{aligned}}
\tag{6.6}
\]

The final line is \(\|(I-S)d_1\|_2^2\ge0\); the first line has no fixed
sign.  If the old load happens to be \(\sigma\)-invariant, the linear term
vanishes and every nontrivial ordinary length-four move weakly increases
quadratic energy.  Without such invariance, the identity alone permits
either sign and supplies no monotonicity theorem.

For comparison, the partial completion has

\[
 \Delta\|f_1\|_2^2
 =2\langle f_1,d_1\rangle+\|d_1\|_2^2.
\tag{6.7}
\]

---

## 7. Relation to the known \(C_8\) anti-repair result

If \(k=2\), each of the two conjugate trades is a balanced two-wreath
alternating \(C_8\).  Its complete first-shadow action is then obtained
from the local changed-vertex formula (6.2).  Only in the additional
universal common-core normal form does this action collapse to the familiar
four-coordinate rectangle with two positive and two negative corners.

The established canonical anti-repair theorem concerns an explicit private
MSW family of those universal common-core \(C_8\)'s.  Neither the
length-four phase pairing nor the common shift \(t\) identifies the present
trades with that private family.  For \(k\ge3\), the trade is outside the
single-\(C_8\) architecture entirely.

Therefore the existing anti-repair result does not sign (6.5) or (6.6).
The exact remaining input is the ambient first-shadow multiplicity profile
on the changed colors, or a new wreath-geometric theorem forcing a special
edge normal form.

There is a completely explicit formula in the universal \(k=2\) subcase.
Orient the partial trade so that

\[
 d_1=e_{P_1}+e_{P_2}-e_{M_1}-e_{M_2}.
\tag{7.1}
\]

Then the ordinary length-four lift has

\[
 \boxed{
 g_1=e_{P_1}+e_{P_2}+e_{SM_1}+e_{SM_2}
     -e_{M_1}-e_{M_2}-e_{SP_1}-e_{SP_2},
 \qquad S=\sigma^{-t}.}
\tag{7.2}
\]

If these eight targets are distinct, its exact hole drift is

\[
 \boxed{
 \begin{aligned}
 \Delta H_1={}&
 \sum_{T\in\{M_1,M_2,SP_1,SP_2\}}\mathbf1_{\{\mu(T)=1\}}\\
 &-\sum_{T\in\{P_1,P_2,SM_1,SM_2\}}\mathbf1_{\{\mu(T)=0\}}.
 \end{aligned}}
\tag{7.3}
\]

Coincident targets are handled by first combining their coefficients in
(7.2) and then using (6.5).  Formula (7.3) makes the absence of a universal
sign explicit: it is an eight-cell orbit-coupled ledger, not the four-cell
private anti-repair ledger.

---

## 8. Status

Proved:

1. the two length-four trades are coordinate-conjugate inverses;
2. every two-for-two wreath trade has the alternating-path multi-cut normal
   form of Theorem 3.1;
3. \(k=2\) is exactly the known balanced \(C_8\) case, while \(k\ge3\)
   gives the rigorous larger-circuit normal form;
4. the ordinary lift has the all-depth coboundary action
   \((I-\sigma^{-t})d_q\);
5. the exact first-shadow support, hole-drift, and quadratic-energy formulas
   are (6.2), (6.5), and (6.6), with no universal sign.
6. the universal-\(C_8\) fixed-index near-translate construction is
   impossible for every odd prime (Theorem 9.1 and Lemma 9.0);
7. any legal component omits an unsigned phase-gap class and therefore has
   a different allowed unsigned gap occurring at least three times.

Still unproved: whether a non-near-translate length-four phase completion
exists in the MSW/prime-cycle geometry, and if it does, which cut numbers
and ambient first-shadow signs occur.

---

## 9. The natural universal-\(C_8\) one-transposition construction is impossible

This section closes the most direct symbolic attempt to realize the
necklace-square criterion.  The calculation is useful because the attempt
gets every numerical feature right--\(p-2\) intended cross-row pairings and
the four correct singleton owner types--but fails for a genuinely geometric
reason: the two exceptional vertices of one wreath fall back into one
coordinate necklace.

Use the universal MSW \(C_8\) words

\[
 Q=(q_0,q_1,q_2,q_3,q_4,\ldots,q_{p-1}),
 \qquad
 R=(q_1,q_3,q_0,q_2,q_4,\ldots,q_{p-1}).
\tag{9.1}
\]

Let \(C_i=V_i(Q)\), \(D_i=V_i(R)\), and let \(C'_i,D'_i\) be the two
new rows in the universal switch.  As in the literal \(C_8\) theorem, the
owner types are

\[
 \begin{array}{c|cc}
 &i\in\{1,2,3\}&i\notin\{1,2,3\}\\ \hline
 C_i&(C,C')&(C,D')\\
 D_i&(D,D')&(D,C').
 \end{array}
\tag{9.2}
\]

Write \(\eta(q_j)=q_{j+1}\), and let

\[
 \rho=(q_0\ q_1\ q_3\ q_2).
\tag{9.3}
\]

Then \(R=\rho Q\), hence

\[
\rho\eta^s C_i=D_{i+s}.
\tag{9.4}
\]

### Lemma 9.0 -- the transposition perturbation is forced

Let \(H\) be a coordinate permutation which fixes pointwise all but two
vertices of one wreath packet \(\{V_i(R):i\in\mathbb Z_p\}\).  Then either
\(H\) is the identity, or the two exceptional row indices are consecutive
and \(H\) is the unique transposition of the two word positions at cyclic
distance two which distinguishes exactly those rows.

#### Proof

For a coordinate in word position \(a\), its incidence column across the
wreath vertices has support

\[
 I_a=\{a-1,a-3,\ldots,a-(p-2)\}\subseteq\mathbb Z_p.
\tag{9.4a}
\]

If \(b-a=2k\) modulo \(p\), with \(1\le k\le p-1\), then dividing the
row-index circle by the step two identifies \(I_a,I_b\) with two cyclic
intervals of length \(m\) at displacement \(k\).  Hence

\[
 |I_a\mathbin\triangle I_b|
 =2\min\{k,p-k,m,p-m\}
 =2\min\{k,p-k\}
\tag{9.4b}
\]

after choosing \(1\le k\le m\).  In particular distinct coordinate
columns can agree after deletion of two row coordinates only when their
word positions differ by \(2\) or \(-2\).  In that case their symmetric
difference is exactly one consecutive pair of row indices.

If \(H\) fixes every nonexceptional wreath vertex as a set, it may permute
only coordinates whose incidence columns agree outside the two exceptional
rows.  Every such equivalence class has size at most two: three word
positions cannot be pairwise at distance \(2\), since the two extremes
would be at distance \(4\) and have column difference four.  Moreover one
exceptional consecutive row pair determines a unique distance-two
coordinate pair.  Thus all coordinate classes are singletons except
possibly that one pair, proving the assertion. \(\square\)

Consequently the perturbation below is not merely a convenient guess.  If
a coordinate cycle \(\sigma\) satisfies

\[
 \sigma C_i=D_{i+s}
\]

for all but two fixed-index pairs, then
\(H=\sigma(\rho\eta^s)^{-1}\) fixes all but two \(D\)-vertices and Lemma
9.0 forces exactly the identity-or-transposition alternative.  The identity
is impossible because \(\rho\eta^s\) is odd whereas a \(p\)-cycle is even.

The obvious way to destroy exactly two of these \(p\) row pairings while
keeping a coordinate \(p\)-cycle is to put

\[
 g_s=\rho\eta^s,
 \qquad
 \sigma=h g_s,
\tag{9.5}
\]

where \(h\) is a transposition of two labels at cyclic distance two in
the word \(R\).  Such a transposition fixes exactly \(p-2\) vertices of
the wreath \(D\): if its positions are \(a,a+2\), the two moved wreath
vertices are

\[
E_D=\{a+1,a+2\}.
\tag{9.6}
\]

Indeed, the positions selected by \(V_i(R)\) are
\(i+1,i+3,\ldots,i+p-2\).  For the two positions \(a,a+2\), exactly one
is selected precisely when \(a-i\) is \(p-2\) or \(p-1\), which is
equivalent to \(i=a+2\) or \(i=a+1\).  On every other vertex the two
labels occur together or are both absent, so their transposition fixes the
set.

Consequently

\[
 \sigma C_i=D_{i+s}
 \quad\text{for every }i\notin E_D-s.
\tag{9.7}
\]

### Theorem 9.1 -- complete no-go for the one-transposition template

Assume \(p\ge7\) is prime.  Suppose (9.5) has all three properties:

1. \(h\) swaps two labels at distance two in \(R\), so (9.7) supplies
   exactly \(p-2\) intended pairings;
2. the two unpaired \(C\)-vertices and two unpaired \(D\)-vertices have
   the four owner types in (4.2), once each;
3. \(\sigma\) is a coordinate \(p\)-cycle.

Then one of the old rows is not transversal to the \(\sigma\)-necklace
partition.  Hence this template never realizes the legal \(p+2\)
length-four component of Theorem 4.1.

#### Proof

Put \(S=\{1,2,3\}\).  By (9.2), the two moved \(D\)-vertices have one
owner of each type precisely when

\[
 |E_D\cap S|=1.
\tag{9.8}
\]

The moved \(C\)-vertices are \(E_D-s\), so the analogous condition is

\[
 |(E_D-s)\cap S|=1.
\tag{9.9}
\]

Because \(E_D\) is a consecutive two-set, (9.8) says

\[
 E_D=\{0,1\}\quad\text{or}\quad E_D=\{3,4\}.
\tag{9.10}
\]

Apart from the trivial value \(s=0\), equations (9.9)--(9.10) force

\[
 \boxed{
 (s,E_D)=(3,\{3,4\})
 \quad\text{or}\quad
 (s,E_D)=(-3,\{0,1\}).}
\tag{9.11}
\]

For \(s=0\), the permutation \(g_0=\rho\) has one four-cycle and
\(p-4\) fixed points.  Multiplication by one transposition changes the
number of cycles by exactly one, so it cannot produce a \(p\)-cycle.

Consider the first case in (9.11).  Here

\[
 h=(q_0\ q_4).
\tag{9.12}
\]

If \(p=6r-1\), the two labels \(q_0,q_4\) lie in the same cycle of
\(g_3\); explicitly, that cycle begins

\[
 (0,2,5,\ldots,6r-4,1,4,7,\ldots,6r-2).
\]

Thus multiplying by \(h\) splits that cycle and cannot make a
\(p\)-cycle.  If \(p=6r+1\), the cycles of \(g_3\) are

\[
 \begin{aligned}
 &(0,2,5,\ldots,6r-1,3,6,\ldots,6r),\\
 &(1,4,7,\ldots,6r-2),
 \end{aligned}
\tag{9.13}
\]

in \(q\)-index notation.  Hence \(q_0,q_4\) lie in different cycles,
and \(\sigma=(q_0\ q_4)g_3\) is indeed one \(p\)-cycle.  Its cyclic
coordinate order is

\[
 \boxed{
 0,2,5,8,\ldots,6r-1,
 3,6,9,\ldots,6r,
 4,7,10,\ldots,6r-2,
 1.}
\tag{9.14}
\]

Nevertheless the two exceptional old vertices \(C_0,C_1\) belong to
the same \(\sigma\)-necklace.  More exactly,

\[
 \boxed{\sigma^{2r}C_0=C_1.}
\tag{9.15}
\]

Here is a direct verification.  Number the positions in (9.14) from
\(0\) to \(6r\).  Since

\[
 C_0=\{q_1,q_3,\ldots,q_{6r-1}\},
 \qquad
 C_1=\{q_2,q_4,\ldots,q_{6r}\},
\]

their position sets are respectively

\[
 \begin{aligned}
 P_0={}&\{6r\}
 \cup\{2,4,\ldots,2r\}
 \cup\{2r+1,2r+3,\ldots,4r-1\}\\
 &\cup\{4r+2,4r+4,\ldots,6r-2\},\\
 P_1={}&\{1,3,\ldots,2r-1\}
 \cup\{2r+2,2r+4,\ldots,4r\}\\
 &\cup\{4r+1,4r+3,\ldots,6r-1\}.
 \end{aligned}
\tag{9.16}
\]

Addition of \(2r\) modulo \(6r+1\) carries \(P_0\) onto \(P_1\),
which is (9.15).  Thus row \(C\) is not transversal.

The second case of (9.11) is the reflected calculation.  When
\(p=6r-1\), the relevant two labels again lie in one cycle of \(g_{-3}\),
so no \(p\)-cycle results.  When \(p=6r+1\), the transposition joins the
two cycles of \(g_{-3}\).  In this case its cyclic coordinate order is

\[
 \boxed{
 0,6r-2,6r-5,\ldots,4,
 6r,6r-3,6r-6,\ldots,6,
 2,3,1,
 6r-1,6r-4,\ldots,5.}
\tag{9.17}
\]

Directly reading the positions of
\(C_3=\{q_1,q_4,q_6,\ldots,q_{6r}\}\) and
\(C_4=\{q_0,q_2,q_5,q_7,\ldots,q_{6r-1}\}\) in this order gives

\[
 \boxed{\sigma^{-2r}C_3=C_4,}
\tag{9.18}
\]

the reflected counterpart of (9.16).  Again row \(C\) is nontransversal.  This exhausts
(9.11) and proves the theorem. \(\square\)

### Consequence 9.2

The universal \(C_8\) does not yield a legal \(p+2\) length-four phase
direction by any fixed-index ``almost packet translate'' having \(p-2\)
preserved row pairs.  Lemma 9.0 shows that every such construction reduces
to the distance-two transposition audited in Theorem 9.1.  The obstruction is sharper than failure of
the translate-disjointness amplitude: the proposed coordinate action
already identifies two vertices of one old row.

Therefore any successful length-four construction must use at least one
of the following genuinely new features:

1. a coordinate \(p\)-cycle not obtained by a one-transposition repair of
   \(\rho\eta^s\);
2. a two-for-two trade outside the universal one-block \(C_8\) normal
   form used in (9.1);
3. a larger cut number \(k\ge3\), so that the support matching is not the
   near-translate matching (9.7).

---

## 10. A compulsory repeated phase gap

The translate-disjointness requirement itself imposes one further sharp
constraint on every legal length-four component, independently of the
universal-\(C_8\) template.

### Proposition 10.1 -- triple repetition of an allowed gap

In a legal \(p+2\) necklace square, orient the \(p-2\) mass-two necklace
pairs and let

\[
 d_1,\ldots,d_{p-2}\in\mathbb F_p^*
\tag{10.1}
\]

be their phase differences.  If amplitude \(t\ne0\) satisfies
\(\mathcal U\cap\sigma^t\mathcal U=\varnothing\), then the unsigned gap
class \(\{t,-t\}\) is absent from the list.  Consequently the
\(2m-1=p-2\) phase pairs use at most \(m-1\) unsigned nonzero gap classes,
and some allowed unsigned class occurs at least three times.

#### Proof

Equation (4.7) says exactly that neither \(t\) nor \(-t\) occurs among the
oriented differences.  The \(p-1=2m\) nonzero field elements form \(m\)
unsigned classes \(\{d,-d\}\), so at most \(m-1\) classes remain.  Since

\[
 \left\lceil{2m-1\over m-1}\right\rceil=3,
\]

the pigeonhole principle proves the last assertion. \(\square\)

Thus a legal component is not merely a near-perfect quotient-support
overlap.  Its overlap must contain a repeated voltage class of multiplicity
at least three while omitting an entire unsigned class.  This is a useful
finite target for any future quotient-voltage classification.

---

## 11. Short-path run rigidity in the universal \(C_8\)

The three short vertices on each old row admit a second exact audit.  With
the notation of (5.2), split the common tail into

\[
 E=(t_0,t_2,\ldots,t_{2m-4}),
 \qquad
 O=(t_1,t_3,\ldots,t_{2m-5}).
\tag{11.1}
\]

Then

\[
 \begin{array}{lll}
 C_1=E\cup\{\gamma\},&
 C_2=O\cup\{\alpha,\delta\},&
 C_3=E\cup\{\beta\},\\
 D_1=E\cup\{\delta\},&
 D_2=O\cup\{\beta,\gamma\},&
 D_3=E\cup\{\alpha\}.
 \end{array}
\tag{11.2}
\]

### Lemma 11.1 -- translate overlap equals run count

Let \(S\subseteq\mathbb F_p\), \(|S|=m\), and let \(d\ne0\).  Read the
indicator of \(S\) around the coordinate cycle generated by \(d\).  If it
has \(r\) one-runs, then

\[
 \boxed{|S\cap(S+d)|=m-r.}
\tag{11.3}
\]

#### Proof

Every one-run has exactly one last point which exits \(S\) after
translation by \(d\), and these are all points of \(S\setminus(S-d)\).
Thus \(|S\setminus(S-d)|=r\), proving (11.3). \(\square\)

Consequently a short-pair necklace equality has one of exactly three run
profiles:

\[
 \begin{array}{c|c|c}
 \text{pair type}&\text{physical intersection}&
 \text{runs in the source at its phase gap}\\ \hline
 E+\text{one point}\leftrightarrow E+\text{one point}&m-1&1\\
 C_2\leftrightarrow D_2&m-2&2\\
 \text{one }E\text{-type and one }O\text{-type}&1&m-1.
 \end{array}
\tag{11.4}
\]

### Proposition 11.2 -- the two central short vertices cannot both be singletons

Assume \(m\ge3\).  In a legal necklace-square realization of the universal
\(C_8\), it is impossible for \(C_2\) and \(D_2\) to be the two unmatched
short vertices.

#### Proof

If \(C_2,D_2\) were unmatched, the two remaining short necklace pairs
would match

\[
 E\cup\{\gamma\},\ E\cup\{\beta\}
 \quad\text{to}\quad
 E\cup\{\delta\},\ E\cup\{\alpha\}
\tag{11.5}
\]

in one of the two possible bijections.  Each matched pair consists of two
translates with intersection \(E\) of size \(m-1\).  Lemma 11.1 says that
both members of such a pair are length-\(m\) cyclic intervals in the
coordinate cycle generated by their phase gap; their common core \(E\) is
therefore a length-\((m-1)\) arithmetic progression with the same step.

The step of an arithmetic progression \(E\), \(2\le|E|\le p-2\), is
unique up to sign.  Indeed, after scaling one representation to
\(E=\{0,1,\ldots,|E|-1\}\), the only nonzero translations \(x\) with
\(|E\cap(E+x)|=|E|-1\) are \(x=\pm1\).  Hence the two short pairs in
(11.5) use the same underlying cyclic order, up to reversal.

But a fixed length-\((m-1)\) cyclic interval has exactly two
length-\(m\) cyclic-interval extensions, obtained by adjoining its left or
right boundary point.  The four sets in (11.5) are distinct extensions of
the same \(E\), a contradiction. \(\square\)

Thus any surviving universal-\(C_8\) candidate must pair at least one of
\(C_2,D_2\).  Equivalently, its two short necklace pairs must contain
either the two-run central pair or at least one \((m-1)\)-run cross pair.
This is independent of the fixed-index no-go in Section 9.

---

## 12. Exact translate-deck correlation gate

There is a useful way to package every remaining non-near-translate
candidate.  For the two old rows \(A,C\), let \(f_A,f_C\) be their
middle-packet indicators and define

\[
 r_d=\langle \sigma^d f_A,f_C\rangle
 =\#\{X\in A:\sigma^dX\in C\}
 \qquad(d\in\mathbb F_p).
\tag{12.1}
\]

### Proposition 12.1 -- correlation ledger of a legal square

Every legal length-four \(p+2\) component satisfies

\[
 \boxed{
 r_0=r_t=r_{-t}=0,
 \qquad
 \sum_{d\in\mathbb F_p}r_d=p-2.}
\tag{12.2}
\]

Moreover the self-correlations are

\[
 \langle\sigma^df_A,f_A\rangle
 =\langle\sigma^df_C,f_C\rangle=0
 \qquad(d\ne0),
\tag{12.3}
\]

and the full translate decks

\[
 \mathscr D_A=\bigsqcup_{a\in\mathbb F_p}\sigma^aA,
 \qquad
 \mathscr D_C=\bigsqcup_{a\in\mathbb F_p}\sigma^aC
\tag{12.4}
\]

have

\[
 \boxed{
 |\mathscr D_A\cap\mathscr D_C|=p(p-2),
 \qquad
 |\mathscr D_A\setminus\mathscr D_C|
 =|\mathscr D_C\setminus\mathscr D_A|=2p.}
\tag{12.5}
\]

#### Proof

Transversality gives (12.3).  Each common necklace of the two rows has a
unique oriented phase difference and contributes one to exactly one
\(r_d\); there are \(p-2\) common necklaces.  Physical disjointness gives
\(r_0=0\), while translate-disjointness (4.3) gives
\(r_t=r_{-t}=0\).  Translating one common physical pair through the full
coordinate deck fills its entire necklace fiber of size \(p\), proving
the intersection count in (12.5).  Each deck has \(p^2\) vertices, giving
the two difference counts. \(\square\)

For the universal \(C_8\), the owner-square condition refines (12.1):
all cross-correlations between a short \(C\)-vertex and a long
\(D\)-vertex, or vice versa, must vanish over the entire translate deck.
Exactly two short-to-short and \(p-4\) long-to-long common necklaces remain.
Together with Proposition 11.2, this leaves only the following short
sectors:

1. one one-run pair and one \((m-1)\)-run cross pair;
2. one one-run pair and the two-run central pair;
3. two \((m-1)\)-run cross pairs.

The forbidden sector of two one-run pairs is exactly Proposition 11.2.

### Fourier form

Let

\[
 P_k={1\over p}\sum_{d\in\mathbb F_p}
       \zeta^{-kd}\sigma^d
\tag{12.6}
\]

be the character projection for the coordinate cycle.  Equations (12.3)
imply

\[
 \|P_kf_A\|_2=\|P_kf_C\|_2=1
 \qquad(k\in\mathbb F_p)
\tag{12.7}
\]

with the present unnormalized packet indicators, and

\[
 \boxed{
 \sum_d r_d\zeta^{kd}
 =p\langle P_kf_A,P_kf_C\rangle,
 \qquad
 \left|\sum_dr_d\zeta^{kd}\right|\le p.}
\tag{12.8}
\]

Thus the remaining object is equivalently a pair of wandering wreath
vectors whose cross-correlation has total mass \(p-2\), three prescribed
zeros \(0,\pm t\), the owner block-diagonal restriction, and the odd-graph
two-factor trade.  The harmonic inequalities alone do not contradict this
ledger; the missing input must use the odd-graph edge geometry.

---

## 13. Odd-edge rigidity eliminates the central-plus-one-run sector

The unique-voltage property of quotient odd-graph edges now rules out one
of the three sectors left by Proposition 11.2.

### Lemma 13.1 -- an edge-to-edge short matching has one phase gap

Suppose two adjacent vertices \(X,Y\) of one transversal wreath are paired
to two adjacent vertices \(X',Y'\) of another transversal wreath:

\[
 X'=\sigma^aX,
 \qquad
 Y'=\sigma^bY.
\tag{13.1}
\]

Then \(a=b\).

#### Proof

After translating by \(\sigma^{-a}\), the target edge says

\[
 X\cap\sigma^{b-a}Y=\varnothing.
\]

The old edge gives \(X\cap Y=\varnothing\).  Since \(X,Y\) lie in
distinct \(\sigma\)-necklaces, Proposition 22.5 of the prime-cycle
row-power theorem says that there is at most one disjointness voltage
between them.  Hence \(b-a=0\). \(\square\)

### Theorem 13.2 -- no central-plus-one-run short sector

In a legal universal-\(C_8\) necklace square, the two short pairs cannot
consist of the central pair \(C_2\leftrightarrow D_2\) and one one-run
pair.

#### Proof

First suppose the selected short edges are

\[
 C_2C_3\longmapsto D_2D_3,
\tag{13.2}
\]

so the pairs are \(C_2\leftrightarrow D_2\) and
\(C_3\leftrightarrow D_3\).  Lemma 13.1 gives one common phase gap; write
\(\tau=\sigma^d\).  Thus

\[
 \tau C_2=D_2,
 \qquad
 \tau C_3=D_3.
\tag{13.3}
\]

Now

\[
 C_3=E\cup\{\beta\},
 \qquad
 D_3=E\cup\{\alpha\},
\]

so \(|C_3\cap\tau C_3|=m-1\).  Lemma 11.1 makes \(C_3\) a single
length-\(m\) interval in the coordinate cycle generated by \(\tau\).
Moreover

\[
 C_3\setminus\tau C_3=\{\beta\},
 \qquad
 \tau C_3\setminus C_3=\{\alpha\}.
\tag{13.4}
\]

Thus \(\beta\) is the initial point of that interval and \(\alpha\) is
the next point after its terminal point.  The complement of \(C_3\) is a
length-\((m+1)\) interval beginning at \(\alpha\).  But

\[
 C_4=O\cup\{\gamma,\delta\}=C_3^c\setminus\{\alpha\}.
\tag{13.5}
\]

Therefore \(C_4\) is itself a length-\(m\) interval in the same
\(\tau\)-cycle.  Hence \(C_3,C_4\) belong to one \(\sigma\)-necklace,
contradicting transversality of row \(C\).

The other aligned short edge is

\[
 C_1C_2\longmapsto D_1D_2.
\]

Here the one-run pair is
\(C_1=E\cup\{\gamma\}\leftrightarrow
D_1=E\cup\{\delta\}\).  The same argument makes \(C_1\) an interval,
and

\[
 C_0=O\cup\{\alpha,\beta\}=C_1^c\setminus\{\delta\}
\]

is the adjacent length-\(m\) interval.  Thus \(C_0,C_1\) lie in one
necklace, again impossible.  These are the two possible
central-plus-one-run sectors. \(\square\)

### Corollary 13.3 -- only two short sectors remain

Every legal universal-\(C_8\) length-four component must have either

1. one one-run pair and one \((m-1)\)-run cross pair, in which one side's
   two selected short vertices are nonadjacent; or
2. two \((m-1)\)-run cross pairs, obtained by crossing two adjacent short
   edges.

Thus the two-one-run sector, the central-plus-one-run sector, and the
fixed-index near-translate sector are all rigorously closed.

---

## 14. A genuine non-near-translate seed for the two-cross sector

The final crossed short sector survives the local odd-edge audit.  In
fact it has a symbolic coordinate-cycle realization in every odd
dimension.

Write

\[
 E=(e_1,\ldots,e_{m-1}),
 \qquad
 O=(o_1,\ldots,o_{m-2}).
\tag{14.1}
\]

### Theorem 14.1 -- exact crossed-short coordinate cycle

For \(m\ge3\), the cyclic coordinate order

\[
 \boxed{
 \tau=(
 \gamma,\delta,e_1,o_1,\alpha,e_2,\beta,
 o_2,e_3,o_3,\ldots,o_{m-2},e_{m-1})}
\tag{14.2}
\]

(with nonexistent terms omitted) is a \(p\)-cycle satisfying

\[
 \boxed{
 \tau C_2=D_3,
 \qquad
 \tau C_3=D_2,
 \qquad
 \tau\gamma=\delta.}
\tag{14.3}
\]

Thus it maps the old short edge \(C_2C_3\) to the reversed target edge
\(D_3D_2\), and both short necklace pairs have the common phase gap one.

#### Proof

Recall

\[
 C_2=O\cup\{\alpha,\delta\},
 \quad
 C_3=E\cup\{\beta\},
 \quad
 D_3=E\cup\{\alpha\},
 \quad
 D_2=O\cup\{\beta,\gamma\}.
\]

Reading successors in (14.2), the elements of \(C_2\) have images

\[
 \delta\mapsto e_1,
 \qquad
 o_1\mapsto\alpha,
 \qquad
 \alpha\mapsto e_2,
 \qquad
 o_j\mapsto e_{j+1}\ (j\ge2).
\]

Their image set is exactly \(E\cup\{\alpha\}=D_3\).  Likewise

\[
 e_1\mapsto o_1,
 \qquad
 e_2\mapsto\beta,
 \qquad
 \beta\mapsto o_2
\]

when \(m\ge4\), while \(\beta\mapsto\gamma\) when \(m=3\); for the
remaining indices \(e_j\mapsto o_j\), and the final
\(e_{m-1}\mapsto\gamma\).  Hence
\(\tau C_3=O\cup\{\beta,\gamma\}=D_2\).  The first edge of (14.2) gives
\(\tau\gamma=\delta\). \(\square\)

### Exact color normal form

Put

\[
 X=C_2,qquad Y=C_3,qquad Z=\{\gamma\}.
\]

These three cells partition the coordinates.  Any coordinate cycle
realizing the crossed equations

\[
 \tau X=D_3,qquad \tau Y=D_2,qquad\tau Z=\{\delta\}
\tag{14.4}
\]

has the transition counts

\[
 \begin{array}{c|ccc}
 &X&Y&Z\\ \hline
 X&1&m-1&0\\
 Y&m-2&1&1\\
 Z&1&0&0.
 \end{array}
\tag{14.5}
\]

Consequently its cyclic color word contains exactly one \(XX\) edge,
exactly one \(YY\) edge, and the unique \(Z\) occurs in a segment
\(Y-Z-X\).  Conversely every labeled cyclic order with transition table
(14.5), with the unique \(XX\) target labeled \(\alpha\), the unique
\(YY\) target labeled \(\beta\), and the \(Z-X\) target labeled
\(\delta\), realizes (14.4).  Formula (14.2) is one explicit member of
this large family.

This is the first explicit non-near-translate length-four seed surviving
all short-path and odd-edge constraints.  It is not yet a legal
\(p+2\) packet: one must still prove, or arrange within the family
(14.5), that

1. both old rows are fully \(\tau\)-transversal;
2. exactly \(p-4\) long-to-long necklace pairs occur;
3. no short-to-long necklace collision occurs;
4. some nonzero amplitude is absent from the full phase-gap set.

Theorem 14.1 proves that none of these remaining issues can be replaced by
a local two-cross-edge impossibility theorem.

---

## 15. Every one-run short pairing is individually impossible

Theorem 13.2 used the second, central short pairing in order to put the
one-run pair on a common phase.  In fact the central pair is unnecessary:
one one-run pair alone already violates row transversality.  This closes
the entire one-run-plus-cross sector.

### Lemma 15.1 -- the opposite interval forced by a one-point slide

Let \(p=2m+1\), let \(\pi\) be a coordinate \(p\)-cycle, and let
\(X\) be an \(m\)-set such that

\[
 Y=\pi X,
 \qquad
 |X\cap Y|=m-1.
\tag{15.1}
\]

Write

\[
 \{u\}=X\setminus Y,
 \qquad
 \{v\}=Y\setminus X.
\tag{15.2}
\]

Then \(X\) is a consecutive length-\(m\) interval in the coordinate
cycle \(\pi\), and

\[
 \boxed{X^c\setminus\{v\}=\pi^{m+1}X.}
\tag{15.3}
\]

In particular \(X\), \(Y\), and \(X^c\setminus\{v\}\) all belong to
one \(\langle\pi\rangle\)-necklace.

#### Proof

By Lemma 11.1, (15.1) says that the binary word of \(X\) around the
\(\pi\)-cycle has exactly one one-run.  After choosing its initial point
to be \(u\),

\[
 X=\{u,\pi u,\ldots,\pi^{m-1}u\}.
\]

Equation (15.2) then gives \(v=\pi^m u\).  The complement of \(X\),
with this first complementary point removed, is

\[
 X^c\setminus\{v\}
 =\{\pi^{m+1}u,\ldots,\pi^{2m}u\}
 =\pi^{m+1}X.
\]
This is (15.3). \(\square\)

### Theorem 15.2 -- no one-run short necklace pair

In a legal universal-\(C_8\) necklace square, no phase pairing between a
short \(E\)-type vertex of row \(C\) and a short \(E\)-type vertex of
row \(D\) is possible.  Explicitly, none of

\[
 C_1\leftrightarrow D_1,
 \quad
 C_1\leftrightarrow D_3,
 \quad
 C_3\leftrightarrow D_1,
 \quad
 C_3\leftrightarrow D_3
\tag{15.4}
\]

can occur in the mass-two necklace matching.

#### Proof

Suppose \(\sigma^a C_i=D_j\) for one pair in (15.4).  The exponent
\(a\) is nonzero because the two displayed physical sets are distinct.
As \(p\) is prime, \(\pi=\sigma^a\) is again a coordinate \(p\)-cycle.
Every pair in (15.4) has intersection \(E\), of size \(m-1\), so Lemma
15.1 applies.

There are four cases.  The new point \(v=D_j\setminus C_i\) and the
forced opposite interval \(C_i^c\setminus\{v\}\) are

\[
\begin{array}{c|c|c}
 C_i\longmapsto D_j&v&C_i^c\setminus\{v\}\\ \hline
 C_1\longmapsto D_1&\delta&C_0\\
 C_1\longmapsto D_3&\alpha&D_4\\
 C_3\longmapsto D_1&\delta&D_0\\
 C_3\longmapsto D_3&\alpha&C_4.
\end{array}
\tag{15.5}
\]

For the first and fourth rows of (15.5), the source \(C_i\) and the
forced opposite interval are two distinct vertices of row \(C\) in one
\(\sigma\)-necklace.  For the second and third rows, the target
\(D_j=\pi C_i\) and the forced opposite interval are two distinct
vertices of row \(D\) in one \(\sigma\)-necklace.  Either conclusion
contradicts the required transversality of that wreath row. \(\square\)

### Corollary 15.3 -- the two-cross sector is the only survivor

Every legal universal-\(C_8\) length-four component must use two cross
pairs.  Up to reflection and exchange of the two factors, its short
matching is therefore

\[
 \boxed{C_2\leftrightarrow D_3,
 \qquad C_3\leftrightarrow D_2,}
\tag{15.6}
\]

the sector realized locally by Theorem 14.1.

Indeed Proposition 11.2 eliminates the two-one-run sector, Theorem 13.2
eliminates central-plus-one-run, and Theorem 15.2 now eliminates every
remaining one-run-plus-cross sector.  The only unresolved geometry is the
long completion of the two-cross seed.

### Remark 15.4 -- factorial freedom remains in the crossed seed

The construction (14.2) is not isolated.  Independently permute the
labels inside the ordered lists

\[
 E=(e_1,\ldots,e_{m-1}),
 \qquad
 O=(o_1,\ldots,o_{m-2})
\]

and insert them in the same slots of (14.2).  The successor-set proof of
Theorem 14.1 uses only membership in \(E\) and \(O\), so all

\[
 \boxed{(m-1)!(m-2)!}
\tag{15.7}
\]

labeled cycles still satisfy
\(\tau C_2=D_3\), \(\tau C_3=D_2\), and \(\tau\gamma=\delta\).
This is genuine deterministic completion freedom: the original long-row
tail order stays fixed while the coordinate cycle may reorder the two
tail parity classes.  The remaining task is to exploit this freedom to
obtain the required \(p-4\) long necklace pairs, row transversality, and
an omitted nonzero phase class simultaneously.

---

## 16. The fixed-reflection near-translate template is also impossible

Section 9 ruled out an almost-everywhere index-preserving identification
of the two universal rows.  The orientation-reversing analogue can be
closed more directly, using the short-sector classification.

### Theorem 16.1 -- no one-transposition perturbation of a reflected row map

Assume \(p\ge7\).  Suppose a coordinate permutation \(g\) identifies the
two complete wreath packets with reversed row index,

\[
 gC_i=D_{k-i}
 \qquad(i\in\mathbb Z_p),
\tag{16.1}
\]

and suppose

\[
 \sigma=hg
\tag{16.2}
\]

where \(h\) is a coordinate transposition which destroys exactly two of
the identifications (16.1).  Then \(\sigma\) cannot realize a legal
universal-\(C_8\) necklace square with the four owner types (4.2).

#### Proof

By Lemma 9.0, the two exceptional \(D\)-row indices form a consecutive
two-set; call it \(E_D\).  The exceptional \(C\)-row indices are

\[
 E_C=k-E_D.
\tag{16.3}
\]

Let \(S=\{1,2,3\}\) be the short block.  The four owner types require
exactly one exceptional short vertex on each row.  A consecutive two-set
meets \(S\) in exactly one point only when it is

\[
 \{0,1\}\quad\hbox{or}\quad\{3,4\}.
\tag{16.4}
\]

Requiring both \(E_D\) and \(E_C\) to lie in this two-element list gives
only

\[
 \begin{array}{c|c|c}
 k&E_D&E_C\\ \hline
 1&\{0,1\}&\{0,1\}\\
 4&\{0,1\}&\{3,4\}\\
 4&\{3,4\}&\{0,1\}\\
 7&\{3,4\}&\{3,4\}.
 \end{array}
\tag{16.5}
\]

For \(k=1\), the two nonexceptional short vertices \(C_2,C_3\) are
sent by (16.1) to \(D_{p-1},D_{p-2}\), which are long.  For \(k=7\),
the two nonexceptional short vertices \(C_1,C_2\) are sent to
\(D_6,D_5\), again long (also when \(p=7\), with indices read modulo
\(p\)).  Both cases contradict the exact short/long block-diagonal
correlation in Proposition 12.1.

For the first \(k=4\) line, the surviving short matching is

\[
 C_1\longmapsto D_3,
 \qquad
 C_2\longmapsto D_2;
\]

for the second it is

\[
 C_2\longmapsto D_2,
 \qquad
 C_3\longmapsto D_1.
\]

Each consists of the central pair and one one-run pair, already forbidden
by Theorem 13.2 (and the one-run pair alone is forbidden by Theorem
15.2).  This exhausts (16.5). \(\square\)

Thus neither an orientation-preserving nor an orientation-reversing
complete row identification, followed by one distance-two transposition,
can produce the required \(p-2\) necklace matches.  Any surviving
two-cross completion must distribute its long matches over genuinely
multiple phase gaps.

---

## 17. Exact prefix equations for the surviving long completion

The two-cross case can be expressed as a finite system of circular prefix
equalities.  This removes any ambiguity about what the remaining
``factorial label freedom'' has to achieve.

### Lemma 17.1 -- two wreaths through one oriented edge

Let \(X,Y\) be disjoint \(m\)-sets and let \(z\) be the remaining
coordinate.  Every wreath containing the oriented edge \(X,Y\) has an
edge-rooted coordinate word

\[
 (z,x_1,y_1,x_2,y_2,\ldots,x_m,y_m),
\tag{17.1}
\]

where \((x_1,\ldots,x_m)\) and \((y_1,\ldots,y_m)\) are orderings of
\(X\) and \(Y\).  Its vertices, starting with \(R_0=X,R_1=Y\), are

\[
 \begin{aligned}
 R_{2a}&=
 X\setminus\{x_1,\ldots,x_a\}
 \ \cup\ \{z,y_1,\ldots,y_{a-1}\},
 &&0\le a\le m,\\
 R_{2a+1}&=
 Y\setminus\{y_1,\ldots,y_a\}
 \ \cup\ \{x_1,\ldots,x_a\},
 &&0\le a\le m-1.
 \end{aligned}
\tag{17.2}
\]

Consequently, if a second wreath through the same oriented edge uses
orders \(x'_1,\ldots,x'_m\) and \(y'_1,\ldots,y'_m\), then the two
rooted vertices of index \(2a\) agree exactly when

\[
 \{x_1,\ldots,x_a\}=\{x'_1,\ldots,x'_a\},
 \qquad
 \{y_1,\ldots,y_{a-1}\}=\{y'_1,\ldots,y'_{a-1}\},
\tag{17.3}
\]

and those of index \(2a+1\) agree exactly when

\[
 \{x_1,\ldots,x_a\}=\{x'_1,\ldots,x'_a\},
 \qquad
 \{y_1,\ldots,y_a\}=\{y'_1,\ldots,y'_a\}.
\tag{17.4}
\]

#### Proof

The coordinate in position zero is omitted by the edge \(R_0R_1\);
the odd positions of (17.1) form \(X\), and the even positive positions
form \(Y\).  The recurrence

\[
 R_{i+2}=R_i\setminus\{w_{i+1}\}\cup\{w_i\}
\]

gives (17.2) by induction.  Since \(X,Y,\{z\}\) are disjoint, equality
in (17.2) separates into equality of the two displayed prefix sets,
giving (17.3)--(17.4). \(\square\)

### The crossed edge in prefix coordinates

Root row \(C\) at the oriented edge \(C_2,C_3\).  Its edge word is

\[
 \bigl(
 \gamma;
 \alpha,e_1,o_1,e_2,o_2,\ldots,
 e_{m-2},o_{m-2},e_{m-1},\delta,\beta
 \bigr),
\tag{17.5}
\]

or, separating the two sides of the edge,

\[
 x=(\alpha,o_1,\ldots,o_{m-2},\delta),
 \qquad
 y=(e_1,\ldots,e_{m-1},\beta).
\tag{17.6}
\]

Root row \(D\) at the reversed edge \(D_3,D_2\).  Reversing its cyclic
word gives

\[
 x'=(\alpha,e_{m-1},e_{m-2},\ldots,e_1),
 \qquad
 y'=(\beta,o_{m-2},o_{m-3},\ldots,o_1,\gamma),
\tag{17.7}
\]

with omitted coordinate \(\delta\).

Let \(\tau\) be any coordinate cycle satisfying the crossed equations
(14.3), and put

\[
 a_i=\tau x_i,
 \qquad
 b_i=\tau y_i.
\tag{17.8}
\]

Then \((a_1,\ldots,a_m)\) is an ordering of \(D_3\), and
\((b_1,\ldots,b_m)\) is an ordering of \(D_2\).  Lemma 17.1 gives the
following exact test for every additional *root-aligned* phase-one match:

\[
 \boxed{
 \tau C_{2+h}=D_{3-h}}
\tag{17.9}
\]

if and only if the appropriate prefix equalities (17.3) or (17.4) hold
between \((a,b)\) and \((x',y')\), according as \(h\) is even or odd.
The two forced short matches are the automatic cases \(h=0,1\).

The shared edge is isolated inside the two row cycles.  Indeed an
extension through \(D_3\) would require

\[
 \tau C_1=D_4,
\]

a short-to-long match, while an extension through \(D_2\) would require

\[
 \tau C_4=D_1,
\]

a long-to-short match.  Both are forbidden by the exact block-diagonal
correlation following Proposition 12.1.  Thus any further phase-one
matches detected by (17.9) form components disjoint from the short edge.

### The complete circular-set equations

For arbitrary phase gaps, let

\[
 \ell:\ [p]\longrightarrow\mathbb Z_p
\]

be the position map in the coordinate cycle \(\tau\), so that
\(\ell(\tau u)=\ell(u)+1\).  For a coordinate set \(S\), write
\(\ell(S)=\{\ell(s):s\in S\}\).  Put

\[
 E_a=\{e_1,\ldots,e_a\},
 \qquad
 O_a=\{o_1,\ldots,o_a\},
\tag{17.10}
\]

with empty prefixes allowed.  The long vertices are exactly

\[
 \begin{aligned}
 C_{4+2a}&=(O\setminus O_a)\cup E_a\cup\{\gamma,\delta\},
 &&0\le a\le m-2,\\
 C_{5+2a}&=(E\setminus E_{a+1})\cup O_a\cup\{\alpha,\beta\},
 &&0\le a\le m-3,\\
 D_{4+2a}&=(O\setminus O_a)\cup E_a\cup\{\beta,\delta\},
 &&0\le a\le m-2,\\
 D_{5+2a}&=(E\setminus E_{a+1})\cup O_a\cup\{\alpha,\gamma\},
 &&0\le a\le m-3.
 \end{aligned}
\tag{17.11}

Together with

\[
 C_0=O\cup\{\alpha,\beta\},
 \qquad
 D_0=O\cup\{\alpha,\gamma\},
\tag{17.12}
\]

these are all \(p-3\) long vertices on each row.

For any long indices \(i,j\), the exact necklace condition is

\[
 \boxed{
 C_i\text{ and }D_j\text{ share a }\tau\text{-necklace}
 \quad\Longleftrightarrow\quad
 \ell(D_j)=\ell(C_i)+d
 \text{ for a unique }d\in\mathbb Z_p.}
\tag{17.13}

Here uniqueness follows from transversality.  Substituting (17.11)--
(17.12) turns (17.13) into four explicit even/odd prefix-exchange systems.
For example, an even-to-even match is exactly

\[
 \boxed{
 \ell\bigl((O\setminus O_b)\cup E_b\cup\{\beta,\delta\}\bigr)
 =
 \ell\bigl((O\setminus O_a)\cup E_a\cup\{\gamma,\delta\}\bigr)+d.}
\tag{17.14}

The other three parity combinations are obtained by taking the
corresponding two lines of (17.11), with (17.12) supplying the endpoint
\(C_0,D_0\).

Equations (14.5) and (17.13)--(17.14) are an exact finite formulation of
the surviving completion problem: choose one labeled cyclic position map
whose color transitions are (14.5), choose a matching of all but one long
vertex on each side, and assign unique shifts \(d\) satisfying these set
equalities.  The assigned nonzero shifts must omit one unsigned class in
order to leave a legal amplitude.  No probabilistic independence of the
\(p-4\) equalities is justified; they are coupled through the single map
\(\ell\).

---

## 18. Exact phase moments of any completed necklace square

The circular-set equations have a useful global consequence.  The phase
gaps cannot be treated as independent labels: all of their power moments
are coupled to the four unmatched vertices.

For a coordinate set \(S\), define in the position field \(\mathbb F_p\)

\[
 M_r(S)=\sum_{x\in S}\ell(x)^r,
 \qquad r\ge0.
\tag{18.1}
\]

Thus \(M_0(S)=m\).  Suppose a completed necklace square matches

\[
 T_k=\tau^{d_k}S_k
 \qquad(1\le k\le p-2),
\tag{18.2}
\]

where the \(S_k\)'s are all vertices of row \(C\) except the two
singletons \(C^*_1,C^*_2\), and the \(T_k\)'s are all vertices of row
\(D\) except \(D^*_1,D^*_2\).

### Theorem 18.1 -- unmatched-vertex moment ledger

For every integer \(r\ge1\),

\[
 \boxed{
 \sum_{k=1}^{p-2}
 \sum_{s=0}^{r-1}
 {r\choose s}d_k^{\,r-s}M_s(S_k)
 =
 M_r(C^*_1)+M_r(C^*_2)
 -M_r(D^*_1)-M_r(D^*_2)}
\tag{18.3}
\]

in \(\mathbb F_p\).  In particular,

\[
 \boxed{
 m\sum_{k=1}^{p-2}d_k
 =M_1(C^*_1)+M_1(C^*_2)
  -M_1(D^*_1)-M_1(D^*_2),}
\tag{18.4}
\]

and

\[
 \boxed{
 2\sum_{k=1}^{p-2}d_kM_1(S_k)
 +m\sum_{k=1}^{p-2}d_k^2
 =M_2(C^*_1)+M_2(C^*_2)
  -M_2(D^*_1)-M_2(D^*_2).}
\tag{18.5}
\]

Since \(p=2m+1\), one may replace \(m^{-1}\) in (18.4) by \(-2\).

#### Proof

Translation in the position cycle gives

\[
 M_r(\tau^dS)
 =\sum_{x\in S}(\ell(x)+d)^r
 =\sum_{s=0}^r{r\choose s}d^{\,r-s}M_s(S).
\tag{18.6}
\]

Across every wreath row, each coordinate occurs in exactly \(m\) row
vertices.  Hence the full row moments agree:

\[
 \sum_{i\in\mathbb Z_p}M_r(C_i)
 =m\sum_{x\in\mathbb F_p}x^r
 =\sum_{j\in\mathbb Z_p}M_r(D_j).
\tag{18.7}
\]

Delete the two unmatched vertices on each side and use (18.2).  Moving
the matched source moments to the target side and applying (18.6) leaves
exactly (18.3).  The cases \(r=1,2\) are (18.4)--(18.5). \(\square\)

For one individual long pair, (18.4) specializes to a closed phase
formula.  If \(T=\tau^dS\), then

\[
 \boxed{d=-2\bigl(M_1(T)-M_1(S)\bigr).}
\tag{18.8}
\]

For example, for the even-to-even equality (17.14), put

\[
 H_a=M_1(E_a)-M_1(O_a).
\tag{18.9}
\]

Its phase is forced to be

\[
 \boxed{
 d=2\bigl(H_a-H_b+\ell(\gamma)-\ell(\beta)\bigr).}
\tag{18.10}
\]

Thus even before the full set equality is imposed, the phase labels are
deterministic functions of the prefix imbalances of the single cyclic
position map.  This is another precise reason that a product-of-marginal
entropy estimate does not give an existence obstruction for the
two-cross lane.

### Corollary 18.2 -- phase sum in the normalized two-cross sector

In the normalization

\[
 \tau C_2=D_3,
 \qquad
 \tau C_3=D_2,
 \qquad
 \tau\gamma=\delta,
\tag{18.11}
\]

the unmatched short vertices are \(C_1,D_1\).  Let \(C_u,D_v\) be the
unmatched long vertices, and let \(d_1,\ldots,d_{p-4}\) be the phases of
the long matches.  Then

\[
 \boxed{
 \sum_{k=1}^{p-4}d_k
 =2\bigl(M_1(D_v)-M_1(C_u)\bigr).}
\tag{18.12}
\]

#### Proof

The two short matches both have phase one.  Moreover

\[
 M_1(C_1)-M_1(D_1)
 =\ell(\gamma)-\ell(\delta)=-1.
\]

Substitute these facts and the two unmatched long vertices into (18.4):

\[
 m\left(2+\sum_{k=1}^{p-4}d_k\right)
 =-1+M_1(C_u)-M_1(D_v).
\]

Multiplication by \(m^{-1}=-2\), followed by cancellation of the two
short phases, gives (18.12). \(\square\)

Thus the total phase of all \(p-4\) long matches is fixed by only the two
unmatched long binary words.  Any proposed phase-gap multiset can be
rejected before checking the individual set equalities if it violates
(18.12).

If the oriented phase multiset has the smallest arithmetically possible
collision profile--namely, it uses every element of
\(\mathbb F_p\setminus\{0,t,-t\}\) once and has one additional copy of
the short phase (1)--then its long submultiset is

\[
 \bigl(\mathbb F_p\setminus\{0,t,-t\}\bigr)\setminus\{1\},
\]

whose sum is (-1).  Equation (18.12) then forces the sharp necessary
condition

\[
 \boxed{M_1(D_v)-M_1(C_u)=m.}
\tag{18.13}
\]

Failure of (18.13) therefore forces at least one additional phase omission
and one additional repeated phase beyond the unavoidable duplicate at the
crossed short edge.

---

## 19. Fixed-endpoint one-run cores are unique

The long prefix equations immediately exclude an almost-diagonal matching
of the two long blocks.

### Lemma 19.1 -- a one-point translate determines its core

Let \(u\ne v\) be coordinates and let \(K\) be an \((m-1)\)-set
disjoint from \(\{u,v\}\).  If

\[
 K\cup\{v\}=\tau^d(K\cup\{u\})
\tag{19.1}
\]

for a nonzero phase \(d\), then, in the position field,

\[
 \boxed{
 d=m^{-1}\bigl(\ell(v)-\ell(u)\bigr)
   =-2\bigl(\ell(v)-\ell(u)\bigr),}
\tag{19.2}
\]

and

\[
 \boxed{
 \ell(K)=
 \{\ell(u)+d,\ell(u)+2d,\ldots,
   \ell(u)+(m-1)d\}.}
\tag{19.3}
\]

Thus, for fixed ordered endpoints \((u,v)\), there is at most one possible
core \(K\).

#### Proof

The two (m)-sets in (19.1) have intersection (m-1).  Lemma 15.1
makes the source a consecutive length-(m) interval under translation by
(d).  Because (u) is the point removed and (v) the point added, its
ordered positions are

\[
 \ell(u),\ell(u)+d,\ldots,\ell(u)+(m-1)d,
\]

and \(\ell(v)=\ell(u)+md\).  This proves (19.2)--(19.3). \(\square\)

### Corollary 19.2 -- at most two diagonal long matches

In the surviving two-cross sector, among all same-index long pairs

\[
 C_i\leftrightarrow D_i,
\tag{19.4}
\]

there is at most one with even (i) and at most one with odd (i).

#### Proof

For (i=4+2a), formulas (17.11) give

\[
 \begin{aligned}
 C_i&=T_a\cup\{\delta,\gamma\},\\
 D_i&=T_a\cup\{\delta,\beta\},
 \end{aligned}
 \qquad
 T_a=(O\setminus O_a)\cup E_a.
\tag{19.5}
\]

This is Lemma 19.1 with fixed endpoints
\((u,v)=(\gamma,\beta)\) and core (K=T_a\cup\{\delta\}).
The cores (T_a\cup\{\delta\}) are pairwise distinct because each step
replaces (o_{a+1}) by (e_{a+1}).  Hence at most one even value of
(a) can satisfy the translate equation.

For (i=5+2a), write

\[
 U_a=(E\setminus E_{a+1})\cup O_a.
\]

Then

\[
 C_i=U_a\cup\{\alpha,\beta\},
 \qquad
 D_i=U_a\cup\{\alpha,\gamma\}.
\tag{19.6}
\]

Lemma 19.1 now has fixed endpoints
\((u,v)=(\beta,\gamma)\) and core (U_a\cup\{\alpha\}).  These cores
are again pairwise distinct.  Extend this prefix path one final step by

\[
 U_{m-2}=O.
\]

The corresponding cyclic endpoint is exactly

\[
 C_0=U_{m-2}\cup\{\alpha,\beta\},
 \qquad
 D_0=U_{m-2}\cup\{\alpha,\gamma\}.
\]

Its core is distinct from all earlier ones, so Lemma 19.1 also permits at
most one match in the odd family after (C_0,D_0) are included.  This
proves the assertion. \(\square\)

Since the completed square needs (p-4=2m-3) long matches, all but at
most two of them must therefore be off-diagonal in the natural long-path
indexing (or switch parity).  Together with Theorems 9.1 and 16.1, this
rules out every completion whose near-total overlap comes from a single
obvious row alignment.

---

## 20. Complete physical-overlap table for the long blocks

The two long paths admit a uniform indexing.  For (0le ale m-2),
put

\[
 T_a=(O\setminus O_a)\cup E_a,
 \qquad
 U_a=(E\setminus E_{a+1})\cup O_a.
\tag{20.1}
\]

Here (U_{m-2}=O).  Define

\[
 \begin{array}{ll}
 C^e_a=T_a\cup\{\gamma,\delta\},&
 D^e_a=T_a\cup\{\beta,\delta\},\\
 C^o_a=U_a\cup\{\alpha,\beta\},&
 D^o_a=U_a\cup\{\alpha,\gamma\}.
 \end{array}
\tag{20.2}
\]

The (e)-families are the vertices of index (4+2a).  For
(ale m-3), the (o)-families have index (5+2a), while
(C^o_{m-2}=C_0) and (D^o_{m-2}=D_0).

### Proposition 20.1 -- exact long intersection sizes

For (0le a,ble m-2),

\[
 \boxed{
 |C^e_a\cap D^e_b|
 =|C^o_a\cap D^o_b|
 =m-1-|a-b|.}
\tag{20.3}
\]

The cross-parity intersections are

\[
 \boxed{
 |C^e_a\cap D^o_b|
 =
 \begin{cases}
 b-a+1,&a\le b,\\
 a-b,&a\ge b+1,
 \end{cases}}
\tag{20.4}
\]

and

\[
 \boxed{
 |C^o_a\cap D^e_b|
 =
 \begin{cases}
 a-b+1,&b\le a,\\
 b-a,&b\ge a+1.
 \end{cases}}
\tag{20.5}
\]

#### Proof

Moving from (T_a) to (T_{a+1}) replaces (o_{a+1}) by
(e_{a+1}); the same statement, with the direction reversed, holds for
the (U_a)'s.  Hence

\[
 |T_a\cap T_b|=|U_a\cap U_b|=m-2-|a-b|.
\]

The same-parity special pairs have one common coordinate, proving
(20.3).

For (T_a\cap U_b), the common (E)-indices are
(b+2,ldots,a), and the common (O)-indices are
(a+1,ldots,b), with an empty range interpreted as zero.  Adding the
common special coordinate (gamma) gives (20.4).  Interchanging the
roles gives (20.5), whose common special coordinate is (eta).
\(\square\)

### Corollary 20.2 -- the only one-run long pairs

A long (C)-vertex and long (D)-vertex have physical intersection
(m-1) only in the following cases:

1. a same-family diagonal pair (C^e_a,D^e_a) or
   (C^o_a,D^o_a);
2. the two boundary pairs

   \[
   C^e_0=C_4\leftrightarrow D^o_{m-2}=D_0,
   \qquad
   C^o_{m-2}=C_0\leftrightarrow D^e_0=D_4.
   \tag{20.6}
   \]

The boundary pairs are impossible in a transversal necklace square.
Indeed, if (C_4) translates to (D_0), Lemma 15.1 makes

\[
 C_4^c\setminus\{\alpha\}=C_3
\]

a translate of (C_4), colliding inside row (C).  If (C_0)
translates to (D_4), it similarly makes

\[
 C_0^c\setminus\{\delta\}=C_1
\]

a translate of (C_0).

Consequently every legal long matching has at most the two diagonal
one-run pairs allowed by Corollary 19.2.  All of its other at least
(p-6) long pairs have run count at least two at their phase gap.

If the permitted even diagonal pair occurs, Lemma 19.1 fixes its phase as

\[
 d_e=-2\bigl(\ell(\beta)-\ell(\gamma)\bigr),
\]

while a permitted odd diagonal pair has phase

\[
 d_o=-d_e.
\]

Thus the two possible diagonal matches consume one common unsigned phase
class; they do not provide independent phase freedom.

---

## 21. Exact enumeration of all crossed-short coordinate cycles

The transition table (14.5) has a particularly simple complete
parameterization.  Normalize the cyclic position of \(\gamma\) to zero,
so the linear word after it has length (2m).

### Theorem 21.1 -- two doubled runs and nothing else

Every coordinate cycle satisfying

\[
 \tau C_2=D_3,
 \qquad
 \tau C_3=D_2,
 \qquad
 \tau\gamma=\delta
\tag{21.1}
\]

has a unique color word of the following form:

1. it begins with (Z,X) and ends with (Y,Z);
2. between the two occurrences of (Z), its (X,Y)-runs alternate,
   beginning with an (X)-run and ending with a (Y)-run;
3. there are (m-1) runs of each color;
4. exactly one (X)-run has length two, exactly one (Y)-run has
   length two, and every other run has length one.

Conversely every such labeled cyclic word satisfies (21.1) when

* the first (X) after (Z) is labeled \(\delta\);
* the second point of the doubled (X)-run is labeled \(\alpha\);
* the second point of the doubled (Y)-run is labeled \(\beta\);
* (Z) is labeled \(\gamma\);
* the remaining (X)-positions receive the labels of (O), and the
  remaining (Y)-positions receive the labels of (E).

Hence, after fixing the position of \(\gamma\), the number of labeled
coordinate cycles satisfying (21.1) is exactly

\[
 \boxed{(m-1)^2(m-2)!(m-1)!.}
\tag{21.2}
\]

#### Proof

Delete the unique (Z) from the cyclic color word.  The remaining linear
word begins in (X), ends in (Y), and contains (m) letters of each
color.  Table (14.5) says it has exactly one (XX) transition and one
(YY) transition.  Equivalently it has (m-1) runs of each color, with
one extra letter distributed inside one run of each color.  This proves
the four run statements.

There are (m-1) choices for the doubled (X)-run and independently
(m-1) choices for the doubled (Y)-run.  Once these are fixed, the
transition targets in (14.5) force the positions of
\(\delta,\alpha,\beta,\gamma\) exactly as stated.  The remaining labels
may be assigned to their color positions in ((m-2)!(m-1)!) ways.
The converse is precisely the transition-table converse following
(14.5). \(\square\)

Thus (21.2), not merely the subfamily (15.7), is the complete deterministic
search space for the last surviving short sector.  The long equations
(17.13) impose their constraints on two run-location parameters and two
independent label permutations.

---

## 22. Barycentric normalization removes all phase variables

There is a canonical representative of every coordinate necklace.  This
turns the long completion into literal equality of zero-sum sets.

For an (m)-set (S), viewed in the position field through \(\ell\),
put

\[
 c(S)=m^{-1}M_1(S)=-2M_1(S)
\tag{22.1}
\]

and define its centered signature

\[
 \boxed{
 \widehat S=\{\ell(x)-c(S):x\in S\}\subseteq\mathbb F_p.}
\tag{22.2}
\]

The elements of \(\widehat S\) sum to zero.

### Theorem 22.1 -- exact necklace signature

For any two (m)-sets (S,T),

\[
 \boxed{
 T=\tau^dS\text{ for some }d
 \quad\Longleftrightarrow\quad
 \widehat T=\widehat S.}
\tag{22.3}
\]

When this holds, the phase is uniquely

\[
 \boxed{d=c(T)-c(S).}
\tag{22.4}
\]

#### Proof

If \(T=\tau^dS\), then

\[
 M_1(T)=M_1(S)+md,
\]

so \(c(T)=c(S)+d\).  Subtracting the centers proves
\(\widehat T=\widehat S\).

Conversely, equality of the centered signatures gives

\[
 \ell(T)=\ell(S)+c(T)-c(S),
\]

which is exactly \(T=\tau^{c(T)-c(S)}S\).  Uniqueness follows because a
nonempty proper subset of \(\mathbb F_p\) has no nonzero translation
stabilizer. \(\square\)

### Corollary 22.2 -- the surviving completion is a deck intersection

For a crossed-short coordinate cycle from Theorem 21.1, form the two
centered long decks

\[
 \mathscr C_{m long}
 =\{\widehat{C_i}:i\text{ long}\},
 \qquad
 \mathscr D_{m long}
 =\{\widehat{D_j}:j\text{ long}\}.
\tag{22.5}
\]

Row transversality says that each deck is a set rather than a multiset.
The exact long-completion requirement is simply

\[
 \boxed{
 |\mathscr C_{m long}\cap\mathscr D_{m long}|=p-4.}
\tag{22.6}
\]

The two unmatched signatures on each side identify the unmatched long
vertices.  Every phase is then recovered from (22.4), and the amplitude
condition asks for an unsigned nonzero value absent from these recovered
differences together with the two short phases.

Thus the only remaining existence question is the following precise
stability problem:

> Can two prefix-exchange decks (17.11), placed on one of the
> ((m-1)^2(m-2)!(m-1)!) crossed coordinate cycles, have centered-signature
> overlap exactly (p-4) while each deck remains collision-free?

The fixed-index no-go theorems show that such an overlap, if it exists,
cannot come from one near-dihedral identification.  It must be a genuinely
off-diagonal equality of the centered prefix signatures.

---

## 23. Center recurrence along the two universal rows

The barycentric representatives also give an explicit voltage coordinate
on each quotient row.  Write

\[
 s_i=c(C_i),
 \qquad
 t_i=c(D_i),
 \qquad
 q_i=\ell(Q_i),
 \qquad
 r_i=\ell(R_i).
\tag{23.1}
\]

### Proposition 23.1 -- omitted coordinates are center midpoints

For every row edge,

\[
 \boxed{
 s_i+s_{i+1}=2q_i,
 \qquad
 t_i+t_{i+1}=2r_i.}
\tag{23.2}
\]

Consequently, because the universal words (Q,R) agree from coordinate
position four onward,

\[
 \boxed{
 t_{i+1}-s_{i+1}=-(t_i-s_i)
 \qquad(4\le i\le p-1).}
\tag{23.3}
\]

Thus the center difference of the same-index long vertices is one constant
on the even long family and its negative on the odd long family.

#### Proof

The adjacent (m)-sets (C_i,C_{i+1}) partition all coordinates except
the omitted word coordinate (Q_i).  Since the sum of all elements of
\(\mathbb F_p\) is zero,

\[
 M_1(C_i)+M_1(C_{i+1})+q_i=0.
\]

Multiplication by (m^{-1}=-2) gives the first identity in (23.2); the
second is identical.  Subtract the two recurrences and use (q_i=r_i)
for (i\ge4) to get (23.3). \(\square\)

In the normalized crossed sector, the constant in (23.3) is exactly

\[
 -2\bigl(\ell(\beta)-\ell(\gamma)\bigr),
\]

agreeing with the diagonal phases in Section 20.  Proposition 23.1 is the
explicit quotient-voltage form of the long-prefix problem: the signature
cycles \((\widehat C_i)\), \((\widehat D_i)\) must share all but two
vertices, while their lift centers evolve by the alternating affine
recurrences (23.2).

---

## 24. Complete hand obstruction at (p=7)

For (m=3), Theorem 21.1 leaves only four unlabeled color words and two
orders of the two (E)-labels.  The centered signatures rule out all
eight cycles before any long matching is considered.

Normalize

\[
 ell(\gamma)=0,
 \qquad
 ell(\delta)=1.
\]

Let (r_X,r_Y\in\{1,2\}) denote which of the two (X)-runs and which
of the two (Y)-runs is doubled.  The four coordinate patterns and their
forced collisions are

\[
\begin{array}{c|c|c}
(r_X,r_Y)&\text{coordinate word, with (E)-slots unlabeled}
&\text{equal centered signatures}\\ \hline
(1,1)&(\gamma,\delta,\alpha,E,\beta,o,E)
&\widehat C_0=\widehat C_4=\{3,5,6\}\\
(1,2)&(\gamma,\delta,\alpha,E,o,E,\beta)
&\widehat C_0=\widehat C_1=\{0,2,5\}\\
(2,1)&(\gamma,\delta,E,\beta,o,\alpha,E)
&\widehat C_2=\widehat C_3=\{0,3,4\}\\
(2,2)&(\gamma,\delta,E,o,\alpha,E,\beta)
&\widehat C_0=\widehat C_4=\{1,2,4\}.
\end{array}
\tag{24.1}
\]

The displayed equalities are unchanged when the two (E)-labels are
interchanged, because each listed pair either contains the entire
(E)-set or no (E)-label.  By Theorem 22.1, every row of (24.1) puts
two distinct vertices of row (C) in one coordinate necklace.

### Corollary 24.1

No legal universal-(C_8) length-four (p+2) component exists at
(p=7).

#### Proof

Sections 11, 13, and 15 reduce every candidate to the two-cross sector.
Theorem 21.1 enumerates that sector, and (24.1) violates transversality in
every case. \(\square\)

The obstruction is finite-dimensional: the table alone does not show that
the same collision persists when there are more than two (X)- and
(Y)-runs.  It does, however, validate the centered-deck criterion on the
first nontrivial prime and shows that the explicit seed of Theorem 14.1 is
strictly local there.

---

## 25. Explicit quotient-neighbor map on centered signatures

The centered signatures carry the quotient odd graph without any hidden
phase choices.  Let (Asubseteq\mathbb F_p) be an (m)-set with
zero sum.  For (z\notin A), define

\[
 \boxed{
 N_z(A)=igl(A^c\setminus\{z\}igr)-2z.}
\tag{25.1}
\]

### Proposition 25.1 -- all quotient neighbors and their voltage

The (m+1) quotient neighbors of (A) are exactly the sets (N_z(A)),
(z\notin A).  The unique relative phase from (A) to (N_z(A)) is

\[
 \boxed{2z.}
\tag{25.2}
\]

#### Proof

Represent (A) at center zero.  Its physical odd-graph neighbor obtained
by omitting (z\notin A) is

\[
 T=A^c\setminus\{z\}.
\]

Since the sum of the whole field is zero,

\[
 M_1(T)=-z,
 \qquad
 c(T)=m^{-1}(-z)=2z.
\]

Centering (T) gives (25.1), while its center gives the voltage (25.2).
Every physical neighbor is obtained from one of the (m+1) choices of
(z), and distinct choices have distinct omitted coordinates, proving
the assertion. \(\square\)

The edge labels reverse exactly:

\[
 \boxed{N_{-z}(N_z(A))=A.}
\tag{25.2a}
\]

Indeed, shifting the physical partition
(A\sqcup(A^c\setminus\{z\})\sqcup\{z\}) by (-2z) makes
(N_z(A)) the centered first endpoint and changes the omitted coordinate
to (-z).  For the lifted wreath rows considered here, the signed
voltages sum to zero because their physical lift itself closes; a general
quotient cycle need not have zero total voltage.

For row (C), let

\[
 A_i=\widehat C_i,
 \qquad
 z_i=\ell(Q_i)-s_i.
\tag{25.3}
\]

Then (23.2) is equivalent to the exact recursion

\[
 \boxed{
 A_{i+1}=N_{z_i}(A_i),
 \qquad
 s_{i+1}-s_i=2z_i.}
\tag{25.4}

The same equations hold for row (D).  Thus the last stability question
can be stated entirely inside the explicit graph (25.1): two length-(p)
cycles generated by (N_z)-moves share (p-2) vertices, their lifts use
the prescribed universal-(C_8) omitted-coordinate words, and their two
shared short vertices form the reversed edge fixed in Section 14.

Any reconstruction theorem must use more than the abstract vertex overlap:
it must exploit the (N_z) labels or the lift-center recurrence, since a
general graph can contain two cycles with (p-2) common vertices and
arbitrarily reordered common parts.

---

## 26. Arithmetic location of the one-point short self-collisions

The color word itself has (m-1) (X)-runs and (m-1) (Y)-runs.
This pins the only possible phases of a one-point collision inside row
(C).

### Lemma 26.1 -- a near-alternating interval has step (pm2/3)

Let (Ssubseteq\mathbb F_p), (|S|=m), have exactly (m-1) runs in
the ordinary (+1) cyclic order.  If (S) is a consecutive
length-(m) interval in the cyclic order generated by (d\ne0), then

\[
 \boxed{d\in\{2/3,-2/3\}.}
\tag{26.1}
\]

#### Proof

The run hypothesis and Lemma 11.1 give

\[
 |S\cap(S+1)|=1.
\]

After scaling by (d^{-1}), (S) becomes an ordinary interval of
length (m), while translation by (1) becomes translation by
(d^{-1}).  Two length-(m) intervals in a (2m+1) cycle intersect in
one point exactly when their unsigned displacement is (m-1).  Hence

\[
 d^{-1}=\pm(m-1).
\]

Since ((m-1)^{-1}=-2/3) in \(\mathbb F_p\), (26.1) follows.
\(\square\)

### Corollary 26.2 -- forced special positions

In the normalization \(\ell(\gamma)=0,\ell(\delta)=1\), the following
implications hold:

\[
 \boxed{
 \widehat C_1=\widehat C_3
 \quad\Longrightarrow\quad
 \ell(\beta)=1/3,}
\tag{26.2}
\]

\[
 \boxed{
 \widehat C_2=\widehat C_4
 \quad\Longrightarrow\quad
 \ell(\alpha)=1/3,}
\tag{26.3}
\]

and

\[
 \boxed{
 \widehat C_2=\widehat C_0
 \quad\Longrightarrow\quad
 \ell(\beta)=4/3,
 \quad
 \ell(\alpha)=2.}
\tag{26.4}

#### Proof

For (26.2), the physical replacement is

\[
 C_1=C_3\setminus\{\beta\}\cup\{0\}.
\]

Lemma 19.1 fixes its phase at (d=2\beta), while Lemma 26.1 gives
\(d=\pm2/3).  If \(\beta=-1/3\), the unique ordinary adjacent pair in
the resulting interval begins at \(\beta\).  But \(\beta\) is, by
Theorem 21.1, the second point of the doubled (Y)-run.  Hence only
\(\beta=1/3\) remains.  The same argument with

\[
 C_4=C_2\setminus\{\alpha\}\cup\{0\}
\]

proves (26.3).

Finally

\[
 C_0=C_2\setminus\{1\}\cup\{\beta\},
\]

so its phase is (d=-2(\beta-1)).  The choice (d=2/3) would make the
interval beginning at (1) contain (0=\gamma), impossible because
(C_2=X) is disjoint from (Z).  Thus (d=-2/3), giving
\(\beta=4/3\).  The unique ordinary adjacent pair of this interval is
then ((1,2)); its second point is the labeled target \(\alpha\) of the
unique (XX) transition, so \(\alpha=2\). \(\square\)

These are necessary, not sufficient, conditions.  They show that three
of the easiest row-transversality failures occupy only three exceptional
special-position patterns inside the full family of Theorem 21.1.

---

## 27. Conditional reconstruction from the quotient Johnson graph

For two coordinate necklaces define

\[
 d_\tau([S],[T])
 =\min_{d\in\mathbb F_p}|S\setminus\tau^dT|.
\tag{27.1}
\]

This is well defined on necklace classes.  On the signature deck of any
wreath row, the natural pairs

\[
 [C_i]\,[C_{i+2}]
\tag{27.2}
\]

have (d_\tau=1), because the physical sets already differ by one
coordinate.  Since step two generates \(\mathbb Z_p\), these natural
edges form one (p)-cycle on the deck.

Let (e_J(\mathscr R)) denote the number of additional (d_\tau=1)
edges induced by a collision-free row deck \(\mathscr R), beyond this
natural cycle.

### Theorem 27.1 -- every order break consumes a Johnson chord

Suppose two collision-free wreath decks \(\mathscr C,\mathscr D\) share
(p-2) signatures.  Identify their common vertices.  After deleting the
two unmatched vertices from the natural (C)-cycle, all but at most

\[
 \boxed{e_J(\mathscr D)}
\tag{27.3}
\]

of the remaining natural (C)-edges are natural (D)-edges.  In
particular the common-signature matching decomposes, in the natural
step-two orders, into at most

\[
 \boxed{4+e_J(\mathscr D)}
\tag{27.4}
\]

order-preserving or order-reversing path segments.  The symmetric bound
with (C,D) exchanged also holds.

#### Proof

A natural (C)-edge whose two endpoints are common signatures remains a
pair of necklace classes at quotient Johnson distance one when viewed
inside the (D)-deck.  It is therefore either a natural (D)-edge or
one of the (e_J(\mathscr D)) extra induced edges.  This proves (27.3).

Deleting two vertices from a cycle destroys at most four natural edges.
Every further failure of the common matching to follow a natural
(D)-edge is charged injectively to an extra (D)-chord.  Cutting the
natural (C)-cycle at these places gives at most (27.4) path segments.
On one connected segment the orientation cannot change: at an internal
vertex, the two distinct neighboring images must be the two distinct
natural neighbors in the (D)-cycle.  Hence each segment is consistently
order-preserving or order-reversing. \(\square\)

### Corollary 27.2 -- the exact missing stability input

If

\[
 e_J(\mathscr C)+e_J(\mathscr D)=O(1),
\tag{27.5}
\]

then some common natural path has linear length.  If the chord count is
(o(p)), some aligned path has length tending to infinity.

Theorem 27.1 makes the reconstruction strategy precise, but (27.5) is not
a consequence of row transversality.  An extra chord is an equality

\[
 |C_i\cap\tau^dC_j|=m-1
\tag{27.6}
\]

between two *distinct* necklace classes.  Lemma 26.1 concerns a set and
one of its own translates, so it does not bound (27.6).  Controlling
(e_J) is exactly a first-shadow codegree/rainbow statement for the
translate deck.  Thus intrinsic path reconstruction succeeds once that
new chord bound is supplied, but does not obtain the bound for free.

### Proposition 27.3 -- exact facet-collision charging

For an ((m-1))-set (K), center its position set using
((m-1)^{-1}), and denote its facet-necklace signature by
\(\widehat K_{m-1}\).  For a collision-free middle row deck
\(\mathscr C=\{[C_i]\}\), define the facet loads

\[
 \lambda(L)=#\{(i,x):x\in C_i,
 \ \widehat{C_i\setminus\{x\}}_{m-1}=L\}
\tag{27.7}
\]

and the factorial collision count

\[
 \mathcal E_1(\mathscr C)=\sum_L{\lambda(L)\choose2}.
\tag{27.8}
\]

Then

\[
 \boxed{
 p+e_J(\mathscr C)
 \le \mathcal E_1(\mathscr C).}
\tag{27.9}
\]

Consequently

\[
 \boxed{
 \mathcal E_1(\mathscr C)=p+o(p)
 \quad\Longrightarrow\quad
 e_J(\mathscr C)=o(p).}
\tag{27.10}
\]

#### Proof

Every natural edge ([C_i][C_{i+2}]) has the common physical facet

\[
 C_i\cap C_{i+2}.
\]

Thus its two facet occurrences have the same signature.  The (p)
natural edges give (p) distinct pairs of facet occurrences counted by
(27.8).

For every extra quotient-Johnson chord ([C_i][C_j]), choose a phase
(d) with

\[
 |C_i\cap\tau^dC_j|=m-1.
\]

Writing the intersection as

\[
 C_i\setminus\{x\}
 =\tau^d(C_j\setminus\{y\})
\]

gives another pair of equal facet signatures.  It is not one of the
natural occurrence pairs because the middle edge is extra.  Distinct
simple chords give distinct unordered pairs of middle owners, and hence
distinct pairs of facet occurrences after one witnessing phase is fixed.
All these pairs occur among the binomial pairs counted in (27.8), proving
(27.9). \(\square\)

Equation (27.9) identifies the precise obstruction to completing the
reconstruction argument.  A sublinear extra-chord theorem is already a
baseline-corrected first-shadow collision theorem for this one row's full
translate deck.  The middle-rank transversality hypothesis supplies no
such estimate by itself.

### Lemma 27.4 -- at most six two-run shifts

Assume (m\ge4).  For every (m)-set (S\subseteq\mathbb F_p),

\[
 \boxed{
 \#\{d\ne0:|S\cap(S+d)|\ge m-2\}\le6.}
\tag{27.11}
\]

#### Proof

Let

\[
 r(d)=|S\cap(S+d)|.
\]

Pollard's addition theorem, applied to (S+(-S)) with truncation
(t=m-3), gives

\[
 \sum_{d\in\mathbb F_p}\min\{m-3,r(d)\}
 \ge(m-3)(m+3)=m^2-9.
\tag{27.12}
\]

On the other hand (sum_dr(d)=m^2).  Hence

\[
 \sum_d(r(d)-(m-3))_+\le9.
\tag{27.13}
\]

The zero shift has (r(0)=m) and consumes three units of the right side.
Every nonzero shift counted in (27.11) consumes at least one further unit.
At most six such shifts remain. \(\square\)

### Proposition 27.5 -- phase changes on an aligned prefix edge

Suppose two consecutive vertices of a natural step-two path are matched
to consecutive vertices of the other natural step-two path:

\[
 D_j=\tau^aC_i,
 \qquad
 D_{j\mathbin\pm2}=\tau^bC_{i+2}.
\tag{27.14}
\]

If (a\ne b), then

\[
 \boxed{
 |C_{i+2}\cap\tau^{,b-a}C_{i+2}|\ge m-2.}
\tag{27.15}
\]

Thus the phase increment (b-a) belongs to a set of at most six nonzero
values determined by (C_{i+2}).

#### Proof

The natural pairs (C_i,C_{i+2}) and
(D_j,D_{j\mathbin\pm2}) each have intersection (m-1).  Translate the
second target equality in (27.14) by (	au^{-a}).  Then both
(C_{i+2}) and (	au^{b-a}C_{i+2}) are at Johnson distance one from
(C_i).  Their mutual Johnson distance is therefore at most two, which
is (27.15).  Lemma 27.4 supplies the final assertion. \(\square\)

The six-shift bound gives uniform local branching for any path-order
reconstruction.  It does not by itself bound the number of vertices at
which the phase changes, so it is not yet a proof of (e_J=o(p)).

### Proposition 27.6 -- general index-gap classification of a chord

Let (C_i,C_j) have natural step-two cyclic distance (k),
(1\le k\le m).  Thus

\[
 |C_i\cap C_j|=m-k.
\tag{27.16}
\]

If a quotient-Johnson chord is witnessed at phase (d),

\[
 |C_i\cap\tau^dC_j|=m-1,
\tag{27.17}
\]

then

\[
 \boxed{
 |C_j\cap\tau^dC_j|\ge m-k-1.}
\tag{27.18}
\]

Equivalently, (C_j) has at most (k+1) runs in the coordinate cycle
generated by (d).

Moreover, for (k\le m-3), a fixed (C_j) has at most

\[
 \boxed{(k+1)(k+2)}
\tag{27.19}
\]

nonzero phases which can witness a chord from an index at step-two
distance (k).

#### Proof

Both (C_j\cap C_i) and (	au^dC_j\cap C_i) lie inside (C_i).
Inclusion-exclusion inside this (m)-set gives

\[
 |C_j\cap\tau^dC_j|
 \ge(m-k)+(m-1)-m=m-k-1,
\]

which is (27.18); Lemma 11.1 gives the run statement.

For the count, apply Pollard's inequality as in Lemma 27.4 with

\[
 t=m-k-2.
\]

It yields

\[
 \sum_d(r(d)-t)_+
 \le m^2-t(2m-t)=(k+2)^2.
\]

The zero shift consumes (m-t=k+2) units.  Every nonzero shift
satisfying (27.18) consumes at least one, leaving at most

\[
 (k+2)^2-(k+2)=(k+1)(k+2)
\]

possible phases. \(\square\)

Thus short-index chords have uniformly bounded phase spectra: distance
one permits at most six nonzero phases, distance two at most twelve, and
so forth.  A counterfamily with linear (e_J), if it exists, must either
reuse these bounded spectra across linearly many vertices or place much of
its chord mass at growing index gaps.

---

## 28. An almost-transversal crossed row with linearly many extra chords

The hoped-for estimate \(e_J=o(p)\) cannot be obtained from the
near-alternating coordinate word plus an \(o(p)\) row-collision error.  The
following explicit family misses exact row transversality by only three
necklace identifications, but has a linear family of distance-one chords.

Put

\[
 B_i=\{i+1,i+3,\ldots,i+2m-1\}\subseteq\mathbb F_p,
 \qquad p=2m+1,
 \tag{28.1}
\]

and let \(\phi=(0\ 1)\) be the transposition of two adjacent coordinate
positions.  Define

\[
 A_i=\phi(B_i),\qquad D=\{0,1\}.
 \tag{28.2}
\]

The standard coordinate colour word is alternating away from its unique
\(Z\)-position.  Choose \(0,1\) to be an internal \(YX\)-pair.  Swapping
them creates exactly one doubled \(X\)-run and one doubled \(Y\)-run.
Consequently, after assigning the special labels as in Theorem 21.1,
(28.2) is the \(C\)-row position deck of a legitimate crossed-short
candidate.

### Theorem 28.1 -- exact collisions and a linear chord subdeck

Assume \(p\ge11\).  Then:

1. \(B_1\) contains neither \(0\) nor \(1\), while every other \(B_i\)
   contains exactly one of them.  Hence
   \[
   A_1=B_1,
   \qquad
   A_i=B_i\mathbin\triangle D\quad(i\ne1).
   \tag{28.3}
   \]
2. The complete list of distinct-row translate equalities is
   \[
   A_1=A_0-1=A_2+1,
   \qquad
   A_4=A_{-2}+2.
   \tag{28.4}
   \]
   Thus the \(p\) rows determine exactly \(p-3\) necklace classes.
3. For every \(i\notin\{1,2\}\),
   \[
   |A_i\cap(A_{i-1}+1)|=m-1.
   \tag{28.5}
   \]
4. If
   \[
   I=\mathbb F_p\setminus\{0,2,-2\},
   \tag{28.6}
   \]
   then \(\{[A_i]:i\in I\}\) is collision-free and contains at least
   \[
   \boxed{p-8}
   \tag{28.7}
   \]
   distinct extra quotient-Johnson edges between consecutive indices.

#### Proof

The sets \(B_i\) are the length-\(m\) intervals in the step-two cycle.
The two ordinary-adjacent points \(0,1\) are at step-two cyclic distance
\(m\), so no \(B_i\) contains both.  Since each point lies in \(m\) of
the \(p\) sets, exactly \(2m=p-1\) rows contain one of the two points.
Directly from (28.1), the exceptional row is \(B_1\).  This proves
(28.3).

We next classify translate collisions.  If \(i,j\ne1\), then

\[
 A_i=A_j+d
 \quad\Longleftrightarrow\quad
 B_i\mathbin\triangle B_{j+d}
   =D\mathbin\triangle(D+d).
 \tag{28.8}
\]

For later use, the small symmetric differences between the standard
rows are

\[
\begin{aligned}
 B_i\triangle B_{i+2}&=\{i,i+1\},\\
 B_i\triangle B_{i-2}&=\{i-2,i-1\},\\
 B_i\triangle B_{i+4}&=\{i,i+1,i+2,i+3\},\\
 B_i\triangle B_{i-4}&=\{i-4,i-3,i-2,i-1\}.
\end{aligned}
\tag{28.9}
\]

The right side of (28.8) has size zero for \(d=0\), size two for
\(d=\pm1\), and size four otherwise.  Also

\[
 |B_i\triangle B_k|=2\,\mathrm{dist}_{\langle2\rangle}(i,k),
 \tag{28.10}
\]

where the distance is measured in the step-two index cycle.  Therefore a
nontrivial solution of (28.8) must use one of the four differences in
(28.9).  For \(d=\pm1\), the right side is respectively \(\{0,2\}\) or
\(\{-1,1\}\), whereas every size-two set in (28.9) is an
ordinary-adjacent pair; hence there is no solution.  In the size-four
case, \(D\triangle(D+d)\) is the union of the two adjacent pairs
\(\{0,1\}\) and \(\{d,d+1\}\).  It is an ordinary interval of length
four only for \(d=\pm2\).  Substitution in (28.9) gives precisely

\[
 A_0=A_2+2,
 \qquad
 A_4=A_{-2}+2.
 \tag{28.11}
\]

It remains to compare the exceptional row with an affected row.  The
equality \(A_1=A_j+d\), \(j\ne1\), is equivalent to

\[
 B_1\triangle B_{j+d}=D+d.
 \tag{28.12}
\]

The right side is an adjacent pair, so (28.9) forces \(j+d=1\pm2\).
The two substitutions give exactly

\[
 A_1=A_2+1,
 \qquad
 A_1=A_0-1.
 \tag{28.13}
\]

Equations (28.11)--(28.13) prove the complete list (28.4), and hence
the count \(p-3\).

For \(i\notin\{1,2\}\), both rows in (28.5) are affected.  Translating
(28.3) gives

\[
 A_{i-1}+1=B_i\triangle(D+1),
\]

and consequently

\[
 A_i\triangle(A_{i-1}+1)
 =D\triangle(D+1)=\{0,2\}.
 \tag{28.14}
\]

Both sets have size \(m\), so (28.5) follows.  These are consecutive-index
edges, whereas the natural row edges have index difference two.

Finally, (28.4) shows that deleting the indices \(0,2,-2\) leaves one
representative of each necklace class.  Before deletion, (28.5) supplies
\(p-2\) consecutive-index chords.  Deleting three vertices destroys at
most six of them, leaving at least \(p-8\).  Injectivity on \(I\) implies
that none of the surviving consecutive-index pairs can coincide with a
natural index-difference-two pair.  They are therefore distinct extra
quotient-Johnson edges. \(\square\)

### Consequence 28.2 -- exact transversality is the whole remaining issue

Theorem 28.1 rules out any stability statement of the form

\[
 \text{near-alternating crossed word}
 +o(p)\text{ necklace collisions}
 \Longrightarrow e_J=o(p).
\]

Indeed, the left side holds with only three lost necklace classes, while
a collision-free subdeck of size \(p-3\) already has \(p-O(1)\) extra
chords.  A valid sublinear-chord theorem must therefore exploit the exact
full-row transversal condition, or additional compatibility with the
second row and the \(p-2\) common-signature deck.  Neither the local run
classification nor the prefix formulas alone can supply it.

---

## 29. Exact collision repair preserves the linear chord family

The three necklace identifications in Theorem 28.1 are not rigid.  Two
further transpositions inside the colour classes remove all of them while
changing only six row vertices.  Thus even *exact* one-row transversality
does not imply a sublinear extra-chord bound.

Retain the notation \(B_i\) of (28.1).  Choose the internal adjacent
\(YX\)-pair at positions \(0,1\), so that after applying
\(\phi=(0\ 1)\), the positions \(-2,2\) have colour \(Y\) and the
positions \(3,5\) have colour \(X\).  Put

\[
 \sigma=(-2\ 2),
 \qquad
 \rho=(3\ 5),
 \qquad
 \pi=\rho\sigma\phi,
 \qquad
 A_i=\pi(B_i).
 \tag{29.1}
\]

Both \(\sigma\) and \(\rho\) preserve the crossed colour word.  Hence
the word still has exactly one doubled \(X\)-run and one doubled
\(Y\)-run and is still an admissible crossed-short coordinate cycle.

### Theorem 29.1 -- a transversal crossed row with linear chord count

For every \(p=2m+1\ge31\), the \(p\) sets in (29.1) lie in pairwise
distinct translation necklaces.  Nevertheless

\[
 \boxed{e_J(\{[A_i]:i\in\mathbb F_p\})\ge p-12.}
 \tag{29.2}
\]

#### Proof

Start with \(A_i^0=\phi(B_i)\).  The transposition \(\sigma\) changes
exactly the four rows with indices

\[
 -1,0,1,2,
\]

and in each of them toggles the pair \(\{-2,2\}\).  The transposition
\(\rho\) changes exactly the two rows with indices

\[
 4,5,
\]

and toggles \(\{3,5\}\).  Thus \(A_i=A_i^0\) outside

\[
 \mathcal S=\{-1,0,1,2,4,5\}.
 \tag{29.3}
\]

For the six exceptional rows, write

\[
 A_i=B_i\triangle E_i,
 \qquad
 M_1(A_i)=M_1(B_i)+\Delta_i.
 \tag{29.4}
\]

Direct membership inspection gives the complete table

\[
\begin{array}{c|rrrrrr}
 i&-1&0&1&2&4&5\\ \hline
 \Delta_i&-3&3&-4&5&-1&1\\
 E_i
 &\{-2,0,1,2\}
 &\{-2,0,1,2\}
 &\{-2,2\}
 &\{-2,0,1,2\}
 &\{0,1,3,5\}
 &\{0,1,3,5\}.
\end{array}
\tag{29.5}
\]

Every nonexceptional row has

\[
 A_j=B_j\triangle D,
 \qquad D=\{0,1\}.
 \tag{29.6}
\]

We first exclude a collision between an exceptional and a
nonexceptional row.  Such an equality would have the form

\[
 B_i\triangle B_{j+d}=E_i\triangle(D+d).
 \tag{29.7}
\]

The left side is either empty or one ordinary interval of even length;
more precisely, if its step-two index distance is \(k\), it is an
ordinary interval of length \(2k\).  There are only three exceptional
sets on the right side of (29.7):

\[
 E^- =\{-2,0,1,2\},
 \quad E^0=\{-2,2\},
 \quad E^+=\{0,1,3,5\}.
 \tag{29.8}
\]

A direct adjacent-pair cancellation gives:

\[
\begin{array}{c|c}
 E&\{d:E\triangle(D+d)\text{ is one even interval}\}\\ \hline
 E^-&\{-2\}\\
 E^0&\varnothing\\
 E^+&\varnothing.
\end{array}
\tag{29.9}
\]

For \(E^-\) and \(d=-2\), the interval is
\(\{-1,0,1,2\}\).  Among the exceptional indices carrying \(E^-\),
namely \(-1,0,2\), its position agrees with a symmetric difference from
\(B_i\) only when \(i=-1\).  Equation (29.7) then forces \(j=5\), which
is itself exceptional.  Hence no exceptional--nonexceptional collision
exists.

It remains to compare the six exceptional rows with one another.  The
center of \(B_i\) is \(m+i\), while the center of \(A_i\) is

\[
 c(A_i)=m+i-2\Delta_i.
 \tag{29.10}
\]

Therefore an equality \(A_i=A_j+d\) has the unique possible phase

\[
 d=(i-j)-2(\Delta_i-\Delta_j).
 \tag{29.11}
\]

Put \(\delta=\Delta_i-\Delta_j\).  At this phase the standard-row part
of the equality is

\[
 B_i\triangle B_{i-2\delta},
 \tag{29.12}
\]

an interval of length \(2|\delta|\).  Since every \(E_i\) has size at
most four, pairs with \(|\delta|>4\) are impossible by cardinality.
For the remaining nine unordered pairs, substitution in (29.5) gives
the following table.  The last two columns are respectively the left
and right sides of the required equality.

\[
\begin{array}{c|r|r|l|l}
\{i,j\}&\delta&d
&B_i\triangle B_{i-2\delta}
&E_i\triangle(E_j+d)\\ \hline
\{-1,1\}&1&-4&[-3,-2]&\{-6,0,1,2\}\\
\{-1,4\}&-2&-1&[-1,2]&\{-2,-1,1,4\}\\
\{-1,5\}&-4&2&[-1,6]&\{-2,0,1,3,5,7\}\\
\{0,2\}&-2&2&[0,3]&\{-2,1,3,4\}\\
\{0,4\}&4&-12&[-8,-1]
 &\{-12,-11,-9,-7,-2,0,1,2\}\\
\{0,5\}&2&-9&[-4,-1]
 &\{-9,-8,-6,-4,-2,0,1,2\}\\
\{1,4\}&-3&3&[1,6]&\{-2,2,3,4,6,8\}\\
\{2,5\}&4&-11&[-6,1]
 &\{-11,-10,-8,-6,-2,0,1,2\}\\
\{4,5\}&-2&3&[4,7]&\{0,1,4,5,6,8\}.
\end{array}
\tag{29.13}
\]

Here \([a,b]\) denotes the full ordinary integer interval.  For
\(p\ge31\), all displayed residues are distinct exactly as written, and
no row of the table gives equality.  Thus no two exceptional rows
collide.

Finally, two nonexceptional rows have exactly the same position sets as
in Theorem 28.1.  The complete collision list (28.4) always involves at
least one member of \(\mathcal S\).  Hence there is no
nonexceptional--nonexceptional collision either.  The full deck is
therefore transversal.

For the chord count, whenever neither \(i\) nor \(i-1\) lies in
\(\mathcal S\), equation (28.14) remains valid:

\[
 |A_i\cap(A_{i-1}+1)|=m-1.
 \tag{29.14}
\]

Deleting six vertices from the consecutive-index cycle destroys at most
twelve such edges, so at least \(p-12\) survive.  Full transversality
implies that they are distinct quotient edges, and an index-difference-one
pair cannot equal a natural index-difference-two pair.  All are extra
Johnson chords, proving (29.2). \(\square\)

### Consequence 29.2 -- one-row reconstruction is false

There is no theorem of the form

\[
 \boxed{
 \text{crossed-short coordinate word}
 +\text{exact row transversality}
 \Longrightarrow e_J=o(p).}
\]

Theorem 29.1 supplies exact transversality with \(e_J=p-O(1)\).  Any
successful reconstruction of a universal \(C_8\) in the two-cross
sector must use compatibility with the *other* row and with the
\(p-2\) common-signature matching.  The intrinsic geometry of either
single row is insufficient.

---

## 30. One transposition suffices

The two-transposition repair in Section 29 can be sharpened.  One further
same-colour transposition repairs all three necklace identifications and
leaves all but seven consecutive-index chords.

Choose the internal `YX` pair at `0,1` sufficiently far from the unique
`Z` position that the alternating colour pattern is ordinary on
`[-4,2]`.  Put

\[
 \psi=(-4\ 2),\qquad
 \pi=\psi\phi,\qquad
 A_i'=\pi(B_i).                                               \tag{30.1}
\]

The positions `-4` and `2` belong to the same untouched parity class of
the alternating word.  They therefore have the same colour after
`phi=(0\ 1)`, so `psi` preserves the crossed `X/Y` word pointwise.

### Theorem 30.1 -- one-swap transversal repair

For every prime `p=2m+1>=23`, subject to the harmless deep-internal choice
above, the `p` sets `A_i'` lie in pairwise distinct translation
necklaces.  Moreover

\[
 \boxed{
 e_J(\{[A_i']:i\in\mathbb F_p\})\ge p-7.}                   \tag{30.2}
\]

#### Proof

The coordinates `-4` and `2` are three steps apart in the step-two
coordinate cycle.  A length-`m` step-two interval contains exactly one of
them precisely when one of its boundaries lies in the three intervening
steps.  Hence `psi` changes exactly the rows

\[
 R=\{-3,-2,-1,0,1,2\}.                                     \tag{30.3}
\]

It toggles the pair `P={-4,2}` in each of these six rows.  Since `psi` is
disjoint from the support of `phi`, equations (28.3) give

\[
 A_i'=B_i\mathbin\triangle F_i,qquad
 F_i=
 \begin{cases}
  P,&i=1,\\
  G:=\{-4,0,1,2\},&i\in R\setminus\{1\},\\
  D:=\{0,1\},&i\notin R.
 \end{cases}                                                \tag{30.4}
\]

In particular all old collisions (28.4) are broken.  In
`A_1=A_0-1` and `A_1=A_2+1`, the two sides are now toggled by `P` and by
`P-1` or `P+1`; in `A_4=A_{-2}+2`, only the row `-2` is toggled.

We classify possible new collisions.  Suppose

\[
                         A_i'=A_j'+d,qquad i\ne j.          \tag{30.5}
\]

Then

\[
 B_i\mathbin\triangle B_{j+d}
       =F_i\mathbin\triangle(F_j+d).                         \tag{30.6}
\]

If both `i,j` lie outside `R`, (30.5) is an old collision, but every
collision in (28.4) meets `R`.  Reverse (30.5) if necessary and assume
`i in R`.  The right side of (30.6) has at most eight elements, so
(28.10) shows that the step-two distance from `i` to `j+d` is at most
four.  Distance zero cannot occur: it would require
`F_i=F_j+(i-j)`, but the three possible defect types have respectively
cardinality/gap data `(2,1)`, `(2,6)`, and `(4;4,1,1)`, and no nonzero
translate stabilizes one of them.  We may therefore write

\[
 j+d=i+2t\quad\hbox{or}\quad j+d=i-2t,qquad1\le t\le4.
\]

The left side of (30.6) is respectively

\[
 J^+_{i,t}=\{i,i+1,\ldots,i+2t-1\},
 \qquad
 J^-_{i,t}=\{i-2t,\ldots,i-1\}.                              \tag{30.7}
\]

Thus `F_i triangle J^pm_(i,t)` must be a translate of one of the three
possible defect shapes `D,P,G`.  The complete endpoint check is

\[
\begin{array}{c|c}
i&\text{cases for which }F_i\triangle J^\pm_{i,t}
       \text{ is a translate of }D,P,\text{ or }G\\ \hline
-3&\varnothing\\
-2&\varnothing\\
-1&\varnothing\\
0 &(+,1):\quad F_0\triangle J^+_{0,1}=P\\
1&\varnothing\\
2 &(-,1):\quad F_2\triangle J^-_{2,1}=P.
\end{array}                                                  \tag{30.8}
\]

Here is a short audit of the finite check.  Up to translation, the three
defect sets have respectively the cyclic small-gap patterns

\[
                 D:(1),\qquad P:(6),\qquad G:(4,1,1).       \tag{30.9}
\]

For each of the six values of `i` in (30.8), cancel the points of `F_i`
lying in the interval (30.7).  Unless the resulting cardinality is two or
four it cannot be a defect translate; comparison of the small-gap pattern
then leaves exactly the two displayed cases.  All sets involved in this
two/four-point check have ordinary span at most nine.  For `p>=23` their
complementary cyclic gap is uniquely the large gap, so reduction modulo
`p` creates no extra case.

Neither survivor of (30.8) is consistent with the forced type of the
other row.  For `(i,+,t)=(0,+,1)`, one has `j+d=2`; equality with the
displayed unshifted `P` forces `d=0`, hence `j=2`, but `F_2=G`.  For
`(i,-,t)=(2,-,1)`, one gets `j+d=0`, again `d=0`, hence `j=0`, but
`F_0=G`.  This rules out (30.5) and proves transversality.

Finally, the consecutive-index chord (28.5) remains unchanged whenever
both endpoint indices avoid `R`.  The set of possibly destroyed chord
indices is exactly contained in

\[
 R\cup(R+1)=\{-3,-2,-1,0,1,2,3\}.                           \tag{30.10}
\]

The two original exceptional indices `1,2` already lie in this set, so at
least `p-7` consecutive-index chords survive.  Transversality makes these
quotient edges distinct, and an index-difference-one edge cannot equal a
natural index-difference-two edge.  They are all extra chords, proving
(30.2). \(\square\)

### Consequence 30.2

The failure of one-row reconstruction is stronger than Consequence 29.2:
one colour-preserving position transposition beyond the original cross
already gives a fully transversal row with `e_J=p-O(1)`.  Any valid
stability input must be genuinely two-row.

---

## 31. Bounded local repairs cannot satisfy the two-row overlap

Section 30 shows that a bounded local repair can make the source row
transversal while retaining a linear family of extra chords.  The target
row supplies the missing rigidity: if the repair stays bounded and is
separated from the special \(Z\)-frame, the two centered decks have only
bounded overlap.

Use the standard edge-rooted coordinate positions of (17.5), and after a
cyclic shift put the crossed internal \(YX\)-pair at positions \(0,1\).
Let

\[
 B_i=\{i+1,i+3,\ldots,i+2m-1\}.
 \tag{31.1}
\]

If the unique \(Z\)-position is \(z\), the reversed target edge word
(17.7) differs from the reflected source edge word by the four-cycle

\[
 \kappa_z=(z\ z-2\ z-1\ z+1).
 \tag{31.2}
\]

After harmless reversal and cyclic reindexing, the two physical row decks
in an arbitrary position map \(\pi\) are therefore

\[
 \mathcal C(\pi)=\{\pi B_i:i\in\mathbb F_p\},
 \qquad
 \mathcal D(\pi)=\{\pi\kappa_z B_i:i\in\mathbb F_p\}.
 \tag{31.3}
\]

### Lemma 31.1 -- the target-frame defect is generically one pair

For all but the three indices \(z-1,z,z+1\),

\[
 \boxed{
 \kappa_zB_i=B_i\triangle K_z,
 \qquad K_z=\{z-1,z\}.}
 \tag{31.4}
\]

#### Proof

Translate to \(z=0\).  In the step-two coordinate cycle the four support
points occur as the two adjacent pairs

\[
 (-2,0),\qquad(-1,1),
\]

on opposite sides of a length-\(m\) interval.  Directly from (31.1), the
three boundary rows have corrections

\[
 B_0\triangle\kappa_0B_0=\{-2,-1,0,1\},
\]

\[
 B_1\triangle\kappa_0B_1=\{-1,1\},
 \qquad
 B_{-1}\triangle\kappa_0B_{-1}=\{-2,0\}.
\]

Every other length-\(m\) step-two interval meets one of the two pairs in
the stable pattern, and applying \(\kappa_0\) toggles exactly
\(\{-1,0\}\).  Translating back by \(z\) proves (31.4). \(\square\)

Call a permutation \(\theta\) an \(L\)-local repair if its support lies
in a step-two interval of at most \(L\) positions and is disjoint from
both \(\{0,1\}\) and the four positions in (31.2).  Put

\[
 \phi=(0\ 1),
 \qquad
 \pi=\theta\phi.
 \tag{31.5}
\]

Assume also that the ordinary cyclic distance between the adjacent pairs
\(J_0=\{0,1\}\) and \(K_z\) is at least five.  This is the deep-internal
cross regime used in Section 30.

### Theorem 31.2 -- local two-row overlap is bounded

Suppose both row decks in (31.3) are transversal.  Then

\[
 \boxed{
 |\widehat{\mathcal C(\pi)}
   \cap\widehat{\mathcal D(\pi)}|
 \le 4L+9.}
 \tag{31.6}
\]

In particular no bounded local repair can have the required overlap
\(p-2\), or the long overlap \(p-4\), for all sufficiently large \(p\).

#### Proof

A length-\(m\) step-two interval is changed by \(\theta\) only if one of
its two boundaries cuts the step-two support interval of \(\theta\).
Thus at most \(2L\) row indices are affected by the repair.  The adjacent
transposition \(\phi\) has one exceptional row.  Consequently, outside a
set \(E_C\) of size at most \(2L+1\),

\[
 \pi B_i=B_i\triangle J_0.
 \tag{31.7}
\]

The supports of \(\theta\phi\) and \(\kappa_z\) are disjoint, so the
permutations commute.  Lemma 31.1 shows that outside a target exceptional
set \(E_D\) of size at most \(2L+4\),

\[
 \pi\kappa_zB_j
 =B_j\triangle J_0\triangle K_z.
 \tag{31.8}
\]

Consider a necklace match with \(i\notin E_C\) and \(j\notin E_D\):

\[
 \pi B_i=(\pi\kappa_zB_j)+d.
\]

Equations (31.7)--(31.8) give

\[
 B_i\triangle B_{j+d}
 =J_0\triangle J_d\triangle J_{z-1+d},
 \qquad J_a=\{a,a+1\}.
 \tag{31.9}
\]

Put \(a=z-1\), so \(K_z=J_a\).  The left side of (31.9) is either empty
or one ordinary cyclic interval of even length.  On the right are three
adjacent pairs whose starting points are \(0,d,a+d\).  Because the two
fixed pairs \(J_0,K_z\) are separated, the pairs with starts \(d,a+d\)
never meet.  If neither of them meets \(J_0\), the right
side has three components and cannot be an interval.  Hence

\[
 d\in\{0,\pm1,-a,-a\pm1\}.
 \tag{31.10}
\]

The separation assumption permits an immediate six-case check.  For
\(d=0\), the first two pairs cancel and the right side is \(J_a\).  For
\(d=-a=1-z\), the first and third pairs cancel and it is \(J_{-a}\).  In each
of the other four cases, the overlap of two adjacent pairs leaves two
points at distance two, while the third pair is separated; the result is
not one interval.  Thus only

\[
 d=0\quad\hbox{or}\quad d=1-z
 \tag{31.11}
\]

can occur.

For a prescribed adjacent pair \(J_a\), the equality

\[
 B_u\triangle B_v=J_a
\]

has only the two ordered solutions \((u,v)=(a,a+2)\) and
\((a+2,a)\).  Hence (31.11) supplies at most four generic--generic
necklace matches.

Every remaining match uses at least one exceptional row.  Since both
decks are transversal, the common-signature relation is a matching, so
the number of such matches is at most

\[
 |E_C|+|E_D|\le4L+5.
\]

Adding the four generic matches proves (31.6). \(\square\)

### Corollary 31.3 -- the Section 30 repair is not two-row compatible

The one-swap repair \(\pi=(-4\ 2)(0\ 1)\) has bounded \(L\).  If its
cross is chosen deep inside the alternating block, Theorem 31.2 gives
only \(O(1)\) common source--target signatures.  Thus its exact
transversality and \(p-7\) extra one-row chords cannot be promoted to a
universal-\(C_8\) necklace square.  Any surviving two-cross construction
must reorder coordinates on an unbounded scale, or place its essential
geometry at the special \(Z\)-frame.

### Corollary 31.4 -- a quantitative linear-span requirement

Under the separated-frame hypotheses of Theorem 31.2, the required full
overlap \(p-2\) forces

\[
 \boxed{L\ge {p-11\over4}.}
 \tag{31.12}
\]

Thus it is not enough that the number of repair moves tend slowly to
infinity: their step-two support span must already occupy a positive
fraction of the coordinate cycle.

#### Proof

Combine \(p-2\le4L+9\) with (31.6). \(\square\)

---

## 32. Pointwise centered-deck cancellation

The moment ledger of Section 18 can be strengthened before any phase
variables are introduced.  Near-total deck overlap forces an exact
pointwise identity between the centered incidence loads of the two rows.

For a family \(\mathscr A\) of centered signatures, put

\[
 \Lambda_{\mathscr A}(x)
 =\#\{S\in\mathscr A:x\in S\},
 \qquad x\in\mathbb F_p.
 \tag{32.1}
\]

### Theorem 32.1 -- unmatched signatures carry the whole load difference

Assume the two crossed rows are transversal and have the required two
short matches

\[
 \widehat C_2=\widehat D_3,
 \qquad
 \widehat C_3=\widehat D_2.
 \tag{32.2}
\]

If their long decks overlap in \(p-4\) signatures, and
\(C_u,D_v\) are the unique unmatched long vertices, then

\[
 \boxed{
 \Lambda_{\mathscr C_{\rm long}}(x)
 -\Lambda_{\mathscr D_{\rm long}}(x)
 =\mathbf1_{\widehat C_u}(x)-\mathbf1_{\widehat D_v}(x)
 \quad(x\in\mathbb F_p).}
 \tag{32.3}
\]

Equivalently, for the full decks,

\[
 \boxed{
 \Lambda_{\mathscr C}(x)-\Lambda_{\mathscr D}(x)
 =\mathbf1_{\widehat C_1}(x)+\mathbf1_{\widehat C_u}(x)
  -\mathbf1_{\widehat D_1}(x)-\mathbf1_{\widehat D_v}(x).}
 \tag{32.4}
\]

Consequently every legal completion satisfies

\[
 \|\Lambda_{\mathscr C_{\rm long}}
   -\Lambda_{\mathscr D_{\rm long}}\|_\infty\le1,
 \tag{32.5}
\]

\[
 \|\Lambda_{\mathscr C_{\rm long}}
   -\Lambda_{\mathscr D_{\rm long}}\|_1\le2m,
 \qquad
 \|\Lambda_{\mathscr C_{\rm long}}
   -\Lambda_{\mathscr D_{\rm long}}\|_2^2\le2m.
 \tag{32.6}
\]

#### Proof

Both long decks have size \(p-3\), are sets by transversality, and have a
common subset of size \(p-4\).  Cancel the common signatures in the two
formal sums of their indicator vectors.  Exactly
\(\widehat C_u\) and \(\widehat D_v\) remain, proving (32.3).
The two short equalities in (32.2) cancel in the same way; the only
unmatched short signatures are \(\widehat C_1,\widehat D_1\), proving
(32.4).  The bounds (32.5)--(32.6) follow from the difference of two
\(m\)-set indicators. \(\square\)

### Corollary 32.2 -- centered power-moment ledger without phases

For \(r\ge0\), define the translation-invariant centered moment

\[
 K_r(S)=\sum_{x\in S}(\ell(x)-c(S))^r
       =\sum_{x\in\widehat S}x^r.
 \tag{32.7}
\]

Then every legal completion satisfies

\[
 \boxed{
 \sum_{i\ {m long}}K_r(C_i)
 -\sum_{j\ {m long}}K_r(D_j)
 =K_r(C_u)-K_r(D_v).}
 \tag{32.8}
\]

For \(r=2\), writing \(s_i=c(C_i)\) and \(t_i=c(D_i)\), this becomes

\[
 \boxed{
 K_2(C_1)+K_2(C_u)-K_2(D_1)-K_2(D_v)
 =m\sum_{i\in\mathbb F_p}(t_i^2-s_i^2).}
 \tag{32.9}
\]

#### Proof

Multiply (32.3) by \(x^r\) and sum over \(x\) to obtain (32.8).
For the quadratic identity,

\[
 K_2(S)=M_2(S)-m c(S)^2.
\]

Across a full wreath row every coordinate occurs exactly \(m\) times,
so the full raw second-moment sums of rows \(C,D\) agree.  Therefore

\[
 \sum_iK_2(C_i)-\sum_iK_2(D_i)
 =m\sum_i(t_i^2-s_i^2).
\]

Use (32.2) to cancel the two matched short moments and (32.8) to cancel
the matched long moments.  The four unmatched terms give (32.9).
\(\square\)

Identity (32.3) is strictly stronger than any fixed finite list of scalar
moment equations.  It gives a direct test for every proposed global
reordering: after centering, the aggregate long-row load difference must
already be a single \(m\)-set exchange.  No choice of phase matching can
repair a violation of (32.5) or (32.6).

### Proposition 32.3 -- explicit alternating kernel for the quadratic test

Write

\[
 q_i=\ell(Q_i),\qquad r_i=\ell(R_i),
\]

with indices represented by \(0,1,\ldots,p-1\).  Put

\[
 \mathcal K(h)=(p-2h)(-1)^h
 \quad(0\le h<p),
 \tag{32.10}
\]

viewed in \(\mathbb F_p\), and extend it cyclically.  Then

\[
 \boxed{
 \sum_i(t_i^2-s_i^2)
 =\sum_{a,b\in\mathbb F_p}
   \bigl(r_ar_b-q_aq_b\bigr)\mathcal K(b-a).}
 \tag{32.11}
\]

In the crossed normalization

\[
 (q_0,q_1,q_2,q_3)=(1,B,0,A),
 \qquad
 (r_0,r_1,r_2,r_3)=(B,A,1,0),
 \tag{32.12}
\]

where \(A=\ell(\alpha)\), \(B=\ell(\beta)\), let

\[
 e=(B-1,A-B,1,-A,0,\ldots,0).
 \tag{32.13}
\]

For every \(b\ge4\), its convolution with the kernel is

\[
 \boxed{
 \sum_{a=0}^3e_a\mathcal K(b-a)
 =-2(-1)^b\bigl(2Bb-(2A+B+2)\bigr).}
 \tag{32.14}
\]

Hence the right side of the unmatched quadratic test (32.9) contains the
explicit global tail functional

\[
 \boxed{
 -4m\sum_{b=4}^{p-1}(-1)^b
 \bigl(2Bb-(2A+B+2)\bigr)q_b,}
 \tag{32.15}
\]

plus a boundary polynomial depending only on \(A,B\).

#### Proof

The center recurrence (23.2) has the unique odd-cycle inverse

\[
 s_i=\sum_{h=0}^{p-1}(-1)^h q_{i+h},
 \qquad
 t_i=\sum_{h=0}^{p-1}(-1)^h r_{i+h}.
 \tag{32.16}
\]

Indeed the two adjacent alternating sums cancel except for two copies of
\(q_i\), or \(r_i\).  The cyclic autocorrelation of the kernel
\((-1)^h\) is

\[
 \sum_{i=0}^{p-1}(-1)^i(-1)^{i+h\ ({\rm mod}\ p)}
 =(p-2h)(-1)^h=\mathcal K(h).
 \tag{32.17}
\]

Expanding the two squared norms in (32.16) proves (32.11).
Since \(r=q+e\), the difference is

\[
 2\sum_bq_b\sum_{a=0}^3e_a\mathcal K(b-a)
 +\sum_{a,b=0}^3e_ae_b\mathcal K(b-a).
 \tag{32.18}
\]

For \(b\ge4\), no residue wraps in \(b-a\), and

\[
 \mathcal K(b-a)=-2(-1)^{b-a}(b-a)
 \quad\hbox{in }\mathbb F_p.
\]

Now

\[
 \sum_{a=0}^3(-1)^ae_a=2B,
 \qquad
 \sum_{a=0}^3a(-1)^ae_a=2A+B+2.
\]

Substitution gives (32.14), and the factor two in (32.18), followed by
the factor \(m\) in (32.9), gives (32.15).  All omitted terms have
indices at most three and therefore form the asserted boundary
polynomial. \(\square\)

---

## 33. Every two-row completion creates a near-perfect radius-one self-matching

The relation between the universal rows is a four-coordinate cycle.  In
the edge-rooted position coordinates of Section 31,

\[
 D_j=\theta C_j,
 \qquad
 \theta=\pi\kappa_z\pi^{-1},
 \tag{33.1}
\]

where \(\theta\) is a four-cycle on coordinates.  Thus every target row
vertex differs from the same-index source vertex in at most two exchanged
coordinates; Lemma 31.1 makes this exactly one away from three indices.

### Theorem 33.1 -- near-perfect bounded-radius self-matching

Assume a legal two-cross completion.  Match each common target signature
\(\widehat D_j\) to its unique source signature \(\widehat C_{f(j)}\).
Then, for every matched index \(j\),

\[
 \boxed{
 d_\tau([C_{f(j)}],[C_j])\le2.}
 \tag{33.2}
\]

The partial map \(f\) has domain and image of size \(p-2\).  At most two
of its edges are loops.  In fact it contains at least \(p-7\) directed
edges of exact quotient distance one, and consequently at least

\[
 \boxed{{p-7\over2}}
 \tag{33.3}
\]

distinct unordered source-row pairs of exact quotient Johnson distance
one.  Every such pair admits a nonzero-phase witness
\[
 |C_i\cap\tau^dC_j|=m-1.
 \tag{33.4}
\]

#### Proof

For a matched target vertex there is a unique phase \(d_j\) such that

\[
 D_j=\tau^{d_j}C_{f(j)}.
\]

Using (33.1) and translating back gives

\[
 C_{f(j)}=\tau^{-d_j}\theta C_j.
\]

The four-cycle \(\theta\) changes membership only on its four-point
support.  Since the two sets have equal size, at most two support points
can leave, so

\[
 |\theta C_j\setminus C_j|\le2.
\]

Translation preserves Johnson distance, proving (33.2).  Put
\[
 r_j=|\theta C_j\setminus C_j|.
\]
Squarefreeness of the two source rows implies \(r_j\ne0\), and hence
\(1\le r_j\le2\).  Moreover Lemma 31.1 gives \(r_j=1\) outside its
three exceptional indices.  The actual matching phase \(-d_j\) is the
witness in (33.4) whenever \(r_j=1\).

The deck matching is injective on both sides because both rows are
transversal.  Corollary 19.2 permits at most one same-index match in each
long parity family; the crossed short matches are nonloops.  Thus there
are at most two loops altogether.  At most three further directed edges
have exceptional target index.  Every one of the remaining at least
\(p-7\) directed edges therefore has positive distance at most one, hence
exact distance one.  After loops are discarded, an
unordered pair \(\{i,j\}\) can support at most the two directed matching
edges \(i\to j\) and \(j\to i\).  They therefore determine at least
(33.3) unordered pairs, with their actual matching phases giving (33.4).
\(\square\)

### Corollary 33.2 -- a fixed full simplicial shadow has linear translated collisions

For one of the distance-one pairs supplied by (33.3), let

\[
 C_i=\tau^dC_j\quad\hbox{up to one exchanged coordinate}
\]

be one of the witnessing pairs, and put

\[
 L=C_i\cap\tau^dC_j.
\]

Then \(|L|=m-1\), while \(L\subseteq C_i\) and
\(\tau^{-d}L\subseteq C_j\) have the same centered
\((m-1)\)-shadow signature.  Distinct unordered owner pairs give
distinct pairs of shadow occurrences.  Hence the full simplicial
facet-occurrence deck contains at least \((p-7)/2\) translated collision
pairs forced solely by the putative component.

This does not itself contradict transversality at the middle rank: the
one-row construction of Section 30 already exhibits a linear radius-one
chord family.  It does show that every globally nonlocal completion left
open by Theorem 31.2 must retain a linear full-facet collision mechanism;
the near-total overlap cannot be hidden in large-radius geometry.

### Corollary 33.3 -- linear excess above the full simplicial-shadow baseline

For \(1\le r\le4\), let \(\lambda_r(L)\) count occurrences of the
centered \((m-r)\)-shadow signature \(L\) among all pairs

\[
 (i,K),\qquad K\in\binom{C_i}{m-r},
\]

and put

\[
 \mathcal E_r(\mathscr C)
 =\sum_L\binom{\lambda_r(L)}2.
 \tag{33.5}
\]

The phase-zero common-subset pairs inside one wreath row contribute the
exact baseline

\[
 \boxed{
 \mathcal B_r
 =p\sum_{k=1}^r\binom{m-k}{r-k}
 =p\binom{m}{r-1}.}
 \tag{33.6}
\]

Every legal two-cross completion forces

\[
 \boxed{
 \mathcal E_1(\mathscr C)-\mathcal B_1
 \ge {p-7\over2}.}
 \tag{33.7}
\]

#### Proof

Two row vertices whose step-two cyclic distance is \(k\) have physical
intersection size \(m-k\).  There are exactly \(p\) unordered owner pairs
at every distance \(1\le k\le m\).  Such a pair has

\[
 \binom{m-k}{m-r}=\binom{m-k}{r-k}
\]

common physical \((m-r)\)-subsets when \(k\le r\), and none when
\(k>r\).  These give distinct pairs of shadow occurrences with equal
centered signatures.  Summing over \(k\) gives the first expression in
(33.6); the second is the hockey-stick identity.

Now take the distinct unordered owner pairs supplied by (33.3).  For one
such pair \(\{i,j\}\), choose the nonzero phase \(d\) in (33.4)
with

\[
 |C_i\cap\tau^dC_j|=m-1.
\]

The phase is nonzero: phase zero would make the matched target vertex a
physical source-row vertex, contrary to squarefreeness of the two old
wreath rows.  The two shadow occurrences

\[
 C_i\cap\tau^dC_j\subset C_i,
 \qquad
 \tau^{-d}(C_i\cap\tau^dC_j)\subset C_j
\]

have equal centered signatures.  This occurrence pair is not one of the
phase-zero baseline pairs.  If it were, the two displayed subsets would
be the same physical set, invariant under the nonzero translation
\(\tau^d\); a nonempty proper subset of \(\mathbb F_p\) has no such
stabilizer.  Distinct unordered owner pairs give distinct occurrence
pairs.  Thus all pairs counted in (33.3) add to (33.5) beyond the complete
baseline (33.6), proving (33.7). \(\square\)

Unlike the raw collision count, (33.7) has already subtracted every
collision forced by physically common subsets of one wreath.  It is a
literal *full simplicial-shadow* excess tax of any putative \(p+2\)
component.  The chosen intersections need not be cyclic depth-\(r\)
intervals in row \(C\), so (33.7) is not by itself an MWB cyclic-shadow
energy bound.

---

## 34. The universal four-cycle forces a linear facet-energy excess

For the actual universal rows the radius-four conclusion collapses almost
entirely to radius one.

### Lemma 34.1 -- same-index physical distances

For every row index \(j\ne2\),

\[
 \boxed{|C_j\cap D_j|=m-1,}
 \tag{34.1}
\]

whereas

\[
 \boxed{|C_2\cap D_2|=m-2.}
 \tag{34.2}
\]

#### Proof

For the long vertices this is the diagonal case \(a=b\) of (20.3).
For the four short vertices, use

\[
\begin{array}{c|c|c}
j&C_j&D_j\\ \hline
0&O\cup\{\alpha,\beta\}&O\cup\{\alpha,\gamma\}\\
1&E\cup\{\gamma\}&E\cup\{\delta\}\\
2&O\cup\{\alpha,\delta\}&O\cup\{\beta,\gamma\}\\
3&E\cup\{\beta\}&E\cup\{\alpha\}.
\end{array}
\]

The displayed intersections have sizes \(m-1,m-1,m-2,m-1\),
respectively. \(\square\)

### Theorem 34.2 -- near-perfect nonzero-phase facet matching

Every legal two-cross completion determines at least

\[
 \boxed{{p-5\over2}}
 \tag{34.3}
\]

distinct unordered pairs of source-row owners \(\{i,j\}\) for which
there is a nonzero phase \(d\) satisfying

\[
 \boxed{|C_i\cap\tau^dC_j|=m-1.}
 \tag{34.4}
\]

#### Proof

Among the \(p-2\) matched target indices, \(D_1\) and one long target are
unmatched.  The exceptional target \(D_2\) is matched to \(C_3\) by the
forced crossed short edge.  Hence exactly \(p-3\) matched target indices
fall under (34.1).

For such an index \(j\), write

\[
 D_j=\tau^{d_j}C_{f(j)}.
\]

Combining this equality with (34.1) gives

\[
 |C_j\cap\tau^{d_j}C_{f(j)}|=m-1.
\]

The phase is nonzero because the physical source rows \(C,D\) are
disjoint.  At most two of the directed owner pairs are loops, by
Corollary 19.2.  After those are discarded, an unordered pair supports at
most two opposite directed matches.  Thus the remaining \(p-5\) directed
pairs yield at least (34.3) distinct unordered pairs. \(\square\)

### Corollary 34.3 -- exact excess above the physical facet baseline

Let \(\lambda_1(L)\) count centered \((m-1)\)-facet-signature
occurrences over all facets of all \(C_i\), and put

\[
 \mathcal E_1^{\rm full}(\mathscr C)
 =\sum_L\binom{\lambda_1(L)}2.
 \tag{34.5}
\]

Then every legal completion satisfies

\[
 \boxed{
 \mathcal E_1^{\rm full}(\mathscr C)
 \ge p+{p-5\over2}.}
 \tag{34.6}
\]

#### Proof

The \(p\) natural step-two owner pairs have one physically common facet
each, giving \(p\) distinct phase-zero occurrence pairs.  Every pair in
Theorem 34.2 supplies the two facet occurrences

\[
 C_i\cap\tau^dC_j\subset C_i,
 \qquad
 \tau^{-d}(C_i\cap\tau^dC_j)\subset C_j.
\]

They have equal centered signatures.  Because \(d\ne0\), this occurrence
pair is not a phase-zero common-facet pair: equality would make a proper
nonempty subset invariant under \(\tau^d\).  Distinct unordered owners
give distinct occurrence pairs.  Add the (34.3) new pairs to the physical
baseline. \(\square\)

This is stronger than the radius-pigeonhole bound (33.7), but its scope is
the same: it concerns all \(m\) facets of every middle vertex.  It does
not assert that the collided facet is the one designated by the cyclic
lower flag of that owner.

### Proposition 34.4 -- the canonical facet witnesses are almost all noncyclic

For \(j\ne2\), put

\[
                         K_j=C_j\cap D_j.                 \tag{34.7}
\]

Among all these \(p-1\) facets, at most four are cyclic length-
\((m-1)\) intervals of the source wreath \(C\).  Consequently the
\(\Omega(p)\) occurrence pairs constructed in Theorem 34.2 certify at
most four cyclic depth-one collisions by their actual matching phases.

#### Proof

The formulas (17.11)--(17.12), together with the four short rows displayed
in Lemma 34.1, show that

\[
 C_j\setminus D_j\in\{\beta,\gamma\}
 \qquad(j\ne2).                                          \tag{34.8}
\]

A facet of a cyclic middle interval is itself a cyclic interval of length
\(m-1\) exactly when the deleted coordinate is one of the two endpoints
of that middle interval.  In one wreath, a fixed coordinate is an endpoint
of exactly two middle intervals.  Hence deletion of \(\beta\) can be
cyclic for at most two indices, and deletion of \(\gamma\) for at most
two more.

For the matching edge based at \(D_j\), the facet occurrence used in
Theorem 34.2 on the \(C_j\)-side is precisely \(K_j\).  If it is not a
cyclic facet there, the produced pair is not a collision of the cyclic
depth-one deck, regardless of what happens at its translated
\(C_{f(j)}\)-side. \(\square\)

Proposition 34.4 does not prove that the two source owners have no *other*
phase realizing a cyclic-facet collision.  It proves that neither the
\(p-2\) matching nor the bounded-radius/full-shadow argument supplies
such a phase.  A new endpoint-alignment theorem would be required.
Pollard-type popular-difference bounds do not by themselves provide this:
they control how often translations intersect, whereas cyclicity here is
the pointwise condition that one of the two deleted special coordinates
occupy one of two row endpoints.  The present universal rows exhibit the
extreme separation explicitly--linear full-facet incidence supported on
only two deleted coordinates, but only \(O(1)\) endpoint incidences.
