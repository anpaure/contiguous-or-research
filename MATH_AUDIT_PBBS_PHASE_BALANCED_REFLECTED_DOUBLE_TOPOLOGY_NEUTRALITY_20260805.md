# Audit of the phase-balanced reflected-double topology theorem

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_PBBS_PHASE_BALANCED_REFLECTED_DOUBLE_TOPOLOGY_NEUTRALITY_20260805.md`  
**Method:** independent permutation, component-ledger, and quantifier replay;
no computation

## 1. Anti-conjugacy

For a successor cycle

\[
                    (X_0,X_1,\ldots,X_{t-1}),
\]

the permutation `rho s^{-1} rho` has the cycle

\[
                    (\rho X_0,\rho X_{t-1},\ldots,\rho X_1).
\]

This is a bijection on cycles and preserves each cycle length.  Since the
word on `rho X` is the reversal of the word on `X`, the second cyclic word
is a cyclic rotation of the complete reversal of the first.  Width and
value of every cyclic interval are therefore preserved.  Theorem 1.1 is
correct.

## 2. Resident phase signs

Put `A=H_2` and `B=H_3`.  The resident theorem gives

\[
             H_1=\operatorname{rev}(A),\qquad
             H_0=\operatorname{rev}(B).
\]

Hence reflecting and exchanging the two copies sends

\[
             (H_0^-,H_2^+)=(\operatorname{rev}B,A)
\]

to

\[
             (H_1^-,H_3^+)=(\operatorname{rev}A,B).
\]

The inverse in the successor formula is required: reflection is an
anti-isomorphism of directed occurrence order.  Thus equation (2.1), not
ordinary conjugacy, is the correct relation.

## 3. Component ledgers

The resident counts are

\[
 c(H_0)=c(H_3)=1,
 \qquad
 c(H_1)=c(H_2)=q.
\]

Therefore the uncoupled double has `q+1` components in both phases.

For the displayed fully crossed successor map,

\[
 (s_0)^2(X_i^+)=X_{i+1}^+,
 \qquad
 (s_0)^2(X_i^-)=X_{i+1}^-.
\]

One orbit consequently contains all `2q` paths.  Anti-conjugacy gives one
terminal orbit as well.  The `1 -> 1` statement is exact as an abstract
cut-path calculation and is correctly not promoted to a PBBS physical
seam-existence claim.

## 4. Exterior quantifier

The cyclic-deck assertion includes a complete context only when that
context is one of the reflected path occurrences.  It does not authorize
holding an arbitrary named left/right exterior fixed.  The theorem keeps
this distinction:

* closed or reflected paired context: exact;
* pointwise-fixed independent exterior: false without another witness.

This agrees with the sharp private-prefix boundary counterexample.  The
topological no-go is scoped to cancellation by a complete occurrence
bijection inside the two copies; it does not exclude larger witness-creating
packets.

## 5. Verdict

**PASS within the stated scope.**  The phase-balanced reflected double can
remove the upper-current defect only as a reflected occurrence isomorphism.
Such an isomorphism preserves cycle type, so it cannot simultaneously be a
component-fusion actuator.
