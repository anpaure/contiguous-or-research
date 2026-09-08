# The \(\rho/z\) pair recurrence and the exact restoring-compensator dual

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

This note makes two corrections to the stochastic priority-nibble lane.

First, the density of surviving resources and the density of surviving
fixed decorations are different quantities.  Write them as

\[
 z_t\qquad\hbox{and}\qquad \rho_t.
\]

The pair-square recurrence does **not** require
\(\rho_t=z_t^{k-1}\).  It only requires the one-anchor degree reference
to be \(\rho_t\) and the two-anchor link reference to be

\[
 \boxed{\ell_t={\rho_t\over z_t}.}
 \tag{0.1}
\]

Thus, if

\[
 q_t={z_{t+1}\over z_t},\qquad
 a_t={\rho_{t+1}\over\rho_t},\qquad
 b_t={\ell_{t+1}\over\ell_t}={a_t\over q_t},
 \tag{0.2}
\]

then

\[
 {b_t^2\over a_t^2}=q_t^{-2}.
 \tag{0.3}
\]

Consequently the desired \(z_t^{-2}\) pair-square inflation remains
algebraically exact even when \(\rho_t\) is as small as \(z_t^K\),
**provided the absolute reference degrees \(\rho_tD_0(F)\) still tend
to infinity on the tracked fibres**.  The normalization cannot revive
an extinct support catalogue.  What is missing is
the theorem that the actual conditioned link means follow
\(\rho_t/z_t\); monotonicity alone does not imply it.

Second, the existence of a sampling law with the required restoring
degree drift, link drift, and second-moment budget has an exact finite
convex dual.  At a residual state, let \(\Omega\) be the finite set of
legal next outcomes and let \(c(\omega)\) be the vector of all degree,
link, and variance impacts of outcome \(\omega\).  For any polytope
\(\Pi\) of admissible probability laws on \(\Omega\), the target impact
vector \(b\) is attainable to coordinatewise error \(\delta\) if and
only if

\[
 \boxed{
 \langle w,b\rangle
 \le
 \max_{\pi\in\Pi}\sum_{\omega\in\Omega}
       \pi_\omega\langle w,c(\omega)\rangle
 +\delta\|w\|_1
 \quad\hbox{for every real }w.}
 \tag{0.4}
\]

This is the exact residual multirank Hall condition for a compensator.
It is not supplied by raw regularity or by the pair-square estimate.
It also explains why defining a self-correcting compensator does not
prove that a legal sampler realizes it.

Together, (0.1)--(0.4) give a noncircular sufficient lemma: prove the
dual cuts (0.4), including the conditioned second-moment coordinates,
and the global stopped martingale plus the recurrence below propagate
all protected fibres through \(z=1/\log m\).  The dual cuts themselves
remain unproved for the physical catalogue, so no coefficient-one
conclusion is claimed.

## 1. A fully asymmetric pair-square recurrence

Let \({\cal X}\) and \({\cal Y}\) be two tracked resource strata.  At
time \(t\), write

\[
 D_t(x)=\#\{P:x\in P\},\qquad
 C_t(x,y)=\#\{P:x,y\in P\}.
 \tag{1.1}
\]

Fix positive reference degree densities \(\rho_{x,t}\),
\(\rho_{y,t}\), and a positive resource density \(z_t\).  Put

\[
 a_{x,t}={\rho_{x,t+1}\over\rho_{x,t}},\qquad
 a_{y,t}={\rho_{y,t+1}\over\rho_{y,t}},\qquad
 q_t={z_{t+1}\over z_t}.
 \tag{1.2}
\]

Here \(x\) is fixed, while \(\rho_{y,t}\) and \(a_{y,t}\) are common
reference values for the whole stratum \({\cal Y}\); pointwise degree
deviations of its members are absorbed in \(e_t\).  A version with
varying references follows by retaining the ratios inside the sum and
taking their uniform upper bounds.

A sufficient symmetric two-anchor reference is

