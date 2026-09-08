# Moving-atlas outer packets: complement reduction and the exact Hall cut

Date: 2026-07-26

## 0. Outcome

Assume the local compiler is complete: every admissible cell option is an
exact whole-cycle factor, and its literal lower and upper trace maps are
certified through the protected depth.  The remaining choice problem has
an exact quotient formulation.

For a moving perfect-matching atlas `A`, let `U_kappa` be the common owner
supports classified in
`MATH_THEOREM_MOVING_PERFECT_MATCHING_ATLAS_RECOUPLING_20260726.md`.
These `U_kappa`, and no finer componentwise pieces, are the independent
integral variables.  At depth `q`, the exact fractional deficit is

\[
 \boxed{
 \eta_q=\max_{0\le y_T^- ,y_T^+\le1}
 \left[
   \sum_T(y_T^-+y_T^+)
   -\sum_\kappa\max_{o\in\Theta_\kappa}
      \left(
       \sum_{T\in L_{\kappa,o}}y_T^-
       +\sum_{T\in U_{\kappa,o}}y_T^+
      \right)
 \right].}                                                    \tag{0.1}
\]

This is the sharp multiple-choice Hall cut.  The desired outer theorem is
equivalent to proving that (0.1), summed over protected depths, is `o(W)`,
followed by an integral component-rounding theorem.

Complementation removes a false doubling of the gate.  For every whole
isometric doubled-permutation cycle, upper traces are complements of lower
traces on the antipodal cycle phase.  On a complement-closed packet atlas,
the fractional programme has an optimal complement-symmetric solution, so
the two signs reduce exactly to one sign on complement orbits.  Integral
choices have the same reduction whenever complementary owner components
are assigned complementary options.

The known frozen-suffix obstruction is one explicit feasible dual vector
in (0.1).  A moving atlas escapes it only if its component options transport
literal occurrences across every positive-density suffix cut.  Local trace
injectivity, balanced face counts, and exact owner recoupling do not imply
this condition.

## 1. Exact component variables

Let the coordinate union graph of the atlas have components
`B_1,...,B_c`.  For

\[
 \kappa=(\kappa_1,\ldots,\kappa_c),\qquad
 0\le\kappa_j\le|B_j|,\qquad\sum_j\kappa_j=m,                  \tag{1.1}
\]

put

\[
 U_\kappa=\{X\in\tbinom{[2m]}m:|X\cap B_j|=\kappa_j\}.         \tag{1.2}
\]

The exclusion-component theorem proves that every status-cell partition
from every atlas matching restricts to a partition of `U_kappa`, and that
the multipartite overlap is connected on `U_kappa`.  Hence an exact
componentwise construction must choose one whole option

\[
                              o(\kappa)\in\Theta_\kappa         \tag{1.3}
\]

on each `U_kappa`.  It cannot choose different matching shores on a
proper nonempty subset of `U_kappa` merely by invoking cell overlap.

For an option `o`, let

\[
 L_{\kappa,o,q}\subseteq\binom{[2m]}{m-q},\qquad
 U_{\kappa,o,q}\subseteq\binom{[2m]}{m+q}                     \tag{1.4}
\]

be its literal signed target images, counted with multiplicity if the
certified local map is not injective.  Nothing below treats different
presentations, shores, or cells as additional owner mass.

## 2. Multiple-choice primal and dual

For one depth, the fractional component programme is

\[
\begin{aligned}
 \eta_q=\minquad&\sum_T(z_T^-+z_T^+),\\
 z_T^-+&\sum_{\kappa,o}{\bf1}_{T\in L_{\kappa,o,q}}x_{\kappa,o}\ge1,\\
 z_T^++&\sum_{\kappa,o}{\bf1}_{T\in U_{\kappa,o,q}}x_{\kappa,o}\ge1,\\
 &\sum_{o\in\Theta_\kappa}x_{\kappa,o}=1,
 \qquad x,z\ge0.                                               \tag{2.1}
\end{aligned}
\]

### Theorem 2.1 (exact component-quotient dual)

The value of (2.1) is (0.1).  Equivalently, fractional `o(W)` deficit is
possible if and only if, for every pair of target weights in `[0,1]`,

\[
 \sum_\kappa\max_{o\in\Theta_\kappa}
 \left(\sum_{T\in L_{\kappa,o,q}}y_T^-
      +\sum_{T\in U_{\kappa,o,q}}y_T^+\right)
 \ge \sum_T(y_T^-+y_T^+)-o(W).                                 \tag{2.2}
\]

#### Proof

Dualize the two target-cover inequalities with variables in `[0,1]`; the
upper bound comes from the unit repair variable `z_T`.  The equality for
one component has a free dual scalar.  Minimizing over that scalar replaces
it by the maximum option weight in the component, giving (0.1).  Strong LP
duality applies because the finite programmes are feasible and bounded.
\(\square\)

For integral choices, the corresponding necessary Hall family is: for all
target sets `A^-,A^+`,

\[
 |A^-|+|A^+|
 \le\sum_\kappa\max_o
 \bigl(|L_{\kappa,o,q}\cap A^-|
      +|U_{\kappa,o,q}\cap A^+|\bigr)+o(W).                    \tag{2.3}
\]

Weighted inequalities (2.2), not only singleton or set indicators, are
the exact fractional criterion.

For simultaneous depths, the same option must be used at every `q`.  The
exact joint dual is therefore

