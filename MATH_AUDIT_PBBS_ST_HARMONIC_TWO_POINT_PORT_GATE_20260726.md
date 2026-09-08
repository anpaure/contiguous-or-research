# The ST two-point gate on harmonic PBBS profiles: exact fibre neutrality and the residual phase clustering

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,                 \tag{0.1}
\]

and retain the long quotient cycles.  Let \(E_H\) be the set of genuine
eligible PBBS return starts and

\[
 R_H=|E_H|,\qquad
 \mathcal C_H=\sum_{h=1}^{H+1}|E_H\cap\tau^{-h}E_H|.           \tag{0.2}
\]

The exact Turan alternative is

\[
 \overline\nu_H\ge
 \frac{R_H^2}{R_H+2\mathcal C_H}.               \tag{0.3}
\]

This note computes the contribution of the outer Pascal sheets on a
harmonic passage profile.  The conclusion is decisive but does not settle
\((ST_A)\).

Let \(C\) be a reduced quotient cycle and let \(\Omega_t\) be one fixed
inverse-profile fibre over its phase \(t\).  The PBBS transport gives
bijections

\[
                         \Theta_{t,h}:\Omega_t\longrightarrow\Omega_{t+h}.
                                                                    \tag{0.4}
\]

If phase \(t\) is a reduced predecessor passage, let
\(\mathcal A_t\subseteq\Omega_t\) be the exact outer sheets satisfying
its terminal-slot and upper-profile conditions; otherwise put
\(\mathcal A_t=\varnothing\).  Then the contribution above \(C\) is
exactly

\[
 \boxed{
 R_H(C)=\sum_t|\mathcal A_t|,\qquad
 \mathcal C_H(C)=
 \sum_{h=1}^{H+1}\sum_t
 |\mathcal A_t\cap
   \Theta_{t,h}^{-1}\mathcal A_{t+h}|.}           \tag{0.5}
\]

Thus the two-point gate is an intersection problem for transported
Pascal hyperplanes, not a second one-column estimate.

For the coordinate-stable terminal-zero harmonic tower

\[
                         r_j=\frac R{j+1}\qquad(0\le j\le L+1), \tag{0.6}
\]

let \(M_L\) be its complete inverse-fibre size.  A one-phase terminal-zero
cylinder has exact density

\[
 Q_L=\prod_{j=0}^{L-1}\left(1-\frac1{(j+2)^2}\right)
 =\frac{L+2}{2(L+1)}.                             \tag{0.7}
\]

If two phases transport the terminal-zero coordinate at each level either to
the same slot or to two distinct slots, then, uniformly for
\(L=O(\sqrt R)\), their two-cylinder intersection satisfies

\[
 \boxed{
 (1-o(1))Q_L^2M_L
 \le |\mathcal A_t\cap
          \Theta_{t,h}^{-1}\mathcal A_{t+h}|
 \le Q_LM_L.}                                     \tag{0.8}
\]

In particular all outer-sheet pair correlations are bounded above and
below by absolute positive constants.  They neither create a little-oh
nor create divergent clustering.

Let \(J\) be the set of phases on the reduced skeleton which actually
carry the relevant predecessor passage, and put

\[
 P_H(J)=\sum_{h=1}^{H+1}|J\cap(J-h)|.             \tag{0.9}
\]

On the coordinate-stable harmonic cell, (0.5) and (0.8) give

\[
 \boxed{
 R_H(C)=Q_LM_L|J|,\qquad
 (1-o(1))Q_L^2M_LP_H(J)
 \le\mathcal C_H(C)
 \le Q_LM_LP_H(J).}                               \tag{0.10}
\]

Consequently

\[
 \boxed{
 \frac{\mathcal C_H(C)}{R_H(C)}
 \asymp \frac{P_H(J)}{|J|}.}                      \tag{0.11}
\]

This is the exact harmonic two-point reduction.  Outer-fibre congestion
cancels from the ratio.  Therefore:

* bounded short-lag degree of the genuine reduced passage phases gives
  \(\mathcal C_H^{\rm harm}=O(R_H^{\rm harm})\); combined with
  \(R_H^{\rm harm}=\Omega(B/H)\), it would refute \((ST_A)\) by applying
  the conflict-graph bound to this subset alone;
