# The ST two-point statistic under exact PBBS peak deletion

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

This note combines the exact predecessor transmission in
`MATH_THEOREM_PBBS_TWO_POINT_PREDECESSOR_TRANSMISSION_20260726.md` with
the chronological cell/coarea identities in
`MATH_ATTACK_LOW_POSITIVE_WINDING_TRANSPORTED_SECTOR_MATCHING_20260726.md`.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil .
\]

Let \(E_H\) and

\[
 R_H=|E_H|,
 \qquad
 \mathcal C_H=\sum_{t=1}^{H+1}|E_H\cap\tau^{-t}E_H|
\]

be the genuine long-cycle return-start set and its two-point statistic from
`PBBS_ST_TWO_POINT_CLUSTERING_DICHOTOMY_20260726.md`.

This note does not decide \((ST_A)\): neither
\(\mathcal C_H=O_A(R_H)\) nor
\(\mathcal C_H/R_H\to\infty\) is proved at the critical density
\(R_H\asymp B_r/H\).  It makes three exact advances.

1. There is a sharp universal lower bound

   \[
    \boxed{
    \mathcal C_H
      \ge {1\over2}\left({(H+2)R_H^2\over B_r}-R_H\right).}
   \]

   Consequently

   \[
    {H R_H\over B_r}\longrightarrow\infty
    \quad\Longrightarrow\quad
    {\mathcal C_H\over R_H}\longrightarrow\infty.
   \]

   This is a genuine divergent lower bound, but it is silent at the
   critical one-point scale \(R_H=\Theta(B_r/H)\).

2. In the main Pascal saddle, the outer two-point ratio is equivalent up
   to absolute constants to one exact lower-rank statistic.  Let
   \(\mathcal A_{d,k,H}\) be the rank-\(d\), peak-\(k\) cores for which
   the decorated root--predecessor passage makes every terminal-slot-zero
   parent lift eligible by horizon \(H\).  With the exact inverse-fibre
   weight

   \[
    F_r(d,k)=\binom{r+d-k}{2d},
   \]

   put

   \[
    \mathscr R_H
      =\sum_{d,k}F_r(d,k)|\mathcal A_{d,k,H}|,
   \]

   \[
    \mathscr C_H
      =\sum_{d,k}F_r(d,k)
       \sum_{t=1}^{H+1}
       |\mathcal A_{d,k,H}\cap
          \tau_d^{-t}\mathcal A_{d,k,H}|.
   \]

   Along every critical subsequence on which the return mass is
   concentrated in the audited saddle tube, the saddle and short-cycle
   deletions give

   \[
    \boxed{
      \left({1\over2}-o(1)\right){\mathscr C_H\over\mathscr R_H}
      \le {\mathcal C_H\over R_H}
      \le
      \left({4\over3}+o(1)\right)
      {\mathscr C_H\over\mathscr R_H}.}
   \]

   Thus bounded clustering and divergent clustering are each preserved by
   the first exact peak-deletion lift.  The Pascal fibre neither creates
   nor removes the missing divergence.

3. A large-lag linear transported cell is a one-start condition.  Its
   internal endpoints \((D_j,\phi D_k)\) are not two members of \(E_H\)
   merely because the cell is nonempty.  The exact statistic it must
   control is instead

   \[
    {\mathscr C_H\over\mathscr R_H}
     ={\sum_{d,k}F_r(d,k)
       \sum_{E\in\mathcal A_{d,k,H}}
       \sum_{t=1}^{H+1}
       \mathbf1_{\mathcal A_{d,k,H}}(\tau_d^tE)
       \over
       \sum_{d,k}F_r(d,k)|\mathcal A_{d,k,H}|}.
   \]

   Proving that the cell forces a diverging number of these *decorated
   passage* neighbours would prove the clustering side of \((ST_A)\).
   Proving that their weighted average is bounded, together with a
   critical lower bound for \(R_H\), would refute \((ST_A)\).  The carrier
   overlap alone proves neither assertion.

