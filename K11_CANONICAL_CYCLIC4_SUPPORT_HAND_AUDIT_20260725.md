# Hand audit of the canonical \(K=11\) cyclic-four support table

> **Positive-support transcription correction (2026-07-25).**  In the
> class-E occurrence table, E13 and E14 formerly printed `1236` and
> `1235`.  Their literal cyclic windows are respectively `1346` and
> `1345`.  The table and class-E local profile below are corrected.  The
> complete global positive-support certificate is
> `K11_CORRECTED_CYCLIC4_POSITIVE_SUPPORT_CERTIFICATE_20260725.md`.

> **Second correction notice (2026-07-25).**  The class-E internal-deletion
> table in Section 6 omitted four backward-tail incidences: E9 has
> \(158(10)\) in deletion position 1; E13 has \(136(10)\) in position 1;
> E14 has \(158(10)\) in position 1 and \(136(10)\) in position 3.  The
> corrected E total is 86 and its maximum degree remains 10.  The complete
> corrected ledger and a full 32-hole tail transversal are in
> `K11_CORRECTED_TAIL_TRANSVERSAL_AND_COUPLED_GATE_20260725.md`.

Date: 2026-07-25

## 1. Immediate verdict

The claimed hole list in
K11_CANONICAL_CYCLIC4_SUPPORT_CLASSIFICATION_20260725.md is not compatible
with its own recursion and class-E formula.  The set

\[
\boxed{\{1,2,7,10\}}
\]

is listed there as absent, but it is an old cyclic four-window in class E.
The explicit witness is derived below without computation.

The T3 and T4 tables, the convention \(\pi=(0,R,I)\), and the class-E
formula used in this counterexample all follow directly from the displayed
flip recursion.  Thus the discrepancy is in the support classification,
not in an optional orientation convention.

This report records the complete hand audit of class E.  Global
reconciliation with classes A--D is ongoing; no corrected global support
number is asserted before that reconciliation.

## 2. Verification of the small recursion tables

The semilength-one table is

\[
T_1=\{1\mid2\}.
\]

Applying (1.1) at semilength two gives

\[
T_2=\{13\mid24,\ 21\mid43\}.
\]

At semilength three, first-return size \(r=0\) gives

\[
135\mid246,\qquad143\mid265.
\]

The case \(r=1\) gives

\[
215\mid436,
\]

and \(r=2\) gives

\[
421\mid653,\qquad231\mid645.
\]

This is exactly the displayed T3 table.

Applying the same recurrence once more gives T4 in four blocks:

\[
\begin{array}{c|l}
r& R\mid I\\ \hline
0&
1357\mid2468,\ 1365\mid2487,\ 1437\mid2658,\
1643\mid2875,\ 1453\mid2867\\
1&
2157\mid4368,\ 2165\mid4387\\
2&
4217\mid6538,\ 2317\mid6458\\
3&
6421\mid8753,\ 6231\mid8745,\ 4521\mid8673,\
2351\mid8467,\ 2431\mid8657 .
\end{array}
\]

For example, the \(r=2\) row \(13\mid24\) of T2 gives

\[
R=(6-(2,4),1,7)=4217,\qquad
I=(6,6-(1,3),8)=6538.
\]

Thus the displayed T4 table is also correct.  In these formulas \(h-I\)
and \(h-R\) preserve list order and subtract componentwise, exactly as in
the recursion
\[
[h-v:v\in\Phi(\operatorname{rc}(p))].
\]

Finally, splitting the flip sequence into its even and odd positions gives
the stated cyclic coordinate order

\[
\pi=(0,R,I).
\]

There is no reversal of either list hidden in this notation.

## 3. The class-E counterexample

For class E, the source formula is

\[
R=(10-I_4,1),\qquad I=(10,10-R_4).
\tag{3.1}
\]

Use the verified T4 row

\[
R_4\mid I_4=4217\mid6538.
\]

Equation (3.1) gives

\[
R=(4,5,7,2,1),\qquad I=(10,6,8,9,3),
\]

and hence

\[
\pi=(0,4,5,7,2,1,10,6,8,9,3).
\tag{3.2}
\]

The four consecutive coordinates in positions \(3,4,5,6\) are

\[
(7,2,1,10).
\]

Therefore

\[
\{1,2,7,10\}
\]

is the third zero-avoiding template

\[
\{r_3,r_4,r_5,i_1\}
\]

of this class-E row.  This directly contradicts its appearance in the
claimed missing list.

## 4. Complete class-E window audit

For compactness, a string such as \(127\,10\) denotes the set
\(\{1,2,7,10\}\).  The columns \(Z_1,\ldots,Z_4\) are the four
zero-containing templates (2.1), and \(N_1,\ldots,N_7\) are the seven
zero-avoiding templates (2.2).