\[
 \ell_{xy,t}={\sqrt{\rho_{x,t}\rho_{y,t}}\over z_t}.
 \tag{1.3}
\]

Its one-step contraction is

\[
 b_{xy,t}
 ={\ell_{xy,t+1}\over\ell_{xy,t}}
 ={\sqrt{a_{x,t}a_{y,t}}\over q_t}.
 \tag{1.4}
\]

Define the anchored pair-square block

\[
 S_t(x)=\sum_{y\in{\cal Y}}
 {C_t(x,y)^2\over D_t(x)D_t(y)}.
 \tag{1.5}
\]

As in the earlier survival-conditioned recurrence, let
\({\cal A}_{xy}\) be the event that the bite does not directly consume
either anchor.  Direct-consumption jumps are terminal successes and are
not part of the residual variance process.

### Theorem 1.1 (reference-density pair recurrence)

Suppose, outside a separately charged exceptional family, that

\[
 D_{t+1}(x)\ge(1-e_t)a_{x,t}D_t(x),\qquad
 D_{t+1}(y)\ge(1-e_t)a_{y,t}D_t(y),
 \tag{1.6}
\]

and that, under \({\cal A}_{xy}\),

\[
 \left|\mathbb E C_{t+1}(x,y)-b_{xy,t}C_t(x,y)\right|
 \le e_tb_{xy,t}C_t(x,y).
 \tag{1.7}
\]

Assume also the conditioned variance bound

\[
 \sum_y{
 \operatorname {Var}(C_{t+1}(x,y)\mid{\cal F}_t,{\cal A}_{xy})
 \over D_t(x)D_t(y)}
 \le
 \varepsilon_t b_{xy,t}^2 S_t(x)+b_{xy,t}^2E_t(x),
 \tag{1.8}
\]

where in (1.8) a common value of \(b_{xy,t}\) may be replaced by its
uniform upper and lower approximations with the corresponding
\(1+o(1)\) error.  Then

\[
 \boxed{
 \mathbb E S_{t+1}(x)
 \le q_t^{-2}\bigl(1+O(e_t+\varepsilon_t)\bigr)S_t(x)
 +q_t^{-2}(1+O(e_t))E_t(x).}
 \tag{1.9}
\]

#### Proof

The degree lower bounds give

\[
 S_{t+1}(x)
 \le{(1-e_t)^{-2}\over a_{x,t}a_{y,t}}
 \sum_y{C_{t+1}(x,y)^2\over D_t(x)D_t(y)}.
 \tag{1.10}
\]

For every \(y\), conditional second-moment decomposition and (1.7)
give

\[
 \mathbb E C_{t+1}(x,y)^2
 \le(1+O(e_t))b_{xy,t}^2C_t(x,y)^2
 +\operatorname {Var}C_{t+1}(x,y).
 \tag{1.11}
\]

Insert (1.8) into (1.10)--(1.11).  By (1.4),

\[
 {b_{xy,t}^2\over a_{x,t}a_{y,t}}=q_t^{-2}.
 \tag{1.12}
\]

Finally \((1-e_t)^{-2}=1+O(e_t)\), proving (1.9).
\(\square\)

The common-stratum specialization is

\[
 \rho_{x,t}=\rho_{y,t}=\rho_t,qquad
 \ell_t={\rho_t\over z_t},qquad
 b_t={a_t\over q_t}.
 \tag{1.13}
\]

Notice that no identity between \(\rho_t\) and \(z_t\) was used.

Exact equality in (1.4) is not necessary.  The proof uses only the
quotient bound

\[
 {b_{xy,t}^2\over a_{x,t}a_{y,t}}
 \le q_t^{-2}(1+\zeta_t).
 \tag{1.14}
\]

Under (1.14), the right side of (1.9) acquires the additional relative
error \(O(\zeta_t)\).  Hence a summable Palm distortion
\(\sum_t\zeta_t=o(1)\) is as good as the exact reference
\(\sqrt{\rho_x\rho_y}/z\).  Equivalently, if the actual two-anchor
reference is

