# Audit of the reduced predecessor-passage phase degree at \(ST_A\)

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search,
probabilistic surrogate, or external input is used.

## 0. Verdict

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
 \qquad G=2H-1.
\]

After the exact Pascal-threshold reduction, a reduced root \(E\) is
active precisely when

\[
 Z_H(E):=\max\{z\ge0:B_{2z+2}(E)\le G\}\ge0,
\]

equivalently when \(B_2(E)\le G\).  Write

\[
 \mathscr A_H=\{E:Z_H(E)\ge0\}.
\]

The actual reduced two-sided phase degree is

\[
 \Delta_H(E)=
 \sum_{t=1}^{H+1}
 \left(
 \mathbf1_{\mathscr A_H}(\tau^tE)
 +\mathbf1_{\mathscr A_H}(\tau^{-t}E)
 \right).
\tag{0.1}
\]

This audit proves four things.

1. There is an exact invariant-section model.  If \(\Lambda E\) is the
   unique minimal peak expansion of \(E\), obtained by adding only the
   compulsory leaf at every old leaf and no free leaves, then

   \[
   \boxed{
   \tau\Lambda E=\Lambda\tau E,\qquad
   E\in\mathscr A_H
   \iff \Lambda E\text{ starts an ordinary short PBBS return}.}
   \tag{0.2}
   \]

   Thus \(\Delta_H(E)\) is exactly the return-start phase degree on the
   \(\tau\)-invariant minimal-expansion section.  It is not a Pascal
   occupancy statistic.

2. A critical Pascal mass of bounded \(\Delta_H\) refutes \(ST_A\).
   For every fixed \(K\),

   \[
   \boxed{
   \overline\nu_H\ge {1\over K+1}
   \left[
    \sum_{d,k}K_0(d,k)
    \#\{E\in\mathscr A_H(d,k):\Delta_H(E)\le K\}
    -Z_H^{\rm cyc}
   \right]_+,}
   \tag{0.3}
   \]

   where

   \[
   K_0(d,k)=\binom{m+d-k-1}{2d-1},
   \qquad
   Z_H^{\rm cyc}\le(2H+2)N^{2H+2}=o(B_m/H).
   \]

3. The uncalibrated terminal-singleton statement does **not** by itself
   prove bounded reduced phase degree.  It proves that one chosen parent
   lift has one prescribed duration-\(s\) phase.  The exact threshold
   cylinders show the missing implication:

   \[
   \boxed{
   x\notin\mathcal A_t
   \quad\Longleftrightarrow\quad
   x_{i_t}>Z_H(\tau^tE),}
   \tag{0.4}
   \]

   whereas reduced inactivity is

   \[
   \boxed{Z_H(\tau^tE)=-1.}
   \tag{0.5}
   \]

   Condition (0.4) is compatible with
   \(Z_H(\tau^tE)\ge0\) at every one of the \(H+1\) tested phases.
   Hence parent singleton-phase chronology supplies no bound on
   \(\Delta_H(E)\).

4. The gap can be repaired by choosing the cutoff exactly at the minimum
   duration, \(H=s+1\), and passing to minimal expansions.  This gives
   actual long-period Pascal-saddle cores with

   \[
      \boxed{\Delta_H(E)\le2.}
   \]

   Their complete weighted mass is only

   \[
      {B_m\over H}e^{-\Theta(\sqrt m)}.
   \]

   An exact Narayana ratio shows that even the full inverse Pascal mass
   above every core with the same deterministic collar remains
   \(e^{-\Theta(\sqrt m)}B_m\), hence \(o(B_m/H)\).

5. Neither requested **global** alternative is proved.  The mountain
   calibration has bounded **outer** susceptibility but divergent
   reduced degree, because its reduced core is fixed by \(\tau\).
   The calibrated singleton family has bounded reduced degree but
   subcritical collar mass.  No currently audited family has both
   critical global Pascal mass and bounded reduced degree.

