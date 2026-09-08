# Lane E: a four-row full-ledger Tamari associator

Date: 2026-07-26

Method: pure mathematics only.  The proof below is the literal inspection
of two finite tables; no search, program, solver, or web input is used.

## 0. Outcome

The naive two-row associator fails, but three auxiliary paths cure it.
There is a four-for-four packet of length-four Johnson geodesics on
\([8]\) with

1. identical aggregate middle-state (\(X\)) multisets;
2. identical aggregate adjacent-union (\(Y\)) multisets;
3. pairwise disjoint states and colours on either side; and
4. a distinguished primitive-root row in which the first step is changed
   from the canonical MSW step to the nonleaf Tamari root rotation.

The distinguished negative and positive traces are

\[
\begin{aligned}
 L^-&=(1245,1258,1268,1678,3678),\\
 L^+&=(1245,1256,1268,1678,3678).
\end{aligned}                                                   \tag{0.1}
\]

Here \(1245\) is the Dyck word \(11011000\), whose first return has
semilength \(j=4\), while \(1256\) is the other bracketing
\(11001100\).  Thus the first edge of \(L^+\) literally performs the root
associator

\[
                         1245\longrightarrow1256.          \tag{0.2}
\]

Moreover the intrinsic long-window target changes:

\[
 \bigcap_{t=1}^4L^-_t=\{8\},
 \qquad
 \bigcap_{t=1}^4L^+_t=\{6\}.                              \tag{0.3}
\]

In the first-return indexing this is the nontrivial movement
\(2j=8\longrightarrow 2(j-1)=6\).  It is therefore outside the certified
leaf rotation, which only connects the classes \(j=2\) and \(j=1\).

The construction gives an unconditional full-ledger associator with four
rows on each side.  Since the two-row packet is already known to be
impossible, the present information on the minimum row number is

\[
                              3\le k_{\min}\le4.            \tag{0.4}
\]

The existence or nonexistence of a three-row packet remains open.

There is a port subtlety and an exact cure.  The positive packet which
literally displays the edge \(1245\to1256\) is not
\(\mathcal D_4\)-port-transversal: \(1256\) is internal in \(L^+\), and
\(A^+\) has no Dyck port.  The same \(X/Y\) ledgers admit a third
decomposition \(\mathcal P^\star\) which restores all four Dyck ports
row-by-row while retaining the target \(\{6\}\).  Consequently there is a
two-stage exact route

\[
 \mathcal P^-\longrightarrow\mathcal P^+
 \longrightarrow\mathcal P^\star                      \tag{0.5}
\]

whose first stage performs the literal Tamari edge and whose second stage
restores the Section-17 port allocation without undoing the root movement.

## 1. The packet

As usual, a string such as \(1256\) denotes the set
\(\{1,2,5,6\}\).  The negative packet is

\[
\begin{array}{c|ccccc}
 A^-&1256&1246&1467&3467&3478\\
 L^-&1245&1258&1268&1678&3678\\
 C^-&1257&1247&1248&1468&3468\\
 D^-&1237&1347&1478&4678&4568
\end{array}                                                \tag{1.1}
\]

and the positive packet is

\[
\begin{array}{c|ccccc}
 A^+&3467&3478&1478&1248&1258\\
 L^+&1245&1256&1268&1678&3678\\
 C^+&1257&1247&1246&1468&3468\\
 D^+&1237&1347&1467&4678&4568.
\end{array}                                                \tag{1.2}
\]

The rows \(A,C,D\) are the three auxiliary paths.

The port-restored packet is

\[
\begin{array}{c|ccccc}
 A^\star&1256&1258&1248&1478&3478\\
 L^\star&1245&1246&1268&1678&3678\\
 C^\star&1257&1247&1467&1468&3468\\
 D^\star&1237&1347&3467&4678&4568.
\end{array}                                                \tag{1.3}
\]

## 2. Every row is a legal wreath path

### Lemma 2.1

Every consecutive pair in (1.1)--(1.2) is a Johnson edge, and the last
state of every row is the complement in \([8]\) of its first state.
Consequently every row lifts, by adjoining the omitted coordinate
\(\infty\), to a legal \(C_9\) wreath.

#### Proof

In each displayed row, consecutive four-sets have intersection size three.
The complementary endpoint pairs are