* if \((ST_A)\) holds at critical one-point mass, then on every
  positive critical harmonic contribution one must have
  \[
                         P_H(J)/|J|\longrightarrow\infty.       \tag{0.12}
  \]

Thus the divergent clustering required by \((ST_A)\), if true, must
already be present in the **reduced canonical passage-phase process**.
It is not supplied by the harmonic Pascal sheets.

Neither alternative is presently proved for the actual global PBBS
process.  In particular, the critical coefficient
\(\Theta(4^r/r^2)=\Theta(B/H)\) of the harmonic profile series is an
upper capacity envelope, not a lower count of canonical passage towers.
It cannot be used to assert \(R_H=\Omega(B/H)\).  Conversely, the actual
singleton-phase family proves that bounded phase degree is dynamically
possible, but its total mass is
\(e^{-\Theta(\sqrt r)}B/H\), so it cannot refute \((ST_A)\).

The exact remaining theorem is therefore the weighted reduced-skeleton
alternative.  Put \(w_C=Q_{L(C)}M_{L(C)}\).  Then

\[
 \boxed{
 \sum_C w_C|J_C|=\Omega(B/H)
 \quad\Longrightarrow\quad
 \begin{cases}
 \sum_C w_CP_H(J_C)=O(B/H),&\text{ST is false},\\
 \displaystyle
 \frac{\sum_C w_CP_H(J_C)}
      {\sum_C w_C|J_C|}\to\infty,&\text{ST can hold}.
 \end{cases}}                                                   \tag{0.13}
\]

Equation (0.13) is about genuine selected-label itineraries on the
critical Pascal saddle.  No one-point port calculation decides it.

## 1. Exact phase-fibre formulas

Fix a reduced quotient cycle

\[
                         C=(E_t)_{t\in\mathbb Z/\ell\mathbb Z}, \tag{1.1}
\]

where \(\ell>H+1\).  Fix one invariant inverse rank/profile cell above
this cycle.  Let \(\Omega_t\) be its finite fibre over \(E_t\).  The
semiconjugacy of peak deletion with \(\tau\) makes the time-\(h\) map a
bijection (0.4).  The fibre size

\[
                         |\Omega_t|=M                             \tag{1.2}
\]

is independent of \(t\).

If the reduced phase \(E_t\) has no predecessor passage leading to an
outer return within the horizon, put \(\mathcal A_t=\varnothing\).  If it
does, \(\mathcal A_t\) is the subset of inverse sheets whose prescribed
terminal values, at every retained inverse level, agree with the passage
chronology.

### Theorem 1.1 (exact lifted one- and two-point ledger)

The roots in this profile cell contribute (0.5) to \(R_H\) and
\(\mathcal C_H\).

#### Proof

At phase \(t\), every sheet in \(\mathcal A_t\) is exactly one outer root
starting an eligible return, and every such root has a unique sheet over
\(E_t\).  Summing proves the first equality.

A sheet \(x\in\Omega_t\) contributes to
\(E_H\cap\tau^{-h}E_H\) exactly when

\[
                         x\in\mathcal A_t,\qquad
                         \Theta_{t,h}x\in\mathcal A_{t+h}.       \tag{1.3}
\]

The number of such sheets is the intersection in (0.5).  Sum over all
base phases and \(1\le h\le H+1\).  Cyclic-cover degrees cause no extra
factor: the disjoint fibres \(\Omega_t\) already contain every sheet over
one base phase exactly once. \(\square\)

At one inverse level with reduced rank \(d\) and free mass \(y\), a
passage prescribing terminal value \(z\) has the exact hyperplane size

\[
                         K_z(d,y)=\binom{y-z+2d-1}{2d-1}.        \tag{1.4}
\]

Thus Theorem 1.1 contains the full one-point predecessor-port ledger.  Its
new datum is

\[
 |\mathcal A_t\cap\Theta_{t,h}^{-1}\mathcal A_{t+h}|,          \tag{1.5}
\]

which depends on the actual phase transport.  The cardinalities
\(|\mathcal A_t|\) do not determine it.

## 2. Exact two-coordinate Pascal intersections

Let

\[
 \mathcal W_{K,y}
 =\{(n_1,\ldots,n_K)\in\mathbb Z_{\ge0}^K:
                         \sum_an_a=y\},           \tag{2.1}
\]

