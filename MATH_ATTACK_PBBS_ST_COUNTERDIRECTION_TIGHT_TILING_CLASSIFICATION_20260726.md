# The \(ST_A\) counterdirection: exact tight-return and reciprocal-trace equality

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, web
input, or long-running job is used.

## 0. Outcome

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H_A=\lceil A\sqrt m\rceil.
\]

The open quotient form of the PBBS short-residence gate is

\[
 \overline\nu_{H_A}=o_A(B_m/\sqrt m).
 \tag{QST_A}
\]

The proved reciprocal-height trace gives only

\[
 \overline\nu_{H_A}
 \le
 \sum_{h\le H_A-1}\frac{b_{m,h}}{h+2}
 =
 O_A(B_m/\sqrt m),                                 \tag{0.1}
\]

where \(b_{m,h}\) is the number of semilength-\(m\) Dyck roots of height
\(h\).

No genuine family attaining the right order in (0.1) is constructed here.
The report instead proves the exact equality classification which any
counterfamily must approach.

1. A minimum-gap return of a height-\(h\) root has gap \(2h+1\). In the
   equality-particle PBBS, its leading particle must first be selected
   again at time \(2h-1\), exactly two steps before the parent return.
   The final selected particle is its immediate predecessor, and the
   number of earlier predecessor selections is exactly the initial
   physical spacing. These conditions are also sufficient.

2. Iterating the preceding statement under simultaneous peak deletion
   gives an exact **leader--predecessor closure tower** down to the first
   mountain core. Thus equality in the height-gap theorem is not merely
   the statement that every pruned root has the right height; it includes
   one exact selection-time and one exact physical-spacing equation at
   every pruning level.

3. In one height stratum the reciprocal trace has the exact slack identity

   \[
   \boxed{
   b_{m,h}-(h+2)|\mathcal P_h|
   =
   \bigl(b_{m,h}-|U_h|\bigr)
   +
   \sum_{I\in\mathcal P_h}\bigl(|I|-(h+2)\bigr),}
                                                               \tag{0.2}
   \]

   where \(U_h\) is the union of the selected quotient-edge intervals.
   Equality holds if and only if every interval has minimum length
   \(h+2\) and the intervals tile every quotient edge of the stratum.
   Cycle by cycle, the starts are then one residue class modulo \(h+2\),
   and every used quotient-cycle length is divisible by \(h+2\).

4. In the coefficient-critical one-defect terminal rotor, a complete tight
   tiling has the additional necessary arithmetic condition

   \[
    2p+3\mid2q+1,
   \]

   where \(p\) is the first-mountain depth and \(q=h-p\). This excludes
   exact tiling on every other one-defect profile, but still does not
   exclude positive-density partial packing.

The known complete gap-seven family satisfies the tight-return
classification, but its quotient packing is only \(\Theta(2^m)\), whereas
the critical target is \(\Theta(4^m/m^2)\). Hence it is exponentially
subcritical. The genuine counterdirection is now precise: construct
Gaussian-height PBBS cycles carrying a positive edge-density of
leader--predecessor closure towers, or prove that their utilization tends
to zero. Marginal height equality alone does neither.

## 1. Equality-particle coordinates

Let \(D\) be a nonempty Dyck root of semilength \(m\), and let

\[
 E=\partial D
\]

be its simultaneous peak deletion. Label the equality particles of
Theorem 14.1 of
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md in cyclic order. Let

\[
 \kappa_t
\]

be the equality particle selected at one-step PBBS time \(t\), and let
\(x_j(t)\) be the physical edge occupied by particle \(j\). Choose integer
lifts preserving their cyclic order during the time interval under
consideration. The exact skew recursion is

\[
 \boxed{
 x_{\kappa_t}(t+1)=x_{\kappa_t}(t)+1,\qquad
 x_j(t+1)=x_j(t)\ (j\ne\kappa_t),\qquad
 \lambda_t=x_{\kappa_t}(t)+1.}                    \tag{1.1}
\]

Suppose \(\kappa_0=a\), and let \(a^-\) be its immediate cyclic
predecessor. Put

\[
 r_a=\min\{t>0:\kappa_t=a\},                       \tag{1.2}
\]

\[
 \Delta_a=x_a(0)-x_{a^-}(0)>0,                    \tag{1.3}
\]

and

\[
 M_{a^-}(g)=
 \#\{0\le t<g:\kappa_t=a^-\}.                     \tag{1.4}
\]