| row \(R_4\mid I_4\) | \(Z_1,Z_2,Z_3,Z_4\) | \(N_1,\ldots,N_7\) |
|---|---|---|
| \(1357\mid2468\) | \(0468,0357,0358,0368\) | \(2468,1246,124\,10,129\,10,179\,10,579\,10,3579\) |
| \(1365\mid2487\) | \(0268,0457,0458,0568\) | \(2368,1236,123\,10,139\,10,179\,10,479\,10,4579\) |
| \(1437\mid2658\) | \(0458,0367,0378,0348\) | \(2458,1245,125\,10,129\,10,169\,10,679\,10,3679\) |
| \(1643\mid2875\) | \(0238,0467,0678,0278\) | \(2358,1235,135\,10,159\,10,149\,10,469\,10,4679\) |
| \(1453\mid2867\) | \(0248,0567,0578,0278\) | \(2348,1234,134\,10,139\,10,169\,10,569\,10,5679\) |
| \(2157\mid4368\) | \(0467,0359,0356,0367\) | \(2467,1247,124\,10,128\,10,189\,10,589\,10,3589\) |
| \(2165\mid4387\) | \(0267,0459,0456,0567\) | \(2367,1237,123\,10,138\,10,189\,10,489\,10,4589\) |
| \(4217\mid6538\) | \(0457,0389,0349,0345\) | \(2457,1257,\mathbf{127\,10},126\,10,168\,10,689\,10,3689\) |
| \(2317\mid6458\) | \(0456,0379,0349,0346\) | \(2456,1256,125\,10,128\,10,178\,10,789\,10,3789\) |
| \(6421\mid8753\) | \(0235,0689,0289,0239\) | \(2357,1357,157\,10,147\,10,146\,10,468\,10,4689\) |
| \(6231\mid8745\) | \(0236,0789,0279,0239\) | \(2356,1356,156\,10,145\,10,148\,10,478\,10,4789\) |
| \(4521\mid8673\) | \(0234,0589,0289,0249\) | \(2347,1347,137\,10,167\,10,156\,10,568\,10,5689\) |
| \(2351\mid8467\) | \(0246,0579,0259,0269\) | \(2346,1346,134\,10,138\,10,178\,10,578\,10,5789\) |
| \(2431\mid8657\) | \(0245,0679,0279,0249\) | \(2345,1345,135\,10,138\,10,168\,10,678\,10,6789\) |

Inspection of this complete table gives:

* among the claimed thirty-two holes, the only class-E occurrence is
  \(127\,10\), in the bold entry above;
* the 56 zero-containing occurrences have 44 distinct values: 32 occur
  once and 12 occur twice;
* the 98 zero-avoiding occurrences have 82 distinct values: 67 occur once,
  14 occur twice, and \(138\,10\) occurs three times.

Thus class E alone has 126 distinct cyclic-four values and internal
multiplicity profile

\[
99\text{ singles},\qquad26\text{ doubles},\qquad1\text{ triple}.
\tag{4.1}
\]

These are class-local multiplicities; occurrences from classes A--D must
still be added before drawing a global histogram.

## 5. Consequence for the splice-Hall argument

For a genuinely missing four-set \(C\), the seven-distinct-tail-wreath
argument is correct: every \(C+\beta\), \(\beta\notin C\), owns \(C\) by an
internal deletion, and two such five-sets cannot lie in one wreath without
making \(C\) an old four-window.

That theorem cannot currently be applied to the stated 32-set list,
because \(127\,10\) is not missing.  Any \(32\cdot7=224\) incidence count
and any Hall bound built from that particular list must be recomputed after
the true missing family is identified.

## 6. Class-E tail degrees for the corrected candidate family

Consider the provisional corrected family

\[
\mathcal H'=(\mathcal H_{\rm claimed}\setminus\{127\,10\})
             \cup\{347\,10\}.
\tag{6.1}
\]

For each class-E row, the table below lists the members of \(\mathcal H'\)
obtained by deleting internal position 1, 2, or 3 from one of its cyclic
five-windows.  These are exactly its backward-safe missing-colour
witnesses after both tail orientations are allowed.

| E row | delete position 1 | delete position 2 | delete position 3 | degree |
|---|---|---|---|---:|
| E1 | -- | -- | -- | 0 |
| E2 | \(136\,10,1479\) | \(0478,0256\) | \(0479,0258\) | 6 |
| E3 | \(0478\) | \(0258,259\,10,1269,0369\) | \(0347\) | 6 |
| E4 | \(1469,0478\) | \(1459,0479,0237\) | \(0258,0469\) | 7 |
| E5 | \(0258\) | \(1369,0247\) | \(136\,10,0569,0257,0478\) | 7 |
| E6 | \(0247,0369\) | \(0569,0347\) | \(247\,10,158\,10\) | 6 |
| E7 | \(0237,0569\) | \(0469,0257\) | \(0489,0256\) | 6 |
| E8 | \(0257,0369\) | \(0247,267\,10,0489\) | \(257\,10,0347\) | 7 |
| E9 | \(0256,0347,0469\) | \(258\,10,0479\) | \(0369\) | 6 |
| E10 | \(0489\) | \(0257,0469\) | \(0237\) | 4 |
| E11 | \(1478,0479,0237,2369\) | \(0256,136\,10,0489,0369\) | \(158\,10,0478\) | 10 |
| E12 | \(0347,136\,10\) | \(0237,158\,10,0569,0258\) | \(0247,347\,10,2589,0489\) | 10 |
| E13 | \(0256\) | \(0257,0469\) | \(158\,10,0569\) | 5 |
| E14 | \(0247\) | -- | \(0479\) | 2 |

Thus the class-E right-degree maximum for \(\mathcal H'\) is

\[
\boxed{\Delta_E=10,}
\tag{6.2}
\]

attained by E11 and E12.  The class-E incidence total is \(82\).
In particular, class E is consistent with the degree-at-most-ten bound
which would imply a matching of more than 21 repairs if it held over all
forty-two rows.  This table alone does not establish the global bound.