This is a two-point reduction using simultaneous canonical PBBS block
rotations throughout.  No independent fibre transport, random matching,
or formal cocycle is substituted for \(\tau\).

## 1. A sharp autocorrelation lower bound

The first theorem is valid for every permutation; it is included because
it gives the strongest unconditional divergent alternative presently
available for the PBBS statistic.

### Theorem 1.1 (Fejér-window lower bound)

Let \(\tau\) be any permutation of a set of size \(B\), let
\(E\) have size \(R\), and put

\[
 C_h(E)=\sum_{t=1}^h|E\cap\tau^{-t}E|.
\]

Then

\[
 \boxed{
 C_h(E)\ge {1\over2}\left({(h+1)R^2\over B}-R\right).}
 \tag{1.1}
\]

#### Proof

Write \(x(v)=\mathbf1_E(v)\) and

\[
 y(v)=\sum_{a=0}^h x(\tau^av).
\]

Then

\[
 \sum_vy(v)=(h+1)R.
\]

Cauchy--Schwarz gives

\[
 \sum_vy(v)^2\ge{(h+1)^2R^2\over B}.
 \tag{1.2}
\]

On the other hand, expansion by the displacement \(t=|a-b|\) gives

\[
 \sum_vy(v)^2
 =(h+1)R+2\sum_{t=1}^h(h+1-t)|E\cap\tau^{-t}E|.
 \tag{1.3}
\]

Since \(h+1-t\le h+1\), the right side of (1.3) is at most

\[
 (h+1)(R+2C_h(E)).
\]

Combine this with (1.2) and divide by \(h+1\). \(\square\)

Apply Theorem 1.1 with \(B=B_r\) and \(h=H+1\).  It gives

\[
 \boxed{
 {\mathcal C_H\over R_H}
 \ge {1\over2}\left({(H+2)R_H\over B_r}-1\right).}
 \tag{1.4}
\]

Thus supercritical one-point mass forces divergent clustering.  At
\(R_H=cB_r/H\), (1.4) gives only a constant lower bound.  This limitation
is sharp for set geometry: on a long cycle, starts spaced by \(H+2\) have
size \(\Theta(B/H)\) and zero correlation through lag \(H+1\).  Such a
set is not asserted to be a PBBS return-start set.

## 2. Peak deletion and the decorated passage set

Let

\[
 \partial:\mathcal D_r\longrightarrow\bigcup_{d<r}\mathcal D_d
\]

be simultaneous peak deletion.  The exact semiconjugacy is

\[
 \boxed{\partial\tau_r=\tau_d\partial}
 \tag{2.1}
\]

on a fibre over rank \(d\).

Fix \(E\in\mathcal D_d\), put

\[
 k=\operatorname {pk}(E),
 \qquad M=r+d-k,
\]

and assume \(d+k\le r\), which is exactly the condition that rank-
\(r\) inverse lifts exist.

Let

\[
 \mathcal F_E=\partial^{-1}(E).
\]

The exact Pascal-slot parametrization gives

\[
 \boxed{|\mathcal F_E|=F_r(d,k)=\binom M{2d}.}
 \tag{2.2}
\]

The peak count is constant on a \(\tau_d\)-cycle.  One way to see this
is to view \(\phi\) as a cyclic rotation of the complemented rooted word.
The number of cyclic \(10\)-transitions is invariant under rotation and
complementation, and for a Dyck word it equals its number of peaks.
Consequently (2.2) is constant along every reduced quotient cycle, as is
also forced by the fibre bijections in (2.1).

Let \(\mathcal Z_E\subseteq\mathcal F_E\) be the terminal-slot-zero
hyperplane.  Its exact size is

