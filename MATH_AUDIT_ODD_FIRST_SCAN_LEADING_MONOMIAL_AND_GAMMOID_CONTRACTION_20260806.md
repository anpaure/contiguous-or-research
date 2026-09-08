# Audit of first-scan leading monomial and gammoid contraction

**Date:** 2026-08-06  
**Audited note:**  
MATH_THEOREM_ODD_FIRST_SCAN_LEADING_MONOMIAL_AND_GAMMOID_CONTRACTION_20260806.md  
**Method:** matching-state, strict-gammoid, contraction, and coefficient
replay; no computation  
**Verdict:** PASS as a one-layer factorization.  The recursive
quiet-compression minor remains open.

## 1. Scan basis

The coordinate scan is an involution away from its all-quiet states.
Because the chosen coordinate matching contains the cut boundary, the
selected state edges split disjointly into same-shore boundary edges \(P\)
and cross-shore nonwrap edges \(N\).  Removing \(P\) leaves \(N\) as a
matching of every cut-open vertex except \(V(P)\) and the quiet residue
\(Q\).  Hence \(V(P)\dot\cup Q\) is a surplus basis.  Quiet local masses
are even, so odd total mass forces the unpaired digit to be one and gives
the stated compressed layer.

This argument is in the labelled sector.  Quotient occurrence
coalescence is not silently asserted.

## 2. Gammoid orientation

Relative to \(N\), nonmatching edges are oriented \(L\to R\) and matching
edges \(R\to L\).  Symmetric difference with any other
minority-saturating matching gives vertex-disjoint directed alternating
paths from the \(N\)-unmatched surplus basis onto the new unmatched basis.
Conversely, flipping such paths gives the new matching.  This is the
standard strict-gammoid representation of a cotransversal matroid.

Every source in \(V(P)\) has indegree zero because it has no incident
\(N\)-edge.  If that source is also a prescribed target, its linkage path
must be trivial.  Deleting those forced paths proves that contraction by
\(V(P)\) is represented by deleting those vertices and retaining source
set \(Q\).

## 3. Coefficient extraction

Normalize the representation on the source basis
\(V(P)\dot\cup Q\).  In a Pfaffian term containing every independent
occurrence variable \(x_{o_e}\), \(e\in P\), the endpoints of \(P\) are
forced and already paired.  Deleting those pairs leaves exactly a basis
and boundary matching of the contraction.  Conversely every contracted
witness extends uniquely by \(P\).

The normalized determinant on the forced source columns is one.
Square-zero hub variables kill a repeated colour inside \(P\) or between
\(P\) and the residual witness; deleting used colours in the residual
matrix is therefore exact.  This proves the coefficient identity up to
the harmless global Pfaffian sign.

## 4. Scope

The coefficient identity proves that the first scan layer cannot cancel
internally.  It does not show that the contracted coefficient is nonzero.
The quiet residue is only the correct next vertex set; no theorem yet
identifies the contracted linkage digraph, physical occurrence matrix,
and hub colours with a fresh smaller sector.  The companion canonical-root
obstruction confirms that trivial paths from the quiet sources cannot
finish the contraction at nonextreme mass.
