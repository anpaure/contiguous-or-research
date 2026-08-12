# Audit of the raw first-kill switch coefficient and polarization ledger

**Date:** 2026-08-06  
**Method:** line-by-line algebraic and scope audit; no computation or search  
**Verdict:** **FAIL / DO NOT CITE**  
**Audited file:**
`MATH_THEOREM_RAW_FIRST_KILL_SWITCH_COEFFICIENT_AND_POLARIZATION_LEDGER_20260806.md`  
**Audited SHA-256:**
`1a37aceab055047cae6e140a373f32b44bf7e859a18334c0f58d4f89b01125b5`

The requested audit named SHA
`fe7228c1...`, but those bytes were no longer present in the shared
workspace when the audit began.  This verdict is bound only to the complete
SHA displayed above.  Any replacement theorem needs a fresh audit.

## 1. Parts that are algebraically sound

The following isolated statements pass.

1. Given the definitions in Section 1 and assuming the future-density
   ratios are at least one, the bare hypothetical coefficient is bounded by
   the future-weighted hypothetical coefficient.
2. Coordinate relabelling preserves the base atomic-orbit weight and the
   deterministic rank-compensation counts.  Thus an available candidate
   and its coordinate-transposed image have equal bare rates.
3. The numerical inequality in Theorem 2.1 follows immediately from the
   preceding coefficient inequality.  It is a correct inequality between
   the two quantities *as defined*.
4. The Hilbert-space polarization estimate

   \[
   [\|u\|_R^2-\|v\|_R^2]_+
       \le \|v\|_R^2+2\|u-v\|_R^2
   \]

   is correct for positive-semidefinite `R`.
5. The earliest-blocker partition and the pathwise fact that an unordered
   availability boundary is born at most once remain valid.

None of these statements identifies the actual stopped-boundary coefficient
with a summand of the future-overlap potential.  That identification is the
load-bearing missing step.

## 2. Fatal mismatch: a switch pair is not a future-overlap pair

Sections 2--4 use the same symbols `E,F` for two different algebraic roles.

* In the switch calculation, `F=tau E` is the transposed candidate paired
  with `E` by the Johnson switch.
* In the future-overlap potential `(FP2)`, `E,F` are the two candidate
  indices arising after a square expansion, and both contain the same named
  pair root `Q`.

No derivation in the audited note proves that the stopped switch covariance
is indexed by the latter pair, or that its coefficient is

\[
 {a_G(i)\over X(i)}\,\widetilde c_i^+(Q,E,F).
\]

In particular, a general coordinate transposition need not fix `Q`.
Although `E` may contain `Q`, `tau E` contains `tau Q`; it need not contain
the same `Q`.  Carrying the root along by `tau` proves equivariance between
two differently labelled root terms, not membership of `E,tau E` in one
fixed `(Q,E,F)` summand of `(FP2)`.

Therefore the sentence calling (2.2) the **true** switch-birth coefficient
is unsupported.  The numerical domination (2.3) is consequently not a
domination of the actual boundary term.

This is an algebraic-degree problem, not a missing constant: the switch
candidate pair, the squared future-potential pair, and the first blocker
must first be kept as separate indices and only then related by an explicit
contraction or injection.

## 3. The killed cross term does not automatically pay the killed diagonal

Section 2 identifies the right side of (2.3) with the killed **cross** term
`c_i(Q,E,F)R_i(E,F;Q)`.  Section 3 then says that the
`||v||_R^2` part of polarization is paid by a killed **diagonal** term for
`F`.

Those are distinct future-potential summands.  Even when the two bare rates
are equal, their common-root conditions and their future-fugacity exponents
are different.  A valid proof must display the diagonal coefficient
`c_i(Q,F,F)R_i(F,F;Q)` (with a legal fixed root) and prove the needed
coefficient domination.  The audited note does neither.  It switches from
the cross coefficient to the diagonal payment without an identity or an
inequality.

## 4. Equation (4.2) is false

Let

\[
 D(E,\tau)=((\tau E)-E)\cap
      (\mathcal L\mathbin{\dot\cup}\mathcal R)
\]