\[
 \boxed{
 K_0(d,k)=|\mathcal Z_E|
 =\binom{M-1}{2d-1},
 \qquad
 {K_0(d,k)\over F_r(d,k)}={2d\over M}.}
 \tag{2.3}
\]

Put \(G=2H-1\).  If \(\kappa_u(E)\) is the selected-particle itinerary
of the reduced equality particle, normalized by \(\kappa_0(E)=0\), put

\[
 V_G(E)=\#\{1\le u\le G:\kappa_u(E)=-1\}.
 \tag{2.4}
\]

The equality-particle return theorem says that a parent lift with terminal
slot \(z\) is eligible by the prescribed horizon exactly when the
\((2z+2)\)-nd occurrence of the immediate predecessor occurs by time
\(G\), equivalently when \(V_G(E)\ge2z+2\).  In particular:

* if any lift over \(E\) is eligible, then the slot-zero lift is eligible;
* either every member of \(\mathcal Z_E\) is eligible or none is; and
* the decision depends only on the actual canonical \(\tau_d\)-itinerary
  of \(E\).

Define

\[
 \boxed{
 \mathcal A_{d,k,H}
 =\{E\in\mathcal D_d:\operatorname {pk}(E)=k,
       \ V_G(E)\ge2\}.}
 \tag{2.5}
\]

This is the exact decorated predecessor-passage set.  It is not the set of
all lower-rank short-return roots: the final adjacent-particle passage is
retained.

## 3. One-point fibre comparison

For the moment retain all parent quotient cycles, and put tildes on their
return statistics.  Let \(\widetilde R_H(d,k)\) be the number of eligible
parent roots whose first-pruned core lies in the \((d,k)\) cell.

### Lemma 3.1 (one-point sandwich)

For every \((d,k)\),

\[
 \boxed{
 K_0(d,k)|\mathcal A_{d,k,H}|
 \le\widetilde R_H(d,k)
 \le F_r(d,k)|\mathcal A_{d,k,H}|.}
 \tag{3.1}
\]

#### Proof

If \(E\in\mathcal A_{d,k,H}\), all \(K_0(d,k)\) slot-zero lifts are
eligible, proving the lower bound.  Conversely, an eligible lift with
slot \(z\ge0\) requires at least the second predecessor occurrence.  The
same reduced passage therefore makes the slot-zero lift eligible, so its
core lies in \(\mathcal A_{d,k,H}\).  There are at most
\(F_r(d,k)\) lifts over such a core. \(\square\)

In the main Pascal saddle

\[
 d={r\over2}+O(\sqrt{r\log r}),
 \qquad
 k={r\over6}+O(\sqrt{r\log r}),
 \tag{3.2}
\]

one has uniformly

\[
 \boxed{
 {K_0(d,k)\over F_r(d,k)}
 ={3\over4}+O\!\left(\sqrt{\log r\over r}\right).}
 \tag{3.3}
\]

Thus the decorated core mass and the outer one-point mass are comparable;
there is no vanishing one-step fibre factor.

## 4. Two-point fibre comparison under the actual block rotation

For \(t\ge1\), semiconjugacy gives a canonical bijection

\[
 \tau_r^t:\mathcal F_E\longrightarrow
             \mathcal F_{\tau_d^tE}.
 \tag{4.1}
\]

No assumption is made that (4.1) is a coordinate permutation of Pascal
slots.  This point is essential: general PBBS block rotation may transport
the slot hyperplane nontrivially.

Suppose both

\[
 E,\tau_d^tE\in\mathcal A_{d,k,H}.
\]

Inside the reference fibre \(\mathcal F_E\), the two sufficient
zero-slot sets are

\[
 \mathcal Z_E,
 \qquad
 \tau_r^{-t}\mathcal Z_{\tau_d^tE}.
\]

Both have cardinality \(K_0(d,k)\), solely by the genuine fibre
bijection (4.1).  Therefore

