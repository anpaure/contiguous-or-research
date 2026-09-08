# Audit of Lane K13: the (q\ge2) hereditary collision frame

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, web search,
SAT, or solver is used.

Audited file:
`MATH_ATTACK_K13_QGE2_HEREDITARY_COLLISION_FRAME_20260725.md`.

## 0. Verdict

The report contains a correct literal obstruction on the autonomous token
ledger, and it correctly incorporates the audited owner-fixed spike chart.
Its strongest valid conclusion is

\[
 \boxed{\text{no complete signed, descent-valid hereditary frame exists
 for adjacent plus owner-fixed switches.}}
\]

This conclusion remains valid for literal low-run words after one additional
boundary debit described below. It does **not** refute either

1. a raw numerical frame at one fixed standard all-depth weighting, or
2. the upper-only, drift-corrected frame.

The following correction is needed before the word ``literal'' is used for
the completed contiguous-word obstruction. The standard initialization
collars add (O(HJ)) flag occurrences, whereas Section 5 subtracts only the
(W-T) completion occurrences. Thus the exact post-completion equality in
(5.8), and the exact lower bound (5.7) as stated for every literalization,
are too strong. Under the report's hypothesis

\[
 J=O(W\log ^2m/m),\qquad H\log ^2m=o(m),
\]

one has (HJ=o(W)). Therefore the corrected literal bound is still

\[
 Q_{2,\mathrm{lit}}^-
 \ge
 2Z_2^-(M_0)-2(W-T)-O(HJ)
 =(1/32-o(1))W.
\]

This repairs the theorem without changing its asymptotic constant or its
architectural conclusion. The sentence saying that the conclusion remains
true after deleting the run restriction is justified only on the autonomous
token ledger. For a literal word the (HJ=o(W)) hypothesis must be retained,
since unrestricted fragmentation can emit enough collar occurrences to
destroy the displayed hole count.

Subject to these two scope corrections, the report passes.

## 1. Adjacent-visible census

For a loaded upper target (U) in the coherent first-avoided state, its
phase is uniquely

\[
 \kappa(U)=\min\{j:U\cap P_j=\varnothing\}.
\]

Indeed, a phase-(j) root meets every earlier pair, the upper target contains
the root, and the complete local row avoids (P_j). Hence every occurrence
of the same (U) belongs to the same phase.

For an occurrence over (S), the adjacent (j)-chart moves it exactly when

\[
 \varnothing\ne U\cap P_{j+1}\subseteq U\setminus S.
\]

Thus (a_{j,q,U}) in (1.4)--(1.5) is the exact movable multiplicity. With

\[
 I_q=\sum_U\left[\binom{x_{q,U}}2-
                      \binom{a_{\kappa(U),q,U}}2\right]
\]

and (\Phi_q^+=\sum_U\binom{x_{q,U}}2-p_q^{\min}), direct cancellation gives

\[
 \mathcal C_{{\rm all},q}
 =\Phi_q^+-(I_q-p_q^{\min}).
\]

There is no missing floor term or factor two. The phrase ``collision pairs
split into the two movable occurrences'' should only be read as ``pairs of
two movable occurrences.''

The (q=1) vanishing is exact. If two occurrences share (U), exactness of
the local factor forces their two-point collars to be disjoint. Joint
visibility would put the nonempty set (U\cap P_{j+1}) in both collars.
Therefore (a_{j,1,U}\le1), and every adjacent (q=1) charge is zero.

The odd/even statement is also normalized correctly: the two parity layers
partition the full adjacent census, so one captures at least one half. The
run and new-boundary costs are respectively (2r_{\rm parity}) and
(4r_{\rm parity}), with

\[
 r_{\rm parity}=O(W\log ^2m/m)=o(W/H).
\]

## 2. Owner-fixed spike quantifiers

The report incorporates all material corrections from
`PAIR_OMISSION_OWNER_FIXED_SPIKE_CHART_AUDIT_20260725.md`.

Fix a hub (A). For every distinct leaf (B), one bijection (B\to A)
must be fixed once, and the one attached factor must be

\[
 F_B=\theta_BF_A.
\]

Repeated use of (B) must use that same (\theta_B). Distinct leaf pairs
may overlap: they index distinct omitted-pair universes and cause no
one-hub consistency problem.

If (B\subset U_q\setminus Y), then the old phase-(A) row avoids (A),
while (B\cap Y=\varnothing). Hence

\[
 \theta_BS=S,\qquad \theta_BY=Y.
\]

The replacement fixes the unlabelled central edge pointwise and therefore
preserves lower saturation and middle injectivity under arbitrary choices
at distinct central edges. It changes row provenance and does not prove
labelled synchronization.

At depth (p), put (d_{i,p}=\delta_{\theta_{B_i}U_i}-\delta_{U_i}). The
correct identity is

