# Independent audit of the controlled-leave residual coordinate obstruction

Date: 2026-08-01  
Audited files:

* `MATH_THEOREM_CATALAN_CONTROLLED_LEAVE_PACKET_BANK_AND_BALANCED_RESIDUAL_FOREST_GATE_20260801.md`;
* `MATH_THEOREM_CATALAN_CONTROLLED_LEAVE_RESIDUAL_COORDINATE_COCYCLE_NOGO_20260801.md`.

Verdict: **PASS for the packet construction, residual counts and local
degree/codegree estimates; FAIL for the proposed balanced residual matching.
The new coordinate-cocycle no-go is exact and precedes topology.**

## 1. Residual scalar ledger

Each of the `C` packets reserves two upper resources, two lower resources,
four slots at its two old physical endpoints, and two slots at its two new
endpoints.  The packet-bank injectivity theorem makes these resources
distinct.  Therefore the residual counts are exactly

\[
 U-2C,qquad W-2C,qquad 2W-6C=2(U-2C)                           \tag{1.1}
\]

on upper, lower and owner-slot resources.  An upper/slot-saturating matching
would have `U-2C` edges and leave exactly `C` residual lowers unused.

## 2. Coordinate conservation

For one selected physical diamond with lower intersection `K`, upper union
`R` and middle owners `T,H`, direct membership gives

\[
 {\bf1}_{t\in T}+{\bf1}_{t\in H}
 ={\bf1}_{t\in K}+{\bf1}_{t\in R}                               \tag{2.1}
\]

for every coordinate `t`.  Summing proves that any exact residual matching
would force its unused lower family to have coordinate loads

\[
 h_t=|\mathcal L'_t|+|\mathcal U'_t|-|\mathcal S'_t|.            \tag{2.2}
\]

The full unpunctured layers contribute `-2c` to (2.2), since

\[
 {2m-2\choose m-1}-{2m-2\choose m-2}
   =\operatorname {Cat}_{m-1}=c.                                \tag{2.3}
\]

## 3. Packet contribution and contradiction

One controlled packet reserves upper resources `azL,azV`, lower resources
`aS,L`, and slot multiset

\[
                         2[aL]+2[azS]+[aV]+[zL].                  \tag{3.1}
\]

Adding deleted-slot incidences and subtracting deleted outer incidences
reduces literally to

\[
                         2[a]+[z]+[S]+[L].                       \tag{3.2}
\]

Thus a `C`-packet bank forces

\[
 h_a=2C-2c,qquad h_z=C-2c,qquad
 h_t=-2c+d_P(t;S)+d_P(t;L)quad(t\in G).                         \tag{3.3}
\]

The `beta` target cancels, so spreading, derangement and slot labels cannot
alter this row.  Since

\[
 {C\over c}={2(2m-1)\over m+1}>2\qquad(m>2),                    \tag{3.4}
\]

equation (3.3) requires more than all `C` unused lowers to contain `a`.
This is impossible.

Equivalently, the residual matching would require `C-2c` more distinct
lower resources avoiding `a` than exist.  This is an exact capacity/Hall
row, not a probabilistic or graphic obstruction.

The total-coordinate check passes:

\[
                         \sum_t h_t=(m-1)C,                       \tag{3.5}
\]

so the failure is distributional rather than scalar.

## 4. Deficiency floor

If a residual matching has `d` fewer edges than the residual upper count,
let `u_a` count unmatched uppers containing `a` and `s_a` unused slots over
owners containing `a`.  The same identity gives

\[
 h_a=2C-2c+s_a-u_a.                                              \tag{4.1}
\]

There are only `C+d` unused lowers, while `u_a<=d` and `s_a>=0`; hence

\[
                         C-2c\le2d.                              \tag{4.2}
\]

This verifies the matching-deficiency floor

\[
                         d\ge\left\lceil{C-2c\over2}\right\rceil. \tag{4.3}
\]

## 5. Local expansion audit

The exact residual-star formulas in the source theorem follow directly by
indexing an upper star by its deleted pair, a lower star by its added pair,
and an owner-slot star by one deletion/insertion pair.  The spread-bank
hypergeometric estimates therefore still give

\[
 d_U=2m(m+1)-O(m^2/\log m),qquad
 d_L,d_O=2m(m-1)-O(m^2/\log m).                                  \tag{5.1}
\]

Induced deletion cannot increase pair codegrees, so `Delta_2<=2m` remains
valid.  These estimates support the near-perfect Delcourt--Postle result,
but they cannot imply exact saturation because they do not encode (2.2).

No computation or asymptotic heuristic is used in the no-go proof.