Choose the adjacent cyclic lifts so that \(1\le\Delta_a<N\). The integer
\(\Delta_a\) is the initial number of one-edge particle moves needed to
bring the predecessor to the initial position of \(a\).

## 2. Exact leader--predecessor return criterion

### Theorem 2.1 (one-level exact criterion)

Assume \(g<N\). The physical omitted label has a consecutive return

\[
 \lambda_0=\lambda_g,\qquad
 \lambda_t\ne\lambda_0\quad(0<t<g),                \tag{2.1}
\]

if and only if

\[
 \boxed{
 r_a<g,\qquad
 \kappa_g=a^-,
 \qquad
 M_{a^-}(g)=\Delta_a.}                             \tag{2.2}
\]

For a return satisfying (2.1), \(r_a\) is itself a consecutive
omitted-label return gap in the compressed PBBS on \(E=\partial D\).

#### Proof

At time zero, (1.1) gives

\[
 \lambda_0=x_a(0)+1.
\]

After that update, particle \(a\) occupies the returned physical edge.
It must be selected again before any other particle can enter that edge,
which proves \(r_a<g\).

Particles never overtake. Since \(g<N\), the next particle that can enter
the vacated edge is the immediate predecessor \(a^-\); a full lap by
particle \(a\) is impossible. Hence a consecutive return forces

\[
 \kappa_g=a^-.
\]

Before the update at time \(g\), recursion (1.1) gives

\[
 x_{a^-}(g)
 =
 x_{a^-}(0)+M_{a^-}(g).
\]

Thus

\[
 \lambda_g=\lambda_0
 \quad\Longleftrightarrow\quad
 x_{a^-}(0)+M_{a^-}(g)=x_a(0)
 \quad\Longleftrightarrow\quad
 M_{a^-}(g)=\Delta_a.                              \tag{2.3}
\]

The congruence has no second lift: both
\(M_{a^-}(g)\) and \(\Delta_a\) lie in \([0,N)\), because \(g<N\).
This proves necessity.

Conversely assume (2.2). Particle \(a\) vacates the returned edge at
time \(r_a<g\). Before time \(g\), the predecessor has made fewer than
\(\Delta_a\) moves at each of its earlier selection times, so it has not
yet entered that edge. No particle farther behind can overtake it, and
particles ahead cannot move backwards. At time \(g\), (2.3) gives
\(\lambda_g=\lambda_0\). Therefore the return is consecutive.

Finally, the definition of \(r_a\) says exactly that the compressed
omitted-label word selects \(a\) at times \(0,r_a\) and not in between.
Thus \(r_a\) is a consecutive compressed return gap. \(\square\)

### Theorem 2.2 (classification of height-gap equality)

Let \(D\) have height \(h\ge2\). Then \(D\) starts a consecutive return
of the minimum possible gap

\[
 g=2h+1<N                                             \tag{2.4}
\]

if and only if, in its equality-particle PBBS,

\[
 \boxed{
 r_a=2h-1,\qquad
 \kappa_{2h+1}=a^-,
 \qquad
 M_{a^-}(2h+1)=\Delta_a.}                          \tag{2.5}
\]

In particular, \(\partial D\) starts a consecutive return of gap
\(2h-1\), which is again the minimum allowed by its height \(h-1\).

#### Proof

Suppose first that \(D\) has the return (2.4). By Theorem 2.1,
\(r_a<g\). Both gaps are odd, so

\[
 r_a\le g-2=2h-1.                                  \tag{2.6}
\]

Peak deletion lowers height by exactly one:

\[
 \operatorname {ht}(\partial D)=h-1.
\]

Apply the height-gap theorem to the compressed consecutive return
\(r_a\). It gives

\[
 r_a\ge2(h-1)+1=2h-1.                              \tag{2.7}
\]

Equations (2.6)--(2.7) force \(r_a=2h-1\). The remaining two equations
in (2.5) are Theorem 2.1.

Conversely, (2.5) is exactly criterion (2.2) with \(g=2h+1\), so
Theorem 2.1 supplies the parent return. Its gap equals the height-gap
lower bound and is therefore minimum. \(\square\)

This theorem separates two facts which were conflated in the retracted
primitive-height converse. The compressed leader may return at the correct
time while the predecessor closure equation fails. Both parts of (2.5)
are needed.

## 3. The full tight-return tower

Put

\[
 D^{(j)}=\partial^jD,\qquad h_j=h-j,
\]

