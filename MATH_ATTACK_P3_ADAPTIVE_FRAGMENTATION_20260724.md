# Third-wave lane P: adaptive profile release and recomputed fragmentation

Date: 2026-07-24

## 0. Verdict

This report proves a genuinely adaptive exact-factor theorem after the
fixed-word and subgroup-aggregation no-go.

Let a coordinate forest grow by fresh bridges

\[
 e_1,\ldots,e_{n-1},
 \qquad
 G_t=\langle e_1,\ldots,e_t\rangle.
\]

Between successive fresh bridges one may perform arbitrary finite legal
component switches using already exposed coordinates, recomputing the
ownership components after every switch.  If \(F_t\) is the exact factor
at the end of stage \(t\), then every \(G_t\)-orbit total of every
lower-rank load is exactly the same in \(F_t\) as in \(F_0\).  Consequently
the current quadratic and overload profile releases

\[
 \Delta_t^Q
 =
 \mathfrak B_{H,G_{t-1}}(F_{t-1})
 -
 \mathfrak B_{H,G_t}(F_t),
\]

\[
 \Delta_t^O
 =
 \Omega_{H,G_{t-1}}(F_{t-1})
 -
 \Omega_{H,G_t}(F_t)
\]

are nonnegative and telescope pathwise:

\[
 \boxed{
 \sum_{t=1}^{n-1}\Delta_t^Q=\mathcal Q_H(F_0),
 \qquad
 \sum_{t=1}^{n-1}\Delta_t^O=\mathcal O_H(F_0).
 }
 \tag{0.1}
\]

This remains true when the fresh edge and all component choices are
selected predictably from the preceding exact-factor history.

There is a second exact telescope.  Put

\[
 X_t^Q
 =
 \mathcal Q_H(F_t)-\mathfrak B_{H,G_t}(F_t).
\]

If the net energy decrease during stage \(t\) is

\[
 \Gamma_t=\mathcal Q_H(F_{t-1})-\mathcal Q_H(F_t),
\]

then

\[
 \boxed{
 X_t^Q-X_{t-1}^Q=\Delta_t^Q-\Gamma_t.
 }
 \tag{0.2}
\]

Thus a released profile floor has only two destinations: actual energy
decrease or new excess above the coarser orbit floor.  At a global
minimizer, every released unit must be restored as excess.

For one freshly recomputed transposition cube, this report also proves an
exact best-child formula.  If \(d_K\) are the multidepth component effects,

\[
 A_\tau=\left\|\sum_Kd_K\right\|_H^2,
 \qquad
 V_\tau=\sum_K\|d_K\|_H^2,
\]

\[
 \rho_\tau
 =
 \min_{\varepsilon_K\in\{\pm1\}}
 \left\|\sum_K\varepsilon_Kd_K\right\|_H^2,
\]

then the fair and optimal legal decreases are exactly

\[
 \boxed{
 \Gamma_\tau^{\mathrm{fair}}
 =\frac{A_\tau-V_\tau}{4},
 \qquad
 \Gamma_\tau^*
 =\frac{A_\tau-\rho_\tau}{4}.
 }
 \tag{0.3}
\]

Hence a fresh bridge captures an \(\eta\)-fraction of its subgroup-profile
release \(\Delta_\tau\) if and only if

\[
 \boxed{
 \rho_\tau\le A_\tau-4\eta\Delta_\tau.
 }
 \tag{0.4}
\]

This is an exact signed-Gram cut condition on the recomputed components.

The adaptive telescope does not prove (0.4).  In fact the route has two
independent missing gates:

1. **exposure:** a single bridge must see a positive share of the relaxed
   floor released by merging two coordinate components; and
2. **fragmentation:** the bridge effect must split among recomputed owner
   components with a productive common multidepth sign cut.

Two explicit profile models isolate the failures.  The exposure gate does
not follow from orbit totals, nonnegativity, and integrality alone.  The
fragmentation gate does not follow even after adding zero total and zero
point margins to the centered signed discrepancy.  These models are not
exact-wreath counterexamples, and the first does not have zero point
margins.  No exact factor is proved to violate the desired adaptive
theorem.

The strongest valid conclusion is therefore conditional but sharp.  If,
for fixed \(A\), a recomputed adaptive forest policy captures a fixed
fraction \(\eta_A>0\) of the releases up to total error
\(O_A(H_A\operatorname{Cat}_m)\), then every global fixed-window minimizer
has

\[
 \mathcal Q_{H_A}
 =
 O_A(H_A\operatorname{Cat}_m)
 =
 O_A(W/\sqrt m)
 =
 o(W).
\]

This proves the required fixed-window unlabelled balancing statement and
then MWB by the audited diagonalization.  The fixed-fraction
productive-release assertion itself remains unproved.

No web search, finite search, or computational search is used below.

## 1. Exact energies and orbit floors

Let

\[
 n=2m+1.
\]

Fix a depth window \(0\le q\le H\).  At depth \(q\), let
\(\mu_q(F)\) be the integral target-load vector of an exact middle wreath
factor \(F\).  Write

\[
 W=c_qN_q+\delta_q,
 \qquad
 0\le\delta_q<N_q.
\]

Use the floor-corrected quadratic and balanced overload

\[
 Q_q(F)
 =
 \sum_S
 (\mu_q(S)-c_q)(\mu_q(S)-c_q-1),
 \tag{1.1}
\]

\[
 O_q(F)
 =
 \frac12
 \min_{\substack{b(S)\in\{c_q,c_q+1\}\\
                  \sum_Sb(S)=W}}
 \|\mu_q-b\|_1.
 \tag{1.2}
\]

Their weighted fixed-window sums are

\[
 \mathcal Q_H(F)
 =
 \sum_{q\le H}\frac{Q_q(F)}{c_q},
 \qquad
 \mathcal O_H(F)
 =
 \sum_{q\le H}\frac{O_q(F)}{c_q}.
 \tag{1.3}
\]

