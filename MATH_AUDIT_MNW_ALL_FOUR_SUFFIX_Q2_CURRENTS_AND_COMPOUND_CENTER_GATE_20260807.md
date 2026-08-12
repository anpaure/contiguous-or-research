# Audit of all-four MNW suffix q2 currents

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_MNW_ALL_FOUR_SUFFIX_Q2_CURRENTS_AND_COMPOUND_CENTER_GATE_20260807.md`  
**Verdict:** PASS.

## 1. Source-edge audit

The four witnessing cycles in MNW are:

\[
\begin{aligned}
C_{\alpha(w)}={}&(1w00101,1w00111,1w00110,
                  1w10110,1w10100,1w10101),\\
C_\beta={}&(111000,111001,011001,011011,011010,111010),\\
C_\gamma={}&(11011100,10011100,10011101,10011001,
              11011001,11011000),\\
C_\delta={}&(111000,111001,110001,110011,010011,
              011011,011010,111010).
\end{aligned}
\]

Alternating edges are the canonical path edges.  Reading the other
canonical neighbour at every internal rank-lower centre gives exactly the
tables in Sections 2--3.  The third edge of every triple and two edges of
the delta cycle meet path endpoints where indicated and contribute no q2
turn after closure deletion.

**Result:** PASS.

## 2. Current simplification

The uncancelled currents are

\[
\begin{array}{c|l}
\alpha(w)v &[1w11101v]-[1w11110v]\\
\beta v &[111101v]-[111110v]\\
\gamma v &[11111001v]-[11111100v]\\
\delta v &[111101v]+[011111v]-[110111v]-[111110v].
\end{array}
\]

Appending a Dyck suffix preserves each path prefix and appends the same
bits to every union, by the published MSW concatenation identity.

**Result:** PASS.

## 3. Inverse-test witnesses

The positive targets have the following witnesses:

\[
\begin{array}{c|c|c|c}
T&p&q&\text{left/right count}\\ \hline
1w11101v&\text{first 1 of final block}&\text{third 1}&1/1\\
11111001v&2&4&1/1\\
011111v&3&6&0/0.
\end{array}
\]

There is no forbidden height-two/three down-step between any displayed
pair.  Every suffix \(v\) starts at height four, and \(w\) is read from
height one in the first row, so neither changes the counts.

**Result:** PASS.

## 4. No-support inference

Pairwise-disjoint path supports imply disjoint rank-lower centre sets.
Hence every affected centre is singly touched and its new target is one of
the positive terms above.  Since all positive terms are canonically
present, no canonical hole can be filled.

This inference would be invalid for overlapping supports that double-touch
one centre; the theorem explicitly excludes them and isolates them in
Section 5.

**Result:** PASS.

## 5. Compound identity

At a doubly touched centre, the two final facets are \(X+c,X+d\), so their
union is exactly \(X+\{c,d\}\).  The target criterion (5.4) is therefore
necessary and sufficient locally.  Extension of many offers to one MNW
hypertree is correctly left open.

**Result:** PASS.

**Overall verdict:** PASS within the stated suffix-tensor scope.

