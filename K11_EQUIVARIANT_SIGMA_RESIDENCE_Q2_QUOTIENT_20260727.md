# The exact \(k=11\) quotient predicates after the sigma reduction

Date: 2026-07-27

## 0. Outcome

Let translation by one on \(\mathbb Z_{11}\) be denoted by \(\tau\).  Start
with a translation-equivariant sigma map

\[
 \sigma:\binom{\mathbb Z_{11}}5\longrightarrow
              \binom{\mathbb Z_{11}}7,
 \qquad X\subset\sigma(X),
\]

whose selected middle-level graph is a single quotient cycle of nonzero
voltage.  The quotient has \(42\) lower edges and \(42\) middle vertices.

There are exact finite quotient tests for both remaining central predicates.

* Delay-three residence is \(126=42\cdot3\) local inequalities.
* Rank-eight \(q=2\) coverage is surjectivity of \(42\) derived local colours
  onto the \(15\) translation orbits of eight-sets.

There is also a useful rigidity specific to equivariance.  A single linear
cut cannot hide even one quotient residence defect: every defect has eleven
translated, pairwise disjoint copies.  Hence a factorable cut exists only if
the **whole lifted cycle** already has cyclic delay-three residence.  Once
this holds, a nested \(5\supset4\supset3\) endpoint flag always exists; in
fact there are exactly nine flags compatible with any fixed cut.

The cut must still preserve rank-seven and rank-eight coverage.  Those two
redundancy conditions are explicit below, but no counting argument forces a
common safe cut.

## 1. Voltage coordinates on the quotient cycle

Orient the quotient cycle and index its middle vertices and lower edges by
\(j\in\mathbb Z_{42}\).  Choose representatives

\[
 V_j\in\binom{\mathbb Z_{11}}6
\]

and voltages \(\omega_j\in\mathbb Z_{11}\) so that edge \(j\) joins
\(V_j\) to \(\tau^{\omega_j}V_{j+1}\).  Put

\[
\begin{aligned}
 C_j&=V_j\cap\tau^{\omega_j}V_{j+1},\\
 A_j&=\sigma(C_j)=V_j\cup\tau^{\omega_j}V_{j+1},\\
 \{\delta_j\}&=V_j\setminus\tau^{\omega_j}V_{j+1},\\
 \{\alpha_j\}&=\tau^{\omega_j}V_{j+1}\setminus V_j.
\end{aligned}
\tag{1.1}
\]

Thus \(\delta_j\) is deleted and \(\alpha_j\) is inserted when edge \(j\)
is traversed in phase zero.  Define

\[
 s_0=0,\qquad s_j=\sum_{u=0}^{j-1}\omega_u,
 \qquad \Omega=s_{42},
\tag{1.2}
\]

and extend by \(s_{j+42}=s_j+\Omega\), while \(V,\alpha,\delta,\omega\)
are extended \(42\)-periodically.  The nonzero-voltage hypothesis is

\[
 \Omega\ne0\pmod {11}.
\tag{1.3}
\]

The lifted middle Hamilton cycle is

\[
 Y_{42t+j}=\tau^{\,t\Omega+s_j}V_j
 \qquad(0\le t<11,\ 0\le j<42).
\tag{1.4}
\]

Its transition at \(42t+j\) deletes
\(\tau^{t\Omega+s_j}\delta_j\) and inserts
\(\tau^{t\Omega+s_j}\alpha_j\).  Equations (1.1)--(1.4) remove all phase
ambiguity from the remaining predicates.

## 2. Exact delay-three residence

### Theorem 2.1

The lifted cycle has cyclic coordinate residence at least four if and only
if

\[
 \boxed{
 \alpha_j+s_j\ne\delta_{j+h}+s_{j+h}
 \quad(j\in\mathbb Z_{42},\ h=1,2,3),}
\tag{2.1}
\]

where the elements of \(\mathbb Z_{11}\) are written additively.
Equivalently,

\[
 \alpha_j\ne
 \delta_{j+h}+\sum_{u=j}^{j+h-1}\omega_u.
\tag{2.2}
\]

Hence residence contributes exactly \(126\) local forbidden-equality tests
after the quotient cycle has been oriented.

#### Proof

At a lifted occurrence of edge \(j\), the inserted coordinate is
\(\alpha_j+s_j+t\Omega\).  At the occurrence \(h\) transitions later, the
deleted coordinate is \(\delta_{j+h}+s_{j+h}+t\Omega\).  Equality says that
the new one-run has length \(h\le3\).  Cancelling the common phase gives
(2.1).  These are all possible cyclic runs of length at most three. \(\square\)

