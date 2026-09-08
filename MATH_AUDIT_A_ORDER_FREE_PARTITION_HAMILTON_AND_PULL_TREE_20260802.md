# Audit of the order-free partition-Hamilton and protected pull-tree theorem

**Date:** 2026-08-02  
**Audited root theorem:**  
MATH_THEOREM_ROOT_ORDER_FREE_TWO_CORRIDOR_HAMILTON_CONTRACTION_20260802.md  
**Root theorem SHA:**  
7231f74bf433c75d81e117d21861e9763862ccba62ca3ee6accbd6c13c6ea9e6  
**Audited continuation:**  
MATH_THEOREM_A_ORDER_FREE_PARTITION_HAMILTON_AND_PULL_TREE_GATE_20260802.md  
**Continuation SHA:**  
9f412c1401c1a1e7f2103028f6a1360ac914893d2782fb9b91ccd7ec567d6052  
**Verdict:** PASS_SCOPE_SAFE.

## 1. Contraction and prescribed arcs

The root equivalence is exact with its current state-fibre interpretation.
Every internal physical fragment of \(P_3\) is removed, and the marked
\(g_2\) realization carries the complete cumulative path ledger.  Deleting
\(g_1,g_2\) from one partition-Hamilton cycle produces exactly the two
uncrossed corridors; concatenating those corridors with the marked arcs
recovers the cycle.

Directional contraction retains only external entrances to the tail and
external exits from the head.  A variable marked state indexes a complete
compatible path realization and ledger, not merely an endpoint pair.

## 2. Exact common-state master

The continuation correctly adds the correlation absent from ordinary
Hamiltonicity:

1. one state is selected from every physical-fragment fibre;
2. selected indegree and outdegree equal the state selector;
3. one compatible realization of each protected composite is forced;
4. all global resource/capacity/charge rows are imposed on the same variables;
5. fibre-union subtour cuts exclude every proper cycle component.

The fibre-union cuts are sufficient; arbitrary state-subset cuts are not
needed.  The two-fibre directed four-cycle in Proposition 4.1 independently
shows that ordinary state-graph Hamiltonicity and quotient Hall can both hold
while the common-state partition cycle is impossible.

## 3. Expansion and pull scope

The dense semidegree criterion is applied only after a globally
ledger-feasible state transversal has been selected and the marked arcs have
been contracted.  Parallel literal options do not raise simple semidegree.

The factor-first Boolean theorem is also correctly scoped.  A rooted
tree-coherent spanning family of exact-safe pulls, executed
parent-before-child with the fresh-child two-to-one port test, merges all
factor components and preserves both marked contractions and every carried
ledger row.  Pairwise support disjointness alone is not claimed sufficient.

The protected deletion inequality is exact as a component-cut statement.
The scalar consequence \(\lambda>bL\) is best possible using only edge
connectivity \(\lambda\), protected-bank size \(b\), and per-resource pull
load \(L\).  Connectivity still needs a rooted tree-coherent/common-base
selection; total catalogue abundance is not a substitute.

## 4. Independent finite replay

The lightweight verifier

scratch/audit_a_order_free_partition_hamilton_20260802.py

has SHA

59ba59e1da79f4160d6ce8c0c8f643eae3fb961dc7422901fa7583f0dc779c69

and returns:

    PASS two-fibre state holonomy obstruction
    PASS m=3,d=1 explicit internal Boolean endpoint cover
    PASS internal endpoint census 2520 feasible / 2520 infeasible
    PASS special endpoints have 0 covers after g1 boundary history

Thus the finite positive example is correctly labelled as internal only; it
does not solve the marked-boundary problem.

## 5. Exclusions

Neither theorem proves an all-dimensional state transversal, robust safe-pull
supply, deep upper coverage, source/erosion transport, common compiler,
regeneration, or the final asymptotic construction.  The live theorem is now
precisely a protected rooted pull-atlas/common-base statement after a
globally compatible state-labelled cycle factor has been obtained.