The exact remaining theorem is therefore

\[
\boxed{
\begin{array}{l}
\text{either }\displaystyle
\sum_{d,k}P_m(d,k)
\#\{E\in\mathscr A_H(d,k):\Delta_H(E)\le K\}
=\Omega(B_m/H)
\text{ for some fixed }K,\\[2mm]
\text{or }\Delta_H(E)\to\infty
\text{ in Pascal-weighted probability on every critical active mass.}
\end{array}}
\tag{0.6}
\]

The first line refutes \(ST_A\); the second is necessary for \(ST_A\)
but still requires a higher-order packing upper bound.

## 1. The minimal-expansion invariant section

Fix a nonempty reduced root

\[
 E\in\mathcal D_d,\qquad k=\operatorname {pk}(E).
\]

Every inverse peak-deletion lift is obtained by first placing one
compulsory new leaf at each old leaf and then distributing free leaves
among the \(2d+1\) ordered slots.  At the minimal outer rank

\[
 r_{\min}(E)=d+k,
\tag{1.1}
\]

there is no free mass.  Hence the inverse fibre contains one root.
Denote it by

\[
 \Lambda E.
\tag{1.2}
\]

### Lemma 1.1 (equivariance)

\[
 \boxed{\partial\Lambda E=E,\qquad
        \tau\Lambda E=\Lambda\tau E.}
\tag{1.3}
\]

#### Proof

The first equality is the definition.  Peak deletion semiconjugates the
PBBS quotient map:

\[
 \partial\tau=\tau\partial.
\]

Therefore \(\tau\Lambda E\) lies in the rank-\((d+k)\) inverse fibre over
\(\tau E\).  Rank and peak count are \(\tau\)-invariant, so this is again
the minimal rank and its free mass is zero.  That fibre is a singleton,
namely \(\Lambda\tau E\).  This proves the second equality. \(\square\)

### Theorem 1.2 (predecessor activity is an ordinary return)

Assume \(G<2(d+k)+1\).  Then

\[
 \boxed{
 Z_H(E)\ge0
 \quad\Longleftrightarrow\quad
 g(\Lambda E)=B_2(E)\le G.}
\tag{1.4}
\]

Consequently, for every integer \(t\),

\[
 \boxed{
 \mathbf1_{\mathscr A_H}(\tau^tE)
 =\mathbf1\{g(\tau^t\Lambda E)\le G\}.}
\tag{1.5}
\]

#### Proof

The terminal free occupancy of \(\Lambda E\) is zero.  The exact
no-overtaking predecessor theorem says that a terminal-\(z\) lift first
returns at \(B_{2z+2}(E)\), before the outer circumference.  With
\(z=0\), this is \(B_2(E)\), proving (1.4).  Apply Lemma 1.1 at phase
\(t\) to obtain (1.5). \(\square\)

In the Pascal saddle relevant to rank \(m\),

\[
 d={m\over2}+O(\sqrt{m\log m}),
 \qquad
 k={m\over6}+O(\sqrt{m\log m}),
\tag{1.6}
\]

so

\[
 d+k={2m\over3}+O(\sqrt{m\log m})
\]

and \(G=O(\sqrt m)\) is far below the minimal-expansion circumference.
Thus (1.4) has no wrap exception in the critical cells.

The reduced weighted degree problem can now be stated without inverse
fibres.  Give the minimal-expansion root \(\Lambda E\) the inherited
weight

\[
 P_m(E)=\binom{m+d-k}{2d}.
\tag{1.7}
\]

This weight is constant on every \(\tau\)-orbit.  The exact one- and
two-time reduced statistics are

\[
 \mathscr R_H
 =\sum_EP_m(E)\mathbf1\{g(\Lambda E)\le G\},
\tag{1.8}
\]

\[
 \mathscr C_H
 =\sum_EP_m(E)\mathbf1\{g(\Lambda E)\le G\}
   \sum_{t=1}^{H+1}
    \mathbf1\{g(\tau^t\Lambda E)\le G\}.
\tag{1.9}
\]

