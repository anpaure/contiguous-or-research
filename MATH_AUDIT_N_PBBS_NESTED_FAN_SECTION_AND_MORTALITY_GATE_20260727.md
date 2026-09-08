# PBBS corrected fans: nested common starts, absorbing mortality, and the exact all-depth section gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let

\[
 n=2m+1,
 \qquad W=\binom{2m+1}{m},
 \qquad g=f^2:\binom{[n]}m\longrightarrow\binom{[n]}m
\]

be the canonically oriented step-two PBBS permutation.  Fix

\[
 1\le q_0<H\le m,
 \qquad N_q=\binom{2m+1}{m-q}.
\]

This note audits whether the corrected PBBS windows can replace the
ordinary cyclic packets in the synchronized annular repeat-excess
problem.  The exact conclusions are as follows.

1. **A positive local common-start theorem holds.**  The audited
   global-maximum fan witnessing a target

   \[
       S\in\binom{[n]}{m-Q},\qquad Q=q_0+D,
   \]

   is not a collection of independently chosen rankwise witnesses.  Its
   single initial PBBS state simultaneously witnesses the nested tower

   \[
      S_0\supset S_1\supset\cdots\supset S_D=S,
      \qquad |S_j|=m-q_0-j,
   \]

   and its sliding rank-\(q_0\) traces form one directed Johnson
   geodesic of length \(D\), with total intersection \(S\).  Exact
   formulas are proved in Theorem 3.1.

2. **Correctness has absorbing chronology.**  For any PBBS start, the
   lower rank excess

   \[
      \eta_q=\left|\bigcap_{t=0}^{q}g^tX\right|-(m-q)
   \]

   is nondecreasing in \(q\).  Once a selected occurrence has the wrong
   rank, it can never return to the correct-rank fan at a later depth.
   Thus every selected start has a single first-failure time.

3. **The ordinary shared-leave identity needs a PBBS correction.**  Let
   \(\mathcal X\) be \(M=N_{q_0}-L\) selected starts, all correct at
   depth \(q_0\).  Let \(b_d\) be the number which have died by depth
   \(q_0+d\).  If \(H_d\) is the number of holes at that depth and
   \(\widetilde E_d\) is repeat excess above the forced floor for the
   *actual correct mass* \(M-b_d\), then

   \[
   \boxed{
      H_d=
      \bigl(b_d+L-(N_{q_0}-N_{q_0+d})\bigr)_+
      +\widetilde E_d.}
      \tag{0.1}
   \]

   Hence

   \[
   \boxed{
      \sum_{d=0}^{H-q_0}H_d
      =\sum_{d=0}^{H-q_0}
        \bigl(b_d+L-(N_{q_0}-N_{q_0+d})\bigr)_+
       +\sum_{d=0}^{H-q_0}\widetilde E_d.}
      \tag{0.2}
   \]

   The familiar formula with \(b_d=0\) is therefore valid for a safe
   cyclic packet, but not for an arbitrary corrected PBBS subdeck.

4. **The uncut PBBS deck is already synchronized.**  On the complete
   canonical PBBS deck, the all-depth support theorem gives zero holes
   and hence zero floor-correct repeat excess at every depth
   simultaneously.  Thus PBBS's target histogram is not the obstruction
   before cutting.  The obstruction is preserving that common chronology
   while thinning, cutting, or rebundling it into literal exact factors.

5. **The full conjugate fan library has an exact integral one-sided
   solution.**  Every ordered nested flag from rank \(m-q_0\) down to
   rank \(m-H\) is the lower tower of a coordinate conjugate of one
   terminal-depth-\(H\) fan.  Composing inclusion-preserving surjections
   between consecutive rank layers therefore selects one conjugate fan
   per entrance root, covers every lower target at every depth, has no
   mortality, and has \(\widetilde E_d=0\) identically.  This is stronger
   than the telescoping fractional calibration.  It deliberately changes
   the PBBS conjugate from root to root, so it proves that the residual
   one-sided obstruction is specifically *common-factor coherence*, not
   abstract nested integral rounding.  Conversely, deleting the largest
   coordinate at every step gives another integral common-history section
   in the same catalogue with exact aggregate excess
   \(\Theta_{a,b}(W\sqrt m)\).  Hence local flag availability does not
   force a favorable choice.

6. **Complete PBBS support is not a fixed-factor common section theorem.**  At one
   deeper depth, a common section exists exactly when a bipartite graph
   of entrance roots and allowed PBBS continuations satisfies all Hall
   inequalities.  The all-depth PBBS corridor proves only the singleton
   Hall inequalities.  Across several depths the exact fractional gate
   is the configuration support inequality (5.7); integral selection is
   stronger and cannot be assembled from rankwise independent matchings.

7. **Phase symmetry cannot perform the integral selection.**  On every periodic
   PBBS target with nontrivial rotational stabilizer, no rotation-
   equivariant choice of one corrected occurrence exists.  Such targets
   occur at every fixed positive Gaussian ratio along explicit arithmetic
   subsequences.  This is an exact obstruction to “average over all
   phases and choose a canonical section.”  It is not a Catalan-scale
   lower bound, because the displayed periodic target family is sparse.

8. **The two signs are not independent.**  The upper depth-\(q\) window
   based at \(X\) is the complement of the lower depth-\((q-1)\) window
   based at \(fX\).  A two-sided common section must therefore solve one
   paired, phase-shifted configuration problem.

Consequently PBBS supplies the exact local nested towers which a positive
annular construction would need, but one fixed canonical PBBS factor does
**not** presently force

\[
       \sum_{d=0}^{H-q_0}\widetilde E_d=o(W).
\]

Nor does this note prove a counterexample to such a selection.  The
proved boundary is the mortality-plus-configuration gate (0.2), together
with the separate physical task of rebundling the selected PBBS histories
into literal exact wreath factors.

## 1. PBBS chronology and lower rank excess

On one oriented \(g\)-component write

\[
 X_t=g^tX_0,
 \qquad
 X_{t+1}=X_t-\{a_t\}+\{c_t\},
 \tag{1.1}
\]

where \(a_t\in X_t\) is the departure and \(c_t\notin X_t\) is the
arrival.  Put

\[
 L_q(X_0)=\bigcap_{t=0}^{q}X_t.
 \tag{1.2}
\]

### Lemma 1.1 (exact departure formula)

For every \(q\ge0\),

