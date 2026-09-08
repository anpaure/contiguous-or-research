# Audit of MNW mirror-wrapper q2 hole mobility

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_MNW_MIRROR_WRAPPER_Q2_HOLE_MOBILITY_20260807.md`  
**Verdict:** PASS.

## 1. Published wrapper identity

MNW Lemma 7 proves that `1 revcomp(phi) 0` is flippable whenever `phi` is.
Its proof explicitly embeds the old canonical path under

\[
                         y\longmapsto1\operatorname{revcomp}(y)1.
\]

This swaps ranks `m` and `m+1`.  Hence intersections at old upper centres
become unions at new lower centres.  Formula (1.4) follows exactly.

**Result:** PASS.

## 2. Base coturn ledgers

The uncancelled coturn currents are

\[
\begin{array}{c|l}
\alpha &[000110]+[100001]-[000101]-[100010],\\
\beta &[001001]+[010010]-[010001]-[001010],\\
\gamma &[10010100]+[10001001]-[10001100]-[10010001],\\
\delta &[000011]+[011000]-[010001]-[001010].
\end{array}
\]

They result by intersecting the replacement lower endpoint with the
unchanged canonical lower neighbour at each changed upper vertex.  Direct
substitution through `F(A)=1 revcomp(A) 1` gives every row of (2.2).

**Result:** PASS.

## 3. Presence and absence checks

Canonical coturn witnesses for all alpha and delta gains and for the second
beta gain are listed explicitly in (3.1).  The exact canonical q2 inverse
test gives:

\[
\begin{array}{c|c}
\text{target}&\text{status}\\ \hline
10110111&\text{absent},\\
11011011&\text{present via }(p,q)=(4,5),\\
1110101101&\text{absent},\\
1011011101&\text{present via }(p,q)=(6,7).
\end{array}
\]

The height and ordinal arguments in Section 3 exhaust every candidate pair
for the two absent targets.

**Result:** PASS.

## 4. Suffix closure and scope

Every displayed target prefix ends at height four.  A Dyck suffix read from
that height contributes no eligible inverse-test positions, so both absence
and presence persist.  Distinct suffixes give distinct roots and targets.

The theorem does not claim that one wrapper preserves complete q2 support;
it explicitly records the negative unit-load targets in the beta current.
It therefore proves mobility, not completion.

**Result:** PASS.

**Overall verdict:** PASS.