Hence

\[
 {2\mathscr C_H\over\mathscr R_H}
\]

is the Pascal-weighted mean of \(\Delta_H\).  Equations (1.8)--(1.9)
are the precise reduced predecessor-passage process.

## 2. Exact bounded-degree pullback to a parent packing

For an eligible rank-\(m\) parent root \(D\), let \(I_D\) be its actual
quotient residence trace.  It has at most \(H+1\) consecutive quotient
edges.  Let \(d_H(D)\) be its degree in the graph joining two eligible
starts whose traces share an edge.

### Lemma 2.1 (conflict localization)

If \(D\) lies over \(E=\partial D\), then

\[
 \boxed{d_H(D)\le\Delta_H(E).}
\tag{2.1}
\]

#### Proof

Two conflicting traces lie on the same parent quotient cycle.  Since
each has at most \(H+1\) consecutive edges, one start is
\(\tau^{\pm t}D\) from the other for some \(1\le t\le H+1\).
Semiconjugacy sends that neighbour to \(\tau^{\pm t}E\).  Eligibility of
the parent neighbour implies \(Z_H(\tau^{\pm t}E)\ge0\).  Thus every
distinct conflict neighbour consumes one lag incidence in (0.1);
repeated descriptions only enlarge the right side. \(\square\)

Every active core \(E\) has an entire eligible terminal-zero hyperplane
of cardinality

\[
 K_0(d,k)=\binom{m+d-k-1}{2d-1}.
\tag{2.2}
\]

### Theorem 2.2 (critical bounded-degree obstruction)

For every integer \(K\ge0\), equation (0.3) holds.

#### Proof

For every active \(E\) with \(\Delta_H(E)\le K\), take all its
terminal-zero rank-\(m\) lifts.  They are eligible by the predecessor
theorem, and Lemma 2.1 gives conflict degree at most \(K\).  Delete the
at most \(Z_H^{\rm cyc}\) roots on short parent cycles.

For any finite graph,

\[
 \alpha(G)\ge\sum_{v}{1\over d(v)+1}.
\]

Apply this to the full parent conflict graph and retain only the
constructed vertices.  Each contributes at least \(1/(K+1)\), proving
(0.3). \(\square\)

At the saddle,

\[
 {K_0(d,k)\over P_m(d,k)}
 ={2d\over m+d-k}
 ={3\over4}+o(1).
\tag{2.3}
\]

Define

\[
 \mathscr L_{H,K}
 =\sum_{d,k}P_m(d,k)
   \#\{E\in\mathscr A_H(d,k):\Delta_H(E)\le K\}.
\tag{2.4}
\]

The total inverse mass outside (1.6) is \(o(B_m/m)\).  Therefore

\[
 \boxed{
 \overline\nu_H
 \ge {(\frac34-o(1))\mathscr L_{H,K}-o(B_m/H)
       \over K+1}.}
\tag{2.5}
\]

The established minimal-simple-return reduction loses at most a factor
two.  Hence

\[
 \boxed{
 \liminf {H\mathscr L_{H,K}\over B_m}>0
 \text{ for one fixed }K
 \quad\Longrightarrow\quad ST_A\text{ is false}.}
\tag{2.6}
\]

Conversely, \(ST_A\) implies

\[
 \mathscr L_{H,K}=o(B_m/H)
\qquad\text{for every fixed }K.
\tag{2.7}
\]

If \(\mathscr R_H\ge\kappa B_m/H\), this is exactly

\[
 \Delta_H(E)\longrightarrow\infty
\]

in Pascal-weighted probability conditional on \(E\in\mathscr A_H\).

## 3. Parent phase support is not reduced phase support

Fix one reduced cycle \(E_t=\tau^tE_0\), one invariant rank/peak cell
above it, and pull every parent fibre back to a common weak-composition
simplex

