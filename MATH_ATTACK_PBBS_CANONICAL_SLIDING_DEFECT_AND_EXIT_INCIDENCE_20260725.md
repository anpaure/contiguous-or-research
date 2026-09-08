# Canonical PBBS cross-phase attack: the sliding defect and exit incidence

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

The proposed joint-saturation theorem in
`MATH_ATTACK_PBBS_CRITICAL_PROFILE_BOUNDARY_JOINT_SATURATION_20260725.md`
is retracted. Its fixed-word bound was only an upper bound, its profile
objects were capacity-envelope tuples rather than canonical towers, and
its fresh cycles had no fibrewise parent-clone supply.

This note attacks the surviving problem entirely inside the canonical
PBBS chronology. No endpoint word is assigned, no inverse tuple is
declared realizable, and no cycle is generated.

Put

\[
 N=2m+1,\qquad B_m=\operatorname{Cat}_m,
 \qquad \tau=\phi^2.
\]

For one canonical one-step orbit define

\[
 a_t=\delta(\phi^tD),\qquad
 c_t=d(\phi^tD).
\]

The first result is an exact cross-phase coordinate.

### Theorem A (canonical sliding defect)

For a fixed height/duration $s$, put

\[
 \mathscr R_s(x)
 :=\sum_{t=0}^{2s}a_{2x+t}-sN.
 \tag{0.1}
\]

Then a phase $x$ is a zero-winding duration-$s$ start exactly when

\[
 \mathscr R_s(x)=0.
 \tag{0.2}
\]

Moreover

\[
 \boxed{
 \mathscr R_s(x+1)-\mathscr R_s(x)
 =c_{2x}-c_{2x+2s+1}.}
 \tag{0.3}
\]

At a genuine zero-winding start, $c_{2x}=1$. Hence the next quotient
phase is again a duration-$s$ zero-winding start if and only if

\[
 c_{2x+2s+1}=1.
 \tag{0.4}
\]

If the run stops, its last start satisfies the exact canonical exit
condition

\[
 \boxed{
 \mathscr R_s(x)=0,\qquad c_{2x}=1,qquad
 c_{2x+2s+1}\ge3.}
 \tag{0.5}
\]

Thus the residual common-base problem is not a free intersection of
transported sets. It is a two-time incidence of two literal first-deficit
statistics on the same $\phi$-orbit.

### Theorem B (legal rarity--length reduction)

Restrict to the critical band

\[
 \varepsilon\sqrt m\le s\le A\sqrt m
 \tag{0.6}
\]

and to long quotient cycles. Let $Z_m$ be the total number of genuine
zero-winding starts in the band, let $Z_m^0$ be the number with endpoint
excess zero, and let $X_m^+$ be the number of positive-excess exits (0.5).
Every quotient-edge-disjoint positive-excess family satisfies

\[
 \boxed{
 |\mathcal P^+|
 \le \frac{2Z_m}{\varepsilon\sqrt m}+X_m^++Z_m^0+o(B_m/\sqrt m).}
 \tag{0.7}
\]

The already proved start-density theorem gives $Z_m=o_A(B_m)$, while the
solved zero-excess sector gives $Z_m^0=O_A(B_m/m)$. Consequently

\[
 \boxed{
 X_m^+=o_A(B_m/\sqrt m)
 \quad\Longrightarrow\quad
 |\mathcal P^+|=o_A(B_m/\sqrt m).}
 \tag{0.8}
\]

This is a valid use of start rarity and interval length: the division by
$s$ occurs only inside literal consecutive runs of starts on one actual
PBBS cycle. No independent marginal estimates are multiplied.

The new exact remaining theorem is therefore

\[
 \boxed{
 \sum_{\varepsilon\sqrt m\le s\le A\sqrt m}
 \#\{D:\operatorname{ht}(D)=s,
       \ \mathscr R_s(D)=0,
       \ \Lambda(D)>0,
       \ d(\phi\tau^sD)\ge3\}
 =o_A(B_m/\sqrt m),}
 \tag{0.9}