\[
\begin{array}{c|c}
A^-&1256\leftrightarrow3478\\
L^-&1245\leftrightarrow3678\\
C^-&1257\leftrightarrow3468\\
D^-&1237\leftrightarrow4568
\end{array}
\qquad
\begin{array}{c|c}
A^+&3467\leftrightarrow1258\\
L^+&1245\leftrightarrow3678\\
C^+&1257\leftrightarrow3468\\
D^+&1237\leftrightarrow4568.
\end{array}
\]

For a Johnson geodesic \(X_0,\ldots,X_4\), insert between \(X_t\) and
\(X_{t+1}\) the odd-graph vertex

\[
 Z_t=\{\infty\}\cup\bigl([8]\setminus(X_t\cup X_{t+1})\bigr).
\]

This gives the required nine-cycle. \(\square\)

The same inspection applies to (1.3); its complementary endpoint pairs
are exactly those of (1.1), in the same row order.

## 3. Exact \(X\)-ledger

### Lemma 3.1

The two packets have the same aggregate state multiset:

\[
 \boxed{
 \biguplus_{P\in\{A^-,L^-,C^-,D^-\}}\ \biguplus_{t=0}^4
       \{P_t\}
 =
 \biguplus_{P\in\{A^+,L^+,C^+,D^+\}}\ \biguplus_{t=0}^4
       \{P_t\}.}                                         \tag{3.1}
\]

Every state occurs once on either side.

#### Proof

Both sides of (3.1) are the following twenty-set family:

\[
\begin{aligned}
\mathcal X=\{&
1237,1245,1246,1247,1248,1256,1257,1258,1268,\\
&1347,1467,1468,1478,1678,3467,3468,3478,\\
&3678,4568,4678\}.
\end{aligned}                                            \tag{3.2}
\]

The tables list every member exactly once. \(\square\)

The table (1.3) also lists every member of \(\mathcal X\) exactly once, so
its aggregate \(X\)-ledger equals both sides of (3.1).

## 4. Exact adjacent-union ledger

For a row \(P=(P_0,\ldots,P_4)\), put

\[
                         Y_t(P)=P_t\cup P_{t+1}.
\]

### Lemma 4.1

The two packets have the same aggregate \(Y\)-multiset:

\[
 \boxed{
 \biguplus_{P\in\{A^-,L^-,C^-,D^-\}}\ \biguplus_{t=0}^3
       \{Y_t(P)\}
 =
 \biguplus_{P\in\{A^+,L^+,C^+,D^+\}}\ \biguplus_{t=0}^3
       \{Y_t(P)\}.}                                      \tag{4.1}
\]

Every colour occurs once on either side.

#### Proof

The negative rows have colour lists

\[
\begin{array}{c|cccc}
A^-&12456&12467&13467&34678\\
L^-&12458&12568&12678&13678\\
C^-&12457&12478&12468&13468\\
D^-&12347&13478&14678&45678,
\end{array}                                              \tag{4.2}
\]

whereas the positive rows have

\[
\begin{array}{c|cccc}
A^+&34678&13478&12478&12458\\
L^+&12456&12568&12678&13678\\
C^+&12457&12467&12468&13468\\
D^+&12347&13467&14678&45678.
\end{array}                                              \tag{4.3}
\]

Thus both sides enumerate exactly

\[
\begin{aligned}
\mathcal Y=\{&
12347,12456,12457,12458,12467,12468,12478,\\
&12568,12678,13467,13468,13478,13678,14678,\\
&34678,45678\}.
\end{aligned}                                            \tag{4.4}
\]

This proves (4.1). \(\square\)

The four colour lists of the restored packet are

\[
\begin{array}{c|cccc}
A^\star&12568&12458&12478&13478\\
L^\star&12456&12468&12678&13678\\
C^\star&12457&12467&14678&13468\\
D^\star&12347&13467&34678&45678.
\end{array}                                               \tag{4.5}
\]

They again enumerate \(\mathcal Y\) exactly once.  Hence
\(\mathcal P^\star\) has the same aggregate \(Y\)-ledger as
\(\mathcal P^-\) and \(\mathcal P^+\).

## 5. The full-ledger associator theorem

