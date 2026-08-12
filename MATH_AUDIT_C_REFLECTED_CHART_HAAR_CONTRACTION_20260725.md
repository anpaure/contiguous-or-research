# Audit of the reflected-chart Haar contraction

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or experiment is used.

## 0. Verdict

The central construction and its quantitative floor-energy contraction in
MATH_ATTACK_C_REFLECTED_CHART_HAAR_CONTRACTION_20260725.md are correct.
In particular, the extracted mixed corner is a literal exact factor reached
from the prescribed exact factor \(F^*\) by exactly two freshly recomputed
nonempty proper transposition-component cuts, and

\[
\mathcal Q_H(F_{\varepsilon})
\le \mathcal Q_H(F^*)-
\frac{B4^H}{1024M_AH^4}
\]

for all sufficiently large \(m\). The exact adjacent-integer floor cancels
in the endpoint comparison; no fractional factor occurs.

There are three required wording/notation corrections.

1. Not **every** corner is reached by two proper cuts: the corner \(F^*\)
   itself corresponds to two empty cuts. Every corner is reached by at most
   two fresh cuts, while the decreasing mixed corner is reached by exactly
   two nonempty proper cuts.
2. The correlated bundle variance
   \(\sum_R\|d_R-\sigma d_R\|_H^2\) is not, by definition, the ordinary
   component variance of the \(F^*/(\sigma F^*)\) comparison. The latter is
   \(2\sum_R\|d_R\|_H^2<16HB\), which is stronger than the displayed
   \(32HB\).