Indeed, put

\[
 L_q=\sum_S(c_q-\mu_q(S))_+,
 \qquad
 U_q=\sum_S(\mu_q(S)-c_q-1)_+.
\]

The exact balanced-overload formula is
\(O_q=\max(L_q,U_q)\).  For an integer \(z\), the scalar floor polynomial
is zero at \(c_q,c_q+1\), is at least twice the deficit below \(c_q\), and
is at least twice the excess above \(c_q+1\).  Hence

\[
 Q_q\ge2(L_q+U_q)\ge2O_q.
\]

After weighting and summing, this gives

\[
 \boxed{\mathcal Q_H(F)\ge2\mathcal O_H(F).}
 \tag{1.4}
\]

For a transposition-generated coordinate subgroup \(G\), let
\(\mathfrak B_{q,G}(F)\) be the exact minimum of \(Q_q\) among integral
load vectors having the same \(G\)-orbit totals as \(F\).  Let
\(\Omega_{q,G}(F)\) be the analogous exact minimum balanced overload after
only the \(G\)-orbit totals are retained.  Put

\[
 \mathfrak B_{H,G}(F)
 =
 \sum_{q\le H}\frac{\mathfrak B_{q,G}(F)}{c_q},
 \qquad
 \Omega_{H,G}(F)
 =
 \sum_{q\le H}\frac{\Omega_{q,G}(F)}{c_q}.
 \tag{1.5}
\]

The audited orbit-floor theorems give

\[
 \mathcal Q_H(F)\ge\mathfrak B_{H,G}(F)\ge0,
 \qquad
 \mathcal O_H(F)\ge\Omega_{H,G}(F)\ge0.
 \tag{1.6}
\]

If \(G\le G'\), then \(G'\)-orbits are unions of \(G\)-orbits, so constraints
are removed and

