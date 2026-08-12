# Audit of Hamilton-first Ferrers intersection and arbitrary boundary deletion

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_PBBS_HAMILTON_FIRST_FERRERS_INTERSECTION_AND_ARBITRARY_BOUNDARY_DELETION_20260807.md`  
**Method:** line-by-line symbolic audit; no computation or finite search  
**Verdict:** PASS.  The total-shadow recurrence, endpoint minimization,
Kruskal--Katona application, and residual Hall deduction are exact.  The
result closes ordinary containment capacity only.

## 1. Colex recurrence

For

\[
 q={x\choose j}+q',\qquad0\le q'\le{x\choose{j-1}},
\]

the relevant colex prefix consists of all rank-\(j\) sets on \([x]\),
followed by \(\{x+1\}\cup B\) for a rank-\((j-1)\) colex prefix on
\([x]\).  The proper faces not containing \(x+1\) are the complete
\((j-1)\)-skeleton on \([x]\).  The proper faces containing \(x+1\)
are in bijection with proper faces of the link prefix, including its empty
face.  They are disjoint from the first class.  Hence (2.6) has neither a
missing singleton nor a double-counted empty face.

At \(q=1\), the proper downset including the empty face has size
\(2^j-1\).  At the full layer it has size
\(\sum_{t<j}\binom at\).  These are exactly the two endpoint terms.

## 2. Endpoint induction

The identity

\[
 G_j(x+1)-G_j(x)=G_{j-1}(x)
\]

is Pascal's identity.  The ratio

\[
 {\binom xt\over\binom x{j-1}}
\]

strictly decreases with \(x\) for every \(t<j-1\), since its successive
ratio is

\[
 {x-j+2\over x-t+1}<1.
\]

Thus \(G_{j-1}\) changes sign at most once, from positive to negative,
and \(G_j\) first rises and then falls.  Its minimum on the breakpoint
interval is at an endpoint.

Inside one colex block the inductive third candidate is
\(G_j(x)+A_{j-1}\).  If \(A_{j-1}\ge0\), it is no smaller than the left
endpoint.  If \(A_{j-1}<0\), the decreasing ratio in the preceding
paragraph gives directly
\(G_{j-1}(x)\le A_{j-1}\), so it is no smaller than the right endpoint.
This verifies the only non-obvious step in Lemma 2.1.

## 3. Shadow normalization and the Ferrers constant

Iterated Kruskal--Katona simultaneously minimizes every rank-\(s\) lower
shadow at the colex prefix.  Since different ranks are disjoint, the
inequalities may be summed.  Removing the one empty face converts the two
endpoint gaps to

\[
 2^r-2-d
 \quad\text{and}\quad
 \Lambda-dW=h.
\]

The parameter assumption gives

\[
 h\le\binom{d+1}{2}\le2^r-2-d.
\]

The second inequality is correctly reduced to the worst case
\(d=r-1\), namely
\(\binom r2\le2^r-r-1\).  It holds at \(r=1,2\) and then strengthens
inductively.  Therefore the full owner layer is the minimum endpoint and
the sharp inequality is \(D(\mathcal Q)\ge d|\mathcal Q|+h\).

## 4. Hall deduction

For a residual family \(\mathcal F\), if its owner neighborhood is full,
the arbitrary deletion of \(h\) targets supplies exactly the missing
global capacity.  If the neighborhood is proper, every target in
\(\mathcal F\) lies outside the total lower shadow of the complementary
owner family \(\mathcal Q\).  Thus

\[
 |\mathcal F|
 \le\Lambda-D(\mathcal Q)
 \le d(W-|\mathcal Q|)
 =d|N(\mathcal F)|.
\]

These are precisely Hall's inequalities for \(d\) owner copies.  Nothing
about the ranks or identities of the deleted targets is used.  The
uniform-transversal-matroid corollary follows by extending any smaller
target family to size \(dW\).

## 5. Scope audit

The result proves:

* arbitrary named boundary deletion of cardinality \(h\);
* exact residual containment matching;
* capacity at most \(d\) per owner; and
* compatibility of that row with the independently chosen Hamilton-first
  clean packet targets.

It does not prove ownerwise comparability, suffix chronology, deep upper
coverage, or common-cap feasibility.  In particular, calling the
transversal matroid uniform does not turn the chain-configuration
hypergraph into a matroid.  The theorem's final scope statement is
therefore proof-safe.

The Section 8 warning is also exact.  Its residual family has eight
targets and four capacity-two owners, and (8.1) is a valid containment
assignment using every target once.  Four two-element strict chains would
each require one singleton and one pair, but only three residual
singletons exist.  The example refutes only a generic capacity-to-flag
inference; its noncentral owner rank is stated explicitly.