\[
 \mathcal W_{p,y}
 =\{x\in\mathbb Z_{\ge0}^p:\sum_ix_i=y\}.
\]

The exact threshold cylinder at phase \(t\) is

\[
 \mathcal A_t
 =\{x:x_{i_t}\le Z_t\},
\qquad
 Z_t=Z_H(E_t),
\tag{3.1}
\]

with \(\mathcal A_t=\varnothing\) when \(Z_t=-1\).  Here \(i_t\) is the
transported terminal-slot address.

The reduced active phase set is

\[
 J=\{t:Z_t\ge0\}.
\tag{3.2}
\]

For one selected parent vector \(x\), its active phase set is

\[
 J(x)=\{t:x_{i_t}\le Z_t\}.
\tag{3.3}
\]

Necessarily

\[
 J(x)\subseteq J,
\tag{3.4}
\]

but equality need not hold.

### Proposition 3.1 (exact singleton counterterm)

If one parent vector \(x\) has a unique active phase \(0\) in a phase
window \(W\), then the exact conclusion at every \(t\in W\setminus\{0\}\)
is only

\[
 \boxed{x_{i_t}\ge Z_t+1.}
\tag{3.5}
\]

It does not imply \(Z_t=-1\), and hence gives no upper bound on
\(|J\cap W|\) or on \(\Delta_H(E)\).

#### Proof

By (3.1), failure of the selected parent at phase \(t\) is exactly the
negation of \(x_{i_t}\le Z_t\), which is (3.5).  Reduced inactivity is
the emptiness of the whole cylinder, equivalently \(Z_t=-1\).  The first
condition concerns one point of the simplex; the second concerns its
support. \(\square\)

The distinction is quantitatively live at the saddle.  Let

\[
 p>H+1,\qquad y\ge H,
\]

take distinct addresses \(i_t=t\) for \(0\le t\le H\), and set

\[
 Z_t=0\quad(0\le t\le H).
\]

Choose a weak composition with

\[
 x_0=0,\qquad x_t=1\ (1\le t\le H),
\]

placing the remaining free mass arbitrarily.  Then

\[
 J=\{0,1,\ldots,H\},
\qquad
 J(x)=\{0\}.
\tag{3.6}
\]

This is an exact threshold-cylinder configuration, not an assertion that
every such configuration is PBBS-realizable.  Its logical consequence is
decisive: Pascal support geometry cannot convert singleton parent
chronology into bounded reduced phase degree.  In the critical saddle
\(p=(1+o(1))m\), \(y=(1/3+o(1))m\), and \(H=\Theta(\sqrt m)\), so the
configuration satisfies the genuine parameter inequalities with ample
free mass.

More generally, for active but rejected phases,

\[
 |J\setminus J(x)|
 \le\sum_{t\in J\setminus J(x)}x_{i_t}
\tag{3.7}
\]

when all thresholds are zero.  Even if all addresses are distinct, the
right side may be as large as \(y=\Theta(m)\), much larger than the
\(\Theta(\sqrt m)\) phase window.  With repeated addresses there is even
less control.  No hidden free-mass inequality closes the gap.

## 4. Audit of the two standard calibrations

### 4.1 Mountain renewal

For the Gaussian mountain inverse fibre, the outer start process has

\[
 {R_H^{\rm mt}\over|\Omega_{m,h}|}=\Theta(1/H),
\qquad
 {\mathcal C_H^{\rm mt}\over R_H^{\rm mt}}=O(1).
\]

This does not provide a bounded reduced phase.  Its reduced mountain core
is fixed by \(\tau\) in the relevant quotient normalization and is
predecessor-active.  Hence every lag \(1\le t\le H+1\) is again active,
so

\[
 \Delta_H(E_{\rm mt})=2(H+1).
\tag{4.1}
\]

The bounded outer ratio comes instead from the sparse terminal-zero
fraction