\[
 \boxed{
 L_q(X_0)
 =X_0\setminus
   \{a_t:a_t\in X_0,\ 0\le t<q\}.}
 \tag{1.3}
\]

Consequently, if

\[
 r_q(X_0)=
 \left|\{a_t:a_t\in X_0,\ 0\le t<q\}\right|,
\]

then

\[
 \boxed{\eta_q(X_0):=|L_q(X_0)|-(m-q)=q-r_q(X_0)\ge0.}
 \tag{1.4}
\]

#### Proof

An initial coordinate belongs to the complete intersection precisely
when it is never departed during the window.  A later reinsertion cannot
restore it to an intersection containing the earlier state at which it
was absent.  This proves (1.3), and cardinalities give (1.4). \(\square\)

### Theorem 1.2 (absorbing rank excess)

For every start,

\[
 \boxed{
   \eta_{q+1}(X_0)-\eta_q(X_0)\in\{0,1\}.}
 \tag{1.5}
\]

In particular, if \(L_q(X_0)\) has the wrong rank at one depth, then it
has the wrong rank at every larger depth.

#### Proof

The new departure \(a_q\) either adds one new member to the set in
(1.3), or it does not.  Thus

\[
 r_{q+1}-r_q\in\{0,1\}.
\]

Subtract this from the unit increase in \(q\) in (1.4).  This proves
(1.5). \(\square\)

If a depth-\(Q\) window is correct, then all \(Q\) departures are
distinct elements of its initial owner.  Every shorter prefix is
therefore correct.  Every shifted subwindow lying inside it is also
correct: its departures are a distinct sublist, and each is still present
when it departs.

## 2. Heredity and the entrance trace path

Fix \(q_0\) and define the sliding entrance traces

\[
 T_k=L_{q_0}(X_k)
     =\bigcap_{t=k}^{k+q_0}X_t.
 \tag{2.1}
\]

### Lemma 2.1 (setwise heredity)

For every \(D\ge0\), with no rank-correctness hypothesis,

\[
 \boxed{
 L_{q_0+D}(X_0)=\bigcap_{k=0}^{D}T_k.}
 \tag{2.2}
\]

#### Proof

The intervals of time indices

\[
 [k,k+q_0],\qquad0\le k\le D,
\]

have union \([0,q_0+D]\).  Intersecting their owner intersections gives
(2.2). \(\square\)

### Lemma 2.2 (a correct deep window gives a correct-rank trace path)

Assume \(L_{q_0+D}(X_0)\) has rank \(m-q_0-D\).  Then every \(T_k\),
\(0\le k\le D\), has rank \(m-q_0\), and

\[
 \boxed{
 T_{k+1}=T_k-\{a_{k+q_0}\}+\{c_k\}.}
 \tag{2.3}
\]

The displayed trace is a directed Johnson path of length \(D\), and its
total intersection is the deep target.  Lower correctness by itself
does not justify calling it a geodesic: the preceding transition
calculus does not exclude an inserted coordinate from equalling a
coordinate deleted at an earlier trace step.

#### Proof

Correctness at the terminal depth says that every departure in the full
window is a new element of \(X_0\).  Hence each shifted list of \(q_0\)
departures consists of distinct elements present in its shifted initial
owner, proving \(|T_k|=m-q_0\).

Relative to \(T_k\), shifting the owner window one step removes the
last departure \(a_{k+q_0}\) and admits the first arrival \(c_k\).
The former has not departed earlier and lies in \(T_k\); the latter is
absent from \(X_k\), hence from \(T_k\), and cannot depart inside the
new window because every such departure is a previously undeparted
element of \(X_0\).  This proves (2.3).  The departures and arrivals in
(2.3) are distinct on their respective sides.  Indeed, two equal
arrivals would require the coordinate to depart between its two arrivals,
whereas every departure in the full window is a new initial coordinate.
An arrival cannot equal a *later* trace departure: if it is an initial
coordinate, it has already departed before being reinserted; if it is
noninitial, it cannot be one of the departures at all.  It may, however,
equal an *earlier* trace departure.  Thus (2.3) gives a Johnson path but
lower correctness alone does not make it geodesic.  Equation (2.2) gives
its intersection. \(\square\)

For a concrete *abstract adjacent-deletion chronology* showing the gap,
take \(q_0=1\) and four distinct initial coordinates \(a,b,c,d\).  Let
the first four departures be \(a,b,c,d\), and let the first three
arrivals be \(x,y,b\), with the remaining coordinates chosen legally and
distinctly.  The depth-four lower window is correct, but the third trace
insertion \(b\) repeats the first trace deletion \(b\).  The trace is not
geodesic.  This example is not asserted to be a canonical PBBS orbit;
it proves that a PBBS-specific no-return lemma would be needed before
upgrading the generic conclusion.  No such lemma is used below.

Notice that this is a lower-trace statement.  A coordinate may be
departed and later reinserted without spoiling the lower intersection.
This is exactly the return that destroys generic geodesicity, and it
also shows why lower correctness alone does not imply two-sided
\(H\)-safety.

## 3. Exact factorization of the audited global-maximum fan

We now import only the proved global-maximum corridor construction.  Let

\[
 Q=q_0+D,
 \qquad S\in\binom{[n]}{m-Q}.
\]

The expanded unmatched-mark word of \(S\) has \(2Q+1\) marks of each
type.  Choose the audited global-maximum boundary and number the reverse
marks forward as

\[
 C_0,C_1,\ldots,C_{2Q},
\]

and the forward marks backward as

\[
 A_0,A_1,\ldots,A_{2Q}.
\]

The corresponding PBBS fan is

\[
 B_t=S\cup P_t,
 \qquad
 P_t={C_0,\ldots,C_{Q-t-1}\}
       \cup\{A_0,\ldots,A_{t-1}\},
 \tag{3.1}
\]

for \(0\le t\le Q\), with empty ranges omitted.  The corridor theorem
proves

\[
 B_0\longrightarrow B_1\longrightarrow\cdots\longrightarrow B_Q
 \tag{3.2}
\]

under \(g\), and

\[
 \bigcap_{t=0}^{Q}B_t=S.
 \tag{3.3}
\]

It also proves the collision rule

\[
 \boxed{C_j=A_h\quad\Longrightarrow\quad j+h\ge2Q}
 \tag{3.4}
\]

throughout all selected index ranges.

