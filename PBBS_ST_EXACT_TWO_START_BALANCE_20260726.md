# Exact two-start equations for Gaussian PBBS clustering

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, or
independence heuristic is used.

## 0. Outcome

Let

\[
 N=2m+1,
 \qquad B_m=\operatorname {Cat}_m,
 \qquad \tau=\phi^2,
 \qquad D_i=\tau^iD,
\]

and put

\[
 a_i=\delta(D_i),\qquad
 c_i=d(D_i),\qquad
 \widehat c_i=d(\phi D_i).
\tag{0.1}
\]

The exact first-maximum block rotation gives the cocycle identity

\[
 \boxed{a_{i+1}-a_i=c_i-\widehat c_i.}
\tag{0.2}
\]

The main result of this note is an exact reduction of the zero-winding
part of the two-point correlation to one equality between two boundary
blocks.

For a height-\(h\) root define

\[
 F_i^{(h)}
 =\sum_{j=0}^{h-1}c_{i+j}-a_{i+h}.
\tag{0.3}
\]

Then \(D_i\) starts a zero-winding return if and only if
\(F_i^{(h)}=0\).  Moreover, for every \(t\ge1\),

\[
 \boxed{
 F_{i+t}^{(h)}-F_i^{(h)}
 =\sum_{j=0}^{t-1}\widehat c_{i+h+j}
  -\sum_{j=0}^{t-1}c_{i+j}.}
\tag{0.4}
\]

Consequently two zero-winding starts at quotient distance \(t\) obey the
literal two-boundary balance

\[
 \boxed{
 \sum_{j=0}^{t-1}d(\tau^{i+j}D)
 =
 \sum_{j=0}^{t-1}d(\phi\tau^{i+h+j}D).}
\tag{0.5}
\]

This is stronger than equality of two marginal distributions: the two
blocks occur on opposite boundaries of the same exact PBBS passage.  It is
also the precise unresolved enumeration.  A proof that the solutions of
(0.3), (0.5), summed over \(h,t=O(\sqrt m)\), have bounded average
multiplicity would give the desired zero-winding part of
\(\mathcal C_H=O_A(R_H)\).

There are two rigorous limitations.

1. Positive-winding starts are not covered by (0.5).  The scalar winding
   ledger only gives

   \[
    R_H^+\le {H\over N}\sum_{D\in\mathcal D_m}d(D)
    =O_A(B_m)
   \tag{0.6}
   \]

   at \(H=\lceil A\sqrt m\rceil\), which is much too large at the
   critical scale \(B_m/H\).
2. No bounded-multiplicity injection can hold cycle by cycle.  The exact
   one-defect mountain rotor has \(2h-2\) zero-winding starts on a cycle
   of length \(2h-1\), and its local two-point ratio is asymptotic to
   \(h\).  This is an exact divergent cluster, although at its native
   rank it is outside the Gaussian ambient scaling and therefore does not
   decide the global \(m\)-rank ratio.

Thus neither \(\mathcal C_H=O_A(R_H)\) nor global divergent clustering is
proved.  The exact residual is the boundary-block equation (0.5), together
with a separate positive-winding two-start estimate.

## 1. The primal--dual deficit telescope

Write the canonical first-maximum factorization as

\[
 D_i=P_i1R_i0S_i.
\]

The two-step formula and its one-step companion give

\[
 c_i=N-a_i-\delta(\phi D_i),
\]

\[
 \widehat c_i=N-\delta(\phi D_i)-a_{i+1}.
\]

Subtracting proves (0.2).  Now use (0.3):

\[
\begin{aligned}
 F_{i+1}^{(h)}-F_i^{(h)}
 &=c_{i+h}-c_i-(a_{i+h+1}-a_{i+h})\\
 &=c_{i+h}-c_i-(c_{i+h}-\widehat c_{i+h})\\
 &=\widehat c_{i+h}-c_i.
\end{aligned}
\tag{1.1}
\]

Summing (1.1) for \(i,i+1,\ldots,i+t-1\) proves (0.4).

The telescope is not restricted to zero winding or to minimum duration.
For every fixed \(s\ge1\), define

\[
 F_i^{(s)}=\sum_{j=0}^{s-1}c_{i+j}-a_{i+s}.
\tag{1.2}
\]

The same calculation gives

\[
 \boxed{
 F_{i+t}^{(s)}-F_i^{(s)}
 =\sum_{j=0}^{t-1}\widehat c_{i+s+j}
  -\sum_{j=0}^{t-1}c_{i+j}.}
\tag{1.3}
\]

If \(D_i\) and \(D_{i+t}\) both return after step-two duration \(s\),
with windings \(w\) and \(v\), respectively, then the complete return
criterion says

\[
 F_i^{(s)}=wN,
 \qquad F_{i+t}^{(s)}=vN.
\]

Hence every same-duration two-start pair satisfies the exact congruence
lift

\[
 \boxed{
 \sum_{j=0}^{t-1}\widehat c_{i+s+j}
 -\sum_{j=0}^{t-1}c_{i+j}
 =(v-w)N.}
\tag{1.4}
\]