### Theorem 5.1 (four-row Tamari associator)

Replacing the four wreath paths (1.1) by the four paths (1.2) preserves
both exact wreath ownership ledgers.  It is support-feasible: each side is
a vertex-disjoint union of four \(C_9\)'s.  In the distinguished row it
implements the root first-return move (0.2) and changes the marked
long-window target as in (0.3).

The same packet remains valid after an arbitrary coordinate relabelling
and after adjoining a common exterior set to every \(X\)-state.

#### Proof

Lemma 2.1 gives four legal wreaths on either side.  Lemma 3.1 is the exact
ledger for vertices avoiding \(\infty\).  Lemma 4.1 is the adjacent-union
ledger; complementation in \([8]\), followed by adjoining \(\infty\),
therefore gives exactly the same vertices containing \(\infty\).  The
distinctness assertions in Lemmas 3.1 and 4.1 prove support feasibility.

The second rows are exactly (0.1), so their first edge is (0.2).  Finally,

\[
\begin{aligned}
1258\cap1268\cap1678\cap3678&=\{8\},\\
1256\cap1268\cap1678\cap3678&=\{6\},
\end{aligned}
\]

which proves (0.3).  Relabelling and adjoining a common exterior set
preserve Johnson adjacency and both multiset identities. \(\square\)

## 6. How the three auxiliary rows close the two-row defect

The distinguished replacement alone changes

\[
                         1258\longrightarrow1256          \tag{6.1}
\]

in the \(X\)-ledger and

\[
                         12458\longrightarrow12456        \tag{6.2}
\]

in the \(Y\)-ledger.  The other incident colour \(12568\) is unchanged.

The three auxiliary \(X\)-differences are

\[
\begin{aligned}
\Delta_XA={}&
 e_{1478}+e_{1248}+e_{1258}
 -e_{1256}-e_{1246}-e_{1467},\\
\Delta_XC={}&e_{1246}-e_{1248},\\
\Delta_XD={}&e_{1467}-e_{1478}.
\end{aligned}                                            \tag{6.3}
\]

Therefore

\[
 \Delta_XA+\Delta_XC+\Delta_XD
 =e_{1258}-e_{1256}=-\Delta_XL.                         \tag{6.4}
\]

Similarly their \(Y\)-differences are

\[
\begin{aligned}
\Delta_YA={}&
 e_{13478}+e_{12478}+e_{12458}
 -e_{12456}-e_{12467}-e_{13467},\\
\Delta_YC={}&e_{12467}-e_{12478},\\
\Delta_YD={}&e_{13467}-e_{13478}.
\end{aligned}                                            \tag{6.5}
\]

Hence

\[
 \Delta_YA+\Delta_YC+\Delta_YD
 =e_{12458}-e_{12456}=-\Delta_YL.                       \tag{6.6}
\]

Thus the cure is genuinely multirow: the state and colour defects telescope
through different auxiliary supports, but both close exactly.

## 7. Exact restoration of the Dyck ports

Let

\[
\begin{aligned}
\mathcal D_4=\{&
1234,1235,1236,1237,1245,1246,1247,\\
&1256,1257,1345,1346,1347,1356,1357\}
\end{aligned}                                             \tag{7.1}
\]

be the standard Dyck four-sets in \([8]\).

### Proposition 7.1 (the intermediate port defect)

The negative packet has one Dyck port on each row, namely

\[
 1256,\quad1245,\quad1257,\quad1237.
 \tag{7.2}
\]

The positive packet \(\mathcal P^+\) is not
\(\mathcal D_4\)-port-transversal: the ports of \(A^+\) are
\(3467,1258\), neither Dyck, while \(1256\) occurs internally in \(L^+\)
beside its Dyck port \(1245\).

#### Proof

Read the first and last entries of (1.1)--(1.2) and compare them with
(7.1). \(\square\)

Thus \(\mathcal P^+\) alone is not a Section-17 context substitute.

### Theorem 7.2 (four distinguished port pairs are restored)

The packet \(\mathcal P^\star\) in (1.3) is
\(\mathcal D_4\)-port-transversal.  Its four Dyck ports are exactly (7.2),
and its complementary endpoint pairs agree row-by-row with
\(\mathcal P^-\).  It has the same aggregate \(X\)- and \(Y\)-ledgers as
\(\mathcal P^-\), while