\[
 \boxed{
 |\mathcal Z_E\cap
   \tau_r^{-t}\mathcal Z_{\tau_d^tE}|
 \ge 2K_0(d,k)-F_r(d,k).}
 \tag{4.2}
\]

Every lift in this intersection is eligible both at phase zero and at
phase \(t\).  Notice that (4.2) is inclusion--exclusion inside the actual
PBBS fibre; it does not assume independent or common-order slot columns.

Let \(\widetilde{\mathcal C}_H(d,k)\) be the contribution to the parent
two-point statistic from the \((d,k)\) cell.

### Theorem 4.1 (two-point fibre sandwich)

One has

\[
 \boxed{
 \begin{aligned}
 &(2K_0(d,k)-F_r(d,k))_+
   \sum_{t=1}^{H+1}
    |\mathcal A_{d,k,H}\cap
       \tau_d^{-t}\mathcal A_{d,k,H}|\\
 &\hspace{22mm}\le
   \widetilde{\mathcal C}_H(d,k)\\
 &\hspace{22mm}\le
 F_r(d,k)
   \sum_{t=1}^{H+1}
    |\mathcal A_{d,k,H}\cap
       \tau_d^{-t}\mathcal A_{d,k,H}|.
 \end{aligned}}
 \tag{4.3}
\]

#### Proof

The lower bound is (4.2), summed over every reduced core pair and every
lag.  For the upper bound, if a parent root and its phase-\(t\) translate
are both eligible, Lemma 3.1 applied at the two phases says that both
reduced cores belong to \(\mathcal A_{d,k,H}\).  A fixed reduced core
pair has at most the full fibre size \(F_r(d,k)\) common parent lifts.
Summation proves (4.3). \(\square\)

At the saddle, (3.3) gives

\[
 \boxed{
 {2K_0-F_r\over F_r}
 ={1\over2}+O\!\left(\sqrt{\log r\over r}\right).}
 \tag{4.4}
\]

This positive half-fibre intersection is the decisive point.  Arbitrary
canonical transport of two subsets of density \(3/4+o(1)\) cannot make
them almost disjoint.

## 5. Equivalence of the outer and reduced clustering ratios

Restrict \((d,k)\) to the saddle tube (3.2), and define

\[
 \mathscr R_H
  =\sum_{(d,k)}F_r(d,k)|\mathcal A_{d,k,H}|,
 \tag{5.1}
\]

\[
 \mathscr C_H
  =\sum_{(d,k)}F_r(d,k)
    \sum_{t=1}^{H+1}
     |\mathcal A_{d,k,H}\cap
       \tau_d^{-t}\mathcal A_{d,k,H}|.
 \tag{5.2}
\]

Summing Lemma 3.1 and Theorem 4.1 gives

\[
 \left({3\over4}-o(1)\right)\mathscr R_H
 \le\widetilde R_H^{\rm sad}
 \le\mathscr R_H,
 \tag{5.3}
\]

\[
 \left({1\over2}-o(1)\right)\mathscr C_H
 \le\widetilde{\mathcal C}_H^{\rm sad}
 \le\mathscr C_H.
 \tag{5.4}
\]

Consequently

\[
 \boxed{
 \left({1\over2}-o(1)\right)
 {\mathscr C_H\over\mathscr R_H}
 \le
 {\widetilde{\mathcal C}_H^{\rm sad}
   \over\widetilde R_H^{\rm sad}}
 \le
 \left({4\over3}+o(1)\right)
 {\mathscr C_H\over\mathscr R_H}.}
 \tag{5.5}
\]

This proves the claimed two-point equivalence before deleting short parent
cycles.

Let \(Z_H\) be the number of parent roots on quotient cycles of length at
most \(H+1\).  Removing those roots changes the one-point statistic by at
most \(Z_H\) and the two-point statistic by at most

\[
 2(H+1)Z_H.
 \tag{5.6}
\]

The audited voltage-itinerary estimate gives

