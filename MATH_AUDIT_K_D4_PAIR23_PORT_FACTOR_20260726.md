# Independent pure-math audit of the \(D_4\) pair-2-to-pair-3 port factor

Date: 2026-07-26

Audited source: `MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md`.

Method: literal inspection of the displayed paths and ownership ledgers; no
search, program, solver, or web input.

## 0. Verdict

The certificate is correct.  There are two complete
\(\mathcal D_4\)-port-rooted complement path factors on \([8]\): the
canonical MSW factor and the explicit factor \(G\) below.  If

\[
 c_i(F)=\#\{P\in\mathcal D_4:
             b_1^F(P)\in\{2i,2i+1\}\},\qquad1\le i\le3, \tag{0.1}
\]

then

\[
 (c_1,c_2,c_3)(F_{\rm MSW})=(5,2,2),\qquad
 (c_1,c_2,c_3)(G)=(5,1,3).                              \tag{0.2}
\]

Thus

\[
                         \boxed{\Delta c=(0,-1,+1)}       \tag{0.3}
\]

is a literal integral transfer of one first-insertion unit from the pair
\(\{4,5\}\) to the pair \(\{6,7\}\).  In particular the protected pair
totals of the previously known \(H_r\), rooted-pentagon, and elementary
rectangle menus are not invariants of the full port-factor fibre.

The remaining five first insertions of each factor lie in the endpoint
pair \(\{1,8\}\), in fact at coordinate 8.  Including this pair, the two
four-pair vectors are

\[
 (5,5,2,2)\quad\hbox{and}\quad(5,5,1,3).                \tag{0.4}
\]

## 1. The explicit rooted paths

The rows of \(G\), indexed by their prescribed Dyck ports, are

\[
\begin{array}{c|ccccc|c}
P&X_0&X_1&X_2&X_3&X_4&b_1=X_1\setminus X_0\\ \hline
1234&1234&1238&1368&1568&5678&8\\
1235&1235&1358&1378&1678&4678&8\\
1236&1236&1267&1467&4567&4578&7\\
1237&1237&1278&1268&1468&4568&8\\
1245&1245&2345&3456&3567&3678&3\\
1246&1246&2346&2368&2378&3578&3\\
1247&1247&2347&2348&2358&3568&3\\
1256&1256&1567&1367&3467&3478&7\\
1257&1257&2357&3457&3458&3468&3\\
1345&1345&1456&2456&2567&2678&6\\
1346&1346&1348&1458&1578&2578&8\\
1347&1347&1478&1248&1258&2568&8\\
1356&1356&2356&2367&2467&2478&2\\
1357&1357&1457&2457&2458&2468&4.
\end{array}                                             \tag{1.1}
\]

### Lemma 1.1 (Johnson legality and complementary ports)

Every consecutive pair in every row of (1.1) intersects in three labels,
and \(X_4=[8]\setminus X_0\).  The fourteen first states are exactly

\[
\begin{aligned}
\mathcal D_4=\{&1234,1235,1236,1237,1245,1246,1247,\\
                &1256,1257,1345,1346,1347,1356,1357\}.
\end{aligned}                                          \tag{1.2}
\]

#### Audit

The exact symmetric differences are checked directly from (1.1): each
pair has one deleted and one inserted element.  For example the first row
has

\[
1234\to1238\to1368\to1568\to5678,                      \tag{1.3}
\]

with exchanges \(4\to8,2\to6,3\to5,1\to7\).  The same
one-symbol comparison applies literally to the other thirteen displayed
rows.  Their endpoint pairs are

\[
\begin{gathered}
1234|5678, 1235|4678, 1236|4578, 1237|4568,\\
1245|3678, 1246|3578, 1247|3568, 1256|3478,\\
1257|3468, 1345|2678, 1346|2578, 1347|2568,\\
1356|2478, 1357|2468,
\end{gathered}                                          \tag{1.4}
\]

so the complement assertion is exact.  This proves the lemma. \(\square\)

## 2. Audit of the complete \(X\)-ledger

The 28 endpoints in (1.4) are distinct.  The 42 internal states are

\[
\begin{aligned}
\{&1267,1367,1456,1457,1467,1567,
2345,2346,2347,2356,2357,2367,\\
&2456,2457,2467,2567,3456,3457,3467,3567,4567,\\
&1238,1248,1258,1268,1278,1348,1358,1368,1378,
1458,1468,1478,\\
&1568,1578,1678,2348,2358,2368,2378,2458,3458\}.
\end{aligned}                                          \tag{2.1}
\]

The first 21 entries of (2.1) avoid 8 and are visibly distinct.  The last
21 contain 8 and become distinct three-subsets after deleting 8.  None is
one of the 28 endpoints in (1.4): among the 8-free states none is a Dyck
root in (1.2), and among the 8-containing states none is a listed
complement.  Hence (1.1) contains

\[
                         28+42=70=\binom84             \tag{2.2}
\]

distinct four-subsets.  This is the complete \(X\)-shore, once each.

## 3. Audit of the complete \(Y\)-ledger

For each transition put \(Y_t=X_t\cup X_{t+1}\).  Direct union in (1.1)
gives

\[
\begin{array}{c|cccc}
1234&12348&12368&13568&15678\\
1235&12358&13578&13678&14678\\
1236&12367&12467&14567&45678\\
1237&12378&12678&12468&14568\\
1245&12345&23456&34567&35678\\
1246&12346&23468&23678&23578\\
1247&12347&23478&23458&23568\\
1256&12567&13567&13467&34678\\
1257&12357&23457&34578&34568\\
1345&13456&12456&24567&25678\\
1346&13468&13458&14578&12578\\
1347&13478&12478&12458&12568\\
1356&12356&23567&23467&24678\\
1357&13457&12457&24578&24568.
\end{array}                                             \tag{3.1}
\]

