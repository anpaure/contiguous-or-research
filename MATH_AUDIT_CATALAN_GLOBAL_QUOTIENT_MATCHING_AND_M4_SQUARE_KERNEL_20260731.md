# The \(m=4\) alternating-square kernel inside the global quotient matching

Date: 2026-07-31  
Status: exact audit of the two authenticated \(m=4\) lifts; positive local
exchange fixture, not an all-\(m\) exchange theorem

## 1. Global-first rebase

The regular-quotient Hall argument in
MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md
is correct: the clean-\(H\) quotient of the complete lower--upper diamond
graph is balanced regular, hence has a perfect matching.  Exceptional
period-three filters are the restriction of that global matching, not
independently prescribed inputs.

The exact remaining physical gate is already isolated in
MATH_THEOREM_CATALAN_GLOBAL_MATCHING_CYCLE_FIRST_PHYSICAL_GATE_20260731.md:
find a spanning quotient Johnson occurrence cycle of primitive
\(H\)-voltage whose lower--upper colour-incidence graph has a perfect
matching.  That matching is automatically a spanning common-transversal
linear forest inside the cycle.  The deterministic \(m=8\) quotient
matching shows why global palette Hall alone is insufficient: its physical
lift has overload \(2640\) and cyclomatic number \(331\).

This note records the additional local exchange structure supplied by the
authenticated \(m=4\) seed.

## 2. The exact alternating square

For \(m=4\),

\[
 (q,h,s)=(7,7,1),\qquad
 (|\bar{\mathcal M}|,|\bar F|,\#\operatorname{comp}\bar F)=(10,8,2).
\]

The common transversals induced by the two authenticated repair choices
\(K_0\) and \(K_1\) are global quotient perfect matchings with eight
occurrence edges.  They share six edges.  Their remaining four occurrences
form the complete alternating square on lower colour orbits

\[
                 \{\mathtt{83},\mathtt{85}\}
\]

and upper colour orbits

\[
                 \{\mathtt{97},\mathtt{ab}\}.
\]

The two matching diagonals are

\[
\begin{array}{c|c}
K_0&(\mathtt{83},\mathtt{ab}),(\mathtt{85},\mathtt{97})\\
K_1&(\mathtt{83},\mathtt{97}),(\mathtt{85},\mathtt{ab}).
\end{array}                                             \tag{2.1}
\]

Both choices remain in the physical linear-forest fibre:

\[
K_0:\ 7+3,\qquad K_1:\ 6+4
\]

are their quotient path-size profiles.  Both connector cycles have total
voltage \(2\bmod7\), so both lifts are connected 70-cycles.

Thus the m4 binary kernel is, in global-first language, one alternating
\(K_{2,2}\) matching square whose two diagonals are simultaneously
palette-exact, forest-safe, and primitive-voltage closable.

## 3. Reusable exchange statement and scope

Toggling an alternating cycle in the quotient diamond graph preserves the
global lower/upper perfect matching.  Such a toggle is admissible for the
physical problem exactly when its occurrence lift remains a loopless
degree-at-most-two quotient forest and its new path endpoints admit a
one-cycle primitive-voltage connector selection.

The m4 square proves that a nontrivial admissible toggle can change path
geometry while preserving closure holonomy.  It does not prove that every
dimension or every perfect-matching component has such a toggle.  In
particular, period-three phase sections are derived matching choices, and
the authenticated K16 compiler may break \(H\); no filter-to-seam or
filter-to-compiler identification is made here.

## 4. Reproduction

Run

    python3 scratch/audit_catalan_m4_global_matching_square_kernel_20260731.py

The script reconstructs both quotient common transversals directly from
the frozen physical-lift audit, verifies both colour matchings and both
linear forests, and identifies the alternating square (2.1).