\[
 \eta_H=max_{0\le y_{q,T}^\pm\le1}
 \left[
  \sum_{q,T}(y_{q,T}^-+y_{q,T}^+)
  -\sum_\kappa\max_o
    \sum_{q,T}
       \bigl({\bf1}_{T\in L_{\kappa,o,q}}y_{q,T}^-
            +{\bf1}_{T\in U_{\kappa,o,q}}y_{q,T}^+\bigr)
 \right].                                                       \tag{2.4}
\]

It is essential not to replace (2.4) by a sum of independently optimized
one-depth programmes: that would silently allow a different option at each
depth, which the construction does not permit.

## 3. Complement symmetry collapses the two signs

Let a cycle have middle phases

\[
                         X_0,X_1,\ldots,X_{2h-1},
 \qquad X_{t+h}=[2m]\setminus X_t                              \tag{3.1}
\]

on its active coordinates, with frozen spectators complemented in the
companion packet.  For a cyclic phase interval `I`, De Morgan gives

\[
 [2m]\setminus\bigcup_{t\in I}X_t
 =\bigcap_{t\in I}([2m]\setminus X_t)
 =\bigcap_{t\in I}X_{t+h}.                                     \tag{3.2}
\]

### Lemma 3.1 (signed option involution)

On a complement-closed packet system there is an involution

\[
 (\kappa,o,T,-)\longmapsto
 (\kappa^c,o^c,[2m]\setminus T,+),qquad
 \kappa_j^c=|B_j|-\kappa_j,                                   \tag{3.3}
\]

which preserves literal occurrence multiplicity.

#### Proof

Complement every owner, reverse the frozen full/empty statuses, and shift
each doubled-permutation cycle by its antipodal half-period.  Equation
(3.2) exchanges lower and upper traces and complements the target.  This
operation is involutive and preserves phase counts. \(\square\)

### Corollary 3.2 (fractional sign reduction)

Average any feasible fractional solution of (2.1) with its image under
(3.3).  The result is feasible, has the same objective, and satisfies

\[
 x_{\kappa,o}=x_{\kappa^c,o^c},\qquad
 z_T^-=z_{[2m]\setminus T}^+.                                  \tag{3.4}
\]

Hence an optimal symmetric solution exists and its two signed deficits
are equal.  The two-sign fractional gate is exactly twice the one-sign
gate on complement orbits.

For an integral construction, imposing

\[
                         o(\kappa^c)=o(\kappa)^c                 \tag{3.5}
\]

gives the same conclusion.  Self-complementary component orbits require a
complement-stable option or a two-option antipodal packet, which is the
only finite parity caveat.

## 4. The frozen-suffix dual as a special case

Suppose a positive-density coordinate set `R` is untouched by every option
on all but `o(W)` owners.  Give unit lower dual weight to targets satisfying

\[
                         |T\cap R|\le a                          \tag{4.1}
\]

and unit upper dual weight to targets satisfying

\[
                         |T\cap R|\ge |R|-a.                     \tag{4.2}
\]

Every normal component option has weighted occurrence count at most the
number of its middle owners in the corresponding two suffix tails.  Summing
the component maxima therefore gives exactly the histogram-capacity bound
of
`MATH_ATTACK_L_PARITY_COMPLETE_OUTER_PACKET_OCCURRENCE_HALL_20260726.md`.
At `q=A sqrt(m)` its dual margin is

\[
                         (2\delta_A-o(1))W>0.                    \tag{4.3}
\]

Thus (4.1)--(4.2) are a concrete witness violating (2.2) for every fixed
first-eligible/frozen-suffix atlas.

The moving atlas must invalidate the premise at the occurrence level: it
must place `Omega(W)` protected windows across each such suffix boundary.
Merely listing matchings which cross `R` is insufficient if component
rigidity forces their corresponding options to be selected globally or on
negligible owner mass.

## 5. Sharp remaining cut

After complement reduction, define for one sign and one depth

\[
 \mathfrak D_q(y)=
 \sum_Ty_T-sum_\kappa\max_{o\in\Theta_\kappa}
                  \sum_{T\in L_{\kappa,o,q}}y_T,
 \qquad0\le y_T\le1.                                          \tag{5.1}
\]

At one depth the exact outer fractional theorem is

\[
                         \sup_y\mathfrak D_q(y)=o(W)             \tag{5.2}
\]

The simultaneous theorem uses (2.4), with one common per-component maximum,
and requires `eta_H=o(W)`.  This is now the unique
quantitative gate: ownership exactness is already encoded by the
`U_kappa` variables, and local trace injectivity is already encoded by the
literal image sets.

No theorem proved so far bounds (5.1) for a moving atlas.  In particular:

* local image injectivity controls `|L_{kappa,o,q}|` but not its placement;
* average face balance controls singleton weights but not arbitrary `y`;
* the atlas component theorem supplies legal variables but no target
  expansion;
* complement symmetry removes one sign but no weighted cut.

A sufficient next theorem is a uniform component-expansion inequality

\[
 \sum_\kappa\max_o\sum_{T\in L_{\kappa,o,q}}y_T
 \ge(1-o(1))\sum_Ty_T                                           \tag{5.3}
\]

for every `y in [0,1]`, simultaneously in `q`.  Conversely, one explicit
weight with positive linear `mathfrak D_q(y)` is a statewise obstruction
to the entire moving-atlas packet menu.

Even after (5.3), integral rounding is a separate theorem: an arbitrary
multiple-choice set-cover matrix need not have vanishing integrality gap.
One must either prove a balanced-decomposition/TU property of these
component images or construct the integral choices directly.