and stop at the first level \(p\) at which the semilength of \(D^{(p)}\)
equals its height. Then

\[
 D^{(p)}=M_{h-p}=1^{h-p}0^{h-p}.                  \tag{3.1}
\]

For \(0\le j<p\), let

\[
 \kappa_t^{[j]},\quad a_j,\quad a_j^-,
 \quad\Delta_j,\quad M_j(\cdot)
\]

be the equality-particle data (1.2)--(1.4) of the parent
\(D^{(j)}\). Thus \(\kappa^{[j]}\) is the omitted-label word of the
compressed root \(D^{(j+1)}\).

### Corollary 3.1 (recursive equality classification)

A nonwrapping height-\(h\) return is tight if and only if, at every
\(0\le j<p\),

\[
 \boxed{
 \begin{aligned}
 \min\{t>0:\kappa_t^{[j]}=a_j\}
   &=2(h-j)-1,\\
 \kappa_{2(h-j)+1}^{[j]}
   &=a_j^-,\\
 M_j(2(h-j)+1)&=\Delta_j,
 \end{aligned}}                                    \tag{3.2}
\]

and the bottom mountain supplies the terminal full-wrap return.

#### Proof

Apply Theorem 2.2 at level \(j\). Its first equation says that the
compressed root \(D^{(j+1)}\) has the next tight return, so induction
continues until the first mountain. Conversely, begin with the mountain
return and apply the sufficient direction of Theorem 2.2 successively
from level \(p-1\) back to level zero. \(\square\)

The indexing in (3.2) deliberately keeps the selected-particle word on
the compressed root \(D^{(j+1)}\): those particles are the equality
particles of the parent level \(j\).
The equations include the physical inverse-slot spacing \(\Delta_j\), not
only the sequence of pruned Dyck roots. This is the datum absent from a
height-only equality statement.

## 4. Exact equality in the reciprocal-height trace

Fix a height \(h\), and let \(\Omega_{m,h}\) be the directed quotient-edge
set of all height-\(h\) Dyck roots. Since \(\tau\) preserves height,

\[
 |\Omega_{m,h}|=b_{m,h}.                           \tag{4.1}
\]

Let \(\mathcal P_h\) be any pairwise quotient-edge-disjoint family of
nonwrapping residence intervals in this stratum, and let \(|I|\) denote
the number of quotient edges in the interval, including its two boundary
edges. The height-gap theorem gives

\[
 |I|\ge h+2.                                       \tag{4.2}
\]

Put

\[
 U_h=\bigcup_{I\in\mathcal P_h}I.
\]

### Theorem 4.1 (exact reciprocal-trace slack identity)

\[
 \boxed{
 b_{m,h}-(h+2)|\mathcal P_h|
 =
 \bigl(b_{m,h}-|U_h|\bigr)
 +
 \sum_{I\in\mathcal P_h}\bigl(|I|-(h+2)\bigr).}   \tag{4.3}
\]

Both terms on the right are nonnegative. Consequently equality in

\[
 |\mathcal P_h|\le\frac{b_{m,h}}{h+2}              \tag{4.4}
\]

holds if and only if:

1. every selected interval has \(|I|=h+2\), equivalently its
   omitted-label gap is \(2h+1\); and
2. the selected intervals cover every edge of \(\Omega_{m,h}\).

On each quotient cycle met by such an equality family, the cycle length
is divisible by \(h+2\), and the selected starts form one residue class
modulo \(h+2\).

#### Proof

The intervals are edge-disjoint, so

\[
 |U_h|=\sum_{I\in\mathcal P_h}|I|.
\]

Substitute this equality into the right side of (4.3); the terms telescope
to the left side. Nonnegativity follows from (4.1)--(4.2).

Equality holds exactly when both right-side terms vanish. This gives
conditions 1--2. A cyclic sequence tiled by consecutive intervals of one
common length \(h+2\) has length divisible by \(h+2\), and successive
starts differ by exactly \(h+2\). \(\square\)

Combining Theorems 2.2 and 4.1 gives the promised equality
classification: every tile start carries the complete recursive
leader--predecessor closure tower (3.2).

### Corollary 4.2 (quantitative near-equality)

Suppose

\[
 |\mathcal P_h|
 \ge(1-\varepsilon)\frac{b_{m,h}}{h+2},
 \qquad0<\varepsilon<1.                            \tag{4.5}
\]

Then

\[
 b_{m,h}-|U_h|\le\varepsilon b_{m,h},              \tag{4.6}
\]

