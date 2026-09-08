# Audit of signed ERP provenance and the deep crossing Hall cut

Date: 2026-07-26

Audited file:
`MATH_ATTACK_K_ERP_SIGNED_PROVENANCE_AND_DEEP_CROSSING_HALL_20260726.md`.

Method: independent hand audit; no computation, finite search, solver, or
external input.

## Verdict

**PASS.** No theorem-level correction remains after the patches recorded
below.

The audit independently verified:

1. the exact formulas for the signed projected rows \(P_j,Q_j\) and all
   four intersection/union families;
2. the \(2s+3\) circular chart, the \(3s+2\) full-port word, overlap
   length \(s\), and trail ledger \(t(2s+2)+cs\);
3. the ordered-interval owner-credit Hall theorem and the natural
   first-owner injection with capacity \(b_u\ge1\);
4. the asymmetric residual halo counts and the unique pin carriers
   \(D_{a+q-H}\) and \(D_{a+q+1}\), under the explicit
   \(H\)-erosion-admissibility hypothesis;
5. the support-level lower bound \(d_I+s-1\), its sharp maximum
   \(3s-3\), and the exact local ledger
   \(\delta_I\ge d_I-s-3-c_I-\rho_I\);
6. the persistent-carrier specialization \(d_I=2s-2\) and exact toll
   \(c_I+\rho_I+\delta_I\ge s-5\);
7. the one-shore FIFO theorem after restoring distinct-token,
   carrier-disjointness, and adjacent-tuple-disjointness hypotheses; and
8. the fixed-graph Hall scope, hypergraph bundling caveat, edge-bearing
   directed-trail formula, weighted opening scope, and final implication
   boundary.

## Corrections incorporated during audit

The final theorem file explicitly incorporates the following necessary
scope corrections.

* Canonical erosion identities are invoked only on
  \(H\)-erosion-admissible capped paths. A short positive run can otherwise
  occur in an owner but in no erosion letter.
* The one-shore FIFO compiler assumes every token tuple is internally
  distinct, disjoint from the carrier, and disjoint from each adjacent
  tuple. Nonadjacent reuse remains allowed.
* Small local excess implies either deep support collisions or linear
  collar absorption/export; it does not force export alone.
* Proper core splitting and persistent FIFO cores are two valid
  implications, not an exhaustive dichotomy.
* Endpoint Hall deficiency is exact for a fixed endpoint graph; an
  arbitrary interior redesign requires recomputing that graph.
* The trail formula omits edgeless weak components, and the weighted
  opening identity is asserted only for uniform toll within each
  component.
* The conclusion closes the signed owner-credit and packet-interior
  provenance subgate only. It does not claim full ERP\(_H\) or coefficient
  one.

With these scopes, the theorem package is internally consistent and the
constants are exact.
