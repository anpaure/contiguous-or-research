# GMM tight one-sided bands: multilevel contraction and the geodesic/return dichotomy

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Let

\[
 p=2m+1,\qquad
 \mathcal B_H=\bigcup_{j=0}^{H}\binom{[p]}{m-j},
 \qquad 2\le H\le m,
\]

and let \(\mathcal E\) be a GMM tight enumeration of this one-sided band.
Put

\[
 A_H=\sum_{\substack{0\le j\le H\\j\ {\rm even}}}
             \binom p{m-j},\qquad
 B_H=\sum_{\substack{0\le j\le H\\j\ {\rm odd}}}
             \binom p{m-j},\qquad
 W=\binom pm.                                      \tag{0.1}
\]

The parity class containing rank \(m\) is the larger one, and tightness
has the following exact local consequence:

* every consecutive pair of opposite parity differs in one coordinate;
* every consecutive pair in the smaller parity class is absent; and
* there are exactly \(A_H-B_H\) same-parity transitions in the larger
  class, each of Hamming distance two.

Expand every distance-two transition by a shortest two-edge cube path
inside the band.  Between consecutive rank-\(m\) vertices
\(X_i,X_{i+1}\), let

\[
 \ell_i=\text{number of expanded coordinate flips},\qquad
 d_i=d_J(X_i,X_{i+1}),
\]

and define the return excess

\[
                         \rho_i={\ell_i-2d_i\over2}\ge0.        \tag{0.2}
\]

Then:

1. the excursion is coordinate-simple, hence endpoint-geodesic, exactly
   when \(\rho_i=0\);
2. an endpoint geodesic requires \(d_i-1\) synthetic rank-\(m\) owners
   when \(d_i>1\); all of these collide with owners already listed by the
   tight enumeration; and
3. globally one has the exact conservation law

\[
 \boxed{
 \sum_{i=0}^{W-1}(d_i-1)
 +\sum_{i=0}^{W-1}\rho_i
 =A_H-W
 =\sum_{\substack{2\le j\le H\\j\ {\rm even}}}
       \binom p{m-j}.}                              \tag{0.3}
\]

In particular,

\[
 \boxed{
 \sum_i(d_i-1)+\sum_i\rho_i
 \ge\binom p{m-2}
 ={m(m-1)\over(m+2)(m+3)}W
 =(1-o(1))W.}                                      \tag{0.4}
\]

This is a literal positive-density obstruction to the proposed direct
multilevel contraction.  Excursion by excursion, one cannot
simultaneously have

\[
 \text{\(o(W)\) synthetic owner occurrences}
 \quad\text{and}\quad
 \text{\(o(W)\) erased/repeated flip mass}.          \tag{0.5}
\]

If the first term in (0.3) is large, geodesic contraction duplicates
\(\Omega(W)\) already-owned middle sets.  If the second is large, the
band chronology contains \(\Omega(W)\) cancelling toggle pairs and is not
a collection of literal geodesic flags.  Tightness fixes only their sum;
it supplies no upper bound for either defect.

There is a further distinction.  A coordinate-simple excursion gives
endpoint geodesic data.  Its actual lower vertices form one nested
deletion/addition flag only when, after expanding distance-two steps, its
rank word is unimodal: all downward flips precede all upward flips.
Tightness does not impose this condition.

Thus GMM Corollary 2 for the whole band does not produce a
\(W+o(W)\) literal \(H\)-safe owner word by contracting its lower
excursions.  The obstruction already appears for \(H=2\), before any
question of target collisions across distinct flags.  A positive theorem
would require a nonlocal reassignment of the synthetic middle owners,
not the direct contraction of one tight enumeration.

## 1. Equality structure of a tight band enumeration

The band is bipartite by rank parity.  Let \(A\) be the class containing
rank \(m\) and \(B\) the other class.  First,

\[
\begin{aligned}
 A_H-B_H
 &=\sum_{j=0}^{H}(-1)^j\binom p{m-j}\\
 &=\binom{p-1}{m}
   +(-1)^H\binom{p-1}{m-H-1}>0.                    \tag{1.1}
\end{aligned}
\]

