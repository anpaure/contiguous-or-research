# Audit of the PBBS height-ladder body co-selection theorem

**Date:** 2026-08-05  
**Method:** symbolic word, distance, and Hall replay; no computation  
**Audited file:**
`MATH_THEOREM_PBBS_HEIGHT_LADDER_BODY_COSELECTION_20260805.md`
**Audited SHA-256:**
`d50a16bafe01073456c28ddcea43d91129231d288a47a72b7a33139e4a8d2d06`

## 0. Verdict

**PASS at the stated component-co-selection scope.**  Each alternating socket
has a list of `2d+1` distinct PBBS components within contact distance `d`,
and any fixed bank has a distinct representative assignment.  The theorem
does not choose the connector paths jointly resource-disjoint and does not
convert them into relative PBBS matching returns.

## 1. Word and distance replay

The word

\[
                         1^h0^h(10)^{r-h}
\]

is Dyck and has height exactly `h`.  Appending the unmatched zero gives a
valid deficit-one PBBS state.  Comparing it with `(10)^r0`, the only new
ones are the even positions at most `h`, exactly `floor(h/2)` of them; the
same number of later odd positions disappear.  Hence the Johnson distance
is `floor(h/2)`.

Different heights imply different PBBS components because the largest
soliton part is component-invariant.  Taking `h<=2d+1` gives the claimed
`2d+1` components and radius `d`.

The replacement indices in (2.3) are exactly the even positions at most
`h` and the first `floor(h/2)` odd positions greater than `h`.  Therefore
the displayed connector ends at `A_h` and has the stated length.

## 2. Hall replay

Every collar list has cardinality `2d+1`.  The union of any nonempty
subfamily consequently has cardinality at least `2d+1`, even if all lists
are identical.  For a fixed bank of size `H<=2d+1`, this is at least the
subfamily size.  Hall gives distinct PBBS body components exactly as
claimed.

## 3. Scope replay

Complementing the Johnson path and inserting common facets gives a literal
Middle-Levels incidence path.  If a fixed family of these paths is
resource-disjoint from the shield bank, the existing protected-factor
theorem can plant their union prospectively.  The SDR alone does not prove
that disjointness.  Nor is a connector a directed cycle cover in either
fixed PBBS exchange graph, and it need not preserve the rest of a selected
PBBS component.  The theorem explicitly retains all qualifications.

The `O(1)` component conclusion concerns only the fixed named protected
subsystem.  No bound on all unprotected factor components is claimed.