\[
 \mathfrak B_{H,G'}(F)\le\mathfrak B_{H,G}(F),
 \qquad
 \Omega_{H,G'}(F)\le\Omega_{H,G}(F).
 \tag{1.7}
\]

For the trivial group, every orbit is a singleton:

\[
 \mathfrak B_{H,\{1\}}(F)=\mathcal Q_H(F),
 \qquad
 \Omega_{H,\{1\}}(F)=\mathcal O_H(F).
 \tag{1.8}
\]

For \(G=S_n\), there is one orbit on every rank and the total \(W\) lies
between the two global quotas, so

\[
 \mathfrak B_{H,S_n}(F)=\Omega_{H,S_n}(F)=0.
 \tag{1.9}
\]

All these quantities concern unlabelled rank loads.  No labelled
common-owner synchronization is asserted.

## 2. Genuinely adaptive forest process

Start with the edgeless coordinate forest on \([n]\).  At stage \(t\), let
\(G_{t-1}\) be the product of the symmetric groups on the current forest
components.

A legal adaptive stage may have the following form.

1. Starting from \(F_{t-1}\), perform any finite sequence of exact component
   switches using transpositions in \(G_{t-1}\), recomputing the ownership
   components after every switch.

2. Select, from the resulting exact factor and all preceding history, a
   fresh bridge \(e_t\) between two different coordinate components.

3. Enlarge
   \[
   G_t=\langle G_{t-1},e_t\rangle,
   \]
   and perform any finite sequence of exact component switches using
   transpositions in \(G_t\), again recomputing after every switch.  Denote
   the final exact factor by \(F_t\).

Require the fresh bridges to form a spanning tree after \(n-1\) stages.
The edge and every random component choice must be predictable: the edge
is chosen before randomness used later in its stage.  Deterministic choices
are included.

Every individual component update under a transposition \(\tau\) has, at
every depth, the exact form

\[
 \mu'_q-\mu_q=(\tau-I)a_q
 \tag{2.1}
\]

for an integral component-side histogram \(a_q\).  This identity is the
only structural input needed for the next theorem.

### Theorem 2.1 (adaptive spanning-tree profile-release telescope)

For every stage \(t\), every depth \(q\), and every \(G_t\)-orbit
\(\mathcal O\),

\[
 \boxed{
 \sum_{S\in\mathcal O}\mu_q(F_t)(S)
 =
 \sum_{S\in\mathcal O}\mu_q(F_0)(S).
 }
 \tag{2.2}
\]

Consequently,

\[
 \mathfrak B_{H,G_t}(F_t)
 =
 \mathfrak B_{H,G_t}(F_{t-1})
 =
 \mathfrak B_{H,G_t}(F_0),
 \tag{2.3}
\]

and the same identities hold with \(\Omega\).

Define

\[
 \Delta_t^Q
 =
 \mathfrak B_{H,G_{t-1}}(F_{t-1})
 -
 \mathfrak B_{H,G_t}(F_t),
 \tag{2.4}
\]

\[
 \Delta_t^O
 =
 \Omega_{H,G_{t-1}}(F_{t-1})
 -
 \Omega_{H,G_t}(F_t).
 \tag{2.5}
\]

Then, pathwise,

\[
 \boxed{\Delta_t^Q\ge0,\qquad\Delta_t^O\ge0,}
 \tag{2.6}
\]

and

\[
 \boxed{
 \sum_{t=1}^{n-1}\Delta_t^Q=\mathcal Q_H(F_0),
 \qquad
 \sum_{t=1}^{n-1}\Delta_t^O=\mathcal O_H(F_0).
 }
 \tag{2.7}
\]

In particular, along every realized ordered tree chain, some stage has

\[
 \Delta_t^Q\ge\frac{\mathcal Q_H(F_0)}{n-1},
 \tag{2.8}
\]

and some, possibly different, stage has

\[
 \Delta_t^O\ge\frac{\mathcal O_H(F_0)}{n-1}.
 \tag{2.9}
\]

#### Proof

Every switch used through stage \(t\) has a transposition
\(\tau\in G_t\).  A \(G_t\)-orbit is \(\tau\)-invariant.  Summing (2.1)
over that orbit gives zero.  Summing over all preceding switches proves
(2.2).

Orbit floors depend only on the corresponding orbit totals, proving
(2.3).  Since \(G_{t-1}\le G_t\), orbit coarsening and (1.7) give (2.6).
Now telescope (2.4) and (2.5).  Equations (1.8) and (1.9) give the two
endpoints, proving (2.7).  Pigeonholing the \(n-1\) nonnegative summands
gives (2.8) and (2.9).  \(\square\)

For a fixed ordered tree, all releases in (2.4)--(2.5) are determined by
\(F_0\) and the subgroup chain.  They are independent of all intermediate
component-side choices.  If the next edge is selected adaptively, the
chosen group chain depends on the history, but (2.2)--(2.7) remain exact
on every realized path.

The pigeonhole assertion concerns the releases along one ordered
completion.  It does not assert that the marginal releases of all currently
available bridges sum to the current profile floor.  Such a simultaneous
statement would require an additional submodularity theorem, which is not
proved here.

## 3. Exact adaptive slack and restitution

Define the excesses above the current orbit floors:

\[
 X_t^Q
 =
 \mathcal Q_H(F_t)-\mathfrak B_{H,G_t}(F_t)\ge0,
 \tag{3.1}
\]

\[
 X_t^O
 =
 \mathcal O_H(F_t)-\Omega_{H,G_t}(F_t)\ge0.
 \tag{3.2}
\]

Let

\[
 \Gamma_t^Q
 =
 \mathcal Q_H(F_{t-1})-\mathcal Q_H(F_t),
 \qquad
 \Gamma_t^O
 =
 \mathcal O_H(F_{t-1})-\mathcal O_H(F_t).
 \tag{3.3}
\]

These are the net stage gains, including the cost or benefit of all
preparatory and cleanup switches.

### Theorem 3.1 (release-or-slack identity)

Pathwise, for every stage,

\[
 \boxed{
 X_t^Q-X_{t-1}^Q
 =
 \Delta_t^Q-\Gamma_t^Q,
 }
 \tag{3.4}
\]

\[
 \boxed{
 X_t^O-X_{t-1}^O
 =
 \Delta_t^O-\Gamma_t^O.
 }
 \tag{3.5}
\]

Since \(X_0^Q=X_0^O=0\),

\[
 \boxed{
 X_t^Q
 =
 \sum_{s\le t}\Delta_s^Q
 +
 \mathcal Q_H(F_t)-\mathcal Q_H(F_0),
 }
 \tag{3.6}
\]

\[
 \boxed{
 X_t^O
 =
 \sum_{s\le t}\Delta_s^O
 +
 \mathcal O_H(F_t)-\mathcal O_H(F_0).
 }
 \tag{3.7}
\]

If \(F_0\) globally minimizes \(\mathcal Q_H\) over exact factors, then

\[
 \boxed{
 X_t^Q\ge\sum_{s\le t}\Delta_s^Q
 }
 \tag{3.8}
\]

for every realized adaptive path.  If \(F_0\) globally minimizes
\(\mathcal O_H\), the analogous overload inequality holds.

#### Proof

Subtract the definitions:

\[
\begin{aligned}
 X_t^Q-X_{t-1}^Q
 &=
 \mathcal Q_H(F_t)-\mathcal Q_H(F_{t-1})\\
 &\quad+
 \mathfrak B_{H,G_{t-1}}(F_{t-1})
 -\mathfrak B_{H,G_t}(F_t)\\
 &=-\Gamma_t^Q+\Delta_t^Q.
\end{aligned}
\]

This is (3.4); (3.5) is identical.  Summation proves (3.6)--(3.7).
At a global minimizer, every \(F_t\) is an exact factor and
\(\mathcal Q_H(F_t)\ge\mathcal Q_H(F_0)\), giving (3.8).
\(\square\)

Equation (3.8) is the adaptive form of exact component restitution.  It
does not say that every later factor is itself a global minimizer, nor that
every individual later cube has nonnegative drift.  Global minimality is
used only to compare each exact \(F_t\) with the initial \(F_0\).

## 4. One freshly recomputed component cube

Fix a current exact factor \(F\) and a transposition \(\tau\).  Work in the
weighted direct-sum Hilbert space

\[
 \|x\|_H^2
 =
 \sum_{q\le H}\frac{\|x_q\|_2^2}{c_q}.
 \tag{4.1}
\]

Let \(f=f(F)\) be the centered multidepth load vector.  Let
\(\mathcal K_\tau(F)\) be the recomputed ownership components.  Orient each
component effect \(d_K\) from the old side to the transposed side.  Then

\[
 \tau d_K=-d_K,
 \qquad
 \sum_Kd_K=\tau f-f.
 \tag{4.2}
\]

Switching a component subset \(I\subseteq\mathcal K_\tau(F)\) gives one
integral exact factor \(F_I\) with

\[
 f(F_I)=f+d_I,
 \qquad
 d_I=\sum_{K\in I}d_K.
 \tag{4.3}
\]

### Theorem 4.1 (exact fair and best-child gain)

For every component subset \(I\),

\[
 \boxed{
 \mathcal Q_H(F)-\mathcal Q_H(F_I)
 =
 \langle d_I,d_{I^c}\rangle_H.
 }
 \tag{4.4}
\]

Put

\[
 A_\tau
 =
 \left\|\sum_Kd_K\right\|_H^2
 =
 \|f-\tau f\|_H^2,
 \tag{4.5}
\]

\[
 V_\tau=\sum_K\|d_K\|_H^2,
 \tag{4.6}
\]

\[
 \rho_\tau
 =
 \min_{\varepsilon\in\{\pm1\}^{\mathcal K_\tau(F)}}
 \left\|\sum_K\varepsilon_Kd_K\right\|_H^2.
 \tag{4.7}
\]

Then fair independent component signs give expected gain

\[
 \boxed{
 \Gamma_\tau^{\mathrm{fair}}
 =
 \frac{A_\tau-V_\tau}{4},
 }
 \tag{4.8}
\]

while the best legal cube child gives

\[
 \boxed{
 \Gamma_\tau^*
 =
 \max_I
 \bigl[\mathcal Q_H(F)-\mathcal Q_H(F_I)\bigr]
 =
 \frac{A_\tau-\rho_\tau}{4}
 =
 \max_I\langle d_I,d_{I^c}\rangle_H.
 }
 \tag{4.9}
\]

In particular,

\[
 \Gamma_\tau^*
 \ge
 \max\left\{0,\frac{A_\tau-V_\tau}{4}\right\}.
 \tag{4.10}
\]

#### Proof

The midpoint

\[
 P_\tau f=\frac{f+\tau f}{2}
\]

is \(\tau\)-invariant, while every signed sum of the \(d_K\)'s is
\(\tau\)-anti-invariant.  If \(\varepsilon_K=+1\) on \(I\) and \(-1\) on
\(I^c\), then

\[
 f(F_I)
 =
 P_\tau f
 +
 \frac12\sum_K\varepsilon_Kd_K.
 \tag{4.11}
\]

The two terms are orthogonal.  The old child corresponds to the signed sum
\(-\sum_Kd_K\).  Therefore

\[
 \mathcal Q_H(F)-\mathcal Q_H(F_I)
 =
 \frac14\left(
 A_\tau-
 \left\|\sum_K\varepsilon_Kd_K\right\|_H^2
 \right).
 \tag{4.12}
\]

Expanding the right side gives (4.4).  Averaging independent fair signs
replaces the signed-square term by \(V_\tau\), proving (4.8).  Minimizing
it proves (4.9).  The old child has gain zero, and the best child is at
least the fair average, proving (4.10).  \(\square\)

The signs in (4.11) are common across all depths.  Thus (4.9) is already
the correct bundled multidepth cut problem; it is not a sum of separately
optimized rankwise signs.

## 5. Integer profile release versus component capture

For the same transposition, let

\[
 \mathcal R_\tau(F)
 =
 \mathcal Q_H(F)-\mathfrak B_{H,\langle\tau\rangle}(F)
 \tag{5.1}
\]

be the elementary pair-orbit release.  It is the energy decrease available
if one may redistribute load arbitrarily and integrally inside every
\(\tau\)-orbit, without respecting owner components.

Put

\[
 \mathsf B_H
 =
 \sum_{q\le H}\frac{\beta_q}{c_q},
\]

where \(\beta_q\) is the global integral squared-norm floor, and define

\[
 \pi_\tau
 =
 4\left[
 \mathfrak B_{H,\langle\tau\rangle}(F)
 +\mathsf B_H
 -\|P_\tau f\|_H^2
 \right].
 \tag{5.2}
\]

The bracket is the exact integer restitution above the fractional
\(\tau\)-orbit midpoint.

### Theorem 5.1 (exact exposure--capture decomposition)

One has

\[
 \boxed{
 0\le\pi_\tau\le\rho_\tau\le\min\{A_\tau,V_\tau\},
 }
 \tag{5.3}
\]

\[
 \boxed{
 \mathcal R_\tau(F)
 =
 \frac{A_\tau-\pi_\tau}{4},
 }
 \tag{5.4}
\]

\[
 \boxed{
 \Gamma_\tau^{\mathrm{fair}}
 =
 \mathcal R_\tau(F)
 -
 \frac{V_\tau-\pi_\tau}{4},
 }
 \tag{5.5}
\]

\[
 \boxed{
 \Gamma_\tau^*
 =
 \mathcal R_\tau(F)
 -
 \frac{\rho_\tau-\pi_\tau}{4}.
 }
 \tag{5.6}
\]

The quantities \(V_\tau-\pi_\tau\) and \(\rho_\tau-\pi_\tau\) are,
respectively, the fair and optimal component excess above the elementary
integer orbit floor.

#### Proof

The minimum centered squared norm among integral vectors with the current
\(\tau\)-orbit totals is

\[
 \mathfrak B_{H,\langle\tau\rangle}(F)+\mathsf B_H.
\]

The fractional orbit average is \(P_\tau f\), proving
\(\pi_\tau\ge0\).  Every legal cube child is integral and has the same
\(\tau\)-orbit totals.  Its centered squared norm is, by (4.11),

\[
 \|P_\tau f\|_H^2
 +
 \frac14
 \left\|\sum_K\varepsilon_Kd_K\right\|_H^2.
\]

Minimizing over signs gives \(\pi_\tau\le\rho_\tau\).  Averaging signs gives
\(\pi_\tau\le V_\tau\).  The old and all-new signs give signed norm
\(A_\tau\), so \(\rho_\tau\le A_\tau\); averaging gives
\(\rho_\tau\le V_\tau\).

Finally,

\[
\begin{aligned}
 \mathcal R_\tau(F)
 &=
 \|f\|_H^2-\mathsf B_H
 -\mathfrak B_{H,\langle\tau\rangle}(F)\\
 &=
 \bigl(\|f\|_H^2-\|P_\tau f\|_H^2\bigr)
 -\frac{\pi_\tau}{4}\\
 &=
 \frac{A_\tau-\pi_\tau}{4}.
\end{aligned}
\]

Combine this with (4.8)--(4.9) to obtain (5.5)--(5.6).
\(\square\)

Now let \(G\) be the current forest group, let \(\tau\) be a fresh bridge,
and put

\[
 G^+=\langle G,\tau\rangle,
\]

\[
 \Delta_\tau
 =
 \mathfrak B_{H,G}(F)-\mathfrak B_{H,G^+}(F).
 \tag{5.7}
\]

Every \(\tau\)-child preserves all \(G^+\)-orbit totals.  Thus, if

\[
 \mathcal S_G(F)
 =
 \mathcal Q_H(F)-\mathfrak B_{H,G}(F),
\]

then for every child \(F_I\),

\[
 \boxed{
 \mathcal S_{G^+}(F_I)-\mathcal S_G(F)
 =
 \Delta_\tau-
 \bigl[\mathcal Q_H(F)-\mathcal Q_H(F_I)\bigr].
 }
 \tag{5.8}
\]

This is the one-cube specialization of (3.4).

### Corollary 5.2 (exact productive-bridge criteria)

For \(\eta\ge0\), the following are equivalent:

\[
 \exists I:
 \mathcal Q_H(F)-\mathcal Q_H(F_I)
 \ge\eta\Delta_\tau,
 \tag{5.9}
\]

\[
 \boxed{
 \rho_\tau\le A_\tau-4\eta\Delta_\tau.
 }
 \tag{5.10}
\]

Fair heat is \(\eta\)-productive exactly when

\[
 \boxed{
 V_\tau\le A_\tau-4\eta\Delta_\tau.
 }
 \tag{5.11}
\]

Necessarily, every \(\eta\)-productive bridge obeys

\[
 A_\tau\ge4\eta\Delta_\tau.
 \tag{5.12}
\]

The elementary release and component capture separate further.  Suppose
that, for some \(0\le\alpha,\beta\le1\) and errors
\(\xi,\zeta\ge0\),

\[
 \mathcal R_\tau(F)\ge\alpha\Delta_\tau-\xi,
 \tag{5.13}
\]

\[
 \frac{\rho_\tau-\pi_\tau}{4}
 \le
 (1-\beta)\mathcal R_\tau(F)+\zeta.
 \tag{5.14}
\]

Then one exact cube child satisfies

\[
 \boxed{
 \mathcal Q_H(F)-\mathcal Q_H(F_I)
 \ge
 \alpha\beta\Delta_\tau-\beta\xi-\zeta.
 }
 \tag{5.15}
\]

The same assertion holds for fair expected heat with \(\rho_\tau\) replaced
by \(V_\tau\).

#### Proof

Equations (5.10)--(5.11) are (4.8)--(4.9) rewritten.  Equation (5.12)
uses \(\rho_\tau\ge0\).  From (5.6) and (5.14),

\[
 \Gamma_\tau^*\ge\beta\mathcal R_\tau(F)-\zeta.
\]

Apply (5.13) to prove (5.15).  \(\square\)

Condition (5.13) is the **exposure gate**: one transposition matching must
see the floor unlocked by merging two much larger subgroup orbits.
Condition (5.14) is the **signed-fragmentation gate**: the exposed pair
release must not be restored by bundling its occurrences into too few or
badly aligned owner components.

At the first tree edge, \(G=\{1\}\) and \(G^+=\langle\tau\rangle\), so

\[
 \boxed{\Delta_\tau=\mathcal R_\tau(F).}
 \tag{5.16}
\]

Thus there is no exposure loss at the first step.  Exposure becomes a
separate issue only after nontrivial coordinate components have already
formed.

## 6. A rigorous signed-fragmentation sufficient condition

Fix one transposition \(\tau\).  At depth \(q\), index its moved target
pairs by

\[
 p=\{S,\tau S\}.
\]

For component \(K\), orient

\[
 d_{pK}=u_K(S)-u_K(\tau S),
 \qquad
 z_p=\sum_Kd_{pK}
 =\mu_q(S)-\mu_q(\tau S).
 \tag{6.1}
\]

This scalar convention is the negative of the \(S\)-coordinate of the
vector effect \(d_K\) used in Section 4.  All formulas below involve its
sum or square and are consistent with this stated orientation.

Let

\[
 \epsilon_p=
 \begin{cases}
 1,&z_p\text{ odd},\\
 0,&z_p\text{ even}.
 \end{cases}
\]

The pair's elementary integer release and fair gain are exactly

\[
 r_p
 =
 \frac{z_p^2-\epsilon_p}{2c_q},
 \tag{6.2}
\]

\[
 g_p^{\mathrm{fair}}
 =
 \frac{z_p^2-\sum_Kd_{pK}^2}{2c_q}.
 \tag{6.3}
\]

### Lemma 6.1 (same-sign nondominance captures a fixed fraction)

Fix \(0<\eta\le1\).  Suppose, for every moved pair \(p\), that:

1. if \(z_p=0\), then every \(d_{pK}=0\);
2. if \(z_p\ne0\), every nonzero \(d_{pK}\) has the sign of \(z_p\); and
3. whenever \(|z_p|\ge2\),
   \[
   \max_K|d_{pK}|
   \le(1-\eta)|z_p|.
   \tag{6.4}
   \]

Then fair common-sign component heat satisfies

\[
 \boxed{
 \Gamma_\tau^{\mathrm{fair}}
 \ge\eta\mathcal R_\tau(F).
 }
 \tag{6.5}
\]

Consequently one integral exact cube child has at least this gain.

#### Proof

If \(z_p=0\), hypothesis 1 gives zero release and zero gain.  If
\(|z_p|=1\), same-sign integrality forces exactly one nonzero
\(d_{pK}=z_p\); again (6.2)--(6.3) are both zero.

If \(|z_p|\ge2\), the same-sign property gives

\[
 \sum_K|d_{pK}|=|z_p|.
\]

Therefore

\[
\begin{aligned}
 \sum_Kd_{pK}^2
 &\le
 \max_K|d_{pK}|
 \sum_K|d_{pK}|\\
 &\le
 (1-\eta)z_p^2.
\end{aligned}
\]

Equation (6.3) gives

\[
 g_p^{\mathrm{fair}}
 \ge\frac{\eta z_p^2}{2c_q}
 \ge\eta r_p.
\]

Sum over all pairs and depths.  The same component sign is used at all
depths, but linearity of expectation makes the rankwise calculation
simultaneous.  Some cube vertex is no worse than the fair average.
\(\square\)

### Corollary 6.2 (hole--duplicate fragmentation)

Suppose a moved pair has loads \((0,d)\), \(d\ge2\).  Every component
imbalance has the same sign.  If no component carries more than a
\(\rho\)-fraction of the \(d\) duplicate occurrences, then that pair's
fair gain is at least a \(1-\rho\) fraction of its elementary release.

In particular, if every component carries at most one duplicate
occurrence, the pair capture fraction is at least \(1/2\).

This is a pairwise statement.  It does not prove global descent unless
the opposite-sign risk from all other moved pairs is also controlled.
Raw component count or component size alone does not imply the same-sign
condition.

## 7. Conditional adaptive cover-down theorem

The adaptive telescope becomes a balancing theorem as soon as a
quantitative productive-release statement is supplied.

### Theorem 7.1 (fixed-fraction adaptive cover-down)

Let \(F_0\) globally minimize \(\mathcal Q_H\) over all exact middle wreath
factors.  Suppose there is a predictable adaptive forest policy of the
form in Section 2 and nonnegative predictable errors \(\varepsilon_t\)
such that

\[
 \mathbb E\!\left[
 \mathcal Q_H(F_t)
 \mid\mathcal F_{t-1}
 \right]
 \le
 \mathcal Q_H(F_{t-1})
 -\eta\,
 \mathbb E\!\left[
 \Delta_t^Q\mid\mathcal F_{t-1}
 \right]
 +\varepsilon_t
 \tag{7.1}
\]

for a constant \(\eta>0\).  Then

\[
 \boxed{
 \mathcal Q_H(F_0)
 \le
 \frac{\mathbb E\sum_{t=1}^{n-1}\varepsilon_t}{\eta}.
 }
 \tag{7.2}
\]

The same conclusion holds for deterministic choices, with expectations
deleted.  More generally, the local assumptions may be replaced by the
single aggregate path condition

\[
 \mathbb E\sum_t\Gamma_t^Q
 \ge
 \eta\mathcal Q_H(F_0)
 -
 \mathbb E\sum_t\varepsilon_t.
 \tag{7.3}
\]

#### Proof

Sum (7.1), use the pathwise release telescope (2.7), and obtain

\[
 \mathbb E\mathcal Q_H(F_{n-1})
 \le
 (1-\eta)\mathcal Q_H(F_0)
 +
 \mathbb E\sum_t\varepsilon_t.
\]

Every terminal leaf is an exact factor.  Global minimality gives

\[
 \mathbb E\mathcal Q_H(F_{n-1})
 \ge
 \mathcal Q_H(F_0).
\]

Rearrangement proves (7.2).  The aggregate version is identical.
\(\square\)

If the fresh edge, and hence \(\Delta_t^Q\), is selected before all
randomness of stage \(t\), then it is
\(\mathcal F_{t-1}\)-measurable and (7.1) has the simpler form displayed
in the verdict.  The conditional-expectation formulation also permits
random preparatory routing and an edge selected later in the stage.  Its
energy cost remains included in the left side.

There is an exact fair-heat form of the hypothesis.  If stage \(t\)
consists of one fresh fair component cube, then (7.1) is equivalent to

\[
 \boxed{
 A_{e_t}-V_{e_t}
 \ge
 4\eta\Delta_t^Q-4\varepsilon_t.
 }
 \tag{7.4}
\]

For a deterministic best child it is equivalent to

\[
 \boxed{
 A_{e_t}-\rho_{e_t}
 \ge
 4\eta\Delta_t^Q-4\varepsilon_t.
 }
 \tag{7.5}
\]

If a stage includes preparatory switches, their energy cost must be
included in the net \(\Gamma_t^Q\).  Recomputing components is free
structurally but not automatically free energetically.

### Fixed-window implication

Fix \(A>0\) and put

\[
 H_A=\lceil A\sqrt m\rceil,
 \qquad
 \operatorname{Cat}_m=\frac Wn.
\]

A sufficient theorem has constants

\[
 \eta_A>0,
 \qquad
 C_A<\infty,
 \qquad
 m_A,
\]

such that for every \(m\ge m_A\), a global
\(\mathcal Q_{H_A}\)-minimizer admits the preceding adaptive policy with

\[
 \mathbb E\sum_t\varepsilon_t
 \le
 C_AH_A\operatorname{Cat}_m.
 \tag{7.6}
\]

Then

\[
 \boxed{
 \mathcal Q_{H_A}(F_0)
 \le
 \frac{C_A}{\eta_A}
 H_A\operatorname{Cat}_m
 =
 O_A\!\left(\frac W{\sqrt m}\right)
 =
 o(W).
 }
 \tag{7.7}
\]

Equation (1.4) gives the same \(o(W)\) conclusion for weighted overload.
The constants \(\eta_A,C_A\) and the threshold \(m_A\) may depend on the
fixed \(A\), but not on \(m\).  The minimizer and adaptive policy may
depend on both \(m\) and \(A\).

More generally, total error \(o_A(W)\) suffices.  If one uses the same
per-stage allowance over \(n-1\) stages, the Catalan-scale target is

\[
 \varepsilon_t
 =
 O_A\!\left(
 \frac{H_A\operatorname{Cat}_m}{n}
 \right).
 \tag{7.8}
\]

An error \(O_A(\operatorname{Cat}_m)\) at every stage totals \(O_A(W)\)
and is not enough for \(o(W)\).

One must not infer

\[
 \Delta_t^Q\ge2\Delta_t^O
\]

from \(\mathfrak B_{H,G}\ge2\Omega_{H,G}\); differences of two such floors
need not preserve the factor two.  The quadratic and overload telescopes
are separate.  The quadratic route obtains overload only at the end via
(1.4).

## 8. Two rigorous barriers to profile-only productivity

### 8.1 Exposure can vanish before component bundling

The following is an integral orbit-profile construction.  It is not
claimed to be the load profile of an exact wreath factor.

Let \(V\) be a coordinate component of size \(t\ge3\), let \(x\) be a new
singleton coordinate, and put \(G=S_V\).  Fix all coordinates outside
\(V\cup\{x\}\), and consider targets using exactly two coordinates from
\(V\cup\{x\}\).  The two relevant \(G\)-orbits are

\[
 \mathcal X_0=\binom V2
\]

for targets avoiding \(x\), and

\[
 \mathcal X_1=\{\{x,b\}:b\in V\}
\]

for targets containing \(x\).

Choose \(A_*\in\binom V2\) and \(b_*\in V\setminus A_*\).  On these two
orbits set the integral loads

\[
 \mu(A_*)=c+2,
 \qquad
 \mu(\{x,b_*\})=c,
 \]

and put load \(c+1\) on every other target.

To make this a full formal rank-load vector with \(c\) as its global floor,
put load \(c\) on every target outside these two local orbits.  If their
combined size is \(M<N_q\), the total is \(cN_q+M\), so the quotient is
indeed \(c\).  This is a formal choice of total mass, not an assertion that
it equals the actual wreath occurrence total at the chosen rank.

Within \(\mathcal X_0\), the unique excess unit forces quadratic
orbit-floor contribution \(2\).  Within \(\mathcal X_1\), the loads
\(c,c+1\) are already floor-balanced.  After adjoining any bridge
\((a,x)\), the generated group merges the two orbits, whose combined total
is exactly

\[
 (c+1)(|\mathcal X_0|+|\mathcal X_1|).
\]

Thus the fresh subgroup release is

\[
 \boxed{\Delta^Q=2.}
 \tag{8.1}
\]

For a bridge \(\tau_a=(a,x)\), the moved target pairs are exactly the
incidences

\[
 A\longleftrightarrow\{x\}\cup(A\setminus\{a\}),
 \qquad a\in A.
\]

The two exceptional vertices are never paired **with each other**, because
\(b_*\notin A_*\).  Either exceptional vertex may move, but its partner
then has load \(c+1\).  Every moved pair therefore has load difference at
most one.  Such a pair is already integrally balanced at its fixed sum, so

\[
 \boxed{
 \mathcal R_{\tau_a}=0
 \quad\text{for every }a\in V.
 }
 \tag{8.2}
\]

Hence no inequality

\[
 \max_{a\in V}\mathcal R_{(a,x)}
 \ge\alpha\Delta^Q
\]

with universal \(\alpha>0\) follows from the orbit totals and integrality
alone.  This is an exact obstruction to the exposure gate at the relaxed
profile level.  A positive theorem must use additional exact-wreath
structure or tolerate an additive error that absorbs such discrete
plateaux.

Relative to the \(c+1\) baseline on the two displayed orbits, the local
discrepancy is

\[
 \mathbf1_{A_*}-\mathbf1_{\{x,b_*\}},
\]

whose point margins are nonzero.  Thus this construction does not rule out
an exposure theorem that makes essential use of exact-factor point
regularity.

### 8.2 Positive elementary release can have zero component capture

There is also a formal mean-one last-slack model whose centered discrepancy
satisfies the relevant homogeneous linear constraints.

On a rank \(2\le r\le n-2\), choose four coordinates \(a,b,c,d\) and put

\[
 g(S)
 =
 (\mathbf1_{a\in S}-\mathbf1_{b\in S})
 (\mathbf1_{c\in S}-\mathbf1_{d\in S}).
 \tag{8.3}
\]

Then \(g\ne0\), has zero total and zero point margins, and is negated by
\(\tau=(a\,b)\).

Indeed, swapping \(a,b\) pairs all nonzero total contributions with their
negatives.  For a point different from \(a,b\), the same pairing preserves
membership of that point; for the \(a\)- and \(b\)-point margins, swapping
\(c,d\) instead preserves the relevant membership and negates \(g\).
The \(c\)- and \(d\)-point margins are handled by swapping \(a,b\).

The nonnegative integral mean-one load

\[
 \mu=\mathbf1+g
\]

takes values \(0,1,2\).  Its centered discrepancy has zero total and zero
point margins, and it has positive elementary \(\tau\)-pair release:
every nonzero pair has loads \(0,2\).

Now formally place the whole \(\tau\)-effect in one component.  The only
two component children are \(\mu\) and \(\tau\mu=\mathbf1-g\).  They have
identical floor energy, so

\[
 \boxed{\mathcal R_\tau>0,\qquad\Gamma_\tau^*=0.}
 \tag{8.4}
\]

This model is nonnegative, integral, equivariant, and has a zero-point-
margin centered discrepancy, but its total is the rank size \(N_r\), not
the actual wreath occurrence total \(W\) at a general lower rank.  No
actual-parameter or exact-wreath ownership realization is asserted.  It
proves that integrality, Johnson support, and profile release alone cannot
establish the fragmentation gate.

An actual connected \(\tau\)-overlay would have the same conclusion:
there would be one component, hence only \(F\) and \(\tau F\), with zero
gain for every relabelling-invariant energy.  Connected exact overlays are
known, but no all-dimensional exact factor is proved here to have both a
connected overlay and positive elementary release for that same
transposition.  Thus no exact-factor counterexample to adaptive
productivity is claimed.

### 8.3 Aggregating before choosing is still impossible

The exact point-stabilizer theorem gives a physical warning.  The subgroup
\(S_{n-1}\) has zero profile floor for every exact factor, so aggregating a
spanning tree on \(n-1\) coordinates releases the entire quadratic profile
floor.  Nevertheless its joined owner partition has one block and every
subgroup child is a whole relabelling, with exactly zero gain.

This does not refute sequential recomputation after each bridge.  It proves
that component choices must be made while the release is fresh; postponing
all choices until after the joins restores the full release as component
noise.

## 9. Exact remaining theorem

The adaptive route is now reduced to the following statement.

> **AFR\(_A\): adaptive fresh-release theorem (UNPROVED).**  For every
> fixed \(A>0\), there are constants
> \(\eta_A>0\), \(C_A<\infty\), and \(m_A\) such that, for every
> \(m\ge m_A\), a global minimizer \(F_0\) of
> \(\mathcal Q_{H_A}\), \(H_A=\lceil A\sqrt m\rceil\), admits a
> predictable spanning-tree sequence of genuinely recomputed exact
> component switches for which
> \[
> \mathbb E\sum_t\Gamma_t^Q
> \ge
> \eta_A\sum_t\Delta_t^Q
> -
> C_AH_A\operatorname{Cat}_m.
> \]

By Theorem 2.1,

\[
 \sum_t\Delta_t^Q=\mathcal Q_{H_A}(F_0),
\]

so Theorem 7.1 shows immediately that AFR\(_A\) implies

\[
 \mathcal Q_{H_A}(F_0)
 \le
 \frac{C_A}{\eta_A}
 H_A\operatorname{Cat}_m
 =
 o(W).
\]

A stronger but cleaner local version asks, at every fresh stage, for

\[
 \Gamma_t^Q
 \ge
 \eta_A\Delta_t^Q-\varepsilon_t,
 \qquad
 \sum_t\varepsilon_t
 \le
 C_AH_A\operatorname{Cat}_m.
 \tag{9.1}
\]

The two-gate Corollary 5.2 gives one precise route to (9.1):

\[
 \text{expose a fixed share of }\Delta_t^Q
 \quad+\quad
 \text{capture a fixed share by a signed component cut}.
\]

The exposure countermodel in Section 8.1 and the fragmentation countermodel
in Section 8.2 show that each part must use genuine wreath ownership
geometry.  The spanning-tree telescope by itself supplies neither.

At a global minimizer, every individual best-child gain is zero, because
the old cube vertex is available and no exact child can have lower energy.
Therefore a no-error universal positive-fraction theorem would force
\(\mathcal Q_H(F_0)=0\) exactly.  This would be a much stronger simultaneous
exact-balancing theorem.  The Catalan-scale total error in AFR\(_A\) is
not cosmetic; it is the natural scale needed for the actual \(o(W)\)
target.

## 10. Scope and audit

The decisive assertions were independently audited in three directions.

1. The adaptive-orbit audit confirmed that every current \(G_t\)-orbit
   total equals its initial value, even after arbitrary recomputed
   \(G_t\)-legal switches.  It confirmed both telescopes, the
   \(1/(n-1)\) pigeonhole constant, and the fact that adaptive edge choice
   changes only the realized subgroup chain.

2. The component-cut audit confirmed the exact subset gain
   \(\langle d_I,d_{I^c}\rangle_H\), the factors \(1/4\) in
   (4.8)--(4.9), the integer restitution ordering
   \(\pi_\tau\le\rho_\tau\le\min(A_\tau,V_\tau)\), and the productive
   criterion (5.10).

3. The adversarial audit confirmed that neither best-child selection nor
   bridge averaging supplies a term involving \(\Delta_\tau\) without a
   new exposure or signed-fragmentation theorem.  It also identified the
   ordered-chain scope: the release telescope is not a simultaneous sum
   over all currently available bridges.

The following qualifications are essential.

* Every factor actually visited is one integral exact factor.  Fractional
  orbit averages and profile minima are analytic comparison objects only.

* Components are recomputed after every legal switch.  No fixed endpoint
  bundle or common component join is used.

* Releases are common multidepth quantities, and component signs are common
  across all depths.  Rankwise sign optimization would prove a different,
  weaker statement.

* A fixed ordered forest chain has releases independent of intermediate
  component choices.  The capture quantities \(V_\tau\), \(\rho_\tau\),
  and the signed Gram cuts depend on the current exact factor.

* Later factors on a path from a global minimizer need not themselves be
  minimizers.  Only comparison with the initial global minimum is valid.

* The two profile telescopes are separate.  The inequality
  \(\mathfrak B_{H,G}\ge2\Omega_{H,G}\) does not imply the corresponding
  inequality between successive releases.

* Sections 8.1 and 8.2 are rigorous profile or signed-load barriers, not
  exact-wreath counterexamples.

* AFR\(_A\) is an unlabelled sufficient theorem.  It neither proves nor
  requires the stronger labelled common-owner synchronization statement.

## 11. Final theorem-level conclusion

The fixed-word/subgroup no-go does not kill adaptive heat.  It identifies
the timing constraint.  Along a genuinely recomputed spanning-tree process,
the entire initial profile defect is released exactly once, pathwise, and
the release survives every intervening exact component choice as an orbit
invariant.  The exact slack identity records whether each released unit is
converted to actual descent or restored as new component excess.

What remains is not another spectral estimate.  It is the wreath-specific
productive-release theorem AFR\(_A\): before a fresh subgroup merger is
hidden inside later joins, expose a positive portion of its orbit-floor
release to one or more fresh transposition matchings and disperse the
resulting signed multidepth effects among recomputed components so that one
common sign cut captures a fixed portion, up to total
\(O_A(H_A\operatorname{Cat}_m)\) loss.

The adaptive release and slack telescopes are proved.  The fixed-fraction
capture theorem is not.