\[
 \langle d_{i,p},d_{k,p}\rangle
 =\mathbf1_{\{d_{i,p}\ne0,d_{k,p}\ne0\}}
 \left(
  \mathbf1_{\{U_i=U_k\}}+
  \mathbf1_{\{\theta_{B_i}U_i=\theta_{B_k}U_k\}}
 \right)\ge0.
\]

The vanishing-column indicator is essential and is present in the K13
report. At the distinguished common target (U_q=U), every column is
nonzero and therefore

\[
 \Gamma_{\rm sp}\ge w_q^+t(t-1).
\]

For doubled factorial-floor energy the exact Haar identity is

\[
 \mathbb E Q(M_\varepsilon)-Q(M_0)
 =\frac{Q(M_1)-Q(M_0)}2-\frac{\Gamma_{\rm sp}}4.
\]

Thus raw Gram curvature is below the coherent endpoint average, not
necessarily below the current all-old endpoint. The report correctly uses
the drift-corrected quantity and correctly leaves corner-dependent
completion and collar terms outside the identity.

Switching (t) tokens adds at most (2t) selected runs, at most (4t)
new raw run endpoints, and (O(Ht)) initialization positions. In the
proper-window range, a common (U) occurs at most once in each row, so

\[
 t\le R_m=\operatorname {Cat}_{m-1},
 \qquad 2t<C_m.
\]

These are single-spike bounds. They cannot be summed over a diffuse family
without paying for its distinct leaf-row blocks.

## 3. Diffuse carrier and factor-consistency ceilings

For one row and one fixed leaf (B), the starts satisfying
(B\subset D_q^Y(i)) form at most one cyclic interval of length at most
(q-1). Consequently (M) switched occurrences require at least

\[
 M/(q-1)
\]

leaf-row blocks. A positive-density bounded-multiplicity (q)-collision
sector therefore costs (\Omega(W/q)\ge\Omega(W/H)) blocks. This is a
valid architecture ceiling, not a statement about concentrated spikes.

The path-versus-star calculation also checks algebraically:

\[
 F_3=\theta_{23}\theta_{12}F_1=\theta_{13}F_1
 \quad\Longrightarrow\quad
 \theta_{13}^{-1}\theta_{23}\theta_{12}
 =\theta_{23}\in\operatorname {Aut}(F_1).
\]

What is forced is the displayed automorphism condition. The word
``forbidden'' requires a separate assertion that the chosen (F_1) has no
such two-block automorphism. The report only uses this paragraph to explain
why compatibility is not automatic, for which the conditional formulation
is sufficient.

## 4. Canonical lower-depth-two defect

Theorem 4.1 is valid. Phase one selects every start of the canonical MSW
factor on the (2m-1)-point universe (Q_1). The marked-gap theorem gives
at least

\[
 A_m\left[
 \frac{m(m-1)}{4(2m-3)(2m-1)}-\frac2{m+1}
 \right]
\]

missing rank-((m-2)) targets. This is a deliberately weakened version of
the available marked-gap coefficient and is therefore safe.

Every such target avoids (P_1). If a phase-(h>1) token fills it, its
rank-((m-2)) lower flag has category below that of its root. The departing
coordinate must be the unique root coordinate in one of
(P_1,\ldots,P_{h-1}). Each coordinate departs once in a cyclic row, giving
at most (2(h-1)) candidate fills per row. Thus phases (2\le h\le t_0)
fill at most

\[
 R_mt_0(t_0-1)
\]

holes. The category tail fills at most

\[
 4C_0\sqrt m\,A_m(3/4)^{t_0}.
\]

Since (A_m/W\to1/4), the bracket tends to (1/16), and both debit terms
are (o(W)). Hence

\[
 Z_2^-(M_0)\ge(1/64-o(1))W.
\]

This is an actual first-avoided fixed-factor token matching, rather than an
ambient histogram witness.

## 5. Floor normalization and persistence

For autonomous mass (T),

\[
 \frac{T}{N_2^-}=\frac{m+3}{m-1},
 \qquad N_2^-=\binom{2m+1}{m-2}.
\]

For all sufficiently large (m), the floor levels are one and two, and the
doubled polynomial is

\[
 Q_2^-(x)=\sum_R(x_R-1)(x_R-2).
\]

Every zero contributes exactly two and every integral summand is
nonnegative. Therefore

\[
 Q_2^-(M_0)\ge(1/32-o(1))W.
\]

Also (W-T=2W/(m+2)), and the completed mass still has floor levels one
and two for (m\ge8). Adding one occurrence can fill at most one old hole.
This verifies the (W-T) debit in Section 5.