\[
 \sum_{I\in\mathcal P_h}\bigl(|I|-(h+2)\bigr)
 \le\varepsilon b_{m,h}.                           \tag{4.7}
\]

For every \(\eta>0\), the fraction of selected intervals satisfying

\[
 |I|\ge h+2+\eta h
\]

is at most

\[
 \boxed{
 \frac{\varepsilon(h+2)}
      {\eta h(1-\varepsilon)}.}                    \tag{4.8}
\]

#### Proof

The left side of (4.3) is at most \(\varepsilon b_{m,h}\). Since its two
right-side terms are nonnegative, each is at most that quantity, proving
(4.6)--(4.7).

Each interval counted in (4.8) contributes at least \(\eta h\) to (4.7).
Divide the resulting count bound by the lower bound (4.5) for
\(|\mathcal P_h|\). \(\square\)

Thus near-full reciprocal saturation forces almost all covered edge mass
into near-minimum returns. A mere positive constant fraction of capacity
does not force exact equality, but it still occupies a positive fraction
of the height-stratum edge measure.

### Corollary 4.3 (one-defect terminal-rotor divisibility)

Consider one height-\(s\) quotient cycle on which the invariant pruning
profile has first mountain depth \(p\ge1\). Put

\[
 q=s-p,
 \qquad K=2q+1,
 \qquad b=K-p.
 \tag{4.9}
\]

Assume that the terminal curvature is one. Equivalently, immediately
above the stopping mountain \(M_q\), the inverse fibre is the unit-vector
rotor on \(K\) slots. If this whole top quotient cycle is tiled by tight
return supports, then

\[
 \boxed{2p+3\mid 2q+1.}                           \tag{4.10}
\]

In particular, every one-defect cycle for which (4.10) fails has strictly
positive uncovered-edge defect in (4.3).

#### Proof

Peak deletion commutes with \(\tau\). On the unit-vector terminal fibre,
\(\tau\) rotates the positive slot by one position, so the projected
terminal cycle has exact length \(K\); consequently \(K\) divides the
length of the top quotient cycle.

The tight Pascal fan at first-mountain depth \(p\) requires a cyclic block
of \(p\) consecutive terminal slots to be zero. For a unit vector, the
admissible anchors are therefore exactly one cyclic interval of
\(K-p=b\) residues; its complement is a cyclic interval of \(p\)
forbidden residues.

By Theorem 4.1, consecutive tile starts on the top cycle differ by exactly

\[
 L=s+2=p+q+2                                      \tag{4.11}
\]

quotient phases. Their terminal anchors consequently run through a full
coset of the subgroup generated by \(L\) in \(\mathbb Z_K\). If

\[
 d=\gcd(K,L),
\]

that coset has cyclic spacing \(d\). Since every tile start is admissible,
the forbidden interval of \(p\) consecutive residues contains no point of
the coset. Hence

\[
 d\ge p+1.                                        \tag{4.12}
\]

On the other hand,

\[
 d\mid 2L-K=2p+3.                                 \tag{4.13}
\]

Every proper divisor of \(2p+3\) is at most
\((2p+3)/2<p+2\). The only integer in the range allowed by (4.12) is then
\(p+1\), but \(2p+3=2(p+1)+1\), so \(p+1\nmid2p+3\). Thus

\[
 d=2p+3.
\]

Since \(d\mid K=2q+1\), equation (4.10) follows. If (4.10) fails, a
complete tight tiling is impossible, and Theorem 4.1 leaves at least one
uncovered edge on the cycle. \(\square\)

The corollary is an exact obstruction to *full* reciprocal equality, not
to critical-order partial packing. One uncovered edge per long quotient
cycle can be negligible, and the admissible terminal interval itself has
positive density \(b/K\) in the critical regime. Thus (4.10) does not
silently supply the little-oh required by \((QST_A)\).

## 5. Consequences for a putative \(ST_A\) counterfamily

Define the reciprocal capacity

\[
 R_{m,A}
 =
 \sum_{h\le H_A-1}\frac{b_{m,h}}{h+2}.             \tag{5.1}
\]

The exact Dyck height spectrum gives

\[
 R_{m,A}=\Theta_A(B_m/\sqrt m)                     \tag{5.2}
\]

for every fixed \(A>0\), with a positive constant depending on \(A\).
Here is the lower bound, since positivity of the constant matters for the
counterdirection. Let \(F_m(t)\) count Dyck paths of height at most \(t\).
Then

