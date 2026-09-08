# Audit of the period-\(2q+1\) pure-rail and central-wreath factor theorem

**Date:** 2026-08-13  
**Verdict:** **PASS after two scope corrections.**  No substantive defect
remains in the literal rail construction or in the MSW-to-wreath
implication.

## 1. Audited files

1. `MATH_THEOREM_PERIOD_2Q_PLUS_1_PURE_RAIL_RESIDENCE_AND_CENTRAL_WREATH_FACTOR_20260813.md`;
2. the residence patch in
   `MATH_THEOREM_CENTRAL_ODD_CYCLES_WREATHS_AND_FIXED_CORE_RAIL_SEMIGROUP_BOUNDARY_20260812.md`.

The external input used by the second file is exactly Theorem 4 of
M\"utze--Standke--Wiechert: for every \(q\ge1\), the odd graph
\(KG(2q+1,q)\) has a \(C_{2q+1}\)-factor with \(\operatorname{Cat}_q\)
components.

## 2. Literal interval and residence audit

Let \(N=2q+1\), let \(x_0,\ldots,x_{N-1}\) be distinct, and put

\[
 A_i=C\cup\{x_i\},\qquad
 O_i=\bigcup_{t=0}^{q-1}A_{i+t}=C\cup I_i^q.
\]

For every \(1\le j<N\), the union of a cyclic \(j\)-interval of source
letters is exactly \(C\cup I_i^j\).  Equality of two such values first
forces the same cardinality \(c+j\), hence the same width \(j\), and then
the same proper cyclic interval in an order of distinct labels, hence the
same start.  This proves the claimed full proper-deck simplicity.

Advancing the owner window deletes \(x_i\) and inserts \(x_{i+q}\), so
the owners form a simple Johnson cycle.  Consecutive intersection and
union rows are respectively \(C\cup I^{q-1}\) and
\(C\cup I^{q+1}\), and are simple provided \(q\ge2\).

Each toggle trace on the owner cycle is exactly a cyclic shift of

\[
 1^q0^{q+1}.
\]

Thus both its positive run and its zero run meet the strict finite-cycle
threshold \(D=d+1=q\).  A core trace is constant one and an unused trace
constant zero; its unique present run has physical length \(2q+1\ge q\),
while the absent run type is vacuous.  This is exactly the project's
strict positive/dual residence convention.  Cyclic return restores the
complete source state, so the whole component has zero trace boundary.

The same calculation in fact shows that an unprotected period-\(2q\)
rail is also simple and biresident for \(q\ge2\), with trace
\(1^q0^q\).  The stronger \(N\ge2q+2\) assumptions in later absorber
theorems pay for exterior port labels; they are not residence axioms.

## 3. MSW factor-to-rail implication

The audited Aug-12 theorem proves independently that a
\(C_{2q+1}\) vertex family in \(KG(2q+1,q)\) is exactly the family of
all cyclic \(q\)-windows of one coordinate order.  The odd-cycle order
uses start increment \(q\); the rail order uses start increment one.  As
\(\gcd(2q+1,q)=1\), these are two enumerations of the same vertex family.

Consequently every component of the MSW factor can be reordered as the
owner row of the literal period-\(2q+1\) source above.  Since the MSW
cycles partition all \(q\)-sets, adjoining a fixed disjoint core \(C\)
gives an exact positive factor of the shell

\[
 \{C\cup Q:Q\in\tbinom Tq\}
\]

into

\[
 \frac1{2q+1}\binom{2q+1}{q}=\operatorname{Cat}_q
\]

legal resident rails.  This conclusion is owner-exact.  Immediate rows
are simple inside each rail, but the MSW theorem does not say that those
rows are globally disjoint across different rails.

## 4. Corrections made

Two literal range/scope corrections were necessary.

1. The period theorem now assumes \(q\ge2\).  At \(q=1\), the owner row
   remains a triangle, but the immediate lower row is the same core \(C\)
   at all three starts and is therefore not simple.
2. The patched Aug-12 note still defined admitted pure-rail periods by the
   old lower bound \(N\ge2q+2\).  It now consistently admits the
   unprotected resident range \(2q\le N\le M\).  Accordingly the \(k=17\)
   period list is \(8,9,10,11,12\), not \(10,11,12\).  The fixed-core
   divisibility proof is unchanged because every period-\(N\) rail gives
   every used toggle point degree exactly \(q\).

## 5. Exact boundary

The theorem supplies an exact positive owner factor on each central
\((2q+1)\)-toggle shell.  It does not supply:

* a decomposition of a larger fixed-core fibre;
* globally exact lower or upper palettes across its Catalan rails;
* compulsory lower marks or common-cap tickets;
* fusion of the Catalan components; or
* the exterior labels needed by the protected adjacent-transposition
  ports.

Subject to that boundary, the theorem and the corrected Aug-12 patch are
proof-safe.
