# Independent audit of the unified-rail carousel orbit hypergraph

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_UNIFIED_RAIL_CAROUSEL_ORBIT_HYPERGRAPH_DEGREES_LATTICE_AND_ROUNDING_BOUNDARY_20260807.md`  
**Verdict:** PASS for the requested exact orbit formulas, owner ledger,
target-correlation formula, and the (k=17) lattice obstruction.  The
perfect-matching discussion is correctly presented as a theorem boundary,
not as an application.  Two scope clarifications below should remain
explicit when the result is cited.

## 1. Degree and pair-codegree formulas

For a parameterized injection of a (U)-coordinate template into
([k]), fix a named rank-(R) owner (X).  There are (N) choices of
template owner, (R!) bijections onto (X), and
((k-R)_{U-R}) injections of the remaining template coordinates outside
(X).  Therefore

\[
 D_R=N R!(k-R)_{U-R}.
\]

The identical argument for (m_s) designated, distinct rank-(s)
template values gives

\[
 D_s=m_s s!(k-s)_{U-s}.
\]

For named sets (X,Y) of ranks (r,s) and intersection rank (q), a
fixed ordered template pair with the same ranks contributes

\[
 q!(r-q)!(s-q)!
 (k-r-s+q)_{U-r-s+q}
\]

injections.  Multiplication by the exact internal inventory
(\kappa_{r,s,q}) proves (3.4).  Parallel injection copies are retained,
so no unstated automorphism divisor is needed.

**Scope clarification.**  Formula (3.2) requires the (m_s) designated
template values to be distinct on a given shore, exactly as Section 2
states.  If one instead designates two occurrences having the same
underlying template set on one shore, a set-valued hyperedge does not
carry two copies of that vertex and the formula must be reformulated with
occurrence vertices.

## 2. Closed owner inventory

Two distinct cyclic (w)-intervals at displacement
(\delta=1,\ldots,w-1) overlap in (w-\delta) toggles.  There are two
directions and (N) roots, giving

\[
 \kappa_{R,R,R-\delta}=2N.
\]

The remaining ordered pairs are disjoint outside the core.  Their number
is

\[
 N(N-1)-2N(w-1)=N(N-2w+1),
\]

which proves (4.1)--(4.2).  Direct cancellation against (D_R) gives

\[
 \frac{D(X,Y)}{D_R}
 =\frac2{\binom R\delta\binom{k-R}\delta}
\]

in the short-overlap case and

\[
 \frac{D(X,Y)}{D_R}
 =\frac{N-2w+1}{\binom Rw\binom{k-R}w}
\]

in the core-only case.  For central (R), (w=o(R)), the maximum is the
(\delta=1) value (2/(R(k-R))=\Theta(k^{-2})).  The complete owner
ledger (4.1)--(4.5) passes.

## 3. Target correlation

When (\alpha+\beta\le N), the cyclic overlap distribution has two
unit-slope ramps, a plateau of length
(|\alpha-\beta|+1), and (N-\alpha-\beta+1) zero-overlap starts.  Its
listed multiplicities sum to (N), so (5.1) passes.

For fixed marked phase/depth types ((i,j)), ((i',\ell)):

* the first endpoint has (L) possible roots;
* the relative endpoint displacement is constrained by
  (v\equiv i'-i\pmod p);
* the permanent-bank intersection contributes
  (|\widehat B_{i,j}\cap\widehat B_{i',\ell}|);
* the toggle contribution is counted by
  (n_{N,p}^{i'-i}(j,\ell;\cdot)).

Summing these contributions is exactly (5.6).  When both shores and
designations coincide, the (m_s) identical occurrence pairs must be
removed; when the shores are distinct labelled copies, they must not be
removed.  The source states this distinction correctly.

**Scope clarification.**  Equations (5.3) and (5.6) are exact for the
phase-invariant marking encoded by sets of phase/depth pairs
(\mathcal M_s).  An arbitrary endpoint-level marking would require its
own relative-displacement inventory rather than the displayed factor
(L).

## 4. Coordinate lattice and (k=17)

In a selected carousel component, a fixed ground coordinate contributes

* (N_\theta) owner incidences when it is in the core;
* (w=d+1) incidences when it is a toggle;
* zero otherwise.

An exact partition of all rank-(R) owners must therefore satisfy

\[
 \sum_\theta
 (N_\theta c_{x,\theta}+w t_{x,\theta})
 =\binom{k-1}{R-1}
\]

for every coordinate (x), proving the gcd condition (6.6).

At (k=17), (R=9,d=3,w=4,c=5).  For
(a=0,1,2,3), respectively (p=4,3,2,1), formula (1.2) gives
(L=3,4,6,12) and hence (N=12) in all four cases.  Thus every
maximal component contributes (0,4,) or (12) incidences at a fixed
coordinate, whereas

\[
 \binom{16}{8}=12870\equiv2\pmod4.
\]

This proves the coordinate obstruction.  Independently,
(\binom{17}{9}=24310\not\equiv0\pmod{12}), so even the scalar owner
part-size equation fails.  The conclusion that maximal unified-rail
cycles alone cannot partition the (k=17) owner layer is exact.

## 5. Final audit boundary

The following statements are proved by the audited note:

1. exact parameterized orbit degrees and pair codegrees;
2. relative owner codegree (\Theta(k^{-2}));
3. exact finite formulas for phase-restricted target correlations;
4. exact scalar and coordinate lattice necessities;
5. a decisive maximal-cycle no-go at (k=17).

The following are deliberately **not** proved:

1. a growing-uniformity nibble theorem for this host;
2. an exact decorated component factor;
3. a lattice-generating opened-component catalogue;
4. upper-ticket/common-cap-compatible absorption;
5. (B(k)+O(1)) or exact equality.

Accordingly the proof-safe next object remains a lattice-breaking opened
component together with literal trades.  No correction to the central
mathematical claims of the audited note is required.
