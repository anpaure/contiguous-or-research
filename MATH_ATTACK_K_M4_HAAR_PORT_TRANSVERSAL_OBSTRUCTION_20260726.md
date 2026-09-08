# The two nonlocal Haar factors have an intrinsic port-transversal obstruction

Date: 2026-07-26

Method: pure finite mathematics; no search or computation.

## 0. Outcome

Let \(F^-\) and \(F^+\) be the two exact \(m=4\) factors in
`NONLOCAL_HAAR_M4.md`, obtained by adjoining respectively the four negative
or four positive rows to the ten common rows.

The corrected context interface is port-transversality, not ordinary
transversality.  With that correction, neither factor can be made into a
canonical \(\mathcal D_4\)-port-transversal factor by any combination of

1. a permutation of the nine labels;
2. a choice of the distinguished label \(\infty\);
3. a cyclic rooting of the individual wreaths; or
4. reversal of any wreath.

The obstruction is intrinsic.  First, port-transversality forces two labels
to be separated by the \(\infty\)-cut in every one of the fourteen cyclic
orders.  The common rows leave only two possible separator frames:

\[
 (\infty,\{a,b\})=(6,\{7,8\}),\qquad
 (\infty,\{a,b\})=(7,\{8,9\}).                 \tag{0.1}
\]

Here \(a\) is the label present in every canonical Dyck boundary and \(b\)
is the terminal local label, present in none.  In both surviving frames the
fourteen forced \(a\)-ports have the wrong point-degree multiset.  A
relabeled canonical \(\mathcal D_4\) family has degree multiset

\[
                 \boxed{14,9,9,7,7,5,5,0,0},              \tag{0.2}
\]

whereas the surviving forced port families and their opposite orientations
have respectively

\[
\begin{array}{c|c|c}
\infty& a&\text{degree multiset}\ \\ \hline
6&7&(14,9,7,7,7,6,6,0,0),\\
6&8&(14,8,8,7,7,7,5,0,0),\\
7&8&(14,9,8,8,7,5,5,0,0),\\
7&9&(14,9,9,7,6,6,5,0,0).
\end{array}                                                \tag{0.3}
\]

Thus none is a canonical Dyck family.

The positive factor does have an ordinary, unported \(\mathcal D_4\)
transversal after relabeling.  That apparent positive construction is an
exact illustration of why the port correction is essential: several of its
selected Dyck sets are interior vertices of the \(\infty\)-free Johnson
path.  It cannot be used by the corrected context-substitution theorem.

Consequently the recorded rank-four Haar factors cannot be context-lifted by
merely relabeling them, declaring an infinity, and rooting their existing
rows at the canonical hole boundaries.  A successful lift must alter the
endpoint routing, use auxiliary local paths/rows, or reproduce the
preparatory commutator and its completion inside a larger context.  This is
an obstruction to the direct port-substitution architecture, not to every
possible state-level context lift.

## 1. Canonical \(\mathcal D_4\) as an intrinsic frame

Let the eight core labels be linearly ordered

\[
                         x_1,x_2,\ldots,x_8,               \tag{1.1}
\]

and let \(\omega=\infty\) be the ninth label.  A four-subset with ordered
positions \(i_1<i_2<i_3<i_4\) is a Dyck boundary exactly when

\[
                         i_j\le 2j-1\qquad(1\le j\le4).    \tag{1.2}
\]

In particular every member contains \(a=x_1\), and no member contains either
\(b=x_8\) or \(\omega\).  Put

\[
 E_1=\{x_2,x_3\},\qquad E_2=\{x_4,x_5\},\qquad
 E_3=\{x_6,x_7\}.                                        \tag{1.3}
\]

Then every member of \(\mathcal D_4\) is \(\{a\}\cup T\), where the
occupancy vector

\[
 (|T\cap E_1|,|T\cap E_2|,|T\cap E_3|)                  \tag{1.4}
\]

is one of