### Theorem 3.1 (nested prefix and sliding-trace formulas)

For \(0\le j\le D\), the target supplied by the *same initial start*
at depth \(q_0+j\) is

\[
 \boxed{
 S_j:=\bigcap_{t=0}^{q_0+j}B_t
 =S\cup\{C_0,\ldots,C_{D-j-1}\}.}
 \tag{3.5}
\]

Thus

\[
 S_0\supset S_1\supset\cdots\supset S_D=S,
 \qquad
 S_{j+1}=S_j-\{C_{D-j-1}\}.
 \tag{3.6}
\]

For \(0\le k\le D\), the sliding rank-\(q_0\) entrance trace is

\[
 \boxed{
 T_k:=\bigcap_{t=k}^{k+q_0}B_t
 =S
  \cup\{C_0,\ldots,C_{D-k-1}\}
  \cup\{A_0,\ldots,A_{k-1}\}.}
 \tag{3.7}
\]

In particular,

\[
 \boxed{
 T_{k+1}=T_k-\{C_{D-k-1}\}+\{A_k\},
 \qquad
 \bigcap_{k=0}^{D}T_k=S.}
 \tag{3.8}
\]

Every set in (3.5) and (3.7) has its displayed correct rank.
Moreover, the trace in (3.8) is a directed Johnson geodesic of length
\(D\).

#### Proof

In (3.1), the \(A\)-range grows with \(t\), while the \(C\)-range
shrinks.  Since the interval in (3.5) begins at \(t=0\), no \(A\)-mark
belongs to every \(P_t\).  The common \(C\)-range is the range at the
largest time \(q_0+j\), namely

\[
 0\le i<Q-(q_0+j)=D-j.
\]

This proves (3.5).

A physical coordinate carrying both labels \(C_i=A_h\) cannot evade
this intersection calculation by switching from its \(C\)-copy to its
\(A\)-copy.  Its \(C\)-copy is available through time \(Q-i-1\), and
its \(A\)-copy from time \(h+1\) onward.  Covering the whole prefix
without an absent state would require \(i+h\le Q-1\), contradicting
(3.4).

For (3.7), over \(k\le t\le k+q_0\), the common \(A\)-range is the
range at the smallest time \(k\), and the common \(C\)-range is the
range at the largest time \(k+q_0\).  They are exactly the two ranges
shown in (3.7).

The two added ranges in (3.7) are disjoint.  Indeed, an equality
\(C_i=A_h\) there would have

\[
 i+h\le(D-k-1)+(k-1)=D-2<Q,
\]

contradicting (3.4).  They also avoid \(S\), since all marks are zero
coordinates of \(S\).  Thus (3.7) has rank

\[
 (m-Q)+(D-k)+k=m-q_0.
\]

The same argument gives \(|S_j|=m-q_0-j\).  Comparing consecutive
formulas proves the transition in (3.8).  Its deleted coordinates are
\(C_{D-1},\ldots,C_0\), and its inserted coordinates are
\(A_0,\ldots,A_{D-1}\).  Each list is internally distinct.  A collision
between the two lists would have indices \(i,h\le D-1\), hence

\[
 i+h\le 2D-2<2(q_0+D)=2Q,
\]

contradicting (3.4).  The two lists are therefore disjoint, so (3.8) is
a Johnson geodesic.  For completeness, a physical
coordinate shared as \(C_i=A_h\) occurs through its \(C\)-copy only for
\(k\le D-i-1\), and through its \(A\)-copy only for \(k\ge h+1\).
Those two ranges could cover every \(0\le k\le D\) only if
\(i+h\le D-1<Q\), contradicting (3.4).  Every unshared mark plainly
disappears from one endpoint trace.  Hence intersecting all of (3.7)
leaves only \(S\). \(\square\)

The theorem is the strongest legitimate use of the all-depth PBBS fan
in the present lane: every terminal target has at least one genuine
nested tower, and that tower is already correlated across all shallower
depths.  It does **not** say that towers chosen for different terminal
targets have distinct entrance roots.

## 4. Exact mortality-corrected shared-leave identity

Let \(\mathcal X\) be any set of \(M\) PBBS starts.  We later specialize
to an entrance family in which every depth-\(q_0\) lower window is
correct.  Repetition of a correct depth-\(q_0\) target is allowed for the
moment.

For \(0\le d\le H-q_0\), define

\[
 b_d=
 \#\{X\in\mathcal X:\eta_{q_0+d}(X)>0\},
 \qquad
 G_d=M-b_d.
 \tag{4.1}
\]

For a correct target \(S\in\binom{[n]}{m-q_0-d}\), put

\[
 \mu_d(S)=
 \#\{X\in\mathcal X:L_{q_0+d}(X)=S,\ \eta_{q_0+d}(X)=0\}.
 \tag{4.2}
\]

Define

\[
 E_d=\sum_S(\mu_d(S)-1)_+,
 \qquad
 F_d=(G_d-N_{q_0+d})_+,
 \qquad
 \widetilde E_d=E_d-F_d.
 \tag{4.3}
\]

### Lemma 4.1 (floor nonnegativity)

\[
 \boxed{\widetilde E_d\ge0.}
 \tag{4.4}
\]

#### Proof

If \(D_d\) is the number of positive-load targets, then

\[
 E_d=G_d-D_d.
\]

Since \(D_d\le\min(G_d,N_{q_0+d})\),

\[
 E_d\ge G_d-\min(G_d,N_{q_0+d})=F_d.
\]

This proves (4.4). \(\square\)

### Theorem 4.2 (mortality-corrected hole identity)

Let \(H_d=N_{q_0+d}-D_d\) be the number of uncovered targets.  Then

\[
 \boxed{
 H_d=(N_{q_0+d}-G_d)_++\widetilde E_d.}
 \tag{4.5}
\]

If

\[
 M=N_{q_0}-L,
 \qquad
 \Delta_d=N_{q_0}-N_{q_0+d},
\]

this is exactly

\[
 \boxed{
 H_d=(b_d+L-\Delta_d)_++\widetilde E_d.}
 \tag{4.6}
\]

The mortality sequence always satisfies

\[
 0\le b_0\le b_1\le\cdots\le b_{H-q_0}.
 \tag{4.7}
\]

For a corrected entrance family, \(b_0=0\).

#### Proof

The correct occurrence mass gives

\[
 H_d=N_{q_0+d}-D_d
     =N_{q_0+d}-G_d+E_d.
\]