\[
 Z_H=\exp(o_A(r)).
\]

Likewise, the audited Pascal-saddle moderate-deviation deletion has outer
mass \(o_A(B_r/r)\), so its entire two-point contribution is
\(o_A(B_r/\sqrt r)=o_A(B_r/H)\).  Hence (5.5) remains valid, with additive
\(o_A(B_r/H)\) errors, for the retained long-cycle statistic whenever the
one-point mass is of critical order.

The conclusion is exact at the qualitative level:

\[
 \boxed{
 \begin{aligned}
 \mathcal C_H=O_A(R_H)
 &\Longleftrightarrow
 \mathscr C_H=O_A(\mathscr R_H),\\
 \mathcal C_H/R_H\to\infty
 &\Longleftrightarrow
 \mathscr C_H/\mathscr R_H\to\infty,
 \end{aligned}}
 \tag{5.7}
\]

provided the critical mass is concentrated in the audited saddle tube.

## 6. A second Fejér bound on the tilted core space

The weights \(F_r(d,k)\) are constant on every \(\tau_d\)-cycle.
Therefore one may replace each reduced core by \(F_r(d,k)\) formal copies
and apply Theorem 1.1 to the resulting disjoint union of genuine reduced
cycles.  The total replicated mass is at most

\[
 \sum_{d,k}F_r(d,k)
  \#\{E\in\mathcal D_d:\operatorname {pk}(E)=k\}
 \le B_r.
\]

This gives

\[
 \boxed{
 \mathscr C_H
 \ge {1\over2}\left(
  {(H+2)\mathscr R_H^2\over B_r}-\mathscr R_H
 \right).}
 \tag{6.1}
\]

Thus

\[
 {H\mathscr R_H\over B_r}\to\infty
 \quad\Longrightarrow\quad
 {\mathscr C_H\over\mathscr R_H}\to\infty,
\]

and equation (5.5) transports this divergence back to the genuine outer
return process.  At
\(\mathscr R_H=\Theta(B_r/H)\), however, (6.1) again gives only a
constant.  Peak deletion does not move the critical threshold.

## 7. Connection to the large-lag linear cell

For one positive-winding return, a selected chronological cell has
internal endpoints

\[
 D_j,\qquad \phi D_k=\phi\tau^{k-j}D_j.
\]

The cell asserts an overlap of the literal carrier blocks
\(S_j1\) and \(\overline T_k1\).  It does **not** assert that either
internal endpoint starts another omitted-label return.  In particular,

\[
 E_j\cap O_k\ne\varnothing
 \quad\not\Longrightarrow\quad
 D_j,\tau^tD_j\in E_H
\]

for any specified \(t\).  The left side is a carrier-coordinate
intersection; the right side consists of two complete first-return
congruences and their proper-prefix exclusions.

Here is the exact missing counterterm in the unpruned block ledger.  Put

\[
 a_i=\delta(D_i),\qquad c_i=d(D_i),\qquad
 \widehat c_i=d(\phi D_i)
\]

and, for a proposed step-two duration \(s\), define

\[
 F_i^{(s)}=\sum_{u=0}^{s-1}c_{i+u}-a_{i+s}.
 \tag{7.1}
\]

The simultaneous canonical block rotations obey

\[
 a_{i+1}-a_i=c_i-\widehat c_i.
\]

Consequently an exact telescope gives

\[
 \boxed{
 F_{i+t}^{(s)}-F_i^{(s)}
 =\sum_{u=0}^{t-1}\widehat c_{i+s+u}
  -\sum_{u=0}^{t-1}c_{i+u}.}
 \tag{7.2}
\]

If phases \(i\) and \(i+t\) both start returns of duration \(s\) and
windings \(w\) and \(v\), respectively, then

\[
 \boxed{
 \sum_{u=0}^{t-1}\widehat c_{i+s+u}
 -\sum_{u=0}^{t-1}c_{i+u}=(v-w)N.}
 \tag{7.3}
\]