\[
 \ell_{xy,t}
 =\vartheta_{xy,t}{\sqrt{\rho_{x,t}\rho_{y,t}}\over z_t},
 \tag{1.15}
\]

it is enough that

\[
 \sum_t\left|\log{\vartheta_{xy,t+1}\over
                         \vartheta_{xy,t}}\right|=o(1).
 \tag{1.16}
\]

This slowly varying form is the strongest version needed by the global
iteration.

## 2. Why this is stronger than the independent-survival formula

For a fixed \(k\)-resource decoration under independent resource
survival,

\[
 \rho_t=z_t^{k-1},\qquad
 {\rho_t\over z_t}=z_t^{k-2}.
 \tag{2.1}
\]

Thus (1.13) reduces to the familiar formula

\[
 a_t=q_t^{k-1},\qquad b_t=q_t^{k-2}.
 \tag{2.2}
\]

In the actual priority catalogue, however, owner and deadline
conditioning can make the surviving decoration density \(\rho_t\)
very different from \(z_t^{k-1}\).  Formula (1.13) says exactly what
must replace independence:

> after conditioning on both anchors surviving, removing the second
> anchor from the feasibility constraints raises the surviving
> decoration density by the factor \(1/z_t\).

This is a two-anchor Palm identity.  It is a theorem to prove, not a
consequence of codegree monotonicity.  Monotonicity yields only
\(C_{t+1}\le C_t\); inserted into (1.10), this gives inflation
\((a_{x,t}a_{y,t})^{-1}\), which may be exponentially larger than
\(q_t^{-2}\).

There is, however, an exact aggregate identity which forces the
\(\rho/z\) scale before any probabilistic argument.

### Proposition 2.1 (exact link row sum)

Let \({\cal Y}_t\) be a current resource stratum.  Suppose every current
catalogue decoration containing a fixed anchor \(x\) contains exactly
\(s\) resources from \({\cal Y}_t\) (excluding \(x\) itself when the
two strata coincide).  Then

\[
 \boxed{
 \sum_{y\in{\cal Y}_t}C_t(x,y)=sD_t(x).}
 \tag{2.3}
\]

If initially \(|{\cal Y}_0|=N_Y\), currently
\(|{\cal Y}_t|=z_{Y,t}N_Y\), and
\(D_t(x)=\rho_{x,t}D_0(x)\), then

\[
 \boxed{
 { |{\cal Y}_t|^{-1}\sum_{y\in{\cal Y}_t}C_t(x,y)
  \over
   N_Y^{-1}\sum_{y\in{\cal Y}_0}C_0(x,y)}
 ={\rho_{x,t}\over z_{Y,t}}.}
 \tag{2.4}
\]

#### Proof

Count ordered pairs \((P,y)\) where \(P\) is a current decoration
containing \(x\) and \(y\) is one of its \(s\) resources in
\({\cal Y}_t\).  Counting first by \(P\) gives \(sD_t(x)\); counting
first by \(y\) gives the left side of (2.3).  Divide (2.3) at time
\(t\) by the same identity at time zero to obtain (2.4).
\(\square\)

For a common stratum with \(z_{Y,t}=z_t\) and
\(\rho_{x,t}=\rho_t\), Proposition 2.1 proves the average link
reference \(\rho_t/z_t\) **exactly in every residual catalogue**.
Thus the remaining first-moment issue is not its scalar value.  It is
the assertion that the current tilted sampling law contracts each
weighted link row, or all but an exceptional part of it, close to this
forced row average.  The second-moment issue is dispersion around that
average.  These are precisely the signed and nonnegative cut families
in Theorem 4.2 below.

The row sum also separates an automatically harmless term from the
genuine pair-square obstruction.

### Proposition 2.2 (only centered link dispersion is dangerous)

In the setting of Proposition 2.1, put

\[
 n_t=|{\cal Y}_t|,qquad
 \overline C_t(x)={sD_t(x)\over n_t}.
 \tag{2.5}
\]