\[
                         111,\quad120,\quad201,\quad210.   \tag{1.5}
\]

Their multiplicities are \(8,2,2,2\), giving the fourteen Catalan
boundaries.  Counting occurrences in (1.5) gives

\[
 d(a)=14,\quad d(E_1)=9,\quad d(E_2)=7,\quad d(E_3)=5,
 \quad d(b)=d(\omega)=0.                                  \tag{1.6}
\]

This proves (0.2).  Notice that internal order inside each pair \(E_i\)
does not change the family.  More importantly, any relabeling only permutes
the nine entries of the degree vector.  Hence (0.2) is an intrinsic
necessary condition for an affine canonical \(\mathcal D_4\) family.

At rank four this degree condition is also rigid.

### Lemma 1.1 (the canonical degree signature determines the frame)

Let \(\mathcal A\) be a family of fourteen distinct four-subsets on nine
labels.  Suppose one label \(a\) lies in all its members, two labels
\(b,\omega\) lie in none, and the other six point degrees are

\[
                         9,9,7,7,5,5.                       \tag{1.7}
\]

Then \(\mathcal A\) is an affine canonical \(\mathcal D_4\) family.  The
degree-nine, degree-seven, and degree-five pairs are respectively
\(E_1,E_2,E_3\).

#### Proof

Delete \(a\) from every member.  This gives fourteen distinct triples on
the six active labels.  Let \(\mathcal E\) be the six triples omitted from
the complete set of twenty triples.  Since every active label belongs to
ten triples in total, the degrees in \(\mathcal E\) are

\[
                         1,1,3,3,5,5.                       \tag{1.8}
\]

