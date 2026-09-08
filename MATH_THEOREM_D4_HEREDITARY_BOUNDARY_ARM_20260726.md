# The hereditary boundary arm of the explicit `D_4` packet

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let (F) be the canonical rooted `D_4` factor and (G) the explicit
fourteen-row factor of
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md`.  The marked first-insertion
slot is position (5=b_1) in the local coordinate word

\[
 q=(a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,9).
\tag{0.1}
\]

There is a genuine hereditary arm, but only for a precisely aligned
one-sided ancestor chain.

* If every ancestor target meets the local `D_4` word in the same singleton
  slot ({b_1}), then the same marked row sends
  (K_q\cup\{a\}) to (K_q\cup\{b\}) at every serviced depth (q).
  For example

  \[
  P=1345:\quad K_q\cup\{2\}\longmapsto K_q\cup\{6\},
  \tag{0.2}
  \]

  and

  \[
  P=1256:\quad K_q\cup\{4\}\longmapsto K_q\cup\{7\}.
  \tag{0.3}
  \]

* Merely saying that the ancestor window shares that boundary is not
  sufficient.  If the growing window also takes an adjacent local slot,
  its local carrier is a larger position set (A_q), and the action is
  determined by the full row words.  It need not remain (a\to b), and
  can become another arm, a multi-element replacement, or zero.
* Even on the singleton-aligned chain the complete legal choice is the
  whole fourteen-row factor trade.  Its exact boundary vector is

  \[
  -4e_2+4e_3-e_4-e_6+2e_7,
  \tag{0.4}
  \]

  not one isolated unit.  The other cyclic starts have total unresolved
  collar capacity much larger than the one marked arm and cancel it
  exactly when all nine starts acquire one common carrier.

Thus one parent-aligned switch can act on the whole hereditary tail
simultaneously at the level of a marked vertical arm.  It is not yet a
hereditary PCap repair: one must prove the singleton-carrier alignment,
destination slack, and favourable sign of the other thirteen rows and all
collar starts in the actual parent atlas.

## 1. Exact boundary-persistence lemma

For one affected ancestor target at depth (q), let (A_q\subseteq
\mathbb Z_9) be the set of local word positions retained by its carrier,
let (O_q) be its fixed exterior intersection, and let (iota) be the
inherited injection of local coordinates.  For a row (P), the old and
new physical targets are

\[
 T^F_{P,q}=O_q\cup\iota\{q^F_i(P):i\in A_q\},\qquad
 T^G_{P,q}=O_q\cup\iota\{q^G_i(P):i\in A_q\}.
\tag{1.1}
\]

This is the row-resolved context formula; no aggregation assumption is
being made.

### Lemma 1.1 (one-sided hereditary arm)

Suppose a nested family of ancestor windows is aligned so that

\[
                         A_q=\{5\}
       \qquad(q\in\mathcal Q_B).
\tag{1.2}
\]

If (q^F_5(P)=a) and (q^G_5(P)=b), then, with
(K_q=O_q),

\[
 e_{T^G_{P,q}}-e_{T^F_{P,q}}
 =e_{K_q\cup\{\iota(b)\}}-e_{K_q\cup\{\iota(a)\}}
 \qquad(q\in\mathcal Q_B).
\tag{1.3}
\]

In particular the same factor choice orients all depths in
(mathcal Q_B) coherently.

#### Proof

Substitute (A_q=\{5\}) into (1.1).  The exterior core may vary with
(q), but the local old/new singleton pair does not.  The packet choice is
one common integral choice, so the orientation is common to every depth.
(square)

For a pair-position block ([s,s+r)), the one-sided containing windows
([s+r-q,s+r)) all share the right boundary whenever the displayed start
is legal; the left-sided analogue is identical.  If the installed `D_4`
packet lies just outside that shared boundary, these windows satisfy
(1.2).  Hence a chain (q=r,r+1,\ldots,Q) has
(|\mathcal Q_B|=Q-r+1).  If the packet lies inside the growing side,
(1.2) fails and the next section is authoritative.

## 2. Boundary sharing alone does not preserve the marked arm

For the marked row (P=1345), the two local words are

\[
 q^F=145328679,\qquad q^G=314562789.
\tag{2.1}
\]

Starting at the marked position (5) and growing to the right gives

\[
\begin{array}{c|c|c|c}
A&F(A)&G(A)&\text{net set replacement}\\ \hline
\{5\}&\{2\}&\{6\}&2\to6\\
\{5,6\}&\{2,8\}&\{6,2\}&8\to6\\
\{5,6,7\}&\{2,8,6\}&\{6,2,7\}&8\to7\\
\{5,6,7,8\}&\{2,8,6,7\}&\{6,2,7,8\}&0.
\end{array}
\tag{2.2}
\]

Growing left already gives a two-for-two change at the second slot:

\[
 \{4,5\}:\qquad \{3,2\}\longmapsto\{5,6\}.
\tag{2.3}
\]

For (P=1256),

\[
 q^F=216543879,\qquad q^G=251673489,
\tag{2.4}
\]

and the right-growing carriers give

\[
\begin{array}{c|c|c|c}
A&F(A)&G(A)&\text{net set replacement}\\ \hline
\{5\}&\{4\}&\{7\}&4\to7\\
\{5,6\}&\{4,3\}&\{7,3\}&4\to7\\
\{5,6,7\}&\{4,3,8\}&\{7,3,4\}&8\to7\\
\{5,6,7,8\}&\{4,3,8,7\}&\{7,3,4,8\}&0.
\end{array}
\tag{2.5}
\]

Therefore there is no theorem of the form "every ancestor which shares
the boundary sees the same (a\to b) arm."  The correct hypothesis is
the singleton-carrier condition (1.2), or a separately verified equality
of the two set differences in (1.1).

## 3. Exact cumulative cap gain of one marked vertical arm

Let

\[
 A_q=K_q\cup\{a\},\qquad B_q=K_q\cup\{b\},
\tag{3.1}
\]

and let (mu_q) be the current full load histogram before the unit move
(A_q\to B_q).  Define gain as old cap tail minus new cap tail.  The
exact finite-difference identity is

\[
 \boxed{
 g_q(a\to b)
 =\mathbf1_{\{\mu_q(A_q)>p\}}
  -\mathbf1_{\{\mu_q(B_q)\ge p\}}.}
\tag{3.2}
\]

Consequently the common packet choice has exact marked-arm gain

\[
 \boxed{
 G_{\rm mark}
 =\sum_{q\in\mathcal Q_B}
  \left(
   \mathbf1_{\{\mu_q(A_q)>p\}}
   -\mathbf1_{\{\mu_q(B_q)\ge p\}}
  \right).}
\tag{3.3}
\]

If every source is overloaded and every destination has one free slot,
then

\[
                         G_{\rm mark}=|\mathcal Q_B|.
\tag{3.4}
\]

Thus a one-sided chain (q=r,\ldots,Q) really converts one physical row
move into (Q-r+1) units of hereditary cap descent.  This is not a
counting heuristic: it is the exact hinge finite difference.  Conversely,
if the destinations are already at cap throughout, the same marked move
has zero net gain; if they are at cap while some source is not overloaded,
it is harmful.

## 4. The other thirteen rows at the marked boundary

At the (b_1) slot the fourteen literal transitions are

\[
\begin{array}{c|c@{\ \to\ }c@{\qquad}c|c@{\ \to\ }c}
P&F&G&P&F&G\\ \hline
1234&8&8&1235&8&8\\
1236&8&7&1237&6&8\\
1245&8&3&1246&8&3\\
1247&6&3&1256&4&7\\
1257&4&3&1345&2&6\\
1346&2&8&1347&2&8\\
1356&2&2&1357&2&4.
\end{array}
\tag{4.1}
\]

Thus three rows are fixed and eleven change.  With one common exterior
core (K_q), the complete fourteen-row boundary vector is

\[
 \boxed{
 d^{\partial}_q
 =-4e_{K_q2}+4e_{K_q3}-e_{K_q4}-e_{K_q6}+2e_{K_q7},}
\tag{4.2}
\]

where (K_qx) abbreviates (K_q\cup\{\iota(x)\}).  Its positive and
negative masses are both six.

If the marked row is (1345:2\to6), the other thirteen rows alone have

\[
 -3e_{K_q2}+4e_{K_q3}-e_{K_q4}-2e_{K_q6}+2e_{K_q7},
\tag{4.3}
\]

again of positive and negative mass six.  Thus the marked row is not the
dominant part of its legal packet.

For (x\ge0), put

\[
 R_t(x)=(x-p)_+-(x-t-p)_+,
 \qquad
 A_t(x)=(x+t-p)_+-(x-p)_+.
\tag{4.4}
\]

Writing (mu_{q,x}=\mu_q(K_qx)), the exact old-minus-new gain of the
whole boundary sector is

\[
\boxed{
\begin{aligned}
G_{\partial}
=\sum_{q\in\mathcal Q_B}\bigl[&
 R_4(\mu_{q,2})+R_1(\mu_{q,4})+R_1(\mu_{q,6})\\
 &-A_4(\mu_{q,3})-A_2(\mu_{q,7})\bigr].
\end{aligned}}
\tag{4.5}
\]

Each summand lies in ([-6,6]).  It equals (6) when the three negative
cells have all the required removable excess and the two positive cells
have respectively four and two free slots.  The canonical plateau certifies
excess on its distinguished source only; it does not certify the other
four residual-capacity statements in (4.5).

## 5. Collar arms and the exact cancellation boundary

Let (delta_j) be the complete fourteen-row singleton vector at local
position (j).  Their positive masses are

\[
 (m_1,\ldots,m_9)=(5,7,6,7,6,3,4,6,0),
 \qquad \sum_jm_j=44.
\tag{5.1}
\]

The marked boundary is (j=5) and has mass six.  The other singleton
starts therefore carry a triangle-inequality disturbance budget thirty-eight
per depth.  More importantly, the exact identity is

\[
                         \sum_{j=1}^9\delta_j=0.
\tag{5.2}
\]

Hence if all nine starts at depth (q) acquire one common exterior core
and injection, the complete packet action is zero, including the marked
vertical arm.  A hereditary repair must physically separate the marked/open
sector from the compensating starts, not merely observe (3.2) in isolation.

For larger local carrier lengths the complete start-resolved positive-mass
totals are

\[
\begin{array}{c|cccccccc}
\ell&1&2&3&4&5&6&7&8\\ \hline
\sum_jm_{\ell,j}&44&56&60&39&39&60&56&44.
\end{array}
\tag{5.3}
\]

With a common carrier the aggregate packet cancels at lengths
(ell=1,4,5,8), survives with positive masses (19,22,22,19) at
(ell=2,3,6,7), and still has no background-independent cap sign.
Thus the conservative full-collar disturbance bound for one packet at one
depth is sixty, while the certified marked gain is at most one for one row
or six for the entire (b_1) sector.

All these profiles arise from a *legal* aligned substitution.  The changed
symbols (a_1,b_4) are internal exchange coordinates, not interface
states.  The interface states remain (X_0=P) and
(X_4=[8]\setminus P), and equality of the complete (X)- and
adjacent-union (Y)-ledgers proves exact gluing in every aligned context.

## 6. Decision

The explicit `D_4` factor supplies a real vertical primitive:

\[
 \sum_{q\in\mathcal Q_B}
  \left(e_{K_q\cup\{b\}}-e_{K_q\cup\{a\}}\right).
\tag{6.1}
\]

It can repair all depths of a one-sided hereditary chain simultaneously
if the source/destination hinge conditions hold.  Two facts prevent this
from being a completed absorber theorem.

1. A boundary-sharing chain is not automatically a singleton-carrier
   chain; (2.2)--(2.5) show the marked action changes as soon as the window
   grows into the local slab.
2. The integral move is the entire fourteen-row packet.  The exact
   boundary gain is (4.5), the other collar starts can cancel it as in
   (5.2), and the actual canonical residual capacities have not been
   shown to give favourable sign simultaneously over (q).

Therefore the correct next theorem is not another finite-factor existence
statement.  It is a **hereditary carrier-separation and residual-capacity
theorem** proving that a positive-density aligned packet bank satisfies
(1.2) and makes the sum of the full row-resolved hinge gains negative by
the amount required by PCap.