Suppose all retained \(y\in{\cal Y}_t\) satisfy

\[
 D_t(y)\ge(1-e_t)\overline D_{Y,t}.
 \tag{2.6}
\]

Then

\[
 \boxed{
 S_t(x)
 \le {1+O(e_t)\over D_t(x)\overline D_{Y,t}}
 \left[
   {s^2D_t(x)^2\over n_t}
   +\sum_{y\in{\cal Y}_t}
      (C_t(x,y)-\overline C_t(x))^2
 \right].}
 \tag{2.7}
\]

If

\[
 D_t(x)=\rho_{X,t}D_0(x)(1+o(1)),\qquad
 \overline D_{Y,t}=\rho_{Y,t}\overline D_{Y,0}(1+o(1)),
 \qquad n_t=z_{Y,t}N_Y,
 \tag{2.8}
\]

then the first term in (2.7), relative to its time-zero value, is

\[
 (1+o(1)){\rho_{X,t}\over\rho_{Y,t}}z_{Y,t}^{-1}.
 \tag{2.9}
\]

In particular, when \(\rho_{X,t}/\rho_{Y,t}=1+o(1)\), this is only
\(z_t^{-1}\), smaller than the permitted \(z_t^{-2}\) inflation.

#### Proof

By (2.6),

\[
 S_t(x)
 \le{1+O(e_t)\over D_t(x)\overline D_{Y,t}}
       \sum_y C_t(x,y)^2.
 \tag{2.10}
\]

The exact row sum (2.3) says that the arithmetic mean of the link row
is \(\overline C_t(x)\).  Hence the orthogonal decomposition

\[
 \sum_yC_t(x,y)^2
 ={s^2D_t(x)^2\over n_t}
 +\sum_y(C_t(x,y)-\overline C_t(x))^2
 \tag{2.11}
\]

proves (2.7).  Substituting (2.8) into the first term proves (2.9).
\(\square\)

Therefore the sampler need not prescribe every link mean separately.
Once the degree corridor is known, (2.3) fixes the row mean.  A sharper
and lower-dimensional compensator problem asks only for

1. restoring degree means; and
2. an upper bound on the centered row energy in (2.7).

This replaces exponentially many signed individual-link constraints
by degree equalities and nonnegative centered-variance cuts.  It does
not prove those variance cuts, but it removes a redundant part of the
remaining LP gate.

## 3. Iteration with two independent reference densities

Let

\[
 R_t(x)=z_t^2S_t(x)/B
 \tag{3.1}
\]

for an initial block bound \(S_0(x)\le B\).  Theorem 1.1 gives

\[
 \mathbb E R_{t+1}(x)
 \le(1+O(e_t+\varepsilon_t))R_t(x)
 +(1+O(e_t)){z_t^2E_t(x)\over B}.
 \tag{3.2}
\]

Therefore

\[
 \sum_te_t=o(1),\qquad
 \sum_t\varepsilon_t=o(1),\qquad
 \sum_t{z_t^2E_t(x)\over B}=o(1)
 \tag{3.3}
\]

imply

\[
 \boxed{\mathbb E S_t(x)\le(1+o(1))z_t^{-2}B.}
 \tag{3.4}
\]

Again, \(\rho_t\) cancels from the normalized ratio.  It may be tiny
relative to one, but the absolute-degree abundance condition remains
necessary.  The substantive input is
the relative one-anchor/two-anchor calibration (1.3), not a lower bound
on \(\rho_t\).

## 4. The exact sampler polytope

Fix a residual state.  Let \(\Omega\) be a finite family of legal next
outcomes.  An outcome can mean one accepted decorated edge, or an
entire legal parallel bite including all conflict resolutions.  Using
the latter convention keeps every formula below exact.

Let \({\cal J}\) be any finite index set of observables.  It may contain

1. protected degree fibres \(F\);
2. protected links \((F,G)\);
3. aggregate second-moment blocks \((F,h)\);
4. tag-usage and resource-usage constraints.