### Theorem 2.2 (one cut cannot repair an equivariant defect)

If a linear ordering obtained by cutting the lifted Hamilton cycle is a
three-fold OR derivative, then (2.1) holds everywhere on the cyclic lift.

#### Proof

Because \(\Omega\ne0\), choose \(u\in\mathbb Z_{11}^{\times}\) with
\(u\Omega=1\).  From (1.4), translation \(\tau\) acts on the Hamilton cycle
as rotation by \(42u\) positions.  Therefore any cyclic one-run of length at
most three has eleven translated copies.  As a set of positions, their
starts differ by the multiples of \(42\), so their transition intervals,
each of length at most four, are pairwise disjoint.

A cut can turn at most one such cyclic run into an initial or terminal run.
The other ten remain internal runs of length at most three, contradicting
the exact residence criterion for a three-fold OR preimage.  Thus no short
cyclic run exists. \(\square\)

Conversely, if (2.1) holds, every cut has all internal one-runs of length at
least four.  Thus the usual freedom to choose a clever cut disappears in the
equivariant model: residence must be built into the quotient cycle itself.

## 3. The boundary flag is then automatic

Cut the lifted occurrence of quotient edge \(c\), so the path starts at the
head of this edge and ends at its tail.  The missing lower colour is the
translated copy of \(C_c\).  Ignore a common translation and write it simply
as \(C_c\).

Let \(\widehat\alpha_i=\alpha_i+s_i\) denote the aligned inserted letters at
the chosen lift.  Under (2.1), the three letters

\[
 \widehat\alpha_{c-3},\quad
 \widehat\alpha_{c-2},\quad
 \widehat\alpha_{c-1}
\tag{3.1}
\]

are distinct and all belong to \(C_c\): none may be deleted in the one,
two, or three following transitions, including the cut edge.

For a prescribed right boundary flag

\[
 F_1=C_c\supset F_2\supset F_3,
 \qquad |F_i|=6-i,
\tag{3.2}
\]

the endpoint-flag theorem reduces exactly to

\[
 \boxed{
 \widehat\alpha_{c-1}\in F_3,
 \qquad
 \{\widehat\alpha_{c-2},\widehat\alpha_{c-1}\}\subset F_2.}
\tag{3.3}
\]

The \(F_1\) condition is already supplied by (3.1).  Indeed, the terminal
coordinates of residence at most \(t\le3\) are precisely the last \(t\)
inserted letters.  The coordinate deleted at the cut has terminal residence
at least four by (2.1), so it is not forced into \(F_1=C_c\).

Consequently a compatible flag always exists.  More precisely, \(F_2\) is
one of the three four-subsets of \(C_c\) containing the last two letters,
and, for each \(F_2\), \(F_3\) is one of its three three-subsets containing
the last letter.  Thus

\[
 \boxed{\text{every fixed cut has exactly }3\cdot3=9
 \text{ residence-compatible }5\supset4\supset3\text{ flags}.}
\tag{3.4}
\]

This is only the endpoint-factorability statement.  Choosing among the nine
flags so that all other lower masks retain witnesses is the separate lower
compiler problem.

## 4. Exact quotient colours at \(q=2\)

Align two consecutive upper colours through their common middle set and put

\[
 B_j=A_j\cup\tau^{\omega_j}A_{j+1}
     =V_j\cup\tau^{\omega_j}V_{j+1}
          \cup\tau^{\omega_j+\omega_{j+1}}V_{j+2}.
\tag{4.1}
\]

This is exactly the union of three consecutive lifted middle sets, before a
common translation.  It has size seven or eight.  The following equivalent
tests are often useful:

\[
\begin{aligned}
 |B_j|=8
 &\iff A_j\ne\tau^{\omega_j}A_{j+1}\\
 &\iff \delta_j\ne\alpha_{j+1}+\omega_j.
\end{aligned}
\tag{4.2}
\]

Thus a degenerate \(q=2\) window is exactly an immediate reinsertion of the
coordinate just deleted.  This is a zero-gap condition; it is **not**
forbidden by the positive-residence inequalities (2.1).

There are

\[
 \frac1{11}\binom{11}{8}=15
\tag{4.3}
\]

translation orbits of rank-eight targets.  For such an orbit \(\mathcal O\),
define

\[
 \ell_2(\mathcal O)
 =\#\{j\in\mathbb Z_{42}:|B_j|=8,\ [B_j]=\mathcal O\}.
\tag{4.4}
\]

### Theorem 4.1

The cyclic lift covers every rank-eight set if and only if