\[
 {K_0\over P}
 =\Theta(1/H)
\]

outside the Pascal saddle and from the rotation of the tested free
coordinate.  Thus mountain bounded susceptibility is not evidence for
bounded reduced degree.

### 4.2 Terminal-singleton family

The terminal-singleton construction proves that one explicit top parent
root has one duration-\(s\), zero-winding return-start phase in a
terminal-rotor period, and that its constructed parent conflict graph has
maximum degree two.  After first peak deletion, its core \(E\) satisfies
\(Z_H(E)\ge0\).

There are actually two gaps between this statement and bounded reduced
degree.

First, uniqueness was proved for the prescribed duration-\(s\)
zero-winding return.  It does not exclude a different eligible duration
at another phase, so it does not by itself prove that the chosen parent
lies outside the full threshold cylinder \(\mathcal A_t\).

Second, even if this stronger full-horizon parent singleton statement
were added, Proposition 3.1 would give only

\[
 x_{i_t}>Z_H(\tau^tE)
\]

for the particular parent vector.  It would still not give reduced
inactivity.

What is not proved is

\[
 Z_H(\tau^tE)=-1
\qquad(1\le |t|\le H+1).
\tag{4.2}
\]

The complete terminal-zero lift above any phase with
\(Z_H(\tau^tE)\ge0\) would still be eligible, even if the constructed
parent were rejected there.

Therefore the sentence that the terminal-singleton construction has
bounded \(T_H/S_H\), when \(T_H/S_H\) denotes the reduced active-phase
ratio of the exact Pascal-threshold theorem, is not established by the
proved parent chronology.  Bounded degree is established only for the
selected constructed duration-\(s\) parent family.  This is the precise
hidden issue in using that family as a calibration of the reduced
predecessor process.

Even if a separate proof of (4.2) were supplied, the constructed family
has only

\[
 {B_m\over H}\exp[-\Theta(\sqrt m)]
\]

ambient mass because of its deterministic \(\Theta(\sqrt m)\) collar.
It would remain a subcritical bounded-degree calibration rather than a
global refutation.

## 5. Exact remaining theorem

The Pascal threshold and transport have now been completely separated
from the reduced dynamics.

* The outer fibre cannot create a bounded-degree obstruction unless the
  reduced active support already has bounded degree on critical weight.
* A selected parent can have one active phase while its reduced core has
  every nearby phase active.
* Long parent period, positive boundary, terminal-rotor phase isolation,
  and bounded selected-parent conflict degree do not settle
  \(\Delta_H\).

The direct positive target is

\[
 \boxed{
 \forall K<\infty,\qquad
 \sum_{d,k}P_m(d,k)
 \#\{E\in\mathscr A_H(d,k):\Delta_H(E)\le K\}
 =o(B_m/H).}
\tag{5.1}
\]

At critical active mass this is divergence in probability of the exact
minimal-expansion return-start degree.  It is necessary for \(ST_A\).

The direct negative target is the reverse for one fixed \(K\):

\[
 \boxed{
 \sum_{d,k}P_m(d,k)
 \#\{E\in\mathscr A_H(d,k):\Delta_H(E)\le K\}
 \ge\kappa {B_m\over H}}
\tag{5.2}
\]

along a subsequence.  By Theorem 2.2, this gives a literal
\(\Omega(B_m/H)\) PBBS packing and refutes \(ST_A\).

No audited identity presently proves (5.1) or (5.2).  The smallest
remaining object is the weighted ordinary-return process on the
minimal-expansion section \(\Lambda\mathcal D_d\), equations
(1.8)--(1.9).  Any further use of a parent singleton family must first
prove a support statement of the form (4.2); one-point cylinder exclusion
is insufficient.

## 6. A calibrated bounded reduced-degree family

The terminal-singleton construction can nevertheless be repaired as a
reduced-degree calibration when the horizon is set exactly at its minimum
return duration.  The repair does not reach critical global mass.