If \(G_d\le N_{q_0+d}\), then \(F_d=0\), giving (4.5).
If \(G_d>N_{q_0+d}\), then

\[
 E_d=F_d+\widetilde E_d
    =G_d-N_{q_0+d}+\widetilde E_d,
\]

and again (4.5) follows.  Substitution gives (4.6).
Monotonicity follows from Theorem 1.2; the final assertion follows from
entrance correctness. \(\square\)

### Corollary 4.3 (the complete PBBS deck has zero synchronized excess)

Take \(\mathcal X=\binom{[n]}m\), all \(W\) canonical PBBS starts.
For every \(0\le q\le m\), let \(b_q\) be the wrong-rank count and let
\(\mu_q\) be the correct-window histogram.  Then

\[
 \boxed{
 H_q=0,\qquad
 W-b_q\ge N_q,\qquad
 E_q=W-b_q-N_q,\qquad
 \widetilde E_q=0}
 \tag{4.7a}
\]

simultaneously at every depth.

#### Proof

The audited all-depth PBBS corridor theorem gives \(H_q=0\) for every
depth on this same canonical deck.  Hence every one of the \(N_q\)
targets has positive load, so the correct occurrence mass
\(G_q=W-b_q\) is at least \(N_q\).  The identity

\[
 E_q=G_q-N_q+H_q
\]

then gives the displayed raw repeat count, and subtracting its forced
floor \(G_q-N_q\) gives \(\widetilde E_q=0\). \(\square\)

This is the exact sense in which corrected PBBS windows *can* serve all
depths simultaneously.  It is not yet the annular packet theorem:
the complete deck contains wrong-rank starts, its PBBS components need
not be exact wreaths, and cutting/literalizing the components is precisely
the operation which can destroy the common windows.

There is a useful exact depth-difference form.  For every selected family
and every \(d\ge1\),

\[
 \boxed{
 (b_d-b_{d-1})+(E_d-E_{d-1})-(H_d-H_{d-1})
 =N_{q_0+d-1}-N_{q_0+d}.}
 \tag{4.7b}
\]

Indeed \(H_d=N_{q_0+d}-M+b_d+E_d\), and subtraction proves the
identity.  On the complete PBBS deck, \(H_d=0\), so the exact layer
decrement splits between new wrong-rank deaths and the change in raw
repeat mass:

\[
 (b_d-b_{d-1})+(E_d-E_{d-1})
 =N_{q_0+d-1}-N_{q_0+d}.
 \tag{4.7c}
\]

This is a genuine all-depth conservation law, but it has no favorable
sign on \(E_d-E_{d-1}\).  It therefore does not by itself bound the
mortality of a thinned section.

Summing (4.6) proves (0.2).  Since both sums on its right are
nonnegative, aggregate annular holes are \(o(W)\) if and only if both

\[
 \boxed{
 \sum_{d=0}^{H-q_0}(b_d+L-\Delta_d)_+=o(W),}
 \tag{4.8}
\]

and

\[
 \boxed{
 \sum_{d=0}^{H-q_0}\widetilde E_d=o(W).}
 \tag{4.9}
\]

hold for the same selected starts.  The first is the exact PBBS
first-return mortality staircase; the second is the floor-balanced
colour condition.

For reference, the odd-layer ratios are

\[
 \boxed{
 {N_{q_0+d}\over N_{q_0}}
 =\prod_{j=0}^{d-1}
   {m-q_0-j\over m+q_0+j+2}.}
 \tag{4.10}
\]

Uniformly for \(q_0,d=O(\sqrt m)\),

\[
 \log {N_{q_0+d}\over N_{q_0}}
 =-{2q_0d+d^2+d\over m}+O(m^{-1}).
 \tag{4.11}
\]

At the first deeper rank,

\[
 \boxed{
 \Delta_1
 =N_{q_0}{2q_0+2\over m+q_0+2}.}
 \tag{4.12}
\]

More generally, the layer-shrink increments are exactly

\[
 \boxed{
 \Delta_d-\Delta_{d-1}
 =N_{q_0+d-1}
   {2(q_0+d)\over m+q_0+d+1}
 \qquad(d\ge1).}
 \tag{4.13}
\]

If \(z_d=b_d-b_{d-1}\) is the number of selected starts whose first
failure occurs precisely at depth \(q_0+d\), then

\[
 b_d=\sum_{j=1}^{d}z_j.
 \tag{4.14}
\]

Thus a perfectly calibrated death-only realization would compare the
first-failure histogram \(z_d\) with the layer decrement in (4.13);
condition (4.8) is the exact weaker cumulative requirement after leave
credit and target repetitions are restored.

Thus when \(q_0=a\sqrt m+O(1)\), only

\[
 (2a+o(1)){N_{q_0}\over\sqrt m}
\]

selected starts can die immediately before exceeding the scalar layer
shrink.  PBBS support gives no such selected-fibre estimate.

## 5. The exact common-section problem

Let

\[
 \mathcal R=\binom{[n]}{m-q_0}
\]

be the entrance-root layer.  For \(T\in\mathcal R\), let

\[
 \Omega(T)=
 \{X:L_{q_0}(X)=T,\ \eta_{q_0}(X)=0\}
 \tag{5.1}
\]

be its corrected PBBS occurrence fibre.  The all-depth support theorem at
depth \(q_0\) says only that every \(\Omega(T)\) is nonempty.

For a fixed \(d\ge1\), define a bipartite graph \(G_d\) between
\(\mathcal R\) and

\[
 \mathcal S_d=\binom{[n]}{m-q_0-d}
\]

by

\[
 T\sim S
 \quad\Longleftrightarrow\quad
 \exists X\in\Omega(T):
 \eta_{q_0+d}(X)=0,
 \ L_{q_0+d}(X)=S.
 \tag{5.2}
\]

### Theorem 5.1 (one-depth common-section Hall criterion)

There is a choice of at most one PBBS occurrence from every entrance root
which covers every target of \(\mathcal S_d\) if and only if

\[
 \boxed{
 |N_{G_d}(\mathcal A)|\ge|\mathcal A|
 \qquad(\mathcal A\subseteq\mathcal S_d).}
 \tag{5.3}
\]

#### Proof

