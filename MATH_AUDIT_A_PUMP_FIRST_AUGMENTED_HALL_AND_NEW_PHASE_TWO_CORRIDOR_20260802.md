# Audit: pump-first augmented Hall and prospective new-phase two corridors

**Date:** 2026-08-02  
**Lane:** A, common-base/ordered-table certificate after the twisted `C6`
pump is selected  
**Verdict:** PASS after the scope corrections recorded below.  The notes give
an exact reduction and exact cut certificates; they do not prove that an
accepted Boolean table exists.

## 1. Frozen inputs

The audited inputs are:

1. `MATH_THEOREM_ROOT_PROSPECTIVE_NEW_PHASE_BOOLEAN_HEX_TWO_CORRIDOR_REDUCTION_20260802.md`,
   SHA-256
   `3aa2903d61018fba4eee19cacdb0e2174f43e32241fdcf43f9216954cccc891f`;
2. `MATH_THEOREM_A_PUMP_FIRST_AUGMENTED_ORDERED_HALL_DAMAGE_AND_CORRIDOR_AVOIDANCE_20260802.md`,
   SHA-256
   `0313ed9b89c7a4c57a2f5e88d73629b30dd2848c1d9503a5c35e46c8074be8d2`;
3. the Boolean-hex source theorem
   `MATH_THEOREM_K_TWISTED_C6_PUMP_CORRIDOR_ENDPOINT_AND_TERNARY_FUSION_GATE_20260802.md`,
   SHA-256
   `9bd6ee3468e48eae2d1e344dc4c86ecdbc97e617ae9619d98879d870f6668759`;
4. the pump-first Johnson-separation theorem
   `MATH_THEOREM_K_C6_UNIT_PUMP_SEVEN_EAR_PROSPECTIVE_PLANTING_20260802.md`,
   SHA-256
   `7bba1cac18cbfa23223bcf321fa23c5d25167959e1aa41ce73550084c7b711fb`;
5. the endpoint-conditioned ordered-corridor theorem
   `MATH_THEOREM_A_ENDPOINT_CONDITIONED_PHASE_COMMON_CORRIDOR_MATERIALIZATION_20260802.md`,
   SHA-256
   `57512e6b3b7ab175dc1b2e441d0f6641bba1e2bef8616c786bfaf3446ea1a083`.

The root note's original supplied SHA was `3441ebfc...`; intermediate scope
SHAs were `cb126962...` and `badc43d4...`.  The frozen SHA above contains the
independently required central-resource, common-host, two-block, voltage,
Hall-damage, and physical/non-equivariant scope corrections, together with
the corrected Section 4 charge reference and a nonempty candidate family.

## 2. Local Boolean-hex audit

For

\[
 O=\{A\to B,C\to D,E\to F\},\qquad
 N=\{A\to F,C\to B,E\to D\},
\]

the two phases have identical tail and head multisets.  The source Boolean
identity also gives identical lower and immediate-upper colour multisets.
Thus the owner-degree and immediate-palette residual vectors agree exactly
on one declared common host.  Equality of the target vector does not imply
that old- and new-phase-conditioned hosts are identical; the common-host
hypothesis, or direct use of the new-phase host, is load-bearing.

This equality does **not** identify old and new directed seam occurrences.
The corrected root note therefore restricts its vector `r` to the central
owner/lower/immediate-upper/tail/head ledger.  Directed histories,
edge-private tokens, and seam-specific sidecars are tested on the new phase
itself.  This is the strongest valid resource-neutrality statement.

The reduction is for one physical pump edge.  An orbit-closed selection would
open several pump paths and requires a multi-corridor theorem; no such claim
is present.

## 3. Topology and voltage audit

Deleting the old pump seam `E->F` leaves `P_3:F leadsto E`.  A final cycle
containing the three new seams must, and can only, have the form

\[
 A\to F\stackrel{P_3}{\leadsto}E\to D
 \stackrel{Q_1}{\leadsto}C\to B
 \stackrel{Q_2}{\leadsto}A.                          \tag{3.1}
\]