\]

after restricting to the critical profiles.

The note also derives the exact capacity series for $L$ consecutive
canonical starts. It has an additional factor asymptotic to $2^{-(L-1)}$,
not a vanishing factor depending on $m$ for fixed $L$. Thus local
consecutive-phase smoothing cannot close (0.9); the missing estimate is a
genuinely separated two-time incidence.

Coefficient one is not proved.

## 1. One-step voltages and deficits

For a Dyck root $E$, use its canonical first-highest-component
factorization

\[
 E=P1R0S
\]

and put

\[
 \delta(E)=|P|+1,\qquad d(E)=|S|+1.
\]

Along a one-step quotient orbit let

\[
 E_t=\phi^tD,qquad a_t=\delta(E_t),qquad c_t=d(E_t).
 \tag{1.1}
\]

The three positive canonical block lengths at phase $t$ are

\[
 a_t,\qquad a_{t+1},\qquad c_t,
\]

and sum to $N$. Therefore

\[
 \boxed{c_t=N-a_t-a_{t+1}.}
 \tag{1.2}
\]

Every $c_t$ is a positive odd integer.

At quotient phase $x$, the step-two state is

\[
 D_x=E_{2x}=\tau^xD.
\]

Its forward and dual step-two deficits are respectively

\[
 d(D_x)=c_{2x},\qquad e(D_x)=c_{2x+1}.
 \tag{1.3}
\]

The second equality also follows from the local staircase identity

\[
 \delta(D_x)+d(D_x)-\delta(D_{x+1})=e(D_x).
\]

## 2. Proof of the sliding-defect theorem

The exact zero-winding orbit-sum identity says that a duration-$s$ start
at phase $x$ obeys

\[
 \sum_{t=0}^{2s}a_{2x+t}=sN.
 \tag{2.1}
\]

This proves (0.2). In the fixed Gaussian band the corresponding gap
$2s+1$ is below the physical circumference, so the equality case of the
height-gap theorem makes the hit first and consecutive whenever the state
has height $s$.

Sliding the window by two one-step phases gives

\[
 \begin{aligned}
 \mathscr R_s(x+1)-\mathscr R_s(x)
 &=-a_{2x}-a_{2x+1}
   +a_{2x+2s+1}+a_{2x+2s+2}\\
 &=c_{2x}-c_{2x+2s+1},
 \end{aligned}
 \tag{2.2}
\]

where (1.2) is used in the second line. This proves (0.3).

For a genuine zero-winding equality, the initial terminal suffix is
empty. Hence

\[
 c_{2x}=d(D_x)=1.
 \tag{2.3}
\]

Equations (2.2)--(2.3) show

\[
 \mathscr R_s(x+1)=0
 \quad\Longleftrightarrow\quad
 c_{2x+2s+1}=1.
 \tag{2.4}
\]

If equality fails, positivity and oddness of $c_{2x+2s+1}$ give
$c_{2x+2s+1}\ge3$. This proves (0.4)--(0.5).

There is also an exact separated two-start identity. If phases $x$ and
$x+h$ both start duration-$s$ zero-winding returns, subtracting their two
orbit-sum equations gives

\[
 \boxed{
 \sum_{t=0}^{2h-1}a_{2x+t}
 =\sum_{t=2s+1}^{2s+2h}a_{2x+t}.}
 \tag{2.5}
\]

This is the literal canonical cross-phase constraint that a saturating
packing must obey at every separation $h\ge s$.

## 3. Endpoint excess is an exact deficit resource

For a zero-winding start at phase $x$, define

\[
 \Lambda_x
 =a_{2x}+a_{2x+2s}-(N-1).
 \tag{3.1}
\]

This is the usual endpoint excess. Sum (1.2) over the $2s$ one-step
edges of the return window. Since (2.1) holds,

