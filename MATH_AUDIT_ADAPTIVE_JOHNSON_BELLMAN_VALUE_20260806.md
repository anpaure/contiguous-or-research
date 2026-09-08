# Audit of the adaptive Johnson Bellman-value reduction

**Date:** 2026-08-06  
**Scope:** independent algebraic audit of
`MATH_THEOREM_ADAPTIVE_JOHNSON_BELLMAN_VALUE_AND_EQUIVARIANT_HIDING_OBSTRUCTION_20260806.md`

## 1. Resolvent kernel

For a transitive Johnson layer, a commuting operator has constant diagonal.
The multiplicity formula gives

\[
 R(x,x)=|\Omega_q|^{-1}\sum_sm_s
        \widehat\chi_s/\vartheta_s.
\]

Equation (5.34) in the parent theorem is exactly the assertion that this is
`O(1)`.  Positivity gives the off-diagonal bound by a two-by-two principal
minor.  No unproved sector union bound is used.

For Theorem 1.2, averaging the `R`-resistance over directed Johnson edges
gives `2 tr(R(I-P))/|Omega_q|`.  Since `R=L^dagger B` on mean zero and `B`
vanishes on constants, this is `2 tr(B)/|Omega_q|`.  Directed-edge
transitivity makes the average the value on every edge.  The geodesic and
flow bounds are ordinary Hilbert-space triangle inequalities.  They are
exact sufficient tools, not a claim that the required adaptive innovation
flow already exists.

For Theorem 1.3, a uniform coordinate transposition changes a `q`-set with
probability `2q(k-q)/[k(k-1)]` and otherwise fixes it.  Conditional on a
change, every Johnson neighbour is equally likely.  Thus
`I-E(tau)=alpha_q L`.  Since `tau^2=I` and `tau R=R tau`, expanding the two
factors `I-tau` gives `2 alpha_q R L=2 alpha_q B`.  This identity is exact.
The subsequent broken-switch charge remains explicitly unproved.

For Theorem 1.4, every unavailable switched candidate has a unique earliest
selected edge which blocks it.  Availability of the unswitched candidate
forces every common blocker resource to lie in `tau E-E`; coordinate
transposition pairs every non-slot such resource with an adjacent resource
of `E-tau E`.  Slot-only boundary terms stay in the separate slot ledger.
The decomposition is pathwise and remains true after cylinder weighting.
Calling its weighted diagonal `(ROc)` and its multi-entry part `(FE3)` is a
target identification only; the audit confirms that the theorem does not
claim the still-missing coefficient domination.

For Lemma 1.5, a new non-slot collision under a coordinate transposition
yields a Johnson-adjacent ordered resource pair; that pair uniquely determines the
coordinate transposition.  The union bound over at most `R_E R_G` pairs is
therefore exact and gives `O(d^-2)`.  The audit agrees with the warning that
two hits are correlated through the same transposition and are not squared
independently.

Lemma 1.6 uses only monotonicity of availability.  Each switch pair changes
membership state from both live, to at most one live, to neither live, so
its boundary indicator has one positive jump.  The statement is unweighted;
the audit confirms that future-fugacity control of the weight at that jump
remains an explicit open coefficient comparison.

## 2. Equivariant hiding

The calculation

\[
 \langle gf,R(gAg^{-1}-A_0)gf\rangle
 =\langle f,R(A-A_0)f\rangle
\]

is exact whenever `R,A_0` commute with the group.  Thus a hidden global
permutation or prefix stabilizer cannot average the quadratic discrepancy.
This does not rule out a different algorithm with genuinely independent
private relabellings; it shows that relabelling the same stopped state is
not such an algorithm.

## 3. Counterexample

The balanced sign vectors `f_A` have squared norm `N`.  The rank-one
projection `B_A` has trace one and fixes `f_A`.  Its full symmetric-group
average is scalar on the `(N-1)`-dimensional mean-zero representation, so
the scalar is `1/(N-1)`.  The block Laplacian is regular and kills `f_A`.
All claims in Proposition 3.1 follow.

The example is a logical counterexample to an equivariance/degree-only
proof, not a claimed reachable balanced-doublet prefix.

## 4. Bellman identity

Because the full stopped state includes the density index, remaining host,
occurrence labels, and analytical stop flags, its transition law is Markov.
Splitting the future nonnegative cost at the first step proves (4.3).
Tonelli justifies the telescoping even before finiteness is known; the
horizon is finite in the actual process in any case.

`(JVAL)` is exactly equivalent to the unconditioned cumulative payment.
`(JBEL)` is a sufficient hereditary domination, not a claim that the value
has already been bounded.  The note therefore does not claim JSEC or the
balanced-doublet theorem.

## 5. Prefix scope

Unconditional cleanup and a rare unordered carrier cylinder can be
disjoint, so a purely initial-state estimate is insufficient if the output
law is first conditioned on cleanup.  Final fair orientation coins are
independent of unordered cleanup, but a global coordinate permutation is
not.  Restricting heredity to the actual atomic separator-prefix class is
valid for that interface.

There is also a valid unconditioned interface: the raw monotone-quarantine
law already has the hereditary killed-event cylinder, regardless of its
realized cleanup size.  For that route an initial expected cleanup bound is
enough if the downstream theorem consumes expected leave and is proved in
one joint expectation.  The note now records both alternatives and does
not choose between them silently.

## Verdict

The reduction is **PASS**.  It closes no host-specific adaptive estimate.
Its exact gain is to replace the unnecessarily strong absolute rows
`(JRES)`--`(JSW)` by the one-sided selected-relation Bellman row `(JBEL)`
and to rule out global/stabilizer hiding as a proof of that row.