Equation (0.5) is the zero-winding, height-tight specialization of (1.4).
Different return durations do not telescope to a single pair of equal
boundary blocks; their two literal equations retain an unmatched interior
segment.  Thus duration mixing is a second genuine part of the
positive-winding correlation problem.

## 2. Exact zero-winding two-start theorem

The one-step map \(\phi\) preserves Dyck height.  Hence an entire
\(\tau\)-cycle lies in one height stratum, say height \(h\).

### Theorem 2.1 (zero-return equation in one height stratum)

For a height-\(h\) root \(D_i\), the following are equivalent.

1. \(D_i\) starts a zero-winding omitted-label return.
2. It returns with winding zero after exactly \(2h+1\) PBBS steps.
3. \(F_i^{(h)}=0\).

When these conditions hold,

\[
 c_i=1
\tag{2.1}
\]

and the return is first and consecutive.

#### Proof

The proved zero-winding necessity theorem says that a zero-winding return
from a height-\(h\) root has step-two duration \(h\) and initial deficit
one.  Its return equation is exactly \(F_i^{(h)}=0\).

Conversely suppose \(F_i^{(h)}=0\).  Put

\[
 M_k=a_{i+k}-\sum_{j=0}^{k-1}c_{i+j}.
\]

Equation (0.2) gives

\[
 M_{k+1}-M_k=-\widehat c_{i+k}<0.
\tag{2.2}
\]

Since \(M_h=0\), one has \(M_k>0\) for \(0\le k<h\).  Thus the
integer zero-winding equality occurs for the first time at \(h\), so it
is a genuine first return.  The height--gap theorem gives no earlier
consecutive return, and the usual terminal-prefix argument gives
\(c_i=1\).  This proves the equivalence.  \(\square\)

### Theorem 2.2 (exact two-boundary balance)

Let \(D_i\) and \(D_{i+t}\) be two zero-winding starts on the same
height-\(h\) quotient cycle.  Then (0.5) holds.  Conversely, if \(D_i\)
is a zero-winding start and (0.5) holds, then \(D_{i+t}\) is also a
zero-winding start.

#### Proof

By Theorem 2.1, the two-start assertion is

\[
 F_i^{(h)}=F_{i+t}^{(h)}=0.
\]

Equation (0.4) now proves both directions.  \(\square\)

The nearest-neighbour specialization is particularly rigid:

\[
 D_i,D_{i+1}\text{ both zero starts}
 \quad\Longrightarrow\quad
 c_i=\widehat c_{i+h}=1.
\tag{2.3}
\]

More generally, if

\[
 D_i,D_{i+1},\ldots,D_{i+L-1}
\]

are all zero starts, then

\[
 c_i=\cdots=c_{i+L-1}=1,
\qquad
 \widehat c_{i+h}=\cdots=\widehat c_{i+h+L-2}=1.
\tag{2.4}
\]

Thus a consecutive cluster is simultaneously a primal unit-deficit run
at its entrance and a dual unit-deficit run at its exit.  This is an exact
two-sided restriction, not an independence assertion.

## 3. Exact zero-winding correlation gate

Let \(L_H\) be the \(\tau\)-invariant set of roots on quotient cycles of
length greater than \(H+1\).  For \(h\le H-1\), put

\[
 Z_{H,h}
 =\{D\in L_H:\operatorname {ht}(D)=h, F_0^{(h)}(D)=0\}.
\tag{3.1}
\]

These are exactly the retained zero-winding starts whose residence is at
most \(H\).  Define the literal word-equation class

\[
\begin{aligned}
 \mathcal Q_{H,h,t}=\{D\in L_H:\;&\operatorname {ht}(D)=h,
 \ F_0^{(h)}(D)=0,\\
 &\sum_{j=0}^{t-1}d(\tau^jD)
 =\sum_{j=0}^{t-1}d(\phi\tau^{h+j}D)\}.
\end{aligned}
\tag{3.2}
\]

Theorem 2.2 gives the exact identity

\[
 \boxed{
 |Z_{H,h}\cap\tau^{-t}Z_{H,h}|
 =|\mathcal Q_{H,h,t}|.}
\tag{3.3}
\]

Therefore the zero-winding part of the desired correlation is

\[
 \boxed{
 \mathcal C_H^{00}
 =\sum_{h=1}^{H-1}\sum_{t=1}^{H+1}
   |\mathcal Q_{H,h,t}|.}
\tag{3.4}
\]

Equation (3.4) is the exact two-time enumeration problem left by the block
rotation.  In particular, one-point enumeration of \(d(D)\), even with
height retained, does not evaluate it.

## 4. Separation of positive winding

Write the retained start set as a disjoint union

\[
 E_H=Z_H\mathbin{\dot\cup}P_H,
 \qquad R_H^+=|P_H|,
\]

where \(Z_H=\bigcup_hZ_{H,h}\) and \(P_H\) consists of positive-winding
starts.  In the ordered-pair definition of \(\mathcal C_H\), pairs with
at least one endpoint in \(P_H\) are at most

