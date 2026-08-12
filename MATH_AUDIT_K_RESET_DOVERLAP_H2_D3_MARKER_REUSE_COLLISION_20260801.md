# The h=2,d=3 overlap survives, but two-marker reuse does not give a protected twin bank

**Date:** 2026-08-01

**Status:** exact scoped audit and counterexample. The coefficient-one
d-overlap and both Ferrers witness paths remain correct at h=2,d=3.
However, identifying
\[
 \eta _3=\eta _1,\qquad \eta _4=\eta _2
\]
forces one repeated owner and two repeated lower-q1 colours. Thus the
literal four-marker separation theorem, and consequently its 7d/22d or
9d/26d protected-subgraph corollaries, cannot be invoked in this
two-marker realization.

## 1. Parameters and the overlap leave

Let
\[
 H=\{e_1,e_2\},\qquad d=3,\qquad r=h+2d+1=9,\qquad M=4d+2=14.
\]
Use the packet antecedent \(A_0,\ldots,A_{13}\) from
MATH_THEOREM_RESET_RETURN_DOVERLAP_AND_UPPER_FERRERS_TWIN_BANK_20260801.md.
Exact enumeration gives
\[
 \operatorname {Deck}_{\rm cyc}(A)
 \setminus
 \operatorname {Deck}(A_{11},A_{12},A_{13},A_0,\ldots,A_{13})
 =
 \mathcal Z_X\mathbin{\dot\cup}\mathcal Z_U
\]
with the following histogram.

| family | rank | multiplicity |
|---|---:|---:|
| \(\mathcal Z_X\) | 10 | 1 |
| \(\mathcal Z_X\) | 11 | 2 |
| \(\mathcal Z_X\) | 12 | 3 |
| \(\mathcal Z_U\) | 13 | 1 |
| \(\mathcal Z_U\) | 14 | 2 |
| \(\mathcal Z_U\) | 15 | 3 |

Hence the leave still consists of exactly twelve upper targets and contains
no lower or middle target. This part of the theorem does not use four
distinct markers.

## 2. What remains valid after marker reuse

Set
\[
 \eta _1=\eta _3=e_1,\qquad \eta _2=\eta _4=e_2.
\]
Construct \(\mathcal P_X\) and \(\mathcal P_U\) by the frozen formulas.
Separately:

* \(\mathcal P_X\) is a six-owner Johnson path with five distinct lower and
  five distinct upper q1 colours;
* \(\mathcal P_U\) is a nine-owner Johnson path with eight distinct lower
  and eight distinct upper q1 colours;
* neither path has an internal positive run shorter than \(d+1=4\);
* \(\mathcal P_X\) witnesses all six members of \(\mathcal Z_X\), and
  \(\mathcal P_U\) witnesses all six members of \(\mathcal Z_U\);
* each bank is owner/q1-disjoint from the opened packet.

Thus target coverage, internal residence, and the bank-versus-packet
separation survive. The failure is exactly in the interaction between the
two banks.

## 3. Exact cross-bank collision table

Write
\[
 B_X=H\cup C\cup Y\cup\{\alpha,\delta\}.
\]
The complete cross-bank collision census is:

| resource | \(\mathcal P_X\) occurrence | \(\mathcal P_U\) occurrence | common value |
|---|---|---|---|
| owner | \(L_0\) | \(M_4\) | \(B_X\setminus\{e_1\}\) |
| lower q1 | \(L_0R_0\) | \(M_3M_4\) | \(B_X\setminus\{e_1,e_2\}\) |
| lower q1 | \(L_1L_0\) | \(M_4S_1\) | \(B_X\setminus\{e_1,c_1\}\) |

In literal coordinate notation,
\[
\begin{aligned}
 L_0=M_4
   &=\{e_2,c_1,c_2,c_3,y_1,y_2,y_3,\alpha,\delta\},\\
 L_0\cap R_0=M_3\cap M_4
   &=\{c_1,c_2,c_3,y_1,y_2,y_3,\alpha,\delta\},\\
 L_1\cap L_0=M_4\cap S_1
   &=\{e_2,c_2,c_3,y_1,y_2,y_3,\alpha,\delta\}.
\end{aligned}
\]
There is no cross-bank upper-q1 collision. There is also no bank-packet
owner, lower-q1, or upper-q1 collision.

These collisions are structural. With \(H=\{e_1,e_2\}\),
\[
 M_{d+1}
  =(C\cup\{\alpha,\delta\})\cup Y\cup\{e_2\}
  =B_X\setminus\{e_1\}=L_0.
\]
The first repeated lower colour follows by intersecting the adjacent
owners, and the second follows from
\[
 S_1=(M_{d+1}\setminus\{c_1\})\cup\{u_d\}.
\]
Thus this literal obstruction already exists for every \(d\ge2\) under
the same two-marker identification. The claim that these are the only
collisions is made here only for \(d=3\).

## 4. Exact ledger and scope

For the opened packet plus both banks, the occurrence/distinct counts are

| resource | occurrences | distinct |
|---|---:|---:|
| owners | 29 | 28 |
| lower q1 colours | 26 | 24 |
| upper q1 colours | 26 | 26 |

Consequently the two banks are not a disjoint protected path forest. The
shared owner is incident with both paths, and the two repeated lower
vertices receive repeated incidences. The fixed-protected-subgraph theorem
used in the collar corollary therefore does not apply to this realization.

The corrected global scope is:

* 7d collared bank owners and the m>=22d incidence bound are conditional,
  even with four distinct markers: two exterior bank ends must be certified
  global ends or supplied with nested ambient continuations;
* 9d collared bank owners and m>=26d are the unconditional four-collar
  ledger, assuming the four-marker owner/q1 separation;
* at h=2, direct marker reuse satisfies neither protected ledger. A
  separate collision repair or a different bank construction is necessary
  before either bound can be used.

This audit does not rule out a repaired h=2 construction. It rules out only
the literal identification
\(\eta _3=\eta _1,\eta _4=\eta _2\) in the frozen two-bank formulas.

## 5. Reproducer

The tiny exact audit is

    scratch/audit_k_h2_d3_twin_bank_marker_reuse_20260801.py

It reconstructs the packet, overlap deck, both paths, all owner/q1
palettes, interval witnesses, and internal positive runs directly from the
displayed formulas. Its SHA-256 is

    779cde167f1e796212f6314170364c77399bf705667eed40c2dd5bf922ad738e
