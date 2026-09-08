# Audit: boundary-locked dual-phase linkage

**Date:** 2026-08-06  
**Primary proof:**
`MATH_OBSTRUCTION_ODD_ADJACENT_SOURCE_HAMILTON_AND_DUAL_APERTURE_20260806.md`,
Section 7  
**Method:** literal local-row and alternating-component replay; no
computation or search  
**Verdict:** PASS within the labelled fixed-scan contraction.

## 1. Local phase table

The original and dual mass-two rows are

\[
\begin{array}{c|c|c}
\text{phase}&\text{matching edge}&\text{quiet state}\\ \hline
0&02-11&20,\\
1&20-11&02.
\end{array}
\tag{1.1}
\]

They have the same three-vertex union

\[
                         20-11-02.
\tag{1.2}
\]

The rows at local masses one and three agree in both phases.  The
boundary-locked scan changes only the internal mass-two rows and leaves
the physical boundary row in phase zero.

## 2. Component endpoint replay

Fix a compressed source word \(u\).  Along the union of the two scan
matchings:

1. every code-zero pair remains \(00\);
2. every code-two pair remains \(22\);
3. every internal code-one pair stays in the set
   \(\{20,11,02\}\); and
4. the boundary pair never changes.

These data are component invariants.  In this invariant fibre, the unique
vertex unmatched by phase zero has every internal code-one pair equal to
\(20\), while the unique vertex unmatched by the boundary-locked dual
phase has every such pair equal to \(02\).  Therefore they are the two
endpoints of one alternating component.  Distinct compressed words have
different invariant data, so all components are vertex-disjoint.

If there is no internal code-one pair, the two endpoints are the same
vertex and the linkage path is trivial.  This is compatible with strict-
gammoid linkage conventions.

## 3. Directedness and contraction

Start at the phase-zero quiet source.  The first nontrivial edge belongs
to the dual scan and is not in the phase-zero reference matching.  The
next edge belongs to the phase-zero matching, and so on.  All changed
pairs are nonboundary pairs.  Relative to the standard orientation, the
path therefore alternates

\[
              L\xrightarrow{\text{nonmatching}}R
               \xrightarrow{\text{matching}}L.
\]

It is a directed path.

Every endpoint of the installed boundary current has an active boundary
row.  Every vertex of the boundary-locked phase component has boundary
state \(00\), \(20\), or \(22\), quiet in phase zero.  Hence the component
is disjoint from the entire deleted endpoint set \(V(P)\), not merely
from the boundary edges themselves.  The path survives in \(D'\).

Thus the terminal bank \(Q_*\) is linked disjointly from every quiet source
and is a basis of the contracted strict gammoid.

## 4. Literal complement identity

On an internal pair, literal complement sends

\[
              00\leftrightarrow22,qquad20\mapsto02.
\]

On the boundary pair, applying the boundary swap after complement sends

\[
              00\leftrightarrow22,qquad20\mapsto20.
\]

Therefore, with \(\tau=(0\ \ 2m)\),

\[
                         q_*(u)=\tau\,\overline{q_0(2-u)}.
\tag{4.1}
\]

The boundary swap in (4.1) is an identity between endpoint labels.  It is
not being asserted to be an automorphism of the cut-open digraph.

## 5. Full-complement collision

If the boundary row is changed to phase one as well and the boundary code
is one, any alternating component from the phase-zero quiet endpoint to
the phase-one quiet endpoint must change \(20\) to \(02\).  The only
local union route is (1.2), so it uses the phase-zero physical boundary
edge

\[
                         11-02.
\]

Its endpoints belong to \(V(P)\), and the component is destroyed by the
contraction.  If the boundary code is zero or two, the boundary local
state is respectively \(00\) or \(22\) and no such collision occurs.

The exact number of affected central sources is obtained by fixing the
boundary compressed digit to one:

\[
             \#\{u:u_m=1,\ \sum_i u_i=m\}
             =[z^{m-1}](1+z+z^2)^{m-1}.
\tag{5.1}
\]

This is a macroscopic bank.  It cannot be exported as one parity socket or
absorbed by a fixed protected interface.

## 6. Scope

The audit certifies:

1. one explicit macroscopic noncanonical basis \(Q_*\) in the labelled
   contraction;
2. exact disjointness and directedness of its phase linkage;
3. exact avoidance of the installed boundary current; and
4. the exact full-complement collision slice (5.1).

It does **not** certify a boundary-edge paired basis.  Every member of
\(Q_*\) still has a quiet physical boundary pair.  The remaining operation
must transport the boundary phase defect through a different scan root
before returning it.

