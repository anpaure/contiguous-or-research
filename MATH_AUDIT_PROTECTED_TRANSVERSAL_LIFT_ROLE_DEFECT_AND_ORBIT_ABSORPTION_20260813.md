# Audit: protected transversal-lift role defect and orbit absorption

**Date:** 2026-08-13  
**Verdict:** **PASS after deleting an invalid draft token-count argument.**
The final theorem contains only the exact protected role formulas, the
rigorous whole-orbit symmetry obstruction, and the exact nonuniform
weighted-core/Hall gate.

**Frozen theorem:**
`MATH_THEOREM_PROTECTED_TRANSVERSAL_LIFT_ROLE_DEFECT_AND_LOCAL_ORBIT_ABSORPTION_OBSTRUCTION_20260813.md`  
**Theorem SHA-256 (H100):**
`9dd8352c8c8705e99153427f3e22f8ee7347bd18d7cba988807b5c1bc7594fc5`

**Verifier:** `verify_protected_transversal_lift_role_defect.py`  
**Verifier SHA-256 (H100):**
`8062809577c463a29226b09f08e2568223961dec8b4e6f77534c43c49ee854de`

**Frozen H100 output SHA-256:**
`1fc70978843ce60599cb409195adf780c2fbe748f5a4cd0cdc040eb56293e21e`

## 1. Protected shore replay

Each physical endpoint of pair `P_i` lies in `2^(p-1)` transversal lower
facets.  Among lifted owners it has that base load plus `h_i/2`: every
direction-`i` transition doubles the pair, and the cyclic transitions split
equally between the two bit values.  The sentinel lies in neither protected
shore.  These facts give exactly

\[
 z_{a_i}=z_{b_i}=2^{p-1},
 \qquad
 y_{a_i}=y_{b_i}=2^{p-1}+h_i/2,
 \qquad y_z=z_z=0.
\]

Subtracting these loads from the owner and lower point equations and then
subtracting the two equations from each other gives

\[
 U_{a_i}=U_{b_i}=W/k-h_i/2,qquad U_z=W/k,
\]

\[
 K_{a_i}=K_{b_i}
 =(R-q)W/k-\bigl(2^{p-1}-(q-1)h_i/2\bigr),
 \qquad K_z=(R-q)W/k.
\]

The total support defect is `2^p`; the weighted-core defect is
`(R-q)2^p`.  Both total-degree ledgers agree with residual period
`W-2^p`.

## 2. Orbit obstruction

A full regular cyclic orbit block translates its base core and support
through all ground points, so both its support-degree and weighted-core
vectors are constant.  Every signed real combination of such blocks remains
constant.  The protected defect is nonconstant: it vanishes at the sentinel
and is positive on every paired coordinate.  Therefore no number of whole
regular orbit blocks, even with signed coefficients or mixed periods, can
implement the protected role correction.

This is a symmetry obstruction only.  It does not rule out breaking orbit
blocks into individual shells or solving a nonuniform flow.

## 3. Rejected draft argument

An earlier draft attempted to lower-bound the number of deleted shell
tokens by the weighted-core defect at one coordinate.  That is false: a
period-`N` shell containing a coordinate in its core contributes `N` units
of weighted core load, not one.  The argument was removed completely before
freezing.  No token-count no-go is claimed.

This hostile correction matters: the remaining exact problem may still
admit a lift-sized nonuniform deletion/replacement bank.  What is proved is
only that it cannot be a union or signed trade of complete cyclic orbits.

## 4. Exact residual flow gate

For chosen residual periods of total `W-2^p`, first select `c`-set cores
with weighted degrees equal to the displayed `K_x`.  For fixed cores, the
core-disjoint supports with sizes `N_j` and point degrees `U_x` exist
exactly when

\[
 \sum_{x\in X}U_x
 \le\sum_j\min\{N_j,|X-C_j|\}
 \qquad(X\subseteq[k]).
\]

This is the ordinary integral capacitated Hall condition.  It isolates the
first nonuniform protected gate.  Solving it still leaves the integral
two-shore named-order equations and their forced owner--facet correlations.

## 5. H100 verifier replay

All script compilation, execution, and hashing were performed through
`ssh h100`; none ran locally after the user directive.  The verifier
returned `PASS` for `(p,q)=(3,2),(5,2),(7,3)`.  It reconstructed the
reflected Gray lift, checked every shore load and residual point equation,
and reproduced:

\[
\begin{array}{c|c|c|c}
(p,q)&(h_i)&\sum d^T&\sum d^C\\\hline
(3,2)&(4,2,2)&8&16\\
(5,2)&(16,8,4,2,2)&32&128\\
(7,3)&(64,32,16,8,4,2,2)&128&640.
\end{array}
\]

The verifier is a finite identity checker, not a solver for the weighted
core sequence, Hall system, or integral named ordering.

## 6. Frozen companion ledger

| Role | File | H100 SHA-256 |
|---|---|---|
| global two-shore cross-bank bridge | `MATH_THEOREM_PAIR_CELL_CROSS_BANK_EMBEDS_IN_TWO_SHORE_OVERLAPPING_CORE_ORDER_FLOW_20260813.md` | `b280d1a8844d62d21e2cc8ff6c2d9aa6373022f58ded50f99d81df64380056be` |
| two-shore bridge audit | `MATH_AUDIT_PAIR_CELL_CROSS_BANK_TO_TWO_SHORE_OVERLAPPING_CORE_ORDER_FLOW_20260813.md` | `c329ff70c24e1896105207c1ae2cc5814ba420288cf4d2344f039a853541ca51` |
| parity/low-cell cross lower bound | `MATH_THEOREM_PAIR_CELL_PARITY_CHARGE_TRIANGLE_AND_EXPONENTIAL_CROSS_EDGE_LOWER_BOUND_20260813.md` | `f89034566a28883910566016cff373166ef80131cba894c44b4e269b6f241f78` |
| hostile parity audit | `MATH_AUDIT_TRANSVERSAL_LIFT_INTERNAL_PARITY_AND_BOUNDED_ABSORBER_HOSTILE_20260813.md` | `353d4185faa51802149d9950ad242eebeebb712398ce3c09af7b16450dd18a83` |

