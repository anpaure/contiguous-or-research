# Corrected closure of the canonical K=11 backward-tail Hall count

Date: 2026-07-25

## 1. Result

Let

\[
 \mathcal H'=
 \bigl(\mathcal H_{\rm old}\setminus\{\{1,2,7,10\}\}\bigr)
 \cup\{\{3,4,7,10\}\}.
\]

The existing A--E cyclic-four audits prove that every member of
\(\mathcal H'\) is absent from the canonical cyclic-four support.  For a
canonical wreath row \(Q\), join \(Q\) to \(C\in\mathcal H'\) when one of
the eleven cyclic five-windows of \(Q\), after deletion of an internal
position \(1,2\), or \(3\), equals \(C\).  This is exactly the
backward-safe tail incidence graph after both orientations are allowed.

The corrected row degrees satisfy

\[
 \boxed{\Delta=10}.
\]

Since every one of the 32 holes has degree seven, this graph has 224 edges.
Kőnig's theorem therefore gives

\[
 \boxed{\nu\ge \left\lceil\frac{224}{10}\right\rceil=23.}
\]

Thus the backward-tail Hall problem is closed with two units of slack over
the 21 distinct lower-colour repairs required by the support ledger.  This
does **not** yet impose the head double-block filter, the upper-colour
ledger, one common port per wreath, or acyclicity.

No search or program is used below.

## 2. Four omissions in the former class-E tail table

The table in
`K11_CANONICAL_CYCLIC4_SUPPORT_HAND_AUDIT_20260725.md` omitted four
internal-deletion witnesses.  Write `A` for coordinate 10.

The relevant rows and literal cyclic five-windows are:

\[
\begin{array}{c|c|c|c}
\text{row}&\text{cyclic order}&\text{five-window}&\text{deleted entry / hole}\\ \hline
E9 &(0,4,6,5,2,1,A,8,7,9,3)&(5,2,1,A,8)&2\,/\,158A\\
E13&(0,2,6,4,3,1,A,8,7,5,9)&(6,4,3,1,A)&4\,/\,136A\\
E14&(0,2,4,5,3,1,A,8,6,7,9)&(5,3,1,A,8)&3\,/\,158A\\
E14&(0,2,4,5,3,1,A,8,6,7,9)&(3,1,A,8,6)&8\,/\,136A.
\end{array}
\]

All four deleted entries are internal.  Hence the corrected E-row degrees
are unchanged except for

\[
 d(E9)=7,\qquad d(E13)=6,\qquad d(E14)=4.
\]

The corrected class-E incidence total is

\[
 \boxed{86}
\]

rather than 82, while its maximum remains

\[
 \boxed{\Delta_E=10}.
\]

There is also a conceptual check.  The hole \(136A\) has the seven
five-supersets obtained by adding \(0,2,4,5,7,8,9\).  Its previously listed
owners accounted for only five of them; the E13 and E14 witnesses above
are exactly the missing \(4\)- and \(8\)-supersets.  Likewise, the E9 and
E14 witnesses complete the seven supersets of \(158A\).

## 3. Complete class-A incidence table

For a cyclic five-window \((p_0,p_1,p_2,p_3,p_4)\), the three candidates
are

\[
 \{p_0,p_2,p_3,p_4\},\quad
 \{p_0,p_1,p_3,p_4\},\quad
 \{p_0,p_1,p_2,p_4\}.
\]

Substitution in the fourteen displayed class-A orders gives the following
complete list.  Entries within a row are distinct.

| row | members of \(\mathcal H'\) obtained by an internal deletion | degree |
|---|---|---:|
| A1 | -- | 0 |
| A2 | \(267A,247A,0469,0169\) | 4 |
| A3 | \(1369,2369,2589,247A,047A,0478,136A\) | 7 |
| A4 | \(259A,247A,0479,047A\) | 4 |
| A5 | \(247A,257A,258A,0489,1369,0369,0169\) | 7 |
| A6 | \(0347,0147,1479,2369,2589,258A,158A\) | 7 |
| A7 | \(1478,257A,267A,259A,0569\) | 5 |
| A8 | \(1369,1469,2369,2589,257A,258A\) | 6 |
| A9 | \(1459,2589,2369,267A,0147,047A\) | 6 |
| A10 | \(257A,259A\) | 2 |
| A11 | \(259A,2369,267A,0169,1478,0478,0147\) | 7 |
| A12 | \(0147,247A,347A,2589,259A,258A,0169,0569\) | 8 |
| A13 | \(0147,257A,267A,0169,0489,1459\) | 6 |
| A14 | \(258A,0147,1479,0479,1469,0469,0169\) | 7 |

Consequently

\[
 \boxed{\Delta_A=8},\qquad
 \sum_{j=1}^{14}d(A_j)=76.
\]

The total 76 provides an independent completeness check.  The already
audited class totals, after the four E corrections, are

\[
 \sum_Bd(B)=17,\qquad
 \sum_{C\cup D}d=45,\qquad
 \sum_Ed(E)=86.
\]

Therefore

\[
 76+17+45+86=224=32\cdot7.
\]

The orientation-complete seven-witness theorem says each member of
\(\mathcal H'\) already contributes exactly seven incidences in distinct
tail wreaths.  Hence the displayed 224 incidences exhaust the graph; there
can be no omitted A--E incidence.

## 4. Hall conclusion

Combining the row maxima gives

\[
 \Delta_A=8,\quad \Delta_B=5,\quad
 \Delta_{C\cup D}=8,\quad \Delta_E=10,
\]

and hence global maximum right degree ten.  If a vertex cover has size at
most 22, it covers at most \(22\cdot10=220\) of the 224 edges.  Therefore
every vertex cover has size at least 23, and Kőnig's theorem proves the
matching bound in Section 1.

## 5. Exact remaining finite gate

The corrected theorem supplies 23 distinct holes on 23 distinct tail
wreaths before the head filter.  A length-465 construction needs at least
21 net lower repairs and, simultaneously, at least 21 net complementary
upper repairs.  It remains to prove one of the following stronger coupled
statements:

1. the head-surviving subgraph still has a 21-matching; or
2. two discarded tail matches can absorb every head double-block while
   retaining 21 distinct lower colours; and then
3. the chosen incidences admit common head ports, the required upper
   colours, a 36-arc transversal directed forest, and cut-loss at most 11
   in both ledgers.

The present note proves the backward Hall resource exactly; it does not
claim the physical rainbow port-forest theorem or a length-465 word.
