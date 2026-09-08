# Independent audit: three pair structures cover every owner

**Date:** 2026-08-13  
**Verdict:** **PASS.**  
**Frozen source:** `MATH_THEOREM_THREE_PAIR_STRUCTURES_COVER_EVERY_OWNER_BY_A_GOOD_CELL_20260813.md`  
**Source SHA-256:** `db2b82ed1f9994c29d3aaebf4b39fe9c74cfc0411e178675930d7b46700177c9`

This was a proof-level audit; no finite search was used.

## 1. Probability calculation

The symmetric group is transitive on the rank-\(R\) owner layer and on the orbit of
a sentinel-plus-perfect-matching structure.  Since every fixed structure has exactly
\(L_{p,q}\) bad owners, a fixed owner is bad for a uniform random structure with
probability

\[
                         \delta_{p,q}=L_{p,q}/W.
\]

For \(t\) independent structures the all-bad probability is
\(\delta_{p,q}^t\).  The union bound over the \(W\) owners is therefore exactly
\(W\delta_{p,q}^t\), proving Theorem 2.1.

For \(t=3\), inserting (1.3) and \(W\le 2^{2p+1}\) gives

\[
 W\delta_{p,q}^3
 \le 2^{1-p}(2p+2)^3(ep/M)^{3M}.
\]

The logarithmic condition actually needed is

\[
 3M\log_2(ep/M)+3\log_2(2p+2)+1<p;
\]

the displayed hypothesis (2.2) uses \(+2\), so it has one full bit of slack and is
sufficient.  When \(q=\Theta(\sqrt p)\), its left side is
\(O(\sqrt p\log p)=o(p)\), proving the eventual three-structure assertion.

## 2. Exact scope

The conclusion is only a set cover by good cells from three overlapping cell
partitions.  It does not imply a disjoint whole-cell cover.  Assigning an owner to its
first good structure generally removes a nonempty proper subset from later cubes, so
their Hamilton Gray cycles no longer restrict to cycles.  The source explicitly states
this obstruction and does not infer a resident factor, exact palettes, or a fused
chronology.

Thus the theorem closes the support-cover question and leaves the genuinely integral
whole-cell/cycle-selector problem open, exactly as claimed.
