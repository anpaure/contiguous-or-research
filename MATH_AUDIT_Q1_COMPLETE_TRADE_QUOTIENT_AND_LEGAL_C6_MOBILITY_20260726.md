# Audit of the complete \(q=1\) trade quotient and legal \(C_6\) certificate

Date: 2026-07-26

Audited file:
MATH_THEOREM_Q1_COMPLETE_TRADE_QUOTIENT_AND_LEGAL_C6_MOBILITY_20260726.md.

Method: pure mathematics only.  No computation, search, or external input
is used.

## 0. Verdict

The substantive finite certificate is correct.

1. The two displayed lists are simple cycles of length

   \[
                            \binom62=15,
   \]

   not full-owner Hamilton cycles of \(J(6,3)\).  Each lower two-set occurs
   exactly once.  They are therefore exactly the lower-rainbow saturating
   objects required by the even-ground \(q=1\) gate.
2. The changed edges form precisely the advertised one-copy lower-neutral
   \(C_6\).  Its outside endpoint matching is

   \[
                            R=\{14,26,35\},
   \]

   which is disjoint from both shores.  The switch consequently preserves
   one cycle.
3. The old cycle has four upper holes and four units of repeat excess; the
   new cycle has three of each.  Hence

   \[
                            (M^+,R^+):(4,4)\longmapsto(3,3)
   \]

   is exact.

The complete signed-image theorem is also consistent with its stated
quantifiers \(m\ge2,\ n\ge m+3\).  The remaining corrections are
terminological or local proof qualifications, recorded in Section 5.

## 1. Exact saturating-cycle audit

Put \(m=3,n=6\).  The lower and upper target layers both have size

\[
 |\tbinom{[6]}2|=|\tbinom{[6]}4|=15,                         \tag{1.1}
\]

whereas the middle layer has size \(\binom63=20\).  Thus a cycle using all
lower colours once must have length fifteen; it cannot be Hamilton in the
full graph \(J(6,3)\).

The old cyclic owner list is

\[
\begin{aligned}
126,236,136,156,125,256,456,245,234,123,\\
135,345,346,146,124.
\end{aligned}                                                 \tag{1.2}
\]

Its consecutive intersections, including the closing edge, are

\[
26,36,16,15,25,56,45,24,23,13,35,34,46,14,12.                \tag{1.3}
\]

These are respectively

\[
\begin{gathered}
12,13,14,15,16,\quad
23,24,25,26,\quad
34,35,36,\quad45,46,\quad56
\end{gathered}                                                 \tag{1.4}
\]

in a different order.  Hence every lower two-set occurs once.  Every
intersection in (1.3) has size two, so every consecutive owner pair is a
Johnson edge.  The fifteen owners in (1.2) are distinct.

The new cyclic owner list is

\[
\begin{aligned}
126,136,236,256,125,156,456,245,234,123,\\
135,345,346,146,124.
\end{aligned}                                                 \tag{1.5}
\]

Its consecutive intersections are

\[
16,36,26,25,15,56,45,24,23,13,35,34,46,14,12,                \tag{1.6}
\]

again exactly the family (1.4).  Its owners are the same fifteen owners as
in (1.2), merely reordered.  Thus both states are simple lower-rainbow
saturating cycles.

There is a useful equivalent description, but its rank must be stated.
The cyclic lower-colour lists (1.3) and (1.6) are Hamilton cycles of
\(J(6,2)\), and the union of each consecutive lower pair is the intervening
middle owner.  They are not Hamilton cycles of \(J(6,3)\).

## 2. Exact \(C_6\) and port-order audit

In the general \(C_6\) construction take

\[
 K=\{6\},\qquad p=5,\qquad
 (a,b,c,d)=(1,2,3,4).                                        \tag{2.1}
\]

The six touched owners are

\[
\begin{aligned}
X_1&=126,&X_2&=236,&X_3&=256,\\
X_4&=456,&X_5&=156,&X_6&=136.
\end{aligned}                                                 \tag{2.2}
\]

The old and new shores are

\[
 M^-=\{X_1X_2,X_3X_4,X_5X_6\},\qquad
 M^+=\{X_2X_3,X_4X_5,X_6X_1\}.                              \tag{2.3}
\]

All three old edges occur in (1.2), with \(X_5X_6\) traversed in the
reverse direction.  Deleting them leaves the following three paths:

\[
\begin{aligned}
&X_2-X_6,\\
&X_5-125-X_3,\\
&X_4-245-234-123-135-345-346-146-124-X_1.
\end{aligned}                                                 \tag{2.4}
\]

Therefore the quotient endpoint matching is exactly

\[
 R=\{X_2X_6,X_3X_5,X_1X_4\}=\{26,35,14\}.                    \tag{2.5}
\]

In the cyclic labelling of the six touched owners,

\[
 M^-=\{12,34,56\},\qquad M^+=\{23,45,61\}.                   \tag{2.6}
\]

The matching (2.5) is disjoint from both shores.  Moreover,

\[
 1-6-2-3-5-4-1                                                \tag{2.7}
\]

alternates between \(M^+\) and \(R\), so \(M^+\cup R\) is one six-cycle.
Thus inserting \(M^+\) preserves connectedness.  Expanding the three
quotient paths gives exactly the new cyclic list (1.5).  This proves legal
Hamiltonity at the quotient level and legal saturating-cycle connectivity
at the physical level.

The lower ledgers also agree literally:

\[
\begin{array}{c|ccc}
 &1&2&3\\ \hline
M^-&Kb&Kp&Ka\\
M^+&Kb&Kp&Ka.
\end{array}                                                 \tag{2.8}
\]