Fix \(A>0\).  For each sufficiently large integer \(p\), put

\[
 s=2p-1,\qquad h=p-2,
\tag{6.1}
\]

and choose

\[
 r_p=\left\lfloor {4p^2\over A^2}\right\rfloor,
 \qquad
 M_p=r_p-3p+1.
\tag{6.2}
\]

Then

\[
 \lceil A\sqrt{r_p}\rceil=2p=s+1
\tag{6.3}
\]

for all sufficiently large \(p\): the floor in (6.2) changes
\(A\sqrt{r_p}\) from \(2p\) by \(O(1/p)<1\).  Also

\[
 {h\over\sqrt{M_p}}\longrightarrow {A\over2}.
\tag{6.4}
\]

For every Dyck filler \(F\) of semilength \(M_p\) and exact height \(h\),
put

\[
 D(F)=1^p0^p1^{2p-1}0^{p+1}F0^{p-2},
\tag{6.5}
\]

and let

\[
 E(F)=\partial D(F).
\tag{6.6}
\]

### Lemma 6.1 (minimal expansion retains the singleton word)

Let \(G=\partial F\), and let \(F_{\min}=\Lambda G\) be the minimal peak
expansion of \(G\).  Then

\[
 \boxed{\Lambda E(F)=D(F_{\min}).}
\tag{6.7}
\]

Moreover,

\[
 \operatorname {ht}(F_{\min})=h,
 \qquad
 \operatorname {ht}(\Lambda E(F))=s.
\tag{6.8}
\]

#### Proof

Direct simultaneous peak deletion in (6.5) gives

\[
 E(F)=
 1^{p-1}0^{p-1}
 1^{2p-2}0^p
 G0^{p-2}.
\tag{6.9}
\]

Its leaves are the two displayed collar peaks together with the leaves
of \(G\).  Adding exactly one compulsory new leaf at each of these leaves
restores the two deleted collar peaks and replaces \(G\) by its minimal
expansion \(F_{\min}\).  No free peak is inserted, proving (6.7).

Peak deletion lowers the height of every nonempty Dyck path by exactly
one, while minimal peak expansion raises it by one.  Since
\(\operatorname {ht}(F)=h\), one has
\(\operatorname {ht}(G)=h-1\) and
\(\operatorname {ht}(F_{\min})=h\).  The second collar in (6.7) has
height \(2p-1=s\), while the filler has smaller height \(p-2\), proving
(6.8). \(\square\)

### Theorem 6.2 (bounded reduced predecessor degree)

Suppose \(E=E(F)\) lies on a reduced quotient cycle longer than
\(2s+4\).  Then

\[
 \boxed{\Delta_H(E)\le2.}
\tag{6.10}
\]

#### Proof

By Theorem 1.2, a phase \(\tau^tE\) is predecessor-active exactly when
the minimal expansion

\[
 \tau^t\Lambda E=\Lambda\tau^tE
\]

starts an ordinary return of residence at most \(H=s+1\).

The PBBS quotient map preserves height.  Lemma 6.1 therefore makes every
phase of \(\Lambda E\) a height-\(s\) root.  The exact height-gap theorem
says that every return from such a phase has odd gap at least \(2s+1\),
or residence at least \(s+1\).  Hence every return admitted by the cutoff
has exactly duration \(s\).

The terminal-singleton theorem applied to the word \(D(F_{\min})\)
states that, in one terminal-rotor period of length \(s\), only its
distinguished residue can start this duration-\(s\) return.  By
semiconjugacy through the terminal rotor, every active phase of
\(\Lambda E\) is consequently congruent to zero modulo \(s\).

The two-sided degree window is

\[
 1\le |t|\le H+1=s+2.
\]

On a cycle longer than \(2s+4\), the only nonzero multiples of \(s\) in
this window are \(t=s\) and \(t=-s\).  Thus at most two lag incidences
are active, proving (6.10). \(\square\)