By contrast, the large-cell coarea bound controls an interior quantity of
the form

\[
 |E_j\cap O_k|(k-j)
 \le\sum_{u=1}^{s-1}a_{i+u}.
\]

It contains neither boundary sum in (7.3).  For different return
durations the subtraction leaves an additional unmatched interior
segment.  Thus the exact block algebra supplies no implication from a
large-lag cell to a second start: (7.3), together with the second
proper-prefix chronology, is the missing condition.

After peak deletion, the parent start itself maps to one decorated core
\(E\in\mathcal A_{d,k,H}\).  A necessary core-level condition for a
second parent return at lag \(t\) is

\[
 \tau_d^tE\in\mathcal A_{d,k,H}.
 \tag{7.4}
\]

The exact average number of such phases is

\[
 \boxed{
 {\mathscr C_H\over\mathscr R_H}
 ={\sum_{d,k}F_r(d,k)
    \sum_{E\in\mathcal A_{d,k,H}}
    \deg_H(E)
   \over
   \sum_{d,k}F_r(d,k)|\mathcal A_{d,k,H}|},}
 \tag{7.5}
\]

where

\[
 \deg_H(E)=
  \sum_{t=1}^{H+1}
   \mathbf1_{\mathcal A_{d,k,H}}(\tau_d^tE).
 \tag{7.6}
\]

Equivalently, with no probabilistic interpretation,

\[
 \boxed{
 \mathscr C_H=
 \sum_{d,k}F_r(d,k)
 \sum_{E\in\mathcal D_d:\,\operatorname {pk}(E)=k}
 \sum_{t=1}^{H+1}
 \mathbf1_{\{V_G(E)\ge2\}}
 \mathbf1_{\{V_G(\tau_d^tE)\ge2\}}.}
 \tag{7.7}
\]

This is the precise simultaneous-rotation connection.  The large-lag
cell is produced inside the itinerary beginning at \(E\), whereas a term
counted by (7.7) requires the complete predecessor-passage predicate to restart
at the translated root \(\tau_d^tE\).  No identity in the cell ledger
turns the first predicate into the second.

Therefore the exact cell-to-clustering lemma still needed is one of the
following mutually exclusive statements.

* **Bounded decorated degree:**
 \(\mathbb E_{\mathrm{Pascal}}[\deg_H(E)]=O_A(1)\).
  Together with \(R_H=\Omega_A(B_r/H)\), this gives
  \(\mathcal C_H=O_A(R_H)\) and refutes \((ST_A)\).

* **Divergent decorated degree:**
 \(\mathbb E_{\mathrm{Pascal}}[\deg_H(E)]\to\infty\).
  By (5.5), this gives the necessary clustering mechanism for
  \((ST_A)\).

The expectation in (7.5) is over actual canonical lower-rank PBBS
orbits with the Pascal tilt.  It is not a marginal carrier distribution.
The large-lag linear cell may be used only by proving that its literal
intervening word forces one of these two degree alternatives.

## 8. Decision boundary

The requested global decision is not obtained.  What is decided is the
role of the first inverse level.

1. Supercritical start density forces divergent two-point clustering by
   the sharp Fejér bound (1.4).
2. At critical density, the first Pascal lift preserves the two-point
   clustering ratio within constants \(1/2+o(1)\) and \(4/3+o(1)\).
3. Hence no one-level fibre entropy, transported-slot rearrangement, or
   large carrier cell can by itself decide \((ST_A)\).
4. The smallest remaining theorem is the Pascal-weighted decorated-degree
   estimate (7.5) for simultaneous lower-rank block rotations.

In particular, the present mathematics proves neither an
\(O_A(R_H)\) upper bound nor a divergent lower bound at
\(R_H\asymp B_r/H\).  Claiming either would require new information about
the actual joint occurrences of two decorated predecessor passages.