Such a choice assigns every target \(S\) to a distinct entrance root
\(T\) for which an occurrence in (5.2) exists.  This is precisely a
matching saturating \(\mathcal S_d\).  Hall's theorem gives (5.3).
After choosing the matched occurrences, choose arbitrary depth-\(q_0\)
occurrences for any unused roots if a full entrance section is desired.
\(\square\)

The global-maximum fan and Theorem 3.1 prove

\[
 N_{G_d}(\{S\})\ne\varnothing
 \qquad(S\in\mathcal S_d).
 \tag{5.4}
\]

These are only the singleton instances of (5.3).  No inequality for an
arbitrary family \(\mathcal A\) follows from complete support.

There is an exact simultaneous fractional formulation.  For
\(X\in\Omega(T)\), define its live target incidence by

\[
 a_X(d,S)=
 \mathbf1_{\{\eta_{q_0+d}(X)=0,
              L_{q_0+d}(X)=S\}}.
 \tag{5.5}
\]

A fractional common section consists of \(z_X\ge0\) satisfying

\[
 \sum_{X\in\Omega(T)}z_X=1
 \qquad(T\in\mathcal R).
 \tag{5.6}
\]

### Theorem 5.2 (all-depth configuration support criterion)

There is a fractional common section (5.6) covering every target at every
depth \(1\le d\le H-q_0\) if and only if, for every nonnegative target
weight array \(w=(w_{d,S})\),

\[
 \boxed{
 \sum_{T\in\mathcal R}
    \max_{X\in\Omega(T)}
      \sum_{d=1}^{H-q_0}\sum_{S\in\mathcal S_d}
        w_{d,S}a_X(d,S)
 \ \ge\
 \sum_{d=1}^{H-q_0}\sum_{S\in\mathcal S_d}w_{d,S}.}
 \tag{5.7}
\]

#### Proof

Let \(P\) be the product of simplices defined by (5.6), and let
\(A(P)\) be its image in the target-load space.  The desired fractional
section exists exactly when

\[
 A(P)\cap(\mathbf1+\mathbb R_{\ge0}^{\mathcal S})\ne\varnothing.
\]

If the two convex sets are disjoint, separation from the upward-closed
orthant may be taken with a nonnegative normal \(w\).  The support
function of \(A(P)\) is, by the product-simplex structure,

\[
 \max_{z\in P}\langle w,Az\rangle
 =\sum_T\max_{X\in\Omega(T)}\langle w,a_X\rangle.
\]

Thus separation is impossible exactly when (5.7) holds for every
\(w\ge0\). \(\square\)

An integral common section requires one vertex of each simplex in (5.6).
It is strictly the integral configuration selection problem; Theorem 5.2
does not assert its integrality.  In particular, proving (5.3) separately
for each \(d\) does not select the same occurrence in each root fibre.
The future tower is deterministic once that occurrence is chosen.

There is nevertheless a sharp positive fractional calibration if one is
allowed to mix *coordinate conjugates* of PBBS rather than remain inside
one canonical factor.  Let \(\Omega^{\rm sym}(T)\) contain corrected
histories from every conjugate \(\sigma g\sigma^{-1}\), rooted at \(T\).

### Theorem 5.2A (symmetrized fractional nested tower design)

Put \(J=H-q_0\) and \(N_j^\star=N_{q_0+j}\).  The symmetrized
configuration catalogue has a fractional entrance section of root load
exactly one which covers every lower target at every depth
\(0\le j\le J\) with load at least one.

More precisely, put

\[
 x_\ell=
 \begin{cases}
 N_\ell^\star-N_{\ell+1}^\star,&0\le\ell<J,\\
 N_J^\star,&\ell=J.
 \end{cases}
 \tag{5.7a}
\]

For each \(\ell\), take one global-maximum PBBS fan of terminal depth
\(q_0+\ell\), and distribute total weight \(x_\ell\) uniformly over
its full coordinate-conjugacy orbit.  Then every entrance root has total
weight

\[
 {1\over N_0^\star}\sum_{\ell=0}^{J}x_\ell=1,
 \tag{5.7b}
\]

and every depth-\(j\) lower target receives guaranteed weight

\[
 {1\over N_j^\star}\sum_{\ell=j}^{J}x_\ell=1.
 \tag{5.7c}
\]

#### Proof

Theorem 3.1 says that the chosen terminal fan of lifetime \(\ell\)
contains one corrected target at every depth \(0,\ldots,\ell\), all
from the same start.  The symmetric group is transitive on each rank
layer.  Therefore the uniform coordinate-conjugacy orbit of that fan has
uniform root marginal \(1/N_0^\star\), and uniform depth-\(j\) target
marginal \(1/N_j^\star\) for every \(j\le\ell\).

Weighting the orbit by \(x_\ell\) and summing gives (5.7b)--(5.7c) by
telescoping:

\[
 \sum_{\ell=0}^{J}x_\ell=N_0^\star,
 \qquad
 \sum_{\ell=j}^{J}x_\ell=N_j^\star.
\]

If a chosen history remains correct beyond its guaranteed terminal
depth, its conjugacy orbit contributes an additional uniform nonnegative
load there; it cannot spoil coverage. \(\square\)

The fractional statement can in fact be strengthened to an exact
integral one-sided section.  This removes a possible but spurious
``rounding gap'' from the symmetrized relaxation.

### Theorem 5.2B (integral nested section in the full conjugate fan library)

There is a choice of exactly one history

\[
 X_T\in\Omega^{\rm sym}(T)
 \qquad(T\in\mathcal R)
 \tag{5.7d}
\]

such that every chosen history is correct through depth \(H\), and, for
every \(0\le j\le J=H-q_0\),

\[
 \left\{L_{q_0+j}(X_T):T\in\mathcal R\right\}
 =\binom{[n]}{m-q_0-j}
 \tag{5.7e}
\]

as supports.  Consequently this section has

\[
 b_j=H_j=\widetilde E_j=0
 \qquad(0\le j\le J).
 \tag{5.7f}
\]

#### Proof

Write \(k_0=m-q_0\).  We first construct, for every
\(k_0-J<k\le k_0\), a surjection

\[
 \pi_k:\binom{[n]}k\longrightarrow\binom{[n]}{k-1},
 \qquad \pi_k(A)\subset A.
 \tag{5.7g}
\]

Consider the inclusion graph between ranks \(k-1\) and \(k\).  For any
family \(\mathcal A\subseteq\binom{[n]}{k-1}\), double counting its
incident inclusion edges gives

