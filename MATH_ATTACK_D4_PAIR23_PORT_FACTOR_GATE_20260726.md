# The \(D_4\) pair-\(2\)/pair-\(3\) port gate

Date: 2026-07-26

Method: pure mathematics. Every finite assertion below is checked from the
displayed \(X\)- and \(Y\)-tables; no search, solver, or web input is used.

## 0. Verdict

Let

\[
 {\cal D}_4=\{1234,1235,1236,1237,1245,1246,1247,
 1256,1257,1345,1346,1347,1356,1357\}.
\]

For a rooted complement path

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots
 \subset Y_3\supset X_4=[8]\setminus P
\]

write \(b_1(P)\) for the unique member of \(Y_0\setminus P\), and put

\[
 c_i=\#\{P\in{\cal D}_4:b_1(P)\in\{2i,2i+1\}\},
 \qquad 1\le i\le3,
\]

with the cyclic fourth pair \(\{8,1\}\). The canonical vector is

\[
                         (c_1,c_2,c_3,c_4)=(5,2,2,5).
\tag{0.1}
\]

The requested pair-\(2\) to pair-\(3\) transfer is present in the known
four-row full-ledger associator, but that signed packet is not contained in
any \(D_4\)-port factor: three additional Dyck sets occur internally. Its
local displacement is exactly

\[
                         (0,-1,+1,0).
\tag{0.2}
\]

There is also an explicit port-clean completion of a very close four-carrier
defect. It gives the fourteen-row \(D_4\)-port factor in Section 2. However,
its pair vector is again (0.1). More sharply, the four-carrier support used
by that repair has a **unique** \(D_4\)-ported decomposition. Thus no second
decomposition of that support can realize (0.2); the port repair repays the
entire apparent transfer.

This is a support-level no-go, not a global invariant of every
\(D_4\)-port factor. A global construction or a global pair-total invariant
is not proved here. The exact smaller remaining lemma is now:

> **P23+.** Find a clean, complement-paired \(X/Y\) trade outside both forced
> supports of Sections 4--5, whose signed
> first-up-edge weight is \((0,-1,+1,0)\); or prove that every alternating
> component of the full port-path fibre has zero such weight.

Section 5 records a forced-up-edge obstruction which deletes the most
tempting five-row continuation. It is global, not merely support-local.

## 1. The desired direction already exists before the port audit

The negative and port-restored four-row tables from the full-ledger
associator have the following first transitions:

\[
\begin{array}{c|c|c}
P&X_1^-&X_1^\star\\ \hline
1256&1246&1258\\
1245&1258&1246\\
1257&1247&1247\\
1237&1347&1347.
\end{array}
\tag{1.1}
\]

Consequently their insertion labels are

\[
 (4,8,4,4)\qquad\hbox{and}\qquad(8,6,4,4),
\tag{1.2}
\]

so the signed pair-count change is exactly (0.2).

This is not yet the requested object. On either shore the aggregate state
support contains the seven Dyck sets

\[
 1237,1245,1246,1247,1256,1257,1347,
\tag{1.3}
\]

but only four of them are path ports. In a complete \(D_4\)-port factor all
fourteen Dyck sets already occur once as the fourteen initial ports, so no
Dyck set may occur internally. Hence neither shore of the four-row packet
can be extended to a \(D_4\)-port factor. Equation (0.2) is a genuine
\(X/Y\)-ledger direction but not a clean port-fibre direction.

## 2. An explicit noncanonical \(D_4\)-port factor

The following fourteen paths are indexed by all members of \({\cal D}_4\).

\[
\begin{array}{c|ccccc}
1234&1234&1348&1458&1568&5678\\
1235&1235&1358&1368&1468&4678\\
1236&1236&1238&1278&1578&4578\\
1237&1237&1367&1467&4567&4568\\
1245&1245&1258&1268&1678&3678\\
1246&1246&1248&1478&1378&3578\\
1247&1247&1267&1567&3567&3568\\
1256&1256&2356&3456&3467&3478\\
1257&1257&1457&3457&3458&3468\\
1345&1345&2345&2358&2368&2678\\
1346&1346&2346&2348&2378&2578\\
1347&1347&2347&2367&2567&2568\\
1356&1356&1456&2456&2458&2478\\
1357&1357&2357&2457&2467&2468.
\end{array}
\tag{2.1}
\]