Every adjacent generator fixes its root because that root avoids both
exchanged pairs. Every owner-fixed generator fixes its root and owner by
construction. Since every lower flag is a subset of the root, all
autonomous lower flags are pointwise invariant under arbitrary dependent
sequences of these generators. Thus (5.8) is exact on the autonomous token
ledger.

For a literal word, however, every selected-run cut emits a standard
(H)-entry initialization collar. Those added positions can fill lower
holes even though the autonomous tokens are fixed. The safe completed
count is

\[
 Z_{2,\mathrm{lit}}^-
 \ge Z_2^-(M_0)-(W-T)-O(HJ).
\]

Because (HJ=o(W)), this retains the same asymptotic (1/64) hole
constant and (1/32) doubled-energy constant. Exact equality of the
literal lower histogram across mixed corners is not established when the
collars depend on the corner.

## 6. What Theorem 6.1 does and does not refute

On any fixed literal factor system there are finitely many token matchings.
The closure under compatible adjacent and owner-fixed generators preserves
the autonomous lower defect. Choose a state of minimum complete energy in
that closure. No legal reachable corner has positive descent there, while
the invariant lower (q=2) term is (\Omega(W)). Since

\[
 HC_m=\frac{HW}{2m+1}=o(W),
\]

no descent-valid charge can satisfy

\[
 \mathfrak D(M)\ge
 \eta\bigl(\mathcal Q_{\ge2}(M)-CHC_m\bigr)
\]

at every reachable state. The finite-minimum argument is correct and does
not require the generators to commute.

There are three different frame statements, and they must not be merged.

1. **Complete signed, descent-valid frame.** Refuted by the preceding
   argument for the adjacent-plus-owner-fixed architecture.
2. **Raw complete signed frame uniform over nonnegative signed-depth
   weights.** Refuted numerically by choosing only (w_2^-=1), because all
   proposed innovations have zero lower projection.
3. **Raw frame for one fixed standard all-depth weighting.** Not refuted.
   Positive upper Gram may numerically cross-pay invariant lower excess,
   even though endpoint drift prevents it from certifying descent.
4. **Upper-only drift-corrected frame.** Not refuted and remains exactly
   the gate stated in (7.5).

The obstruction also applies only to spikes whose central owner and root
are fixed. A broader legal menu containing genuine lower-moving charts is
outside Theorem 6.1 and is exactly what the theorem says is necessary.

For the autonomous token energy, the run hypothesis is irrelevant to the
invariance. For literal words it cannot simply be deleted: the proof that
the collar debit is (o(W)) uses (HJ=o(W)).

## 7. Terminal phase-(m), (q=2) repair

Theorem 7.1 checks. A phase-(m) root meets each
(P_1,\ldots,P_{m-1}) exactly once and avoids (P_m), so there are

\[
 N_m=2^{m-1}
\]

such roots. For a depth-two occurrence, (B=U\setminus Y) is disjoint
from (Y). It is not a priority pair: every earlier priority pair meets
(Y), while the old row avoids (P_m).

Thus every required (B) is a fresh nonpriority leaf of the one hub
(P_m). Fix one conjugacy per repeated leaf. Overlap between distinct
leaves is harmless.

The new depth-one and depth-two targets are respectively

\[
 Y\cup\{a\},\qquad Y\cup P_m.
\]

They meet every priority pair, whereas every old coherent target avoids its
phase pair. They were therefore empty. Distinct middle owners give distinct
new targets. Moving all but one occurrence of each old target leaves every
old and new depth-two cell at load at most one, so the half-floor collision
drop is exactly

\[
 \sum_U\binom{x_U}{2}.
\]

The depth-one collision energy cannot increase. The added selected-run
cost is at most (2N_m=2^m=o(W/H)). This is a valid static one-sided repair
for the two-upper-depth ledger. It neither moves the lower defect nor
controls the endpoint drift at depths above two.

## 8. Certified boundary

After the literal-collar correction, the following are theorem-grade:

* exact (q=1) adjacent flatness;
* exact adjacent (q\ge2) collar census and parity capture;
* fixed-conjugacy one-hub owner-fixed spikes with nonnegative cross-Gram;
* exact Haar normalization and endpoint-drift correction;
* one-spike (O(H\operatorname {Cat}_m)) context reservoir;
* the diffuse (M/(q-1)) leaf-row-block ceiling;
* a fixed-factor canonical state with
  (Q_2^-\ge(1/32-o(1))W);
* pointwise autonomous invariance under all adjacent and owner-fixed
  generators;
* failure of a complete signed descent-valid hereditary frame;
* the terminal phase-(m), (q=2) upper repair.

The following are not proved:

* a raw fixed-weight numerical frame inequality;
* an upper-only drift-corrected hereditary frame;
* multi-hub factor compatibility and renewal;
* low-run diffuse spike packing;
* a lower-moving literal chart;
* exact corner-independent completed-word histograms.

No coefficient-one conclusion follows.
