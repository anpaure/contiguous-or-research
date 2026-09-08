# Independent audit of the rooted `D_4` pair-2-to-pair-3 factor

Date: 2026-07-26

Method: pure mathematics only.  Every finite assertion below follows by
set subtraction, set union, and comparison with the displayed ledgers.

## 0. Verdict

The fourteen-row certificate in
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md` is correct.

It is a complete anchored `D_4` complement-path factor, not merely a
partial packet.  Its seventy `X`-states are exactly
`binom([8],4)`, its fifty-six adjacent unions are exactly
`binom([8],5)`, and its row endpoints are the fourteen prescribed pairs

\[
                         P\longleftrightarrow[8]\setminus P,
                         \qquad P\in\mathcal D_4.
\]

If `b_1(P)=X_1(P) setminus X_0(P)` and

\[
 E_1=\{2,3\},\qquad E_2=\{4,5\},\qquad E_3=\{6,7\},
\]

then the new and canonical first-insertion ledgers are respectively

\[
 \boxed{(c_1,c_2,c_3,n_8)(G)=(5,1,3,5)},
 \qquad
 \boxed{(c_1,c_2,c_3,n_8)(G_{\rm MSW})=(5,2,2,5)}.
\]

Consequently

\[
 \boxed{(c_1,c_2,c_3,n_8)(G)-(c_1,c_2,c_3,n_8)(G_{\rm MSW})
                      =(0,-1,+1,0).}                 \tag{0.1}
\]

Thus the requested rooted pair-2-to-pair-3 gadget exists.  In particular,
the pair totals are not invariants of the complete anchored fibre.

## 1. The candidate and its exchange words

The candidate paths are

\[
\begin{array}{c|ccccc}
1234&1234&1238&1368&1568&5678\\
1235&1235&1358&1378&1678&4678\\
1236&1236&1267&1467&4567&4578\\
1237&1237&1278&1268&1468&4568\\
1245&1245&2345&3456&3567&3678\\
1246&1246&2346&2368&2378&3578\\
1247&1247&2347&2348&2358&3568\\
1256&1256&1567&1367&3467&3478\\
1257&1257&2357&3457&3458&3468\\
1345&1345&1456&2456&2567&2678\\
1346&1346&1348&1458&1578&2578\\
1347&1347&1478&1248&1258&2568\\
1356&1356&2356&2367&2467&2478\\
1357&1357&1457&2457&2458&2468.
\end{array}                                             \tag{1.1}
\]

For a row write `a_1...a_4 | b_1...b_4` when step `t` deletes `a_t`
and inserts `b_t`.  Direct subtraction of consecutive entries of (1.1)
gives

\[
\begin{array}{c|c}
1234&4231\mid8657\\
1235&2531\mid8764\\
1236&3216\mid7458\\
1237&3721\mid8645\\
1245&1245\mid3678\\
1246&1462\mid3875\\
1247&1742\mid3856\\
1256&2516\mid7348\\
1257&1275\mid3486\\
1345&3145\mid6278\\
1346&6341\mid8572\\
1347&3741\mid8256\\
1356&1536\mid2748\\
1357&3175\mid4286.
\end{array}                                             \tag{1.2}
\]

In every row the four deleted labels are precisely the root and the four
inserted labels are precisely its complement.  Hence each consecutive
pair has intersection three and the last entry is the complement of the
first.  This proves Johnson legality and all fourteen endpoint identities.

The first entries in (1.1) are exactly

\[
\mathcal D_4=\{1234,1235,1236,1237,1245,1246,1247,
1256,1257,1345,1346,1347,1356,1357\}.                 \tag{1.3}
\]

Thus the endpoint labels are the required Dyck ports.

## 2. Independent `X`-ledger check

The twenty-eight endpoints in (1.1) are the fourteen sets in (1.3) and
their fourteen complements, hence are distinct.  Sorting the internal
states according to whether they contain coordinate `8` gives

\[
\begin{aligned}
\mathcal I_0=\{&1267,1367,1456,1457,1467,1567,
2345,2346,2347,2356,2357,2367,\\
&2456,2457,2467,2567,3456,3457,3467,3567,4567\},\\
\mathcal I_8=\{&1238,1248,1258,1268,1278,1348,1358,1368,1378,
1458,1468,1478,\\
&1568,1578,1678,2348,2358,2368,2378,2458,3458\}.
                                                               \tag{2.1}
\end{aligned}
\]

Each line has twenty-one distinct members.  No member of `I_0` is a
Dyck root or the complement of one: complements all contain `8`, while
comparison with (1.3) excludes the roots.  No member of `I_8` is an
endpoint: those containing `1` cannot be complementary endpoints, and
the six avoiding `1`, namely

\[
                   2348,2358,2368,2378,2458,3458,
\]

are absent from the complement list in (1.1).  The two internal lists are
disjoint because of coordinate `8`.

We have therefore exhibited

\[
                        28+21+21=70=\binom84
\]

distinct four-sets.  They are exactly `binom([8],4)`.  In particular no
Dyck state occurs internally; every displayed first state is the unique
Dyck port of its row.

## 3. Independent `Y`-ledger check

Taking unions of consecutive entries of (1.1) gives

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

There are thirty-five colours containing `1`.  Sorted by their remaining
four labels, they are

\[
\begin{aligned}
&12345,12346,12347,12348,12356,12357,12358,12367,
12368,12378,\\
&12456,12457,12458,12467,12468,12478,12567,12568,
12578,12678,\\
&13456,13457,13458,13467,13468,13478,13567,13568,
13578,13678,\\
&14567,14568,14578,14678,15678.
                                                               \tag{3.2}
\end{aligned}
\]

This is the complete family of `binom(7,4)=35` five-sets containing `1`.
The remaining twenty-one colours are

\[
\begin{aligned}
&23456,23457,23458,23467,23468,23478,23567,23568,
23578,23678,\\
&24567,24568,24578,24678,25678,34567,34568,34578,
34678,35678,45678,
                                                               \tag{3.3}
\end{aligned}
\]

the complete family of `binom(7,5)=21` five-sets avoiding `1`.  Hence the
fifty-six entries of (3.1) are distinct and equal
`binom([8],5)`.

## 4. Exact odd-graph factorhood

For every adjacent pair put

\[
                  Z_t=\{9\}\cup\bigl([8]\setminus
                                      (X_t\cup X_{t+1})\bigr).
                                                               \tag{4.1}
\]

The row legality from Section 1 makes

\[
                 X_0,Z_0,X_1,Z_1,X_2,Z_2,X_3,Z_3,X_4
\]

a minimum nine-cycle of `KG([9],4)`.  Section 2 assigns every vertex
avoiding `9` once.  Complementation in `[8]` is a bijection from the
fifty-six colours in Section 3 to the four-subsets containing `9`, so
(4.1) assigns every remaining odd-graph vertex once.  The fourteen cycles
therefore form an exact `C_9`-factor.

Since the canonical MSW factor has the same complete two ledgers and the
same rowwise endpoint pairs, (1.1) and the canonical table are precisely
the two complete rooted factors requested in the problem.

## 5. First-insertion audit

The first inserted labels are the first symbols after the bars in (1.2):

\[
\begin{array}{c|cccccccccccccc}
P&1234&1235&1236&1237&1245&1246&1247&1256&1257&1345&1346&1347&1356&1357\\ \hline
b_1^G(P)&8&8&7&8&3&3&3&7&3&6&8&8&2&4.
\end{array}                                             \tag{5.1}
\]

Thus `2` occurs once, `3` four times, `4` once, `5` zero times, `6` once,
`7` twice, and `8` five times.  It follows that

\[
                     (c_1,c_2,c_3,n_8)(G)=(5,1,3,5).
                                                               \tag{5.2}
\]

For the canonical factor the same root order gives

\[
             (b_1^{\rm MSW}(P))_P
                =(8,8,8,6,8,8,6,4,4,2,2,2,2,2),       \tag{5.3}
\]

and hence

\[
             (c_1,c_2,c_3,n_8)(G_{\rm MSW})=(5,2,2,5).
                                                               \tag{5.4}
\]

Subtracting (5.4) from (5.2) proves (0.1).

There is no hidden contribution from coordinate `1`: every Dyck root
contains `1`, whereas `b_1(P)` lies outside the root.  Therefore the
source theorem's class `E_0={1,8}` has count exactly `n_8`; treating
`n_8` separately gives the same value five on both factors.

Finally, because a complementary Johnson geodesic inserts each complement
coordinate once and never deletes it later,

\[
                        \bigcap_{t=1}^4X_t(P)=\{b_1(P)\}.
\]

Thus (5.1) is also the exact marked child-intersection ledger, not merely
an edge label.

## 6. Exact boundary

The audit proves a finite rooted Haar-effect primitive with full support:
the pair-2 mass decreases by one, the pair-3 mass increases by one, and
the pair-1 and coordinate-8 masses are fixed.  Because both objects are
complete exact factors, their signed difference automatically has zero
full `X`- and `Y`-ledger and fixes every root/complement pair.

This does not by itself prove a bounded-support subtrade, a recursive
suspension to all ranks, or a favourable floor-corrected PCap sign.  Those
remain separate quantitative questions.  What is now closed is the finite
`D_4`-ported existence gate and the proposed pair-total invariant: the
latter is false.