Every row is a Johnson geodesic from its displayed root to its complement.
The associated adjacent-union table is

\[
\begin{array}{c|cccc}
1234&12348&13458&14568&15678\\
1235&12358&13568&13468&14678\\
1236&12368&12378&12578&14578\\
1237&12367&13467&14567&45678\\
1245&12458&12568&12678&13678\\
1246&12468&12478&13478&13578\\
1247&12467&12567&13567&35678\\
1256&12356&23456&34567&34678\\
1257&12457&13457&34578&34568\\
1345&12345&23458&23568&23678\\
1346&12346&23468&23478&23578\\
1347&12347&23467&23567&25678\\
1356&13456&12456&24568&24578\\
1357&12357&23457&24567&24678.
\end{array}
\tag{2.2}
\]

### Theorem 2.1

Tables (2.1)--(2.2) are a \(D_4\)-port-transversal complement path factor.

### Proof

The seventy entries of (2.1) are pairwise distinct four-subsets. Their
number is \(\binom84=70\), so they exhaust the \(X\)-shore. The fifty-six
entries of (2.2) are pairwise distinct five-subsets. Their number is
\(\binom85=56\), so they exhaust the \(Y\)-shore. Consecutive \(X\)-states
have the displayed \(Y\)-set as their union, and the last \(X\)-state in
each row is the complement of the first. Thus the tables partition the
middle-levels incidence graph into the required fourteen paths.

The initial states are exactly the fourteen members of \({\cal D}_4\).
Since the \(X\)-ledger is exact, no other occurrence of a Dyck state is
possible. Hence the port condition holds literally. \(\square\)

The first insertion labels in root order are

\[
\begin{array}{c|rrrrrrrrrrrrrr}
P&1234&1235&1236&1237&1245&1246&1247&1256&1257&1345&1346&1347&1356&1357\\ \hline
b_1&8&8&8&6&8&8&6&3&4&2&2&2&4&2.
\end{array}
\tag{2.3}
\]

Therefore this noncanonical factor still has

\[
                         (c_1,c_2,c_3,c_4)=(5,2,2,5).
\tag{2.4}
\]

The table is useful because it shows that a two-defect near-port factor can
indeed be repaired exactly; failure of the desired transfer is not caused
by nonexistence of the surrounding port factor.

## 3. The four-carrier port defect and its exact repair

Before the repair, the affected state paths are

\[
\begin{array}{c|ccccc}
Q_1&1247&1478&1378&3578&3568\\
Q_2&1456&2456&2458&2578&2378\\
Q_3&1248&1246&1267&1567&3567\\
Q_4&1356&1346&2346&2348&2478.
\end{array}
\tag{3.1}
\]

Their \(Y\)-rows are

\[
\begin{array}{c|cccc}
Q_1&12478&13478&13578&35678\\
Q_2&12456&24568&24578&23578\\
Q_3&12468&12467&12567&13567\\
Q_4&13456&12346&23468&23478.
\end{array}
\tag{3.2}
\]

The endpoint pairs of \(Q_2,Q_3\) are not Dyck/complement pairs, while the
missing Dyck roots \(1246,1346\) occur internally. Redecompose exactly the
same twenty \(X\)-states and sixteen \(Y\)-states as

\[
\begin{array}{c|ccccc}
R_{1246}&1246&1248&1478&1378&3578\\
R_{1247}&1247&1267&1567&3567&3568\\
R_{1356}&1356&1456&2456&2458&2478\\
R_{1346}&1346&2346&2348&2378&2578.
\end{array}
\tag{3.3}
\]

The \(Y\)-rows become