For \(j\in{\cal J}\) and \(\omega\in\Omega\), let \(c_j(\omega)\) be
the exact impact of outcome \(\omega\) on observable \(j\).  Examples
are

\[
 c_F(\omega)=1-{D^\omega(F)\over D(F)},
 \tag{4.1}
\]

\[
 c_{FG}(\omega)=1-{C^\omega(F,G)\over C(F,G)},
 \tag{4.2}
\]

and, for a prescribed link contraction \(b_{FG}\),

\[
 c^{(2)}_{F,h}(\omega)
 =\sum_{G\in h}{
  (C^\omega(F,G)-b_{FG}C(F,G))^2
 \over D(F)D(G)}.
 \tag{4.3}
\]

The expectation of every coordinate in (4.1)--(4.3) is linear in the
law of \(\omega\).  In particular, (4.3) encodes the full bias-plus-
variance quantity required by the fresh-branching bound; it is not only
a first-moment proxy.

Let \(\Pi\subseteq\mathbb R^\Omega\) be a nonempty compact polytope of
admissible laws.  Thus

\[
 \pi_\omega\ge0,\qquad \sum_\omega\pi_\omega=1,
 \tag{4.4}
\]

together with any desired linear tag marginals, activation rates, or
symmetry constraints.  Define the attainable impact polytope

\[
 {\cal K}=\left\{
 \sum_{\omega\in\Omega}\pi_\omega c(\omega):\pi\in\Pi
 \right\}\subseteq\mathbb R^{\cal J}.
 \tag{4.5}
\]

### Theorem 4.1 (exact approximate-compensator dual)

For a target vector \(b\in\mathbb R^{\cal J}\) and \(\delta\ge0\), the
following are equivalent:

1. there is \(v\in{\cal K}\) with
   \(\|v-b\|_\infty\le\delta\);
2. for every real vector \(w\in\mathbb R^{\cal J}\),

\[
 \boxed{
 \langle w,b\rangle
 \le
 \max_{\pi\in\Pi}
 \sum_{\omega\in\Omega}\pi_\omega
       \langle w,c(\omega)\rangle
 +\delta\|w\|_1.}
 \tag{4.6}
\]

#### Proof

Condition 1 says exactly

\[
 b\in{\cal K}+\delta B_\infty,
 \tag{4.7}
\]

where \(B_\infty\) is the unit cube.  The support function of the
right side is

\[
 h_{{\cal K}+\delta B_\infty}(w)
 =h_{\cal K}(w)+\delta\|w\|_1.
 \tag{4.8}
\]

Moreover

\[
 h_{\cal K}(w)
 =\max_{\pi\in\Pi}\sum_\omega
       \pi_\omega\langle w,c(\omega)\rangle.
 \tag{4.9}
\]

A point belongs to a compact convex set if and only if every linear
functional at that point is at most the support function of the set.
Equations (4.7)--(4.9) prove the equivalence. \(\square\)

Because \(w\) ranges over both signs, (4.6) contains both upper and
lower inequalities.  It also detects every exact invariant: if
\(\langle w,c(\omega)\rangle\) is constant over all legal outcomes,
then the target must have the same \(w\)-coordinate up to the allowed
error.

The fresh-branching variance coordinate is naturally an upper bound,
not an equality.  The exact mixed version is as follows.

### Theorem 4.2 (equalities together with variance upper bounds)

Partition the observable coordinates as

\[
 {\cal J}={\cal E}\sqcup{\cal U},
 \tag{4.10}
\]

where \({\cal E}\) contains the degree and link means, and
\({\cal U}\) contains second-moment costs.  Fix equality targets
\(b\in\mathbb R^{\cal E}\), tolerances
\(\delta\in\mathbb R_+^{\cal E}\), and upper budgets
\(u\in\mathbb R^{\cal U}\).  There is \(v\in{\cal K}\) such that

\[
 |v_j-b_j|\le\delta_j\quad(j\in{\cal E}),
 \qquad
 v_j\le u_j\quad(j\in{\cal U})
 \tag{4.11}
\]

