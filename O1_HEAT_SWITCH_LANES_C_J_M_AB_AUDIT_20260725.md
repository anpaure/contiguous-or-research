# Full proof audit: O(1) heat/switching lanes C, J, M, and AB

Date: 2026-07-25

Scope: complete mathematical audit of the latest proof bodies in lanes C, J,
M, and AB.  No computation, solver, or web input was used.  This note also
reconciles the reports chronologically: several statements which were honest
when written are superseded by the later theorem in AB7.

## 1. Common normalization

Write

\[
n=2m+1,\qquad W=\binom nm,\qquad B=W/n=\operatorname{Cat}_m,
\qquad H=\lceil A\sqrt m\rceil .
\]

At depth \(q\), put \(W=c_qN_q+r_q\) and

\[
Q_q(F)=\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1)=2\Phi_q(F).
\]

Lanes C, J, and M use

\[
\mathcal Q_H(F)=\sum_{q\le H}\frac{Q_q(F)}{c_q},
\]

while AB7 uses

\[
\mathfrak F_A(F)=\sum_{q\le H}
\frac{\Phi_q(F)}{\binom{c_q+1}{2}}
=\sum_{q\le H}\frac{Q_q(F)}{c_q(c_q+1)}.
\]

On a fixed Gaussian window \(c_q\le K_A\), so the two objectives are
uniformly equivalent:

\[
\boxed{
\frac{\mathcal Q_H(F)}{K_A+1}
\le \mathfrak F_A(F)
\le \frac{\mathcal Q_H(F)}2.}
\tag{1.1}
\]

This comparison is the key to reconciling J with the later AB7 theorem.

## 2. Lane C

Audited files:

- `MATH_ATTACK_C_U1_INDEX_CORRECTION_20260725.md`;
- `MATH_ATTACK_C_CELL_TRACE_NOGO_20260725.md`;
- `MATH_ATTACK_C_MSW_CELL_VARIANCE_FLOOR_20260725.md`;
- `MATH_ATTACK_C_COMPONENT_NOISE_HARMONICS_20260725.md`.

### 2.1 Component margins and Johnson indexing — verified

For every ownership component \(K\), its two sides have the same number of
wreath rows.  Each row has total rank-\(r\) mass \(n\) and point margin
\(r\).  Consequently every innovation \(\Delta_{K,q}\) has zero total and
zero point margins.  Hence

\[
\Pi_{U_0}\Delta_{K,q}=\Pi_{U_1}\Delta_{K,q}=0.
\]

For a transposition overlay, \(R_K=\tau L_K\), so
\(\tau\Delta_{K,q}=-\Delta_{K,q}\).  The proof that every row has a
\(\tau\)-fixed middle mask is sound: the two swapped coordinates have
\(2m=n-1\) incidences among the \(n\) middle windows, so not every window
can contain exactly one of them.

**Verdict:** correct.  The first possible slow module is the ordinary Johnson
\(U_2\), with transposition rate \(2/n\).  Any report calling this mode
\(U_1\) must explicitly mean the quotient reindexing after removing ordinary
\(U_0\oplus U_1\).

### 2.2 Exact cell trace — verified

On one intrinsic fixed-\(\tau\) cell, write

\[
f(F_\sigma)=p+\frac12\sum_K\sigma_Kd_K.
\]

The invariant and anti-invariant parts are orthogonal.  Direct sign averaging
gives

\[
\boxed{A_{\tau,H}(F_\sigma)-V_{\tau,H}
=4\bigl(\mathcal Q_H(F_\sigma)-\overline{\mathcal Q}_{\mathcal C}\bigr).}
\tag{2.1}
\]

The same identity holds rankwise and harmonic by harmonic.  In particular,
the cell-average gap is exactly zero.  The switching-cell equivalence is
closed under all sign changes; possible degenerate components merely give a
constant corner multiplicity and do not change the trace calculation.

**Verdict:** correct.