\[
\begin{array}{c|cccc}
R_{1246}&12468&12478&13478&13578\\
R_{1247}&12467&12567&13567&35678\\
R_{1356}&13456&12456&24568&24578\\
R_{1346}&12346&23468&23478&23578.
\end{array}
\tag{3.4}
\]

Tables (3.1),(3.3) have the same \(X\)-set, and (3.2),(3.4) have the same
\(Y\)-set. Thus (3.3) is a literal four-carrier port repair. Substituting it
into the ten unchanged rows gives (2.1).

## 4. Uniqueness of the natural four-carrier repair

### Theorem 4.1 (forced four-carrier decomposition)

On the common support (3.1)--(3.2), (3.3) is the unique decomposition into
four clean complement paths rooted respectively at

\[
                         1246,\ 1247,\ 1356,\ 1346.
\tag{4.1}
\]

In particular every port-clean decomposition of this support contributes
one first insertion in each of the four adjacent coordinate pairs. It
cannot carry a pair-\(2\) to pair-\(3\) transfer.

### Proof

All references below are to the finite support (3.1)--(3.2).

First consider the path ending at \(3568=\overline{1247}\). The terminal
colour \(35678\) can meet the nonendpoint state \(3567\); its other relevant
neighbour \(3578\) is already the prescribed endpoint
\(\overline{1246}\) and cannot occur internally. Thus the penultimate state
is \(3567\). Moving backwards, its only available clean continuation is

\[
 3567-13567-1567-12567-1267-12467-1247.
\]

This forces the second row of (3.3).

The root \(1356\) can no longer use \(13567\). Its clean first transition is
therefore forced through \(13456\) to \(1456\), after which the available
degree-two chain is

\[
 1456-12456-2456-24568-2458-24578-2478.
\]

This forces the third row.

Now \(24578\) is occupied. The path ending at
\(2578=\overline{1346}\) must therefore enter through \(23578\), and its
backwards chain is

\[
 2578-23578-2378-23478-2348-23468-2346-12346-1346.
\]

This forces the fourth row. The five remaining states and four remaining
colours are exactly the first row of (3.3). Hence the decomposition is
unique.

Its first insertion labels are \(8,6,4,2\), one in each pair, proving the
last assertion. \(\square\)

This theorem explains why the obvious repair of a near-port certificate
does not solve the requested gate: once the missing roots are promoted to
ports, the support has no remaining decomposition freedom.

## 5. A global forced-up-edge obstruction

The most tempting clean replacement for the \(1356\)-row in (2.1) is

\[
 1356,1456,2456,2458,2478
 \quad\longrightarrow\quad
 1356,1567,2567,2467,2478.
\tag{5.1}
\]

It changes the first insertion from \(4\) to \(7\), hence has exactly the
desired pair-\(2\) to pair-\(3\) sign. Nevertheless the positive row in
(5.1) cannot occur in any \(D_4\)-port factor, independent of what other
rows are chosen.

### Lemma 5.1 (forced up edge at \(2567\))

In every \(D_4\)-port complement path factor, the outgoing \(Y\)-edge of the
state \(2567\) is

\[
                            2567\subset25678.
\tag{5.2}
\]

Consequently \(2567\) is penultimate on its rooted path.

### Proof

Orient every path from its Dyck root to its complementary endpoint. The
edges \(X_t\subset Y_t\) form a perfect matching

\[
 M^\uparrow:\binom{[8]}4\setminus\overline{{\cal D}_4}
                 \longleftrightarrow\binom{[8]}5.
\]

The five four-subsets of \(25678\) are

\[
 2567,\quad2568,\quad2578,\quad2678,\quad5678.
\tag{5.3}
\]

The last four are precisely

\[
 \overline{1347},\quad\overline{1346},\quad
 \overline{1345},\quad\overline{1234};
\]

they are excluded from the domain of \(M^\uparrow\). Thus \(2567\) is the
unique eligible lower neighbour of \(25678\), proving (5.2). The two
incidences used at a \(Y\)-vertex join distinct \(X\)-states, so the next
state is one of the other four neighbours in (5.3), hence a complementary
endpoint. Complementary endpoints occur only at phase four; therefore
\(2567=X_3\). \(\square\)

