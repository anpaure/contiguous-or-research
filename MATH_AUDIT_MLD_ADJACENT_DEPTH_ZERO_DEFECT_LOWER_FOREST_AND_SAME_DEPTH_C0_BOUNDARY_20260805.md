# Audit: MLD adjacent-depth zero-defect lower forest and same-depth `C=0` boundary

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_MLD_ADJACENT_DEPTH_ZERO_DEFECT_LOWER_FOREST_AND_SAME_DEPTH_C0_BOUNDARY_20260805.md`  
**Method:** independent-style symbolic audit; no computation, search, or solver  
**Verdict:** **GO**, with “zero defect” restricted to the named lower
Boolean-chain system and with global carrier serialization explicitly open.

## 1. Cutoff audit

At old boundary `t=r-D`, the canonical residual histogram uses ranks
`1,...,t-1`.  Hence a chain born at `a` has `t-a` targets.  The relevant MLD
cutoff is `t-1`.  After terminal deletion and the shift to `b=t-1`, the
new histogram uses `1,...,b-1=t-2`.  The theorem's strict-below-`b`
assertion is therefore correct; no endpoint target is counted twice.

## 2. Extreme-point audit

On the support of an extreme configuration point, the matrix has one job
equality per job and at most `D` active aggregate tail rows.  Thus at most
`D` jobs have more than one positive configuration.  This conclusion fails
with the same numerical bound if further constrained aggregate rows are
introduced; the theorem records the corrected `D+R` bound.

## 3. Capacity-tail audit

The new exact capacity-`g` multiplicity is `H_(b+g)`, so

\[
 \sum_{g=q}^{D+1}H_{b+g}=W-C_{b+q-1}=K_q^+.
\]

Subtracting the old tail gives `H_(t+q-1)` for `q<=D`, and the new maximum
tail is `H_r`.  After deleting `h` maximum sockets and the exact reserves,
the residual tail is exactly (4.4).  Therefore (3.5)--(3.6), together with
`A_q<=K_q`, are precisely the sorted-tail inequalities.  Every assigned
socket is a genuine collar-chain occurrence.

The audit confirms the important scope condition: if an old fractional LP
uses endpoint-triangle sockets in addition to `K`, then `A_q<=K_q` is not
automatic and the theorem may not be invoked without a new check.

## 4. Quantifier and MLD audit

Capacity marks are derived from deterministic extreme-point counts and an
integer sorted-tail matching before the Boolean paths are sampled.  Grouping
equal mark vectors gives a fixed-count refinement inside each birth cohort.
This is exactly the quantifier allowed by cohort MLD.  No realized path is
recoloured.

Once paths are realized, a piece top at a prescribed rank is a union of
persistent configuration labels.  MLD supplies its binomial Laplace bound.
Generalized Holder does not require independence across ranks.  The
pointwise-codegree event has positive probability under (4.2), and matching
integrality may then be applied after top names are known.  Thus the final
collar starts are both named and occurrence-disjoint.

## 5. Charge audit

The construction leaves no unmatched lower target.  The quantities `h` and
`Delta_g` count used or deliberately unused sockets, not appended literals.
The only structural charge is the transition from depth `D` to `D+1`.
Converting that depth into one added source-word position remains a separate
serialization theorem.

## 6. Same-depth boundary audit

If an ordinary tail saturates `K_q`, deleting one socket of capacity at
least `q` violates the necessary sorted-tail inequality.  Therefore a
same-depth disjoint reserve is not a valid generic consequence of
fractional feasibility.  Equation (6.2) correctly states the required
capacity-neutral integer augmentation.

The workload lower bound is conditional but correctly scoped: a residue of
`Theta(r^(3/2))` cells needs `Omega(r)` depth-`Theta(sqrt(r))` occurrences.
It rules out bounded physical support for such a residue, not a finite-state
rule repeated many times.

## 7. Parity audit

For an even complete pair slice, every one-copy orientation has odd degree,
and hence odd divergence, at every slice state.  A balanced supergraph needs
an odd number of external incidences at every state, so at least `n/2`
external arcs; an open trail can exempt at most two states.  The
bounded-support no-go follows immediately.

The theorem correctly separates this dynamic parity obstruction from the
static socket-semigroup obstruction.  It does not claim that even slices
are forced globally, that a bounded-state replicated rule is impossible, or
that linear rethreading costs extra word positions.

## 8. Final scope

The audited implication is

\[
 \boxed{
 \text{fractional `D`-tail configurations}
 +\text{unconditioned cohort MLD}
 +\text{adjacent reserve}
 \Longrightarrow
 \text{zero-defect named lower forest at depth `D+1`}.}
\]

It is not yet

\[
 \text{a resident upper-complete word at }B(k)+1,
\]

and it gives no same-depth `C=0` theorem without the two new gates isolated
in Section 8 of the audited note.