### 2.3 Integer floor and Gaussian asymptotic — verified

The identity

\[
Q_q=\|\mu_q-(W/N_q)\mathbf1\|_2^2
-N_q\theta_q(1-\theta_q)
\]

is exact.  The Riemann-sum computation

\[
\frac1{W\sqrt m}\sum_{q\le A\sqrt m}\frac{\beta_q}{c_q}
\longrightarrow
\int_0^A
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
{e^{x^2}\lfloor e^{x^2}\rfloor}\,dx
\]

is sound; the apparent discontinuities vanish at integer crossings.  Thus the
slow \(U_2\) floor replenishment is exactly on the \(HB\) scale.

**Verdict:** correct.

### 2.4 Genuine MSW cell variance — verified, conditional only on the
previously audited MSW component parametrization

The four-arm formula gives squared profile norm four at depth one and eight
at depths \(2,\ldots,H\) for each of \(\operatorname{Cat}_{m-2}\)
sealed size-two components.  The prefix/suffix distinctness argument is
correct in the stated rank range.  Hence

\[
V_{\tau,H}\ge \operatorname{Cat}_{m-2}
\left(4+8\sum_{q=2}^H\frac1{c_q}\right)=\Theta_A(HB).
\]

The resulting no-go for a fixed multiplicative comparison of \(V\) with
\(A\), with sub-mesoscopic slack, is valid.  It does not by itself bound
\(V-A\) at an individual corner.

**Verdict:** correct within the audited canonical MSW hierarchy.

### 2.5 Scope correction forced by AB7

The C reports state that the pointwise-in-\(\tau\), energy-dependent gate was
not contradicted because no exact high-mean cell was known.  That statement is
now obsolete.  AB7 proves an intrinsic MSW \((2\ 3)\)-cell on which every
integral corner has \(\mathfrak F_A/W\to\infty\).  By (1.1), the cell mean of
\(\mathcal Q_H\) is also \(\omega(W)\).  Averaging a hypothetical pointwise
gate

\[
A_{\tau,H}-V_{\tau,H}
\ge \frac{4\eta_A}{n}\mathcal Q_H-rac{4C_A}{n}HB
\]

over that cell gives a contradiction.  Thus:

- a universal **fixed/prescribed-transposition** energy-dependent heat gap is
  false;
- the direct local-minimum theorem requiring local minimality for **every**
  transposition is not refuted;
- the uniform-transposition average and adaptive multistep gates remain open.

### 2.6 Retention recommendation

**Retain lane C.**  Its cell-centering identity, correct \(U_2\) indexing,
and all-transposition local-minimum formulation are foundational and remain
distinct after AB7.  Amend its status with Section 2.5 above.

## 3. Lane J

Audited files:

- `MATH_ATTACK_J_MSW_DEGREE2_CUBE_ENERGY_AUDIT_20260725.md`;
- `MATH_ATTACK_J_CONSTANT_ONE_CIRCUIT_AUGMENTATION_20260725.md`;
- `MATH_ATTACK_J_UNIVERSAL_CIRCUIT_PARITY_NO_GO_20260725.md`.

### 3.1 Exact degree-two cube and Bernoulli rounding — verified

The universal four-arm circuit is a genuine two-for-two middle trade.  For a
conflict-free atlas, all Boolean corners are exact factors and the real cube is
nonnegative.  Independent Bernoulli rounding gives exactly

\[
\mathbb E\mathcal Q_H(F_X)
=\widetilde{\mathcal Q}_H(x(t))
+\alpha_H\sum_Rt_R(1-t_R),
\]

without requiring cross-generator orthogonality.  The toll \(D_H/4\) in the
unhalved normalization is correct.

The one-flip local-minimum theorem is also correct: retaining the full squared
norm in the quadratic expansion avoids the usual false orthogonality step.

**Verdict:** correct and useful as a general rounding lemma.