\[
 \boxed{
 \bigcap_{t=1}^4L^-_t=\{8\},
 \qquad
 \bigcap_{t=1}^4L^\star_t=\{6\}.}
 \tag{7.3}
\]

Consequently the composite (0.5) is a finite exact-ledger route which
performs a nonleaf root Tamari move and then restores the four displayed
labelled endpoint pairs without reversing the marked target movement.
Equivalently, the net
trade

\[
                 \mathcal P^-\longleftrightarrow
                 \mathcal P^\star                         \tag{7.4}
\]

is a rowwise fixed-endpoint slab trade whenever its negative packet is
already present.

#### Proof

The first entries of (1.3) are the four distinct Dyck sets in (7.2), and
their last entries are their complements.  No complement is Dyck, so each
row has exactly one Dyck port.  Lemma 2.1 and its extension to (1.3) give
legality and the rowwise boundary identities.  The observations after
Lemmas 3.1 and 4.1 give the exact \(X/Y\) ledgers.

Finally,

\[
 1246\cap1268\cap1678\cap3678=\{6\},
\]

while the first equality in (7.3) was computed in Theorem 5.1.  Hence the
restoration step does not undo the target movement. \(\square\)

The restoration is economical: it uses no new state or colour.  It is a
second decomposition of precisely the same incidence supports
\(\mathcal X\) and \(\mathcal Y\).

It does **not** by itself produce a complete
\(\mathcal D_4\)-port-transversal local factor.

### Proposition 7.3 (the seven-root completion obstruction)

Each of the packets \(\mathcal P^-\) and \(\mathcal P^\star\) contains
seven standard Dyck states:

\[
 1237,1245,1246,1247,1256,1257,1347.                 \tag{7.5}
\]

Only four of them are ports.  Consequently neither packet can be contained
in a complete \(\mathcal D_4\)-port-transversal exact factor on \([8]\).

#### Proof

A complete exact factor partitions all \(70\) four-sets into fourteen
five-state paths.  A \(\mathcal D_4\)-port-transversal factor has fourteen
paths and fourteen Dyck sets.  Its selected Dyck ports are distinct, hence
exhaust \(\mathcal D_4\); therefore no Dyck set can occur internally.

Inspection of (1.1) or (1.3) gives (7.5), with \(1246,1247,1347\)
internal.  Equivalently, after these four paths are fixed, the ten
remaining paths have only seven unused Dyck states available for ten
required ports.  This is impossible. \(\square\)

Thus the four-row construction is a genuine fixed-endpoint local trade but
not a Section-17 replacement factor.  A root-restoration theorem must
change a larger support, not merely redecompose \(\mathcal X,\mathcal Y\).

## 8. Scope and remaining minimum question

The theorem supplies the requested finite full-ledger packet.  It is
stronger than equality of the middle-state ledger alone and avoids the
failure of the two canonical rows in the naive associator.

It does not prove that four is the absolute minimum.  The known two-row
no-go gives the lower bound in (0.4), but no invariant in the two ownership
ledgers presently excludes a three-row circuit.  Proving minimality would
require either

1. classifying three-path decompositions of the common \(X/Y\) incidence
   multiset, or
2. finding a new parity or endpoint invariant which survives aggregate
   \(X/Y\) equality.

The port-restored net trade (7.4) fixes its four complementary endpoint
pairs row-by-row.  The intermediate packet
\(\mathcal P^+\) is retained only to exhibit the literal Tamari edge
\(1245\to1256\).  Proposition 7.3 is the remaining global qualification:
the four paths cannot be completed to a Section-17 port-transversal factor.

## 9. Provenance of the table

For orientation only, the table is a coordinate relabelling and reversal
of the four-for-four nonlocal \(m=4\) Haar circuit.  The relabelling is

\[
 1\mapsto8,\quad2\mapsto6,\quad3\mapsto4,\quad4\mapsto7,
 \quad5\mapsto5,\quad6\mapsto3,\quad7\mapsto2,\quad8\mapsto1.
\]

No property of that earlier construction is used in the proof: the
Johnson adjacencies, complementary endpoints, \(X\)-ledger, \(Y\)-ledger,
and root movement are all verified directly above.
