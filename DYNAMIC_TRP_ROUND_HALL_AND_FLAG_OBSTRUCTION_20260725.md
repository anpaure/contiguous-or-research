# Dynamic TRP: exact round Hall systems and an upper-flag obstruction

Date: 2026-07-25

This note works only with the truncated carrier rotor.  No computational
input is used.

## 0. Outcome

Put

\[
 M=m+H,\qquad a=H-Q,\qquad b=m-Q,
\]

and take one radius-\(Q\) carrier state at every
\(U\in\binom{[2m]}M\).  One transition has \(a\) arrival choices and
\(b\) delayed-departure choices.

There is an exact round decomposition.

* The arrival chooses the next middle owner, every next upper flag, and
  every next lower flag except the deepest lower flag.
* After the arrivals have been chosen, the delayed-departure choice controls
  only the next depth-\(Q\) lower flag.

Thus owner distinctness in one round is an ordinary capacitated Hall
problem of left degree \(a\), and the final depth-\(Q\) lower choices form
a second ordinary capacitated Hall problem of left degree \(b\).  The
intermediate simultaneous arrival problem is instead a common transversal
of \(2Q+1\) partition systems.  Separate rowwise Hall conditions do not in
general glue.

More sharply, there are asymptotically legitimate collections of current
states for which

1. all current owners are distinct;
2. the candidate next-owner sets of different carriers are pairwise
   disjoint, so owner Hall holds with maximum slack;
3. nevertheless the candidate depth-\(Q\) upper flags of
   \(K(H-Q)+1\) carriers lie in the same set of only \(H-Q\) targets.

Consequently no choice can respect upper-flag capacity \(K\), and all
\(m-Q\) delayed-departure choices are irrelevant to this failure.  The
example applies with the natural balanced capacity

\[
 K=\left\lceil {MN_H\over N_Q}\right\rceil.
\]

This is not a counterexample to TRP, because a global construction may
avoid the bad state fibre.  It is an exact obstruction to proving TRP by
owner Hall followed by unrestricted delayed-departure choices.  A successful
dynamic proof needs a maintained flag-fibre congestion invariant.

## 1. One transition, exactly

Fix a carrier \(U\) and a state

\[
 \omega=(L;z_1,\ldots,z_{2Q};R),
 \qquad |L|=b,\quad |R|=a.
 \tag{1.1}
\]

For \(x\in L\) and \(y\in R\), its rotor successor is

\[
 \omega'=(L-x+y;\ x,z_1,\ldots,z_{2Q-1};\ R-y+z_{2Q}).
 \tag{1.2}
\]

Use signs to distinguish lower and upper rows.  Put

\[
 A_0=L\cup\{z_1,\ldots,z_{Q-1}\},                 \tag{1.3}
\]

\[
 A^-_q=L\cup\{z_1,\ldots,z_{Q-q-1}\}
 \quad(1\le q<Q),                                  \tag{1.4}
\]

\[
 A^+_q=L\cup\{z_1,\ldots,z_{Q+q-1}\}
 \quad(1\le q\le Q).                              \tag{1.5}
\]

An empty displayed interval of \(z\)'s is omitted.  Direct substitution
in the flag definitions gives