\[
 |\Gamma(\mathcal A)|
 \ge {n-k+1\over k}|\mathcal A|
 \ge |\mathcal A|,
 \tag{5.7h}
\]

because \(k\le k_0\le m\) and \(n=2m+1\).  Hall therefore gives an
injection

\[
 \iota_k:\binom{[n]}{k-1}\hookrightarrow\binom{[n]}k,
 \qquad B\subset\iota_k(B).
\]

Set \(\pi_k(\iota_k(B))=B\); on the remaining \(k\)-sets choose any
one of their \((k-1)\)-subsets.  This proves (5.7g).

For each entrance root \(T=T_0\in\binom{[n]}{k_0}\), define recursively

\[
 T_j=\pi_{k_0-j+1}(T_{j-1}),
 \qquad1\le j\le J.
 \tag{5.7i}
\]

Thus \(T_0\supset T_1\supset\cdots\supset T_J\), with one element
deleted at every step.  Since each \(\pi_k\) is onto, every composition
\(\pi_{k_0-j+1}\circ\cdots\circ\pi_{k_0}\) is onto.  Hence the set of
depth-\(j\) values in (5.7i) is the whole rank-\((k_0-j)\) layer.

It remains to realize each flag by one corrected PBBS history.  Fix one
global-maximum fan of terminal depth \(H=q_0+J\).  By Theorem 3.1 its
lower prefix tower is an ordered flag of the same rank sequence.  The
symmetric group is transitive on ordered flags

\[
 T_0\supset T_1\supset\cdots\supset T_J,
 \qquad |T_{j-1}\setminus T_j|=1:
\]

map the terminal set bijectively and then map the ordered list of deleted
coordinates bijectively.  Therefore a coordinate conjugate of the fixed
fan has prefix tower exactly (5.7i).  Choose its initial history as
\(X_T\).  This proves (5.7d)--(5.7e), and all histories live through the
terminal depth, so \(b_j=0\).

Finally the correct mass at every depth is \(N_{q_0}\), while (5.7e)
gives full support of size \(N_{q_0+j}\).  Hence

\[
 E_j=N_{q_0}-N_{q_0+j}
     =(N_{q_0}-N_{q_0+j})_+,
\]

so \(\widetilde E_j=0\), and full support gives \(H_j=0\). \(\square\)

The same catalogue also contains maximally bad synchronized sections.
Thus existence of nested corrected flags is not itself a repeat-excess
inequality.

### Proposition 5.2C (ordered-deletion section with macroscopic excess)

In the full conjugate fan catalogue, choose for every entrance root
\(T\) the flag obtained by deleting the largest remaining coordinate at
each step.  All selected histories are correct through depth \(H\), but
at depth \(j\) their support has the exact size

\[
 B_j=\binom{n-j}{k_0-j},
 \qquad k_0=m-q_0,
 \tag{5.7j}
\]

and hence

\[
 \boxed{
 H_j=\widetilde E_j
 =N_{q_0+j}-\binom{n-j}{k_0-j}.}
 \tag{5.7k}
\]

If \(q_0=a\sqrt m+O(1)\), \(H=b\sqrt m+O(1)\), with fixed
\(0<a<b\), then

\[
 \sum_{j=1}^{H-q_0}\widetilde E_j
 =\Theta_{a,b}(W\sqrt m).
 \tag{5.7l}
\]

#### Proof

After \(j\) largest-element deletions, the target consists of the
\(k_0-j\) smallest elements of its entrance root.  A set
\(S\in\binom{[n]}{k_0-j}\) occurs exactly when there are at least \(j\)
coordinates larger than \(\max S\), equivalently
\(\max S\le n-j\).  This gives (5.7j), and every such ordered flag is
realized by a conjugate terminal fan exactly as in Theorem 5.2B.

All \(N_{q_0}\) histories remain correct.  Since
\(N_{q_0}\ge N_{q_0+j}\), the support form of floor-correct excess gives

\[
 \widetilde E_j
 =N_{q_0+j}-B_j=H_j,
\]

proving (5.7k).  Moreover

\[
 {B_j\over N_{q_0+j}}
 ={\binom{n-j}{k_0-j}\over\binom n{k_0-j}}
 =\prod_{i=1}^{j}{n-k_0+i\over n-j+i}
 \le\left({1\over2}+o_{a,b}(1)\right)^j
 \tag{5.7m}
\]

uniformly for \(1\le j\le(b-a)\sqrt m+O(1)\).  Every layer size
\(N_{q_0+j}\) is \(\Theta_{a,b}(W)\) in this fixed Gaussian annulus.
Summing (5.7k), using (5.7m) for the lower bound and the trivial
\(\widetilde E_j\le N_{q_0+j}\) for the upper bound, proves (5.7l).
\(\square\)

Thus there is no one-sided fractional, scalar, or abstract integral
*existence* obstruction in the full conjugate fan library, but neither
does that library force small excess: it contains both the exact
zero-excess section of Theorem 5.2B and the
\(\Theta(W\sqrt m)\)-excess section of Proposition 5.2C.  The positive
theorem does not give a section of the fixed canonical PBBS factor: the
conjugating permutation may depend on \(T\).  It therefore does not
preserve one exact owner partition and does not solve the paired upper
configuration in Section 7.  Those are exactly the noncommuting global
constraints suppressed by symmetrization.

The exact deterministic interface for a colour-biased construction is
also available.  Order distinct entrance roots
\(T_1,\ldots,T_s\).  After choosing occurrences
\(X_i\in\Omega(T_i)\) for \(i\le t\), let \(G_{d,t}\) and
\(\mathcal B_{d,t}\) be respectively the correct occurrence mass and
the target support at depth \(d\).  For a candidate
\(X\in\Omega(T_{t+1})\), put

\[
 \ell_d(X)=\mathbf1_{\{\eta_{q_0+d}(X)=0\}},
 \tag{5.7n}
\]

\[
 C_{d,t}(X)
 =\min\{G_{d,t}+\ell_d(X),N_{q_0+d}\}
   -\min\{G_{d,t},N_{q_0+d}\},
 \tag{5.7o}
\]

and

\[
 Z_{d,t}(X)
 =\ell_d(X)\,
  \mathbf1_{\{L_{q_0+d}(X)\notin\mathcal B_{d,t}\}}.
 \tag{5.7p}
\]

