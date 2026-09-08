# Independent audit of the rigid odd-GK palette-neutral `C10`

**Date:** 2026-08-13  
**Audited file:** `MATH_THEOREM_GK_RIGID_PALETTE_NEUTRAL_C10_FUSION_20260813.md`  
**Audited SHA256:** `2bb672ae98ffc86fcab4140b533cf7281b62e00a6530ecfed688425f040eaee6`  
**Verdict:** **PASS** at the stated scopes: immediate palettes and topology
for `m>=5`, serial phasewise q2 neutrality for `m>=6`.

The only change from the previously audited source was the scope correction
in Section 5: whole-sector selection and the resulting unpunctured outputs
are asserted only for `m>=6`, while no such claim is made at `m=5`.  This is
the correct qualification and does not alter any endpoint, palette, q2, or
topology identity audited below.

## 1. Immediate diamonds and the two hexagons

I independently reconstructed the standard and complement Greene--Kleitman
successors of each word `L_i`.  For every `m>=5`, their unordered pair is
exactly the displayed `{A_i,B_i}`.  The ten owners are distinct.

For the net switch, direct Boolean algebra gives

\[
 B_i\cap A_{i-1}=L_{i-1},\qquad
 B_i\cup A_{i-1}=A_i\cup B_i.                    \tag{1.1}
\]

Thus the five lower colours rotate and each upper colour is restored at
the same role.

Let `c=A_3B_1`.  All nine edges occurring in the two phases are Johnson
edges.  The independently computed lower/upper multisets are

\[
 \{e_1,e_2,e_3\}\longleftrightarrow\{n_2,n_3,c\},\qquad
 \{e_0,e_4,c\}\longleftrightarrow\{n_0,n_1,n_4\}. \tag{1.2}
\]

They agree separately on both sides of each arrow.  The first phase
inserts `c`; the second removes it, so the serial state is a simple
two-factor throughout and the net symmetric difference is exactly the
displayed decagon.

## 2. Independent q2 replay

For each `A_i`, I constructed its other incident factor diamond directly
from the complete GK/complement incidence table; no q2 values were copied
from the theorem.  If its union is `C_i` and the changed diamond has union
`U`, I evaluated

\[
                         q_2(A_i)=\overline{C_i\cup U}.          \tag{2.1}
\]

For `m>=6`, phase one gives

\[
 X_1\mapsto X_2,\qquad X_2\mapsto X_3,
 \qquad X_3\mapsto X_1,                            \tag{2.2}
\]

and phase two, evaluated in the post-phase-one state, gives

\[
 X_0\mapsto X_1,\qquad X_1\mapsto X_4,
 \qquad X_4\mapsto X_0.                            \tag{2.3}
\]

The strings `X_0,...,X_4` are exactly those in the audited note.  At every
changed `B_i`, the transported lower/upper role remains the same, so its
q2 row is pointwise fixed.  Equations (2.2)--(2.3) therefore exhaust all
changed q2 occurrences and prove phasewise multiset neutrality.

The boundary is real.  At `m=5`, phase one instead begins

\[
 01100000001\mapsto00100000011,
\]

so the claimed `X_1->X_2` identity fails.  Phase two still cycles, but the
note correctly does not claim a serial protected theorem at `m=5`.

## 3. Four-to-two topology

Reconstructing the entire factor independently gives the component labels

\[
 E_0:C_0,\quad E_1,E_4:C_1,\quad E_3:C_3,\quad E_2:C_2,             \tag{3.1}
\]

with four distinct old cycles of lengths

\[
 n,\quad n(2m-3),\quad n(2m-5),\quad n(2m-7).       \tag{3.2}
\]

After deleting the five old edges, the exposed path pairing is

\[
 A_0-B_0,\qquad A_1-B_4,\qquad A_4-B_1,
 \qquad A_2-B_2,\qquad A_3-B_3.                    \tag{3.3}
\]

This is precisely the return involution

\[
                         (0)(1\ 4)(2)(3).           \tag{3.4}
\]

Composing (3.4) with the new five-cycle gives two return orbits, hence two
output cycles.  The first hexagon already changes the global component
count by `-2`; the second leaves it unchanged.  The final result is

\[
                         \Delta c=-2,              \tag{3.5}
\]

so four affected input cycles become two outputs.

## 4. Audit boundary

The theorem proves an actual ambient escape from the forced
single-soliton cycle and does so while preserving both immediate palettes
and q2.  It does not puncture the two output cycles, and it proves no q3,
long-residence, history, or typed-cap transport.  The scope language in
the audited note states these limitations correctly.

Lightweight exact replays were made for `m=5,...,20` for all Boolean
identities and for `m=5,...,9` for the complete factor topology.  They are
corroboration; Sections 1--3 are the symbolic proof.
