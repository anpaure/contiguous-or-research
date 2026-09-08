# Audit of future service, adapted marks, and the small potential cap

**Date:** 2026-08-06  
**Audited notes:**

* `MATH_THEOREM_FUTURE_WEIGHTED_AFFINE_INSERTION_HARDY_AND_POTENTIAL_CAP_REDUCTION_20260806.md`;
* `MATH_THEOREM_ADAPTED_MARK_FUTURE_SERVICE_IDENTITY_AND_INNOVATION_REDUCTION_20260806.md`;
* `MATH_THEOREM_SMALL_CAP_FIRST_VIOLATION_AND_JOINT_ABSORPTION_20260806.md`.

**Verdict:** **PASS AS A CONDITIONAL REDUCTION, NOT AS CLOSURE OF THE
JOINT ANALYTIC GATE.**  The fixed-mark future-service identity, the
`PCAP => beta_T=O(epsilon_P/d^2)` scaling, the exact adapted-mark square
expansion, the quadratic incidence estimate, the algebraic small-constant
absorption, and the first-violation Markov bound are valid under their
displayed hypotheses.  Revision
`49db2d78212c15adee1230a2495de7e88db6e35b03dd64a65557fe3621306b7f`
also removes the former unsupported `K1 -> FE3` step: ordinary Young,
followed by the small Hardy coefficient, controls the killed correlation
without `FE3`.  The small-cap theorem nevertheless remains conditional on
its stated joint signed decomposition `(1.2)`, in particular the mean
one-root hazard/`HDIR` transfer and the identified `GDIR`/root-carre rows.

## 1. Fixed-mark future service

For one live row, the next fixed-mark contribution is

\[
 c_i(a)R_i(a;G){\bf1}_{\{a\text{ survives}\}}\psi(a)^2.
\]

Consequently `(1.3)` gives the displayed supermartingale drift after
summing rows.  Stopping and telescoping are legitimate in the present
finite process; for an abstract unbounded stopping time the statement
should be read after localization and monotone convergence.

For the pair future fugacity,

\[
 R_i(1-q_i)=\rho_i^2
\]

and therefore

\[
 R_i(1-\kappa_i)-1
 =-(1-\rho_i^2)+R_i(q_i-\kappa_i).
\]

Replacing the signed last term by
`R_i(q_i-kappa_i)_+` proves the claimed one-sided drift.  No independence
or future conditioning is used.  This part is exact.

The affine estimate is also valid for the frozen coordinate-star mode:
the candidate quadratic mass bounds the positive killed-Green residue,
and the coordinate-star slope is absolute (`1` on the lower shore and
`h<=3` on the owner shore).  Thus no unrecorded amplitude factor is lost
when `d^{-2}||psi||_infty^2=O(1)` is used.

## 2. The potential-cap coefficient calculation

Let

\[
 g_x^\circ=\sum_{a:x\in U_a^\circ}c_i(a)R_i(a),
 \qquad
 \beta_T={\sum_xg_x^\circ\over\sum_xY_x}.
\]

If a row has at most `C d` incidences of type `T`, then

\[
 \sum_xg_x^\circ\le Cd\sum_ac_i(a)R_i(a)=Cd\mathcal P_i^+.
\]

On the good-load interval, `sum_x Y_x >= c N_T`; one density step has
`R_i(a)=1+o(1)`, uniformly for rows of size `O(d)`, so
`mathcal P_i^+ <= 2 mathcal P_i` for large `d`.  Hence

\[
 \mathcal P_i\le\varepsilon_P{N_T\over d^3}
 \quad\Longrightarrow\quad
 \beta_T\le {C\varepsilon_P\over d^2}.
\]

Moreover `X >= c_X pM/(2d)` and
`1-rho=2d/(pM)` imply

\[
 {1\over X}\le C(1-\rho^2).
\]

Thus `(PCAP)` really does imply the coefficient ratio used by the
fixed-coordinate affine occupation argument.

There is one notation/interface condition: the `beta_i` multiplying
`(IPH)` must be the same type-resolved potential-incidence coefficient
`beta_T` (or a sum for which the same incidence count is proved).  The
ANOVA note introduces `beta_i` only inside `(IPH)`.  The cap calculation
does not by itself identify an arbitrary Bellman prefactor with `beta_T`,
nor does it cover the other Hoeffding modes.  That bridge should remain an
explicit hypothesis.

## 3. Adapted-mark expansion and Proposition 3.1

Provided `K` is the fixed incidence operator on a surviving row and
`delta_i^G` is the full hypothetical resource-vector increment, the
identity