Here \(\binom{p-1}{-1}=0\) when \(H=m\).

For odd \(H\), positivity follows because the first binomial coefficient
is strictly larger than the second; for even \(H\) it is immediate.
Hence \(A=A_H\) is the larger parity class.

In a cyclic enumeration, let:

* \(a\) be the number of opposite-parity consecutive pairs;
* \(b_A\) the number of same-parity pairs in \(A\); and
* \(b_B\) the number of same-parity pairs in \(B\).

Counting the two incidences at every vertex gives

\[
                         2A_H=a+2b_A,\qquad
                         2B_H=a+2b_B.               \tag{1.2}
\]

An opposite-parity pair has odd Hamming distance at least one.  A
same-parity pair of distinct vertices has even Hamming distance at least
two.  Therefore the total number of coordinate flips is at least

\[
                         a+2b_A+2b_B
                         =2A_H+2b_B.                \tag{1.3}
\]

By definition, a tight enumeration has total flip length

\[
 |\mathcal B_H|+(A_H-B_H)=2A_H.                    \tag{1.4}
\]

Equality in (1.3)--(1.4) proves:

\[
 \boxed{
 b_B=0,\qquad b_A=A_H-B_H,}                         \tag{1.5}
\]

and every local transition attains its minimum Hamming distance.

### Theorem 1.1 (exact tight-transition classification)

Every transition of \(\mathcal E\) is of exactly one of the following
types.

1. A cube edge between consecutive ranks.
2. A distance-two transition between vertices in the parity class of
   rank \(m\).  Its endpoint ranks are equal or differ by two.

There are exactly \(A_H-B_H\) transitions of the second type.  No
same-parity transition occurs in the other parity class.

This is all that tightness says locally.  It does not relate the
coordinate labels of different transitions.

## 2. Expanded excursions and endpoint distance

Expand a distance-two transition by toggling its two symmetric-difference
coordinates in an order which stays inside \(\mathcal B_H\).  Such an
order always exists:

* when the ranks differ by two, the order is monotone;
* at one rank, toggle first toward the interior of the band.

The expansion is used only as a labelled chronology; its intermediate
vertex may be another vertex already appearing in the enumeration.

List the rank-\(m\) vertices in cyclic order as

\[
                         X_0,X_1,\ldots,X_{W-1},X_0.
\]

The expanded segment from \(X_i\) to \(X_{i+1}\), with no internal listed
rank-\(m\) vertex, is its \(i\)-th lower excursion.  Let its coordinate
word be

\[
                         \lambda_{i,1},\ldots,\lambda_{i,\ell_i}.  \tag{2.1}
\]

Because the endpoints have equal rank, \(\ell_i\) is even.  A coordinate
belongs to \(X_i\triangle X_{i+1}\) exactly when its multiplicity in
(2.1) is odd.  Therefore

\[
                         2d_i=|X_i\triangle X_{i+1}|
                         \le\ell_i.                 \tag{2.2}
\]

### Theorem 2.1 (exact excursion-geodesic criterion)

The following are equivalent.

1. \(\rho_i=0\).
2. Every coordinate in (2.1) occurs exactly once.
3. The expanded excursion is a shortest cube path between its endpoints.
4. Its endpoint data consist of \(d_i\) distinct deletions and \(d_i\)
   distinct insertions, with no coordinate used on both sides.

Under these conditions, any pairing of the deletion and insertion labels
gives a Johnson geodesic of length \(d_i\) from \(X_i\) to \(X_{i+1}\),
and that geodesic is internally safe at every depth.

#### Proof

Every symmetric-difference coordinate has odd positive multiplicity, and
every other coordinate has even multiplicity.  The minimum possible total
multiplicity is therefore \(|X_i\triangle X_{i+1}|=2d_i\), attained
exactly when each symmetric-difference coordinate occurs once and no
other coordinate occurs.  This proves the equivalence.

In the equality case, all deletion and insertion labels are distinct.
Pairing them produces \(d_i\) one-coordinate exchanges, and no coordinate
can repeat in any subwindow. \(\square\)

