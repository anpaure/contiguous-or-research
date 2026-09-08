# Independent audit of the GMM--Catalan common-refinement obstruction

Date: 2026-07-31  
Status: PASS after two explicit scope corrections

## 1. Audited object

This note audits
MATH_AUDIT_K_GMM_SINGLE_PORT_GLUE_CATALAN_COMMON_REFINEMENT_OBSTRUCTION_20260731.md
against the full Gregor--Mütze source for *Trimming and Gluing Gray Codes*.

The source numbering is correctly separated:

* Lemmas 12--13 are the constant-weight reflected-Gray-code and adjacent-row
  subsequence lemmas.
* The displayed adjacent-level one-port splice is Theorem 15.

The printed proof uses the strict induction range
\(1\le k<\lfloor n/2\rfloor\).  The central substitution
\(n=2m-1,\ k=m-1\) is outside that literal sentence, although the displayed
splice remains algebraically valid because its two required port paths
exist.  The report now states this nuance and scopes its no-go to that
displayed boundary splice.

## 2. Sector arithmetic: PASS

Put

\[
 A=\binom{2m-1}{m-1},\qquad
 B=\binom{2m-1}{m-2},\qquad
 K=A-B.
\]

Then

\[
 A=\frac12\binom{2m}{m},\qquad
 B=\frac{m-1}{m+1}A,\qquad
 K=\frac1{m+1}\binom{2m}{m}=\operatorname{Cat}_m.
\]

The lower rows avoiding/containing the new coordinate have sizes \(A,B\).
The upper colours avoiding/containing it have sizes \(B,A\).  A bijective
selected lower-to-upper map therefore sends exactly \(K\) unmarked lower
rows across the sector cut.  This proves the Catalan transport identity
without assumptions on the parent cycles.

## 3. Theorem-15 crossing and direct label: PASS

The displayed splice removes

\[
 (b_{n,k}0,a_{n,k+1}0),\qquad
 (a_{n,k}1,b_{n,k}1)
\]

and adds

\[
 (b_{n,k}0,b_{n,k}1),\qquad
 (a_{n,k+1}0,a_{n,k}1).
\]

Only the lower row \(b_{n,k}0\) changes from two zero-sector middle
neighbours to one neighbour in each sector.  The second new edge is a
same-rank distance-two step and has no lower row.  Hence the number of
distinguished crossing rows is exactly one, giving deficiency
\(K-1\).

Moreover

\[
 a_{n,k}\cup b_{n,k}=a_{n,k+1},
\]

so both the removed direct edge and its replacement have union
\(z+a_{n,k+1}\).  Every other direct edge is untouched.  The direct union
multiset, and therefore its squarefreeness when present, is preserved
exactly.

## 4. Pascal-square algebra and all-\(K\) converse: PASS

For \(x=a\cup b\), the switch

\[
 \{b0-x0,\ a1-b1\}
 \longmapsto
 \{b0-b1,\ x0-a1\}
\]

is degree preserving and legal.  It preserves the direct union \(z+x\)
and moves exactly one distinguished lower row across sectors.  Therefore
any common refinement inside this square-switch fibre uses exactly \(K\)
squares.  Since the lower parent has exactly \(K\) direct steps and no
direct occurrence can be removed twice, all direct steps must be used.

The converse is correct for the **floor-profile** common refinement:
physical compatibility, both palette bijections, squarefree direct labels,
and one-cycle topology are necessary and sufficient.  Literal cap-two
blocks require the additional condition

\[
\text{each direct edge is adjacent to the unique selected edge of the
same union colour.}
\]

The report now records this as condition (2.2a).  Palette data alone do
not force adjacency.

## 5. Candidate orientations and the floor core: PASS

For a direct edge \(d=\{a,b\}\) with \(x=a\cup b\), an endpoint is usable
exactly when it is one of the two lower neighbours of \(x\) in the central
cycle.  Thus

\[
 \operatorname{Cand}(d)\ne\varnothing
 \iff
 \{a,b\}\cap N_{C_0}(x)\ne\varnothing.
\]

Identifying facets of the \(m\)-set \(x\) by their missing elements turns
this into intersection of two 2-subsets of an \(m\)-set.  It is automatic
for \(m=3\), and it is not automatic for \(m\ge4\).

Under the stated floor marginals, the direct-step/doubled-colour/hole
hypergraph is exactly the simultaneous-square palette problem.  A perfect
matching is equivalent to both exact palettes.  Endpoint reuse is excluded
because a reused orientation has the same loss label, violating matching
on the doubled-colour shore.  One-cycle topology and condition (2.2a)
remain separate.

## 6. Final verdict

The added block-coherent closure lemma also passes.  If a direct child edge
\(ab\) of union \(x\) has its equal-union distinguished partner through
\(a\), the Pascal square with free endpoint \(b\) replaces it by
\(x0-a1\).  The partner survives through \(a1\), acquires union \(z+x\),
and is therefore still consecutive with the direct edge.  Pairwise distinct
free endpoints and distinct direct unions make the square supports
edge-disjoint.  This proves the literal block conclusion under the stated
strong child-port hypotheses; it does not prove those hypotheses exist for
all \(m\).

The architecture-specific obstruction and its constant are correct:

\[
\boxed{\text{one published port versus }
\operatorname{Cat}_m\text{ required ports}.}
\]

The exact constructive replacement is a Catalan-sized orientation atlas
with endpoint, two-palette, topology, and block-adjacency constraints.
Leaf peeling of its full occurrence hypergraph is a sufficient certificate,
not a consequence of the published recursion.

Audited main-report SHA-256:
`3692fd0cec97ed16224465791ec6ca62822e5797a01de8a31b825ff52261c02a`.
