# Audit of the PCPS Row-2 turn-factor and safe-opening theorem

**Date:** 2026-08-02  
**Verdict:** proof-correct with the eligibility and phase guards stated in
the theorem note.  The result is a conditional support construction, not an
all-`m` existence proof.

Audited source:

`MATH_THEOREM_K_PCPS_ROW2_TURN_FACTOR_TRANSPARENT_PULL_AND_SAFE_OPENING_20260802.md`.

## 1. Turn-table replay

For `L in binom([2m-1],m-1)`, exactly `m` owners contain `L`.  Choosing two
of them gives a unique Johnson edge with intersection `L`.  One choice at
every `L`, together with owner degree two, is therefore exactly a spanning
Middle Levels two-factor.  No edge can be duplicated under two different
roots, because a Johnson edge has a unique intersection.

The uniform fractional value `1/binom(m,2)` has:

* root load `1`;
* owner load
  \[
       {m(m-1)\over\binom m2}=2;
  \]
* upper-colour load
  \[
       {\binom{m+1}2\over\binom m2}={m+1\over m-1}.
  \]

Thus Proposition 2.1 is exact.  It is only an LP point: connectivity,
integrality, the forced pivot and literal boundary eligibility are absent.

For an integral unguarded table, if `h` upper colours are missing, the
number represented is `U-h`; hence repeat excess is

\[
                       W-(U-h)=C+h.
\]

This independently verifies (2.6).

## 2. Pull-tree topology and palette scope

The incidence-tree induction is valid because every pull changes the same
perfect-matching phase, pull supports are pairwise incidence-vertex
disjoint, and each pull has one deleted edge in every incident old factor
component.  Rooting the incidence tree gives an order in which a pull sees
one accumulated parent component and otherwise fresh child components.
Strictness then merges all of them and never splits a prior component.

The theorem requires equality of the complete **eligible task-label
multiset**, not merely equality of ordinary set-union values.  This is the
correct guard for a boundary/`D` provider restriction.  If a boundary row is
an additional named occurrence rather than one task in the rank-`m+1`
colour shore, the stated counting theorem does not cover it; the note
explicitly exports that case.

The all-dimensional coherent-ECO theorem supplies connected two-section,
not the incidence tree above.  The distinction is necessary.  Likewise the
canonical lexical GMN family cannot be substituted: its audited deficit
exceeds the maximum `3(C_r-1)` turn gain for every `m>=12`.

## 3. Redundant-provider count

Let `E=W-b` eligible occurrences cover all `U` tasks, and let `s` task
classes have multiplicity at least two.  Exactly `U-s` classes are
singletons, so the number of occurrences in repeated classes is

\[
                         E-(U-s)=C-b+s.
\]

When `E>U`, one has `s>=1`, giving the lower bound `C-b+1`.  Hence
`C-b+1>3d` puts a redundant eligible occurrence outside the `3d` protected
roots.  This verifies the strict inequality and the off-by-one.

For `b=0`, `Cat_m>=m` for `m>=3` and `m>=3d+1` imply

\[
                         C+1\ge m+1\ge3d+2>3d.
\]

No analogous automatic claim is made for a guarded shore with large `b`.

## 4. Cycle opening versus path support

At a safe lower root `o`, delete the incidence belonging to the non-
predecessor matching `M_1`.  This point matters: deleting an arbitrary cycle
edge could destroy the fixed perfect predecessor phase.

The incidence cycle becomes one path with lower endpoint `o`.  Suppressing
lower vertices gives all `W` owners and exactly the `W-1` roots other than
`o` as distinct consecutive intersections.  Its owner endpoints are
`M_0(o)` and `M_1(o)`, so

\[
                         o\subset M_0(o)
\]

proves the endpoint aperture.  The task occurrence centred at `o` is the
only lost turn; its duplicate remains.  Since `o` is not a pivot root, no
pivot incidence is deleted.

Relative to `M_0`, the remaining `M_1` incidences form one rooted directed
path.  Every subset is graphic-independent.  Therefore, after availability
has been proved, the protected graphic-Rado inequalities reduce to
nonemptiness of the residual eligible occurrence families.  The theorem
does not use Rado to manufacture an occurrence.

The cycle and path are not interchangeable certificates: the path has one
fewer turn.  The redundant-provider argument is the exact bridge.

## 5. Private absorber audit

After fewer than `h` circuits have been selected, each prior circuit
eliminates at most `Delta` candidates from the next family.  Thus fewer than
or equal to `(h-1)Delta` candidates are blocked, and the strict inequality
`q>(h-1)Delta` leaves one.  Pairwise vertex-disjoint circuits commute and
the declared untouched reserve preserves every formerly represented task.
The lemma is exact but deliberately strong; no Boolean degree/codegree bound
establishing its hypotheses is claimed.

## 6. Final scope

The note proves the implication

\[
 \text{protected upper-covering factor + transparent strict pull tree}
 \Longrightarrow
 \text{rooted Row-2 path with full task availability}.
\]

It does not prove the left side in all dimensions.  In particular it does
not prove `PUTP`, `PCS`, a source antecedent, global address/history replay,
ambient residence, deeper upper shadows, compiler feasibility, or
regeneration.  No finite computation was used in this audit.