### 3.2 \(\mathrm{FCE}_A\) implication — logically correct, but its premise is
now disproved

If the continuous minimum were \(O_A(HB)\), J's rounding theorem would indeed
produce an integral exact factor with \(\mathcal Q_H=O_A(HB)\), hence MWB and
coefficient one.  This conditional implication is correct.

However AB7 proves that every integral vertex of the **full** intrinsic
\((2\ 3)\)-cell satisfies

\[
\mathfrak F_A(F)\ge L_m,
\qquad L_m/W\to\infty.
\]

J's degree-two cube is a subcube of this full cell.  By (1.1), every one of its
integral vertices satisfies \(\mathcal Q_H(F)\ge2L_m\).  Applying J's own
Bernoulli identity to any real cube point gives

\[
\boxed{
\widetilde{\mathcal Q}_H(x(t))
\ge2L_m-D_H/4.}
\tag{3.1}
\]

Since \(D_H=O(HB)\) and \(L_m/(HB)\to\infty\), equation (3.1) disproves
\(\mathrm{FCE}_A\) for every fixed \(A>0\).

This is stronger than J's immutable-hole necessary condition.  The report's
statement that no all-dimensional contradiction to \(\mathrm{FCE}_A\) was
known was accurate before AB7, but is no longer current.

### 3.3 Parity kernel and universal-circuit census — verified

For even \(m\), the dihedral stabilizer of an unoriented odd cyclic order is
contained in \(A_n\), so cyclic-order sign is well defined.  Pairing orders by
a transposition inside \(S\) or \(S^c\) proves \(B_r\epsilon=0\) at every
rank.  The displayed universal two-for-two circuit contains one row of each
sign on both sides, so it preserves the negative-row census.

The orbit-sum identity and the consequent failure of whole-fibre generation
are sound, conditional only on the cited genuine size-three MSW component
stratum.  The conclusion concerns the known universal circuit family, not all
degree-two trades.

**Verdict:** correct method no-go, but not a positive O(1) route.

### 3.4 Retention recommendation

**Archive lane J after merging its rounding lemma and parity invariant into the
handoff.**  Its sole positive completion premise \(\mathrm{FCE}_A\) is now
rigorously false by AB7.  The exact Bernoulli and local-descent lemmas remain
valuable reusable tools, but the lane itself no longer has a surviving route to
coefficient one.

## 4. Lane M

Audited file:

- `MATH_ATTACK_M_HARMONIC_FLOOR_COMPONENT_NOGO_20260725.md`.

The external owner input used in its strongest floor-collision theorem was
also checked in Section 2.1 and Section 9.1 of
`MATH_ATTACK_P5_AFR_BRIDGE_SELECTION_20260725.md`.

### 4.1 Harmonic cell trace and all-depth profile — verified

The levelwise identity \(\mathbb E_{\rm corners}A_{q,j}=V_{q,j}\) is the same
correct cell trace as in lane C.  The canonical four-arm profile gives the
stated \(4,8,\ldots,8\) norms and the Catalan-scale raw variance.

### 4.2 Rectangle spectrum — verified

For the depth-one rectangle, down-incidence to pairs has norm four, and its
squared singular value on \(U_2\) is
\(\binom{n-4}{r-2}\).  Thus the projection formula \(4/\alpha\), not
\(4/\alpha^2\), is correct.  The Johnson Dirichlet calculation
\(4d+8\) is also correct: four internal opposite-sign edges contribute
sixteen and the boundary contributes \(4(d-2)\).

### 4.3 Pair floor and parity--Johnson identity — verified

At fixed pair sum, the adjacent-integer excess is

\[
G_p=\frac{D_p^2-(D_p\bmod2)}{2c_q}.
\]

Fair component signs replace \(D_p^2\) by \(\sum_Kd_{K,p}^2\), giving the
stated restitution.  Summing over Johnson edges yields exactly