\[
 (g_i+K\delta_i^G)^2-g_i^2
 =2g_iK\delta_i^G+(K\delta_i^G)^2
\]

gives `(1.4)` exactly.  Adding all hypothetical transitions and subtracting
the killed rows gives `(2.4)` exactly as well.

Proposition 3.1 is valid.  If `m_x=E_i(delta_{i,x}^G)^2`, then row-size
Cauchy gives

\[
 \mathcal Q_i\le Cd\sum_x(\beta_iY_x+\zeta_x)m_x.
\]

For the centered part one must take absolute values, and

\[
 |\zeta_x|m_x
 \le {d\over2}{\zeta_x^2\over Y_x}
   +{1\over2d}Y_xm_x^2.
\]

The bounded-increment hypothesis makes `m_x^2=O(m_x)`.  This yields

\[
 \mathcal Q_i
 \le C\{d^2\mathfrak G_i+(1+d\beta_i)\mathcal V_i^{\rm root}\}.
\]

After multiplication by the `O(epsilon_P/d^2)` occupation coefficient,
there is no residual positional `d^2` loss.  Calling the first term the
*existing* `GDIR` row still requires the coefficient/occurrence
identification between this innovation incidence family and the
type-resolved family in `GDIR`; the displayed inequality alone does not
prove that dynamic transfer.

## 4. The killed linear correlation is closed by the small coefficient

The revised note uses ordinary Young:

\[
 -\mathcal K_i^{(1)}
 \le \mathcal D_i^{\rm kill}
      +\mathcal Q_i^{\rm kill}.
\]

An `O(d)`-row has actual hit probability `O(d(1-rho_i))` on the good
total-rate interval.  Hence

\[
 \mathcal D_i^{\rm kill}
 \le Cd(1-\rho_i^2)\Phi_i
\]

up to an absolute factor from `R_i<=2`.  The entire adapted innovation is
then multiplied by `C epsilon_P/d^2`; its killed-diagonal contribution is
only `O(epsilon_P/d)` times the service mass.  Also
`Q_i^{kill}<=Q_i`, and Proposition 3.1 controls the latter after the same
multiplier.  Therefore no `FE3` injection is needed for `K1`.

The phrase in the revised note saying that one-entry and two-entry
expansions must "implement (4.6)" is unnecessary: `(4.6)` is already the
pointwise Young inequality.  It should not be read as an additional gate.
The note's final conditional statement

\[
 \text{GDIR + HDIR + root-carre injection}
 \Longrightarrow\text{adapted innovation absorption}
\]

is proof-safe without a killed-correlation/`FE3` premise.  Its live
analytic premise is now the mean one-root hazard/`HDIR` term in `(4.4)`,
together with the already named `GDIR` and root-carre identification used
by Proposition 3.1.

## 5. Small-cap stopping and circularity

Given the two inequalities

\[
 \mathsf D+\mathsf H\le C_0\mathsf A+C_1\mathsf I,
 \qquad
 \mathsf I\le C_2\varepsilon_P
    (\mathsf A+\mathsf D+\mathsf H),
\]

the simultaneous absorption is elementary and noncircular.  Choosing
`epsilon_P` first closes all three stopped budgets together.  The future
potential drift then gives

\[
 E\mathcal P_\tau\le\mathcal P_0+\mathsf D\le C\mathsf A,
\]

so the first-violation Markov estimate is correct.

The stopping time must include every condition used to derive the two
inequalities: besides `PCAP`, this includes the good-load, total-rate,
owner-mixture, and any individual-root stops.  At a `PCAP` violation the
lower bound `N_T(tau)>=c_T cM/d` must still hold.  If those other stops are
handled in a separate bootstrap, their failure probabilities must be
combined before declaring a terminal success event.

The annealed terminal-event interface is valid under the raw law: a
constant-probability event may be imposed at reciprocal constant expected
cost.  It does not prove a conditioned random output law, and it does not
supply any downstream deterministic completion missing from the event.

## 6. Proof-safe frontier

The three notes establish the following implication:

\[
 \boxed{
 \begin{gathered}
 \text{coefficient-faithful joint GDIR/HDIR/root-carre decomposition,}\\
 \text{including the mean one-root hazard transfer}
 \end{gathered}
 \Longrightarrow
 \text{affine IPH + PCAP close with a small constant}.}
\]

They do **not** establish the antecedent.  In particular, `PCAP` and the
killed `K1` correlation are no longer independent scale obstructions.  The
mean one-root hazard/`HDIR` transfer, plus the coefficient-faithful
identification of the normalized-gradient and root-carre rows, is the live
analytic gate.