Here \(C_{d,t}\in\{0,1\}\) is the increase in usable scalar capacity,
while \(Z_{d,t}\in\{0,1\}\) records a genuinely fresh target.

### Theorem 5.2D (mortality-aware synchronized fresh-score identity)

For every adaptive sequence of root-fibre choices,

\[
 \boxed{
 \widetilde E_{d,t+1}-\widetilde E_{d,t}
 =C_{d,t}(X_{t+1})-Z_{d,t}(X_{t+1}).}
 \tag{5.7q}
\]

Consequently,

\[
 \boxed{
 \sum_d\widetilde E_{d,s}
 =\sum_{t=0}^{s-1}
   \left[
   \sum_d C_{d,t}(X_{t+1})
      -\sum_d Z_{d,t}(X_{t+1})
   \right].}
 \tag{5.7r}
\]

#### Proof

At every partial stage the support form of the floor-correct excess is

\[
 \widetilde E_{d,t}
 =\min\{G_{d,t},N_{q_0+d}\}
  -|\mathcal B_{d,t}|.
\]

Choosing \(X_{t+1}\) raises the first term by exactly \(C_{d,t}\), and
raises the support cardinality by exactly \(Z_{d,t}\).  This proves
(5.7q).  Sum over depths and stages to obtain (5.7r). \(\square\)

Thus a sufficient adaptive theorem would choose the root order and one
occurrence per root so that the cumulative synchronized deficit on the
right of (5.7r) is \(o(W)\).  Requiring each step to have
\(\sum_d Z_{d,t}\ge\sum_d C_{d,t}\) would even keep the aggregate excess
identically zero.  No such evolving-fibre freshness theorem is presently
proved for canonical PBBS.  Formula (5.7r), rather than separate
rankwise choices, is the exact process to attack.

There is also an exact audit of the most natural common randomized
section.  Put

\[
 m_T=|\Omega(T)|,
 \qquad
 r_{T,S}^{(d)}
 =|\{X\in\Omega(T):a_X(d,S)=1\}|,
 \qquad
 p_{T,S}^{(d)}={r_{T,S}^{(d)}\over m_T}.
 \tag{5.8}
\]

Choose one occurrence uniformly and independently inside every root
fibre \(\Omega(T)\), but use that same chosen occurrence at every depth.

### Proposition 5.3 (exact common random-section formula)

At depth \(d\),

\[
 \boxed{
 \mathbb E H_d
 =\sum_{S\in\mathcal S_d}
    \prod_{T\in\mathcal R}(1-p_{T,S}^{(d)}).}
 \tag{5.9}
\]

If

\[
 \Lambda_d(S)=\sum_Tp_{T,S}^{(d)},
 \tag{5.10}
\]

then

\[
 \boxed{
 \sum_{S\in\mathcal S_d}\Lambda_d(S)\le N_{q_0}.}
 \tag{5.11}
\]

Consequently, fix \(\varepsilon<1\).  If, at a depth for which
\(N_{q_0}/N_{q_0+d}=O(1)\), all but \(o(N_{q_0+d})\) targets satisfy

\[
 \max_Tp_{T,S}^{(d)}\le\varepsilon,
 \tag{5.12}
\]

then this unbiased common section has

\[
 \boxed{\mathbb E H_d=\Omega(N_{q_0+d})=\Omega(W)}
 \tag{5.13}
\]

in a fixed Gaussian annulus.

#### Proof

A target \(S\) is missed exactly when every root fibre chooses outside
its \(r_{T,S}^{(d)}\) eligible occurrences.  Independence across root
fibres gives (5.9).

For one root \(T\), at most \(m_T\) of its occurrences remain live at
depth \(d\), and each live occurrence contributes to exactly one target.
Therefore

\[
 \sum_Sp_{T,S}^{(d)}\le1.
\]

Summing over the \(N_{q_0}\) roots proves (5.11).

Markov's inequality applied to (5.11) shows that at least half of the
targets obey

\[
 \Lambda_d(S)\le {2N_{q_0}\over N_{q_0+d}}.
\]

After removing the \(o(N_{q_0+d})\) exceptions in (5.12), a positive
fraction obey both estimates.  For them,

\[
 \begin{aligned}
 \prod_T(1-p_{T,S}^{(d)})
 &\ge
 \exp\left(-{1\over1-\varepsilon}
              \sum_Tp_{T,S}^{(d)}\right)\\
 &\ge
 \exp\left(
   -{2N_{q_0}\over(1-\varepsilon)N_{q_0+d}}\right),
 \end{aligned}
\]

where \(\log(1-x)\ge-x/(1-x)\) was used.  The last expression is a
positive constant in a fixed Gaussian annulus.  Summing in (5.9) proves
(5.13). \(\square\)

Thus one common independent choice across depths is already the wrong
mechanism whenever the root exposures are diffuse.  A positive PBBS
section must exploit many nearly forced root-to-tower choices, or a
globally correlated matching/rounding.  Proposition 5.3 is a method
obstruction only; it does not rule out the correlated integral selection
in Theorem 5.1 or its all-depth analogue.

The need for group Hall information cannot be removed by the nested-set
identity alone.  Abstractly, for a fixed set \(S\) and distinct elements
\(x_1,\ldots,x_t\notin S\), the legal one-step flags

\[
 S\cup\{x_i\}\supset S
 \qquad(1\le i\le t)
\]

have distinct entrance roots and all collide on one deeper target.  This
is a genuine Johnson-geodesic configuration.  It is not asserted to be a
positive-density PBBS subdeck; it proves that heredity and root
injectivity alone imply no repeat-excess inequality.

## 6. A rotational obstruction to canonical fan sections

Let \(\rho\) be the cyclic coordinate rotation.  PBBS is rotation
equivariant:

\[
 g(\rho X)=\rho g(X).
 \tag{6.1}
\]

The rotation action on middle sets is free, because a stabilizer order
would divide both \(m\) and \(2m+1\).

### Theorem 6.1 (no rotation-equivariant corrected section)

Suppose a rank-\((m-q_0)\) target \(T\) has a nontrivial rotational
stabilizer.  There is no rotation-equivariant map

\[
 \sigma:\binom{[n]}{m-q_0}\longrightarrow\binom{[n]}m
 \tag{6.2}
\]

such that

\[
 \sigma(T)\in\Omega(T)
\]

for every target.

#### Proof