\[
 \begin{aligned}
 \sum_{t=0}^{2s-1}c_{2x+t}
 &=2sN-\left(
 a_{2x}+a_{2x+2s}
 +2\sum_{t=1}^{2s-1}a_{2x+t}\right)\\
 &=a_{2x}+a_{2x+2s}\\
 &=N-1+\Lambda_x.
 \end{aligned}
 \tag{3.2}
\]

Thus positive endpoint overlap is not an independent decoration: it is
the excess of the actual one-step deficit mass carried by the return.

Let $\mathcal P$ be a quotient-edge-disjoint zero-winding family. A
step-two edge $D\to\tau D$ owns the two one-step deficits
$d(D)$ and $d(\phi D)$. Distinct selected quotient edges give distinct
one-step edges on both parities. Therefore

\[
 \boxed{
 \sum_{I\in\mathcal P}(N-1+\Lambda_I)
 \le2\sum_{D\in\mathcal D_m}d(D).}
 \tag{3.3}
\]

The exact deficit-moment theorem gives

\[
 \sum_{D\in\mathcal D_m}d(D)
 =\Theta(\sqrt m\,B_m).
 \tag{3.4}
\]

Consequently (3.3) recovers only

\[
 |\mathcal P|=O(B_m/\sqrt m).
 \tag{3.5}
\]

This is coefficient-one critical. It is nevertheless useful as an audit:
even the exact joint endpoint/trace resource, with no marginal product,
does not supply the missing little-oh.

## 4. Zero runs and the proof of Theorem B

Fix one actual long $\tau$-cycle and one height $s$. Let

\[
 \mathcal Z_s
 =\{x:\mathscr R_s(x)=0\}
 \tag{4.1}
\]

be its zero-winding start set. Decompose $\mathcal Z_s$ into maximal
cyclic runs of consecutive quotient phases.

If a run has length $\ell$, any two starts in the run whose return
intervals are edge-disjoint differ by at least $s$ phases. Hence that run
contributes at most

\[
 \left\lceil\frac\ell s\right\rceil
 \le\frac\ell s+1
 \tag{4.2}
\]

selected intervals.

Every proper run has one last phase $x$. By Theorem A, that phase obeys
the exit condition (0.5). If the whole cycle is one run and its length is
greater than $2s$, its packing is at most twice its number of starts
divided by $s$. Cycles of length at most $2s$ have total state mass
$\exp(o(m))$ by the audited voltage-itinerary bound and are negligible at
the Catalan scale.

It follows, after summing over the long cycles, that

\[
 |\mathcal P_s|
 \le\frac{2|\mathcal Z_s|}{s}+X_s,
 \tag{4.3}
\]

where $X_s$ is the number of run exits.

Now retain only positive endpoint excess. Removing a zero-excess start
from a cyclic run creates at most one additional positive run. Therefore

\[
 |\mathcal P_s^+|
 \le\frac{2|\mathcal Z_s|}{s}+X_s^++Z_s^0
 +\exp(o(m)),
 \tag{4.4}
\]

where $X_s^+$ counts exits whose last positive start has
$\Lambda>0$, and $Z_s^0$ counts zero-excess starts. Sum (4.4) over the
critical band (0.6). Different $s$ count disjoint starts because a
zero-winding duration equals the height of the root. Thus

\[
 \sum_s\frac{|\mathcal Z_s|}{s}
 \le\frac{Z_m}{\varepsilon\sqrt m}.
\]

This proves (0.7). The known estimates for $Z_m$ and $Z_m^0$ then prove
(0.8).

The reduction is genuinely chronological. It does not infer a
$1/s$ factor from global rarity; it extracts that factor from the geometry
of one actual consecutive run before summing over roots.

## 5. Exact envelope for several consecutive canonical starts

This section audits whether long zero runs could themselves supply the
missing gain.

Suppose $L=k+1$ consecutive top phases start genuine tight zero-winding
returns with the same height $s$ and first-mountain depth $p$. At inverse
level $j$, the union of their triangular fans fixes

\[
 j+k
 \tag{5.1}
\]

