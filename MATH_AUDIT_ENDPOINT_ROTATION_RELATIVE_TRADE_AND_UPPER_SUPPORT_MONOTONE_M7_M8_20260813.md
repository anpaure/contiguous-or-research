# Independent audit: endpoint-rotation relative seam trades

**Date:** 2026-08-13  
**Verdict:** **PASS, with one interpretive clarification in Corollary 1.2.**  
**Frozen source:** `MATH_THEOREM_ENDPOINT_ROTATION_RELATIVE_TRADE_AND_UPPER_SUPPORT_MONOTONE_M7_M8_20260813.md`  
**Source SHA-256:** `8152a2e1509f19ac346305fcf8a8251c2a5230690f90a357235c63c6622ef7d1`  
**Verifier SHA-256:** `a812f88becbf4c594cd50e623f4b2ed9ffe91a99de5775ed236f306549902930`  
**Frozen H100 result SHA-256:** `edc94db7fb50c917575b834f71f7d7b2dfc3b370000c660f26fafa9a502b73d7`

This was a proof audit plus an independent replay of the frozen verifier on H100.
The replay output has exactly the frozen result SHA above.

## 1. Abstract circuit algebra

For an arc

\[
  V_{i-1}\xrightarrow{L_i}V_i,
\]

the old edge is \(\{P_i,V_{i-1}\}\) and the new edge is
\(\{P_i,V_i\}\).  On a closed directed circuit, the stationary endpoints
cancel termwise and the moving endpoint multisets telescope.  Thus every owner
degree and every facet colour is preserved.  The upper-current change is literally

\[
 \sum_i\bigl({\bf e}_{P_i\cup V_i}
              -{\bf e}_{P_i\cup V_{i-1}}\bigr),
\]

so Lemma 1.1 is correct.

Corollary 1.2 is also correct, but its phrase “form endpoint-rotation circuits”
should be read as a combined two-open-path trade, not as two independently legal
circuits using the seam facet twice.  The path \(C\leadsto A\) has owner-degree
defect \(-C+A\), the path \(U\leadsto B\) has defect \(-U+B\), and the single
combined seam replacement

\[
             \{A,B\}\longmapsto\{C,U\}
\]

has defect \(-A-B+C+U\).  Their sum is zero.  Mutual facet-label disjointness and
avoidance of \(L_0\) then preserve every other colour exactly.  This is the precise
algebra supporting the stated conclusion.

## 2. Upper-support scope

Condition (2.2) is exactly equivalent to support monotonicity relative to the old
factor.  It neither preserves upper multiplicities nor proves that the old factor
covered every possible upper target.  The source maintains this distinction
throughout, including its final scope statement.

## 3. Finite witnesses

The verifier reconstructs the complete first-aligned factors at \(m=7,8\), checks
that every displayed old pair is literal, checks avoidance of all protected portal
facets, compares old and new owner multisets, identifies the required
\(C_4-U_5\) seam, and replays the global old upper loads.

For \(m=7\), all five net removed upper values have old load at least two and final
load at least one.  For \(m=8\), the five net removed values likewise retain positive
load.  Hence both tables establish upper-support monotonicity, not merely local
upper-current balance.

No uniform-in-\(m\) path theorem, chronology realization, residence preservation, or
universal upper cover follows from these two witnesses; the source correctly leaves
all four assertions open.