Let \(h\ne1\) be a rotation fixing \(T\).  Equivariance would give

\[
 \sigma(T)=\sigma(hT)=h\sigma(T).
\]

This fixes the selected middle start under a nonidentity rotation,
contradicting freeness. \(\square\)

The obstruction occurs in a fixed Gaussian window.  Let \(d,L\ge3\)
be odd,

\[
 n=dL,
 \qquad m={dL-1\over2},
 \qquad q_0={d-1\over2},
\]

and define

\[
 T_{d,L}
 =\{aL+b:0\le a<d,\ 0\le b<(L-1)/2\}.
 \tag{6.3}
\]

Then \(|T_{d,L}|=m-q_0\), and its stabilizer has order exactly \(d\).
Indeed \(\rho^L\) preserves the residue \(b\bmod L\) and has order
\(d\).  Conversely, a rotation fixing \(T_{d,L}\), reduced modulo
\(L\), fixes the proper cyclic interval
\(\{0,\ldots,(L-3)/2\}\).  If the reduced rotation has order \(e\),
that interval is a union of \(e\)-orbits, so \(e\) divides both \(L\)
and \((L-1)/2\); hence \(e=1\).  The original rotation is therefore a
multiple of \(L\).
If \(L/d\to c\in(0,\infty)\), then

\[
 {q_0\over\sqrt m}\longrightarrow{1\over\sqrt{2c}}.
 \tag{6.4}
\]

Thus the obstruction occurs at every prescribed positive Gaussian ratio
along a suitable odd arithmetic subsequence.  It forbids an invariant
integral leaf of the rotation-averaged fan catalogue.  It does not forbid
a symmetry-breaking section, and the periodic targets in (6.3) are too
sparse to yield an \(\Omega(W)\) lower bound by themselves.

## 7. Complement and the two-sided gate

Return to the original PBBS order \(A_i=f^i(A_0)\).  The exact PBBS
identity is

\[
 A_{i+1}=[n]\setminus(A_i\cup A_{i+2}).
 \tag{7.1}
\]

Intersecting (7.1) over the even step-two window gives, for \(q\ge1\),

\[
 \boxed{
 [n]\setminus\bigcup_{h=0}^{q}A_{i+2h}
 =\bigcap_{h=0}^{q-1}A_{i+1+2h}.}
 \tag{7.2}
\]

Equivalently, if \(U_q(X)\) is the upper window based at \(X\), then

\[
 \boxed{
 U_q(X)=[n]\setminus L_{q-1}(fX).}
 \tag{7.3}
\]

Thus the upper tower of a selected start is fixed by the lower tower on
the opposite PBBS phase, with a one-depth shift.  A two-sided version of
(5.7) must put both incidences

\[
 L_{q_0+d}(X),
 \qquad
 [n]\setminus L_{q_0+d-1}(fX)
 \tag{7.4}
\]

in the same configuration column.  Separate lower and upper nibbles do
not produce one physical PBBS history.

This phase shift is also why the lower common-start theorem in Section 3
must not be advertised as an automatically two-sided safe packet.  The
opposite-sign fan is real and has complete support, but it belongs to the
paired phase chronology in (7.3).

## 8. Audited implication boundary

The following statements are proved.

1. Every corrected deep PBBS fan supplied by the global-maximum theorem
   is one explicit nested prefix tower, with formulas (3.5)--(3.6).
2. Its sliding entrance traces are the explicit geodesic
   (3.7)--(3.8); this is the precise PBBS realization of hereditary
   path colours.
3. Wrong-rank lower windows are absorbing in depth.
4. For any selected PBBS entrance family, (4.6) and (0.2) are the exact
   hole and aggregate-hole identities.
5. The exact one-depth selection condition is Hall (5.3), and the exact
   all-depth fractional condition is (5.7).
6. In the full coordinate-conjugate fan catalogue, Theorem 5.2B gives
   an exact integral one-sided section with \(b_j=H_j=\widetilde E_j=0\)
   at every controlled depth, while Proposition 5.2C gives another
   all-depth-correct section with aggregate excess
   \(\Theta_{a,b}(W\sqrt m)\).
7. Rotation-equivariant corrected sections are impossible on periodic
   target fibres.
8. Upper and lower towers are coupled by the exact phase-shifted
   complement identity (7.3).

The following statements are not proved.

1. A critical-size entrance section inside one fixed canonical PBBS
   factor satisfying all Hall inequalities (5.3), let alone the integral
   all-depth version of (5.7).
2. The mortality envelope (4.8) for one selected section.
3. The synchronized repeat estimate (4.9).
4. A critical-size PBBS section violating either condition by
   \(\Omega(W)\).
5. A rebundling of the selected PBBS histories into one exact cyclic
   wreath factor with \(o(W)\) literal seam cost.

Hence the corrected PBBS windows answer the *local chronology* question
positively: one deep witness is already a genuine all-shallower nested
witness.  The symmetrized catalogue also answers the abstract one-sided
integral flag problem exactly.  What remains unanswered is the
*simultaneous integral section inside one fixed factor*, and then its
paired upper chronology.  That is precisely a mortality-aware,
two-phase configuration selection, not a collection of rankwise
independent support statements.

## 9. Independent adversarial audit

An independent audit found and repaired one substantive overclaim in the
first draft: generic lower correctness gives the correct-rank Johnson
path of Lemma 2.2, but does not by itself exclude a return to an earlier
trace-departure coordinate.  The special global-maximum fan remains a
geodesic because its exact source collision law is

\[
 C_i=A_h\Longrightarrow i+h\ge2Q,
\]

whereas all deletion/insertion indices used in (3.8) satisfy
\(i+h\le2D-2<2Q\).

After that correction, the audit verified Theorems 4.2, 4.3, 5.2,
5.2A, 5.2D, the rotation obstruction, and the complement identity.
A second adversarial pass verified the additions in Theorem 5.2B and
Proposition 5.2C: the Hall ratio is exactly \((n-k+1)/k\), coordinate
conjugacy is transitive on the required ordered flags, the zero-excess
floor calculation is exact, and the largest-first support ratio is

\[
 {\binom{n-j}{k_0-j}\over\binom n{k_0-j}}
 =\prod_{i=1}^{j}{n-k_0+i\over n-j+i}
 \le\left({1\over2}+O_{a,b}(m^{-1/2})\right)^j.
\]

No further constant, quantifier, or implication-scope defect was found.