be the full set of non-slot resources changed by the transposition, and let

\[
 J(G;E,\tau E)=D(E,\tau)\cap G.
\]

The first-blocker condition proves only that `J` is nonempty.  It does not
prove `J=D`.  The switch innovation `(I-tau)z` changes every resource in
`D`, including resources not met by `G`.  Thus the asserted decomposition

\[
                         z=\sum_{x\in J}z_x
\]

omits all terms indexed by `D-J`.

A two-resource example already breaks it: if `D={x_1,x_2}` and the first
blocker meets only `x_1`, then `J={x_1}` while the switch innovation still
contains the nonzero `x_2` contribution.  Its diagonal energy is absent
from (4.3), and the cross energy between `x_1` and `x_2` is not a
two-hit term because the blocker hits only one of them.

Consequently:

* the one-entry map to `(ROc)` is incomplete;
* the correlated map to `(FE3)` is incomplete; and
* the spare `1/d` in `(FE3)` does not pay the omitted switch energy.

This defect remains even if the coefficient mismatch in Section 2 is
repaired.

## 5. The pristine transposition average is not yet the stopped average

The identity

\[
 \mathbb E_\tau\|(I-\tau)z\|_R^2
       =2\alpha_q\langle z,Bz\rangle
\]

is an average over a uniform complete transposition orbit.  At a first
kill, the transposition is filtered by the event that its mate is killed by
the adapted blocker, and the term carries an `E,F,G,Q`-dependent future
coefficient.  The audited note does not prove that these coefficients are
constant across the complete transposition orbit, nor a weighted coarea
inequality reducing the filtered average to the uniform one.

Lemma 1.1 only compares one candidate with its own transposed mate.  It
does not compare coefficients for different transpositions of the same
candidate: the overlap exponents and fixed-root membership may change.
Hence (3.4) cannot simply be inserted after conditioning on a first kill.

## 6. The `(ROc)` and `(FE3)` normalization is asserted, not derived

Even on the truncated set `J`, Section 4 does not write the identities
needed to pass from

\[
 {a_G(i)\over X(i)}\,c_iR_i
\]

to the static `(ROc)` and `(FE3)` weights.  A proof needs, separately:

1. the one-hit sum over `G`, including `1/X(i)`, the compensated rates, and
   the future-survival exponents;
2. the two-hit density change of variables producing exactly
   `K_{p_*}(j)`;
3. multiplicity bounds for the map from stopped switch terms to the
   complete-host rooted tuples; and
4. the same replay for each marked size-two and size-three pattern.

The cited `(FP9)`/global-rate reconstruction explains why such formulas may
be plausible, but the identity map in (4.7) is not a proof of them.  In
particular it cannot repair the index mismatch or the missing `D-J` terms.

## 7. Consequence

The implication

\[
 V(S_0)=O(M/d^4)
 \quad\Longrightarrow\quad
 \mathbb E(B_0+B_1)=O(M/d^2)
\]

belongs to the parent stopped-transfer framework once its hypotheses are
proved.  The audited note does not prove the antecedent.  Therefore its
claims `(5.1)`, `(DROOT)`, `(ASE)`, `(AIB)`, and `(5.2)` do not follow.

## 8. Minimum requirements for a corrected theorem

A corrected proof must do all of the following without identifying the
indices prematurely.

1. Expand the actual stopped boundary form `D(S_i)` and derive its literal
   first-kill coefficient.
2. Keep the switch candidate pair, the future-potential square pair, the
   named root, and the blocker as separate indices until an explicit map is
   proved.
3. Decompose the switch innovation over the full changed-resource set `D`,
   not only the blocker-hit subset `J`.
4. Supply a weighted complete-orbit/coarea estimate for the adapted
   first-kill restriction.
5. Prove the one-hit and multi-hit injections with every normalization and
   multiplicity shown.
6. Only after those rows pass, replay the finite marked-pattern cases and
   infer the Bellman-value estimate.

Until such a rewrite is audited, the raw Johnson-switch coefficient row
remains open.