The last geodesic is synthetic unless \(d_i=1\): its internal rank-\(m\)
vertices are not visits of the original tight enumeration.

## 3. When the excursion itself is a literal flag

Write a downward expanded flip as \(D\) and an upward flip as \(U\).
Every excursion has a balanced rank word of length \(2d_i+2\rho_i\) whose
proper prefixes have nonnegative depth below rank \(m\).

### Theorem 3.1 (literal nested-flag criterion)

An excursion itself is the down-and-up traversal of one geodesic nested
flag if and only if:

1. \(\rho_i=0\); and
2. its expanded rank word is
   \[
                            D^{d_i}U^{d_i}.          \tag{3.1}
   \]

#### Proof

A down-and-up nested flag deletes \(d_i\) distinct elements successively
and then inserts \(d_i\) distinct elements successively.  Hence it has
distinct labels and rank word (3.1).

Conversely, coordinate simplicity and (3.1) make the first half a strictly
nested deletion chain and the second half a strictly nested addition
chain between the same bottom and the endpoint. \(\square\)

A coordinate-simple Dyck word such as \(DDUDUU\) is endpoint-geodesic but
is not one literal nested flag in its original order.  Turning it into a
flag requires reordering lower vertices, which is an additional
unlicensed operation.

## 4. Exact global contraction identity

The excursions partition every transition of the cyclic enumeration.
After expanding the distance-two transitions, their total flip length is
the tight length:

\[
                         \sum_{i=0}^{W-1}\ell_i=2A_H.           \tag{4.1}
\]

By definition of \(\rho_i\),

\[
                         {\ell_i\over2}=d_i+\rho_i.
\]

Summing and subtracting the \(W\) compulsory endpoint-to-endpoint Johnson
steps gives

\[
\begin{aligned}
 A_H-W
 &=\sum_i(d_i-1)+\sum_i\rho_i\\
 &=\sum_{\substack{2\le j\le H\\j\ {\rm even}}}
       \binom p{m-j}.
\end{aligned}                                      \tag{4.2}
\]

This proves (0.3).

### Interpretation

Put

\[
                         G=\sum_i(d_i-1),\qquad
                         R=\sum_i\rho_i.             \tag{4.3}
\]

* \(G\) is the exact number of internal middle-owner occurrences needed
  to replace every endpoint jump by a Johnson geodesic.
* \(2R\) is the exact excess flip length erased when every excursion is
  replaced by a shortest endpoint path.

Since every rank-\(m\) set already occurs once among the \(X_i\)'s, all
\(G\) internal geodesic occurrences duplicate existing owners, counted
with multiplicity.  They cannot be inserted into a coefficient-one owner
word without deleting or rerouting the same number of original owner
occurrences.

For \(H\ge2\), equation (0.4) gives the dichotomy

\[
                         G\ge{1\over2}\binom p{m-2}
 \quad\text{or}\quad
                         R\ge{1\over2}\binom p{m-2}.             \tag{4.4}
\]

Thus direct excursion contraction has a positive-density defect in every
tight enumeration of the whole band.

## 5. Two literal local witnesses

The two sides of the dichotomy are both compatible with the local
tight-transition rules.

### 5.1 Geodesic excursion requiring a synthetic owner

Let \(|S|=m-2\), and use four coordinates outside \(S\).  The cube path

\[
 S12,\quad S2,\quad S,\quad S3,\quad S34            \tag{5.1}
\]

has flip word \(1,2,3,4\).  It lies in levels \(m,m-1,m-2,m-1,m\), is
coordinate-simple and unimodal, and its endpoints have Johnson distance
two.  Its contraction therefore needs one internal rank-\(m\) owner.
That owner is already present elsewhere in the tight enumeration.

### 5.2 Delayed return with adjacent endpoints

With the same core \(S\), the path

\[
 S12,\quad S2,\quad S,\quad S1,\quad S13            \tag{5.2}
\]

