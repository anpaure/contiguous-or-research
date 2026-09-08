# Audit of MNW leaf-protected pivot rethreading and q2 mobility

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_MNW_LEAF_PROTECTED_PIVOT_RETHREAD_AND_Q2_MOBILITY_20260807.md`  
**Verdict:** PASS within its stated scope.

## 1. Primary-source hypotheses

The source is T. Mütze, J. Nummenpalo and B. Walczak,
*Sparse Kneser graphs are Hamiltonian*, J. London Math. Soc. 103 (2021),
1253--1275, DOI 10.1112/jlms.12406.

The proof uses exactly these source statements:

1. canonical paths \(P(x)\) partition the bipartite graph \(G_m\);
2. every flippable tuple selects one marked edge from each supported path;
3. \(\mathcal H_m\) has a spanning tree for \(m\ge3\);
4. every such spanning tree is conflict-free;
5. its flipping cycles Hamiltonize \(G_m^+\) while retaining all complement
   closure edges; and
6. Section 6 lifts the resulting rethreaded forest in one half together
   with the fixed canonical forest in the other half to a middle-levels
   Hamilton cycle.

All six statements occur explicitly in the paper.

## 2. Leaf calculation

The recursive hypertree definition joins \(\ell\) smaller incidence
trees through one new tuple-node of degree \(\ell\).  Hence its incidence
graph is a tree.  Tuple-nodes have degree three or four, so an ordinary
leaf is necessarily a Dyck-word node and has one selected mark.

If the marked edge is in position \(j\) on a \(2m\)-edge path, reversal
moves it to \(2m+1-j\).  One of these positions exceeds \(m\), so the first
\(m\) edges of one orientation are untouched.

**Result:** PASS.

## 3. Full-path no-go scope

Every Dyck-word node has positive degree in the incidence tree, and every
incident selected tuple removes one edge of its canonical path.  New flip
edges join distinct canonical paths and cannot recreate that old edge.

This proves impossibility only inside the MNW spanning-tree
Hamiltonization.  It is not a no-go for an arbitrary unrelated
middle-levels Hamilton cycle.

**Result:** PASS.

## 4. Owner-to-incidence indexing

For \(t\) owner transitions, the completed incidence path is

\[
 X_0,Y_0,X_1,Y_1,\ldots,X_t,Y_t,X_{t+1}.
\]

The required owner lift starts at \(Y_0\) and ends at \(Y_t\), so it uses
edge positions \(2,\ldots,2t+1\).  The sufficient inequality
\(2t+1\le m\) places all of them in the protected prefix.  For the
\(3h\)-transition pivot buffer this becomes \(6h+1\le m\).

**Result:** PASS.

## 5. q1 and q2 scope

Every rank-\((m+1)\) vertex in the rethreaded incidence forest has degree
two.  Suppression therefore uses it exactly once as a q1 edge colour.
This proves q1 exactness independently of the chosen hypertree.

The explicit \(\alpha\)-flip calculation gives

\[
 \{101111v,111110v\}
 \mapsto\{111101v,101111v\},
\]

so the turn map is genuinely movable.  The MNW recursive tree contains
one such connector for every \(v\in\mathcal D_{m-3}\), giving the stated
Catalan-scale bank.  Other flips can subsequently modify a second edge at
the same centre, so the theorem correctly stops short of final target
surjectivity.

The gained target \(111101v\) is canonically present: positions two and
four satisfy the exact MSW inverse test, with left and right ordinal counts
both one, and a Dyck suffix at height four changes none of the test data.
Thus the theorem also correctly records that this first explicit bank is
not itself a missing-target repair.

**Result:** PASS.

## 6. Count ledger

Using \(\binom{2m}{m}=(m+1)\operatorname{Cat}_m\), removal of the
\(\operatorname{Cat}_m\) closure matching leaves

\[
 (m+1)C-2C=(m-1)C
\]

internal rank-\(m\) vertices.  Also

\[
 \binom{2m}{m+2}=\frac{m(m-1)}{m+2}C.
\]

Their difference is \(2(m-1)C/(m+2)\), as stated.

**Result:** PASS.

## 7. Exact exclusions

The theorem does not claim:

1. connectivity after forbidding an arbitrary interval on an arbitrarily
   predesignated canonical path;
2. preservation of a whole canonical path in the rethreaded half;
3. final q2 surjectivity;
4. global residence or deeper upper coverage; or
5. a literal antecedent/compiler.

It proves the existential conjugated protected-pivot theorem and reduces
the remaining upper row to (7.5).

**Overall result:** PASS.