\[
 X(\omega')=A_0+y,                                  \tag{1.6}
\]

\[
 L_q(\omega')=A^-_q+y\quad(1\le q<Q),              \tag{1.7}
\]

\[
 U_q(\omega')=A^+_q+y\quad(1\le q\le Q),          \tag{1.8}
\]

whereas

\[
 L_Q(\omega')=L-x+y.                                \tag{1.9}
\]

Indeed, in every row in (1.6)--(1.8), the element \(x\) removed from
\(L\) is immediately restored as the new first queue element.  At the
deepest lower row the queue prefix is empty, so the cancellation does not
occur.

Equations (1.6)--(1.9) are the exact arrival/departure separation.  Notice
that the delayed choice is rich, \(|L|=m-Q\), but it is completely invisible
to all the new upper flags.

## 2. Exact Hall condition for owners

Let \(I\) be the carrier set in one round.  For carrier \(i\), let
\(A_{i,0}\) and \(R_i\) be (1.3) and the current arrival reservoir.  Let
\(c_0(S)\in\{0,1\}\) be the residual owner capacity; in the no-repetition
problem it is one precisely for owners not used in earlier rounds.

The candidate graph has left part \(I\), right part
\(\binom{[2m]}m\), and edge

\[
 i\sim A_{i,0}+y\qquad(y\in R_i)
 \tag{2.1}
\]

whenever that target has positive residual capacity.  There are distinct
next owners if and only if

\[
 \boxed{
 |J|\le
 \sum_{S\in N_0(J)}c_0(S)
 \quad\hbox{for every }J\subseteq I.}
 \tag{OH}
\]

This is just capacitated Hall, and is both necessary and sufficient.
Equivalently, after replacing a right target by \(c_0(S)\) clones, it is
ordinary Hall.

A useful elementary sufficient form is

\[
 \min_{i\in I}\deg(i)\ge
 \max_S\deg(S).
 \tag{2.2}
\]

Indeed edge counting gives
\(\delta |J|\le \Delta |N_0(J)|\).

Owner distinctness alone does not imply (OH).  For example, take a fixed
\((m-1)\)-set \(C\), a fixed \(a\)-set \(R\) disjoint from it, and
\(a+1\) distinct elements \(d_i\) outside \(C\cup R\).  States can be
chosen with current owner \(C+d_i\), scheduled departure \(d_i\), and
arrival reservoir \(R\).  Their current owners are distinct, but every
candidate owner family is

\[
 \{C+y:y\in R\},
\]

so Hall fails.  Thus a dynamic proof already needs an owner-fibre
expansion invariant; distinctness of the current layer is insufficient.

## 3. The simultaneous arrival system

For every carrier \(i\) and arrival \(y\in R_i\), define its arrival
column

\[
 \mathcal E_i(y)=
 \bigl(A_{i,0}+y;\ (A^-_{i,q}+y)_{1\le q<Q};\
 (A^+_{i,q}+y)_{1\le q\le Q}\bigr).
 \tag{3.1}
\]

The coordinates are rank-tagged.  If every target currently has residual
capacity zero or one, choosing the arrivals is exactly the problem of
choosing one column \(\mathcal E_i(y_i)\) per carrier such that the selected
columns are coordinatewise disjoint and avoid exhausted targets.  With
larger residual capacities it is the same statement after cloning each
target by its remaining capacity.

On the ground set

\[
 \{(i,y):i\in I,\ y\in R_i\},
\]

the carrier condition and every individual rank condition are partition
matroids.  The desired arrival set is a common base of \(2Q+1\) such
systems.  Each single row has its own capacitated Hall theorem, but
intersection of all the rows is not an ordinary bipartite matching
problem.  In particular, rowwise Hall conditions cannot simply be checked
independently.

After arrivals \(y_i\) have been selected, the only unfinished new row is
the deepest lower row.  Its candidate graph is

\[
 i\sim L_i-x+y_i\qquad(x\in L_i).                  \tag{3.2}
\]

If \(c^-_Q(S)\) is the residual capacity in that row, delayed departures
exist if and only if

\[
 \boxed{
 |J|\le
 \sum_{S\in N^-_Q(J)}c^-_Q(S)
 \quad\hbox{for every }J\subseteq I.}
 \tag{DH}
\]

This second exact Hall system has raw left degree \(b=m-Q\), much larger
than the arrival degree \(a=H-Q\).  It solves the current deepest row only;
the selected \(x_i\)'s also shape bases in later rounds, so (DH) by itself
is not a continuation theorem.

### 3.1 A quantitative one-round sufficient condition

There is a useful rigorous condition between raw rowwise Hall and the full
common-transversal problem.  Delete an arrival option \((i,y)\) if any
coordinate of \(\mathcal E_i(y)\) is already saturated.  On the remaining
options put an edge between \((i,y)\) and \((j,y')\), \(i\ne j\), when the
two columns use the same target in at least one rank.  Call this the
arrival-conflict graph.

Suppose every carrier retains at least \(s\) options, every carrier has at
most \(a\) options, and the maximum degree of the arrival-conflict graph is
\(\Delta\).  If

\[
 \boxed{s^2\ge e(2a\Delta+1),}                     \tag{3.3}
\]

then one can choose one arrival option per carrier with no conflict in any
arrival-controlled row.

Indeed, choose one remaining option independently and uniformly from every
carrier.  For each conflict edge, the event that both endpoints are chosen
has probability at most \(s^{-2}\).  Such an event is dependent only on
conflict events involving one of its two carrier parts.  Each part is
incident with at most \(a\Delta\) conflict edges, so the dependency degree
is at most \(2a\Delta\).  The symmetric Lovasz local lemma proves (3.3).

In the unfiltered case \(s=a\), the simple condition

\[
 \Delta\le {a\over 3e}                              \tag{3.4}
\]

is sufficient for all large \(a\).  Combining this independent transversal
with (DH) gives a complete one-round extension respecting every residual
quota.  Consequently a dynamic proof of TRP would follow from maintaining
through all \(M\) rounds:

* a positive fraction of the \(H-Q\) arrival options at every carrier;
* cross-carrier arrival-column conflict degree \(O(H-Q)\) with a small
  enough constant (or a sharper independent-transversal substitute);
* the deepest-lower Hall inequalities (DH).

This is a genuine partial theorem, but it is an invariant hypothesis, not
something implied by owner Hall.

## 4. Balanced capacities imply TRP if every round extends

Let

\[
 T=MN_H.
\]

For every controlled rank \(r\), prescribe a balanced integral quota
vector of total mass \(T\):

\[
 b_r(S)\in
 \left\{\left\lfloor {T\over\binom{2m}r}\right\rfloor,
              \left\lceil {T\over\binom{2m}r}\right\rceil\right\},
 \qquad \sum_S b_r(S)=T.                            \tag{4.1}
\]

Suppose the \(M\) rounds can be extended using (3.1) and (3.2), never
exceeding any quota (4.1).  Since every row emits exactly \(T\) occurrences,
every quota is then attained exactly.  Its support size is

\[
 \min\left\{T,\binom{2m}r\right\}.                 \tag{4.2}
\]

At the calibrated first crossing, write \(D=W-T\).  The exact calibration
gives

\[
 D=O(WH/m).                                         \tag{4.3}
\]

Moreover

\[
 \sum_{q=0}^{Q}(N_q-T)_+
 =O\left({W H^{3/2}\over m}\right)=o(W).           \tag{4.4}
\]

To verify (4.4), use

\[
 \log {W\over N_q}\ge {q^2\over m+q}.
\]

For \(q^2=O(H)\), this implies

\[
 W-N_q\ge (1+o(1)){Wq^2\over 2m}.
\]

Hence \(N_q>T\) can hold only for \(q=O(\sqrt H)\).  There are
\(O(\sqrt H)\) such terms, each at most \(D\), proving the first estimate.
Finally

\[
 {H^{3/2}\over m}
 =m^{-1/4}(\log m)^{3/4+o(1)}=o(1).
\]

Counting both sides of the band changes only the absolute constant.
Therefore exact completion of the dynamic balanced-quota system is a
strict sufficient theorem for (TRP).

## 5. Exact upper-flag obstruction despite perfect owner Hall

The following construction shows why the owner Hall system and the large
delayed-departure degree do not finish the dynamic argument.

### Theorem 5.1 (common upper-star obstruction)

Let \(K\ge1\), put \(s=Ka+1\), and assume

\[
 s\le m-H+1,
 \qquad m\ge 2H-Q,
 \qquad \binom{m+Q-2}{Q-1}\ge s.                   \tag{5.1}
\]

There are \(s\) distinct carriers with legitimate radius-\(Q\) states
such that:

1. their current owners are distinct;
2. their next-owner candidate sets are pairwise disjoint;
3. all their next depth-\(Q\) upper candidate sets equal the same
   \(a\)-element family.

Consequently the owner Hall condition holds for every subfamily, but no
transition choice can keep every depth-\(Q\) upper target below capacity
\(K\).  This remains true after arbitrary choices among all \(b=m-Q\)
delayed departures.

#### Proof

Choose pairwise disjoint sets

\[
 |B|=m+Q-1,\qquad |R|=a,\qquad
 E=\{e_1,\ldots,e_s\},                              \tag{5.2}
\]

which is possible by (5.1).  Fix \(w\in B\).  Choose distinct
\((m-1)\)-sets

\[
 C_i\subseteq B\setminus\{w\},\qquad 1\le i\le s.
\tag{5.3}
\]

There are far more than \(s\) such sets in the stated asymptotic range.
Put

\[
 X_i=C_i+w.                                          \tag{5.4}
\]

Partition \(B\) as follows.  Set \(z_{i,Q}=w\); choose
\(z_{i,1},\ldots,z_{i,Q-1}\) in \(C_i\); let

\[
 L_i=X_i\setminus\{z_{i,1},\ldots,z_{i,Q}\};       \tag{5.5}
\]

and order the \(Q-1\) elements of \(B\setminus X_i\) as
\(z_{i,Q+1},\ldots,z_{i,2Q-1}\).  Finally put

\[
 z_{i,2Q}=e_i,qquad R_i=R,qquad
 U_i=B\cup R\cup\{e_i\}.                            \tag{5.6}
\]

These data form a legitimate state on the distinct carrier \(U_i\).
Its current owner is \(X_i\), so the owners are distinct.  From (1.3)
and (5.5),

\[
 A_{i,0}=X_i-w=C_i.                                  \tag{5.7}
\]

Thus its next-owner candidates are \(C_i+y\), \(y\in R\).  Since
\(B\cap R=\varnothing\) and the \(C_i\)'s are distinct, these candidate
families are pairwise disjoint.  Owner Hall therefore holds with strict
slack except at singletons.

On the other hand, (1.5) and the partition of \(B\) give

\[
 A^+_{i,Q}=L_i\cup\{z_{i,1},\ldots,z_{i,2Q-1}\}=B
 \tag{5.8}
\]

for every \(i\).  All depth-\(Q\) upper candidates are consequently

\[
 \{B+y:y\in R\},                                    \tag{5.9}
\]

the same family of \(a\) targets.  Their total capacity is \(Ka<s\).
This violates capacitated Hall in that row.  Formula (1.8) shows that
\(x_i\) does not occur in these targets, so none of the \(b\) delayed
choices can alter the obstruction. \(\square\)

### Corollary 5.2 (the obstruction occurs at the natural TRP scale)

Assume here the intended truncation regime

\[
 \frac{Q^2}{m}=(1+o(1))\log\log m.                 \tag{5.10}
\]

Take

\[
 K=\left\lceil {T\over N_Q}\right\rceil.
\tag{5.11}
\]

For the TRP parameters,

\[
 {W\over N_Q}
 =\exp\left({Q^2\over m}+o(1)\right)
 =(\log m)^{1+o(1)}.                                \tag{5.12}
\]

Hence

\[
 K(H-Q)
 \le m^{1/2}(\log m)^{3/2+o(1)}=o(m).              \tag{5.13}
\]

The hypotheses (5.1) therefore hold for all sufficiently large \(m\).
Even when every upper target begins with its full natural balanced
capacity, owner Hall does not prevent an immediate upper-flag quota
failure.

## 6. A fresh random round is simultaneously sparse

The preceding obstruction is adversarial.  It is not typical of the full
state catalogue.  In fact all rows can be handled simultaneously in one
fresh round, apart from a vanishing fraction of carriers.

### Theorem 6.1 (fresh-round simultaneous transversal)

Independently at every carrier \(U\), choose a uniform state
\(\omega_U\in\Omega_Q(U)\).  Expose all

\[
 A:=ab=(m-Q)(H-Q)                                    \tag{6.1}
\]

outgoing transition options \((x,y)\).  Join two options from distinct
carriers when their successor states have the same flag in at least one of
the \(2Q+1\) controlled rows (the owner row is counted once).

There is a deterministic realization of the current states and a set of

\[
 (1-o(1))N_H                                         \tag{6.2}
\]

carriers for which one may choose one outgoing transition per retained
carrier so that their next owners and every one of their lower and upper
flags through depth \(Q\) are pairwise distinct within the corresponding
rank.

#### Proof

Fix a controlled row of rank \(r=m\pm q\).  For a fixed top \(U\), a
uniform state followed by a uniform outgoing transition has a uniform
successor state, because the carrier rotor is regular.  Its rank-\(r\)
flag is therefore uniform in \(\binom Ur\).  Equivalently, for a fixed
\(S\in\binom Ur\), the expected number among all \(A\) outgoing options
whose successor flag is \(S\) equals

\[
 {A\over\binom Mr}.                                  \tag{6.3}
\]

States at distinct carriers are independent.  The expected number
\(C_r\) of conflict edges created by this row is consequently at most

\[
\begin{aligned}
 \mathbb E C_r
 &\le {1\over2}\sum_{S\in\binom{[2m]}r}
 \left(
   \binom{2m-r}{M-r}{A\over\binom Mr}
 \right)^2\\
 &= {A^2N_H^2\over2\binom{2m}r}.                    \tag{6.4}
\end{aligned}
\]

The last equality is the standard containment identity

\[
 {\binom{2m-r}{M-r}\over\binom Mr}
 ={N_H\over\binom{2m}r}.                            \tag{6.5}
\]

Let \(C\) be the total conflict-edge count over all rows.  Since the two
rank-\((m\pm q)\) layers have common size \(N_q\), (6.4) gives

\[
 {2\mathbb E C\over A N_H}
 \le {A\over\lambda_H}
 \left(1+2\sum_{q=1}^{Q}\lambda_q\right).          \tag{6.6}
\]

The left side is the expected average conflict degree.  Now

\[
 \lambda_H\ge M\sim m,
 \qquad
 \lambda_q\le\lambda_Q=(\log m)^{1+o(1)},
\]

so

\[
 {1+2\sum_{q\le Q}\lambda_q\over\lambda_H}
 =O\left({Q\lambda_Q\over m}\right)=o(1).          \tag{6.7}
\]

Choose a realization whose average conflict degree obeys (6.6).  Fix
\(\delta<1/(8e)\), and delete every option of conflict degree exceeding
\(\delta A\).  Equations (6.6)--(6.7) show that only \(o(AN_H)\) options
are deleted.  Delete also every carrier which lost more than \(A/2\)
options.  This removes only \(o(N_H)\) carriers.

Every remaining carrier part has at least \(A/2\) options, and the induced
conflict graph has maximum degree at most \(\delta A\).  Apply the
one-round local-lemma criterion (3.3), now with raw part size \(A\),
retained size \(A/2\), and \(\Delta=\delta A\).  The inequality is

\[
 {A^2\over4}\ge e(2\delta A^2+1),                  \tag{6.8}
\]

which holds for all large \(A\).  The resulting independent transversal
chooses one full transition \((x,y)\) per retained carrier and has no
collision in any controlled row. \(\square\)

Theorem 6.1 is stronger than separate owner and flag Hall statements for
one unsaturated round.  Its limitation is exactly temporal: the selected
successor states are neither independent nor certified uniform, and after
many rounds some targets have exhausted quota.  Reapplying the theorem
therefore requires a propagation or mixing invariant not presently
proved.  If a version with the same \(o(N_H)\) exceptional count held
conditionally at every one of the \(M\) rounds, the aggregate exceptional
state count would be \(o(MN_H)=o(W)\), and Section 4 would finish TRP.

## 7. Exact frontier

The dynamic TRP route has been reduced to a precise invariant problem.
At every round one must maintain, simultaneously:

1. owner-fibre expansion (OH);
2. a common-transversal condition for all arrival-controlled rows in
   (3.1), not merely separate rowwise Hall;
3. deepest-lower expansion (DH);
4. enough future dispersion of the selected \(x_i\)'s that the next
   arrival-column bases do not form common-star clusters of Theorem 5.1.

The raw choice inequality

\[
 m-Q\gg H-Q\gg Q
\]

is favorable but not sufficient.  The large delayed-departure freedom can
repair the current deepest lower row and can shape later bases; it cannot
repair any current upper-row concentration.  A proof of TRP along this
line therefore needs a quantitative propagation theorem saying that the
\(m-Q\) delayed choices keep all future arrival-star congestion below the
available balanced capacities.  Theorem 5.1 shows that this propagation
condition is genuine rather than a cosmetic strengthening of owner Hall.