where \(K=2d+1\).  Its cardinality is

\[
                         P_{K,y}=\binom{y+K-1}{K-1}.             \tag{2.2}
\]

For a slot \(a\) and value \(z\), put

\[
                         H_a(z)=\{\mathbf n:n_a=z\}.             \tag{2.3}
\]

Then

\[
                         |H_a(z)|=\binom{y-z+K-2}{K-2}.          \tag{2.4}
\]

For distinct \(a,b\),

\[
 \boxed{
 |H_a(z)\cap H_b(z')|
 =\binom{y-z-z'+K-3}{K-3},}                     \tag{2.5}
\]

with the usual zero convention.  If \(a=b\), the intersection is empty
for \(z\ne z'\) and equals \(H_a(z)\) for \(z=z'\).

#### Proof

After fixing one coordinate, distribute the remaining \(y-z\) units
among \(K-1\) slots.  After fixing two distinct coordinates, distribute
\(y-z-z'\) units among \(K-2\) slots.  Stars and bars gives (2.4)--(2.5).
\(\square\)

For zero slots, write

\[
 q(K,y)=\frac{|H_a(0)|}{P_{K,y}}
 =\frac{K-1}{y+K-1},                              \tag{2.6}
\]

and, for two distinct coordinates,

\[
 q^{(2)}(K,y)
 =\frac{|H_a(0)\cap H_b(0)|}{P_{K,y}}
 =q(K,y)\widetilde q(K,y),                        \tag{2.7}
\]

where

\[
                         \widetilde q(K,y)
 =\frac{K-2}{y+K-2}.                              \tag{2.8}
\]

These are exact identities, not independence approximations.

## 3. The harmonic two-point product

Fix \(L\), choose \(R\) so that all ranks below are integral, and put

\[
                         r_j=\frac R{j+1}\qquad(0\le j\le L+1). \tag{3.1}
\]

At inverse level \(j\),

\[
 d_j=r_{j+1}=\frac R{j+2},\qquad
 y_j=\frac{2R}{(j+1)(j+2)(j+3)},                 \tag{3.2}
\]

and the number of slots is \(K_j=2d_j+1\).  Therefore

\[
 q_j:=q(K_j,y_j)
 =\frac{2d_j}{y_j+2d_j}
 =1-\frac1{(j+2)^2}.                              \tag{3.3}
\]

The complete profile-fibre size is

\[
                         M_L=\prod_{j=0}^{L-1}P_{K_j,y_j}.      \tag{3.4}
\]

Assume now that, on the displayed phase interval, the actual inverse-slot
transport is coordinate-stable: at each level, a phase-zero terminal
condition pulls back to the vanishing of one coordinate of the reference
weak composition.  The coordinate may depend on the phase and the level.
This includes the exact mountain rotor and every interval on which the
same inverse frame remains canonical.

One phase fixes one zero coordinate at every level, so its cylinder has
size

\[
                         Q_LM_L,\qquad
 Q_L=\prod_{j=0}^{L-1}q_j
 =\frac{L+2}{2(L+1)}.                             \tag{3.5}
\]

Take two phases.  Let \(D\subseteq\{0,\ldots,L-1\}\) be the levels at
which they prescribe two distinct coordinates.  Equations (2.6)--(2.8)
give the exact intersection density

\[
 \boxed{
 \frac{|\mathcal A_t\cap
          \Theta_{t,h}^{-1}\mathcal A_{t+h}|}{M_L}
 =Q_L\prod_{j\in D}\widetilde q_j.}              \tag{3.6}
\]

At levels not in \(D\), the two conditions coincide and contribute only
the one factor \(q_j\).

### Theorem 3.1 (harmonic outer fibres are two-point neutral)

Uniformly for \(L=O(\sqrt R)\), every pair in (3.6) satisfies (0.8).

#### Proof

Put \(a_j=K_j-1=2d_j\).  Direct algebra gives

\[
 \frac{\widetilde q_j}{q_j}
 =\frac{(a_j-1)(a_j+y_j)}
        {a_j(a_j+y_j-1)}
 =1-\varepsilon_j,                                \tag{3.7}
\]

where

\[
 \varepsilon_j=\frac{y_j}{a_j(a_j+y_j-1)}.        \tag{3.8}
\]

For \(L=O(\sqrt R)\), one has \(a_j\to\infty\) uniformly and

\[
 \sum_{j=0}^{L-1}\varepsilon_j
 =O\left(\frac{\log(L+2)}R\right)=o(1).           \tag{3.9}
\]

Indeed \(y_j/a_j=1/((j+1)(j+3))\) and
\(a_j=2R/(j+2)\), so the summand is \(O(1/(R(j+1)))\).
Consequently

\[
 \prod_{j\in D}\widetilde q_j
 \ge(1-o(1))\prod_{j\in D}q_j
 \ge(1-o(1))Q_L.                                  \tag{3.10}
\]

The first inequality follows by multiplying (3.7); the second uses
\(0<q_j\le1\) and \(D\subseteq\{0,\ldots,L-1\}\).  Equations
(3.6) and (3.10) give the lower bound in (0.8).  The upper bound follows
from intersection being contained in either one-phase cylinder. \(\square\)

Since \(1/2<Q_L\le3/4\), the constants in (0.8) can be taken, for all
sufficiently large \(R\), to be any fixed numbers below \(1/4\) and above
\(3/4\), respectively.

## 4. Reduction to the reduced passage-phase process

Let \(J\subseteq\mathbb Z/\ell\mathbb Z\) be the phases at which the
reduced canonical skeleton supplies the terminal-zero predecessor passage
being lifted.  For \(t\notin J\), put \(\mathcal A_t=\varnothing\); for
\(t\in J\), use the harmonic cylinder of Section 3.

The one-point identity in (0.10) follows from (3.5).  For every ordered
pair \((t,t+h)\in J^2\) with \(1\le h\le H+1\), Theorem 3.1 supplies the
two bounds in (0.8).  Summing them proves the two-point inequalities in
(0.10), hence (0.11).

This calculation distinguishes three logically separate regimes.

1. **Dense phase blocks.**  If \(J\) contains blocks of length
   \(\Theta(H)\) on a positive fraction of its mass, then
   \[
                         P_H(J)/|J|=\Theta(H),                   \tag{4.1}
   \]
   and the required clustering diverges.  This is the behavior permitted
   by the terminal mountain rotor before upper-level chronology is imposed.

2. **Bounded-degree phases.**  If every phase in \(J\) has only \(O(1)\)
   forward neighbors from \(J\) within distance \(H+1\), then
   \[
                         P_H(J)=O(|J|),                          \tag{4.2}
   \]
   and \(\mathcal C_H(C)=O(R_H(C))\).  At global critical one-point mass,
   (0.3) refutes \((ST_A)\).  The actual singleton-phase construction
   realizes the extreme local case \(P_H(J)=0\), but not at critical mass.

3. **Critical ST behavior.**  If \((ST_A)\) is true and these harmonic
   cells contribute \(\Omega(B/H)\) starts, (0.3) and (0.11) force the
   weighted average of \(P_H(J)/|J|\) to diverge.

The outer fibre cannot distinguish regimes 1 and 2.  It multiplies their
one- and two-point counts by the same profile capacity, up to absolute
constants.

## 5. What fails outside a coordinate-stable block

For a general canonical PBBS phase, the fibre transport in (0.4) is a
bijection but need not carry a terminal-slot hyperplane to a single
coordinate hyperplane of the reference weak composition.  A frame change
can turn it into a block-sum or more complicated passage cylinder.  Then
the exact formula remains (0.5), but (2.5) and (3.6) no longer apply.

This is not a removable technicality.  The proved reciprocal-height
stability theorem says that any critical counterfamily can be reduced,
after little-oh loss, to returns which

* reframe on a positive fraction of their transitions; and
* contain no coordinate-stable block longer than
  \((1/2+\varepsilon)\log_2r+O(1)\).

Thus the coordinate-stable two-point calculation covers precisely the
sector in which the slot transport is explicit, while a critical residual
may live in the dense-reframing sector where the transported cylinders are
not coordinate hyperplanes.  The remaining two-point object is literally

\[
 \boxed{
 \Gamma_{t,h}
 :=|\mathcal A_t\cap
       \Theta_{t,h}^{-1}\mathcal A_{t+h}|.}        \tag{5.1}
\]

No marginal Pascal count determines \(\Gamma_{t,h}\).

## 6. Why the critical one-point lower bound is still absent

The harmonic full-fan coefficient series has critical order

\[
                         \Theta(4^r/r^2)=\Theta(B/H).           \tag{6.1}

This is an upper capacity envelope.  Its integral objects are formal
weak-composition tower tuples, and no bounded-fibre realization map into
canonical PBBS passage towers is known.  Therefore (6.1) cannot be used
as

\[
                         R_H=\Omega(B/H).                         \tag{6.2}

The distinction is essential.  A separate actual construction produces
singleton-phase critical-shaped roots and pairwise edge-disjoint returns,
but its forced collar has length \(\Theta(\sqrt r)\).  Its count is only

\[
                         e^{-\Theta(\sqrt r)}B/H,                \tag{6.3}

not the scale in (6.2).

Conversely, the terminal mountain rotor supplies \(\Theta(H)\) admissible
phase anchors and the pair-overlap law of Section 3, but terminal
admissibility is only necessary for the upper parent return.  It cannot be
used to lower-bound actual members of \(E_H\).

Hence neither

\[
 R_H=\Omega(B/H),\quad\mathcal C_H=O(R_H),                        \tag{6.4}

nor the unconditional divergent alternative has been proved for the
actual PBBS process.

## 7. Exact remaining weighted dichotomy

For every coordinate-stable harmonic cell \(\xi\), let

\[
 w_\xi=Q_{L(\xi)}M_{L(\xi)},\qquad
 J_\xi=\text{its genuine reduced passage-phase set}.            \tag{7.1}
\]

Summing (0.10) gives

\[
 R_H^{\rm harm}=\sum_\xi w_\xi|J_\xi|,                           \tag{7.2}
\]

and

\[
 c\sum_\xi w_\xi P_H(J_\xi)
 \le\mathcal C_H^{\rm harm}
 \le C\sum_\xi w_\xi P_H(J_\xi)                               \tag{7.3}
\]

for absolute \(0<c<C<\infty\), after negligible finite-rank adjustment.
Therefore the exact harmonic-profile alternatives are:

### Refutation alternative

If

\[
 \sum_\xi w_\xi|J_\xi|\ge c_A B/H,
 \qquad
 \sum_\xi w_\xi P_H(J_\xi)\le C_A
             \sum_\xi w_\xi|J_\xi|,             \tag{7.4}
\]

then

\[
 R_H^{\rm harm}=\Omega_A(B/H),\qquad
 \mathcal C_H^{\rm harm}=O_A(R_H^{\rm harm}),                   \tag{7.5}
\]

and (0.3), applied to the harmonic subset of starts, refutes \((ST_A)\).

### Clustering alternative

If \((ST_A)\) holds and the first inequality in (7.4) holds, then

\[
 \boxed{
 \frac{\sum_\xi w_\xi P_H(J_\xi)}
      {\sum_\xi w_\xi|J_\xi|}
 \longrightarrow\infty.}                         \tag{7.6}
\]

This is the divergent clustering required on harmonic profiles.  It is
stronger in localization than the global two-point alternative: the
outer Pascal weights have been removed, leaving only the genuine reduced
selected-label phase sets.

The unresolved mathematical input is now exactly one of the two
inequalities in (7.4), or the divergence (7.6), for the dense-reframing
canonical passage process.  The predecessor-port container supplies the
weights \(w_\xi\) and proves (7.2)--(7.3); it supplies no estimate for the
sets \(J_\xi\).

## 8. Certified boundary

Proved:

1. the exact phase-fibre identities (0.5);
2. exact one- and two-coordinate Pascal hyperplane counts;
3. the harmonic one-phase density \(Q_L\);
4. uniform constant two-point overlap on coordinate-stable harmonic
   towers;
5. cancellation of outer-fibre congestion in
   \(\mathcal C_H/R_H\); and
6. the localized weighted alternatives (7.4)--(7.6).

Not proved:

1. critical one-point abundance of actual harmonic passage towers;
2. bounded reduced-phase degree;
3. divergent reduced-phase clustering;
4. a two-cylinder estimate through dense frame changes; or
5. \((ST_A)\) or its negation.

The exact predecessor-port container therefore reaches the correct
two-point boundary but does not cross it.  On harmonic profiles the outer
Pascal sheets are neutral; the decision is entirely in the canonical
PBBS phase chronology \(J_\xi\).
