# Audit of complete-row blocker conjugation and switch normalization

**Date:** 2026-08-06  
**Audited file:**
MATH_THEOREM_COMPLETE_ROW_BLOCKER_CONJUGATION_AND_SWITCH_NORMALIZATION_GATE_20260806.md  
**Method:** exact coefficient, operator-type, orbit-multiplicity, and
normalization audit; no computation or search  
**Verdict:** **PASS AS A CONDITIONAL TRANSPORT THEOREM AND A
NORMALIZATION NO-GO.  NOT AN UNCONDITIONAL BELLMAN CLOSURE.**

## 1. Service scalar

The calculation

\[
 1-\rho_i=\frac{2d}{p_iM},
 \qquad
 X_i=(1+o(1))\frac{p_iM}{2d}
\]

gives

\[
                         X_i(1-\rho_i^2)=2+o(1).
\]

This is exact up to the already stated global-rate bootstrap.  No private
switch quantity enters it.

## 2. Operator types

For a composite incidence vector \(z_A\) and resource vector \(f\),
\[
                         g_A=\langle z_A,f\rangle
\]
is scalar, while
\[
                         b_{A,\tau}=z_A-z_{\tau A}
\]
is a resource-layer vector.  Therefore
\[
 \langle f,b_{A,\tau}b_{A,\tau}^*f\rangle
                         =(g_A-g_{\tau A})^2
\]
is well typed.  The proof never applies the resource resolvent to
\(g_A\).  It does not repeat the type error in the withdrawn raw
composite-switch note.

## 3. Complete-row polarization

The inequality

\[
                         (g_A-g_{\tau A})^2
 \le2g_A^2+2g_{\tau A}^2
\]

is exact and includes every changed occurrence.  Hence, conditional on
both complete-row squares having the same first-entry coefficient and
being present in the rooted ledger, no hit/unhit decomposition remains.

The blocker map

\[
                         (\tau A,G,y)
 \longmapsto(A,\tau G,\tau y)
\]

is an involution when the transposition label is retained.  Complete
coordinate covariance preserves the raw rate and hypothetical-next
coefficient.  Forgetting the transposition has fibre at most
\(\binom{k}{2}\), exactly cancelled by the uniform transposition
normalization.  This part passes.

## 4. Input that remains conditional

The complete-row estimate (4.1) of the audited theorem is an explicit
input.  Static rooted-overlap normalization makes it plausible and is the
intended selected-relation ledger, but this audit does not identify a
separate source theorem whose displayed coefficient is literally

\[
 \frac{\beta_Td}{X_i}\,
 w_i(A,\tau,G)\,g_{\tau A}^2
\]

for every stopped boundary.  In particular:

1. the transition probability must occur exactly once;
2. the hypothetical-next composite coefficient must be the same one used
   by the first-entry ledger;
3. the density change to the static kernel must retain the factor \(d\);
4. occurrence repeats must use the occurrence-labelled multiplicity.

Thus Theorem 4.1 is a valid implication, not an independent proof of this
coefficient identification.

## 5. Lower queue holonomy

The two-block support calculation agrees with the earlier private-order
audit.  Swapping adjacent old deletion labels changes:

* one current lower state;
* one next-block owner state in each of the \(h\in\{2,3\}\) copies; and
* no later state, because the next outgoing queue uses the next deletion
  order.

The support is \(1+h\le4\).  Since the entire change is one global
coordinate conjugation, complete-row polarization pays it without a
size-four cluster **provided the conditional complete-row ledger in
Section 4 is available**.  This implication passes.

## 6. Marked scope

For a family with fixed occurrence roles and every coordinate labelling,
\(h\mapsto\tau h\) is a bijection.  Therefore the raw orbit-summed marked
estimate inherits the unmarked transport.  A single fixed labelled
cylinder does not; its continuation ratio may change.  The annealed
bottom target uses the raw aggregate, but every finite role family still
needs its declared occurrence replay.

## 7. Normalization no-go

The scaling counterexample is decisive.  The current definitions of
\(X_i,\rho_i,\mu_i,g_x^\circ\), and \(\beta_T\) do not use the auxiliary
private-switch conductance.  Multiplying every such conductance by
\(t>0\) leaves those quantities fixed and sends
\(\alpha_i\mapsto t\alpha_i\).  Hence the present premises cannot imply

\[
                         \frac{X_i(1-a_i)\zeta_i}{\alpha_i}
                         =\Theta(1)
\]

for any already fixed external scalar \(\zeta_i\).

This agrees with the existing private-switch audit: the structural
generator was rescaled to represent the Johnson Laplacian, but its edge
weights were not identified with the actual stopped Bellman
coefficients.

The conditional degree/incidence double count also passes.  If the
literal edge conductance is comparable to \(\mu_A\), then

\[
 \alpha_i^{\rm tr}
 \asymp\frac{\sum_A\mu_As_T(A)}{N_T},
 \qquad
 \beta_T
 =\frac{\sum_A\mu_An_T(A)}{\sum_xY_x}.
\]

Good loads and \(s_T(A)\asymp n_T(A)\) imply
\(\alpha_i^{\rm tr}\asymp\beta_T\).  This closes the scalar ratio
conditionally.

Neither premise is currently automatic on the stopped fibre.  In
particular, a positive-weight row can have every private mate unavailable;
then it contributes to \(\beta_T\) but has switch degree zero.  Also, a
trace comparison cannot imply positive-operator domination: conductance
may be concentrated on one Johnson star.  Therefore the live-degree and
capacity rows in the theorem are genuine additional requirements, not
consequences of good resource loads.

## 8. Exact remaining row

An unconditional closure needs the literal coefficient theorem

\[
 K_T^*\Lambda_iK_T=L_{T,i}^{0},
 \qquad
 K_T^*\Lambda_{i,\partial}K_T=A_{T,i},
 \qquad
 0\le\Lambda_{i,\partial}\le\Lambda_i,
\]

with the conductance of each private switch derived from the same
hypothetical-next coefficient appearing in the Duhamel boundary.

It must additionally prove either the displayed live-degree condition
(DEG) plus the operator aperture (CAP), or a direct capacity-faithful
domination which implies both.

Once that is written, capacity faithfulness follows by positive-operator
order.  If the external scalar removed in the definition is exactly the
orbit scalar, the service ratio reduces to the already proved
\(X_i(1-\rho_i^2)=2+o(1)\).

Until then, the proof-safe status is:

\[
\boxed{
\text{transported complete-row energy: conditionally closed;}
\quad
\text{coefficient-faithful switch normalization: open}.}
\]