consecutive child-slot variables to prescribed nonnegative values. In the
unsaturated profile one has

\[
 (2r_j+1)-j\ge b,
 \tag{5.2}
\]

so these variables are distinct whenever $0\le k<b$.

As usual, the compatible count is maximized when all prescribed values
are zero. For profile curvatures $y_j$ the resulting envelope is

\[
 \prod_{j=1}^p
 \binom{y_j+2r_j-j-k}{y_j}.
 \tag{5.3}
\]

Let $\mathscr F^{[k]}_{s,p}(z)$ be the sum of (5.3) over all convex
profiles with $y_p\ge1$ and $\sum jy_j=m-s$.

### Theorem 5.1 (multi-anchor collapse)

For $0\le k<b$,

\[
 \boxed{
 \mathscr F^{[k]}_{s,p}(z)
 =\frac{C_p(z)^{b-k}}{Q_p(z)^3}
 \left[1-\left(1-\frac{z^p}{Q_p(z)^2}\right)^{b-k}\right].}
 \tag{5.4}
\]

#### Proof

Put

\[
 b_j=2s-3j+1,
 \qquad
 t_j=z^j\prod_{i<j}(1-t_i)^{-2(j-i)}.
\]

Summing the $y_j$ in increasing order now gives

\[
 \prod_{j=1}^p(1-t_j)^{-(b_j-k)}.
 \tag{5.5}
\]

The continuant identities give

\[
 t_j=\frac{z^j}{Q_j(z)^2},\qquad
 1-t_j=\frac{Q_{j-1}(z)Q_{j+1}(z)}{Q_j(z)^2}.
\]

The interior powers telescope exactly as in the one-anchor calculation.
Equivalently,

\[
 \prod_{j=1}^p(1-t_j)^k=C_p(z)^{-k}.
 \tag{5.6}
\]

Finally, restricting the last $y_p$ sum to $y_p\ge1$ replaces its full
factor by the same factor minus one. This proves (5.4). $\square$

At the critical point, with

\[
 x=(p+1)^{-2},\qquad
 \alpha=\frac{p+1}{p+2},
\]

equation (5.4) gives

\[
 4^{-s}\mathscr F^{[k]}_{s,p}(1/4)
 =\frac{2^{1-k}}{(p+1)^3}
   \alpha^{b-k}
   \left[1-(1-x)^{b-k}\right].
 \tag{5.7}
\]

If $p\le b\le2p$ and $0\le k\le b/2$, then

\[
 \boxed{
 4^{-s}\mathscr F^{[k]}_{s,p}(1/4)
 \le C2^{-k}p^{-4}.}
 \tag{5.8}
\]

The same two-pole tilt used for the one-anchor series remains uniform:
$b-k\asymp p$, the independent $1/Q_{p-1}$ factor is unchanged, and
the partition ratio between $1/4$ and
$z_p=\tfrac14(1+\kappa p^{-2})$ is bounded. More explicitly, Fourier
inversion of that $1/Q_{p-1}$ factor gives largest tilted atom
$O(p^{-2})$. The logarithmic mean of the remaining positive factors is
$O(p^2+kp)=O(p^2)$, so a relative tilt of order $p^{-2}$ changes their
partition function by only $e^{O(1)}$. Finally

\[
 \left(\frac{z_p}{1/4}\right)^{-(m-s)}
 \le e^{-cm/p^2}
\]

after reducing the fixed tilt constant. Combining this with (5.8) gives,
in the critical coefficient window $m\asymp p^2$,

\[
 [z^{m-s}]\mathscr F^{[k]}_{s,p}(z)
 \le C_A2^{-k}4^m p^{-6}e^{-cm/p^2}.
 \tag{5.9}
\]

Summing the critical cells yields

\[
 \boxed{
 \#\{\text{actual critical starts beginning at least }k+1
       \text{ consecutive starts}\}
 \le C_A2^{-k}\frac{4^m}{m^2}.}
 \tag{5.10}
\]

