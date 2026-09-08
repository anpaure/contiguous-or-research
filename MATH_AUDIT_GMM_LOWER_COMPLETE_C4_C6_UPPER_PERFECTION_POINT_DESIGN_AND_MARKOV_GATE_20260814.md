# Independent audit: GMM lower-complete C4/C6 upper-perfection gate

**Date:** 2026-08-14
**Source:** `MATH_REDUCTION_GMM_LOWER_COMPLETE_C6_UPPER_PERFECTION_POINT_DESIGN_AND_MARKOV_GATE_20260814.md`
**Verdict:** PASS after scope corrections

## 1. Exact invariant

For `n=2m+1`, `m>=2`, the source's diamond identity is correct:

\[
 P_{m-1}B_-+P_{m+1}B_+=P_mB_0.
\]

For a spanning two-factor with lower load `1+d`, it yields

\[
 P_{m+1}(u-\mathbf1)=\eta\mathbf1-P_{m-1}d,
 \qquad
 \eta={D(m-1)\over2m+1}
 =2{2m\choose m-1}-{2m\choose m-2}-{2m\choose m}.
\]

Thus upper perfection in a fixed lower-load fibre forces the surplus
`d` to be a regular point design.  The norm estimate in (1.9) is also
correct: pairing each repeated upper occurrence with a hole gives the
`2m` denominator, while either sign of a single point margin has mass at
most `R^+(u)`.

## 2. Complete signed image

The source correctly invokes the integral square-generation theorem

\[
 \ker_{\mathbb Z}P_{m+1}
 =\langle e_{Cbc}+e_{Cad}-e_{Cbd}-e_{Cac}\rangle_{\mathbb Z}.
\]

Each square has two independently checked fixed-owner, fixed-lower lifts:

- a two-edge `C_4` whose two lower occurrences both have colour `C`; and
- for nonempty `C`, the six-owner packet in (2.5), whose three lower
  colours are distinct and whose upper action is the same square.

Consequently point margins are the complete torsion-free invariant of the
signed upper-load quotient.  The source now correctly avoids extending
this conclusion to legal support-state or component-parity invariants.

## 3. Local-move audit

The corrected support statement is exact.  The `C_4` is the unrestricted
support-minimal rectangle.  The explicit `C_6` is minimal only under the
additional condition that its lower shore is occurrence-distinct.  The
source also gives a valid six-owner counterexample showing that an
arbitrary lower-neutral `C_6` need not have rectangle upper action.

For the explicit rectangle packet, the repeat-excess derivative and the
cross-distance-three local lock are correct.  A legal Hamilton `C_6`
additionally needs negative-edge containment, positive-edge absence, and
the six-port chronology condition.  These nonlinear requirements are not
consequences of signed lattice generation.

## 4. Coverage and endpoint scope

If only lower coverage is preserved, every upper-perfect endpoint still
has a nonnegative surplus `d'` of total mass `D` with regular point
degrees.  The square-sum swap proof correctly establishes the existence
of a simple regular `D`-block family for `m>=2`; it does not establish its
realization by one Hamilton factor.  The `1/6` transport lower bound applies
to any path using the displayed `C_4/C_6` catalogue, since six is the
largest per-move lower-ledger change; for a `C_4`-only path it sharpens to
`1/4`.

The distinction from gate (4.6) is correct.  An upper-perfect,
lower-complete Hamilton endpoint admits the paired-perfect-matching model.
A non-upper-perfect GMM source does not: its occurrence incidence lift has
upper degree `2u(U)`, and incidence-graph matching hexagons preserve an
already exact upper ledger.  Thus gate (4.6) is an endpoint formulation,
not a repair path from the GMM source.

## 5. Exact remaining gate

The strongest justified target is a conformal Markov theorem: first obtain
or transport to point-regular lower surplus, then prove that legal Johnson
`C_4/C_6` moves connect the source to an upper-perfect Hamilton state.
Signed generation proves neither availability nor chronology.  A
restricted `C_6`-only problem remains meaningful when distinct lower
occurrences must be protected, but it is not the full move graph.

No upper-perfect GMM cycle is proved by the source or this audit.

The source and this audit are frozen by their SHA-256 values reported with
the checkpoint.