3. The reflection \(\sigma\) is a fixed-point involution, not a
   transposition. Thus the final high-sector ratio is the exact nonlocal,
   correlated analogue of shield burnout. It is not literally one term of
   the earlier iid-transposition renewal sum. The two actual stages are
   the transpositions \(\tau,\tau'\), but their individual fair-heat
   variances are not bounded by this argument.

These corrections do not alter the energy contraction or the literal
two-proper-cut realization of the selected decreasing endpoint. The theorem
also does not prove escape from an all-transposition local minimum: the
prescribed \(F^*\) is not shown to be locally locked, and its first proper
cut may already decrease energy.

## 1. Exact reachability

For \(R\in\mathcal I\), the two root packets \(U_R\) and \(\sigma U_R\)
are disjoint, as are all packets belonging to distinct indices. On \(U_R\),
\(F^*\) uses \(\tau K_R\); on \(\sigma U_R\), it uses \(\sigma K_R\).

Let

\[
S=\{R:\varepsilon_R=-1\}.
\]

In the fresh \(\tau\)-overlay of \(F^*\), restriction to \(U_R\) is the
same connected two-row component with shores \(\tau K_R,K_R\), possibly
read in reverse. Since \(\tau U_R=U_R\), no overlay edge crosses the packet
boundary. Switching precisely the components indexed by \(S\) therefore
changes \(\tau K_R\) to \(K_R\) exactly for \(R\in S\).

The first cut leaves every \(\sigma U_R\) unchanged. Because
\(\tau'\sigma U_R=\sigma U_R\), the fresh \(\tau'\)-overlay at the new
intermediate factor restricts to the original connected component with shores
\(\sigma K_R,\sigma\tau K_R\). Switching the same index set \(S\) produces
the asserted corner.

If

\[
\varnothing\ne S\ne\mathcal I,
\]

then at each stage at least one displayed component is switched and at least
one is retained. Both cuts are consequently nonempty and proper, regardless
of the remaining components of the overlay. For \(S=\varnothing\), both
cuts are empty. This proves the corrected reachability quantifier.

## 2. Haar identity and the exact floor

Write

\[
D=\sum_Rd_R,\qquad h_R=d_R-\sigma d_R,\qquad
A=\left\|\sum_Rh_R\right\|_H^2,\qquad
V_{\rm bun}=\sum_R\|h_R\|_H^2.
\]

Setwise reflection invariance of the canonical factor gives exactly

\[
f(F_\varepsilon)
=P_\sigma f(F^*)+\frac12\sum_R\varepsilon_Rh_R.
\]

The first term is \(\sigma\)-invariant and the second is
\(\sigma\)-anti-invariant, so they are orthogonal in every Johnson layer.
Fair independent bundle signs give

\[
\mathbb E\|(I-P_\sigma)f(F_\varepsilon)\|_H^2
=\frac14V_{\rm bun},
\qquad
\|(I-P_\sigma)f(F^*)\|_H^2=\frac14A.
\]

At every depth, all exact factors have the same total load \(W\). Expanding
\((\mu-c_q)(\mu-c_q-1)\) therefore shows that the difference of two floor
energies is exactly the difference of their centered squared norms. Hence

\[
\mathbb E[\mathcal Q_H(F_\varepsilon)-\mathcal Q_H(F^*)]
=\frac14(V_{\rm bun}-A).
\]

No term depending on the fractional mean \(W/N_q\), on \(c_q\), or on the
integer remainder \(\rho_q\) has been dropped.

## 3. Constants

For \(d=m-H-2\), the number of retained terminal-chart-free suffixes is

\[
L^\circ=\operatorname{Cat}_d-2\operatorname{Cat}_{d-2}
\ge\frac12\operatorname{Cat}_d
>\frac{B}{2\,4^{H+2}}.
\]

The original and reflected private target families are disjoint: an original
target contains \(2m,n\) and omits \(1\), whereas its reflection contains
\(1,n\) and omits \(2m\). All nonprivate arms omit \(n\). Thus the two
families contribute without cancellation, giving

\[
A\ge\frac{4L^\circ\operatorname{Cat}_H^2}{c_H}
>\frac{B4^H}{128M_AH^4}.
\]

Here one uses exactly

\[
\operatorname{Cat}_H\ge\frac{4^H}{4H^2},
\qquad c_H\le M_A.
\]

For one packet,

\[
\|d_R\|_H^2=4+8\sum_{q=2}^Hc_q^{-1}<8H,
\]

and therefore

\[
V_{\rm bun}
\le4\sum_R\|d_R\|_H^2<32HB.
\]

Substitution in the Haar identity proves the expected gain in the source
report. Since the empty and full bundle choices are \(F^*\) and
\(\sigma F^*\), both of the starting energy, an endpoint attaining the strict
average gain has a mixed sign set. The preceding section then supplies its
two proper cuts.

## 4. High-sector truncation

Let \(P_{\le J}\) denote Johnson degrees \(2,\ldots,J\). The universal
run-cap bound and permutation invariance give

\[
\|P_{\le J}(f(F^*)-\sigma f(F^*))\|_H^2
\le2\mathcal L_J(F^*)+2\mathcal L_J(\sigma F^*)
\le4U.
\]

Consequently

\[
A_\sigma^{>J}(F^*)
>\frac{B4^H}{128M_AH^4}-4U.
\]

The genuine active components of the comparison \(F^*/(\sigma F^*)\)
are, separately, the two-row components on \(U_R\) and on \(\sigma U_R\).
Their component variance is

\[
V_{\sigma,\mathrm{comp}}
=\sum_R(\|d_R\|_H^2+\|\sigma d_R\|_H^2)
=2\sum_R\|d_R\|_H^2<16HB.
\]

Orthogonal projection only decreases this quantity, so

\[
V_{\sigma,\mathrm{comp}}^{>J}<16HB.
\]

Finally,

\[
\frac{U}{B4^H/(M_AH^4)}
=\frac{M_AH^7}{n}e^{-(\log4-\gamma)H}\longrightarrow0,
\]

and \(M_AH^5/4^H\to0\). Hence

\[
\frac{V_{\sigma,\mathrm{comp}}^{>J}}
     {A_\sigma^{>J}(F^*)}=o_{A,\gamma}(1).
\]

This verifies the high-degree truncation and all floor-sensitive constants,
with the scope correction that \(\sigma\) is the nonlocal comparison
involution rather than either one of the two transposition stages.