Equation (5.10) is an upper bound because every actual consecutive run
supplies the slot union (5.1); no envelope tuple is declared realizable.

The factor $2^{-k}$ shows that very long consecutive runs are negligible.
It does not make the packing little-oh: the capacity envelope is
consistent with runs of bounded mean length, in which case the number of
exits is of the same order as the number of starts. Thus the true residual
is (0.9), not long-run mass.

## 6. The exact remaining canonical incidence theorem

Define, for one actual state $D$ of height $s$,

\[
 \mathcal X_s^+
 =\left\{D:
 \begin{array}{l}
 \sum_{t=0}^{2s}\delta(\phi^tD)=sN,\\
 \delta(D)+\delta(\tau^sD)>N-1,\\
 d(D)=1,\\
 d(\phi\tau^sD)\ge3
 \end{array}\right\}.
 \tag{6.1}
\]

Every condition in (6.1) is determined by the single canonical
$\phi$-orbit of $D$. There is no freely chosen boundary word, phase set,
or ambient cycle.

The first line is zero winding; the second is positive endpoint overlap;
the last two say that this start is the last member of its consecutive
zero run. Theorem B reduces the critical packing gate to

\[
 \boxed{
 \sum_{\varepsilon\sqrt m\le s\le A\sqrt m}
 |\mathcal X_s^+|
 =o_A(4^m/m^2).}
 \tag{6.2}
\]

For two separated members of a prospective packing, equation (2.5) is an
additional exact block-sum equality. Therefore a direct route to (6.2) is
a fixed-profile two-time estimate for

\[
 \left(
 \sum_{t=0}^{2s}a_t,
 \ a_0+a_{2s},
 \ c_0,
 \ c_{2s+1}
 \right),
 \tag{6.3}
\]

retaining the canonical relation $c_t=N-a_t-a_{t+1}$ and the pruning
profile. A marginal law for any one entry of (6.3) is insufficient.

The terminal one-defect mountain rotor has one exit per rotor cycle and
endpoint excess zero. Hence it is removed by the proved zero-excess
estimate. Every member of (6.1) is created strictly above that rotor. This
locates the remaining positive-boundary theorem at the first upper level
where the canonical exit $c_{2s+1}\ge3$ is created.

## 7. Adversarial audit

1. **Retraction honored.** No upper bound is used as lower supply.

2. **Actual orbit data only.** Equations (0.1), (0.3), (2.5), (3.2), and
   (6.1) use the canonical $\phi$-orbit of an actual Dyck root.

3. **No free cycles.** Packing is bounded on the existing quotient
   cycles by decomposing their actual zero sets into runs.

4. **No invalid rarity--length product.** Division by $s$ occurs only in
   (4.2), inside one literal run of consecutive starts.

5. **Envelope used in the correct direction.** The multi-anchor series
   (5.4) is only an upper bound for actual runs.

6. **Endpoint coupling is exact.** Equation (3.2) counts the same
   one-step deficits carried by the return; it is not a product of an
   endpoint marginal and a trace marginal.

7. **Scope.** The exit estimate (6.2) is not proved. Consequently neither
   the critical PBBS packing little-oh nor coefficient one is claimed.

## 8. Final status

The false joint-saturation theorem has been retracted. The actual
canonical cross-phase problem now has a smaller exact form: count positive
zero-winding starts for which the sliding defect leaves zero at the next
quotient phase, equivalently

\[
 d(D)=1,\qquad d(\phi\tau^sD)\ge3.
\]

All starts inside long zero plateaux legally contribute only their total
mass divided by $s$; the known $o(B_m)$ start theorem disposes of them at
the required scale. The only unresolved mass is the set of canonical
positive-boundary exits (6.1). Long consecutive runs have the exact
$2^{-k}$ envelope penalty and are not the obstruction.

Thus the next theorem is no longer a generic profile--boundary coupling
or an arbitrary transported-set intersection. It is the fixed-profile,
two-time exit incidence (6.2), together with the separated block-sum
identity (2.5).