\[
\sum_\tau G_{\tau,q}
=\frac1{2c_q}
\bigl(\langle f_q,L_qf_q\rangle
-\langle p_q,L_qp_q\rangle\bigr).
\]

This is a genuinely nonlinear floor correction; assigning it to one harmonic
of \(f_q\) would be invalid.

### 4.4 Catalan harmful floor collision — verified subject to the cited owner
classification

The owner theorem supplies a private odd component on each of two even-parity
target pairs.  Since their total imbalance is even, each private odd term
forces a second odd component term.  Therefore each pair contributes at least
one unit of restitution, and the \(2\operatorname{Cat}_{m-4}\) lower bound is
correct.  The conclusion is fixed-\(\tau\): a floor-corrected strict comparison
with only \(O_A(HB/n)=o(B)\) restitution is impossible.

### 4.5 Quantifier scope — verified

M does not refute uniform-transposition averaging: one bad transposition has
weight \(\Theta(n^{-2})\).  Its stationary replenishment identity is correct
and shows that the still-open averaged gate already contains a classwise
low-energy theorem.

### 4.6 Distinctness and retention recommendation

M is mathematically sound, but much of its fixed-cell no-go is subsumed by the
stronger AB7 theorem, which allows the best correlated cut and produces a
super-high-energy locked cell.  M's genuinely distinct reusable contribution is
the parity--Johnson identity and its nonlinear floor interpretation.

**Recommendation with a 16-thread cap:** archive lane M after merging the
parity--Johnson identity and stationary-replenishment formula into the retained
C/AB notes.  If the project prioritizes harmonic diagnostics over breadth, M
can replace C, but retaining C, M, and AB separately is redundant.

## 5. Lane AB

Audited files:

- `MATH_ATTACK_AB6_DISTINCT_BRIDGE_SCHEDULE_20260725.md`;
- `MATH_ATTACK_AB7_FACTORIAL_DUPLICATE_MIXING_NO_GO_20260725.md`.

### 5.1 AB6 distinct bridge schedule — verified

The native edges \(\tau_s=(2s+2\ 2s+3)\) are pairwise vertex-disjoint, and
the first-run Dyck prefixes make the packet owners row-disjoint across all
stages.  The shifted Catalan pile calculation is correct; in particular, the
private marker must be taken in \(\mathsf B(P_s)\) for \(q\le s\) and as
\(n\) for \(q>s\).  The constants in

\[
\|D_s\|_H^2>36Hk_s,\qquad
V_s\le(8H-4)k_s,
\qquad \Lambda_s>(28H+4)k_s
\]

check exactly.

The balanced-block covariance is \(-1/(k-1)\) for even \(k\) and \(-1/k\)
after adding a zero dummy for odd \(k\).  Backward coherent sign choice then
gives the stated unconditional stage gain.  The report correctly warns that
conditional stage gain may be negative and that deterministic extraction
preserves only total gain.

The odd-stage subgroup release theorem and constants also check.  It is a
second lower bound, not a capture-ratio theorem.  The owner-capacity and native
matching obstructions are correctly scoped.

**Verdict:** correct positive partial theorem.  It gives a linear number of
distinct fresh bridge labels, but only a geometrically depleted total packet
supply and no arbitrary-start or capture theorem.

### 5.2 AB7 duplicate--mixing ledger — verified

For a component cut, direct expansion on each moved target pair gives

\[
\Phi_q(F)-\Phi_q(F^I)
=(x_I-y_I)(x_{\bar I}-y_{\bar I}),
\]

which is exactly same-target duplicate separation minus opposite-target
mixing.  The fair residual normalization, all-transposition Johnson ledger,
and coefficient \(2/n\) all check.  The sufficient hypothesis controlling
\(X_A^{\rm fac}\) remains unproved.