\[
 R_{m,A}
 \ge
 \frac1{H_A+1}\sum_{h\le H_A-1}b_{m,h}
 =
 \frac{F_m(H_A-1)}{H_A+1}.                        \tag{5.2a}
\]

The positive spectral expansion

\[
 F_m(t)
 =
 \frac2{t+2}\sum_{j=1}^{t+1}
 \sin^2\!\frac{\pi j}{t+2}
 \left(2\cos\frac{\pi j}{t+2}\right)^{2m}
\]

allows us to retain its \(j=1\) term. With \(t=H_A-1\), elementary
\(\sin x\ge2x/\pi\) and \(\log\cos x\ge-Cx^2\) estimates give

\[
 F_m(H_A-1)
 \ge c_A\,4^m m^{-3/2}
 \ge c_A'B_m.                                      \tag{5.2b}
\]

Substitution in (5.2a) proves the required
\(\Omega_A(B_m/\sqrt m)\) bound. The reciprocal-height trace estimate
(0.1) supplies the matching upper bound.

For a packing \(\mathcal P\), put

\[
 u_{m,h}
 =
 \frac{(h+2)|\mathcal P_h|}{b_{m,h}}\in[0,1].
 \tag{5.3}
\]

Then

\[
 |\mathcal P|
 =
 \sum_{h\le H_A-1}
 u_{m,h}\frac{b_{m,h}}{h+2}.                      \tag{5.4}
\]

Therefore

\[
 |\mathcal P|=\Theta_A(B_m/\sqrt m)                \tag{5.5}
\]

is equivalent to a positive weighted-average utilization of the
reciprocal capacity:

\[
 \frac{\sum_hu_{m,h}b_{m,h}/(h+2)}
      {\sum_hb_{m,h}/(h+2)}
 \ge c_A>0                                         \tag{5.6}
\]

along a subsequence.

An exact upper-constant saturator would, by Theorem 4.1, tile almost every
relevant height-stratum edge with the tight towers (3.2). A
constant-order counterfamily need only have positive utilization, but it
must still place actual return intervals on a positive fraction of the
critical edge measure. The formal inverse-profile and mountain-fibre
models do not do this: they supply capacity objects or candidate cycles,
not canonical PBBS intervals.

## 6. The known tight family is exponentially subcritical

The complete gap-seven classification gives

\[
 R_7(m)=2^{m-1}-m
\]

actual quotient starts of height three and minimum gap seven. Greedy
selection on the long quotient cycles gives a quotient-edge-disjoint
family of order \(2^m\). However

\[
 \frac{2^m}{B_m/\sqrt m}
 =
 \Theta\!\left(\frac{m^2}{2^m}\right)
 \longrightarrow0.                                \tag{6.1}
\]

Every fixed-height tight family is likewise exponentially subcritical by
the bounded-height spectral estimate. Hence a genuine counterfamily must
have heights tending to infinity, and the reciprocal mass calculation
forces its relevant heights onto the \(\sqrt m\) scale.

The explicit critical atom

\[
 D_{n,M}
 =
 1^{3n+1}0^n1^{2n-1}0^{4n-1}(10)^M0
\]

is a genuine Gaussian-height zero-winding tight return, but its rotations
and parameter choices are sub-Catalan in aggregate. It proves local
nonemptiness of (3.2), not positive utilization in (5.6).

## 7. Exact boundary

Proved here:

1. the one-level necessary-and-sufficient leader--predecessor criterion
   (2.2);
2. the recursive classification (3.2) of every height-gap equality
   return;
3. the exact two-slack identity (4.3);
4. cycle-by-cycle tiling and divisibility in the equality case;
5. quantitative stability of near-full reciprocal saturation;
6. the terminal-rotor divisibility obstruction (4.10) for exact tilings.

Not proved:

1. a genuine family with quotient packing
   \(\Theta_A(B_m/\sqrt m)\);
2. a proof that every canonical PBBS family has utilization \(o_A(1)\);
3. \((QST_A)\), \((ST_A)\), or the coefficient-one theorem.

The counterdirection is therefore genuinely exhausted at the current
structural level. A saturating construction must realize the closure
equations (3.2) on a positive fraction of Gaussian-height quotient edge
mass. A strict upper bound must prove that this simultaneous realization
has vanishing utilization. Neither conclusion follows from rotational
stabilizers, terminal mountain fibres, additive Pascal-fan volumes, or
the Dyck height spectrum alone.