if and only if, for every
\(w_{\cal E}\in\mathbb R^{\cal E}\) and every
\(w_{\cal U}\in\mathbb R_+^{\cal U}\),

\[
 \boxed{
 \min_{\pi\in\Pi}\sum_{\omega}\pi_\omega
 \langle w,c(\omega)\rangle
 \le
 \langle w_{\cal E},b\rangle
 +\sum_{j\in{\cal E}}\delta_j|w_j|
 +\langle w_{\cal U},u\rangle.}
 \tag{4.12}
\]

#### Proof

Let

\[
 {\cal C}
 =\{x:|x_j-b_j|\le\delta_j\ (j\in{\cal E}),
        \ x_j\le u_j\ (j\in{\cal U})\}.
 \tag{4.13}
\]

The desired statement is \({\cal K}\cap{\cal C}\ne\varnothing\).
If these two convex sets are disjoint, strong separation (one set is
compact) gives a vector \(w\) for which

\[
 \inf_{x\in{\cal K}}\langle w,x\rangle
 >\sup_{x\in{\cal C}}\langle w,x\rangle.
 \tag{4.14}
\]

The supremum on the right is finite exactly when
\(w_{\cal U}\ge0\), and in that case it equals

\[
 \langle w_{\cal E},b\rangle
 +\sum_{j\in{\cal E}}\delta_j|w_j|
 +\langle w_{\cal U},u\rangle.
 \tag{4.15}
\]

Thus a separating vector exists exactly when (4.12) fails. \(\square\)

This is the sharp form needed later: signed dual tests govern the
restoring means, while only nonnegative tests are allowed on the
variance-cost coordinates.

### Product-tag specialization

Suppose one chooses independently, for each tag \(U\), an edge from a
distribution \(p_U\) after activation with a fixed rate \(\alpha_U\),
and suppose impacts are additive before conflict resolution.  Then the
first-order attainable set is the Minkowski sum

\[
 {\cal K}_{\rm lin}
 =\sum_U\alpha_U\operatorname {conv}
   \{c_U(e):e\in E_U\}.
 \tag{4.16}
\]

Its exact dual is

\[
 \boxed{
 \langle w,b\rangle
 \le
 \sum_U\alpha_U
 \max_{e\in E_U}\langle w,c_U(e)\rangle
 +\delta\|w\|_1
 \quad(w\in\mathbb R^{\cal J}).}
 \tag{4.17}
\]

For a real parallel bite, conflict resolution makes the total impact
nonadditive.  Then (4.16)--(4.17) are only a linearization.  The exact
object is the full-outcome polytope (4.5)--(4.6).  This distinction is
necessary: independence is a nonconvex restriction on the law of full
outcomes, whereas arbitrary randomized legal outcomes form a simplex.

## 5. The restoring degree drift

For a degree fibre \(F\) in stratum \(r\), let

\[
 X_t(F)=\log{D_t(F)\over\rho_{r,t}D_0(F)}.
 \tag{5.1}
\]

Put

\[
 \kappa_{r,t}=-\log{\rho_{r,t+1}\over\rho_{r,t}}.
 \tag{5.2}
\]

If the exact fractional loss in one step is

\[
 I_{t,F}=1-{D_{t+1}(F)\over D_t(F)},
 \tag{5.3}
\]

then, before direct consumption,

\[
 X_{t+1}(F)-X_t(F)
 =\log(1-I_{t,F})+\kappa_{r,t}.
 \tag{5.4}
\]

Choose the desired expected loss

\[
 b_{t,F}
 =\kappa_{r,t}+\gamma_tX_t(F)\Delta t.
 \tag{5.5}
\]

If (4.6) supplies a legal law with

\[
 |\mathbb E I_{t,F}-b_{t,F}|\le\delta_t\Delta t,
 \tag{5.6}
\]

then Taylor expansion yields