Sorted lexicographically, these are

\[
\begin{aligned}
\{&12345,12346,12347,12348,12356,12357,12358,12367,
12368,12378,\\
&12456,12457,12458,12467,12468,12478,12567,12568,
12578,12678,\\
&13456,13457,13458,13467,13468,13478,13567,13568,
13578,13678,\\
&14567,14568,14578,14678,15678,23456,23457,23458,
23467,23468,\\
&23478,23567,23568,23578,23678,24567,24568,24578,
24678,25678,\\
&34567,34568,34578,34678,35678,45678\}.
\end{aligned}                                          \tag{3.2}
\]

This is the complete lexicographic list: 35 entries contain 1 and 21 do
not, for a total of

\[
                         35+21=56=\binom85.             \tag{3.3}
\]

No entry repeats.  Thus (3.1) is the complete \(Y\)-shore, once each.

## 4. Literal \(C_9\)-factor and port conclusion

Between consecutive \(X\)-states insert

\[
                         Z_t=\{9\}\cup([8]\setminus Y_t).
                                                               \tag{4.1}
\]

Because \(X_t,X_{t+1}\subset Y_t\), both are disjoint from \(Z_t\), and
all three sets have size four.  Lemma 1.1 supplies the closing edge
\(X_4-X_0\), since those states are complementary.  Hence each row becomes
a legal nine-cycle in \(KG(9,4)\).

Section 2 owns every four-set avoiding 9 once.  Complementation in \([8]\)
and adjoining 9 is a bijection

\[
 \binom{[8]}5\longrightarrow
 \{S\in\tbinom{[9]}4:9\in S\},qquad
 Y\longmapsto\{9\}\cup([8]\setminus Y).                \tag{4.2}
\]

Section 3 therefore owns every four-set containing 9 once.  The fourteen
cycles form an exact \(C_9\)-factor.

All fourteen Dyck sets have already been used once as the first states in
(1.1).  Exact \(X\)-ownership prevents a Dyck set from appearing again as
an internal state or a second port.  Thus the factor is literally
\(\mathcal D_4\)-port-rooted, not merely ordinarily transversal.

## 5. First-insertion transfer

Reading the last column of (1.1) gives

\[
 \{b_1(P):P\in\mathcal D_4\}
   =\{8,8,7,8,3,3,3,7,3,6,8,8,2,4\}.                  \tag{5.1}
\]

Equivalently its histogram is

\[
                         5e_8+e_2+4e_3+e_4+e_6+2e_7.   \tag{5.2}
\]

This gives the new pair vector (0.4).

For the canonical factor, the first insertion is the position of the
first return of the Dyck root.  Grouping the fourteen roots by first-return
position gives

\[
\begin{array}{c|l|c}
b_1&\text{roots}&\text{count}\\ \hline
8&1234,1235,1236,1245,1246&5\\
6&1237,1247&2\\
4&1256,1257&2\\
2&1345,1346,1347,1356,1357&5.
\end{array}                                             \tag{5.3}
\]

Thus its full pair vector is \((5,5,2,2)\), and subtraction gives exactly
(0.3).

### Theorem 5.1 (the finite missing primitive exists)

There are two literal integral \(\mathcal D_4\)-port complement path
factors with different first-insertion pair totals.  Their difference
transfers one unit from \(\{4,5\}\) to \(\{6,7\}\), while leaving the
\(\{1,8\}\) and \(\{2,3\}\) totals fixed.

#### Proof

The canonical MSW factor is a \(\mathcal D_4\)-port factor.  Sections
1--4 prove the same for \(G\).  Section 5 proves their pair totals and
their difference. \(\square\)

## 6. Exact scope

This settles the finite existence/invariant dichotomy in the positive
direction.  It does not yet provide

* a proper smaller-support/common-completion subtrade between the two
  fourteen-row factors;
* a recursive suspension preserving the same transfer at every scale;
* a decomposition of their ownership overlay into small components; or
* a quantitative global packet selection theorem.

The whole fourteen-for-fourteen replacement is of course already a finite
trade.  Accordingly, the phrase “no bounded-row trade” in the source's
scope paragraph should be read in the sharper sense above; literally it
would be false.

What is now rigorous is the required primitive: no invariant of the full
\(\mathcal D_4\)-port factor fibre can force the pair-2 and pair-3 totals
separately, because the two explicit integral fibre points differ by
\((0,-1,+1)\).

There is also an immediate, precisely scoped recursive use.  For any fixed
Dyck suffix \(B\) of semilength \(s\), apply the common context
\(x\mapsto xB\) to all fourteen rows on both sides.  The rooted context
functor preserves the rowwise
complement endpoints and both aggregate ledgers.  In the MSW concatenation
identity the old four-step path is the first slab and \(B\) is a fixed
spectator there, so the first-insertion transfer (0.3) survives verbatim in
that local coordinate block.  Keeping all other \(\mathcal D_{4+s}\)
rows canonical therefore gives a literal larger port factor.

This does not provide a genuinely root-scale new primitive: the active
core still has size eight.  Left concatenation moves the gadget away from
the first global edge, and \(J\)-wrapping dualizes its internal states
through the old \(Y\)-ledger, so neither operation may be credited with the
same global first-insertion vector without a separate calculation.