has flip word \(1,2,1,3\).  Its endpoints are Johnson adjacent, but
\(\rho_i=1\).  Endpoint contraction erases one cancelling return pair and
does not preserve the literal band chronology.

Both paths use only cube edges, so every one of their transitions is
locally compatible with tightness.

## 6. Delayed returns and \(H\)-safety

The aggregate \(R\) in (4.3) counts cancelling toggle pairs, not their
separation.  A return whose two occurrences are more than \(2H\) flips
apart need not spoil any one \(2H\)-window.  Therefore tightness does not
give either an upper or a lower bound on the number of locally bad
\(H\)-windows.

For one excursion, let \(\beta_H(i)\) be the minimum number of cuts in
its expanded word required so that every remaining piece has no repeated
coordinate in a \(2H\)-flip window.  Put

\[
                         \Beta_H=\sum_i\beta_H(i).               \tag{6.1}
\]

Then the standard radius-\(H\) reset interface has the exact necessary
chronology gate

\[
                         \Beta_H=o(W/H).            \tag{6.2}
\]

The value \(R\) alone does not imply or refute (6.2): it records how many
returns occur, while \(\Beta_H\) records their interval-hitting number.
No estimate for \(\Beta_H\) follows from GMM tightness.

This explains why (0.3) is a literal flag obstruction but not, by itself,
a theorem that every tight enumeration has a positive density of short
delayed returns.  The unconditional obstruction is the
owner/flag dichotomy \(G+R=A_H-W\).

## 7. Collision ledger after synthetic contraction

Suppose every coordinate-simple excursion is replaced by a chosen Johnson
geodesic.  At depth \(q\), its lower and upper targets have the usual
forms

\[
\begin{aligned}
 L_{i,t}^{q}
 &=Y_{i,t}\setminus
       \{\text{the next \(q\) deletion labels}\},\\
 U_{i,t}^{q}
 &=Y_{i,t}\cup
       \{\text{the next \(q\) insertion labels}\},
\end{aligned}                                      \tag{7.1}
\]

whenever the complete \(q\)-window stays in one coordinate-simple
geodesic.

Tightness controls none of:

1. whether synthetic owners from different excursions coincide;
2. whether they coincide with excursion endpoints other than their own;
3. whether the maps in (7.1) are injective;
4. whether their unions cover almost every target; or
5. whether one pairing of deletion/insertion labels works simultaneously
   through all depths.

The first collision is already unavoidable in the fixed top-owner
listing: every synthetic owner is one of the \(W\) owners listed
elsewhere.  Hence \(G\) is an exact occurrence-level collision count
before any shadow collision is considered.

## 8. Scope of the obstruction

The identity (0.3) rules out the following direct strategy:

1. take one GMM tight enumeration of the whole one-sided band;
2. keep its cyclic order of rank-\(m\) owners;
3. contract each lower excursion independently to a geodesic owner flag;
4. preserve all but \(o(W)\) literal band chronology; and
5. add only \(o(W)\) owner occurrences.

It does not rule out a global re-resolution which moves rank-\(m\) owners
between excursions and uses the synthetic occurrences to replace, rather
than duplicate, their original positions.  Such a construction would
have to solve a new global owner matching together with all-depth target
coverage.  Nothing in Corollary 2 supplies that matching.

## 9. Certified boundary

Proved:

1. the exact equality classification of all transitions in a tight
   one-sided-band enumeration;
2. the exact excursion-geodesic criterion \(\rho_i=0\);
3. the stricter literal nested-flag criterion;
4. the global conservation identity (0.3);
5. the positive-density lower bound (0.4);
6. the unavoidable synthetic-owner collision count \(G\); and
7. the exact distinction between aggregate return mass \(R\) and local
   \(H\)-window cut number \(\Beta_H\).

Not proved:

1. a positive-density lower bound on short delayed returns;
2. an estimate for \(\Beta_H\);
3. a global reassignment of synthetic middle owners;
4. near-complete lower or upper target coverage after reassignment; or
5. coefficient one.

The whole-band GMM tight enumeration therefore has an exact multilevel
contraction obstruction even though its two-level specialization remains
useful at depth one.
