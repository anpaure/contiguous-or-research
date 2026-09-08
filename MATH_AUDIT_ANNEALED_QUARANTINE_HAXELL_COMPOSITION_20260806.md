# Audit of annealed quarantine--Haxell composition

**Date:** 2026-08-06  
**Audited source:**
`MATH_THEOREM_ANNEALED_QUARANTINE_HAXELL_COMPOSITION_20260806.md`,
SHA-256
`c8bfc8f7073c9d805d238f3b69c4776e1519438be7268b415259108b2651078c`

## 1. Quantifiers

The selected-relation quarantine theorem proves its cylinder by a killed
event induction under the raw clock law.  It does not condition the clock on
the terminal size of the quarantine.  Consequently the factorial-moment and
Laplace estimates used for the bottom option and resource-load tails may be
integrated under that same raw law.

After the exceptional tasks are exposed, the independent-transversal step is
deterministic.  Thus there is no need to preserve a random cylinder after
choosing the Haxell transversal.

## 2. Expectation argument

Under (A2)--(A3),

\[
 \mathbb E(L_0+Q+Y)
 \le L_0+C_QM/d+o(M/d).
\]

All three variables live on one finite probability space.  Hence one outcome
has total charge at most this expectation.  The pointwise clause in (A3)
then completes every task not counted by `Q+Y`.  No union bound and no
positive lower bound on
`Pr(Q<=CM/d | F)` is used.  Theorem 2.1 is therefore correct.

The unit conversion caveat in the source is necessary: if `Q` counts macros
and `Y` counts tasks, each must first be multiplied by its deterministic
maximum lower-resource cost.  The stated theorem already requires this.

## 3. Bank conditioning

The application of the abstract theorem is valid only with the pre-reserved
banks in the initial sigma-field.  In that formulation the quarantine
cylinder is applied conditionally on the banks, and every marked block type
used by the bottom moment calculation must be among the quarantine tests.
These are hypotheses, not consequences of the annealed expectation
argument.

## 4. Downstream scope

Selecting a low-`Q+Y` outcome destroys the random output law.  This causes no
problem for the bottom option-tail/Haxell use, because Haxell completion is
pointwise.  It would be invalid to reuse a hereditary cylinder from the
chosen deterministic outcome in a later randomized theorem.

In particular, the still-open terminal component-joining row must be one of:

1. a pointwise invariant of every retained outcome;
2. a deterministic completion after the outcome is fixed; or
3. another nonnegative loss/failure variable included in the same annealed
   total before choosing the outcome.

The annealed theorem does not itself prove component joinability.

The added Corollary 2.2 is correct.  For a terminal event `J` with
`Pr(J)>=eta`, nonnegativity gives

\[
 \mathbb E[Q+Y\mid J]
 \le {\mathbb E(Q+Y)\over\eta}.
\]

Choosing an outcome inside `J` below this conditional mean proves the
stated fixed-factor loss.  No independence is needed.  Thus a component
joiner available on an unconditionally constant-probability terminal event
may be folded into the same annealed selection.  A rare event, or one whose
probability is known only after conditioning on cleanup, is not covered.

## Verdict

**PASS**, for the claimed bottom use.  It proof-safely replaces the
separator-cylinder-weighted cleanup requirement by the raw expectation

\[
                 \mathbb E(B_0+B_1)=O(M/d^2).
\]

It does not provide a conditioned cleaned law and must not be cited for a
later step that requires such a law.
