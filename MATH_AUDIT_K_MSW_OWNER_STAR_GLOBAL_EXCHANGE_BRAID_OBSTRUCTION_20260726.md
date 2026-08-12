# Audit of the MSW owner-star/all-depth-exchange braid obstruction

Date: 2026-07-26

Audited file:
`MATH_THEOREM_K_MSW_OWNER_STAR_GLOBAL_EXCHANGE_BRAID_OBSTRUCTION_20260726.md`

Method: independent pure-mathematics audit. No computation, finite
search, solver, or web input is used.

## 0. Verdict

The report is valid with the implication scopes stated in its final
version.  The principal result is an obstruction to the **direct**
composition of the incidencewise MSW owner-star lift with the audited
load-neutral complete-frame exchanges.  It is not a no-go for an
external partial-column splice, overlapping growing-rank composition,
or coefficient one.

Four distinctions are essential and are correctly retained.

1. Top margins and complete load vectors are genuine invariants of the
   audited exchange moves; physical word-component count is not claimed
   as an invariant after an additional endpoint-gluing operation.
2. The \(W-o(W)\) MSW objects in the direct lift are individually legal
   witness columns, each certifying one designated phase.  They are not
   asserted to be a jointly selected all-phase factor.
3. The partial-mask run invariant lives in the marked frame-table model.
   A nonlinear coalescence or cross-row endpoint pairing is an additional
   operation outside that model.
4. The dense trap theorem is quantified for each fixed maximum rank
   \(R\).  The formal scale \(R\asymp\log M\) is not asserted as a
   proved lower bound for growing-rank libraries.

## 1. Top-margin and load-fibre audit

For every fixed-core directed-cycle move, including a triangle, the two
shores use one column at each of the same pair tops.  For every coherent
placeholder cube, the two shores use one column at each of the same
\(2^d\) corners.  Therefore

\[
                         T_Az=0
\]

for every root \(A\).  Because the identities are phasewise and use a
common deleted phase and tag schedule, they also satisfy

\[
                         \mathsf Az=0
\]

for the complete phase-refined all-depth matrix.  Thus target loads,
holes, collisions, and floor energies are exactly invariant.  This part
passes without asymptotic qualifications.

For the direct incidencewise lift,

\[
 x_{\rm lift}=\sum_{A,i}e(A,i,\Phi_F(A,D_{A,i}))
\]

has top margin \(|I_A|\), while a factor has top margin one.  Hence no
integer combination of the audited exchanges maps this particular
literalization to a factor.  The conclusion is a missing
assembly/preimage theorem, not a cardinality impossibility for every
possible direct selection of one frame per root.  The report states this
scope correctly.

## 2. Lag-\(H\) holonomy audit

With

\[
 x_i=J_i\setminus J_{i+1},\qquad
 y_i=J_{i+1}\setminus J_i,
\]

a cyclic \(H\)-window loses \(x_i\) and gains \(x_{i+H}\), so necessity
of \(y_i=x_{i+H}\) is immediate.  Conversely that identity gives the
same recurrence as the windows

\[
                         \{x_i,\ldots,x_{i+H-1}\}.
\]

Each \(x_k\) is present from the state immediately after transition
\(k-H\) through the state immediately before transition \(k\), exactly
\(H\) consecutive states.  The two decks therefore agree.  The
insertion permutation is conjugate to rotation by \(H\), with
\(\gcd(M,H)\) cycles of common length \(M/\gcd(M,H)\).  The indexing and
cycle type are correct.

## 3. Provider-star audit

For a \(d\)-cube, compatibility with a target \(D\) requires the fixed
set \(B\) and at least one label from every active pair to belong to
\(D\).  A pair wholly in \(D\) contributes one free bit.  Hence the
intersection is empty or has exact size

\[
                         2^t,
\]

where \(t\le\min(d,H)\).  The bound

\[
                         2^H=o\!\left(\binom mH\right)
\]

follows from \(\binom mH\ge(m/H)^H\) and \(H=o(m)\).

For a fixed \((M-2)\)-core, put \(K=m-H+2\).  The exact numbers of
compatible pair tops are

\[
                         \binom K2,\quad K-1,\quad1,\quad0
\]

according as the number of outside-core labels absent from \(D\) is
\(0,1,2,>2\).  A single directed cycle uses at most \(K\) tops.  These
formulas and all asymptotic comparisons in the report pass.

The thinness conclusion is local.  It forces many packet incidences in
any star-scale construction but does not obstruct their correlated
overlapping transitive closure.  The report preserves this caveat.

## 4. Fixed-rank and frozen-order audits

In a rank-\((R+1)\) long-cycle checkerboard trap, a directed-cycle move
contained in the gadget lies in a two-face.  The fixed placeholder left
in its common core is moved to another gap by the long cycle, so the
required common-core restrictions disagree.  Every coherent subcube of
rank at most \(R\) similarly fixes a placeholder moved by the long
cycle.  The internal isolation proof is exact.

For fixed \(R\), almost all tops partition into such constant-size
gadgets.  Independent generic core orders exclude cross-gadget moves:
the factorial denominator for agreement on \(M-O_R(1)\) core labels
dominates the exponentially many common-core choices and the label
choices for cycles of every length.  This validates the deterministic
existence conclusion by the probabilistic method for fixed \(R\).  No
uniform-in-growing-\(R\) conclusion is audited.

For the frozen global-order table \(\pi_A=\Pi|_{A^c}\), every realized
fixed-core tournament is transitive.  A nontrivial cube would give the
four-corner strict-order cycle

\[
 a_{r,0}<a_{s,0}<a_{r,1}<a_{s,1}<a_{r,0},
\]

so no cube applies.  The exact provider formula

\[
                         r_\Pi(D)=\sum_i\binom{g_i}{H}
\]

is correct, as is

\[
 |\operatorname{supp}r_\Pi|
 \le2m\binom{2m-H}{m-H}
 \le2m\,2^{-H}W=o(W).
\]

This is a valid all-rank isolated low-frame-block/high-hole state.  It
does not assert that the selected global-order frames themselves are the
MSW witness frames.

## 5. Moving-hole boundary

The squarefree four- and eight-top moving-hole exchanges are not in the
load-neutral kernel: they preserve the retained middle vector but have
nonzero lower and upper action.  They therefore evade the load-fibre
part of the obstruction.  They still preserve one complete column at
each touched top, so they do not evade the top-margin obstruction to the
direct incidencewise literalization.  No audited positive-density
charged packing or MSW endpoint-splice theorem currently upgrades them
to the global braid.

## 6. Final audited boundary

The following conclusion is certified:

> Triangle/cycle and coherent higher-cube exchanges are exact local
> braids within an already nonempty, already grouped all-depth fibre.
> They cannot, by direct application to the incidencewise MSW owner-star
> witnesses, construct the first one-frame-per-root lag-\(H\) table or
> recycle its source cuts into \(O(N_H)\) final blocks.

Still open are a direct CCTPF selection, growing-rank overlapping
composition, recyclable catalysts, and a dense moving-hole/endpoint
splice construction.  No coefficient-one conclusion is claimed.