In the proposed positive row (5.1), \(2567=X_2\), contradicting Lemma 5.1.
This is an exact global counterterm, not merely failure to fit the support of
Section 4.

There is, however, a compatible clean pair-\(3\) entrance which survives
this particular test:

\[
                 1356,1367,2367,2467,2478.
\tag{5.4}
\]

Its \(Y\)-row is

\[
                 13567,12367,23467,24678,
\tag{5.5}
\]

and its forced penultimate edge \(2467\subset24678\) is correctly placed.
Thus Lemma 5.1 does not prove a global pair-total invariant. Completing
(5.4) while preserving all other root/complement pairs is the smallest
concrete positive branch left by this audit.

There is nevertheless a second exact obstruction if one uses only the five
rows of (2.1) rooted at

\[
                  1356,\quad1247,\quad1237,\quad1347,\quad1357.
\tag{5.6}
\]

### Proposition 5.2 (the natural five-row closure fails)

Replace the \(1356\)-row by (5.4), and require the other four roots in
(5.6) to be completed using exactly the remaining \(X/Y\)-support of those
five old rows. No such four-path completion exists.

### Proof

The new row (5.4) takes the three old internal states

\[
                         1367,\quad2367,\quad2467
\tag{5.7}
\]

from the rows rooted at \(1237,1347,1357\), and takes the four old colours

\[
                13567,\quad12367,\quad23467,\quad24678
\tag{5.8}
\]

from the rows rooted at \(1247,1237,1347,1357\), respectively.

Three terminal-star edges are forced by the same argument as Lemma 5.1:

\[
\begin{aligned}
3567&\subset35678,\\
4567&\subset45678,\\
2567&\subset25678.
\end{aligned}
\tag{5.9}
\]

Within the five-row support, the only available endpoints in these three
stars are \(3568,4568,2568\). Hence the paths rooted at
\(1247,1237,1347\) must have penultimate states \(3567,4567,2567\),
respectively.

Now consider the required predecessor of \(3567\) on the \(1247\)-path.
The colour \(13567\) was consumed by (5.4). The only other remaining colour
in the five-row support which can enter \(3567\) is \(23567\). Its possible
other supported states are

\[
                         2357,\quad2367,\quad2567.
\tag{5.10}
\]

Here \(2367\) is already in (5.4), \(2567\) is the forced penultimate state
of the \(1347\)-path, and \(2357\) is forced as the first internal state of
the \(1357\)-path: after (5.4) consumes \(13567\), the only remaining
supported first colour at root \(1357\) is \(12357\), whose only clean
continuation is \(2357\). Thus no state remains to precede \(3567\).
This contradiction proves the proposition. \(\square\)

Proposition 5.2 does not exclude every five-row packet on a different
support. It says that the literal owner closure of the clean candidate
(5.4) is insufficient; a successful trade must import at least one new
state/colour carrier beyond that closure.

## 6. Exact boundary

The following are proved.

1. The unported four-row full-ledger circuit has the desired signed pair
   displacement \((0,-1,+1,0)\).
2. That circuit is excluded from every \(D_4\)-port factor by its three
   internal Dyck states.
3. Table (2.1) is an explicit noncanonical \(D_4\)-port factor.
4. Its natural four-carrier port repair is an exact \(X/Y\) re-decomposition.
5. That four-carrier repair is unique and has pair vector contribution
   \((1,1,1,1)\).
6. The apparent clean row (5.1) is globally impossible because the up edge
   at \(2567\) is forced.
7. The alternative clean row (5.4) is not eliminated by the singleton
   forced-edge test, but its natural five-row owner closure is impossible.

The global finite target remains open: no two complete \(D_4\)-port factors
with different \((c_1,c_2,c_3,c_4)\) are produced, and no invariant proving
all four totals fixed is established. Any positive solution must leave the
unique support of Section 4 and must route the three borrowed states in
(5.4) through a larger owner-preserving alternating component.
