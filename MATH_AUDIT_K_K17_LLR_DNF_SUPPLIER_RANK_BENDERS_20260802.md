# Independent audit: K17 LLR DNF and supplier-rank Benders oracle

**Date:** 2026-08-02  
**Audited note:**
`MATH_THEOREM_K17_LLR_OCCURRENCE_DNF_SUPPLIER_RANK_BENDERS_ORACLE_20260802.md`  
**Verdict:** PASS for the symbolic finite formulation and matching-rank cuts.
The corrected `4,803/470/1,012` census is accepted only as an externally
reported warm47-scoped input until its local hashes arrive.  Its materialized
470 table is not the protected `b268...` table.

## 1. Transfer conservation

One selected transfer

\[
 (\ell,m,r)+(u,q)\mapsto(m,r)+(\ell,u,q)
\]

deactivates exactly one old direct-low short and activates exactly one new
middle short.  It changes the type vector by `(LLR,LMR,LR,MR) +=
(1,-1,-1,1)` and leaves the row-length vector unchanged.  Hence the
unprotected short count remains `5,647`, total shorts remain `7,395`, and
the residual long-port count is `16,915-7,395=9,520`.  Row-disjoint transfer
sets are exactly matchings in the declared donor/host graph.

## 2. Selected-parent Hall formula

For an integral master assignment, retain a supplier edge only when its
complete selected parent, state, and signed placement conjunction is true.
For active head set `H_*` and a subset `X`, exact OR linearization gives

\[
 \sum_u n_u^X=|N(X)|.
\]

The standard deficiency identity

\[
 |H_*|-\nu=\max_{X\subseteq H_*}(|X|-|N(X)|)
\]

therefore rearranges to the theorem's epigraph cut.  With a dynamic
head-universe bit `d_h`, the same cut is

\[
 \Theta\le K-\sum_{h\in X}d_h+\sum_u n_u^X,
 \qquad K=\sum_h d_h.
\]

The exhaustive independent C++ auditor enumerated every bipartite graph
with each shore of order one through four: `74,954` graphs and `1,157,324`
set-shore checks.  In every case it verified

\[
 \nu(G)=\min_X(|L|-|X|+|N_G(X)|).
\]

It also independently recomputed the determinant-two natural socket minor.

```text
scratch/audit_k17_supplier_rank_benders_formula_20260802.cpp
  c9bb689418321827e8e6ab1a6fbe79c972c3d2f40edaa5f868d02c3c5eccd231

scratch/k17_supplier_rank_benders_formula_20260802.audit.json
```

## 3. Structural consistency correction

The protected residual bottom matching and the low side of the general
common-basis presentation describe the same target-placement witness on the
fixed-owner/root face.  They cannot be completed independently.  The
audited theorem now explicitly requires shared edge literals:

* use the `15,151` residual bottom presentation on the restricted face; or
* use the general augmented common-basis presentation on a root-changing
  face, embedding all protected placement units.

Every occurrence DNF refers to those same placement literals.  Thus the
oracle cannot certify one structural table while the state layer silently
uses another.

The 470-transfer table is warm47 plus selected transfers, whereas the
literal `1,748/3,496/3,495` private object was materialized on `b268...`.
Avoiding the protected row IDs in the warm47 transfer matching proves only
a row-disjoint projection.  It does not transport the protected occurrence
tickets or their bottom placements.  A joint branch is legal only if the
union of both footprint sets is a partial matching and the residual
structural presentation has a perfect matching.  Otherwise the
common-materialization Hall oracle closes it before repricing.

## 4. Exactness and non-TU scope

The exact role rows select one genuinely active occurrence because every
ticket variable implies all signed parents and the selected variables sum
to the binary role-activity bit.  Protected ports, flags, tokens, and
physical resources are literal capacity units.  Conditional on these
choices:

1. structural completion is ordinary bipartite matching;
2. residual long completion is ordinary bipartite matching; and
3. supplier rank/perfectness is ordinary bipartite matching.

Their Hall/DM shores become globally valid Benders cuts only after each
neighbor indicator is encoded as a bidirectional OR of complete parent
activations.  A union edge, stale supplier record, or forward-only parent
implication is insufficient.

The joint master is not claimed TU or polynomial.  Occurrence columns bundle
two directed ports, states, placements, and resources; its general catalogue
contains three-dimensional matching, while the natural marginal socket
matrix already has determinant two.  Branching and finite cut generation,
not a generic matching shortcut, is therefore the proof-safe conclusion.

## 5. Exact scope

This audit proves the formulation and separation oracles.  It does not
replay the not-yet-local full-private-470 table, regenerate its `5,647`
role catalogues, or prove supplier rank `16,898`.  It makes no chronology,
residence, upper, common-cap/compiler, or word claim.