Hence the residual topology is exactly two paths `Q_1:D leadsto C` and
`Q_2:B leadsto A`.  A correct split table must assign residual fragments to
these two roles and retain only within-role forward joins.  Without that
role separation, a matching may pair `D` with `A` and `B` with `C`, producing
two cycles.  The crossed-pair example in Proposition 8.2 is therefore a
literal topology counterexample to untyped Hall.

The voltage identity is also exact only in the corrected form.  The direct
new-phase cycle voltage equals the sum of the three conceptual old closure
voltages

\[
 V(P_3+E\to F)+V(Q_1+C\to D)+V(Q_2+A\to B).          \tag{3.2}
\]

Thus the unit pump closure supplies the desired absolute unit precisely when
the two partner closures have the required total charge.  For one finite
`Z_n` lift, a total residue coprime to `n` is enough to give one lifted cycle.
Exact integer zero background is the stronger row needed when the charge is
exported as a regenerative invariant.  In neither setting does the local hex
make the matching-dependent partner charge automatic.

## 4. Exact Hall-damage audit

Fix the physical hex, the protected pump path, a two-block assignment and
orders, all endpoint states, and a capacity-faithful state expansion.  After
subtracting fixed protected demands, let `B_0^(2)` be the raw block-diagonal
option table and let `F` be the options rejected by history or a zero-residual
join/port occurrence.  For every left shore `S`, put

\[
\begin{aligned}
 D^{(2)}(S)&=\{v\in N_0^{(2)}(S):E_0^{(2)}(S,v)\subseteq F\},\\
 \kappa^{(2)}(S)&=|N_0^{(2)}(S)|-|S|.
\end{aligned}                                        \tag{4.1}
\]

Then

\[
 N_{B^{(2)}}(S)=N_0^{(2)}(S)-D^{(2)}(S),             \tag{4.2}
\]

so Hall is exactly

\[
                    |D^{(2)}(S)|\le\kappa^{(2)}(S)
                    \quad\hbox{for every }S.          \tag{4.3}
\]

This is necessary and sufficient for the two encoded corridors on the fixed
table.  The global min--max `Delta_hex` is exact within its declared
capacity-/charge-faithful candidate family, and globally exact only if that
family contains the literal restriction induced by every physical solution.

An independent three-block derivation gives the same result before
contraction.  Cut the conceptual old seams into pump, `A`, and partner blocks;
prescribe the three new seams cyclically between them; and use a forward table
inside each block.  The pump block is already the fixed path `P_3`, so
contracting it leaves exactly the root note's two variable blocks.  Residual
capacity subtracts the new phase **once**.  The old phase is not also
subtracted; it is only the central-vector and charge identity.  A candidate
with a negative residual coordinate is absent.  All six positive/negative
fixed-seam history tests are part of the endpoint state before Hall is
applied.

The audit also confirms the following qualifications in the A note.

* Four-endpoint deletion proves an at-most-one occurrence row, not arbitrary
  capacity faithfulness.  Exact-one additionally needs the no-avoidance test.
* The closing join and all fixed protected seams must pass history/private
  tests and have their demand subtracted before the residual table is built.
* A fragment endpoint owner is not consumed twice merely because a join is
  incident with it; only separately named join/port occurrences enter the
  zero-residual forbidden bank.
* Hall does not imply a matching-dependent group-charge row.  That row must
  be fixed, state-encoded, or solved jointly.
* Ticket averaging is valid only on one literally aligned physical table,
  after all ticket-level failures are prefiltered or charged edge-locally.

## 5. What is and is not closed

Direct new-phase planting removes two post-hoc gates:

1. finding two functional partners after the owner factor is completed;
2. proving that the three old edges occupy three mergeable components.

It replaces them by the single prospective certificate `Delta_hex=0` on the
two-root/two-sink table.  The pump-first Johnson-ball inequality separately
guarantees a local seven-ear anchor outside the pump bank for
`d=O(sqrt(m))` and large `m`.

No current theorem bounds the accepted two-corridor option loads strongly
enough to force `Delta_hex=0`.  A load-one triangular example in the A note
shows that marginal local ticket loads alone cannot do so.  Common endpoint
histories, integer partner charge, deeper upper shadows, source/envelope
transport, common compiler, and Pascal regeneration remain open.

No heavy computation was used in this audit.