\[
 2(H+1)R_H^+.
\]

Indeed, there are at most \(H+1\) choices of lag for a pair whose first
endpoint lies in \(P_H\); for the remaining pairs, fix the second endpoint
in \(P_H\) and the lag, which determines the first endpoint uniquely.
Hence

\[
 \boxed{
 \mathcal C_H
 \le
 \sum_{h=1}^{H-1}\sum_{t=1}^{H+1}
 |\mathcal Q_{H,h,t}|
 +2(H+1)R_H^+.}
\tag{4.1}
\]

There is an exact scalar bound on \(R_H^+\), but it does not close (4.1).
If a positive-winding return has step-two duration \(s\), then

\[
 \sum_{j=0}^{s-1}c_j=a_s+wN\ge N.
\tag{4.2}
\]

On the retained long cycles, one directed quotient edge lies in at most
\(H\) such deficit traces.  Summing (4.2) over every positive-winding
start gives

\[
 \boxed{
 NR_H^+
 \le H\mathscr D_m,
 \qquad
 \mathscr D_m=\sum_{D\in\mathcal D_m}d(D).}
\tag{4.3}
\]

Since the proved first-deficit moment is
\(\mathscr D_m=\Theta(\sqrt m B_m)\), equation (4.3) gives only (0.6)
in a fixed Gaussian window.  Thus winding charge alone is short by the
same factor that the two-point problem is meant to recover.

## 5. A cyclewise obstruction to bounded-fibre injection

The exact one-defect mountain rotor shows that (3.4) cannot be bounded by
a uniform cyclewise injection.

### Proposition 5.1 (an exact maximally clustered rotor)

For every \(h\ge4\), there is a \(\tau\)-cycle of length

\[
 K=2h-1
\]

on semilength-\((h+1)\) Dyck roots such that exactly \(K-1=2h-2\) roots
start zero-winding returns of step-two duration \(h\).  Set

\[
 H=h+1.
\]

This cycle is retained because \(K>H+1\), and every one of its \(K-1\)
starts belongs to \(E_H\).  Its contribution satisfies

\[
 \boxed{
 R_H^{\rm rot}=2h-2,
 \qquad
 \mathcal C_H^{\rm rot}=(h+2)(2h-3),}
\tag{5.1}
\]

so

\[
 \boxed{
 {\mathcal C_H^{\rm rot}\over R_H^{\rm rot}}
 ={(h+2)(2h-3)\over2h-2}
 \sim h.}
\tag{5.2}
\]

#### Proof

Put \(q=h-1\).  The inverse fibre over the mountain \(M_q\) with one
free leaf is the unit-vector rotor of length \(2q+1=2h-1\).  The exact
mountain-rotor theorem says that every state except its unique bad state
starts a first zero-winding return of duration \(q+1=h\).  Its residence
is \(h+1=H\).

At the bad state, the duration-\(h\) deficit sum exceeds the terminal
first-maximum position by \(2\), which is not a multiple of the ambient
circumference \(2h+3\).  The height--gap theorem excludes every shorter
return, while every longer return has residence greater than \(H\).
Hence the bad state is not in \(E_H\), and the other \(K-1\) states are
exactly the contribution of this cycle to \(R_H\).

For \(1\le t\le H+1=h+2<K\), translating the set consisting of all but
one point around the \(K\)-cycle gives an intersection of size \(K-2\).
Summing over these \(h+2\) nonzero lags proves (5.1)--(5.2).  \(\square\)

This proposition rules out each of the following possible shortcuts:

* a bound \(\mathcal C_H(C)=O(R_H(C))\) on every retained quotient cycle;
* a bounded-fibre injection which keeps a pair inside its own quotient
  cycle; or
* a pointwise bound on the number of nearby zero-winding starts.

It does **not** prove divergent clustering in the Gaussian problem.  Here
the ambient semilength is \(h+1\), whereas the selected window is of order
\(h\), not order \(\sqrt h\).  At Gaussian ambient rank, the known
terminal-rotor and buffered lifts can have either many admissible terminal
phases or a single actual outer phase, and their presently proved total
mass is subcritical.  An aggregate cross-cycle enumeration is still
necessary.

## 6. Exact implication boundary

The block rotation and short-return equations reduce a proof of
\(\mathcal C_H=O_A(R_H)\) to two genuinely separate assertions:

\[
 \sum_{h=1}^{H-1}\sum_{t=1}^{H+1}
 |\mathcal Q_{H,h,t}|=O_A(R_H),
\tag{6.1}
\]

and a bound on pairs incident with positive-winding starts that improves
the scalar estimate in (4.1)--(4.3) to \(O_A(R_H)\).

Conversely, the rotor in Proposition 5.1 proves that divergent local
clustering is compatible with every exact first-maximum and first-return
constraint.  What is not known is whether such clustered cycles carry a
critical fraction of the Gaussian-height Catalan mass.  Hence the exact
word algebra does not decide the global alternative without an additional
aggregate theorem.