\[
 \boxed{
 \mathbb E[\Delta X_t(F)\mid{\cal F}_t]
 =-\gamma_tX_t(F)\Delta t
 +O\bigl(\delta_t\Delta t+mathbb EI_{t,F}^2\bigr).}
 \tag{5.7}
\]

Thus the desired compensator really is restoring: high-degree fibres
are sampled slightly more and low-degree fibres slightly less.  But
(5.5) is only a target vector.  Its realizability is **equivalent** to
the signed residual cuts (4.6).  Merely defining (5.5) supplies no
sampling law.

The same construction may include the link target

\[
 \mathbb E{C_{t+1}(F,G)\over C_t(F,G)}
 ={\sqrt{a_{F,t}a_{G,t}}\over q_t}+o(1),
 \tag{5.8}
\]

and the block second-moment budget (4.3) in the same index set
\({\cal J}\).  Hence one convex feasibility problem governs both scalar
degree restoration and the \(\rho/z\) pair recurrence.

## 6. A noncircular sufficient lemma

The following packages exactly what would close the stochastic lane.

### Compensated Palm-feasibility lemma (open)

Through the stopping time \(z_t\ge1/\log m\), suppose that every
nonexceptional residual state admits a legal outcome law satisfying:

1. the dual inequalities (4.6) for the restoring degree target (5.5),
   with \(\sum_t\delta_t\Delta t=o(1)\);
2. the conditioned link target (5.8), equivalently the reference
   \(\sqrt{\rho_{F,t}\rho_{G,t}}/z_t\), with summable relative error;
3. the block second-moment target (4.3) with total normalized error
   as in (3.3);
4. total weighted predictable quadratic variation \(o(W)\) in the
   global stopped martingale ledger;
5. total weight of states/fibres for which the preceding cuts fail is
   \(o(W)\).

Then all nonexceptional degree fibres remain within multiplicative
\(1+o(1)\) of their reference trajectories, and every protected
pair-square block satisfies

\[
 S_t(x)\le(1+o(1))z_t^{-2}B.
 \tag{6.1}
\]

Consequently the previously audited cover/remainder Schur ledger has
total physical target defect \(o(W)\) through \(z=1/\log m\).

#### Justification

Items 1 and 4, inserted into (5.7), give the global stopped restoring
degree corridor.  Items 2 and 3 give Theorem 1.1; its iteration is
(3.4).  Item 5 charges every discarded object directly.  The existing
cover/remainder calculation then converts (6.1) into \(o(W)\) physical
defect.  No step identifies \(z_t\) with \(\rho_t\), and no compensator
is assumed feasible merely because it has been written down.

By Propositions 2.1--2.2, items 2 and 3 may be replaced by the weaker
single requirement that the centered link-row energy in (2.7) obey the
corresponding conditioned upper-budget cuts.  The row mean is then
forced by incidence counting and does not require separate signed link
constraints.

## 7. Exact remaining cut problem

The mathematical bottleneck can now be stated without stochastic
terminology.  At every dense residual catalogue and every real signed
weighting \(w\) of

* degree fibres,
* two-anchor links, and
* pair-square blocks,

prove

\[
 \langle w,b_t\rangle
 \le
 \max_{\pi\in\Pi_t}\mathbb E_{\omega\sim\pi}
       \langle w,c_t(\omega)\rangle
 +o(\Delta t)\|w\|_1,
 \tag{7.1}
\]

where \(b_t\) contains (5.5), (5.8), and the fresh-branching
second-moment allowance.

Equation (7.1) is a support-feasible, survival-conditioned,
multirank Hall theorem.  It is stronger than raw degree regularity and
different from the outer-slice collision inequality: the latter bounds
the cost of a given law, while (7.1) proves that a law with the required
signed corrections exists.

The useful narrowing is exact:

\[
 \boxed{
 \text{resource/edge density mismatch is harmless once }
 \ell_t=\rho_t/z_t;
 \quad
 \text{the unresolved issue is the dual feasibility of that Palm law.}}
 \]