\[
 \boxed{\ell_2(\mathcal O)\ge1
 \quad\text{for all }15\text{ rank-eight orbits }\mathcal O.}
\tag{4.5}
\]

#### Proof

During the eleven passages through quotient position \(j\), (4.1) appears
as

\[
 \tau^{t\Omega+s_j}B_j\qquad(0\le t<11).
\]

Since \(\Omega\ne0\), these are the eleven distinct members of the orbit of
\(B_j\).  Hence every member of an orbit \(\mathcal O\) occurs exactly
\(\ell_2(\mathcal O)\) times in the cyclic lift. \(\square\)

If \(g=\#\{j:|B_j|=7\}\), then

\[
 \sum_{\mathcal O}\ell_2(\mathcal O)=42-g.
\tag{4.6}
\]

Thus coverage only forces \(g\le27\), and its quotient excess is \(27-g\).
There are \(15\) coverage inequalities, not \(165\); equivalently, one may
colour every nondegenerate position by the three-set complement of \(B_j\).

## 5. Exact safe-cut predicate for the upper side

Let

\[
 \ell_1(\mathcal P)=\#\{j:[A_j]=\mathcal P\}
\tag{5.1}
\]

for the \(30=\binom{11}{7}/11\) rank-seven orbits.  Cutting edge \(c\)
removes its immediate upper occurrence and the two cyclic \(q=2\) windows
starting at \(c-1\) and \(c\).  Therefore immediate upper coverage survives
if and only if

\[
 \boxed{\ell_1([A_c])\ge2.}
\tag{5.2}
\]

This is exactly the loss in the optimal-length OR word: after a safe cut,
the maximal three-fold factor has \(W-2=460\) cells in row \(D^5\), and
they are precisely the cyclic triple windows other than those starting at
\(c-1\) and \(c\).

To state the \(q=2\) condition, align the two removed actual sets as

\[
 \widehat B_{c-1}=\tau^{s_{c-1}}B_{c-1},
 \qquad
 \widehat B_c=\tau^{s_c}B_c.
\tag{5.3}
\]

Ignore either one when it has size seven.  Rank-eight coverage survives the
cut if and only if, for every rank-eight set \(R\),

\[
 \boxed{
 \ell_2([R])>
 \mathbf1_{R=\widehat B_{c-1}}+
 \mathbf1_{R=\widehat B_c}.}
\tag{5.4}
\]

Equivalently:

* neither removed rank-eight window may belong to a quotient colour of load
  one; and
* if the two removed windows are the same actual eight-set, its quotient
  load must be at least three.

The predicate depends only on the \(42\) quotient cut types: changing the
lifted occurrence translates both removed sets together.  Combining
(2.1), (3.3), (5.2), and (5.4) is the exact central safe-cut test.

## 6. Constraint ledger and the remaining nonimplication

The complete equivariant \(k=11\) central quotient now has the following
finite ledger.

| predicate | quotient data / number |
|---|---:|
| sigma choices | \(42\) variables, \(15\) values each |
| middle degree two | \(42\) equations |
| rank-seven coverage | \(30\) inequalities |
| connected lift | one quotient cycle and \(\Omega\ne0\) |
| delay-three residence | \(126\) local inequalities |
| rank-eight \(q=2\) coverage | \(15\) inequalities from \(42\) local colours |
| cut types | \(42\) up to translation |
| boundary flags per residence-safe cut | \(9\) |

Some redundancy is guaranteed at \(q=1\): positive loads on \(30\) orbits
sum to \(42\), so at least one orbit is repeated.  This does **not** force a
cut satisfying both upper safety predicates.  In the weakest load ledger,
only \(13\) of the \(42\) edge positions are forced to carry repeated
rank-seven colours.  A singleton rank-eight quotient colour forbids the two
cuts adjacent to its unique position; up to \(15\) singleton colours can
therefore forbid as many as \(30\) cut positions (before the double-removal
condition in (5.4)).  Even under the cap-two q1 profile, only \(24\) edge
positions are q1-safe, so pigeonhole still gives no common safe cut.

The sharp simplifications are therefore:

1. residence is a fixed \(126\)-test quotient predicate, not a cut-selection
   problem;
2. the endpoint flag has no additional existence obstruction once residence
   holds; and
3. \(q=2\) is a \(15\)-colour adjacent-edge surjectivity problem, but its safe
   cut must still be coupled to the repeated q1 colour.

These predicates are necessary and sufficient for the central
residence-plus-rank-eight interface.  They do not yet solve the lower
compiler/pin-survival problem.