This theorem closes both gaps identified in Section 4.2 for the
calibrated family.  The exact horizon eliminates every alternative
duration, and minimal expansion makes the parent phase process identical
to the reduced support process.

## 7. Exact weight of the calibrated obstruction

The bounded-degree family is large enough to survive every exponential
saddle and short-period deletion, but it remains
stretched-exponentially below \(B_r/H\).

### 7.1 Exact-height filler count

Let \(E_{M,h}\) be the number of semilength-\(M\) Dyck paths of exact
height \(h\).  The path-graph spectral formula is

\[
 C_a(M)=\frac{2}{a+2}\sum_{j=1}^{a+1}
 \sin^2{\pi j\over a+2}
 \left(2\cos{\pi j\over a+2}\right)^{2M},
\tag{7.1}
\]

where \(C_a(M)\) counts height at most \(a\), and

\[
 E_{M,h}=C_h(M)-C_{h-1}(M).
\]

Uniform expansion of (7.1) at \(h/\sqrt M\to c>0\), followed by taking
the first difference, gives the local height law

\[
 \boxed{
 E_{M,h}
 =\left(f(c)+o(1)\right){4^M\over M^2},}
\tag{7.2}
\]

where \(f(c)=\Psi'(c)/\sqrt\pi\ge0\) is the derivative density of

\[
 \Psi(c)=\frac{4\pi^{5/2}}{c^3}
 \sum_{j\ge1}j^2e^{-\pi^2j^2/c^2}.
\tag{7.3}
\]

For completeness, uniformity follows by splitting the sum at
\(j=M^{1/8}\): Taylor expansion is uniform below the split and the
Gaussian tail is uniform above it.  The first difference changes
\(c=h/\sqrt M\) by \(M^{-1/2}\), producing the extra
\(M^{-1/2}\) relative to
\(\operatorname {Cat}_M\asymp4^M/M^{3/2}\).
The function \(\Psi\) is analytic and strictly increasing.  Hence
\(f\) is not identically zero and its zero set in \((0,\infty)\) is
discrete.  In particular \(f(c)>0\) for every \(c\) outside this possible
discrete exceptional set.  Positivity at a specified exceptional value is
not needed for the structural degree theorem, only for the quantitative
shell lower bound below.

For every \(A\) with \(f(A/2)>0\), equations (6.2)--(6.4) give

\[
 \#\{F:|F|_{\rm semi}=M_p,\operatorname {ht}(F)=p-2\}
 =\left(f(A/2)+o(1)\right){4^{M_p}\over M_p^2}.
\tag{7.4}
\]

### 7.2 Pascal-weighted low-degree mass

Different fillers may have the same first-pruned core, but this causes no
loss.  Every \(D(F)\) is a terminal-zero rank-\(r_p\) lift of \(E(F)\).
Thus, after grouping equal cores,

\[
 \sum_{E\in\{E(F)\}}K_0(E)
 \ge \#\{F:\operatorname {ht}(F)=p-2\}.
\tag{7.5}
\]

The right side is

\[
 {B_{r_p}\over H}
 \exp[-(3\log4+o(1))p].
\tag{7.6}
\]

Indeed \(r_p-M_p=3p-1\) and
\(B_{r_p}/H=(1+o(1))4^{r_p}/(\sqrt\pi r_p^2 A)\).

For such \(A\), the family in (7.6) has size
\(B_{r_p}e^{-o(r_p)}\).  The established
Pascal saddle complement and reduced-period-\(O(r/\log r)\) classes each
have mass \(B_{r_p}e^{-\Omega(r_p)}\).  Deleting them removes a relative
\(o(1)\).  On the remainder, (2.3) and Theorem 6.2 give

\[
 \boxed{
 \mathscr L_{H,2}
 \ge {B_{r_p}\over H}
 \exp[-(3\log4+o(1))p].}
\tag{7.7}
\]

Thus bounded reduced degree occurs in actual long-period Pascal-saddle
cores.  What fails is critical total mass.

### 7.3 The collar penalty is intrinsic to this family

The first-pruned core in (6.9) has a deterministic collar of semilength

\[
 a=3p-3
\]

and exactly two collar peaks.  If its full rank and peak count are
\((d,k)\), the arbitrary filler core \(G\) has parameters

\[
 (d-a,k-2).
\]

Let

\[
 \operatorname {Nar}(d,k)
 ={1\over d}\binom dk\binom d{k-1}
\]

be the Narayana number.  The complete rank-\(r_p\) Pascal mass of all
cores carrying this collar is

\[
 \mathscr W_p
 =\sum_{d,k}
 \operatorname {Nar}(d-a,k-2)
 \binom{r_p+d-k}{2d}.
\tag{7.8}
\]

In the saddle tube \(d/r_p\to1/2\), \(k/r_p\to1/6\), direct division of
the four binomial coefficients gives, uniformly for
\(p=\Theta(\sqrt{r_p})\),

\[
 \begin{aligned}
 \log{\operatorname {Nar}(d-a,k-2)
       \over\operatorname {Nar}(d,k)}
 &=2a\log\left(1-{k\over d}\right)+o(p)\\
 &=-\bigl(6\log(3/2)+o(1)\bigr)p.
 \end{aligned}
\tag{7.9}
\]

The \(k\mapsto k-2\) shift contributes only \(O(1)\) to the logarithm,
and the accumulated falling-factorial error is
\(O(a^2/r_p)=O(1)=o(p)\).  Outside the saddle tube the total Pascal mass
is \(B_{r_p}e^{-\Omega(r_p)}\).  Comparing (7.8) cell by cell with the
complete Narayana--Pascal decomposition of \(B_{r_p}\) yields

\[
 \boxed{
 \mathscr W_p
 \le B_{r_p}
 \exp[-(6\log(3/2)+o(1))p].}
\tag{7.10}
\]

Since \(p=\Theta(\sqrt{r_p})\), this is \(o(B_{r_p}/H)\).
Therefore even granting every possible filler core and its complete
rank-\(r_p\) inverse Pascal fibre cannot make this deterministic-collar
mechanism critical.

## 8. Updated decision

The reduced phase degree has now been evaluated on the strongest known
phase-isolated family:

\[
 \boxed{\Delta_H(E)\le2}
\]

on actual long-period Pascal-saddle cores, with exact weighted mass

\[
 {B_m\over H}e^{-\Theta(\sqrt m)}.
\]

This proves that neither saddle location, long reduced period, minimum
return, nor terminal phase isolation forces divergent reduced clustering.
It also proves, through (7.10), that the known deterministic collar cannot
be amplified into the critical bounded-degree obstruction required by
(5.2).

The global alternatives remain:

\[
 \mathscr L_{H,K}=\Omega(B_m/H)
\quad\text{for some fixed }K,
\]

which refutes \(ST_A\), or

\[
 \mathscr L_{H,K}=o(B_m/H)
\quad\text{for every fixed }K,
\]

which is the necessary reduced-degree divergence law.  Any further
bounded-degree construction must remove the
\(\exp[-6\log(3/2)\,p]\) first-pruned collar penalty, not merely enlarge
the inverse Pascal fibre above the same collar.

Finally, the physical normalization in the task is the same gate.  Every
quotient start has \(N\) spatial lifts, and

\[
 {N B_m\over H}
 =\left({2\over A}+o(1)\right)B_m\sqrt m.
\]

Thus a quotient obstruction \(\Omega(B_m/H)\) is exactly a physical
obstruction \(\Omega(B_m\sqrt m)\) to
\(\nu_{A\sqrt m}=o(B_m\sqrt m)\).  The calibrated collar family reaches
only

\[
 B_m\sqrt m\,e^{-\Theta(\sqrt m)}
\]

physical intervals, so it does not decide the requested asymptotic.