Call the two degree-five vertices \(h,h'\).  Each is absent from exactly
one of the six edges of \(\mathcal E\).  Those two missing edges are
distinct: if they coincided, the other five distinct triples would all
contain the pair \(hh'\), but only four triples on six vertices contain a
fixed pair.  Hence exactly four edges contain both \(h,h'\), and they must
be

\[
                         hh'x\qquad(x\notin\{h,h'\}).       \tag{1.9}
\]

Every other vertex now has degree one.  The remaining two edges contain
respectively \(h\) and \(h'\).  To raise exactly the two degree-three
vertices by two while leaving the two degree-one vertices unchanged, both
edges must use the same degree-three pair \(u,u'\).  Thus

\[
 \mathcal E=\{hh'x:x\notin\{h,h'\}\}\cup\{huu',h'uu'\}.   \tag{1.10}
\]

This is exactly the forbidden family complementary to (1.5), with
\(E_3=\{h,h'\}\), \(E_2=\{u,u'\}\), and \(E_1\) the remaining pair.
Therefore \(\mathcal A=\mathcal D_4\) in that frame. \(\square\)

For reference, in standard labels on the core the family is

\[
\begin{gathered}
1234,1235,1236,1237,1245,1246,1247,1256,1257,\\
1345,1346,1347,1356,1357.
\end{gathered}                                             \tag{1.11}
\]

## 2. The port-frame criterion

For an omitted-label order \(q=(q_0,\ldots,q_8)\), define its physical
middle-window cycle

\[
 p(q)=(q_0,q_2,q_4,q_6,q_8,q_1,q_3,q_5,q_7).              \tag{2.1}
\]

The sets \(I_i^{(4)}(q)\) are precisely the consecutive four-blocks of
\(p(q)\).  Fix a proposed infinity \(\omega\).  Let

\[
 H_q(\omega)=\{\text{the four entries immediately after \(\omega\) in
                         \(p(q)\)}\}.                       \tag{2.2}
\]

The two core ports of this wreath are

\[
 H_q(\omega),\qquad
 ([9]\setminus\{\omega\})\setminus H_q(\omega).           \tag{2.3}
\]

They are the two endpoints of the block of five middle windows avoiding
\(\omega\).

### Lemma 2.1 (universal separator necessity)

Suppose an exact fourteen-row factor is \(\mathcal D_4\)-port-transversal
for some relabeling.  Let \(a,b,\omega\) be the labels corresponding to
\(x_1,x_8,\infty\).  Then, for every row \(q\), exactly one of \(a,b\)
belongs to \(H_q(\omega)\).

Moreover, the member of \(\mathcal D_4\) owned by row \(q\) is forced: it is
the unique port in (2.3) containing \(a\).

#### Proof

Every Dyck boundary contains \(a\) and avoids \(b,\omega\).  Its row port
must therefore be the side of (2.3) containing \(a\), and \(b\) must lie on
the other side.  Conversely, once \(a,b,\omega\) are fixed and separated,
there is only one \(a\)-port in each row.  Exact factorhood makes the
fourteen forced ports distinct, because no middle set is owned by two rows.
Thus a port-transversal realization would force their family to equal the
fourteen-member \(\mathcal D_4\), not merely to meet it. \(\square\)

Together with Lemma 1.1 this gives an exact abstract rank-four test: after
choosing \(\omega,a\), form the fourteen forced \(a\)-ports.  They are a
canonical port transversal if and only if their degree multiset is (0.2),
with \(a\) of degree 14, \(\omega\) and one other label of degree zero.

For fixed \(\omega\), define the row-signature

\[
 \epsilon_\omega(x)
  =\bigl(\mathbf1_{\{x\in H_{C_i}(\omega)\}}\bigr)_{i=1}^{6}
  \in\{0,1\}^6,                                           \tag{2.4}
\]

using the first six common rows \(C_1,\ldots,C_6\) in the order displayed
in `NONLOCAL_HAAR_M4.md`.  Lemma 2.1 requires

\[
                         \epsilon_\omega(a)
                         =\mathbf1-\epsilon_\omega(b).     \tag{2.5}
\]

Rotation of a row does not change (2.3), and reversal merely exchanges its
two sides.  Therefore the complement relation (2.5) is invariant under all
row rootings and reversals.

## 3. Exhaustion of the possible separator frames

The following table is obtained directly by writing the first six physical
cycles (2.1).  Each entry is `label : six-bit signature`.

\[
\begin{array}{c|l}
\omega&\epsilon_\omega(x),\quad x\ne\omega\\ \hline
1&2:111010,\ 3:010111,\ 4:000001,\ 5:110100,\ 6:100111,\
   7:101011,\ 8:011100,\ 9:001000\\
2&1:000101,\ 3:101010,\ 4:111011,\ 5:001010,\ 6:011100,\
   7:010110,\ 8:100001,\ 9:110101\\
3&1:101000,\ 2:010101,\ 4:001110,\ 5:101011,\ 6:111000,\
   7:110100,\ 8:010011,\ 9:000111\\
4&1:111110,\ 2:000100,\ 3:110001,\ 5:010011,\ 6:000001,\
   7:001101,\ 8:111010,\ 9:101110\\
5&1:001011,\ 2:110101,\ 3:010100,\ 4:101100,\ 6:010010,\
   7:001000,\ 8:111011,\ 9:100111\\
6&1:011000,\ 2:100011,\ 3:000111,\ 4:111110,\ 5:101101,\
   7:110011,\ 8:001100,\ 9:010000\\
7&1:010100,\ 2:101001,\ 3:001011,\ 4:110010,\ 5:110111,\
   6:001100,\ 8:000100,\ 9:111011\\
8&1:100011,\ 2:011110,\ 3:101100,\ 4:000101,\ 5:000100,\
   6:110011,\ 7:111011,\ 9:011000\\
9&1:110111,\ 2:001010,\ 3:111000,\ 4:010001,\ 5:011000,\
   6:101111,\ 7:000100,\ 8:100111.
\end{array}                                                \tag{3.1}
\]

Reading off complementary strings gives the complete first-six-row list

\[
\begin{array}{c|c}
\omega&\{a,b\}\text{ allowed after }C_1,\ldots,C_6\\ \hline
1&\varnothing\\
2&\{5,9\}\\
3&\{6,9\}\\
4&\{1,6\}\\
5&\varnothing\\
6&\{7,8\}\\
7&\{8,9\}\\
8&\{5,7\}\\
9&\{5,8\}.
\end{array}                                                \tag{3.2}
\]

There is no hidden orientation choice in this table: complementarity is
unchanged if a row is reversed.

Now use the common physical cycles

\[
\begin{aligned}
p(C_7)&=(1,6,5,2,4,8,7,9,3),\\
p(C_8)&=(1,7,4,5,6,8,9,2,3).
\end{aligned}                                              \tag{3.3}
\]

For \(\omega=4\), the next-four side in \(C_7\) is
\(\{8,7,9,3\}\), which contains neither 1 nor 6; hence \(C_7\) kills
\((4,\{1,6\})\).  In \(C_8\), the next-four sides for
\(\omega=2,3,8,9\) are respectively

\[
 \{3,1,7,4\},\quad\{1,7,4,5\},\quad
 \{9,2,3,1\},\quad\{2,3,1,7\}.                           \tag{3.4}
\]

They put the corresponding pairs \(\{5,9\},\{6,9\},\{5,7\},\{5,8\}\)
on the same side and kill those four cases.  The two cases in (0.1) remain
separated in \(C_7,\ldots,C_{10}\) and in all four negative and all four
positive rows, as direct reading of their physical cycles shows.  Thus
(0.1) is the exhaustive list for both \(F^-\) and \(F^+\).

## 4. Degree obstruction in the two surviving frames

### 4.1. Infinity 6 and separator pair \(\{7,8\}\)

Choose \(a=7,b=8\).  For both \(F^-\) and \(F^+\), the fourteen forced
\(a\)-ports form the same family (the final four are merely assigned to
different trade rows):

\[
\begin{gathered}
2457,1479,2379,1279,2347,2357,1379,1457,3479,1247,\\
1579,3579,4579,2579.
\end{gathered}                                             \tag{4.1}
\]

Its degree vector in label order \(1,\ldots,9\) is

\[
                         (6,7,6,7,7,0,14,0,9),             \tag{4.2}
\]

whose sorted multiset is the first line of (0.3), not (0.2).

If \(a=8,b=7\), every selected port is the complement in
\([9]\setminus\{6\}\) of the corresponding port in (4.1).  Thus each
residual degree \(d\) becomes \(14-d\), while the new \(a\) has degree 14
and the new \(b\) has degree zero.  This gives the second line of (0.3),
again not canonical.

### 4.2. Infinity 7 and separator pair \(\{8,9\}\)

Choose \(a=8,b=9\).  The first ten forced ports, common to both factors,
are

\[
1368,2368,1458,1568,1268,1468,2458,4568,2568,2468.        \tag{4.3}
\]

For \(F^-\), the last four are

\[
                         2348,1248,1238,3468,              \tag{4.4-}
\]

whereas for \(F^+\) they are

\[
                         1348,1248,1238,3468.              \tag{4.4+}
\]

The degree vectors on the six residual labels \(1,2,3,4,5,6\) are

\[
 (7,8,5,8,5,9)\quad\text{for }F^-,\qquad
 (8,7,5,8,5,9)\quad\text{for }F^+.                        \tag{4.5}
\]

They have the same sorted multiset.  Adding degrees 14,0,0 for
\(a,b,\omega\) gives the third line of (0.3).  Complementing the ports and
interchanging \(a,b\) gives the fourth line.  Neither orientation has the
canonical signature.

### Theorem 4.1 (intrinsic rank-four obstruction)

Neither \(F^-\) nor \(F^+\) is a relabeled
\(\mathcal D_4\)-port-transversal exact factor for any choice of infinity
and any rooting or reversal of its wreaths.

#### Proof

Lemma 2.1 and Section 3 reduce every possible labeling to the four oriented
cases in (0.3).  Section 4 shows that the forced port family in each case
has a point-degree multiset different from the invariant canonical multiset
(0.2).  Relabeling can only permute degrees.  Rotation preserves each port
pair, while reversal swaps its two members and is already represented by
interchanging \(a,b\).  Therefore no omitted choice remains. \(\square\)

## 5. The ordinary-transversal false positive

It is useful to record why ordinary transversality would have produced the
wrong answer.  In \(F^+\), take

\[
 \omega=6,qquad
 (x_1,\ldots,x_8)=(1,8,9,2,3,5,7,4).                      \tag{5.1}
\]

Equivalently, the three Dyck pairs are

\[
 E_1=\{8,9\},\qquad E_2=\{2,3\},\qquad E_3=\{5,7\},       \tag{5.2}
\]

and the two degree-zero labels are 4 and 6.  The fourteen Dyck sets, listed
in their owner rows \(C_1,\ldots,C_{10},P_1,\ldots,P_4\), are

\[
\begin{array}{c|cccccccccccccc}
\text{row}&C_1&C_2&C_3&C_4&C_5&C_6&C_7&C_8&C_9&C_{10}&P_1&P_2&P_3&P_4\\ \hline
\text{set}&1389&1358&1789&1279&1589&1289&1379&1239&1258&1359&
1378&1278&1238&1259.
\end{array}                                                \tag{5.3}
\]

Thus the owner map is indeed bijective: (5.1) is a genuine ordinary
\(\mathcal D_4\) transversal.

It is not a port transversal.  If 6 is infinity, the two 6-ports in row
\(C_2\) are

\[
                         2358,\qquad1479,                  \tag{5.4}
\]

so its selected set 1358 is interior.  Swapping the two zero-degree roles
does not help: if 4 is infinity, the two 4-ports in row \(C_7\) are

\[
                         1256,\qquad3789,                  \tag{5.5}
\]

so its selected set 1379 is interior.  The global obstruction in Theorem
4.1 shows that no different affine frame repairs this endpoint failure.

## 6. Exact implication for context lifting

The corrected context-substitution theorem requires a unique canonical
Dyck set at a port of every local wreath.  The port condition is what makes
the \(\infty\)-avoiding core windows a Johnson geodesic

\[
                         P=X_0,\ldots,X_4=J\setminus P      \tag{6.1}
\]

with the prescribed canonical boundary states at its two endpoints.  An
interior Dyck set such as (5.4) cannot be made the endpoint of this fixed
geodesic by rotating or reversing the row.

Theorem 4.1 therefore rules out the following literal lift:

1. take either completed rank-four Haar factor unchanged;
2. relabel its coordinates and choose one as infinity;
3. root each existing wreath at its unique canonical Dyck owner; and
4. insert those rooted traces into an aligned canonical size-four hole.

This failure applies separately to both sides, so the four-for-four Haar
trade cannot be imported as a boundary-fixed local factor pair by that
procedure.  In particular, ordinary middle-owner transversality and the
identities \(B_4w=B_3w=0\) do not repair the endpoint ledger.

The theorem does **not** prove any of the following stronger claims:

* that no noncanonical rank-four factor is \(\mathcal D_4\)-port-transversal;
* that the nonlocal Haar shadow direction has no state-level suspension;
* that auxiliary rows cannot route the interior selected sets to the
  canonical ports;
* that a parent-hole substitution cannot contain a corrected copy of the
  commutator; or
* that a dimension-dependent completion cannot seal a lifted interaction
  component.

Thus the exact remaining context route is a **port-correction/state-level
completion theorem**: alter the local paths or the surrounding completion
so that the canonical boundaries are genuine endpoints, while retaining
exact middle and adjacent-union ownership.  Merely re-rooting either
finished \(m=4\) Haar factor is now rigorously closed.
