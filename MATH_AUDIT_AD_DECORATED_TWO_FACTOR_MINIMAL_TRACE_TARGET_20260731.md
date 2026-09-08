# Audit of the decorated two-factor minimal trace target

Date: 2026-07-31  
Audited corrected source:
`MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`  
Source SHA-256:
`17e0e5fee4ade4bb61802c0e8baabaab4eceb4cb24e209cbb8c03f6d3ee3315a`  
Verdict: **PASS after the all-marked correction**; the earlier snapshot
without that correction is false; no all-dimension existence or word
theorem

## 1. Decisive correction

The first snapshot treated a marked component as safe whenever its binary
trace failed the mixed condition

\[
 \text{all positive zero-runs have length two and all one-runs are odd}.
 \tag{1.1}
\]

That criterion presupposes that both symbols occur.  A wholly marked
component has trace \(1^{2q}\) and instead lifts to two same-rail cycles.
The corrected source explicitly requires every marked component to contain
an unmarked occurrence and applies (1.1) only to mixed traces.  This is the
exact missing hypothesis.

The smallest counterexample to the uncorrected statement is at \(m=3\).
On \(\mathbb Z_5\), the cycles

\[
 A_i=\{i,i+1\},\quad B_i=\{i,i+1,i+2\},
 \tag{1.2}
\]

and

\[
 D_i=\{2i,2i+2\},\quad E_i=D_i\cup D_{i+1}
 \tag{1.3}
\]

form a spanning two-factor of \({\rm ML}(5)\).  Mark all of the first
cycle and none of the second.  Then

\[
 \ell_i=\{i+1\},\qquad
 u_i=\mathbb Z_5\setminus\{i+3\},
 \tag{1.4}
\]

so both palettes are bijective and the shores alternate.  Nevertheless the
first component lifts to two five-cycles.  The current source excludes this
state.

## 2. Perfect diamond matching

The matching ledger is exact.  Across all factor components there are
exactly \(P\) selected \(A\)-turns and \(P\) selected \(B\)-turns.
After deleting the marks, every mixed component is a union of even paths
and has one residual matching; every unmarked component has either of its
two alternating phases.  Thus the residual edge count is

\[
                         Q-P=\operatorname {Cat}_m.    \tag{2.1}
\]

The selected turns cover the two outer palette banks bijectively, while the
residual edges cover every remaining occurrence once.  Hence the diamonds
form a perfect matching.  The two residual phases on an unmarked component
are genuinely free and preserve all central palette counts.

## 3. Acyclicity and exact path count

The component lifts have disjoint physical vertex sets.  The exact local
classification is:

* all zero: a matching of cross edges;
* all one: two rail cycles, now forbidden;
* mixed: exactly one cycle precisely under (1.1), otherwise a forest.

Therefore the corrected local conditions imply a global linear forest.
It has

\[
 |V|={2m\choose m},\qquad
 |E|={2m\choose m-1}=|V|-\operatorname {Cat}_m,
 \tag{3.1}
\]

so Euler gives exactly \(\operatorname {Cat}_m\) path components; isolated
vertices cause no exception.

## 4. Quantifier and terminology audit

For any two spanning two-factors, the red-blue symmetric difference
decomposes into alternating closed trails.  Since the middle-levels graph is
bipartite, these split into simple alternating even cycles.  Thus an
alternating packet from a prescribed starting factor adds no existential
condition beyond the accepting terminal factor.

“Consecutive selected occurrences” must include cyclic wrap-around; under
that convention a singleton-mark component is not alternating.  The
corrected source's cyclic wording has this meaning.

Hamiltonicity and component merging are genuinely unnecessary for this
middle-levels-supported implication.  The word “weakest” must nevertheless
remain scoped to the factor-resolvable architecture: arbitrary Catalan
linear diamond matchings need not admit such a support.

## 5. Remaining boundary

The corrected theorem proves only Catalan Linear Matching conditional on an
accepting decorated factor.  It does not prove that such a factor exists in
all dimensions, nor does it provide residence, deep-shadow coverage,
connectors, voltage, or the lower compiler needed for \(\nu(k)=B(k)\).