Here \(Kb=26,Kp=56,Ka=16\), which are pairwise distinct.  Hence this is a
one-copy lower-neutral packet, not merely a signed lower cancellation.

## 3. Upper histogram audit

Taking consecutive unions in (1.2) gives

\[
\begin{array}{c|lllllllllllllll}
C_{\rm old}
&1236&1236&1356&1256&1256&2456&2456&2345\\
&&1234&1235&1345&3456&1346&1246&1246 .
\end{array}                                                 \tag{3.1}
\]

Thus the four load-two targets are

\[
                         1236,1256,2456,1246,                 \tag{3.2}
\]

and the four holes are

\[
                         1245,1456,2346,2356.                 \tag{3.3}
\]

Every other upper four-set has load one.

For the new cycle, the union list is

\[
\begin{array}{c|lllllllllllllll}
C_{\rm new}
&1236&1236&2356&1256&1256&1456&2456&2345\\
&&1234&1235&1345&3456&1346&1246&1246 .
\end{array}                                                 \tag{3.4}
\]

Its three load-two targets are

\[
                         1236,1256,1246,                       \tag{3.5}
\]

and its three holes are

\[
                         1245,1356,2346.                       \tag{3.6}
\]

The signed upper change is

\[
 e_{2356}+e_{1456}-e_{2456}-e_{1356}.                         \tag{3.7}
\]

Both positive targets in (3.7) were old holes.  Of the negative targets,
\(2456\) had old load two and \(1356\) had old load one.  Therefore only
the removal at \(2456\) lowers repeat excess, by one.

For completeness, for any upper histogram of total mass fifteen on
fifteen targets,

\[
\begin{aligned}
R^+&=\sum_U(u(U)-1)_+=15-|\{U:u(U)>0\}|,\\
M^+&=15-|\{U:u(U)>0\}|.
\end{aligned}                                                 \tag{3.8}
\]

Hence \(M^+=R^+\).  Equations (3.2)--(3.6) prove exactly

\[
                         (M^+,R^+)=(4,4)\longmapsto(3,3).      \tag{3.9}
\]

## 4. Quantifier audit of the trade theorem

The signed-image theorem is stated for

\[
                         m\ge2,\qquad n\ge m+3.                \tag{4.1}
\]

These are sufficient for both parts of the proof.

1. With \(k=m+1\), the point-kernel lemma needs

   \[
                            2\le k\le n-2,
   \]

   which is exactly implied by (4.1).
2. The five-coordinate \(C_6\) lift chooses \(p\) in an
   \((m-1)\)-set \(C\), so it needs \(m\ge2\), and then uses the four
   further points \(a,b,c,d\).  This is exactly \(n\ge m+3\).

When Section 6 specializes to even ground \(n=2m\), the global hypothesis
\(n\ge m+3\) becomes \(m\ge3\).  This should be stated explicitly in that
section.  It causes no loss in the asymptotic application.

The parity claim is also correct.  Lucas' criterion gives

\[
 \binom{2m}{m-1}\equiv1\pmod2
 \quad\Longleftrightarrow\quad
 (m-1)\mathbin{\&}(m+1)=0.                                   \tag{4.2}
\]

If \(m\) is even, both operands in (4.2) are odd.  If \(m\) is odd and
\(2^a\Vert(m+1)\), every bit of \(m+1\) above position \(a\) also occurs
in \(m-1=(m+1)-2\).  The intersection vanishes exactly when there is no
such upper bit, namely when \(m+1=2^a\).  Thus

\[
 \binom{2m}{m-1}\text{ is odd}
 \quad\Longleftrightarrow\quad m=2^a-1.                       \tag{4.3}
\]

## 5. Corrections and terminology

The audit found the following presentation issues.  They have now been
incorporated into the consolidated theorem; the list is retained to record
the exact scope corrections.

1. Define the two defect statistics before their first use:

   \[
   M^+=|\{U:u(U)=0\}|,\qquad
   R^+=\sum_U(u(U)-1)_+.
   \]

2. The phrase “support-minimal for an exact lower-rainbow state” is too
   broad.  What Section 3.3 proves is:

   > The \(C_6\) has minimum shore size among nonzero binary owner-neutral
   > packets whose two shores use the same lower colours, once each.

   It does not prove minimum vertex support among all possible global
   switches.
3. The elementary implication used in the four-cycle minimality proof
   needs distinct outer owners:

   \[
   A\cap B=B\cap C=S,\quad A\ne C
   \quad\Longrightarrow\quad A\cap C=S.
   \]

   Without \(A\ne C\), the displayed implication is false.  The hypothesis
   is available because the overlay is a simple alternating four-cycle.
4. “Hamilton cycle” must retain its rank.  The finite certificate is a
   Hamilton cycle of the lower Johnson graph \(J(6,2)\) after projection,
   and a simple saturating 15-cycle in \(J(6,3)\).  It is not a Hamilton
   cycle of \(J(6,3)\), which has twenty vertices.  Accordingly,
   “legal lower-rainbow Hamilton fibre” should be replaced by
   “legal lower-rainbow saturating-cycle fibre,” unless the lower-rank
   projection is explicitly named.
5. In the final summary, the counterexample is fully displayed through the
   new holes in equation (5.9), so the clean reference is
   (5.1)--(5.9), not (5.1)--(5.8).
6. The explanatory parity paragraph should keep \(m\) and its divisibility
   condition inside mathematical delimiters; this is a rendering issue, not
   a mathematical error.

With these incorporated qualifications, the consolidated theorem has the correct proved
boundary: union defect is legally mobile already in the exact length-fifteen
lower-rainbow fibre, while global legal connectivity from an arbitrary
point-balanced saturating cycle remains open.