The singleton-fragmentation formula is correct: a cyclic row has exactly
\(n\) Johnson-adjacent cyclic-window pairs for \(2\le r<n/2\), and legal
coarsening adds \(I^{\rm opp}-I^{\rm dup}\).  The constant
\(\sqrt2-1\) follows from the exact maximum
\(\max_{c\ge1,\theta}\theta(1-\theta)/(c+\theta)=3-2\sqrt2\).

### 5.3 AB7 same-overlay no-go — verified

At depth \(H\), the Catalan packet pile supplies
\(\operatorname{Cat}_{m-H-2}\) distinct moved target pairs, each with
cell-invariant pair total at least \(\operatorname{Cat}_H\).  Convexity of
pair collisions therefore gives, at every cell corner,

\[
\mathfrak F_A(F)
\ge W\left(\frac{4^H}{2048K_A nH^4}-1\right).
\]

All constant factors in this estimate check.  Choosing a cell minimizer makes
the best correlated complete-component cut have gain zero.  Since the lower
bound grows faster than every polynomial multiple of \(W\), the prescribed
overlay no-go and its inverse-polynomial variants follow.

This theorem uses genuine integral exact factors throughout.  Its one
structural input is the previously audited private-pair four-arm formula; no
independent occupancy or abstract Gram model is involved.

### 5.4 Quantifier scope

AB7 closes

\[
\forall F\,\forall\tau
\quad\text{and every bridge prescribed independently of }F,
\]

including arbitrary correlated cuts within that fixed intrinsic cell.  It does
not close

\[
\forall F\,\exists\tau,
\]

nor adaptive recomputation after moving to genuinely new transpositions.
AB6 is therefore not contradicted: it begins at a specially selected endpoint
and uses a sequence of distinct bridges.

### 5.5 Retention recommendation

**Definitely retain lane AB.**  It contains both the strongest positive
multi-bridge theorem in this family (AB6) and the strongest exact prescribed-
overlay no-go (AB7).  Its surviving all-transposition selector inequality is
one of the cleanest direct O(1) gates left.

## 6. Consolidated theorem status

| Result | Verdict | Current implication |
|---|---|---|
| C: \(U_0,U_1\) vanish componentwise | verified | slow mode is ordinary \(U_2\) |
| C: cell trace \(A-V=4(Q-\bar Q)\) | verified | no intrinsic positive fixed-cell curvature |
| C: MSW raw cell variance \(\Theta_A(HB)\) | verified | refutes multiplicative raw-variance domination |
| J: Bernoulli cube rounding and local descent | verified | reusable exact rounding theorem |
| J: \(\mathrm{FCE}_A\Rightarrow O(1)\) | valid implication | premise now false by AB7 |
| J: parity kernel/census | verified | known universal circuits not a fibre Markov basis |
| M: parity--Johnson floor identity | verified | exact nonlinear smoothing ledger |
| M: fixed-\(\tau\) harmful floor collision | verified with audited owner input | refutes tiny-restitution fixed-\(\tau\) heat |
| AB6: distinct fresh-bridge schedule | verified | positive partial, no capture/arbitrary-start theorem |
| AB7: aggregate duplicate--mixing ledger | verified | exact adaptive selector gate remains open |
| AB7: locked high-energy prescribed overlay | verified | refutes J's FCE and every fixed-bridge capture theorem |

## 7. Recommended 16-thread decision for these four lanes

1. **Keep AB.**  Highest priority.
2. **Keep C**, amended by the AB7 chronological correction.
3. **Archive J** after preserving its rounding and parity lemmas in the
   consolidated handoff.
4. **Archive M** after preserving its parity--Johnson and stationary formulas;
   retain it instead of C only if the project wants one harmonic-toolkit lane
   rather than the cleaner local-minimum lane.

The genuinely surviving mathematical target shared by the retained heat lanes
is adaptive in its quantifiers: select or recompute transpositions from the
current factor, or prove that a factor locally minimal under **all** such cells
already has \(O_A(HB)\) floor energy.  Every fixed/prescribed-overlay version is
now closed.
