# Independent audit: minimal relative incidence trade for \(C_4-U_5\)

**Date:** 2026-08-13  
**Verdict:** **PASS.**  
**Frozen source:** MATH_REDUCTION_MINIMAL_RELATIVE_INCIDENCE_TRADE_FOR_C4_U5_IN_ALIGNED_MSW_FACTOR_20260813.md  
**Source SHA-256:** a0f11d6e64f5d3a796277c1acdea95ac70b151a82900662285d2b2cd69bbb093

This audit checked the colored-factor equivalence, the explicit five-facet witness, the
global CP-SAT model and finite-result scope, and the upper-current formulation.
Substantive searches were not rerun locally.

## 1. Colored-edge equivalence

A rank-\(m\) facet \(L\) has rank-\(m+1\) supersets \(L+x\).  Two distinct such
owners form a Johnson edge with intersection \(L\), so a legal edge of color \(L\)
is exactly an unordered pair of distinct owners containing \(L\).  The source now
states the required distinctness \(X_L\ne Y_L\).

Keeping one edge for every facet preserves the complete immediate-lower row.  Equation
(1.5) is exactly preservation of every owner degree, hence is necessary and sufficient
for a relative owner/lower factor trade when all facets outside the support remain
fixed.  The union of the two endpoints is the edge's immediate-upper value, so equality
of the union-value multisets is exactly (1.6).  Proposition 1.1 passes.

For a three-facet support, inserting \(CU\) forces one other changed old edge incident
with \(C\) and one incident with \(U\).  Their colors are respectively
\(C\cap X_C\) and \(U\cap X_U\).  The remaining endpoint pairing is finite, and the
containment and optional union-multiset tests are complete.  Section 2 is correctly
scoped as a finite diagnostic at \(m=8,9,10\), not an asymptotic theorem.

## 2. Five-facet witness

For every row of (3.1), the listed old extra pair agrees with the literal edge of that
facet in \(F_7\).  None of the five facets belongs to one of the six frozen selected
portal rows.

Expanding the five rows gives identical old and new owner endpoint multisets.  The last
new row has endpoints

\[
\{0,5,6,7,8,9,12,14\}=C_4,\qquad
\{0,6,7,8,9,10,12,14\}=U_5.
\]

Thus the new last edge is the desired seam, and the table satisfies (1.5) exactly.
Its old and new upper-union multisets differ, so the source correctly says that the
witness is not upper-current exact.

The global CP-SAT model uses one Boolean variable for every pair of distinct outside
labels on every facet, imposes exactly one pair per facet, degree two at every owner,
the desired seam, and the old edge on every protected facet.  A chosen nonold pair is
counted once in the change bound.  Hence the recorded \(t=3,4\) infeasibility and
\(t=5\) feasibility establish the finite minimum in the stated model.

## 3. Upper-current results and scope

When enabled, the CP-SAT upper constraints equate the count of every rank-\(m+2\)
endpoint union to its old multiplicity, which is precisely (1.6).  The frozen \(m=7\)
files have statuses

\[
\begin{array}{c|cccc}
\text{change bound}&5&6&8&12\\ \hline
\text{status}&\mathrm{INFEASIBLE}&\mathrm{INFEASIBLE}&
\mathrm{INFEASIBLE}&\mathrm{INFEASIBLE}.
\end{array}
\]

The unrestricted \(m=7\) run has status UNKNOWN, so no nonexistence claim is made.
The \(m=6\) file records a feasible upper-exact solution with 27 changed facets and no
optimality claim.  The source's statements match these statuses.

The universal inverse-triple replay for \(m=8,9,10\) records no applicable two-row
trade installing the seam.  This is properly separated from arbitrary colored trades.

The note does not infer a uniform lift, a protected wreath-row rethread, residence,
fusion, or an upper-exact bounded trade.  Its conclusion is exactly the proved one:
the middle-incidence obstruction is locally solvable in the first finite case, while
upper current is the next sharp local gate.

## 4. Frozen finite ledger

The audited finite files include:

* cpsat_relative_compound_seam_m7_middle_cert_c3_20260813.json;
* cpsat_relative_compound_seam_m7_middle_cert_c4_20260813.json;
* cpsat_relative_compound_seam_m7_middle_cert_c5_20260813.json;
* cpsat_relative_compound_seam_m7_upper_c5_20260813.json;
* cpsat_relative_compound_seam_m7_upper_c6_20260813.json;
* cpsat_relative_compound_seam_m7_upper_c8_20260813.json;
* cpsat_relative_compound_seam_m7_upper_c12_20260813.json;
* cpsat_relative_compound_seam_m6_upper_exact_20260813.json;
* relative_inverse_trade_compound_seam_m8_m10_20260813.json.

The source does not list a separate frozen artifact for the \(m=9,10\) three-facet
diagnostic.  That affects reproducibility bookkeeping only; the claim remains explicitly
finite and is not used in Theorem 3.1.
