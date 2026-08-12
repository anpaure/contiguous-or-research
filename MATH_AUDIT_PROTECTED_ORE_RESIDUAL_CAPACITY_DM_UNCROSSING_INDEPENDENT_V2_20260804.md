# Independent audit V2: protected Ore residual-capacity DM uncrossing

**Date:** 2026-08-04  
**Verdict:** **GO**.  No computation, search, or solver output is used.

Audited theorem:
`MATH_THEOREM_PROTECTED_ORE_RESIDUAL_CAPACITY_DM_UNCROSSING_20260804.md`,
SHA-256
`03878c6d28fc466ff09a0fca827592449cd2e48705f16a68ee0eb4248d4b5c79`.

Author self-audit:
`MATH_AUDIT_PROTECTED_ORE_RESIDUAL_CAPACITY_DM_UNCROSSING_SELF_20260804.md`,
SHA-256
`d4b94e42be96f7c4666abcab842643c1c3cde674cda91a4879bbdb8df10c5d44`.

This audit supersedes
`MATH_AUDIT_PROTECTED_ORE_RESIDUAL_CAPACITY_DM_UNCROSSING_INDEPENDENT_20260804.md`
at SHA
`d9acde12a412dea8c585332b0eb568e0f8206a69446c7137dc3d0ed9c9c0f8ee`
for the changed Section 6.  The Hall-surplus, min-cut, strict-block, and
Johnson-density arguments audited there are unchanged and remain valid at
the new theorem hash.

## 1. Revalidated unchanged core

Ownerwise,

\[
 \min(c_U,d_A(U))+e_P(U,A)=\min(2-p_U,a_U),
\]

so summation gives the exact identity

\[
 \mu_P(A)=\kappa_P(A)-r(A).
\]

The capacitated cut with projected lower shore `A` has optimized capacity
`R+mu_P(A)`.  Hence lower projections of minimum cuts are exactly the
maximum-deficiency shores.  Their family is a lattice by submodularity, and
the least and greatest residual-closed cut sides project to `A^-` and `A^+`.

Inclusion minimality/maximality gives the strict removal and addition block
inequalities.  The constant-spread ledger still cancels exactly to

\[
 d_{J[A^-]}(x)\ge2m-32-t_{\rm top}(x).
\]

No changes in the revised theorem affect these conclusions.

## 2. Exchange identity and forced elements

For `x in A` and `y notin A`, the displayed exchange identity is the sum of
the removal marginal at `A` and the addition marginal at `A-{x}`:

\[
 \mu(A-x+y)-\mu(A)
 =r_x-e_A(x)+u_{A-x}(y)-r_y.
\]

If `A` is a maximum-deficiency shore, this value is nonnegative and is zero
exactly when the exchanged shore is another minimizer.

The forced-element correction is exact.  By definition

\[
 A^- = \bigcap\{A:A\text{ is a maximum-deficiency shore}\}.
\]

Thus every `x in A^-` belongs to every minimizer.  Any exchange deleting
`x` produces a shore not containing a forced element and therefore cannot
remain a minimizer.  Its value in the exchange identity is strictly
positive.  A shifted minimizer containing `A^-` must instead add missing
downward shifts while moving upward in the min-cut lattice.

## 3. Residual SCC description of all minimum cuts

Fix any maximum flow and contract the strongly connected components of its
residual network.  The resulting `Q_f` is a DAG.  A minimum-cut source side
is exactly a union of residual SCCs which:

1. contains the source component `q_s`;
2. omits the sink component `q_t`; and
3. is successor-closed under every condensation arc.

Necessity is residual closure of a minimum cut.  Conversely, a
successor-closed component union containing `q_s` and excluding `q_t` has no
positive residual arc leaving it, so its cut capacity equals the maximum
flow value and it is a minimum cut.

## 4. Shift implications and Theorem 6.2

For every elementary downward coordinate shift `x -> y`, the implication
arc `[x] -> [y]` enforces exactly the shifted-family condition on the lower
projection of a component union.  This remains true when `x` and `y` lie in
the same SCC, in which case the implication is automatic.

Consequently, a lower projection is both a maximum-deficiency shore and
shifted if and only if its SCC union is successor-closed in the augmented
digraph `Q_f^sh`, contains `q_s`, and omits `q_t`.

Such a union exists if and only if the successor closure of `q_s` in the
augmented digraph omits `q_t`, equivalently

\[
 q_s\not\leadsto q_t\quad\text{in }Q_f^{\rm sh}.
\]

If the path exists, every successor-closed set containing `q_s` must contain
`q_t`.  If it does not, the successor closure itself is feasible.  That
closure is contained in every other feasible augmented-closed set, so it is
the unique minimal shifted minimum-cut source side.  Its lower projection is
therefore a shifted maximum-deficiency shore.

The criterion is independent of the chosen maximum flow as an existence
statement: for each chosen flow it is equivalent to existence of the same
intrinsic object, namely a shifted maximum-deficiency lower shore.

## 5. Scope

The SCC criterion proves neither the required no-path assertion for the
constant-spread residual network nor an initial-colex classification.  Even
when the augmented source closure avoids `q_t`, its lower projection is only
shifted and capacity-closed.  A separate extremal theorem is still needed to
place it in an already-closed family such as initial colex.

The corrected forced-element discussion and Theorem 6.2 are exact.  The
independent V2 verdict is **GO** at the hashes listed above.
